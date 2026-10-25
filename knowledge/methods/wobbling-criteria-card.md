---
type: method
title: 摇摆运动判据卡（Wobbling Criteria Card）
aliases: [wobbling criteria card, wobbling identification card, 摇摆运动判据卡]
created: 2026-10-24
updated: 2026-10-25
status: ai-draft
review_status: unreviewed
method_type: collective-mode-criteria-card
tags: [wobbling, phonon, evidence-boundaries, counterexamples]
---

# 摇摆运动判据卡

## Purpose

Day22判据卡：分开模式定义、谐声子近似、实验支持和竞争解释。checkpoint091替换旧080卡；旧卡的数值硬门限与排他改判全部撤回。本文仍为self-audit，不代表用户审核。

## Inputs and Assumptions

逐线核素、带身份、自旋宇称、母末态、能量、光子分支、多极混合比及其相位约定；若需绝对B值，还需寿命、总分支和内转换。模型另列三轴形状主轴、惯量排序、准粒子取向、参数/算符及适用spin区间。

## 必要检验、支持条件与反证

| 层级 | 应检验的对象 | 支持条件 | 反证或降级条件 |
|---|---|---|---|
| 几何定义 | 在指定粒子–转子约定下，j相对最大惯量轴的方向；进一步区分完整模型的进动拓扑 | F14将平行称longitudinal、垂直称transverse | 未确定轴/惯量顺序时，不从Ewob单调升降命名几何 |
| 谐声子适用域 | 对所用Hamiltonian检查局部稳定性、小角展开与有限spin修正 | F14 Eq.(23)明确检验横向分量远小于总J² | 接近不稳定点HFA失效；这不自动排除完整量子模型的拓扑模式 |
| 电磁模式支持 | 同母态的out/in E2约化强度、M1/E2混合、寿命支持的绝对B | 集体带间E2增强与统一模型几何相容，是重要支持 | E2光子份额大不等于绝对E2增强；两准粒子候选可以M1占优，不设跨核统一δ或W.u.阈值 |
| 声子阶梯 | 同spin定义/插值下的能量与相邻阶矩阵元标度 | 谐极限能量近等间距、相邻阶强度随n增加 | 非谐性和组态混合允许偏离，不能由单条Δn≈2支路判所有声子解释失败 |
| 实验辨识 | 多条连接线的角分布、P或计数不对称A、校准Q(E)、门条件及统计/系统误差 | 联合观测显著区分所竞争δ分支 | 只有偏振正负号、未排除第二分支或受污染弱线时，保留选解边界 |
| 竞争解释 | signature partner、TiP、振动耦合、组态交叉等对完整观测向量的预测 | 独立观测能区分所比较解释 | 能谱或相近alignment单独不能唯一识别；缺数据不是证明机制不存在 |

依据：[[frauendorf-2014-transverse-wobbling]] F14-D22-R091-1、F14-D22-R091-2；[[hamamoto-2003-quantized-wobbling-excitations-alignments]] H03-D22-R091-1；[[chen-2019-transverse-wobbling-even-even]] CH19-D22-R091-1。

## 定义分歧与适用域

Lawrie2020将wobbling用于要求n量子化的谐近似；Chen–Frauendorf2022将其用于可非谐的完整PTR拓扑。f不小可挑战前者对应展开，不自动否定后者的分类；应明确所检验定义。见[[lawrie-2020-tilted-precession-wobbling]] LAW20-D22-R093-1及[[chen-2022-study-wobbling-spin-coherent-state-maps]] CF22-D22-R093-1。

## 四列证据练习

| 候选带 | Band energy | In/out strengths | Alignment | Polarization |
|---|---|---|---|---|
| 163Lu TSD2/TSD1 | 相邻带能量与随spin演化，原文支持一声子解释 | OD01平均δ=−3.10(+.36/−.44)，为E2份额约90.6%；原文相对比与本轮未重读的寿命文献分开 | 相近i_x/J(2)支持共同结构；Harris参考明确 | 原文联合DCO/AD/偏振选大模，不把某一符号推广为普适规则 |
| 135Pr side/yrast | Matta2015与Lv2022的能谱及候选TW2重组需按各自图核 | Lv2022的813.2/726同母态rE2=.12(.08)；不冒充绝对W.u. | TiP/QTR重取向是模型解释；不能宣称实测固定j方向 | 新采集联合P–Rac给小δ，与早期支持数据有争议，需保留两套实验谱系 |
| 136Nd L3/L1 | Eq.(4)/Fig.4下降Ewob，作者支持两准粒子TW | 751 keV rE2=.36(.17)、rM1=.61(.29)，不是绝对寿命B值 | 刚性两准粒子j=10为模型输入；E2/M1参数由单点定标 | 仅751线可联合提δ=−.48(+.13/−.14)，约19% E2；另外三条污染/弱 |

逐线来源：[[odegard-2001-evidence-wobbling-163lu]] OD01-D22-001；[[lv-2022-evidence-against-wobbling-135pr]] L22-D22-002；[[lv-2022-transverse-wobbling-136nd]] LV22-D22-R091-1、LV22-D22-R091-2。扩展矩阵见[[wobbling-geometry-phonon-observable-contract]]。

## “近简并＋强E2”的反证练习

135Pr争议说明：两条带和下降Ewob不足以固定声子标签；早期大δ对应的相对E2证据会受后续小δ分析挑战。大δ本身仍只描述同一跃迁的光子混合，无法给绝对集体强度。TiP或其他耦合机制也须用电磁、组态和近似有效域共同比较，不能从早期指认受挑战直接得出替代理论唯一正确。

一个可证伪问题：对同一母态的干净两条退激支路，以共同校准响应同时比较δ分支，再测寿命得到绝对B(E2)；各候选模型能否在不复用该点定标的情况下预言另一条连接线？

## What It Can Establish

建立可追溯观测清单、适用条件和区分性实验问题；说明哪个观测支持哪个范围。M1占优的两准粒子原文是检验旧普适规则的反例，不是本卡已确证任一候选模式的证明。

## What It Cannot Establish Alone

不由本卡证明全核区只有一个摆动核、不设统一85% E2或15–30 W.u.门限，不从邻核低spin S(4)推断奇A高spin势能面或耗散宽度。未知寿命、角响应协方差和模型输入须保留为未知。

## Sources

- [[frauendorf-2014-transverse-wobbling]] F14-D22-R091-1、F14-D22-R091-2。
- [[hamamoto-2003-quantized-wobbling-excitations-alignments]] H03-D22-R091-1。
- [[odegard-2001-evidence-wobbling-163lu]] OD01-D22-001。
- [[matta-2015-transverse-wobbling-135pr]] M15-D22-001。
- [[lv-2022-evidence-against-wobbling-135pr]] L22-D22-002。
- [[chen-2019-transverse-wobbling-even-even]] CH19-D22-R091-1、CH19-D22-R091-2。
- [[lv-2022-transverse-wobbling-136nd]] LV22-D22-R091-1、LV22-D22-R091-2。

## 判据卡原子陈述

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WOB-CARD-080-1 | 旧080五项通用数值门限撤回；当前卡按模型定义、适用域、相对/绝对强度、偏振选解及竞争解释分层，不认证全核区唯一或全部证伪。 | task-correction | source-bounded-synthesis | 本卡checkpoint091；F14 Eq.(21)、CH19 Table I、LV22 Figs.3–5 | true |

## 模型定标与独立检验点：105Pd控制

[[timar-2019-transverse-wobbling-105pd]] TI19-D22-R103-1/2的三条大δ由DCO/P联合测量支持，主线不应因另一核的争议预先否决。TI19-D22-R103-3明确g_eff×.36按一条δ定标、惯量按能量拟合；区分输入定标、同源派生量和额外可检验点。固定wavefunction/E2时M1∝g_eff²，单个幅度调节不能代替对全部组态/分支/寿命的独立验证；也不应因有调节就抹去实际电磁支持。needs_review: true。

## Day22 checkpoint105：wobbling–scissors耦合不同于磁转动分类

[[frauendorf-2024-wobbling-review]] F24-D22-R105-1–3核review的QRPA说明及图量：Fig35纵轴为绝对B(M1)out，图注称比值，引用前须先锁定量。LL模型改善频率/M1而不同时解决全部E2；不能据一项M1淬火宣布模型已完整复现实验。

| 对象 | 被讨论的自由度 | 本轮可用出处与边界 |
|---|---|---|
| wobbling的集体取向 | 核密度/总角动量相对进动 | F24的模型/表征，实际识别仍看多观测向量 |
| scissors耦合 | 质子/中子轨道角动量的isovector相对振动，可重新分配低能M1强度 | F24-R105的QRPA解释，不是单一geff数值证明 |
| 磁转动shears | 高j价质子/中子叶片随spin闭合，alignment可重开 | [[agarwal-2007-137pr-magnetic-rotation-bandcrossing]] AG07-D22-R098-1的实验/模型分层，不能从wobbling中M1受抑直接归为shears |

105Pd的geff=.36是TI19明确的算符定标；不能因为数值能压低M1就称本核已独立探测scissors，亦不把IBFM缺项和QRPA的LL自动当同一实现。Ref67公开accepted稿已只读核，尚未正式raw/source摄入；F24转述的164Yb与原稿162Yb/系统学条件差异保持needs_review: true。

## Day22 checkpoint108：γ-soft不是模式禁止条件，PES不定标全部M1

[[frauendorf-2024-wobbling-review]] F24-D22-R108-1讨论同一TPSM输入同时出现core的softness交错特征与odd核的wobbling支持预测；这是作者模型解释，不能将fixedbasisγ独立当实验刚度，也不能从邻芯softness普适否定wobbling。其对IBFM能谱趋势的反驳与实际混合比冲突是不同层级，原privateenergy/producer未取得。

[[nomura-2022-questioning-wobbling-ibfm]] NOM22-D22-R108-1/2补充为什么整磁性向量重要：受限同质子/中子变形PES不能独立定Majorana强度，M1仍可受未确定项影响；该模型已有exchange term，不能称完全没有费米交换处理。127Xe的平均场v²=.4317使动力学/E2费米子prefactor较小、exchange权重接近最大，但这些不是实际B或普适M1零条件。额外磁性/混合对称响应能约束模型中静态PES不识别的方向；需实际数据/完整模型计算，不用固定γ宽度或M1百分比作跨核充要门。needs_review: true。

## Day22 checkpoint112：静态g的独立标量约束与几何边界

以下是本任务定义的单一量子j+core模型练习，不是F14或TI19的新g测量。取`I=R+j`、`μ/μN=gR R+gj j`、ħ=1并定义`gI=⟨μ·I⟩/[μN I(I+1)]`，则

`gI=gR+(gj−gR)⟨I·j⟩/[I(I+1)]`，

`⟨R²⟩=I(I+1)+j(j+1)−2I(I+1)(gI−gR)/(gj−gR)`，后式只在gj≠gR且单j/算符模型可信时可用。若gj=gR，gI恒为gR，不能反演核芯几何；接近该极限时问题病态。

独立CG²耦合基核I=j=11/2、R=0/2/4和chosen有理g，磁矩投影期望与该标量式精确相等。R分布`(1/2,1/2,0)`及`(17/20,0,3/20)`有同⟨R²⟩=3及同g=834/715，但分布不同；由均方矩构造的Reff≈1.3028不是确定R量子数。五项exact归一/CG/反演/奇异域/混合控制通过，所有g参数均为人工模型输入。

因此g可在限定模型下补充对粒子/核芯耦合的约束，却不重建三轴取向、进动锥或chirality。[[frauendorf-2014-transverse-wobbling]] F14-D22-R091-1的动态M1含gj−gR、[[timar-2019-transverse-wobbling-105pd]] TI19-D22-R103-3的geff按一条动态δ定标；不能自动把该动态淬火参数当已验证的静态g算符。实际多轨道、pairing/core polarization及g参数误差需另检，不把R≈I−j当量子几何。needs_review: true。

三组分的实验/模型对照见[[grodner-2018-128cs-chiral-g-factor]] GR18-D22-R114-1；该文orientation算符定义的开放问题不能用本文单j控制填补，也不改变其实际g结果。
