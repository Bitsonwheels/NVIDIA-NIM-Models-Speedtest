---
title: "magpie-tts-zeroshot"
publisher: "nvidia"
type: "endpoint"
updated: "2025-06-12T15:03:36.401Z"
description: "Expressive and engaging text-to-speech, generated from a short audio sample."
canonical: "https://build.nvidia.com/nvidia/magpie-tts-zeroshot"
---

Overview
# Speech Synthesis: Magpie TTS Zeroshot Model Overview

## Description:
The Magpie TTS Zeroshot model converts text into audio (speech).

Magpie TTS is a generative model, designed to be used as the first part of a neural text-to-speech system in conjunction with an audio codec model. This model uses the International Phonetic Alphabet (IPA) for inference and training, and it can output a female or a male voice for English-US and European-Spanish. In addition, it uses character-based encoding for French. 

Audio Codec is a neural codec model for speech applications. It is the second part of a two-stage speech synthesis pipeline.

This model is ready for commercial use.  

### License/Terms of Use: <br> 
[NVIDIA AI Foundation Models Community License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/)

## References:
TTS model papers:
[Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance](https://arxiv.org/pdf/2502.05236)
[Improving Robustness of LLM-based Speech Synthesis by Learning Monotonic Alignment](https://arxiv.org/pdf/2406.17957)
[Low Frame-rate Speech Codec: A Codec Designed for Fast High-quality Speech LLM Training and Inference](https://arxiv.org/abs/2409.12117)

## Model Architecture: 
Network Architecture: T5-TTS + Audio codec 
T5-TTS is an encoder-decoder transformer model for text-to-speech synthesis that improves robustness by learning monotonic alignment between text and speech tokens. The model takes text tokens and reference audio codes as input and autoregressively predicts acoustic tokens of the target speech.
Low Frame Rate Speech Codec - 21Hz is a neural audio compression model that quantizes speech or audio signals into discrete tokens at a low temporal rate of 21 frames per second. The model typically employs a multi-stage encoding process to compress the input audio into a sequence of discrete codes while preserving essential acoustic characteristics despite the aggressive temporal compression. During encoding, it analyzes longer windows of audio to capture relevant acoustic features before downsampling to 21Hz, and during decoding, it uses neural upsampling techniques to reconstruct high-fidelity audio at the original sampling rate. This lower frame rate allows for efficient storage and transmission while still maintaining reasonable audio quality for applications like speech synthesis and audio compression.

## Input: 
**Input Type:** Text <br>
**Input Format:** Strings (Graphemes in US English) <br>
**Input Parameters:** One-Dimensional (1D) <br>

## Output: 
**Output Type:** Audio  <br>
**Output Format:** Audio of shape (batch x time) in wav format  <br>
**Output Parameters:** Mono, PCM-encoded 16 bit audio; sampling rate of 22.05 kHz; 20 Second Maximum Length; Depending on input, this model can output a female or a male voice for English US with two (2) emotions for the female voice and six (6) emotions for male voices.  The female voice is classified as “neutral” and “calm.”  The male voice is classified as “neutral,” “calm,” “happy,” and “fearful”, “sad”, and “angry.”  <br>

## Software Integration:
**Runtime Engine(s):** Riva 2.19.0 or greater <br>

**Supported Hardware Platform(s):** <br>
* NVIDIA Turing T4 <br>
* NVIDIA A100 GPU <br>
* NVIDIA A30 GPU <br>
* NVIDIA A10 GPU <br>
* NVIDIA H100 GPU <br>
* NVIDIA L4 GPU <br>
* NVIDIA L40 GPU <br>

**Supported Operating System(s):** <br>
* Linux <br>

## Inference

**Engine:** Triton <br>
**Test Hardware:** <br>
* NVIDIA Turing T4 <br>
* NVIDIA A100 GPU <br>
* NVIDIA A30 GPU <br>
* NVIDIA A10 GPU <br>
* NVIDIA H100 GPU <br>
* NVIDIA L4 GPU <br>
* NVIDIA L40 GPU <br>

## Model Version(s): 
magpie-tts-zeroshot v1<br>

## Ethical Considerations (For NVIDIA Models Only):
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## GOVERNING TERMS: 
This trial is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). The use of this model is governed by the [AI Foundation Models Community License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/)

## Capabilities

- **Function Calling:** Not supported

## Bias

Field  |  Response
:------|:----------
What is the language balance of the model validation data?  |  US English: 58%,Spanish (North America) 15%, 27% French (France)
What is the geographic origin language balance of the model validation data?  |  Unknown
What is the accent balance of the model validation data?  |  Unknown 
Measures taken to mitigate against unwanted bias:  |  This model was trained on a variety of languages and accents, including: US English, French, German, Italian, European Spanish, Dutch, Polish, and Brazilian Portuguese.
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing:  |  None

## Explainability

Field  |  Response
:------|:----------
Intended Application & Domain:  |  Speech Synthesis
Model Task  |  Speech Synthesis 
Intended Users  |  This model is intended for developers building interactive call centers, virtual assistants, and language learning assistants to improve pronunciation, automatically generate voice-overs, narrate or comment on videos, and/or provide audio alternatives for visually impaired users or people with light sensitivity.
Model Output  |  Speech codes (passed onto Codec model to decode and create audio files (.wav)).
How the model works | This model synthesizes input text characters into audio representation.
Technical Limitations  |  This model only has the capacity to produce a voice in the language, dialect and gender(s) in which it is trained.  This model makes no effort to moderate or modify input text. 
Performance Metrics  |  % preference when compared with available alternatives<br>word error rate(wer)<br>character error rate(cer)<br>mean opinion score (MOS)
Potential Known Risks  |  This model may unnaturally synthesize vocabulary not included in the pronunciation dictionary or omit phonetic symbols not used in training. This model may insert unexpected words or phonemes. 
Licensing:  |  [https://docs.nvidia.com/ai-foundation-models-community-license.pdf](https://docs.nvidia.com/ai-foundation-models-community-license.pdf)

## Privacy

Field  |  Response
:------|:---------
Generatable or reverse engineerable personal data?  |  None
Personal data used to create this model? |  Yes - Voice
Was consent obtained for any personal data used? Yes
How often is the dataset reviewed?  |  Before release (during training)
Is a mechanism in place to honor data subject right of access or deletion of personal data?  |  Yes
If personal data collected for the development of the model, was it collected directly by NVIDIA?  |  Yes
If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  Yes
If personal data collected for the development of this AI model, was it minimized to only what was required?  |  Yes
Is there provenance for all datasets used in training?  |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?  |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?  |  Yes

## Safety & Security

Field  |  Response
:------|:---------
Model Application(s):  |  Speech synthesis
Describe the life critical impact (if present).  |  Not Applicable
Model and dataset restrictions:  |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to.
Use case restrictions for the model.  |  Abide by [https://developer.nvidia.com/riva/ga/license](https://developer.nvidia.com/riva/ga/license)