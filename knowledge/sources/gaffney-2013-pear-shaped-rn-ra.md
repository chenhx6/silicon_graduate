---
type: source
title: "Gaffney et al. 2013 - Studies of pear-shaped nuclei using accelerated radioactive beams"
aliases: [Gaffney 2013 pear-shaped nuclei, 220Rn 224Ra Coulomb excitation]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Studies of pear-shaped nuclei using accelerated radioactive beams"
authors: [L. P. Gaffney, P. A. Butler, M. Scheck, A. B. Hayes, F. Wenander, et al.]
journal: Nature
year: 2013
volume: 497
pages: "199-204"
doi: "10.1038/nature12073"
canonical_source: "https://doi.org/10.1038/nature12073"
library_file: "raw/papers/gpt/high-spin-20260920/形变/2013_Gaffney et al_Studies of pear-shaped nuclei using accelerated radioactive beams.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/形变/2013_Gaffney et al_Studies of pear-shaped nuclei using accelerated radioactive beams.pdf"
raw_sha256: "3b7975206409de9286df55a82c820783b2ebd371824bf50d69da6c9e916c551b"
nuclei: [220Rn, 224Ra]
reactions: [coulomb-excitation-radioactive-beams]
experiments: [cern-isolde-rex-miniball]
models: [rotational-model, mean-field-octupole, cluster-model]
observables: [E1, E2, E3, Q1, Q2, Q3, Coulomb-excitation-yields]
methods: [coulomb-excitation, GOSIA, gamma-ray-spectroscopy]
tags: [pear-shape, octupole, reflection-asymmetry, Rn, Ra, EDM]
---

# Studies of pear-shaped nuclei using accelerated radioactive beams

## Bibliographic Record

- L. P. Gaffney *et al.*, *Nature* **497**, 199–204 (2013), DOI `10.1038/nature12073`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/形变/2013_Gaffney et al_Studies of pear-shaped nuclei using accelerated radioactive beams.pdf`。
- 6-page Nature PDF; title, author list, DOI, figures, Table 1 and Methods/Outlook identity checked. This is a direct Coulomb-excitation experiment, not merely a review of pear shapes.

## Scope and Reading Depth

- PDF pp.199–204 fully read, including abstract/introduction, Figs.1–5, partial level schemes, Table 1 matrix elements, Coulomb-excitation/GOSIA description, shape comparison and Outlook/Methods.
- Figure/table audit: MINIBALL spectra and level schemes, `Q2/Q3` versus spin, intrinsic-shape plots, isotope-systematics plot and all Table 1 E1/E2/E3 matrix elements were checked.
- Not covered: raw GOSIA input/output files, event matrices, full lifetime datasets and later independent measurements.

## Paper Question and Experimental Logic

The experiment asks whether direct electric-octupole transition strengths can distinguish dynamic octupole correlations in `220Rn` from stronger, more static pear-shaped collectivity in `224Ra`, using accelerated radioactive beams and Coulomb excitation.

1. Produce and accelerate `220Rn`/`224Ra` at REX-ISOLDE (`2.82–2.83 MeV/u`), bombard `60Ni`, `112Cd`, `114Cd` or `120Sn` targets, and detect scattered projectiles/recoils with segmented silicon plus MINIBALL (24 segmented HPGe detectors).
2. Measure γ yields in separated recoil-angle ranges and fit Coulomb-excitation matrix elements with GOSIA. Known lifetimes/branching and target matrix elements constrain the fit; 34 (`220Rn`) and 57 (`224Ra`) independent points constrain 22/23 free parameters.
3. Convert matrix elements to intrinsic `Q1`, `Q2`, `Q3` and compare level energies, transition strengths, shape plots and isotope trends with mean-field and cluster-model predictions.

## Key Evidence and Reasoning Chain

- `220Rn` has `Q2≈434(14) e fm²` and `Q3≈2180(130) e fm³`; `224Ra` has `Q2≈632(10) e fm²` and `Q3≈2520(90) e fm³` for the lowest transitions (Table 2/systematics). The direct E3 matrix elements are `810(50) e fm³` (`220Rn`, `0+→3−`) and `940(30) e fm³` (`224Ra`, `0+→3−`), with additional E3 links listed in Table 1.
- `Q2` and `Q3` remain approximately constant over the measured spin range, supporting a rotational intrinsic-moment description rather than a rapidly changing shape (Fig.3).
- Shape reconstruction gives `220Rn` a more vibrational motion about reflection symmetry and `224Ra` a stronger static octupole/pear component; the `224Ra` E3 strength is larger and more coherent with a permanent deformation interpretation (Fig.4).
- `220Rn` has weaker octupole collectivity than `224Ra`; comparisons with mean-field D1M/D1S and cluster-model predictions show differing isotope trends. The authors conclude `219,221Rn` are likely less favorable EDM candidates than `223,225Ra`, while future heavier Rn isotopes may improve.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GA13-1 | Coulomb excitation of radioactive `220Rn` and `224Ra` measures E1/E2/E3 matrix elements with `10%`-level accuracy using MINIBALL and GOSIA. | experimental-result | direct | PDF pp.199–203, Table 1, Methods | true |
| GA13-2 | `224Ra` exhibits stronger and more coherent octupole collectivity than `220Rn`, with `Q3` and E3 strengths supporting a pear-shaped/static-deformation interpretation. | experimental-result/author-interpretation | mixed | PDF pp.200–203, Figs.3–5, Tables 1–2 | true |
| GA13-3 | Intrinsic E2/E3 moments are approximately constant across the measured spin range. | experimental-result | direct | PDF p.202, Fig.3 | true |
| GA13-4 | Mean-field and cluster-model calculations predict different Rn/Ra octupole trends; the data oppose the cluster-model trend and distinguish model families. | model-data-comparison | mixed | PDF pp.202–203, Fig.5, Outlook | true |
| GA13-5 | Octupole-enhanced EDM candidate ranking favors Ra over the measured Rn isotopes, subject to future spectroscopy. | author-interpretation | indirect | PDF p.203, Outlook | true |

## Summary

This experiment provides direct E3-strength evidence separating weaker octupole collectivity in `220Rn` from stronger pear-shaped behavior in `224Ra`. The result anchors the distinction between octupole correlations and static deformation with a multi-target Coulomb-excitation/GOSIA analysis, while retaining model and input-data boundaries.

## Competing Interpretations and Limitations

Constant intrinsic moments support a rotational description but do not by themselves prove a rigid static shape; vibrational/soft models can produce strong E3 transitions. GOSIA results depend on target matrix elements, recoil-angle ranges, lifetimes/branching and rotational-model constraints. Absolute E1 moments remain small and cancellation-sensitive, and the EDM-candidate extrapolation to odd-A isotopes is not a direct measurement.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GA13-AR-1 | Evidence chain | Coulomb-excitation yields → GOSIA matrix elements → Q1/Q2/Q3 → shape/systematics comparison. | PDF pp.200–203, Methods | self-checking |
| GA13-AR-2 | Direct versus model | E1/E2/E3 matrix elements and Q values are measured/fitted observables; pear/static and EDM implications are author/model interpretations. | Table 1, Figs.3–5 | self-checking |
| GA13-AR-3 | Transfer condition | Q3 comparison transfers only with matched Coulomb-excitation model, target matrix elements and spin range; not as a universal β3 prior. | PDF Methods/Table 1 | provisional |
| GA13-AR-4 | Failure condition | Missing raw GOSIA files, target uncertainties, lifetime/branching revisions or soft-vibrational alternatives could change absolute strengths and deformation ranking. | PDF pp.202–203 | active-L3 |
| GA13-AR-5 | Independence | Direct Rn/Ra experiment; cited `226Ra` and other isotope values are historical comparison, not independent new points. | Table 2/Fig.5 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` octupole-deformation/correlation boundaries and provides a direct Coulomb-excitation benchmark; `revises` any assumption that E3 enhancement alone identifies static shape.
- Persistence: update [[octupole-deformation]], [[octupole-correlation]], [[reflection-asymmetric-nuclei]], [[coulomb-excitation]] and the high-spin evidence map.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[octupole-deformation]] | Direct E3/Q3 benchmark for stronger static-like `224Ra` versus weaker `220Rn`. |
| supports | [[octupole-correlation]] | E3 moments as direct collective octupole observable, separated from model β3. |
| methodological-bridge | [[coulomb-excitation]] | Radioactive-beam MINIBALL/GOSIA matrix-element extraction. |
| candidate-L3 | [[a130-high-spin-collective-modes-evidence-map]] | Non-A≈130 benchmark for parity-sensitive collective-mode inference. |

## Human Review Triage

### P0

- `GA13-P0-1`: keep measured matrix elements, intrinsic moments and pear/static interpretation separate; do not convert `Q3` directly to a universal β3 without the stated shape model.

### P1

- `GA13-P1-1`: GOSIA fit correlations, target matrix elements and lifetime inputs need source-data-level recheck before absolute-strength reuse.
- `GA13-P1-2`: EDM-candidate ranking is an extrapolation to odd-A isotopes and depends on parity-doublet/Schiff-moment theory.

## Extracted Pages

- Nuclei: `220Rn`, `224Ra` (source-level pages not created in this unit).
- Concepts: [[octupole-deformation]], [[octupole-correlation]], [[reflection-asymmetric-nuclei]]。
- Methods: [[coulomb-excitation]]。

## L3/L4 Follow-up

- L3 question: can a common E3/Q3–PES–parity-systematics map distinguish stable octupole minima from soft octupole correlations across Rn/Ra/Th/U and the A≈130 cases? Required companions are E3 strengths, E1/energy-displacement, parity bands and model sensitivity.
- No L4 run: GOSIA files and raw yield matrices are not supplied; Table 1 is a reported result, not a machine-readable analysis input.
