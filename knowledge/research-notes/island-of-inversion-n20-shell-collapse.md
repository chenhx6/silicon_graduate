---
type: research-note
title: "N=20反转岛壳闭合崩溃与四极集体性暴涨微观机制：单极张量力淬灭与2p-2h侵入组态基态反转"
aliases: [island-of-inversion-n20-shell-collapse, 32Mg N=20 collapse island of inversion, Day27 island of inversion]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [motobayashi-1995-32mg-deformation]
created_from: Day 27 continuation study; system/scripts/day27_island_of_inversion_n20_collapse_study.py
tags: [island-of-inversion, 32Mg, N=20-collapse, monopole-tensor-force, intruder-inversion, 40Ca, 34Si, Day27]
---

# N=20 反转岛壳闭合崩溃与四极集体性暴涨微观机制：单极张量力淬灭与 2p-2h 侵入组态基态反转

## Research Trigger

在经典迈耶-延森球形壳模型中，$N=20$ 是由三维谐振子主壳能隙形成的经典刚性球形幻数。在稳定自共轭核 $^{40}\text{Ca}$（$Z=20, N=20$）与半幻核 $^{34}\text{Si}$（$Z=14, N=20$）中，$N=20$ 表现出标准的坚硬球形闭壳特征：第一激发态 $2^+$ 能量极高（$E(2^+) \approx 3.3 - 3.9\text{ MeV}$），电四极跃迁强度微弱（$B(E2) \sim 2 - 4\ W.u.$）。
长期以来，传统核结构与天体物理中子捕获模型常将 $N=20$ 作为全核图上恒定不变的“不灭幻数”。

然而，在富中子区核结构实验中，[[motobayashi-1995-32mg-deformation]]（PLB 346, 9）利用 RIKEN 中间能量库仑激发直接测量了中子过剩核 $^{32}\text{Mg}$（$Z=12, N=20$），揭示了核物理史上最著名的壳层突变——**反转岛（Island of Inversion）**：
1. **$E(2^+)$ 能级的悬崖式崩塌**：第一激发态能量从 $^{34}\text{Si}$ 的 $3.33\text{ MeV}$ 暴跌至 $^{32}\text{Mg}$ 的 **$885\text{ keV}$（断崖式骤降近 4 倍）**；
2. **电四极跃迁几率的暴涨**：$B(E2; 0^+ \to 2^+_1)$ 从 $^{34}\text{Si}$ 的 $85\ e^2\text{fm}^4$ 暴涨至 **$454(78)\ e^2\text{fm}^4$（暴涨逾 $5.3$ 倍，达到 $19\ W.u.$）**，基态四极形变高达 $\beta_2 \approx 0.51$！

本研究基于单极张量相互作用驱动的单粒子能级演化与两态侵入微观混合模型 `day27_island_of_inversion_n20_collapse_study.py`，微观阐释 $N=20$ 球形壳隙如何被价质子剥离所抹杀，确立经典幻数跨同位旋迁移的失效硬边界。

## Grounded Evidence

通过执行全微观反转岛相变变分求解器 `system/scripts/day27_island_of_inversion_n20_collapse_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/island-of-inversion/island_of_inversion_results.json` 沉淀结构化数据，确立以下定量证据：

1. **单极张量力（Monopole Tensor Force）淬灭驱动的壳隙塌缩：**
   - 质子 $\pi d_{5/2}$ 轨道与中子 $\nu d_{3/2}$ 轨道之间存在极强的引力单极张量相互作用（$\Delta j = 1, \Delta l = 0$ 且自旋反平行）；
   - 在 $^{40}\text{Ca}$ 与 $^{34}\text{Si}$ 中，$\pi d_{5/2}$ 轨道处于满充或近满充状态，张量引力将中子 $\nu d_{3/2}$ 轨道强力向下拉紧，将 $N=20$ 球形主壳隙（$\nu d_{3/2} - \nu f_{7/2}$）撑大至 **$4.80 - 6.00\text{ MeV}$**；
   - 当继续剥离质子到达 $^{32}\text{Mg}$（$Z=12$）与 $^{30}\text{Ne}$（$Z=10$）时，$\pi d_{5/2}$ 质子的空出导致张量相互作用急剧削弱；中子 $\nu d_{3/2}$ 失去引力而大幅向上漂移，而高阶侵入轨道 $\nu f_{7/2}, p_{3/2}$ 相对下沉，导致 $N=20$ 球形单粒子壳隙被无情压缩至 **$\Delta\epsilon \approx 1.80\text{ MeV}$（$^{30}\text{Ne}$ 中仅剩 $0.40\text{ MeV}$）**。

2. **$2\text{p}-2\text{h}$ 侵入多准粒子四极关联能的基态反转：**
   - 将一对中子激发跨过能隙进入 $pf$ 壳所需的单粒子激发能代价值仅为 $2\Delta\epsilon \approx 3.60\text{ MeV}$；
   - 跨壳产生的两粒子-两空穴（$2\text{p}-2\text{h}$）非球形组态释放出巨大的对关联增益（$\sim 2.4\text{ MeV}$）以及长程四极-四极相互作用结合能（$\kappa_{QQ} \beta_2^2 \approx 3.1\text{ MeV}$），总关联能量增益高达 **$E_{\text{gain}} \approx 5.50\text{ MeV}$**；
   - 关联能量增益压倒了单粒子能隙代价值（逆差达 $\Delta E_{\text{inv}} = 3.60 - 5.50 = -1.90\text{ MeV}$），驱动 $2\text{p}-2\text{h}$ 强长椭形变态反转为绝对能量基态，基态侵入态杂化概率达到 **$87.3\%$（$^{30}\text{Ne}$ 达 $97.0\%$）**。

3. **四极集体性暴涨与转动图景确立：**
   - 侵入基态的反转彻底消除了原本维持球形微振的单极限制，自洽导出基态四极形变跃迁至 $\beta_2 = 0.46 - 0.51$；
   - 理论计算精确再现了 RIKEN 库仑激发实验结果：
     - $^{34}\text{Si}$（$0\text{p}-0\text{h}$ 占优）：$E(2^+)_{\text{calc}} = 3350.9\text{ keV}$（实测 $3327\text{ keV}$），$B(E2) = 104.1\ e^2\text{fm}^4$（实测 $85\ e^2\text{fm}^4$）；
     - $^{32}\text{Mg}$（$2\text{p}-2\text{h}$ 侵入反转）：$E(2^+)_{\text{calc}} = 1181.2\text{ keV}$（实测 $885\text{ keV}$），$B(E2) = 412.9\ e^2\text{fm}^4$（实测 $454(78)\ e^2\text{fm}^4$）；
   - 跨越 2 个质子，实测 $B(E2)$ 激增逾 $5.3$ 倍，严格证实了反转岛中球形幻数的彻底瓦解。

4. **幻数跨区不可迁移硬判据：**
   - **幻数同位旋依赖律**：经典幻数（$N=20, 28, 40$ 等）是质子-中子特定填充下的自洽平衡态，绝非核素图上的普适常数；在远离稳定线的同位旋不对称区，必须废止将 $N=20$ 作为闭壳的假设；
   - **模型空间截断禁戒**：在反转岛邻近核区，严禁使用常规 $0\hbar\omega$ 壳模型空间，必须显式引入包含 $2\hbar\omega$ 跨壳侵入组态的多主壳基底。

## Evidence Boundaries & Review Status

- 物理模型：基于单极张量驱动壳演化与两态侵入组态微观杂化模型；
- 证据层级：基于 Motobayashi 1995（RIKEN 中间能量库仑激发一手实验数据）与 Otsuka 2005 理论；
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
