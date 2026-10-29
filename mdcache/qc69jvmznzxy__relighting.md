---
title: "Relighting"
publisher: "nvidia"
type: "endpoint"
updated: "2026-04-17T04:01:50.298Z"
description: "Re-illuminate people in video to match target lighting from a 360 HDRI environment map."
canonical: "https://build.nvidia.com/nvidia/relighting"
---

# Model Overview

### Description:

The NVIDIA AI for Media Relighting model re-illuminates a person in a video to match the target lighting provided by a 360 High Dynamic Range Image (HDRI).

Relighting is a developer-ready AI feature for enhancing video communication and content creation workflows. Its state-of-the-art models create high-quality visual AI effects using standard cameras without additional special equipment.

Relighting is exclusively part of NVIDIA AI Enterprise for production workflows — an extensive library of full-stack software, including AI solution workflows, frameworks, pre-trained models, and infrastructure optimization.

This model is ready for commercial/non-commercial use. <br>

### License/Terms of Use

Refer to [NVIDIA SOFTWARE LICENSE AGREEMENT](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and [Product-Specific Terms for NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). Use of the models is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).
<br>

### Deployment Geography:

Global <br>

### Use Case: <br>

1. Virtual Production: Match lighting between real subjects and virtual environments for seamless compositing.

2. Video Conferencing: Adjust participant lighting to match virtual backgrounds or improve appearance.

3. Content Creation: Enhance lighting consistency when combining footage from different sources.

### Release Date: <br>

NGC - 01/06/2026 via https://catalog.ngc.nvidia.com/orgs/nvidia/teams/maxine/models/nvvfxrelighting <br>

## References(s):

- [NVIDIA AI for Media](https://developer.nvidia.com/topics/ai/generative-ai/ai-for-media)

## Model Architecture:

**Architecture Type:** Convolution Neural Network (CNN), Generative Adversarial Networks (GANs)
**Network Architecture:** ResNet, UNET

- This model was developed based on [LUMOS](https://research.nvidia.com/labs/dir/lumos/).
- Number of model parameters 2.06 x 10^7

## Input: <br>

**Input Type(s):** Image
**Input Format(s):** Red, Green, Blue (RGB)
**Input Parameters:** Two-Dimensional (2D) <br>
**Other Properties Related to Input:** Input image 360p to 4k, Input HDR Image with extension .hdr or .exr. F16/F32 data type. <br>

## Output: <br>

**Output Type(s):** Image
**Output Format:** Red, Green, Blue (RGB)
**Output Parameters:** Two-Dimensional (2D)<br>
**Other Properties Related to Output:** Output resolution is the same as input.

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:

**Runtime Engine(s):**

- VFX SDK- 1.1.0.0 <br>

**Supported Hardware Microarchitecture Compatibility:** <br>

- NVIDIA Ampere
- NVIDIA Blackwell
- NVIDIA Hopper
- NVIDIA Lovelace
- NVIDIA Turing

**[Preferred/Supported] Operating System(s):** <br>

- Ubuntu 20.04 <br>
- Ubuntu 22.04 <br>
- Ubuntu 24.04 <br>
- Debian 12 <br>
- Rocky/RHEL 8.\* <br>
- Rocky/RHEL 9.\* <br>
- Windows 10 <br>
- Windows 11 <br>

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Training, Testing, and Evaluation Datasets:

- The total size (in number of data points): around 700k
- Total number of datasets: 24
- Dataset partition: Training [98%], testing [1%], evaluation [1%]

### Training Dataset:

**Link:**

- Turbosquid assets
- FFHQ CCBY
- HDRi Haven HDRI asset
- hdri-skies.com HDR Data Set
- Universite Laval HDR Data Set
- noemotionhdrs.net HDR Data Set
- HDRMaps.com HDR Data Set
- PolyHaven HDR
- TalkingHeads Dataset
- NV_UpperBody_Dataset
- RenderPeopleDataset
- AI Greenscreen Dataset Broadcast feedback website
- AI Greenscreen Dataset Youtube CCBY
- InternalCapture-GazeRedirection dataset
- Youtube-ccby dataset
- TripleGanger dataset

**Data Collection Method by dataset**
Hybrid: Human and Synthetic <br>

**Labeling Method by dataset**
Hybrid: Automated and Synthetic<br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**
Synthetic dataset contains 600k training samples of image, HDRIs and intermediate ground truth under paired lighting conditions.
Real dataset contains around 40k images and 50k videos of people in different lighting environments.
HDR dataset contains over 8000 HDR images.

**Data Modality**

- Image
- Envrionment map

**Image Training Data Size**

- Less than a Million images
<br>

### Testing Dataset:

**Link:**

- PolyHaven HDR
- NV_UpperBody_Dataset
- AI Greenscreen Dataset Youtube CCBY
- InternalCapture-GazeRedirection dataset
- Youtube-ccby dataset
<br>

**Data Collection Method by dataset**
Human <br>

**Labeling Method by dataset**
Automated<br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**
Around 200 videos with various lengths of a single person in front of the camera conducting a video conference or broadcasting. The dataset varies in terms of quality, lighting, head pose, gaze angles and other diversity factors such as race, eye color, and gender.
<br>

### Evaluation Dataset:

**Link:**

- PolyHaven HDR
- TripleGanger dataset
<br>

**Data Collection Method by dataset**
Synthetic <br>

**Labeling Method by dataset**
Synthetic <br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**
50 sets of image-albedo pairs rendered using TripleGanger assets and 600 Polyhaven HDRI images using Omniverse Kit.
<br>

# Inference:

**Engine:** TensorRT <br>
**Test Hardware:** <br>

- T4, A10, A40, A100, L4, L40, B40 <br>
- RTX 2060, 3070, 4090, 5080 <br>

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please make sure you have proper rights and permissions for all input image and video content; if image or video includes people, personal health information, or intellectual property, the image or video generated will not blur or maintain proportions of image subjects included.

For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing:  |  Age, Gender, Race, Skin color
Measures taken to mitigate against unwanted bias:                                                   |  Collected synthetic data and real data from public and private sources to increase age, gender, race and skin color diversity.  Evaluated using internal, proprietary data mix to achieve identical key performance indicators.

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Task/Domain:                                                                   |  Content Creation and Video Communication
Model Type:                                                                                            |  Image Enhancement Convolutional Neural Networks (CNNs).
Intended Users:                                                                                        |  This model is intended for users interested in content creation and video conferencing.
Output:                                                                                                |  Image relighted per supplied environment map
Describe how the model works:                                                                          |  The model re-illuminates a person's image to match the target lighting provided by a 360 HDR Image that contains environment lighting.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age, Gender, Race, Skin color.
Technical Limitations & Mitigation:                                                                    |  This model may not perform well for frames with multiple subjects/persons. 
Verified to have met prescribed NVIDIA quality standards:  |  Yes
Performance Metrics:                                                                                   |  Quality (subjective and objective metrics), Latency, Throughput
Potential Known Risks:                                                                                 |  This model may shift hue, tone, temperature of skin tone based on the lighting of the subjects.
Licensing:                                                                                             |  Refer to [NVIDIA SOFTWARE LICENSE AGREEMENT](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and [Product-Specific Terms for NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). Use of the models is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                     |  No
Personal data used to create this model?                                                                                       |  Yes
Was consent obtained for any personal data used?                                                                                             |  No, not possible with web-sourced data.
How often is dataset reviewed?                                                                                                     |  At the onset of the project and when needed during the development. 
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Not applicable
If personal data was collected for the development of the model, was it collected directly by NVIDIA?                                            | No
If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  | Not applicable
If personal data was collected for the development of this AI model, was it minimized to only what was required?                                 |  Yes
Is there provenance for all datasets used in training?                                                                                |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  Not applicable
Applicable Privacy Policy        |  https://www.nvidia.com/en-us/about-nvidia/privacy-policy/

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application Field(s):                               |  Video Conferencing and Broadcasting Enhanced Lighting
Describe the life critical impact (if present).   |  Not Applicable <br>
Use Case Restrictions:                              |   Refer to [NVIDIA SOFTWARE LICENSE AGREEMENT](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and [Product-Specific Terms for NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). Use of the models is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).
Model and dataset restrictions:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.