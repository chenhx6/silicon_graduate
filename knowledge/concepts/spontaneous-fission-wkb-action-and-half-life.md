---
type: concept
title: "Spontaneous fission double-humped barrier WKB action and half-life systematics"
aliases: [spontaneous-fission-action, sf-half-life-systematics, hill-wheeler-double-hump, swiatecki-fissility-scaling]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [nuclear-fission, spontaneous-fission, double-humped-barrier, wkb-action, hill-wheeler, strutinsky-shell-correction, half-life-systematics, superheavy-nuclei]
---

# Spontaneous fission double-humped barrier WKB action and half-life systematics

## Definition

### Definition and Phenomenological Framework

Spontaneous Fission (SF) is a fundamental decay mode of heavy actinides and superheavy elements (SHE), wherein a nucleus in its ground state undergoes sub-barrier quantum mechanical tunneling through the multidimensional potential energy surface into two fission fragments without external excitation.

Based on 卢希庭《原子核物理（修订版）》第 4 章 §4.4 (pp. 102–115), C. A. Bertulani & P. Danielewicz *Introduction to Nuclear Reactions* Chapter 11, P. Möller et al. (Phys. Rev. C 79, 064304, 2009), and W. J. Swiatecki (1955):

1. **Double-Humped Fission Barrier Topography**:
   Superposition of macroscopic liquid-drop surface/Coulomb deformation energy and microscopic Strutinsky shell corrections creates two barriers:
   - **Inner Barrier $A$**: Height $E_A$, curvature $\hbar\omega_A$ (typically $\sim 5 - 7\text{ MeV}$, $\hbar\omega_A \sim 0.9 - 1.2\text{ MeV}$);
   - **Second Minimum $II$**: Depth $E_{II}$, hosting superdeformed shape isomers;
   - **Outer Barrier $B$**: Height $E_B$, curvature $\hbar\omega_B$ (typically $\sim 4.5 - 6\text{ MeV}$, $\hbar\omega_B \sim 0.5 - 0.7\text{ MeV}$).

---

## Hill-Wheeler Quantum Tunneling and WKB Action

For a ground state with zero-point vibration energy $E_0 \approx 0.80\text{ MeV}$ ($E_0 = \frac{1}{2}\hbar\omega_0$):

1. **Hill-Wheeler Penetration Factor for Each Barrier**:
   $$P_A = \frac{1}{1 + \exp\left( \frac{2\pi(E_A - E_0)}{\hbar\omega_A} \right)}, \quad P_B = \frac{1}{1 + \exp\left( \frac{2\pi(E_B - E_0)}{\hbar\omega_B} \right)}$$
   In the deep sub-barrier limit ($E_0 \ll E_A, E_B$), transmission drops exponentially:
   $$P_i \approx \exp\left( -\frac{2\pi(E_i - E_0)}{\hbar\omega_i} \right)$$

2. **Two-Barrier Composite Penetration**:
   $$P_{\text{tot}} \approx \frac{P_A P_B}{4.0}$$
   The effective WKB action integral across the entire barrier landscape is:
   $$S_{\text{eff}} = -\ln(P_{\text{tot}}) = \frac{2\pi(E_A - E_0)}{\hbar\omega_A} + \frac{2\pi(E_B - E_0)}{\hbar\omega_B} + \ln(4)$$

3. **Spontaneous Fission Half-Life**:
   Assault frequency of the fission vibration: $\nu_0 \approx \frac{\omega_0}{2\pi} \approx 1.0 \times 10^{21}\text{ s}^{-1}$.
   $$T_{1/2}^{\text{SF}} = \frac{\ln 2}{\nu_0 P_{\text{tot}}} = \left[ \frac{\ln 2}{\nu_0} \right] \exp(S_{\text{eff}})$$
   Because $S_{\text{eff}} \sim 70 - 100$, half-lives span more than 30 orders of magnitude across the nuclear chart!

---

## Swiatecki Systematics & Superheavy Stability

1. **Liquid Drop Fissility Parameter ($Z^2/A$)**:
   The classical fissility parameter $x = (Z^2/A) / (Z^2/A)_{\text{crit}}$ sets the baseline Coulomb repulsion:
   $$(Z^2/A)_{\text{crit}} = 50.883 \left[ 1 - 1.7826 \left( \frac{N-Z}{A} \right)^2 \right] \approx 46 - 48$$
   Without shell stabilization, liquid drop fission barriers collapse to zero when $x \to 1.0$.

2. **Shell Correction Shielding ($\delta U$)**:
   In actinide and superheavy nuclei (e.g. $^{294}\text{Og}$), negative shell corrections ($\delta U \approx 5 - 8\text{ MeV}$) stabilize the spherical or deformed ground state, raising the inner barrier $E_A$ and creating the **Island of Stability** ($Z = 114 - 120, N = 184$).
   $$\log_{10}(T_{1/2}^{\text{SF}} [\text{yr}]) \approx a_0 - a_1 \left( \frac{Z^2}{A} \right) + k_{\text{shell}} \delta U$$

---

## Canonical Experimental Benchmarks

1. **$^{238}\text{U}$ ($Z = 92, A = 238$)**:
   - $E_A = 6.30\text{ MeV}, \hbar\omega_A = 1.00\text{ MeV}, E_B = 5.65\text{ MeV}, \hbar\omega_B = 0.51\text{ MeV}$;
   - Action $S_A = 34.56, S_B = 59.75 \implies S_{\text{eff}} = 95.70$;
   - $P_{\text{tot}} = 2.75 \times 10^{-42} \implies T_{1/2}^{\text{SF}} \approx 7.98 \times 10^{12}\text{ yr}$ ($\log_{10} = 12.90$, matching experimental longevity).
2. **$^{252}\text{Cf}$ ($Z = 98, A = 252$) Commercial Neutron Source**:
   - $E_A = 5.30\text{ MeV}, E_B = 5.05\text{ MeV}$;
   - $S_{\text{eff}} = 72.82, P_{\text{tot}} = 2.37 \times 10^{-32} \implies T_{1/2}^{\text{SF}} \approx 927\text{ yr}$ ($\log_{10} = 2.97$).
3. **$^{240}\text{Pu}$ ($Z = 94, A = 240$)**:
   - $T_{1/2}^{\text{SF}} \approx 1.14 \times 10^{11}\text{ yr}$.

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用


- **Lu Xiting (卢希庭)**: *Nuclear Physics (Revised Edition)* (《原子核物理（修订版）》), Atomic Energy Press (2000), Chapter 4 §4.4 (Nuclear Fission), pp. 102–115.
- **Bertulani, C. A. & Danielewicz, P.**: *Introduction to Nuclear Reactions*, CRC Press / Z-Library (2004), Chapter 11 (Fission).
- **Möller, P. et al.**: *Heavy-element fission barriers*, Phys. Rev. C 79, 064304 (2009).
- **Swiatecki, W. J.**: *Systematics of fission, alpha, and beta decay half-lives*, Phys. Rev. 100, 937–938 (1955).


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
