---
type: source
title: "Königshofen et al. 2001 - Multipole mixing ratios in 130Ba"
aliases: [Königshofen 2001 130Ba mixing ratios]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Multipole mixing ratios in 130Ba"
authors: [C. T. Königshofen, K. Jessen, A. Gade, I. Wiedenhöver, H. Meise, P. von Brentano]
journal: "Physical Review C"
year: 2001
volume: 64
article: 037302
pages: "1-3"
doi: "10.1103/PhysRevC.64.037302"
citation_key: K_nigshofen_2001
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevC.64.037302"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2001_Königshofen et al_Multipole mixing ratios in 130 Ba.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2001_Königshofen et al_Multipole mixing ratios in 130 Ba.pdf"
raw_sha256: "34428af79a8dcc3a7dc27a6a416c3fa556a2d37e763df76cb1218241f370a755"
nuclei: [130Ba, 130La]
reactions: [120Sn(14N,4n)130La]
experiments: [cologne-osiris8-euroball-cluster]
models: [interacting-boson-model-1, consistent-q-iba]
observables: [multipole-mixing-ratio, gamma-gamma-angular-correlation, branching-ratio, B(E2)]
methods: [angular-correlation, gamma-gamma-coincidence]
tags: [130Ba, mixing-ratio, low-spin, A130, gamma-gamma]
---

# Multipole mixing ratios in 130Ba

## Bibliographic Record

- C. T. Königshofen *et al.*, *Physical Review C* **64**, 037302 (2001), DOI `10.1103/PhysRevC.64.037302`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/纲图/2001_Königshofen et al_Multipole mixing ratios in 130 Ba.pdf`。
- 3-page selectable-text PRC Brief Report; title page, authors, DOI, volume/article number and publication date agree.

## Scope and Reading Depth

- PDF pp.037302-1–3 fully read: reaction/off-beam β-decay setup, Osiris-8/Euroball cluster geometry, three-angle matrices, Figs.1–3, complete Table I, Rose–Brink sign convention, B(E2) correction, IBA-CQF comparison and conclusions.
- Figure/table audit: gated spectrum quality (Fig.1), `W(180)/W(90)` and `W(55)/W(90)` versus `arctan δ` unique-branch example (Fig.2), partial `130Ba` level scheme (Fig.3), and all 18 transition rows in Table I.
- Not covered: raw coincidence matrices, detector-pair efficiency files, decay-scheme source data and IBA code.

## Paper Question and Experimental Logic

The paper asks whether multi-angle γγ directional correlations can determine unique multipole mixing ratios for low-spin `130Ba` transitions and correct the inferred `B(E2)` branchings used in IBA-1/consistent-Q comparisons.

1. Produce `130La` with `120Sn(14N,4n)` at 65 MeV, collect off-beam β+/EC decay γγ coincidences in Osiris-8 plus one Euroball cluster (47 million events; detector-pair angles 180°, 90° and 55°; PDF p.037302-1).
2. Use efficiency-corrected ratios `W(180°)/W(90°)` and `W(55°)/W(90°)` and compare with calculated angular-correlation curves for spin/parity and multipolarity hypotheses.
3. Analyze cascades containing one pure E2 transition so the two measured ratios intersect at a unique `δ` (Rose–Brink convention); correct branching/B(E2) ratios for M1 admixtures and compare with IBA-CQF.

## Key Evidence and Reasoning Chain

- Two independent detector-angle ratios give unique solutions for 18 transitions; the high sensitivity comes from sizable `P2` and `P4` coefficients (example `−0.0321` and `−0.0778`) and clean β-decay spectra (PDF pp.037302-1–2, Fig.2).
- A new `3−` assignment for the 1918.3-keV level is adopted because its decays are consistent with pure E1 and its β population is much weaker than the positive-parity `3+` state at 2053.3 keV (PDF p.037302-2). This is an author assignment built on the measured mixing patterns and population.
- The `2+_3→2+_1` transition is `91.7%` M1 and `2+_3→2+_2` is pure M1 within limits; `4+_3→4+_1` is `97.8%` M1. M1 corrections remove earlier B(E2) discrepancies (PDF p.037302-2, Table I).
- `4+_3→3+_1` has no unique δ; pure M1 is excluded. The source therefore demonstrates both the power and the multi-solution boundary of angular-correlation extraction.
- Strong M1 components near 1.7 MeV are interpreted as evidence for mixed-symmetry/proton-neutron degrees of freedom beyond simple IBA-1; absolute M1 strengths are still needed for an unambiguous mixed-symmetry assignment (PDF p.037302-3).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KO01-1 | Three-angle γγ correlations and clean β-decay spectra determine unique mixing ratios for 18 low-spin `130Ba` transitions. | experimental-method-result | direct | PDF pp.037302-1–2, Fig.2, Table I | true |
| KO01-2 | `2+_3` decays contain dominant/pure M1 components, and `4+_3→4+_1` is 97.8% M1. | experimental-result | direct | PDF p.037302-2, Table I | true |
| KO01-3 | M1 corrections reconcile earlier `B(E2)` ratios for `2+_3` and `4+_3` branches with consistent-Q calculations. | model-data-comparison | mixed | PDF p.037302-2, Table I | true |
| KO01-4 | `4+_3→3+_1` has no unique mixing ratio; only pure M1 is excluded. | ambiguity/limitation | direct | PDF p.037302-2 | false |
| KO01-5 | Strong M1 admixtures near 1.7 MeV are consistent with mixed-symmetry states, but absolute M1 strengths are needed. | author-interpretation | indirect | PDF p.037302-3 | true |

## Summary

Königshofen *et al.* provide a direct three-angle angular-correlation determination of 18 `130Ba` mixing ratios. The results correct B(E2) systematics and expose strong M1 components in higher collective states, while preserving a concrete no-unique-solution case.

## Competing Interpretations and Limitations

Spin/parity hypotheses, detector-pair efficiency corrections, Rose–Brink sign convention and assumed pure-E2 reference transitions are part of the inference. A unique intersection in two ratios is source-specific; rows marked estimated/asterisk or without a unique δ cannot be treated as equally precise. Mixed-symmetry interpretation requires absolute M1 strengths and independent structure evidence.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| KO01-AR-1 | Observable chain | Detector-angle yields → efficiency-corrected `W` ratios → angular-correlation curves → δ and multipolarity → M1-corrected branching/B(E2). | PDF pp.037302-1–2, Fig.2, Table I | self-checking |
| KO01-AR-2 | Convention | δ signs follow Rose–Brink; cross-source use requires convention mapping. | Table I caption; Ref.14 | self-checking |
| KO01-AR-3 | Transfer condition | Ratios and sensitivity depend on Osiris-8/cluster geometry and three fixed angles; no universal detector calibration follows. | PDF p.037302-1 | self-checking |
| KO01-AR-4 | Failure condition | Contamination/asterisk rows, assumed pure transitions and unresolved δ branches can alter B(E2) correction. | Table I; PDF pp.037302-2–3 | active-L3 |
| KO01-AR-5 | Independence | Direct `130Ba` experiment; cited 128Xe/126Xe/132Ce mixed-symmetry studies are background, not new measurements here. | Introduction/References | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` and `methodological-bridge` for angular-correlation/mixing-ratio analysis; `revises` the assumption that low-spin `130Ba` B(E2) tables can be read without M1 corrections.
- Persistence: update [[angular-correlation]], [[multipole-mixing-ratio]], [[a130-high-spin-collective-modes-evidence-map]] and the A≈130 γ-soft/mixed-symmetry map.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[angular-correlation]] | Three-angle `W` ratios and unique/multi-solution δ inference. |
| supports | [[multipole-mixing-ratio]] | Direct Rose–Brink sign-convention and M1-corrected B(E2) example. |
| supports | [[gamma-soft-deformation]] | Low-spin `130Ba` collective/mixed-symmetry context; does not by itself fix γ softness. |
| candidate-L3 | [[a130-high-spin-collective-modes-evidence-map]] | Compare robust δ rows with wobbling/signature/chiral candidate evidence requirements. |

## Human Review Triage

### P0

- `KO01-P0-1`: preserve the Rose–Brink δ convention and detector-angle calibration; do not transplant Table I values to another array or convention.

### P1

- `KO01-P1-1`: asterisk/estimated rows and the unresolved `4+_3→3+_1` δ need original spectra or follow-up before paper-level quantitative use.
- `KO01-P1-2`: mixed-symmetry interpretation remains provisional without absolute M1 strengths.

## Extracted Pages

- Nuclei: `130Ba` (source-level low-spin map).
- Methods: [[angular-correlation]], [[multipole-mixing-ratio]]。
- Projects: [[a130-high-spin-collective-modes-evidence-map]]。

## L3/L4 Follow-up

- L3 question: how often do A≈130 low-spin angular-correlation datasets provide a unique δ once detector-angle coverage, reference transitions and M1 contamination are modeled consistently? Required counter-checks are convention mapping and unresolved-branch sensitivity.
- No L4 run: raw matrices/response files and a machine-readable Table I are not supplied.
