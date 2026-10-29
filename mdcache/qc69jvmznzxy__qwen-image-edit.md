---
title: "qwen-image-edit"
publisher: "qwen"
type: "endpoint"
updated: "2026-05-01T19:55:32.704Z"
description: "Qwen-Image-Edit is an image editing model with multilingual text editing and strong subject consistency."
canonical: "https://build.nvidia.com/qwen/qwen-image-edit"
---

# Overview

## Description:   
Qwen-Image-Edit is the image editing version of Qwen-Image. Built upon the 20B Qwen-Image model, Qwen-Image-Edit successfully extends Qwen-Image’s unique text rendering capabilities to image editing tasks, enabling precise text editing. Furthermore, Qwen-Image-Edit simultaneously feeds the input image into Qwen2.5-VL (for visual semantic control) and the VAE Encoder (for visual appearance control), achieving capabilities in both semantic and appearance editing.  

Qwen-Image-Edit was developed by the Qwen Team.   
This model is ready for commercial/non-commercial use.

## Third-Party Community Consideration:
These models are not owned or developed by NVIDIA. These models have been developed and built to a third-party’s requirements for this application and use case; see links to:  
* [Qwen/Qwen-Image-Edit Model Card](https://huggingface.co/Qwen/Qwen-Image-Edit)
* [Qwen/Qwen-Image-Edit-2509 Model Card](https://huggingface.co/Qwen/Qwen-Image-Edit-2509)
* [Qwen/Qwen-Image-Edit-2511 Model Card](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)

### License/Terms of Use
GOVERNING TERMS: The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); and use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). **Additional Information**: [Apache 2.0 license](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md).

### Deployment Geography:

Global

### Use Case:  
- **Content Creation**: For artists, designers, and creators generating text-rich images (e.g., posters, UI mockups, and artistic works) and performing precise image editing.
- **Educational & Professional**: For educators creating visual teaching materials (for example, mathematical diagrams with text) and professionals synthesizing documents and images (e.g., technical slides and reports).
- **Research**: For computer vision and generative AI researchers studying text-image alignment, diffusion-based generation, and multimodal integration.

### Release Date:    
* HuggingFace/Modelscope: Qwen-Image-Edit version August 18, via https://huggingface.co/Qwen/Qwen-Image-Edit and https://modelscope.cn/models/Qwen/Qwen-Image-Edit   
* HuggingFace/Modelscope: Qwen-Image-Edit-2509 version September 22, via https://huggingface.co/Qwen/Qwen-Image-Edit-2509 and https://modelscope.cn/models/Qwen/Qwen-Image-Edit-2509   
* HuggingFace/Modelscope: Qwen-Image-Edit-2511 version December 23, via https://huggingface.co/Qwen/Qwen-Image-Edit-2511 and https://modelscope.cn/models/Qwen/Qwen-Image-Edit-2511    
* build.nvidia.com April 30, 2026 via [https://build.nvidia.com/qwen/qwen-image-edit](https://build.nvidia.com/qwen/qwen-image-edit)    

## References

* [Technical Report](https://arxiv.org/abs/2508.02324)  

## Model Architecture:   
### Architecture Type:  
Qwen-Image adopts a **three-core module architecture**:  
1. **Multimodal Large Language Model (MLLM)**: Qwen2.5-VL (frozen) for text/image feature extraction and semantic alignment.  
2. **Variational AutoEncoder (VAE)**: Single-encoder (frozen, adapted from Wan2.1-VAE) + dual-decoder (image-specific decoder fine-tuned) for image tokenization and reconstruction.  
3. **Multimodal Diffusion Transformer (MMDiT)**: Backbone diffusion model with novel **Multimodal Scalable RoPE (MSRoPE)** for joint text-image positional encoding.  

### Network Architecture:  
- **Key Components**:  
- MSRoPE: Balances image resolution scaling and text positional encoding by mapping text to the diagonal of image grids.  
- Dual-Encoding Mechanism: Combines semantic features (from Qwen2.5-VL) and reconstructive features (from VAE) for editing consistency.  
- Multi-Task Training: Integrates T2I (text-to-image), TI2I (text-image-to-image), and I2I (image-to-image reconstruction) tasks.  

### Number of Model Parameters:  
| Component        | Parameter Count |  
|------------------|-----------------|  
| Qwen2.5-VL (VLM) | 7B              |  
| VAE (Enc/Dec)    | 54M / 73M       |  
| MMDiT            | 20B             |  
| **Total**        | ~27.1B          |  

## Input:  
### Input Type(s):  
[Text, Image]  

### Input Format(s):  
- Text: String (supports English and Chinese).  
- Image: Common formats (e.g., png, jpg, jpeg) for editing tasks.  

### Input Parameters:  
- Text: One-Dimensional (1D), sequence of tokens.  
- Image: Two-Dimensional (2D), spatial pixels, dynamic resolutions.  
- Context: Native support for text prompts (unlimited length in practice, optimized for paragraph-level text); image inputs support dynamic resolutions (256p → 1328p during training).  

### Other Properties Related to Input:  
- Pre-processing:  
- Text: Tokenization via Qwen2.5-VL’s tokenizer; system prompts for task alignment (e.g., T2I: detail-rich description guidance; TI2I: image feature + text instruction fusion).  
- Image: Resized to target resolution (256p/640p/1328p) with aspect ratio preservation; encoded via VAE for latent representation.  
- Context Length: No strict token limit for text prompts; image latent length varies by resolution (e.g., 8×8 patch size for VAE).  

## Output:  
### Output Type(s):  
[Image]  

### Output Format:  
Raster image formats (e.g., png, jpg, jpeg) via VAE decoding.  

### Output Parameters:  
Two-Dimensional (2D), with configurable resolution (supports aspect ratios: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3).  

### Other Properties Related to Output:  
- Resolution: Up to 1328×1328 (default) for high-fidelity generation; supports ultra-high resolution via multi-scale training.  
- Text Fidelity: Preserves font, layout, and language coherence for text-in-image outputs (e.g., Chinese characters, English paragraphs).  

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:
**Runtime Engines:**
* SGlang Diffusion

**Supported Hardware Microarchitecture Compatibility**:   
* NVIDIA Blackwell <br> 
* NVIDIA Hopper <br>   
* NVIDIA Lovelace <br>  

**Supported Operating Systems**:       
* Linux   
* Windows Subsystem for Linux 

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment. 

## Model Version(s):  
* Qwen-Image-Edit    
* Qwen-Image-Edit-2509   
* Qwen-Image-Edit-2511   

## Training, Testing, and Evaluation Datasets:  
### Dataset Overview:  
- **Total Size**: Undisclosed  
- **Total Number of Datasets**: 3  

### Training Dataset:  
- **Link**: Undisclosed  
- **Data Modality**: [Image, Text]  
- **Image Training Data Size**: Undisclosed   
- **Text Training Data Size**: Undisclosed
- **Data Collection Method by dataset**:  [Hybrid: Automated, Synthetic]  
- **Labeling Method by dataset**: [Hybrid: Automatic/Sensors, Human] 
- **Properties**:  
- Quantity: Undisclosed.  
- Descriptions: Datasets used for training included images of nature (55%, e.g., landscapes, objects), Design (27%, e.g., posters, UI), People (13%, e.g., portraits), and Synthetic Data (5%, text rendering-focused).
- Sensors: Undisclosed.  

### Testing Dataset:  
- **Link**: Undisclosed  
- **Data Collection Method by dataset**: Undisclosed  
- **Labeling Method by dataset**: Undisclosed  
- **Properties**: Undisclosed  

### Evaluation Dataset:  
- **Link**: Undisclosed
- **Data Collection Method by dataset**: [Automated]  
- **Labeling Method by dataset**: [Hybrid: Automated, Human]   
- **Properties**: Undisclosed.  

## Key Considerations:

This model can generate synthetic images and may produce content that is inaccurate, offensive, or otherwise inappropriate. Users should implement robust safety guardrails — including content filtering, abuse monitoring, and access controls— to reduce the risk of harmful outputs. Users are responsible for ensuring that their use of the model complies with all applicable laws and regulations, and for regularly reviewing and updating their guardrails as risks evolve.

For more information about the implementation of Cosmos pre and post guardrails to improve model safety, please see the [Cosmos-1.0 Guardrail Model](https://huggingface.co/nvidia/Cosmos-1.0-Guardrail).

## Inference:  
**Engine**: SGLang Diffusion   
**Test Hardware**: H100

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal developer team to ensure these software components meet requirements for the relevant industry and use case and address unforeseen product misuse.   

Please make sure you have proper rights and permissions for all input image and video content; if image or video includes people, personal health information, or intellectual property, the image or video generated will not blur or maintain proportions of image subjects included.

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

# Get Help

## Getting started with the NIM
Deploying and integrating the NIM is straightforward thanks to our industry standard APIs. Visit the [Visual Generative AI NIM page](https://docs.nvidia.com/nim/visual-genai/latest/overview.html) for release documentation, deployment guides and more.

## Enterprise Support
Get access to knowledge base articles and support cases or [submit a ticket](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Specifications

- **Parameters:** 20,430,401,088

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