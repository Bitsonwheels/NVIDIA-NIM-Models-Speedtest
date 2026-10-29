---
title: "parakeet-ctc-1.1b-asr"
publisher: "nvidia"
type: "endpoint"
updated: "2025-06-26T20:47:19.082Z"
description: "Record-setting accuracy and performance for English transcription."
canonical: "https://build.nvidia.com/nvidia/parakeet-ctc-1_1b-asr"
---

# Model Overview
Parakeet is a major step forward in the evolution of conversational AI. Its exceptional accuracy, coupled with the flexibility and ease of use offered by NeMo, empowers developers to create more natural and intuitive voice-powered applications. The possibilities are endless, from enhancing the accuracy of virtual assistants to enabling seamless real-time communication.

## Description
Parakeet transcribes audio into text, using spaces and apostrophes where needed <br>

## Terms of use
GOVERNING TERMS: Use of this model is governed by the [NVIDIA Community Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/).

# Disclaimer
AI models generate responses and outputs based on complex algorithms and machine learning techniques, and those responses or outputs may be inaccurate or indecent. By testing this model, you assume the risk of any harm caused by any response or output of the model. Please do not upload any confidential information or personal data. Your use is logged for security. 

# References
* [Fast Conformer](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#fast-conformer)

## Model Architecture
**Architecture Type:** Convolutional Neural Network + Transformer <br>
**Network Architecture:** Fast Conformer Encoder with CTC Decoder <br>

## Input
**Input Type(s):** Audio in English <br>
**Input Format(s):** Linear PCM 16-bit 1 channel <br>

## Output
**Output Type(s):** Text String in English with Timestamps <br>

## Software Integration
**Runtime Engine(s):** 
* Riva 2.15.0 or Higher <br>

**Supported Operating System(s):**  <br>
* Linux <br>

## Model Version
Parakeet-1.1b-ctc-en-us-asr-set-6.0 <br>

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

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Participation considerations from adversely impacted groups ([protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/)) in model design and testing:  |  Age, Gender, Linguistic Background
Measures taken to mitigate against unwanted bias:                                                   |  Used custom dataset to validate model performance across gender, age, and linguistic demographics

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Applications & Domains:                                                                       |  Speech Transcription
Types:                                                                                                 |  Speech Transcription
Intended Users:                                                                                        |  Data Scientists in Contact Center Transcription, Video Conferencing Transcription, Virtual Assistants, etc
Output:                                                                                                |  Transcribed text with timestamps and confidence scores
Describe how the model works:                                                                          |  Model transcribes audio input into text for the input language
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age, Gender, National Origin
Technical Limitations:                                                                                 |  Transcripts may  not be 100% accurate. Accuracy varies based on the characteristics of input audio (Domain, Use Case, Accent, Noise, Speech Type, Context of speech, etc.)
Verified to have met prescribed NVIDIA quality standards:                                                     |  Yes
Performance Metrics:                                                                                   |  Word Error Rate (WER), Silence Robustness (Characters/mins of silent audio), Latency (in milliseconds), Throughput (Total audio processed per unit of time)
Potential Known Risks:                                                                                 |  Not recommended for word-for-word transcription as accuracy varies based on the characteristics of input audio (domain, use case, accent, noise, speech type, and context of speech)
Licensing:                                                                                             |  https://developer.nvidia.com/riva/ga/license

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personally-identifiable information (PII)?                                                     |  None
Was consent obtained for any PII used?                                                                                             |  Yes
Protected class data used to create this model?                                                                                    |  Age, Gender, Linguistic Background, National Origin
How often is dataset reviewed?                                                                                                     |  Before Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  No
If PII collected for the development of the model, was it collected directly by NVIDIA?                                            |  PII not collected by NVIDIA for development of model
If PII collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  Not applicable
If PII collected for the development of this AI model, was it minimized to only what was required?                                 |  Yes
Is there provenance for all datasets used in training?                                                                                                                          |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes  
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  The data is compliant where applicable, but is not applicable for all data.

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  Speech Transcription
Describe the life-critical impacts (if present).   |  Not Applicable for Licensed Use Cases per [NVIDIA RIVA License Agreement](https://developer.nvidia.com/riva/ga/license)
Use Case Restriction(s):                              |  Abide by https://developer.nvidia.com/riva/ga/license
Model and Dataset Restriction(s):                       |  Dataset access restrictions
Describe access restrictions (if any):   | The Principle of Least Privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training and dataset license constraints adhered to.