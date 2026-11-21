---
type: source
title: "Zheng et al. 2021 - Complete set of proton excitations in 119Cs"
aliases: [Zheng 2021 119Cs PRC 044305]
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model
reading_depth: deep-read
title_original: "Complete set of proton excitations in 119Cs"
authors: [K. K. Zheng, C. M. Petrache, et al.]
journal: "Physical Review C"
year: 2021
volume: 104
pages: "044305"
doi: "10.1103/PhysRevC.104.044305"
canonical_source: "Zheng et al., Phys. Rev. C 104, 044305 (2021)"
raw_file: "raw/papers/gpt/query/20261119-polarization-delta-collection/10.1103_PhysRevC.104.044305.pdf"
raw_sha256: "cf158de9b2cef6471046aadac36c6f1791072caed59c45db814d1952bd61d2fa"
archive_required: true
nuclei: [119Cs]
observables: [DCO, Rac, polarization-asymmetry, angular-distribution, mixing-ratio]
tags: [JUROGAM3, MARA, recoil-tagging, rotational-bands]
---

# \(^{119}\mathrm{Cs}\) spectroscopy and the JUROGAM 3 angle and polarization matrices

## Bibliographic Record

K. K. Zheng et al., *Phys. Rev. C* 104, 044305 (2021), DOI `10.1103/PhysRevC.104.044305`. The local PDF has one institutional cover followed by 20 publisher-formatted pages. PDF p.2 corresponds to 044305-1.

## Scope and Reading Depth

Read the published main text, level schemes, alignment and PNC-CSM comparisons, Table II layout and footnotes, and references. Checked source-specific geometry and representative transition rows against the thesis. The table was not transcribed row by row.

## Summary

The \(^{58}\mathrm{Ni}(^{64}\mathrm{Zn},3p)\) experiment at 255 MeV uses mass-tagged and X-ray evidence for nuclide identity before construction of the level scheme with higher-statistics ungated prompt γ coincidences. The article combines new bands with results previously published or referenced in Refs. 14–15 from the same high-statistics experiment. The shared acquisition is also explicit in the \(^{118}\mathrm{Cs}\) companion. See [[zheng-2021-cs118-bands-and-isomers]] and [[zheng-2021-collectivity-shape-119cs-119ba-118cs]].

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| Z21-CS119-1 | \(R_{\rm DCO}\) swaps target and gate angles at \(157.6^\circ\) and the combined \(75.5^\circ+104.5^\circ\) group. \(R_{\rm ac}\) uses the same all-angle energy gates with backward \(133.6^\circ+157.6^\circ\) and near-transverse intensity groups normalized by their efficiencies. | experiment-method | direct | 044305-2–3, Sec. II A |
| Z21-CS119-2 | The two clover-scattering matrices use an all-detector gate. Eq. (1) gives the normalized count asymmetry \(A_P\), and the article uses polarimetry to help establish the parities of selected linking transitions. | experiment-method | direct | 044305-3, Eq. (1), Table II |
| Z21-CS119-3 | The level placement identifies the long-lived \(3/2^+\) state as ground and puts the β-decaying \(9/2^+\) level at an estimated 85.7 keV, with a cumulative uncertainty of about 2 keV. The delayed 87.1 keV transition connects a different state sequence. | level-placement | direct | 044305-3–4, Fig. 4 |

## Competing Interpretations and Limitations

- The same-parity \(5/2^+\to3/2^+\) 208.7 keV line gives \(R_{\rm ac}=0.80(9)\), \(a_2=-0.29(4)\), \(a_4=0.24(7)\), \(A_P=-0.001(1)\), and \(\delta=0.10(20)\). These values agree with thesis Table 5.2 for the same transition and experiment. The original DCO cell is blank. Printed 044305-16 / PDF p.17 and thesis printed p.97.
- For example, the 1095.6 keV Table II line gives \(R_{\rm DCO}=0.6(1)\) with a stretched quadrupole gate, \(a_2=-0.17(35)\), \(a_4=0.19(67)\), \(A_P=0.1(1)\), and \(\delta=0.05(25)\). The transition is \(17/2^+\to15/2^-\), labeled \((E1)\) in the original. It therefore belongs outside a same-parity E2/M1 data subset. Printed 044305-16 / PDF p.17.
- Article Table II lists \(A_P\) rather than a per-line \(P\). It lacks an explicit account of the width and fit inputs for each \(\delta\) entry. The matrix and asymmetry definitions establish how the observables were measured.
- The new band assignments rely on level connections and spectra plus model comparisons. Bands 8–9 and their proton-based revolving chirality interpretation are revisited from earlier work. The source treats their near-degeneracy and calculated tilt as different evidence from the newly observed bands and recognizes limits of the axially symmetric principal-axis model for dipole-band interpretation. Printed 044305-8, 044305-12, Secs. III–IV.

## Extracted Pages

- Publisher pp.1–8, apparatus, ratios, asymmetry, level schemes, connections and earlier-band lineage.
- Publisher pp.9–12, PNC-CSM calculations and band-specific interpretation.
- Publisher pp.13–20, full Table II layout, gating notes and references.
