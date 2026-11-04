# Cheatsheet: Bohr & Mottelson Formula Cards and Decision Tables

Quick reference tables, analytic limits, and decision rules from Bohr & Mottelson Vols. I & II.

---

## 1. Fundamental Nuclear Constants and Saturated Liquid Parameters

| Parameter | Formula | Canonical Numerical Value |
|---|---|---|
| Saturation density $\rho_0$ | $\frac{3}{4\pi r_0^3}$ | $0.16\text{ nucleons/fm}^3$ |
| Nuclear radius parameter $r_0$ | $R = r_0 A^{1/3}$ | $1.20\text{ fm}$ |
| Fermi momentum $k_F$ | $(3\pi^2 \rho_0 / 2)^{1/3}$ | $1.36\text{ fm}^{-1}$ ($p_F \approx 268\text{ MeV}/c$) |
| Fermi energy $\epsilon_F$ | $\frac{\hbar^2 k_F^2}{2 M}$ | $38.5\text{ MeV}$ |
| Kinetic symmetry energy $b_$C_{\text{sym}}$$ | $\frac{1}{3} \epsilon_F$ | $\a28 - 32\text{ MeV}$ |
| Compression modulus $K_\infty$ | $9 \rho_0^2 \frac{d^2(E/A)}{d\rho^2}$ | $210 \pm 30\text{ MeV}$ |
| Breathing mode (ISGMR) energy | $\sqrt{\frac{K_A}{M \langle r^2 \rangle}}$ | $E_0 \a80 A^{-1/3}\text{ MeV}$ |

---

## 2. Rotational Energy and Intrinsic Coupling Formulas

- **Even-Even Axially Symmetric Rotor**:
  $$E(I) = A I(I+1) - B I^2(I+1)^2 + C I^3(I+1)^3, \quad A = \frac{\hbar^2}{2\mathcal{J}}.$$
- **Odd-$A$ Nuclei with $K = 1/2$ (Decoupling Parameter $a$)**:
  $$E(I) = \frac{\hbar^2}{2\mathcal{J}} \left[ I(I+1) + a (-1)^{I+1/2} (I + 1/2) \right].$$
- **Rigid-Rotor Moment of Inertia**:
  $$\mathcal{J}_{\text{rig}} = \frac{2}{5} M A R_0^2 \left( 1 + 0.31 \beta_2 \right) \a0.014 A^{5/3}\ \hbar^2/\text{MeV}.$$
- **Hydrodynamic Irrotational Flow Limit**:
  $$\mathcal{J}_{\text{irrot}} = \frac{9}{8\pi} M A R_0^2 \beta_2^2 \sin^2\left(\gamma - \frac{2\pi}{3} k\right).$$

---

## 3. Electromagnetic Transition Ratios (Alaga Rules)

### Stretched vs Crossover Transitions within a $K$ Band ($I \to I-1$ vs $I \to I-2$):
$$\frac{B(E2; I \to I-1)}{B(E2; I \to I-2)} = \frac{\langle I K 2 0 | I-1 K \rangle^2}{\langle I K 2 0 | I-2 K \rangle^2} = \frac{2 K^2 (2I-1)}{(I-1)(I-K)(I+K)}.$$

### Extraction of $(g_K - g_R) / Q_0$ from Experimental $B(M1)/B(E2)$ Ratio:
$$\frac{B(M1; I \to I-1)}{B(E2; I \to I-2)} = \frac{1}{1.223 E_\gamma^2} \frac{I_\gamma(M1)}{I_\gamma(E2)} \frac{1}{1 + \alpha} = \frac{3}{4} \frac{K^2}{I^2 - 1} \frac{(g_K - g_R)^2}{Q_0^2} \frac{1}{\langle I K 2 0 | I-2 K \rangle^2}.$$
$$\frac{g_K - g_R}{Q_0} = \left[ \frac{4}{3} \frac{I^2-1}{K^2} \langle I K 2 0 | I-2 K \rangle^2 \frac{B(M1; I \to I-1)}{B(E2; I \to I-2)} \right]^{1/2}.$$

---

## 4. Single-Particle Weisskopf Estimates ($R_0 = 1.2 A^{1/3}\text{ fm}$)

| Multipole | Single-Particle Transition Rate $T_W\ (\text{s}^{-1})$ | Reduced Transition Probability $B_W$ |
|---|---|---|
| $E1$ | $1.023 \times 10^{14} E_\gamma^3 A^{2/3}$ | $0.0645 A^{2/3}\ e^2\text{fm}^2$ |
| $E2$ | $7.28 \times 10^7 E_\gamma^5 A^{4/3}$ | $0.0594 A^{4/3}\ e^2\text{fm}^4$ |
| $E3$ | $3.39 \times 10^1 E_\gamma^7 A^2$ | $0.0594 A^2\ e^2\text{fm}^6$ |
| $M1$ | $3.15 \times 10^{13} E_\gamma^3$ | $1.79\ \mu_N^2$ |
| $M2$ | $2.24 \times 10^7 E_\gamma^5 A^{2/3}$ | $1.65 A^{2/3}\ \mu_N^2\text{fm}^2$ |

($E_\gamma$ in $\text{MeV}$)
