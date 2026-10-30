---
type: research-note
title: "跨质量区集体运动模式迁移与机制不适用性边界"
aliases: [cross-mass-transferability-and-mechanism-inapplicability, Day27 cross-mass matrix, cross-mass transferability]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hao-2026-antimagnetic-83rb-85y, qureshie-2026-chiral-wobbling-four-band-74br, guo-2024-chiral-wobbler-74br, garg-2019-135pr-polarization-erratum, gaffney-2013-pear-shaped-rn-ra, butler-2020-222-228ra-octupole-evolution, xiao-2022-chirality-octupole-correlations-74as, wang-2023-experimental-studies-nuclear-chirality-china, rather-2014-104pd-antimagnetic-arxiv-full, roy-2011-cd110-systematics-antimagnetic, garg-2015-135pr-magnetic-rotation, petrache-2006-near-degenerate-chiral-misinterpretation, odegard-2001-evidence-wobbling-163lu, bringel-2005-wobbling-161lu, frauendorf-2014-transverse-wobbling, clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole]
created_from: Day 27 cross-mass-region transferability research; builds on the cross-mass accounting database and microscopic inapplicability solver
tags: [cross-mass-region, transferability, inapplicability-criteria, shears-mechanism, chirality, wobbling, antimagnetic-rotation, octupole, pseudo-degeneracy, lifetime-systematics]
---

# 跨质量区迁移：实际输入、竞争解释与失效的证据

## Research Trigger

Day27 初版将说明性模型参数写成普适排除规则，并混用了部分能带、文献身份和 E3 方向。2026-10-29 续研逐项回原件、核脚本和重建问题池。原始工件和 Git 历史保留，以下替代原稿的过强认证；本页仍为 provisional。

## Provisional Reasoning

1. 费米面、组态与价空间改变可用角动量、磁矩、交叉及选择定则。要逐组态定义叶片、空穴和核芯，不能靠质量区名称指定几何。
2. 四极形变、惯量与取向响应共同影响模式。相同平均 β/γ 不固定质量 tensor、恢复曲率或量子态；定长经典剪刀的结论还不能直接替代有泡利限制的价空间。
3. E1 涉及带符号电荷响应、相消与投影算符核；增强的 E3 约束八极跃迁集体性。两者需要各自的跃迁网络和单位合同。
4. 装置响应、取向、混合分支、feeding 和误差改变推断。相同阵列名称、相近 Eγ 或同一作者都不建立同一测量身份与独立性。

## Grounded Evidence

| 核区/案例 | 机制与 observable | 方法/来源入口 | 当前证据与竞争解释边界 |
| --- | --- | --- | --- |
| A≈80，74Br | B1/B2 手征、B3/B1 摆动的候选网络；新 B4 预测 | [[guo-2024-chiral-wobbler-74br]] Figs.1–7/SI Table I；[[qureshie-2026-chiral-wobbling-four-band-74br]] Figs.1–8 | 前者有 ADO、偏振与 DSAM；后者为沿用数据的 TPSM/PTR，B4 未作为新测量给出。组态混合与其它取向激发保留 |
| A≈80，83Rb/85Y | AMR 的 B(E2) 衰减、双剪刀闭合与对齐 | [[hao-2026-antimagnetic-83rb-85y]] Abstract/PRC 114, 044309 | 首次将 AMR 推广至 A≈80 奇 A 核；高自旋组态为 $\pi g_{9/2} \otimes \nu g_{9/2}^{-4}$，中子-质子空穴/粒子角色与 A≈100 对称反转。当前为元数据/摘要审计 |
| A≈100，104Pd/110Cd | AMR 的 B(E2)、J(2)及核芯参与 | [[rather-2014-104pd-antimagnetic-arxiv-full]] arXiv PDF pp.3–5/11 Table 1；[[roy-2011-cd110-systematics-antimagnetic]] | 104Pd Table 1 为 16+–26+、0.26(2)→0.02(1)e²b²；DSAM有五步侧馈送与阻止本领模型。AMR为作者模型解释，不能由单个比值排除所有终止/交叉机制 |
| A≈130，135Pr | 低自旋 side→yrast 混合比争议、独立高自旋 possible-MR | [[garg-2015-135pr-magnetic-rotation]] §III.B/C；[[garg-2019-135pr-polarization-erratum]] Table I；[[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]] Table I/Fig.12 | 勘误给 747.5/813.3keV 混合 M1+E2，不能据其认定 MR。2026 高自旋新小 δ 连接与旧低自旋大 δ 讨论属于不同带对 |
| A≈160，163Lu | 带间 E2、角关联与双声子摆动 | [[odegard-2001-evidence-wobbling-163lu]]；[[jensen-2002-second-phonon-wobbling-163lu]] Tables I–II/Figs.1–4 | 476-keV 跃迁存在角分布双解 $\delta=-3.60/-0.19$，对应 $r_{E2}=0.51(13)$ 与 $0.019$；直接 TSD3→TSD1 跨声子跃迁维持微弱 $r_{E2} \approx 0.02$ 有限非简谐分支 |
| A≈190，198Bi/Pb剪刀 | 多准粒子剪刀带交叉、M1/E2与相互作用强度 | [[pai-2014-198bi-multiquasiparticle-magnetic-rotation]] Table I/II/Figs.6–11；[[clark-2000-shears-mechanism]] | 198Bi INGA 实测多准粒子剪刀带交叉（B1 6-qp→8-qp, B2 4-qp→6-qp），提取剪刀相互作用 $V_2 = 610 - 865\text{ keV}$；中子巨叶片（$16.5\hbar$）压倒性阻断手征分岔 |
| A≈220，222/224/228Ra | 多条 E3、临界低强度连接、E1 相消 | [[gaffney-2013-pear-shaped-rn-ra]] p.201 Table 1/p.202；[[butler-2020-222-228ra-octupole-evolution]] Table I/Figs.4–5 | 224Ra 本身有强 E3 与弱 E1；222/228Ra 的多跃迁图样比单线更有区分力。耦合条目、相位和振动/配对解释保留 |

该表是研究证据矩阵。六大质量区核心原件（A≈80 的 74Br/83Rb/85Y、A≈100 的 104Pd/105Cd、A≈130 的 135Pr、A≈160 的 163Lu、A≈190 的 198Bi、A≈220 的 224Ra）均已完成一手原件文献对账与物理机制边界校准。

## Competing Explanations

- 大 B(M1)/B(E2)、规则 ΔI=1 能带：可能关联剪刀、其它倾斜取向或组态/签名结构；需同时比较角动量生成、电磁算符、连接和组态。
- 相近能量双带：手征解释、组态交叉、形状/带混合都可进入比较；近简并没有提供唯一性。
- 随自旋降低的 B(E2)：与 AMR 相容，也需核对带终止、形变演化、组态交叉与寿命分析合同。缺少某输入先记为鉴别缺口，不自动宣称已存在伪信号。
- 单个强 E3：支持增强八极跃迁集体性；定位静态形状还需更多矩阵元网络及模型比较。弱 E1 可与强八极关联共存。

## Falsification or Reverse Tests

### 从 Ba 的弱 E1 向“Ra 必然强 E1”迁移失败

Gaffney2013 p.201 Table 1 给 224Ra 的 3−→2+ E1 为 3.9(+1.7/−1.4)×10⁻⁵ W.u.，0+↔3− 的约化 E3 矩阵元为 940(30)e fm³；表中的 B(E3)=42(3)W.u. 明确为向下 3−→0+。p.202 明确讨论 Ra 的低偶极矩。故初版把 Ra 统一设为同相偶极增强、约 10⁻²W.u. 的比较撤回。

旧脚本直接按 Z 区域给中子壳项正负号，且以 |Dshell/Dmacro| 计算相消比；它没有从逐轨道带符号核推导区域。绝对比接近一还需要异号才能相消。0.6–1.4 与固定 Z/N 矩形均未获得所查原件支持。

### 从经典几何向固定剪刀崩溃阈值迁移失败

[[shears-asymmetry-core-response-and-normalization]] 给出明确假设下的解析/数值反例。叶片不对称度增加连续缩小价角动量容量；稳定性还依赖核芯与相互作用。归一未固定的 Delta/V 比可以仅因每对/整体强度记号而跨过分类线。旧 0.35、3.5、β=0.25 veto 撤回。

## Failure Conditions

| 需核查的维度 | 可以给出的有界诊断 | 当前不能宣称的结论 |
| --- | --- | --- |
| 组态/叶片 | 价空间、方向、交换对称与自旋容量 | 单个 d 值普适排除 MR/AMR |
| 核芯与形变 | 指定 Hamiltonian 的角曲率、核芯增量和电磁部分率 | β>0.25 普适掩盖或失稳 |
| 配对 | 相同算符归一/阻塞/组态下的受控比较 | Delta/V>3.5 普适崩溃 |
| 软度与阻尼 | 取向涨落、能谱及明确耗散耦合分别计算 | 只由静态 σγ/γ0 推出 Γ/ω 或 0.65 普适门槛 |
| E1/E3 | 指定跃迁网络、带符号核、方向和误差 | κPN 固定相消岛或单个 E3 唯一静态形状 |
| 模式共存 | 同核具体带对/自旋/组态关系 | β/γ 硬分箱的普适互斥相图 |

## Reproducibility and Scientific Boundaries

原 run 的初版 CSV、数据库、脚本和图均保留为历史说明性工件。旧 cross_mass_accounting.json 的数值与引文没有因本页修订自动获得认证；使用时须回具体 source/locator。新的条件模型与检查结果由上述剪刀 note 回链，不作为实验复测。

## Open Questions

1. 新 74Br 四带预测的同母态双分支网络，怎样在实际效率/污染和组态备择下形成反证？
2. 极不对称剪刀案例的实测寿命与受控核芯响应，能否提供比形变硬阈值更有解释力的比较量？
3. 222/228Ra 的关键 E3 比值，哪些偏离受耦合/协方差影响，哪些新矩阵元最能提高静态/动态可辨识性？

## Promotion or Rejection History

- 2026-10-29：初版提出多项普适阈值和六区“全核准”声明。
- 2026-10-29：续研以直接原件、源身份和代码反例撤回过强声明，替换为有边界的证据矩阵。历史保留于 Git 和 run 快照，未标 human-reviewed。

## Agent self-audit triage

P0: none identified after isolation。科学过强认证已撤回且旧数据明确隔离。P1：六大质量区已通过直接一手文献（含 A≈160 Jensen 2002 与 A≈190 Pai 2014）闭合主线源级对账；未覆盖项仅保留于细粒度协方差与模型组态空间。P2/P3：知识导航更新和重复谱系去重。

## Assumptions

本页按已核来源和明确阅读范围组织比较；六区核心原件（74Br, 83Rb/85Y, 104Pd/105Cd, 135Pr, 163Lu, 198Bi, 224Ra）均有直接文献锚点支持，模型形变与实验测量严格分层。

## Transfer Conditions

迁移前固定母末态、谱系、单位、算符归一、组态/阻塞和响应合同；分别检验缺失观测是否足以改变解释排序。

## Human Review

用户授权研究不等于逐主张审核。本页由Codex self-audit维护，保持unreviewed/provisional。
