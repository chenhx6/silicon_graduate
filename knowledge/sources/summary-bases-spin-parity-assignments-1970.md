---
type: source
title: "Nuclear Data Sheets 1970 - Summary of bases for spin and parity assignments (1970)"
aliases: [Summary of Bases 1970]
created: 2026-09-21
updated: 2026-11-22
status: ai-draft
review_status: unreviewed
source_type: data-sheet-method-summary
reading_depth: deep-read
title_original: "Summary of Bases for Spin and Parity Assignments - 1970"
authors: [Nuclear Data Sheets editorial compilation]
journal: "Nuclear Data Sheets"
year: 1970
citation_key: "compilation_1970_assignment-methods-summary-bases"
pages: "iii-iv"
pii: "S0090-550X(70)80047-X"
canonical_source: "Nuclear Data Sheets 1970 summary of bases"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/1970_Summary of bases for spin and parity assignments — 1970.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/1970_Summary of bases for spin and parity assignments — 1970.pdf"
raw_sha256: "d8386bab5d0b6639354207e7149709c615bf4cf907303e5fc7e61a349a19487e"
archive_required: true
nuclei: [assignment-methods]
reactions: [transfer, Coulomb-excitation, neutron-capture, high-spin-reaction]
experiments: []
models: [rotational-band, shell-model, Nilsson]
observables: [spin, parity, multipolarity, beta-gamma-polarization-correlation, angular-correlation, conversion-coefficient]
methods: [spin-parity-assignment]
tags: [spin-parity, polarization, angular-correlation, method-summary]
---

# Summary of bases for spin and parity assignments (1970)

## Bibliographic Record

- Nuclear Data Sheets editorial compilation, PII `S0090-550X(70)80047-X`, four-page scan with the proposition sheet on pp.iii–iv.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/1970_Summary of bases for spin and parity assignments — 1970.pdf`。

## Scope and Reading Depth

- PDF 1–2 (pp. iii–iv) contains the special introduction for the even \(A=230\)–242 issue and the assignment guide. The guide has 32 strong propositions and eight weak propositions. PDF 3–4 (pp. v–vi) contains E0 material and data-sheet notation.
- The later [[summary-bases-spin-parity-assignments]] adds rules specific to high-spin in-beam γ spectroscopy.

## Key Results

- Strong arguments include conversion coefficients, directional correlations, β–γ polarization correlation, transfer `L`, Coulomb excitation and rotational-band evidence (PDF1–2, propositions 1–32).
- Propositions 18–19 address β–γ polarization and allowed β transitions (PDF2, p. iv). The modern guide is the source for the DCO reference values and the typical \(\sigma/J\) condition.
- The sheet explicitly lists strong versus weak bases and notes that g factors, Nilsson interpolation, regional trends and nonobservation need supporting evidence (PDF p.iv).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SB70-1 | The guide gives conditions on conversion coefficients, directional correlations and nuclear reactions for spin/parity assignment. | method-guideline | direct | PDF1–2, propositions 3–32 | false |
| SB70-2 | The β–γ polarization propositions address allowed β transitions. | method-guideline | direct | PDF2, propositions 18–19 | false |
| SB70-3 | The guide classes regional interpolation and nonobservation as weak bases. | evidence-hierarchy | direct | PDF2, weak propositions 7–8 | false |

## Summary

The 1970 proposition sheet is an early evidence hierarchy for spin/parity assignment. It remains useful as historical context and self-audit guidance, but all numerical heuristics must be rechecked against the actual detector setup and alignment model.

## Competing Interpretations and Limitations

- The propositions are heuristic strength rankings, not universal likelihood thresholds.
- The polarization propositions depend on the transition type and the stated angular-correlation convention.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SB70-AR-1 | Evidence hierarchy | The guide ranks specified observations and relationships above regional extrapolation. | PDF1–2, strong and weak headings | self-checking |
| SB70-AR-2 | Transfer condition | Use the β–γ polarization relation within its stated allowed-transition and angle conditions. | PDF2, propositions 18–19 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: provides the historical comparison for [[summary-bases-spin-parity-assignments]] and the evidence framework for [[angular-correlation]].
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SB70-P0-1`: Keep the 1970 and later proposition sheets as separate source versions; never turn their typical thresholds into universal assignment rules.

## Extracted Pages

- Methods: [[angular-correlation]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]]。
