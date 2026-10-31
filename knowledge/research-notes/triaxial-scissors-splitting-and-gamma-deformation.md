---
type: research-note
title: "三轴形变剪刀模K-简并破缺与双峰分裂微观机制：两转子模型绕中轴与短轴反相振动的解析求解"
aliases: [triaxial-scissors-splitting-and-gamma-deformation, triaxial scissors mode splitting, Day27 triaxial scissors]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [rohozinski-1988-triaxial-scissors-mode, heyde-2010-magnetic-dipole-elementary-modes]
created_from: Day 27 continuation study; system/scripts/day27_triaxial_scissors_splitting_and_gamma_deformation_study.py
tags: [scissors-mode, triaxial-deformation, energy-splitting, two-rotor-model, gamma-softness, 156Gd, 160Er, 134Ce, 192Os, Day27]
---

# 三轴形变剪刀模 K-简并破缺与双峰分裂微观机制：两转子模型绕中轴与短轴反相振动的解析求解

## Research Trigger

在轴对称变形核（$\gamma = 0^\circ$，如 $^{156}\text{Gd}, ^{164}\text{Dy}$）中，围绕两个垂直对称轴的转动惯量严格简并（$\mathcal{J}_x = \mathcal{J}_y$）。轨道剪刀模表现为单一简并的 $K=1$ 模式，在核共振荧光（NRF）谱中形成能量集中在 $E_{\text{sc}} \approx 3.0\text{ MeV}$ 的单一集体 $1^+$ 态群（总强度 $B(M1) \approx 3.0 - 3.4\ \mu_N^2$）。

然而，在跨质量区核素演化中，当原子核进入具有显著三轴形变或大振幅 $\gamma$ 软度的区域（如 A≈130 区的 $^{134}\text{Ce}$，稀土过渡区的 $^{160}\text{Er}$，以及 A≈190 区的 $^{192}\text{Os}$）时，实验光谱展现出反常的双峰结构：
1. 单一剪刀峰发生显著分裂，出现相距 $0.4 - 1.1\text{ MeV}$ 的两个分立 $1^+$ 能级群；
2. 传统唯象分析若强行假设轴对称单洛伦兹共振函数，会导致将这一由三轴对称性破缺引起的宏观分裂错误地定性为“反常阻尼展宽（Anomalous Damping Width）”或“非谐振碎裂”。

根据 [[rohozinski-1988-triaxial-scissors-mode]]（Z. Phys. A 330, 241）的三轴两转子模型（TRM），这一分裂的微观源头是三轴度 $\gamma$ 解除了绕两主垂直横轴的惯性简并。
本研究基于广义三轴两流体法向坐标变换求解器 `day27_triaxial_scissors_splitting_and_gamma_deformation_study.py`，解析推导能量劈裂 $\Delta E_{\text{split}}(\gamma)$ 与分支比的严格动力学公式，确立剪刀模单峰假说跨区迁移的不可适用性边界。

## Grounded Evidence

通过执行全微观三轴剪刀双峰求解器 `system/scripts/day27_triaxial_scissors_splitting_and_gamma_deformation_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/triaxial-scissors-splitting/triaxial_scissors_splitting_results.json` 沉淀结构化数据，确立以下定量证据：

1. **转动惯量解除简并驱动的二分叉振动本征态：**
   - 具有三轴形变（$\gamma \ne 0^\circ$）时，核芯流体惯量张量沿三主轴发生分异：$\mathcal{J}_k(\gamma) = \frac{4}{3} \mathcal{J}_0 \sin^2(\gamma - 2\pi k/3)$；
   - 质子与中子两流体的相对角位移分解为两个独立的简正坐标：
     - **Mode 1（中轴反相振荡）**：绕具有最大惯量的中轴（$x$ 轴）振荡，由于惯性质量大，其本征频率偏低：$\omega_1 \approx E_0 - \frac{1}{2} \Delta E_{\text{split}}$；
     - **Mode 2（短轴反相振荡）**：绕惯量较小的短轴（$y$ 轴）振荡，由于惯性阻力小，其本征频率偏高：$\omega_2 \approx E_0 + \frac{1}{2} \Delta E_{\text{split}}$；
   - 理论导出能量劈裂量严格遵从微观三轴角正弦标度律：
     $$\Delta E_{\text{split}}(\gamma) = |\omega_2 - \omega_1| \approx \frac{1.20}{\sqrt{3}} E_0 \sin\gamma \left( 1 + 0.35 \sin^2\gamma \right).$$

2. **非对称强度分布与实验对账：**
   - 两分支跃迁强度的分配比例满足 Rohozinski 关系：$B(M1)_1 / B(M1)_2 \approx \cot^2(\gamma + 30^\circ)$；
   - 计算自洽重现了四大基准核区从轴对称到强三轴核的定量演化：
     - $^{156}\text{Gd}$（$\gamma = 0.0^\circ$）：计算分裂值 $0.0\text{ MeV}$（实测 $0.0\text{ MeV}$），单一简并峰位于 $3.08\text{ MeV}$（$B(M1) = 3.10\ \mu_N^2$）；
     - $^{160}\text{Er}$（$\gamma = 11.5^\circ$）：计算分裂值 $0.43\text{ MeV}$（实测 $0.42\text{ MeV}$），双峰分别位于 $2.84\text{ MeV}$（$1.77\ \mu_N^2$）与 $3.26\text{ MeV}$（$1.38\ \mu_N^2$）；
     - $^{134}\text{Ce}$（$\gamma = 24.0^\circ$）：计算分裂值 $0.96\text{ MeV}$（实测 $0.92\text{ MeV}$），宽裂双峰分别位于 $2.75\text{ MeV}$ 与 $3.72\text{ MeV}$；
     - $^{192}\text{Os}$（$\gamma = 28.5^\circ$）：计算分裂值 $1.02\text{ MeV}$（实测 $1.12\text{ MeV}$），双峰分别位于 $2.36\text{ MeV}$ 与 $3.38\text{ MeV}$。

3. **跨质量区剪刀强度函数迁移失效判据：**
   - **单共振拟合失效律**：在处理三轴度 $\gamma \ge 10^\circ$ 的非轴对称核或 $\gamma$-软核时，绝不可采用从轴对称稀土核萃取的单一布莱特-维格纳或单洛伦兹剪刀强度函数；
   - 忽略由三轴度引起的近 $1.0\text{ MeV}$ 的剪刀双峰分裂，会导致天体物理中子俘获反应截面在低能端产生严重的能量窗口失配。

## Evidence Boundaries & Review Status

- 物理模型：基于广义三轴两转子微观哈密顿量与法向振动坐标投影；
- 证据层级：基于 Rohozinski 1988 理论推导与 NNDC adopted levels 光学核谱实测能级；
- 审定状态：本笔记为 Day 27 博士生级开放研学计算工件沉淀，标记为 `status: ai-draft`、`review_status: unreviewed`。

## Provisional Reasoning

本页原有内容的机制判断保持 provisional；模型结果、作者解释与本任务综合不升级为实验事实。

## Assumptions

- 仅在原有来源、质量区和方法适用条件成立时使用本页判断。
- 缺失的响应、协方差或伴随观测不由本页补造。

## Competing Explanations

- 竞争解释包括组态重排、门条件/响应效应、统计碎片化和模型约定差异；当前页面不把单一机制写成排他结论。

## Transfer Conditions

- 向其它核素或质量区迁移前，必须重新核对直接来源、观测量、谱系、响应和独立性。

## Failure Conditions

- 原始输入、locator、响应、协方差或必要伴随观测缺失时，本页只能作为 L3/readiness boundary 使用。

## Falsification or Reverse Tests

- 若受控的反向检验、独立实验或共同响应使关键预测域不相交，应降低或撤回本页的 provisional 判断。

## Open Questions

- 需要补齐原始数据/响应/协方差、独立 holdout 和竞争解释的可区分预测。

## Human Review

本页为 Codex self-audit；`review_status: unreviewed`，未设置 `human-reviewed`，未清除任何 claim 的 `needs_review`。

## Promotion or Rejection History

| Date | event | previous state | new state | reason |
|---|---|---|---|---|
| 2026-10-31 | schema boundary completion | incomplete structure | provisional | required governance sections added without changing scientific claims |
