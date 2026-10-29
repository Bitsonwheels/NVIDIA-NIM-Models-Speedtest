---
title: "parakeet-ctc-0.6b-asr"
publisher: "nvidia"
type: "endpoint"
updated: "2025-06-13T14:13:00.782Z"
description: "State-of-the-art accuracy and speed for English transcriptions."
canonical: "https://build.nvidia.com/nvidia/parakeet-ctc-0_6b-asr"
---

# Model Overview
Parakeet-CTC-XL-0.6B (around 600M parameters) is trained on ASRSet with over 35000 hours of English (en-US) speech. The model transcribes speech in lower case English alphabet along with spaces and apostrophes.

## Description
Parakeet transcribes audio into text, using spaces and apostrophes where needed <br>

## Terms of use
By using this software or microservice, you are agreeing to the [terms and conditions](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/) of the license and acceptable use policy.

# Disclaimer
AI models generate responses and outputs based on complex algorithms and machine learning techniques, and those responses or outputs may be inaccurate or indecent. By testing this model, you assume the risk of any harm caused by any response or output of the model. Please do not upload any confidential information or personal data. Your use is logged for security. 

# References
* [Paper](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#fast-conformer)
* [Fast-Conformer-CTC Model](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#fast-conformer)
* [Conformer](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html#conformer)

## Model Architecture
**Architecture Type:** Parakeet-CTC (also known as FastConformer-CTC), which is an optimized version of Conformer model with 8x depthwise-separable convolutional downsampling with CTC loss <br> 
**Network Architecture:** Parakeet-CTC-XL-0.6B <br>

## Input
**Input Type(s):** Audio in English <br>
**Input Format(s):** Linear PCM 16-bit 1 channel <br>
**Other Properties Related to Input:** Maximum Length in seconds specific to GPU Memory, No Pre-Processing Needed, Mono channel is required <br>

## Output
**Output Type(s):** Text String in English with Timestamps <br>
**Output Parameters:** 1-Dimension <br>
**Other Properties Related to Output:** No Maximum Character Length, Does not handle special characters <br>

## Software Integration
**Runtime Engine(s):** 
* Riva 2.15.0 or Higher <br>

**Supported Operating System(s):**  <br>
* Linux <br>

## Model Version
Parakeet-0.6b-ctc-en-us-asr-set-6.0 <br>

# Inference
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

## GOVERNING TERMS: 
This trial is governed by the NVIDIA API Trial Terms of Service (found at https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). The use of this model is governed by the AI Foundation Models Community License Agreement (found at NVIDIA Agreements | Enterprise Software | NVIDIA AI Foundation Models Community License Agreement).

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
What is the language balance of the model validation data? | English: 100%
What is the geographic origin language balance of the model validation data? | United States: 80%, United Kingdom: 10%, Others: 10%
What is the accent balance of the model validation data? | American English: 80%, British English: 10%, Others: 10%
Participation considerations from adversely impacted groups ([protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/)) in model design and testing:  |  Age, Gender, Linguistic Background
Measures taken to mitigate against unwanted bias:                                                   |  Used custom dataset to validate model performance across gender, age, and linguistic demographics

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Applications & Domains:                                                                       |  Speech Transcription
Types:                                                                                                 |  Speech Transcription
Intended Users:                                                                                        |  This model is intended for developers and data scientists building interactive call centers, virtual assistants, language learning assistants.
Output:                                                                                                |  Transcribed text with timestamps and confidence scores
Describe how the model works:                                                                          |  Model transcribes audio input into text for the input language
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age, Gender, National Origin
Technical Limitations:                                                                                 |  Transcripts may not be 100% accurate. Accuracy varies based on the characteristics of input audio (Domain, Use Case, Accent, Noise, Speech Type, Context of speech, etc.)
Verified to have met prescribed NVIDIA quality standards:                                                     |  Yes
Performance Metrics:                                                                                   |  Word Error Rate (WER), Silence Robustness (Characters/mins of silent audio), Latency (in milliseconds), Throughput (Total audio processed per unit of time)
Potential Known Risks:                                                                                 |  Not recommended for word-for-word transcription as accuracy varies based on the characteristics of input audio (domain, use case, accent, noise, speech type, and context of speech)
Licensing:                                                                                             |  [https://docs.nvidia.com/ai-foundation-models-community-license.pdf](https://docs.nvidia.com/ai-foundation-models-community-license.pdf)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personally-identifiable information (PII)?                                                     |  None
Was consent obtained for any personal data used?                                                                                   |  Yes
Protected class data used to create this model?                                                                                    |  Age, Gender, Linguistic Background, National Origin
How often is dataset reviewed?                                                                                                     |  Before Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  No
If Personal data collected for the development of the model, was it collected directly by NVIDIA?                                  |  Personal data not collected by NVIDIA for development of model
If Personal data collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  Not Applicable
If Personal data collected for the development of this AI model, was it minimized to only what was required?                                 |  Yes
Is there provenance for all datasets used in training?                                                                                                                          |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes  
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  The data is compliant where applicable, but is not applicable for all data.

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  Speech Transcription
Describe the life-critical impacts (if present).   |  Not Applicable
Use Case Restriction(s):                              |  Abide by https://developer.nvidia.com/riva/ga/license
Describe access restrictions (if any):   | The Principle of Least Privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training and dataset license constraints adhered to.