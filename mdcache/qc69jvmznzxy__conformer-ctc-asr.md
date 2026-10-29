---
title: "conformer-ctc-asr"
publisher: "nvidia"
type: "endpoint"
updated: "2025-04-10T15:19:39.201Z"
description: "Automatic speech recognition model that transcribes speech in lower case Spanish with record-setting accuracy and performance"
canonical: "https://build.nvidia.com/nvidia/conformer-ctc-asr"
---

## Model Overview

Conformer-CTC (around 120M parameters) is trained on ASRSet with over 4100 hours of Spanish (es-US) speech. The model transcribes speech in lower case Spanish alphabet along with spaces and apostrophes.

## Model Architecture

Conformer-CTC model is a non-autoregressive variant of Conformer model for Automatic Speech Recognition which uses CTC loss/decoding instead of Transducer. For more information, refer to the [Conformer-CTC Model](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html#conformer-ctc) documentation.

## License/Terms of Use

GOVERNING TERMS: The use of this model is governed by the NVIDIA Community Model License (found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/).

# Disclaimer
AI models generate responses and outputs based on complex algorithms and machine learning techniques, and those responses or outputs may be inaccurate or indecent. By testing this model, you assume the risk of any harm caused by any response or output of the model. Please do not upload any confidential information or personal data. Your use is logged for security. 

# References
* [Paper](https://arxiv.org/abs/2005.08100)
* [Conformer](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html#conformer)

## Model Architecture
**Architecture Type:** Convolutional Neural Network + Transformer <br>
**Network Architecture:** Conformer Encoder with CTC Decoder <br>

## Input
**Input Type(s):** Audio in Spanish <br>
**Input Format(s):** Linear PCM 16-bit 1 channel <br>

## Output
**Output Type(s):** Text String in Text String in Spanish <br>

## Software Integration
**Supported Operating System(s):**  <br>
* Linux <br>

## Model Version
* Conformer-CTC-L_spe256_es-US_3.1 <br>

# Inference
**Engine:** Triton <br>
**Test Hardware:**  <br>
* NVIDIA A10 <br>
* NVIDIA A100 <br>
* NVIDIA A30 <br>
* NVIDIA H100 <br>
* NVIDIA Jetson Orin <br>
* NVIDIA L4 <br>
* NVIDIA L40 <br>
* NVIDIA Turing T4 <br>
* NVIDIA Volta V100 <br>

## Ethical Considerations (For NVIDIA Models Only):
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

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