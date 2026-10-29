---
title: "parakeet-ctc-0.6b-zh-cn"
publisher: "nvidia"
type: "endpoint"
updated: "2025-09-09T10:36:17.833Z"
description: "Record-setting accuracy and performance for Mandarin English transcriptions."
canonical: "https://build.nvidia.com/nvidia/parakeet-ctc-0_6b-zh-cn"
---

# Speech Recognition: Parakeet CTC 0.6b Mandarin English Code Switch Model

## Description

NVIDIA Parakeet‑CTC‑0.6B‑Unified is a 600M‑parameter ASR model trained on more than 17K hours of Mandarin Chinese (zh‑CN) and American English (en‑US) speech. It delivers high‑quality transcription for both languages, producing mixed‑case text with support for periods, commas, question marks, spaces, and apostrophes. This model is suitable for commercial deployment in production applications.

## License/Terms of Use 

GOVERNING TERMS: The use of this model is governed by the NVIDIA Community Model License (found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/).

## References

[1] [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084) <br>
[2] [Fast-Conformer-CTC Model](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html) <br>
[3] [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100) <br>

## Model Architecture

**Architecture Type:** Parakeet-CTC (also known as FastConformer-CTC) [1], [2] which is an optimized version of Conformer model [3] with 8x depthwise-separable convolutional downsampling with CTC loss <br> 
**Network Architecture:** Parakeet-CTC-XL-0.6B <br>

## Input 

**Input Type(s):** Audio <br>
**Input Format(s):** wav <br>
**Input Parameters:** 1-Dimension <br>
**Other Properties Related to Input:** Maximum Length in seconds specific to GPU Memory, No Pre-Processing Needed, Mono channel is required. <br>

## Output 

**Output Type(s):** Text 
**Output Format:** String (in Mandarin and English) <br>
**Output Parameters:** 1-Dimension <br>
**Other Properties Related to Output:** No Maximum Character Length, Does not handle special characters. <br>

**Supported Operating System(s):**  <br>
* Linux <br>

## Model Version(s): 

Parakeet-CTC-XL-unified-0.6b_spe7k_zh-CN_3.0

## Training & Evaluation 

### Training Dataset

**Data Collection Method by dataset**<br>

* Human <br>

**Labeling Method by dataset** <br>

* Human <br>

**Properties:**  <br>

This model is trained on over 17,000 hours of Mandarin (zh-CN) and English (en-US) speech, comprised of a dynamic blend of public and internal proprietary datasets normalized to have upper-cased, lower-cased, punctuated, and spoken forms in text.

### Evaluation Dataset

**Data Collection Method by dataset** <br>

* Human <br>

**Labeling Method by dataset** <br>

* Human <br>

**Properties:**

A dynamic blend of public and internal proprietary datasets normalized to have upper-cased, lower-cased, punctuated, and spoken forms in text.

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

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
What is the language balance of the model validation data? | Mandarin Chinese: 49%, English: 51%
What is the geographic origin language balance of the model validation data? | China: 47%, United States: 49%, Other: 4%
What is the accent balance of the model validation data? | Mandarin Chinese: 49%, American English: 49%, Other Accented English: 2%
Participation considerations from adversely impacted groups ([protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/)) in model design and testing:  |  Age, Gender, Linguistic Background
Measures taken to mitigate against unwanted bias:                                                   |  Used custom dataset to validate model performance across gender, age, and linguistic demographics

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Applications & Domains:                                                                       |  Speech Transcription
Types:                                                                                                 |  Speech Transcription
Intended Users:                                                                                        |  This model is intended for developers and data scientists building interactive call centers, virtual assistants, and language learning assistants
Output:                                                                                                |  Transcribed text with timestamps and confidence scores
Describe how the model works:                                                                          |  Model transcribes audio input into text for the input language
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age, Gender, National Origin
Technical Limitations:                                                                                 |  Transcripts may not be 100% accurate. Accuracy varies based on the characteristics of input audio (Domain, Use Case, Accent, Noise, Speech Type, Context of speech, etc.)
Verified to have met prescribed NVIDIA quality standards:                                                     |  Yes
Performance Metrics:                                                                                   |  Word Error Rate (WER), Silence Robustness (Characters/mins of silent audio), Latency (in milliseconds), Throughput (Total audio processed per unit of time)
Potential Known Risks:                                                                                 |  Not recommended for word-for-word transcription as accuracy varies based on the characteristics of input audio (domain, use case, accent, noise, speech type, and context of speech)
Licensing:                                                                                             |  [https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personally-identifiable information (PII)?                                                     |  None
Was consent obtained for any personal data used?                                                                                   |  None
How often is dataset reviewed?                                                                                                     |  Before Release
Is there data provenance for all datasets used in training?                                                                        |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes  
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  The data is compliant where applicable, but is not applicable for all data.

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  Speech Transcription
Describe the life-critical impacts (if present).   |  Not Applicable
Use Case Restriction(s):                              |  Abide by [https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/)
Describe access restrictions (if any):   | The Principle of Least Privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training and dataset license constraints adhered to.