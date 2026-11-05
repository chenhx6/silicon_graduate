---
type: concept
title: "Davydov-Rostovsky non-adiabatic triaxial rotor beta- and gamma-band mixing, Mikhailov expansion and Alaga rule deviation"
aliases: [davydov-rostovsky-model, triaxial-band-mixing, z-gamma-mixing, mikhailov-expansion, alaga-rule-deviation]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [triaxiality, non-adiabatic-rotor, band-mixing, alaga-rule, davydov-rostovsky, mikhailov-expansion, 152sm]
---

# Davydov-Rostovsky non-adiabatic triaxial rotor beta- and gamma-band mixing, Mikhailov expansion and Alaga rule deviation

## Definition

### Definition and Phenomenological Origin

In the adiabatic rotor limit (Alaga rule), interband electromagnetic transitions connecting vibrational bands to the ground-state rotational band depend solely on geometry (Clebsch-Gordan coefficients):
$$\frac{B(E2; 2_\gamma^+ \to 0_g^+)}{B(E2; 2_\gamma^+ \to 2_g^+)} = \frac{\langle 2 2 2 -2 | 0 0 \rangle^2}{\langle 2 2 2 -2 | 2 0 \rangle^2} = \frac{7}{10} = 0.700$$
Experimental measurements across transitional and deformed nuclei (e.g. $^{152}\text{Sm}, {}^{130}\text{Ba}, {}^{156}\text{Gd}$) reveal a universal systematic deviation: the observed ratio is systematically suppressed to $\mathcal{R}_{\text{exp}} \sim 0.45 - 0.58$, lower than the Alaga prediction by $20\% - 35\%$.

Based on A. S. Davydov & V. S. Rostovsky (Nucl. Phys. 60, 529, 1964), A. Bohr & B. R. Mottelson *Nuclear Structure* Vol. II §4-2 (pp. 140–165), and W. Greiner & J. A. Maruhn *Nuclear Models* Ch. 6:
This suppression arises from non-adiabatic rotation-vibration coupling: centrifugal stretching and Coriolis forces mix the $K=0$ ground-state band ($g$), the $K=0$ $\beta$-vibrational band, and the $K=2$ $\gamma$-vibrational band.

---

## Mathematical Formalism: Mikhailov Expansion & Mixing Parameter $z_\gamma$

### 1. Perturbed Wavefunctions
First-order perturbation theory mixes intrinsic $K$-components:
$$|I M, g\rangle \approx |I M 0, g\rangle - z_\beta \sqrt{I(I+1)} |I M 0, \beta\rangle - z_\gamma \sqrt{(I-1)I(I+1)(I+2)} |I M 2, \gamma\rangle$$
where $z_\gamma$ and $z_\beta$ are the non-adiabatic band-mixing parameters.

### 2. Inversion of Mixing Parameter $z_\gamma$
The interband $B(E2)$ ratio under the Mikhailov expansion is:
$$\frac{B(E2; 2_\gamma^+ \to 0_g^+)}{B(E2; 2_\gamma^+ \to 2_g^+)} = 0.700 \cdot \left[ \frac{1 - 2 z_\gamma}{1 + z_\gamma} \right]^2$$
Given the experimental ratio $\mathcal{R}_{\text{exp}}$, $z_\gamma$ is directly inverted:
$$z_\gamma = \frac{1 - \sqrt{\mathcal{R}_{\text{exp}} / 0.700}}{2 + \sqrt{\mathcal{R}_{\text{exp}} / 0.700}}$$

### 3. Microscopic Coupling Matrix Element $h_2$ & Dynamic Softness $\mu$
The rotation-vibration interaction matrix element is:
$$h_2 = \langle 2_\gamma | H_c | 2_g \rangle / \sqrt{6} = z_\gamma \cdot \frac{E(2_\gamma^+) - E(2_g^+)}{\sqrt{6}} \quad [\text{keV}]$$
The non-adiabatic softness parameter $\mu$ is evaluated from the bandhead ratio:
$$\mu = \left( \frac{E(2_g^+)}{E(0_\beta^+)} \right)^{1/4}$$

---

## Executable Analysis Tool: `rostovsky`

The Python analysis suite integrates `davydov_rostovsky_triaxial_band_mixing_solver.py`, accessible via:

```bash
# Benchmark 1: 152Sm classic rotational-vibrational transitional nucleus (Bohr Vol 2)
python3 system/scripts/analysis/nuclear_analyzer.py rostovsky --preset 152Sm_classic_transitional_nucleus

# Benchmark 2: 130Ba gamma-soft triaxial nucleus (R_exp = 0.485)
python3 system/scripts/analysis/nuclear_analyzer.py rostovsky --preset 130Ba_gamma_soft_triaxial

# Benchmark 3: Rigid rotor reference limit (R_exp = 0.700, z_gamma = 0)
python3 system/scripts/analysis/nuclear_analyzer.py rostovsky --preset rigid_rotor_zero_mixing_limit
```

### Model or fixture replay (not experimental validation): $^{152}\text{Sm}$
- Preset/public-derived ratio $\mathcal{R}_{\text{exp}} = 0.5400$ ($22.86\%$ suppression relative to Alaga $0.700$);
- Inverts mixing parameter $z_\gamma = +0.04228$;
- Rotation-vibration coupling matrix element $h_2 = 16.64\text{ keV}$, softness parameter $\mu = 0.6494$;
- Accurately predicts $B(E2; 2_\gamma \to 4_g) / B(E2; 2_\gamma \to 2_g) = 0.0629$ (matching experiment).


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

本页整理模型公式、参数化输出和观测量映射的条件性 screening logic。预设结果属于 model-derived 或 synthetic fixture；它们不能替代 raw spectra、detector response、feeding/covariance 和逐线实验审计。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
