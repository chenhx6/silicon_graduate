# Cheatsheet: Chirality & Wobbling Fast-Check Cards

Decision matrices, analytic formulas, and experimental diagnostic thresholds from *Chirality and Wobbling in Atomic Nuclei* (CRC Press, 2025).

---

## 1. Fast Arbitration Matrix: Wobbling vs Signature Partner (TiP) vs Chirality

| Observable | Genuine Wobbling (TW) | Unfavored Signature Partner (TiP) | Chiral Doublet Bands | $\gamma$-Vibrational Coupling |
|---|---|---|---|---|
| **Band Energy $\Delta E(I)$** | $\Delta I = 1$ band, $\hbar\omega_w$ decreases with $I$ | $\Delta I = 1$ band, normal signature splitting | $\Delta I = 1$ doublet, near-degenerate ($\Delta E < 100\text{ keV}$) | $\Delta I = 1$ or 2 bandhead near core $2_2^+$ |
| **Connecting Transition** | Strong collective $E2$ ($f_{E2} > 70\%$) | $M1$-dominated ($f_{M1} > 75\%$) | Interband $M1/E2$ with $S_{M1}(I)$ in-phase | High-energy transitions ($E_\gamma \sim 1\text{ MeV}$) |
| **Multipole Ratio $|\delta|$** | Large ($|\delta| \ge 1.5$) | Small ($|\delta| \le 0.5$) | Moderate ($|\delta| \sim 0.3 - 1.0$) | Small to moderate |
| **Linear Polarization $P$** | **Positive ($P > 0$)** | **Negative ($P < 0$)** | Dependent on multipolarity | Varies by multipole order |
| **$B(E2)_{\text{inter}}/B(E2)_{\text{intra}}$** | **Collective ($0.20 - 0.50$)** | **Suppressed ($\le 0.05$)** | Small interband ($< 0.10$) | Moderate ($0.05 - 0.20$) |
| **Interband $B(M1; \Delta I=0)$** | Negligible ($\ll 0.05\ \mu_N^2$) | Single-particle order ($\sim 0.1 - 0.5$) | **Vanishing minimum ($<0.05\ \mu_N^2$)** | Single-particle order |
| **Gyromagnetic Ratio $g$** | Different from ground state | Different from ground state | **Strictly equal ($g_1 \equiv g_2$)** | Distinct from ground state |

---

## 2. Harmonic Wobbling Frequencies (Frauendorf & Tanabe)

### Even-Even Triaxial Rotor (Bohr-Mottelson / Davydov):
$$\hbar\omega_w = I \sqrt{\left(\frac{1}{\mathcal{J}_x} - \frac{1}{\mathcal{J}_z}\right)\left(\frac{1}{\mathcal{J}_y} - \frac{1}{\mathcal{J}_z}\right)}, \quad \mathcal{J}_z > \mathcal{J}_x, \mathcal{J}_y.$$

### Transverse Wobbling in Odd-$A$ Nuclei (Particle along $x$, Core rotating around $z$):
$$\hbar\omega_w = 2 I \sqrt{\left(\frac{1}{2\mathcal{J}_x} - \frac{1}{2\mathcal{J}_z} + \frac{j}{2 I \mathcal{J}_x}\right) \left(\frac{1}{2\mathcal{J}_y} - \frac{1}{2\mathcal{J}_z}\right)}.$$
As $I$ increases, the term $j/(2 I \mathcal{J}_x)$ decreases, driving the monotonic drop of $\hbar\omega_w$ ($d\hbar\omega_w / dI < 0$).

---

## 3. Directional Angular Distribution & Linear Polarization Equations

### Quadratic Dual-Root Inversion:
$$(R_{22} - a_2) \delta^2 + 2 R_{12} \delta + (R_{20} - a_2) = 0.$$
- Root 1 (Wobbling candidate): $\delta_1 = \frac{-R_{12} - \sqrt{R_{12}^2 - (R_{22}-a_2)(R_{20}-a_2)}}{R_{22}-a_2}$;
- Root 2 (Signature partner): $\delta_2 = \frac{-R_{12} + \sqrt{R_{12}^2 - (R_{22}-a_2)(R_{20}-a_2)}}{R_{22}-a_2}$.

### Clover Compton Linear Polarization Asymmetry:
$$P(\delta) = \frac{3 \delta^2 R_{22} - 2\sqrt{6} \delta R_{12} - R_{20}}{(2 - \delta^2) R_{20} + 1 + \delta^2}.$$
- Measured asymmetry: $P_{\text{exp}} = \frac{1}{Q(E_\gamma)} \frac{N_\perp - a_{\text{geo}} N_\parallel}{N_\perp + a_{\text{geo}} N_\parallel}$.

---

## 4. Benchmark Case Ledger

| Nucleus | Mode Status | Primary Falsifier or Confirmation |
|---|---|---|
| $^{135}\text{Pr}$ | **Falsified Wobbling $\to$ TiP Confirmed** | Gammasphere $a_2=-0.42$ degenerate; JUROGAM II $P=-0.21(4)$ rejects wobbling at $11.1\sigma$ ($81.9\%\ M1$). |
| $^{135}\text{Nd}$ | **Chiral Doublet Confirmed** | $100\%$ in-phase $S_{M1}(I)$ staggering, interband $M1$ vanishing minimum $0.040\ \mu_N^2$ at $39/2^-$. |
| $^{134}\text{Pr}$ | **Chiral Doublet Confirmed** | GASP RDDS/DSAM lifetimes: $100\%$ in-phase $S_{M1}$, interband $M1$ minimum $0.030\ \mu_N^2$ at $13^+$. |
| $^{131}\text{Ce}$ | **$\gamma$-Vibrational Coupling** | Mid-shell $\nu h_{11/2}$ ($N=73$), Band 4 decays via high-energy lines ($994, 1108\text{ keV}$). |
| $^{133}\text{Ce}$ | **Falsified Wobbling $\to$ TiP Partner** | Top-shell $\nu h_{11/2}$ ($N=75$), negative wobbling frequency ($-84.5\text{ keV}$), connecting lines $76.8\% - 97.2\%\ M1$. |
| $^{128}\text{Cs}$ | **Chiral Doublet Confirmed** | TDPAD gyromagnetic ratios strictly equal: $g_1(11^+) = +0.58(4)$, $g_2(11^+) = +0.56(5)$. |
| $^{78}\text{Br}$ | **Chiral-Octupole Quartet Confirmed** | Two chiral doublets with enhanced cross-parity $E1$ network ($B(E1)/B(E2) \sim 10^{-4}\ \text{fm}^{-2}$). |
