---
type: research-note
title: "99Rh1117：实际AD/P摘要在非负布居约束下能排除什么"
aliases: [Rh99 1117 positive population feasibility, P00 conditional branch audit]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
question: "不预设Gaussian布居时，原1117的AD/P边际区间是否仍区分EM候选？"
evidence_sources: [palit-2000-rh99-clover-polarimetry]
created_from: daily-learning-phys-model
promotion_target:
reproducibility_entry: system/scripts/day16_rh99_population_feasibility.py
nuclei: [99Rh]
tags: [alignment, covariance, identifiability, conditional-model, mixing-ratio]
---

# 实际观测摘要与布居正性：可行模型不是新实验δ

## Research Trigger

[[palit-2000-rh99-clover-polarimetry]] P00-4/5报告1117keV、Ji=23/2→Jf=21/2，Legendre a2=−.16(.01)、a4=.01(.01)、plane-axis P90=.37(.21)；作者联合AD/P选择近pureE1+M2。本文问：不把未给出的Gaussianalignment当已知，只要求轴对称、P(m)=P(−m)且非负，已报摘要在明确point模型下还容纳哪些候选？

本note持久化理由是实际source输入的可识别性/失败控制可跨任务复用，且可改变“给出a2/a4/P就唯一”的方法判断。它不是重新测量δ、置信区间、原producer复现或新的99Rh宇称赋值；原作者结论保留为原作者的分析。

## Grounded Evidence

- P00-4给同跃迁原AD/P和spin对象；P00-5给竞争EM曲线和作者排除理由。
- P00-1/3/8/11保留finitegeometry、reference和完整Cov缺口；point核不能假称真实实验响应。
- 全部source原件/printedinputs/hash未改。第一个β网格前冻结source均值/区间、模型/LP/tolerance；看到网格结果后才设计的逐根与凸包证书明确标记post-grid，不冒称事前盲注册。

## Assumptions

只取单emitter、real相邻multipoles、未额外去取向/feeding、pointgamma角，native振幅坐标δ=tanβ。两family为M1/E2与E1/M2，原source/KS/RB的完整δ相位桥仍未认证；这里的正负号只属于明确的native内核。

Ji=23/2有12个|m| pair，令q_i≥0、Σq_i=1，每对±m各取q_i/2。photon-helicity/Jones振幅给每个pair的I和Q；Legendre a2/a4、I90与Q90对q线性，I90=1−a2/2+3a4/8。每个δ下，用LP求下列条件的可行性：

- exactcentral：a2=−.16、a4=.01、Q90=.37 I90；
- marginalbox：a2∈[−.17,−.15]、a4∈[0,.02]、.16 I90≤Q90≤.58 I90。

这个box仅逐坐标使用quotedmarginals；它不是联合1σ区域，也不估Bayesianposterior或频率置信度。LP目标是可行/最大最小q，不是χ²或实验likelihood。

## Provisional Reasoning

三段实际执行均exit0：[grid程序](../../system/scripts/day16_rh99_population_feasibility.py)、[孤立根程序](../../system/scripts/day16_rh99_population_rootcheck.py)、[凸包/strictq程序](../../system/scripts/day16_rh99_population_certificate.py)。完整合同、旧结果与post-grid设计都在同run receipts。

纯基的4π强度归一、cross积分0、rank6/8为数值零、I90由a2/a4重构、EMdual的I相同/Q反号、pureM1的P–a2关系均先验控制通过；不clip非物理Stokes或改输入。β=±90是pureupper的同一全局相位极限。

### 网格与孤立根不能混淆

−90…90°、step.25°网格在marginalbox找到M1/E2的204点和E1/M2的26点；所见窗口分别为12.75–47.75°、67.75–83.25°及−2.5–3.75°。这只是采样可行点，不能宣称连续边界精度或把点数当概率。

exactcentral网格没有命中。固定三个精确观测时可行δ可能是zero-measure孤立根，因此本run没有把“0点”报为“无解”。随后把rank2/rank4核向量分解，centralP方程成为二次式，找全部realroots并逐根回原LP：

| family | native δ根 | q正性结果 | 适用含义 |
| --- | --- | --- | --- |
| M1/E2 | .2931401346 | 可行；严格正q可重现三个central值 | 声明point/freepopulation模型的数学witness |
| M1/E2 | 9.184370799 | 不可行；有凸包分离证书 | 仅排这组exactcentral/model合同 |
| E1/M2 | .04838995835 | 不可行；有凸包分离证书 | 不将带误差数据等同精确均值 |
| E1/M2 | 55.63773527 | 不可行；有凸包分离证书 | 同上，不否定源E1归属 |

看到central根结果后又保存了post-root证书合同。对三个不可行根，所需rank2/rank4矩落在12个physicalpair点的凸包外；所给线性不等式对每个vertex的最大lhs≤约6×10^-17，而所需点违反量约.07120、3.33826、.45716。它们不只是一条solverinfeasible消息。

### 严格正布居witness

按各自原约束最大化所有q_i的共同下界ε，所得三个witness均每个pair概率严格正；不是依靠negativeweights、clip或单个purem边界点：

| family/约束 | native δ | min q_i | a2 | a4 | P90 |
| --- | --- | --- | --- | --- | --- |
| M1/E2 /central | .2931401346 | .048840 | −.16 | .01 | .37 |
| E1/M2 /box | 0 | .039103 | −.15 | 约0 | .209302 |
| M1/E2 /box | 3.732050808 | .057612 | −.15 | .02 | .165020 |

为使证书本身不只留在outputs，保留central M1/E2的完整q结构：按|m|=23/2,21/2,…,1/2顺序，

`q=(.145703938351223, .365898412762607, ε, ε, ε, ε, ε, ε, ε, ε, ε, ε)`，`ε=.048839764888617`。

每一±m各q/2，和为1；这些数来自明确LP，不是实测磁子态。另定义`M2=Σq_i A2_i(pureM1)`、`M4=Σq_i A4_i(pureE2)`，一个可复核的physical hull必要不等式为：

`0.969591608508 M2 − 0.244728651186 M4 − 0.329142301885 ≤0`。

central大根δnative=9.184370799需要`(M2,M4)=(.415447911295,.010118549897)`，lhs≈+.0711962，故不满足这一模型必要条件。

所有witness的约束残差≤约4.1×10^-15。pureE1的a4有−1.2×10^-15浮点残差，按事前1e−8残差门解释为数学0，没有修改source下界。q向量全值留在[证书结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rh99-1117-certificate-result.json)。这些q不是测得布居，也未证明这类布居能由真实fusion反应产生。

## Competing Explanations

本结果`limits`在未给出alignment/response/联合Cov时，仅由边际误差条推出EM唯一性的强措辞：在这一声明box/freepositivepopulation模型中，两类EM候选均有严格正witness。它不表明原实验真的留下同样的联合概率区域，因为原covariance/finiteacceptance/作者selection尚未恢复。

exactcentral只保留一个M1/E2数学根也不构成新的M1赋值。真实数据有误差，原作者以其它假设/资料选E1，point响应和自由P(m)都不是已认证的实验描述；源E1仍在所设box内可行。不能将source均值的正性失配改写成实验错误或新parity。

必要companion包括：同实验、同条件的reference所约束P(m)/rank2/rank4；逐角response与calibrationP的方向tag；a2/a4/P联合Cov；作者F/δphase/AD拟合约束。给δ强制Gaussianσ或调Q直到重合都不能代替这些输入。

## Falsification or Reverse Tests

此前直觉是“actuala2/a4/P可能已足以唯一选择EM”。网格和严格正witness把该说法限制到明确的population/response/联合误差条件。另一个认识修正是：连续参数的孤立解不能由有限网格0命中排除。

若拿到原作者明确的alignment/reference、actualresponse与联合误差后排除了所有sameParitywitness，方法排序应更新；若在同样假设下可复算原reportedδ的profile，才可能从本note进入experimentalfit。当前不具备该输入，不提升L4或模式结论。

## Agent Self-audit Triage

P0：未识别未隔离的技术/来源身份问题；所有模型/数据边界已显式给出。

P1：centralroots、采样窗口和convex证书都是Codex条件模型结果。论文使用时须回P00原AD/P、完整response/Cov和phase；不将nativeδ当reportedδ或实验信赖区间。

P1：严格正q只证明这个数学模型有解，不给fusionreaction布居的实测支持；源parity/组态未改。

## Reproducibility

原[合同](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rh99-1117-feasibility-contract.json)、[网格结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rh99-1117-feasibility-result.json)、[逐根结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/rh99-1117-rootcheck-result.json)及上方证书结果保留源码/输入hash与实际exit。原PSD/helicityhelpers不改；环境为本run固定SciPy1.18.1/NumPy2.5.3/SymPy1.14.0和明确PYTHONPATH。没有新随机toycounts、实验δ或人审标记。


## Transfer Conditions

只迁移“已知source摘要→声明物理域→正性/根/误差域分开”的分析程序；其它spin、δphase、acceptance或feeding需重建kernel。LP可行点和box不得移作联合统计区间。

## Failure Conditions

真实response/联合Cov或物理布居机制若不满足这里假设，witness只对本模型有效。未识别相位、source参数对象、极限/归一失配或正性证书失败时，不能推进实际核赋值。

## Open Questions

原source如何约束B2/B4或σ/J、如何处理reference方向门及a2/a4/P共同误差？是否能取得actualresponse/producer以替代point模型？这些是判别力的输入，当前不补猜值。

## Human Review

尚无本note的用户审核轮次；review_status保持unreviewed。完整P1清单见上方self-audit，Codex可继续相称自审但不写human-reviewed或清源needs_review。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
| --- | --- | --- | --- | --- | --- |
| 2026-10-19 | created | none | provisional | P00实际摘要与三段可复算模型/证书，尚缺真实response/Cov | 暂不晋升实验结论 |


## 额外准备条件的falsifier：只约束二阶矩的符号

这一层见上述结果后才设计，另冻合同；所有source数值/区间和原LP容差不变。它检验一个额外而未被本run测得的条件：

`⟨m²⟩≤J(J+1)/3=47.9166667`。

这只是beam轴布居不偏向过大的|m|的条件，弱于指定Gaussian宽度，但强于任意正q。不能因fusion反应名称就宣称源已经验证它。对该spin-path，pureM1的二阶系数严格为

`u2=Σ q_i[3m_i²−J(J+1)]/[2J(2J−1)]`，

已与每个kernelvertex一致到约1.4×10^-15；故该条件给u2≤0。观测a2<0要求M1/E2的`F(δ)>0`。独立CG/6j给`F22/F11=13/35`、`(F12/F11)²=63/5`；只核幅度比大小，不据此指定另一来源的phase。用本note既定native号：

`F=1−2√(63/5)δ+(13/35)δ²`，

`G=3/2+√(63/5)δ+(39/70)δ²`，

`P90=[a2 G/F+(5/8)a4]/[1−a2/2+(3/8)a4]`。

在整个F>0域，`G/F≥rmin=−60/107+21√13/214≈−.2069318842`。这不只来自扫描：存在正数

`A=(819−39√13)/1070>0`，

使`G−rmin F=A(δ+√455/13)²`，因此是全实δ的代数必要界。对原marginalbox四个角求这一线性分式的最大值，得到

`P90(M1/E2 | 额外low-|m|条件) ≤ .04364157466 < .16`。

所以在这一个附加条件下，sameParityM1/E2无法进入所设sourcebox；pureE1仍有严格正q/lowm witness（a2≈−.15、a4≈0、P≈.20930）。先前centralM1/E2 strictq的⟨m²⟩≈75.8489，违反这个新条件；原witness继续保留。

[额外条件程序](../../system/scripts/day16_rh99_lowm_bound.py)最终actualexit0；首个actual0源码/结果保留，随后补显式正平方证书和kernel-coefficient逐项对照，未改source输入。全域解析界另以100001点sanitycheck。

这给一个具体companion：能否独立证明同一发射态、同trigger/gate/feeding定义的u2符号？同母态且多极性已知的reference branch，或经实际数据验证的reaction/feeding取向模型，才可能提供它。当前未取得这项matching输入，记expected-but-not-established；其它核素校准线的alignment不是这个量。

认识更新为：任意正布居保留两EMfamily，额外一个取向二阶矩条件可使相同box具有判别力。该条件未取得实验支撑前，不能把此数学排除写成99Rh的新宇称或作者证据已经闭合。


## 实际同母态参考审计

[[nndc-2017-99rh-matched-reference-records]] N099-2–9确认3710.6同母态六支，不含现成pureE2支路；MR空/理论CC不提供pure或u2。N099-13给实际561.3(ΔJ0)/820.4(ΔJ1)条件设计：同density pureD0的a2=−44a2(D1)/25；保证F2不翻号的充分|δ|界分别.86021/.141913。前者更耐混合但RI弱，实际AD/纯度/门/response仍缺，未把额外lowm条件升为已测。


## 额外取向条件的物理支持仍有前提

[[unobserved-feeding-alignment-sign]]把lowm条件继续拆到入口和完整未观测feeding。所证Ji/Jf≥5/2、L1/2保号域与Rh99两条已列spin路径可支持条件设计，但未知蒸发j/全链、方向选择和环境不允许宣布P00实际u2已知；方向门可从isotropicparent产生正u2。原freeq多解与额外lowm条件层级保持。

原U定义与迁移限制另回[[cejnar-1996-spin-deorientation-alpha-2n-gamma]] C96-D16-1/2/4/5；source模型与本核实际反应证据分开。
