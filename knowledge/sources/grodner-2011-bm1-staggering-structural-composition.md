---
type: source
title: "Grodner 2011 - B(M1) staggering and structural composition of chiral bands"
aliases: [Grodner 2011 B(M1) staggering]
created: 2026-10-10
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Staggering of the B(M1) value as a fingerprint of specific chiral bands structure"
authors: [E. Grodner]
journal: "International Journal of Modern Physics E"
year: 2011
volume: 20
issue: 2
pages: "380-386"
doi: "10.1142/S0218301311017752"
arxiv: "1101.5907v1"
canonical_source: "https://doi.org/10.1142/S0218301311017752"
full_text_url: "https://arxiv.org/pdf/1101.5907v1"
downloaded_pdf_sha256: "716faa155028c0a6f6e34faca638c9ca76ec98ee7c69642a3d8186eb98190d67"
nuclei: [128Cs, 135Nd, 106Rh, 105Rh, 104Rh, 103Rh, 102Rh]
models: [symmetry-restoration, core-quasiparticle-coupling]
observables: [B(M1), B(E2), inband-strength, interband-strength, chiral-doublet]
methods: [R_yT-symmetry, phase-convention, transition-matrix-element-analysis]
tags: [chirality, M1-staggering, configuration-dependence, triaxiality, 128Cs]
citation_key: "Grodner_2011_BM1"
raw_file: "raw/papers/codex-day10/grodner-2011-bm1-staggering.pdf"
raw_sha256: "716faa155028c0a6f6e34faca638c9ca76ec98ee7c69642a3d8186eb98190d67"
---

# B(M1) staggering and structural composition of chiral bands

## Bibliographic Record

- E. Grodner, “Staggering of the B(M1) value as a fingerprint of specific chiral bands structure,” *Int. J. Mod. Phys. E* **20**(2), 380–386 (2011), DOI 10.1142/S0218301311017752.
- Crossref verifies the DOI, author, journal, volume, issue, and pages. The arXiv record identifies version 1 as 1101.5907, posted 2011-01-31. The full seven-page text was read from the arXiv PDF; SHA-256 716faa155028c0a6f6e34faca638c9ca76ec98ee7c69642a3d8186eb98190d67.
- The article has no experimental table or new data figure. Its main line is a symmetry/transition-matrix-element argument and a model-dependent comparison to previously published data.

## Theory Argument and Evidence Type

The paper uses the combined time-reversal/π-rotation operator R_yT to define the chiral-symmetry basis and introduces a phase convention for matrix elements. In the strong-symmetry-breaking limit it expresses the inband transition amplitude through the real part and the interband amplitude through the imaginary part of a left-handed matrix element. The author argues that B(M1) staggering is not caused by chirality alone: it depends on the odd-particle configuration and the triaxial core structure, especially the single-j πh11/2⊗νh11/2−1 case.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GRODNER11-1 | The combined R_yT operator commutes with the nuclear Hamiltonian and relates partner eigenstates. | symmetry-argument | model | Eq. (1) | true |
| GRODNER11-2 | The electromagnetic transition operator M(σλ) is taken to commute with R_yT. | symmetry-argument | model | Eq. (19) | true |
| GRODNER11-3 | In the strong chiral limit, the derived inband transition amplitude reduces to a real-part combination of left-handed matrix elements. | model-result | model | Eq. (26) | true |
| GRODNER11-4 | In the strong chiral limit, the derived interband transition amplitude reduces to an imaginary-part combination of left-handed matrix elements. | model-result | model | Eq. (27) | true |
| GRODNER11-5 | The author states that corresponding B(M1) and B(E2) probabilities in partner bands should become equal in the strong-limit construction. | model-result | model | printed p. 6 | true |
| GRODNER11-6 | B(M1) staggering depends on structural composition, including the odd-nucleon configuration and triaxial core, rather than on chiral symmetry alone. | interpretation-boundary | model | printed p. 6 | true |
| GRODNER11-7 | The paper cites weak or absent B(M1) staggering in 104Rh and 135Nd as cases where partner-band structure differs from the specific Cs configuration. | interpretation | mixed | printed p. 6 | true |
| GRODNER11-8 | The cited core-quasiparticle model predicts that the staggering weakens rapidly when the triaxial deformation moves away from γ≈30°. | model-result | model | printed p. 6 | true |
| GRODNER11-9 | The conclusion describes B(M1) staggering as an additional property arising from the structural composition of a nucleus. | author-conclusion | interpretation | printed p. 7 | true |
| GRODNER11-10 | The 128Cs experimental input is cited to Grodner et al. 2006, so this article adds no independent 128Cs transition-strength dataset. | source-lineage | direct | Reference [1] | true |
| GRODNER11-11 | The 135Nd comparison is cited to Mukhopadhyay et al. 2007, so that comparison reuses the existing DSAM dataset. | source-lineage | direct | Reference [12] | true |

## Comparison Boundary

For 128Cs, this is a theoretical interpretation of the same published transition-strength evidence already represented by the Grodner 2006 DSAM source. For 135Nd, it cites the same 2007 lifetime/strength study used in the DAY10 continuity analysis. The paper does not add a new experiment, independent lifetime, or direct geometric measurement.

The author distinguishes two claims: partner-band strength equality in the strong chiral limit, and spin-dependent B(M1) staggering that requires additional structural conditions. The first does not make staggering a universal necessary indicator; the second does not make observed staggering sufficient proof of a particular geometry. Its descriptions of 135Nd and Rh are author/model interpretations, not new reanalyses of their raw spectra or covariance.

## Scope and Reading Depth

The seven-page arXiv article and Eqs. (1)–(27) were read; its model conditions, phase convention, and references to reused 128Cs/135Nd data were checked. It contains no new experimental table.

## Summary

The paper derives how in-band and interband B(M1) staggering depends on configuration and triaxial-core structure in the model. It limits staggering as a unique experimental fingerprint of chiral geometry.

## Key Results

- GRODNER11-1/2/3/4 define the R_yT-symmetry construction and matrix-element phase relations.
- GRODNER11-5/6/7/8/9 show configuration- and deformation-dependent staggering examples.
- GRODNER11-10/11 identify the reused 128Cs and 135Nd experimental datasets.

## Competing Interpretations and Limitations

This is a theoretical interpretation, not an additional experiment. Its examples reuse GR06 and MU07 inputs; changes in configuration or core deformation can weaken or remove the staggering without uniquely diagnosing geometry.

## Extracted Pages

- [[grodner-2006-128cs-chiral-doublet-lifetimes]]
- [[mukhopadhyay-2007-135nd-chiral-vibration-static]]
- [[chirality-wobbling-competition-evidence]]
