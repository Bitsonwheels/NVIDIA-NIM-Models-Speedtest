---
title: "Studio Voice"
publisher: "nvidia"
type: "endpoint"
updated: "2025-06-13T14:12:57.045Z"
description: "Enhance input speech recorded with low-quality microphones in noisy or reverberant environments, producing studio-quality speech."
canonical: "https://build.nvidia.com/nvidia/studiovoice"
---

# Model Overview

### Description:

Studio Voice is a speech enhancement model from NVIDIA. Studio Voice enhances input speech recorded with low-quality microphones in noisy or reverberant environments, producing studio-quality speech. 

This model is ready for commercial use.  

### License/Terms of Use:

Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).  

### Deployment Geography:

Global  

### Use Case:
Studio Voice models removes microphone artifacts and room reverberations to produce studio quality voice. It is intended to be used by content developers and broadcasters.  

### Release Date:
NGC [03/16/2026] via [afx_studio_voice](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/maxine/models/afx_studio_voice)  

## Model Architecture

**Architecture Type:** Convolution Neural Networks (CNNs), Transformers, Generative Adversarial Networks (GANs)  
**Network Architecture:** Encoder-Decoder  
**Number of model parameters:** 183M  

## Input(s):

**Input Type(s):** Audio  
**Input Format(s):** PCM F32  
**Input Parameters:** One-Dimensional (1D)  
**Other Properties Related to Input:** Pulse Code Modulation (PCM) audio samples
with no encoding or pre-processing; 16kHz or 48kHz sampling rate required.  

## Output(s):

**Output Type(s):** Audio  
**Output Format:** PCM F32  
**Output Parameters:** One-Dimensional (1D)  
**Other Properties Related to Output:** PCM audio samples at input sampling rate
with no encoding or post-processing.  

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated 
systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software 
frameworks (e.g., CUDA libraries), the model achieves faster training and 
inference times compared to CPU-only solutions.   

## Software Integration

**Runtime Engine(s):**  
* Audio Effects 2.1.0

**Supported Hardware Microarchitecture Compatibility:**  
* NVIDIA Ampere  
* NVIDIA Blackwell  
* NVIDIA Hopper
* NVIDIA Lovelace  
* NVIDIA Turing  

**Preferred/Supported Operating System(s):**  
* Linux  
* Windows  

The integration of foundation and fine-tuned models into AI systems requires 
additional testing using use-case-specific data to ensure safe and effective 
deployment. Following the V-model methodology, iterative testing and validation
at both unit and system levels are essential to mitigate risks, meet technical 
and functional requirements, and ensure compliance with safety and ethical 
standards before deployment.  

This AI model can be embedded as an Application Programming Interface (API) call
into the software environment described above.

## Model Version(s)

StudioVoice v0.5.1   

## Training, Testing, and Evaluation Datasets

**Data Modality:**
* Audio

**Audio Training Data Size:**
* Less than 10,000 Hours

**Dataset partition:**
Training [80%], Testing [10%], Validation [10%]

NVIDIA models are trained on a diverse set of public and proprietary datasets.
The Studio Voice model is trained on a dataset that comprises of diverse 
English accents and different types of microphone devices.

**Data Collection Method by dataset:** [Hybrid: Human, Synthetic] 
**Labeling Method by dataset:** [Hybrid: Human, Synthetic] 

**Link:** [DAPS](https://ccrma.stanford.edu/~gautham/Site/daps.html)  
**Properties:**  
The DAPS dataset has 15 versions of audio (3 professional versions and
12 consumer device/real-world environment combinations). Each version consists
of about 4.5 hours of data (about 14 minutes from each of 20 speakers).  

**Link:** [LibriTTS](https://www.openslr.org/60/)  
**Properties:**  
LibriTTS is a multi-speaker English corpus of approximately 585 hours of read
English speech, which is resampled at 16kHZ.  

**Link:** [VCTK](https://datashare.ed.ac.uk/handle/10283/3443)  
**Properties:**  
This CSTR VCTK Corpus includes speech data uttered by 110 English speakers with
various accents. Each speaker reads out about 400 sentences, which were selected
from a newspaper, the rainbow passage and an elicitation paragraph used for the
speech accent archive.  

**Link:** [HiFi-TTS](https://www.openslr.org/109/)  
**Properties:**  
A multi-speaker English dataset for training text-to-speech models.
The HiFi-TTS dataset contains about 291.6 hours of speech from 10 speakers with
at least 17 hours per speaker sampled at 44.1 kHz.  

**Link:** [Device Recorded VCTK (DR-VCTK)](https://github.com/nii-yamagishilab/downloader-DR-VCTK-complete)  
**Properties:**  
Device recorded version of VCTK dataset on common consumer devices 
(laptop, tablet and smartphone) in office environment. This dataset contains 
109 English speakers with different accents. There are around 400 sentences 
available from each speaker. For this recording, 8 different microphones were 
used. This dataset contains around 250 Gb of re-recorded speech.  

**Link:** [Dataset of impulse responses from variable acoustics room Arni at Aalto Acoustic Labs](https://zenodo.org/records/6985104#.Y7_vv3ZBy3C)  
**Properties:**  
A dataset of impulse responses collected in the variable acoustics laboratory 
Arni at Acoustics Lab of Aalto University, Espoo, Finland. IRs of 5342 
configurations of sound absorption in Arni are included in the dataset. Each of 
them were measured using an omnidirectional sound source and 5 sound receivers. 
For each configuration, 5 impulse reponses (IRs) were captured. The total number
of measurements in the dataset is 132 037.  

**Link:** [Room Impulse Response and Noise Database](https://www.openslr.org/28/)  
**Properties:**  
A database of simulated and real room impulse responses, isotropic and
point-source noises. The audio files in this data are all in 16KHz sampling rate
and 16-bit precision.  

**Link:** [DNS Challenge 5](https://github.com/microsoft/DNS-Challenge/tree/2db96d5f75257df764a6ef66513b4b97bc707f30)  
**Properties:**  
Collated dataset of clean speech, noise and impulse response provided by 
Microsoft for the ICASSP 2023 Deep Noise Suppression Challenge.  

**Link:** [AudioSet](https://research.google.com/audioset/download.html)  
**Properties:**  
AudioSet consists of an expanding ontology of 632 audio event classes and 
a collection of 2,084,320 human-labeled 10-second sound clips drawn from 
publicly available internet scale data.  

**Link:** Multi-Language and Emotions Speech Dataset  
**Properties:**  
Multi-Language and Emotions Speech Dataset contains high quality
speech data worth approximately 140 hours and contains approximately 80 unique
speakers. The dataset contains different english accents and contains
different emotions as well. This dataset is taken from publicly available
internet scale data. 

**Link:** Audio2Gesture Bones Dataset  
**Properties:**  
Audio2Gesture Bones Dataset is a speech dataset which is bought from Bones.studio 
company. It contains only 2 speakers covering all different types of emotions.
It is a small dataset of around 4 GB and contains 7 hours of speech data.

### Testing Datasets

**Data Collection Method by dataset:** [Hybrid: Human, Synthetic]  
**Labeling Method by dataset:** [Hybrid: Human, Synthetic]

**Properties:**

The Studio Voice model is tested on a dataset that comprises of diverse
English accents and different types of microphone devices. Test data is taken by sampling
10% of the training dataset mentioned above. The modality and data type is same as that of
the training dataset.

### Evaluation Datasets

**Data Collection Method by dataset:** [Hybrid: Human, Synthetic]  
**Labeling Method by dataset:** [Hybrid: Human, Synthetic]

**Properties:**

The Studio Voice model is evaluated on a dataset that comprises of diverse
English accents and different types of microphone devices. Evaluation data is taken by sampling
10% of the training dataset mentioned above. The modality and data type is same as that of
the training dataset.

## Inference

**Acceleration Engine:** Tensor(RT), [Triton](https://developer.nvidia.com/triton-inference-server)  
**Test Hardware:**  
* T4, T10, A30, A100, A2, A10, A16, A40, L4, L40, H100, B40, B100  
* RTX 4080, RTX 4090, RTX 5070, RTX 5080, RTX 5090   

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established
policies and practices to enable development for a wide array of AI applications.
When downloaded or used in accordance with our terms of service, developers
should work with their internal model team to ensure this model meets
requirements for the relevant industry and use case and addresses unforeseen
product misuse.

For more detailed information on ethical considerations for this
model, please see the Model Card++ Bias, Explainability,
Safety & Security, and Privacy Subcards.  

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns
[here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

| Field | Response |
|-------|----------|
| Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing: | Age (18+), Gender |
| Measures taken to mitigate against unwanted bias: | Evaluated using internal, proprietary data mix to achieve similar key performance indicators. |

## Explainability

| Field | Response |
|-------|----------|
| Intended Task/Domain:          | Voice Enhancement |
| Model Type:                    | Speech Enhancement |
| Intended Users:                | Content developers and Broadcasters |
| Output:                        | Audio |
| Describe how the model works:  | This model enhances the voice in input audio by removing acoustic noise, room reverberation, and bad frequency characteristics of the recording device while maintaining the linguistic and vocal properties. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Age (18+), Gender |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics:                 | Quality Mean Opinion Score (MOS), Non-Intrusive Speech Quality Assessment (NISQA), Latency, Throughput. |
| Technical Limitations & Mitigation: | The model may not work well on a variety of demographic and regional representations of English or with very noisy or very low quality inputs. Exclamatory emotions may not be transferred to the output. |
| Potential Known Risks: | The model may not preserve some speaker characteristics like pitch/fundamental frequency of the speakers voice and might also impact intelligibility of speech. |
| Licensing: | [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/) |

## Privacy

| Field | Response |
|-------|----------|
| Generatable or reverse engineerable personal data?  | No |
| Personal data used to create this model?            | Yes |
| Was consent obtained for any personal data used?    | Yes |
| How often is dataset reviewed?                      | Before Release |
| Is a mechanism in place to honor data subject right of access or deletion of personal data? | Yes |
| If personal data collected for the development of the model, was it collected directly by NVIDIA?     | No |
| If personal data collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects? | NO |
| If personal data collected for the development of this AI model, was it minimized to only what was required? | Yes |
| Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model? | No |
| Is there provenance for all datasets used in training?              | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | No, not possible with externally-sourced data. |
| Applicable Privacy Policy | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/ |

## Safety & Security

|  Field  |  Response  |
|---------|------------|
| Model Application(s):                             | Speech Enhancement |
| Describe the life critical impact (if present):   | Not Applicable |
| Use Case Restrictions:                            | Abide by [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |
| Model and dataset restrictions:                   | The Principle of Least Privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |