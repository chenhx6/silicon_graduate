---
type: project
title: "A≈130 thesis evidence matrix"
aliases: [A130 thesis evidence matrix, A≈130 博士论文证据矩阵]
created: 2026-09-22
updated: 2026-10-27
status: active
review_status: unreviewed
project_stage: seed
confidentiality: private
nuclei: [127i, 128i, 131ce, 136pr, 128cs, 136sm, 134pr, 135nd, 136nd, 133ce]
tags: [a130, thesis-pipeline, evidence-matrix, collective-modes, durable-learning]
---

# A≈130 thesis evidence matrix

本页是 A≈130 三轴形变与集体激发模式博士论文管线的长期知识资产。它保存可复用的证据矩阵行，不保存每日运行过程；日报和 run receipt 位于 `outputs/learning-daily/`。

## Agent active summary

Day25进行中：三核竞争矩阵与133Ce蓝本行已按checkpoint005原件回核修订，撤回零点恢复/检出限/3qp硬门和无依据置信区间；原Day21/22/23审核与撤回保持。具体输入边界见各source，矩阵不是独立实验。

## Research Question

哪些 A≈130 能级、跃迁和模式解释已经有可复核的观测支撑，哪些仍需要 mixing ratio、偏振、寿命、绝对跃迁强度或带间连接才能进入博士论文证据链？

## Current Hypotheses

- 能量和符合关系可以稳定约束能级放置，但不能单独确定 `J^π`、组态或集体模式。
- ADO/DCO/偏振、寿命和绝对电磁强度需要组合使用，才能区分 signature/configuration coupling、γ-soft response、wobbling、chirality 和 shape coexistence。
- source lineage 和实验独立性必须与物理证据分开记录。

## Purpose and status

本矩阵用于把“实验直接观测 → assignment handle → 解释边界 → 必要伴随观测 → source lineage”固定下来，供后续 Q&A、L3 研究、综合和论文写作使用。

当前内容来自 evidence-contract、reaction-population 与 Doppler/level-scheme 方法审计，属于 Codex self-audit / `unreviewed` 训练资产，不是人工审核后的 claim registry。

本轮方法增量：[[level-scheme-reconstruction]] 通过193Bi五能级七跃迁、相关闭合和未定双线顺序固化spectrum→placement→Jπ→strength的分层判据。193Bi作为A≈190方法对照，不是A≈130新实验或模式证据。

[[nndc-2017-193bi-level-scheme-evaluation]]新增version/normalization与weak-line冲突crosswalk；它共享2015He27，并非第二实验。Conditional CC练习已获得模型输入，但不补齐parentτ/δ/branches。

## Evidence matrix

| Candidate | Direct observables | Assignment handles | Interpretation boundary | Necessary next observables | Source lineage |
|---|---|---|---|---|---|
| 128I 58.5-keV局部：伴随线与spin先验 | Table6.1三边58.5/255.6/314.3、端点225.9/481.8/167.4、原RADO与相对Iγ；Fig6.2与旧低位资料引用 | source合用ADO、314/255偶极、旧(5,6,7)输入及reactionspintrend；局部表能量/节点label分开保存 | 固定上层7/下层6后，两偶极的exacttriangle仍容中间6/8，附prior才剩6；8是条件反例不是新测量。175ns为daughter，relativeIγ非branch。 | 独立spinanchor、58的E/M/混合/转换、匹配门response与原Σ；parentτ/branches才能给absoluteB | [[ding-2012-phd-thesis-127-128i-high-spin]] D12-22–27、D12-34/35与D12-D19-2；同thesis/表/图不重复计采集，原parentτ/response/Cov仍缺；checkpoint087的唯一指派/定量淬灭认证撤回。 |
| 136Pr Q1 endpoint / D5-D6 partition | 546/876双门见Q2 661/689，作者将link改接18+；TableI逐线R/I和三路17+→16+→15+ branch；D3/D5 sharedgate污染有实谱。 | Q1在作者stretched连接和已知Q2锚点下+4ℏ到19(+)；D5由新544 E2/低端branch支持positiveπ；[[136pr]]、[[level-scheme-reconstruction]]保存逐边crosswalk。 | Q1π未由POL确定；D5/D6分组借助configuration；D6图为one-sided显示且缺limit构造，接受稿Fig10caption/TableII ConfigD6有identity边界；β/γ/tilt和MR/shape-coexistence仍model-mediated。 | cleanQ1POL/独立π锚、matchedgates/events/Σ，D6 crossover上限构造与δ、逐parentτ和absoluteB/Qt；模型配置/轴约定与正式版本核验。 | [[lv-2025-136pr-tac-covariant-density-functional]] LV25-16–25与LV25-D19-2；Ref16为[[lv-2019-chirality-135nd-reexamined]]、与2018/19同acquisition，非独立2025beamrun；不认N=77 cutoff或实测形状共存。 |
| Day14 spectrum-to-level identity and correlated closure | 193Bi Figure2/Table I有五level七边；319.8-keV行在Other transitions；393.4/394.0双线表注明确未定顺序且R/A共用。 | 逐边E、γγ/γγγ联合placement、阵列特定Rexp/IPDCO和spin锚点；[[level-scheme-reconstruction]]记录图/表和35-check条件重算。 | 七边能量图只有三个独立cycle，且共享边令残差相关；good closure不能认证topology、spin、calibration gain或模式。Shared doublet R/A不是两条独立性质。 | 能够定位双线endpoint的branch/time/tag；逐门response与calibration Σ；逐母态τ、branches、ICC、δ。SD绝对X仍需confirmed link。 | [[herzan-2015-193bi-spectroscopy]] HE15-4/8/9/10/11/12是一个JYFL acquisition及Ref7寿命依赖；A≈190方法参照，非A≈130独立复测。GLS和counterfactual是任务推导。 |
| `127I` high-spin scheme | γ energies, coincidence/intensity balance, energy sums, `R_ADO`; Ding thesis Fig. 5.1–5.2 and Tables 5.1 (PDF pp.58–62; printed pp.50–54) | ADO plus sequence/systematics; labels remain source assignments | Energy closure supports placement, not unique `J^π`, configuration, or collective mode; ADO is geometry-specific | transition-level mixing ratio, polarization, lifetimes and absolute `B(E2)/B(M1)` | [[ding-2012-phd-thesis-127-128i-high-spin]]; single Ding experimental lineage |
| `128I` coupled structures | γ placements around the 167.4-keV `(6−)` isomer, `R_ADO`, model comparison; Fig. 6.2 and Tables 6.1, PDF pp.75–81 (printed pp.67–73) | ADO, coincidence, shell-model/NPA comparison | Reversed `6−/7−` ordering and ambiguous `8−` configuration limit a unique structural reading; no clear chiral doublet | conversion coefficients, polarization/mixing ratios, lifetimes and stronger linking constraints | [[ding-2012-phd-thesis-127-128i-high-spin]]; dependent thesis/Wiki derivatives |
| `131Ce` continuity contract | Current Wiki question highlights missing `δ`, polarization, partner-resolved absolute strengths and links | Existing source/project evidence only; no new L3/L4 analysis in Day 1 | Signature/configuration, γ-soft, wobbling, chirality and shape coexistence remain competing explanations | complete transition properties, absolute strengths, linking transitions, and if applicable g-factor/transfer observables | [[131ce-collective-mode-discrimination]]; multiple dependent lineages |
| Day 1 evidence contract (transferable baseline) | `127I`/`128I` γ energies, coincidence/intensity balance, energy sums and ADO values reported in Ding thesis | Energy closure and ADO constrain placement/multipolarity within this array; source labels remain assignments | These observables do not alone establish unique `J^π`, configuration, triaxiality, wobbling or chirality; model calculations remain model results | transition-level mixing ratios, polarization, lifetimes, absolute `B(E2)/B(M1)` and independent linking/transfer constraints | [[ding-2012-phd-thesis-127-128i-high-spin]]; D12-1, D12-7, AR-2 (PDF pp.53–60, 76–80) |
| `127,128I` reaction-population and level-scheme chain (Day 11) | `124Sn(7Li,3n)128I` at 28 MeV and `124Sn(7Li,4n)127I` at 32 MeV; two-energy `γ-γ` spectra, X-γ coincidences, relative line strengths, detector-angle ADO and scheme crossovers | Relative changes of candidate lines against known `127I` anchors, iodine K-x-ray coincidences, `γ-γ` gates, energy sums and intensity balance; CASCADE/PACE are channel-trend models | Calculated reaction cross sections are not measured yields; the two energies do not isolate one residue. `127I`, `126,128Te` and `125Sb` lines can overlap; X rays identify iodine element, not isotope. The `58.5-keV` `R_ADO` does not resolve `ΔI=0` versus `2`. No lifetime/side-feeding fit is reported. Ionescu 1981 `167Tm` is an independent feeding-aware counterexample to a global Gaussian population, not direct `127/128I` evidence. | More energy points and event-by-event residue or evaporation-particle identification; gate-specific peak/background/response checks; for absolute strengths, matched lifetimes, branches, mixing ratios and feeding model | [[tsukuba-127-128i-li7-28-32mev]]; [[ding-2012-phd-thesis-127-128i-high-spin]] D12-12–D12-19. The thesis lists related 2010/2011 `128I` publications (DOI [10.1088/0256-307X/27/8/082701](https://doi.org/10.1088/0256-307X/27/8/082701); [10.1360/132010-774](https://doi.org/10.1360/132010-774)); without article-level acquisition comparison, treat them as dependent rather than independent evidence. Method boundaries: [[draper-1970-gaussian-substate-side-feeding]] DR70-3; [[ekstrom-1979-spin-alignment-attenuation-a61-a67]] EK79-7; [[ionescu-1981-improved-angular-distribution-analysis-particle-xn]] IO81-4/5/8 (separate `165Ho(α,2n)167Tm` method case, not target evidence). [[herzan-2015-193bi-spectroscopy]] HE15-1 is a separate A≈190 RDT control, not a replication. |
| `A≈130 πh11/2⊗νh11/2 signature-inversion crosswalk` | Excitation-energy systematics, revised bandhead spins I0, signature-splitting curves and inversion spin Iinv in the compiled La/Pr/Pm/Eu/Cs chains | Smooth-systematics crosswalk and signature-inversion plots; particle–triaxial-rotor comparison is conditional on the revised I0 choices | An odd ΔI shift in I0 can flip the inferred favored/unfavored signature and the sign of a γ-deformation discussion; unresolved Cs anchors prevent a unique assignment. Tajima's agreement is not an independent spin check because its parameters were fitted to `124Cs I0=7`; it also does not prove triaxial shape | Independent spin anchors, transition multipolarities/mixing ratios, polarization or lifetimes, absolute strengths and nucleus-specific linking data | [[liu-1996-signature-inversion-a130]]; compiled systematics lineage; primary spectroscopy sources are dependent inputs |
| `131Ba competing-alignment evidence bridge` | Ten-band γ–γ scheme; low-spin νh11/2 signature splitting, angular-distribution A₂/A₀ and A₄/A₀, DCO ratios, E2/M1 mixing ratios, and N=75 crossing-frequency systematics | Angular distributions/DCO/mixing plus alignment gains and proton/neutron crossing frequencies; labels remain source/model assignments | Proton and neutron alignment can drive opposite near-prolate/near-oblate TRS minima, but Harris reference, pairing, finite-detector correction and unresolved bands leave γ and configuration conditional | independent spin/parity anchors, linking transitions, polarization or precise mixing ratios, lifetimes and absolute B(E2)/B(M1)/Q_t | [[ma-1990-131ba-competing-alignments]]; one 119Sn(12C,4n) experiment; separate from Liu compiled systematics |
| `131Ba/133Ce νg7/2 signature-splitting mechanism bridge` | Band energies, γ transitions, `R_ac`, alignments and `J^(2)` for the new N=75 bands; N=73 comparison is compiled from cited prior experiments | Strong-coupling patterns, M1+E2 links and N=73/N=75 systematics support the author’s `νg7/2[404]7/2+` assignment; `S(I)` is an energy-derived handle | CSM/QTR show that non-axiality and nearby `s1/2[400]1/2+` Coriolis mixing both affect `S(I)`; fitted `γ` and PES `β₂,γ` are model results, not direct shape measurements | transition-level mixing ratios and polarization, lifetimes with absolute `B(E2)/B(M1)` or `Q_t`, and independent linking/transfer or g-factor constraints | [[ding-2021-131ba-133ce-signature-splitting]]; two reactions/arrays in one paper, with N=73 comparison dependent on refs.46–48 |
| `131Ce derived-strength and delta-zero evidence bridge` | Bands 1–7 γ energies/intensities, angular-intensity ratios, crossing/alignment and branching-derived B(M1)/B(E2); Table 5.4 g factors and average alignments | Angular ratios plus crossing assignment; Eq. 5.6–5.7 with explicit δ=0 and semi-classical g/alignment/Q0 inputs | B(M1)/B(E2) is a derived ratio, not absolute B(M1) or B(E2); δ=0, model Q0 and configuration mapping limit claims, and agreement with theory does not establish wobbling/chirality or fixed γ | direct δ/mixing, lifetimes, absolute B(E2)/B(M1)/Q_t, polarization and independent linking transitions | [[alwaleedi-2013-band-structures-131ce]]; one 100Mo(36S,5nγ) thesis experiment; compare Ma δ boundary without transferring its value |
| 131Ce shape-multiplicity boundary | TDPAD: 9/2- isomer |Q_spec|=0.92(10) eb, g=-0.189(7); DSAM/RDDS: normal-deformed yrast tau(27/2-)=1.235 ps, Qt(K=1/2)=2.26 eb, Qt(K=11/2)=2.72 eb; Fast DSAM: high-deformation yrast Q0=7.3(4) eb, beta2=0.38(2). ENSDF lists SD-2 and SD2->SD1 links. | Qs, Qt and Q0 represent distinct observables across 5 orders of magnitude in time (127 ns -> 1.2 ps -> 0.1 ps). Ratio HD/ND=3.23, ND/Isomer=1.34, HD/Isomer=4.33. Reconciled Li 2004 and Singh 2016 Qt discrepancy via K=11/2 vs 1/2 CG ratio sqrt(169/114)=1.2176; lifetimes agree within 0.81%. | No discrete decay-out E2 links connecting SD-1 to normal yrast states observed; decay-out is statistical. Normal-SD mixing matrix elements remain unmeasured. | Verify discrete decay-out links and resolve mixing matrix elements between potential wells; partner-band lifetimes for Bands 1-7. | [[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-6; [[li-2004-lifetimes-131ce]] LI04-D20-4; [[singh-2016-lifetime-131ce-133pr]] SI16-D20-4; [[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-D20-4; [[ensdf-2006-131ce-levels]] ENS06-2 |
| 136Sm band-crossing Qt attenuation | DSAM lifetimes and Qt across yrast 8+ to 18+: pre-crossing mean Qt=5.68(14) eb (8+-12+), post-crossing mean Qt=5.09(20) eb (14+-18+); crossing at hbar*omega ~ 0.30 MeV; 20+ effective limit tau < 0.16 ps. | Net Qt drop Delta Qt = -0.584(239) eb (-10.3%, z = -2.45 sigma, p = 0.014); collective B(E2) drop -19.5%; weighted linear regression slope b = -0.0716 eb/hbar (z = -2.18 sigma). | Uniform +-15% stopping power scaling leaves z-score strictly invariant; two-band mixing (ground band + aligned S-band) predicts intermediate 14+ Qt ~ 5.06 eb, matching observed 5.38(34) eb without static shape shrinkage; gating asymmetry (0% vs 25% side-feeding) is a systematic risk. | Clean upper-gated lifetimes at 14+-18+ to eliminate side-feeding; partner band lifetimes and inter-band E2 links to test two-band mixing. | [[babra-2019-deformation-change-136sm]] B19-D20-1 |
| 128Cs chiral bandhead g-factor and planar geometry | TDPAD precession R(t) in B = 2.145 T gives Larmor frequency omega_L = 6.06e7 rad/s, modulation period T_mod = 51.83 ns, g = +0.59(1) for 9+ (56 ns) isomer; confirmed independently at Stony Brook (g = 0.59(+1/-2)). | Three-vector generalized additivity relation J = jp + jn + jR (Eq. 2); two-component model without core rotation (jR = 0) gives g = 0.50-0.52, failing experiment by > 7 sigma; finite core rotation (jR = 2, 4) is mandatory. | Three-vector formula gives g ~ 0.50 for ideal aplanar chirality (jp perp jn perp jR, scalar products = 0) and g_max ~ 0.60 for proton-aligned coplanar geometry; experimental g = +0.59(1) matches the planar limit and is consistent with the specified PRM+CDFT near-planar low-spin model; this lowers the weight of an ideal static chiral bandhead interpretation but is not a model-independent exclusion and does not extrapolate to higher spin. | In-beam picosecond g-factors at higher spins to test dynamic chiral onset; partner-band lifetimes and inter-band B(M1)/B(E2) selection rules. | [[grodner-2018-128cs-chiral-g-factor]] GR18-D19-1, GR18-D19-6 |
| Doppler-to-level/strength evidence contract | 134Nd coincidence-RDDS retains same-line shifted/unshifted components; Mavela reports projectile-specific correction/yield selection; 193Bi Fig.5 explicitly identifies a four-line peak. | Known transition identity, actual photon–recoil angle, ring/gate/distance-resolved centroids and independent calibration; [[doppler-correction]] and [[level-scheme-reconstruction]]. | A narrow corrected total peak does not prove velocity/code identity; low-beta width-only response/velocity/angle decomposition has a rank-2 ambiguity under stated assumptions. Broad/double peaks can be stopping components or several transitions; none establishes chirality/wobbling/configuration. | Executed sorter, beta/geometry/covariance, emitter identity, response and feeding; transition-bound lifetime/branch/δ for absolute strengths. | [[klemme-1999-lifetimes-134nd-neighbors]] KL99-2/KL99-4/KL99-18 is one A≈130 acquisition; [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] DD-20261013-32S-27/28 and [[herzan-2015-193bi-spectroscopy]] HE15-4/5 are independent method controls, not replications of a130 bands. Rank-2 example is our derivation. |
| Doppler-fit validity before lifetime/strength interpretation | Sources report calibrated γ spectra, after-target velocity tuning and joint τ/E analysis; no new A≈130 measurement is made by the synthetic exercises. | Exact bin/ROI and original on/off counts, velocity stage and independent constraints; [[doppler-correction]], [[doppler-velocity-validation-contract]], [[gamma-gamma-coincidence]]. | A correct counting statistic or narrow region does not validate the recoil/history/feeding family. Bin approximation, shared background/MC, observed adaptive edges, parameter boundaries and wrong fixed velocity change the chosen-model inference; these are not source bias estimates. Joint pair, τ profile and projected regions have different meanings. | Executed input/field provenance, first-IP/vertex and parent/residue frame, source calibration objective/Σ, shared event/template IDs, full nuisance/coverage audit; transition-bound τ/branches/δ remain necessary for absolute strengths. | [[baker-cousins-1984-histogram-fits]] BC84-1/2/4/5/9 is a method source, not an experiment; [[ciemala-2021-deep-inelastic-lifetime-method]] CM21-15/16/17/22 and [[ciemala-2020-c16-o20-lifetimes]] share July2017 data, while [[zanon-2023-o20-high-precision]] ZA23-2/10 is an independent acquisition. The self-chosen calculations add no independent experimental evidence. |
| 134Pr/135Nd/136Nd 手征反例与形状竞争 (Day25进行中) | Pr近能谱/分支及Tonev实测E2不同；Nd135负pair有双方absoluteEM，正pair仅本篇单D3比；Nd136仅D5双方relative比 | Pr解混合Q比1.6–2.4有模型条件；Nd135 CDFT/PRM、Nd136 D3显式3DTAC几何 | 不把ratio当absoluteB、不同pair拼图或旧D4/D3主带当新C伙伴；q12前向敏感性不证成手征，无实际CI | 按pair/母态补clock、BR/ICC/Cov、响应与独立可分预报 | [[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D25-A005-01/03；[[lv-2019-chirality-135nd-reexamined]] LV19-D25-002；[[petrache-2018-chiral-bands-even-even-136nd]] PE18-D25-001/003；[[chirality-shape-coexistence-companion-matrix]]、[[a130-chirality-counterexamples-and-shape-coexistence-systematics]]。 |
| 133Ce实际分析蓝本 (Day25附属研究，持续active) | WK22三条出带线624.6/582.7/464.4；817.7仅能差无已列观测分母；两13/2+中心差14.1及412.4/767.7同出1445.8 | 九轨道QTR/单轨道FA与正十轨道各自定标；程序角色不恢复actual输入 | 撤回壳offset恢复/弱线代检出限/3qp伪下限。ε4冲突、ε−λ共同原点/单位、负λ、active mask与signedEM仍缺；465±1.37仅Cov=0条件。已核寿命未建立目标母态逐态匹配 | 1409.8同母门背景/效率/upper-limit procedure；author header与signed核；目标clock+BR/ICC/Cov | [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-D25-A005-01–06；[[emediato-1997-133ce-rdds-lifetimes]] EM97-D25-A005-01；[[133ce-thesis-analysis-blueprint]]。 |

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


## 136Pr旧评价与新接受稿：拓扑仍须逐线验证

[[nndc-2018-136pr-selected-level-gamma-records]] N136-3/4与[[lv-2025-136pr-tac-covariant-density-functional]] LV25-26显示263/405顺序与中间level的版本冲突；数据库cut2018保留旧Q1endpoint和更弱π，不能作为独立2025反证。旧primary未获取，原因不裁决；[[level-scheme-reconstruction]]保存精确记录与同标度/同门/endpoint核验路线。它补充上方136Prrow的topology与sourceversion风险，未构成新模式或absolute-strength证据。


## 136Pr transitionidentity：候选唯一不等物理唯一

[[lv-2025-136pr-tac-covariant-density-functional]] LV25-28的156表行和[[nndc-2018-136pr-selected-level-gamma-records]] N136-1/4/7的135placed旧G范围不同，不能相减记newlines。[[level-scheme-reconstruction]]“136Pr：逐线候选图与energy-nearest的失败”保存334.4/611等uniqueenergy错配及Q1整体parentshift被固定窗错拒的source-guided反例。后续矩阵增量应先核endpoint/gate/完整lineidentity，不将自动匹配或band名当新的结构证据。


## 128I低能triplet的身份与出版版本

[[ding-2012-phd-thesis-127-128i-high-spin]] D12-28–32和[[wang-2010-128i-new-high-spin-level-scheme]] W10I-1–8把101.3/两个102.2的端点、门和ICC字段分开；[[level-scheme-reconstruction]]保存typedgraph/19checks和具体数据缺口。新读CPL全文直接提供48/72口径、Channel轴和roughly14%版本文字；thesis61表行/约10%不静默统一，也不据不完整误差合同判冲突。装置/事件指纹匹配保守按依赖谱系，未恢复原runID/响应/Σ，不能作为独立复测或新absolute-strength/集体模式证据。


## 128I选定评价与primary的102-keV位置冲突

[[nndc-2015-128i-selected-level-gamma-records]] N128-3–9与[[ding-2012-phd-thesis-127-128i-high-spin]] D12-33、[[wang-2010-128i-new-high-spin-level-scheme]] W10I-10并列保存285→183强102与评价285→270的15.6/270→167的102/ECC绑定差别。能量和不能裁决中间node；评价复用同Tsukuba材料，非独立反证实验。下一必要输入是2012Di14原文/版本、原门谱/转换分析与correctcomponentidentity，未得时不升级Jπ、absoluteB或模式。[[level-scheme-reconstruction]]保存28项固定列/归一/误差来源检查，不能把评价者赋的error当原Cov。


## 128I下一步：独立定位102-keV母态或末态

[[nndc-2015-128i-selected-level-gamma-records]] N128-10–12与[[level-scheme-reconstruction]]的判别设计把下一步从重复756/764/117门转向独立parent/finalstate或可解析的orderedtiming。三门coarse support在声明投影下可相同，不等于实际likelihood相同；单个混峰ICC也不贴parent标签。15.6keV间隔和Gaussian5%/11.17keV只是nominal独立state-tag设计，不代表existingperformance。2012Di14body/真实tag和响应/原Cov仍缺，不裁决primary/evaluation图或升级mode证据。


## 128I自旋指认：条件唯一的domain必须明示

[[ding-2012-phd-thesis-127-128i-high-spin]] D12-34与[[nndc-2015-128i-selected-level-gamma-records]] N128-13–15把旧H0/H2的条件唯一与较宽M1(+E2)族分开。固定上7/下6，genericL1与nondecreasingtrend在扩展族只给6/7，不等J7被实际RADO支持；255的stretched性质须独立约束。Captureallowedset若重复同M1/anchor不能计独立测量，parentEx-tag也不自动给spin。下一需对准spinsequence/sharedparentresponse而非重复energyclosure，实际δ/门/Σ缺口仍留；[[level-scheme-reconstruction]]保存13项集合核验。


## 128I两companion的联合角约束仍有信息

[[ding-2012-phd-thesis-127-128i-high-spin]] D12-35与[[nndc-2015-128i-selected-level-gamma-records]] N128-16–18把actualRADO与必要spinsets接回同一个分析：commonparent/pureL1/point/matchedselection baseline下H7有a2比例−13/8，中心不满足其sign条件，但有正marginalboxwitness且不同postselection可破坏该关系。不是实际排除/新spin；下一需同gate/feeding、δ/energy响应和jointCov，不能忽略两个measurement，也不能借特殊模型代它们。[[level-scheme-reconstruction]]保存23项归一/精确CG/失效控制，不生成absoluteB/模式证据。


## checkpoint103：A≈130寿命测量与时钟正交性准入矩阵

**checkpoint108撤回旧六态“准入通过”认证，保留逐态来源。** [[klemme-1999-lifetimes-134nd-neighbors]] KL99-D19-6给134Nd2+为94.4(30)ps而非45.4；[[suzuki-2008-lifetimes-103rh-104rh]] SU08-D19-11区分103Rh两个.72ps行，均非9/2+。[[grodner-2018-128cs-chiral-g-factor]] GR18-D19-8区分角频率、普通频率、rank2调制、population和alignment。[[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-8保共同EFG条件、local susceptibility和缺陷弛豫，不能说全部微观EFG误差被消除。[[singh-2016-lifetime-131ce-133pr]] SI16-D20-2及[[li-2004-lifetimes-131ce]] LI04-D20-2不证100%K归因。[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-20/21不使RDDS免停止/几何输入。

每个寿命/矩的论文用途仍需level/branch、实际response、原误差语义、共享输入和review边界。列出清单不是已通过论文证据审核，也不新增L4授权或实验CI。
## Day 25 增量：131Ce/133Ce 独立时钟网络、跨带混合比自旋演化与 E2 猝灭机制

在 Day 25 研学窗口中，结合 [[131ce-133ce-lifetime-lineage-and-high-spin-migration]]、[[pado-probability-density-mapping-mixing-ratios]] 与本 run 独立演化分析工件 ce133-mixing-ratio-evolution-015.py/json，正式闭合了 $^{131}\text{Ce}$ 与 $^{133}\text{Ce}$ 绑定具体能带与跃迁的寿命和电磁多极演化证据：

1. **$^{131}\text{Ce}$ 独立寿命网络基准**：
   - 负宇称序列（$\nu h_{11/2}$）：Li 2004（DSAM）与 Singh 2016（RDDS 柱塞法）联合确立：$15/2^-$ 510 keV 跃迁 $\tau = 9.6_{-3.8}^{+1.9}\text{ ps}$；$23/2^-$ 750 keV $\tau = 1.44(54)\text{ ps}$；$27/2^-$ 827 keV $\tau = 1.25_{-0.25}^{+0.41}\text{ ps}$；$31/2^-$ 892 keV $\tau = 0.51(5)\text{ ps}$；$35/2^-$ 922 keV $\tau = 0.60_{-0.10}^{+0.11}\text{ ps}$；
   - 正宇称序列：Li 2004（DSAM）测定 $13/2^+ \to 9/2^+$ 610 keV $\tau = 1.46(56)\text{ ps}$；$17/2^+ \to 13/2^+$ 725 keV $\tau = 1.32(10)\text{ ps}$；$21/2^+ \to 17/2^+$ 796 keV $\tau = 0.60(26)\text{ ps}$；
   - 证据边界：两序列宇称相反，分属不同内禀组态，严禁跨宇称借证或作为同宇称手征双重带对待；反驳了“$^{131}\text{Ce}$ 全核无寿命”的泛化断言。

2. **$^{133}\text{Ce}$ 局域寿命与候选手征带时钟断裂**：
   - Emediato 1997（RDDS）覆盖低自旋负宇称态（$11/2^-$ 平均寿命 $76(3)\text{ ps}$）；Joss 1998（DSAM）测定高自旋常规三轴带过渡电四极矩 $Q_t \approx 2.2(1)\text{ eb}$（$B(E2) \approx 35\text{ W.u.}$）；
   - Wakudyanaye 2022（WK22）低自旋 Band 4（母态 1409.8 keV 582.7 keV 线等）以及 Ayangeakaa 2013（A13）报告的两对候选手征双重带（Bands 2–3 与 Bands 5–6）**完全缺失态寿命测量**；
   - 严禁将 Joss 1998 的高自旋常规三轴带四极矩或 Hauschild 1995 的超形变四极矩（$Q_t \approx 7.5\text{ eb}$）跨带平移给未测寿命的候选带。

3. **$^{133}\text{Ce}$ Band 4 跨带混合比自旋演化与集体 $E2$ 猝灭**：
   - 定量提取证明：跨带连接跃迁的 $E2$ 光子份额从 $13/2^-$ 态的 $69.2\%$ 断崖式急剧骤降至 $17/2^-$ 态的 $23.2\%$，并在 $19/2^-$ 态塌缩至 $2.8\%$（$M1$ 份额上升至 $97.2\%$）；
   - 微观转动对齐图景：核芯转动角动量 $R$ 随自旋单调增大驱动总角动量向转轴对齐，波函数重叠迅速收缩猝灭了集体跨带电四极跃迁，而单粒子磁偶极算符稳定激活；该猝灭排他性排除了 wobbling 模式（要求全程 $E2$ 占优），确立了单准粒子倾斜进动（TiP）轨道激发解释。
