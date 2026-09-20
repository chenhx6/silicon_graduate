---
type: source
title: "Wadsworth et al. 1977 - Gamma ray spectroscopy in 61Ni: levels below 2.2 MeV"
aliases: [Wadsworth 1977 61Ni spectroscopy, 61Ni levels below 2.2 MeV]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Gamma ray spectroscopy in 61Ni-levels below 2.2 MeV in excitation"
authors: [R. Wadsworth, A. Kogan, P. R. G. Lornie, M. R. Nixon, H. G. Price, P. J. Twin]
journal: "Journal of Physics G: Nuclear Physics"
year: 1977
volume: 3
pages: "35-53"
canonical_source: "Wadsworth et al., J. Phys. G 3, 35-53 (1977)"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/1977_Wadsworth et al_Gamma ray spectroscopy insup61-sup Ni-levels below 2.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/1977_Wadsworth et al_Gamma ray spectroscopy insup61-sup Ni-levels below 2.pdf"
raw_sha256: "47533c460e7af3bdb01b6864790dc1f14aea69f4a1316ea4faf42eb28aec279a"
nuclei: [61Ni, 58Fe, 61Cu]
reactions: [58Fe(alpha,nγ)61Ni, 61Ni(p,n)61Cu]
experiments: [liverpool-geLi-compton-dsam]
models: [compound-nuclear-statistical-model, shell-model]
observables: [level-scheme, gamma-branching, angular-distribution, linear-polarization, mixing-ratio, DSAM-lifetime]
methods: [gamma-gamma-coincidence, angular-distribution, compton-polarimetry, doppler-shift-attenuation]
tags: [61Ni, level-scheme, DSAM, polarization, mixing-ratio, spectroscopy]
---

# Gamma ray spectroscopy in 61Ni: levels below 2.2 MeV

## Bibliographic Record

- R. Wadsworth *et al.*, *J. Phys. G* **3**, 35–53 (1977).
- 规范文件：`raw/papers/gpt/high-spin-20260920/纲图/1977_Wadsworth et al_Gamma ray spectroscopy insup61-sup Ni-levels below 2.pdf`。
- 19-page experiment; title/reaction/figures/tables and historical provenance checked.

## Scope and Reading Depth

- PDF pp.35–53 fully read: `58Fe(α,nγ)61Ni` coincidence experiment at 8.0/8.5/12 MeV, angular distributions/polarization at 7.8/11/13 MeV, `61Cu` β+ reference, Rose–Brink convention, Tables 1–4, level scheme, nine spin/parity assignments, mixing ratios and DSAM centroid shifts/lifetimes.
- Figure/table audit: spectra and decay scheme, all branching/mixing/lifetime tables and representative χ²/polarization plots.
- Not covered: raw spectra, full MANDY/DSAM codes, modern shell-model calculations and later reevaluations.

## Paper Question and Experimental Logic

The paper determines the low-lying `61Ni` level scheme below 2.2 MeV, spin/parity and γ multipole mixing using γγ coincidences, angular distributions, linear polarization and Doppler-shift attenuation, then compares with shell-model calculations.

1. Populate `61Ni` with `58Fe(α,nγ)` and use two Ge(Li) detectors for γγ coincidences; excitation functions and a `61Cu` β-decay source constrain branches.
2. Fit angular distributions with compound-nuclear alignment/population parameters and Rose–Brink phase convention; use a three-GeLi Compton polarimeter for linear polarization.
3. Extract centroid shifts versus `cosθ`, attenuation factors and mean lifetimes using Blaugrund/Lindhard stopping treatment.

## Key Evidence and Reasoning Chain

- Nine levels receive spin/parity assignments: 1015 (`3−`), 1454 (`3−`), 1609 (`5/2−`), 1807 (`7/2−`), 1987 (`5/2−`), 1997 (`7/2−`), 2018 (`5/2−`), 2121 (`7/2−`) and 2129 (`9/2−`, assignments as printed; Table 3/abstract).
- The 656-keV level remains most likely `3/2−` rather than `5/2−` based on isotropic/zero-polarization branches, lifetime/E2-strength consistency and comparison with prior data.
- 1015-keV `3−` assignment is strongly constrained by angular distribution/polarization; δ(948-keV)≈−2.46(16). 908-keV and 1454-keV levels provide strong DSAM/lifetime and E2 strengths.
- Measured lifetimes range from ~1.5 ns for 908 keV to tens of femtoseconds for high levels; abstract values include 450(30) fs (1132), 140(20) fs (1186), 1200(290) fs (1454), 37(30) fs (1609), 99(8) fs (1729), 1600(250) fs (1807), 960(240) fs (1987), 72(6) fs (1997) and 580(60) fs (2018), with exact table locators retained in the PDF.
- `61Ni` low-lying positive-parity states and negative-parity particle-hole configurations are compared with shell-model predictions; older Williams et al. assignments/lifetimes are explicitly contrasted, including disagreement for the 1454-keV spin and many lifetimes.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WA77-1 | γγ coincidences, angular distributions and Compton polarization establish the low-lying `61Ni` decay scheme and multiple spin/parity assignments. | experimental-result | direct | PDF pp.35–53, Tables 1–3 | true |
| WA77-2 | The 656-keV level is most likely `3/2−`, while 1015 keV is assigned `3−` with a large mixing ratio. | experimental-assignment | direct | PDF pp.37–40, Table 3 | true |
| WA77-3 | DSAM centroid shifts yield lifetimes/transition strengths for levels from 908 keV through 2.1 MeV. | experimental-result | direct | PDF pp.35–36, Table 4 | true |
| WA77-4 | Rose–Brink convention, compound-population priors and detector response are essential to δ/spin inference. | limitation | direct | PDF pp.36–37, Methods | false |

## Summary

Wadsworth *et al.* establish a detailed low-energy `61Ni` spectroscopy baseline using the same joint angular-distribution/polarization/mixing-ratio logic as the contemporary `40K` and `61Ni` studies, while adding DSAM lifetimes and explicit cross-checks against `61Cu` decay and shell-model calculations.

## Competing Interpretations and Limitations

Spin/parity assignments depend on compound-nuclear population estimates, Rose–Brink sign convention, polarization-efficiency calibration and stopping/feeding assumptions in DSAM. Several old/new assignments differ; weak lines and unresolved branches should not be treated as equally secure.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| WA77-AR-1 | Evidence chain | γγ level links → `a2/a4`/polarization → joint χ² δ/spin/parity → DSAM lifetime/strength. | PDF pp.36–53 | self-checking |
| WA77-AR-2 | Convention | Rose–Brink phase convention is explicit; cross-source signs require mapping. | PDF p.36 | self-checking |
| WA77-AR-3 | Transfer condition | DSAM lifetimes require matching stopping/feeding and recoil velocity; angular/polarization Q/R are detector-specific. | PDF pp.36–37, Table 4 | active-L3 |
| WA77-AR-4 | Independence | Direct `61Ni` experiment; Meyer 1978/other `61Ni` papers are related but not duplicate rows. | Scope/Introduction | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` the `61Ni` spectroscopy/level-scheme baseline and method lineage for angular distributions, polarization, mixing ratios and DSAM.
- Persistence: link to [[meyer-1978-multiparticle-configurations-61ni-67zn]], [[angular-distribution]], [[linear-polarization-asymmetry]], [[doppler-shift-attenuation-method]] and the high-spin evidence map.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[meyer-1978-multiparticle-configurations-61ni-67zn]] | Independent/preceding `61Ni`/`67Zn` spectroscopy lineage; compare level/lifetime assignments. |
| methodological-bridge | [[doppler-shift-attenuation-method]] | DSAM centroid-shift and stopping/feeding boundaries. |
| methodological-bridge | [[linear-polarization-asymmetry]] | Early three-GeLi Compton polarization and Rose–Brink analysis. |

## Human Review Triage

### P0

- `WA77-P0-1`: preserve assignment/lifetime disagreements with prior `61Ni` studies; do not collapse historical level lineages.

### P1

- `WA77-P1-1`: historical DSAM stopping/feeding and polarimeter calibrations require source-level reanalysis for modern absolute strengths.

## Extracted Pages

- Nuclei: `61Ni` (source-level).
- Methods: [[angular-distribution]], [[linear-polarization-asymmetry]], [[doppler-shift-attenuation-method]]。
- Sources: [[meyer-1978-multiparticle-configurations-61ni-67zn]]。

## L3/L4 Follow-up

- L3 question: reconcile `61Ni` level/lifetime/mixing-ratio lineages from Williams 1975, Wadsworth 1977, Meyer 1978 and later Samanta 2019 while preserving independent datasets. No L4 run: raw spectra/codes absent.
