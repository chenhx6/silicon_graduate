---
type: source
title: "Jones et al. 1995 - Calibration of the EUROGAM clover as a Compton polarimeter"
aliases: [Jones 1995 clover calibration]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Calibration of the new composite 'clover' detector as a Compton polarimeter for the EUROGAM array"
authors: [P. M. Jones, L. Wei, F. A. Beck, P. A. Butler, T. Byrski, G. Duchêne, G. de France, F. Hannachi, G. D. Jones, B. Kharraja]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1995
volume: 362
pages: "556-560"
pii: "0168-9002(95)00246-4"
canonical_source: "Jones et al., NIM A 362, 556-560 (1995)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1995_Jones et al_Calibration of the new composite “clover” detector as a Compton polarimeter for.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1995_Jones et al_Calibration of the new composite “clover” detector as a Compton polarimeter for.pdf"
raw_sha256: "8d2cf5ee101d9f3109f6663269fa62f9d6a829e432e05db2502252bf5b132460"
nuclei: [19F, 107Ag, 109Ag, 56Fe, 24Mg]
reactions: [19F-polarized-gamma, 107Ag-polarized-gamma, 109Ag-polarized-gamma, 56Fe-polarized-gamma, 24Mg-polarized-gamma]
experiments: [EUROGAM-II-clover]
models: [Klein-Nishina-response, point-scatterer-calibration]
observables: [polarization-sensitivity-Q, asymmetry-A, linear-polarization-P, figure-of-merit]
methods: [CLOVER-Compton-polarimetry, angular-distribution]
tags: [CLOVER, EUROGAM, Compton-polarimetry, Q-calibration, linear-polarization]
---

# Calibration of the EUROGAM CLOVER as a Compton polarimeter

## Bibliographic Record

- P. M. Jones *et al.*, *NIM A* **362**, 556–560 (1995), PII `0168-9002(95)00246-4`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1995_Jones et al_Calibration of the new composite “clover” detector as a Compton polarimeter for.pdf`。

## Scope and Reading Depth

- PDF pp.556–560 fully read: four-crystal geometry, `P`/`A`/`Q` definitions, two calibration configurations, electronics, Table 1 reactions, Table 2 results, Figs.1–5 and threshold/conclusion discussion.
- Not covered: later EUROBALL/Gammasphere calibrations and raw event files.

## Key Results

- The four-crystal n-type Ge CLOVER uses adjacent-crystal Compton events; horizontal/vertical counts give `A`, while angular-distribution fits provide the physical `P`, with `Q=A/P` and an energy/geometry dependence (PDF pp.556–558, Eqs.1–3).
- Calibration spans 197–1368 keV using polarized γ rays from `19F`, `107,109Ag`, `56Fe` and `24Mg`. Table 2 gives `Q=0.34(9), 0.27(3), 0.20(2), 0.167(12), 0.121(5)` at 197, 415, 423, 845 and 1368 keV respectively (PDF pp.557–560, Tables 1–2).
- The response is fitted to a Klein–Nishina point-scatterer function with a linear correction, `Q(E)=Q′(E)(B+C E)`; the printed fit parameters are `B=0.29(3)` and `C≈0.003` for `E` in MeV (PDF p.560, Eq.4, Fig.4).
- A 60-keV segment threshold was used to retain adequate statistics and sensitivity; the figure-of-merit changes slowly until the threshold becomes comparable to the incident energy (PDF p.559, Fig.5).
- The detector combines about 2.1-keV FWHM at 1.33 MeV, about 21% per-crystal efficiency and about 125% add-back efficiency relative to the stated NaI reference; the planned 24-CLOVER EUROGAM-II arrangement targets weak-transition polarimetry (PDF p.556, Sec.2 and conclusion).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JO95-1 | CLOVER adjacent-crystal Compton asymmetry can be converted to physical linear polarization through the calibrated `Q(E,geometry)`. | method-result | direct | PDF pp.556–558, Eqs.1–3 | true |
| JO95-2 | `Q` decreases from about 0.34 at 197 keV to 0.121 at 1368 keV for the tested geometry and threshold. | calibration-result | direct | PDF pp.559–560, Table 2, Fig.4 | true |
| JO95-3 | Angular-distribution-derived `P` and detector asymmetry `A` are separate measured/modelled quantities. | observable-boundary | direct | PDF pp.557–560 | false |
| JO95-4 | The 60-keV threshold and the fit are detector-specific; they are not universal CLOVER response constants. | limitation | direct | PDF p.559–560, Fig.5 | false |

## Summary

Jones *et al.* establish the early four-crystal CLOVER calibration used to make EUROGAM polarimetry practical. The source is especially useful for separating physical polarization `P`, count asymmetry `A` and detector sensitivity `Q`, and for retaining energy, threshold and geometry dependence when importing a calibration.

## Competing Interpretations and Limitations

- The angular-distribution fit uses a finite-solid-angle correction and fitted magnetic-substate populations; uncertainties in those inputs propagate into `P` and `Q`.
- The response fit is based on a point-scatterer Klein–Nishina form with empirical scaling; it does not replace a geometry-specific Monte Carlo for another detector arrangement.
- Adjacent-crystal event selection, threshold, add-back and relative efficiency determine the measured `A`; changing them changes the calibration.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| JO95-AR-1 | Observable chain | Adjacent-crystal counts → asymmetry `A` with `a(E)` normalization; angular-distribution fit → `P`; ratio gives `Q`. | PDF Eqs.1–3, Table 2 | self-checking |
| JO95-AR-2 | Response chain | Klein–Nishina point response plus finite geometry/threshold correction gives the fitted `Q(E)`. | PDF Eq.4, Figs.4–5 | self-checking |
| JO95-AR-3 | Transfer condition | Recalibrate `Q`, threshold, geometry and normalization before using CLOVER values in PDCO or parity assignments. | PDF pp.557–560 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]] and the Starosta/Droste CLOVER method lineage.
- New reusable rule: `Q` is a response calibration, not a property of “CLOVER” independent of energy, threshold or geometry.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `JO95-P0-1`: Preserve the tested geometry, threshold and normalization when comparing `Q(E)` with later arrays; do not treat the fit as a universal detector constant.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
