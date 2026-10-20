---
type: research-note
title: "PPCO四计数的联合响应与信息自由度"
aliases: [PPCO joint response, fourN information contract]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: daily-learning-Day17-L3-design
evidence_sources: [droste-1999-ppco-polarization, starosta-1999-pdco-experimental-test]
promotion_target: ""
tags: [polarimetry, PPCO, joint-response, covariance, information]
---

# PPCO四计数的联合响应与信息自由度

## Research Trigger

[[droste-1999-ppco-polarization]] DR99-D17-1–14的原件260–270说明PPCO需要四jointW与四计数N；它复用[[starosta-1999-pdco-experimental-test]]同164Yb主数据/响应假设。这里检验：两singleP与两localQ足以决定整个fourN吗；fourN究竟增加几个shape量；为何原AA2精度好而AA1区分力弱？本页是源定义上的条件推导，不是原FORTRAN、实验counts或新的δ/Jπfit。

## Grounded Evidence

原Eq1将physicalP定义为fieldparallel减fieldperpendicular；scatterN⊥−N∥为正A。Eq8对两个局部正交分析器分别施加σ响应，源jointW由cascade/布居/geometry计算，不能先设为两single的乘积（DR99-D17-4）。Eq11–15分别定义PP1/AA1、PP2/AA2；Footnote3明确PP1是两个P之外的新ratio量（DR99-D17-5/6）。

原24Clover选18个，在75.5/104.5度两环，φ近0/30/60/90。a=1、18Clover identical及NORDBALL单器件Q近似EUROGAM是明确假设（DR99-D17-2/3），不是本页验证的实验事实。原Table1的8种positive-parity候选经AA2/4N后仍留1/4/5/8（DR99-D17-8）；需要lifetime等companion，不把四计数或多观测自动等同唯一根。

## Assumptions

只在原Eq8的两局部正交、已相对效率归一的σ响应factorize且同一γ角色/planes/共同门条件下，归一W四概率。Q暂视固定已知；总曝光/接受另由K表述。计数误差段额外假定四类别互斥、无背景/权重、fixedN，仅作localJacobian控制；这些不是原数据已认证条件。自由positiveW例只检验信息映射，不要求它们代表指定核cascade。

## Provisional Reasoning

### 从jointW到四计数

在固定两emissionplanes、给定γ角色/方向/门下，将W总和归一1；字段顺序为∥∥、∥⊥、⊥∥、⊥⊥，令P1/P2为该**共同条件样本**的fieldmarginals，C=PP1。于是

\[
W=\tfrac14(1+P_1+P_2+C,\quad1+P_1-P_2-C,\quad
1-P_1+P_2-C,\quad1-P_1-P_2+C).
\]

这些P不是无gate singles的自动替代；总W/角相关归一若变化须一起传递。W非负要求

\[
-1+|P_1+P_2|\le C\le1-|P_1-P_2|.
\]

对原Eq8的factorized、已相对效率归一且正交响应，单分析器矩阵可归一为

\[
B(Q)=\frac12\begin{pmatrix}1-Q&1+Q\\1+Q&1-Q\end{pmatrix},
\qquad n=[B(Q_1)\otimes B(Q_2)]W.
\]

这里n顺序仍是scatter∥∥、∥⊥、⊥∥、⊥⊥；省掉的总接受/曝光另属K。Q是polarimetersensitivity，不是核角关联Qk。局部探测响应可factorize并不要求源Wfactorize。若存在cross-talk、共同trigger或jointselection不满足此响应式，须先换actualkernel，不能凭两个标量Q继续用本式。

### 哪个量是PPCO额外信息

\[
AA1=Q_1Q_2 C,\qquad
AA2=\frac{Q_1P_1+Q_2P_2}{1+Q_1Q_2 C},\qquad
PP2=\frac{P_1+P_2}{1+C}.
\]

独立symbolic代入Eq8核Eq11–15（包括differentQ时原Eq14的inverse）通过。即使Q1=Q2=Q，一般仍为

\[
AA2=Q\frac{1+C}{1+Q^2C}\,PP2,
\]

因此不能普遍用AA2=Q1Q2 PP2。Q1=Q2=1时两者相等是理想极限；有限Q时AA2含singlemarginal之和及joint分母，AA2精度好不能解释成专测C的能力好。

四normalizedN只有3个独立shape量，分别编码Q1P1、Q2P2、Q1Q2C；未归一总量另由K承载。把AA1/AA2/各PDCO和fourN当多组独立数据会重复使用事件。C=P1P2只在源该条件分布独立时成立，不能从两localQ或不同detector得到。

两个**自设**positiveW控制固定P1=P2=0，分别C=.8与−.4，均W≥0，给予相同两个single asymmetry和AA2=0，却给不同AA1。这只证明信息不由两个marginal决定；不是任一核cascade的实际W、纠缠验证或Belltest。

### 原摘要数值告诉什么，没告诉什么

原490/569keV的R1=1.62/R2=1.57（printed267，DR99-D17-9）经Q=(R−1)/(R+1)给

| 固定原输入 | 中央转换 | 边界 |
|---|---|---|
| Q490、Q569 | .2366412214、.2217898833 | 原response假设下，未补QCov |
| Q1Q2 | .05248462887 | 联合moment反演放大1/(Q1Q2)=19.05319751 |
| AA1=.038(.028) | C≈.7240215、仅AA1传播σ≈.5334895 | 固定Q的局部描述，非full实验CI |
| AA2=.229(.038) | Q1P1+Q2P2中央=.229(1+.038)=.237702 | 未得另一marginal组合与联合Σ，不唯一P1/P2 |

归一响应矩阵的奇异值为1、|Q1|、|Q2|、|Q1Q2|；0<|Qi|≤1时条件数1/|Q1Q2|。有一个Q=0便失去对应polarization信息，不能通过fourN逆恢复；这与事件数/新卡信用无关。原569–577的AA2=.235(.027)推14+ σ/I=.22(+.06/−.11)是另一个cascade的fit输入（DR99-D17-7），不是490–569的第三个独立alignment测量。

### 计数模型的误差边界

若四类别互斥、无权重/背景且fixed总N，多项计数的Σ=diag(Ni)−NiNj/N。在localJacobian阶，

\[
\operatorname{Var}(AA1)=\frac{1-AA1^2}{N},\quad
\operatorname{Var}(AA2)=\frac{1-AA2^2}{N_{\parallel\parallel}+N_{\perp\perp}},\quad
\operatorname{Cov}(AA1,AA2)=0.
\]

最后的零来自该特定分类模型中“落在同号类的比例”和“同号类内部差”的正交，不能外推到两个共同peakfit/共享背景/门求和、finiteN零分母事件或共同校准误差。Poissonized独立primitivecounts同阶得到同样shape式；它不意味着四原子分类的normalizedfractions独立，更不意味着原Tableχ²或两个实验AA没有Cov。Q/geometry/a与背景nuisance需加入完整Jacobian/likelihood。本文没有从AA误差倒造有效N。

## Competing Explanations

原AA2的区分力可来自不同候选的singleP组合，不必全来自connected C−P1P2。Table1保留的多解说明addingjointchannel不保证识别。真实共同校准/不等器件、alignment或finitegeometry变化也会改fourN图形，不能把所有差归于候选spin/parity。

## Transfer Conditions

需sameγrole/planes/geometry/门、相对效率与localresponse定义；源W和总接受共享正确归一。对φ/group/gate求和，应先作用各自response并计权，不能用未说明的两个平均Q代替pair加权Q1Q2。stretchedcascade理论相等不证明同一event多次门计数独立。

## Failure Conditions

任一Q为零、nonorthogonalgeometry、cross-talk/jointselection破坏factorization、未匹配γ角色或无actualbackgroundΣ时，不能用本逆式认证实验PPCO。C的正性域不等任意nuclearpath均可实现；本页不认证原FORTRAN或四计数拟合。

## Falsification or Reverse Tests

symbolicEq8→Eq11–15、differentQ inverse、Q=1极限、detB⊗B=Q1²Q2²、equalmarginal positiveW反例和声明multinomialJacobian均已实际执行。若实际jointkernel不factorize，先否定本标量响应应用；若实际fourN连同Σ支持同一W，则可检验是否独立C=P1P2，而非先假定它。

## Open Questions

原18unit/pair/gate的actualcounts、Q/a逐器件值与Cov、netpeak/background和重复gate分类规则、精确χ²producer/ν未得。当前不能重做原Fig8/9或Table1pvalues，也不能据此裁决164Yb新spin/parity。原15%transition实例不是通用灵敏度下限；未来Q.3@1MeV为模拟/所引private与conference边界（DR99-D17-11/13）。

## Human Review

Codex self-audit、provisional；新claims全部needs_review，未新增human-reviewed或清旧flags。正式论文仍回原件及匹配actualresponse。

## Knowledge Impact and Learning Decision

`supports`PPCO相对两个single的第三shape信息；`limits`fourN自动四独立ratio/唯一Jπ/无条件Q迁移的简写。保原Table1候选与sameST99数据依赖，没有新的实验P、Q、δ、CI或模式指认。

## Promotion or Rejection History

2026-10-20首次以Day17条件推导写入。复算脚本`system/scripts/day17_droste1999_joint_response.py`，本run冻结输入`droste1999-response-contract.json`、结果`droste1999-response-result.json`；仍未晋升实验结论。

### Falkoff1948：相对电场角不是探测器方位角

[[falkoff-1948-polarization-correlation]] FA48-D17-1–8为本session原单页完整letter/表/式复核。原Eq1印cos2φ，φ为两电场相对角，原purequad A_F=2/7与Wmax/Wmin=1.8匹配cos(2φ)，独立exactCG/Jones亦闭合。旧FA48-1的cos²转录已明确撤回，但历史row/falseflag保。不是官方erratum；若改写cos²形式必须同时改幅度和常数：

\[
1+A_F\cos(2\varphi)=(1-A_F)\left[1+\frac{2A_F}{1-A_F}\cos^2\varphi\right].
\]

A_F=2/7时新cos²系数b=4/5；同A裸cos²只给9/7而非9/5。此处方位角不是DR99两emissionplanes的φ。对反向两光子，必须先选同一globalxy并明确第二photon局部e_theta=−globalx，才作PP1桥；未匹配轴不能直接把两个φ设同。

新独立kernel用pureCG(jf mf,Lμ|ji mi)、θ0/π的μ=±helicity、globalxy Jonesoperator和初态I/(2Ji+1)，逐cascadeoperator相乘后求迹；不导入Day16UC/tensor/历史FORTRAN。Table1 J′=J−Δj/J″=J+ΔJ的九dipole表达在J2/3/4共27exactrows核，Eq3号和换secondEM均过；quad J+2→J→J−2在J2/3/4/5均±2/7，relativeφ=π/6/π/4/π/3核cos(2φ)。这是有限组point验证，allJ叙述仍归原作者，不把采样当全域证明。

在该unoriented/backtoback共同轴控制，P1=P2=0但PP1=A_F，直接示范单光子零偏振不排两光子相关；A_F不是单P、计数A或polarimeterQ。若另满足原PPCO局部factorized响应，AA1=Q1Q2A_F；不以此把490/569的Q迁移给Co60。现代Co60混合/源制备、门、finitegeometry仍须原matchinginput。Madansky当时仅settingupapparatus，本文不是新的实际偏振标定/独立实验，原directionalRefs不补actualcounts。

复算`system/scripts/day17_falkoff1948_cg_audit.py`；falkoff1948-CG-contract/result保存本run版本/初scratchimport缺sympy失败及改用已有Wiki依赖的处置。未测任何新核P/Q/δ/实验CI。
