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
is not a verdict on the model. `REQUEST_TIMEOUT` (default 300 s) is the patience per request, because
free-tier models can need ~90 s for their first token.

## AI-Ranking (Top 3 per category)

At the end of a run, a judge model (default `meta/muse-glimmer-30b`, see `AI_JUDGE_MODEL`) picks the best 3 models per
category — **Coding** and **Embedding** — and writes `ai_ratings.json`.

- Only models that were reachable **and** delivered output are rated (chat: `tokens > 0`, embeddings: `dim > 0`).
- The judge only sees model ids and labels — never tok/s, latency or dimensions — so the ranking is
  independent of the measured values.
- Models the judge invents or repeats are dropped — the rating contains only models from the benchmark.
- If the judge fails or times out, the ranking stays empty and the reason is stored in `ai_ratings.json` —
  re-run `python ai_rating.py` to retry (optionally with `--judge MODEL`).
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
| `results_history.json` | Run snapshots (History / Compare tab) — generated after running |
| `visualize.html` | Animated bar chart |

## History (run snapshots + comparison)

Every benchmark run appends a snapshot to `results_history.json` — the same results list plus
metadata (timestamp, prompt, model counts, duration). Old runs are pruned automatically
(retention: `HISTORY_RETENTION_DAYS`, hard cap: `MAX_HISTORY_RUNS`).

```bash
# List recent runs
python benchmark.py --history

# Compare two runs by id
python benchmark.py --history-compare <RUN_A> <RUN_B>

# Manually prune by retention policy
python benchmark.py --history-prune

# Skip the snapshot for this run
python benchmark.py --no-history
```

The web UI shows a **Compare** tab: pick two runs, see which models improved, regressed,
appeared or disappeared — with the relevant metric per task (tok/s for chat, latency for
embeddings / ranking). A 5 % relative change counts as "same"; everything else is
classified as improved or regressed.

| Env var | Default | Effect |
|---|---|---|
| `HISTORY_FILE` | `results_history.json` | Path to the history file |
| `HISTORY_RETENTION_DAYS` | `30` | Prune runs older than this |
| `MAX_HISTORY_RUNS` | `100` | Hard cap on number of runs kept |

## Changelog

- v2.4.2 (2026-11-06): Data update after two benchmark runs on 2026-11-04 (run ids `d96ed2ce`, `50b6d34d`) — `results.json` refreshed (33 models: 15 ok, 12 error, 6 skipped, 1 empty; newly failed: Deepseek V4.1 Flash (timeout) and Step 5 Preview (empty answer), newly successful: `ising-calibration-1.5-31b`); `ai_ratings.json` re-rated with judge `google/gemma-4-31b-it` — both categories came back without a usable answer ("no usable answer from the judge model"), so the top 3 from v2.4.1 (judge `minimaxai/minimax-m3.1-flash`) only survives in the git history and can be regenerated with `python ai_rating.py`; `results_history.json` (7 snapshots) is now versioned as well; web UI — models with status `empty` now show up in the error table (before they were only counted as errors); docs — `REQUEST_TIMEOUT` default in the README corrected (120 s → 300 s) and `results_history.json` added to the file table.
- v2.4.1 (2026-11-03): History UI polish — section headers (h2) now larger (16px) with red accent background/border; Run A/Run B dropdowns in Compare tab styled with colored borders (green/cyan), glow shadows, hover/focus states; history feature working with real data snapshots.
- v2.4 (2026-11-03): History — every run appends a snapshot to `results_history.json` (metadata + full results); `--history`, `--history-compare A B`, `--history-prune` and `--no-history` added; retention via `HISTORY_RETENTION_DAYS` (30) and `MAX_HISTORY_RUNS` (100); web UI "Compare" tab with run selector and diff table (improved / regressed / same / added / removed). Comparison metric: tok/s for chat, latency for embeddings/ranking; 5 % relative change counts as stable.
- v2.4 (2026-11-03) — **Bugfix**: Fixed critical 404 regression caused by corrupted `.env` (broken API base URL `.../vMODELS_FILE=...` → restored `.../v1`); restored `results.json` (33 models, 19 OK) and `models.json` (109 models, 22 callable) from git; history snapshots now capture real benchmark data.
- v2.4 (2026-11-03) — **History Feature (Core)**: Implemented append-only run snapshots (`results_history.json`) with per-run metadata (run_id, timestamp, prompt, model counts, duration); CLI commands `--history` (list), `--history-compare A B` (diff table with metrics), `--history-prune` (manual retention), `--no-history` (skip snapshot); web UI Compare tab with dual run selectors, summary cards, color-coded diff table (green=improved, red=regressed, cyan=added, grey=same); comparison logic: chat uses tokens/sec (higher=better), embeddings/ranking use latency (lower=better), 5% relative threshold = "same"; retention via env vars `HISTORY_RETENTION_DAYS=30` and `MAX_HISTORY_RUNS=100`; zero new dependencies (stdlib only).
- v2.3 (2026-10-30): `REQUEST_TIMEOUT` raised to 300 s — the last three timing-out models (Deepseek V4.1 Flash, Mistral Large 4 1T, Step 5 Preview) now answer, the result set has 19 successful models and no timeouts; resume fix — only models scheduled in the current run are retried, so a filtered run no longer drops the results of other models; cleanup — legacy `.bck` backups and the orphaned worktree removed, the `mdcache/` markdown cache is no longer versioned; web UI table alignment (chat headers centered, embedding and skipped/error columns right-aligned).
- v2.2 (2026-10-30): All configuration moved to `.env` (see the new `.env.example`); the Ranking section was removed from `visualize.html`; timeout fix — `REQUEST_TIMEOUT` 30 s → 120 s (free-tier cold starts need ~90 s), OpenAI client retries 2 → 0 (one controlled retry in `attempt()`), and failed models are retried on the next run instead of staying broken in `results.json`.
- v2.1 (2026-10-30): AI-Rating — a judge model on the NVIDIA API (default `meta/muse-glimmer-30b`) ranks the reachable models into a top 3 per category (Coding, Embedding); new menu item "AI-Ranking" in `visualize.html`. Only models that were reachable and delivered tokens are rated, the judge never sees tok/s, latency or dimensions, invented or duplicate models are dropped. New options: `benchmark.py --no-ai-rating`, `benchmark.py --judge MODEL`, `ai_rating.py` with `--judge` / `--prepare` / `--selftest`, env `AI_JUDGE_MODEL`.
- v2.0 (2026-10-29): `--refresh` (fetched 109 NIM models from build.nvidia.com), `--modelgrep` regex filter, `--restart`, `results.json` resume, `ranking`/`embeddings` tests added, `visualize.html` bar-chart rebuilt.
