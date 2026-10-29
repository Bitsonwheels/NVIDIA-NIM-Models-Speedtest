---
title: "genmol"
publisher: "nvidia"
type: "endpoint"
updated: "2025-07-21T16:23:28.815Z"
description: "Fragment-Based Molecular Generation by Discrete Diffusion."
canonical: "https://build.nvidia.com/nvidia/genmol-generate"
---

# Model Overview

### Description:

GenMol v2.0 (NV-GenMol-89M-v2) is a masked diffusion model<sup>1</sup> trained on molecular Sequential Attachment-based Fragment Embedding ([SAFE](https://arxiv.org/abs/2310.10773)) representations<sup>2</sup> for fragment-based molecule generation, which can serve as a generalist model for various drug discovery tasks, including De Novo generation​, linker design​, motif extension​, scaffold decoration/morphing​, hit generation​, and lead optimization. NV-GenMol-89M-v2 was developed by NVIDIA as part of the BioNeMo NIM family. <br>

This model is ready for commercial use.

### License/Terms of Use:

Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.

### Deployment Geography:

Global

### Use Case:

GenMol is intended for computational chemists, drug discovery researchers, and AI/ML scientists performing fragment-based molecular generation tasks including de novo generation, linker design, motif extension, scaffold decoration/morphing, hit generation, and lead optimization.

### Release Date:
- build.nvidia.com: May 05, 2026 at [build.nvidia.com/nvidia/genmol-generate](https://build.nvidia.com/nvidia/genmol-generate)
- NGC: May 05, 2026 at [catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/genmol)

## References:

```
@misc{sahoo2024simpleeffectivemaskeddiffusion,
title={Simple and Effective Masked Diffusion Language Models}, 
author={Subham Sekhar Sahoo and Marianne Arriola and Yair Schiff and Aaron Gokaslan and Edgar Marroquin and Justin T Chiu and Alexander Rush and Volodymyr Kuleshov},
year={2024},
eprint={2406.07524},
archivePrefix={arXiv},
primaryClass={cs.CL},
url={https://arxiv.org/abs/2406.07524}, 
}
```

```
@misc{noutahi2023gottasafenewframework,
title={Gotta be SAFE: A New Framework for Molecular Design}, 
author={Emmanuel Noutahi and Cristian Gabellini and Michael Craig and Jonathan S. C Lim and Prudencio Tossou},
year={2023},
eprint={2310.10773},
archivePrefix={arXiv},
primaryClass={cs.LG},
url={https://arxiv.org/abs/2310.10773}, 
}
```

## Model Architecture:
**Architecture Type:** Transformer <br>
**Network Architecture:** BERT <br>
**Number of model parameters:** 89M <br>

## Input(s):
**Input Type(s):** Text (Molecular Sequence), Number (Molecules to generate, temperature scaling factor, noise scaling factor), Enumeration (Scoring method), Binary (Showing unique molecules only) <br>
**Input Format(s):** Text: String (Sequential Attachment-based Fragment Embedding (SAFE)); Number: Integer, FP32; Enumeration: String (QED, LogP); Binary: Boolean <br>
**Input Parameters:** 1D <br>
**Other Properties Related to Input:** Maximum input length is 512 tokens.

## Output(s):
**Output Type(s):** Text (List of molecule sequences), Number (List of scores) <br>
**Output Format(s):** Text: Array of string (Sequential Attachment-based Fragment Embedding (SAFE)); Number: Array of FP32 (Scores) <br>
**Output Parameters:** 2D <br>
**Other Properties Related to Output:** Maximum output length is 512 tokens. <br>

## Software Integration:
**Runtime Engine(s):** <br>
* PyTorch >= 2.5.1 <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Lovelace <br>
* NVIDIA Hopper <br>
* NVIDIA Grace Hopper <br>
* NVIDIA Blackwell <br>
* NVIDIA Grace Blackwell <br>

**Supported Operating System(s):** <br>
* Linux <br>

## Model Version(s):
GenMol v2.0 <br>

## Training, Testing, and Evaluation Datasets:

### Training Dataset:

**Link:** SAFE-GPT [GitHub](https://github.com/datamol-io/safe), [HuggingFace](https://huggingface.co/datasets/datamol-io/safe-gpt) <br>
**Data Collection Method by dataset:** Automated <br>
**Labeling Method by dataset:** Automated <br>
**Properties:** 1.1B SAFE strings consist of various molecule types (drug-like compounds, peptides, multi-fragment molecules, polymers, reagents and non-small molecules). <br>

### Testing Dataset:

**Link:** SAFE-GPT [GitHub](https://github.com/datamol-io/safe), [HuggingFace](https://huggingface.co/datasets/datamol-io/safe-gpt) <br>
**Data Collection Method by dataset:** Automated <br>
**Labeling Method by dataset:** Automated <br>
**Properties:** 1.1B SAFE strings consist of various molecule types (drug-like compounds, peptides, multi-fragment molecules, polymers, reagents and non-small molecules). <br>

### Evaluation Dataset:

**Link:** SAFE-DRUGS [GitHub](https://github.com/datamol-io/safe), [HuggingFace](https://huggingface.co/datasets/datamol-io/safe-drugs) <br>
**Data Collection Method by dataset:** Not Applicable <br>
**Labeling Method by dataset:** Not Applicable <br>
**Properties:** SAFE-DRUGS consists of 26 known therapeutic drugs. <br>

## Inference:
**Acceleration Engine:** PyTorch <br>
**Test Hardware:** NVIDIA RTX 6000 Ada, NVIDIA A10G, NVIDIA A100, NVIDIA L40S, NVIDIA H100, NVIDIA H200, NVIDIA GH200, NVIDIA B200, NVIDIA GB200, NVIDIA B300, NVIDIA GB300, NVIDIA RTX 6000 Blackwell Workstation, NVIDIA DGX Spark <br>

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Users are responsible for ensuring the physical properties of model-generated molecules are appropriately evaluated and comply with applicable safety regulations and ethical standards.

For more detailed information on ethical considerations for this model, please see the Model Card++ [Explainability](explainability.md), [Bias](bias.md), [Safety & Security](safety.md), and [Privacy](privacy.md) Subcards.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

|Field|Response|
|:---|:---|
|Participation considerations from adversely impacted groups ([protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/)) in model design and testing|Not Applicable|
|Measures taken to mitigate against unwanted bias|Not Applicable|
|Bias Metric (If Measured)|Not Applicable|

## Explainability

|Field|Response|
|:---|:---|
|Intended Application(s) & Domain(s)|Molecular drug discovery and design|
|Model Type|Molecular sequence generation|
|Intended Users|Developers in the academic or pharmaceutical industries who build artificial intelligence applications to perform property guided molecule optimization and novel molecule generation.|
|Output|Text (molecule sequence)|
|Describe how the model works|From the input of a molecular sequence (SAFE format) with masks (masking tokens), the neural network model (Transformer & BERT architecture) will one-by-one predict the best characters (valid tokens in the chemistry vocabulary) to replace the masking tokens, until all masks are replaced, which is an unmasking process by discrete diffusion.|
|Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of|Not Applicable|
|Technical Limitations & Mitigation|Model may not perform well on sequences that are highly divergent from the ZINC-15 dataset.|
|Verified to have met prescribed quality standards?|Yes|
|Performance Metrics|Validity, Uniqueness, Diversity, Central Distance, Qualified Ratio.|
|Potential Known Risks|The model may produce molecules that are difficult or impossible in synthesis.|
|Licensing|The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and the [Product-Specific Terms for NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/); use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). ADDITIONAL INFORMATION: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).|

## Privacy

|Field|Response|
|:---|:---|
|Generatable or reverse engineerable personal data?|No|
|Personal data used to create this model?|No|
|Was consent obtained for any personal data used?|Not Applicable|
|How often is dataset reviewed?|Before Every Release|
|Was data from user interactions with the AI model (e.g. user input and prompts) used to train the model?|No|
|Is there provenance for all datasets used in training?|Yes|
|Does data labeling (annotation, metadata) comply with privacy laws?|Yes|
|Is data compliant with data subject requests for data correction or removal, if such a request was made?|Not Applicable|
|Applicable Privacy Policy|[NVIDIA Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/)|

## Safety & Security

|Field|Response|
|:---|:---|
|Model Application(s)|Molecular drug discovery and design|
Experimental drug discovery and medicine: Additional in silico and in vitro tests are recommended before using the proteins for downstream applications.
|Use Case Restrictions|Abide by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/), the [Product-Specific Terms for NVIDIA AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/), and the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). ADDITIONAL INFORMATION: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).|
|Model and Dataset Restrictions|The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.|

## Prototype

```bash
#!/usr/bin/env bash

invoke_url='https://health.api.nvidia.com/v1/biology/nvidia/genmol/generate'

authorization_header="Authorization: Bearer $NVIDIA_API_KEY"
content_type_header='Content-Type: application/json'

data='{
"smiles": "",
"num_molecules": ,
"temperature": ,
"noise": ,
"scoring": ""
}'

response=$(curl --silent -i -w "%{http_code}" --request POST \
--url "$invoke_url" \
--header "$authorization_header" \
--header "$content_type_header" \
--data "$data"\
)

echo "$response"
```

```python
import requests

invoke_url = "https://health.api.nvidia.com/v1/biology/nvidia/genmol/generate"

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

payload = {
"smiles": "",
"num_molecules": ,
"temperature": ,
"noise": ,
"scoring": ""
}

# re-use connections
session = requests.Session()

response = session.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)
```