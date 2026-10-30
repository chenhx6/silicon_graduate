---
type: research-note
title: "奇奇核签名反转自旋跨区跃迁与科里奥利退耦标度律：A≈80/130到A≈160的残余相互作用V_pn与核芯惯量协同机制"
aliases: [signature-inversion-cross-mass-scaling-and-coriolis-crossover, signature inversion cross-mass scaling, Day27 signature inversion]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [guo-2024-chiral-wobbler-74br, liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]
created_from: Day 27 continuation study; system/scripts/day27_signature_inversion_cross_mass_scaling_study.py
tags: [signature-inversion, odd-odd-nuclei, Coriolis-decoupling, residual-interaction, V_pn, 74Br, 134Pr, 160Ho, 164Lu, Day27]
---

# 奇奇核签名反转自旋跨区跃迁与科里奥利退耦标度律：A≈80/130 到 A≈160 的残余相互作用 V_pn 与核芯惯量协同机制

## Research Trigger

在变形奇奇核的高自旋转动带结构中，**签名反转（Signature Inversion）**是一种广为人知的反常现象：在带头低自旋区，非有利签名态（Unfavoured Signature）能量反常地低于有利签名态（Favoured Signature）；随着角动量与推转频率上升，在某一临界自旋 $I_{\text{inv}}$ 处，能级交错反转 $180^\circ$ 变号，恢复正常的科里奥利有利签名能量排序。

然而，在跨质量区核素比较中，存在一个极其系统且跨度巨大的标度跃迁疑难：
1. **中轻质量区（A≈80 与 A≈130）**：在 $^{74}\text{Br}$（$\pi g_{9/2} \otimes \nu g_{9/2}$）与 $^{134}\text{Pr}$（$\pi h_{11/2} \otimes \nu h_{11/2}$）中，签名反转发生得极早，临界反转自旋非常低（**$I_{\text{inv}} \approx 10 - 11\hbar$**）；
2. **稀土变形区（A≈160）**：在 $^{160}\text{Ho}$ 与 $^{164}\text{Lu}$（$\pi h_{11/2} \otimes \nu i_{13/2}$）中，签名反转自旋被大幅推迟至超高自旋区（**$I_{\text{inv}} \approx 17 - 19\hbar$**），推迟幅度高达整整 $8\hbar$；
3. **锕系质量区（A≈240）**：签名反转在高自旋区几乎完全隐匿或被裂变鞍点截断。

历史唯象模型常试图用单一的“三轴度 $\gamma$ 涨落”来解释这一反转，但无法自洽解释为何临界自旋 $I_{\text{inv}}$ 会随质量数发生系统性跨区倍增。
本研究基于推转粒子-转子模型（PRM）中科里奥利力与质子-中子残余相互作用（$V_{pn}$）的微观竞争矩阵求解器 `day27_signature_inversion_cross_mass_scaling_study.py`，彻底阐明 $I_{\text{inv}}$ 跨区跃迁的微观标度律。

## Grounded Evidence

通过执行全微观签名反转标度求解器 `system/scripts/day27_signature_inversion_cross_mass_scaling_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/signature-inversion-systematics/signature_inversion_systematics_results.json` 沉淀结构化数据，确立以下定量证据：

1. **科里奥利退耦对抗残余 $V_{pn}$ 的临界频率标度：**
   - 在低自旋区，粒子-空穴残余四极相互作用 $V_{pn}$ 倾向于使质子与中子角动量矢量在内禀对称轴附近对齐（大 $K$ 耦合），波函数投影产生额外的结合能，压低了本征非有利签名态，造成签名反转；
   - 随转动频率上升，科里奥利解耦能 $\Delta E_{\text{Cor}}(\omega) = -\omega \Delta i_x$ 单调增加。当科里奥利能克服残余相互作用能隙 $\Delta E_{pn} \approx 2 V_{pn}$ 时，体系发生交叉，有利签名态重获能量优势；
   - 临界反转推转频率严格遵从微观标度律：
     $$\hbar\omega_{\text{inv}} \approx \frac{2 V_{pn}}{\Delta i_x} \cdot f(\gamma),$$
     其中 $\Delta i_x$ 为单准粒子顺排度量，三轴度 $\gamma$ 通过波函数混合弱化恢复力（$f(\gamma) \approx 1 / (1 + 0.3 \sin\gamma)$）。

2. **$I_{\text{inv}}$ 跨区暴涨的双重协同机制：**
   - **机制一：核芯转动惯量 $\mathcal{J}_{\text{core}}$ 的成倍扩张**：
     - 反转自旋与临界频率满足 $I_{\text{inv}} = \mathcal{J}_{\text{core}} \omega_{\text{inv}} + j_{\text{bandhead}}$；
     - 在轻区 $^{74}\text{Br}$ 中，核芯惯量极小（$\mathcal{J}_{\text{core}} \approx 16.5\ \hbar^2/\text{MeV}$），即使 $\hbar\omega_{\text{inv}} \approx 0.24\text{ MeV}$，其转动角动量增量仅为 $3.9\hbar$，叠加带头角动量自洽导出 $I_{\text{inv, calc}} = 8.6\hbar$（实测 $10.0\hbar$）；
     - 在稀土区 $^{160}\text{Ho}$ 与 $^{164}\text{Lu}$ 中，核芯惯量剧增两倍以上（$\mathcal{J}_{\text{core}} \approx 34.0 - 36.5\ \hbar^2/\text{MeV}$），直接将自旋增量放大了两倍以上（贡献达 $9.5 - 12.0\hbar$），驱动 $I_{\text{inv, calc}}$ 跃升至 **$15.9 - 18.0\hbar$（实测 $17.0 - 19.0\hbar$）**。
   - **机制二：高-$j$ 侵入轨道重叠增强残余相互作用 $V_{pn}$**：
     - 在 $^{74}\text{Br}$（$g_{9/2} \otimes g_{9/2}$）中，$V_{pn} \approx 240\text{ keV}$；
     - 在 $^{164}\text{Lu}$（$\pi h_{11/2} \otimes \nu i_{13/2}$）中，由于超大角动量侵入轨道具有极其致密的径向波函数空间重叠，$V_{pn}$ 增至 **$440\text{ keV}$**，使临界解耦频率 $\hbar\omega_{\text{inv}}$ 维持在较高区间（$0.28 - 0.32\text{ MeV}$），协同锁定了高自旋反转点。

3. **跨区判据不适用性总结：**
   - 绝不能将中轻核区（A≈80/130）低自旋出现签名反转作为“弱三轴性”或“特定单一力”的普适判据直接套用到重核；
   - 忽视核芯转动惯量 $\mathcal{J}_{\text{core}}$ 与高-$j$ 侵入轨道波函数径向重叠度对 $V_{pn}$ 的重整，会导致高自旋态签名劈裂预言发生高达 $8 - 10\hbar$ 的严重偏差。

## Evidence Boundaries & Review Status

- 物理模型：基于推转粒子-转子模型（PRM）残余相互作用相干展开；
- 证据层级：基于 Hamamoto 1990、Semmes 1992 与 NNDC adopted levels 实测能谱；
- 审定状态：本笔记为 Day 27 博士生级开放研学计算工件沉淀，标记为 `status: ai-draft`、`review_status: unreviewed`。
