# Reasoning Patterns: Chirality & Wobbling Diagnostics

Practical diagnostic reasoning patterns and decision rules extracted from *Chirality and Wobbling in Atomic Nuclei* (CRC Press, 2025).

---

## Pattern 1: Wobbling vs Tilted Precession (TiP) Arbitration

- **Core Objective**: Determine whether an excited $\Delta I = 1$ band is a genuine wobbling phonon excitation ($n_w = 1$) or an unfavored signature partner band undergoing tilted precession (TiP).
- **Step-by-Step Arbitration Protocol**:
  1. **Directional Angular Distribution $a_2$**:
     Solve the quadratic equation $(R_{22} - a_2)\delta^2 + 2 R_{12}\delta + (R_{20} - a_2) = 0$.
     Note both real roots: Root 1 (large $|\delta|$, $E2$-dominated) and Root 2 (small $|\delta|$, $M1$-dominated). *Acknowledge that directional data alone cannot distinguish them ($\Delta\chi^2 = 0$).*
  2. **Linear Polarization Asymmetry $P$ (The Gold Standard)**:
     Evaluate the predicted Clover polarization $P(\delta)$:
     - Root 1 predicts $P_{\text{calc}} > 0$ (typically $+0.3 \sim +0.6$, electric character);
     - Root 2 predicts $P_{\text{calc}} < 0$ (typically $-0.1 \sim -0.3$, magnetic character).
     Compare with experimental $P_{\text{exp}}$. If $P_{\text{exp}} < 0$ and excludes Root 1 by $>3\sigma$, wobbling is definitively rejected and TiP is confirmed (as in $^{135}\text{Pr}$).
  3. **Interband Transition Strength Ratio**:
     Measure absolute lifetimes $\tau$ via DSAM/RDDS. Compute $B(E2)_{\text{inter}} / B(E2)_{\text{intra}}$:
     - Wobbling requires collective enhancement: $B(E2)_{\text{inter}} / B(E2)_{\text{intra}} \sim 0.20 - 0.50$;
     - TiP exhibits single-particle weakness: $B(E2)_{\text{inter}} / B(E2)_{\text{intra}} \le 0.05$.

---

## Pattern 2: Koike-Starosta-Hamamoto (KSH) Chiral Verification

- **Core Objective**: Verify whether two degenerate $\Delta I = 1$ bands represent authentic nuclear chirality.
- **Diagnostic Checklist**:
  1. **$S_{M1}(I)$ Staggering Test**:
     Plot $S_{M1}(I)$ for both bands. They must show **100% in-phase staggering**. If the staggering is out-of-phase, classify the bands as planar signature partners.
  2. **Intra-band $B(E2)$ Congruence**:
     Compare transition quadrupole moments $Q_t$. The two bands must agree within experimental errors ($<15\%$). If $Q_t$ differs by $>40\%$, classify the bands as shape coexistence.
  3. **Interband $\Delta I = 0$ $M1$ Minimum**:
     At the spin of minimum energy separation $\Delta E(I) \to \min$, the interband $B(M1; B \to A, \Delta I=0)$ must plunge to a sharp minimum ($<0.05\ \mu_N^2$) caused by quantum destructive interference between time-reversed intrinsic states.
  4. **$g$-Factor Equality**:
     TDPAD measurement of gyromagnetic factors must yield $g_1 \equiv g_2$.

---

## Pattern 3: Multiple Chiral Doublets ($M\chi D$) Classification

- **Core Objective**: Classify the physical nature of two or more chiral doublet pairs in a single nucleus.
- **Classification Logic**:
  - **Test A: Parity and Alignment Differences**:
    If Pair 1 and Pair 2 have different parities (e.g. positive-parity vs negative-parity bands in $^{133}\text{Ce}$) or distinctly different single-particle alignments ($\Delta i_x \ge 4\hbar$), classify as **Type I: Multi-Configuration $M\chi D$**.
  - **Test B: Transverse Deformation Differences**:
    If both pairs have identical configurations and parities, but mean-field PES calculations reveal distinct triaxial minima (e.g. $\gamma \sim 20^\circ$ and $\gamma \sim -40^\circ$), classify as **Type II: Chiral Shape Coexistence**.
  - **Test C: Chiral Phonon Excitations**:
    If both pairs share identical configurations, alignments, and deformations, but Pair 2 lies higher in excitation energy with increased instanton tunneling width (e.g. $^{103}\text{Rh}$), classify as **Type III: Chiral Multi-Phonon Excitations**.

---

## Pattern 4: Top-on-Top Inertia Sorting and Axis Permutation Check

- **Core Rule**: In particle-plus-triaxial-rotor models, verify the convention used for principal axes:
  - In Bohr-Mottelson Vol. II Eq. (4-282), the axis permutation inadvertently assigned $\mathcal{J}_3 > \mathcal{J}_1 > \mathcal{J}_2$ instead of hydrodynamic ordering $\mathcal{J}_2 > \mathcal{J}_1 > \mathcal{J}_3$.
  - In Tanabe's top-on-top algebraic model (Ch. 4), the largest moment of inertia is properly aligned with the collective core rotation axis (the intermediate axis $m$ for $\gamma \in (0^\circ, 60^\circ)$).
  - Always verify whether hydrodynamic ($\mathcal{J} \propto \sin^2(\gamma - 2\pi k/3)$) or rigid-body moments of inertia are used; high-spin states require renormalized rigid-body moments due to Coriolis Anti-Pairing (CAP).
