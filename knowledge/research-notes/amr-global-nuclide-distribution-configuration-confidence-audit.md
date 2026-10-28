---
type: research-note
title: "AMR全球核素分布、配置演化与证据置信度审计"
aliases: [AMR global nuclide distribution, AMR evidence confidence audit]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [kumar-2023-amr-review, amr-cd-isotopes-quantum-termination-odda-signature-audit, amr-pd-four-hole-geometry-evolution-audit, amr-j2-dynamic-inertia-endpoint-audit, qiao-2025-pd-systematic-amr-metadata, diwanshu-2025-106cd-amr-metadata, chauhan-2025-100ru-amr-metadata, chauhan-2024-101ru-amr-metadata, joshi-2026-97-99mo-amr-metadata]
created_from: Day26 delegated global AMR distribution and configuration comparison
promotion_target: antimagnetic-rotation
tags: [antimagnetic-rotation, evidence-gradient, Pd, Cd, Dy, In, lifetime, BE2, configuration]
---

# AMR全球核素分布、配置演化与证据置信度

## Research Trigger

本页把Kumar等综述Table 3的40条结构逐带拆开，回答三个问题：哪些AMR归属有绝对寿命和实测B(E2)支撑，哪些主要是ΔI=2级联或模型解释，Cd/Pd/Dy的价核子几何有什么真正可迁移的共同点，以及“AMR”这个标签在新文献中怎样避免被自动升级为实验事实。该页只推进Day26研究知识，不创建新的run、deadline或课程学分。

## Grounded Evidence

Kumar Table 3的逐带抽取、寿命/B(E2)字段和页码定位见本页所列CSV/JSON工件；已有Cd、Pd、J(2)审计页提供独立的模型与单位边界。

## Provisional Reasoning

本页将绝对寿命、派生B(E2)、模型配置和竞争解释分开，不把综述标签当作实验事实。

## Evidence Rubric

| Tier | 进入条件 | 可以说什么 | 不能说什么 |
|---|---|---|---|
| A | 至少一组绝对寿命（DSAM/RDDS等）并由此得到多个B(E2)，总体随自旋下降或与剪刀闭合相容，且配置/模型不自相矛盾 | “直接电磁强度证据最强的AMR候选/代表” | 不能把模型配置写成波函数唯一解，也不能把所有强度下降归因于剪刀闭合 |
| B | 有部分寿命或B(E2)，但点数少、趋势有反弹、能级不规则或作者保留竞争解释 | “有直接约束但仍需限定的候选” | 不能称为无争议确立 |
| C | 主要是ΔI=2级联、J(2)或模型计算；缺绝对寿命/B(E2) | “文献候选/模型候选” | 不能由级联本身证明AMR |
| D | 仅综述提及、结构类比或元数据入口 | “待检索的新入口” | 不能抽取配置、寿命或AMR判据 |

本轮40条结构的机械统计为A=7、B=9、C=22、D=2，分布在28个核。逐带记录见[`amr_global_inventory.csv`](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-global-distribution-20261029/amr_global_inventory.csv)，机器可读版本见[`amr_global_inventory.json`](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-global-distribution-20261029/amr_global_inventory.json)。这些Tier是本任务的证据分层，不是Kumar原文的官方等级。

## Global Distribution from Kumar Table 3

Kumar综述Table 3（PDF pp77–86）实际覆盖28个核、40条结构。Pd、Cd和In构成主体；其余入口包括58Fe、61Ni、82Kr、127Xe、130Ba、137Nd、142,143Eu和144Dy。综述正文同时提醒：许多结构没有绝对寿命、B(E2)或B(M1)，并明确把99Pd、102Pd、110Cd、110In、112In和144Dy等列为较不确定案例。因此表中的“AMR”不能直接当作统一实验结论。

最强的直接约束集中在：

- **104Pd band 1（A）**：16–26 ħ有六个寿命点，B(E2)从0.26(3)降至0.07(1)，顶端为>0.02；J(2)/B(E2)从112(9)升至554(80)。这满足“寿命→绝对B(E2)→整体下降”的主证据链，但仍允许形变收缩、配对和四准粒子重排共同作用。
- **105Cd band 1（A）**：27/2−至43/2−有五个寿命点，B(E2)总体由0.126降至0.052 e²b²；35/2−→39/2−有中心值小反弹，落在误差约束内，不能强写成严格逐点单调。
- **106Cd bands 2/3（A）**：两条带分别有四点和五点寿命及B(E2)下降。band 2为0.37(1)→0.04(2)，band 3为0.42(1)→0.10(1) e²b²；二者的J(2)/B(E2)在高自旋显著增大。band 1只有模型计算，降为C。
- **107Cd bands 1/2（A）**：两条signature partner均有五个寿命点，B(E2)分别由0.208降至0.044和由0.183降至0.034 e²b²，Qt同步下降；这是奇A Cd中最完整的成对证据之一。
- **108Cd band 1（A）**：四个寿命点和0.19(2)→0.11(3) e²b²下降，属于经典直接证据，但下降幅度和J(2)/B(E2)并不要求所有AMR都共享同一数值阈值。

B层中，100Pd只有少数寿命/B(E2)点；101Pd和103Pd有较完整的寿命与下降趋势，但存在配置分歧和集体转动竞争；109Cd band 3有四个寿命点与总体下降但39/2点反弹；110Cd虽有寿命和B(E2)序列，能级间距不规则且综述明确提醒其归属较不确定；142,143Eu有直接寿命和B(E2)，但配置/终止解释仍未收敛。

C/D层中，99Pd、102Pd、103Pd bands 2/3、109Cd bands 1/2、111Cd、In多条带、127Xe、130Ba、137Nd和144Dy主要缺绝对电磁强度或只靠TAC/SCM/粒子-转子计算。特别是144Dy的πh11/2²⊗νh11/2⁻²只是一种可能配置，表中没有B(E2)数值，并且能级被标成quasi-rotational；它不能与104Pd或105Cd并列为直接确立AMR。

## Configuration Comparison

### Cd: πg9/2空穴与中子刃的同区演化

Cd（Z=48）最稳定的图像是π(g9/2)⁻²空穴提供一对近似反向横向磁矩，中子端由h11/2与g7/2、d5/2占据或准粒子对齐补足角动量。105–108Cd的实测B(E2)下降和Qt下降支持横向分量逐渐闭合，但不同质量数的中子配置、配对和形变并不相同。106Cd band 2/3与107Cd双带的强度证据最完整；110Cd的较慢下降和不规则能级说明核芯惯量、对齐和非理想四刃几何不能被忽略。

此前的量子审计已经限定：g9/2²或h11/2²的单j最大角动量只能约束冻结子空间，不能作为全核AMR终止上限；奇A核在保持合适的半整数签名对称时仍可让横向磁矩分量相消。因而“剪刀闭合=配对严格崩溃”不是实验判据。

### Pd: Z=46时空穴数与模型图像不能混同

Pd（Z=46）更靠近Z=50闭壳层下方，文献中既出现π(g9/2)⁻²的有效粒子-转子配置，也出现π(g9/2)⁻⁴的奇A/高自旋配置。104Pd的实验带通常用π(g9/2)⁻²⊗ν(h11/2)²(g7/2/d5/2)²描述；PNC计算则显示四个部分空的g9/2质子空穴，低频配对和非对角占据使“每个空穴都是一根独立经典刃”不成立。四刃几何能解释横向磁矩和Q21相消的对称性，但不能单独预测绝对B(E2)、配对演化或终止交叉。

103Pd的band 1具备实测B(E2)下降和寿命，是Pd中仅次于104Pd的直接约束案例；其bands 2/3虽被后续模型赋予AMR解释，仍没有对应绝对强度，故降为C。99Pd和102Pd的“possible mixed collective/AMR”更应保留为候选。

### Dy: 结构类比成立，实验阶梯不成立

144Dy的πh11/2²⊗νh11/2⁻²把质子粒子和中子空穴放在同一高-j轨道，形式上可产生反磁双剪刀类比。但Kumar Table 3没有绝对寿命或B(E2)，且能级序列不满足简单转子单调性；因此只能是C层候选。它提供“不同质量区也可构造双剪刀”的模型启发，不能成为Cd/Pd实验证据的替代。

## Newer-Literature Boundary

本轮从Crossref保存了三个综述截止后或相邻的新入口：100Ru（2025）、101Ru（2024）和97,99Mo（2026）。它们的题名分别含“possible antimagnetic rotation”，但本轮没有取得正文、寿命或B(E2)表，因此均保持D层元数据边界；详见[[chauhan-2025-100ru-amr-metadata]]、[[chauhan-2024-101ru-amr-metadata]]和[[joshi-2026-97-99mo-amr-metadata]]。同理，[[qiao-2025-pd-systematic-amr-metadata]]和[[diwanshu-2025-106cd-amr-metadata]]只能说明新理论/综述入口，不能把103/105/107/109Pd或106Cd升级为实验确立。

## Evidence Gradient and Practical Decision Rule

对一个新AMR候选，按以下顺序判定：

1. **身份响应**：是否有稳定ΔI=2带、M1/E2混合和极化/角分布约束？只有这一级时最多C。
2. **绝对时钟**：是否有DSAM、RDDS或等价绝对寿命，且feeding/side-feeding与stopping修正可追溯？没有绝对时钟不能声称测得B(E2)。
3. **强度轨迹**：B(E2)是否在明确自旋区间内下降，误差和effective lifetime脚注是否被保留？局部反弹不能被删掉。
4. **结构检验**：配置、J(2)/B(E2)、Qt、g因子或模型是否共同支持横向磁矩相消？模型预测必须与实验量分栏。
5. **竞争解释**：是否排查形变收缩、普通集体转动、背弯、配对重排、带交叉、终止和实验系统学？若不能排查，最多B。

因此，“AMR带”应写成证据带有层级的复合主张：直接测量建立电磁强度，派生B(E2)给出趋势，模型才解释剪刀几何。ΔI=2级联和大J(2)/B(E2)本身不能越级。

## Reproducible Artifacts

- [`amr_global_inventory.csv`](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-global-distribution-20261029/amr_global_inventory.csv)：40条逐带记录。
- [`amr_global_inventory.json`](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-global-distribution-20261029/amr_global_inventory.json)：同一记录的机器可读版本。
- [`inventory_summary.json`](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-global-distribution-20261029/inventory_summary.json)：28核、40带和A/B/C/D计数。
- [[kumar-2023-amr-review]]：105页综述PDF，Table 3 pp77–86为主定位。

## Competing Interpretations and Limits

实测B(E2)下降可由剪刀闭合、形变收缩、配对变化、粒子对齐、四准粒子交叉和核芯惯量共同造成；本页不把它们压缩成单一因果链。综述表格中的空白可能表示未测、未列或本轮未取得原始表，不能统一解释为零。各带之间也存在同一实验campaign的谱学依赖，不应把论文、综述和理论重复计为独立证据。

本轮分类依赖Kumar综述的整理和现有Day26来源页；A层是“直接证据最强”，不是人审后的最终确证。所有页面保持`review_status: unreviewed`，Codex self-audit不写成`human-reviewed`。

## Sources

- [[kumar-2023-amr-review]]
- [[amr-cd-isotopes-quantum-termination-odda-signature-audit]]
- [[amr-pd-four-hole-geometry-evolution-audit]]
- [[amr-j2-dynamic-inertia-endpoint-audit]]
- [[qiao-2025-pd-systematic-amr-metadata]]
- [[diwanshu-2025-106cd-amr-metadata]]
- [[chauhan-2025-100ru-amr-metadata]]
- [[chauhan-2024-101ru-amr-metadata]]
- [[joshi-2026-97-99mo-amr-metadata]]

## Human Review

Codex source/claim self-audit；保持`unreviewed`。本页没有改变Day21–Day25学分、人审或撤回边界。

## Continuation Handoff

下一轮若继续AMR，优先取得82Kr、100Ru、101Ru和97,99Mo原始正文或开放数据；其次对100Pd/101Pd/103Pd原始寿命表做side-feeding与不确定度复核；最后用同一PNC/TAC观测量合同比较Cd、Pd与Dy，测试绝对B(E2)、Qt和J(2)/B(E2)能否在同一配置空间中同时拟合。


## Assumptions

Tier A/B/C/D只用于本轮证据审计；表格缺失视为“未提供/未核验”，不解释为零。Kumar PDF页码按实际105页PDF打印页定位。

## Competing Explanations

B(E2)下降还可能来自形变收缩、配对和准粒子对齐、带交叉、终止、核芯惯量和寿命系统学。

## Transfer Conditions

可迁移的是绝对时钟优先、B(E2)误差保留和模型/实验分栏；具体配置、形变和J(2)/B(E2)阈值不能跨核无条件迁移。

## Failure Conditions

若把ΔI=2级联、综述列名或模型预测当作绝对寿命证据，或删掉effective lifetime、上限和非单调点，本页分类失效。

## Falsification or Reverse Tests

取得原始DSAM/RDDS表后，逐点重算寿命到B(E2)，加入side-feeding/stopping协方差，并比较普通集体转动、终止和AMR模型的留出预测。

## Open Questions

新近100Ru、101Ru、97,99Mo候选是否有正文寿命？103Pd和106Cd新理论能否提供绝对强度而非只给计算趋势？144Dy是否存在可追溯的RDDS/DSAM数据？

## Promotion or Rejection History

2026-10-29：建立40带/28核逐带清单；A层定义为直接电磁证据最强而非人审确证，新增文献保持元数据边界。
