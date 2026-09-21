---
type: synthesis
title: "High-spin angular distributions, polarization and mixing-ratio evidence"
aliases: [高自旋角分布偏振混合比证据综合]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
scope: high-spin-angular-polarization-mixing-ratio
confidence: medium
sources: [yamazaki-1967-aligned-angular-coefficients, suffert-1959-proton-capture-polarization, lange-kumar-hamilton-1982-multipole-admixtures, droste-1996-pdco-formalism, starosta-1999-pdco-experimental-test]
tags: [high-spin, angular-distribution, polarization, mixing-ratio, evidence-map]
---

# High-spin angular distributions, polarization and mixing-ratio evidence

## Question and Scope

This synthesis compares the method and application sources in the high-spin batch. It is a method map, not a universal calibration table.

## Evidence Matrix

| Layer | What the sources establish | Main boundary |
|---|---|---|
| Formalism | Yamazaki, Rose–Brink, Taras, Hamilton and Lange define statistical tensors, angular coefficients, polarization terms and δ conventions. | Operator phase, state order and emission/absorption convention must be mapped. |
| Population | Gaussian `σ/J`, attenuation coefficients and cascade `U_k` connect alignment to `A2/A4`. | Alignment and side feeding are reaction dependent. |
| Detector | GeLi, CLOVER, Gammasphere, SeGA, BGO and AFRODITE sources calibrate `P/A/Q`, `Q(E)`, efficiency and finite geometry. | Numerical `Q`, `R_ADO` and `R_DCO` are setup specific. |
| Assignment | DCO/ADO, angular distributions and linear polarization can jointly constrain spin, parity and multipole branch. | A single observable commonly retains multiple branches. |

## Synthesis

1. The reliable unit is a joint fit of transition identity, alignment, detector response, angular distribution, polarization and convention. A quoted δ without this context is not portable.
2. Polarization adds electric/magnetic sensitivity, while angular distributions and DCO primarily constrain angular momentum and multipole combinations. Their information is complementary, not interchangeable.
3. The strongest historical sources expose failure modes: unresolved cascades, background subtraction, finite solid angle, Gaussian alignment assumptions and sign conversion.
4. Modern sources add better detectors and simulations but retain the same logical dependencies. Better resolution narrows uncertainty; it does not remove model identifiability limits.

## Model Dependence

Alignment distributions, attenuation coefficients, detector response and phase conventions are source and setup dependent. Review tables provide transfer rules but do not replace a matched calibration.

## Counter-evidence

Unresolved cascades, finite solid angle, background and multiple δ branches can produce apparently consistent but non-identifying fits.

## Open L3 questions

- Under what covariance conditions can `A2/A4`, polarization and DCO identify δ uniquely?
- Which detector response quantities must be remeasured when transferring a calibration between arrays?
- Can a common likelihood express alignment, feeding, response and branch uncertainty without treating `σ/J` as a universal prior?

## Limitations and Missing Evidence

- `needs_review: true` remains on numerical claims intended for paper-level reuse.
- Review tables are provenance maps, not independent experiments.
- No L4 re-fit is claimed because raw response matrices and complete analysis code are generally unavailable.

## Sources

- [[yamazaki-1967-aligned-angular-coefficients]], [[rose-brink-1967-phase-defined-angular-distributions]], [[taras-1971-phase-defined-polarization-formulas]], [[hamilton-1948-successive-quanta-polarization]]
- [[suffert-1959-proton-capture-polarization]], [[lange-kumar-hamilton-1982-multipole-admixtures]]
- [[droste-1996-pdco-formalism]], [[starosta-1999-pdco-experimental-test]], [[droste-1999-ppco-polarization]]
- [[simpson-1983-sectored-geli-compton-polarimeter]], [[jones-1995-clover-compton-calibration]], [[schmid-1998-gammasphere-polarization]], [[miller-2007-sega-polarization]]

## Self-audit

- Evidence is separated into formalism, population model, detector response and nuclear assignment.
- Historical conventions are not silently converted; each source retains its own sign and state-order locator.
- This synthesis is a Codex self-audit and remains unreviewed.
