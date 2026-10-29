---
title: "nemotron-table-structure-v1"
publisher: "nvidia"
type: "endpoint"
updated: "2026-03-04T21:40:22.023Z"
description: "Model for object detection, fine-tuned to detect charts, tables, and titles in documents."
canonical: "https://build.nvidia.com/nvidia/nemotron-table-structure-v1"
---

## Model Overview

### Description

The **Nemotron Table Structure v1** model is a specialized object detection model designed to identify and extract the structure of tables in images. Based on YOLOX, an anchor-free version of YOLO (You Only Look Once), this model combines a simpler architecture with enhanced performance. While the underlying technology builds upon work from [Megvii Technology](https://github.com/Megvii-BaseDetection/YOLOX), we developed our own base model through complete retraining rather than using pre-trained weights.

The model excels at detecting and localizing the fundamental structural elements within tables. Through careful fine-tuning, it can accurately identify and delineate three key components within tables:

1. Individual cells (including merged cells)
2. Rows
3. Columns

This specialized focus on table structure enables precise decomposition of complex tables into their constituent parts, forming the foundation for downstream retrieval tasks. This model helps convert tables into the markdown format which can improve retrieval accuracy.

This model is ready for commercial or non-commercial use.

The [Nemotron Table Structure v1 Preview API](https://build.nvidia.com/nvidia/nemotron-table-structure-v1) provides hosted inference for images of cropped tables.

### License/Terms of use

**GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

### Model Architecture

**Architecture Type**: YOLOX <br>
**Network Architecture**: DarkNet53 Backbone \+ FPN Decoupled head (one 1x1 convolution \+ 2 parallel 3x3 convolutions (one for the classification and one for the bounding box prediction). The YOLOX architecture is a single-stage object detector that improves on Yolo-v3. <br>
**Deployment Geography**: Global <br>

**Use Case**: <br>
This model specializes in analyzing images containing tables by:
- Detecting and extracting table structure elements (rows, columns, and cells)
- Providing precise location information for each detected element
- Supporting downstream tasks like table analysis and data extraction

The model is designed to work in conjunction with OCR (Optical Character Recognition) systems to:
1. Identify the structural layout of tables
2. Preserve the relationships between table elements
3. Enable accurate extraction of tabular data from images

Ideal for:
- Document processing systems
- Automated data extraction pipelines
- Digital content management solutions
- Business intelligence applications

**Release Date**
**Build.NVIDIA.com:** 10/01/2026 via [link](https://build.nvidia.com/nvidia/nemotron-table-structure-v1) <br>
**Hugging Face:** 10/23/2025 via [link](https://huggingface.co/nvidia/nemotron-table-structure-v1)

## Technical Details

### Input

**Input Types:** Image <br>
**Input Format:** Base64-encoded PNG or JPEG image of a cropped table, supplied as a data URL in the input array; Red, Green, Blue (RGB) <br>
**Input Parameters:** Two-Dimensional (2D) <br>
**Other Properties Related to Input:** Image size resized to `(1024, 1024)`

### Output

**Output Type(s)**: Structured table detections <br>
**Output Format**: JSON-compatible table detections containing bounding boxes, class labels, and confidence scores <br>
**Output Parameters**: 1D <br>
**Other Properties Related to Output**: Bounding boxes are normalized to `[0, 1]`; object classes are cell, row, and column. `confidence_threshold` defaults to `0.01`, and `nms_threshold` defaults to `0.25` for table structure.

### Software Integration

**Runtime**: NVIDIA hosted Preview API <br>
**API Endpoint**: `https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-table-structure-v1` <br>
**Supported Hardware Microarchitecture Compatibility**: NVIDIA Ampere, NVIDIA Blackwell, NVIDIA Hopper, NVIDIA Lovelace

## Model Version(s):

* `nemotron-table-structure-v1` (Preview release `2.0-preview`; model artifact `nemotron-table-structure-v1:2.0.1`)

## Training Dataset & Evaluation

### Training Dataset

**Data collection method by dataset**: Automated <br>
**Labeling method by dataset**: Automated <br>
**Pretraining**: [COCO train2017](https://cocodataset.org/#download)
**Finetuning (by NVIDIA)**: 23,977 images from [Digital Corpora dataset](https://digitalcorpora.org/), with annotations from [Azure AI Document Intelligence](https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence).
Number of bounding boxes per class: 1,828,978 cells, 134,089 columns and 316,901 rows. The layout model of Document Intelligence was used with `2024-02-29-preview` API version.

### Evaluation Results

**The primary evaluation set**: 2,459 digital corpora images with Azure labels. Number of bounding boxes per class: 200,840 cells, 13,670 columns and 34,575 rows. mAP was used as an evaluation metric. <br>
**Data collection method by dataset**: Hybrid: Automated, Human <br>
**Labeling method by dataset**: Hybrid: Automated, Human <br>
**Properties**: We evaluated with Azure labels from manually selected pages, as well as manual inspection on public PDFs and powerpoint slides.

**Per-class Performance Metrics**:
| Class  | Average Precision (%) | Average Recall (%) |
|:-------|:----------------------|:------------------|
| cell   | 58.365                | 60.647            |
| row    | 76.992                | 81.115            |
| column | 85.293                | 87.434            |

## Inference:

**Acceleration Engine:** YOLOX engine using cuDNN fused operations, custom CUDA kernels, and CUDA graphs <br>
**Test Hardware:**

- NVIDIA Ampere (A100)
- NVIDIA Ampere (A10G)
- NVIDIA Blackwell (B200)
- NVIDIA Blackwell (GB200)
- NVIDIA Blackwell (GB10)
- NVIDIA Blackwell (RTX PRO 6000)
- NVIDIA Hopper (H100)
- NVIDIA Hopper (H200)
- NVIDIA Lovelace (L40S)

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

| Field | Response |
| ----- | ----- |
| Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing | None |
| Measures taken to mitigate against unwanted bias | None |

## Explainability

| Field | Response |
| ----- | ----- |
| Intended Application & Domain: | Object Detection |
| Model Type: | YOLOX-architecture for detection of table structure within images of tables. |
| Intended User: | Enterprise developers, data scientists, and other technical users who need to extract table structure from images. |
| Output: | After post-processing, the output is three numpy array that contains the detections: `boxes [N x 4]` (format is normalized `(x_min, y_min, x_max, y_max)`), associated classes: `labels [N]` and confidence scores: `scores [N]`.|
| Describe how the model works: | Finds and identifies objects in images by first dividing the image into a grid. For each section of the grid, the model uses a series of neural networks to extract visual features and simultaneously predict what objects are present (in this case "cell", "row", or "column") and exactly where they are located in that section, all in a single pass through the image. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Not Applicable |
| Technical Limitations & Mitigation: | The model may not generalize to unknown table formats. Further fine-tuning might be required for such documents. Furthermore, it is not robust to rotated tables. |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics: | Mean Average Precision, detectionr recall and visual inspection |
| Potential Known Risks: | This model may not always detect all elements in a document. |
| Licensing & Terms of Use: | **GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |

## Privacy

| Field | Response |
| ----- | ----- |
| Generatable or reverse engineerable personal data? | No |
| Personal data used to create this model? | None |
| How often is the dataset reviewed? | Before Every Release |
| Is a mechanism in place to honor data subject right of access or deletion of personal data? | No |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Applicable Privacy Policy | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/ |

## Safety & Security

| Field | Response |
| ----- | ----- |
| Model Application Field(s): | Object Detection for Retrieval, focused on Enterprise |
| Describe the life critical impact (if present). | Not Applicable |
| Use Case Restrictions: | **GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |

## Prototype

```python
import requests, base64

invoke_url = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-table-structure-v1"

with open("yolox1.png", "rb") as f:
image_b64 = base64.b64encode(f.read()).decode()

assert len(image_b64) < 180_000, \
"To upload larger images, use the assets API (see docs)"

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json"
}

payload = {
"input": [
{
"type": "image_url",
"url": f"data:image/png;base64,{image_b64}"
}
]
}

response = requests.post(invoke_url, headers=headers, json=payload)

print(response.json())
```

```javascript
import axios from 'axios';
import { readFile } from 'node:fs/promises';

const invokeUrl = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-table-structure-v1";

const headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json"
};

readFile("yolox1.png")
.then(data => {
const imageB64 = Buffer.from(data).toString('base64');
if (imageB64.length > 180_000) {
throw new Error("To upload larger images, use the assets API (see docs)");
}

const payload = {
"input": [
{
"type": "image_url",
"url": `data:image/png;base64,${imageB64}`
}
]
};

return axios.post(invokeUrl, payload, { headers: headers, responseType: 'json' });
})
.then(response => {
console.log(JSON.stringify(response.data));
})
.catch(error => {
console.error(error);
});
```

```bash
image_b64=$( base64 -i yolox1.png )

accept_header='Accept: application/json'

# Construct the JSON payload
echo '{
"input": [
{
"type": "image_url",
"url": "data:image/png;base64,'"${image_b64}"'"
}
]
}' > payload.json

curl https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-table-structure-v1 \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "Content-Type: application/json" \
-H "$accept_header" \
-d @payload.json
```