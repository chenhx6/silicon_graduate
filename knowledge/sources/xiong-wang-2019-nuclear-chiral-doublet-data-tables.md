---
type: source
title: "Xiong and Wang 2019 - Nuclear chiral doublet bands data tables"
aliases: [Xiong Wang 2019 chiral data tables, nuclear chiral doublet census]
created: 2026-08-11
updated: 2026-11-22
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Nuclear Chiral Doublet Bands Data Tables"
authors: [B. W. Xiong, Y. Y. Wang]
journal: Atomic Data and Nuclear Data Tables
year: 2019
volume: 125
pages: 193-225
doi: 10.1016/j.adt.2018.05.002
language: English
canonical_source: https://doi.org/10.1016/j.adt.2018.05.002
citation_key: xiong_2019_Nuclearchiral
raw_file: "raw/papers/2019_Xiong_Wang_Nuclear chiral doublet bands data tables.pdf"
raw_sha256: DBB2208A1090E2DC9DCB673199F4AEC19D270727591171CAE95987442641296E
archive_required: true
nuclei: []
reactions: []
experiments: []
observables: [energy-displacement, energy-staggering-parameter, moments-of-inertia, bm1-be2-ratio]
tags: [project-ingest, nuclear-chirality, multiple-chiral-doublet-bands, data-compilation, systematics]
---

# Nuclear Chiral Doublet Bands Data Tables

## Bibliographic Record

Atomic Data and Nuclear Data Tables 125, 193-225 (2019), DOI `10.1016/j.adt.2018.05.002`. The protected BibTeX key is `xiong_2019_Nuclearchiral`. The repository PDF is an article-in-press version carrying 2018 copyright/citation wording; this page uses the final volume's bibliographic year, 2019.

## Scope and Reading Depth

- 核定馆藏 33 页为 Article in Press 排版，采用 PDF 自身页码。PDF17 的表说明将星号定义为同自旋最低能态；Table 1 的若干强度比由汇编者按原实验数据重新求出，`126Cs` 等核还用已有的绝对跃迁几率求比。Table 2 的绝对值仍须追踪引用的原实验。两个表可共享输入，引用时保留数值的推导路径。

- Completed reading_depth: `deep-read`.
- Covered scope: all 33 PDF pages, including motivation, four mass-region energy and fingerprint systematics, complete table explanations, Table 1's compiled level energies and `B(M1)/B(E2)` values, Table 2's available absolute `B(M1)` and `B(E2)` values, references and summary.
- Evidence role: secondary data compilation and discovery/cross-check layer. It does not add a new experiment, independently remeasure a band, or validate the original papers' spin, parity, configuration or chirality assignments.
- Coverage caveat: the authors retain the source literature's candidate labels, numerical precision and heterogeneous transition-strength provenance. Reuse of any nucleus-specific datum or interpretation requires return to the cited original source.

## Extracted Pages

- PDF pp.1-3: abstract, motivation, definitions, 47-nucleus chart and energy spectra.
- PDF pp.4-13: mass-region systematics of energy difference, `S(I)`, rotational frequency, kinematic/dynamic moments of inertia and `B(M1)/B(E2)`.
- PDF pp.14-16: references.
- PDF p.17: explanation of Tables 1-2 and provenance conventions.
- PDF pp.18-30: Table 1, compiled spins/parities, level energies and available `B(M1)/B(E2)` values.
- PDF pp.31-33: Table 2, available absolute `B(M1)` and `B(E2)` values.

## Paper Question and Scientific Motivation

The paper asks how to make the rapidly expanding reported chiral-doublet literature reusable as a common numerical data set. It compiles band energies and transition-strength information, derives a standard set of rotational fingerprints and surveys their mass- and spin-dependent similarities and exceptions.

## Method and Design Logic

- Literature-reported pairs are grouped into the `A≈80`, `100`, `130` and `190` regions and labeled “yrast” and “side” within each proposed doublet.
- Published level energies generate energy spectra, partner displacement `ΔE`, `S(I)`, rotational frequency, and kinematic/dynamic moments of inertia.
- Published or reconstructed `B(M1)/B(E2)` ratios are plotted, but their source differs across nuclei; a smaller subset with absolute strengths is separated into Table 2.
- Similarity and smoothness are surveyed as commonly proposed fingerprints, while crossings, backbends, bandhead irregularities and transition-strength gaps are retained as exceptions.

## Summary

Xiong and Wang compile 59 reported chiral doublet bands in 47 nuclei, including eight nuclei described as reported or suggested MχD cases. This is a historical census through the paper's cutoff, not 59 independent confirmations. Its lasting value is a compact lookup table and a uniform set of derived plots. Its central limitation is equally important: the source classifications and electromagnetic inputs remain heterogeneous, and absolute lifetime-based transition probabilities are available for only a small subset.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| XW19-1 | The compilation counts 59 reported chiral doublet bands in 47 nuclei across the `A≈80`, `100`, `130` and `190` regions. | literature-census | indirect | PDF p.1, Abstract; p.6, Introduction; p.12, Summary | true |
| XW19-2 | Eight nuclei are listed as reported or suggested MχD cases: `78Br`, `103Rh`, `105Rh`, `107Ag`, `133Ce`, `136Nd`, `138Nd` and `140Eu`. | literature-census | indirect | PDF pp.1-2, Abstract/Introduction; Fig.2 | true |
| XW19-3 | Table 1 compiles spin/parity, partner energies and available `B(M1)/B(E2)`; Table 2 separately gives available absolute `B(M1)` and `B(E2)`. | source-structure | direct | PDF p.17, Explanation of Tables; pp.18-33 | true |
| XW19-4 | The plotted partners are generally close in energy, but crossings occur in `112Ru`, `105Rh`, `107Ag`, `136Nd`, `137Nd`, `140Eu` and `188Ir`, which the authors say require careful examination. | compiled-systematics | indirect | PDF p.7, Secs.2.1-2.2; Figs.3-10 | true |
| XW19-5 | `ΔE` is below `600 keV` for the compiled pairs except `100Tc`, `102Rh`, `104Ag`, `106Ag`, `107Ag` and `126I`; this is a census pattern, not a chirality threshold. | derived-observable | indirect | PDF p.9, Sec.2.2; Figs.7-10 | true |
| XW19-6 | Smooth `S(I)` is treated as a possible fingerprint, but the paper notes large changes near some bandheads and therefore does not make smoothness universal. | evidence-boundary | direct | PDF p.9, Sec.2.3; Figs.11-14 | true |
| XW19-7 | Yrast/side `I-ω` relations are usually similar but show possible backbending and named exceptions; kinematic moments are roughly constant for most cases but differ markedly in several nuclei. | compiled-systematics | indirect | PDF pp.9-10, Secs.2.4-2.5; Figs.15-22 | true |
| XW19-8 | Dynamic moments fluctuate strongly because they are second derivatives of energy; the authors still find broad pairwise similarity in most compiled cases. | derived-observable | indirect | PDF pp.10-12, Sec.2.6; Figs.23-26 | true |
| XW19-9 | Similar/staggered `B(M1)/B(E2)` curves are presented as electromagnetic fingerprints, but the paper does not convert this systematics into an assignment-independent selection rule. | evidence-boundary | direct | PDF pp.10-13, Sec.2.7; Figs.27-30 | true |
| XW19-10 | Ratio provenance is heterogeneous: many values are reconstructed with the paper's cited equation, some are calculated from available absolute strengths, and others are taken from original sources. | source-provenance | direct | PDF p.12, Sec.2.7; p.17, Explanation of Table 1 | true |
| XW19-11 | Table stars mark the actual nucleus yrast state at a given spin; “yrast” and “side” otherwise label the two members of the proposed pair and do not independently establish their physical identity. | terminology-boundary | direct | PDF p.17, Explanation of Table 1 | true |
| XW19-12 | The number of printed digits follows original articles or propagated errors, so apparent numerical precision is not a new uniform reanalysis. | source-provenance | direct | PDF p.17, Explanation of Tables 1-2 | true |
| XW19-13 | The authors explicitly state that lifetime measurements needed for absolute transition probabilities remain rare; Table 2 consequently covers only a small subset of the 47-nucleus census. | evidence-gap | direct | PDF p.6, Introduction; p.12, Summary; pp.31-33, Table 2 | true |
| XW19-14 | The low-spin structures in `106Mo` and `110Ru` are described as soft chiral vibrations, whereas high-spin chiral rotations are cited in `136Nd`; these are carried-over interpretations rather than new calculations in this paper. | literature-synthesis | indirect | PDF p.7, Sec.2.1 | true |
| XW19-15 | The paper supplies no new reaction, detector, angular-correlation, polarization, lifetime or configuration measurement and therefore cannot serve as independent confirmation of any entry in its census. | evidence-boundary | direct | Full paper; Tables 1-2 reference columns | true |

## Data-Reuse Contract

1. Use this source to discover a candidate nucleus, locate the cited original literature and cross-check transcribed values.
2. Preserve the table's star and yrast/side conventions when transcribing level rows.
3. Record whether a ratio was imported, reconstructed from branching information or calculated from absolute strengths.
4. Return to the original experiment before using spin/parity, configuration, lifetime, transition strength or chirality status as evidence.
5. Do not compare the 2019 counts directly with later censuses without matching cutoff date, inclusion rules and pair-count convention.

## Competing Interpretations and Limitations

- Energy proximity, smooth `S(I)`, similar alignments/inertias and ratio staggering are not unique to chiral geometry; configuration mixing, crossings, shape coexistence and other collective modes remain viable in individual nuclei.
- The census inherits source dependencies. Multiple papers on one nucleus or repeated use of one level scheme do not become independent evidence through compilation.
- Ratio reconstruction can embed pure-M1, mixing-ratio, branching and lifetime assumptions from the original articles.
- “MχD nucleus” compresses nonuniform cases: number of pairs, partner-resolved strengths, configuration evidence and model support differ sharply.
- Table 2's sparse absolute-strength coverage prevents a uniform electromagnetic test across the census.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The durable output is a 2019 lookup/cross-check data layer, not a new experiment or validation study. | XW19-1, XW19-3, XW19-15 | unreviewed |
| AR-2 | Census meaning | “59 bands/47 nuclei/8 MχD nuclei” records the authors' inclusion decisions at a historical cutoff and must not be treated as a timeless confirmed count. | XW19-1/2 | unreviewed |
| AR-3 | Observable comparability | Uniform plots do not imply uniform upstream observables because ratio provenance and absolute-strength coverage differ. | XW19-9/10/12/13 | unreviewed |
| AR-4 | Counterexample value | Crossings, backbends and bandhead irregularities are more useful as audit flags than as exceptions to be smoothed away. | XW19-4/6/7/8 | unreviewed |
| AR-5 | MχD use | The eight-name list should seed pair-by-pair original-source review, not create eight nucleus-level confirmations. | XW19-2, XW19-13/15 | unreviewed |
| AR-6 | Research decision | Persist one source page plus project/concept census boundaries; do not mechanically create pages for all 47 nuclei. | Full paper | unreviewed |

## Knowledge Impact and Learning Decision

- Effect: `organizes` the reported-candidate landscape and `limits` confidence inflation from reused systematics.
- Persistence: source page; update the MχD concept and nuclear-chirality project with census/provenance rules.
- No nucleus, band or experiment page is created solely from this secondary compilation.
- Review state: all `XW19-*` and AR claims remain unreviewed and outside the paper evidence gate.

## Human Review Triage

### P0

P0: none identified.

### P1

- **XW19-1/2 — census semantics.** Check pair-count and MχD inclusion conventions before quoting the headline numbers.
- **XW19-4 to XW19-9 — fingerprint boundaries.** Preserve named exceptions and do not turn descriptive ranges into criteria.
- **XW19-10/12/13 — provenance heterogeneity.** Require source-specific assumptions before numerical reuse.
- **XW19-15 — evidence independence.** Never cite the table compilation as an independent replication of the original level schemes.

## Related Knowledge and Project Relations

- [[multiple-chiral-doublet-bands]], [[chiral-doublet-bands]].
- [[energy-displacement]], [[energy-staggering-parameter]], [[moments-of-inertia]], [[bm1-be2-ratio]].
- [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Sources

- Protected BibTeX record: `xiong_2019_Nuclearchiral` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2019_Xiong_Wang_Nuclear chiral doublet bands data tables.pdf`.
