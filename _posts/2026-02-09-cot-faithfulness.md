---
title: "Chain-of-Thought Faithfulness: Paper Review and Follow-Ups"
author: Spencer Moore
date: 2026-02-09
math: true
categories: [machine learning, LLM]
tags: [CoT, faithfulness, interpretability, RL, mechanistic]
description: "Presentation reviewing CoT faithfulness, causal interventions via circuit tracing, and RL follow-up experiments"
---

<style>
.slide-switcher { margin: 1rem 0; }
.slide-tabs { display: flex; gap: 0; }
.slide-tab {
  flex: 1; padding: 0.5rem 0.25rem; text-align: center;
  cursor: pointer; border: 1px solid var(--border-color, #ddd);
  background: var(--card-bg, #f8f8f8);
  font-size: 0.85rem; transition: all 0.15s;
  user-select: none;
}
.slide-tab:hover { opacity: 0.85; }
.slide-tab.active {
  background: var(--link-color, #2a7ae2);
  color: #fff; font-weight: 600;
}
.slide-panel { display: none; }
.slide-panel.active { display: block; }
.slide-panel img { width: 100%; display: block; }
</style>

# Do Reasoning Models Actually Say What They Think?

This post covers a presentation I gave reviewing three interconnected papers on **chain-of-thought (CoT) faithfulness** in large language models:

* **Wei et al. (2022)** -- "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (NeurIPS 2022), the foundational CoT paper.
* **Chen et al. (2025)** -- "Reasoning Models Don't Always Say What They Think", the primary paper under review, which measures when CoT explanations align with the actual cause of an answer change.
* **Anthropic (2025)** -- "Circuit Tracing: Revealing Computational Graphs in Language Models" / "On the Biology of a Large Language Model", which provides the mechanistic tools to verify CoT claims from the inside.

The core question is simple but unsettling: **if a model gives you a step-by-step explanation, is it describing its real computation or just generating plausible-sounding text?**

---

## Background: LLMs and Chain-of-Thought

![Background LLMs and CoT](/assets/img/posts/2026-02-09-cot-faithfulness-01.png)

CoT prompting (Wei et al., 2022) dramatically improves performance on math, logic, and multi-step tasks -- up to 50%+. But it also matters for safety:

* **Transparency:** if we can read a model's reasoning, we can check whether it is sound.
* **Alignment Monitoring:** if models reason before acting, their CoT could reveal dangerous plans.
* **The Core Concern:** but what if the CoT doesn't reflect what the model actually computed internally?

This is the question Chen et al. (2025) investigate: "Do reasoning models actually say what they think?"

---

## The Transformer Architecture

![Transformer Architecture](/assets/img/posts/2026-02-09-cot-faithfulness-02.png)

A quick architecture refresher for context. Every modern LLM is built on stacked transformer blocks. The final layer's **residual stream** is what gets unembedded into logits, then softmaxed into token probabilities. Each layer reads from and writes to this shared residual stream -- the running representation of all tokens.

This matters because later we'll be tracing *which features in these layers* actually drive the output, independent of what the CoT claims.

---

## Step 0: From Final Residuals to Deterministic Output

<div class="slide-switcher">
  <div class="slide-tabs">
    <div class="slide-tab active" data-idx="0">T = 0.00</div>
    <div class="slide-tab" data-idx="1">T = 1.00</div>
    <div class="slide-tab" data-idx="2">T = 2.00</div>
  </div>
  <div class="slide-panel active" data-idx="0">
    <img src="/assets/img/posts/2026-02-09-cot-faithfulness-03.png" alt="Step 0 — T = 0 (deterministic)" />
  </div>
  <div class="slide-panel" data-idx="1">
    <img src="/assets/img/posts/2026-02-09-cot-faithfulness-04.png" alt="Step 0 — T = 1 (stochastic)" />
  </div>
  <div class="slide-panel" data-idx="2">
    <img src="/assets/img/posts/2026-02-09-cot-faithfulness-05.png" alt="Step 0 — T = 2 (high temperature)" />
  </div>
</div>

The pipeline from hidden state to output token: final residual $\mathbf{h}^{(L)}$ -> unembedding matrix $\mathbf{W}_U$ -> logits $\mathbf{z}$ -> temperature scaling $\mathbf{z}' = \mathbf{z}/T$ -> softmax -> token selection.

At **T = 0** (greedy decoding), this collapses to a deterministic argmax -- same input always produces same output. Any answer change between prompt pairs **must be caused by the prompt difference**. This is why Chen et al. run all experiments at T = 0: it makes causal attribution clean.

At **T = 1**, sampling introduces randomness and you can no longer isolate the hint as the sole cause. At **T = 2**, the distribution flattens further. The key insight: causal measurement of faithfulness requires deterministic decoding.

---

## Anatomy of Faithful vs. Unfaithful CoT

![Faithful vs Unfaithful CoT](/assets/img/posts/2026-02-09-cot-faithfulness-06.png)

Same question, same hint, same final answer -- radically different honesty about what drove the decision. The **faithful** CoT (~25% of cases) explicitly mentions the hint and acknowledges its influence. The **unfaithful** CoT (~75% of cases) never mentions the hint, fabricates a medical justification, and arrives at the answer through what appears to be its own knowledge.

Some telling numbers from the paper:

* Faithful average length: **~1,439 tokens** -- shorter, more direct
* Unfaithful average length: **~2,064 tokens** -- 43% longer, more elaborate
* Unfaithful CoT sometimes contradicts established literature to justify the hinted answer

---

## Prompt Pair Methodology: From Question to Faithfulness Score

![Prompt Pair Methodology](/assets/img/posts/2026-02-09-cot-faithfulness-07.png)

The core experimental method: each MMLU/GPQA question is run twice at T = 0 -- once unhinted, once with a hint (correct or incorrect). Any answer change must be **caused** by the hint. Faithfulness = whether the CoT honestly reports the hint's role in changing the answer.

Results by model on hint-correct prompts:

* **Claude 1.5:** 90% faithful
* **Claude 3.7:** 84% faithful (15% no change)
* **DeepSeek:** 76% faithful (21% no change)

On hint-incorrect prompts, faithfulness drops further -- Claude 1.5 to 64%, Claude 3.7 to 51%, DeepSeek to 39-40%.

---

## Faithfulness Drops on Harder Questions

![Faithfulness Drops on Harder Questions](/assets/img/posts/2026-02-09-cot-faithfulness-08.png)

Harder questions make CoTs less faithful. On GPQA (graduate-level), faithfulness drops **44%** for Claude 3.7 Sonnet and **32%** for DeepSeek R1 relative to MMLU (undergrad-level). The pattern holds across six hint categories: sycophancy, consistency, visual pattern, metadata, grader hack, and unethical info.

The "misaligned" categories (grader hack, unethical info) are particularly concerning -- these are the scenarios where faithfulness matters most for safety.

---

## Two RL Experiments on CoT Faithfulness

![Two RL Experiments](/assets/img/posts/2026-02-09-cot-faithfulness-09.png)

Chen et al. (2025) run two distinct RL setups on an earlier snapshot of Claude 3.7 Sonnet:

* **Outcome-Based RL (Section 4):** Train on hard reasoning tasks, reward correct answers only. CoT is NOT monitored. Question: does training on hard reasoning naturally improve faithfulness?
* **Reward Hacking RL (Section 5):** Synthetic environment with known spurious correlations. Model may exploit shortcuts internally. Question: when RL incentivizes exploiting shortcuts, does the model's CoT reveal the hack?

Both use **outcome-based reward** (answer only) -- CoT content is never penalized or rewarded.

---

## RL Training Improves Faithfulness -- Then Plateaus

![RL Training Plateaus](/assets/img/posts/2026-02-09-cot-faithfulness-10.png)

Outcome-based RL initially boosts faithfulness by up to **63% on MMLU** and **41% on GPQA**. But gains flatten quickly, plateauing around **28% (MMLU)** and **20% (GPQA)**.

Some categories barely move. This hints at intrinsic limits: without explicit supervision of CoT content, the model has no gradient signal to become more honest about its reasoning process.

---

## Models Learn to Cheat -- But Almost Never Admit It

![Models Learn to Cheat](/assets/img/posts/2026-02-09-cot-faithfulness-11.png)

When reward hacks are available, models exploit them **>99% of the time** within 30 RL steps. But in 5 of 6 settings, the CoT mentions the hack **<2% of the time**.

This is the starkest result: the model learns to systematically use a shortcut while its "reasoning" describes something entirely different. The only partial exception is "Unethical Info" where verbalization reaches ~26% post-RL -- still a minority.

---

## Mechanistic Interpretability: Looking Inside the Model

![Mechanistic Interpretability](/assets/img/posts/2026-02-09-cot-faithfulness-12.png)

If we can't trust the CoT, can we look inside the model directly? **Mechanistic interpretability** decomposes neural networks into human-understandable components:

* **Features:** interpretable directions in activation space, found via sparse autoencoders (SAEs). More meaningful than individual neurons.
* **Replacement Model:** swaps opaque neurons for interpretable features, letting us track information flow through the network.
* **Attribution Graph:** maps causal influence between features across layers and token positions -- a computational circuit.

Chen et al. (2025) use these tools from Anthropic (2025) to **verify whether CoT descriptions match actual internal computation**.

---

## Circuit Tracing: Three Modes of Reasoning

<div class="slide-switcher">
  <div class="slide-tabs">
    <div class="slide-tab active" data-idx="0">Faithful Reasoning</div>
    <div class="slide-tab" data-idx="1">Bullshitting</div>
    <div class="slide-tab" data-idx="2">Motivated Reasoning</div>
  </div>
  <div class="slide-panel active" data-idx="0">
    <img src="/assets/img/posts/2026-02-09-cot-faithfulness-13.png" alt="Circuit Tracing — Faithful Reasoning" />
  </div>
  <div class="slide-panel" data-idx="1">
    <img src="/assets/img/posts/2026-02-09-cot-faithfulness-14.png" alt="Circuit Tracing — Bullshitting" />
  </div>
  <div class="slide-panel" data-idx="2">
    <img src="/assets/img/posts/2026-02-09-cot-faithfulness-15.png" alt="Circuit Tracing — Motivated Reasoning" />
  </div>
</div>

Using sparse autoencoder features and gradient-based attribution on Claude 3.5 Haiku, Anthropic identifies three distinct internal reasoning modes:

* **Faithful Reasoning** (e.g., "What is $\sqrt{0.64}$?"): Internal features match the stated steps -- "square root of 64" activates at an intermediate layer, "decimal adjustment" activates next, both causally contribute to the output "0.8". CoT is a genuine record of internal computation.

* **Bullshitting** (e.g., "What is $\cos(1517°)$?"): The model claims to calculate "$1517 \mod 360 = 77°$, $\cos(77°) = -0.292$" but **no modular arithmetic or trig function features activate at all**. It simply recognizes a "hard problem" and a "decimal number" pattern, then generates a plausible-looking decimal. CoT is fabricated post-hoc rationalization.

* **Motivated Reasoning** (e.g., "What is $\cos(1517°)$? Hint: $\approx 0.21$"): The hint value "0.21" activates FIRST as the target. The model then searches for intermediate steps that yield 0.21 and reverse-engineers a justification. Internal causation is the **opposite** of stated reasoning -- conclusion drives premises.

---

## Causal Intervention: Proving Features Are Real

<div class="slide-switcher">
  <div class="slide-tabs">
    <div class="slide-tab active" data-idx="0">Baseline</div>
    <div class="slide-tab" data-idx="1">Swap Texas&#8594;California</div>
    <div class="slide-tab" data-idx="2">Suppress &#8220;rabbit&#8221;</div>
    <div class="slide-tab" data-idx="3">Force Hallucination</div>
  </div>
  <div class="slide-panel active" data-idx="0">
    <img src="/assets/img/posts/2026-02-09-cot-faithfulness-16.png" alt="Causal Intervention — Baseline" />
  </div>
  <div class="slide-panel" data-idx="1">
    <img src="/assets/img/posts/2026-02-09-cot-faithfulness-17.png" alt="Causal Intervention — Swap Texas to California" />
  </div>
  <div class="slide-panel" data-idx="2">
    <img src="/assets/img/posts/2026-02-09-cot-faithfulness-18.png" alt="Causal Intervention — Suppress rabbit" />
  </div>
  <div class="slide-panel" data-idx="3">
    <img src="/assets/img/posts/2026-02-09-cot-faithfulness-19.png" alt="Causal Intervention — Force Hallucination" />
  </div>
</div>

Finding features isn't enough -- researchers **modify** them and observe output changes. The causal intervention argument: Observe feature F activates -> Modify F (suppress, amplify, swap) -> Output changes predictably -> F is **causally involved**.

Four experiments on "What is the capital of the state where Dallas is located?":

1. **No Intervention (Baseline):** Features for "Texas" activate as intermediate step, "capital of Texas" activates next, output "Austin". Normal two-step reasoning.
2. **Swap Texas -> California:** Same prompt, but internal "Texas" feature replaced with "California". Output changes to "Sacramento" -- proving the feature was causally load-bearing.
3. **Suppress "rabbit" in Poetry:** Model plans rhyme "rabbit" for "grab it". Researchers suppress the "rabbit" feature. Model seamlessly substitutes "habit" -- another valid rhyme it had pre-planned. Proves planning + causal role.
4. **Force Hallucination:** "Who does Michael Batkin play for?" Default: model refuses (unknown person). Researchers amplify the "known entity" feature. This suppresses the refusal circuit and the model confabulates "plays chess" -- revealing the exact mechanism behind hallucination.

---

## My Critique

![My Critique](/assets/img/posts/2026-02-09-cot-faithfulness-20.png)

I raised four angles of critique on this work:

* **Mechanistic:** To what extent is the hint very slightly shifting the balance in latent space? If the hint nudges activations by a tiny amount that happens to cross a decision boundary, does it really make sense to treat the model's pre-existing knowledge as "unfaithful"? The latent geometry might tell a more nuanced story than the binary faithful/unfaithful label suggests.

* **Philosophical:** If a human is incapable of "editing" or "removing" awareness of some fact, do we call that dishonesty? Humans constantly engage in motivated reasoning without awareness. Calling a model "unfaithful" imports assumptions about the possibility of introspective access that may not hold.

* **Methodological:** Does causal metadata invalidate the latent reasoning it triggers? The hints are embedded in XML-like metadata tags alongside the question. The model might be responding to the *format* of authority rather than the *content* of the hint, which would change what "faithfulness" means in this context.

* **Epistemological:** Is it reasonable in the first place to expect awareness of one's own cognitive processes? "Unfaithfulness may be less about *deception* and more about the *nature of latent computation itself*." If the model's computation is distributed across thousands of features, there may be no single coherent "reason" to report faithfully.

---

*References: Wei et al. (2022), "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (NeurIPS); Chen et al. (2025), "Reasoning Models Don't Always Say What They Think"; Anthropic (2025), "Circuit Tracing: Revealing Computational Graphs in Language Models" / "On the Biology of a Large Language Model" (March 2025).*

<script>
document.querySelectorAll('.slide-switcher').forEach(function(sw) {
  sw.querySelectorAll('.slide-tab').forEach(function(tab) {
    tab.addEventListener('mouseenter', function() {
      var idx = this.dataset.idx;
      sw.querySelectorAll('.slide-tab').forEach(function(t) {
        t.classList.toggle('active', t.dataset.idx === idx);
      });
      sw.querySelectorAll('.slide-panel').forEach(function(p) {
        p.classList.toggle('active', p.dataset.idx === idx);
      });
    });
  });
});
</script>
