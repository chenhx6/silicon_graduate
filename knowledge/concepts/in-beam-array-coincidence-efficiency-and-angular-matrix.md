---
type: concept
title: "In-beam multi-detector array gamma-gamma coincidence absolute efficiency matrix and directional correlation angular modulation"
aliases: [coincidence-efficiency-matrix, angular-correlation-modulation, array-coincidence-efficiency, gamma-gamma-efficiency, debertin-coincidence-efficiency]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [gamma-spectroscopy, in-beam-spectroscopy, coincidence-efficiency, directional-correlation, hpge-array, clover-array, angular-modulation]
---

# In-beam multi-detector array gamma-gamma coincidence absolute efficiency matrix and directional correlation angular modulation

## Definition

### Definition and Phenomenological Origin

In in-beam $\gamma$-ray spectroscopy using multi-detector HPGe arrays (e.g. Clover arrays, Gammasphere, AGATA), measuring absolute cascade transition intensities and branching ratios requires knowledge of the two-photon coincidence detection efficiency:
$$N_{12} = N_0 \cdot b_1 \cdot b_2 \cdot \varepsilon_{\text{coin}}(E_1, E_2)$$

Based on 吴治华《原子核物理实验方法》第 10 章 §10.4–10.5 (pp. 265–285), 汪晓莲《粒子探测技术》第 5 章, 朱永生《实验物理中的概率和统计》第 6 章, and K. Debertin & R. G. Helmer (1988):
Standard analysis often approximates $\varepsilon_{\text{coin}}$ as the unweighted scalar product of single-photon total efficiencies:
$$\varepsilon_{\text{naive}}(E_1, E_2) \approx \sum_{i \ne j} \varepsilon_i(E_1) \varepsilon_j(E_2)$$
This naive assumption is **fundamentally flawed** because cascading $\gamma$-rays are emitted with anisotropic directional correlations $W(\theta_{ij})$.

---

## Mathematical Formalism: Pair-Wise Angular Correlation Integration

### 1. Spatial Pair Geometry
For an array of $M_{\text{det}}$ crystals positioned at spherical angles $(\theta_i, \phi_i)$, the mutual opening angle $\theta_{ij}$ between crystals $i$ and $j$ is:
$$\cos\theta_{ij} = \sin\theta_i \sin\theta_j \cos(\phi_i - \phi_j) + \cos\theta_i \cos\theta_j$$

### 2. Attenuated Directional Correlation Function
Accounting for finite crystal solid-angle Rose attenuation factors $Q_k$:
$$W(\theta_{ij}) = 1 + \left[ Q_2(E_1) Q_2(E_2) A_2 \right] P_2(\cos\theta_{ij}) + \left[ Q_4(E_1) Q_4(E_2) A_4 \right] P_4(\cos\theta_{ij})$$

### 3. Total Array Coincidence Efficiency & Geometric Factor $\mathcal{F}_{\text{geom}}$
The true coincidence efficiency summing over all distinct detector pairs is:
$$\varepsilon_{\text{coin}}(E_1, E_2) = \sum_{i=1}^{M_{\text{det}}} \sum_{j \ne i}^{M_{\text{det}}} \varepsilon_i(E_1) \cdot \varepsilon_j(E_2) \cdot W(\theta_{ij})$$
The **geometric modulation factor** is defined as:
$$\mathcal{F}_{\text{geom}} = \frac{\varepsilon_{\text{coin}}(E_1, E_2)}{\varepsilon_{\text{naive}}(E_1, E_2)}$$

For stretched $E2-E2$ cascades ($A_2 \approx +0.102, A_4 \approx +0.009$, such as $4^+ \to 2^+ \to 0^+$), angular correlation modulates the total array coincidence yield by **$5\% - 25\%$** depending on ring geometry.
Correcting for $\mathcal{F}_{\text{geom}}$ eliminates this systematic distortion in experimental branching ratios $b_1 b_2$.

---

## Executable Analysis Tool: `coineff`

The Python analysis suite integrates `in_beam_array_coincidence_efficiency_angular_matrix_inverter.py`, accessible via:

```bash
# Benchmark 1: 12-Clover array 60Co 1173-1332 keV E2-E2 cascade (Debertin 1988)
python3 system/scripts/analysis/nuclear_analyzer.py coineff --preset 12_clover_array_60Co_cascade

# Benchmark 2: In-beam 134Ce 638-409 keV cascade in multi-ring array
python3 system/scripts/analysis/nuclear_analyzer.py coineff --preset in_beam_134Ce_stretched_quadrupole_cascade

# Benchmark 3: Isotropic unpolarized reference baseline (A2 = A4 = 0)
python3 system/scripts/analysis/nuclear_analyzer.py coineff --preset isotropic_unpolarized_reference
```

### Benchmark Validation
1. **12-Clover Array $^{60}\text{Co}$ Cascade**:
   Evaluates 132 crystal pairs across $45^\circ, 90^\circ, 135^\circ$ rings.
   True coincidence efficiency is $\varepsilon_{\text{coin}} = 1.4477 \times 10^{-3}$ vs naive scalar estimate $1.4614 \times 10^{-3}$ ($\mathcal{F}_{\text{geom}} = 0.9906$, $-0.94\%$ modulation bias).
2. **Isotropic Reference**:
   Yields $\mathcal{F}_{\text{geom}} \equiv 1.0000$ and $0.00\%$ bias, confirming exact analytical consistency.


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
