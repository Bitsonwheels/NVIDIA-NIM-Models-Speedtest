---
title: "rfdiffusion"
publisher: "ipd"
type: "endpoint"
updated: "2025-05-28T21:48:43.610Z"
description: "A generative model of protein backbones for protein binder design."
canonical: "https://build.nvidia.com/ipd/rfdiffusion"
---

# Model Overview

## Description:
RFdiffusion (RoseTTAFold Diffusion) is a generative model that creates novel protein structures for protein scaffolding and protein binder design tasks. This model generates entirely new protein backbones and designs proteins that can be specifically tailored to bind to target molecules.<br>

This model is available for commercial use.<br>

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed
and built to a third-party’s requirements for this application and use case; see link to Non-NVIDIA [GitHub Model Card](https://github.com/RosettaCommons/RFdiffusion). <br>

### License/Terms of Use:
GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Service Terms of Use](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Community Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). Additional Information: [BSD License](https://github.com/RosettaCommons/RFdiffusion/blob/820bfdfaded8c260b962dc40a3171eae316b6ce0/LICENSE).

**You are responsible for ensuring that your use of NVIDIA AI Foundation Models
complies with all applicable laws.**

### Release Date
build.nvidia.com: March 30, 2026 via [build.nvidia.com/ipd/rfdiffusion](https://build.nvidia.com/ipd/rfdiffusion) <br>
NGC: March 30, 2026 via [catalog.ngc.nvidia.com](https://catalog.ngc.nvidia.com/orgs/nim/teams/ipd/models/rfdiffusion) <br>

## References:
```
@ARTICLE{nat2023rfdiffusion,
title    = "De novo design of protein structure and function with RFdiffusion",
author   = "Watson, Joseph L. and Juergens, David and Bennett, Nathaniel R.
and Trippe, Brian L. and Yim, Jason and Eisenach, Helen E. and Ahern, Woody
and Borst, Andrew J. and Ragotte, Robert J. and Milles, Lukas F. and Wicky,
Basile I. M. and Hanikel, Nikita and Pellock, Samuel J. and Courbet, Alexis
and Sheffler, William and Wang, Jue and Venkatesh, Preetham and Sappington,
Isaac and Torres, Susana Vázquez and Lauko, Anna and De Bortoli, Valentin
and Mathieu, Emile and Ovchinnikov, Sergey and Barzilay, Regina and
Jaakkola, Tommi S. and DiMaio, Frank and Baek, Minkyung and Baker, David",
journal  = "Nature",
volume   =  620,
number   =  7976,
pages    = "1089--1100",
month    =  aug,
year     =  2023,
language = "en",
doi = {10.1038/s41586-023-06415-8}
}
```

## Model Architecture:
**Architecture Type:** Diffusion-based Generative Neural Network <br>
**Network Architecture:** RFdiffusion <br>

## Input:
**Input Type(s):** Text (Protein) <br>
**Input Format(s):** Protein Data Bank (PDB)  <br>
**Input Parameters:** String, One-Dimensional (1D) <br>

## Output:
**Output Type(s):** Text (Protein)  <br>
**Output Format:** Protein Data Bank (PDB)<br>
**Output Parameters:** String, 1D <br>

## Software Integration:
**Runtime Engine(s):**
* PyTorch <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Blackwell <br>
* NVIDIA Hopper<br>
* NVIDIA Lovelace <br>
* NVIDIA Turing <br>

**[Preferred/Supported] Operating System(s):** <br>
* Linux <br>

## Model Version(s):
RFdiffusion 2.0.0 <br>

# Training & Evaluation:

## Training Dataset:

**Link:**
[The Protein Data Bank](https://www.rcsb.org/) <br>

** Data Collection Method by dataset <br>
* Hybrid: Automatic, Human <br>

For PDB dataset, scientists worldwide submit structural data
determined by X-ray crystallography or cryo-electron microscopy (cryo-EM).
This includes atomic coordinates, experimental data, and metadata about the
biological macromolecules. <br>

** Labeling Method by dataset <br>
* Hybrid: Automatic, Human <br>

For PDB dataset, expert biocurators review the submitted data to
ensure accuracy and completeness. This involves checking the plausibility of
the data and annotating it with relevant biological and chemical information.<br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**
The training dataset
used for RFdiffusion, as detailed in referenced paper, consists of protein structures sampled
from the Protein Data Bank (PDB). To prepare these structures for training, a
noising process is applied. This process involves simulating up to 200 steps of
random modifications on the protein structures. Specifically, the modifications
include perturbing the Cα coordinates with 3D Gaussian noise and applying
Brownian motion to the residue orientations on the manifold of rotation
matrices.<br>

**Dataset License(s):** [CC0 1.0](https://www.rcsb.org/news/feature/611e8d97ef055f03d1f222c6). <br>

## Evaluation Dataset:

The evaluation strategy involved training the model on PDB structures (as
described in Training Dataset) with added noise and then assessing its ability
to denoise these structures, as well as evaluating its performance on design
tasks with auxiliary conditioning information.<br>

** Data Collection Method by dataset <br>
* Automatic: random splits from PDB dataset. <br>

** Labeling Method by dataset <br>
* Automatic: random splits from PDB dataset. <br>

The training, validation, and test splits were derived from protein assemblies
in the PDB, which includes structures determined by X-ray
crystallography or cryo-electron microscopy (cryoEM).<br>

## Inference:
**Engine:** PyTorch <br>
**Test Hardware:** <br>
* NVIDIA A100 <br>
* NVIDIA GB200 <br>
* NVIDIA H100 <br>
* NVIDIA L40 <br>

### Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

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

URL=${URL:-https://health.api.nvidia.com/v1/biology/ipd/rfdiffusion/generate}

if [ ! -e 1R42.pdb ]; then curl -O https://files.rcsb.org/download/1R42.pdb; fi

pdb=$(cat 1R42.pdb | grep ^ATOM | head -n 400 | awk '{printf "%s\\n", $0}')

request='{
"input_pdb": "'"$pdb"'",
"contigs": "A20-60/0 50-100",
"hotspot_res": ["A50","A51","A52","A53","A54"],
"diffusion_steps": 15
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
return "\n".join(list(lines)[:400])

r = requests.post(
url=os.getenv("URL", "https://health.api.nvidia.com/v1/biology/ipd/rfdiffusion/generate"),
headers={"Authorization": "Bearer $NVIDIA_API_KEY"},
json={
"input_pdb": get_reduced_pdb(),
"contigs": "A20-60/0 50-100",
"hotspot_res": ["A50","A51","A52","A53","A54"],
"diffusion_steps": 15,
},
)
print(r, "Saving to output.pdb:\n", r.text[:200], "...")
Path("output.pdb").write_text(json.loads(r.text)["output_pdb"])
```