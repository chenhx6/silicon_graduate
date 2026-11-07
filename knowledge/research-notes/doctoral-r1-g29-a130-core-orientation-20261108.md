---
type: research-note
title: "A≈130：130Ba两准粒子候选与核芯形状—取向耦合"
aliases: [A130 core and orientation contract]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [chen-2019-transverse-wobbling-even-even, petrache-2019-diversity-shapes-rotations-130ba, doctoral-r1-g29-wang-2024-exploring-wobbling-even-even, doctoral-r1-g29-nomura-2022-questioning-wobbling-ibfm]
created_from: "G29研学；总控核原件后重建公式与跨模型解释"
promotion_target: ""
tags: [a130, ba130, wobbling, gamma-vibration, collective-core, doctoral-foundations]
---

# 不能把核芯形状和取向运动先验地分开

## Research Trigger

130Ba的S1/S1′是两准粒子偶偶核候选，适合检验从经典转子到准粒子极化、
再到软核芯形状与取向耦合的解释。这里的“偶偶”不意味着零准粒子，
也不能把其它奇A核的IBFM结果直接搬到它身上。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 四角角分布有大小δ两支，作者选小模较低χ²，但明说仅靠该数据不能完全排大模 | [[chen-2019-transverse-wobbling-even-even]]，PDF2 Table I及左栏；[[petrache-2019-diversity-shapes-rotations-130ba]] | 同一实验采集的理论再分析；总控核Chen PDF1–3 | 不是独立新实验；未据此取得绝对寿命/偏振 |
| I=13行δ=−0.58(13)，E2out/E2in=0.32⁺⁰·¹⁸₋₀·¹⁵，M1out/E2in=0.36⁺⁰·¹⁹₋₀·¹³μN²/(e²b²) | 同上Table I | 所选δ根下强度比 | 19/21行δ未印误差，不能补造 |
| π(h₁₁/₂)² CDFT极小(β=.24,γ=21.5°)，PRM惯量参数按两带能量拟合 | 同上PDF2 | 模型输入及校准 | 势面极小不是测得形状，固定形状PRM未给完整γ分布 |
| Ji=Θi(1+cI)，Θs/m/l=1.09/1.50/.65ℏ²MeV⁻¹、c=.59；惯量比.73/1/.43 | 同上PDF2右栏 | 显式拟合合同 | 同点能谱吻合不算独立留出 |
| 模型核芯可保形状涨落且出现作者解释的摆动图样 | [[doctoral-r1-g29-wang-2024-exploring-wobbling-even-even]]，PDF2–5 Eqs1–6、Figs4–6 | 5DCH算例112Ru等；总控读主文 | 不是130Ba破对计算，也非新实验确证 |
| 单奇费米子映射IBFM提供替代解释，PES不能固定部分磁相关项 | [[doctoral-r1-g29-nomura-2022-questioning-wobbling-ibfm]]，PDF3–4、9 | 另一个模型空间和部分拟合 | 不等于两费米子130Ba的定量否定 |

## Provisional Reasoning

### 1. 比值不是模式的独立开关

在Chen采用的混合比定义下，E2光子份额为\(\delta^2/(1+\delta^2)\)。
δ≈−.58给约25%，作者仍结合大E2out/E2in及PRM几何支持其TW解释。
这直接表明不能把“E2份额必须大于一半”写成无条件模式禁令。
反之，大δ也可由M1很小造成，Nomura Table II的127Xe例外给出实际提醒。
必须比较绝对EM、同态分支、核芯与准粒子算符及波函数，而不只比较比值。

Chen Table I的I=13模型M1out/E2in=1.11，相应所选实验为.36；
作者把M1偏大与未含剪刀模耦合作联系，这是作者借QRPA先例给的解释，
不是本文独立测得剪刀耦合或已经唯一归因。

### 2. 冻结粒子近似的局域稳定公式

以下为任务推导而非原实验反演。令I与冻结短轴对齐j无量纲，
\(a_k=\hbar^2/\mathcal J_k\)为能量，
\[
H=\tfrac12[a_s(I_s-j)^2+a_mI_m^2+a_lI_l^2].
\]
在\(I_s\simeq I-(I_m^2+I_l^2)/(2I)\)、小横向分量下，
\[
H_\perp=\tfrac12K_mI_m^2/I+\tfrac12K_lI_l^2/I,
\quad K_m=ja_s+I(a_m-a_s),\quad K_l=ja_s+I(a_l-a_s).
\]
采用相容的体坐标正则变量，领先阶
\[
\hbar\omega\simeq\sqrt{K_mK_l}.
\]
若\(\mathcal J_m>\mathcal J_s>\mathcal J_l\)，则K_m随I减，K_l随I增。
**不能仅因第一项减就证明频率在所有自旋单调下降**：
对常惯量，平方的导数为
\[
\frac{d(K_mK_l)}{dI}=ja_s(a_m+a_l-2a_s)
+2I(a_m-a_s)(a_l-a_s).
\]
其符号取决于输入与I。两个因子为正时才是这个定态的局域稳定振动。
常j/常惯量近似下，K_m为零给
\(I_c=j\mathcal J_m/(\mathcal J_m-\mathcal J_s)\)。
这是近似模型的边界，不是从实验直接测出的崩溃自旋。
惯量随I、准粒子重取向、配对和带交叉改变后，必须重新检查。
不据此给所有两准粒子核14–36ℏ或其它固定窗口，也不称“拓扑保护”。

### 3. 核芯形状不是一个不受扰动的背景参数

Chen将CDFT形状极小、PRM拟合惯量及准粒子波函数一起使用，
有实际核芯极化与有效惯量的输入依赖。作者也讨论形状在平均值附近有涨落。
Wang2024进一步在同一5DCH波函数中保留β、γ和Euler角，
而不是先把γ振动或摆动定义成永不耦合的两个对象。
原文还将惯量增强到匹配2₁能量，不能宣称全部为无调参预测。

Wang的取向SCS先对形状自由度求迹：
\[
\rho^{(I\alpha)}_{K'K}=\int d\mu(\beta,\gamma)
\,\psi^*_{\alpha K'}\psi_{\alpha K},
\]
再由ρ生成取向概率。此为模型边缘分布，舍去了形状—取向的部分关联。
**任务推断：** 只给取向边缘分布不能唯一决定联合波函数。
例如\(|\Psi\rangle=\sum_a\sqrt{p_a}|s_a\rangle|u_a\rangle\)的正交形状基求迹给
\(\rho_{\rm rot}=\sum_ap_a|u_a\rangle\langle u_a|\)；
不同形状基或联合关联可能产生相同ρ_rot。
这不推翻作者对其波函数的解释，而是限制由一幅SCS图外推唯一物理机制。

### 4. 静态PES映射还遗漏什么

Nomura采用IBM-2，并为简化设质中形变相等。其PDF3明确某些Majorana项在此PES上无独立贡献，
参数不能仅靠PES映射固定；这些项又可能影响M1。
因此“模型再现核芯势面”不等于“已唯一确定其磁响应”。
这与Chen讨论剪刀模影响M1形成可研究的接口，但两个模型的算符/空间尚未匹配，
不能把它们当同一机制的独立重复证明。

## Assumptions

- 冻结j、常惯量与小振幅的公式只解释一个局域极限；真实PRM可解冻/量子化全部角动量。
- 实验δ按原分支与取向输入理解，强度比不是已获得的绝对B。
- γ带、K=2分量和取向激发的关系取决于Hamiltonian；三轴态不默认有精确好K。
- SCS及形状PES都是指定模型中的诊断，不是直接实验快照。

## Competing Explanations

不同准粒子组态、核芯形状激发及其与取向的耦合都可能生成相近带结构。
Nomura的单费米子结果不能裁决130Ba；一个γ均值或E2主导也不能裁决全部模型。
实验混合比分支、磁算符和未观测feeding还可能改变解释排序。

## Transfer Conditions

从163Lu到130Ba要匹配破对数、高j占据、惯量、形状涨落和自旋尺度；
从零准粒子112Ru的5DCH到破对Ba需显式加入相应自由度。
迁移的是检验合同，不是只把粒子j加倍就保证模式更稳。

## Failure Conditions

忽略δ另一根、把比值当绝对EM、用q₃平均测γ宽、
从单个PES极小确定取向、将一个稳定因子单调性当整个频率单调性，
或让未拟合磁项默认为零，都会使判别失效。

## Falsification or Reverse Tests

对同一组态联合拟合已有输入，再预测未使用的两方向/多末态分支及绝对寿命。
保留实验δ两根和响应；重复同采集论文不增加独立性。
对冻结模型检查上面的频率导数和K_m/K_l稳定条件；
完整模型则跟踪波函数与形状—取向关联，不能仅对比一条能差曲线。

## Open Questions

- **idea：** 条件取向分布P(θ,φ\|β,γ)是否比边缘SCS更能区分近刚性取向振荡与形状—取向耦合？
  assumption是可访问同模型联合波函数；竞争解释为同一物理的不同表示。
  先前向预测未拟合EM，若条件分析不改变任何可测预言，只保留为解释工具。
- **idea：** 在匹配PES和谱后，未被静态映射固定的质中磁关联项能否改变候选带的M1而保留E2？
  先限定算符/空间，竞争解释为有效g、配对与组态混合；
  需联合剪刀强度、磁矩和多分支EM，若预测不可区分则不能归因某一耦合。
- 已读上述原件，不声称全球新颖性；尚无共同计算输入或作者波函数可重放。

## Human Review

- Review scope: G29研读与总控逐表/公式核查，未发生用户逐项审阅。
- Decision: provisional；不以作者或模型数量投票。
- Complete unresolved P0/P1 inventory: 版本/原件身份已核；P1为绝对EM、完整Cov、
  形状—取向联合波函数及共同磁响应模型未取得。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 总控重建 | worker draft | provisional | 核Chen Table I、Wang主文与Nomura Table II，撤回普适δ门/固定窗口/γ均值刚性和频率单调证明 | doctoral-nuclear-structure-foundations |
