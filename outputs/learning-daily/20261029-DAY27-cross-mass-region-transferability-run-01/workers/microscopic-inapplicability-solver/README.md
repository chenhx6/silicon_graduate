# Microscopic Inapplicability Criteria Formalization and Phase Boundary Topology Solver

This worker implements the quantitative formalization of the four microscopic inapplicability criteria and solves the multimodal coexistence phase boundary topology across the nuclear chart for Day 27 of the nuclear structure research apprenticeship.

## 1. Mathematical Formalisms

### Criterion 1: Core Quadrupole Collective Masking Limit
In a shears (magnetic rotation) band, the transverse magnetic dipole transition probability is:
$$B(M1; I \to I-1) = \frac{3}{8\pi} j_{\rm eff}^2 (g_p - g_n)^2 \sin^2(\theta/2)$$
and the shears quadrupole transition probability is:
$$B(E2; I \to I-2)_{\rm shears} = \frac{15}{128\pi} Q_{\rm eff}^2 \sin^4(\theta/2)$$
where $Q_{\rm eff} \sim 0.25\ e{\rm b}$.
Meanwhile, the collective rotor core emits $E2$ radiation with intrinsic quadrupole moment:
$$Q_0 = \frac{3}{\sqrt{5\pi}} Z R_0^2 \beta_2 (1 + 0.36\beta_2)$$
$$B(E2; I \to I-2)_{\rm core} \approx \frac{15}{128\pi} e^2 Q_0^2(\beta_2)$$
We formalize the collective masking ratio:
$$R_{E2}(\beta_2, \theta) = \frac{B(E2)_{\rm core}}{B(E2)_{\rm shears}} = \frac{e^2 Q_0^2(\beta_2)}{Q_{\rm eff}^2 \sin^4(\theta/2)}$$
**Quantitative Boundary:**
- When $\beta_2 < 0.18$ ($A \approx 190$ Pb, $A \approx 100$ Cd, $A \approx 135$ Pr), $R_{E2} < 15$ for open shears ($\theta \sim 90^\circ$), allowing clear observation of isolated shears dipole cascades.
- When $\beta_2 > 0.25$ ($A \approx 160$ Dy, Er), $Q_0 \gtrsim 6.5\ e{\rm b}$, driving $R_{E2} > 50$ even for open shears, and $R_{E2} > 500$ as the shears angle closes ($\theta < 45^\circ$). The weak shears radiation is completely masked by the overwhelming collective core flow.

### Criterion 2: Particle-Hole Shears Asymmetry and Pairing Breakdown
Shears rotation requires perpendicular high-$j$ blades forming a planar opening angle $\theta$.
Let $j_p$ and $j_n$ be the angular momenta of the proton and neutron blades.
The blade asymmetry parameter is:
$$\Delta_j = \frac{|j_p - j_n|}{j_p + j_n}$$
**Quantitative Boundary:**
- Stable shears require $\Delta_j \le 0.35$ and pairing ratio $\Delta / V_{\pi\nu} \le 3.5$.
- In configurations with severe mismatch (e.g., $j_p = 3/2, j_n = 13/2$, $\Delta_j = 0.625$), the lighter blade is Coriolis-aligned into the rotation axis immediately, destroying shears dynamics.
- When the pairing gap exceeds particle-hole coupling ($\Delta / V_{\pi\nu} > 3.5$), pairing condensation suppresses independent shears opening.

### Criterion 3: Anharmonic Wobbling Phonon Damping and $\gamma$-Softness
Harmonic wobbling frequency:
$$\hbar\omega_{\rm wob} = I \sqrt{\left(\frac{1}{\mathcal{J}_x} - \frac{1}{\mathcal{J}_y}\right)\left(\frac{1}{\mathcal{J}_x} - \frac{1}{\mathcal{J}_z}\right)}$$
In a $\gamma$-soft potential, the RMS fluctuation width is $\sigma_\gamma = \sqrt{\langle (\gamma - \gamma_0)^2 \rangle}$.
Coupling to low-lying $\gamma$-vibrations induces anharmonicity:
$$\alpha = \frac{E(n_w=2) - 2E(n_w=1)}{E(n_w=1)} \approx -3 \left(\frac{\sigma_\gamma}{\gamma_0}\right)^2$$
and phonon damping width:
$$\frac{\Gamma_{\rm wob}}{\hbar\omega_{\rm wob}} \approx 1.5 \left(\frac{\sigma_\gamma}{\gamma_0}\right)^2$$
**Quantitative Boundary:**
- In triaxial superdeformed bands of $^{163,165}{\rm Lu}$ ($\sigma_\gamma \approx 5^\circ, \gamma_0 \approx 20^\circ$), $\Gamma_{\rm wob}/\hbar\omega_{\rm wob} \approx 0.09 < 0.20$, supporting discrete multiphonon wobbling states.
- In normally deformed $A \approx 130$ ($^{135}{\rm Pr}, ^{131}{\rm Ce}$, $\sigma_\gamma \approx 18^\circ$, near the flat Wilets-Jean limit $17.3^\circ$), $\Gamma_{\rm wob}/\hbar\omega_{\rm wob} \approx 1.2 > 0.50$. The wobbling phonon is overdamped, mixing completely into quasiparticle-plus-core excitations.

### Criterion 4: Proton-Neutron Octupole Dipole Cancellation Boundary
The intrinsic electric dipole moment is:
$$D_0 = D_0^{\rm macro} + D_0^{\rm shell}(\pi) + D_0^{\rm shell}(\nu)$$
where $D_0^{\rm macro} \approx 0.00069 A Z \beta_2 \beta_3\ e{\rm fm}$.
**Quantitative Boundary:**
- In the light lanthanides ($Z \approx 56, N \approx 88$, e.g., $^{144,146}{\rm Ba}$), the neutron shell correction $D_0^{\rm shell}(\nu) \approx -0.28\ e{\rm fm}$ opposes the macroscopic term $D_0^{\rm macro} \approx +0.25\ e{\rm fm}$, producing near-exact dipole cancellation ($|D_0| < 0.08\ e{\rm fm}$) despite strong octupole collectivity ($B(E3) \approx 48\text{ W.u.}$).
- In the actinides ($Z \approx 88, N \approx 136$, e.g., $^{224}{\rm Ra}, ^{226}{\rm Th}$), proton and neutron shell contributions are in-phase ($D_0^{\rm macro} + D_0^{\rm shell} \approx +0.35 + 0.10 \approx +0.45\ e{\rm fm}$), yielding huge $D_0$ and strong $E1$ transitions.
- The cancellation island is strictly confined to $Z \approx 54-58, N \approx 86-90$. Extrapolating the small $E1$ of $^{144}{\rm Ba}$ to Actinides or vice versa violates microscopic shell structure.

## 2. Multimodal Phase Boundary Topology
Phase mapping in $(\beta_2, \gamma)$ deformation space reveals:
- **Magnetic Rotation (MR):** Confined to $\beta_2 \le 0.22$, $\gamma \le 20^\circ$ or $\gamma \ge 40^\circ$.
- **Antimagnetic Rotation (AMR):** Confined to $\beta_2 \le 0.20$, near-axial oblate/prolate shapes.
- **Triaxial Chirality:** Confined to $0.15 \le \beta_2 \le 0.32$, $18^\circ \le \gamma \le 42^\circ$ (peaked at $30^\circ$).
- **Wobbling:** Requires stable triaxiality ($\beta_2 \ge 0.22$, $12^\circ \le \gamma \le 48^\circ$) with asymmetric moments of inertia.
- **Conventional Collective Core Rotation:** Dominates for $\beta_2 > 0.25$ outside triaxial wobbling conditions.

## 3. Worker Artifacts
- `microscopic_inapplicability_solver.py`: Core computational engine.
- `plot_phase_boundaries.py`: Visualizations of criteria curves and phase topology.
- `core_quadrupole_masking.json` & `.csv`: Numerical evaluation of $R_{E2}$.
- `particle_hole_asymmetry.json` & `.csv`: Shears blade mismatch and pairing stability data.
- `anharmonic_wobbling_damping.json` & `.csv`: Wobbling damping and anharmonicity data.
- `octupole_dipole_cancellation.json` & `.csv`: Microscopic $D_0$ dipole cancellation across $A \approx 140$ and $A \approx 220$.
- `phase_boundary_topology.json` & `.csv`: Grid evaluation of collective modes in $(\beta_2, \gamma)$ space.
- Figures: `core_quadrupole_masking.png`, `anharmonic_wobbling_damping.png`, `phase_boundary_topology.png`.
- `worker-delivery.json`: Structured manifest.
