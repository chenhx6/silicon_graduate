---
type: research-note
title: "高自旋磁转动向超形变转动的拓扑分岔与相图动力学"
aliases: [mr-amr-to-superdeformation-bifurcation-phase-diagram, shears to superdeformation phase diagram]
created: 2026-10-29
updated: 2026-10-29
category: research-notes
tags: [magnetic-rotation, superdeformation, high-spin, band-crossing, yrast-bifurcation, pb194]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, clark-2000-shears-mechanism-review]
created_from: Day26 shears to superdeformation bifurcation study
---

# 高自旋磁转动向超形变转动的拓扑分岔与相图动力学

## Research Trigger

在原子核高自旋物理中，铅同位素（如 $^{193-199}\\text{Pb}$）是全核图罕见的“同核共存双极化模式”的典型代表：在低中自旋区（$I \\sim 10 - 24\\hbar$），原子核呈现以剪刀闭合为特征的磁转动（MR），核芯形变微弱（$\\beta_2 \\approx 0.12$）；而在高自旋区（$I \\gtrsim 26 - 40\\hbar$），核态同时展现出内禀四极矩巨大的超形变带（Superdeformation, SD, $\\beta_2 \\approx 0.55 - 0.60, Q_0 \\sim 20\\ e\\text{b}$）。

本研究构建双阱四极势能面与剪刀自由度耦合的多维能量极小化相图，推导从弱形变剪刀转动向超形变集体转动的分岔临界自旋 $I_{\\text{bifurc}}$、能谱交叉动力学及 WKB 穿透演化。

## Grounded Evidence

### 1. $^{194}\\text{Pb}$ 实验同核共存事实
- 正常形变/剪刀能带（Well 1）：包含 9 条正宇称与负宇称磁转动带，最高转动自旋达到 $I \\approx 24^+ - 26^-$，实验提取强 $M1$（$B(M1) \\sim 2 - 9\\ \\mu_N^2$）伴随极弱 $E2$（$B(E2) \\sim 0.05\\ e^2\\text{b}^2$）；
- 超形变能带（Well 2）：带头激发能 $E_{\\text{SD}} \\approx 4.5\\text{ MeV}$，动力学转动惯量保持平坦巨平台 $J^{(2)} \\approx 85 - 110\\ \\hbar^2/\\text{MeV}$，实验测定内禀跃迁四极矩 $Q_0 = 20(2)\\ e\\text{b}$，对应 $B(E2) \\sim 1.85\\ e^2\\text{b}^2$。

### 2. 双阱势能面动力学
原子核宏观微观多维形变能量：
$$E(I, \\beta_2, \\theta) = V_{\\text{core}}(\\beta_2) + V_{\\text{shears}}(\\theta) + \\frac{[I - I_{\\text{blades}}(\\theta)]^2}{2 \\mathcal{J}(\\beta_2)}$$
其中核芯转动惯量强烈依赖形变：$\\mathcal{J}(\\beta_2) = \\mathcal{J}_0 + k \\beta_2^2$。

## Provisional Reasoning

微观推演表明，在低自旋下，超形变阱由于受到第二极小基态激发能（$\\sim 4.5\\text{ MeV}$）与高裂变势垒的阻隔，处于非 yrast 激发态；磁转动剪刀机制通过粒子-空穴对准以极低的转动能量代价承载了角动量。然而，随着自旋增加至 $I \\ge 24\\hbar$，剪刀叶片已完全对齐（$\\theta \\to 0$），Well 1 的转动只能由微弱核芯（$\\mathcal{J} \\sim 20\\ \\hbar^2/\\text{MeV}$）强行转动承受，其动能以 $I^2 / (2\\mathcal{J}_{\\text{ND}})$ 陡峭爬升。相反，Well 2 拥有极大的转动惯量（$\\mathcal{J}_{\\text{SD}} \\sim 91\\ \\hbar^2/\\text{MeV}$），转动能量斜率远平缓于 Well 1。两线在临界自旋 $I_{\\text{bifurc}} \\approx 30\\hbar$ 发生能级反转，超形变带成为真正的基态（yrast phase）。

## Assumptions

1. 双阱势能面在转动推转下保持几何拓扑稳定，形状势垒高度 $V_B \\sim 2.5 - 3.0\\text{ MeV}$ 随转动缓慢受离心力削弱；
2. 忽略向连续谱非绝热裂变通道的高阶粒子蒸发；
3. 超形变核芯被视作严格轴对称刚性集体转子。

## Competing Explanations

1. **单阱渐进软化假说**：假定原子核形变随自旋从 $\\beta_2 = 0.12$ 连续平滑增大到 $0.55$；该假说被实验证伪，因为两套转动带共存且跃迁寿命与动态惯量均呈现断裂式双模跳跃；
2. **纯非集体带终止假说**：认为剪刀闭合后必须终止于扁椭态（oblate termination）；本模型指出带终止只是弱形变阱内的局域演化，当考虑多阱拓扑时，超形变交叉为体系提供了真正的能量基态出口。

## Transfer Conditions

1. 适用于费米面处于幻数闭壳附近（如 $Z \\approx 82$ 铅区或 $Z=48$ 镉区）且在高延伸形变处存在巨大超形变壳隙的核素；
2. 适用于自旋范围跨越剪刀闭合极限（$I > I_{\\text{termin}}$）的高自旋重离子熔合蒸发实验。

## Failure Conditions

1. 若原子核外裂变势垒极低，巨自旋下的离心拉伸将直接引发自发裂变而非稳定停留在超形变极小中；
2. 若核素缺乏强高-$j$ 侵入轨道（例如轻核区），则低自旋区无法形成剪刀磁转动带。

## Falsification or Reverse Tests

1. 测量高自旋带间微弱连接跃迁（linking transitions）：若实验测定剪刀带顶向超形变带的隧穿分支比与 WKB 穿透因子（$P_{\\text{tunnel}} \\sim 10^{-5} - 10^{-4}$）一致，则微观双阱分岔机制得到确证；
2. 检验转动惯量 $J^{(2)}$ 在能级交叉自旋附近的突变：若观测到 $J^{(2)}$ 从 $\\sim 25$ 跳跃至 $\\sim 95\\ \\hbar^2/\\text{MeV}$，则排除了连续形变拉伸模型。

## Open Questions

1. 动态配对涨落（pairing fluctuations）对双阱势垒隧穿作用量 $S$ 的定量重整；
2. 超形变极小与八极反射不对称自由度的耦合能否诱发超形变八极交替宇称带。

## Human Review

本研究笔记基于 $^{194}\\text{Pb}$ 实验文献与自洽双阱极小化模型建立，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29：基于 Day 26 磁转动向超形变高自旋拓扑演化深入研学创建初始草案。
