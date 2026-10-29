---
title: "molmim"
publisher: "nvidia"
type: "endpoint"
updated: "2025-07-18T21:05:23.707Z"
description: "MolMIM performs controlled generation, finding molecules with the right properties."
canonical: "https://build.nvidia.com/nvidia/molmim-generate"
---

# Model Overview

## Description:
MolMIM generates a random sample of new molecules in SMILES format by sampling from the latent space around the point corresponding to the given seed molecule. MolMIM performs optimization with the CMA-ES algorithmin the model’s latent space and sample molecules with improved values of the desired scoring function.

MolMIM is a latent variable model developed by NVIDIA that is trained in an unsupervised manner over a large-scale dataset of molecules in the form of SMILES strings. MolMIM utilizes transformer architecture to learn an informative fixed-size latent space using Mutual Information Machine (MIM) learning. MIM is a learning framework for a latent variable model which promotes informative and clustered latent codes. MolMIM can be used for sampling novel molecules from the model’s latent space.

## References(s):
[Improving Small Molecule Generation using Mutual Information Machine](https://arxiv.org/abs/2208.09016)

[MIM: Mutual Information Machine](https://arxiv.org/abs/1910.03175)

[The CMA Evolution Strategy: A Comparing Review](https://link.springer.com/chapter/10.1007/3-540-32494-1_4)

## Model Architecture:
**Architecture Type:** Encoder-Decoder 
**Network Architecture:** Perceiver <br>

MolMIM utilizes a Perceiver encoder architecture which outputs a fixed-size representation, where molecules of various lengths are mapped into a latent space. MolMIM’s decoder architecture is a Transformer. Both encoder and decoder container 6 layers with a hidden size of 512, 8 attention heads, and a feed-forward dimension of 2048. Total number of parameters in MolMIM is 65.2M. The model was trained with A-MIM learning. <br>

## Input:
**Input Type(s):** Text (Molecular Sequence) <br>
**Input Format(s):** Comma Separated Values, Simplified Molecular-Input Line Entry System (SMILES)  <br>
**Input Parameters:** 1D <br>
**Other Properties Related to Input:** Maximum input length is 512 tokens. Pretraining dataset samples were randomly split into train, validation, and test sets ( 99% / 0.5% / 0.5% ). <br>

## Output: <br>
**Output Type(s):** Text, Numerical <br>
**Output Format:** [SMILES] <br>
**Output Parameters:** [2D] <br>
**Other Properties Related to Output:** Maximum output length is 128 tokens <br> 

## Software Integration:
**Runtime Engine(s):**
* Triton Inference Server<br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* Ampere <br>
* L40 <br>

## Preferred/Supported Operating System(s):
* [Linux] <br>
* [Windows] <br>

## Model Version(s):
MolMIM-24.03  <br>

## Training and Evaluation Dataset:

**Link:** [ZINC-15](https://zinc15.docking.org) <br>

** Data Collection Method by dataset <br>
* Not Applicable <br>

** Labeling Method by dataset <br>
* Not Applicable <br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** 1.54B molecules with molecular weight <= 500 Daltons, LogP <= 5, with reactivity levels rated as  “reactive” and purchasability “annotated.” The compounds were filtered to ensure a maximum length of 512 characters. <br>

## Evaluation Dataset:
**Link:** [MoleculeNet - Lipophilicity, FreeSolv, ESOL](https://deepchem.io/tutorials/an-introduction-to-moleculenet) <br>

** Data Collection Method by dataset <br>
* Hybrid: Human & Automatic/Sensors <br>

** Labeling Method by dataset <br>
* Hybrid: Human & Automated <br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**

[MoleculeNet Physical Chemistry](https://deepchem.io/tutorials/an-introduction-to-moleculenet) is an aggregation of public molecular datasets. The physical chemistry portion of MoleculeNet that we used for evaluation is made up of ESOL (1128 compunds), FreeSolv (642 compunds) and Lipohilicity (4200 compunds).

Zhenqin Wu, Bharath Ramsundar, Evan N. Feinberg, Joseph Gomes, Caleb Geniesse, Aneesh S. Pappu, Karl Leswing, Vijay Pande, [MoleculeNet: A Benchmark for Molecular Machine Learning](https://arxiv.org/abs/1703.00564), arXiv preprint, arXiv: 1703.00564, 2017.

From the MoleculeNet documentation:

* ESOL is made up of water solubility data(log solubility in mols per litre) for common organic small molecules.
* FreeSolv is made up of experimental and calculated hydration free energy of small molecules in water.
* Lipophilicity is composed of experimental results of octanol/water distribution coefficient(logD at pH 7.4).

## Inference:

**Engine:** Tensor(RT) <br>
**Test Hardware:** <br>

* Ampere <br>
* L40  <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Users are responsible for ensuring the physical properties of model-generated molecules are appropriately evaluated and comply with applicable safety regulations and ethical standards.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Participation considerations from adversely impacted groups ([protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/)) in model design and testing:  |  None of the above
Measures taken to mitigate against unwanted bias:                                                   |   None

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Applications & Domains:                                                                       |  Molecular drug discovery and design
Type:                                                                                                 | Molecular Sequence Generation
Intended Users:                                                                                        | This model is intended for developers in the academic or pharmaceutical industries who build artificial intelligence applications to perform property guided molecule optimization and novel molecule generation. 
Output:                                                                                                |  Text (Molecule Sequence)
Describe how the model works:                                                                          |  Computes numerical embeddings for molecular representations and generates similar molecular representations from numerical embeddings
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  None of the Above
Technical Limitations:                                                                                 |  Model may not perform well on sequences that are highly divergent from the ZINC-15 dataset
Verified to have met prescribed quality standards:                                                     | Yes
Performance Metrics:                                                                                   | Similarity, Modelability, Nearest Neighbor Correlation, Validity, Unique, Novelty, Non-Identicality, Effective Novelty, Scaffold Unique, Scaffold Non-Identical Similarity, Scaffold Novelty, Effective Scaffold Novelty, and Entropy
Potential Known Risks:                                                                                 | The model may produce molecules that are invalid; validate with RDKit.
Licensing:                                                                                             | https://docs.nvidia.com/ai-foundation-models-community-license.pdf

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personally-identifiable information (PII)?                                                     |  None
Was consent obtained for any PII used?                                                                                             |   Not Applicable 
How often is dataset reviewed?                                                                                                     |  Before Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Not Applicable 
If PII collected for the development of the model, was it collected directly by NVIDIA?                                            |  Not Applicable
If PII collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  Not Applicable
If PII collected for the development of this AI model, was it minimized to only what was required?                                 |   Not Applicable
Is there provenance for all datasets used in training?                                                                                                                          |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Not Applicable
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  Not Applicable

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               | Small Molecular sampling and generation
Describe the life-critical impacts (if present).   |  None 
Use Case Restriction(s):                              |  Abide by https://docs.nvidia.com/ai-foundation-models-community-license.pdf
Model and Dataset Restriction(s):                       |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered toThe Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.

## Prototype

```bash
invoke_url='https://health.api.nvidia.com/v1/biology/nvidia/molmim/generate'

authorization_header='Authorization: Bearer $NVIDIA_API_KEY'
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data='{
"algorithm": "CMA-ES",
"num_molecules": 30,
"property_name": "QED",
"minimize": false,
"min_similarity": 0.3,
"particles": 30,
"iterations": 10,
"smi": "[H][C@@]12Cc3c[nH]c4cccc(C1=C[C@H](NC(=O)N(CC)CC)CN2C)c34"
}'

response=$(curl --silent -i -w "
%{http_code}" --request POST \
--url "$invoke_url" \
--header "$authorization_header" \
--header "$accept_header" \
--header "$content_type_header" \
--data "$data"
)

echo "$response"
```

```python
import requests

invoke_url = "https://health.api.nvidia.com/v1/biology/nvidia/molmim/generate"

headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"Accept": "application/json",
}

payload = {
"algorithm": "CMA-ES",
"num_molecules": 30,
"property_name": "QED",
"minimize": False,
"min_similarity": 0.3,
"particles": 30,
"iterations": 10,
"smi": "[H][C@@]12Cc3c[nH]c4cccc(C1=C[C@H](NC(=O)N(CC)CC)CN2C)c34"
}

# re-use connections
session = requests.Session()

response = session.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)
```