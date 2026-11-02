---
type: concept
title: "Heavy-ion fusion Wong barrier penetration, initial spin distribution and evaporation channel design"
aliases: [heavy-ion-fusion-wong, wong-barrier-penetration, fusion-spin-distribution, xn-channel-design]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [heavy-ion-reactions, fusion-cross-section, wong-formula, spin-distribution, hill-wheeler, rldm-fission, evaporation-residues, experimental-design]
---

# Heavy-ion fusion Wong barrier penetration, initial spin distribution and evaporation channel design

## Definition

In low-energy experimental nuclear structure, heavy-ion fusion-evaporation reactions ($A_p \ge 10$) are the primary mechanism for populating high-spin collective states, triaxial wobblers, and chiral doublet bands. The reaction proceeds through two distinct dynamical phases:

1. **Entrance Channel Fusion & Wong Barrier Penetration**:
   Projectile $(Z_p, A_p)$ collides with target $(Z_t, A_t)$ at laboratory energy $E_{\text{lab}}$, with center-of-mass energy $E_{\text{cm}} = E_{\text{lab}} A_t / (A_p + A_t)$ and reduced mass $\mu$. The interaction potential forms an effective barrier $V_B(\ell) = V_{B0} + \frac{\hbar^2 \ell(\ell+1)}{2\mu R_B^2}$.
   Using the Hill-Wheeler parabolic barrier transmission coefficient:
   $$T_\ell(E_{\text{cm}}) = \frac{1}{1 + \exp\left[ \frac{2\pi}{\hbar\omega_0} (V_B(\ell) - E_{\text{cm}}) \right]}$$
   the compound nucleus initial spin distribution is given by:
   $$\sigma_\ell(E_{\text{cm}}) = \frac{\pi}{k^2} (2\ell + 1) T_\ell(E_{\text{cm}})$$
   Integrating over continuous angular momentum $\ell$ yields Wong's celebrated closed analytical formula (Wong 1973; 林承键 2017 第 6 章):
   $$\sigma_{\text{fus}}^{\text{Wong}}(E_{\text{cm}}) = \frac{R_B^2 \hbar\omega_0}{2 E_{\text{cm}}} \ln\left[ 1 + \exp\left( \frac{2\pi}{\hbar\omega_0} (E_{\text{cm}} - V_{B0}) \right) \right]$$
   The discrete partial wave summation $\sum_\ell \sigma_\ell$ converges exactly to Wong's formula to within $< 0.05\%$.

2. **Rotating Liquid Drop Fission Limit (RLDM)**:
   Centrifugal rotation reduces the fission barrier $B_f(\ell)$. According to the Cohen-Plasil-Swiatecki (1974) model, at the limiting angular momentum $\ell_{\text{fiss}}$ (typically $65 - 75\ \hbar$ in $A \sim 130 - 150$), $B_f(\ell_{\text{fiss}}) \to 0$. Partial waves with $\ell > \ell_{\text{fiss}}$ undergo fast fission or deep inelastic scattering, while only partial waves with $\ell \le \ell_{\text{fiss}}$ survive to form Evaporation Residues (ER):
   $$\sigma_{\text{ER}} = \sum_{\ell=0}^{\min(\ell_{\text{crit}}, \ell_{\text{fiss}})} \sigma_\ell(E_{\text{cm}})$$

3. **$xn$ Statistical Evaporation Channel Window**:
   The compound nucleus de-excites via neutron cascade. Because each evaporated neutron removes binding energy $S_n \approx 8\text{ MeV}$ plus thermal kinetic energy $2 T \approx 2.5\text{ MeV}$, the optimum excitation energy to populate the $xn$ channel is:
   $$E_{\text{opt}}^*(xn) \approx x \cdot (S_n + 2T) \approx x \cdot 10.5\text{ MeV} - 2.0\text{ MeV}$$
   This determines the optimal recommended beam energy $E_{\text{lab}}^{\text{opt}}(xn)$ to maximize the cross section for the desired residue.

## Necessary Assumptions

1. **Parabolic Barrier Approximation**: The nuclear-plus-Coulomb barrier top is approximated by an inverted harmonic oscillator with curvature $\hbar\omega_0 \approx 3.5 - 5.0\text{ MeV}$. (For massive systems with large charge product $Z_p Z_t > 1600$, dynamical quasi-fission hinders complete fusion).
2. **Sharp Fission Angular Momentum Cutoff**: Partial waves above $\ell_{\text{fiss}}$ decay exclusively by binary fission without emitting discrete in-beam $\gamma$ cascades.
3. **Compound Nucleus Statistical Equilibration**: Entrance channel memory is lost, and decay depends only on excitation energy $E^*$ and angular momentum $\ell$.

## Discriminating Observables

1. **Fusion Excitation Function Shape**:
   At $E_{\text{cm}} \gg V_{B0}$, $\sigma_{\text{fus}}$ asymptotically approaches the geometrical cross section $\pi R_B^2 (1 - V_{B0}/E_{\text{cm}})$. At sub-barrier energies ($E_{\text{cm}} < V_{B0}$), $\sigma_{\text{fus}}$ exhibits an exponential falloff governed by quantum tunneling.
2. **Initial Spin Distribution $P(\ell)$**:
   The triangular distribution $P(\ell) \propto (2\ell+1) T_\ell$ rises linearly with $\ell$ and drops sharply near the critical angular momentum $\ell_{\text{crit}}$ where $T_\ell = 0.5$.
3. **$xn$ Residue Population Optimization**:
   Tuning $E_{\text{lab}}$ aligns $E^*(CN)$ with the peak of the $xn$ excitation function, suppressing competing $(x-1)n$ and $(x+1)n$ contaminants in $\gamma-\gamma$ coincidence matrices.

## Supporting Evidence

1. **$^{16}\text{O} + {}^{122}\text{Sn} \to {}^{138}\text{Ce}^* \to {}^{134}\text{Ce} + 4n$ Triaxial Core Benchmark**:
   - $E_{\text{lab}} = 80.0\text{ MeV} \implies E_{\text{cm}} = 70.72\text{ MeV}$, $V_{B0} = 50.56\text{ MeV}$, $R_B = 10.72\text{ fm}$.
   - Wong analytical cross section: $\sigma_{\text{fus}} = 1030.0\text{ mb}$.
   - Partial wave summation: $\sigma_{\text{sum}} = 1030.2\text{ mb}$ (Agreement: $99.98\%$).
   - Critical angular momentum: $\ell_{\text{crit}} = 40\ \hbar$, mean spin $\langle \ell \rangle = 25.9\ \hbar$.
   - Recommended beam energy for $4n$ channel ($^{134}\text{Ce}$): $E_{\text{lab}} \approx 48.6\text{ MeV}$; at $80\text{ MeV}$, $E^* = 67.8\text{ MeV}$ preferentially drives $5n/6n$ evaporation.
2. **$^{10}\text{B} + {}^{128}\text{Te} \to {}^{138}\text{La}^* \to {}^{134}\text{La} + 4n$ Chiral Odd-Odd Benchmark**:
   - $E_{\text{lab}} = 55.0\text{ MeV} \implies E_{\text{cm}} = 51.01\text{ MeV}$, barrier $V_{B0} = 34.6\text{ MeV}$.
   - Populates intermediate-spin chiral candidates with high survival against fission.

## Counter-evidence and Competing Interpretations

1. **Sub-Barrier Fusion Enhancement & Coupled Channels**:
   Experimental fusion cross sections for deformed nuclei (e.g. $^{154}\text{Sm}$) below the barrier exceed simple 1D Wong formula predictions by several orders of magnitude. As discussed in Lin Chengjian Ch. 6, this enhancement originates from coupling to low-lying collective quadrupole ($\beta_2$) and octupole ($\beta_3$) surface vibrations and transfer channels, forming a distribution of fusion barriers rather than a single fixed barrier.
2. **Quasi-Fission in Superheavy Reactions**:
   In very heavy projectile-target combinations (e.g. $^{48}\text{Ca} + {}^{238}\text{U}$), re-separation before reaching a compact compound nucleus (quasi-fission) drastically suppresses the true fusion probability.

## Our Current Position

In this wiki, heavy-ion fusion reactions, entrance barrier penetrations, compound nucleus initial spin distributions, and $xn$ residue channel optimizations are calculated using Module 99 (`heavy_ion_fusion_spin_distribution_wong_calculator.py`, CLI subcommand `wong`). The module validates Wong's analytical solution against discrete partial wave summation and integrates RLDM fission boundaries to guide realistic in-beam experiment proposals.

## Sources

- [[book-lin-heavy-ion-reactions]]: 林承键, 《重离子核反应》, 科学出版社 (2017), 第6章 近垒重离子熔合反应, 印刷 pp. 134–153 / PDF pp. 144–163.
- [[book-bertulani-nuclear-reactions]]: C. A. Bertulani and P. Danielewicz, *Introduction to Nuclear Reactions*, CRC Press (2021), Ch. 5 (Fusion and Fission, pp. 175–195).
- Wong, C. Y., *Barrier penetration of projectile-target interaction in heavy-ion collisions*, Phys. Rev. Lett. 31, 766 (1973).
- Cohen, S., Plasil, F., Swiatecki, W. J., *Equilibrium configurations of rotating charged or gravitating masses with surface tension. II*, Ann. Phys. 82, 557 (1974).
