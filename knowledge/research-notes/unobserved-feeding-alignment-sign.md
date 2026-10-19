---
type: research-note
title: "未观测feeding的二阶取向：保号条件、符号反例与Gaussian边界"
aliases: [Unobserved feeding rank2 sign, C96 signed U and Gaussian replay]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
question: "何时可由入口取向与退激路径支持u2符号，而不假设一个Gaussian宽度？"
evidence_sources: [diamond-1966-nuclear-alignment-heavy-ion-reactions, cejnar-1996-spin-deorientation-alpha-2n-gamma, nndc-2017-99rh-matched-reference-records, martin-1987-ensdf-mixing-ratio-phase-conventions]
created_from: daily-learning-phys-model
promotion_target:
reproducibility_entry: system/scripts/day16_alignment_transfer_sign.py
nuclei: [99Rh, 110Cd, 112Cd]
tags: [alignment, feeding, deorientation, Gaussian-assumption, conditional-model]
---

# 保号不等于不变宽，也不等于已测得取向

## Research Trigger

[[rh99-1117-population-feasibility]]的EM排除依赖额外条件u2≤0。[[nndc-2017-99rh-matched-reference-records]] N099-7/13尚未给出匹配的实验取向参考。因此要区分三件事：反应几何为何使低|m|成为合理预期、哪些退激路径保留二阶矩符号、实际实验是否满足那些路径和选择条件。

[[diamond-1966-nuclear-alignment-heavy-ion-reactions]] D66-1/2/4/9给出入口轨道m=0、蒸发后保留取向的物理预期，以及Gaussian偏差与同母态pure参考的限制。它没有对Rh99逐条证明。[[cejnar-1996-spin-deorientation-alpha-2n-gamma]] Eq1/5/6提供明确的orientation-flow与U定义；其p229还写U属于(0,1)。本note检验该定义的精确数学域，不把作者的反应模型与任意角动量通道混成一个命题。

## Grounded Evidence

- D66原3页1205–1207重新完整读到自身参考文献，排除1207下半的另一篇地磁论文；Fig1/2原式和符号核。
- C96原19页225–243、Eq1–9及7图主线重新读取。C96-5/6/7/11已说明side-feeding与total population不同，以及具体反应的近Gaussian结果不能普遍迁移。
- N099-14的278.5和867.8分别给25/2→23/2与27/2→23/2的实际feeding路径；它们属于2014记录，不能移作P00的实际feeding权重。
- 两个旧source的人审前缀、旧claims和review字段保持；本日新推导/计算独立标为Codex模型与unreviewed。

## Assumptions

单个固定Ji、Jf和发射系统总角动量j；所有发射方向及其自旋/偏振均未观测，完整trace；核自旋取向在共同束轴定义，没有额外外场、方向门或未建模的选择。用于显式概率图的初态密度对角；旋转协变的张量结果本身不限于一个Gaussian。

粒子总j包括其轨道与自旋耦合；γ的总角动量取L。模型不指定真实蒸发j分布、各路径强度、compound spin分布或反应代码。角动量单位取ℏ=1。

## Provisional Reasoning

### 完整未观测通道的精确矩转移

非负、列归一的CG映射为

\[
T_{m_fm_i}=\sum_q|\langle J_fm_f;jq\mid J_im_i\rangle|^2.
\]

定义`μ2(J)=⟨3m²−J(J+1)⟩`。令I=Ji(Ji+1)、A=Jf(Jf+1)、b=j(j+1)、x=(I+A−b)/2，则

\[
\mu_{2f}=c\mu_{2i},\qquad
c=\frac{3x^2-3x/2-IA}{2I^2-3I/2}.
\]

这是本run的张量投影推导，并由每个m的CG映射及独立6j逐项检查。一个推导入口是把`Qab=½(JaJb+JbJa)−δab J²/3`投影到固定Ji子空间，使用`Ji·Jf=x`、`Qi·Qf=x²−x/2−IA/3`与`Qi·Qi=2I²/3−I/2`。Ji<1时没有rank2张量，不能对上式的零分母硬取值；程序另核这类初态不能产生未观测的rank2矩。

C96的B2与这里的μ2、u2不是同一个归一：

\[
B_2=\sqrt{\frac{5}{J(J+1)(2J-1)(2J+3)}}\mu_2,
\quad u_2=\frac{\mu_2}{2J(2J-1)}.
\]

因此c、C96的U2和u2的转移因子可有不同大小，但正归一不改变其符号。两条实际Rh99 spin路径若按所列pure multipole和完全未观测处理，得到：

| 条件路径 | μ2转移c | u2转移 | 实验边界 |
| --- | --- | --- | --- |
|25/2→23/2，L1（278.5） |253/300 |1 |不是已测feeding density或pure程度 |
|27/2→23/2，L2（867.8） |253/351 |1 |同上，且非P00同采集权重 |

u2不变不表示磁子态宽度或完整P(m)不变；也不能把c或u2转移误写为C96的U2。

上表的精确c与u2转移数只属于pure项。若完全未观测的feeding仅混合L1/L2，则两分量均在保号域时，未知混合份额也不改变符号。这与参考AD的F2不同：后者保留干涉项，故其符号可能需要更严格的混合界。完整trace与被观测的参考线不能互换。

### 可以证明的高自旋低L保号域

对所有Ji,Jf≥5/2、L=1或2且角动量三角关系允许的γ路径，c严格为正。证明按n=Ji−Jf的八种情况展开，取`Jf=5/2+max(0,−n)+s`、s≥0；分子与分母均得到系数全正的多项式。

例如L2、n0时，分子为`2s⁴+24s³+(175/2)s²+93s+14`，分母为`2s⁴+24s³+(211/2)s²+201s+140`。其余七项的完整系数证书与CG边界核验保存于程序结果。另对Jf=23/2、j=.5,1,1.5,2,2.5,3的全部27条允许Ji路径逐项核，c均正；这只是有限域验证，不是P00蒸发角动量的测量。

若每条实际feeding链都满足保号条件，初始μ2≤0的非相干正权重混合仍满足末态μ2≤0。这比指定Gaussian宽度弱，但必须验证整个相关链，不能只核最后一条γ。

### U可以为负，方向门也会改变对象

C96 Eq6与上述CG定义相容，但其p229的“U∈(0,1)”不是任意允许角动量的恒等式。直接代原Eq6得到：

| Ji→Jf；j；rank | 精确U |
| --- | --- |
|1→1；1；2 |−1/2 |
|2→2；2；2 |−3/14 |
|23/2→23/2；11；2 |−37/575 |
|5/2→5/2；2；4 |−1/2 |

前两项是合法低自旋通道，第三项说明仅“自旋高”仍不足；第四项说明rank2保号定理不自动给rank4保号。这些是定义的数学反例，不证明作者在Cd所采样的实际代码路径或实验结论错误。

完整CG通道的两端均匀分布仍为均匀分布。C96 Eq1的各rank基函数在均匀m边际下二阶范数为1；U就是两端基函数在CG联合分布中的内积。Cauchy–Schwarz给一般界`abs(U)≤1`。对rank>0，其均值为零，也可把它理解为相关系数。负U允许取向反号，同时不违背幅度界。

Ω也是有符号的量。原Fig1的J5、L1支路给U2=9/10，B2<0，故以单位feeding归一时`Ωout>Ωin`而`abs(Ωout)<abs(Ωin)`。描述“衰减”时须说明幅度，不能把signed flow当非负粒子流做同向不等式。

方向门破坏完整trace的假设。对相同25/2→23/2、pureL1和各向同性初态，全部未观测时u2f=0；选择发射沿束轴的光子后，子态u2f=+.05，选择90°方向时其束轴二阶矩为−.025。后一条件还可引入非轴对称张量。这个PSD控制使用既定物理路径，不是Rh99的观测或模拟计数；它说明“有门”和“未观测”不能共用同一U。

### 原Fig1两条模型链的重放

按C96 p232 Fig1原标注，从J5、m0出发分别计算：

1. `5 →(j=1/2) 11/2 →(j=1/2) 5`；
2. `5 →(j=3/2) 11/2 →(j=3/2) 5 →(L1) 5 →(L1) 5`。

完整P(m)、rank0/2/4/6/8/10与Eq6都逐步闭合。第一链末态只有`p0=6/11、p±1=5/22`，其它m为零；它显然不是有限σ的精确Gaussian。

把末态B2或B4分别投影到`P_G(m)∝exp(−m²/(2σ²))`，得到：

| 原模型链 | 只匹配B2的σ2 | 只匹配B4的σ4 | 性质 |
| --- | --- | --- | --- |
|两s波中子 |.6756862 |.6814923 |低阶矩较接近，但完整分布非Gaussian |
|两p波中子、两dipole |2.1461374 |2.5715712 |两阶给不同宽度，不强制压成单σ |

这些是源作者模型序列的重算，不是Cd实验σ。以`r=exp(−1/(2σ²))`把各匹配方程化为有理系数多项式，再用Sturm计数和根隔离核全物理区间0<r<1；四个方程均仅一根，没有用网格零命中排除孤立根。

相应Gaussian与精确P(m)的总变差距离约.056–.060及.195–.215；只是模型分布距离，不是p值或实验误差。第二链的两宽度差不等于C96 Fig2实际side-feeding ensemble的误差，不能拿它否定作者在特定Pd反应中发现的近Gaussian关系。

原文`ln U4/ln U2`的deorientation曲线幂律还要求所用步长相同、U2/U4为正且分母不为零。不能对上述负U、零U或U2=1直接取实对数，也不能把某一链的关系当任意feeding平均的Gaussian证明。

## Competing Explanations

低|m|可以由入口几何和保号链支持，也可以被未知较大j、低自旋通道、方向门或外场改变。Gaussian拟合只是更强的一种表示；即使B2/B4近Gaussian，完整P(m)、高rank或其它条件样本也可能不同。detector finite-angle attenuation另属响应，不能混作核取向转移。

完全未观测的混合跃迁无L与L′干涉；但若包含内转换，总衰变权重须按[[martin-1987-ensdf-mixing-ratio-phase-conventions]] MA87-3的`Δ²=δγ²(1+αL′)/(1+αL)`处理。光子样本、总衰变样本与单壳电子样本分开。只有每个参与分量都保号时，正权重的具体大小才不影响这一符号结论。

## Falsification or Reverse Tests

已有三个rank2负U、一个rank4负U和一个方向门控制，足以推翻“任何未观测发射都会同号衰减”以及“high spin本身足够”的无条件说法。八个正多项式证书支持一个更窄、可复用的充分域。

若恢复P00实际入口、粒子j/feeding强度、门与环境后发现全链满足该域，额外lowm条件可取得反应模型层的支持；仍应与同条件reference实验交叉核验。若有显著出域通道或direction selection，则必须重新传播，不能用调σ、Q或删除原freeq witness维持判决。

## Agent Self-audit Triage

P0：未识别未隔离的原始来源/权限/路径问题。原件哈希和旧人审前缀保留。

P1：所有新系数、保号域、反例和Gaussian重算均为Codex条件模型；它们不测定P00/Rh99的实际u2、δ、宇称、统计置信度或Avalanche II producer。C96原literal与新定义核验分列，旧用户审核不被冒充为本日审核。

## Reproducibility

[rank2程序](../../system/scripts/day16_alignment_transfer_sign.py)及[原Fig1重放程序](../../system/scripts/day16_cejnar1996_transfer_replay.py)均actualexit0。合同、原件/前缀hash、实际执行与完整结果在本run的`alignment-transfer-*`和`cejnar1996-transfer-*`回执。现有photon helpers只读，未安装依赖；沿用固定PYTHONPATH与SymPy版本。

## Transfer Conditions

只迁移明确的完整trace、spin/j域和张量归一。换核、换反应、换门、换rank或把光子权重换成totalICC权重，都要重新核对象。C96的source-authored两链也不能代其它反应的真实population。

## Failure Conditions

方向或粒子postselection、未处理的外场、实际j/feeding出域、源phase/归一不明、非正概率或CG/6j不闭合时，不使用本note赋值。低阶Gaussian相合不能替代完整输入合同。

## Open Questions

P00实际入口/蒸发/γfeeding是否能在不强加Gaussian的情况下独立约束u2符号？C96实际Avalanche II采样的U2/U4域和T_l输入是否公开？哪些同母态reference能同时测得混合纯度、AD和条件密度？

## Human Review

本note尚无人类审核。旧D66/C96用户审核只属于各自保留的原前缀，新推导与追加claims均保持unreviewed/needs_review。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
| --- | --- | --- | --- | --- | --- |
|2026-10-19 |created |none |provisional |实际source、精确CG/6j/多项式与反例，真实反应输入仍缺 |暂不晋升实验结论 |


进一步的实际AD检查见[[199tl-three-ad-reference-feasibility]]：[[diamond-1966-nuclear-alignment-heavy-ion-reactions]] D66-D16-2数据在freeq与额外lowm条件下给不同存在witness；它没有恢复真实reactionprior，也不把源19→5→3化为本run的新完整允许数。


## 原producer可用性与已知反例的重叠核验

C96-D16-8的1993Ref8身份已核，但限定公开route只得metadata、未得原代码/反应输入，缺口不能用本run自有程序替代。C96-D16-9与[[yamazaki-1967-aligned-angular-coefficients]] YA67-4/7的定向原p3/7复核说明：negativeU例此前Day14已持久化；本session新增的是C96 literal/domain crosswalk、八类保号证明与原Fig1精确PM/Gaussian重放，不声称第一次发现负U，不重计旧脚本数或独立实验证据。YA67知识页核后无需改写。
