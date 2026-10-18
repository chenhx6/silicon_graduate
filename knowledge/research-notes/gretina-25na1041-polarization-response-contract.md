---
type: research-note
title: "25Na1041：混合比分支与GRETINA偏振响应合同"
aliases: [25Na 1041 mixing branches, GRETINA Q convention audit]
created: 2026-10-18
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [longfellow-2026-gretina-energy-ordering-polarization, morse-2022-gretina-polarization-sensitivity, lauritsen-2025-gamma-angular-formalism-tracking-arrays, nndc-2025-a25-mixing-reference-records, ucgretina-2021-polarized-emission-code, ucgretina-2012-eu152-public-calibration-data]
created_from: Day16 independent daily-learning run with uncredited Day17 preview
promotion_target: compton-polarimetry
tags: [mixing-ratio, polarization, GRETINA, response-calibration, phase-convention]
---

# 25Na1041：同号偏振如何参与分支判别

## Research Trigger

Day16的DCO多解需要matching偏振companion；本note追踪一个真实AD/偏振双支案例的Q、reference与phase合同。它是有来源的暂定分析，不是新source evidence或新增课程学分。

## Grounded Evidence

### 实验对象与原作者的两个候选

[[longfellow-2026-gretina-energy-ordering-polarization]] L26-17/18给18O(55MeV)+9Be fusion-evaporation、FMA species selection下的25Na1041-keV、9/2+→9/2+跃迁。阵列为12quads、47个working crystals、无addback；最高deposit为first、第二高为second。Fig.1给25Na β=.046，polarimetry要求至少两点且sum位于Doppler-corrected photopeak。

这是angular-distribution/Compton数据，**没有该文R_DCO测量或γγ reference gate**。paper未给本任务可用的target Ei/Ef细表；本run随后取得官方对象，补得下述版本限定的level identity，未从1041与spin label猜值。无偏振source归一用56Co/152Eu近能量线；它与Q的外部标定角色不同。

### 官方对象补齐的身份与reference版本

[[nndc-2025-a25-mixing-reference-records]] N25-1–10给当前/旧对象的直接核验：Na2025 Adopted1041.3(.4)连3459.4(.7)(9/2+)→2418.3(.7)(9/2+)；2015FSU对象为3458.6(.8)→2418.5(.8)、1041(1)，XUNDL为3459→2419、1041。各自原值/括号保留，不强配能量闭合。旧FSU为35MeV反应与不同阵列，评价A2=+.28(.09)不直接替代55MeV的a2=.20(.02)。XUNDL把L26同采集编为unevaluated记录，未增加独立实验。

| Mg reference | 2009官方MR，经δRB=−δKS转换 | L26 Table1已用δRB | 2025当前MR | 本run结论 |
| --- | --- | --- | --- | --- |
| 1612 | +.189(.012) | +.189(.012) | −.207(.013) | 旧引用逐项闭合；当前更新不是新测量 |
| 1793 | +.13(.03) | +.13(.03) | −.13(.02) | 当前误差不能由简单独立平均完整重现 |
| 3970 | +.02(.03) | +.02(.03) | −.02(.03) | field MR(F)追到Kean1972，非默认Butler1975 |

NaXUNDL的δ0.0(.2)在comment，numeric MR仍空；POL=.043(.008)是L26 A0，非P。官方PDF把靶厚度排为1.152µg/cm²，primary为1.152mg/cm²，保留千倍单位转录差异。MgXUNDL gamma3971与当前Adopted3970.3不能按nearest-keV同值替换。上述校对提高数据身份可追踪性，没有补到actualjointCov、response或另一支prediction误差，也不独立选δ支。

| 层次 | source实际报告 | 当前解释边界 |
| --- | --- | --- |
| AD直接fit | a2=.20(.02)、a4=.00(.04) | fit Cov及原角谱/response未给 |
| 作者允许的AD候选 | δRB约0与−.85 | δ是dimensionless amplitude ratio，不是arctan角度；另一支sigma未完整列出 |
| ξ fit | A0=.043(.008) | 使用N(1−A0 cos2ξ)；与AD有共享事件/归一 |
| 采用response/布居的prediction | δ0给+.021(.007)，−.85给+.002 | 第二支未单列误差，不能做独立z test |
| 作者解释 | 偏好δ≈0；更改sigma或Q会改prediction | 这是adopted response条件下的选择，未由本run重拟合 |

**两支预测A0同为正。** 符号没有独自选支，作者使用的是幅度及既定response/布居。这里不将δ0当纯E2；该行的lower/upper是M1/E2，δ0对应M1。Table1另三条pure E2的“δ0”属于另一multipole对象。

### 上游Q为什么仍需独立核查

[[morse-2022-gretina-polarization-sensitivity]] M22-2/4/5/8/9实际使用6quads/24crystals、24Mg(p,p′)2.45MeV、tracking/20°clustering。它采用同一A0=Q Pbar/2约定，报告1368处Q=.196(.002)。但.131/3.25×10^-4的整条能量曲线来自同一position tuning后的**模拟GRETA**500/1000/1500/2000-keV四点，不是当前12-quad energy-order模式的多能实测校准；L26的2419/3970等还在该模拟范围外。

σ100≈7mm是选择的post-processing参数。作者明确不把它称实测分辨率；调至ξ不对称度接近数据时，simulated AD推得的P90约.85，实验约1.00，仍有companion不闭合。这个实际反证限制“已匹配一项A0就等于完整response复现”。

[[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] L25-30另用60Co1173 coincidence来polarize1333，measured/ideal amplitudes .016/.048给Q=.33(.04)。它的reference、polar angles、ξ normalization和ideal-curve定义与无γγ条件的source singles/beam reaction plane不同；.33无法直接替.196。

L26的AD、ξ和不同拟合处理属于同一fusion acquisition；不同核素/图表不增加独立实验。Morse是另一反应/配置，但它的fit、tuning和GRETA曲线共享输入。L25 source events是否部分与其它calibration采集共享未认证，不按paper数量计独立验证。

### 公开Stokes内核的可运行边界

[[ucgretina-2021-polarized-emission-code]] UC21-1–9取得与Morse README显式关联的公开实现，2021与2026的ITDecay相同；没有认证exact论文producer。固定core抽取执行暴露mixed k0/pureM1高rank的0/0×F，而强度norm仍正。独立photontrace物理有限，Morse2→0 pureE2则通过；因此不能把这个代码边界外推成原实验错误。

具体F_G4与R_RB系数核验要求delta_native=−delta_RB；本note的RB0/−.85在代码应送native0/+.85。本run初次Na benchmark命名曾混用坐标，原输入/结果保留，canonical采用更正后v2。固定Gaussianσ/J=.56的独立trace在θ90°给P1≈.340288/.017054，两支仍同号；这些是条件理论值，不能替换实测A0=.043(.008)、恢复Q或重做联合CI。正确phase、finite/PSD/强度及纯极限是阵列响应重放前的必要条件。

## Assumptions

数值复算明确使用源Racah/B/Gaussian与Qlambda≈1；positive-density与Fisher公式各有单独声明的ideal-response/knownQ/statistical条件。原event/response/Cov、另一支sigma和作者Pi intent未被补齐。quoted margins只作字面边界，不赋联合置信度。

## Provisional Reasoning

### 先固定符号、角色与归一

| 符号/对象 | 本案例合同 | 常见混淆 |
| --- | --- | --- |
| δRB | L26 Eq.(3)/(4)的emission multipole amplitude ratio，lower/upper显式给出 | 图7称mixing angle但横轴δ值不能按degree/radian解释 |
| δD96 native | 本run相同single-emitter state order/Jones轴下为−δRB | first/last cascade角色不能只抄一个换号 |
| Π/电磁sign | Morse pure式写photon parity；L25另用Electric +/Magnetic −；L26须连同upper order与(−1)^Lupper解释 | 不能因同写Π就跨pure/mixed式固定同一数值；本run工作桥不等于认证作者intent |
| Qlambda | finite solid-angle attenuation | 不是Compton Q(E) |
| A0与Q | L26/Morse：A0=Q Pbar/2 | 另用A0=Qnew Pbar时必须Qnew=Q/2，不能固定Q删半因子 |
| θlab | incident γ相对beam的角 | 不等于Compton polar angle |
| ψ（Morse/L26） | first scatter的Compton polar angle | D96/Jones kernel中ψ还可能是linear-analyser axis；要带角色 |
| ξ | reaction plane与Compton plane的azimuth | 换first-point会改reaction plane/Doppler方向 |
| Ft与F | tracking quality与polarimeter Q²epsilon | 两者数值/单位/优化目标不同 |

源Racah coefficients与显式photon trace在声明桥下mixed/pure AD与P一致到3.89×10^-16；错误同号混用可差1.5336但pure端点仍通过。此为两种数学实现的检查，不是独立实验。


### 一般tensor续核的保留边界

UC21-10–13补了有限CG乘积设计、同tensor角采样/归一的dκ0与d0κ区别，以及literalpureM1/evenκ控制的U反号。一般PSD案例是声明的数学压力测试；Morse实际κ0/pureE2控制仍通过，不用general失败改写其标定实验。不能把只消除NaN称为完整response修复，也不能把新的点Compton K比当实际Q或1041偏振。原实验two-branch inference仍等待matching jointresponse/Cov，所有新推断保持provisional。


UC21-14–16后来从同一Jones/fullq合同构造另名finite IQUV，540点及12新PSD态验证已过；前述初始general未闭合与literal失败保持不变。这改善了光子域模型readiness，不提供1041实验response、Q或jointCov，不能据此宣称δ0支被本run重新拟合选中。

## Failure Conditions

### 三项真实失败或表示边界

L26-19：p7的positive E1+M2、ΔJ0例句与Table3 negative相反。按其Fig.7 spin path、sigma/J=.3，δ0时M1/E2的P90=.726274，E1/M2为−.726274；正号对照应带完整spin/multipole/Π条件。旧L26-15保留但不再单独作物理规则；新分析没有human review。

L26-26：A2=0时，Eq.(11)的(A2prime/A2)a2字面0/0，一致模型中的A2prime B2 Q2却可有限。9/2→9/2、sigma/J=.3、δRB=.57787494给a2=0/P90=.43201160。相反，纯2→0且只布居m0时θ90没有光子，P90物理上undefined，不能用同一“消0/0”手法制造观测。

M22-10：在声明ideal-response/轴对称pureE2模型中，印刷a2/a4给grouped p=(.5233,.4776,−.0009)、P90=1.003776。它不是负核布居的实测；pabs2=0与literal两marginal误差盒有p0区间[.5211,.5246]相容。真实fit/response Cov缺失，不由误差盒造jointCI或夹掉原P。


### 实际publicsource数据没有填平1041的response缺口

[[ucgretina-2012-eu152-public-calibration-data]] UE12-1–11核到NSCL2012七quad的实际源/背景能谱及conditional共同归一Cov。它们确为可访问实验processedhist，却只有energy/labdirection而无当前Comptonξ/rawpoints，array/时间/source/selection也不同。新数据不能裸给1041的Q/feeding/AD–A0 Cov；公开simulation sorting还带truth门。上游GRUT降序排序又限制了isolatedselector反例，不能由它宣判正常Morse链路偏差。

## Transfer Conditions

迁移前须匹配nuclear transition/spin/multipole、gamma/gate角色、反应平面、能量frame、theta/psi/point选择、source归一与Q定义；当前表格不足以认证这些条件全部成立。

### 从真实cut表得到的设计信息

M22-6/11的Ft≤.1将Q从.196提高至.314，但中央F降为baseline的.25；F/Q²反推的efficiency仅余.0974。ψ60–80°的相应比例为.3922和.2113。它说明在同一pipeline内，较高Q未抵消丢失的效率；没有Q–F Cov，不另报epsilon误差。

若仅声明uniform reference、无background、knownQ的连续模型p(ξ|P)=[1−κQP cos2ξ]/(2π)，则P=0的Fisher information/yield为κ²Q²epsilon/2。κ=.5、Q=.196与κ=1、Qnew=.098给同一observable及同一information；单看Q²epsilon会因归一转换改变四倍。这是统计定义检查，不是本实验实际精度/束流时间测量。

对单Compton后photoabsorption的two-hit full-energy事件，大deposit为真first当且仅当cosψ<1−511/Elab；E≤255.5keV时不可能。这里必须用detector-frame incident energy；L26的β和quad center只提供条件设计例，不提供真实hit-order率。≥3hit、pair-production等不同拓扑需实际response。两点与target组成的unoriented Compton plane换序不变；beam×first-point的reaction plane一般会变，ξ和Doppler角不能假定不变。

## Competing Explanations

作者的delta0偏好与另一AD分支必须连同sigma/Q条件保存；response迁移、alignment或背景处理改变预测的可能性未由本run裁决。Morse smearing匹配一项A0但不匹配P90，不据此指定唯一失效原因。

## Falsification or Reverse Tests

错误同号delta桥、Q=0/isotropy、A2zero与零intensity、pure/mixed EM sign及cut损失均是明确反向控制。真正新增matching response/Cov或独立reference可检验选支；重复同数据处理或调Q到目标根不能充当该检验。

## Open Questions

### 当前可建立与不能建立的内容

`supports`原作者在adopted response下的δ0偏好；`limits`符号单独选支、裸Q迁移及same-data回代认证。所需下一输入是matching θ/ψ/point-multiplicity/energy cuts的joint response、AD–A0与a/Q Cov、峰/背景/source ledger及另一支实际sigma/producer。未发送作者请求，不把缺口自动转给用户。

当前是L2理论/表格复算与L3 source/readiness audit；实验L4 refit仍not-ready。正式课程只计Day16一次，此案例仍是partial17知识预习。

## Human Review

本note保持unreviewed/provisional。原source的旧human-review事件和flags完整保留；新增自审claims为needs_review，不把本分析表述为人工审阅。当前没有要求用户立即裁决。

## Promotion or Rejection History

2026-10-18：依据实际primary、冻结输入与代码建立provisional ledger；尚未晋升或拒绝整个推理。可复用定义已回链方法页，实验delta/response问题仍保留。

## Reproducibility

[L26冻结8行](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-primary-input.json)、[M22冻结标定/四cut/模型](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/morse2022-calibration-input.json)、[事前约定](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/gretina-replay-contract.json)、[程序](../../system/scripts/day16_gretina_convention_audit.py)、[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/gretina-convention-audit.json)。SymPy1.14/mpmath1.3只在repo tmp，按既有PYTHONPATH重放。首尝试的symbolic vector `==` guard未先simplify而exit1；仅修algebraic guard后exit0，原inputs/helpers不变。


## 22Ne图形平均的续核：不能替1041补响应

L26-27–29从同paper原Fig4取实际vector黑C/红P，得到sourcecoverage均值约.377923/.543870，正文about.35/.53保持未闭合；不是rawevent重放或作者错误归因。该C来自1238-keV56Co、用于22Ne1275案例，不能未验证energy/points/角门就迁给1041。

sourcecoverage与event-weighted平均在声明kernel下不同；Q作为A/(κPbar)的经验校准量也随平均定义改变。保持旧Q、只改target平均来强配A0不是独立标定。真实kernel需joint θ/ψ/ξ、multiplicity和source/背景选择；已有0/−.85两分支的误差/response缺口仍保持。图示cut保留比例不是polarimetry实际count ratio，不把更漂亮ξ振幅直接当更优统计设计。
