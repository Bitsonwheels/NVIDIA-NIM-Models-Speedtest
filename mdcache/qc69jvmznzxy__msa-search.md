---
title: "msa-search"
publisher: "colabfold"
type: "endpoint"
updated: "2025-06-16T15:53:34.676Z"
description: "Generates a multiple sequence alignment from a query sequence and a protein sequence database search."
canonical: "https://build.nvidia.com/colabfold/msa-search"
---

## Model Overview

### Description:

The MSA Search model is powered by GPU MMSeqs2. GPU MMSeqs2 is a GPU-accelerated toolkit for protein database search, Multiple Sequence Alignment (MSA), and Structural Template Search. While not a deep learning model, MMSeqs2 does require large protein databases for sequence similarity search and structural template discovery.
<br>

This model is ready for commercial use.
<br>

### Third-Party Community Consideration

This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case. ColabFold was developed by the authors of Mirdita *et al*. 2022. GPU MMSeqs2 was developed by the authors of Kallenborn *et al*. 2025.

#### License / Terms of Use

GOVERNING TERMS: The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). MSA Data: This data is governed by the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/legalcode.en) (CC-BY-4.0).

### Deployment Geography
Global

### Use Case
The MSA Search model enables researchers and commercial entities in the Drug Discovery, Life Sciences, and Digital Biology fields to rapidly generate multiple sequence alignments (MSA) and find structural templates from PDB databases. The output MSA and template structures can be used in downstream protein structure prediction and evolutionary analysis applications.

### Release Date

#### 2.6.0

build.nvidia.com: 07/30/2026 via [build.nvidia.com](https://build.nvidia.com/colabfold/msa-search) <br>

### References:

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

```
@ARTICLE{mirdita2022colabfold,
title   = "ColabFold: making protein folding accessible to all",
author  = "Mirdita, Milot and Sch{\"u}tze, Konstantin and Moriwaki, Yoshitaka and Heo, Lim and Ovchinnikov, Sergey and Steinegger, Martin",
journal = "Nature Methods",
volume  = 19,
number  = 6,
pages   = "679--682",
month   = jun,
year    = 2022,
language = "en",
doi     = {10.1038/s41592-022-01488-1},
}
```

```
@ARTICLE{kallenborn2025gpu,
title   = "GPU-accelerated homology search with MMseqs2",
author  = "Kallenborn, Felix and Chacon, Alejandro and Hundt, Christian and Sirelkhatim, Hassan and Didi, Kieran and Cha, Sooyoung and Dallago, Christian and Mirdita, Milot and Schmidt, Bertil and Steinegger, Martin",
journal = "bioRxiv",
year    = 2025,
month   = jan,
day     = 20,
language = "en",
doi     = {10.1101/2024.11.13.623350},
}
```

<br>

### Model Architecture:

**Architecture Type:** Not Applicable — MSA Search is not a neural network; it is a GPU-accelerated sequence search tool (MMseqs2). <br>
**Network Architecture:** Not Applicable — see above. <br>
**Number of Parameters:** Not Applicable — see above. <br>

### Input:

**Input Type(s):** Protein Sequence, Databases, Structural Template Databases <br>
**Input Format(s):** String (less than or equal to 4096 characters), Constrained List of Strings (one or more valid database names) <br>
**Input Parameters:** String: One-Dimensional (1D); Constrained List of Strings: 1D <br>
**Other Properties Related to Input:** Maximum 4096 amino acid characters for protein sequences. No pre-processing required. <br>

### Output:

**Output Type(s):** Multiple Sequence Alignment in A3M or FASTA format; Structural templates in mmCIF format <br>
**Output Format:** A3M or FASTA (text file); mmCIF (text file)<br>
**Output Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:** Output alignment length depends on number of homologous sequences found in the database. Default maximum MSA depth is 500 sequences; an integrating system may apply a stricter global cap. <br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster inference times compared to CPU-only solutions.

### Software Integration:

**Runtime Engine(s):**
* Python, C++, CUDA <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Blackwell <br>
* NVIDIA Hopper<br>
* NVIDIA Lovelace <br>

**Supported Operating System:** <br>
* [Linux] <br>
* The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

### Model Version(s):
v2.0.0

## Training and Evaluation Datasets:
Not Applicable. MSA Search is not a machine learning model and does not involve training or evaluation/testing. It performs database search using GPU-accelerated MMseqs2.

### Training Dataset:

**Link:** Not Applicable.  <br>
** Data Collection Method by dataset <br>
* [Not Applicable] <br>

** Labeling Method by dataset <br>
* [Not Applicable] <br>

**Properties:**
Not Applicable.

### Evaluation Dataset:

**Link:** Not Applicable.  <br>
** Data Collection Method by dataset <br>
* [Not Applicable] <br>

** Labeling Method by dataset <br>
* [Not Applicable] <br>

**Properties:**
Not Applicable
<br>

### Inference:

**Acceleration Engine:** Python, C++, CUDA <br>
**Test Hardware:** <br>
* NVIDIA Ada Lovelace L40 <br>
* NVIDIA Ampere A100 <br>
* NVIDIA Blackwell B200 <br>
* NVIDIA Blackwell B300 <br>
* NVIDIA GB10 Grace Blackwell Superchip <br>
* NVIDIA Grace Blackwell GB200 Superchip <br>
* NVIDIA Grace Blackwell GB300 Superchip <br>
* NVIDIA Grace Hopper GH200 Superchip <br>
* NVIDIA Hopper H100 <br>
* NVIDIA Hopper H200 <br>
* NVIDIA Lovelace RTX 6000 Ada Generation <br>

### Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. 

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

**You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.**

## Get Help

### Enterprise Support
Get access to knowledge base articles and support cases or  submit a ticket at the [NVIDIA AI Enterprise Support Services page.](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Capabilities

- **Function Calling:** Not supported

## Prototype

```bash
#!/usr/bin/env bash
set -e

URL="${URL:-https://health.api.nvidia.com/v1/biology/colabfold/msa-search/predict}"
if [[ "$URL" == *"nvidia"* ]] && [ -z "$NVIDIA_API_KEY" ]; then
read -p "Paste Run Key: " NVIDIA_API_KEY
fi

request='{
"sequence": "SGSMKTAISLPDETFDRVSRRASELGMSRSEFFTKAAQR",
"e_value": 0.0001,
"iterations": 1,
"output_alignment_formats": ["a3m", "fasta"]
}'

response=$(curl -s -w "\n%{http_code}" \
-H 'Content-Type: application/json' \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-d "$request" "$URL")

http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

echo "HTTP Status: $http_code"
echo "Response (first 25 lines):"
printf '%b' "$body" | head -n 25 && echo ...trimmed...
```

```python
#!/usr/bin/env python3

import requests
import json
import os
from pathlib import Path

url = os.getenv("URL", "https://health.api.nvidia.com/v1/biology/colabfold/msa-search/predict")
key = os.getenv("NVIDIA_API_KEY") or input("Paste the Run Key: ") if "nvidia" in url else ""

r = requests.post(
json={
"sequence": "SGSMKTAISLPDETFDRVSRRASELGMSRSEFFTKAAQR",
"e_value": 0.0001,
"iterations": 1,
"output_alignment_formats": ["a3m", "fasta"],
},
url=url,
headers={"Authorization": f"Bearer {key}"},
)

print(r.text[:100], "...")
r = r.json()

Path("msa_outputs").mkdir(exist_ok=True)
Path("msa_outputs/response.json").write_text(json.dumps(r, indent=4, sort_keys=True))
print("Saved response to msa_outputs/response.json\n")

print("Response keys:", list(r.keys()), "\n")
print("Alignments by dbs:\n")
for db, formats in r["alignments"].items():
print(" ", db)
for fmt, alignment_obj in formats.items():
aln = alignment_obj["alignment"]
fmt_name = alignment_obj["format"]
print("   ", fmt_name, "lines:", len(aln.split("\n")))
from textwrap import indent
print(indent(aln[:300] + "...", "        | "))

f = Path(f"msa_outputs/{db}.{fmt_name}")
f.write_text(aln)
print(f"        Saved to {f}")
```