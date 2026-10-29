---
title: "Active Speaker Detection"
publisher: "nvidia"
type: "endpoint"
updated: "2026-04-16T18:32:58.699Z"
description: "Detect and track speaker identities across video frames."
canonical: "https://build.nvidia.com/nvidia/active-speaker-detection"
---

# Active Speaker Detection

Active Speaker Detection is in fact a combination of multiple models that are used to perform the Active Speaker Detection effect, which processes video and multiple audio track inputs to detect, identify and track speaker identities across video frames. These include the Adaface model, Face and landmark Detector models and the SyncDiscriminator model

This feature and all associated models are available for commercial/non-commercial use.

### Using these models

To download the models, use the feature installation script bundled with the NVIDIA AR SDK (`features/install_feature.[ps1|sh]`). Please refer to the Active Speaker Detection Collection page or the AR SDK Documentation for more details. You can navigate to the collection page by click on the **Related Collections** tab at the top of this page.

### License/Terms of use:

The use of NVIDIA Active Speaker Detection is governed by the [NVIDIA SOFTWARE LICENSE AGREEMENT](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and [Product-Specific Terms for NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/).

Please see the additional sections below for each model for the governing terms of their use.

---

## Adaface

### Model Overview
Adaface generates embeddings for identifying people captured in different scenes. This model does not include biometric data.

### License/Terms of use
Use of the Adaface model is governed by the [NVIDIA Open Model License]( https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).  Additional Information: [MIT](https://github.com/mk-minchul/AdaFace/blob/master/LICENSE).

### Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA model card here: [CVLFace Adaface IR101 WebFace12M](https://huggingface.co/minchul/cvlface_adaface_ir101_webface12m).

### Deployment Geography:

Global

### Use Case:

- Generates embeddings for identifying people captured in different scenes for video dubbing
- Based on ResNet101 architecture with Additive Angular Margin Loss
- Optimized for minimal computational overhead
- Supports various demographics, lighting conditions, and image qualities
- Produces 512-dimensional face embeddings for identification tasks
- Compatible with InsightFace framework, replaces ArcFace/AuraFace model

### Release Date:
HuggingFace [repo](https://huggingface.co/minchul/cvlface_adaface_ir101_webface12m) June 5, 2024

NGC: 03/12/2026 - TensorRT optimized

### References

- **Paper:** [AdaFace: Quality Adaptive Margin for Face Recognition](https://arxiv.org/abs/2204.00964)
- **HuggingFace:** [Adaface IR101 WebFace12M](https://huggingface.co/minchul/cvlface_adaface_ir101_webface12m)

## Model Architecture

### Architecture Type
**Convolutional Neural Network (CNN)**

### Network Architecture
- **Backbone:** IResNet101
- **Loss Function:** Additive Angular Margin Loss (ArcFace)
- **Embedding Dimension:** 512-dimensional face embeddings
- **Framework:** ONNX format compatible with InsightFace ArcFace, TensorRT optimized
- **Number of model parameters:** 65.2M

## Input

### Input Type
Image

### Input Format
- **Color Space:** RGB (Red, Green, Blue)
- **Image Dimensions:** 112x112 pixels
- **Data Type:** float32 (normalized)

### Input Parameters
- **Batch Size:** Configurable (1 or more)
- **Image:** Two-Dimensional (2D)
- **Channels:** 3 (BGR)
- **layout:** NHWC

### Preprocessing Requirements
1. Face detection and alignment
2. Cropping to standard size (112x112)
3. Normalization to [0, 1] range

### Other Properties Related to Input
- Input images should contain a single face, properly aligned
- Images with multiple faces should be preprocessed to identify individual faces
- Optimal performance with well-lit, frontal face images
- Model can handle various lighting conditions and poses due to training data diversity

## Output

### Output Type
Embedding Vector

### Output Format
- **Embedding Dimension:** 512-dimensional normalized feature vector
- **Data Type:** float32
- **Normalization:** L2-normalized (unit vector)

### Output Parameters
- **Shape:** [batch_size, 512]

### Other Properties Related to Output
- Output embeddings can be compared using cosine similarity or Euclidean distance
- Typical similarity threshold for same person: >0.5 (cosine similarity)
- Embeddings are designed to cluster faces of the same identity closely in feature space
- Can be used for face verification, identification, and clustering tasks

## Training & Evaluation Data

### Training Dataset

#### Dataset Sources
The model was trained on a commercial dataset comprising face images from various publicly available and licensed sources:
- Commercially licensed face datasets
- Publicly available face identification benchmarks

#### Dataset Characteristics
AdaFace was trained on a commercial dataset comprising face images from various sources, including synthetic images. The dataset includes a wide range of demographics, lighting conditions, and image qualities to ensure robust performance across different scenarios.

- Data Collection Method:
- Hybrid: Synthetic, Undisclosed
- Labeling Method: Undisclosed

#### Data Preprocessing
- **Normalization:** All images were normalized to standard size and format
- **Augmentation:** Rotation, flipping, and scaling were used to improve generalization
- **Face Alignment:** All training faces were detected and aligned using standard landmarks

#### Dataset Limitations
Due to commercial licensing requirements, the training dataset may not extensively cover all global ethnicities and demographic groups. Users should conduct their own assessments to confirm the model's performance in their specific application context.

### Evaluation Benchmarks

AdaFace has been tested on multiple face recognition benchmarks:

- LFW: 0.99650
- CFP-FP: 0.95186
- AGEDB: 0.96100
- CALFW: 0.94700
- CPLFW: 0.90933

## Intended Use

### Primary Use Cases

**Media and Entertainment**
- Face-based search in media libraries
- Content personalization

### Bias and Fairness

#### Known Limitations
- **Demographic Representation:** The training dataset attempts to include diverse demographics, but may have limited representation of certain ethnicities due to dataset availability and commercial licensing constraints
- **Performance Variation:** Model efficacy in identity preservation may vary based on ethnicity, age, gender, and other demographic factors
- **Lighting Sensitivity:** Performance may degrade in extreme lighting conditions not well-represented in training data

#### Mitigation Efforts
- Training data included diverse demographics, lighting conditions, and image qualities
- Continuous monitoring and evaluation across demographic groups
- Open-source release to enable community testing and feedback
- Commercial licensing ensures proper data usage rights

#### Fairness Considerations
Efforts have been made to ensure that AdaFace performs equitably across different demographic groups. However, users should:
- Conduct their own fairness assessments in their specific application context
- Test model performance across relevant demographic groups for their use case
- Implement appropriate thresholds and decision-making processes
- Monitor for bias in production deployments

### Privacy Considerations

#### Data Privacy
- AdaFace characterizes faces, which is considered sensitive personal information in many jurisdictions
- Users must ensure compliance with relevant privacy laws (GDPR, CCPA, BIPA, etc.)
- Implement appropriate data protection measures (encryption, access controls)
- Obtain necessary consent from individuals whose faces are processed

#### Recommendations
- Store face embeddings rather than raw images when possible
- Provide transparency to users about face identification usage
- Enable user consent and opt-out mechanisms
- Conduct Privacy Impact Assessments (PIA) for your application

### Security Considerations

#### Potential Vulnerabilities
- **Presentation Attacks:** The model may be vulnerable to spoofing attacks using photos, videos, or masks (requires additional liveness detection)
- **Adversarial Attacks:** Like all neural networks, the model may be susceptible to adversarial perturbations
- **Model Extraction:** Publicly available model weights could be subject to model stealing attacks

#### Security Best Practices
- Implement liveness detection for security-critical applications
- Use multi-factor authentication rather than face identication alone for high-security scenarios
- Monitor for unusual patterns or potential attacks
- Keep model and dependencies updated
- Implement proper access controls for model deployment

## Limitations and Recommendations

### Known Limitations

1. **Generalization:** The model's generalization is limited by the scope of the training data
2. **Perfect Accuracy:** The model does not achieve perfect photorealism and identity consistency in all cases
3. **Demographic Variance:** Performance may vary across different demographic groups
4. **Environmental Conditions:** Extreme lighting, poses, or occlusions may reduce accuracy
5. **Performance Gap:** Does not match the performance of the original ArcFace due to smaller commercial training dataset
6. **Real-time Requirements:** May require GPU acceleration for real-time applications with high throughput

### Recommendations for Users

1. **Validation:** Conduct thorough testing in your specific deployment environment
2. **Threshold Tuning:** Adjust similarity thresholds based on your use case
3. **Demographic Testing:** Test across relevant demographic groups for your application
4. **Liveness Detection:** Implement additional liveness detection for security applications
5. **Monitoring:** Continuously monitor model performance in production
6. **Legal Compliance:** Ensure compliance with all relevant regulations (GDPR, CCPA, BIPA, etc.)
7. **Human Oversight:** Implement human review for high-stakes decisions
8. **Feedback Loop:** Establish mechanisms to collect and address user feedback

### Performance Optimization Tips

- Use GPU inference for batch processing and real-time applications
- Implement face detection caching for video streams
- Optimize image preprocessing pipeline
- Use TensorRT for additional performance gains on NVIDIA hardware
- Consider model quantization (FP16, INT8) for edge deployment

## Model Governance

### Model Maintenance
- **Updates:** The model is currently at version 1.0, with community feedback guiding future improvements
- **Issue Reporting:** Users can report issues on the HuggingFace model page or GitHub repository
- **Community Contributions:** The open-source nature enables community improvements and extensions

### Compliance and Regulations
Users are responsible for ensuring their use of AdaFace complies with:
- Local and international privacy laws (GDPR, CCPA, BIPA, etc.)
- Biometric data regulations
- Industry-specific requirements
- Ethical AI guidelines

## Changelog and Versioning

### Version 1.0 (Initial Release)
- ResNet101 architecture with Additive Angular Margin Loss
- Trained on commercially available face datasets
- ONNX format for broad framework compatibility
- Compatible with InsightFace framework, replaces ArcFace

## Contact and Support

### Model Developers
- **Organization:** Minchul Kim
- **Contributors:** @minchul
- **HuggingFace:** [minchul/cvlface_adaface_ir101_webface12m](https://huggingface.co/minchul/cvlface_adaface_ir101_webface12m)

## Additional Resources

### Documentation
- [AdaFace Paper](https://arxiv.org/abs/2204.00964)
- [Model Weights on HuggingFace](https://huggingface.co/minchul/cvlface_adaface_ir101_webface12m)

### Citations
If you use AdaFace in your research or applications, please cite:

```bibtex
@misc{adaface2022,
title={AdaFace: Quality Adaptive Margin for Face Recognition},
author={Minchul Kim, Anil K. Jain, Xiaoming Liu},
year={2022},
howpublished={\url{https://arxiv.org/abs/2204.00964}}
}

@inproceedings{deng2019arcface,
title={Arcface: Additive angular margin loss for deep face recognition},
author={Deng, Jiankang and Guo, Jia and Xue, Niannan and Zafeiriou, Stefanos},
booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
pages={4690--4699},
year={2019}
}
```

---

## Face and Landmarks Detector (FLD)

### Model Overview

The Face and Landmarks Detector (FLD) is a high-performance face detection and facial landmark localization model based on the SCRFD (Sample and Computation Redistribution for Face Detection) architecture. SCRFD is an efficient face detector with landmark localization capabilities, designed for real-time performance while maintaining high accuracy. The model simultaneously detects faces and predicts facial keypoints, making it ideal for comprehensive facial analysis pipelines.

### License/Terms of Use:

GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

### Deployment Geography:

Global

### Use Case:
### Primary Applications

- **Facial Recognition Pipelines:** Face detection and landmark extraction as preprocessing for recognition/verification
- **Face Alignment:** Landmark-based face normalization for downstream tasks
- **Facial Expression Analysis:** Face detection with keypoints for emotion recognition
- **Video Analytics:** Real-time face and landmark detection in video streams
- **Media Organization:** Automated face detection with alignment for media libraries

### Supported Domains

- Broadcasting and media production
- Entertainment
- Human-Computer Interaction

## Release Date:
03/12/2026

## Model Architecture

### Architecture Details

- **Backbone:** ResNet-inspired efficient backbone
- **Detection Framework:** SCRFD (Sample and Computation Redistribution for Face Detection)
- **Detection Method:** Anchor-free detection with stride-based feature pyramids
- **Feature Pyramid Network:** Multi-scale feature extraction
- **Landmark Prediction:** 5-point facial landmarks (two eyes, nose, two mouth corners)
- **Number of model parameters:** 3.9 million (10 GFLOPS variant)

### SCRFD Architecture Highlights

- **Sample Redistribution:** Efficient positive/negative sample assignment strategy
- **Computation Redistribution:** Optimized computation allocation across detection heads
- **Anchor-Free Design:** Direct prediction without predefined anchors
- **Multi-Task Learning:** Simultaneous face detection and landmark localization

## Input(s):
**Input Type:** Image

**Input Format:**
- Input name: `input_image`
- Color format: Red, Green, Blue (RGB)
- Data type: fp32, fp16
- Shape: [1, 3, 640, 640] (NCHW format)

**Input Parameters:**
- Image: Two-Dimensional (2D) (width, height) = (640, 640)
- Pre-processing:
- Division by 255.0
- Resize image to (640, 640) using bilinear interpolation, preserve aspect ratio, zero-padding
- Mean normalization: [127.5, 127.5, 127.5]
- Standard deviation: [128.0, 128.0, 128.0]

## Output(s)

**Output Type(s):**
For each detected face:
- Bounding boxes (x1, y1, x2, y2) in image space
- Confidence score
- 5 facial landmarks (x, y coordinates for each keypoint: eye centers, nose, mouth corners)

**Output Format(s):**
- Bounding Box: 4 fp32/fp16 values per detection
- Confidence score: 1 fp32/fp16 value per detection
- Landmarks: 10 fp32/fp16 values per detection (5 points × 2D coordinates)

**Output Parameters:**
- `bboxes`: Nx4 fp32/fp16 array (N detections, 4 coordinates each)
- `scores`: Nx1 fp32/fp16 array (N confidence scores)
- `landmarks`: Nx10 fp32/fp16 array (N detections, 10 landmark coordinates)

### Post-processing

- **Score Thresholding:** Applied to filter low-confidence detections (default: 0.5)
- **Non-Maximum Suppression (NMS):** Applied with default IoU threshold of 0.4
- **Landmark Refinement:** Direct landmark coordinate prediction in image space
- **Optional Face Selection:** Supports limiting detections to top-N faces by confidence or area

# Performance

### Inference Characteristics

- **Optimized Runtime:** TensorRT (NVIDIA), ONNX Runtime
- **Supported Hardware:** NVIDIA GPUs CC 7.5 and up with TensorRT support
- **Precision:** FP32 (supports FP16/INT8 optimization)
- **Typical Latency:** Real-time performance on modern NVIDIA GPUs (~5-10ms on RTX 3080)
- **Memory Footprint:** Lightweight design optimized for edge and datacenter deployment

### Detection Metrics

- **Default Confidence Threshold:** 0.50
- **Default IoU Threshold:** 0.40 (NMS)
- **Detection Capabilities:** Multiple face detection per frame with landmarks
- **Landmark Points:** 5 keypoints (left eye, right eye, nose tip, left mouth corner, right mouth corner)
- **Face Selection Modes:**
- `max`: Select faces by maximum area
- `center`: Select faces closest to image center with area weighting

## Limitations

### Known Constraints

- **Occlusion Sensitivity:** Detection and landmark accuracy may degrade with partial face occlusions (masks, sunglasses, hands)
- **Lighting Conditions:** Reduced accuracy in extreme low-light or high-contrast scenarios
- **Face Pose:** Optimized for frontal and near-frontal faces; extreme profile views (>60° yaw) may have lower detection rates and less accurate landmarks
- **Face Size:** Performance varies based on face size in the image; very small faces (<20×20 pixels) may not be detected reliably
- **Landmark Accuracy:** 5-point landmarks are sufficient for alignment but not for detailed facial analysis requiring dense landmarks

### Bias and Fairness Considerations

- Model performance may vary across different demographic groups depending on training data composition
- Users should evaluate model performance on their specific target populations
- Consider using diverse test datasets to assess fairness metrics across age, gender, ethnicity, and skin tone

## Training Data

### Dataset Characteristics

The model has been trained on diverse face detection and landmark datasets including:
- Multiple age groups (children, adults, elderly)
- Various ethnicities and skin tones
- Different lighting conditions (indoor, outdoor, natural, artificial)
- Indoor and outdoor scenarios
- Various face poses and expressions
- Occluded and non-occluded faces

Data Collection Method by dataset
- Hybrid: Human, Synthetic images and videos

Labeling Method by dataset
- Hybrid: Human annotators, Automatic/Sensors

**Note:** Training typically involves publicly available datasets such as WIDER FACE, and additional proprietary datasets.

## Inference
- Acceleration Engine: TensorRT 10.9 - 10.13, ONNX Runtime 1.15+
- Test Hardware: Tesla T4, A100, GeForce RTX 3080, GeForce RTX 4090, L40, GH100, Jetson AGX Orin

## Key Considerations

- **Privacy:** Ensure compliance with applicable privacy laws and regulations (GDPR, CCPA, BIPA, etc.)
- **Consent:** Obtain necessary consent for face detection and biometric data collection in applicable jurisdictions
- **Bias Mitigation:** Regularly evaluate and monitor for demographic performance disparities
- **Transparency:** Inform end-users when face detection and landmark extraction technology is in use
- **Data Retention:** Establish policies for retention and deletion of facial data

## References

### Technical Papers

- **SCRFD:** Guo, J., Deng, J., Lattas, A., & Zafeiriou, S. (2021). "Sample and Computation Redistribution for Efficient Face Detection." *arXiv preprint arXiv:2105.04714*. [Paper Link](https://arxiv.org/abs/2105.04714)

### Related Resources

- [InsightFace GitHub Repository](https://github.com/deepinsight/insightface)
- [InsightFace SCRFD Documentation](https://github.com/deepinsight/insightface/tree/master/detection/scrfd)
- [NVIDIA TensorRT Documentation](https://docs.nvidia.com/deeplearning/tensorrt/)
- [NVIDIA NGC Catalog](https://catalog.ngc.nvidia.com/)
- [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/)

### Biometric Data Considerations
This model extracts facial landmarks which may be considered biometric data under certain regulations (e.g., BIPA in Illinois). Users must:
- Obtain informed consent before collecting biometric data
- Clearly disclose the purpose and duration of data storage
- Implement appropriate security measures to protect biometric data
- Provide mechanisms for data subject rights (access, deletion)

---

## SyncDiscriminator

### Model Overview:

The SyncDiscriminator model determines whether a visible person in a video frame is actively speaking, using both audio and visual cues. The model processes face crops from video frames alongside corresponding audio Mel-Frequency Cepstral Coefficient (MFCC) features to produce a per-frame speaking detection score.

This model is ready for commercial/non-commercial use.

### License/Terms of Use

GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: [MIT](https://github.com/Junhua-Liao/LR-ASD/blob/main/LICENSE).

### Deployment Geography:

Global

### Use Case:

NVIDIA AR SDK developers building video communication and content creation applications that require identifying which person in a scene is currently speaking.

### Release Date:

NGC - 03/12/2026 via [URL](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/maxine/models/nvaractivespeakerdetection)

### References(s):

* [NVIDIA AR SDK Developer Page](https://developer.nvidia.com/ai-for-media)

## Model Architecture:

**Architecture Type:** Convolutional Neural Network (CNN), Recurrent Neural Network (RNN)

**Network Architecture:** 3D CNN, 2D CNN, Gated Recurrent Unit (GRU)

- This model was developed based on a lightweight audio-visual architecture with separate visual and audio encoders, gated concatenation fusion, and a bidirectional GRU temporal detector.
- Number of model parameters 8.4 x 10^5

## Input(s):

**Input Type(s):** Video (Face Crops), Audio

**Input Format(s):**

- Video: Grayscale
- Audio: MFCC (Mel-Frequency Cepstral Coefficients)

**Input Parameters:**

- Video: Three-Dimensional (3D)
- Audio: Two-Dimensional (2D)

**Other Properties Related to Input:** Video: Grayscale face crops resized to 112x112 pixels with zero-centered pixel intensity normalization; variable length up to 6 seconds, variable frame rates supported. Audio: MFCC coefficients extracted to yield 4 MFCC frames per video frame.

## Output(s):

**Output Type(s):** Score

**Output Format(s):**

- Float32

**Output Parameters:**

- One-Dimensional (1D)

**Other Properties Related to Output:** Per-frame active speaker detection score (raw logit). A score greater than 0.0 indicates the person is speaking. One score is produced per input video frame.

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Training and Evaluation Datasets:

- The total size (in number of data points): 28,726 training tracks and 7,753 validation tracks (AVA-ActiveSpeaker), plus 6,635 evaluation clips (VoxCeleb2/TalkSet) and Columbia ASD (5 speakers)
- Total number of datasets: 4 (AVA-ActiveSpeaker train, AVA-ActiveSpeaker validation, Columbia ASD, VoxCeleb2/TalkSet)
- Dataset partition: Training [79%], evaluation [21%] (AVA train/val split; Columbia ASD and VoxCeleb2/TalkSet are evaluation-only datasets)

### Training Dataset:

- AVA-ActiveSpeaker Dataset

**Data Collection Method by dataset**
Hybrid: Human and Automated

**Labeling Method by dataset**
Hybrid: Human and Automated

**Properties:**
The AVA-ActiveSpeaker dataset contains face tracks and corresponding audio from Hollywood movie clips. Each face track is annotated with a binary speaking/not-speaking label at the frame level. The training set contains approximately 3.6 million entity-level annotations across 120 15-minute movie segments. Face crops are extracted using S3face detection and tracking.

**Data Modality**

- Video
- Audio

**Video Training Data Size**

- Less than 10,000 Hours

### Evaluation Dataset:

- AVA-ActiveSpeaker Validation Set
- Columbia ASD Dataset
- VoxCeleb2/TalkSet Validation Set

**Benchmark Score:**

AVA validation: mAP = 94.44%. Columbia ASD: F1 = 87.23% (averaged across 5 speakers, evaluated with 3-second duration).

**Data Collection Method by dataset**
Hybrid: Human and Automated

**Labeling Method by dataset**
Hybrid: Human and Automated

**Properties:**
AVA validation set contains 7,753 tracks across ~33 movie segments with frame-level annotations. Columbia ASD contains panel discussion videos with 5 speakers. VoxCeleb2/TalkSet validation set contains 6,635 clips (TAudio: 2,494, FAudio: 2,072, TFAudio: 2,069) derived from VoxCeleb2 celebrity interview videos with constructed speaking/non-speaking scenarios.

---

# Software Integration:

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

## Inference:
**Engine:** [TensorRT](https://developer.nvidia.com/tensorrt), [Triton](https://developer.nvidia.com/triton-inference-server) <br>
**Test Hardware:**
Desktops and Servers with following GPU architectures:
* NVIDIA Blackwell <br>
* NVIDIA Hopper <br>
* NVIDIA Lovelace <br>
* NVIDIA Ampere <br>
* NVIDIA Turing <br>

# Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Bias, Explainability, Safety & Security, and Privacy Subcards.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Contact and Support

For questions, issues, or support:
- **NVIDIA NGC Support:** [https://ngc.nvidia.com/support](https://ngc.nvidia.com/support)
- **NVIDIA Developer Forums:** [https://forums.developer.nvidia.com/](https://forums.developer.nvidia.com/)

## Get Help
### Enterprise Support
Get access to knowledge base articles and support cases or [submit a ticket](nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Capabilities

- **Function Calling:** Not supported

## Bias

# Face and Landmark Detector:
Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing:  |  None
Measures taken to mitigate against unwanted bias:                                                   |  Dataset rebalancing for fair representation of age, gender, race/skin tones

# SyncDiscriminator:
Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
| Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing: | Age, Gender, Race, Skin color                                                                                                                                                                                                                                                                                     |
| Measures taken to mitigate against unwanted bias:                                                                                                                 | Trained on AVA-ActiveSpeaker dataset which contains diverse demographics from Hollywood movie clips spanning a wide range of ages, genders, races, and skin colors. Evaluated on Columbia ASD dataset with multiple speakers of different backgrounds to verify consistent performance across demographic groups. |

## Explainability

# Face and Landmark Detector:
Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Domain:                                                                                       |  Human face detection and facial landmark localization in images and videos
Model Type:                                                                                            |  CNN with ResNet-inspired backbone using SCRFD architecture
Intended Users:                                                                                        |  Media and Entertainment, Academics/Researchers, Video analytics, Security, Biometrics
Output:                                                                                                |  Bounding box per face detected plus 5 facial keypoints (eyes, nose, mouth corners)
Describe how the model works:                                                                          |  Image input is analyzed by SCRFD model that outputs face bounding boxes with confidence scores and 5 facial landmarks per face. NMS post-processing filters overlapping detections.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Not Applicable
Technical Limitations:                                                                                 |  The model may struggle in poorly lit conditions, with small faces (<20 pixels), extreme head orientations (>60° yaw/pitch), heavy occlusions, and may have reduced landmark accuracy for profile faces.
Verified to have met prescribed NVIDIA quality standards:                                              |  Yes
Performance Metrics:                                                                                   |  mAP (mean Average Precision), NME (Normalized Mean Error) for landmarks
Potential Known Risks:                                                                                 |  The model may fail to detect some faces or provide inaccurate landmarks in instances with poor lighting, small faces, extreme poses, or heavy occlusions. Performance may vary across demographic groups.
Licensing:                                                                                             |  GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

# SyncDiscriminator:
Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Task/Domain:                                                                   |  Video Communication and Content Creation
Model Type:                                                                                            |  Audio-Visual Convolutional and Recurrent Neural Networks (CNN + RNN).
Intended Users:                                                                                        |  This model is intended for developers building video communication and content creation applications that require active speaker detection.
Output:                                                                                                |  Per-frame active speaker detection score (raw logit, threshold 0.0)
Describe how the model works:                                                                          |  The model takes grayscale face crops and audio MFCC features as input. Visual and audio features are extracted through separate CNN encoders, fused via gated concatenation, and processed by a bidirectional GRU detector to produce per-frame speaking scores.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Age, Gender, Race, Skin color.
Technical Limitations & Mitigation:                                                                    |  This model may not perform well with extreme audio noise, heavily occluded faces, very small face regions, or when multiple overlapping speakers are present.
Verified to have met prescribed NVIDIA quality standards:  |  Yes
Performance Metrics:                                                                                   |  Mean Average Precision (mAP), F1 Score, Latency, Throughput
Potential Known Risks:                                                                                 |  This model may produce incorrect speaking predictions in noisy environments or when face detection quality is poor, potentially leading to incorrect speaker attribution.
Licensing:                                                                                             |  GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: [MIT](https://github.com/Junhua-Liao/LR-ASD/blob/main/LICENSE).

## Privacy

# Face and Landmark Detector:
Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                     |  Potentially: Facial landmarks can be considered biometric identifiers under certain regulations
Personal data used to create this model?                                                                                       |  No
Was consent obtained for any personal data used?                                                                                             |  Yes
How often is dataset reviewed?                                                                                                     |  Before Every Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Yes
If personal data was collected for the development of the model, was it collected directly by NVIDIA?                                            |  No
If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  N/A
If personal data was collected for the development of this AI model, was it minimized to only what was required?                                 |  N/A
Is there provenance for all datasets used in training?                                                                                |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  No, not possible with externally-sourced data.
| Applicable Privacy Policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  [NVIDIA Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/)                                                                |

# SyncDiscriminator:
Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                     |  No
Personal data used to create this model?                                                                                       |  Yes
Was consent obtained for any personal data used?                                                                                             |  Unknown (Externally-Sourced Data)
How often is dataset reviewed?                                                                                                     |  At the onset of the project and when needed during the development.
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Unknown (Externally-Sourced Data)
If personal data was collected for the development of the model, was it collected directly by NVIDIA?                                            | No
If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  | Not Applicable
If personal data was collected for the development of this AI model, was it minimized to only what was required?                                 |  Unknown (Externally-Sourced Data)
Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model?                                         |  No
Is there provenance for all datasets used in training?                                                                                |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  No, not possible with externally-sourced data
Applicable Privacy Policy        |  https://www.nvidia.com/en-us/about-nvidia/privacy-policy/

## Safety & Security

# Face and Landmark Detector:
Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  The model detects faces and facial landmarks in inputs that can be video, single or multiple images. The output includes bounding boxes (4 2D image coordinates) and 5 facial keypoints (10 2D coordinates) per detected face.
Describe the life critical impact (if present).   |  Not Applicable
Use Case Restrictions:                              |  GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Users must comply with applicable biometric data regulations (e.g., BIPA, GDPR Article 9) when using landmark detection features.
Model and dataset restrictions:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. Facial landmark data is considered biometric information in many jurisdictions.

# SyncDiscriminator:
Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application Field(s):                               |  Video Communication, Content Creation
Describe the life critical impact (if present).   |  Not Applicable <br>
Use Case Restrictions:                              |   GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: [MIT](https://github.com/Junhua-Liao/LR-ASD/blob/main/LICENSE).
Model and dataset restrictions:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.