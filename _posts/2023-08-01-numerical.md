---
title: "Presentation on Numerical Methods: Runge-Kutta Numerical Integration & Example Use in Neutron Transport"
author: Spencer Moore
date: 2023-08-01
categories: [numerical, quantum]
tags: [Numerical, Modeling, Quantum RF]
description: "Presentation for Prospective Numerical Quantum RF Project: Runge-Kutta"
---

## Introduction

This post gives covers the initial part of my presentation to Army Research Lab (ARL) on **Runge-Kutta numerical integration methods**, starting from the basics of Euler’s method, extending to higher-order Taylor expansions, and finally applying them to a real-world physics problem: **neutron transport and spin precession**.

---

## Numerical Integration

![Numerical Integration](/assets/img/posts/runge-kutta/page_6.png)

As seen in this post we start with an ordinary differential equation (ODE):

\[
\frac{dy(t)}{dt} = f(t, y(t)), \quad y(t_0) = y_0
\]

Our goal is to approximate \( y(t_0 + h) \) when no analytic solution exists.  
This leads us into numerical integration methods.

---

## Euler’s Method (First Order)

![Euler's Method](/assets/img/posts/runge-kutta/page_7.png)

Euler’s method is the simplest numerical approach, using the **instantaneous slope** to extrapolate forward:

\[
y_{n+1} = y_n + h f(t_n, y_n)
\]

This corresponds to a first-order Taylor expansion with error \( O(h^2) \).

---

## Runge-Kutta: Higher Orders

![Runge-Kutta Higher Orders](/assets/img/posts/runge-kutta/page_8.png)

Runge-Kutta methods generalize this approach by taking **multiple weighted evaluations** of \( f(t, y) \) within a step.  
They are summarized by the **Butcher Tableau**, which encodes the recursive scheme.

---

## Runge-Kutta 4th Order (RK4)

![Runge-Kutta 4th Order](/assets/img/posts/runge-kutta/page_9.png)

The most widely used is **RK4**, which balances accuracy and computational cost:

\[
y_{n+1} = y_n + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)
\]

This gives error \( O(h^5) \), making it very efficient for many physical simulations.

---

## Runge-Kutta with Adaptive Step Size

![Runge-Kutta Higher Orders Adaptive](/assets/img/posts/runge-kutta/page_10.png)

By comparing two Runge-Kutta methods of different order (e.g., Cash-Karp RK45), one can estimate the local error and **adapt the step size**.  
This avoids wasted computation on smooth regions and ensures accuracy in rapidly changing dynamics.

---

## Application: Neutron Transport at LANL

![LANL Neutron Science Center](/assets/img/posts/runge-kutta/page_11.png)

At LANL’s Neutron Science Center, Runge-Kutta methods were used to simulate **neutron transport through spin-flipper devices**.  
The challenge: the system had both strong static fields and **time-dependent RF fields**, making the ODEs stiff and requiring careful step-size control.

---

## Halbach Array and Neutron Trapping

![Halbach Array Neutron Bottle](/assets/img/posts/runge-kutta/page_12.png)

Simulations also reproduced effects like **neutron bottles** using Halbach arrays.  
These arrays create steep magnetic gradients, effectively trapping neutrons like a "neutron trampoline."

---

## Previous Project: Ultra-Cold Neutron Spin Precession

![UCN Spin Precession Code](/assets/img/posts/runge-kutta/page_13.png)

Runge-Kutta methods were implemented in CUDA to simulate **neutron spin precession** in magnetic fields, using Maxwell-generation GPUs for acceleration.

---

## Full System of Equations

![System of ODEs](/assets/img/posts/runge-kutta/page_14.png)

The system combines velocity, force, and spin-precession equations:

\[
\frac{d\vec{\mu}(t)}{dt} = \vec{\mu}(t) \times \vec{B}(t), 
\quad
\vec{F}(t) = -\nabla (\vec{\mu}(t) \cdot \vec{B}(t)) + m_n \vec{g}
\]

This leads to a large coupled system of ODEs, handled efficiently with **Runge-Kutta Cash-Karp adaptive stepping**.

---

## Stiff Differential Equations

![Stiff Equations](/assets/img/posts/runge-kutta/page_16.png)

Some neutron transport problems are **stiff**, requiring very small time steps for stability.  
Explicit Runge-Kutta methods struggle here, and often implicit methods or specialized solvers are needed.

---

## Conclusion

Runge-Kutta methods, particularly higher-order and adaptive-step variants, are crucial tools in computational physics.  
From basic ODEs to **complex neutron transport and spin dynamics**, they bridge the gap between theory and simulation.

---

*References: Numerical Recipes in C, Butcher (1963), Cash-Karp RK45, LANL Neutron Science Center.*
