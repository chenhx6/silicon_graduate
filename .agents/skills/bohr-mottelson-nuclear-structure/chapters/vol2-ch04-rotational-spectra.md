# Volume II, Chapter 4: Rotational Spectra

**Book**: *Nuclear Structure, Vol. II: Nuclear Deformations* (A. Bohr & B. R. Mottelson)
**Printed Pages**: pp. 1–174 | **Source**: `raw/books/nuclear structure Ⅱ_Bohr, Mottelson.pdf`

---

## 1. Core Frameworks and Theoretical Invariants

### 1.1 The Unified Rotational Wave Function
- Factorization in axially symmetric deformed nuclei:
  $$\Psi_{IMK} = \sqrt{\frac{2I+1}{16\pi^2 (1 + \delta_{K0})}} \left[ D_{MK}^I(\theta_i) \chi_K + (-1)^{I+K} D_{M,-K}^I(\theta_i) \mathcal{T} \chi_K \right].$$
- Energy eigenvalues for $K > 1/2$:
  $$E(I) = E_0 + \frac{\hbar^2}{2\mathcal{J}} [I(I+1) - K^2].$$
- Energy eigenvalues for $K = 1/2$:
  $$E(I) = E_0 + \frac{\hbar^2}{2\mathcal{J}} \left[ I(I+1) + a (-1)^{I+1/2} (I + 1/2) \right],$$
  where $a$ is the decoupling parameter: $a = -\langle K=1/2 | j_+ \mathcal{T} | K=1/2 \rangle$.

### 1.2 Geometrical Electromagnetic Branching: Alaga Rules
- The transition operator $\mathcal{M}(\lambda, \mu)$ transforms under rotation via Wigner $D$-matrices:
  $$\mathcal{M}(\lambda, \mu) = \sum_\nu D_{\mu\nu}^\lambda(\theta_i) \mathcal{M}'(\lambda, \nu).$$
- Reduced transition probability between rotational states:
  $$B(\lambda; I_i K_i \to I_f K_f) = \langle I_i K_i \lambda \Delta K | I_f K_f \rangle^2 |M_{\text{intr}}(\lambda, \Delta K)|^2.$$
- The ratio of two transition rates from the same initial state $I_i K_i$ to different members $I_{f1}, I_{f2}$ of a final band $K_f$ is a model-independent ratio of Clebsch-Gordan coefficients:
  $$\frac{B(\lambda; I_i K_i \to I_{f1} K_f)}{B(\lambda; I_i K_i \to I_{f2} K_f)} = \frac{\langle I_i K_i \lambda \Delta K | I_{f1} K_f \rangle^2}{\langle I_i K_i \lambda \Delta K | I_{f2} K_f \rangle^2}.$$

### 1.3 Mikhailov Representation for Non-Adiabatic Coriolis Mixing
- First-order perturbation expansion:
  $$\frac{\sqrt{B(E2; I_i K_i \to I_f K_f)}}{\langle I_i K_i 2 \Delta K | I_f K_f \rangle} = M_0 + M_1 [I_f(I_f+1) - I_i(I_i+1)].$$
  Deviations from Alaga rules in experimental in-beam intensities plotted against $[I_f(I_f+1) - I_i(I_i+1)]$ fall on a straight line whose intercept gives the unperturbed moment $M_0$ and slope gives the interband Coriolis mixing matrix element $M_1$.

---

## 2. Experimental Diagnostic Rules

1. Any departure of measured $\gamma$-ray branching ratios from Alaga rules must be analyzed via a Mikhailov plot before hypothesizing shape changes.
2. The intrinsic quadrupole moment $Q_0$ extracted from intra-band $B(E2; 2^+ \to 0^+)$ connects directly to deformation $\beta_2$:
   $$Q_0 = \frac{3}{\sqrt{5\pi}} Z R_0^2 \beta_2 (1 + 0.16 \beta_2).$$
