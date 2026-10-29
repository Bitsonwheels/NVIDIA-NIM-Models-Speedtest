---
title: "Video Super Resolution NIM"
publisher: "nvidia"
type: "endpoint"
updated: "2026-07-22T21:24:15.027Z"
description: "Upscale encoded or ST 2110 video to higher resolutions with NVIDIA Video Super Resolution."
canonical: "https://build.nvidia.com/nvidia/vsr"
---

# Video Super Resolution NIM

NVIDIA Video Super Resolution (VSR) NIM is an AI inference microservice for
upscaling video to higher resolutions. It supports two runtime modes with
separate deployment artifacts:

- **ST 2110 video workflows:** SMPTE ST 2110-20 uncompressed video workflows on
NVIDIA Holoscan for Media.
- **Compressed video workflows:** gRPC, RTP/UDP, and Cloud File workflows for
encoded video, controlled through the VSR gRPC API.

Use ST 2110 video workflows when deploying VSR into a Holoscan for Media
pipeline for live SMPTE ST 2110-20 uncompressed video. Use compressed video
workflows when running the NIM as a container and sending encoded-video requests
with gRPC, RTP/UDP, or Cloud File inputs and outputs.

For details about the model used inside this NIM, see the underlying NVIDIA
Video Super Resolution model card. The model card covers the video
post-processing model used for artifact removal, resolution upscaling, and
visual quality enhancement:

[NVIDIA Video Super Resolution model card](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/maxine/models/nvvfxvideosuperres?version=1.2.0.0_lib_linux)

For deployment and API details, see the
[Video Super Resolution NIM documentation](https://docs.nvidia.com/nim/maxine/vsr/latest/index.html).

## Capabilities

- **Function Calling:** Not supported