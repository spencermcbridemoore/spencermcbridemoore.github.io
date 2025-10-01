---
title: "Placed in 2019 IBM Quantum Hackathon: Part 2"
author: Spencer Moore
date: 2020-02-15
categories: [hackathon, quantum computing]
tags: [IBM, hackathon, quantum computing]
description: "IBM Grover's Algorithm Hackathon: details"
---


## Let’s look at the basis of the calculation
![Basis of calculation](/assets/img/posts/2019-q-hackathon-87.gif)

Color-codes the huge circuit into **Initialization** (green), **Phase Oracle** (blue), and **Diffusion Operator** (red) blocks.

---

## Requirements – Part 1
![Requirements Part 1](/assets/img/posts/2019-q-hackathon-88.gif)

Zooms in on the initialization and diffusion operator sections of the 62-qubit circuit.

---

## Requirements – Part 2
![Requirements Part 2](/assets/img/posts/2019-q-hackathon-89.gif)

Introduces the 7-location graph problem and shows the oracle sub-circuit mapping those locations.

---

## Requirements – Combined
![Requirements Combined](/assets/img/posts/2019-q-hackathon-90.gif)

Reassembles Parts 1 & 2 into the full 62-qubit Grover circuit.

---

## First Simplification – 21-Input Toffoli
![21-input Toffoli](/assets/img/posts/2019-q-hackathon-91.gif)

Replaces an 81-qubit oracle with a 21-control Toffoli, reducing ancilla overhead.

---

## Example 8-Input Toffoli Decomposition
![8-input Toffoli](/assets/img/posts/2019-q-hackathon-92.gif)

Shows how a multi-controlled Toffoli can be broken into CNOT ladders plus ancilla qubits.

---

## Small Problem
![Small problem](/assets/img/posts/2019-q-hackathon-93.gif)

Marks the initialization block that limits qubit count when scaling Grover’s algorithm.

---

## Hand Waving – Reversibility & Resource Estimates
![Reversibility collage](/assets/img/posts/2019-q-hackathon-94_plus_quantum_collage.jpg)

Explains uncomputing to free qubits, compares 62- vs. 81-qubit versions, and displays the final result histogram.

---

## So about this score…
![Leaderboard slide](/assets/img/posts/2019-q-hackathon-98.gif)

Screenshot of the IBM Quantum Challenge leaderboard highlighting team **SpoonBoyAndThePotentials** and their submission score.

