---
type: source
title: "Evidence against the wobbling nature of low-spin bands in 135Pr"
aliases: [Lv 2022 135Pr, evidence against 135Pr wobbling]
created: 2026-07-03
updated: 2026-10-26
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Evidence against the Wobbling Nature of Low-Spin Bands in 135Pr"
authors: [B. F. Lv, C. M. Petrache, E. A. Lawrie, S. Guo, A. Astier, et al.]
journal: Physics Letters B
year: 2022
volume: 824
pages: 136840
doi: 10.1016/j.physletb.2021.136840
arxiv:
language: en
canonical_source: doi:10.1016/j.physletb.2021.136840
zotero_item_key:
citation_key: lv_2022_Evidencewobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr.pdf"
raw_sha256: 4B87C540BF9DA5141FA88EF8F00859162CB08918D56A5DA74726C7537DF5E26B
nuclei: [135pr]
reactions: [100mo-ar40-1p4n-135pr]
experiments: [jyfl-jurogam2-135pr-ar40-152mev]
models: [triaxial-particle-rotor-model]
observables: [multipole-mixing-ratio, interband-e2-strengths]
methods: [gamma-gamma-coincidence, two-point-angular-correlation-ratio, linear-polarization-asymmetry]
tags: [a130, 135pr, wobbling-counter-evidence, jurogam-ii, qtr, tilted-precession]
---

# Lv 等（2022）：反对 `135Pr` 低自旋带 wobbling 指认的证据

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

B. F. Lv et al., *Physics Letters B* **824**, 136840 (2022)，DOI `10.1016/j.physletb.2021.136840`。题名、作者、年份与 DOI 和只读 BibTeX 条目唯一匹配，使用 citation key `lv_2022_Evidencewobbling`。

## Scope and Reading Depth

主文与 supplementary material 全文精读，并视觉核对主文 Fig.1 的能级纲图、Fig.2 的 angular-distribution 双解与联合 `P-R_ac` 约束、Table 1 的 polarization/`R_ac`/mixing ratio、Fig.4 的实验-QTR 比较，以及补充材料 pp.1-6 的选门与污染检查、完整跃迁表和逐带 QTR 波函数成分。

本页按 `experiment-ingest + project-ingest` 建立反对方证据链。它不把 Lv 2022 的作者结论写成本 Wiki 的最终裁决。补充材料作为主论文附属证据层挂接到本 source，不另建 source、DOI 或 BibTeX 条目。

## Supplementary Material Record

- 文件：`raw/papers/2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr supplementary.pdf`
- SHA-256：`C25CF17CE10EFB2D62FC27A665082DF7BFFEB30F0044726B2730754B035BF225`
- 证据边界：该文件补充主文的实验与 QTR 细节，不具有独立文献身份；所有新增 claims 仍引用 `lv_2022_Evidencewobbling`。

## Summary

作者用独立的 JUROGAM II 数据同时测量 two-point angular-correlation ratio `R_ac` 与 linear polarization，重新确定三条关键 connecting transitions 的 mixing ratio。所得 `|δ|<1` 被作者解释为 M1-dominated，与 wobbling 所要求的 E2-dominated interband links 冲突。作者还重组 Sensharma 2019 的 TW2 候选结构，并用采用标准输入、允许单粒子角动量重排的 QTR 计算，把低激发带解释为 tilted-precession bands。

## Experimental or Theoretical Setup

- 152 MeV `40Ar` 束流轰击 `0.5 mg/cm²` 自支撑富集 `100Mo` 靶，经 `100Mo(40Ar,1p4n)135Pr` 产生 `135Pr`；
- JUROGAM II 包含 24 个 EUROGAM clover 与 15 个 EUROGAM phase-one Compton-suppressed Ge detectors；
- 收集约 `5.1×10^10` 个三重及更高重数 γ 符合事件；
- 用 coincidence、`R_ac` 与 clover linear polarization 联合约束 multipolarity 和 mixing ratio；
- QTR 使用 `ε2=0.16, γ=26°`，采用 irrotational-flow moments of inertia，并允许 single-particle angular momentum 自由重排。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L22-1 | 实验使用 152 MeV `100Mo(40Ar,1p4n)135Pr`、JUROGAM II 的 24 个 clover 与 15 个 phase-one Ge detectors，并收集约 `5.1×10^10` 个 fold≥3 γ 符合事件。 | experimental-fact | direct | p.2, right column, experimental setup | false |
| L22-2 | 本文能级纲图不再把 827、764、1009 keV 三条跃迁组成同一 rotational band；作者建立含 688、871 keV 的 band 4，并把 764 keV 视为可能 band 5 的首条跃迁、827 keV 视为 band 5 到 band 4 的连接。 | experimental-fact | direct | p.2, Fig.1 and final paragraph | false |
| L22-3 | 对 ΔI=1 angular-distribution 数据的 `χ²` 拟合通常可产生 `abs(δ_1)>1` 与 `abs(δ_2)<1` 两个解；本文把 linear polarization 与 `R_ac` 联合作为选择 mixing-ratio 解的实验判据。 | experimental-criterion | direct | pp.2-3, text preceding Fig.2 | false |
| L22-4 | 联合 `P-R_ac` 分析给出 747.3、813.2、450.2 keV transitions 的 `δ=-0.47(+0.09/-0.22)`、`-0.37(+0.10/-0.14)`、`-0.31(+0.10/-0.13)`，三者均满足 `abs(δ)<1`。 | experimental-fact | direct | p.3, Fig.2 and Table 1 | false |
| L22-5 | 作者由上述 mixing ratios 得到 747、813、450 keV transitions 分别约 82%、88%、91% 的 magnetic character。 | experimental-fact | direct | p.3, left column, paragraph below Fig.2 | false |
| L22-6 | 755.1 keV connecting transition 太弱而不能提取 polarization asymmetry；其 `R_ac=0.50(6)` 与 813.2 keV 的 `0.48(6)` 接近，作者据此提出两者可能有相近的 `δ` 解。 | experimental-fact | direct | p.3, Table 1 and paragraph below Fig.2 | false |
| L22-7 | 本文报告 `B(E2;747)/B(E2;526)=0.7(+0.7/-0.5)`；作者认为相近的两条 E2 strengths 与把 band 3 视为相对 band 1 的 one-phonon wobbling excitation 不相容。 | experimental-fact | direct | p.3, left column, final paragraph | false |
| L22-8 | Lv 等指出 Matta 2015 在六条候选 wobbling links 中仅对 747、813 keV 给出 polarization，且只使用 polarization 的正负号而非幅度选择 `abs(δ)>1` 解；正号本身不唯一选出大 `abs(δ)`。 | author-interpretation | direct | pp.2-3, discussion before Fig.2 | false |
| L22-9 | Lv 等指出 Matta 2015 的 747、813 keV polarization 与随后使用相同反应和装置的 Garg 2015 结果存在矛盾；后续 erratum 与 Matta 较接近，但相关分析仍曾受到质疑。 | author-interpretation | secondary-comparison | p.2, left column, discussion of Refs.10, 21, 23, 24 | false |
| L22-10 | Sensharma 2019 对 450、551、519 keV links 只使用 angular distribution 与 DCO-like measurements，未给出 polarization；本文测得 450.2 keV 的 `abs(δ)<1`，作者据此反对其 two-to-one-phonon link 解释。 | author-interpretation | direct | pp.2-3, Fig.2 and Table 1 | false |
| L22-11 | 作者把关键 links 的 M1-dominated character、747/526 E2-strength ratio 与能级重组联合解释为反对 band 3 的 one-phonon 和第二个 `19/2-` state 的 two-phonon wobbling 性质。 | author-interpretation | direct | p.3 and p.5, Summary | false |
| L22-12 | 本文 QTR 使用 `ε2=0.16, γ=26°`、irrotational-flow moments of inertia 与 unfrozen single-particle angular momentum；作者将其与先前为维持 short-axis precession 而调整参数和冻结单粒子取向的计算作对照。 | model-result | direct | pp.4-5, model discussion | false |
| L22-13 | 作者在 p.5 正文报告：标准输入 QTR 中五条带均显著受到 Fig.3(d) 所示 single-particle excitation 机制影响，并发生 single-particle 与 total angular momenta 从 short axis 向 intermediate axis 的快速 realignment；逐带性质的细节指向 supplementary material。Fig.4(c) 只显示近似恒定且接近最大值的 `j_parallel=<I·j>/abs(I)`，支持两角动量近乎平行、同步演化，并不直接显示主轴分量。QTR 对 bands 1、3、4 的能量及 747/813 keV mixing ratios、813 keV transition ratio 给出较好比较；作者据此将这些带解释为基于 `πh11/2` 的 tilted-precession bands。 | model-result | direct | pp.4-5, Fig.3(d) as mechanism sketch; p.5 paragraphs before Fig.4 and Summary; Fig.4(a-d) | false |
| L22-14 | 补充材料给出 747、813、450 keV polarization gates 的逐项污染检查：747 keV 使用 450 keV gated spectra；813 keV 只采用 796 keV suitable gate，并排查邻近 `136,137Nd` 线；450 keV 使用 747 keV gate，并以窄 gate 排除邻近 `136Nd` 449 keV line。作者据联合 `P-R_ac` 中心值选择 `δ`，其误差传播自 `P` 与 `R_ac`，而非不同 `σ/I` 本身。 | experimental-criterion | direct | supplementary material pp.1-4, Figs.2-5 | false |
| L22-15 | 补充 QTR 计算采用 `ε2=0.16, γ=26°`、Harris `J0=J1=12.5`（相应单位）、10 个负宇称轨道、`g_s,eff=0.6g_s,free` 与 `g_core=Z/A`，不使用 frozen approximation，也不增强 short-axis moment of inertia。波函数把 bands 1-5 描述为 orbitals #14/#15/#16 的竞争与随自旋向 intermediate axis 的 realignment；single-particle 与 total angular momenta 同步转向且相对夹角近乎不变。 | model-result | direct | supplementary material pp.4-6, calculations section | false |
| L22-16 | 主文Table1列P：747.3为.04(+.08/−.13)、813.2为−.03(+.05/−.12)、450.2为−.07(+.09/−.10)；SI Table1另列Ap分别.006(+.012/−.019)、−.004(+.007/−.016)、−.017(+.022/−.023)。二者是同一次acquisition的A与P，不是两份独立偏振数据。 | published-observable-identity | direct-and-self-audit | mainp3 Table1；SIp5 Table1 | true |
| L22-17 | SI Eq1的Rac是target在157.6+133.6度对75.5+104.5度、同all-detector轴gates的强度比。Eq2给P=Ap/Q、Ap=(aNperp−Nparallel)/(aNperp+Nparallel)，a(E)=.9844(21)+2(1)×10^−5 E；Q另采用Herzan2015 Ref6，不是继承该文的a。 | geometry-and-calibration-definition | direct | SIp1 Eq1/2及两段说明 | true |
| L22-18 | SI称sigma为spin projection的variance但未在该段给Gaussian指数式；该字面用语不能自动认证D96 Eq19的std。主文/SI未给a0/a1、Q的p0/p1或P与Rac的完整joint Cov。引用的marginal error传播说明不等于提供了完整likelihood。 | width-and-covariance-boundary | direct-and-self-audit | SIp4 error-propagation段；SIp1 calibration段 | true |
| L22-19 | Fig2中旧角分布是重用Matta2015/Sensharma2019；747图的旧大/小模曲线标delta−1.24/−.64，813图为−1.54/−.5；新JUROGAM数据另以green/right axis及新P-Rac点给出。旧曲线再分析不能另算一份独立采集，也未由图标给出小模解的jointCI。 | shared-data-and-branch-identity | direct-and-self-audit | mainp3 Fig2(a–f)及图注 | true |

## Nuclear Structure Information

- band 1 对应既有 [[135pr-yrast-band]]；
- band 3 对应 Matta 2015 的 [[135pr-side-band]]；
- Lv 2022 把 Sensharma 2019 的 [[135pr-second-side-band]] 重组为 band 4 与可能的 band 5，不接受原 TW2 grouping；
- 747、813、755 keV 是 band 3→band 1 links；450 keV 是 band 4→band 3 link。

## Authors' Interpretation

- `|δ|<1` 与 M1-dominated links 不满足 wobbling 的 E2-dominated connecting-transition criterion；
- band 3 不应解释为 one-phonon wobbling，第二个 `19/2-` state 不应解释为 two-phonon wobbling；
- 低激发带更适合解释为 tilted-precession bands。

这些是 Lv 2022 的 counter-interpretation，不是本 Wiki 的最终裁决。

## Model Results

- 标准输入 QTR 允许 rotational、Coriolis-favored short-axis 与 single-particle excitation 三种机制竞争；
- Fig.3(d) 只示意 single-particle excitation 可导致 gradual realignment，并非 bands 1-5 的逐带结果图；
- p.5 正文称五条计算带均显著受该机制影响并发生快速 realignment，逐带性质的细节位于 supplementary material；
- Fig.4(c) 的 `j_parallel` 近似恒定且接近最大值，只支持 single-particle 与 total angular momenta 近乎平行、同步演化，不直接给出主轴分量；
- QTR 对 bands 1、3、4 的能量再现较好，对 bands 2、5 尤其高自旋处有高估；Fig.4(b,d) 比较 747/813 keV mixing ratios 与 813 keV transition ratio。

## Competing Interpretations and Limitations

- 本文是 wobbling 反对方原始实验；其 TiP/realignment 解释仍是模型依赖结论；
- 755 keV 缺 polarization，551 与 519 keV links 未在本文给出新的联合 `P-R_ac` mixing ratios；
- 对 Matta/Garg/erratum 的 polarization 争议涉及多篇来源；在这些来源分别摄入前，本页只记录 Lv 2022 的比较性陈述；
- band 5 部分结构依赖此前报告但本实验未观察到的 1009 keV transition；
- QTR 对 bands 2、5 的高自旋能量仍有偏差。

## Extracted Pages

- Nucleus: [[135pr]]
- Bands: [[135pr-yrast-band]], [[135pr-side-band]], [[135pr-second-side-band]], [[135pr-signature-partner-band]]
- Experiment: [[jyfl-jurogam2-135pr-ar40-152mev]]
- Concepts: [[wobbling-motion]], [[transverse-wobbling]]
- Observables: [[multipole-mixing-ratio]], [[interband-e2-strengths]]
- Methods: [[two-point-angular-correlation-ratio]], [[linear-polarization-asymmetry]]
- Model: [[triaxial-particle-rotor-model]]
- Project: [[135pr-wobbling-controversy]]

## Personal Notes

本页建立 counter-source，不裁决争议。用户已完成 source 页面及 L22-1 至 L22-15 的核对，并校正 L22-13 对 Fig.3(d)、p.5 正文与 Fig.4(c) 的证据边界；全部 claims 均为 `needs_review: false`。

## 2026-10-17定向复核：标定谱系与逐量对齐

本次核主文6页、SI7页与各自SHA-256，读实验/分析/反证/QTR主线；视觉核主文Fig2/Table1、SI Eq1/2、SI Table1及Fig3–5的门和污染标签。旧L22-1–15及page级human-reviewed保持；Personal Notes原称“全部claims false”只指当时1–15。新L22-16–19及本节仅Codex self-audit，needs_review:true，不属新增人审。

按SI明确采用的[[herzan-2015-193bi-spectroscopy]] HE15-10，Qpoint=(1+x)/(1+x+x²)、x=E/(me c²)，Q=Qpoint[.42−1.9×10^−4 E(keV)]。[[135pr-mixing-branch-input-contract]]的新计算用独立原件的Q中央系数把SI Ap及其误差尺度变回主文P，三线均在印刷rounding内闭合。它确认两张表的数据身份，不证明完整误差预算已包含/漏掉Q误差，也不恢复原counts/fit Cov。

本文a(E)与Herzan Fig3的a(E)不同；所采用的是其Q(E)，不能因同阵列名称一并复制所有calibration。原件SI p4的width措辞按L22-18保留，不把它改写为方差或标准差已核准的Gaussian prior。没有用本任务integer-only kernel计算135Pr半整数响应，作者模式解释和反方/后续支持方仍并列。


## Day18 checkpoint050修订：小根结果与TiP解释的适用范围

原LV22-claims/review保留，旧LV22P-D18-1的“全实验排除”改为作者结论与本任务边界分列。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV22P-D18-2 | Table1三条线δ=-.47/-.37/-.31来自本次P/Rac与角分布联合分析；813的.12(.08)是沿这些分支输入得到的派生BE2out/in。它不是独立寿命或绝对矩阵元，且误差/response/branch协方差未在本任务重建。 | reported-result-and-dependence | direct-and-boundary | PDF3 Table1；PDF2–4 methods | true |
| LV22P-D18-3 | 作者以|δ|<1、M1主导和QTR再现把低带解释为tilted precession并反对原wobbling解释；这是该核/该实验的结构结论。把它推广为所有低自旋wobbling的排除，或把.12与旧.843的7倍差写成无模型条件的实验CI，均超出来源。 | author-interpretation-boundary | direct-and-boundary | PDF1 abstract；PDF3–5 discussion/summary | true |

## Day20 checkpoint041：135Pr对立解释、相对强度与模型文字

本轮按primed-recall-041先冻结暴露回忆；实际回读两篇主文全文主线与Lv全部SI，scope041逐页记录。旧human-reviewed范围及原flags不变；新增为Codex self-audit，不是新人审或原实验重分析。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L22-D20-R41-1 | 主Table1/SITable1的747.3/813.2/450.2对应band3→1(17/2→15/2、21/2→19/2)和band4→3(19/2→17/2)，δ−.47/−.37/−.31保原非对称误差。主P误差端点各跨0，作者以联合P-Rac决定分支；SI Ap经Q转成主P，同采集不计两份证据。755.1无P/新δ。 | observable-lineage-and-measured-scope | direct-original-and-conditional | mainPDF2 Fig1; mainPDF3 Table1/Fig2; SIp1 Eqs1–2; SIp5 Table1 | true |
| L22-D20-R41-2 | 本任务用SI Iγ747.3/526.2=9.4/.4、Iγ813.2/726.0=6.4/3.7、主δ与reference pureE2声明，得同parent photon E2比.735975/.118129。parentτ可相消，实际δ/intensity/response/Cov未重建。正文.7(+.7/−.5)系作者特定onephonon禁戒测试，不是ratio<1.5普适标准或新绝对B/τ。 | conditional-rate-ratio-and-author-test | direct-original-and-conditional | mainPDF3 finalparagraph; SIp5 Table1; task result041 | true |
| L22-D20-R41-3 | Lv对早期frozen处理的批评是作者模型比较陈述；Matta2015 PDF5另明确Coriolis使j脱离short转medium，不能仅据批评判实际Matta全spin冻结。Lv的j_parallel及orientation是QTR输出，bands2/5高spin能量高估；未取得原producer以作全参数/算法等价审计。 | cross-source-model-comparison-boundary | direct-original-and-conditional | mainPDF4–5; SIpp4/6; MattaPDF4–5 | true |


### checkpoint141：康普顿散射偏振去污染、M1 主导性确立与多核摆动争议审查

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV22-D20-R141-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |

## checkpoint146：原件身份与推断边界更正

本轮为Codex定向self-audit；已有review_status与原claim flags不变。121–145旧认证撤回；实际新阅读范围见source-reading-scope-146.json，引用较早纠错不冒称新全文阅读。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| L22-D20-R146-1 | 新实验联合P-Rac分析给小模δ，作者据此反对所述低spin带wobbling并提出TiP。三线P误差端点跨0，不能仅用中心符号声称唯一排除。0.12与.843之比是派生输出中央比，不是恢复真实共同likelihood。旧124等生成分析的726keV、δ−3.20/−.18、P−.16(4)与34→1.17W.u.链未受此原表支持，继续隔离；不推广到La/Xe无偏振或全区排除。 | prior-primary-audit-and-transfer-boundary | source-and-bounded-self-audit | L22-D20-R41-1至R41-3; Table1/Fig2/SI Table1 | true |

## Day 21周考对比：135Pr多极双解简并与摇摆模式证伪（Checkpoint 003）

## Day21 checkpoint055：135Pr带间相对几率与绝对强度边界审计

124纠正：R55不证明所有候选被唯一排除或普适禁戒；保作者联合分析/小模解与TiP解释。旧全文见superseded-124，不声称本轮新读这些原件全文。原review与原始claims/flags保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV22-D21-1 | superseded：124撤回本条新科学认证；改用本页L22-D20-R146-1的有限范围。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| L22-D21-R55-1 | superseded：124撤回本条新科学认证；改用本页L22-D20-R146-1的有限范围。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| L22-D21-R55-2 | superseded：124撤回本条新科学认证；改用本页L22-D20-R146-1的有限范围。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| L22-D21-R55-3 | superseded：124撤回本条新科学认证；改用本页L22-D20-R146-1的有限范围。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |

## Day22 原件复核：支路分母、联合偏振及模型比较

主文6页与SI7页实际重读，视觉核主文p3及SI p5的表/分母，raw/SI哈希保持。以下仅Codex self-audit，原page review/既有claim flags不改；新增claims均needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L22-D22-001 | 主文的B(E2;747)/B(E2;526)=.7(+.7/−.5)来自同母态band3 17/2−(1477.9keV)，747.3到band1 15/2−、526.2到band2 13/2−，两者均为带间退激。SI Table1的526.2多极性/Rac空白；按E2分母使用是提取前提，不能误记成band3的in-band E2测量。 | transition-and-denominator-identity | direct-original-and-extraction-boundary | main p.3, 747/526 paragraph; SI p.2 Fig.1; SI p.5 Table 1 | true |
| L22-D22-002 | Fig4(d)将Table1的rE2=.12(.08)、rM1=.4(.3)绑定813.2与726.0同母态退激，SI表分别给6.4(.3)、3.7(.3)光子强度及2203.9keV 21/2−母态。755.1仅有Rac、未测P，不能因Rac接近813而填入实测δ。 | transition-strength-and-missing-data | direct-original | main p.3 Table 1; main p.5 Fig.4(d); SI p.5 Table 1 | true |
| L22-D22-003 | 联合P-Rac新结果的747.3keV中央P为+.04，仍给|δ|=.47<1；这直接限制仅靠正号选大模解的推断。主文P与SI Ap来自同一次采集和同一Q校正，不是独立偏振证据；完整jointCov未提供。 | joint-observable-and-dependence | direct-original-and-bounded-inference | main p.3 Fig.2(b) and Table 1; SI p.1 Eq.2; SI p.4 error paragraph; SI p.5 Table 1 | true |
| L22-D22-004 | 作者对旧QTR冻结方向的批评保留为其观点，但F14及Matta原文实际描述完整QTR中的j重定向；未获得旧producer前不能把该批评升格为旧全spin实现已核冻结。Lv本模型也对bands2/5能量过估；“standard”是其输入方案称谓，不是无参数实验认证。 | competing-model-interpretations | cross-source-self-audit | main p.4–5 model discussion; SI p.4 and p.6 calculations; F14-D22-004; M15-D22-003 | true |

### Knowledge Impact and Learning Decision

Supports/limits：保留作者的支持或反对解释，并将逐线测量、选解前提、模型结果和依赖链分开。四列比较与条件强度重建见[[wobbling-geometry-phonon-observable-contract]]；不以模型或跨采集中心值差替代新实验置信区间。

### Day22能级中央值的能量判据重建

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L22-D22-005 | 按Matta Eq1的相邻yrast平均定义，以本SI Table1的bands1/3能级重建Ewob：17/2为417.2、21/2为386.0、25/2为255.3、29/2为172.4、(33/2)为324.55keV。最后spin原表带括号，完整能级Cov未提供。这组能量仍先降后升，而作者据联合电磁数据解释为TiP，说明下降曲线单独不裁决模式。以上是本任务对实测能级中央值的派生，不是作者新列的Ewob表或新CI。 | derived-energy-criterion | original-input-and-our-calculation | SI p.5 Table1 bands1/3; M15 printed082501-3 Eq1 | true |

## Day22 checkpoint095：逐线P/δ、比值对账和模型归属

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L22-D22-R095-1 | Table1逐线配对：747.3的P=.04(+.08/−.13)、δ=−.47(+.09/−.22)；813.2的P=−.03(+.05/−.12)、δ=−.37(+.10/−.14)；450.2的P=−.07(+.09/−.10)、δ=−.31(+.10/−.13)。不能把747的+.04绑给813的−.37。747中央P为正而δ小限制正号独立选根，但不证明任意负δ必正P，也不据此推出未经联合响应验证的3σ。 | line-resolved-experimental-fact | direct-original | main p.3 Table1 and Fig.2 | true |
| L22-D22-R095-2 | 813.2/726同母态退激：SI光子强度6.4(.3)/3.7(.3)、δ=−.37，按纯E2分母和MeV惯例重建rE2=.11813、rM1=.39785，与打印.12(.08)/.4(.3)近合。这只是打印中心算术；Matta .843/.12=7.025为独立测量中央比，不是同一计数只改δ后的物理塌缩。相同分支/能量假设下δ−1.54到−.37只给E2份额因子5.8415。 | relative-strength-reconstruction-boundary | original-input-and-task-arithmetic | main p.3 Table1; main p.5 Fig.4(d); SI p.5 Table1 | true |
| L22-D22-R095-3 | SI的a(E)=.9844(.0021)+2(1)×10−5E，Q(E)借Ref6既有JUROGAM-II标定。作者用P–Rac和σ/I曲线映射界限，无公开完整joint Cov。作者重组旧TW2网络并由QTR提出TiP，但bands2/5高spin能量仍过估；完整模型图像是解释。不能把全部可能的TW2结构绝对不存在或TiP唯一成立写成实验直接事实。 | response-and-interpretation-boundary | direct-original | SI p.1 Eq2, p.4 extraction paragraph; main p.2 Fig1 and final paragraph; main p.5 model comparison | true |


## Day23：同I两序列的能级中央值

本次fresh视觉核SI PDF5 Table1并重核SI SHA，原L22既有claims/人审flags不变，新增needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L22-D23-001 | SI Table1给Band2/Band3在17/2−的Ei分别1433.9/1477.9keV，在21/2−分别2159.4/2203.9keV；同I中央差E3−E2为44.0/44.5keV。它们是不同序列的能级，不是跨实验测量差或两δ分支；完整能级Cov未在本任务恢复，未据此计算新显著性。 | line-bound-same-spin-level-identity | direct-original-and-centre-arithmetic | SI PDF5 Table1, Band2/Band3 rows482.1/747.3 and725.5/813.2 | true |

这些已发表中央值可检验指定模型下的mapping，但原源/旧模型参数的能谱定标谱系须保留；本任务对照不自动成为blind holdout。实际固定H练习见[[signature-tip-shears-discrimination-contract]]，未修改原实测计数、δ或能级。

## Day23：QTR输入与共同磁尺度的适用条件

本次针对SI PDF4/6 calculations、主文PDF4–5比较限制回读，SI PDF6重新视觉核并校验原SHA；未新称重读全主文/SI。原L22-1–15及page人审历史保留，以下仅Codex self-audit。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L22-D23-002 | SI采用10个费米面附近负宇称轨道，proton Fermi44MeV，gs,eff=.6gs,free及gcore=Z/A；#14/#15/#16为h11/2来源、波函数主分量随band/spin变化。Nilsson/配对使用standard参数的文字及上述g值，不等于已公开每一轨道相干振幅/占据和完整EM矩阵；本任务single-j commonSM因子化不能只凭这句标准参数便认证为完整QTR。若多个Nilsson分量严格同一l,j且无其它operator/coherence影响，单j投影仍可成立；轨道数多本身不是反例。 | original-QTR-input-and-singlej-transfer-boundary | direct-original-plus-bounded-operator-inference | SI PDF4 Calculations; SI PDF6 first two paragraphs and band-by-band wavefunctions | true |
| L22-D23-003 | 主文称标准QTR对bands1/3/4能量符合较好，但bands2/5偏高且高spin更明显；作者提出1qp/3qp相互作用或所有bands共用MoI等可能因素。这些是模型适用限制与可能解释，不是已测混合矩阵元，也不允许本任务用任意off-diagonal项为固定009最低两态补齐44keV。 | author-model-limitation-and-candidate-explanations | direct-original | main PDF5 paragraph beginning Five rotational bands | true |

[[hamamoto-2002-wobbling-excitations-odd-a-high-j-aligned-particles]] H02-D23-004和[[signature-tip-shears-discrimination-contract]]给出单j与完整l/s算符的迁移合同，不把当前ST18单jvariant的gap失败扩大成对本QTR的数值排除。没有依据standard一词补造κ/μ/Δ或原producer。

## Day23：逐线门的上游身份

本次回读SI PDF3 Figs3–5、PDF4门选择段与PDF5 Table1端点，fresh视觉PDF3、原SI SHA相符。原L22-14等人审claims保持，新条目needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L22-D23-004 | 747偏振用450门，813偏振用796门。与SI Table1端点合读，796.4为25/2−→21/2− E2，先于813.2的21/2−→19/2−；450.2的19/2−→17/2−先于747.3的17/2−→15/2−。二者是上游门；不能把“对后续光子作4π迹而恢复先发光子singles”的恒等式反过来认证目标母态取向已知。当前只是source身份与响应readiness，不证明作者忽略该效应、原P/δ有错或污染存在。 | line-bound-upstream-gate-and-response-boundary | direct-original-plus-cascade-order-inference | SI PDF3 Figs.3–4; SI PDF4 gate-selection paragraphs; SI PDF5 Table1 rows450.2/747.3/796.4/813.2 | true |

上游门的量子响应练习见[[signature-tip-shears-discrimination-contract]]，前提为[[droste-1996-pdco-formalism]] DR96-D23-003与[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D23-003；它未拟合本实验实际角环/权重或计数，不能代替原条件响应核。

## Day23：实际角组与conditional group-response的区分

本次只定向回核SI PDF1 Eq1/2与角组段，fresh视觉/原SI SHA相符；不是全文重读，旧page/claim人审范围保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L22-D23-005 | Eq1的far角组为157.6/133.6，near为75.5/104.5，并用all-detector轴相同gates。任务在声明每组为positive weighted mean后写R=ηWfar/Wnear，η为实际relative group calibration/normalizer未获值；轴对称singles中near镜角W/P相同可取消组内权重，但不取消η。用本文nominal角替代013的154/90改变conditional响应；这不等于原作者没校准、unknownη无界或actualRac已被新包络限定。 | source-angle-identity-and-declared-normalizer-boundary | direct-original-plus-task-conditional-response | SI PDF1 Eq.1–2 and preceding angle-group paragraph; task model-contract-026 | true |

任务KS应用假设、Gaussian宽度、有限门/acceptance未齐的边界仍见[[signature-tip-shears-discrimination-contract]]；不能用conditional η=1数字与本文点比较后宣布原δ/σ或jointlikelihood已复现。
