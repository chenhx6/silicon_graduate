# Volume II, Chapter 5: One-Particle Motion in Non-Spherical Nuclei

**Book**: *Nuclear Structure, Vol. II: Nuclear Deformations* (A. Bohr & B. R. Mottelson)
**Printed Pages**: pp. 175–344 | **Source**: `raw/books/nuclear structure Ⅱ_Bohr, Mottelson.pdf`

---

## 1. Core Frameworks and Theoretical Invariants

### 1.1 The Nilsson Hamiltonian and Asymptotic Quantum Numbers
- Anisotropic deformed oscillator Hamiltonian:
  $$H_{\text{sp}} = -\frac{\hbar^2}{2M} \nabla^2 + \frac{1}{2} M (\omega_x^2 x^2 + \omega_y^2 y^2 + \omega_z^2 z^2) - C \vec{l}\cdot\vec{s} - D (\vec{l}^2 - \langle \vec{l}^2 \rangle_N).$$
- Axially symmetric deformation ($\omega_x = \omega_y = \omega_\perp$):
  $$\omega_z = \omega_0 (1 - \frac{2}{3}\delta), \quad \omega_\perp = \omega_0 (1 + \frac{1}{3}\delta).$$
- Asymptotic basis states at large deformation: $|N n_z \Lambda \Omega\rangle$:
  - $N$: Total oscillator quantum number ($N = n_x + n_y + n_z$);
  - $n_z$: Number of oscillator nodes along the symmetry axis ($z$);
  - $\Lambda$: Component of orbital angular momentum along $z$ ($\Lambda \le N - n_z$);
  - $\Omega$: Component of total angular momentum along $z$ ($\Omega = \Lambda \pm 1/2$).
- Energy systematics: Orbitals with large $n_z$ (slender wave functions aligned along the prolate axis) decrease sharply in energy with prolate deformation ($\delta > 0$).

### 1.2 Coriolis Coupling and Stephens-Simon Decoupled Bands
- The rotating-frame particle-plus-rotor Hamiltonian:
  $$H = H_{\text{intr}} + \frac{\hbar^2}{2\mathcal{J}} [(\vec{I} - \vec{j})^2] = H_{\text{intr}} + \frac{\hbar^2}{2\mathcal{J}} [\vec{I}^2 + \vec{j}^2 - 2 I_z j_z] - \frac{\hbar^2}{\mathcal{J}} (I_+ j_- + I_- j_+).$$
- **Decoupled Bands**: For high-$j$ intruder orbitals (e.g. $i_{13/2}, h_{11/2}$) with low $\Omega = 1/2$, the Coriolis matrix element is large and negative for the favored signature ($\alpha = 1/2$ or $I = j, j+2, j+4, \dots$). The particle decouples from the deformation axis and aligns its angular momentum along the collective rotation axis $\vec{R}$.
- **Backbending Mechanism**: The crossing of the ground-state band ($0\text{-qp}$) with the aligned two-quasiparticle band ($S\text{-band}$, $\pi h_{11/2}^2$ or $\nu i_{13/2}^2$) at critical rotational frequency $\hbar\omega_c$.

---

## 2. Experimental Diagnostic Rules

1. Single-nucleon transfer spectroscopic factors $S_{lj}$ directly measure the spherical spherical-harmonic expansion amplitudes $c_{lj}$ of the Nilsson orbital:
   $$\frac{d\sigma}{d\Omega}(I) \propto \langle I_0 K_0 j \Omega | I K \rangle^2 |c_{lj}|^2.$$
2. Staggering between favored ($\alpha = +1/2$) and unfavored ($\alpha = -1/2$) signature states in odd-$A$ bands diagnoses the position of the Fermi level relative to the bottom ($\Omega = 1/2$) or top ($\Omega = j$) of the high-$j$ subshell.
