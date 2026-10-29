---
title: "LipSync"
publisher: "nvidia"
type: "endpoint"
updated: "2026-04-16T18:31:52.434Z"
description: "Generative lip dubbing that syncs lips in a video to input audio."
canonical: "https://build.nvidia.com/nvidia/lipsync"
---

## LipSync

LipSync is a generative model to lip sync a video containing a human face to a target audio containing human speech such that the mouth movements of the generated video match with the speech in the provided audio.

The model takes a speech segment and an image containing a human face as input and morphs the lip movements to generate an image where lips sync with the input audio. The head pose, background and the quality of the output image are kept the same as the input image.

This model is ready for commercial use. To try out this model, you must join the Private Access Program. You may request access at [Private Access Program](https://developer.nvidia.com/topics/ai/generative-ai/ai-for-media/private-access).

### Using this model

To download the model, use the feature installation script bundled with the NVIDIA AR SDK (`features/install_feature.[ps1|sh]`). Please refer to the LipSync Collection page or the AR SDK Documentation for more details. You can navigate to the collection page by click on the **Related Collections** tab at the top of this page.

## License/Terms of use:

Use of the NVIDIA LipSync models is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

## Deployment Geography:

Global

## Use Case:

NVIDIA AR SDK developers for enabling LipSync capabilities to content localization workflows.

## Release Date:  

10/17/2025

## References(s):

[NVIDIA AR SDK Developer Page](https://developer.nvidia.com/ai-for-media)

## Model Architecture:
**Architecture Type:** Convolutional Neural Networks (CNNs), Generative Adversarial Networks (GANs)   <br>
**Network Architecture:** Encoder-Decoder   <br>
**Number of model parameters:** 6.13*10^8 <br>

## Input:
**Input Type(s):** Image, Audio <br>
**Input Format:** Float vector containing 32-bit float Pulse Code Modulation (PCM) data, RGB Image<br>
**Input Parameters:** Audio (1D), Image (2D)<br>
**Other Properties Related to Input:** Up to 4K image resolution. 16kHz sampling rate for audio. The input image should have 1 complete face and only 1 face. The input audio should have a single channel (mono). Input images are pre-processed using proprietary technique and PCM audio samples are expected without any encoding or pre-processing.<br>

## Output: 
**Output Type(s):** Image <br>
**Output Format:** Image: Red, Green, Blue (RGB) <br>
**Output Parameters:** 2D. Same resolution as input image. <br>
**Other Properties Related to Output:** Output images post-processed using proprietary technique to blend the lip synced face image to original frame.

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:

**Runtime Engine(s):**

NVIDIA AR SDK

**Supported Hardware Microarchitecture Compatability:**

* NVIDIA Ampere <br>
* NVIDIA Blackwell <br>
* NVIDIA Hopper <br>
* NVIDIA Lovelace <br>
* NVIDIA Turing <br> 

**Preferred/Supported Operating System(s):**

* Ubuntu 20.04 <br> 
* Ubuntu 22.04 <br> 
* Ubuntu 24.04 <br> 
* Debian 12 <br> 
* Rocky/RHEL 8.* <br> 
* Rocky/RHEL 9.* <br> 
* Windows 10 <br>
* Windows 11 <br>

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Training and Evaluation Dataset:

### Training Dataset:

**Datasets used:**
* VoxCeleb dataset  
* VFHQ dataset  
* HDVILA dataset  
* Synthetic dataset

**Data Modality:**
* Audio  
* Video  

**Audio Training Data Size:** <br>
Less than 10,000 Hours  

**Video Training Data Size:** <br>
Less than 10,000 Hours 

**Data collection method by dataset:** <br>
Automated <br>

**Labeling method by dataset:** <br>
Not Applicable <br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** <br>
Training dataset contains approximately 240,000 videos of different speakers in different environments such as outdoor recording, indoor recording, data covering different phonemes. It is made of audio-visual data consisting of short clips of human speech. <br>

### Evaluation Dataset:

**Datasets used:**
* Internal captures <br>
* YouTube videos <br>

**Data Collection Method by dataset:**  <br>
Hybrid: Automated and Human <br>

**Labeling method by dataset:** <br>
Not Applicable <br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**
Around 40 videos with various lengths of a single person in front of the camera conducting a video conference or broadcasting. The dataset varies in terms of quality, lighting, head pose, gaze angles and other diversity factors such as race, eye color, and gender. The audios in the videos have been translated to 5 languages. <br>

# Inference:
**Engine:** [TensorRT](https://developer.nvidia.com/tensorrt), [Triton](https://developer.nvidia.com/triton-inference-server) <br>
**Test Hardware:**
Desktops and Servers with following GPU architectures:
* NVIDIA Blackwell <br>
* NVIDIA Hopper <br>
* NVIDIA Lovelace <br>
* NVIDIA Ampere <br>
* NVIDIA Turing <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing:  |  Age, Gender, Race, Skin Color
Measures taken to mitigate against unwanted bias:                                                   |   Collected data from public and private sources to better balance gender diversity. Evaluated using internal, proprietary data mix to achieve identical key performance indicators.

## Explainability

| Field                                                                                                 | Response                                                                                                                                                                                                                                                                                                |
| :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Intended Task/Domain:                                                                                 | Content localization for real-time broadcasting and streaming                                                                                                                                                                                                                                                         |
| Model Type:                                                                                           | Convolutional Neural Networks (CNNs), Generative Adversarial Networks (GANs)                                                                                                                                                                                                                                                |
| Intended Users:                                                                                       | This model is intended for users working on content localization for real-time broadcasting and streaming use cases.                                                                                                                                                                                                                                 |
| Output:                                                                                               | Reanimated video frames with lip motion in sync with input audio.                                                                                                                                                                                                                                                                |
| Describe how the model works:                                                                         | Model generates images of human with lip motions synced with audio based on extracted features; head pose and background are kept the same, and the overall image quality is also maintained.                                                                                                                                                                    |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Age, Gender, Race, Skin Color                                                                                                                                                                                                                                                                            |
| Technical Limitations & Mitigation:                                                                   | This model may not work well for occluded faces, poor lighting conditions, large profile views and for audios with multiple speakers.                                                                                                                                  |
| Verified to have met prescribed NVIDIA quality standards:                                             | Yes                                                                                                                                                                                                                                                                                                     |
| Performance Metrics:                                                                                  | Quality (subjective and objective metrics), Per frame latency on various GPUs                                                                                                                                                                                       |
| Potential Known Risks:                                                                                | This model may generate faces with artifacts like artificial-looking teeth and beards. This model may fail to accurately lip sync with the input audio typically in cases of poor lighting and noisy audio. |
| Licensing:                                                                                            |  Governing Terms: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).                                                                                              |

## Privacy

**Privacy Information**

LipSync was trained on large-scale publicly available data that may contain images, audio-video, and text relating to people. NVIDIA collected and used this data in compliance with applicable data protection and privacy laws. This model was not designed to derive insights or otherwise learn from any personal data contained in the datasets.

NVIDIA uses a combination of filters, data minimization techniques, and other guardrails to help prevent personal data from being recited by our models. We employ automated tools and data processing techniques during pre-training or training to identify and filter certain categories of personal data.

Please review NVIDIA's [Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) for more information.

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  Content localization for real-time broadcasting and streaming
Describe the life critical impact (if present).   |  Not Applicable
Use Case Restrictions:                              |  Governing Terms: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).
Model and dataset protection:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to.