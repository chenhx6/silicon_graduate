---
type: concept
title: "Schiffer-True universal two-body matrix elements (TBME), Pandya inversion and chiral bandhead coupling"
aliases: [schiffer-true-tbme, universal-tbme-theta12, pandya-inversion, chiral-bandhead-coupling, nordheim-rules]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [shell-model, two-body-matrix-elements, schiffer-true, pandya-transformation, chiral-bandheads, nordheim-rules, odd-odd-nuclei]
---

# Schiffer-True universal two-body matrix elements (TBME), Pandya inversion and chiral bandhead coupling

## Definition

In the nuclear shell model, the residual interaction between two valence nucleons outside a doubly magic core governs the energy multiplet spectra of two-particle and particle-hole configurations. For two nucleons in single-particle orbitals $j_1$ and $j_2$ coupled to total angular momentum $J$ ($|j_1 - j_2| \le J \le j_1 + j_2$):

1. **Semiclassical Angle $\theta_{12}$ Between Angular Momentum Vectors**:
   The angle $\theta_{12}$ between $\vec{j}_1$ and $\vec{j}_2$ in the coupled state $|(j_1 j_2) J\rangle$ is given by:
   $$\cos\theta_{12} = \frac{J(J+1) - j_1(j_1+1) - j_2(j_2+1)}{2 \sqrt{j_1(j_1+1) j_2(j_2+1)}}$$
   - $J = 0$ (for $j_1 = j_2$): $\cos\theta_{12} = -1.0 \implies \theta_{12} = 180^\circ$ (antiparallel alignment, maximum pairing overlap);
   - $J \approx \sqrt{2} j$: $\cos\theta_{12} \approx 0.0 \implies \theta_{12} \approx 90^\circ$ (perpendicular coupling);
   - $J = J_{\text{max}} = j_1 + j_2$: $\cos\theta_{12} \to +1.0 \implies \theta_{12} \to 0^\circ$ (coplanar parallel alignment).

2. **Schiffer-True Universal Empirical Curve (Schiffer & True 1976)**:
   John P. Schiffer and W. W. True (Rev. Mod. Phys. 48, 191, 1976) discovered that when plotted against the semiclassical angle $\theta_{12}$, experimental two-body matrix elements (TBMEs) $V(J) = \langle j_1 j_2 J | V | j_1 j_2 J \rangle$ across the entire nuclear chart collapse onto a single universal curve:
   $$V_{\text{pp}}(\theta_{12}) = v_{\text{pair}} \cdot \delta_{J, 0} + v_1 \cos\theta_{12} + v_2 P_2(\cos\theta_{12})$$
   - Deep attractive pairing well at $\theta_{12} = 180^\circ$ ($J = 0^+$): $V_0 \approx -2.0\text{ to } -3.5\text{ MeV}$;
   - Secondary attractive minimum at $\theta_{12} \to 0^\circ$ ($J = J_{\text{max}}$);
   - Weak or repulsive interaction at intermediate angles $\theta_{12} \approx 90^\circ$.

3. **Pandya Transformation for Particle-Hole Multiplets**:
   In odd-odd nuclei with a valence particle $j_1$ and a valence hole $j_2^{-1}$ (such as chiral nuclei $^{134}\text{Pr}, ^{128}\text{Cs}$ with configuration $\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$), the particle-hole matrix elements are related to particle-particle matrix elements by the exact Pandya transformation (Pandya 1956; Bohr & Mottelson Vol. I §3-4):
   $$V_{\text{ph}}(J) = - \sum_{J'} (2J' + 1) \left\{ \begin{matrix} j_1 & j_2 & J \\ j_1 & j_2 & J' \end{matrix} \right\} V_{\text{pp}}(J')$$
   The Pandya transformation inverts the multiplet spectrum: the deep $J=0^+$ pairing minimum is removed, and the lowest energy states are shifted to $J = |j_1 - j_2|$ and $J = j_1 + j_2$ (the aligned chiral bandhead!).

4. **Nordheim Coupling Rules for Odd-Odd Bandheads**:
   The Nordheim number $\mathcal{N} = (j_p - \ell_p) + (j_n - \ell_n)$:
   - **Strong Rule** ($\mathcal{N} = 0$): Proton and neutron have opposite spin-orbit couplings ($j_p = \ell_p \pm 1/2, j_n = \ell_n \mp 1/2$) $\implies$ Ground state favors antiparallel alignment:
     $$J_{\text{fav}} = |j_p - j_n|$$
   - **Weak Rule** ($\mathcal{N} = \pm 1$): Both nucleons have parallel spin-orbit couplings ($j = \ell + 1/2$ for both, e.g. $\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$) $\implies$ Favors maximum alignment or intermediate coupling:
     $$J_{\text{fav}} \approx j_p + j_n$$
   In $^{134}\text{Pr}$, $\mathcal{N} = +1$, which favors the high-spin aligned chiral bandhead $I_0 = 10^+ / 11^+$.

## Necessary Assumptions

1. **Weak Core Polarization**: The inert core contributes a smooth mass-dependent renormalization to the two-body interaction, without inducing severe shape coexistence or non-spherical deformation in the two-particle state.
2. **Phase Consistency in Pandya Recoupling**: Wigner $6j$ symbols follow the standard Condon-Shortley phase convention.

## Discriminating Observables

1. **U-Shaped Semiclassical $\theta_{12}$ Plot**:
   Plotting $V_{\text{pp}}(J)$ versus $\theta_{12}$ reveals the universal two-body curve, validating short-range nuclear force characteristics.
2. **Particle-Hole Inversion**:
   Inverting from $(h_{11/2}^2)$ in $^{134}\text{Te}$ to $(\pi h_{11/2} \nu h_{11/2}^{-1})$ in $^{134}\text{Pr}$ shifts the lowest state from $0^+$ to the high-spin aligned state.
3. **Nordheim Number Diagnostic**:
   Calculates $\mathcal{N}$ directly from single-particle spectroscopic assignments to predict odd-odd ground-state and isomer spins.

## Supporting Evidence

1. **$^{134}\text{Te}$ $(h_{11/2}^2)$ Particle-Particle Multiplet ($j_1=5.5, j_2=5.5$)**:
   - $J=0^+$ has $\theta_{12} = 180.0^\circ, V_{\text{pp}} = -3.70\text{ MeV}$ (deepest pairing minimum);
   - $J=2^+$ has $\theta_{12} = 156.4^\circ, V_{\text{pp}} = -1.27\text{ MeV}$;
   - $J=8^+$ has $\theta_{12} = 89.6^\circ, V_{\text{pp}} = +0.33\text{ MeV}$ (repulsive at $90^\circ$);
   - $J=10^+$ has $\theta_{12} = 57.4^\circ, V_{\text{pp}} = +0.50\text{ MeV}$.
2. **$^{134}\text{Pr}$ $\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$ Pandya Inversion**:
   - Pandya transformation inverts the spectrum: $J=0^+$ shifts from $-3.70\text{ MeV}$ to $-0.30\text{ MeV}$;
   - $J=2^+$ state is bound at $-1.10\text{ MeV}$, and high-spin aligned states form the chiral bandhead.
3. **Nordheim Rule for $^{134}\text{Pr}$**:
   - $\pi h_{11/2}$ ($\ell=5, j=11/2 \implies j-\ell = +1/2$), $\nu h_{11/2}^{-1}$ ($\ell=5, j=11/2 \implies j-\ell = +1/2$);
   - $\mathcal{N} = +1$ (Weak rule), predicting favored spin $J \sim j_p + j_n = 11^+$, matching the experimental chiral doublet bandhead at $I_0 = 10^+ / 11^+$.

## Counter-evidence and Competing Interpretations

1. **Triaxial Mean Field Deformation vs Spherical Shell Model**:
   In strongly deformed odd-odd nuclei, the spherical shell model basis is replaced by Nilsson orbitals $[N n_z \Lambda \Omega]$ and the Gallagher-Moszkowski (GM) coupling rules for $\Omega_p \pm \Omega_n$. Semiclassical $\theta_{12}$ parameterization applies in the spherical-to-transitional regime before stable axial or triaxial deformation sets in.
2. **Core Polarizability and Tensor Force**:
   Detailed fine structure within the $v=2$ multiplet ($J=2, 4, 6$) requires small tensor force and quadrupole-quadrupole core polarization corrections beyond the simple three-parameter Schiffer curve.

## Our Current Position

In this wiki, two-body matrix elements, semiclassical $\theta_{12}$ angle parameterizations, particle-hole Pandya inversions, and Nordheim odd-odd coupling rules are calculated using Module 110 (`schiffer_true_two_body_matrix_elements_calculator.py`, CLI subcommand `schiffer`). The module provides the microscopic shell-model foundation for understanding the formation of chiral doublet bandheads in odd-odd nuclei.

## Sources

- [[book-bohr-mottelson-nuclear-structure]]: A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. I, §3-4 (pp. 314–332).
- Schiffer, J. P., True, W. W., *The effective interaction between nucleons deduced from nuclear spectra*, Rev. Mod. Phys. 48, 191 (1976).
- Pandya, S. P., *Particle-hole transformation in nuclear shell model*, Phys. Rev. 103, 956 (1956).
- Nordheim, L. W., *Nuclear shell structure and beta-decay. II*, Phys. Rev. 78, 294 (1950).
