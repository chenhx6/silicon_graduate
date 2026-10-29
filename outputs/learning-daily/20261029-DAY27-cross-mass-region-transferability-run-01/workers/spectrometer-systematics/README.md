# Cross-Instrument Experimental Systematics and Methodological Pseudo-Degeneracy Analysis

This worker provides quantitative modeling and systematic error budgets across major gamma-ray spectrometer arrays (Gammasphere, Euroball III/IV, GASP, JUROGAM I/II/III, and AGATA) for Day 27 of the nuclear structure apprenticeship.

## 1. Major Spectrometer Arrays Evaluated
1. **Gammasphere:** 110 Compton-suppressed HPGe detectors in $4\pi$ spherical geometry, photopeak efficiency $9.5\%$, peak-to-total $0.59$. Compton polarimetry via planar crystals and inter-detector scattering; DSAM lineshape analysis across 37 angular rings. Typical systematic uncertainty budget: $10-15\%$.
2. **Euroball (III/IV):** Composite array with 26 Clover HPGe (4-fold) and 15 Cluster HPGe (7-fold). High polarization sensitivity ($Q(662\text{ keV}) \approx 0.22$) via Clover perpendicular/parallel scattering. Köln coincidence plunger integration for RDDS. Systematic budget: $6-10\%$.
3. **GASP:** 40 Compton-suppressed HPGe detectors plus an 80-element BGO inner ball filter. Systematic budget: $12-18\%$.
4. **JUROGAM (I/II/III):** Coupled to RITU gas-filled separator and GREAT spectrometer at focal plane. Recoil-decay tagging (RDT) provides clean background suppression. Systematic budget: $5-8\%$.
5. **AGATA:** Advanced GAmma Tracking Array, 36-fold segmented encapsulated HPGe crystals with pulse shape analysis (PSA) and gamma tracking. Spatial resolution $2-4\text{ mm}$, high Doppler correction capability for recoil velocities $v/c = 10-50\%$. Systematic budget: $3-5\%$.

## 2. Experimental Systematic Biases Modeled
### A. Polarimeter Analyzing Power and Calibration Bias
The Compton polarimeter analyzing power is:
$$Q(E_\gamma) = \frac{\alpha + 1}{\alpha^2 + \alpha + 1}, \quad \alpha = \frac{E_\gamma}{m_e c^2}$$
Linear polarization asymmetry:
$$A = \frac{N_\perp - a N_\parallel}{N_\perp + a N_\parallel} = Q \cdot P$$
where $a(E_\gamma)$ is the geometric asymmetry calibration factor.
**Case Study (Garg 2015 vs 2019 Erratum in $^{135}\text{Pr}$):**
In Garg 2015, using an uncalibrated constant $a \approx 1.0$ gave an apparent negative asymmetry $A = -0.20(8)$ for the $813.3\text{ keV}$ transition ($P \approx -1.06$), leading to a pure $M1$ shears assignment. In 2019, implementing energy-dependent calibration $a(E_\gamma) = 1.01229 + 1.171 \times 10^{-6} E_\gamma$ shifted the asymmetry to $A = +0.04(3)$ ($P \approx +0.21$), revising the multipolarity to mixed $M1+E2$.

### B. DSAM and RDDS Lifetime Systematics
1. **Stopping Power Databases:** Northcliffe-Schilling (NS) vs Ziegler-Biersack-Littmark (ZBL/SRIM). Differences of $10-15\%$ in electronic and nuclear stopping power propagate directly into extracted level lifetimes $\tau$ and transition probabilities $B(M1), B(E2)$.
2. **Side-Feeding Modeling:** Unobserved delayed cascades ($\tau_{\text{sf}} \approx 50-100\text{ fs}$) entering the highest spin states can artificially delay centroid shifts. An analyst assuming prompt feeding will erroneously infer decreasing $B(E2)$ values with spin, fabricating false antimagnetic rotation (AMR) signatures.

## 3. Methodological Pseudo-Degeneracy Matrix
The matrix (`pseudo_degeneracy_matrix.csv`) details three critical classes of pseudo-degeneracy:
- **Case 1: Large $B(M1)/B(E2)$ dipole bands:** Magnetic rotation shears vs Chiral doublets vs Strongly coupled oblate high-$K$ bands vs Octupole $E1$ bands. Key discriminant: Linear polarization sign ($P < 0$ for $M1$, $P > 0$ for $E1$) and absolute $B(E2)$ magnitude.
- **Case 2: Near-degenerate doublet bands:** True chiral vibration/rotation vs Triaxial shape coexistence vs Signature partners with anomalous decoupling vs Octupole parity doublets. Key discriminant: Persisting degeneracy over $\ge 4$ spin states, identical $Q_t$ values in both bands, and parity selection rules.
- **Case 3: Smoothly decreasing $B(E2)$ with spin:** Antimagnetic rotation (two-shears closing) vs Band termination (alignment-driven loss of collectivity) vs Side-feeding delay artifact. Key discriminant: Smoothness of dynamic moment of inertia $\mathcal{J}^{(2)}$ and independent RDDS coincidence plunger validation.

## 4. Worker Deliverables
- `spectrometer_systematics_model.py`: Computational model.
- `spectrometer_specs.csv`: Specifications and error budgets of the 5 arrays.
- `polarimeter_sensitivity.csv`: Energy-dependent analyzing power $Q(E_\gamma)$.
- `polarization_calibration_bias.csv`: Bias propagation on linear polarization $P$.
- `pr135_erratum_case_study.json`: Numerical audit of Garg 2015 vs 2019 erratum.
- `stopping_power_lifetime_systematics.csv`: Comparison of NS vs ZBL vs ICRU.
- `side_feeding_amr_simulation.csv`: Apparent $B(E2)$ distortion under delayed side feeding.
- `pseudo_degeneracy_matrix.csv`: Comprehensive diagnostic discriminant matrix.
- `spectrometer_systematics.json`: Unified structured database.
- `worker-delivery.json`: Machine-readable delivery receipt.
