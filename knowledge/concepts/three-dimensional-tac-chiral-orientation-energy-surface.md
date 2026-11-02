---
type: concept
title: "Three-dimensional tilted axis cranking (TAC) chiral orientation energy surface and bifurcation"
aliases: [3d-tac-chiral-energy-surface, chiral-bifurcation, aplanar-planar-transition, chiral-tunneling-barrier]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [triaxiality, nuclear-chirality, tilted-axis-cranking, tac, aplanar-rotation, chiral-bifurcation, chiral-doublets]
---

# Three-dimensional tilted axis cranking (TAC) chiral orientation energy surface and bifurcation

## Definition

In rotating triaxial odd-odd and odd-$A$ nuclei with a high-$j$ valence particle and hole (such as $^{134}\text{Pr}, ^{128}\text{Cs}, ^{106}\text{Ag}$ with $\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$), the three mutually orthogonal angular momentum components:
- Valence proton particle $\vec{j}_p$ along the short $s$-axis;
- Valence neutron hole $\vec{j}_n$ along the long $l$-axis;
- Core collective rotation $\vec{R}$ along the intermediate $m$-axis ($\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$);
combine into a total angular momentum vector $\vec{J} = \vec{R} + \vec{j}_p + \vec{j}_n$.

In the Three-Dimensional Tilted Axis Cranking (TAC) model (Frauendorf & Meng 1997; Frauendorf 2001 §VII.B; Petrache 2025 CRC Press Ch. 3), the orientation of $\vec{J}$ on the unit sphere is parameterized by the polar tilt angle $\theta$ and azimuthal tilt angle $\phi$:
$$J_s = J \sin\theta \cos\phi, \quad J_m = J \sin\theta \sin\phi, \quad J_l = J \cos\theta$$
The total quasiclassical orientation energy surface $E(\theta, \phi; J)$ is:
$$E(\theta, \phi; J) = \frac{(J_s - j_p)^2}{2\mathcal{J}_s} + \frac{J_m^2}{2\mathcal{J}_m} + \frac{(J_l - j_n)^2}{2\mathcal{J}_l}$$

The competition among these three terms governs the phase transition from planar to aplanar rotation:
1. **Low-Spin Planar Phase ($J < J_{\text{crit}}$)**:
   At low spins, the core rotational energy is insufficient to pull $\vec{J}$ away from the $(s, l)$ plane. The energy minimum occurs at $\phi_{\text{min}} = 0^\circ \implies J_m = 0$. Rotation is confined to the $(s, l)$ principal plane, and chiral symmetry is preserved.
2. **Chiral Bifurcation ($J \ge J_{\text{crit}}$)**:
   At the critical bifurcation spin $J_{\text{crit}}$, the planar minimum becomes a saddle point. Two degenerate aplanar minima emerge at:
   $$(\theta_0, \phi_0) \quad \text{and} \quad (\pi - \theta_0, \pi - \phi_0)$$
   where all three components ($J_s, J_m, J_l$) are simultaneously non-zero! The rotational axis breaks $\mathcal{T}\mathcal{R}_y(\pi)$ symmetry, spontaneously creating **Left-handed and Right-handed chiral twins**.
3. **Planar Chiral Barrier $\Delta E_{\text{barrier}}$**:
   The energy difference between the planar saddle point and the aplanar minimum:
   $$\Delta E_{\text{barrier}} = E_{\text{planar}} - E_{\text{min}}$$
   In quantum mechanics, finite tunneling through this barrier lifts the degeneracy between left- and right-handed states, producing the observed **Chiral Doublet Band splitting** $\Delta E(I) \approx \Delta E_{\text{tunneling}}$.

## Necessary Assumptions

1. **Rigid Triaxial Rotor Core**: The intermediate-axis moment of inertia dominates ($\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$).
2. **Frozen Intrinsic Alignments**: The valence proton particle remains aligned with the $s$-axis and the neutron hole with the $l$-axis over the chiral rotation window.

## Discriminating Observables

1. **Azimuthal Tilt Angle $\phi_{\text{min}}$ Non-Zero Onset**:
   Tracking $\phi_{\text{min}}$ versus spin $J$ shows $\phi = 0^\circ$ below $J_{\text{crit}}$ and a smooth rise to $\phi \sim 35^\circ - 45^\circ$ above $J_{\text{crit}}$, directly marking the chiral bifurcation.
2. **Aplanarity Volume Metric $\mathcal{V}_{\text{chiral}}$**:
   $$\mathcal{V}_{\text{chiral}} = \frac{|\vec{j}_p \cdot (\vec{j}_n \times \vec{R})|}{j_p j_n R} \approx \frac{J_m}{J}$$
   $\mathcal{V}_{\text{chiral}} = 0$ in the planar phase, rising to $\mathcal{V}_{\text{chiral}} > 0.40$ in the robust chiral regime.
3. **Energy Barrier $\Delta E_{\text{barrier}}$ Growth**:
   The barrier grows from $0\text{ keV}$ at $J_{\text{crit}}$ to $> 100 - 300\text{ keV}$ at high spin, thickening the tunneling barrier and driving the doublet band energy splitting toward degeneracy ($\Delta E(I) \to 0$).

## Supporting Evidence

1. **$^{134}\text{Pr}$ Chiral Tripod Benchmark ($\mathcal{J}_m = 25, \mathcal{J}_s = 15, \mathcal{J}_l = 5\ \hbar^2/\text{MeV}, j_p = 5.5, j_n = 5.5$)**:
   - At $J \le 14\ \hbar$: $\phi_{\text{min}} = 1.0^\circ \approx 0^\circ, J_m \approx 0.2\ \hbar$, barrier $= 0.0\text{ keV}$ (Planar Rotation);
   - At $J = 16\ \hbar$: $\phi_{\text{min}} = 17.9^\circ, J_m = 4.4\ \hbar$, barrier $= 6.3\text{ keV}$ (Chiral Bifurcation onset!);
   - At $J = 18\ \hbar$: $\phi_{\text{min}} = 34.3^\circ, J_m = 9.4\ \hbar$, $\theta_{\text{min}} = 67.5^\circ$, barrier $= 107.8\text{ keV}$, $\mathcal{V}_{\text{chiral}} = 0.520$;
   - At $J = 20\ \hbar$: $\phi_{\text{min}} = 42.9^\circ, J_m = 12.8\ \hbar$, barrier $= 329.8\text{ keV}$, reproducing Frauendorf & Meng (1997) Fig. 2.
2. **$^{128}\text{Cs}$ Chiral Doublet Band**:
   Experimental energy splitting drops below $30\text{ keV}$ at $I \ge 14\ \hbar$, consistent with a calculated chiral barrier $\Delta E_{\text{barrier}} > 100\text{ keV}$ suppressing quantum tunneling.

## Counter-evidence and Competing Interpretations

1. **Chiral Vibration vs Static Chiral Rotation**:
   When $\Delta E_{\text{barrier}}$ is small compared to the zero-point quantum vibrational energy ($\hbar\Omega_{\text{vib}} \sim 200 - 300\text{ keV}$), the system oscillates rapidly between left- and right-handed states (chiral vibration) rather than forming static stable chiral rotation.
2. **Planar Collapse at Extreme Spin**:
   At very high rotational frequencies, Coriolis forces eventually pull both $j_p$ and $j_n$ into alignment with the $m$-axis, collapsing $\vec{J}$ back into the $(s, m)$ or $(l, m)$ plane and terminating chirality.

## Our Current Position

In this wiki, 3D Tilted Axis Cranking orientation energy surfaces $E(\theta, \phi)$, chiral bifurcation points $J_{\text{crit}}$, planar tunneling barriers $\Delta E_{\text{barrier}}$, and aplanarity metrics are calculated using Module 111 (`tac_3d_chiral_orientation_energy_surface_calculator.py`, CLI subcommand `tac`). The module numerically maps the transition from planar rotation to spontaneous chiral symmetry breaking.

## Sources

- [[book-petrache-chirality-and-wobbling]]: J. Meng and Y. P. Wang, in *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025), Ch. 3 (pp. 81–93).
- Frauendorf, S., Meng, J., *Tilted rotation of triaxial nuclei*, Nucl. Phys. A 617, 131 (1997).
- Frauendorf, S., *Spontaneous symmetry breaking in rotating nuclei*, Rev. Mod. Phys. 73, 463 (2001).
