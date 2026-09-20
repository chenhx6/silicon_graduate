---
type: source
title: "Macchiavelli et al. 2018 - Erratum: spectroscopic factors in 11,12Be"
aliases: [Macchiavelli 2018 erratum Nilsson spectroscopic factors]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-erratum
reading_depth: deep-read
title_original: "Erratum: Analysis of spectroscopic factors in 11Be and 12Be in the Nilsson strong-coupling limit"
authors: [A. O. Macchiavelli, H. L. Crawford, C. M. Campbell, R. M. Clark, M. Cromaz, P. Fallon, M. D. Jones, I. Y. Lee, M. D. Salathe]
journal: "Physical Review C"
year: 2018
volume: 97
article: 049902
pages: "1"
doi: "10.1103/PhysRevC.97.049902"
canonical_source: "https://doi.org/10.1103/PhysRevC.97.049902"
library_file: "raw/papers/gpt/high-spin-20260920/三轴/进动/实验/2018_Macchiavelli et al_Erratum.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/三轴/进动/实验/2018_Macchiavelli et al_Erratum.pdf"
raw_sha256: "772804ce5ddf6817024757cede56cabcff9efbbf10d221b04bac2e1f661f7e84"
nuclei: [11Be, 12Be, 13Be, 13B]
reactions: [12Be(d,p)13Be, 13B(d,3He)12Be]
experiments: []
models: [Nilsson-strong-coupling]
observables: [spectroscopic-factor]
methods: [transfer-reaction-analysis]
tags: [erratum, spectroscopic-factor, Nilsson, Be-isotopes]
---

# Macchiavelli et al. 2018 erratum

## Bibliographic Record

- *Physical Review C* **97**, 049902(E) (2018), DOI `10.1103/PhysRevC.97.049902`.
- One-page erratum; the supplied batch row is a correction notice, not the original `PRC 97, 011302(R)` paper.

## Scope and Reading Depth

- Read the correction formulas and revised Table II. The error concerns predicted spectroscopic factors for `12Be(d,p)13Be`; authors state main conclusions are unaffected.
- Original article, minimization data and source-code are not supplied in this row.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MC18-1 | Corrected formulas are `S(0+,1/2+)=C²_{1/2,0}β²`, `S(0+,5/2+)=13 C²_{5/2,2}β²`, and `S(0+,1/2−)=C²_{1/2,1}α²`; revised Table II gives corrected factors. | correction | direct | PDF p.049902-1, formulas/Table II | true |
| MC18-2 | Authors state the correction does not alter the original conclusions. | author-statement | direct | PDF p.049902-1 | true |

## Summary

This erratum is an identity-correction and reproducibility boundary for a Nilsson spectroscopic-factor paper; it is not directly relevant to the A≈130 high-spin map beyond demonstrating correction lineage.

## Competing Interpretations and Limitations

Without the original paper and fit amplitudes, the revised numerical table cannot be independently rederived; do not treat this notice as a complete experiment/source.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| MC18-AR-1 | Correction scope | Table II/formula correction is localized; main conclusions are author-stated unaffected. | PDF p.049902-1 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `no material change` to the high-spin target map; record erratum/source identity only.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `MC18-P0-1`: do not quote corrected factors without the original paper's amplitude/uncertainty context.

## Extracted Pages

- Source-only erratum; no new high-spin concept, nucleus or project page created.
