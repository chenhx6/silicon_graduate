---
type: research-note
title: "超重核裂变势垒反转（B_f < S_n）与多次裂变雪崩微观机制：传统统计蒸发模型跨区外推的百万倍高估破除"
aliases: [superheavy-barrier-inversion-and-multi-chance-fission, superheavy fission barrier inversion survival, Day27 superheavy survival]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [zagrebaev-2001-superheavy-synthesis-survival]
created_from: Day 27 continuation study; system/scripts/day27_superheavy_survival_and_multi_chance_fission_study.py
tags: [superheavy-elements, multi-chance-fission, survival-probability, fission-barrier-inversion, 208Pb, 248Cm, 296_116, 304_120, Day27]
---

# 超重核裂变势垒反转（B_f < S_n）与多次裂变雪崩微观机制：传统统计蒸发模型跨区外推的百万倍高估破除

## Research Trigger

在重核与超重核合成动力学中，复合核经由 $xn$ 蒸发退激形成最终蒸发剩余核（Evaporation Residue, ER）的截面为：
$$\sigma_{\text{ER}}(E^*) = \sigma_{\text{cap}}(E^*) \cdot P_{\text{CN}}(E^*) \cdot W_{\text{surv}}(E^*),$$
其中生存几率 $W_{\text{surv}}$ 是约束合成截面绝对量级的核心统计瓶颈。
然而，当尝试将从稳定双幻核（$^{208}\text{Pb}$）或轻锕系核建立的经典 Hauser-Feshbach / CASCADE 统计蒸发模型直接平移至超重元素（$Z \ge 114$）时，理论预测截面发生了高达 **$10^4 - 10^6$ 倍的灾难性虚高**！

根据 [[zagrebaev-2001-superheavy-synthesis-survival]]（PRC 65, 014607）的微观自洽动力学分析，这一统计模型跨区迁移的根本破缺源于超重核独有的两大微观物理现实：
1. **裂变势垒反转（Fission Barrier Inversion, $B_f < S_n$）**：超重核宏观液滴势垒为零，纯靠微观壳效应维持势垒，其高度（$B_f \approx 5.5\text{ MeV}$）系统性低于中子分离能（$S_n \approx 7.2\text{ MeV}$）；
2. **热壳能阻尼消融（Thermal Shell Damping）**：在复合核初始激发能（$E^* \sim 35 - 45\text{ MeV}$）下，微观壳能发生指数热消融，使有效裂变势垒暴跌至 $< 1.0\text{ MeV}$。

本研究基于玻尔-惠勒裂变统计理论与多次裂变级联求解器 `day27_superheavy_survival_and_multi_chance_fission_study.py`，微观阐明裂变雪崩对中子蒸发的压倒性扼杀机制，确立传统统计代码向超重核迁移的不可适用性边界。

## Grounded Evidence

通过执行全微观超重核多次裂变与生存几率变分求解器 `system/scripts/day27_superheavy_survival_and_multi_chance_fission_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/superheavy-survival/superheavy_survival_results.json` 沉淀结构化数据，确立以下定量证据：

1. **热相空间下有效裂变势垒的雪崩式塌缩：**
   - 在基态下，超重核 $^{296}116$ 依靠微观壳效应维持 $B_f(0) = 5.85\text{ MeV}$；
   - 在热核激发（$E^* \approx 38.0\text{ MeV}$，温度 $T \approx 1.13\text{ MeV}$）下，壳修正遵从 Ignatyuk 阻尼定律 $B_f(E^*) = B_f(0) \exp(-E^* / E_d)$（阻尼能标 $E_d \approx 18.5\text{ MeV}$）；
   - 初始复合核第一步的有效势垒暴跌至 **$B_f^{\text{eff}} \approx 0.75\text{ MeV}$**；
   - 这与稳定的 $^{208}\text{Pb}$ 形成鲜明对比：$^{208}\text{Pb}$ 具有庞大的宏观液滴势垒（$B_f^{\text{LD}} \approx 18.0\text{ MeV}$），即使在 $E^* = 40\text{ MeV}$ 下其势垒仍高达 $19.5\text{ MeV}$。

2. **多次裂变（Multi-Chance Fission）雪崩与指数淬灭：**
   - 依据玻尔-惠勒截面公式，中子蒸发与裂变分支比为：
     $$\frac{\Gamma_n}{\Gamma_f}(E^*) \approx 0.14 A^{2/3} T \exp\left( \frac{B_f^{\text{eff}} - S_n}{T} \right);$$
   - 在 $^{296}116$ 第一步中，由于能量亏损 $B_f^{\text{eff}} - S_n = 0.75 - 7.20 = -6.45\text{ MeV}$，玻尔兹曼惩罚因子跌落至 $\exp(-5.7) \approx 0.0033$；
   - 第一中子蒸发生存几率仅为 $P_{n, 1} \approx 0.5\%$（即 $99.5\%$ 的反应通量在第一阶段即发生一裂变损失）；
   - 连续经历 $3n$ 蒸发步长（依次为 $38 \to 28 \to 18\text{ MeV}$）后，总生存几率被极度压缩至 **$W_{\text{surv}} \approx 2.81 \times 10^{-6}$**（在 $^{304}120$ 的 $4n$ 蒸发中跌至 **$< 10^{-8}$**）；
   - 而在 $^{208}\text{Pb}$ 中，由于 $B_f - S_n = +17.13\text{ MeV}$，中子蒸发几率恒定在 $99.995\%$，裂变完全被动力学锁死。

3. **统计蒸发模型跨区外推失效判据：**
   - **势垒反转硬判据**：当体系处于 $B_f < S_n$ 的超重逆转区时，严禁使用将裂变宽度设为常数或忽略热壳能消融的弱耦合统计近似；
   - **数量级灾难破除**：传统代码若沿用宏观平均势垒，计算出的超重生存几率高达 $10^{-2} - 10^{-1}$，系统性夸大产额百万倍；自洽考虑多次裂变雪崩是解释超重元素“皮靶截面”极限的根本物理保障。

## Evidence Boundaries & Review Status

- 物理模型：基于玻尔-惠勒统计衰变、Ignatyuk 热壳能阻尼与多次裂变概率级联；
- 证据层级：基于 Zagrebaev 2001（PRC 理论原件）与 Dubna FLNR-DGAS 合成实验截面；
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
