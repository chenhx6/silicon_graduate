---
type: source
title: "Nuclear Data Sheets 1970 - Summary of bases for spin and parity assignments"
aliases: [Summary of Bases 1970]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: data-sheet-method-summary
reading_depth: deep-read
title_original: "Summary of Bases for Spin and Parity Assignments - 1970"
authors: [Nuclear Data Sheets editorial compilation]
journal: "Nuclear Data Sheets"
year: 1970
pages: "iii-iv"
pii: "S0090-550X(70)80047-X"
canonical_source: "Nuclear Data Sheets 1970 summary of bases"
library_file: "raw/papers/gpt/high-spin-20260920/review/1970_Summary of bases for spin and parity assignments — 1970.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/1970_Summary of bases for spin and parity assignments — 1970.pdf"
raw_sha256: "d8386bab5d0b6639354207e7149709c615bf4cf907303e5fc7e61a349a19487e"
nuclei: [assignment-methods]
reactions: [transfer, Coulomb-excitation, neutron-capture, high-spin-reaction]
experiments: []
models: [rotational-band, shell-model, Nilsson]
observables: [spin, parity, multipolarity, DCO, polarization, angular-distribution, conversion-coefficient]
methods: [spin-parity-assignment]
tags: [spin-parity, DCO, polarization, angular-distribution, method-summary]
---

# Summary of bases for spin and parity assignments (1970)

## Bibliographic Record

- Nuclear Data Sheets editorial compilation, PII `S0090-550X(70)80047-X`, four-page scan with the proposition sheet on pp.iii–iv.
- 规范文件：`raw/papers/gpt/high-spin-20260920/review/1970_Summary of bases for spin and parity assignments — 1970.pdf`。

## Scope and Reading Depth

- Full four-page PDF read: strong/weak propositions for ground states, γ transitions, β decay, directional correlations, polarization, reactions, transfer, deformed bands, alpha/proton decay and magnetic moments.
- This 1970 sheet is a distinct historical compilation from the later compact 2010 sheet [[summary-bases-spin-parity-assignments]]; it is not an independent experiment.

## Key Results

- Strong arguments include multiple conversion coefficients, angular correlations, polarization, DCO/ADO, transfer `L`, Coulomb-excitation probabilities and consistent rotational-band evidence; generic systematics and nonobservation are weak arguments (PDF pp.iii–iv, propositions 1–36).
- Typical high-spin guidance is setup-specific: DCO near `1/0.5` or `2/1` under specified stretched gates, angular-distribution `A2/A4` patterns for dipole/quadrupole, and polarization signs under the stated correlation convention (PDF p.iv, propositions 13–19, 37).
- The sheet explicitly lists strong versus weak bases and notes that g factors, Nilsson interpolation, regional trends and nonobservation need supporting evidence (PDF p.iv).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SB70-1 | Spin/parity assignments should combine independent conversion, angular, DCO/polarization and reaction evidence. | method-guideline | direct | PDF pp.iii–iv, propositions 3–37 | false |
| SB70-2 | Typical high-spin DCO/angle/polarization values are conditional on gate, alignment and geometry. | limitation | direct | PDF p.iv, propositions 13–21, 37 | false |
| SB70-3 | Interpolation, nonobservation and generic g-factor/Nilsson arguments are weak bases. | evidence-hierarchy | direct | PDF p.iv, weak propositions 1–12 | false |

## Summary

The 1970 proposition sheet is an early evidence hierarchy for spin/parity assignment. It remains useful as historical context and self-audit guidance, but all numerical heuristics must be rechecked against the actual detector setup and alignment model.

## Competing Interpretations and Limitations

- The propositions are heuristic strength rankings, not universal likelihood thresholds.
- DCO, polarization and angular-distribution heuristics remain geometry-, alignment- and convention-dependent.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SB70-AR-1 | Evidence hierarchy | Direct observables and consistent multi-method convergence outrank regional/systematic guesses. | Propositions 1–37 | self-checking |
| SB70-AR-2 | Transfer condition | Historical thresholds are not universal; retain geometry, alignment, convention and source version. | Propositions 13–21, 37 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[summary-bases-spin-parity-assignments]], [[angular-correlation]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]] and batch-wide evidence gates.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SB70-P0-1`: Keep the 1970 and later proposition sheets as separate source versions; never turn their typical thresholds into universal assignment rules.

## Extracted Pages

- Methods: [[angular-correlation]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]]。
