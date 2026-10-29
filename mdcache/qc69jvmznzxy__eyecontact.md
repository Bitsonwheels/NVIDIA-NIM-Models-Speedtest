---
title: "eyecontact"
publisher: "nvidia"
type: "endpoint"
updated: "2025-03-21T13:58:01.201Z"
description: "Estimate gaze angles of a person in a video and redirect to make it frontal."
canonical: "https://build.nvidia.com/nvidia/eyecontact"
---

# Model Overview

## Description:

The Maxine Eye Contact model redirects eye gaze for video conference applications.

The model estimates the gaze direction of the input eye gaze and synthesizes a redirected gaze using a region of interest around one’s eyes known as an eye patch.

The encoder encodes the image’s contents into latent representations for eye gaze, head pose and environmental conditions.

A transformation is applied to these latent representations to align them with the redirection angle provided by the user. The transformed representations when fed to the decoder result in the generation of an output eye patch with eyes redirected in the desired angle.

More information about eye contact can be found in the developer blog [here](https://developer.nvidia.com/blog/improve-human-connection-in-video-conferences-with-nvidia-maxine-eye-contact/).

<br>
## Terms of use

The use of NVIDIA Maxine Eye Contact is available as a demonstration of the input and output of the Gaze Estimation transformer model. As such the user may submit a reference "video" and download the generated gaze redirected video for evaluation under the terms of the [NVIDIA MAXINE EVALUATION LICENSE AGREEMENT](https://developer.download.nvidia.com/maxine/nvidia-maxine-evaluation-license-24oct2023.pdf).

## References(s):

* Rochelle, et al. “[Improve Human Connection in Video Conferences with NVIDIA Maxine Eye Contact](https://developer.nvidia.com/blog/improve-human-connection-in-video-conferences-with-nvidia-maxine-eye-contact/)”, Jan 21, 2023, NVIDIA Technical Blog.<br>

## Model Architecture:
**Architecture Type:** Convolution Neural Network (CNN)  <br>
**Network Architecture:** Encoder-Decoder <br>
The network architecture includes a transforming encoder and decoder network. The encoder encodes the image’s contents into latent representations for (a) the image’s non-subject related factors(e.g., environmental lighting, shadows, image white balance and hue, blurriness); (b) subjected-related factors (e.g., skin color, face/eye shape, eye glasses); (c) eye gaze and (d) head pose.

A rotation applied to the individual latent factors affects a corresponding change in the appearance of the image to alter the factor. In this application, we apply a rotation to the gaze related latent factor. The transformed latent factors are fed to the decoder to generate the transformed version of the input with a gaze redirected angle.
<br>

## Input:
**Input Type(s):** Image: Angle vector<br>
**Input Format(s):** Image: Red, Green, Blue (RGB), Angle vector: Radians <br>
**Input Parameters:** Input Image:(256 x 64) 2D redirection angle vector [2,1] <br>
**Other Properties Related to Input:** Input image of resolution 256 x 64 normalized RGB in range of [0, 1].  Redirection gaze angle is a float32 value representing the pitch and yaw angles in radians.  <br>

## Output: <br>
**Output Type(s):** Image, Estimated Angle Vector,Landmarks Vector <br>
**Output Format:** Image: Red, Green, Blue (RGB), Estimated Angle Vector: Radians, Landmarks Vector: Float32  <br>
**Output Parameters:** Image: [256 x64], Estimated Angle Vector[2,1] , Landmarks Vector [2,1] <br>
**Other Properties Related to Output:** Output image is normalized by dividing by 255. Estimated gaze angle is a float32 representing the pitch and yaw angles in radians. Redirected eye landmarks are represented by 12 fiducial points marking the outline of the eyes, each value represented by x and y positions of the point in float32 format. <br>

## Software Integration:
0.8.8.0

## Supported Operating System(s):
* Ubuntu 18.04 <br>
* Ubuntu 20.04 <br>
* Ubuntu 22.04 <br>
* Debian 11 <br>
* Rocky 8.7 <br>
* Windows 10 <br>
* Windows 11 <br>

## Model Version(s):
[Maxine- 0.8.6.0] <br>

## Supported Hardware Microarchitecture Compatability:

* [Turing] <br>
* [Ampere] <br>
* [ADA] <br>
* [Blackwell] <br>

## Training and Evaluation Dataset:

**Data Collection Method by dataset:**
* Hybrid: Human and Synthetic <br>

**Labeling Method by dataset:**
* Automated <br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**
Training dataset contains approximately 2 million images of rectangular eye patches of people captured with different environmental conditions, head poses and gaze angles. The dataset contain a combination of real data and synthetic data. <br>

### Evaluation Dataset:

**Data Collection Method by dataset:** Automated, Human <br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**

Internally-captured dataset of 65 videos, each between 30 seconds to two (2) minutes of a single person between 1 to 3 feet in front of the camera conducting a video conference. The dataset varies in terms of quality, lighting, head pose, gaze angles and other diversity factors such as race, eye color, and gender. <br>
# Inference:
**Engine:** [TensorRT](https://developer.nvidia.com/tensorrt), [Triton](https://developer.nvidia.com/triton-inference-server) <br>
**Test Hardware:**
* CUDA 12.8 compatible hardware versions of Desktop and Servers.

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing:  |  Age (18+), Gender, Skin Color
Measures taken to mitigate against unwanted bias:                                                   |   Collected data from public and private sources to increase eye and skin color diversity.  Developed 25% synthetically-generated data to further increase variety of eye colors represented.

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Applications & Domains:                                                                       |  Content Creation and Video communication.
Types:                                                                                                 |  Facial Animation
Intended Users:                                                                                        |  Applications for gaze estimation and/or gaze redirection in video communication and content creation.
Output:                                                                                                |  Eye patch image and gaze angle
Describe how the model works:                                                                          |  The model takes an eye patch image of a person as input. The model estimates the gaze angle of the eyes with respect to the camera. The GAN model redirects the eye patch to make it look at the camera or specified redirection angle. 
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age (18+), Gender, Ethnicity
Technical Limitations:                                                                                 |   Model requires both eyes to be visible and within feasible redirection limits. 
Verified to have met prescribed NVIDIA quality standards:  |  Yes
Performance Metrics:                                                                                   |  Throughput, Latency, and other quality metrics including gaze estimation error, gaze redirection error and Learned perceptual image patch similarity.
Potential Known Risks:                                                                                 |  This model may fail to detect the eyes or redirect them accurately towards the camera typically in cases of uneven lighting, glare, occlusion or high angles of redirection. Color of redirected eyes could change slightly due to lighting or bias in the model. 
Licensing:                                                                                             | [NVIDIA Maxine Evaluation License Agreement](https://developer.download.nvidia.com/maxine/nvidia-maxine-evaluation-license-24oct2023.pdf)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                                                 |  None
Was consent obtained for any personal data used?                                                                                   |  Yes
Protected class data used to create this model?                                                                                    |  Yes
How often is dataset reviewed?                                                                                                     |  Before Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Not Applicable
If personal data collected for the development of the model, was it collected directly by NVIDIA?                                            |  Yes 
If personal data collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  Yes
If personal data collected for the development of this AI model, was it minimized to only what was required?                                 |  Yes
Is there provenance for all datasets used in training?                                                                                                      |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Not Applicable 
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  Not applicable

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  Video Conferencing and Content creation
Describe the life critical impact (if present).   |  Not Applicable
Use Case Restrictions:                              |  Refer to [Maxine Evaluation EULA](https://developer.download.nvidia.com/maxine/nvidia-maxine-evaluation-license-24oct2023.pdf)
Model and dataset protection:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to.