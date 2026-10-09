---
type: source
title: "Timár et al. 2007 - High-Spin Structure of 105Ag: Search for Chiral Doublet Bands"
aliases: [Timar 2007 105Ag, 105Ag chiral search]
created: 2026-08-11
updated: 2026-10-09
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "High-spin structure of 105Ag: Search for chiral doublet bands"
authors: [J. Timár, T. Koike, N. Pietralla, G. Rainovski, D. Sohler, T. Ahn, G. Berek, A. Costin, K. Dusling, T. C. Li, E. S. Paul, K. Starosta, C. Vaman]
journal: Physical Review C
year: 2007
volume: 76
pages: 024307
doi: 10.1103/PhysRevC.76.024307
language: English
canonical_source: https://doi.org/10.1103/PhysRevC.76.024307
citation_key: timar_2007_Highspinstructure
raw_file: "raw/papers/2007_Timár et al_High-spin structure of Ag 105.pdf"
raw_sha256: 730BE91DC2FFBBC785EBE36F5ECC50AEEFD8EF74D577C8A2E314204CB4F58442
nuclei: [105ag]
reactions: ["100Mo(10B,5n)105Ag"]
experiments: [stony-brook-linac-105ag-b10-58-64mev]
models: [total-routhian-surface, donau-frauendorf-geometrical-model]
observables: [dco-ratio, angular-momentum-alignment, bm1-be2-ratio, energy-staggering-parameter]
methods: [gamma-gamma-coincidence, dco-ratio]
tags: [experiment-ingest, project-ingest, a100, odd-a, nuclear-chirality, chiral-doublet-bands, counter-evidence]
---

# High-Spin Structure of `105Ag`: Search for Chiral Doublet Bands

## Bibliographic Record

Physical Review C 76, 024307 (2007), DOI `10.1103/PhysRevC.76.024307`. The protected BibTeX record is `timar_2007_Highspinstructure`.

## Supporting Information Availability

The official APS article page was checked on 2026-10-09. It returned HTTP 200 with no SI/attachment link; the supplemental resolver returned to the article record at `#supplemental`, and the standard supplemental-PDF endpoint returned HTTP 404. No SI file was found on these checked publisher routes; separately hosted author material is outside this check.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`.
- Covered scope: all 11 PDF pages, experiment/DCO method, full A–G partial level scheme and transition table, revised Band-E placement, new Bands F/G, TRS/Routhian/alignment assignments, branching-derived `B(M1)/B(E2)`, intended-partner null search, D/G chiral criteria, configuration-mixing alternative and summary.
- Not covered: raw coincidence matrices, detector-by-detector efficiencies, earlier level-scheme/lifetime sources, or the cited TAC calculations' original papers.
- Coverage caveats: many high-spin F/G/D assignments are tentative; branching ratios are not lifetime-separated absolute strengths; no dedicated TAC or quantum chiral calculation was performed for Bands D/G.

## Extracted Pages

- PDF pp.1-2: motivation, experiment, DCO calibration and prior-level-scheme context.
- PDF pp.3-5: Table I and complete partial A–G level scheme.
- PDF pp.6-8: revised placements, configuration analysis, TRS/Routhian/alignment and `B(M1)/B(E2)` comparisons.
- PDF p.9: D/G chiral-candidate criteria, configuration-mixing ambiguity and summary.
- PDF pp.10-11: references only.

## Paper Question and Scientific Motivation

The primary experiment asks whether the known positive-parity `πg9/2⊗ν(h11/2)^2` yrast Band E has a weak chiral side band analogous to Rh-region candidates. The broader question is whether Ag isotopes define the high-Z boundary of the A≈104 chiral region and how γ softness/rigidity evolves with neutron number (PDF pp.1-2).

## Method and Design Logic

- A higher-sensitivity γ-γ experiment reconstructs and corrects the `105Ag` level scheme, with DCO ratios constraining transition multipolarities and revised spins/parities (PDF pp.2-6; Figs.1-2; Table I).
- Experimental Routhians and alignments are compared with Woods-Saxon TRS configurations; branching-derived `B(M1)/B(E2)` ratios are compared with the Dönau-Frauendorf geometrical model to assign quasiparticle configurations (PDF pp.6-8; Figs.3-5; Tables II-III).
- The intended Band-E partner is tested as a detection-sensitivity null result. Separately, natural-parity Bands D/G are compared through same-spin energy separation, `S(I)` and `B(M1)/B(E2)` fingerprints, then explicitly audited against simple configuration mixing (PDF pp.8-9; Fig.6).

## Summary

The source extends/corrects the `105Ag` A–G level scheme. It finds no Band-E side band above approximately one tenth of Band E's population and therefore rejects a chiral partner for the intended `πg9/2⊗ν(h11/2)^2` structure at that sensitivity. Unexpectedly, Bands D/G form a linked, near-degenerate negative-parity pair with several chiral fingerprints. The paper calls D/G a good candidate but does not prove chirality: natural-parity `πg9/2⊗νh11/2(g7/2,d5/2)` configuration mixing remains experimentally indistinguishable without a dedicated quasiparticle-rotor/chiral calculation.

## Experimental or Theoretical Setup

- `100Mo(10B,5n)105Ag` at 58 and 64 MeV, Stony Brook tandem-injected superconducting LINAC.
- Enriched `100Mo` target `1.3 mg/cm²` on `20 mg/cm²` natural Pb backing.
- Six Compton-suppressed HPGe detectors plus a 14-element BGO multiplicity filter; about `10^8` γ-γ coincidences.
- DCO calibration: with stretched-quadrupole gate, `R_DCO≈0.6` for stretched dipole and `1` for stretched quadrupole; with dipole gate, expected ratios `1` and `≈1.5`.
- TRS supplies configurations/shapes and model inputs; the Dönau-Frauendorf calculation uses fixed `K_n/i_n`, literature `g_n`, `g_R=Z/A`, and TRS-derived `Q0/γ`.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TI07-1 | The 58/64-MeV experiment collected about `10^8` γ-γ coincidences with six suppressed HPGe detectors and a 14-element BGO filter. | experimental-fact | direct | PDF p.2 | true |
| TI07-2 | DCO ratios, coincidences and intensity/energy balances establish an A–G partial level scheme; Bands F/G are new, Band D is extended and Band E is repositioned. | experimental-fact | direct | PDF pp.2-6; Figs.1-2; Table I | true |
| TI07-3 | Weak links from Band E to A/C require Band E to be placed differently from Ref.27 and its spins to increase by `2ℏ` while retaining positive parity. | experimental-assignment | direct | PDF pp.5-8; Figs.1-3 | true |
| TI07-4 | TRS/Routhian/alignment and ratio agreement support `πg9/2` for Band A and `πg9/2⊗ν(h11/2)^2` for Band E. | author-interpretation | indirect | PDF pp.7-8; Figs.3,5 | true |
| TI07-5 | The experiment would have observed an intended Band-E side band if its population exceeded about one tenth of Band E; none was detected. | experimental-fact | direct | PDF p.8, Sec.III.B | true |
| TI07-6 | The authors conclude there is no chiral partner to Band E at the experiment's sensitivity and interpret this as a more γ-rigid axial `105Ag` yrast shape than γ-soft `106Ag`. | author-interpretation | indirect | PDF pp.8-9; Summary | true |
| TI07-7 | Negative-parity Bands C/D/G are assigned related `πg9/2⊗νh11/2(g7/2,d5/2)` three-quasiparticle configurations from TRS, alignments and branching ratios. | author-interpretation | indirect | PDF pp.7-8; Figs.4-5 | true |
| TI07-8 | Band F's five-quasiparticle assignment is tentative; small observed signature splitting and calculated ratio scale favor `(a,b)BEFG` over `(abc,abd)EB`. | author-interpretation | indirect | PDF p.8; Figs.4-5 | true |
| TI07-9 | Assuming `Q0=2 eb`, Band-E→C E1 branches give `B(E1)≈2×10^-5 W.u.`, which the authors state is too small to conclude octupole correlations. | derived-observable | indirect | PDF p.8 | true |
| TI07-10 | Bands D/G are linked and remain separated by about `70 keV` over the observed common-spin interval. | experimental-fact | direct | PDF pp.8-9; Figs.2,6 | true |
| TI07-11 | D/G show relatively smooth `S(I)` curves and mutually consistent branching-derived `B(M1)/B(E2)` values with pronounced ratio staggering. | experimental-fact | direct | PDF p.9; Fig.6 | true |
| TI07-12 | On the Koike criteria, the authors describe D/G as a good chiral-doublet candidate but not a perfect chiral geometry. | author-interpretation | direct | PDF p.9 | true |
| TI07-13 | No dedicated TAC calculation was performed for D/G; cited TAC only predicts triaxiality for Band C, assigned the same broad quasiparticle family. | model-boundary | direct | PDF p.9 | true |
| TI07-14 | The paper cannot distinguish chiral geometry from simple mixing of `πg9/2⊗νh11/2g7/2` and `πg9/2⊗νh11/2d5/2` configurations. | author-interpretation | direct | PDF p.9 | true |
| TI07-15 | Because D/G have natural parity, the authors warn that their similarities may arise from excitations without chiral angular-momentum coupling. | author-interpretation | direct | PDF p.9, Summary | true |
| TI07-SI-1 | The APS article page exposes no SI/attachment link; the supplemental resolver returns to the article record and the standard SI PDF endpoint returns HTTP 404. No SI file was found on the checked publisher routes. | evidence-boundary | direct | APS article `https://journals.aps.org/prc/abstract/10.1103/PhysRevC.76.024307`; resolver `https://link.aps.org/supplemental/10.1103/PhysRevC.76.024307`; standard endpoint `https://journals.aps.org/prc/supplemental/10.1103/PhysRevC.76.024307/PhysRevC.76.024307.supplemental.pdf` | true |

## Nuclear Structure Information

| Band(s) | Parity / identity | Assigned role | Evidence boundary |
|---|---|---|---|
| A | positive | `πg9/2` reference | TRS/Routhian/alignment supported |
| E | positive | corrected `πg9/2⊗ν(h11/2)^2` target band | intended chiral partner not observed above ≈0.1 intensity ratio |
| C/D/G | negative | related `πg9/2⊗νh11/2(g7/2,d5/2)` structures | D/G form candidate pair; configuration mixing remains viable |
| F | tentative negative | probable five-quasiparticle | first observed here; assignment tentative |

## Competing Interpretations and Limitations

- Band-E null result is sensitivity-bounded, not proof that no side band exists at any intensity; the axial/γ-rigid inference is model dependent.
- D/G fingerprints are not configuration-unique. Natural parity permits close low-j orbitals and simple mixing to imitate chiral-systematics observables.
- No D/G TAC/PRM wave functions, angular-momentum geometry, lifetimes, absolute strengths or measured mixing ratios are reported.
- `B(M1)/B(E2)` is branching-derived and uses model inputs; agreement is not a direct matrix-element symmetry test.
- Band F and high-spin D/G assignments include tentative spins/parities.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | This paper contains both direct counter-evidence for the intended Band-E chiral pair and a separate D/G candidate; these must never be collapsed into “chirality found/not found in 105Ag.” | TI07-5/6 and TI07-10 to TI07-15 | unreviewed |
| AR-2 | Assumptions and dependencies | Band E and D/G configuration claims depend on corrected spins, TRS matching and branching-model inputs; the null result depends on an intensity threshold. | TI07-3 to TI07-8 | unreviewed |
| AR-3 | Transfer conditions | The ≈0.1 sensitivity and DCO calibrations are experiment-specific; the logical distinction between target-pair null search and alternative-pair discovery is transferable. | PDF pp.2,8-9 | unreviewed |
| AR-4 | Failure conditions | A weaker Band-E partner or a quantum calculation showing D/G are ordinary mixed configurations would overturn the respective interpretations without invalidating the observed scheme. | TI07-5/14/15 | unreviewed |
| AR-5 | Reverse/falsification test | Measure D/G lifetimes, mixing ratios and interband matrix elements, and compare chiral PRM versus explicit `g7/2-d5/2` configuration mixing on the same observables. | PDF p.9 | unreviewed |
| AR-6 | Research-question decision | Persist Band E as a null-search reference and D/G as a separate candidate pair; count neither as confirmed chirality. | Full paper | unreviewed |

### Companion Evidence Audit

- Band-E side band above ≈10% relative population: `not-observed`.
- D/G near-degeneracy, links, `S(I)` and ratio similarity: `observed/derived`.
- D/G aplanar geometry: `expected-but-not-established`.
- Band-C triaxial TAC result: `external-model-context` from Ref.35, not a calculation of D/G.
- Octupole correlations from E1 links: `not-established` by the paper's own estimate.

## Knowledge Impact and Learning Decision

- Effect: `supports` a D/G candidate, `limits` Band-E chirality, and `competes-with` via configuration mixing.
- Persistence: create `105Ag`, experiment, Band-E null-search reference and D/G candidate-pair pages; add separate project claims for the null and candidate results.
- Review state: all TI07 and AR claims are unreviewed and outside the paper evidence gate.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[nuclear-chirality-and-multiple-chiral-doublet-bands]] | Adds a low-mass natural-parity candidate pair with explicit alternative. |
| limits | [[chiral-doublet-bands]] | Shows a sensitive null result for the theoretically preferred Band-E configuration. |
| competes-with | [[signature-splitting-mechanisms]] | `g7/2/d5/2` configuration mixing can mimic D/G fingerprints. |

## Human Review Triage

### P0

P0: none identified.

### P1

- **TI07-5/6 and AR-1 — null-result scope.** Confirm that “no chiral partner” remains tied to Band E and ≈0.1 population sensitivity, not the whole nucleus.
- **TI07-10 to TI07-15 — D/G candidate versus mixing.** Confirm that observed fingerprints, author candidate wording, absent dedicated TAC and natural-parity configuration-mixing alternative remain co-visible.
- **TI07-3/4 — corrected Band-E identity.** Verify the `+2ℏ` spin revision and links before later sources reuse Band E.
- **TI07-9 — octupole exclusion.** Keep the assumed `Q0=2 eb` and “insufficient to conclude” wording; do not turn a small E1 estimate into octupole evidence.

### P2/P3

- P2: verify selected A–G spin ranges and model-label crosswalk if reused quantitatively.
- P3: review navigation, aliases and project wording before finalization.

## Sources

- Protected BibTeX record: `timar_2007_Highspinstructure` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2007_Timár et al_High-spin structure of Ag 105.pdf`.
