---
type: concept
title: "Particle-triaxial-rotor model (PTRM) diagonalization and microscopic wobbling"
aliases: [ptrm-model, particle-triaxial-rotor, ptrm-diagonalization, microscopic-wobbling-ptrm, meyer-ter-vehn-model]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [triaxiality, ptrm, particle-rotor-model, wobbling, meyer-ter-vehn, hamamoto-model, algebraic-diagonalization, d2-symmetry]
---

# Particle-triaxial-rotor model (PTRM) diagonalization and microscopic wobbling

## Definition

### Definition and Theoretical Framework

While high-spin harmonic approximations (Bohr-Mottelson 1975; Frauendorf & Dönau 2014) provide intuitive asymptotic expressions for wobbling frequencies $\hbar\omega_w \propto \sqrt{\dots}$ in the limit $I \gg j$, they break down at low spins ($I \approx 13/2 - 21/2\ \hbar$) where non-linear centrifugal and Coriolis terms dominate.

To achieve exact microscopic predictions across the entire low-to-high spin evolution, the **Particle-Triaxial-Rotor Model (PTRM)** (J. Meyer-ter-Vehn, Nucl. Phys. A 249, 111, 1975; I. Hamamoto, Phys. Rev. C 65, 044305, 2002; Raduta in Petrache CRC 2025 Ch. 8) diagonalizes the coupled Hamiltonian:

$$H_{\text{PTRM}} = H_{\text{rot}} + H_{\text{sp}}$$
$$H_{\text{rot}} = \frac{(I_s - j_s)^2}{2\mathcal{J}_s} + \frac{(I_m - j_m)^2}{2\mathcal{J}_m} + \frac{(I_l - j_l)^2}{2\mathcal{J}_l}$$
where $(s, m, l)$ correspond to the short, intermediate, and long principal axes of the triaxial ellipsoid with moments of inertia $\mathcal{J}_s, \mathcal{J}_m, \mathcal{J}_l$.

---

## Microscopic Single-$j$ Quadrupole Potential

In the single-$j$ shell approximation (such as $h_{11/2}$ in $^{135}\text{Pr}$ or $i_{13/2}$ in $^{163}\text{Lu}$), the deformed triaxial potential is parameterized by quadrupole deformation splitting $C$ and triaxiality angle $\gamma$:
$$H_{\text{sp}} = C \left[ \cos(\gamma) \cdot (3 j_l^2 - j(j+1)) - \sqrt{3}\sin(\gamma) \cdot (j_s^2 - j_m^2) \right]$$
- $\gamma = 0^\circ$: Prolate axially symmetric limit;
- $\gamma = 60^\circ$: Oblate axially symmetric limit;
- $\gamma \approx 20^\circ - 30^\circ$: Maximum triaxial deformation with intermediate-axis dominance ($\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$).

---

## Symmetrized $D_2$ Basis and Matrix Structure

In the coupled basis $|I M K j \Omega\rangle$:
Because atomic nuclei exhibit $D_2$ invariance under $\pi$-rotations about all three principal axes, the physical eigenstates are symmetrized:
$$|I M K j \Omega, \alpha\rangle = \frac{1}{\sqrt{2(1 + \delta_{K0}\delta_{\Omega0})}} \left[ |I M K j \Omega\rangle + (-1)^{I-j} |I M -K j -\Omega\rangle \right]$$
The Hamiltonian matrix couples states via four distinct interaction mechanisms:
1. **Diagonal Energy**:
   $$\langle H \rangle = \frac{(K - \Omega)^2}{2\mathcal{J}_l} + A_+ [I(I+1) - K^2 + j(j+1) - \Omega^2] + C\cos\gamma (3\Omega^2 - j(j+1))$$
   where $A_+ = \frac{1}{4}(1/\mathcal{J}_s + 1/\mathcal{J}_m)$;
2. **Coriolis Particle-Rotor Coupling ($\Delta K = \pm 1, \Delta\Omega = \pm 1$)**:
   $$-A_+ (I_+ j_- + I_- j_+) - A_- (I_+ j_+ + I_- j_-) \quad \left(A_- = \frac{1}{4}(1/\mathcal{J}_s - 1/\mathcal{J}_m)\right)$$
3. **Single-Particle Triaxial Asymmetry ($\Delta\Omega = \pm 2$)**:
   $$-\frac{\sqrt{3}}{2} C \sin\gamma \cdot (j_+^2 + j_-^2)$$
4. **Core Triaxial Asymmetry ($\Delta K = \pm 2$)**:
   $$\frac{1}{2} A_- \cdot (I_+^2 + I_-^2)$$

---

## Wobbling Hierarchy and Eigenvalue Properties

Exact algebraic diagonalization for each spin $I$ yields the complete physical spectrum:
- **Yrast Band ($n_w = 0$)**: Lowest eigenvalue $E_{\text{yrast}}(I)$;
- **One-Phonon Wobbling Band ($n_w = 1$)**: Second eigenvalue $E_{\text{wob1}}(I)$;
- **Two-Phonon Wobbling Band ($n_w = 2$)**: Third eigenvalue $E_{\text{wob2}}(I)$.

The microscopic wobbling frequency:
$$\hbar\omega_w(I) = E(I, n_w=1) - E_{\text{yrast}}(I)$$
and the anharmonic ratio:
$$R_{21} = \frac{E(I, n_w=2) - E_{\text{yrast}}(I)}{\hbar\omega_w(I)}$$
characterize whether the wobbling excitation behaves as an ideal harmonic oscillator ($R_{21} = 2.0$) or undergoes sub-harmonic softening ($R_{21} < 2.0$, observed in $^{163}\text{Lu}$).

---

## Canonical Experimental Benchmarks

1. **$^{135}\text{Pr}$ Transverse Wobbler ($h_{11/2}$ Proton, $\gamma = 26^\circ$)**:
   - Parameters: $\mathcal{J}_m = 26.0, \mathcal{J}_s = 15.0, \mathcal{J}_l = 6.0\ \hbar^2/\text{MeV}, C = 35.0\text{ keV}$;
   - PTRM diagonalization yields smooth wobbling frequency $\hbar\omega_w \approx 2.7 - 2.8\text{ keV}$ (scaled by core units) with stable single-particle alignment along the short axis.
2. **$^{163}\text{Lu}$ Triaxial Superdeformed Wobbler ($i_{13/2}$ Proton, $\gamma = 20^\circ$)**:
   - Parameters: $\mathcal{J}_m = 45.0, \mathcal{J}_s = 20.0, \mathcal{J}_l = 10.0\ \hbar^2/\text{MeV}, C = 50.0\text{ keV}$;
   - Accurately reproduces multi-phonon wobbling states $n_w = 0, 1, 2$.

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用


- **Meyer-ter-Vehn, J.**: *Rotational band-structures in transitional odd-A nuclei*, Nucl. Phys. A 249, 111–140 (1975).
- **Frauendorf, S. & Dönau, F.**: *Transverse wobbling of a triaxial nucleus*, Phys. Rev. C 89, 014322 (2014).
- **Hamamoto, I.**: *Wobbling excitations in odd-A nuclei with high-j aligned particles*, Phys. Rev. C 65, 044305 (2002).
- **Petrache, C. M. (ed.)**: *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025), Chapter 2 & Chapter 8.


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
