---
type: synthesis
title: "High-spin angular distributions, polarization and mixing-ratio evidence"
aliases: [高自旋角分布偏振混合比证据综合]
created: 2026-09-21
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
scope: high-spin-angular-polarization-mixing-ratio
confidence: medium
sources: [yamazaki-1967-aligned-angular-coefficients, suffert-1959-proton-capture-polarization, lange-kumar-hamilton-1982-multipole-admixtures, droste-1996-pdco-formalism, starosta-1999-pdco-experimental-test]
tags: [high-spin, angular-distribution, polarization, mixing-ratio, evidence-map]
---

# High-spin angular distributions, polarization and mixing-ratio evidence


## Agent active summary

Day16原件复核把δ的operator phase、P的坐标轴、detectorcount角色与response权重分成四个必要合同。FH59的plane-axis与SU59normal-axis相差π/2；B15的literal桥须连同As/P一起处理，未知actualproducer保持。SU59同跃迁在替代AD下仍双解，FH59同E3线在不同布居下P不同；都限制只靠多一个偏振数就唯一赋值。Hamilton原16purecase又给等权role抵消的null及rank4分类必要条件，进一步限定reference/selection对象。Palit实际AD/P案例补有条件的选根支持，标定a与Q仍分层、数值不迁移给Garg。实际Rh99摘要的freepositivepopulation可行性另保留边际box与孤立根/联合CI的区别。新增全为self-audit，不改变review状态或取得Day17学分。

## Question and Scope

This synthesis compares the method and application sources in the high-spin batch. It is a method map, not a universal calibration table.

## Evidence Matrix

| Layer | What the sources establish | Main boundary |
|---|---|---|
| Formalism | Yamazaki, Rose–Brink, Taras, Hamilton and Lange define statistical tensors, angular coefficients, polarization terms and δ conventions. | Operator phase, state order and emission/absorption convention must be mapped. |
| Population | Gaussian `σ/J`, attenuation coefficients and cascade `U_k` connect alignment to `A2/A4`. | Alignment and side feeding are reaction dependent. |
| Detector | GeLi, CLOVER, Gammasphere, SeGA, BGO and AFRODITE sources calibrate `P/A/Q`, `Q(E)`, efficiency and finite geometry. | Numerical `Q`, `R_ADO` and `R_DCO` are setup specific. |
| Assignment | DCO/ADO, angular distributions and linear polarization can jointly constrain spin, parity and multipole branch. | A single observable commonly retains multiple branches. |

## Synthesis

1. The reliable unit is a joint fit of transition identity, alignment, detector response, angular distribution, polarization and convention. A quoted δ without this context is not portable.
2. Polarization adds electric/magnetic sensitivity, while angular distributions and DCO primarily constrain angular momentum and multipole combinations. Their information is complementary, not interchangeable.
3. The strongest historical sources expose failure modes: unresolved cascades, background subtraction, finite solid angle, Gaussian alignment assumptions and sign conversion.
4. Modern sources add better detectors and simulations but retain the same logical dependencies. Better resolution narrows uncertainty; it does not remove model identifiability limits.

## Model Dependence

Alignment distributions, attenuation coefficients, detector response and phase conventions are source and setup dependent. Review tables provide transfer rules but do not replace a matched calibration.

## Counter-evidence

Unresolved cascades, finite solid angle, background and multiple δ branches can produce apparently consistent but non-identifying fits.

## Open L3 questions

- Under what covariance conditions can `A2/A4`, polarization and DCO identify δ uniquely?
- Which detector response quantities must be remeasured when transferring a calibration between arrays?
- Can a common likelihood express alignment, feeding, response and branch uncertainty without treating `σ/J` as a universal prior?

## Limitations and Missing Evidence

- `needs_review: true` remains on numerical claims intended for paper-level reuse.
- Review tables are provenance maps, not independent experiments.
- No L4 re-fit is claimed because raw response matrices and complete analysis code are generally unavailable.

## Sources

- [[yamazaki-1967-aligned-angular-coefficients]], [[rose-brink-1967-phase-defined-angular-distributions]], [[taras-1971-phase-defined-polarization-formulas]], [[hamilton-1948-successive-quanta-polarization]]
- [[suffert-1959-proton-capture-polarization]], [[lange-kumar-hamilton-1982-multipole-admixtures]]
- [[droste-1996-pdco-formalism]], [[starosta-1999-pdco-experimental-test]], [[droste-1999-ppco-polarization]]
- [[simpson-1983-sectored-geli-compton-polarimeter]], [[jones-1995-clover-compton-calibration]], [[schmid-1998-gammasphere-polarization]], [[miller-2007-sega-polarization]]

## Self-audit

- Evidence is separated into formalism, population model, detector response and nuclear assignment.
- Historical conventions are not silently converted; each source retains its own sign and state-order locator.
- This synthesis is a Codex self-audit and remains unreviewed.


## Day16 REFLECT：从同符号到同一个observable

| 必要对象 | 这轮原件能够闭合的内容 | 仍不能据此推出 |
| --- | --- | --- |
| 辐射振幅δ | [[krane-steffen-1970-cd110-mixing-ratios]]与[[droste-1996-pdco-formalism]]有本run已核的operator/state-order桥 | FH59δ/SU59x只因都是amplitude ratio就自动同KS/RB号；其上游原件仍缺 |
| electric-axis P | [[suffert-1959-proton-capture-polarization]] SEH59-4与[[fagg-hanna-1959-polarization-measurements]] FH59-5给P_SU=−P_plane | 这个坐标重写是新的物理解，或能认证B15 actualproducer |
| 计数与响应 | FH59-8/9的p/R/r三层给A=QP，circular R另含2；[[bizzeti-2015-agata-triple-cluster-polarimetry]] B15-7/16区分fit与endpoint符号 | 同字母R/Q/As或数值近似即同零点/同分析核 |
| 布居与权重 | B15-2的event-P不同于center-P；FH59-12同E3不同Ep/reference仍不同P | 同能量/EM便能跨selection给定P或直接迁移Q |
| companion与多解 | SEH59-9/10同25Al线在另一AD下仍两解；FH59-14/15保留未分辨cascade与外部赋值条件 | 添加偏振必唯一选根，或把不同AD对象合并为四根数据 |
| 证据独立性 | FH59-14的review原图/表是同Me50数据的复述，B15 modelgrid也非独立实验 | 用同一采集的多种处理/多篇转述增加实验票数 |

因此可复用单元应保存transition identity、source/gate/reference方向、δ完整phase、P轴和counterroles、response/averaging、误差与共有Cov。若其中一个对象未对齐，结果只能作为有条件候选；直接改P或δ的号不能补齐缺失响应。这个判断由已读原件及具体反例支持，不把review表中的数对冲突或模型purelimit当作新实验裁决。

已核源：[[suffert-1959-proton-capture-polarization]] SEH59-4/9/10；[[fagg-hanna-1959-polarization-measurements]] FH59-5/8/9/12/14/15；[[bizzeti-2015-agata-triple-cluster-polarimetry]] B15-2/7/16。仍未得BR1953/Fe55、Me50原producer和联合Cov；新FH59转述不替primary实验。


### Day16 self-audit triage

P0：本批未识别未隔离的来源身份/权限/raw/路径技术问题；历史operator phase与actualresponse缺口已显式保留，不能据此作新δ或实验结论。

| 优先级 | 实际判断及证据 | 后续使用需核的内容 |
| --- | --- | --- |
| P1 | phase/axis/count/response矩阵为Codex跨来源综合；SU59-4、FH59-5/8和B15-16支持同observable的合同，不能归为任何一篇原作者完整结论 | 用于论文前逐项回原轴、原countroles和producer；未对齐时有误翻号/混合数据对象风险 |
| P1 | FH59-12只为review转述的同E3不同布居反例；SEH59-10是原作者对替代AD保留双解的直接限制 | 不把两者合成同dataset或据此判当代array calibration；原实验/response/Cov缺口保持 |
| P2 | 末页、索引和preparedprompt更新只纠正导航/priming；未改reviewflags、raw或Bib | 后续formal17仍独立计卡，不能将本runpreview作学分 |


### Hamilton原件追加的null与分类边界

[[hamilton-1948-successive-quanta-polarization]] HAM48-7–12将前述“同一个observable”进一步限定到两个overallrole权重：8个purecase在等权下给null，故unresolvedsignal的P≈0不独立证明源完全不polarized。识别需要gate/能量/效率次序真正分开角色；Q/finiteacceptance仍另校。另有中间J=1的pureQQ rank4被禁止，所以按α4分类也要有可用rank的前提。新项是直接原式复算和明确选律推断，未作实际核赋值、未解决历史mixedδ operatorphase。


### Palit实测案例对联合观测的补强

[[palit-2000-rh99-clover-polarimetry]] P00-4/5提供实际1117keV同正P与不同EM混合候选、再用同跃迁AD排largeδ的作者分析；与SEH59-10替代AD仍两解互为必要限制。联合观测有判别力仍依原reference/phase/response和误差，不能升级成“多测P必唯一”的定理。P00-1/3又明确a与Q分层，其method引用不迁移C/D给Gargactualcalibration。此为Codex跨来源综合，新source/缺口仍unreviewed，未作新的核赋值。


### 实际Rh99摘要的条件可行性

[[rh99-1117-population-feasibility]]把前述companion问题落到P00 actuala2/a4/P：在明确point/freepositivepopulation和逐marginalbox条件下，两种EMfamily均有strictlypositiveq；sourcefullCov/response/布居prior缺失，不能由此作实验概率或parity更改。centralisolatedroots与convex分离证书又限制只靠网格扫描的排除。新认识是“联合观测的判别力必须连同实际联合统计域和布居约束表述”，未裁决原paper/135Pr模式。


P00-15的额外二阶取向条件给可检验companion：同发射态u2符号若独立成立，可改变同一AD/Pbox的EM可识别性；当前未测得，不能写成作者已给或用Gaussianσ替代。数学witness、额外准备条件与实验支持层分别保存。


### 同母态参考的纯度与测量代价

[[nndc-2017-99rh-matched-reference-records]] N099-13把companion从笼统“加reference”收窄为实际Rh99的561.3ΔJ0/820.4ΔJ1选择：前者模型符号对混合较稳但photon强度弱，后者计数多而需更严纯度。N099-1/10同时把2014新采集、2017编译与P00不同响应分开；未得primarybody/AD纯度条件时不宣布分支已经排除。


### 取向输入的物理支持不能省略完整选择

[[unobserved-feeding-alignment-sign]]串联[[diamond-1966-nuclear-alignment-heavy-ion-reactions]] D66-D16-1/2与[[cejnar-1996-spin-deorientation-alpha-2n-gamma]] C96-D16-1–7：入口低m预期、signedtransfer/保号域、source两链近Gaussian与实际reference是不同证据层。高spin低L的全域条件证明不包含任意蒸发或方向门；C96原range/flow文句须带定义域，原Fig7也保留prior下多极小。此为新self-audit，不改旧人审或把Rh99 u2升为已测。


### 实际三线AD中的条件存在与实验排除

[[199tl-three-ad-reference-feasibility]]针对[[diamond-1966-nuclear-alignment-heavy-ion-reactions]] D66-D16-2保存freeq至少8个、额外lowm找到3个源probable序列的witness；不宣称完整8/3或复现原19→5。共同上态rank4负比例使精确中央数不闭合，但误差box仍有解；这把“prior/companion影响选择”的判断落在实际输入上，未新增核赋值。


### 从Stokes输运到实际校准的对象合同

[[garciaraffi-1997-monte-carlo-compton-polarimeters]] GR97-5–14与[[gr97-stokes-response-and-merit]]把线性Stokes的reference/degree、不同threshold和absolute/activeΩ归一分开。正确normalizedP与PSD不独立认证能量权重；Q/M/派生ε也不是三组独立证据。原Eq13的误读已按原图纠正，不虚构sourceerratum；实际modifiedproducer/Σ缺口保持。
