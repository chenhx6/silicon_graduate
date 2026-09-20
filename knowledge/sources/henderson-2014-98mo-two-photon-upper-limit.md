---
type: source
title: "Henderson et al. 2014 - Upper limit on two-photon emission in 98Mo"
aliases: [Henderson 2014 98Mo two-photon limit]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-theory
reading_depth: deep-read
title_original: "Upper limit on the two-photon emission branch for the 0+2 → 0+1 transition in 98Mo"
authors: [J. Henderson, D. G. Jenkins, P. J. Davies, M. Alcorta, M. P. Carpenter, B. P. Kay, C. J. Lister, S. Zhu]
journal: "Physical Review C"
year: 2014
volume: 89
pages: "064307"
doi: "10.1103/PhysRevC.89.064307"
canonical_source: "Henderson et al., Phys. Rev. C 89, 064307 (2014)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2014_Henderson et al_Upper limit on the two-photon emission branch for the 0 2 + → 0 1 + transition.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2014_Henderson et al_Upper limit on the two-photon emission branch for the 0 2 + → 0 1 + transition.pdf"
raw_sha256: "cc58109417fc373322985f880b6b54f3bb2efbe9a88baa8536fb96a6a015d7cd"
nuclei: [98Mo, 90Zr, 16O, 40Ca]
reactions: [98Mo-proton-scattering]
experiments: [Gammasphere, DSSD, conversion-electron, two-photon-search]
models: [two-photon-polarizability, magnetic-susceptibility, shape-coexistence]
observables: [two-photon-branching, E0-conversion, energy-sum, confidence-limit]
methods: [particle-gamma-coincidence, delayed-gamma-coincidence]
tags: [98Mo, two-photon-decay, upper-limit, shape-coexistence, Gammasphere]
---

# Upper limit on two-photon emission in `98Mo`

## Bibliographic Record

- J. Henderson *et al.*, *Phys. Rev. C* **89**, 064307 (2014), DOI `10.1103/PhysRevC.89.064307`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/2014_Henderson et al_Upper limit on the two-photon emission branch for the 0 2 + → 0 1 + transition.pdf`。

## Scope and Reading Depth

- PDF pp.064307-1–5 fully read: 98Mo motivation/shape coexistence, resonant proton scattering, DSSD conversion-electron normalization, Gammasphere delayed γγ search, Feldman–Cousins limits, phase-space/polarizability discussion and conclusion.
- Not covered: raw spectra and subsequent two-photon searches.

## Key Results

- The first excited `0+` state of `98Mo` at 735 keV was populated with 6.7-MeV resonant inelastic proton scattering; a DSSD measured E0 conversion electrons and Gammasphere searched for a 735-keV two-photon sum peak (PDF pp.1–3, Figs.1–3).
- No two-photon peak was observed. Combining proton-gated and 1024-keV γ-gated analyses gives `Γ2γ/Γtot < 1×10^-4` at 95% CL (97% before rounding), with corrected counts/efficiency and time-window treatment listed in Table I (PDF pp.3–4, Table I).
- The limit is below prior `16O`, `40Ca`, `90Zr` branches; simple phase-space scaling would predict an even smaller value (`~10^-7` if 98Mo resembled 90Zr), while deformation/shape coexistence and low-lying M1 strength could enhance the polarizability/susceptibility terms by one–two orders (PDF pp.1, 4–5).
- The result is an upper limit, not a null proof of absent two-photon decay; sensitivity is limited by Gammasphere efficiency and low branch expectation (PDF pp.3–5).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HE14-1 | `98Mo 0+2→0+1` two-photon branch is `<1×10^-4` at 95% CL. | upper-limit | direct | PDF pp.3–5, Table I | true |
| HE14-2 | DSSD conversion-electron normalization and delayed Gammasphere γγ search provide independent gating routes. | method-result | direct | PDF pp.2–4, Figs.1–3 | false |
| HE14-3 | Shape coexistence/deformation may enhance two-photon polarizability, but this is a model motivation rather than a measured branch. | model-interpretation | mixed | PDF pp.1, 4–5 | true |

## Summary

Henderson *et al.* establish a stringent `98Mo` two-photon upper limit in a non-closed-shell/shape-coexistence candidate, extending the `16O/40Ca/90Zr` measurement lineage. The absence of a peak is an efficiency- and confidence-limited upper bound, not evidence that the branch is zero.

## Competing Interpretations and Limitations

- The 4% γγ efficiency assumes an equal energy-sharing distribution; different matrix-element distributions can alter the limit.
- Feldman–Cousins upper limits depend on background, time window, electron efficiency and Gammasphere response.
- Phase-space comparison and polarizability/susceptibility estimates depend on nuclear structure; shape coexistence is motivation, not a closed causal explanation.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| HE14-AR-1 | Normalization chain | Proton excitation/conversion-electron count → total decays → delayed γγ candidate count → efficiency-corrected upper limit. | PDF pp.2–4, Table I | self-checking |
| HE14-AR-2 | Background chain | PAF/Compton and prompt-dark-current controls → energy-sum window → Feldman–Cousins confidence limit. | PDF pp.2–4, Figs.2–3 | self-checking |
| HE14-AR-3 | Transfer condition | Compare with other nuclei only after phase-space, energy-sharing and polarizability assumptions are mapped. | PDF pp.1, 4–5 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[two-photon-nuclear-decay]], [[triaxial-shape-coexistence]], [[gamma-soft-deformation]] and upper-limit methodology.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HE14-P0-1`: Preserve upper-limit/efficiency/energy-sharing boundaries; do not treat non-observation as a zero branch or direct shape verdict.

## Extracted Pages

- Concept: [[two-photon-nuclear-decay]]。
