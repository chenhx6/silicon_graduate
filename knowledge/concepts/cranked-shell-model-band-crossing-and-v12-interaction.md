---
type: concept
title: "Cranked shell model band crossing, avoided crossing Routhians and V12 interaction strength"
aliases: [csm-band-crossing, v12-interaction-strength, avoided-crossing-routhians, backbending-vs-upbending]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [cranked-shell-model, band-crossing, routhians, backbending, upbending, v12-interaction, pair-alignment, high-spin]
---

# Cranked shell model band crossing, avoided crossing Routhians and V12 interaction strength

## Definition

In high-spin nuclear spectroscopy, when deformed nuclei are spun up to rotational frequencies $\hbar\omega \ge 0.25\text{ MeV}$, the Coriolis force $-\vec{\omega} \cdot \vec{j}$ acts with opposite signs on time-reversed paired nucleons in high-$j$ intruder orbitals ($i_{13/2}$ neutrons in rare earths, $h_{11/2}$ protons/neutrons in $A \sim 130$). The Coriolis force breaks the pair, aligning their angular momenta along the rotational axis and inducing a crossing between the ground-state band and the aligned two-quasiparticle band.

In the Cranked Shell Model (CSM; Bengtsson & Frauendorf 1979; Bohr & Mottelson Vol. II §4-3):

1. **Rotating Frame Routhians**:
   At rotational frequency $\omega = dE / dI_x \approx [E(I+1) - E(I-1)] / [I_x(I+1) - I_x(I-1)]$, the energy in the rotating intrinsic frame is the Routhian:
   $$e'(\omega) = E(I) - \omega I_x(I)$$
   Subtracting the Harris two-parameter reference core $I_x^{\text{ref}}(\omega) = \mathcal{J}_0 \omega + \frac{1}{3} \mathcal{J}_1 \omega^3$ yields the quasiparticle alignment:
   $$i_x(\omega) = - \frac{de'}{d\omega} = I_x(\omega) - I_x^{\text{ref}}(\omega)$$

2. **The Two-Band Crossing Model**:
   At crossing frequency $\omega_c$, the unperturbed (diabatic) ground band ($|1\rangle$, alignment $i_1 \approx 0$) intersects the aligned Stockholm band ($|2\rangle$, alignment $i_2 \approx 8 - 12\ \hbar$):
   $$e_1'(\omega) = -\frac{1}{2}\mathcal{J}_0 \omega^2 - \frac{1}{4}\mathcal{J}_1 \omega^4$$
   $$e_2'(\omega) = e_{20}' - i_2 \omega - \frac{1}{2}\mathcal{J}_0 \omega^2$$
   The crossing frequency condition $e_1'(\omega_c) = e_2'(\omega_c)$ defines the bandhead of the aligned configuration.

3. **Avoided Crossing and Interaction Matrix Element $|V_{12}|$**:
   The residual two-body interaction couples the two diabatic configurations via Hamiltonian matrix:
   $$\mathcal{H}_{\text{CSM}} = \begin{pmatrix} e_1'(\omega) & V_{12} \\ V_{12} & e_2'(\omega) \end{pmatrix}$$
   The physical adiabatic Routhians (eigenvalues) exhibit an **avoided crossing**:
   $$e_{\pm}'(\omega) = \frac{e_1' + e_2'}{2} \pm \sqrt{ \left( \frac{e_1' - e_2'}{2} \right)^2 + V_{12}^2 }$$
   At the exact crossing frequency $\omega = \omega_c$ (where $e_1' = e_2'$), the minimum energy separation between the physical yrast and yrare bands directly yields the interaction strength:
   $$\Delta e'_{\text{min}} = e_+'(\omega_c) - e_-'(\omega_c) = 2 |V_{12}| \implies |V_{12}| = \frac{1}{2} \Delta e'_{\text{min}}$$

4. **Backbending vs Upbending Classification**:
   - **Sharp Backbending** ($|V_{12}| < 35\text{ keV}$): Weak interaction produces a sharp avoided crossing. In the lab frame, $d\omega / dI_x$ becomes negative, creating an S-shaped backward loop in the $\mathcal{J}_1$ vs $\omega^2$ curve (e.g. $^{156}\text{Dy}, ^{158}\text{Er}$).
   - **Smooth Upbending** ($|V_{12}| \ge 65\text{ keV}$): Strong interaction mixes the bands over a wide frequency interval. $d\omega / dI_x$ remains positive, producing a smooth upward inflection (e.g. $^{164}\text{Er}, ^{168}\text{Yb}$).

## Necessary Assumptions

1. **Constant Deformation Across the Crossing**: Quadrupole deformation parameters $(\varepsilon_2, \gamma)$ change smoothly without sudden shape transitions during pair alignment.
2. **Diabatic Two-State Truncation**: Near the crossing frequency $\omega_c$, coupling to higher-lying four-quasiparticle configurations can be neglected.

## Discriminating Observables

1. **Avoided Crossing Minimum Splitting $\Delta e'_{\text{min}}$**:
   Plotting experimental Routhians of the yrast and yrare bands versus $\hbar\omega$ directly extracts $2|V_{12}|$.
2. **50/50 Configuration Mixing at $\omega_c$**:
   At $\omega = \omega_c$, the mixing angle $\theta = 45^\circ$, meaning the physical state is a $50\%$ mixture of the paired vacuum and the broken high-$j$ pair.
3. **Oscillatory $|V_{12}|$ with Fermi Surface $\lambda$**:
   As the neutron number increases across an isotopic chain, $|V_{12}|$ oscillates between sharp backbending (node of $V_{12}$) and smooth upbending (antinode), reflecting the filling of the high-$j$ shell.

## Supporting Evidence

1. **$^{164}\text{Er}$ Smooth Upbending Benchmark**:
   - $\hbar\omega_c = 0.280\text{ MeV}$, aligned angular momentum $\Delta i_x = 10.0\ \hbar$ ($i_{13/2}$ neutron pair).
   - Minimum avoided crossing splitting $\Delta e'_{\text{min}} = 180.0\text{ keV} \implies |V_{12}| = 90.0\text{ keV}$.
   - Classified as smooth upbending ($|V_{12}| > 65\text{ keV}$), reproducing experimental gradual alignment.
2. **$^{156}\text{Dy}$ Sharp Backbending Benchmark**:
   - $\hbar\omega_c = 0.290\text{ MeV}$, $|V_{12}| = 20.0\text{ keV}$, $\Delta e'_{\text{min}} = 40.0\text{ keV}$.
   - Classified as sharp backbending ($|V_{12}| < 35\text{ keV}$), reproducing the classic S-shaped backbending curve.
3. **$^{134}\text{Nd}$ Proton Crossing Benchmark ($A \sim 130$)**:
   - $\hbar\omega_c = 0.320\text{ MeV}$, $|V_{12}| = 45.0\text{ keV}$, $\Delta i_x = 7.5\ \hbar$ ($h_{11/2}$ proton alignment).

## Counter-evidence and Competing Interpretations

1. **Band Crossing vs Shape Coexistence**:
   In transitional nuclei (e.g. Hg and Pt isotopes), an apparent backbend can be caused by the crossing of states with different nuclear shapes (prolate vs oblate) rather than Coriolis pair alignment. Shape coexistence crossings are distinguished by large changes in transition quadrupole moments $Q_t$.
2. **Pairing Collapse vs Coriolis Anti-Pairing (CAP)**:
   Early models attributed backbending to a complete phase transition from superfluid to normal state (pairing collapse). The Mottelson-Valatin CAP model and CSM demonstrated that backbending is caused by the alignment of a specific high-$j$ pair, with residual pairing remaining substantial in the other orbits.

## Our Current Position

In this wiki, high-spin band crossings, avoided crossing Routhians, and interaction matrix elements $|V_{12}|$ are analyzed using Module 105 (`cranked_shell_model_band_crossing_v12_inverter.py`, CLI subcommand `csm`). The module calculates diabatic and adiabatic Routhians, configuration mixing percentages, dynamic alignments $i_x(\omega)$, and classifies sharp backbending versus smooth upbending.

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]: A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-3 (pp. 31–38).
- Bengtsson, R., Frauendorf, S., *Quasiparticle spectra in rotating nuclei*, Nucl. Phys. A 327, 139 (1979).
- Stephens, F. S., *Coriolis effects and rotation alignment in nuclei*, Rev. Mod. Phys. 47, 43 (1975).
