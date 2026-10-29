---
title: "nemotron-parse"
publisher: "nvidia"
type: "endpoint"
updated: "2025-10-28T18:51:38.495Z"
description: "Cutting-edge vision-language model exceling in retrieving text and metadata from images."
canonical: "https://build.nvidia.com/nvidia/nemotron-parse"
---

# nemotron-parse Overview

nemotron-parse is a general purpose text-extraction model, specifically designed to handle documents. Given an image, nemotron-parse is able to extract formatted-text, with bounding-boxes and the corresponding semantic class. This has downstream benefits for several tasks such as increasing the availability of training-data for Large Language Models (LLMs), improving the accuracy of retriever systems, and enhancing document understanding pipelines.

This model is ready for commercial use.

## License 
GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Community Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/).Use of the tokenizer included in this model is governed by the [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/).

## Deployment Geography:
Global

## Use Case:
nemotron-parse will be capable of comprehensive text understanding and document structure understanding. It will be used in retriever and curator solutions. Its text extraction datasets and capabilities will help with LLM and VLM training, as well as improve run-time inference accuracy of VLMs.
The nemotron-parse model will perform text extraction from PDF and PPT documents. The nemotron-parse can classify the objects (title, section, caption, index, footnote, lists, tables, bibliography, image) in a given document, and provide bounding boxes with coordinates. 

## Release Date:
October 28, 2025 

## References 
* https://huggingface.co/docs/transformers/en/model_doc/mbart

## Model Architecture 

### Architecture Type : 
Transformer-based vision-encoder-decoder model

### Network Architecture 
* Vision Encoder: ViT-H model (https://huggingface.co/nvidia/C-RADIO)<br>
* Adapter Layer: 1D convolutions & norms to compress dimensionality and sequence length of the latent space (1280 tokens to 320 tokens)<br>
* Decoder: mBart [1] 10 blocks<br>
* Tokenizer: Use of the tokenizer included in this model is governed by the [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/)<br>
* Number of Parameters: <1B <br>

## Computational Load (For NVIDIA Models Only) 
**Cumulative Compute:** 1.4e+21 <br>
**Estimated Energy and Emissions for Model Training:** 
Energy Consumption: 6200 kWh <br>
Carbon Emissions: 2.55<br>

### Input 
* Input Type: Image, Text<br>
* Input Type(s): Red, Green, Blue (RGB) + Prompt (String)
* Input Parameters: 2D, 1D
- Other Properties Related to Input:
- Max Input Resolution (Width, Height): 1648, 2048
- Min Input Resolution (Width, Height): 1024, 1280
- Channel Count: 3

### Output 
* Output Type: Text<br>
* Output Format: String
* Output Parameters: 1D
- Other Properties Related to Output:
- nemotron-parse output format is a string which encodes text content (formatted or not) as well as bounding boxes and class attributes.<br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.<br>

## Software Integration:

Runtime Engine(s): TensorRT-LLM

Supported Hardware Microarchitecture Compatibility: <br>
NVIDIA Hopper/NVIDIA Ampere/NVIDIA Turing<br>

Supported Operating System(s): Linux<br>

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.<br>

## Model Version:

nemotron-parse: As part of this first release, we share the set of weights named overjoyed-adder.

## Training, Testing, and Evaluation Datasets:

### Training Dataset 

nemotron-parse is first pre-trained on our internal datasets: human, synthetic and automated.
Data Modality:
*Text
*Image<br>
Data Collection Method by Dataset: Hybrid: Human, Synthetic, Automated
Labeling Method by Dataset: Hybrid: Human, Synthetic, Automated

### Testing and Evaluation Dataset:

nemotron-parse is evaluated on multiple datasets for robustness, including public and internal dataset.
Data Collection Method by Dataset: Hybrid: Human, Synthetic, Automated
Labeling Method by Dataset: Hybrid: Human, Synthetic, Automated

## Inference 

Runtime Engine(s): TensorRT-LLM

Test Hardware: NVIDIA H100

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

**You are responsible for ensuring that your use of NVIDIA AI Models complies with all applicable laws.**

## Capabilities

- **Function Calling:** Supported
- **Structured Output:** Not supported
- **Reasoning:** Supported

## Bias

## Bias
| Field | Response |
| :---- | :---- |
| Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing: | None |
| Measures taken to mitigate against unwanted bias: | Not applicable |
| Bias Metric (If Measured): | [None |

## Explainability

## Explainability

| Field | Response |
| :---- | :---- |
| Intended Task/Domain: | image to text |
| Model Type: | Transformer-based vision-encoder-decoder model|
| Intended Users: | Generative AI creators working with conversational AI models and image content. |
| Output: | Text |
| Describe how the model works: | Generates text by predicting the next word or token based on the context provided in the input sequence using multiple self-attention layers. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Not Applicable |
| Technical Limitations & Mitigation: | The model demonstrates weakness to alignment-breaking attacks. Users are advised to deploy language model guardrails alongside this model to prevent potentially harmful outputs. The Model may generate answers that are inaccurate, omit key information, or include irrelevant or redundant text. |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics: | Accuracy, Throughput, and User-side throughput |
| Potential Known Risks: | The model was optimized explicitly for instruction following and as such is more susceptible to prompt injection and jailbreaking in various forms as a result of its instruction tuning. This means that the model should be paired with additional rails or system filtering to limit exposure to instructions from malicious sources  \-- either directly or indirectly by retrieval (e.g. via visiting a website)  \-- as they may yield outputs that can lead to harmful, system-level outcomes up to and including remote code execution in agentic systems when effective security controls including guardrails are not in place. The model was trained on data that contains toxic language and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. |
| Licensing: | GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Community Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). Use of the tokenizer included in this model is governed by the [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/).|

## Privacy

Field | Response |
| :---- | :---- |
| Generatable or reverse engineerable personal data? | No |
| Personal data used to create this model? | No |
| Was consent obtained for any personal data used? | Not Applicable |
| How often is the dataset reviewed? | Before Release |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | No, not possible with externally-sourced data. |
| Applicable Privacy Policy | [NVIDIA Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) |

## Safety & Security

| Field | Response |
| :---- | :---- |
| Model Application Field(s): | Chat, Instruction Following, Chatbot Development, Code Generation, Reasoning, Customer Service |
| Describe the life critical impact (if present). | Not Applicable |
| Use Case Restrictions: | GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Community Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). Use of the tokenizer included in this model is governed by the [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/).|
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to. |

**You are responsible for ensuring that your use of NVIDIA AI Models complies with all applicable laws.**

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
temperature=,
top_p=,
max_completion_tokens=,
)

lc_messages = [
{
"role": "user",
"content": "",
},
]

response = client.invoke(lc_messages)
if response.additional_kwargs and "reasoning_content" in response.additional_kwargs:
print(response.additional_kwargs["reasoning_content"])
print(response.content)
```

```javascript
import axios from 'axios';

const invokeUrl = "https://integrate.api.nvidia.com/v1/chat/completions";
const stream = ;

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
stream=
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