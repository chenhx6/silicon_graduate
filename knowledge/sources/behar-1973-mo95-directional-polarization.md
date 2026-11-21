---
type: source
title: "Behar, Garber and Grabowski 1973 - Directional and polarization correlations in 95Mo"
aliases: [Behar 1973 95Mo polarization]
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "Spins of the levels and multipole mixing ratios of the transitions in 95Mo"
authors: [M. Behar, D. A. Garber, Z. W. Grabowski]
journal: "Nuclear Physics A"
year: 1973
volume: 209
pages: "525-534"
doi: "10.1016/0375-9474(73)90844-0"
canonical_source: "Behar, Garber and Grabowski, Nucl. Phys. A 209, 525–534 (1973)"
raw_file: "raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_0375-9474_73_90844-0.pdf"
raw_sha256: "cda0a210581cb4d47401f6ce987310e80dad50be3e3282df115a027a1d34ed40"
archive_required: true
nuclei: [95Tc, 95Mo]
observables: [directional-correlation, linear-polarization-asymmetry, E2-M1-mixing-ratio]
tags: [decay-spectroscopy, gamma-gamma-correlation, polarization, mixing-ratio]
---

# Directional and polarization correlations in \(^{95}\mathrm{Mo}\)

## Bibliographic Record

M. Behar, D. A. Garber and Z. W. Grabowski, *Nuclear Physics A* 209, 525–534 (1973). DOI `10.1016/0375-9474(73)90844-0`.

## Scope and Reading Depth

Read the ten publisher pages (printed pp.525–534), including the Ge(Li) method, all three result tables, the spin assignments and the model comparison. PDF p.1 corresponds to printed p.525.

## Summary

The experiment populates \(^{95}\mathrm{Mo}\) through \(^{95}\mathrm{Tc}\) decay. Tables 1–3 give angle-correlation coefficients, measured polarization count ratios and the selected solutions. The coaxial detector selects the 204 keV ray in the polarization runs. \(\beta=N_\perp/N_\parallel\) is a measured count ratio at a two-photon opening angle of \(90^\circ\). The paper relates it to the gated polarization via \(\beta=(1+PQ)/(1-PQ)\), with \(Q=0.135\pm0.005\) in the energy region of interest. Printed pp.528–531, Secs. 2.3 and 3–4.

| Cascade, keV | \(A_{22}\) | \(A_{44}\) | Measured \(\beta\) | Final \(\delta\) of the first ray |
| --- | --- | --- | --- | --- |
| 582–204 | \(-0.306\pm0.010\) | \(-0.008\pm0.012\) | \(0.958\pm0.006\) | \(+0.266^{+0.052}_{-0.040}\) |
| 616–204 | \(+0.248\pm0.017\) | \(-0.010\pm0.018\) | \(0.981\pm0.043\) | \(-2.00\pm0.22\) |
| 835–204 | \(-0.200\pm0.007\) | \(-0.003\pm0.010\) | \(0.936\pm0.012\) | \(+0.038\pm0.019\) |
| 219–(616)–204 | \(-0.145\pm0.053\) | \(+0.012\pm0.075\) | | \(-19\le\delta\le-0.64\) |

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| BGG73-1 | The experiment reports relative-angle coefficients and a polarization count ratio with \(Q=0.135\pm0.005\). | experimental-observation | direct | pp.528–530, Sec. 2.3 and Tables 1–2 |
| BGG73-2 | Comparison of predicted and measured polarization count ratios is used to select the published \(\delta\) values at 582, 616 and 835 keV. | analysis-result | direct | pp.530–531, Tables 2–3 |

## Competing Interpretations and Limitations

- A NaI(Tl)–Ge(Li) spectrometer establishes the directional coefficients with finite solid-angle corrections. The agreement of the fits for \(A_{22}\) with \(A_{44}\) set free or set to zero is specific to these data. The sign convention is Krane–Steffen. \(\delta(204)=-0.60\pm0.05\) comes from Ref. 3 and is used as a companion-transition input. Printed pp.527–529, Secs. 2.2 and 3.1; see [[krane-steffen-1970-cd110-mixing-ratios]] for the convention.
- The authors predict \(\beta\) from the angular-correlation solutions, then compare with the polarimetry. For 582 keV the predicted ratios are \(0.966\pm0.004\) and \(1.035\pm0.004\) for the two roots with the adopted spin. For 835 keV the four candidates span two spins and the measured ratio supports \(J_i=1/2^+\), \(\delta=+0.038\). The ratio chiefly selects among precomputed candidates. Its role differs from a fit that jointly estimates both observables' uncertainties. Printed p.530 Table 2.
- For 616 keV the predictions are \(1.044\pm0.004\) and \(0.980\pm0.001\) for \(\delta=-0.215\pm0.045\) and \(-2.00\pm0.22\), respectively. The selected large-magnitude root is closest to the observation, and its reported E2 fraction is \(80\pm3\%\). The separation of the small root's prediction from the measurement is approximately \(1.46\) combined standard uncertainties if the reported errors are treated as independent. This is an audit calculation from Table 2 and is distinct from an exclusion at a stated confidence level. Table 3 records the authors' selection.
- \(A_{22}\) and \(A_{44}\) are two-photon relative-angle coefficients. The decay-cascade fit uses spin and companion-transition inputs and reports no in-beam Gaussian \(\sigma/I\). The original polarization observable for these rows is \(\beta\). A value of \(P\) derived from \(\beta,Q\) would need a separate provenance tag.

## Extracted Pages

- PDF pp.1–4 (print 525–528) describe the decay source, spectrometers and finite-solid-angle and polarimeter calibration.
- PDF pp.5–10 (print 529–534) contain Tables 1–3, selected spins and mixing ratios, model comparisons and references.
