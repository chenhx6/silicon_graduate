---
type: project
title: "Gamma-Ray Linear Polarization in Nuclear Spectroscopy"
aliases: [gamma-ray linear polarization evidence map, nuclear Compton polarimetry project]
created: 2026-07-13
updated: 2026-07-13
status: active
review_status: human-reviewed
project_stage: evidence-map
confidentiality: private
nuclei: []
tags: [gamma-ray-linear-polarization, compton-polarimetry, detector-methods, tracking-array, pado-support]
---

# Gamma-Ray Linear Polarization in Nuclear Spectroscopy

## Active Summary for Agents

This is an evidence map for nuclear gamma-ray linear polarization, Compton-polarimeter calibration, detector sensitivity, measured azimuthal asymmetry and in-beam relativistic corrections. It connects three source-level methods without treating a detector demonstration, a response simulation or an author interpretation as a universal experimental criterion. The project is not a formal synthesis or a paper draft.

Current source set: Garcia-Raffi 1995 non-orthogonal response formalism; Simpson 1983 sectored-GeLi calibration; Jones 2002 calibration formalism; Go 2024 multi-layer CdTe detector demonstration; Longfellow 2026 GRETINA in-beam angular-distribution and polarization method; Zheng 2013 EXOGAM clover calibration. The added source pages are deep-read and remain page-level `unreviewed`; numerical response values remain detector-specific.

## Research Question

How can nuclear gamma-ray linear polarization be calibrated and combined with angular-distribution, DCO/ADO and P-ADO evidence while keeping physical polarization, detector response, efficiency, alignment and relativistic corrections distinct?

## Research Questions

- How should physical polarization `P`, measured asymmetry `A`, modulation factor `Q'`, sensitivity `Q` and event efficiency `epsilon` be kept separate?
- What calibration conditions are needed before a Compton asymmetry can be converted to a physical polarization?
- How do Clover, tracking-array and multi-layer CdTe implementations differ in event reconstruction, response treatment and efficiency trade-offs?
- Which polarization signs or magnitudes remain ambiguous when mixing ratio, Delta-J, parity or alignment assumptions are not fixed?
- How should Lorentz angular aberration, solid-angle compression and Doppler-energy correction be applied in in-beam arrays?
- How can linear polarization be combined with angular distributions, DCO/ADO and P-ADO mixing-ratio analysis without hiding alignment or detector assumptions?

## Scope and Limits

The project covers method/formalism and detector-performance evidence directly supported by the three ingested papers. It does not claim complete coverage of all Compton polarimeters, all tracking-array response functions, or all nuclear gamma-ray polarization experiments. A source's calibration reaction is not automatically an in-beam nuclear-structure result, and a detector simulation is not a nuclear model calculation.

## Current Hypotheses

- H1: A polarization constraint is most useful when `P`, `A`, `Q`, efficiency and alignment assumptions are reported as separate layers.
- H2: Modern tracking or CdTe position sensitivity improves response control but does not eliminate calibration, background, population or branch ambiguities.
- H3: Relativistic angle and Doppler-energy corrections should be implemented and audited as related but different in-beam operations.

## Evidence Available

The current evidence is limited to the three deep-read source pages listed above plus the existing Lauritsen 2025 tracking-array context. The three source notes and this evidence map have completed the current user review; no claim is promoted to universal paper evidence by this project alone.

## Source-by-Source Evidence Table

| Source | Role | Direct contribution | Key claims | Review state |
|---|---|---|---|---|
| [[jones-2002-calibration-compton-polarimeters]] | formalism and calibration method | Defines `P`, `A`, `Q`, Klein-Nishina sensitivity, a2/a4 calibration and Rose-Brink mixed-transition polarization; documents special full-polarization cases and low-energy calibration limits. | J02-2 to J02-13 | Source and claim review complete |
| [[go-2024-demonstration-nuclear-gamma-ray-polarimetry-cdte]] | detector method and demonstration | Characterizes a twenty-layer CdTe camera with a `56Fe` 847-keV reference line, two-hit events, simulated response, maximum-likelihood polarization inference and modulation/sensitivity-efficiency trade-off. | G24-2 to G24-15 | Source and claim review complete |
| [[longfellow-2026-gretina-energy-ordering-polarization]] | in-beam tracking-array method | Connects angular distributions, Gaussian alignment, `Pbar`, `Q`, `A0`, mixing ambiguity, GRETINA energy ordering, Lorentz angle transformation and separate Doppler correction. | L26-2 to L26-16 | Source and claim review complete |
| [[simpson-1983-sectored-geli-compton-polarimeter]] | historical segmented-detector calibration | Gives single-crystal sector geometry, `P/A/Q`, configuration-dependent efficiency/sensitivity and `F=Q²εc` trade-off. | S83-1 to S83-4 | Source-level self-audit complete |
| [[garciaraffi-1995-nonorthogonal-compton-polarimeter]] | non-orthogonal response formalism | Replaces the orthogonal `A=QP` shortcut with `Q1/Q2/Q3` response terms and CLUSTER merit simulation. | GR95-1 to GR95-4 | Source-level self-audit complete |
| [[zheng-2013-linear-polarization-91ru]] | in-beam clover experiment | Demonstrates EXOGAM `A/Q/P` calibration with DCO and retains the `91Ru` ground-state assumption. | Z13-1 to Z13-5 | Source-level self-audit complete |

## Evidence Categories

### Observed or Measured Facts

- Go reports a 847-keV `56Fe` peak, two-hit event selection, an azimuthal distribution and a fitted modulation curve for the specified CdTe setup (G24-5, G24-6, G24-10, G24-11).
- Longfellow reports angular-distribution coefficients and Compton-plane asymmetries for known transitions in `25Mg`, `25Na` and `22Ne` using GRETINA (L26-9, L26-12).
- Jones reports the `19F` calibration example and the measured asymmetry used to infer its sensitivity (J02-6).

### Experimental Criteria and Formalism

- A polarization inference needs a defined count asymmetry and detector sensitivity, not a sign label alone (J02-2 to J02-4; G24-7/G24-12; L26-7).
- Angular-distribution coefficients and magnetic-substate population enter the predicted polarization; the detector response and finite geometry are separate terms (J02-5/J02-8; L26-4/L26-7).
- Mixing and Delta-J can produce multiple sign or magnitude possibilities. Longfellow's `25Na` example shows an angular-distribution two-solution case that polarization helps constrain, while its Appendix shows why an asymmetry sign alone remains insufficient (L26-13 to L26-15).

### Detector Characterization and Simulation

- Go uses Geant4/ComptonSoft simulations, normalization factors and a Poisson maximum-likelihood fit to separate response, background and polarization mixture terms (G24-7/G24-8).
- GRETINA's tracking-array position resolution supports continuous-angle response, but Longfellow's simple energy ordering is an analysis choice evaluated under one experiment's conditions (L26-1, L26-10, L26-11, L26-16).
- A high `Q` does not imply high efficiency. Go quantifies the `Q` versus `epsilon` trade-off with `F=epsilon Q^2` (G24-12/G24-13).

### Relativistic Corrections

The Longfellow chain is kept explicit:

1. Define `W(theta)` in the center-of-mass frame (L26-2).
2. Map `theta_lab` to `theta` with `cos(theta)=(cos(theta_lab)-beta)/(1-beta cos(theta_lab))` and include the forward-compression solid-angle factor (L26-2/L26-3).
3. In the polarization ratio the common solid-angle factor cancels, but the angle transformation remains in the Legendre and direction-polarization functions (L26-5/L26-6).
4. Construct the laboratory direction and Compton-plane angle event by event (L26-7/L26-10).
5. Apply the Doppler energy correction separately to the full-energy selection (L26-8).
6. Treat the reported 0 to -9% boost effect as an experiment- and angle-dependent quantitative check, not as a universal correction size (L26-9).

### P-ADO and Mixing-Ratio Bridge

This project links to [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]] as a method bridge only. The source set supports the following cautious mapping:

- `P` and `A0` can provide an independent electromagnetic-character constraint alongside angular distributions or P-ADO.
- `Q`, source response, event efficiency and solid-angle treatment belong to the detector layer; `sigma/J`, `sigma/I`, statistical tensors and feeding belong to the nuclear-population layer.
- Jones and Longfellow show that `delta` enters the transition formalism and that mixing-ratio branches can remain ambiguous if alignment or response assumptions are not exposed.
- Go shows one response/simulation route for a detector-specific polarization inference. It does not supply a universal correction for a different array or reaction.

## Evidence Matrix

| Topic | Supporting evidence | What is directly available | Boundary / unresolved issue |
|---|---|---|---|
| Physical polarization `P` | J02-2, J02-5, J02-8; L26-5 | Definitions and transition/alignment dependence | Special full-polarization cases require stated alignment and pure transitions. |
| Experimental asymmetry `A` / `A0` | J02-3; G24-11; L26-7 | Count/modulation definitions for specified geometries | Sign conventions and normalization differ between setups. |
| Sensitivity `Q` and modulation `Q'` | J02-4; G24-11/G24-12; L26-7 | Energy- and geometry-dependent response relations | Must not be replaced by a detector-independent number. |
| Detection efficiency `epsilon` | G24-6, G24-13 | Event-selection and figure-of-merit examples | Efficiency is configuration- and cut-dependent. |
| Alignment and mixing | J02-5/J02-8; L26-4, L26-13/L26-14 | a2/a4, statistical tensors, Gaussian `sigma/J`, `delta` and branch examples | Population assumptions and detector response must be fitted or bounded jointly. |
| Tracking-array polarimetry | L26-1, L26-10/L26-11; existing Lauritsen 2025 | Continuous-angle GRETINA method and energy-ordering test | Simple ordering is not established as universally better than full tracking. |
| CdTe polarimetry | G24-4 to G24-15 | Detector geometry, response simulation, modulation and performance | Demonstration is not a mature universal in-beam standard. |
| Relativistic corrections | L26-2/L26-3/L26-5/L26-6/L26-8/L26-9 | CM-to-LAB angle map, common-factor cancellation, separate Doppler equation | Exact implementation and sign/coordinate conventions need source-level review. |

## Unresolved Methodological Issues

- How should uncertainties in `P`, `Q`, source-response normalization and background be propagated into a mixing-ratio interval?
- When a transition has two angular-distribution or asymmetry branches, which independent observable is sufficient to select a branch under the actual detector geometry?
- How should Gaussian alignment width, feeding, response halos and energy ordering be jointly varied in a user P-ADO analysis?
- Which detector-performance quantity should be optimized for a rare in-beam transition: `Q`, `epsilon`, or `F=epsilon Q^2`?
- How large is the Lorentz correction for a given residue velocity and angular acceptance, and where should the transformed direction enter the polarization response?

## Risks and Blockers

- Do not merge physical `P`, count asymmetry `A/A0`, modulation factor `Q'`, sensitivity `Q` and efficiency `epsilon`.
- Do not transfer Jones, Go or Longfellow numerical detector values to a different array or reaction without a matched calibration.
- Do not infer a universal `sigma/I` or `sigma/J`, or a unique mixing-ratio branch, from one polarization sign.
- Do not treat a detector-response simulation as a nuclear-structure prediction.

## Claims Not Yet Ready for Paper Evidence Gate

- A numerical `Q` or `epsilon` value transferred from Go, Jones or Longfellow to another array or reaction.
- A statement that the sign of a measured polarization asymmetry uniquely fixes electric/magnetic character.
- A universal `sigma/I` or `sigma/J` value inferred from one calibration reaction or one GRETINA setup.
- A claim that the simple energy-ordering approach is equivalent to, or superior to, full tracking in all conditions.
- A claim that beta can be neglected without checking the angular transformation and event geometry.

## Human Review Triage

### Review outcome

The current user review is complete for the three source notes and this evidence map. No claim-level `needs_review: true` items remain in the source bundle. The review corrected the J02-13 table escape for `|P|` and restored the division index `j` on the Go Eq.3 normalization factor; the P/A/Q, detector-response, GRETINA Lorentz/Doppler and alignment boundaries remain explicit.

### Future validation (not pending review)

- Recheck detector-specific efficiencies and figure-of-merit values if a future in-beam dataset uses a different array or energy range.
- Map the Longfellow Lorentz/Doppler chain to the user's actual residue velocity and angular acceptance before writing code-facing equations.
- Keep the P-ADO bridge explicit so `P/A/Q` and `sigma/J` remain distinct.

## Next Actions

1. Add a detector-specific calibration source if a future in-beam dataset requires a different energy or array response.
2. Compare the Longfellow Lorentz/Doppler chain with the user's actual residue velocity and angular acceptance before writing code-facing equations.
3. Update the existing P-ADO project only where the source-to-user notation mapping is explicit.
4. Do not create a formal synthesis in this ingest round.

## Sources and Related Pages

- Sources: [[jones-2002-calibration-compton-polarimeters]], [[go-2024-demonstration-nuclear-gamma-ray-polarimetry-cdte]], [[longfellow-2026-gretina-energy-ordering-polarization]]
- Methods: [[compton-polarimetry]], [[modulation-curve]], [[linear-polarization-asymmetry]], [[tracking-array]], [[doppler-correction]]
- Concepts: [[gamma-ray-linear-polarization]], [[lorentz-boost-correction]], [[magnetic-substate-population]], [[spin-alignment]]
- Observables: [[experimental-asymmetry]], [[polarization-sensitivity]], [[detection-efficiency]], [[angular-distribution-coefficient]], [[multipole-mixing-ratio]]
- Related project: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]
