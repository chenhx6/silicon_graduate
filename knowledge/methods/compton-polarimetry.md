---
type: method
title: "Gamma-Ray Compton Polarimetry"
aliases: [Compton polarimetry, gamma-ray Compton polarimeter]
created: 2026-07-13
updated: 2026-09-20
status: active
review_status: unreviewed
method_type: gamma-ray-polarimetry
tags: [compton-scattering, linear-polarization, detector-response, parity]
---

# Gamma-Ray Compton Polarimetry

## Purpose

Compton polarimetry infers the linear polarization of gamma rays from the azimuthal dependence of Compton-scattering events. The scattering plane is correlated with the incident electric-field direction through the Klein-Nishina cross section.

## Inputs and Assumptions

- Calibrated energy and position information for the scatter and absorber interactions.
- A defined azimuth convention, accepted Compton-scatter angle range, detector response and background treatment.
- A reference polarization or validated response simulation when converting a modulation to `P`.

## Core Chain

1. Select events with a reconstructible scatter and absorber interaction.
2. Form an azimuthal distribution or detector-pair count asymmetry.
3. Correct or model detector geometry, efficiency, background and accepted Compton-scatter angles.
4. Relate the measured modulation to physical polarization with a calibrated sensitivity `Q` or a simulated detector response.

The analyzing power is a Compton-scattering property and depends on photon energy and scatter angle. It is not the same as nuclear angular-distribution alignment.

## Detector Implementations

- Clover and segmented HPGe arrays provide compact Compton event selections.
- GRETINA/AGATA tracking arrays provide many interaction positions and a continuous angular phase space, but still require response and ordering treatment.
- Go 2024 demonstrates a twenty-layer position-sensitive CdTe camera for a 847-keV calibration line. Its likelihood and Geant4/ComptonSoft chain is a detector demonstration, not a universal replacement for HPGe arrays.

## What It Can Establish

With calibration and response control, Compton polarimetry can constrain the linear polarization and electromagnetic character of selected gamma-ray transitions.

## What It Cannot Establish Alone

It cannot by itself fix nuclear alignment, choose a unique mixing-ratio branch, or establish a nuclear-structure interpretation without the transition and population context.

## Boundaries

Physical `P`, measured `A`, sensitivity `Q`, modulation factor `Q'`, and efficiency `epsilon` must be reported separately. A detector simulation characterizes response; it does not establish a nuclear-structure interpretation by itself.

[[zheng-2013-linear-polarization-91ru]] gives a clover-specific in-beam example: the measured asymmetry uses adjacent-crystal horizontal/vertical scatters, `A=([aN⊥]−N∥)/([aN⊥]+N∥)`, and the EXOGAM sensitivity is fitted as `Q=Q_point(p0+p1Eγ)` from known pure E2 transitions. The reported figure of merit is detector- and energy-dependent; the source does not define a universal `Q` or asymmetry sign outside its geometry and convention.

[[garciaraffi-1997-monte-carlo-compton-polarimeters]] adds the response-simulation layer: modified GEANT3/Stokes tracking reproduces five-coaxial, four-coaxial and CLOVER `Q(E)` values to roughly 10% for the tested geometries. Multiple-scatter polarization propagation is essential; first-scatter-only treatment underestimates `Q` in the four-crystal test. The quoted `Q` and `M=εQ²` remain geometry/threshold/window specific.

[[bass-1972-two-crystal-compton-polarimeter]] provides an early symmetric two-crystal coincidence/anticoincidence design; its `R(E,E_th)` and efficiency trade-off are explicit detector-response quantities.

[[klein-nishina-1929-compton-scattering]] is the free-electron relativistic response foundation; it does not include polarization, finite geometry or detector sensitivity.

[[vonderwerth-1995-compton-polarimeters]] supplies POLALI/MINIPOLA modular detector designs and the kinematic-gate/sensitivity/efficiency figure-of-merit trade-off.

[[schmid-1998-gammasphere-polarization]] supplies the segmented-Gammasphere confined/shared asymmetry and Monte Carlo `Q(E)` validation, including high-background `197Pb` parity application limits.

[[droste-1999-ppco-polarization]] extends CLOVER polarimetry to PPCO two-γ correlations; alignment and both detector sensitivities remain explicit inputs.

[[starosta-1999-pdco-experimental-test]] provides the complementary single-transition PDCO validation: `A=QP`, a detector-specific `Q(E)` calibration and four polarimeter/gamma-detector geometries are combined with `R_DCO`. Its `490 keV` case remains E2 versus ΔI=0 M1/E2 ambiguous, and integrated-mode `P` is qualitative unless solid-angle and efficiency corrections are known.

[[droste-1996-pdco-formalism]] is the formal precursor: one statistical-tensor expression covers DCO, PDCO and PPCO, with explicit detector-plane, emission-angle, deorientation and Gaussian-alignment terms.

[[jones-1995-clover-compton-calibration]] is the early four-crystal EUROGAM calibration: `P`, count asymmetry `A` and sensitivity `Q=A/P` are kept separate, with `Q` falling from `0.34(9)` at 197 keV to `0.121(5)` at 1368 keV for a 60-keV threshold. The fit and threshold are geometry-specific.

[[miller-2007-sega-polarization]] extends the response map to side-irradiated SeGA: a `249Cf` α–γ calibration gives `Q≈0.14(2)` near 350 keV and `FM≈5.9×10^-6`. The side orientation, geometric asymmetry and finite-angle correction are part of the calibration identity.

[[aoki-1975-geli-summing-polarimeters]] is an early simultaneous-angle Ge(Li) design: a central scatterer and four analyzers measure `φ=0°,30°,60°,90°` without rotation; majority anticoincidence reduces Compton background, while the ring-reflector summing spectrometer trades efficiency for a flat low background and a practical ≈300-keV threshold.

## Sources

- [[jones-2002-calibration-compton-polarimeters]]
- [[simpson-1983-sectored-geli-compton-polarimeter]]
- [[garciaraffi-1995-nonorthogonal-compton-polarimeter]]
- [[butler-1973-three-geli-compton-polarimeter]]
- [[logan-1974-generalized-polarimeter-merit]]
- [[go-2024-demonstration-nuclear-gamma-ray-polarimetry-cdte]]
- [[longfellow-2026-gretina-energy-ordering-polarization]]
- [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]
- [[zheng-2013-linear-polarization-91ru]]
- [[garciaraffi-1997-monte-carlo-compton-polarimeters]]
- [[bass-1972-two-crystal-compton-polarimeter]]
- [[klein-nishina-1929-compton-scattering]]
- [[vonderwerth-1995-compton-polarimeters]]
- [[schmid-1998-gammasphere-polarization]]
- [[droste-1999-ppco-polarization]]
