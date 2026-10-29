---
title: "rfd4-proteina"
publisher: "ipd"
type: "endpoint"
updated: "2026-10-20T15:06:59.535Z"
description: "A unified generative model for protein, enzyme, binder and antibody design."
canonical: "https://build.nvidia.com/ipd/rfd4-proteina"
---

# Model Overview

## Description:
RFD4-Proteina is a unified generative model for protein design, produced through a
collaboration between NVIDIA's Generative AI team and the David Baker Lab at the
Institute for Protein Design. Rather than screening existing molecules, it creates
them: users express structural, sequence and chemical constraints, then generate,
score and search for molecules that satisfy their objectives.<br>

This deployment serves seven design tasks — generation, motif
scaffolding, enzyme design, small-molecule binder design, antibody design, partial
diffusion and inverse folding — and supports reward-guided beam search over the
diffusion trajectory, so a request can optimise against locally computable metrics
rather than returning a single unranked sample.<br>

This model is ready for commercial or non-commercial use.<br>

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and
built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [Institute for Protein Design RFD4-Proteina Model Card](https://github.com/RosettaCommons/RFD4-Proteina).<br>

### License/Terms of Use:
GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Service Terms of Use](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause), Copyright (c) 2026, Institute for Protein Design, University of Washington.

**You are responsible for ensuring that your use of NVIDIA AI Foundation Models
complies with all applicable laws.**

## Deployment Geography:
Global

## Use Case
RFD4-Proteina is used by academic and pharmaceutical industry research labs for de
novo protein, enzyme, binder and antibody design, supporting early-stage biologic
discovery: scaffolding a functional site, designing a binder against a known
target, or resampling a sequence for an existing backbone.

## Release Date
- build.nvidia.com 10/20/2026 (NVIDIA GTC Berlin) via [build.nvidia.com/ipd/rfd4-proteina](https://build.nvidia.com/ipd/rfd4-proteina)
- NGC 10/20/2026 (NVIDIA GTC Berlin) via [catalog.ngc.nvidia.com/orgs/nim/teams/ipd/containers/rfd4-proteina](https://catalog.ngc.nvidia.com/orgs/nim/teams/ipd/containers/rfd4-proteina)

## References:
```
@article{Watson2023,
author  = {Watson, Joseph L. and Juergens, David and Bennett, Nathaniel R. and Trippe, Brian L. and Yim, Jason and Eisenach, Helen E. and Ahern, Woody and Borst, Andrew J. and Ragotte, Robert J. and Milles, Lukas F. and Wicky, Basile I. M. and Hanikel, Nikita and Pellock, Samuel J. and Courbet, Alexis and Sheffler, William and Wang, Jue and Venkatesh, Preetham and Sappington, Isaac and Torres, Susana Vázquez and Lauko, Anna and De Bortoli, Valentin and Mathieu, Emile and Ovchinnikov, Sergey and Barzilay, Regina and Jaakkola, Tommi S. and DiMaio, Frank and Baek, Minkyung and Baker, David},
journal = {Nature},
title   = {De novo design of protein structure and function with RFdiffusion},
year    = {2023},
volume  = {620},
pages   = {1089--1100},
doi     = {10.1038/s41586-023-06415-8}
}
```

## Model Architecture:
**Architecture Type:** Other <br>
**Network Architecture:** RFD4-Proteina, a latent-space flow-matching generative model <br>
** Number of model parameters: 4.34×10⁸ (trunk 1.78×10⁸, autoencoder 2.56×10⁸) <br>

The trunk runs inside a latent space produced by a paired autoencoder. The default
composition uses the `thinking_medium` recycle schedule: 60 sampling steps with
recycle depth peaking at 6 through the middle of the trajectory, 185 trunk passes
in total, so compute concentrates where the fold is decided rather than on the
noisy start or the already-settled end. `thinking_low` and `thinking_high` trade
that budget down and up. The released checkpoint has self-conditioning off and
carries no MSA module.

## Input:
**Input Type(s):** Text (protein structure and design specification) <br>
**Input Format(s):** annotated mmCIF; condition spec<br>
**Input Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Input:** Design length up to 1024 tokens; attached structures are named files carried in the request body <br>

Two input dialects sit behind a `format` discriminator. An annotated mmCIF carries
the design conditions inside the file; a condition spec states them as selections
over an attached structure. Attached structures are named files carried in the
request body, never filesystem paths.

## Output:
**Output Type(s):** Text (protein structure and sequence) <br>
**Output Format:** annotated mmCIF, plus per-design metrics <br>
**Output Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:** Per-design metrics (for example clash fraction, bond-length violations and sequence adherence) are returned alongside each structure <br>

Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated
systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks
(e.g., CUDA libraries), the model achieves faster inference times compared to
CPU-only solutions.

## Tasks

| Task | What it does |
| --- | --- |
| `generation` | Generated regions start from noise while any supplied conditions are preserved; covers de novo monomers and conditional designs alike, including protein and DNA binders |
| `motif_scaffolding` | A scaffold around motif segments held at their given positions |
| `enzyme_design` | Scaffold an unindexed catalytic site, the model choosing placement |
| `small_molecule_binder` | A protein around an atomized small molecule at its given pose |
| `antibody_design` | Redesign CDR loops on a fixed Ig framework, optionally against a fixed antigen; also covers TCRs |
| `partial_diffusion` | Refine an existing design by restarting the trajectory partway |
| `inverse_folding` | Hold the backbone, resample sequence and side chains |

`task` selects how the sampler runs the trajectory, not which design problem is
being solved. Several problems need no task of their own because they are
expressed by what the input holds fixed: a protein binder against a target is
`generation` with the target's atoms held by coordinate and sequence
conditioning and its epitope marked as hotspots.

## Reward-guided search

Search is not best-of-N. At each checkpoint every surviving candidate is branched,
each branch is rolled out to a clean structure to be scored, and the best
`beam_width` survive. Compute concentrates on trajectories that are going
somewhere, which is why it beats filtering at equal budget. Cost is roughly
`beam_width * n_branch * (len(step_checkpoints) - 1)` rollouts per replicate.

This deployment serves the in-repository, non-oracle metrics by default.
Oracle-backed refolding metrics require an operator-mounted structure-prediction
model and are not part of the default deployment.

## Software Integration:
**Runtime Engine(s):**
* NVIDIA NIM <br>
* PyTorch <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Blackwell <br>
* NVIDIA Hopper <br>
* NVIDIA Lovelace <br>

**Supported Operating System(s):** <br>
* Linux <br>

The integration of foundation and fine-tuned models into AI systems requires
additional testing using use-case-specific data to ensure safe and effective
deployment. Following the V-model (a development methodology), iterative testing and validation at
both unit and system levels are essential to mitigate risks, meet technical and
functional requirements, and ensure compliance with safety and ethical standards
before deployment. <br>

## Model Version(s):
* Institute for Protein Design trained weights
* RFD4-Proteina version 1.0.0 <br>

# Training and Evaluation Datasets:

## Training Dataset:

** Data Modality <br>
* [Other: Protein 3D structures and sequences]

** Training Data Size <br>
* Undisclosed (third-party)

**Link:** [Institute for Protein Design RFD4-Proteina](https://github.com/RosettaCommons/RFD4-Proteina) <br>

This model's weights were trained by the Institute for Protein Design and are not
collected, curated, or retrained by NVIDIA. For the RFdiffusion backbone-generation
approach this model builds on, see [Watson et al. 2023](https://doi.org/10.1038/s41586-023-06415-8).

** Data Collection Method by dataset <br>
* Undisclosed

** Labeling Method by dataset <br>
* Undisclosed

**Properties:** The training data composition, count and content are not disclosed
by the Institute for Protein Design. The data is structural (protein 3D
structures and sequences) and contains no natural-language text.

## Evaluation Dataset:

**Link:** [Institute for Protein Design RFD4-Proteina](https://github.com/RosettaCommons/RFD4-Proteina) <br>

** Data Collection Method by dataset <br>
* Undisclosed

** Labeling Method by dataset <br>
* Undisclosed

**Properties:** Design-quality evaluation of this model was performed by the
Institute for Protein Design and is not reproduced by NVIDIA; its dataset count
and composition are not disclosed. The data is structural (protein, enzyme,
small-molecule-binder and motif-scaffolding design targets) and contains no
natural-language text.

## Testing Dataset:

**Link:** [Institute for Protein Design RFD4-Proteina](https://github.com/RosettaCommons/RFD4-Proteina) <br>

** Data Collection Method by dataset <br>
* Undisclosed

** Labeling Method by dataset <br>
* Undisclosed

**Properties:** NVIDIA's own verification of this NIM deployment uses 87
annotated mmCIF design inputs drawn from 12 conditioning families authored by the
Institute for Protein Design: motif scaffolding (50 inputs), unconditional and
secondary-structure-conditioned generation (25) and small-molecule-binder and
interchain-interaction conditioning (12). Each input is a protein structure,
optionally with a ligand, and contains no natural-language text. It checks that
each supported task returns a valid, physically finite structure under the
metrics the NIM reports; it is a functional check, not a design-quality
benchmark.

## Inference:
**Acceleration Engine:** PyTorch, NVIDIA BioNeMo Inference Runtime (BioIR) <br>
**Test Hardware:** <br>
* NVIDIA A100 <br>
* NVIDIA B200 <br>
* NVIDIA B300 <br>
* NVIDIA DGX Spark (GB10) <br>
* NVIDIA GB200 <br>
* NVIDIA GB300 <br>
* NVIDIA GH200 <br>
* NVIDIA H100 <br>
* NVIDIA H200 <br>
* NVIDIA L40S <br>
* NVIDIA RTX 6000 Ada Generation <br>
* NVIDIA RTX PRO 6000 Blackwell Server Edition <br>
* NVIDIA RTX PRO 6000 Blackwell Workstation Edition <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established
policies and practices to enable development for a wide array of AI applications.
Developers should work with their internal model team to ensure this model meets
requirements for the relevant industry and use case and addresses unforeseen
product misuse.

Users are responsible for ensuring the physical properties of model-generated
molecules are appropriately evaluated and comply with applicable safety
regulations and ethical standards.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns
[here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

# Get Help

## Enterprise Support
Get access to knowledge base articles and support cases or [submit a ticket](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Specifications

- **Parameters:** 435,622,465

## Capabilities

- **Function Calling:** Not supported

## Prototype

```bash
#!/usr/bin/env bash
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail

# The request body carries the input structure inline, so it is a file rather
# than a here-doc: the examples on this page are 13 KB to 725 KB of annotated
# mmCIF. Download an example request from the Deploy tab.
REQUEST=${REQUEST:-request.json}

URL=${URL:-https://health.api.nvidia.com/v1/biology/ipd/rfd4-proteina/generative}

: "${NVIDIA_API_KEY:?Set NVIDIA_API_KEY to an NGC personal key}"

# A design runs tens of seconds and reward-guided search runs longer, so ask
# NVCF to hold the connection instead of handing back a polling job.
curl -sS -X POST "${URL}" \
-H "Authorization: Bearer ${NVIDIA_API_KEY}" \
-H "Content-Type: application/json" \
-H "NVCF-POLL-SECONDS: 300" \
--max-time 600 \
--data-binary "@${REQUEST}" \
| jq '{task, duration_ms, warnings, designs: [.designs[] | {design_id, sequence, metrics}]}'
```

```python
#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Submit an RFD4-Proteina design request to the NVIDIA-hosted NIM."""

from __future__ import annotations

import json
import os
import urllib.request
from pathlib import Path

URL = os.getenv(
"URL",
"https://health.api.nvidia.com/v1/biology/ipd/rfd4-proteina/generative",
)

# The input structure travels inline, so the body is a file rather than a
# literal: the examples on this page are 13 KB to 725 KB of annotated mmCIF.
# Download an example request from the Deploy tab.
REQUEST = Path(os.getenv("REQUEST", "request.json"))

def main() -> None:
api_key = os.environ["NVIDIA_API_KEY"]
request = urllib.request.Request(
URL,
data=REQUEST.read_bytes(),
headers={
"Authorization": f"Bearer {api_key}",
"Content-Type": "application/json",
# A design runs tens of seconds and reward-guided search runs
# longer, so ask NVCF to hold the connection rather than hand back
# a polling job.
"NVCF-POLL-SECONDS": "300",
},
method="POST",
)
with urllib.request.urlopen(request, timeout=600) as response:
result = json.load(response)

print(f"{result['task']} in {result['duration_ms'] / 1000:.1f}s")
for design in result["designs"]:
Path(design["structure"]["filename"]).write_text(design["structure"]["content"])
print(f"  {design['design_id']}: {design['sequence']}")

if __name__ == "__main__":
main()
```