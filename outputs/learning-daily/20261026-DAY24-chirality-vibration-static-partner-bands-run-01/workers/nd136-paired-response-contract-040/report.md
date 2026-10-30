# 040：实际四条 E2 的连续响应与联合 Cov 合同

**窄增量成立。** 028/033及canonical已覆盖实际四线、条件比与“τ/共同reference消去但gate/Cov缺”；`ado-covariance-calibration`已覆盖一般共同效率mode与背景Cov。本单元只补这四条真实能量的联合log-response Jacobian及共同幂律tilt残留，未建立另一套toy或新实验结论。

## 输入与证据层级

沿用028/033已核的Lv2019 thesis Table5.1，physicalPDF94–95、footnote b PDF97及Fig5.6 PDF77；canonical为`knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md`的TH19-D25P-001/005/006。原件SHA256为`84e8b934fda9a97ea79527a8b1456f40e534bc67be847d61b1a1219002d85749`。本单元没有新增全文阅读或网络检索；原始输入属于同campaign，以下响应代数是任务推导。

| 顺序/身份 | 同母态 | Eγ keV | 原相对 Iγ | 终态 |
|---|---|---:|---|---|
|o20|D5-C20+/7543.0|1021.2|.6(1)|D5 18+/6521.8|
|i20|同上|611.4|.21(10)|D5-C18+；6931.6为条件能差|
|o21|D5-C21+/7927.1|1060.7|.8(4)|D5 19+/6866.4|
|i21|同上|714.1|.18(4)|D5-C19+/7213.0|

四行均按源E2赋值。条件名义值仍是R20=.2197885667、R21=.6146810196、D=R21/R20=2.7966924248；不再计为新发现，不使用括号误差制造CI。

## 共同量怎样消去

在同母态、同E2、可比较的光子产额定义下，理想逐线产额可写

\[
q_l=N_j\tau_j C_{E2}E_l^5 B_l.
\]

这里N_j是该母态布居，τ_j是同一母态总mean lifetime；光子partial rate为C E⁵B。两线之比同时消去N_j、τ_j与C。**不要求τ20=τ21，也不要求测得任何一个τ或完整totalBR。** 若不同门选择了不同feeding/postselection，相关差异必须留在逐线response，不能借共同parent直接消掉。

令f_l=ε_true(E_l)/ε_used(E_l)，g_l为使用已有校正后残余的逐线selection/acceptance，b_l为有符号的**加性**净峰/背景残差（换算到相同效率修正numerator单位）。一个明确的响应写法为

\[
\widehat I_l={100\over\widehat Q_{373.7}}
    [q_l f_l g_l+b_l].
\]

同一个随机normalizer在每个Iout/Iin里**逐实现精确消去**，它可以与分子相关；不需假定独立。反之，若不同谱用各自normalizer估计再组合，必须交付真实变换，不能仅凭“都归一373.7”宣布精确共享。normalizer的背景/污染如果还通过其它分析路径进入逐线提取，也不能全部归到已消去的一项。

b=0时，Rhat_j/Rtrue_j=(f_o/f_i)(g_o/g_i)。一个共同全局效率scale f_l=c严格消去；同parent两线确实共有的selection multiplier也可消去。**能量相关效率一般不消，g_o≠g_i时门差不消，逐线加性背景一般不消。** 即便两个b相等，其分数偏差b/q通常也不同。

## 连续联合敏感度

令η_l=b_l/(q_l f_l g_l)，净numerator为正时定义ρ_l=ln f_l+ln g_l+ln(1+η_l)。于是

\[
\begin{pmatrix}
\ln(\widehat R_{20}/R_{20})\\
\ln(\widehat R_{21}/R_{21})\\
\ln(\widehat D/D)
\end{pmatrix}
=
\underbrace{\begin{pmatrix}1&-1&0&0\\0&0&1&-1\\-1&1&1&-1\end{pmatrix}}_{J}
\begin{pmatrix}\rho_{o20}\\\rho_{i20}\\\rho_{o21}\\\rho_{i21}\end{pmatrix}.
\]

这是log残差定义下的精确关系；小背景时ln(1+η)≈η仅是一阶近似。J消去全局mode(1,1,1,1)，也消去真正共同的parent内mode(1,1,0,0)、(0,0,1,1)。第三行是第二行减第一行，故R20、R21、D不是三项独立约束。

若未来有实际Σρ，则Σy=JΣρJᵀ；特别Var(lnD)=Var(lnR21)+Var(lnR20)−2Cov(lnR21,lnR20)。同campaign及两个不同parent均不允许默认该cross-Cov为零。统计净峰误差与校准/背景若有关，须在primitive joint模型中一次传播，不能把同一误差重复计入。

### 一个声明过的效率子模型

只在**共同单斜率**f(E)=(E/E*)^s、其它response不动的子模型中，

\[
\partial_s\ln(\widehat R_{20}/R_{20})=\ln(1021.2/611.4)=0.5129822759,
\]
\[
\partial_s\ln(\widehat R_{21}/R_{21})=\ln(1060.7/714.1)=0.3956613380,
\]
\[
\partial_s\ln(\widehat D/D)=-0.1173209380.
\]

共同E*消去；上述log关系在该幂律族内对任意s成立。这说明两个能量比接近，使双比对这个**单一平滑mode**较不敏感；不是四能量下的一般效率函数抵消。任意效率曲率、不同run/detector weighting、line gate和弱峰背景都可沿J保留下来。即使某假定目标要求很大的s，也只能约束该幂律族，**不能据此排除一般系统误差**。本轮不估计或拟合s，不假设任何nuisance大小。

## 未来联合再分析最小交付

1. 固定四条线与母/末态身份、E2赋值和能量校准；给实际Eγ误差及相关性，不能把EFFIT误差当作E⁵运动学误差。
2. 每线实际projection/gates、门角色/窗宽/权重、event reuse、曝光/active detector mask、addback/cuts、条件角接受；“total projection+gated spectra”或Fig5.11门名本身不足以重建四线producer。
3. gross/net峰面积、ROI/峰形、背景/污染模型、sideband/transport或共同拟合参数，以及跨四线Cov或完整joint likelihood；保留有符号加性残差的定义。
4. ε_used与修正约定、实际校准参数/full Cov、run/detector共享模式；至少交付四能量log效率Cov，或可重建它的参数Jacobian。逐线gate/acceptance校正及其同calibration/background的交叉项也须交付。
5. 373.7参考的实际身份、是否同一随机量、组合变换；最好同时保存**归一前**四个修正产额。若只交归一后I，应保真实normalizer相关结构，不能将四个括号误差视独立。
6. 最终四线修正产额的完整4×4 Cov及其与primitive模型的对应关系（避免double counting），包括两个parent之间项；误差分布、coverage/约束和producer/version、control-data谱系一并保存。弱峰比值实际覆盖是否可靠，不能由一阶公式自行认证。

这些字段当前仍unknown；没有为它们填0或虚构数值。只索取同E2比不必强制追加τ/totalBR，但绝对B与完整衰变检验仍各有输入要求。

## 可写回的一项任务推导

可在既有TH19-D25P-005/006后追加：实际四线顺序(o20,i20,o21,i21)的log-response方向为R20=(1,−1,0,0)、R21=(0,0,1,−1)、D=(−1,1,1,−1)；共同373.7/reference和全局scale消去，逐线/能量响应与背景不消。共同幂律效率tilt的D系数为−.117320938，不能排除一般systematics。此项证据类型应为**verified-source-input + task-derived-response-contract**，不能写成thesis直接报告的新实验事实或human-reviewed。

`calculate.py`只读取033实际输入并重建`response-contract.json`，核共同mode与行差代数。没有实际Cov、CI、显著性、模型fit、假计数、phase或模式排他。只写040 worker目录；canonical/raw/PLAN/Bib/Git及session/course状态未动，仍Day24＋恰好Day25未计分预习。
