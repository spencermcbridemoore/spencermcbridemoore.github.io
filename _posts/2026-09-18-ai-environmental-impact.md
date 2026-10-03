---
title: "The Environmental Impact of AI"
author: Spencer Moore
date: 2026-09-18
categories: [machine learning, LLM]
tags: [environmental impact, energy, water, data centres, AI-PER]
description: "Slides from my AI-PER community meeting talk: the one objection you can put numbers on — and why the numbers are harder than they look."
image: /assets/img/posts/2026-09-18-ai-environmental-impact-29.png
---

<style>
  /* Tables in this post hold sentences, not short values, so let the cells wrap. */
  .content .table-wrapper > table th,
  .content .table-wrapper > table td { white-space: normal; vertical-align: top; min-width: 7rem; }

  /* Each slide sits beside its own text; the two stack when the column is narrow. */
  .sl { container-type: inline-size; display: flex; flex-wrap: wrap; align-items: flex-start; gap: 0.75rem 1.5rem; margin: 1rem 0 1.5rem; }
  .sl > .sl-fig, .sl > .sl-txt { flex: 1 1 100%; min-width: 0; }
  .sl-fig > p { position: relative; margin: 0; line-height: 0; }
  .content .sl-fig > p > a.popup { display: block; margin: 0; }
  .sl-fig img { display: block; width: 100%; height: auto; aspect-ratio: 16 / 9; border-radius: 2px; box-shadow: 0 0 0 1px rgba(128, 128, 128, 0.35); }
  .sl-txt > :first-child { margin-top: 0; }
  .sl-txt > :last-child { margin-bottom: 0; }
  @container (min-width: 40rem) {
    .sl > .sl-fig { flex: 0 0 46%; position: sticky; top: 1rem; }
    .sl > .sl-txt { flex: 1 1 0; }
    .sl-txt .table-wrapper > table th,
    .sl-txt .table-wrapper > table td { min-width: 5rem; padding: 0.35rem 0.4rem; font-size: 0.9em; }
    /* A slide whose text is a wide table: the slide stays pinned on top and the table runs full width beneath it. */
    .sl.sl-stack > .sl-fig { flex: 0 0 100%; top: 0; z-index: 2; padding: 0.5rem 0 0.75rem; background: var(--main-bg, #fff); }
    .sl.sl-stack > .sl-fig > p { max-width: 30rem; margin: 0 auto; }
    .sl.sl-stack > .sl-txt { flex: 0 0 100%; }
    .sl.sl-stack .sl-txt .table-wrapper > table th,
    .sl.sl-stack .sl-txt .table-wrapper > table td { min-width: 7rem; padding: 0.5rem 0.75rem; font-size: 1em; }
  }

  /* Linked highlight: a piece of text and its place on the slide light up together. */
  .sl-r { position: absolute; pointer-events: none; border-radius: 2px; opacity: 0; background: rgba(255, 179, 0, 0.3); outline: 2px solid rgba(255, 145, 0, 0.95); transition: opacity 0.12s; }
  .sl-r.on { opacity: 1; }
  .sl-txt [data-k], h2[data-k] > span { border-radius: 2px; transition: background-color 0.12s, box-shadow 0.12s; }
  .sl-txt [data-k].on, h2[data-k].on > span { background-color: rgba(255, 179, 0, 0.28); box-shadow: 0 0 0 0.25rem rgba(255, 179, 0, 0.28); }
  .sl-txt th[data-k].on, .sl-txt td[data-k].on { box-shadow: none; }
</style>

# The Environmental Impact of AI

*The one objection you can put numbers on — and why the numbers are harder than they look.*

**Spencer McBride Day Moore**  
Department of Physics, University of Central Florida · advised by Zhongzhou Chen

**AI-PER Community Meeting · 18 September 2026**

> These are the slides from my talk at the AI-PER (artificial intelligence in physics education research) community meeting on 18 September 2026. Beside each slide (below it on a phone) is that slide's own text, transcribed exactly, so it can be read on a phone and searched. Point at a line of text or at part of a slide, and the matching part of the other is highlighted. Click a slide to see it full size. The slides reflect what had been published as of mid-September 2026.
>
> Each slide carries the short source line it had in the talk. A few slides mention a source list, and some carry codes like P12; both refer to a full source table that is still being checked, reference by reference. I'll link it here once that check is done.
{: .prompt-info }

---

## Spencer McBride Day Moore
{: id="spencer-mcbride-day-moore" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 2: background — education, prior research and current work, with a diagram of UCN Area B at Los Alamos and a heatmap of weight change by layer](/assets/img/posts/2026-09-18-ai-environmental-impact-02.png)<span class="sl-r" data-k="t" style="left:4.22%;top:8.43%;width:43.85%;height:6.57%"></span><span class="sl-r" data-k="1" style="left:4.17%;top:15.93%;width:50.52%;height:6.11%"></span><span class="sl-r" data-k="1" style="left:4.22%;top:20.74%;width:22.19%;height:4.17%"></span><span class="sl-r" data-k="2" style="left:4.22%;top:24.72%;width:6.82%;height:2.68%"></span><span class="sl-r" data-k="3" style="left:8.65%;top:28.06%;width:27.6%;height:2.96%"></span><span class="sl-r" data-k="4" style="left:8.59%;top:31.2%;width:27.81%;height:2.96%"></span><span class="sl-r" data-k="5" style="left:8.65%;top:34.35%;width:25%;height:2.96%"></span><span class="sl-r" data-k="6" style="left:4.22%;top:40.37%;width:9.58%;height:2.78%"></span><span class="sl-r" data-k="7" style="left:8.65%;top:43.8%;width:46.25%;height:5.56%"></span><span class="sl-r" data-k="8" style="left:8.59%;top:49.44%;width:51.35%;height:5.56%"></span><span class="sl-r" data-k="9" style="left:8.65%;top:55.18%;width:42.92%;height:2.96%"></span><span class="sl-r" data-k="10" style="left:4.17%;top:64.44%;width:5.57%;height:2.78%"></span><span class="sl-r" data-k="11" style="left:8.65%;top:67.78%;width:46.61%;height:2.96%"></span><span class="sl-r" data-k="12" style="left:8.65%;top:70.93%;width:49.48%;height:2.96%"></span><span class="sl-r" data-k="13" style="left:8.65%;top:74.07%;width:39.64%;height:2.96%"></span><span class="sl-r" data-k="14" style="left:5.78%;top:84.81%;width:42.86%;height:3.15%"></span><span class="sl-r" data-k="15" style="left:61.51%;top:55.09%;width:33.54%;height:4.91%"></span><span class="sl-r" data-k="15" style="left:66.09%;top:89.63%;width:24.38%;height:2.69%"></span>
</div>
<div class="sl-txt" markdown="1">

Second-year doctoral student in physics, University of Central Florida · advised by Zhongzhou Chen  
Earlier work published as S D Moore
{: data-k="1"}

**Education**
{: data-k="2"}

- {: data-k="3"} B.S. Physics, North Carolina State University, 2017
- {: data-k="4"} M.S. Physics, North Carolina State University, 2019
- {: data-k="5"} Graduate-level computer science coursework

**Prior research**
{: data-k="6"}

- {: data-k="7"} GPU programming in CUDA since 2014 — neutron-transport integrator ported to GPU; Lindbladian Runge–Kutta
- {: data-k="8"} Ultracold Neutron Asymmetry (UCNA) collaboration — beta-decay asymmetry and dark-matter constraints; six peer-reviewed papers
- {: data-k="9"} Experimental atomic, molecular and optical physics — ColdQuanta / Infleqtion

**Current**
{: data-k="10"}

- {: data-k="11"} Physics education research and mechanistic interpretability of large language models
- {: data-k="12"} Numerical LLM: Ex. SVD of instruct-minus-base weight deltas across Qwen 2.5, 0.5B to 14B
- {: data-k="13"} Reviewer, Association for Computational Linguistics (ACL) Rolling Review

> Work in LLM has relevance but more so work in CUDA GPU programming.
> {: data-k="14"}

*Image captions: UCN Area B, Los Alamos Neutron Science Center (LANSCE), Los Alamos National Laboratory · Weight change by layer, base vs. instruction-tuned*
{: .small data-k="15" }

</div>
</div>

---

## Educational Work: Interactive Quantum Computing Game “Entangled States”
{: id="educational-work-interactive-quantum-computing-game-entangled-states" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 3: the Entangled States quantum-circuit game from the IBM Quantum Hackathon 2020, and the ESTELA workshop presentation](/assets/img/posts/2026-09-18-ai-environmental-impact-03.png)<span class="sl-r" data-k="t" style="left:4.32%;top:9.44%;width:21.15%;height:4.26%"></span><span class="sl-r" data-k="t" style="left:4.32%;top:14.63%;width:66.67%;height:5.09%"></span><span class="sl-r" data-k="1" style="left:4.22%;top:25.56%;width:21.67%;height:3.33%"></span><span class="sl-r" data-k="1" style="left:4.17%;top:27.68%;width:9.58%;height:4.35%"></span><span class="sl-r" data-k="2" style="left:4.12%;top:37.96%;width:27.97%;height:11.85%"></span><span class="sl-r" data-k="3" style="left:5.62%;top:55.74%;width:24.63%;height:6.11%"></span><span class="sl-r" data-k="4" style="left:5.73%;top:64.26%;width:20.89%;height:3.33%"></span><span class="sl-r" data-k="5" style="left:5.73%;top:70%;width:25.42%;height:5.09%"></span><span class="sl-r" data-k="6" style="left:5.62%;top:77.59%;width:21.88%;height:5.74%"></span>
</div>
<div class="sl-txt" markdown="1">

**IBM Quantum Hackathon, 2020**  
**Second place**
{: data-k="1"}

A sandbox for building quantum circuits. Place a gate on a wire and the state vector on the left redraws — all eight amplitudes, live.
{: data-k="2"}

> The other half: tools that make an abstraction something you can push on.
> {: data-k="3"}
>
> **ESTELA Summer Workshop 2026**
> {: data-k="4"}
>
> Empowering STEM Educators and Learners with AI · UCF and Valencia College
> {: data-k="5"}
>
> A presentation on building interactive coursework tools with AI, on the fly.
> {: data-k="6"}

</div>
</div>

{% include embed/video.html src='/assets/img/posts/2026-09-18-ai-environmental-impact-03.mp4' poster='/assets/img/posts/2026-09-18-ai-environmental-impact-03-poster.png' title='Screen capture · no audio' loop=true muted=true %}

---

## What do students find uncomfortable about using generative AI?
{: id="what-do-students-find-uncomfortable-about-using-generative-ai" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 4: three cards — Provenance, Substitution, Environment — listing what students find uncomfortable about generative AI](/assets/img/posts/2026-09-18-ai-environmental-impact-04.png)<span class="sl-r" data-k="t" style="left:4.12%;top:12.04%;width:91.2%;height:6.02%"></span><span class="sl-r" data-k="1" style="left:5.88%;top:29.44%;width:10.31%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:37.03%;top:29.44%;width:10.63%;height:3.33%"></span><span class="sl-r" data-k="3" style="left:68.33%;top:29.44%;width:11.25%;height:3.33%"></span><span class="sl-r" data-k="4" style="left:5.83%;top:34.35%;width:20.78%;height:3.06%"></span><span class="sl-r" data-k="5" style="left:37.03%;top:34.35%;width:19.95%;height:3.06%"></span><span class="sl-r" data-k="6" style="left:68.23%;top:34.35%;width:21.98%;height:3.06%"></span><span class="sl-r" data-k="7" style="left:8.91%;top:40.46%;width:7.66%;height:2.96%"></span><span class="sl-r" data-k="8" style="left:8.91%;top:43.43%;width:4.95%;height:2.96%"></span><span class="sl-r" data-k="9" style="left:8.96%;top:46.39%;width:3.7%;height:2.5%"></span><span class="sl-r" data-k="10" style="left:8.91%;top:49.26%;width:3.59%;height:2.59%"></span><span class="sl-r" data-k="11" style="left:40.16%;top:40.46%;width:14.74%;height:2.96%"></span><span class="sl-r" data-k="12" style="left:40.16%;top:43.43%;width:22.24%;height:2.59%"></span><span class="sl-r" data-k="13" style="left:40.1%;top:46.39%;width:8.75%;height:2.96%"></span><span class="sl-r" data-k="14" style="left:71.35%;top:40.83%;width:4.32%;height:2.59%"></span><span class="sl-r" data-k="15" style="left:71.35%;top:43.43%;width:9.48%;height:2.96%"></span><span class="sl-r" data-k="16" style="left:71.3%;top:46.57%;width:5.99%;height:2.41%"></span><span class="sl-r" data-k="17" style="left:71.35%;top:49.26%;width:5.42%;height:2.96%"></span><span class="sl-r" data-k="18" style="left:4.12%;top:61.3%;width:24.53%;height:3.24%"></span><span class="sl-r" data-k="19" style="left:7.87%;top:75.65%;width:84.17%;height:12.13%"></span>
</div>
<div class="sl-txt" markdown="1">

| Provenance | Substitution | Environment |
|---|---|---|
| *loss of attribution for original work* | *replacement and its consequences* | *sudden industrial scaling and its costs* |
| <span data-k="7">artist images</span><br><span data-k="8">writings</span><br><span data-k="9">music</span><br><span data-k="10">video</span> | <span data-k="11">social media manipulation</span><br><span data-k="12">artists and content-creators out of work</span><br><span data-k="13">AI content slop</span> | <span data-k="14">energy</span><br><span data-k="15">carbon footprint</span><br><span data-k="16">water use</span><br><span data-k="17">pollution</span> |
{: data-keys="1 2 3 4 5 6 - - -"}

*My split. It may not be the right three.*
{: data-k="18"}

**The third one is the only one I can put numbers on… which is handy since that is what the presentation is on!**
{: data-k="19"}

</div>
</div>

---

## AI's environmental footprint
{: id="ais-environmental-footprint" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 5: AI's environmental footprint — what was measured, what was modelled, and what nobody knows](/assets/img/posts/2026-09-18-ai-environmental-impact-05.png)<span class="sl-r" data-k="t" style="left:5.57%;top:8.61%;width:51.88%;height:7.41%"></span><span class="sl-r" data-k="1" style="left:5.62%;top:18.15%;width:53.54%;height:4.26%"></span><span class="sl-r" data-k="2" style="left:7.5%;top:26.85%;width:19.43%;height:2.22%"></span><span class="sl-r" data-k="3" style="left:7.5%;top:30.37%;width:29.27%;height:3.89%"></span><span class="sl-r" data-k="4" style="left:7.5%;top:35.74%;width:45.94%;height:2.68%"></span><span class="sl-r" data-k="5" style="left:5.62%;top:43.52%;width:21.15%;height:2.78%"></span><span class="sl-r" data-k="6" style="left:5.68%;top:47.13%;width:43.91%;height:5.28%"></span><span class="sl-r" data-k="7" style="left:5.62%;top:54.07%;width:43.18%;height:5.37%"></span><span class="sl-r" data-k="8" style="left:5.68%;top:61.11%;width:41.09%;height:5.28%"></span><span class="sl-r" data-k="9" style="left:52.5%;top:43.52%;width:10.31%;height:2.78%"></span><span class="sl-r" data-k="10" style="left:52.55%;top:47.13%;width:39.79%;height:5.28%"></span><span class="sl-r" data-k="11" style="left:52.55%;top:54.07%;width:41.3%;height:5.37%"></span><span class="sl-r" data-k="12" style="left:52.5%;top:61.11%;width:41.3%;height:4.91%"></span><span class="sl-r" data-k="13" style="left:5.62%;top:74.26%;width:85.52%;height:6.3%"></span>
</div>
<div class="sl-txt" markdown="1">

What was measured, what was modelled, and what nobody knows
{: data-k="1"}

> **SPOILER ALERT · SUBJECTIVE IMPRESSION**
> {: data-k="2"}
>
> **The *measurement* is a mess.**
> {: data-k="3"}
>
> The numbers contradict each other. Most of them are also correct. **That is the talk.**
> {: data-k="4"}

**The people who do this for a living say so**
{: data-k="5"}

Isolating the internet's share of US electricity "virtually guarantees large calculational errors." — *Berkeley Lab, 2000*
{: data-k="6"}

Its own earlier model's utilisation assumptions had "**little-to-no measured data** available to verify them." — *Lawrence Berkeley National Laboratory on LBNL, 2026*
{: data-k="7"}

"a general lack of consensus on methods to measure AI emissions" — *Cooper Elsworth, Google, to the National Academies, 2025*
{: data-k="8"}

**And it travels badly**
{: data-k="9"}

"Training a single AI model **can** emit as much carbon as five cars in their lifetimes" — *MIT Technology Review, 2019.* Google researchers later put the same run **88× lower**.
{: data-k="10"}

Of **100** news articles on ChatGPT's energy use sampled in April 2025, **53%** repeated one 2023 estimate and **75%** gave no source or uncertainty.
{: data-k="11"}

Of the **676** sources cited by **46** data-centre energy studies, **11%** had dead links and **10%** could not be located.
{: data-k="12"}

**So every number in this talk comes with three labels:** what it is a share **of**, what **year** it describes, and whether someone read a **meter** or ran a **model**. The talk is built to help you check them, not to tell you what to conclude.
{: data-k="13"}

</div>
</div>

---

## Start with the unsurprising part: efficiency up, totals up
{: id="start-with-the-unsurprising-part-efficiency-up-totals-up" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 6: two columns — per unit of work, energy down; in total, three different totals up](/assets/img/posts/2026-09-18-ai-environmental-impact-06.png)<span class="sl-r" data-k="t" style="left:3.75%;top:4.81%;width:65.73%;height:5.28%"></span><span class="sl-r" data-k="1" style="left:3.85%;top:13.7%;width:88.44%;height:6.11%"></span><span class="sl-r" data-k="2" style="left:4.32%;top:24.72%;width:13.28%;height:2.78%"></span><span class="sl-r" data-k="3" style="left:50.1%;top:24.72%;width:13.54%;height:2.78%"></span><span class="sl-r" data-k="4" style="left:4.27%;top:29.17%;width:45.1%;height:8.7%"></span><span class="sl-r" data-k="5" style="left:50.05%;top:29.17%;width:43.23%;height:5.93%"></span><span class="sl-r" data-k="6" style="left:4.27%;top:41.85%;width:42.92%;height:5.83%"></span><span class="sl-r" data-k="7" style="left:50.05%;top:41.76%;width:44.01%;height:5.83%"></span><span class="sl-r" data-k="8" style="left:4.27%;top:54.54%;width:45.05%;height:11.3%"></span><span class="sl-r" data-k="9" style="left:50%;top:54.54%;width:42.13%;height:8.24%"></span><span class="sl-r" data-k="10" style="left:3.75%;top:69.17%;width:92.03%;height:5.74%"></span><span class="sl-r" data-k="11" style="left:3.75%;top:93.98%;width:44.84%;height:2.41%"></span>
</div>
<div class="sl-txt" markdown="1">

Per unit of *work*, energy has fallen wherever it has been tracked. **Totals have risen** — but totals of three different things: one company's electricity, one country's metered electricity, and a forecast of peak *power*.
{: data-k="1"}

| **Down — per unit of work** | **Up — in total: total *what*?** |
|---|---|
| **Google, median Gemini Apps text prompt: 0.24 Wh** (May 2025, Google's own measurement), **33× lower than a year earlier**, mostly software. The repeated "~3 Wh" was never a measurement: an executive's remark about *cost* × a 2009 blog post | **Google's company-wide electricity rose 37%** in 2025 (Google's own report; all of Google, not only AI) |
| **Worldwide, 2010–2018:** computing work in data centres rose **~550%** while their electricity rose **~6%** (a model, *Science*, 2020) | **Ireland:** data centres went from **5% (2015) to 23% (2025)** of metered electricity. In 2025 alone their use rose **10%**; all other users' rose **2%** |
| **A famous 2019 training-carbon estimate** — 284 t for an automated architecture search — was recomputed by Google researchers in 2021 at **3.2 t**: **88× lower**, a figure they state *conditionally*, "for energy-efficient organizations like Google". **18.7×** of it is like-for-like, correcting only how the search had been read | **North America's grid reliability body** raised its ten-year summer peak-demand *growth* forecast by **69%** in one year (132 → 224 GW). **A forecast, not a measurement** |
{: data-keys="2 3 4 5 6 7 8 9"}

***Left:*** *a company's own measurement, a model, and a company's re-estimate.* ***Right:*** *a company's own total, a national meter reading, and a forecast. Efficiency per unit is real, and totals rose anyway. Neither column settles the other.*
{: data-k="10"}

Sources: Google 2025 and 2026; Masanet et al. 2020; Patterson et al. 2021; CSO Ireland 2026; NERC LTRA 2025
{: .small data-k="11" }

</div>
</div>

---

## What "AI's footprint" actually counts
{: id="what-ais-footprint-actually-counts" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 7: nested squares drawn to scale — world electricity 28,600 TWh, all data centres 485 TWh, "AI-focused" facilities about 155 TWh — beside notes on water, carbon, training and embodied emissions](/assets/img/posts/2026-09-18-ai-environmental-impact-07.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5%;width:48.33%;height:5.83%"></span><span class="sl-r" data-k="1" style="left:55.1%;top:21.57%;width:14.38%;height:2.87%"></span><span class="sl-r" data-k="2" style="left:55.16%;top:26.94%;width:39.69%;height:8.15%"></span><span class="sl-r" data-k="3" style="left:55.16%;top:36.57%;width:39.32%;height:8.24%"></span><span class="sl-r" data-k="4" style="left:55.16%;top:46.39%;width:37.24%;height:5.46%"></span><span class="sl-r" data-k="5" style="left:55.16%;top:53.43%;width:40%;height:13.52%"></span><span class="sl-r" data-k="6" style="left:3.75%;top:68.7%;width:45.78%;height:5.19%"></span><span class="sl-r" data-k="7" style="left:4.45%;top:18.02%;width:38.55%;height:2.82%"></span><span class="sl-r" data-k="8" style="left:4.48%;top:20.98%;width:43.65%;height:2.12%"></span><span class="sl-r" data-k="9" style="left:5.41%;top:23.53%;width:30.56%;height:2.03%"></span><span class="sl-r" data-k="10" style="left:8.11%;top:37.86%;width:8.78%;height:7.83%"></span><span class="sl-r" data-k="11" style="left:23.48%;top:32.53%;width:25.05%;height:5.17%"></span><span class="sl-r" data-k="11" style="left:34.39%;top:48.35%;width:14.14%;height:3.48%"></span><span class="sl-r" data-k="12" style="left:4.43%;top:57.63%;width:42.87%;height:3.21%"></span><span class="sl-r" data-k="12" style="left:4.47%;top:60.29%;width:40.56%;height:1.85%"></span><span class="sl-r" data-k="12" style="left:4.43%;top:61.62%;width:33.27%;height:1.85%"></span><span class="sl-r" data-k="12" style="left:4.45%;top:62.93%;width:48.85%;height:1.85%"></span><span class="sl-r" data-k="12" style="left:4.43%;top:64.26%;width:22.17%;height:1.87%"></span><span class="sl-r" data-k="13" style="left:3.75%;top:93.98%;width:43.07%;height:2.32%"></span>
</div>
<div class="sl-txt" markdown="1">

**What leaves the boxes**
{: data-k="1"}

- {: data-k="2"} **Water, at two layers:** cooling at the building, and water consumed generating the electricity. For US data centres in 2018 the second layer was **about three-quarters** of the total, hydropower reservoir evaporation included.
- {: data-k="3"} **Carbon, at the electricity layer,** reported two ways: **location-based** (the local grid's average) and **market-based** (after clean-energy purchases). Meta reports Llama 3.1 training as **11,390 t** one way and **0 t** the other.
- {: data-k="4"} **Training versus use:** the only company splits published predate ChatGPT. Google, all machine learning 2019–2021: about **⅗ use, ⅖ training**.
- {: data-k="5"} **Outside every electricity figure above:** making the chips and building the data centres. Meta put that **embodied** share at about **30%** of its AI tasks' emissions (2022); a 2026 review says **more than half** for large AI data centres — **50–82% of data-centre emissions** in its one numeric statement — without stating its carbon basis, and with its own boundary drawn around **server manufacturing only**.

*The IEA's "slightly more than 1.5% of global electricity demand" names no total. On the IEA's own consumption total it is 1.70%; on Ember's demand total, 1.53%.*
{: data-k="6"}

*Text in the figure:*

> **What “AI’s footprint” is a share of — three nested totals, 2025**
> {: data-k="7"}
>
> Modelled, not metered. Every percentage here is of world electricity CONSUMPTION, 28,600 TWh (IEA, July 2026 revision).
> {: data-k="8"}
>
> Key: Everything else · Data centres other than “AI-focused” facilities · “AI-focused” facilities
> {: data-k="9"}
>
> World electricity **28,600 TWh**, consumption, 2025 (IEA) — *areas to scale*
> {: data-k="10"}
>
> *The same two squares, magnified 5×:* All data centres 485 TWh, 1.70% of world electricity consumption · “AI-focused” facilities ~155 TWh, 0.54% of world electricity consumption
> {: data-k="11"}
>
> 485 TWh is ALL data centres — streaming, email, storage, business IT, not only AI. “AI-focused” is the IEA’s label for whole FACILITIES: everything in such a building counts, and AI work done elsewhere does not. Neither total separates AI workloads from the rest; no metering system anywhere does.
> Both are modelled from purchased shipment records, so they can err high (chips sold but not yet running) and low (custom chips that trackers cannot see).
> The other denominator: on Ember’s world “demand” total of 31,779 TWh — counted from generation, so it includes grid losses — the same 485 TWh is 1.53% and the 155 TWh is 0.49%.
> Sources: IEA (all data centres, P12; AI-focused facilities, P13); Ritchie / Our World in Data (155 TWh, derived from IEA’s 465 TWh for 2030 ÷ 3); Ember Global Electricity Review 2026 (P22).
> Type E — modelled estimate, in the deck’s own labelling. Percentages derived here.
> {: data-k="12"}
{: .small }

Sources: IEA 2026; Ember 2026; Our World in Data; Siddik et al. 2021; Meta model cards; Chien et al. 2026
{: .small data-k="13" }

</div>
</div>

---

## Percentage of *what*?
{: id="percentage-of-what" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 8: table — the same numerators over different denominators give different shares](/assets/img/posts/2026-09-18-ai-environmental-impact-08.png)<span class="sl-r" data-k="t" style="left:3.8%;top:5%;width:26.72%;height:5.83%"></span><span class="sl-r" data-k="1" style="left:3.75%;top:14.91%;width:71.93%;height:3.24%"></span><span class="sl-r" data-k="2" style="left:4.32%;top:23.7%;width:6.15%;height:2.31%"></span><span class="sl-r" data-k="3" style="left:36.56%;top:23.61%;width:7.29%;height:2.41%"></span><span class="sl-r" data-k="4" style="left:71.04%;top:23.61%;width:3.49%;height:2.41%"></span><span class="sl-r" data-k="5" style="left:4.32%;top:27.96%;width:19.22%;height:2.59%"></span><span class="sl-r" data-k="6" style="left:36.51%;top:27.96%;width:20.05%;height:2.68%"></span><span class="sl-r" data-k="7" style="left:71.09%;top:27.96%;width:3.38%;height:2.32%"></span><span class="sl-r" data-k="8" style="left:36.51%;top:32.22%;width:16.3%;height:2.68%"></span><span class="sl-r" data-k="9" style="left:71.09%;top:32.22%;width:3.38%;height:2.32%"></span><span class="sl-r" data-k="10" style="left:4.32%;top:36.39%;width:15.05%;height:2.59%"></span><span class="sl-r" data-k="11" style="left:36.56%;top:36.39%;width:13.7%;height:2.68%"></span><span class="sl-r" data-k="12" style="left:71.04%;top:36.39%;width:3.44%;height:2.32%"></span><span class="sl-r" data-k="13" style="left:36.56%;top:40.65%;width:19.17%;height:2.68%"></span><span class="sl-r" data-k="14" style="left:71.04%;top:40.65%;width:16.46%;height:2.68%"></span><span class="sl-r" data-k="15" style="left:36.56%;top:44.81%;width:11.93%;height:2.59%"></span><span class="sl-r" data-k="16" style="left:71.04%;top:44.81%;width:3.44%;height:2.32%"></span><span class="sl-r" data-k="17" style="left:4.32%;top:49.07%;width:10.94%;height:2.59%"></span><span class="sl-r" data-k="18" style="left:36.61%;top:49.07%;width:13.85%;height:2.68%"></span><span class="sl-r" data-k="19" style="left:71.04%;top:49.07%;width:2.6%;height:2.31%"></span><span class="sl-r" data-k="20" style="left:4.32%;top:53.24%;width:10.99%;height:2.59%"></span><span class="sl-r" data-k="21" style="left:36.61%;top:53.24%;width:23.75%;height:2.68%"></span><span class="sl-r" data-k="22" style="left:71.04%;top:53.24%;width:15.83%;height:2.68%"></span><span class="sl-r" data-k="23" style="left:4.32%;top:57.5%;width:24.58%;height:2.69%"></span><span class="sl-r" data-k="24" style="left:36.56%;top:57.5%;width:17.45%;height:2.59%"></span><span class="sl-r" data-k="25" style="left:71.04%;top:57.5%;width:3.44%;height:2.32%"></span><span class="sl-r" data-k="26" style="left:4.27%;top:61.67%;width:10.99%;height:2.68%"></span><span class="sl-r" data-k="27" style="left:36.56%;top:61.67%;width:12.29%;height:2.31%"></span><span class="sl-r" data-k="28" style="left:71.04%;top:61.67%;width:24.17%;height:4.63%"></span><span class="sl-r" data-k="29" style="left:3.8%;top:83.43%;width:86.98%;height:2.87%"></span><span class="sl-r" data-k="30" style="left:3.75%;top:93.98%;width:25.26%;height:2.32%"></span>
</div>
<div class="sl-txt" markdown="1">

**The same quantity over different totals gives different answers. Neither is wrong, as long as it says which total it used.**
{: data-k="1"}

| Numerator | Denominator | Share |
|---|---|---|
| Data centres worldwide, ~485 TWh (2025) | world **"demand"** (Ember, generation-based) | **1.53%** |
| | world **consumption** (IEA, July 2026) | **1.70%** |
| US data centres, 192 TWh (2024) | US net **generation** (EIA, 2024) | **4.46%** |
| | US total **end-use consumption** (EIA, 2024) | **4.67%** — the "4.7%" LBNL publishes |
| | US **retail sales** (EIA, 2024) | **4.83%** |
| Irish data centres, 2025 | Irish **metered** electricity (CSO) | **23%** |
| Irish data centres, 2024 | Irish electricity **demand** (SEAI, a different state body) | **21.2%** — a different year *and* base |
| US data-centre water, 2023 (building + power stations) | US water **consumed** (three main uses) | **0.76%** |
| the same, building only | US **fresh** water **withdrawn** | **0.017%** — **~45× lower**, from choices of what to count alone |
{: data-keys="2 3 4 5 6 7 - 8 9 10 11 12 - 13 14 - 15 16 17 18 19 20 21 22 23 24 25 26 27 28"}

***Most arguments about "how big" are arguments about the bottom of the fraction.*** *The water rows divide 2023 use by long-run totals (2010–2020; 2015): the years differ.*
{: data-k="29"}

Sources: Ember; IEA; EIA; LBNL 2025; CSO Ireland; SEAI; USGS
{: .small data-k="30" }

</div>
</div>

---

## Where the electricity, the water and the carbon actually enter
{: id="where-the-electricity-the-water-and-the-carbon-actually-enter" data-k="t"}

<div class="sl sl-stack" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 9: a grid of five layers — making the chips and building the data centre; generating the electricity; the building; training a model; everyday use — against electricity, water and carbon, with layer 1 marked as outside every electricity figure](/assets/img/posts/2026-09-18-ai-environmental-impact-09.png)<span class="sl-r" data-k="t" style="left:5.06%;top:7.48%;width:49.53%;height:3.37%"></span><span class="sl-r" data-k="1" style="left:5.08%;top:11.27%;width:69.99%;height:4.8%"></span><span class="sl-r" data-k="2" style="left:7.83%;top:20.33%;width:6.1%;height:2.77%"></span><span class="sl-r" data-k="3" style="left:24.28%;top:20.33%;width:6.41%;height:2.77%"></span><span class="sl-r" data-k="4" style="left:44.65%;top:20.4%;width:4.17%;height:2.32%"></span><span class="sl-r" data-k="5" style="left:65.11%;top:20.37%;width:4.7%;height:2.35%"></span><span class="sl-r" data-k="6" style="left:7.9%;top:23.86%;width:13.6%;height:4.65%"></span><span class="sl-r" data-k="7" style="left:7.83%;top:30.59%;width:11.53%;height:3.67%"></span><span class="sl-r" data-k="8" style="left:24.25%;top:23.86%;width:11.57%;height:2.32%"></span><span class="sl-r" data-k="9" style="left:44.65%;top:23.86%;width:16.96%;height:5.66%"></span><span class="sl-r" data-k="10" style="left:65.09%;top:23.86%;width:18.91%;height:7.54%"></span><span class="sl-r" data-k="11" style="left:9.54%;top:36.83%;width:14.47%;height:2.66%"></span><span class="sl-r" data-k="12" style="left:7.85%;top:41.67%;width:8.82%;height:3.67%"></span><span class="sl-r" data-k="13" style="left:24.21%;top:36.83%;width:10.75%;height:4.05%"></span><span class="sl-r" data-k="14" style="left:44.65%;top:36.83%;width:17.45%;height:7.5%"></span><span class="sl-r" data-k="15" style="left:65.07%;top:36.83%;width:17.89%;height:5.66%"></span><span class="sl-r" data-k="16" style="left:7.87%;top:47.91%;width:12.16%;height:4.61%"></span><span class="sl-r" data-k="17" style="left:7.85%;top:54.6%;width:8.72%;height:3.67%"></span><span class="sl-r" data-k="18" style="left:24.23%;top:47.91%;width:18.36%;height:4.05%"></span><span class="sl-r" data-k="19" style="left:44.65%;top:47.91%;width:18.29%;height:7.35%"></span><span class="sl-r" data-k="20" style="left:65.11%;top:47.91%;width:11.32%;height:4.05%"></span><span class="sl-r" data-k="21" style="left:9.5%;top:60.84%;width:9.59%;height:2.65%"></span><span class="sl-r" data-k="22" style="left:7.85%;top:65.24%;width:7.41%;height:2.2%"></span><span class="sl-r" data-k="23" style="left:24.21%;top:60.88%;width:12.42%;height:4.01%"></span><span class="sl-r" data-k="24" style="left:44.65%;top:60.84%;width:17.64%;height:4.04%"></span><span class="sl-r" data-k="25" style="left:65.09%;top:60.84%;width:30.93%;height:5.77%"></span><span class="sl-r" data-k="26" style="left:9.59%;top:70.05%;width:7.73%;height:2.65%"></span><span class="sl-r" data-k="27" style="left:7.85%;top:74.86%;width:10.37%;height:3.37%"></span><span class="sl-r" data-k="28" style="left:24.23%;top:70.05%;width:20.64%;height:5.77%"></span><span class="sl-r" data-k="29" style="left:44.65%;top:70.05%;width:19.27%;height:5.66%"></span><span class="sl-r" data-k="30" style="left:65.09%;top:70.05%;width:17.11%;height:5.77%"></span><span class="sl-r" data-k="31" style="left:44.8%;top:81.81%;width:27.83%;height:2.28%"></span><span class="sl-r" data-k="32" style="left:5.04%;top:84.89%;width:60.46%;height:5.28%"></span><span class="sl-r" data-k="32" style="left:5.04%;top:89.74%;width:50.59%;height:2.05%"></span><span class="sl-r" data-k="32" style="left:5.06%;top:91.32%;width:64.88%;height:3.71%"></span>
</div>
<div class="sl-txt" markdown="1">

*Text in the figure:*

Five layers. Most published “AI uses X” figures count only the shaded ones — and not all of them count the same shaded ones. Nothing here is drawn to scale: the layers are not comparable quantities.
{: data-k="1"}

*Layer 1 is marked “OUTSIDE every one of them”; layers 2–5 are shaded and marked “INSIDE the electricity figures on the other slides”.*

| The layer | Electricity | Water | Carbon |
|---|---|---|---|
| <span data-k="6">**1. Making the chips, building the data centre**</span><br><span data-k="7">*“embodied” — spent before a single query is answered*</span> | No figure for AI in this corpus. | A chip fab “can use” ~38 million L a day of ultra-pure water — drawn, not consumed. (E, 2024) | ~30% of Meta’s AI-task emissions (D, pub. 2022). “More than half” for large AI data centres in a 2026 review — carbon basis not stated (E). 1,312 kg per 8-GPU H100 board (D, 2025). |
| <span data-k="11">**2. Generating the electricity**</span><br><span data-k="12">*the grid, wherever the building is plugged in*</span> | ~485 TWh, all data centres — 1.70% of world electricity consumption. (E, 2025) | ~75% of the US data-centre water footprint, reservoir evaporation included (E, 2018). Coefficient 1.8–7.6 L/kWh, and which end you get is mostly the hydropower choice. | Whatever the local grid emits — and which method you use: 11,390 t location-based, 0 t market-based, for the same runs. (D, 2024) |
| <span data-k="16">**3. The building: cooling and overhead**</span><br><span data-k="17">*the part a data-centre operator can change*</span> | Inside “full serving stack” figures. Counting only the chips is about 1.7× narrower. (D, 2025) | ~25% of the US data-centre water footprint by volume — but over 40% of its scarcity-weighted index, because it is drawn next to the building. (E, 2018) | Follows the electricity above. No separate figure. |
| <span data-k="21">**4. Training a model**</span><br><span data-k="22">*one-off, per model*</span> | 433 MWh, BLOOM 176B — GPU-hours × rated power, not metered. (E, 2022) | 281,000 m³, Mistral Large 2, lifecycle method, server manufacturing included. (D, 2025) | 50.5 t, BLOOM — chips + idle + embodied (E, 2022). 8,930 t, Llama 3.1 405B (D). 1,247.61 t, Gemma 2 — pre-training only (D). Nothing published for GPT-4/5, Gemini, Claude, Grok. |
| <span data-k="26">**5. Everyday use**</span><br><span data-k="27">*every query, for as long as the model is served*</span> | 0.24 Wh, median Google text prompt (D, May 2025). 3.91 Wh, a simulated long reasoning query (E, 2026). ~150 Wh, one typed agentic-coding prompt (E, 2026). | 0.26 mL per prompt — the building only (D, 2025). 16.9 mL per response — including the power station, 87% of it off-site (E, model of GPT-3). | 0.03 g per prompt, market-based — the only basis the paper reports (D, 2025). ~0.09 g location-based, derived here. |
{: data-keys="2 3 4 5 - 8 9 10 - 13 14 15 - 18 19 20 - 23 24 25 - 28 29 30"}

**Water leaves at two layers, and only one of them is the building.** *(Marked on layers 2 and 3.)*
{: data-k="31"}

Training versus everyday use: the only company splits ever published predate ChatGPT. Google, all its machine learning 2019–21: about ⅗ use, ⅖ training. Meta, one production translation model (pub. 2022): 65% use, 35% training; its recommendation models, about even. No company publishes how many times a current chatbot is used, so no one can compute this ratio for the models you actually use.
Type codes, as used throughout the talk: M metered or instrumented · D first-party disclosure · E modelled estimate. A figure’s type matters more than its size.
Sources, by row: IEA P12; Siddik, Shehabi & Marston 2021 P37; Torcellini et al. 2003 and the coefficient set in “amendment-01”; Meta Llama 3.1 model card; Chien et al. 2026 P53; Wu et al. (Meta) P70; NVIDIA PCF summary 2025; WEF 2024 P66; Luccioni, Viguier & Ligozat P59; Gemma 2 technical report; Mistral AI with Carbone 4 and ADEME P69; Google (Elsworth et al.) P42; Li et al. P29; Oviedo et al. P33.
{: .small data-k="32" }

</div>
</div>

---

## What one use costs
{: id="what-one-use-costs" data-k="t"}

<div class="sl sl-stack" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 10: table of three per-use energy figures — 0.24 Wh, 3.91 Wh and about 150 Wh — with what kind of number each is and its weakness](/assets/img/posts/2026-09-18-ai-environmental-impact-10.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5.09%;width:25.47%;height:4.63%"></span><span class="sl-r" data-k="1" style="left:3.75%;top:14.26%;width:85%;height:3.24%"></span><span class="sl-r" data-k="2" style="left:15.52%;top:24.26%;width:10.57%;height:2.78%"></span><span class="sl-r" data-k="3" style="left:39.53%;top:24.26%;width:13.23%;height:2.78%"></span><span class="sl-r" data-k="4" style="left:67.66%;top:24.26%;width:22.24%;height:2.78%"></span><span class="sl-r" data-k="5" style="left:4.32%;top:28.7%;width:3.75%;height:2.59%"></span><span class="sl-r" data-k="6" style="left:15.52%;top:28.61%;width:4.43%;height:2.32%"></span><span class="sl-r" data-k="7" style="left:39.53%;top:28.61%;width:4.43%;height:2.32%"></span><span class="sl-r" data-k="8" style="left:67.66%;top:28.61%;width:11.67%;height:2.69%"></span><span class="sl-r" data-k="9" style="left:4.27%;top:32.87%;width:10.36%;height:2.32%"></span><span class="sl-r" data-k="10" style="left:15.52%;top:32.87%;width:22.86%;height:7.41%"></span><span class="sl-r" data-k="11" style="left:39.53%;top:32.87%;width:26.51%;height:7.04%"></span><span class="sl-r" data-k="12" style="left:67.66%;top:32.87%;width:26.15%;height:7.04%"></span><span class="sl-r" data-k="13" style="left:4.32%;top:41.76%;width:6.41%;height:2.32%"></span><span class="sl-r" data-k="14" style="left:15.52%;top:41.76%;width:22.55%;height:5.09%"></span><span class="sl-r" data-k="15" style="left:39.53%;top:41.76%;width:24.69%;height:4.72%"></span><span class="sl-r" data-k="16" style="left:67.66%;top:41.76%;width:16.87%;height:2.59%"></span><span class="sl-r" data-k="17" style="left:5.31%;top:63.8%;width:58.23%;height:3.15%"></span><span class="sl-r" data-k="18" style="left:3.75%;top:70.19%;width:91.56%;height:8.24%"></span><span class="sl-r" data-k="19" style="left:3.75%;top:79.63%;width:91.04%;height:5.46%"></span><span class="sl-r" data-k="20" style="left:3.75%;top:93.89%;width:44.17%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**Three ways of "using AI", three very different numbers — and none is an independent measurement of the closed services most people use**
{: data-k="1"}

| | **A quick text prompt** | **A long "reasoning" query** | **One typed prompt in an agentic coding tool** |
|---|---|---|---|
| **Energy** | **0.24 Wh** | **3.91 Wh** | **~150 Wh** *(range 60–290)* |
| **What kind of number** | Google's own production measurement (May 2025): the prompt-weighted median of its models' averages | A simulation by Microsoft researchers (2026): models over 200 billion parameters on H100 servers, answers of ~5,000 tokens | One researcher's estimate from his own usage logs (Aug 2026) using three published per-token factors. His median *session* was ~600 Wh |
| **Its weakness** | One company's median; Google publishes neither the mean nor the number of prompts | Assumed hardware, load and answer length; an earlier version said 4.32 | One user, one tool, borrowed factors |
{: data-keys="- 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16"}

> **Do not multiply any of these by a number of uses.** None is an average over real traffic that you can scale.
> {: data-k="17"}

**The kind of task matters as much as the model.** Luccioni et al. (FAccT 2024), one 8×A100 node, inference only: **≈60×** between the mean energy of text generation **capped at 10 output tokens** and the mean for image generation; **≈29× on the paper's own medians**. n = 8, the image side's standard deviation exceeds its mean, and the comparison is **not size-matched** — the 11-billion-parameter model is on the *text* side. Image generation costs more *despite* smaller models.
{: data-k="18"}

**Why there is no everyday comparison here.** Items that make these look small, such as a drive or a flight, are published as *carbon*, not energy. The item that makes them look large, a web search, rests on a 2009 blog post. Both groups are in the source list.
{: data-k="19"}

Sources: Google (Elsworth et al.) 2025; Oviedo et al. 2026; Hausfather 2026; Luccioni, Jernite & Strubell 2024
{: .small data-k="20" }

</div>
</div>

---

## Why there is no single "cost of a prompt"
{: id="why-there-is-no-single-cost-of-a-prompt" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 11: four axes of per-query energy — task (1,450×), boundary (2.4×), how busy (0.28 kWh), mode (154–697×)](/assets/img/posts/2026-09-18-ai-environmental-impact-11.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5%;width:53.49%;height:5.83%"></span><span class="sl-r" data-k="1" style="left:3.8%;top:15%;width:67.08%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:7.66%;top:28.61%;width:7.71%;height:4.63%"></span><span class="sl-r" data-k="2" style="left:20.26%;top:24.07%;width:74.48%;height:5.56%"></span><span class="sl-r" data-k="3" style="left:8.91%;top:45.28%;width:5.21%;height:3.98%"></span><span class="sl-r" data-k="3" style="left:20.26%;top:40.83%;width:75.52%;height:5.46%"></span><span class="sl-r" data-k="4" style="left:6.93%;top:62.13%;width:9.43%;height:3.61%"></span><span class="sl-r" data-k="4" style="left:20.26%;top:57.41%;width:73.96%;height:5.56%"></span><span class="sl-r" data-k="5" style="left:6.93%;top:78.89%;width:9.27%;height:3.52%"></span><span class="sl-r" data-k="5" style="left:20.31%;top:74.07%;width:73.91%;height:5.56%"></span><span class="sl-r" data-k="6" style="left:3.75%;top:93.89%;width:42.19%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**Per-query energy depends on the task, the accounting boundary, how busy the server is, and the mode**
{: data-k="1"}

**1,450×**  
**Task.** From **0.002 to 2.907 kWh per 1,000 inferences** — text classification against image generation — on the same lab hardware (open models up to 11 billion parameters, one request at a time, 2024).
{: data-k="2"}

**2.4×**  
**Boundary.** Google's 0.24 Wh becomes **0.10 Wh** under its narrower method: about **1.7×** from counting only the chips, about **1.4×** from counting only the most efficient tenth of its data centres (same month, May 2025).
{: data-k="3"}

**0.28 kWh**  
**How busy.** On BLOOM's lightly used public demo (2022) the server still used about **0.28 kWh every 10 minutes** when almost no requests arrived. *Software-estimated; the authors say the total cannot be cleanly split into idle and working energy.*
{: data-k="4"}

**154–697×**  
**Mode.** For three open models that can switch "reasoning" on and off (3, 15 and 70 billion parameters), turning it on raised GPU energy per query **154× to 697×**, as they wrote 300–800× more tokens. Across the benchmark, reasoning models averaged about **30×** (Dec 2025).
{: data-k="5"}

Sources: Luccioni, Jernite & Strubell 2024; Google 2025; BLOOM (Luccioni et al.) 2022; ML.ENERGY 2025
{: .small data-k="6" }

</div>
</div>

---

## Why “task” is worth a moment’s focus
{: id="why-task-is-worth-a-moments-focus" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 12: the 1,450× task spread beside a diagram of six shapes of work one typed prompt can set running. A single box labelled ONE PROMPT leads to six rows: answers straight away; thinks first, then answers; reads an image you attached; calls a tool; keeps looping between model and tool; hands parts of the job to other agents. A marker on each row is filled where this talk prints a per-use energy figure for that shape of work (rows 1, 2 and 5) and hollow where it does not (rows 3, 4 and 6). The diagram is schematic and encodes no quantities.](/assets/img/posts/2026-09-18-ai-environmental-impact-12.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5%;width:49.84%;height:5.83%"></span><span class="sl-r" data-k="1" style="left:3.75%;top:14.54%;width:51.51%;height:6.2%"></span><span class="sl-r" data-k="2" style="left:5.73%;top:30.19%;width:11.72%;height:6.76%"></span><span class="sl-r" data-k="3" style="left:21.77%;top:26.67%;width:25.1%;height:3.24%"></span><span class="sl-r" data-k="4" style="left:21.77%;top:31.02%;width:33.65%;height:6.94%"></span><span class="sl-r" data-k="5" style="left:3.8%;top:44.54%;width:52.19%;height:8.8%"></span><span class="sl-r" data-k="6" style="left:3.75%;top:55.46%;width:52.5%;height:8.89%"></span><span class="sl-r" data-k="7" style="left:3.75%;top:66.48%;width:51.77%;height:8.43%"></span><span class="sl-r" data-k="8" style="left:3.75%;top:77.31%;width:53.02%;height:11.76%"></span><span class="sl-r" data-k="9" style="left:60.8%;top:17.03%;width:22.28%;height:3.08%"></span><span class="sl-r" data-k="10" style="left:60.78%;top:20.23%;width:28.83%;height:2.28%"></span><span class="sl-r" data-k="11" style="left:61.65%;top:23.53%;width:16.76%;height:4.05%"></span><span class="sl-r" data-k="11" style="left:83.73%;top:24.47%;width:7.78%;height:1.89%"></span><span class="sl-r" data-k="12" style="left:63.94%;top:30.2%;width:11.46%;height:2.73%"></span><span class="sl-r" data-k="13" style="left:63.94%;top:36.29%;width:12.92%;height:2.66%"></span><span class="sl-r" data-k="14" style="left:64%;top:42.39%;width:14.56%;height:2.72%"></span><span class="sl-r" data-k="15" style="left:63.96%;top:47.13%;width:15.47%;height:4.87%"></span><span class="sl-r" data-k="16" style="left:63.99%;top:53.08%;width:13.72%;height:5.13%"></span><span class="sl-r" data-k="17" style="left:63.98%;top:61.64%;width:15.47%;height:5.2%"></span><span class="sl-r" data-k="18" style="left:61.78%;top:71.45%;width:28.77%;height:4.64%"></span><span class="sl-r" data-k="19" style="left:60.78%;top:77.59%;width:31.47%;height:3.71%"></span><span class="sl-r" data-k="20" style="left:60.77%;top:81.42%;width:32.71%;height:3.83%"></span><span class="sl-r" data-k="21" style="left:60.79%;top:85.31%;width:32.52%;height:3.85%"></span><span class="sl-r" data-k="22" style="left:3.75%;top:93.89%;width:51.93%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**The same number as the slide before, with room to say what it is** — and what “task” can mean beyond the two types the study measured
{: data-k="1"}

> **1,450×**
> {: data-k="2"}
>
> **0.002 → 2.907 kWh per 1,000 inferences**
> {: data-k="3"}
>
> the *means* of two task types — text classification against image generation — on one 8×A100 node, open models up to 11 billion parameters, one request at a time, 2024
> {: data-k="4"}

- {: data-k="5"} **The spread is task** *and* **model.** The two tasks use different models, so this is not a controlled comparison at fixed model size. **88 open models**, the largest Flan-T5-XXL at **11 billion parameters**, one 8×A100 node, **unbatched** — a lab setup, not production traffic.
- {: data-k="6"} **It is the extremes of a spread, not a headline multiple.** The paper reports a range across tasks; the variation *inside* each task is not shown. Read 1,450× as the distance between the cheapest and the dearest task measured, not as a ratio that anything typical has.
- {: data-k="7"} **And it is one axis of four.** The slide before shows three more — the accounting boundary, how busy the server is, and whether “reasoning” is switched on. **None of them multiplies with any other.**
- {: data-k="8"} **What “task” can also mean.** Everything above is across task *types* inside **single model calls**. The diagram to the right is a different axis: how much work one typed prompt can set running before any answer comes back. It carries its own caveats — **it encodes no energy, and it does not multiply with the 1,450×.**

*Text in the figure:*

> **“One prompt” is not one kind of work**
> {: data-k="9"}
>
> Six shapes of work one typed prompt can set running, ordered by structure and **not** by cost.
> {: data-k="10"}
>
> **ONE PROMPT** — one thing you typed, one reply on your screen. Key: model call · tool call · reply
> {: data-k="11"}
>
> <span data-k="12">● Answers straight away</span>  
> <span data-k="13">● Thinks first, then answers</span>  
> <span data-k="14">○ Reads an image you attached</span>  
> <span data-k="15">○ Calls a tool — a search, a fetch, some code</span>  
> <span data-k="16">● Keeps looping: model, tool, model, tool</span>  
> <span data-k="17">○ Hands parts of the job to other agents</span>
>
> **All six of these are one prompt.** So the first question about any “per-prompt” number is: which of these was it?
> {: data-k="18"}
>
> ● a per-use energy figure for this shape of work is printed somewhere in this talk · ○ none is. That is a statement about this deck, not about the literature.
> {: data-k="19"}
>
> Schematic, drawn for this talk, not reproduced from a source. **Nothing here encodes energy:** a longer chain means more calls happen, never how many and never what they cost; “···” means “repeats”, not a number.
> {: data-k="20"}
>
> Nothing here says which path is common, and no source in this talk does either. The >1,450× spread on this slide is a different axis: it is between the *means* of two task types, inside single model calls (Luccioni et al. 2024).
> {: data-k="21"}
{: .small }

Sources: Luccioni, Jernite & Strubell, FAccT 2024 (P60). The diagram was drawn for this talk and is not reproduced from a source.
{: .small data-k="22" }

</div>
</div>

---

## Why this talk prints no everyday comparison
{: id="why-this-talk-prints-no-everyday-comparison" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 13: three per-use figures in their own units — 0.24 Wh, 3.91 Wh, about 150 Wh — and why nothing is compared to anything else](/assets/img/posts/2026-09-18-ai-environmental-impact-13.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5.09%;width:59.17%;height:5.74%"></span><span class="sl-r" data-k="1" style="left:3.75%;top:15%;width:59.84%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:5.68%;top:27.13%;width:11.88%;height:4.91%"></span><span class="sl-r" data-k="2" style="left:5.68%;top:34.07%;width:25%;height:5.19%"></span><span class="sl-r" data-k="3" style="left:36.41%;top:27.13%;width:11.56%;height:4.91%"></span><span class="sl-r" data-k="3" style="left:36.41%;top:34.07%;width:23.18%;height:5.09%"></span><span class="sl-r" data-k="4" style="left:67.19%;top:27.13%;width:12.71%;height:4.91%"></span><span class="sl-r" data-k="4" style="left:67.14%;top:34.07%;width:24.11%;height:5.09%"></span><span class="sl-r" data-k="5" style="left:5.68%;top:53.52%;width:87.45%;height:6.02%"></span><span class="sl-r" data-k="6" style="left:3.8%;top:69.72%;width:80.36%;height:3.06%"></span><span class="sl-r" data-k="7" style="left:3.75%;top:74.17%;width:71.98%;height:3.15%"></span><span class="sl-r" data-k="8" style="left:3.75%;top:93.89%;width:46.04%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**Three kinds of use, in their own units — and why nothing here is compared to anything else**
{: data-k="1"}

**0.24 Wh**  
a median Google text prompt — Google's own measurement; **0.03 g CO₂e** market-based, May 2025
{: data-k="2"}

**3.91 Wh**  
a long reasoning query — Microsoft researchers' simulation, 2026
{: data-k="3"}

**~150 Wh**  
one typed prompt in an agentic coding tool — one user's estimate, 2026
{: data-k="4"}

> **No everyday comparator appears anywhere in this talk.** Eighteen of them were chosen and frozen on 19 August, before any AI figure had been seen, and they stay published in the source list. None of them reaches a slide.
> {: data-k="5"}

*Why:* every conversion needs a choice — which use, how many uses, which grid, whether the screen counts — and the choice decides the answer.
{: data-k="6"}

The two items that would sway you most, **a kettle boil** and **doing the task by hand**, are exactly the two that nobody has published.
{: data-k="7"}

Sources: Google 2025; Oviedo et al. 2026; Hausfather 2026; comparator set, frozen 19 Aug 2026 (Amendment 03)
{: .small data-k="8" }

</div>
</div>

---

## One training run, fully counted
{: id="one-training-run-fully-counted" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 14: BLOOM's training emissions split three ways, with a world map of grid carbon intensity by country and a US map of a hypothetical data centre's carbon footprint by watershed](/assets/img/posts/2026-09-18-ai-environmental-impact-14.png)<span class="sl-r" data-k="t" style="left:3.8%;top:5%;width:41.04%;height:5.83%"></span><span class="sl-r" data-k="1" style="left:3.8%;top:13.7%;width:59.58%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:4.27%;top:20.09%;width:9.32%;height:2.5%"></span><span class="sl-r" data-k="3" style="left:19.06%;top:20.09%;width:9.79%;height:2.5%"></span><span class="sl-r" data-k="4" style="left:33.85%;top:20.09%;width:9.48%;height:2.5%"></span><span class="sl-r" data-k="5" style="left:4.27%;top:24.07%;width:6.04%;height:2.5%"></span><span class="sl-r" data-k="6" style="left:19.11%;top:24.07%;width:5.99%;height:2.5%"></span><span class="sl-r" data-k="7" style="left:33.91%;top:24.07%;width:5.99%;height:2.5%"></span><span class="sl-r" data-k="8" style="left:4.27%;top:28.06%;width:12.45%;height:6.85%"></span><span class="sl-r" data-k="9" style="left:19.06%;top:28.06%;width:13.49%;height:6.94%"></span><span class="sl-r" data-k="10" style="left:33.8%;top:28.06%;width:13.7%;height:6.57%"></span><span class="sl-r" data-k="11" style="left:49.84%;top:19.54%;width:44.58%;height:4.72%"></span><span class="sl-r" data-k="12" style="left:49.84%;top:25.65%;width:45.47%;height:10.09%"></span><span class="sl-r" data-k="13" style="left:49.9%;top:36.76%;width:44.11%;height:5.09%"></span><span class="sl-r" data-k="14" style="left:65.05%;top:45.37%;width:30.63%;height:8.61%"></span><span class="sl-r" data-k="15" style="left:65.05%;top:55.65%;width:30%;height:8.7%"></span><span class="sl-r" data-k="16" style="left:3.75%;top:83.24%;width:91.72%;height:5%"></span><span class="sl-r" data-k="17" style="left:3.75%;top:93.89%;width:57.71%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**BLOOM (176 billion parameters, trained in France in 2022): 50.5 tonnes CO₂e, counted three ways**
{: data-k="1"}

| **Chips doing the work** | **Keeping the cluster on** | **Making the hardware** |
|---|---|---|
| **24.69 t (49%)** | **14.60 t (29%)** | **11.20 t (22%)** |
| Estimated: GPU-hours × each GPU's rated 400 W. Real-time power was not tracked | Measured: the cluster's draw when idle against its draw when training | A lower bound — no chipmaker published manufacturing figures at the time |
{: data-keys="2 3 4 5 6 7 8 9 10"}

**The trial and intermediate runs emitted more than the final model:** 35.8 t against 24.69 t. Some of those intermediate models were released too.
{: data-k="11"}

**Where you train can matter more than how much you train.** In the paper's comparison table BLOOM used *more* electricity than a comparable model, OPT (433 vs 324 MWh), yet emitted about a third as much carbon (25 vs 70 t), because France's grid was 57 g CO₂e/kWh and OPT's was 231. *(The table's rows do not all count data-centre overhead the same way.)*
{: data-k="12"}

*One cluster, one country. The chip term assumes every GPU drew its full rating, which can err either way; the hardware term is a lower bound.*
{: data-k="13"}

**Left — the world, by country.** *Lifecycle* g CO₂e per kWh generated: upstream, supply chain and manufacturing included, all greenhouse gases. **2025**, or the nearest year 2022–2024 where 2025 is missing. Scale **0 to 900+ g**. *Our World in Data, from Ember 2026, CC BY.*
{: data-k="14"}

**Right — the United States, by watershed.** The carbon footprint of the same **hypothetical 1 MW data centre**, **0.02 to 1 ton CO₂e/MWh**, 2018 data. The paper states neither short or metric tons, nor whether the basis is lifecycle or combustion only. *Siddik et al. 2021, figure 4 panel C, CC BY 4.0.*
{: data-k="15"}

*Two different bases and three different years, so do not read a value off either map and set it against the 57 and 231 above — those are the operational grid factors the paper used. What the maps show is the size of the spread: where you build or train moves the number further than most people expect.*
{: data-k="16"}

Sources: Luccioni, Viguier & Ligozat, JMLR 2023 (BLOOM); Our World in Data / Ember 2026 (CC BY); Siddik, Shehabi & Marston 2021 (CC BY 4.0)
{: .small data-k="17" }

</div>
</div>

---

## The largest disclosed footprints, and the accounting underneath
{: id="the-largest-disclosed-footprints-and-the-accounting-underneath" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 15: training footprints disclosed by Meta (Llama 3.1), Google (Gemma 2) and Mistral (Large 2), each with its own boundary](/assets/img/posts/2026-09-18-ai-environmental-impact-15.png)<span class="sl-r" data-k="t" style="left:3.75%;top:4.81%;width:72.4%;height:5.09%"></span><span class="sl-r" data-k="1" style="left:3.75%;top:16.57%;width:45.05%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:5.73%;top:26.39%;width:9.9%;height:2.68%"></span><span class="sl-r" data-k="2" style="left:25.16%;top:25.19%;width:68.28%;height:7.87%"></span><span class="sl-r" data-k="3" style="left:5.62%;top:45.28%;width:11.04%;height:3.15%"></span><span class="sl-r" data-k="3" style="left:25.16%;top:44.17%;width:67.81%;height:5.28%"></span><span class="sl-r" data-k="4" style="left:5.73%;top:64.26%;width:9.53%;height:3.15%"></span><span class="sl-r" data-k="4" style="left:25.16%;top:62.87%;width:66.15%;height:5.56%"></span><span class="sl-r" data-k="5" style="left:3.75%;top:83.24%;width:50.68%;height:2.96%"></span><span class="sl-r" data-k="5" style="left:3.8%;top:87.04%;width:78.39%;height:3.06%"></span><span class="sl-r" data-k="6" style="left:3.75%;top:93.98%;width:44.58%;height:2.41%"></span>
</div>
<div class="sl-txt" markdown="1">

**Companies' own training numbers — each with a different boundary**
{: data-k="1"}

**Meta · Llama 3.1**  
**8,930 t CO₂e** for the 405B model; **11,390 t** for the three-model family. Both **location-based**, using the average grid where the chips ran. **The same runs are reported as 0 t "market-based"**, after renewable purchases. Meta multiplied GPU-hours by each GPU's *rated* power, which leaves out the rest of the server; a 2025 measurement study treats that as a **lower bound**.
{: data-k="2"}

**Google · Gemma 2**  
**1,247.61 t CO₂e**, **pre-training only**. The larger "teacher" model used to train two of the three is not counted. The report calls Google's data centres carbon-neutral; Google itself stopped claiming operational carbon neutrality from 2023 (its July 2024 report).
{: data-k="3"}

**Mistral · Large 2**  
**20.4 kt CO₂e and 281,000 m³ of water consumed** — training "as of January 2025, and after 18 months of usage", server manufacturing included. A lifecycle study with France's ecological transition agency, reviewed by two consultancies (2025).
{: data-k="4"}

**These are not comparable with each other:** different phases, boundaries and carbon methods.  
**No developer has published a training energy or emissions figure** for GPT-4, GPT-5, any Gemini model, Claude or Grok (as of mid-September 2026).
{: data-k="5"}

Sources: Meta model cards; Google Gemma 2 report; Mistral/ADEME lifecycle study 2025; Newkirk et al. 2025
{: .small data-k="6" }

</div>
</div>

---

## The bar chart these numbers invite — and why it is not a comparison
{: id="the-bar-chart-these-numbers-invite--and-why-it-is-not-a-comparison" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 16: a deliberately naive bar chart of five published training footprints on one axis — 20,400 t, 11,390 t, 8,930 t, 1,247.61 t and 0 t — beside a column explaining what each number actually covers](/assets/img/posts/2026-09-18-ai-environmental-impact-16.png)<span class="sl-r" data-k="t" style="left:7.12%;top:7.1%;width:48.45%;height:3.07%"></span><span class="sl-r" data-k="1" style="left:7.2%;top:10.67%;width:50.8%;height:4.42%"></span><span class="sl-r" data-k="2" style="left:7.16%;top:16.56%;width:21.96%;height:2.24%"></span><span class="sl-r" data-k="3" style="left:7.2%;top:23.84%;width:7.7%;height:2.45%"></span><span class="sl-r" data-k="4" style="left:7.16%;top:25.99%;width:3.53%;height:1.98%"></span><span class="sl-r" data-k="5" style="left:11.49%;top:25.95%;width:12.7%;height:2.13%"></span><span class="sl-r" data-k="6" style="left:7.13%;top:27.84%;width:32.66%;height:2.13%"></span><span class="sl-r" data-k="7" style="left:7.71%;top:29.7%;width:20.63%;height:2.16%"></span><span class="sl-r" data-k="8" style="left:7.2%;top:34.1%;width:17.38%;height:2.46%"></span><span class="sl-r" data-k="9" style="left:7.2%;top:36.25%;width:3.49%;height:1.98%"></span><span class="sl-r" data-k="10" style="left:11.49%;top:36.21%;width:17.03%;height:2.13%"></span><span class="sl-r" data-k="11" style="left:7.13%;top:38.1%;width:33.33%;height:3.73%"></span><span class="sl-r" data-k="12" style="left:8.38%;top:41.6%;width:25.95%;height:2.13%"></span><span class="sl-r" data-k="13" style="left:7.2%;top:44.4%;width:7.87%;height:2.13%"></span><span class="sl-r" data-k="14" style="left:7.16%;top:46.51%;width:3.1%;height:1.98%"></span><span class="sl-r" data-k="15" style="left:11.06%;top:46.47%;width:19.96%;height:2.13%"></span><span class="sl-r" data-k="16" style="left:7.13%;top:48.37%;width:25.28%;height:2.13%"></span><span class="sl-r" data-k="17" style="left:7.71%;top:50.26%;width:19.81%;height:2.13%"></span><span class="sl-r" data-k="18" style="left:7.16%;top:54.66%;width:8.32%;height:2.45%"></span><span class="sl-r" data-k="19" style="left:48.21%;top:57.72%;width:4.8%;height:2.09%"></span><span class="sl-r" data-k="20" style="left:12.06%;top:56.73%;width:13.88%;height:2.16%"></span><span class="sl-r" data-k="21" style="left:7.18%;top:58.63%;width:28.57%;height:2.13%"></span><span class="sl-r" data-k="22" style="left:7.73%;top:60.52%;width:21.35%;height:2.13%"></span><span class="sl-r" data-k="23" style="left:7.2%;top:64.92%;width:15.46%;height:2.45%"></span><span class="sl-r" data-k="24" style="left:9.57%;top:67.03%;width:17.28%;height:2.13%"></span><span class="sl-r" data-k="25" style="left:7.13%;top:68.89%;width:35.16%;height:3.51%"></span><span class="sl-r" data-k="26" style="left:7.73%;top:72.38%;width:24.66%;height:2.13%"></span><span class="sl-r" data-k="27" style="left:7.12%;top:76.02%;width:22.8%;height:4.38%"></span><span class="sl-r" data-k="28" style="left:45.41%;top:16.56%;width:24.84%;height:2.27%"></span><span class="sl-r" data-k="29" style="left:45.37%;top:80.64%;width:49.27%;height:3.98%"></span><span class="sl-r" data-k="30" style="left:7.16%;top:87.66%;width:55.24%;height:4.78%"></span><span class="sl-r" data-k="30" style="left:7.16%;top:91.92%;width:48.24%;height:3.33%"></span>
</div>
<div class="sl-txt" markdown="1">

*Text in the figure:*

Five published training footprints, in tonnes of CO₂-equivalent. Every one is transcribed correctly from the company’s own document. Put them on one axis and you are ranking the boundaries, not the runs.
{: data-k="1"}

**WHAT EACH NUMBER ACTUALLY COVERS**
{: data-k="2"}

| Number | What it covers |
|---|---|
| <span data-k="3">**Mistral Large 2**</span><br><span data-k="4">20,400 t</span> | <span data-k="5">lifecycle, incl. server manufacturing · (D, pub. 22 Jul 2025)</span><br><span data-k="6">training “as of January 2025, and after 18 months of usage”. also 281,000 m³ of water consumed.</span><br><span data-k="7">▸ **widest boundary here: server manufacturing included**</span> |
| <span data-k="8">**Llama 3.1 family (8B + 70B + 405B)**</span><br><span data-k="9">11,390 t</span> | <span data-k="10">location-based; GPU-hours × 700 W rated power · (D, 2024)</span><br><span data-k="11">final pre-training runs only; development runs excluded. three models summed; the card leaves the family’s power cell blank.</span><br><span data-k="12">▸ **a SUM of three runs; chip-only power, a lower bound on server energy**</span> |
| <span data-k="13">**Llama 3.1 405B**</span><br><span data-k="14">8,930 t</span> | <span data-k="15">location-based; 30.84 M GPU-hours × 700 W rated power · (D, 2024)</span><br><span data-k="16">final pre-training run only. the same runs are reported as 0 t market-based.</span><br><span data-k="17">▸ **chip-only power: a LOWER BOUND on server energy**</span> |
| <span data-k="18">**Gemma 2 family**</span><br><span data-k="19">1,247.61 t</span> | <span data-k="20">TPU energy scaled for facility overhead · (D, 2024)</span><br><span data-k="21">PRE-TRAINING ONLY. excludes the larger teacher model used to train two of the three.</span><br><span data-k="22">▸ **pre-training only; the distillation teacher is not counted**</span> |
| <span data-k="23">**Llama 3.1 family, market-based**</span><br>0 t | <span data-k="24">market-based, after renewable-energy purchases · (D, 2024)</span><br><span data-k="25">the same runs as the 11,390 t above. the Greenhouse Gas Protocol asks for both methods; Meta reported both.</span><br><span data-k="26">▸ **SAME RUNS as the 11,390 t bar — a different accounting method**</span> |

**Nothing in the left-hand column is wrong. The chart beside it still is.**
{: data-k="27"}

**NAIVE ANALYSIS** *— one axis, 5 different boundaries:* bars of 20,400 t, 11,390 t, 8,930 t and 1,247.61 t, and “0 t — the same runs as the 11,390 t bar”, on one axis of tonnes CO₂e from 0 to 20,000.
{: data-k="28"}

**What the order is actually measuring: how wide a boundary each company drew, which carbon accounting method it chose,** and how many runs it added together. Change any one of those and the order changes.
{: data-k="29"}

The tallest bar is not the largest training run — only the largest one DISCLOSED. No developer has published a training energy or emissions figure for GPT-4, GPT-5, any Gemini model, Claude or Grok (as of mid-September 2026). Market-based zeros are standard practice: the Greenhouse Gas Protocol asks companies to report both methods, and Meta did. Showing both is the point, not an accusation. Do not divide any of these by any other, and do not convert them into “N people’s annual footprint” — that sets a one-off total against a yearly flow.
Sources: Meta Llama 3.1 model card (2024); Gemma 2 technical report §3.4 (2024); Mistral AI with Carbone 4 and ADEME, reviewed by Resilio and Hubblo, P69 (22 Jul 2025); Type D — first-party disclosure.
{: .small data-k="30" }

</div>
</div>

---

## Training versus use
{: id="training-versus-use" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 17: what the published splits say about training versus everyday use](/assets/img/posts/2026-09-18-ai-environmental-impact-17.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5.09%;width:26.25%;height:5.74%"></span><span class="sl-r" data-k="1" style="left:3.85%;top:15%;width:72.55%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:3.85%;top:25.74%;width:80.57%;height:3.43%"></span><span class="sl-r" data-k="3" style="left:3.75%;top:33.43%;width:91.82%;height:6.76%"></span><span class="sl-r" data-k="4" style="left:3.85%;top:44.35%;width:87.76%;height:6.85%"></span><span class="sl-r" data-k="5" style="left:3.85%;top:55.56%;width:86.35%;height:3.33%"></span><span class="sl-r" data-k="6" style="left:3.85%;top:63.06%;width:71.88%;height:3.33%"></span><span class="sl-r" data-k="7" style="left:3.75%;top:93.89%;width:43.02%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**Is training or everyday use the bigger cost? The measured splits all predate ChatGPT, and they differ by product.**
{: data-k="1"}

- {: data-k="2"} **Google, all its machine learning, 2019–2021:** roughly **⅗ of the energy went to use and ⅖ to training** (Google's own report).
- {: data-k="3"} **Meta, published 2022:** for a production translation model, **65% use and 35% training**; for its recommendation models, **about even**. Meta's AI *power capacity* was split **10:20:70** across experimentation, training and use (capacity, not energy).
- {: data-k="4"} **Four small open models (0.56–7 billion parameters):** deployment matched the energy of training plus fine-tuning after about **200–590 million uses** (one lab measured both sides, 2024).
- {: data-k="5"} **No company publishes how many times a current chatbot is used**, so no one can compute this ratio for the models you actually use.
- {: data-k="6"} The **"80–90% is inference"** figure that circulates traces to **two 2019 remarks about cost in dollars**, not energy.

Sources: Patterson et al. 2022; Wu et al. 2022 (Meta); Luccioni et al. 2024; NVIDIA and AWS remarks, 2019
{: .small data-k="7" }

</div>
</div>

---

## Water, nationally
{: id="water-nationally" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 18: US data-centre water in 2018 — 513 million m³ consumed, a quarter on site and three-quarters via electricity, and a scarcity-weighted index 2.5× the volume](/assets/img/posts/2026-09-18-ai-environmental-impact-18.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5.09%;width:23.07%;height:5.74%"></span><span class="sl-r" data-k="1" style="left:3.8%;top:15%;width:48.18%;height:3.24%"></span><span class="sl-r" data-k="2" style="left:3.85%;top:23.61%;width:23.44%;height:6.2%"></span><span class="sl-r" data-k="2" style="left:3.75%;top:31.76%;width:27.6%;height:5.28%"></span><span class="sl-r" data-k="3" style="left:35.42%;top:24.44%;width:9.11%;height:5.46%"></span><span class="sl-r" data-k="3" style="left:35.26%;top:31.76%;width:27.66%;height:7.87%"></span><span class="sl-r" data-k="4" style="left:66.77%;top:24.54%;width:6.93%;height:5.28%"></span><span class="sl-r" data-k="4" style="left:66.77%;top:31.76%;width:28.96%;height:10.46%"></span><span class="sl-r" data-k="5" style="left:3.75%;top:45.83%;width:91.98%;height:5.46%"></span><span class="sl-r" data-k="6" style="left:5.62%;top:54.35%;width:88.07%;height:8.8%"></span><span class="sl-r" data-k="7" style="left:3.75%;top:75.19%;width:92.03%;height:5.56%"></span><span class="sl-r" data-k="7" style="left:3.7%;top:82.13%;width:41.15%;height:3.05%"></span><span class="sl-r" data-k="8" style="left:3.75%;top:93.98%;width:48.75%;height:2.41%"></span>
</div>
<div class="sl-txt" markdown="1">

**US data centres, 2018 — the most detailed all-data-centre estimate found**
{: data-k="1"}

**513 million m³**  
water **consumed** in 2018: on site, via electricity, and via water utilities. All data centres, not only AI
{: data-k="2"}

**¼ · ¾**  
**a quarter** used at the buildings, at an assumed typical cooling rate; **three-quarters** consumed generating their electricity, hydropower reservoir evaporation included
{: data-k="3"}

**2.5×**  
weighted by local water scarcity, the footprint **index** is 2.5× the plain volume — 1.29 bn m³ US-equivalent against 513 mn m³ — and the on-site quarter becomes **over 40%** of it. *An index with its own reference point, not litres*
{: data-k="4"}

**2.5 is one of five numbers the authors publish, one for each allocation rule.** Theirs is the "primary purpose" rule for reservoir evaporation. Charge **none** of that evaporation to hydropower and the same model gives **5.1×**; charge **all** of it and it gives **1.6×**. Same data, same year, one decision.
{: data-k="5"}

> *US AI servers, projected: 731–1,125 million m³ a year, averaged over 2024–2030 — that is 0.6–1.0% of what US crop irrigation, power stations and public water supply consume combined. For 2030 alone the same model gives about 0.9–2.0%*, from the authors' own published code, which computes each year before averaging; the paper prints only the average.
> {: data-k="6"}

**Not like for like:** the AI figure counts reservoir evaporation and cooling-tower drain-off; the national total counts neither. **No one has published a scarcity-weighted figure for AI.**  
*All estimates, not meter readings. The national total is a 2010–2020 average.*
{: data-k="7"}

Sources: Siddik, Shehabi & Marston 2021; Xiao et al., Nature Sustainability 2025 and its published code; USGS PP 1894-D
{: .small data-k="8" }

</div>
</div>

---

## Water, where the buildings are
{: id="water-where-the-buildings-are" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 19: three findings from Virginia's legislative audit — 0.2% to 21% at six utilities, under 0.5% of state withdrawals, 83% of data centres no thirstier than a large office building — and The Dalles, Oregon](/assets/img/posts/2026-09-18-ai-environmental-impact-19.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5.09%;width:40.73%;height:5.74%"></span><span class="sl-r" data-k="1" style="left:3.75%;top:14.17%;width:88.54%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:5.68%;top:27.32%;width:12.24%;height:3.8%"></span><span class="sl-r" data-k="2" style="left:5.68%;top:33.33%;width:25.36%;height:5.28%"></span><span class="sl-r" data-k="3" style="left:36.41%;top:27.22%;width:12.5%;height:3.89%"></span><span class="sl-r" data-k="3" style="left:36.41%;top:33.33%;width:25.57%;height:5.28%"></span><span class="sl-r" data-k="4" style="left:67.14%;top:26.94%;width:6.87%;height:4.91%"></span><span class="sl-r" data-k="4" style="left:67.14%;top:33.33%;width:24.43%;height:7.31%"></span><span class="sl-r" data-k="5" style="left:5.62%;top:55.09%;width:26.2%;height:3.15%"></span><span class="sl-r" data-k="6" style="left:5.68%;top:59.07%;width:88.12%;height:5.56%"></span><span class="sl-r" data-k="7" style="left:3.8%;top:80.83%;width:76.67%;height:2.78%"></span><span class="sl-r" data-k="8" style="left:3.75%;top:93.89%;width:37.4%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**The same buildings are 21% of one thing and under 0.5% of another. All three findings come from one legislative audit (Virginia, December 2024).**
{: data-k="1"}

**0.2% – 21%**  
of **total water use at six named water utilities**. That range spans the utilities; it is not an uncertainty band
{: data-k="2"}

**under 0.5%**  
of **Virginia's total water withdrawals** — a total that is about three-quarters water drawn by power plants
{: data-k="3"}

**83%**  
of Virginia's data centres used **no more water than an average large office building** (2023). The other 17% used more
{: data-k="4"}

> **The Dalles, Oregon (population about 16,000)**
> {: data-k="5"}
>
> Google's data-centre campus was billed for **355 million gallons in 2021, 29% of the city's water**. That is Google's oldest campus, cooled by evaporation, with all its workloads counted, in a year before ChatGPT launched. The city sued to keep the figure private, with Google paying its legal costs, then settled and released it (December 2022).
> {: data-k="6"}

*Denominators differ: under 0.5% is of withdrawals, three-quarters of which is power-plant water; the 21% is of one utility's total use; The Dalles is a city total.*
{: data-k="7"}

Sources: JLARC Report 598 (Dec 2024); Virginia DEQ 2024; The Oregonian / RCFP; US Census
{: .small data-k="8" }

</div>
</div>

---

## The water multiplier
{: id="the-water-multiplier" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 20: the water multiplier — coefficient, location, hydropower, withdrawn versus consumed, building versus power station — with a US map of total water per MWh for a hypothetical data centre in each watershed](/assets/img/posts/2026-09-18-ai-environmental-impact-20.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5.09%;width:28.07%;height:5.65%"></span><span class="sl-r" data-k="1" style="left:3.8%;top:14.72%;width:48.8%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:3.8%;top:21.76%;width:56.88%;height:8.06%"></span><span class="sl-r" data-k="3" style="left:3.75%;top:31.48%;width:57.55%;height:13.24%"></span><span class="sl-r" data-k="4" style="left:3.75%;top:46.39%;width:58.02%;height:7.96%"></span><span class="sl-r" data-k="5" style="left:3.8%;top:55.83%;width:57.5%;height:5.65%"></span><span class="sl-r" data-k="6" style="left:3.8%;top:63.15%;width:57.87%;height:5.37%"></span><span class="sl-r" data-k="7" style="left:62.97%;top:70.93%;width:31.61%;height:6.39%"></span><span class="sl-r" data-k="8" style="left:62.97%;top:78.24%;width:32.5%;height:6.48%"></span><span class="sl-r" data-k="9" style="left:62.97%;top:85.46%;width:32.08%;height:4.35%"></span><span class="sl-r" data-k="10" style="left:3.75%;top:93.89%;width:62.08%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**Every "AI uses X litres" figure is electricity × a water coefficient × a location**
{: data-k="1"}

- {: data-k="2"} **The coefficient** — litres of water consumed per kWh of US grid electricity — runs from **1.8 to 7.6** in published values. Much of that spread is one choice: **whether evaporation from hydropower reservoirs counts.** A 2003 government-lab study, as cited, gives **1.8 without hydro and 7.6 with it**. Others in between: 2.18, 3.14, 4.35, about 5.3.
- {: data-k="3"} **The location:** place the same **hypothetical 1 MW data centre** in each of **2,110 US watersheds** and its total water per MWh — building plus electricity — runs from **1.8 to 105.9 m³**, a **59-fold** gap (2018 grid data, modelled). **The paper prints no middle; its supplement has one:** the median watershed is **6.8 m³/MWh** and the middle half run **4.0 to 7.9** — a spread of two, not of fifty-nine. Only **2 of 2,078** watersheds sit at the 1.8 floor, which is the building's flat cooling assumption where the electricity consumes no water. **The 59× is a gap between two extremes, not a spread of observations.**
- {: data-k="4"} **Drop hydropower and the totals move a long way.** In the authors' own supplement the US data-centre water footprint falls **54%** if no reservoir evaporation is charged to hydropower, and rises **70%** if all of it is. A separate 2026 model's off-site water for US hyperscale sites falls **43%** without hydro.
- {: data-k="5"} **Withdrawn versus consumed:** one widely quoted projection for global AI in 2027 is **4.2–6.6 billion m³ withdrawn**, but only **0.38–0.60 billion m³ consumed**.
- {: data-k="6"} **Building versus power station:** of **16.9 mL** per response (GPT-3, US average, modelled), **87%** evaporates generating the electricity. Google's **0.26 mL** counts **only the building**.

<span data-k="7">**That bullet as a map.** Figure 4, panel A of the same paper: total water per MWh for one *hypothetical* 1 MW data centre placed in each of the 2,110 US subbasins — **not real facilities**. 2018, m³/MWh.</span>  
<span data-k="8">**The colour scale runs 1.8 to 106 and the legend prints nothing in between**, so almost the whole country sits in its low end: the median watershed is 6.8. The red is mostly **hydropower reservoir evaporation** under the paper's allocation rule.</span>  
<span data-k="9">*Shown for the size of the spread, not as a source of values. Siddik, Shehabi & Marston 2021, CC BY 4.0.*</span>

Sources: Torcellini et al. 2003, as cited; Siddik, Shehabi & Marston 2021 and its supplement (CC BY 4.0); Guidi & Dominici 2026; Li et al. 2025; Google 2025
{: .small data-k="10" }

</div>
</div>

---

## Electricity, where someone reads a meter
{: id="electricity-where-someone-reads-a-meter" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 21: four national series that meter data-centre electricity — Ireland 23%, Netherlands 4.6%, Great Britain about 2%, Norway 2.5%](/assets/img/posts/2026-09-18-ai-environmental-impact-21.png)<span class="sl-r" data-k="t" style="left:3.8%;top:5.09%;width:54.37%;height:5.74%"></span><span class="sl-r" data-k="1" style="left:3.8%;top:15%;width:63.49%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:4.32%;top:23.61%;width:4.12%;height:2.41%"></span><span class="sl-r" data-k="3" style="left:27.19%;top:23.61%;width:6.82%;height:2.41%"></span><span class="sl-r" data-k="4" style="left:50.05%;top:23.61%;width:7.03%;height:2.41%"></span><span class="sl-r" data-k="5" style="left:72.97%;top:23.7%;width:4.53%;height:2.69%"></span><span class="sl-r" data-k="6" style="left:4.27%;top:27.96%;width:16.93%;height:2.87%"></span><span class="sl-r" data-k="7" style="left:27.13%;top:27.96%;width:14.43%;height:2.87%"></span><span class="sl-r" data-k="8" style="left:50.05%;top:27.96%;width:21.82%;height:5.46%"></span><span class="sl-r" data-k="9" style="left:72.92%;top:27.96%;width:16.25%;height:2.87%"></span><span class="sl-r" data-k="10" style="left:3.8%;top:40.83%;width:92.08%;height:11.57%"></span><span class="sl-r" data-k="11" style="left:3.8%;top:54.44%;width:89.48%;height:8.7%"></span><span class="sl-r" data-k="12" style="left:3.85%;top:65.19%;width:65.05%;height:2.96%"></span><span class="sl-r" data-k="13" style="left:3.75%;top:93.98%;width:38.49%;height:2.41%"></span>
</div>
<div class="sl-txt" markdown="1">

**Four national series that meter data-centre electricity. None of them can say how much of it is AI.**
{: data-k="1"}

| **Ireland** | **Netherlands** | **Great Britain** | **Norway** |
|---|---|---|---|
| **23%** of metered electricity (2025) | **4.6%** of consumption (2024) | **~2%** of grid consumption (2024); leaves out companies' own in-house data centres | **2.5%** of net consumption (2025) |
{: data-keys="2 3 4 5 6 7 8 9"}

- {: data-k="10"} **Ireland is roughly ten times Great Britain on same-year figures (2024) — the gap is real, and its size is not settled.** Ireland **22%** of metered electricity against Great Britain **2%** of electricity taken from the grid. **The two countries do not count the same object:** the British figures cover only data centres serving outside customers and leave out companies' own in-house facilities. Britain's own department prints a rival figure for its own country — **4.1 TWh** against the grid operator's **7.6 TWh** for 2023 — which would put Great Britain nearer 3% and the gap nearer **7×**. On Ireland's own base, **homes are 28%**.
- {: data-k="11"} **Growth is real in every series.** In Ireland about **two-thirds (63%)** of the 2015–2025 rise in data-centre electricity had happened by 2022, the year ChatGPT launched (30 November). Growth since has averaged **~800 GWh a year**, faster than the 2015–2022 average of ~580 — even though new data-centre grid connections around Dublin were largely paused from 2021–22 (the regulator replaced the pause with conditional rules in December 2025).
- {: data-k="12"} **The world figure is a model, not a meter:** about **1.5–1.7%** for all data centres (2025). **There is no metered US series at all.**

Sources: CSO Ireland 2026; CBS Netherlands; DESNZ/National Grid; Statistics Norway; IEA 2026
{: .small data-k="13" }

</div>
</div>

---

## The United States: modelled, not metered
{: id="the-united-states-modelled-not-metered" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 22: the most-cited US figures are models — Lawrence Berkeley National Laboratory and EPRI — and how a shipment model is built](/assets/img/posts/2026-09-18-ai-environmental-impact-22.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5.09%;width:54.58%;height:5.28%"></span><span class="sl-r" data-k="1" style="left:3.75%;top:15%;width:49.69%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:3.8%;top:25.65%;width:91.15%;height:6.85%"></span><span class="sl-r" data-k="3" style="left:3.85%;top:36.2%;width:91.98%;height:6.76%"></span><span class="sl-r" data-k="4" style="left:3.8%;top:46.76%;width:89.12%;height:6.76%"></span><span class="sl-r" data-k="5" style="left:3.85%;top:57.22%;width:91.41%;height:6.76%"></span><span class="sl-r" data-k="6" style="left:3.85%;top:67.78%;width:71.67%;height:3.33%"></span><span class="sl-r" data-k="7" style="left:3.75%;top:93.98%;width:28.07%;height:2.41%"></span>
</div>
<div class="sl-txt" markdown="1">

**The most-cited US figures are models, built from records you cannot inspect**
{: data-k="1"}

- {: data-k="2"} **Lawrence Berkeley National Laboratory** (a Department of Energy lab): data centres used **176 TWh (4.4%)** of US electricity in 2023 and **192 TWh (4.7% of consumption)** in 2024 — all data centres, not only AI. *Built from purchased records of servers sold.*
- {: data-k="3"} **The Electric Power Research Institute** (funded mainly by utilities): data centres are **4–5% of US *generation*** now, and its 2030 projections are **60% higher** than in its 2024 report. *Built from state-level data on operating capacity, construction and announced projects.*
- {: data-k="4"} **How a shipment model is built:** hardware sold → assumed installed → assumed power → assumed utilisation → assumed hours → assumed overhead. The Berkeley lab says its 2024 report's utilisation assumptions had "**little-to-no measured data** available to verify them."
- {: data-k="5"} **These can err in either direction.** Sales records count chips sold but not yet switched on (too high) and miss custom chips nobody sells (too low). Project pipelines can include projects that never get built.
- {: data-k="6"} **The US has no metered national series.** The federal statistics agency began pilot surveys of data centres in 2026.

Sources: LBNL 2024 and 2025 Update; EPRI 2024 and 2026; EIA 2026
{: .small data-k="7" }

</div>
</div>

---

## Rated power cuts both ways
{: id="rated-power-cuts-both-ways" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 23: rated power — estimates built on a whole server's rating run high, estimates built on the chips' rating run low](/assets/img/posts/2026-09-18-ai-environmental-impact-23.png)<span class="sl-r" data-k="t" style="left:3.8%;top:5.09%;width:36.72%;height:5.74%"></span><span class="sl-r" data-k="1" style="left:3.7%;top:14.26%;width:75.31%;height:3.24%"></span><span class="sl-r" data-k="2" style="left:5.62%;top:26.3%;width:16.3%;height:3.24%"></span><span class="sl-r" data-k="2" style="left:5.68%;top:30.83%;width:41.25%;height:8.15%"></span><span class="sl-r" data-k="3" style="left:52.13%;top:26.3%;width:14.06%;height:3.24%"></span><span class="sl-r" data-k="3" style="left:52.13%;top:30.83%;width:40.52%;height:10.83%"></span><span class="sl-r" data-k="4" style="left:3.8%;top:55.65%;width:70.42%;height:3.15%"></span><span class="sl-r" data-k="4" style="left:3.75%;top:60.46%;width:57.08%;height:3.15%"></span><span class="sl-r" data-k="5" style="left:3.8%;top:74.72%;width:59.38%;height:2.87%"></span><span class="sl-r" data-k="6" style="left:3.75%;top:93.89%;width:30.21%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

***A rating is what hardware could draw. Whether an estimate built on a rating runs high or low depends on which rating it used.***
{: data-k="1"}

**Whole server → runs *high***  
One 8-GPU H100 server peaked at **8.4 kW** against its **10.2 kW** rating. Under heavy training loads, servers averaged at most **76%** of that rating. Estimates that multiply the *server's* rating by hours run high.
{: data-k="2"}

**Chips only → runs *low***  
The same server's eight GPUs are rated **5.6 kW** in total — less than the 8.4 kW the whole server drew, because processors, memory and networking draw power too. The lab that measured this treats such estimates as a **lower bound**. Meta's Llama figures use this method.
{: data-k="3"}

**How far off:** on the lab's workloads, server-rating estimates erred by about **37%** and GPU-rating estimates by about **27%** (2025).  
**A lightly loaded service:** GPUs on BLOOM's public demo drew **78–171 W** against a 400 W rating (2022).
{: data-k="4"}

*One lab, one server type (8×H100), two papers with overlapping authors. Cooling and building overhead are not included.*
{: data-k="5"}

Sources: Newkirk et al. 2025; MLPerf Power; BLOOM (Luccioni et al.) 2022
{: .small data-k="6" }

</div>
</div>

---

## The reasonable worst case is two numbers
{: id="the-reasonable-worst-case-is-two-numbers" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 24: the reasonable worst case — modelled national and world shares for 2030 beside measured local shares where data centres cluster](/assets/img/posts/2026-09-18-ai-environmental-impact-24.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5.09%;width:55.78%;height:4.63%"></span><span class="sl-r" data-k="1" style="left:3.8%;top:15%;width:59.32%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:4.32%;top:23.61%;width:22.81%;height:2.78%"></span><span class="sl-r" data-k="3" style="left:53.75%;top:23.61%;width:25.16%;height:2.78%"></span><span class="sl-r" data-k="4" style="left:4.32%;top:28.06%;width:47.4%;height:5.28%"></span><span class="sl-r" data-k="5" style="left:53.8%;top:28.06%;width:36.25%;height:2.78%"></span><span class="sl-r" data-k="6" style="left:4.27%;top:34.91%;width:48.96%;height:5.28%"></span><span class="sl-r" data-k="7" style="left:53.8%;top:34.91%;width:24.06%;height:2.78%"></span><span class="sl-r" data-k="8" style="left:4.32%;top:41.76%;width:48.18%;height:5.28%"></span><span class="sl-r" data-k="9" style="left:53.8%;top:41.76%;width:38.18%;height:4.91%"></span><span class="sl-r" data-k="10" style="left:3.8%;top:62.96%;width:90.47%;height:5.93%"></span><span class="sl-r" data-k="11" style="left:3.8%;top:70.28%;width:91.46%;height:5.83%"></span><span class="sl-r" data-k="12" style="left:3.8%;top:85.46%;width:74.53%;height:2.87%"></span><span class="sl-r" data-k="13" style="left:3.75%;top:93.98%;width:37.66%;height:2.41%"></span>
</div>
<div class="sl-txt" markdown="1">

***Rule: take the top of each source's own published range. Never multiply worst cases together.***
{: data-k="1"}

| **Nationally and worldwide, 2030 — modelled** | **Where data centres cluster, recently — measured** |
|---|---|
| **US:** up to **15%** of electricity consumption (Berkeley lab) or **17%** of generation (EPRI). All data centres, not only AI | **29%** of one Oregon city's water (2021; one Google campus, all its workloads) |
| **World:** about **2.8%** for all data centres and **1.4%** for AI-focused facilities (IEA base case; its higher case is published for 2035, not 2030) | **21%** of one Virginia utility's water use (2024 audit) |
| **US water, AI servers:** up to **~1%** of irrigation, power-station and public-supply consumption as a 2024–2030 average, and **~2%** in 2030 itself (from the authors' code) | **23%** of Ireland's metered electricity (2025): a whole country, but one where data centres cluster |
{: data-keys="2 3 4 5 6 7 8 9"}

- {: data-k="10"} **Share and amount tell different stories.** On one pair of IEA totals the world share goes from ~1.7% to ~2.8% (**×1.64**), while data-centre electricity itself goes from 485 to ~950 TWh (**×1.96**). The share grows more slowly because world use grows too.
- {: data-k="11"} **No figure for 2050 is given.** The published envelopes run 25 years out — one rests on a fitted relationship whose estimated range includes both signs — and this work has no world electricity total for that year to divide by.

***The best-measured numbers are the local ones, and they are the least transferable. Certainty and representativeness run in opposite directions.***
{: data-k="12"}

Sources: LBNL 2025 Update; EPRI 2026; IEA 2026; Xiao et al. 2025 + code; JLARC; CSO Ireland
{: .small data-k="13" }

</div>
</div>

---

## What nobody measures
{: id="what-nobody-measures" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 25: what nobody measures, and one new exception — a satellite-based estimate of nitrogen oxides from the gas-turbine plant in Southaven, Mississippi](/assets/img/posts/2026-09-18-ai-environmental-impact-25.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5.09%;width:31.35%;height:5.74%"></span><span class="sl-r" data-k="1" style="left:3.75%;top:15%;width:43.54%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:3.85%;top:22.59%;width:53.18%;height:2.87%"></span><span class="sl-r" data-k="3" style="left:3.85%;top:26.67%;width:49.58%;height:2.87%"></span><span class="sl-r" data-k="4" style="left:3.85%;top:30.74%;width:59.79%;height:2.87%"></span><span class="sl-r" data-k="5" style="left:3.8%;top:34.72%;width:90.52%;height:5.65%"></span><span class="sl-r" data-k="6" style="left:3.85%;top:41.57%;width:74.17%;height:2.87%"></span><span class="sl-r" data-k="7" style="left:5.62%;top:54.82%;width:87.81%;height:5.55%"></span><span class="sl-r" data-k="8" style="left:5.68%;top:64.44%;width:85.57%;height:5.28%"></span><span class="sl-r" data-k="9" style="left:5.62%;top:70.28%;width:84.38%;height:5.19%"></span><span class="sl-r" data-k="10" style="left:5.73%;top:76.02%;width:82.03%;height:2.68%"></span><span class="sl-r" data-k="11" style="left:5.62%;top:79.26%;width:88.39%;height:5.09%"></span><span class="sl-r" data-k="12" style="left:3.75%;top:93.89%;width:57.29%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**The thing everyone argues about is the thing least often measured**
{: data-k="1"}

- {: data-k="2"} **No national metering system separates AI** from other data-centre use — all four metered series say so.
- {: data-k="3"} As of mid-2024, **1 of 13** major AI chip buyers had ever disclosed the scale of its AI electricity use.
- {: data-k="4"} **None of Google, Microsoft, Amazon or Meta splits AI from other workloads** in its environmental reports (2025–26).
- {: data-k="5"} **No one outside the companies has measured a query to the closed services most students use** (ChatGPT, Gemini, Claude). Independent labs do now measure large *open* models, GPU energy only (46 models, January 2026).
- {: data-k="6"} The EU's mandatory register covers **36%** of the EU's estimated data centres. The first US government pilot surveys (2026) **do not ask about water**.

> **One new exception — a preprint, one site, 2026.** Satellite data were used to estimate **~730 kg/h** of nitrogen oxides (the mean of eleven two-week estimates, March to mid-August 2026) from the gas-turbine plant in Southaven, Mississippi, built to power SpaceXAI's nearby Colossus 2 data centre.
> {: data-k="7"}
>
> - {: data-k="8"} **Start with the plant next door.** The Tennessee Valley Authority's combined-cycle plant **1.5 km away reported 21 ± 3 kg/h on its own stack monitors** over an overlapping window. Same pollutant, same air, both period averages.
> - {: data-k="9"} The authors also put their estimate at **about 16×** the **~47 kg/h** in the site's March 2026 permit. That 47 is the **sum of per-turbine hourly caps for 41 permanent, pollution-controlled turbines all running at once** — a ceiling on equipment that had not been built, not a rate anything emitted.
> - {: data-k="10"} What was running: **up to 69 temporary turbines**, without air permits, under a state exemption that a federal lawsuit disputes. How many had pollution controls is also disputed.
> - {: data-k="11"} *The method was calibrated on four other power plants, and it cannot detect emissions as low as the permitted level.* **These emissions are behind the meter: they appear in no grid-electricity statistic, so no national share on the earlier slides can see them.**

Sources: Masanet, Lei & Koomey 2024; ML.ENERGY 2026; EC DG ENER 2025; EIA 2026; Gauld et al. 2026 (preprint); MDEQ permit 0680-00119
{: .small data-k="12" }

</div>
</div>

---

## Air: two sites, two kinds of document
{: id="air-two-sites-two-kinds-of-document" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 26: two Memphis-area sites — a permit at Colossus 1 in South Memphis, a satellite-based estimate at Colossus 2's power plant in Southaven — with an aerial photograph of the Memphis site](/assets/img/posts/2026-09-18-ai-environmental-impact-26.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5%;width:48.75%;height:5.37%"></span><span class="sl-r" data-k="1" style="left:3.75%;top:13.43%;width:89.79%;height:6.02%"></span><span class="sl-r" data-k="2" style="left:5.26%;top:23.06%;width:22.81%;height:2.96%"></span><span class="sl-r" data-k="3" style="left:5.26%;top:26.57%;width:19.22%;height:2.59%"></span><span class="sl-r" data-k="4" style="left:5.62%;top:30.09%;width:23.91%;height:9.91%"></span><span class="sl-r" data-k="5" style="left:5.62%;top:41.11%;width:24.63%;height:8.24%"></span><span class="sl-r" data-k="6" style="left:5.68%;top:50.09%;width:20.78%;height:4.35%"></span><span class="sl-r" data-k="7" style="left:30.73%;top:50%;width:16.51%;height:8.98%"></span><span class="sl-r" data-k="8" style="left:52.13%;top:23.06%;width:27.92%;height:2.96%"></span><span class="sl-r" data-k="9" style="left:52.13%;top:26.57%;width:23.07%;height:2.59%"></span><span class="sl-r" data-k="10" style="left:52.5%;top:30.09%;width:41.09%;height:9.17%"></span><span class="sl-r" data-k="11" style="left:52.5%;top:40%;width:40.62%;height:9.26%"></span><span class="sl-r" data-k="12" style="left:52.5%;top:50%;width:40.21%;height:6.94%"></span><span class="sl-r" data-k="13" style="left:52.5%;top:57.78%;width:41.04%;height:7.04%"></span><span class="sl-r" data-k="14" style="left:5.62%;top:68.24%;width:86.15%;height:8.89%"></span><span class="sl-r" data-k="15" style="left:3.75%;top:81.94%;width:87.45%;height:5.19%"></span><span class="sl-r" data-k="16" style="left:3.8%;top:87.96%;width:90.37%;height:4.44%"></span><span class="sl-r" data-k="17" style="left:3.75%;top:93.89%;width:58.49%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**SpaceXAI (xAI until Feb 2026) has run gas turbines at two sites near Memphis. One has a permit you can read. One has a satellite-based estimate. Neither alone tells you what the air received.**
{: data-k="1"}

### Colossus 1 — South Memphis, Tennessee
{: id="colossus-1--south-memphis-tennessee" data-k="2"}

*a permit: a legal ceiling, not a measurement*
{: data-k="3"}

- {: data-k="4"} The county's evaluation (March 2025) of an application for **15 turbines**, rated 16.48 MW each, caps nitrogen oxides at **87 short tons a year** — a **legal ceiling, not a measurement**, which makes the plant a "synthetic minor" source below federal major-source thresholds.
- {: data-k="5"} **Up to 35 turbines** were at the site in April 2025, before the permit was issued (35 is the site total, not 35 extra), **running under a claimed federal "nonroad engine" exemption**: the county accepted it, the Southern Environmental Law Center disputed it.
- {: data-k="6"} The county board **dismissed an appeal as moot, 6–1** (December 2025), after the temporary turbines had left.

*Photo caption:* xAI's Memphis site from the air, **31 March 2025** — three months before the permit was issued. Photograph **Steve Jones**; flight by **Southwings for the Southern Environmental Law Center**, which appealed the permit. A daylight aerial: the camera recorded equipment, not emissions.
{: .small data-k="7" }

### Colossus 2's power plant — Southaven, Mississippi
{: id="colossus-2s-power-plant--southaven-mississippi" data-k="8"}

*an estimate, against a permit for different equipment*
{: data-k="9"}

- {: data-k="10"} **Start with the plant next door.** Satellite data put the turbine site at **~730 kg/h** of NOx — the mean of eleven two-week estimates, March to mid-August 2026, spread ±185, no median published. The Tennessee Valley Authority's combined-cycle plant **1.5 km away reported 21 ± 3 kg/h on its own stack monitors** over an overlapping window. Same pollutant, same air, both period averages.
- {: data-k="11"} The state permit (March 2026) covers **41 permanent turbines with pollution controls** (1.24 GW). Their per-turbine short-term limits, summed as though all 41 ran at the limit at once, come to about **47 kg/h**. The preprint's authors put their estimate at **about 16×** that sum — a ratio of an observed rate to a legal ceiling, not of two rates.
- {: data-k="12"} **But the 41 permanent turbines weren't running yet.** Up to **69 temporary, trailer-mounted turbines** were, without air permits, under the state's "mobile and temporary" exemption. A federal lawsuit disputes it; the US Justice Department has intervened on the company's side.
- {: data-k="13"} **How many had pollution controls is disputed.** The researchers, citing the state's order, say 14 of 69. The company says all its mobile turbines have "advanced emission control technologies", without giving a count.

> **The legal record, at both sites.** Those retirement dates exist because the exemption ran **12 months from arrival** (Aug 2025 → Aug 2026): an MDEQ agreed order of **30 July 2026** let **13 turbines** run past the deadline, three by up to **five months**, at the company's request after supply-chain delays on the 41 permanent turbines. **No penalty is reported.** **And neither site produced a ruling on the question itself** — whether a trailer-mounted turbine is a stationary source. Memphis: the turbines left, then the appeal was dismissed as moot; the removal defeated the challenge rather than resulting from it. Southaven: the August 2026 injunction hearing was postponed, the Justice Department intervened (June 2026) and moved to dismiss citing national security, and retirement proceeds on a negotiated schedule.
> {: data-k="14"}

**And none of it appears in any national number.** Both sites generate their own power **behind the meter**, so every national and world share earlier in this talk is blind to these emissions by construction. A national average is not an instrument for a local question.
{: data-k="15"}

***What this shows:*** *a permit caps only the equipment it names; state records show what ran; only a measurement could estimate what it emitted; and the question is undecided at both sites — which denies the alarmed reading a finding of illegality and the reassuring reading a finding of compliance. The satellite study is a preprint at a single site, calibrated on four other power plants, and its method cannot detect emissions as low as the permitted level.*
{: data-k="16"}

Sources: Shelby County 01156-01PC; MDEQ 0680-00119 and agreed order 30 Jul 2026; Gauld et al. 2026 (preprint); Mississippi Today 31 Jul 2026
{: .small data-k="17" }

</div>
</div>

---

## Two famous numbers, and what happened to them
{: id="two-famous-numbers-and-what-happened-to-them" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 27: two famous numbers — the 1999 claim that the internet uses 8% of US electricity, and the 2019 table row headed "Training one model"](/assets/img/posts/2026-09-18-ai-environmental-impact-27.png)<span class="sl-r" data-k="t" style="left:3.75%;top:5%;width:66.77%;height:5.74%"></span><span class="sl-r" data-k="1" style="left:3.85%;top:15%;width:27.03%;height:3.52%"></span><span class="sl-r" data-k="2" style="left:5.73%;top:24.72%;width:26.82%;height:3.15%"></span><span class="sl-r" data-k="3" style="left:5.62%;top:29.63%;width:39.48%;height:8.89%"></span><span class="sl-r" data-k="4" style="left:5.68%;top:41.2%;width:39.9%;height:17.69%"></span><span class="sl-r" data-k="5" style="left:5.73%;top:61.76%;width:16.51%;height:2.59%"></span><span class="sl-r" data-k="6" style="left:52.55%;top:24.72%;width:28.02%;height:3.15%"></span><span class="sl-r" data-k="7" style="left:52.5%;top:29.44%;width:39.12%;height:10.46%"></span><span class="sl-r" data-k="8" style="left:52.5%;top:41.76%;width:40.57%;height:13.52%"></span><span class="sl-r" data-k="9" style="left:52.5%;top:56.85%;width:39.32%;height:8.06%"></span><span class="sl-r" data-k="10" style="left:52.55%;top:66.48%;width:40.73%;height:10.74%"></span><span class="sl-r" data-k="11" style="left:3.75%;top:93.89%;width:48.23%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**Numbers lose their qualifiers in transit**
{: data-k="1"}

### 1999: "The internet uses 8% of US electricity"
{: id="1999-the-internet-uses-8-of-us-electricity" data-k="2"}

- {: data-k="3"} …and all office, telecom and network equipment 13%, heading for **half** within a decade. *(Mills & Huber, Forbes; the underlying report was funded through a coal-industry group.)*
- {: data-k="4"} **Berkeley Lab (Koomey, 2000)** put **all** office, telecom and network equipment at **2.6%** of US electricity, or **3.2%** including the power to manufacture it — "about a factor of four lower than Mills' estimate for the electricity demand of 'the digital economy'." Correcting **Mills's own** arithmetic cut his internet figure about **8×**, and Berkeley would not publish an internet-only figure at all.
- {: data-k="5"} **The 1999 claim overstated.**

### 2019: a table row headed "Training one model"
{: id="2019-a-table-row-headed-training-one-model" data-k="6"}

- {: data-k="7"} It gave **626,155 lb CO₂e** (≈284 t) for an automated search over thousands of candidate designs, beside a car's lifetime emissions (126,000 lb). A tweet of that table spread as "five cars". The headline: "Training a single AI model **can** emit as much carbon as five cars in their lifetimes."
- {: data-k="8"} **Google researchers (2021)** — a group that includes the authors of the searched-for model — put the same search at **3.2 t**: **88×** lower, stated conditionally, "for energy-efficient organizations like Google". **18.7×** of that is like-for-like, correcting only how the search had been read; the rest is newer chips and a better-run building.
- {: data-k="9"} **What a large 2024 run cost, as disclosed.** Meta's Llama 3.1 405B pre-training: **8,930 t CO₂e** location-based, **0 t** market-based. The 8B model: **420 t**. The three together: **11,390 t**. Final training runs only.
- {: data-k="10"} **Both lost a qualifier.** The 2019 figure overstated the search it described, and was never a figure for training one model. Read that way it understates today's largest disclosed runs — but **by no stateable multiple**: its denominator is the number this slide has just reported as 88× too high.

Sources: Mills & Huber 1999; Koomey, LBNL-46509 (2000); Strubell et al. 2019; Patterson et al. 2021; Meta model cards
{: .small data-k="11" }

</div>
</div>

---

## Beyond the power bill: buildings and chips
{: id="beyond-the-power-bill-buildings-and-chips" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 28: what most published numbers leave out — embodied emissions from making chips and buildings, and the water used by chip factories](/assets/img/posts/2026-09-18-ai-environmental-impact-28.png)<span class="sl-r" data-k="t" style="left:3.8%;top:5.09%;width:55.89%;height:5.74%"></span><span class="sl-r" data-k="1" style="left:3.85%;top:15%;width:47.14%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:3.85%;top:25.56%;width:90.73%;height:9.81%"></span><span class="sl-r" data-k="3" style="left:3.8%;top:38.33%;width:91.15%;height:6.02%"></span><span class="sl-r" data-k="4" style="left:3.85%;top:47.59%;width:56.56%;height:3.33%"></span><span class="sl-r" data-k="5" style="left:3.8%;top:53.89%;width:91.93%;height:9.63%"></span><span class="sl-r" data-k="6" style="left:3.75%;top:66.39%;width:90%;height:6.2%"></span><span class="sl-r" data-k="7" style="left:3.8%;top:84.17%;width:38.54%;height:2.78%"></span><span class="sl-r" data-k="8" style="left:3.75%;top:93.89%;width:44.43%;height:2.5%"></span>
</div>
<div class="sl-txt" markdown="1">

**Most published numbers count only the electricity used to run the chips**
{: data-k="1"}

- {: data-k="2"} **Making the chips and building the data centres ("embodied" emissions):** about **30%** of Meta's AI tasks' emissions, counted on the local grid average (2022); **more than half** of large AI data centres' emissions — **50–82% of data-centre emissions** in its one numeric statement — in a 2026 review that states no carbon basis and whose own boundary figure covers **server manufacturing only**.
- {: data-k="3"} **In BLOOM's fully counted training run,** hardware was **22%**, on France's very clean grid. On a grid of about 390 g CO₂e/kWh the same hardware would be about **4%**.
- {: data-k="4"} **NVIDIA's first published figure (2025):** **1,312 kg CO₂e** to manufacture one 8-GPU H100 board.
- {: data-k="5"} **A trade-off:** cutting a data centre's water use and cutting its carbon "can be negatively coupled … in some cases" (2026 review). Microsoft said in December 2024 that its new designs will avoid the need for more than **125 million litres of water a year** per data centre, with a "nominal increase" in energy use; pilots begin in 2026.
- {: data-k="6"} **A chip factory** "can use" about **10 million gallons (38 million litres) of ultra-pure water a day** (World Economic Forum, 2024). That is water **drawn**, not water consumed.

*None of these is included in the electricity or water shares on the earlier slides.*
{: data-k="7"}

Sources: Wu et al. 2022 (Meta); Chien et al. 2026; BLOOM 2023; NVIDIA 2025; Microsoft Dec 2024; WEF 2024
{: .small data-k="8" }

</div>
</div>

---

## How to check any number yourself
{: id="how-to-check-any-number-yourself" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 29: four questions for checking any number](/assets/img/posts/2026-09-18-ai-environmental-impact-29.png)<span class="sl-r" data-k="t" style="left:5.73%;top:12.13%;width:55.78%;height:6.85%"></span><span class="sl-r" data-k="1" style="left:11.98%;top:20.74%;width:20.83%;height:3.24%"></span><span class="sl-r" data-k="1" style="left:12.08%;top:24.63%;width:67.97%;height:2.78%"></span><span class="sl-r" data-k="1" style="left:7.45%;top:22.31%;width:1.61%;height:3.43%"></span><span class="sl-r" data-k="2" style="left:11.98%;top:36.11%;width:61.72%;height:3.24%"></span><span class="sl-r" data-k="2" style="left:11.98%;top:40%;width:48.28%;height:2.78%"></span><span class="sl-r" data-k="2" style="left:7.4%;top:37.59%;width:1.67%;height:3.43%"></span><span class="sl-r" data-k="3" style="left:11.98%;top:51.39%;width:23.96%;height:3.24%"></span><span class="sl-r" data-k="3" style="left:11.98%;top:55.37%;width:81.82%;height:5.28%"></span><span class="sl-r" data-k="3" style="left:7.34%;top:52.96%;width:1.77%;height:3.52%"></span><span class="sl-r" data-k="4" style="left:11.98%;top:66.76%;width:42.34%;height:3.24%"></span><span class="sl-r" data-k="4" style="left:11.98%;top:70.65%;width:65.1%;height:2.78%"></span><span class="sl-r" data-k="4" style="left:7.29%;top:68.24%;width:1.88%;height:3.43%"></span><span class="sl-r" data-k="5" style="left:5.73%;top:85.19%;width:51.04%;height:3.7%"></span>
</div>
<div class="sl-txt" markdown="1">

1. {: data-k="1"} **A share of what, and which year?**  
   Energy, capacity, water *withdrawn* or water *consumed*? All data centres, or AI? Are the top and bottom of the fraction from the same year?
2. {: data-k="2"} **What did someone physically record, and how many assumptions stand between that and the claim?**  
   A meter reading, a satellite column, a permit application, a sales record — then every step after it.
3. {: data-k="3"} **Which way can the method be wrong?**  
   A permit caps only the equipment it names. A connection request is not a building. A company disclosure chooses its own boundary. A model built on sales records can err either way.
4. {: data-k="4"} **And when a number is a multiple, what kind of thing is on each side?**  
   A mean, a median, a total, a smallest, a largest, or a legal limit. If the source publishes no middle, the multiple is not a measurement.

**If a number has no base, no year or no boundary, it isn't finished yet.**
{: data-k="5"}

</div>
</div>

---

## Two of these are not mine
{: id="two-of-these-are-not-mine" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 30: the three cards again — Provenance, Substitution, Environment — with the first two highlighted](/assets/img/posts/2026-09-18-ai-environmental-impact-30.png)<span class="sl-r" data-k="t" style="left:4.12%;top:8.43%;width:41.67%;height:5.46%"></span><span class="sl-r" data-k="1" style="left:5.88%;top:19.72%;width:10.31%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:37.03%;top:19.72%;width:10.63%;height:3.33%"></span><span class="sl-r" data-k="3" style="left:68.33%;top:19.72%;width:11.25%;height:3.33%"></span><span class="sl-r" data-k="4" style="left:5.88%;top:24.63%;width:13.07%;height:3.05%"></span><span class="sl-r" data-k="5" style="left:37.03%;top:24.63%;width:19.95%;height:3.05%"></span><span class="sl-r" data-k="6" style="left:68.23%;top:24.63%;width:21.98%;height:3.05%"></span><span class="sl-r" data-k="7" style="left:8.91%;top:30.74%;width:7.66%;height:2.96%"></span><span class="sl-r" data-k="8" style="left:8.91%;top:33.7%;width:4.95%;height:2.96%"></span><span class="sl-r" data-k="9" style="left:8.96%;top:36.57%;width:3.7%;height:2.5%"></span><span class="sl-r" data-k="10" style="left:8.91%;top:39.54%;width:3.59%;height:2.5%"></span><span class="sl-r" data-k="11" style="left:40.16%;top:30.74%;width:14.74%;height:2.96%"></span><span class="sl-r" data-k="12" style="left:40.16%;top:33.7%;width:22.24%;height:2.5%"></span><span class="sl-r" data-k="13" style="left:40.1%;top:36.57%;width:8.75%;height:2.96%"></span><span class="sl-r" data-k="14" style="left:71.35%;top:31.11%;width:4.27%;height:2.59%"></span><span class="sl-r" data-k="15" style="left:71.35%;top:33.7%;width:9.48%;height:2.96%"></span><span class="sl-r" data-k="16" style="left:71.3%;top:36.76%;width:5.99%;height:2.32%"></span><span class="sl-r" data-k="17" style="left:71.41%;top:39.54%;width:5.36%;height:2.96%"></span><span class="sl-r" data-k="18" style="left:4.22%;top:51.2%;width:21.04%;height:2.68%"></span><span class="sl-r" data-k="19" style="left:6.41%;top:68.33%;width:85.78%;height:6.76%"></span><span class="sl-r" data-k="20" style="left:6.35%;top:78.06%;width:72.55%;height:3.52%"></span>
</div>
<div class="sl-txt" markdown="1">

| Provenance | Substitution | Environment |
|---|---|---|
| *the end of attribution* | *replacement and its consequences* | *sudden industrial scaling and its costs* |
| <span data-k="7">artist images</span><br><span data-k="8">writings</span><br><span data-k="9">music</span><br><span data-k="10">video</span> | <span data-k="11">social media manipulation</span><br><span data-k="12">artists and content-creators out of work</span><br><span data-k="13">AI content slop</span> | <span data-k="14">energy</span><br><span data-k="15">carbon footprint</span><br><span data-k="16">water use</span><br><span data-k="17">pollution</span> |
{: data-keys="1 2 3 4 5 6 - - -"}

*There are others I haven’t studied.*
{: data-k="18"}

> On the first two I can only speak to what I have seen with undergraduates — and the objections run strong. For some of them strong enough that raising the subject at all shuts the conversation down.
> {: data-k="19"}
>
> All three of these matter to them. We have to start somewhere, and this is the one I can put numbers on.
> {: data-k="20"}

</div>
</div>

---

## Since this WILL come up…
{: id="since-this-will-come-up" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 31: the AGI question, with film stills from The Matrix and 2001: A Space Odyssey](/assets/img/posts/2026-09-18-ai-environmental-impact-31.png)<span class="sl-r" data-k="t" style="left:4.22%;top:8.43%;width:40.68%;height:6.57%"></span><span class="sl-r" data-k="1" style="left:4.12%;top:16.57%;width:51.87%;height:7.5%"></span><span class="sl-r" data-k="2" style="left:5.73%;top:28.43%;width:35.1%;height:3.33%"></span><span class="sl-r" data-k="3" style="left:5.68%;top:32.13%;width:50.94%;height:11.48%"></span><span class="sl-r" data-k="4" style="left:4.22%;top:48.15%;width:16.2%;height:3.33%"></span><span class="sl-r" data-k="4" style="left:4.17%;top:51.57%;width:54.22%;height:5.93%"></span><span class="sl-r" data-k="5" style="left:4.17%;top:63.89%;width:21.56%;height:3.33%"></span><span class="sl-r" data-k="5" style="left:4.17%;top:67.31%;width:54.22%;height:8.61%"></span><span class="sl-r" data-k="6" style="left:4.17%;top:81.2%;width:54.32%;height:7.5%"></span><span class="sl-r" data-k="7" style="left:65.1%;top:18.8%;width:26.98%;height:7.69%"></span><span class="sl-r" data-k="8" style="left:72.92%;top:60.19%;width:11.35%;height:3.15%"></span><span class="sl-r" data-k="8" style="left:68.07%;top:69.63%;width:26.25%;height:6.11%"></span><span class="sl-r" data-k="8" style="left:68.02%;top:75.83%;width:17.14%;height:2.96%"></span>
</div>
<div class="sl-txt" markdown="1">

**Will these systems reach general human intelligence — artificial general intelligence (AGI) — or pass it?**
{: data-k="1"}

> **RAND on the state of AGI forecasting, 24 March 2026**
> {: data-k="2"}
>
> “Substantial disagreement remains even when definitions and information are held constant.” The field “lacks resolved forecasts for calibration; benchmarks resistant to saturation and gaming; continuous, real-time insight into model capabilities; and independent validation of influential models.”
> {: data-k="3"}

**Karpathy, October 2025**  
Roughly a decade — on stated intuition, not a model: “it feels like a decade to me.” Names continual learning as one of several missing pieces.
{: data-k="4"}

**What I can see, on this question**  
How much instruction tuning changed the weights, and where — its rank and its location. Not what those directions mean, and not the circuits behind a behaviour. That needs causal intervention, which I haven’t done.
{: data-k="5"}

*Company leaders forecasting two years are raising money. Organisations whose purpose is AI-safety advocacy have an interest in short timelines. Forecaster tournaments have known long-horizon pathologies. It cuts every way.*
{: data-k="6"}

**Fiction is the only place anyone knows the timeline!  :)**
{: data-k="7"}

*Image captions:* ***The Matrix, 1999*** (a still subtitled “We marveled at our own magnificence as we gave birth to AI.”) · **“I’m sorry, Dave. I’m afraid I can’t do that.”** ***2001: A Space Odyssey, 1968***
{: .small data-k="8" }

</div>
</div>

---

## What I answered, and what I didn’t
{: id="what-i-answered-and-what-i-didnt" data-k="t"}

<div class="sl" markdown="1">
<div class="sl-fig" markdown="1">
![Slide 32: the three cards, with Environment highlighted, and three closing lines](/assets/img/posts/2026-09-18-ai-environmental-impact-32.png)<span class="sl-r" data-k="t" style="left:4.12%;top:8.43%;width:55.52%;height:6.48%"></span><span class="sl-r" data-k="1" style="left:5.88%;top:20.09%;width:10.31%;height:3.33%"></span><span class="sl-r" data-k="2" style="left:37.03%;top:20.09%;width:10.63%;height:3.33%"></span><span class="sl-r" data-k="3" style="left:68.33%;top:20.09%;width:11.25%;height:3.33%"></span><span class="sl-r" data-k="4" style="left:5.88%;top:25%;width:13.07%;height:3.06%"></span><span class="sl-r" data-k="5" style="left:37.03%;top:25%;width:19.95%;height:3.06%"></span><span class="sl-r" data-k="6" style="left:68.23%;top:25%;width:21.98%;height:3.06%"></span><span class="sl-r" data-k="7" style="left:8.91%;top:31.11%;width:7.66%;height:2.96%"></span><span class="sl-r" data-k="8" style="left:8.91%;top:34.07%;width:4.95%;height:2.96%"></span><span class="sl-r" data-k="9" style="left:8.96%;top:37.04%;width:3.7%;height:2.5%"></span><span class="sl-r" data-k="10" style="left:8.91%;top:39.91%;width:3.59%;height:2.59%"></span><span class="sl-r" data-k="11" style="left:40.16%;top:31.11%;width:14.74%;height:2.96%"></span><span class="sl-r" data-k="12" style="left:40.16%;top:34.07%;width:22.24%;height:2.59%"></span><span class="sl-r" data-k="13" style="left:40.1%;top:37.04%;width:8.75%;height:2.96%"></span><span class="sl-r" data-k="14" style="left:71.35%;top:31.48%;width:4.32%;height:2.59%"></span><span class="sl-r" data-k="15" style="left:71.35%;top:34.07%;width:9.48%;height:2.96%"></span><span class="sl-r" data-k="16" style="left:71.3%;top:37.22%;width:5.99%;height:2.32%"></span><span class="sl-r" data-k="17" style="left:71.41%;top:39.91%;width:5.36%;height:2.96%"></span><span class="sl-r" data-k="18" style="left:4.17%;top:54.35%;width:38.7%;height:3.8%"></span><span class="sl-r" data-k="19" style="left:4.17%;top:62.13%;width:38.18%;height:3.8%"></span><span class="sl-r" data-k="20" style="left:4.12%;top:69.81%;width:56.51%;height:4.44%"></span>
</div>
<div class="sl-txt" markdown="1">

| Provenance | Substitution | Environment |
|---|---|---|
| *the end of attribution* | *replacement and its consequences* | *sudden industrial scaling and its costs* |
| <span data-k="7">artist images</span><br><span data-k="8">writings</span><br><span data-k="9">music</span><br><span data-k="10">video</span> | <span data-k="11">social media manipulation</span><br><span data-k="12">artists and content-creators out of work</span><br><span data-k="13">AI content slop</span> | <span data-k="14">energy</span><br><span data-k="15">carbon footprint</span><br><span data-k="16">water use</span><br><span data-k="17">pollution</span> |
{: data-keys="1 2 3 4 5 6 - - -"}

You have seen what has been **measured**.
{: data-k="18"}

You have seen what has been **modelled**.
{: data-k="19"}

And you have seen where the **boundary** between them sits.
{: data-k="20"}

</div>
</div>

---

*If you find an error on any slide, I'd like to hear about it. My email is linked in the sidebar.*

<script>
/* Links each piece of slide text to its place on the slide image: hovering either one highlights both.
   Written without line comments and with explicit semicolons because the production build joins lines. */
(function () {
  "use strict";
  var each = function (list, fn) { Array.prototype.forEach.call(list, fn); };
  each(document.querySelectorAll(".sl"), function (block) {
    var stage = block.querySelector(".sl-fig > p");
    var text = block.querySelector(".sl-txt");
    var head = block.previousElementSibling;
    if (!head || head.tagName !== "H2" || !head.hasAttribute("data-k")) { head = null; }
    each(block.querySelectorAll("table[data-keys]"), function (table) {
      var keys = table.getAttribute("data-keys").split(" ");
      each(table.querySelectorAll("th, td"), function (cell, i) {
        if (keys[i] && keys[i] !== "-") { cell.setAttribute("data-k", keys[i]); }
      });
    });
    var boxes = [];
    each(block.querySelectorAll(".sl-r"), function (r) {
      var l = parseFloat(r.style.left), t = parseFloat(r.style.top), w = parseFloat(r.style.width), h = parseFloat(r.style.height);
      boxes.push({ k: r.getAttribute("data-k"), l: l, t: t, r: l + w, b: t + h, a: w * h });
    });
    var current = null;
    var mark = function (key, on) {
      each(block.querySelectorAll('[data-k="' + key + '"]'), function (n) { n.classList.toggle("on", on); });
      if (head && head.getAttribute("data-k") === key) { head.classList.toggle("on", on); }
    };
    var show = function (key) {
      if (key === current) { return; }
      if (current !== null) { mark(current, false); }
      current = key;
      if (key !== null) { mark(key, true); }
    };
    var keyOf = function (target) {
      var el = target && target.closest ? target.closest("[data-k]") : null;
      return el && !el.classList.contains("sl-r") ? el.getAttribute("data-k") : null;
    };
    if (text) {
      text.addEventListener("mouseover", function (e) { show(keyOf(e.target)); });
      text.addEventListener("mouseleave", function () { show(null); });
    }
    if (head) {
      head.addEventListener("mouseenter", function () { show(head.getAttribute("data-k")); });
      head.addEventListener("mouseleave", function () { show(null); });
    }
    if (stage) {
      stage.addEventListener("mousemove", function (e) {
        var rect = stage.getBoundingClientRect();
        if (!rect.width || !rect.height) { return; }
        var x = (e.clientX - rect.left) / rect.width * 100;
        var y = (e.clientY - rect.top) / rect.height * 100;
        var best = null;
        for (var i = 0; i < boxes.length; i += 1) {
          var bx = boxes[i];
          if (x >= bx.l && x <= bx.r && y >= bx.t && y <= bx.b && (best === null || bx.a < best.a)) { best = bx; }
        }
        show(best ? best.k : null);
      });
      stage.addEventListener("mouseleave", function () { show(null); });
    }
  });
})();
</script>

*[ACL]: Association for Computational Linguistics
*[ADEME]: Agence de la transition écologique, France's ecological transition agency
*[AGI]: artificial general intelligence
*[AI-PER]: artificial intelligence in physics education research
*[A100]: an NVIDIA data-centre GPU
*[AWS]: Amazon Web Services
*[CBS]: Statistics Netherlands (Centraal Bureau voor de Statistiek)
*[CC BY]: Creative Commons Attribution licence
*[CO₂e]: carbon-dioxide equivalent: all greenhouse gases counted as the mass of CO₂ with the same warming effect
*[CSO]: Central Statistics Office, Ireland
*[CUDA]: NVIDIA's platform for programming GPUs (originally Compute Unified Device Architecture)
*[DEQ]: Department of Environmental Quality
*[DESNZ]: Department for Energy Security and Net Zero (UK)
*[DG ENER]: Directorate-General for Energy (European Commission)
*[EC]: European Commission
*[EIA]: US Energy Information Administration
*[EPRI]: Electric Power Research Institute
*[ESTELA]: Empowering STEM Educators and Learners with AI
*[FAccT]: ACM Conference on Fairness, Accountability, and Transparency
*[GPU]: graphics processing unit
*[GW]: gigawatt
*[GWh]: gigawatt-hour
*[H100]: an NVIDIA data-centre GPU
*[IEA]: International Energy Agency
*[JLARC]: Joint Legislative Audit and Review Commission (Virginia)
*[JMLR]: Journal of Machine Learning Research
*[kt]: kilotonnes (thousands of tonnes)
*[LANSCE]: Los Alamos Neutron Science Center
*[LBNL]: Lawrence Berkeley National Laboratory
*[LLM]: large language model
*[LTRA]: Long-Term Reliability Assessment
*[MDEQ]: Mississippi Department of Environmental Quality
*[MLPerf]: an industry benchmark suite for machine-learning hardware
*[MW]: megawatt
*[MWh]: megawatt-hour
*[NERC]: North American Electric Reliability Corporation
*[NOx]: nitrogen oxides
*[OPT]: Open Pre-trained Transformer, a Meta language model
*[PCF]: product carbon footprint
*[PP]: Professional Paper (a USGS report series)
*[RCFP]: Reporters Committee for Freedom of the Press
*[SEAI]: Sustainable Energy Authority of Ireland
*[SVD]: singular value decomposition
*[TPU]: tensor processing unit, Google's AI accelerator chip
*[TVA]: Tennessee Valley Authority
*[TWh]: terawatt-hour
*[UCF]: University of Central Florida
*[UCN]: ultracold neutron
*[UCNA]: Ultracold Neutron Asymmetry
*[USGS]: US Geological Survey
*[WEF]: World Economic Forum
