---
type: research-note
title: "74Br 第四带预测的检验准备：同母态分支、混合份额与寿命消去"
aliases: [74Br B4 branching network, Chiral wobbler fourth band test]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [guo-2024-chiral-wobbler-74br, qureshie-2026-chiral-wobbling-four-band-74br, lange-kumar-hamilton-1982-multipole-admixtures]
created_from: Day27 continued source reading and public-table analysis
promotion_target: ""
tags: [74br, chirality, wobbling, branching-ratio, falsification, readiness]
---

# 从 E2 份额转向有身份的分支网络

## Grounded Evidence

[[guo-2024-chiral-wobbler-74br]] 的 Supplement Table I（PDF pp.1–2）给出 B3 带内与 B3→B1 的逐线能量、强度、δ 和派生强度。[[qureshie-2026-chiral-wobbling-four-band-74br]] pp.4–5、Figs.6–8 预测 B4→B3 与 B4→B2 两类关系；当前 B4 未作为新实测序列报告。

研究问题：哪些组合能在不先测出 B4 绝对寿命时检验这两条关系，又不会把大 E2 份额误写成大绝对集体强度？

## Provisional Reasoning

在同一真实母态、共同效率修正光子强度、out 为 M1/E2 混合、in 为纯 E2 的条件下，

\[
\frac{B(E2;\mathrm{out})}{B(E2;\mathrm{in})}
=\frac{I_{\gamma,\mathrm{out}}}{I_{\gamma,\mathrm{in}}}
\left(\frac{E_{\gamma,\mathrm{in}}}{E_{\gamma,\mathrm{out}}}\right)^5
\frac{\delta_{\mathrm{out}}^2}{1+\delta_{\mathrm{out}}^2}.
\]

共同寿命和母态布居消去。相同自旋不够，必须是同一能级、同一选择/归一对象。公式只用光子部分率，不再给光子强度比乘内转换系数；若输入实际是总衰变分支，则须先恢复对应光子分支合同。辐射率与 δ 定义见 [[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1 及 [[bm1-be2-ratio]]。

## Published-input Replay

以下是已发表表格的派生重放，属于 L2/readiness；没有重新拟合事件，没有独立新寿命结果。

| B3 母态 | out B3→B1 / in B3→B3 的 Eγ(keV) | δout | out 的 E2 光子份额 | 派生 B(E2)out/in |
| --- | --- | --- | --- | --- |
| 8+ | 815.3 / 682.7 | −1.1(+0.3/−0.4) | 0.5475 | 0.3136 |
| 9+ | 1155.6 / 811.6 | 3.1(+1.8/−0.9) | 0.9057 | 0.04869 |
| 10+ | 1266.8 / 955.5 | 8(+3/−2) | 0.9846 | 0.2049 |

强度输入分别为 12.8(4)/9.2(13)、2.8(6)/8.9(15)、5.2(10)/6.1(10)，均沿用 Supplement Table I 的共同归一。文中 Iγ=100 的参考线为 383.0keV；这些数值不单独作为母态总分支概率。

同表已舍入的 B(E2) 直接相除为约 0.333、0.0457、0.2125。它们重用了寿命、强度与混合比，不能当独立实验验证；本次差异也不超出印刷舍入与原误差合同可允许的解释范围。

为保留缺失协方差，把强度各自的印刷误差端点与 δ 的不对称端点作笛卡尔积，得到约 [0.1897,0.4762]、[0.02996,0.07537]、[0.1405,0.2943] 的输入域包络。它们没有统计覆盖率，也不是置信/可信区间。未传播未给出的联合协方差、响应、背景和能量误差。

## Provisional Insight

9+ 分支的 E2 光子份额约 91%，但相对于同母态带内 E2 的强度商只有约 0.049。大 δ 约束同一光子的 E2/M1 部分率比，不能替代 E2out/in、绝对 B(E2) 或波函数关系。本例把这种区别落到真实公开输入，也说明只按“E2 主导”给模式贴标签会丢失分支网络信息。

8+、9+、10+ 的网络比值明显不同；这些点数和误差不足以独立认证量子声子阶数或对整个自旋区间拟合一个常数。组态、signature、取向与混合的模型预测需要逐态匹配。

## Falsification or Reverse Tests

1. 先用符合关系、Ei、Jπ 确定 B4 及两条连接，证明它们来自同一母态。理论曲线不能补造实验 B4。
2. 同时测 B4→B3 与 B4→B2 的强度及多极成分，使用能量加权部分率比；不只检查一条线的正偏振或大 |δ|。
3. 要检验与已有 B3/B1 的关系，可为 B4 建立带内 E2 参考；若只有不同多极阶数的两条连接，则须保留 M1/E2 的辐射常数和不同 Eγ 幂次。
4. 与其它组态/取向激发在同一输入和算符下比较，同时检验自旋交错、带内电磁率和连接拓扑。缺少竞争模型预测时只形成 readiness。
5. 预测线未见时，先给门、效率、背景、能量窗及多重性对应的上限。缺少灵敏度时记录未测/未识别，不能直接证伪。

## Reproducibility

脚本 `system/scripts/day27_br74_branching_network.py` 运行前核对实际 SI 的 SHA-256；结果位于 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/br74-network/br74-branching-network.json`。它记录逐线身份/locator、输入、包络与舍入对照；验证相同多极比值在 keV/MeV 一致换算下不变，δ 区间跨零时 E2 下界包含零。

## Promotion or Rejection History

- 2026-10-29：新 2026 理论来源触发 B4 双连接检验设计；已有 B3 表格派生量为检验准备提供标度，不作为独立 L4 发现。

## Agent self-audit triage

P0: none identified。公开 SI 身份已核，无虚构 B4 计数或上限。P1：共同母态、纯 E2 参考与 M1/E2 截断、效率/协方差和竞争模型缺口。P2/P3：印刷舍入单独保留；本次不改变 Guo2024 的 human-review 范围。

## Research Trigger

2026年新来源预测第四带，需将单线混合份额推进到可检验的多分支网络。

## Assumptions

公式假定同一母态、共同效率修正的光子强度、纯E2参考和M1/E2截断；这些前提逐线核验。

## Competing Explanations

同组态的其它取向激发、signature结构或组态混合也可能产生部分相似分支，需共同算符下比较。

## Transfer Conditions

将方法用于B4或其它核时，保留母末态身份、能量幂次、相同门与归一合同。

## Failure Conditions

母态不同、参考含未量化混合、未修正相对效率或缺少背景灵敏度时，不把比值解释为此模型的电磁强度商。

## Open Questions

B4双连接的可见性与竞争组态预测能否同时受约束？共同校准与弱分支协方差会怎样改变比较能力？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页未发生人工审核；保留unreviewed与provisional，既有Guo2024审核范围不扩张。
