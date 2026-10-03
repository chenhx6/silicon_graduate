---
type: source
title: "ENSDF 131Ce high-spin and superdeformed-band evaluation"
aliases: [ENSDF 131Ce high-spin levels, NuDat 131Ce SD-1 SD-2]
created: 2026-10-03
updated: 2026-10-03
status: active
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: deep-read
title_original: "Nuclear Data Sheets for A = 131"
authors: [Yu. Khazov, I. Mitropolsky, A. Rodionov]
journal: "Nuclear Data Sheets"
year: 2006
volume: 107
pages: "2715-2930"
doi: "10.1016/j.nds.2006.10.001"
citation_key: Khazov_2006_A131
citation_key_origin: crossref
citation_key_verified: 2026-10-03
canonical_source: "https://doi.org/10.1016/j.nds.2006.10.001"
data_url: "https://www.nndc.bnl.gov/ensnds/131/Ce/hi_xng_superdeformed_bands.pdf"
nudat_url: "https://www.nndc.bnl.gov/nudat3/getdataset.jsp?nucleus=131CE"
raw_file: "raw/papers/gpt/day5-20261003/ensdf-131ce-superdeformed-bands.pdf"
raw_sha256: c7438a39930c111dbe6baff1f96a7fa7a3a6011001f7270d0850b8873a1d51f3
data_sha256: c7438a39930c111dbe6baff1f96a7fa7a3a6011001f7270d0850b8873a1d51f3
data_bytes: 94286
related_raw_files: ["raw/papers/gpt/day5-20261003/ensdf-131ce-high-spin-bands.pdf"]
related_raw_sha256: fc07aef609a67abc8d383d14dc96753ceb8706c977f6cb462d5d5371210a2544
related_data_url: "https://www.nndc.bnl.gov/ensnds/131/Ce/hi_xng.pdf"
retrieved: 2026-10-03
nuclei: [131ce]
reactions: []
experiments: [ensdf-evaluation]
models: []
observables: [level-energy, spin-parity, band-identity, gamma-ray-energy, quadrupole-moment]
methods: [evaluated-data-compilation]
tags: [ensdf, a130, 131ce, superdeformed-bands, level-scheme]
---

# ENSDF 131Ce high-spin and superdeformed-band evaluation

## Bibliographic Record

Crossref verifies the full A=131 evaluation as Yu. Khazov, I. Mitropolsky, and A. Rodionov, Nuclear Data Sheets 107, 2715–2930 (2006), DOI 10.1016/j.nds.2006.10.001. NNDC serves the targeted evaluated subfiles through NuDat3 and the two local PDF endpoints listed in the metadata. The superdeformed-band subfile is five pages (94,286 bytes; SHA-256 c7438a39930c111dbe6baff1f96a7fa7a3a6011001f7270d0850b8873a1d51f3). The normal high-spin subfile is eleven pages (128,494 bytes; SHA-256 fc07aef609a67abc8d383d14dc96753ceb8706c977f6cb462d5d5371210a2544).

## Scope and Reading Depth

Both targeted ENSDF subfiles were read, with visual checks of the SD1/SD2 scheme on PDF p.5 and the evaluated normal-band scheme on PDF p.11. The evaluation cutoff is 17 July 2006. This is an adopted-data compilation, not an independent experiment or a replacement for its cited measurements.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ENS06-1 | The superdeformed evaluation identifies the 1998Pe01 reaction as 132-MeV 110Pd(28Si,alpha3n gamma), with Q0 for an SD-1 band measured by the GASP DSA method. | source-lineage | contextual | PDF p.1, History entry 1998Pe01 | true |
| ENS06-2 | ENSDF labels Band A as SD-1 and gives intrinsic Q0=7.3(4) eb and beta2=0.38(2), attributing these values to 1998Pe01; this is the same result recorded as PE98-7, not an independent confirmation. | evaluation-cross-reference | contextual | PDF p.2, Band(A) SD-1 note | true |
| ENS06-3 | ENSDF separately labels Band B as SD-2 and lists intrinsic Q0=8.5(4), citing 1996Se03 and 1996Cl03. | evaluation-cross-reference | contextual | PDF p.2, Band(B) SD-2 note | true |
| ENS06-4 | The evaluation reports that 2005Pa30 linked the two superdeformed bands; it lists 1513.9(4)- and 1522.6(4)-keV interband transitions with M1+E2 assignments and depicts the two SD sequences on one scheme. | evaluated-transition-record | contextual | PDF p.3, 1513.9/1522.6-keV rows; PDF p.5, SD1/SD2 level scheme | true |
| ENS06-5 | The separate normal high-spin subfile states that its adopted levels are mainly based on 1991Pa07, 1996Gi08, and 2004Li27 and records a 17-Jul-2006 literature cutoff; it predates the 2013 Alwaleedi thesis. | evaluation-scope | contextual | Normal high-spin PDF p.1, History and level-scheme scope | true |
| ENS06-6 | The two available 2006 subfiles present the normal-band families and the SD1/SD2 families separately; the SD subfile shows links between SD2 and SD1, not links to the normal-band scheme. This is a locator-level coverage boundary, not proof that no such transition exists in later or unexamined sources. | evidence-boundary | contextual | SD PDF p.5, level scheme | true |

## Summary

The evaluation closes one identity edge: Petrache et al. 1998, whose measured 131Ce Q0 is PE98-7, is the source cited for ENSDF Band A, SD-1. ENSDF also distinguishes a second superdeformed sequence, SD-2, and lists two transitions that connect SD-2 to SD-1. These evaluated links do not connect either SD sequence to the normal-deformed Bands 1–7 of Alwaleedi 2013.

## Competing Interpretations and Limitations

- ENSDF reuses the primary-source results it cites. Its SD-1 assignment is a retrospective band crosswalk, not another Q0 measurement.
- The SD-2 Q0 value is attributed to 1996Se03/1996Cl03; their acquisition dependence and covariance are not established by this locator audit.
- The 2005Pa30 run used 100Mo(36S,5n gamma) at 160 and 165 MeV with EUROBALL IV. Alwaleedi 2013 used the same target/channel at 165 MeV with Gammasphere, but the datasets are separate. The two ENSDF-listed links are SD2-to-SD1 transitions; they do not map SD1/SD2 onto Alwaleedi Bands 1–7.
- The normal subfile’s cutoff precedes the 2013 thesis. Its separation from the SD subfile cannot be used to prove that no normal-to-SD link was reported later.

## Knowledge Impact and Learning Decision

- Effect: supports and revises. It resolves the Petrache-1998-to-SD1 identity and the SD1/SD2 interband link while leaving the normal-deformed-to-superdeformed transition map open.
- Source independence: this is an ENSDF/NuDat compilation of the listed experiments, not a new experimental lineage.
- Review state: unreviewed; claims are retained as evaluated-data context, not human-reviewed.

## Extracted Pages

- Superdeformed subfile PDF pp.1–5: History/literature lineage; SD-1 and SD-2 level records; the 1513.9(4)- and 1522.6(4)-keV SD2→SD1 transition rows; and the combined SD1/SD2 level scheme.
- Normal high-spin subfile PDF pp.1–11: 2006 evaluator and cutoff, references 1991Pa07/1996Gi08/2004Li27, adopted normal-band levels and gamma records.
- NuDat3 131CE level page: current evaluated index with separate high-spin and superdeformed source keys; the page and the 2006 PDFs are evaluation views, not separate experiments.

## Related Knowledge

- [[131ce]]
- [[petrache-1998-highly-deformed-lifetimes-131ce-nd]]
- [[alwaleedi-2013-band-structures-131ce]]
- [[131ce-collective-mode-discrimination]]
- [[a130-thesis-evidence-matrix]]
