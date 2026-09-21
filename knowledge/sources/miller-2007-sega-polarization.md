---
type: source
title: "Miller et al. 2007 - Linear polarization sensitivity of SeGA detectors"
aliases: [Miller 2007 SeGA polarization]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Linear polarization sensitivity of SeGA detectors"
authors: [D. Miller, A. Chester, V. Moeller, K. Starosta, C. Vaman, D. Weisshaar]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 2007
volume: 581
pages: "713-718"
doi: "10.1016/j.nima.2007.07.141"
citation_key: Miller_2007
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Miller et al., NIM A 581, 713-718 (2007)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/2007_Miller et al_Linear polarization sensitivity of SeGA detectors.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/2007_Miller et al_Linear polarization sensitivity of SeGA detectors.pdf"
raw_sha256: "a334ee35a84ded50f6a7937c037ee13d2d06b2f8406b0c68fac1a4245999acf3"
nuclei: [245Cm, 249Cf]
reactions: [249Cf-alpha-decay]
experiments: [SeGA, alpha-gamma-correlation]
models: [Klein-Nishina-response, pure-dipole-angular-distribution]
observables: [linear-polarization, asymmetry, Q, figure-of-merit]
methods: [Compton-polarimetry, alpha-gamma-correlation]
tags: [SeGA, polarization, Compton-polarimetry, detector-response]
---

# Linear polarization sensitivity of SeGA detectors

## Bibliographic Record

- D. Miller *et al.*, *NIM A* **581**, 713–718 (2007), DOI `10.1016/j.nima.2007.07.141`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/2007_Miller et al_Linear polarization sensitivity of SeGA detectors.pdf`。

## Scope and Reading Depth

- PDF pp.713–718 fully read: SeGA side irradiation/segmentation, `P/A/Q` formalism, `249Cf→245Cm` α–γ calibration, angular distribution, geometric asymmetry, sensitivity, figure-of-merit comparison and outlook.
- Not covered: in-beam pure-transition calibration and raw waveforms.

## Key Results

- SeGA detectors have four quadrants and eight axial slices (32 segments) and are irradiated from the side for fast-beam Doppler correction. The paper measures the previously untested side-irradiated Compton response (PDF pp.713–714, Figs.1–2).
- `249Cf` α–γ correlations provide opposite-sign pure E1 polarizations at 333 and 388 keV. Angular-distribution coefficients are `a2=−0.29(2)` and `+0.17(1)` (PDF pp.714–716, Eqs.7–12, Figs.3–5).
- Geometric asymmetries from unpolarized lines are `a(333)=0.126(7)` and `a(388)=0.128(7)`. After correction, the relative sensitivity is `Qrel=0.18(2)`, corresponding to `Q≈0.14(2)` near 350 keV (PDF pp.716–717, Fig.8, Table 1).
- The single-detector polarization coincidence efficiency is about `2.99×10^-4`, giving a figure of merit `FM≈5.9×10^-6`, comparable within an order of magnitude to other arrays but lower than Clover sensitivity (PDF pp.717–718, Eqs.13–14, Table 1).
- The authors estimate `ΔP≈0.3` with 5000 photopeak counts and emphasize that in-beam calibration at higher energies and tracking improvements remain necessary (PDF p.718).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MI07-1 | Side-irradiated SeGA acts as a usable Compton polarimeter with `Q≈0.14(2)` near 350 keV. | calibration-result | direct | PDF pp.713–717, Fig.8, Table 1 | true |
| MI07-2 | Detector geometry, unpolarized asymmetry correction and finite-angle averaging are explicit response inputs. | method-boundary | direct | PDF pp.714–717, Eqs.1–6 | false |
| MI07-3 | SeGA's efficiency–sensitivity tradeoff gives `FM≈5.9×10^-6` for the tested setup. | performance-result | direct | PDF pp.717–718, Table 1 | true |
| MI07-4 | The calibration is a source/energy/geometry test, not an in-beam parity assignment. | limitation | direct | PDF pp.717–718 | false |

## Summary

Miller *et al.* establish a practical side-irradiated SeGA polarization calibration for fast-beam spectroscopy. It confirms that segmented arrays can access parity-sensitive polarization while preserving Doppler capability, but the `Q` and figure-of-merit values remain detector-, energy- and geometry-specific.

## Competing Interpretations and Limitations

- The 333/388-keV `249Cf` calibration uses pure E1 transitions and source-specific angular distributions; response at higher energies and in-beam backgrounds remains untested here.
- The 30% figure-of-merit uncertainty includes estimated photopeak efficiency; it is not a universal SeGA constant.
- A measured polarization sign still requires known multipolarity/angular distribution before assigning electric or magnetic character.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| MI07-AR-1 | Response chain | α–γ known `P` → segment counts/asymmetry `A` with geometric `a` correction → `Q=A/P`; finite detector angle averaged. | PDF Eqs.1–12, pp.714–717 | self-checking |
| MI07-AR-2 | Performance chain | `Q²` times coincidence efficiency → figure of merit; compare only after equal energy/geometry definitions. | PDF Eqs.13–14, Table 1 | self-checking |
| MI07-AR-3 | Transfer condition | Recalibrate `a`, `Q`, thresholds, scattering selection and background for any fast-beam in-beam use. | PDF pp.716–718 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]] and the detector-response lineage from Jones/Starosta/Schmid.
- New reusable rule: side irradiation changes response geometry; retain detector orientation when comparing `Q` or parity sensitivity.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `MI07-P0-1`: Do not transfer `Q≈0.14` or `FM≈5.9×10^-6` outside the tested SeGA side-irradiated setup without recalibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
