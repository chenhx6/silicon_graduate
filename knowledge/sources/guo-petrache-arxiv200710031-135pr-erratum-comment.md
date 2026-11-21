---
type: source
title: "Guo and Petrache — Comment on the 135Pr polarization erratum"
aliases: []
created: 2026-11-21
updated: 2026-11-21
status: active
review_status: unreviewed
source_type: preprint
reading_depth: read
title_original: "Comment on Erratum: Negative-parity high-spin states and a possible magnetic rotation band in 135Pr"
authors: [S. Guo, C. M. Petrache]
year: 2020
pages: 2
arxiv: 2007.10031v2
canonical_source: "https://arxiv.org/abs/2007.10031v2"
raw_file: "raw/papers/gpt/query/20261121-135pr-polarization-correction/guo-petrache-2007.10031v2.pdf"
raw_sha256: "5eaed35823008713910be2dcd4b6f6d057f67c38e725814428d13c0b2f618efc"
raw_storage_status: archived-local
archive_required: true
nuclei: [135pr]
tags: [polarization, calibration, mixing-ratio, erratum]
---

# Guo and Petrache — Comment on the 135Pr polarization erratum

## Bibliographic Record

S. Guo and C. M. Petrache, arXiv:2007.10031v2 (2020). The arXiv record identifies a two-page comment. Journal publication status remains unverified.

## Scope and Reading Depth

PDF 1–2 read, with visual verification of Table I and Eqs. (3)–(5). Source inputs are the 2015 article and its 2019 erratum. The original coincidence counts, calibration covariance, and actual re-extraction procedure are unavailable.

## Summary

The authors test whether the new asymmetries in the Garg erratum could follow from changing the geometrical correction \(a(E)\) with the former perpendicular-to-parallel count ratios held fixed. The published central values require a change in the effective count ratios under the reported model. The source argues that background subtraction and statistical errors may affect the multipolarity inference.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GP20-PR-1 | Eq. (2) defines \(R=N_\perp/N_\parallel=(1+\Delta)/[a(1-\Delta)]\). With that \(R\) fixed and the erratum's \(a(E)\) substituted, Eq. (3) gives \(\Delta=-0.007,-0.159\) for 747.5 and 813.3 keV. The revised table gives \(+0.03(3),+0.04(3)\). The corresponding old/new effective \(R\) pairs are \(0.973/1.048\) and \(0.717/1.069\). | conditional-recalculation | direct | PDF 1 Eqs. (1)–(2), PDF 2 Eq. (3) and Table I | false |
| GP20-PR-2 | Recalculation from the 21 printed \(\Delta_{\rm old}\) values, \(a_{\rm old}=0.93\), and the erratum's function reproduces the \(\Delta_{\rm deduced}\) column within rounding. Eq. (4) prints a plus sign for the quadratic term in its numerator. Subtracting \(\Delta_{\rm old}\) from Eq. (3) gives the numerator \((a_{\rm new}-a_{\rm old})(1-\Delta_{\rm old}^2)\). This sign correction leaves the Eq. (3) comparison intact. | independent-algebra-and-table-check | derived | PDF 2 Table I and Eqs. (3)–(4) | false |
| GP20-PR-3 | The possibility of re-extracted counts and underestimated errors is the authors' explanation. The printed central values alone cannot determine the actual reason for the changes or assign a significance to them. | author-interpretation-and-evidence-boundary | indirect | PDF 2 final discussion | false |

## Competing Interpretations and Limitations

The published values establish a conditional inconsistency under unchanged effective counts. The calibration change, detector selection, and background subtraction may affect different steps. The comment does not supply separate measurements of those effects or a new \(E2/M1\) mixing ratio.

## Extracted Pages

- PDF 1, Eqs. (1)–(2), and Fig. 1 for the counting convention and calibration.
- PDF 2, Table I, Eqs. (3)–(5), and Fig. 2 for the conditional comparison.

## Related Sources

- [[garg-2015-135pr-magnetic-rotation]] — original angular and asymmetry measurements.
- [[garg-2019-135pr-polarization-erratum]] — the corrected asymmetry table from the same experiment.
- [[matta-2015-transverse-wobbling-135pr]] — separate experimental report cited for comparison.
- [[lv-2022-evidence-against-wobbling-135pr]] — later independent \(P\) and angular-ratio measurement.
