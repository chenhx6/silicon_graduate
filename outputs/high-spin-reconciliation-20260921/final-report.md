---
type: output
title: "High-spin full knowledge reconciliation report"
created: 2026-09-21
updated: 2026-09-21
status: complete
review_status: unreviewed
tags: [high-spin, synthesis, l3, l4, external-research]
---

# High-spin full knowledge reconciliation report

## Corpus and audit state

The source corpus remains 127 ledger rows: 118 valid, 9 user-confirmed exclusions, 110 unique hashes and 8 exact duplicate rows. Source identity and raw hash checks pass. The earlier HS-095 source-slug mismatch was corrected and recorded as an append-only correction event. Four cross-source synthesis pages and four L3 research units were added; no L4 run was started because complete event/response/code inputs were not available.

## Main synthesis findings

1. **Angular and polarization methods:** δ, alignment, detector response, efficiency, state order and phase convention must be fitted as one evidence chain. Historical tables and modern arrays supply transferable equations, not transferable numerical calibration constants.
2. **Lifetimes and deformation:** `136Nd` and `134Pr` counterexamples show that near-degeneracy cannot replace partner-resolved strengths, alignment and crossing checks. `136Nd` D5 remains stronger than D1–D4 rather than representing five equal confirmations.
3. **Chirality and wobbling:** candidate labels remain pair-specific and model dependent. Guo 2024's supplement closes its transition-table gap, while configuration and PRM dependence remain.
4. **Octupole and rare decay:** Bucher 2016 and external Bucher 2017 give direct E3 strengths in `144Ba` and `146Ba` near `48 W.u.`; E1 variation is not a direct proxy for E3 strength. Walz/Söderström agree on the `137Ba` branch but differ in virtual-path ranking, making energy sharing the decisive L3 discriminator.

## External research

`EXT-20260921-001` was added from the lawful open-access arXiv copy of Bucher et al., PRL 118, 152504 (2017). The six-page paper was read end-to-end, hashed, and linked to the octupole synthesis. It adds direct `146Ba` E3 evidence without changing the original 127-row denominator. The Walz Table 1 OCR transcription was also corrected after visual PDF inspection.

## L3/L4 status

Completed L3 units:

- `L3-2G-PATH-001`: double-γ virtual-path separation; open response/data boundary;
- `L3-CHIRAL-PAIR-002`: minimum partner evidence; pair-specific gaps;
- `L3-OCT-E3-E1-003`: direct E3 versus E1/shape evidence ladder;
- `L3-ADO-DELTA-004`: alignment/δ/detector identifiability.

L4 is `not-started`: no selected question has a complete public event matrix, detector response, covariance and analysis-code package.

## Knowledge-base changes

Updated the global index, overview, research questions, A≈130 and chirality projects, polarization project, octupole concepts, two-photon concept, and four new synthesis pages. QMD collection update indexed 531 knowledge files; 2605 vectors are present, no pending vectors remain, and 441 historical orphan chunks are retained as optional cache cleanup.

## Verification

- Wiki lint: `errors=0`.
- Ledger rows/raw hashes: pass (`127 / 118 / 9 / 110`).
- Protected BibTeX preflight: pass.
- `git diff --check`: pass before staging.
- Remaining untracked inputs are the user-provided reading record and prior temporary reading directories; they are outside the publication scope.
