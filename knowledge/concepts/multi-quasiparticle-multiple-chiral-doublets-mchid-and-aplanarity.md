---
type: concept
title: "Multi-quasiparticle multiple chiral doublets (MchiD) and aplanar angular momentum geometry"
aliases: [multi-quasiparticle-mchid, nuclear-chirality-mchid, 4qp-chiral-geometry, aplanar-rotation-even-even]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [chirality, multiple-chiral-doublets, mchid, four-quasiparticle, aplanarity, triaxiality, time-reversal-breaking, spontaneous-symmetry-breaking]
---

# Multi-quasiparticle multiple chiral doublets (MchiD) and aplanar angular momentum geometry

## Definition

### Definition and Physical Mechanisms

Chiral doublet bands in atomic nuclei were initially discovered in odd-odd nuclei (e.g. $^{134}\text{Pr}$) characterized by a simple two-quasiparticle configuration: one high-$j$ valence proton particle ($\pi h_{11/2}$) and one high-$j$ valence neutron hole ($\nu h_{11/2}^{-1}$) coupled to a triaxial collective core (Frauendorf & Meng 1997).

Over the last decade, covariant density functional theory (CDFT) and high-statistics in-beam $\gamma$-spectroscopy (Meng & Wang 2025; Xiong & Wang ADNDT 2019; Petrache et al. 2018) discovered that nuclear chirality extends to **multi-quasiparticle configurations in even-even and odd-mass nuclei**, leading to the phenomenon of **Multiple Chiral Doublet Bands (M$\chi$D)**:

1. **Four-Quasiparticle (4-qp) Chiral Geometry in Even-Even Nuclei**:
   In even-even triaxial nuclei (e.g. $^{136}\text{Nd}$), chirality is formed by a 4-quasiparticle configuration:
   $$\pi (h_{11/2})^2 \otimes \nu (h_{11/2})^{-2}$$
   - Two valence protons align along the short ($s$) axis: $\vec{j}_\pi = (j_{\pi, s}, 0, 0)$ with $j_\pi \approx 8 \sim 10\ \hbar$;
   - Two valence neutron holes align along the long ($l$) axis: $\vec{j}_\nu = (0, 0, j_{\nu, l})$ with $j_\nu \approx 8 \sim 10\ \hbar$;
   - The triaxial collective core rotates along the intermediate ($m$) axis: $\vec{R} = (0, R_m, 0)$.

2. **Aplanarity and the Chiral Invariant $\chi$**:
   The three orthogonal vectors span a non-coplanar (aplanar) frame characterized by the scalar triple product:
   $$\chi = \vec{j}_\pi \cdot (\vec{j}_\nu \times \vec{R}) = j_{\pi, s} j_{\nu, l} R_m$$
   Normalized aplanarity volume metric:
   $$\mathcal{V}_{\text{chiral}} = \frac{|\chi|}{|\vec{j}_\pi| |\vec{j}_\nu| |\vec{R}|} \in [0.0, 1.0]$$
   Under chiral symmetry transformation $\mathcal{T}\mathcal{R}_y(\pi)$ (time reversal $\mathcal{T}$ followed by a $180^\circ$ rotation $\mathcal{R}_y(\pi)$ about the $y$-axis):
   $$\vec{j}_\pi \to -\vec{j}_\pi, \quad \vec{j}_\nu \to -\vec{j}_\nu, \quad \vec{R} \to -\vec{R} \implies \chi \to -\chi$$
   Spontaneous breaking of this symmetry in the intrinsic frame produces two degenerate, orthogonal left- and right-handed states in the laboratory frame: **chiral doublet bands**.

---

## Multiple Chiral Doublets (M$\chi$D) Classification

In a single atomic nucleus, multiple pairs of chiral doublet bands (M$\chi$D) can coexist via two distinct physical pathways:

1. **Configuration-Driven M$\chi$D**:
   - **Doublet 1 (Bands 1 & 2)**: based on the lowest 4-qp state $\pi h_{11/2}^2 \otimes \nu h_{11/2}^{-2}$ (positive parity, e.g. $I = 14^+ \dots 20^+$ in $^{136}\text{Nd}$);
   - **Doublet 2 (Bands 3 & 4)**: based on an excited 4-qp configuration involving different single-particle orbitals, e.g. $\pi h_{11/2}^2 \otimes \nu [h_{11/2}^{-1} (d_{5/2}/g_{7/2})^{-1}]$ (negative parity).

2. **Shape-Coexistence-Driven M$\chi$D**:
   - Doublets sharing the same multi-quasiparticle configuration but occupying distinct local triaxial potential energy minima with different triaxiality angles (e.g. $\gamma_1 \approx -25^\circ$ vs $\gamma_2 \approx -45^\circ$).

---

## Quantitative Experimental Fingerprints

An experimental candidate pair of bands is verified as a chiral doublet if it satisfies five strict experimental criteria:

1. **Energy Degeneracy**:
   $$\Delta E(I) = |E_{\text{band1}}(I) - E_{\text{band2}}(I)| \le 100\text{ keV}$$
   across $\ge 3$ consecutive spin states.
2. **Absence of Signature Splitting (Smooth $S(I)$)**:
   The staggering parameter:
   $$S(I) = \frac{E(I) - E(I-1)}{2I}$$
   must be smooth, monotonic, and nearly identical between partner bands ($\overline{|\Delta S|} \le 1.0\text{ keV}$), in contrast to planar rotation which exhibits pronounced zigzag staggering.
3. **Equal Moment of Inertia**:
   The alignment $i_x(I)$ and dynamic moment of inertia $\mathcal{J}^{(2)}(I)$ are essentially identical for both bands.
4. **Electromagnetic Transition Parity**:
   The $B(M1)/B(E2)$ ratios exhibit identical odd-even spin staggering in both partner bands.
5. **Chiral Selection Rules**:
   Interband $E2$ transitions ($I_2 \to I_1 - 1$) are strongly hindered ($B(E2) \approx 0$), while interband $M1$ transitions ($I_2 \to I_1$) are allowed.

---

## Canonical Experimental Benchmarks

- **$^{136}\text{Nd}$ (Petrache et al. 2018 / ADNDT 2019)**:
  A published candidate/analysis case for 4-quasiparticle M$\chi$D in an
  even-even nucleus; the label remains dependent on the source's band identity,
  lifetimes, transition strengths and competing configurations.
  - Doublet 1 ($\pi h_{11/2}^2 \otimes \nu h_{11/2}^{-2}$): $\overline{\Delta E} = 47.5\text{ keV}$, $\overline{|\Delta S|} = 0.32\text{ keV}$, $\mathcal{V}_{\text{chiral}} = 0.778$, confidence $= 87.3\%$.
  - Doublet 2 ($\pi h_{11/2}^2 \otimes \nu [h_{11/2}^{-1} d_{5/2}^{-1}]$): $\overline{\Delta E} = 50.8\text{ keV}$, $\overline{|\Delta S|} = 0.38\text{ keV}$, $\mathcal{V}_{\text{chiral}} = 0.842$, confidence $= 86.3\%$.
  - Both doublets coexist simultaneously, confirming M$\chi$D.
- **$^{133}\text{Ce}$ (Ayangeakaa et al. 2013)**:
  First demonstration of M$\chi$D in an odd-$A$ nucleus (3-qp and 5-qp configurations).
- **$^{103}\text{Rh}$ (Kuti et al. 2014)**:
  Observation of multiple chiral doublets in the $A \sim 100$ mass region.

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用


- **Meng, J. & Wang, Y. P.**: *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025), Chapter 3 (Chiral Geometry and Multiple Chiral Doublets), PDF pp. 81–93.
- **Chen, Q. B. et al.**: *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025), Chapter 10 (CDFT+PRM for MchiD), PDF pp. 222–238.
- **Xiong, X. H. & Wang, S. Y. et al.**: *Nuclear chiral doublet bands: Data tables*, Atomic Data and Nuclear Data Tables 125, 193–225 (2019).
- **Petrache, C. M. et al.**: Phys. Rev. C 97, 041304(R) (2018) (Multiple chiral doublet bands in $^{136}\text{Nd}$).
- **Frauendorf, S. & Meng, J.**: Nucl. Phys. A 617, 131 (1997) (Tilted rotation of triaxial nuclei - origin of nuclear chirality).


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
