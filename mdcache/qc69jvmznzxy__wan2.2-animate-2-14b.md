---
title: "wan2.2-animate-2-14b"
publisher: "wan-ai"
type: "endpoint"
updated: "2026-08-19T15:49:22.813Z"
description: "Wan2.2-Animate-2 is a novel end-to-end character animation framework"
canonical: "https://build.nvidia.com/wan-ai/wan2.2-animate-2-14b"
---

# Wan2.2-Animate-2-14B Overview

## Description:  

Wan-Animate-2 is a novel end-to-end character animation framework that directly consumes driving videos in a redesigned Diffusion Transformer, which achieves high-fidelity motion generation and strong identity preservation by eliminating intermediate motion extractors.

Wan-Animate-2 was developed by Wan-AI team.

_This model is ready for commercial or non-commercial use._  

## Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model have been developed and built to a third-party’s requirements for this application and use case; see links to:  
* [Wan-AI/Wan2.2-Animate-2-14B](https://huggingface.co/Wan-AI/Wan2.2-Animate-2-14B-Diffusers)

### License/Terms of Use:

GOVERNING TERMS: The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); and use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). **Additional Information**: [Apache 2.0 license](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md).

**You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.**

### Deployment Geography:

Global

### Release Date:   

* HuggingFace: Wan-AI/Wan2.2-Animate-2-14B August 7, 2026 via https://huggingface.co/Wan-AI/Wan2.2-Animate-2-14B-Diffusers

## Model Architecture:   
**Architecture Type:** Transformer   
**Network Architecture:** Mixture of Experts (MoE)  
**Number of model parameters:** 14B (1.4*10^10)  

## Input:  
### Input Type(s):  
[Text, Image, Video]  

### Input Format(s):  
- Text: String.  
- Image: Common formats (e.g., png, jpg, jpeg).  
- Video: mp4.

### Input Parameters:
- Text: One-Dimensional (1D), sequence of tokens.  
- Image: Two-Dimensional (2D), spatial pixels, dynamic resolutions.
- Video: Three-dimensional (3D)

## Output:  
**Output Type(s):** Video
**Output Format:** Tensor 
**Output Parameters:** Three-Dimensional (3D)

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:
**Runtime Engine(s):**
* SGLang Diffusion

**Supported Hardware Microarchitecture Compatibility**:   
* NVIDIA Blackwell <br> 
* NVIDIA Hopper <br>   
* NVIDIA Lovelace <br>  

**Supported Operating System(s):** 
* Linux  
* Windows Subsystem for Linux 

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment. 

## Model Version(s):  

* Wan2.2-Animate-2-14B

## Training, Testing, and Evaluation Datasets:  

## Training Dataset:

**Data Modality:**
* Text  
* Image  
* Video  
* Audio

**Image Training Data Size:** Undisclosed  
**Text Training Data Size:** Undisclosed  
**Video Training Data Size:** Undisclosed   
**Data Collection Method by dataset:** Undisclosed  
**Labeling Method by dataset:** Undisclosed  
**Properties:** Undisclosed  

### Testing Dataset:

**Data Collection Method by dataset:** Undisclosed  
**Labeling Method by dataset:** Undisclosed  
**Properties:** Undisclosed  

### Evaluation Dataset:
**Benchmark Score:** Undisclosed

**Data Collection Method by dataset:** Undisclosed  
**Labeling Method by dataset:** Undisclosed  
**Properties:** Undisclosed  

## Key Considerations:

This model can generate synthetic videos and may produce content that is inaccurate, offensive, or otherwise inappropriate. Users should implement robust safety guardrails — including content filtering, abuse monitoring, and access controls— to reduce the risk of harmful outputs. Users are responsible for ensuring that their use of the model complies with all applicable laws and regulations, and for regularly reviewing and updating their guardrails as risks evolve.

For more information about the implementation of Cosmos pre and post guardrails to improve model safety, please see the [Cosmos-1.0 Guardrail Model](https://huggingface.co/nvidia/Cosmos-1.0-Guardrail).

## Inference:  
**Acceleration Engine**: SGLang Diffusion  
**Test Hardware**: 

H100 SXM<br>
H200 SXM<br>
B200 SXM<br>
H20<br>
GH200<br>
GB200 NVL<br>
RTX 6000 Blackwell SV<br>
RTX 6000 Blackwell WS

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal developer team to ensure these software components meet requirements for the relevant industry and use case and address unforeseen product misuse.   

Please make sure you have proper rights and permissions for all input image and video content; if image or video includes people, personal health information, or intellectual property, the image or video generated will not blur or maintain proportions of image subjects included.

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail).

# Get Help

## Getting started with the NIM
Deploying and integrating the NIM is straightforward thanks to our industry standard APIs. Visit the [Visual Generative AI NIM page](https://docs.nvidia.com/nim/visual-genai/latest/overview.html) for release documentation, deployment guides and more.

## NVIDIA Developer Community Forum
Get access to community knowledge base articles and support cases (https://forums.developer.nvidia.com/)

## Capabilities

- **Function Calling:** Not supported

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