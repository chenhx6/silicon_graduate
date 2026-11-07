---
type: source
title: "Feasibility study of nuclear excitation by electron capture using an electron beam ion trap"
aliases: [Wang 2023 EBIT NEEC feasibility, Wang 2023 Fudan EBIT NEEC]
created: 2026-11-07
updated: 2026-11-07
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: deep-read
title_original: "Feasibility study of nuclear excitation by electron capture using an electron beam ion trap"
authors: [Yumiao Wang, Zhiguo Ma, Yi Yang, Changbo Fu, Wanbing He, Yugang Ma]
journal: Frontiers in Physics
year: 2023
volume: 11
pages: 1203401
doi: 10.3389/fphy.2023.1203401
language: en
canonical_source: doi:10.3389/fphy.2023.1203401
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2023_Feasibility study of nuclear excitation by electron capture using an electron beam ion trap.pdf"
raw_sha256: 5f54811a552c6a5bcc01a80b50ac6c7cfe59a96783ccf31a9fd346dfd5941334
archive_required: true
nuclei: [154eu, 157gd, 161dy, 181ta, 231pa, 237np, 63ni, 73ge, 83kr, 99ru, 111cd, 129i, 138la, 169tm, 187os, 201hg]
reactions: []
observables: [neec-resonance-strength, ebit-production-rate, coulomb-excitation-competition]
methods: [ebit-rate-modeling, dirac-fock-binding-energies, two-beam-energy-resonance-matching]
tags: [ebit, neec, highly-charged-ions, coulomb-excitation-background, experimental-feasibility, clean-environment]
---

# Wang et al. (2023): Feasibility study of nuclear excitation by electron capture using an electron beam ion trap

## Bibliographic Record

Yumiao Wang, Zhiguo Ma, Yi Yang, Changbo Fu, Wanbing He, and Yugang Ma, "Feasibility study of nuclear excitation by electron capture using an electron beam ion trap," *Frontiers in Physics* **11**, 1203401 (2023), DOI: `10.3389/fphy.2023.1203401`. Primary PDF is 8 pages, SHA-256: `5f54811a552c6a5bcc01a80b50ac6c7cfe59a96783ccf31a9fd346dfd5941334`.

## Scope and Reading Depth

The 8-page article was read completely. Reading scope covers EBIT operational principles and resonance matching (PDF p. 2 / printed p. 02, Fig. 1), Table 1 resonance strengths \(S_{\text{NEEC}}\) (in \(\text{b}\cdot\text{eV}\)) and beam energies for 16 heavy highly charged ions (PDF p. 4 / printed p. 04), Table 2 production rates \(R_{\text{NEEC}}\) and \(R_{\text{CE}}\) (in \(\text{s}^{-1}\)) under stated EBIT parameters (PDF p. 5 / printed p. 05), and background discrimination via two-beam energy modulation (PDF p. 5--6 / printed p. 05--06).

## Summary

The authors conduct a feasibility study of NEEC in an Electron Beam Ion Trap (EBIT). By trapping highly charged ions in ultra-high vacuum and bombarding them with a monoenergetic electron beam (\(\Delta E_e \sim 50\text{ eV}\)), stopping power losses and Doppler broadening are eliminated. Evaluating 16 candidate isotopes across \(E1, E2\), and \(M1\) transitions, they predict NEEC production rates reaching \(10^{-2}\text{--}10^{-1}\text{ s}^{-1}\), vastly exceeding Coulomb excitation backgrounds.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WA23-1 | Proposes EBIT for clean NEEC detection, eliminating solid-state stopping deceleration, Doppler shifts, and projectile-target nuclear collision backgrounds. | method-proposal | experimental design | printed p.01--03, Fig. 1 | true |
| WA23-2 | Evaluates NEEC resonance strengths S_NEEC (b*eV) for 16 heavy highly charged ions in Table 1 across E1, E2, and M1 transitions. | model-calculation | derived value | printed p.04, Table 1 | true |
| WA23-3 | Under typical EBIT conditions (L=3 cm, ni=1e8 cm-3, Ie=200 mA, Delta Ee=50 eV), Table 2 predicts NEEC rates of 1e-2 to 1e-1 s-1 (e.g., 4.36e-2 s-1 for 161Dy64+). | model-prediction | theoretical prediction | printed p.05, Table 2 | true |
| WA23-4 | Demonstrates that Coulomb excitation background is suppressed by orders of magnitude (R_CE ~ 1e-7 s-1 or strictly zero) at low electron beam energies. | model-calculation | comparative analysis | printed p.05, Table 2 | true |

## Competing Interpretations and Limitations

The study demonstrates that static ion-trap environments eliminate the backgrounds that compromised beam-foil measurements. Realization requires developing in-trap \(\gamma\)-ray or conversion-electron detection systems with high geometric efficiency at EBIT facilities.

## Extracted Pages

- ebit
- neec
- highly-charged-ions
