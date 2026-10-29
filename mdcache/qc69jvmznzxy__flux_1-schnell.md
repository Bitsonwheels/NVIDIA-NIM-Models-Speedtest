---
title: "FLUX.1-schnell"
publisher: "black-forest-labs"
type: "endpoint"
updated: "2025-06-13T13:37:07.149Z"
description: "FLUX.1-schnell is a distilled image generation model, producing high quality images at fast speeds"
canonical: "https://build.nvidia.com/black-forest-labs/flux_1-schnell"
---

# Overview

## Description:   

FLUX.1-schnell is a 12 billion parameter rectified flow transformer capable of generating images from text descriptions at fast speeds. Trained using latent adversarial diffusion distillation, FLUX.1-schnell can generate high-quality images in only 1 to 4 steps.

This model is ready for commercial use.

## Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to:
* [black-forest-labs/FLUX.1-schnell Model Card](https://huggingface.co/black-forest-labs/FLUX.1-schnell)

### Terms of use  

GOVERNING TERMS: The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). The Flux.1 Schnell model is available at [https://huggingface.co/black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell). Use of the NVIDIA Cosmos-1.0 Guardrail is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). ADDITIONAL INFORMATION: [Llama 2 Community License Agreement](https://github.com/meta-llama/llama-models/blob/main/models/llama2/LICENSE).

### Deployment Geography:

Global

## Use Case:  

Creators and professionals can use this model to generate high-quality images from text prompts, simplifying visual communication.

### Release Date:

August 1, 2024

### References

* [Flux on Black Forest Labs](https://blackforestlabs.ai/)  
* [Flux blog post](https://blackforestlabs.ai/announcing-black-forest-labs/)

## Model Architecture: 
**Architecture Type**: Transformer and Convolutional Neural Network (CNN)  
**Network Architecture**: Diffusion Transformer  
LiheYoung/Depth-anything-large-hf leverages the DPT architecture with a DINOv2 backbone.  

## Input:  
**Input Type**: Text
**Input Parameters**: Text: 1D.
**Input Format**: Text: String.  
**Other Properties Related to Input**: Steps, Output Image Aspect Ratio, and Seed per the [API Reference Page](https://docs.api.nvidia.com/nim/reference/black-forest-labs-flux_1-schnell)

## Output:  
**Output Type**: Image   
**Output Parameters**: 2D  
**Output Format**: Red, Green, Blue (RGB)  
**Other Properties Related to Output**: Supported resolutions 1024x1024, 768x1344, 1344x768, 896x1152, 1152x896, 832x1216, 1216x832  

## Software Integration:
**Runtime Engines:**
* TensorRT

**Supported Hardware Platforms**:  
* NVIDIA Blackwell <br> 
* NVIDIA Hopper <br>   
* NVIDIA Lovelace <br>  

**Supported Operating Systems**: Linux, Windows Subsystem for Linux <br> 

## Model Version(s):  
* FLUX.1-schnell  

# Training, Testing, and Evaluation Datasets:

## Training Dataset:

* Data Collection Method by Dataset: Undisclosed
* Labeling Method by Dataset: Undisclosed

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Undisclosed

## Testing Dataset:

* Data Collection Method by Dataset: Undisclosed
* Labeling Method by Dataset: Undisclosed

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Undisclosed

## Evaluation Dataset:  

* Data Collection Method by Dataset: Undisclosed
* Labeling Method by Dataset: Undisclosed

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Undisclosed

## Inference:  
**Engine**: TensorRT   
**Test Hardware**: H100

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Prototype

```bash
invoke_url='https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-schnell'

authorization_header="Authorization: Bearer $NVIDIA_API_KEY"
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data='{
"prompt": "",
"width": 1024,
"height": 1024,
"seed": ,
"steps": 
}'

response=$(curl --silent -i -w "\n%{http_code}" --request POST \
--url "$invoke_url" \
--header "$authorization_header" \
--header "$accept_header" \
--header "$content_type_header" \
--data "$data"
)

http_code=$(echo "$response" | tail -n 1)

echo "$response" | awk '/{/,EOF-1'
```

```javascript
import fetch from "node-fetch";

const invokeUrl = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-schnell"

const headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

const payload = {
"prompt": "",
"width": 1024,
"height": 1024,
"seed": ,
"steps": 
}

let response = await fetch(invokeUrl, {
method: "post",
body: JSON.stringify(payload),
headers: { "Content-Type": "application/json", ...headers }
});

if (response.status != 200) {
let errBody = await (await response.blob()).text()
throw "invocation failed with status " + response.status + " " + errBody
}
let response_body = await response.json()
console.log(JSON.stringify(response_body))
```

```python
import requests

invoke_url = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-schnell"

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

payload = {
"prompt": "",
"width": 1024,
"height": 1024,
"seed": ,
"steps": 
}

response = requests.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)
```