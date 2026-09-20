---
type: source
title: "Hamilton & Davies 1968 - Angular correlation measurements in 192Pt"
aliases: [Hamilton 1968 192Pt mixing ratios]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-method
reading_depth: deep-read
title_original: "Angular correlation measurements in 192Pt"
authors: [W. D. Hamilton, K. E. Davies]
journal: "Nuclear Physics A"
year: 1968
volume: 122
pages: "165-176"
pii: "0375-9474(68)90710-0"
canonical_source: "Hamilton & Davies, Nucl. Phys. A 122, 165-176 (1968)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1968_Hamilton et al_Angular correlation measurements in 192Pt.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1968_Hamilton et al_Angular correlation measurements in 192Pt.pdf"
raw_sha256: "5a08c45e80c6793456ad892f68e97bf471c86b4ec69f57fe0920d179ec477f77"
nuclei: [192Pt, 192Ir]
reactions: [192Ir-beta-decay]
experiments: [sussex-Ge-NaI-angular-correlation]
models: [angular-correlation-formalism]
observables: [angular-correlation-coefficients, linear-polarization, E2-M1-mixing-ratio]
methods: [gamma-gamma-angular-correlation, linear-polarization-asymmetry]
tags: [192Pt, mixing-ratio, angular-correlation, polarization, historical-method]
---

# Angular correlation measurements in 192Pt

## Bibliographic Record

- W. D. Hamilton and K. E. Davies, *Nuclear Physics A* **122**, 165–176 (1968), PII `0375-9474(68)90710-0`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1968_Hamilton et al_Angular correlation measurements in 192Pt.pdf`。
- 12-page historical experiment; Ge+NaI cascade separation and summing polarimeter checked.

## Scope and Reading Depth

- PDF pp.165–176 fully read: `192Ir` decay scheme, composite 300/600-keV cascade separation, angular-correlation equations, random subtraction, linear-polarization formalism, Tables 1–2, Figs.1–8 and conclusions.
- Not covered: raw coincidence matrices, full detector-response files and later `192Pt` evaluations.

## Key Evidence and Reasoning Chain

- A Ge detector resolves individual lines while NaI selects the 300-keV complex; linear equations disentangle three overlapping cascades and remove the 588-316 contribution.
- Angular coefficients `A22/A44` are corrected for centering, finite source size and solid angle; a summing polarimeter at 90° correlation angle measures `W(γ=0/90)` and polarization.
- Reported E2:M1 mixing ratios are `δ(296)=−9.0 to −11.0`, `δ(308)=−6.5 to −8.3`, `δ(604)=+1.9 to +2.4`, with polarization selecting branches and confirming accepted spins.
- The method is designed to address poor Ge resolution/complex cascades and to inform possible E0 conversion-electron interpretations of the `2+→2+` transition.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HD68-1 | Ge+NaI composite angular correlations separate overlapping 296/308/316 and 588/604-keV cascade contributions. | method-result | direct | PDF pp.165–171, Figs.1–3 | true |
| HD68-2 | Polarization at 90° resolves electric/magnetic branch ambiguities in the directional-correlation mixing ratios. | method-result | direct | PDF pp.167–172, Tables 1–2 | true |
| HD68-3 | Mixing ratios are approximately δ(296)=−9…−11, δ(308)=−6.5…−8.3 and δ(604)=+1.9…+2.4. | experimental-result | direct | PDF pp.165, 172 | true |

## Summary

Hamilton & Davies demonstrate a practical resolution of complex low-resolution γγ cascades using a Ge/NaI hybrid and a summing polarimeter, yielding consistent E2/M1 mixing ratios for `192Pt`.

## Competing Interpretations and Limitations

Results depend on intensity/branching weights, internal-conversion coefficients, solid-angle/centering corrections and polarization sensitivity. Historical line-shape subtraction and convention mapping are required before modern quantitative reuse.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| HD68-AR-1 | Cascade chain | Composite coefficients → cascade separation → A22/A44 → polarization branch selection → δ. | PDF pp.166–172 | self-checking |
| HD68-AR-2 | Convention | δ signs and temporal order follow the paper's convention; cross-source Rose–Brink mapping required. | Table 2 notes | self-checking |
| HD68-AR-3 | Failure condition | Overlap subtraction/solid-angle/random corrections can bias small coefficients and δ. | PDF pp.167–172 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-correlation]], [[linear-polarization-asymmetry]] and [[multipole-mixing-ratio]].
- Persistence: historical method source; no new project-level scientific claim.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HD68-P0-1`: preserve convention, cascade weights and detector corrections before comparing δ across sources.

## Extracted Pages

- Methods: [[angular-correlation]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]]。
