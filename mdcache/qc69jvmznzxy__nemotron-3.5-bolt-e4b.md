---
title: "Nemotron 3.5 Bolt E4B"
publisher: "nvidia"
type: "endpoint"
updated: "2026-10-22T21:51:25.171Z"
description: "Compact text model for reasoning, tool calling, and agentic chat."
canonical: "https://build.nvidia.com/nvidia/nemotron-3.5-bolt-e4b"
---

# Nemotron-3.5-Bolt-E4B-BF16

## Model Overview

**Model Developer:** NVIDIA Corporation

**Model Dates:** December 2025 - May 2026

**Data Freshness:**

* The post-training data has a cutoff date of May 2026.

## Description

**Nemotron-3.5-Bolt-E4B-BF16** is a large language model (LLM) further post-trained from [Gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it) by NVIDIA. This is the full-precision (BF16) release of Nemotron 3.5 Bolt E4B.

This model is ready for commercial or non‑commercial use.

## License/Terms of Use

**GOVERNING HOSTING TERMS:** Use of the API is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1).

**ADDITIONAL INFORMATION:** [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Benchmarks

### Reasoning Benchmark Evaluations

We evaluated our model on the following benchmarks:

Accuracy numbers are measured by NVIDIA under a consistent harness (NeMo Gym / Nemo Evaluator SDK); they may differ from vendors' self-reported numbers.

| Benchmark | Gemma4-E4B-it | Qwen3.5-4B | Nemotron-3.5-Bolt-E4B-BF16 |
| :--- | :--- | :--- | :--- |
| MultiChallenge | 42.1 | 49 | **59.32** |
| RoleMRC | **77.00** | 64.40 | 74.30 |
| RoleBench | 59.57 | 59.43 | **62.18** |
| MiniMax Roleplay | **65.56** | 43.33 | 51.67 |
| EQ-Bench v3 | **57.15** | 50.30 | 54.05 |
| BFCL v3 | 66.29 | **71.60** | 71.33 |
| ToolSandbox | 43.37 | 60.82 | **61.11** |
| Tau2-Bench | 38.72 | **79.90** | 63.23 |
| IHEval | 73.82 | 71.90 | **86.04** |
| AgentIF | 22.63 | 18.26 | **23.48** |
| StructEval-T | 78.09 | 76.30 | **80.18** |
| IFBench | 42.80 | **58.75** | 58.72 |
| InverseIFEval | 41.30 | 29.64 | **51.49** |
| RULER (64K) | 89.15 | **95.18** | 86.47 |
| LongMemEval | 70.60 | **72.40** | 71.80 |
| LongBench v2 (48K) | 45.00 | **63.60** | 48.40 |
| AA-LCR | 36.50 | **57.50** | 42.25 |
| SysBench | 65.64 | 67.80 | **70.36** |
| GaRAGe | 37.80 | 15.53 | **45.03** |
| RAGTruth | **78.00** | 75.50 | 74.57 |
| RelyToolBench | 68.4 | 40.7 | **70.58** |

### Deployment Geography: Global

### Use Case

Nemotron-3.5-Bolt-E4B-BF16 is the full-precision release of a general purpose reasoning and chat model, and is intended primarily for **customization and post-training** rather than direct production inference. It is intended to be used by developers who want to: post-train the model on their own data (SFT, RL via [NeMo RL](https://github.com/NVIDIA-NeMo/RL) and [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym), or distillation), adapt it to a domain or task, produce quantized variants (NVFP4, W4A16, GGUF) for their own deployment targets, or run full-precision research and evaluation. English and coding languages are the primary languages, with Spanish, French, German, Italian, and Japanese also supported.

### Release Date

**Build.NVIDIA.com:** 10/23/2026 via [Nemotron 3.5 Bolt E4B](https://build.nvidia.com/nvidia/nemotron-3.5-bolt-e4b)

Hugging Face 10/23/2026 via https://huggingface.co/nvidia/Nemotron-3.5-Bolt-E4B-BF16

## Model Architecture

- **Architecture Type:** Gemma 4
- **Network Architecture:** Gemma-4-E4B
- **Number of model parameters:** 8B (4B effective parameters)

## Model Design

The model was further post-trained from Gemma-4-E4B-it.

## Training Methodology

Reinforcement Learning

* The model underwent multi-environment reinforcement learning using GRPO (Group Relative Policy Optimization) across instruction following, multi-step tool use, multi-turn conversations, and structured output environments. It utilized an asynchronous RL architecture that decouples training from inference.
* Software used for reinforcement learning: [NeMo RL](https://github.com/NVIDIA-NeMo/RL), [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym)

Nemotron-3.5-Bolt-E4B-BF16 is a result of the above work.

## Input

- **Input Type(s):** Text
- **Input Format(s):** String
- **Input Parameters:** One-Dimensional (1D): Sequences
- **Other Properties Related to Input:** Maximum context length for this WCE endpoint: up to 64K tokens. Supported languages include English, Spanish, French, German, Italian, and Japanese.

## Output

- **Output Type(s):** Text
- **Output Format:** String
- **Output Parameters:** One-Dimensional (1D): Sequences
- **Other Properties Related to Output:** A text response, with an optional reasoning trace and tool calls, in OpenAI-compatible chat format.

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration

- **Runtime Engine(s):** PyTorch
- **Supported Hardware Microarchitecture Compatibility:** NVIDIA Ampere - A100; NVIDIA Blackwell; NVIDIA Hopper - H100-80GB
- **Supported Operating System(s):** Linux

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Model Version(s)

* GA (10/23/2026)

**Asynchronous Tool-Calling**

* Transmit asynchronous functions via the standard OpenAI tools structure.
* Retrieve assistant function executions directly from `message.tool_calls`.
* Restrict generation to a single tool invocation per assistant turn.
* Assign a persistent task identifier to each decoupled job execution.
* Provide subsequent execution outputs as a user role turn prefixed with something like `"TOOL RESULT:"`.
* Avoid submitting secondary tool turns for requests with an active pending response.
* Maintain tracked status sets for unresolved and finalized job identifiers.
* Synthesize the final response only after all background processes finish and zero calls remain outstanding.

Example:

Assistant tool-call

```json
{
"role": "assistant",
"tool_calls": [{
"id": "call_1",
"type": "function",
"function": {
"name": "build_report",
"arguments": "{\"_task_id\":\"task_1\",\"scope\":\"weekly\"}"
}
}]
}
```

Immediate acknowledgement with pending result

```json
{
"role": "tool",
"tool_call_id": "call_1",
"content": "{\"status\":\"pending\",\"task_id\":\"task_1\",\"function\":\"build_report\"}"
}
```

Later tool result completion result

```json
{
"role": "user",
"content": "ASYNC TOOL UPDATE: {\"status\":\"completed\",\"task_id\":\"task_1\",\"function\":\"build_report\",\"response\":\"Report is ready.\"}"
}
```

The model processes the finalized payload to resume generation.

## **Prompting & Usage Guidelines**

General guidelines for using Gemma-Nemotron in conversational and agentic applications.

**Prompt Structure & Content**

* Store persistent behavior constraints and operational guidelines in system prompts.
* Use explicit headers to organize roles, tasks, tool configs, and formatting safety rules.
* Keep the primary objective clear and concise.
* Write unambiguous, verifiable instructions and resolve conflicting guidance.
* Remove redundant guidance and repetitive few-shot examples.
* Use explicit constraints (e.g., `"limit responses to 1-2 sentences"`) instead of vague requests (e.g., `"be brief"`).
* Avoid synthetic or non-model outputs in `"assistant"` turns.
* Adhere strictly to standard `system/user/assistant/tool` turn sequences.

**Conveying Environment State in Stateful Applications**

* Prefix context blocks with explicit structural markers (e.g., `"# CURRENT STATE"`).
* Clearly specify what part of the context belongs to the model and what part refers to information for other entities like the user.
* When state updates end a message, restate the core goal alongside them.

**Instructing the Model**

* Define required behaviors with precise language and mandate necessary tool calls.
* Provide fallback protocols for requests exceeding available tool capabilities.
* Separate output formatting rules from task directives, and use the official chat template.

**Conversational Responses**

* Set `conversational_mode=True` for concise, low-formatting outputs suited for audio or spoken interaction.
* Set or leave the flag to `False` to retain standard generation style.

## Training, Testing, and Evaluation Datasets

# Training

**Data Modality:** Text
**Training Data Size:** More than 20 Trillion Tokens
**Dataset partition:** *Training [100%], testing [0%], validation [0%]*
**Time period for training data collection:** 2013 to December 2025
**Time period for testing data collection:** 2013 to December 2025
**Time period for validation data collection:** 2013 to December 2025
**Data Collection Method by dataset:** Hybrid: Automated, Manually-Collected, Synthetic
**Labeling Method by dataset:** Hybrid: Automated, Manually-Labeled, Synthetic

The post-training corpus for Nemotron-3.5-Bolt-E4B-BF16 consists of high-quality curated and synthetically-generated data. Primary languages used for post-training include English, French, German, Italian, Japanese, Spanish, and Chinese.

These datasets, such as FinePDFs, EssentialWeb, HotpotQA, SQuAD, and HelpSteer3, do not collectively or exhaustively represent all demographic groups (and proportionally therein). For instance, these datasets do not contain explicit mentions of demographic classes such as age, gender, or ethnicity in 64-99% of samples, depending on the source. In the subset where such terms are present, document-based datasets (FinePDFs and EssentialWeb) contain representational skews, such as references to "male" outnumbering those to "female", and mentions of "White" as the most frequent among ethnic identifiers (comprising 43-44% of ethnicity mentions). To mitigate these imbalances, we recommend considering evaluation techniques such as bias audits, fine-tuning with demographically balanced datasets, and mitigation strategies like counterfactual data augmentation to align with the desired model behavior. This evaluation used a 3,000-sample subset per dataset, identified as the optimal threshold for maximizing embedder accuracy.

During post-training, we generate synthetic data by distilling trajectories, solutions, and translations from strong teacher models and agent systems, often grounded in real tasks or documents and aggressively filtered for quality. For math, code, and science, we start from curated problem sets and use open source permissive models such as GPT-OSS-120B to produce step-by-step reasoning traces, candidate solutions, best-of-n selection traces, and verified CUDA kernels. For long-context and science, we build synthetic QA and reasoning data by retrieving passages from long documents, generating MCQ/OpenQA questions and answers, and paraphrasing them into multiple prompt/response formats to ensure diversity. Across all pipelines we stack automated verification—compilers, numerical checks, language identification—to ensure our data is high quality.

For all domains, we apply a unified data filtering pipeline to ensure that only high-quality, license-compliant, and verifiable samples are used for post-training. We first discard malformed examples using structural checks (e.g., missing tool definitions when tool calls are present). We then aggressively filter reasoning traces exhibiting pathological repetition, such as repeated n-grams within a sliding window or across the entire trajectory, which we found to be a strong indicator of malformed or low-quality reasoning. Finally, based on internal audits of synthetically generated datasets, we observed that some teacher models occasionally produce reasoning traces and final responses that implicitly align with specific political entities or promote nationalistic narratives. To mitigate this, we apply targeted keyword- and regex-based filters and remove all trajectories matching such behavior.

Alongside the model, we release our final pre-training and post-training data, as outlined in this section. For ease of analysis, there is a sample set that is ungated. For all remaining code, math and multilingual data, gating and approval is required, and the dataset is permissively licensed for model training purposes.

<details>
<summary>For Detailed Dataset Information: Click here!</summary>

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
| [Reddit Dataset](https://files.pushshift.io/reddit/) | Legacy Download |
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

## Private Non-publicly Accessible Datasets of Third Parties

| Dataset | Model(s) used |
|---------|---------------|
| Global Regulation | Unknown |
| TAUS Translation Memory | Unknown |
| Scale HLE | Unknown |
| HackerRank Coding | Unknown |
| RL data for Search | Gemini 3; GPT-5 |
| Mercor SWE-AgentsV1 | Undisclosed |

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

## NVIDIA-Sourced Synthetic Datasets (Post-Training)

| Dataset | Modality | Dataset Size | Seed Dataset | Model(s) used for generation |
| :---- | :---- | :---- | :---- | :---- |
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

## Language Distribution in Post-Training

For our post-training recipe, we focused on the following languages in addition to English: French, German, Italian, Japanese, Spanish, and Chinese. Those languages were represented in the form of multilingual reasoning and translation tasks.

</details>

## Testing Datasets:

**Data Collection Method by dataset** <br>
* Hybrid: Automated, Manually-Collected, Synthetic
**Labeling Method by dataset** <br>
* Hybrid: Automated, Manually-Labeled, Synthetic
**Properties:** This corpus comprises a mix of high-quality standard benchmarks and test suites for modern agentic AI. These benchmarks test model capabilities on tasks such as tool-calling and instruction following.

## Evaluation Datasets:

**Data Collection Method by dataset** <br>
* Hybrid: Automated, Manually-Collected, Synthetic
**Labeling Method by dataset** <br>
* Hybrid: Automated, Manually-Labeled, Synthetic
**Properties:** This corpus comprises a mix of high-quality standard benchmarks and test suites for modern agentic AI. These benchmarks test model capabilities on tasks such as tool-calling and instruction following.

## Inference

**Acceleration Engine:** vLLM with NVIDIA Dynamo (Preview API).

**Test Hardware:** Reported for the base model:

* NVIDIA Hopper
- 1-8x H100
- 1-8x H200
* NVIDIA Blackwell
- GB200
- GeForce RTX 5090

**Preview API Deployment Hardware:** NVIDIA L40S.

Recommended sampling settings are **Temperature 1.0** and **Top\_P 0.95** in both thinking enabled and disabled modes.

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.

We advise against circumvention of any provided safety guardrails contained in the Model without a substantially similar guardrail appropriate for your use case. For more details: Safety and Explainability Subcards.

For more detailed information on ethical considerations for this model, please see the Model Card++ [Bias](bias.md), [Explainability](explainability.md), [Safety & Security](safety.md), and [Privacy](privacy.md) Subcards.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Specifications

- **Context Length:** 65,536 tokens
- **Parameters:** 8,000,000,000
- **Input:** Text
- **Output:** Text

## Capabilities

- **Function Calling:** Supported
- **Structured Output:** Supported
- **Reasoning:** Supported

## Bias

| Field | Response |
| :---- | :---- |
| Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing: | None |
| Bias Metric (If Measured): | [BBQ Accuracy Scores in Ambiguous Contexts](https://github.com/nyu-mll/BBQ/) |
| Which characteristic (feature) show(s) the greatest difference in performance?: | The model shows high variance in the characteristics when it is used with a high temperature. |
| Measures taken to mitigate against unwanted bias: | Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF) employed to calibrate the model’s reasoning capabilities to maintain logical consistency and appropriate complexity when interacting with or interpreting data from diverse age demographics. |
| If using internal data, description of methods implemented in data acquisition or processing, if any, to address the prevalence of identifiable biases in the training, testing, and validation data: | The training datasets contain a large amount of synthetic data generated by LLMs. We manually curated prompts. |
| Tools used to assess statistical imbalances and highlight patterns that may introduce bias into AI models: | [BBQ](https://github.com/nyu-mll/BBQ/) |
| Tools used to assess statistical imbalances and highlight patterns that may introduce bias into AI models: | These datasets, such as web-scraped finance reasoning data derived from SEC EDGAR filings, science and math problem datasets, OpenResearcher/source-document datasets, Common Crawl, CC-News, Wikimedia, and long-context document datasets, do not collectively or exhaustively represent all demographic groups (and proportionally therein). For instance, these datasets do not contain explicit mentions of demographic classes such as age, gender, or ethnicity in approximately 97% to 99.9% of finance reasoning samples and in over 85% of samples across the broader assessed datasets. In the subset where such terms are present, these datasets contain notable representational skews. For example, ethnicity mentions are often dominated by Middle Eastern contexts (found in finance documents) or "White," "Two or more," and "Black or African American" as the most frequent ethnic identifiers, while references categorized as male-only significantly outnumber those categorized as female-only. Furthermore, gender is explicitly mentioned in approximately 12% of samples across the broader dataset assessment, yet in only 0.9% of finance-specific samples. Dataset-level results vary by source type, with long-context/source-document datasets containing higher explicit demographic mention rates compared to certain web-scraped sources. To mitigate these imbalances, we recommend considering evaluation techniques such as bias audits, fine-tuning with demographically balanced datasets, and mitigation strategies such as counterfactual data augmentation to align with the desired model behavior. This evaluation used a 3,000-sample subset per dataset, identified as the optimal threshold for maximizing embedder accuracy. |
| Unwanted Bias Testing: | Constrained to English-language inputs. Multi-lingual parity is not currently claimed or guaranteed. |

## Explainability

| Field | Response |
| :---- | :---- |
| Intended Task/Domain: | Text generation, reasoning, and chat |
| Model Type: | Text-to-text Gemma-4 |
| Intended Users: | Generative AI creators working with conversational AI models and image content. |
| Output: | Text |
| Tools used to evaluate datasets to identify synthetic data and ensure data authenticity. | We used a Gemma-3 4B-based filtering model fine-tuned on [Nemotron Content Safety Dataset v2](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) to ensure the quality of synthetic data. |
| Describe how the model works: | Generates text by predicting the next word or token based on the context provided in the input sequence using multiple self-attention layers. |
| List the groups (or group characteristics) for which this was tested to produce comparable outcomes: | Age, Disability Status, Gender Identity, Nationality, Physical Appearance, Ethnicity, Socioeconomic Status, Sexual Orientation, Religion |
| Technical Limitations & Mitigation: | This model performs particularly well in instruction following regimes, as such may be strongly influenced by untrusted inputs and should be paired with appropriate guardrails and data filtering to better align use-case behaviors when exposed to such data. |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics: | Accuracy, Throughput, and User-side throughput |
| Potential Known Risks: | The model was optimized explicitly for instruction following and as such may be influenced by untrusted inputs (prompt injection, indirect prompt injection, jailbreaking, web search, etc.) as a result of its instruction tuning that may degrade safety alignment and other training efforts. This model should be paired with additional guardrails and data filtering to limit exposure to instructions from malicious sources. Bypassing of safety alignment, system guardrails, and filters may allow harmful outcomes up to and including remote code execution in some agentic systems when effective security controls are not in place. The model was trained on data that contains toxic language and societal biases originally crawled from the internet. Therefore, the model may generate and amplify harmful, biased, or otherwise unsafe content reinforcing these biases and return toxic responses especially when prompted with toxic prompts. The model may also generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. The model may exhibit self-anthropomorphism (e.g., displaying human-like characteristics in dialogue, such as expressing preferences and emotions). In integrated system contexts, the model could potentially be exploited to access or disclose information beyond the model's intended permissions or scope of operation. |
| Licensing: | **GOVERNING HOSTING TERMS:** Use of the API is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1).<br><br>**ADDITIONAL INFORMATION:** [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0). |

## Privacy

| Field | Response |
| :---- | :---- |
| Generatable or reverse engineerable personal data\*? | No |
| Personal data used to create this model? | No |
| Was consent obtained for any personal data\* used? | Not Applicable |
| (For GPAI Models): A description of any methods implemented in data acquisition or processing, if any, to address the prevalence of personal data in the training data, where relevant and applicable. | We used only prompts that do not contain any personal data for synthetic data generation. |
| How often is dataset reviewed? | Before Release |
| Is a mechanism in place to honor data subject right of access or deletion of personal data? | Not Applicable |
| If personal data was collected for the development of the model, was it collected directly by NVIDIA? | Not Applicable |
| If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects? | Not Applicable |
| If personal data was collected for the development of this AI model, was it minimized to only what was required? | Not Applicable |
| Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model? | No |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | No, not possible with externally-sourced data. |
| Applicable Privacy Policy | [https://www.nvidia.com/en-us/about-nvidia/privacy-policy/](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) |

## Safety & Security

| Field | Response |
| :---- | :---- |
| Model Application Field(s): | Chat, Instruction Following, Chatbot Development, Code Generation, Reasoning, Customer Service |
| Describe the life critical impact (if present). | Not Applicable |
| Description of methods implemented in data acquisition or processing, if any, to address other types of potentially harmful data in the training, testing, and validation data: | We used a guard model for content safety to exclude potentially harmful data from training.  |
| Description of any methods implemented in data acquisition or processing, if any, to address illegal or harmful content in the training data, including, but not limited to, child sexual abuse material (CSAM) and non-consensual intimate imagery (NCII) | We used a Gemma-3 4B-based guard model trained on [Nemotron Content Safety Dataset v2](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) for content safety to exclude potentially illegal or harmful content from the training. |
| Use Case Restrictions: | **GOVERNING HOSTING TERMS:** Use of the API is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1).<br><br>**ADDITIONAL INFORMATION:** [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0). |
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to. |
| This AI model was developed based on our policies to ensure responsible data handling and risk mitigation. The datasets used for training have been scanned for harmful content and illegal content, consistent with our policies including scanning for Child Sexual Abuse Material (CSAM). Ongoing review and monitoring mechanisms are in place based on our policies and to maintain data integrity. | True. We use [Nemotron Content Safety Dataset V2](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) and an internal safety dataset specialized for minority sexuality for content safety evaluation to ensure the safety of this model. |

## Prototype

```python
import requests

invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
stream = False

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "text/event-stream" if stream else "application/json",
}

payload = {
"messages": [
{
"role": "user",
"content": ""
}
],
"model": "nvidia/nemotron-3.5-bolt-e4b"
}

response = requests.post(invoke_url, headers=headers, json=payload, stream=stream)
if stream:
for line in response.iter_lines():
if line:
print(line.decode("utf-8"))
else:
print(response.json())
```

```python
from langchain_nvidia_ai_endpoints import ChatNVIDIA

client = ChatNVIDIA(
model="nvidia/nemotron-3.5-bolt-e4b",
api_key="$NVIDIA_API_KEY",

)

invoke_options = {}

lc_messages = [
{
"role": "user",
"content": "",
},
]

response = client.invoke(lc_messages, **invoke_options)
if response.additional_kwargs and "reasoning_content" in response.additional_kwargs:
print(response.additional_kwargs["reasoning_content"])
print(response.content)
if response.tool_calls:
print(response.tool_calls)
```

```javascript
import axios from 'axios';

const invokeUrl = "https://integrate.api.nvidia.com/v1/chat/completions";
const stream = false;

const headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": stream ? "text/event-stream" : "application/json"
};

async function main() {
const payload = {"messages":[{"role":"user","content":""}],"model":"nvidia/nemotron-3.5-bolt-e4b"};

const response = await axios.post(invokeUrl, payload, {
headers: headers,
responseType: stream ? 'stream' : 'json'
});

if (stream) {
response.data.on('data', (chunk) => {
console.log(chunk.toString());
});
} else {
console.log(JSON.stringify(response.data));
}
}

main().catch(error => {
if (error.response) {
console.error(`HTTP ${error.response.status}`);
if (error.response.data?.on) {
error.response.data.on('data', (chunk) => console.error(chunk.toString()));
} else {
console.error(error.response.data);
}
} else {
console.error(error);
}
});
```

```bash
stream=false
if [ "$stream" = true ]; then
accept_header='Accept: text/event-stream'
else
accept_header='Accept: application/json'
fi

cat > payload.json <<JSON
{"messages":[{"role":"user","content":""}],"model":"nvidia/nemotron-3.5-bolt-e4b"}
JSON

curl https://integrate.api.nvidia.com/v1/chat/completions \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "Content-Type: application/json" \
-H "$accept_header" \
-d @payload.json
```