#!/usr/bin/env python3
"""NVIDIA NIM benchmark — model discovery from build.nvidia.com + tests for
chat, embeddings and reranking endpoints.

Usage:
  python benchmark.py                     # run all models from models.json (resume)
  python benchmark.py --refresh           # re-fetch model list from build.nvidia.com
  python benchmark.py --modelgrep emb     # only test models whose id/label/desc match this regex
  python benchmark.py --restart           # delete results.json first
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
import warnings
from openai import OpenAI

BASE = os.path.dirname(os.path.abspath(__file__))
# Load .env for NVIDIA_API_KEY
env_path = os.path.join(BASE, ".env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and "=" in line and not line.startswith("#"):
                k, v = line.strip().split("=", 1)
                os.environ.setdefault(k, v.strip())

# Configuration lives in .env (template: .env.example); values below are fallbacks.
# Relative paths are resolved against the project directory.
BUILD = os.getenv("BUILD") or "https://build.nvidia.com"
API = os.getenv("API") or "https://integrate.api.nvidia.com/v1"
MODELS_FILE = os.path.join(BASE, os.getenv("MODELS_FILE") or "models.json")
RESULTS_FILE = os.path.join(BASE, os.getenv("RESULTS_FILE") or "results.json")
CACHE = os.path.join(BASE, os.getenv("CACHE") or "mdcache")  # caches downloaded .md pages
KEY = os.getenv("NVIDIA_API_KEY", "")

PROMPT = os.getenv("PROMPT") or "What is the capital of India? Please answer in one sentence."
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT") or 120)  # per request; free-tier cold starts measured at 88s
CHAT_PAUSE = int(os.getenv("CHAT_PAUSE") or 12)   # pause after chat (rate limit on free tier)
OTHER_PAUSE = int(os.getenv("OTHER_PAUSE") or 3)  # pause after embeddings/ranking
RETRY_BACKOFF = int(os.getenv("RETRY_BACKOFF") or 30)

# max_retries=0: attempt() does one controlled retry (backoff + full timeout),
# so a hanging model costs 2x REQUEST_TIMEOUT instead of 6x.
client = OpenAI(base_url=API, api_key=KEY, timeout=REQUEST_TIMEOUT, max_retries=0)
GRN = "\033[92m"; RED = "\033[91m"; YLW = "\033[93m"; RST = "\033[0m"

# ----------------------------------------------------------------------
#  HTTP utilities (simple, resilient)
# ----------------------------------------------------------------------
def fetch_url(url, dest_path=None, retries=2):
    """GET url; save to dest_path if provided; return decoded text.
    Uses the same headers as a modern browser to avoid 403/429.
    """
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            if dest_path:
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                with open(dest_path, "wb") as f:
                    f.write(data)
            return data.decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code in (403, 429, 500) and attempt < retries:
                wait = (2 ** attempt) * 10
                time.sleep(wait)
                continue
            raise
        except Exception as e:
            if attempt < retries:
                time.sleep(2 ** attempt)
                continue
            raise

# ----------------------------------------------------------------------
#  Discovery from build.nvidia.com
# ----------------------------------------------------------------------
def ensure_cache():
    """Ensure the cache directory exists."""
    os.makedirs(CACHE, exist_ok=True)


def extract_rel_links(markdown):
    """Return list of relative hrefs from build.nvidia.com markdown index.
    Pattern: - [title](/tenant/model.md) — description.
    """
    return re.findall(r"\[([^\]]+)\]\(/([a-z0-9_-]+/[a-zA-Z0-9._%+-]+\.md)\) — (.+)", markdown)


def page_of_models():
    """Get models.md index (first + subsequent pages) and return list of (title, rel, desc).
    The pagination footer is e.g. "_100 of 109 shown. Fetch /models.md?page=2 for the next 100._"
    """
    items = []
    page = "models.md"
    while page:
        txt = fetch_url(f"{BUILD}/{page}", dest_path=os.path.join(CACHE, page.replace("/", "__")))
        for title, rel, desc in extract_rel_links(txt):
            items.append((title, rel, desc.strip()))
        # Detect next page link
        m = re.search(r"Fetch /models\.md\?page=(\d+)", txt)
        page = f"models.md?page={m.group(1)}" if m else None
    return items


def model_id_from_md(md_text, rel):
    """Extract canonical model ID from front-matter.
    Front-matter format (YAML block between ---):
    title: "..."
    publisher: "..."
    canonical: "https://build.nvidia.com/<pub>/<name>"
    """
    # Find canonical URL if present
    m = re.search(r'canonical:\s*"?(https://build\.nvidia\.com/([^\s\""]+))', md_text)
    if m:
        canonical = m.group(1).split("?")[0].rstrip("/")
        # strip prefix https://build.nvidia.com/
        after = canonical[len("https://build.nvidia.com/"):]
        # remove any escaped slashes or weird characters
        model_id = after.replace("\\", "")
        return model_id
    # Fallback to publisher/title
    pub_m = re.search(r'publisher:\s*"?([^\n\"]+)', md_text)
    title_m = re.search(r'title:\s*"?([^\n\"]+)', md_text)
    if pub_m and title_m:
        return f"{pub_m.group(1).strip()}/{title_m.group(1).strip()}"
    # Fallback to slug from rel path (remove .md)
    return rel.replace(".md", "")


def classify_task(md_text, model_id, callable_ids):
    """Determine the endpoint task based on code snippets inside the .md.
    Priority: ranking > embeddings > chat > other.
    Detection via plain text (curl, client.*, /v1/* URLs) – exact matches.
    """
    md_low = md_text.lower()
    if "embed" in model_id:
        return "embeddings"
    if "v1/ranking" in md_low or "ranking" in md_low or "rerank" in md_low or "client.post.*/ranking" in md_low or ".ranking" in md_low:
        return "ranking"
    if "v1/embeddings" in md_low or ".embeddings.create" in md_low:
        return "embeddings"
    if "v1/chat/completions" in md_low or ".chat.completions.create" in md_low:
        return "chat"
    return "other"


def is_vision_only(md_text, title, desc):
    """Vision-only models (e.g. nemotron-parse) reject plain-text prompts.
    They cannot be benchmarked with a text prompt — mark as vision_only so dispatch skips them.
    """
    combined = (title + " " + desc + " " + md_text).lower()
    vision_keywords = ["image", "vision", "document", "ocr", "parse", "visual", "vision-language", "vision language"]
    text_keywords = ["text", "chat", "conversation", "dialogue", "llm"]
    has_vision = any(k in combined for k in vision_keywords)
    has_text = any(k in combined for k in text_keywords)
    return has_vision and not has_text


# Chat models that reject plain-text prompts (vision/document-only input)
VISION_ONLY_CHAT_IDS = {
    "nvidia/nemotron-parse",
    "nvidia/nemotron-parse-2.0",
}


def refresh():
    """Build models.json from build.nvidia.com.
    Downloads index page and all per-model .md pages (cached), classifies each model,
    and records which IDs are callable with the current key (free endpoint trial).
    """
    ensure_cache()
    print("🔄 fetching model index from build.nvidia.com …")
    index_items = page_of_models()
    callable_ids = set()
    # fetch /v1/models list once to know which IDs are available
    try:
        callable_ids = {m.id for m in client.models.list().data if getattr(m, "id", None)}
    except Exception as e:
        print(f"⚠️  could not fetch /v1/models: {e}")

    out = []
    total = len(index_items)
    seen_rels = set()
    for i, (title, rel, desc) in enumerate(index_items, 1):
        if rel in seen_rels:
            continue
        seen_rels.add(rel)
        # Fetch markdown file (cached)
        md_path = os.path.join(CACHE, rel.replace("/", "__"))
        try:
            md = fetch_url(f"{BUILD}/{rel}", dest_path=md_path) if not os.path.exists(md_path) else open(md_path, encoding="utf-8").read()
        except Exception:
            md = ""
        model_id = model_id_from_md(md, rel) if md else rel.replace(".md", "")
        task = classify_task(md, model_id, callable_ids) if md else "other"
        vision_only = is_vision_only(md, title, desc) if md else False
        out.append({
            "id": model_id,
            "label": title,
            "task": task,
            "desc": desc,
            "api_ok": model_id in callable_ids,
            "vision_only": vision_only,
        })
        print(f"  [{i}/{total}] {model_id}  → {task}  callable={model_id in callable_ids}")

    # Write models.json sorted by id for deterministic runs
    with open(MODELS_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(out, key=lambda x: x["id"]), f, indent=2, ensure_ascii=False)
    print(f"✓ wrote {len(out)} models to {MODELS_FILE}")

# ----------------------------------------------------------------------
#  Benchmark test implementations
# ----------------------------------------------------------------------
def run_chat(mid):
    start = time.perf_counter()
    stream = client.chat.completions.create(
        model=mid,
        messages=[{"role": "user", "content": PROMPT}],
        temperature=0.0,
        max_tokens=700,
        stream=True,
    )
    first = None
    full = ""
    n = 0
    for chunk in stream:
        if not getattr(chunk, "choices", None):
            continue
        delta = chunk.choices[0].delta
        text = getattr(delta, "content", None) if delta else None
        if text:
            if first is None:
                first = time.perf_counter()
            full += text
            n += 1
    elapsed = time.perf_counter() - start
    ttft = first - start if first else None
    return {
        "status": "ok" if n else "empty",
        "total_time_s": round(elapsed, 3),
        "tokens": n,
        "tokens_per_second": round(n / elapsed, 2) if n else 0,
        "ttft_s": round(ttft, 3) if ttft else None,
        "response_preview": full[:120],
    }


def run_embeddings(mid):
    start = time.perf_counter()
    try:
        r = client.embeddings.create(model=mid, input=[PROMPT])
    except Exception as e:
        # Asymmetric models (e.g. llama-nemotron-embed-vl-1b-v2) require input_type
        if "400" in str(e) or "input_type" in str(e):
            r = client.embeddings.create(
                model=mid, input=[PROMPT], extra_body={"input_type": "query"}
            )
        else:
            raise
    elapsed = time.perf_counter() - start
    return {
        "status": "ok",
        "total_time_s": round(elapsed, 3),
        "dim": len(r.data[0].embedding),
    }


def run_ranking(mid):
    body = {
        "model": mid,
        "query": {"text": "What is the capital of India?"},
        "passages": [
            {"text": "New Delhi is the capital of India."},
            {"text": "Bengaluru is a major IT hub in southern India."},
            {"text": "CN Tower is a landmark in Toronto, Canada."},
        ],
    }
    start = time.perf_counter()
    import urllib.request, json as json_mod
    req = urllib.request.Request(
        f"{API}/ranking",
        data=json_mod.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            data = json_mod.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"status": "skipped", "error": "ranking endpoint not available on free tier (404)"}
        raise
    elapsed = time.perf_counter() - start
    # Extract scores (list of floats) from common shapes
    scores = []
    if "results" in data and isinstance(data["results"], list):
        for item in data["results"]:
            if isinstance(item, dict) and "logit" in item:
                scores.append(float(item["logit"]))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (int, float)):
                scores.append(float(item))
    return {
        "status": "ok",
        "total_time_s": round(elapsed, 3),
        "scores": scores,
        "response_preview": json.dumps(data)[:300],
    }

RUN = {"chat": run_chat, "embeddings": run_embeddings, "ranking": run_ranking}
ORDER = {"chat": ["chat"], "embeddings": ["embeddings"], "ranking": ["ranking"]}
RETRY_RE = re.compile(r"429|timed?-? ?out|connection|read timeout", re.I)


def attempt(kind, mid):
    """Run a single benchmark kind (chat/embeddings/ranking) with simple retry on transient errors."""
    try:
        return RUN[kind](mid)
    except Exception as e:
        msg = str(e)
        if RETRY_RE.search(msg):
            print(f"   {RED}[{kind}] transient error, backoff {RETRY_BACKOFF}s and retrying once …{RST}")
            time.sleep(RETRY_BACKOFF)
            try:
                return RUN[kind](mid)
            except Exception as e2:
                return {"status": "error", "error": f"{kind}: {msg[:130]} / retry: {str(e2)[:130]}"}
        return {"status": "error", "error": f"{kind}: {msg[:160]}"}


def dispatch(model):
    """Try the appropriate kinds for the model's task; unknown tasks get best-effort attempts."""
    mid, task = model["id"], model.get("task", "unknown")
    base = {"id": mid, "label": model["label"], "task": task}
    # Skip testing for "other" models (video/audio/pose etc.) – they are not OpenAI‑compatible.
    if task == "other":
        return {**base, "status": "skipped", "error": "no OpenAI‑compatible endpoint found"}
    # Vision-only chat models (e.g. nemotron-parse) reject plain-text prompts
    if mid in VISION_ONLY_CHAT_IDS:
        return {**base, "status": "skipped", "error": "vision-only model — cannot benchmark with text prompt"}

    errors = []
    for kind in ORDER.get(task, ["chat", "embeddings", "ranking"]):
        r = attempt(kind, mid)
        if r["status"] != "error":
            return {**base, **r}
        errors.append(r["error"])
    # All attempts failed
    return {**base, "status": "error", "error": "; ".join(errors)[:300], "tokens_per_second": 0}

# ----------------------------------------------------------------------
#  Main CLI flow
# ----------------------------------------------------------------------
def print_server_hint():
    """Tell the user how to open the web UI."""
    print("\nStart the web UI:")
    print("  python -m http.server 8000")
    print("  -> http://localhost:8000/visualize.html")


def main():
    parser = argparse.ArgumentParser(description="NVIDIA NIM benchmark (chat/embeddings/ranking)")
    parser.add_argument("--refresh", action="store_true", help="re‑fetch model list from build.nvidia.com")
    parser.add_argument("--modelgrep", metavar="REGEX", help="only test models whose id/label/desc match this regex")
    parser.add_argument("--restart", action="store_true", help="delete results.json first")
    parser.add_argument("--no-ai-rating", action="store_true", help="skip the AI rating at the end")
    parser.add_argument("--judge", help="judge model for the AI rating (default: AI_JUDGE_MODEL or meta/muse-glimmer-30b)")
    args = parser.parse_args()

    if args.refresh:
        refresh()
        return

    if not os.path.exists(MODELS_FILE):
        sys.exit(f"models.json not found — run with --refresh first")

    models = json.load(open(MODELS_FILE, encoding="utf-8"))
    if args.modelgrep:
        try:
            rx = re.compile(args.modelgrep, re.I)
        except re.error as e:
            sys.exit(f"--modelgrep: invalid regex: {e}")
        models = [
            m for m in models
            if rx.search(" ".join(str(m.get(k, "")) for k in ("id", "label", "desc")))
        ]
    if not models:
        sys.exit("no models matched the filters")
    # Only test endpoint-compatible tasks (skip video/audio/pose etc.)
    models = [m for m in models if m.get("task") in ("chat", "embeddings", "ranking")]

    # Resume logic
    if args.restart and os.path.exists(RESULTS_FILE):
        os.remove(RESULTS_FILE)
    if os.path.exists(RESULTS_FILE):
        results = json.load(open(RESULTS_FILE, encoding="utf-8"))
    else:
        results = []
    # Resume logic: retry models that previously failed — timeouts/429s are transient,
    # not a verdict on the model. Old failed entries are dropped, the new result replaces them.
    failed = {r["id"] for r in results if r.get("status") in ("error", "empty")}
    if failed:
        results = [r for r in results if r["id"] not in failed]
    done_ids = {r["id"] for r in results}
    print(f"\n{len(models)} models scheduled — {len(done_ids)} already in {RESULTS_FILE} (resume)\n")

    for idx, model in enumerate(models, 1):
        mid = model["id"]
        task = model.get("task", "unknown")
        if mid in done_ids:
            print(f"  [{idx}/{len(models)}] {mid:47} already done ({task})")
            continue
        print(f"\n→ [{task}] {model['label']}  ({mid})")
        result = dispatch(model)
        results.append(result)
        with open(RESULTS_FILE, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        # Human‑friendly output
        if result["status"] == "ok":
            if result.get("task") == "chat":
                print(f"    {GRN}{result['tokens']} tok  {result['tokens_per_second']} tok/s  ttft {result['ttft_s']}s  total {result['total_time_s']}s{RST}   \"{result.get('response_preview','')[:60]}\"")
            elif result.get("task") == "embeddings":
                print(f"    {GRN}{result['total_time_s']}s{RST}  dim={result.get('dim', '?')}  {result.get('response_preview','')[:120]}")
            else:  # ranking
                scores = result.get("scores", [])
                print(f"    {GRN}{result['total_time_s']}s{RST}  scores={scores[:3]}  {result.get('response_preview','')[:120]}")
        else:
            color = YLW if result.get("status") == "skipped" else RED
            label = "SKIPPED" if result.get("status") == "skipped" else result["status"].upper()
            print(f"    {color}{label}{RST}: {(result.get('error') or '')[:130]}")
        # Respect rate limits
        if result["status"] == "ok" and result.get("task") == "chat":
            time.sleep(CHAT_PAUSE)
        else:
            time.sleep(OTHER_PAUSE)

    # ---- summary ----
    ok = [r for r in results if r["status"] == "ok"]
    chat_ok = sorted([r for r in ok if r.get("task") == "chat"], key=lambda x: -x["tokens_per_second"])
    embed_ok = sorted([r for r in ok if r.get("task") == "embeddings"], key=lambda x: x["total_time_s"])
    rank_ok = sorted([r for r in ok if r.get("task") == "ranking"], key=lambda x: x["total_time_s"])
    print(f"\n=== Summary ({len(results)-len(ok)} errors / {len(ok)} successes) ===")
    if chat_ok:
        print("\nTop‑10 chat models (tokens / s):")
        for r in chat_ok[:10]:
            print(f"  {r['tokens_per_second']:7.1f} tok/s  ttft {r['ttft_s']}s  {r['id']}")
    if embed_ok:
        print("\nFastest 10 embeddings (latency s / dim):")
        for r in embed_ok[:10]:
            print(f"  {r['total_time_s']:7.3f}s  dim={r.get('dim')}  {r['id']}")
    if rank_ok:
        print("\nFastest 10 rerankers (latency s / scores):")
        for r in rank_ok[:10]:
            scores = r.get("scores", [])
            print(f"  {r['total_time_s']:7.3f}s  scores={scores[:3]}  {r['id']}")

    # ---- AI rating (judge model via the same NVIDIA API) ----
    if not args.no_ai_rating:
        print("\n=== AI rating (top 3 per category) ===")
        try:
            import ai_rating
            ai_rating.rate(results, judge=args.judge)
        except Exception as e:
            print(f"{YLW}AI rating skipped: {type(e).__name__}: {str(e)[:160]}{RST}")
            print("  Run separately:  python ai_rating.py --judge <model>")

    print_server_hint()


if __name__ == "__main__":
    main()
