---
title: "Background Noise Removal"
publisher: "nvidia"
type: "endpoint"
updated: "2025-06-13T17:42:41.479Z"
description: "Removes unwanted noises from audio improving speech intelligibility."
canonical: "https://build.nvidia.com/nvidia/bnr"
---

# Model Overview

### Description:

Background Noise Removal (BNR) is an audio background noise removal model 
from NVIDIA. BNR removes unwanted noises from audio, which improves speech 
intelligibility and also improves the speech recognition accuracy of 
various ASR systems under noisy environments.  

This model is ready for commercial use.  

### License/Terms of Use:

Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).  

### Deployment Geography:

Global  

## Model Architecture

**Architecture Type:** Residual Convolutional Recurrent Neural Network (CRNN)  
**Network Architecture:** SEASR  
**Number of model parameters:** ~60M  

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
systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software 
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

BNR v2.1  

# Training, Testing, and Evaluation Datasets

**Data Modality:**
* Audio

**Audio Training Data Size:**
* Less than 10,000 Hours

NVIDIA models are trained on a diverse set of public and proprietary datasets.
The BNR 2.0 model is trained on a wide range of English language accents, 
some European and Asian languages, and 29 different noise profiles that are 
commonly audible in the real world. 

**Data Collection Method by dataset:** [Hybrid: Human, Synthetic]  

**Labeling Method by dataset:** [Hybrid: Human, Synthetic]  

**Link:** [AudioSet](https://research.google.com/audioset/)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
AudioSet consists of an expanding ontology of 632 audio event classes and 
a collection of 2,084,320 human-labeled 10-second sound clips drawn from 
publicly available internet scale data.  

**Link:** [CREMA-D](https://www.kaggle.com/ejlok1/cremad)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
CREMA-D is a data set of 7,442 original clips from 91 actors. These clips were 
from 48 male and 43 female actors between the ages of 20 and 74 coming from a 
variety of races and ethnicities (African American, Asian, Caucasian, Hispanic, 
and Unspecified). Actors spoke from a selection of 12 sentences. The sentences 
were presented using one of six different emotions (Anger, Disgust, Fear, Happy,
Neutral, and Sad) and four different emotion levels (Low, Medium, High, and 
Unspecified).  

**Link:** [Crowdsourced high-quality UK and Ireland English Dialect speech data set](https://www.openslr.org/83/)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
The dataset contains male and female high quality recordings of English from
various dialects of the UK and Ireland for a total of 17,877 lines.  

**Link:** [CSR-I WSJ0](https://catalog.ldc.upenn.edu/LDC93S6A)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
Corpus by the DARPA Spoken Language Program to support research on large-
vocabulary Continuous Speech Recognition (CSR) systems. The first two CSR 
Corpora consist primarily of read speech with texts drawn from a machine-
readable corpus of Wall Street Journal news text and are thus often known as 
WSJ0 and WSJ1. WSJ0 consists of 123 speakers.  

**Link:** [CSTR VCTK](https://datashare.ed.ac.uk/handle/10283/3443)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
This CSTR VCTK Corpus includes speech data uttered by 110 English speakers with
various accents. Each speaker reads out about 400 sentences, which were selected
from a newspaper, the rainbow passage and an elicitation paragraph used for the
speech accent archive.  

**Link:** [DAPS](https://ccrma.stanford.edu/~gautham/Site/daps.html)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
The DAPS dataset has 15 versions of audio (3 professional versions and
12 consumer device/real-world environment combinations). Each version consists
of about 4.5 hours of data (about 14 minutes from each of 20 speakers).  

**Link:** [DEMAND](https://zenodo.org/records/1227121)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
The DEMAND (Diverse Environments Multichannel Acoustic Noise Database) 
contains a set of recordings that allow testing of algorithms using 
real-world noise in a variety of settings. This version provides 15 recordings. 
All recordings are made with a 16-channel array, with the smallest distance 
between microphones being 5 cm and the largest being 21.8 cm. It is a collection 
of multichannel recordings of accoustic noise in diverse environments.  

**Link:** [Edinburgh 56 speaker dataset](https://datashare.ed.ac.uk/handle/10283/2791)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
Clean and noisy parallel speech database from 56 speakers designed to train and 
test speech enhancement methods that operate at 48kHz.  

**Link:** [FreeField](https://archive.org/details/freefield1010)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
A dataset of standardised 7690 10-second excerpts from Freesound field recordings.  

**Link:** [Freesound](https://freesound.org/)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
Freesound is a collaborative collection of 620,291 free sounds which contains 
speakers speaking in different emotions as well as female speakers speaking in 
high pitched voices. The audio data also contains few noise profiles too.  

**Link:** GTC Dataset  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
A collection of talks from NVIDIA GTC Conferences with a total of 103 speakers.  

**Link:** [HiFi-TTS](https://www.openslr.org/109/)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
A multi-speaker English dataset for training text-to-speech models. 
The HiFi-TTS dataset contains about 291.6 hours of speech from 10 speakers 
with at least 17 hours per speaker sampled at 44.1 kHz.  

**Link:** [LibriTTS](https://www.openslr.org/60/)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
LibriTTS is a multi-speaker English corpus of approximately 585 hours of read
English speech by 200 speakers, which is resampled at 16kHZ.  

**Link:** [Vocal set dataset](https://zenodo.org/record/1193957#.Xt9uVUUzaUl)  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):**  
VocalSet is a singing voice dataset consisting of 10.1 hours of monophonic 
recorded audio of professional singers demonstrating both standard and extended 
vocal techniques on all 5 vowels. Existing singing voice datasets aim to capture
a focused subset of singing voice characteristics, and generally consist of just
a few singers. VocalSet contains recordings from 20 different singers (9 male, 
11 female) and a range of voice types.  VocalSet aims to improve the state of 
existing singing voice datasets and singing voice research by capturing not only
a range of vowels, but also a diverse set of voices on many different vocal 
techniques, sung in contexts of scales, arpeggios, long tones, and excerpts.  

# Inference

**Acceleration Engine:** Tensor(RT), [Triton](https://developer.nvidia.com/triton-inference-server)  
**Test Hardware:** 
* T4, T10, A30, A100, A2, A10, A16, A40, L4, L40, H100, B40  
* RTX 4080, RTX 4090, RTX 5070, RTX 5080, RTX 5090  

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established
policies and practices to enable development for a wide array of AI applications.
When downloaded or used in accordance with our terms of service, developers
should work with their internal model team to ensure this model meets
requirements for the relevant industry and use case and addresses unforeseen
product misuse.  

For more detailed information on ethical considerations for this
model, please see the Model Card++ [Bias](bias), [Explainability](explainability),
[Safety & Security](safety-and-security), and [Privacy](privacy) Subcards.  

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns
[here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing:  |  Age (18+), Gender
Measures taken to mitigate against unwanted bias:                                                   |  Evaluated using internal, proprietary data mix to achieve similar key performance indicators.

## Explainability

| Field | Response |
|-------|----------|
| Intended Task/Domain: | Speech Enhancement |
| Model Type:                    | Background Noise Removal |
| Intended Users:                | Automatic Speech Recognition and Video Conference System Developers |
| Output:                        | Audio |
| Describe how the model works:  | This model segments out the background noises from the input noisy audio, retaining only speech for better intelligibility and improved ASR accuracy. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Age (18+), Gender |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics:                | Scale Invariant Signal-to-Noise Ratio Improvement (SI-SNRi), Virtual Speech Quality Objective Listener (VISQOL), Perceptual Evaluation of Speech Quality (PESQ), Latency, Throughput. |
| Technical Limitations & Mitigation: | The model may not handle noises below 5dB or lower SNR. While the model can also work for other types of noises and at lower SNRs, the output speech quality could vary. |
| Potential Known Risks: | The model may not detect and filter out all audio background noises. |
| Licensing: | [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/) |

## Privacy

| Field | Response |
|-------|----------|
| Generatable or reverse engineerable personal data? | No             |
| Personal data used to create this model?           | Yes            |
| Was consent obtained for any personal data used?   | Yes            |
| How often is dataset reviewed?                     | Before Release |
| Is a mechanism in place to honor data subject right of access or deletion of personal data?       | Yes |
| If personal data collected for the development of the model, was it collected directly by NVIDIA? | Yes, for some training data |
| If personal data collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects? | Yes |
| If personal data collected for the development of this AI model, was it minimized to only what was required? | Yes |
| Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model?     | No |
| Is there provenance for all datasets used in training?              | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | No, not possible with externally-sourced data. Yes, for Nvidia collected data. |
| Applicable Privacy Policy | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/ |

## Safety & Security

| Field | Response |
|-------|----------|
| Model Application(s):                             | Audio Denoising |
| Describe the life critical impact (if present):   | Not Applicable |
| Use Case Restrictions:                            | Abide by [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |
| Model and dataset restrictions:                   | The Principle of Least Privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |