---
type: research-note
title: "A≈190：Hg平缓E2表象、形状混合与有限矩阵元网络"
aliases: [A190 Hg charge-shape mixing]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [doctoral-r1-g31-bree-2014-prl112-coulex-182-188hg, dracoulis-2013-192os-isomers-gamma-soft, continuation-g18-lukasiak-1979-191ir-triaxial-rotor]
created_from: "G31研学；总控视觉核Table I及混合段后重建"
promotion_target: ""
tags: [hg, a190, shape-coexistence, coulomb-excitation, quadrupole-invariants, doctoral-foundations]
---

# 相近的2₁→0₁强度，为什么不保证相近的波函数

## Research Trigger

182–188Hg的低能能量和一条E2相近，但其它连接、符号和混合解释可以明显变化。
这提供了A≈190附近形状共存的实质案例，也提醒不能把Hg低自旋几何照搬成Ir/Os高自旋核芯。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| ⟨0₁‖E2‖2₁⟩依次182/184/186/188Hg为1.29⁺·⁰⁴₋·₀₃、1.27(3)、1.25⁺·¹⁰₋·₀₇、1.31(10)eb | [[doctoral-r1-g31-bree-2014-prl112-coulex-182-188hg]]，PDF4/printed162701-3 Table I | 总控视觉核表；同CoulEx+采用输入 | 184/186列不可互换；一行平缓不等于全网络平缓 |
| ⟨2₁‖E2‖4₁⟩依次3.71(6)、3.15(6)、3.4(2)、2.07(8)eb | 同上Table I | 同一分析 | RME比不是B比；4⁺仍为本低能案例，不等于TSD高自旋 |
| 2₁对角：182Hg−.04⁺¹·³⁰₋₁·₄₀，184Hg1.5⁺¹·⁸₋₁·₂，186Hg空缺，188Hg1.0⁺·⁶₋·₄eb | 同上Table I | 误差与空项保留 | 不能把188的值放到186，更不能把中心值当精确形状 |
| 182Hg跨态RME：⟨0₁‖E2‖2₂⟩−.61(3)、⟨0₂‖E2‖2₁⟩−2.68⁺·¹⁵₋·₁₃、⟨2₁‖E2‖2₂⟩−2.2(4)eb | 同上Table I | 所选规范相位下的网络 | 单条非对角符号不是独立物理量 |
| 1.2/3.3eb过渡及1.8/−4.0eb对角未混合矩阵元为全链共同拟合；混合概率来自引用的VMI分析 | 同文PDF5/printed162701-4 | 条件两结构模型 | 不是新测的奇核Q₀；184Hg部分符号未再现 |

实际底本6物理页含机构封页，PRL正文5页；总控回PDF2–5及视觉Table I。
原文PDF4明确186Hg基态、186/188激发0⁺形状性质受关键矩阵元精度限制。
188Hg Fig3实验和只含2₁连接；不能称网络完整。

## Provisional Reasoning

### 1. 旋转参考值先统一方向与统计权

在同一个固定Q₀、轴向K=0理想转子中，
\[
B(E2;4\to2)/B(E2;2\to0)=10/7,
\qquad |M_{24}|/|M_{02}|=\sqrt{18/7}\simeq1.604.
\]
后式还含初态统计权9/5；不能把RME比写成√(10/7)。
182Hg中心RME比3.71/1.29≈2.88，偏离该简单单带参考。
它要求更完整的态混合/结构解释，而不是单凭比值就唯一证明某个势阱。

### 2. 相位与重取向提供什么

单态重相位改变相连非对角RME符号，闭合环乘积不变。
对角RME也不随该规范改变。CoulEx用轨道振幅与多步干涉约束这些量。
182Hg的两个负非对角项可以构成正的环乘积；
不能仅因单条RME为负就叫相消，截面干涉还含轨道积分和角动量几何系数。

在本页约化矩阵元约定下，2⁺谱学矩
\[
Q_s(2)=\sqrt{16\pi/5}\,\sqrt{2/35}\,
\langle2\|T(E2)\|2\rangle\simeq.758\,M_{22}.
\]
K=0轴向转子另有Qs(2)=−2Q₀/7。
由此可在该近似讨论正对角项的oblate倾向，不能直接说测得0⁺的固定内禀形状。
0⁺的实验室一阶Qs恒零。

### 3. 有限矩与形状语言

沿[[doctoral-r1-t03-shape-invariants-and-softness-20261108]]的约定，
\(q_2=\sqrt5\langle[T\times T]^{(0)}\rangle\)，
\(q_3=-\sqrt{35/2}\langle\{[T\times T]^{(2)}\times T\}^{(0)}\rangle\)。
对可交换坐标张量，它们是⟨Q²⟩与⟨Q³cos3δ⟩。
q₃/q₂³ᐟ²是有效矩比，一般不等于无权⟨cos3δ⟩。
原文Fig3的有效不对称量、β映射与模型假设应按实际定义保留，
不能由均值给γ宽或刚性，更不能由幅度方差直接给势曲率。

原文认为较弱变形的基态和较强激发构型与数据相容，同时强调部分核精度不足。
它没有测全真实形状分布或否定所有连续大振幅模型。

### 4. 两结构如何产生平缓表象

作者设未混合两结构之间的E2连接可忽略，
物理0⁺和2⁺各有不同混合系数。
主连接可写成\(M_{02}=\alpha_0\alpha_2m_I+\beta_0\beta_2m_{II}\)，
因此某一混合系数变化可以被另一项补偿，保持一条RME近似不变。
这不一定是两项相消，更不保证所有矩阵元都恒定。

1.2/3.3等是作者拟合值；VMI混合概率又来自引用的能级模型，
不是四项独立无模型测量。184Hg中若干符号偏差在作者测试的混合变化范围内仍存在，
说明该具体截断有改进空间，不能据此否定整个形状共存或BMF模型类。

## Assumptions

- CoulEx分析要求实际散射角/最小距离和核力影响可控；仅称低于势垒不保证纯电磁为精确事实。
- 采用寿命、BR、转换系数与拟合矩阵元相关，原文不加寿命的重拟合相容性是检查而非另一次新采集。
- 低能网络截断对高阶矩可能重要，不预先把遗漏量称微小。
- 两构型间忽略的是E2算符连接，不是禁止Hamiltonian造成混合。

## Competing Explanations

连续β–γ集体分布、多构型投影与不同有效算符可解释部分相近观测。
原文比较的BMF与IBM对SSM/STM仅部分相符，不能以其一条成功曲线消除全部偏差。
单条矩阵元相同也可能因不同结构贡献抵消，尚不能唯一选某个解释。

## Transfer Conditions

Hg与Ir/Os质中数、费米面、组态和自旋不同，只作方法互补。
高自旋K阻碍、形状极化与低自旋电荷矩各需逐态来源；
K混合可以来自多种机制，低fν不独立指定三轴。
奇核RME还需正确耦合，不能把偶偶未混合过渡矩阵元直接叫其Q₀。

## Failure Conditions

错列、漏宽误差、以一个符号确定全波函数、把矩比当无权角宽，
或把低能部分和当全闭合都会破坏相应推断。
第三构型只有在其影响无法被受控两态近似吸收时才要求扩展，不能因存在第三态就一概禁止近似。

## Falsification or Reverse Tests

用同一网络/响应比较未拟合RME、其它0⁺连接及E0。
换靶的前向预测要包含能量、轨道和角覆盖，不只是按Z作线性比例。
E0模型所需的是未混合构型半径差，不能未经映射把不同同位素的同位素位移直接代入。
若一种截断不能同时解释模方和相位不变环，扩展构型/算符并继续检验。

## Open Questions

- **idea：** 同一组输入中，离散混合与连续形状分布能否对新增带符号连接给不同预测？
  assumption为共同状态映射与算符；竞争解释为有效算符/截断。
  若预测重叠，保持不可识别，不由是否出现两条带单独决定。
- **idea：** 准粒子极化对哪些电荷矩及取向响应影响最大？
  需指定同核不同组态，不能拿Hg作为所有Ir/Os的直接参照。
  一个Qs或Qt相同仅约束该量的变化，不能排除补偿的β/γ或算符贡献。
- 未穷尽后续Hg实验或模型；不把2014边界自动叫2026仍未知。

## Human Review

- Review scope: G31研读和总控原件/代数重建；未发生用户逐项审核。
- Decision: provisional，实验、拟合与推断分层。
- Complete unresolved P0/P1 inventory: 列/页码及统计权错误已改；P1为完整Cov、
  高阶闭合和共同模型留出预测，均属研究边界。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 总控核图/式后缩减 | worker draft | provisional | 修184/186/188列、Qs/不变量因子与K/闭合条件，保留真实网络及模型偏差 | doctoral-nuclear-structure-foundations |
