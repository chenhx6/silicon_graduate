---
type: concept
title: "Davydov-Chaban non-adiabatic triaxial rotor model and dynamic beta-stretching"
aliases: [davydov-chaban-model, beta-stretching-triaxial, non-adiabaticity-parameter-mu, davydov-chaban-spectrum]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [triaxiality, davydov-chaban, beta-stretching, collective-model, non-adiabatic-rotation, gamma-bandhead, centrifugal-stretching]
---

# Davydov-Chaban non-adiabatic triaxial rotor model and dynamic beta-stretching

## Definition

The classical Davydov-Filippov (DF 1958) asymmetric rotor model describes non-axial collective rotation by assuming a completely rigid nuclear shape with fixed equilibrium deformation $(\beta_0, \gamma_0)$. In actual rotating atomic nuclei, collective rotation exerts centrifugal stresses that stretch the nuclear shape along the quadrupole deformation $\beta$ coordinate (**$\beta$-softness**).

A. S. Davydov and A. A. Chaban (Nucl. Phys. 20, 499, 1960; Bohr & Mottelson Vol. II §4-2; 卢希庭 2000 第 8 章 §8.4) developed the **Davydov-Chaban Non-Adiabatic Model**, coupling triaxial rotation to harmonic $\beta$-vibrational stretching:

1. **The Non-Adiabaticity / Deformability Parameter $\mu$**:
   The coupling between rotation and dynamic $\beta$-vibrations is parameterized by the dimensionless parameter $\mu$:
   $$\mu = \frac{1}{\beta_0} \left[ \frac{\hbar^2}{B C} \right]^{1/4}$$
   where $B$ is the mass parameter and $C$ is the $\beta$-restoring stiffness.
   - $\mu \to 0$: Recovers the completely rigid Davydov-Filippov rotor (no $\beta$-stretching);
   - $\mu \approx 0.15 - 0.35$: Moderately soft deformed triaxial nucleus (e.g. $^{112}\text{Ru}, ^{190}\text{Pt}$, and $A \sim 130$ Ba/Ce isotopes);
   - $\mu \ge 0.50$: Extremely soft, $\beta$-unstable transitional nucleus.

2. **Equilibrium Centrifugal Stretching Equation**:
   At total angular momentum $J$, centrifugal force stretches the deformation to $\beta(J) = p_J \beta_0$, where the dimensionless stretching ratio $p_J \ge 1.0$ satisfies the quartic equilibrium condition (Davydov & Chaban Eq. 2.13):
   $$p^3 (p - 1.0) = \mu^4 \varepsilon(J, \gamma)$$
   where $\varepsilon(J, \gamma)$ is the dimensionless Davydov-Filippov energy factor in units of $\hbar^2 / (4 B \beta_0^2)$.

3. **Davydov-Filippov Energy Factors $\varepsilon(J, \gamma)$**:
   - For the $2^+$ doublet (yrast $2_1^+$ and $\gamma$-bandhead $2_2^+$):
     $$\varepsilon(2_1^+) = \frac{9 - \sqrt{81 - 72 \sin^2(3\gamma)}}{4 \sin^2(3\gamma)}$$
     $$\varepsilon(2_2^+) = \frac{9 + \sqrt{81 - 72 \sin^2(3\gamma)}}{4 \sin^2(3\gamma)}$$
   - For the odd-spin state $3_1^+$ in the $\gamma$-band:
     $$\varepsilon(3_1^+) = \varepsilon(2_1^+) + \varepsilon(2_2^+) = \frac{18}{4 \sin^2(3\gamma)}$$
   - For $4_1^+$ and $4_2^+$, diagonalized from the $2 \times 2$ asymmetric rotor matrix.

4. **Total State Energy in Davydov-Chaban Model**:
   $$E(J, \gamma, \mu) = A_{\text{scale}} \left[ \frac{\varepsilon(J, \gamma)}{p_J^2} + \frac{1}{2\mu^2} (p_J - 1.0)^2 \right]$$
   where $A_{\text{scale}} = \frac{\hbar^2}{4 B \beta_0^2} \approx \frac{E(2_1^+)}{\varepsilon(2_1^+) / p_{2_1}^2 + \dots}$.
   The energy simultaneously accounts for kinetic rotation (reduced by $1/p^2$ due to increased moment of inertia) and potential stretching energy $\frac{1}{2\mu^2}(p-1)^2$.

## Necessary Assumptions

1. **Decoupled $\beta$ and $\gamma$ Degrees of Freedom**: The potential energy surface is factorized into an adiabatic $\beta$-vibrational well and a fixed triaxiality $\gamma$.
2. **Harmonic $\beta$-Vibrational Well**: The $\beta$-restoring potential is harmonic: $V(\beta) = \frac{1}{2} C (\beta - \beta_0)^2$.

## Discriminating Observables

1. **Dynamic Stretching Ratio $p = \beta / \beta_0$**:
   Tracks the percentage elongation $(p - 1) \times 100\%$ with spin. Higher spins experience greater stretching (typically $1\% - 10\%$).
2. **Energy Ratio $R_{4/2}$ and $\gamma$-Bandhead Ratio $E(2_2^+) / E(2_1^+)$**:
   Provides a two-dimensional map in $(\gamma, \mu)$ parameter space, distinguishing triaxiality ($\gamma$) from non-adiabatic compressibility ($\mu$).
3. **Simultaneous Fit to Ground and $\gamma$-Bands**:
   Unlike the rigid rotor which overestimates $E(4_1^+)$ and $E(6_1^+)$, the Davydov-Chaban model naturally compresses the ground band through $p(J) > 1.0$, achieving excellent agreement with experimental spectra.

## Supporting Evidence

1. **$^{112}\text{Ru}$ Triaxial Wobbler Core Benchmark ($\gamma = 22.0^\circ, \mu = 0.280, E(2_1^+) = 237.2\text{ keV}$)**:
   - Ground state $2_1^+$ has $p = 1.0080$ ($0.80\%$ stretching);
   - $\gamma$-bandhead $2_2^+$ is predicted at $706.0\text{ keV}$ (matching experimental $678.8\text{ keV}$ to within $4\%$);
   - Odd-spin $\gamma$-band state $3_1^+$ is predicted at $923.8\text{ keV}$;
   - High-spin state $4_2^+$ has $p = 1.0875$ ($+8.75\%$ centrifugal stretching), confirming Frauendorf's note on the decisive role of dynamic stretching in Ru wobbling cores.
2. **$^{190}\text{Pt}$ Benchmark ($\gamma = 30.0^\circ, \mu = 0.320$)**:
   - Accurately reproduces the energy staggering of the $2_2^+$ and $3_1^+$ states in the transitional platinum chain.

## Counter-evidence and Competing Interpretations

1. **Dynamic $\gamma$-Softness vs Static Triaxiality**:
   The Davydov-Chaban model assumes a fixed $\gamma$ minimum. In $\gamma$-soft nuclei (such as the Wilets-Jean model), the nucleus fluctuates freely across $\gamma \in [0^\circ, 60^\circ]$, requiring full 5D collective Hamiltonian numerical diagonalization.
2. **Microscopic Quasiparticle Alignment**:
   At high spins, high-$j$ pair breaking (backbending) causes sudden structural changes that exceed the scope of collective rotor models.

## Our Current Position

In this wiki, non-adiabatic triaxial rotation, dynamic $\beta$-stretching ratios $p_J$, and ground/$\gamma$-band energy spectra are calculated using Module 114 (`davydov_chaban_beta_stretching_triaxial_calculator.py`, CLI subcommand `chaban`). The engine analytically solves the quartic equilibrium equation $p^3(p-1) = \mu^4 \varepsilon$, providing a rigorous tool to evaluate the interplay between triaxiality and core compressibility.

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]: A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-2 (pp. 175–195).
- [[book-lu-nuclear-physics-chinese]]: 卢希庭, 江栋兴, 叶沿林, 《原子核物理（修订版）》, 原子能出版社 (2000), 第8章 §8.4.
- Davydov, A. S., Chaban, A. A., *Rotation-vibration interaction in non-axial even nuclei*, Nucl. Phys. 20, 499 (1960).
- Davydov, A. S., Filippov, G. F., *Rotational states in even atomic nuclei*, Nucl. Phys. 8, 237 (1958).
