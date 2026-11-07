---
type: source
title: "Nuclear Excitation by Electron Capture in Excited Ions"
aliases: [Gargiulo 2022 NEEC in excited ions, Gargiulo 2022 NEEC-EXI]
created: 2026-11-07
updated: 2026-11-07
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: deep-read
title_original: "Nuclear Excitation by Electron Capture in Excited Ions"
authors: [Simone Gargiulo, Ivan Madan, Fabrizio Carbone]
journal: Physical Review Letters
year: 2022
volume: 128
pages: 212502
doi: 10.1103/PhysRevLett.128.212502
language: en
canonical_source: doi:10.1103/PhysRevLett.128.212502
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2022_Gargiulo et al_Nuclear Excitation by Electron Capture in Excited Ions.pdf"
raw_sha256: dc0f0fe54e8637a088ba4e9f3b11e3b6d98c07de833a9bc6cb615dc6b29c183f
archive_required: true
nuclei: [73ge, 93mo, 98tc, 125te]
reactions: []
observables: [resonance-strength-boost, k-shell-capture-channels, recoupling-coefficient-lambda]
methods: [flexible-atomic-code-fac, feshbach-projection-operator, recoupling-angular-momentum-algebra, xatom-code]
tags: [neec-exi, excited-ions, ground-state-assumption-violation, k-shell-screening, 73ge, 93mo]
---

# Gargiulo et al. (2022): Nuclear Excitation by Electron Capture in Excited Ions

## Bibliographic Record

Simone Gargiulo, Ivan Madan, and Fabrizio Carbone, "Nuclear Excitation by Electron Capture in Excited Ions," *Physical Review Letters* **128**, 212502 (2022), DOI: `10.1103/PhysRevLett.128.212502`. The archived 17-page PDF is the author-extended preprint version (arXiv:2102.05718v2) containing the complete 5-page Letter text plus 12 pages of Supplemental Material. SHA-256: `dc0f0fe54e8637a088ba4e9f3b11e3b6d98c07de833a9bc6cb615dc6b29c183f`.

## Scope and Reading Depth

Deep reading of the Letter and Supplemental Material. Locators examined: GSA violation and NEEC-EXI concept (PDF p. 1--2 / printed p. 212502-1--2, Fig. 1), recoupling coefficient \(\Lambda\) (PDF p. 2 / printed p. 212502-2, Eq. 2), opening of 100 K-shell channels in \(^{73}\)Ge at \(q=29+\) in Fig. 2 and Table I (PDF p. 2--3 / printed p. 212502-2--3), and discussion of \(^{93}\)Mo stopping (PDF p. 4 / lines 499--515 and 580--583).

## Summary

The authors demonstrate that lifting the Ground State Assumption (GSA) allows NEEC to occur in out-of-equilibrium excited electronic configurations (NEEC-EXI). In \(^{73}\)Ge (13.28 keV transition), outer-electron screening in excited configurations lowers K-shell binding energies below the nuclear excitation energy, opening 100 new resonant K-capture channels at \(q=29+\) and boosting resonance strength by over three orders of magnitude. For \(^{93}\)Mo, excited configurations allow L-shell vacancies at lower charge states (\(q \approx 30\text{--}32\)), providing a \(10^2\text{--}10^3\) gain, though still leaving a multi-order gap to 1%.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GA22-1 | Lifts Ground State Assumption, formulating NEEC in excited electronic configurations (NEEC-EXI) with angular momentum recoupling coefficient Lambda. | theoretical-proposal | theoretical derivation | printed p.212502-1--2, Fig. 1, Eq. (2) | true |
| GA22-2 | Outer-electron screening in excited configurations opens 100 new resonant K-shell capture channels in 73Ge at q=29+. | model-calculation | derived value | printed p.212502-2--3, Fig. 2 | true |
| GA22-3 | Resonance strength in 73Ge increases by >3 orders of magnitude (from 1.25e-4 b*eV under GSA to 0.518 b*eV under NEEC-EXI). | model-calculation | derived value | printed p.212502-3, Table I | true |
| GA22-4 | Evaluates 93Mo stopping: excited configurations allow L-shell vacancies at q=30-32, boosting rates by 2-3 orders of magnitude. | theoretical-extrapolation | model extrapolation | printed p.212502-4, lines 500--515 | true |

## Competing Interpretations and Limitations

NEEC-EXI establishes that out-of-equilibrium atomic states significantly enhance resonance strengths, but the magnitude of the macroscopic enhancement in a beam-foil experiment depends on the transient population of excited atomic states during ion stopping.

## Extracted Pages

- neec-exi
- 73ge
- mo93m
