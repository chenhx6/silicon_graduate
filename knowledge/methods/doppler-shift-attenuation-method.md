---
type: method
title: Doppler-shift attenuation method
aliases: [DSAM, Doppler-shifted attenuation method, Doppler-broadened line-shape analysis]
created: 2026-08-11
updated: 2026-08-11
status: ai-draft
review_status: unreviewed
method_type: nuclear-lifetime-lineshape
tags: [lifetime, doppler-shift, stopping-power, side-feeding, lineshape]
---

# Doppler-Shift Attenuation Method

## Purpose

DSAM extracts short excited-state lifetimes from the Doppler-broadened γ-ray line shape produced while recoils slow in target/backing material. Forward and backward detector angles provide complementary velocity sensitivity.

## Inputs and Assumptions

- reaction kinematics, recoil velocity histories and detector geometry;
- stopping powers and material thickness/profile;
- transition placement, contaminant peaks and detector response;
- direct and side-feeding intensities, lifetimes or effective quadrupole moments;
- branching/mixing information for conversion from lifetime to `B(E2)` or `Q_t`.

## Analysis Chain

Singh 2016 uses LINESHAPE Monte Carlo histories at `0.002-ps` time steps and fits forward/backward gated spectra simultaneously. Ziegler and shell-corrected Northcliffe–Schilling stopping powers are treated as alternative prescriptions; central values are averaged and the larger uncertainty retained.

## What It Can Establish

- source-specific mean lifetimes or limits in the line-shape sensitivity window;
- side-feeding-sensitive `Q_t` after a rotational conversion;
- angle/stopping-prescription consistency and contaminant diagnostics.

## What It Cannot Establish Alone

- intrinsic γ softness/rigidity, microscopic configuration or nuclear chirality;
- a unique lifetime if side feeding, stopping or contaminant structure is underconstrained;
- partner-band electromagnetic equality from a single measured sequence;
- direct intrinsic `Q0` without rotational-geometry assumptions.

## Known Limitations

Thick targets broaden the production-depth/velocity distribution. Stopping powers, side-feeding cascades and long feeding times can dominate the systematic budget. A line that is fully shifted or shows no significant angle-dependent shape yields only a limit or complementary RDDS bracket.

[[wang-2023-experimental-studies-nuclear-chirality-china]] adds a review-level statistical caution: the common practice of varying one nuisance parameter at a time and adding lifetime shifts in quadrature does not represent correlations, asymmetric intervals or physical limits. Its cited Bayesian/MCMC alternative is a useful method lead, not yet direct Wiki evidence, because the underlying Sun et al. 2023 analysis has not been ingested.

[[bark-2024-investigations-nuclear-chirality-ithembalabs]] describes the AFRODITE use of forward/backward line shapes and COMPA/GAMMA/SHAPE Monte Carlo histories that include slowing, feeding and statistical/collective cascades. Its `106Ag` example is secondary to the original Lieder 2014 experiment and should not substitute for that source's fit/systematic details.

[[jensen-2001-165tm-h9-2-configuration]] provides a classic Nordball DSAM example: four angle-specific γγ matrices, Au/Pb backings, Monte Carlo recoil histories, Bateman side-feeding cascades and a fitted effective `Qs` are used to obtain `Qt` for `165Tm` bands. The reported `Qt` comparison is therefore tied to the stated stopping, feeding and rotational-model assumptions.

## Sources

[[wadsworth-1977-61ni-levels]] is a historical `61Ni` DSAM example: centroid shifts at several beam energies are converted to attenuation factors/lifetimes with explicit stopping/feeding caveats.

- [[singh-2016-lifetime-131ce-133pr]]: explicit LINESHAPE/stopping/side-feeding audit for `131Ce`.
- [[li-2004-lifetimes-131ce]]: earlier `131Ce` DSAM lineage.
- [[petrache-1998-highly-deformed-lifetimes-131ce-nd]]: shared-systematics HD-band DSAM comparison.
- [[wang-2023-experimental-studies-nuclear-chirality-china]]: secondary review of DSAM uncertainty practice and pointer to correlated Bayesian/MCMC treatment.
- [[bark-2024-investigations-nuclear-chirality-ithembalabs]]: AFRODITE/COMPA-GAMMA-SHAPE overview and secondary `106Ag` line-shape counterexample.
- [[jensen-2001-165tm-h9-2-configuration]]: Nordball DSAM, `165Tm` `Qt`, side-feeding and stopping-systematics example.

## Related Methods

[[recoil-distance-doppler-shift]], [[doppler-correction]], [[transition-quadrupole-moment]].

## Evolution Log

- 2026-08-11: created from the Singh 2016 corpus on-touch audit with stopping and side-feeding boundaries explicit.
- 2026-08-11: added Wang 2023's correlated-uncertainty warning while retaining the un-ingested status of the cited Bayesian DSAM method.
- 2026-08-11: added Bark 2024's AFRODITE simulation-chain overview and original-source boundary.
