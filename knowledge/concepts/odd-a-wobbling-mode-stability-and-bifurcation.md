---
type: concept
title: "Odd-A nuclei transverse vs. longitudinal wobbling modes, dynamic stability boundaries, and inertia-driven bifurcations"
aliases: [wobbling-stability, transverse-vs-longitudinal, wobbling-bifurcation, critical-wobbling-frequency, 135pr-controversy]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [triaxiality, wobbling, transverse-wobbling, longitudinal-wobbling, 135pr, 105pd, 187au, bifurcation, stability-boundary]
---

# Odd-A nuclei transverse vs. longitudinal wobbling modes, dynamic stability boundaries, and inertia-driven bifurcations

## Definition

### Physical Classification: Transverse (TW) vs. Longitudinal (LW) Wobbling

In triaxially deformed odd-$A$ nuclei, a high-$j$ valence quasiparticle (e.g. $\pi h_{11/2}$ in $^{135}\text{Pr}$, $\nu h_{11/2}$ in $^{105}\text{Pd}$, $\pi h_{9/2}$ in $^{187}\text{Au}$) couples to the triaxial rotor core ($\mathcal{J}_i > \mathcal{J}_s, \mathcal{J}_l$).
Two distinct geometrical modes arise:

1. **Transverse Wobbling (TW)**:
   - The quasiparticle angular momentum $\vec{j}$ aligns along the **nuclear short axis ($s$)**, which is perpendicular to the intermediate axis ($i$) of collective core rotation $\vec{R}$.
   - Small-amplitude harmonic wobbling frequency around the $i$-axis:
     $$\hbar\omega_w^{\text{TW}} = \sqrt{\left[ \omega_{\text{rot}}\left(1 - \frac{\mathcal{J}_i}{\mathcal{J}_s}\right) + \frac{j_{\text{eff}}}{\mathcal{J}_s} \right] \left[ \omega_{\text{rot}}\left(1 - \frac{\mathcal{J}_i}{\mathcal{J}_l}\right) + \frac{j_{\text{eff}}}{\mathcal{J}_l} \right]}$$
   - Since $\mathcal{J}_i > \mathcal{J}_s, \mathcal{J}_l$, both coefficient terms are negative.
   - **Hallmark Feature**: $\hbar\omega_w^{\text{TW}}$ **decreases with spin** $I$ ($d\hbar\omega_w / dI < 0$).

2. **Longitudinal Wobbling (LW)**:
   - The quasiparticle angular momentum $\vec{j}$ aligns along the **intermediate axis ($i$)**, parallel to the collective core rotation axis.
   - **Hallmark Feature**: $\hbar\omega_w^{\text{LW}}$ **increases with spin** $I$ ($d\hbar\omega_w / dI > 0$).

---

## Critical Instability Boundary & The Role of Nuclear Inertia

A fundamental physical issue analyzed in *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025) Ch. 2 (Frauendorf) and Ch. 5 (Guo & Lv) is that harmonic transverse wobbling cannot persist indefinitely.
As rotational frequency increases, the core angular momentum reaches the critical value:
$$R_{\text{crit}} = \frac{j_{\text{eff}}}{1 - \mathcal{J}_l / \mathcal{J}_i}$$
Above $R_{\text{crit}}$, $\omega_w^2 < 0$, causing planar rotation to destabilize via a pitchfork bifurcation into **Tilted Precession (TiP)** or chiral rotation!

### Hydrodynamic vs. Rigid Inertia Paradigms:
1. **Hydrodynamic (Irrotational) Inertia**:
   - $\mathcal{J}_l / \mathcal{J}_i \approx 0.25 - 0.30 \implies R_{\text{crit}} \approx 7.5\hbar$ ($I_{\text{crit}} \approx 9.5 - 10.3\hbar$).
   - The harmonic TW mode terminates at low spin, explaining why pure hydrodynamic models predict immediate instability for $^{135}\text{Pr}$ ($I \ge 10.5\hbar$).
2. **Rigid-Body / Pairing-Quenched (CAP) Inertia**:
   - Coriolis Anti-Pairing suppresses pairing gaps at high spin, driving moments of inertia towards rigid values with $\mathcal{J}_l / \mathcal{J}_i \approx 0.65 - 0.75$.
   - $R_{\text{crit}}$ expands to $15 - 22\hbar$ ($I_{\text{crit}} \approx 16 - 24\hbar$), enabling stable transverse wobbling across the full experimentally observed band.

---

## Executable Analysis Tool: `wobstab`

The Python analysis suite integrates `odd_a_transverse_longitudinal_wobbling_stability_solver.py`, accessible via CLI:

```bash
# 1. 135Pr prototype TW with rigid/pairing-quenched inertia (confirmed dOmega/dI < 0)
python3 system/scripts/analysis/nuclear_analyzer.py wobstab --preset 135Pr_transverse_rigid_stable

# 2. 135Pr with hydrodynamic inertia (exhibits premature instability at I = 10.5h)
python3 system/scripts/analysis/nuclear_analyzer.py wobstab --preset 135Pr_transverse_hydro_unstable

# 3. 187Au longitudinal wobbling benchmark (confirmed dOmega/dI > 0)
python3 system/scripts/analysis/nuclear_analyzer.py wobstab --preset 187Au_longitudinal_wobbling
```

---

## Literature and Textbook Provenance

- **Chirality and Wobbling in Atomic Nuclei** (CRC Press 2025), Chapter 2 (S. Frauendorf), Chapter 5 (X. G. Guo & C. B. Lv), Chapter 6 (E. A. Lawrie).
- **Frauendorf & Dönau**, Phys. Rev. C 89, 014322 (2014): *Transverse wobbling in odd-A nuclei*.
- **Tanabe & Sugawara-Tanabe**, Phys. Rev. C 95, 064315 (2017).
- **Sensharma et al.**, Phys. Rev. Lett. 124, 052501 (2020): *Longitudinal wobbling in 187Au*.


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

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
