---
type: concept
title: "Microscopic octupole collective modes, IS-EWSR sum rules and alternating-parity bands"
aliases: [octupole-collective-modes, octupole-ewsr-sum-rule, pear-shaped-nuclei-d0, alternating-parity-bands, parity-splitting-dynamics]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [octupole-deformation, pear-shaped, ewsr, sum-rule, parity-doublets, intrinsic-dipole, alaga-ratio, reflection-asymmetry]
---

# Microscopic octupole collective modes, IS-EWSR sum rules and alternating-parity bands

## Definition

### Definition and Symmetry-Breaking Framework

While quadrupole deformation ($\lambda = 2$) preserves spatial inversion parity ($\mathcal{P}$ symmetry), **octupole deformation ($\lambda = 3$) breaks reflection symmetry**, creating reflection-asymmetric, pear-shaped nuclear ground states and low-lying negative-parity collective states ($J^\pi = 3^-$ in spherical nuclei, alternating parity sequences $0^+, 1^-, 2^+, 3^-, \dots$ in deformed nuclei).

Based on 卢希庭《原子核物理（修订版）》第 8 章 §8.3, Bohr & Mottelson Vol. II §6-3 (pp. 340–360), and Butler & Nazarewicz (Rev. Mod. Phys. 68, 349, 1996):

1. **Octupole Single-Particle Weisskopf Unit**:
   $$B_{\text{W.u.}}(E3) = \frac{1}{16\pi} R_0^6 e^2 \approx 0.05944 A^2\ e^2\cdot\text{fm}^6 \quad (R_0 = 1.20 A^{1/3}\text{ fm})$$

2. **Isoscalar Octupole Energy-Weighted Sum Rule (IS-EWSR)**:
   According to Bohr & Mottelson Vol. II Eq. (6-82):
   $$S_{\text{IS}}(E3) = \sum_n (E_n - E_0) B(E3; 0^+ \to 3_n^-) = \frac{147}{4\pi} \frac{\hbar^2}{2m_N} \left( \frac{Z^2}{A} \right) R_0^4$$
   In spherical magic nuclei (e.g. $^{208}\text{Pb}$), the first excited collective state $3_1^-$ at $2.6145\text{ MeV}$ has an enhanced transition rate $B(E3; 3^- \to 0^+) = 34\ \text{W.u.}$, exhausting nearly $8\%$ of the total nuclear octupole sum rule on its own!

---

## Macroscopic-Microscopic Pear-Shape Observables

### 1. Intrinsic Electric Dipole Moment ($D_0$)
When a nucleus simultaneously possesses quadrupole ($\beta_2$) and octupole ($\beta_3$) deformations, the nuclear charge center does not coincide with the center of mass. This produces an intrinsic electric dipole moment:
$$D_0^{\text{LD}} \approx 0.000687\ A Z e \left( \frac{N - Z}{A} \right) \beta_2 \beta_3$$
In actual nuclei (e.g. $^{224}\text{Ra}$), shell corrections can alter this value, but $D_0 \sim 0.05 - 0.25\ e\cdot\text{fm}$ remains the primary signature of reflection asymmetry.

### 2. Alternating-Parity Bands and Branching Ratios
In pear-shaped nuclei, the rotational band consists of interleaved positive and negative parity states:
$$K^\pi = 0^\pm: \quad 0^+, 1^-, 2^+, 3^-, 4^+, 5^-, 6^+, \dots$$
Enhanced $E1$ transitions connect the bands. From experimental peak intensities $I_\gamma(E1)/I_\gamma(E2)$:
$$\left[ \frac{B(E1; I \to I-1)}{B(E2; I \to I-2)} \right]_{\text{exp}} = 1.30 \times 10^{-6} \frac{E_\gamma^5(E2)}{E_\gamma^3(E1)} \frac{I_\gamma(E1)}{I_\gamma(E2)}\ [\text{fm}^{-2}]$$
Using the exact Alaga Clebsch-Gordan identity:
$$\frac{\langle I 0 1 0 \mid I-1 0 \rangle^2}{\langle I 0 2 0 \mid I-2 0 \rangle^2} = \frac{2(2I-1)}{3(I-1)} \implies \frac{B(E1)}{B(E2)} = \frac{16(2I-1)}{15(I-1)} \left( \frac{D_0}{Q_0} \right)^2$$
Directly inverting this equation extracts $|D_0|$ ($e\cdot\text{fm}$) and the pear-shape deformation $\beta_3$.

### 3. Parity Displacement Parameter $\delta E(I)$
$$\delta E(I) = E(I^-) - \frac{E((I+1)^+) + E((I-1)^+)}{2}$$
- **Static Pear-Shaped Rotor (e.g. $^{224}\text{Ra}$)**: $\delta E(I) \approx 0$ from low to high spins, signaling a deep reflection-asymmetric potential well;
- **Centrifugally Stabilized Octupole (e.g. $^{144}\text{Ba}$)**: $\delta E(I) \gg 0$ at low spin ($I=1^-$), smoothly collapsing to 0 at higher spins ($I \ge 7^-$);
- **Harmonic Octupole Vibration (e.g. $^{208}\text{Pb}$)**: $\delta E(I)$ remains large and approximately constant.

---

## Canonical Experimental Benchmarks

1. **$^{224}\text{Ra}$ (Gaffney et al. Nature 497, 199, 2013)**:
   - Alternating parity band: $E(1^-) = 216\text{ keV}$, $E(3^-) = 290\text{ keV}$, $B(E3) = 38\ \text{W.u.}$;
   - Parity displacement collapses from $173.8\text{ keV}$ ($I=1^-$) to $0.0\text{ keV}$ ($I=9^-$);
   - Direct Coulomb excitation reported values compatible with $|D_0| \approx 0.10\ e\cdot\text{fm}$ and the model-dependent estimate $\beta_3 \approx 0.11$; the conversion does not by itself establish a rigid pear-shaped minimum.
2. **$^{144}\text{Ba}$ (Bucher et al. PRL 116, 112503, 2016)**:
   - Fission product benchmark with strong octupole collectivity: $B(E3; 3^- \to 0^+) = 48\ \text{W.u.}$;
   - Demonstrates octupole collectivity in the neutron-rich $A \sim 140$ mass region.
3. **$^{208}\text{Pb}$ Spherical Harmonic Benchmark**:
   - $E(3_1^-) = 2614.5\text{ keV}$, $B(E3) = 34.0\ \text{W.u.}$, exhausting $7.98\%$ of the IS-EWSR limit.

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用


- **Lu Xiting (卢希庭)**: *Nuclear Physics (Revised Edition)* (《原子核物理（修订版）》), Atomic Energy Press (2000), Chapter 8 §8.3 (Octupole Vibrations).
- **Bohr, A. & Mottelson, B. R.**: *Nuclear Structure*, Vol. II, Chapter 6 §6-3 (Octupole Deformations and Vibrations, Eq. 6-82), pp. 340–360.
- **Butler, P. A. & Nazarewicz, W.**: *Intrinsic reflection asymmetry in atomic nuclei*, Rev. Mod. Phys. 68, 349–421 (1996).
- **Gaffney, L. P. et al.**: *Studies of pear-shaped nuclei using accelerated radioactive beams*, Nature 497, 199–204 (2013).


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
