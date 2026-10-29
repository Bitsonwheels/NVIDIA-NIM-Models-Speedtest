---
title: "nemotron-page-elements-v3"
publisher: "nvidia"
type: "endpoint"
updated: "2026-03-04T21:39:31.777Z"
description: "Model for object detection, fine-tuned to detect charts, tables, and titles in documents."
canonical: "https://build.nvidia.com/nvidia/nemotron-page-elements-v3"
---

# **nemotron-page-elements-v3**

## **Description**

nemotron-page-elements-v3 is a specialized object detection model designed to identify and extract key page elements in documents, including tables, charts, infographics, titles, header/footers, and text regions. It supports document analysis and multimodal extraction workflows used in enterprise document understanding and retrieval.

The WCE Preview API provides hosted inference for page images.

*This model is ready for commercial or non-commercial use.*

## **License and Terms of Use:**

**GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

**You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.**

**Model Developer:** NVIDIA

## **Deployment Geography:**

**Global**

## **Use Case:**

This model is designed for automating extraction of page elements in enterprise documents, including:

- Enterprise document extraction, embedding, and indexing
- Augmenting Retrieval Augmented Generation (RAG) workflows with multimodal retrieval
- Data extraction from legacy documents and reports

This model supersedes the [nemoretriever-page-elements-v2 model](https://build.nvidia.com/nvidia/nemoretriever-page-elements-v2).

## **Release Date:**

**Build.NVIDIA.com:** 10/01/2026 via [nemotron-page-elements-v3](https://build.nvidia.com/nvidia/nemotron-page-elements-v3) <br>

## **Reference(s):**

**References:**

- [YOLOX Paper](https://arxiv.org/abs/2107.08430)
- [YOLOX Repository](https://github.com/Megvii-BaseDetection/YOLOX)
- [Approaches to PDF Data Extraction for Information Retrieval](https://developer.nvidia.com/blog/approaches-to-pdf-data-extraction-for-information-retrieval/)

## **Model Architecture:**

**Architecture Type:** YOLOX <br>
**Network Architecture:** DarkNet53 Backbone + FPN decoupled head (one 1x1 convolution + 2 parallel 3x3 convolutions: one for classification and one for bounding box prediction) <br>
**Number of Model Parameters:** ~5.4e7 <br>
**Input Resize:** (1024, 1024)

### **Input:**

**Input Types:** Image <br>
**Input Formats:** RGB <br>
**Input Parameters:** Two-Dimensional (2D) <br>
**Other Input Properties:** Supply a base64-encoded PNG or JPEG page image as a data URL in the API input array. The image is resized to (1024, 1024).

### **Output:**

**Output Types:** Structured detections (bounding boxes + labels + confidence) <br>
**Output Format:** JSON-compatible structure <br>
**Output Parameters:** One-Dimensional (1D) <br>
**Other Output Properties:** The API returns normalized [0, 1] bounding boxes, confidence scores, and page-element class labels. `confidence_threshold` defaults to `0.01`; the publishing checklist gives `0.5` as the default `nms_threshold`. <br><br>
**Output Classes:**

* **Table**: Data structured in rows and columns
* **Chart**: Specifically bar charts, line charts, or pie charts
* **Infographic**: Visual representations of information more complex than a chart (diagrams, flowcharts); maps are not considered infographics
* **Title**: Section titles, or table/chart/infographic titles
* **Header/footer**: Page headers and footers
* **Text**: Regions of one or more text paragraphs, or standalone text not belonging to any of the classes above. The WCE API example labels this class `paragraph`.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## **Software Integration:**

**Runtime Engines:**
- **Other:** YOLOX engine using cuDNN fused operations, custom CUDA kernels, and CUDA graphs

**Supported Hardware:**
- **NVIDIA Ampere:** A100, A10G
- **NVIDIA Blackwell:** B200, GB200, GB10, RTX PRO 6000
- **NVIDIA Hopper:** H100, H200
- **NVIDIA Lovelace:** L40S

**Operating Systems:** Linux

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## **Model Version(s)**

nemotron-page-elements-v3 (WCE Preview release `2.0-preview-page-elements-v3`; model artifact `nemotron-page-elements-v3:2.0.1`)

Short Name: `nemotron-page-elements-v3`

## **Training and Evaluation Datasets:**

### **Training Dataset**

**Data Modality:** Image <br>
**Image Training Data Size:** Less than a Million Images <br>
**Training Data Collection:** Automated <br>
**Training Labeling:** Hybrid (Automated, Human) <br>
**Training Properties:** Pretrained on 118,287 images from [COCO train2017](https://cocodataset.org/#download) and fine-tuned on 36,093 images from the [Digital Corpora dataset](https://digitalcorpora.org/), with annotations from [Azure AI Document Intelligence](https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence) and a data annotation team. Bounding boxes per class: 35,328 tables, 44,178 titles, 11,313 charts, 6,500 infographics, 90,812 texts, and 10,743 header/footers. The layout model of Document Intelligence was used with `2024-02-29-preview` API version.

### **Evaluation Dataset**

**Evaluation Data Collection:** Hybrid (Automated, Human) <br>
**Evaluation Labeling:** Hybrid (Automated, Human) <br>
**Evaluation Properties:** The primary evaluation set is a cut of Azure labels and Digital Corpora images. Bounding boxes per class: 1,985 tables, 2,922 titles, 498 charts, 572 infographics, 4,400 texts, and 492 header/footers. Mean Average Precision (mAP) was used as an evaluation metric. We evaluated with Azure labels from manually selected pages, as well as manual inspection on public PDFs and PowerPoint slides. <br><br>
**Per-class Performance Metrics:**

| Class | AP (%) | AR (%) |
|:--|--:|--:|
| table | 44.643 | 62.242 |
| chart | 54.191 | 77.557 |
| title | 38.529 | 56.315 |
| infographic | 66.863 | 69.306 |
| text | 45.418 | 73.017 |
| header_footer | 53.895 | 75.670 |

## **Inference**

**Acceleration Engine:** Other (YOLOX engine using cuDNN fused operations, custom CUDA kernels, and CUDA graphs) <br>
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

## **Ethical Considerations**

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

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
| Intended Task/Domain: | Document Understanding |
| Model Type: | YOLOX Object Detection for Charts, Tables, Infographics, Header/footers, Texts, and Titles |
| Intended User: | Enterprise developers, data scientists, and other technical users who need to extract structural elements from documents. |
| Output: | A List of dictionaries containing lists of dictionaries of floating point numbers (representing bounding box information). <br> **Example**: `{\"data\": [{\"index\": 0,\"bounding_boxes\": {\"table\": [{\"x_min\": 0.6503,\"y_min\": 0.2161,\"x_max\": 0.7835,\"y_max\": 0.3236,\"confidence\": 0.9306}]}}]}` |
| Describe how the model works: | The model identifies objects in an image by first dividing the image into a grid. For each grid cell, it extracts visual features and simultaneously predicts which objects are present (for example, 'chart' or 'table') and where they are located in that cell, all in a single pass through the image. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Not Applicable |
| Technical Limitations & Mitigation: | The model may not generalize to unknown document types/formats not commonly found on the web. Further fine-tuning might be required for such documents. |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics: | Mean Average Precision, detectionr recall and visual inspection |
| Potential Known Risks: | This model may not always detect all elements in a document. |
| Licensing & Terms of Use: | **GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |

## Privacy

| Field | Response |
| ----- | ----- |
| Generatable or reverse engineerable personal data? | No |
| Personal data used to create this model? | No |
| Was consent obtained for any personal data used? | Not Applicable |
| How often is the dataset reviewed? | Before Release |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? |  No, not possible with externally-sourced data. |
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

invoke_url = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-page-elements-v3"

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

const invokeUrl = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-page-elements-v3";

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

curl https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-page-elements-v3 \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "Content-Type: application/json" \
-H "$accept_header" \
-d @payload.json
```