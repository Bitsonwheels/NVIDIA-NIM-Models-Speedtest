---
title: "nemotron-3.5-super-vl-120b-a12b"
publisher: "nvidia"
type: "endpoint"
updated: "2026-10-15T14:13:52.977Z"
description: "Nemotron 3.5 Super early-access reasoning model for agentic, coding, tool-calling, and multimodal workloads"
canonical: "https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b"
---

# NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4

## Description

**NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4** is the quantized release of NVIDIA Nemotron 3.5 Super VL, a vision-language model for reasoning, coding, tool use, document understanding, and video understanding. It uses NVFP4 quantization to reduce memory requirements, with quantization-aware distillation from the [BF16 model](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16).

The model combines interleaved Mamba-2, Mixture-of-Experts (MoE), and attention layers with a C-RADIO vision encoder and a vision-language connector. It has **120B total parameters** and **12B active parameters** and supports context lengths up to **1M tokens**. Multi-Token Prediction (MTP) enables native speculative decoding.

*This model is ready for commercial or non-commercial use.*

**Model Developer:** NVIDIA Corporation

## Model Summary

| | |
|:---|:---|
| **Total Parameters** | 120B (12B active) |
| **Architecture** | Mamba-2–Transformer hybrid Mixture of Experts with a C-RADIO vision encoder |
| **Precision** | NVFP4 (mixed-precision quantized weights) |
| **Context Length** | Up to 1M tokens |
| **Inputs / Outputs** | Text, images, and video / text |
| **Speculative Decoding** | Native Multi-Token Prediction (MTP) |
| **Reasoning Mode** | Configurable through the chat template (`enable_thinking=True/False`) |
| **Recommended Sampling** | Text: temperature 1.0, top_p 0.95; vision: temperature 0.6, top_p 0.95 |
| **Best For** | Efficient deployment of text and vision-language agents |
| **License** | [OpenMDW-1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1) |

## License and Terms of Use:

**GOVERNING TERMS**: The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1).

## Deployment Geography:

Global

## Use Case:

**Use Case:** This model is intended for developers using the NVIDIA-hosted API to build vision-language agents for coding, search, tool-assisted workflows, document question answering, and image and video understanding.

## Release Date:

**Build.NVIDIA.com:** 10/15/2026 via [Build.NVIDIA.com](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b)

**Hugging Face:** 10/15/2026 via [Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4)

## Reference(s):

**References:**

- [BF16 reference model](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16)
- [Nemotron Pretraining Datasets collection](https://huggingface.co/collections/nvidia/nemotron-pre-training-datasets)
- [NVIDIA Model Optimizer](https://github.com/NVIDIA/Model-Optimizer)
- [Nemotron developer page](https://developer.nvidia.com/nemotron)

## Model Architecture:

**Architecture Type:** Mamba-2–Transformer hybrid Mixture of Experts (MoE) with Multi-Token Prediction (MTP)  
**Network Architecture:** Nemotron Hybrid MoE with 512 routed experts per MoE layer, a C-RADIO vision encoder, and a vision-language connector  
**Total Parameters:** 120B  
**Active Parameters:** 12B  
**Base Model:** Nemotron 3 Super Base

### Input:

**Input Types:** Text, Image, Video  
**Input Formats:** Text strings, images, and sampled video frames  
**Input Parameters:** One-Dimensional (1D), Two-Dimensional (2D), Three-Dimensional (3D)  
**Other Input Properties:** Documents can be supplied as page images with accompanying text.

### Output:

**Output Types:** Text  
**Output Format:** String  
**Output Parameters:** One-Dimensional (1D)  
**Other Output Properties:** Input and output tokens share the configured context window, up to 1M tokens. The prompt, visual inputs, conversation history, tool results, and generated response share this window.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## Software Integration:

**Runtime Engines:**

- **vLLM**
- **SGLang**
- **TensorRT-LLM**

**Supported Hardware:**

- **NVIDIA Blackwell:** GB200, DGX Spark
- **NVIDIA Hopper:** H100, H200

**Preferred Operating Systems:** Linux

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## Model Version(s)

NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 (GA)

## Benchmarks

We evaluated our model on the following benchmarks:

| Benchmark | Nemotron 3.5 Super VL BF16 | Nemotron 3.5 Super VL NVFP4 |
| --- | ---: | ---: |
| GPQA-Diamond | 89.52 | 89.90 |
| HLE, text-only | 31.79 | 31.44 |
| MMLU-ProX | 76.91 | 73.76 |
| AA-Omniscience accuracy | 26.20 | 25.86 |
| AA-Omniscience hallucination rate | 30.0 | 27.7 |
| AA-Omniscience index | 4.03 | 5.3 |
| APEX shortlist | 88.36 | 89.36 |
| LiveCodeBench v6 | 88.22 | 87.41 |
| SciCode, subtask | 47.13 | 46.61 |
| AA-LCR v1.1 | 68.62 | 67.69 |
| GraphWalks | 89.71 | 90.34 |
| IFBench | 70.86 | 71.50 |
| LMArena v3 proxy | 52.67 | 51.93 |
| WMT24++ | 84.80 | 84.76 |
| tau2-bench retail | 69.24 | 69.30 |
| tau2-bench airline | 76.50 | 75.75 |
| tau2-bench telecom | 73.19 | 73.19 |
| tau3-bench banking | 18.88 | 17.78 |
| GDPval-AA v2 | 1211 | 1206 |
| BrowseComp | 78 | 77.5 |
| SWE-bench Verified | 71.10 | 71.07 |
| SWE-bench Multilingual | 67.72 | 67.00 |
| SWE-bench Pro | 51.78 | 51.30 |
| Terminal-Bench 2.1 | 66.70 | 60.80 |
| BabyVision | 29.60 | 29.51 |
| MMLongBench-Doc | 62.82 | 62.82 |
| V* | 85.60 | 85.95 |
| OCR-Reasoning | 65.08 | 65.09 |
| MathVision | 78.16 | 77.79 |
| HLE, full set | 29.20 | 29.00 |
| OCRBench v2, EN | 68.12 | 68.34 |
| OCRBench v2, ZH | 59.15 | 59.03 |
| CharXiv reasoning | 80.82 | 79.88 |
| Video-MME v2 | 32.85 | 32.54 |
| OSWorld-Verified | 51.14 | 52.3 |
| BrowseComp [offline] | 78 | 77.5 |
| WebVoyager [offline] | 77.72 | 66.31 |
| AA-Briefcase-Lite [offline] | 1137 (-) \| 1252 (-) \| 40 | 1137 (-) \| 1188 (-) \| 45 |
| AutomationBench-AA [offline] | 32.44 | 32.3 |
| GDP.pdf [offline] | 6.6 (AA 6.6) | 6.0 |
| Terminal Bench 4 [offline] | 1 | 1.5 |
| DeepSWE [offline] | 24.65 | 18.2 |

> The evaluations between the BF16 checkpoint and NVFP4 checkpoint are done with all configs, harnesses, and other non-model parameters held static to ensure fair comparison that isolates the checkpoint impact

We evaluated Nemotron 3.5 Super on a comprehensive suite of benchmarks spanning agentic capabilities, reasoning and knowledge, multimodal, conversational ability and instruction following, long-context understanding, and multilingual performance. All evaluation results for Nemotron 3.5 Super and baselines were collected via NeMo Gym. For reproducibility purposes, more details on the evaluation settings can be found in the [NeMo Gym recipes folder](https://github.com/NVIDIA-NeMo/Gym) and the [corresponding reproducibility tutorial](https://github.com/NVIDIA-NeMo/Gym/blob/main/nemotron_recipes/super-3.5/reproducibility.md). The published recipes specify the benchmark-specific containers, prompts, inference parameters, parser configurations, and scoring settings used to produce the results.

There were a few benchmarks that were not yet onboarded in our open source tools, and for these we used either their official open source implementation or an internal scaffolding that we plan to open source in the future: BabyVision, CharXiv-RQ, MathVision, MMLongBench-Doc, OCR-Reasoning, OCRBench-v2, V*, Video-MME-v2.

## Training, Testing, and Evaluation Datasets

### Training

**Data Modality:** Text, images, and video  
**Foundation Training Data Size:** More than 20 trillion tokens  
**Image Training Data Size:** 1 Million to 1 Billion Images  
**Text Training Data Size:** More than 10 Trillion Tokens  
**Video Training Data Size:** 10,000 to 1 Million Hours  
**Foundation Data Collection Period:** 2013 to December 2025  
**Data Collection Method:** Hybrid: automated, manually-collected, and synthetic  
**Labeling Method:** Hybrid: automated, manually-labeled, and synthetic

The foundation corpus contains curated and synthetic text covering English, 19 other spoken languages, and 43 programming languages. Sources include webpages, dialogue, articles, code, and other written materials across math, science, legal, finance, and general knowledge domains.

The post-training corpus includes reasoning, coding, tool use, instruction following, structured outputs, chat, safety, and long-context tasks, together with image and video understanding. Synthetic trajectories are filtered for structural correctness, repetition, and task validity.

For more information about the datasets used to train this model, please see the [Public Summary of Training Content](https://assets.ngc.nvidia.com/products/api-catalog/nemotron-3.5-super-vl/Nemotron_3.5_Super_VL_EU_Training_Content_Summary.pdf)

<details>
<summary>Detailed dataset information</summary>

#### **Base Pre-Training Corpus (Nemotron 3 Foundation)**

The foundation of the model is trained on the Nemotron 3 corpus, comprising the following datasets from the [Nemotron Pretraining Datasets collection](https://huggingface.co/collections/nvidia/nemotron-pre-training-datasets):

| Dataset Collection | Token Counts | Description |
| :--- | :--- | :--- |
| **Nemotron-CC-v2** & **v2.1** | 9.1T | A massive collection of English web data filtered from Common Crawl, including 2.5T+ tokens of new organic, translated, and synthetically rephrased content. |
| **Nemotron-CC-Code-v1** | 427.9B | High-quality code tokens extracted from Common Crawl using the Lynx + LLM pipeline to preserve structure and equations. |
| **Nemotron-Pretraining-Code-v1** & **v2** & **v3** | 1.7T | Curated GitHub code references with multi-stage filtering, deduplication, and large-scale synthetic code data. |
| **Nemotron-CC-Math-v1** | 133.3B | High-quality math pre-training dataset preserving LaTeX formatting and mathematical structures. |
| **Nemotron-Pretraining-Specialized-v1** & **v1.1** & **v1.2** & **Nemotron-Pretraining-SFT-v1** | 660.0B | Synthetic datasets targeting specialized domains such as STEM reasoning and scientific coding. |
| **Nemotron-Pretraining-Legal-v1** | 4.3B | Synthetic datasets targeting the legal domain. |

### Public Datasets

| Dataset | Collection Period |
| :---- | :---- |
| [GSM8K](https://github.com/openai/grade-school-math) | 4/23/2025 |
| [CC-NEWS](https://commoncrawl.org/blog/news-dataset-available) | 4/23/2025 |
| [Common Crawl](https://commoncrawl.org/) | 4/23/2025 |
| [Wikimedia](https://dumps.wikimedia.org/) | 4/23/2025 |
| [Bespoke-Stratos-17k](https://huggingface.co/datasets/bespokelabs/Bespoke-Stratos-17k) | 4/23/2025 |
| [tigerbot-kaggle-leetcodesolutions-en-2k](https://huggingface.co/datasets/TigerResearch/tigerbot-kaggle-leetcodesolutions-en-2k) | 4/23/2025 |
| [glaive-function-calling-v2](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2) | 4/23/2025 |
| [APIGen Function-Calling](https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k) | 4/23/2025 |
| [LMSYS-Chat-1M](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) | 4/23/2025 |
| [Open Textbook Library - CC BY-SA & GNU subset](https://open.umn.edu/opentextbooks/textbooks/) and [OpenStax - CC BY-SA subset](https://openstax.org/) | 4/23/2025 |
| [Advanced Reasoning Benchmark](https://github.com/TheDuckAI/arb), [tigerbot-kaggle-leetcodesolutions-en-2k](https://huggingface.co/datasets/TigerResearch/tigerbot-kaggle-leetcodesolutions-en-2k), [PRM800K](https://github.com/openai/prm800k), and [SciBench](https://github.com/mandyyyyii/scibench) | 4/23/2025 |
| [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) | 4/23/2025 |
| [Court Listener](https://www.courtlistener.com/help/api/bulk-data/) | Legacy Download |
| [peS2o](https://huggingface.co/datasets/allenai/peS2o) | Legacy Download |
| [OpenWebMath](https://huggingface.co/datasets/open-web-math/open-web-math) | Legacy Download |
| [BioRxiv](https://www.biorxiv.org/tdm) | Legacy Download |
| [PMC Open Access Subset](https://pmc.ncbi.nlm.nih.gov/tools/openftlist/) | Legacy Download |
| [OpenWebText2](https://openwebtext2.readthedocs.io/en/latest/) | Legacy Download |
| [Stack Exchange Data Dump](https://archive.org/details/stackexchange) | Legacy Download |
| [PubMed Abstracts](https://github.com/thoppe/The-Pile-PubMed) | Legacy Download |
| [NIH ExPorter](https://exporter.nih.gov/ExPORTER_Catalog.aspx) | Legacy Download |
| [arXiv](https://info.arxiv.org/help/bulk_data/index.html) | Legacy Download |
| [BigScience Workshop Datasets](https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml#datasets) | Legacy Download |
| [SEC's Electronic Data Gathering, Analysis, and Retrieval (EDGAR)](https://www.sec.gov/search-filings) | Legacy Download |
| [Advanced Mathematical Problem Solving](https://github.com/hendrycks/math?tab=readme-ov-file) | Legacy Download |
| [MathPile](https://github.com/GAIR-NLP/MathPile/) | Legacy Download |
| [NuminaMath CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) | Legacy Download |
| [PMC Article](https://pmc.ncbi.nlm.nih.gov/tools/textmining/) | Legacy Download |
| [FLAN](https://github.com/google-research/FLAN) | Legacy Download |
| [Advanced Reasoning Benchmark](https://github.com/TheDuckAI/arb) | Legacy Download |
| [SciBench](https://github.com/mandyyyyii/scibench) | Legacy Download |
| [WikiTableQuestions](https://huggingface.co/datasets/wikitablequestions) | Legacy Download |
| [FinQA](https://finqasite.github.io/) | Legacy Download |
| [Riddles](https://github.com/crawsome/riddles) | Legacy Download |
| [Problems in Elementary Mathematics for Home Study](https://archive.org/details/AntonovVygodskyNikitinSankinProblemsInElementaryMathematicsForHomeStudyMir1982) | Legacy Download |
| [MedMCQA](https://huggingface.co/datasets/openlifescienceai/medmcqa) | Legacy Download |
| [Cosmos QA](https://huggingface.co/datasets/allenai/cosmos_qa) | Legacy Download |
| [MCTest](https://huggingface.co/datasets/sagnikrayc/mctest) | Legacy Download |
| [AI2's Reasoning Challenge](https://huggingface.co/datasets/ai2_arc) | Legacy Download |
| [OpenBookQA](https://github.com/allenai/OpenBookQA) | Legacy Download |
| [MMLU Auxiliary Train](https://huggingface.co/datasets/cais/mmlu/viewer/all/auxiliary_train) | Legacy Download |
| [social-chemestry-101](https://huggingface.co/datasets/tasksource/social-chemestry-101) | Legacy Download |
| [Moral Stories](https://huggingface.co/datasets/demelin/moral_stories) | Legacy Download |
| [The Common Pile v0.1](https://huggingface.co/common-pile) | Legacy Download |
| [FineMath](https://huggingface.co/datasets/HuggingFaceTB/finemath) | Legacy Download |
| [MegaMath](https://huggingface.co/datasets/LLM360/MegaMath) | Legacy Download |
| [MultiverseMathHard](https://huggingface.co/datasets/Nexusflow/MultiverseMathHard) | 10/2/2025 |
| [SWE-Gym](https://huggingface.co/datasets/SWE-Gym/SWE-Gym) | 10/2/2025 |
| [WorkBench](https://github.com/olly-styles/WorkBench/tree/main/data/raw) | 10/2/2025 |
| [WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) | 10/2/2025 |
| [OpenCodeReasoning-2](https://huggingface.co/datasets/nvidia/OpenCodeReasoning-2) | 10/2/2025 |
| [HelpSteer3](https://huggingface.co/datasets/nvidia/HelpSteer3) | 10/2/2025 |
| [opc-sft-stage2](https://huggingface.co/datasets/OpenCoder-LLM/opc-sft-stage2) | 10/2/2025 |
| [Big-Math-RL-Verified](https://huggingface.co/datasets/SynthLabsAI/Big-Math-RL-Verified) | 10/2/2025 |
| [MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA) | 10/2/2025 |
| [simple-arithmetic-problems](https://huggingface.co/datasets/garrethlee/simple-arithmetic-problems) | 10/2/2025 |
| [arithmetic](https://huggingface.co/datasets/EleutherAI/arithmetic) | 10/2/2025 |
| [Skywork-OR1-RL-Data](https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data) | 10/2/2025 |
| [FastChat](https://github.com/lm-sys/FastChat/blob/main/playground/data/dummy.json) | 10/2/2025 |
| [News Commentary](https://opus.nlpl.eu/News-Commentary.php) | 10/2/2025 |
| [Essential-Web](https://huggingface.co/datasets/EssentialAI/essential-web-v1.0) | 10/2/2025 |
| [finepdfs](https://huggingface.co/datasets/HuggingFaceFW/finepdfs) | 10/2/2025 |
| [HotpotQA](https://huggingface.co/hotpot_qa/datasets) | 10/2/2025 |
| [SQuAD2.0](https://rajpurkar.github.io/SQuAD-explorer/) | 10/2/2025 |
| [NLTK Words Lists](https://www.nltk.org/nltk_data/) | 10/2/2025 |
| NVClip (NV-CC-Img-Text-Dataset) | 2022-2026 |
| [ScaleCUA, Processed Training Subset](https://huggingface.co/datasets/OpenGVLab/ScaleCUA-Data) | 2022-2026 |
| [RoboInter-VQA](https://huggingface.co/datasets/InternRobotics/RoboInter-VQA) | 2022-2026 |
| [Open Images V6, Object-Detection Training Records](https://storage.googleapis.com/openimages/web/index.html) | 2022-2026 |
| YT1B PLM Video QA, Custom No-Thinking and Safety-Filtered | 2022-2026 |
| YT1B PLM Dense Captions, No-Thinking and Safety-Filtered | 2022-2026 |
| [RoboVQA](https://robovqa.github.io/) | 2022-2026 |
| YT1B PLM Thinking Traces, Safety-Filtered | 2022-2026 |
| Boyi Short-Video QA | 2022-2026 |
| Boyi Short-Video QA, Custom No-Thinking and Safety-Filtered | 2022-2026 |
| K710 Video Classification, Full Training Snapshot | 2022-2026 |
| Molmo2-VideoCapQA | 2022-2026 |
| Molmo2-VideoCapQA, Custom No-Thinking and Safety-Filtered | 2022-2026 |
| Molmo2-VideoPoint, Custom No-Thinking and Safety-Filtered | 2022-2026 |
| Molmo2-VideoPoint | 2022-2026 |

### **Directly Crawled Websites and Other Online Data Sources**

The websites directly crawled by NVIDIA for this model are [doubtnut.com](http://doubtnut.com), [archive.org](http://archive.org), [askfilo.com](http://askfilo.com), and [pewresearch.org](http://pewresearch.org).

The English Common Crawl data was downloaded from the Common Crawl Foundation (see their FAQ for details on their crawling) and includes the snapshots CC-MAIN-2013-20 through CC-MAIN-2025-13. The data was subsequently deduplicated and filtered in various ways used in the Nemotron-CC data pipeline. Additionally, we extracted data for fifteen languages from the following three Common Crawl snapshots: CC-MAIN-2024-51, CC-MAIN-2025-08, CC-MAIN-2025-18. The fifteen languages included were Arabic, Chinese, Danish, Dutch, French, German, Italian, Japanese, Korean, Polish, Portuguese, Russian, Spanish, Swedish, and Thai. As we did not have reliable multilingual model-based quality classifiers available, we applied just heuristic filtering instead—similar to what we did for lower quality English data in the Nemotron-CC pipeline, but selectively removing some filters for some languages that did not work well. Deduplication was done in the same way as for Nemotron-CC.

The GitHub Crawl was collected using the GitHub REST API and the Amazon S3 API. Each crawl was operated in accordance with the rate limits set by its respective source, either GitHub or S3. We collect raw source code and subsequently remove any having a license which does not exist in our permissive-license set.

| Dataset | Modality | Dataset Size | Collection Period | Collecting Organisation |
| :---- | :---- | :---- | :---- | :---- |
| English Common Crawl | Text | 3.36T | 4/8/2025 | NVIDIA Advanced Deep Learning Research |
| English Common Crawl 1.1 | Text | Not disclosed | 10/2/2025 | NVIDIA Advanced Deep Learning Research |
| Multilingual Common Crawl | Text | 812.7B | 5/1/2025 | NVIDIA Advanced Deep Learning Research |
| GitHub Crawl | Text | 747.4B | 4/29/2025 | NVIDIA Advanced Deep Learning Research |
| GitHub Crawl 1.1 | Text | 172.7B | 9/30/2025 | NVIDIA Advanced Deep Learning Research |
| [Sangraha](https://huggingface.co/datasets/ai4bharat/sangraha) | Text | 109,263,115 indexed source sequences: 77,231,480 verified and 32,031,635 unverified | Undisclosed | NVIDIA Advanced Deep Learning Research |
| LITA Chunked Video Labels, Custom No-Thinking Dense Captions | Text (video labels) | 151,349 records | Undisclosed | NVIDIA Advanced Deep Learning Research|
| LITA Chunked Video Labels, Cleaned v2 | Text (video labels) | 150,434 records | Undisclosed | NVIDIA Advanced Deep Learning Research |
| Single-Page Document Labels, Qwen3.5 v2 | Text and images | 50,930 records | Undisclosed | NVIDIA Advanced Deep Learning Research |
| Processed YouTube Videos, Cosmos Dense Captions | Text and video | 274,472 records | Undisclosed | NVIDIA Advanced Deep Learning Research |

## Private Non-publicly Accessible Datasets of Third Parties

| Dataset | Model(s) used |
|---------|---------------|
| Global Regulation | Unknown |
| TAUS Translation Memory | Unknown |
| Scale HLE | Unknown |
| HackerRank Coding | Unknown |
| RL data for Search | Gemini 3; GPT-5 |
| Mercor SWE-AgentsV1 | Undisclosed |
| KeenSight Batch 1, Relabeled Subset | Qwen3.5-122B-A10B |
| KeenSight Batch 1, Remaining Subset | Qwen3.5-122B-A10B |
| Camio Multilingual OCR and Document Layout | Undisclosed |
| Chinese Visual Question Answering, Relabeled Subset | Qwen3.5-122B-A10B |
| Camio Chinese OCR, Cleaned Variant | Qwen3.5-122B-A10B |
| Camio English OCR, Cleaned Variant | Qwen3.5-122B-A10B |
| KeenSight Batch 2, Remaining Subset | Qwen3.5-122B-A10B |
| KeenSight Batch 1, Safety-Filtered Trace Variant | Qwen3.5-122B-A10B |
| Chinese Visual Question Answering, Safety-Filtered Trace Variant | Qwen3.5-122B-A10B |
| Camio Chinese Question Answering, Verified-Correct Subset | Qwen3.5 |
| KeenSight Chinese OCR, Filtered Subset | DeepSeek-OCR |
| Camio Synthetic Trading-Graph Question Answering | Undisclosed |
| Camio Synthetic Menu and Receipt Question Answering | Qwen3.5-122B-A10B |
| Camio Chinese OCR, Formatted Variant | Qwen3.5-122B-A10B |
| Camio Synthetic Time-Series Question Answering | Undisclosed |
| Camio English OCR, Formatted Variant | Qwen3.5-122B-A10B |
| Lean Formal Proofs — RL | Undisclosed |
| Document-Grounded Finance Reasoning, Patch Tasks — RL | Undisclosed |
| Math CoT — SFT | Kimi K3 |
| Chat — SFT | Undisclosed |
| Chat, Reasoning Off — SFT | Undisclosed |
| Conversational Tool-Use Simulation — RL | Undisclosed |
| Math CoT, Low Variant — SFT | Kimi K3 |
| Document-Grounded Finance Reasoning — SFT | Undisclosed |
| Safety Preference v0.3 — RL | Undisclosed |
| Response-Length Instruction Following, Reasoning Off — SFT | Undisclosed |
| Math Python TIR, Low Variant — SFT | Kimi K3 |
| Math Python TIR — SFT | Kimi K3 |
| General-Purpose Tool Calling — SFT | Qwen3.5-397B-A17B; Gemma-4-31B-it |
| Knowledge Agent — SFT | Undisclosed |
| DataFunnel arXiv Science4 v1.0 — RL | DeepSeek-V4-Flash (problem extraction); GLM-5.2 (refinement); Kimi K3 and K3 V5 (verification and filtering); Super 3.5 r14 (difficulty profiling); Qwen3-235B-A22B-Instruct-2507-FP8 (reward judging) |
| Structured Outputs v3 — RL | gpt-oss-120b |
| Response-Length Instruction Following — SFT | Undisclosed |
| Filtered CUDA Coding — SFT | Undisclosed |
| Reasoning Gym — RL | Undisclosed |
| Competitive Coding Challenges v2 — SFT | GLM-5.2 |
| Multi-Turn Instruction Following, Reasoning Off — SFT | Undisclosed |
| Multi-Turn Instruction Following — SFT | Undisclosed |
| Instruction Following, Filtered RLHF Prompts — SFT | Undisclosed |
| Citation Formatting — RL | gpt-oss-120b |
| Long-Context General Data — SFT | Undisclosed |
| Free-Form Formatting — RL | gpt-oss-120b |
| Structured Outputs v4 — RL | Undisclosed |
| Tool-Call Schema — RL | No model used for RL conversion; source-generation models undisclosed |
| Competitive Coding, OCR Python — SFT | DeepSeek-V4-Pro |
| Lean Formal Proofs — SFT | gpt-oss-120b; Goedel-Prover-V2-32B; Qwen2.5-32B-Instruct |
| Citation Instruction Following — RL | Undisclosed |
| Search Graph Walks — SFT | MiniMax-M2 |
| General-Purpose Tool Calling, Reasoning Off — SFT | Undisclosed |
| Knowledge Agent Tau3, Reasoning Off — SFT | Undisclosed |
| ARC-AGI Puzzle Reasoning — SFT | Kimi-K2.5; Qwen3-235B-A22B-Thinking-2507; DeepSeek-V3.2; Qwen3-Next-80B-A3B-Thinking; GLM-4.5-Air-FP8; gpt-oss-120b; GLM-4.7-FP8; Ring-1T; Ministral-3-14B-Reasoning-2512 |
| Calendar — RL | Undisclosed |
| ACEProof — SFT | Undisclosed |
| Long Translation — SFT | Undisclosed |
| Agentless Software Engineering — SFT | Undisclosed |
| Long-Context PDF Translation v1.0 — SFT | DeepSeek-V4-Flash (translation generation); GPT-5.6 Sol (filtering and judging) |
| KeenSight Batch 2, Relabeled and Filtered Subset | Qwen3.5-122B-A10B; Gemini 3 Flash Preview (filtering) |
| Camio Chinese Letter QA, Cleaned `entrace_cleaned` Variant | Qwen3-VL-30B-A3B-Thinking-FP8; gpt-oss-120b; Qwen3.5-122B-A10B; GPT-4o mini (filtering and quality checks) |
| Camio Chinese Letter QA, Cleaned Variant | Qwen3-VL-30B-A3B-Thinking-FP8; gpt-oss-120b; Qwen3.5-122B-A10B; GPT-4o mini (filtering and quality checks) |
| Camio Chinese Text QA, Cleaned `entrace_cleaned` Variant | Qwen3-VL-30B-A3B-Thinking-FP8; gpt-oss-120b; Qwen3.5-122B-A10B; GPT-4o mini (filtering and quality checks) |

## Private Non-publicly Accessible Datasets by NVIDIA

| Dataset | Model(s) used |
|---------|---------------|
| Simple Minesweeper | Undisclosed |
| Simple Sudoku | Undisclosed |
| Multitool Typewriter Hard | Undisclosed |
| Machine Translation of News Commentary and TAUS Translation Memory | Undisclosed |
| Machine Translation of STEM - | [Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) |
| Competitive Coding RL data from Nemotron Cascade | Undisclosed |
| Long context RL | Undisclosed |
| Single-step SWE RL for patch generation | Undisclosed |
| OpenHands SWE | Undisclosed |

## NVIDIA-Sourced Synthetic Datasets (Pre-Training)

| Dataset | Modality | Dataset Size | Seed Dataset | Model(s) used for generation |
| :---- | :---- | :---- | :---- | :---- |
| Nemotron-Pretraining-Fact-Seeking | Text | 35.0B | [FineWiki](https://huggingface.co/datasets/HuggingFaceFW/finewiki) | [Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507) |
| Nemotron-Pretraining-Legal | Text | 4.3B | CommonPile (caselaw_access_project_filtered); California Code of Regulations; Judicial Ethics Opinions; [GLOBALCIT](https://globalcit.eu/); [CUAD](https://www.atticusprojectai.org/cuad); Nemotron Personas; [ToSDR Terms of Service Corpus](https://www.kaggle.com/datasets/sonu1607/tosdr-terms-of-service-corpus); CodeHima/TOS_Dataset; [ContractNLI](https://stanfordnlp.github.io/contract-nli/); CaseHOLD; Code of Federal Regulations; [Canadian Case Law](https://huggingface.co/datasets/a2aj/canadian-case-law) (subsets that allow commercial use) | [Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) |
| Nemotron-Pretraining-Formal-Logic | Text | 128M | [Nemotron Personas](https://huggingface.co/datasets/nvidia/Nemotron-Personas-USA) | [Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) |
| Nemotron-Pretraining-Economics | Text | 73.4M | - | [Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) |
| Nemotron-Pretraining-Multiple-Choice | Text | 1.6B | [MMLU Auxiliary Train](https://huggingface.co/datasets/cais/mmlu/viewer/all/auxiliary_train) | [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3); [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) |
| Nemotron-Pretraining-Code-Concepts | Text | 7.3B | - | [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b); [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) |
| Nemotron-Pretraining-Unconditional-Algorithmic | Text | 196.5M | - | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b); [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) |
| More Synthetic Tasks from DeepSeek-V3 and Qwen3-235B-A22B | Text | 1.1B | train splits of acp_bench; ai2_arc; babi; gsm8k; hendrycks_math; IFEval; MedText; mediqa_qa; mlqa; MMLU-Pro; mmlu-pro-plus; MMLU-ProX; nq_open; tinyGSM8k; truthful_qa; truthfulqa-multi; MATH-lighteval; mmlu; awesome-chatgpt-prompts; super_glue | [DeepSeek v3](https://huggingface.co/deepseek-ai/DeepSeek-V3); [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) |
| Synthetic Tasks from DeepSeek-V3 and Qwen3-235B-A22B | Text | 6.7B | train splits of Into the Unknown; AI2 ARC (AI2 Reasoning Challenge); BLiMP (Benchmark of Linguistic Minimal Pairs); CommonSenseQA; GLUE; HeadQA; Hendrycks Ethics; Memo Trap; modus-tollens; NeQA; pattern-matching-suppression; mastermind_24_mcq_random; mastermind_24_mcq_close; quote-repetition; redefine-math; Repetitive Algebra; sig-figs; MMLU-Pro; MC-TACO; MedConceptsQA; MMLU_dataset; OpenbooksQA; PIQA (Physical Interaction Question Answering); SocialIQA; SuperGLUE; tinyAI2_arc; tinyMMLU; tinyWinogrande; TruthfulQA; WebQuestions; Winogrande; GPQA; MBPP | [DeepSeek v3](https://huggingface.co/deepseek-ai/DeepSeek-V3); [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) |
| Synthetic Art of Problem Solving from DeepSeek-R1 | Text | 40B | [Art of Problem Solving](https://artofproblemsolving.com/company); [American Mathematics Competitions 8](https://artofproblemsolving.com/wiki/index.php/AMC_8_Problems_and_Solutions); [American Mathematics Competitions 10](https://artofproblemsolving.com/wiki/index.php/AMC_10_Problems_and_Solutions) | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) |
| Synthetic Moral Stories and Social Chemistry from Qwen3-235B-A22B-Thinking-2507 and Mixtral-8x22B-v0.1 | Text | 15.2M | [social-chemestry-101](https://huggingface.co/datasets/tasksource/social-chemestry-101); [Moral Stories](https://huggingface.co/datasets/demelin/moral_stories) | [Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507); [Mixtral-8x22B-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1) |
| Synthetic Moral Stories and Social Chemistry from Mixtral-8x22B-v0.1 | Text | 327M | [social-chemestry-101](https://huggingface.co/datasets/tasksource/social-chemestry-101); [Moral Stories](https://huggingface.co/datasets/demelin/moral_stories) | [Mixtral-8x22B-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1) |
| Synthetic Social Sciences seeded with OpenStax from DeepSeek-V3, Mixtral-8x22B-v0.1, and Qwen2.5-72B | Text | 83.6M | [OpenStax - CC BY-SA subset](https://openstax.org/) | [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3); [Mixtral-8x22B-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1); [Qwen2.5-72B](https://huggingface.co/Qwen/Qwen2.5-72B) |
| Synthetic Health Sciences seeded with OpenStax from DeepSeek-V3, Mixtral-8x22B-v0.1, and Qwen2.5-72B | Text | 9.7M | [OpenStax - CC BY-SA subset](https://openstax.org/) | [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3); [Mixtral-8x22B-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1); [Qwen2.5-72B](https://huggingface.co/Qwen/Qwen2.5-72B) |
| Synthetic STEM seeded with OpenStax, Open Textbook Library, and GSM8K from DeepSeek-R1, DeepSeek-V3, DeepSeek-V3-0324, and Qwen2.5-72B | Text | 175M | [OpenStax - CC BY-SA subset](https://openstax.org/); [GSM8K](https://github.com/openai/grade-school-math); [Open Textbook Library - CC BY-SA & GNU subset](https://open.umn.edu/opentextbooks/textbooks/) | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1), [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3); [DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324); [Qwen2.5-72B](https://huggingface.co/Qwen/Qwen2.5-72B) |
| [Nemotron-PrismMath](https://huggingface.co/datasets/nvidia/Nemotron-PrismMath) | Text | 4.6B | [Big-Math-RL-Verified](https://huggingface.co/datasets/SynthLabsAI/Big-Math-RL-Verified); [OpenR1-Math-220k](https://huggingface.co/datasets/open-r1/OpenR1-Math-220k) | [Qwen2.5-0.5B-instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct), [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct); [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B) |
| Synthetic Question Answering Data from Papers and Permissible Books from Qwen2.5-72B-Instruct | Text | 350M | [arXiv](https://info.arxiv.org/help/bulk_data/index.html); [National Institutes of Health ExPorter](https://www.nih.gov/); [BioRxiv](https://www.biorxiv.org/tdm); [PMC Article](https://pmc.ncbi.nlm.nih.gov/tools/textmining/); [USPTO Backgrounds](https://data.uspto.gov/apis/transition-guide/bdss#pats); [peS2o](https://huggingface.co/datasets/allenai/peS2o); Global Regulation; [CORE](https://core.ac.uk/documentation/dataset); [PG-19](https://github.com/google-deepmind/pg19); [DOAB CC BY & CC BY-SA subset](https://www.doabooks.org/en); [NDLTD](https://ndltd.org/thesis-resources/global-etd-search/) | [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) |
| Synthetic Rephrased [Math Data from Common Crawl](https://huggingface.co/datasets/nvidia/Nemotron-MIND) from phi-4 | Text | 73B | [Common Crawl](https://commoncrawl.org/latest-crawl) | [phi-4](https://huggingface.co/microsoft/phi-4) |
| Synthetic Math Data from Common Crawl 4plus | Text | 52.3B | [Common Crawl](https://commoncrawl.org/latest-crawl) | [phi-4](https://huggingface.co/microsoft/phi-4) |
| Synthetic Math Data from Common Crawl 3 | Text | 80.9B | [Common Crawl](https://commoncrawl.org/latest-crawl) | [phi-4](https://huggingface.co/microsoft/phi-4) |
| Synthetic AGIEval seeded with AQUA-RAT, LogiQA, and AR-LSAT from DeepSeek-V3 and DeepSeek-V3-0324 | Text | 4.0B | [AQUA-RAT](https://huggingface.co/datasets/deepmind/aqua_rat); [LogiQA](https://huggingface.co/datasets/lucasmccabe/logiqa); [AR-LSAT](https://github.com/zhongwanjun/AR-LSAT) | [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3); [DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) |
| Synthetic AGIEval seeded with AQUA-RAT, LogiQA, and AR-LSAT from Qwen3-30B-A3B | Text | 4.2B | [AQUA-RAT](https://huggingface.co/datasets/deepmind/aqua_rat); [LogiQA](https://huggingface.co/datasets/lucasmccabe/logiqa); [AR-LSAT](https://github.com/zhongwanjun/AR-LSAT) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) |
| Synthetic Art of Problem Solving from Qwen2.5-32B-Instruct, Qwen2.5-Math-72B, Qwen2.5-Math-7B, and Qwen2.5-72B-Instruct | Text | Undisclosed | [Art of Problem Solving](https://artofproblemsolving.com/company); [American Mathematics Competitions 8](https://artofproblemsolving.com/wiki/index.php/AMC_8_Problems_and_Solutions); [American Mathematics Competitions 10](https://artofproblemsolving.com/wiki/index.php/AMC_10_Problems_and_Solutions); [GSM8K](https://github.com/openai/grade-school-math); [PRM800K](https://github.com/openai/prm800k) | [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct); [Qwen2.5-Math-72B](https://huggingface.co/Qwen/Qwen2.5-Math-72B); [Qwen2.5-Math-7B](https://huggingface.co/Qwen/Qwen2.5-Math-7B); [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) |
| Synthetic MMLU Auxiliary Train from DeepSeek-R1 | Text | 0.5B | [MMLU Auxiliary Train](https://huggingface.co/datasets/cais/mmlu/viewer/all/auxiliary_train) | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) |
| Synthetic Long Context Continued Post-Training Data from Papers and Permissible Books from Qwen2.5-72B-Instruct | Text | Undisclosed | [arXiv](https://info.arxiv.org/help/bulk_data/index.html); [National Institutes of Health ExPorter](https://www.nih.gov/); [BioRxiv](https://www.biorxiv.org/tdm); [PMC Article](https://pmc.ncbi.nlm.nih.gov/tools/textmining/); [USPTO Backgrounds](https://data.uspto.gov/apis/transition-guide/bdss#pats); [peS2o](https://huggingface.co/datasets/allenai/peS2o); Global Regulation; [CORE](https://core.ac.uk/documentation/dataset); [PG-19](https://github.com/google-deepmind/pg19); [DOAB CC BY & CC BY-SA subset](https://www.doabooks.org/en); [NDLTD](https://ndltd.org/thesis-resources/global-etd-search/) | [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) |
| Synthetic Common Crawl from Qwen3-30B-A3B and Mistral-Nemo-12B-Instruct | Text | 415.8B | [Common Crawl](https://commoncrawl.org/) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B); [Mistral-NeMo-12B-Instruct](https://huggingface.co/nvidia/Mistral-NeMo-12B-Instruct) |
| Synthetic Multilingual Data from Common Crawl from Qwen3-30B-A3B | Text | Undisclosed | [Common Crawl](https://commoncrawl.org/) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) |
| Synthetic Multilingual Data from Wikimedia from Qwen3-30B-A3B | Text | Undisclosed | [Wikimedia](https://dumps.wikimedia.org/) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) |
| Synthetic Math Data from Wikimedia from Nemotron-4-340B-Instruct | Text | Undisclosed | - | [Nemotron-4-340B-Instruct](https://huggingface.co/nvidia/Nemotron-4-340B-Instruct) |
| Synthetic Common Crawl Code from phi-4 | Text | 427.9B | [Common Crawl](https://commoncrawl.org/latest-crawl) | [phi-4](https://huggingface.co/microsoft/phi-4) |
| Synthetic Scientific Coding from Qwen3-235B-A22B | Text | 1.2B | [Wikimedia](https://dumps.wikimedia.org/) | [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) |
| Tool Calling Data | Text | 26.2B | - | [Qwen3-235B-A22B-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507); [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) |
| Synthetic Essential-Web from QwQ-32B | Text | 28.1B | [Essential-Web](https://huggingface.co/datasets/EssentialAI/essential-web-v1.0) | [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B) |
| Translated Synthetic Crawl | Text | 389.9B | [Common Crawl](https://commoncrawl.org/) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) |
| Translated Synthetic Wikipedia | Text | 7.9B | [Wikimedia](https://dumps.wikimedia.org/) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) |
| Synthetic Long Context from Qwen3-235B-A22B-Instruct-2507 | Text | Undisclosed | [CORE](https://core.ac.uk/documentation/dataset); [PG-19](https://github.com/google-deepmind/pg19); [DOAB CC BY & CC BY-SA subset](https://www.doabooks.org/en); [NDLTD](https://ndltd.org/thesis-resources/global-etd-search/) | [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) |
| Synthetic Search STEM OPENQ from DeepSeek-R1-0528 | Text | Undisclosed | - | [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic MCQ from Qwen2.5-32B-Instruct and DeepSeek-R1-0528 | Text | Undisclosed | - | [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct); [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic Offline Search MCQA HLE from DeepSeek-R1-0528 | Text | Undisclosed | - | [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic Offline Search MCQA GPQA from Qwen3-235B-A22B and DeepSeek-R1-0528 | Text | Undisclosed | - | [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B); [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic Human Preference from QwQ-32B, Qwen3-30B-A3B, Qwen3-235B-A22B, Qwen3-235B-A22B-Instruct-2507, Mistral-Small-3.1-24B-Instruct-2503, Mistral-Small-3.2-24B-Instruct-2506, MiniMax-M1-80k, MiniMax-M1-40k, Kimi-K2-Instruct, DeepSeek-V3-0324, DeepSeek-R1-0528 | Text | Undisclosed | - | [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B); [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B); [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B); [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507); [Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503); [Mistral-Small-3.2-24B-Instruct-2506](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506); [MiniMax-M1-80k](https://huggingface.co/MiniMaxAI/MiniMax-M1-80k); [MiniMax-M1-40k](https://huggingface.co/MiniMaxAI/MiniMax-M1-40k); [Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct); [DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324); [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic WildChat-1M and arena-human-preference-140k from DeepSeek-R1, gemma-2-2b-it, gemma-3-27b-it, gpt-oss-20b, gpt-oss-120b, Mistral-7B-Instruct-v0.3, Mixtral-8x22B-Instruct-v0.1, Nemotron-4-340B-Instruct, NVIDIA-Nemotron-Nano-9B-v2, Phi-4-mini-instruct, Phi-3-small-8k-instruct, Phi-3-medium-4k-instruct, Qwen3-235B-A22B, QwQ-32B | Text | Undisclosed | [WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M); [arena-human-preference-140k](https://huggingface.co/datasets/lmarena-ai/arena-human-preference-140k) | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1); [gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it); [gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it); [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b); [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b); [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3); [Mixtral-8x22B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1); [Nemotron-4-340B-Instruct](https://huggingface.co/nvidia/Nemotron-4-340B-Instruct); [NVIDIA-Nemotron-Nano-9B-v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2); [Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct); [Phi-3-small-8k-instruct](https://huggingface.co/microsoft/Phi-3-small-8k-instruct); [Phi-3-medium-4k-instruct](https://huggingface.co/microsoft/Phi-3-medium-4k-instruct); [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B); [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B) |
| Synthetic Code from Qwen3-32B | Text | Undisclosed | English Common Crawl; English Common Crawl 1.1 | [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) |
| Synthetic OpenCodeReasoning from DeepSeek-R1 | Text | Undisclosed | [OpenCodeReasoning](https://huggingface.co/datasets/nvidia/OpenCodeReasoning) | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) |
| Synthetic OpenCodeReasoning from DeepSeek-R1-0528 | Text | Undisclosed | [OpenCodeReasoning](https://huggingface.co/datasets/nvidia/OpenCodeReasoning) | [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic HackerRank Coding from DeepSeek-R1-0528 | Text | Undisclosed | HackerRank Coding Dataset | [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic LIMO from DeepSeek-R1-0528 | Text | Undisclosed | [LIMO](https://huggingface.co/datasets/GAIR/LIMO) | [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic SCP from DeepSeek-R1-0528 | Text | Undisclosed | [SCP-116K](https://huggingface.co/datasets/EricLu/SCP-116K) | [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic Stack Exchange from DeepSeek-R1-0528 | Text | Undisclosed | [Stack Exchange](https://archive.org/details/stackexchange) | [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic Stack Exchange from gpt-oss-120b and Qwen2.5-32B-Instruct | Text | Undisclosed | [Stack Exchange](https://archive.org/details/stackexchange) | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b); [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) |
| Synthetic Stack Exchange from gpt-oss-120b | Text | Undisclosed | [Stack Exchange](https://archive.org/details/stackexchange) | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) |
| Synthetic Art of Problem Solving from gpt-oss-120b and Qwen2.5-32B-Instruct | Text | Undisclosed | [Art of Problem Solving](https://artofproblemsolving.com/company); [American Mathematics Competitions 8](https://artofproblemsolving.com/wiki/index.php/AMC_8_Problems_and_Solutions); [American Mathematics Competitions 10](https://artofproblemsolving.com/wiki/index.php/AMC_10_Problems_and_Solutions) | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b); [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) |
| Synthetic Common Crawl from Qwen3-30B-A3B | Text | Undisclosed | [Common Crawl](https://commoncrawl.org/) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) |
| Synthetic Wikipedia from Qwen3-30B-A3B | Text | Undisclosed | [Wikimedia](https://dumps.wikimedia.org/) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) |
| Synthetic Essential-Web from Qwen3-30B-A3B and Qwen3-235B-A22B-Thinking-2507 | Text | Undisclosed | [Essential-Web](https://huggingface.co/datasets/EssentialAI/essential-web-v1.0) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B); [Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) |
| Synthetic Essential-Web from gpt-oss-120b | Text | Undisclosed | [Essential-Web](https://huggingface.co/datasets/EssentialAI/essential-web-v1.0) | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) |
| Synthetic Textbook Math from Qwen3-30B-A3B, Qwen3-235B-A22B, phi-4 | Text | Undisclosed | [Common Crawl](https://commoncrawl.org/); [FineMath](https://huggingface.co/datasets/HuggingFaceTB/finemath) | [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B); [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B); [phi-4](https://huggingface.co/microsoft/phi-4) |
| Synthetic Math and Code from DeepSeek-R1 and DeepSeek-R1-0528 | Text | Undisclosed | [Magicoder-Evol-Instruct-110K](https://huggingface.co/datasets/ise-uiuc/Magicoder-Evol-Instruct-110K); [opc-sft-stage2](https://huggingface.co/datasets/OpenCoder-LLM/opc-sft-stage2); [TACO](https://huggingface.co/datasets/BAAI/TACO); [OpenCodeReasoning](https://huggingface.co/datasets/nvidia/OpenCodeReasoning); [OpenMathReasoning](https://huggingface.co/datasets/nvidia/OpenMathReasoning); [NuminaMath CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1); [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic Math from gpt-oss-120b and Qwen2.5-32B-Instruct | Text | Undisclosed | - | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b); [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) |
| Synthetic OpenMathReasoning from gpt-oss-120b and Qwen2.5-32B-Instruct | Text | Undisclosed | [OpenMathReasoning](https://huggingface.co/datasets/nvidia/OpenMathReasoning) | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b); [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) |
| Synthetic KernelBook from DeepSeek-R1-0528 | Text | Undisclosed | [KernelBook](https://huggingface.co/datasets/GPUMODE/KernelBook) | [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic Scale HLE from gpt-oss-120b | Text | Undisclosed | Scale HLE | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) |
| Synthetic CDQuestions from gpt-oss-120b | Text | Undisclosed | [CDQuestions](https://cdquestions.com/) | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) |
| Synthetic GPQA from gpt-oss-120b and Qwen2.5-32B-Instruct | Text | Undisclosed | [Stack Exchange](https://archive.org/details/stackexchange) | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b); [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) |
| Synthetic Vedantu from gpt-oss-120b | Text | Undisclosed | [Vedantu](https://www.vedantu.com/) | [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) |
| Synthetic Search STEM MCQ from Qwen3-235B-A22B and DeepSeek-R1-0528 | Text | Undisclosed | - | [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B); [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic OpenSTEM from Qwen2.5-32B-Instruct and DeepSeek-R1-0528 | Text | Undisclosed | - | [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct); [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic MCQ10 from DeepSeek-R1-0528 | Text | Undisclosed | - | [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| Synthetic MCQ4 from Qwen3-235B-A22B, DeepSeek-R1-0528, and Qwen3-235B-A22B-Instruct-2507 | Text | Undisclosed | - | [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B); [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528); [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) |
| Indic SDG for Nemotron | Text | 711,276,565 indexed source-sequence entries; final training-blend count not confirmed | nvidia/Nemotron-CC-v2 | google/gemma-4-31B-it; google/gemma-4-31B-it-assistant |

## NVIDIA-Sourced Synthetic Datasets (Post-Training)

| Dataset | Modality | Dataset Size | Seed Dataset | Model(s) used for generation |
| :---- | :---- | :---- | :---- | :---- |
| Synthetic Single-Step Tool Use — RL | Text | Approximately 1,433,203 samples | Handwritten prompts; no external seed data | DeepSeek-V3.2; DeepSeek-R1-0528; Qwen3-235B-A22B-Thinking-2507; Qwen3-32B |
| Synthetic Sparse Tables with Mixed Prompts | Text and images | 100,000 records | Generated in-house; no external seed data | None; generated without an SDG model |
| Synthetic Single-Step Tool Use — RL | Text | Approximately 1,433,203 samples | Handwritten prompts; no external seed data | DeepSeek-V3.2; DeepSeek-R1-0528; Qwen3-235B-A22B-Thinking-2507; Qwen3-32B |
| Synthetic Sparse Tables with Mixed Prompts | Text and images | 100,000 records | Generated in-house; no external seed data | None; generated without an SDG model |
| Synthetic Competitive MATH Proofs from DeepSeek-V4-Pro | Text | Undisclosed | [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions] | [deepseek-ai/DeepSeek-V4-Pro] |
| Synthetic Hermes Agent Reasoning Traces | Text | Undisclosed | [lambda/hermes-agent-reasoning-traces] | [hermes-agent-generator] |
| Synthetic Competitive Coding from DeepSeek-V4-Pro | Text | Undisclosed | [NVCompetitiveCodingV1] | [deepseek-ai/DeepSeek-V4-Pro] |
| Synthetic Competitive Science Reasoning from DeepSeek-V4-Pro | Text | Undisclosed | [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions]; [EssentialAI/essential-web-v1.0]; [cdquestions.com]; [Pile-FreeLaw]; [Vedantu]; [askfilo]; [doubtnut]; [ICHO-IPH0 Dataset]; [LIMO dataset (Less is More for Reasoning)]; [AAPT]; [ChemData 700K]; [oMeBench]; [Flavor Analysis and Recognition Transformer]; [ChemCoTBench]; [Llama Nemotron Dataset] | [deepseek-ai/DeepSeek-V4-Pro] |
| Synthetic Competitive MATH CoT and TIR from Nemotron 5.5 | Text | Undisclosed | [Pile-FreeLaw]; [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions] | [Nemotron 5.5] |
| Vendor Terminal Bench-like Tasks from Mercor | Text | Undisclosed | [Terminal bench like tasks curated by the vendor] | [Undisclosed - purchased dataset] |
| Turing Math Data Pack | Text | Undisclosed | [Turing Math Data Pack dataset] | [Undisclosed - purchased dataset] |
| Synthetic Holdout, Skywork, DAPO, and Turing Math from GPT-5.5 | Text | Undisclosed | [DocQA-RL-1.6K]; [DAPO-Math-17k] | [GPT-5.5] |
| Synthetic Long Context RL from QwenLong L1 and DocQA-RL-1.6K | Text | Undisclosed | [DocQA-RL-1.6K] | Undisclosed |
| Synthetic Competitive Coding Gym Tasks | Text | Undisclosed | [NVCompetitiveCodingV1.1] | Undisclosed |
| Synthetic Finance SEC Search Agent from GPT-OSS-120B and Qwen3 | Text | Undisclosed | [SEC filings from sec.gov] | [GPT-OSS-120B]; [Qwen3-235B-A22B-Instruct]; [Qwen3-4B-Instruct] |
| Synthetic Structured Outputs from Qwen3-30B-A3B-Instruct-2507, Qwen3-30B-A3B-Thinking-2507, Qwen3-235B-A22B-Instruct-2507, and Qwen3-235B-A22B-Thinking-2507 | Text | Undisclosed | [Nemotron-RL-agent-structured-outputs-v1] | [Qwen3-30B-A3B-Instruct-2507]; [Qwen3-235B-A22B-Instruct-2507] |
| Synthetic Long Context Equivalence Rule from Qwen3-235B-A22B-Thinking-2507 and DeepSeek-R1 | Text | Undisclosed | [Long-context SFT data] | [Qwen/Qwen3-235B-A22B-Thinking-2507]; [Deepseek-ai/DeepSeek-R1] |
| Synthetic Science RL Data Blend from Qwen2.5-32B | Text | Undisclosed | [doubtnut]; [Pile-FreeLaw]; [Llama Nemotron Dataset]; [askfilo]; [EssentialAI/essential-web-v1.0]; [Vedantu]; [auxiliary_train]; [cdquestions.com]; [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions]; [AAPT]; [ICHO-IPH0 Dataset]; [LIMO dataset (Less is More for Reasoning)] | [Qwen2.5-32B] |
| Synthetic Abstention Data from Nemotron Super v3 | Text | Undisclosed | [Go abstention Dataset] | [nvidia/nvidia/nemotron-3-super-v3] |
| Synthetic Chemistry Data from Nemotron Super v3 | Text | Undisclosed | [ChemData 700K] | [nvidia/nvidia/nemotron-3-super-v3] |
| Synthetic Tool Call Schema for RL | Text | 469,983 | [UltraTool]; [ToolEyes]; [AutoTools]; [API-Bank]; [Nemotron-Personas-USA]; [Salesforce xLAM function-calling]; [Glaive function-calling-v2]; [Agent-Ark/Toucan-1.5M] | [DeepSeek-V3.2]; [GLM-4.6]; [gpt-oss-120b]; [Kimi-K2-Instruct] |
| Synthetic Freeform Text Formatting from GPT-OSS-120B | Text | Undisclosed | [In-house data] | [GPT OSS 120B - Apache 2.0] |
| Synthetic Citation Formatting from GPT-OSS-120B | Text | Undisclosed | [In-house data] | [GPT OSS 120B - Apache 2.0] |
| Droid Harness Pivot Vendor Data | Text | Undisclosed | [Droid Harness Pivot vendor data] | Undisclosed |
| Synthetic HotpotQA Training Data from Qwen3-235B | Text | Undisclosed | [HotpotQA] | [Qwen3-235B] |
| Synthetic Natural Language Math Proofs from Nemotron 5.5 | Text | Undisclosed | [AMC8, AMC10, and AIME problem sets hosted on Art of Problem Solving]; [Pile-StackExchange] | [Nemotron 5.5] |
| Synthetic Stack Overflow OpenQ | Text | Undisclosed | [Pile-FreeLaw] | Undisclosed |
| Chemistry Ether0 Vendor Data | Text | Undisclosed | [Chemistry ether0 vendor data] | Undisclosed |
| Synthetic Litmus-Bench Chemistry from ChEMBL | Text | Undisclosed | [ChEMBL]; [Nemo Gym RL dataset generated from ChEMBL with RDKit] | Undisclosed |
| Synthetic ZINC Chemistry from Nemotron Super v3 | Text | Undisclosed | [ZINC] | [Nemotron Super v3] |
| ARC-AGI Gym Environment | Text | Undisclosed | [ARC-AGI-2] | [ARC-AGI-2] |
| Synthetic Agentic Search Tool-Use from DeepSeek-V3.2 | Text | Undisclosed | [Mercor Data] | [DeepSeek-V3.2] |
| Synthetic Text-To-SQL | Text | 96,564 | [In-house Text-to-SQL data] | [gpt-oss-120b] |
| Dialog Memory Vendor Data | Text | Undisclosed | [Patronus external vendor agreement] | Undisclosed |
| Synthetic Indirect Prompt Injection from Nemotron Super v3 and Qwen3-Next-80B-A3B-Instruct | Text | Undisclosed | [In-house indirect prompt injection data] | [nvidia/nemotron-3-super-v3, qwen/qwen3-next-80b-a3b-instruct] |
| Synthetic Malicious Code and Agentic Security | Text | Undisclosed | [In-house malicious-code / agentic-security data] | Undisclosed |
| Synthetic Single-Step SWE Patch Selection | Text | Undisclosed | [SWE-Gym Dataset]; [SWE Bench Verified Benchmark] | [ground truth and task checks] |
| Synthetic Natural Language Math Final Answers from Nemotron 5.5 | Text | Undisclosed | [AMC8, AMC10, and AIME problem sets hosted on Art of Problem Solving]; [Pile-StackExchange] | [nemotron 5.5] |
| Synthetic Simple Math Prompts for Token Efficiency | Text | Undisclosed | [In-house simple math prompts] | Undisclosed |
| Synthetic Abstention Data from Nemotron Super v3 (CRAG) | Text | Undisclosed | [CRAG] | [nvidia/nvidia/nemotron-3-super-v3] |
| Synthetic Agentless SWE | Text | 242,536 | [SWE-Rebench-V2]; [SWEbench Training Set]; [R2E-Gym/R2E-Gym-Subset]; [SWE-Gym/SWE-Gym]; [SWE-Rebench] | [openai/gpt-oss-120b] |
| Synthetic Agentless SWE from DeepSeek-R1-0528 | Text | 209,976 | [SWE-Bench-Train]; [SWE-Fixer-Train]; [SWE-reBench]; [SWE-Smith] | [deepseek-ai/DeepSeek-R1-0528] |
| Synthetic Agentic CUDA Traces from GLM-4.7 | Text | 2,276 | [Internal CUDA task data] | [GLM-4.7] |
| Synthetic Math Proofs from DeepSeek-V3.2-Speciale | Text | 820,772 | [Nemotron-Math-Proofs-v1] | [SDG: DeepSeek-V3.2-Speciale]; [Filter: proof validation] |
| Synthetic Multilingual SFT from DeepSeek-V3 | Text | 1,245,284 | [Nano v3 SFT data] | [DeepSeek-V3] |
| Synthetic Agentic Code from gpt-oss-120b | Text | 109,086 | [NVAgenticCLIPrompts-v1]; [NVAgenticSkills-v1]; [NVAgenticCLIMultiTurnPrompts-v1] | [openai/gpt-oss-120b] |
| Synthetic Agentic CLI and Web Skills from gpt-oss-120b | Text | 27,418 | [NVAgenticCLIPrompts-v1]; [NVAgenticSkills-v1]; [NVAgenticCLIMultiTurnPrompts-v1]; [NVAgenticCLIPrompts-Web-v1] | [openai/gpt-oss-120b] |
| Synthetic Agentic Coding from gpt-oss-120b | Text | 160,531 | [NVAgenticCLIPrompts-v1]; [NVAgenticSkills-v1]; [NVAgenticCLIMultiTurnPrompts-v1]; [NVAgenticCLIPrompts-Web-v1] | [openai/gpt-oss-120b] |
| Synthetic OpenCode Agentic Tasks from gpt-oss-120b | Text | 614,773 | [NVAgenticCLIPrompts-v1]; [NVAgenticSkills-v1]; [NVAgenticCLIMultiTurnPrompts-v1]; [NVAgenticCLIPrompts-Web-v1] | [openai/gpt-oss-120b] |
| Synthetic SWE Unverified | Text | Undisclosed | [NVAgenticCLIPrompts-v1]; [NVAgenticSkills-v1]; [NVAgenticCLIMultiTurnPrompts-v1]; [NVAgenticCLIPrompts-Web-v1] | [gpt-oss-120b]; [Qwen/Qwen3-Coder-480B-A35B-Instruct]; [GLM-4.7-Flash] |
| Synthetic ARC-AGI Ultra Data | Text | 192,016 | [ARC-AGI-2]; [arc dataset collection] | [ARC-AGI-2] |
| Synthetic LiveCodeBench TIR from DeepSeek-R1-0528 | Text | 1,283,398 | [Nemotron-X training datasets] | [DeepSeek-R1-0528] |
| Synthetic Verilog and SystemVerilog Code from DeepSeek-R1-0528 and GPT-OSS-120B | Text | 1,233,247 | [Verilog/SystemVerilog seed code] | [SDR: DeepSeek R1 0528 and GPT-OSS-120B]; [Filtering: Claude 4 Sonnet] |
| Synthetic Aider Python Tasks from DeepSeek-R1-0528 | Text | 236,099 | [Exercism (GitHub Python)] | [Deepseek R1 0528] |
| Synthetic Chat Reasoning-Off Data from GLM-5 | Text | 646,738 | [lmarena-ai/repochat-arena-preference-4k user prompts] | [Multi-turn conversations generated by GLM-5 with best-of-4 selection via Qwen3-Nemotron-235B-A22B-GenRM] |
| Synthetic Chat Reasoning-On Data from GLM-5 | Text | 644,286 | [lmarena-ai/repochat-arena-preference-4k user prompts]; [lmarena-ai/arena-expert-5k user prompts]; [lmarena-ai/arena-human-preference-55k user prompts]; [lmarena-ai/arena-human-preference-100k user prompts]; [lmarena-ai/arena-human-preference-140k user prompts] | [Multi-turn conversations generated by GLM-5 with best-of-4 selection via Qwen3-Nemotron-235B-A22B-GenRM] |
| Synthetic Multilingual Safety from Riva-Translate-4B-Instruct-v1.1 | Text | 132,067 | [Safety SFT Data: Ultra] | [nvidia/Riva-Translate-4B-Instruct-v1.1] |
| Synthetic Science Reasoning Effort Medium | Text | 502,722 | [science-reasoning-effort-medium-v0] | Undisclosed |
| Synthetic Telecom Tool-Use Trajectories from gpt-oss-120b | Text | 12,455 | [Existing Tau2 telecom trajectories originally generated with DeepSeek V3.2] | [gpt-oss-120b] |
| Synthetic Terminal Bench Data from OpenReasoningv2 | Text | Undisclosed | [OpenCodeReasoningv2]; [OpenMathReasoning]; [nemo-swe-bench-repos]; [SWE-Rebench]; [SWE-Fixer-110K] | [OpenReasoningv2] |
| Synthetic Tulu Instruction Following from DeepSeek-R1-0528 | Text | 105,361 | [Nemotron-X training datasets] | [DeepSeek-R1-0528] |
| Synthetic Instruction Following from gpt-oss-120b | Text | 151,988 | [IFEval]; [IFEvalG] | [gpt-oss-120b] |
| Synthetic Instruction Following for RL | Text | Undisclosed | [WildChat-1M]; [LMSYS-340B-Eval Dataset]; [LMSYS-Chat-1M Prompts]; [IFEval]; [IFEvalG] | [Qwen/Qwen3-235B-A22B-Thinking-2507]; [gpt-oss-120b]; [Qwen3-235B-A22B-Instruct-2507] |
| Synthetic Identity Data from Qwen3-Next-80B-A3B-Instruct and Qwen3-235B-A22B-Instruct-2507 | Text | 25,992 | [Hand-written prompts] | [Qwen3-Next-80B-A3B-Instruct]; [Qwen3-235B-A22B-Instruct-2507] |
| Synthetic Terminus Ultra Agentic Reasoning Blend | Text | 96,881 | [ARC-AGI-2]; [OpenCodeReasoningv2]; [OpenMathReasoning]; [SWE-Fixer-110K]; [SWE-Rebench]; [SWE-Smith] | [DeepSeek-V3.2]; [Qwen3-235B-A22B-Thinking-2507]; [Ring-1T]; [Kimi-K2.5]; [GLM-4.7-FP8]; [Qwen3-Next-80B-A3B-Thinking]; [gpt-oss-120b]; [Ministral-3-14B-Reasoning-2512]; [LM-4.5-Air-FP8] |
| Synthetic STEM from Qwen3-235B-A22B-Thinking-2507 | Text | 1,174,694 | [IChO-IPhO-RL-v2]; [Physics-Big Dataset]; Scale HLE; [OpenMathReasoning]; [OpenCodeReasoning] | [Qwen3-235B-A22B-Thinking-2507] |
| Synthetic STEM from Qwen3-235B-A22B-Instruct-2507 and gpt-oss-120b | Text | Undisclosed | [arXiv]; [National Institutes of Health ExPorter]; [BioRxiv]; [PMC Article]; [USPTO Backgrounds]; [peS2o]; Global Regulation; [CORE]; [PG-19]; [DOAB CC BY & CC BY-SA subset]; [NDLTD] | [Qwen3-235B-A22B-Instruct-2507]; [gpt-oss-120b] |
| Translation Data from TAUS | Text | 1,618,055 | [TAUS proprietary dataset] | Undisclosed |
| Synthetic Art of Problem Solving and Stack Exchange from gpt-oss-120b, Qwen2.5-32B-Instruct, and Goedel-Prover-V2-32B | Text | 860,469 | [Nemotron-Math-Proofs-v1] | [Goedel-Prover-V2-32B] |
| Synthetic Art of Problem Solving and Stack Exchange from gpt-oss-120b | Text | 1,201,815 | [Upstream released math dataset]; [AoPS]; [StackOverflow / StackExchange] | [gpt-oss-120b] |
| Synthetic Multilingual Science and Code data from DeepSeek-R1, DeepSeek-R1-0528, Qwen2.5-32B-Instruct, and Qwen3-235B-A22B, translated with Qwen2.5-32B-Instruct and Qwen2.5-14B-Instruct | Text | Undisclosed | [Nano-V3 SFT Data (without tool call)] | [Qwen/Qwen2.5-14B-Instruct]; [Qwen/Qwen3-4B-Thinking-2507] |
| Synthetic Multilingual Science and Code data from DeepSeek-R1, DeepSeek-R1-0528, Qwen2.5-32B-Instruct, and Qwen3-235B-A22B, translated with Qwen2.5-32B-Instruct and Qwen2.5-14B-Instruct (Stack Exchange lineage) | Text | Undisclosed | [Stack Exchange]; [SCP-116K]; [LIMO]; [TACO]; Code Contest; Codeforces | [DeepSeek-R1]; [DeepSeek-R1-0528]; [Qwen2.5-32B-Instruct]; [Qwen3-235B-A22B] |
| Synthetic Search Graph Walk | Text | 6,977 | [Wikidata / Wikipedia KnowledgeBase] | [MiniMaxAI/MiniMax-M2] |
| Synthetic Agentic Diverse Domains | Text | 281,537 | [Handwritten prompts (synthetic; no external seed data used)] | [SDG model: deepseek-ai/DeepSeek-V3.2, deepseek-ai/DeepSeek-R1-0528, Qwen/Qwen3-235B-A22B-Thinking-2507, Qwen/Qwen3-32B]; [Filtering model: openai/gpt-oss-120b, Qwen/Qwen3-32B, Qwen/Qwen3-235B-A22B-Instruct-2507] |
| Synthetic Long Context from Qwen3-235B-A22B-Instruct-2507 | Text | Undisclosed | [Long-context SFT seed blend (pre-training blend + nano-v1 post-training data)]; [Long-context SFT data: lc_nothink 256k, MRCR 200k, RULER 256k]; [AALCR seed blend: SEC Filings, CC, Wikipedia, FinePDFs, ArXiv, Pile-NIH ExPorter, BioRxiv, PMC Article, USPTO Backgrounds, peS2o, Global Regulations, CORE, Gutenberg (PG-19), DOAB CC-BY, NDLTD, Amps, StackExchange, MathPile, Numinas] | [Qwen/Qwen3-235B-A22B-Thinking-2507]; [deepseek-ai/DeepSeek-R1]; [Qwen3-30B-A3B] |
| Synthetic Nemotron Math SFT from DeepSeek-V3.2-Speciale | Text | 1,900,553 | [Nemotron-Math-v2 (AOPS and StackExchange-math problems)] | [DeepSeek-V3.2-Speciale] |
| Synthetic Nemotron Math TIR from DeepSeek-V3.2 | Text | 1,789,258 | [Nemotron-Math-v2 (AOPS and StackExchange-math problems)] | [DeepSeek-V3.2] |
| Synthetic NemoCascade OCR Distillation from gpt-oss-120b | Text | 682,864 | [Nemotron-X training datasets] | [gpt-oss-120b] |
| Synthetic CUDA 100k | Text | 93,086 | [KernelBook]; [HuggingFace Transformers]; [FlashInfer] | [gpt-oss-120b]; [DeepSeek-R1-0528] |
| Synthetic Science MCQ and QA Diversity from GPT-OSS and Kimi-K2 | Text | 30,358 | [doubtnut]; [Pile-FreeLaw]; [Llama Nemotron Dataset]; [askfilo]; [EssentialAI/essential-web-v1.0]; [Vedantu]; [auxiliary_train]; [cdquestions.com]; [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions]; [AAPT]; [ICHO-IPH0 Dataset]; [LIMO dataset (Less is More for Reasoning)] | [GPT-OSS]; [Kimi-K2] |
| Synthetic Science HLE with Python from GPT-OSS and Kimi-K2 | Text | 85,184 | [doubtnut]; [Pile-FreeLaw]; [Llama Nemotron Dataset]; [askfilo]; [EssentialAI/essential-web-v1.0]; [Vedantu]; [auxiliary_train]; [cdquestions.com]; [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions]; [AAPT]; [ICHO-IPH0 Dataset]; [LIMO dataset (Less is More for Reasoning)] | [GPT-OSS]; [Kimi-K2] |
| Synthetic Science Search and Python from GPT-OSS and Kimi-K2 | Text | 6,179 | [doubtnut]; [Pile-FreeLaw]; [Llama Nemotron Dataset]; [askfilo]; [EssentialAI/essential-web-v1.0]; [Vedantu]; [auxiliary_train]; [cdquestions.com]; [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions]; [AAPT]; [ICHO-IPH0 Dataset]; [LIMO dataset (Less is More for Reasoning)] | [GPT-OSS]; [Kimi-K2] |
| Synthetic Science Search from GPT-OSS and Kimi-K2 | Text | 32,554 | [doubtnut]; [Pile-FreeLaw]; [Llama Nemotron Dataset]; [askfilo]; [EssentialAI/essential-web-v1.0]; [Vedantu]; [auxiliary_train]; [cdquestions.com]; [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions]; [AAPT]; [ICHO-IPH0 Dataset]; [LIMO dataset (Less is More for Reasoning)] | [GPT-OSS]; [Kimi-K2] |
| Synthetic Finance Reasoning from GPT-OSS-120B and Qwen3-235B-A22B-Instruct-2507 | Text | 326,700 | [SEC filings] | [GPT-OSS-120B, Qwen3-235B-A22B-Instruct-2507] |
| Synthetic Science Diversity MCQ from GPT-OSS and Kimi-K2 | Text | 532,942 | [doubtnut]; [Pile-FreeLaw]; [Llama Nemotron Dataset]; [askfilo]; [EssentialAI/essential-web-v1.0]; [Vedantu]; [auxiliary_train]; [cdquestions.com]; [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions]; [AAPT]; [ICHO-IPH0 Dataset]; [LIMO dataset (Less is More for Reasoning)] | [GPT-OSS]; [Kimi-K2] |
| Synthetic Science Diversity OpenQ from GPT-OSS and Kimi-K2 | Text | 131,045 | [doubtnut]; [Pile-FreeLaw]; [Llama Nemotron Dataset]; [askfilo]; [EssentialAI/essential-web-v1.0]; [Vedantu]; [auxiliary_train]; [cdquestions.com]; [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions]; [AAPT]; [ICHO-IPH0 Dataset]; [LIMO dataset (Less is More for Reasoning)] | [GPT-OSS]; [Kimi-K2] |
| Synthetic Science Reasoning No-Tool from GPT-OSS and Kimi-K2 | Text | 2,085,600 | [doubtnut]; [Pile-FreeLaw]; [Llama Nemotron Dataset]; [askfilo]; [EssentialAI/essential-web-v1.0]; [Vedantu]; [auxiliary_train]; [cdquestions.com]; [AMC 8 Problems and Solutions, AMC 10 Problems and Solution, and AIME Problems and Solutions]; [AAPT]; [ICHO-IPH0 Dataset]; [LIMO dataset (Less is More for Reasoning)] | [GPT-OSS]; [Kimi-K2] |
| Synthetic Text-To-SQL from gpt-oss-120b | Text | Undisclosed | [In-house Text-to-SQL data] | [gpt-oss-120b] |
| Synthetic Tool Call Schema for RL (extended) | Text | 707,967 | [UltraTool]; [ToolEyes]; [AutoTools]; [API-Bank]; [Nemotron-Personas-USA]; [Salesforce xLAM function-calling]; [Glaive function-calling-v2]; [Agent-Ark/Toucan-1.5M] | [DeepSeek-V3.2]; [GLM-4.6]; [gpt-oss-120b]; [Kimi-K2-Instruct] |
| Synthetic Safety from gemma-3-4b-it, Nemotron-Nano-9B-v2, and gpt-oss-120b | Text | 44,091 | [Safety SFT Data] | [google/gemma-3-4b-it]; [Nemotron-Nano-9B-v2]; [gpt-oss-120b] |
| Synthetic Safety from DeepSeek-R1-0528, gpt-oss-120b, DeepSeek-R1-Distill-Qwen-7B, and Mixtral-8x7B-v0.1 | Text | Undisclosed | [Nemotron Content Safety Dataset V2]; [Gretel Synthetic Safety Alignment Dataset]; [RedTeam-2K]; [Malicious Tasks]; [Nemotron-Personas-USA] | [DeepSeek-R1-0528]; [gpt-oss-120b]; [DeepSeek-R1-Distill-Qwen-7B]; [Qwen3-30B-A3B-Thinking-2507]; [Qwen3-235B-A22B-Instruct-2507]; [Mixtral-8x7B-v0.1] |
| Synthetic Tool Calling from Qwen3-235B-A22B-Thinking-2507 and Qwen3-Next-80B-A3B-Thinking | Text | Undisclosed | [ToolBench]; [glaive-function-calling-v2]; [APIGen Function-Calling]; [Nemotron-Personas-USA] | [Qwen3-235B-A22B-Thinking-2507]; [Qwen3-Next-80B-A3B-Thinking] |
| Synthetic Chat from gpt-oss-120b, Mixtral-8x22B-Instruct-v0.1, Qwen3-235B-A22B-Instruct-2507, and Qwen3-235B-A22B-Thinking-2507 | Text | Undisclosed | [C4]; [LMSYS-Chat-1M]; [ShareGPT]; [GSM8K]; [PRM800K]; [FinQA]; [WikiTableQuestions]; [Riddles]; [glaive-function-calling-v2]; [SciBench]; [tigerbot-kaggle-leetcodesolutions-en-2k]; [OpenBookQA]; [Advanced Reasoning Benchmark]; Software Heritage; [Khan Academy Math Keywords]; [WildChat-1M]; [Nemotron-Personas-USA] | [gpt-oss-120b]; [Mixtral-8x22B-Instruct-v0.1]; [Qwen3-235B-A22B-Instruct-2507]; [Qwen3-235B-A22B-Thinking-2507] |
| Synthetic Tool Use Interactive Agent from gpt-oss-120b, DeepSeek-R1-0528, Qwen3-32B, and Qwen3-235B-A22B-Thinking-2507 | Text | Undisclosed | NVIDIA Internal | [gpt-oss-120b]; [DeepSeek-R1-0528]; [Qwen3-32B]; [Qwen3-235B-A22B-Thinking-2507] |
| Synthetic DocFinQA and SWE-smith from Qwen3-Coder-480B-A35B-Instruct and Kimi-K2-Thinking | Text | Undisclosed | [DocFinQA]; [SWE-smith] | [Qwen3-Coder-480B-A35B-Instruct]; [Kimi-K2-Thinking] |
| Synthetic SWE-Gym from Qwen3-Coder-480B-A35B-Instruct | Text | Undisclosed | [SWE-Gym] | [Qwen3-Coder-480B-A35B-Instruct] |
| Synthetic SWE-Gym and R2E-Gym-Subset from Qwen3-Coder-480B-A35B-Instruct | Text | Undisclosed | [SWE-Gym]; [R2E-Gym-Subset] | [Qwen3-Coder-480B-A35B-Instruct] |
| Synthetic SWE-Gym and R2E-Gym-Subset from DeepSeek-R1-0528 | Text | Undisclosed | [SWE-Gym]; [R2E-Gym-Subset] | [DeepSeek-R1-0528] |
| Synthetic HelpSteer, LMSYS-Chat-1M, and Nemotron-Personas-USA from gpt-oss-120b, Qwen3-235B-A22B-Instruct-2507, and Qwen3-235B-A22B-Thinking-2507 | Text | Undisclosed | [HelpSteer2]; [HelpSteer3]; [LMSYS-Chat-1M]; [Nemotron-Personas-USA] | [gpt-oss-120b]; [Qwen3-235B-A22B-Instruct-2507]; [Qwen3-235B-A22B-Thinking-2507] |
| Synthetic Nemotron-Personas-USA from gpt-oss-120b and Qwen3-8B | Text | Undisclosed | [Nemotron-Personas-USA] | [gpt-oss-120b]; [Qwen3-8B] |
| Vendor Terminal Bench-like Tasks (Droid) | Text | Undisclosed | [Droid Harness Pivot vendor data] | Undisclosed |
| Synthetic BabyVisionQA Reasoning — Combined SFT | Text and images | 135,207 records | Procedurally generated BabyVision-style visual-reasoning images | Qwen3.5-397B-A17B-FP8 |
| Synthetic BabyVision Tool-Calling SFT, Relative-Path-Corrected Variant | Text and images | 81,494 records | NVIDIA internal BabyVision tool-calling prompts and media | Qwen3.5-397B-A17B-FP8; Kimi-K2.6 |
| Synthetic Chinese OCR v5, NMH5R | Text and images | 29,108 records | Webster's Unabridged Dictionary; rendered Chinese text mixed with English words | Undisclosed; synthetic text rendering is described |
| Synthetic Chinese OCR v5, Augmented and Cleaned | Text and images | 28,576 records | Webster's Unabridged Dictionary; augmented synthetic Chinese OCR images | Undisclosed; synthetic text rendering is described |
| Synthetic Multimodal Safety, Energon Format | Text and images | 22,560 records | NVIDIA Safety-team text prompts and safe responses | Edify (image generation) |
| Synthetic Multimodal Safety, NMH5R and Safety-Filtered | Text and images | 22,541 records | Multimodal safety records with Edify-generated images | Edify (image generation) |
| Synthetic ASCII OCR v5, NMH5R | Text and images | 14,533 records | Webster's Unabridged Dictionary; synthetic ASCII renderings | Undisclosed; synthetic text rendering is described |
| Synthetic English OCR v5, NMH5R | Text and images | 14,525 records | Webster's Unabridged Dictionary; synthetic English renderings | Undisclosed; synthetic text rendering is described |

## Language Distribution in Post-Training

For our post-training recipe, we focused on the following languages in addition to English: French, German, Italian, Japanese, Spanish, and Chinese. Those languages were represented in the form of multilingual reasoning and translation tasks.

</details>

### Additional Training Data

| Data | Composition and Purpose |
|:---|:---|
| Indic continued pre-training | 100B tokens: 10B selected Indic tokens and 90B tokens from the preceding blend. |
| Software-engineering mid-training | 67B tokens: whole repositories (20%), issue–pull-request pairs (41%), commit diffs (3%), build and CI logs (1%), agent traces (10%), pre-training replay (20%), and long-context data (5%). Sources are decontaminated against SWE-bench and Terminal-Bench repositories. |
| Long-context pre-training | A 35B-token extension to 1M context, followed by a 9B-token long-context recovery stage. |
| Vision-language data | Image and video data from the Nemotron 3 Nano Omni training corpus, including visual question answering, charts, tables, OCR, multi-page documents, visual grounding, and video understanding. |

| Post-Training Data | Composition and Purpose |
|:---|:---|
| Additional synthetic vision data | Chart understanding, grounded perception, multimodal reasoning, and visual tool-use trajectories, including data generated with Qwen3.5 and Kimi models. |
| Reasoning trajectories | Mathematics and STEM responses generated with Kimi K3; mathematical proofs generated with DeepSeek V4 Pro; competitive-programming trajectories generated with GLM-5.2. |
| Chat and safety | Refreshed chat responses from Qwen, Kimi, and Gemma models, with additional safety data. |
| Long-context supervised data | 512K-context data, synthetic graph reasoning and transduction tasks, long-horizon search and coding trajectories, and documents containing up to hundreds of pages. |
| Long-document translation | Chunked translations of PG19 and FinePDFs-Edu documents generated with DeepSeek V4 Flash. |

## Testing Datasets

**Data Collection Method:** Hybrid: automated, manually-collected, and synthetic  
**Labeling Method:** Hybrid: automated, manually-labeled, and synthetic  
**Properties:** Standard benchmarks and task-specific test suites covering reasoning, coding, tool use, instruction following, long context, and visual understanding.

## Evaluation Datasets

**Data Collection Method:** Hybrid: automated, manually-collected, and synthetic  
**Labeling Method:** Hybrid: automated, manually-labeled, and synthetic  
**Properties:** Standard benchmarks and task-specific test suites covering reasoning, coding, tool use, instruction following, long context, and visual understanding.

## Inference

**Acceleration Engine:** vLLM + Dynamo  
**Test Hardware:** NVIDIA Hopper (H200)

## Additional Details

### Model Design

The model combines sparse expert computation, attention, and Mamba-2 layers to support long-context processing. The vision encoder and connector turn visual inputs into representations processed by the language backbone. A shared MTP head predicts future tokens recursively for speculative decoding.

The model supports up to 1M tokens of context. The prompt, visual inputs, conversation history, tool results, and generated response share this context window. Individual deployment recipes may use a smaller context window to accommodate the available GPU memory and concurrency.

### Training Methodology

**Stage 1: Foundation and Multi-Token Prediction**

The language backbone is initialized from Nemotron 3 Super Base. A shared MTP head is trained for 100B tokens while the backbone remains frozen, followed by 1T tokens of distillation from Nemotron 3 Ultra Base.

**Stage 2: Continued Pre-Training and Mid-Training**

The model undergoes 100B tokens of Indic continued pre-training, a 35B-token extension to 1M context, 67B tokens of software-engineering mid-training at 256K context, and a final 9B-token long-context recovery stage. Software-engineering data includes repositories, issue–pull-request pairs, commit diffs, build and CI logs, and agent trajectories.

**Stage 3: Vision-Language Training**

A C-RADIO vision encoder and connector extend the language backbone to visual inputs, including images, document pages, and video frames.

**Stage 4: Supervised Fine-Tuning**

A two-stage supervised fine-tuning pipeline jointly trains the language and vision components on vision, reasoning, code, tools, chat, safety, and long-context data. Training uses packed sequences of up to 524,288 tokens.

**Stage 5: Reinforcement Learning and Distillation**

Reinforcement learning with verifiable rewards, reinforcement learning from human feedback, and specialized teacher training improve reasoning, agentic, chat, and vision capabilities. Multi-teacher on-policy distillation consolidates these capabilities into a single model.

**Stage 6: MTP Boosting**

The MTP head is further trained against the frozen post-trained backbone to improve speculative-decoding acceptance.

**Stage 7: Quantization and Quantization-Aware Distillation**

The model is quantized with [NVIDIA Model Optimizer](https://github.com/NVIDIA/Model-Optimizer) and refined through quantization-aware distillation using the supervised fine-tuning data blend. The vision encoder, connector, Mamba convolutions, and embeddings remain in BF16, and the MoE router remains in FP32. Inference uses W4A4 on Blackwell and W4A16 on non-Blackwell platforms, according to the serving configuration.

### Recommended Sampling

Text: temperature 1.0, top_p 0.95; vision: temperature 0.6, top_p 0.95. Reasoning mode is configurable through the chat template (`enable_thinking=True/False`).

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please make sure you have proper rights and permissions for all input image and video content.

Model outputs may contain errors. Applications should validate generated answers, code, and tool arguments, and provide appropriate safeguards and human oversight for their intended use. We advise against removing provided safety guardrails without substantially similar safeguards appropriate for the application.

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.

For more detailed information on ethical considerations for this model, please see the Explainability, Bias, Safety & Security, and Privacy subcards in the ModelCard++ tab.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Specifications

- **Context Length:** 262,144 tokens
- **Parameters:** 123,611,012,096
- **Input:** Text, Image, Video
- **Output:** Text

## Capabilities

- **Function Calling:** Supported
- **Structured Output:** Supported
- **Reasoning:** Supported

## Bias

# NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 — Bias Subcard

| Field | Response |
| :---- | :---- |
| Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing: | None |
| Bias Metric (If Measured): | [BBQ Accuracy Scores in Ambiguous Contexts](https://github.com/nyu-mll/BBQ/) |
| Which characteristic (feature) show(s) the greatest difference in performance?: | The model shows high variance in the characteristics when it is used with a high temperature. |
| Measures taken to mitigate against unwanted bias: | Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF) employed to calibrate the model’s reasoning capabilities to maintain logical consistency and appropriate complexity when interacting with or interpreting data from diverse age demographics. |
| If using internal data, description of methods implemented in data acquisition or processing, if any, to address the prevalence of identifiable biases in the training, testing, and validation data: | The training datasets contain a large amount of synthetic data generated by LLMs. We manually curated prompts. |
| Tools used to assess statistical imbalances and highlight patterns that may introduce bias into AI models: | [BBQ](https://github.com/nyu-mll/BBQ/) |
| Tools used to assess statistical imbalances and highlight patterns that may introduce bias into AI models: | These datasets, such as web-scraped finance reasoning data derived from SEC EDGAR filings, science and math problem datasets, OpenResearcher/source-document datasets, Common Crawl, CC-News, Wikimedia, long-context document datasets, and image datasets including BLIP3, PixMo, COCO-derived collections, and document, chart and page-image datasets, do not collectively or exhaustively represent all demographic groups (and proportionally therein).  For instance, these datasets do not contain explicit mentions of demographic classes such as age, gender, or ethnicity in approximately 97% to 99.9% of finance reasoning samples and in over 85% of samples across the broader assessed text datasets, and automated person-presence screening did not detect a person in approximately 86% of the images analyzed across 40 image datasets (and in over 98% of images in 18 document-, chart- and filing-page-focused datasets). In the subset where such terms or people are present, these datasets contain representational skews; for example, in text, ethnicity mentions are often dominated by Middle Eastern contexts (found in finance documents) or "White," "Two or more," and "Black or African American" as the most frequent ethnic identifiers, while references categorized as male-only significantly outnumber those categorized as female-only. In image datasets, where person-present signals were identified, these datasets contain uneven representation splits across the measured visual taxonomies:  apparent age was predominantly adult, followed by elder; gender presentation skewed male; and automated apparent-ethnicity candidates were led by White and Asian. To mitigate these imbalances, we recommend considering evaluation techniques such as bias audits, task-specific fairness evaluation, red-teaming, fine-tuning with demographically balanced datasets, and mitigation strategies such as counterfactual data augmentation to align with the desired model behavior. This evaluation used a 1,000-3,000-sample subset per dataset, identified as the optimal threshold for maximizing embedder accuracy, and includes outputs from uncalibrated embedders; as such, certain limitations may exist in the reliability |
| Unwanted Bias Testing: | Constrained to English-language inputs. Multi-lingual parity is not currently claimed or guaranteed. |

## Explainability

# NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 — Explainability Subcard

| Field | Response |
| :---- | :---- |
| Intended Task/Domain | Reasoning, coding, tool use, document understanding, image understanding, and video understanding. |
| Model Type | Mamba-2–Transformer hybrid Mixture of Experts (MoE) with a C-RADIO vision encoder and a vision-language connector; NVFP4 quantization with quantization-aware distillation from the BF16 model. |
| Intended Users: | Generative AI creators working with conversational AI models and image content. |
| Output | Text; reasoning mode is configurable through the chat template. Input and output tokens share a context window of up to 1M tokens. |
| Tools used to evaluate datasets to identify synthetic data and ensure data authenticity. | We used a Gemma-3 4B-based filtering model fine-tuned on [Nemotron Content Safety Dataset v2](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) to ensure the quality of synthetic data. |
| Describe how the model works | Visual inputs are encoded by the C-RADIO vision encoder and connector and processed by the hybrid language backbone. The model has 120B total parameters and 12B active parameters. A shared Multi-Token Prediction (MTP) head supports native speculative decoding. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Age, Disability Status, Gender Identity, Nationality, Physical Appearance, Ethnicity, Socioeconomic Status, Sexual Orientation, Religion |
| Technical Limitations & Mitigation: | This model performs particularly well in instruction following regimes, as such may be strongly influenced by untrusted inputs and should be paired with appropriate guardrails and data filtering to better align use-case behaviors when exposed to such data. |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics: | Accuracy, Throughput, and User-side throughput. See Benchmarks in the Overview tab for BF16 and NVFP4 reference scores and evaluation conditions. |
| Potential Known Risks: | The model was optimized explicitly for instruction following and as such is more susceptible to prompt injection and jailbreaking in various forms as a result of its instruction tuning. This means that the model should be paired with additional rails or system filtering to limit exposure to instructions from malicious sources -- either directly or indirectly by retrieval (e.g. via visiting a website) -- as they may yield outputs that can lead to harmful, system-level outcomes up to and including remote code execution in agentic systems when effective security controls including guardrails are not in place. The model may generate answers that may be inaccurate, omit key information, include irrelevant or redundant text, or produce socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. The model may exhibit self-anthropomorphism (e.g., displaying human-like characteristics in dialogue, such as expressing preferences and emotions). |
| Licensing: | Use of this model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1) (OpenMDW-1.1). |

## Privacy

# NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 — Privacy Subcard

| Privacy Information |
| :--- |
| Nemotron 3.5 Super VL was trained on large-scale publicly available data that may contain images, audio-video, and text relating to people. NVIDIA collected and used this data in compliance with applicable data protection and privacy laws. This model was not designed to derive insights or otherwise learn from any personal data contained in the datasets. |
| NVIDIA uses a combination of filters, data minimization techniques, and other guardrails to help prevent personal data from being recited by our models. We employ automated tools and data processing techniques during pre-training or training to identify and filter certain categories of personal data. |
| Please review NVIDIA's [Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) for more information. |

## Safety & Security

# NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 — Safety & Security Subcard

| Field | Response |
| :---- | :---- |
| Model Application Field(s): | Chat, Instruction Following, Chatbot Development, Code Generation, Reasoning, Customer Service |
| Describe the life critical impact (if present). | Not Applicable |
| Description of methods implemented in data acquisition or processing, if any, to address other types of potentially harmful data in the training, testing, and validation data: | We used a guard model for content safety to exclude potentially harmful data from training.  |
| Description of any methods implemented in data acquisition or processing, if any, to address illegal or harmful content in the training data, including, but not limited to, child sexual abuse material (CSAM) and non-consensual intimate imagery (NCII) | We used a Gemma-3 4B-based guard model trained on [Nemotron Content Safety Dataset v2](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) for content safety to exclude potentially illegal or harmful content from the training. |
| Use Case Restrictions: | Use of this model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1) (OpenMDW-1.1).|
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to. |
| This AI model was developed based on our policies to ensure responsible data handling and risk mitigation. The datasets used for training have been scanned for harmful content and illegal content, consistent with our policies including scanning for Child Sexual Abuse Material (CSAM). Ongoing review and monitoring mechanisms are in place based on our policies and to maintain data integrity. | True. We use [Nemotron Content Safety Dataset V2](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) and an internal safety dataset specialized for minority sexuality for content safety evaluation to ensure the safety of this model. |

## Prototype

```python
import os
from openai import OpenAI

client = OpenAI(
base_url = "https://integrate.api.nvidia.com/v1",
api_key = os.environ["NVIDIA_API_KEY"]
)

completion = client.chat.completions.create(
model="",
messages=[{"role": "user", "content": ""}],
temperature=,
top_p=,
max_tokens=,

extra_body={"chat_template_kwargs": {"enable_thinking": True}},
stream=NaN
)

reasoning = getattr(completion.choices[0].message, "reasoning_content", None)
if reasoning:
print(reasoning)
print(completion.choices[0].message.content or "")
```

```python
import os
from langchain_nvidia_ai_endpoints import ChatNVIDIA

client = ChatNVIDIA(
base_url="https://integrate.api.nvidia.com/v1",
model="",
api_key=os.environ["NVIDIA_API_KEY"],
temperature=,
top_p=,
max_completion_tokens=,

)

client = client.bind(**{"chat_template_kwargs": {"enable_thinking": True}})

response = client.invoke([{"role": "user", "content": ""}])
if response.additional_kwargs and "reasoning_content" in response.additional_kwargs:
print(response.additional_kwargs["reasoning_content"])
print(response.content)
```

```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
apiKey: process.env.NVIDIA_API_KEY,
baseURL: 'https://integrate.api.nvidia.com/v1',
})

async function main() {
const completion = await openai.chat.completions.create({
model: "",
messages: [{"role":"user","content":""}],
temperature: ,
top_p: ,
max_tokens: ,

chat_template_kwargs: {"enable_thinking":true},
stream: 
})

const reasoning = completion.choices[0]?.message?.reasoning_content;
if (reasoning) process.stdout.write(reasoning + "\n");
process.stdout.write(completion.choices[0]?.message?.content || '');

}

main();
```

```bash
invoke_url='https://integrate.api.nvidia.com/v1/chat/completions'

payload=$(cat <<'JSON'
{
"model": "",
"messages": [{"role":"user","content":""}],
"temperature": ,
"top_p": ,
"max_tokens": ,

"chat_template_kwargs": {"enable_thinking":true},
"stream": 
}
JSON
)

printf 'header = "Authorization: Bearer %s"\n' "$NVIDIA_API_KEY" | \
curl --fail-with-body --config - -sS \
--request POST \
--url "$invoke_url" \
--header "Accept: application/json" \
--header "Content-Type: application/json" \
--data "$payload"
```