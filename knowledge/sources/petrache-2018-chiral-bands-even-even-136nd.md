---
type: source
title: "Petrache et al. 2018 - Evidence of chiral bands in even-even nuclei"
aliases: [Petrache 2018 136Nd, even-even chirality in 136Nd]
created: 2026-08-11
updated: 2026-09-20
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evidence of Chiral Bands in Even-Even Nuclei"
authors: [C. M. Petrache, B. F. Lv, A. Astier, E. Dupont, Y. K. Wang, S. Q. Zhang, P. W. Zhao, Z. X. Ren, J. Meng, P. T. Greenlees, H. Badran, D. M. Cox, T. Grahn, R. Julin, S. Juutinen, J. Konki, J. Pakarinen, P. Papadakis, J. Partanen, P. Rahkila, M. Sandzelius, J. Saren, C. Scholey, J. Sorri, S. Stolze, J. Uusitalo, B. Cederwall, Ö. Aktas, A. Ertoprak, H. Liu, S. Matta, P. Subramaniam, S. Guo, M. L. Liu, X. H. Zhou, K. L. Wang, I. Kuti, J. Timár, A. Tucholski, J. Srebrny, C. Andreoiu]
journal: Physical Review C
year: 2018
volume: 97
pages: 041304(R)
doi: 10.1103/PhysRevC.97.041304
language: English
canonical_source: https://doi.org/10.1103/PhysRevC.97.041304
citation_key: petrache_2018_Evidencechiral
raw_file: "raw/papers/2018_Petrache et al_Evidence of chiral bands in even-even nuclei.pdf"
raw_sha256: D2615FC0D95428B06C056EB8946AFA2F62940CE58D79C1FC1CC3F50E19C73EF3
additional_raw_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2018_Petrache et al_Evidence of chiral bands in even-even nuclei.pdf"
additional_raw_sha256: "1a67acb9a4088f03260d097e98c7cfb8c0bcd69ee79d74b3dd7df93343743697"
supplementary_raw_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2018_Petrache et al_Evidence of chiral bands in even-even nuclei.pdf"
supplementary_raw_sha256: "1a67acb9a4088f03260d097e98c7cfb8c0bcd69ee79d74b3dd7df93343743697"
published_version_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/实验/2018_Petrache et al_Evidence of chiral bands in even-even nuclei.pdf"
published_version_sha256: "5e6f1c01501598b5cf765d838d86a2b37a4fcf252039ba9058e631ccc7517f81"
nuclei: [136nd]
reactions: ["100Mo(40Ar,4n)136Nd"]
experiments: [jyfl-jurogam2-136nd-ar40-152mev]
models: [constrained-covariant-density-functional-theory, tac-cdft, three-dimensional-tac-cdft, many-quasiparticle-particle-rotor-model]
observables: [dco-ratio, two-point-angular-correlation-ratio, linear-polarization-asymmetry, bm1-be2-ratio, angular-momentum-alignment]
methods: [gamma-gamma-coincidence, angular-distribution, dco-ratio, two-point-angular-correlation-ratio, linear-polarization-asymmetry, tilted-axis-cranking]
tags: [experiment-ingest, project-ingest, a130, even-even, nuclear-chirality, multiple-chiral-doublet-bands]
---

# Evidence of Chiral Bands in Even-Even Nuclei

## Bibliographic Record

Physical Review C 97, 041304(R) (2018), DOI `10.1103/PhysRevC.97.041304`. The protected BibTeX key is `petrache_2018_Evidencechiral`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`.
- Covered scope: repository cover plus all six journal pages; experiment, partial level scheme, five doublet pairs, relative populations, DCO/`R_ac`/angular-distribution/polarization basis, experimental and calculated `B(M1)/B(E2)`, constrained/TAC-CDFT configuration mapping and the D3 3D-TAC example.
- Not covered: the promised full level scheme/angular-correlation paper, raw matrices, numerical transition table, the earlier disputed `136Nd` lifetime paper, or any later MQ-PRM calculation in full.
- Coverage caveats: many in-band dipoles are unobserved; four weak partner bands lack measured `B(M1)/B(E2)`; 3D TAC-CDFT is shown only for D3; details of the summary's MQ-PRM statement are not presented in the body.
- 2026 full-source reuse audit: the HS-012 electronic reprint is a distinct byte version of the same DOI/article. Its title page, abstract, six journal pages, figures, Table I and conclusions were reread; no material claim change was found relative to this source page. The new copy is linked as an additional raw artifact, not a new experiment or source.
- 2026 supplementary audit: the HS-012 PDF includes the electronic reprint and the article's detailed Table I/figures; the tabulated `Eγ`, intensities, `R_ADO`, polarization, `δ`, `B(M1)` and `B(E2)` rows for Bands 1-3 and interband decays were read. Upper limits for the missing high-energy band-2→band-1 E2 links remain explicit, and the material is attached evidence for this parent source, not an independent experiment.
- HS-053 published PRC PDF audit (2026-09-20): the six-page article was reread end-to-end; its five-pair `136Nd` scheme, DCO/`R_ac`/polarization limits, D5 partner-ratio evidence and TAC/CDFT caveats agree with this page. No material claim change; the published PDF is a same-experiment version, not an independent source.

## Extracted Pages

- PDF p.1: repository cover and bibliographic metadata.
- PDF pp.2-3 / journal pp.1-2: motivation, experiment, five-pair level scheme and electromagnetic-analysis basis.
- PDF p.4 / journal p.3: D2-C coincidence evidence, experimental ratios and model setup.
- PDF p.5 / journal p.4: configuration table, alignment/energy/ratio comparisons and model discrepancies.
- PDF p.6 / journal p.5: D3 3D-TAC azimuth angle and calibrated conclusion.
- PDF p.7 / journal p.6: references.

## Paper Question and Scientific Motivation

The paper asks whether an even-even nucleus can realize chirality through multiquasiparticle configurations containing angular-momentum-carrying particles and holes along perpendicular axes. It searches for several such doublets in `136Nd` and tests their triaxial configurations and rotational response with CDFT/TAC calculations.

## Method and Design Logic

- Very-high-statistics 3D/4D JUROGAM II coincidences establish weak partner bands and links to yrast sequences.
- DCO, `R_ac`, angular distributions and polarization support spin/parity assignments, although detailed analysis is deferred.
- Same-spin energy proximity, pair links, alignments and, when available, branching-derived `B(M1)/B(E2)` compare the partners.
- Constrained CDFT supplies candidate configurations/deformations; TAC-CDFT maps alignment, energy and ratios. A 3D TAC-CDFT calculation tests aplanar rotation for D3 only.

## Summary

Five nearly degenerate pairs are identified: D1/D1-C, D2/D2-C, D3/D3-C, D4/D4-C and D5/D5-chiral. D5 is the strongest pair and the only one with measured `B(M1)/B(E2)` in both partners, nearly identical within errors; it is therefore the paper's clearest even-even chiral pair. The other four weak partners remain candidates without partner-resolved ratio data. CDFT/TAC assigns configurations A, B, D*, D and C respectively. Only the D3/D* example receives an explicit 3D aplanar solution above `ħω≈0.5 MeV`; extending that geometry to all pairs is a model-family inference, not a calculation shown pair by pair.

## Experimental or Theoretical Setup

- `100Mo(40Ar,4n)136Nd`, `152 MeV`, K130 Cyclotron, University of Jyväskylä.
- Self-supporting enriched `100Mo`, `0.5 mg/cm²`; `135Nd` and `136Nd` each about `100 mb` within a total `480 mb` cross section.
- JUROGAM II efficiency about `4.3%` at `1.3 MeV`; `5.1×10^10` prompt three-fold-and-higher events.
- GRAIN sorting; RADWARE analysis of fully symmetrized 3D and 4D matrices.
- PC-PK1 CDFT in 10 major Cartesian harmonic-oscillator shells; Harris `J0=11 ħ²/MeV`, `J1=20 ħ⁴/MeV³` for alignments.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE18-1 | The experiment accumulated `5.1×10^10` prompt three-fold-and-higher JUROGAM II events following `100Mo(40Ar,4n)` at `152 MeV`. | experimental-fact | direct | PDF p.3 / journal p.2 | true |
| PE18-2 | Five linked nearly degenerate pairs are identified in the partial `136Nd` scheme: D1/D1-C, D2/D2-C, D3/D3-C, D4/D4-C and D5/D5-chiral. | experimental-fact | direct | PDF pp.3-4; Figs.1-2 | true |
| PE18-3 | Spin/parity assignments combine DCO, `R_ac`, angular distributions and polarization, but the detailed angular-correlation analysis is deferred to a forthcoming paper. | evidence-boundary | direct | PDF p.3 / journal p.2 | true |
| PE18-4 | Weak partners decay through high-energy quadrupole links that can dominate low-energy in-band dipoles by factors of `10–20`; many in-band dipoles are therefore unobserved. | experimental-fact | direct | PDF p.3 / journal p.2 | true |
| PE18-5 | D5/D5-chiral is the strongest pair and has nearly identical experimental `B(M1)/B(E2)` in both partners over the observed spin range. | derived-observable | direct | PDF pp.3-4; Figs.1,3 | true |
| PE18-6 | The other four partner bands are weakly populated and have no measured partner-resolved `B(M1)/B(E2)` values. | evidence-boundary | direct | PDF p.6 / journal p.5; Summary | true |
| PE18-7 | D1/D1-C, D2/D2-C, D5/D5-C, D3/D3-C and D4/D4-C are assigned configurations A, B, C, D* and D, respectively, through constrained/TAC-CDFT alignment and energy comparisons. | model-result | indirect | PDF p.5 / journal p.4; Table I; Figs.4-5 | true |
| PE18-8 | The statement that D1-C shares D1's intrinsic state follows from the absence of another calculated configuration reproducing D1-C; this is an exclusion within the tested model space, not a direct configuration measurement. | model-boundary | direct | PDF p.5 / journal p.4 | true |
| PE18-9 | D2, D3 and D4 show backbends attributed to possible 8-, 6- and 6-qp crossings beyond the current TAC-CDFT calculation. | author-interpretation | indirect | PDF p.5 / journal p.4 | true |
| PE18-10 | Calculations underestimate absolute ratios for D1/D2 but reproduce their relative differences; D3/D4 ratio increases near backbend are not reproduced; configuration C agrees with D5 over the observed range. | model-discrepancy | direct | PDF p.5 / journal p.4; Fig.3 | true |
| PE18-11 | For D3's D* configuration, 3D TAC gives planar `φ=0` below and nonzero `φ` above the critical `ħω≈0.5 MeV`, providing an explicit aplanar solution. | model-result | indirect | PDF p.6 / journal p.5; Fig.6 | true |
| PE18-12 | The paper does not show 3D TAC calculations for the other four pairs; their chiral geometry is inferred from assigned triaxial configurations and TAC systematics. | model-boundary | direct | PDF pp.4-6 | true |
| PE18-13 | Pairing is neglected after a configuration-A test at `ħω=0.2 MeV` changes total energy by `<0.005%` and angular momentum by `4.5%`; transfer to every configuration/frequency is an assumption. | model-assumption | direct | PDF p.4 / journal p.3 | true |
| PE18-14 | The paper concludes one clear even-even chiral pair and four weaker candidates contributing to possible MχD, while further calculations of realized geometry remain in progress. | author-interpretation | direct | Abstract; PDF p.6 / journal p.5 | true |
| PE18-15 | MQ-PRM is named in the summary, but no inputs, equations or results for it are documented in the article body. | source-completeness-boundary | direct | PDF p.6 / journal p.5 versus full body | true |

## Nuclear Structure Information

| Pair | Assigned configuration | Experimental/model status |
|---|---|---|
| D1/D1-C | A, positive, `β=0.21 γ=21°` | good candidate; D1 alignment/energy reproduced, D1-C same-intrinsic inference is model-space exclusion; ratios not both measured |
| D2/D2-C | B, positive, `β=0.22 γ=19°` | weak candidate; backbend and absolute ratio mismatch beyond current fixed configuration |
| D5/D5-chiral | C, positive, `β=0.26 γ=23°` | clearest pair; both experimental ratios nearly identical and calculated trend agrees |
| D3/D3-C | D*, negative, `β=0.21 γ=22°` | weak candidate; only pair with explicit 3D TAC planar-to-aplanar solution; backbend ratio not reproduced |
| D4/D4-C | D, negative, `β=0.22 γ=19°` | weak candidate; backbend ratio not reproduced; no partner-resolved ratios |

## Competing Interpretations and Limitations

- Near degeneracy plus common model assignment does not uniquely exclude configuration mixing or crossings.
- Earlier `136Nd` four-qp chiral interpretation was questioned by unequal reduced transition probabilities; the present paper's strongest response is D5 partner-ratio similarity, not a general resolution for every pair.
- Missing weak in-band dipoles and partner ratios limit four candidate pairs.
- Fixed-configuration TAC omits the crossings invoked for D2/D3/D4.
- Aplanar geometry is demonstrated for one assigned configuration only and mean-field TAC does not quantize left/right tunnelling.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The durable advance is one electromagnetic-strengthened even-even pair plus a four-pair candidate envelope, not five equally established pairs. | PE18-2, PE18-5/6, PE18-14 | unreviewed |
| AR-2 | Assumptions | Pair identities depend on weak transition visibility, model-space configuration exclusions and fixed-configuration TAC. | PE18-3/4, PE18-7 to PE18-10 | unreviewed |
| AR-3 | Geometry scope | D3 demonstrates aplanar mean-field rotation; it is supporting precedent for, not direct geometry calculation of, D1/D2/D4/D5. | PE18-11/12 | unreviewed |
| AR-4 | Failure condition | Partner-resolved lifetimes or configuration-mixing calculations that separate the pair members would reduce the MχD interpretation while retaining the level scheme. | Full paper | unreviewed |
| AR-5 | Reverse test | Measure absolute strengths/mixing ratios for all weak partners and perform pair-specific 3D dynamical calculations including crossings and configuration mixing. | PE18-6, PE18-9/10/12 | unreviewed |
| AR-6 | Research decision | Store D5 separately as the clearest candidate and D1-D4 as four individual weaker candidates; retain the full five-pair MχD claim at author-interpretation level. | Full paper | unreviewed |

## Knowledge Impact and Learning Decision

- Effect: `supports` even-even nuclear chirality and a five-pair MχD candidate census, while `limits` confirmation to one experimentally strengthened pair.
- Persistence: source, experiment and five pair pages; update `136Nd`, MχD concept and chirality project.
- Review state: all `PE18-*` and AR claims remain unreviewed and outside the paper evidence gate.

## Human Review Triage

### P0

P0: none identified.

### P1

- **PE18-5/6/14 — confidence gradient.** Preserve D5 as the one clear pair and the other four as candidates lacking partner ratios.
- **PE18-7/8 — configuration logic.** “No other calculated configuration” is model-space exclusion, not direct proof of one intrinsic state.
- **PE18-9/10 — crossing failures.** Keep backbend/ratio discrepancies visible.
- **PE18-11/12 — geometry scope.** Do not copy D3's 3D aplanar result to all five pairs.
- **PE18-15 — MQ-PRM completeness.** Do not cite undocumented summary wording as a reproducible calculation.

## Related Knowledge and Project Relations

- [[136nd]], [[136nd-d5-chiral-doublet]], [[136nd-d1-chiral-doublet-candidate]], [[136nd-d2-chiral-doublet-candidate]], [[136nd-d3-chiral-doublet-candidate]], [[136nd-d4-chiral-doublet-candidate]].
- [[jyfl-jurogam2-136nd-ar40-152mev]].
- [[multiple-chiral-doublet-bands]], [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Sources

- Protected BibTeX record: `petrache_2018_Evidencechiral` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2018_Petrache et al_Evidence of chiral bands in even-even nuclei.pdf`.
