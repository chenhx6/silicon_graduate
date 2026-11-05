---
type: concept
title: "Gamma-vibrational band mixing, Mikhailov z_gamma parameter and Alaga rule corrections"
aliases: [gamma-band-mixing, mikhailov-z-gamma, alaga-rule-corrections, rotational-vibrational-coupling]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [collective-model, gamma-vibrations, alaga-rules, mikhailov-parameter, band-mixing, clebsch-gordan, gamma-softness, triaxiality]
---

# Gamma-vibrational band mixing, Mikhailov z_gamma parameter and Alaga rule corrections

## Definition

In deformed even-even nuclei, collective quadrupole vibrations of the nuclear shape include $\beta$-vibrations (axially symmetric oscillations along the symmetry axis, $K = 0_\beta$) and $\gamma$-vibrations (non-axial dynamic fluctuations perpendicular to the symmetry axis, $K = 2_\gamma$).

For electric quadrupole ($E2$) transitions from states $I_\gamma$ in the $\gamma$-vibrational band to states $I_g$ in the ground-state rotational band ($K=0$):
1. **Unperturbed Alaga Branching Rules (Alaga et al. 1955)**:
   In the adiabatic limit of decoupled rotation and vibration, the transition matrix element is proportional to the geometric Clebsch-Gordan coefficient:
   $$B(E2; I_\gamma \to I_g)_{\text{Alaga}} = B_0(E2) \cdot \langle I_\gamma 2 2 -2 \mid I_g 0 \rangle^2$$
   For the $2_\gamma^+$ bandhead de-exciting to $0_g^+$ and $2_g^+$:
   $$\frac{B(E2; 2_\gamma^+ \to 0_g^+)}{B(E2; 2_\gamma^+ \to 2_g^+)} = \frac{\langle 2 2 2 -2 \mid 0 0 \rangle^2}{\langle 2 2 2 -2 \mid 2 0 \rangle^2} = \frac{1/5}{2/7} = \frac{7}{10} = 0.700$$

2. **Mikhailov Band-Mixing Expansion (Mikhailov 1966; Bohr & Mottelson Vol. II §4-2)**:
   Coriolis coupling and the $\Delta K = 2$ non-axial quadrupole interaction mix the $\gamma$-vibrational band with the ground-state band, introducing an angular-momentum-dependent perturbation:
   $$M(E2; I_\gamma \to I_g) = M_0 \langle I_\gamma 2 2 -2 \mid I_g 0 \rangle \cdot \left[ 1 + z_\gamma [ I_g(I_g + 1) - I_\gamma(I_\gamma + 1) ] \right]$$
   where $z_\gamma$ is the dimensionless **Mikhailov band-mixing parameter**.

   For $2_\gamma^+ \to 0_g^+$ and $2_\gamma^+ \to 2_g^+$:
   - To $0_g^+$: $I_g(I_g+1) - I_\gamma(I_\gamma+1) = 0 - 6 = -6 \implies M(2_\gamma \to 0_g) \propto (1 - 6 z_\gamma)$;
   - To $2_g^+$: $I_g(I_g+1) - I_\gamma(I_\gamma+1) = 6 - 6 = 0 \implies M(2_\gamma \to 2_g) \propto 1$;
   - The perturbed branching ratio is:
     $$\frac{B(E2; 2_\gamma^+ \to 0_g^+)}{B(E2; 2_\gamma^+ \to 2_g^+)} = 0.700 \times [1 - 6 z_\gamma]^2$$

3. **Inversion of $z_\gamma$ and Rotational-Vibrational Coupling $h_2$**:
   From experimental branching ratios $R_{\text{exp}} = B(E2; 2_\gamma \to 0_g) / B(E2; 2_\gamma \to 2_g)$:
   $$z_\gamma = \frac{1 - \sqrt{R_{\text{exp}} / 0.700}}{6}$$
   The off-diagonal rotation-vibration coupling matrix element $h_2$ (in $\text{keV}$):
   $$h_2 = z_\gamma \cdot \frac{E(2_\gamma^+) - E(2_g^+)}{\sqrt{6}}$$

## Necessary Assumptions

1. **First-Order Perturbation Approximation**: The band-mixing parameter satisfies $z_\gamma \ll 1$ (weak mixing limit).
2. **Pure $E2$ Multipolarity**: The $2_\gamma^+ \to 2_g^+$ transition is assumed pure $E2$ (or corrected for the measured $M1$ mixing ratio $\delta(E2/M1)$).

## Discriminating Observables

1. **Suppression of the $0_g / 2_g$ Ratio**:
   In well-deformed rare earths, $R_{\text{exp}} \approx 0.50 - 0.55$, demonstrating a systematic $20\% - 30\%$ reduction below the Alaga value $0.700$, yielding $z_\gamma \approx 0.02 - 0.04$.
2. **Enhancement of the $4_g / 2_g$ Ratio**:
   The transition to $4_g^+$ has $I_g(I_g+1) - I_\gamma(I_\gamma+1) = +14$, predicting an enhancement by $(1 + 14 z_\gamma)^2 \approx 1.6 - 2.0\times$ above the Alaga value $0.050$.
3. **Model-screening branch**:
   When $z_\gamma > 0.060$ and $h_2 > 10\text{ keV}$, the first-order
   adiabatic rotor expansion indicates stronger band mixing under its stated
   assumptions. The same ratio can also reflect a rigid-triaxial rotor,
   configuration mixing, or branching/normalization effects.

## Supporting Evidence

1. **$^{168}\text{Er}$ Well-Deformed Prolate Rotor Benchmark**:
   - $E(2_\gamma^+) = 821.1\text{ keV}, E(2_g^+) = 79.8\text{ keV}$;
   - Experimental ratio: $R_{\text{exp}} = 0.540 \pm 0.025$ ($-22.86\%$ Alaga deviation);
   - Inverted parameter: $z_\gamma = 0.02028$;
   - Rotational-vibrational coupling: $h_2 = 6.14\text{ keV}$;
   - Predicted $B(E2; 2_\gamma \to 4_g) / B(E2; 2_\gamma \to 2_g) = 0.0824$ (vs unperturbed $0.0500$).
2. **$^{130}\text{Ba}$ Transitional $\gamma$-Soft Benchmark**:
   - $E(2_\gamma^+) = 908.1\text{ keV}, E(2_g^+) = 357.4\text{ keV}$;
   - Experimental ratio: $R_{\text{exp}} = 0.320$ ($-54.29\%$ Alaga deviation);
   - Inverted parameter: $z_\gamma = 0.05398$, $h_2 = 12.14\text{ keV}$; this
     is a conditional band-mixing estimate, not a direct measurement of the
     $\gamma$-softness of the $A \sim 130$ core.

## Counter-evidence and Competing Interpretations

1. **Rigid Triaxial Rotor (Davydov-Filippov Model) vs Mikhailov Mixing**:
   The Davydov-Filippov asymmetric rotor model treats the $2_\gamma^+$ state as the $K=2$ rotational excitation of a fixed triaxial shape ($\gamma \ne 0^\circ$), predicting branching ratios from diagonalizing the asymmetric rotor Hamiltonian. The Mikhailov expansion is mathematically equivalent to the small-$\gamma$ limit of the Davydov model.
2. **Interacting Boson Model (IBM) $O(6)$ Limit**:
   In the $\gamma$-unstable $O(6)$ dynamical symmetry, the selection rule $\Delta \sigma = 0, \Delta \tau = 1$ naturally reproduces the suppression of $2_\gamma \to 0_g$ relative to $2_\gamma \to 2_g$ without explicitly invoking Coriolis mixing.

## Our Current Position

In this wiki, $\gamma$-vibrational band mixing, Mikhailov $z_\gamma$
parameters, and Alaga branching-rule deviations are calculated using Module
112 (`gamma_band_mixing_z_gamma_alaga_inverter.py`, CLI subcommand `zgamma`).
The module inverts $z_\gamma$ and the coupling matrix element $h_2$ from
supplied branching ratios under a first-order pure-E2 contract; the output is a
conditional band-mixing diagnostic rather than a unique core-shape assignment.

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]: A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-2 (pp. 140–155).
- [[book-lu-nuclear-physics-chinese]]: 卢希庭, 江栋兴, 叶沿林, 《原子核物理（修订版）》, 原子能出版社 (2000), 第8章 §8.4.
- Alaga, G., Alder, K., Bohr, A., Mottelson, B. R., Mat. Fys. Medd. Dan. Vid. Selsk. 29, no. 9 (1955).
- Mikhailov, V. M., Bull. Acad. Sci. USSR, Phys. Ser. 30, 1392 (1966).
