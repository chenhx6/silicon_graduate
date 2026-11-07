---
type: research-note
title: "A≈80：Kr的符号网络、形状混合与核芯迁移边界"
aliases: [A80 Kr signed quadrupole network]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [doctoral-r1-g27-clement-2007-prc-krypton-coulex, liu-2008-shape-coexistence-188pt, liu-chen-2016-78br-chirality-reflection-symmetry-thesis]
created_from: "G27研读；总控视觉核表后缩减重建"
promotion_target: ""
tags: [kr, shape-coexistence, coulomb-excitation, phase, e2, doctoral-foundations]
---

# 从强度到带符号网络：Kr为何提供更多信息

## Research Trigger

一条B(E2)只给一个矩阵元模方，不能看到不同激发路径的全部干涉。
Kr多步CoulEx可帮助理解怎样从实验室可测量量进入形状混合语言，
也能检验何时不能把偶偶核基态核芯照搬到邻近奇奇核。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 74Kr2₁→0₁的RME=.782(7)eb、2₁对角−.70⁺·³³₋·₃₀eb | [[doctoral-r1-g27-clement-2007-prc-krypton-coulex]]，PDF15 TablesX–XI | 总控视觉核表；同一CoulEx分析 | 非对角符号依规范，内禀形状依模型 |
| 74Kr0₂→2₁的RME=.68⁺·⁰⁴₋·₀₃eb，B=.47(5)e²b² | 同上TableX | 原表的方向与误差 | 反向B不是.47，而是约.094 |
| 76Kr0₂→2₁字面RME−.490⁺·⁰¹⁶₋·₀₀₈eb，2₁对角−.9(3)eb | 同文PDF11 TablesV–VI | 总控视觉核表 | −.78为理论Qs，不能错置成实验RME |
| K=0/K=2解释在某些激发态不唯一 | 同文PDF15表注与下文 | 作者解释边界 | 不把每个激发态都归纯轴向混合带 |

刘渊2008硕士论文的188Pt研究沿用[[liu-2008-shape-coexistence-188pt]]；
它与Kr不是同一数据，本页没有重新将其全部数值作为Kr证据。
78Br学位/期刊的真实范围见对应source，不由此推定当前所有观测已补齐。

## Provisional Reasoning

### 1. 跃迁方向是第一项检查

采用\(B(E2;i\to f)=|\langle f\|T\|i\rangle|^2/(2I_i+1)\)，
同一对0⁺/2⁺态的正反B相差5，RME模相同。
74Kr表中的.47是0₂→2₁；若需要反向强度，应按统计因子换算，不能把箭头换掉仍保同数字。
不同I的RME直接相除也不等于B比。

### 2. 哪些符号可测

态重相位\(|i\rangle\to e^{i\phi_i}|i\rangle\)使
\(M_{fi}\to e^{i(\phi_i-\phi_f)}M_{fi}\)，
封闭环\(M_{ab}M_{bc}M_{ca}\)不变。
多步CoulEx通过相干路径以及重取向干涉，对这些规范不变量和对角项提供约束。
所以“矩阵元正负”必须伴随整个网络的相位约定，
不能只为迎合内禀长/扁图像而翻一条跃迁的符号。

### 3. 矩阵元与形状混合不是同一个观测层

负2₁对角项和相应负Qs，在轴向K=0近似支持长椭倾向；
0⁺的静态Qs仍恒零。原文还指出K=0、K=2和长/扁构型可混合，
不能把一个符号升级为整个核纯内禀形状已确定。

一般两构型模型可把过渡矩阵写成
\(M=R_2\,\mathrm{diag}(m_a,m_b)\,R_0^T\)，
其中R₀/R₂分别是两个自旋空间的混合变换。
这个式子另外假设未混合构型间交叉E2可忽略。
只给各项模方会丢相位信息；对角矩阵元又提供不同约束。
本页撤回未经完整Cov与相位审计的±1.08eb双支“唯一证明”，
不把一次条件中心值重建当全实验网络的精确反演。

### 4. 不变量约束什么

0⁺态q₂的完整和为全部2⁺连接模方和，正项部分和是该算符的下界；
不是所有模型下“真实几何β”的无条件下界。
q₃需要带符号路径，高阶矩更需闭合/误差。
Q⁴−⟨Q²⟩²关联幅度分布，不直接测γ宽，也不独立给势曲率。
强E0与强带间E2可约束构型混合，却不能凭一个任意普适数字排除所有连续软势模型。

## Assumptions

- RME相位、方向和统计因子全页一致；0⁺/2⁺的几何转换另列K假设。
- 两构型截断与交叉E2忽略为模型条件，不由数据自动成立。
- 已有寿命/分支输入与CoulEx解相关；不将它们重新计成独立证据。
- Kr与78Br或188Pt的关系是机制/方法比较，不是同一核芯同一态的复测。

## Competing Explanations

离散构型混合、连续β–γ波动及多构型投影模型可产生部分相近观测。
K混合、有效电荷与网络截断又影响几何解释。
需要同一输入下的未拟合矩阵元和谱比较，不能靠E0大或某一能比单点命名。

## Transfer Conditions

从偶偶Kr向78Br高自旋迁移需释放奇质中占据、配对阻塞和形状极化；
它们的方向/大小须计算，不存在由Pauli自动给25–40%或γ=−30°的结论。
从Kr到Hg/Pt比较，则可追踪闭壳、入侵组态和带符号网络如何变化，
不按质量数先验设双阱或软势。

## Failure Conditions

混淆exp./theory列、RME/B方向、态规范或K假设；
将正项部分和叫完整形变；丢共同Cov；
或把一个两态模型失败当所有形状共存解释失败，均应停止相应推断。

## Falsification or Reverse Tests

优先预测没有用于拟合的对角RME、其它0⁺连接、绝对带间E2和E0。
检查所有规范环与Hermitian正反关系；增补路径后追踪不变量区间收敛。
若候选模型的联合预测仍重叠，明确现有数据不可识别，而非强行选机制。

## Open Questions

- **idea：** Kr与Hg/Pt两构型混合的相同方法能否由共同未拟合EM检验？
  assumption是状态映射/算符和相位已对齐；竞争解释为多构型连续动力学。
  先比较真实网络，不预设相同混合概率或固定内禀Q；无区分力则转向其它态。
- **idea：** 奇核子极化可在何种局域条件下改变偶核芯的形状—取向关联？
  prediction由同一微观计算前向给出，不先命名“冻结”；
  竞争解释为原软分布上的动态取向、其它组态和有效算符。
  未拟合绝对EM无法区分时，保持问题开放。
- 搜索与原读集中于上述来源，不宣称全球新颖，也不以文献未查到作为反证。

## Human Review

- Review scope: G27研读、总控视觉核表及代数核查；无用户逐项审阅。
- Decision: provisional，撤回强定论，按具体直接证据使用。
- Complete unresolved P0/P1 inventory: 实测/理论列错置已纠正；P1为全Cov、
  符号分支和多构型/高阶闭合未复算，不自动成为用户待办。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 核原表后缩减重建 | worker draft | provisional | 更正76Kr对角列/符号、74Kr方向，撤回普适E0/γ阈值与未经审计的唯一双支反演 | doctoral-nuclear-structure-foundations |
