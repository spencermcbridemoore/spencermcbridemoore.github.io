---
title: "Placed in 2019 IBM Quantum Hackathon: Part 2"
author: Spencer Moore
date: 2020-02-15
categories: [hackathon, quantum computing]
tags: [IBM, hackathon, quantum computing]
description: "IBM Grover's Algorithm Hackathon"
---

## IBM Quantum Challenge — Using Qiskit
![IBM Quantum Challenge overview](..\assets\img\posts\2019-q-hackathon-1to4_qhub_collage.png)

A four-panel collage that introduces the virtual hackathon, spells out the intended audience (“not familiar” vs. “have studied” quantum computing), and shows the web portal and final challenge screen.

---

## Terminology
![Terminology slide](..\assets\img\posts\2019-q-hackathon-14to18.gif)

Defines **state**, **measurement**, and **calculation** while showing a canonical N-qubit circuit diagram.

---

## What does this have to do with Qiskit?
![Qiskit statevector slide]( ../assets/img/posts/2019-q-hackathon-23.gif)

Highlights `Result.get_statevector()` in the Qiskit API to connect the theory with hands-on tooling.

---

## Google vs. IBM
![Google vs. IBM slide](..\assets\img\posts\2019-q-hackathon-31.gif)

Contrasts Google’s Sycamore claim with IBM’s Summit supercomputer paper, listing node counts and aggregate RAM.

---

## What we measure…
![Measurement outcomes slide](..\assets\img\posts\2019-q-hackathon-33to40.gif)

Shows how circuit measurements map to classical bit-strings \(C_0 … C_{2^N-1}\).

---

## Grover’s Algorithm with 3 Qubits
![Grover 3-qubit overview](..\assets\img\posts\2019-q-hackathon-61to64.gif)

Top: textbook block diagram of the algorithm.  
Bottom: the actual Qiskit circuit implementing one Grover iteration.

---

## Grover Step 1 – Initialize
![Initialize step](..\assets\img\posts\2019-q-hackathon-65_ish_grover_steps.gif)

Applies Hadamards to all qubits, produces the uniform superposition state, and shows the equal-amplitude column vector.

---

## Initialize & Measure
![Initialize & Measure](..\assets\img\posts\2019-q-hackathon-71_ish.gif)

Compares the raw amplitude table with the measured probability histogram after immediate read-out.

---

## One Full Iteration & Measure
![One iteration & measure](..\assets\img\posts\2019-q-hackathon-73_ish.gif)

Demonstrates a single Grover iteration: rotation in the two-dimensional {|w⟩, |s⟩} space and the corresponding histogram peak.

---

## Initialize, Phase Oracle & Measure
![Initialize, Oracle & Measure](..\assets\img\posts\2019-q-hackathon-75_ish.gif)

Isolates the effect of applying only the phase oracle before measurement.

---

## Let’s look at the basis of the calculation
![Basis of calculation](..\assets\img\posts\2019-q-hackathon-87.gif)

Color-codes the huge circuit into **Initialization** (green), **Phase Oracle** (blue), and **Diffusion Operator** (red) blocks.

---

## Requirements – Part 1
![Requirements Part 1](..\assets\img\posts\2019-q-hackathon-88.gif)

Zooms in on the initialization and diffusion operator sections of the 62-qubit circuit.

---

## Requirements – Part 2
![Requirements Part 2](..\assets\img\posts\2019-q-hackathon-89.gif)

Introduces the 7-location graph problem and shows the oracle sub-circuit mapping those locations.

---

## Requirements – Combined
![Requirements Combined](..\assets\img\posts\2019-q-hackathon-90.gif)

Reassembles Parts 1 & 2 into the full 62-qubit Grover circuit.

---

## First Simplification – 21-Input Toffoli
![21-input Toffoli](..\assets\img\posts\2019-q-hackathon-91.gif)

Replaces an 81-qubit oracle with a 21-control Toffoli, reducing ancilla overhead.

---

## Example 8-Input Toffoli Decomposition
![8-input Toffoli](..\assets\img\posts\2019-q-hackathon-92.gif)

Shows how a multi-controlled Toffoli can be broken into CNOT ladders plus ancilla qubits.

---

## Small Problem
![Small problem](..\assets\img\posts\2019-q-hackathon-93.gif)

Marks the initialization block that limits qubit count when scaling Grover’s algorithm.

---

## Hand Waving – Reversibility & Resource Estimates
![Reversibility collage](..\assets\img\posts\2019-q-hackathon-94_plus_quantum_collage.jpg)

Explains uncomputing to free qubits, compares 62- vs. 81-qubit versions, and displays the final result histogram.

---

## So about this score…
![Leaderboard slide](..\assets\img\posts\2019-q-hackathon-98.gif)

Screenshot of the IBM Quantum Challenge leaderboard highlighting team **SpoonBoyAndThePotentials** and their submission score.

