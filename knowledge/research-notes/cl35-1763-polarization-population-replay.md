---
type: research-note
title: "35Cl 1763-keV偏振与布居正性的源表复算"
aliases: [35Cl1763 population positivity, T71 Table5 replay]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: daily-learning-Day17-L3-source-replay
evidence_sources: [taras-1971-phase-defined-polarization-formulas]
promotion_target: ""
tags: [35cl, polarization, mixing-ratio, positivity, source-replay]
---

# 35Cl 1763-keV偏振与布居正性的源表复算

## Research Trigger

[[taras-1971-phase-defined-polarization-formulas]] T71-D17-1–17在344–345页用实际AD/P例子说明：布居正性可以排除角分布/偏振留下的候选。它给“多解要保留”一个必要补充：有匹配输入与物理约束时，确实可能选根。本页复算该原表的中央逻辑，不将打印误差当完整实验likelihood。

原例γ=1763keV，从1763level到ground3/2+；不同于VT74动机中的3162→1763γ。T71 Table5/Fig2复用Taras–Matas1969数据，原1969primarybody/事件/Σ未取得，不能计两个独立实验。

## Grounded Evidence

原35Cl(p,p′γ)在Ep3.115MeV，以NaI polarimeter测P，30ccGe测AD。Table5有已finitecountercorrect的a2=−.369(.009)、a4=.213(.013)、a0=1；R=1.683(.017)列名为**calculated**；N90/N0=1.22(.01)，物理强度比p=2.30(.08)。这些是同链的观测/响应计算/派生量（T71-D17-9/10），不是三个独立偏振测量。

作者先假定J5/2→I3/2，得到M1/E2 δ2.68(.18)/−.73(.1)，E1/M2近−.02(.02)/pureM2候选，随后以布居正性选M1/E2正根；另讨论a4、βlogft及J7/2的排除（T71-D17-11–14）。本页只复算明确的5/2族，不补未取得的全spin/a6/βprimary输入。

## Assumptions

采用T71的initialleft RB normalizedT幅度、parity-independentSharpZ，指定J5/2→I3/2及两multipole、point90物理偏振、axisymmetric symmetricM布居。原P(m≥0)为±M的folded概率q，sumq=1，不是每个单态概率。中央AD/P当作名义精确输入以检验代数；真实门/接受/背景、联合Cov和原误差bandrecipe未得到。以下区间不是实验CI。

## Provisional Reasoning

### 从方向计数比到强度比

源Eq49为N=(pR+1)/(p+R)。打印R/N中央给p=2.2748596；反用printedp=2.30/R给N=1.2229224，可舍入成1.22。因此不能把这一末位差判为源矛盾。

局部导数为

\[
\partial_N p=\frac{R^2-1}{(N-R)^2},\qquad
\partial_R p=\frac{1-N^2}{(N-R)^2}.
\]

若额外假定R/N误差独立，得到σp≈.093848；只固定两marginalσ而允许任意相关，局部σ范围约.046752–.124214，包含源.08。缺Σ时既不能认证完整误差重放，也不能声称印σ错误。p是J0/J90，boundedP=(p−1)/(p+1)；R是analyzerσ90/σ0，不是RDCO或angularQk。

### 按原Z重建folded布居

新script依T71 Eq7重建Z：

\[
Z_1(LJL'J,Ik)=(-1)^{L+L'+k/2+1}
\sqrt{(2L+1)(2L'+1)(2J+1)^2}
\langle L{-1},L'1|k0\rangle\mathcal W(LJL'J;Ik).
\]

J5/2/I3/2的k2三值为√21/5、−3√15/5、−5√21/49，k4的22项−32√7/49。令F2=Z11−2δZ12+δ²Z22，则本路径的

\[
p_{20}=\frac{a_2(1+\delta^2)}{F_2},\quad
p_{40}=\frac{-a_4(1+\delta^2)}{\delta^2 Z_{22,k4}},\quad p_{00}=1/\sqrt6,
\]

再用原Eq5反演三个foldedq。脚本核sumq=1及回代两tensor。δ0或F2零时，非零a4/a2不能由此有限布居匹配，不将除零赋零。

源Eq39的p(δ)中央解和正性为：

| family | δ中央解 | folded q(.5,1.5,2.5) | 中央正性 |
|---|---|---|---|
| M1/E2 | +2.6832924 | .7030381, .2400318, .0569301 | 全非负 |
| M1/E2 | −.7304459 | .4200983, −.1137001, .6936018 | 失败 |
| E1/M2 | −.0187839 | 264.9251, −395.8743, 131.9491 | 失败 |
| E1/M2 | +104.34452 | −.3350089, .0031547, 1.3318543 | 失败 |

正根与作者2.68中央值闭合；这不是本任务新测得δ。作者把最后一个高M2分量候选列为pureM2；严格中央方程给有限大根，其M2份额.99990816。实际pureM2极限在centralAD下p≈1.996，而不是printed2.30；源误差band/finitegeometryproducer未取得，故保留“近极限/原允许口径未完整重放”的边界，不替作者修表或宣称实验冲突。近100%强度不等干涉幅度可任意忽略。

### central正性域与打印误差带分开

对centralAD、全部实δ，脚本将每q的零与共同分母实极点分区，逐interval检验正性，得到约

\[
[-15.8320694,-.9511806]\ \cup\ [.7899664,3.0427355].
\]

这是指定family/point/中央输入的可行集合，端点需按极点/有限定义区分。原文给出的排除区约−1到.73以及3.27到∞，尚未以其误差/包络recipe重放；不把本中央区间当原文CI或“作者边界错”。本例的四个中央根中只有+2.683在正性域；不推出所有EM、所有J或误差对象都已唯一。

### 源表与失败轨迹

本session独立计算Table3九个K值、Table4十角六列60值、Table6五targetrow共15Z值和Table7八CG，共92值；按原4dec打印精度核通过。Appendix巨大Table6/7其余行仅阅读结构/作用域，未宣称逐项数值认证。

初输入把Table4 40° P6^(2)读成6.7674、80°P4读成.3062；高清原件分别为9.7674和.2659。初合同/结果保留，改的是本任务录入，不是sourceerratum。冻结exercise误称Table3八项，实际九项，冻结文本保持不改。`system/scripts/day17_taras1971_table5_audit.py`与本run `taras1971-actual-contract/result.json`保存完整版本/来源输入与初失败快照。

## Competing Explanations

不同布居、未解析混线、highermultipole或未匹配phase/响应可改变允许族；当前two-multipole正性结论只在本页合同内。原作者称J7/2也被排除，本任务没有其完整rank6/所有EM族/Σproducer，不把本5/2复算当全部spin证明。

## Transfer Conditions

source MethodII的0°/180°annular particlecounter及m限制不自动给finitecone的uniqueρ；精确修需formation/decaymatrix。simpleAD/MethodII与captureisolatedresonance前提不同。消pko需samegate/制备/beamenergy/时间权重及响应；“同时测量”有助减少漂移，不使不同接受或共享误差自动消失。

## Failure Conditions

任意coherentρ、complexphase、不同RME顺序、不同sourceδ、未匹配AD/P、把ratio当boundedP、把不同uncertainty边界拼jointCI均不适用。完整unobservedγUk不是finitegate通道，γ权重不能未经匹配换totalICC强度。

## Falsification or Reverse Tests

sourceZ/CG/K/Legendre数表与tensor往返已核。获得原净峰/逐角谱、a6、完整acceptance、Rcalculation和联合Σ后，可检验原uncertaintybands、literalpureM2及全spin排除。当前不调整a2/a4/R去强配预设根，也不把额外模型witness当新实验。

## Open Questions

原Taras–Matas1969body与数据/responseproducer是否可取；printed允许区具体如何包误差；actualfiniteP与AD correction是否同接受；spin7/2排除使用哪些未列rank或约束？这比再次重跑中央脚本更有信息。

## Human Review

Codex self-audit、provisional；T71旧四false保留，17新claim needs_review，不新增human-reviewed或将本task模型升为实验事实。

## Knowledge Impact and Learning Decision

`supports`作者本例正根中央筛选与AD/P/positivity互补；`limits`“P永不选根”或“P总会唯一”的两个无条件结论。保actualΣ/finitegeometry/全J族边界，不给新的Jπ/δ/实验CI。

## Promotion or Rejection History

2026-10-20从Day17原件主线及实际Table5形成条件source-replay；尚未晋升核素重测或完整实验复分析。

### AD边际误差箱：精确分区与原口径边界

这是source Table5之后的新有界问题，非重跑中央解；使用a2∈[−.378,−.360]、a4∈[.200,.226]，只把所印marginal±sigma定义成矩形，绝不称jointCI。仍是指定J5/2→3/2/sourcephase/point/two-multipole。

令u=√35δ、q=(q.5,q1.5,q2.5)，可由前述Z/CG精确消根号得

\[
a_2=c_2(u)A,\quad a_4=c_4(u)B,\qquad
c_2=\frac{1/10+3u/35-u^2/686}{1+u^2/35},\quad
c_4=\frac{16u^2/1715}{1+u^2/35},
\]

其中A=−4q.5−q1.5+5q2.5，B=2q.5−3q1.5+q2.5。正q/simplex对应固定triangle，给定非零c2/c4的ADbox对应一个rectangle。它们相交状态的变化只能在rectanglevertex触triangleedge、trianglevertex触rectangleedge或c2/c4零处发生；边平行的首次接触也包含vertex/edge临界条件。

新script用QQ多项式枚举临界条件、分解26不可约因子，exactisolation分出51实criticalroots/52open cells，每cell用rationalpolygon/正q witness精确分类。初步未分类的31criticalpoints随后用QQ[u]/factor的canonical元素与隔离区间sign全部补核，没有额外isolated可行点；projective∞另以leadingresponse精确检验不可行。feasibleopenbands有限端点因continuousresponse+compact q simplex/closedbox可取极限，属于可行闭包。由此完整的**该条件模型ADbox**可行集约

\[
[-17.5907969,-.8972833]\ \cup\ [.7501802,3.1186890].
\]

它比central域宽，但不等作者约.73/3.27边界。无原uncertaintyrecipe时不能据差反推作者使用误差倍数/协方差，更不能称源CI已重放。该投影只含ADbox/positiveq，没有把finiteδ的Pbox共同likelihood做成新实验置信分析。

另有一个简单必要界：pureM2极限p=(1−2a2−a4/4)/(1+a2+a4)在此正denominator矩形上对两系数都递减，四corner给范围约[1.9209007,2.0754258]，与所印p±sigma箱[2.22,2.38]不交。这限制literal∞在该point/box解释下的适用；原Table近pure finite大根、bandrecipe/acceptance未重放，不能把它升级为实际测量冲突或全E1M2family的实验排除。

`system/scripts/day17_taras1971_marginal_box.py`保精确隔离区间/所有open-cell witness、boundary分类与依赖hash。本run初open-only contract/result/script、boundary-before/freeze及更新的最终contract/result均保存；冻结原话不改，不把最初31unknown先算成功。新GoogleScholar query定位原TarasMatas1969未取records/body，失败回执保；实际source/Σ缺口仍需新输入。
