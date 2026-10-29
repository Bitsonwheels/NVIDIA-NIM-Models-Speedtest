---
title: "diffdock"
publisher: "mit"
type: "endpoint"
updated: "2025-07-15T04:14:52.882Z"
description: "Predicts the 3D structure of how a molecule interacts with a protein."
canonical: "https://build.nvidia.com/mit/diffdock"
---

# Model Overview

## Description:

DiffDock is a generative diffusion model for drug discovery in molecular blind docking.

DiffDock consists of two models: the Score and Confidence models. The Score model generates a series of potential poses for protein-ligand binding by running a reverse diffusion process.

DiffDock does not require any information about a binding pocket. During its diffusion process, the molecule's position relative to the protein, its orientation, and the torsion angles are allowed to change. Running the learned reverse diffusion process transforms a distribution of noisy prior molecule poses to the one learned by the model. As a result, it outputs many sampled poses and ranks them via its confidence model.

Leveraging the same neural-network architecture designed in the original DiffDock by MIT, the model v2.2.0 is trained by NVIDIA using PLINDER and SAIR, a state-of-art dataset of well curated and labeled protein-ligand complexes, which therefore, delivers a much higher accuracy for molecular docking tasks.

This model is ready for commercial and non-commercial use.<br>

## License/Terms of Use:
Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: [MIT](https://github.com/gcorso/DiffDock/blob/main/LICENSE).

## Deployment Geography:
Global

## Use Case:
DiffDock is designed for computational chemists, bioinformaticians, and pharmaceutical researchers. Its primary use case is predicting the binding poses of small molecules (ligands) to target proteins, facilitating drug discovery by identifying and optimizing potential therapeutic compounds.

## Release Date:
GitHub 10/03/2022 via [github.com/gcorso/DiffDock](https://github.com/gcorso/DiffDock)<br>
Hugging Face 12/01/2022 via [huggingface.co/spaces/simonduerr/diffdock](https://huggingface.co/spaces/simonduerr/diffdock)<br>
build.nvidia.com 7/6/2026 via [build.nvidia.com/mit/diffdock](https://build.nvidia.com/mit/diffdock)<br>
NGC 7/6/2026 via [catalog.ngc.nvidia.com](https://catalog.ngc.nvidia.com/orgs/nim/teams/mit/models/diffdock)<br>

## References:
```
@article {Durairaj2024.07.17.603955,
author = {Durairaj, Janani and Adeshina, Yusuf and Cao, Zhonglin and Zhang, Xuejin and Oleinikovas, Vladas and Duignan, Thomas and McClure, Zachary and Robin, Xavier and Studer, Gabriel and Kovtun, Daniel and Rossi, Emanuele and Zhou, Guoqing and Veccham, Srimukh and Isert, Clemens and Peng, Yuxing and Sundareson, Prabindh and Akdel, Mehmet and Corso, Gabriele and St{\"a}rk, Hannes and Tauriello, Gerardo and Carpenter, Zachary and Bronstein, Michael and Kucukbenli, Emine and Schwede, Torsten and Naef, Luca},
title = {PLINDER: The protein-ligand interactions dataset and evaluation resource},
elocation-id = {2024.07.17.603955},
year = {2024},
doi = {10.1101/2024.07.17.603955},
publisher = {Cold Spring Harbor Laboratory},
abstract = {Protein-ligand interactions (PLI) are foundational to small molecule drug design. With computational methods striving towards experimental accuracy, there is a critical demand for a well-curated and diverse PLI dataset. Existing datasets are often limited in size and diversity, and commonly used evaluation sets suffer from training information leakage, hindering the realistic assessment of method generalization capabilities. To address these shortcomings, we present PLIN-DER, the largest and most annotated dataset to date, comprising 449,383 PLI systems, each with over 500 annotations, similarity metrics at protein, pocket, interaction and ligand levels, and paired unbound (apo) and predicted structures. We propose an approach to generate training and evaluation splits that minimizes task-specific leakage and maximizes test set quality, and compare the resulting performance of DiffDock when retrained with different kinds of splits.Competing Interest StatementThe authors have declared no competing interest.},
URL = {https://www.biorxiv.org/content/early/2024/07/19/2024.07.17.603955.1},
eprint = {https://www.biorxiv.org/content/early/2024/07/19/2024.07.17.603955.1.full.pdf},
journal = {bioRxiv}
}
```
```
@article{corso2023diffdock,
title={DiffDock: Diffusion Steps, Twists, and Turns for Molecular Docking}, 
author = {Corso, Gabriele and Stärk, Hannes and Jing, Bowen and Barzilay, Regina and Jaakkola, Tommi},
journal={International Conference on Learning Representations (ICLR)},
year={2023}
}
```

## Model Architecture:
**Architecture Type:** Score-Based Diffusion Model (SBDM)  <br>
**Network Architecture:** Graph Convolution Neural Network <br>

The Score model is a 3-dimensional equivariant graph neural network that has three layers: embedding, interaction layer with 6 graph convolution layers, and output layer. In total, the Score model has 20M parameters. 

## Computational Load (Internal Only: For NVIDIA Models Only; please add as an HTML comment and remove the fields below from the published model card) 
**Cumulative Compute:** [Follow Instructions](https://nvidia.sharepoint.com/:w:/s/TrustworthyAI/EbsO-zwZrZlLiavYNk3zVRABuonEHXLJjpzl0jWx5u6S1A?e=5Rxgqw) <br>
**Estimated Energy and Emissions for Model Training:**   [Follow Instructions](https://nvidia.sharepoint.com/:w:/s/TrustworthyAI/Ecb23D6b-kNLv1c6LCdhSiMBjWFz0MKncBaRcryDsfv-vA?e=lIcO9z) <br>

## Input: 
**Input Type(s):** Text (Ligand, Protein), Number (Poses to Generate, Batch Size, Diffusion Steps, Diffusion Time Divisions) Binary (No Final Step Noise, Save Diffusion Trajectory, and Skip Gen Conformer)<br>
**Input Format(s):** Text: String (SMILES, Structural Data Files (SDF) or Tripos molecule structure (Mol2) for Ligand), String (Protein Data Bank (PDB)), Number: Integer; Binary: Boolean<br>
**Input Parameters:** Text: One-Dimensional (1D), Number: One-Dimensional (1D), Binary: One-Dimensional (1D)<br>
**Other Properties Related to Input:** No max sequence<br>

## Output: 
**Output Type(s):** Text (Ligand Molecule 3D Positions, 3D), Text (Ligand Molecule 3D Positions, 3D), Number (List of Confidence Scores, 1D)<br>
**Output Format:** Text: Structural Data Files (SDF), Text: Protein Data Bank (PDB), Number: Array of Floating Point 32<br>
**Output Parameters:** docked_ligand, visualizations_files, pose_confidence<br>
**Other Properties Related to Output:** Output includes ranked binding poses with associated confidence scores. Higher confidence scores indicate more reliable predictions.<br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:

**Runtime Engine(s):**
* PyTorch <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Lovelace <br>
* NVIDIA Hopper <br>
* NVIDIA Grace Hopper <br>

**[Preferred/Supported] Operating System(s):** <br>
* Linux <br>

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Model Version(s):
DiffDock v2.3 <br>

# Training & Evaluation Dataset:

## Data Modality:
Other: 3D Molecular Structures (protein-ligand complexes)

## Training Data Size:
486,000 protein-ligand complexes (450,000 from PLINDER + 36,000 selected from SAIR)

## Training:
**Link:** [PLINDER](https://plinder-org.github.io/plinder/index.html) <br><br>
**Link:** [SAIR](https://www.sandboxaq.com/sair) <br><br>
**Data Collection Method by dataset:** <br>
* Human <br>

**Labeling Method by dataset:** <br>
* Hybrid: Human & Automated <br>

**Properties:** 486,000 protein-ligand complexes (450,000 from PLINDER automatically curated using the PDB database + 36,000 selected from SAIR). For more information, see [Technical Paper](https://www.biorxiv.org/content/10.1101/2024.07.17.603955v3).<br>

## Evaluation:

**Link:**  [PoseBusters benchmark (PDB) set](https://zenodo.org/records/8278563) <br><br>
**Data Collection Method by dataset:** <br>
* Human <br>

**Labeling Method by dataset:** <br>
* Hybrid: Human & Automated <br>

**Properties:** 486,000 protein-ligand complexes (450,000 from PLINDER automatically curated using the PDB database + 36,000 selected from SAIR). For more information, see [Technical Paper](https://www.biorxiv.org/content/10.1101/2024.07.17.603955v3).<br>

## Inference:
**Engine:** PyTorch <br>
**Test Hardware:** <br>
* A10G, A100, RTX6000-Ada, H100, L40, L40S<br>

# Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
Users are responsible for ensuring the physical properties of model-generated molecules are appropriately evaluated and comply with applicable safety regulations and ethical standards.

**For more detailed information on ethical considerations for this model**, please see the [Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards](https://build.nvidia.com/mit/diffdock/modelcard).

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

# Get Help
## Enterprise Support 
Get access to knowledge base articles and support cases or [submit a ticket](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Capabilities

- **Function Calling:** Not supported

## Bias

|Field|Response|
|:---|:---|
|Participation considerations from adversely impacted groups ([protected classes](https://www.senate.ca.gov/content/protected-classes)) in model design and testing:|None|
|Measures taken to mitigate against unwanted bias|None|

## Explainability

|Field|Response|
|:---|:---|
|Intended Task/Domain|Molecular Docking|
|Model Type|Generate docking poses of small molecules against protein receptors.|
|Intended Users|People in drug-design & drug-discovery related researches and industries.|
|Output|This model returns (1) molecular Structural Data Files (SDF) containing the 3D structures of docking poses in plain-text, (2) confidence scores as real numbers and (3) optional Protein Data Bank (PDB) files containing 3D structures of visualization of docking.|
|Describe how the model works|Model generates docked poses from protein structure and molecule information.|
|Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of|Not Applicable|
|Technical Limitations & Mitigation|The poses the model predicts may not be accurate; model cannot do docking for multi-molecule binding pocket or flexible side-chain docking.|
|Verified to have met prescribed NVIDIA quality standards|Yes|
|Performance Metrics|Percentages that the best (smallest) root mean square deviation (RMSD) is smaller than 2Å between the top-N generated poses and ground truth poses from the benchmark dataset.|
|Potential Known Risks|The model may provide inaccurate predictions of molecules for drug design candidates.|
|Licensing|Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: [MIT](https://github.com/gcorso/DiffDock/blob/main/LICENSE).|

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
|Applicable Privacy Policy|https://www.nvidia.com/en-us/about-nvidia/privacy-policy/|

## Safety & Security

|Field|Response|
|:---|:---|
|Model Application Field(s):|Molecular Docking|
|Describe life critical application (if present)|Experimental drug discovery and medicine use cases per [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/).|
|Use Case Restrictions|Abide by [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: [MIT](https://github.com/gcorso/DiffDock/blob/main/LICENSE).|
|Model and dataset restrictions|The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to.|

## Prototype

```bash
#!/bin/bash
#
# Before running this script, you need to:
#   1. Set the NVIDIA_API_KEY environment variable.
#

# Variables
KEY="$NVIDIA_API_KEY"
URL="https://health.api.nvidia.com/v1/biology/mit/diffdock"

# Download protein PDB
echo "Downloading protein PDB..."
PROTEIN=$(curl -s "https://files.rcsb.org/download/8G43.pdb" | grep "^ATOM")

# Download ligand SDF
echo "Downloading ligand SDF..."
LIGAND=$(curl -s "https://files.rcsb.org/ligands/download/ZU6_ideal.sdf")

# Prepare the JSON data using jq for proper escaping
DATA=$(jq -n \
--arg protein "$PROTEIN" \
--arg ligand "$LIGAND" \
'{
"ligand": $ligand,
"ligand_file_type": "sdf",
"protein": $protein,
"num_poses": 10,
"time_divisions": 20,
"steps": 18,
"save_trajectory": false
}')

echo "Making request to DiffDock..."
curl -s -X POST "${URL}" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${KEY}" \
-d "${DATA}" > output.json

cat output.json
```

```python
#!/usr/bin/env python3
# Before running this script, you need to:
#   1. Set the NVIDIA_API_KEY environment variable.

import requests

url = "https://health.api.nvidia.com/v1/biology/mit/diffdock"
header_auth = "Bearer $NVIDIA_API_KEY"

print("Downloading protein from RCSB...")
protein_response = requests.get("https://files.rcsb.org/download/8G43.pdb", timeout=30)
protein_response.raise_for_status()
protein_content = "\n".join(line for line in protein_response.text.split("\n") if line.startswith("ATOM"))

print("Downloading ligand from RCSB...")
ligand_response = requests.get("https://files.rcsb.org/ligands/download/ZU6_ideal.sdf", timeout=30)
ligand_response.raise_for_status()
ligand_content = ligand_response.text

headers = {
"Content-Type": "application/json",
"Authorization": header_auth
}

print("Making request to DiffDock...")
r = requests.post(url, headers=headers, json={
"ligand": ligand_content,
"ligand_file_type": "sdf",
"protein": protein_content,
"num_poses": 10,
"time_divisions": 20,
"steps": 18,
"save_trajectory": False,
})

with open("output.json", "w") as f:
f.write(r.text)

print(r.text)
```