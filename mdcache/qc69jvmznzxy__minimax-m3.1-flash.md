---
title: "minimax-m3.1-flash"
publisher: "minimaxai"
type: "endpoint"
updated: "2026-10-20T21:53:35.696Z"
description: "MiniMax-M3.1-Flash is a native multimodal mixture-of-experts model for coding, agentic workflows, computer use, and cybersecurity."
canonical: "https://build.nvidia.com/minimaxai/minimax-m3.1-flash"
---

# MiniMax-M3.1-Flash

## Description
MiniMax-M3.1-Flash is a native multimodal mixture-of-experts (MoE) model developed by MiniMax for coding, agentic workflows, computer use, and cybersecurity, accepting text and image inputs and producing text output with a context window of up to 1M tokens. Building on MiniMax-M3, it has approximately 428B total parameters with 23B activated per token, and improves task performance and inference efficiency through MiniMax Sparse Attention (MSA) throughout the model, quantization-aware training (QAT) to NVFP4, and DSpark speculative decoding. The model supports five configurable reasoning effort levels (low, medium, high, xhigh, and max).

*This model is for research and development only.*

## Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [MiniMax-M3.1-Flash Model Card](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)

## License and Terms of Use:
**GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); and the use of this model is governed by the [NVIDIA Software and Model Evaluation License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-and-model-evaluation-license/). **ADDITIONAL INFORMATION:** The base model MiniMax M3.1 Flash is governed by the [MINIMAX COMMUNITY LICENSE](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash/blob/main/LICENSE).

## Deployment Geography:
Global

## Use Case:
**Use Case:** MiniMax-M3.1-Flash is designed for developers, researchers, and enterprises building agentic applications. Supported use cases include agentic coding and software engineering (repository generation, refactoring, and terminal tasks), computer use and desktop automation, tool-using workflow automation, cybersecurity tasks, long-context reasoning over up to 1M tokens, and multimodal understanding of images, charts, and documents.

## Release Date:
**Build.NVIDIA.com:** 10/22/2026 via [link](https://build.nvidia.com/minimaxai/minimax-m3.1-flash)  
**Huggingface:** 10/22/2026 via [link](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)

## Reference(s):
**References:**
- [MiniMax-M3.1-Flash on Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash)
- [MiniMax Sparse Attention (arXiv:2606.13392)](https://arxiv.org/abs/2606.13392)
- [SGLang Cookbook for MiniMax-M3.1](https://docs.sglang.io/cookbook/autoregressive/MiniMax/MiniMax-M3.1)
- [vLLM Recipe for MiniMax-M3.1-Flash](https://recipes.vllm.ai/MiniMaxAI/MiniMax-M3.1-Flash)

## Model Architecture:
**Architecture Type:** Transformer  
**Network Architecture:** Mixture-of-Experts  
**Total Parameters:** 428B  
**Active Parameters:** 23B  
**Base Model:** MiniMax-M3

### Input:
**Input Types:** Text, Image  
**Input Formats:** String, Red, Green, Blue (RGB)  
**Input Parameters:** One-Dimensional (1D), Two-Dimensional (2D)  
**Other Input Properties:** Supports a context window of up to 1,000,000 tokens; usable context length and throughput depend on GPU memory and serving configuration. Reasoning effort is set via `reasoning_effort` in the chat template (low, medium, high, xhigh, or max).  
**Input Context Length (ISL):** 1,000,000

### Output:
**Output Types:** Text  
**Output Format:** String  
**Output Parameters:** One-Dimensional (1D)  
**Other Output Properties:** Generates reasoning and final-answer text. Includes a DSpark speculative-decoding draft head for use with compatible serving implementations.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## Software Integration:
**Runtime Engines:**
vLLM <br>
SGLang <br>

**Supported Hardware Microarchitecture Compatibility:**
- **NVIDIA Blackwell:** B200, B300, GB200, GB300

**Preferred Operating Systems:** Linux

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## Model Version(s)
MiniMax-M3.1-Flash v1.0 (October 2026)

## Training, Testing, and Evaluation Datasets:

### Training Dataset
**Data Modality:** Undisclosed  
**Training Data Collection:** Undisclosed  
**Training Labeling:** Undisclosed  
**Training Properties:** Undisclosed

### Testing Dataset
**Testing Data Collection:** Undisclosed  
**Testing Labeling:** Undisclosed  
**Testing Properties:** Undisclosed

### Evaluation Dataset
**Evaluation Benchmark Score:** MiniMax-M3.1-Flash achieves strong results across CoWork, computer use, coding, cybersecurity, and general and multimodal benchmarks, including 76.2 on BankerToolBench, 73.7% on DeepSWE v1.1, 61.7 on OSWorld 2.0, 29.6 on Agents' Last Exam, and 82.2 on CyberGym. Results are for the official NVFP4 weights; third-party quantizations may differ.

<details>
<summary><strong>Detailed Benchmark Comparison Table</strong></summary>

| Benchmark | MiniMax-M3.1-Flash | DeepSeek V4.1 Flash-1017 | DeepSeek V4.1 Flash | Kimi K3 | GLM-5.3 | GPT-5.6 Sol | Opus 5 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Automation-Bench v1.0.6 | **62.8** | 60.5 | 54.8 | 46.7 | 48.8 | 45.8 | 50.3 |
| BankerToolBench | **76.2** | — | 73.7 | 69.1 | 74.5 | 74.6 | **76.2** |
| GDP.pdf AA | 20.8 | — | 12.8 | 22.0 | 11.2 | **27.2** | 21.6 |
| Terminal Bench 4.0 | 38.1 | 42.3 | 31.2 | 12.6 | 37.9 | 39.9 | **51.8** |
| LOCA-Bench 256K | **60.3** | — | — | 49.7 | 50.3 | 60.0 | 53.7 |
| Agents' Last Exam | 29.6 | — | — | 28.3 | — | 30.6 | **32.2** |
| OSWorld 2.0 | 61.7 | — | 54.3 | 58.3 | — | 65.7 | **70.6** |
| PostTrain Bench v1.1 | 39.3 | — | 30.5 | 36.6 | 37.5 | 36.2 | **40.4** |
| DeepSWE v1.1 | 73.7 | **77.0** | 74.2 | 67.5 | 66.9 | 73.0 | 74.0 |
| NL2Repo-Bench | 61.2 | 68.2 | 65.4 | 58.0 | 58.0 | 56.8 | **75.3** |
| SWE Refactor Bench | 23.0 | — | 11.8 | 19.5 | 10.4 | 28.5 | **31.0** |
| CyberGym | 82.2 | — | — | 80.0 | **84.5** | 83.6 | — |
| BabyVision (with tools) | 91.0 | 92.5 | 89.6 | 85.7 | — | 88.9 | **94.1** |
| HLE (without tools) | 43.4 | 42.6 | 39.2 | 43.5 | 42.3 | 49.5 | **55.6** |
| CharXiv RQ | 82.5 | — | 69.0 | 84.8 | — | **85.2** | 83.7 |

*Bold scores indicate the highest reported result in each row. A dash indicates an unavailable or inapplicable result, not zero. Results are for the official NVFP4 weights; third-party quantizations may differ.*

</details>

**Evaluation Data Collection:** Undisclosed  
**Evaluation Labeling:** Undisclosed  
**Evaluation Properties:** Evaluation Methodology Notes:
- **Automation-Bench v1.0.6:** 600 publicly released tasks.
- **BankerToolBench:** OpenCode 1.17.18; MiniMax-M2.7 judge.
- **GDP.pdf AA:** Taken directly from Artificial Analysis.
- **Terminal Bench 4.0:** Codex 0.149.1.
- **LOCA-Bench 256K:** Official implementation.
- **Agents' Last Exam:** Official Overall setting; full-set results from the official ALE leaderboard only. Blank = no official result (CLI-only excluded), not zero.
- **OSWorld 2.0:** 0808 Full release; highest reported per model at release, except DeepSeek V4.1 (in-house reproduction).
- **PostTrain Bench v1.1:** Claude Code 2.1.251, 512K context; otherwise official setup.
- **DeepSWE v1.1:** mini-SWE-agent 2.4.5, 512K context.
- **NL2Repo-Bench:** Claude Code 2.1.233, 512K context; reward hacking = 0; two inconsistent tasks corrected (scores use the corrected set).
- **SWE Refactor Bench:** Claude Code 2.1.220, 200K context; otherwise official setup.
- **CyberGym:** Claude Code 2.1.263, 1M context.
- **BabyVision (with tools):** Claude Code 2.1.285; min image side 1,500 px.
- **HLE (without tools):** Text-only subset (2,158 questions).
- **CharXiv RQ:** GPT-5.5 judge.

## Inference
**Acceleration Engine:** vLLM  
**Test Hardware:** GB200, GB300

## Additional Details

### What's New in M3.1-Flash
MiniMax-M3.1-Flash retains MiniMax-M3's core mixture-of-experts architecture, with three main changes:
- **Sparse attention throughout:** The first three full-attention layers are replaced with sparse attention.
- **QAT NVFP4:** Routed MoE experts move from MXFP8 to NVFP4 W4A4, excluding the shared expert. The sparse-attention indexer and main branch move from Q8KV8 to Q8KV4.
- **DSpark speculative decoding:** DSpark replaces the earlier EAGLE-like MTP approach. The release includes the draft head for use with compatible serving implementations.

### Recommended Inference Settings
- **Sampling:** `temperature=1.0`, `top_p=0.95`
- **Reasoning effort:** Set `reasoning_effort` in the chat template: `low`, `medium`, `high`, `xhigh`, or `max`.
- **Context window:** Up to 1M tokens. Usable context length and throughput depend on GPU memory and the serving configuration.

## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please make sure you have proper rights and permissions for all input image content; if image includes people, personal health information, or intellectual property, the image generated will not blur or maintain proportions of image subjects included.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/)

## Specifications

- **Context Length:** 262,144 tokens
- **Parameters:** 220,490,854,016
- **Input:** Text, Image, Video
- **Output:** Text

## Capabilities

- **Function Calling:** Supported
- **Structured Output:** Supported
- **Reasoning:** Supported

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
]
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
model="",
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
const payload = {"messages":[{"role":"user","content":""}]};

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
{"messages":[{"role":"user","content":""}]}
JSON

curl https://integrate.api.nvidia.com/v1/chat/completions \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "Content-Type: application/json" \
-H "$accept_header" \
-d @payload.json
```