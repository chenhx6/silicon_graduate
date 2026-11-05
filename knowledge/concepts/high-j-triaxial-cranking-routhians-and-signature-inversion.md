---
type: concept
title: "High-j single-shell triaxial cranking Routhians, alignment and signature inversion"
aliases: [high-j-triaxial-cranking, triaxial-routhians, single-j-cranking, signature-inversion-triaxial, frauendorf-cranking-model]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [triaxiality, cranking-model, routhians, signature-symmetry, signature-inversion, h11-2, high-j-intruder, nuclear-chirality, wobbling]
---

# High-j single-shell triaxial cranking Routhians, alignment and signature inversion

## Definition

In rotating triaxial nuclei with high-$j$ intruder orbitals ($h_{11/2}$ in $A \sim 130$, $i_{13/2}$ in rare earths), the single-particle motion in the rotating intrinsic frame provides the microscopic foundation for Transverse Wobbling (TW) and Nuclear Chirality. Following the cranked single-$j$ shell Hamiltonian (Frauendorf & Meng 1997; Frauendorf in Petrache 2025 CRC Press Ch. 2, Eq. 2.13; Bengtsson & Ragnarsson 1985):
$$h_{\text{crank}}(\gamma, \omega) = h_{\text{sp}}(\gamma) - \omega j_x$$
where:
1. **Triaxial Deformed Potential $h_{\text{sp}}(\gamma)$**:
   $$h_{\text{sp}}(\gamma) = \frac{\kappa}{j(j+1)} \left[ \left(3 j_z^2 - j(j+1)\right) \cos\gamma + \sqrt{3} \left(j_x^2 - j_y^2\right) \sin\gamma \right]$$
   where $\kappa$ is the quadrupole coupling strength ($\approx 2.5 - 4.0\text{ MeV}$) and $\gamma$ is the triaxiality parameter (Lund / Copenhagen convention):
   - $\gamma = 0^\circ$: Axially symmetric prolate;
   - $\gamma = -30^\circ$: Maximally triaxial with rotation around the intermediate $m$-axis;
   - $\gamma = -60^\circ$: Axially symmetric oblate.
2. **Cranking Coriolis Operator $-\omega j_x$**:
   Cranking with angular frequency $\omega$ around the $x$-axis mixes magnetic substates $|j, m\rangle$ with $\Delta m = \pm 1$, while $(j_x^2 - j_y^2)$ mixes states with $\Delta m = \pm 2$.

3. **Signature Symmetry $\alpha = \pm 1/2$**:
   The cranking Hamiltonian commutes with the signature rotation operator $\mathcal{R}_x(\pi) = \exp(-i \pi j_x)$:
   $$[ h_{\text{crank}}, \mathcal{R}_x(\pi) ] \equiv 0$$
   Its eigenvalues $r = \exp(-i \pi \alpha)$ partition the $(2j+1)$ single-particle Routhians $e'_\nu(\omega)$ into:
   - **Favored Signature** ($\alpha = +1/2$, eigenvalue $r = -i$);
   - **Unfavored Signature** ($\alpha = -1/2$, eigenvalue $r = +i$).

4. **Signature Splitting and Signature Inversion (旋称反转)**:
   The signature splitting is defined as:
   $$\Delta e'(\omega) = e'(\alpha = -1/2) - e'(\alpha = +1/2)$$
   - In axially symmetric prolate nuclei ($\gamma = 0^\circ$), the favored signature is strictly lower in energy ($\Delta e' > 0$).
   - In triaxial nuclei ($\gamma \approx -30^\circ$) with the Fermi surface near the bottom of the shell, the combination of triaxial non-diagonal coupling $\sqrt{3}(j_x^2 - j_y^2)\sin\gamma$ and Coriolis mixing drives **Signature Inversion**: at low frequencies ($\hbar\omega < \hbar\omega_{\text{inv}}$), the unfavored signature is anomalously lower in energy than the favored signature ($\Delta e' < 0$)!
   - At $\hbar\omega = \hbar\omega_{\text{inv}}$, the splitting crosses zero ($\Delta e' = 0$), restoring normal signature ordering at high spins.

## Necessary Assumptions

1. **Unique-Parity Single-$j$ Shell Isolation**: High-$j$ intruder orbitals ($h_{11/2}, i_{13/2}$) have opposite parity to all other orbitals in the major oscillator shell, preventing parity mixing.
2. **Fixed Quadrupole Core**: Core deformation $(\varepsilon, \gamma)$ is assumed stable against Coriolis centrifugal expansion over the low-frequency cranking interval.

## Discriminating Observables

1. **Routhian Alignment $\langle j_x \rangle$ at $\gamma = -30^\circ$**:
   For $\gamma = -30^\circ$, the lowest Routhian has alignment
   $\langle j_x \rangle \approx j$ (e.g. $\langle j_x \rangle = 5.47\ \hbar$
   for $j=5.5$) in this single-$j$ benchmark. This is compatible with
   short-axis alignment under the supplied convention; it does not establish
   the prerequisite geometry of a real nucleus or a TW assignment.
2. **Signature Inversion Crossing Frequency $\hbar\omega_{\text{inv}}$**:
   Experimentally extracted from odd-odd and odd-$A$ rotational bands via $S(I) = [E(I) - E(I-1)] / (2I)$, where the signature staggering phase flips by $180^\circ$.
3. **Triaxiality $\gamma$ Sensitivity**:
   The signature splitting $\Delta e'(\omega)$ is extremely sensitive to $\gamma$, providing an independent microscopic spectroscopic caliper to measure triaxial deformation.

## Supporting Evidence

1. **$h_{11/2}$ Triaxial Chiral Benchmark ($j = 5.5, \gamma = -30^\circ, \kappa = 3.0\text{ MeV}$)**:
   - Evaluated 12 single-particle Routhians; $[h_{\text{crank}}, \mathcal{R}_x(\pi)] = 0$ verified to machine precision ($< 10^{-14}$).
   - Lowest Routhian at $\hbar\omega = 0.20\text{ MeV}$: $e' = -5.1658\text{ MeV}$, with alignment $\langle j_x \rangle = 5.47\ \hbar$ along the rotation axis.
   - Lowest signature splitting $\Delta e' = -2182.8\text{ keV} < 0$, a
     signature-inversion screening result for the supplied triaxial
     single-$j$ Hamiltonian.
2. **$A \sim 130$ Experimental Observables**:
   Signature inversion is reported or reconstructed in candidate bands of
   $^{134}\text{Pr}, ^{128}\text{Cs}$ and $^{106}\text{Ag}$, with crossings near
   $I_{\text{inv}} \approx 13 - 15\ \hbar$ in the cited cases. The inversion is
   an observable/systematics handle and does not by itself establish chiral
   geometry.

## Counter-evidence and Competing Interpretations

1. **Residual Proton-Neutron Interaction ($V_{pn}$)**:
   In odd-odd nuclei, signature inversion can also be influenced by residual $p-n$ tensor and quadrupole-quadrupole interactions. While triaxiality naturally produces signature inversion in a single-particle framework, realistic two-quasiparticle TAC calculations combine triaxial shape with the $V_{pn}$ residual interaction to achieve quantitative agreement with experimental crossing spins.
2. **$\gamma$-Soft Fluctuations**:
   Large-amplitude zero-point fluctuations along the $\gamma$ degree of freedom can dynamically average the signature splitting, requiring projected shell model (TPSM) or generator coordinate method (GCM) treatment.

## Our Current Position

In this wiki, high-$j$ intruder single-particle Routhians, triaxial
alignments $\langle j_x \rangle$, signature quantum numbers $\alpha=\pm1/2$,
and signature-inversion trajectories are calculated using Module 108
(`triaxial_cranking_single_j_routhian_diagram_calculator.py`, CLI subcommand
`crank`). The module exactly diagonalizes the supplied $(2j+1)\times(2j+1)$
single-$j$ Hamiltonian; its result is a model benchmark and requires
nucleus-specific configuration, pairing, residual interaction and experimental
checks before it can support a TW or chiral assignment.

## Sources

- [[book-petrache-chirality-and-wobbling]]: S. Frauendorf, in *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025), Ch. 2 *Wobbling motion in triaxial nuclei*, Eq. (2.13), pp. 43–80.
- Frauendorf, S., Meng, J., *Tilted rotation of triaxial nuclei*, Nucl. Phys. A 617, 131 (1997).
- Bengtsson, R., Ragnarsson, I., *Rotational bands and particle-hole excitations at very high spin*, Nucl. Phys. A 436, 14 (1985).
- [[book-bohr-mottelson-nuclear-structure-vol2]]: A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-3.
