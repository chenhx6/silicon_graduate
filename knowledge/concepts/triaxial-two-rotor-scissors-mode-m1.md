---
type: concept
title: "Triaxial Two-Rotor Model (TRM) scissors mode magnetic dipole M1 excitation splitting and sum rules"
aliases: [triaxial-scissors-mode, scissors-mode-splitting, two-rotor-model, magnetic-dipole-resonance, mixed-symmetry-scissors]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [nuclear-models, scissors-mode, m1-transitions, two-rotor-model, triaxiality, 156gd, 134ba, 196pt]
---

# Triaxial Two-Rotor Model (TRM) scissors mode magnetic dipole M1 excitation splitting and sum rules

## Definition

### Physical Phenomenon & Two-Rotor Model (TRM)

The nuclear Scissors Mode (Lo Iudice & Palumbo PRL 1978, Bohle et al. PLB 1984) is a fundamental collective magnetic dipole ($M1$) excitation in deformed nuclei, representing the out-of-phase rotational oscillation of deformed proton versus neutron clouds about an axis perpendicular to the deformation axis.

In axially symmetric nuclei ($\gamma = 0^\circ$), the mode occurs solely about the transverse axis, resulting in a single prominent $1^+$ resonance at $E_{1^+} \approx 2.5 - 3.5\text{ MeV}$ with $B(M1; 0^+ \to 1^+) \approx 2 - 3\ \mu_N^2$.

---

## Triaxial Deformation & Scissors Doublet Splitting

In triaxially deformed nuclei with deformation parameters $(\beta_2, \gamma)$:
Because axial symmetry is broken ($\mathcal{J}_s \ne \mathcal{J}_i \ne \mathcal{J}_l$), the relative proton-neutron rotational angle decouples into **TWO orthogonal scissors modes**:
1. **Short-Axis Scissors Mode ($1^+_s$)**:
   Proton-neutron counter-oscillation in the intermediate-long plane about the short axis.
   Restoring shear deformation:
   $$\delta_s = \sqrt{\frac{15}{\pi}} \beta_2 \sin\gamma$$
2. **Long-Axis Scissors Mode ($1^+_l$)**:
   Proton-neutron counter-oscillation in the short-intermediate plane about the long axis.
   Restoring shear deformation:
   $$\delta_l = \sqrt{\frac{15}{\pi}} \beta_2 \sin\left(\frac{\pi}{3} - \gamma\right)$$

### Restoring Force and Reduced Inertia:
$$C_k = \frac{4 Z N}{A^2} b_$C_{\text{sym}}$ \cdot \delta_k^2 \cdot \frac{A}{6}$$
$$\mathcal{J}_{\text{red}, k} = \frac{Z N}{A^2} \mathcal{J}_k(\beta_2, \gamma)$$
where $b_$C_{\text{sym}}$ \approx 28 - 32\text{ MeV}$ is the nuclear symmetry energy.

### Eigenfrequencies & $B(M1)$ Strengths:
$$E_{1^+, k} = \hbar\omega_k = \hbar \sqrt{\frac{C_k}{\mathcal{J}_{\text{red}, k}}}$$
$$B(M1; 0^+ \to 1_k^+) = \frac{3}{16\pi} \mathcal{J}_{\text{red}, k} \cdot \omega_k \cdot (g_p - g_n)^2 \quad (\mu_N^2)$$

When $\gamma \approx 20^\circ - 30^\circ$ (e.g. $^{134}\text{Ba}$), the scissors mode splits into a **doublet of $1^+$ states** separated by $\Delta E_{M1} \approx 0.5 - 1.5\text{ MeV}$, serving as a direct spectroscopic signature of triaxiality in low-lying $M1$ photo-excitation and in-beam spectroscopy!

---

## Executable Analysis Tool: `scissm1`

The Python analysis suite integrates `triaxial_two_rotor_scissors_mode_m1_solver.py`, accessible via CLI:

```bash
# 1. Classic axial prolate scissors baseline: 156Gd (single peak, Delta E_M1 = 0)
python3 system/scripts/analysis/nuclear_analyzer.py scissm1 --preset 156Gd_axial_prolate_baseline

# 2. Triaxial scissors mode doublet splitting: 134Ba (doublet separated by 1.45 MeV)
python3 system/scripts/analysis/nuclear_analyzer.py scissm1 --preset 134Ba_triaxial_scissors_doublet

# 3. Gamma-soft / oblate scissors candidate: 196Pt
python3 system/scripts/analysis/nuclear_analyzer.py scissm1 --preset 196Pt_gamma_soft_oblate
```

---

## Literature and Textbook Provenance

- **K. Heyde**, *Basic Ideas and Concepts in Nuclear Physics* (3rd Ed.), Chapter 9, §9.4.
- **W. Greiner & J. A. Maruhn**, *Nuclear Models* (Springer 1996), Chapter 11.
- **N. Lo Iudice & F. Palumbo**, Phys. Rev. Lett. 41, 1532 (1978).
- **D. Bohle et al.**, Phys. Lett. B 137, 27 (1984).
- **A. A. Raduta**, *Nuclear Structure with Coherent States*, Chapter 4.


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
