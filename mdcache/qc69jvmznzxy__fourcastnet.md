---
title: "fourcastnet"
publisher: "nvidia"
type: "endpoint"
updated: "2025-03-22T01:59:48.383Z"
description: "FourCastNet predicts global atmospheric dynamics of various weather / climate variables."
canonical: "https://build.nvidia.com/nvidia/fourcastnet"
---

# Model Overview

## Description

FourCastNet2 uses Spherical Fourier Neural Operator (SFNO) to predict a collection of surface and atmospheric variables such as wind speed, temperature and pressure and is applied to forecasting global atmospheric dynamics.

FourCastNet is a data-driven model that provides accurate short to medium-range global predictions at a time-step size of 6 hours with predictive stability for over a year of simulated time (1,460 steps), while retaining physically plausible dynamics.

This model is ready for commercial use.

## Reference(s)

* [Spherical Fourier Neural Operator Paper](https://arxiv.org/abs/2306.03838) <br>
* [FourCastNet Paper](https://arxiv.org/abs/2202.11214) <br>
* [Codebase](https://github.com/NVIDIA/modulus) <br>
* [The ERA5 global reanalysis](https://doi.org/10.1002/qj.3803) <br>

## Model Architecture

**Architecture Type:** Neural Operator <br>
**Network Architecture:** FourCastNet SFNO <br>

## Input

**Input Type(s):**

- Tensor (73 Surface & Atmospheric Variables)
- DateTime<br>

**Input Format(s):** NumPy <br>
**Input Parameters:**

- Four Dimensional (4D) (batch, variable, latitude, longitude) <br>
- Input DateTime<br>

**Other Properties Related to Input:**
- 0.25 degree latitude-longitude grid
- Input resolution: [721, 1440]
- Latitude Coordinates: [90, 89.75, 89.5, ..., -89.5, -89.75, -90]
- Longitude Coordinates: [0, 0.25, 0.5, ..., 359.25, 359.5, 359.75]
- Input weather variables: "u10m", "v10m", "u100m", "v100m", "t2m", "sp", "msl", "tcwv", "u50", "u100", "u150", "u200", "u250", "u300", "u400", "u500", "u600", "u700", "u850", "u925", "u1000", "v50", "v100", "v150", "v200", "v250", "v300", "v400", "v500", "v600", "v700", "v850", "v925", "v1000", "z50", "z100", "z150", "z200", "z250", "z300", "z400", "z500", "z600", "z700", "z850", "z925", "z1000", "t50", "t100", "t150", "t200", "t250", "t300", "t400", "t500", "t600", "t700", "t850", "t925", "t1000", "q50", "q100", "q150", "q200", "q250", "q300", "q400", "q500", "q600", "q700", "q850", "q925", "q1000"<br>

## Output

**Output Type(s):**

- Tensor (73 Surface & Atmospheric Variables)

**Output Format(s):** NumPy <br>
**Output Parameters:**

- Four Dimensional (4D) (batch, variable, latitude, longitude) <br>

**Other Properties Related to Output:**
- Time-delta of 6 hours from input array
- 0.25 degree latitude-longitude grid
- Output resolution: [721, 1440]
- Latitude Coordinates: [90, 89.75, 89.5, ..., -89.5, -89.75, -90]
- Longitude Coordinates: [0, 0.25, 0.5, ..., 359.25, 359.5, 359.75]
- Output weather variables: "u10m", "v10m", "u100m", "v100m", "t2m", "sp", "msl", "tcwv", "u50", "u100", "u150", "u200", "u250", "u300", "u400", "u500", "u600", "u700", "u850", "u925", "u1000", "v50", "v100", "v150", "v200", "v250", "v300", "v400", "v500", "v600", "v700", "v850", "v925", "v1000", "z50", "z100", "z150", "z200", "z250", "z300", "z400", "z500", "z600", "z700", "z850", "z925", "z1000", "t50", "t100", "t150", "t200", "t250", "t300", "t400", "t500", "t600", "t700", "t850", "t925", "t1000", "q50", "q100", "q150", "q200", "q250", "q300", "q400", "q500", "q600", "q700", "q850", "q925", "q1000"<br>

## Software Integration
**Runtime Engine(s):** Not Applicable <br>
**Supported Hardware Microarchitecture Compatibility:** <br>
* Ampere <br>
* Hopper <br>
* Turing <br>

**Supported Operating System(s):**
* Linux <br>

## Model Version(s)

**Model version:** v1  <br>

# Training, Testing, and Evaluation Datasets:

## Training Dataset

**Link:** [ERA5](https://cds.climate.copernicus.eu/) <br>

*Data Collection Method by dataset* <br>
* Automatic/Sensors <br>

*Labeling Method by dataset* <br>
* Automatic/Sensors <br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**
ERA5 data for the years of 1979-2017. ERA5 provides hourly estimates of various
atmospheric, land, and oceanic climate variables. The data covers the Earth on a 30km
grid and resolves the atmosphere at 137 levels. <br>

## Evaluation Dataset

**Link:** [ERA5](https://cds.climate.copernicus.eu/) <br>

*Data Collection Method by dataset* <br>
* Automatic/Sensors <br>

*Labeling Method by dataset* <br>
* Automatic/Sensors <br>

**Properties (Quantity, Dataset Descriptions, Sensor(s)):**
ERA5 data for the year of 2018. ERA5 provides hourly estimates of various atmospheric,
land, and oceanic climate variables. The data covers the Earth on a 30km grid and
resolves the atmosphere at 137 levels. <br>

# Inference:

**Engine:** [Triton](https://developer.nvidia.com/triton-inference-server) <br>
**Test Hardware:**
* A100 <br>
* H100 <br>
* L40S <br>
* RTX6000 <br>

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established
policies and practices to enable development for a wide array of AI applications.
When downloaded or used in accordance with our terms of service, developers should work
with their supporting model team to ensure this model meets requirements for the
relevant industry and use case and addresses unforeseen product misuse.
For more detailed information on ethical considerations for this model, please see the
Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards [here](https://ai.nvidia.com).
Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## License
This model is licensed under the [NVIDIA AI Product Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/). By pulling and using this model, you accept the terms and conditions of this license.

**You are responsible for ensuring that your use of NVIDIA AI Foundation Models complies with all applicable laws.**

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing:  |  None of the Above
Measures taken to mitigate against unwanted bias:                                                   |  None

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Application & Domain:                                                                         |  Global Weather Forecasting
Model Type:                                                                                            |  Neural Operator
Intended User:                                                                                         |  Climate and Weather scientists accelerating weather prediction with AI.
Output:                                                                                                |  Global forecast prediction of surface and atmosphere variables.
Describe how the model works:                                                                          |  Neural operator auto-regressively predicts a time-series forecast from an initial state.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Not Applicable
Technical Limitations:                                                                                 | The model may perform poorly for longer range forecasts and atmospheric data sources different from that in the ERA5 training dataset
Verified to have met prescribed NVIDIA quality standards:                                                     |  Yes
Performance Metrics:                                                                                   |  Accuracy, Throughput and Latency
Potential Known Risks:                                                                                 |  This model may mispredict global atmospheric dynamics.
Licensing:                                                                                             |  [Earth-2 Service Terms of Use](https://ngc.nvidia.com/legal/terms)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personally-identifiable information (PII)?                                                     |  None
Was consent obtained for any personal data used?                                                                                             |  Not Applicable (N/A)
Protected class data used to create this model?                                                                                       |  None
How often is dataset reviewed?                                                                                                     |  Before Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  No
If personal data collected for the development of the model, was it collected directly by NVIDIA?                                            |  N/A
If personal data collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  N/A
If personal data collected for the development of this AI model, was it minimized to only what was required?                                 |  N/A
Is there provenance for all datasets used in training?                                                                                                     |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  Global Weather Forecasting
Describe the life critical impact (if present).   |  None Known
Use Case Restrictions:                              |  Abide by [NVIDIA AI Product Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/product-specific-terms-for-ai-products/)
Model and dataset restrictions:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to.

## Prototype

```bash
#!/usr/bin/env bash
if [ "$NGC_API_KEY" = "" ]; then
NGC_API_KEY='$NVIDIA_API_KEY'
fi
invoke_url="https://climate.api.nvidia.com/v1/nvidia/fourcastnet"

output_file="output.zip"
payload='{
"input_id": ,
"variables": "",
"simulation_length": ,
"ensemble_size": ,
"noise_amplitude": 
}'
echo $payload
# Initial request
echo "$(date) Making inference request"
response=$(curl -D - --request POST -H "content-type: application/json" -H "Authorization: Bearer $NGC_API_KEY" -H "NVCF-POLL-SECONDS: 5" --data "$payload" --location "$invoke_url")

http_status=$(echo "$response" | awk '{print $2;exit}')
if [ "$http_status" -eq 202 ]; then
req_id=$(echo "$response" | grep -i "nvcf-reqid:" | awk '{print $2}' | tr -d '\r')
else
echo "Unexpected HTTP status: $http_status"
echo "Response: $response"
exit 1
fi

status_url="https://api.nvcf.nvidia.com/v2/nvcf/pexec/status/$req_id"
# Poll the /status endpoint
echo "$(date) Polling job $req_id"
while true; do
status_response=$(curl -s -D - --request GET -H "content-type: application/json"  -H "Authorization: Bearer $NGC_API_KEY"  -H "NVCF-POLL-SECONDS: 5"  --location "$status_url"  -o "$output_file")
status_http_status=$(echo "$status_response" | awk '{print $2;exit}')

if [ "$status_http_status" -eq 200 ]; then
echo "Saved response to file"
break
elif [ "$status_http_status" -eq 302 ]; then
echo "Downloading large asset"
asset_url=$(echo "$status_response" | grep -i "location:" | awk '{print $2}' | tr -d '\r')
curl --request GET --location "${asset_url}" -o "${output_file}"
break
elif [ "$status_http_status" -ne 202 ]; then
echo "Unexpected HTTP status: $status_http_status"
echo "Response: $status_response"
exit 1
fi
echo "$(date) Job still running, status $status_http_status"
# Wait before polling again
sleep 3
done
```

```python
#!/usr/bin/env python3
import os
import sys
import requests
import time
import logging

logging.basicConfig(
format='%(asctime)s %(levelname)-8s %(message)s',
level=logging.INFO,
datefmt='%Y-%m-%d %H:%M:%S')

output_file = "output.zip"

invoke_url = "https://climate.api.nvidia.com/v1/nvidia/fourcastnet"
headers = {
"Authorization": f"Bearer {os.getenv('NGC_API_KEY', '$NVIDIA_API_KEY')}",
"NVCF-POLL-SECONDS": "5"
}
payload = {
"input_id": ,
"variables": "",
"simulation_length": ,
"ensemble_size": ,
"noise_amplitude": ,
}

# re-use connections
session = requests.Session()

logging.info(f"Payload {payload}")
logging.info("Making inference request")
response = session.post(invoke_url, headers=headers, json=payload)
response.raise_for_status()
if response.status_code == 202:
request_id = response.headers['nvcf-reqid']
else:
raise Exception("Failed request")

logging.info(f"Polling job {request_id}")
status_url = f"https://api.nvcf.nvidia.com/v2/nvcf/pexec/status/{request_id}"
while(True):
response = session.get(status_url, headers=headers, allow_redirects=False)
response.raise_for_status()
# Invocation is fulfilled.
if response.status_code == 200:
logging.info(f"Invocation is fulfilled. Downloading to {output_file}")
with open(output_file, 'wb') as f:
f.write(response.content)
break
# Large asset response
elif response.status_code == 302:
logging.info(f"Downloading large asset output to {output_file}")
asset_url = response.headers['Location']
with requests.get(asset_url, stream=True) as r:
with open(output_file, 'wb') as f:
f.write(r.content)
break
# Response in progress
elif response.status_code == 202:
logging.info(f"Job still running")
else:
raise Exception(f"Unexpected status code {response.status_code}")
time.sleep(3)
```