---
type: research-note
title: "136Sn中壳E2异常：多轨道两体解释与三体模型的可辨识性"
aliases: [Sn136 seniority and three-body identifiability]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
created_from: "Gemini two-paper bridge and parent primary/figure audit"
evidence_sources: [simpson-2014-136sn-138sn-seniority-isomers, maheshwari-2015-sn-isomers-effective-interaction, book-jain-nuclear-isomers]
tags: [136sn, seniority, three-body, multi-orbit, identifiability]
---

# 136Sn：非零中壳E2不唯一识别基本三核力

## Research Trigger

[[seniority-node-three-body-breaking-round2-20261107]]构造了单j内三体解除节点的例子。
本页回到真实核实验与多轨道两体模型，检验该例能否直接反演基本三核力。

## Grounded Evidence

[[simpson-2014-136sn-138sn-seniority-isomers]]的原件6页，TableI/级联给136Sn半衰期46(7)ns。
[[maheshwari-2015-sn-isomers-effective-interaction]]的5页预印本明确引用其
6+→4+₁实验B(E2)=24(4)e²fm⁴，并用不同有效相互作用比较。

2015文Fig.1与pp.3–4给：

| 136Sn模型量 | RCDB | RCDBMO（指定TBME减25keV） |
|---|---:|---:|
| B(E2;6+→4+₁) / e²fm⁴ | 14.5 | 22.0 |
| B(E2;6+→4+₂) / e²fm⁴ | 53.1 | 46.4 |
| B(E2;4+₁→2+₁) / e²fm⁴ | 28.0 | 95.3 |
| 计算E(6+)−E(4+₂) / keV | 42 | 63 |

这些是模型输出，没有在本轮重跑大空间壳模型。
同一实验被两篇引用不能增加独立实验数。

## Provisional Reasoning

### 理想单j计数与真实模型空间

136Sn相对132Sn有n=4价中子；若全部限制在f7/2，Ω=4，
同v=2的6+→4+态对处于理想节点。
但2015计算的空间含六条中子轨道，不能用单j定理禁止其组态混合。
只调节有效两体TBME也能使计算B(E2)接近测量值，
说明这一个非零强度不是显式价空间三体或基本3N的唯一判据。

### 两末态强度的条件两态图像

下面是本任务的简化推断，不是从论文读出的seniority概率。
若初态固定，理想相消通道为零，两个正交4+态仅旋转混合v=2/4，
则B1=sin²θ S、B2=cos²θ S，和S保持不变。
把论文两套输出代入：S从67.6到68.4e²fm⁴，相差约1.18%；
B1/S从0.2145到0.3216。
这提示可用“总强度是否近守恒＋分支如何重分配”检验两态近似，
但这些数不是模型无关的真实seniority概率。
论文B2已经属于物理混合末态，不能再把它当纯v=4强度乘一次混合概率。
多轨道、初态变化、算符和额外4+态都会破坏简单两态关系。

### 三种不同的三体语言

显式残余价三体算符、经验有效两体单极修正、
以及对一个**已指定**微观3N力做正规序再截断，是不同概念。
正规序确可产生零/一/二/三体分量，但是否丢弃残余三体、用何种核芯与密度，
必须逐计算核对。不能把所有经验TBME调节都说成已从手征3N正规序推导。
2015这篇的25keV修改不是对本轮toy λ的标定。

## Assumptions

实验自旋沿原论文保留括号指定，采用作者提取的B(E2)，
不另加无直接出处的ICC或“100%分支”。
n=4的精确节点只对纯单j、指定算符和对应态适用。
两态强度推断另要求固定初态与完整两态子空间，未把它当已验证的真实核模型。

## Competing Explanations

多轨道波函数混合、有效算符、芯极化与显式/诱导三体均可能影响观察。
匹配一个强度不证明某相互作用普遍正确，也不排除物理3N的贡献。
2014文的150keV与2015文的25keV属于不同基线，不能直接作为模型优劣的唯一指标。

## Transfer Conditions

把对称性节点用于跨区比较时，先确认单j近似、粒子/空穴、允许v及算符。
从Sn迁移到其它区域时，体数、价空间和有效算符的共同变化比A标签更关键。

## Failure Conditions

没有统一多轨道Hamiltonian和算符时，不由一个B(E2)反推出唯一3N耦合。
未重放NuShell就不宣称本文重新验证了所有原模型结果。
单j三体例子的成立也不排斥多轨道两体解释。

## Falsification or Reverse Tests

联合6+到两个4+及4+→2+强度、能级顺序和其它核的对应态，
比单独6+→4+₁更有区分力。理论42/63keV支路能量不是实验已观测的弱线；
搜寻前需先查后续能级状态和实际探测/转换灵敏度。
不沿用草案误放134Sn能级得到的136Sn“30–40keV”预报。

## Open Questions

未来对4+态和旁路的测量可限制混合，但最新发现状态尚未穷尽检索。
完整多轨道误差预算、独立算符及基本3N与经验相互作用的连接仍需进一步工作。

## Human Review

本次为Gemini文献学习与总控原件/图表自审，无新增人工审核事件。

## Promotion or Rejection History

2026-11-07建立真实核与受控三体模型的桥接，
撤回草案的绝对“完美复现”、无出处ICC/支路闭合、错误旁路能量及所有经验力等同NO2B等表述。
保留有原件定位的24(4)、14.5→22.0及联合观测的可检验问题。
