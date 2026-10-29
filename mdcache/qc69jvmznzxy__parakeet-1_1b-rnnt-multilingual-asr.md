---
title: "parakeet-1.1b-rnnt-multilingual-asr"
publisher: "nvidia"
type: "endpoint"
updated: "2025-04-30T17:29:30.445Z"
description: "High accuracy and optimized performance for transcription in 25 languages"
canonical: "https://build.nvidia.com/nvidia/parakeet-1_1b-rnnt-multilingual-asr"
---

# Speech Recognition: Parakeet 

## Description

NVIDIA Parakeet‑RNNT‑1.1B is a multilingual ASR model with 1.1B parameters, trained on more than 90K hours of speech for high‑quality transcription across global use cases. It uses a universal tokenizer built by first training language‑specific tokenizers and then merging them into a single shared vocabulary, enabling efficient cross‑lingual learning and deployment. 

The model supports transcription in 25 languages and variants—including English (en‑US, en‑GB), Spanish (es‑US, es‑ES), German (de‑DE), French (fr‑FR, fr‑CA), Italian (it‑IT), Arabic (ar‑AR), Japanese (ja‑JP), Korean (ko‑KR), Portuguese (pt‑BR, pt‑PT), Russian (ru‑RU), Hindi (hi‑IN), Dutch (nl‑NL), Danish (da‑DK), Norwegian Nynorsk (nn‑NO), Norwegian Bokmål (nb‑NO), Czech (cs‑CZ), Polish (pl‑PL), Swedish (sv‑SE), Thai (th‑TH), Turkish (tr‑TR), and Hebrew (he‑IL). 

This model produces case‑sensitive transcripts (upper and lower case) with punctuation, spaces, and apostrophes, making it suitable for production‑grade voice applications and downstream language understanding.  
This model is ready for commercial use.

## License/Terms of Use

GOVERNING TERMS: The use of this model is governed by the NVIDIA Community Model License (found at https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/).

## References

[1] [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084) <br>
[2] [Fast-Conformer-RNNT Model](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/models.html) <br>
[3] [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100) <br>

## Model Architecture

**Architecture Type:** Parakeet-RNNT (also known as FastConformer-RNNT) [1], [2] which is an optimized version of Conformer model [3] with 8x depthwise-separable convolutional downsampling with Hybrid loss <br>
**Network Architecture:** Parakeet-RNNT-XXL-1.1B <br>

## Input 

**Input Type(s):** Audio <br>
**Input Format(s):** wav <br>
**Input Parameters:** 1-Dimension <br>
**Other Properties Related to Input:** Maximum Length in seconds specific to GPU Memory, No Pre-Processing Needed, Mono channel is required <br>

## Output 

**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** 1-Dimension <br>
**Other Properties Related to Output:** No Maximum Character Length, Does not handle special characters <br>

## Software Integration

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Blackwell <br>
* NVIDIA Ampere <br>
* NVIDIA Hopper <br>
* NVIDIA Jetson <br>
* NVIDIA Turing <br>

**[Preferred/Supported] Operating System(s):** <br>
* Linux <br>

## Model Version(s): 

Parakeet-RNNT-XXL-1.1b_universal_spe8.5k_1.0

## Inference

**Engine:** Triton <br>
**Test Hardware:** <br>
* NVIDIA A10 
* NVIDIA A100 
* NVIDIA A30 
* NVIDIA H100 
* NVIDIA L4 
* NVIDIA L40 
* NVIDIA Turing T4

## Ethical Considerations (For NVIDIA Models Only):
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
What is the language balance of the model validation data? | en-US: 35.0%, es-US: 9.66%, ko-KR: 8.07%, ru-RU: 6.33%, ar-AR: 5.65%, de-DE: 5.2%, fr-FR: 4.6%, hi-IN: 4.59%, it-IT: 4.2%, pt-BR: 3.5%, ja-JP: 2.82%, es-ES: 1.9%, pt-PT: 1.5%, nl-NL: 1.4%, tr-TR: 1.3%, fr-CA: 1.1%, en-GB: 0.95%, pl-PL: 0.64%, th-TH: 0.59%, he-IL: 0.26%, cs-CZ: 0.21%, da-DK: 0.19%, nb-NO: 0.18%, sv-SE: 0.16%
What is the geographic origin language balance of the model validation data? | North America: 45.75%, Europe: 27.47%, Asia: 16.1%, Middle East: 7.2%, South America: 3.5%
What is the accent balance of the model validation data? | en-US: 35.0%, es-US: 9.66%, ko-KR: 8.07%, ru-RU: 6.33%, ar-AR: 5.65%, de-DE: 5.2%, fr-FR: 4.6%, hi-IN: 4.59%, it-IT: 4.2%, pt-BR: 3.5%, ja-JP: 2.82%, es-ES: 1.9%, pt-PT: 1.5%, nl-NL: 1.4%, tr-TR: 1.3%, fr-CA: 1.1%, en-GB: 0.95%, pl-PL: 0.64%, th-TH: 0.59%, he-IL: 0.26%, cs-CZ: 0.21%, da-DK: 0.19%, nb-NO: 0.18%, sv-SE: 0.16%
Participation considerations from adversely impacted groups ([protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/)) in model design and testing:  |  Age, Gender, Linguistic Background
Measures taken to mitigate against unwanted bias:                                                   |  Used custom dataset to validate model performance across gender, age, and linguistic demographics

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Applications & Domains:                                                                       |  Speech Transcription
Model Type:                                                                                                 |  Speech Transcription
Intended Users:                                                                                        |  This model is intended for developers and data scientists building interactive call centers, virtual assistants, and language learning assistants
Output:                                                                                                |  Transcribed text with timestamps and confidence scores
Describe how the model works:                                                                          |  Model transcribes audio input into text for 25  languages
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age, Gender, National Origin
Technical Limitations:                                                                                 |  Transcripts may not be 100% accurate. Accuracy varies based on language and characteristics of input audio (Domain, Use Case, Accent, Noise, Speech Type, Context of speech, etc.)
Verified to have met prescribed NVIDIA quality standards:                                                     |  Yes
Performance Metrics:                                                                                   |  Word Error Rate (WER), Silence Robustness (Characters/mins of silent audio), Latency (in milliseconds), Throughput (Total audio processed per unit of time)
Potential Known Risks:                                                                                 |  Not recommended for word-for-word transcription as accuracy varies based on the characteristics of input audio (language, domain, use case, accent, noise, speech type, and context of speech)
Licensing:                                                                                             |  [https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                     |  None
Personal data used to create this model?                                                                                   |  None
How often is dataset reviewed?                                                                                                     |  Before Release
Is there data provenance for all datasets used in training?                                                                                                                          |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes  
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  The data is compliant where applicable, but is not applicable for all data.

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  Speech Transcription
Describe the life-critical impacts (if present).   |  Not Applicable
Use Case Restriction(s):                              |  Abide by [https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/)
Describe access restrictions (if any):   | The Principle of Least Privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training and dataset license constraints adhered to.