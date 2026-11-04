---
type: l4-report
title: "P-ADO alignment-response manuscript submission readiness"
created: 2026-11-05
updated: 2026-11-05
status: partial
visibility: private
publication_status: local-draft
review_status: unreviewed
nuclei: [67ga]
tags: [pado, alignment, epja, submission-readiness, evidence-gate]
---

# P-ADO alignment-response manuscript submission readiness

## Scope

This report audits the current local manuscript package
`raw/writing/gpt/pado-alignment-response-dependence/` against the user-requested
single-innovation paper objective and the current EPJA route. It does not admit
claims into the final paper evidence gate and does not replace user/author review.

## Gate results

| Gate | Status | Evidence | Boundary |
|---|---|---|---|
| Single central innovation | pass | `main.tex`, P-ADO project page | The paper tests reaction-dependent alignment response and maximum-row coverage |
| Public benchmark identity | pass | `data/zobel83_958_table1.csv`, Zobel source page, `sources/zobel-covariance-audit.md` | The input is a fitted public table, not raw spectra |
| Reproducible analysis | local pass / public pending | `analysis/profile_alignment_models.py`, `coverage_check.py`, `coverage_grid.py`, `profile_coverage.py`, `validate_outputs.py` | Table-level Gaussian contract; public repository/DOI and author metadata remain open |
| Reproducible figures | pass | `figures/made/generate_figures.py`, two PDF/PNG figures | Figure producer uses derived JSON/table inputs |
| Manuscript compilation | pass | `analysis/results/compile-record.json`, `main.pdf` | Tectonic 0.17.0 with Springer Nature `iicol`; six-page A4 PDF; underfull layout warnings remain |
| Source provenance | pass | `sources/README.md`, `sources/claim-ledger.md`, archived Zobel source | Exact source locator is recorded |
| Current covariance treatment | partial | common-\(\rho\) profile, \(5\times7\) fixed-\(\rho\) grid and profile-preserving toy calibration | Source does not publish numerical row or cross-row covariance |
| Event-level reanalysis | not ready | Zobel source has no raw event counts or response matrix | Cannot claim event-level likelihood or detector-response reconstruction |
| Feeding-aware physics model | partial | global convex-mixture negative control | Mixture is weakly identified and is not a direct/cascade feeding fraction or validated simulation |
| Paper-use claim review | not ready | P0/P1 ledger exists | No targeted user confirmation or human review has occurred |
| Author/collaboration metadata | not ready | Placeholder author block in `main.tex` | Must be completed before submission |
| Data Availability Statement | partial | `main.tex` and local data README | Must be checked against final author/data permissions |
| EPJA route | candidate | journal route note and archived official pages | Recheck official submission page immediately before submission |

## Scientific result currently supportable

Under the declared table-level Gaussian contract:

- the shared alignment profile has \(r_0=0.280146\) at \(\rho=0\);
- family, energy-dependent and minimal direct/cascade mixture extensions do not
  improve AIC/BIC at the center covariance contract;
- the observed shared-model maximum discrepancy remains large after profiling
  \(\rho\), with refined minimum \(D_{\max}^2=22.18\) at \(\rho=0.64\);
- profile-preserving toy maximum-statistic 95% quantiles are approximately
  \(8.27\)--\(8.65\) for true \(\rho=-0.6,0,0.6\);
- forcing \(\rho=0\) when the generating toy has nonzero correlation lowers
  empirical coverage in some grid cells to approximately \(0.47\) at the edge
  of the scanned negative-correlation range.

These results support a **conditional alignment-transfer and coverage warning**.
They do not identify a unique physical feeding model, invalidate P-ADO generally,
or provide an experimental mode-selection significance for an A≈130 nucleus.

## Hard evidence boundary

The direct PDF audit shows that Zobel et al. discuss error ellipses and
\(\alpha_2\)-\(\alpha_4\) dependence but do not provide numerical covariance,
raw angular counts, or detector response matrices. The current analysis therefore
cannot close the event-level likelihood gate. Searching for a missing numerical
covariance in the paper alone should stop here unless a separate archived source
or author-provided dataset becomes available.

## Required before a submission claim

1. Replace the placeholder author and affiliation block.
2. Obtain user/author confirmation of the exact P0/P1 manuscript wording.
3. Resolve the 1980/1983 source lineage and finite-\(J\) response-map convention.
4. Fill the public-release manifest with a permanent repository/DOI, license and
   author authorization.
5. Decide whether the table-level conditional result is sufficient for an EPJA
   Regular Article or whether an additional public data set is required.
6. Add a final covariance/feeding sensitivity appendix and state that it is a
   declared model contract.
7. Recheck EPJA submission requirements, data statement wording and template
   version immediately before any submission.

## Current disposition

`partial/not-ready`: the manuscript is a compiled, reproducible local candidate
with a defensible single innovation and a clear stopping boundary. It is not yet
a submission-ready paper because author metadata, targeted claim review, and the
missing source covariance/event-level evidence remain unresolved.

## Resume point

Continue from:

`raw/writing/gpt/pado-alignment-response-dependence/`

The next useful action is a targeted decision on the P0/P1 claims and the
accepted strength of the table-level conditional conclusion. If no additional
source covariance or raw data can be obtained, preserve the current
`partial/not-ready` state and use the report as the explicit stopping record.
