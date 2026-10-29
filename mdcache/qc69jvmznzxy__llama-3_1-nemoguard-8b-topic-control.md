---
title: "llama-3.1-nemoguard-8b-topic-control"
publisher: "nvidia"
type: "endpoint"
updated: "2025-03-25T01:16:40.059Z"
description: "Topic control model to keep conversations focused on approved topics, avoiding inappropriate content."
canonical: "https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-topic-control"
---

# Model Overview
## Description:
This open Nemotron safety model, *Llama 3.1 NemoGuard 8B Topic Control*, can be used for topical and dialogue moderation of user prompts in human-assistant interactions being designed for task-oriented dialogue agents and custom policy-based moderation. 
Given a system instruction (also called topical instruction, i.e. specifying which topics are allowed and disallowed) and a conversation history ending with the last user prompt, the model returns a binary response that flags if the user message respects the system instruction, (i.e. message is on-topic or a distractor/off-topic). 
The base large language model (LLM) is the multilingual [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) model from Meta. Llama 3.1 NemoGuard 8B TopicControl is LoRa-tuned on a topic-following dataset generated synthetically with [Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1).
This model is ready for commercial use.  <br>

This model is supported in the open NVIDIA NeMo Guardrails library, designed to simplify scalable AI guardrail orchestration for safeguarding agentic AI applications.

### License/Terms of Use:

Governing NVIDIA Model Hosting Terms (Cloud API) GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Community License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). Additional Information: [Llama 3.1 Community License Agreement](https://www.llama.com/llama3_1/license/). Built with Llama.

## Reference(s):
Related paper: 
```bibtex
@article{sreedhar2024canttalkaboutthis,
title={CantTalkAboutThis: Aligning Language Models to Stay on Topic in Dialogues},
author={Sreedhar, Makesh Narsimhan and Rebedea, Traian and Ghosh, Shaona and Zeng, Jiaqi and Parisien, Christopher},
journal={arXiv preprint arXiv:2404.03820},
year={2024}
}
```
<br>

## Model Architecture:

**Architecture Type:** Transformer  <br>
**Network Architecture:** The base model architecture is based on the Llama-3.1-8B-Instruct model from Meta ([Model Card](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_1/)).
We perform Parameter Efficient FineTuning (PEFT) over the base model using the following network architecture parameters:
- Rank: 8
- Alpha: 32
- Targeted low rank adaptation modules: 'k_proj', 'q_proj', 'v_proj', 'o_proj', 'up_proj', 'down_proj', 'gate_proj'. <br>

**Training Method:**

The training method for **Llama 3.1 NemoGuard 8B TopicControl** involves the following concepts:
- A system instruction which acts like a topical instruction with the rules that define the context of the user-assistant interaction, i.e. topics allowed or disallowed by the current task-oriented scenario, conversation style and tone, conversation flows.
- Any user message in the conversation that respects the topical instruction is considered on-topic, while a user message that contradicts at least one of the rules is a distractor or off-topic.
- A synthetic generated dataset, called CantTalkAboutThis-Mixtral-1.0, of approximately 1,000 multi-turn conversations is used to instruction-tune the base model. Each conversation has a specific topical instruction from various broad domains (i.e. customer support, travel, legal) and contains an entire conversation which is on-topic, together with several distractor user messages replacing some of the on-topic ones at specific key points in the conversation. 
- The model is instruction-tuned to detect whether a user message is either on-topic or a distractor given the topical instruction for the current conversation, with the LLM behaving as a classifier.

## Input:
**Input Type(s):** Text <br>
**Input Format(s):** String <br>
**Input Parameters:** 1D (One-Dimensional) List: System prompt with topical instructions, followed by a conversation structured as a list of user and assistant messages. <br>
**Other Properties Related to Input:** The conversation should end with a user message that is considered for topical moderation given the topical instruction and the context of the entire conversation (previous user and assistant turns). The input format for the system prompt and the conversation respects the [OpenAI Chat specification](https://platform.openai.com/docs/guides/text-generation) widely adopted in the industry including by [NVIDIA AI API](https://build.nvidia.com/).

Sample input:
```json
// User-LLM conversations in the industry-standard payload format for LLM systems:
[
{
"role": "system",
"content": "In the next conversation always use a polite tone and do not engage in any talk about travelling and touristic destinations",
},
{
"role": "user",
"content": "Hi there!",
},
{
"role": "assistant",
"content": "Hello! How can I help today?",
},
{
"role": "user",
"content": "Do you know which is the most popular beach in Barcelona?",
},
]
```
<br>

## Output:

**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** 1D (One-Dimensional) <br>
**Other Properties Related to Output:** The response is a binary string label determining if the last user turn in the input conversation respects the topical instruction. The label options are either *"on-topic"* or *"off-topic"*. <br>

### Example Model Input/Output:
**Input**
```json
// User-LLM conversations in the industry-standard payload format for LLM systems:
[
{
"role": "system",
"content": "In the next conversation always use a polite tone and do not engage in any talk about travelling and touristic destinations",
},
{
"role": "user",
"content": "Hi there!",
},
{
"role": "assistant",
"content": "Hello! How can I help today?",
},
{
"role": "user",
"content": "Do you know which is the most popular beach in Barcelona?",
},
]
```
**Output (Model Response)**
```string
off-topic
```
## Software Integration:
**Runtime Engine(s):** PyTorch <br>
**Libraries:**  Meta's [llama-recipes](https://github.com/meta-llama/llama-recipes), HuggingFace [transformers](https://github.com/huggingface/transformers) library, HuggingFace [peft](https://github.com/huggingface/peft) library <br>
**Supported Hardware Platform(s):** NVIDIA Ampere (A100 80GB, A100 40GB) <br>
**Preferred/Supported Operating System(s):** Linux (Ubuntu) <br>

## Model Version(s): 
Llama 3.1 NemoGuard 8B TopicControl  <br>

# Training, Testing, and Evaluation Datasets:

## Training Dataset:

**Link:** [CantTalkABoutThis](https://github.com/makeshn/topic_following) dataset<br>
**Data Collection Method by dataset**: Synthetic <br>
**Labeling Method by dataset**: Synthetic <br>
**Properties:** [CantTalkABoutThis topic-following dataset](https://github.com/makeshn/topic_following) contains 1080 multi-turn conversations that are on-topic using 540 different topical instructions from various domains. For each on-topic conversation, we also generate off-topic/distractor turns at specific points in the conversation (about 4 distractors per conversation). <br>

## Testing Dataset:
The performance of the model is tested on a smaller, human-annotated subset of the [CantTalkABoutThis topic-following dataset](https://github.com/makeshn/topic_following) synthetically created test set. The test set contains conversations on a different domain (*banking*) that does not appear in training or evaluation sets. While on-topic conversations are samples similar to the training dataset, the distractors are human annotated by expert annotators.

**Link:** [CantTalkABoutThis topic-following dataset](https://github.com/makeshn/topic_following)<br>
**Data Collection Method by dataset**: Hybrid: Synthetic, Human <br>
**Labeling Method by dataset**: Hybrid: Synthetic, Human <br>
**Properties:** We select 20 random dialogues from the synthetic test domain and manually ask two experts in dialogue systems to create five distractors per conversation. Thus, we also provide a small human annotated test set that is both more challenging and reflective of realistic scenarios. The test set contains 100 human annotated distractors and the reminder of the on-topic turns, having 11% of turns as distractors/off-topic. <br>

## Evaluation Dataset:
The evaluation set is similar to the training dataset, synthetically generated on-topic conversations and distractors, but in the *travel* domain (not part of training set). <br>
**Link:** [CantTalkABoutThis](https://github.com/makeshn/topic_following) evaluation set <br>
**Data Collection Method by dataset**: Synthetic <br>
**Labeling Method by dataset**: Synthetic <br>
**Properties:** We generate 20 multi-turn conversations on 10 different scenarios in the travel domain, each conversation having about 20 turns. <br>

## Inference:
**Engine:** TensorRT-LLM available via [NVIDIA NIMs](https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-3.1-nemoguard-8b-topic-control) available on NGC. <br>
**Test Hardware:** A100 80GB  <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  
For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards.  
Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Specifications

- **Context Length:** 131,072 tokens
- **Parameters:** 8,030,261,248
- **Input:** Text
- **Output:** Text

## Capabilities

- **Function Calling:** Not supported
- **Structured Output:** Not supported
- **Reasoning:** Not supported

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing:  |  Not Applicable
Measures taken to mitigate against unwanted bias:                                                   |  None

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Application & Domain:                                                                   	   |  Dialogue Agents and Guardrails
Model Type:                                                                                            |  Transformer
Intended Users:                                                                                        |  This model is intended for developers building task-oriented dialogue assistants that want to specify the dialogue policy in natural language - e.g. allowed topics, disallowed topics, conversation flows, conversation style / tone. The model is also useful as a topical guardrail in NeMo Guardrails. 
Output:                                                                                                |  Text - Binary label determining if the last user turn in the input conversation respects the topical instruction. The label options are either "on-topic" or "off-topic".
Describe how the model works:                                                                          |  The model receives as input the dialogue policy and the current conversation ending with the last user turn in the prompt of a LLM (Llama3.1-8B-Instruct). A binary decision is returned, specifying whether the input is on-topic or not.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Not Applicable
Technical Limitations:                                                                                 |  The model was trained on 9 domains, including finance, health, education, taxes, real estate, computer troubleshooting, travel, banking, and legal. We have tested out-of-domain performance for the model and our results suggest strong generalization in other domains as well. However, we recommend a thorough testing when using the model with prompts that are outside of these 9 domain areas, as the model may provide a deliver a lower performance.
Verified to have met prescribed NVIDIA quality standards:  |  Yes
Performance Metrics:                                                                                   |  F1, Accuracy
Potential Known Risks:                                                                                 |  Potential risks include the dialogue agent engaging in user content that is not on-topic. 
Licensing:                                                                                             | Governing NVIDIA Model Hosting Terms (Cloud API) GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Community License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). Additional Information: [Llama 3.1 Community License Agreement](https://www.llama.com/llama3_1/license/). Built with Llama.

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?                                                     |  None
Personal data used to create this model?                                                                                       |  None
Was consent obtained for any personal data used?                                                                                             |  Not Applicable
How often is dataset reviewed?                                                                                                     |  Before Every Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Not Applicable
If personal data was collected for the development of the model, was it collected directly by NVIDIA?                                            |  Not Applicable
If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  Not Applicable
If personal data was collected for the development of this AI model, was it minimized to only what was required?                                 |  Not Applicable
Is there provenance for all datasets used in training?                                                                                |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  Yes

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  Dialogue agents for topic / dialogue moderation
Describe the life critical impact (if present).   |  Not Applicable
Use Case Restrictions:                              |  Should not be used for any use case other than text-based topic and dialogue moderation in task oriented dialogue agents.
Model and dataset restrictions:            |  Abide by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Community License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-community-models-license/). Additional Information: [Llama 3.1 Community License Agreement](https://www.llama.com/llama3_1/license/). Built with Llama.

## Prototype

```python
from openai import OpenAI

client = OpenAI(
base_url = "https://integrate.api.nvidia.com/v1",
api_key = "$NVIDIA_API_KEY"
)

completion = client.chat.completions.create(
model="",
messages=[{"role":"user","content":""}],
temperature=,
top_p=,
max_tokens=
)
print(completion.choices[0].message)
```

```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
apiKey: '$NVIDIA_API_KEY',
baseURL: 'https://integrate.api.nvidia.com/v1',
})

async function main() {
const completion = await openai.chat.completions.create({
model: "",
messages: [{"role":"user","content":""}],
temperature: ,
top_p: ,
max_tokens: ,
})
process.stdout.write(completion.choices[0]?.message?.content);
}

main();
```

```bash
curl https://integrate.api.nvidia.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-d '{
"model": "nvidia/llama-3.1-nemoguard-8b-topic-control",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens":              
}'
```