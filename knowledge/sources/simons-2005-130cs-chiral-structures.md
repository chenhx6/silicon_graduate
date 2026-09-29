---
type: source
title: "Simons et al. 2005 - Evidence for chiral structures in 130Cs"
aliases: ["Simons 2005 130Cs chiral bands", "130Cs Euroball chiral candidate experiment"]
created: 2026-09-29
updated: 2026-09-29
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "Evidence for chiral structures in 130Cs"
authors: ["A. J. Simons", "P. Joshi", "D. G. Jenkins", "P. M. Raddon", "R. Wadsworth", "D. B. Fossan", "T. Koike", "C. Vaman", "K. Starosta", "E. S. Paul", "H. J. Chantler", "A. O. Evans", "P. Bednarczyk", "D. Curien"]
journal: "Journal of Physics G: Nuclear and Particle Physics"
year: 2005
volume: 31
issue: 7
pages: "541-552"
doi: "10.1088/0954-3899/31/7/001"
language: en
canonical_source: "A. J. Simons et al., J. Phys. G: Nucl. Part. Phys. 31 (2005) 541-552, doi:10.1088/0954-3899/31/7/001."
citation_key:
library_file: "raw/papers/gpt/day3-mean-field-20260929/simons-2005-130cs-chiral-structures.pdf"
raw_file: "raw/papers/gpt/day3-mean-field-20260929/simons-2005-130cs-chiral-structures.pdf"
raw_sha256: "da71d9f1c88421bc7d4421c87c4f1eb3f15043892a1ae821c62ab48cd5a611d6"
nuclei: [130cs]
reactions: ["124Sn(11B,5n)130Cs"]
experiments: ["Euroball IV 130Cs in-beam spectroscopy"]
models: ["core-quasiparticle-coupling-model", "cranked-Nilsson-Woods-Saxon"]
observables: ["band-energies", "gamma-ray-intensities", "RDCO", "linear-polarization", "B(M1)/B(E2)", "B(M1)in/B(M1)out", "S(I)"]
methods: ["gamma-gamma-gamma-coincidence", "directional-correlation", "Clover-Compton-polarimetry", "relative-transition-strength-ratios"]
tags: [a130, chiral-doublet-candidate, Euroball, odd-odd, polarization, lifetime-gap]
---

# Evidence for chiral structures in 130Cs

## Bibliographic Record

- A. J. Simons et al., *Journal of Physics G: Nuclear and Particle Physics* **31**(7), 541–552 (2005), DOI [`10.1088/0954-3899/31/7/001`](https://doi.org/10.1088/0954-3899/31/7/001).
- Open IOP PDF: [`https://iopscience.iop.org/article/10.1088/0954-3899/31/7/001/pdf`](https://iopscience.iop.org/article/10.1088/0954-3899/31/7/001/pdf). Crossref and OpenAlex confirm title/DOI/volume/pages; the publisher PDF was downloaded directly as OA with SI disabled.
- Local PDF: `raw/papers/gpt/day3-mean-field-20260929/simons-2005-130cs-chiral-structures.pdf`; 239,000 bytes; SHA-256 `da71d9f1c88421bc7d4421c87c4f1eb3f15043892a1ae821c62ab48cd5a611d6`.
- Local protected BibTeX search found no unique matching item; no citation key was inferred or added.

## Scope and Reading Depth

- Completed `deep-read` of the 13-page PDF (journal pp.541–552 plus IOP cover): abstract/introduction, reaction and Euroball setup, DCO/polarization equations, Tables 1–2, partial level scheme Fig.1, coincidence spectra Figs.2–3, energy/staggering Figs.4–5, transition-ratio Figs.6–7, discussion and conclusion. Tables 1–2, Fig.1 and Figs.6–7 were visually checked.
- Not covered: raw event data, the primary datasets cited by Bhat et al. Ref. [18] for `126Cs`, and the model-code inputs beyond parameters stated in the article.
- Scope boundary: this is a direct `130Cs` experiment. Its band labels, triaxial-core interpretation and electromagnetic ratios do not transfer to `131Ce` or to a different isotope without new evidence.

## Paper Question and Scientific Motivation

The authors extend the positive-parity `130Cs` doublet candidate and test it against three proposed chiral signatures: near-degenerate partner energies, smooth `S(I)`, and phase/staggering behavior of intraband/interband magnetic transition ratios (Abstract; Introduction; PDF pp.2–3).

## Method and Design Logic

- Reaction: `124Sn(11B,5n)130Cs` at 60 MeV, with a 2.2 mg/cm² `124Sn` target backed by 12 mg/cm² natural Pb. Euroball IV used 30 tapered, 26 Clover and 15 Cluster detectors plus a 210-element BGO inner ball; the selected event sample contained about `2×10^8` triple coincidences (Experimental method, PDF p.3).
- DCO ratios use `R_DCO = Iγ(90° gate,156°)/Iγ(156° gate,90°)`; the paper gives geometry-specific reference values for stretched transitions (Eq. (2), PDF p.3).
- Clover Compton polarimetry uses `P=(1/Q)(N⊥−N∥)/(N⊥+N∥)`; `Q` sensitivity is taken from a cited calibration paper. Positive/negative polarization signs are interpreted as stretched E/M character (Eq. (3), PDF p.3).
- Tables 1–2 report `Eγ`, relative intensity normalized to the 151-keV transition, multipolarity, DCO and linear polarization where measured. `B(M1)/B(E2)` and `B(M1)in/B(M1)out` are transition-ratio observables; the paper does not report state lifetimes or absolute transition strengths for `130Cs`.

## Key Evidence and Reasoning Chain

1. The Euroball data confirm and extend bands A and B, add transitions, and produce a partial level scheme (Tables 1–2, Fig.1; journal pp.544–546 / PDF pp.5–7).
2. DCO and linear polarization were measured for four interband links at 297, 547, 596 and 609 keV. The authors report predominantly magnetic-dipole links and use them to establish the same parity for the two bands; with band A's prior configuration assignment, they infer a common `πh11/2 ⊗ νh11/2⁻¹` configuration (Tables 1–2 and text, journal p.545 / PDF p.6).
3. Same-spin energy differences shrink toward mid-spin; the article describes the bands as closest near `I≈15` with roughly 160-keV residual separation. The apparent closest approach at `I=17` may be affected by a structural change in band A (Fig.4 and discussion, journal pp.548, 551 / PDF pp.9, 12).
4. The measured `S(I)` is approximately smooth above `I≈12`. Fig.6 reports moderate odd/even staggering in several derived ratios, but the `B(M1)/B(E2)` ratio for band B lacks the same staggering; calculated staggering amplitudes are sometimes too large (Figs.5–6, journal pp.548–549 / PDF pp.9–10).
5. Fig.7 gives the ratio `[B(M1)/B(E2)]A/[B(M1)/B(E2)]B`: excluding the spin-13 point, values lie between about 0.3 and 1. The authors regard the total pattern as broadly consistent with chirality up to about spin 16, while noting a finite partner-band splitting and unresolved ratio behavior (Fig.7 and discussion, journal p.550 / PDF p.11).
6. Near `I≈16–17`, the yrast band shows a crossing-like change. Cranked Woods–Saxon calculations attribute it to an aligned `h11/2` neutron pair around `ℏω≈0.45 MeV`; the proposed alignment would planarize the angular-momentum geometry and end the chiral regime (discussion, journal p.551 / PDF p.12). This mechanism is an author/model interpretation, not a directly measured orbital alignment.

## Summary

The direct experiment establishes the extended `130Cs` band structure, angular-correlation/polarization information for linking transitions, near-degenerate same-parity partner sequences and transition-ratio trends. The authors interpret the combined pattern as consistent with chiral rotation over a limited spin range, with a high-spin crossing likely ending it. The evidence does not include `130Cs` lifetimes or absolute `B(E2)/B(M1)`; the authors explicitly identify lifetimes as the next measurement. It is a useful A≈130 experimental control for the TPSM calculation by Bhat et al. 2014, but that theory paper reuses this experiment's ratio data and is not an independent dataset.

## Experimental or Theoretical Setup

- Beam/target/reaction: 60-MeV `11B` on `124Sn`, `124Sn(11B,5n)130Cs`.
- Array: Euroball IV, with Clover Compton polarimetry, DCO angular-correlation matrices and triple-coincidence sorting.
- Direct observables: transition energies and relative intensities, angular-correlation ratios, selected polarization values and coincidence/linking topology.
- Derived observables: `S(I)`, `B(M1)/B(E2)` and `B(M1)in/B(M1)out` ratios; these do not supply absolute transition strengths without lifetimes.
- Model comparison: a core–quasiparticle coupling calculation assumes `γ=27.6°`, `β₂=0.185`; cranked Nilsson–Woods–Saxon calculations discuss the high-spin crossing (PDF pp.7, 12).

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SIM05-1 | `130Cs` was populated by `124Sn(11B,5n)` at 60 MeV and measured with Euroball IV; approximately `2×10^8` triple coincidences were sorted. | observed-fact / experimental-setup | direct | Experimental method, PDF p.3 | true |
| SIM05-2 | Bands A and B were confirmed/extended with new transitions; Table 1–2 and Fig.1 provide the measured scheme and relative gamma intensities. | observed-fact | direct | Tables 1–2, Fig.1; PDF pp.5–7 | true |
| SIM05-3 | Four interband links (297, 547, 596, 609 keV) have DCO/polarization information and are reported as predominantly M1. | observed-fact / experimental-assignment | direct | Tables 1–2 and text, PDF pp.5–6 | true |
| SIM05-4 | The authors infer that A/B have the same parity and common configuration, using link multipolarity/polarization together with band A's prior assignment. | author-interpretation | direct | Discussion of Tables 1–2, PDF p.6 | true |
| SIM05-5 | `S(I)` is approximately smooth above spin 12; transition ratios show mixed signatures, including no clear `B(M1)/B(E2)` staggering in band B and imperfect theory-amplitude agreement. | derived-observable / model-comparison | direct | Figs.5–6, PDF pp.9–10 | true |
| SIM05-6 | The bands remain separated by roughly 160 keV at mid-spin; the authors assign the `I≈16–17` crossing and possible `h11/2` neutron-pair alignment to loss of chiral geometry. | observed-fact / author-interpretation | direct | Fig.4 and discussion, PDF pp.9, 12 | true |
| SIM05-7 | No `130Cs` lifetime/absolute strength is reported; the authors call for lifetimes as the next key measurement. | evidence-boundary | direct | Conclusion, PDF p.12 | true |

## Nuclear Structure Information

- Bands A and B are positive-parity sequences; this work uses interband multipolarity/polarization to support common parity and a shared configuration. Band identifiers are paper-local and should not be merged with other `130Cs` work without level/transition crosswalk.
- The proposed chiral regime is limited to roughly `I≤16`; the high-spin band-A crossing is treated as a competing configuration/alignment change.
- The paper reports no direct triaxial-shape measurement. The `γ=27.6°` core value belongs to the core–quasiparticle model; the high-spin alignment is from a cranked Woods–Saxon calculation.

## Authors' Interpretation

- The authors conclude that A/B are broadly consistent with chiral partner bands up to spin `~16`, but their finite energy splitting may indicate chiral vibration/tunnelling rather than fully static chirality.
- At higher spin they attribute the band crossing to an aligned neutron pair that restores a planar angular-momentum geometry.

## Model Results

- Core–quasiparticle calculations reproduce broad trends but overpredict some staggering amplitudes and do not match all local details.
- Cranked Woods–Saxon results assign the high-spin crossing to `h11/2` neutron alignment at about `0.45 MeV`; this is not a directly measured orbital occupation.
- The model's `γ=27.6°` and `β₂=0.185` are fit/input values, not independent shape observables.

## Competing Interpretations and Limitations

- Near-degenerate energies alone do not establish chirality. The finite `~160-keV` mid-spin splitting and inferred smooth `S(I)` are compatible with chiral vibration/tunnelling in the authors' account.
- The experiment supports the same-parity/common-configuration assignment through DCO/polarization, but the chiral interpretation is inferred from several trends; band B's measured `B(M1)/B(E2)` lacks clear staggering, and calculated amplitudes differ from data.
- No lifetimes or absolute transition strengths are available for `130Cs`; ratio-only agreement cannot supply the missing absolute-strength comparison.
- The `130Cs` ratio data are the same dataset reused as Ref. [32] by Bhat et al. 2014. Count one Euroball experiment, not two independent confirmations.
- Adjacent `130Cs` evidence is not evidence about `131Ce`; the latter requires its own links, polarization, lifetime and absolute strengths.

## Analytical Reconstruction

| ID | Audit item | Agent assessment | Evidence / locator | Status |
|---|---|---|---|---|
| AR-SIM05-1 | Core reconstruction | Direct spectroscopy and link properties support the band map and same-parity assignment; chirality remains a multi-observable author interpretation. | Tables 1–2, Fig.1, PDF pp.5–7 | self-checking |
| AR-SIM05-2 | Assumptions and dependencies | Ratio interpretation depends on transition assignment, relative intensity, mixing/multipolarity and the Clover polarization sensitivity calibration; no absolute lifetime scale is available. | Eq. (2)–(3), Tables 1–2, PDF pp.3–6 | self-checking |
| AR-SIM05-3 | Transfer conditions | This is a `130Cs` mechanism/observable control only; do not transfer band labels, `γ`, polarization or ratios to `131Ce`. | SIM05-1–7 | provisional |
| AR-SIM05-4 | Failure condition | Missing lifetime/absolute strengths and the band-B ratio pattern limit static-chirality inference; high-spin crossing changes the configuration context. | Figs.5–7, Conclusion, PDF pp.9–12 | active-L3 |
| AR-SIM05-5 | Reverse test | Measure partner-resolved lifetimes and absolute `B(E2)/B(M1)` across the candidate spin range, and test the crossing identity with independent configuration-sensitive observables. | Conclusion p.12; crossing discussion p.12 | candidate-L3 |
| AR-SIM05-6 | Research-question decision | Link as the primary experiment underlying Bhat Ref. [32]; retain shared-dataset dependence and do not count their TPSM comparison as a new experiment. | Reference list p.13; Bhat BHA14-4 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Bhat et al. 2014 TPSM predicts `130Cs` absolute strengths and compares to measured ratios, but the experiment lineage for those ratios was not previously resolved in this run.
- Effect: `supports` the primary-origin mapping for the `130Cs` ratio data and `limits` the TPSM result's independence; it adds no `131Ce` evidence.
- Reason: Simons et al. is the referenced Euroball data paper (Bhat Ref. [32]); it reports direct level/link/DCO/polarization information and derived ratios, but not `130Cs` lifetimes or absolute strengths.
- Persistence: add a source page and connect it to the TPSM model page, model-choice card, Bhat source page and `knowledge/index.md`; no `130Cs` band page is needed for this model-transfer question.
- Review state: `unreviewed`; source claims self-audited by Codex, not human-reviewed.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[bhat-2014-tpsm-cs-doublet-bands]] | Bhat Ref. [32] ratio data are from this Euroball experiment; same dataset lineage, not independent evidence. |
| foundational-background | [[triaxial-projected-shell-model]] | Direct Cs transition properties used as input for a neighboring-nucleus TPSM comparison. |
| not-direct-evidence | [[a130-model-choice-card]] | Provides an observable/control example only; does not fill `131Ce` or N=76/78 target gaps. |

## Human Review Triage

### P0

- None identified for this bounded source read.

### P1

- `SIM05-5`: chiral interpretation uses relative transition ratios and partner-band patterns; no lifetimes/absolute strengths were measured. If using a stronger mode claim, revisit the energy, transition and missing-absolute-strength boundary.
- `SIM05-6`: the aligned-neutron-pair crossing is a model/author attribution, not a directly measured configuration; preserve as such.

### P2/P3

- No unique citation key was found in the local protected BibTeX export; DOI and title identify the paper.

## Extracted Pages

- Nuclei: no standalone `130Cs` page created for this adjacent-nucleus method control.
- Bands: retain paper-local A/B labels; do not crosswalk to another `130Cs` level scheme without transition identity.
- Methods/models: [[triaxial-projected-shell-model]], DCO, Clover polarization.

## Non-source Notes and Follow-up

- This is the primary dataset for the `130Cs` ratios cited by Bhat Ref. [32]; the Bhat theory comparison and this experiment are one data lineage.
- Lifetimes/absolute strengths remain the decisive missing measurement for static chiral-strength tests; this gap is not transferred as a measurement claim to `131Ce`.
