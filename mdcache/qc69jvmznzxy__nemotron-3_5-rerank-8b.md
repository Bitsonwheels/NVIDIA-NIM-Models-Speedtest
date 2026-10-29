---
title: "nemotron-3.5-rerank-8b"
publisher: "nvidia"
type: "endpoint"
updated: "2026-10-20T23:06:40.172Z"
description: "8B multimodal reranking model that scores how relevant a text or document-image passage is to a query."
canonical: "https://build.nvidia.com/nvidia/nemotron-3_5-rerank-8b"
---

# Nemotron-3.5-Rerank-8B-BF16

## Description

**Nemotron-3.5-Rerank-8B-BF16** was developed by NVIDIA for multilingual and multimodal question-answering retrieval. It is a world-class reranker optimized to produce a logit representing the relevance of a document to a text query. Documents may contain text, page images, or both, including charts, tables, and infographics. The model can be integrated into classical or agentic vision RAG pipelines. For text retrieval, the model was evaluated across 34 languages: English, Arabic, Assamese, Bengali, Bulgarian, Chinese, Danish, Dutch, Finnish, French, German, Hindi, Hinglish, Indonesian, Italian, Japanese, Korean, Malay, Marathi, Nepali, Norwegian, Persian, Portuguese, Romanian, Russian, Spanish, Swahili, Swedish, Tamil, Telugu, Thai, Ukrainian, Urdu, and Vietnamese. For image retrieval, it was evaluated across 18 languages: Arabic, Bengali, Chinese, English, Persian, Finnish, French, German, Hindi, Indonesian, Japanese, Korean, Russian, Spanish, Swahili, Telugu, Thai, and Yoruba. The model may support additional languages beyond these evaluation sets.

*This model is ready for commercial or non-commercial use.*

## License and Terms of Use:

**GOVERNING HOSTING TERMS:** Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). Additional Information: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) for Ministral-3-8B-Instruct-2512-BF16.

## Deployment Geography:

Global

## Use Case:

**Use Case:** The reranking model serves as a key component of a multimodal retrieval system, such as a vision RAG pipeline, where it helps improve overall retrieval accuracy. A multimodal retrieval system typically uses a multimodal embedding model (dense retrieval) to return a set of potentially relevant documents given an input query. The reranking model then evaluates these candidate documents in greater detail and reorders them based on their relevance to the query, producing a final ranking. By refining the initial retrieval results, the reranking stage can improve the precision of the retrieved documents and ultimately lead to more accurate downstream responses.  

## Release Date:

**Build.NVIDIA.com:** 10/20/2026 (planned) via [model page](https://build.nvidia.com/nvidia/nemotron-3_5-rerank-8b)  
**Hugging Face:** 10/20/2026 via [model card](https://huggingface.co/nvidia/Nemotron-3.5-Rerank-8B-BF16)

## Reference(s):

**References:**

- [Nemotron-3.5-Rerank-8B-BF16 Model Card](https://huggingface.co/nvidia/Nemotron-3.5-Rerank-8B-BF16)
- [Ministral-3-8B-Instruct-2512-BF16](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512-BF16)

## Model Architecture:

**Architecture Type:** Transformer  
**Network Architecture:** The released model contains a Pixtral-based vision encoder and a bidirectional Ministral3 language-model tower. Training proceeded in two stages. In the first stage, an 8B reranker checkpoint derived from the [Ministral-3-8B-Instruct-2512-BF16](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512-BF16) backbone was trained on a blend of text-only datasets. In the second stage, the 8B reranker model initialized from the first-stage checkpoint was trained on image and combined image-text datasets.

**Total Parameters:** 8.38B

### Input:

**Input Types:** Text, Image  
**Input Formats:** Text: String; Image: Red, Green, Blue (RGB)  
**Input Parameters:** Text: One-Dimensional (1D), Image: Two-Dimensional (2D)  
**Other Input Properties:** Each input is one text query paired with one document. The document may be an image, text, or a combination of image and text. The default image `longest_edge` is 1,120 pixels and can be increased to 1,540. The maximum context length is 32,768 tokens.  

### Output:

**Output Types:** Floats  
**Output Formats:** List of Floats  
**Output Parameters:** One-Dimensional (1D)  
**Other Output Properties:** Each output value corresponds to a raw logit. The higher the value, the more relevant a document is to a given query.  

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:

**Runtime Engines:**

- vLLM

**Supported Hardware Microarchitecture Compatibility:**

- NVIDIA Ampere
- NVIDIA Blackwell
- NVIDIA Hopper

**Preferred Operating Systems:** Linux  

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.  

## Model Version(s)

**Nemotron-3.5-Rerank-8B-BF16**  

## Training, Testing, and Evaluation Datasets:

### Training Dataset

**Data Modality:** Text, Image

**Image Training Data Size:** 2.3M samples containing images, with or without accompanying text  
**Text Training Data Size:** 21M text-only data samples  
**Training Data Collection:** Automated, Manually-Labeled, Synthetic  
**Training Labeling:** Hybrid: Automated, Manually-Labeled, Synthetic  
**Training Properties:** Training was conducted using publicly available, commercially permissible datasets and synthetically generated datasets.

<details>
<summary><strong>Public training datasets and synthetic-data sources</strong></summary>

#### Public Datasets:

The language model component of the `Nemotron-3.5-Rerank-8B-BF16` was trained on a blend of text-only dataset files. The public source files used to create text-only training datasets are listed in the [Nemotron-3-Embed-8B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16#dataset-overview) model card.

The following publicly available datasets were also used to train the vision encoder and multimodal projector on image-only and combined image-text inputs.

| Dataset name | Reference |
| --- | --- |
| ArxivQA | [https://huggingface.co/datasets/MMInstruction/ArxivQA](https://huggingface.co/datasets/MMInstruction/ArxivQA) |
| ColPali-PDF | [https://huggingface.co/datasets/vidore/colpali_train_set](https://huggingface.co/datasets/vidore/colpali_train_set) |
| InfoVQA | [https://www.docvqa.org/datasets/infographicvqa](https://www.docvqa.org/datasets/infographicvqa) |
| TAT-DQA | [https://github.com/NExTplusplus/TAT-DQA](https://github.com/NExTplusplus/TAT-DQA) |
| docmatix-ir | [https://huggingface.co/datasets/Tevatron/docmatix-ir](https://huggingface.co/datasets/Tevatron/docmatix-ir) |
| Docmatix | [https://huggingface.co/datasets/HuggingFaceM4/Docmatix](https://huggingface.co/datasets/HuggingFaceM4/Docmatix) |
| wiki-ss-nq | [https://huggingface.co/datasets/Tevatron/wiki-ss-nq](https://huggingface.co/datasets/Tevatron/wiki-ss-nq) |

Synthetic text and image datasets were created either by generating queries from seed documents or by generating complete question–answer pairs through LLM-based prompting using the models listed below.

<table>
<tr>
<th>LLMs used to generate synthetic datasets</th>
</tr>
<tr>
<td>nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16<br>nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4</td>
</tr>
<tr>
<td>Qwen/Qwen3-Next-80B-A3B-Instruct<br>Qwen/Qwen3-235B-A22B<br>Qwen/Qwen3.5-397B-A17B<br>Qwen/Qwen3.5-35B-A3B<br>Qwen/Qwen3.6-27B<br>Qwen/Qwen3.6-35B-A3B<br>Qwen/Qwen3.8-27B</td>
</tr>
<tr>
<td>google/gemma-4-31B-it</td>
</tr>
<tr>
<td>mistralai/Pixtral-12B-2409</td>
</tr>
<tr>
<td>openai/gpt-oss-120b<br>openai/gpt-oss-20b</td>
</tr>
</table>

<table>
<tr>
<th colspan="2">Seed Datasets</th>
</tr>
<tr>
<th>Dataset</th>
<th>Reference</th>
</tr>
<tr>
<td>FinePdfs</td>
<td><a href="https://huggingface.co/datasets/HuggingFaceFW/finepdfs">https://huggingface.co/datasets/HuggingFaceFW/finepdfs</a></td>
</tr>
<tr>
<td>CentralActs</td>
<td><a href="https://zenodo.org/records/5088102">https://zenodo.org/records/5088102</a></td>
</tr>
<tr>
<td>BRIGHT</td>
<td><a href="https://huggingface.co/datasets/xlangai/BRIGHT">https://huggingface.co/datasets/xlangai/BRIGHT</a></td>
</tr>
<tr>
<td>MultiHiertt</td>
<td><a href="https://github.com/psunlpgroup/MultiHiertt">https://github.com/psunlpgroup/MultiHiertt</a></td>
</tr>
<tr>
<td>Digital Corpora</td>
<td><a href="https://digitalcorpora.org/corpora/file-corpora/cc-main-2021-31-pdf-untruncated/">https://digitalcorpora.org/corpora/file-corpora/cc-main-2021-31-pdf-untruncated/</a></td>
</tr>
<tr>
<td>Vdr-multilingual</td>
<td><a href="https://huggingface.co/datasets/llamaindex/vdr-multilingual-train">https://huggingface.co/datasets/llamaindex/vdr-multilingual-train</a></td>
</tr>
</table>

</details>

### Testing Dataset

**Testing Data Collection:** Not Applicable  
**Testing Labeling:** Not Applicable  
**Testing Properties:** Not Applicable. Model quality was assessed using the evaluation benchmark datasets described in the Evaluation Dataset subsection.

### Evaluation Dataset

**Benchmark:**

- [ViDoRe V3](https://huggingface.co/blog/QuentinJG/introducing-vidore-v3)
- [MIRACL-VISION](https://huggingface.co/datasets/nvidia/miracl-vision)  

**Benchmark Score:** NDCG@10  

The `Nemotron-3.5-Rerank-8B-BF16` model was evaluated with the model's default image `longest_edge` set to 1,120 pixels. `Qwen3-VL-Reranker-8B` was evaluated with the model's default `max_pixels` set to 1,310,720. Both models reranked the top 50 candidates retrieved by the [Nemotron-3.5-Embed-8B-BF16](https://huggingface.co/nvidia/Nemotron-3.5-Embed-8B-BF16) model.

<details>
<summary><strong>Detailed Benchmark Comparison Table</strong></summary>

<table>
<tr>
<th rowspan="2">Model</th>
<th colspan="3" style="text-align: center">ViDoRe V3</th>
<th>MIRACL-VISION</th>
</tr>
<tr>
<th>image</th>
<th>text</th>
<th>image + text</th>
<th>image</th>
</tr>
<tr>
<td><a href="https://huggingface.co/nvidia/Nemotron-3.5-Embed-8B-BF16">Nemotron-3.5-Embed-8B-BF16</a></td>
<td>60.39</td>
<td>60.65</td>
<td>61.47</td>
<td>70.15</td>
</tr>
<tr>
<td><a href="https://huggingface.co/Qwen/Qwen3-VL-Reranker-8B">Qwen3-VL-Reranker-8B</a></td>
<td>66.32</td>
<td>65.30</td>
<td>66.49</td>
<td>72.75</td>
</tr>
<tr>
<td><strong>Nemotron-3.5-Rerank-8B-BF16</strong></td>
<td><strong>67.49</strong></td>
<td><strong>67.35</strong></td>
<td><strong>68.09</strong></td>
<td><strong>76.35</strong></td>
</tr>
</table>

</details>

**Evaluation Data Collection:** Automated, Manually-Labeled, Synthetic  
**Evaluation Labeling:** Hybrid: Automated, Manually-Labeled, Synthetic  
**Evaluation Properties:** `ViDoRe V3` is a visual document retrieval benchmark covering 8 public and 2 private datasets across professional domains. `MIRACL-VISION` is a multilingual visual retrieval dataset for 18 different languages. It is an extension of MIRACL, a popular text-only multilingual retrieval dataset.

## Inference

**Acceleration Engine:** vLLM  
**Test Hardware:** NVIDIA Lovelace (L40S)  

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  
Please make sure you have proper rights and permissions for all input image and video content; if image or video includes people, personal health information, or intellectual property, the image or video generated will not blur or maintain proportions of image subjects included.  
For more detailed information on ethical considerations for this model, please see the Explainability, Bias, Safety, and Privacy subcards.
Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

# Bias

| Field | Response |
| ----- | ----- |
| Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing: | None |
| Measures taken to mitigate against unwanted bias: | None |
| Bias Metric (If Measured): | Not Applicable |

## Explainability

# Explainability

| Field | Response |
| ----- | ----- |
| Intended Task/Domain: | Passage or document ranking for question and answer retrieval. |
| Model Type: | Transformer cross-encoder. |
| Intended Users: | Generative AI developers working with conversational AI models. This is suitable for users building question-answering applications over large multimodal corpora and aiming to improve retrieval performance by reranking a set of candidate documents for a given question. The corpus may include visually rich document images (e.g., pages with text, figures, tables, charts, or infographics) and/or text extracted from documents. |
| Output: | List of Floats (Score/Logit indicating if a passage/document relevant to a question). |
| Describe how the model works: | The model outputs a relevance score (logit) reflecting how strongly it predicts that the passage or document contains the information required to answer the question. |
| List the groups (or group characteristics) for which this was tested to produce comparable outcomes: | Not Applicable |
| Technical Limitations & Mitigation: | The model’s max sequence length is 32768 tokens. If the combined text-and-image sequence exceeds that limit, truncate the text or reduce the image resolution until it fits. |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics: | Accuracy, Latency, Throughput |
| Potential Known Risks: | This model does not always guarantee to provide a meaningful ranking of document(s) for a given query. |
| Licensing: | Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). Additional Information: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) for Ministral-3-8B-Instruct-2512-BF16. |

## Privacy

# Privacy

The datasets used to train this model were reviewed before release. Please review [NVIDIA’s Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) for more information.

## Safety & Security

# Safety & Security

| Field | Response |
| ----- | ----- |
| Model Application Field(s): | Document reranking for retrieval. User queries are text. Documents can be text or page images (including pages with charts, tables, and infographics). |
| Describe the life critical impact (if present). | Not Applicable |
| Use Case Restrictions: | Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). Additional Information: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) for Ministral-3-8B-Instruct-2512-BF16. |
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |

## Prototype

```python
import requests

invoke_url = "https://ai.api.nvidia.com/v1/retrieval/nvidia/nemotron-3.5-rerank-8b/reranking"

headers = {
"Authorization": "Bearer ",
"Accept": "application/json",
}

payload = {
"messages": [
{
"role": "user",
"content": ""
}
]
}

# re-use connections
session = requests.Session()

response = session.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)
```

```javascript
import fetch from "node-fetch";

const invokeUrl = "https://ai.api.nvidia.com/v1/retrieval/nvidia/nemotron-3.5-rerank-8b/reranking"

const headers = {
"Authorization": "Bearer ",
"Accept": "application/json",
}

const payload = {
"messages": [
{
"role": "user",
"content": ""
}
]
}

let response = await fetch(invokeUrl, {
method: "post",
body: JSON.stringify(payload),
headers: { "Content-Type": "application/json", ...headers }
});

let response_body = await response.json()

console.log(JSON.stringify(response_body))
```

```bash
invoke_url='https://ai.api.nvidia.com/v1/retrieval/nvidia/nemotron-3.5-rerank-8b/reranking'

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