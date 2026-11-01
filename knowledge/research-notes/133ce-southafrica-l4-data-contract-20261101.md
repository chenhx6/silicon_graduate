---
type: research-note
title: "133Ce South Africa user-data L4 contract"
aliases: [133Ce iThemba 2019 data contract, South Africa 133Ce L4 readiness]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
visibility: private
publication_status: local-only-unpublished-user-data
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [userdata-133ce-southafrica-dataset]
created_from: "User-authorized South Africa 133Ce data audit and L4 readiness task"
tags: [133ce, l4, user-data, data-lineage, ado, dco, pdco, matrix, ithemba]
---

# `133Ce` South Africa user-data L4 contract

## Research Trigger

The user supplied a large South Africa data archive and requested a reproducible
L4-oriented audit for `133Ce`, including data organization, calculation checks,
and possible ROOT/Geant4/LISE++ follow-up.

## User-data boundary

The user explicitly designated `raw/data/SouthAfrica` as experimental data and
defined the semantic partition:

1. `SouthAfrica/` identifies the South Africa/iThemba experiment location.
2. `SouthAfrica/133Ce_iThemba2019/` is the acquisition, calibration and
   matrix-processing layer, including cube/matrix products and original
   calibration/sorter information.
3. `SouthAfrica/133Ce/` is the derived `133Ce` result and systematics layer,
   including later analysis sheets, figures and online/systematic comparison
   material.

The directory audit confirmed the partition and the user then authorized a
targeted cleanup. Experiment metadata and sorter configuration now sit in
`133Ce_iThemba2019/experiment/` and `133Ce_iThemba2019/config/`; derived
figures, the exported intensity workbook and analysis code sit under
`133Ce/analysis/`. The second pass places the supplied ROOT matrices in
`133Ce_iThemba2019/mat/root/` and calibration spectra in
`133Ce_iThemba2019/calibration/source-spectra/`, consistent with the user's
fixed-input definition. Three named backup drawings were moved to
`133Ce/analysis/archive/`. Four utility copies that were byte-for-byte
identical to retained shared copies were removed; the pre-change hashes and
all destinations are recorded in
`outputs/l4/20261101-133ce-southafrica-data-audit/raw-cleanup-plan-20261101.json`.
The second-pass file ledger and verification receipt are
`fixed-input-reclassification-plan.json` and
`fixed-input-reclassification-receipt.json` in that same audit directory.

## Minimum observable contract

The current workbook and matrix set can support a first audit of:

- calibrated energy and efficiency;
- ADO ratios and their count-level numerator/denominator;
- DCO ratios and gate/transition efficiency factors;
- linear-polarization asymmetry and analyzing-power correction;
- mixing-ratio interval fields and branching-ratio transformations;
- cross-nucleus wobbling-frequency comparison as a derived, non-independent
  systematic layer.

The contract requires each result to retain gate energy, counts, uncertainty,
efficiency/calibration version and matrix/source path.

## L4 readiness

The data are **partial-L4-ready**. The local files contain enough material to
recompute spreadsheet formulas and inspect matrix objects. They do not yet
prove a reproducible event-level result because response covariance, producer
history, background treatment and holdout lineage are not closed. The first
audit is therefore arithmetic and provenance validation, not a nuclear-structure
claim.

## Reproducible artifact

The first audit artifact is:

`outputs/l4/20261101-133ce-southafrica-data-audit/report.md`

The script and machine-readable output are:

- `outputs/l4/20261101-133ce-southafrica-data-audit/audit_133ce_workbook.py`
- `outputs/l4/20261101-133ce-southafrica-data-audit/workbook-audit.json`

The output must remain separate from `raw/data/SouthAfrica`; it is a derived
audit artifact and can be regenerated after Docker restarts.

## Grounded Evidence

The grounded data identity is recorded in
[[userdata-133ce-southafrica-dataset]] `SA-DATA-1`–`SA-DATA-3`. The workbook
formula audit and ROOT inspection are reproducible artifacts under
`outputs/l4/20261101-133ce-southafrica-data-audit/`.

## Provisional Reasoning

The archive is a partial-L4-ready input because it contains matrices,
calibration, sorter configuration and derived observables. This does not yet
mean that an event-level likelihood or nuclear-structure claim has been
reproduced.

## Assumptions

- File paths and workbook formulas are treated as user-provided provenance,
  not as independently published experimental source.
- Cached spreadsheet values are compared against formulas without assuming that
  the cached workbook was produced by the current software version.
- ROOT object dimensions are treated as structural checks only.

## Competing Explanations

Differences among `133Ce` analysis sheets could arise from gate definitions,
calibration versions, background subtraction, detector response, matrix export
versions or genuine nuclear-structure effects. The current audit does not rank
these explanations.

## Transfer Conditions

Any result transferred to `131Ce`, `133Ce` systematics, `135Pr` or another
nucleus must retain reaction/source lineage, detector response, gate rules,
uncertainties and an independent holdout. Similar workbook formulas do not
make the experiments independent.

## Failure Conditions

Stop at partial L4 readiness if producer identity, event-to-matrix provenance,
response covariance, background treatment or holdout data cannot be recovered.
Do not fill those gaps with toy counts, a model posterior or a borrowed
efficiency.

## Falsification or Reverse Tests

Recompute ADO/DCO/asymmetry from raw stored count fields; compare selected
matrix projections with the derived workbook; vary calibration and gate
versions; and reserve one gate family as a holdout. A claimed transition or
mode should be lowered if the result changes under these response-preserving
checks.

## Open Questions

- Which sorter build and calibration version produced each `mat/` and `cube/`
  product?
- Which background/random/sideband windows entered the stored ADO, DCO and
  asymmetry values?
- Can ROOT/cube objects be mapped to event or gate identifiers?
- Can Geant4 reproduce the polarization and efficiency response with a
  documented geometry?

## Human Review

This page records a Codex self-audit of user-supplied data and remains
`unreviewed`; it does not set `human-reviewed`.

## Promotion or Rejection History

2026-11-01: created as a provisional partial-L4 data contract. No experimental
claim, curriculum credit or full L4 result was promoted.

## Data locators

| ID | User-data locator | Meaning |
|---|---|---|
| SA133CE-1 | `raw/data/SouthAfrica/133Ce_iThemba2019/133Ce - calibration/133Ce calibration file.xlsx`, sheets `PDCO Cali`, `ADO Cali`, `Energy Cali` | calibration inputs and response controls |
| SA133CE-2 | `raw/data/SouthAfrica/133Ce/analysis/intensity_iThemba2019_export.xlsx`, sheets `ADO`, `DCO`, `Asymmetry`, `delta`, `branchingratio` | derived count-level observables and workbook formulas |
| SA133CE-3 | `raw/data/SouthAfrica/133Ce_iThemba2019/config/PR295offline`, `PR295offline75_95.dat`, `cube/sort/readme` | sorter channel layout, gain arrays and cube production route |
| SA133CE-4 | `raw/data/SouthAfrica/133Ce_iThemba2019/cube/ce.cub`, `cube/ce.scr`, `cube/mapfile.dat`, `cube/ener.cal` | processed cube and calibration/provenance inputs |
| SA133CE-5 | `raw/data/SouthAfrica/133Ce_iThemba2019/mat/root/g45allmatprompt.root`, `g90allmatprompt.root`, `gg.root`, `hgg.root`, `vgg.root` | supplied fixed-input ROOT TH2 representations inspected with ROOT |
| SA133CE-6 | `outputs/l4/20261101-133ce-southafrica-data-audit/matrix-content-audit.json` | bin-by-bin comparison of the five ROOT representations with candidate `.m4b` binaries |

The integer bin comparison shows that the supplied ROOT matrices do not form
a uniform coincidence sample. `g45` and `g90` match `g45allmatprompt.m4b` and
`g90allmatprompt.m4b` directly with zero bin mismatches. `gg`, `hgg` and
`vgg` do not match `ggmatprompt.m4b`, `hggmatprompt.m4b` or
`vggmatprompt.m4b`; instead, each matches `ggmat.m4b`, `hggmat.m4b` and
`vggmat.m4b` without the prompt label. The prompt versions of the latter three
matrices contain fewer counts. The gate logic, prompt time cut, Doppler
correction, detector efficiency and event-level covariance remain
unresolved; these matrix objects cannot be pooled without determining the
underlying acquisition and timing windows.

The first ROOT inspection found all five selected files readable as `TH2I`
objects with `4096×4096` bins, channel ranges `[0,2048]` on both axes and
approximately `1.67772×10^7` entries. This verifies file readability and matrix
shape only; it does not verify event provenance, gate contents or response
covariance.
