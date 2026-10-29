---
title: "Step 5 Preview"
publisher: "stepfun-ai"
type: "endpoint"
updated: "2026-10-15T01:44:30.728Z"
description: "Preview of StepFun's Step 5: ~600B-total / 27B-active multimodal MoE (text and image in, text out) with 1M context, reasoning and tool calling, served in NVFP4."
canonical: "https://build.nvidia.com/stepfun-ai/step-5-preview"
---

# Step 5 Preview

## Description
Step 5 Preview is a vision-language model developed by StepFun for agentic work that processes text and images to generate text. It supports software engineering, long-horizon tool use, and professional knowledge work, with a focus on finance.

*This model is ready for commercial or non-commercial use.*

## Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [Step 5 Preview Model Card](https://huggingface.co/stepfun-ai/Step-5-Preview/).

## License and Terms of Use:
**GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); and the use of this model is governed by the [NVIDIA Open Model Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-agreement/).

**ADDITIONAL INFORMATION:** The base model Step 5 Preview is governed by the [StepFun Model License 1.0](https://huggingface.co/stepfun-ai/Step-5-Preview/blob/main/LICENSE.txt).

## Deployment Geography:
Global

## Use Case:
**Use Case:** Intended for developers building applications for repository-level software engineering, frontend and visual development, programming for devices, long-horizon agentic execution, professional research and reporting, and financial analysis.

## Release Date:
**Build.NVIDIA.com:** 10/14/2026 via [link](https://build.nvidia.com/stepfun-ai/step-5-preview)  
**Huggingface:** 10/14/2026 via [link](https://huggingface.co/stepfun-ai/Step-5-Preview/)

## Reference(s):
**References:**

- [Step 5 Preview Model Page](https://huggingface.co/stepfun-ai/Step-5-Preview/)
- [Step 5 Preview BF16 Model Page](https://huggingface.co/stepfun-ai/Step-5-Preview-BF16)
- [Step 5 Preview on OpenRouter](https://openrouter.ai/stepfun/step-5-preview)

- [StepFun Model Overview](https://www.stepfun.com/step-5-preview)
- [Step 5 Preview Documentation](https://platform.stepfun.ai/docs/en/guides/models/step-5-preview)
- [StepFun API Platform](https://platform.stepfun.ai/)
- [Artificial Analysis](https://artificialanalysis.ai/)
- [SWE-agent](https://github.com/SWE-agent/SWE-agent)

## Model Architecture:
**Architecture Type:** Transformer  
**Network Architecture:** Mixture-of-Experts  
**Total Parameters:** 600B  
**Active Parameters:** 27B  
**Vocabulary Size:** 128,896

### Input:
**Input Types:** Text, Image  
**Input Formats:** String, Red, Green, Blue (RGB)  
**Input Parameters:** One-Dimensional (1D), Two-Dimensional (2D)  
**Other Input Properties:** The vision encoder uses 728 × 728 image inputs with a patch size of 14 and a vision projection ratio of 2.

### Output:
**Output Types:** Text  
**Output Format:** String  
**Output Parameters:** One-Dimensional (1D)  
**Other Output Properties:** Context window up to 1M tokens; maximum output up to 1M tokens, as specified by the model builder. Actual usable context length and concurrency depend on the checkpoint, inference framework, and KV cache allocation.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## Software Integration:
**Runtime Engines:**

- **vLLM**
- **SGLang**
- **Transformers**

**Supported Hardware Microarchitecture Compatibility:**

- **NVIDIA Blackwell:** GB300
- **NVIDIA Hopper:** H200

**Supported Operating System(s):** Linux

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## Model Version(s)
Step 5 Preview (BF16 and FP8 variants)

## Training, Testing, and Evaluation Datasets:

### Training Dataset
**Data Modality:** Text, Image  
**Image Training Data Size:** Undisclosed  
**Text Training Data Size:** Undisclosed  
**Training Data Collection:** Undisclosed  
**Training Labeling:** Undisclosed  
**Training Properties:** Undisclosed

### Testing Dataset
**Testing Data Collection:** Undisclosed  
**Testing Labeling:** Undisclosed  
**Testing Properties:** Undisclosed

### Evaluation Dataset
**Evaluation Data Collection:** Undisclosed  
**Evaluation Labeling:** Undisclosed  
**Evaluation Properties:** The model builder reports results across coding, agentic tasks, professional knowledge work, and finance. Reported Step 5 Preview results use the High reasoning setting. GDPval-AA v2.1 scores are based on Artificial Analysis results as of September 20, 2026. Benchmark testing conditions: DeepSWE v1.1 uses the SWE-agent harness with temperature=1.0 and top_p=0.95.

[Model builder benchmark results](https://cdn-uploads.huggingface.co/production/uploads/65dc9de42a6348b052a3286e/mfY2eltwq9TlXWlK6lx7K.png)

## Inference
**Acceleration Engine:** Other (Dynamo 1.6.0 with the partner vLLM backend; NVFP4 experts via Marlin or CUTLASS)  
**Test Hardware:** NVIDIA Blackwell (GB300), 4 GPUs

## Additional Details
Recommended inference settings from the model builder: temperature=1.0, top_p=0.95, top_k=0.

The model builder provides FP8 deployment examples on one eight-GPU H200 node and BF16 examples on two eight-GPU H200 nodes. These examples describe upstream deployment configurations. The full BF16 standalone file-shard conversion and generation workflow has not yet been validated end to end; the reference implementation has validated checkpoint names and shapes, BF16 small-model conversion, loading and generation, and full-model streaming-weight inference.

## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please make sure you have proper rights and permissions for all input image content; if image includes people, personal health information, or intellectual property, the image generated will not blur or maintain proportions of image subjects included.

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/)

## Specifications

- **Context Length:** 1,048,576 tokens
- **Parameters:** 600B
- **Input:** Text, Image
- **Output:** Text

## Capabilities

- **Function Calling:** Supported
- **Structured Output:** Not supported
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