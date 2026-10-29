---
title: "nemotron-graphic-elements-v1"
publisher: "nvidia"
type: "endpoint"
updated: "2026-03-04T21:39:30.311Z"
description: "Model for object detection, fine-tuned to detect charts, tables, and titles in documents."
canonical: "https://build.nvidia.com/nvidia/nemotron-graphic-elements-v1"
---

# **nemotron-graphic-elements-v1**

## **Description**

nemotron-graphic-elements-v1 is a specialized object detection model designed to identify and extract key elements from charts and graphs. Based on YOLOX (an anchor-free version of YOLO), it detects and localizes graphic elements including titles, axis labels, legends, and data point annotations. While the underlying approach builds upon work from the YOLOX ecosystem, NVIDIA developed its own base model through complete retraining rather than using pre-trained weights.

This model supersedes the [CACHED model](https://build.nvidia.com/university-at-buffalo/cached).

*This model is ready for commercial/non-commercial use.*

## **License and Terms of Use:**

**GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

**You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.**

**Model Developer:** NVIDIA

## **Deployment Geography:**

**Global**

## **Use Case:**

This model is designed for automating extraction of graphic elements in enterprise documents, including:

- Enterprise document extraction, embedding, and indexing
- Augmenting Retrieval Augmented Generation (RAG) workflows with multimodal retrieval
- Data extraction from legacy documents and reports

## **Release Date:**

Build.NVIDIA.com 03/02/2026 via [nemotron-graphic-elements-v1](https://build.nvidia.com/nvidia/nemotron-graphic-elements-v1) <br>

## **Reference(s):**

**References:**

- [YOLOX Repository](https://github.com/Megvii-BaseDetection/YOLOX)
- [YOLOX Paper](https://arxiv.org/abs/2107.08430)

## **Model Architecture:**

**Architecture Type:** YOLOX <br>
**Network Architecture:** DarkNet53 Backbone + FPN decoupled head (one 1x1 convolution + 2 parallel 3x3 convolutions: one for classification and one for bounding box prediction) <br>
**Classes Detected:** chart_title, x_title, y_title, xlabel, ylabel, other, legend_label, legend_title, mark_label, value_label <br>
**Number of Model Parameters:** 5.4e7

### **Input:**

**Input Types:** Image <br>
**Input Formats:** RGB <br>
**Input Parameters:** Two Dimensional (2D) <br>
**Other Input Properties:** Expects an image array (single image or batch). Expected input is a `np.ndarray` image of shape `[Channel, Width, Height]`, or an `np.ndarray` batch of images of shape `[Batch, Channel, Width, Height]`.

### **Output:**

**Output Types:** Structured detections (bounding boxes + labels + confidence) <br>
**Output Format:** Dict / JSON-compatible structure <br>
**Output Parameters:** One Dimensional (1D) <br>
**Other Output Properties:** Outputs detections per input image.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## **Software Integration:**

**Runtime Engines:** TensorRT <br>
**Supported Hardware Microarchitecture Compatibility:** <br>
NVIDIA Ampere <br>
NVIDIA Hopper <br>
NVIDIA Lovelace <br>
**Operating Systems:** Linux

## **Inference**

**Acceleration Engine:** TensorRT <br>
**Test Hardware:** Tested on supported hardware in the compatibility section

## **Model Version(s)**

nemotron-graphic-elements-v1

Short Name: `nemotron-graphic-elements-v1`

## **Training and Evaluation Datasets:**

### **Training Dataset**

**Data Modality:** Image <br>
**Training Data Collection:** Hybrid (Automated + Human) <br>
**Training Labeling:** Hybrid (Automated + Human) <br>
**Training Properties:** Trained using a mixture of real-world chart images and pseudo-labeled charts, including:

- **PubMed Central (PMC) Chart Dataset** ([link](https://chartinfo.github.io/index_2022.html)): A real-world dataset collected from PubMed Central documents and manually annotated (ICPR 2022 CHART-Infographic competition). Includes 5,614 images for chart element detection, 4,293 images for plot detection/data extraction, and 22,924 images for chart classification.
- **DeepRule dataset** ([link](https://github.com/soap117/DeepRule)): A large dataset of chart images crawled from public Excel sheets with text overwritten to protect privacy. Relevant classes were pseudo-labeled using the CACHED model; training used a subsample of 9,091 charts where a title was detected, alongside the PMC training images.

### **Evaluation Dataset**

**Evaluation Data Collection:** Hybrid (Automated + Human) <br>
**Evaluation Labeling:** Hybrid (Automated + Human) <br>
**Evaluation Properties:** Evaluated using the PMC Chart dataset. Mean Average Precision (mAP) was used as the evaluation metric. The validation dataset is the same as the PMC Chart dataset. <br><br>
**Number of bounding boxes and images per class:**

| Label | Images | Boxes |
|:--|--:|--:|
| chart_title | 38 | 38 |
| legend_label | 318 | 1077 |
| legend_title | 17 | 19 |
| mark_label | 42 | 219 |
| other | 113 | 464 |
| value_label | 52 | 726 |
| x_title | 404 | 437 |
| xlabel | 553 | 4091 |
| y_title | 502 | 505 |
| ylabel | 534 | 3944 |
| Total | 560 | 11520 |

**Per-class Performance Metrics**

**Average Precision (AP)**

| Class | AP | Class | AP | Class | AP |
|:--|--:|:--|--:|:--|--:|
| chart_title | 82.38 | x_title | 88.77 | y_title | 89.48 |
| xlabel | 85.04 | ylabel | 86.22 | other | 55.14 |
| legend_label | 84.09 | legend_title | 60.61 | mark_label | 49.31 |
| value_label | 62.66 |  |  |  |  |

**Average Recall (AR)**

| Class | AR | Class | AR | Class | AR |
|:--|--:|:--|--:|:--|--:|
| chart_title | 93.16 | x_title | 92.31 | y_title | 92.32 |
| xlabel | 88.93 | ylabel | 89.40 | other | 79.48 |
| legend_label | 88.07 | legend_title | 68.42 | mark_label | 73.61 |
| value_label | 68.32 |  |  |  |  |

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## **Ethical Considerations**

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case, and address unforeseen product misuse.

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
| Intended Application & Domain: | Object Detection |
| Model Type: | YOLOX-architecture for detection of graphic elements within images of charts. |
| Intended User: | Enterprise developers, data scientists, and other technical users who need to extract textual elements from charts and graphs. |
| Output: | A List of dictionaries containing lists of dictionaries of floating point numbers (representing bounding box information). <br> **Example**: `{\"data\": [{\"index\": 0,\"bounding_boxes\": {\"table\": [{\"x_min\": 0.6503,\"y_min\": 0.2161,\"x_max\": 0.7835,\"y_max\": 0.3236,\"confidence\": 0.9306}]}}]}` |
| Describe how the model works: | Finds and identifies objects in images by first dividing the image into a grid. For each section of the grid, the model uses a series of neural networks to extract visual features and simultaneously predict what objects are present (in this case "chart title" or "axis label" etc.) and exactly where they are located in that section, all in a single pass through the image. |
| Performance Metrics: | Accuracy, Throughput, and Latency |
| Potential Known Risks: | This model will not always detect all graphic elements in an image, especially for uncommon elements or lower quality images. |
| Licensing & Terms of Use: | **GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |
| Technical Limitations | The model may correctly detect graphic elements of charts, espectially on uncommon chart styles or lower quality images. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Not Applicable |
| Verified to have met prescribed NVIDIA quality standards: | Yes |

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
| Model Application(s): | Object Detection for Retrieval, focused on Enterprise |
| Describe the life critical impact (if present). | Not Applicable |
| Use Case Restrictions: | **GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |

## Prototype

```python
import requests, base64

invoke_url = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-graphic-elements-v1"

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

const invokeUrl = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-graphic-elements-v1";

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

curl https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-graphic-elements-v1 \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "Content-Type: application/json" \
-H "$accept_header" \
-d @payload.json
```