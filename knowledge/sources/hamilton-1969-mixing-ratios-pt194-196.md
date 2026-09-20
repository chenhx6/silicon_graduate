---
type: source
title: "Hamilton 1969 - E2/M1 mixing ratios in 194Pt and 196Pt"
aliases: [Hamilton 1969 Pt mixing ratios]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "The multipole mixing ratio of 2'+ → 2+ transitions in 194Pt and 196Pt"
authors: [W. D. Hamilton]
journal: "Nuclear Physics A"
year: 1969
volume: 136
pages: "251-264"
pii: "0375-9474(69)90052-9"
canonical_source: "Hamilton, Nucl. Phys. A 136, 251-264 (1969)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1969_Hamilton_The multipole mixing ratio of 2′+ → 2+ transitions in 194Pt and 196Pt.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1969_Hamilton_The multipole mixing ratio of 2′+ → 2+ transitions in 194Pt and 196Pt.pdf"
raw_sha256: "8b575f5913d054340bb26b03e6ef7270de7e96e26f110420f331f2ff7beeda7a"
nuclei: [194Pt, 196Pt, 194Au, 196Au]
reactions: [194Pt-proton-neutron, 196Pt-proton-neutron]
experiments: [gamma-gamma-angular-correlation, gamma-linear-polarization]
models: [Biedenharn-mixing-ratio, Kumar-matrix-elements]
observables: [A22, A44, linear-polarization, E2-M1-mixing-ratio]
methods: [Ge-NaI-coincidence, summing-polarimeter, gamma-gamma-angular-correlation]
tags: [194Pt, 196Pt, mixing-ratio, polarization, angular-correlation]
---

# E2/M1 mixing ratios in `194Pt` and `196Pt`

## Bibliographic Record

- W. D. Hamilton, *Nucl. Phys. A* **136**, 251–264 (1969), PII `0375-9474(69)90052-9`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1969_Hamilton_The multipole mixing ratio of 2′+ → 2+ transitions in 194Pt and 196Pt.pdf`。

## Scope and Reading Depth

- PDF pp.257–264 fully read: source preparation, Ge–NaI γγ setup, four correlation angles, accidental/background/miscentering corrections, Tables 1–3, γ-linear-polarization analysis, Figs.1–3 and the unresolved 759-keV issue.
- Not covered: later evaluated level schemes and the cited original theory papers beyond the comparisons printed here.

## Key Results

- High-resolution Ge coincidence spectra separated the `294-328 keV` `194Pt` cascade and the `333-356 keV` `196Pt` cascade, avoiding unresolved contributions that had affected earlier angular-correlation measurements (PDF pp.258–260, Fig.1).
- For `194Pt`, the corrected weighted averages are `A22=−0.092(13)` and `A44=0.303(20)`; the inferred E2/M1 mixing ratio is `δ=−(30^{+39}_{−19})` under the Biedenharn convention (PDF p.261, Table 1).
- For `196Pt`, the weighted averages are `A22=0.113(5)` and `A44=0.315(10)`, giving `δ=+4.03(12)` for the 333-keV transition (PDF p.261, Table 1). The value strongly disagrees with the then-current Kumar theoretical `+101.4` prediction, whereas the `194Pt` result is compatible with `−19.9`.
- γ-linear-polarization gives `P=0.034(46)` for 294 keV and `P=0.067(31)` for 333 keV; the 196Pt cascade has a unique positive-δ solution in the combined plot, while the 194Pt polarization is weak and not independently decisive (PDF pp.261–262, Table 2, Figs.2–3).
- Additional `759-333` and `759-356 keV` correlations in `196Pt` yield no consistent solution for the accepted spin sequence; the author preserves a possible unresolved doublet/extra transition near 759 keV and calls for better-resolution coincidence data (PDF pp.263–264, Table 1).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HA69-1 | High-resolution γγ correlations determine `δ=−(30^{+39}_{−19})` for the 294-keV `194Pt` transition under the stated convention and corrections. | mixing-ratio-result | direct | PDF pp.259–262, Table 1, Fig.2 | true |
| HA69-2 | The 333-keV `196Pt` transition has `δ=+4.03(12)` and a unique combined-correlation solution within the accepted cascade. | mixing-ratio-result | direct | PDF pp.261–263, Tables 1–2, Fig.3 | true |
| HA69-3 | The `196Pt` result conflicts with the then-current Kumar theoretical mixing ratio; matrix-element cancellations are proposed as one explanation. | experiment-model-conflict | mixed | PDF pp.262–263, Table 3 | true |
| HA69-4 | The 759-keV correlations are inconsistent with the accepted level sequence and may indicate an unresolved nearby transition. | source-integrity-boundary | direct | PDF pp.263–264, Table 1 | false |

## Summary

Hamilton combines high-resolution γγ angular correlations with γ-linear polarization to resolve E2/M1 mixing in `194Pt` and `196Pt`. The result illustrates both the power and fragility of mixing-ratio extraction: careful cascade separation gives a robust branch in `196Pt`, while weak polarization and unresolved feeding leave explicit ambiguity in `194Pt` and around 759 keV.

## Competing Interpretations and Limitations

- The `δ` values use the Biedenharn convention in which the first cascade member is treated as an absorption matrix element; signs cannot be compared with Rose–Brink values without an explicit phase map.
- Corrections rely on a 6% contaminant estimate for the 294-keV line, assumed spin sequences, source centering, accidental/background subtraction and comparable polarization efficiency for cascade members.
- The 194Pt polarization is consistent with a broad range of δ values and is not a unique branch selector by itself.
- The 196Pt theory disagreement may reflect matrix-element cancellation, but the paper does not test modern wave functions; it is a historical experiment–model conflict, not a universal failure of theory.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| HA69-AR-1 | Correlation chain | Isolate cascade peaks → correct contamination/accidentals/miscentering → fit `A22/A44` → map to δ with the stated convention. | PDF pp.259–262, Table 1 | self-checking |
| HA69-AR-2 | Polarization chain | Summing polarimeter → measured linear P → compare positive/negative δ response; equal-efficiency assumption is explicit. | PDF pp.261–262, Table 2, Figs.2–3 | self-checking |
| HA69-AR-3 | Integrity check | 759-keV branch fails the accepted sequence, so the result is retained as a level-scheme warning rather than forced into δ. | PDF pp.263–264 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[multipole-mixing-ratio]], [[angular-correlation]], [[linear-polarization-asymmetry]] and the convention/branch audit.
- New reusable rule: high-resolution cascade identity and phase convention are prerequisites for comparing δ across experiments; a polarization-compatible fit does not repair unresolved feeding.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HA69-P0-1`: Preserve the Biedenharn convention and the 759-keV unresolved-transition warning; do not merge these δ values with Rose–Brink values without a convention conversion and cascade audit.

## Extracted Pages

- Observables/methods: [[multipole-mixing-ratio]], [[angular-correlation]], [[linear-polarization-asymmetry]]。
