---
title: "flux-3-image-klein"
publisher: "black-forest-labs"
type: "endpoint"
updated: "2026-10-15T18:26:40.926Z"
description: "FLUX 3 Image Klein is a state-of-the-art open-weight image generation and editing model"
canonical: "https://build.nvidia.com/black-forest-labs/flux-3-image-klein"
---

# Overview

## Description

FLUX 3 Image Klein is an open-weights model family developed by Black Forest Labs for text-to-image generation and image editing. It takes a text prompt and up to 10 reference images and returns one image, supporting single-reference edits, multi-reference compositions, and prompt-based bounding-box layout control. Its image transformer has 5.6 billion parameters and uses Qwen3-VL-4B-Instruct as a separate text encoder.

*This model is ready for non-commercial use.*

The vendor describes commercial production use for Qualifying Users under the FLUX Kommunity License v1.0, subject to its conditions and restrictions; other uses may require a separate license from Black Forest Labs.

## Third-Party Community Consideration:

This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [FLUX 3 Image Klein Base Model Card](https://huggingface.co/black-forest-labs/flux-3-image-klein-base)

## License and Terms of Use:

**GOVERNING TERMS:** Use of this container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and [Product-Specific Terms for NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). The Flux 3 Image Klein model is available at [FLUX 3 Image Klein](https://huggingface.co/black-forest-labs/flux-3-image-klein) and governed by its accompanying license.

## Deployment Geography:

Global

## Use Case:

**Use Case:** Creators and developers can deploy the NIM for text-to-image generation, single-reference editing, and multi-reference composition. The downloadable undistilled Base checkpoint is the starting point for fine-tuning, LoRA training, and research; the distilled checkpoint is intended for generation and editing.

## Reference(s):

**References:**

- [FLUX 3 Image Klein Base source repository](https://huggingface.co/black-forest-labs/flux-3-image-klein-base)
- [FLUX 3 Image Klein source repository](https://huggingface.co/black-forest-labs/flux-3-image-klein)
- [FLUX 3 bounding-box prompting guide](https://docs.bfl.ai/flux_3/flux3_image_bounding_boxes)
- [Black Forest Labs: Capable, Open, and Safe: Combating AI Misuse](https://bfl.ai/blog/capable-open-and-safe-combating-ai-misuse)

## Model Architecture:

**Architecture Type:** Transformer  
**Network Architecture:** Transformer  
**Total Parameters:** 5.6B (image transformer only)  
**Base Model:** Undisclosed

The image generation pipeline combines an image transformer with the separate Qwen3-VL-4B-Instruct text encoder and an image autoencoder. The vendor's 5.6B count covers only the image transformer; the complete pipeline parameter count is undisclosed. The exact image-transformer configuration is undisclosed. The vendor card does not identify a predecessor model for the undistilled base checkpoint; the text encoder is a component, not the base model of the image generator.

### Input:

**Input Types:** Text, Image  
**Input Formats:** String, Red, Green, Blue (RGB)  
**Input Parameters:** One-Dimensional (1D), Two-Dimensional (2D)  
**Other Input Properties:** A full scene caption may be accompanied by up to 10 reference images for editing or composition. Bounding-box layout control uses tagged caption elements and a JSON list; each bbox is [top, left, bottom, right] on a 0 to 1000 grid and provides prompt conditioning rather than a hard mask.

### Output:

**Output Types:** Image  
**Output Format:** Red, Green, Blue (RGB)  
**Output Parameters:** Two-Dimensional (2D)  
**Other Output Properties:** One generated or edited image at the requested resolution.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## Software Integration:

**Runtime Engines:**

- **SGLang Diffusion**

**Supported Hardware Microarchitecture Compatibility:**

- **NVIDIA Blackwell:** B200
- **NVIDIA Hopper:** H200
- **NVIDIA Lovelace**

**Preferred Operating Systems:** Linux, Other (Windows Subsystem for Linux)

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## Model Version(s)

- FLUX 3 Image Klein (distilled checkpoint; vendor reference setting: 16 steps, no guidance)
- FLUX 3 Image Klein Base (undistilled checkpoint; vendor reference setting: 50 steps, guidance 3.5)

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
**Evaluation Properties:** Undisclosed

## Inference

**Acceleration Engine:** SGLang  
**Test Hardware:** NVIDIA Hopper (H200)

## Additional Details

This card covers the downloadable NIM model family. Both checkpoints share the text encoder and image autoencoder; fine-tuning and LoRA training use the undistilled Base checkpoint. Hosted Preview API use is governed by its separate trial-service terms.

The vendor also provides a distilled FLUX 3 Image Klein checkpoint. Both packages include BF16 weights and FP8 and NVFP4 variants, the same Qwen3-VL-4B-Instruct text encoder, and an image autoencoder. Available model-package precision variants do not establish the precision selected by a particular NIM deployment.

### Prompting and limitations

- Describe the target scene, including framing, subject, background, and lighting. For edits, describe the target image with the requested change included in the caption.
- Reference images condition the output but do not guarantee preservation of the original composition. Edits can change content outside a requested bounding box, elements can extend beyond their boxes, and small requested elements may not appear.
- Prompt upsampling depends on the inference implementation. The vendor reference code obtains its prompt upsampler separately; without upsampling, use a full scene caption. Short prompts can produce generic output.
- The model is not intended or able to provide factual information. Rendered text can be inaccurate or distorted.
- The model can represent or amplify training-data biases and can fail to follow prompts. Prompt-following quality depends strongly on prompting style.

### Responsible use and restrictions

The vendor card identifies restrictions covering military purposes; surveillance and related research; biometric processing; unlawful, unsafe, fraudulent, defamatory, or abusive activity; unlawful content including child sexual abuse material or non-consensual intimate imagery; violations of third-party, publicity, or digital replica rights; and use of the model, derivatives, or outputs to improve another AI model with a similar function. Export controls and sanctions also apply. Consult the complete license for the applicable restrictions.

The vendor describes Qualifying Users as users whose gross annualized revenue, together with affiliates, is below USD 5 million. Permission to generate commercial outputs is conditional and does not provide blanket permission for commercial fine-tuning or distribution. The vendor license requires qualifying users to maintain content filters or review outputs for unlawful or infringing content before distribution, display, transmission, or dissemination, and to disclose AI generation or modification when required by law.

The Qwen3-VL-4B-Instruct text encoder is provided under Apache 2.0. Black Forest Labs grants no trademark rights through the model license; derivatives must not be represented as official, endorsed, approved, or validated BFL products without written authorization. These source-license disclosures do not replace the governing terms above.

The vendor reports evaluating and mitigating risks including child sexual abuse material and non-consensual intimate imagery before release. NVIDIA deployment uses Cosmos pre- and post-generation guardrails; see the [Cosmos-1.0-Guardrail Model Card](https://huggingface.co/nvidia/Cosmos-1.0-Guardrail).

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please make sure you have proper rights and permissions for all input image content; if image includes people, personal health information, or intellectual property, the image generated will not blur or maintain proportions of image subjects included.

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Specifications

- **Parameters:** 5,548,681,984

## Capabilities

- **Function Calling:** Not supported

## Prototype

```bash
invoke_url='https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux-3-image-klein'

authorization_header="Authorization: Bearer $NVIDIA_API_KEY"
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data='{
"prompt": "",
"image": [""],
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

const invokeUrl = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux-3-image-klein"

const headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

const payload = {
"prompt": "",
"image": [""],
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

invoke_url = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux-3-image-klein"

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

payload = {
"prompt": "",
"image": [""],
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