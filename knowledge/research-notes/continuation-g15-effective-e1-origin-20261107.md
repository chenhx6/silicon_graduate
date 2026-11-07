---
type: research-note
title: "102Ru有效E1的稀土文献来源与跨区匹配合同"
aliases: [effective-e1-operator-hamamoto-hagemann]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [continuation-g15-hamamoto-1989-plb226-dipole-octupole, continuation-g15-hagemann-1993-prc47-octupole-softness, saracino-2026-102ru-scissors-octupole-resonances]
created_from: "G15 primary acquisition and extraction; T02 theoretical audit; parent integration"
promotion_target:
tags: [102ru, rare-earth, e1, octupole, effective-operator, model-matching]
---

# 稀土有效E1与102Ru：应迁移哪些内容？

## Grounded Evidence

[[continuation-g15-hamamoto-1989-plb226-dipole-octupole]]为5页PLB原件，
[[continuation-g15-hagemann-1993-prc47-octupole-softness]]为11页PRC原件。
前者p19 Eqs2–3明确写Wigner D1的实验室旋转与内禀eeff·rY1+e·bνr³Y3；
后者p2011 Eqs4–5给出极化参数对RPA模矩阵元与模能量的依赖。
两篇研究是理论谱系，不能作为又两次独立102Ru实验。
G15取得全文，Terra针对实际原式独立核查；完整推导见
[[continuation-t02-ru102-covariant-effective-e1-20261107]]。

## Provisional Reasoning

| 要比较的层次 | 稀土原文 | 102Ru实际模型 | 不能越过的边界 |
|---|---|---|---|
| 系统/态 | 形变奇A核低能yrast跃迁、准粒子—转子/声子 | 偶偶核基态NRF偶极响应、TAC-QRPA | 不能只因b数量级相近就认定共同结构 |
| 探针 | eeff·rY1+e·bνr³Y3 | eeff·(rY1+bνr³Y3) | 八极项电荷因子不同，先统一定义 |
| 极化 | 本例静态近似、模式依赖的b0/b±1 | 共同b=.009fm^-2并配IVOO适配累计E1 | 需要能量/模型空间/响应匹配；两者均非普适常数 |
| 旋转 | 明确的D1内禀—实验室关系 | 采用内禀分量的QRPA表达 | 不等于已恢复作者全部投影/代码 |
| 误差与拟合 | 数据与模型依赖的参数 | b与κ共同拟合 | 同曲线拟合不自动证明强相关、严格退化或唯一解 |

## Tensor and Symmetry Conditions

Wigner D1表示能够构造实验室rank1。单一最低阶[Q2⊗O3]1是一个有条件的
协变例子，不是上述转子表示的唯一或普遍逐项同义表达。
Terra在标准球谐和冻结轴向Q2背景下得到b±1/b0=√(2/3)，
与共同b不同；更一般协变背景仍可构造共同b，因此不能据此宣布PRL表达不合法。
这些是本任务推导，不归给1989/1993作者。

轴对称良好K下的直接rank1耦合限制属于指定模型。
三轴性使K不再严格守恒，但不消除所有残余对称性，也不保证所有K分量有可观强度。
对现实γ软核，必须通过波函数/算符计算混合，而不能口头“解禁”所有模式。

## Static Approximation and Alternative Explanations

旧文低Eγ与八极模式能量的分离支持其使用静态极化。
迁移到102Ru约5MeV响应时，需指定实际消去空间、能量分母、相位和顶角匹配。
最低3−能量不等于所有中间态分母，故能量比较不能单独证明必然失效或必然有效。
同一关联是否在QRPA波函数与有效算符中重复计算，也须实际空间匹配才可判断。

相同累计强度可受到组态混合、一般偶极极化、两声子等解释影响。
2.95MeV态在SI标(E1)，作者提出两声子“可能性”；未再现不等于该能量所有单声子
响应严格为零。下一步需要同态绝对E1/E2/E3与理论复响应，而不是增加无源阈值。

## Correction and Decision History

Terra核图发现Hagemann p2017 Eq8两数应为−4.8×10^-5、+1.58×10^-5 MeV fm^-6，
G15草案曾误写大100倍；本批已纠正source和本页，保留原件。
其余无条件协变等价、全K解禁、严格零值、强共线和量纲不全D0公式均已撤回。
本页保持条件研究合同，不是2026作者实现的独立复现或静态八极认证。


## Research Trigger

稀土有效E1能否按相同定义迁移到102Ru。


## Assumptions

采用本页声明的态对应、单位、多极/旋转规范和所用模型范围；未给的联合Cov、原始响应或作者实现不补造。


## Competing Explanations

所选机制须与组态混合、占据变化及实际实验/有效算符依赖比较；与名义数据相容不等于唯一解释。


## Transfer Conditions

迁移到另一核素/核区前，重新核对同态身份、占据/配对、形状动力学和探针算符；仅质量数或名词相同不满足合同。


## Failure Conditions

若原件/态映射/算符规范改变、或必要响应未恢复，重新计算并收窄结论；不得以缺失伴随信号代替有灵敏度的排除。


## Falsification or Reverse Tests

比较两文原式、电荷因子、模能量分母及1993参数修正。 本页没有未执行的真实核模型排他认证。


## Open Questions

一致的空间划分、能量依赖与算符匹配。


## Human Review

本任务未发生用户逐项审核；记录的是Agent原件自审，未伪装human-reviewed。审核标注不作为检索或使用资格门。


## Promotion or Rejection History

本批根据直接原件与独立核查修订worker草案，撤回无源数值/普适断言；本页保持provisional。具体触发证据和仍存边界见正文，不以结构检查替代物理核验。
