---
type: source
title: "93mMo Isomer Depletion via Beam-Based Nuclear Excitation by Electron Capture"
aliases: [Wu 2019 Mo93m NEEC theory, Wu 2019 9-orders-discrepancy]
created: 2026-11-07
updated: 2026-11-07
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: deep-read
title_original: "93mMo Isomer Depletion via Beam-Based Nuclear Excitation by Electron Capture"
authors: [Yuanbin Wu, Christoph H. Keitel, Adriana Pálffy]
journal: Physical Review Letters
year: 2019
volume: 122
pages: 212501
doi: 10.1103/PhysRevLett.122.212501
language: en
canonical_source: doi:10.1103/PhysRevLett.122.212501
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2019_Wu et al_Mo 93 m Isomer Depletion via Beam-Based Nuclear Excitation by Electron Capture.pdf"
raw_sha256: 65a948a1144b2745a83cf0888fba24fa2fcdd79aa786faed6723f768641daf45
archive_required: true
nuclei: [93mo]
reactions: []
observables: [neec-resonance-strength, partial-capture-probabilities, stopping-power, charge-state-distribution]
methods: [multiconfigurational-dirac-fock, grasp92, casp-code, lorentz-profile-integration]
tags: [mo93m, neec, theory-discrepancy, stopping-power, charge-state-evolution, isomer-depletion]
---

# Wu et al. (2019): \(^{93\text{m}}\)Mo Isomer Depletion via Beam-Based Nuclear Excitation by Electron Capture

## Bibliographic Record

Yuanbin Wu, Christoph H. Keitel, and Adriana Pálffy, "\(^{93\text{m}}\)Mo Isomer Depletion via Beam-Based Nuclear Excitation by Electron Capture," *Physical Review Letters* **122**, 212501 (2019), DOI: `10.1103/PhysRevLett.122.212501`. Primary PDF is 6 pages, SHA-256: `65a948a1144b2745a83cf0888fba24fa2fcdd79aa786faed6723f768641daf45`.

## Scope and Reading Depth

The 6-page Letter was read completely. Reading covers formulation of beam-target NEEC stopping integrals (PDF p. 2 / printed p. 212501-2, Eqs. 1--3), stopping-power models and empirical charge-state distributions (PDF p. 3 / printed p. 212501-3, Fig. 2), mapping of 648 recombination channels (PDF p. 3 / printed p. 212501-3, Fig. 3), and Table I total probabilities and Table II shell-by-shell breakdown (PDF p. 4 / printed p. 212501-4).

## Summary

The authors calculate the theoretical probability of beam-based NEEC for \(^{93\text{m}}\)Mo slowing down in solid carbon. Modeling 648 atomic recombination channels across charge states \(\text{Mo}^{14+}\) to \(\text{Mo}^{42+}\) with MCDF wavefunctions and CasP stopping power, they find a total depletion probability \(P \approx 2.58 \times 10^{-11}\). This stands in conflict by approximately nine orders of magnitude with the experimental value of \(1.0(3)\%\) reported by Chiara et al. (Nature 2018).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| W19-1 | Calculates total NEEC depletion probability for 93mMo in solid carbon as P = (2.26 to 2.73)e-11 across 648 recombination channels. | model-calculation | derived value | printed p.212501-2--4, Table I | true |
| W19-2 | Demonstrates a 9-orders-of-magnitude discrepancy between relativistic atomic theory (~2.6e-11) and the Chiara 2018 report (1.0e-2). | theoretical-challenge | comparative analysis | printed p.212501-1, 4 | true |
| W19-3 | Identifies physical quenching of L-shell capture (P_L ~ 1.5e-19) due to charge-state cooling to q_bar ~ 20-25 during stopping in carbon. | physical-mechanism | theoretical model | printed p.212501-4, Table II | true |
| W19-4 | Shows that M-shell (P_M ~ 1.53e-11) and N-shell (P_N ~ 7.54e-12) dominate the total stopping-target NEEC probability. | model-calculation | derived value | printed p.212501-4, Table II | true |

## Competing Interpretations and Limitations

The calculation relies on the Ground State Assumption (GSA) and equilibrium stopping power. Later theoretical work showed that non-equilibrium excited ion states (Gargiulo 2022) and target electron Compton profiles (Rzadkiewicz 2021) can enhance cross sections, but still leave a multi-order-of-magnitude discrepancy with the 1% report.

## Extracted Pages

- mo93m
- neec
- stopping-power
- charge-state-distributions
