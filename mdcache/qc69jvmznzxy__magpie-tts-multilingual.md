---
title: "magpie-tts-multilingual"
publisher: "nvidia"
type: "endpoint"
updated: "2025-06-26T19:40:46.733Z"
description: "Natural and expressive voices in multiple languages. For voice agents and brand ambassadors."
canonical: "https://build.nvidia.com/nvidia/magpie-tts-multilingual"
---

Overview
# Speech Synthesis: Magpie TTS Multilingual Model Overview

### Description:
The model is an end-to-end multilingual neural text-to-speech model that generates speech in twelve different languages (English-US, European-Spanish, German-German, French-France, Italian, Vietnamese, Mandarin-Chinese, Hindi, Japanese, Modern Standard Arabic, Brazilian Portuguese, and Korean) by predicting discrete audio codec tokens autoregressively using a transformer encoder-decoder architecture. It supports at least one male and one female speaker for all the languages. It employs multi-codebook prediction (typically 8 codebooks) with local transformer refinement and frame stacking (factor = 2) for high-quality audio generation, and leverages techniques like attention priors, classifier-free guidance (CFG), and Group Relative Policy Optimization (GRPO) for improved alignment and robustness. This release also includes a zero-shot inference fix, IPA grapheme-to-phoneme (G2P) support for custom dictionaries and code-switching, and updated G2P support for English-to-Katakana code-switching. The model supports both batch inference for complete utterances and long-form inference for very long text inputs with sliding window mechanisms. The generated codecs are then converted to a speech waveform using a frozen pretrained audio codec model.
<br>

This model is ready for commercial use.  <br>

### License/Terms of Use:

GOVERNING TERMS: The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and the [Product-Specific Terms for NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/); and the use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). <br> 

### Deployment Geography:
Global <br>

### Use Case: <br>
For streaming voice agent use-cases, For Offline speech generation from text, In multiple languages. <br>

### Release Date:  <br>
Build.Nvidia.com [06/22/2026] via [https://build.nvidia.com/nvidia/magpie-tts-multilingual] <br> 
NGC [06/22/2026] via [https://registry.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/magpie-tts-multilingual] <br>

## References(s):
TTS model papers:
- [Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance](https://arxiv.org/abs/2502.05236)
- [Improving Robustness of LLM-based Speech Synthesis by Learning Monotonic Alignment](https://arxiv.org/abs/2406.17957)

Audio codec paper:
- [Low Frame-rate Speech Codec: A Codec Designed for Fast High-quality Speech LLM Training and Inference](https://arxiv.org/abs/2409.12117) <br> 

## Model Architecture:
**Architecture Type:** Transformer Encoder, Transformer Decoder, Local Transformer, and feedforward layers <br>

**Network Architecture:** 

1. Causal Transformer Encoder with 6 layers, learnable positional encoder of length 2048, and 1 Layer Normalization output layer. 

2. Causal Transformer Decoder with 12 layers, learnable positional encoder of length 2048, and 1 Layer Normalization output layer.

3. Local Transformer for multi-codebook refinement, operating on stacked frames with a frame stacking factor of 2 to improve audio quality and reduce sequence length. <br>

** Number of model parameters: 3.64 × 10^8 (364 M parameters) <br>

**Inference Configuration:**
- Decoding: `decoder-ce-context` with GRPO-aligned weights
- Classifier-free guidance: `cfg_scale = 2.5`
- Sampling: `temperature = 0.6`, `top_k = 80`
- Attention prior: `apply_attention_prior = True`, `prior_epsilon = 0.1`, `estimate_alignment_from_layers = [4, 5, 8, 9]`, `apply_prior_to_layers = [2, 3, 4, 5, 6, 7, 8, 9, 10]`, `start_prior_after_n_audio_steps = 0` <br>

## Computational Load (Internal Only: For NVIDIA Models Only) 
**Computational Load:** 1.62 × 10²¹ FLOP <br>
**Cumulative Compute:** ~2,230 kWh <br>
**Estimated Energy and Emissions for Model Training:** ~0.72 tCO2e <br>

## Input(s): <br>
**Input Type(s):** Text, Audio (optional reference utterance for zero-shot voice cloning) <br>

**Input Format(s):**
- Text: Strings
- Audio: WAV <br>

**Input Parameters:**
- Text: One-Dimensional (1D)
- Audio: One-Dimensional (1D) <br>

**Other Properties Related to Input:** Text input is UTF-8 encoded; text normalization is required. Audio reference (when provided for voice cloning) is mono, PCM-encoded 16-bit WAV at a sampling rate of 22.05 kHz; recommended reference duration is between 3 and 10 seconds. <br>

## Output(s)

**Output Type(s):** Audio <br>

**Output Format(s):** 
- Audio: WAV <br>

**Output Parameters:** 
- Audio: One-Dimensional (1D) <br>

**Other Properties Related to Output:** Mono, PCM-encoded 16 bit audio; sampling rate of 22.05 kHz; Audio output with dimensions (B x T), where B is batch size and T is time dimension. <br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. <br> 

## Software Integration:
**Runtime Engine(s):** 
* Riva 2.15.0 <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere
- NVIDIA A100 GPU
- NVIDIA A30 GPU
- NVIDIA A10 GPU <br>
* NVIDIA Hopper
- NVIDIA H100 GPU <br>
* NVIDIA Lovelace
- NVIDIA L4 GPU
- NVIDIA L40 GPU <br>

**Preferred/Supported Operating System(s):**
* Linux <br>
* Linux 4 Tegra <br>

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment. <br>

## Model Version(s):
RivaTTS_MagpieTTS_Multilingual v4.0 <br> 

## Training and Evaluation Datasets:

## Training Dataset:
The following datasets were used to train the model, including additional datasets focused on speech and ASR.

**English (En):**
* HiFiTTS En: [link](https://www.openslr.org/109/)<br>
* HiFiTTS-2 A Large-Scale High Bandwidth Speech Dataset En: [link](https://huggingface.co/datasets/nvidia/hifitts-2)<br>
* LibriTTS En: [link](https://www.openslr.org/60/)<br>
* GLOBE_V2 En (multi-accent): [link](https://huggingface.co/datasets/MushanW/GLOBE_V2)
* DavidAI En: Internal Dataset
* Jensen Huang 2020 Keynote En: Internal Dataset
* RIVA Speakers En: Internal Dataset
* Publicly available internet-scale data En: Internal Dataset

**German (De):**
* CML-TTS De: [Link](https://www.openslr.org/146/)
* King-ASR-182 De: [Link](https://dataoceanai.com/datasets/asr/german-speech-recognition-corpus-desktop-2/)

**Spanish (Es):**
* CML-TTS Es: [Link](https://www.openslr.org/146/)
* ESP_ASR003 Es: Internal Dataset
* Riva Speakers Es: Internal Dataset

**French (Fr):**
* CML-TTS Fr: [Link](https://www.openslr.org/146/)
* Riva Speakers Fr: Internal Dataset

**Italian (It):**
* CML-TTS It: [Link](https://www.openslr.org/146/)
* MLS-Sidon It: [Link](https://huggingface.co/datasets/sarulab-speech/mls_sidon)

**Hindi (Hi):**
* AI4Bharat Kathbath Hi: [link](https://huggingface.co/datasets/ai4bharat/Kathbath)
* Hindi-English (MUCS) Hi: [Link](https://www.openslr.org/104/)
* Publicly available internet-scale data Hi: Internal Dataset

**Japanese (Ja):**
* Common Voice Ja: [Link](https://commonvoice.mozilla.org/)
* Emilia YODAS Ja: [Link](https://huggingface.co/datasets/amphion/Emilia-Dataset)
* Emilia YODAS Ja-En (code-switching): [Link](https://huggingface.co/datasets/amphion/Emilia-Dataset)
* Japanese Anime Speech Ja: [Link](https://huggingface.co/datasets/joujiboi/japanese-anime-speech)
* PlacesJapanese100k Ja: [Link](https://zenodo.org/records/5563425)
* King-ASR-444 Ja: [Link](https://dataoceanai.com/datasets/asr/japanese-conversational-speech-recognition-corpus-mobile/)

**Mandarin Chinese (Zh):**
* AISHELL-3 Zh: [Link](https://www.openslr.org/93/)
* THCHS-30 Zh: [Link](https://www.openslr.org/18/)
* Emilia YODAS Zh: [Link](https://huggingface.co/datasets/mrfakename/Emilia-YODAS)
* RIVA Speakers Zh: Internal Dataset
* Publicly available internet-scale data Zh: Internal Dataset

**Vietnamese (Vi):**
* InfoRe-1 Vi: [Link](https://huggingface.co/datasets/doof-ferb/infore1_25hours)
* Riva Speakers Vi: Internal Dataset
* Publicly available internet-scale data Vi: Internal Dataset

**Brazilian Portuguese (pt-BR) — NEW:**
* TTS-Portuguese-Corpus pt-BR: [Link](https://github.com/Edresson/TTS-Portuguese-Corpus)
* pt-br_char pt-BR: [Link](https://huggingface.co/datasets/firstpixel/pt-br_char)
* CML-TTS pt-BR: [Link](https://openslr.org/146/)

**Arabic — Modern Standard Arabic (ar_MSA) — NEW; also includes Saudi Arabia (ar_SA), UAE (ar_AE), and Damascene (ar_SY) accents:**
* Common Voice Arabic: [Link](https://huggingface.co/datasets/MohamedRashad/common-voice-18-arabic)
* ArVoice Ar: [Link](https://huggingface.co/datasets/MBZUAI/ArVoice)
* YodaLingua Ar: [Link](https://huggingface.co/collections/Thomcles/yodalingua)
* Arabic Speech Corpus ar_SY: [Link](https://huggingface.co/datasets/tunis-ai/arabic_speech_corpus)
* King-ASR-109 ar_AE: [Link](https://dataoceanai.com/datasets/asr/uae-arabic-speech-recognition-corpus-corpus-desktop/)
* ClArTTS ar_SA: [Link](https://huggingface.co/datasets/MBZUAI/ClArTTS)
* King-ASR-318 ar_SA: [Link](https://dataoceanai.com/datasets/asr/arabic-saudi-arabia-speech-recognition-corpus-desktop/)
* Publicly available internet-scale data Ar: Internal Dataset

**Korean (Ko) — NEW:**
* Emilia YODAS Ko: [Link](https://huggingface.co/datasets/seastar105/Emilia-YODAS-KO-filtered)
* Zeroth-Korean Ko: [Link](https://www.openslr.org/40/)

**Data Modality** <br>
* [Audio] <br>

<!-- xlsx May 26 tab total: 54,304.66 hours -->
**Audio Training Data Size** <br>
* 54,305 Hours <br>

**Data Collection Method by dataset** <br>
* [Human] <br>

**Labeling Method by dataset** <br>
* [Hybrid: Human, Synthetic] - Human recorded data points were preprocessed algorithmically. <br>

**Properties:** 
Number of data items in training set: ~54.3k hours
Modality: Audio (speech signal)
Nature of the content: Audio books, conversational speech, and read speech
Language: Multilingual (En, Es, De, Fr, Vi, It, Zh, Hi, Ja, Ar, pt-BR, Ko)
Sensor Type: Microphones <br>

### Evaluation Dataset:
* LibriTTS test-clean En: [link](https://www.openslr.org/60/)<br>
* CML-TTS Es: [Link](https://www.openslr.org/146/)<br>
* CML-TTS Fr: [Link](https://www.openslr.org/146/)<br>
* CML-TTS De: [Link](https://www.openslr.org/146/)<br>
* CML-TTS It: [Link](https://www.openslr.org/146/)<br>
* CML-TTS pt-BR: [Link](https://openslr.org/146/)<br>
* English accent test set (derived from GLOBE_V2): [Link](https://huggingface.co/datasets/MushanW/GLOBE_V2)<br>
* Internal Mandarin, Hindi, Japanese, Vietnamese, Arabic (MSA), and Korean test sets<br>

Data Collection Method by dataset:  <br>
* [Human] <br>

Labeling Method by dataset:  <br>
* [Human] <br>
* [Hybrid: Human, Synthetic] - Human labeled data points are mixed and matched to create more variabilities. <br>

**Properties:** 
Modality: Audio (speech signal)
Nature of the content: Audio books, conversational speech, and newspaper passages
Language: Multilingual (En, Es, De, Fr, Vi, It, Zh, Hi, Ja, Ar, pt-BR, Ko)
Sensor Type: Microphones <br>

|                       | CER (%) | SV-SSIM (%) |
| --------------------- | ------- | ----------- |
| English (LibriTTS)    |  0.34   |  82.79      |
| English Accents       |  0.33   |  76.31      |
| Spanish CML           |  0.51   |  78.18      |
| German CML            |  0.86   |  75.05      |
| French CML            |  1.07   |  74.30      |
| Italian               |  1.78   |  78.50      |
| Vietnamese            |  0.41   |  75.34      |
| Mandarin              |  2.49   |  83.13      |
| Hindi                 |  1.23   |  78.71      |
| Japanese              |  1.17   |  77.57      |
| Arabic (MSA)          |  1.63   |  80.32      |
| Korean                |  2.57   |  81.23      |
| Brazilian Portuguese  |  3.46   |  76.79      |

Lower CER is better; higher SV-SSIM is better. MagpieTTS 4.0 (May 2026) shows CER and SV-SSIM improvements over MagpieTTS 3.1 across all previously supported languages, with the largest CER gains on Mandarin, French, and Italian. The English hard-set evaluation shows a substantial improvement on short prompts (CER reduced from 4.0% to 1.2%) while remaining comparable on Money, Digits, and Letters categories.

# Inference:
**Acceleration Engine:** Triton <br>
**Test Hardware:** <br>  
* NVIDIA A100 GPU <br>
* NVIDIA A30 GPU <br>
* NVIDIA A10 GPU <br>
* NVIDIA H100 GPU <br>
* NVIDIA L4 GPU <br>
* NVIDIA L40 GPU <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br> 

For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards. <br> 

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).  <br>

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response 
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing:  |  None
Bias Metric (If Measured):                                                   |  None
Measures taken to mitigate against unwanted bias: | None

## Explainability

Field                                                                                                  |  Response 
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Task/Domain:                                                                                  |  Text to Speech
Model Type:                                                                                            |  Causal Transformer Encoder, Causal Transformer Encoder
Intended Users:                                                                                        |  People working with conversational AI models that need to generate speech from text for a single speaker.
Output:                                                                                                |  Speech
Describe how the model works:                                                                          |  MagpieTTS is a text-to-speech model that synthesizes speech from input text, conditioned on an audio prompt embedding that captures the target speaker's acoustic characteristics. The model autoregressively predicts discrete audio codec tokens using a transformer encoder-decoder, with a Local Transformer refining the multi-codebook predictions and frame stacking (factor = 2) reducing sequence length. The model supports two inference modes: standard and long-form. In standard mode, the entire input text is passed through the encoder. The encoder output is concatenated with the audio prompt embedding and fed to the decoder, which autoregressively generates the corresponding speech. In long-form mode, the input text is split into sentences, each processed independently while maintaining a rolling window of prior text and attention states. This preserves prosodic continuity across sentence boundaries.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Not Applicable
Technical Limitations & Mitigation:                                                                    |  There are two modes of inference, namely, standard and long-form. In standard mode, this model can generate up to thirty (30) seconds of multilingual (En, Es, De, Fr, Vi, It, Zh, Hi, Ja, Ar, pt-BR, Ko) speech at a time. In long-form mode, the model performs optimally when the input text contains punctuation and capitalization. The model was trained on a mix of publicly available speech datasets and internally recorded datasets in twelve languages. As a result, it is not suitable for speech generation in any language other than the twelve languages mentioned. We have removed zero-shot capabilities of this model for security purposes. Text normalization is required.
Verified to have met prescribed NVIDIA quality standards:  |  Yes
Performance Metrics:                                                                                   |  character error rate (CER) and speaker verification model speaker similarity (SV-SSIM)
Potential Known Risks:                                                                                 |  In standard inference mode, if the input text is too long, the model might not produce speech. In long-form inference mode, if the input text does not contain punctuation and capitalization, the generated speech may not be 100% accurate.
Licensing:                                                                                             |  GOVERNING TERMS: The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and the [Product-Specific Terms for NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/); and the use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

## Privacy

## Privacy Information

Magpie TTS Multilingual 4.0 was trained on large-scale publicly available data that may contain images, audio-video, and text relating to people. NVIDIA collected and used this data in compliance with applicable data protection and privacy laws. This model was not designed to derive insights or otherwise learn from any personal data contained in the datasets.

NVIDIA uses a combination of filters, data minimization techniques, and other guardrails to help prevent personal data from being recited by our models. We employ automated tools and data processing techniques during pre-training or training to identify and filter certain categories of personal data.

Please review [NVIDIA's Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) for more information.

## Safety & Security

Field                                               |   Response
:---------------------------------------------------|:----------------------------------
Model Application Field(s):                               |  Single Speaker Text to Speech Systems 
Describe the life critical impact (if present).   |  Not Applicable 
Use Case Restrictions:                              |  Abide by GOVERNING TERMS: The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and the [Product-Specific Terms for NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/); and the use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).
Model and dataset restrictions:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to.