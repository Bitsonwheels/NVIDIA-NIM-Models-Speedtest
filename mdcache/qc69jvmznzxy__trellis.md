---
title: "TRELLIS"
publisher: "microsoft"
type: "endpoint"
updated: "2025-09-03T07:04:29.314Z"
description: "MSFT TRELLIS is a 3D AI model that generates high-quality 3D assets from text or image inputs."
canonical: "https://build.nvidia.com/microsoft/trellis"
---

# Overview

## Description:   
MSFT TRELLIS 3D is an asset generation model capable of producing detailed meshes directly from text prompts or images. With multiple size variants, TRELLIS offers options for users aiming to maximize quality and/or speed.
This model is ready for non-commercial/commercial use.

## Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to:
* [microsoft/TRELLIS-image-large Model Card](https://huggingface.co/microsoft/TRELLIS-image-large)
* [microsoft/TRELLIS-text-large Model Card](https://huggingface.co/microsoft/TRELLIS-text-large)

### License/Terms of Use

GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Community Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). Additional Information: MIT license.

### Deployment Geography:

Global

## Use Case:  

Creators and professionals can use this model to generate high-quality images from text prompts, simplifying visual communication.

### Release Date:

* Build.Nvidia.com September 2, 2025 via [https://build.nvidia.com/microsoft/trellis](https://build.nvidia.com/microsoft/trellis)   
* Huggingface December 2, 2024 via [https://huggingface.co/microsoft/TRELLIS-image-large](https://huggingface.co/microsoft/TRELLIS-image-large)   

### References

* [TRELLIS project page ](https://microsoft.github.io/TRELLIS/)   

## Model Architecture: 
**Architecture Type**: Transformer  
**Network Architecture**: Sparse Flow Transformer  
**Number of model parameters**: TRELLIS-image-large-1.2B, TRELLIS-text-base-342M, TRELLIS-text-large 1.1B.  

## Input:  
**Input Type**: Text, Image   
**Input Parameters**: Text: One-Dimensional (1D); Image: Two-Dimensional (2D)    
**Input Format**: Text: String. Image: Red, Green, Blue (RGB)    
**Other Properties Related to Input**: Steps, Classifier-Free Guidance Scale and Seed

## Output:  
**Output Type**: 3D Object   
**Output Parameters**: Three-Dimensional (3D)   
**Output Format**:  Graphics Library Binary (GLB)   

## Software Integration:
**Runtime Engines:**
* Pytorch

**Supported Hardware Platforms**:  
* NVIDIA Blackwell <br> 
* NVIDIA Hopper <br>   
* NVIDIA Lovelace <br>  

**Supported Operating Systems**: Linux, Windows Subsystem for Linux <br> 

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Model Version(s):  
* TRELLIS-image-large 
* TRELLIS-text-large

# Training, Testing, and Evaluation Datasets:

## Training Dataset:

**Link:** https://huggingface.co/datasets/JeffreyXiang/TRELLIS-500K

**Data Modality:** Image, Text, 3D Objects     

* Data Collection Method by dataset: Automated
* Labeling Method by dataset: Automated

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** TRELLIS-500K is a dataset of 500K 3D assets curated from Objaverse(XL), ABO, 3D-FUTURE, HSSD, and Toys4k, filtered based on aesthetic scores.

## Testing Dataset:

**Link:** https://huggingface.co/datasets/JeffreyXiang/TRELLIS-500K

**Data Modality:** Image, Text, 3D Objects    

* Data Collection Method by dataset: Automated
* Labeling Method by dataset: Automated

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** TRELLIS-500K is a dataset of 500K 3D assets curated from Objaverse(XL), ABO, 3D-FUTURE, HSSD, and Toys4k, filtered based on aesthetic scores.

## Evaluation Dataset:  

**Link:** https://huggingface.co/datasets/JeffreyXiang/TRELLIS-500K

**Data Modality:** Image, Text, 3D Objects    

* Data Collection Method by dataset: Automated
* Labeling Method by dataset: Automated

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  TRELLIS-500K is a dataset of 500K 3D assets curated from Objaverse(XL), ABO, 3D-FUTURE, HSSD, and Toys4k, filtered based on aesthetic scores.

## Inference:  
**Engine**: Pytorch   
**Test Hardware**: L40S

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please  report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Prototype

```bash
invoke_url='https://ai.api.nvidia.com/v1/genai/microsoft/trellis'

authorization_header="Authorization: Bearer $NVIDIA_API_KEY"
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data='{
"image": "",
"slat_cfg_scale": ,
"ss_cfg_scale": ,
"slat_sampling_steps": ,
"ss_sampling_steps": ,
"seed": 
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

const invokeUrl = "https://ai.api.nvidia.com/v1/genai/microsoft/trellis"

const headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

const payload = {
"image": "",
"slat_cfg_scale": ,
"ss_cfg_scale": ,
"slat_sampling_steps": ,
"ss_sampling_steps": ,
"seed": 
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

invoke_url = "https://ai.api.nvidia.com/v1/genai/microsoft/trellis"

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

payload = {
"image": "",
"slat_cfg_scale": ,
"ss_cfg_scale": ,
"slat_sampling_steps": ,
"ss_sampling_steps": ,
"seed": 
}

response = requests.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)
```