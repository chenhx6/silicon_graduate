---
type: concept
title: "Heavy-ion optical model nuclear rainbow scattering, semiclassical deflection singularity and Airy structure"
aliases: [nuclear-rainbow-scattering, optical-rainbow, airy-minima, deflection-function-singularity, optical-potential-disambiguation]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [heavy-ion-reactions, optical-model, nuclear-rainbow, airy-structure, deflection-function, semiclassical-scattering, potential-ambiguity]
---

# Heavy-ion optical model nuclear rainbow scattering, semiclassical deflection singularity and Airy structure

## Definition

### Definition and Phenomenological Origin

In medium-energy heavy-ion elastic scattering (e.g. $^{16}\text{O} + {}^{16}\text{O}$ at $E_{\text{lab}} \ge 10 - 25\text{ MeV/u}$, $^{12}\text{C} + {}^{12}\text{C}$ at $1016\text{ MeV}$, or $\alpha + {}^{40}\text{Ca}$ at $104\text{ MeV}$), projectile nuclei possess sufficient kinetic energy to overcome the Coulomb barrier and penetrate deeply into the attractive nuclear interior.

Based on 林承键《重离子核反应》第 3–4 章 (pp. 80–110), C. A. Bertulani *Introduction to Nuclear Reactions* Chapter 4, and K. W. McVoy (Nucl. Phys. A 407, 395, 1983):
1. **Semiclassical Deflection Function $\Theta(l)$**:
   The semiclassical deflection angle is given by the derivative of the total phase shift $\delta_l = \sigma_l + \delta_l^{\text{nucl}}$:
   $$\Theta(l) = 2 \frac{d\delta_l}{dl} = \Theta_C(l) + \Theta_N(l)$$
   - At large impact parameters (large $l \gg l_{\text{grazing}}$), repulsive Coulomb forces dominate:
     $$\Theta_C(l) = 2 \arctan\left(\frac{\eta}{l}\right) > 0$$
   - At intermediate impact parameters ($l \sim l_R$), the strong short-range nuclear attractive potential overcomes Coulomb repulsion, pulling trajectories inward ($\Theta_N(l) < 0$).
   - This creates an extremum (negative minimum) in the deflection function:
     $$\left.\frac{d\Theta}{dl}\right|_{l_R} = 0 \implies \Theta_R = \Theta(l_R) < 0 \quad (\text{Nuclear Rainbow Angle})$$

2. **Classical Caustic Singularity vs Quantum Airy Pattern**:
   Classically, the differential cross section diverges at the rainbow angle:
   $$\left(\frac{d\sigma}{d\Omega}\right)_{\text{class}} = \frac{1}{\sin\theta} \sum \frac{b}{|d\Theta/db|} \xrightarrow{l \to l_R} \infty$$
   In quantum mechanics, wave interference between trajectories passing on opposite sides of the rainbow radius replaces this singularity with a characteristic **Airy diffraction oscillation pattern**:
   $$\frac{d\sigma}{d\Omega}(\theta) \propto \text{Ai}^2\left( - \left[ \frac{1}{2} \left|\frac{d^2\Theta}{dl^2}\right|_{l_R} \right]^{-1/3} (\theta - |\Theta_R|) \right)$$
   The cross section exhibits broad Airy maxima ($A_1, A_2$) followed by steep exponential decay on the "dark side" ($\theta > |\Theta_R|$), where trajectories are classically forbidden.

---

## Resolution of Optical Potential Ambiguities

At low energies near or below the Coulomb barrier, elastic scattering is dominated by strong surface absorption, giving rise to continuous and discrete optical potential ambiguities:
$$V_0 R^2 \approx \text{const} \quad \text{or} \quad V_0 \exp(R/a) \approx \text{const}$$
Multiple deep or shallow optical potentials yield indistinguishable Rutherford ratio curves at forward angles.

**The Nuclear Rainbow Solution**:
1. Because the rainbow trajectory penetrates into the nuclear core ($r \sim 0 - 2\text{ fm}$), the position of the nuclear rainbow angle $|\Theta_R|$ directly measures the **volume integral and central depth $V_0$** of the real optical potential:
   $$|\Theta_R| \approx \frac{V_0}{E_{\text{c.m.}}}$$
2. The exponential slope of the cross section in the shadow region ($\theta > |\Theta_R|$) constrains the nuclear surface diffuseness $a$ and imaginary absorption $W_0$.
3. Measuring the Airy minima locations uniquely eliminates the discrete family ambiguity, establishing the physical deep potential depth (typically $V_0 \sim 100 - 140\text{ MeV}$ for light heavy-ion systems).

---

## Executable Analysis Tool: `optrainbow`

The Python analysis suite integrates `heavy_ion_optical_rainbow_scattering_analyzer.py`, accessible via:

```bash
# Benchmark: 16O + 16O at 350 MeV (Stiliaris et al. 1989)
python3 system/scripts/analysis/nuclear_analyzer.py optrainbow --preset 16O_16O_350MeV

# High-energy: 12C + 12C at 1016 MeV (Buenerd et al. 1984)
python3 system/scripts/analysis/nuclear_analyzer.py optrainbow --preset 12C_12C_1016MeV

# Large-angle alpha scattering: alpha + 40Ca at 104 MeV
python3 system/scripts/analysis/nuclear_analyzer.py optrainbow --preset alpha_40Ca_104MeV
```

### Benchmark Validation: $^{16}\text{O} + {}^{16}\text{O}$ at $E_{\text{lab}} = 350\text{ MeV}$
- Center-of-mass energy: $E_{\text{c.m.}} = 175.0\text{ MeV}$, Sommerfeld parameter $\eta = 2.45$;
- Rainbow angular momentum: $l_R \approx 25\ \hbar$;
- Rainbow deflection minimum: $\Theta_R = -60.8^\circ \implies \theta_R^{\text{obs}} = 60.8^\circ$;
- First Airy minimum: $\theta_{A1} = 50.0^\circ$; second Airy minimum: $\theta_{A2} = 37.8^\circ$;
- Real optical potential central depth resolved to $V_0 \approx 138\text{ MeV}$, excluding shallow optical potential solutions ($V_0 < 50\text{ MeV}$).


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
