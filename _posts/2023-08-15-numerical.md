---
title: "Presentation on Numerical Methods: Lindbladian Runge-Kutta & Applied Computer Science"
author: Spencer Moore
date: 2023-08-01
categories: [numerical, quantum]
tags: [Numerical, Modeling, Quantum RF]
description: "Presentation for Prospective Numerical Quantum RF Project"
---

## Lindbladian Formalism  
**The missing to understanding quantum mechanics in real-world experimental terms**

![Lindbladian Formalism](/assets/img/posts/2023-08-15-numerical-17.png)

---

## Short-Term: Speed  
Big optimizations possible for steady state solvers and time solvers.

![Short Term Speed](/assets/img/posts/2023-08-15-numerical-18.png)

---

## Example Issue: Serialization  
Large memory footprint for NumPy arrays.

![Serialization Issue 1](/assets/img/posts/2023-08-15-numerical-19.png)

---

## Example Issue: Serialization (Lazy Iterators)  
Use generators (`yield`) to reduce memory footprint.

![Serialization Issue 2](/assets/img/posts/2023-08-15-numerical-20.png)

---

## Example Improvement  
Give NumPy fixed, contiguous buffers.

![Example Improvement](../assets/img/posts/2023-08-15-numerical-21.png)

---

## Mid-Term: Functionality & Speed  
Extend time-dependent functions; add GPU parallelization.

![Mid Term Functionality](/assets/img/posts/2023-08-15-numerical-22.png)

---

## Mid-Term: SaaS & BYOH  
Cloud deployment and Dockerized environments.

![Mid Term SaaS](/assets/img/posts/2023-08-15-numerical-23.png)

---

## Mid-Term: Does It Work?  
Experimental verification and validation.

![Mid Term Verification](/assets/img/posts/2023-08-15-numerical-24.png)

---

## Long-Term: Functionality  
If it works there are all kinds of interesting directions to take things.

![Long Term Functionality](/assets/img/posts/2023-08-15-numerical-25.png)

---

## Long-Term: What Errors Build Up?  
Alternate integration approaches: explicit/implicit Runge–Kutta and BDF (stiff ODEs).

![Long Term — Errors Build Up](/assets/img/posts/2023-08-15-numerical-26.png)

---

## Long-Term: What If It’s Too Slow?  
Linear multistep methods and **quantum jump** (MCWF) alternatives.

![Long Term — Too Slow](/assets/img/posts/2023-08-15-numerical-27.png)

---

### Summary
The Lindbladian formalism is both conceptually satisfying and an excellent candidate for practical **Runge–Kutta**. But making something fast and capable of running on a given hardware setup means understanding programming informed by computer science. This means buffered serialization, lazy iterators, possible **GPU acceleration**, and considering additional integration schemes (implicit RK/BDF, multistep, MCWF).