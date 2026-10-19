---
type: research-note
title: "199Tl三线AD：同母态、正布居与取向条件"
aliases: [D66 three AD feasibility, Tl199 sameparent reference model]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
question: "实际三条AD在共同上态约束下，哪些结论依赖额外的取向输入？"
evidence_sources: [diamond-1966-nuclear-alignment-heavy-ion-reactions]
created_from: daily-learning-phys-model
promotion_target:
reproducibility_entry: system/scripts/day16_diamond1966_three_ad_feasibility.py
nuclei: [199Tl]
tags: [angular-distribution, sameparent-reference, identifiability, conditional-model]
---

# 实际AD支持条件解，不把中央数和误差域混为一谈

## Research Trigger

[[diamond-1966-nuclear-alignment-heavy-ion-reactions]] D66-D16-2给出实际197Au(4He,2n)199Tl三线AD及作者“19→5→3”的推断。本文检查共同母态与取向前提，不重新指定199Tl自旋或复现作者的完整处理。

## Grounded Evidence

331和701keV来自同一个上态，370keV来自中间态，底态是749keV、9/2−。原Fig2报告：

| γ/keV | A2 | A4 |
| --- | --- | --- |
|331 |−.58±.03 |−.02±.03 |
|370 |−.36±.02 |−.03±.02 |
|701 |+.26±.04 |−.03±.04 |

原文称AD把19种序列降至5种，再用expected alignment得到3种probable序列；图中后三者为上/中态(13/2,11/2)、(9/2,11/2)、(9/2,7/2)。那5个中间候选的完整列表与原producer未取得，不替作者补表。ICC与其它资料仍是作者所需companion。

## Assumptions

本run采用明确point、4π归一的Legendre模型。上/中态候选各为5/2至13/2，三条spin差≤2，恰有19对。|ΔJ|=2只取L2，其余允许real native L1/L2混合；全取负宇称可给一组合法的AD实现，但不是实测宇称指定。

331与701共享一个非负对称P(m)；370的total P(m)另作未知，不能因看见331 feeding就假设中态只由这条线布居。响应、方向门、feeding强度与联合Cov未恢复。每个quoted±数只作为所选边际box半宽，不把它当联合置信域或原实验likelihood。

对照两域：任意非负对称q；额外要求上态与中态各自`u2≤0`。后者仍比固定Gaussian弱，是模型前提。

## Provisional Reasoning

### 找到的正布居解是存在证据

固定arctanδ网格步长5°，每组振幅下用LP最大化所有|m|pair概率的共同下界。先找独立370域，再查共享上态的331/701。5845次LP中找到：

| 取向域 | 有严格正q的网格序列数 | 正确含义 |
| --- | --- | --- |
|free positive q |8 |至少有这8个条件解，非完整允许数 |
|额外u2≤0 |3 |找到作者列出的3个probable序列，未证明只有3个 |

有限网格零命中不能排连续δ或孤立根。这不是复现原“19→5”，也不能把8/3当实验后验、候选概率或新指定。

例如(上态13/2、中态11/2)有如下低m条件解：native β331=−20°、701为pureL2、β370=−15°。输出(331 A2,A4)=(-.55,+.01)，701=(+.259173,−.032057)，370=(-.34,−.01)，均在所设box内。它们在部分box边界上；“strict”仅指所有q严格为正。

为使witness不只保存在outputs，上态按|m|=6.5,5.5,…,.5的pair概率为：

`qtop=(e,e,e,e,.483316664716,.376639232863,e)`，`e=.0280088204841`。

中态按|m|=5.5,4.5,…,.5为：

`qmid=(f,f,f,.690083622463,.160767245802,f)`，`f=.0372872829338`。

每一±m各取pair的一半。其u2上/中态约−.181421/−.133441；这是数学布居，不是测得的PM或D66作者δ。

free域还找到例如(7/2,9/2)的正q条件解，所给中态u2≈+.326086，说明该witness并不满足低m前提。不能由这一点断言该序列在整个lowm连续域无解，也不能把其高m布居说成实际反应产物。

### 中央A4的必要关系不是带误差数据的排除

对同一上态，L1纯项和L1/L2干涉都不含rank4；所以A4由高多极photon份额`f=δ²/(1+δ²)`乘共同rank4矩给出。独立6j与photon核核对，三组作者probable spins的pureE2系数比A4(331)/A4(701)依次为：

`−8/3、−16/39、−8/7`。

核与这些精确比的最大差小于7.6×10^-15。若两条A4中央值均非零且同为负，这些负比例不可能由非负f满足；因而这三组在**精确中央数**问题中不闭合。但两个A4的quoted-margin区间都含0，前面的共享上态witness也确实在区间内。不能把中央数的必要失配改写成实验自旋被排除。

若将quoted误差条件性地当作边际标准差，写必要残差`r=A4(331)+k A4(701)`，k≥0。其中央绝对值为`.02+.03k`；允许任意PSD相关性时，标准差的上界为`.03+.04k`。故

\[
\frac{2}{3}\le\frac{.02+.03k}{.03+.04k}<\frac34.
\]

这一比使用“最大允许标准差”，不是实际z值；它只说明该数对不给一个对所有未知Cov都成立的一倍标准差排除。实际联合统计仍需原谱/拟合Cov。

## Competing Explanations

源作者的expected alignment、几何与拟合流程可能比本模型的任意q更强。任意非负q可容纳与入口反应机制不相称的布居；lowm又只是二阶矩条件，不等于Gaussian。三种域不能混用，也不由当前数学witness对源作者的5个或3个候选投票。

## Falsification or Reverse Tests

后续若取得真实response、trigger/feeding及联合Σ，应按同一观测对象重建域；若它排除现有freeq witness，更新条件解，不把旧存在证据删除为“从未存在”。若要证明完整spin允许数，需连续参数的根/可行域证书，当前网格不能承担该结论。

## Agent Self-audit Triage

P0：未识别未隔离的原件身份、权限或路径问题。D66输入和旧helpers哈希保持。

P1：所有新增native振幅、PM、网格计数和误差域均为Codex条件分析；未恢复原角响应、全部5候选、δphase或联合Cov，不赋予实验Jπ/δ/CI。

## Reproducibility

[网格/LP程序](../../system/scripts/day16_diamond1966_three_ad_feasibility.py)actualexit0；[独立rank4/误差/全部witness重构](../../system/scripts/day16_diamond1966_rank4_certificate.py)actualexit0。11个记录（8free与3lowm）逐个从kernel重构，observable差0、box残差约1.6×10^-15。合同和post-grid设计时序均保留，不冒称盲测；没有生成toy counts。

## Transfer Conditions

只迁移“同母态共享密度、中央值与误差域分开、存在与排除分开”的方法。换spin、门、响应、rank或δ约定均需重建，不能拿这些native数填其它核素。

## Failure Conditions

源系数并非这里的响应层、两线非相同条件布居、实际角门改变density、原不确定度不支持所设box，或任一正性/归一/核验失败时，模型不用于实验赋值。

## Open Questions

作者AD-only五个候选的具体名单和complete-alignment约束怎样实现？实际三线共享何种trigger、角响应和Cov？有哪些匹配ICC/参考线能区分probable序列？

## Human Review

尚无本note的用户审核；旧D66人审只属于其原前缀，新分析保持unreviewed。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
| --- | --- | --- | --- | --- | --- |
|2026-10-19 |created |none |provisional |实际AD、共同母态与正q存在证据；实际response/Σ仍缺 |不晋升实验结论 |


## 后网格连续域审计与漏解

看到原8/3网格结果后才冻结本层合同，未改源误差盒、positivepopulation域或已有振幅/模型。系数用独立Racah/CG高精度构造，与原helicity核逐项差小于3×10^-12；native cross项相位匹配不当D66作者δ桥。

每个β区间内系数均为`a+b cos(2β)+c sin(2β)`，用解析极值加1e−10向外padding构造逐vertex必要LP。q≥0保证entrywise界给真实域的外包。若非负dual权重λ满足

`min_vertex(λᵀ A_vertex)−λᵀb > 1e−8`，

则该外包分离；否则检验原核中心点或细分。预算/最小格宽不能分离的叶子原本应保留undecided，本次结果没有此类叶子。浮点/outward padding合同明确，不称形式化exact-real证明。

此检查找到了5°粗网格漏掉的freeq序列(上/中态)=(11/2,11/2)，native(β331,β701)=(5.625°,−84.375°)。固定这些β不变，再最大化box内部余量得到一个新的严格内部witness：

`qtop=(.437179930762,.538451260378,g,g,g,g)`，`g=.00609220221487`，按|m|=5.5,4.5,…,.5。

中态β370=−15°，

`qmid=(h,h,.0259229463655,.899502487767,h,h)`，`h=.0186436414669`。

高精度重构的(331 A2,A4)=(-.566789,+.00002918)，701=(+.233120,−.00311964)，370=(-.346691,−.0166910)。上/中态分别保留约.328/.335个quoted半宽的共同内部余量；不是靠LP容差卡在box边上。此上态布居偏高|m|，不满足lowm前提。

独立80位重放不用原区间/分离器函数，重建系数与极值、核每个dual余量，并用有理dyadic路径的prefix-free/Kraft sum1检查完整覆盖。16个negative子问题共23个叶子，最小高精度分离gap约.00170146，远高于1e−8阈值；原source/box/hash不变。

本run现在对**这一个声明point/轴对称/矩形误差域**给出数值覆盖分类：freeq九个序列有存在witness，其余十个在此外包/精度合同下分离；额外lowm有三项witness、其余十六项分离。新9/3不是D66实验允许数、未恢复作者19→5流程，也未认证真实角响应/联合误差。此前“至少8”的旧网格结论保留为历史，不能继续写成完整8个。

## 偏振companion先绑定完整振幅域

继续使用同一源ADbox，没有测得新的P。对四组已知β（源三个probable网格点及上述新点），允许q在共享母态ADbox内变化，以Charnes–Cooper分式LP分别投影θγ=90°处signedP；这不是完整βprofile，更不是联合CI或两个P的矩形联合域。

| 上/中态 | 固定β331/β701 | P331投影 | P701投影 |
| --- | --- | --- | --- |
|13/2、11/2，lowm |−20°、pureL2 |[−.04514,−.03536] |[+.42955,+.50780] |
|9/2、11/2，lowm |+15°、−15° |[−.04669,−.04655] |[+.73507,+.73797] |
|9/2、7/2，lowm |−10°、−10° |[−.19969,−.19130] |[+.70690,+.75278] |
|11/2、11/2，freeq |+5.625°、−84.375° |[−.59379,−.55946] |[−.13625,−.07303] |

它们给可能有信息的同线偏振测量方向，但这些固定点的分离不证明整个spin/mixing族可分。实验仍需同trigger/gate/feeding、相位/物理轴、响应与联合误差；θγ90°是核发射相对beam的角，不是Compton散射角。

全19spin路径/pair核控制给pureM1 `Q90=1.5 A2`、pureE2 `Q90=1.5 A2+.625 A4`，I90由A2/A4重构；这里Q90为光子Stokes分子，不是polarimeterQ。把AD导出的pureP再当独立伴随观测会重复计证据。EMduality保持AD并翻P，不能在未知宇称时省掉这种竞争。

新11/11点的701虽然E2辐射份额约99.04%，P也不能直接替pureE2值；有限低多极振幅保留干涉，强度百分比不是忽略相干项的充分判据。这里的数只是条件witness，不是实际701混合比或新的实验E/M赋值。

[连续域程序](../../system/scripts/day16_diamond1966_continuous_domain.py)、[独立重放](../../system/scripts/day16_diamond1966_domain_replay.py)及[偏振投影](../../system/scripts/day16_diamond1966_polarization_companion.py)最终实际exit0；首个numpy API/错误helper import失败保留，修正未改任何科学输入。所有新内容仍provisional，无新spin/δ/P测量。


## 全β伴随符号检查：固定点分离并不延伸到候选族

在同一ADbox/取向域/指定same-parity M1+E2内核下，继续对四个spin对做β全区间的P701正、负可行性检查。不是新增偏振数据，也不把其它E/M dual候选排除。结果为：

| 上/中态与取向域 | 负P701的存在点 | 正P701的存在点 |
| --- | --- | --- |
|13/2、11/2；lowm |无；pureE2解析Q90下界+.28625 |+.38404 |
|9/2、11/2；lowm |−.03648 |+.47152 |
|9/2、7/2；lowm |−.04246 |+.42747 |
|11/2、11/2；freeq |−.13625 |+.85700 |

各存在点均回原核/80位Racah–Stokes重构，满足ADbox、正q及相应取向条件；部分q仅为预设floor1e−7、observable也可在box边界，不称为所有物理机制都支持。唯一的负域分离项另有纯E2恒等式：`Q90=1.5A2+.625A4≥.28625`、I90>0，因此不依赖网格；它只是已指定阶次/物理轴的条件符号界。

这说明前节三个混合候选的固定点P投影差异不能支撑“P701符号必能区分全族”。两个lowm混合族和新free族各允许正负号，至少仍须完整P值/误差与其它门/参考、phase和响应联合检查。未知EMduality还可翻P而保持AD，实际没有新的唯一Jπ/δ结论。

另一个精确关系解释了近pure强度也可有偏振偏移：在本M1/E2、θγ90约定下，令`A2_int=2 cosβ sinβ × A2_LH`为二阶干涉贡献，则

`Q90_mix − [1.5 A2_mix+.625 A4_mix] = −2 A2_int`。

pureL1/L2项逐一消去，差只来自干涉。因此upper强度1−ε并不使修正按ε下降；振幅交叉项可按sqrt(ε)量级保留，还受spin/取向系数影响。本模型新点99.04%E2但P701≈−.08548，而同一AD的pureE2反事实约+.39413；这不把该点说成实验测量。

[全β符号程序](../../system/scripts/day16_diamond1966_fullbeta_Psign.py)和[独立MP80复核](../../system/scripts/day16_diamond1966_fullbeta_Psign_replay.py)实际exit0；七个正q/非零符号witness、一个负域dual与纯限解析界均通过。当前只完成既有四候选的符号问题，未计算全9候选的联合P331/P701 likelihood或置信区域。
