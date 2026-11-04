# Reasoning Patterns: Bohr & Mottelson Nuclear Structure Toolkit

This document formalizes reusable theoretical and spectroscopic reasoning patterns established in Bohr & Mottelson Vols. I & II.

---

## Pattern 1: Symmetry and Invariance Analysis First

- **Core Rule**: Before attempting dynamical or phenomenological modeling of a nuclear state, classify its quantum numbers under the exact invariance operations: parity $\mathcal{P}$, time-reversal $\mathcal{T}$, rotational signature $\mathcal{R}_x(\pi)$, and isospin $T$.
- **Application Examples**:
  - **Kramers Degeneracy Check**: If a nucleus has odd mass $A$, any static deformed mean field preserves $\mathcal{T}^2 = -1$. Single-particle orbits must pair as $(\Omega, -\Omega)$. Never introduce spontaneous time-reversal breaking without an explicit cranking angular frequency $\vec{\omega}_{\text{rot}} \neq 0$.
  - **Morpurgo $E1$ Cancellation**: For a transition with $\Delta T = 0$ in an $N=Z$ nucleus, the isovector $E1$ operator cancels identically. If an experimental $E1$ strength exceeds $10^{-4}\text{ W.u.}$, it immediately signals isospin symmetry breaking by the Coulomb interaction.

---

## Pattern 2: Adiabatic Separation and Geometric Branching (Alaga Protocol)

- **Core Rule**: In a well-deformed axially symmetric rotor, the transition matrix element factors into a purely geometric Clebsch-Gordan coefficient times an intrinsic matrix element $M_{\text{intr}}$:
  $$B(E\lambda; I_i K_i \to I_f K_f) = \langle I_i K_i \lambda \Delta K | I_f K_f \rangle^2 |M_{\text{intr}}|^2.$$
- **Workflow**:
  1. Compute the theoretical Alaga branching ratio:
     $$R_{\text{Alaga}} = \frac{\langle I_i K_i \lambda \Delta K | I_{f1} K_f \rangle^2}{\langle I_i K_i \lambda \Delta K | I_{f2} K_f \rangle^2}.$$
  2. Compare with the experimental ratio $R_{\text{exp}} = (I_{\gamma 1} / E_{\gamma 1}^{2\lambda+1}) / (I_{\gamma 2} / E_{\gamma 2}^{2\lambda+1})$.
  3. If $R_{\text{exp}} \approx R_{\text{Alaga}}$, the states are pure rotational band members with preserved $K$-symmetry.
  4. If $R_{\text{exp}}$ deviates systematically from $R_{\text{Alaga}}$, proceed to Pattern 3 (Mikhailov non-adiabatic perturbation).

---

## Pattern 3: Mikhailov Non-Adiabatic Coriolis Decomposition

- **Core Rule**: When Coriolis mixing perturbs the rotational band, expand the transition matrix element in powers of the spin difference:
  $$M_I = \frac{\sqrt{B(E2; I_i K_i \to I_f K_f)}}{\langle I_i K_i 2 \Delta K | I_f K_f \rangle} = M_0 + M_1 \left[ I_f(I_f+1) - I_i(I_i+1) \right].$$
- **Interpretation**:
  - $M_0$: Unperturbed intrinsic quadrupole moment;
  - $M_1$: First-order Coriolis mixing matrix element;
  - A linear Mikhailov plot confirms first-order Coriolis perturbation between $\Delta K = \pm 1$ bands;
  - Curvature in the Mikhailov plot signals strong multistate mixing or an avoided level crossing (backbending).

---

## Pattern 4: Coriolis Decoupling and High-$j$ Intruder Alignment

- **Core Rule**: Valence nucleons in high-$j$ unique-parity orbitals (e.g. $\pi h_{11/2}, \nu i_{13/2}$) experience a Coriolis force that scales with $j(j+1)$.
- **Diagnostic Signature**:
  - For low Fermi levels ($\Omega = 1/2, 3/2$), the Coriolis matrix element pushes the favored signature states ($\alpha = +1/2$ or $-1/2$) to lower energies, creating a decoupled band:
    $$\Delta E(I \to I-2) \approx \Delta E_{\text{core}}(R \to R-2).$$
  - The energy spacing of the decoupled odd-$A$ band mirrors the ground-state band of the adjacent even-even core.
  - In contrast, for high Fermi levels near the top of the subshell ($\Omega = j, j-1$), the Coriolis alignment is blocked, and the nucleus exhibits strong deformation-coupled $\Delta I = 1$ rotational bands with regular Alaga branching.

---

## Pattern 5: Collective Vibrations vs EWSR Exhaustion

- **Core Rule**: Never classify a low-lying $2^+$ or $3^-$ state as a collective phonon without auditing its Energy-Weighted Sum Rule (EWSR) fraction.
- **Criterion**:
  - A genuine collective surface vibration must exhaust at least $10\% - 30\%$ of the classical EWSR:
    $$S_{\text{EWSR}}(E\lambda) = \frac{\lambda (2\lambda+1)^2}{8\pi} \frac{\hbar^2}{M} Z R_0^{2\lambda-2} e^2.$$
  - If a state exhausts $<2\%$ of the EWSR, it is predominantly a 2-quasiparticle non-collective excitation, regardless of whether its energy looks low.
