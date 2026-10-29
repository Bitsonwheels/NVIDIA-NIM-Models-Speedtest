---
title: "stable-diffusion-3.5-large"
publisher: "stabilityai"
type: "endpoint"
updated: "2025-08-12T18:56:17.501Z"
description: "Stable Diffusion 3.5 is a popular text-to-image generation model"
canonical: "https://build.nvidia.com/stabilityai/stable-diffusion-3_5-large"
---

# Overview

## Description:
Stable Diffusion 3.5 is an 8B parameter base model that produces high-quality images, with Depth and Canny ControlNets offering controllability over image outputs. Choose this model when you want high quality, artistic style, and more fine-tuning flexibility.

This model is ready for non-commercial use. Contact Stability AI at https://stability.ai/enterprise for commercial use of Stable Diffusion 3.5 Large model.

## Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see links to:
* [stabilityai/stable-diffusion-3.5-large Model Card](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)
* [stabilityai/stable-diffusion-3.5-large-controlnet-canny Model Card](https://huggingface.co/stabilityai/stable-diffusion-3.5-large-controlnet-canny)
* [stabilityai/stable-diffusion-3.5-large-controlnet-depth Model Card](https://huggingface.co/stabilityai/stable-diffusion-3.5-large-controlnet-depth)
* [LiheYoung/Depth-anything-large-hf Model Card](https://huggingface.co/LiheYoung/depth-anything-large-hf)

### License/Terms of Use

GOVERNING TERMS: The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf), and use of the Cosmos model is governed by the [NVIDIA Community Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). Contact Stability AI at https://stability.ai/enterprise for commercial use of Stable Diffusion 3.5 Large model. ADDITIONAL INFORMATION: [Llama 2 Community Model License Agreement](https://github.com/meta-llama/llama-models/blob/main/models/llama2/LICENSE) and [Apache License, Version 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md).

### Deployment Geography:

Global

## Use Case:  

Creators and professionals can use this model to generate high-quality images from text prompts, simplifying visual communication.

### Release Date:

* Build.Nvidia.com August 11, 2025 via [https://build.nvidia.com/stabilityai/stable-diffusion-3_5-large](https://build.nvidia.com/stabilityai/stable-diffusion-3_5-large)  
* Huggingface October 22, 2024 via [https://huggingface.co/stabilityai/stable-diffusion-3.5-large](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)

### References

* [Stable Diffusion 3.5 blog post](https://stability.ai/news/introducing-stable-diffusion-3-5)

## Model Architecture: 
**Architecture Type**: Transformer and Convolutional Neural Network (CNN)  
**Network Architecture**: Diffusion Transformer  
LiheYoung/Depth-anything-large-hf leverages the DPT architecture with a DINOv2 backbone.  

## Input:  
**Input Type**: Text, Image (optional)  
**Input Parameters**: Text: One-Dimensional (1D); Image: Two-Dimensional (2D)
**Input Format**: Text: String. Image: Red, Green, Blue (RGB)   
**Other Properties Related to Input**: Steps, Classifier-Free Guidance Scale, Output Image Aspect Ratio, and Seed

## Output:  
**Output Type**: Image   
**Output Parameters**: Two-Dimensional (2D)
**Output Format**: Red, Green, Blue (RGB)  
**Other Properties Related to Output**: Supported resolutions 1024x1024, 768x1344, 1344x768, 1344x768, 1344x768, 1344x768, 1216x832

## Software Integration:
**Runtime Engines:**
* TensorRT

**Supported Hardware Platforms**:  
* NVIDIA Blackwell <br> 
* NVIDIA Hopper <br>   
* NVIDIA Lovelace <br>  

**Supported Operating Systems**: Linux, Windows Subsystem for Linux <br> 

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Model Versions:  
* Stable Diffusion 3.5 Large  
* Stable Diffusion 3.5 Large Controlnet - Canny    
* Stable Diffusion 3.5 Large Controlnet - Depth   
* LiheYoung/Depth-anything-large-hf

# Training, Testing, and Evaluation Datasets:

## Training Dataset:

* Data Collection Method by dataset: Undisclosed
* Labeling Method by dataset: Undisclosed

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Undisclosed

## Testing Dataset:

* Data Collection Method by dataset: Undisclosed
* Labeling Method by dataset: Undisclosed

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Undisclosed

## Evaluation Dataset:  

* Data Collection Method by dataset: Undisclosed
* Labeling Method by dataset: Undisclosed

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Undisclosed

## Inference:  
**Engine**: TensorRT   
**Test Hardware**: H100

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Prototype

```bash
invoke_url='https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-dev'

authorization_header="Authorization: Bearer $NVIDIA_API_KEY"
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data='{
"prompt": "",
"mode": "",
"image": "",
"cfg_scale": ,
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

const invokeUrl = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-dev"

const headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

const payload = {
"prompt": "",
"mode": "",
"image": "",
"cfg_scale": ,
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

invoke_url = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-dev"

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

payload = {
"prompt": "",
"mode": "",
"image": "",
"cfg_scale": ,
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