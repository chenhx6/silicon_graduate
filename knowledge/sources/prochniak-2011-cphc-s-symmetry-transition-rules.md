---
type: source
title: "Prochniak et al. 2011 - S symmetry in the core-particle-hole coupling model"
aliases: [Prochniak 2011 CPHC S-symmetry, S symmetry and M1/E2 staggering]
created: 2026-10-10
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "A symmetry of the CPHC model of odd-odd nuclei and its consequences for properties of M1 and E2 transitions"
authors: [L. Próchniak, S. G. Rohoziński, Ch. Droste, K. Starosta]
journal: "Acta Physica Polonica B"
year: 2011
volume: 42
issue: 3-4
pages: "465-469"
doi: "10.5506/aphyspolb.42.465"
canonical_source: "https://doi.org/10.5506/aphyspolb.42.465"
full_text_url: "https://www.actaphys.uj.edu.pl/fulltext?series=Reg&vol=42&page=465"
downloaded_pdf_sha256: "38086d08899d60b4b400be263ec600596c0ca971e339ff5cde1d9d13c9e052cd"
nuclei: [126Cs, 128Cs, 130Cs, 132La, 134Pr, 135Nd]
models: [core-particle-hole-coupling, Bohr-Hamiltonian, chiral-symmetry-breaking]
observables: [B(M1), B(E2), inband-strength, interband-strength, M1-staggering]
methods: [discrete-symmetry, selection-rules, gamma-soft-core]
tags: [S-symmetry, chirality, electromagnetic-selection-rules, triaxiality, 126Cs]
citation_key: "Prochniak_2011"
raw_file: "raw/papers/codex-day10/prochniak-2011-cphc-s-symmetry.pdf"
raw_sha256: "38086d08899d60b4b400be263ec600596c0ca971e339ff5cde1d9d13c9e052cd"
---

# A symmetry of the CPHC model and M1/E2 transition staggering

## Bibliographic Record

- L. Próchniak, S. G. Rohoziński, Ch. Droste, and K. Starosta, “A symmetry of the CPHC model of odd-odd nuclei and its consequences for properties of M1 and E2 transitions,” *Acta Phys. Pol. B* **42**(3–4), 465–469 (2011), DOI 10.5506/aphyspolb.42.465.
- Crossref verifies the authors, journal, volume, issue, first page, year, and DOI, but supplies no article title. The Acta Physica Polonica B article page and the PDF title page verify the exact title.
- The five-page PDF was retrieved from the journal’s public full-text endpoint; SHA-256 is 38086d08899d60b4b400be263ec600596c0ca971e339ff5cde1d9d13c9e052cd. The full text, Eqs. (1)–(9), references, and Figure 1 schematic were read/visually checked.

## Model and S-Symmetry

The Core-Particle-Hole Coupling (CPHC) Hamiltonian contains an even-even core, a proton particle, a neutron hole, quadrupole interactions and a proton-neutron interaction. The new symmetry operator is S = Pα Cπν: Pα changes the sign of the five-dimensional core deformation coordinates and includes a rotation in the intrinsic frame; Cπν exchanges the proton and neutron states. Pα is explicitly not spatial parity. A good S quantum number s = ±1 exists when the core Bohr Hamiltonian is Pα-invariant and both particles occupy the same single-j shell.

For E2 transitions, the dominant core operator is odd under S, so transitions between states with the same s are suppressed. For M1, the one-particle part is not purely even or odd, but at gR − (gπ+gν)/2 = 0 the same-s matrix element vanishes for unequal spins. With realistic A≈130 gyromagnetic factors the exact condition is slightly broken, but same-s M1 probabilities remain small relative to different-s transitions.

In a gamma-soft Wilets–Jean core the CPHC Hamiltonian is S-invariant. For a rigid Davydov–Filippov core, the analogous invariance requires maximal triaxiality gamma = π/6. Thus the paper gives a second model symmetry condition for transition-strength staggering alongside the Koike A-quantum-number selection-rule framework.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PS11-1 | The new S operator is the product of deformation-coordinate alpha parity Pα and proton-neutron exchange Cπν. | symmetry-definition | model | Eq. (3) | true |
| PS11-2 | Pα maps the deformation and intrinsic Euler angles as specified by the authors and is not ordinary spatial parity. | symmetry-definition | model | Eq. (5) | true |
| PS11-3 | If the core Bohr Hamiltonian is Pα-invariant, the CPHC odd-odd Hamiltonian is S-invariant and its states carry s=±1. | symmetry-condition | model | printed p. 467 | true |
| PS11-4 | With the dominant core E2 operator odd under S, E2 transitions between states with the same s are suppressed relative to different-s transitions. | model-selection-rule | model | printed p. 467, Section 2.2 | true |
| PS11-5 | For a single-j proton/neutron space, M1 transitions between same-s states vanish at gR − (gπ+gν)/2 = 0 for unequal spins. | model-selection-rule | model | Eq. (9) | true |
| PS11-6 | The paper gives A≈130 values gR=0.44, gπ=1.22, gν=−0.21, for which same-s M1 probabilities are nonzero but very small. | model-input/result | model | printed p. 468 | true |
| PS11-7 | The S symmetry is conserved in the studied gamma-soft Wilets–Jean CPHC Hamiltonian. | model-result | model | printed p. 468 | true |
| PS11-8 | For a rigid core, the analogous Pα invariance requires maximal triaxiality gamma=π/6. | model-condition | model | printed p. 469 | true |
| PS11-9 | Small deviations from exact S invariance need not destroy the M1/E2 staggering pattern. | applicability-limit | model | printed p. 466 | true |
| PS11-10 | This Letter explains staggering calculated in its earlier CPHC model; it contains no new lifetime, absolute B value, or experimental level scheme. | source-type-boundary | direct | References [3] and Conclusion | true |
| PS11-11 | The experimental 126Cs study cites this paper as its S-symmetry interpretation for M1 staggering; this theory article does not add a second 126Cs experiment. | source-lineage | direct | Reference [8] | true |

## Distinction from the Koike A Quantum Number

The S symmetry is defined through deformation-space alpha parity and exchange of proton and neutron states. The longer EPJA follow-up [[rohozinski-2011-cphc-s-symmetry-chirality]] explicitly calls S a generalization of Koike A within CPHC (CPHC11-5/12). It still has a distinct operator implementation and model domain; labels s and A are not interchangeable without a state-by-state mapping. This paper therefore does not resolve the Wang 2005 thesis paraphrase that reverses the Koike A-rule M1 direction.

The connection to 126Cs is interpretive: Grodner et al. 2011 reports measured inband/interband M1 staggering and cites this work for the additional S-symmetry explanation. The lifetime measurements are in the Grodner article, not here. The S-symmetry mechanism is a model result and a non-uniqueness condition on M1 staggering, not a direct observation of geometry.

## Quantitative Parameter Check

For the paper’s A≈130 example, the stated gyromagnetic values give

gR − (gπ+gν)/2 = 0.44 − (1.22 − 0.21)/2 = −0.065.

The exact same-s suppression condition is therefore not met, but the residual is small compared with the individual terms. This reproduces the authors’ statement that same-s M1 probabilities are nonzero but very small. It is a check of the model input arithmetic, not a measurement of g factors in 126Cs.

## Knowledge Impact and Learning Decision

Decision: **limits**. The paper supplies a distinct symmetry mechanism that can contribute to M1/E2 staggering in the same configuration and deformation region. It strengthens the boundary that M1 staggering alone cannot establish chirality, while leaving the Koike-A versus Wang-thesis direction conflict unresolved.

## Wiki Relations

- Experimental source that invokes S symmetry: [[grodner-2011-126cs-chiral-selection-rules]].
- Distinct A-symmetry source: [[koike-2004-chiral-bands-selection-rules]].
- Related data/theory pages: [[wang-2006-126cs-candidate-chiral-doublet]], [[wang-shouyu-2005-126cs-123i-chiral-thesis]], [[grodner-2011-bm1-staggering-structural-composition]], and [[chirality-wobbling-competition-evidence]].
- Model context: [[particle-rotor-model]] and [[triaxial-particle-rotor-model]]; the CPHC variant is defined and locatored in this source page.

## Scope and Reading Depth

The five-page Acta article, Eqs. (1)–(9), references, and Fig. 1 were reviewed; the A≈130 gyromagnetic-parameter arithmetic was checked.

## Summary

The paper defines an S symmetry in the core-particle-hole-coupling model and derives conditional M1/E2 transition suppression. S is not the Koike A quantum number and is not ordinary spatial parity.

## Key Results

- PS11-1/2/3 define S=PαCπν and the model conditions for same-s suppression.
- PS11-5/6 give the Eq. (9) gyromagnetic cancellation condition and the A≈130 residual −0.065.
- PS11-7/8/9 discuss consequences for staggering and relation to the Koike A rule.

## Competing Interpretations and Limitations

These are model results, not measured s/A labels or geometry. The numerical suppression is approximate for the cited A≈130 parameters; the longer Rohoziński 2011 paper extends the same theoretical line, not a second experiment.

## Extracted Pages

- [[rohozinski-2011-cphc-s-symmetry-chirality]]
- [[grodner-2011-126cs-chiral-selection-rules]]
- [[chirality-wobbling-competition-evidence]]
