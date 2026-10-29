---
title: "proteinmpnn"
publisher: "ipd"
type: "endpoint"
updated: "2025-07-22T08:47:16.211Z"
description: "ProteinMPNN is a deep learning model for predicting amino acid sequences for protein backbones."
canonical: "https://build.nvidia.com/ipd/proteinmpnn"
---

## Model Overview

### Description:

ProteinMPNN (Protein Message Passing Neural Network) is a deep learning-based graph neural network designed to predict amino acid sequences for given protein backbones. This network leverages evolutionary, functional, and structural information to generate sequences that are likely to fold into the desired 3D structures.

This model is available for commercial use.
<br>

### Third-Party Community Consideration

This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party's requirements for this application and use case.

#### License / Terms of Use

GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Service Terms of Use](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Community Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). Additional Information: [MIT](https://github.com/dauparas/ProteinMPNN/blob/8907e6671bfbfc92303b5f79c4b5e6ce47cdef57/LICENSE).

The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and [Product-Specific Terms for AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). Users must accept the license terms on the [NGC container page](https://catalog.ngc.nvidia.com/orgs/nim/teams/ipd/containers/proteinmpnn) before pulling the container image.

Use of the models in this Blueprint is governed by the [NVIDIA AI Foundation Models Community License](https://docs.nvidia.com/ai-foundation-models-community-license.pdf).

**You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.**

### Deployment Geography
Global

### Use Case
ProteinMPNN enables researchers and commercial entities in the Drug Discovery, Life Sciences, and Protein Engineering fields to design amino acid sequences that fold into desired 3D protein structures. It is particularly useful for de novo protein design, enzyme engineering, and therapeutic protein development.

### Release Date
build.nvidia.com: 7/27/2026 via [build.nvidia.com/ipd/proteinmpnn](https://build.nvidia.com/ipd/proteinmpnn) <br>
NGC: 7/27/2026 via [catalog.ngc.nvidia.com](https://catalog.ngc.nvidia.com/orgs/nim/teams/ipd/containers/proteinmpnn) <br>

### References:

```
@article{dauparas2022robust,
title={Robust deep learning--based protein sequence design using ProteinMPNN},
author={Dauparas, Justas and Anishchenko, Ivan and Bennett, Nathaniel and Bai, Hua and Ragotte, Robert J and Milles, Lukas F and Wicky, Basile IM and Courbet, Alexis and de Haas, Rob J and Bethel, Neville and others},
journal={Science},
volume={378},
number={6615},  
pages={49--56},
year={2022},
publisher={American Association for the Advancement of Science}
}
```

<br>

### Model Architecture:

**Architecture Type:** Protein Amino Acid Sequence Prediction <br>
**Network Architecture:** ProteinMPNN <br>
**Number of Model Parameters:** 1.7 million <br>

### Input:

**Input Type(s):** Protein in Protein Data Bank (PDB) format <br>
**Input Format(s):** String <br>
**Input Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Input:** Accepts protein backbone structures in PDB format. <br>

### Output:

**Output Type(s):** Amino Acid Sequence <br>
**Output Format:** Multi-FASTA (text file) <br>
**Output Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:** Generates sequences predicted to fold into the input backbone structure. <br>
Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. <br>

### Software Integration:

**Runtime Engine(s):**
* Triton <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Blackwell, NVIDIA Hopper, NVIDIA Ampere, NVIDIA Lovelace <br>

**Supported Operating System:** <br>
* [Linux] <br>
* The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

### Model Version(s):

ProteinMPNN 1.0.0 <br>

## Training & Evaluation:

### Training Dataset:
** Data Modality <br>
* [Other: 3D Protein Structures]

**Link:** [The Protein Data Bank](https://www.rcsb.org/) <br>
** Data Collection Method by dataset <br>
* Hybrid: Automatic, Human <br>

For PDB dataset, scientists worldwide submit structural data determined by X-ray crystallography or cryo-electron microscopy (cryo-EM). This includes atomic coordinates, experimental data, and metadata about the biological macromolecules.

** Labeling Method by dataset <br>
* Hybrid: Automatic, Human <br>

For PDB dataset, expert biocurators review the submitted data to ensure accuracy and completeness. This involves checking the plausibility of the data and annotating it with relevant biological and chemical information. CATH 4.1 dataset is derived from the PDB dataset. The CATH (Class, Architecture, Topology, Homologous superfamily) database hierarchically classifies protein domain structures that are obtained from protein structures deposited in the PDB. The data in CATH are specifically sourced from PDB files and include structures determined at a resolution of 4 angstrom or better. The classification process involves both manual and automated methods to ensure accurate domain identification and classification. For ProteinMPNN, the data underwent quality filtering to ensure high accuracy, this involved removing structures with low resolution and potential errors.

**Properties:**
Model was trained by Institute for Protein Design. The dataset for training consisted of 23,358 sequences. Dataset: CATH 4.2, PDB. Sensors: X-ray crystallography, cryoEM.

### Evaluation Dataset:

**Link:** [The Protein Data Bank](https://www.rcsb.org/) <br>
** Data Collection Method by dataset <br>
* Automatic: random splits from PDB dataset. <br>

** Labeling Method by dataset <br>
* Automatic: random splits from PDB dataset. <br>

**Properties:**
The training, validation, and test splits were derived from protein assemblies in the PDB, which includes structures determined by X-ray crystallography or cryo-electron microscopy (cryoEM). The dataset was divided into random splits with 23,358 sequences for training, 1,464 for validation, and 1,529 for testing.

### Inference:

**Acceleration Engine:** Triton <br>
**Test Hardware:** <br>
* NVIDIA Ampere A100 <br>
* NVIDIA Blackwell B200 <br>
* NVIDIA Blackwell B300 <br>
* NVIDIA Blackwell RTX PRO 6000 Blackwell Workstation Edition <br>
* NVIDIA Grace Blackwell GB10 Superchip (DGX Spark) <br>
* NVIDIA Grace Blackwell GB200 Superchip <br>
* NVIDIA Grace Blackwell GB300 Superchip <br>
* NVIDIA Grace Hopper GH200 Superchip <br>
* NVIDIA Hopper H100 <br>
* NVIDIA Hopper H200 <br>
* NVIDIA Lovelace L40S <br>
* NVIDIA RTX6000-Ada <br>

### Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

**You are responsible for ensuring the physical properties of model-generated molecules are appropriately evaluated, and comply with applicable safety regulations and ethical standards.**

# Get Help
## Enterprise Support
Get access to knowledge base articles and support cases or [submit a ticket](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Capabilities

- **Function Calling:** Not supported

## Prototype

```bash
#!/usr/bin/env bash
set -e

URL=${URL:-https://health.api.nvidia.com/v1/biology/ipd/proteinmpnn/predict}

if [ ! -e 1R42.pdb ]; then curl -O https://files.rcsb.org/download/1R42.pdb; fi

pdb=$(cat 1R42.pdb | grep ^ATOM | head -n 200 | awk '{printf "%s\\n", $0}')

request='{
"input_pdb": "'"$pdb"'",
"ca_only": false,
"use_soluble_model": false,
"sampling_temp": [0.1]
}'
curl -H 'Content-Type: application/json' \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "nvcf-poll-seconds: 300" \
-d "$request" "$URL"
```

```python
#!/usr/bin/env python3
import requests
import os
import json
from pathlib import Path

def get_reduced_pdb():
pdb = Path("1R42.pdb")
if not pdb.exists():
pdb.write_text(requests.get(f"https://files.rcsb.org/download/{pdb}").text)
lines = filter(lambda line: line.startswith("ATOM"), pdb.read_text().split("\n"))
return "\n".join(list(lines)[:200])

r = requests.post(
url=os.getenv("URL", "https://health.api.nvidia.com/v1/biology/ipd/proteinmpnn/predict"),
headers={"Authorization": "Bearer $NVIDIA_API_KEY"},
json={
"input_pdb": get_reduced_pdb(),
"ca_only": False,
"use_soluble_model": False,
"sampling_temp": [0.1],
},
)
print(r, "Saving to output.fa:\n", r.text[:200], "...")
Path("output.fa").write_text(json.loads(r.text)["mfasta"])
```