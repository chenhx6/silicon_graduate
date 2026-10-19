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
