---
type: source
title: "Williams et al. 1975 - Low-lying levels in 61Ni"
aliases: [Williams 1975 61Ni levels]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-shell-model
reading_depth: deep-read
title_original: "A study of the low-lying levels in 61Ni"
authors: [J. R. Williams, C. R. Gould, R. O. Nelson, D. R. Tilley, D. G. Rickel, N. R. Roberson]
journal: "Nuclear Physics A"
year: 1975
volume: 253
pages: "365-379"
pii: "0375-9474(75)90487-X"
canonical_source: "Williams et al., Nucl. Phys. A 253, 365-379 (1975)"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/1975_Williams et al_A study of the low-lying levels in 61Ni.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/1975_Williams et al_A study of the low-lying levels in 61Ni.pdf"
raw_sha256: "bfdcc111891a0f88c3ab01df131c438337497fc0d456e8ca3fa6a09912f0a02e"
nuclei: [61Ni, 61Cu]
reactions: [58Fe-alpha-n-gamma, 60Ni-deuteron-p-gamma]
experiments: [GeLi, DSAM, angular-correlation, linear-polarization]
models: [sd-pf-shell-model, Glaudemans-shell-model]
observables: [lifetime, mixing-ratio, linear-polarization, angular-distribution, M1, E2]
methods: [Doppler-shift-attenuation, gamma-gamma-angular-correlation, Compton-polarimetry]
tags: [61Ni, level-scheme, DSAM, mixing-ratio, polarization, shell-model]
---

# Low-lying levels in `61Ni`

## Bibliographic Record

- J. R. Williams *et al.*, *Nucl. Phys. A* **253**, 365–379 (1975), PII `0375-9474(75)90487-X`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/纲图/1975_Williams et al_A study of the low-lying levels in 61Ni.pdf`。

## Scope and Reading Depth

- PDF pp.365–379 fully read: `58Fe(α,nγ)` and `60Ni(d,pγ)` methods, DSAM, angular correlations, linear polarization, level scheme below 2.2 MeV, Table 1 strengths/lifetimes and shell-model comparison.
- Not covered: raw spectra and later re-evaluated `61Ni` levels.

## Key Results

- Seventeen `61Ni` states below 2.2 MeV were studied with DSAM, γ angular correlations, linear polarization and particle–γ coincidences. New `Jπ` assignments include levels at 1016, 1611, 2020 and 2123 keV (PDF pp.365–369, Fig.2).
- DSAM F(θ) factors and lifetimes were obtained with FTAU/stopping-power calculations; examples include 909-keV state `τ≈450^{+330}_{−150} fs`, 1132-keV `τ≈100^{+200}_{−100} fs`, 1457-keV `τ≈480^{+440}_{−160} fs` and 1611-keV `τ≈365^{+160}_{−90} fs` (PDF pp.366–369, Table 1).
- Angular correlations and a Ge(Li) Compton polarimeter determine multipolarities and mixing ratios under the Rose–Brink convention. The paper reports M1/E2 strengths and compares transition rates with the Glaudemans shell model (PDF pp.367–374, Table 1).
- The `1016-keV` assignment is `3/2−`, `1611-keV` `5/2−`, `2020-keV` `3/2−` and `2123-keV` `7/2+` in the authors' combined analysis; weak/uncertain branches retain explicit limits (PDF abstract, Fig.2 and Table 1).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WI75-1 | Multimethod spectroscopy establishes the low-lying `61Ni` scheme and revised `Jπ` assignments. | experiment-result | direct | PDF pp.365–369, Fig.2 | true |
| WI75-2 | DSAM lifetimes and M1/E2 strengths constrain single-particle/shell-model configurations. | lifetime-result | direct | PDF pp.366–374, Table 1 | true |
| WI75-3 | Mixing-ratio and polarization signs use an explicit Rose–Brink convention. | convention-boundary | direct | PDF pp.367–370 | false |

## Summary

Williams *et al.* provide a foundational `61Ni` multimethod data set that complements Meyer 1978, Wadsworth 1977 and Samanta 2019. Its strength is the joint lifetime, angular-correlation and polarization evidence; DSAM stopping/feeding, weak branches and shell-model mapping remain explicit limitations.

## Competing Interpretations and Limitations

- DSAM lifetimes depend on stopping powers, feeding assumptions and line-shape corrections; several values are upper/lower limits.
- Mixing ratios and `Jπ` assignments depend on reference spins, angular distributions, detector response and Rose–Brink phase conventions.
- Shell-model comparison is a model test, not a direct measurement of configuration purity or deformation.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| WI75-AR-1 | Scheme chain | Particle–γ/γ–γ coincidences → angular distribution/polarization → multipolarity/Jπ → level placement. | PDF pp.366–370 | self-checking |
| WI75-AR-2 | Lifetime chain | Doppler shift factors + stopping model → τ → M1/E2 strengths → shell-model comparison. | PDF pp.366–374, Table 1 | self-checking |
| WI75-AR-3 | Transfer condition | Keep low-energy `61Ni` data separate from later `61Ni` remeasurements and high-spin interpretations; reconcile lineages explicitly. | PDF pp.365–379 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[wadsworth-1977-61ni-levels]], [[meyer-1978-multiparticle-configurations-61ni-67zn]], [[samanta-2019-single-particle-configurations-61ni]], [[doppler-shift-attenuation-method]], [[multipole-mixing-ratio]].
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `WI75-P0-1`: Preserve DSAM and Rose–Brink boundaries when reconciling the `61Ni` source lineage; do not merge strengths without transition crosswalks.

## Extracted Pages

- Sources/methods: [[doppler-shift-attenuation-method]], [[multipole-mixing-ratio]], [[wadsworth-1977-61ni-levels]]。
