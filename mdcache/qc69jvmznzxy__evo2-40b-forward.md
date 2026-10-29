---
title: "evo2-40b-forward"
publisher: "arc"
type: "endpoint"
updated: "2025-12-01T08:25:05.608Z"
description: "Evo 2 is a biological foundation model that is able to integrate information over long genomic sequences while retaining sensitivity to single-nucleotide changes."
canonical: "https://build.nvidia.com/arc/evo2-40b-forward"
---

# Evo 2 NIM Overview

## Description
Evo 2 is a biological foundation model that is able to integrate information over long genomic sequences while retaining sensitivity to single-nucleotide change. At 7 billion parameters, the model understands the genetic code for all domains of life and is the largest AI model for biology to date. Evo 2 was trained on a dataset of nearly 9 trillion nucleotides.

This model is ready for commercial use.

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party's requirements for this application and use case.

## License/Terms of Use
GOVERNING TERMS: The NIM container is governed by the [NVIDIA Software License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-software-license-agreement/) and [Product-Specific Terms for AI Products](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). Use of this model is governed by the [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). ADDITIONAL INFORMATION: [Apache 2.0 License](https://github.com/arcinstitute/evo2).

**You are responsible for ensuring that your use of NVIDIA AI Foundation Models complies with all applicable laws.**

## Deployment Geography
Global

## Use Case
Evo is able to perform zero-shot function prediction for genes. Evo also can perform multi-element generation tasks, such as generating synthetic CRISPR-Cas molecular complexes. Evo 2 can also predict gene essentiality at nucleotide resolution and can generate coding-rich sequences up to at least 1M kb in length. Advances in multi-modal and multi-scale learning with Evo provide a promising path toward improving our understanding and control of biology across multiple levels of complexity.

## Release Date
NGC 09/25/2025 via https://catalog.ngc.nvidia.com/orgs/nim/teams/arc/containers/evo2-7b

## Reference(s)
- [Evo 2 preprint](https://arcinstitute.org/manuscripts/Evo2)
- [Evo Designer](https://arcinstitute.org/tools/evo/evo-designer)
- [Evo Mech Interp Visualizer](https://arcinstitute.org/tools/evo/evo-mech-interp)
- [Evo 2 code](https://github.com/arcinstitute/evo2)
- [NVIDIA Blog](https://developer.nvidia.com/blog/understanding-the-language-of-lifes-biomolecules-across-evolution-at-a-new-scale-with-evo-2/)

## Model Architecture
- **Architecture Type:** Generative Neural Network
- **Network Architecture:** StripedHyena
- **Number of model parameters:** 7 Billion

## Input
- **Input Type(s):** DNA Sequence
- **Input Format(s):** String
- **Input Parameters:** One-Dimensional (1D)

The user supplies an uppercase DNA sequence which may optionally be prepended with a specifically formatted taxonomy prompt (also uppercase) for an organism. The format of this prompt is `|D__[DOMAIN];P__[PHYLUM];C__[CLASS];O__[ORDER];F__[FAMILY];G__[GENUS];S__[SPECIES]|"`. For example, the token for Escherichia coli would be `|D__BACTERIA;P__PSEUDOMONADOTA;C__GAMMAPROTEOBACTERIA;O__ENTEROBACTERALES;F__ENTEROBACTERIACEAE;G__ESCHERICHIA;S__ESCHERICHIA|`. You can include a taxonomy token anywhere in your input DNA for your target organism if you want to bias the model's generated result in that direction.

## Output
- **Output Type(s):** DNA Sequence
- **Output Format:** String
- **Output Parameters:** One-Dimensional (1D)

Our AI models are designed and/or optimized to run on **NVIDIA GPU-accelerated systems**. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration

### Runtime Engine(s)
- PyTorch
- Transformer Engine

### Supported Hardware Microarchitecture Compatibility
- NVIDIA Hopper

### Preferred Operating System(s)
- Linux

The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.

## Model Version(s)
evo2-7b:2.0.0

## Training, Testing, and Evaluation Datasets

- **Data Modality:** Text
- **Text Training Data Size:** 9.3 Trillion Tokens

Multiple datasets were used for training, testing and evaluation (see details below).

### OpenGenome

**Link:** https://www.science.org/doi/10.1126/science.ado9336

**Data Collection Method:** Automatic/Sensors/Human

**Labeling Method by dataset:** N/A (no labels)

The previously published OpenGenome dataset was used in its entirety as part of the training data for this study. This included representative prokaryotic genomes available through GTDB release v214.1, and curated phage and plasmid sequences retrieved through IMG/VR and IMG/PR.

### Updated GTDB prokaryotic genomes

**Link:** https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkab776/6370255

**Data Collection Method:** Automatic/Sensors/Human

**Labeling Method by dataset:** Automatic

New prokaryotic reference genomes made available through the GTDB release 220.0 update were added to the training data for this study. New genomes were identified by selecting all species' reference genomes that had no previously published (release 214.1) genomes within their species cluster, resulting in 28,174 additional prokaryotic genomes.

### NCBI Eukaryotic reference genomes

**Link:** https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0997-x

**Data Collection Method:** Automatic/Sensors/Human

**Labeling Method by dataset:** Automatic

All available eukaryotic reference genomes were downloaded from NCBI on 05/32/2024, excluding atypical genomes, metagenome-assembled genomes, and genomes from large multi-isolate projects. This resulted in 16,704 genomes including an estimated ~10.7 trillion nucleotides. Only contigs that were annotated as 'Primary Assembly', 'non-nuclear', or 'aGasCar1.hap1' (an aberrant annotation that applied only to GCA_027917425.1) were retained. Mash sketch was run on each individual genome with the flag "-s 10000" and the mash distance was calculated between all genomes as an estimate for their pairwise 1-ANI (average nucleotide identity). All genomes with a mash distance < 0.01 were joined with edges in a graph, and clusters were identified by finding connected components. One representative genome per cluster was chosen, prioritizing genomes with a higher assembly level and genomes with longer total sequence length. This clustering resulted in 15,148 candidate genomes. Genomes were further filtered by removing ambiguous nucleotides at the termini of each contig, by removing regions annotated as "centromere" in an available GFF file, and by removing contigs that were less than 10 kb in total length. Finally, contigs that were composed of more than 5% ambiguous nucleotides were removed. This final filtered set included 15,032 genomes and 6.98 trillion nucleotides.

### Bridge Metagenomic Data

**Link:** https://www.nature.com/articles/s41586-024-07552-4

**Data Collection Method:** Automatic/Sensors/Human

**Labeling Method by dataset:** Automatic

A previously described metagenomics dataset was further curated as part of the training data. This included 41,253 metagenomes and metagenome-assembled genomes from NCBI, JGI IMG, MGnify, MG-RAST, Tara Oceans samples, and Youngblut et al. animal gut metagenomes. All contigs were split at consecutive stretches of ambiguous nucleotides of length 5 bp or longer, the split contigs were filtered by a minimum sequence length of 1 kb, and only contigs with at least one open reading frame as predicted by prodigal were kept. Contig-encoded proteins were previously clustered at 90% identity using MMseqs. To further remove redundant sequences, contigs were sorted by descending length, and each contig was only retained if at least 90% of its respective protein clusters were not already in the sequence collection (determined using a bloom filter).

### NCBI Organelle

**Link:** https://www.ncbi.nlm.nih.gov/datasets/organelle

**Data Collection Method:** Automatic/Sensors/Human

**Labeling Method by dataset:** Automatic

Eukaryotic organelle genomes: 33,457 organelle genomes were identified and downloaded using the "NCBI Organelle" web resource. Ambiguous nucleotides at the terminal ends of the organelle genome sequences were removed. Sequences that had over 25 ambiguous nucleotides were removed. This resulted in 32,241 organelle genomes that were used for training, including 1,613 mitochondria, 12,856 chloroplasts, 1,751 plastids, 18 apicoplasts, 1 cyanelle, and 1 kinetoplast.

## Inference

### Engine
- PyTorch 2.5.0
- Transformer Engine 1.9.0

### Test Hardware
- H200 (1 and 2 GPU configurations, 144 GB each)
- H100 (2 GPU configuration, 80 GB each)

## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Capabilities

- **Function Calling:** Not supported

## Prototype

```bash
#!/usr/bin/env bash
set -e

URL=${URL:-https://health.api.nvidia.com/v1/biology/arc/evo2-40b/forward}

request='{
"sequence": "ATCG",
"output_layers": ["output_layer", "decoder.layers.20.mlp"]
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
from base64 import decodebytes

r = requests.post(
url=os.getenv("URL", "https://health.api.nvidia.com/v1/biology/arc/evo2-40b/forward"),
headers={"Authorization": "Bearer $NVIDIA_API_KEY"},
json={
"sequence": "ATCG",
"output_layers": ["output_layer", "decoder.layers.20.mlp"],
},
)

if "application/json" in r.headers.get("Content-Type", ""):
print(r, "Saving numpy array to data.npz:\n", r.text[:200], "...")
Path("data.npz").write_bytes(decodebytes(json.loads(r.text)["data"].encode("ascii")))
elif "application/zip" in r.headers.get("Content-Type", ""):
print(r, "Saving large response to data.zip")
Path("data.zip").write_bytes(r.content)
else:
print(r, r.headers, r.content)
```