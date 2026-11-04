# Volume I, Chapter 1: Symmetries and Conservation Laws

**Book**: *Nuclear Structure, Vol. I: Single-Particle Motion* (A. Bohr & B. R. Mottelson)
**Printed Pages**: pp. 1–136 | **Source**: `raw/books/nuclear structure Ⅰ_Bohr, Mottelson.pdf`

---

## 1. Core Frameworks and Theoretical Invariants

### 1.1 Time-Reversal Invariance ($\mathcal{T}$) and Kramers Degeneracy
- Time-reversal operation on spin-$1/2$ particles:
  $$\mathcal{T} = U K_0 = -i \sigma_y K_0 = e^{-i \pi s_y} K_0.$$
- For an $A$-nucleon system with total angular momentum $J$:
  $$\mathcal{T}^2 = (-1)^{2J} = (-1)^A.$$
- **Kramers Degeneracy Theorem**: For odd-$A$ systems ($\mathcal{T}^2 = -1$), no state can be an eigenstate of $\mathcal{T}$ with real eigenvalue. Therefore, every single-particle energy level in a time-reversal-invariant deformed potential is at least twofold degenerate:
  $$\langle \psi | \mathcal{T} \psi \rangle = 0 \implies |\psi\rangle \perp \mathcal{T}|\psi\rangle.$$
  In deformed mean fields with axial symmetry, states $|\Omega\rangle$ and $|-\Omega\rangle$ have identical single-particle energy $\epsilon_\Omega$.

### 1.2 Space-Inversion Parity ($\mathcal{P}$)
- Single-particle wave function parity: $\pi = (-1)^l$.
- Strong interaction strictly conserves parity. Parity-violating weak interactions contribute small admixtures ($\sim 10^{-7}$).

### 1.3 Isospin Invariance ($T$) and Morpurgo $E1$ Selection Rule
- The nuclear dipole operator in the center-of-mass frame:
  $$\vec{D} = e \sum_{p} (\vec{r}_p - \vec{R}_{\text{c.m.}}) = \frac{N}{A} e \sum_{p} \vec{r}_p - \frac{Z}{A} e \sum_{n} \vec{r}_n = \sum_{k=1}^A e_k^{\text{eff}} \vec{r}_k.$$
- Effective charges for electric dipole radiation:
  $$e_p^{\text{eff}} = \frac{N}{A} e, \quad e_n^{\text{eff}} = - \frac{Z}{A} e.$$
- Decomposition into isoscalar ($T=0$) and isovector ($T=1$) parts:
  $$e_{\text{IS}} = \frac{1}{2} (e_p^{\text{eff}} + e_n^{\text{eff}}) = \frac{N-Z}{2A} e, \quad e_{\text{IV}} = \frac{1}{2} (e_p^{\text{eff}} - e_n^{\text{eff}}) = \frac{1}{2} e.$$
- **Morpurgo Rule**: For $N = Z$ self-conjugate nuclei, the isoscalar effective charge $e_{\text{IS}} \equiv 0$. Since the photon field cannot induce $\Delta T = 0$ transitions via an isovector operator without changing isospin, **$\Delta T = 0$ $E1$ transitions in $N=Z$ nuclei are strictly forbidden by isospin invariance**.

---

## 2. Experimental Diagnostic Rules

1. Any claim of time-reversal symmetry breaking in an intrinsic nuclear state must identify an external magnetic field, rotating cranking frequency $\vec{\omega}_{\text{rot}}$, or weak interaction.
2. In $N=Z$ nuclei, any observed $E1$ transition with strength exceeding $10^{-4}\text{ W.u.}$ represents Coulomb-induced isospin mixing $\alpha_C^2$.
