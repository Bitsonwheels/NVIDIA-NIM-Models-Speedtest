---
title: "nemotron-3.5-embed-8b"
publisher: "nvidia"
type: "endpoint"
updated: "2026-10-20T23:06:32.594Z"
description: "8B multimodal embedding model for text and document-image retrieval in RAG applications."
canonical: "https://build.nvidia.com/nvidia/nemotron-3_5-embed-8b"
---

# Nemotron-3.5-Embed-8B-BF16

## Description:
**Nemotron-3.5-Embed-8B-BF16** is a world-class, versatile embedding model trained by NVIDIA and optimized for multimodal and multilingual question-answering retrieval. The model can embed document pages in the form of image, text, or combined image–text inputs. Documents can be retrieved given a user query in text form. The model supports page images containing text, tables, charts, and infographics. For text retrieval, the model was evaluated across 34 languages: English, Arabic, Assamese, Bengali, Bulgarian, Chinese, Danish, Dutch, Finnish, French, German, Hindi, Hinglish, Indonesian, Italian, Japanese, Korean, Malay, Marathi, Nepali, Norwegian, Persian, Portuguese, Romanian, Russian, Spanish, Swahili, Swedish, Tamil, Telugu, Thai, Ukrainian, Urdu, and Vietnamese. For image retrieval, it was evaluated across 18 languages: Arabic, Bengali, Chinese, English, Persian, Finnish, French, German, Hindi, Indonesian, Japanese, Korean, Russian, Spanish, Swahili, Telugu, Thai, and Yoruba. The model may support additional languages beyond these evaluation sets.

_This model is ready for commercial or non-commercial use._

This Model Card describes the NVIDIA API Catalog Preview API for **Nemotron-3.5-Embed-8B-BF16**.

## License and Terms of Use:

**Governing Hosted-Service Terms:** Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). <br>
**Governing Download Terms:** Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). <br>
**Additional Information:** [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) for Ministral-3-8B-Instruct-2512-BF16.

## Deployment Geography:
Global

## Use Case:
The **Nemotron-3.5-Embed-8B-BF16** is suitable for users who want to build a multimodal question-and-answer application over a large corpus, leveraging the latest dense retrieval technology. The input of the model is a text or document image and the output is a fixed-size embedding vector. The embedding model is a bi-encoder that supports context in textual format (e.g. the query or the OCR text of a page or a section of a document) or the image of a document page.
Typically, the embedding model is used first to embed (vectorize) the whole corpus (document images or text chunks), and embeddings are stored in a vector database associated to its raw content (image or text). Then at inference time, the embedding model is used to embed the query. The model generates dense vector embeddings from text or image inputs, enabling multimodal retrieval, semantic search, and (agentic) RAG workflows. <br>

## Release Date:

**Build.NVIDIA.com:** 10/19/2026 via [Nemotron 3.5 Embed 8B Preview API](https://build.nvidia.com/nvidia/nemotron-3_5-embed-8b) <br>
**Hugging Face:** 10/20/2026 via [model card](https://huggingface.co/nvidia/Nemotron-3.5-Embed-8B-BF16)

## Model Architecture:
**Architecture Type:** Transformer <br>
**Network Architecture:** `Nemotron-3.5-Embed-8B-BF16` architecture with the Vision Encoder initialized from [mistralai/Ministral-3-8B-Instruct-2512-BF16](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512-BF16) and the LLM component initialized from [nvidia/Nemotron-3-Embed-8B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16). <br>
**Total Parameters:** 8.38B

The language-model component of `Nemotron-3.5-Embed-8B-BF16` is initialized from [Nemotron-3-Embed-8B-BF16](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16) and kept frozen, preserving that model's text retrieval accuracy while adding image retrieval capabilities. The two models therefore share the same embedding space and produce identical text embeddings. During fine-tuning, only the vision encoder and multimodal projector were trained, on image and combined image-text datasets.

### Input:
**Input Type(s):** Text, Image <br>
**Input Format(s):** Text: String; Image: Red, Green, Blue (RGB) <br>
**Input Parameters:** Text: One-Dimensional (1D), Image: Two-Dimensional (2D) <br>
**Other Properties Related to Input:** The model supports image and/or text inputs. For queries, the model accepts text input only. For documents, it accepts an image, text, or a combination of image + text. The default image `longest_edge` is 1,120 pixels, and it can be increased up to 1,540 pixels. The model’s max context length is 32,768 tokens.

### Output:
**Output Type(s):** Embeddings <br>
**Output Format:** Vector <br>
**Output Parameters:** One-Dimensional (1D) per input <br>
**Other Properties Related to Output:** Token-level hidden states are mean-pooled and then L2-normalized to produce one 4096-dimensional embedding vector for each input. The model also supports dynamic embedding sizes by truncating the vector from the end (e.g., retaining the first 1024 or 512 dimensions). The truncated embeddings remain effective for retrieval, provided they are L2-normalized after truncation.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## Software Integration:
**Runtime Engine(s):** Native CUDA backend: Photon Engine

**Supported Hardware Microarchitecture Compatibility:**
* NVIDIA Ampere
* NVIDIA Blackwell
* NVIDIA Hopper
* NVIDIA Lovelace

**Supported Operating System(s):** Linux <br>

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## Model Version(s):
**Nemotron-3.5-Embed-8B-BF16**

## Training, Testing, and Evaluation Datasets:

### Training Dataset:

**Data Modality:**
* Image
* Text

**Image Training Data Size:** 2.3M samples containing images, with or without accompanying text <br>
**Text Training Data Size:** 50M+ text-only data samples <br>
**Data Collection Method by dataset:** Automated, Manually-Labeled, Synthetic <br>
**Labeling Method by dataset:** Automated, Manually-Labeled, Synthetic <br>
**Properties:** Training was conducted using publicly available, commercially permissible datasets and synthetically generated datasets.

#### Public Datasets:
The language model in **Nemotron-3.5-Embed-8B-BF16** was trained on more than 50 million text-only samples from the datasets listed in the [Nemotron-3-Embed-8B-BF16 Model Card](https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16#dataset-overview). In addition, the following publicly available datasets were used to train the vision encoder and multimodal projector on image-only or combined image-text inputs.

| Dataset name | Reference |
| --- | --- |
| ArxivQA | [https://huggingface.co/datasets/MMInstruction/ArxivQA](https://huggingface.co/datasets/MMInstruction/ArxivQA) |
| ColPali-PDF | [https://huggingface.co/datasets/vidore/colpali_train_set](https://huggingface.co/datasets/vidore/colpali_train_set) |
| InfoVQA | [https://www.docvqa.org/datasets/infographicvqa](https://www.docvqa.org/datasets/infographicvqa) |
| TAT-DQA | [https://github.com/NExTplusplus/TAT-DQA](https://github.com/NExTplusplus/TAT-DQA) |
| docmatix-ir | [https://huggingface.co/datasets/Tevatron/docmatix-ir](https://huggingface.co/datasets/Tevatron/docmatix-ir) |
| Docmatix | [https://huggingface.co/datasets/HuggingFaceM4/Docmatix](https://huggingface.co/datasets/HuggingFaceM4/Docmatix) |
| wiki-ss-nq | [https://huggingface.co/datasets/Tevatron/wiki-ss-nq](https://huggingface.co/datasets/Tevatron/wiki-ss-nq) |

Synthetic datasets were created either by generating queries from seed documents or by generating complete question–answer pairs through LLM-based prompting using the models listed below.

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

### Testing Dataset:

**Data Collection Method by dataset:** Not Applicable <br>
**Labeling Method by dataset:** Not Applicable <br>
**Properties:** Not Applicable. Model quality was assessed using the evaluation benchmark datasets described in the Evaluation Dataset subsection.

### Evaluation Dataset:
**Benchmark**:
- [ViDoRe V3](https://huggingface.co/blog/QuentinJG/introducing-vidore-v3)
- [MIRACL-VISION](https://huggingface.co/datasets/nvidia/miracl-vision) <br>

**Benchmark Score:** NDCG@10 <br>

The **Nemotron-3.5-Embed-8B-BF16** and **Nemotron-3.5-Embed-1B-BF16** were evaluated with the models' default image `longest_edge` of 1,120 pixels. [Qwen3-VL-Embedding-8B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B) and [Qwen3-VL-Embedding-2B](https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B) were evaluated with `max_pixels` set to 1,843,200. <br>

Model training and evaluations used `transformers==5.12.1`.

The 8B BF16 model achieves NDCG@10 scores of 60.39 (image), 60.65 (text), and 61.47 (image + text) on ViDoRe V3, and 70.15 (image) on MIRACL-VISION.

<details>
<summary><strong>Detailed Benchmark Comparison Table</strong></summary>

<table>
<tr>
<th rowspan="2">Model</th>
<th colspan="3" style="text-align: center">ViDoRe V3</th>
<th colspan="1">MIRACL-VISION</th>
</tr>
<tr>
<th>image</th>
<th>text</th>
<th>image + text</th>
<th>image</th>
</tr>
<tr>
<td><a href="https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B">Qwen3-VL-Embedding-2B</a></td>
<td>52.89</td>
<td>48.31</td>
<td>51.97</td>
<td>56.19</td>
</tr>
<tr>
<td><a href="https://huggingface.co/nvidia/Nemotron-3.5-Embed-1B-BF16">Nemotron-3.5-Embed-1B-BF16</a></td>
<td><strong>58.02</strong></td>
<td><strong>57.80</strong></td>
<td><strong>58.82</strong></td>
<td><strong>66.56</strong></td>
</tr>
<tr>
<td><a href="https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B">Qwen3-VL-Embedding-8B</a></td>
<td>58.29</td>
<td>53.69</td>
<td>57.03</td>
<td>65.87</td>
</tr>
<tr>
<td><strong>Nemotron-3.5-Embed-8B-BF16</strong></td>
<td><strong>60.39</strong></td>
<td><strong>60.65</strong></td>
<td><strong>61.47</strong></td>
<td><strong>70.15</strong></td>
</tr>
</table>

</details>

**Data Collection Method by dataset:** Automated, Manually-Labeled, Synthetic <br>
**Labeling Method by dataset:** Automated, Manually-Labeled, Synthetic <br>
**Properties:** `ViDoRe V3` is a visual document retrieval benchmark covering 8 public and 2 private datasets across professional domains. `MIRACL-VISION` is a multilingual visual retrieval dataset for 18 different languages. It is an extension of MIRACL, a popular text-only multilingual retrieval dataset.

## Inference:
**Acceleration Engine:** Native CUDA backend: Photon Engine <br>
**Test Hardware:**

* NVIDIA Ampere (A100)
* NVIDIA Ampere (A10G)
* NVIDIA Blackwell (GB200)
* NVIDIA Blackwell (GB10)
* NVIDIA Blackwell (RTX PRO 6000 Blackwell Server Edition)
* NVIDIA Hopper (H100)
* NVIDIA Hopper (H100 NVL)
* NVIDIA Lovelace (L40S)

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br>
Please make sure you have proper rights and permissions for all input image and video content; if image or video includes people, personal health information, or intellectual property, the image or video generated will not blur or maintain proportions of image subjects included. <br>
For more detailed information on ethical considerations for this model, please see the Explainability, Bias, Safety, and Privacy subcards. <br>
Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

# Bias

**Model:** Nemotron-3.5-Embed-8B-BF16

| Field | Response |
| ----- | ----- |
| Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing: | None |
| Measures taken to mitigate against unwanted bias: | None |
| Bias Metric (If Measured): | Not Applicable |

## Explainability

# Explainability

**Model:** Nemotron-3.5-Embed-8B-BF16

| Field | Response |
| ----- | ----- |
| Intended Task/Domain: | Document and query embedding for question and answer retrieval. |
| Model Type: | Transformer encoder |
| Intended Users: | Generative AI creators working with conversational AI models - users who want to build a multilingual and multimodal question and answer application over a large document corpus, leveraging the latest dense retrieval technologies. |
| Output: | Array of float numbers (Dense Vector Representation for the input text or image) |
| Describe how the model works: | Model transforms the tokenized input into a dense vector representation. |
| List the groups (or group characteristics) for which this was tested to produce comparable outcomes: | Not Applicable |
| Technical Limitations & Mitigation: | The model’s max sequence length is 32768. Therefore, the longer inputs should be truncated. |
| Verified to have met prescribed NVIDIA quality standards: | Yes |
| Performance Metrics: | Accuracy, Latency and Throughput|
| Potential Known Risks: | This model does not always guarantee to retrieve the correct document(s) for a given query. |
| Licensing: | Governing hosting terms: Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). Governing download terms: Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). Additional information: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) for Ministral-3-8B-Instruct-2512-BF16. |

## Privacy

# Privacy

**Model:** Nemotron-3.5-Embed-8B-BF16

The datasets used to train this model were reviewed before release. Please review [NVIDIA’s Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) for more information.

## Safety & Security

# Safety & Security

**Model:** Nemotron-3.5-Embed-8B-BF16

| Field | Response |
| ----- | ----- |
| Model Application Field(s): | Document Embedding for Retrieval. User queries can be text and documents can be text, document page images, charts, tables, and infographics. |
| Describe the life critical impact (if present). | Not Applicable |
| Use Case Restrictions: | Governing hosting terms: Use of this trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). Governing download terms: Use of the model is governed by the [OpenMDW License Agreement, version 1.1](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1). Additional information: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) for Ministral-3-8B-Instruct-2512-BF16.|
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |

## Prototype

```bash
image_source="https://assets.ngc.nvidia.com/products/api-catalog/nemotron-rerank-vl/example1.jpg"
if [[ $image_source == http* ]]; then
base64_image=$(curl -s "${image_source}" | base64 -w 0)
else
base64_image=$(base64 -w 0 < "${image_source}")
fi

json_payload='{
"input": ["data:image/png;base64,'"${base64_image}"'"],
"model": "nvidia/nemotron-3.5-embed-8b",
"modality": ["image"],
"input_type": "",
"encoding_format": "float",
"truncate": "END"
}'

echo "${json_payload}" | \
curl -X POST https://integrate.api.nvidia.com/v1/embeddings \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-d @-
```

```python
import base64
import requests
from openai import OpenAI

image_source = "https://assets.ngc.nvidia.com/products/api-catalog/nemotron-rerank-vl/example1.jpg"

if image_source.startswith(('http://', 'https://')):
response = requests.get(image_source)
image_b64 = base64.b64encode(response.content).decode()
else:
with open(image_source, "rb") as image_file:
image_b64 = base64.b64encode(image_file.read()).decode()

client = OpenAI(
api_key="$NVIDIA_API_KEY",
base_url="https://integrate.api.nvidia.com/v1"
)

response = client.embeddings.create(
input=[f"data:image/png;base64,{image_b64}"],
model="nvidia/nemotron-3.5-embed-8b",
encoding_format="float",
extra_body={"modality": ["image"], "input_type": "", "truncate": "END"}
)

print(response.data[0].embedding)
```

```python
import base64
import requests
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

image_source = "https://assets.ngc.nvidia.com/products/api-catalog/nemotron-rerank-vl/example1.jpg"

if image_source.startswith(('http://', 'https://')):
response = requests.get(image_source)
image_b64 = base64.b64encode(response.content).decode()
else:
with open(image_source, "rb") as image_file:
image_b64 = base64.b64encode(image_file.read()).decode()

client = NVIDIAEmbeddings(
model="nvidia/nemotron-3.5-embed-8b",
api_key="$NVIDIA_API_KEY",
truncate="END",
)

image_input = f"data:image/png;base64,{image_b64}"

embedding = client.embed_documents([image_input])
print(embedding)
```