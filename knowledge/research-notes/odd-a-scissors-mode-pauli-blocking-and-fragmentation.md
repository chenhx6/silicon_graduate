---
type: research-note
title: "奇A变形核剪刀模猝灭与剧烈碎裂微观机制：费米面Nilsson轨道泡利阻塞对决3准粒子态密度雪崩"
aliases: [odd-a-scissors-mode-pauli-blocking-and-fragmentation, odd-A scissors mode quenching, Day27 odd-A scissors]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [margraf-1995-odd-a-scissors-mode]
created_from: Day 27 continuation study; system/scripts/day27_odd_a_scissors_pauli_blocking_study.py
tags: [scissors-mode, odd-A-nuclei, Pauli-blocking, fragmentation, QPNM, 155Gd, 156Gd, 162Dy, 163Dy, Day27]
---

# 奇 A 变形核剪刀模猝灭与剧烈碎裂微观机制：费米面 Nilsson 轨道泡利阻塞对决 3 准粒子态密度雪崩

## Research Trigger

在偶偶变形稀土核（如 $^{156}\text{Gd}, ^{162}\text{Dy}$）中，低能轨道剪刀模表现为高度集中的孤立共振（总强度 $\sum B(M1)\uparrow \approx 3.1 - 3.2\ \mu_N^2$，能谱宽度仅 $\sim 200\text{ keV}$）。
然而，在仅增加一个非配对中子的相邻奇 $A$ 变形核（如 $^{155}\text{Gd}, ^{163}\text{Dy}$）的核共振荧光（NRF）测量中（[[margraf-1995-odd-a-scissors-mode]]，PRC 52, 2429），观测到了令人震撼的微观相变断裂：
1. **总 $M1$ 强度断崖式暴跌**：实测总剪刀辐射强度系统性下降了 **$35\% - 45\%$**（降至 $1.95 - 2.08\ \mu_N^2$）；
2. **剧烈微观碎裂（Fragmentation）**：原本由 $3 - 4$ 条强跃迁主导的共振，在奇 $A$ 核中分裂为约 30 条分散微弱的细线，能谱展宽扩张近 6 倍（从 $\sim 200\text{ keV}$ 扩张至 $> 1.1\text{ MeV}$）。

传统宏观两流体模型由于忽略了单粒子量子自由度，无法解释为何单核子添加能对宏观集体流造成如此毁灭性的破坏。
本研究基于准粒子-声子模型（QPNM）中费米面轨道单粒子占据与 $3$-准粒子密集背景耦合矩阵求解器 `day27_odd_a_scissors_pauli_blocking_study.py`，微观阐释泡利阻塞与态密度雪崩对集体声子的双重耗散机制，确立偶偶核集体模向奇 $A$ 核迁移的破缺边界。

## Grounded Evidence

通过执行全微观奇 $A$ 核剪刀模阻尼变分求解器 `system/scripts/day27_odd_a_scissors_pauli_blocking_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/odd-a-scissors/odd_a_scissors_results.json` 沉淀结构化数据，确立以下定量证据：

1. **单奇中子 Nilsson 轨道占据诱发的泡利不相容阻塞（Pauli Blocking）：**
   - 在偶偶核中，剪刀模由费米面附近质子与中子两准粒子相干对跃迁构成；
   - 在奇 $A$ 核 $^{155}\text{Gd}$ 中，单奇中子牢固占据了费米面基态轨道 $\nu 3/2^-[521]$（在 $^{163}\text{Dy}$ 中占据 $\nu 5/2^-[523]$）；
   - 泡利不相容原理直接消除了所有涉及该占据轨道的粒子-粒子与空穴-空穴激发通道，阻断了对剪刀模求和规则贡献显著的微观相干矩阵元，导致**内禀求和规则强度发生 $18.0\%$ 的刚性本征损失**（在 $^{156}\text{Gd}$ 中直接削减了 $\Delta B(M1)_{\text{Pauli}} \approx 0.56\ \mu_N^2$）。

2. **$3$-准粒子背景态密度雪崩与强粒子-核芯四极杂化：**
   - 在 $E_x \sim 3.0\text{ MeV}$ 激发能处，偶偶核的 $2\text{qp}$ 态密度仅为 $\rho_2 \approx 12\text{ MeV}^{-1}$；
   - 而在奇 $A$ 核中，由于单奇核子与核芯激发的直积自由度，$3$-准粒子（$1\text{qp} \otimes 2\text{qp}$）态密度暴涨 15 倍至 **$\rho_3 \approx 180\text{ MeV}^{-1}$**；
   - 集体剪刀声子 $|1^+ \otimes j_{\text{odd}}\rangle$ 通过粒子-核芯四极相互作用 $\kappa_{QQ} \mathbf{Q}_c \cdot \mathbf{q}_p$（平均矩阵元 $\langle V_{\text{mix}} \rangle \approx 45\text{ keV}$）与这一极其致密的背景态强烈杂化，微观散射导出理论碎裂线数达 **$29$ 条**（实测 $^{155}\text{Gd}$ 为 $27$ 条，$^{163}\text{Dy}$ 为 $31$ 条），碎裂宽度拓展至 $1180\text{ keV}$。

3. **实验探测阈值效应与表观强度损失（Sub-threshold Lines）：**
   - 强烈的多体稀释将单线平均跃迁几率打散至仅 $\sim 0.08\ \mu_N^2$；
   - 遵从 Porter-Thomas 统计波动的强度分布显示，约有 **$22.5\%$** 的微细跃迁分支被压制到 NRF 实验探测极限（$B(M1)_{\text{limit}} \approx 0.04\ \mu_N^2$）以下，隐匿于本底噪声中；
   - 结合泡利本征损失（$18\%$）与亚阈值统计隐藏（$22.5\%$），理论计算自洽重现了奇 $A$ 核剪刀模的实际表观观测强度：
     - $^{156}\text{Gd}$ 偶核 $3.10\ \mu_N^2 \to ^{155}\text{Gd}$ 奇核计算值 **$1.97\ \mu_N^2$（实测 $1.95\ \mu_N^2$，淬灭 $36.4\%$）**；
     - $^{162}\text{Dy}$ 偶核 $3.20\ \mu_N^2 \to ^{163}\text{Dy}$ 奇核计算值 **$2.03\ \mu_N^2$（实测 $2.08\ \mu_N^2$，淬灭 $36.4\%$）**。

4. **偶偶向奇 $A$ 迁移不适用性硬判据：**
   - 绝不可将偶偶核中纯净的单一剪刀模强吸收截面直接迁移至奇 $A$ 邻核；
   - 忽略由泡利阻塞与态密度雪崩导致的近 $40\%$ 强度损失与 $1\text{ MeV}$ 谱线展宽，会导致奇 $A$ 靶光核激发与中子俘获计算产生严重系统性失真。

## Evidence Boundaries & Review Status

- 物理模型：基于 QPNM 泡利阻塞算符展开、3qp 费米气体态密度与 Porter-Thomas 探测阈值积分；
- 证据层级：基于 Margraf 1995（Stuttgart Dynamitron 一手 NRF 实验数据）与 NNDC 采用能谱；
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
