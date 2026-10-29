# NVIDIA NIM — LLM Speed Benchmark

Benchmarks 20 free NVIDIA NIM models on the same prompt and visualizes results as an animated bar chart.

## Setup

```bash
pip install openai python-dotenv
```

Add your API key to `.env`:
```
NVIDIA_API_KEY=your_key_here
```

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
```

Results are saved to `results.json` after every model — safe to interrupt and resume.

## Visualize

Serve the folder and open the chart:
```bash
python -m http.server 8080
# open http://localhost:8080/visualize.html
```

## Files

| File | Purpose |
|---|---|
| `benchmark.py` | Runs the benchmark |
| `models.json` | List of models to test |
| `results.json` | Output — generated after running |
| `visualize.html` | Animated bar chart |

## Changelog

- v2.0 (2026-10-29): `--refresh` (fetched 109 NIM models from build.nvidia.com), `--modelgrep` regex filter, `--restart`, `results.json` resume, `ranking`/`embeddings` tests added, `visualize.html` bar-chart rebuilt.
