---
type: source
title: "User-supplied South Africa 133Ce dataset identity and analysis boundary"
aliases: [South Africa 133Ce data, iThemba PR295 133Ce user dataset, 133Ce user-data source]
created: 2026-11-01
archive_required: true
updated: 2026-11-01
status: ai-draft
visibility: private
publication_status: local-only-unpublished-user-data
review_status: unreviewed
source_type: user-data-archive
reading_depth: read
title_original: "South Africa 133Ce experiment data archive"
authors: ["User-supplied dataset"]
year: 2019
pages: "directory archive; workbook and matrix locators"
language: [en, zh]
canonical_source: "raw/data/SouthAfrica/"
source_url: "raw/data/SouthAfrica/"
citation_key: userdata_133ce_southafrica_dataset
raw_file: "raw/data/SouthAfrica/133Ce/analysis/intensity_iThemba2019_export.xlsx"
raw_sha256: "3ad110823a29c164d8d402a0c49b82bc4718e19b9fac49f8e3107512671d3455"
raw_storage_status: user-provided-local-data
matrix_manifest_file: "raw/data/SouthAfrica/133Ce/analysis/provenance/manifest.json"
matrix_manifest_sha256: "fd60a8560d6291cccbe7dd2b2cf148c55e1120f4afe96cdb117587ce608d747d"
nuclei: [133ce]
reactions: [user-data-experiment-archive]
experiments: [ithembalabs-pr295]
observables: [ado, dco, linear-polarization-asymmetry, mixing-ratio, branching-ratio]
methods: [gamma-gamma-coincidence, matrix-analysis, calibration]
tags: [user-data, 133ce, south-africa, ithemba, pr295, l4-readiness]
---

# User-supplied South Africa `133Ce` dataset

## Bibliographic Record

This page identifies the local user-supplied archive under
`raw/data/SouthAfrica/`. The source identity anchor is the
`133Ce/analysis/intensity_iThemba2019_export.xlsx` workbook with the SHA-256
recorded in the frontmatter. The directory itself is treated as raw user data
and is not copied into `knowledge/`.

## Scope and Reading Depth

The archive was inventoried at the directory level and selected workbooks,
sorter configuration, calibration files, ROOT matrices and cube products were
read sufficiently to define an L4 analysis contract. On 2026-11-01, the
user-authorized cleanup moved misplaced derived products into
`133Ce/analysis/`, placed experiment metadata and sorter configuration into
subdirectories of `133Ce_iThemba2019/`, archived three named backup drawings,
and removed only four bitwise-identical utility copies. The cleanup manifest
records the pre-change hashes and destinations. A second classification pass
follows the user's definition of fixed inputs: supplied ROOT matrices are in
`133Ce_iThemba2019/mat/root/`, and supplied calibration spectra and conversion
references are in `133Ce_iThemba2019/calibration/source-spectra/`. These paths
classify the supplied snapshot, not its unknown producer history.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SA-DATA-1 | The archive is partitioned into `133Ce_iThemba2019` acquisition/calibration/matrix inputs and `133Ce` derived-analysis/systematics outputs, under the South Africa experiment-location root. | data-identity-and-boundary | direct-local | `raw/data/SouthAfrica/` directory structure | true |
| SA-DATA-2 | `intensity_iThemba2019_export.xlsx` contains count-level Intensity, ADO, DCO, Asymmetry, delta and branchingratio sheets; the stored formula families can be recomputed from the workbook inputs. | data-observable | direct-local | `raw/data/SouthAfrica/133Ce/analysis/intensity_iThemba2019_export.xlsx`, named sheets | true |
| SA-DATA-3 | Supplied ROOT representations `g45allmatprompt.root`, `g90allmatprompt.root`, `gg.root`, `hgg.root` and `vgg.root` are readable TH2I matrices; the ROOT audit records their dimensions and axis ranges. | data-structure | direct-local | `raw/data/SouthAfrica/133Ce_iThemba2019/mat/root/`; `outputs/l4/20261101-133ce-southafrica-data-audit/inspect_133ce_root.C` | true |
| SA-DATA-4 | Bin-by-bin integer comparison establishes that `g45allmatprompt.root` and `g90allmatprompt.root` reproduce the corresponding `prompt` m4b arrays, while `gg.root`, `hgg.root` and `vgg.root` reproduce `ggmat.m4b`, `hggmat.m4b` and `vggmat.m4b` without the prompt label. | data-export-provenance | direct-local | `outputs/l4/20261101-133ce-southafrica-data-audit/matrix-content-audit.json` | true |

## Summary

The archive is a viable user-data entry point for partial L4 work. It supports
reproducible workbook and matrix audits, while event producer identity,
response covariance, background handling and independent holdout remain open.

## Competing Interpretations and Limitations

Derived spreadsheet values are not independent measurements. ADO, DCO, PDCO,
asymmetry and mixing-ratio conclusions depend on calibration, gate, detector
response and analysis-version provenance. The current source page establishes
data identity and scope only; it does not certify a wobbling, chirality or
systematics claim.

## Extracted Pages

- `SA-DATA-1`: raw directory partition and file inventory.
- `SA-DATA-2`: workbook sheets and formula audit.
- `SA-DATA-3`: selected ROOT matrix readability audit.
- `SA-DATA-4`: binary-to-ROOT matrix content equivalence audit.

## Human Review

This page records a Codex self-audit of user-supplied data and remains
`unreviewed`; it does not set `human-reviewed`.
