---
type: source
title: "Garg et al. 2019：135Pr 偏振不对称度勘误"
aliases: [Garg 2019 135Pr erratum, 135Pr polarization asymmetry correction]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: journal-article-erratum
reading_depth: deep-read
title_original: "Erratum: Negative-parity high-spin states and a possible magnetic rotation band in 135Pr"
authors: [Ritika Garg, S. Kumar, Mansi Saxena, Savi Goyal, Davinder Siwal, Sunil Kalkal, S. Verma, R. Singh, S. C. Pancholi, R. Palit, Deepika Choudhury, S. S. Ghugre, G. Mukherjee, R. Kumar, R. P. Singh, S. Muralithar, R. K. Bhowmik, S. Mandal]
journal: "Physical Review C"
year: 2019
volume: 100
pages: "069901(E)"
doi: "10.1103/PhysRevC.100.069901"
citation_key: Garg_2019_Erratum
canonical_source: "https://doi.org/10.1103/PhysRevC.100.069901"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/pr135-erratum-2019.pdf"
raw_sha256: "c9fbed8bb0a1463c6d083f29e1331ff72102f5fb4edfdd96b76f3c5c0149db30"
nuclei: [135Pr]
experiments: [INGA]
models: [polarization-asymmetry, DCO]
observables: [polarization-asymmetry, multipolarity]
methods: [gamma-ray-polarimetry, directional-correlation]
tags: [135Pr, erratum, polarization, magnetic-rotation, multipole-mixing]
---

# `135Pr` 偏振不对称度勘误

## Bibliographic Record

Garg *et al.*, *Phys. Rev. C* **100**, 069901(E) (2019), DOI `10.1103/PhysRevC.100.069901`. Public APS PDF: two pages, `%PDF-1.3`, SHA-256 recorded above. The erratum corrects the energy dependence of the clover geometric asymmetry used for polarization asymmetries.

## Scope and Reading Depth

Both printed pages were read, including the explanatory text and all Table I rows. The underlying coincidence counts, full covariance and a re-fit of the 2015 experiment were not obtained.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GE19-1 | The 813.3-keV line changes from the old polarization asymmetry `−0.20(8)` to `+0.04(3)` after using energy-dependent geometric asymmetry. | correction-result | direct | PDF p.1, Table I | true |
| GE19-2 | The 747.5- and 813.3-keV transitions are both assigned mixed `M1+E2` character in the corrected table. | experimental-criterion | direct | PDF p.1, Table I | true |
| GE19-3 | The correction factor is `a(Eγ)=1.01229+(1.17083×10−6)Eγ` with Eγ in keV, based on three 90° clovers. | method-result | direct | PDF p.1, Table I footnote b | true |
| GE19-4 | The authors state that the earlier results and interpretations are not affected; this does not supply absolute lifetimes or absolute B(M1). | author-scope | direct | PDF p.2 | true |

## Summary

The erratum removes the old large negative 813.3-keV polarization asymmetry as a current input and establishes mixed multipolarity for both 747.5 and 813.3 keV transitions. The original paper remains the source for its relative intensity analysis; the erratum is the current source for these corrected polarization values.

## Competing Interpretations and Limitations

The corrected mixed character supports a more cautious multipolarity assignment. It does not independently establish a magnetic-rotation band, determine absolute transition strengths, or resolve the 3qp/5qp TAC interpretation. No raw-count reanalysis was performed here.

## Model Dependence

The correction concerns detector geometric-asymmetry calibration and polarization ratios. It does not replace the original TAC model or provide a new structure calculation.

## Knowledge Impact and Learning Decision

`revises` the current status of the two 135Pr polarization rows in [[garg-2015-135pr-magnetic-rotation]]; `supports` retaining a possible-MR interpretation only with the mixed-multipolarity boundary. It does not upgrade the original candidate to an established MR band.

## Extracted Pages

- PDF pp.1–2, including Table I and the closing correction statement.

## Sources

- [[garg-2015-135pr-magnetic-rotation]] — corrected source paper, with erratum dependency.

## Review Status

Codex source self-audit; not `human-reviewed`.
