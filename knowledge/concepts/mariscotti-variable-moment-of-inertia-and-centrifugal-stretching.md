---
type: concept
title: "Mariscotti variable moment of inertia (VMI) model and dynamic centrifugal stretching"
aliases: [mariscotti-vmi-model, variable-moment-of-inertia, centrifugal-stretching, r42-casten-triangle]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [nuclear-structure, rotational-bands, vmi-model, moment-of-inertia, centrifugal-stretching, transitional-nuclei, casten-triangle]
---

# Mariscotti variable moment of inertia (VMI) model and dynamic centrifugal stretching

## Definition

In transitional and deformed even-even nuclei, ground-state rotational bands systematically deviate from the rigid rotor $I(I+1)$ rule due to Coriolis pair-breaking and centrifugal stretching of the nuclear surface. The **Variable Moment of Inertia (VMI) Model** (Mariscotti, Scharff-Goldhaber, Kirk 1969; 卢希庭 2000 第 8 章 §8.5; Bohr & Mottelson Vol. II §4-2) models this dynamic response by parameterizing the total energy as a sum of kinetic rotation and harmonic potential stretching:
$$E(I) = \frac{I(I+1)}{2\mathcal{J}(I)} + \frac{1}{2} C (\mathcal{J}(I) - \mathcal{J}_0)^2$$
where:
- $\mathcal{J}_0$ is the ground-state moment of inertia ($\hbar^2/\text{MeV}$);
- $C$ is the restoring force constant (core rigidity / hardness parameter, $\text{MeV} / (\hbar^2/\text{MeV})^2$);
- $\mathcal{J}(I)$ is the equilibrium moment of inertia at angular momentum $I$.

The equilibrium condition $\frac{\partial E}{\partial \mathcal{J}} = 0$ yields the fundamental cubic equation:
$$\mathcal{J}(I)^3 - \mathcal{J}_0 \mathcal{J}(I)^2 = \frac{I(I+1)}{2C}$$
Using Cardano's algebraic method, the depressed cubic equation $y^3 + p y + q = 0$ (with $y = \mathcal{J} - \mathcal{J}_0/3, p = -\mathcal{J}_0^2/3, q = -2\mathcal{J}_0^3/27 - \frac{I(I+1)}{2C}$) provides an exact analytical solution for $\mathcal{J}(I)$ at every spin $I$.

## Necessary Assumptions

1. **Adiabatic Centrifugal Stretching**: Collective rotation is slow compared to intrinsic single-particle transitions, allowing the nuclear shape to adjust adiabatically to the centrifugal force.
2. **Harmonic Restoring Potential**: Deviations of the moment of inertia from the ground state $\mathcal{J}_0$ are resisted by a linear restoring stress $\propto C (\mathcal{J} - \mathcal{J}_0)$.
3. **Absence of Band Crossing (Backbending)**: The VMI description applies prior to the alignment of high-$j$ quasiparticle pairs (such as $i_{13/2}$ neutrons or $h_{11/2}$ protons), where alignment induces sharp discontinuities in the moment of inertia.

## Discriminating Observables

1. **Evolution of Dynamic Moment of Inertia $\mathcal{J}(I)$**:
   In transitional nuclei (e.g. $^{120}\text{Xe}, ^{112}\text{Ru}$), $\mathcal{J}(I)$ expands by $50\% - 100\%$ as spin increases from $2^+$ to $10^+$, directly quantifying centrifugal stretching.
2. **Energy Ratio $R_{4/2} = E(4_1^+) / E(2_1^+)$ Classification**:
   - $R_{4/2} \to 3.333$: Rigid axially symmetric rotor ($C \to \infty, \mathcal{J}(I) = \mathcal{J}_0$);
   - $2.90 \le R_{4/2} \le 3.29$: Deformed / centrifugally stretched rotor (VMI domain);
   - $2.25 \le R_{4/2} < 2.90$: Transitional / $\gamma$-soft core (O(6) dynamical symmetry / triaxial);
   - $R_{4/2} \to 2.000$: Harmonic spherical vibrator ($\mathcal{J}_0 \to 0$);
   - $R_{4/2} < 2.000$: Sub-vibrational (negative $\mathcal{J}_0$, indicating particle-hole intruder mixing).
3. **Stretching Energy Fraction**:
   The potential energy fraction $E_{\text{pot}} / E_{\text{total}} = \frac{0.5 C (\mathcal{J}-\mathcal{J}_0)^2}{E(I)}$ increases with spin, reaching $10\% - 25\%$ at high spins in soft cores.

## Supporting Evidence

1. **Well-Deformed Rotor $^{168}\text{Er}$ Benchmark**:
   - Experimental levels: $E(2^+)=79.8, E(4^+)=264.1, E(6^+)=548.7, E(8^+)=912.0, E(10^+)=1344.0, E(12^+)=1833.2\text{ keV}$.
   - VMI inversion yields $\mathcal{J}_0 = 35.805\ \hbar^2/\text{MeV}, C = 0.00280\ \text{MeV}^3$.
   - $R_{4/2} = 3.2565$; RMS fit residual is only $3.45\text{ keV}$ across all six levels.
2. **Triaxial Wobbler Core $^{112}\text{Ru}$ Benchmark (Frauendorf 2025 Ch. 2, p. 50)**:
   - Experimental levels: $E(2^+)=237.2, E(4^+)=678.8, E(6^+)=1279.0, E(8^+)=1999.0, E(10^+)=2780.0\text{ keV}$.
   - VMI inversion yields $\mathcal{J}_0 = 11.516\ \hbar^2/\text{MeV}, C = 0.00644\ \text{MeV}^3$, RMS residual $6.24\text{ keV}$.
   - Moment of inertia stretches dynamically from $\mathcal{J}(2^+) = 13.92$ to $\mathcal{J}(10^+) = 25.09\ \hbar^2/\text{MeV}$ ($80\%$ increase), confirming Frauendorf's note that dynamic VMI stretching is decisive for describing wobbling bandhead energies in Ru isotopes.
3. **Transitional $A \sim 130$ Nucleus $^{120}\text{Xe}$**:
   - $R_{4/2} = 2.47$, successfully modeled by soft core stiffness parameter $C$.

## Counter-evidence and Competing Interpretations

1. **Backbending Breakdown**:
   At spin $I \approx 12 - 16\ \hbar$ in rare earths or $I \approx 10 - 14\ \hbar$ in $A \sim 130$, the Coriolis force breaks a high-$j$ pair, causing an abrupt jump in the moment of inertia and backbending. Because VMI assumes smooth potential stretching, it cannot describe states beyond the band-crossing frequency $\hbar\omega_c$.
2. **Microscopic Cranking and QRPA vs Phenomelogical VMI**:
   While VMI provides an economical two-parameter description of the ground band, it is a phenomenological macro-model. Microscopic self-consistent cranking (CSM) or constrained triaxial RMF calculations are required to derive $\mathcal{J}_0$ and $C$ from effective nucleon-nucleon interactions.

## Our Current Position

In this wiki, ground-state rotational bands and centrifugal stretching across the Casten triangle are analyzed using Module 101 (`mariscotti_vmi_rotational_stretching_calculator.py`, CLI subcommand `vmi`). The engine analytically solves Cardano's cubic equation, computes dynamic $\mathcal{J}(I)$ stretching, and performs least-squares inversion of $(\mathcal{J}_0, C)$ from experimental levels.

## Sources

- [[book-lu-nuclear-physics-chinese]]: 卢希庭, 江栋兴, 叶沿林, 《原子核物理（修订版）》, 原子能出版社 (2000), 第8章 核结构模型 §8.5 (VMI模型, 印刷 pp. 212–215 / PDF pp. 222–225).
- [[book-bohr-mottelson-nuclear-structure-vol2]]: A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-2 (pp. 31–38).
- Mariscotti, M. A. J., Scharff-Goldhaber, G., Kirk, B., *Phenomenological analysis of ground-state bands in even-even nuclei*, Phys. Rev. 178, 1864 (1969).
- [[book-petrache-chirality-and-wobbling]]: S. Frauendorf, in *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025), Ch. 2, p. 50 (VMI in $^{112}\text{Ru}$).
