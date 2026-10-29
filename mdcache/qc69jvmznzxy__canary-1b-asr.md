---
title: "canary-1b-asr"
publisher: "nvidia"
type: "endpoint"
updated: "2025-04-10T15:18:38.670Z"
description: "Multi-lingual model supporting speech-to-text recognition and translation."
canonical: "https://build.nvidia.com/nvidia/canary-1b-asr"
---

# Speech Recognition/Translation: Canary

## Description

NVIDIA Canary‑1B is a 1‑billion‑parameter multilingual model for both automatic speech recognition (ASR) and speech‑to‑text translation (AST). It’s designed to transcribe speech and translate between English and a wide range of other languages for production use cases.

This model is ready for commercial use. 

### License/Terms of Use

GOVERNING TERMS: The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and [Product-Specific Terms for AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). Use of this model is governed by the [NVIDIA Community Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/).

## Deployment Geography:
Global

## Use Case:
This model serves developers, researchers, academics, and industries building applications that require speech-to-text capabilities, including but not limited to: conversational AI, voice assistants, transcription services, subtitle generation, and voice analytics platforms.

#Release Date:
Build.Nvidia.com [10/15/2025] via [https://build.nvidia.com/nvidia/canary-1b-asr] 
Hugging Face [10/15/2025] via [URL] 
NGC [10/15/2025] via [https://build.stg.ngc.nvidia.com/nvidia/canary-1b-asr] 

## References

[1] [Less is More: Accurate Speech Recognition & Translation without Web-Scale Data](https://arxiv.org/pdf/2406.19674) <br>
[2] [Training and Inference Efficiency of Encoder-Decoder Speech Models](https://arxiv.org/pdf/2503.05931) <br>
[3] [New Standard for Speech Recognition and Translation from the NVIDIA NeMo Canary Model](https://developer.nvidia.com/blog/new-standard-for-speech-recognition-and-translation-from-the-nvidia-nemo-canary-model/) <br>
[4] [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084) <br>
[6] [Attention Is All You Need](https://arxiv.org/abs/1706.03762) <br>

## Model Architecture

**Architecture Type:** This model was developed based on the Canary Flash Architecture [2]. An encoder-decoder model with FastConformer [4] encoder and Transformer decoder [5]  <br>
**Network Architecture:** 42 layer encoder, 8 layer decoder, Number of model parameters: 918M <br>

## Input

**Input Type(s):** Audio <br>
**Input Format:** wav <br>
**Input Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Input:** Mono channel is required <br>

## Output

**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:** No Maximum Character Length, Does not handle special characters <br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration

**Runtime Engine(s):** 
* Riva 2.23.0 or higher <br>

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

Canary-1B-Flash 2.0

# Training & Evaluation 

## Training Dataset

**Data Modality**

[Audio]<br>
[Text]

**Audio Training Data Size**

[10,000 to 1 Million Hours]

**Data Collection Method by dataset** <br>

* Human <br>

**Labeling Method by dataset**<br>

* ASR: Human <br>
* AST: Human, Synthetic <br>

**Properties:**  <br>

Mixture of organic ASR data aligned with human voices and machine generated translations to create AST pairings.

## Evaluation Dataset

**Data Collection Method by dataset** <br>

* Human <br>

**Labeling Method by dataset**<br>

* Hybrid: Human, Synthetic <br> 

**Properties:**

A dynamic blend of public and internal proprietary and customer datasets aligning text with human audio data.

## Inference

**Acceleration Engine:** Triton <br>
**Test Hardware:** <br>
* NVIDIA A10 
* NVIDIA A100 
* NVIDIA A30 
* NVIDIA H100 
* NVIDIA L4 
* NVIDIA L40 
* NVIDIA Turing T4
* NVIDIA Volta V100

## Get Help

### Enterprise Support

Get access to knowledge base articles and support cases or [submit a ticket](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  

For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
What is the language balance of the model validation data? | ~3% per language across following languages and dialects: Arabic, Danish, Czech, German, American English, British English, Latin American Spanish, European Spanish, Metropole French, Canadian French, Hebrew, Hindi, Italian, Japanese, Korean, Norwegian Bokmal, Dutch, Polish, European Portuguese, Brazilian Portuguese, Russian, Swedish, Thai, Turkish, Mandarin Chinese.  
What is the geographic origin language balance of the model validation data? | Middle East, United States, Europe, East Asia, South Asia, Africa, Latin America, Southeast Asia
What is the accent balance of the model validation data? | ~3% per language.
Participation considerations from adversely impacted groups ([protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/)) in model design and testing:  |  Age, Gender, Linguistic Background
Measures taken to mitigate against unwanted bias:                                                   |  Used a custom dataset to validate model performance across demographic groups (gender, age, and language).

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Applications & Domains:                                                                       |  FastConformer-Encoder Transformer-Decoder Model for Automatic Speech Recognition (ASR) and Translation (AST)
Model Type:                                                                                            |  Speech Recognition and Speech Translation
Intended Users:                                                                                        |  This model is intended for developers and data scientists who are building interactive call-center applications, virtual assistants, and language-learning assistants.
Output:                                                                                                |  Text Sequence
Describe how the model works:                                                                          |  Model transcribes audio input into text for the input language or translates audio input into target language based on  probability of next word and audio input.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age, Gender, National Origin
Technical Limitations:                                                                                 |  Transcripts may not be 100% accurate. <br>  Translations may be technically correct but lack fluency. <br>  Translations may show bias towards grammatical gender in some European languages. <br>  Translations may show bias towards formal-informal tense in Korean and Japanese. <br>  Dialects not represented in training will likely see poor performance on both ASR and AST.
Verified to have met prescribed NVIDIA quality standards:                                              |  Yes
Performance Metrics:                                                                                   |  Word Error Rate (WER) of the ASR transcription. Bilingual Evaluation Understudy (BLEU) of the AST translation.
Potential Known Risks:                                                                                 |  If an audio sample occurs outside the domain of training, there is a higher likelihood of mistranslation/poor transcription. Dialects not represented in training will likely see poor performance on both ASR and AST.
Licensing:                                                                                             |  The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and [Product-Specific Terms for AI Products.](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/) Use of this model is governed by the [NVIDIA Community Model License.](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                                                 |  No
Personal data used to create this model?                                                                                           |  No
How often is dataset reviewed?                                                                                                     |  Before Release
Is there provenance for all datasets used in training?                                                                             |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  The data is compliant where applicable, but is not applicable for all data.
Applicable Privacy Policy                                                                                                          | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application Field(s):                         |  Automatic Speech Recognition & Translation
Describe the life-critical impacts (if present).    |  Not Applicable
Use Case Restriction(s):                            |  Abide by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and [Product-Specific Terms for AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). Use of this model is governed by the [NVIDIA Community Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/).
Describe access restrictions (if any):              | The Principle of Least Privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training and dataset license constraints adhered to.