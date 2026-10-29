---
title: "Boltz-2"
publisher: "mit"
type: "endpoint"
updated: "2025-07-09T01:28:35.670Z"
description: "Predict complex structures using Boltz-2."
canonical: "https://build.nvidia.com/mit/boltz2"
---

## Model Overview

### Description:

Boltz-2 NIM is a next-generation structural biology foundation model that shows strong performance for both structure and affinity prediction. Boltz-2 is the first deep learning model to approach the accuracy of free energy perturbation (FEP) methods in predicting binding affinities of small molecules and proteins—achieving strong correlations on benchmarks while being nearly 1000x more computationally efficient.

### Key Features:
**Trunk optimizations:** Mixed-precision (bfloat16) and trifast triangle attention cut runtime/memory; enables training with 768-token crops (as in AlphaFold3). <br>
**Physical quality:** Integrates Boltz-steering at inference (Boltz-2x) to reduce steric clashes and stereochemistry errors without losing accuracy. <br>
**Controllability:** <br>
* **Method conditioning:** Steers predictions to resemble X-ray, NMR, or MD-style structures. <br>
* **Template conditioning + steering:** Uses single or multimeric templates; supports strict template enforcement or soft guidance. <br>
* **Contact/pocket conditioning:** Accepts distance constraints from experiments or expert priors. <br>

**Affinity module:** PairFormer refines protein–ligand and intra-ligand interactions; predicts both binding likelihood and a continuous affinity on log µM scale (trained on mixed Ki, Kd, IC50). Output is an IC50-like measure suitable for ranking. <br>
**Key advances vs Boltz-1/1x:** Faster/more memory-efficient trunk, improved physical plausibility via integrated steering, markedly enhanced controllability, and added affinity prediction head. <br>

This model is ready for commercial or non-commercial use.
<br>

### Third-Party Community Consideration

This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to Non-NVIDIA MIT [Model Card](https://github.com/jwohlwend/boltz).

#### License / Terms of Use

GOVERNING HOSTING TERMS: Use of this trial service is governed by the [NVIDIA API Trial Service Terms of Use](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-agreement/). 
**ADDITIONAL INFORMATION:** [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) and [MIT License](https://github.com/jwohlwend/boltz/blob/main/LICENSE).

**You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.**

### Deployment Geography
Global

### Use Case
Boltz-2 NIM enables researchers and commercial entities in the Drug Discovery, Life Sciences, and Digital Biology fields to predict the three-dimensional structure of biomolecular complexes and predict small-molecule binding affinities. Trained on millions of curated experimental datapoints with a novel training strategy tailored for noisy biochemical assay data, Boltz-2 demonstrates robust performance across hit-discovery, hit-to-lead, and lead optimization.

### Release Date
build.nvidia.com: 9/8/2026 via [build.nvidia.com/mit/boltz2](https://build.nvidia.com/mit/boltz2) <br>
NGC: 9/8/2026 via [catalog.ngc.nvidia.com](https://catalog.ngc.nvidia.com/orgs/nim/teams/mit/containers/boltz2) <br>

### References:

```
@article{passaro2025boltz2,
author = {Passaro, Saro and Corso, Gabriele and Wohlwend, Jeremy and Reveiz, Mateo and Thaler, Stephan and Somnath, Vignesh Ram and Getz, Noah and Portnoi, Tally and Roy, Julien and Stark, Hannes and Kwabi-Addo, David and Beaini, Dominique and Jaakkola, Tommi and Barzilay, Regina},
title = {Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction},
year = {2025},
doi = {10.1101/2025.06.14.659707},
journal = {bioRxiv},
language = "en"
}
```

<br>

### Model Architecture:

**Architecture Type:** Four components — trunk, denoising module (with steering), confidence module, and a new affinity module <br>
**Network Architecture:** PairFormer <br>
**Number of Model Parameters:** 1 billion <br>

### Input:

**Input Type(s):** Biomolecular sequences (protein, DNA, RNA), ligand SMILES or CCD strings, molecular modifications, structural constraints, conditioning parameters, optional booleans <br>
**Input Format(s):** Dictionary containing sequence strings, modification records, and constraint parameters <br>
**Input Parameters:** Sequences (strings), predict_affinity(boolean), modifications (list of residue-specific changes), constraints (dictionary of structural parameters) <br>
**Other Properties Related to Input:** Maximum sequence length of 4096 residues per chain. Maximum of 12 input polymers. Maximum of 20 input ligands. Passing boolean options such as predict_affinity will increase the runtime of the request. <br>
**Model Parameters:**
Tables 1 and 2 record some of the hyperparameters of Boltz-2's architecture, training and inference procedures that differ from Boltz-1's and were not previously mentioned in the manuscript.  

**Table 1:** Extra model architecture and training hyperparameters that differ from Boltz-1 and were not previously mentioned in the manuscript.

| Parameter | Value |
|-----------|-------|
| Max number of MSA sequences during training | 8192 |
| Template pairwise dim | 64 |
| Num template blocks | 2 |
| Training diffusion multiplicity | 32 |
| bfactor loss weight | 1 × 10⁻³ |

**Table 2:** Diffusion process hyperparameters that differ from Boltz-1, with the exception of sigma_min we opted for AlphaFold3's default hyperparameters, see Abramson et al. (2024) for more details.

| Parameter   | Value   |
|-------------|---------|
| sigma_min   | 0.0001  |
| rho         | 7       |
| gamma_0     | 0.8     |
| gamma_min   | 1.0     |
| noise_scale | 1.003   |
| step_scale  | 1.5     |

### Output:

**Output Type(s):** Structure prediction in mmcif format; scores in numeric arrays; runtime metrics as a dictionary <br>
**Output Format:** mmcif (text file); numeric arrays; scalar numeric values <br>
**Output Parameters:** 3D atomic coordinates, predicted scores, and metadata <br>
**Other Properties Related to Output:** All Boltz-2 scores are returned by default. Runtime metrics are optional. <br>
Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. <br>

### Software Integration:

**Runtime Engine(s):**
* PyTorch, TensorRT <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere, NVIDIA Blackwell, NVIDIA Hopper, NVIDIA Lovelace <br>

**Supported Operating System(s)** <br>
* [Linux] <br>
* The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

### Model Version(s):

Boltz2 v2.2.1 <br>

## Training and Evaluation Datasets:

### Training Dataset:
** Data Modality <br>
* [Text]

** Training Data Size: <br>
Manually-Collected <br>

**Link:** [Protein Data Bank as used by AlphaFold3](https://github.com/jwohlwend/boltz/blob/main/docs/training.md)  <br>

** Data Collection Method by dataset <br>
* Manually-Collected <br>

** Labeling Method by dataset <br>
* Manually-Labeled <br>

**Properties:**
All Protein Data Bank structures before 2021-09-30 with a resolution of at least 9 Angstroms, preprocessed to match each structure to its sequence. Ligands were processed similarly. All data was cleaned as described in AlphaFold3.

### Evaluation Dataset:

**Link:** [Boltz Evaluation Performed on 744 Structures from the Protein Data Bank](https://github.com/jwohlwend/boltz/blob/main/docs/evaluation.md)  <br>
** Data Collection Method by dataset <br>
* Manually-Labeled <br>

** Labeling Method by dataset <br>
* Hybrid: Human and Automated <br>

**Properties:**
The test and validation datasets were generated by extensive filtering of PDB sequences deposited between 2021-09-31 and 2023-01-13. In total, 593 structures passed filters and were used for validation.
<br>

### Inference:

**Acceleration Engine:** PyTorch, TensorRT <br>
**Test Hardware:** <br>
* NVIDIA Ampere A100 <br>
* NVIDIA Blackwell B200 <br>
* NVIDIA Blackwell B300 <br>
* NVIDIA Grace Blackwell GB10 Superchip (DGX Spark) <br>
* NVIDIA Grace Blackwell GB200 Superchip <br>
* NVIDIA Grace Blackwell GB300 Superchip <br>
* NVIDIA Grace Hopper GH200 Superchip <br>
* NVIDIA Hopper H100 <br>
* NVIDIA Hopper H200 <br>
* NVIDIA Lovelace L40 <br>
* NVIDIA Blackwell RTX PRO 6000 Workstation Edition <br>
* NVIDIA Lovelace RTX 6000 / NVIDIA RTX 6000 Ada Generation <br>

### Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br> 

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).  <br>

**You are responsible for ensuring the physical properties of model-generated molecules are appropriately evaluated, and comply with applicable safety regulations and ethical standards.**

# Get Help
## Enterprise Support
Get access to knowledge base articles and support cases or [submit a ticket](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Specifications

- **Parameters:** 520,636,223

## Capabilities

- **Function Calling:** Not supported

## Prototype

```bash
#!/bin/bash

# Uncomment the following line for debugging purposes
# set -x

# Exit immediately if a command exits with a non-zero status.
set -e

# Constants
PUBLIC_URL="https://health.api.nvidia.com/v1/biology/mit/boltz2/predict"

# Configuration
NVCF_POLL_SECONDS=300  # Set poll seconds to 300 by default
MANUAL_TIMEOUT_SECONDS=400  # Used to set max time for curl requests
POLL_INTERVAL=10  # Poll every 10 seconds

echo "[INFO] Starting Boltz2 prediction request..."

# Define the sequence
sequence="MKTVRQERLKSIVRILERSKEPVSGAQLAEELSVSRQVIVQDIAYLRSLGYNIVATPRGYVLAGG"
echo "[INFO] Using protein sequence: ${sequence:0:20}...${sequence: -10}"

# Define the data payload as JSON using a subshell to prevent read issues
data=$(cat <<EOF
{
"polymers": [
{
"id": "A",
"molecule_type": "protein", 
"sequence": "$sequence",
"msa": {
"uniref90": {
"a3m": {
"alignment": ">seq1\n$sequence",
"format": "a3m"
}
}
}
}
],
"ligands": [
{
"smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
"id": "L1",
"predict_affinity": true
}
],
"recycling_steps": 1,
"sampling_steps": 50,
"diffusion_samples": 3,
"step_scale": 1.2,
"without_potentials": true
}
EOF
)

# Use temporary files for response headers and body
response_headers=$(mktemp)
response_body=$(mktemp)

# Ensure temporary files are deleted on exit
cleanup() {
rm -f "$response_headers" "$response_body"
}
trap cleanup EXIT

echo "[INFO] Sending request to $PUBLIC_URL"

# Perform the POST request with curl
curl -s -D "$response_headers" -o "$response_body" -X POST "$PUBLIC_URL" \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-H "NVCF-POLL-SECONDS: $NVCF_POLL_SECONDS" \
-H "Content-Type: application/json" \
--max-time "$MANUAL_TIMEOUT_SECONDS" \
-d "$data"

# Extract status code from headers
status_code=$(grep -i "^HTTP/" "$response_headers" | tail -n1 | awk '{print $2}')
echo "[INFO] Received HTTP status code: $status_code"

if [ "$status_code" -eq 200 ]; then
echo "[SUCCESS] Request succeeded - processing response"

# Save to output.json and display
jq '.' "$response_body" > output.json
echo "[SUCCESS] Response saved to output.json"

# Display response to screen
echo ""
echo "Response content:"
echo "=================="
jq '.' "$response_body"
echo "=================="
echo ""

# Extract and print information about structures and confidence scores
num_structures=$(jq '.structures | length' output.json 2>/dev/null || echo "0")
num_scores=$(jq '.confidence_scores | length' output.json 2>/dev/null || echo "0")

echo "Analysis Results:"
echo "  • Number of structures returned: $num_structures"
echo "  • Number of confidence scores: $num_scores"

# Print details about the first structure if available
if [ "$num_structures" -gt 0 ]; then
first_format=$(jq -r '.structures[0].format' output.json 2>/dev/null || echo "unknown")
first_length=$(jq -r '.structures[0].structure | length' output.json 2>/dev/null || echo "unknown")
echo "  • First structure format: $first_format"
echo "  • First structure length: $first_length characters"
fi

# Print confidence scores
if [ "$num_scores" -gt 0 ]; then
confidence_scores=$(jq -r '.confidence_scores | join(", ")' output.json 2>/dev/null || echo "none")
echo "  • Confidence scores: $confidence_scores"
fi

elif [ "$status_code" -eq 202 ]; then
echo "[INFO] Request accepted - task queued for processing"

# Extract Task ID from headers
task_id=$(grep -i "nvcf-reqid:" "$response_headers" | awk '{print $2}' | tr -d '\r\n')
if [ -z "$task_id" ]; then
echo "[ERROR] No Task ID found in response headers - cannot poll for status" >&2
exit 1
fi

echo "[SUCCESS] Task ID: $task_id"
echo "[INFO] Task has been queued for processing"

# Save initial response and display
jq '.' "$response_body" > output.json
echo "[SUCCESS] Response saved to output.json"

# Display response to screen
echo ""
echo "Response content:"
echo "=================="
jq '.' "$response_body"
echo "=================="
echo ""

else
echo "[ERROR] Request failed with status code: $status_code" >&2
echo ""
echo "Response body:"
if jq '.' "$response_body" 2>/dev/null; then
jq '.' "$response_body"
else
cat "$response_body"
fi
exit 1
fi

echo "[SUCCESS] Script completed successfully"
```

```python
#!/usr/bin/env python3
import asyncio
import json
from typing import Any, Dict, Optional
import os
from pathlib import Path
from enum import StrEnum
import logging
import sys

# Check for required dependencies
missing_deps = []
try:
import httpx
except ImportError:
missing_deps.append("httpx")
try:
from fastapi import HTTPException
except ImportError:
missing_deps.append("fastapi")

if missing_deps:
print("Error: Missing required dependencies. Please install them using:")
print(f"pip install {' '.join(missing_deps)}")
sys.exit(1)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

STATUS_URL = "https://api.nvcf.nvidia.com/v2/nvcf/pexec/status/{task_id}"

PUBLIC_URL = "https://health.api.nvidia.com/v1/biology/mit/boltz2/predict"

async def make_nvcf_call(function_url: str,
data: Dict[str, Any],
additional_headers: Optional[Dict[str, Any]] = None,
NVCF_POLL_SECONDS: int = 300,
MANUAL_TIMEOUT_SECONDS: int = 400) -> Dict:
"""
Make a call to NVIDIA Cloud Functions using long-polling,
which allows the request to patiently wait if there are many requests in the queue.
"""
async with httpx.AsyncClient() as client:
headers = {
"Authorization": "Bearer $NVIDIA_API_KEY",
"NVCF-POLL-SECONDS": f"{NVCF_POLL_SECONDS}",
"Content-Type": "application/json"
}
if additional_headers is not None:
headers.update(additional_headers)
logger.debug(f"Headers: {dict(**{h: v for h, v  in headers.items() if 'Authorization' not in h})}")
# TIMEOUT must be greater than NVCF-POLL-SECONDS
logger.debug(f"Making NVCF call to {function_url}")
logger.debug(f"Data: {data}")
response = await client.post(function_url,
json=data,
headers=headers,
timeout=MANUAL_TIMEOUT_SECONDS)
logger.debug(f"NVCF response: {response.status_code, response.headers}")

if response.status_code == 202:
# Handle 202 Accepted response
task_id = response.headers.get("nvcf-reqid")
while True:
## Should return in 5 seconds, but we set a manual timeout in 10 just in case
status_response = await client.get(STATUS_URL.format(task_id=task_id),
headers=headers,
timeout=MANUAL_TIMEOUT_SECONDS)
if status_response.status_code == 200:
return status_response.status_code, status_response
elif status_response.status_code in [400, 401, 404, 422, 500]:
raise HTTPException(status_response.status_code,
"Error while waiting for function: ",
response.text)
elif response.status_code == 200:
return response.status_code, response
else:
raise HTTPException(status_code=response.status_code, detail=response.text)

async def main():
# Example protein sequence
sequence = "MKTVRQERLKSIVRILERSKEPVSGAQLAEELSVSRQVIVQDIAYLRSLGYNIVATPRGYVLAGG"
output_file = Path("output.json")

# Prepare the request payload
data = {
"polymers": [
{
"id": "A",
"molecule_type": "protein", 
"sequence": sequence,
"msa": {
"uniref90": {
"a3m": {
"alignment": f">seq1\n{sequence}",
"format": "a3m"
}
}
}
}
],
"ligands": [
{
"smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
"id": "L1",
"predict_affinity" : True
}
],
"recycling_steps": 1,
"sampling_steps": 50,
"diffusion_samples": 3,
"step_scale": 1.2,
"without_potentials": True
}

print("Making request...")
code, response = await make_nvcf_call(function_url=PUBLIC_URL,
data=data)

if code == 200:
print(f"Request succeeded, returned {code}")
response_dict = response.json()
output_file.write_text(json.dumps(response_dict, indent=4))

# Print information about the returned structures
print(f"Number of structures returned: {len(response_dict['structures'])}")
print(f"Number of confidence scores: {len(response_dict['confidence_scores'])}")

# Print the first structure's format and length
if response_dict['structures']:
first_structure = response_dict['structures'][0]
print(f"First structure format: {first_structure['format']}")
print(f"First structure length: {len(first_structure['structure'])} characters")

# Print confidence scores
print(f"Confidence scores: {response_dict['confidence_scores']}")

if __name__ == "__main__":
asyncio.run(main())
```