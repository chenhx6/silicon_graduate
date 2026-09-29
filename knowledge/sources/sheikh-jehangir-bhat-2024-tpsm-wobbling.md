---
type: source
title: "Sheikh, Jehangir & Bhat 2024 - TPSM study of wobbling bands"
aliases: [Sheikh et al. 2024 TPSM wobbling study]
created: 2026-09-29
updated: 2026-09-29
status: ai-draft
review_status: unreviewed
source_type: theoretical-model-comparison
reading_depth: read
title_original: "Microscopic investigation of wobbling motion in atomic nuclei using the triaxial projected shell model approach"
authors: [J. A. Sheikh, S. Jehangir, G. H. Bhat]
journal: "Chirality and Wobbling in Atomic Nuclei, Taylor & Francis book chapter 12"
year: 2024
volume: ""
pages: ""
doi: 10.1201/9781032691633-12
arxiv: 2405.08368v1
language: en
canonical_source: "https://doi.org/10.1201/9781032691633-12"
zotero_item_key: ""
citation_key: ""
zotero_uri: ""
library_file: ""
raw_file: "raw/papers/gpt/day3-mean-field-20260929/2405-08368-wobbling-133La-135Pr/PDFs/Microscopic_investigation_of_wobbling_motion_in_atomic_nuclei_using_the_triaxial_projected_shell_model_approach.pdf"
raw_sha256: a7fa3cc75113a1ff2881cbc7edd9d3285a228b429c34b6f0b9b22da4c2b90d22
nuclei: [133La, 135Pr]
reactions: []
experiments: []
models: [triaxial-projected-shell-model, triaxial-nilsson-bcs, angular-momentum-projection]
observables: [wobbling-energy, rotational-frequency, aligned-angular-momentum, B(E2)-out-in-ratio, B(M1)-out-B(E2)-in-ratio]
methods: [triaxial-nilsson-bcs, three-dimensional-angular-momentum-projection, configuration-mixing]
tags: [tpsm, wobbling, a130, 133la, 135pr, model-comparison]
---

# 三轴投影壳模型对 `133La` 与 `135Pr` 摇摆带的计算

## Bibliographic Record

J. A. Sheikh, S. Jehangir & G. H. Bhat, “Microscopic investigation of wobbling motion in atomic nuclei using the triaxial projected shell model approach,” arXiv:2405.08368v1 (2024-05-14), subsequently published as chapter 12 of *Chirality and Wobbling in Atomic Nuclei*, Taylor & Francis, DOI [`10.1201/9781032691633-12`](https://doi.org/10.1201/9781032691633-12). The publisher landing page was reachable for metadata; the arXiv v1 PDF was obtained from [`https://arxiv.org/pdf/2405.08368`](https://arxiv.org/pdf/2405.08368). Its SHA-256 is recorded above. No matching Zotero/BibTeX citation key was verified, so the field remains blank.

## Scope and Reading Depth

- Completed `reading_depth`: `read`.
- Covered scope: paper question and introduction; TPSM method and Eqs. (8), (10)–(14); Table 1; the normal-deformed results for `133La` and `135Pr`; Figs. 11–14 and their discussion; summary and references [11]–[15]. The displayed energy, wobbling-frequency, alignment and transition-ratio comparisons were visually inspected.
- Not covered: independent reanalysis of the cited experiments, refitting TPSM parameters, all results for the strongly deformed Lu/Ta isotopes, or the full text of the later 2026 IJMPE article discovered during this run.
- Coverage caveats: `ε`, `ε′` and `γ` are model inputs in Table 1. The later article's comparison with existing data is not a new measurement or an independent determination of shape.

## Paper Question and Scientific Motivation

The authors ask whether TPSM can give a common microscopic account of observed odd-mass wobbling-band spectra, their spin-dependent wobbling frequencies, alignments and electromagnetic-transition ratios. The paper treats wobbling as a mode requiring triaxial degrees of freedom and compares the model to previously published data (PDF pp. 1–3, 20–21).

## Method and Design Logic

1. Build triaxial Nilsson intrinsic states with `ε` and `ε′`, then include pairing by BCS (PDF §4, pp. 6–7).
2. Restore rotational symmetry with the three-dimensional angular-momentum projector `P̂^I_MK` (Eq. (8), PDF p. 7).
3. Form projected multi-quasiparticle configurations (Eqs. (10)–(11)) and diagonalize a Hamiltonian with quadrupole–quadrupole, monopole-pairing and quadrupole-pairing terms (Eq. (12), PDF pp. 7–8).
4. Compare calculated bands with available experimental energies, wobbling frequencies, aligned angular momenta, and `B(E2)_out/B(E2)_in` and `B(M1)_out/B(E2)_in` ratios (Figs. 11–14, PDF pp. 17–20).

## Key Evidence and Reasoning Chain

- The model begins with an explicitly triaxial intrinsic basis, projects angular momentum, and mixes selected multi-quasiparticle states; the outputs are model spectra and transition probabilities, not measured deformation parameters (Eqs. (8), (10)–(12)).
- Table 1 uses `ε=0.150`, `ε′=0.110`, `γ=36°` for `133La`, and `ε=0.160`, `ε′=0.100`, `γ=32°` for `135Pr` (PDF p. 10, Table 1).
- Figs. 11–13 compare TPSM and previously reported band energies, wobbling frequencies and aligned angular momenta for the two nuclei. Fig. 14 compares experimental and calculated transition-strength ratios (PDF pp. 17–20).
- The authors classify the frequency trend as longitudinal wobbling for `133La` and transverse wobbling for `135Pr` (PDF p. 18, Sec. 5 and Fig. 11). This is a model-mediated mode interpretation, not a direct shape measurement.

## Summary

This is a later direct TPSM calculation for two exact nuclei marked as “presumably triaxial” in Hara–Sun Table 5: `133La` and `135Pr` (both `N=76`). It closes part of the historical calculation-coverage question: a three-dimensional projected-shell-model study later treats bands in these nuclei. It does not test all seven Table 5 starred nuclei or independently establish their shapes. The 2024 study fixes triaxial deformation inputs and compares calculated observables to existing experiments; successful agreement therefore supports model applicability for the selected bands, while the shape interpretation remains conditional on those inputs and the chosen basis.

## Experimental or Theoretical Setup

- This is a theory/model-comparison chapter; it reports no new reaction, detector run or event-level analysis.
- For `133La`, Table 1 lists `ε=0.150`, `ε′=0.110`, `γ=36°`; for `135Pr`, `ε=0.160`, `ε′=0.100`, `γ=32°`.
- The authors state that Fig. 11 data are taken from Refs. [11]–[15]. Ref. [11] is Biswas et al. 2019 on `133La`; Refs. [12] and [13] are Matta et al. 2015 and Sensharma et al. 2019 on `135Pr`. These experimental sources remain the evidence for measured quantities; this chapter reuses them.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SHJ24-1 | TPSM restores angular momentum from triaxial intrinsic states with a three-dimensional projection operator. | model-method | direct | Eq. (8), PDF p. 7 | true |
| SHJ24-2 | The adopted TPSM Hamiltonian includes quadrupole–quadrupole, monopole-pairing and quadrupole-pairing interactions. | model-method | direct | Eq. (12), PDF p. 8 | true |
| SHJ24-3 | Table 1 inputs are `ε=0.150, ε′=0.110, γ=36°` for `133La` and `ε=0.160, ε′=0.100, γ=32°` for `135Pr`. These are model parameters, not experimental shape measurements. | model-input | direct | Table 1, PDF p. 10 | true |
| SHJ24-4 | Figs. 11–13 compare TPSM band energies, wobbling frequencies and aligned angular momenta with values derived from previously measured level schemes. | model-result/data-comparison | direct | Figs. 11–13, PDF pp. 17–19 | true |
| SHJ24-5 | The chapter classifies `135Pr` as transverse and `133La` as longitudinal from the calculated and compared wobbling-frequency trends. | author-interpretation | direct | Sec. 5, Fig. 11, PDF pp. 17–18 | true |
| SHJ24-6 | Fig. 14 compares experimental and TPSM `B(E2)_out/B(E2)_in` and `B(M1)_out/B(E2)_in` ratios for `133La` and `135Pr`; these comparisons do not supply new absolute lifetime measurements. | model-result/data-comparison | direct | Fig. 14, PDF p. 20 | true |
| SHJ24-7 | The paper's experimental curves reuse earlier sources cited in Refs. [11]–[15], including Biswas 2019 for `133La` and Matta 2015/Sensharma 2019 for `135Pr`; the theory chapter is not an independent experimental confirmation. | source-independence | direct | Fig. 11 caption and Refs. [11]–[15], PDF pp. 17, 22–23 | true |
| SHJ24-8 | The authors state that two-phonon wobbling assignments remain tentative pending definitive electromagnetic transition measurements. | author-limitation | direct | Abstract, PDF p. 1 | true |

## Nuclear Structure Information

The `133La` and `135Pr` cases are odd-mass normal-deformed wobbling-band comparisons. No new level scheme or experimental band assignment is introduced by this chapter. For source-level experimental details, use [[biswas-2019-longitudinal-wobbling-133la]], [[matta-2015-transverse-wobbling-135pr]] and [[sensharma-2019-two-phonon-wobbling-135pr]].

## Authors' Interpretation

The authors interpret the spin dependence of `E_wob` as longitudinal for `133La` and transverse for `135Pr`, and argue that TPSM reasonably reproduces the selected observed properties (PDF pp. 17–21, Figs. 11–14). These mode labels depend on the band assignments, triaxial parameters and model-space choices.

## Model Results

The calculated spectra and transition ratios are compared with data for ten normal-deformed wobbling cases. For the two target nuclei, the input values in Table 1 are fixed; the paper does not report a joint parameter-covariance or deformation-sensitivity analysis for the `133La`/`135Pr` comparison. Fig. 14 provides ratios, not a new absolute-strength measurement.

## Competing Interpretations and Limitations

- The model assumes triaxial shapes through its input basis; output agreement cannot independently confirm that shape assumption.
- The chapter reuses the experiments in Refs. [11]–[15]. Do not count it as a second experiment for `133La` or `135Pr`.
- For `135Pr`, the low-spin wobbling assignment remains contested. The independent JUROGAM II analysis in [[lv-2022-evidence-against-wobbling-135pr]] reports smaller-`|δ|`, predominantly magnetic solutions for key links (L22-4/L22-5), while [[nomura-2022-questioning-wobbling-ibfm]] supplies a γ-soft theoretical alternative. TPSM agreement does not settle that dispute.
- Absolute, partner-resolved lifetimes and electromagnetic strengths remain useful companions to energy trends and relative ratios.
- A 2026 IJMPE paper on odd-mass TPSM wobbling was identified by DOI during this run, but the available checks found no lawful OA full text. No scientific claim from its abstract has been imported; see the daily report for the access boundary.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SHJ24-AR-1 | Historical transfer | Of Hara–Sun Table 5's seven starred nuclei across `N=76–78`, this chapter directly calculates two `N=76` cases (`133La`, `135Pr`). Its fixed `γ` inputs and reuse of earlier experimental curves make it a later model application, not a controlled confirmation of all historical shape labels. | HARA95 HS10-4; SHJ24-3, SHJ24-4, SHJ24-7 | unreviewed |
| SHJ24-AR-2 | Failure/alternative check | `135Pr` mode assignment is disputed by an independent angular-correlation/polarization study and a separate γ-soft model; agreement to selected spectra is therefore not a unique interpretation. | L22-4/L22-5; NOM22-2–NOM22-12 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Hara–Sun's `N=76–78` Table 5 entries are historical axial-PSM inferences, not measured shapes; it was not yet clear from the model-choice card whether exact starred nuclei had later TPSM calculations.
- Effect of this source: **revises** the later-calculation coverage map and **limits** the strength of any shape-validation claim.
- Reason: the paper calculates two exact `N=76` Table 5 cases, but uses chosen triaxial inputs, reuses previous experimental data, and does not cover the remaining five starred cases.
- Persistence decision: update the TPSM model page and A≈130 model-choice card; link the existing `131Ce` project without changing its mode ranking.
- Review state: source page remains `unreviewed`; every claim retains `needs_review: true`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[triaxial-projected-shell-model]] | Concrete TPSM inputs and model-to-observable comparison for two exact Hara Table 5 nuclei. |
| retrospective-connection | [[hara-sun-1995-projected-shell-model-high-spin]] | Later TPSM calculation overlaps two of the 1995 table's starred `N=76` candidates; it does not retrospectively validate the full table. |
| competing-interpretation | [[135pr-wobbling-controversy]] | TPSM's `135Pr` interpretation joins an unresolved experimental/theoretical dispute. |
| not-direct-evidence | [[131ce-collective-mode-discrimination]] | `133La` and `135Pr` calculations do not provide `131Ce` (`N=73`) observations. |

## Human Review Triage

### P0

P0: none identified.

### P1

- `SHJ24-3`, Table 1: preserve `ε`, `ε′` and `γ` as input parameters; do not quote them as measured deformation or as independent confirmation of Hara–Sun's shape candidates.
- `SHJ24-4`–`SHJ24-7`, Figs. 11–14 and Refs. [11]–[15]: keep model outputs, earlier measurements and shared-data lineage separate; the `135Pr` wobbling claim has counter-evidence.

### P2/P3

- Citation key was not matched to the protected Zotero BibTeX input and remains blank.
- Full text of the 2026 follow-up lead was not available through the checked OA routes.

## Extracted Pages

- Nuclei: [[133la]], [[135pr]]
- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[longitudinal-wobbling]]
- Models: [[triaxial-projected-shell-model]]
- Projects: [[135pr-wobbling-controversy]], [[a130-model-choice-card]]

## Non-source Notes and Follow-up

Search next for direct calculations of Hara Table 5's remaining starred nuclei (`134La`, `135Ce`, `136Pr`, `137Pr`, `137Nd`) and for lawful full text of the DOI-only 2026 TPSM follow-up. Do not repeat the 2026 publisher or exact-title arXiv requests already recorded in the Day 3 report.
