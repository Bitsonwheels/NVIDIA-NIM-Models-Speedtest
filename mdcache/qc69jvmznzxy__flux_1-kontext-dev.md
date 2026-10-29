---
title: "FLUX.1-Kontext-dev"
publisher: "black-forest-labs"
type: "endpoint"
updated: "2025-08-12T18:43:11.036Z"
description: "FLUX.1 Kontext is a multimodal model that enables in-context image generation and editing."
canonical: "https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev"
---

# Overview

## Description:   
FLUX.1 Kontext is a suite of generative models for in-context image generation and editing, enabling users to prompt with text and modify with targeted changes. This allows for inpainting, character and object consistency, and style transfer - all without a complex workflow.

This model is ready for non-commercial use. Contact sales@blackforestlabs.ai for commercial terms.

## Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to:
* [black-forest-labs/FLUX.1-Kontext-dev Model Card](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev)

### License/Terms of Use

GOVERNING TERMS: The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Contact sales@blackforestlabs.ai for commercial terms to use the Flux.1-Kontext-dev model. ADDITIONAL INFORMATION: [Apache 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md), [NVIDIA Community Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/) and [Llama 2 Community Model License Agreement](https://github.com/meta-llama/llama-models/blob/main/models/llama2/LICENSE).

### Deployment Geography:

Global

## Use Case:  

Creators and professionals can use this model to generate high-quality images from text prompts, simplifying visual communication.

### Release Date:

* Build.Nvidia.com August 11, 2025 via [https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev](https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev)  
* Huggingface May 29, 2025 via [https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev)  

### References

* [Flux.1-Kontext-dev blog post](https://bfl.ai/announcements/flux-1-kontext/)

## Model Architecture: 
**Architecture Type**: Transformer and Convolutional Neural Network (CNN)  
**Network Architecture**: Diffusion Transformer  
LiheYoung/Depth-anything-large-hf leverages the DPT architecture with a DINOv2 backbone.  

## Input:  
**Input Type**: Text, Image  
**Input Parameters**: Text: One-Dimensional (1D); Image: Two-Dimensional (2D)
**Input Format**: Text: String. Image: Red, Green, Blue (RGB) 
**Other Properties Related to Input**: Steps, Classifier-Free Guidance Scale, Output Image Aspect Ratio, and Seed per the [API Reference Page](https://docs.api.nvidia.com/nim/reference/black-forest-labs-flux_1-kontext-dev)

## Output:  
**Output Type**: Image   
**Output Parameters**: Two-Dimensional (2D) 
**Output Format**: Red, Green, Blue (RGB)  
**Other Properties Related to Output**: Supported resolutions 672x1568, 688x1504, 720x1456, 752x1392, 800x1328, 832x1248, 880x1184, 944x1104, 1024x1024, 1104x944, 1184x880, 1248x832, 1328x800, 1392x752, 1456x720, 1504x688, 1568x672  

## Software Integration:
**Runtime Engines:**
* TensorRT

**Supported Hardware Platforms**:  
* NVIDIA Blackwell <br> 
* NVIDIA Hopper <br>   
* NVIDIA Lovelace <br>  

**Supported Operating Systems**: Linux, Windows Subsystem for Linux <br> 

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Model Version(s):  
* FLUX.1-Kontext-dev  

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

Pre-training mitigation. We filtered pre-training data for multiple categories of “not safe for work” (NSFW) content to help prevent a user generating unlawful content in response to text prompts or uploaded images.
Post-training mitigation. We have partnered with the Internet Watch Foundation, an independent nonprofit organization dedicated to preventing online abuse, to filter known child sexual abuse material (CSAM) from post-training data. Subsequently, we undertook multiple rounds of targeted fine-tuning to provide additional mitigation against potential abuse. By inhibiting certain behaviors and concepts in the trained model, these techniques can help to prevent a user generating synthetic CSAM or nonconsensual intimate imagery (NCII) from a text prompt, or transforming an uploaded image into synthetic CSAM or NCII.
Pre-release evaluation. Throughout this process, we conducted multiple internal and external third-party evaluations of model checkpoints to identify further opportunities for improvement. The third-party evaluations—which included 21 checkpoints of FLUX.1 Kontext [pro] and [dev]—focused on eliciting CSAM and NCII through adversarial testing with text-only prompts, as well as uploaded images with text prompts. Next, we conducted a final third-party evaluation of the proposed release checkpoints, focused on text-to-image and image-to-image CSAM and NCII generation. The final FLUX.1 Kontext [pro] (as offered through the FLUX API only) and FLUX.1 Kontext [dev] (released as an open-weight model) checkpoints demonstrated very high resilience against violative inputs, and FLUX.1 Kontext [dev] demonstrated higher resilience than other similar open-weight models across these risk categories. Based on these findings, we approved the release of the FLUX.1 Kontext [pro] model via API, and the release of the FLUX.1 Kontext [dev] model as openly-available weights under a non-commercial license to support third-party research and development.
Inference filters. We are applying multiple filters to intercept text prompts, uploaded images, and output images on the FLUX API for FLUX.1 Kontext [pro]. Filters for CSAM and NCII are provided by Hive, a third-party provider, and cannot be adjusted or removed by developers. We provide filters for other categories of potentially harmful content, including gore, which can be adjusted by developers based on their specific risk profile. Additionally, the repository for the open FLUX.1 Kontext [dev] model includes filters for illegal or infringing content. Filters or manual review must be used with the model under the terms of the FLUX.1 [dev] Non-Commercial License. We may approach known deployers of the FLUX.1 Kontext [dev] model at random to verify that filters or manual review processes are in place.
Content provenance. The FLUX API applies cryptographically-signed metadata to output content to indicate that images were produced with our model. Our API implements the Coalition for Content Provenance and Authenticity (C2PA) standard for metadata.
Policies. Access to our API and use of our models are governed by our Developer Terms of Service, Usage Policy, and FLUX.1 [dev] Non-Commercial License, which prohibit the generation of unlawful content or the use of generated content for unlawful, defamatory, or abusive purposes. Developers and users must consent to these conditions to access the FLUX Kontext models.
Monitoring. We are monitoring for patterns of violative use after release, and may ban developers who we detect intentionally and repeatedly violate our policies via the FLUX API. Additionally, we provide a dedicated email address (safety@blackforestlabs.ai) to solicit feedback from the community. We maintain a reporting relationship with organizations such as the Internet Watch Foundation and the National Center for Missing and Exploited Children, and we welcome ongoing engagement with authorities, developers, and researchers to share intelligence about emerging risks and develop effective mitigations.

## Inference:  
**Engine**: TensorRT   
**Test Hardware**: H100

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Prototype

```bash
invoke_url='https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-kontext-dev'

authorization_header="Authorization: Bearer $NVIDIA_API_KEY"
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data='{
"prompt": "",
"image": "",
"aspect_ratio":  "match_input_image" ,
"steps":  30 ,
"cfg_scale":  3.5 ,
"seed":  0 
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

const invokeUrl = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-kontext-dev"

const headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

const payload = {
"prompt": "",
"image": "",
"aspect_ratio":  "match_input_image" ,
"steps":  30 ,
"cfg_scale":  3.5 ,
"seed":  0 
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

invoke_url = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-kontext-dev"

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

payload = {
"prompt": "",
"image": "",
"aspect_ratio":  "match_input_image" ,
"steps":  30 ,
"cfg_scale":  3.5 ,
"seed":  0 
}

response = requests.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)
```