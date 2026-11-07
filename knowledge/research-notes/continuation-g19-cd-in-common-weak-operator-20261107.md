---
type: research-note
title: "129Cd/130In：母态归一、相互作用版本与弱算符的共同输入边界"
aliases: [129Cd 130In weak-decay contract]
created: 2026-11-07
updated: 2026-11-08
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [continuation-g19-saito-2020-129cd-spectroscopy, continuation-g19-dunlop-2016-cd-halflives, continuation-g19-taprogge-2014-129cd-isomer, campaign-g09-taprogge-2015-129cd-beta-decay, campaign-g09-nesterenko-2020-in-isomers]
created_from: "G19 acquisition; G22 primary-table audit; parent integration"
promotion_target:
tags: [129cd, 130in, beta-decay, gamow-teller, first-forbidden, source-lineage, normalization]
---

# 近等寿命怎样约束不同的微观模型？

## Grounded Evidence

[[continuation-g19-saito-2020-129cd-spectroscopy]]的实际版本是arXiv2008.02959v1，
TableII在PDF10；[[continuation-g19-dunlop-2016-cd-halflives]]实际版本为
arXiv1711.05621v1，淬灭讨论在PDF5。发表身份和实际读取版本分别保留。
Saito沿用Dunlop所分析的同批GRIFFIN数据及129Cd两母态147(3)、157(8)ms半衰期；
与[[campaign-g09-taprogge-2015-129cd-beta-decay]]的EURICA采集分开。
两篇GRIFFIN文章不能当成重复独立的寿命测量。

[[continuation-g19-taprogge-2014-129cd-isomer]]另提供电子探测的毫秒电磁异能态与tentative E3约束，
应与两个β母态的寿命/feeding区分；它不是同一GT分布的重复验证。

## Normalization is Part of the Observable

Saito TableII分别给对全部129Cd衰变的Iβ，以及按11/2−或3/2+母态分开的Iβ。
前者包含母态混合份额，后者的误差和归一也依赖该份额。
总控回读PDF8–10和关键表行：

| 女儿态Ex，keV | 对全部衰变的Iβ，% | 母态归一Iβ，% | 原文定位/边界 |
|---|---:|---:|---|
| 3150 | 24.1(9) | 11/2−：45(10) | TableII；3/2+列空白不等于上限或零 |
| 3184 | 10.4(5) | 3/2+：22(6) | TableII；11/2−列空白 |
| 3347 | 6.1(4) | 3/2+：13(3) | TableII；另有单独括号(3347)候选行 |
| 1354 | <3.3 | 11/2−：<6.3 | 上限保留，不能改确定测量 |
| 1761 | <1.2 | 3/2+：<2.6 | 不是3150主馈送45(10) |

这些原表数不是新拟合；logft、B(GT)、Iβ与母态T1/2相互有推导依赖。
不能把表中重复列和由它们计算的B(GT)当多项独立证据。
已有两母态不同分布使单一总率不足唯一固定组态或普适gA；
本任务没有将其近等寿命的原因分解成已测定的唯一相空间/矩阵元补偿。

## Model and Mass-version Contract

| 输入/模型 | 实际可用内容 | 尚缺/不可混用 |
|---|---|---|
| NA-14与jj45pna | 来源分别采用的相互作用/运行空间，可比较各自预测 | 不是同一Hamiltonian；共同CD-Bonn背景不保证矩阵元相同 |
| 所读NA-14 β计算 | 价空间允许GT及所用幅度q=.75的计算 | 本批未恢复完整允许+FF共同算符求解；不外推全理论界都无此方法 |
| Dunlop的q调整 | PDF5讨论LSSM以较短130Cd寿命重新标定.66→.75 | 不归给图中DF3/RHB两个QRPA模型，也不是普适gA测量 |
| Qβ与母态Ex | Saito采用AME2016 Qβ=9780(17)keV，并引2020质量工作Ex343(8)keV | 不同输入/评估版本，联合Cov未得；本页不报独立误差假设下的合成Q精度 |
| 130In质量 | Nesterenko独立质量约束含10−Ex58.6(82)keV | 质量差不等于完整β/EM分支；局部能量偏差不能证伪整套有效力 |

## Missing Observables and Competing Explanations

本批材料的GT/FF归属须保留自旋宇称及logft的候选性质；一个logft门限不是
跨所有核/所有跃迁的唯一分类定理。允许衰变常见的能窗五次方只能作近似，
FF的形状因子不能直接套用同一幂律。

现有原件未给可支持G19草案“Pn10–15%”或“价空间损失95%Ikeda强度”的数据，
相关数字已撤回。完整空间/算符的Ikeda代数总和与有限Q窗率、截断空间的实际计算
分别处理，不能用一个未核实的比例倒推淬灭。
TAGS是可能减轻漏计的一类测量，但仍需响应反解与母态混合约束；
不能称完全无偏，也不应声称缺少质量纯化时所有其它分离手段都不可能。

## Decision and Reproducibility

G22按TableII列界重建40行CSV，总控核查强态、上限、空白及归一差别。
CSV仅保留原表数值列；先前的无源上限和解释性标签已移除。其任务路径和版本说明在
`outputs/l3/20261107-nuclear-structure-continuation/G19/`，长期科学入口以本页/source为准。
下一步应冻结态对应、质量版、相互作用及GT/FF算符，预测未拟合分支；
没有共同输入不宣称已经完成真实核弱率的排他性检验。


## Research Trigger

母态归一、Q版本与GT/FF算符能否放入同一预测合同。


## Provisional Reasoning

本页比较从原表/算符到条件结论的推断；这些推断与作者实验报告分别标注，不视作新的独立测量。


## Assumptions

采用本页声明的态对应、单位、多极/旋转规范和所用模型范围；未给的联合Cov、原始响应或作者实现不补造。


## Competing Explanations

所选机制须与组态混合、占据变化及实际实验/有效算符依赖比较；与名义数据相容不等于唯一解释。


## Transfer Conditions

迁移到另一核素/核区前，重新核对同态身份、占据/配对、形状动力学和探针算符；仅质量数或名词相同不满足合同。


## Failure Conditions

若原件/态映射/算符规范改变、或必要响应未恢复，重新计算并收窄结论；不得以缺失伴随信号代替有灵敏度的排除。


## Falsification or Reverse Tests

回核Saito TableII的总混合和各母态归一、上限及空白。 本页没有未执行的真实核模型排他认证。


## Open Questions

一致质量版、Hamiltonian、GT/FF实现与实验Cov。


## Human Review

本任务未发生用户逐项审核；记录的是Agent原件自审，未伪装human-reviewed。审核标注不作为检索或使用资格门。


## Promotion or Rejection History

本批根据直接原件与独立核查修订worker草案，撤回无源数值/普适断言；本页保持provisional。具体触发证据和仍存边界见正文，不以结构检查替代物理核验。
