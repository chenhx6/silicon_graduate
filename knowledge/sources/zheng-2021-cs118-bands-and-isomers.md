---
type: source
title: "Zheng et al. 2021 - 118Cs band structure, polarization asymmetries and isomers"
aliases: [Zheng 2021 118Cs PRC 044325]
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model
reading_depth: deep-read
title_original: "Rich band structure and multiple long-lived isomers in the odd-odd 118Cs nucleus"
authors: [K. K. Zheng, C. M. Petrache, et al.]
journal: "Physical Review C"
year: 2021
volume: 104
pages: "044325"
doi: "10.1103/PhysRevC.104.044325"
canonical_source: "Zheng et al., Phys. Rev. C 104, 044325 (2021)"
raw_file: "raw/papers/gpt/query/20261119-polarization-delta-collection/10.1103_PhysRevC.104.044325.pdf"
raw_sha256: "0299c4be119be72584791d71298c2b4da4987628c44f400fc4bcfa386d4a784b"
archive_required: true
nuclei: [118Cs]
observables: [DCO, Rac, polarization-asymmetry, E2-M1-mixing-ratio, half-life]
tags: [JUROGAM3, MARA, isomers, proton-rich, mixing-ratio]
---

# The \(^{118}\mathrm{Cs}\) bands and delayed branches

## Bibliographic Record

K. K. Zheng et al., *Phys. Rev. C* 104, 044325 (2021), DOI `10.1103/PhysRevC.104.044325`. The local PDF contains one Jyväskylä repository cover followed by 19 publisher-formatted pages. PDF p.2 corresponds to 044325-1.

## Scope and Reading Depth

Read the published main text, experimental spectra, band and PNC-CSM discussion, complete Table I layout and notes, and references. Key lifetime, gate and mixed-ray entries were verified in the original illustrations and table. The table was not transcribed row by row.

## Summary

The authors study \(^{118}\mathrm{Cs}\) populated by \(^{58}\mathrm{Ni}(^{64}\mathrm{Zn},3pn)\) at 255 MeV with JUROGAM 3 and MARA. They identify ten new bands and low-lying states. The paper explicitly identifies the \(^{119}\mathrm{Cs}\) and \(^{119}\mathrm{Ba}\) work as results of the same acquisition and points to the companion experiment description. Together with the thesis these form distinct publication records for one experiment. Print 044325-2, Secs. I–II. See [[zheng-2021-cs119-proton-excitations]] and [[zheng-2021-collectivity-shape-119cs-119ba-118cs]].

| \(E_\gamma\) in Band 3 (keV) | \(R_{\rm DCO}\), stretched dipole gate | \(R_{\rm ac}\) | \(a_2\) | \(a_4\) | \(A_p\) | \(\delta\) |
| --- | --- | --- | --- | --- | --- | --- |
| 182.9 | 1.2(2) | 0.91(5) | −0.15(9) | 0.31(17) | −0.03(2) | 0.10(35) |
| 265.5 | 1.0(2) | 0.9(1) | −0.18(2) | 0.10(2) | −0.2(1) | 0.00(20) |
| 288.3 | 1.0(2) | 0.74(8) | −0.00(30) | 0.11(57) | −0.3(2) | 0.10(20) |

All three entries are \(M1+E2\) in Table I, 044325-15 / PDF p.16. The 265.5 keV row agrees with thesis Table 7.1, printed p.137. The 115.9 keV row on 044325-16 retains \(-3.6(13)\) or \(-0.1(5)\); its \(A_p\) cell is blank.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| Z21-CS118-1 | The original tabulates two distinct angular ratios, measured polarization asymmetry \(A_p\), and mixing ratio \(\delta\). Observables for representative Band 3 M1+E2 rows agree with thesis values. | experiment-and-lineage | direct | 044325-14–18, Table I; thesis p.137 |
| Z21-CS118-2 | Summing the delayed 79 and 126 keV time spectra gives \(T_{1/2}=0.55(6)\,\mu\mathrm{s}\) for the proposed \(7^+\) band-head. Direct angular-correlation assignments are unavailable for those MARA focal-plane rays. | experiment-and-limitation | direct | 044325-4, 044325-7, Figs. 3, 7, 9 |
| Z21-CS118-3 | The authors use alignment and moments of inertia with PNC-CSM to propose band configurations. Competing effects remain for observed small signature splittings that the calculation does not include. | interpretation-and-model-boundary | direct | 044325-8–13, Sec. III, Figs. 10–18 |

## Competing Interpretations and Limitations

- \(A_p\) is the corrected yield asymmetry in the adopted two-matrix procedure. The table does not give a calibrated per-line \(P\). A row with both \(A_p\) and \(\delta\) does not identify which columns entered the \(\delta\) fit. The paper does not specify a Gaussian \(\sigma/I\) or give a line-by-line \(\delta\) extraction recipe.
- The \(8^+\) band-head is assigned short isomeric character by the observed topological and timing evidence. The \(7^+\) half-life is the separate Fig. 9 result. Multiple multipolarities can account for the 126 keV decay, so its transition character remains conditional.

## Extracted Pages

- Publisher pp.1–7, acquisition lineage, level schemes, coincidences and lifetime.
- Publisher pp.8–13, configuration assignments, model comparisons and summary.
- Publisher pp.14–19, Table I and references.
