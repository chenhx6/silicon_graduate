---
type: research-note
title: "GR97：Stokes输运、响应对象与merit比较"
aliases: [GR97 response and merit audit, Compton Stokes transport contract]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
question: "如何把正确的光子偏振输运、校准Q和几何比较放在同一可复核合同中？"
evidence_sources: [garciaraffi-1997-monte-carlo-compton-polarimeters, palit-2000-rh99-clover-polarimetry]
created_from: daily-learning-uncredited-Day17-preview
promotion_target:
reproducibility_entry: system/scripts/day16_garciaraffi1997_stokes_audit.py
tags: [Compton, Stokes, detector-response, calibration, figure-of-merit]
---

# 正确传递偏振后，仍需匹配实际response

## Research Trigger

[[garciaraffi-1997-monte-carlo-compton-polarimeters]]比较历史五coax、四coax与EUROGAM CLOVER的偏振响应。它为[[palit-2000-rh99-clover-polarimetry]] P00-10涉及的固定角比值/有限几何区别提供直接方法参照。本note属于Day16窗口内恰好Day17的无学分预习；不启动正式Day17或新的实验拟合。

## Grounded Evidence

原7页461–467、Eq1–16、3图/Table I及29项参考主线均重新读取。Table I是同一modified GEANT3程序的计算，不是九次实验。原GR97-2/4的review字段保持；本日新分析不归入旧审核。

正文把三种校准主线对应von der Werth[22]、Bass[23]、Jones[25]，图注却分别写[24]、[25]、[27]。本note保留两套数字，按正文叙述识别所述装置，不暗改图注或声称已核每篇primary的完整数据。作者比较的是上游已发表校准，本文没有重新采集三组核结构数据。

## Assumptions

点核采用自由、静止、未极化电子的线性Stokes模型，省略共同的经典电子半径平方。使用`(I,Q_s,U_s)=(P0,P1,P2)`，Q_s是相对散射平面的平行减垂直分量；它不是仪器灵敏度Q。这里只处理线偏振，不扩展到圆偏振、材料输运或真实阵列响应。

原Eq9的总偏振度是非负幅度；核谱学相对reactionplane的signedP由带方向的Stokes分量与参考轴定义。不能用sqrt(Q_s²+U_s²)/I丢掉方向后再判E/M或δ号；M=εQ²也不能校验探测器符号。

Table I算术直接使用原印刷中央值与误差。将quoted误差用于局部传播时，Cov未知；不补成独立误差或一个总预算。时间比较另要求固定入射通量、对称探测、理想独立计数、无背景且Q已知。

## Provisional Reasoning

### Stokes正性、坐标与出射混合

令`r=E′/E=[1+(E/m_ec²)(1−cosθ)]⁻¹`、S=r+1/r、c=cosθ。原Eq11的无量纲矩阵部分为

\[
F=\begin{pmatrix}
S-\sin^2\theta&-\sin^2\theta&0\\
-\sin^2\theta&1+c^2&0\\
0&0&2c
\end{pmatrix},\qquad T=\frac{r^2}{2}F.
\]

Eq12把输入参考轴转到散射平面，线性分量按2φ旋转。`T M(φ)`与Eq13的三个分量及前因子相合，Eq14的偏振度与Eq15的两正交纯态混合也相合。

程序用`J=diag(c,1)`验证：F等于Thomson的Jones密度映射`ρ→2JρJ†`，加上强度为`(S−2)I`的无偏振项。因S≥2，它对整个物理线性Stokes圆盘保持正性，不只对几个试点成立。

对完全线偏振输入，出射偏振的本征方向是入射E方向投影到垂直于出射k的平面；Eq15按相应权重抽样两正交纯态，可在ensemble层面表示部分偏振。θ90°且入射偏振在散射平面内时，投影可为零：有限能量输出无偏振，不能强行归一一个零方向；Thomson零强度节点的偏振度则未定义。

无偏振入射光也可在**选定散射方向后**产生线偏振。以原Table能量作两次90°的点核控制，保留第一次散射偏振时，第二次正交平面的条件不对称为约.579118、.237759、.088885；把第一次输出重置无偏振则全为0。这不是GR97紧凑装置“Q低估40%”的重放，也不是新Q测量。

原程序假设bremsstrahlung/annihilation所生secondary photons无偏振，并调用原GCOMP；primary的Compton链才使用GCOMPOL/POLAR。不能把它称为所有光子通道均完整偏振追踪，也不能据点核控制推断这一近似实际造成多少误差。

### 本次误读的纠正与失败控制

本run最初将Eq13分子上的撇号漏读，误提出其前因子为`(E/E′)²`的假设。放大原p466确认它与Eq11一样是`(E′/E)²`；初合同、首次脚本和纠正记录均保留，最终v2据原件计算，不把误读写成source erratum。

P00 p349 Eq5确实另印`(E/E′)²`（P00-10），其文字定义E为入射、E′为散射。作为有明确归属的反事实控制，在GR97点核上故意倒置前因子：固定θ的归一Stokes和PSD仍通过，但强度被乘r^-4。Table三能量、θ90°时因子约15.32、239.87、6073.11。因此“归一偏振正确/密度正定”不能独立验证有限角权重。P00实际producer未知，不能从印刷式宣布其数据或GR97程序错误。

### 九项印刷Q/M与推回的效率

原Table I共同条件为距源25cm、每晶体阈值50keV、对称polarimeter；ε是`ε∥+ε⊥`的absolute coincidence efficiency。下表ε由`M/Q²`重算，仍是同一组数据的派生量。

| E/MeV | 配置 | Q | M | 推回ε |
| --- | --- | --- | --- | --- |
|.5 |5coax |.516±.005 |(7.4±.2)×10^-6 |2.77928×10^-5 |
|.5 |4coax |.286±.005 |(2.3±.1)×10^-5 |2.81187×10^-4 |
|.5 |CLOVER |.209±.005 |(3.1±.1)×10^-5 |7.09691×10^-4 |
|1.5 |5coax |.263±.008 |(1.0±.1)×10^-6 |1.44573×10^-5 |
|1.5 |4coax |.155±.007 |(3.9±.4)×10^-6 |1.62331×10^-4 |
|1.5 |CLOVER |.101±.006 |(5.1±.6)×10^-6 |4.99951×10^-4 |
|4 |5coax |.088±.006 |(4.9±.7)×10^-8 |6.32748×10^-6 |
|4 |4coax |.068±.005 |(3.4±.5)×10^-7 |7.35294×10^-5 |
|4 |CLOVER |.040±.004 |(4.2±.8)×10^-7 |2.62500×10^-4 |

这些absolute ε比不能与正文按active solid angle归一后的“50%更高/4倍”直接相除比较，二者分母不同。也不能把Q/M/ε计成三组独立模拟证据。

若把quoted数作为边际标准差，局部误差项为`a=σM/Q²`、`b=2MσQ/Q³`，未知Cov下`abs(a−b)≤σε≤a+b`。M本身含Q²，同一MC的共同误差不可忽略。某行形式下界为0不表示实际效率误差为0。

### Merit与测量时间的适用条件

理想计数下`Var(A)≈(1−A²)/N`，A=PQ，故固定σP时

`t=(1−P²Q²)/(flux × εQ² × σP²)`。

因此M=εQ²是在上述条件下比较偏振精度的指标，不是任意背景、任意校准误差下的硬件排名。用原中央数，紧凑配置对5coax的merit比为4coax约3.11/3.90/6.94、CLOVER约4.19/5.10/8.57；原文“3–8倍”是近似说明，当前未做带共同误差的差异检验。

保留有限P修正，在整个0≤abs(P)≤1内，上述理想条件的`time5/time4`分别落在[2.48,3.11]、[3.72,3.90]、[6.92,6.94]；`time5/timeClover`在[3.21,4.19]、[4.80,5.10]、[8.52,8.57]。这只重算印刷配置下的中央设计比较，没有给实际曝光时间或推荐用户阵列。

### 校准曲线与Table I不是同一response对象

五coax验证用每晶体60keV、重构θ在70°–110°，fit在.3–1.8MeV为`Q=Q0(a+bE)`，a=.79(.17)、b=.0780(.0011)MeV^-1；Cov(a,b)未给。四coax验证阈值150keV，CLOVER为60keV，均与Table I共同50keV条件不同。

原式给.5/1.5MeV的五coax fit约.558657/.284368，Table I则.516/.263；这不是同response的闭合检验，不能用自由Cov强迫相等。Table I未再次明确角窗，不能自行补成70°–110°。4MeV也不在该校准fit域内。

## Competing Explanations

灵敏度变化可以来自多次散射中的偏振输运、阈值、有限角接受、尺寸、事件排序和不同channel选择。单独归一P正确不能区分这些原因。原MC与历史校准的相容是方法验证，不是独立核赋值或每个能量点的完整10%误差预算。

## Falsification or Reverse Tests

原four-crystal first-scatter-only控制使Q约低40%，而fulltransport较接近历史数据；这是源程序的控制，不由本run点核数代替。原文仍承认1.4/2.1MeV两点在quoted实验带外，并用“by only30%”描述；未给清晰统一的σ口径，本run不据图新算z值。

几何小变化也并非永远只有几percent：原five-coax散射晶体长度+5mm时Q降7%，four-coax长度+5mm降9%。未知实际几何/门/响应时，不能把这些局部结果换成新装置的统一systematic。

## Agent Self-audit Triage

P0：未识别未隔离的来源身份、路径或权限问题。错误的Eq13假设已按高分辨原件纠正，不作为source事实传播。

P1：新表算术、Mueller正性、点散射和理想时间范围均为条件核验；原GCOMPOL/材料response、校准ledger、每通道Cov和完整GEANT3运行未恢复。不新增实验Q、δ、宇称或正式Day17学分。

## Reproducibility

[程序](../../system/scripts/day16_garciaraffi1997_stokes_audit.py)最终actualexit0；首次SymPy结构等式断言失败留档，改为展开后的代数相等检验，未改源Table I、阈值或几何。v1误读假设与v2纠正均有hash/时序；原source前缀及GR97-2/4 review值保持。

## Transfer Conditions

只迁移符号/参考轴、自由电子Stokes核及匹配条件下的比较程序。换探测阵列、阈值、角窗、能量区间、background或光子类别，须重新生成实际response和统计合同。

## Failure Conditions

零强度节点、零投影偏振轴、遗漏2φ旋转、重置Compton后偏振、能量前因子倒置、absolute/active-solid-angle分母混用或不同threshold样本混比，都能使迁移失败。不能通过clip、调Q或挪用source“10%”修补。

## Open Questions

原1997修改的GCOMPOL/POLAR/GDROT3版本、完整几何及threshold/anglewindow配置是否可合法取得？三历史校准的未舍入counts与共同Cov在哪里？图注与正文引用号为何不一致？

## Human Review

本note尚无人类审核；新推导与claims保持unreviewed/needs_review，不把旧source局部审阅移作本日审核。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
| --- | --- | --- | --- | --- | --- |
|2026-10-19 |created |none |provisional |原七页、表算术及Stokes核验；实际producer/response仍缺 |不晋升实验结论 |
