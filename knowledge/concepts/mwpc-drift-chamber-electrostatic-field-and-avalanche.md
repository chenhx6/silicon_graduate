---
type: concept
title: "MWPC and drift chamber electrostatic fields, Townsend avalanche and space-time calibration"
aliases: [mwpc-field-simulator, drift-chamber-calibration, townsend-avalanche-gain, gas-detector-conformal-field]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [detector-physics, mwpc, drift-chamber, gas-detectors, townsend-avalanche, electrostatic-field, space-time-calibration, position-sensitive-detectors]
---

# MWPC and drift chamber electrostatic fields, Townsend avalanche and space-time calibration

## Definition and Operating Principles

Position-sensitive gas detectors (Multiwire Proportional Chambers, MWPC, and Drift Chambers) provide tracking, trajectory reconstruction, and focal plane particle identification in nuclear physics spectrometers (e.g. VAMOS, PRISMA, CSR External Target, RIBLL).

Based on 汪晓莲等《粒子探测技术》第 3 章 (pp. 58–105), 吴治华《原子核物理实验方法》第 4 章, and F. Sauli (CERN 77-09, 1977):

1. **Geometry and Conformal Field Formulation**:
   An array of parallel anode wires with pitch $s$ and radius $r_0$ is centered at $y=0$ between two grounded cathode planes at $y = \pm L$. Anode wires are biased to positive high voltage $+V_0$.
   The charge per unit length on each anode wire is:
   $$\frac{q}{2\pi\varepsilon_0} = \frac{V_0}{\frac{\pi L}{s} - \ln\frac{2\pi r_0}{s}}$$
   The exact analytical potential distribution in $(x, y)$ is given by conformal mapping:
   $$V(x, y) = V_0 - \frac{q}{4\pi\varepsilon_0} \left[ \frac{2\pi L}{s} - \ln\left( 4 \left( \sin^2\frac{\pi x}{s} + \sinh^2\frac{\pi y}{s} \right) \right) \right]$$

2. **Dual-Zone Electric Field Architecture**:
   - **Near-Wire Avalanche Zone ($r \ll s$)**:
     $$E(r) = \frac{q}{2\pi\varepsilon_0 r}$$
     At the wire surface ($r = r_0 \sim 10 - 20\ \mu\text{m}$), field strength reaches $E(r_0) \sim 10^5 - 10^6\text{ V/cm}$, initiating Townsend electron multiplication;
   - **Drift Zone ($y \ge s/2$)**:
     The field becomes asymptotically uniform:
     $$E_{\text{drift}} = \frac{\pi}{s} \frac{q}{2\pi\varepsilon_0} \sim 10^3\text{ V/cm}$$
     guaranteeing saturated drift velocity $v_d$ across the chamber volume.

---

## Townsend Avalanche and Gas Multiplication Gain ($M$)

Electrons drifting into the high-field region around an anode wire undergo Townsend ionization collisions. The first Townsend ionization coefficient is:
$$\alpha(E) = A P \exp\left( -\frac{B P}{E} \right)$$
where for standard P-10 gas ($90\%\text{ Ar} + 10\%\text{ CH}_4$ at $760\text{ Torr}$), $A \approx 14.0\text{ cm}^{-1}\cdot\text{Torr}^{-1}$, $B \approx 180.0\text{ V}/(\text{cm}\cdot\text{Torr})$.

Total gas avalanche multiplication gain $M$:
$$M = \exp\left( \int_{r_0}^{r_c} \alpha(E(r)) dr \right)$$
In standard proportional mode, $M \approx 10^4 - 10^6$, providing sufficient signal amplitude without inducing destructive spark discharges.

---

## Drift Chamber Space-Time Relation $x(t)$ & Diffusion Limit

Under saturated drift velocity ($v_d \approx 5.0\text{ cm}/\mu\text{s} = 50\ \mu\text{m/ns}$):
$$t_{\text{drift}}(x) = \frac{x}{v_d}$$
Thermal diffusion sets the fundamental spatial resolution limit:
$$\sigma_x = \sqrt{2 D t_{\text{drift}}} = \sqrt{\frac{2 D x}{v_d}} \propto \sqrt{x}$$
where diffusion coefficient $D \approx 100 - 150\ \mu\text{m}^2/\text{ns}$.
For typical $10\text{ mm}$ drift distance, $\sigma_x \approx 120 - 150\ \mu\text{m}$, enabling sub-millimeter trajectory tracking for heavy ions!

---

## Canonical Experimental Benchmarks

1. **Standard MWPC with P-10 Gas ($s = 2.0\text{ mm}, L = 5.0\text{ mm}, r_0 = 10\ \mu\text{m}, V_0 = 2600\text{ V}$)**:
   - Surface field $E(r_0) = 2.30 \times 10^5\text{ V/cm}$, drift field $E_{\text{drift}} = 3610\text{ V/cm}$;
   - Avalanche boundary $r_c = 155.3\ \mu\text{m}$, gas gain $M = 2.55 \times 10^4$;
   - Drift time across $5\text{ mm}$ is $100.0\text{ ns}$ with diffusion width $\sigma_x = 154.9\ \mu\text{m}$.
2. **High-Gain Ar-Isobutane MWPC ($V_0 = 3200\text{ V}$)**:
   - Gas gain $M = 3.90 \times 10^4$, drift field $3970\text{ V/cm}$.

---

## Primary Source References

- **Wang Xiaolian (汪晓莲) et al.**: *Particle Detection Technology* (《粒子探测技术》), USTC Press (2009), Chapter 3 (Gas Detector Physics), pp. 58–105.
- **Wu Zhihua (吴治华)**: *Methods of Nuclear Physics Experiments* (《原子核物理实验方法》), Fudan University Press (1995), Chapter 4 (Gas Ionization Detectors).
- **Sauli, F.**: *Principles of Operation of Multiwire Proportional and Drift Chambers*, CERN Report 77-09 (1977).
- **Charpak, G. et al.**: *The use of multiwire proportional counters to select and localize charged particles*, Nucl. Instrum. Methods 62, 262–268 (1968).
