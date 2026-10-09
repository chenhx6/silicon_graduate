---
type: source
title: "Zhu et al. 2003 - A Composite Chiral Pair of Rotational Bands in 135Nd"
aliases: ["Zhu 2003 135Nd Band A/B"]
created: 2026-10-09
updated: 2026-10-09
status: ai-draft
review_status: unreviewed
source_type: original-experiment-and-3D-TAC
reading_depth: deep-read
title_original: "A Composite Chiral Pair of Rotational Bands in the Odd-A Nucleus 135Nd"
authors: ["S. Zhu", "U. Garg", "B. K. Nayak", "S. S. Ghugre", "N. S. Pattabiraman", "D. B. Fossan", "T. Koike", "K. Starosta", "C. Vaman", "R. V. F. Janssens", "R. S. Chakrawarthy", "M. Whitehead", "A. O. Macchiavelli", "S. Frauendorf"]
journal: "Physical Review Letters"
year: 2003
volume: 91
pages: "132501"
doi: "10.1103/PhysRevLett.91.132501"
arxiv: "nucl-ex/0302029v2"
language: en
canonical_source: "Zhu et al., Phys. Rev. Lett. 91, 132501 (2003)"
zotero_item_key: ""
citation_key: ""
zotero_uri: ""
library_file: "raw/papers/gpt/high-spin-20261009/2003_Zhu et al_A Composite Chiral Pair of Rotational Bands in 135Nd.pdf"
raw_file: "raw/papers/gpt/high-spin-20261009/2003_Zhu et al_A Composite Chiral Pair of Rotational Bands in 135Nd.pdf"
raw_sha256: "8dd7aaa0a2e369532dd673384bcc18c60abc330408f20243939b31df15d98542"
nuclei: [135Nd]
reactions: ["110Pd(30Si,5n)135Nd"]
experiments: [Gammasphere, DCO, angular-distribution]
models: [three-dimensional-tilted-axis-cranking]
observables: [level-scheme, interband-transitions, DCO-ratio, angular-distribution, conversion-coefficient]
methods: [in-beam-gamma-spectroscopy, gamma-gamma-coincidence, DCO-ratio, angular-distribution]
tags: [135nd, a130, chiral-doublet, three-quasiparticle, level-scheme, interband-transition]
---

# A Composite Chiral Pair of Rotational Bands in 135Nd

## Bibliographic Record

- S. Zhu et al., Physical Review Letters 91, 132501 (2003), DOI 10.1103/PhysRevLett.91.132501, arXiv:nucl-ex/0302029v2.
- CrossRef metadata confirms the title, first author, journal, volume, article number and DOI. The OA copy used here is arXiv v2 dated 10 June 2003.
- Raw PDF: raw/papers/gpt/high-spin-20261009/2003_Zhu et al_A Composite Chiral Pair of Rotational Bands in 135Nd.pdf; 169,558 bytes; SHA-256 8dd7aaa0a2e369532dd673384bcc18c60abc330408f20243939b31df15d98542.
- Download route: Unpaywall identified the arXiv repository PDF as an article-level OA candidate. On 2026-10-09, a user-authorized check of the official APS and arXiv records found no linked SI file; this does not rule out separately hosted author material. The route results are listed under Supporting Information Availability.

## Supporting Information Availability

Checked 2026-10-09 after the user authorized obtaining relevant supplementary material. The official APS article page had no SI or attachment link; its supplemental resolver returned to the article page, the standard APS supplemental-PDF endpoint returned 404, and the official arXiv record exposed the article PDF and TeX source without an SI/ancillary link. No SI file was found at these official endpoints; separately hosted author material was not ruled out.

| ID | Check result | Evidence kind | source independence | source locator | needs_review |
|---|---|---|---|---|---|
| ZH03-SI-1 | APS article landing page returned HTTP 200 and contained no Supporting Information, Supplemental, or attachment link. | evidence-boundary | direct | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.91.132501 | true |
| ZH03-SI-2 | APS supplemental resolver redirected to the same article record with the `#supplemental` anchor rather than a file. | evidence-boundary | direct | https://link.aps.org/supplemental/10.1103/PhysRevLett.91.132501 | true |
| ZH03-SI-3 | The standard APS supplemental-PDF endpoint returned HTTP 404. | evidence-boundary | direct | https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.91.132501/PhysRevLett.91.132501.supplemental.pdf | true |
| ZH03-SI-4 | The official arXiv version record links the article PDF and TeX source, with no SI or ancillary-file entry. | evidence-boundary | direct | https://arxiv.org/abs/nucl-ex/0302029v2 | true |

## Scope and Reading Depth

- Completed reading_depth: deep-read.
- Covered scope: PDF pp.1–8 main article, including title/abstract, motivation, reaction and detector setup, Fig.2 partial level scheme and linking transitions, DCO/angular-distribution and conversion-intensity discussion, 3D-TAC configuration/table, spin-frequency and energy-splitting figures, and the conclusion. Fig.2 was visually checked at readable resolution.
- Not covered: raw event tapes, detector calibrations, the full gated spectra, original event-level transition-intensity extraction, or a review of all cited references. PDF pp.9–10 contain references and were not independently audited.
- Coverage caveat: the relative thickness of arrows in Fig.2 denotes transition intensity only. It is not an absolute or reduced transition probability.

## Paper Question and Scientific Motivation

The paper asks whether the near-degenerate same-parity Band A and Band B sequences in odd-A 135Nd can represent a chiral rotational pair, extending the proposed geometry beyond the familiar odd-odd configuration.

## Method and Design Logic

- High-spin states were populated with 133-MeV 30Si on 110Pd through the 5n channel. Gammasphere recorded about 1.3×10^9 fivefold-and-higher coincidence events. The paper describes cube/hypercube sorting, RADWARE background subtraction, and double-/triple-gated spectra (PDF pp.2–3).
- Spins and parities were taken from prior work for Band A and extracted for Band B using the same procedure. Multipolarity assignments used DCO ratios and angular-distribution analysis (PDF pp.3–4).
- The structural argument combines the level scheme and linking transitions with three-dimensional TAC calculations. Experimental level/transition observations and calculated intrinsic geometry are separate evidence layers.

## Key Evidence and Reasoning Chain

1. The abstract reports two close, same-parity ΔI=1 bands populated in the 110Pd(30Si,5n) reaction and linked by ΔI=1 and ΔI=2 transitions (PDF p.1).
2. Fig.2 supplies a partial level scheme for the earlier Band A and newly observed Band B. The arrows connect the bands; their thickness is proportional to relative transition intensity (PDF p.4, Fig.2 caption).
3. The linking-line analysis explicitly confirms ΔI=1 for the 648- and 670-keV lines from angular-distribution ratios. It describes 648 and 649 keV for related analyses in the same page; preserve the label discrepancy. The 896-keV link is assigned E2 using a forward-to-90-degree intensity ratio. The remaining weak links did not all receive their own angular-distribution ratios (PDF pp.4–5).
4. The source estimates conversion coefficients for 170- and 226-keV transitions by intensity balance and finds values consistent with mixed M1/E2 character. This is not a lifetime determination or an absolute B measurement (PDF p.4).
5. The three-quasiparticle configuration and the planar-to-aplanar orientation evolution are results of the 3D-TAC calculation, not directly measured angular-momentum geometry (PDF pp.5–8).

## Summary

Zhu et al. report the 135Nd Band A/B level scheme, same parity, interband links, and a 3D-TAC interpretation. The paper's transition scheme provides a line-identity crosswalk useful for reading the later 2007 lifetime/strength plots. Its arrow thickness represents relative intensity, not B(M1), B(E2), or Qt.

## Experimental Setup

- Reaction: 133-MeV 30Si + 110Pd → 135Nd + 5n (PDF p.2).
- The excitation function used three Compton-suppressed HPGe detectors; the high-fold coincidence data were collected with the Gammasphere array, with 103 active Compton-suppressed Ge detectors and about 1.3×10^9 events (PDF p.3).
- Gated spectra were sorted in RADWARE cube/hypercube formats. Background subtraction, coincidence gates, DCO ratios, and angular distributions informed the level scheme and multipolarity assignments (PDF pp.3–5).

## Key Results

| ID | Statement | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| ZH03-1 | The experiment populated 135Nd through 110Pd(30Si,5n) at 133 MeV and reports a high-fold Gammasphere data set of about 1.3×10^9 events. | experimental-fact | direct | single | PDF pp.2–3, experiment description | true |
| ZH03-2 | Band A and Band B are presented as close, same-parity ΔI=1 sequences connected by ΔI=1 and ΔI=2 transitions. | experimental-fact | direct | single | PDF p.1 abstract; PDF p.4, Fig.2 | true |
| ZH03-3 | Fig.2 maps four Band B→Band A links: Band B 31/2−→Band A 29/2−, 648 keV in the figure; Band B 33/2−→Band A 31/2−, 639 keV; Band B 35/2−→Band A 33/2−, 591 keV; Band B 37/2−→Band A 35/2−, (556) keV. The same scheme labels Band B in-band ΔI=1 lines at 226, 282, 309 and 372 keV for these initial spins. The parentheses on 556 are retained. | experimental-fact | direct | single | PDF p.4, Fig.2 level scheme | true |
| ZH03-4 | The paper reports A2/A0 values −0.654(30) and −0.564(22) for the 648- and 670-keV links as evidence of ΔI=1; later on the same page, a DCO sentence refers to 649 and 670 keV. It assigns the 896-keV link as E2 from a forward-to-90-degree intensity ratio of 1.7(3). | experimental-criterion | direct | single | PDF pp.4–5, linking-transition discussion and Fig.2 | true |
| ZH03-5 | The Fig.2 arrow thickness is proportional to transition intensity; the figure does not tabulate absolute B(M1), B(E2), or Qt. | evidence-boundary | direct | single | PDF p.4, Fig.2 caption | true |
| ZH03-6 | For the 170- and 226-keV transitions, intensity-balance estimates of electron-conversion coefficients are 0.25(10) and 0.17(3), respectively, supporting mixed M1/E2 character. No lifetime is supplied for these lines. | experimental-criterion | direct | single | PDF p.4, conversion-coefficient discussion | true |
| ZH03-7 | The 3D-TAC calculation uses a πh11/2^2νh11/2−1 configuration, deformation ε≈0.20 and γ≈30°, with neutron pairing Δ=1.08 MeV and zero proton pairing. | model-input | direct | single | PDF pp.5–6, model section and Table I | true |
| ZH03-8 | The TAC calculation predicts a finite chiral region near I≈19 with residual tunnelling and a near-planar solution at higher spin; the source calls static chirality transient over a short spin interval. | model-result + author-interpretation | mixed | single | PDF pp.7–8, Figs.4–5 and discussion | true |

## Nuclear Structure Information

Band A and Band B are same-parity ΔI=1 sequences in 135Nd, assigned in this work to the three-quasiparticle πh11/2^2νh11/2−1 configuration. Fig.2 shows several linking transitions and the associated level labels. The energy-resolved and spin-resolved scheme is the source for the cross-source mapping; the arrow width is relative intensity only.

## Authors' Interpretation

The authors interpret the same-parity doublet and three-component angular-momentum geometry as a chiral structure in an odd-A nucleus. The experiment establishes transitions and multipolarity indicators; three-axis orientation is inferred through 3D TAC.

## Model Results

The 3D-TAC calculation begins planar, becomes aplanar near the reported critical frequency, and approaches the s-i plane again at higher frequency. The paper describes the static region as transient around I≈19 and attributes a remaining band splitting near 100 keV to tunnelling. These are model results/author interpretation, not a measured geometry or a direct lifetime observable.

## Competing Interpretations and Limitations

- Relative arrow thickness in Fig.2 is not an absolute transition probability; do not convert it to B values.
- The source does not report absolute lifetimes, partner-resolved B(M1)/B(E2), or transition-by-transition covariance.
- The figure prints 648 keV, while the text later calls the DCO line 649 keV. Retain both.
- The 556-keV transition is printed in parentheses in Fig.2; keep its tentative display status.
- The transition line identities are useful for mapping the 2007 plotted same-spin points, but the 2007 figures themselves do not print the line energies. Treat the crosswalk as a cross-source identity inference, not as an additional B measurement.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | Review status |
|---|---|---|---|---|
| ZH03-AR-1 | Line identity | The four Fig.2 Band B→Band A arrows map to adjacent lower-spin Band A states at the same parity; the 37/2− 556-keV line remains parenthesized. | PDF p.4, Fig.2 | self-checking |
| ZH03-AR-2 | Multipolarity closure | 648/670 are discussed as ΔI=1; 896 is assigned E2; weak links do not each have separate angular-distribution ratios. | PDF pp.4–5 | self-checking |
| ZH03-AR-3 | Transfer to MU07 | MU07 cites this scheme and plots Band B→Band A strengths by initial spin. The line-energy assignment is cross-source and dependent on the earlier scheme; it does not add an independent strength measurement. | MU07 printed 172501-1 Ref.[8], PDF pp.2–3 Figs.2–3; Zhu PDF p.4 Fig.2 | self-checking |
| ZH03-AR-4 | Model boundary | 3D-TAC describes calculated orientation; experimental bands/links do not directly measure an aplanar geometry. | PDF pp.5–8 | self-checking |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: MU07 has DSAM-derived in-band/interband strengths, but its two plot axes do not print line energies or endpoint spins; the transition scheme is cited to Ref.[8].
- Effect of this source: limits the line-identity gap by supplying a same-spin crosswalk; supports mapping MU07's four 31/2−–37/2− interband data markers to the corresponding earlier Band B→Band A lines; preserves 556 parentheses and the 648/649 text discrepancy.
- Reason: MU07 printed p.1 says its partial scheme is taken from Ref.[8]; Zhu Fig.2 labels the levels and transition arrows. Different entrance reactions/experimental campaigns mean the level-scheme crosswalk is not a duplicate B-strength measurement.
- Persistence decision: source page + minimal MU07/nucleus/index links; no new independent experimental strength claim.
- Review state: Codex self-audited; page remains unreviewed and all new source claims retain needs_review: true.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[mukhopadhyay-2007-135nd-chiral-vibration-static]] | MU07 cites the 2003 partial level scheme as its level-identity basis; the later DSAM strength data are a separate 100Mo(40Ar,5n) campaign. |
| retrospective-connection | [[lv-2019-chirality-135nd-reexamined]] | The later D5/D6 labels are retrospective lineage for Band A/B; those labels are not back-projected into the 2003 paper. |
| foundational-background | [[nuclear-chirality]] | The paper is a historical odd-A three-quasiparticle chiral candidate interpreted with 3D TAC; geometry remains model-derived. |

## Human Review Triage

### P0

P0: none identified.

### P1

- ZH03-P1-1: The 648-keV Fig.2 label and the later 649-keV DCO wording disagree. Preserve both; do not choose one for line-energy reporting.
- ZH03-P1-2: The 556-keV interband link is parenthesized in Fig.2; retain its tentative display status when it is crosswalked to the MU07 37/2− marker.
- ZH03-P1-3: The B-to-A assignments are read from a partial level scheme and used to map MU07's initial-spin plotting convention; they identify line candidates but do not reproduce the MU07 absolute strengths.

### P2/P3

- P2: No page-level review has occurred. Other weaker links and individual multipolarity assignments remain at the source's reported confidence.

## Extracted Pages

- Nuclei: [[135nd]]
- Bands: Band A/B are preserved as the paper's historical labels; do not create new duplicate band entities.
- Concepts: [[nuclear-chirality]]
- Methods: [[high-spin-lifetime-strength-deformation]]; [[lange-kumar-hamilton-1982-multipole-admixtures]]

## Non-source Notes and Follow-up

The local public OA PDF was fetched from arXiv via Unpaywall; the manifest for this run is in tmp/day9-zhu-2003/manifest.json. The PDF is stored under raw/papers/gpt/high-spin-20261009 and remains immutable.
