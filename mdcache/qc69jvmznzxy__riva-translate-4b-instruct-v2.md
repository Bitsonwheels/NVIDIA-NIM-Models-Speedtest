---
title: "riva-translate-4b-instruct-v2"
publisher: "nvidia"
type: "endpoint"
updated: "2026-07-27T17:35:59.075Z"
description: "Translation model in 37 languages with few-shots example prompts capability."
canonical: "https://build.nvidia.com/nvidia/riva-translate-4b-instruct-v2"
---

# Riva-Translate-4B-Instruct-v2

## Description

The Riva-Translate-4B-Instruct-v2 Neural Machine Translation model translates text in English and 36 non-English languages. The supported languages are: English(en), Czech(cs), Danish(da), German(de), Greek(el), European Spanish(es-ES), LATAM Spanish(es-US), Finnish(fi), French(fr), Hungarian(hu), Italian(it), Lithuanian(lt), Latvian(lv), Dutch(nl), Norwegian(no), Polish(pl), European Portuguese(pt-PT), Brazilian Portuguese(pt-BR), Romanian(ro), Russian(ru), Slovak(sk), Swedish(sv), Simplified Chinese(zh-CN), Traditional Chinese(zh-TW), Japanese(ja), Hindi(hi), Korean(ko), Estonian(et), Slovenian(sl), Bulgarian(bg), Ukrainian(uk), Croatian(hr), Arabic(ar), Vietnamese(vi), Turkish(tr), Indonesian(id), Thai(th).

It supports both sentence- and document-level translation. The model surpasses all in-house NMT models we've built so far.

*This model is ready for commercial or non-commercial use.*

## License and Terms of Use:

GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

## Deployment Geography:

Global

## Use Case:

Translators, marketers, and web developers who deliver content in multiple languages.

## Release Date:

Build.nvidia.com 07/27/2026 via [Link](https://build.nvidia.com/nvidia/riva-translate-4b-instruct-v2)

## Reference(s):

1. [Vaswani, Ashish, et al. "Attention Is All You Need." arXiv:1706.03762 (2017).](https://arxiv.org/abs/1706.03762)
2. <https://github.com/openai/tiktoken>
3. <https://en.wikipedia.org/wiki/BLEU>
4. <https://github.com/mjpost/sacreBLEU>
5. <https://github.com/Unbabel/COMET>
6. [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)

## Model Architecture:

**Architecture Type:** Transformer  
**Network Architecture:** Decoder-only

This model was developed based on Transformer architecture originally presented in "Attention Is All You Need" paper [1]. It is a fine-tuned version of a 4B Base model that was pruned and distilled from nvidia/Mistral-NeMo-Minitron-8B-Base using our LLM compression technique. The model was trained using a multi-stage CPT and SFT. It uses tiktoken [2] as the tokenizer. The model supports a context length of 8K tokens. The model has 4,179,704,832, parameters.

### Input:

**Input Types:** Text  
**Input Formats:** String  
**Input Parameters:** One-Dimensional (1D)  
**Other Input Properties:** This model supports a context length of 8K.

### Output:

**Output Types:** Text  
**Output Format:** String  
**Output Parameters:** One-Dimensional (1D)  
**Other Output Properties:** This model supports a context length of 8K.

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Prompt Format

We recommend using the following prompt template, which was used to fine-tune the model. The model may not perform optimally without it.

```python
messages = [
{
"role": "system",
"content": "en-zh-cn",
},
{"role": "user", "content": "The GRACE mission is a collaboration between the NASA and German Aerospace Center.?"},
]
```

## Software Integration:

**Runtime Engine(s):** NeMo Framework 24.09

**Supported Hardware Microarchitecture Compatibility:**

- NVIDIA Ampere
- NVIDIA Blackwell
- NVIDIA Hopper
- NVIDIA Lovelace

**Supported Operating System(s):**

- Linux

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Model Version(s)

Riva-Translate-4B-Instruct-v2

## Training, Testing, and Evaluation Datasets:

### Training Dataset

**Data Modality:** Text  
**Text Training Data Size:** 1 Billion to 10 Trillion Tokens  
**Training Data Collection:** Hybrid: Human, Synthetic  
**Training Labeling:** Hybrid: Human, Synthetic  
**Training Properties:** No personal data; copyright protected content. The training set consists of pairs of source text with its translation. The style of the translations ranges from conversational to formal.

### Testing Dataset

**Testing Data Collection:** Automated  
**Testing Labeling:** Human  
**Testing Properties:** [FLORES-101](https://huggingface.co/datasets/gsarti/flores_101). No personal data; copyright protected content. The test set consists of pairs of source text with its translation. The style of the translations ranges from conversational to formal.

### Evaluation Dataset

**Evaluation Data Collection:** Automated  
**Evaluation Labeling:** Human  
**Evaluation Properties:** [FLORES-101](https://huggingface.co/datasets/gsarti/flores_101). No personal data; copyright protected content. The evaluation set consists of pairs of source text with its translation. The style of the translations ranges from conversational to formal.

### Benchmark Score

sacreBLEU and WMT20-COMET-da scores for any2en and en2any directions

| Language               | Eng -> Language (BLEU / COMET) | Language -> Eng (BLEU / COMET) |
|------------------------|--------------------------------|--------------------------------|
| Czech                  | 29.1 / 0.900                   | 40.6 / 0.752                   |
| Danish                 | 42.7 / 0.839                   | 48.0 / 0.833                   |
| German                 | 36.3 / 0.666                   | 44.4 / 0.769                   |
| Greek                  | 22.4 / 0.720                   | 36.7 / 0.731                   |
| European Spanish       | 28.6 / 0.759                   | 32.5 / 0.748                   |
| Latin America Spanish  | 28.6 / 0.757                   | 32.5 / 0.748                   |
| Finnish                | 19.9 / 0.936                   | 34.2 / 0.761                   |
| French                 | 47.8 / 0.823                   | 45.1 / 0.817                   |
| Hungarian              | 21.0 / 0.882                   | 35.5 / 0.747                   |
| Italian                | 28.0 / 0.753                   | 35.0 / 0.759                   |
| Lithuanian             | 21.9 / 0.911                   | 34.1 / 0.648                   |
| Latvian                | 26.2 / 0.879                   | 35.4 / 0.707                   |
| Dutch                  | 24.2 / 0.620                   | 32.3 / 0.695                   |
| Norwegian              | 29.9 / 0.805                   | 43.4 / 0.798                   |
| Polish                 | 18.0 / 0.736                   | 31.1 / 0.672                   |
| European Portuguese    | 43.3 / 0.875                   | 49.3 / 0.838                   |
| Brazil Portuguese      | 47.8 / 0.899                   | 49.3 / 0.838                   |
| Romanian               | 37.2 / 0.894                   | 43.7 / 0.800                   |
| Russian                | 28.8 / 0.728                   | 36.5 / 0.674                   |
| Slovak                 | 29.4 / 0.891                   | 39.3 / 0.736                   |
| Swedish                | 40.3 / 0.857                   | 47.4 / 0.830                   |
| Simplified Chinese     | 39.7 / 0.673                   | 29.8 / 0.716                   |
| Traditional Chinese    | 34.1 / 0.662                   | 28.6 / 0.701                   |
| Japanese               | 32.4 / 0.712                   | 28.0 / 0.686                   |
| Hindi                  | 24.8 / 0.754                   | 38.7 / 0.737                   |
| Korean                 | 28.6 / 0.715                   | 30.0 / 0.702                   |
| Estonian               | 22.2 / 0.978                   | 36.9 / 0.753                   |
| Slovenian              | 26.3 / 0.826                   | 35.1 / 0.697                   |
| Bulgarian              | 35.8 / 0.827                   | 41.4 / 0.735                   |
| Ukrainian              | 25.8 / 0.749                   | 39.5 / 0.695                   |
| Croatian               | 24.7 / 0.818                   | 37.7 / 0.709                   |
| Arabic                 | 24.6 / 0.614                   | 40.1 / 0.712                   |
| Vietnamese             | 37.7 / 0.710                   | 36.7 / 0.734                   |
| Turkish                | 22.5 / 0.945                   | 37.3 / 0.754                   |
| Indonesian             | 42.4 / 0.851                   | 43.8 / 0.812                   |
| Thai                   | 27.8 / 0.449                   | 29.4 / 0.667                   |
| **Average**            | **30.58 / 0.789**              | **37.76 / 0.742**              |

## Inference

**Acceleration Engine:** vLLM  
**Test Hardware:** NVIDIA Ampere (A100), NVIDIA Ampere (A10G), NVIDIA Hopper (H100), NVIDIA Lovelace (L40S)

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Specifications

- **Parameters:** 4,179,704,832

## Capabilities

- **Function Calling:** Not supported

## Bias

| Field | Response |
|:--|:--|
| Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing: | None |
| Bias Metric: | Not measured |
| Measures taken to mitigate against unwanted bias: | We balanced the number of training data in each language domain. |

## Explainability

| Field | Response |
|:--|:--|
| Intended Task/Domain: | Text-to-Text translation |
| Model Type: | Decoder-only Transformer |
| Intended Users: | Translators, marketers, and web developers who deliver content in multiple languages. |
| Output: | Text translated into the target language |
| Describe how the model works: | The model takes text in the source language as input and translates it into the target language as text. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Not Applicable |
| Technical Limitations & Mitigation: | Accuracy varies based on the characteristics of the input (domain, use case, noise, context, etc.). Grammatical errors and semantic issues may be present. As a potential mitigation, users can adjust the prompt to improve translation quality. |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics: | BLEU and COMET scores. |
| Potential Known Risks: | Translations may not be 100% accurate. This is not recommended for word-for-word translation. |
| Licensing: | GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |

## Privacy

| Field | Response |
|:--|:--|
| Generatable or reverse engineerable personal data? | No |
| Personal data used to create this model? | No |
| How often is dataset reviewed? | Dataset is initially reviewed upon addition, and subsequent reviews are conducted as needed or upon request for changes. |
| Is there provenance for all datasets used in training? | Yes. |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes. |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | Yes |
| Was consent obtained for any personal data used? | Not Applicable |
| Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model? | No |
| Applicable Privacy Policy | [Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) |

## Safety & Security

| Field | Response |
|:--|:--|
| Model Application Field(s): | Media and entertainment, as well as web content creation. |
| Describe the life critical impact (if present). | Not Applicable |
| Use Case Restrictions: | Abide by [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). |
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |

## Prototype

```python
from openai import OpenAI

client = OpenAI(
base_url = "https://integrate.api.nvidia.com/v1",
api_key = "$NVIDIA_API_KEY"
)

completion = client.chat.completions.create(
model="",
messages=[{"role":"user","content":""}],
temperature=,
top_p=,
max_tokens=,
stream=NaN
)

print(completion.choices[0].message)
```

```python
from langchain_nvidia_ai_endpoints import ChatNVIDIA

client = ChatNVIDIA(
model="",
api_key="$NVIDIA_API_KEY", 
temperature=,
top_p=,
max_tokens=,
)

response = client.invoke([{"role":"user","content":""}])
print(response.content)
```

```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
apiKey: '$NVIDIA_API_KEY',
baseURL: 'https://integrate.api.nvidia.com/v1',
})

async function main() {
const completion = await openai.chat.completions.create({
model: "",
messages: [{"role":"user","content":""}],
temperature: ,
top_p: ,
max_tokens: ,
stream: 
})

process.stdout.write(completion.choices[0]?.message?.content);

}

main();
```

```bash
invoke_url='https://integrate.api.nvidia.com/v1/chat/completions'

authorization_header='Authorization: Bearer '
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data=$'{
"messages": [
{
"role": "user",
"content": ""
}
]
}'

response=$(curl --silent -i -w "\n%{http_code}" --request POST \
--url "$invoke_url" \
--header "$authorization_header" \
--header "$accept_header" \
--header "$content_type_header" \
--data "$data"
)

echo "$response"
```