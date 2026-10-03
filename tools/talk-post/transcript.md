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

![Slide 2: background — education, prior research and current work, with a diagram of UCN Area B at Los Alamos and a heatmap of weight change by layer](/assets/img/posts/2026-09-18-ai-environmental-impact-02.png)

Second-year doctoral student in physics, University of Central Florida · advised by Zhongzhou Chen  
Earlier work published as S D Moore

**Education**

- B.S. Physics, North Carolina State University, 2017
- M.S. Physics, North Carolina State University, 2019
- Graduate-level computer science coursework

**Prior research**

- GPU programming in CUDA since 2014 — neutron-transport integrator ported to GPU; Lindbladian Runge–Kutta
- Ultracold Neutron Asymmetry (UCNA) collaboration — beta-decay asymmetry and dark-matter constraints; six peer-reviewed papers
- Experimental atomic, molecular and optical physics — ColdQuanta / Infleqtion

**Current**

- Physics education research and mechanistic interpretability of large language models
- Numerical LLM: Ex. SVD of instruct-minus-base weight deltas across Qwen 2.5, 0.5B to 14B
- Reviewer, Association for Computational Linguistics (ACL) Rolling Review

> Work in LLM has relevance but more so work in CUDA GPU programming.

*Image captions: UCN Area B, Los Alamos Neutron Science Center (LANSCE), Los Alamos National Laboratory · Weight change by layer, base vs. instruction-tuned*
{: .small }

---

## Educational Work: Interactive Quantum Computing Game “Entangled States”

![Slide 3: the Entangled States quantum-circuit game from the IBM Quantum Hackathon 2020, and the ESTELA workshop presentation](/assets/img/posts/2026-09-18-ai-environmental-impact-03.png)

**IBM Quantum Hackathon, 2020**  
**Second place**

A sandbox for building quantum circuits. Place a gate on a wire and the state vector on the left redraws — all eight amplitudes, live.

> The other half: tools that make an abstraction something you can push on.
>
> **ESTELA Summer Workshop 2026**
>
> Empowering STEM Educators and Learners with AI · UCF and Valencia College
>
> A presentation on building interactive coursework tools with AI, on the fly.

{% include embed/video.html src='/assets/img/posts/2026-09-18-ai-environmental-impact-03.mp4' poster='/assets/img/posts/2026-09-18-ai-environmental-impact-03-poster.png' title='Screen capture · no audio' loop=true muted=true %}

---

## What do students find uncomfortable about using generative AI?

![Slide 4: three cards — Provenance, Substitution, Environment — listing what students find uncomfortable about generative AI](/assets/img/posts/2026-09-18-ai-environmental-impact-04.png)

| Provenance | Substitution | Environment |
|---|---|---|
| *loss of attribution for original work* | *replacement and its consequences* | *sudden industrial scaling and its costs* |
| artist images<br>writings<br>music<br>video | social media manipulation<br>artists and content-creators out of work<br>AI content slop | energy<br>carbon footprint<br>water use<br>pollution |

*My split. It may not be the right three.*

**The third one is the only one I can put numbers on… which is handy since that is what the presentation is on!**

---

## AI's environmental footprint

![Slide 5: AI's environmental footprint — what was measured, what was modelled, and what nobody knows](/assets/img/posts/2026-09-18-ai-environmental-impact-05.png)

What was measured, what was modelled, and what nobody knows

> **SPOILER ALERT · SUBJECTIVE IMPRESSION**
>
> **The *measurement* is a mess.**
>
> The numbers contradict each other. Most of them are also correct. **That is the talk.**

**The people who do this for a living say so**

Isolating the internet's share of US electricity "virtually guarantees large calculational errors." — *Berkeley Lab, 2000*

Its own earlier model's utilisation assumptions had "**little-to-no measured data** available to verify them." — *Lawrence Berkeley National Laboratory on LBNL, 2026*

"a general lack of consensus on methods to measure AI emissions" — *Cooper Elsworth, Google, to the National Academies, 2025*

**And it travels badly**

"Training a single AI model **can** emit as much carbon as five cars in their lifetimes" — *MIT Technology Review, 2019.* Google researchers later put the same run **88× lower**.

Of **100** news articles on ChatGPT's energy use sampled in April 2025, **53%** repeated one 2023 estimate and **75%** gave no source or uncertainty.

Of the **676** sources cited by **46** data-centre energy studies, **11%** had dead links and **10%** could not be located.

**So every number in this talk comes with three labels:** what it is a share **of**, what **year** it describes, and whether someone read a **meter** or ran a **model**. The talk is built to help you check them, not to tell you what to conclude.

---

## Start with the unsurprising part: efficiency up, totals up

![Slide 6: two columns — per unit of work, energy down; in total, three different totals up](/assets/img/posts/2026-09-18-ai-environmental-impact-06.png)

Per unit of *work*, energy has fallen wherever it has been tracked. **Totals have risen** — but totals of three different things: one company's electricity, one country's metered electricity, and a forecast of peak *power*.

| **Down — per unit of work** | **Up — in total: total *what*?** |
|---|---|
| **Google, median Gemini Apps text prompt: 0.24 Wh** (May 2025, Google's own measurement), **33× lower than a year earlier**, mostly software. The repeated "~3 Wh" was never a measurement: an executive's remark about *cost* × a 2009 blog post | **Google's company-wide electricity rose 37%** in 2025 (Google's own report; all of Google, not only AI) |
| **Worldwide, 2010–2018:** computing work in data centres rose **~550%** while their electricity rose **~6%** (a model, *Science*, 2020) | **Ireland:** data centres went from **5% (2015) to 23% (2025)** of metered electricity. In 2025 alone their use rose **10%**; all other users' rose **2%** |
| **A famous 2019 training-carbon estimate** — 284 t for an automated architecture search — was recomputed by Google researchers in 2021 at **3.2 t**: **88× lower**, a figure they state *conditionally*, "for energy-efficient organizations like Google". **18.7×** of it is like-for-like, correcting only how the search had been read | **North America's grid reliability body** raised its ten-year summer peak-demand *growth* forecast by **69%** in one year (132 → 224 GW). **A forecast, not a measurement** |

***Left:*** *a company's own measurement, a model, and a company's re-estimate.* ***Right:*** *a company's own total, a national meter reading, and a forecast. Efficiency per unit is real, and totals rose anyway. Neither column settles the other.*

Sources: Google 2025 and 2026; Masanet et al. 2020; Patterson et al. 2021; CSO Ireland 2026; NERC LTRA 2025
{: .small }

---

## What "AI's footprint" actually counts

![Slide 7: nested squares drawn to scale — world electricity 28,600 TWh, all data centres 485 TWh, "AI-focused" facilities about 155 TWh — beside notes on water, carbon, training and embodied emissions](/assets/img/posts/2026-09-18-ai-environmental-impact-07.png)

**What leaves the boxes**

- **Water, at two layers:** cooling at the building, and water consumed generating the electricity. For US data centres in 2018 the second layer was **about three-quarters** of the total, hydropower reservoir evaporation included.
- **Carbon, at the electricity layer,** reported two ways: **location-based** (the local grid's average) and **market-based** (after clean-energy purchases). Meta reports Llama 3.1 training as **11,390 t** one way and **0 t** the other.
- **Training versus use:** the only company splits published predate ChatGPT. Google, all machine learning 2019–2021: about **⅗ use, ⅖ training**.
- **Outside every electricity figure above:** making the chips and building the data centres. Meta put that **embodied** share at about **30%** of its AI tasks' emissions (2022); a 2026 review says **more than half** for large AI data centres — **50–82% of data-centre emissions** in its one numeric statement — without stating its carbon basis, and with its own boundary drawn around **server manufacturing only**.

*The IEA's "slightly more than 1.5% of global electricity demand" names no total. On the IEA's own consumption total it is 1.70%; on Ember's demand total, 1.53%.*

*Text in the figure:*

> **What “AI’s footprint” is a share of — three nested totals, 2025**
>
> Modelled, not metered. Every percentage here is of world electricity CONSUMPTION, 28,600 TWh (IEA, July 2026 revision).
>
> Key: Everything else · Data centres other than “AI-focused” facilities · “AI-focused” facilities
>
> World electricity **28,600 TWh**, consumption, 2025 (IEA) — *areas to scale*
>
> *The same two squares, magnified 5×:* All data centres 485 TWh, 1.70% of world electricity consumption · “AI-focused” facilities ~155 TWh, 0.54% of world electricity consumption
>
> 485 TWh is ALL data centres — streaming, email, storage, business IT, not only AI. “AI-focused” is the IEA’s label for whole FACILITIES: everything in such a building counts, and AI work done elsewhere does not. Neither total separates AI workloads from the rest; no metering system anywhere does.
> Both are modelled from purchased shipment records, so they can err high (chips sold but not yet running) and low (custom chips that trackers cannot see).
> The other denominator: on Ember’s world “demand” total of 31,779 TWh — counted from generation, so it includes grid losses — the same 485 TWh is 1.53% and the 155 TWh is 0.49%.
> Sources: IEA (all data centres, P12; AI-focused facilities, P13); Ritchie / Our World in Data (155 TWh, derived from IEA’s 465 TWh for 2030 ÷ 3); Ember Global Electricity Review 2026 (P22).
> Type E — modelled estimate, in the deck’s own labelling. Percentages derived here.
{: .small }

Sources: IEA 2026; Ember 2026; Our World in Data; Siddik et al. 2021; Meta model cards; Chien et al. 2026
{: .small }

---

## Percentage of *what*?

![Slide 8: table — the same numerators over different denominators give different shares](/assets/img/posts/2026-09-18-ai-environmental-impact-08.png)

**The same quantity over different totals gives different answers. Neither is wrong, as long as it says which total it used.**

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

***Most arguments about "how big" are arguments about the bottom of the fraction.*** *The water rows divide 2023 use by long-run totals (2010–2020; 2015): the years differ.*

Sources: Ember; IEA; EIA; LBNL 2025; CSO Ireland; SEAI; USGS
{: .small }

---

## Where the electricity, the water and the carbon actually enter

![Slide 9: a grid of five layers — making the chips and building the data centre; generating the electricity; the building; training a model; everyday use — against electricity, water and carbon, with layer 1 marked as outside every electricity figure](/assets/img/posts/2026-09-18-ai-environmental-impact-09.png)

*Text in the figure:*

Five layers. Most published “AI uses X” figures count only the shaded ones — and not all of them count the same shaded ones. Nothing here is drawn to scale: the layers are not comparable quantities.

*Layer 1 is marked “OUTSIDE every one of them”; layers 2–5 are shaded and marked “INSIDE the electricity figures on the other slides”.*

| The layer | Electricity | Water | Carbon |
|---|---|---|---|
| **1. Making the chips, building the data centre**<br>*“embodied” — spent before a single query is answered* | No figure for AI in this corpus. | A chip fab “can use” ~38 million L a day of ultra-pure water — drawn, not consumed. (E, 2024) | ~30% of Meta’s AI-task emissions (D, pub. 2022). “More than half” for large AI data centres in a 2026 review — carbon basis not stated (E). 1,312 kg per 8-GPU H100 board (D, 2025). |
| **2. Generating the electricity**<br>*the grid, wherever the building is plugged in* | ~485 TWh, all data centres — 1.70% of world electricity consumption. (E, 2025) | ~75% of the US data-centre water footprint, reservoir evaporation included (E, 2018). Coefficient 1.8–7.6 L/kWh, and which end you get is mostly the hydropower choice. | Whatever the local grid emits — and which method you use: 11,390 t location-based, 0 t market-based, for the same runs. (D, 2024) |
| **3. The building: cooling and overhead**<br>*the part a data-centre operator can change* | Inside “full serving stack” figures. Counting only the chips is about 1.7× narrower. (D, 2025) | ~25% of the US data-centre water footprint by volume — but over 40% of its scarcity-weighted index, because it is drawn next to the building. (E, 2018) | Follows the electricity above. No separate figure. |
| **4. Training a model**<br>*one-off, per model* | 433 MWh, BLOOM 176B — GPU-hours × rated power, not metered. (E, 2022) | 281,000 m³, Mistral Large 2, lifecycle method, server manufacturing included. (D, 2025) | 50.5 t, BLOOM — chips + idle + embodied (E, 2022). 8,930 t, Llama 3.1 405B (D). 1,247.61 t, Gemma 2 — pre-training only (D). Nothing published for GPT-4/5, Gemini, Claude, Grok. |
| **5. Everyday use**<br>*every query, for as long as the model is served* | 0.24 Wh, median Google text prompt (D, May 2025). 3.91 Wh, a simulated long reasoning query (E, 2026). ~150 Wh, one typed agentic-coding prompt (E, 2026). | 0.26 mL per prompt — the building only (D, 2025). 16.9 mL per response — including the power station, 87% of it off-site (E, model of GPT-3). | 0.03 g per prompt, market-based — the only basis the paper reports (D, 2025). ~0.09 g location-based, derived here. |

**Water leaves at two layers, and only one of them is the building.** *(Marked on layers 2 and 3.)*

Training versus everyday use: the only company splits ever published predate ChatGPT. Google, all its machine learning 2019–21: about ⅗ use, ⅖ training. Meta, one production translation model (pub. 2022): 65% use, 35% training; its recommendation models, about even. No company publishes how many times a current chatbot is used, so no one can compute this ratio for the models you actually use.
Type codes, as used throughout the talk: M metered or instrumented · D first-party disclosure · E modelled estimate. A figure’s type matters more than its size.
Sources, by row: IEA P12; Siddik, Shehabi & Marston 2021 P37; Torcellini et al. 2003 and the coefficient set in “amendment-01”; Meta Llama 3.1 model card; Chien et al. 2026 P53; Wu et al. (Meta) P70; NVIDIA PCF summary 2025; WEF 2024 P66; Luccioni, Viguier & Ligozat P59; Gemma 2 technical report; Mistral AI with Carbone 4 and ADEME P69; Google (Elsworth et al.) P42; Li et al. P29; Oviedo et al. P33.
{: .small }

---

## What one use costs

![Slide 10: table of three per-use energy figures — 0.24 Wh, 3.91 Wh and about 150 Wh — with what kind of number each is and its weakness](/assets/img/posts/2026-09-18-ai-environmental-impact-10.png)

**Three ways of "using AI", three very different numbers — and none is an independent measurement of the closed services most people use**

| | **A quick text prompt** | **A long "reasoning" query** | **One typed prompt in an agentic coding tool** |
|---|---|---|---|
| **Energy** | **0.24 Wh** | **3.91 Wh** | **~150 Wh** *(range 60–290)* |
| **What kind of number** | Google's own production measurement (May 2025): the prompt-weighted median of its models' averages | A simulation by Microsoft researchers (2026): models over 200 billion parameters on H100 servers, answers of ~5,000 tokens | One researcher's estimate from his own usage logs (Aug 2026) using three published per-token factors. His median *session* was ~600 Wh |
| **Its weakness** | One company's median; Google publishes neither the mean nor the number of prompts | Assumed hardware, load and answer length; an earlier version said 4.32 | One user, one tool, borrowed factors |

> **Do not multiply any of these by a number of uses.** None is an average over real traffic that you can scale.

**The kind of task matters as much as the model.** Luccioni et al. (FAccT 2024), one 8×A100 node, inference only: **≈60×** between the mean energy of text generation **capped at 10 output tokens** and the mean for image generation; **≈29× on the paper's own medians**. n = 8, the image side's standard deviation exceeds its mean, and the comparison is **not size-matched** — the 11-billion-parameter model is on the *text* side. Image generation costs more *despite* smaller models.

**Why there is no everyday comparison here.** Items that make these look small, such as a drive or a flight, are published as *carbon*, not energy. The item that makes them look large, a web search, rests on a 2009 blog post. Both groups are in the source list.

Sources: Google (Elsworth et al.) 2025; Oviedo et al. 2026; Hausfather 2026; Luccioni, Jernite & Strubell 2024
{: .small }

---

## Why there is no single "cost of a prompt"

![Slide 11: four axes of per-query energy — task (1,450×), boundary (2.4×), how busy (0.28 kWh), mode (154–697×)](/assets/img/posts/2026-09-18-ai-environmental-impact-11.png)

**Per-query energy depends on the task, the accounting boundary, how busy the server is, and the mode**

**1,450×**  
**Task.** From **0.002 to 2.907 kWh per 1,000 inferences** — text classification against image generation — on the same lab hardware (open models up to 11 billion parameters, one request at a time, 2024).

**2.4×**  
**Boundary.** Google's 0.24 Wh becomes **0.10 Wh** under its narrower method: about **1.7×** from counting only the chips, about **1.4×** from counting only the most efficient tenth of its data centres (same month, May 2025).

**0.28 kWh**  
**How busy.** On BLOOM's lightly used public demo (2022) the server still used about **0.28 kWh every 10 minutes** when almost no requests arrived. *Software-estimated; the authors say the total cannot be cleanly split into idle and working energy.*

**154–697×**  
**Mode.** For three open models that can switch "reasoning" on and off (3, 15 and 70 billion parameters), turning it on raised GPU energy per query **154× to 697×**, as they wrote 300–800× more tokens. Across the benchmark, reasoning models averaged about **30×** (Dec 2025).

Sources: Luccioni, Jernite & Strubell 2024; Google 2025; BLOOM (Luccioni et al.) 2022; ML.ENERGY 2025
{: .small }

---

## Why “task” is worth a moment’s focus

![Slide 12: the 1,450× task spread beside a diagram of six shapes of work one typed prompt can set running. A single box labelled ONE PROMPT leads to six rows: answers straight away; thinks first, then answers; reads an image you attached; calls a tool; keeps looping between model and tool; hands parts of the job to other agents. A marker on each row is filled where this talk prints a per-use energy figure for that shape of work (rows 1, 2 and 5) and hollow where it does not (rows 3, 4 and 6). The diagram is schematic and encodes no quantities.](/assets/img/posts/2026-09-18-ai-environmental-impact-12.png)

**The same number as the slide before, with room to say what it is** — and what “task” can mean beyond the two types the study measured

> **1,450×**
>
> **0.002 → 2.907 kWh per 1,000 inferences**
>
> the *means* of two task types — text classification against image generation — on one 8×A100 node, open models up to 11 billion parameters, one request at a time, 2024

- **The spread is task** *and* **model.** The two tasks use different models, so this is not a controlled comparison at fixed model size. **88 open models**, the largest Flan-T5-XXL at **11 billion parameters**, one 8×A100 node, **unbatched** — a lab setup, not production traffic.
- **It is the extremes of a spread, not a headline multiple.** The paper reports a range across tasks; the variation *inside* each task is not shown. Read 1,450× as the distance between the cheapest and the dearest task measured, not as a ratio that anything typical has.
- **And it is one axis of four.** The slide before shows three more — the accounting boundary, how busy the server is, and whether “reasoning” is switched on. **None of them multiplies with any other.**
- **What “task” can also mean.** Everything above is across task *types* inside **single model calls**. The diagram to the right is a different axis: how much work one typed prompt can set running before any answer comes back. It carries its own caveats — **it encodes no energy, and it does not multiply with the 1,450×.**

*Text in the figure:*

> **“One prompt” is not one kind of work**
>
> Six shapes of work one typed prompt can set running, ordered by structure and **not** by cost.
>
> **ONE PROMPT** — one thing you typed, one reply on your screen. Key: model call · tool call · reply
>
> ● Answers straight away  
> ● Thinks first, then answers  
> ○ Reads an image you attached  
> ○ Calls a tool — a search, a fetch, some code  
> ● Keeps looping: model, tool, model, tool  
> ○ Hands parts of the job to other agents
>
> **All six of these are one prompt.** So the first question about any “per-prompt” number is: which of these was it?
>
> ● a per-use energy figure for this shape of work is printed somewhere in this talk · ○ none is. That is a statement about this deck, not about the literature.
>
> Schematic, drawn for this talk, not reproduced from a source. **Nothing here encodes energy:** a longer chain means more calls happen, never how many and never what they cost; “···” means “repeats”, not a number.
>
> Nothing here says which path is common, and no source in this talk does either. The >1,450× spread on this slide is a different axis: it is between the *means* of two task types, inside single model calls (Luccioni et al. 2024).
{: .small }

Sources: Luccioni, Jernite & Strubell, FAccT 2024 (P60). The diagram was drawn for this talk and is not reproduced from a source.
{: .small }

---

## Why this talk prints no everyday comparison

![Slide 13: three per-use figures in their own units — 0.24 Wh, 3.91 Wh, about 150 Wh — and why nothing is compared to anything else](/assets/img/posts/2026-09-18-ai-environmental-impact-13.png)

**Three kinds of use, in their own units — and why nothing here is compared to anything else**

**0.24 Wh**  
a median Google text prompt — Google's own measurement; **0.03 g CO₂e** market-based, May 2025

**3.91 Wh**  
a long reasoning query — Microsoft researchers' simulation, 2026

**~150 Wh**  
one typed prompt in an agentic coding tool — one user's estimate, 2026

> **No everyday comparator appears anywhere in this talk.** Eighteen of them were chosen and frozen on 19 August, before any AI figure had been seen, and they stay published in the source list. None of them reaches a slide.

*Why:* every conversion needs a choice — which use, how many uses, which grid, whether the screen counts — and the choice decides the answer.

The two items that would sway you most, **a kettle boil** and **doing the task by hand**, are exactly the two that nobody has published.

Sources: Google 2025; Oviedo et al. 2026; Hausfather 2026; comparator set, frozen 19 Aug 2026 (Amendment 03)
{: .small }

---

## One training run, fully counted

![Slide 14: BLOOM's training emissions split three ways, with a world map of grid carbon intensity by country and a US map of a hypothetical data centre's carbon footprint by watershed](/assets/img/posts/2026-09-18-ai-environmental-impact-14.png)

**BLOOM (176 billion parameters, trained in France in 2022): 50.5 tonnes CO₂e, counted three ways**

| **Chips doing the work** | **Keeping the cluster on** | **Making the hardware** |
|---|---|---|
| **24.69 t (49%)** | **14.60 t (29%)** | **11.20 t (22%)** |
| Estimated: GPU-hours × each GPU's rated 400 W. Real-time power was not tracked | Measured: the cluster's draw when idle against its draw when training | A lower bound — no chipmaker published manufacturing figures at the time |

**The trial and intermediate runs emitted more than the final model:** 35.8 t against 24.69 t. Some of those intermediate models were released too.

**Where you train can matter more than how much you train.** In the paper's comparison table BLOOM used *more* electricity than a comparable model, OPT (433 vs 324 MWh), yet emitted about a third as much carbon (25 vs 70 t), because France's grid was 57 g CO₂e/kWh and OPT's was 231. *(The table's rows do not all count data-centre overhead the same way.)*

*One cluster, one country. The chip term assumes every GPU drew its full rating, which can err either way; the hardware term is a lower bound.*

**Left — the world, by country.** *Lifecycle* g CO₂e per kWh generated: upstream, supply chain and manufacturing included, all greenhouse gases. **2025**, or the nearest year 2022–2024 where 2025 is missing. Scale **0 to 900+ g**. *Our World in Data, from Ember 2026, CC BY.*

**Right — the United States, by watershed.** The carbon footprint of the same **hypothetical 1 MW data centre**, **0.02 to 1 ton CO₂e/MWh**, 2018 data. The paper states neither short or metric tons, nor whether the basis is lifecycle or combustion only. *Siddik et al. 2021, figure 4 panel C, CC BY 4.0.*

*Two different bases and three different years, so do not read a value off either map and set it against the 57 and 231 above — those are the operational grid factors the paper used. What the maps show is the size of the spread: where you build or train moves the number further than most people expect.*

Sources: Luccioni, Viguier & Ligozat, JMLR 2023 (BLOOM); Our World in Data / Ember 2026 (CC BY); Siddik, Shehabi & Marston 2021 (CC BY 4.0)
{: .small }

---

## The largest disclosed footprints, and the accounting underneath

![Slide 15: training footprints disclosed by Meta (Llama 3.1), Google (Gemma 2) and Mistral (Large 2), each with its own boundary](/assets/img/posts/2026-09-18-ai-environmental-impact-15.png)

**Companies' own training numbers — each with a different boundary**

**Meta · Llama 3.1**  
**8,930 t CO₂e** for the 405B model; **11,390 t** for the three-model family. Both **location-based**, using the average grid where the chips ran. **The same runs are reported as 0 t "market-based"**, after renewable purchases. Meta multiplied GPU-hours by each GPU's *rated* power, which leaves out the rest of the server; a 2025 measurement study treats that as a **lower bound**.

**Google · Gemma 2**  
**1,247.61 t CO₂e**, **pre-training only**. The larger "teacher" model used to train two of the three is not counted. The report calls Google's data centres carbon-neutral; Google itself stopped claiming operational carbon neutrality from 2023 (its July 2024 report).

**Mistral · Large 2**  
**20.4 kt CO₂e and 281,000 m³ of water consumed** — training "as of January 2025, and after 18 months of usage", server manufacturing included. A lifecycle study with France's ecological transition agency, reviewed by two consultancies (2025).

**These are not comparable with each other:** different phases, boundaries and carbon methods.  
**No developer has published a training energy or emissions figure** for GPT-4, GPT-5, any Gemini model, Claude or Grok (as of mid-September 2026).

Sources: Meta model cards; Google Gemma 2 report; Mistral/ADEME lifecycle study 2025; Newkirk et al. 2025
{: .small }

---

## The bar chart these numbers invite — and why it is not a comparison

![Slide 16: a deliberately naive bar chart of five published training footprints on one axis — 20,400 t, 11,390 t, 8,930 t, 1,247.61 t and 0 t — beside a column explaining what each number actually covers](/assets/img/posts/2026-09-18-ai-environmental-impact-16.png)

*Text in the figure:*

Five published training footprints, in tonnes of CO₂-equivalent. Every one is transcribed correctly from the company’s own document. Put them on one axis and you are ranking the boundaries, not the runs.

**WHAT EACH NUMBER ACTUALLY COVERS**

| Number | What it covers |
|---|---|
| **Mistral Large 2**<br>20,400 t | lifecycle, incl. server manufacturing · (D, pub. 22 Jul 2025)<br>training “as of January 2025, and after 18 months of usage”. also 281,000 m³ of water consumed.<br>▸ **widest boundary here: server manufacturing included** |
| **Llama 3.1 family (8B + 70B + 405B)**<br>11,390 t | location-based; GPU-hours × 700 W rated power · (D, 2024)<br>final pre-training runs only; development runs excluded. three models summed; the card leaves the family’s power cell blank.<br>▸ **a SUM of three runs; chip-only power, a lower bound on server energy** |
| **Llama 3.1 405B**<br>8,930 t | location-based; 30.84 M GPU-hours × 700 W rated power · (D, 2024)<br>final pre-training run only. the same runs are reported as 0 t market-based.<br>▸ **chip-only power: a LOWER BOUND on server energy** |
| **Gemma 2 family**<br>1,247.61 t | TPU energy scaled for facility overhead · (D, 2024)<br>PRE-TRAINING ONLY. excludes the larger teacher model used to train two of the three.<br>▸ **pre-training only; the distillation teacher is not counted** |
| **Llama 3.1 family, market-based**<br>0 t | market-based, after renewable-energy purchases · (D, 2024)<br>the same runs as the 11,390 t above. the Greenhouse Gas Protocol asks for both methods; Meta reported both.<br>▸ **SAME RUNS as the 11,390 t bar — a different accounting method** |

**Nothing in the left-hand column is wrong. The chart beside it still is.**

**NAIVE ANALYSIS** *— one axis, 5 different boundaries:* bars of 20,400 t, 11,390 t, 8,930 t and 1,247.61 t, and “0 t — the same runs as the 11,390 t bar”, on one axis of tonnes CO₂e from 0 to 20,000.

**What the order is actually measuring: how wide a boundary each company drew, which carbon accounting method it chose,** and how many runs it added together. Change any one of those and the order changes.

The tallest bar is not the largest training run — only the largest one DISCLOSED. No developer has published a training energy or emissions figure for GPT-4, GPT-5, any Gemini model, Claude or Grok (as of mid-September 2026). Market-based zeros are standard practice: the Greenhouse Gas Protocol asks companies to report both methods, and Meta did. Showing both is the point, not an accusation. Do not divide any of these by any other, and do not convert them into “N people’s annual footprint” — that sets a one-off total against a yearly flow.
Sources: Meta Llama 3.1 model card (2024); Gemma 2 technical report §3.4 (2024); Mistral AI with Carbone 4 and ADEME, reviewed by Resilio and Hubblo, P69 (22 Jul 2025); Type D — first-party disclosure.
{: .small }

---

## Training versus use

![Slide 17: what the published splits say about training versus everyday use](/assets/img/posts/2026-09-18-ai-environmental-impact-17.png)

**Is training or everyday use the bigger cost? The measured splits all predate ChatGPT, and they differ by product.**

- **Google, all its machine learning, 2019–2021:** roughly **⅗ of the energy went to use and ⅖ to training** (Google's own report).
- **Meta, published 2022:** for a production translation model, **65% use and 35% training**; for its recommendation models, **about even**. Meta's AI *power capacity* was split **10:20:70** across experimentation, training and use (capacity, not energy).
- **Four small open models (0.56–7 billion parameters):** deployment matched the energy of training plus fine-tuning after about **200–590 million uses** (one lab measured both sides, 2024).
- **No company publishes how many times a current chatbot is used**, so no one can compute this ratio for the models you actually use.
- The **"80–90% is inference"** figure that circulates traces to **two 2019 remarks about cost in dollars**, not energy.

Sources: Patterson et al. 2022; Wu et al. 2022 (Meta); Luccioni et al. 2024; NVIDIA and AWS remarks, 2019
{: .small }

---

## Water, nationally

![Slide 18: US data-centre water in 2018 — 513 million m³ consumed, a quarter on site and three-quarters via electricity, and a scarcity-weighted index 2.5× the volume](/assets/img/posts/2026-09-18-ai-environmental-impact-18.png)

**US data centres, 2018 — the most detailed all-data-centre estimate found**

**513 million m³**  
water **consumed** in 2018: on site, via electricity, and via water utilities. All data centres, not only AI

**¼ · ¾**  
**a quarter** used at the buildings, at an assumed typical cooling rate; **three-quarters** consumed generating their electricity, hydropower reservoir evaporation included

**2.5×**  
weighted by local water scarcity, the footprint **index** is 2.5× the plain volume — 1.29 bn m³ US-equivalent against 513 mn m³ — and the on-site quarter becomes **over 40%** of it. *An index with its own reference point, not litres*

**2.5 is one of five numbers the authors publish, one for each allocation rule.** Theirs is the "primary purpose" rule for reservoir evaporation. Charge **none** of that evaporation to hydropower and the same model gives **5.1×**; charge **all** of it and it gives **1.6×**. Same data, same year, one decision.

> *US AI servers, projected: 731–1,125 million m³ a year, averaged over 2024–2030 — that is 0.6–1.0% of what US crop irrigation, power stations and public water supply consume combined. For 2030 alone the same model gives about 0.9–2.0%*, from the authors' own published code, which computes each year before averaging; the paper prints only the average.

**Not like for like:** the AI figure counts reservoir evaporation and cooling-tower drain-off; the national total counts neither. **No one has published a scarcity-weighted figure for AI.**  
*All estimates, not meter readings. The national total is a 2010–2020 average.*

Sources: Siddik, Shehabi & Marston 2021; Xiao et al., Nature Sustainability 2025 and its published code; USGS PP 1894-D
{: .small }

---

## Water, where the buildings are

![Slide 19: three findings from Virginia's legislative audit — 0.2% to 21% at six utilities, under 0.5% of state withdrawals, 83% of data centres no thirstier than a large office building — and The Dalles, Oregon](/assets/img/posts/2026-09-18-ai-environmental-impact-19.png)

**The same buildings are 21% of one thing and under 0.5% of another. All three findings come from one legislative audit (Virginia, December 2024).**

**0.2% – 21%**  
of **total water use at six named water utilities**. That range spans the utilities; it is not an uncertainty band

**under 0.5%**  
of **Virginia's total water withdrawals** — a total that is about three-quarters water drawn by power plants

**83%**  
of Virginia's data centres used **no more water than an average large office building** (2023). The other 17% used more

> **The Dalles, Oregon (population about 16,000)**
>
> Google's data-centre campus was billed for **355 million gallons in 2021, 29% of the city's water**. That is Google's oldest campus, cooled by evaporation, with all its workloads counted, in a year before ChatGPT launched. The city sued to keep the figure private, with Google paying its legal costs, then settled and released it (December 2022).

*Denominators differ: under 0.5% is of withdrawals, three-quarters of which is power-plant water; the 21% is of one utility's total use; The Dalles is a city total.*

Sources: JLARC Report 598 (Dec 2024); Virginia DEQ 2024; The Oregonian / RCFP; US Census
{: .small }

---

## The water multiplier

![Slide 20: the water multiplier — coefficient, location, hydropower, withdrawn versus consumed, building versus power station — with a US map of total water per MWh for a hypothetical data centre in each watershed](/assets/img/posts/2026-09-18-ai-environmental-impact-20.png)

**Every "AI uses X litres" figure is electricity × a water coefficient × a location**

- **The coefficient** — litres of water consumed per kWh of US grid electricity — runs from **1.8 to 7.6** in published values. Much of that spread is one choice: **whether evaporation from hydropower reservoirs counts.** A 2003 government-lab study, as cited, gives **1.8 without hydro and 7.6 with it**. Others in between: 2.18, 3.14, 4.35, about 5.3.
- **The location:** place the same **hypothetical 1 MW data centre** in each of **2,110 US watersheds** and its total water per MWh — building plus electricity — runs from **1.8 to 105.9 m³**, a **59-fold** gap (2018 grid data, modelled). **The paper prints no middle; its supplement has one:** the median watershed is **6.8 m³/MWh** and the middle half run **4.0 to 7.9** — a spread of two, not of fifty-nine. Only **2 of 2,078** watersheds sit at the 1.8 floor, which is the building's flat cooling assumption where the electricity consumes no water. **The 59× is a gap between two extremes, not a spread of observations.**
- **Drop hydropower and the totals move a long way.** In the authors' own supplement the US data-centre water footprint falls **54%** if no reservoir evaporation is charged to hydropower, and rises **70%** if all of it is. A separate 2026 model's off-site water for US hyperscale sites falls **43%** without hydro.
- **Withdrawn versus consumed:** one widely quoted projection for global AI in 2027 is **4.2–6.6 billion m³ withdrawn**, but only **0.38–0.60 billion m³ consumed**.
- **Building versus power station:** of **16.9 mL** per response (GPT-3, US average, modelled), **87%** evaporates generating the electricity. Google's **0.26 mL** counts **only the building**.

**That bullet as a map.** Figure 4, panel A of the same paper: total water per MWh for one *hypothetical* 1 MW data centre placed in each of the 2,110 US subbasins — **not real facilities**. 2018, m³/MWh.  
**The colour scale runs 1.8 to 106 and the legend prints nothing in between**, so almost the whole country sits in its low end: the median watershed is 6.8. The red is mostly **hydropower reservoir evaporation** under the paper's allocation rule.  
*Shown for the size of the spread, not as a source of values. Siddik, Shehabi & Marston 2021, CC BY 4.0.*

Sources: Torcellini et al. 2003, as cited; Siddik, Shehabi & Marston 2021 and its supplement (CC BY 4.0); Guidi & Dominici 2026; Li et al. 2025; Google 2025
{: .small }

---

## Electricity, where someone reads a meter

![Slide 21: four national series that meter data-centre electricity — Ireland 23%, Netherlands 4.6%, Great Britain about 2%, Norway 2.5%](/assets/img/posts/2026-09-18-ai-environmental-impact-21.png)

**Four national series that meter data-centre electricity. None of them can say how much of it is AI.**

| **Ireland** | **Netherlands** | **Great Britain** | **Norway** |
|---|---|---|---|
| **23%** of metered electricity (2025) | **4.6%** of consumption (2024) | **~2%** of grid consumption (2024); leaves out companies' own in-house data centres | **2.5%** of net consumption (2025) |

- **Ireland is roughly ten times Great Britain on same-year figures (2024) — the gap is real, and its size is not settled.** Ireland **22%** of metered electricity against Great Britain **2%** of electricity taken from the grid. **The two countries do not count the same object:** the British figures cover only data centres serving outside customers and leave out companies' own in-house facilities. Britain's own department prints a rival figure for its own country — **4.1 TWh** against the grid operator's **7.6 TWh** for 2023 — which would put Great Britain nearer 3% and the gap nearer **7×**. On Ireland's own base, **homes are 28%**.
- **Growth is real in every series.** In Ireland about **two-thirds (63%)** of the 2015–2025 rise in data-centre electricity had happened by 2022, the year ChatGPT launched (30 November). Growth since has averaged **~800 GWh a year**, faster than the 2015–2022 average of ~580 — even though new data-centre grid connections around Dublin were largely paused from 2021–22 (the regulator replaced the pause with conditional rules in December 2025).
- **The world figure is a model, not a meter:** about **1.5–1.7%** for all data centres (2025). **There is no metered US series at all.**

Sources: CSO Ireland 2026; CBS Netherlands; DESNZ/National Grid; Statistics Norway; IEA 2026
{: .small }

---

## The United States: modelled, not metered

![Slide 22: the most-cited US figures are models — Lawrence Berkeley National Laboratory and EPRI — and how a shipment model is built](/assets/img/posts/2026-09-18-ai-environmental-impact-22.png)

**The most-cited US figures are models, built from records you cannot inspect**

- **Lawrence Berkeley National Laboratory** (a Department of Energy lab): data centres used **176 TWh (4.4%)** of US electricity in 2023 and **192 TWh (4.7% of consumption)** in 2024 — all data centres, not only AI. *Built from purchased records of servers sold.*
- **The Electric Power Research Institute** (funded mainly by utilities): data centres are **4–5% of US *generation*** now, and its 2030 projections are **60% higher** than in its 2024 report. *Built from state-level data on operating capacity, construction and announced projects.*
- **How a shipment model is built:** hardware sold → assumed installed → assumed power → assumed utilisation → assumed hours → assumed overhead. The Berkeley lab says its 2024 report's utilisation assumptions had "**little-to-no measured data** available to verify them."
- **These can err in either direction.** Sales records count chips sold but not yet switched on (too high) and miss custom chips nobody sells (too low). Project pipelines can include projects that never get built.
- **The US has no metered national series.** The federal statistics agency began pilot surveys of data centres in 2026.

Sources: LBNL 2024 and 2025 Update; EPRI 2024 and 2026; EIA 2026
{: .small }

---

## Rated power cuts both ways

![Slide 23: rated power — estimates built on a whole server's rating run high, estimates built on the chips' rating run low](/assets/img/posts/2026-09-18-ai-environmental-impact-23.png)

***A rating is what hardware could draw. Whether an estimate built on a rating runs high or low depends on which rating it used.***

**Whole server → runs *high***  
One 8-GPU H100 server peaked at **8.4 kW** against its **10.2 kW** rating. Under heavy training loads, servers averaged at most **76%** of that rating. Estimates that multiply the *server's* rating by hours run high.

**Chips only → runs *low***  
The same server's eight GPUs are rated **5.6 kW** in total — less than the 8.4 kW the whole server drew, because processors, memory and networking draw power too. The lab that measured this treats such estimates as a **lower bound**. Meta's Llama figures use this method.

**How far off:** on the lab's workloads, server-rating estimates erred by about **37%** and GPU-rating estimates by about **27%** (2025).  
**A lightly loaded service:** GPUs on BLOOM's public demo drew **78–171 W** against a 400 W rating (2022).

*One lab, one server type (8×H100), two papers with overlapping authors. Cooling and building overhead are not included.*

Sources: Newkirk et al. 2025; MLPerf Power; BLOOM (Luccioni et al.) 2022
{: .small }

---

## The reasonable worst case is two numbers

![Slide 24: the reasonable worst case — modelled national and world shares for 2030 beside measured local shares where data centres cluster](/assets/img/posts/2026-09-18-ai-environmental-impact-24.png)

***Rule: take the top of each source's own published range. Never multiply worst cases together.***

| **Nationally and worldwide, 2030 — modelled** | **Where data centres cluster, recently — measured** |
|---|---|
| **US:** up to **15%** of electricity consumption (Berkeley lab) or **17%** of generation (EPRI). All data centres, not only AI | **29%** of one Oregon city's water (2021; one Google campus, all its workloads) |
| **World:** about **2.8%** for all data centres and **1.4%** for AI-focused facilities (IEA base case; its higher case is published for 2035, not 2030) | **21%** of one Virginia utility's water use (2024 audit) |
| **US water, AI servers:** up to **~1%** of irrigation, power-station and public-supply consumption as a 2024–2030 average, and **~2%** in 2030 itself (from the authors' code) | **23%** of Ireland's metered electricity (2025): a whole country, but one where data centres cluster |

- **Share and amount tell different stories.** On one pair of IEA totals the world share goes from ~1.7% to ~2.8% (**×1.64**), while data-centre electricity itself goes from 485 to ~950 TWh (**×1.96**). The share grows more slowly because world use grows too.
- **No figure for 2050 is given.** The published envelopes run 25 years out — one rests on a fitted relationship whose estimated range includes both signs — and this work has no world electricity total for that year to divide by.

***The best-measured numbers are the local ones, and they are the least transferable. Certainty and representativeness run in opposite directions.***

Sources: LBNL 2025 Update; EPRI 2026; IEA 2026; Xiao et al. 2025 + code; JLARC; CSO Ireland
{: .small }

---

## What nobody measures

![Slide 25: what nobody measures, and one new exception — a satellite-based estimate of nitrogen oxides from the gas-turbine plant in Southaven, Mississippi](/assets/img/posts/2026-09-18-ai-environmental-impact-25.png)

**The thing everyone argues about is the thing least often measured**

- **No national metering system separates AI** from other data-centre use — all four metered series say so.
- As of mid-2024, **1 of 13** major AI chip buyers had ever disclosed the scale of its AI electricity use.
- **None of Google, Microsoft, Amazon or Meta splits AI from other workloads** in its environmental reports (2025–26).
- **No one outside the companies has measured a query to the closed services most students use** (ChatGPT, Gemini, Claude). Independent labs do now measure large *open* models, GPU energy only (46 models, January 2026).
- The EU's mandatory register covers **36%** of the EU's estimated data centres. The first US government pilot surveys (2026) **do not ask about water**.

> **One new exception — a preprint, one site, 2026.** Satellite data were used to estimate **~730 kg/h** of nitrogen oxides (the mean of eleven two-week estimates, March to mid-August 2026) from the gas-turbine plant in Southaven, Mississippi, built to power SpaceXAI's nearby Colossus 2 data centre.
>
> - **Start with the plant next door.** The Tennessee Valley Authority's combined-cycle plant **1.5 km away reported 21 ± 3 kg/h on its own stack monitors** over an overlapping window. Same pollutant, same air, both period averages.
> - The authors also put their estimate at **about 16×** the **~47 kg/h** in the site's March 2026 permit. That 47 is the **sum of per-turbine hourly caps for 41 permanent, pollution-controlled turbines all running at once** — a ceiling on equipment that had not been built, not a rate anything emitted.
> - What was running: **up to 69 temporary turbines**, without air permits, under a state exemption that a federal lawsuit disputes. How many had pollution controls is also disputed.
> - *The method was calibrated on four other power plants, and it cannot detect emissions as low as the permitted level.* **These emissions are behind the meter: they appear in no grid-electricity statistic, so no national share on the earlier slides can see them.**

Sources: Masanet, Lei & Koomey 2024; ML.ENERGY 2026; EC DG ENER 2025; EIA 2026; Gauld et al. 2026 (preprint); MDEQ permit 0680-00119
{: .small }

---

## Air: two sites, two kinds of document

![Slide 26: two Memphis-area sites — a permit at Colossus 1 in South Memphis, a satellite-based estimate at Colossus 2's power plant in Southaven — with an aerial photograph of the Memphis site](/assets/img/posts/2026-09-18-ai-environmental-impact-26.png)

**SpaceXAI (xAI until Feb 2026) has run gas turbines at two sites near Memphis. One has a permit you can read. One has a satellite-based estimate. Neither alone tells you what the air received.**

### Colossus 1 — South Memphis, Tennessee

*a permit: a legal ceiling, not a measurement*

- The county's evaluation (March 2025) of an application for **15 turbines**, rated 16.48 MW each, caps nitrogen oxides at **87 short tons a year** — a **legal ceiling, not a measurement**, which makes the plant a "synthetic minor" source below federal major-source thresholds.
- **Up to 35 turbines** were at the site in April 2025, before the permit was issued (35 is the site total, not 35 extra), **running under a claimed federal "nonroad engine" exemption**: the county accepted it, the Southern Environmental Law Center disputed it.
- The county board **dismissed an appeal as moot, 6–1** (December 2025), after the temporary turbines had left.

*Photo caption:* xAI's Memphis site from the air, **31 March 2025** — three months before the permit was issued. Photograph **Steve Jones**; flight by **Southwings for the Southern Environmental Law Center**, which appealed the permit. A daylight aerial: the camera recorded equipment, not emissions.
{: .small }

### Colossus 2's power plant — Southaven, Mississippi

*an estimate, against a permit for different equipment*

- **Start with the plant next door.** Satellite data put the turbine site at **~730 kg/h** of NOx — the mean of eleven two-week estimates, March to mid-August 2026, spread ±185, no median published. The Tennessee Valley Authority's combined-cycle plant **1.5 km away reported 21 ± 3 kg/h on its own stack monitors** over an overlapping window. Same pollutant, same air, both period averages.
- The state permit (March 2026) covers **41 permanent turbines with pollution controls** (1.24 GW). Their per-turbine short-term limits, summed as though all 41 ran at the limit at once, come to about **47 kg/h**. The preprint's authors put their estimate at **about 16×** that sum — a ratio of an observed rate to a legal ceiling, not of two rates.
- **But the 41 permanent turbines weren't running yet.** Up to **69 temporary, trailer-mounted turbines** were, without air permits, under the state's "mobile and temporary" exemption. A federal lawsuit disputes it; the US Justice Department has intervened on the company's side.
- **How many had pollution controls is disputed.** The researchers, citing the state's order, say 14 of 69. The company says all its mobile turbines have "advanced emission control technologies", without giving a count.

> **The legal record, at both sites.** Those retirement dates exist because the exemption ran **12 months from arrival** (Aug 2025 → Aug 2026): an MDEQ agreed order of **30 July 2026** let **13 turbines** run past the deadline, three by up to **five months**, at the company's request after supply-chain delays on the 41 permanent turbines. **No penalty is reported.** **And neither site produced a ruling on the question itself** — whether a trailer-mounted turbine is a stationary source. Memphis: the turbines left, then the appeal was dismissed as moot; the removal defeated the challenge rather than resulting from it. Southaven: the August 2026 injunction hearing was postponed, the Justice Department intervened (June 2026) and moved to dismiss citing national security, and retirement proceeds on a negotiated schedule.

**And none of it appears in any national number.** Both sites generate their own power **behind the meter**, so every national and world share earlier in this talk is blind to these emissions by construction. A national average is not an instrument for a local question.

***What this shows:*** *a permit caps only the equipment it names; state records show what ran; only a measurement could estimate what it emitted; and the question is undecided at both sites — which denies the alarmed reading a finding of illegality and the reassuring reading a finding of compliance. The satellite study is a preprint at a single site, calibrated on four other power plants, and its method cannot detect emissions as low as the permitted level.*

Sources: Shelby County 01156-01PC; MDEQ 0680-00119 and agreed order 30 Jul 2026; Gauld et al. 2026 (preprint); Mississippi Today 31 Jul 2026
{: .small }

---

## Two famous numbers, and what happened to them

![Slide 27: two famous numbers — the 1999 claim that the internet uses 8% of US electricity, and the 2019 table row headed "Training one model"](/assets/img/posts/2026-09-18-ai-environmental-impact-27.png)

**Numbers lose their qualifiers in transit**

### 1999: "The internet uses 8% of US electricity"

- …and all office, telecom and network equipment 13%, heading for **half** within a decade. *(Mills & Huber, Forbes; the underlying report was funded through a coal-industry group.)*
- **Berkeley Lab (Koomey, 2000)** put **all** office, telecom and network equipment at **2.6%** of US electricity, or **3.2%** including the power to manufacture it — "about a factor of four lower than Mills' estimate for the electricity demand of 'the digital economy'." Correcting **Mills's own** arithmetic cut his internet figure about **8×**, and Berkeley would not publish an internet-only figure at all.
- **The 1999 claim overstated.**

### 2019: a table row headed "Training one model"

- It gave **626,155 lb CO₂e** (≈284 t) for an automated search over thousands of candidate designs, beside a car's lifetime emissions (126,000 lb). A tweet of that table spread as "five cars". The headline: "Training a single AI model **can** emit as much carbon as five cars in their lifetimes."
- **Google researchers (2021)** — a group that includes the authors of the searched-for model — put the same search at **3.2 t**: **88×** lower, stated conditionally, "for energy-efficient organizations like Google". **18.7×** of that is like-for-like, correcting only how the search had been read; the rest is newer chips and a better-run building.
- **What a large 2024 run cost, as disclosed.** Meta's Llama 3.1 405B pre-training: **8,930 t CO₂e** location-based, **0 t** market-based. The 8B model: **420 t**. The three together: **11,390 t**. Final training runs only.
- **Both lost a qualifier.** The 2019 figure overstated the search it described, and was never a figure for training one model. Read that way it understates today's largest disclosed runs — but **by no stateable multiple**: its denominator is the number this slide has just reported as 88× too high.

Sources: Mills & Huber 1999; Koomey, LBNL-46509 (2000); Strubell et al. 2019; Patterson et al. 2021; Meta model cards
{: .small }

---

## Beyond the power bill: buildings and chips

![Slide 28: what most published numbers leave out — embodied emissions from making chips and buildings, and the water used by chip factories](/assets/img/posts/2026-09-18-ai-environmental-impact-28.png)

**Most published numbers count only the electricity used to run the chips**

- **Making the chips and building the data centres ("embodied" emissions):** about **30%** of Meta's AI tasks' emissions, counted on the local grid average (2022); **more than half** of large AI data centres' emissions — **50–82% of data-centre emissions** in its one numeric statement — in a 2026 review that states no carbon basis and whose own boundary figure covers **server manufacturing only**.
- **In BLOOM's fully counted training run,** hardware was **22%**, on France's very clean grid. On a grid of about 390 g CO₂e/kWh the same hardware would be about **4%**.
- **NVIDIA's first published figure (2025):** **1,312 kg CO₂e** to manufacture one 8-GPU H100 board.
- **A trade-off:** cutting a data centre's water use and cutting its carbon "can be negatively coupled … in some cases" (2026 review). Microsoft said in December 2024 that its new designs will avoid the need for more than **125 million litres of water a year** per data centre, with a "nominal increase" in energy use; pilots begin in 2026.
- **A chip factory** "can use" about **10 million gallons (38 million litres) of ultra-pure water a day** (World Economic Forum, 2024). That is water **drawn**, not water consumed.

*None of these is included in the electricity or water shares on the earlier slides.*

Sources: Wu et al. 2022 (Meta); Chien et al. 2026; BLOOM 2023; NVIDIA 2025; Microsoft Dec 2024; WEF 2024
{: .small }

---

## How to check any number yourself

![Slide 29: four questions for checking any number](/assets/img/posts/2026-09-18-ai-environmental-impact-29.png)

1. **A share of what, and which year?**  
   Energy, capacity, water *withdrawn* or water *consumed*? All data centres, or AI? Are the top and bottom of the fraction from the same year?
2. **What did someone physically record, and how many assumptions stand between that and the claim?**  
   A meter reading, a satellite column, a permit application, a sales record — then every step after it.
3. **Which way can the method be wrong?**  
   A permit caps only the equipment it names. A connection request is not a building. A company disclosure chooses its own boundary. A model built on sales records can err either way.
4. **And when a number is a multiple, what kind of thing is on each side?**  
   A mean, a median, a total, a smallest, a largest, or a legal limit. If the source publishes no middle, the multiple is not a measurement.

**If a number has no base, no year or no boundary, it isn't finished yet.**

---

## Two of these are not mine

![Slide 30: the three cards again — Provenance, Substitution, Environment — with the first two highlighted](/assets/img/posts/2026-09-18-ai-environmental-impact-30.png)

| Provenance | Substitution | Environment |
|---|---|---|
| *the end of attribution* | *replacement and its consequences* | *sudden industrial scaling and its costs* |
| artist images<br>writings<br>music<br>video | social media manipulation<br>artists and content-creators out of work<br>AI content slop | energy<br>carbon footprint<br>water use<br>pollution |

*There are others I haven’t studied.*

> On the first two I can only speak to what I have seen with undergraduates — and the objections run strong. For some of them strong enough that raising the subject at all shuts the conversation down.
>
> All three of these matter to them. We have to start somewhere, and this is the one I can put numbers on.

---

## Since this WILL come up…

![Slide 31: the AGI question, with film stills from The Matrix and 2001: A Space Odyssey](/assets/img/posts/2026-09-18-ai-environmental-impact-31.png)

**Will these systems reach general human intelligence — artificial general intelligence (AGI) — or pass it?**

> **RAND on the state of AGI forecasting, 24 March 2026**
>
> “Substantial disagreement remains even when definitions and information are held constant.” The field “lacks resolved forecasts for calibration; benchmarks resistant to saturation and gaming; continuous, real-time insight into model capabilities; and independent validation of influential models.”

**Karpathy, October 2025**  
Roughly a decade — on stated intuition, not a model: “it feels like a decade to me.” Names continual learning as one of several missing pieces.

**What I can see, on this question**  
How much instruction tuning changed the weights, and where — its rank and its location. Not what those directions mean, and not the circuits behind a behaviour. That needs causal intervention, which I haven’t done.

*Company leaders forecasting two years are raising money. Organisations whose purpose is AI-safety advocacy have an interest in short timelines. Forecaster tournaments have known long-horizon pathologies. It cuts every way.*

**Fiction is the only place anyone knows the timeline!  :)**

*Image captions:* ***The Matrix, 1999*** (a still subtitled “We marveled at our own magnificence as we gave birth to AI.”) · **“I’m sorry, Dave. I’m afraid I can’t do that.”** ***2001: A Space Odyssey, 1968***
{: .small }

---

## What I answered, and what I didn’t

![Slide 32: the three cards, with Environment highlighted, and three closing lines](/assets/img/posts/2026-09-18-ai-environmental-impact-32.png)

| Provenance | Substitution | Environment |
|---|---|---|
| *the end of attribution* | *replacement and its consequences* | *sudden industrial scaling and its costs* |
| artist images<br>writings<br>music<br>video | social media manipulation<br>artists and content-creators out of work<br>AI content slop | energy<br>carbon footprint<br>water use<br>pollution |

You have seen what has been **measured**.

You have seen what has been **modelled**.

And you have seen where the **boundary** between them sits.

---

*If you find an error on any slide, I'd like to hear about it. My email is linked in the sidebar.*

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
