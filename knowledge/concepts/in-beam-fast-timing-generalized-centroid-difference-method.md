---
type: concept
title: "In-beam electronic fast-timing generalized centroid difference (GCD) method and picosecond lifetimes"
aliases: [gcd-lifetime-method, generalized-centroid-difference, fast-timing-picosecond-lifetime, prf-walk-correction]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, fast-timing, nuclear-lifetimes, labr3-detectors, generalized-centroid-difference, prf-time-walk, transition-strengths]
---

# In-beam electronic fast-timing generalized centroid difference (GCD) method and picosecond lifetimes

## Definition and Fast-Timing Spectroscopy Challenges

Measuring nuclear excited-state lifetimes in the picosecond regime ($\tau \sim 5 - 500\text{ ps}$) provides model-independent access to reduced transition probabilities $B(E2)$ and $B(M1)$, crucial for testing triaxial quadrupole collectivity, wobbling phonon transitions, and chiral partner band structures.

While the Recoil Distance Doppler Shift (RDDS / plunger) method is standard for $\tau \ge 1\text{ ps}$, **electronic fast-timing with fast inorganic scintillators ($\text{LaBr}_3(\text{Ce})$, $\text{CeBr}_3$, $\text{BaF}_2$)** directly measures time differences between feeding ($\gamma_{\text{feed}}$) and decay ($\gamma_{\text{decay}}$) transitions.

However, traditional prompt centroid shift methods suffer from:
1. **Prompt Response Function (PRF) Time Walk**:
   Pulse rise-time variations and PMT transit-time dispersion cause the prompt timing centroid to vary strongly with $\gamma$-ray energy:
   $$\text{PRF}(E_\gamma) = \frac{a_0}{\sqrt{E_\gamma}} + c_0 E_\gamma + d_0$$
   For $\text{LaBr}_3(\text{Ce})$, $a_0 \approx 450\text{ ps}\cdot\text{keV}^{1/2}, c_0 \approx -0.02\text{ ps/keV}$. Energy walk can introduce spurious delays of $10 - 50\text{ ps}$!
2. **Absolute Time Zero Drift**:
   Electronic temperature variations induce drift in the absolute zero-time delay.

Based on J.-M. Régis et al. (Nucl. Instrum. Methods A 606, 466, 2009; NIM A 726, 191, 2013), 吴治华《原子核物理实验方法》第 9, 14 章, and 汪晓莲等《粒子探测技术》第 8 章:
The **Generalized Centroid Difference (GCD)** method eliminates both absolute zero drift and prompt walk offsets.

---

## The Generalized Centroid Difference (GCD) Formalism

In a calibrated symmetric $\gamma-\gamma-t$ coincidence matrix, two complementary time spectra are gated for the cascade $\gamma_{\text{feed}}(E_1) \to \text{Level}(\tau) \to \gamma_{\text{decay}}(E_2)$:

1. **Forward Centroid $C_1(E_1, E_2)$**:
   Gate start on feeding transition $E_1$, stop on decay transition $E_2$:
   $$C_1 = \Delta\text{PRF}(E_1, E_2) + \tau + T_{\text{offset}}$$
2. **Reverse Centroid $C_2(E_2, E_1)$**:
   Gate start on decay transition $E_2$, stop on feeding transition $E_1$:
   $$C_2 = -\Delta\text{PRF}(E_1, E_2) - \tau + T_{\text{offset}}$$
3. **Centroid Difference $\Delta C$**:
   Subtracting the two symmetric centroids strictly cancels the arbitrary electronic offset $T_{\text{offset}}$:
   $$\Delta C = C_1 - C_2 = 2 \tau + 2 \left[ \text{PRF}(E_1) - \text{PRF}(E_2) \right]$$
4. **Lifetime Inversion Formula**:
   $$\tau = \frac{\Delta C - 2 \Delta\text{PRF}(E_1, E_2)}{2}$$
   with propagated experimental uncertainty:
   $$\sigma_\tau = \frac{1}{2} \sqrt{\sigma_{C1}^2 + \sigma_{C2}^2 + 4 \sigma_{\text{walk}}^2}$$

This enables extracting lifetimes down to $\tau \approx 5 - 10\text{ ps}$ with sub-picosecond statistical precision!

---

## Transition Probability Inversion

From the extracted level lifetime $\tau$:
$$T_{\text{total}} = \frac{1}{\tau (1 + \alpha_{\text{tot}})}$$
$$T(M1) = \frac{T_{\text{total}}}{1 + \delta^2}, \quad T(E2) = \frac{T_{\text{total}} \delta^2}{1 + \delta^2}$$
Evaluating in Weisskopf single-particle units (W.u.):
$$B(M1) [\text{W.u.}] = \frac{T(M1)}{3.15 \times 10^{13} E_\gamma^3 [\text{MeV}^3]}, \quad B(E2) [\text{W.u.}] = \frac{T(E2)}{1.22 \times 10^9 A^{4/3} E_\gamma^5 [\text{MeV}^5]}$$

---

## Canonical Experimental Benchmarks

1. **$^{134}\text{Ce}$ $2_1^+$ State Lifetime ($4_1^+ 638\text{ keV} \to 2_1^+ \to 0^+ 409\text{ keV}$)**:
   - $\Delta\text{PRF}(638, 409) = -9.02\text{ ps}$;
   - Measured centroids $C_1 = +75.4\text{ ps}, C_2 = -72.6\text{ ps} \implies \Delta C = 148.0 \pm 2.5\text{ ps}$;
   - Extracted lifetime: $\tau = [148.0 - 2(-9.02)] / 2 = 83.0 \pm 1.3\text{ ps}$, matching the literature value ($\tau_{\text{lit}} \approx 62 - 85\text{ ps}$).
2. **$^{60}\text{Co}$ Prompt Calibration**:
   - Cascade $1173.2\text{ keV} \to 1332.5\text{ keV}$ ($\tau \approx 1\text{ ps}$ prompt):
   - Correctly reproduces $\tau \approx 0\text{ ps}$ within $\pm 0.5\text{ ps}$ error.

---

## Primary Source References

- **Régis, J.-M. et al.**: *The generalized centroid difference method for picosecond lifetime measurements with fast-timing detector arrays*, Nucl. Instrum. Methods Phys. Res. A 726, 191–202 (2013).
- **Régis, J.-M. et al.**: *Picosecond lifetime measurements with LaBr3(Ce) detectors*, Nucl. Instrum. Methods Phys. Res. A 606, 466–474 (2009).
- **Wu Zhihua (吴治华)**: *Methods of Nuclear Physics Experiments* (《原子核物理实验方法》), Fudan University Press (1995), Chapters 9 & 14.
- **Mach, H. et al.**: *Subnanosecond lifetime measurements in nuclear spectroscopy*, Nucl. Instrum. Methods Phys. Res. A 280, 49–70 (1989).
