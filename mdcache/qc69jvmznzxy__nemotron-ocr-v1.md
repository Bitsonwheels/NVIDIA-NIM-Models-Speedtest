---
title: "nemotron-ocr-v1"
publisher: "nvidia"
type: "endpoint"
updated: "2026-03-12T18:07:08.119Z"
description: "Powerful OCR model for fast, accurate real-world image text extraction, layout, and structure analysis."
canonical: "https://build.nvidia.com/nvidia/nemotron-ocr-v1"
---

# **nemotron-ocr-v1**

## **Description**

nemotron-ocr-v1 is a text recognition model designed for robust end-to-end optical character recognition (OCR) on complex real-world images and documents. It integrates three core neural network modules: a detector for text region localization, a recognizer for transcription of detected regions, and a relational model for layout and reading-order analysis.

This model is optimized for a wide variety of OCR tasks, including multi-line, multi-block, and natural scene text, and supports advanced reading order analysis via its relational model component. It is production-ready with a focus on speed and accuracy on both document and natural scene images.

*This model is ready for commercial/non-commercial use.*

## **License and Terms of Use:**

**GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

**You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.**

**Model Developer:** NVIDIA

## **Deployment Geography:**

**Global**

## **Use Case:**

This model is designed for high-accuracy and high-speed OCR to support multimodal retrieval systems, RAG pipelines, and document intelligence applications that require extraction of text and structure from images and scanned documents.

## **Release Date:**

Build.NVIDIA.com 03/02/2026 via [nemotron-ocr-v1](https://build.nvidia.com/nvidia/nemotron-ocr-v1) <br>

## **Reference(s):**

**References:**

- [NVIDIA NIM Documentation](https://docs.nvidia.com/nim/)

## **Model Architecture:**

**Architecture Type:** Hybrid detector–recognizer with document-level relational modeling <br>
The model integrates three specialized neural components:

- **Text Detector:** Utilizes a RegNetY-8GF convolutional backbone for high-accuracy localization of text regions within images.
- **Text Recognizer:** Employs a Transformer-based sequence recognizer to transcribe text from detected regions, supporting variable word and line lengths.
- **Relational Model:** Applies a multi-layer global relational module to predict logical groupings, reading order, and layout relationships across detected text elements.

All components are trained jointly in an end-to-end fashion, providing robust, scalable OCR for diverse document and scene images.

**Parameter Counts:**

| Component | Parameters |
|:--|--:|
| Detector | 45,268,472 |
| Recognizer | 4,944,346 |
| Relational model | 2,254,422 |
| **Total** | 52,467,240 |

### **Input:**

| Property | Value |
|:--|:--|
| Input Type & Format | Image (RGB, PNG/JPEG, float32/uint8), aggregation level (word, sentence, or paragraph) |
| Input Parameters | 3 x H x W (single image) or B x 3 x H x W (batch) |
| Input Range | [0, 1] (float32) or [0, 255] (uint8, auto-converted) |
| Other Properties | Handles both single images and batches. Automatic multi-scale resizing for best accuracy. |

### **Output:**

| Property | Value |
|:--|:--|
| Output Type | Structured OCR results: a list of detected text regions (bounding boxes), recognized text, and confidence scores |
| Output Format | Bounding boxes: tuple of floats, recognized text: string, confidence score: float |
| Output Parameters | Bounding boxes: 1D list of bounding box coordinates, recognized text: 1D list of strings, confidence score: 1D list of floats |
| Other Properties | Please see the sample output for an example of the model output. |

### **Sample output**

```
ocr_boxes = [[[15.552736282348633, 43.141815185546875],
[150.00149536132812, 43.141815185546875],
[150.00149536132812, 56.845645904541016],
[15.552736282348633, 56.845645904541016]],
[[298.3145751953125, 44.43315124511719],
[356.93585205078125, 44.43315124511719],
[356.93585205078125, 57.34814453125],
[298.3145751953125, 57.34814453125]],
[[15.44686508178711, 13.67985725402832],
[233.15859985351562, 13.67985725402832],
[233.15859985351562, 27.376562118530273],
[15.44686508178711, 27.376562118530273]],
[[298.51727294921875, 14.268900871276855],
[356.9850769042969, 14.268900871276855],
[356.9850769042969, 27.790447235107422],
[298.51727294921875, 27.790447235107422]]]

ocr_txts = ['The previous notice was dated',
'22 April 2016',
'The previous notice was given to the company on',
'22 April 2016']

ocr_confs = [0.97730815, 0.98834222, 0.96804602, 0.98499225]
```

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## **Software Integration:**

**Runtime Engines:** TensorRT <br>
**Supported Hardware Microarchitecture Compatibility:** <br>
NVIDIA Ampere <br>
NVIDIA Blackwell <br>
NVIDIA Hopper <br>
NVIDIA Lovelace <br>
**Operating Systems:** Linux

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## **Model Version(s)**

nemotron-ocr-v1

Short Name: `nemotron-ocr-v1`

## **Training and Evaluation Datasets:**

### **Training Dataset**

**Data Modality:** Image <br>
**Training Data Collection:** Hybrid (Automated, Human, Synthetic) <br>
**Training Labeling:** Hybrid (Automated, Human, Synthetic) <br>
**Training Properties:** Trained on a large-scale, curated mix of public and proprietary OCR datasets, focusing on high diversity of document layouts and natural scene images. The training set includes synthetic and real images with varied noise and backgrounds, filtered for commercial use eligibility. Includes scanned documents, natural scene images, receipts, and business documents.

### **Evaluation Dataset**

**Evaluation Data Collection:** Hybrid (Automated, Human, Synthetic) <br>
**Evaluation Labeling:** Hybrid (Automated, Human, Synthetic) <br>
**Evaluation Properties:** Evaluated on several NVIDIA internal datasets for pure OCR, table content extraction, and document retrieval. Benchmarks include challenging scene images, documents with varied layouts, and multi-language data.

### **Evaluation Results**

Benchmarked against PaddleOCR on internal evaluation datasets across OCR (Character Error Rate), table extraction (TEDS), and document retrieval (Recall@5).

| Metric | nemotron-ocr-v1 | PaddleOCR | Net change |
|:--|--:|--:|:--|
| Character Error Rate | 0.1633 | 0.2029 | -19.5% ✔️ |
| Bag-of-character Error Rate | 0.0453 | 0.0512 | -11.5% ✔️ |
| Bag-of-word Error Rate | 0.1203 | 0.2748 | -56.2% ✔️ |
| Table Extraction TEDS | 0.781 | 0.781 | 0.0% ⚖️ |
| Public Earnings Multimodal Recall@5 | 0.779 | 0.775 | +0.5% ✔️ |
| Digital Corpora Multimodal Recall@5 | 0.901 | 0.883 | +2.0% ✔️ |

### **Detailed Performance Analysis**

The model demonstrates robust performance on complex layouts, noisy backgrounds, and challenging real-world scenes. Reading order and block detection are powered by the relational module, supporting downstream applications such as chart-to-text, table-to-text, and infographic-to-text extraction.

## **Inference**

**Acceleration Engine:** TensorRT, PyTorch <br>
**Test Hardware:** H100 PCIe/SXM, A100 PCIe/SXM, L40s, L4, A10G

## **Ethical Considerations**

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case, and address unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Bias

| Field | Response |
| ----- | ----- |
| Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing | None |
| Measures taken to mitigate against unwanted bias | None |

## Explainability

| Field | Response |
| ----- | ----- |
| Intended Application & Domain: | Optical Character Recognition (OCR) with a focus on retrieval application and documents. |
| Model Type: | Hybrid neural network with convolutional detector, transformer recognizer, and document structure modeling. |
| Intended User: | Developers and teams building AI-driven search, RAG, multimodal agents, or document intelligence applications. Ideal for those working with large collections of scanned or photographed documents, including PDFs, forms, and reports. |
| Output: | Structured OCR results, including detected bounding boxes, recognized text, and confidence scores. |
| Describe how the model works: | The model first detects text regions in the image, then transcribes recognized text, and finally analyzes document structure and reading order. Outputs structured, machine-readable results suitable for downstream search and analysis. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | N/A |
| Technical Limitations: | This model version supports English only. |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics: | Accuracy (e.g., character error rate), throughput, and latency. |
| Potential Known Risks: | The model may not always extract or transcribe all text with perfect accuracy, particularly in cases of poor image quality or highly stylized fonts. |
| Licensing & Terms of Use: | **GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |

## Privacy

| Field | Response |
| ----- | ----- |
| Generatable or reverse engineerable personal data? | None |
| Personal data used to create this model? | None |
| How often is dataset reviewed? | Dataset is initially reviewed upon addition, and subsequent reviews are conducted as needed or upon request for changes. |
| Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model? | No |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | No, not possible with externally-sourced data. |
| Applicable Privacy Policy | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/ |

## Safety & Security

| Field | Response |
| ----- | ----- |
| Model Application(s): | Text recognition and structured OCR for multimodal retrieval. Inputs can include natural scene images, scanned documents, charts, tables, and infographics. |
| Use Case Restrictions: | **GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |
| Model and dataset restrictions: | The principle of least privilege (PoLP) is applied, limiting access for dataset generation and model development. Restrictions enforce dataset access only during training, and all dataset license constraints are adhered to. |
| Describe the life critical impact (if present): | Not applicable. |

## Prototype

```python
import requests, base64

invoke_url = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-ocr-v1"

with open("paddleocr1.png", "rb") as f:
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

const invokeUrl = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-ocr-v1";

const headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json"
};

readFile("paddleocr1.png")
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
image_b64=$( base64 -i paddleocr1.png )

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

curl https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-ocr-v1 \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "Content-Type: application/json" \
-H "$accept_header" \
-d @payload.json
```