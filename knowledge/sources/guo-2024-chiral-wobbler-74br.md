---
type: source
title: "Guo et al. 2024 - Evidence for Chiral Wobbler in Nuclei"
aliases: [Guo 2024 74Br chiral wobbler]
created: 2026-07-16
updated: 2026-09-20
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evidence for Chiral Wobbler in Nuclei"
authors: [R. J. Guo, S. Y. Wang, C. Liu, R. A. Bark, J. Meng, S. Q. Zhang, B. Qi, A. Rohilla, Z. H. Li, H. Hua, Q. B. Chen, H. Jia, X. Lu, S. Wang, D. P. Sun, X. C. Han, W. Z. Xu, E. H. Wang, H. F. Bai, M. Li, P. Jones, J. F. Sharpey-Schafer, M. Wiedeking, O. Shirinda, C. P. Brits, K. L. Malatji, T. Dinoko, J. Ndayishimye, S. Mthembu, S. Jongile, K. Sowazi, S. Kutlwano, T. D. Bucher, D. G. Roux, A. A. Netshiya, L. Mdletshe, S. Noncolela, W. Mtshali]
journal: Physical Review Letters
year: 2024
volume: 132
pages: 092501
doi: 10.1103/PhysRevLett.132.092501
canonical_source: https://doi.org/10.1103/PhysRevLett.132.092501
citation_key: guo_2024_EvidenceChiral
raw_file: "raw/papers/2024_Guo et al_Evidence for Chiral Wobbler in Nuclei.pdf"
raw_sha256: 1783B784C3843E15DE39406182613757F9C3B928A2791E45A7D650F117EA4333
supplementary_raw_file: "raw/papers/gpt/high-spin-20260920/三轴/进动/实验/2024_Guo et al_Evidence for Chiral Wobbler in Nuclei 1.pdf"
supplementary_raw_sha256: 1eb2c1af4ff7d1bf6460c154baabacb80e3ca7e63fa1832ca1d1b3d58b5ea9a0
alternate_version_file: "raw/papers/gpt/high-spin-20260920/三轴/进动/实验/2024_H. Amro et al_Evidence for Chiral Wobbler in Nuclei.pdf"
alternate_version_sha256: f8ca78604264fc3cf5081d8ddd20c2a8e708e3fe4526d73fa037f1f75c532fe6
nuclei: [74br]
reactions: ["58Ni(19F,2p1n)74Br"]
experiments: []
models: [particle-rotor-model]
observables: [multipole-mixing-ratio, interband-e2-strengths, bm1-be2-ratio]
methods: [angular-distribution, linear-polarization-asymmetry, doppler-correction]
tags: [experiment-ingest, chiral-wobbler, chirality, wobbling, lifetime, odd-odd, a80]
---

# Evidence for Chiral Wobbler in Nuclei

## Bibliographic Record

PRL 132, 092501 (2024), DOI `10.1103/PhysRevLett.132.092501`; PDF/BibTeX identity checked. On 2026-08-11 the local PDF identity was reverified from its title page, author list, journal/article number and DOI, and `raw_sha256` was synchronized to the current local binary; the raw PDF itself was not modified.

## Scope and Reading Depth

- Completed reading_depth: `deep-read` for the supplied main PRL and its supplied Supplemental Material.
- Covered scope: complete main PRL, level scheme, ADO/polarization, mixing-ratio logic, DSAM lifetimes, absolute transition-probability figures, PRM interpretation, and Supplement pp.1–3 including Table I, gated spectra and upper-limit rows.
- Not covered: raw event matrices, detector-response files, PRM source code and the cited independent spectroscopy sources.
- Coverage caveats: the supplement closes the local numerical-table gap, but it does not remove the parent paper's configuration, branch-choice or model-dependence boundaries.
- HS-126 alternate PDF audit: the seven-page APS PDF differs from the canonical copy only in minor typesetting/reference-line text; title, DOI, figures, tables, equations and claims agree. It is attached evidence for this PRL, not a second experiment.

## Paper Question and Scientific Motivation

- Author-explicit motivation: test whether chirality and wobbling can coexist in bands assigned the same odd-odd configuration, forming a “chiral wobbler” (PDF pp.1-2).

## Method and Design Logic

- Combine three-band spectroscopy, ADO/polarization, DSAM lifetimes and absolute strengths; compare B1/B2 chiral fingerprints and B1/B3 wobbling fingerprints with PRM angular-momentum geometry (PDF pp.2-5, Figs.1-7, Table I).

## Key Evidence and Reasoning Chain

- Similar B1/B2 energies/strengths plus M1 interlinks → chiral-partner interpretation; increasingly E2 B1-B3 links → wobbling interpretation; same-configuration assignment and PRM mapping → coexistence claim. The supplied supplement closes the transition-table gap; configuration and PRM dependence remain.

## Summary

The paper proposes `74Br` bands B1/B2 as chiral partners and B3 as a one-phonon wobbling excitation built on B1, coining an experimental “chiral wobbler” candidate. The supplied supplement now makes the transition-level table and upper limits locally auditable. The conclusion remains evidence/interpretation supported by multiple observables and PRM, not a model-independent proof of coexistence.

## Experimental or Theoretical Setup

`58Ni(19F,2p1n)74Br`; AFRODITE with eight Compton-suppressed clovers (five at 90°, three at 135°), about `3.5×10^9` γ-γ events. A thick backed target stopped recoils for DSAM lifetime extraction with modified LINESHAPE and five-step side feeding.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU24-1 | Three `ΔI=1` bands assigned the same `πg9/2⊗νg9/2` configuration were extended and interconnected. | experimental-fact | direct | PDF pp.2-3, Figs.1-2 | true |
| GU24-2 | Spin/parity and E2/M1 mixing were constrained by ADO ratios and linear polarization. | experimental-criterion | direct | PDF pp.2-3, Fig.3; Supplement Table I, pp.1-2 | true |
| GU24-3 | Level lifetimes were measured by DSAM and agree with earlier measurements within uncertainties. | experimental-fact | direct | PDF pp.2-4, Fig.4, Table I | true |
| GU24-4 | B1/B2 satisfy the authors' chiral-doublet fingerprint set, including similar energies/staggering/alignment/in-band strengths and M1-dominated interband links. | author-interpretation | indirect | PDF pp.3-4, Figs.5-6 | true |
| GU24-5 | B1-B3 E2 fractions rise with spin and reach about 90% at high spin; B3 is interpreted as one-phonon wobbling. | experimental-fact | direct | PDF p.4, Fig.6; Supplement Table I, pp.1-2 | true |
| GU24-6 | PRM angular-momentum components support chiral B1/B2 and wobbling B1/B3 pictures. | model-result | direct | PDF pp.4-5, Figs.6-7 | true |
| GU24-7 | Authors conclude evidence for coexistence of chirality and wobbling with the same configuration, notated as a chiral wobbler. | author-interpretation | indirect | PDF p.5, Summary | true |

## Nuclear Structure Information

B1/B2/B3 are interconnected ΔI=1 bands assigned πg9/2⊗νg9/2. Lifetimes and relative/absolute strengths provide unusually broad observables; the supplied supplement makes the transition table locally auditable.

## Authors' Interpretation

The authors conclude evidence for a same-configuration coexistence of chirality and wobbling, not a model-independent proof.

## Model Results

PRM angular-momentum components reproduce the proposed chiral and wobbling geometries. The mapping depends on common configuration and fitted deformation/coupling assumptions.

## Competing Interpretations and Limitations

The same-configuration inference uses linking patterns, similar strengths and PRM. Chiral/wobbling fingerprints are not individually sufficient; configuration assignment and PRM dependence remain. Future thin-target and `g`-factor measurements are explicitly proposed.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GU24-AR-1 | Core reconstruction | The three-band comparison, lifetimes and strengths are unusually rich; the supplement closes the table gap, while same-configuration coexistence still depends on configuration and PRM mapping. | Key Results and Competing Interpretations above | unreviewed |
| GU24-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| GU24-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| GU24-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| GU24-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| GU24-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: The three-band comparison, lifetimes and strengths are unusually rich; the supplement closes the table gap, while same-configuration coexistence still depends on configuration and PRM mapping.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed` within the main-paper-only scope; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[nuclear-chirality-and-multiple-chiral-doublet-bands]] | New same-configuration coexistence candidate outside existing `78Br/133Ce` cases. |
| supports | [[wobbling-motion]] | Lifetime/ADO/polarization-supported one-phonon candidate in an odd-odd nucleus. |
| limits | [[chiral-doublet-bands]] | Fingerprint conjunction still requires configuration and model review. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current main-paper evidence boundary without correction. The P0/P1 items remain future strict paper-use verification prompts; the supplied supplement is audited, while raw matrices, detector response and PRM inputs remain unavailable.

### P0

- `GU24-2`/`GU24-5`, Fig.3/Fig.6 and Supplement Table I — Evidence: the supplied supplement gives the per-transition ADO/polarization/mixing and E2-fraction rows; exact values are now locally auditable, while interpretation still depends on branch and model assumptions. Agent self-audit: table-level coverage closed, claim-level paper gate remains open. Risk: numerical rows may be detached from the stated gates or uncertainty conventions.

### P1

- `GU24-1`/`GU24-4`/`GU24-7`, Figs.5-7 — Evidence: linking/strength similarities and PRM support same configuration and dual chiral/wobbling mapping. Agent inference: coexistence depends on configuration identity and model geometry. User check: configuration evidence and PRM parameter mapping. Risk: fingerprint conjunction may be overstated as model-independent proof.
- `GU24-3`, Fig.4/Table I — Review DSAM side-feeding assumptions and lifetime uncertainties before using absolute strengths quantitatively.

### P2/P3

- P2: exact level/transition transcription after the supplement is obtained. P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of the main-paper source page and accepted its claims and attribution boundaries.

## Supplementary-material audit (2026-09-20)

- The supplied three-page supplement was read end-to-end. Table I provides transition energies/intensities, `R_ADO`, polarization `P`, mixing ratios `δ`, and `B(M1)/B(E2)`-related quantities for Bands 1–3; the spectra/gate panels and upper-limit E2 rows were checked against the surrounding text.
- This is attached evidence for the same PRL experiment, not a second experiment or independent source. It closes the transition-table coverage gap but preserves `needs_review` for claims whose interpretation requires the parent PRL's configuration assignment and PRM.

## Alternate-version audit (HS-126, 2026-09-21)

- The supplied `2024_H. Amro et al_...pdf` was compared with the canonical PRL copy. The DOI/title/author list, partial level scheme, ADO/polarization/lifetime analysis, PRM parameters and conclusion reconcile.
- Only presentation-level differences were found: text line wrapping and minor reference grammar (`parameter`/`parameters`, `Ref.`/`Refs.` and `et al.` placement). No numerical, equation, figure or interpretation change was identified.
- HS-126 remains `reused-and-audited-existing-source`; no new source or independent experiment count is added.

## Review Status

Page-level review is complete for this ingest round. `reading_depth: deep-read`; claim-level `needs_review` and Analytical Reconstruction review markers remain because the supplement is now read but this remains Codex self-audit, not human claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[74br]]
- Concepts: [[nuclear-chirality]], [[wobbling-motion]]
- Methods: [[angular-distribution]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

For paper use, recheck any quoted Table-I number against the stated gate, uncertainty and branch convention; do not clear the model-dependent coexistence interpretation solely because the supplement is available.
