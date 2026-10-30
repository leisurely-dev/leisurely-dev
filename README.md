<div align="center">
<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/hero.svg" width="100%" alt="leisurely, agents, inference, evals" />
</div>

<br />

<div align="center">
<a href="https://github.com/leisurely-dev"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=21&pause=900&color=00C6FF&center=true&vCenter=true&width=640&lines=keep+the+loop+small;measure+before+you+ship;delete+half+of+it" alt="typing" /></a>
</div>

<br />

I build small systems around language models and try to keep them boring enough to debug. What I actually care about sits in the unglamorous middle: how a tool call fails at 3am, what an eval is quietly not measuring, why the p99 got worse after a refactor that touched nothing.

Most of my time goes into agent loops with tight retry boundaries, inference on hardware I own instead of renting, and eval suites small enough to read in one sitting.

Off the clock it is the same instinct pointed at my own rack: Proxmox backups I have actually restored from, an OpenWrt box doing more than it should, and the occasional postmortem of a server that picked a bad hour to fall over. Some of that ends up in [forensics-notes](https://github.com/leisurely-dev/forensics-notes).

<div align="center">
<br />
<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/divider.svg" width="100%" height="2" />
</div>

### What I'm working on

| Area | What it covers |
| :--- | :--- |
| **Agents** | Tool-use loops, explicit state machines instead of free-form ReAct, hard caps on steps and spend |
| **Inference** | Quantized local serving, batching, speculative decoding, KV cache pressure |
| **Evals** | Hand-written suites that catch regressions instead of leaderboard cosplay |
| **Retrieval** | Chunking strategies, hybrid search, reranker latency budgets |

<div align="center">
<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/loop.svg" width="820" alt="agent loop" />
</div>

<details>
<summary><b>things I keep re-learning the hard way</b></summary>

<br />

- A prompt is a program. It needs version control, tests, and someone to review the diff.
- Most reports of "the model got worse" trace back to a tokenizer or chat template change upstream.
- Retries without idempotency just multiply the bill.
- If an eval can't fail, it isn't an eval.
- The fastest model is the one you didn't call.

</details>

<div align="center">
<br />
<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/divider.svg" width="100%" height="2" />
</div>

### Toolbox

<div align="center">
<img src="https://skillicons.dev/icons?i=py,pytorch,ts,fastapi,docker,linux,postgres,redis,git,bash&theme=dark&perline=10" />
<br />
<img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=000" /> <img src="https://img.shields.io/badge/llama.cpp-2b2b2b?style=flat-square&logo=llama&logoColor=fff" /> <img src="https://img.shields.io/badge/vLLM-1a1a1a?style=flat-square&logo=v&logoColor=fff" /> <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=fff" /> <img src="https://img.shields.io/badge/Qdrant-DC244C?style=flat-square&logo=qdrant&logoColor=fff" /> <img src="https://img.shields.io/badge/nginx-009639?style=flat-square&logo=nginx&logoColor=fff" />
</div>

<div align="center">
<br />
<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/divider.svg" width="100%" height="2" />
</div>

### Constantly open in a tab

- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) is still the best place to see what inference actually costs
- [vllm-project/vllm](https://github.com/vllm-project/vllm) for paged attention, and the scheduler bugs that come with it
- [huggingface/transformers](https://github.com/huggingface/transformers) mostly to check what the tokenizer just did to my input
- [BerriAI/litellm](https://github.com/BerriAI/litellm) one interface, twelve providers, twelve sets of quirks
- [ollama/ollama](https://github.com/ollama/ollama) the fastest way to get something running locally before I overthink it

<div align="center">
<br />
<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/divider.svg" width="100%" height="2" />
</div>

### Lately

<div align="center">
<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/activity.svg" width="880" alt="recent activity" />
</div>

<div align="center">
<br />
<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/divider.svg" width="100%" height="2" />
</div>

### Elsewhere

<div align="center">
<a href="mailto:winston_cn@yeah.net"><img src="https://img.shields.io/badge/email-0b0f14?style=for-the-badge&logo=maildotru&logoColor=00c6ff" /></a> <a href="https://github.com/leisurely-dev?tab=repositories"><img src="https://img.shields.io/badge/repos-0b0f14?style=for-the-badge&logo=github&logoColor=00c6ff" /></a> <a href="https://github.com/leisurely-dev?tab=stars"><img src="https://img.shields.io/badge/starred-0b0f14?style=for-the-badge&logo=githubsponsors&logoColor=00c6ff" /></a>
<br /><br />
<img src="https://komarev.com/ghpvc/?username=leisurely-dev&color=00c6ff&style=flat-square&label=visitors" />
</div>

<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/footer.svg" width="100%" />
