---
type: concept
title: Gamow-Teller transition strength
aliases: [Gamow-Teller strength, BGT]
created: 2026-09-05
updated: 2026-09-05
status: ai-draft
review_status: unreviewed
tags: [beta-decay, gamow-teller, shell-model, a100]
concept_type: decay-observable
confidence: medium
high_confirmed_by:
high_confirmed_date:
---

# Gamow-Teller transition strength

## Definition

Gamow-Teller（GT）跃迁是允许 β 衰变中的自旋-同位旋算符跃迁，常用约化强度 `B(GT)` 表征。`B(GT)` 通常由半衰期、端点能量/相空间因子和分支模型联合得到，不能脱离这些输入直接比较。

## `100Sn` Evidence Boundary

- Hinke 2010 的 GSI `100Sn` thesis 报告 `BGT=9.1(+4.8/-2.3)`，依赖约 70 个衰变事件、`Eβ0=3.29±0.20 MeV`、single-final-state assumption 和 conversion/annihilation corrections。
- Lubos 2016 的 RIKEN thesis 报告 `BGT=5.26(+0.90/-1.06)`，依赖 `T1/2=1.17±0.10 s`、`Q=3.74±0.14 MeV` 和 detector-response/positron-calorimetry fit。
- 两者来自不同 facility 和分析链，属于 `multiple-independent` candidate evidence；在 claim-specific review 前不应静默平均或简单称为矛盾。

## Model and Review Boundary

`B(GT)` 与 shell-model model space、核矩阵元、Q-value、branching、detector response 和 systematic uncertainty 相关。Hinke 的“Super GT/no quenching”与 Lubos 的大空间壳模型一致性都属于 source-attributed interpretation；需要回到两个 source 和原始数据后才能用于论文级表述。

## Necessary Assumptions

使用具体 `B(GT)` 数值时，必须说明半衰期、端点/Q-value、decay branch、相空间因子、detector response、conversion/annihilation correction 和 shell-model convention；不同实验的数值不能脱离这些条件平均。

## Discriminating Observables

半衰期、Q-value/endpoint、branching ratio、β-delayed γ/γγ coincidence、`log(ft)`、绝对强度和 shell-model model-space comparison。

## Supporting Evidence

[[hinke-2010-100sn-decay-spectroscopy]] 与 [[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]] 提供两条不同 facility 的 `100Sn` decay-spectroscopy 链。

## Counter-evidence and Competing Interpretations

`B(GT)` 差异可能来自统计、Q-value、single-state/branching assumptions、response simulation 和 model-space choices；不能直接解释为 GT quenching 的物理冲突。

## Our Current Position

`100Sn` 的 GT 强度是高价值但仍需 claim-specific verification 的比较问题。当前保留两条 independent measurements 和各自 assumptions，不把“Super GT/no quenching”升级为最终结论。

## Sources

- [[hinke-2010-100sn-decay-spectroscopy]]
- [[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]]

## Human Review Triage

### P0

- 核对两份 `BGT` 数值、Q/endpoint、半衰期、branch assumptions 和 uncertainty propagation；避免把不同实验合并。

### P1

- 核对 shell-model comparison、single-final-state assumption 和 `100In` level-scheme dependence。

### P2/P3

- 需要论文写作时，再针对具体 `BGT` claim 回到两个原始 source。
## Day21 Checkpoint090 推断阶梯边界：相空间五次方幂律非线性敏感度

099修订：端点敏感度取决于能区、库仑函数、EC/β+及分支定义，“约五次方”不作全能区定理。旧078的168.09/304.25是非相对论Sommerfeld β+积分，非原论文LOGFT结果；105.5%不是解释率或统计覆盖率。

[[hinke-2010-100sn-decay-spectroscopy]] HK10-D21-R99-2/3与[[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]] LB16-D21-R99-1/3分别给原计算入口和样本身份。多条子核γ级联可以来自同一个母核GT终态；Super GT不等于无淬灭。必须统一端点、部分半衰期、EC约定、模型空间与误差后才能判断quenching差异。


## Day21 checkpoint124：条件证据与量词纠正

[[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]] LB16-D21-R99-1/2/3区分库存、端点谱样本与子核成分；24个子核谱成分不能改成24个母核GT终态，也不能无原表把它们全部叫γ级联。[[nndc-2026-logft-calculator-input-contract]] LOGFT26-4/5只验证当前程序声明通道及部分半衰期，不重放历史job。Super GT不等无淬灭；新增基态/1+终态归属与介子交换流解释没有在120独立核实，不沿用。
