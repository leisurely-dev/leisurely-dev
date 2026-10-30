<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b0f14,40:14304a,100:00c6ff&height=210&section=header&text=leisurely&fontSize=72&fontColor=ffffff&fontAlignY=36&desc=agents%20%C2%B7%20inference%20%C2%B7%20evals&descAlign=50&descAlignY=58&descSize=19&animation=fadeIn" width="100%" />

<a href="https://github.com/leisurely-dev">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=21&pause=900&color=00C6FF&center=true&vCenter=true&width=640&lines=keep+the+loop+small;measure+before+you+ship;delete+half+of+it" alt="typing" />
</a>

</div>

I build small systems around language models and try to keep them boring enough to debug. Most of what I care about sits in the unglamorous middle: how a tool call actually fails, what an eval is quietly not measuring, why the p99 got worse after a harmless refactor.

Lately that means agent loops with tight retry boundaries, inference on hardware I actually own, and eval harnesses that fit on one screen.

<div align="center">

<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/divider.svg" width="100%" height="2" />

</div>

### What I'm working on

| | |
|---|---|
| **Agents** | Tool-use loops, state machines instead of free-form ReAct, hard caps on steps and spend |
| **Inference** | Quantized local serving, batching, speculative decoding, KV cache pressure |
| **Evals** | Small hand-written suites that catch regressions, not leaderboard cosplay |
| **Retrieval** | Chunking strategies, hybrid search, reranker latency budgets |

<details>
<summary><b>things I keep re-learning the hard way</b></summary>

<br />

- A prompt is a program. It needs version control, tests, and a diff review.
- Most reports of "the model got worse" trace back to a tokenizer or template change upstream.
- Retries without idempotency just multiply the bill.
- If an eval can't fail, it isn't an eval.
- The fastest model is the one you didn't call.

</details>

<div align="center">

<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/divider.svg" width="100%" height="2" />

</div>

### Toolbox

<div align="center">

<img src="https://skillicons.dev/icons?i=py,pytorch,ts,fastapi,docker,linux,postgres,redis,git,bash&theme=dark&perline=10" />

<br /><br />

<img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=000" />
<img src="https://img.shields.io/badge/vLLM-1a1a1a?style=flat-square&logo=v&logoColor=fff" />
<img src="https://img.shields.io/badge/llama.cpp-2b2b2b?style=flat-square&logo=llama&logoColor=fff" />
<img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=fff" />
<img src="https://img.shields.io/badge/Qdrant-DC244C?style=flat-square&logo=qdrant&logoColor=fff" />

</div>

<div align="center">

<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/divider.svg" width="100%" height="2" />

</div>

### Numbers

<div align="center">

<img height="160" src="https://github-readme-stats.vercel.app/api?username=leisurely-dev&show_icons=true&hide_border=true&bg_color=0b0f14&title_color=00c6ff&icon_color=00c6ff&text_color=c9d1d9&include_all_commits=true&count_private=true" />
<img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=leisurely-dev&layout=compact&hide_border=true&bg_color=0b0f14&title_color=00c6ff&text_color=c9d1d9&langs_count=8" />

<br />

<img src="https://github-readme-streak-stats.herokuapp.com/?user=leisurely-dev&hide_border=true&background=0b0f14&stroke=14304a&ring=00c6ff&fire=00c6ff&currStreakLabel=00c6ff&sideLabels=c9d1d9&dates=8b949e" />

<br />

<img src="https://github-readme-activity-graph.vercel.app/graph?username=leisurely-dev&bg_color=0b0f14&color=c9d1d9&line=00c6ff&point=ffffff&area=true&hide_border=true&custom_title=Contribution%20graph" width="96%" />

</div>

<div align="center">

<img src="https://raw.githubusercontent.com/leisurely-dev/leisurely-dev/main/assets/divider.svg" width="100%" height="2" />

</div>

### Elsewhere

<div align="center">

<a href="mailto:winston_cn@yeah.net"><img src="https://img.shields.io/badge/email-0b0f14?style=for-the-badge&logo=maildotru&logoColor=00c6ff" /></a>
<a href="https://github.com/leisurely-dev?tab=repositories"><img src="https://img.shields.io/badge/repos-0b0f14?style=for-the-badge&logo=github&logoColor=00c6ff" /></a>
<a href="https://github.com/leisurely-dev?tab=stars"><img src="https://img.shields.io/badge/stars-0b0f14?style=for-the-badge&logo=githubsponsors&logoColor=00c6ff" /></a>

<br /><br />

<img src="https://komarev.com/ghpvc/?username=leisurely-dev&color=00c6ff&style=flat-square&label=visitors" />

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00c6ff,60:14304a,100:0b0f14&height=120&section=footer" width="100%" />
