---
type: project
title: "A≈130 thesis evidence matrix"
aliases: [A130 thesis evidence matrix, A≈130 博士论文证据矩阵]
created: 2026-09-22
updated: 2026-10-14
status: active
review_status: unreviewed
project_stage: seed
confidentiality: private
nuclei: [127i, 128i, 131ce]
tags: [a130, thesis-pipeline, evidence-matrix, collective-modes, durable-learning]
---

# A≈130 thesis evidence matrix

本页是 A≈130 三轴形变与集体激发模式博士论文管线的长期知识资产。它保存可复用的证据矩阵行，不保存每日运行过程；日报和 run receipt 位于 `outputs/learning-daily/`。

## Research Question

哪些 A≈130 能级、跃迁和模式解释已经有可复核的观测支撑，哪些仍需要 mixing ratio、偏振、寿命、绝对跃迁强度或带间连接才能进入博士论文证据链？

## Current Hypotheses

- 能量和符合关系可以稳定约束能级放置，但不能单独确定 `J^π`、组态或集体模式。
- ADO/DCO/偏振、寿命和绝对电磁强度需要组合使用，才能区分 signature/configuration coupling、γ-soft response、wobbling、chirality 和 shape coexistence。
- source lineage 和实验独立性必须与物理证据分开记录。

## Purpose and status

本矩阵用于把“实验直接观测 → assignment handle → 解释边界 → 必要伴随观测 → source lineage”固定下来，供后续 Q&A、L3 研究、综合和论文写作使用。

当前内容来自 evidence-contract、reaction-population 与 Doppler/level-scheme 方法审计，属于 Codex self-audit / `unreviewed` 训练资产，不是人工审核后的 claim registry。

## Evidence matrix

| Candidate | Direct observables | Assignment handles | Interpretation boundary | Necessary next observables | Source lineage |
|---|---|---|---|---|---|
| `127I` high-spin scheme | γ energies, coincidence/intensity balance, energy sums, `R_ADO`; Ding thesis Fig. 5.1–5.2 and Tables 5.1 (PDF pp.58–62; printed pp.50–54) | ADO plus sequence/systematics; labels remain source assignments | Energy closure supports placement, not unique `J^π`, configuration, or collective mode; ADO is geometry-specific | transition-level mixing ratio, polarization, lifetimes and absolute `B(E2)/B(M1)` | [[ding-2012-phd-thesis-127-128i-high-spin]]; single Ding experimental lineage |
| `128I` coupled structures | γ placements around the 167.4-keV `(6−)` isomer, `R_ADO`, model comparison; Fig. 6.2 and Tables 6.1, PDF pp.75–81 (printed pp.67–73) | ADO, coincidence, shell-model/NPA comparison | Reversed `6−/7−` ordering and ambiguous `8−` configuration limit a unique structural reading; no clear chiral doublet | conversion coefficients, polarization/mixing ratios, lifetimes and stronger linking constraints | [[ding-2012-phd-thesis-127-128i-high-spin]]; dependent thesis/Wiki derivatives |
| `131Ce` continuity contract | Current Wiki question highlights missing `δ`, polarization, partner-resolved absolute strengths and links | Existing source/project evidence only; no new L3/L4 analysis in Day 1 | Signature/configuration, γ-soft, wobbling, chirality and shape coexistence remain competing explanations | complete transition properties, absolute strengths, linking transitions, and if applicable g-factor/transfer observables | [[131ce-collective-mode-discrimination]]; multiple dependent lineages |
| Day 1 evidence contract (transferable baseline) | `127I`/`128I` γ energies, coincidence/intensity balance, energy sums and ADO values reported in Ding thesis | Energy closure and ADO constrain placement/multipolarity within this array; source labels remain assignments | These observables do not alone establish unique `J^π`, configuration, triaxiality, wobbling or chirality; model calculations remain model results | transition-level mixing ratios, polarization, lifetimes, absolute `B(E2)/B(M1)` and independent linking/transfer constraints | [[ding-2012-phd-thesis-127-128i-high-spin]]; D12-1, D12-7, AR-2 (PDF pp.53–60, 76–80) |
| `127,128I` reaction-population and level-scheme chain (Day 11) | `124Sn(7Li,3n)128I` at 28 MeV and `124Sn(7Li,4n)127I` at 32 MeV; two-energy `γ-γ` spectra, X-γ coincidences, relative line strengths, detector-angle ADO and scheme crossovers | Relative changes of candidate lines against known `127I` anchors, iodine K-x-ray coincidences, `γ-γ` gates, energy sums and intensity balance; CASCADE/PACE are channel-trend models | Calculated reaction cross sections are not measured yields; the two energies do not isolate one residue. `127I`, `126,128Te` and `125Sb` lines can overlap; X rays identify iodine element, not isotope. The `58.5-keV` `R_ADO` does not resolve `ΔI=0` versus `2`. No lifetime/side-feeding fit is reported. Ionescu 1981 `167Tm` is an independent feeding-aware counterexample to a global Gaussian population, not direct `127/128I` evidence. | More energy points and event-by-event residue or evaporation-particle identification; gate-specific peak/background/response checks; for absolute strengths, matched lifetimes, branches, mixing ratios and feeding model | [[tsukuba-127-128i-li7-28-32mev]]; [[ding-2012-phd-thesis-127-128i-high-spin]] D12-12–D12-19. The thesis lists related 2010/2011 `128I` publications (DOI [10.1088/0256-307X/27/8/082701](https://doi.org/10.1088/0256-307X/27/8/082701); [10.1360/132010-774](https://doi.org/10.1360/132010-774)); without article-level acquisition comparison, treat them as dependent rather than independent evidence. Method boundaries: [[draper-1970-gaussian-substate-side-feeding]] DR70-3; [[ekstrom-1979-spin-alignment-attenuation-a61-a67]] EK79-7; [[ionescu-1981-improved-angular-distribution-analysis-particle-xn]] IO81-4/5/8 (separate `165Ho(α,2n)167Tm` method case, not target evidence). [[herzan-2015-193bi-spectroscopy]] HE15-1 is a separate A≈190 RDT control, not a replication. |
| `A≈130 πh11/2⊗νh11/2 signature-inversion crosswalk` | Excitation-energy systematics, revised bandhead spins I0, signature-splitting curves and inversion spin Iinv in the compiled La/Pr/Pm/Eu/Cs chains | Smooth-systematics crosswalk and signature-inversion plots; particle–triaxial-rotor comparison is conditional on the revised I0 choices | An odd ΔI shift in I0 can flip the inferred favored/unfavored signature and the sign of a γ-deformation discussion; unresolved Cs anchors prevent a unique assignment. Tajima's agreement is not an independent spin check because its parameters were fitted to `124Cs I0=7`; it also does not prove triaxial shape | Independent spin anchors, transition multipolarities/mixing ratios, polarization or lifetimes, absolute strengths and nucleus-specific linking data | [[liu-1996-signature-inversion-a130]]; compiled systematics lineage; primary spectroscopy sources are dependent inputs |
| `131Ba competing-alignment evidence bridge` | Ten-band γ–γ scheme; low-spin νh11/2 signature splitting, angular-distribution A₂/A₀ and A₄/A₀, DCO ratios, E2/M1 mixing ratios, and N=75 crossing-frequency systematics | Angular distributions/DCO/mixing plus alignment gains and proton/neutron crossing frequencies; labels remain source/model assignments | Proton and neutron alignment can drive opposite near-prolate/near-oblate TRS minima, but Harris reference, pairing, finite-detector correction and unresolved bands leave γ and configuration conditional | independent spin/parity anchors, linking transitions, polarization or precise mixing ratios, lifetimes and absolute B(E2)/B(M1)/Q_t | [[ma-1990-131ba-competing-alignments]]; one 119Sn(12C,4n) experiment; separate from Liu compiled systematics |
| `131Ba/133Ce νg7/2 signature-splitting mechanism bridge` | Band energies, γ transitions, `R_ac`, alignments and `J^(2)` for the new N=75 bands; N=73 comparison is compiled from cited prior experiments | Strong-coupling patterns, M1+E2 links and N=73/N=75 systematics support the author’s `νg7/2[404]7/2+` assignment; `S(I)` is an energy-derived handle | CSM/QTR show that non-axiality and nearby `s1/2[400]1/2+` Coriolis mixing both affect `S(I)`; fitted `γ` and PES `β₂,γ` are model results, not direct shape measurements | transition-level mixing ratios and polarization, lifetimes with absolute `B(E2)/B(M1)` or `Q_t`, and independent linking/transfer or g-factor constraints | [[ding-2021-131ba-133ce-signature-splitting]]; two reactions/arrays in one paper, with N=73 comparison dependent on refs.46–48 |
| `131Ce derived-strength and delta-zero evidence bridge` | Bands 1–7 γ energies/intensities, angular-intensity ratios, crossing/alignment and branching-derived B(M1)/B(E2); Table 5.4 g factors and average alignments | Angular ratios plus crossing assignment; Eq. 5.6–5.7 with explicit δ=0 and semi-classical g/alignment/Q0 inputs | B(M1)/B(E2) is a derived ratio, not absolute B(M1) or B(E2); δ=0, model Q0 and configuration mapping limit claims, and agreement with theory does not establish wobbling/chirality or fixed γ | direct δ/mixing, lifetimes, absolute B(E2)/B(M1)/Q_t, polarization and independent linking transitions | [[alwaleedi-2013-band-structures-131ce]]; one 100Mo(36S,5nγ) thesis experiment; compare Ma δ boundary without transferring its value |
| 131Ce shape-multiplicity boundary | TDPAD: 9− isomer moment magnitude Q=0.92(10) eb and g=−0.189(7); DSAM: high-deformation yrast Q0=7.3(4) eb, retrospectively mapped by ENSDF to Band A/SD-1. ENSDF separately lists SD-2 and SD2→SD1 links. | Qs and Q0 constrain different states and are not directly comparable. ENSDF maps PE98→SD1; it does not map SD1 to Alwaleedi Bands 1–7. SD1/SD2 Q0 values come from cited datasets without common covariance. | Verify any positive normal-to-SD transition and endpoint identities in the post-2006 scheme; compare state-resolved E2/E0 or moments under a common convention. | [[ionescu-bujor-1998-static-moments-129-131ce]] IB98-2/IB98-3; [[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-7/PE98-13; [[ensdf-2006-131ce-levels]] ENS06-2/ENS06-4/ENS06-5; [[alwaleedi-2013-band-structures-131ce]] AW13-1/AW13-16 |
| Doppler-to-level/strength evidence contract | 134Nd coincidence-RDDS retains same-line shifted/unshifted components; Mavela reports projectile-specific correction/yield selection; 193Bi Fig.5 explicitly identifies a four-line peak. | Known transition identity, actual photon–recoil angle, ring/gate/distance-resolved centroids and independent calibration; [[doppler-correction]] and [[level-scheme-reconstruction]]. | A narrow corrected total peak does not prove velocity/code identity; low-beta width-only response/velocity/angle decomposition has a rank-2 ambiguity under stated assumptions. Broad/double peaks can be stopping components or several transitions; none establishes chirality/wobbling/configuration. | Executed sorter, beta/geometry/covariance, emitter identity, response and feeding; transition-bound lifetime/branch/δ for absolute strengths. | [[klemme-1999-lifetimes-134nd-neighbors]] KL99-2/KL99-4/KL99-18 is one A≈130 acquisition; [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] DD-20261013-32S-27/28 and [[herzan-2015-193bi-spectroscopy]] HE15-4/5 are independent method controls, not replications of a130 bands. Rank-2 example is our derivation. |
| Doppler-fit validity before lifetime/strength interpretation | Sources report calibrated γ spectra, after-target velocity tuning and joint τ/E analysis; no new A≈130 measurement is made by the synthetic exercises. | Exact bin/ROI and original on/off counts, velocity stage and independent constraints; [[doppler-correction]], [[doppler-velocity-validation-contract]], [[gamma-gamma-coincidence]]. | A correct counting statistic or narrow region does not validate the recoil/history/feeding family. Bin approximation, shared background/MC, observed adaptive edges, parameter boundaries and wrong fixed velocity change the chosen-model inference; these are not source bias estimates. Joint pair, τ profile and projected regions have different meanings. | Executed input/field provenance, first-IP/vertex and parent/residue frame, source calibration objective/Σ, shared event/template IDs, full nuisance/coverage audit; transition-bound τ/branches/δ remain necessary for absolute strengths. | [[baker-cousins-1984-histogram-fits]] BC84-1/2/4/5/9 is a method source, not an experiment; [[ciemala-2021-deep-inelastic-lifetime-method]] CM21-15/16/17/22 and [[ciemala-2020-c16-o20-lifetimes]] share July2017 data, while [[zanon-2023-o20-high-precision]] ZA23-2/10 is an independent acquisition. The self-chosen calculations add no independent experimental evidence. |

### 2026-10-12 `128I` thesis and publication lineage audit

- **Acquisition fingerprint:** [[ding-2012-phd-thesis-127-128i-high-spin]] and [[wang-haixia-2012-173w-128i-high-spin-thesis]] both report the `124Sn(7Li,3n)128I` channel at 28/32 MeV, 9 BGO-suppressed HPGe detectors plus a planar detector, `67×10^6` `γ-γ-t` events and `3×10^6` X-γ events. Wang gives a 200-ns timing window; Ding's shared-experiment description gives 100 ns for the 127I chapter and says 127I/128I use the same offline method. The identical count/array/beam fingerprint makes shared Tsukuba acquisition lineage highly likely; the different timing-window descriptions prevent claiming identical event selections or proving one event-list identity. Keep these dissertations and their 2010/2011 journal derivatives within one evidence lineage unless acquisition logs show otherwise.
- **Scheme-count audit:** Wang reports 48 levels and 72 transitions. The current Ding source-page summary had said 20/31, but those totals are not explicit in the directly checked chapter prose; a reproducible extraction of Ding Table 6.1 gives 61 rows with both transition energy and level arrow. The definitions (all observed entries versus a selected/new subset) have not been reconciled, so the counts must not be compared as established scheme revisions.
- **Publication boundary:** Wang's thesis says Zheng et al. 2009 reported a high-spin 128I scheme before Wang's article was written, without excitation-energy/spin/parity/configuration assignments; Crossref identifies DOI [10.1088/1674-1137/33/S1/057](https://doi.org/10.1088/1674-1137/33/S1/057). Thesis publication lists and Crossref identify the related Wang 2010 [10.1088/0256-307X/27/8/082701](https://doi.org/10.1088/0256-307X/27/8/082701) and Ding 2011 [10.1360/132010-774](https://doi.org/10.1360/132010-774) articles; their full texts were not obtained, so no article-specific acquisition or level-scheme changes are asserted.
- **Next discriminating evidence:** a journal full text containing methods/run identifiers, event-file metadata or contemporaneous acquisition logs could resolve whether 100/200 ns reflects analysis-cut changes, reporting discrepancy or separate runs. Until then, the 2009 report's acquisition independence is also unresolved.


## Evidence Available

当前矩阵行来自 Ding 2012 原始 thesis、`131Ce` project evidence map 和相关方法页。Day 11 增加了从反应入口、蒸发道、探测/门控到 `127/128I` 能级纲图的证据链，并保留模型截面、实验谱线和 Codex 推断的区别。每行均记录直接观测、assignment handle、解释边界、必要观测与 source lineage。形状共存的通用证据要求见 [[heyde-wood-2011-shape-coexistence-review]]（HW11-1/HW11-3）；矩阵不替代 source/raw locator。Day 5 的跨机制观测量映射见 [[shape-observable-matrix]]。

## Risks and Blockers

- thesis/journal/shared-dataset lineages 不能重复计为独立实验；
- ADO 数值依赖阵列几何、alignment、feeding 和效率校准；
- source 页仍可能 `unreviewed` 或 `needs_review`；
- 当前没有用户数据、响应、协方差和代码包，不能进入 L4。

## Decision rule retained

A new line or energy-sum closure may strengthen placement. It cannot by itself promote parity, configuration, triaxiality, wobbling, chirality or shape coexistence. Any future L4 route requires a complete data/response/covariance/code package and the applicable manual gate.

## Next matrix increments

- Day 2 shell-gap/orbital evidence is persisted in [[a130-shell-gap-orbital-observable]] with the `130–134Sn` closure comparison, `131Ce` lifetime-to-`Q_t` reconstruction and `N=75` model counter; source entry points include [[ame2020-sn132-mass-curvature]] and [[li-2004-lifetimes-131ce]]. Add a matrix row only when it maps directly to a thesis candidate/transition, rather than duplicating this bridge page.
- Add A≈130 source rows only after title/DOI, raw or public-full-text identity, locator and source-independence checks.
- Link each row to at least one nucleus/band page, one method/model page, and one competing source or project where applicable.

## Next Actions

1. 为 `131Ce/133Ce` 补充与具体带和跃迁绑定的 `δ`/偏振/寿命/绝对强度证据；不从 `127/128I` 的 ADO 标定移植数值。
2. 若后续需要定量 reaction-population 或 `sigma/I` 分析，先取得用户反应道、粒子/残核识别、角度响应、feeding、事件级协方差与拟合代码；缺少这些输入时保持 L4 readiness boundary。
3. 每次扩展前核对 DOI、raw/public-full-text identity、locator、claim kind 和 source independence。
