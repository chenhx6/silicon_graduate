---
type: research-note
title: "102Ru补充材料：106行光子跃迁、相互作用定义与尚未闭合的数据边界"
aliases: [102Ru PRL Supplemental Material, continuation-g14-ru102-si-thesis-20261107]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [saracino-2026-102ru-scissors-octupole-resonances, campaign-g12-saracino-2026-thesis]
created_from: "G14 acquisition and transcription; parent primary-source audit"
promotion_target:
tags: [102ru, nrf, e1, m1, supplemental-material, tac-qrpa, covariance]
---

# 102Ru补充材料带来的证据变化

## Grounded Evidence

[[saracino-2026-102ru-scissors-octupole-resonances]]所引SI已实际取得：
`raw/papers/gpt/query/20261107-continuation-G14/102Ru-PRL-136-252501-Supplemental-Material.pdf`，
5页、322835字节，SHA256 `8b9fba94fd43ea2af1860029889c0cb3e30ebb3c2cc29a5e0d749649c93a2df0`。
这是主PRL的附件，和主文同一实验/模型，不能另计为独立实验。
G14转录TableI；总控回读SI1–5、TableI标题/代表行、Eqs1–5及图注，独立重算表的计数与和。
106行并不等于106项统计独立的测量，也不意味着全部非弹性支路或探测器响应已恢复。

| SI位置 | 实际新获得内容 | 保留边界 |
|---|---|---|
| pp1–3 TableI | Ei、Eγ、BR、不对称度、多极标签及B(M1)↑/B(E1)↑ | 无完整联合Cov、事件或效率响应；括号标签保留 |
| p3 Eqs1–4 | hmho、推转项及ISDD/ISJJ/IVSS/IVJJ/IVDD/IVOO可分相互作用的形式 | 未提供全部作者生产代码、基底/矩阵与完整运行卡 |
| pp3–4 SecIII/Fig1 | TAC角动量—频率比较；正宇称回弯的双h11/2准中子解释 | 是模型比较；不是本任务独立拟合或组态直接测量 |
| pp3–4 SecIV/Eq5/Fig2 | κIVDD由100Mo的IVGDR峰位置约束；SLO比较 | 102Ru无同样吸收截面数据的来源边界须保留 |
| p5 refs | 四条所引来源身份 | 参考列表存在不证明被引原件均已读 |

## Table Reconstruction

106行分布为SI1的38行、SI2的51行、SI3的17行。按表中多极标签，
M1有34行（含1个括号标签），E1有72行（含6个括号标签）。
BR<1有40行，BR=1有66行。此处“无括号”只描述原表指定方式，不宣称所有Jπ已由本任务独立确证。

总控对已转录的原报上跳列重算：

| 表列求和范围 | ΣB(M1)↑，μN² | ΣB(E1)↑，e²fm² |
|---|---:|---:|
| 包含原表括号标签 | 1.660 | .15408 |
| 仅无括号标签 | 1.646 | .12713 |

这些是本任务表列算术，不是作者重新测得的额外强度，也不是全能区完备求和。
1.660与主文约1.7的概述相容，不应写为“严格相等”。
由Eγ筛取4.5≤Eγ<5.5 MeV的E1有38行，名义和为.10137 e²fm²。
其中5080.93(31)-keV线贡献.05(4) e²fm²，约占这一名义和49.3%，
其BR为.12(11)（SI2 TableI）。这说明精确分支信息很可能影响该窗口的定量强度；
没有联合似然不能断言总误差已由此单项完全决定，也不能将删除该线当作真实修正。

两个原行抽查：SI1的2953.2(1.9)-keV线标`(E1)`，BR=1、B(E1)↑=.016(5)；
SI2的4528.8/4528.6(4)-keV行标E1、BR=.34(19)、B(E1)↑=.0015(6)。
原表Ei−Eγ的差值不能凭小数位数单独验证核反冲理论，也不能由BR边际误差认定B误差的唯一来源。

## Direction, Branching and Feeding

原表报告上跳B。CSV中的下跳列是按0+↔1的详细平衡关系除3所得，属于推导；
括号标签在主下跳列留空，条件列才给出“若为偶极”的数值。
原始上跳强度自身也沿用作者的多极假设；不能先把未知自旋改成2，再仍用原偶极强度直接除5。

在只考虑无feeding的弹性NRF提取、保持散射强度与其它输入固定时，
`Is∝Γ0·BR`意味着采用BR=1会给较小的Γ0。
这是一条条件推断，不是对全部66行的无条件实验下限证明：
feeding、未分辨支路及效率/背景都可能影响所提取的散射强度。
表中BR=1无误差条也不等于“已测得严格100%支路”。
SI没有补齐完整feeding/响应处理的事件级输入，窄束不能被写成严格消除所有feeding。

## Hamiltonian and Interpretation Boundary

SI p3给出hmho−ω·JIS，以及ISDD、ISJJ、IVSS、IVJJ、IVDD、IVOO六项标量耦合。
具体耦合常数和有效E1算符须与主文PDF4–6一同阅读；SI本身不是完整数值实现。
主文将b=.009 fm^-2与κIVOO=4κ3sc用于共同描述累计E1，
不能从“共同拟合”独自推出两参数强相关的数值结论、严格退化或唯一最优解。
SI公开逐态表使后续诊断更具体，但完整Cov/似然、响应函数及作者运行卡仍缺。
IS伪模处理的符号和单位须按作者的标量耦合约定解释，不将负κ直接口称“强吸引”，
不补写原文未给的伪模能量阈值。

## Thesis and Cross-region Transfer

[[campaign-g12-saracino-2026-thesis]]仍无实际PDF。
UNC连接超时、索引pdf_url为空或CORE403都不能证明学位论文处于embargo、校园防火墙限制，
也不能证明全球无合法镜像。本批只关闭SI实际获取缺口，未关闭博士论文正文缺口。

低自旋E1响应、直接E3矩阵元、静态八极结构和高自旋手征几何是不同观测层。
TAC-QRPA的八极诱导E1是作者解释，NRF未直接测得E3或静态D0。
跨区迁移须指定质/中子占据、形变、配对、有效算符与相互作用，并比较其它偶极解释。
100Mo和102Ru均N=58，98Mo和100Ru均N=56；这两组同中子素比较须分别保留。

## Reproducibility and Decision

原表转录的计算副本位于`outputs/l3/20261107-nuclear-structure-continuation/G14/`；
它是从PDF生成的转录，不能冒充出版商原始CSV。raw中worker保存的同名副本也保持此派生身份。
下一步优先核查5081.22-keV母态的分支与原报误差传播、累计Cov及算符敏感性；
不凭表公开就宣称全部模型和实验数据缺口闭合。
本页经过父代理原件自审；原worker关于UNC限制原因、严格强相关、完整闭合和全部独立测量等断言均已撤回。


## Research Trigger

102Ru SI已取得，需分清逐态表、BR与完整响应。


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

核查SI逐态字段和谱线，而非假定106行独立。 本页没有未执行的真实核模型排他认证。


## Open Questions

完整Cov、响应与作者运行卡。


## Human Review

本任务未发生用户逐项审核；记录的是Agent原件自审，未伪装human-reviewed。审核标注不作为检索或使用资格门。


## Promotion or Rejection History

本批根据直接原件与独立核查修订worker草案，撤回无源数值/普适断言；本页保持provisional。具体触发证据和仍存边界见正文，不以结构检查替代物理核验。
