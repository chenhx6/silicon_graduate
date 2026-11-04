---
type: concept
title: "Heavy-ion triaxial deformed nuclei fusion barrier distribution D_fus(E) inversion and in-plane belly splitting"
aliases: [triaxial-fusion-barrier, barrier-distribution-triaxial, wong-orientation-average, heavy-ion-triaxial-fingerprint]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [heavy-ion-reactions, fusion-cross-section, barrier-distribution, triaxiality, gamma-deformation, wong-formula, 154sm, 186w]
---

# Heavy-ion triaxial deformed nuclei fusion barrier distribution $D_{\text{fus}}(E)$ inversion and in-plane belly splitting

## Definition

### Phenomenological Definition & Channel Coupling

In heavy-ion fusion reactions around the Coulomb barrier, the measured fusion cross section $\sigma_{\text{fus}}(E)$ exceeds the one-dimensional barrier penetration model (1D-BPM) by several orders of magnitude at sub-barrier energies. This phenomenon is driven by the dynamic coupling of the relative radial motion to target/projectile internal collective degrees of freedom (quadrupole/hexadecapole deformation, rotational bands, surface vibrations).

As formulated by Rowley, Satchler & Stelson (PLB 1991), 林承键《重离子核反应》第 4 章 §4.3, and C. A. Bertulani *Introduction to Nuclear Reactions* §7.4:
The representation of channel coupling is formalized through the experimental **fusion barrier distribution**:
$$D_{\text{fus}}(E) = \frac{d^2(E \sigma_{\text{fus}})}{dE^2}$$

---

## Orientation-Dependent Fusion Barrier for Triaxial Nuclei

For a spherical projectile colliding with a triaxially deformed target nucleus with Bohr deformation parameters $(\beta_2, \gamma)$:
The nuclear surface in the intrinsic frame is:
$$R(\theta, \phi) = R_0 \left[ 1 + \sqrt{\frac{5}{16\pi}} \beta_2 \left( \cos\gamma (3\cos^2\theta - 1) + \sqrt{3} \sin\gamma \sin^2\theta \cos(2\phi) \right) \right]$$

The orientation-dependent Coulomb + nuclear proximity barrier height is:
$$V_B(\theta, \phi) = V_{B0} - \Delta V_B \left[ \cos\gamma (3\cos^2\theta - 1) + \sqrt{3} \sin\gamma \sin^2\theta \cos(2\phi) \right]$$
where $\Delta V_B = V_{B0} \sqrt{\frac{5}{16\pi}} \frac{R_t}{R_p + R_t} \beta_2$.

In Wong's parabolic barrier penetration formula, the total fusion cross section is obtained by 2D spherical orientation averaging:
$$\sigma_{\text{fus}}(E) = \frac{R_B^2 \hbar\omega_B}{2E} \frac{2}{\pi} \int_0^{\pi/2} \sin\theta d\theta \int_0^{\pi/2} d\phi \ln\left[ 1 + \exp\left( \frac{2\pi(E - V_B(\theta, \phi))}{\hbar\omega_B} \right) \right]$$

---

## Structural Fingerprint: The Three-Peaked Barrier Distribution

1. **Axially Prolate Target ($\gamma = 0^\circ$, e.g. $^{154}\text{Sm}$)**:
   - $V_B(\theta = 0, \text{pole-on})$ produces a low-energy peak;
   - $V_B(\theta = \pi/2, \text{side-on})$ is degenerate for all $\phi$, producing a single high-energy peak ($\Delta V_{\text{tri}} \equiv 0$).
   - The resulting $D_{\text{fus}}(E)$ exhibits a classic **two-peaked structure**.

2. **Triaxial Target ($0^\circ < \gamma < 60^\circ$, e.g. $\gamma \approx 20^\circ - 30^\circ$, $^{186}\text{W}$, $^{100}\text{Mo}$)**:
   - Non-axial deformation $\gamma$ lifts the azimuthal degeneracy along the equatorial belly:
     $$V_{\text{side}}(\phi = 0, \text{short axis}) = V_{B0} - \Delta V_B [-\cos\gamma + \sqrt{3}\sin\gamma]$$
     $$V_{\text{side}}(\phi = \pi/2, \text{intermediate axis}) = V_{B0} - \Delta V_B [-\cos\gamma - \sqrt{3}\sin\gamma]$$
   - The in-plane belly splitting:
     $$\Delta V_{\text{tri}} = 2\sqrt{3} \Delta V_B \sin\gamma$$
     splits the high-energy side-on peak into two distinct components separated by $3 - 6\text{ MeV}$!
   - This produces an unmistakable **three-peaked barrier distribution fingerprint**, directly proving ground-state triaxiality prior to high-spin in-beam excitation!

---

## Executable Analysis Tool: `triaxfus`

The Python analysis suite integrates `heavy_ion_triaxial_fusion_barrier_distribution_inverter.py`, accessible via CLI:

```bash
# 1. Classic prolate baseline: 16O + 154Sm (two peaks, zero in-plane belly splitting)
python3 system/scripts/analysis/nuclear_analyzer.py triaxfus --preset 16O_154Sm_prolate_baseline

# 2. Triaxial candidate: 16O + 186W (three distinct peaks, Delta V_tri = 4.73 MeV)
python3 system/scripts/analysis/nuclear_analyzer.py triaxfus --preset 16O_186W_triaxial_candidate

# 3. In-beam entry-state fusion: 36S + 100Mo (in-plane splitting Delta V_tri = 4.42 MeV)
python3 system/scripts/analysis/nuclear_analyzer.py triaxfus --preset 36S_100Mo_in_beam_fusion
```

---

## Literature and Textbook Provenance

- **林承键**, 《重离子核反应》 (科学出版社), 第 4 章 §4.3.
- **C. A. Bertulani & P. Danielewicz**, *Introduction to Nuclear Reactions* (CRC 2004), Chapter 7, §7.4.
- **Rowley, Satchler & Stelson**, Phys. Lett. B 254, 25 (1991).
- **Leigh et al.**, Phys. Rev. C 52, 3151 (1995).


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
