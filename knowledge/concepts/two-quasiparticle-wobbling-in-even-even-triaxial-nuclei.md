---
type: concept
title: "Two-quasiparticle wobbling excitations in even-even triaxial nuclei and transverse frequency evolution"
aliases: [two-quasiparticle-wobbling, even-even-wobbler, 130ba-wobbler, transverse-wobbling-even-even, quasiparticle-rotor-coupling]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [triaxiality, wobbling-motion, even-even-nuclei, two-quasiparticle-alignment, transverse-wobbling, 130ba, b-e2-branching]
---

# Two-quasiparticle wobbling excitations in even-even triaxial nuclei and transverse frequency evolution

## Definition

### Definition and Phenomenological Origin

Wobbling motion is a unique fingerprint of stable triaxial deformation ($\gamma \ne 0^\circ, 60^\circ$). Historically predicted by A. Bohr and B. R. Mottelson for simple asymmetric rotors and first observed in odd-$A$ Lu isotopes ($^{161,163,165,167}\text{Lu}$) in the 2000s, wobbling was long believed to be absent in low-lying even-even nuclei due to the lack of high-$j$ single-particle alignment and early band crossings.

In 2019–2020, a major theoretical and experimental breakthrough occurred:
1. **Q. B. Chen & S. Frauendorf (Phys. Rev. Lett. 123, 232502, 2019)** demonstrated theoretically that when an even-even triaxial nucleus rotates beyond the first backbending crossing, two high-$j$ nucleons align their angular momenta along the short (s) axis of the triaxial core ($\vec{j}_{12} = \vec{j}_1 + \vec{j}_2$).
2. **S. Y. Wang, F. Q. Chen, C. Liu et al. (Phys. Lett. B 808, 135634, 2020)** reported the first experimental observation of two-quasiparticle wobbling in $^{130}\text{Ba}$ based on in-beam $\gamma$-ray spectroscopy using the AFRODITE array.
3. Extensively discussed in *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025) Chapter 10 (PDF pp. 215–230) and Chapter 11 (PDF pp. 235–255).

---

## Theoretical Framework: Quasiparticle-Triaxial-Rotor Coupling

### 1. Vector Coupling Geometry
The total angular momentum $\vec{I}$ is composed of the collective rotation of the triaxial core $\vec{R}$ and the aligned two-quasiparticle spin $\vec{j}_{12}$:
$$\vec{I} = \vec{R} + \vec{j}_{12}$$
For two $h_{11/2}$ protons in the $A \sim 130$ region, maximum alignment yields $j_{12} \approx 10\ \hbar$ directed along the short ($s$) axis ($\gamma \sim -20^\circ \text{ to } -30^\circ$).

The core has intermediate-axis dominance ($\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$), rotating preferentially about the $m$-axis.

### 2. Transverse Wobbling Frequency Trend
In the harmonic approximation, the wobbling excitation energy is:
$$E_{\text{wob}}(I) = E(n_w=1, I) - \frac{1}{2}\left[ E(n_w=0, I+1) + E(n_w=0, I-1) \right] \approx \hbar\omega_w(I)$$
Because the quasiparticle angular momentum $\vec{j}_{12}$ is perpendicular to the collective rotation axis ($m$), this constitutes **Transverse Wobbling (TW)**.
The wobbling frequency decreases with increasing spin $I$:
$$\frac{d(\hbar\omega_w)}{dI} < 0$$
This negative slope can support a transverse-alignment interpretation within a
specified model and spin window, but it is not by itself a definitive hallmark.
Longitudinal wobbling, configuration mixing, band crossing and response
assumptions must remain in the comparison.

### 3. Interband $E2/M1$ Transitions
The transition connecting the $n_w = 1$ band to the $n_w = 0$ yrast band proceeds via $\Delta I = 1$ transitions with prominent $E2$ nature:
$$\frac{B(E2, n_w=1, I \to n_w=0, I-1)}{B(E2, n_w=1, I \to n_w=1, I-2)} \approx \frac{2}{I} \left[ \frac{\sin(|\gamma| + 30^\circ)}{\sin(|\gamma| - 60^\circ)} \right]^2$$
The ratio is typically $0.3 - 0.6$, several orders of magnitude higher than single-particle transitions ($\sim 10^{-3}$), and the mixing ratio $\delta(E2/M1)$ is large ($|\delta| \ge 1.5 - 3.0$), verifying collective electric quadrupole radiation.

---

## Executable Analysis Tool: `twoqpwob`

The Python analysis suite integrates `two_quasiparticle_even_even_wobbling_analyzer.py`, accessible via:

```bash
# Benchmark 1: 130Ba experimental landmark (Wang et al. PLB 2020)
python3 system/scripts/analysis/nuclear_analyzer.py twoqpwob --preset 130Ba_two_quasiparticle_wobbler

# Benchmark 2: 136Nd predicted 2-qp transverse wobbler (Chen & Frauendorf PRL 2019)
python3 system/scripts/analysis/nuclear_analyzer.py twoqpwob --preset 136Nd_two_quasiparticle_wobbler

# Counterexample: Spurious single-particle band with rising frequency and low B(E2)
python3 system/scripts/analysis/nuclear_analyzer.py twoqpwob --preset spurious_quasiparticle_counterexample
```

### Conditional screening examples
1. **$^{130}\text{Ba}$ ($I = 11 \dots 17$)**:
   $E_{\text{wob}}$ decreases monotonically from $505\text{ keV}$ to $325\text{ keV}$ (slope $-30.25\text{ keV}/\hbar$).
   Experimental $B(E2)_{\text{out}}/B(E2)_{\text{in}}$ averages $0.385$, in excellent agreement with theoretical expectation ($0.299$).
   The preset passes a heuristic transverse-wobbling screening score. It is a
   derived fixture and does not establish experimental wobbling.
2. **Spurious Counterexample**:
   Displays rising frequency ($+125\text{ keV}/\hbar$) and negligible $B(E2)$ ratio ($0.023$), correctly triggering `REJECTED_SPURIOUS_OR_SINGLE_PARTICLE_BAND`.


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本页整理模型和观测量的条件性 screening logic。预设输出属于 derived
fixture；它不能替代带有 source locator、响应、寿命、协方差和竞争模型的
实验级模式判定。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
