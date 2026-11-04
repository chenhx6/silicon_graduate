---
type: concept
title: "Coriolis anti-pairing (CAP) dynamic pairing gap quenching, superfluid-to-normal phase transition and triaxial moment of inertia expansion"
aliases: [coriolis-anti-pairing, cap-effect, mottelson-valatin-effect, pairing-gap-quenching, moi-cap-expansion]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [high-spin, pairing-correlations, coriolis-anti-pairing, cap, moments-of-inertia, phase-transition, 163lu]
---

# Coriolis anti-pairing (CAP) dynamic pairing gap quenching, superfluid-to-normal phase transition and triaxial moment of inertia expansion

## Definition

### Definition and Phenomenological Origin

In deformed low-energy atomic nuclei, short-range attractive residual interactions between nucleons form Cooper pairs, generating a static monopole pairing gap $\Delta_0 \sim 0.8 - 1.3\text{ MeV}$ and reducing nuclear moments of inertia to $30\% - 50\%$ of the rigid-body value (irrotational fluid flow).

Based on Bohr & Mottelson *Nuclear Structure* Vol. II §4-3 & §6-3, *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025) Chapters 2 & 9 (PDF pp. 204–221), and B. R. Mottelson & J. G. Valatin (Phys. Rev. Lett. 5, 511, 1960):
As the nucleus rotates with collective frequency $\omega_{\text{rot}}$, the Coriolis force $\vec{F}_{\text{Cor}} = -2m (\vec{\omega} \times \vec{v})$ acts in opposite directions on time-reversed paired nucleons $(j, -j)$.
This exerts a pair-breaking rotational torque that unbinds Cooper pairs—the **Mottelson-Valatin Coriolis Anti-Pairing (CAP)** effect.

---

## Mathematical Formalism: Dynamic Gap Quenching & MOI Evolution

### 1. Monopole Pairing Gap Quenching Law
Self-consistent mean-field BCS and cranking theory predict that the pairing gap $\Delta(\omega)$ collapses monotonically with frequency:
$$\Delta(\omega) = \Delta_0 \sqrt{ \max\left( 0.0, 1 - \left( \frac{\omega}{\omega_{\text{crit}}} \right)^2 \right) }$$
where $\omega_{\text{crit}}$ is the critical CAP frequency ($\sim 0.35 - 0.50\text{ MeV}/\hbar$, corresponding to spin $I_{\text{CAP}} \sim 25 - 40\ \hbar$).
At $\omega = \omega_{\text{crit}}$, the pairing gap vanishes ($\Delta \to 0$), marking a continuous second-order phase transition from the superfluid state to the normal Fermi liquid regime.

### 2. Triaxial Moments of Inertia Non-Linear Expansion
As the pairing gap collapses, each principal moment of inertia expands from the irrotational superfluid baseline towards the classical rigid-body limit:
$$\mathcal{J}_k(\Delta) = \mathcal{J}_{\text{rig}, k} \cdot \left[ 1 - \left( 1 - \frac{\mathcal{J}_{\text{irr}, k}}{\mathcal{J}_{\text{rig}, k}} \right) \frac{\Delta(\omega)}{\Delta_0} \right] \quad (k = s, m, l)$$
For triaxial shapes, the intermediate ($m$) axis experiences the fastest expansion, creating the dynamical moment of inertia asymmetry required to stabilize high-spin transverse wobbling and chiral doublets before final band termination.

---

## Executable Analysis Tool: `capgap`

The Python analysis suite integrates `coriolis_anti_pairing_gap_quenching_moi_engine.py`, accessible via:

```bash
# Benchmark 1: 163Lu TSD band CAP pairing collapse (Delta_0 = 0.95 MeV, omega_crit = 0.45 MeV/hbar)
python3 system/scripts/analysis/nuclear_analyzer.py capgap --preset 163Lu_TSD_superfluid_to_normal_phase_transition

# Benchmark 2: 130Ba transitional triaxial CAP quenching
python3 system/scripts/analysis/nuclear_analyzer.py capgap --preset 130Ba_transitional_triaxial_cap

# Benchmark 3: Zero-pairing rigid rotor limit
python3 system/scripts/analysis/nuclear_analyzer.py capgap --preset rigid_rotor_zero_pairing_limit
```

### Benchmark Validation: $^{163}\text{Lu}$ Superfluid-to-Normal Transition
- At $I = 10\ \hbar$: $\omega = 0.268\text{ MeV}/\hbar$, $\Delta = 0.763\text{ MeV}$ ($19.7\%$ quenched), $\mathcal{J}_m = 37.3\ \hbar^2/\text{MeV}$;
- At $I = 25\ \hbar$: $\omega = 0.427\text{ MeV}/\hbar$, $\Delta = 0.297\text{ MeV}$ ($68.7\%$ quenched), $\mathcal{J}_m = 58.5\ \hbar^2/\text{MeV}$;
- At $I = 35\ \hbar$: $\Delta \to 0.000\text{ MeV}$ ($100\%$ collapse), identifying the critical transition threshold $I_{\text{CAP}} \approx 35.0\ \hbar$;
- Beyond $35\ \hbar$: $\mathcal{J}_m$ locks at the rigid limit $72.0\ \hbar^2/\text{MeV}$, reproducing the observed high-spin moment of inertia plateau.


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
