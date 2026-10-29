---
title: "nemoguard-jailbreak-detect"
publisher: "nvidia"
type: "endpoint"
updated: "2025-07-02T15:21:58.541Z"
description: "Industry leading jailbreak classification model for protection from adversarial attempts"
canonical: "https://build.nvidia.com/nvidia/nemoguard-jailbreak-detect"
---

# Model Overview

## Description:

This open Nemotron safety model, *NemoGuard JailbreakDetect*, was developed to detect attempts to jailbreak large language models.
This model is ready for commercial use.<br>

This model is supported in the open NVIDIA NeMo Guardrails library, designed to simplify scalable AI guardrail orchestration for safeguarding agentic AI applications.

### License/Terms of Use:

[NVIDIA Open Model License](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf)

## Reference(s):

[Improved Large Language Model Jailbreak Detection via Pretrained Embeddings](https://arxiv.org/abs/2412.01547)

## Model Architecture:

**Architecture Type:** Random Forest <br>
**Network Architecture:** N/A <br>

## Input:

**Input Type(s):** Text Embedding <br>
**Input Parameters:** 768 dimensional vector <br>
**Input Format(s):** Vector <br>
**Other Properties Related to Input:** Must be an output from the corresponding embedding model. Either [`nv-embedqa-e5-v5`](https://build.nvidia.com/nvidia/nv-embedqa-e5-v5) or [`snowflake-arctic-m-long`](https://huggingface.co/Snowflake/snowflake-arctic-embed-m-long). <br>

## Output:

**Output Type(s):** Classification, Probability <br>
**Output Format:** Bool, Float <br>
**Output Parameters:** 1D <br>
**Other Properties Related to Output:** N/A <br>

## Software Integration:

**Runtime Engine(s):**

- Not Applicable (N/A) <br>

**Supported Hardware Microarchitecture Compatibility:** <br>

- x86
- x64

**[Preferred/Supported] Operating System(s):** <br>

- Windows
- MacOS
- Linux

## Model Version(s):

NemoGuard-JailbreakDetect-v1.0: Jailbreak detection model using Snowflake-arctic-embed-m embeddings<br>

# Training, Testing, and Evaluation Datasets:

## Training Dataset:

A combination of three open datasets, mixed together, de-duplicated, and reviewed for data quality.
Jailbreak data was augmented with the use of [garak](https://github.com/NVIDIA/garak).
The datasets used are outlined below:

### Advbench

**Link:** https://github.com/thunlp/Advbench <br>
**Data Collection Method by dataset** <br>

- [Automated] <br>

**Labeling Method by dataset**<br>

- [Automated] <br>

**Properties:**  
520 entries, all comprised of jailbreak attempts. <br>

### Wildjailbreak

**Link:** https://huggingface.co/datasets/allenai/wildjailbreak <br>
**Data Collection Method by dataset**<br>

- Hybrid: Automated, Synthetic <br>

**Labeling Method by dataset**<br>

- [Automated] <br>

**Properties:**  
6387 total entries: 5721 benign prompts, 666 jailbreak attempts <br>

### jackhao/jailbreak-classification

**Link:** https://huggingface.co/datasets/jackhhao/jailbreak-classification <br>
**Data Collection Method by dataset**<br>

- [Automated] <br>

**Labeling Method by dataset**<br>

- [Automated] <br>

**Properties:**  
1306 total entries: 640 benign prompts, 666 jailbreak attempts <br>

## Testing Dataset:

A stratified subset (20%) of the aggregate dataset was used for testing.

## Evaluation Dataset:

Evaluated on [JailbreakHub](https://huggingface.co/datasets/walledai/JailbreakHub).
| Model | F1 Score | False Positive Rate | False Negative Rate |
|:----------------------------:|:--------:|:-------------------:|:-------------------:|
| NemoGuard JailbreakDetect | 0.9601 | 0.0042 | 0.0435 |

## Inference:

**Engine:** N/A <br>
**Test Hardware:** <br>

- RTX A6000 <br>
- A100

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility, and we have established policies and practices to enable development for a wide array of AI applications.  
When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.
Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Bias

| Field | Response |
| ----- | ----- |
| Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing | None |
| Measures taken to mitigate against unwanted bias | None |

## Explainability

| Field                                           | Response                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Intended Users:                                 | This model is intended for developers and deployers of LLM-powered applications who wish to protect the application from the effects of LLM jailbreaking.                                                                                                                                                                                             |
| Output(s):                                      | A binary label for whether the prompt constitutes a jailbreak and a score indicating the confidence of the classification.                                                                                                                                                                                                                            |
| List the steps explaining how this model works: | The model takes in a text embedding from a pre-specified embedder and uses a random forest to return a label and confidence score concerning whether or not the input is a jailbreak attempt.                                                                                                                                                         |
| Technical Limitations:                          | The model performs well against many current public jailbreak attacks but experiences both false positives (detections on benign input) and false negatives (failure to detect malicious input) on less than 1% of evaluated examples. This model was validated against English language prompts, and may perform differently under different inputs. |
| Performance Metrics:                            | F1 score, False Positive Rate, False Negative Rate                                                                                                                                                                                                                                                                                                    |
| Potential Known Risks:                          | The model may fail to detect jailbreaking attempts, or may generate a false positive (detections on benign input)                                                                                                                                                                                                                                     |
| Licensing:                                      | [NVIDIA Open Model License Agreement](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf)                                                                                                                                                                                                               |

## Privacy

| Field                                                                                                                             | Response                                       |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| Generatable or reverse engineerable personally-identifiable information (PII)?                                                    | None                                           |
| How often is dataset reviewed?                                                                                                    | Before Release                                 |
| Is a mechanism in place to honor data subject right of access or deletion of personal data?                                       | Not Applicable                                 |
| If PII collected for the development of the model, was it collected directly by NVIDIA?                                           | Not Applicable                                 |
| If PII collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects? | Not Applicable                                 |
| If PII collected for the development of this AI model, was it minimized to only what was required?                                | Not Applicable                                 |
| Is data in dataset traceable?                                                                                                     | Yes                                            |
| Are we able to identify and trace source of dataset?                                                                              | Yes                                            |
| Does data labeling (annotation, metadata) comply with privacy laws?                                                               | Yes                                            |
| Is data compliant with data subject requests for data correction or removal, if such a request was made?                          | No, not possible with externally-sourced data. |

## Safety & Security

| Field                                             | Response                                                                                                                                                                                                         |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model Application(s):                             | LLM jailbreak detection                                                                                                                                                                                          |
| Describe the physical safety impact (if present). | Not Applicable                                                                                                                                                                                                   |
| Use Case Restrictions:                            | Abide by NVIDIA Open Model License Agreement                                                                                                                                                                     |
| Explicit model and dataset restrictions:          | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to |

## Prototype

```bash
invoke_url='https://ai.api.nvidia.com/v1/security/nvidia/nemoguard-jailbreak-detect'

authorization_header='Authorization: Bearer '
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data=$'{
"messages": [
{
"role": "user",
"content": ""
}
]
}'

response=$(curl --silent -i -w "\n%{http_code}" --request POST \
--url "$invoke_url" \
--header "$authorization_header" \
--header "$accept_header" \
--header "$content_type_header" \
--data "$data"
)

echo "$response"
```

```python
import requests
invoke_url = "https://ai.api.nvidia.com/v1/security/nvidia/nemoguard-jailbreak-detect"

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json"
}

payload = {
"input": ""
}

response = requests.post(invoke_url, headers=headers, json=payload)

print(response.json())
```

```javascript
import axios from 'axios';

const invokeUrl = "https://ai.api.nvidia.com/v1/security/nvidia/nemoguard-jailbreak-detect";

const headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json"
};

const payload = {
"input": ""
};

axios.post(invokeUrl, payload, { headers: headers, responseType: 'json' })
.then(response => {
console.log(JSON.stringify(response.data)); // Log the response data
})
.catch(error => {
console.error("Error occurred:", error.message); // Log error message
});
```