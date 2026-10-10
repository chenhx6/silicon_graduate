---
type: source
title: "Koike et al. 2004 - Chiral bands and electromagnetic selection rules"
aliases: [Koike Starosta Hamamoto 2004 chiral selection rule]
created: 2026-10-10
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Chiral Bands, Dynamical Spontaneous Symmetry Breaking, and the Selection Rule for Electromagnetic Transitions in the Chiral Geometry"
authors: [T. Koike, K. Starosta, I. Hamamoto]
journal: "Physical Review Letters"
year: 2004
volume: 93
issue: 17
article_number: "172502"
pages: "172502-1–172502-4"
doi: "10.1103/PhysRevLett.93.172502"
canonical_source: "https://doi.org/10.1103/PhysRevLett.93.172502"
full_text_url: "https://tohoku.repo.nii.ac.jp/record/5332/files/PhysRevLett.93.172502.pdf"
repository_record: "https://tohoku.repo.nii.ac.jp/records/5332"
downloaded_pdf_sha256: "f39816a5d2f3f3ec45098fc636371ee3e8e4dc721b0ced33e7c87b453b7f155e"
nuclei: [128Cs, 130Cs, 132La, 134Pr, 136Pm]
models: [particle-rotor-model, triaxial-rotor]
observables: [B(E2), B(M1), transition-selection-rules, chiral-doublet]
methods: [discrete-symmetry, quantum-number-selection, electromagnetic-matrix-elements]
tags: [chirality, selection-rules, dynamical-symmetry-breaking, A-quantum-number, 128Cs]
citation_key: "Koike_2004"
raw_file: "raw/papers/codex-day10/koike-2004-selection-rules.pdf"
raw_sha256: "f39816a5d2f3f3ec45098fc636371ee3e8e4dc721b0ced33e7c87b453b7f155e"
---

# Chiral bands and electromagnetic selection rules in the chiral geometry

## Bibliographic Record

- T. Koike, K. Starosta, and I. Hamamoto, “Chiral Bands, Dynamical Spontaneous Symmetry Breaking, and the Selection Rule for Electromagnetic Transitions in the Chiral Geometry,” *Phys. Rev. Lett.* **93**, 172502 (2004), DOI 10.1103/PhysRevLett.93.172502.
- Crossref and the Tohoku University repository record 5332 verify title, authors, journal, volume, issue, article number, and year. The repository provides the four-page PDF; its downloaded SHA-256 is f39816a5d2f3f3ec45098fc636371ee3e8e4dc721b0ced33e7c87b453b7f155e.
- No arXiv version was found by exact-title query. The full four-page article, Eqs. (1)–(10), and Figures 1–3 were read; Figures 2–3 were visually inspected.

## Model and Selection Rules

The model is a special particle-rotor limit: a triaxial core at gamma = 90 degrees, one proton particle and one neutron hole in the same single-j shell, with the intermediate axis used for quantization. In the Lund convention the shape corresponds to gamma = -30 degrees. The numerical example restricts both valence angular momenta to h11/2 and uses A = 130, Z = 55, beta = 0.3, and a core moment-of-inertia parameter J0 = 8.55 hbar-squared/MeV.

The Hamiltonian is invariant under a rotation by 90 or 270 degrees about the intermediate axis combined with exchange of the valence proton and neutron. The associated operator A has eigenvalues +1 and -1. C denotes the symmetric/antisymmetric character under proton-neutron exchange. For the collective-core E2 operator, same-A matrix elements vanish. With the selected M1 operator and realistic effective gyromagnetic factors, same-A M1 matrix elements are about an order of magnitude weaker than opposite-A transitions.

The paper explicitly states that these rules hold for any eigenstates of this special Hamiltonian, irrespective of whether chiral geometry is actually achieved. Chiral geometry connects the two near-degenerate partner states to opposite A eigenvalues, but observing the transition rule alone does not demonstrate that the angular-momentum vectors are noncoplanar.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KOIKE04-1 | The special particle-rotor model uses a gamma = 90 degree core coupled to a proton particle and neutron hole in the same single-j shell. | model-assumption | model | PDF p. 2 | true |
| KOIKE04-2 | The A symmetry combines a pi/2 or 3pi/2 rotation about the intermediate axis with exchange of the valence proton and neutron. | symmetry-definition | model | Eq. (5) | true |
| KOIKE04-3 | In the collective-core E2 approximation, transitions between states with the same A quantum number are forbidden. | model-result | model | PDF p. 2, paragraph beginning “If only the core contributions” | true |
| KOIKE04-4 | With the chosen M1 operator and effective gyromagnetic factors, same-A transition matrix elements are about an order of magnitude smaller than opposite-A matrix elements. | model-result | model | Eq. (6) | true |
| KOIKE04-5 | The selection rule is predicted for any eigenstates of the model Hamiltonian, irrespective of whether chiral geometry is realized. | applicability-boundary | model | PDF p. 2, paragraph beginning “Summarizing the above results” | true |
| KOIKE04-6 | In the chiral construction, the two near-degenerate partner states have different A eigenvalues. | model-result | model | PDF p. 3, paragraph beginning “The formation of chirality” | true |
| KOIKE04-7 | In the ideal no-tunneling limit, corresponding in-band transition probabilities in the two partners are equal, as are corresponding interband probabilities. | model-result | model | Eq. (10) | true |
| KOIKE04-8 | The calculated model has approximate two-band degeneracy for 13 < I < 25, after the low-spin displaced region. | model-result | model | Figure 3 | true |
| KOIKE04-9 | Figure 2 distinguishes allowed E2 and stronger M1 transitions from weaker allowed M1 transitions in the chiral-band schematic. | selection-rule-summary | model | Figure 2 | true |
| KOIKE04-10 | The model predicts the three angular-momentum vectors can be noncoplanar at intermediate spin, while low- and high-spin limits are less favorable. | model-result | model | PDF p. 3 | true |
| KOIKE04-11 | The authors state that departures from their simplified assumptions can modify the selection rule. | applicability-limit | interpretation | PDF p. 4 | true |
| KOIKE04-12 | Reference [11] identifies the 2003 128Cs transition study as prior experimental context; this 2004 paper adds no measured transition-strength dataset. | source-lineage | direct | Reference [11] | true |
| KOIKE04-13 | Reference [10] is listed only as “to be published”; this article alone does not establish its later publication identity. | citation-boundary | direct | Reference [10] | true |

## Evidence Classification and Limits

All transition-strength inequalities, the A quantum number, the spin-dependent geometry, and the calculated level scheme are model results. The measured-energy references provide experimental context; this Letter has no new level table, measured lifetime, absolute B(E2)/B(M1), or event-level data.

The distinction between a selection-rule match and geometric confirmation is explicit in the source: the rule follows from the symmetry of the chosen Hamiltonian even when the geometry is not chiral. Chiral partner states in the model have opposite A values, but a measured electromagnetic pattern alone cannot directly assign A or prove noncoplanar angular momenta. The authors also warn that realistic departures from the special configuration and shape can change the rule.

## Source Lineage

The 2004 article is the theoretical predecessor to [[hamamoto-2011-selection-rule-chiral-geometry]]; the latter develops the same special-limit A-quantum-number approach, not an independent experimental test. Reference [11] points to [[koike-2003-128cs-chiral-doublet-bands]], which supplies the 128Cs level scheme, DCO, relative intensities, and selected mixing ratios. These sources play different roles and should not be counted as separate measurements of one strength pattern.

The paper cites Starosta et al. 2001 for N = 75 band context. Reference [10] is retained as an unresolved “to be published” citation; it is not silently mapped to a later paper.

- Model pages: [[particle-rotor-model]] and [[triaxial-particle-rotor-model]]. Band/source context: [[134pr-chiral-doublet-candidate-pair]] and [[koike-2003-128cs-chiral-doublet-bands]]. Cross-source synthesis: [[chirality-wobbling-competition-evidence]].

## Knowledge Impact and Learning Decision

Decision: **limits**. The paper gives a symmetry-based transition test for a clearly specified model and clarifies its failure mode: satisfying the rule is not sufficient to establish chiral geometry. This limits the evidential weight of a qualitative “selection-rule consistency” statement when A assignments, line-resolved strengths, and model validity are not independently established.

## Scope and Reading Depth

The four-page PRL, Eqs. (1)–(10), and Figs. 1–3 were reviewed against the Tohoku repository copy and Crossref metadata.

## Summary

The paper derives electromagnetic selection rules associated with the A operator in a special particle-rotor Hamiltonian and explicitly limits their interpretation as a geometry indicator.

## Key Results

- KOIKE04-1–4 define the model and conditional E2/M1 strength ordering.
- KOIKE04-5 states that the rule holds for model eigenstates whether or not chiral geometry is realized.
- KOIKE04-6–13 record the operators, numerical examples, and model boundaries.

## Competing Interpretations and Limitations

This is a theoretical model result, not an experimental measurement. Rule compatibility is not sufficient evidence for non-planar geometry; Hamamoto 2011 is a continuation of this theory lineage, not an independent experiment.

## Extracted Pages

- [[hamamoto-2011-selection-rule-chiral-geometry]]
- [[chirality-wobbling-competition-evidence]]
