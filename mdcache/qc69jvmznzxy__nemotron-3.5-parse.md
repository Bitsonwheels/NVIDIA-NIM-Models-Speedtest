---
title: "nemotron-3.5-parse"
publisher: "nvidia"
type: "endpoint"
updated: "2026-10-23T17:30:21.880Z"
description: "Extract text, tables, and document layout from page images."
canonical: "https://build.nvidia.com/nvidia/nemotron-3.5-parse"
---

# Nemotron 3.5 Parse

## Description

Nemotron 3.5 Parse is a document image parser that produces structured, machine-readable text with semantic layout classes, bounding boxes, and reading order. It combines a C-RADIOv4-SO400M vision encoder with a 10-layer mBART decoder that consumes the visual sequence as a causal prefix. The release uses dynamic rectangular NaViT preprocessing, content-normalized coordinates, grouped-query self-attention (16 query heads and 8 key/value heads), a 72,505-token multilingual tokenizer, and chart-aware output through the `<class_Chart>` token. It is intended for document understanding, information retrieval, data extraction, and multimodal data-curation workflows.

Nemotron 3.5 Parse was developed by NVIDIA as a part of Nemotron.

*This model is ready for commercial or non-commercial use.*

## License and Terms of Use:

**GOVERNING TERMS:** Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1).

**Model and Tokenizer Terms:** Your use of this model is governed by the [OpenMDW License Agreement, version 1.1](https://openmdw.ai/license/1-1/). Use of the tokenizer included in this model is governed by the [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/). See [third-party notices](https://huggingface.co/nvidia/Nemotron-3.5-Parse/blob/main/THIRD_PARTY_NOTICES.md) for separately installed dependencies.

## Deployment Geography:

Global

## Use Case:

**Use Case:** Nemotron 3.5 Parse is designed for developers and teams building document intelligence, retrieval-augmented generation (RAG), curator, extractor, and agentic AI applications. It can convert scanned or rendered PDFs, presentation slides, forms, reports, tables, and mixed-content document pages into structured outputs for downstream indexing, retrieval, analytics, model training-data creation, and human-in-the-loop review.

## Release Date:

**Build.NVIDIA.com:** 10/20/2026 via [link](https://build.nvidia.com/nvidia/nemotron-3.5-parse)  
**Hugging Face:** 10/20/2026 via [link](https://huggingface.co/nvidia/Nemotron-3.5-Parse)

## Reference(s):

**References:**

* [Nemotron 3.5 Parse](https://huggingface.co/nvidia/Nemotron-3.5-Parse)
* [Hugging Face Transformers mBART documentation](https://huggingface.co/docs/transformers/en/model_doc/mbart)
* [NVIDIA C-RADIOv4-SO400M](https://huggingface.co/nvidia/C-RADIOv4-SO400M)

## Model Architecture:

**Architecture Type:** Transformer

**Network Architecture:**

* Vision Encoder: NVIDIA C-RADIOv4-SO400M (`vit_so400m_patch16_224`) with dynamic rectangular NaViT preprocessing
* Adapter Layer: 1D convolutions and normalization layers that compress the vision latent sequence before decoding
* Decoder: 10-layer mBART causal visual-prefix decoder with 16 query heads and 8 key/value heads
* Auxiliary Prediction Head: One trained one-step multi-token-prediction (MTP) head is included in `model.safetensors`. Transformers uses the normal decoder for generation; the vLLM plugin enables the bundled head for one-token speculative decoding.
* Tokenizer: 72,505 entries with multilingual and task/control tokens including `<predict_bbox>`, `<predict_classes>`, `<predict_text_in_pic>`, and `<class_Chart>`; the decoder embedding is padded to 72,512 rows. Use of the tokenizer included in this model is governed by the [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/).

**Total Parameters:** 630.8M (630,800,496 unique trainable parameters, including the MTP head; shared decoder embedding/output weights are counted once)

### Input:

**Input Types:** Image, Text

**Input Formats:**

* Image: Red, Green, Blue (RGB)
* Text: Prompt string

**Input Parameters:** Image: Two-Dimensional (2D), Text: One-Dimensional (1D)

**Other Input Properties:**

* Recommended maximum input resolution (Width, Height): 1664, 2048
* Channel Count: 3
* Prompt format: one task prompt composed from the supported control tokens. The default prompt extracts bounding boxes, semantic classes, and text in markdown format: `</s><s><predict_bbox><predict_classes><output_markdown><predict_text_in_pic>`.

### Output:

**Output Types:** Text

**Output Format:** String

**Output Parameters:** One-Dimensional (1D)

**Other Output Properties:** Nemotron 3.5 Parse returns a string encoding document text, semantic element classes, and content-normalized bounding boxes. Scale x coordinates by the evaluated image width and y coordinates by its height. Postprocessing utilities can convert table or chart-associated text into LaTeX, HTML, markdown, JSON, or CSV where supported.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## Software Integration:

**Runtime Engine(s):**

* **Native CUDA backend: Photon Engine**

**Supported Hardware Microarchitecture Compatibility:**

* **NVIDIA Ampere:** A100, A10G
* **NVIDIA Blackwell:** GB200, GB10, RTX PRO 6000 Blackwell Server Edition
* **NVIDIA Hopper:** H100 NVL
* **NVIDIA Lovelace:** L40S

**Supported Operating System(s):** Linux

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## Model Version(s)

Nemotron 3.5 Parse

## Training, Testing, and Evaluation Datasets:

### Training Dataset

**Data Modality:** Image, Text

**Image Training Data Size:** 1 Million to 1 Billion Images

**Text Training Data Size:** 1 Billion to 10 Trillion Tokens

**Data Collection Method by dataset:** Hybrid: Automated, Manually-Collected, Synthetic

**Labeling Method by dataset:** Hybrid: Automated, Manually-Labeled, Synthetic  
**Labeling Details:** Labels are produced through a combination of automated OCR and layout annotation, manual annotation, and synthetic generation. The combination varies by constituent dataset.

**Properties:** The training set contains millions of image-text items aggregated across large document, table, and layout datasets. The data consists of document-page and table images paired with OCR text, bounding boxes, and layout labels. Sources include rendered digital documents, scientific papers, PDFs, Wikipedia-style pages, and synthetic document, table, word, and character renderings. Annotations come from OCR and layout models, third-party OCR services, synthetic-generation pipelines, and human labeling.

### Testing Dataset

**Data Collection Method by dataset:** Hybrid: Automated, Manually-Collected, Synthetic  
**Collection Details:** Sources combine automated collection, manually collected material, and synthetic generation; methods vary by constituent dataset.

**Labeling Method by dataset:** Hybrid: Automated, Manually-Labeled, Synthetic  
**Labeling Details:** Labels are produced through a combination of automated OCR and layout annotation, manual annotation, and synthetic generation. The combination varies by constituent dataset.

**Properties:** Tested on internal and public document-understanding benchmarks using document-page images and reference text, layout classes, bounding boxes, and structure annotations. Coverage includes OCR quality, layout structure, table parsing, reading order, and visual grounding across document types and languages.

### Evaluation Dataset

**Data Collection Method by dataset:** Hybrid: Automated, Manually-Collected, Synthetic  
**Collection Details:** Sources combine automated collection, manually collected material, and synthetic generation; methods vary by constituent dataset.

**Labeling Method by dataset:** Hybrid: Automated, Manually-Labeled, Synthetic  
**Labeling Details:** Labels are produced through a combination of automated OCR and layout annotation, manual annotation, and synthetic generation. The combination varies by constituent dataset.

**Properties:** Evaluated on internal and public document-understanding benchmarks covering OCR quality, layout structure, table parsing, reading order, and visual grounding. The ParseBench reference evaluation covers 2,078 unique document pages. Additional benchmarks cover Indic-language OCR and multilingual synthetic OCR across the scripts listed below.

Benchmark coverage:

* ParseBench evaluates document parsing across text fidelity, semantic formatting, tables, charts, and visual grounding with layout boxes/classes.
* IndicVisionBench evaluates OCR quality for Indic-language pages, including Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, and Telugu.
* MOSCAR evaluates multilingual synthetic OCR across broad script coverage, including Latin, Arabic, Cyrillic, Han, Hangul, Japanese, Indic scripts, Hebrew, Thai, Greek, and others.

### Evaluation Results

**Evaluation Benchmark Score:** ParseBench mean 69.05; MOSCAR corpus CER 1.46; IndicVision character ANLS 82.00.

**#1 ParseBench among models below 1B parameters, with 4.6× the measured page throughput of PaddleOCR-VL 1.6.** Nemotron 3.5 Parse scores 69.05 and processes 14.21 pages/s in the reference BF16 profile.

<details>
<summary><strong>Detailed Benchmark Comparison and Methodology</strong></summary>

| Model | Mean ↑ | Tables ↑ | Charts ↑ | Content Faithfulness ↑ | Semantic Formatting ↑ | Visual Grounding ↑ | Pages/s ↑ |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| PaddleOCR-VL 1.6 | 67.43 | 67.77 | 54.24 | 82.71 | 54.64 | 77.80 | 3.09 |
| Nemotron Parse 2.0 | 64.46 | 70.41 | 31.59 | 84.72 | 65.36 | 70.23 | 3.97 |
| **Nemotron 3.5 Parse** | **69.05** | **72.60** | 49.89 | **86.83** | **65.56** | 70.26 | **14.21** |

Paddle accuracy uses its unchanged official published results; its throughput uses the optimized full native pipeline on the same 2,078 pages and one H100. Paddle retains a 16,384-token context and 8,192-token output cap. Parse uses one-token MTP, a 16,384-token context, and an 8,744-token output cap. Timing excludes startup, image preload, and 16 warmups. [Paddle timing and settings](https://huggingface.co/nvidia/Nemotron-3.5-Parse/blob/main/reference/parsebench/paddle_optimized/README.md) are included.

| Benchmark / metric | Direction | Nemotron Parse 2.0 | Nemotron 3.5 Parse |
| :--- | :---: | ---: | ---: |
| MOSCAR · corpus CER | ↓ | 4.25 | **1.46** |
| IndicVision · character ANLS | ↑ | 67.44 | **82.00** |

</details>

Inference reference outputs and verification instructions are available in [reference/](https://huggingface.co/nvidia/Nemotron-3.5-Parse/blob/main/reference/README.md).

## Inference

**Acceleration Engine:** Native CUDA backend: Photon Engine

**Test Hardware:**

* NVIDIA Ampere (A100)
* NVIDIA Ampere (A10G)
* NVIDIA Blackwell (GB200)
* NVIDIA Blackwell (GB10)
* NVIDIA Blackwell (RTX PRO 6000 Blackwell Server Edition)
* NVIDIA Hopper (H100 NVL)
* NVIDIA Lovelace (L40S)

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please make sure you have proper rights and permissions for all input image and video content. If an input image contains people, personal health information, confidential business data, or intellectual property, the model may extract or reproduce visible text from that content.

For more detailed information on ethical considerations for this model, please see the Explainability, Bias, Safety, and Privacy subcards.
Please report model quality, risk, security vulnerabilities, or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Specifications

- **Context Length:** 9,000 tokens
- **Parameters:** 630,800,504

## Capabilities

- **Function Calling:** Not supported
- **Structured Output:** Not supported
- **Reasoning:** Not supported

## Bias

# Bias

Field | Response
:---- | :----
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing: | None
Measures taken to mitigate against unwanted bias: | Dataset curation, filtering, and evaluation include review across document types, layouts, languages, and scripts where available. Users should evaluate performance on their target document domains before deployment.
Bias Metric (If Measured): | Not measured as a demographic fairness metric. Model quality is evaluated through document parsing, OCR, layout, table, chart, and reading-order metrics.

## Explainability

# Explainability

Field | Response
:---- | :----
Intended Task/Domain: | Document understanding, OCR, layout parsing, table extraction, and text extraction with spatial grounding.
Model Type: | Transformer-based vision-encoder-decoder model.
Intended Users: | Developers and teams building document intelligence, retrieval-augmented generation (RAG), data-curation, extraction, and multimodal agent workflows.
Output: | Structured text containing document element classes, bounding boxes, reading-order information, chart/table annotations, and extracted text.
Describe how the model works: | Nemotron 3.5 Parse encodes a dynamically sized document image with C-RADIOv4-SO400M, compresses the visual features with a neck, and places them before the OCR prompt as a causal prefix to a 10-layer mBART decoder. The decoder uses grouped-query self-attention and produces structured document annotations with content-normalized boxes. The 72,505-token tokenizer includes multilingual, task-control, and chart-aware tokens such as `<class_Chart>`.
List the groups (or group characteristics) for which this was tested to produce comparable outcomes: | Not Applicable
Technical Limitations & Mitigation: | Performance can vary for low-resolution scans, motion blur, handwriting, decorative fonts, dense tables, unusual layouts, unsupported languages or scripts, and documents with heavy compression artifacts. Users should evaluate outputs on representative documents and use human review for high-impact workflows.
Verified to have met prescribed NVIDIA quality standards: | Yes
Performance Metrics: | OCR accuracy, layout/class accuracy, table extraction quality, chart extraction quality, reading-order quality, grounding quality, latency, throughput, and qualitative visual inspection.
Potential Known Risks: | The model may miss text, hallucinate structure, assign incorrect classes, produce inaccurate bounding boxes, or incorrectly order elements. Downstream systems should treat output as model-generated extraction results and apply validation, confidence checks, and human review where appropriate.
Licensing: | Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). Use of the tokenizer included in this model is governed by the [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/). See [third-party notices](https://huggingface.co/nvidia/Nemotron-3.5-Parse/blob/main/THIRD_PARTY_NOTICES.md) for separately installed dependencies.

## Privacy

# Privacy

Personal data was used to create Nemotron 3.5 Parse through externally sourced datasets. This personal data was not collected directly by NVIDIA. Whether consent was obtained for personal data used in externally sourced datasets is unknown. Whether a mechanism is in place to honor data-subject requests for access or deletion is also unknown for externally sourced data. Access to disclosures made to data subjects by NVIDIA is not applicable because NVIDIA did not collect this personal data directly. Personal data was minimized to only what was required for model development. The model is not intended to generate personal data from its weights, but it may extract personal data visible in user-provided input images. Data from user interactions with the model was not used to train it. Provenance is maintained for all training datasets, and data labeling complies with privacy laws. Datasets are reviewed before every release. Individual data-subject requests for correction or removal cannot be fulfilled for externally sourced data. Users should handle inference inputs and extracted outputs according to the personal or confidential information they may contain. For more information, please see the [NVIDIA Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/).

## Safety & Security

# Safety & Security

Field | Response
:---- | :----
Model Application Field(s): | Document intelligence, information retrieval, enterprise automation, data extraction, multimodal data curation, and retrieval-augmented generation workflows.
Describe the life critical impact (if present). | Not Applicable. This model is not intended to make life-critical, legal, medical, financial, or safety-critical decisions without downstream validation and human oversight.
Use Case Restrictions: | Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). Use of the tokenizer included in this model is governed by the [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/). See [third-party notices](https://huggingface.co/nvidia/Nemotron-3.5-Parse/blob/main/THIRD_PARTY_NOTICES.md) for separately installed dependencies.
Input permissions: | Users are responsible for ensuring they have rights and permissions for input documents and images.
Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.

**You are responsible for ensuring that your use of NVIDIA-provided models complies with all applicable laws.**

## Prototype

```python
import json
import requests

invoke_url = "https://ai.api.nvidia.com/v1/retrieval/nvidia/nemotron-3.5-parse/parse"
image_source = "https://assets.ngc.nvidia.com/products/api-catalog/nemoretriever-parse/example_1.jpg"

if image_source.startswith(("http://", "https://")):
image_bytes = requests.get(image_source).content
else:
with open(image_source, "rb") as image_file:
image_bytes = image_file.read()

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json"
}

# One rendered page (image/png or image/jpeg) plus optional JSON options, sent as multipart/form-data
files = {
"document": ("example_1.jpg", image_bytes, "image/jpeg"),
"options": (None, json.dumps({"decoding": {"max_output_tokens": 1024}}), "application/json")
}

response = requests.post(invoke_url, headers=headers, files=files)
response.raise_for_status()

result = response.json()
print(result["content"])
```

```javascript
const invokeUrl = "https://ai.api.nvidia.com/v1/retrieval/nvidia/nemotron-3.5-parse/parse";
const imageSource = "https://assets.ngc.nvidia.com/products/api-catalog/nemoretriever-parse/example_1.jpg";

const headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json"
};

async function main() {
const imageResponse = await fetch(imageSource);
const imageBlob = new Blob([await imageResponse.arrayBuffer()], { type: "image/jpeg" });

// One rendered page (image/png or image/jpeg) plus optional JSON options, sent as multipart/form-data
const form = new FormData();
form.append("document", imageBlob, "example_1.jpg");
form.append("options", new Blob([JSON.stringify({ decoding: { max_output_tokens: 1024 } })], { type: "application/json" }));

const response = await fetch(invokeUrl, { method: "POST", headers: headers, body: form });
if (!response.ok) {
throw new Error(`${response.status} ${await response.text()}`);
}

const result = await response.json();
console.log(result.content);
}

main();
```

```bash
invoke_url="https://ai.api.nvidia.com/v1/retrieval/nvidia/nemotron-3.5-parse/parse"
image_source="https://assets.ngc.nvidia.com/products/api-catalog/nemoretriever-parse/example_1.jpg"

if [[ $image_source == http* ]]; then
curl -fsSL "$image_source" -o example_1.jpg
document_path="example_1.jpg"
else
document_path="$image_source"
fi

# One rendered page (image/png or image/jpeg) plus optional JSON options, sent as multipart/form-data
curl -X POST "$invoke_url" \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "Accept: application/json" \
-F "document=@${document_path};type=image/jpeg" \
-F 'options={"decoding":{"max_output_tokens":1024}};type=application/json'
```