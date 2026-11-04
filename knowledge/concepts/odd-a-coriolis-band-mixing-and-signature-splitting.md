---
type: concept
title: "Odd-A deformed Coriolis band mixing, signature splitting and decoupling parameter"
aliases: [coriolis-band-mixing, signature-splitting-odd-a, decoupling-parameter-kerman, deformed-particle-rotor-mixing]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [coriolis-mixing, odd-a-nuclei, signature-splitting, decoupling-parameter, nilsson-model, particle-rotor, kerman-model, deformed-nuclei]
---

# Odd-A deformed Coriolis band mixing, signature splitting and decoupling parameter

## Definition

### Definition and Theoretical Origin

In deformed odd-$A$ atomic nuclei (such as odd-neutron rare earths $^{159}\text{Dy}, ^{167}\text{Er}$ or odd-proton transitional nuclei $^{135}\text{Pr}, ^{169}\text{Tm}$), the odd valence nucleon moves in an axially deformed Nilsson potential with projection $K = \Omega$ along the symmetry axis.

As the deformed core rotates, the Coriolis interaction couples the single-particle angular momentum $\vec{j}$ to the collective rotation $\vec{R} = \vec{I} - \vec{j}$:

Based on A. Bohr & B. R. Mottelson *Nuclear Structure* Vol. II §4-3 (pp. 158–175), 卢希庭《原子核物理（修订版）》第 8 章 §8.6, and A. K. Kerman (1956):

The total Hamiltonian in the body-fixed intrinsic coordinate frame is:
$$H = H_0 + H_{\text{rot}} + H_{\text{Coriolis}}$$
$$H_{\text{rot}} = A_{\text{rot}} [ I(I+1) - K^2 ] \quad \left(A_{\text{rot}} = \frac{\hbar^2}{2\mathcal{J}}\right)$$
$$H_{\text{Coriolis}} = -A_{\text{rot}} [ I_+ j_- + I_- j_+ ]$$

---

## Matrix Elements and Algebraic Diagonalization

In the strong-coupling basis $|I, M, K, j\rangle$:

1. **Diagonal Matrix Elements**:
   $$\langle I, K \mid H \mid I, K \rangle = \varepsilon_K + A_{\text{rot}} [I(I+1) - K^2] + \delta_{K, 1/2} \cdot a \cdot A_{\text{rot}} (-1)^{I+1/2} (I+1/2)$$
   where $\varepsilon_K$ is the unperturbed Nilsson intrinsic single-particle energy, and $a$ is the **decoupling parameter** for the $K = 1/2$ band:
   $$a = -\sum_j (-1)^{j+1/2} (j + 1/2) |c_j|^2$$
   For high-$j$ intruder orbitals ($h_{11/2}, i_{13/2}$), $a$ can reach large negative or positive values ($a \sim -3.5$ or $+0.85$), causing massive zigzag shifts in energy levels.

2. **Off-Diagonal Coriolis Matrix Elements ($\Delta K = \pm 1$)**:
   $$\langle I, K+1 \mid H_{\text{Coriolis}} \mid I, K \rangle = -A_{\text{rot}} \sqrt{(I-K)(I+K+1)} \langle K+1 \mid j_+ \mid K \rangle$$
   In the single-$j$ shell approximation:
   $$\langle K+1 \mid j_+ \mid K \rangle = \sqrt{j(j+1) - K(K+1)}$$
   For $j = 11/2$: $\langle 3/2 \mid j_+ \mid 1/2 \rangle = \sqrt{35} \approx 5.916$; for $j = 13/2$: $\langle 3/2 \mid j_+ \mid 1/2 \rangle = \sqrt{48} \approx 6.928$.

3. **Tridiagonal Hamiltonian Matrix**:
   For each total spin $I$, the basis spans all allowed projections $K \le I$. Exact algebraic diagonalization yields:
   - Perturbed eigenenergies $E_i(I)$;
   - Mixed wavefunctions $|\Psi_i(I)\rangle = \sum_K c_{i, K}(I) |I, K\rangle$.

---

## Signature Splitting and Rotational Alignment

Coriolis mixing breaks the degeneracy between the two signature branches ($\alpha = +1/2$ and $\alpha = -1/2$):
$$S(I) = \frac{E(I) - E(I-1)}{2I}$$

1. **Favored vs Unfavored Signatures**:
   States with favored signature $\alpha_f = \frac{1}{2}(-1)^{j-1/2}$ receive strong downward Coriolis shifts, lowering their excitation energies relative to unfavored states;
2. **Wavefunction Delocalization**:
   At high spin $I \gg j$, the single-particle angular momentum completely decouples from the symmetry axis and aligns with the collective rotation axis (**rotation alignment**, Stephens 1975). The wavefunction $|\Psi\rangle$ spreads across all $K$ projections ($K = 1/2, 3/2, 5/2, \dots$);
3. **Signature Inversion**:
   At low spins in transitional nuclei, residual proton-neutron interactions or triaxial shapes can invert the phase of signature staggering until a critical frequency $\omega_{\text{inv}}$ is reached.

---

## Canonical Experimental Benchmarks

- **$^{159}\text{Dy}$ ($i_{13/2}$ neutron band mixing)**:
  - Mixing between $K = 1/2^+, 3/2^+, 5/2^+, 7/2^+$ ($A_{\text{rot}} = 12.0\text{ keV}, a = 0.85$);
  - At $I = 9/2^+$, the yrast state wavefunction has $c_{1/2} = 0.659, c_{3/2} = 0.654, c_{5/2} = 0.355$, demonstrating extreme multi-band Coriolis mixing.
- **$^{135}\text{Pr}$ ($h_{11/2}$ proton band mixing)**:
  - $a = -3.20$, producing huge signature splitting in the yrast band head.
- **$^{169}\text{Tm}$ ($K = 1/2^+ [411]$ decoupling)**:
  - $a = -0.77$, ground bandhead exhibits classic inverted $1/2^+ - 3/2^+$ doublet ordering.

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用


- **Bohr, A. & Mottelson, B. R.**: *Nuclear Structure*, Vol. II, Chapter 4 §4-3 (Perturbations of Rotational Motion, Coriolis Coupling), pp. 158–175.
- **Lu Xiting (卢希庭)**: *Nuclear Physics (Revised Edition)* (《原子核物理（修订版）》), Atomic Energy Press (2000), Chapter 8 §8.6.
- **Kerman, A. K.**: *Rotational perturbations in nuclei of odd mass*, Mat. Fys. Medd. Dan. Vid. Selsk. 30, no. 15 (1956).
- **Stephens, F. S.**: *Coriolis effects and rotation-alignment in nuclei*, Rev. Mod. Phys. 47, 43–65 (1975).


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
