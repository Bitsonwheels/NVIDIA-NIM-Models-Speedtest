---
title: "parakeet-ctc-0.6b-zh-tw"
publisher: "nvidia"
type: "endpoint"
updated: "2025-10-16T01:36:31.358Z"
description: "Record-setting accuracy and performance for Mandarin Taiwanese English transcriptions."
canonical: "https://build.nvidia.com/nvidia/parakeet-ctc-0_6b-zh-tw"
---

# Speech Recognition: Parakeet 

## Description

NVIDIA Parakeet-CTC-0.6B ASR Taiwanese Mandarin (600M parameters) is trained on an ASR dataset with around 90 hours of Taiwanese Mandarin (zh-TW) speech. The model transcribes speech in Taiwanese Mandarin (Traditional Chinese), in upper case and lower case alphabets along with spaces. While the model does not transcribe text with punctuation (period, comma, and question mark), the fused Language Model (LM) decoding may attempt to provide punctuation capabilities.

This model is ready for commercial use.

## License/Terms of Use 

<!-- GOVERNING TERMS: The use of this model is governed by the NVIDIA Community Model License (found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). -->

### Deployment Geography:

Global

### Use Case:

This model serves developers, researchers, academics, and industries building applications that require speech-to-text capabilities, including but not limited to: conversational AI, voice assistants, transcription services, subtitle generation, and voice analytics platforms.

### Release Date:

Build.Nvidia.com 10/09/2025 via [URL] <br>
<!-- Github [Insert MM/DD/YYYY] via [URL] <br>
Hugging Face [Insert MM/DD/YYYY] via [URL] <br> -->
NGC 10/09/2025 via [URL] <br>
<!-- Other [Insert MM/DD/YYY] via [URL]<br> -->

## References

[1] [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084) <br>
[2] [Fast-Conformer-CTC Model](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html) <br>
[3] [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100) <br>

## Model Architecture

**Architecture Type:** Parakeet-CTC (also known as FastConformer-CTC) [1], [2], which is an optimized version of the Conformer model [3], features 8x depthwise-separable convolutional downsampling with CTC loss. <br> 
**Network Architecture:** Parakeet-CTC-XL-0.6B <br>
**This model was developed based on [FastConformer](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#fast-conformer) architecture.** <br>
**This model has 600 million model parameters.**

## Input 

**Input Type(s):** Audio <br>
**Input Format:** wav <br>
**Input Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Input:** Maximum Length in seconds specific to GPU Memory, No Pre-Processing Needed, Mono channel is required. <br>

## Output 

**Output Type(s):** Text 
**Output Format:** String (in Mandarin and English) <br>
**Output Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:** No Maximum Character Length, Does not handle special characters. <br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. 

## How to Use this Model

The [Riva Quick Start Guide](https://ngc.nvidia.com/catalog/resources/nvidia:riva:riva_quickstart) is recommended as the starting point for trying out Riva models. For more information on using this model with Riva Speech Services, see the [Riva User Guide](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/asr/asr-overview.html).

## Suggested Reading

Refer to the [Riva documentation](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/index.html) for more information.

## Software Integration

**Runtime Engine(s):** 
* Riva 2.19.0 or higher <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Hopper <br>
* NVIDIA Jetson <br>
* NVIDIA Turing <br>
* NVIDIA Volta <br>

**[Preferred/Supported] Operating System(s):** <br>
* Linux <br>
* Linux 4 Tegra <br>

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Model Version(s): 

Parakeet-CTC-XL-0.6b_zh-TW_1.0

# Training and Evaluation Datasets: 

## Training Dataset

**Data Modality**<br>

* Other: Speech<br>

**Text Training Data Size**<br>

Less than a Billion Tokens

**Non-Audio, Image, Text Training Data Size**<br>

The model was trained approximately 90 hours of Taiwanese Mandarin speech data:
* Common Voice Corpus 20.0
* TechOrange-Podcast

**Data Collection Method by dataset**<br>

* Human <br>

**Labeling Method by dataset**<br>

* Human <br>

**Properties:**  <br>

This model is trained on around 90 hours of Taiwanese Mandarin (zh-TW) speech, comprised of a dynamic blend of public and internal proprietary datasets.

## Evaluation Dataset

**Data Modality**<br>

* Other: Speech<br>

**Text Evaluation Data Size**<br>

Less than a Billion Tokens

**Non-Audio, Image, Text Evaluation Data Size**<br>

The model was evaluated approximately 17.5 hours of Taiwanese Mandarin speech data:
* Common Voice Corpus 20.0
* TechOrange-Podcast
* NV-zh-tw-subtitle

**Data Collection Method by dataset**<br>

* Human <br>

**Labeling Method by dataset**<br>

* Human <br>

**Properties:**

A dynamic blend of public and internal proprietary datasets.

## Inference

**Acceleration Engine:** Triton <br>
**Test Hardware:** <br>
* NVIDIA A10 
* NVIDIA A100 
* NVIDIA A30 
* NVIDIA H100 
* NVIDIA Jetson Orin
* NVIDIA L4 
* NVIDIA L40 
* NVIDIA Turing T4
* NVIDIA Volta V100

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards [here](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/riva/models/parakeet-ctc-riva-0-6b-unified-zh-cn/bias).  

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
What is the language balance of the model validation data? | Taiwanese Mandarin Chinese: 100%
What is the geographic origin language balance of the model validation data? | Taiwan: 100%
What is the accent balance of the model validation data? | Taiwanese Mandarin Chinese: 100%
Participation considerations from adversely impacted groups ([protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/)) in model design and testing:  |  Age, Gender, Linguistic Background
Measures taken to mitigate against unwanted bias:                                                   |  Used custom dataset to validate model performance across gender, age, and linguistic demographics

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Task/Domain:                                                                       |  Speech Transcription
Model Type:                                                                                                 |  Transformer
Intended Users:                                                                                        |  This model is intended for developers and data scientists building interactive call centers, virtual assistants, and language learning assistants.
Output:                                                                                                |  Transcribed text with timestamps and confidence scores.
Describe how the model works:                                                                          |  Model transcribes audio input into text for the input language.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age, Gender, National Origin
Technical Limitations & Mitigation:                                                                                 |  Transcripts may not be 100% accurate. Accuracy varies based on the characteristics of input audio (domain, use case, accent, noise, speech type, context of speech, etc.).
Verified to have met prescribed NVIDIA quality standards:                                                     |  Yes
Performance Metrics:                                                                                   |  Word error rate (WER), silence robustness (characters per minute of silent audio), latency (in milliseconds), and throughput (total audio processed per unit of time).
Potential Known Risks:                                                                                 |  Not recommended for word-for-word transcription as accuracy varies based on the characteristics of input audio (domain, use case, accent, noise, speech type, and context of speech).
Licensing:                                                                                             |  [https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                     |  No
Personal data used to create this model?                                                     |  No
Was consent obtained for any personal data used?                                                                                   |  Not Applicable
How often is dataset reviewed?                                                                                                     |  Before Release
Is there data provenance for all datasets used in training?                                                                        |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes  
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  The data is compliant where applicable, but is not applicable for all data.
Applicable Privacy Policy | [https://www.nvidia.com/en-us/about-nvidia/privacy-policy/](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/)

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application Field(s):                               |  Speech Transcription
Describe the life-critical impacts (if present).   |  Not Applicable
Use Case Restriction(s):                              |  Abide by [https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/)
Model and dataset restrictions:   | The Principle of Least Privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training and dataset license constraints adhered to.