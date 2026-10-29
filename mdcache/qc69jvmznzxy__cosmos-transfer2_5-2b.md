---
title: "cosmos-transfer2.5-2b"
publisher: "nvidia"
type: "endpoint"
updated: "2026-02-26T00:09:28.953Z"
description: "Generates physics-aware video world states for physical AI development using text prompts and multiple spatial control inputs derived from real-world data or simulation."
canonical: "https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b"
---

# Model Overview

## Description
**Cosmos-Transfer2.5**: A family of highly performant pre-trained world foundation models purpose-built for generating physics-aware images, videos and world states aligned with the input control conditions.

Cosmos-Transfer2.5 diffusion models are a collection of diffusion based world foundation models that generate dynamic, high quality images and videos from text, image, or control video inputs. It can serve as the building block for various applications or research that are related to world generation. This model is ready for commercial/non-commercial use.

**Model Developer**: NVIDIA

## Model Versions

The Cosmos-Transfer2.5 diffusion-based model family includes the following models:

- [Cosmos-Transfer2.5-2B](https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B)
- Given a text prompt and one or multiple (up to four) control input videos -- Canny edge, blurred RGB, segmentation mask, and depth map  -- predict a photorealistic output video by leveraging guidance in the control input videos. Automatic extraction is available for edge and blur controls when only an RGB video is provided.

The model produces 720P video with 16FPS

- [Cosmos-Transfer2.5-2B/ Auto / Multiview](https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B)
- Given a text prompt and 7 "world scenario" control input videos (from front center, front left, front right, rear left, rear right, rear tele, front tele cameras on an autonomous vehicle), generate 29 view-consistent frames for each of the 7 cameras at resolution of 1280×720 (text-to-world). The model can additionally be conditioned by 1 or 2 initial latent frames using reference videos of the 7 cameras (image-to-world, video-to-world).

The model has been trained on 720p video at 10FPS.

### License
The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); and use of the model is governed by the  [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license). Additional Information: [Apache License 2.0](https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B/blob/main/LICENSE). 

### Deployment Geography:

Global

### Use Case:

Physical AI: encompassing robotics, autonomous vehicles (AV), and more.

### Release Date:

Github [10/06/2025] via https://github.com/nvidia-cosmos/cosmos-transfer2.5

HuggingFace [10/06/2025] via https://huggingface.co/collections/nvidia/cosmos-transfer25-6864569b8acaf966a107bfe3

## Model Architecture
Cosmos-Transfer2.5-2B is a diffusion transformer model designed for video denoising in the latent space, modulated by multiple control branches. 

The diffusion transformer network (“the base model”) is composed of interleaved self-attention, cross-attention and feedforward layers as its building blocks. The cross-attention layers allow the model to condition on input text throughout the denoising process. Before each layer, adaptive layer normalization is applied to embed the time information for denoising. When image or video is provided as input, their latent frames are concatenated with the generated frames along the temporal dimension. Augment noise is added to conditional latent frames to bridge the training and inference gap.

The control branch is formed by replicating a few transformer blocks of the base model. It processes the control input video to extract control signals, which are then injected into the corresponding transformer blocks of the base model, guiding the denoising process with structured control. When multiple control input videos are provided, each is processed by a dedicated control branch to extract modality-specific control signals. These control signals are then combined with spatial-temporal weight maps, and injected into the corresponding transformer blocks in the base model.

**This model was developed based on:**  [Cosmos-Predict2.5](https://huggingface.co/nvidia/Cosmos-Predict2.5-2B)

**Number of model parameters:** 2,358,047,744 

## Input/Output Specifications

* **Input**

* **Input Type(s)**:  Text+Video
* **Input Format(s)**:
* Text: String
* Control Input Video: mp4
* **Input Parameters**:
* Text: One-dimensional (1D)
* Control Input Video: Three-dimensional (3D)
* **Other Properties Related to Input**:
* The input text string should contain fewer than 300 words and should provide descriptive content for world generation, such as a scene description, key objects or characters, background, and any specific actions or motions to be depicted within the 5-second duration.
* The model supports control input videos of varying lengths, but a length which is multiples of 93 frames (e.g., 93, 186, or 279 frames) performs the best.
* The model supports four types of control input videos: blurred video, Canny edge video, depth map video, and segmentation mask video. When multiple control inputs are provided, they must be derived from the same source video, representing different modalities of the same content while maintaining identical spatio-temporal dimensions.
* The control input video should have a spatial resolution of 1280×720 for the 720P model. 

* **Output**
* **Output Type(s)**: Video
* **Output Format(s)**: mp4
* **Output Parameters**: Three-dimensional (3D)
* **Other Properties Related to Output**: The output video is of the same temporal length and spatial resolution of the control input video. The frame rate of the output video is determined by the model variant (i.e., 16 FPS)

The video content visualizes the input text description as a short animated scene, capturing key elements within the specified time constraints.

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration
**Runtime Engine(s):**
* [Cosmos-Transfer2.5](https://github.com/nvidia-cosmos/cosmos-transfer2.5)

**Supported Hardware Microarchitecture Compatibility:**

* NVIDIA Ampere
* NVIDIA Blackwell
* NVIDIA Hopper

**Note**: Only BF16 precision is tested. Other precisions like FP16 or FP32 are not officially supported.

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Training Dataset:

**Data Modality** <br>
* [Image] <br>
* [Text] <br>
* [Video] <br>

**Data Collection Method by dataset** <br>
* [Automated] <br>

**Labeling Method by dataset** <br>
* [Hybrid: Human, Automated] <br>

### Testing Dataset:

**Data Collection Method by dataset** <br>
* [Automated] <br>

**Labeling Method by dataset** <br>
* [Hybrid: Human, Automated] <br>

# Evaluation

Please see our [technical paper](https://research.nvidia.com/publication/2025-09_world-simulation-video-foundation-models-physical-ai) for detailed evaluations of the base model. The control models are built upon the base foundation model.

**Data Collection Method**:
* Automated

**Labeling Method**:
* Hybrid:  Human,Automated

**System Requirements and Performance:**
This model requires 65.4 GB of GPU VRAM.

The following table shows generation times across different NVIDIA GPU hardware for single-GPU inference:

| GPU Hardware | Cosmos-Transfer2-2B (Segmentation) |
|--------------|---------------|
| NVIDIA B200 | 285.83 sec |
| NVIDIA H100 NVL | 719.4 sec |
| NVIDIA H100 PCIe | 870.3 sec |
| NVIDIA H20 | 2326.6 sec |

**Operating System(s):**
* Linux (We have not tested on other operating systems.)

**Note**: Only BF16 precision is tested. Other precisions like FP16 or FP32 are not officially supported.

# Usage

* See [Cosmos-Transfer2.5](https://github.com/nvidia-cosmos/cosmos-transfer2.5) for details.

## Limitations
Despite various improvements in world generation for Physical AI, Cosmos-Transfer2.5 models still face technical and application limitations for world-to-world generation. In particular, they struggle to generate long, high-resolution videos without artifacts. Common issues include temporal inconsistency, camera and object motion instability, and imprecise interactions. The models may inaccurately represent 3D space, 4D space-time, or physical laws in the generated videos, leading to artifacts such as disappearing or morphing objects, unrealistic interactions, and implausible motions. As a result, applying these models for applications that require simulating physical law-grounded environments or complex multi-agent dynamics remains challenging.

## Inference:
**Acceleration Engine**: [PyTorch](https://pytorch.org/), [Transformer Engine](https://github.com/NVIDIA/TransformerEngine)

**Test Hardware:** H100, A100, GB200

## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Please make sure you have proper rights and permissions for all input image and video content; if image or video includes people, personal health information, or intellectual property, the image or video generated will not blur or maintain proportions of image subjects included.

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.

For more detailed information on ethical considerations for this model, please see the subcards of Explainability, Bias, Safety & Security, and Privacy below. Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

### Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing:  |  None
Measures taken to mitigate against unwanted bias:                                                   |  None

## Explainability

### Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Application & Domain:                                                                   |  World Generation
Model Type:                                                                                            |  Transformer
Intended Users:                                                                                        |  Physical AI developers
Output:                                                                                                |  Videos
Describe how the model works:                                                                          |  Generates videos based on text and video inputs
Technical Limitations:                                                                                 |  The model may not follow the video input accurately.
Verified to have met prescribed NVIDIA quality standards:  |  Yes
Performance Metrics:                                                                                   |  Quantitative and Qualitative Evaluation. We use PAIBench-Transfer, a benchmark dataset containing 600 videos spanning diverse domains such as driving and robotics. The evaluation is structured around two key dimensions: adherence to control inputs (how well the generated video follows the provided conditions) and overall video quality (measuring realism and consistency).
Potential Known Risks:                                                                                 |  The model's output can generate all forms of videos, including what may be considered toxic, offensive, or indecent.
Licensing:                                                                                             |  * The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); and use of the model is governed by the  [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license). Additional Information: [Apache License 2.0](https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B/blob/main/LICENSE).

## Privacy

### Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                |  No
Personal data used to create this model?                                                     |  None Known
Was consent obtained for any personal data used?                                                                                             |  None Known
How often is dataset reviewed?                                                                                                     |  Before Release
Is there provenance for all datasets used in training?                                                                                |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  No, not possible with externally-sourced data.
Applicable Privacy Policy        | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/

## Safety & Security

### Safety And Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  World Generation
Describe the life critical impact (if present).   |  None Known
Use Case Restrictions:                              |  * Abide by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); and use of the model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license). Additional Information: [Apache License 2.0](https://huggingface.co/Qwen/Qwen3Guard-Gen-0.6B/blob/main/LICENSE).. 
Model and dataset restrictions:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to. Model checkpoints are made available on Hugging Face, and may become available on cloud providers' model catalog.