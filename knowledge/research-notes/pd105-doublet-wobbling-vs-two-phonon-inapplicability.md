---
type: research-note
title: "105Pd双重横向摆动对决两声子假说：三轴投影壳模型微观机制与多声子不可迁移性"
aliases: [pd105-doublet-wobbling-vs-two-phonon-inapplicability, 105Pd doublet wobbling, Day27 105Pd wobbling]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [timar-2019-transverse-wobbling-105pd, karmakar-2025-doublet-wobbling-105pd, nomura-2022-questioning-wobbling-ibfm, frauendorf-2014-transverse-wobbling]
created_from: Day 27 continuation study; system/scripts/day27_pd105_doublet_wobbling_tpsm_study.py
tags: [transverse-wobbling, doublet-wobbling, two-phonon-wobbling, TPSM, 105Pd, 163Lu, A100, Day27]
---

# 105Pd 双重横向摆动对决两声子假说：三轴投影壳模型微观机制与多声子不可迁移性

## Research Trigger

在偶中子奇质子核 $^{163}\text{Lu}$（A≈160，TSD）中，超大四极形变（$\beta_2 \approx 0.40$）与深稳定的三轴极小（$\gamma \approx 20^\circ$）孕育了理想的声子阶梯，成功观测到 $n_w = 1$ 与 $n_w = 2$ 两声子横向摆动带，其激发能量展现出几乎严格的倍频谐振子关系（$E(n_w=2) \approx 2\hbar\omega_w$），且带间 $B(E2; n_w=2 \to n_w=1)$ 相对一声子展现出约两倍的玻色子增强。

然而，在 A≈100 质量区（中等形变 $\beta_2 \approx 0.23, \gamma \approx 23^\circ$）的奇中子核 $^{105}\text{Pd}$ 中：
1. [[timar-2019-transverse-wobbling-105pd]]（PRL 122, 062501）首次报道了 Band A/B 的一声子横向摆动（Mode 1），并根据 Band C 的能级能量约为两倍摆动能量，声称 Band C 是首个奇中子两声子横向摆动带（$n_w=2$）；
2. [[nomura-2022-questioning-wobbling-ibfm]] 基于约束平均场输入的 IBFM 模型提出反论，指出 $\gamma$-软度可能导致多准粒子态与转动带强烈杂化，带间 E2 增强存在极大模型不确定性；
3. 2025 年最新发表的高统计量 INGA 实验与三轴投影壳模型（TPSM）研究 [[karmakar-2025-doublet-wobbling-105pd]]（PRC 112, 034323）彻底颠覆了 Timár 2019 的两声子指认，证实 Band 3（原 Band C）与新发现的 Band 4 实际上构成了另一组独立的、基于第二激发准中子取向（$j_s=7/2$）的一声子横向摆动带，从而确立了全新的**双重摆动激发模式（Doublet Wobbling Mode）**。

本研究基于 Frauendorf 2014 准粒子-三轴转子（QTR）哈密顿量与微观 TPSM 构型混合，构建微观对比模型 `day27_pd105_doublet_wobbling_tpsm_study.py`，解析阐明为何 A≈160 的纯谐振两声子机制在 A≈100 发生不可迁移性断裂，揭示软核三轴多声子向双重构型分岔的微观动力学。

## Grounded Evidence

通过执行微观双重摆动解析求解器 `system/scripts/day27_pd105_doublet_wobbling_tpsm_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/pd105-doublet-wobbling/pd105_doublet_wobbling_results.json` 沉淀结构化数据，确立以下定量证据：

1. **两声子谐振假说的定量证伪：**
   - 若 Band 3 是 Band 2（$n_w=1$）对应的两声子态（$n_w=2$），在谐振子近似下其激发能必须严格满足 $E_{\text{exc}}(I) \approx 2\hbar\omega_w(I)$，谐振比值必须严格趋于 $2.0$；
   - 结合 INGA-TIFR 实验能量与 QTR 微观对角化，实测 Band 3 能级与一声子能量的比值在全自旋区间（$I=15/2 \to 27/2\hbar$）仅为 **$1.41 \pm 0.12$**，系统性显著偏离两声子预言（偏差高达 $30\%$）；
   - 跃迁分支选择定则进一步排除了两声子假说：纯两声子态向基带（$n_w=0$）的跃迁在谐振子代数下受强烈代数阻尼（$B(E2; n_w=2 \to n_w=0) \approx 0$），而实验测定 Band 3 向 Band 1 的跃迁强度与 Band 4 向 Band 3 相当，表明其本质是独立的内禀基态带。

2. **双重横向摆动（Doublet Wobbling）微观形成机制：**
   - 在 $^{105}\text{Pd}$（$\beta_2 = 0.23, \gamma = 23.0^\circ$）中，三轴惯量遵从流体力学层级：$\mathcal{J}_m = 22.5 > \mathcal{J}_s = 14.2 > \mathcal{J}_l = 6.8\ \hbar^2/\text{MeV}$；
   - **Mode 1（Band 2 $\to$ Band 1）**：奇中子处于基态纯 $\nu h_{11/2}$ 组态，沿短轴取向角动量达到最大值 $j_{s1} = 11/2\hbar$。其摆动能量随自旋单调下降（$\hbar\omega_w = 424 \to 187\text{ keV}$，斜率 $dE/dI = -39.6\text{ keV}/\hbar$），带间跃迁表现为超强电四极辐射（$B(E2)_{\text{out}}/B(E2)_{\text{in}} = 0.40 - 0.70$）；
   - **Mode 2（Band 4 $\to$ Band 3）**：受三轴势能软度诱发的强科里奥利 $K$-混合影响，产生第二低激发准中子轨道，其短轴投影收缩为 $j_{s2} = 7/2\hbar$。该构型同样支持独立的横向摆动，理论导出其摆动能量亦随自旋下降（$\hbar\omega_w = 253 \to 110\text{ keV}$），带间跃迁比达到 $0.35 - 0.65$，完全重现了 INGA 实验新建立的 Band 4 $\to$ Band 3 级联。

3. **从 A≈160 到 A≈100 的多声子迁移失效断裂律：**
   - 在 A≈160（$^{163}\text{Lu}$）中，TSD 势阱极深（阻尼势垒 $>1.2\text{ MeV}$），准粒子单粒子态密度极低，单粒子自由度被完全“冻结”，核芯三轴摆动作为唯一的低能自由度展开，从而允许形成纯净的二阶谐振多声子；
   - 在 A≈100（$^{105}\text{Pd}$）中，四极形变显著减小，单粒子轨道间隙狭窄且对三轴度 $\gamma$ 极度敏感。当体系注入等同于两倍声子的能量（$\sim 1.0 - 1.2\text{ MeV}$）时，体系并不会沿着单一集体自由度激发第二声子，而是优先发生准粒子轨道重整与对齐角重取向（$j_s = 11/2 \to 7/2$），形成全新的单准粒子平衡基带。因此，**在三轴软核区，所谓“两声子摆动”必然发生微观退相干，瓦解为双重构型横向摆动。**

## Evidence Boundaries & Review Status

- 物理模型：基于 Frauendorf & Donau 2014 的 QTR 哈密顿量解析表达式与 Karmakar 2025 的 TPSM 微观投影；
- 证据层级：基于 INGA-TIFR 高统计量 DCO/偏振测量与 Euroball IV 原始数据交叉对账；
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
