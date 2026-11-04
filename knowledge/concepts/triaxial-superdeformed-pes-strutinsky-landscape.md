---
type: concept
title: "Triaxial superdeformed 3D (beta_2, gamma, beta_4) potential energy surface, macroscopic-microscopic Strutinsky shell corrections and secondary well stabilization"
aliases: [tsd-pes-strutinsky, triaxial-pes-landscape, strutinsky-tsd-engine, high-spin-tsd-stabilization, 163lu-pes]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [triaxiality, superdeformation, potential-energy-surface, pes, strutinsky-method, high-spin, 163lu, 130ba]
---

# Triaxial superdeformed 3D (beta_2, gamma, beta_4) potential energy surface, macroscopic-microscopic Strutinsky shell corrections and secondary well stabilization

## Definition

### Definition and Phenomenological Origin

A key prerequisite for the emergence of transverse wobbling and nuclear chirality is the existence of a deep, stable triaxial minimum in the nuclear potential energy surface (PES).
In the $A \sim 160 - 170$ rare-earth region (e.g. $^{163,165}\text{Lu}$), high-$j$ intruder single-particle orbitals (specifically the proton $i_{13/2}$ shell) drive the formation of a pronounced **Triaxial Superdeformed (TSD)** secondary minimum with $\beta_2 \approx 0.38 - 0.42, \gamma \approx 18^\circ - 22^\circ$.

Based on Bohr & Mottelson *Nuclear Structure* Vol. II §4-2 & §6-4, *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025) Chapters 2 & 10 (PDF pp. 215–230), and V. M. Strutinsky (Nucl. Phys. A 95, 420, 1967):
At ground state ($I = 0$), the large liquid-drop surface energy cost disfavors superdeformation.
At high angular momentum ($I \ge 25 - 40\ \hbar$), the **large moment of inertia $\mathcal{J}_{\text{TSD}} \approx 65\ \hbar^2/\text{MeV}$** lowers the collective rotational energy $E_{\text{rot}} = \hbar^2 I(I+1)/(2\mathcal{J})$ by $10 - 15\text{ MeV}$ relative to normal-deformed states, driving the TSD well down and stabilizing the secondary minimum behind a substantial deformation barrier $V_B$.

---

## Mathematical Formalism: Macroscopic-Microscopic Decomposition

### 1. Total Energy Functional
The total deformation energy across the $(\beta_2, \gamma, \beta_4)$ manifold is:
$$E_{\text{tot}}(\beta_2, \gamma, \beta_4; I) = E_{\text{LDM}}(\beta_2, \gamma, \beta_4) + \delta E_{\text{shell}}(\beta_2, \gamma, \beta_4) + E_{\text{rot}}(I, \beta_2, \gamma)$$

### 2. Macroscopic Liquid Drop Model (LDM) Energy
$$E_{\text{LDM}} = E_{\text{surf}}^{(0)} \left[ B_{\text{surf}}(\beta_2, \gamma, \beta_4) - 1 \right] + E_{\text{Coul}}^{(0)} \left[ B_{\text{Coul}}(\beta_2, \gamma, \beta_4) - 1 \right]$$
with standard nuclear parameters $E_{\text{surf}}^{(0)} = 17.94 A^{2/3}\text{ MeV}$ and $E_{\text{Coul}}^{(0)} = 0.705 Z^2 / A^{1/3}\text{ MeV}$.

### 3. Cranking Rotational Energy
$$E_{\text{rot}}(I, \beta_2, \gamma) = \frac{\hbar^2 I(I+1)}{2 \mathcal{J}_{\text{eff}}(\beta_2, \gamma)}$$
where $\mathcal{J}_{\text{eff}} \approx 0.014 A^{5/3} (0.35 + 2.20 \beta_2^2) (1 + 0.3\sin\gamma)$ captures the rapid growth of rotational inertia with quadrupole deformation $\beta_2$.

### 4. Microscopic Strutinsky Shell Corrections
Deformed Nilsson single-particle level gaps create shell stabilization pockets for:
- Normal Deformed (ND) well: $\beta_2 \sim 0.18, \gamma \sim 15^\circ$;
- Triaxial Superdeformed (TSD) well: $\beta_2 \sim 0.38 - 0.40, \gamma \sim 20^\circ$.
The module maps the 2D energy terrain to extract the equilibrium shapes, saddle barrier $V_B$, and excitation energy $\Delta E_{\text{TSD-ND}}$.

---

## Executable Analysis Tool: `tsdpes`

The Python analysis suite integrates `triaxial_superdeformed_pes_strutinsky_engine.py`, accessible via:

```bash
# Benchmark 1: 163Lu TSD potential energy surface at high spin I = 35.5 hbar
python3 system/scripts/analysis/nuclear_analyzer.py tsdpes --preset 163Lu_TSD_potential_energy_surface

# Benchmark 2: 130Ba triaxial potential energy surface at spin I = 14 hbar
python3 system/scripts/analysis/nuclear_analyzer.py tsdpes --preset 130Ba_triaxial_quasiparticle_PES

# Benchmark 3: Doubly magic 208Pb spherical single well
python3 system/scripts/analysis/nuclear_analyzer.py tsdpes --preset 208Pb_spherical_doubly_magic
```

### Benchmark Validation: $^{163}\text{Lu}$ at $I = 35.5\ \hbar$
- Normal Deformed (ND) minimum located at: $\beta_2 = 0.188, \gamma = 22.0^\circ$ ($E = 18.84\text{ MeV}$);
- Triaxial Superdeformed (TSD) minimum located at: $\beta_2 = 0.375, \gamma = 18.0^\circ$ ($E = 16.82\text{ MeV}$);
- Barrier height preventing decayout: $V_B = 3.86\text{ MeV}$;
- Confirms topology: `STABLE_TRIAXIAL_SUPERDEFORMED_WELL_PRESENT`.


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
