---
title: "whisper-large-v3"
publisher: "openai"
type: "endpoint"
updated: "2025-04-10T15:18:41.346Z"
description: "Robust Speech Recognition via Large-Scale Weak Supervision."
canonical: "https://build.nvidia.com/openai/whisper-large-v3"
---

# Model Overview

## Description:
This model is used to transcribe short-form audio files and is designed to be compatible with *OpenAI's sequential long-form transcription algorithm*. Whisper is a pre-trained model for automatic speech recognition (ASR) and speech translation. Trained on 680k hours of labeled data, Whisper models demonstrate a strong ability to generalize to many datasets and domains without the need for fine-tuning. Whisper-large-v3 is one of the 5 configurations of the model with 1550M parameters.<br>
This model version is optimized to run with NVIDIA TensorRT-LLM. This model is ready for commercial use.

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see the Whisper Model Card on GitHub.(https://github.com/openai/whisper/blob/main/model-card.md).

### License/Terms of Use: 

GOVERNING TERMS: Use of this model is governed by the [NVIDIA Community Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/).
ADDITIONAL INFORMATION: [MIT License](https://github.com/openai/whisper/blob/main/LICENSE).

## References:
Whisper [website](https://openai.com/index/whisper/) <br>
Whisper paper: <br>
```
@misc{radford2022robust,
title={Robust Speech Recognition via Large-Scale Weak Supervision}, 
author={Alec Radford and Jong Wook Kim and Tao Xu and Greg Brockman and Christine McLeavey and Ilya Sutskever},
year={2022},
eprint={2212.04356},
archivePrefix={arXiv},
primaryClass={eess.AS}
}
```

## Model Architecture: 
**Architecture Type:** Transformer (Encoder-Decoder) <br>
**Network Architecture:** Whisper <br>

## Input: 
**Input Type(s):** Audio, Text-Prompt <br>
**Input Format(s):** Linear PCM 16-bit 1 channel (Audio), String (Text Prompt) <br>
**Input Parameters:** One-Dimensional (1D) <br>

## Output:
**Output Type(s):** Text
**Output Format:** String
**Output Parameters:** 1D

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Blackwell <br>

**Supported Operating System(s):** <br>
* Linux <br>

## Model Version(s): 
**Large-v3:** Whisper large-v3 has the same architecture as the previous large and large-v2 models, except for the following minor differences:
- The spectrogram input uses 128 Mel frequency bins instead of 80.
- A new language token for Cantonese.

## Training Dataset:

**Data Collection Method by dataset:** [Hybrid: human, automatic] <br>

**Labeling Method by dataset:** [Automated] <br>

**Dataset License(s):** NA

## Inference:
**Engine:** Tensor(RT)-LLM, Triton <br>
**Test Hardware:**
- A100
- H100

For more detail on model usage, evaluation, training data set and implications, please refer to [Whisper Model Card](https://github.com/openai/whisper/blob/main/model-card.md).

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  
Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Specifications

- **Parameters:** 1,543,490,560

## Capabilities

- **Function Calling:** Not supported