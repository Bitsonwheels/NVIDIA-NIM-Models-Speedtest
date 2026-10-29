---
title: "parakeet-ctc-0.6b-vi"
publisher: "nvidia"
type: "endpoint"
updated: "2025-09-08T15:59:08.704Z"
description: "Accurate and optimized Vietnamese-English transcriptions with punctuation and word timestamps."
canonical: "https://build.nvidia.com/nvidia/parakeet-ctc-0_6b-vi"
---

# Model Overview

RIVA Parakeet-CTC-0.6B-Unified ASR Vietnamese (around 600M parameters) [1] is trained on an ASR dataset with over 4,000 hours of Vietnamese (vi) speech. The model transcribes speech in Vietnamese, in upper case and lower case alphabets, along with punctuations (period, comma, and question mark), and spaces. 

This model is ready for commercial/non-commercial use.

## Terms of use
GOVERNING TERMS: Use of this model is governed by the [NVIDIA Community Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/).

## References
* [Fast Conformer](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#fast-conformer)

## Model Architecture

**Architecture Type:** Parakeet-CTC (also known as FastConformer-CTC) which is an optimized version of Conformer model with 8x depthwise-separable convolutional downsampling with CTC loss. <br>
**Network Architecture:** Parakeet-CTC-0.6B <br>

## Input
**Input Type(s):** Audio in Vietnamese + English <br>
**Input Format(s):** Linear PCM 16-bit 1 channel <br>
**Input Parameters:** One-Dimensional (1D)

## Output
**Output Type(s):** Text String in Vietnamese + English with Timestamps <br>
**Output Format(s):** String
**Output Parameters:** One-Dimensional (1D)

**Supported Operating System(s):**  <br>
* Linux <br>

## Inference
**Engine:** Triton <br>
**Test Hardware:**  <br>
* NVIDIA A2 <br>
* NVIDIA A10 <br>
* NVIDIA A16 <br>
* NVIDIA A30 <br>
* NVIDIA A40 <br>
* NVIDIA A100 <br>
* NVIDIA H100 <br>
* NVIDIA L4 <br>
* NVIDIA L40 <br>
* GeForce RTX 40xx <br>
* GeForce RTX 50xx <br>
* Blackwell RTX 60xx <br>

## Ethical Considerations (For NVIDIA Models Only):
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Bias

| Field Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing: | Response None |
| ----- | ----- |
| Measures taken to mitigate against unwanted bias: | None  |

## Explainability

| Field | Response |
| ----- | ----- |
| Intended Task/Domain: | Speech to text transcription |
| Model Type: | ASR |
| Intended Users: | This model is intended for developers, researchers, academics, and industries building conversational based applications.    |
| Output: | Transcribed text with timestamps and confidence scores |
| Describe how this model works: | The model transcribes audio input into text in the input language. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Age, Gender, National Origin |
| Technical Limitations & Mitigation: | Transcripts may not be 100% accurate. Accuracy varies based on the characteristics of the input audio (domain, use case, accent, noise, speech type, context of speech, etc.). |
| Verified to have met prescribed NVIDIA quality standards: Performance Metrics: | Yes Word Error Rate (WER), Silence Robustness (characters per minute of silent audio), Latency (milliseconds), Throughput (total audio processed per unit of time). |
| Potential Known Risks: | Not recommended for word-for-word transcription as accuracy varies based on the characteristics of the input audio (domain, use case, accent, noise, speech type, and context of speech). |
| Licensing | **GOVERNING TERMS**: Your use of this API is governed by the [NVIDIA API Trial Service Terms of Use](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fassets.ngc.nvidia.com%2Fproducts%2Fapi-catalog%2Flegal%2FNVIDIA%2520API%2520Trial%2520Terms%2520of%2520Service.pdf&data=05%7C02%7Cjaydar%40nvidia.com%7C95bb810010dc4a66c6da08dde4f09e53%7C43083d15727340c1b7db39efd9ccc17a%7C0%7C0%7C638918444317044724%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=vvzmA%2Bo2tdifKPXG%2FGjgN4TPVdoUTsXD4%2BE%2B1M%2F7CWI%3D&reserved=0); and the use of this model is governed by the [NVIDIA Agreements | Enterprise Software | NVIDIA Community Model License](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.nvidia.com%2Fen-us%2Fagreements%2Fenterprise-software%2Fnvidia-community-models-license%2F&data=05%7C02%7Cjaydar%40nvidia.com%7C95bb810010dc4a66c6da08dde4f09e53%7C43083d15727340c1b7db39efd9ccc17a%7C0%7C0%7C638918444317058237%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=c%2B1IgzlTBZaDGUkIFi08wYwzVcmWVYnCCBwztkCBRTI%3D&reserved=0). |

## Privacy

| Field | Response |
| ----- | ----- |
| Generatable or reverse engineerable personal data? | None |
| Personal data used to create this model? | None |
| How often is the dataset reviewed? | Before Release |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | The data is compliant where applicable, but is not applicable for all data. |
| Applicable Privacy Policy | [https://www.nvidia.com/en-us/about-nvidia/privacy-policy/](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/)  |

## Safety & Security

| Field | Response |
| ----- | ----- |
| Model Application Field(s): | Speech to text transcription |
| Describe the life-critical application (if present). | Not Applicable  |
| Use Case Restrictions: | **GOVERNING TERMS**: Your use of this API is governed by the [NVIDIA API Trial Service Terms of Use](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fassets.ngc.nvidia.com%2Fproducts%2Fapi-catalog%2Flegal%2FNVIDIA%2520API%2520Trial%2520Terms%2520of%2520Service.pdf&data=05%7C02%7Cjaydar%40nvidia.com%7C95bb810010dc4a66c6da08dde4f09e53%7C43083d15727340c1b7db39efd9ccc17a%7C0%7C0%7C638918444317044724%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=vvzmA%2Bo2tdifKPXG%2FGjgN4TPVdoUTsXD4%2BE%2B1M%2F7CWI%3D&reserved=0); and the use of this model is governed by the [NVIDIA Agreements | Enterprise Software | NVIDIA Community Model License](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.nvidia.com%2Fen-us%2Fagreements%2Fenterprise-software%2Fnvidia-community-models-license%2F&data=05%7C02%7Cjaydar%40nvidia.com%7C95bb810010dc4a66c6da08dde4f09e53%7C43083d15727340c1b7db39efd9ccc17a%7C0%7C0%7C638918444317058237%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=c%2B1IgzlTBZaDGUkIFi08wYwzVcmWVYnCCBwztkCBRTI%3D&reserved=0). |
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |