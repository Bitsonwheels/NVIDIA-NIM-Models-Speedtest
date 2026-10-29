---
title: "openfold2"
publisher: "openfold"
type: "endpoint"
updated: "2025-05-29T20:33:10.517Z"
description: "Predicts the 3D structure of a protein from its amino acid sequence, multiple sequence alignments, and templates."
canonical: "https://build.nvidia.com/openfold/openfold2"
---

# Model Overview

## Description:
OpenFold2 is a protein structure prediction model from the [OpenFold Consortium](https://openfold.io/) and the [Alquraishi Laboratory](https://www.aqlab.io/).  OpenFold2 is a pytorch re-implementation of Google Deepmind's [AlphaFold2](https://github.com/google-deepmind/alphafold), with support for both training and inference.  OpenFold2 demonstrates accuracy parity with AlphaFold2, and improved speed. For more information, please see the OpenFold repository [https://github.com/aqlaboratory/openfold](https://github.com/aqlaboratory/openfold).<br>

This model is ready for commercial or non-commercial use.<br>

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to Non-NVIDIA [OpenFold Consortium (AlQuraishi Laboratory, Columbia University) OpenFold Model Card](https://github.com/aqlaboratory/openfold).

### License/Terms of Use:

GOVERNING HOSTING TERMS: Use of this trial service is governed by the [NVIDIA API Trial Service Terms of Use](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-agreement/). 
**ADDITIONAL INFORMATION:** [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

**You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.**

## Deployment Geography: 
Global

## Use Case
The OpenFold2 NIM can be used at academic and pharmaceutical industry research labs.  The structure prediction functionality supports computer-aided drug design.

## Release Date

- build.nvidia.com: September 1, 2026 at [build.nvidia.com/openfold/openfold2](build.nvidia.com/openfold/openfold2)
- NGC: September 1, 2026 at [https://registry.ngc.nvidia.com](https://registry.ngc.nvidia.com/orgs/nvstaging/teams/nim/models/openfold2)

## References:
```
@article {Ahdritz2022.11.20.517210,
author = {Ahdritz, Gustaf and Bouatta, Nazim and Floristean, Christina and Kadyan, Sachin and Xia, Qinghui and Gerecke, William and O{\textquoteright}Donnell, Timothy J and Berenberg, Daniel and Fisk, Ian and Zanichelli, Niccolò and Zhang, Bo and Nowaczynski, Arkadiusz and Wang, Bei and Stepniewska-Dziubinska, Marta M and Zhang, Shang and Ojewole, Adegoke and Guney, Murat Efe and Biderman, Stella and Watkins, Andrew M and Ra, Stephen and Lorenzo, Pablo Ribalta and Nivon, Lucas and Weitzner, Brian and Ban, Yih-En Andrew and Sorger, Peter K and Mostaque, Emad and Zhang, Zhao and Bonneau, Richard and AlQuraishi, Mohammed},
title = {{O}pen{F}old: {R}etraining {A}lpha{F}old2 yields new insights into its learning mechanisms and capacity for generalization},
elocation-id = {2022.11.20.517210},
year = {2022},
doi = {10.1101/2022.11.20.517210},
publisher = {Cold Spring Harbor Laboratory},
URL = {https://www.biorxiv.org/content/10.1101/2022.11.20.517210},
journal = {bioRxiv}
}
```
```
@ARTICLE{jumper2021alphafold,
title    = "Highly accurate protein structure prediction with {AlphaFold}",
author   = "Jumper, John and Evans, Richard and Pritzel, Alexander and Green,
Tim and Figurnov, Michael and Ronneberger, Olaf and
Tunyasuvunakool, Kathryn and Bates, Russ and {\v Z}{\'\i}dek,
Augustin and Potapenko, Anna and Bridgland, Alex and Meyer,
Clemens and Kohl, Simon A A and Ballard, Andrew J and Cowie,
Andrew and Romera-Paredes, Bernardino and Nikolov, Stanislav and
Jain, Rishub and Adler, Jonas and Back, Trevor and Petersen, Stig
and Reiman, David and Clancy, Ellen and Zielinski, Michal and
Steinegger, Martin and Pacholska, Michalina and Berghammer, Tamas
and Bodenstein, Sebastian and Silver, David and Vinyals, Oriol
and Senior, Andrew W and Kavukcuoglu, Koray and Kohli, Pushmeet
and Hassabis, Demis",
journal  = "Nature",
volume   =  596,
number   =  7873,
pages    = "583--589",
month    =  aug,
year     =  2021,
language = "en",
doi = {10.1038/s41586-021-03819-2},
}
```

## Model Architecture:
**Architecture Type:** Protein Structure Prediction <br>
**Network Architecture:** AlphaFold2 <br>
** Number of model parameters: 9.3×10⁷

## Input:
**Input Type(s):** Protein Sequence, Multiple Sequence Alignments, Templates <br>
**Input Format(s):** String (less than or equal to 1000), a3m-format strings, hhr-format strings <br>
**Input Parameters:** One-Dimensional (1D), One-Dimensional (1D), One-Dimensional (1D)<br>
**Other Properties Related to Input:** a3m is a standard file format for storing multiple sequence alignment results.  hhr is the file format output by the tool hh-search.  For more informaiton see [hh-suite](https://github.com/soedinglab/hh-suite)  <br>

## Output:
**Output Type(s):** Protein Structure(s) in PDB Format <br>
**Output Format:** PDB (text file)<br>
**Output Parameters:** 1D <br>
**Other Properties Related to Output:** Pose (num_atm_ x 3)<br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration:
**Runtime Engine(s):**
* PyTorch <br>
* TensorRT-BioNeMo<br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Hopper<br>
* NVIDIA Ampere <br>
* NVIDIA Lovelace <br>
* NVIDIA Blackwell <br>

**[Preferred/Supported] Operating System(s):** <br>
* Linux <br>

## Model Version(s):
* OpenFold2 v2.6.0<br>

# Training and Evaluation Datasets:

## Training Dataset:

** Data Modality <br>
* [Other: Protein sequences, multiple sequence alignments, and 3D protein structures]

** Training Data Size <br>
* Non-Audio, Image, Text: Uniclust dataset of 355,993 sequences with full MSAs, plus the clustered PDB set.

**Link:** [Highly Accurate ... Data Availability](https://www.nature.com/articles/s41586-021-03819-2#data-availability)

The model parameter sets were trained by Google Deepmind as part of AlphaFold2 development.  A description of the training dataset and relevant download links are available at [Highly Accurate ... Data Availability](https://www.nature.com/articles/s41586-021-03819-2#data-availability). This data was not collected by NVIDIA. <br>

** Data Collection Method by dataset <br>
* Hybrid: Automatic/Sensors, Manually-Collected
* See the description at [Highly Accurate ... Data Availability](https://www.nature.com/articles/s41586-021-03819-2#data-availability). <br>

** Labeling Method by dataset <br>
* Hybrid: Automatic/Sensors, Manually-Labeled
* See the description at [Highly Accurate ... Data Availability](https://www.nature.com/articles/s41586-021-03819-2#data-availability). <br>

**Properties:** Uniclust dataset of 355,993 sequences with the full MSAs. These predictions were then used to train a final model with identical hyperparameters, except for sampling examples 75% of the time from the Uniclust prediction set, with sub-sampled MSAs, and 25% of the time from the clustered PDB set.
<br>

## Evaluation Dataset:

**Link:** See the description at [Highly Accurate... 
Sec10](https://www.nature.com/articles/s41586-021-03819-2#Sec10).  <br>

** Data Collection Method by dataset <br>
* Hybrid: Automatic/Sensors, Manually-Collected
* See the description at [Highly Accurate ... Data Availability](https://www.nature.com/articles/s41586-021-03819-2#data-availability). <br>

** Labeling Method by dataset <br>
* Hybrid: Automatic/Sensors, Manually-Labeled
* See the description at [Highly Accurate ... Data Availability](https://www.nature.com/articles/s41586-021-03819-2#data-availability). <br>

**Properties:** Uniclust dataset of 355,993 sequences with the full MSAs. These predictions were then used to train a final model with identical hyperparameters, except for sampling examples 75% of the time from the Uniclust prediction set, with sub-sampled MSAs, and 25% of the time from the clustered PDB set.
<br>

## Inference:
**Acceleration Engine:** PyTorch <br>
**Test Hardware:** <br>
* NVIDIA A100  <br>
* NVIDIA B200 <br>
* NVIDIA B300 <br>
* NVIDIA GB10 (DGX Spark) <br>
* NVIDIA GB200 <br>
* NVIDIA GB300 <br>
* NVIDIA GH200 <br>
* NVIDIA H100 <br>
* NVIDIA H200 <br>
* NVIDIA L40 <br>
* NVIDIA RTX PRO 6000 Blackwell Workstation Edition <br>
* NVIDIA RTX6000-Ada <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI Concerns
[here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

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
#   - the sequence is 7WBN_A
#

# Variables
URL="https://health.api.nvidia.com/v1/biology/openfold/openfold2/predict-structure-from-msa-and-template"
SEQUENCE="GGSKENEISHHAKEIERLQKEIERHKQSIKKLKQSEQSNPPPNPEGTRQ\
ARRNRRRRWRERQRQKENEISHHAKEIERLQKEIERHKQSIKKLKQSEC"

# Prepare the JSON data
DATA="{\"sequence\": \"$SEQUENCE\"}"
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
#   sequence is correct for 7WBN_A
#
import os
import requests
from pathlib import Path

# ----------------------------
# parameters
# ----------------------------
url = os.getenv("URL", "https://health.api.nvidia.com/v1/biology/openfold/openfold2/predict-structure-from-msa-and-template")
output_file = Path("output1.json")
selected_models = [1, 2]
sequence = (
"GGSKENEISHHAKEIERLQKEIERHKQSIKKLKQSEQSNPPPNPEG"
"TRQARRNRRRRWRERQRQKENEISHHAKEIERLQKEIERHKQSIKKLKQSEC"
)

small_bfd_alignment_in_a3m = \
""">BQXYMDHSRWGGVPIWVK
GGSKENEISHHAKEIERLQKEIERHKQSIKKLKQSEQSNPPPNPEGTRQARRNRRRRWRERQRQKENEISHHAKEIERLQKEIERHKQSIKKLKQSEC
>A0A076V4A1_9HIV1
------------------------------------QSNPPPNHEGTRQARRNRRRRWRERQRQ----------------------------------
"""

data = {
"sequence": sequence,
"alignments": {
"small_bfd": {
"a3m": {
"alignment": small_bfd_alignment_in_a3m, 
"format": "a3m",
}
},
},
"selected_models": [1, 2],
"relax_prediction": False,
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