---
title: "riva-translate-1.6b"
publisher: "nvidia"
type: "endpoint"
updated: "2025-06-26T19:40:20.620Z"
description: "Enable smooth global interactions in 36 languages."
canonical: "https://build.nvidia.com/nvidia/riva-translate-1_6b"
---

## Description:
The Riva Translate 1.6B Multilingual Neural Machine Translation model translates text in any to any directions across the 37 supported languages, including non-English centric translation (such as French to Chinese, etc). The Supported languages are: English(en), Czech(cs), Danish (da), German(de), Greek(el), European Spanish(es-ES), LATAM Spanish(es-US), Finnish(fi), France(fr), Hungarian(hu), Italian(it), Lithuanian(lt), Latvian(lv),Dutch(nl), Norwegian(no), Polish(pl), European Portuguese(pt-PT), Brazillian Portuguese(pt-BR), Romanian(ro), Russian(ru), Slovak(sk), Swedish(sv), Simplified Chinese(zh-CN), Traditional Chinese(zh-TW), Japanese(ja), Hindi(hi), Korean(ko), Estonian(et), Slovenian(sl), Bulgarian(bg), Ukrainian(uk), Croatian(hr), Arabic(ar), Vietnamese(vi), Turkish(tr), Indonesian(id), Thai(th). This model is ready for commercial use. 

## Model Architecture

Architecture Type: Transformer

Network Architecture: Megatron

The model is based on Transformer architecture originally presented in "Attention Is All You Need" paper [1]. In this particular instance, the model has 24 layers in the encoder and 24 layers in the decoder. It is using SentencePiece tokenizer [2].

## Input: 
**Input Type(s):** Text String <br>
**Input Format(s):** List <br>

**Other Properties Related to Input:** No Pre-Processing Needed; No Tokenization required; 512 Character Text String Limit (No non-textual characters) <br>

## Output: 
**Output Type(s):** Text String <br>
**Output Format:** List <br>
**Output Parameters:** Selected Language <br>
**Other Properties Related to Output:** Outputs are not tokenized or processed to hide sensitive input information <br>

# Training & Evaluation Dataset: 

** Data Collection Method by dataset <br>
* Human <br>

** Labeling Method by dataset <br>
* Automated <br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** This model is trained on open-sourced datasets and synthetic datasets of text parallel corpora generated via back-translation. <br>

## References:
[1] Vaswani, Ashish, et al. "Attention is all you need." arXiv preprint arXiv:1706.03762 (2017).
[2] https://github.com/google/sentencepiece
[3] https://en.wikipedia.org/wiki/BLEU
[4] https://github.com/mjpost/sacreBLEU
[5] NVIDIA NeMo Toolkit

## Software Integration
**Runtime Engine(s):** 
* Riva 2.19.0 or Higher <br>

**Supported Operating System(s):**  <br>
* Linux <br>

## Model Version(s): 
riva-translate-1.6b<br>

# Inference
**Engine:** Triton <br>
**Test Hardware:**  <br>
* NVIDIA H100 GPU
* NVIDIA A100 GPU
* NVIDIA L40 GPU

## Ethical Considerations (For NVIDIA Models Only):
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## GOVERNING TERMS: 
This trial is governed by the NVIDIA API Trial Terms of Service (found at https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). The use of this model is governed by the AI Foundation Models Community License Agreement (found at NVIDIA Agreements | Enterprise Software | NVIDIA AI Foundation Models Community License Agreement).

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Participation considerations from adversely impacted groups ([protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/)) in model design and testing:  |  Not Applicable
Measures taken to mitigate against unwanted bias:                                                   |    Sourced diverse dataset from East Asia, South Asia, Latin America, and North America annotated by different gender." See https://www.arxiv-vanity.com/papers/2106.03193/ for more details.

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Applications & Domains:                                                                       | Text and Document Translation
Types:                                                                                                 | Text translation
Intended Users:                                                                                        | This model is intended for our developers to perform text and document translation.
Output:                                                                                                | Text (in Target Language)
Describe how the model works:                                                                          | Model translates text in one language into in target language.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  | Not Applicable
Technical Limitations:                                                                                 | Translations may not be 100% accurate. Accuracy varies based on the characteristics of input (Domain, Use Case, Noise, Context, etcetera). Grammar errors and semantic issues may be present.
Verified to have met prescribed NVIDIA quality standards:                                                     | Yes
Performance Metrics:                                                                                   | BiLingual Evaluation Understudy (BLEU) Scores, Crosslingual Optimized Metric for Evaluation of Translation (COMET)
Potential Known Risks:                                                                                 | None.
Licensing:                                                                                             | [Riva](https:developer.nvidia.com/riva/ga/license)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personally-identifiable information (PII)?                                                     | None
Was consent obtained for any PII used?                                                                                             | Not Applicable
Protected class data used to create this model?                                                                                    | Not Applicable
How often is dataset reviewed?                                                                                                     | Before Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        | No
If PII collected for the development of the model, was it collected directly by NVIDIA?                                            | Not Applicable
If PII collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  | Not Applicable
If PII collected for the development of this AI model, was it minimized to only what was required?                                 | Not Applicable
Is there provenance for all datasets used in training?                                                                                                                          | Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                | Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           | No, not possible with externally-sourced data.

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               | Language Translation
Describe the life-critical impacts (if present).   | Not Applicable
Use Case Restriction(s):                              | Abide by https://developer.nvidia.com/riva/ga/license
Model and Dataset Restriction(s):                       | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.