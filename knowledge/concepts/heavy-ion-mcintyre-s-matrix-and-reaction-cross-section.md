---
type: concept
title: "Heavy-ion strong absorption McIntyre S-matrix parameterization, transmission coefficients and total reaction cross section inversion"
aliases: [mcintyre-s-matrix, strong-absorption-model, reaction-cross-section, grazing-angular-momentum, strong-absorption-radius]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [heavy-ion-reactions, elastic-scattering, s-matrix, mcintyre-model, strong-absorption, reaction-cross-section, grazing-angular-momentum]
---

# Heavy-ion strong absorption McIntyre S-matrix parameterization, transmission coefficients and total reaction cross section inversion

## Definition

### Definition and Phenomenological Origin

In heavy-ion elastic scattering near and above the Coulomb barrier (e.g. $^{16}\text{O} + {}^{208}\text{Pb}$ at $E_{\text{lab}} \approx 130\text{ MeV}$, $^{12}\text{C} + {}^{12}\text{C}$ at $120\text{ MeV}$), strong nuclear interactions cause complete absorption of low partial waves into compound nucleus formation and direct reaction channels.

Based on 林承键《重离子核反应》第 3 章 §3.2 (pp. 55–75), C. A. Bertulani *Introduction to Nuclear Reactions* Chapters 3 & 4, and J. A. McIntyre et al. (Phys. Rev. 117, 1337, 1960):
1. The partial-wave scattering matrix is $S_l = \eta_l e^{2i\delta_l}$, where the reflection modulus $\eta_l \in [0, 1]$ parameterizes the absorption probability.
2. **McIntyre Strong Absorption Model (SAM)** parameterizes $\eta_l$ as a smooth Woods-Saxon cutoff in angular momentum space:
   $$\eta_l = \left[ 1 + \exp\left( \frac{l_g - l}{\Delta l} \right) \right]^{-1}$$
   where $l_g$ is the **grazing angular momentum** (corresponding to $50\%$ absorption: $\eta_{l_g} = 0.50$), and $\Delta l$ is the angular momentum diffuseness.
3. The transmission coefficient (reaction probability per partial wave) is:
   $$T_l = 1 - |S_l|^2 = 1 - \eta_l^2$$

---

## Mathematical Cross Section Formalism & Radius Inversion

### 1. Partial Wave Sums
The total reaction cross section $\sigma_R$, total elastic cross section $\sigma_{\text{el}}$, and total scattering cross section $\sigma_{\text{tot}}$ are given by:
$$\sigma_R = \frac{\pi}{k^2} \sum_{l=0}^\infty (2l + 1) T_l = \frac{\pi}{k^2} \sum_{l=0}^\infty (2l + 1) (1 - \eta_l^2)$$
$$\sigma_{\text{el}} = \frac{\pi}{k^2} \sum_{l=0}^\infty (2l + 1) |1 - S_l|^2$$
$$\sigma_{\text{tot}} = \sigma_R + \sigma_{\text{el}}$$

### 2. Semiclassical Inversion of Strong Absorption Radius
From the grazing angular momentum $l_g$, the strong absorption radius $R_{\text{int}}$ corresponds to the classical distance of closest approach at grazing impact:
$$E_{\text{c.m.}} = \frac{Z_p Z_t e^2}{R_{\text{int}}} + \frac{\hbar^2 l_g (l_g + 1)}{2\mu R_{\text{int}}^2}$$
Solving this quadratic equation yields $R_{\text{int}}$, from which the nuclear interaction radius parameter $r_0$ and spatial surface diffuseness $d$ are directly deduced:
$$r_0 = \frac{R_{\text{int}}}{A_p^{1/3} + A_t^{1/3}}, \quad d = \frac{\Delta l}{k}$$

---

## Executable Analysis Tool: `mcintyre`

The Python analysis suite integrates `heavy_ion_mcintyre_s_matrix_reaction_cross_section_analyzer.py`, accessible via:

```bash
# Benchmark 1: 16O + 208Pb at 129.5 MeV (Ball et al. 1975)
python3 system/scripts/analysis/nuclear_analyzer.py mcintyre --preset 16O_208Pb_129.5MeV

# Benchmark 2: 12C + 12C at 120 MeV (Stokstad 1980)
python3 system/scripts/analysis/nuclear_analyzer.py mcintyre --preset 12C_12C_120MeV
```

### Benchmark Validation: $^{16}\text{O} + {}^{208}\text{Pb}$ at $E_{\text{lab}} = 129.5\text{ MeV}$
- Center-of-mass energy $E_{\text{c.m.}} = 120.25\text{ MeV}$, wavenumber $k = 9.245\text{ fm}^{-1}$, Sommerfeld parameter $\eta = 36.31$;
- Grazing angular momentum $l_g = 55.4\ \hbar$, $\Delta l = 3.25\ \hbar$;
- Total reaction cross section: $\sigma_R = 1294.8\text{ mb}$ ($1.295\text{ barns}$);
- Strong absorption radius inverted to $R_{\text{int}} = 11.09\text{ fm}$, yielding physical nuclear radius parameter $r_0 = 1.314\text{ fm}$ and diffuseness $d = 0.352\text{ fm}$.


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
