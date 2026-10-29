---
title: "nemotron-parse-2.0"
publisher: "nvidia"
type: "endpoint"
updated: "2026-09-11T21:29:41.274Z"
description: "Cutting-edge vision-language model excelling in retrieving text and metadata from images."
canonical: "https://build.nvidia.com/nvidia/nemotron-parse-2.0"
---

# NVIDIA Nemotron Parse 2.0 Overview

## Description:  
NVIDIA Nemotron Parse 2.0 transforms document images into structured, machine-readable representations with text, layout classes, bounding boxes, and reading-order information. Given a Red, Green, Blue (RGB) document image and a task prompt, the model produces formatted text and spatial annotations for document elements such as titles, paragraphs, captions, tables, charts, page headers, page footers, footnotes, pictures, and bibliography entries. Compared with NVIDIA Nemotron Parse v1.2, NVIDIA Nemotron Parse 2.0 adds an approximately 20k-token vocabulary expansion for more efficient multilingual support, chart-aware document parsing with the `<class_Chart>` class token, and updated training coverage for chart/table-heavy documents and stronger support for many languages. NVIDIA Nemotron Parse 2.0 is intended for document understanding, information retrieval, data extraction, and multimodal data-curation workflows.
NVIDIA Nemotron Parse 2.0 was developed by NVIDIA as a part of Nemotron.  
_This model is ready for commercial or non-commercial use._

### License/Terms of Use:
**GOVERNING TERMS:** Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1).

### Deployment Geography:  
Global

### Use Case:  
NVIDIA Nemotron Parse 2.0 is designed for developers and teams building document intelligence, retrieval-augmented generation (RAG), curator, extractor, and agentic AI applications. It converts scanned or rendered PDFs, presentation slides, forms, reports, tables, and mixed-content document pages into structured outputs for downstream indexing, retrieval, analytics, model training-data creation, and human-in-the-loop review. The model supports document understanding, OCR, layout parsing, table extraction, and text extraction with spatial grounding.  

### Release Date:
**Build.NVIDIA.com:** 09/11/2026 via [link](https://build.nvidia.com/nvidia/nemotron-parse-2.0)
**HuggingFace:** 06/30/2026 via [link](https://huggingface.co/nvidia/NVIDIA-Nemotron-Parse-2.0)

## Reference(s):
[Hugging Face Transformers mBART documentation](https://huggingface.co/docs/transformers/en/model_doc/mbart)  
[NVIDIA C-RADIO](https://huggingface.co/nvidia/C-RADIO)  

## Model Architecture:   
**Architecture Type:** Transformer   
**Network Architecture:** Vision Encoder (ViT-H based on NVIDIA C-RADIO) + Adapter (1D convolutions and normalization layers) + Decoder (mBART with 10 blocks)  
**This model was developed based on mBART.**  
**Number of model parameters:** 905M  

## Computational Load
**Cumulative Compute:** 1.50x10^21 FLOP  
**Estimated Energy and Emissions for Model Training:** ~4.64 MWh  

## Input:  
**Input Type(s):** Image, Text  
**Input Format(s):**
* Image: Red, Green, Blue (RGB)
* Text: String

**Input Parameters:** Two-Dimensional (2D), One-Dimensional (1D)  
**Other Properties Related to Input:** The model accepts RGB images with a recommended maximum resolution of 1664×2048 pixels and a minimum of 1024×1280 pixels. Input prompts consist of control tokens; the default prompt is `</s><output_markdown>` to extract bounding boxes, classes, and markdown text. The model can also emit `<class_Chart>` tokens for detected chart regions.  

## Output:  
**Output Type(s):** Text  
**Output Format:** String  
**Output Parameters:** One-Dimensional (1D)  
**Other Properties Related to Output:** Maximum output length configurable via max_new_tokens parameter (default 9000, max determined by generation config). Supports streaming output via transformers generate. Output is UTF-8 encoded text in formats such as markdown, LaTeX, HTML, JSON, or plain text.  

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:
**Runtime Engine(s):**
* Transformers
* vLLM

**Supported Hardware Microarchitecture Compatibility:**
* NVIDIA Ampere
* NVIDIA Blackwell
* NVIDIA Hopper
* NVIDIA Turing

**Supported Operating System(s):** Linux  

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.  

This AI model can be embedded as an Application Programming Interface (API) call into the software environment described above.

## Model Version(s): 
NVIDIA Nemotron Parse 2.0  

Integration requires Transformers or vLLM frameworks and runs on Linux with NVIDIA Ampere, NVIDIA Blackwell, NVIDIA Hopper, or NVIDIA Turing GPUs.

## Training, Testing, and Evaluation Datasets:

## Training Dataset:

**Data Modality:**
* Image  
* Text  

**Image Training Data Size:** 1 Million to 1 Billion Images  
**Text Training Data Size:** 1 Billion to 10 Trillion Tokens  
**Data Collection Method by dataset:** Hybrid: Automated/Manually-Collected/Synthetic  
**Labeling Method by dataset:** Hybrid: Automated/Manually-Labelled/Synthetic  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):** The training set contains millions of image-text items aggregated from large document, table, and layout datasets. It consists of document-page and table images paired with OCR text, bounding boxes, and layout labels. Sources include rendered digital documents, scientific papers, PDFs, Wikipedia-style pages, and synthetic document, table, word, and character renderings. Annotations are derived from OCR and layout models, third-party OCR services, synthetic-generation pipelines, and human labeling.

### Testing Dataset:

**Data Collection Method by dataset:** Hybrid: Automated/Manually-Collected/Synthetic  
**Labeling Method by dataset:** Hybrid: Automated/Manually-Labelled/Synthetic  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Tested on internal and public document-understanding benchmarks covering OCR quality, layout structure, table parsing, reading order, and visual grounding.

### Evaluation Dataset:
**Benchmark Score:** See benchmark table below.  

Benchmark coverage:  
* ParseBench evaluates document parsing across text fidelity, semantic formatting, tables, charts, and visual grounding with layout boxes/classes.  
* IndicVisionBench evaluates OCR quality for Indic-language pages, including Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, and Telugu.  
* MOSCAR evaluates multilingual synthetic OCR across broad script coverage, including Latin, Arabic, Cyrillic, Chinese, Hangul, Japanese, Indic scripts, Hebrew, Thai, Greek, and others.  
* OmniDocBench Notes (Handwriting) evaluates text-block edit distance on note-style document pages from the `data_source: note` slice.

The following results compare NVIDIA Nemotron Parse 2.0 with NVIDIA Nemotron Parse v1.2 on internal and public evaluation benchmarks. NVIDIA Nemotron Parse 2.0 results use the equal-weight checkpoint soup from training checkpoints 58k, 60k, 62k, 64k, and 66k. Unless marked otherwise, metrics are higher-is-better; arrows indicate the direction of the 2.0 change relative to v1.2.

| Benchmark | Metric | NVIDIA Nemotron Parse v1.2 | NVIDIA Nemotron Parse 2.0 | Change |
| :---- | :---- | :---- | :---- | :---- |
| ParseBench | Overall score | 0.5782 | 0.6391 | ↑ +0.0609 |
| OmniDocBench Notes (Handwriting) | Text edit distance (lower is better) | 0.9739 | 0.3395 | ↓ -0.6343 |
| IndicVisionBench | Overall ANLS character | 0.0612 | 0.7203 | ↑ +0.6592 |
| MOSCAR (Multilingual) | Overall BoC F1 | 0.4410 | 0.9102 | ↑ +0.4692 |

**Data Collection Method by dataset:** Hybrid: Automated/Manually-Collected  
**Labeling Method by dataset:** Hybrid: Automated/Manually-Labelled  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Evaluated on internal and public document-understanding benchmarks covering OCR quality, layout structure, table parsing, reading order, and visual grounding.

## Inference:
**Acceleration Engine:** vLLM
**Test Hardware:**
* NVIDIA Ampere (A100, A10G)
* NVIDIA Blackwell (B200, GB200, RTX PRO 6000)
* NVIDIA Hopper (H100)
* NVIDIA Lovelace (L40S)

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  
Please make sure you have proper rights and permissions for all input image and video content; if image or video includes people, personal health information, or intellectual property, the image or video generated will not blur or maintain proportions of image subjects included.  
For more detailed information on ethical considerations for this model, please see the Model Card++ [Explainability](explainability.md), [Bias](bias.md), [Safety & Security](safety_security.md), and [Privacy](privacy.md) Subcards.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

**Generated by NVIDIA Model Card Generator Toolkit.**

## Specifications

- **Context Length:** 9,000 tokens
- **Parameters:** 903,049,225

## Capabilities

- **Function Calling:** Supported
- **Structured Output:** Not supported
- **Reasoning:** Supported

## Bias

# Bias Subcard

## Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing:

None of the Above

## Measures taken to mitigate against unwanted bias:

None of the Above

## Bias Metric (If Measured):

Not Applicable

## Explainability

# Explainability Subcard

## Intended Task/Domain:

Document Understanding and Optical Character Recognition (OCR)

## Model Type:

Transformer

## Intended Users:

Developers and teams building document intelligence, retrieval-augmented generation (RAG), curator, extractor, and agentic AI applications for converting scanned or rendered PDFs, presentation slides, forms, reports, tables, and mixed-content document pages into structured outputs for downstream indexing, retrieval, analytics, model training-data creation, and human-in-the-loop review.

## Output:

Text

## Describe how the model works:

This transformer-based model uses a Vision Encoder (ViT-H based on NVIDIA C-RADIO) for image processing, an Adapter with 1D convolutions and normalization layers, and a Decoder (mBART with 10 blocks) to transform document images into structured, machine-readable representations with text, layout classes, bounding boxes, and reading-order information.

## Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:

Not Applicable

## Technical Limitations and Mitigation:

NVIDIA Nemotron Parse 2.0 may produce OCR and document-structure extraction errors, including omitted, substituted, duplicated, or misordered text; incorrect layout classes or bounding boxes; inaccurate reading order; and incomplete or malformed tables and charts. Performance may vary with image resolution, scan quality, handwriting, layout complexity, and language or script. To mitigate these limitations, follow the recommended input-resolution guidance, validate parsed output against the source document, and use human review for accuracy-sensitive workflows.

## Verified to have met prescribed NVIDIA quality standards:

Yes

## Performance Metrics:

Accuracy (Top-1)
F-1 Score
Throughput & Latency

## Potential Known Risks:

Incorrect or incomplete document parsing can propagate inaccurate text, spatial annotations, or document structure into downstream indexing, retrieval, analytics, retrieval-augmented generation, model training-data creation, or agentic workflows. These errors may cause downstream systems to retrieve the wrong content, miss relevant content, or act on an incorrect representation of the source document. Do not rely on parsed output as the sole source for accuracy-sensitive or high-impact decisions; retain the original document for validation and review.

## Terms of Use/Licensing:

**GOVERNING TERMS:** Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1).

## Privacy

# Privacy Subcard

## Generatable or reverse engineerable personal data?

No

## Personal data used to create this model?

Yes

## Was consent obtained for any personal data used?

Unknown (Externally-Sourced Data)

## How often is dataset reviewed?

Before Every Release

## Is a mechanism in place to honor data subject right of access or deletion of personal data?

Unknown (Externally-Sourced Data)

## If personal data was collected for the development of the model, was it collected directly by NVIDIA?

No

## If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?

Not Applicable

## If personal data was collected for the development of this AI model, was it minimized to only what was required?

Yes

## Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model?

No

## Is there provenance for all datasets used in training?

Yes

## Does data labeling (annotation, metadata) comply with privacy laws?

Yes

## Is data compliant with data subject requests for data correction or removal, if such a request was made?

No, not possible with externally sourced data.

## Applicable Privacy Policy

https://www.nvidia.com/en-us/about-nvidia/privacy-policy/

## Safety & Security

# Safety & Security Subcard

## Model Application Field(s):

Image Understanding/Object Detection

## Describe the life critical impact (if present).

Not Applicable

## Use Case Restrictions:

**GOVERNING TERMS:** Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1).

## Model and dataset restrictions:

The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.

## Prototype

```python
from openai import OpenAI

client = OpenAI(
base_url = "https://integrate.api.nvidia.com/v1",
api_key = "$NVIDIA_API_KEY"
)

messages = [
{
"role": "user",
"content": [
{
"type": "text",
"text": "</s><s><predict_bbox><predict_classes><output_markdown><predict_text_in_pic>"
},
{
"type": "image_url",
"image_url": {
"url": "https://assets.ngc.nvidia.com/products/api-catalog/nemoretriever-parse/example_1.jpg"
}
}
]
}
]

completion = client.chat.completions.create(
model="nvidia/nemotron-parse-2.0",
messages=messages,
temperature=0,
top_p=1,
max_tokens=1024,
stream=False
)

print(completion.choices[0].message.content)
```

```python
from langchain_nvidia_ai_endpoints import ChatNVIDIA

client = ChatNVIDIA(
model="nvidia/nemotron-parse-2.0",
api_key="$NVIDIA_API_KEY",
temperature=0,
top_p=1,
max_tokens=1024,
)

messages = [
{
"role": "user",
"content": [
{
"type": "text",
"text": "</s><s><predict_bbox><predict_classes><output_markdown><predict_text_in_pic>"
},
{
"type": "image_url",
"image_url": {
"url": "https://assets.ngc.nvidia.com/products/api-catalog/nemoretriever-parse/example_1.jpg"
}
}
]
}
]

response = client.invoke(messages)
print(response.content)
```

```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
apiKey: '$NVIDIA_API_KEY',
baseURL: 'https://integrate.api.nvidia.com/v1',
})

async function main() {
const completion = await openai.chat.completions.create({
model: "nvidia/nemotron-parse-2.0",
messages: [
{
"role": "user",
"content": [
{
"type": "text",
"text": "</s><s><predict_bbox><predict_classes><output_markdown><predict_text_in_pic>"
},
{
"type": "image_url",
"image_url": {
"url": "https://assets.ngc.nvidia.com/products/api-catalog/nemoretriever-parse/example_1.jpg"
}
}
]
}
],
temperature: 0,
top_p: 1,
max_tokens: 1024,
stream: false,
})

process.stdout.write(completion.choices[0]?.message?.content ?? '')

}

main();
```

```bash
curl https://integrate.api.nvidia.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-d '{
"model": "nvidia/nemotron-parse-2.0",
"messages": [
{
"role": "user",
"content": [
{
"type": "text",
"text": "</s><s><predict_bbox><predict_classes><output_markdown><predict_text_in_pic>"
},
{
"type": "image_url",
"image_url": {
"url": "https://assets.ngc.nvidia.com/products/api-catalog/nemoretriever-parse/example_1.jpg"
}
}
]
}
],
"temperature": 0,
"top_p": 1,
"max_tokens": 1024,
"stream": false
}'
```