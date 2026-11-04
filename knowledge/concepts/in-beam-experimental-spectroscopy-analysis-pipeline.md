---
type: concept
title: "In-beam experimental nuclear spectroscopy master data analysis pipeline"
aliases: [in-beam-spectroscopy-pipeline, in-beam-analysis-workbench, experimental-spectroscopy-workflow, nuclear-data-reduction-pipeline]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, analysis-pipeline, heavy-ion-fusion, doppler-correction, dco-ratio, dsam-lifetimes, wobbling, chirality]
---

# In-beam experimental nuclear spectroscopy master data analysis pipeline

## Definition

In-beam $\gamma$-ray spectroscopy of excited nuclear states involves an intricate, multi-stage physical reduction pipeline bridging detector observables to collective-model diagnostics. The repository implementation is a demonstration and source-summary replay chain: its presets do not replace raw event sorting, detector-response calibration, feeding treatment, or a paper-level evidence review.

1. **Stage 1: Reaction Entrance Kinematics & Evaporation Residue Planning**:
   Calculates center-of-mass energy $E_{\text{cm}}$, Coulomb barrier $V_{B0}$, Wong barrier penetration cross section $\sigma_{\text{fus}}^{\text{Wong}}$, and $xn$ residue optimal excitation energy windows (Module 99).
2. **Stage 2: Relativistic Doppler Shift & Peak Broadening Budget**:
   Applies full relativistic Doppler transformation $E_{\text{lab}}(\theta) = E_0 \frac{\sqrt{1-\beta^2}}{1-\beta\cos\theta}$ and evaluates peak line broadening contributions from detector opening angle $\Delta\theta$ (peaks at $90^\circ$), recoil velocity dispersion $\Delta\beta$ (peaks at $0^\circ/180^\circ$), and isotropic neutron evaporation kicks $\Delta\theta_R$ (Module 107).
3. **Stage 3: Directional Angular Distribution & Multipole Mixing Ratio $\delta(E2/M1)$ Dual Roots**:
   Calculates algebraic Yamazaki / Biedenharn-Rose $F$-coefficients without numerical lookup tables, and solves the quadratic equation for $a_2$ returning both mathematically degenerate real roots $\delta_1$ and $\delta_2$ without subjective bias (Module 93).
4. **Stage 4: Nuclear Lifetime Inversion (DSAM / RDDS)**:
   Inverts picosecond excited state lifetimes $\tau$ from measured Doppler attenuation factors $F(\tau)$ using LSS stopping powers and Blaugrund multiple scattering integration (Module 100), or from RDDS plunger distance curves using the Differential Decay Curve Method (DDCM, Module 65).
5. **Stage 5: Transition Probabilities & Collective Deformation**:
   Converts level lifetimes $\tau$ and branching ratios into absolute reduced transition probabilities $B(E2)$ and $B(M1)$, transition quadrupole moments $Q_t$, and quadrupole deformation parameters $\beta_2$, evaluating Grodzins product rule scaling $\mathcal{G}$ and superfluid pairing reductions (Module 104).
6. **Stage 6: Physical Mode Diagnostics & Statistical Boundaries**:
   - **Wobbling Diagnostic**: Audits whether the inter-band linking transition is $E2$-dominated ($|\delta| \gg 1$), calculates the transverse wobbling frequency slope $d\omega/dI < 0$, and tests Elena Lawrie's 7-dimensional TiP vs wobbling criteria (Module 96);
   - **Chiral Doublet Diagnostic**: Evaluates twin band energy splittings $\Delta E(I) \to 0$, $B(M1)/B(E2)$ odd-even staggering, and 3D aplanarity volume metrics $\mathcal{V}_{\text{chiral}}$ (Module 96);
   - **Low-Count Physical Boundaries**: When peak counts are sparse ($n \le 15$), computes exact Feldman-Cousins unified confidence intervals (Module 97), preventing unphysical negative signal estimates.

## Necessary Assumptions

1. **Sequential Independence of Calibration Stages**: Instrumental response (Doppler, efficiency, and timing walk) is calibrated prior to multipole and lifetime inversion.
2. **Compound Nucleus Statistical Evaporation**: De-excitation proceeds via statistical neutron evaporation and statistical $\gamma$ cascades before populating the discrete yrast and non-yrast bands.

## Discriminating Observables

1. **Multipole Mixing Ratio Dual Root Ambiguity**:
   Demonstrates whether a supplied $a_2$ coefficient admits two divergent conditional solutions (e.g. $|\delta_1| < 1$ with $M1$ dominance vs $|\delta_2| > 1$ with $E2$ dominance), mandating independent linear polarimetry or internal conversion measurements before physical use.
2. **Coincidence Peak FWHM Recovery**:
   Tracks supplied peak-width inputs against detector ring angle as a response-budget demonstration; it does not recover an experimental intrinsic resolution without calibrated data.
3. **Derived Demonstration JSON Receipt**:
   Intermediate kinematic variables, model inversions, and screening diagnostics are bundled into a JSON schema. The receipt is `demonstration-derived`; it is not a paper-level validation record.

## Supporting Evidence

1. **$^{135}\text{Pr}$ Source-Summary Replay Fixture**:
   - Reaction: $^{14}\text{N} + {}^{124}\text{Sn} \to {}^{138}\text{Pr}^* \to {}^{135}\text{Pr} + 3n$ at $E_{\text{lab}} = 65\text{ MeV}$;
   - Preset $726.5\text{ keV}$ ($17/2^- \to 15/2^-$) and $a_2 = -0.180$ inputs; these are source-summary replay values, not a new raw event-level measurement;
   - Stage 1 yields Wong fusion cross section $\sigma_{\text{fus}} = 840.8\text{ mb}$, $\ell_{\text{crit}} = 31\ \hbar$;
   - Stage 2 gives Doppler shifted energy $E_{\text{lab}}(90^\circ) = 726.46\text{ keV}$, peak width $\text{FWHM} = 2.39\text{ keV}$;
   - Stage 3 inverts dual roots: $\delta_1 = 0.2530$ ($94.0\%$ $M1$ dominance) and $\delta_2 = 7.0361$ ($98.0\%$ $E2$ dominance);
   - Stage 4 returns a derived DSAM lifetime $\tau = 0.6767\text{ ps}$ ($676.7\text{ fs}$) under the preset attenuation model;
   - Stage 6 retains a conditional candidate screen: the two roots remain unresolved until independent polarization, response, feeding, and source-level checks are supplied.
2. **$^{134}\text{Pr}$ Source-Summary Replay Fixture**:
   - Reaction: $^{11}\text{B} + {}^{128}\text{Te} \to {}^{139}\text{Pr}^* \to {}^{134}\text{Pr} + 5n$ at $60\text{ MeV}$;
   - Analyzes twin bands starting at $I_0 = 10^+$, testing energy splitting $\Delta E(I)$ and $B(M1)/B(E2)$ staggering.

## Counter-evidence and Competing Interpretations

1. **Side-Feeding Delay Biases in DSAM**:
   If unobserved high-spin feeder transitions have lifetimes comparable to the state of interest, the apparent attenuation factor $F_{\text{app}}$ overestimates $\tau$. Gate-from-above coincidence slicing or side-feeding deconvolution modeling (Module 21) is required when feeder lifetimes are non-negligible.
2. **Polarization Conventions**:
   Polarization asymmetries $A_{\text{pol}}$ must be matched to the exact phase convention of the $F$-coefficients (Rose-Brink vs Krane-Steffen) to prevent erroneous sign assignment for $\delta$.

## Evidence boundary

The CLI preset is `data_kind: synthetic_or_source_summary_replay`. It does not contain raw
events, detector response, peak-fit covariance, side-feeding histories, or a reproducible
joint likelihood. The $135$Pr source lineage must be read with
[[matta-2015-transverse-wobbling-135pr]], [[sensharma-2019-two-phonon-wobbling-135pr]], and
[[lv-2022-evidence-against-wobbling-135pr]]; those sources distinguish experiment, author
interpretation, model output, and later counter-evidence. Values produced by this module should
be marked `derived` or `conditional-candidate-screen`.

## Our Current Position

In this wiki, Module 109 (`in_beam_experiment_analysis_pipeline.py`, CLI subcommand
`pipeline`) is a demonstration-derived analysis chain. It combines kinematics, Doppler
broadening, DCO dual roots, DSAM lifetime inversion, deformation transforms, mode diagnostics,
and Feldman-Cousins intervals. It does not certify experimental facts, mode assignments, or
publication readiness.

## Sources

- [[book-wu-nuclear-experiment-methods]]: 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第10章 & 第15章.
- [[book-lin-heavy-ion-reactions]]: 林承键, 《重离子核反应》, 科学出版社 (2017), 第6章.
- [[book-zhu-probability-statistics-in-physics]]: 朱永生, 《实验物理中的概率和统计（第二版）》, 科学出版社 (2006), 第11章.
- [[book-petrache-chirality-and-wobbling]]: C. M. Petrache (Ed.), *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025).
