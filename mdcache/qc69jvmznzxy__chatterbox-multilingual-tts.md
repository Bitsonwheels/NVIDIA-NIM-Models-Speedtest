---
title: "chatterbox-multilingual-tts"
publisher: "resembleai"
type: "endpoint"
updated: "2026-06-03T19:38:39.980Z"
description: "Natural and expressive voices in 23 languages. For voice agents and brand ambassadors."
canonical: "https://build.nvidia.com/resembleai/chatterbox-multilingual-tts"
---

# Chatterbox TTS Multilingual Overview

## Description:  
Chatterbox Multilingual is a 500M-parameter, end-to-end multilingual text-to-speech (TTS) model from Resemble AI. It generates expressive, natural speech across 23 languages using a T3 (Text-to-Speech Token Generator) architecture paired with an S3Gen diffusion-based decoder with flow matching, enabling high-fidelity audio generation and robust cross-lingual synthesis.  
Chatterbox TTS Multilingual was developed by Resemble AI as a part of Chatterbox.  
_This model is ready for commercial/non-commercial use._  

## Third-Party Community Consideration  
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [Resemble AI Model Card](https://huggingface.co/ResembleAI/chatterbox).  

### License/Terms of Use:
Governing Terms: The Chatterbox model governed by the [NVIDIA Open Model Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-agreement/).

ADDITIONAL INFORMATION: The Chatterbox base model is governed by [MIT License](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/mit.md).

### Deployment Geography:  
Global

### Use Case:  
Developers building multilingual voice agents, content localization systems, interactive media, language learning tools, and accessibility applications. Suitable for applications requiring expressive, natural speech synthesis in 23 languages.  

### Release Date: 26-May, 2026
**Build.Nvidia.com:** https://build.nvidia.com/resemble-ai/chatterbox-multilingual  
**NGC:** https://registry.ngc.nvidia.com/orgs/nim/containers/chatterbox-multilingual  
**HuggingFace:** https://huggingface.co/ResembleAI/chatterbox-multilingual  
**GitHub:** https://github.com/resemble-ai/chatterbox  

## Reference(s):
[Resemble AI Chatterbox GitHub](https://github.com/resemble-ai/chatterbox)  
[Chatterbox Multilingual announcement blog](https://www.resemble.ai/chatterbox-multilingual/)  
[Hugging Face model card](https://huggingface.co/ResembleAI/chatterbox-multilingual)  
[PerTh Watermarker GitHub](https://github.com/resemble-ai/perth)  
[NVIDIA API Trial Service Terms of Use / NVIDIA AI Enterprise EULA](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)  

## Model Architecture:   
**Architecture Type:** Transformer   
**Network Architecture:** T3 token generator + S3Gen diffusion decoder with flow matching  
**Number of model parameters:** 500M (5.0*10^8)  

## Input:  
**Input Type(s):** Text  
**Input Format(s):** UTF-8 string  
**Input Parameters:** One-Dimensional (1D)  
**Other Properties Related to Input:** Input text to synthesize. Language code (BCP-47) required. Emotion exaggeration control: float parameter 0.0-1.0 with recommended range 0.4-0.7.  

## Output:  
**Output Type(s):** Audio  
**Output Format:** WAV  
**Output Parameters:** One-Dimensional (1D)  
**Other Properties Related to Output:** Output is 24 kHz, mono, 16-bit PCM WAV audio. Recommended maximum per generation: ~15 seconds of audio.  

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:
**Runtime Engine(s):** Triton    
**Supported Hardware Microarchitecture Compatibility:**
* NVIDIA Ampere
* NVIDIA Hopper
* NVIDIA Lovelace

**Supported Operating System(s):** Linux  

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.  

This AI model can be embedded as an Application Programming Interface (API) call into the software environment described above.  

## Model Version(s): 
Chatterbox Multilingual v1.0  

The model is integrated via NVIDIA NIM (Triton-based microservice) with support for NVIDIA Ampere (A100, A30, A10), Hopper (H100), Lovelace (L4, L40), and Ada (RTX 6000) GPUs. Preferred OS is Linux. The model can be used with the open-source weights or upgraded to the Pro version for enterprise features.  

## Training, Testing, and Evaluation Datasets:  

## Training Dataset:

**Data Modality:** Text  

**Text Training Data Size:** Less than a Billion Tokens  
**Data Collection Method by dataset:** Undisclosed  
**Labeling Method by dataset:** Undisclosed  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Undisclosed

### Testing Dataset:

**Data Collection Method by dataset:** Undisclosed  
**Labeling Method by dataset:** Undisclosed  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Undisclosed

### Evaluation Dataset:
**Benchmark Score:** Undisclosed

**Data Collection Method by dataset:** Undisclosed  
**Labeling Method by dataset:** Undisclosed  
**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Evaluated on diverse multilingual text-to-speech tasks across 23 languages, including stress testing for pronunciation, prosody, and cross-lingual synthesis.

## Key Considerations:
Known limitations include variable quality in non-English languages, pronunciation issues in Castilian Spanish, and boundary artifacts in long text handling.

## Inference:
**Acceleration Engine:** Triton
**Test Hardware:**
- NVIDIA A100 GPU
- NVIDIA A30 GPU
- NVIDIA A10 GPU
- NVIDIA H100 GPU
- NVIDIA L4 GPU
- NVIDIA L40 GPU

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Specifications

- **Parameters:** 331,473,663

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing:  |  None of the Above
Bias Metric (If Measured):                                                   |  Not Applicable
(For GPAI Models): Which characteristic (feature) show(s) the greatest difference in performance?: |  Not Applicable
(For GPAI Models): Which feature(s) have have the worst performance overall? | Not Applicable
Measures taken to mitigate against unwanted bias:                                                   |  None of the Above (No Human-Trained Data)
(For GPAI Models): If using internal data, description of methods implemented in data acquisition or processing, if any, to address the prevalence of identifiable biases in the training, testing, and validation data: | Not Applicable
(For GPAI Models): Tools used to assess statistical imbalances and highlight patterns that may introduce bias into AI models: | Not Applicable
(For GPAI Models): Not Applicable

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Task/Domain:                                                                                       |  Speech & Text
Model Type:                                                                                            |  Transformer
Intended Users:                                                                                        |  Developers building multilingual voice agents, content localization systems, interactive media, language learning tools, and accessibility applications. Suitable for applications requiring expressive, natural speech synthesis in 23 languages.
Output:                                                                                                |  Types: Audio. Formats: WAV
(For GPAI Models): Tools used to evaluate datasets to identify synthetic data and ensure data authenticity | Not Applicable
Describe how the model works:                                                                          |  Chatterbox Multilingual uses a T3 token generator paired with an S3Gen diffusion-based decoder with flow matching to generate expressive, natural speech across 23 languages.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Not Applicable
Technical Limitations and Mitigation:                                                                  |  This model only has the capacity to produce a voice in the language, dialect and gender(s) in which it is trained. This model makes no effort to moderate or modify input text.
Verified to have met prescribed [Insert Company Name Here] quality standards:                          |  Not Applicable
Performance Metrics:                                                                                   |  Accuracy (Top-1)
F-1 Score
Throughput & Latency
Potential Known Risks:                                                                                 |  This model may unnaturally synthesize vocabulary not included in the pronunciation dictionary or omit phonetic symbols not used in training. This model might produce unexpected or inaccurate words or phonemes.
Terms of Use/Licensing:                                                                                |  GOVERNING TERMS: [TO BE PROVIDED BY PRODUCT LEGAL VIA NSPECT WORKFLOW]

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                     |  None
Personal data used to create this model?                      |  None Known
Was consent obtained for any personal data used?                                                                                   |  Not Applicable
(For GPAI Models): Personal data methods | Not Applicable
How often is dataset reviewed?                                                                                                     |  Before Every Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Not Applicable
Was data from user interactions with the AI model used to train the model?                           |  No
Dataset provenance?                                                                             |  Yes
Privacy law compliance?                                                                |  Yes
Applicable Privacy Policy                                                                                                          | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/
(For GPAI Models): Copyright compliance | Not Applicable
(For GPAI Models): PII filtering | Not Applicable

## Safety & Security

Field  |  Response
:------|:---------
Model Application(s):  |  Speech synthesis
Describe the life critical impact (if present).  |  Not Applicable
Model and dataset restrictions:  |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to.
Use case restrictions for the model.  |  Abide by [https://developer.nvidia.com/riva/ga/license](https://developer.nvidia.com/riva/ga/license)