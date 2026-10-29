---
title: "parakeet-ctc-0.6b-es"
publisher: "nvidia"
type: "endpoint"
updated: "2025-09-09T10:10:03.570Z"
description: "Accurate and optimized Spanish English transcriptions with punctuation and word timestamps."
canonical: "https://build.nvidia.com/nvidia/parakeet-ctc-0_6b-es"
---

# Speech Recognition: Parakeet CTC 0.6b Spanish English Code Switch Model

## Description
NVIDIA Parakeet-CTC-0.6B is a 600M parameter model trained on ASR Set with over 28k hours of Spanish (es-US) and English (en-US) speech. The model transcribes speech in Spanish and English, in upper case and lower case alphabets, along with punctuations (period, comma, and question mark), spaces, and apostrophes.

This model is ready for commercial use.

## Terms of use
GOVERNING TERMS: This trial is governed by the NVIDIA API Trial Terms of Service (found at https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). 

## References
* [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084)
* [Fast-Conformer-CTC Model](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html)
* [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100)

## Model Architecture
**Architecture Type:** Parakeet-CTC (also known as FastConformer-CTC) [1], [2] which is an optimized version of Conformer model [3] with 8x depthwise-separable convolutional downsampling with CTC loss <br>
**Network Architecture:** Parakeet-CTC-XXL-0.6B <br>

## Input
**Input Type(s):** Audio 
**Input Format(s):** wav 
**Input Parameters:** 1-Dimension 
**Other Properties Related to Input:** Maximum Length in seconds specific to GPU Memory, No Pre-Processing Needed, Mono channel is required

## Output
**Output Type(s):** Transcription for what was spoken in input speech <br>
**Output Type(s):** Text 
**Output Format:** String (in Spanish and English) 
**Output Parameters:** 1-Dimension 
**Other Properties Related to Output:** No Maximum Character Length, Does not handle special characters

**Supported Operating System(s):**  <br>
* Linux <br>

## Model Version
Parakeet-CTC-XL-unified-0.6b_spe1024_es-en-US_3.0 <br>

## Training & Evaluation

### Training Dataset

**Data Collection Method by dataset**<br>

* Human <br>

**Labeling Method by dataset** <br>

* Human <br>

**Properties:** 

This model is trained on over 28,000 hours of Spanish (es-US) and English (en-US) speech, comprised of a dynamic blend of public and internal proprietary and customer datasets normalized to have upper-cased, lower-cased, punctuated, and spoken forms in text.

### Evaluation Dataset

**Data Collection Method by dataset** <br>

* Human <br>

**Labeling Method by dataset** <br>

* Human <br>

**Properties:**
A dynamic blend of public and internal proprietary and customer datasets normalized to have upper-cased, lower-cased, punctuated, and spoken forms in text.

## Inference
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
What is the language balance of the model validation data? | Spanish: 50%, English 50%
What is the geographic origin language balance of the model validation data? | America: 65%, Europe: 30%, Other: 5%
What is the accent balance of the model validation data? | Latin American Spanish: 30%, European Spanish: 20%, American English: 40%, British English: 5%, Other Accented English: 5%
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
Was consent obtained for any personal data used?                                                                                   |  Not Applicable
Protected class data used to create this model?                                                                                    |  Age, Gender, Linguistic Background, National Origin
How often is dataset reviewed?                                                                                                     |  Before Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Not Applicable
If Personal data collected for the development of the model, was it collected directly by NVIDIA?                                  |  Not Applicable
If Personal data collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  Not Applicable
If Personal data collected for the development of this AI model, was it minimized to only what was required?                                 |  Not Applicable
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