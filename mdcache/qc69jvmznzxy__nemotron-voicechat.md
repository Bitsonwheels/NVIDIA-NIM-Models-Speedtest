---
title: "nemotron-voicechat"
publisher: "nvidia"
type: "endpoint"
updated: "2026-03-16T20:13:48.921Z"
description: "Nemotron 3 Voicechat"
canonical: "https://build.nvidia.com/nvidia/nemotron-voicechat"
---

# Model Overview

### Description:

NVIDIA Nemotron™ 3 VoiceChat is a 12B end-to-end, realtime full duplex speech-to-speech model for conversational AI that jointly performs streaming speech understanding and speech generation [1]. Unlike traditional cascaded stacks (ASR → LLM → TTS), this model achieves full duplex, real-time, seamless voice interaction in one unified architecture, eliminating the need for multiple models or API handoffs, reducing end-to-end latency.  
It sets new benchmarks by bringing open, robust, and highly natural conversation capabilities to enterprises. 

The model operates on audio signals, which are encoded using a fast conformer module. The resulting audio tokens are inputted into a Nemotron Nano V2 9B LLM backbone to predict text tokens, which are fed to a TTS decoder [2] to predict audio codes for generating the agent's speech. The model supports persona control through text-based role prompts based on NVIDIA PersonaPlex [3].
Nemotron 3 VoiceChat offers an unprecedented trade-off between intelligence and latency in the space of open source voice agents, as highlighted by our benchmarking results [below](#testingevaluation-dataset).

This model is ready for early access evaluation purposes only.

### License/Terms of Use:
GOVERNING TERMS: Your use of this API is governed by the [NVIDIA API Trial Service Terms of Use](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); use of NIM container and the use of this model is governed by the [NVIDIA Software and Model Evaluation License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-and-model-evaluation-license/).

### Use Case: <br>
Nemotron 3 VoiceChat is targeted for researchers, developers, and professionals in the field of natural language processing (NLP) and speech technology for purposes such as automatic speech recognition (ASR), text-to-speech synthesis (TTS), and voice assistant development.

### Deployment Geography:
Global

### Release Date:  <br>
NGC [03/16/2026] via [Nemotron Voicechat Model on NGC](https://registry.ngc.nvidia.com/orgs/nim/teams/nvidia/models/nemotron-voicechat) <br> 

## References(s):
[1] [SALM-Duplex: Efficient and Direct Duplex Modeling for Speech-to-Speech Language Model](https://arxiv.org/abs/2505.15670) <br> 
[2] [Audio Flamingo 3: Advancing Audio Intelligence with Fully Open Large Audio Language Models](https://arxiv.org/abs/2507.08128) <br>
[3] [PersonaPlex: Voice and role control for full duplex conversational speech models](https://research.nvidia.com/labs/adlr/files/personaplex/personaplex_preprint.pdf) <br>

## Model Architecture:
**Architecture Type:** Hybrid Mamba/Transformer <br>

**Network Architecture:** <br>

Nemotron VoiceChat uses:
* Fast Conformer Speech Encoder from [Nemotron-Speech-Streaming-En-0.6b](https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b)
* [NVIDIA Nemotron Nano v2 LLM backbone](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2)
* NVIDIA TTS decoder and codec [2]
* Number of model parameters: 12B <br>

## Input(s): <br>
**Input Type(s):** Text (prompt), Audio (user speech) <br>
**Input Format:** String, WAV/WebAudio <br>
**Input Parameters:** One-Dimensional (1D), One-Dimensional (1D) <br>
**Other Properties Related to Input:** 16 kHz sample rate for audio. <br>

## Output(s)
**Output Type(s):** Text (agent text), Audio (agent speech), Text (user speech transcription) <br>
**Output Format:** String, WAV/WebAudio <br>
**Output Parameters:** One-Dimensional (1D), One-Dimensional (1D), One-Dimensional (1D) <br>
**Other Properties Related to Output:** 22.05 kHz sample rate for audio. <br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. <br> 

## Software Integration:
**Runtime Engine:** vLLM <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Hopper (H100)

**Preferred/Supported Operating System(s):**
* Linux

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment. <br>

## Model Version(s):
* v1.0

## Training, Testing, and Evaluation Datasets:

### Training Dataset:

**Data Modality:** Audio (speech) and Text <br>
**Audio Training Data Size:** 10,000 to 1 Million Hours <br>

VoiceChat has been trained on a blend of different datasets comprising both real audio datasets and synthetic speech datasets generated using various TTS systems on text training corpora, including:

- Nemotron 5.5 pre-training and SFT text data
- Brainy-mantis text data
- Greteal AI v1 and v2 text data
- [Ultrachat text data](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k)
- Blackwell studio recordings real speech data
- [Fisher real speech data](https://catalog.ldc.upenn.edu/LDC2004S13)
- [LibriVox](https://librivox.org/)
- [LibriTTS](https://www.openslr.org/60/)
- [HiFi-TTS](https://www.openslr.org/109/)
- Riva Speakers: Internal Dataset
- Publicly available internet scale data
- [PromptTTS](https://speechresearch.github.io/prompttts/)
- [VCTK](https://datashare.ed.ac.uk/handle/10283/3443)
- [Voxmovies](https://mmai.io/datasets/voxmovies/)
- [JL-Corpus](https://huggingface.co/datasets/CLAPv2/JL-Corpus)
- Nemotron Nano v3 function calling data
- Persona Plex training datasets

**Data Collection Method by dataset:** Hybrid: Human, Synthetic, Automated. <br>
**Labeling Method by dataset:** Automated. <br>

### Testing/Evaluation Dataset:

#### VoiceBench

**Link:** [VoiceBench](https://github.com/MatthewCYM/VoiceBench) <br>
**Data Collection Method by dataset:** Hybrid: Human, Synthetic, Automated. <br>
**Labeling Method by dataset:** Automated. <br>
**Properties:** VoiceChat is #1 amongst all open full-duplex models on [VoiceBench](https://arxiv.org/abs/2410.17196), a benchmark dataset developed to evaluate large language model (LLM)-based voice assistants, focusing on real-world spoken interactions rather than just text or clean speech recognition. It combines audio and text data. The dataset includes multiple subsets covering tasks like open-ended questions, multiple-choice QA, instruction following, and adversarial cases - sourced from both real human speech and synthetic text-to-speech examples. <br>

**Benchmark Scores:** <br>

| Metric                                   | Value |
|------------------------------------------|-------|
| Text-output average accuracy             | 58.1  |

#### FullDuplexBench 1.0
**Link:** [FullDuplexBench 1.0](https://arxiv.org/abs/2503.04721) <br>
**Data Collection Method by dataset:** Hybrid: Human, Synthetic, Automated. <br>
**Labeling Method by dataset:** Automated. <br>
**Properties:** Nemotron 3 VoiceChat is #2 amongst all open models on [FullDuplexBench 1.0](https://arxiv.org/abs/2503.04721),which is a benchmark designed to evaluate the interactive capabilities of full-duplex spoken dialogue models like VoiceChat. It focuses on measuring natural, human-like conversational behaviors such as pause handling, backchanneling, smooth turn-taking, and user interruption management, using automatic metrics to provide consistent, reproducible assessments of model performance. <br>

**Benchmark Scores:** <br>
| Metric                                   | Value |
|------------------------------------------|-------|
| Pause Handling(Synthetic): TOR↓          | 0.55  |
| Pause Handling(Candor): TOR↓             | 0.69  |
| Smooth Turn Taking: TOR↑                 | 1.00  |
| Smooth Turn Taking: Latency↓             | 0.26  |
| User Interruption: TOR↑                  | 1.00  |
| User Interruption: GPT-4o↑               | 4.18  |

[Artificial Analysis](https://artificialanalysis.ai/models/speech-to-speech) shows Nemotron 3 VoiceChat is the best open model as balanced for conversational dynamics and speech reasoning amongst all open models. 

# Inference:
**Acceleration Engine:** vLLM <br>
**Test Hardware:** NVIDIA H100 <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards. <br> 

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing:  |  None
Measures taken to mitigate against unwanted bias:                                                   |  None
Bias Metric (If Measured):                                                   |  [BBQ Accuracy Scores in Ambiguous Contexts](https://github.com/nyu-mll/BBQ/)
Which feature(s) have the worst performance overall |                          Socio-Economic Status and Race/Ethnicity
Measures taken to mitigate against unwanted bias:| Supervised Fine-Tuning (SFT) employed to calibrate the model’s reasoning capabilities to maintain logical consistency and appropriate complexity when interacting with or interpreting data from diverse demographics.
Unwanted Bias Testing: | Constrained to English-language inputs. Multi-lingual parity is not currently claimed or guaranteed.

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Task/Domain:                                                                   |  Speech To Speech Conversational Chat Agent 
Model Type:                                                                                            |  Speech Encoder (Fast Conformer), Nemotron Nano v2 LLM backbone (hybrid Mamba/Transformer), TTS Speech Decoder (ConvNet, Transformer)
Intended Users:                                                                                        |  Nemotron VoiceChat is targeted for researchers, developers, and professionals in the field of natural language processing (NLP) and speech technology for purposes such as automatic speech recognition (ASR), text-to-speech synthesis (TTS), and voice assistant development.
Output:                                                                                                |  Speech, Text
Describe how the model works:                                                                          |  Nemotron Nemotron VoiceChat is a real-time speech-to-speech conversational model that jointly performs streaming speech understanding and speech generation. The model operates on continuous audio encoded using a fast conformer module before the resulting audio tokens are handed to a Nemotron nano V2 9b LLM backbone to predict text tokens which are fed to a TTS decoder [2] generating the agent's speech.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age, Disability Status, Gender Identity, Nationality, Physical Appearance, Ethnicity, Socioeconomic Status, Sexual Orientation, Religion
Technical Limitations & Mitigation:                                                                    |  This model is trained with audio context windows of up to 2 minutes, and as such, conversational context beyond this duration may not be reliably preserved.
Nemotron VoiceChat has been optimized to achieve a trade-off between general knowledge and natural conversation, hence it may not be as performant as the LLM backbone it is derived from, namely NVIDIA Nemotron Nano v2, in terms of knowledge, instruction-following capabilities and safety.
Nemotron VoiceChat was not explicitly trained for reasoning or alignment. Its performance on tasks requiring multi-step reasoning, arithmetic, or safety-aligned behavior may therefore be limited. Further, the model may not yet properly handle user interruptions and backchannelling. Finally, the model is not suitable for noisy or highly reverberant environments, especially where background speech may occur.
Verified to have met prescribed NVIDIA quality standards:  |  Yes
Performance Metrics:                                                                                   |  Knowledge performance metrics include accuracy (%), GPT-scores (1-5) and refusal rate (%).<br>Conversational dynamics metrics include takeover rate (TOR); latency (seconds) for interruptions, pause handling, and turn-taking; frequency and Jensen–Shannon divergence (JSD) for backchannels; question-answering accuracy (score); and speaker similarity (SSIM).
Potential Known Risks:                                                                                 |  The model may present errors in speech understanding and/or pronunciation. The model is trained exclusively on English speech; the model does not support other languages at this time. The model's performance may degrade outside assistant-style or general chat scenarios. For privacy and security reasons, the model cannot generate voice prompts from real user voice recordings.The model was optimized explicitly for instruction following and as such may be influenced by untrusted inputs (prompt injection, indirect prompt injection, jailbreaking, web search, etc.) as a result of its instruction tuning that may degrade safety alignment and other training efforts. This model should be paired with additional guardrails and data filtering to limit exposure to instructions from malicious sources. Bypassing of safety alignment, system guardrails, and filters may allow harmful outcomes up to and including remote code execution in some agentic systems when effective security controls are not in place. The model was trained on data that contains toxic language and societal biases originally crawled from the internet. Therefore, the model may generate and amplify harmful, biased, or otherwise unsafe content reinforcing these biases and return toxic responses especially when prompted with toxic prompts. The model may also generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. The model may exhibit self-anthropomorphism (e.g., displaying human-like characteristics in dialogue, such as expressing preferences and emotions). In integrated system contexts, the model could potentially be exploited to access or disclose information beyond the model's intended permissions or scope of operation.
Licensing:                                                                                             |  GOVERNING TERMS: Your use of this API is governed by the [NVIDIA API Trial Service Terms of Use](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); use of NIM container and the use of this model is governed by the [NVIDIA Software and Model Evaluation License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-and-model-evaluation-license/).

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                     |  No
Personal data used to create this model?                                                                                       |  Yes - Voice
Was consent obtained for any personal data used?                                                                                             |  Yes
How often is dataset reviewed?                                                                                                     |  During dataset creation, model training, evaluation and before release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Yes
If personal data was collected for the development of the model, was it collected directly by NVIDIA?                                            |  No
If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  NA
If personal data was collected for the development of this AI model, was it minimized to only what was required?                                 |  Yes
Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model? |  No
Is there provenance for all datasets used in training?                                                                                |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  NA
Applicable Privacy Policy        | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/ 
Privacy Testing: | Constrained to English-language inputs. Multi-lingual parity is not currently claimed or guaranteed

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application Field(s):                               |  Speech To Speech Conversational Systems 
Describe the life critical impact (if present).   |  Not Applicable 
Use Case Restrictions:                              |  Abide by GOVERNING TERMS: Your use of this API is governed by the [NVIDIA API Trial Service Terms of Use](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); use of NIM container and the use of this model is governed by the [NVIDIA Software and Model Evaluation License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-and-model-evaluation-license/).
Model and dataset restrictions:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to.