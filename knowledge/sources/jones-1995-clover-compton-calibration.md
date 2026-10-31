---
type: source
title: "Jones et al. 1995 - Calibration of the EUROGAM clover as a Compton polarimeter"
aliases: [Jones 1995 clover calibration]
created: 2026-09-21
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Calibration of the new composite 'clover' detector as a Compton polarimeter for the EUROGAM array"
authors: [P. M. Jones, L. Wei, F. A. Beck, P. A. Butler, T. Byrski, G. Duchêne, G. de France, F. Hannachi, G. D. Jones, B. Kharraja]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1995
doi: "10.1016/0168-9002(95)00246-4"
volume: 362
pages: "556-560"
pii: "0168-9002(95)00246-4"
canonical_source: "Jones et al., NIM A 362, 556-560 (1995)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1995_Jones et al_Calibration of the new composite “clover” detector as a Compton polarimeter for.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1995_Jones et al_Calibration of the new composite “clover” detector as a Compton polarimeter for.pdf"
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
- 2026-10-17 Crossref exact DOI核题名、10作者、362(2–3)、556–560及1995年8月：`10.1016/0168-9002(95)00246-4`。正文取本地原件，不以registry metadata替代。
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1995_Jones et al_Calibration of the new composite “clover” detector as a Compton polarimeter for.pdf`。

## Scope and Reading Depth

- PDF pp.556–560 fully read: four-crystal geometry, `P`/`A`/`Q` definitions, two calibration configurations, electronics, Table 1 reactions, Table 2 results, Figs.1–5 and threshold/conclusion discussion.
- Not covered: later EUROBALL/Gammasphere calibrations and raw event files.

## Key Results

- The four-crystal n-type Ge CLOVER uses adjacent-crystal Compton events; horizontal/vertical counts give `A`, while angular-distribution fits provide the physical `P`, with `Q=A/P` and an energy/geometry dependence (PDF pp.556–558, Eqs.1–3).
- Calibration spans 197–1368 keV using polarized γ rays from `19F`, `107,109Ag`, `56Fe` and `24Mg`. Table 2 gives `Q=0.34(9), 0.27(3), 0.20(2), 0.167(12), 0.121(5)` at 197, 415, 423, 845 and 1368 keV respectively (PDF pp.557–560, Tables 1–2).
- 原印Eq4为`Q(E)=Q′(E)(B+C E)`，`B=.29±.03`、`C=0.0±.003`，E以MeV计。旧Wiki把C不确定度误作中心值，已纠正。Q′在本文由KN点散射/90°几何文字描述，未印显式代数式；跨文献normalization仍须核定（printed560；JO95-5/9）。
- A 60-keV segment threshold was used to retain adequate statistics and sensitivity; the figure-of-merit changes slowly until the threshold becomes comparable to the incident energy (PDF p.559, Fig.5).
- The detector combines about 2.1-keV FWHM at 1.33 MeV, about 21% per-crystal efficiency and about 125% add-back efficiency relative to the stated NaI reference; the planned 24-CLOVER EUROGAM-II arrangement targets weak-transition polarimetry (PDF p.556, Sec.2 and conclusion).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JO95-1 | CLOVER adjacent-crystal Compton asymmetry can be converted to physical linear polarization through the calibrated `Q(E,geometry)`. | method-result | direct | PDF pp.556–558, Eqs.1–3 | true |
| JO95-2 | `Q` decreases from about 0.34 at 197 keV to 0.121 at 1368 keV for the tested geometry and threshold. | calibration-result | direct | PDF pp.559–560, Table 2, Fig.4 | true |
| JO95-3 | Angular-distribution-derived `P` and detector asymmetry `A` are separate measured/modelled quantities. | observable-boundary | direct | PDF pp.557–560 | false |
| JO95-4 | The 60-keV threshold and the fit are detector-specific; they are not universal CLOVER response constants. | limitation | direct | PDF p.559–560, Fig.5 | false |
| JO95-5 | Eq4打印C=0.0±.003（MeV^-1）、B=.29±.03；旧Wiki的C≈.003是中心/不确定度转录混淆。E改为keV时C的sigma为3×10^-6，不能仍用.003。常数reduction factor也不等于Q本身与能量无关。 | calibration-transcription-correction | direct-and-self-audit | printed560 Eq4 andfollowingparagraph | true |
| JO95-6 | 每个reaction做两配置：CLOVER90°测A、0°测a；70%coaxial逐90/60/45/30/0°测angular distribution，以90°CLOVER addback归一；STAG拟合初态子态布居并作finite-angle修正求P。A/P两步及AND/OR trigger不同，不把P当无模型无误差的已知真值。 | calibration-input-identity | direct | printed557 Fig2；printed558 Sec4 Fig3；printed559–560 Sec5 | true |
| JO95-7 | Eq5定义F=Q²(Nperp+Nparallel)，是当前采集计数型figure of merit；离线逐segment threshold改变接受/统计，采用60keV。Fig5 scan复用数据；未给cross-thresholdCov或生产计数，不据图宣布普适最优阈值。21%/125%的相对NaI photopeak效率不是该N的absolute polarimetry efficiency。 | threshold-and-statistical-boundary | direct-and-self-audit | printed556 Sec2；printed559 Fig5；printed560 Eq5 | true |
| JO95-8 | 采用名义pureE2/point90映射，Table2 a2/a4给P约.231608/.382772/.452416/.530864/.986696；未重放STAG或finite-angle recipe。把printed coefficient sigmas视作精确nominal inputs时，Mg的localJacobian任意2x2Cov可给sigmaP仅.001561–.019654，原表P sigma=.04；这是参数/误差预算未闭合的条件边界，不判作者错误或推断实际Cov。 | bounded-summary-and-uncertainty-replay | task-calculation | printed560 Table2；printed559–560 Sec5 | true |
| JO95-9 | 若将未显式印式的Q′认作ST99 Eq6的标准KN90函数，Eq4 central B=.29/C=0在1368keV给Q=.098337，而Table2为.121(5)；source normalization/fit weighting/unrounded producer未得。不能称published calibration已完全重放，也不据此改B或解释实际差因。 | cross-convention-replay-boundary | task-calculation-and-direct-scope | printed560 Eq4 Table2；printed559 Fig4 | true |
| JO95-10 | 本文F/Ag/Fe/Mg标定与Starosta1999 NORDBALL Cd/Ba/Sn的数据身份不同；器件同族/KN方法和历史引用仍共享，具体unit/selection/完整Σ未核。同能量central曲线比较只作条件设计，不作两个核实验的矛盾裁决。 | calibration-independence-and-transfer | cross-source-synthesis | printed558 Table1 Fig2；printed560 Eq4 | true |

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

## 2026-10-17原件回核：C误差、两步标定与point映射边界

在已见旧Wiki摘要的primed回忆冻结后，核原PDF SHA-256 `8d2cf5ee101d9f3109f6663269fa62f9d6a829e432e05db2502252bf5b132460`，完整读5页printed556–560；视觉查Eq1–5、Fig1–5、Table1/2与高分辨率Eq4参数和Table2列。JO95-1–4/flags/page review不改，新5–10 true，不新增人审。没有作者STAG/原始events/selection、fit recipe或Cov。

Table2首行a2为+.15(4)，a4为−.02(4)、A=.077(8)；1368keV a2=.550(3)的括号按通常字面是.003。原值保留，不从任务推断改其误差。source只给spin路径与结果；2+→0+强制E2，5/2→1/2的名义E2核算不独立排除允许的M3或验证全部参考文献。

完整P90推导、全部五行和Cov范围、Fisher近似条件及Q′同量识别边界写在[[compton-polarimetry]]的“Jones1995：标定系数、偏振误差与阈值信息”。相同P/AD/Q派生列不是独立测量。Q′未印完整式及STAG/finite acceptance/error recipe缺失时，不能凭同叫Klein–Nishina就宣布完整跨paper curve重放。当前不再自由拟合B/C来消除差异；下一优先回核其直接方法伴随来源与response定义。
