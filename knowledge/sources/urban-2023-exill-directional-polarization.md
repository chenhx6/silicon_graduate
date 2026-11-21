---
type: source
title: "Urban et al. 2023 — Directional-polarization correlations using EXILL"
aliases: [EXILL polarimetry, Urban 2023 directional-polarization]
created: 2026-11-21
updated: 2026-11-21
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Directional-polarization correlations using EXILL"
authors: [W. Urban, M. Czerwinski, G. de France, M. Jentschel, U. Koster, P. Mutti, T. Rzaca-Urban, J. Wisniewski]
year: 2023
journal: "Journal of Instrumentation"
volume: 18
pages: P11031
doi: "10.1088/1748-0221/18/11/P11031"
canonical_source: "https://doi.org/10.1088/1748-0221/18/11/P11031"
raw_file: "raw/papers/gpt/query/20261119-polarization-delta-collection/10.1088_1748-0221_18_11_p11031.pdf"
raw_sha256: "5a7c8af47e870e6ba44f04450e81cab04555731d9c50673b03c17bace68b68c9"
archive_required: true
nuclei: [132xe, 152gd, 152sm, 133cs]
tags: [angular-correlation, polarization, mixing-ratio, clover, exill]
---

# Urban et al. 2023 — Directional-polarization correlations using EXILL

## Bibliographic Record

W. Urban et al., *Journal of Instrumentation* **18**, P11031 (2023), doi:10.1088/1748-0221/18/11/P11031.

## Scope and Reading Depth

The local IOP PDF has 36 pages with a download wrapper, title page and 34 article pages. PDF 2–36 cover the theory, experiment, fitting and calibration, Tables 1–10, Appendices A–D, and references. The original coincidence matrices and per-run response files were unavailable.

## Summary

Eight EXOGAM clovers at PF1B formed the EXILL polarimeter. For initially unoriented ensembles, selecting one photon direction in a cascade conditions the polarization of the other photon. The opening-angle correlation and the direction–polarization correlation therefore provide distinct constraints on spin, parity and mixing ratio. The paper derives a formula for examining polarization of the first photon and tests both photon roles.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EX23-1 | The octagonal array groups the two-photon opening angles as \(0^\circ,45^\circ,90^\circ\), with \(180^\circ\) and \(135^\circ\) folded by even Legendre symmetry. The measured angular inputs are cascade \(a_2,a_4\). The instrumental asymmetry is calibrated separately from \(Q(E)\), and \(P_{\rm exp}=A/Q\). | experimental-method | direct | printed pp. 6–9, 12–17, Eqs. (3.3), (3.11), Figs. 3, 7–8 | false |
| EX23-2 | \(^{132}\mathrm{Xe}\) 630.2–667.7 keV, \(2^+\to2^+\to0^+\), gives \(\delta_{630}=+4.2(4)\) from the angular coefficients. Its measured \(P_{630}=+0.12(5)\) agrees with the \(+0.154(15)\) prediction. The combined result is \(+4.2(5)\). The angular coefficients already select one shared branch, and the polarization confirms the M1/E2 assignment. | experiment-result | direct | printed pp. 17–18, Table 5 and Fig. 9(a) | false |
| EX23-3 | In \(^{133}\mathrm{Cs}\), \(P(356.0)=+0.082(36)\) tests the mixing of the *other* photon, at 81.0 keV. Assuming the 356.0-keV branch is stretched E2, the measured value favors \(\delta(81.0)=-0.178(12)\) over the positive value associated with an earlier ICC magnitude. | experiment-result-with-cascade-condition | direct | printed pp. 17–19, Table 5 | false |
| EX23-4 | \(^{152}\mathrm{Sm}\) 688.7 and 1112.1 keV give \(\delta=12^{+5}_{-3}\) and \(-12(2)\) from angular correlation, with \(P_{\rm exp}=+0.16(8)\) and \(-0.26(3)\), respectively, gated in coincidence with 121.8 keV. For the 964.1-keV upper photon, \(P_{\rm exp}=-0.03(3)\) should be kept alongside the angular result \(\delta=-8.5(9)\) and prediction \(+0.046(4)\). The authors report a discrepancy for that photon. | experiment-result-and-limitation | direct | printed pp. 20–22, Tables 6–7 | false |

## Competing Interpretations and Limitations

These examples use relative photon directions and conditional polarization from initially unoriented ensembles. The angular coefficients, coincidence gates, and roles of each photon define the analysis. They provide evidence for a polarization–mixing-ratio survey without requiring a beam-axis Gaussian alignment width. Three opening-angle intensities determine three angular-distribution coefficients before normalization. Appendix D discusses propagated and systematic uncertainties, including limited knowledge of the instrumental asymmetry calibration curve. The paper neither fixes nor fits a beam-axis \(\sigma/I\) for these examples.

## Extracted Pages

- Printed pp. 2–5 and 27–32, upper and lower photon polarization formulas and experimental response.
- Printed pp. 17–23, \(^{132}\mathrm{Xe}\), \(^{133}\mathrm{Cs}\), and \(^{152}\mathrm{Sm}\) cascade and branch evidence.

## Related Sources

- [[davies-hamilton-1967-ta181-482kev-mixing-ratio]] — historical polarization and angular correlation branch analysis.
- [[kramer-flecken-1989-use-dco-ratios]] — oriented ensemble with a different angular observable.
- [[starosta-1999-pdco-experimental-test]] — in-beam clover calibration and conditional polarization gates.
