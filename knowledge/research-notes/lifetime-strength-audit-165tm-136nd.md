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
