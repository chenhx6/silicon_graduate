---
type: research-audit
title: "High-spin corpus full knowledge impact map"
created: 2026-09-21
updated: 2026-09-21
status: active
review_status: unreviewed
---

# High-spin corpus full knowledge impact map

## Baseline

The execution ledger remains the row-level source of truth:

- 127 original rows;
- 118 valid rows and 9 user-confirmed exclusions;
- 110 unique SHA-256 values;
- 102 source-created rows, 8 reused/alternate-version rows, 7 duplicate-row audits and 1 attached-material audit;
- 106 unique source slugs in the current ledger. The HS-095 Kramp slug was reconciled to the existing page name `kramp-1987-160-two-photon-decay` during this audit.

The corpus is treated as read. This map audits whether the resulting claims can reach the rest of the Wiki and whether the rest of the Wiki needs an update.

## Evidence graph inventory

The source pages most often connect to the following reusable method and concept nodes:

| Target node | Approximate incoming source links | Audit priority | Reason |
| --- | ---: | --- | --- |
| `linear-polarization-asymmetry` | 73 | P0 | calibration, sign and detector-response claims span historical and modern arrays |
| `angular-correlation` | 61 | P0 | convention, state order, alignment and DCO/PDCO/PPCO transfer |
| `compton-polarimetry` | 55 | P0 | `Q(E)`, geometry, efficiency and background are repeatedly array-specific |
| `multipole-mixing-ratio` | 49 | P0 | δ sign, branch multiplicity and model/data separation |
| `angular-distribution` | 48 | P0 | `A2/A4`, ADO and alignment assumptions |
| `doppler-shift-attenuation-method` | 18 | P1 | stopping, feeding and absolute-strength propagation |
| `octupole-deformation` / `octupole-correlation` | 17 / 12 | P1 | direct E3 versus E1/systematics/PES evidence ladder |
| `nuclear-chirality-and-multiple-chiral-doublet-bands` | 8 | P0 | energy-degeneracy counterexamples and partner-strength requirements |
| `two-photon-nuclear-decay` | 11 | P0 | Walz/Söderström path conflict and rare-branch controls |
| `a130-high-spin-collective-modes-evidence-map` | 17 | P1 | cross-mass and method evidence needs current batch integration |

The link count is an impact signal, not an evidence score. A review or alternate version does not add an independent experiment.

## Planned update groups

### P0: source and method consistency

- Fix all source slug/file mismatches and parent/alternate/duplicate relations.
- Normalize claim tables and locators on sources touched by the batch.
- Reconcile the angular-distribution, angular-correlation, polarization and mixing-ratio method pages into one convention map.
- Add a single warning path for detector-specific `Q(E)`, alignment, finite-angle and efficiency transfer.

### P0: rare two-photon and chirality conflicts

- Update the double-γ concept with Walz SI and Söderström's independent energy-sharing result.
- Update the chirality project with the Mukhopadhyay 2008 and Petrache 2006 electromagnetic-strength counterexamples.
- Keep the Guo 2024 alternate PDF and supplement attached to the parent source.

### P1: collective modes, octupole and decay

- Add the direct `144Ba` E3 result to the octupole evidence ladder.
- Connect Dey 2026 to drip-line/continuum concepts with explicit low-statistics and data-availability boundaries.
- Connect `193Bi` isomer and SD evidence to the high-spin/isomer/shape-coexistence control map.

### Global entry points

- Refresh `knowledge/overview.md` counts and review-state wording.
- Add corpus-derived unresolved questions to `knowledge/questions.md`, preserving older questions and dates.
- Create topic synthesis pages only where at least two independent source lineages provide a real comparison.

## Known audit findings

1. HS-095's ledger slug was inconsistent with its existing source filename; the ledger and event were corrected to `kramp-1987-160-two-photon-decay`.
2. Source-only pages `macchiavelli-2018-erratum-spectroscopic-factors-be` and `walker-dracoulis-2001-exotic-isomers` have no inbound links outside the index; their reason for persistence must be made explicit.
3. `knowledge/overview.md` still reports earlier corpus snapshots and must be rewritten after the impact map is stable.
4. `knowledge/questions.md` predates this batch and does not yet contain the new double-γ path, chiral-pair strength, direct-E3 and convention-transfer questions.
5. QMD indexes the knowledge directory, but vector/index status must be recorded after the update; it is a retrieval aid and does not replace source/raw verification.

## Audit outputs

- Row-level mapping: `outputs/high-spin-learning-20260920/ledger.json`.
- Append-only corrections: `outputs/high-spin-learning-20260920/ledger-events.jsonl`.
- Machine-readable update register: `knowledge-update-ledger.json` in this directory.
- Next step: Task 2 source/identity reconciliation, followed by Task 3 claim and locator normalization.
