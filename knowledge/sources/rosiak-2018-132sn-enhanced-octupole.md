---
type: source
title: "Rosiak et al. 2018: enhanced quadrupole and octupole strength in 132Sn"
aliases: [Rosiak 2018 132Sn E3, 132Sn enhanced octupole strength, HIE-ISOLDE 132Sn Coulomb excitation]
created: 2026-11-01
archive_required: true
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Enhanced Quadrupole and Octupole Strength in Doubly Magic 132Sn"
authors: [D. Rosiak, M. Seidlitz, P. Reiter, H. Naïdja, Y. Tsunoda, T. Togashi, F. Nowacki, T. Otsuka]
journal: "Physical Review Letters"
year: 2018
volume: 121
pages: "252501"
doi: 10.1103/PhysRevLett.121.252501
language: en
canonical_source: "https://doi.org/10.1103/PhysRevLett.121.252501"
citation_key: rosiak_2018_132sn_e3
raw_file: "raw/papers/gpt/learning-daily/20261101-cross-mass-132sn/rosiak-2018-132sn-enhanced-octupole.pdf"
raw_sha256: "74e5280874a860617fb0d5f886be3c7998965b4afd8a62b1292fd20d36222a67"
nuclei: [132sn, 206pb]
reactions: [132sn-206pb-coulomb-excitation]
experiments: [hie-isolde-miniball-132sn]
models: [gosia2, large-scale-shell-model, monte-carlo-shell-model, rpa, rrpa]
observables: [b-e2, b-e3, e1, coulomb-excitation-yield, gamma-energy, beam-purity]
methods: [radioactive-beam, safe-coulomb-excitation, hpge, dssd, gosia2, doppler-correction]
tags: [132sn, n82, octupole, e3, hie-isolde, miniball, coulomb-excitation, primary-experiment]
---

# Rosiak et al. 2018：`132Sn` 增强四极与八极强度

## Bibliographic Record

D. Rosiak et al. (MINIBALL and HIE-ISOLDE Collaborations), *Enhanced Quadrupole and
Octupole Strength in Doubly Magic `132Sn`*, *Physical Review Letters* **121** (2018)
252501, DOI `10.1103/PhysRevLett.121.252501`。本地 self-archived published-version
PDF 共 7 页，SHA-256 为
`74e5280874a860617fb0d5f886be3c7998965b4afd8a62b1292fd20d36222a67`。

## Scope and Reading Depth

全文正文、摘要、实验装置、图表、Table I、GOSIA2 分析和理论比较均已读取。PDF
首页为开放仓储的 published-version copy，排版可能与 APS VoR 略有差异；主文物理
内容、数字和图表均可回链。没有取得 GOSIA2 原始输入、逐事件计数、完整响应矩阵或
联合协方差，因此本文的实验结果可作为 primary reported observable，而不是本任务
重新拟合的 L4 producer。

## Experimental Setup

`132Sn` radioactive beam 在 HIE-ISOLDE 加速到 `5.49 MeV/u`，轰击 `3.1 mg/cm²`
的 `206Pb` 靶；平均束流约 `3.0×10^5 ions/s`，on-target 时间约 127 h。DSSSD
测量散射粒子，MINIBALL 使用 8 个 triple-cluster HPGe；4-MeV 附近 γ 效率为
`2.74(4)%`，Doppler-corrected γ resolution 约 `1.1%` FWHM。上述设置见 PDF
pp.2–3, experimental section and Fig.1。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ROS18-1 | Safe Coulomb excitation identifies the `132Sn` `2+_1→0+` line at `4041.2 keV` and the `3−_1→0+` line at `4351.9 keV` in coincidence with scattered particles. | experimental-fact | direct | PDF pp.2–3, Fig.1 and surrounding text | true |
| ROS18-2 | The experiment reports `B(E2;0+→2+)=0.087(19) e²b²`, `B(E3;0+→3−)=0.11(4) e²b³`, and an E1 strength for `2+→3−`; the `3−→2+` 310.7-keV line was not observed. | derived-observable | direct | PDF p.4, Table I and text after Fig.2 | true |
| ROS18-3 | The `132Sn` `2+` and `3−` transition intensities have relative errors of about 22% and 30%; the analysis uses GOSIA2, detector geometry, level schemes and adopted `206Pb` matrix elements. | analysis-method | direct | PDF p.3, analysis paragraph and Table I | true |
| ROS18-4 | The measured `B(E2)` is locally enhanced relative to neighboring `130,134Sn`; theory attributes the effect to cross-shell proton and neutron excitations while the ground-state wave function remains strongly spherical/doubly magic. | experimental-result-and-model-interpretation | mixed | PDF pp.4–6, Figs.3–4 and conclusion | true |
| ROS18-5 | RPA/RRPA calculations reproduce the measured E3 strength within uncertainties but overestimate the `3−` excitation energy by about `0.8 MeV`. | model-comparison | direct | PDF pp.4–5, Fig.3(c,d) and conclusion | true |
| ROS18-6 | The paper identifies future measurements of E3 strengths in neighboring isotopes as a needed extension; it does not report a two-phonon `0+,2+,4+,6+` octupole multiplet in `132Sn`. | open-question | direct | PDF p.5, paragraph before acknowledgements | true |

## Summary

`132Sn` is now a direct one-phonon E3 benchmark, not an unmeasured octupole nucleus.
The high-energy `3−_1` state and its sizable E3 matrix element provide the starting
phonon for a future two-phonon search. The missing experiment is therefore the
multi-state `3−⊗3−` network and its E3 strength/feeding closure, not the existence of
the first octupole excitation itself.

## Competing Interpretations and Limitations

- The reported `B(E2)` and `B(E3)` are primary experimental results from a GOSIA2
  Coulomb-excitation analysis; the underlying event counts, response files and complete
  covariance are not public in this source.
- The statement that `132Sn` is doubly magic/spherical is supported by the combined
  experiment-theory comparison; it is not a claim that every excited state is spherical.
- The missing `3−→2+` line and the finite uncertainty on `B(E3)` limit direct inference
  about multi-phonon branching.
- One-phonon E3 strength does not establish a two-phonon quartet. The latter requires
  `0+,2+,4+,6+` candidates, feeding control and state-resolved E3/fast-timing observables.

## Nuclear Structure Information

This source establishes a rare-radioactive-beam, safe-Coulomb-excitation route for a
double-magic N=82 nucleus and supplies an experimental E3 anchor for the `132Sn`
two-phonon prospectus.

## Authors' Interpretation

The authors interpret the locally enhanced E2 and E3 strengths as cross-shell
collectivity compatible with a spherical, doubly magic ground state; this interpretation
is constrained by shell-model, MCSM, RPA and RRPA calculations.

## Model Results

LSSM/MCSM/RPA/RRPA comparisons and cross-shell occupation statements are model results.
They help identify the next measurement but do not replace the reported Coulomb-excitation
observables.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence | Status |
|---|---|---|---|---|
| ROS18-AR-1 | Beam-to-observable chain | HIE-ISOLDE beam + DSSSD scattering + MINIBALL γ + GOSIA2 fit gives the primary E2/E3 observables. | ROS18-1–3 | unreviewed |
| ROS18-AR-2 | Cross-mass inference | `132Sn` supplies a one-phonon E3 anchor; the two-phonon question remains open. | ROS18-2, ROS18-6 | unreviewed |
| ROS18-AR-3 | Experiment design | A future quartet search must add multi-state γγγ, feeding and E3/lifetime closure to the existing beam/array architecture. | ROS18-3, ROS18-6 | unreviewed |

## Knowledge Impact and Learning Decision

- `revises`: the cross-mass prospectus no longer treats `132Sn` as lacking direct E3
  information.
- `supports`: a RIB experiment can be designed around an existing HIE-ISOLDE/MINIBALL
  one-phonon baseline rather than an uncalibrated theoretical starting point.
- `limits`: no two-phonon quartet, multi-state E3 network or new RIBLL yield is reported.

## Extracted Pages

- PDF pp.1–2: motivation, HIE-ISOLDE beam production and target/detector setup.
- PDF pp.2–4: γ spectra, GOSIA2 analysis and Table I transition strengths.
- PDF pp.4–6: theory comparison, T-plots, conclusion and future E3 measurements.

## Related Knowledge

- [[132sn-two-phonon-continuum-readiness-20261101]]
- [[ensdf-132sn-coulomb-excitation]]
- [[varner-2005-coulomb-excitation-132-134sn]]
- [[cross-mass-phenomena-detector-beam-prospectus-20261101]]

## Human Review

This page is a Codex self-audit of a primary experiment. `review_status: unreviewed`;
claim-level paper use should return to Table I, the stated GOSIA2 inputs and the actual
response/covariance boundary.
