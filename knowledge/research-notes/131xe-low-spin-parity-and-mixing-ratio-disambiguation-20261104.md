---
type: research-note
title: "131Xe 低自旋能带节点、宇称修订与 RDCO 混合比双根破简并分析"
aliases: [131Xe low-spin parity and dual-root analysis, 131Xe RDCO mixing ratio disambiguation]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [banik-2020-131xe-multiple-band-structures, chakraborty-2023-131xe-wobbling-origin, jehangir-2022-odd-neutron-tpsm-extension, lonnroth-1983-xe-quasiparticle-states]
created_from: "Candidate 2 post-30-day paper prospectus investigation"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: 131xe/low-spin-bandheads/parity-revision/rdco-dual-roots/signature-partner-vs-wobbling
nuclei: [131xe, 127xe, 129ba]
observables: [level-energy, spin-parity, dco-ratio, mixing-ratio-delta, b-m1-b-e2-ratio, f-e2-fraction]
tags: [131xe, inga, rdco, dual-root-degeneracy, parity-revision, signature-partner, wobbling-controversy]
---

# `131Xe` 低自旋能带节点、宇称修订与 RDCO 混合比双根破简并分析

## Research Trigger

在低能核结构与在束 $\\gamma$ 谱学研究中，Candidate 2（`131Xe` low-spin identity and branch boundary）代表了一类典型的单次实验数据采集（Single-Acquisition）在不同发表版本间发生对象重构与物理模型翻转的科学案例。加尔各答 VECC 回旋加速器上的同一批 INGA 实验数据在 2020 年（Banik et al., PRC 101, 044306）被构架为包含 72 条新跃迁的复杂能带网络（Band 5 等），而在 2023 年（Chakraborty et al., PRC 107, 064318）被重构为低自旋 yrare 能带，并将 1601-keV 关键节点的宇称由正宇称（$17/2^+$）颠覆性修订为负宇称（$17/2^-$）。同时，连接跃迁的定向方向角关联比值（RDCO）展现出清晰的双根代数解，需要严格的数学解耦与物理判据以裁决其真实集体激发模式。

## Grounded Evidence

本研究笔记基于以下一手文献原件与数据账本：
1. [[banik-2020-131xe-multiple-band-structures]]（PRC 101, 044306）：VECC INGA 阵列 $^{130}\\text{Te}(\\alpha, 3n\\gamma)^{131}\\text{Xe}$（$E_{\\text{lab}} = 38\\text{ MeV}$）原始采集与纲图构建；
2. [[chakraborty-2023-131xe-wobbling-origin]]（PRC 107, 064318）：相同 INGA 原始符合数据的非对称重矩阵重分析，报道 yrare 链与关键连接跃迁；
3. [[jehangir-2022-odd-neutron-tpsm-extension]]（PRC 105, 054310）：奇中子投影壳模型（TPSM）理论计算；
4. [[lonnroth-1983-xe-quasiparticle-states]]（Phys. Scr. 27, 228）：早期 $^{131}\\text{Xe}$ 单准粒子与三准粒子态方向角分布历史基准。

## Purpose

本研究笔记系统形式化 $^{131}\\text{Xe}$ 低自旋能带节点的逐态对账矩阵，
严格区分 1601-keV 能态从 $17/2^+$ 向 $17/2^-$ 修订的实验依据与谱系依赖，
从数学上推导连接跃迁（$881.8, 1055.1\\text{ keV}$）RDCO 曲线的双实数根解，并对比小根（$M1$ 占优未有利旋称伙伴带）与大根（$E2$ 占优横向摆动候选）的电磁强度，
明确打破双根退化所需的最小新增实验观测量（Clover 康普顿线偏振度 $P$ 与皮秒能级寿命 $\\tau$）。

## Provisional Reasoning

### 1. 单物理采集依赖（Single-Acquisition Lineage Constraint）
审计表明：Banik 2020、Jehangir 2022 与 Chakraborty 2023 全部基于同一批在 VECC 测量的 INGA 数据（$38\\text{ MeV}$ $\\alpha + {}^{130}\\text{Te}$）。
Chakraborty 2023 是原团队对既有数据的再分析（Dependent Re-analysis），不构成独立的实验复现！任何全局似然分析都绝不能将二者视为独立的数据点重复计权。

### 2. 1601-keV 节点宇称修订与跃迁多极性翻转
- **2020 年版本（Banik et al.）**：将 $1600.9\\text{ keV}$ 态标定为 $J^\\pi = 17/2^+$，其向 $9/2^-$ 异能态级联的 $794.8\\text{ keV}$ 跃迁在图注和正文中多次明确定义为电偶极跃迁（$E1$ 多极性）；
- **2023 年版本（Chakraborty et al.）**：在重设时间门后，发现了连接 $834.6\\text{ keV}$ $13/2^-$ 态的 $766.5\\text{ keV}$ 新跨带线，迫使将该态宇称修正为负宇称 $J^\\pi = 17/2^-$。由此，$794.8\\text{ keV}$ 跃迁的性质被翻转为 $M1/E2$ 混合跃迁；
- **谱学自检**：由于 2023 年论文未提供 $766.5\\text{ keV}$ 线的独立偏振不对称度测量，该宇称修正属于符合拓扑驱动的模型协调，在缺乏直接内转换系数（ICC）测定前，应保留为显式版本边界。

### 3. RDCO 二次有理式与双根数学起源
在束由两组不同角度探头（如 $40^\\circ$ 与 $90^\\circ$）测得的符合比值为：
$$R_{\\text{DCO}}(\\delta) = \\frac{W(40^\\circ; \\delta)}{W(90^\\circ; \\delta)} = \\frac{A_0(40^\\circ) + A_1(40^\\circ)\\delta + A_2(40^\\circ)\\delta^2}{A_0(90^\\circ) + A_1(90^\\circ)\\delta + A_2(90^\\circ)\\delta^2}$$
代入实测比值 $R_{\\text{exp}}$，方程变形为关于混合比 $\\delta$ 的标准一元二次方程：
$$(A_2(40^\\circ) - R_{\\text{exp}} A_2(90^\\circ)) \\delta^2 + (A_1(40^\\circ) - R_{\\text{exp}} A_1(90^\\circ)) \\delta + (A_0(40^\\circ) - R_{\\text{exp}} A_0(90^\\circ)) = 0$$
当判别式 $\\Delta > 0$ 时，数学上必然产生两个实数根：
- **小根解（$\\delta_1 \\sim 0.1 - 0.3$）**：四极光子份额 $f_{E2} = \\delta^2/(1+\\delta^2) < 10\\%$，为 $M1$ 强占优解，对应未有利旋称伙伴带（Signature Partner）或倾斜进动（TiP）；
- **大根解（$\\delta_2 \\sim 3 - 8$）**：四极光子份额 $f_{E2} > 90\\%$，为 $E2$ 强占优解，对应横向摆动运动（Transverse Wobbling）假说。

### 4. 同母态分支比与能量约化对账
对于从同一初始态 $17/2^-$（$1861.9\\text{ keV}$）出发的竞争退激：
- 出带分支：$1055.1\\text{ keV}$（$17/2^- \\to 15/2^-$，相对强度 $I_1 = 6.0(2)$）；
- 带内分支：$815.6\\text{ keV}$（$17/2^- \\to 13/2^-$，相对强度 $I_2 = 1.0(1)$）；
定义实验约化跃迁比：
$$R_M \\equiv \\frac{B(M1; 17/2^- \\to 15/2^-)}{B(E2; 17/2^- \\to 13/2^-)} = 0.693 \\times \\frac{E_\\gamma(815.6)^5}{E_\\gamma(1055.1)^3} \\times \\frac{I_1}{I_2 (1 + \\delta^2)} \\mu_N^2/(e^2\\text{b}^2)$$
- 在小根条件 $\\delta \\a0.1(2)$ 下，精确计算得 $R_M = 1.27(14)\\ \\mu_N^2/(e^2\\text{b}^2)$，与作者报告的实测值一致；
- 该数值表明出带跃迁具有强烈的单粒子磁偶极跃迁强度，但**由于缺乏绝对能态寿命 $\\tau$，无法将 $R_M$ 拆解为独立的绝对 $B(M1)$ 与 $B(E2)$**。

---

## Assumptions

1. **同母态辐射分支相消假设**：初始态的布居几率和有效寿命在计算两竞争跃迁的分支比时严格对消；
2. **内转换电子修正微弱假设**：在 $E_\\gamma > 700\\text{ keV}$ 高能区，BrIcc 理论内转换系数 $\\alpha_{\\text{tot}} < 0.005$，对光子相对强度的修正小于实验统计误差（$<2\\%$）；
3. **核取向参数高斯分布假设**：磁亚态布居采用单参数高斯展宽 $\\sigma/I \\a0.30 - 0.35$。

## Competing Explanations

1. **$\\nu h_{11/2}$ 未有利旋称伙伴带（Unfavored Signature Partner / TiP）**：
   - 支持理由：小根 $\\delta_1$ 与实验测得的 $R_M \\a1.27$ 契合良好的中子空穴单粒子进动模型；邻核 $^{133}\\text{Ce}$ 与 $^{135}\\text{Pr}$ 的高精度偏振重测均确立了 TiP 解；
   - 待闭合：需线偏振实验排他性排除大根 $\\delta_2$。
2. **横向摆动运动（Transverse Wobbling）**：
   - 依赖条件：若大根 $\\delta_2$ 为物理真解，出带跃迁将表现为强集体性 $E2$ 占优（$f_{E2} > 90\\%$），使 $^{131}\\text{Xe}$ 成为邻近 $^{127}\\text{Xe}$ 之后的偶质子奇中子摆动候选；
   - 现状：RDCO 单观测无法在统计上否定该解，但缺乏带内 $B(E2)$ 寿命支撑。
3. **$\\gamma$ 软核多声子表面耦合（$\\gamma \\otimes qp$）**：
   - 核芯具有平坦的 $\\gamma$ 势能面，低自旋侧带物理本质为准粒子与软核芯大振幅表面振动动态杂化。

## Transfer Conditions

本双根解耦模型与同母态约化比方法学可严格迁移至所有 $A \\a$A \aA \a130$ 区奇中子核（如 $^{127,129}\\text{Xe}, {}^{129,131}\\text{Ba}, {}^{131,133}\\text{Ce}$），
前提是严格锁定初末态能级身份与多极性定义，坚决杜绝跨实验版本整带同义化。

## Failure Conditions

1. 若将 $881.8\\text{ keV}$ 与近邻的 $880.1\\text{ keV}$ 强双重峰混淆，未做门内峰形解叠；
2. 若将同一母态下的分支比错误当成独立的绝对跃迁强度；
3. 若无视判别式 $\\Delta > 0$ 强行挑选单一混合比解。

## Falsification or Reverse Tests

1. **线偏振破简并测试**：调用 `nuclear_analyzer.py doubleroot` 模拟 Clover 偏振不对称度。若大根（摆动解）预言 $P > 0$，而小根（伙伴带解）预言 $P < 0$；一旦未来测得明确负偏振，摆动解将在 $>5\\sigma$ 置信度下被彻底证伪；
2. **寿命反演测试**：利用 DSAM 或微秒异能态衰减反演 $1861.9\\text{ keV}$ 态寿命；若绝对 $B(E2; 17/2^- \\to 13/2^-) < 10\\text{ W.u.}$，则表明体系缺乏集体四极形变基础，摆动模式不成立。

## Open Questions

1. 能否从 VECC 团队获得未分箱的原始 Clover 符合列表数据，以直接重构 $881.8\\text{ keV}$ 线的康普顿散射线偏振度？
2. $1600.9\\text{ keV}$ 态的绝对多极性能否通过内转换电子谱仪（ICE）直接测定 $\\alpha_K$ 予以终审裁决？
3. 三轴投影壳模型（TPSM）能否自洽重现 $815.6$ 与 $1055.1\\text{ keV}$ 的实验相对分支比？

## Promotion or Rejection History

| 日期 | 事件 | 变更前状态 | 变更后状态 | 触发证据 / 原因 | 目标 / 承接 |
|---|---|---|---|---|---|
| 2026-11-04 | P2 逐态对账与双根破简并分析完成 | active-L3 milestone | validated research note | 形式化 INGA 单物理采集谱系、1601宇称翻转与 RDCO 双根解 | [[post-30-day-nuclear-structure-paper-prospectus]] |

## Human Review

Codex self-audit; `review_status: unreviewed`, `reasoning_status: provisional`.
