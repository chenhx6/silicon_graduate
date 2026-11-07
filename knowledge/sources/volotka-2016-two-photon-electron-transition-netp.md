---
type: source
title: "Nuclear Excitation by Two-Photon Electron Transition"
aliases: [Volotka 2016 NETP, Volotka 2016 two-photon nuclear excitation]
created: 2026-11-07
updated: 2026-11-07
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: deep-read
title_original: "Nuclear Excitation by Two-Photon Electron Transition"
authors: [A. V. Volotka, A. Surzhykov, S. Trotsenko, G. Plunien, Th. Stöhlker, S. Fritzsche]
journal: Physical Review Letters
year: 2016
volume: 117
pages: 243001
doi: 10.1103/PhysRevLett.117.243001
language: en
canonical_source: doi:10.1103/PhysRevLett.117.243001
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2016_Volotka et al_Nuclear Excitation by Two-Photon Electron Transition.pdf"
raw_sha256: f5e8286a8662e1d869dbff49d51877647c182e190c078c59a343b7724978026f
archive_required: true
nuclei: [225ac]
reactions: []
observables: [two-photon-transition-probability, nuclear-excitation-rate, continuous-energy-sharing]
methods: [relativistic-qed, dirac-hartree-fock, second-order-perturbation-theory]
tags: [netp, nuclear-excitation, two-photon, non-resonant-matching, highly-charged-ions, isomeric-control]
---

# Volotka et al. (2016): Nuclear Excitation by Two-Photon Electron Transition

## Bibliographic Record

A. V. Volotka, A. Surzhykov, S. Trotsenko, G. Plunien, Th. Stöhlker, and S. Fritzsche, "Nuclear Excitation by Two-Photon Electron Transition," *Physical Review Letters* **117**, 243001 (2016), DOI: `10.1103/PhysRevLett.117.243001`. Primary PDF is 5 pages, SHA-256: `f5e8286a8662e1d869dbff49d51877647c182e190c078c59a343b7724978026f`.

## Scope and Reading Depth

The 5-page Letter was read completely. Reading covers relativistic bound-state QED derivations of second-order electron-nucleus transitions (PDF p. 1--2 / printed p. 243001-1--2), Feynman diagrams (Fig. 1), continuous energy-sharing differential decay rates (PDF p. 3 / printed p. 243001-3, Eq. 6, Fig. 2), and numerical evaluation for He-like \(^{225}\)Ac\(^{87+}\) in Table I (PDF p. 4 / printed p. 243001-4).

## Summary

The authors propose a new mechanism of nuclear excitation: Nuclear Excitation by Two-Photon Electron Transition (NETP). While single-photon NEET and single-electron NEEC require strict resonance matching between atomic and nuclear levels within level widths (\(10^{-7}\text{--}1\text{ eV}\)), NETP utilizes two-photon electron de-excitation where one photon carries continuous energy \(\omega_1\) into the continuum, while the second photon carries \(\omega_2 = \Delta E_{\text{el}} - \omega_1 = E_N\), exciting the nucleus. This continuous energy sharing bypasses the strict energetic matching bottleneck.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| V16-1 | Formulates NETP mechanism where continuous two-photon electronic decay automatically satisfies nuclear excitation without energetic degeneracy. | theoretical-proposal | theoretical derivation | printed p.243001-1--2, Fig. 1 | true |
| V16-2 | Calculates NETP probability P_NETP = 3.5e-9 for 1s2s 1S0 -> 1s2 1S0 in He-like 225Ac87+ (Delta E_el = 92.42 keV) exciting the 3/2+ state (40.09 keV). | model-calculation | derived value | printed p.243001-3--4, Table I | true |
| V16-3 | NETP probability is comparable to resonant NEET probabilities in neutral atoms (~1e-7 to 1e-10) while possessing continuous phase space. | model-calculation | comparative analysis | printed p.243001-4 | true |
| V16-4 | Proposes detection at heavy-ion storage rings via coincidence between monochromatic photon omega_1 = 52.33 keV and nuclear de-excitation gamma-ray. | method-proposal | experimental design | printed p.243001-4 | true |

## Competing Interpretations and Limitations

Single-photon resonant excitation (NEET/NEEC) has higher peak cross sections at exact resonance, but requires fine-tuned matching of atomic and nuclear energies. NETP circumvents the resonance constraint, but its total probability is limited by the second-order electromagnetic coupling (\(\sim 3.5 \times 10^{-9}\)), requiring high ion luminosity in storage rings for experimental observation.

## Extracted Pages

- netp
- neet
- neec
- 225ac
