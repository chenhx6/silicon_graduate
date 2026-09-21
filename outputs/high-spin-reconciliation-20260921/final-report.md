---
type: output
title: "High-spin full knowledge reconciliation report"
created: 2026-09-21
updated: 2026-09-21
status: complete-with-registered-residuals
review_status: unreviewed
tags: [high-spin, synthesis, l3, l4, external-research]
---

# High-spin full knowledge reconciliation report

## Corpus and audit state

The source corpus remains 127 ledger rows: 118 valid, 9 user-confirmed exclusions, 110 unique hashes and 8 exact duplicate rows. Source identity and raw hash checks pass. The earlier HS-095 source-slug mismatch was corrected and recorded as an append-only correction event. Four cross-source synthesis pages and four L3 research units were added. The residual pass also restored 19 local-BibTeX citation keys and 55 DOI-verified Crossref keys; 76 intentionally unmapped keys remain.

## Main synthesis findings

1. **Angular and polarization methods:** δ, alignment, detector response, efficiency, state order and phase convention must be fitted as one evidence chain. Historical tables and modern arrays supply transferable equations, not transferable numerical calibration constants.
2. **Lifetimes and deformation:** `136Nd` and `134Pr` counterexamples show that near-degeneracy cannot replace partner-resolved strengths, alignment and crossing checks. `136Nd` D5 remains stronger than D1–D4 rather than representing five equal confirmations.
3. **Chirality and wobbling:** candidate labels remain pair-specific and model dependent. Guo 2024's supplement closes its transition-table gap, while configuration and PRM dependence remain.
4. **Octupole and rare decay:** Bucher 2016 and external Bucher 2017 give direct E3 strengths in `144Ba` and `146Ba` near `48 W.u.`; E1 variation is not a direct proxy for E3 strength. Walz/Söderström agree on the `137Ba` branch but differ in virtual-path ranking, making energy sharing the decisive L3 discriminator.

## External research

`EXT-20260921-001` was added from the lawful open-access arXiv copy of Bucher et al., PRL 118, 152504 (2017). The six-page paper was read end-to-end, hashed, and linked to the octupole synthesis. It adds direct `146Ba` E3 evidence without changing the original 127-row denominator. `EXT-20260921-002` checks the public-data route for the `137Ba` re-fit: the cited Mendeley snapshot is currently unavailable, so the L4 readiness audit remains safe-suspended. `EXT-20260921-003` records the corresponding public-input scan for the chiral, octupole and ADO/δ units; all remain L3-only at the checked evidence boundary. The Walz Table 1 OCR transcription was also corrected after visual PDF inspection.

## L3/L4 status

Completed L3 units:

- `L3-2G-PATH-001`: double-γ virtual-path separation; open response/data boundary;
- `L3-CHIRAL-PAIR-002`: minimum partner evidence; pair-specific gaps;
- `L3-OCT-E3-E1-003`: direct E3 versus E1/shape evidence ladder;
- `L3-ADO-DELTA-004`: alignment/δ/detector identifiability.

L4 remains `not-started` as an analysis run. A readiness audit was completed for the highest-value `137Ba` candidate, but no complete public event matrix, detector response, covariance and analysis-code package was found. No figure-digitized or synthetic data were promoted as an L4 result.

## Knowledge-base changes

Updated the global index, overview, research questions, A≈130 and chirality projects, polarization project, octupole concepts, two-photon concept, four new synthesis pages, and the explicit source-provenance registry. The formal typed knowledge tree contains 529 pages; including the three root-level navigation pages, QMD indexes 532 Markdown documents with 2,172 current vectors, no pending vectors and no retained orphan chunks after compaction.

The whole `knowledge/` directory was then audited and re-audited: 529 pages were scanned for frontmatter, required sections, links, source claim tables and orphan status. Three malformed frontmatter pages and one alias collision were fixed; the former 59 graph orphans now have an explicit provenance hub. The element map and exact-channel parser were expanded and regression-tested; only three genuinely underdetermined reaction strings remain warnings. Residual citation-key and reaction warnings are registered with reasons in [global-audit-20260921.md](global-audit-20260921.md), [citation-key-audit.md](citation-key-audit.md), and [citation-key-crossref-registry.json](citation-key-crossref-registry.json).

## Verification

- Wiki lint: `errors=0`, `warnings=79`, `info=1106` (current residual state).
- Ledger rows/raw hashes: pass (`127 / 118 / 9 / 110`).
- Protected BibTeX preflight: pass.
- `git diff --check`: pass before staging.
- Remaining untracked inputs are the user-provided reading record and prior temporary reading directories; they are outside the publication scope.
