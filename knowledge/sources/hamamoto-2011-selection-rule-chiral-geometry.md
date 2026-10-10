---
type: source
title: "Hamamoto 2011 - Selection rule for electromagnetic transitions in chiral geometry"
aliases: [Hamamoto 2011 chiral transition selection rule]
created: 2026-10-10
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Selection Rule for Electromagnetic Transitions in Nuclear Chiral Geometry"
authors: [Ikuko Hamamoto]
journal: "International Journal of Modern Physics E"
year: 2011
volume: 20
issue: 2
pages: "373-379"
doi: "10.1142/S0218301311017740"
arxiv: "1102.0163v1"
canonical_source: "https://doi.org/10.1142/S0218301311017740"
full_text_url: "https://arxiv.org/pdf/1102.0163v1"
downloaded_pdf_sha256: "dafe5f8f25081661413c5c8e2dc0b1d44a48c12ec4f5169bd1b06b0facd1c205"
nuclei: [128Cs, 126Cs, 134Pr, 132La]
models: [particle-rotor-model, triaxial-rotor]
observables: [B(E2), B(M1), transition-selection-rules, chiral-doublet]
methods: [discrete-symmetry, electromagnetic-transition-matrix-elements]
tags: [chirality, selection-rules, B(E2), B(M1), model-limit, 128Cs]
citation_key: "Hamamoto_2011"
raw_file: "raw/papers/codex-day10/hamamoto-2011-selection-rule.pdf"
raw_sha256: "dafe5f8f25081661413c5c8e2dc0b1d44a48c12ec4f5169bd1b06b0facd1c205"
---

# Selection rule for electromagnetic transitions in nuclear chiral geometry

## Bibliographic Record

- Ikuko Hamamoto, “Selection Rule for Electromagnetic Transitions in Nuclear Chiral Geometry,” *International Journal of Modern Physics E* **20**(2), 373–379 (2011), DOI 10.1142/S0218301311017740.
- Crossref verifies the title, author, journal, volume, issue, pages, and February 2011 publication record. The arXiv record identifies version 1 as 1102.0163, posted 2011-02-01.
- Locators below use the arXiv manuscript pagination, distinct from the Crossref journal pages 373–379. The arXiv PDF was downloaded to the run-local temporary directory and SHA-256 checked as dafe5f8f25081661413c5c8e2dc0b1d44a48c12ec4f5169bd1b06b0facd1c205. The temporary copy is not a durable raw artifact; the public arXiv URL and hash are retained for reproducibility.

## Scope and Reading Depth

The full article was read from the introduction through the particle-rotor construction, symmetry and transition-matrix-element derivation, numerical level scheme, experimental comparison, limitations, Table I, and Figures 1–3. The central result is a selection rule for one special odd-odd configuration. This is a model-derived rule and a comparison to previously reported transition data, not a new experiment.

## Model and Selection-Rule Derivation

The limiting model couples a triaxial core at gamma = 90 degrees to a proton particle and neutron hole in the same single-j shell. In the Lund convention the gamma value corresponds to -30 degrees, with the intermediate axis as quantization axis. The numerical example takes both valence angular momenta from h11/2 and uses a specified core moment of inertia and deformation.

The Hamiltonian is invariant under an operation A formed by a pi/2 or 3pi/2 rotation about the intermediate axis together with exchange of the valence proton and neutron. Its eigenstates therefore carry A = +1 or -1 even when chiral geometry is absent. Table I gives the allowed combinations of the rotor projection R3 and the proton-neutron exchange quantum number C for each A eigenvalue.

For collective-core E2 transitions, the model requires delta-C = 0 and delta-R3 nonzero; the gamma = 90 degree core makes delta-R3 = 0 E2 matrix elements vanish. The resulting selection rule is delta-A nonzero for a nonzero B(E2). For M1, the chosen particle-rotor operator and gyromagnetic factors make the matrix element approximately antisymmetric under proton-neutron exchange. In this construction, B(M1) for delta-A nonzero is predicted to be much stronger than for delta-A = 0.

When a chiral pair is formed, the left- and right-handed configurations combine into states with opposite A quantum numbers. In Figure 2(a), this gives allowed E2 transitions with delta-I = 1 and 2 and stronger M1 transitions with delta-I = 1; weaker delta-I = 1 M1 transitions are also allowed in the schematic. Figure 2(b) shows a particle-rotor calculation with approximate degeneracy of the two lowest bands over 13 < I < 24. Figure 3 illustrates why the authors expect chiral geometry only at moderate spin in this example: the angular-momentum vectors are coplanar at low spin and align toward the intermediate axis at high spin.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HM11-1 | The special model uses gamma = 90 degrees, equivalent to gamma = -30 degrees in the Lund convention when the intermediate axis is the quantization axis. | model-assumption | model | arXiv PDF p. 3, footnote 2 | true |
| HM11-2 | The particle-rotor model includes a core rotational Hamiltonian with the stated triaxial moment-of-inertia dependence. | model-definition | model | Eq. (2) | true |
| HM11-3 | The proton-particle potential in the same-j-shell limit is proportional to the difference of its squared angular-momentum components along axes 1 and 2. | model-definition | model | Eq. (3) | true |
| HM11-4 | The neutron-hole potential has the opposite axis ordering to the proton-particle potential in this limit. | model-definition | model | Eq. (4) | true |
| HM11-5 | The Hamiltonian is invariant under a combined intermediate-axis rotation and proton-neutron exchange, defining A = +/-1 eigenvalues independently of whether chirality is realized. | symmetry-argument | model | arXiv PDF p. 4, paragraph beginning “The total particle-rotor Hamiltonian” | true |
| HM11-6 | Table I lists the allowed R3 and C combinations for each A eigenvalue. | model-structure | model | Table I | true |
| HM11-7 | With only the collective-core E2 operator, nonzero B(E2) requires delta-A nonzero in this model. | model-result | model | Eq. (5) | true |
| HM11-8 | With the specified particle-rotor M1 operator and gyromagnetic factors, B(M1) for delta-A nonzero is predicted to exceed the delta-A = 0 strength. | model-result | model | Eq. (7) | true |
| HM11-9 | In the chiral construction, the two nearly degenerate partner states have opposite A eigenvalues. | model-result | model | Eq. (9) | true |
| HM11-10 | Figure 2(a) depicts the allowed E2 and stronger M1 transition classes and also shows weaker allowed delta-I = 1 M1 transitions. | selection-rule-summary | model | Figure 2(a) | true |
| HM11-11 | The numerical particle-rotor example has approximate partner-band degeneracy over 13 < I < 24. | model-result | model | Figure 2(b) | true |
| HM11-12 | The calculated angular-momentum vectors favor coplanar low-spin and high-spin aligned limits, leaving moderate spin as the candidate chiral region. | model-result | model | Figure 3 | true |
| HM11-13 | The author reports that measured electromagnetic properties of 128Cs and 126Cs are consistent with the proposed rules. | author-comparison | interpretation | arXiv PDF p. 7 | true |
| HM11-14 | The author summarizes the 134Pr in-band B(E2) values as differing by at least a factor of two. | author-summary | interpretation | arXiv PDF p. 7 | true |
| HM11-15 | The author reports that measured 134Pr M1 transitions violate the proposed rule. | author-summary | interpretation | arXiv PDF p. 7 | true |
| HM11-16 | The author cautions that deviations from the special model assumptions can modify the selection rule. | applicability-limit | interpretation | arXiv PDF p. 7 | true |
| HM11-17 | The 128Cs comparison cites Grodner et al. 2006, so the article adds no independent 128Cs transition-strength dataset. | source-lineage | direct | Reference [8] | true |
| HM11-18 | The numerical illustration uses A=130, Z=55, beta=0.3, and a core moment-of-inertia parameter of 8.55 hbar-squared/MeV. | model-input | model | arXiv PDF p. 5 | true |

## Evidence Classification and Limits

The symmetry operator and transition inequalities are model results. The statements about 128Cs, 126Cs, and 134Pr are the author’s comparisons to previously reported measurements; they are not measurements in this paper. The 128Cs comparison points to Grodner et al. 2006, represented in [[grodner-2006-128cs-chiral-doublet-lifetimes]]. This article does not report event-level spectra, a new lifetime, a new absolute B value, or a covariance matrix.

The rule is conditional on the special same-j proton-particle/neutron-hole configuration, gamma = 90 degrees, the selected collective E2 contribution, and the M1 operator and gyromagnetic assumptions. The paper explicitly says realistic deviations can modify the rule. Near-degenerate bands alone do not establish that its symmetry assignment applies. The authors also note that equal spin-parity had not been experimentally proved for many of the candidate pairs discussed.

For 134Pr, the factor-of-two B(E2) difference and M1-rule violation are retained here as the author’s summary of cited work, not as an independent remeasurement or a new numerical extraction. The source is useful as a conditional model discriminator and as a warning against treating near-degeneracy or any single B(M1)/B(E2) trend as sufficient evidence of chiral geometry.

## Wiki Relations

- The 128Cs experimental comparison is linked to [[grodner-2006-128cs-chiral-doublet-lifetimes]]; the 2003 level-scheme and DCO context is [[koike-2003-128cs-chiral-doublet-bands]]. These are experimental records, not extra calculations in this article.
- The model context is [[particle-rotor-model]] and [[triaxial-particle-rotor-model]]. The cross-source interpretation is tracked in [[chirality-wobbling-competition-evidence]].

## Knowledge Impact and Learning Decision

Decision: **limits**. The model provides a symmetry-based set of transition tests for a clearly specified odd-odd limit, and the author finds the reported 128Cs properties consistent with it. The 134Pr comparison is a counterexample within the same article. This makes electromagnetic transition patterns more useful as conditional, configuration-aware diagnostics, but it does not promote the 128Cs assignment to direct geometric evidence or add an independent experiment.

## Summary

This paper derives A-quantum-number E2/M1 selection rules in a restricted particle-rotor model and compares them with previously published 128Cs and 134Pr electromagnetic evidence.

## Key Results

- HM11-1–8 specify the model assumptions, A operator, and conditional E2/M1 selection rules.
- HM11-9–12 give model-state/geometry examples; HM11-13–15 summarize the authors’ comparison with 128Cs and 134Pr.
- HM11-17 records the data/reference lineage for the 128Cs comparison.

## Competing Interpretations and Limitations

The rules depend on the selected gamma=90° and same-j particle-hole model. Koike 2004 states the rule can hold without chiral geometry; the paper’s cited-data comparisons are not new measurements or direct A labels.

## Extracted Pages

- [[koike-2004-chiral-bands-selection-rules]]
- [[koike-2003-128cs-chiral-doublet-bands]]
- [[petrache-2006-near-degenerate-chiral-misinterpretation]]
- [[chirality-wobbling-competition-evidence]]
