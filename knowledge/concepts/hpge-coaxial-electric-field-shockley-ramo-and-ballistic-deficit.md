---
type: concept
title: "HPGe coaxial detector electric field, Shockley-Ramo pulse formation and ballistic deficit"
aliases: [hpge-coaxial-electric-field, shockley-ramo-charge-collection, ballistic-deficit-hpge, hpge-neutron-radiation-damage]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [hpge-detectors, electric-field, depletion-voltage, shockley-ramo, ballistic-deficit, trapezoidal-filter, radiation-damage, in-beam-spectroscopy]
---

# HPGe coaxial detector electric field, Shockley-Ramo pulse formation and ballistic deficit

## Definition

In high-resolution in-beam $\gamma$-ray spectroscopy, High-Purity Germanium (HPGe) detectors operate as reverse-biased semiconductor diodes at liquid nitrogen temperatures ($77\text{ K}$, $\varepsilon_r = 16.0$). In a true coaxial or closed-end coaxial geometry with inner core contact radius $r_1$ and outer contact radius $r_2$, the fundamental detector physics comprises four interrelated mechanisms:

1. **Space Charge & Depletion Voltage $V_{\text{dep}}$**:
   Uncompensated residual impurities (net concentration $|N_A - N_D| \sim 10^9 - 10^{10}\text{ cm}^{-3}$) establish an unneutralized space charge density $\rho = e |N_A - N_D|$. Full depletion across the active volume requires an applied reverse bias exceeding the depletion voltage:
   $$V_{\text{dep}} = \frac{e |N_A - N_D|}{2\varepsilon} \left[ r_2^2 \ln\left(\frac{r_2}{r_1}\right) - \frac{1}{2}(r_2^2 - r_1^2) \right]$$
   where $\varepsilon = \varepsilon_r \varepsilon_0$. Operational overbiasing ($V_{\text{bias}} \approx 1.3 - 2.0 \times V_{\text{dep}}$) ensures the electric field $E(r) \ge 10^3\text{ V/cm}$ everywhere in the crystal, driving both electrons and holes into the drift velocity saturation regime ($v_s \approx 1.0 \times 10^7\text{ cm/s} = 10^5\text{ m/s}$).

2. **Shockley-Ramo Theorem & Pulse Formation**:
   The instantaneous current $i(t)$ induced on the readout electrode by a carrier moving with velocity $\vec{v}(r)$ is governed by the Shockley-Ramo theorem:
   $$i(t) = q \vec{v}(r(t)) \cdot \vec{E}_w(r(t))$$
   where $\vec{E}_w(r) = \frac{1}{\ln(r_2/r_1)} \frac{1}{r}$ is the dimensionless weighting electric field for coaxial geometry.
   Because $E_w(r) \propto 1/r$, the induced charge rises steeply only when the carrier approaches the central electrode $r_1$.

3. **Charge Collection Time & Ballistic Deficit**:
   For a $\gamma$ interaction at radius $r_0$, the total charge collection time is:
   $$t_c(r_0) = \max(t_e(r_0), t_h(r_0))$$
   with maximum collection time across the crystal:
   $$t_{c,\text{max}} = \frac{r_2 - r_1}{v_s} \approx 200 - 400\text{ ns}$$
   In conventional analog shaping amplifiers (CR-(RC)$^4$ / semi-Gaussian) with peaking time $\tau$, the finite and position-dependent collection time causes an amplitude attenuation known as **ballistic deficit**:
   $$\text{Deficit}_{\text{Gaussian}} \approx \frac{1}{12} \left( \frac{t_c}{\tau} \right)^2$$
   In digital signal processing (DSP) using a **digital trapezoidal filter** (Jordanov algorithm; Nakhostin 2020 Ch. 10), providing a flat-top duration $T_{\text{flat}} \ge t_{c,\text{max}}$ ensures that the peak sampling window encompasses all moving charges, achieving **exact zero ballistic deficit**:
   $$\text{Deficit}_{\text{Trapezoidal}} = 0.0 \quad (\text{when } T_{\text{flat}} \ge t_{c,\text{max}})$$

4. **P-Type vs N-Type Fast Neutron Radiation Hardness**:
   Fast neutrons ($E_n > 1\text{ MeV}$) from heavy-ion reactions create Frenkel defects and vacancy cluster cascades that act predominantly as **hole traps**.
   - In P-type HPGe: Holes must drift across the large radius toward the core; hole trapping causes severe low-energy peak tailing and FWHM loss at fluences $\Phi_n \ge 10^9\text{ n/cm}^2$.
   - In N-type (reverse electrode) HPGe: Holes created near the outer surface only drift a very short distance to the outer cathode, making N-type detectors $10 - 20\times$ more radiation-hard ($\Phi_n \sim 1 - 2 \times 10^{10}\text{ n/cm}^2$).

## Necessary Assumptions

1. **Isothermal Saturated Carrier Transport**: The crystal is cooled to $77\text{ K}$; electric field $E(r) \ge 10^3\text{ V/cm}$ across the active volume, fixing electron and hole drift velocities at $v_s \approx 10^5\text{ m/s}$.
2. **True Coaxial Cylindrical Boundary**: Edge effects from the closed-end bullet shape (hemispherical front face) are neglected in the mid-plane analytical approximation.
3. **Point-Like Photoelectric Conversion**: High-energy Compton scattering cascades are approximated by localized primary interaction centroids $r_0$.

## Discriminating Observables

1. **Overbias Ratio and Peak Shape**:
   Operating below $V_{\text{dep}}$ leaves an undepleted dead layer; operating with $V_{\text{dep}} \le V_{\text{bias}} < 1.3 V_{\text{dep}}$ leaves low-field regions near $r_2$ where $v(E) < v_s$, increasing collection time and worsening energy resolution.
2. **Trapezoidal Filter Flat-Top Optimization**:
   As $T_{\text{flat}}$ increases from $100\text{ ns}$ to $800\text{ ns}$, the energy resolution of high-energy $\gamma$ peaks improves monotonically until plateauing at $T_{\text{flat}} \approx t_{c,\text{max}}$, verifying the elimination of ballistic deficit.
3. **Neutron Tailing Asymmetry ($FW.1M / FWHM$)**:
   In irradiated p-type detectors, the ratio of full-width-at-tenth-maximum ($FW.1M$) to $FWHM$ increases from the ideal Gaussian $1.82$ up to $> 2.5$ due to exponential hole trapping. N-type detectors retain symmetric peak shapes ($FW.1M/FWHM < 2.0$) under the same fluence.

## Supporting Evidence

1. **Standard Coaxial P-Type HPGe Benchmark ($r_1=5\text{ mm}, r_2=35\text{ mm}, |N_A - N_D| = 3 \times 10^9\text{ cm}^{-3}$)**:
   - Depletion voltage $V_{\text{dep}} = 3026.0\text{ V}$;
   - At $V_{\text{bias}} = 4000\text{ V}$ (overbias ratio $1.32$): $E(r_1) = 3150\text{ V/cm}$, $E_{\text{mid}} = 1106\text{ V/cm}$, $E(r_2) = 1032\text{ V/cm} \ge 1000\text{ V/cm}$;
   - Velocity saturation verified throughout $100\%$ of active volume.
2. **Shockley-Ramo Collection Time**:
   - For interaction at $r_0 = 25\text{ mm}$: $t_e = 200\text{ ns}, t_h = 100\text{ ns}, t_c = 200\text{ ns}$;
   - Maximum collection time $t_{c,\text{max}} = (35 - 5)\text{ mm} / 10^5\text{ m/s} = 300\text{ ns}$.
3. **Ballistic Deficit Reconciliation**:
   - Analog Gaussian shaper ($\tau = 2\ \mu\text{s}$): deficit is $0.0833\%$;
   - Digital trapezoidal filter ($T_{\text{flat}} = 800\text{ ns} > 300\text{ ns}$): deficit is exactly $0.0000\%$.
4. **Neutron Damage Thresholds**:
   - At $\Phi_n = 2.0 \times 10^9\text{ n/cm}^2$: P-type shows severe low-energy tailing requiring thermal annealing; N-type shows negligible resolution loss.

## Counter-evidence and Competing Interpretations

1. **Wu Zhihua vs Wang Xiaolian Textbook Conflict Reconciliation**:
   - Wu Zhihua (2005 Ch. 5) focuses on nuclear spectroscopy and pulse signal chains, highlighting N-type HPGe for in-beam neutron environments; Wang Xiaolian (2009 Ch. 5) focuses on high-energy particle physics calorimeters and tracking arrays where radiation damage mechanisms include surface leakage and high flux hadron showers.
   - The two textbooks do not present a theoretical contradiction; they describe the same underlying Shockley-Ramo and Frenkel defect physics tailored to different experimental facilities.
2. **Electronic Noise vs Ballistic Deficit Trade-Off**:
   Increasing flat-top $T_{\text{flat}}$ eliminates ballistic deficit, but broadens the filter weighting function, slightly increasing series electronic noise (thermal preamplifier FET noise). In experimental tuning, $T_{\text{flat}}$ is set to the minimum value satisfying $T_{\text{flat}} \approx t_{c,\text{max}}$.

## Our Current Position

In this wiki, HPGe detector coaxial fields, depletion conditions, Shockley-Ramo collection times, ballistic deficits, and fast-neutron damage reconciliation are computed using Module 98 (`hpge_coaxial_electric_field_ballistic_deficit_calculator.py`, CLI subcommand `hpgefield`). For in-beam heavy-ion experiments, N-type reverse-electrode coaxial detectors combined with digital trapezoidal filtering ($T_{\text{flat}} \ge 300\text{ ns}$) are adopted as the standard configuration.

## Sources

- [[book-wu-nuclear-experiment-methods]]: 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第5章 半导体探测器, 印刷 pp. 135–150 / PDF pp. 143–158.
- [[book-wang-particle-detection]]: 汪晓莲, 李澄, 绍明, 陈宏芳, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第5章 半导体探测器, 印刷 pp. 180–225 / PDF pp. 194–239.
- [[book-nakhostin-signal-processing-detectors]]: M. Nakhostin (吴鸿毅译), 《辐射探测器信号处理》, 科学出版社 (2020), 第1章 感应电荷脉冲与Shockley-Ramo定理 & 第4章 脉冲成形与弹道亏损.
