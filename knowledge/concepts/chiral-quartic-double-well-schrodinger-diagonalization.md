---
type: concept
title: "Chiral collective motion quartic double-well potential 1D Schrödinger equation diagonalization, tunneling splitting and wavefunctions"
aliases: [chiral-schrodinger-diagonalizer, quartic-double-well-chirality, chiral-tunneling-splitting, lacm-chiral-vibration, 135nd-chiral-vibration]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [triaxiality, nuclear-chirality, collective-hamiltonian, schrodinger-equation, double-well-potential, chiral-vibration, 135nd]
---

# Chiral collective motion quartic double-well potential 1D Schrödinger equation diagonalization, tunneling splitting and wavefunctions

## Definition

### Definition and Phenomenological Origin

Nuclear chirality can manifest in two distinct dynamical regimes:
1. **Static Chiral Rotation**: In deep double-well potentials with high barriers, the nucleus possesses stable left- and right-handed aplanar shapes, producing nearly degenerate chiral doublet bands ($\Delta E \le 50 - 100\text{ keV}$).
2. **Chiral Vibration**: Near the critical bifurcation spin ($J \sim J_{\text{crit}}$), the barrier separating the left and right wells is shallow or flat-bottomed. The angular momentum vector executes large-amplitude collective vibrations (LACM) across the planar boundary ($\phi = 0^\circ$), producing widely split partner bands ($\Delta E \sim 250 - 400\text{ keV}$).

Based on *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025) Chapter 2 (PDF pp. 43–80), Chapter 10 (PDF pp. 222–238), S. Mukhopadhyay et al. (Phys. Rev. Lett. 99, 172501, 2007), and Q. B. Chen et al. (Phys. Rev. C 96, 051303(R), 2017):
Semiquantal WKB action methods fail in the shallow-barrier regime. An exact numerical diagonalization of the collective 1D Schrödinger equation is required.

---

## Mathematical Formalism: 1D Collective Hamiltonian

### 1. Schrödinger Equation in Out-of-Plane Coordinate $\phi$
The collective motion along the out-of-plane azimuth $\phi \in [-\pi/2, \pi/2]$ is governed by:
$$\left[ -\frac{\hbar^2}{2 B_\phi} \frac{d^2}{d\phi^2} + V(\phi) \right] \Psi_n(\phi) = E_n \Psi_n(\phi)$$
where $B_\phi$ is the collective mass parameter.

### 2. Anharmonic Quartic Potential
The orientation potential energy is expanded as:
$$V(\phi) = \frac{1}{2} c_2 \phi^2 + \frac{1}{4} c_4 \phi^4$$
- For $c_2 < 0, c_4 > 0$: symmetric double-well with minima at $\pm\phi_0 = \pm\sqrt{-c_2/c_4}$ and central barrier $V_B = c_2^2 / (4c_4)$;
- For $c_2 > 0, c_4 \ge 0$: single-well planar harmonic/anharmonic vibrator.

### 3. Finite-Difference Tridiagonal Diagonalization
Discretizing on a grid $\phi_i$ ($i = 1 \dots N_{\text{grid}}$) with spacing $\Delta\phi$:
$$H_{ii} = \frac{\hbar^2}{B_\phi \Delta\phi^2} + V(\phi_i), \quad H_{i, i+1} = H_{i+1, i} = -\frac{\hbar^2}{2 B_\phi \Delta\phi^2}$$
Diagonalizing this tridiagonal system yields exact energy levels:
- $E_0$: Symmetric ground state (even parity, Band 1);
- $E_1$: Antisymmetric first excited state (odd parity, Band 2);
- Chiral energy splitting: $\Delta E_{\text{chir}} = E_1 - E_0$;
- Two-phonon excitation: $E_2 - E_0$;
- Anharmonicity ratio: $R_{21} = (E_2 - E_0) / (E_1 - E_0)$ ($R_{21} \approx 2.0$ for harmonic vibrator, $R_{21} \gg 2.0$ for tunneling doublets).

---

## Executable Analysis Tool: `chirasch`

The Python analysis suite integrates `chiral_vibrational_quartic_schrodinger_diagonalizer.py`, accessible via:

```bash
# Benchmark 1: 135Nd soft-potential chiral vibration (Mukhopadhyay 2007)
python3 system/scripts/analysis/nuclear_analyzer.py chirasch --preset 135Nd_chiral_vibration

# Benchmark 2: 134Pr deep double-well static chirality (Tonev 2006)
python3 system/scripts/analysis/nuclear_analyzer.py chirasch --preset 134Pr_static_chiral_rotation

# Benchmark 3: Pure harmonic vibrator reference limit
python3 system/scripts/analysis/nuclear_analyzer.py chirasch --preset harmonic_vibrator_limit
```

### Benchmark Validation
1. **$^{135}\text{Nd}$ Chiral Vibration**:
   Shallow barrier $V_B = 170.1\text{ keV}$ produces large vibrational splitting $\Delta E_{\text{chir}} = 332.5\text{ keV}$ and $R_{21} = 2.87$, in excellent agreement with experimental observation.
2. **$^{134}\text{Pr}$ Static Chirality**:
   Deep barrier $V_B = 640.0\text{ keV}$ collapses the splitting to $\Delta E_{\text{chir}} = 105.4\text{ keV}$ with high anharmonicity $R_{21} = 6.36$.
3. **Harmonic Limit**:
   Reproduces exact harmonic ladder $R_{21} = 2.06 \approx 2.00$ and zero barrier height.


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
