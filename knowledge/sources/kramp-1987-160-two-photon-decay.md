---
type: source
title: "Kramp et al. 1987 - Nuclear two-photon decay in 0+ to 0+ transitions"
aliases: [Kramp 1987 two-photon decay]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-theory
reading_depth: deep-read
title_original: "Nuclear two-photon decay in 0+ → 0+ transitions"
authors: [J. Kramp, D. Habs, R. Kroth, M. Music, J. Schirmer, D. Schwalm, C. Broude]
journal: "Nuclear Physics A"
year: 1987
volume: 474
pages: "412-450"
pii: "0375-9474(87)90625-7"
canonical_source: "Kramp et al., Nucl. Phys. A 474, 412-450 (1987)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/1987_Kramp et al_Nuclear two-photon decay in 0+→0+ transitions.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/1987_Kramp et al_Nuclear two-photon decay in 0+→0+ transitions.pdf"
raw_sha256: "be1b792e5b3e47a50e177a3ec48f7fbb605ae4db0d8af8f6ec2c60cdf9388413"
nuclei: [16O, 40Ca, 90Zr]
reactions: [16O-proton-scattering]
experiments: [Heidelberg-Darmstadt-crystal-ball, two-photon-coincidence, linear-polarization]
models: [second-order-QED, two-level-polarizability, E1-M1-interference]
observables: [two-photon-branching, energy-sharing, angular-correlation, linear-polarization, matrix-element-ratio]
methods: [Crystal-Ball, particle-gamma-coincidence, gamma-gamma-correlation]
tags: [two-photon-decay, 16O, E1, M1, polarizability, Crystal-Ball]
---

# Nuclear two-photon decay in `0+→0+` transitions

## Bibliographic Record

- J. Kramp *et al.*, *Nucl. Phys. A* **474**, 412–450 (1987), PII `0375-9474(87)90625-7`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/1987_Kramp et al_Nuclear two-photon decay in 0+→0+ transitions.pdf`。

## Scope and Reading Depth

- PDF pp.412–450 (39 pages) fully read: second-order two-photon theory, Crystal-Ball/particle setup, `16O` energy-angle matrices, PAF/background rejection, branching ratio, polarization, `E1/M1` interference, comparison with `40Ca/90Zr` and Appendix S-matrix/polarizability formalism.
- Not covered: raw event matrices and later two-photon reanalyses.

## Key Results

- The `16O` first excited `0+` state at 6.05 MeV was populated with `7.58-MeV` proton scattering, favoring the `0+` state over the nearby `3−` state by about 16:1. A Heidelberg–Darmstadt 4π Crystal Ball with particle coincidence separates true two-photon decay from Compton and positron-annihilation-in-flight backgrounds (PDF pp.412–418).
- The measured two-photon branching ratio is `Γ2γ/Γtot=(6.6±0.5)×10^-4` for `16O`; the full energy-sharing/angle matrix and event-selection checks establish the candidate branch (PDF pp.417–424, 427–431).
- The angular correlation contains an interference term proving comparable `2E1` and `2M1` amplitudes. The ratio `αE1/χ` is restricted to two inverse solutions, approximately `−6.2±1.5` or `−0.16±0.04`, and linear polarization selects the dominant branch (PDF pp.431–438, 441–447).
- The authors compare `16O`, `40Ca` and `90Zr` through electric polarizabilities and magnetic susceptibilities in a two-level spherical/deformed basis; this gives qualitative/partial quantitative understanding but remains model dependent (PDF pp.447–450, Appendix A).
- Two-photon decay is a second-order QED process with resonance and seagull amplitudes constrained by gauge invariance; they are not separately measurable mechanisms (PDF pp.413–414, Appendix A).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KR87-1 | `16O` `0+→0+` two-photon branching is `(6.6±0.5)×10^-4`. | decay-result | direct | PDF pp.417–438 | true |
| KR87-2 | Angular-correlation interference establishes comparable `2E1` and `2M1` amplitudes with inverse matrix-ratio branches. | matrix-element-result | direct | PDF pp.431–447 | true |
| KR87-3 | Crystal-Ball particle/energy/angle controls separate true 2γ decay from Compton/PAF backgrounds. | method-result | direct | PDF pp.414–431 | false |
| KR87-4 | Polarizability/susceptibility interpretation is a two-level model layer, not a direct measurement of shape. | model-boundary | mixed | PDF pp.447–450, Appendix A | false |

## Summary

Kramp *et al.* establish a careful `16O` two-photon decay measurement and demonstrate that angular correlations and linear polarization reveal interference between `2E1` and `2M1` amplitudes. The source is a direct methodological precursor to modern two-photon nuclear-decay work, with explicit background, branch and model boundaries.

## Competing Interpretations and Limitations

- The two inverse `αE1/χ` branches arise from the angular-correlation fit; polarization and prior model information are needed to choose one.
- PAF and Compton backgrounds can mimic two-photon energy sums; the Crystal-Ball and proton-gate controls are part of the claim.
- The two-level polarizability/susceptibility interpretation depends on spherical/deformed basis mixing and cannot be generalized without nucleus-specific structure input.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| KR87-AR-1 | Event chain | Proton gate → Crystal-Ball two-γ energy/angle → PAF/Compton rejection → branching ratio. | PDF Secs.2–3 | self-checking |
| KR87-AR-2 | Amplitude chain | Second-order E1/M1 amplitudes → angular interference/polarization → inverse matrix-ratio branches. | PDF Sec.3, Appendix A | self-checking |
| KR87-AR-3 | Transfer condition | Use common phase, background and multipole decomposition before comparing with 40Ca/90Zr/Freire/Walz sources. | PDF pp.431–450 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[two-photon-nuclear-decay]], [[compton-polarimetry]], [[linear-polarization-asymmetry]] and the two-photon experimental lineage.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `KR87-P0-1`: Preserve PAF/Compton rejection and the inverse `E1/M1` branch; do not merge two-photon matrix ratios across nuclei without phase/background mapping.

## Extracted Pages

- Concept/methods: [[two-photon-nuclear-decay]], [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
