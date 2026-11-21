---
type: source
title: "Aoki et al. 1982 - Ge(Li) polarimetry and angular distributions in 177Ta"
aliases: [Aoki 1982 GeLi Compton polarimeter, 177Ta 311 keV mixing ratio]
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-formalism
reading_depth: deep-read
title_original: "A familiar arrangement for a Ge(Li) Compton linear polarimeter"
authors: [T. Aoki, K. Furuno, Y. Tagishi, T. Ishihara, Y. Nagashima, S. Ohya]
journal: "Nuclear Instruments and Methods"
year: 1982
volume: 196
pages: "421-429"
doi: "10.1016/0029-554X(82)90107-0"
canonical_source: "Aoki et al., Nucl. Instrum. Methods 196, 421–429 (1982)"
raw_file: "raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_0029-554X_82_90107-0.pdf"
raw_sha256: "6cadca1e47c207b5d2a74815bb179f61d4dce499f1b771f6b10009519aeff6c0"
archive_required: true
nuclei: [177Ta, 109Cd, 110Cd]
observables: [linear-polarization-modulation, angular-distribution, internal-conversion, E2-M1-mixing-ratio]
tags: [in-beam-spectroscopy, compton-polarimeter, angular-distribution, mixing-ratio]
---

# Measured angular coefficients and linear polarization in \(^{177}\mathrm{Ta}\)

## Bibliographic Record

T. Aoki et al., *Nuclear Instruments and Methods* 196, 421–429 (1982). DOI `10.1016/0029-554X(82)90107-0`.

## Scope and Reading Depth

Read all nine publisher pages, including Figs. 1–9, the detector and calibration sections, the experimental applications, the appendix and references. PDF p.1 corresponds to printed p.421.

## Summary

The authors use two coaxial Ge(Li) crystals with adjacent front faces as a symmetrical Compton polarimeter. Their calibration gives \(qQ_0=(0.59\pm0.06)Q_0\), where \(Q_0\) is the energy-dependent point sensitivity at a \(90^\circ\) Compton scattering angle. The \(^{175}\mathrm{Lu}(\alpha,2n\gamma)^{177}\mathrm{Ta}\) result in Fig. 6 uses 29.5 MeV alphas (Fig. 4). The 311 and 550 keV transitions both leave the \(5\,\mu\mathrm{s}\) isomer; the 352 keV comparison line comes from another level. The polarization observable fitted in the paper is \(B\), the signed \(\cos 2\phi\) modulation in the count distribution, with the photon at \(90^\circ\) to the beam.

| \(E_\gamma\) (keV) | \(\rho_2 A_2\) | \(\rho_4 A_4\) | \(B\) | Reported outcome |
| --- | --- | --- | --- | --- |
| 311 | \(+0.048\pm0.007\) | \(-0.006\pm0.011\) | \(+0.063\pm0.031\) | M1+E2, \(\delta=+0.29^{+0.11}_{-0.06}\) after comparison with conversion |
| 550 | \(+0.190\pm0.041\) | \(-0.071\pm0.059\) | \(-0.092\pm0.066\) | Almost pure E2. A small M3 amplitude stays unresolved. |
| 352 | \(+0.303\pm0.012\) | \(-0.068\pm0.020\) | \(-0.229\pm0.046\) | Comparison line in Fig. 6. |

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| AOK82-1 | Polarization counts and angular distributions supply the fitted modulation \(B\) and the observed products \(\rho_2A_2,\rho_4A_4\). | experimental-observation | direct | p.425 Fig. 6, p.428 Eq. (14), p.429 Eq. (15) |
| AOK82-2 | The dipole/quadrupole procedure takes those measured products and calibrated \(qQ_0\) to obtain \(H_2(12)\). It has no assumed Gaussian \(\sigma/I\) parameter. | analysis-method | direct | pp.428–429, Eqs. (5)–(6), (12), (14)–(16) |
| AOK82-3 | The 311 keV M1+E2 branch is selected using the conversion coefficient. The smaller polarization-plus-angular root is retained after comparison. | analysis-result | direct | p.424 text, p.426 Fig. 8 |

## Competing Interpretations and Limitations

- With \(a_k=\rho_kA_k\) and \(s=+1\) for M1+E2 or \(-1\) for E1+M2, Eq. (16) is \(H_2(12)=-[sB(2-a_2+0.75a_4)/(qQ_0)+1.25a_4]/(3a_2)\). The measured \(a_k\) carry the alignment information. Since the expression divides by \(a_2\), a small or poorly measured \(a_2\) weakens the inference. The paper requires matching target and beam conditions for separately acquired spectra so that they share the same state tensors. The observed \(a_k\) are full angular-distribution fit coefficients, which carry more information than a single angular intensity ratio.
- In Fig. 8 the M1+E2 hypothesis gives \(H_2(12)=-1.70\pm0.92\), and the angular-plus-polarization candidates are \(+0.29^{+0.36}_{-0.06}\) and \(+10.2^{+2.6}_{-5.6}\). The conversion constraint \(|\delta|\le0.40\) under that hypothesis selects and limits the small solution. The opposite-parity E1+M2 hypothesis gives \(H_2(12)=+1.81\pm0.92\); its angular-plus-polarization solutions are incompatible with the corresponding conversion interval \(0.55\le|\delta|\le0.70\).
- The 550 keV line provides a measured relation in \((H_2,H_4)\) checked against the conversion-derived range in Fig. 9. The result concerns M3/E2, a different admixture from the requested E2/M1 dataset. Neither the plotted modulation \(B\) nor the coefficient \(H_2\) is a tabulated, detector-independent \(P\).

## Extracted Pages

- PDF pp.1–4 (print 421–424) describe detector geometry, threshold/efficiency tradeoffs and the \(^{177}\mathrm{Ta}\) measurement.
- PDF pp.5–7 (print 425–427) show the angular and polarization measurements, response calibration, competing solutions and conversion constraints.
- PDF pp.8–9 (print 428–429) define \(H_k\), the measured count distribution and the angular-coefficient-based extraction and calibration equations.
