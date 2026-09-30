---
type: source
title: "Budaca & Budaca 2025 - Harmonic chiral vibration in triaxial nuclei"
aliases: [Budaca 2025 harmonic chiral vibration, harmonic chiral vibration in triaxial nuclei]
created: 2026-09-30
updated: 2026-09-30
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Harmonic chiral vibration in triaxial nuclei"
authors: [R. Budaca, A. I. Budaca]
journal: Physics Letters B
year: 2025
volume: 868
pages: 139794
doi: 10.1016/j.physletb.2025.139794
arxiv: 2508.00373v1
language: en
canonical_source: "https://doi.org/10.1016/j.physletb.2025.139794"
zotero_item_key: ""
citation_key: ""
zotero_uri: ""
library_file: ""
raw_file: "raw/papers/gpt/day3-mean-field-20260929/2508-00373-harmonic-chiral-vibration/PDFs/Harmonic_chiral_vibration_in_triaxial_nuclei.pdf"
raw_sha256: f6ef887d1be887af7c4b147de8943824e3d9d25acff5116c6ca0e1ba322876fa
nuclei: [103Rh, 105Rh, 107Ag, 133Ce, 135Nd, 137Nd]
reactions: []
experiments: []
models: [particle-rotor-model, harmonic-chiral-vibration, semiclassical-rotor]
observables: [chiral-band-energy-splitting, triaxial-deformation, B(M1)/B(E2)]
methods: [semiclassical-variational-principle, harmonic-oscillator-approximation, rotor-diagonalization]
tags: [triaxiality, chirality, chiral-vibration, particle-rotor, a130, 137nd]
---

# Budaca & Budaca（2025）：三轴核中的谐振手征振动模型

## Bibliographic Record

R. Budaca & A. I. Budaca, “Harmonic chiral vibration in triaxial nuclei,” *Physics Letters B* **868**, 139794 (2025), DOI [`10.1016/j.physletb.2025.139794`](https://doi.org/10.1016/j.physletb.2025.139794), arXiv [`2508.00373v1`](https://arxiv.org/abs/2508.00373). Crossref lists a CC-BY publisher license; the v1 PDF was obtained from [`https://arxiv.org/pdf/2508.00373`](https://arxiv.org/pdf/2508.00373). The local PDF SHA-256 is recorded above. No Zotero/BibTeX citation key was matched, so the key remains blank.

## Scope and Reading Depth

- Completed `reading_depth`: `deep-read`.
- Covered scope: all seven main-text pages; Eqs. (1)–(20); Figs. 1–6; the `137Nd` panel of Fig. 4; transition-ratio comparison and limitations; references [25]–[30] carrying the input band data. Figures 1–6 were visually inspected.
- Not covered: independent re-analysis of the underlying `137Nd` γ-ray data, re-fitting the PRM/HA, or retrieving supplementary material (no relevant SI is listed in the arXiv or article records checked here).
- Coverage caveat: the HA is an approximation around a planar stationary point. Its energy-splitting fit and extracted `γ` are model-conditioned; the `137Nd` input data are reused from Petrache et al. 2020, and this paper does not compare measured `137Nd` `B(M1)/B(E2)` ratios.

## Paper Question and Scientific Motivation

The authors ask whether low-spin chiral-partner energy splittings can be described as a harmonic oscillation of the total angular-momentum vector around a planar equilibrium, and over what range of triaxiality, quasiparticle alignment and spin that approximation remains valid (Abstract; PDF pp. 1–4).

## Method and Design Logic

1. Begin from a triaxial particle-rotor Hamiltonian with two rigidly aligned quasiparticle spins and three principal-axis inertias (Eqs. (1)–(4), PDF pp. 1–2).
2. Use a time-dependent variational principle to obtain a classical energy surface in conjugate variables `(x,φ)`; solve for the planar stationary point and its critical spin `I_c` (Eqs. (6)–(8), PDF pp. 2–3).
3. Expand the surface harmonically around that point and quantize it. The calculated phonon-like frequency `ω_I` is identified with the chiral-partner energy splitting `ΔE(I)` (Eqs. (9)–(11), PDF p. 3).
4. Check the approximation against exact diagonalization and monitor `R_I`, the ratio of quartic to quadratic terms; the HA degrades as `I` approaches `I_c` (Eq. (12), Fig. 2, PDF pp. 3–4).
5. Fit the spin dependence of normalized experimental `ΔE(I)` values to obtain a triaxiality measure, excluding points near zero splitting or with a clear change from monotonic decrease (Fig. 4 and surrounding text, PDF p. 5).

## Key Evidence and Reasoning Chain

- The model's validity is conditional: the planar stationary point must exist and the anharmonicity indicator must remain small; the critical spin marks the harmonic-approximation failure boundary (Eqs. (7)–(12), Figs. 1–2).
- For the `137Nd` panel, the assumed configuration is `πh11/2²⊗νh11/2⁻¹` with `j=11/2`, `j′=10`; Fig. 4 prints a fitted `γ=97.5°` in the paper's extended `60°–120°` convention and compares the calculated energy splitting with experiment (PDF p. 5, Fig. 4f).
- Fig. 4 normalizes `ΔE(I)` to the lowest considered split and says open symbols were excluded. In the `137Nd` panel two filled points are used and a higher-spin open point is omitted; its `γ=97.5°` label shows no `±` uncertainty. The authors describe this as the most triaxial fit, but only a complementary result because `135Nd` has more points (PDF p. 5, Fig. 4 and discussion).
- Under the paper's axis-sector mapping `γ_std=120°−γ`, the fitted `97.5°` maps to `22.5°`. This is a coordinate conversion, not a new measurement.
- Fig. 4 cites Refs. [29]–[30] for the `135Nd/137Nd` experimental energy splittings. Ref. [30] is the existing [[petrache-2020-137nd-multiple-chiral-bands]] study; Budaca & Budaca therefore add a theoretical analysis of the same `137Nd` band data, not another experiment.
- Fig. 5 compares measured and calculated `B(M1)/B(E2)` only for `103Rh` and `105Rh`. The authors note that available `133Ce` and `135Nd` ratios have higher values in the excited band, contrary to their prediction; the paper presents no corresponding measured-ratio test for `137Nd` (PDF p. 6, Fig. 5 and discussion).

## Summary

The paper offers a compact particle-rotor-based harmonic approximation that relates chiral-partner energy splitting to triaxiality and quasiparticle alignment. For the Hara–Sun Table 5 candidate `137Nd (N=77)`, it fits a model triaxiality from a sparse normalized `ΔE(I)` subset. The output is a later same-nucleus triaxial model result, but it is neither a PSM/TPSM recalculation of Hara's old axial-model discrepancy nor independent experimental confirmation of shape. Its `137Nd` data are reused from Petrache et al. 2020; the small number of included energy points, the HA critical-spin limit and absent `137Nd` transition-strength comparison keep the conclusion bounded.

## Experimental or Theoretical Setup

- This is a theory paper and reports no new reaction or detector run.
- It uses published energy splittings from `103,105Rh`, `107Ag`, `133Ce`, `135Nd` and `137Nd`; for `137Nd`, Fig. 4 cites Ref. [30] ([[petrache-2020-137nd-multiple-chiral-bands]]).
- The `137Nd` calculation assumes `πh11/2²⊗νh11/2⁻¹`, with `j=11/2`, `j′=10`; the rotor's `γ` convention spans 60°–120° and is related to the customary sector by symmetry.
- `γ`, empirical normalization and aligned quasiparticle spins are model inputs or fitted quantities. The model is not a self-consistent mean-field shape measurement.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BU25-1 | The HA starts from a particle-rotor Hamiltonian with three axis-dependent inertias and two rigidly aligned quasiparticle angular momenta. | model-definition | direct | Eqs. (1)–(4), PDF pp. 1–2 | true |
| BU25-2 | The planar solution exists below a critical angular momentum `I_c`; above it, the stationary point splits into chiral minima. | model-result | direct | Eqs. (6)–(8), PDF pp. 2–3 | true |
| BU25-3 | The harmonic approximation identifies the partner energy splitting with `ω_I`; `R_I` compares quartic and quadratic terms and grows near the critical spin where HA fails. | model-method/limitation | direct | Eqs. (9)–(12), Fig. 2, PDF pp. 3–4 | true |
| BU25-4 | For `137Nd`, Fig. 4 uses `πh11/2²⊗νh11/2⁻¹`, `j=11/2`, `j′=10`, and prints a fitted `γ=97.5°`. | model-result | direct | Fig. 4f, PDF p. 5 | true |
| BU25-5 | The Fig. 4 `137Nd` `γ` fit is normalized to the lowest selected energy splitting; two filled points are used and a higher-spin open point is excluded. The displayed `γ` has no visible statistical `±` uncertainty. | fit-boundary | direct | Fig. 4 caption and panel f, PDF p. 5 | true |
| BU25-6 | The authors describe `137Nd` as the highest-triaxiality fitted case but only complementary to `135Nd`, which has more data points. | author-interpretation/limitation | direct | Discussion following Fig. 4, PDF p. 5 | true |
| BU25-7 | The `137Nd` experimental energy-splitting data are referenced to Petrache et al. 2020; this paper adds a model calculation, not a second experiment. | source-independence | direct | Fig. 4 caption, Ref. [30], PDF pp. 5, 7 | true |
| BU25-8 | Fig. 5 gives `B(M1)/B(E2)` comparisons for `103Rh/105Rh`; the text reports a model/data contradiction for `133Ce/135Nd`, and presents no `137Nd` measured-ratio comparison. | model-limitation | direct | Fig. 5 and text below, PDF p. 6 | true |

## Nuclear Structure Information

The `137Nd` application is to the `πh11/2²⊗νh11/2⁻¹` partner-band configuration, the same D5/D6 band pair discussed in [[petrache-2020-137nd-multiple-chiral-bands]]. It adds an HA energy-splitting interpretation; it does not add levels, measured transitions, lifetimes or a new experimental dataset.

## Authors' Interpretation

The authors interpret a decreasing normalized `ΔE(I)` trend as a harmonic chiral-vibration signature and use its spin dependence to extract a triaxiality parameter. For `137Nd`, they report the highest fitted triaxiality among their examples, but explicitly treat it as complementary because the available energy-splitting dataset is sparse (PDF p. 5).

## Model Results

- The HA is most reliable for relatively large quasiparticle alignments and moderate triaxiality; Fig. 2 compares its splittings with exact diagonalization and Fig. 3 compares approximate/exact wavefunction distributions for Rh examples.
- `137Nd` fit: paper-convention `γ=97.5°`; converting to the conventional sector with `120°−γ` gives `22.5°`.
- Petrache et al. 2020 report `137Nd` D5/D6 PRM input `γ=23.5°` and constrained-CDFT `γ=29.5°` ([[petrache-2020-137nd-multiple-chiral-bands]] P20-4). The approximately 1° difference between the HA conversion and the PRM input is a same-data, cross-model comparison, not an uncertainty estimate or an independent shape measurement; the parameter conventions and fit objectives differ.

## Competing Interpretations and Limitations

- The extracted `γ` depends on the assumed quasiparticle alignment/configuration, hydrodynamic inertia relation, normalization to the lowest selected splitting and exclusion of points near `ΔE=0` or non-monotonic changes.
- `137Nd` has fewer usable `ΔE` points than `135Nd`; the Fig. 4 fit prints no uncertainty for the `137Nd` parameter and does not test its prediction against measured `B(M1)/B(E2)` ratios.
- The Figure 4 band data are reused from Petrache et al. 2020; the model paper is not an independent experimental confirmation.
- The HA collapses near `I_c` as the quartic correction increases. Do not extrapolate the low-spin harmonic assignment through the critical-spin regime.
- The authors' statement that this is the highest-triaxiality case is a model fit, not a direct measurement of nuclear shape.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| BU25-AR-1 | Hara transfer | The later `137Nd` application gives a triaxial model fit to D5/D6 energy splittings, but is not a projected-shell-model test of Hara's original axial PSM mismatch and does not independently establish shape. | HARA95 HS10-4; BU25-4–BU25-7; P20-1/P20-4 | unreviewed |
| BU25-AR-2 | Cross-model parameter check | `γ=97.5°` maps to `22.5°` in the conventional sector, near P20's D5/D6 PRM input `23.5°`; the apparent proximity shares P20's energy data and is not a second measurement or a calibrated uncertainty. | BU25-4/BU25-7; P20-4 | unreviewed |
| BU25-AR-3 | Falsifier/companion | Same-spin lifetimes and measured `B(M1)/B(E2)` for `137Nd` D5/D6 would test the model's electromagnetic predictions; no such comparison for `137Nd` is presented here. | BU25-8; P20-5 | unreviewed |
| BU25-AR-4 | Critical-spin consistency check | Using Eq. (2) with printed `γ=97.5°`, `j=11/2`, `j′=10`, the Eq. (7) planar critical spin is `I_c≈17.804ℏ`; after normalizing the Fig. 4f `137Nd` points to `I_0=16.5ℏ`, the filled `I=17.5ℏ` point lies below this model boundary while the open `I=18.5ℏ` point lies above it and is excluded. The agreement is a consistency check of the HA fit selection, not a measurement of `I_c` or `γ`. | Eqs. (2), (7); Fig. 4f and caption, PDF pp. 1–2, 5 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Hara Table 5 marks `137Nd (N=77)` “presumably triaxial”; P20 models D2/D3 and D5/D6 with CDFT/PRM and notes that weak D3/D6 lack measured `B(M1)/B(E2)`.
- Effect of this source: **revises** the same-nucleus theory-coverage map and **limits** interpreting a fitted `γ` as independent shape evidence.
- Reason: this later HA paper fits the low-spin D5/D6 energy-splitting trend from the P20 dataset, but does not test Hara's old axial PSM sequence, has sparse `137Nd` points, and lacks its own measured-strength comparison.
- Persistence decision: update the A≈130 model-choice card and triaxial particle-rotor model page; preserve the P20 shared-data lineage.
- Review state: source page remains `unreviewed`; all new claims retain `needs_review: true`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[triaxial-particle-rotor-model]] | Semiclassical HA derived from a constrained PRM Hamiltonian with explicit critical-spin and anharmonicity limits. |
| competing-interpretation | [[petrache-2020-137nd-multiple-chiral-bands]] | Reuses the `137Nd` D5/D6 energy-splitting data while applying a distinct chiral-vibration model. |
| retrospective-connection | [[hara-sun-1995-projected-shell-model-high-spin]] | Same `137Nd (N=77)` Table 5 candidate, but no direct projected-shell-model reanalysis of the 1995 calculation. |
| not-direct-evidence | [[131ce-collective-mode-discrimination]] | `137Nd` fitted parameters do not supply `131Ce (N=73)` observations. |

## Human Review Triage

### P0

P0: none identified.

### P1

- `BU25-4`–`BU25-7`, Fig. 4: keep the extended γ convention, open-point exclusions, sparse `137Nd` data and P20 reference lineage attached to any reuse.
- `BU25-8`, Fig. 5/text: do not generalize the Rh transition-ratio comparison or the `133Ce/135Nd` mismatch into a measured `137Nd` result.

### P2/P3

- Citation key was not verified against the protected Zotero BibTeX input and remains blank.
- No new experimental dataset or event-level reanalysis is included.

## Extracted Pages

- Nuclei: [[137nd]], [[133ce]], [[135nd]], [[103rh]], [[105rh]]
- Models: [[triaxial-particle-rotor-model]]
- Sources: [[petrache-2020-137nd-multiple-chiral-bands]]
- Concepts: [[chiral-doublet-bands]], [[chiral-vibration]], [[triaxial-deformation]]

## Non-source Notes and Follow-up

For Hara Table 5 coverage, distinguish the 2024 TPSM calculations for `133La`/`135Pr` from this 2025 PRM-derived HA fit to `137Nd` D5/D6. Both are model analyses of existing data; neither adds a shape measurement or a new experiment.
