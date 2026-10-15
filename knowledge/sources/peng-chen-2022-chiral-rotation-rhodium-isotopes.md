---
type: source
title: "Peng and Chen 2022 - Evolution of the chiral rotation mode in rhodium isotopes"
aliases: [Peng Chen 2022 Rh chirality, 102-107Rh 3D-TAC CDFT]
created: 2026-08-11
updated: 2026-10-15
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evolution of the chiral rotation mode in rhodium isotopes"
authors: [J. Peng, Q. B. Chen]
journal: Physical Review C
year: 2022
volume: 105
issue: 4
pages: 044318
doi: 10.1103/PhysRevC.105.044318
language: English
canonical_source: https://doi.org/10.1103/PhysRevC.105.044318
citation_key: peng_2022_Evolutionchiral
raw_file: "raw/papers/2022_Peng_Chen_Evolution of the chiral rotation mode in rhodium isotopes.pdf"
raw_sha256: 96D6A04D4F7DEFC0C68AE62DCC401F3859056C353F219AA55E5F2DDE26C081DF
nuclei: [102rh, 103rh, 104rh, 105rh, 106rh, 107rh]
reactions: []
experiments: []
models: [three-dimensional-tilted-axis-cranking, covariant-density-functional-theory]
observables: [critical-rotational-frequency, orientation-angle, angular-momentum-alignment, moments-of-inertia, bm1-be2-ratio, energy-splitting]
methods: [total-routhian-surface-minimization, configuration-fixed-cranking]
tags: [theory-ingest, project-ingest, a100, nuclear-chirality, planar-to-aplanar, 3d-tac-cdft, rhodium-isotopes]
---

# Evolution of the Chiral Rotation Mode in Rhodium Isotopes

## Bibliographic Record

Physical Review C 105, 044318 (2022), DOI `10.1103/PhysRevC.105.044318`. The protected BibTeX key is `peng_2022_Evolutionchiral`.

## Scope and Reading Depth

- Completed reading depth: `deep-read`.
- Covered scope: all eight PDF pages; 3D-TAC CDFT formalism and inputs; total-Routhian surfaces; orientation angles; critical-frequency systematics; `(gd)`-neutron angular-momentum components; experimental energy/alignment/inertia/ratio comparisons; mean-field and pairing boundaries.
- Not covered: the original experimental papers underlying plotted `102-106Rh` points, source code, numerical convergence files, or beyond-mean-field RPA/collective-Hamiltonian calculations proposed by the authors.
- Coverage caveats: this paper reports no new experiment; plotted side-band energies and electromagnetic data are secondary imports. The mean field cannot calculate doublet splitting, tunnelling or the side-band spectrum.

## Extracted Pages

- PDF pp.1-2: motivation, isotope-chain evidence context, 3D-TAC CDFT equations, PC-PK1/ten-shell/no-pairing setup and configuration scope.
- PDF pp.2-3: configuration fixing, Routhian surfaces, orientation angles and critical frequencies.
- PDF pp.3-5: comparison with `I(ω)` and alignment data; `(gd)`-neutron mechanism for critical-frequency evolution.
- PDF pp.5-6: yrast energies, experimental pair splittings, `B(M1)/B(E2)`, kinematic/dynamic moments and summary.
- PDF pp.7-8: references.

## Paper Question and Scientific Motivation

The paper asks how self-consistent three-dimensional rotation evolves across `102-107Rh`, especially why the calculated onset frequency of aplanar chiral rotation changes as `(gd)` neutrons are added, and whether available experimental systematics are consistent with that mechanism (PDF pp.1-2).

## Method and Design Logic

- Fix one `νh11/2` occupation and trace the `πg9/2^-3⊗ν[h11/2(gd)^n]` configurations, with `n=6-11`, across `102-107Rh` (PDF pp.2-3).
- At each rotational frequency, minimize the self-consistent total Routhian in polar angle `θ` and scan azimuth `φ`; `φ=0` is planar and nonzero paired minima are aplanar (PDF pp.2-3; Figs.1-2).
- Decompose `(gd)`-neutron angular momentum along short/medium/long axes to explain the isotope trend in `ωcrit` (PDF pp.4-5; Fig.5).
- Compare mean-field yrast energies, `I(ω)`, quasiparticle alignment, semiclassical `B(M1)/B(E2)` and finite-difference moments with previously published data (PDF pp.4-6; Figs.3-7).

## Summary

With PC-PK1 3D-TAC CDFT and no pairing, the authors obtain planar-to-aplanar transitions in `103-107Rh` at decreasing critical frequencies `ℏωcrit=0.58, 0.55, 0.49, 0.46, 0.34 MeV`. `102Rh` stays planar through `0.75 MeV`; nonconvergence above that prevents a finite critical value, so static chirality is not supported in the observed range while chiral vibration remains possible. The isotope trend is attributed to added `(gd)` neutrons contributing progressively less incremental short-axis and more medium-axis angular momentum. Model-data agreement is uneven: `I(ω)`, alignment and `J(1)` are better for `103,105,106Rh` and overestimated for even-`(gd)` `102,104Rh`; `B(M1)/B(E2)` is good for `102,103,106Rh` and high for `104Rh`. Because the mean field lacks pairing, tunnelling and chiral vibration, it cannot calculate side bands or partner splitting and cannot by itself validate experimental doublets.

## Experimental or Theoretical Setup

- Point-coupling density functional PC-PK1.
- Three-dimensional harmonic-oscillator basis truncated to ten major shells.
- Pairing neglected; the authors explicitly expect effects on `ωcrit`, total angular momentum and `B(M1)`.
- Configurations `πg9/2^-3⊗ν[h11/2(gd)^n]`, `n=6-11`; two of the three proton holes are antialigned, leaving about `3.5ℏ` along the long axis, while the `νh11/2` particle contributes about `5.5ℏ` along the short axis.
- `θ` is measured from the long axis; `φ` locates the short-medium projection relative to the short axis. Symmetric `±φ` minima represent degenerate intrinsic handed solutions.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PC22-1 | The paper performs no new experiment; all comparisons use data from earlier `102-106Rh` sources, while `107Rh` lacks experimental pair splitting. | source-provenance | direct | PDF pp.1-2,5-6; Figs.3-7 | true |
| PC22-2 | Calculations use PC-PK1, ten oscillator shells and no pairing for `πg9/2^-3⊗ν[h11/2(gd)^n]`, `n=6-11`, across `102-107Rh`. | model-input | direct | PDF pp.2-3, Secs.II-III | true |
| PC22-3 | The total Routhian is minimized in `θ` for each scanned `φ`; planar solutions have a minimum at `φ=0`, while symmetric nonzero minima define aplanar intrinsic solutions. | model-method | direct | PDF pp.2-3; Figs.1-2 | true |
| PC22-4 | Calculated `ℏωcrit` values for `103,104,105,106,107Rh` are `0.58, 0.55, 0.49, 0.46, 0.34 MeV`, respectively. | model-result | direct | PDF p.3; Figs.1-2 | true |
| PC22-5 | `102Rh` remains planar through `ℏω=0.75 MeV`; failure to converge higher means only `ωcrit>0.75 MeV` is suggested, not established. | model-boundary | direct | PDF p.3; Figs.1-2 | true |
| PC22-6 | The authors therefore do not support static chirality in observed `102Rh` spins but do not exclude planar chiral vibration. | author-interpretation | direct | PDF pp.3-4 | true |
| PC22-7 | Experimental `I(ω)` kinks occur near calculated `ωcrit` for `103,104,106Rh`; confirmation is requested for `105,107Rh`. | model-data-comparison | indirect | PDF pp.3-4; Fig.3 | true |
| PC22-8 | The fixed configurations yield continuous, not step-like, calculated alignments, leading the authors to associate `I(ω)` kinks with aplanar onset rather than quasiparticle alignment. | author-interpretation | indirect | PDF p.4; Figs.3-4 | true |
| PC22-9 | The `νh11/2` particle supplies about `5.5ℏ` along the short axis and the effectively unpaired `πg9/2` hole about `3.5ℏ` along the long axis; `(gd)` neutrons control the isotope dependence. | model-result | direct | PDF p.4 | true |
| PC22-10 | With added `(gd)` neutrons, the incremental short-axis component decreases and the medium-axis component grows, making aplanar rotation easier and lowering `ωcrit`. | model-interpretation | direct | PDF pp.4-5; Fig.5 | true |
| PC22-11 | The model reproduces `I(ω)`, alignments and `J(1)` better for `103,105,106Rh` but overestimates `102,104Rh`; omitted pairing is offered as the explanation for the even-`(gd)` cases. | model-boundary | direct | PDF pp.3-6; Figs.3-4,7 | true |
| PC22-12 | Experimental doublet splittings are only displayed, not calculated: `103,104,106Rh` lie near `200-300 keV`, `105Rh` reaches about `650 keV`, and `102Rh` has a minimum near `460 keV`. | secondary-systematics | indirect | PDF p.5; Fig.6(g-k) | true |
| PC22-13 | Mean-field 3D-TAC CDFT cannot calculate the side-band spectrum or doublet splitting because chiral vibration and tunnelling are absent; RPA or a collective Hamiltonian is required. | model-boundary | direct | PDF p.5 | true |
| PC22-14 | Semiclassical `B(M1)/B(E2)` agrees within errors for `102,103,106Rh` but overestimates `104Rh`; pairing is again identified as a needed extension. | model-data-comparison | indirect | PDF pp.5-6; Fig.6(m-r) | true |
| PC22-15 | Experimental `J(2)` oscillations are only partly reproduced by smooth mean-field curves; the authors suggest mixing with normal-deformed bands as one cause. | competing-interpretation | indirect | PDF p.6; Fig.7 | true |
| PC22-16 | Calculated `J(1)` and `J(2)` approach one another above `ωcrit`, but this mean-field trend is not a model-independent experimental signature. | model-result | direct | PDF p.6; Fig.7 | true |
| PC22-17 | Higher/wider Routhian barriers are interpreted as suppressed left-right tunnelling and stronger doublet degeneracy, although tunnelling itself is not calculated in the mean field. | model-interpretation | direct | PDF p.3; Fig.1 | true |
| PC22-18 | The paper's introductory statements that MχD is experimentally verified in `103,105Rh` are literature summaries, not new evidence generated by this calculation. | evidence-boundary | direct | PDF pp.1-2 | true |
| PC22-19 | 原文Eq.(2)取J1=2I/[Eγ(I+1→I)+Eγ(I→I−1)]，Eq.(3)取J2=2/[Eγ(I+1→I)−Eγ(I−1→I−2)]；其后另给ℏωexp为前两相邻γ能量之和的一半。J2分母是跨两条edge的source-specific式，频率标签也按原文保留，不把本任务的edge-pair中点约定归给该图。 | source-finite-difference-convention | direct | PDF p.6 Eqs.(2)–(3) and frequency sentence | true |

### Day14定向公式回查

本轮只回查原raw hash及PDF6的Eqs.(2)–(3)、频率句和相应图示语境，未重新执行全文摄入或模型。PC22-19补足[[moments-of-inertia]]已有source-specific式的直接locator；不改原18条claims/review，也不把本任务Pr136的edge-pair位置或差分结果归到本文图7。

## Nuclear Structure Information

| Nucleus | 3D-TAC CDFT result | Experimental-comparison boundary |
|---|---|---|
| `102Rh` | planar through `0.75 MeV`; possible higher `ωcrit` unresolved | observed range does not support static chirality; vibration not excluded |
| `103Rh` | `ωcrit=0.58 MeV` | experimental kink/ratios broadly supportive; doublet splitting not calculated |
| `104Rh` | `ωcrit=0.55 MeV` | kink is close, but `I`, alignment, `J(1)` and ratios are overestimated without pairing |
| `105Rh` | `ωcrit=0.49 MeV` | `I/alignment/J(1)` broadly reproduced; critical kink awaits experimental confirmation |
| `106Rh` | `ωcrit=0.46 MeV` | kink and ratios broadly reproduced; side-band quantum dynamics absent |
| `107Rh` | `ωcrit=0.34 MeV` | prediction only; no experimental pair splitting in Fig.6 |

## Competing Interpretations and Limitations

- Neglected pairing systematically affects the even-`(gd)` isotopes and may also shift critical frequencies and magnetic strengths.
- Configuration fixing makes a smooth alignment curve expected within the model; it does not experimentally exclude an alignment/mixing origin for every observed kink.
- A mean-field barrier is not a tunnelling calculation. Static-chirality and partner-degeneracy claims require symmetry restoration or a quantum collective model.
- The configuration family treats only one `νh11/2` particle; rhodium candidates based on two `h11/2` neutrons or other configurations are outside the calculation.
- Imported experimental candidates share the original-source uncertainties already recorded on their source and band pages.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The robust new result is a mean-field isotope trend in planar-to-aplanar onset, not new partner bands or calculated doublet spectra. | PC22-1 to PC22-6, PC22-13 | unreviewed |
| AR-2 | Mechanism | The declining `ωcrit` is traced to `(gd)`-neutron angular-momentum redistribution within one fixed configuration family. | PC22-9/10 | unreviewed |
| AR-3 | Model-data gate | Agreement in kinks, ratios and inertias is supportive but nonuniform; `102,104Rh` pairing failures and oscillatory `J(2)` remain visible. | PC22-7/8, PC22-11, PC22-14/15 | unreviewed |
| AR-4 | Reverse test | Pairing-inclusive 3D-TAC plus a quantum collective treatment should predict both onset and the side-band splitting/transition network. | PC22-11/13/17 | unreviewed |
| AR-5 | Transfer condition | Do not transfer the one-`h11/2` isotope trend to two-`h11/2` MχD configurations without a separate calculation. | PC22-2/18 | unreviewed |
| AR-6 | Research decision | Persist `102Rh` as a planar/no-static control, `103-106Rh` as model-tested experimental-candidate contexts, and `107Rh` as a theory-only aplanar prediction. | Full paper | unreviewed |

### Companion Evidence Audit

- New experimental levels or transition strengths: `none`.
- Planar/aplanar minima and `ωcrit`: `self-consistent mean-field results`.
- Experimental kinks, splittings and ratios: `secondary imported data`.
- Side bands, tunnelling and doublet splitting: `outside current mean field`.
- Static chirality in `102Rh`: `not supported in observed range`.

## Knowledge Impact and Learning Decision

- Effect: supplies a common microscopic systematics for `102-107Rh` and a mechanistic `(gd)`-neutron explanation of `ωcrit` evolution.
- Persistence: source; lightweight `102,105,106,107Rh` pages; update `103,104Rh`, TAC/CDFT, static/chiral-vibration concepts and the chirality project. No new band page is created from secondary experimental inputs.
- Review state: all `PC22-*` and AR claims remain unreviewed and outside the paper evidence gate.

## Human Review Triage

### P0

P0: none identified.

### P1

- **PC22-4/5 — critical values.** Keep the five finite values separate from the unconverged `102Rh >0.75-MeV` suggestion.
- **PC22-7/8 — kink semantics.** A fixed-configuration mean-field attribution does not eliminate experimental alignment/mixing alternatives.
- **PC22-11/14 — pairing omission.** Do not call model-data agreement uniform across the chain.
- **PC22-13/17 — mean field versus doublet.** Barrier/aplanar solutions cannot calculate tunnelling, partner splitting or side bands.
- **PC22-18 — evidence provenance.** Do not recount imported Rh candidate data as an independent experiment.

### P2/P3

- P2: cross-check each plotted dataset against Refs.5-11 and 15 before numerical reuse.
- P3: test the isotope trend with pairing-inclusive 3D-TAC and a collective Hamiltonian.

## Related Knowledge and Project Relations

- [[102rh]], [[103rh]], [[104rh]], [[105rh]], [[106rh]], [[107rh]].
- [[tilted-axis-cranking]], [[covariant-density-functional-theory]], [[static-chirality]] and [[chiral-vibration]].
- [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Sources

- Protected BibTeX record: `peng_2022_Evolutionchiral` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2022_Peng_Chen_Evolution of the chiral rotation mode in rhodium isotopes.pdf`.
