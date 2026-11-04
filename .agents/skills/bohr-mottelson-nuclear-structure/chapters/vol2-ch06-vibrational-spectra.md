# Volume II, Chapter 6: Vibrational Spectra and Sum Rules

**Book**: *Nuclear Structure, Vol. II: Nuclear Deformations* (A. Bohr & B. R. Mottelson)
**Printed Pages**: pp. 345–560 | **Source**: `raw/books/nuclear structure Ⅱ_Bohr, Mottelson.pdf`

---

## 1. Core Frameworks and Theoretical Invariants

### 1.1 Multipole Surface Vibrations
- Nuclear radius surface multipole expansion:
  $$R(\theta, \phi) = R_0 \left[ 1 + \sum_{\lambda \ge 2} \sum_{\mu=-\lambda}^\lambda \alpha_{\lambda\mu}^* Y_{\lambda\mu}(\theta, \phi) \right].$$
- Quadrupole vibration ($\lambda = 2$):
  - $\mu = 0$: $\beta$-vibration (axially symmetric stretching);
  - $\mu = \pm 2$: $\gamma$-vibration (non-axial dynamic excursion into triaxial shapes).
- Octupole vibration ($\lambda = 3$):
  - Negative-parity phonon creating alternating-parity states ($1^-, 3^-, 5^-$) with enhanced $E1$ and $E3$ transition rates.

### 1.2 Energy-Weighted Sum Rules (EWSR)
- Model-independent sum rule for electric multipole operators:
  $$S(E\lambda) = \sum_n (E_n - E_0) B(E\lambda; 0 \to n) = \frac{\hbar^2}{2M} \frac{\lambda (2\lambda+1)^2}{4\pi} Z e^2 \langle r^{2\lambda-2} \rangle.$$
- **Phonon Collectivity Metric**: A single low-lying vibrational phonon exhausts a significant percentage ($10\% - 40\%$) of the EWSR, whereas single-particle states each exhaust $<1\%$.

### 1.3 Random Phase Approximation (RPA) and Effective Charges
- Particle-hole and quasiparticle pair creation/annihilation operators:
  $$Q_\nu^\dagger = \sum_{p h} (X_{ph}^\nu a_p^\dagger a_h - Y_{ph}^\nu a_h^\dagger a_p).$$
- Core polarization induces an effective charge for valence nucleons:
  $$e_{\text{eff}} = e_{\text{bare}} + \delta e_{\text{pol}}, \quad e_{\text{eff}}(p) \a1.5 e, \quad e_{\text{eff}}(n) \a0.5 e.$$

---

## 2. Experimental Diagnostic Rules

1. Coulomb excitation cross sections directly measure the absolute $B(E\lambda; 0^+ \to \lambda^\pi)$ transition probability, establishing whether the state exhausts the collective EWSR fraction.
2. In transitional nuclei, the ratio of the $\gamma$-bandhead energy to the first $2_1^+$ state, $E(2_2^+) / E(2_1^+)$, serves as an indicator of the transition from spherical vibrator ($\sim 2$) to deformed rotor ($\gg 2$) or $\gamma$-soft triaxial nucleus ($\approx 2.0 - 2.5$).
