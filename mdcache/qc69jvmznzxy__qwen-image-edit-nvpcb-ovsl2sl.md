---
title: "qwen-image-edit-nvpcb-ovsl2sl"
publisher: "nvidia"
type: "endpoint"
updated: "2026-07-03T14:52:51.516Z"
description: "An image edit model specialized for Omniverse synthetic to photographic solder-light style captured at NVIDIA PCB inspection stations"
canonical: "https://build.nvidia.com/nvidia/qwen-image-edit-nvpcb-ovsl2sl"
---

# Model Overview

### Description:
Qwen-Image-Edit-NVPCB-OVSL2SL transforms synthetic solder-light printed-circuit-board (PCB) component crops — produced in NVIDIA Omniverse — into the photographic solder-light style captured at NVIDIA PCB inspection stations, so that downstream PCB inspection models trained on real solder-light photographs can be augmented with Omniverse-generated synthetic data. The release is an NVIDIA fine-tuned version of the Qwen-Image-Edit image-to-image diffusion pipeline (diffusion transformer, Qwen2.5-VL text encoder, Qwen-Image VAE, tokenizer, image processor, and scheduler configuration), specialized for the Omniverse → NVPCB solder-light style transfer. Qwen-Image-Edit-NVPCB-OVSL2SL v1.0.0 was developed by NVIDIA as part of the NVPCB inspection-data harmonization pipeline. This model is ready for commercial use.<br>

### License/Terms of Use:

Governing Terms: Use of this model is governed by the [NVIDIA Open Model Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: [Apache License, Version 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md).<br>

### Deployment Geography:
Global<br>

### Use Case:
NVIDIA engineers and researchers building PCB inspection / automated optical inspection (AOI) systems that need to be augmented with Omniverse-generated synthetic data. The model converts Omniverse-rendered solder-light PCB component crops into the photographic solder-light style produced by NVIDIA's physical inspection stations, closing the sim-to-real style gap so that inspection models trained on real photographs can be evaluated or augmented with synthetic Omniverse data. This model is **not** intended to be the primary inspection decision-maker; it is a sim-to-real data-translation step. Inspection pass/fail decisions must come from a downstream inspection model with human review.<br>

### Release Date:
Github 06/02/2026 via https://github.com/NVIDIA/paidf-augmentation<br>

## References(s):
- Qwen-Image-Edit base model — https://huggingface.co/Qwen/Qwen-Image-Edit
- Qwen2.5-VL text encoder — https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct
- LoRA: Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models," 2021 — https://arxiv.org/abs/2106.09685
- Diffusers library — https://github.com/huggingface/diffusers<br>

## Model Architecture:
**Architecture Type:** Transformer (diffusion transformer with cross-modal conditioning)<br>

**Network Architecture:** This release is a self-contained HuggingFace `diffusers` pipeline directory. All of the following components are redistributed as part of the release artifact:
- `transformer/` *(NVIDIA fine-tuned, redistributed)*: the upstream Qwen-Image-Edit flow-matching image-to-image diffusion transformer, fine-tuned by NVIDIA on the attention and feed-forward projections of `QwenImageTransformerBlock` (`to_q`, `to_k`, `to_v`, `to_out`, the cross-attention `add_{q,k,v}_proj` / `to_add_out`, and `img_mlp` / `txt_mlp`).
- `text_encoder/` *(redistributed unmodified)*: Qwen2.5-VL; attends over both the input image and the instruction prompt.
- `vae/` *(redistributed unmodified)*: Qwen-Image VAE.
- `tokenizer/`, `processor/`, `scheduler/`, and `model_index.json` *(redistributed unmodified)*: Qwen-Image-Edit tokenizer, image processor, scheduler configuration, and pipeline entry point.
- Fine-tuning methodology: NVIDIA fine-tuned the transformer using LoRA (rank 16, ~1.7 × 10^8 parameters introduced during training); the resulting weights were then merged back into the transformer for release, so the released artifact is a standalone diffusers pipeline that requires no separate adapter file at inference time.
- The released pipeline directory can be loaded directly with `diffusers.QwenImageEditPipeline.from_pretrained(...)`.<br>

**This model was developed based on Qwen-Image-Edit.**<br>

**Number of model parameters:** Approximately ~2.0 × 10^10 (20B) total parameters in the released checkpoint. Of these, ~1.7 × 10^8 (170M) parameters in the diffusion transformer were updated by NVIDIA fine-tuning; the remaining parameters come from the upstream Qwen-Image-Edit pipeline (transformer + Qwen2.5-VL text encoder + Qwen-Image VAE) and are redistributed unmodified.<br>

**Cumulative Compute:** ~0.6 GPU-hour total on a single NVIDIA H100 SXM (~0.5 GPU-hour for the 1500-step fine-tuning run + ~5 GPU-minutes for the latent/embedding cache build).<br>

**Estimated Energy and Emissions for Model Training:** ~0.4 kWh and ~0.16 kgCO2e total. Methodology: GPU energy = 0.6 GPU-hour × 0.7 kW (H100 SXM rated TDP) × 0.6 average utilization (typical for LoRA fine-tuning, which is not consistently GPU-bound) ≈ 0.25 kWh; multiplied by an assumed datacenter PUE of 1.5 to account for cooling and facility overhead ≈ 0.38 kWh; multiplied by 0.4 kgCO2e/kWh (U.S. national-grid average) ≈ 0.16 kgCO2e. Estimates use rated TDP rather than measured wall-power and are therefore conservative upper bounds; actual emissions depend on the specific datacenter's PUE and regional grid carbon intensity at training time.<br>

## Input(s):
**Input Type(s):** Image, Text<br>

**Input Format(s):**
- Image: PNG / JPG, Red, Green, Blue (RGB)
- Text: UTF-8 instruction prompt (English)<br>

**Input Parameters:**
- Image: Two-Dimensional (2D)
- Text: One-Dimensional (1D)<br>

**Other Properties Related to Input:** Fine-tuned at target area 262,144 pixels (~512×512); other resolutions are accepted by the underlying diffusers pipeline but NVIDIA fine-tuning was not performed at them, so style fidelity may degrade. Input must be a single Omniverse-rendered PCB component crop on an approximately black background, similar to the synthetic solder-light style the model was fine-tuned on. The accompanying instruction prompt is the fixed English sentence used during training, recovered automatically from the cached training metadata (`cache/_meta.pt`) at inference time; the trained prompt is:

> "Render this PCB component crop in the style of an NVPCB raked-solder-light photograph: dark reddish board with bright orange-red and blue specular highlights on the solder pads, photorealistic textures."

<br>

## Output(s)

**Output Type(s):** Image<br>

**Output Format(s):** PNG; Red, Green, Blue (RGB)<br>

**Output Parameters:** Two-Dimensional (2D)<br>

**Other Properties Related to Output:** Output resolution matches the input target area used during caching (~512×512). The output preserves component identity and board layout while transferring the rendering style from Omniverse-synthetic solder-light to NVPCB photographic solder-light.<br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.<br>

## Software Integration:
**Runtime Engine(s):**
- PyTorch (via HuggingFace `diffusers` `QwenImageEditPipeline`)<br>

**Supported Hardware Microarchitecture Compatibility:**
NVIDIA Ampere (A100) <br>
NVIDIA Hopper (H100) <br>
NVIDIA Lovelace (RTX 40-series) <br>

**Supported Operating System(s):**
- Linux<br>

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.<br>

## Model Version(s):
v1.0.0 — `qwen-image-edit-nvpcb-OVSL2SL` (NVIDIA fine-tune of the upstream Qwen-Image-Edit pipeline, 1500 training steps). The released artifact is a self-contained HuggingFace `diffusers` pipeline directory containing `transformer/`, `text_encoder/`, `vae/`, `tokenizer/`, `processor/`, `scheduler/`, and `model_index.json`.<br>

## Training, Testing, and Evaluation Datasets:

### Dataset Overview
- Total Number of Datasets: 1 (paired Omniverse-synthetic / NVPCB-photographic solder-light component crops; NVIDIA-internal)
- Total Size: 228 paired component crops (228 Omniverse-rendered synthetic solder-light inputs + 228 NVPCB photographic solder-light targets), ~512×512 each
- Dataset partition: Training ~95%, Validation ~5% (held-out by filename stem; no separate test split — evaluation is qualitative side-by-side plus CLIP-style embedding distance against held-out targets)
- Time period for data collection: H1 2026 (January – June 2026)<br>

## Training Dataset:

### Data Modality:
- Image
- Text (fixed instruction prompt)<br>

** Image Training Data Size

* [Less than a Million Images]

** Text Training Data Size

* [Less than a Billion Tokens]

** Data Collection Method by dataset
- Hybrid: Synthetic, Human (Omniverse synthetic rendering for the input side + manually-collected photography at NVIDIA inspection stations for the target side)

** Labeling Method by dataset
- Not Applicable — paired-image translation is supervised by the target image itself; no per-image label is required beyond the fixed instruction prompt.

**Properties:** 228 paired component crops with Omniverse-rendered synthetic solder-light as input and NVPCB photographic solder-light as target. Modality: image + a fixed English instruction prompt. Content nature: synthetic renders and photographs of inanimate PCBs (NVIDIA-internal). No personal data, no copyright-protected web content, no machine-generated text/speech. No human subjects are depicted.<br>

### Testing Dataset:
Data Collection Method by dataset:
* [Not Applicable]

Labeling Method by dataset:
* [Not Applicable]

**Properties** Not Applicable — the model is qualitatively evaluated on the held-out validation split (~5%) via side-by-side HTML reports rather than against a separate test split. <br>

### Evaluation Dataset:

** Data Collection Method by dataset
- Hybrid: Synthetic, Human (Omniverse synthetic rendering + manually-collected photography)

** Labeling Method by dataset
- Not Applicable

** Properties: Held-out validation pairs (~5%) from the same paired set, used to produce qualitative side-by-side comparison HTML reports and to compute CLIP-style embedding distance between generated and ground-truth target images.<br>

## Inference:
**Acceleration Engine:** PyTorch (native, bf16 weights) via `diffusers.QwenImageEditPipeline.from_pretrained(...)`, loaded directly from the released pipeline directory.<br>

**Test Hardware:**
- NVIDIA H100
- NVIDIA A100<br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.<br>

Please make sure you have proper rights and permissions for all input image and video content; if image or video includes people, personal health information, or intellectual property, the image or video generated will not blur or maintain proportions of image subjects included.<br>

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.<br>

For more detailed information on ethical considerations for this model, please see the Bias, Explainability, Privacy, and Safety & Security tabs of ModelCard++.<br>

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).<br>

# Get Help

## Getting started with the NIM
Deploying and integrating the NIM is straightforward thanks to our industry standard APIs. Visit the [Visual Generative AI NIM page](https://docs.nvidia.com/nim/visual-genai/latest/overview.html) for release documentation, deployment guides and more.

## Enterprise Support
Get access to knowledge base articles and support cases or [submit a ticket](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Specifications

- **Parameters:** 20,430,401,088

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing:  |  Not Applicable. The model operates on synthetic renders and photographs of inanimate printed circuit boards; no human subjects are depicted in the training, validation, or evaluation data, and no human-attribute label is used as a supervision signal.
Measures taken to mitigate against unwanted bias:                                                   |  Training data was screened to ensure it contains only PCB component crops and no incidental images of people, identifying documents, or workspaces. The fixed instruction prompt is reviewed and describes a lighting/style transformation only; it contains no demographic or human descriptors.
Bias Metric (If Measured):                                                                          |  Not Applicable.

## Explainability

| Field                                                                                                 | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Intended Task/Domain:                                                                                 | Sim-to-real paired image-to-image translation for printed-circuit-board (PCB) inspection. The model converts Omniverse-rendered synthetic solder-light component crops into the photographic solder-light style captured at NVIDIA PCB inspection stations, so that inspection models trained on real photographs can be augmented with synthetic Omniverse data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Model Type:                                                                                           | Diffusion transformer (LoRA fine-tune of Qwen-Image-Edit) with a Qwen2.5-VL text encoder that conditions on the input image as well as the instruction prompt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Intended Users:                                                                                       | NVIDIA engineers and researchers building PCB inspection / AOI systems that need to be augmented with Omniverse-generated synthetic data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output:                                                                                               | Image (RGB, PNG). The output is a re-rendered version of the input Omniverse PCB crop in the NVPCB photographic solder-light style; component identity and board layout are preserved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Describe how the model works:                                                                         | The input Omniverse-rendered PCB photograph is encoded into latents by the Qwen-Image VAE. In parallel, the fixed instruction prompt is encoded by Qwen2.5-VL conditioned on the input image. The released diffusion transformer — the upstream Qwen-Image-Edit transformer, fine-tuned by NVIDIA on its attention and feed-forward projections — iteratively denoises a noise tensor toward a latent that, when decoded by the VAE, reproduces the same scene under the target NVPCB photographic solder-light style described in the prompt. Flow-matching with Qwen-Image's resolution-aware time-shift schedule is used during training; Classifier-Free Guidance (CFG) is used at inference.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Not Applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Technical Limitations & Mitigation:                                                                   | (1) Fine-tuning was performed at one resolution (target area ~512×512); large deviations may degrade style fidelity. (2) Generalization outside the Omniverse-synthetic distribution it was trained on (e.g., real photographs as input, synthetic renders with non-black backgrounds, extreme close-ups or wide shots of full boards) is not guaranteed. (3) The model is a *sim-to-real data-translation* step and is not itself a defect-detection model; defect-detection decisions must be made by a downstream inspection model. (4) Style strength is fixed at release time and cannot be tuned at inference; if a different style strength is required, a new fine-tuned checkpoint must be released. Mitigation: Per-request prompt, true-CFG, and seed are exposed at inference time so a user can adjust prompt phrasing or sampling stochasticity when artifacts appear. The model must not be used as the sole signal for any inspection pass/fail decision; defect-detection decisions must come from a downstream inspection model with human review.                                                                                                                                                |
| Verified to have met prescribed NVIDIA quality standards:                                             | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Performance Metrics:                                                                                  | Qualitative side-by-side comparison of generated vs. held-out target images; CLIP-style embedding distance between generated and ground-truth target on held-out pairs; visual inspection of component-identity preservation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Potential Known Risks:                                                                                | The model may hallucinate solder-pad highlights or component textures that are not present on the underlying Omniverse-rendered board, especially on out-of-distribution inputs or at low LoRA scales. Downstream defect-detection models trained on these translated images may therefore learn spurious style cues; the model should be used as a *data augmentation aid*, not as a replacement for capture under the target lighting. Additionally, the underlying `QwenImageEditPipeline` technically accepts any RGB image as input; while this model was fine-tuned only on Omniverse-rendered PCB component crops, callers can supply arbitrary out-of-distribution images. As a result, this model can generate synthetic images and may produce content that is offensive, unsafe, misleading, indecent, or unsuitable for a target deployment. Users should implement robust safety guardrails — including content filtering, abuse monitoring, and access controls — to reduce the risk of harmful outputs. Users are responsible for ensuring that their use of the model complies with all applicable laws and regulations, and for regularly reviewing and updating their guardrails as risks evolve. |
| Licensing:                                                                                            | Governing Terms: Use of this model is governed by the [NVIDIA Open Model Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: [Apache License, Version 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Privacy

| Field                                                                                                    | Response                                                                                                                                             |
|:---------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Generatable or reverse engineerable personal data?                                                       | No.                                                                                                                                                  |
| Personal data used to create this model?                                                                 | No.                                                                                                                                                  |
| Was consent obtained for any personal data used?                                                         | Not Applicable.                                                                                                                                      |
| How often is dataset reviewed?                                                                           | Before Release. The PCB image set is reviewed at the time of capture / render by the team that produced it and again before being used for training. |
| Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model? | No.                                                                                                                                                  |
| Is there provenance for all datasets used in training?                                                   | Yes.                                                                                                                                                 |
| Does data labeling (annotation, metadata) comply with privacy laws?                                      | Yes.                                                                                                                                                 |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | Not Applicable.                                                                                                                                      |
| NVIDIA Privacy Policy                                                                                    | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/                                                                                            |

## Safety & Security

| Field                                           | Response                                                                                                                                                                                                                                                                                                                          |
|:------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model Application Field(s):                     | Industrial / Machinery and Robotics — specifically printed-circuit-board (PCB) inspection sim-to-real data augmentation for automated optical inspection (AOI) workflows.                                                                                                                                                         |
| Describe the life critical impact (if present). | Not Applicable.                                                                                                                                                                                                                                                                                                                   |
| Use Case Restrictions:                          | Governing Terms: Use of this model is governed by the [NVIDIA Open Model Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: [Apache License, Version 2.0](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md).<br> |
| Model and dataset restrictions:                 | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.                                                                                                                 |

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