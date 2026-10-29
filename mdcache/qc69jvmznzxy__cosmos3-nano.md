---
title: "cosmos3-nano"
publisher: "nvidia"
type: "endpoint"
updated: "2026-06-01T04:48:19.454Z"
description: "Generates images, videos and action predictions from text, visual inputs and spatial controls, with mandatory input screening and visual SynthID watermarking."
canonical: "https://build.nvidia.com/nvidia/cosmos3-nano"
---

# Cosmos3 Nano

[Model card](https://huggingface.co/nvidia/Cosmos3-Nano) | [Code](https://github.com/nvidia/cosmos) | [Technical report](https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf) | [Download NIM](https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/cosmos3/-)

Cosmos3 Nano is NVIDIA's world foundation model for generating images, videos, and action predictions for Physical AI workflows, including robotics, autonomous vehicles, and industrial simulation. This hosted generator accepts text prompts, image and video conditioning, spatial video controls, and action trajectories. Input-media screening and visual SynthID watermarking are mandatory.

## Model information

**Model developer:** NVIDIA. **Architecture:** Transformer, using the Cosmos3 Mixture-of-Transformers architecture. Visual and action generation use iterative denoising. The [base model card](https://huggingface.co/nvidia/Cosmos3-Nano) documents architecture, model specifications, release information, and research integrations.

**This model was developed based on:**  [Cosmos Framework](https://github.com/nvidia/cosmos-framework)

**Number of trainable model parameters:**

- Cosmos3-Edge: 4B
- Cosmos3-Nano: 16B
- Cosmos3-Super: 64B
- Cosmos3-Nano-Policy-Droid: 16B
- Cosmos3-Super-Image2Video: 64B
- Cosmos3-Super-Text2Image: 64B

The underlying model is trained on curated public, private, and synthetic multimodal data. The model card describes acquisition, filtering, provenance review, and evaluation datasets. See the [Public Summary of Training Content](https://docs.nvidia.com/cosmos/latest/_downloads/e482b7114ce8dbfbb07d2d4b42cafe4e/training-content-Cosmos-3.pdf) for training-data information and the [technical report](https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf) for benchmarks. Model-level materials do not specify hosted API latency or availability guarantees; the endpoint contract is described below and in its API reference.

## Generation modes

Every request requires `model_mode`. Fields outside the selected mode are rejected. `text2image` and `text2video` require a nonempty `prompt`.

| `model_mode` | Conditioning input | Output |
| --- | --- | --- |
| `text2image` | Text prompt | JPEG in `b64_image` |
| `text2video` | Text prompt | MP4 in `b64_video` |
| `image2video` | Image in `input_reference` | MP4 in `b64_video` |
| `video2video` | Video in `input_reference`, or `transfer` controls | MP4 in `b64_video` |
| `forward_dynamics` | Image and `action_params.action` trajectory | MP4 in `b64_video` |
| `policy` | Image and `action_params` | MP4 and predicted `action` |
| `inverse_dynamics` | Video and `action_params` | MP4 and inferred `action` |

Media references accept base64, a base64 data URI, or a public HTTP(S) URL accessible to the service. Image inputs can be JPEG, PNG, or WebP. Returned videos use a VP9 track in an MP4 container; use a compatible player.

## API quickstart

The hosted API route is `POST /v1/cosmos/nvidia/cosmos3-nano` on `https://ai.api.nvidia.com`. Use the invocation URL and credentials supplied with your deployment. A directly deployed NIM serves `POST /v1/infer`.

With `API_KEY` set to your endpoint access key, request a short video:

```bash
curl --fail-with-body -sS -D headers.txt \
"https://ai.api.nvidia.com/v1/cosmos/nvidia/cosmos3-nano" \
-H "Authorization: Bearer $API_KEY" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-d '{
"model_mode": "text2video",
"prompt": "A robotic arm picks up a component on a workbench",
"resolution": "480_16_9",
"num_frames": 25,
"num_inference_steps": 35,
"fps": 24,
"seed": 42
}' -o response.json
```

After receiving the completed JSON result, decode the original MP4 bytes:

```bash
python3 -c "import json, base64; from pathlib import Path; response = json.loads(Path('response.json').read_text()); Path('output.mp4').write_bytes(base64.b64decode(response['b64_video'], validate=True))"
```

For image-to-video, set `model_mode` to `image2video` and supply the image in `input_reference`, for example `"data:image/jpeg;base64,<BASE64_IMAGE>"`, replacing the placeholder with encoded image bytes. Image generation instead uses `text2image` and returns `b64_image`.

## Generation settings

Defaults depend on the mode:

| Mode | Resolution | Frames | Steps | FPS |
| --- | --- | --- | --- | --- |
| `text2image` | `720_1_1` | 1 | 50 | Not applicable |
| `text2video`, `image2video`, ordinary `video2video` | `720` | 189 | 35 | 24 |
| Transfer, except WSM-only | `720` | 121 | 50 | 30 |
| WSM-only transfer | `720` | 101 | 50 | 10 |
| Action modes | `action_params.image_size`: `480` | `action_chunk_size + 1` | 30 | 10 |

`resolution` combines a tier (`256`, `480`, or `720`) with an optional aspect suffix: `16_9`, `1_1`, `9_16`, `4_3`, or `3_4`. A bare tier means `16_9`. These are predefined sizes: `480_16_9` is 832×480, `480_1_1` is 640×640, and `720_16_9` is 1280×720. Video `num_frames` accepts integers from 25 through 397, 297, or 197 for tiers `256`, `480`, or `720`, respectively.

See the API reference for sampling controls and numeric limits. Ordinary `video2video` also supports `condition_video_keep` (`first` or `last`) and `condition_frame_indexes_vision`: positions in the model's latent-frame sequence, not raw video-frame numbers.

## Spatial video controls

Use `video2video` with a `transfer` object containing one or more controls:

- `edge` and `blur`: supplied control videos or controls derived from an input video.
- `depth`: supplied depth video.
- `seg`: supplied segmentation video.
- `wsm`: supplied world-state-map video.

For supplied controls, use `{"video": "<VIDEO_REFERENCE>"}` as each control's value. Replace the placeholder with base64 media, a data URI, or a public video URL. Control videos must contain sufficient frames and match the requested aspect ratio within the API's tolerance.

For derived edges or blur, provide `input_reference` and set `edge` or `blur` to `true`. This example bounds the transfer chunk and output to 25 frames:

```json
{
"model_mode": "video2video",
"prompt": "A warehouse robot moves between shelving units",
"input_reference": "data:video/mp4;base64,<BASE64_VIDEO>",
"resolution": "480_16_9",
"num_frames": 25,
"transfer": {"edge": true, "num_video_frames_per_chunk": 25}
}
```

Replace `<BASE64_VIDEO>` with encoded video bytes. Do not combine `transfer` with ordinary V2V conditioning indexes or keep settings.

## Action workflows

Action requests require `action_params.domain_name` and `action_params.action_chunk_size`. Domains are `av`, `bridge_orig_lerobot`, `droid_lerobot`, and `umi`. The chunk size is a positive multiple of four; the output video has `action_chunk_size + 1` frames. Use `action_params.image_size` instead of ordinary `resolution` and `num_frames`.

`forward_dynamics` requires an action matrix with one row per action step: 9 values per row for `av`, or 10 for other domains. `policy` and `inverse_dynamics` return an `action` object with `data`, `shape`, `dtype`, `raw_action_dim`, `action_mode`, and `domain_id`. `data` is the numeric matrix; `shape` gives its dimensions, and `dtype` is `float32`.

## Long-running requests

Generation time and response size depend on resolution, frame count, sampling steps, controls, and service load. Start interactive workflows with a short 480p clip and measure the response time and quality your application needs. Use the timeout and result-retrieval contract provided with your endpoint; not all gateways expose the same asynchronous polling or download flow. Never forward your API bearer token to a signed result-download URL.

A client timeout does not establish that generation stopped. Retain the request identifier when provided, and resolve an unknown outcome before automatically submitting the same job again.

## Safety, limitations, and provenance

Input media undergoes mandatory screening for child sexual abuse material (CSAM), alongside content-safety guardrails. Rejected media or screening that cannot complete causes refusal without generated output. Invalid requests and safety refusals can both return HTTP 422; inspect the error message. Request parameters cannot disable screening or watermarking.

Returned images and videos carry a SynthID watermark. Numeric action arrays are not visually watermarked. Preserve the original JPEG or MP4 when checking provenance; re-encoding, resizing, and other editing may affect detection.

Generation can contain temporal inconsistencies, unstable motion, imprecise physical interactions, and action-state drift. The model is not a physics simulator: geometry, object permanence, contact, and physical laws are only approximated. Quality can degrade outside the training distribution. Generated outputs are not physically accurate simulation or safety-certified decisions. Robotics, autonomous systems, and other safety-critical applications require independent validation, system-level safety analysis, and appropriate constraints. The model is not designed or tested for uses where failure could cause injury, death, or catastrophic damage.

Users are responsible for input rights, outputs, and safe integration. Review the Model Card++ Explainability, Bias, Safety & Security, and Privacy subcards and the [base model card](https://huggingface.co/nvidia/Cosmos3-Nano) for further limitations and ethical considerations. Report security vulnerabilities or AI concerns through [NVIDIA Product Security](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Governing terms and support

This hosted trial is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). The published Cosmos3 model license is [OpenMDW-1.1](https://openmdw.ai/license/1-1/). The downloadable NIM container has separate [NGC governing terms](https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/cosmos3/-), including the NVIDIA Software License Agreement and Product-Specific Terms for NVIDIA AI Products. Consult the relevant terms for your use.

For deployment instructions, use the released NIM's NGC documentation. For enterprise assistance, see [NVIDIA AI Enterprise Support](https://www.nvidia.com/en-us/data-center/products/ai-enterprise-suite/support/).

## Specifications

- **Context Length:** 262,144 tokens
- **Parameters:** 15,750,057,456

## Capabilities

- **Function Calling:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing:  |  None
Measures taken to mitigate against unwanted bias:                                                   |  None

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Application & Domain:                                                                          |  World Generation
Model Type:                                                                                            |  World foundation model
Intended Users:                                                                                        |  Physical AI developers
Output:                                                                                                |  Videos
Describe how the model works:                                                                          |  Generates videos from text prompts and optional image conditioning.
Technical Limitations:                                                                                 |  The model may not follow the prompt or image input accurately and may generate visual artifacts.
Verified to have met prescribed NVIDIA quality standards:                                               |  Yes
Performance Metrics:                                                                                   |  Quantitative and qualitative evaluation
Potential Known Risks:                                                                                 |  The model can generate broad video content, including content that may be inaccurate, unsafe, offensive, or indecent.
Licensing:                                                                                             |  [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal information?                                                                          |  None Known
Protected class data used to create this model?                                                                                    |  None Known
Was consent obtained for any personal data used?                                                                                   |  None Known
How often is dataset reviewed?                                                                                                     |  Before Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Not Applicable
If personal data was collected for the development of the model, was it collected directly by NVIDIA?                              |  Not Applicable
If personal data was collected for the development of this AI model, was it minimized to only what was required?                   |  Not Applicable
Is there provenance for all datasets used in training?                                                                              |  Yes
Does data labeling comply with privacy laws?                                                                                       |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  Not Applicable

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  World Generation
Describe the life critical impact (if present).     |  None Known
Use Case Restrictions:                              |  See the published model license, [OpenMDW-1.1](https://openmdw.ai/license/1-1/), and the hosted service's [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf).
Model and dataset restrictions:                     |  The principle of least privilege is applied to dataset generation and model development. Restrictions enforce dataset access during training and dataset license constraints are adhered to.

## Prototype

```bash
curl --fail-with-body --silent --show-error \
--request POST \
--url https://ai.api.nvidia.com/v1/cosmos/nvidia/cosmos3-nano \
--header "Authorization: Bearer $NVIDIA_API_KEY" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-binary @- <<'JSON'
{"messages":[{"role":"user","content":""}]}
JSON
```