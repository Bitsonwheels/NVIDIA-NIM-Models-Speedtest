#!/usr/bin/env python3
"""AI model rating via the NVIDIA NIM API.

Ranks the models that were reachable in the benchmark (and actually delivered
output) into a top 3 per category — Coding and Embedding — using a judge model. 
The judge only sees model ids and labels, never benchmark
measurements (tok/s, latency, dimension), so the ranking is independent of the
measured values.

Usage:
  python ai_rating.py                 # rate all categories -> ai_ratings.json
  python ai_rating.py --judge MODEL   # use another judge model
  python ai_rating.py --prepare       # only write the prompts (manual fallback)
  python ai_rating.py --selftest      # offline self-check
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
if BASE not in sys.path:
    sys.path.insert(0, BASE)
import benchmark  # reuse API base, key, client and results path

# Configuration lives in .env (template: .env.example); values below are fallbacks.
RESULTS_FILE = benchmark.RESULTS_FILE
RATINGS_FILE = os.path.join(BASE, os.getenv("RATINGS_FILE") or "ai_ratings.json")
PROMPTS_FILE = os.path.join(BASE, os.getenv("PROMPTS_FILE") or "ai_rating_prompts.json")

JUDGE_MODEL = os.getenv("AI_JUDGE_MODEL") or "meta/muse-glimmer-30b"
JUDGE_TIMEOUT = int(os.getenv("JUDGE_TIMEOUT") or 180)
JUDGE_PAUSE = int(os.getenv("JUDGE_PAUSE") or 5)  # free-tier rate limit between judge calls

# Benchmark task -> rating category. Swap the task here to change the mapping.
CATEGORIES = {
    "coding": {"label": "Coding", "task": "chat"},
    "embedding": {"label": "Embedding", "task": "embeddings"},
}


# ----------------------------------------------------------------------
#  Which models are rated
# ----------------------------------------------------------------------
def delivered(result):
    """True if the model was reachable and actually delivered output."""
    if result.get("status") != "ok":
        return False
    task = result.get("task")
    if task == "chat":
        return (result.get("tokens") or 0) > 0
    if task == "embeddings":
        return (result.get("dim") or 0) > 0
    return True  # ranking: endpoint answered successfully


def candidates(results):
    """Group eligible models per category: {category: [{"id", "label"}]}."""
    out = {cat: [] for cat in CATEGORIES}
    for r in results:
        cat = next((c for c, m in CATEGORIES.items() if m["task"] == r.get("task")), None)
        if cat and delivered(r):
            out[cat].append({"id": r["id"], "label": r.get("label") or r["id"]})
    return out


def build_prompt(label, models):
    """Prompt for the judge. Contains only model ids/labels — no measurements."""
    listing = "\n".join(f"- {m['id']} ({m['label']})" for m in models)
    return (
        f"You are an independent jury for AI models. Rate the following {label} models "
        "purely on your expert knowledge of model quality, fit for the task "
        f'"{label}" and practical usefulness. Speed, latency or benchmark measurements are '
        "deliberately not available to you and must not influence the rating.\n\n"
        f"Models:\n{listing}\n\n"
        f'Pick the best 3 models for the task "{label}" (fewer if fewer models are available — '
        "do not invent models).\n\n"
        "Answer with JSON only (no markdown, no extra text) in exactly this form:\n"
        '{"ranking": [{"rank": 1, "model": "<model id>", "reason": "<reason in English, max 2 sentences>"}, '
        '{"rank": 2, "model": "<Model-ID>", "reason": "..."}, {"rank": 3, "model": "<Model-ID>", "reason": "..."}]}'
    )


def parse_answer(text, models):
    """Extract the top 3 from the judge's answer.

    Only models that were actually benchmarked are kept — names the judge
    invented or repeated are dropped.
    """
    raw = text or ""
    start, end = raw.find("{"), raw.rfind("}")
    data = None
    if start != -1 and end > start:
        try:
            data = json.loads(raw[start:end + 1])
        except json.JSONDecodeError:
            data = None
    items = (data or {}).get("ranking") or []
    by_id = {m["id"].lower(): m for m in models}
    by_label = {m["label"].lower(): m for m in models}
    top, seen = [], set()
    for item in items:
        if len(top) >= 3:
            break
        item = item if isinstance(item, dict) else {}
        name = str(item.get("model", "")).strip()
        match = by_id.get(name.lower()) or by_label.get(name.lower())
        if not match or match["id"] in seen:
            continue  # not benchmarked or already ranked
        seen.add(match["id"])
        top.append({
            "rank": len(top) + 1,
            "model": match["id"],
            "label": match["label"],
            "reason": str(item.get("reason", "")).strip(),
        })
    return top


# ----------------------------------------------------------------------
#  Judge model (NVIDIA NIM API, same key as the benchmark)
# ----------------------------------------------------------------------
def ask(prompt, judge, max_tokens):
    """One judge call; returns the raw answer ("" on failure)."""
    client = benchmark.client.with_options(timeout=JUDGE_TIMEOUT, max_retries=1)
    kwargs = dict(model=judge, messages=[{"role": "user", "content": prompt}],
                  temperature=0.2, max_tokens=max_tokens)
    try:
        r = client.chat.completions.create(response_format={"type": "json_object"}, **kwargs)
    except Exception:
        r = client.chat.completions.create(**kwargs)  # model rejects response_format
    return r.choices[0].message.content or ""


def judge_answer(prompt, models, judge):
    """Ask until a parsable top 3 comes back; returns (raw, top3)."""
    raw, top = "", []
    for max_tokens in (1500, 3000):  # 2nd try: reasoning models need more room
        try:
            raw = ask(prompt, judge, max_tokens)
        except Exception as e:
            print(f"  ✗ Judge {judge}: {type(e).__name__}: {str(e)[:160]}")
            break
        top = parse_answer(raw, models)
        if top:
            break
    return raw, top


# ----------------------------------------------------------------------
#  Entry points
# ----------------------------------------------------------------------
def load_results():
    if not os.path.exists(RESULTS_FILE):
        sys.exit(f"results.json not found — run 'python benchmark.py' first")
    with open(RESULTS_FILE, encoding="utf-8") as f:
        return json.load(f)


def rate(results, judge=None):
    """Ask the judge for a top 3 per category and write ai_ratings.json."""
    judge = judge or JUDGE_MODEL
    if not benchmark.KEY:
        sys.exit("NVIDIA_API_KEY is missing — set it in .env")
    cats = candidates(results)
    todo = {c: m for c, m in cats.items() if m}
    for cat, meta in CATEGORIES.items():
        if not todo.get(cat):
            print(f"  – {meta['label']}: no reachable models")
    if not todo:
        print("No eligible models — AI rating skipped.")
        return None

    print(f"Judge {judge} is rating {len(todo)} categories …")
    answers = {}
    for cat, models in todo.items():
        prompt = build_prompt(CATEGORIES[cat]["label"], models)
        raw, top = judge_answer(prompt, models, judge)
        answers[cat] = (raw, top)
        if top:
            print(f"  ✓ {CATEGORIES[cat]['label']}: {len(top)} models rated")
        else:
            print(f"  ✗ {CATEGORIES[cat]['label']}: no answer")
        time.sleep(JUDGE_PAUSE)

    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source": f"NVIDIA API ({judge})",
        "categories": {},
    }
    for cat, meta in CATEGORIES.items():
        models = todo.get(cat, [])
        raw, top = answers.get(cat, ("", []))
        if not models:
            error = "no reachable models in the benchmark"
        elif not top:
            error = "no usable answer from the judge model"
        else:
            error = ""
        payload["categories"][cat] = {
            "label": meta["label"],
            "candidates": models,
            "top3": top,
            "raw": raw,
            "error": error,
        }
    with open(RATINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"✓ wrote {RATINGS_FILE}")
    return payload


def prepare(results):
    """Write the prompts so they can be answered manually."""
    cats = candidates(results)
    prompts = {c: build_prompt(CATEGORIES[c]["label"], m) for c, m in cats.items() if m}
    with open(PROMPTS_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, indent=2, ensure_ascii=False)
    print(f"✓ wrote {len(prompts)} prompts to {PROMPTS_FILE}")
    for cat, prompt in prompts.items():
        print(f"\n===== {cat} =====\n{prompt}")


def selftest():
    sample = [
        {"id": "a/chat1", "label": "chat1", "task": "chat", "status": "ok", "tokens": 5},
        {"id": "a/chat2", "label": "chat2", "task": "chat", "status": "ok", "tokens": 0},
        {"id": "a/chat3", "label": "chat3", "task": "chat", "status": "error"},
        {"id": "a/chat4", "label": "chat4", "task": "chat", "status": "ok", "tokens": 1},
        {"id": "a/emb1", "label": "emb1", "task": "embeddings", "status": "ok", "dim": 1024},
        {"id": "a/emb2", "label": "emb2", "task": "embeddings", "status": "ok", "dim": 0},
        {"id": "a/rank1", "label": "rank1", "task": "ranking", "status": "ok", "scores": [1.0]},
        {"id": "a/rank2", "label": "rank2", "task": "ranking", "status": "skipped"},
    ]
    cats = candidates(sample)
    assert [m["id"] for m in cats["coding"]] == ["a/chat1", "a/chat4"], cats["coding"]
    assert [m["id"] for m in cats["embedding"]] == ["a/emb1"], cats["embedding"]
    assert "ranking" not in cats, cats  # rerank is not a rating category

    prompt = build_prompt("Coding", cats["coding"])
    for leak in ("tokens_per_second", "tok/s", "total_time_s", "ttft", "dim"):
        assert leak not in prompt, f"prompt leaks measurement '{leak}'"
    assert "a/chat1" in prompt and "a/chat4" in prompt

    top = parse_answer(
        '```json\n{"ranking": [{"rank": 1, "model": "a/chat1", "reason": "gut"},'
        ' {"rank": 2, "model": "CHAT4", "reason": "ok"}, {"rank": 3, "model": "a/x", "reason": "?"}]}\n```',
        cats["coding"],
    )
    assert len(top) == 2, top            # "a/x" was never benchmarked -> dropped
    assert top[0]["model"] == "a/chat1" and top[0]["reason"] == "gut"
    assert top[1]["model"] == "a/chat4"  # label/id match, case-insensitive
    assert top[1]["rank"] == 2           # ranks renumbered
    assert parse_answer("no json here", cats["coding"]) == []
    dup = parse_answer('{"ranking": [{"model": "a/chat1"}, {"model": "a/chat1"}]}', cats["coding"])
    assert len(dup) == 1, dup           # duplicate dropped
    print("✓ selftest ok")


def main():
    ap = argparse.ArgumentParser(description="AI model rating via the NVIDIA API")
    ap.add_argument("--judge", help=f"judge model id (default: {JUDGE_MODEL})")
    ap.add_argument("--prepare", action="store_true", help="only write the prompts (manual fallback)")
    ap.add_argument("--selftest", action="store_true", help="run the offline self-check")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    results = load_results()
    if args.prepare:
        return prepare(results)
    rate(results, judge=args.judge)
    benchmark.print_server_hint()


if __name__ == "__main__":
    main()
