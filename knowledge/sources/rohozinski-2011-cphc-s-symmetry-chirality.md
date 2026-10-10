---
type: source
title: "Rohoziński et al. 2011 - Odd-odd nuclei as core-particle-hole systems and chirality"
aliases: [Prochniak Rohozinski 2011 CPHC follow-up, S-symmetry CPHC model 2011]
created: 2026-10-10
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Odd-odd nuclei as the core-particle-hole systems and chirality"
authors: [S. G. Rohoziński, L. Próchniak, K. Starosta, Ch. Droste]
journal: "The European Physical Journal A"
year: 2011
volume: 47
article_number: "90"
doi: "10.1140/epja/i2011-11090-7"
canonical_source: "https://doi.org/10.1140/epja/i2011-11090-7"
full_text_url: "https://link.springer.com/content/pdf/10.1140/epja/i2011-11090-7.pdf"
downloaded_pdf_sha256: "94b2b3bc89c1d942f07f7c512c5aecc38c3cc08bbf48dac507ad373ace64b8c9"
license: "CC BY-NC"
nuclei: []
models: [core-particle-hole-coupling, Bohr-Hamiltonian, Wilets-Jean, Davydov-Filippov]
observables: [band-energy, band-splitting, B(E2), B(M1), magnetic-moment, S(I)]
methods: [discrete-symmetry, CPHC-diagonalization, triaxial-shape-variation, transition-matrix-element-analysis]
tags: [S-symmetry, CPHC, nuclear-chirality, M1-staggering, non-unique-fingerprint, A130]
citation_key: "Rohozinski_2011"
raw_file: "raw/papers/codex-day10/rohozinski-2011-cphc-s-symmetry.pdf"
raw_sha256: "94b2b3bc89c1d942f07f7c512c5aecc38c3cc08bbf48dac507ad373ace64b8c9"
---

# Odd-odd nuclei as core-particle-hole systems and chirality

## Bibliographic Record

- S. G. Rohoziński, L. Próchniak, K. Starosta, and Ch. Droste, “Odd-odd nuclei as the core-particle-hole systems and chirality,” *Eur. Phys. J. A* **47**, 90 (2011), DOI 10.1140/epja/i2011-11090-7.
- Crossref verifies title, authors, journal, volume, article number and 2011 publication. The 15-page Springer PDF is available under CC BY-NC; its SHA-256 is 94b2b3bc89c1d942f07f7c512c5aecc38c3cc08bbf48dac507ad373ace64b8c9.
- The paper is the full-length follow-up in the same theory lineage as Próchniak et al., *Acta Phys. Pol. B* **42**, 465 (2011); EPJA Ref. [28] cites that Acta paper. They are not independent theory frameworks.

## Model and Symmetry Definition

The Core-Particle-Hole Coupling (CPHC) model treats an odd-odd system as an even-even core plus a proton particle and a neutron hole. The core is described by a Bohr Hamiltonian with variable beta, gamma and Euler angles. The new operator is S = Pα Cπν: Pα reverses the five-dimensional quadrupole-deformation coordinates and includes a rotation in the intrinsic frame; Cπν exchanges proton and neutron states. The paper emphasizes that Pα is not ordinary spatial parity.

For the core to be Pα-symmetric, its potential and inertial functions must satisfy the alpha-parity relations in Eq. (7). The combined Hamiltonian is then S-invariant when the proton and neutron single-particle energy spectra match up to a common shift. The eigenstates receive a new quantum number s = ±1. The authors call S a generalization of the A operation introduced in the Koike particle-rotor selection-rule papers, not an identical operator or interchangeable state label.

## Electromagnetic Selection Rules

The dominant core E2 operator is odd under S; its matrix elements between states with the same s vanish in the model. The single-particle E2 contributions are not exactly zero in the full odd-odd operator but are usually smaller than the core term. The M1 operator contains a collective core term and proton/neutron orbital-spin terms. In the single-j limit, same-s M1 matrix elements vanish for unequal spins when gR − (gπ+gν)/2 = 0.

For the A≈130 parameter example, the authors use gR = 0.44, gπ = 1.22 and gν = −0.21. The cancellation term is −0.065, so same-s M1 probabilities are small but nonzero. This is a model-input result, not a measured magnetic factor for 126Cs.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CPHC11-1 | The CPHC Hamiltonian is a core-particle-hole system with a core Bohr Hamiltonian and quadrupole interactions to proton and neutron-hole degrees of freedom. | model-definition | model | Eqs. (1)–(2) | true |
| CPHC11-2 | The combined symmetry is S = Pα Cπν, where Pα acts in five-dimensional deformation space and Cπν exchanges proton/neutron states. | symmetry-definition | model | Eq. (3) | true |
| CPHC11-3 | In the first gamma sextant, Pα maps (beta,gamma,Omega) to (beta,pi/3−gamma,Rx(pi/2)Omega); this is not spatial parity. | symmetry-definition | model | Eq. (11) | true |
| CPHC11-4 | The combined S symmetry holds when the core is Pα-invariant and proton/neutron single-particle energy differences match up to a common shift. | symmetry-condition | model | Eq. (22) | true |
| CPHC11-5 | S labels CPHC eigenstates with s=±1, and the authors describe S as a generalization of Koike's A operation. | symmetry-lineage | model | printed p. 4, paragraph following Eq. (22) | true |
| CPHC11-6 | The collective-core E2 operator is odd under Pα/S; same-s E2 reduced matrix elements are suppressed when the core contribution dominates. | model-selection-rule | model | Eqs. (14)–(15), (23) | true |
| CPHC11-7 | For same-j proton/neutron orbitals, same-s M1 matrix elements vanish when gR−(gπ+gν)/2=0. | model-selection-rule | model | Eq. (9) | true |
| CPHC11-8 | The stated A≈130 gyromagnetic parameters leave a residual −0.065, yielding small but nonzero same-s M1 strengths in the model. | model-input/result | model | Eq. (27) | true |
| CPHC11-9 | With same-j particle-hole configurations and alpha-symmetric WJ, well and barrier cores, partner bands exhibit near-degeneracy and regular electromagnetic staggering. | model-result | model | Figs. 5–11 | true |
| CPHC11-10 | Changing the particle-hole orbitals breaks proton-neutron symmetry and weakens or irregularizes the calculated staggering. | model-result | model | Figs. 12–17 | true |
| CPHC11-11 | Breaking core alpha-parity symmetry removes regular B(M1)/B(E2) staggering and weakens interband transitions in the model. | model-result | model | Figs. 18–25 | true |
| CPHC11-12 | The authors conclude that S-symmetric odd-odd models display fingerprints usually ascribed to chirality without assuming that angular momenta form chiral geometry. | applicability-boundary | model | Conclusions, printed p. 14 | true |
| CPHC11-13 | The EPJA article cites the 2011 Acta paper at Ref. [28], establishing a short-note/full-paper relationship within the same S-symmetry theory lineage. | source-lineage | direct | Reference [28] | true |

## Results and Non-Uniqueness Boundary

The calculations use fictitious odd-odd nuclei near A≈130 to compare gamma-soft Wilets–Jean cores, cores with a gamma well or barrier, rigid Davydov–Filippov cores, same-j particle-hole configurations, different-j configurations and alpha-asymmetric cores. The same-j, alpha-symmetric cases retain near-degenerate partner bands, similar inband E2 strengths, and strong regular inband/interband M1 and E2 staggering across different core potentials (Figs. 5–11). The authors explicitly say they do not assume that these systems possess chiral angular-momentum geometry.

When proton-neutron symmetry is broken by different particle-hole orbitals, the calculated band splitting grows and the staggering becomes weaker and irregular (Figs. 12–17). When alpha-parity of the core is broken, the regular staggering disappears and interband transitions become weak (Figs. 18–25). This supplies a model route for chiral-like electromagnetic fingerprints that depends on symmetry conditions but does not require a demonstrated left/right geometry.

## Distinction from the Koike A Rule and Relation to Data

The EPJA paper calls S a generalization of the Koike A operation within CPHC, while changing the symmetry implementation from intermediate-axis rotation plus exchange to deformation-space alpha parity plus exchange. The A and s labels should not be assigned to experimental levels by name alone. In the model, S can produce transition-strength fingerprints in states for which no chiral geometry was imposed, so matching those patterns cannot by itself establish orthogonal angular-momentum coupling.

Grodner et al. 2011 uses the short Acta S-symmetry paper to interpret measured 126Cs M1 staggering (GR126-8/9). The Acta paper and this EPJA follow-up are one theory lineage; neither adds a new 126Cs experiment. The later Warsaw DSA measurement remains a separate data set, and its measured line strengths do not provide direct s or A labels.

## Quantitative Model-Parameter Check

For the paper’s A≈130 example,

gR − (gπ+gν)/2 = 0.44 − (1.22−0.21)/2 = −0.065.

The exact same-s M1 cancellation is not met, but the small residual is consistent with the calculated same-s M1 amplitudes being small rather than identically zero. This is a model-parameter arithmetic check, not an experimental g-factor measurement.

## Knowledge Impact and Learning Decision

Decision: **limits** the uniqueness of chiral electromagnetic fingerprints. The paper shows that an S-symmetric CPHC Hamiltonian can generate doublets and M1/E2 staggering without imposing chiral geometry. It strengthens the need to combine transition strengths with line-level assignments, configuration evidence and geometry-sensitive observables.

## Wiki Relations

- Short theory report: [[prochniak-2011-cphc-s-symmetry-transition-rules]].
- Experimental S-symmetry application: [[grodner-2011-126cs-chiral-selection-rules]].
- Contrasting A-rule source: [[koike-2004-chiral-bands-selection-rules]] and [[hamamoto-2011-selection-rule-chiral-geometry]].
- Current comparison/question map: [[chirality-wobbling-competition-evidence]], [[wang-2006-126cs-candidate-chiral-doublet]], [[wang-shouyu-2005-126cs-123i-chiral-thesis]].

## Scope and Reading Depth

The 15-page EPJA article, Eqs. (1)–(31), and selected Figs. 5–11, 12–13, and 24–25 were reviewed. The paper is a theoretical extension of the Prochniak Acta work.

## Summary

The S-symmetric CPHC model can generate partner-band and M1/E2 electromagnetic patterns without assuming chiral geometry, demonstrating that these fingerprints are not unique geometry measurements.

## Key Results

- CPHC11-1–4 define the CPHC model and S operator.
- CPHC11-9/12 show parameter regimes with similar electromagnetic patterns without imposed chirality.
- CPHC11-10/11 show how changing orbitals or core symmetry weakens the regular pattern.

## Competing Interpretations and Limitations

This is a model scan, not experimental evidence or a new dataset. Results depend on single-j particle-hole and core-symmetry assumptions; the paper extends Prochniak 2011 rather than providing an independent experimental confirmation.

## Extracted Pages

- [[prochniak-2011-cphc-s-symmetry-transition-rules]]
- [[grodner-2011-bm1-staggering-structural-composition]]
- [[chirality-wobbling-competition-evidence]]
