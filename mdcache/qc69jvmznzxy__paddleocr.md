---
title: "paddleocr"
publisher: "baidu"
type: "endpoint"
updated: "2025-07-09T15:04:55.570Z"
description: "Model for table extraction that receives an image as input, runs OCR on the image, and returns the text within the image and its bounding boxes."
canonical: "https://build.nvidia.com/baidu/paddleocr"
---

## Model Overview

### Description

PaddleOCR is an ultra-lightweight Optical Character Recognition (OCR) system developed by Baidu. It supports a variety of cutting-edge OCR algorithms and provides value at every stage of the AI pipeline, including data generation, model training, and inference.

This model is ready for commercial use.

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to Non-NVIDIA [PaddleOCR Toolkit](https://github.com/PaddlePaddle/PaddleOCR).

### Terms of use
PaddleOCR is licensed under  [Apache-2](https://www.apache.org/licenses/LICENSE-2.0).
**You are responsible for ensuring that your use of models complies with all applicable laws.**

### References
[Github](https://github.com/PaddlePaddle/PaddleOCR/blob/main/README_en.md)
[Arxiv](https://arxiv.org/abs/2206.03001)

## Model Architecture
**Architecture Type for Text Detector:** CNN <br>
**Network Architecture for Text Detector:**  LK-PAN

**Architecture Type for Text Recognition:** Hybrid Transformer CNN  <br>
**Network Architecture for Text Recognition:** SVTR-LCNet (NRTR Head and CTCLoss head) <br>

## Input
**Input Type(s):** Image <br>
**Input Format(s):** Red, Green, Blue (RGB) <br>
**Input Parameters:** Two Dimensional (2D) <br>
**Other Properties Related to Input:** nd array, or batch of nd arrays are passed in with shape [Batch, Channel, Width, Height]. PaddleOCR does some internal thresholding, but none was implemented from our side. <br>

## Output
**Output Type(s):** Text <br>
**Output Format:**  String <br>
**Output Parameters:** 1D <br>
**Other Properties Related to Output:** Batch of text strings. <br>

**Supported Hardware Microarchitecture Compatibility:** NVIDIA Ampere, NVIDIA Hopper, NVIDIA Lovelace<br>

## Supported Operating System(s):
* Linux <br>

## Model Version(s):
* baidu/paddleocr  <br>

## Training Dataset:

**Link:**  <br>

Text detection datasets include LSVT (Sun et al. 2019), RCTW-17 (Shiet al. 2017), MTWI 2018 (He and Yang 2018), CASIA-10K (He et al. 2018), SROIE (Huang et al. 2019), MLT 2019 (Nayef et al. 2019), BDI (Karatzas et al. 2011), MSRATD500 (Yao et al. 2012) and CCPD 2019 (Xu et al. 2018).

These are two of the datasets (among others) which are used for text recognition:
[OpenImages](https://github.com/openimages/dataset) <br>
[InvoiceDatasets](https://github.com/FuxiJia/InvoiceDatasets)

**Data Collection Method by dataset:** Unknown <br>
**Labeling Method by dataset** Unknown <br>

Text Detection: 127k training images (68K real scene images from Baidu image search and public datasets and 59K synthetic images)

Text Recognition: 18.5M training images (7M real scene images from Baidu image search and public datasets and 11.5M synthetic images)

## Inference:
**Engine:** Tensor(RT) <br>
**Test Hardware:** Tested on all supported hardware listed in compatibility section <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Prototype

```python
import requests, base64

invoke_url = "https://ai.api.nvidia.com/v1/cv/baidu/paddleocr"

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

const invokeUrl = "https://ai.api.nvidia.com/v1/cv/baidu/paddleocr";

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

curl https://ai.api.nvidia.com/v1/cv/baidu/paddleocr \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "Content-Type: application/json" \
-H "$accept_header" \
-d @payload.json
```