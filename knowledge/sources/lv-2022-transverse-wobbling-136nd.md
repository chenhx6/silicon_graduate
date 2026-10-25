---
type: source
title: "Lv et al. 2022 - Experimental evidence for transverse wobbling bands in 136Nd"
aliases: [Lv 2022 136Nd transverse wobbling]
created: 2026-07-16
updated: 2026-10-22
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Experimental evidence for transverse wobbling bands in 136Nd"
authors: [B. F. Lv, C. M. Petrache, R. Budaca, A. Astier, K. K. Zheng, P. Greenlees, H. Badran, T. Calverley, D. M. Cox, T. Grahn, J. Hilton, R. Julin, S. Juutinen, J. Konki, J. Pakarinen, P. Papadakis, J. Partanen, P. Rahkila, P. Ruotsalainen, M. Sandzelius, J. Saren, C. Scholey, J. Sorri, S. Stolze, J. Uusitalo, B. Cederwall, A. Ertoprak, H. Liu, S. Guo, J. G. Wang, H. J. Ong, X. H. Zhou, Z. Y. Sun, I. Kuti, J. Timár, A. Tucholski, J. Srebrny, C. Andreoiu]
journal: Physical Review C
year: 2022
volume: 105
pages: 034302
doi: 10.1103/PhysRevC.105.034302
canonical_source: https://doi.org/10.1103/PhysRevC.105.034302
citation_key: lv_2022_Experimentalevidence
raw_file: "raw/papers/2022_Lv et al_Experimental evidence for transverse wobbling bands in Nd 136.pdf"
raw_sha256: C5C8A30FE8450372D97DD09FD004A4FF9C1E4427BC837EE7AA157C3DA07D9D69
nuclei: [136nd]
reactions: ["100Mo(40Ar,4n)136Nd"]
experiments: []
models: [particle-rotor-model, triaxial-projected-shell-model]
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio]
methods: [two-point-angular-correlation-ratio, linear-polarization-asymmetry]
tags: [experiment-ingest, transverse-wobbling, even-even, two-quasiparticle]
---

# Transverse wobbling bands in `136Nd`

## Bibliographic Record

PRC 105, 034302 (2022), DOI `10.1103/PhysRevC.105.034302`; the supplied PDF is a self-archived published version and matches the BibTeX record.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full published-version text, L1/L3 bands, contamination audit, combined `P-R_ac`, 751-keV `δ`, wobbling energy and new two-quasiparticle PRM.
- Not covered: earlier same-dataset papers' full experimental details and independent calculation.
- Coverage caveats: only one connecting transition permits a combined polarization/correlation mixing-ratio extraction.

## Paper Question and Scientific Motivation

- Author-explicit motivation: test the predicted two-quasiparticle transverse-wobbling assignment of bands L1/L3 in even-even `136Nd` using a clean connecting transition (PDF pp.1-2).

## Method and Design Logic

- Audit four links for contamination, combine polarization and two-point angular correlation for the 751-keV line, derive δ/E2 fraction, and compare E_wob and electromagnetic ratios with a two-quasiparticle PRM (PDF pp.2-5, Figs.1-5).

## Key Evidence and Reasoning Chain

- One clean mixed M1-dominated link + decreasing E_wob → necessary experimental support; two-quasiparticle PRM mapping → transverse interpretation; model electromagnetic parameters are normalized to the same single point.

## Summary

The paper reports necessary experimental evidence for a two-quasiparticle transverse-wobbling interpretation in even-even `136Nd`. Its link is M1-dominated (`19%` E2), explicitly differing from one-quasiparticle odd-A cases.

## Experimental or Theoretical Setup

High-statistics JuroGam II dataset from the previously documented `100Mo(40Ar,4n)136Nd` experiment. This paper refers setup details to earlier same-run publications and focuses on `R_DCO`, `R_ac` and polarization.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV22-1 | Bands L1 and L3 are treated as predicted zero-/one-phonon candidates built on a two-quasiproton `πh11/2^2` configuration. | author-interpretation | indirect | PDF pp.2-3, Fig.1 | true |
| LV22-2 | Four L3→L1 `ΔI=1` links are known, but contamination/weakness prevents polarization analysis for 768, 785 and 740 keV. | experimental-fact | direct | PDF pp.2-3 | true |
| LV22-3 | Combined polarization and `R_ac` for the clean 751-keV `17+→16+` link yields `δ=-0.48^{+0.13}_{-0.14}`, corresponding to about `19%` E2. | experimental-criterion | direct | PDF pp.3-4, Figs.2-3 | true |
| LV22-4 | The paper explicitly states the link is M1-dominated, unlike one-quasiparticle wobblers, because two aligned quasiprotons give larger M1 matrix elements. | author-interpretation | indirect | PDF p.4 | true |
| LV22-5 | Experimental `E_wob` decreases with spin and is reproduced by a rigid two-quasiparticle PRM. | model-result | direct | PDF p.4, Fig.4 | true |
| LV22-6 | The E2 operator's second-order term is fixed to the single experimental `B(E2)_out/B(E2)_in` point; `g_eff/Q` is fitted to the 751-keV `δ`. | model-result | direct | PDF p.5, Fig.5 | true |
| LV22-7 | Authors conclude this is the second even-even transverse-wobbling case. | author-interpretation | indirect | PDF p.5, Summary | true |

## Nuclear Structure Information

L1/L3 are assigned as zero-/one-phonon bands on πh11/2². Three of four connecting transitions cannot support equivalent polarization analysis because of weakness/contamination.

## Authors' Interpretation

The authors explicitly argue that two-quasiparticle wobbling can have an M1-dominated link, unlike common odd-A one-quasiparticle criteria.

## Model Results

The rigid PRM reproduces E_wob and selected ratios, but second-order E2 and g_eff/Q parameters are fixed to the sole usable experimental transition point.

## Competing Interpretations and Limitations

The model normalizes key electromagnetic parameters to the only measured link/strength point and assumes rigid short-axis quasiparticle alignment; high-spin discrepancies are attributed to alignment depletion. The conventional “predominant E2” criterion is not transferable unchanged to this two-quasiparticle case.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| LV22-AR-1 | Core reconstruction | Direct evidence is one clean M1-dominated mixed link plus decreasing E_wob; two-quasiparticle wobbling geometry is model-dependent. | Key Results and Competing Interpretations above | unreviewed |
| LV22-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| LV22-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| LV22-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| LV22-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| LV22-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: Direct evidence is one clean M1-dominated mixed link plus decreasing E_wob; two-quasiparticle wobbling geometry is model-dependent.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| limits | [[wobbling-motion]] | Two-quasiparticle candidate with M1-dominated connecting transition. |
| limits | [[interband-e2-strengths]] | Demonstrates configuration-dependent criterion boundaries. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `LV22-3`/`LV22-4`, 751-keV link, Figs.2-3 — Evidence: δ≈-0.48 and only ~19% E2, so the clean link is M1 dominated. Agent inference: this is a configuration-specific exception, not support for a universal E2-dominant rule. User check: sign/uncertainty and contamination audit. Risk: mislabeling it E2 dominated reverses the experimental result.

### P1

- `LV22-6`, Fig.5 — Evidence: second-order E2 and g_eff/Q are fixed to the sole usable point. Agent inference: model agreement is not an independent multi-point prediction. User check: normalization procedure and remaining predictions. Risk: fitted reproduction may be overstated as validation.

### P2/P3

- P1: rigid alignment/high-spin depletion. P2/P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[136nd]]
- Concepts: [[transverse-wobbling]]
- Methods: [[two-point-angular-correlation-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

P0: do not describe the 751-keV link as E2-dominant.


## Day18定量审计：136Nd连接跃迁强度与PRM单点定标边界

在Day18正式学习中对本文Table/Fig数据进行深入定量审计，raw SHA256 `C5C8A30FE8450372D97DD09FD004A4FF9C1E4427BC837EE7AA157C3DA07D9D69`已核。原LV22-1–7各claim及`human-reviewed`状态完全保留；新LV22-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV22-D18-1 | 本文751 keV（17+→16+）连接跃迁是四条候选线中唯一获得有效线偏振与 $R_	ext{ac}$ 测量的跃迁；其 $\delta = -0.48^{+0.13}_{-0.14}$ 对应 $E2$ 份额仅为 $18.7\%$（$10.9\%	ext{--}27.8\%$），与奇质量数wobbler中 $E2 > 90\%$ 的主导特征截然不同。Fig. 5中两准粒子PRM理论曲线的二阶E2参数（$\chi \beta_2 = 2.14 	imes 0.185$）与M1参数（$g_	ext{eff}/Q$）系完全由这单一实验点和实验 $\delta$ 强制匹配定标而来，因此模型曲线的高自旋外推是对该单点的参数化延拓而非无参预测。 | task-rate-and-model-audit | derived-and-boundary | PDF pp.3–5 Figs.3–5；新lv22-136nd-wobbling-result-017 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/lv22-136nd-wobbling-contract-017.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/lv22-136nd-wobbling-result-017.json)4项检查全过，确立了136Nd多能带谱系中跃迁强度提取与理论定标的真实边界。

## Day19量化审计：751 keV混合比M1主导性与单点参数化定标边界

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_nd136_chiral_wobbling_crossing_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/nd136-chiral-wobbling-crossing-result-049.json`，核准了 $^{136}\text{Nd}$ 候选横向摇摆连接跃迁多极混合比的物理性质：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV22-D19-2 | 对四条候选 $L3 \to L1$ 连接跃迁进行完整实验多极性审计，确认仅有 751 keV（$17^+ \to 16^+$）获得有效线偏振与 $R_{\text{ac}}$ 提取（其余 740, 768, 785 keV 均因弱或污染无法分析）。751 keV 的混合比 $\delta = -0.48^{+0.13}_{-0.14}$ 导出电四极 $E2$ 份额仅为 $18.73\%$（$10.91\%\text{--}27.77\%$），磁偶极 $M1$ 份额高达 $81.27\%$（$72.2\%\text{--}89.1\%$）。这一 $M1$ 压倒性特征与经典单粒子横向摇摆（$E2 > 90\%$）完全相左。理论 PRM 曲线的高自旋行为依赖于将二阶 $E2$ 参数与 $M1$ 参数强制对齐该单一实验点，因此偶偶核 $^{136}\text{Nd}$ 尚未具备多能级多极性与绝对跃迁寿命所要求的摆动模式充分判定依据。 | task-multipole-and-wobbling-audit | derived-and-boundary | PDF pp.3-5 Figs.3-5; nd136-chiral-wobbling-crossing-result-049.json | true |

## Day20量化审计：751 keV M1主导性与偶偶核摆动模式去污染

> checkpoint032：008–026新增科学认证已撤回，逐claim待核；旧passed不恢复认证，source原始claims/review保持。

依据独立审计程序 `system/scripts/day20_chiral_wobbling_geometry_audit.py` 与基准输出 `outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/chiral-wobbling-geometry-result-022.json`，核准了 $^{136}\text{Nd}$ 候选横向摆动连接线 751.2 keV（$17^+ \to 16^+$）的多极混合特性与模式鉴别边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV22-D20-1 | checkpoint042保751keV同线M1/E2中心份额，撤回普适E2>80%模式阈值/完整几何分类。作者even-even2qp案例明确可M1主导；单点参数定标与外推、两相对B共享输入均保边界。cover造成rawPDF/刊页偏移，AP/P字面保留而actualQ/producer未得，不移植Pr校准。见R42-1/R42-2。 | task-multipole-and-wobbling-audit | derived-and-boundary | PDF pp.3-5 Figs.2-5; chiral-wobbling-geometry-result-022.json | true |

## Day20 checkpoint042：逐线分支、模型轴与校准依赖

本轮先冻结primed回忆，定向原读Table/图/分析与解释范围；未重新测δ或取得完整likelihood/producer。原review/flags保留，新增仅Codex self-audit。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV22-D20-R42-1 | 原作者明确2qpeven-even的连接可M1主导；751keV δ给E2≈18.73%不构成普适>80%阈值反证。χβ2由单E2ratio定标，g_eff/Q由同线δ定标；B_M1out/E2in与E2out/E2in共享同δ/强度/分母，不能互算再计独立验证；外推保模型条件。 | two-qp-and-calibration-scope | original-selected-and-conditional | rawPDF3/journal034302-2; rawPDF5–6/journal034302-4–5 | true |
| LV22-D20-R42-2 | 本raw文件含repositorycover。rawPDF4/journalp3印AP=.03(+.06/−.07)、P=.02(+.04/−.05)，未在此给actualQ/responseproducer，字面保留。额外P=AP/Q合同下中央比1.5不是已核真实Q或统计不一致显著性，不能导入Pr的Q静默修正。 | literal-observable-and-pagination-boundary | original-selected-and-conditional | rawPDF1 cover; rawPDF4/journal034302-3 experimentalparagraph | true |


### checkpoint045：偏振数据谱系与响应来源

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV22-D20-R45-1 | 本文实验数据源自2018年同批次JYFL JuroGam II测量（100Mo(40Ar,4n)136Nd，152 MeV），与Petrache 2018 PRC 97, 041304(R)及Lv 2019博士论文属同一谱系，非独立重复实验。论文偏振分析方法明确指向Starosta 1999 NIM A 423 PDCO方法。由于未公开具体Q(E)响应曲线与效率矩阵，保留AP=0.03(+0.06/-0.07)与P=0.02(+0.04/-0.05)的原印字面值，不人为补充刻度曲线或将其作为独立实验证据。 | experimental-lineage-and-calibration | direct-and-provenance | PDF pp.2-3; Ref [38]; Lv 2019 thesis p.70 [Ref 96] | true |


## Day20量化审计：751 keV连接跃迁多极性、MU08电磁反证与偶偶核横向摆动争议（checkpoint140）

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV22-D20-R140-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |

## Day22 checkpoint091 直接原件纠错

本次读本地8页PDF（含自归档封面），核主文034302-1–7；视觉核034302-4的δ/比值和034302-5的模型定标。SHA256 c5c8a30fe8450372d97dd09fd004a4ff9c1e4427bc837ee7aa157c3da07d9d69。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV22-D22-R091-1 | 唯一可作联合P–Rac的751 keV 17+→16+线给δ=−0.48(+.13/−.14)，约19% E2；同母态相对比rM1=.61(.29)、rE2=.36(.17)。本篇没有报告这对L1/L3带的DSAM寿命或17→18处B(E2)从.44降至.04 e²b²；不能归给本篇11倍绝对强度塌缩。 | experimental-result-and-report-scope | direct-original | 034302-3–5, Secs.II–IV, Figs.3–5 | true |
| LV22-D22-R091-2 | 作者把M1占优解释为两高j准粒子使M1矩阵元较大，仍支持两准粒子横向wobbling；E2二阶算符参数由唯一rE2点固定，geff/Q由该线δ拟合。模型符合支持其解释，但共享单点定标不能计作独立实验或无参验证。 | author-interpretation-and-model-dependency | direct-original | 034302-4, text following Fig.3; 034302-5, Fig.5 discussion and Summary | true |
