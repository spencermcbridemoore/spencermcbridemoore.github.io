---
title: "Placed in 2019 IBM Quantum Hackathon: Part 1"
author: Spencer Moore
date: 2020-02-01
categories: [hackathon, quantum computing]
tags: [IBM, hackathon, quantum computing]
description: "IBM Grover's Algorithm Hackathon: overview "
---

## IBM Quantum Challenge 2019 — Using Qiskit
![IBM Quantum Challenge overview](/assets/img/posts/2019-q-hackathon-1to4_qhub_collage.png)

First four slides of my presentation of the virtual hackathon, spells out the intended audience (“not familiar” vs. “have studied” quantum computing), and shows the web portal and final challenge screen.

---

# Terminology
![Terminology slide](/assets/img/posts/2019-q-hackathon-14to18.gif)

Defines **state**, **measurement**, and **calculation** while showing a canonical N-qubit circuit diagram.

---

## What does this have to do with Qiskit?
![Qiskit statevector slide](/assets/img/posts/2019-q-hackathon-23.gif)

Highlights `Result.get_statevector()` in the Qiskit API to connect the theory with hands-on tooling.

---

## Google vs. IBM

Here is IBM's paper discussing Google’s Sycamore 54-qubit computer which, as I chave disucssed, is described by a state vector of $2^{54}$ complex numbers. This state can (utilizing a few tricks) just barely fit into the with the Summit supercomputer, listing node counts and aggregate RAM.

![Google vs. IBM slide](/assets/img/posts/2019-q-hackathon-31.gif)

$$
\begin{aligned}
& \text{Number of Petabytes (PB)}=2^{N}\,\cdot M \cdot\frac{1\,\,\text{Petabyte}}{10^{15}\,\,\text{Bytes}} \\
& M = \text{Bytes/Complex-number} N=\text{Qubit Count} \\
& \text{Example:}\quad M=8 \text{ (Complex128)},N=54~\Rightarrow~\text{PB}\approx 144.12
\end{aligned}
$$


So we can see here that (as IBM gets into in their paper) the size of the state vector is not theoretical. It does require 

---

## What we measure…
![Measurement outcomes slide](/assets/img/posts/2019-q-hackathon-33to40.gif)

Shows how circuit measurements map to classical bit-strings \(C_0 … C_{2^N-1}\).

---

# Grover’s Algorithm with 3 Qubits
![Grover 3-qubit overview](/assets/img/posts/2019-q-hackathon-61to64.gif)

Top: textbook block diagram of the algorithm.  
Bottom: the actual Qiskit circuit implementing one Grover iteration.

---

## Grover Step 1 – Initialize
![Initialize step](/assets/img/posts/2019-q-hackathon-65_ish_grover_steps.gif)

Applies Hadamards to all qubits, produces the uniform superposition state, and shows the equal-amplitude column vector.

---

## Initialize & Measure
![Initialize & Measure](/assets/img/posts/2019-q-hackathon-71_ish.gif)

Compares the raw amplitude table with the measured probability histogram after immediate read-out.

---

## One Full Iteration & Measure
![One iteration & measure](/assets/img/posts/2019-q-hackathon-73_ish.gif)

Demonstrates a single Grover iteration: rotation in the two-dimensional {|w⟩, |s⟩} space and the corresponding histogram peak.

---

## Initialize, Phase Oracle & Measure
![Initialize, Oracle & Measure](/assets/img/posts/2019-q-hackathon-75_ish.gif)

Isolates the effect of applying only the phase oracle before measurement.
