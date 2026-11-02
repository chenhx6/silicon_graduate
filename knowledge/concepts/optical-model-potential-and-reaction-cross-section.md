---
type: concept
title: "Nuclear optical model potential (OMP), S-matrix transmission and reaction cross sections"
aliases: [optical-model-potential, omp-reaction-cross-section, s-matrix-transmission, eikonal-absorption-cross-section]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [optical-model, woods-saxon, reaction-cross-section, s-matrix, eikonal-approximation, compound-nucleus-absorption, direct-reactions]
---

# Nuclear optical model potential (OMP), S-matrix transmission and reaction cross sections

## Definition

In low- and intermediate-energy nuclear physics, nuclear collisions (nucleons, deuterons, $\alpha$ particles, and heavy ions) simultaneously undergo elastic scattering and flux absorption into non-elastic channels (inelastic excitation, nucleon transfer, and compound nucleus fusion). The **Optical Model of the Nucleus** (Feshbach, Porter, Weisskopf 1954; Bertulani 2021 Ch. 3; 卢希庭 2000 第 9 章 §9.3) treats the target nucleus as a cloudy crystal ball using a complex effective potential:
$$U(r) = - V_0 f_v(r) - i W_0 f_w(r) - i 4 a_s W_s \left[ -\frac{d}{dr} f_s(r) \right] + V_C(r)$$
where $f_i(r) = [1 + \exp((r - R_i)/a_i)]^{-1}$ is the Woods-Saxon form factor with nuclear radius $R_i = r_{0i} A_{\text{target}}^{1/3}$ and surface diffuseness $a_i \approx 0.65\text{ fm}$.
- **Real Potential $V_0$** ($\sim 40 - 55\text{ MeV}$): Refracts the incident de Broglie wave, determining the shape and diffraction oscillations of the elastic angular distribution;
- **Imaginary Volume Potential $W_0$** ($\sim 10 - 20\text{ MeV}$): Absorbs flux in central collisions ($b < R$), modeling transitions into complex compound nucleus configurations;
- **Imaginary Surface Potential $W_s$** ($\sim 3 - 10\text{ MeV}$): Concentrates absorption in peripheral collisions ($b \approx R$), modeling direct transfer and collective inelastic excitations.

In the semiclassical eikonal / WKB approximation, the phase shift along an impact parameter trajectory $b$ is:
$$\chi(b) = -\frac{1}{\hbar v} \int_{-\infty}^{\infty} U(\sqrt{b^2 + z^2}) dz$$
The imaginary part $\text{Im}[\chi(b)]$ governs the attenuation of probability flux. The partial wave $S$-matrix transmission probability is:
$$T(b) = 1 - |\eta(b)|^2 = 1 - \exp[-2 \text{Im}(\chi(b))]$$
Integrating over all impact parameters $b$ (or summing over partial waves $\ell = k b$) yields the **total reaction cross section**:
$$\sigma_R = 2\pi \int_0^\infty b T(b) db = \frac{\pi}{k^2} \sum_{\ell=0}^{\ell_{\text{max}}} (2\ell + 1) (1 - |\eta_\ell|^2)$$

## Necessary Assumptions

1. **Semiclassical Eikonal Approximation**: The wavelength $\lambda = 1/k$ is smaller than the potential range ($k R \gg 1$), validating straight-line trajectory integration.
2. **Spherical Central Potential**: The target nucleus is treated in its spherical ground state; rotational or vibrational coupling is incorporated as an effective imaginary absorption potential $W(r)$.

## Discriminating Observables

1. **Impact Parameter Transmission Profile $T(b)$**:
   - $T(b) \approx 1.0$ for central collisions ($b \ll R$): The nucleus behaves as a black disc absorbing nearly all incoming flux;
   - $T(b)$ drops smoothly to zero across the nuclear surface region ($b \approx R \pm 2a$).
2. **Total Reaction Cross Section $\sigma_R$ Magnitude**:
   $\sigma_R$ scales with the geometric area $\pi (R_{\text{target}} + a)^2 \sim 1000\text{ mb}$ for $A \sim 60$ targets at $E \sim 40\text{ MeV}$.
3. **Nuclear Opacity Ratio**:
   The ratio $\sigma_R / [\pi (R+a)^2] \approx 1.0 - 1.2$ measures the total absorptive opacity of the nuclear medium.

## Supporting Evidence

1. **$40\text{ MeV}$ Proton on $^{58}\text{Ni}$ Benchmark ($Z_t=28, A_t=58, E_{\text{lab}}=40\text{ MeV}$)**:
   - $R_{\text{target}} = 4.84\text{ fm}, a = 0.65\text{ fm}$;
   - Real potential $V_0 = 45.0\text{ MeV}$, volume $W_0 = 10.0\text{ MeV}$, surface $W_s = 3.0\text{ MeV}$;
   - Semiclassical WKB reaction cross section: $\sigma_R = 1093.9\text{ mb}$;
   - Geometric scale $\pi(R+a)^2 = 946.4\text{ mb}$, nuclear opacity ratio $= 1.156$;
   - Central transmission: $T(b=0.03\text{ fm}) = 0.9795 \approx 1.0$; peripheral transmission: $T(b=7.23\text{ fm}) = 0.1003$.
2. **Heavy-Ion Optical Potential Benchmark ($^{16}\text{O} + {}^{208}\text{Pb}$ at $90\text{ MeV}$)**:
   - Strong surface absorption reproduces the rapid drop in elastic scattering beyond the grazing angle $\theta_{\text{graz}}$.

## Counter-evidence and Competing Interpretations

1. **Microscopic Folding Potentials vs Phenomenological Woods-Saxon**:
   Phenomenological Woods-Saxon potentials adjust parameters ($V_0, W_0, r_0, a$) to fit experimental data. Microscopic double-folding models fold realistic nucleon-nucleon interactions (e.g. DDM3Y or Gogny) with self-consistent Hartree-Fock matter densities, eliminating free geometry parameters.
2. **Threshold Anomalies in Weakly Bound Nuclei**:
   Near the Coulomb barrier in reactions with halo or weakly bound nuclei (e.g. $^{6}\text{Li}, ^{11}\text{Be}$), breakup channels generate a large repulsive polarization potential that modifies the energy dependence of $V(E)$ and $W(E)$ (the breakup threshold anomaly).

## Our Current Position

In this wiki, complex Optical Model Potentials (OMP), S-matrix transmission probabilities $T(b)$, and total reaction cross sections $\sigma_R$ are calculated using Module 106 (`optical_model_potential_reaction_cross_section_calculator.py`, CLI subcommand `omp`). The module integrates Woods-Saxon volume and surface derivative absorptive potentials along semiclassical eikonal trajectories, validating reaction cross sections against global evaluated systematics.

## Sources

- [[book-bertulani-nuclear-reactions]]: C. A. Bertulani and P. Danielewicz, *Introduction to Nuclear Reactions*, CRC Press (2021), Ch. 3 (The Optical Model, pp. 65–115).
- [[book-lu-nuclear-physics-chinese]]: 卢希庭, 江栋兴, 叶沿林, 《原子核物理（修订版）》, 原子能出版社 (2000), 第9章 原子核反应 §9.3 (光学模型, 印刷 pp. 248–254 / PDF pp. 258–264).
- [[book-lin-heavy-ion-reactions]]: 林承键, 《重离子核反应》, 科学出版社 (2017), 第2章 (重离子相互作用势).
- Feshbach, H., Porter, C. E., Weisskopf, V. F., *Model for nuclear reactions with neutrons*, Phys. Rev. 96, 448 (1954).
