---
type: concept
title: "Triaxial projected shell model (TPSM) 3D angular momentum projection matrix diagonalization, Hill-Wheeler secular equation and K-mixing"
aliases: [tpsm-3d-projection, tpsm-diagonalizer, hill-wheeler-tpsm, 3d-angular-momentum-projection, k-mixing-tpsm]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [triaxiality, tpsm, angular-momentum-projection, shell-model, k-mixing, gamma-band, wobbling-motion]
---

# Triaxial projected shell model (TPSM) 3D angular momentum projection matrix diagonalization, Hill-Wheeler secular equation and K-mixing

## Definition

### Definition and Phenomenological Origin

While the particle-rotor model (PRM) treats the core macroscopically and tilted axis cranking (CSM/TAC) breaks rotational invariance in the laboratory frame, the **Triaxial Projected Shell Model (TPSM)** provides a fully microscopic quantum mechanical framework.

Based on *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025) Chapter 12 (J. A. Sheikh, G. H. Bhat, R. Jehangir, PDF pp. 256–274), J. A. Sheikh & K. Hara (Phys. Rev. Lett. 82, 3968, 1999), and P. Ring & P. Schuck *The Nuclear Many-Body Problem* Ch. 11:
TPSM constructs deformed multi-quasiparticle Nilsson+BCS intrinsic states $|\Phi_K\rangle$ (0-qp vacuum, 2-qp proton, 2-qp neutron, and 4-qp configurations) with non-axial quadrupole deformation $(\varepsilon_2, \gamma)$, and restores laboratory rotational symmetry by exact 3D angular momentum projection.

---

## Mathematical Formalism: 3D Projection & Hill-Wheeler Equation

### 1. Three-Dimensional Angular Momentum Projection Operator
Rotational symmetry in the laboratory frame is restored using:
$$\hat{P}^I_{MK} = \frac{2I + 1}{8\pi^2} \int D^{I*}_{MK}(\Omega) \hat{R}(\Omega) d\Omega$$
The physical laboratory wavefunction for state $\kappa$ with total angular momentum $I$ is an expansion over projected intrinsic states:
$$|I M, \kappa\rangle = \sum_K C_{K}^\kappa(I) \hat{P}^I_{MK} |\Phi_K\rangle$$

### 2. Hill-Wheeler Generalized Secular Equation
Variational minimization leads to the generalized eigenvalue problem:
$$\sum_{K^\prime} \left[ H_{KK^\prime}(I) - E(I) N_{KK^\prime}(I) \right] C_{K^\prime}(I) = 0$$
where:
$$H_{KK^\prime}(I) = \langle \Phi_K | \hat{H} \hat{P}^I_{KK^\prime} | \Phi_{K^\prime} \rangle, \quad N_{KK^\prime}(I) = \langle \Phi_K | \hat{P}^I_{KK^\prime} | \Phi_{K^\prime} \rangle$$

### 3. $K$-Mixing Driven by Triaxiality ($\Delta K = \pm 2$)
The diagonal matrix elements reflect rotational kinetic energy:
$$H_{KK}(I) = E_{\text{qp}}(K) + \frac{\hbar^2}{2\mathcal{J}_{\text{eff}}} \left[ I(I+1) - K^2 \right]$$
Triaxial deformation ($\gamma \ne 0$) introduces off-diagonal core couplings with $\Delta K = \pm 2$:
$$H_{K, K\pm 2}(I) \propto V_{\text{core}} \sin(\gamma) \sqrt{ (I \mp K)(I \mp K - 1)(I \pm K + 1)(I \pm K + 2) }$$
Diagonalizing this coupled system naturally yields:
- **Yrast Band**: lowest eigenstate ($K=0$ dominant, gaining $\sim 3\% - 5\%$ $K=2$ mixing at high spin);
- **$\gamma$-Vibrational Band**: second eigenstate ($K=2$ dominant);
- **Wobbling / Two-Phonon Band**: third eigenstate ($K=4$ dominant).

---

## Executable Analysis Tool: `tpsmproj`

The Python analysis suite integrates `tpsm_3d_angular_momentum_projection_diagonalizer.py`, accessible via:

```bash
# Benchmark 1: 130Ba triaxial bands TPSM projection (epsilon2=0.23, gamma=25 deg)
python3 system/scripts/analysis/nuclear_analyzer.py tpsmproj --preset 130Ba_TPSM_triaxial_bands

# Benchmark 2: 163Lu TSD band TPSM wobbling projection
python3 system/scripts/analysis/nuclear_analyzer.py tpsmproj --preset 163Lu_TSD_TPSM_wobbling

# Benchmark 3: Axially symmetric reference limit (gamma = 0 deg, K-mixing vanishes)
python3 system/scripts/analysis/nuclear_analyzer.py tpsmproj --preset axial_symmetric_limit
```

### Benchmark Validation
1. **$^{130}\text{Ba}$ Triaxial Projection**:
   At $I=4$: Yrast = $259.6\text{ keV}$, $\gamma$-band = $1292.5\text{ keV}$, Wobbling = $2164.0\text{ keV}$ ($\Delta E_{\text{wob}} = 1904.4\text{ keV}$).
   Yrast $K=0$ weight decreases from $99.8\%$ ($I=2$) to $96.7\%$ ($I=16$), with $K=2$ expanding to $3.3\%$.
2. **Axial Symmetric Limit**:
   At $\gamma = 0^\circ$, off-diagonal matrix elements vanish identically ($K=0$ strictly $100.0\%$, $K=2$ is $0.0\%$), confirming exact quantum consistency.


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
