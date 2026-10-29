---
title: "nemotron-asr-streaming"
publisher: "nvidia"
type: "endpoint"
updated: "2026-03-14T12:33:34.989Z"
description: "Real-time speech recognition for English"
canonical: "https://build.nvidia.com/nvidia/nemotron-asr-streaming"
---

## Model Overview

### Description

This NIM contains 2 profiles:

- `nvidia/nemotron-speech-streaming-en-0.6b` (Nemotron 3 ASR - English)
- `nvidia/nemotron-3.5-asr-streaming-0.6b` (Nemotron 3.5 ASR - 40 language-locales)

**Nemotron 3 ASR** is a 600-million-parameter streaming Automatic Speech Recognition (ASR) model engineered for high-quality English transcription across both low-latency streaming and high-throughput batch workloads. Developed by NVIDIA, it natively outputs punctuation and capitalization with no post-processing required.

By leveraging a **Cache-Aware FastConformer-RNNT** architecture, the model processes only new audio chunks while reusing cached encoder context - eliminating redundant overlapping computations and minimizing end-to-end latency without sacrificing accuracy. Trained on over 250,000 hours of US English (en-US) speech, it performs robustly across diverse acoustic conditions.

**Key Features:**

- Low-latency streaming with zero overlapping computations
- Native punctuation and capitalization output
- 250,000+ hours of en-US training data for strong noise robustness
- Supports both streaming and high-throughput batch inference

**Nemotron 3.5 ASR** extends Nemotron 3 ASR from English to **40 languages and locales**, with automatic language detection - no language selection required at runtime. Built on the same Cache-Aware FastConformer-RNNT architecture, it is designed for the same low-latency streaming use cases as its predecessor, now serving global, multilingual deployments.

**Key Features:**

- 40 supported languages and locales with automatic language detection
- Low-latency streaming with zero overlapping computations
- Native punctuation and capitalization output
- Drop-in multilingual replacement for Nemotron 3 ASR streaming pipelines

## License/Terms of Use

**GOVERNING TERMS:** This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/); use of the model is governed by the [OpenMDW License Agreement v1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1).

```{note}
To deploy the multilingual variant of this model, Nemotron 3.5 ASR, with 40 language-locales, set
`NIM_TAGS_SELECTOR=type=multi`

The model includes automatic language detection and is intended for the same streaming use cases as Nemotron 3 ASR which is English only. Refer to the deployment instructions for usage details.
```

## Deployment Selectors

Please see the **Deploy** tab for reference.

| Profile | `NIM_TAGS_SELECTOR` | HuggingFace |
| --- | --- | --- |
| Nemotron 3 ASR (English) | (default is en-US - for English, no selector needed) | [nvidia/nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b) |
| Nemotron 3.5 ASR (40 languages) | `type=multi` | [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) |

## Release Date

**Nemotron 3 ASR: 03/12/2026**

- build.nvidia.com: [build.nvidia.com/nvidia/nemotron-asr-streaming](https://build.nvidia.com/nvidia/nemotron-asr-streaming)
- Hugging Face: [nvidia/nemotron-speech-streaming-en-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)
- NGC: [catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemotron-asr-streaming](https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemotron-asr-streaming/)

**Nemotron 3.5 ASR: June 4 and June 11, 2026**

- build.nvidia.com: [build.nvidia.com/nvidia/nemotron-asr-streaming](https://build.nvidia.com/nvidia/nemotron-asr-streaming)
- Hugging Face: [nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)
- NGC: [catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemotron-asr-streaming](https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemotron-asr-streaming/)

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
What is the language balance of the model validation data?  |  English: 100%
What is the geographic origin language balance of the model validation data?                                                 |  United States: 80%, United Kingdom: 10%, Others: 10%
What is the accent balance of the model validation data?                                                   |  American English: 80%, British English: 10%, Others: 10%
Participation considerations from adversely impacted groups ([protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/)) in model design and testing: |  Age, Gender, Linguistic Background
Measures taken to mitigate against unwanted bias: | Used a custom dataset to evaluate model performance across genders, age groups, and linguistic backgrounds.

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Task/Domain:                                                                   |  Speech Transcription
Model Type:                                                                                            |  FastConformer-RNNT
Intended Users:                                                                                        |  This model is intended for developers and data scientists building interactive call centers, virtual assistants, and language learning assistants.
Output:                                                                                                |  Transcribed text with timestamps and confidence scores
Describe how the model works:                                                                          |  Model transcribes audio input into text for the input language
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age, Gender, National Origin
Technical Limitations & Mitigation:                                                                    |  Transcripts may not be 100% accurate. Accuracy varies depending on the characteristics of the input audio, such as domain, use case, accent, noise, speech type, and speech context. 
Verified to have met prescribed NVIDIA quality standards:  |  Yes
Performance Metrics:                                                                                   |  Word Error Rate (WER), Silence Robustness (Characters/mins of silent audio), Latency (in milliseconds), Throughput (Total audio processed per unit of time)
Potential Known Risks:                                                                                 |  Not recommended for word-for-word transcription as accuracy varies based on the characteristics of input audio (domain, use case, accent, noise, speech type, and context of speech)
Licensing:                                                                                             | This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/); use of the model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                     |  No
Personal data used to create this model?                                                                                       |  Yes - Voice
Was consent obtained for any personal data used?                                                                                             |  Yes
Is a mechanism in place to honor data subject right of access or deletion of personal data? | Yes
If personal data was collected for the development of the model, was it collected directly by NVIDIA?                                            |  Yes
If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  Yes
If personal data was collected for the development of this AI model, was it minimized to only what was required?                                 |  Yes
Is there provenance for all datasets used in training?                                                                                |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  No, not possible with externally-sourced data.
Applicable Privacy Policy        | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/ 
How often is dataset reviewed? | Dataset is initially reviewed upon addition, and subsequent reviews are conducted as needed or upon request for changes.
Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model? | No

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application Field(s):                               |  Speech Transcription
Describe the life critical impact (if present).   |  Not Applicable 
Use Case Restrictions:                              |  Abide by Governing Terms: This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/); use of the model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).
Model and dataset restrictions:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to.