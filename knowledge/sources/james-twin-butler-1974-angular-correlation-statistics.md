---
type: source
title: "James, Twin and Butler 1974 - Statistical analysis of gamma-ray angular-correlation experiments"
aliases: [James Twin Butler 1974 angular-correlation statistics]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "The statistical analysis of γ-ray angular correlation experiments"
authors: [A. N. James, P. J. Twin, P. A. Butler]
journal: "Nuclear Instruments and Methods"
year: 1974
volume: 115
pages: "105-113"
pii: "0029-554X(74)90433-9"
canonical_source: "James, Twin & Butler, Nucl. Instr. Meth. 115, 105-113 (1974)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/DCO/1974_James et al_The statistical analysis of γ-ray angular correlation experiments.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/DCO/1974_James et al_The statistical analysis of γ-ray angular correlation experiments.pdf"
raw_sha256: "c629c42b34570b1a03f450d63feed892f22df864732a47ab02bfa2d9e2a8101a"
nuclei: [generic]
reactions: [generic-alignment-reaction]
experiments: [gamma-angular-correlation]
models: [least-squares, chi-square, alignment-model]
observables: [angular-distribution, mixing-ratio, alignment, confidence-interval]
methods: [statistical-analysis, DCO, angular-correlation]
tags: [angular-correlation, statistics, alignment, mixing-ratio, uncertainty]
---

# Statistical analysis of γ-ray angular-correlation experiments

## Bibliographic Record

- A. N. James, P. J. Twin & P. A. Butler, *Nucl. Instr. Meth.* **115**, 105–113 (1974), PII `0029-554X(74)90433-9`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/DCO/1974_James et al_The statistical analysis of γ-ray angular correlation experiments.pdf`。

## Scope and Reading Depth

- PDF pp.105–113 (9 pages) fully read: uncertain alignment, direct/indirect data, χ²/F tests, design-matrix rank, spin-hypothesis testing, mixing-ratio error estimates, variance components, fitting and alignment prescriptions.
- Not covered: implementation code and later covariance treatments.

## Key Results

- Angular-correlation fits should combine direct intensities/polarization, indirect δ measurements and uncertain alignment-model outputs in one statistical comparison; the alignment estimate is data with its own variance, not a fixed prior (PDF pp.105–108, Secs.2–4).
- `χ²` compatibility uses the number of data terms minus the rank of the design matrix. Correlated alignment/mixing parameters reduce independent degrees of freedom; incorrect rank inflates confidence or rejects valid spin hypotheses (PDF pp.106–109, Tables 1–2).
- `arctan δ` is recommended as a fitting coordinate because it is more uniformly spaced in the `(a2,a4)` plane; error estimates should be obtained from confidence intersections, not by reading a symmetric interval on δ (PDF pp.107–111, Sec.7, Fig.5).
- Internal errors from counting statistics and external errors from model/variance mismatch must be distinguished. If residual dispersion is too large, scale parameter errors by the estimated variance rather than claiming a precise δ (PDF pp.107–113, Secs.7.3–7.5).
- The paper warns that near a compensation between alignment and δ, an angular-distribution experiment may be intrinsically unable to separate them; additional γ rays, polarization or independent alignment information are required (PDF pp.107–109, Fig.2).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JT74-1 | Alignment-model uncertainty must enter the same χ²/design-matrix analysis as angular-correlation data. | statistics-result | direct | PDF pp.105–109 | false |
| JT74-2 | The effective degrees of freedom are `n−rank(design matrix)`, not simply the number of angle bins. | statistics-result | direct | PDF pp.106–109, Tables 1–2 | true |
| JT74-3 | `arctan δ` confidence intersections are preferable to symmetric δ error bars under nonlinear angular-response ovals. | uncertainty-method | direct | PDF pp.107–113, Sec.7 | true |
| JT74-4 | Alignment/δ compensation can make a single angular distribution non-identifying. | limitation | direct | PDF pp.107–109, Fig.2 | false |

## Summary

James, Twin and Butler provide the statistical discipline needed for angular-correlation and DCO mixing-ratio claims. Their practical message is that alignment, δ, calibration and model error belong in one covariance-aware fit; a small formal χ² or a symmetric δ interval is not evidence of unique identification by itself.

## Competing Interpretations and Limitations

- The recommended Gaussian/least-squares approximations rely on adequate counts and a locally quadratic statistic; nonlinear or bounded δ branches require confidence contours.
- Model alignment errors can dominate counting statistics; treating `σ/J` as exact understates uncertainty and overstates spin/multipole discrimination.
- Degrees-of-freedom and variance scaling are experiment-specific; do not transplant the paper's numerical thresholds without the design matrix.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| JT74-AR-1 | Data chain | Counts/polarization/δ/alignment estimate → design matrix → χ²/F test → spin-hypothesis confidence. | PDF Secs.2–6 | self-checking |
| JT74-AR-2 | Error chain | Internal counting variance + external alignment/model variance → covariance/design rank → confidence contour in `arctan δ`. | PDF Sec.7 | self-checking |
| JT74-AR-3 | Failure condition | Alignment/δ compensation or underestimated systematic error leaves the fit non-identifying. | PDF Fig.2, Secs.7–8 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-correlation]], [[angular-distribution]], [[multipole-mixing-ratio]], [[dco-ratio]] and self-audit of DCO/ADO fits.
- New reusable rule: every future δ or spin assignment should record alignment-model variance, design-matrix rank, confidence topology and independent-discriminator status.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `JT74-P0-1`: Do not report δ errors or spin confidence without including alignment/model covariance and correct effective degrees of freedom.

## Extracted Pages

- Methods/observables: [[angular-correlation]], [[angular-distribution]], [[multipole-mixing-ratio]], [[dco-ratio]]。
