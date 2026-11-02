---
type: concept
title: "In-beam relativistic Doppler broadening, finite opening angle and array resolution"
aliases: [in-beam-doppler-broadening, relativistic-doppler-shift, detector-opening-angle-broadening, agata-tracking-doppler]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, doppler-broadening, relativistic-kinematics, opening-angle, velocity-spread, agata, gammasphere, hpge-arrays]
---

# In-beam relativistic Doppler broadening, finite opening angle and array resolution

## Definition

In in-beam $\gamma$-ray spectroscopy using heavy-ion fusion-evaporation reactions, excited residual nuclei decay in flight before coming to rest in a thin target. The laboratory energy $E_{\text{lab}}$ detected at polar angle $\theta$ relative to the recoil velocity vector $\vec{\beta} = \vec{v}/c$ is governed by the relativistic Doppler transformation (吴治华 2005 第 15 章; 汪晓莲 2009 第 5 章; Nolan & Sharpey-Schafer 1979):
$$E_{\text{lab}}(\theta) = E_0 \frac{\sqrt{1 - \beta^2}}{1 - \beta \cos\theta}$$
where $E_0$ is the intrinsic unshifted $\gamma$-ray transition energy.

The total observed full-width-at-half-maximum ($\text{FWHM}_{\text{total}}$) of the in-beam peak consists of the intrinsic detector resolution added in quadrature with three kinematic Doppler broadening mechanisms:
$$\text{FWHM}_{\text{total}} = \sqrt{ \text{FWHM}_{\text{intrinsic}}^2 + (\Delta E_\theta)^2 + (\Delta E_\beta)^2 + (\Delta E_{\text{strag}})^2 }$$

1. **Finite Detector Opening Angle Broadening ($\Delta E_\theta$)**:
   A detector subtending a polar opening angle $\Delta\theta$ spans a range of Doppler shifts:
   $$\Delta E_\theta = E_0 \left[ \frac{\beta \sin\theta}{1 - \beta \cos\theta} \right] \Delta\theta_{\text{rad}}$$
   Because $\sin\theta = 1.0$ at $\theta = 90^\circ$, detector angle broadening **peaks sharply at $90^\circ$**, dominating the peak width in unsegmented HPGe rings.
2. **Recoil Velocity Spread Broadening ($\Delta E_\beta$)**:
   Dispersion in recoil velocity $\Delta\beta$ caused by finite target thickness energy loss ($dE/dx$) and reaction kinematics:
   $$\Delta E_\beta = E_0 \left| \frac{\cos\theta - \beta}{(1 - \beta \cos\theta) \sqrt{1 - \beta^2}} \right| \Delta\beta$$
   This component **peaks at forward ($0^\circ$) and backward ($180^\circ$) angles** where $|\cos\theta| = 1.0$.
3. **Neutron Evaporation Kick Recoil Straggling ($\Delta E_{\text{strag}}$)**:
   Evaporation of $x$ neutrons with thermal energy $T_n \approx 2.5\text{ MeV}$ imparts random isotropic momentum kicks $\Delta p_R \approx \sqrt{x \cdot 2 m_n T_n}$, deflecting the recoil vector by angle $\Delta\theta_R \approx \Delta p_R / (M_R \beta c)$:
   $$\Delta E_{\text{strag}} \approx E_0 \beta \sin\theta \cdot \Delta\theta_R$$

## Necessary Assumptions

1. **Unidirectional Planar Approximation**: The beam is well-collimated along the $z$-axis; target thickness is uniform across the beam spot.
2. **First-Order Small Angle Spread**: The opening angle $\Delta\theta$ and straggling deflection $\Delta\theta_R$ are small ($\Delta\theta \ll 1\text{ rad}$), validating first-order differential Taylor expansions.

## Discriminating Observables

1. **Angular Distribution of Line Widths**:
   Plotting observed peak FWHM versus detector ring angle $\theta$:
   - Standard HPGe arrays (e.g. Gammasphere with $\Delta\theta \sim 8^\circ$) exhibit a broad peak maximum at $\theta = 90^\circ$;
   - Tracking arrays (AGATA / GRETINA with pulse-shape analysis $\Delta\theta \le 1.2^\circ$) flatten the angular profile, recovering intrinsic resolution ($\text{FWHM} \sim 2.3\text{ keV}$).
2. **Target Thickness vs Energy Loss Trade-Off**:
   Thicker targets increase $\gamma$-ray yield but broaden $\Delta\beta$, setting a strict upper limit on optimal target thickness ($\sim 0.5 - 1.0\text{ mg/cm}^2$).

## Supporting Evidence

1. **$^{134}\text{Ce}$ In-Beam Thin-Target Benchmark ($E_0 = 1000\text{ keV}, \beta = 0.020, \Delta\theta = 8.0^\circ$)**:
   - At $\theta = 90^\circ$: shifted energy $E_{\text{lab}} = 999.8\text{ keV}$;
   - Opening angle broadening: $\Delta E_\theta = 2.79\text{ keV}$ (dominates over velocity spread $\Delta E_\beta = 0.04\text{ keV}$);
   - Neutron straggling ($4n$ kick): $\Delta\theta_R = 3.15^\circ \implies \Delta E_{\text{strag}} = 1.10\text{ keV}$;
   - Total observed peak width: $\text{FWHM}_{\text{total}} = 3.61\text{ keV}$ ($1.80\times$ degradation over intrinsic $2.0\text{ keV}$).
2. **AGATA Tracking Array Benchmark ($\Delta\theta = 1.2^\circ, \beta = 0.025$)**:
   - At $90^\circ$, angle broadening drops from $2.79\text{ keV}$ to $0.52\text{ keV}$;
   - Total peak width recovers to $\text{FWHM}_{\text{total}} = 2.34\text{ keV}$, verifying the revolutionary advantage of $\gamma$-ray tracking.

## Counter-evidence and Competing Interpretations

1. **Recoil Separator Tagging (RITU / VAMOS / FMA)**:
   In reactions coupled to a magnetic recoil separator or focal plane detector, the recoil velocity $\vec{\beta}$ is measured event-by-event. This eliminates the velocity spread $\Delta\beta$ and deflection $\Delta\theta_R$, leaving only the detector opening angle $\Delta\theta$ as the limiting factor.
2. **DSAM Backing Slowdown vs Thin-Target In-Flight Emission**:
   In thick-backed targets, nuclei slow down and stop before decaying, producing a continuous asymmetric Doppler lineshape (DSAM, Module 100) rather than a single shifted peak.

## Our Current Position

In this wiki, in-beam relativistic Doppler shifts, finite opening angle broadenings, and neutron evaporation straggling are calculated using Module 107 (`in_beam_doppler_broadening_array_correction_calculator.py`, CLI subcommand `doppler`). For in-beam experiment proposals, target thickness and detector ring angles are quantitatively evaluated to guarantee adequate peak-to-background ratios for candidate wobbling and chiral transitions.

## Sources

- [[book-wu-nuclear-experiment-methods]]: 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第15章 核寿命的测量 §15.2, 印刷 pp. 421–445 / PDF pp. 429–453.
- [[book-wang-particle-detection]]: 汪晓莲, 李澄, 绍明, 陈宏芳, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第5章 半导体探测器.
- Nolan, P. J., Sharpey-Schafer, J. F., *The measurement of the lifetimes of excited nuclear states using the Doppler shift attenuation method*, Rep. Prog. Phys. 42, 1 (1979).
