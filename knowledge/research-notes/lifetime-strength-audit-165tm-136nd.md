---
type: research-note
title: "寿命到强度与Qt：165Tm/136Nd的提取和几何审计"
aliases: [lifetime-strength-audit, 165Tm 136Nd lifetime strength audit]
created: 2026-10-19
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day17-uncredited-Day18-preview
evidence_sources: [jensen-2001-165tm-h9-2-configuration, mukhopadhyay-2008-136nd-transition-rates, lange-kumar-hamilton-1982-multipole-admixtures]
promotion_target: ""
tags: [DSAM, lifetime, transition-strength, quadrupole-moment, geometry, feeding]
---

# lifetime-strength-audit：从谱形到Qt必须保存的合同

当前入口：2026-10-20独立Day18 session在新primed回忆冻结后定向原读Jensen、完整原读MU08六页，并完成新的“Day18停止时钟与带间contrast”分析（末节）。前面和其它Day17段落保留原无学分预习历史；它们的“本session”不改写为本次新证据。课程信用只由本次日报/回执的逐卡验收决定。

## Research Trigger

Day17的P/A/Q课题已显示，响应校准与核物理量不能按同名符号合并。本页预习恰好下一Day18的DSAM卡，把同样的分层原则用于τ→B(Eλ)→Qt；只保存知识，不授Day18信用。

[[jensen-2001-165tm-h9-2-configuration]] J01-6–10与[[mukhopadhyay-2008-136nd-transition-rates]] MU08-15–17来自本session重新原读/定向核验。旧摄入、Day9的branch/ICC练习与本次重复原读有priming，不是独立实验或盲测。

## Grounded Evidence

| 层 | 165Tm：Jensen2001 | 136Nd：Mukhopadhyay2008 | 证据层/locator |
| --- | --- | --- | --- |
| 原始观测 | Au/Pb两backing、四角gated能谱；Fig7 | 两角组/合并rings的double-gated谱；Fig2 | 已发表直方图，不是本任务取得events/fitbins；J01-6/8，MU08-15/16 |
| 门与feeding | 统计不足，不能abovegate；below门，三步同Qs且J(2)=65 | 所有门below；movinggate每ring含完整shifted+stopped尾；五步effectivefeeding | 模型/selection；不能宣称sidefeeding已消；J01-6/7，MU08-15/16 |
| slowing与τfit | empirical电子stop+shell修正、核Lindhardt、5fs、Bateman+least-squares | SRIM、5000 histories、2fs、逐级再global lifetimefit | 条件拟合，非无模型直接寿命；J01-7，MU08-16 |
| stopping误差 | 文句称additional5%已加tableuncertainties；未给Σ | quoted errors明确不含最高约15%stopping，Fig4称statisticalonly | 不同预算/概率口径，不可跨文拼成统一1σ；J01-8，MU08-5 |
| B/Qt换算 | Table2给τ/Qt；rigidrotormodel，Table6另两band靠mixing标尺 | TableII给τ、B、Qt；pureM1是ΔI1提取假设，未印Qt几何公式 | 同链派生，不能计成独立companion；J01-9/10，MU08-11/17 |
| 结构判断 | larger[541]Qt支持corepolarization；CSM仍欠完整crossingdelay | 两bandtransitionrates不同限制早期idealchiralpair；TAC/RPA解释不同configuration/mixing | 作者解释/模型与谱图层分列；J01-4，MU08-2/3 |

Jensen的Qs是effective **side-feeding** transition moment，不是静态spectroscopic quadrupole moment，也不是Compton polarimeter Q。Qt是带内换算量；不能按相似符号迁移。

## Assumptions

新数值均在明确的photonfraction/ICC、纯E2、meanτ和候选G条件下计算；near-decimalbox只是假设的中心打印精度。没有actualevents、原fitΣ或historicalproducer，因而不将表值复算当实验重测、实际误差复现或唯一几何识别。

## Provisional Reasoning

### τ到B的逐项合同

令τ为**总平均寿命**，λ_tot=1/τ；pγ,j为每次leveldecay的绝对光子概率，fXL,j为该光子中指定multipole的率份额，则

\[
\lambda_{\gamma,XL,j}=\frac{p_{\gamma,j}f_{XL,j}}{\tau},\qquad
B(E2)_j=\frac{C_{E2}\,p_{\gamma,j}f_{E2,j}}{\tau(\mathrm{ps})E_j(\mathrm{MeV})^5},\quad C_{E2}\simeq0.0816202120.
\]

B单位e²b²；C是[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1的Eq2.2按现代单位重构，**不是原文直接打印的数值**。若给的是完整totalbranch b_j且普通IC库存成立，pγ,j=b_j/(1+α_j)；若只是相对photonintensity，必须先建所有支路与非γ库存。不能将levelτ当partialτγ、把T1/2直接当meanτ，或因表中branch和1就认证完整库存。

对同一M1/E2光子，fE2=δ²/(1+δ²)，但rate不含δ相对符号。δ/ICC/branch来自同一输入时保持Cov；不能把mixedfraction和mixedICC独立重复计误差。此处沿用既有MU08库存边界，不重算旧757.4支或恢复其actualΣ。

### B到Qt要另给几何

声明一套rotationalgeometry G时，

\[
B(E2)=\frac5{16\pi}Q_t^2G,\qquad
Q_t=\sqrt{\frac{16\pi B(E2)}{5G}}.
\]

固定K轴向模型用G_K=|〈I K;2 0|I−2 K〉|²，需要K与模型条件。另一个**候选**stretched-axis投影用

\[
G_s=|\langle I,I;2,-2|I-2,I-2\rangle|^2=\frac{2I-3}{2I+1}.
\]

后者的初末投影随I变化，不是把同一个固定intrinsicK设为I；不可混叫K=0/axialrotor的同一几何。

### 真实印刷表的新定量练习

[新输入合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/day18-lifetime-strength-contract.json)、[新程序](../../system/scripts/day17_day18_lifetime_strength_audit.py)、[实际结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/day18-lifetime-strength-result.json)保存全部11行Jensen Table2与9行MU08非空B/Qt，不引用旧scriptcheck数。

| 原表项 | 本页声明条件 | 新算术结果 | 原打印/边界 |
| --- | --- | --- | --- |
| 165Tm[541]33/2→29/2，618.3keV，τ=.27ps | photonfraction1、ICC0、pureE2、fixedK1/2 | λγ=3.70370×10¹²s⁻¹；B≈3.34532e²b²；Qt≈9.77587eb | sourceQt9.8；条件相合不认证全branch/ICC |
| 165Tm[541]45/2→41/2，741.9keV，τ=.15ps | 同上 | Qt≈8.24354eb | source8.1；是11行最大centralrelative差约1.772%，不调α消差 |
| 136NdBand1 I16，B=.26 | candidateG_s=29/33 | Qt≈1.72462eb | source1.73；fixedK0却约2.72536eb |
| 136NdBand2 I15，B=.54 | candidateG_s=27/31 | Qt≈2.49658eb | source2.50；fixedK0约3.93615eb |

Jensen11行在**另加**nearest.1keV/.01ps/.1eb中心打印box时都有交集；MU08九行在**另加**nearest.01B/.01Qt时也都有candidate交集。这只检查条件算术与打印精度，不是实验CI、原fit误差复现或证明作者实际用了该candidate。没有从Qt反推ICC/branch/K，不能把匹配升为已知historicalproducer。

## Competing Explanations

- 改stoppingtime/速度谱可改变拟合τ；增加feedingdelay也可改变谱形。belowgate保留这类退化，fulltailgate只针对截掉快分量的selectionbias。
- 较大Qt可来自较大E2矩，但Qt→β/γ解释仍依赖rotor/轴/混合。几何选择本身可令同一B的数值差约1.58倍，不能据跨论文Qt差直接判形变不同。
- 165Tm另两带Qt由mixing比值乘DSAM标尺，136Nd各列B/Qt由同τ/branch派生；这些并列量不能互作独立验证。
- 136Nd作者明确bandmixing未加入TAC计算，RPA在chiralvibrational域且某configuration强度fragmentation；近简并/模型minimum不替actualrates。

## Transfer Conditions

同一level/transition身份、总meanτ、绝对photon/totalbranch定义、multipolefraction/ICC库存、几何与单位闭合后才可迁用换算。165Tm与136Nd的stopping/feeding参数和几何数值不可互借；新Q_s、Q_t与Day17 polarimeterQ分开。

## Failure Conditions

未观测支路、门截tail、contaminant/response、unknownfeeding、Kmixing/带混合或非轴旋转可使当前简化链失效。若5%/15%的作用范围与Cov未给，不将其当独立Gaussianσ，亦不据共用backing就说ratio完全抵消。

## Falsification or Reverse Tests

获得abovegate或独立feeding约束、换backing/束能/同transition各角拟合以及stopping替代模型，是检查τ敏感性的高信息路线；需实际谱与response重拟。若一个声称通用的Qt公式不能同时明确两文的G/轴/branch，先查合同，不通过自由调normalizer强配原表。

## Evidence Gaps

原events/角门能谱bins、slowinghistories/代码、完整branch/ICC与实际Kmixedmatrixelements、jointfitΣ及stopping/feeding概率模型未取得。公开图和表支持L2/L3提取审计，不能凭它们造新L4τ/B/Qt实验CI。

## Open Questions

MU08原Qt公式/轴的直接出处或实际code仍待新原件/producer；candidate匹配不唯一。Jensen的5%具体在各输出/weightedaverage中如何相关也未给。若取得历史input，再决定哪项系统误差影响跨带结论；本页不反解不存在的Σ。

## Reproducibility

[primed回忆冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/day18-preview-recall-freeze.json)先于本session打开两source/raw；[identity/hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/day18-preview-original-identity.json)、[actualreadscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/day18-preview-reading-scope.json)与Crossref验证单独保存。MU08六页主线完整原读；Jensen仅本次DSAM/必要context定向核，不声明重新48页fullread；LKH82仅PDF3公式/图像复核。

运行`PYTHONPATH=/workspace/wiki/tmp/day16-jt74/python-deps python3 system/scripts/day17_day18_lifetime_strength_audit.py --contract outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/day18-lifetime-strength-contract.json --output tmp/day18-strength-audit-replay.json`。原raw/hash不变，不把已有source深读状态改成新信用。

## 31S的Bayesian方法companion：model扣除仍需分层

[[sun-2023-bayesian-dsam-31s]] SUN23-6–13为本preview新增实际primary：restrictivepriors/GP/Gaussianlikelihood与16/50/84quantile、90th上限合同都可原件核，而actualSI/paperproducer/训练input仍缺。其αtransfer门不是165Tm/136Nd的belowγgate；不可裸搬模型。

1248态的τ=1.120(.180)ps用于M1提取时，作者另用USDB E2partialτ=6.9ps作rate扣除：τM1=t e/(e−t)≈1.33702ps，固定model时local尺度≈.25652ps，现代单位/roundedE给B(M1)≈.021883µN²、RME≈.295858µN。原作者称experimentalB，但这里含modelE2条件（central约16.232%totalrate）；模型σ/Cov未给，不称completeCI。源6390的20fs仅条件width单位转换≈32.9106meV，不升级为reported90%limit。新[合同/结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sun2023-rate-result.json)不造实验后验。

## Human Review

原J01与MU08所有claimflags保持；新claims均needs_review，未设置human-reviewed。研究边界由Codex自审追踪，不自动变成用户待办。

## Knowledge Impact and Learning Decision

`supports`两文各自的提取链；`revises`默认同Qt一定同几何、Qs一定静态矩、fulltailgate等于消feeding的习惯；`limits`表中中心值闭合、重复测量/换算及误差百分数对模式判断的保证。量化结果是条件重构，与source实验事实/作者解释/模型分别保存。

## Promotion or Rejection History

2026-10-19 Day17内无学分Day18知识preview建立；L2表/单位/CG控制完成，L3输入/反证矩阵已写回，L4原始谱重拟未ready。不给Day18正式学分、不将next_day_index越18、不打开Day19；formalDay18仍需其独立run逐卡审计。

公开方法软件companion [[madai-2015-distribution-sampling-likelihood]] MDA15-3/4/6保存一项新nativecontrol：variableCov可令缺normalizer的quadratic排序反转，fixedCov不受该常数影响，ordinarycustomloglike不自动覆盖MH下一API。此处只L2/L3合同，非三核素原data重拟/CI或实验归因。

## 15O的实验反证：finite转limit要查校准和模型

[[schuermann-2008-15o-6792-dsam]] SCH08-5/7/8/9/10以新实际primary补充：单Ge/密角/共geometry与primaryF约束把6792/6172推到fullshiftcompatible，而旧数据点仍非矛盾。P.987是finite-detectorDoppler，不能按字母当physicalpolarization。5181与旧评价相合是必要companion，TableII再算旧F则非新测量；1σlimit/Γ条件链不升级90%CI。

新F分母映射和reportedscalarcontrast是[[schuermann-2008-15o-6792-dsam]] SCH08-11–13的条件exercise，未得actualcentroids/Σ/SRIMpoly所以不造lifetimefit。与Sun的GP/posterior或165Tm/136Nd的feeding假设只按方法边界比较，不转其数值。

## 165Tm主线再核：组态混合不是光子δ，四Qt不是四份寿命

[[jensen-2001-165tm-h9-2-configuration]] J01-11–18补完本session48页主线、19图/8表角色与Eq1–9；密表只selectedrows核算不冒全inventory重建。原Table5/6和Sec5–6显示绝对DSAM两个标尺怎样进入另外两band，同时有明确modelconditions。

令A=Q541=8.3、B=Q411=7.4、rplus=Q404/Q411=.96、rminus=Q541/Q523=1.16，则输出为Q=(A,B,rplus B,A/rminus)=(8.3,7.4,7.104,7.15517)eb，与source四舍五入7.1/7.2分列。第三/四个值不是新独立lifetime；positivepair在Table5还明确固定Q411=7.4。用一个完整primitiveΣ经Jacobian传播，而非给每输出各自添独立DSAM标尺误差。即使另让四primitive独立，Cov(B,rplusB)=rplusVar(B)、Cov(A,A/rminus)=Var(A)/rminus仍非0。Q523/Q541=1/rminus，A与其crossCov精确取消；原stop/feeding若还影响rminus则不能取消。声明primitiveSD=(.5,.5,.05,.09)仅作局部设计，得到ratio尺度.0668847；原Table6.87(.10)保持，不从不匹配反推真实Σ/判作者错，不重复加已经在原Table2提及的5%。

本session[新合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/jensen-bandmixing-contract.json)/[程序](../../system/scripts/day17_jensen_bandmixing_reference_chain.py)/[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/jensen-bandmixing-result.json)沿原negativepair的Eq4/5，用Table1实际37.25/.80及branchratio/CG(3/7)给α²≈.0166274、β²≈.9833726、|V|≈1.764615keV、Q541/Q523≈1.164763。源α/β是configurationamplitudes，原photonδ是不同对象；sinθ的principalasin14.818°不是由原rate选的165.182°分支，不能不看branchroles就取主值。强度只给当前basis下平方/|V|，不测signedinteraction。原possibly50%Ω3/2混合贡献ratio误差未有完整合同，未恢复其CI。

Table5六个**源模型**eigenpair给|ab(Ecalc404−Ecalc411)|≈4.97keV，符合sourceV5.0的额外nearestdecimalbox，norm必要检查也过；它不替原VMI/branchfit的GOF或uncertainty。positivepair要求跨spinQ411近constant，作者用modelQt频段变化通常<.2eb支持，而非另有逐低spin测量；转移到别的体系/转轴不能自动用同数值。

实际counterinput：N96时Table7 modelTm/Er/Yb crossing255/225/217keV，对应Table3/8 observed355/281/269。Tm的100keV总残差包含evenbaseline问题；中心double-difference分别44/48keV不是新pninteraction实测或精确误差排除。作者还核crossinggain，但Tm>5.3只lowerlimit不可当5.3点；deformation/pairing/Coriolis与pn解释必须共同面对数据。

Fig19的absoluteB(E1)也取同Table6 Qt、λ和mixing修正，故不是独立验证DSAMQt的绝对companion；octupolecoupling只是examples未fit，spin/signature残差与b单位字面边界保持。需要独立lifetime/feeding/stopping/原modelinput才会提高绝对shape裁决信息，重复当下代数不会补它。

## 31S的有源MRcompanion与原双根

[[nndc-2022-s31-mixing-lifetime-reference]] S31-2–10实际核2022Adopted/旧reaction两对象：1248MR+.35(.02)来自1970Moss，另+5.3(.4)根仍在comment，小根偏好用了RUL；1971DSAM的T1/2.50(.12)ps与meanτ720(180)fs为同测量/不同字段。不能将两个evaluation或单位表示重复计权。

固定Sun总mean1.12ps作γ-only诊断时smallMR给τM1=1.2572ps、BM1≈.0232725，USDBτE2=6.9ps则给τM1≈1.33702、BM1≈.021883；后一输入的rate-equivalent|δ|≈.440195不是新测MR。原largealternate也保存条件rate，不用newτ/RUL再选根。primaryphase/fit与modelσ/actualbranchCov缺，不能把差/.02当显著性或把本重算叫新experimentalCI。

S31-11另把2010Do03两detector的quotedstat/sys半衰期预算与Sunmeanτ转引做条件单位核；同paper/不同detector不自动独立，quadrature只是额外算术假设，不从summary重建旧jointΣ或physical-limitCI。


## 实验停止本领的覆盖审计

新增[[iaea-2026-stopping-s-au-o-ta-records]] ISP26-1–9，以真实S/Au39行和O/Ta24行及模型角色表替代“已有数据库就能校准sp”的笼统假设。S/Au32S低能Wr1979仅两点，Fs1976与Wr1979作者部分重叠；独立实验/共同尺度仍需primary核查。O/Ta稳定同位素最低能区与15O低能capture recoil有大缺口，不能补Schürmann原15N surrogate。电子阻止和v(t)cosψ合同不同，也不把现今SRIM2013当Sun的Geant4或SchürmannSRIM2006。

实际CSV哈希/原行/单位、同位素匹配插值比、literalerror与修正记录均持久化于source和run artifact。Wr低点.58MeV/(mg/cm²)对应189.701×10⁻¹⁵eV cm²/atom；比值只描述既有数据相对模型，不作新独立验证/fit或τCI。这一节是Day18无学分知识预习，正式17仍只一次，不开19。


### Bt1966 primary补充：比值之前先识别计量

[[bethge-1966-heavy-ion-stopping-charge-states]] B66-1–10已原读五页/六图/四式。其25%误差有具体beam-charge系统背景，direct与charge-derived有共用装置/理论输入，S线也不是独立Northcliffe预测。Seff局部权重、N0共同尺度及电荷二阶矩推导可复核，但原Fig3到IAEA16行归一/符号/核扣除桥仍partial；不把.962–1.928模型比值叫实验矛盾。Bister15N/Ta原件仍缺，当前route不补它，也不产生新τ/CI。


### 从stopping模型名称到actual组件输入

[[geant4-2026-ion-stopping-component-contract]] GSI26-1–10核公开callpath与已存在SDK的三个声明模型组件，63编译行按实际稳定同位素查询，另31S/15O只是声明诊断。Wr低点相对三曲线差别显著，但error语义、模型训练谱系、Sun实际配置与材料仍缺；不能只按模型比值倒改实验τ或prior。

无event的API查询也有初始化/历史条件：原fixture缺RunInitialization崩溃已修；external低能首次range构建的内部charge状态变化已trace定位且保留首次/重复值，SDK未patch。它证明单个“Geant4值”须附模型/表/能量/cut/调用合同，非原实验CI错误或完整DSAM再分析。


### native前两步控制与实验影响之间的界限

GSI26-11–15的实际Geant4 native控制补API→AlongStep的必要检验：同起点external首event首步/后续event约.0959881，option4为1；.1nm短步无需range积分即可由首次transitioncache触发，两个事件各两步后人为kill。源码诊断/原生step相同、局部能量账本闭合并不等完整transport或实验response通过。没有Sun所用版本/配置、材料、全轨迹、衰变/feeding和Σ，不外推τ/CI偏差或用它替原stoppingprior。


## 31S alpha门：沉积能量到vertex的必要映射

SUN23-27–31/GSI26-16的新输入审计保留实际Si角色和原Q：E为1mmSi残余沉积，DeltaE为87µmSi；门变量的exactsorter表达式仍缺。下表仅为128MeVvertex/靶静止/sourceQ5.533/无任何损失/0–13°的声明模型，Ex与gate中心沿原打印；原两MeV门宽不是σ。单位均MeV，列出的vertex−gate差不是测得targetloss。

| Ex | printed alpha gate center | 高root vertex alpha范围 | vertex−gate |
| --- | --- | --- | --- |
| 1.248 | 49 | 51.2407–53.9719 | 2.2407–4.9719 |
| 2.234 | 47 | 49.4806–52.2116 | 2.4806–5.2116 |
| 3.076 | 46 | 47.9518–50.6840 | 1.9518–4.6840 |
| 3.435 | 45 | 47.2922–50.0254 | 2.2922–5.0254 |
| 4.971 | 42 | 44.4108–47.1521 | 2.4108–5.1521 |
| 5.156 | 42 | 44.0567–46.7995 | 2.0567–4.7995 |
| 6.390 | 39 | 41.6503–44.4063 | 2.6503–5.4063 |

所有positivephysicalroots仍保留；低root与被探测tensMeV支分开。actualSDK核质量和sourceQ分别计算，高rootQ选择差至多约.000578MeV；不以多位质量调gate。2234无损Jacobian约−.555、2MeV窗映约1.11MeVEx只是量级控制，未恢复实际beamdepthloss、posttarget/Si响应、calibrationCov或gate平均。

`supports`原约1MeVEx窗口的量级；`revises`把αgate中心直接当vertex动能或把残差拟成targetloss；`limits`当前数据对实际recoil history/τ/CI的保证。原Sunmain/SI/SDK条件算术不增加独立实验。下一应找actualgate/同设施source response来核角色，不能拿这张表宣称原实验矛盾。


## 23Mg原DSAM与SimDSAM的独立companion

[[kirsebom-2016-23mg-dsam-lifetimes]] K16-1–16完整13页/21图/2表/4式实际读。四finite/九95%upperlimit保留，7787<12fs同时允许争议的不同τ；固定Bp/J的ωγ约1.1168meV不是含输入不确定度的新joint95%界。Bp前文±.07与结论±.007/19%不一致保留，不从元数据改原测量。

该实验的alpha出靶约4MeV、He植入层swelling及有限束斑/散射，使门到vertex/响应的映射具体化：不能裸迁给Sun；density部分peak约.55944，He项仍需一起算，不将它当额外固定系统σ。Fig21理想cone乘积近恒并不消除门更宽/背景/角分布的代价。

[[simdsam-2015-public-dsam-code]] SD15-1–15给真实52文件/2015代码与原表达式组件，但defaultGEANT表/半径/插值与正文有差别，原ROOTanal/data/Σ/job未给。原native uniform-radius矩约.331814、不是uniform-area .5；原gamma/v时钟与properclock不同；报告xOutput未同步最后position修正；measuredalpha32MeV控制约31.9864而internalresidual27.9898，说明变量角色不能混。同表模型peak mix/pure约.603–.612非新测量或Sun40%误差。原源hash/失败/警告保留，未改physics或重fitτ。


## Forster输入：新的真实点限制过强的模型冲突判断

ISP26-14–17/K16-17/SD15-16核actual24Mg/Au十个Forster编译点、exactref与全库相同；0.2–3.2MeV/u/literal4%。ρ19.30把1.6MeV/u的4.37质量阻止转换为8.4341MeV/µm，支持K16 about8.5。原publicGEANT reader在1.6/2.0邻点与compiled值约2%内相容；所以defaultGEANT label与正文Forster的差别需保留为输入谱系/actualjob缺口，不能直接叫数值矛盾。

整十点compiled/GEANT约.800–1.064、compiled/PASS约.699–.903说明全能区/不同模型并非同一constant scale；未拟合/无Σ。Forster原文仍OA未得，NRC exactquery无结果，downloaderTDMlicense标签不是正文/OA取得；不从metadata补测量方法/σ或把24Mg相近速度迁到23Mg混合靶认独立校准。


## 有界原eventmain MODEL packet与readiness

SD15-17–21/K16-18给64对实际原publiceventmain输出：dsamTree/EPART/EGAMMA Float_t以keV存，ASCII另有observedangles；ROOT与ASCII仅有序列化舍入差。另新目录卡只改输出路径，ASCII流及ROOT分支逐值重复。诊断EQa GetEntries/全bins=6820proposal，默认积分5427，源info的1entry/积分15只是lifetimepayload。

这个MODEL stream是条件反应/角域/相对效率的输出，64/6820不认实验absoluteefficiency，也不补原ROOTanal/experimentalROOT/Cov。原properclock/radial/默认输入问题和libUnuran Load警告保留，52源hash未改；sourcepacket说明接口能运行，不宣称物理/原τCI通过。

K16-19另核A物性原源Alexander1981的准确DOI10.1016/0022-3115(81)90217-8及metadata，正文仍未得。题名含DSAM不能替原方法/校准寿命/共享停止数据的读取，A=.75(.25)独立性/置信语义/迁移到Sun仍是开放输入。


## 23Mg独立fractional-Doppler：新τ与adoptedωγ不能混读

[[jenkins-2004-23mg-fractional-doppler-rate]] J04-1–14四页主线/表图实际读：22MeV12C/薄C/Gammasphere采集独立于K16；七角centroid→fractionalshift→模型τ，feedingdirect为假设，原Σ/stopmodel配置不齐。τ10(3)fs与tableomega1.8(.7)meV分别是本次结果/Angulo adopted；附近新态靠不同branch gates识别，不只按energy合并。

原Q7579.6(1.4)、质量数NR因子回算九Ep中心均.05keV内；独立quadrature名义误差未完整闭合，共同Q-only的2.14223keV²外积仅为条件模型。τ10给Γtotal65.8212meV而非已测Γgamma；固定adoptedω/J/两通道可得互补Bp根.0504/.9496，展示独立branch输入的必要，不是新Bp或CI。7769的58/42两γ在3MeV理想阈值下visible.58，但实际作者4meV保守界另含yield/energy/response，无此Letter明确CL。

K16对旧Ex未校recoil的评论和J04原文说已校正同时保留，需actualenergy定义/详细文/原谱才能判；不以此改raw或ωγ。DCO约.9/1.7的gate合同、transfer/mirror/stretched条件和gamma threshold是必要companion，不替P/A/Q/δ。后续2013详细文是否同data尚未原读，不计新独立实验。

## 23Mg官方匹配：先列自旋和分支，再谈寿命换强度

[[nndc-2021-mg23-lifetime-strength-reference]] M23-1–15五对象原读确认：fusion7785.2为7/2(+)，Adopted7784.7为3/2+,5/2+且保留旧7/2意见。half6.9(2.1)fs来自J04 mean10(3)，另一<8.3half来自K16<12mean，非两次新寿命。capture支11/89和新omega5.7(+1.6,-.9)是不同年代/对象输入，原2011body/联合Σ尚未得。

条件两通道omega=g(hbar/τ)Bp(1−Bp)，固定τ10fs/omega5.7meV时J3/2中心无根、J5/2和7/2各有互补两根；对应τ上界8.248/12.372/16.497fs。无根不等spin排除，旧tau误差、新limit/omega误差/共同输入未组成联合统计模型。归一RI也不提供totaldecaybranch；其Jacobian列和零，不能把两个derivedfraction误差当独立。

M23-2/10另保留靶厚160vs40和7852/5138在2013缺失的评价注释；2013正文未取，不宣称版本/采集关系已完全闭合。此处新增的是可追溯输入/条件矩阵，不是实验τ、Jπ或率重测。

## 直接capture强度：停止功率与归一分别检查

[[sallaska-2011-na22-absolute-resonance-strength]] S11-1–20原20页/18图/6表/7式全读。uniform raster照满target与完整beam-energy积分使有限强度不必显式用absolute-stopping；代价为总NT、ρb、跨能量efficiency与扫描尾部合同。198/232weaktemplate按Cu stopping比伸缩，energyloss另用TRIM并假20%，213尾为total10(5)%；不能由摘要认所有结果独立于stopping。

213新5732branch约10.6%有same-strongshape约束，placement与J04的209不同；610的6112因F背景采用旧branch估partial。按作者允许upper单侧加法，名义partial预算能近复213/288/610总误差，454约20.903对原22保留未闭合。不是新原事件拟合/CI，也不从被排finalspin1/2补误差强配。

共同Co/efficiency可能同时进入1275活动度和高能capture：omega条件比∝η1275/ηH，需跨能量Cov；共同乘法尺度可消掉，但实际完整Cov未得，不能指控作者doublecount或重报σ。原2010PRL/erratum与2011自称同研究详细报告，不计第二次独立采集；后续若核erratum先读原件，不从标题补更正内容。

## 短报/详细文的frame与同源版本

[[sallaska-2010-na22-letter-version-contract]] S10-1–10：2010v1/v2 Eq1与TableI源码同、rateEPS同；2011四有限强度也相同，不能重复计实验。LetterlambdaLab²与详细文CM定义需r²桥；NR全窄峰数学积分给Lab系数lambdaLab²r³。质量数控制只说明相差约9.3%的定义因子，不认证原producer用了错公式，也不解释2.4–3.2倍争议。

正式Erratum105209901准确存在/9Nov2010，但body当前未得；Sepv2关联DOI不等包含Nov更正。232footnote门与旧branch配对、2011TableIII角色差异同样保留，不能猜更正内容或改raw/强度。后续高信息应是actualerratum/producer或匹配独立particlebranch，而不是更多条件模型history。

## 低能质子companion：两层分母与作者自旋解释

[[saastamoinen-2011-thesis-al23-proton-response]] SA11-1–14来自作者2011 JYX thesis定向4.2/5.3/AppendixA，期刊PRC83045808尚未取得。Table5.4低p relative.32(.06)乘I451abs43.3(1.0)%给perβ.13856%，不能放到Γp/Γtotal公式；Fig5.7同单位p/γ .32/6.63/1.53归一为Bp.0377358。固定旧τ10/J7/2/所列两通道得Γp2.484/Γγ63.337/omega1.366meV，仅中心重构，无新CI。

作者排3/2借L2势垒、排5/2借IAS/IMME混合推断；角动量允许集合仍含J3/2 L2，同spin也不强制大混合。新source不反向推唯一J；30keVFWHM对16keVdoublet仍不能排小IAS。原gamma来自Zhai2007/Iacob2006、τ来自J04，同源输入与当下measurement分列。

AppendixA明确ROOT5.22/Rebin/ShowBackground/Smooth/150keV数据匹配与Add减背景，并称errors自动传播、fit约16%；这些是待actualcode核验的工具合同，Sumw2本身不保证fullCov。真实events/原analysis/模板Cov未得，不以更多toy重造实验CI。

## 实际ROOT5.22：自动误差传播的范围收窄

[[root-2008-v522-background-error-contract]] R522-1–11读真实v5-22-00 TH1/TSpectrum调用链，另名原Smooth/Background表达式配当前ROOT6.40helpers执行。Smooth保留stored errors；Background cloneReset后非零content/零stored errors，无buffer则sqrtcontentfallback，不能当估计背景的fullCov。Add/Rebin/Scale只按给定系数合并diagonal，未含数据估计scale与跨bin相关。

声明D−(Dk/Bk)B的Jacobian使matchingbinvariance0，而固定aAdd给正variance，说明共享归一信息丢失；这个四bin设计不是原hist/原匹配实现。旧thesis16%/2%/13%保持作者结果，actualpatch/job/events/模板Σ未得，不能据API反证重报实验CI或判τ/Bp无效。下一输入需actualproducer/data或独立reference，不加更多toy填缺。

## Fougères2023：新τ不变，branch更新改变omega

[[fougeres-2023-mg23-velocity-difference-lifetime]] F23-1–20主7页/SI8页全读。GANIL独立事件级βreac−βems给新τ11(+7,−5)fs；新BRp=.68(.17)%与引用Friedman2020 .65(.08)%组合推荐.66(.07)%，tau又与旧J04组合10.2(2.6)fs。假J7/2的中心omega.24177与作者.24近闭，旧BR.037同τ量级给约1.34meV，故关键更新是分支，不能由寿命相容推强度不变。

Δβ拟合仍依赖SRIM/角与能量分辨、jointEg0与τ、finitegate/模板normalization；newbranch需pureAu背景与邻态模板约束。低χ²ndf不是coverage证明，7/2明确assume。Figshare实际XLSX显示区与SIgrid不可直接一键重算χ²，7785全显示区Pearson123.956对grid17.1982和一条零grid切片保留待核，不叫实验矛盾。

公开Zenodo v1.0.0确有34文件、409303-entry衍生TreeMaster，不再是纯readiness缺数据；原DAQ/全calibration史/原paperfit脚本/Σ仍未闭。下一实际L4路线应核本公开producer的参数传递/门/normalization与源数据匹配，保原文件hash、不要改producer冒作者结果。

## publicrelease与原paperproducer分开审计

[[evasions-2023-public-release-native-readiness]] EV23-1–14实际原source/native与publicevent核：原make先因lib输出目录缺失exit2，补目录后0；无analysispath按literalreturn1正常结束。原loader sentinel长度不回传且逗号小数解析失败仍status1；原VAMOS beta scalar也不回caller。其它停止路径/MCdepth/未绑定Si_theta/sizeofpointer/未完成fit块均原release边界，原34hash与data保留。

该release提供409303真实作者标记衍生event、7933条Si_dE>0，L4从缺data推进到actualquery；没有原DAQ/完整校准史/实际paperfit配置/Σ，不能把多项release问题累加成实验τ偏差或修源后重报CI。当前停止literalfullMCfit路线，继续最高信息独立companion或原fit定义，不以更多history补输入。

## Friedman2020：独立相对强度与共享绝对输入

[[friedman-2020-gadget-al23-proton-branch]] FR20-1–16实际完整OSTI作者稿8页/4图/2表读，newgasratio .063(.004)不同旧Si.34(.06)，但I866abs.41(.01)%和gammafeed3.95(.37)%仍来自旧source；newIβp.0257(.0017)%→daughterBR.0065(.0008)。其中新采集/旧归一/假spin/旧tau逐层分列，不从“gas新测”假所有输入独立。

两方案.066/.060共享effsys且作者称stat近独立，条件rho0/.5/1合成scale.004062/.004770/.005385，只是敏感性不重报CI。固定新branch/旧τ10/J7/2得omega.24289；τ12端点.20241不复现Table2 joint下界>.16或CL。旧thesis两γprintedsum×.433=3.53328%对本through-state3.95需原gamma源/版本，不强配。

F23推荐又复用本新branch/J04tau，故两篇≈.24不计独立强度确认。真实GADGETcounts/GEANT4setup/fullCov尚未取；后续最高信息是instrumentprimary或准确gammafeedreference，不用更多条件toy填原Σ。

## γ参考谱系：真实后续采集与绝对分母仍有边界

[[tamu-2006-2007-al23-gamma-reference-reports]] TA07-1–12核机构原三报告8页。2005sample/3.2s计数与2006Sep/Nov后续/2s计数、高能统计和24Al标定/BGO不同，后续数据不能全算旧event转载；同设施/效率知识也不自动独立。相对γ比[3.8,100,20]归一3.1/80.8/16.2%近S11旧参考，并未给absoluteI451或FR20through3.95的原表/Σ。

旧报告r=Γp/Γγ .080不能当Bp；Bp=r/(1+r)=.07407。报告字面T1/2=10fs与引用J04mean10标签不闭合：固定mean10得omega2.5797近报2.6，literalhalf10则1.7881，保原文字/算术，不改raw或当正式erratum。原PRC74045810/thesis未取，当前journalreadiness边界明确；下一可查官方exact23AlEC编译的字段/来源，仍不以转载当独立实验。

## 官方23AlEC：NR空与绝对参考警示

[[nndc-2021-mg23-lifetime-strength-reference]] M23-17–26新增exact299行对象：NR空、RI451100只相对，EC TI总87.7483%不完整；评价明确I451abs43.3(1)%由旧source推导程序/γinventory不清需caution。7788TI4.89(.25)%不是throughγ3.95，两个gamma1.53comment与base20/100/原SA11图不同时闭合，不修raw或判实验矛盾。

这给FR20旧absolute参考使用门，却不自动否定daughter比：若p和γ共用同一physicalI451scale可相消，relativebranch/eff/feeding/Cov仍需原源。另beta-p detectorlab kinetic→totalCM乘r，capturebeam lab→CM除r，原两行558.2/828.8近闭583.8/866.8；必须先识别particle角色。3.95原表/Σ仍readiness未闭，不能以官方转载补新CI。

## 作者Chapter4修订geometry疑点与response范围

[[fougeres-2022-thesis-evasions-response-contract]] F22-1–15原13页完整主线/图表式读(未读全201页)。作者实测target/catcher间19(1)mm，确支持public19000µm；此前与Nature“back-to-back”的比较只能当描述/版本桥，不能当geometry已错。原publicloader/scalar故障另保，逐项证据不混加。

Chapter4给σ=FWHM/2.35、data-derivedSNR/noise与28Si benchmark：归一6.81–6.91、fit6.84–6.90MeV，τ2.0(.4)ps/90%CL只该longlived条件；caption角窗与prose/legend不同需job核，不移作F23fsfit。Table4.1 .28‰×6750=1.89keV，binwidth不等仪器σ或零profileeffect统计定理。正确只读publicbeamSPlookup约.63074MeV对thesis.662保残差，未修source/重报实验CI。

### Ch5原选择合同：粒子门、合成角与污染拒绝

[[fougeres-2022-thesis-evasions-response-contract]] F22-16–30新增完整Chapter5原读，所有15图3表11式文本/视觉核。Table5.1真实22门及Eq5.8分别核，key37.5–39.5MeV与另六行区间相交，不能以α门独占父态或把区间长度当污染概率。

原PID需要Z/Bρ/t*；方向由VAMOS与DCT在3°θ/30°φ条件下组合；Eq5.7实际用recoil—γ点积角，不等beamθγ。最关键的是Figs5.8/5.9作者明确拒绝28Si6879与Mg7333相交的(Eγ,θγ)区域，实际mask/job缺。这使publicderivedtree/全显示χ²不能认证paperfit的输入差异更具体，不证明已经找到唯一差异原因。

Eq5.5厚靶打印系数与图量级不闭合，Table5.2的7.785标签与only7.333文字不闭合，保原件不猜修；Fig5.13的Exsigma.1451MeV为母态分辨非寿命CI。thesisβems与F23Δβ需eventmatched转换，共享key参考归一不是新独立测量。新[实际输入练习](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch5-exercise-result.json)只作门/印刷式/Doppler交叉核验，无新τ/BR/CI。下一精确route是Ch6的实际fitdomain/背景统计；Chapter3/6及appendix尚未读。

### Ch6同数据组合：minσ与未知协方差

[[fougeres-2022-thesis-evasions-response-contract]] F22-31–47完整Ch6原件/17图9表4式。正文明确DSAM/βM/DCLM共用data，Eq6.2取逆variance中心及minσ；不能作为三个独立τ。DCLM每个τ以MCmeanβ改变data/MC坐标，Fig6.8方法差值约对称仍不能排共同bias。真实targetshift17mm/ZAGATA−252.3(1.7)为原校准，不是publicgeometry错误。

[新实际输入练习](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch6-exercise-result.json)以11(+6,−4)、9.5(+4.5,−2)的声明对称化σ5/3.25，weighted9.9455；固定weights时ρ>.4623125则σ>min3.25，条件反证minσ通用保守性，actualρ/联合asymmetriclikelihood仍缺。Table6.4 τ9.5与Γ60中心打印不闭合，Table6.7 τ9.9/Γ66闭合量级，保原值不修CI。

BR模板仅7.65–7.85MeV算χ²，7770有BR<.2%约束，Ex差门/pureAu背景/SPIDER100%intrinsic假设明确。thesis.68(.06)%与F23.68(.17)%是同实验版本差，非独立BR确认；另一alphaγ方法15(+16,−15)%不能当精密确认。TALYS截面不能定keyspin，源levelscheme的7/2标签不变实验J证据。ROOTmaximumlikelihood/LL接口与手写likelihood需新API核，原job/Σ未认证。

### ROOT接口与inactive示例：不能由LL名字指定统计量

[[root-2026-chi2test-option-contract]] RCT26-1–13新增固定ROOT6.24.06/6.40.04原函数全读及actualnative；LL不被Chi2Test消费，默认自动UU/UW/WW由Sumw2/有效entries决定。内部MLE共同bin概率不等fixedmodelPoissondeviance。Chisquare(TF1,L)是另一个接口。ndf为selectedbins−1再去jointempty，不自动扣τ/E0物理fit。

同contents的声明组件从6.199134(UU)变8.783184(UW)，LL/无LL一致；Tools.C原表达式摘取原样编译，base6.410432对properdeviance12.410432，o>0/s0时原finite而proper∞；FindBin高端排除也改变domain。全为design组件，不是实验data/新CI。ROOT低counts/forcedUUwarnings原样留档。

CodeA L42–141整段示例inactive，这是对grep候选的明确限制，也吻合旧EV23-13；不能说原paper跑了这些调用。源本身、实际job、Sumw2历史/模板Σ及fitmask仍需匹配，代码有用但不认证原实验统计。

### A.2实际三窗：扣背景谱的误差合同

[[fougeres-2022-thesis-evasions-response-contract]] F22-48–53原AppendixA.2/FigA.2：DCγ中心7318–7348keV与左右7288–7318/7348–7378各30keV，投影Ealpha后D=S−(L+U)/2，实际图有负值。

[符号练习](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-a2-exercise-result.json)以真实门而无假造counts推Var=VS+VL/4+VU/4−CSL−CSU+CLU/2；仅独立primitivePoisson时S+(L+U)/4。多track/sharedevent或其它weights需实际Cov。减后D不能直接当Poisson计数，原bin/闭开边界也待job。背景曲率模型b0+b1x+b2x²残余−b2h³，h30给−27000b2，不给actualb2/实验偏差；signal到side泄漏另需response。

只补原operator，不补Ch6pureAu全流程/τfit/Σ。初sympy缺失已记，最终只标准库Fraction精确有理数；读取时额外A.3文字作为priming记录，不称整个附录原读或新课程卡。

### 真实25图点：统计合同查询仍未识别原fit

[[fougeres-2023-mg23-velocity-difference-lifetime]] F23-24–28与[[root-2026-chi2test-option-contract]] RCT26-14使用原公开25图点作新native接口查询，不重复旧Pearson当新实验。全点/原error/原XLSXhash保，未扫描门或删bin匹配17.1982。

| 明确声明的数值合同 | 全25点结果 | 边界 |
| --- | --- | --- |
| ROOTautoUU、modelerror取fallbacksqrt(M) | 41.654553 | 不知道真实MC误差；非固定模板deviance |
| zero-modelvariance的UW、same-domain归一 | 110.195944 | 等normalizedPearson；zero只是条件 |
| same-domainfixedmodeldeviance | 95.748411 | fractionaldisplay不认证rawPoisson |
| 假定原variance=M后actualScaleα，强制UW | 47.939784 | α²variance配套缩放前后一致，不估实际MCstats |

α=1.095013423；重新只填αM而让fallbacksqrt(αM)给UU43.206006，改变了数值误差合同。actualScale保存α²sumM=437.019908，不能把只内容归一和完整统计对象缩放混同。所有接口p/ndf24/lowcountwarnings都不解读为实验检验、没有原τ/E0profile/Cov。下一matchinginput仍是原job/mask/模板误差历史，当前都不能与SI17.1982作同一统计量闭合。

### Ch3实际校准：高能效率、角核与Bρ物理合同

[[fougeres-2022-thesis-evasions-response-contract]] F22-54–73完整Ch3/PDF44–72/31图8表11式。真实输入补充薄靶无keyγ、事后3He面密度/beamintensity缺口、Eu152低能绝对eff与Geant100–8000keV同geometry归一、547Au门/4mmPSA尺度导出的σθ.667，并非独立knowntrueposition分辨测量。source/inputcalibration与原job/Σ仍分层。

[实际输入/native练习](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch3-exercise-result.json)：Eq3.9 fractionε1300=.0429969/7333=.0105908，图fullcoeff给.0408452/.00987088，相差5.268/7.293%；不猜实际job采用哪组。声明β/角的ε(Eobs)/ε(Erest)约1.04–1.076是角色控制，不是实验eff用错裁决。

Eq3.6按p=qBρ定义把p/(mc)作为β；publicBrho_Ekin_conv原body/native在.95Tm给43.93835vs同常数momentum42.92645MeV，反向仍回.95。互逆不证明物理关系，原code/data不改、原papercal/job未知，不重报能量/τ/BR。[[evasions-2023-public-release-native-readiness]] EV23-17只追加原表达式边界，旧rows/flags保留。

SPIDER图/表/default几何与宽度须matching：σθ与∆φ分割宽不同；strip/sector一致性门、PID/Alcover/响应不可从public12branch完整重建；DCT气压未记，位置标定借SPIDER孔且两DCT均值/分位差不是独立absoluteangle真值。下一高信息可用真实publicderivedevents作条件选择descriptor，保持事件/track分母，不能在原reconstruction/contaminationmask缺时冒paperfit。

### 真实event/track分母：相同门数也可能换事件

[[evasions-2023-public-release-native-readiness]] EV23-18–23与[[fougeres-2022-thesis-evasions-response-contract]] F22-74。actualpreflight已存trackZ≈−324…−108mm；public−17是relative nominalshift，不是thesis绝对−252.3。初冻结混同在计数前依直接code/metadata修订、原冻结保，未扫描offset调出结果。

[固定条件query及51entryledger](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-conditional-event-result.json)只用beamaxis/meanβ近似，base363176、angulartracks382017，真实三窗L/S/U18/20/13、51event且无窗内多track。D4.5，Poissonizedrecordcluster二阶矩/trackdiag均27.75，fixedN中心化27.749944是另一条件模型，不附实验CI或通用独立性结论。

同S集合的α37.5–39.5MeV门：两个Bρ表达式都3events，却只2个共同entry；literal独11896、momentum独124638、共同132983/205708，均0-based。原θDS/PID/target/contaminantmask不完整，不能从同count或这51条query裁物理keyyield/原τ偏差。原34source/datahash保、无新原paperfit。

### AppendixB实际校准：core、TrackE与共同增益误差

[[fougeres-2022-thesis-evasions-response-contract]] F22-75–86完整AppendixB/PDF171–178，7图2表无编号式，文本/视觉核。canonical源页保存完整七线σ表与TableB.2全部64通道字面输入，62numeric/1missing/1ambiguous；Q1strip14与Q4strip6不填补，不能由表变publicraw重放。

B.4是coreE，Ch3效率图TrackE；同source不等同observable/selection。Eu初activity/age/time实际数给mean/half两角色Astart4461.82/6932.14/s，ratio1.553656为条件算术，四个官方HTTPSTLS失败均无body，当前不靠记忆裁τ/eff更正。保失败、不降TLS、不强配1.80归一。

[实际参数Cov练习](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-B-exercise-result.json)：Q2strip1在5485.6keV的unknownρ预测尺度1.999–101.741keV，不是intrinsicFWHM或原CI；共同gain/offset产生跨eventCov，不能作独立eventsmear。TableB1近7MeVσ4.4±2.1→FWHM10.34，quotedfituncert/truekernel分开。Si6878在线cal与longbenchmark至少共享线/装置，eventsidentity未知不数完全独立验证。

### Si角度生成指纹：可恢复index，不能恢复原标定

[[evasions-2023-public-release-native-readiness]] EV23-24–28/F22-87在已读Backup与新Ch3/B输入下作actualquery，不计新sourcebody或独立data。7933个positiveSi_dE的16个Siθ逐项match固定119.8mm/24.75+1.5i stripcenter recipe，最大残差8.47e−7deg。source页canonical保16值/occupancy，数值精度是写入规则的浮点指纹，不是survey或truepositionresolution。

可恢复recipeindex0..15，仍缺quadrant/rawamplitude/完整calCov，不能由此补Q1strip14或唯一选TableB2 gain。Backup的GATCONF1/Brho>0/target1–5链与QPL/time只comment、γ条件只selfassignment应分层；原data里6867–6883keV inclusive确有26tracks/26events，不把它们全叫某核素污染或直接作一维veto。

[新query结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-recipe-fingerprint-result.json)与34hash保；初ROOT RVecOps Abs接口名称编译失败已保，freshprocess逐track std::abs成功，原fixedquestion/selection不改。下一可用actualopticalangles核mrad/θlab生成合同，但θ一致也不能独定φ handedness/相对frame；不以缺原job/Σ填MODELhistory。

### 极角吻合不能认证相对方位frame

[[evasions-2023-public-release-native-readiness]] EV23-29–33/F22-88新actualdata核：既定363176条base中storedThetaLdeg全matchEq3.5 acos(cosΘcosΦ)及mrad输入，max4.7683e−7deg；two-projected-slope式max.058978deg、RMS.008721deg，不是同一个角约定。未fit scale/offset或另搜公式强配。

[实际字段/数学控制](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-optical-angle-result.json)还显示[±cosΦsinΘ,sinΦ,cosΦcosΘ]均unitnorm/同θ，但φ候选绝对差median104.198°、max180°。这个候选反射不是实验测得frame失配；θ一致不决定正确相对handedness，更不认证γ−π/2/光学xsign/DCT组合/原θDS。当前不做缺matchingvertex-loss/完整坐标cal的recoil/fullτ重fit。

输入角色获得直接支持，原源/δ/Jπ/τ/BR/CI无新裁决；同dataset函数关系不计独立geometry测量。该局部变量问题已达到明确readiness边界，回到Day18的τ→B→Qt和bandmixing核结构问题重建候选，避免只按更多代码检查数推进。

## Chiara完整主线：分支来源改变强度，AMR还缺高频率寿命

[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-7–24完整30页/21图7表3式(旧目标29保freeze，实际末页reference30)，SB六Ge/8π原TableI纠正旧metadata Gammasphere误标。review旧6row保持，所有新claim needs_review；全文仍未给bandQt轴公式，不能以MU08 methodcitation识别其candidategeometry。

实际不同reaction决定intensity来源：108In用backed，110In用thin。三个parent[新ledger/结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/chiara2001-branch-result.json)在声明γ-only/α0/δ0下核E1/link缺支：108B3 16+的357.3还有1220.5E1，control2.5135对原2.48；110B3(18+)还含366.9link，controlBM1 1.3633/BE2 .031633，原1.35/.029保差不强配；110(19+)作者thin给BE2 .051479，故意换backed给.101528，固定同G的Qt比1.40436。只是错误输入替换对照，不指作者用错、不给新CI。

AMR反证：已测110B5四点ωmax.536，作者预测明显BE2下降>.70；已观测(27-)/(29-)E2在.70955/.8134但无τ/B，优先新测这些level的lifetime+feeding/branch身份才提高解释。largeJ2/BE2必要非充分，现postalignmentBE2近常量且crossing点可混合；无shift的其它band下限依equalQ/fastSF，slowSF是原作者保留的竞争解释，不可把无shift等同已测小形变。

Day17本卡P/A/Q的实际companion同样在原文出现：DCO无法区分E1/nearM1时采用旧pol，本文不是新测P/A/Q；source引用的priorbody本轮未开，不补其校准。TAC/PAC形状/minimum是模型，g_s/配对/quantumfluctuations和alignment残差另保，不把模式标签移成experimentalshape。

## E2算符与转轴：同强度不唯一给内禀矩

[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]] dated F01-D17-1–9只定向printed468–473新原读，自审增量needs_review；旧15人审claims/falseflags与原12906-byteprefix完全保持。Eq10球张量规范和Eqs34–36的charge分量、potentialq/β/γ及labz沿J分别保存。

[新条件推导](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/frauendorf2001-e2-exercise-result.json)另定义q_ch=<Q20′>=Q0conventional/2。axialcharge得到Q22=sqrt(3/8)q_ch sin²θ，BΔI2=15Q0²sin⁴θ/(128π)；Cartesian张量旋转/norm作独立规范核。保持同B的q_ch/θ例(4,30°)/(4/3,60°)/(1,90°)不是TACselfconsistentminima或实验多解，只反证单projection不唯一给intrinsic矩。actualPACθ90/组态等约束不能被此自由family绕开。

同axialmodel的BE2ΔI1/BE2ΔI2=4cot²θ是必要companion形式；同一ΔI1光子δ²=(.0569/.0816)E²BE2_same/BM1_same，不给符号，不可拿E2crossover比M1代同photonδ。普通IC/branch若随δ变，须共同传播。staticQ20、μperp及更多E2component/axis信息可提高识别，单τ/B转换不足。

finiteI16/K0 exactCG²120/341=.351906、highspin.375、candidateGs29/33=.878788是三种有条件对象；固定同B时Qcand/Q0=.632807，不能凭近表值认historicalproducer。source直接说semiclassical式取highspinCG、fixedK在weakdeformation会失败。MU08实际Qt轴依然缺，不改原reportedQt/β/γ/模式或CI。


## 110In缺失companion与综述的同数据边界

[[kumar-2025-review-magnetic-antimagnetic-rotational-structures]] KU25-11–15原Table3 p50仍只引用2001Ch71，四点τ/B与[[chiara-2001-108-110in-shears-band-lifetimes]] TableVI一致；27/29的Eg/2=.70955/.8134MeV虽过模型预测.70门，但τ/B空白，不是新的高频率测量。2025汇编日期不增加独立实验。

本次[实际表列计算](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/amr-review-energy-result.json)核Elevel严格升、Eg在15→19先降，原review“level energies”literal不闭合；保词义而不制造实验矛盾。19/21/23的quoted marginal BE2 box交于[.258,.279]，不能称jointCI、恒定性显著度或AMR支持概率。原TableVI未含达±20%stopping系统量，fullCov/response仍缺；没有给该量指定Gaussian或共模比例。

Simons2005 DOI10.1103/PhysRevC.72.024318、Datta2005 DOI10.1103/PhysRevC.71.041305为高信息Cd检索入口；本次网络TLS失败仅有身份，不认证正文/独立τ/同模型差异。下一route应取得primarybody及actualfeeding/stopping，或在现有本地原件检查已知DSAM输入链，不能用更多同表重算填补缺τ。


## 侧喂养积分取向不提供时间取向合同

[[draper-1970-gaussian-substate-side-feeding]] DR70-D17-1–10新全文自审将Eq7归一population的intensity混合与Eq8转换总强度反演固定下来；Os/Hf表使用smoothedside列，不是独立yield。168Hf raw .91−1.08=−.17而smoothI6=.15；声明截断smoothF6=.95时对相邻A反演放大6.333/−5.333，实际fitCov/IC细节未知，不生成实验CI。

p216原σ2=.143对A2=.225不闭合：完整CG/photon核给A2约.714；保持原件与旧人审prefix，另记source-number boundary。匹配A2约需σ2=1.42，但exactcascade与单Gaussian代理A4差约.01344；不能仅匹配A2便继承整个population。原constantσ/J=.28与184Os趋势不合，也是固定取向输入的实际反证。

原Eq7只给时间积分的路径权重；各路径feedingtime与rank2/4若相关，能否以固定W(theta)乘共同衰减需另核jointkernel。原作者未给DSAMtime/response，当前任何extension必须标Codex条件推导，不能说原论文测出当前核的τbias。必要输入是samegate路径强度、各路径时间/取向和逐角response；共同stop/feeding/Σ仍缺。


### 同边际仍缺时角关联

[[feeding-time-alignment-joint-response]]给一项CG可实现/正ρ的解析存在反例：交换两feedingpath的取向与等待kernel，积分AD/全Stokesρ及总时间密度相同，逐角DSAM响应不同。依据DR70-D17-1/2/10限定原积分混合，extension另标Codexdesign；新无量纲30°Δcentroid/(E0β0)=.0290767不对应当前核实际bias。需actualsamegate逐路径时间/取向、multiangle响应及Σ，不能仅由source积分I_J和全谱timeprofile补闭合。


### 取向误差的实际反应域

[[ekstrom-1979-spin-alignment-attenuation-a61-a67]] EK79-D17-3/5/9/11的MANDY模型alpha2处方、hightreshold残差及20%feedingdesign提醒：预测误差/实验误差/实际feedingtime不是同对象。alpha,p有效能量2–3MeV差仅该域说明；不能给重离子DSAM/ComptonQ套相同floor或认定currenttimekernel已知。原α2/α4表新计算保共同parent/来源与Σ，不转实际τ/B/Qt修正。


### 61Ni原实验的fs单位与强度companion

[[wadsworth-1977-61ni-levels]] WA77-D17-1–14新19页核改旧Wiki：1609寿命370fs而非37、908为约1.5–1.6ps而非ns，9个Jπ分数/正负按原表；保WA77旧reviewflags。声明γ-only/α0与same-lineδ的1609两支给BE2约.520/.0467WU、BM1约6.87/12.60mWU，近原表而不调input；错τ37会使strength×10。

Table4τ误差不含stop，strength采用τ±25%allowance；908摘要1500(400)fs与表1600(500)fs保差，不能一项预算复制所有物理量。1609/1997最终宇称依AD/P加τ/M2合理性，sourceP本身不足。1729/2018的90°branch、1186的61Cusource与其它fitteda0有不同inputrole；finitewindow/feeding/overlap使时角joint合同仍未闭合。

## Day18停止时钟与带间contrast

### 新session问题与实际阅读

本节为2026-10-20独立正式Day18 run的新交付；[来源前primed回忆/hash](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/active-recall-freeze.json)承认Day17大量预习，非盲测。新[合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/exercise-contract-001.json)、[程序](../../system/scripts/day18_dsam_clock_contrasts.py)和[结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/clock-contrast-result-001.json)没有重跑旧script/JSON换信用。Jensen本次只定向DSAM和必要context，MU08本次完整六页/五图两表三式；[actualscope](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/source-reading-scope-001.json)将全文与定向区分。

问题是：由停止标尺导致的绝对时钟不确定性，能否任意解释两带随spin改变的强度差？支持与反证分开：J01-D18-1给出5%已加的真实口径与mixing同标尺依赖；MU08-D18-1给出15%未含、belowgate与五步feeding口径。两种百分数不定义同一概率模型，也不补原Σ。

### 测量、拟合、率与几何的分层

| 环节 | 本次原件依据 | 主要输入/系统误差与边界 |
| --- | --- | --- |
| 谱观测 | J01-D18-1的Fig7；MU08-D18-1的Fig2 | 逐ring背景、峰污染、门尾、探测器响应/位置/能标；公开直方图不是已取得原计数账本 |
| forwardfit到总meanτ | J01-D18-1的Sec3.2；MU08-D18-1的PDF2–3 | 停止曲线、材料、反应深度、feeding/sidefeeding、离散时步和统计量；不是无模型计时读数 |
| partial photon rate | J01-D18-1的Table2/刚转子提取；MU08-D18-1的TablesI–II与pureM1假设 | 必须另有绝对pγ、IC/额外衰变库存与同光子multipolefraction；branch归一和1不认证库存 |
| B(Eλ) | MU08-D18-2的TableII输出；率定义见本页前节 | 固定单位/多极性下B∝pγ f/(τE^(2λ+1))；τ、分支、δ、α和效率可共享Cov |
| Qt/结构 | J01-D18-1的rigidrotor/Table6；MU08-17候选几何边界 | Qt需G/轴，Qs为sidefeeding量；MU08三式并非Qt式，tableprinting相合不认证producer；β/组态/手征另需companion |

这里未重新复算旧十一/九行，也没有将旧nearest-decimalbox升为CI。Jensen的Table2直接DSAM两带与Table6 mixing派生两带、MU08的τ/B/Qt和本次contrast均保同源。

### 完整谱形的条件时钟对称

以下是本任务解析模型，不是两篇作者声称的精确实验对称。设同一均匀介质的速度/散射生成元整体乘s，沿轨迹有v_s(t)=v_1(st)。t可取一个统一时钟；本程序取**proper time**，保证meanτ角色明确。令Bateman生成元也整体乘s，即每个总寿命及sidefeeding等待时间都除s。若目标发射密度为p_s(t)=s p_1(st)，能量/角接受/分辨率/能量门合成核K只依赖对应速度历史、分支和固定几何，而不独立依赖绝对时间或发射位置，则逐bin预测为

\[
\mu_k(s)=N\int_0^\infty s p_1(st)K_k[v_1(st)]\,dt
=N\int_0^\infty p_1(u)K_k[v_1(u)]\,du.
\]

这是概率密度换元的恒等式，不要求Gaussian数据或只测centroid。多角度、固定能量分辨率、finitebins或只依赖γ能量的门，都不自行提供另一个绝对时钟。所有支路时间一起缩放时，相同论证适用于条件cascade选择；若某条已知feed寿命固定，则前提已破。

固定photonbranch/multipole/能量/G时，τ_i→τ_i/a给λγ→aλγ、B→aB、Qt→sqrt(a)Qt。它说明共同绝对标尺与相对contrast是不同问题。实验中只改变电子阻停而不改核散射/其它生成元、有限靶层边界、反应深度及位置敏感度，通常并不等于这个整体变换；不能据本恒等式宣称Jensen或MU08实际完全不可识别。实际prior或独立calibration可以破这个方向，但其信息须单列。

新数值控制选择β0=.025、proper停止时标.45ps、meanτ=.55ps、35%直接+65%三步Erlang侧馈（每步mean.18ps）、E0=600keV、Gaussianσ=.9keV、37/79/143度±5度接受和120个.5keV bins；均为**本任务声明设计**，非两实验输入。能量核用E0/[γ(1−βcosθ)]，独立Laplace矩核验发射密度，384/512/768节点核求积收敛。a=.4/.75/1.25/2的同步变换在数值精度内保持所有bins；新25项检查全部通过，检查数不是实验或学分。

### 破对称的必要companion和反例

| 自设控制 | 最大逐ring归一bin差 | 含义与限制 |
| --- | --- | --- |
| 只把stopping乘1.25，τ/feed固定 | .0252213 | 真正新增的已知时钟可使谱形变化，不能把stopping变化等同任意寿命变换 |
| 同步改stopping/τ，但feed保持原物理时钟 | .0124288 | 独立feeding约束可破退化；仅freeeffectiveQs未必提供该约束 |
| 固定实验室.4ps时间窗 | .0399677 | proper/lab映射按同β轨迹精确积分；不是实际装置已有如此时间门 |
| 固定位置响应exp(−x/2µm) | .00729456 | x=c ts/s[asinβ0−asinβ(t)]；空间轨迹随scale改变，固定geometry不必保持谱 |
| β(t)停止曲线形变而非纯scale | .0141125 | 单个全局scale方向不能代表全部stoppingmodel差异 |

数值只是声明forwardfamily的反证，不估计实际τbias、效应显著性或装置精度。原材料界面是同类破对称条件，但本程序没有模拟Jensen/MU08的真实多层材料；不将位置响应控制冒充原backing重拟。

### 原MU08表的尺度不变contrast

本次直接从PDF4 TableII重新取I16–19原B(E2)打印中心，不由旧Qt或原τ反解：

| I | Band1 B(E2) | Band2 B(E2) | R=B2/B1 |
| --- | --- | --- | --- |
| 16 | .26 | .51 | 51/26≈1.96154 |
| 17 | .08 | .44 | 11/2=5.5 |
| 18 | .14 | .04 | 2/7≈.285714 |
| 19 | .11 | .05 | 5/11≈.454545 |

B单位e²b²；原quotederrors保持在source，此处未把它们当jointCI。令任意两带各自常数标尺为c1、c2，则R_I→(c2/c1)R_I，故

\[
D=\frac{R_{17}}{R_{18}}=\frac{.44\,.14}{.08\,.04}
=\frac{77}{4}=19.25
\]

不变。没有一组每带恒定标尺能把这些**打印中心**同时调成全部R_I=1；最优任意相对常数也至少留下sqrt(19.25)≈4.38748的最大乘法偏离。这个结论不需要Qt轴，也不等于实际拒绝某个结构模型的joint统计检验；若逐态branch/feeding/效率/multipole输入可变，前述标尺域已变。

进一步只作透明的**自设box灵敏度**：每个B独立容许乘[1−d,1+d]且0≤d<1，则D最低为19.25[(1−d)/(1+d)]²。d=.10/.20时分别12.8864/8.55556；要让这个必要条件达到1，需d≥.628769。这不是源15%的解释、测得系统误差、概率区间或原CI，不能写成“实验需要63%错误”。它仅量化指定box到底允许什么。

MU08-D18-3另保原文“factors2to3”与I17中心5.5/I18逆比3.5的literal范围差异，不为匹配文字去改表或猜erratum。强度模式对每带常数尺度稳健，并不免除同data的branch、feeding与选择审计。

### Jensen对照、readiness和self-audit

J01-D18-2中均值Qt541/Qt411=8.3/7.4≈1.12162，共同时钟尺度不改该比。但若额外允许两带不同常数a541/a411≈.794890，则sqrt(a541/a411)可把中心比调到1。这只显示**哪种自由度**能改变单一平均比；没有用原5%定义这种自由度的分布或把21%当实际停止偏差。其Au/Pb一致性与结构模型提供有用companion，不能被本设计抹去。

原Jensen/MU08匹配逐角bins、slowing/branch/混合/几何producer及联合Σ仍未取得；实际实验重拟合/CI为not-ready。下一高信息输入是matchingstopping/feeding校准、原DSAM方法/实现及逐态响应，而非更多同族toy或重复旧表。原谱直观、拟合τ、转换B、Qt及结构解释各自的证据角色保留。

本节Codex self-audit：解析域和反例均显式，旧review/needs_review保持；J01-D18-1/2与MU08-D18-1/2/3全为needs_review，非human-reviewed。`supports`共同尺度与spincontrast分开，`limits`把相对比较自动说成systematicsfree。真实两带组态/手征解释仍须matchedobservables/模型边界，不由本设计唯一裁决。此独立交付不兑换Day17预习学分，整段原deadline与最终课程发布门仍由本次actualreceipt控制。

## Day18新54Cr原件：停止分量、组合角色与模型δ

[[stuchbery-2026-cr54-dsam-reevaluation]] SC26-1–12为本session新发现且完整原读的arxivv2十一页/五图五表五式，不是Day17旧preview。期刊metadataPRC114034322/DOIgm4m-8wyn与实际arxivbody分开；官方源码九成员只有文稿/图，不认证作者OCR重建程序或logbook已经取得。

SC26-2/4/5把前节clock模型的边界落到真实案例：作者重用1980观测，用更新SRIM替换LSS电子停止，核停止变化较小且影响散射；因此不等整个生成元统一timechange。七个matchedTa-only寿命中心的倍率约1.193–1.268，不能拿一项恒定乘数作精确替换；不是新独立寿命。也不把这个6.3%倍率spread迁给MU08逐态误差或推翻D19.25诊断。

SC26-7特别区分旧Ta3.5ps、新Ta4.2ps和合Mo的3.8ps：20%的matchedTa变化与8.57%的mixed-role商都可从原打印中心得到，但只有清楚标对象才能解释。源“16–27%”不解释成TableIV所有新旧商的无条件界。TableI/II主误差来自ΔE，末两列为电子±5%/核±10%变化效应，TableIII另含组合；这些都不提供原jointΣ。

SC26-11的新23行Eq5复算中心最大差.000769；Ta/Mo的3160同母态两条线在额外独立误差候选下得F.332181±.023122/.380722±.050897，不能据相合认定原平均程序/Cov。观测printedF1.002保持，不clip后称新数据。原Ta4+1/6+1在pγ1/pureE2条件给B227.004/230.762e²fm4，仅近原228/233，仍不认证branchinventory。

SC26-9/12是另一反证：4043态候选6+及820keV支的“experimental”B88e²fm4用了模型δ=.05。固定绝对photonprobability/τ/E，换自设δ=.025/.10会把E2份额乘.250468/3.970297，条件B为22.041/349.386；不是新的实验误差或可自由选δ。作者明确新spin建议与DCO冲突，保tentative/待新spectroscopy；不能用同模型δ构造的B独立验证该模型。

源对另DSAM的LSS/Ta依赖、Lieb/Kuronen同GRIDdata重分析以及2620态未闭合差异均按SC26-8保留；未读那些原件不计新独立measurement。下一高价值路线是本公开源码文稿可定位的原analysis/独立Coulomb或GRID输入，而非重复新30项算术检查。Jensen引用Gascon/Currie/Bacelar的当下合法路线只得metadata/访问失败，尚未原读；不因题名或TDMlicense补方法。所有新claims待审，原raw/PLAN/Bib/旧flags保持，整日原窗口继续。

## Day18新58Fe原件：新计数不等最终B全输入独立

[[woodside-2026-fe58-collectivity-coulex-dsam]] WO26-1–14实际完整原读arxivv1十五页/13图10表4式；abs写14页保留。新Coulomb数据与旧1978DSAMraw/重建analysis分开；原src19成员没有Gosia job、旧DSAM程序、数值yields/联合Σ，不用更多模拟代输入。

| 信息层 | 此原件实际对象 | 独立性与判别边界 |
| --- | --- | --- |
| 新采集 | WO26-2的CAESAR/photodiode particleγcounts、56Fe同条件对照 | 对旧DSAM事件是新采集，不能因此宣布全部后续约束独立 |
| yields/response | WO26-3的relativeefficiency/AD修正、2→0归一 | TableII不是absolutephotonbranch或裸count比；共同reference/背景/接受仍需Σ |
| fixedreference/diagonal/buffer | WO26-4/6的旧CoulombRME、Qs2及assumedQs4=0、bufferstates | 独立信息、模型迁移与旧数据依赖要逐项列；Qs此处静态，不是sidefeeding量 |
| lifetimeconstraints | WO26-5 TableVI的2+2τ2.4(.5)及目标4+1τ.66(.08)来自updatedDSAM | 直接存在共同输入；无去目标τ的matchingfit，不称最终GosiaB与该τ完全独立 |
| phase/fit/B | WO26-7/8的八phase、Q方向相关与19–27W.u.输出 | 保七未排方案，不用minχ²直接选唯一phase或任意分配Bayesian权重 |
| 旧DSAM重分析 | WO26-9/10的电子/核模型改动、stat/含stop两误差 | 原raw已不存在，logbook/listing为作者所持；新code/τ/B不增实验次数 |

这个矩阵`revises`前节依据SC26二级简写的“58Fe独立Coulomb验证”：独立采集与完全独立提取不是同一命题；也不据此反判新Coulomb观测无信息或原结论无效。Gosia还用SRIM能量积分，其角色不等于DSAM时钟；同软件名不能代误差相消或同一输入假设。

本session新[相位/输入合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/woodside58fe-input-contract-003.json)、[程序](../../system/scripts/day18_fe58_phase_input_audit.py)/[20项结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/woodside58fe-input-result-003.json)只枚举Fig8/9真实印图E2子集。实statephaseη_i下M_ij→η_iη_jM_ij，每个closedloop的η成偶次；56Fe图V7/E8有2个独立环、4类，每类64符号配置，58Fe图V8/E10有3环、8类，每类128配置。单statephase不测得，Eq3P3不变；同pair E2/M1比也不因statephase改变，故不把三chord符号叫measuredδ或configurationmixing。DiagonalM_ii不变，静态Q符号也不能靠这种gauge翻转。

新TableVII八个RME按Eq1/常规WeisskopfR=1.2A^(1/3)转换与原整数B在.51W.u.打印域内相近，不是原Gosia/CI复现。TableII rawratio→yield总修正因子约1.394/1.630/1.449/1.789，只能称combinedrelativeefficiency+AD，不拆成absoluteeff。Eq2静态Q56/58对应diagRME约−.250682/−.356232eb，独立于statephase；原Q4=0仍是从56Fe校到58Fe的分析选择。

WO26-10保TableVIII首stat/第二含stop误差以及prose.66(6)与VI/VIII/IX.66(8)的literal差异，不重复quadrature。WO26-12保effectivecharge点簇不定斜率、prose1.33/caption1.3与basis依赖，不把壳模型贴合替代实验校准。

下一能改变认识的actualinput是：目标τ约束的Gosia权重/去约束profile、fixedbuffer与referenceB/τ的官方原源谱系、独立Qs4或更强相位观测。只做更多E2图gauge枚举不能量化原constraint贡献；当前真实B/τ/CI重拟仍not-ready。所有新claims待审，未给独立盲测或下一卡学分，原次日15点窗口继续。

## Day18官方58Fe参考：同一B的τ与矩阵元

[[nndc-2010-fe58-reference-lifetime-lineage]] F58-1–8来自本session新取的exactENSDF201004三个对象。Adopted只读header/低态选段、Coulomb34行与αpγ140行全读；download2026不是新评价。官方811T评论直接写由1981Le02 B(E2)=.1234(.0036)推得，静态Q同primary；新NSR两querySSL失败无body、不降TLS。旧原实验未读不预填其phase/Σ。

F58-2/4给811half-life6.54(.19)ps→mean9.43523(.27411)ps，同paperadopted9.4(.3)对应。Coulomb励起Bup=.1234的声明E2chart给M=.351283eb、Bdown=.02468e²b²；fixedprintedICC/γ的现代rate给τ9.43732ps。相合只是单位/率核算，不增加独立measurement，也不据其认证原Gosia执行细节。原.351(.006)、9.4(.3)及官方旧值均保持。

如果在固定E/branch/ICC下只保一primitive x=lnBup，则lnM=x/2、lnτ=c−x，Cov=Var(x)C，其中C的两行为(1/4,−1/2)与(−1/2,1)，rank1且corr−1。新[合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/fe58-official-input-contract-004.json)/[程序](../../system/scripts/day18_fe58_reference_lineage_audit.py)/[13项结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/fe58-official-input-result-004.json)将数值variance代入明确列为局部设计，不冒actualGosiaCov。真实额外输入可破rank1；B与静态Q虽同研究，不能未经原Σ设corr=±1。

F58-5/6还保oldreaction2076T.37ps→mean.5338ps与paperold.54的桥；Adoptedtarget.28ps是三个oldhalflife的加权，不是2026newτ。RI76.4与δ−.69属于F58-7的另一2+2支路输入，不能当全parentphotonbranch或用旧half替新mean。

认识变化是原“independentreference lifetime”箭头要回到同CoulombB。actualGosia是否重复使用该primitive、normalization有何特殊处理，仍需原weights/job，不能因官方依赖就判doublecount已发生或给CI修正。下一输入优先原1981Coulomb的B/Q/矩阵元合同、Gosia可执行输入/去targetτprofile及独立静态Q，而非继续同一率换算。

## Day18新106Ag原件：共同寿命消去与形状解释边界

[[rather-2014-ag106-transition-rates]] RA14-1–5是本session新完整原读的arxiv1310.7731v1：12页、3图、1表，VoR未得。INGA/96Zr14N4n/68MeV与Bark review的AFRODITE叙述先按不同采集分层；1fs/5000histories/shell-correctedNorthcliffe与Jensen5fs/三步、MU08的2fs/五步/SRIM均不可混用。18/19effectivefeeding、17强度加权topfeed及12的490abovegate是实际输入，不称全部feeding已消。

RA14-6的新[合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/rather-ag106-input-contract-005.json)、[程序](../../system/scripts/day18_ag106_published_rate_contrasts.py)/[16项结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/rather-ag106-input-result-005.json)用真实12行TableI。在固定分支/ICC/多极成分条件下，同母态BM1/BE2消共同τ；再比较partner/main与spin15/17，得到S15/S17=22624/3105≈7.2863124。每态各自共同normalizer都可消，不要求两个带τ相同；线特异eff/δ/branch/response误差不消，仍无实验CI。这扩展MU08每带常数标尺contrast，但不是独立data。

RA14-7仅反证额外独立SD解释：B∝1/τ且强度独立时，main12/13的寿命至少给BM1局部SD.07625/.16190，而原表为.01/.02。不能据此修表、猜真实Cov或指控作者计算错。RA14-8保正文17dip/peak与TableI/Fig2中心15minimum/maximum不一致；partner18literal0.1(2)原样保，不改为.10(.02)。

RA14-9/10的同B(E2)/异B(M1)与TPSM解释分开：epsilon.15/gamma30°是模型输入，两个不同Nilsson2qp态仍同名pi g9/2 nu h11/2，不能只由B近似相等唯一测出相同形状。RA14-11/12与[[106ag]]还保二手Bark反应90+14−4=100不闭106；不改raw、不拿Rather96靶倒填Lieder。另一primary Lieder PRL112202502仍只有metadata/访问失败，故双原件比较partial，不映射main/partner到reviewBands1–3。


## Day18时间响应设计：RDDS不是无条件的“独立寿命”

[[klemme-1999-lifetimes-134nd-neighbors]] KL99-D18-1–4是在既有priming后的新定向PDF2–4核验，非新完整阅读/Day19。六个tcorr/standard中心因子1.181159–1.255319不共一乘法尺度；空tcorr不当精确零。作者说电子stop+30%可把差异约减半，不提供逐态完整alternatefit/Σ；本任务额外声明tau(f)=standard+f(corrected−standard)、f在[.5,1]而不赋概率。

在fixedbranch/ICC/能量/几何下，B∝1/tau、Qt∝tau^−1/2。新[合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/finite-stopper-input-contract-006.json)、[六行程序](../../system/scripts/day18_rdds_companion_contract.py)/[结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/rdds-companion-result-006.json)给12S1/10S1的Qt比1.1827957→1.1894563（+.563123%）和8g/6g.9296482→.9350779（+.584053%）；平方ratio随f的导数定号，所以端点确实界定本chart。它不重现原stoppingbranch、likelihood或CI，亦不把旧6g18%单行算术算新交付。

DDCM距离恒定性是有用诊断，不保证所有共同速度/门/强度/有限stopping无误差；Qt又继承branch/轴假设。KL99是134Nd独立采集而非106Ag同levelRDDS，不能按同核区/同符号补Rather的数据。下一应取actualsamelevel/response/Cov输入，本session仍正式Day18，下一卡未开。


## 135Nd与136Nd的双向反例：异寿命同强度与同寿命异强度

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D18-1/2与[[mukhopadhyay-2008-136nd-transition-rates]] MU08-D18-1/2共同构成了DSAM方法中寿命与强度关系的完整双向反例：

1. **136Nd（同寿命尺度，异跃迁强度）**：MU08 Table II中两带在I=17处B(E2)比为11/2=5.5，而在I=18处为2/7≈0.286，带间双比D=19.25。即使假设存在共同的stopping时钟缩放，也无法消除这种强度差异。
2. **135Nd（异能级寿命，同跃迁强度）**：MU07 Table I中低自旋区（31/2−–37/2−）Band B的能级寿命τ_B约为Band A的2倍（例如31/2−为1.46 vs 0.75 ps，比值1.947），但两者的带内B(E2)却几乎完全相等（0.28 vs 0.32 e²b²，比值为定值0.875）。由B(E2)∝p_γ/(τ E^5)可知，Band B的偏率因子p_γ/E^5比Band A高出1.70–2.00倍，精确补偿了寿命的2倍差距。

这彻底澄清了物理图像：**能级寿命由所有退激通道总宽度决定（τ=ℏ/Γ_total），而跃迁强度只与该特定通道的偏跃迁率相关（B∝Γ_γ/E^5）**。在没有完整测量分支比和跃迁能量之前，绝不能将寿命长短直接当成形变大小或集体性强弱的代名词。


## 相对强度提取中的混合比双根敏感性：167Lu案例

跃迁强度提取不仅在绝对测量中受能级寿命与分支比影响，在相对测量 $B(E2)_{\text{out}}/B(E2)_{\text{in}}$ 中同样面临决定性的多极混合比 $\delta(E2/M1)$ 约束。[[amro-2003-wobbling-167lu]] AM03-D18-1 展示了这一关键边界：

在三轴超形变带的单声子 wobbling 识别中，带间 $\Delta I=1$ 跃迁的 $B(E2)_{\text{out}}/B(E2)_{\text{in}} \propto \lambda (E_{\text{in}}/E_{\text{out}})^5 [\delta^2/(1+\delta^2)]$。由于 DCO 测量存在两个数学双根：
- 大负解 $\delta \sim -3.1$ 至 $-5.1$：$E2$ 纯度高达 90.6%–96.3%，提取出的 $B(E2)_{\text{out}}/B(E2)_{\text{in}} \approx 0.23\text{--}0.27$，支持 wobbling 图像；
- 小负解 $\delta \sim -0.07$ 至 $-0.35$：$E2$ 份额仅为 0.5%–10.9%，对应的 $B(E2)_{\text{out}}$ 将被压低 **8.6 至 197.5 倍**（比值跌入 0.001–0.031 的非集体区间）。

作者因缺乏直接线偏振测量，只能借用 $^{163}\text{Lu}$ 的类比来排除小解。新[分析结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/amro03-167lu-result-014.json)确认了这种敏感性：**在跃迁强度用于集体模式判据时，混合比解的唯一确定与能级寿命的测量具有同等关键的权重**。
