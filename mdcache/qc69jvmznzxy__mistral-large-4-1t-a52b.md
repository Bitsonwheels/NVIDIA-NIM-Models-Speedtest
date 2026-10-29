---
title: "Mistral Large 4"
publisher: "mistralai"
type: "endpoint"
updated: "2026-10-29T14:10:58.920Z"
description: "Mistral Large 4 from Mistral AI, a 1T-total / 52B-active granular MoE for text and image input with reasoning, function calling and structured outputs, served in NVFP4 with DSpark speculative decoding."
canonical: "https://build.nvidia.com/mistralai/mistral-large-4-1t-a52b"
---

# Mistral Large 4

## Description
Mistral Large 4 is a multimodal Mixture-of-Experts model from Mistral AI that accepts text and images and generates text for instruction following, reasoning, coding, and agentic workflows. It has approximately 1000B total parameters and 49B active parameters per token, or 52B including embeddings and output layers.

*This model is ready for commercial or non-commercial use.*

## Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [Mistral Large 4 Model Card](https://docs.mistral.ai/models/mistral-large-4-0)

## License and Terms of Use:
**GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). To deploy and customize the model in your environment, please [contact Mistral](https://mistral.ai/contact/).

## Deployment Geography:
Global

## Use Case:
**Use Case:** Developers can use the model for instruction following, reasoning, coding, image and document analysis, structured outputs, and agentic workflows with tool calls, including applications in cybersecurity, finance, and law.

## Release Date:
**Build.NVIDIA.com:** 10/29/2026 via [link](https://build.nvidia.com/mistralai/mistral-large-4-1t-a52b)

## Reference(s):
**References:**

- [Mistral Large 4 vendor Model Card](https://docs.mistral.ai/models/mistral-large-4-0)
- [Introducing Mistral Large 4](https://mistral.ai/news/mistral-large-4/)
- [Vendor checkpoint repository](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)

## Model Architecture:
**Architecture Type:** Transformer  
**Network Architecture:** Mixture-of-Experts  
**Total Parameters:** ~1000B  
**Active Parameters:** 49B

### Input:
**Input Types:** Text, Image  
**Input Formats:** String, Red, Green, Blue (RGB)  
**Input Parameters:** One-Dimensional (1D), Two-Dimensional (2D)  
**Other Input Properties:** Text and images share a combined input/output context window of up to 1M tokens. Images use a Pixtral-style vision encoder that handles variable image sizes and aspect ratios. Maximum pixel dimensions, preprocessing steps, and images-per-request limits are not specified by the vendor.

### Output:
**Output Types:** Text  
**Output Format:** String  
**Output Parameters:** One-Dimensional (1D)  
**Other Output Properties:** Combined input and output context length is 1M tokens. The vendor's max_completion_tokens setting includes reasoning tokens and visible output tokens.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## Software Integration:
**Runtime Engines:**

- **Other:** vLLM, NVIDIA Dynamo

**Supported Hardware:**

- **NVIDIA Blackwell:** GB200, GB300

**Preferred Operating Systems:** Linux

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## Model Version(s)
Mistral Large 4; vendor checkpoint: `mistralai/Mistral-Large-4-1T-A52B`; vendor API model ID: `mistral-large-4`. Vendor release: 10/29/2026.

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
**Evaluation Properties:** The vendor reports results on the Artificial Analysis Intelligence Index v5 and Artificial Analysis Coding Agent Index. Underlying task sets, dataset collection and labeling methods, evaluation scaffolding, and run counts are not specified.  
**Evaluation Benchmark Score:** Artificial Analysis Intelligence Index v5: 26; Artificial Analysis Coding Agent Index: 48%.

## Inference
**Acceleration Engine:** vLLM  
**Test Hardware:** NVIDIA Blackwell (GB300)

## Additional Details
**Architecture and training:** The model uses 128 routed experts, with four active per token, and one shared expert. Mistral AI states it trained the model from scratch on 3,800 NVIDIA Grace Blackwell GPUs in its European datacenters.

**Capabilities:** The vendor describes support for 160+ languages, including all official European Union languages, system prompts, native function calling, JSON output, strict JSON schema enforcement, and visual grounding of images, charts, technical drawings, and documents.

**Vendor-recommended settings:** Reasoning effort can be low, medium, or high, with high as the default; the vendor recommends temperature=1.0 and top_p=0.95. These are vendor model recommendations; hosted endpoint options depend on the serving configuration.

**Speculative decoding:** The checkpoint includes an embedded DSpark draft head with three dense MLA draft layers in BF16 that propose three tokens. The vendor reports throughput gains of up to 1.4x to 1.8x over serving the target model alone, with gains dependent on hardware and workload.

**Vendor-reported evaluation:** On the Artificial Analysis Coding Agent Index, the vendor describes the 48% result as effectively tied with GLM-5.3 while using 47% fewer tokens per task on average. The draft does not supply additional evaluation methodology for this comparison.

**Vendor usage restriction:** The vendor states that operating a Model-as-a-Service business requires a separate commercial license with Mistral.

## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please make sure you have proper rights and permissions for all input image content; if image includes people, personal health information, or intellectual property, the image generated will not blur or maintain proportions of image subjects included.

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/)

## Specifications

- **Context Length:** 262,144 tokens
- **Parameters:** 1050B
- **Input:** Text, Image
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