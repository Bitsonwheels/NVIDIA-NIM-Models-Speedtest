---
title: "cuopt"
publisher: "nvidia"
type: "endpoint"
updated: "2025-05-21T21:16:32.788Z"
description: "World-record accuracy and performance for complex route optimization."
canonical: "https://build.nvidia.com/nvidia/nvidia-cuopt"
---

# Model Overview

## Description

NVIDIA® cuOpt™ is an open-source, GPU-accelerated decision optimization engine that powers faster, smarter logistics routing, helping enterprises cut costs, boost revenue, and lower carbon emissions. It offers dynamic rerouting, horizontal load-balancing, and robotic simulations, with sub-second solver response times. 
cuOpt enables organizations to leverage the world's best accelerated optimization capabilities across multi- and hybrid cloud environments. It solves complex routing problems with multiple constraints and delivers new capabilities, empowering teams to make dynamic, data-driven decisions.

Typical Use Cases

**Last Mile Delivery** : Optimizes vehicle fleets to serve multiple demand points while minimizing costs, such as distance, time, or fleet size, under operational constraints. Each customer has specific demands and service requirements, while vehicles face limits on capacity, distance, emissions, and availability. Applications span manufacturing (component delivery to production lines), distribution (stocking retail stores), and e-commerce or grocery delivery (final hand-off to customers or drop-off locations).

**Dispatch Optimization**: Optimizes the allocation and routing of field technicians or vehicles to efficiently fulfill service requests. It balances factors like location, capacity, skillset, and priority to minimize travel time, fuel use, and costs while maintaining SLAs. The system adapts dynamically to new requests or disruptions and balances workloads to boost productivity. Essential for logistics, field services, emergency response, and other mobile operations.

**Pickup and Delivery**: Optimizes routes for fleets to efficiently pick up and drop off items while meeting operational constraints and service goals. Objectives include minimizing travel time, fleet size, and costs, maximizing utilization, and reducing emissions, all while maintaining SLAs and on-time performance. Both pickup and drop-off points have capacity, time window, and service constraints, while fleets are limited by load, distance, and emissions. Applicable to diverse scenarios such as food delivery, ride-hailing, retail distribution, parcel logistics, intralogistics, school transport, and waste collection.

## Terms of use
By using this software or microservice, you are agreeing to the [terms and conditions](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/) of the license and acceptable use policy.

### References(s):

- [NVIDIA cuOpt docs](https://docs.nvidia.com/cuopt/) <br>
- [NVIDIA cuOpt Resources](https://github.com/NVIDIA/cuopt-examples) <br>
- [DLI Course on NVIDIA cuOpt](https://www.nvidia.com/en-us/training/) <br>

## Model Architecture

**Architecture Type:** x86/aarch64 <br>
**Network Architecture:** Not Applicable (N/A) <br>
**Container Version:** 26.06.00 <br>

## Input

**Input Format:** Json data in Text or File format. <br>
**Input Parameters:** Please refer to [open-api](https://docs.nvidia.com/cuopt/user-guide/latest/open-api.html) specification.

## Output

**Output Format:**  Json data in Text or File format. <br>
**Output Parameters:** Please refer to [open-api](https://docs.nvidia.com/cuopt/user-guide/latest/open-api.html) specification. <br>

### Software Integration:

**Runtime(s):** N/A <br> 
**Supported Hardware Platform(s):** Please refer to [requirement doc](https://docs.nvidia.com/cuopt/user-guide/latest/system-requirements.html#system-requirements) <br>
**Supported Operating System(s):** Please refer to [requirements doc](https://docs.nvidia.com/cuopt/user-guide/latest/system-requirements.html#system-requirements) <br>

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing:  |  None
Measures taken to mitigate against unwanted bias:                                                   |  None

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Applications & Domains:                                                                       |  Solving routing problems (transportation & delivery) and operations research to optimize for time and cost
Intended Users:                                                                                        |  Data scientists,  operations research engineers, and AI developers building route optimization solutions
Output:                                                                                                |  List of tasks (e.g. delivery, pick-up) per vehicle
Describe how the model works:                                                                          |  Solver calculates route-specific parameters based upon constraints. 
Technical Limitations:                                                                                 |  None
Verified to have met prescribed NVIDIA quality standards:                                                     |  Yes
Performance Metrics:                                                                                   |  Throughput and Latency
Potential Known Risks:                                                                                 |  None Known
Licensing:                                                                                             |  [NVIDIA cuOpt AGREEMENT](https://ngc.nvidia.com/legal/terms)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personally-identifiable information (PII)?                                                     |  None
Was consent obtained for any PII used?                                                                                             |  Not Applicable (N/A); user should consider PII implications when using actual addresses for routing.
Protected class data used to create this model?                               |  N/A
How often is dataset reviewed?                                                                                                     |  N/A
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  N/A
If PII collected for the development of the model, was it collected directly by NVIDIA?                                            |  N/A
If PII collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  N/A
If PII collected for the development of this AI model, was it minimized to only what was required?                                 |  N/A
Is there provenance for all datasets used in training?                                                                                                      |  N/A
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  N/A
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  N/A

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  Solving Vehicle Routing Problems and Optimizing Logistics Operations
Describe the life-critical impact (if present).   |  None
Use Case Restrictions:                              |  Solver for Non-Commerical Use Only
Model and dataset restrictions:            |  The Principle of Least Privilege (PoLP) is applied limiting access for the solver's development.  Restrictions enforce solver access and solver license constraints adhered to.

## Prototype

```python
import requests

invoke_url = "https://optimize.api.nvidia.com/v1/nvidia/cuopt"
fetch_url_format = "https://optimize.api.nvidia.com/v1/status/"

headers = {
"Authorization": "Bearer $API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC",
"Accept": "application/json",
}

payload = {
"action": "cuOpt_OptimizedRouting",
"data": {
"cost_waypoint_graph_data": None,
"travel_time_waypoint_graph_data": None,
"cost_matrix_data": {
"data": {
"1": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
1,
0
]
],
"2": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
2,
0
]
]
}
},
"travel_time_matrix_data": {
"data": {
"1": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
1,
0
]
],
"2": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
2,
0
]
]
}
},
"fleet_data": {
"vehicle_locations": [
[
0,
0
],
[
0,
0
]
],
"vehicle_ids": [
"veh-1",
"veh-2"
],
"capacities": [
[
2,
2
],
[
4,
1
]
],
"vehicle_time_windows": [
[
0,
10
],
[
0,
10
]
],
"vehicle_break_time_windows": [
[
[
1,
2
],
[
2,
3
]
]
],
"vehicle_break_durations": [
[
1,
1
]
],
"vehicle_break_locations": [
0,
1
],
"vehicle_types": [
1,
2
],
"vehicle_order_match": [
{
"order_ids": [
0
],
"vehicle_id": 0
},
{
"order_ids": [
1
],
"vehicle_id": 1
}
],
"skip_first_trips": [
True,
False
],
"drop_return_trips": [
True,
False
],
"min_vehicles": 2,
"vehicle_max_costs": [
7,
10
],
"vehicle_max_times": [
7,
10
]
},
"task_data": {
"task_locations": [
1,
2
],
"task_ids": [
"Task-A",
"Task-B"
],
"demand": [
[
1,
1
],
[
3,
1
]
],
"task_time_windows": [
[
0,
5
],
[
3,
9
]
],
"service_times": [
0,
0
],
"order_vehicle_match": [
{
"order_id": 0,
"vehicle_ids": [
0
]
},
{
"order_id": 1,
"vehicle_ids": [
1
]
}
]
},
"solver_config": {
"time_limit": 1,
"objectives": {
"cost": 1,
"travel_time": 0,
"variance_route_size": 0,
"variance_route_service_time": 0,
"prize": 0
},
"verbose_mode": False,
"error_logging": True
}
},
"client_version": ""
}

# re-use connections
session = requests.Session()

response = session.post(invoke_url, headers=headers, json=payload)

while response.status_code == 202:
request_id = response.headers.get("NVCF-REQID")
fetch_url = fetch_url_format + request_id
response = session.get(fetch_url, headers=headers)

response.raise_for_status()
response_body = response.json()
print(response_body)
```

```javascript
import fetch from "node-fetch";

const invokeUrl = "https://optimize.api.nvidia.com/v1/nvidia/cuopt"
const fetchUrlFormat = "https://optimize.api.nvidia.com/v1/status/"

const headers = {
"Authorization": "Bearer $API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC",
"Accept": "application/json",
}

const payload = {
"action": "cuOpt_OptimizedRouting",
"data": {
"cost_waypoint_graph_data": null,
"travel_time_waypoint_graph_data": null,
"cost_matrix_data": {
"data": {
"1": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
1,
0
]
],
"2": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
2,
0
]
]
}
},
"travel_time_matrix_data": {
"data": {
"1": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
1,
0
]
],
"2": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
2,
0
]
]
}
},
"fleet_data": {
"vehicle_locations": [
[
0,
0
],
[
0,
0
]
],
"vehicle_ids": [
"veh-1",
"veh-2"
],
"capacities": [
[
2,
2
],
[
4,
1
]
],
"vehicle_time_windows": [
[
0,
10
],
[
0,
10
]
],
"vehicle_break_time_windows": [
[
[
1,
2
],
[
2,
3
]
]
],
"vehicle_break_durations": [
[
1,
1
]
],
"vehicle_break_locations": [
0,
1
],
"vehicle_types": [
1,
2
],
"vehicle_order_match": [
{
"order_ids": [
0
],
"vehicle_id": 0
},
{
"order_ids": [
1
],
"vehicle_id": 1
}
],
"skip_first_trips": [
true,
false
],
"drop_return_trips": [
true,
false
],
"min_vehicles": 2,
"vehicle_max_costs": [
7,
10
],
"vehicle_max_times": [
7,
10
]
},
"task_data": {
"task_locations": [
1,
2
],
"task_ids": [
"Task-A",
"Task-B"
],
"demand": [
[
1,
1
],
[
3,
1
]
],
"task_time_windows": [
[
0,
5
],
[
3,
9
]
],
"service_times": [
0,
0
],
"order_vehicle_match": [
{
"order_id": 0,
"vehicle_ids": [
0
]
},
{
"order_id": 1,
"vehicle_ids": [
1
]
}
]
},
"solver_config": {
"time_limit": 1,
"objectives": {
"cost": 1,
"travel_time": 0,
"variance_route_size": 0,
"variance_route_service_time": 0,
"prize": 0
},
"verbose_mode": false,
"error_logging": true
}
},
"client_version": ""
}

let response = await fetch(invokeUrl, {
method: "post",
body: JSON.stringify(payload),
headers: { "Content-Type": "application/json", ...headers }
});

while (response.status == 202) {
let requestId = response.headers.get("NVCF-REQID")
let fetchUrl = fetchUrlFormat + requestId;
response = await fetch(fetchUrl, {
method: "get",
headers: headers
})
}

if (response.status != 200) {
let errBody = await (await response.blob()).text()
throw "invocation failed with status " + response.status + " " + errBody
}

let response_body = await response.json()

console.log(JSON.stringify(response_body))
```

```bash
invoke_url='https://optimize.api.nvidia.com/v1/nvidia/cuopt'
fetch_url_format='https://optimize.api.nvidia.com/v1/status/'

authorization_header="Authorization: Bearer $API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC"
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data='{
"action": "cuOpt_OptimizedRouting",
"data": {
"cost_waypoint_graph_data": null,
"travel_time_waypoint_graph_data": null,
"cost_matrix_data": {
"data": {
"1": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
1,
0
]
],
"2": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
2,
0
]
]
}
},
"travel_time_matrix_data": {
"data": {
"1": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
1,
0
]
],
"2": [
[
0,
1,
1
],
[
1,
0,
1
],
[
1,
2,
0
]
]
}
},
"fleet_data": {
"vehicle_locations": [
[
0,
0
],
[
0,
0
]
],
"vehicle_ids": [
"veh-1",
"veh-2"
],
"capacities": [
[
2,
2
],
[
4,
1
]
],
"vehicle_time_windows": [
[
0,
10
],
[
0,
10
]
],
"vehicle_break_time_windows": [
[
[
1,
2
],
[
2,
3
]
]
],
"vehicle_break_durations": [
[
1,
1
]
],
"vehicle_break_locations": [
0,
1
],
"vehicle_types": [
1,
2
],
"vehicle_order_match": [
{
"order_ids": [
0
],
"vehicle_id": 0
},
{
"order_ids": [
1
],
"vehicle_id": 1
}
],
"skip_first_trips": [
true,
false
],
"drop_return_trips": [
true,
false
],
"min_vehicles": 2,
"vehicle_max_costs": [
7,
10
],
"vehicle_max_times": [
7,
10
]
},
"task_data": {
"task_locations": [
1,
2
],
"task_ids": [
"Task-A",
"Task-B"
],
"demand": [
[
1,
1
],
[
3,
1
]
],
"task_time_windows": [
[
0,
5
],
[
3,
9
]
],
"service_times": [
0,
0
],
"order_vehicle_match": [
{
"order_id": 0,
"vehicle_ids": [
0
]
},
{
"order_id": 1,
"vehicle_ids": [
1
]
}
]
},
"solver_config": {
"time_limit": 1,
"objectives": {
"cost": 1,
"travel_time": 0,
"variance_route_size": 0,
"variance_route_service_time": 0,
"prize": 0
},
"verbose_mode": false,
"error_logging": true
}
},
"client_version": ""
}'

response=$(curl --silent -i -w "
%{http_code}" --request POST \
--url "$invoke_url" \
--header "$authorization_header" \
--header "$accept_header" \
--header "$content_type_header" \
--data "$data"
)

http_code=$(echo "$response" | tail -n 1)
req_id=$(echo "$response" | grep -i '^nvcf-reqid:' | awk '{print $2}' | tr -d '\r')

while [ "$http_code" -eq 202 ]; do
response=$(curl --silent -i -w "
%{http_code}" --request GET \
--url "$fetch_url_format$req_id" \
--header "$authorization_header" \
--header "$accept_header" \
--header "$content_type_header" \
)

http_code=$(echo "$response" | tail -n 1)
req_id=$(echo "$response" | grep -i '^nvcf-reqid:' | awk '{print $2}' | tr -d '\r')
done

echo "$response" | sed '$d' | awk 'BEGIN{body=0} body{print} /^\r$/{body=1}'
```