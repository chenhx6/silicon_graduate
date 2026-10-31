---
type: research-note
title: "超重稳定岛幻数不可迁移性与自旋—轨道劈裂淬灭微观机制：库仑中心凹陷诱发的Z=114对决Z=120模型分歧"
aliases: [superheavy-magic-numbers-and-spin-orbit-quenching, superheavy magic numbers non-transferability, Day27 superheavy magic]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bender-1999-superheavy-magic-numbers]
created_from: Day 27 continuation study; system/scripts/day27_superheavy_magic_numbers_and_spin_orbit_quenching_study.py
tags: [superheavy-elements, magic-numbers, spin-orbit-quenching, Coulomb-repulsion, central-depression, 208Pb, 298_114, 304_120, Day27]
---

# 超重稳定岛幻数不可迁移性与自旋—轨道劈裂淬灭微观机制：库仑中心凹陷诱发的 Z=114 对决 Z=120 模型分歧

## Research Trigger

在经典低能核结构中，$^{208}\text{Pb}$（$Z=82, N=126$）被奉为坚不可摧的球形双幻核典范：其具有高达 $3.85 - 4.20\text{ MeV}$ 的巨质子壳隙，基态四极刚度极高（$C_2 \approx 280\text{ MeV}$），第一激发态 $2^+$ 能量高达 $4.09\text{ MeV}$。
长期以来，文献中常习惯性地将“坚硬球形双幻核”的概念直接平移至超重核“稳定岛（Island of Stability，预测位于 $Z \sim 114 - 126, N \sim 184$）”。

然而，自洽微观密度泛函理论（[[bender-1999-superheavy-magic-numbers]]，PRC 60, 034304）与近代超重核合成实验揭示了一个根本性的迁移断裂：
1. **质子闭壳模型的根本对立**：相对论平均场（RMF / CDFT）系统性预言 $Z=114$ 为质子闭壳（壳隙处于 $2f_{7/2} - 2f_{5/2}$ 之间）；而非相对论 Skyrme（如 SLy4, SkI4）与 Gogny（D1S）则坚决预言 $Z=120$（壳隙处于 $2f_{5/2} - 3p_{3/2}$ 之间）甚至 $Z=126$ 为质子闭壳；
2. **壳隙高度压缩与四极软度**：无论哪种自洽模型，超重候选闭壳的质子能隙仅为 $\sim 1.8 - 2.15\text{ MeV}$（不足 $^{208}\text{Pb}$ 的一半）；四极刚度暴跌近 5 倍（$C_2 \approx 58\text{ MeV}$），导致超重基态普遍陷入形变软度与长椭—扁椭形状共存，根本不存在 $^{208}\text{Pb}$ 那样的刚性球形基态。

本研究基于自洽库仑自能退局域化与自旋—轨道势梯度展开 `day27_superheavy_magic_numbers_and_spin_orbit_quenching_study.py`，微观阐释库仑斥力诱发中心密度凹陷（Bubble 效应）、进而淬灭自旋—轨道相互作用的动力学机制，形式化幻数概念向超重核迁移的不可适用性边界。

## Grounded Evidence

通过执行全微观超重幻数演化求解器 `system/scripts/day27_superheavy_magic_numbers_and_spin_orbit_quenching_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/superheavy-magic-numbers/superheavy_magic_numbers_results.json` 沉淀结构化数据，确立以下定量证据：

1. **巨大库仑斥力诱发中心密度凹陷（Central Depression）：**
   - 在超重核（$^{298}114, ^{304}120$）中，质子静电自能总额激增至 $E_C \sim 1400 - 1800\text{ MeV}$（单质子平均库仑斥力高达 $12.3 - 12.85\text{ MeV}$，较 $^{208}\text{Pb}$ 增长近 $30\%$）；
   - 巨大的内部正电荷斥力迫使质子波函数向表面剧烈挤压，使自洽核物质中心密度 $\rho(0)$ 发生显著塌缩：在 $^{298}114$ 中，$\rho(0)/\rho_{\text{sat}} \approx 0.821$（中心凹陷 $18\%$）；在 $^{304}120$ 中，$\rho(0)/\rho_{\text{sat}} \approx 0.774$（中心凹陷近 $23\%$），呈现明显的“红酒瓶底形（Wine-bottle shape）”密度分布。

2. **密度梯度平坦化驱动自旋—轨道相互作用（$V_{ls}$）深度淬灭：**
   - 自旋—轨道势能严格遵从表面梯度导数公式 $V_{ls}(r) \propto \frac{1}{r} \frac{d\rho}{dr} \mathbf{l} \cdot \mathbf{s}$；
   - 中心密度的凹陷与平坦化破坏了传统核势阱内部向心梯度，导致高-$l$ 轨道核内重叠区的自旋—轨道势发生雪崩式衰减：
     - $\pi 2f_{7/2} - \pi 2f_{5/2}$ 劈裂能量从 $^{208}\text{Pb}$ 的 $1.82\text{ MeV}$ 骤降至 $^{304}120$ 的 **$1.33\text{ MeV}$（淬灭达 $28.2\%$）**；
     - $\pi 1i_{13/2} - \pi 1i_{11/2}$ 劈裂能量从 $6.08\text{ MeV}$ 骤降至 **$4.45\text{ MeV}$**；
   - 正是自旋—轨道能量分裂的剧烈压缩，使得原本在轻中核中牢不可破的主壳隙发生轨道交错杂化，直接造成了不同自洽平均场模型（因有效质量与相对论项微小差异）对 $Z=114$ 与 $Z=120$ 闭壳指认的彻底撕裂。

3. **四极恢复力塌缩与形状共存基态：**
   - 壳隙的微弱化（$\Delta E \le 2.15\text{ MeV}$）使体系对抗四极变形的刚度从 $^{208}\text{Pb}$ 的 $C_2 = 280\text{ MeV}$ 塌缩至 **$C_2 = 58\text{ MeV}$（削弱 $4.8$ 倍）**；
   - 仅需不足 $0.65\text{ MeV}$ 的变形驱动能，超重“闭壳候选核”便自发在 $\beta_2 \approx \pm 0.12$ 处形成长椭与扁椭能量极小；
   - 确立了**幻数概念跨区不可迁移性判据**：绝不可将 $^{208}\text{Pb}$ 的“单主导球形双幻刚硬性”作为物理前提平移至超重岛区；超重核的所谓“闭壳”本质上是高态密度背景下的局部弥散弱壳隙，伴随内禀形变软度与连续谱耦合。

## Evidence Boundaries & Review Status

- 物理模型：基于自洽平均场中心库仑密度响应、自旋—轨道势梯度求导与四极曲率动力学展开；
- 证据层级：基于 Bender 1999（RMF 与 Skyrme 跨模型对比基准）与 $^{208}\text{Pb}$ NNDC 数据；
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
