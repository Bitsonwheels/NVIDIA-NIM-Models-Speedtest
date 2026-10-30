# NVIDIA NIM — LLM Speed Benchmark

Benchmarks free NVIDIA NIM models (chat, embeddings, reranking) on the same prompt, visualizes the results as an animated bar chart and lets an AI jury rank the best models per category.

## Setup

```bash
pip install openai python-dotenv
```

Add your API key to `.env`:
```
NVIDIA_API_KEY=your_key_here
```

All other settings (endpoints, file paths, test prompt, timeouts, judge model) also live in `.env` — see `.env.example` for the full list with defaults.

## Run

```bash
# Fresh run (restart from scratch)
python benchmark.py --restart

# Refresh model list from build.nvidia.com (fetches all 109 NIM models, filters by endpoint)
python benchmark.py --refresh

# Only test models matching a regex (e.g. embeddings)
python benchmark.py --modelgrep emb

# Resume after interruption (default — uses results.json)
python benchmark.py

# Skip the AI rating at the end
python benchmark.py --no-ai-rating

# Use a different judge model for the AI rating
python benchmark.py --judge openai/gpt-oss-20b
```

Results are saved to `results.json` after every model — safe to interrupt and resume.

Models that failed before (timeout, 429) are retried automatically on the next run — a failed attempt
is not a verdict on the model. `REQUEST_TIMEOUT` (default 120 s) is the patience per request, because
free-tier models can need ~90 s for their first token.

## AI-Ranking (Top 3 per category)

At the end of a run, a judge model (default `meta/muse-glimmer-30b`, see `AI_JUDGE_MODEL`) picks the best 3 models per
category — **Coding** and **Embedding** — and writes `ai_ratings.json`.

- Only models that were reachable **and** delivered output are rated (chat: `tokens > 0`, embeddings: `dim > 0`).
- The judge only sees model ids and labels — never tok/s, latency or dimensions — so the ranking is
  independent of the measured values.
- Models the judge invents or repeats are dropped — the rating contains only models from the benchmark.
- Shown in `visualize.html` under the menu item **AI-Ranking** (category tabs).

```bash
python ai_rating.py                    # rate again without re-running the benchmark
python ai_rating.py --judge MODEL      # use another judge model
python ai_rating.py --prepare          # only write the prompts (manual fallback)
python ai_rating.py --selftest         # offline self-check
```

The judge runs on the same NVIDIA API key (`NVIDIA_API_KEY` in `.env`).

### Options

| Option | Effect |
|---|---|
| `--no-ai-rating` | `benchmark.py` only — skip the AI rating at the end of the run |
| `--judge MODEL` | Judge model for the rating, e.g. `nvidia/nemotron-3.5-bolt-e4b` (default `meta/muse-glimmer-30b`). With `benchmark.py` it only affects the rating step |
| `AI_JUDGE_MODEL` | Environment variable — same as `--judge`, for a permanent setting (e.g. in `.env`) |
| `--prepare` | `ai_rating.py` only — write the prompts to `ai_rating_prompts.json` instead of calling the API, for manual answering |
| `--selftest` | `ai_rating.py` only — offline self-check of filter, prompt and JSON parsing, no API calls |

## Visualize

Serve the folder and open the chart:
```bash
python -m http.server 8000
# open http://localhost:8000/visualize.html
```

## Files

| File | Purpose |
|---|---|
| `benchmark.py` | Runs the benchmark |
| `ai_rating.py` | AI rating (top 3 per category) via the NVIDIA API |
| `models.json` | List of models to test |
| `results.json` | Output — generated after running |
| `ai_ratings.json` | AI rating — generated after running |
| `visualize.html` | Animated bar chart |

## Changelog

- v2.2 (2026-10-30): All configuration moved to `.env` (see the new `.env.example`); the Ranking section was removed from `visualize.html`; timeout fix — `REQUEST_TIMEOUT` 30 s → 120 s (free-tier cold starts need ~90 s), OpenAI client retries 2 → 0 (one controlled retry in `attempt()`), and failed models are retried on the next run instead of staying broken in `results.json`.
- v2.1 (2026-10-30): AI-Rating — a judge model on the NVIDIA API (default `meta/muse-glimmer-30b`) ranks the reachable models into a top 3 per category (Coding, Embedding); new menu item "AI-Ranking" in `visualize.html`. Only models that were reachable and delivered tokens are rated, the judge never sees tok/s, latency or dimensions, invented or duplicate models are dropped. New options: `benchmark.py --no-ai-rating`, `benchmark.py --judge MODEL`, `ai_rating.py` with `--judge` / `--prepare` / `--selftest`, env `AI_JUDGE_MODEL`.
- v2.0 (2026-10-29): `--refresh` (fetched 109 NIM models from build.nvidia.com), `--modelgrep` regex filter, `--restart`, `results.json` resume, `ranking`/`embeddings` tests added, `visualize.html` bar-chart rebuilt.
