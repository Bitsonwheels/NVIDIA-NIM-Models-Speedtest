---
title: "openfold3"
publisher: "openfold"
type: "endpoint"
updated: "2025-10-24T15:35:18.191Z"
description: "OpenFold3 is a third-generation biomolecular foundation model that predicts the three-dimensional structures of molecular complexes (proteins, DNA, RNA, ligands)"
canonical: "https://build.nvidia.com/openfold/openfold3"
---

# Model Overview

## Description:
OpenFold3 is a biomolecular complex structure prediction model from the [OpenFold Consortium](https://openfold.io/) and the [Alquraishi Laboratory](https://www.aqlab.io/).  OpenFold3 is a pytorch re-implementation of Google Deepmind's [AlphaFold3](https://www.nature.com/articles/s41586-024-07487-w), with support for both training and inference.  See the github repo [https://github.com/aqlaboratory/openfold-3](https://github.com/aqlaboratory/openfold-3).<br>

This model is ready for commercial or non-commercial use.<br>

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to Non-NVIDIA [OpenFold Consortium (AlQuraishi Laboratory, Columbia University) OpenFold3 Model Card](https://huggingface.co/OpenFold/OpenFold3).

### License/Terms of Use:
Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

**You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.**

## Deployment Geography: 
Global

## Use Case
The OpenFold3 NIM can be used at academic and pharmaceutical industry research labs.  The structure prediction functionality supports computer-aided drug design.

## Release Date
- build.nvidia.com: September 1, 2026 at [build.nvidia.com/openfold/openfold3](https://build.nvidia.com/openfold/openfold3)
- NGC: September 1, 2026 at [catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3](https://catalog.ngc.nvidia.com/orgs/nim/teams/openfold/containers/openfold3)

## References:
```
@article{Abramson2024,
author  = {Abramson, Josh and Adler, Jonas and Dunger, Jack and Evans, Richard and Green, Tim and Pritzel, Alexander and Ronneberger, Olaf and Willmore, Lindsay and Ballard, Andrew J. and Bambrick, Joshua and Bodenstein, Sebastian W. and Evans, David A. and Hung, Chia-Chun and O’Neill, Michael and Reiman, David and Tunyasuvunakool, Kathryn and Wu, Zachary and Žemgulytė, Akvilė and Arvaniti, Eirini and Beattie, Charles and Bertolli, Ottavia and Bridgland, Alex and Cherepanov, Alexey and Congreve, Miles and Cowen-Rivers, Alexander I. and Cowie, Andrew and Figurnov, Michael and Fuchs, Fabian B. and Gladman, Hannah and Jain, Rishub and Khan, Yousuf A. and Low, Caroline M. R. and Perlin, Kuba and Potapenko, Anna and Savy, Pascal and Singh, Sukhdeep and Stecula, Adrian and Thillaisundaram, Ashok and Tong, Catherine and Yakneen, Sergei and Zhong, Ellen D. and Zielinski, Michal and Žídek, Augustin and Bapst, Victor and Kohli, Pushmeet and Jaderberg, Max and Hassabis, Demis and Jumper, John M.},
journal = {Nature},
title   = {Accurate structure prediction of biomolecular interactions with AlphaFold 3},
year    = {2024},
volume  = {630},
number  = {8016},
pages   = {493–-500},
doi     = {10.1038/s41586-024-07487-w}
}
```

## Model Architecture:
**Architecture Type:** Protein Structure Prediction <br>
**Network Architecture:** AlphaFold3 <br>
** This model was developed based on AlphaFold3 <br>
** Number of model parameters: 3.68×10⁸

## Input:
**Input Type(s):** Protein Sequence, Multiple Sequence Alignments; DNA Sequence; RNA Sequence; Ligand CCD code; Ligand SMILES code <br>
**Input Format(s):** String (less than or equal to 1000), a3m-format strings, csv-format string, string <br>
**Input Parameters:** One-Dimensional (1D), One-Dimensional (1D), One-Dimensional (1D); One-Dimensional (1D); One-Dimensional (1D);One-Dimensional (1D); One-Dimensional (1D) <br>
**Other Properties Related to Input:** a3m is a standard file format for storing multiple sequence alignment results. a3m-format strings, csv-format string is a standard format for atomic structures <br>

## Output:
**Output Type(s):** Biomolecular Complex Structure(s) in mmCIF format <br>
**Output Format:** mmCIF/PDB (text)<br>
**Output Parameters:** 1D <br>
**Other Properties Related to Output:** Pose (num_atm_ x 3)<br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:
**Runtime Engine(s):**
* TensortRT-BioNeMo <br>
* PyTorch <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Hopper<br>
* NVIDIA Lovelace<br>
* NVIDIA Blackwell<br>

**[Preferred/Supported] Operating System(s):** <br>
* Linux <br>

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment. <br>

## Model Version(s):
* OpenFold Consortium trained weights
* OpenFold3 version 1.6.0 <br>

# Training and Evaluation Datasets:

## Training Dataset:

** Data Modality <br>
* [Other: Protein, DNA and RNA sequences, multiple sequence alignments, ligand specifiers, and 3D biomolecular complex structures]

** Training Data Size <br>
* Non-Audio, Image, Text: ~13 million biomolecular complexes (~400k unique experimental PDB structures plus the distillation datasets).

**Link:** [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w)

The model weights trained by the OpenFold Consortium followed the procedure in [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w).  This data was not collected by NVIDIA. <br>

** Data Collection Method by dataset <br>
* Hybrid: Automatic/Sensors, Manually-Collected
* See the description at [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w). <br>

** Labeling Method by dataset <br>
* Hybrid: Automatic/Sensors, Manually-Labeled
* See the description at [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w). <br>

**Properties:** 

During training, each learning example is composed of the input and the target, where the target is a crop (a piece) of the 3D structure of a biomolecular complex.  The biomolecular complex structure is either (a) experimentally determined, or (b) model-predicted.  The input is composed of the crop-restricted portions of (i) ligand identifiers and protein, DNA, and RNA sequences, (ii) protein and RNA multiple sequence alignments, and (iii) protein structural templates.

The experimental complex structures are sourced from the PDB, and are organized into a 
- Weighted PDB Dataset (~400k unique structures)

The predicted complex structures are organized into 
- Protein Monomer Distillation Dataset
- OF2 code, AF2 weights (checkpoint)
- Short Monomer Distillation Dataset
- OF2 code, AF2 weights (checkpoint)
- Disordered Protein PDB Distillation Dataset
- AF2 Multimer code, AF2 Multimer weights (checkpoint)

In total, these datasets are composed of ~13 million complexes.  Throughout the training process a total of ~20 million sample complex crops are drawn from these datasets, using probability weights described at [Accurate structure prediction of biomolecular interactions with AlphaFold 3, Supplementary Information](https://www.nature.com/articles/s41586-024-07487-w#Sec19).

All of the experimental complex structures in the Weighted PDB Dataset were deposited before 2021-09-30.

For details on the computation of protein and RNA multiple sequence alignments, and protein structure templates, these methods follow [Accurate structure prediction of biomolecular interactions with AlphaFold 3, Supplementary Information](https://www.nature.com/articles/s41586-024-07487-w#Sec19)

## Evaluation Dataset:

**Link:** See the description at [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w). <br>

** Data Collection Method by dataset <br>
* Hybrid: Automatic/Sensors, Manually-Collected
* See the description at [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w). <br>

** Labeling Method by dataset <br>
* Hybrid: Automatic/Sensors, Manually-Labeled
* See the description at [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w). <br>

**Properties:** 

For evaluation (post-validation benchmarks), each learning example has an input and target, similar to the Training Dataset, but not restricted to a crop.  Every complex in the Evaluation Dataset has structure determined after 2021-09-30.

For details on the computation of protein and RNA multiple sequence alignments, and protein structure templates, these methods follow [Accurate structure prediction of biomolecular interactions with AlphaFold 3, Supplementary Information](https://www.nature.com/articles/s41586-024-07487-w#Sec19)

## Inference:
**Acceleration Engine:** TRT, PyTorch <br>
**Test Hardware:** <br>
* NVIDIA A100 <br>
* NVIDIA B200 <br>
* NVIDIA DGX Spark <br>
* NVIDIA GB200 <br>
* NVIDIA GH200 <br>
* NVIDIA H100 <br>
* NVIDIA H200 <br>
* NVIDIA L40s <br>
* NVIDIA RTX PRO 6000 Blackwell Workstation Edition <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns
[here](https://app.intigriti.com/programs/nvidia/nvidiavdp/detail).

# Get Help

## Enterprise Support
Get access to knowledge base articles and support cases or [submit a ticket](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Capabilities

- **Function Calling:** Not supported

## Prototype

```bash
#!/bin/bash
#
# usage
#   (1) Open a bash shell
#   (2) Run the command "export NVIDIA_API_KEY=<your key>"
#   (3) Copy-paste this code into an empty file named example.sh 
#       in the current working directory.
#   (4) Run the command "source example.sh"
#
# notes
#   - Example with protein-DNA complex (PDB: 5GNJ)
#

# Variables
URL="https://health.api.nvidia.com/v1/biology/openfold/openfold3/predict"

# Prepare the JSON data
DATA='{
"request_id": "5GNJ",
"inputs": [
{
"input_id": "5GNJ",
"molecules": [
{
"type": "protein",
"id": "A",
"sequence": "MGREEPLNHVEAERQRREKLNQRFYALRAVVPNVSKMDKASLLGDAIAYINELKSKVVKTESEKLQIKNQLEEVKLELAGRLEHHHHHH",
"msa": {
"main_db": {
"csv": {
"alignment": "key,sequence\n-1,MGREEPLNHVEAERQRREKLNQRFYALRAVVPNVSKMDKASLLGDAIAYINELKSKVVKTESEKLQIKNQLEEVKLELAGRLEHHHHHH",
"format": "csv"
}
}
}
},
{
"type": "dna",
"id": "B",
"sequence": "AGGAACACGTGACCC"
},
{
"type": "dna",
"id": "C",
"sequence": "TGGGTCACGTGTTCC"
}
],
"output_format": "pdb"
}
]
}'

echo "DATA=${DATA}"

# Make the request
echo "Submitting request...the response should arrive in less than a 1 minute"
POLL_SECONDS=300
curl -s -X POST "${URL}" \
-H "content-type: application/json" \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "NVCF-POLL-SECONDS: ${POLL_SECONDS}" \
-d "${DATA}"  &> output.json
```

```python
#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

#
# usage
#   (1) Open a bash shell
#   (2) Run the command "export NVIDIA_API_KEY=<your key>"
#   (3) Copy-paste this code into an empty file named example.py 
#       in the current working directory.
#   (4) Run the command "python example.py"
#   (5) View the response in a newly created file output.json in the same directory.
#
# notes:
#   Example with protein-DNA complex (PDB: 5GNJ)
#
import os
import requests
from pathlib import Path

# ----------------------------
# parameters
# ----------------------------
url = os.getenv("URL", "https://health.api.nvidia.com/v1/biology/openfold/openfold3/predict")
output_file = Path("output.json")

# MSA alignment in CSV format
msa_alignment_csv = (
"key,sequence\n"
"-1,MGREEPLNHVEAERQRREKLNQRFYALRAVVPNVSKMDKASLLGDAIAYINELKSKVVKTESEKLQIKNQLEEVKLELAGRLEHHHHHH"
)

data = {
"request_id": "5GNJ",
"inputs": [
{
"input_id": "5GNJ",
"molecules": [
{
"type": "protein",
"id": "A",
"sequence": "MGREEPLNHVEAERQRREKLNQRFYALRAVVPNVSKMDKASLLGDAIAYINELKSKVVKTESEKLQIKNQLEEVKLELAGRLEHHHHHH",
"msa": {
"main_db": {
"csv": {
"alignment": msa_alignment_csv,
"format": "csv",
}
},
},
},
{
"type": "dna",
"id": "B",
"sequence": "AGGAACACGTGACCC",
},
{
"type": "dna",
"id": "C",
"sequence": "TGGGTCACGTGTTCC",
},
],
"output_format": "pdb",
}
],
}
print(data)

# ---------------------------------------------------------
# Submit
# ---------------------------------------------------------
headers = {
"content-type": "application/json",
"Authorization": "Bearer $NVIDIA_API_KEY",
"NVCF-POLL-SECONDS": "300",
}
print("Making request...")
response = requests.post(url, headers=headers, json=data)

# ---------------------------------------------------------
# View response
# ---------------------------------------------------------
if response.status_code == 200:
output_file.write_text(response.text)
print(f"Response output to file: {output_file}")

else:
print(f"Unexpected HTTP status: {response.status_code}")
print(f"Response: {response.text}")
```