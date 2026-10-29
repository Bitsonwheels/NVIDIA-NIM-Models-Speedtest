---
title: "3D Body Pose"
publisher: "nvidia"
type: "endpoint"
updated: "2026-09-30T22:21:37.105Z"
description: "Estimate 3D human body pose and skeleton from video input."
canonical: "https://build.nvidia.com/nvidia/body-pose"
---

# 3D Body Pose NIM — Container Card

## Description

The 3D Body Pose NIM uses GPU-accelerated inference to estimate 3D human body poses and skeletal structures from video input. It processes video frames using an NVIDIA Triton Inference Server backend and returns pose-estimation results through a streaming gRPC API.

The container components are ready for commercial or non-commercial use.

## License/Terms of Use

Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the GENMO model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Use of the Vitpose model is governed by the NVIDIA Open Model License Agreement, the [Meta Dinov3 License](https://ai.meta.com/resources/models-and-libraries/dinov3-license/) and the [SAM License](https://huggingface.co/facebook/sam-3d-body-dinov3/blob/main/LICENSE); Built with Dinov3. Use of the SAM3DB-Body model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/) and the [SAM License](https://huggingface.co/facebook/sam-3d-body-dinov3/blob/main/LICENSE).

## Intended Use

- Real-time and offline 3D body pose estimation from video
- Video production, motion capture, sports analytics
- Accessibility applications
- Research and development in computer vision

## Known Limitations

- Requires NVIDIA GPU, compute capability 8.0+ (Ampere and newer: sm80, sm86, sm89, sm90, sm100, sm120). T4/sm75 not supported.
- Multi-person pose estimation supported natively (tracked bounding boxes in, per-body 3D pose out); throughput scales with bodies/frame.
- Performance depends on input video resolution, bodies/frame, and GPU model
- Production 3D body pose model (AR SDK `3DBodyPoseEstimation`, release 1.2.0) is integrated; not a dummy backend

## Deployment Geography

Global

## Release Date

Build.NVIDIA.com 09/30/2026 via https://build.nvidia.com/nvidia/body-pose
NGC 09/30/2026 via https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/body-pose

## Program Classes

The body_pose Container includes the AR SDK `3DBodyPoseEstimation` (release 1.2.1), which ships as a bundle of the following models:

| Model Name & Link | Use Case                                             | How to Pull the Model |
| ----------------- | ---------------------------------------------------- | --------------------- |
| GENMO             | 3D human body pose and skeletal structure generation | Automatic             |
| SAM3DB            | 3D body segmentation/tracking                        | Automatic             |
| Dino-v3-VITPose   | 2D keypoint/pose detection backbone                  | Automatic             |

## Deployment Details

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

- **Cloud**: Hosted on build.nvidia.com (NV-GCP) via NVCF
- **On-premise**: Docker container with NVIDIA GPU runtime
- **Ports**: gRPC 8001, Triton HTTP 9000, Triton gRPC 9001
- **Config**: `NIM_MODEL_PROFILE`, `NGC_API_KEY`, `NV_AI4M_MAX_CONCURRENCY_PER_GPU`, `NV_AI4M_MAX_INPUT_FILE_SIZE_BYTES`, `BODY_POSE_ENABLE_CONTACT`, `BODY_POSE_MAX_ACTIVE_REQUESTS` — see nim-documentation getting-started/advanced-usage guides

## Software Stack

| Component               | Version                   |
| ----------------------- | ------------------------- |
| Base                    | DeepStream 25.03          |
| Triton Inference Server | v2.56.0                   |
| CUDA                    | 12.8.1                    |
| cuDNN                   | 9.8.0                     |
| TensorRT                | 10.9.0.34                 |
| Python                  | 3.12                      |
| gRPC                    | 1.62.3                    |
| GStreamer               | System (HW encode/decode) |

## Security Common Vulnerabilities and Exposures (CVEs)

Please review the Security Scanning tab on NGC to view the latest security scan results.
For certain open-source vulnerabilities listed in the scan results, NVIDIA provides a response in the form of a Vulnerability Exploitability eXchange (VEX) document. The VEX information can be reviewed and downloaded from the Security Scanning tab.

## Security

- gRPC transport unencrypted by default (`NIM_SSL_MODE=disabled`); TLS/mTLS opt-in

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal developer team to ensure these software components meet requirements for the relevant industry and use case and address unforeseen product misuse.

Please report quality, risk, security vulnerabilities, or NVIDIA AI concerns through the [NVIDIA Vulnerability Disclosure Program](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail).

# Get Help

## Getting started with the NIM

Deploying and integrating the NIM is straightforward thanks to our industry standard APIs. Visit the [NIM container page on NGC](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/body-pose) for release documentation, deployment guides and more.

## Enterprise Support

Get access to knowledge base articles and support cases or [submit a ticket](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Capabilities

- **Function Calling:** Not supported

## Bias

# ViTPose

| Field | Response |
|---|---|
| Participation considerations from adversely impacted groups/protected classes in model design and testing | Not Applicable - The model does not include humans; it leverages synthetic avatars. Avatar selection was randomized across age, gender, race, and skin color. No demographic subgroup parity measurement was performed. |
| Measures taken to mitigate unwanted bias | Not Applicable |
| Bias Metric | Not Applicable |

# GENMOv1

| Field | Response |
|---|---|
| Participation considerations from adversely impacted groups/protected classes in model design and testing | Not Applicable - No demographic subgroup comparable-outcomes measurement was performed. |
| Measures taken to mitigate unwanted bias | Not Applicable |
| Bias Metric | Not Applicable |

## Explainability

# ViTPose

| Field | Response |
|---|---|
| Intended Task/Domain | Top-down 2D human-pose estimation for the [SOMA-77](https://github.com/NVlabs/SOMA-X) keypoint layout; intended as an input to the downstream NVIDIA AR SDK 3D Body Pose Estimation pipeline. |
| Model Type | DINOv3 ViT-H+/16 encoder with a deconvolutional heatmap decoder. |
| Intended Users | AR SDK developers building 3D body-pose, body-motion, and animation applications. |
| Output | Raw Float32 heatmaps with shape `[batch, 77, 64, 48]`; AR SDK postprocessing produces per-person source-image `[x, y, confidence]` keypoints with shape `[batch, 77, 3]`. |
| How the model works | A DINOv3 H+ encoder divides the person crop into 16×16 patches and produces dense visual features. A deconvolutional decoder upsamples those features into one heatmap per SOMA-77 keypoint. Heatmap peaks are refined and mapped back to source-image coordinates. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of | Not Applicable |
| Technical Limitations and Mitigation | Accuracy depends on the upstream person bounding box. Performance may degrade with occlusion, truncation, subjects occupying too few pixels in the image, extreme viewpoints or poses, motion blur, poor lighting, concealing clothing, mobility aids, and synthetic-to-real domain differences. Detection, tracking, multi-person association, and 3D reconstruction are outside the model. Mitigate through detector/tracker validation, confidence-aware handling, system-level checks, operational bounds, and human review where appropriate. |
| Verified to have met prescribed NVIDIA quality standards | Yes |
| Performance Metrics | Accuracy (PCK@5% bbox) and per-frame latency. PCK@5% bbox is 97.9% on MetroSim DigitalHuman minival and 98.9% on MetroSim RenderPeople minival. |
| Potential Known Risks | Incorrect or low-confidence 2D keypoints can propagate into downstream 3D reconstruction, producing jitter, implausible limb placement, or unstable animation. Confidence values are not calibrated probabilities. Outputs must not be treated as medical, biometric-identity, safety-critical, or ground-truth anatomical measurements. |
| Licensing | GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |

# GENMOv1

| Field | Response |
|---|---|
| Intended Task/Domain | 3D human body-pose estimation from a tracked bounding box for one person in a video. |
| Model Type | Diffusion model with Transformer-based denoising blocks. |
| Intended Users | Developers using 3D Body Pose Estimation through NVIDIA AR SDK for single-person 3D body-pose estimation in computer-vision, animation, gaming, and 3D-content workflows. |
| Output | Body parameters for SOMA, NVIDIA's canonical body topology and rig; camera-space 3D joint coordinates; body mesh; and BioVision Hierarchy animation. A caller-provided world-root transform can convert applicable outputs to world space. |
| How the model works | An upstream detector/tracker supplies one person's per-frame bounding boxes. The pipeline extracts SAM3DB features and 2D keypoints with confidence values from ViTPose. GENMOv1 conditions its diffusion-based motion model on those inputs to estimate a temporally coherent body-pose sequence. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of | Not Applicable |
| Technical Limitations and Mitigation | Accuracy can degrade with poor or partial body visibility, severe truncation or occlusion, fast or unusual motion, significant upstream tracking/keypoint error, or clothing, activities, viewpoints, and assistive devices not represented in the training data. Each inference run supports one tracked person. Use a reliable upstream detector/tracker, ensure the body is clearly visible, run additional people separately, and validate the complete pipeline on use-case-specific data. GENMOv1 does not estimate facial expression or articulated hand detail. |
| Verified to have met prescribed NVIDIA quality standards | Yes |
| Performance Metrics | Public benchmark PA-MPJPE and acceleration error, per-frame latency, throughput, and visual inspection. |
| Potential Known Risks | GENMOv1 can produce inaccurate, temporally unstable, or physically implausible body pose and motion. Errors can propagate into animation, analytics, or downstream decisions. This model is not intended for medical, biometric, surveillance, or other high-impact decisions. |
| Licensing | GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |

## Privacy

# ViTPose

| Field | Response |
|---|---|
| Generatable or reverse engineerable personal data? | No |
| Personal data used to create this model? | No |
| Was consent obtained for any personal data used? | Not Applicable |
| How often is dataset reviewed? | Before Release |
| Was data from user interactions with the AI model used to train the model? | No |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | No, not possible with externally-sourced data |
| Applicable Privacy Policy | [NVIDIA Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) |

# GENMOv1

| Field | Response |
|---|---|
| Generatable or reverse engineerable personal data? | No |
| Personal data used to create this model? | Yes |
| Was consent obtained for any personal data used? | Unknown (Externally-Sourced Data) |
| How often is dataset reviewed? | Before Release |
| Is a mechanism in place to honor data subject right of access or deletion of personal data? | Unknown (Externally-Sourced Data) |
| If personal data was collected for the development of the model, was it collected directly by NVIDIA? | No |
| If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects? | Not Applicable |
| If personal data was collected for the development of this AI model, was it minimized to only what was required? | Yes |
| Was data from user interactions with the AI model used to train the model? | No |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | No, not possible with externally-sourced data |
| Applicable Privacy Policy | [NVIDIA Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) |

## Safety & Security

# ViTPose

| Field | Response |
|---|---|
| Model Application Field(s) | 3D Body Pose Estimation for Media and Entertainment |
| Life-critical impact | Not Applicable |
| Use Case Restrictions | GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |
| Model and dataset restrictions | The principle of least privilege is applied, limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset-license constraints are followed. |

# GENMOv1

| Field | Response |
|---|---|
| Model Application Field(s) | 3D Human Body Pose Estimation for Media and Entertainment |
| Life-critical impact | Not Applicable. The model is not intended for medical, emergency-response, biometric-identification, or other life- or safety-critical decisions. |
| Use Case Restrictions | GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |
| Model and dataset restrictions | The principle of least privilege is applied, limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset-license constraints are followed. |