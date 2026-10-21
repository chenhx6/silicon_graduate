---
type: method
title: Doppler-shift attenuation method
aliases: [DSAM, Doppler-shifted attenuation method, Doppler-broadened line-shape analysis]
created: 2026-08-11
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
method_type: nuclear-lifetime-doppler-attenuation
tags: [lifetime, doppler-shift, stopping-power, side-feeding, lineshape]
---

# Doppler-Shift Attenuation Method

Day18新独立分析入口：[[lifetime-strength-audit-165tm-136nd]]“Day18停止时钟与带间contrast”。均匀时钟缩放可使完整谱形不变，却不改变共同强度标尺下的ratio；固定外部时钟、位置响应、停止曲线形变和逐态feeding是必要反例。MU08-D18-2的真实表中心双比只排除每带恒定标尺这个解释域，不是原实验重拟合或CI。

[[stuchbery-2026-cr54-dsam-reevaluation]] SC26-2/4/5给实际反例：1980同data重建analysis后只更新电子/核停止曲线，不等所有生成元整体scale，寿命改变可逐态不同。SC26-7另区分Ta-only与Ta/Mo组合，SC26-9保模型δ进入“experimental”B和tentativeJπ的DCO反证；不能用新code/τ/B各算一项独立观测。

[[woodside-2026-fe58-collectivity-coulex-dsam]] WO26-2/4/5进一步区分新Coulombcounts与最终GosiaB：后者明确使用updatedDSAM的目标4+1τ及其它外部constraints，不能由方法名认全输入独立；也不能反判新counts没有信息。WO26-6/7/13的静态Qs、statephase闭环和same-pairδ分别保存，不迁到sidefeedingQs/Qt。

[[nndc-2010-fe58-reference-lifetime-lineage]] F58-2/4进一步核官方811参考τ由同CoulombB推得，6.54ps为half-life而mean约9.435ps。F58-8的单primitive相关只在固定E/branch/ICC条件下成立；不能把adoptedT、derivedB及referenceRME按不同字段各计独立观测，实际Gosia计权仍需job。

## Purpose

DSAM uses the attenuation of recoil Doppler shifts during slowing in target/backing material to constrain short excited-state lifetimes. Depending on the analysis, the measured observable is an angle-dependent centroid shift or the full Doppler-broadened γ-ray line shape. Forward and backward detector angles provide complementary velocity sensitivity.

## Inputs and Assumptions

- reaction kinematics, recoil velocity histories and detector geometry;
- stopping powers and material thickness/profile;
- transition placement, contaminant peaks and detector response;
- direct and side-feeding intensities, lifetimes or effective quadrupole moments;
- branching/mixing information for conversion from lifetime to `B(E2)` or `Q_t`.

## Analysis Chain

Singh 2016 uses LINESHAPE Monte Carlo histories at `0.002-ps` time steps and fits forward/backward gated spectra simultaneously. Ziegler and shell-corrected Northcliffe–Schilling stopping powers are treated as alternative prescriptions; central values are averaged and the larger uncertainty retained.

## What It Can Establish

- source-specific mean lifetimes or limits in the line-shape sensitivity window;
- side-feeding-sensitive `Q_t` after a rotational conversion;
- angle/stopping-prescription consistency and contaminant diagnostics.

## What It Cannot Establish Alone

- intrinsic γ softness/rigidity, microscopic configuration or nuclear chirality;
- a unique lifetime if side feeding, stopping or contaminant structure is underconstrained;
- partner-band electromagnetic equality from a single measured sequence;
- direct intrinsic `Q0` without rotational-geometry assumptions.

## Known Limitations

Thick targets broaden the production-depth/velocity distribution. Stopping powers, side-feeding cascades and long feeding times can dominate the systematic budget. A line that is fully shifted or shows no significant angle-dependent shape yields only a limit or complementary RDDS bracket.

[[wang-2023-experimental-studies-nuclear-chirality-china]] adds a review-level statistical caution: the common practice of varying one nuisance parameter at a time and adding lifetime shifts in quadrature does not represent correlations, asymmetric intervals or physical limits. 该二级入口的历史边界保留；现在原读的[[sun-2023-bayesian-dsam-31s]] SUN23-6–11核了actual2022v2 primary的priors、Gaussianlikelihood、GP/MCMC与quantile/6390限制。完整SI/实际input仍未得，不能把review赞词当完整precision认证。

[[bark-2024-investigations-nuclear-chirality-ithembalabs]] describes the AFRODITE use of forward/backward line shapes and COMPA/GAMMA/SHAPE Monte Carlo histories that include slowing, feeding and statistical/collective cascades. Its `106Ag` example is secondary to the original Lieder 2014 experiment and should not substitute for that source's fit/systematic details.

[[jensen-2001-165tm-h9-2-configuration]] provides a classic Nordball DSAM example: four angle-specific γγ matrices, Au/Pb backings, Monte Carlo recoil histories, Bateman side-feeding cascades and a fitted effective `Qs` are used to obtain `Qt` for `165Tm` bands. The reported `Qt` comparison is therefore tied to the stated stopping, feeding and rotational-model assumptions.

## 质心位移与恒定Qt提取：Riley2001

[[riley-2001-global-lifetime-a135]] RI01-1–5给出centroid-shift DSAM的直接例子，不只使用完整lineshape。其`F(τ)=[Eγ(θ)−E0]/[E0 β′cosθ]`中β′是mid-target recoil velocity；实际producer/数值未给，不能用束流能量代填。173 MeV 35Cl+105Pd、Au backing、97HPGe和Microball是采集条件。底部stopped门的前角31.7°/37.4°、后角142.6°/148.3°，moving double gates与90°谱、最高spin门是不同选择。

FITFTAU以带内恒定Qt拟合F曲线；默认`Qt(sf)=Qt(band)`，不等于τ相等。高spin上方门针对下方态侧馈，五个b注pair的Qt增加约8.3–12.1%；135Sm c注另用`τsf≈1.2τband`时序假设，不属于相同gate比较。不要把band-average Qt当每条transition独立测得τ（RI01-3/4/7/8）。

正文称阻停加侧馈可给absolute Qt附加15–20%系统误差，相对accuracy约5–10%；Table I caption称stopping-only 10–15%。作用范围及概率解释未统一，缺Σ时不将它们独立quadrature，也不把摘要“free from common systematics”当剩余误差为零。共同条件有助相对比较，不能直接推出所有点完全相关或各核素独立（RI01-5/9）。

### 原始重拟合的输入边界

进入真实L4需要逐ring/gate谱与centroid/calibration、事件交集和共同Σ、反应点/β′定义、靶厚与slowing histories、门污染/效率和feeding模型、E2/branch/geometry及FITFTAU版本/输入。现有表只能支持已发表参数的角色审计与条件敏感性；不能生成Pr136新τ、补原始CI或取代Laird2002最终版本。

## 同束靶的通道速度与可见带顶归一

[[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-16/17把粒子tag和v0输入放到实际证据链：GASP+ISIS的α veto/选择分开134Nd与131Ce近简并峰；Nd β0=.0202(2)，Ce α3n发射动量由MC修正为.0192(2)。共用束靶/backing不代表可以共用未经通道修正的速度，tag效率/污染仍需实际response。

保持同Ce平均发射速度却误借Nd β，按F定义归一会乘.950495（约−4.9505%）；这是条件敏感性，不是证明原作者用错值或给出τ/Q0偏差。原文带顶可见F<1还受thin-target已知而当前厚靶未见的更高跃迁和慢侧馈影响，不能无条件以观测最高点强制F=1校速度。其β值来自明确计算/MC并以高线shift交叉检查，不是由Ftop必须等1得到。

该文高门统计不够，最终对带内所有组合双门的sidefeeding effective intensity作选择修正，并用二维χ²拟合Q0/Qsf；缺实际grid/Σ不能复现误差或把单一/两段Q0的接受程度定量化。Band3表格alternative rows及Qsf文字范围歧义保留（PE98-5/6/11/18）。

## Sources

- [[riley-2001-global-lifetime-a135]] RI01-1–9/14：centroid shift、恒定Qt、门选/feeding、systematics与L4边界。

[[wadsworth-1977-61ni-levels]] is a historical `61Ni` DSAM example: centroid shifts at several beam energies are converted to attenuation factors/lifetimes with explicit stopping/feeding caveats.

- [[singh-2016-lifetime-131ce-133pr]]: explicit LINESHAPE/stopping/side-feeding audit for `131Ce`.
- [[li-2004-lifetimes-131ce]]: earlier `131Ce` DSAM lineage.
- [[petrache-1998-highly-deformed-lifetimes-131ce-nd]]: shared-systematics HD-band DSAM comparison.
- [[wang-2023-experimental-studies-nuclear-chirality-china]]: secondary review of DSAM uncertainty practice and pointer to correlated Bayesian/MCMC treatment.
- [[bark-2024-investigations-nuclear-chirality-ithembalabs]]: AFRODITE/COMPA-GAMMA-SHAPE overview and secondary `106Ag` line-shape counterexample.
- [[jensen-2001-165tm-h9-2-configuration]]: Nordball DSAM, `165Tm` `Qt`, side-feeding and stopping-systematics example.

## Related Methods

[[recoil-distance-doppler-shift]], [[doppler-correction]], [[transition-quadrupole-moment]].

## Evolution Log

- 2026-08-11: created from the Singh 2016 corpus on-touch audit with stopping and side-feeding boundaries explicit.
- 2026-08-11: added Wang 2023's correlated-uncertainty warning while retaining the un-ingested status of the cited Bayesian DSAM method.
- 2026-08-11: added Bark 2024's AFRODITE simulation-chain overview and original-source boundary.

- 2026-10-15：方法定义扩展为包含centroid shift；新增Riley2001的恒定Qt、门与误差预算，不改旧source/review状态。

[[lifetime-strength-audit-165tm-136nd]]按J01-6/7/8与MU08-15/16分开三步/五步feeding、5fs/2fs与两种stopping预算；fulltailbelowgate只控制一类selectionbias，不消sidefeeding。新11行/9行换算为条件审计，不是原谱重拟。

本次原件链：[[jensen-2001-165tm-h9-2-configuration]] J01-6–10与[[mukhopadhyay-2008-136nd-transition-rates]] MU08-15–17；实际逐角谱/response/Σ仍需匹配原producer。

## Bayesian DSAM的primary合同：31S

[[sun-2023-bayesian-dsam-31s]] SUN23-6–10：positivelifetimeprior、Eγ/bkg/sppriors和PCA/GP+Gaussianbinlikelihood是实际分析选择，restrictivenuisancepriors会强烈影响后验。τ–sp的负相关是原两long-lived态的报告，不裸迁给其它能区/体系。若emulatorΣ随参数变，完整Gaussian的normalizer也相关；原Eq3approx与actualtailoredcode需分开，未凭print判实验失败。

SUN23-11的6390态无finiteconstraint；20fs及Γ>33meV是条件应用链，不能当TableI第五项90%upperlimit。SUN23-12/13显示由总τ得到的B(M1)另含USDB E2partialrate扣除；它不是独立测得纯M1或δ。当前[[lifetime-strength-audit-165tm-136nd]]增加该链作方法对照，不修改两原实验数值或宣称L4原谱已重拟。

[[madai-2015-distribution-sampling-likelihood]] MDA15-2–8原样组件对variableΣ/normalizer、默认flag与ordinary/gradient-output两API作条件反例；fixedΣ是必要反证。它不认证[[sun-2023-bayesian-dsam-31s]] actualtailoredcode或原CI失效；需papercommit/config/实际response与数据。

SUN23-17–22的publisherSI已原读：见[[sun-2023-bayesian-dsam-31s]]。它补target/DAQ/逐态αgates与posterior图，不给actualGP/config/draws；Fig13不是额外90%limit表，图轴也不自动给priorhardcut。1/2+态的A2需先核其物理对象/帧，不能直接叫已测alignment。

[[spinhalf-angular-nuisance-response-contract]]按SUN23-20/23/24区别核rest发射prior与lab/responseA2：Ji1/2在末态全求迹的parityconservingEM singles核内无P2/linearP，但后续γgate/boost是必要反例。未定Sunactualframe前不机械置零或推τbias；alpha初态tag与末态postselection分开。

## finite寿命与upperlimit的实验反证：15O6792

[[schuermann-2008-15o-6792-dsam]] SCH08-3–10给实际同Ge密角扫描、gain/geometrycombinedfit与primaryF限制的反证：旧data点可相容，但原finiteτ提取未获新数据支持。Eq1的P=.987为Doppler有限尺寸修正，非偏振P。F.99(.01)与τ<.77fs的上限需source的SRIM/density/σ语义，不能自动转90%limit或与Sunposteriorquantile同口径。

SCH08-11/12的条件算术表明省P可造成apparentF.97713，以及两个reported中心的独立SDcontrast并非作者>5σtest。原centroidΣ/MCcurve未得，不从summary造重拟。TableII复用旧F检验analysis，非新增两态测量；5181同runcompanion也共享systematics。

J01-12–18的[[jensen-2001-165tm-h9-2-configuration]]主线将直接DSAM两band、mixing派生两band与E1绝对提取同标尺关联；详[[lifetime-strength-audit-165tm-136nd]]。constantQt跨spin是带条件迁移，有模型支持不等独立全spin测量；crossingmodel的evenbaseline/增益反证不因Qt较大消失。

[[nndc-2022-s31-mixing-lifetime-reference]] S31-2–5/9/10给Sun1248模型E2扣除之外的旧MRcompanion，含真实双根/RUL选择及half-life/mean同源字段。官方数据可收窄输入，不能自动替代新DSAMactualresponse/priors/Σ，或用adoptedpreferred值重造唯一δ。

S31-11的旧RISINGcluster/Miniball两预算还提示：meanτ/half-life及stat/sys组合必须同口径再比较，不能把同paper的两个detector和其单位换算重复当独立lifetime证据。


## 独立阻止输入先核对象与能区

[[iaea-2026-stopping-s-au-o-ta-records]] ISP26-1–9保存实际官方S/Au、O/Ta表。电子截面−dE/dx=nS不含完整核散射/速度投影；63实验行与329SRIM模型点分列，literal百分比误差无共同Σ或统一置信定义。S/Au六组全32S，O/Ta全无15O且最低实验能量.1167807MeV/u。Ep.318MeV的15O质量近似起点约.001424MeV/u，即使声明总γ能量8MeV宽松界也仍有约46.55倍能区缺口。这是覆盖控制，不是新停止程/F/τ计算。

Sun实际sp中心是Geant4使用的database，不能将当前IAEA附带SRIM2013曲线认作其producer或以同源模型比值直接更新10/20%Gaussian先验（SUN23-6）。Schürmann用SRIM2006投影历史与15N/Ta上游控制；现今电子表不补原collision/多项式/材料/Σ（SCH08-9）。实际下一输入应是matching isotope/velocity/material的primary方法、核阻止扣除和共同误差，而非按表行数缩小系统预算。


### 厚靶参考的局部量与共同归一

[[bethge-1966-heavy-ion-stopping-charge-states]] B66-3/5/9/10给更具体的输入门：原反向散射法Eq3要求入/出路径阻止近似相同。放开为两个局部量，在固定K与正几何g下只识别Seff=(KSi+gSo)/(K+g)，单谱bin不能拆两路径；不是任意强能变轨道的公式。作者束流计量N0偏高使直接S整体偏高，25%不当逐点独立σ。共同scale模型的Cov外积和有效电荷二阶矩只是条件推导，无原Cov恢复；这类电子表仍不替完整DSAM速度投影。


### Geant4模型、表和查询顺序也是停止本领合同

[[geant4-2026-ion-stopping-component-contract]] GSI26-1–10保存新actualSDK11.4.2/G4EMLOW8.8组件。defaultstandard/option4/default与external分别选Bragg/LindhardSorensen/ParamICRU73；只说Geant4不能唯一指定曲线。totalenergy、E/A与模型proton-mass-scaled energy要桥接；电子DBL_MAX cut查询与1keV restricted、核阻止开关及productionrange cut分列。calculator已调用step correction，不能重复加修正或只取模型裸DEDX。

在声明的external低能15O/Ta API控制中，首次range建表改变chargeSquareRatio，使首次返回值只约后续值.095988倍；原生重复、源码只插诊断的副本与严格重放一致。它限制该组件如何取值，不认证Sun的版本/physicslist/callingorder或真实transport偏差。原63编译行对三模型比值只是matching-isotope组件比较；未恢复实际材料/轨迹/Σ，不从此设新10/20%先验或寿命CI。


### API异常须另作native路径控制

[[geant4-2026-ion-stopping-component-contract]] GSI26-11–15进一步核实际AlongStep当前couple、track charge和step/cut。指定15O/Ta、nuclear/fluctuationoff、仅前两步的人为控制中，external首event首步deposit约为次event同起点的.0959881倍，option4对照为1；步骤能量账本仍闭合。短步.1nm未建range也出现，源trace定位首次高能transitioncache覆盖q²，不把所有首次状态问题只归于range积分。

这些native控制只扩大软件条件证据，不等完整slowing、F(τ)、任意geometry或Sun真实事件验证。不能从局部ratio直接计算实验τbias；rawStepPoint charge与model有效q²也分别保存。原SDK未patch，重放保留首次与后续状态。


### 粒子门能量须映射回反应顶点

[[sun-2023-bayesian-dsam-31s]] SUN23-27–31区分Si的residual E、DeltaE、实际gate表达式与vertex动能。原Fig1 E位于1mmSi，DeltaE位于87µmSi；caption“47MeVgate”不能替排序代码。反应depth前beamloss、alpha出靶/死层/两Si沉积与实际角接受都需fold。以无损128MeVvertex模型算2234高root49.48–52.21而不是47±1，只反证省掉这些层的等式，不给新loss或τ偏差。

固定角无损dEx/dTalpha约−.555，2MeV窗映约1.11MeVEx；真实gate/角平均/材料响应与σ不同。SDK质量或源Q的打印细节并不能补这个实验映射合同，source/SI/compiledrecord也不是三次独立校准。


## 同设施DSAM输入仍需逐层匹配

[[kirsebom-2016-23mg-dsam-lifetimes]] K16-1–16给独立reaction采集但共享设施/方法的实际例：alpha出Au约4MeV后才形成测量门，nominal8°点接受随束斑/散射扩展，植入层的He贡献与swelling同时进入Eq4。不能将其4MeV、100/500µmSi或2.4MeVgate补给Sun的32S实验。TableI粗略δE/E不当独立GaussianΣ，7787上限<12fs并未裁决rate争议。

[[simdsam-2015-public-dsam-code]] SD15-1–15可实际读/运行原表达式组件，却仍无原experimentalROOT/fitCov/exactjob：default表/束斑/效率插值与正文不同；printed及code clock均γds/v，均匀半径与均匀圆盘不同。成功重放代码不等这些物理合同通过；source代码表传播也不能直接套当前Geant4 runtime的首状态问题。下一输入应优先匹配原job/response/计数，再评估任何实验τ影响。


### MODEL联合事件包只关闭格式与producer入口缺口

[[simdsam-2015-public-dsam-code]] SD15-17–21实际从原eventmain生成64个MODEL已检测alpha-gamma对，并在新目录重放ASCII/ROOT Float32流；这为后续输入合同提供可检查接口，不提供原experimentalhistogram/fitCov或实际job。诊断TH2全bins计数能恢复6820次模型proposal，default积分仅5427；info积分15是τpayload，不是事件数。

64/6820不是实验绝对效率：当前角提议域被截断、gamma效率逐能量归一，且反应channel已预设。旧clock/radius/输入物理问题及runtime libUnuran加载警告仍保留，不能以输出完整来宣称原实验τ/CI已验证。下一真实输入应是原analysis/data或对应材料/校准primary，不能靠更多模拟history代替。


## Fractional Doppler与line-shape是不同观测链

[[jenkins-2004-23mg-fractional-doppler-rate]] J04-1–14以七角centroids/最大位移构造fractionalshift，再经模型得到τ；高unboundfeeding直接为作者假设。它与K16alpha-tagged line-shape是不同采集/响应，不能以同叫DSAM互补缺少的stopping/feeding/Σ。J04表中τ10(3)与omega1.8(.7)分别是本次寿命和旧评价强度，不能算两项新独立结果。

旧directgamma阈值漏掉2316.9keV分支的例子还说明：由总τ到Γgamma/强度需要particle/radiativebranch及实际ε/gate。理想3MeVstep下58%visible→1.724total/visible只是声明的inventory控制，不是原4meV上限或置信区间重放。共同Q、gamma校准及能量definition的Σ未得时，不强配quotederrors或按近能量合并母态。

## 用总寿命推共振强度时的额外输入

[[nndc-2021-mg23-lifetime-strength-reference]] M23-4/8/9/13/14给实际反例：自旋候选、另一gamma支和更新omega必须逐源匹配。总τ只给Γtotal；两通道时omega=gΓBp(1−Bp)，同Γ/omega常有互补Bp两根，固定中心也可能无根。它说明输入条件不相容，不自动排自旋/实验或给CI。half/mean、LT与原CL、评价平均值/原measurement都要分开。

## 独立capture companion的“无绝对停止”也有条件

[[sallaska-2011-na22-absolute-resonance-strength]] S11-2/8/9/11/12/17说明：完整积分可消除归一能移核的位移依赖，前提是扫描完备、全部活动区照射及NT/束密度稳定有据。弱模板伸缩、有限尾、energyloss仍有stopping/response；这类capture强度不能自动替DSAM的v(t)、feeding或其原协方差。强度与总τ组合前仍逐项核spin、branch和共享输入。

## 寿命companion的frame合同

[[sallaska-2010-na22-letter-version-contract]] S10-3/4/5示范实际公式审计：同质量因子下lambdaLab²与lambdaCM²不能凭符号互换，NR有lambdaCM²=r²lambdaLab²。即使条件推导清楚，仍要原分析程序/版本证据才能修改实验率；未读正式erratum不能给它指定更正内容。该合同与DSAM中lab/proper时钟一样，文字检查不等实际fit偏差。

## 事件级速度差也保留停止和联合能量输入

[[fougeres-2023-mg23-velocity-difference-lifetime]] F23-3/4/5/7/8/18用α两体运动学给βreac、γ反演βems，降低未知初速度/feeding影响；仍有SRIM能损/初始剖面、角/能量校准和同Ex门下γ/particle响应。τ/Eg0共同free、profile按integral归一，公开data/source要matching才可谈CI；这个方法的优势不等任意finitegate下全部feeding/角度系统为零。

## 已公开producer仍需原输入和调用合同

[[evasions-2023-public-release-native-readiness]] EV23-5/6/7/8/13/14把build、原方法返回、实际停止表与paperfit四层分开：build0不等physics/CI通过，status1也未必表示表已正确加载。实际原输入/native失败可定位readiness，不能直接外推作者实验无效；原source/数据不改，修正版必须另名。

## 同作者primary也能修订代码审计的解释

[[fougeres-2022-thesis-evasions-response-contract]] F22-2/10/11/12/13/15表明：genericpublicinput的19mm有实际装置依据，不能仅凭paper简写判geometry错；responseσ/FWHM/bin和SNR来源须明确，benchmark归一/fit窗口不可替论文其它case。source/code/实验结果逐项核而不把故障数量当证据权重。

## 直方图比较的接口名不能替代统计合同

[[root-2026-chi2test-option-contract]] RCT26-2/3/4/5/8/9：Chi2Test的LL静默未消费、自动UU/UW/WW依误差状态，属于两hist同质性比较；Chisquare(TF1,L)另有Poissonratio接口。matchingproducer必须记录范围/bin/normalizer、Sumw2与MCstats、零bin、自由参数与sharedCov。EVASIONS示例调用inactive，native组件不是原paperjob或τCI认证。

## 原校准与互逆计算的物理边界

[[fougeres-2022-thesis-evasions-response-contract]] F22-58/59/62/63/64/68/71/72：Bρ↔E两个错误物理表达式仍可互逆，不能用roundtrip单独认证动量/速度合同；source/模拟校准、PSA尺度派生角核及实际particlecleaning也不能合称一个测得response。高能eff的source+MC角色与精确coeff/自然log单位需match原job。当前native只组件，未知papercal/Σ不从数值差直接重报τ/BR。

## 分支表与强度表不是相同的完整库存

[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-9/12/13/14/15/19：同parent的E1/带间link也会改变partialτ，thin/backed强度来源由实际reaction/分析合同确定；只取rate表两列可制造B/Qt差。无shift给的roughlifetimebound仍依sidefeeding与响应，不能裸转小shape/统一CL。该文的SFQ是effectiveτ参数，不代静态Qs或bandQt。

## 由B到Qt之前先固定电荷算符和转轴

[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]] F01-D17-2/3/4/5/6/9：τ/branch给的B只是指定transition的率强度。potentialq与chargeQ、球张量与conventionalQ0、static与transversecomponent、finiteCG与highspin近似须逐项明确。axial模型已有sin⁴θ方向因子，单B不同时决定intrinsic矩和axis；实际PAC/TAC约束要加入，不能用自由取向witness替实验模型。MU08的候选G数值相合仍不是actualQtproducer认证。


## 侧喂养的积分角分布与时间响应

[[draper-1970-gaussian-substate-side-feeding]] DR70-D17-1/2/3/10的purestretchedE2完整trace及积分混合不提供各路径时间kernel；表1smoothedfeeding不能直接作为γγ门后/时间slice的权重。将固定alignment与DSAMfeeding分别设定前，需检查samegate逐路径取向/时间是否可分离，并保留强度/取向/response的共享Cov。原p216Gaussian数值有literal边界，新CG复核只是条件计算，不修正真实τ/δ。


### 同边际与联合响应的区别

[[feeding-time-alignment-joint-response]]从[[draper-1970-gaussian-substate-side-feeding]] DR70-D17-1/2/10明确另作解析design：两个正的CG可实现路径交换time-alignment关联时，总时间密度与积分ρ相同，逐角Doppler速度矩仍可不同。actual多角line-shape/feeding标记及jointΣ才可能约束该耦合；design差不当当前核τbias，90°point不以零shift倒推F。

## Day18 Ag106：同母态ratio的有限抵消

[[rather-2014-ag106-transition-rates]] RA14-3/4/6给新的完整primary实例：1fs/5000histories/shell-correctedNorthcliffe、逐级feeding及12的abovegate，不可迁成其它原件的同producer。固定branch/ICC/multipole时同母态BM1/BE2消共同τ，再作跨带/跨spincontrast；不消line-specific intensity/δ/response，不生成独立实验CI。RA14-7/8的quotederror与prose/table边界保原。RA14-9/10将相似B(E2)与同meanfieldshape模型解释分列；Liederbody未得，不称两primary已一致或冲突已裁决。


## RDDS/DDCM作为DSAM的正交时间合同

[[klemme-1999-lifetimes-134nd-neighbors]] KL99-D18-1/2/3/4来自本session定向原读PDF2–4，承认既有Day13阅读。距离/shifted-feedinggate/导数给DSAM以外的时间响应，但约1.1ps Au减速仍使短τ需要stopping修正；六个非空tcorr因子1.181–1.255不是统一比例。固定branch/ICC/几何，声明将修正量减半的chart中12S1/10S1和8g/6g的Qt比分别仅变+.563%/+.584%；不把这一个chart当原CI/完整系统envelope或106Ag独立实验。实际输入/Σ与samelevel身份才决定companion是否增加独立约束。


## 寿命与跃迁强度的非一一对应：135Nd/136Nd对照

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D18-1/2与[[mukhopadhyay-2008-136nd-transition-rates]] MU08-D18-2展示了DSAM分析中必须严加区分的核心命题：
- 能级寿命相等不保证跃迁强度相等（136Nd中带间B(E2)相差达5倍）；
- 跃迁强度近同不代表能级寿命相同（135Nd低自旋区B(E2)相近但寿命相差2倍，由偏分支比与能量5次方补偿）。
在DSAM lineshape分析中，必须建立完整的衰变纲图、分支比与内转换修正，才能将提取的τ安全转化为B(Eλ)或Qt。


## 相对跃迁强度提取中的混合比双根依赖

[[amro-2003-wobbling-167lu]] AM03-D18-1 进一步扩展了强度提取的误差链：即使在消去绝对能级寿命的相对比值 $B(E2)_{\text{out}}/B(E2)_{\text{in}}$ 中，跨带混合跃迁的 $E2$ 成分比重 $f_{E2} = \delta^2/(1+\delta^2)$ 仍是决定性输入。若角分布测量存在双根且缺乏线偏振独立裁决，不同根可导致提取强度发生近两个数量级的系统性偏离。


## 侧馈参数模式切换对Qt自旋趋势的系统性偏差

[[singh-2016-lifetime-131ce-133pr]] SI16-D18-1 揭示了DSAM分析中侧馈参数形式的影响：若在同一自旋链中将低自旋的固定时延参数 $\tau_\text{SF}$ 切换为高自旋的转动级联参数 $Q_\text{SF}$，拟合程序在分配能级寿命与未观测侧馈时长的权衡会发生系统性跳跃，从而可能在 $Q_t$ 序列中制造出统计不显著（$<1\sigma$）但视觉明显的“形变演化”假象。


## 单调中心与交错归因的诊断范围

[[suzuki-2008-lifetimes-103rh-104rh]] SZ08-D18-2–4保真实TableIII和作者“BM1下降、BE2弱交错”的解释。它不等于通过统计检验得到百分之百的因果分解。新声明S[x]=ln x_next−2ln x+ln x_prev，精确有S[M1/E2]=S[M1]−S[E2]；单调BM1中心仍可有非零S。103Rh的三者约−.16034/−.83900/+.67866，104Rh也两项皆非零。

此任意中心曲率诊断不唯一代表物理交错，不给显著性/CI，也不反驳作者的定性模式；其提示必须声明趋势/函数与协方差，不能从“单调”推任意去趋势oscillation零。正宇称对象与[[kuti-2014-multiple-chiral-doublets-103rh]]负宇称候选分开，B由同τ/branches导出仍同源。

## 相对强度提取的单点数据与唯象模型定标边界

[[lv-2022-transverse-wobbling-136nd]] LV22-D18-1 说明：在评价多能带跃迁强度的模型符合度时，必须检查理论算符的有效电荷或二阶修正参数是否已被唯一的实验强度点所定标。当模型自由参数恰好由该实验点固定时，理论曲线展现的良好符合属于自洽拟合，不能被当作无参先验验证。


## 混合比解翻转引起的跃迁强度塌缩效应

[[matta-2015-transverse-wobbling-135pr]] MA15-D18-1 与 [[lv-2022-evidence-against-wobbling-135pr]] LV22P-D18-1 的对比确立了跃迁强度审计的警示边界：当实验从单纯角分布的 $|\delta|>1$ 解修正为结合线偏振的真实 $|\delta|<1$ 解时，带间跃迁的 $E2$ 份额可从 $70\%$ 骤降至 $12\%$，带间强度比 $B(E2)_\text{out}/B(E2)_\text{in}$ 遭受整整 **7 倍的断崖式塌缩**（0.843 降至 0.12）。这再次证明：跃迁强度的可信度完全受制于多极混合比解的唯一确定性。


## 相对强度提取中的能量五次方放大因子

[[rojeeta-devi-2021-multiphonon-transverse-wobbling-133ba]] RD21-D18-1 揭示了跃迁几率公式中能量因子的巨大作用：当跨带跃迁能量低于带内跃迁时，$(E_\text{in}/E_\text{out})^5$ 因子可造成数倍的强度放大（如 $^{133}\text{Ba}$ 中放大达 5.43 倍）。在评估带间跃迁的四极集体性增强时，必须剥离该五次方相空间因子，避免将能量差异引起的物理率效应误解为形变算符本征矩阵元的反常跃变。

## 混合比双根引起的多极强度全面倒转：从横向到纵向wobbling

[[biswas-2019-longitudinal-wobbling-133la]] BI19-D18-1 进一步拓宽了多极混合比根敏感性的审计范式：不仅在横向wobbling（$^{135}\text{Pr}$）中，在纵向wobbling（$^{133}\text{La}$）中，所谓的带间集体四极跃迁增强与磁偶极压低也完全依赖于对大混合比解（$|\delta| \sim 2\text{--}3$）的人为采纳。一旦选择退取向展宽下同样相容的小解（$|\delta| \sim 0.35\text{--}0.4$），$B(E2)_\text{out}/B(E2)_\text{in}$ 即发生6至7倍的全面塌缩，而 $B(M1)_\text{out}/B(E2)_\text{in}$ 反向暴涨5至9倍，使物理机制彻底从集体形变进动倒转为单粒子磁偶极退激。这确立了多极跃迁几率审计的通用铁律：**未获独立物理裁决的双解，不能作为任何新型集体运动模式的判决性证据**。

## 混合比分支敏感性与有效g的定标范围

[[timar-2019-transverse-wobbling-105pd]] TI19-D18-2–6：固定其余输入，以作者991/1034 DCO小支.59/.40替代大支1.8/2.3，条件RE2为.223021/.098403，RM1为.509517/.482595。原文同实验偏振支持大支；这些替换不能当已测唯一小解。994的.35缺原文明印出处，排出此次有源计算。

原q=.36缩放的是g_eff=g_nu-g_R；定标21/2→19/2 δ，作者给出PRM未含scissors mixing的理由。固定波函数/Q0时幅度乘.36、强度乘.1296（逆7.716），不同于所有M1算符普适缩7.72倍。新mixed-boundary-result-047的26项检查验证有源词项与条件分解，不拟原polarization likelihood或CI。[[nomura-2022-questioning-wobbling-ibfm]]保替代解释，不由任一模型定标单独判模式。

## 跃迁强度的单粒子极限与内转换系数的判决性检验

支持方原件[[sensharma-2020-longitudinal-wobbling-187au]] SE20-D18-1与反方[[guo-2022-low-spin-wobbling-187au]] GU22-D18-1应成对回查；下段既有强措辞只记录该争议的审计解释，实际多极解与统计输入仍需逐源核验，不能由程序成功或与模型接近直接判决。

[[guo-2022-low-spin-wobbling-187au]] GU22-D18-1 确立了跃迁几率审计的最高判决准则：在评估高自旋或低自旋集体增强时，相对分支比往往受单粒子本征态几何跃迁几率的欺骗。当核芯具有上百Weisskopf单位（W.u.）的内禀集体性时，若错误采纳角分布的多极混合比大解（$|\delta| > 2$），会将原本仅 $1\text{--}2$ W.u. 的单粒子轨道间退激人工放大至近百W.u.，制造出虚假的超集体“wobbling声子”。此时，由内转换电子谱仪测定的内转换系数 $\alpha_K$ 以及高信噪比线偏振度 $P$，能够绕过取向参数 $\sigma/I$ 的简并，直接提供对多极性质的刚性裁决。在跃迁强度从相对比值折算为绝对强度时，必须校核是否触及单粒子Weisskopf极限。

## 多声子激发态跃迁拓扑的谐振子选择定则审计

[[chakraborty-2020-multiphonon-longitudinal-wobbling-127xe]] CH20-D18-1 确立了在评估多声子集体运动（如两声子wobbling）时的拓扑判据：三轴转子中真正的多声子谐振进动（$n_\omega = 2$）要求其向基带（$n_\omega = 0$）的跃迁满足 $\Delta n_\omega = 2$ 弱退激选择定则，且以伸展四极跃迁（$\Delta I = 2$）为主。若实验观测到的二声子候选带向基态带的退激反常地由非伸展（$\Delta I = 0$）跃迁主导甚至强度超过伸展跃迁，则表明该能级序列源自轴对称核芯的准 $\gamma$ 振动带或单粒子混合，而非真正的多声子三轴旋转谐振子进动。

## 弱显著性线偏振对混合比解判据的有效度边界

[[mukherjee-2023-transverse-wobbling-151eu]] MU23-D18-1 揭示了由低显著性偏振数据导致的多极强度灾难性放大假象：当线偏振不对称度 $\Delta$ 的测量显著性低于 $2\sigma$（例如在 $^{151}\text{Eu}$ 中仅为 $1.09\sigma$ 与 $1.60\sigma$）时，它在统计上完全无法提供区分 $|delta| < 0.2$ 小解与 $|delta| > 3$ 大解的判决力。在此类边缘显著性下若轻率采纳极大解，会将真实 $B(E2)_\text{out}/B(E2)_\text{in}$ 人为夸大60倍至600倍之巨。因此，在跃迁强度审计中，必须校核偏振测量本身的绝对信噪比与统计显著度，不能仅凭测量值的代数符号做出结构物理定论。

## 历史文献角分布数据重解与解分支挑选的证据审计

[[chakraborty-2024-possibility-wobbling-129ba]] CH24-D18-1 规范了文献重分析数据的采信准则：在缺乏新探测器阵列数据、新寿命测量或全统计事件支持的纯文献重分析中，将早期实验已采纳的特征伙伴解（$|\delta| \approx 0.8$，$M1$ 主导）替换为角分布另一极大解（$|\delta| \approx 2.0$，$E2$ 达 $80\%$），若仅依托统计显著性接近 $1\sigma$ 的历史线偏振测量，属于高度模型假定的唯象重标。在建立核素与带结构卡片时，应如实标注解分支争议与偏振统计弱性，防止历史已证伪或已解决的特征伙伴带被无新证据地重新泛化为wobbling。

## 多声子谐振标度检验中的单线敏感性与无偏振依赖

[[jensen-2002-second-phonon-wobbling-163lu]] JE02-D18-1 揭示了在检验集体声子谐振倍增律（$B(E2; n=2 \to 1) \approx 2 B(E2; n=1 \to 0)$）时的数据拓扑脆弱性：多声子态由于激发能高、粒子蒸发退激退火剧烈，通常仅有单一甚至极弱的分支线可供测量。若关键连接线（如 $^{163}\text{Lu}$ 中的 476 keV 线）因统计限制无法获得线偏振检验，则大解所给出的‘2倍谐振标度’与小解所给出的‘近30倍强度暴跌’在纯角分布/DCO数据上完全简并。在断言观察到多声子玻色子激发前，必须严格披露该标度是否受制于无偏振约束的单线混合比双解。

## 同位素类比推断与循环假定对电磁证据链的侵蚀

[[hartley-2009-wobbling-167ta]] HA09-D18-1 与 [[schonwasser-2003-wobbling-165lu]] SC03-D18-1 揭示了在复杂核结构模式归属中‘类比推断’替代‘实验测量’时的证据污染链条：当某一基准核（如 $^{163}\text{Lu}$）确立了某种多极混合比（如 $90\%~E2$）后，后续在同位素或邻近同中子素实验中，往往由于探测统计不足而直接援引该比值作为已知先验，或以此排除双解中的小解。更严重者，直接基于该援引假定算得四极跃迁增强，并反向声称‘排除了不支持该增强的竞争物理模型’。在科学证据审计中，必须将‘独立实验提取的多极混合比’与‘援引外来假定算出的名义跃迁几率’进行绝对隔离，杜绝此类循环论证转化为实验定论。

## 跃迁四极矩斜率显著性与阻停/侧馈系统误差包络

[[babra-2019-deformation-change-136sm]] B19-D18-1 与 [[singh-2016-lifetime-131ce-133pr]] SI16-D18-2 规范了在束DSAM寿命测量推导跃迁四极矩 $Q_t$ 自旋演化时的判决准则：在评估高自旋态形变是否‘减小’或‘塌缩’时，必须进行加权最小二乘线性回归，检验斜率偏离零的显著度是否达到 $3\sigma$ 硬指标。若显著度低于 $3\sigma$（如 $^{131}\text{Ce}$ 的 $-0.64\sigma$、$^{133}\text{Pr}$ 的 $-1.68\sigma$ 或 $^{136}\text{Sm}$ 的 $-2.72\sigma$），且变动幅度完全落在未引用的 $10\%\text{--}15\%$ 阻停本领系统误差带内，则在统计学上不能拒绝常数形变假定。同时，必须特别核查侧馈平均时延 $\tau_\text{SF}$ 是否存在跨数量级的跃变，防止未隔离的慢馈入成分在拟合中被补偿为假象式的形变演化。

## wobbling四极电磁判据与两准粒子M1主导衰变的定义冲突

[[chen-2019-transverse-wobbling-even-even]] CH19-D18-1 规范了评估多准粒子系统中声称wobbling模式时的电磁判别底线：在偶偶核两准粒子带（如 $\pi h_{11/2}^2$）或奇奇核四极能带中，当带间连接线的多极混合比仅给出 $25\%\text{--}28\%~E2$、而 $M1$ 份额占到 $72\%\text{--}75\%$ 时，该跃迁在物理上属于强磁偶极退激。若为了将其塞入wobbling框架而放宽‘$E2$ 必须占主导’的基本假定，将导致wobbling与普通未偏爱特征伙伴带在实验上无法区分。在此类体系中，必须依托DSAM或RDDS提供绝对能级寿命 $\tau$ 并独立提取绝对 $B(E2)_\text{out}$（验证其是否达到数十Weisskopf单位），否则不能仅凭相对分支比判定为偶偶核wobbling。

## TiP逐线样本与跨核外推边界

[[lv-2021-tilted-precession-135nd]] LV21-D18-2–8核TableII：旧7.4%平均混入410.2带内与518.3 TiP2→TiP1。五条已知δ的TiP1→D1为518.1/566.8/618.3/566.0/560.7，声明无权中心分率均值约8.305%；仍不是全部TiP链接的实验总体平均。560.7 AP空，566.0 AP=-.081(.072)只约1.13个打印误差，不能称全线显著负。

原TiP为该核能谱、连接与PRM综合解释；没有同response/相位/组态/Σ，不能将其它核的条件small-δ替根都认证TiP，不能“否定全A130 wobbling”。新parent-branch-exercise-result-048保正确样本身份与缺项，未对原角分布/偏振重拟合。

## 74Br列身份、有限寿命与多极性例外

[[guo-2024-chiral-wobbler-74br]] GU24-D18-2–9纠正TableI列：7+的1.79ps属于Band3，不是Band2；本Letter矩阵15个有限值与5个上限，空栏/上限不能作新中央值。Band2有限8–12+为.62/.53/.43/.25/.10ps，Band3有限7–10+为1.79/1.21/1.10/.38ps。

SI Band2→1的527.2/959.5线δ=-.63/-.7给E2中心28.4/32.9%，反驳“全线<10%”；Band3→1低spin600.3 δ=-.5给20%，并非全线E2占90%。作者讨论的是特定带对和spin区的DSAM/branches/ADO/P及PRM支持的模式共存，τ/B/Qt同data，不据此定义跨所有核的多极二分律。原PRL为132,092501；旧133,082501误录已撤。

## 跨论文强度比较先核母态与宇称

[[mukhopadhyay-2008-136nd-transition-rates]] MU08-D18-5–7与[[petrache-2018-chiral-bands-even-even-136nd]] PE18-D18-2/3给明确纠错：旧脚本把不在原表的4.17/2.88eb及错误A/B形变当输入，即使输出算术自洽也不构成验证。原表B2/B1随spin为51/26、11/2、2/7、5/11；不能以平均值遮掉翻转。

跨论文先核核素、parity、Ji/Jf、带内级联和link，再比较逐态branch/τ/B与模型。2008负宇称Band1/2的低spin指纹对应2018 D4/D3而非正宇称D1/D2；同名编号不能替代身份表。不同论文模型组态/形变是解释层；需转轴、矩阵元、混合和producer合同，不能直接用beta平方判微观原因。

## IBFM模型比较应核整个观测向量

[[nomura-2022-questioning-wobbling-ibfm]] NOM22-D18-2–6的Pr813模型δ=-.368与所列实验-.37(+.10,-.14)中央接近，但RE2=.040对.12(.08)，没有模型不确定度，不能称精确验证。Xe735模型RE2=.163同时δ=-1.801、E2分率.76435；RE2恰近旧条件替根.164不表示同一small-δ物理解。

TableII存在大δ和RE2远超.04–.16的明确例外，不能以选中几行否定整个质量区。IBFM带EDF/能谱耦合/算符定标，属于替代模型；[[timar-2019-transverse-wobbling-105pd]] TI19-D18-3的实验偏振companion仍需同时解释。原作者questioning/open与各实验冲突分列，不重报δ或模态身份。

## 上限与终态带身份必须进入寿命强度账本

[[grodner-2011-126cs-chiral-selection-rules]] GR126-D18-2–12报告13τ与作者总结26对应概率，但新实际XML库存含36条表分支/8条明确上限；不能将上限当中央或把总结数量直接等同逐线库存。旧7.8%来自上限取端点、gamma-only的同源算术，不是独立精度验证。253/277keV跨带线曾混入带内交错序列，现撤该序列。固定K=6的Qt均值非原文测得的三轴形变。

新条件设计保持有限B中央、ICC0/光子通道完整，允许8个上限分支在0到cap之间，给每母态确定性速率端点范围；不是概率CI，更不能推原τ有误。保持旧277总光子率时，B(E2)≈4909.12 f Wu；要证f<.005仍须独立B(E2)<24.55Wu或同线δ约束，E5因子502.595本身不提供纯度界。

[[grodner-2006-128cs-chiral-doublet-lifetimes]] GR06-D18-2–7直接保存131La侧馈参数迁移、132La约20倍B(E2)差的作者报告和128Cs作者解释；sqrt20仅同几何条件Qt比。原件未给128Cs Qt≈2.1eb，也不由此裁“真假手征”。

## 同母态比值仍须保留带内与跨带身份

[[petrache-2020-137nd-multiple-chiral-bands]] P20-D18-2–12撤回旧“恢复未绘弱带in/in比”。原PDF8/Fig6明确D3/D6没有实验in/in值，缺E2 crossover。五对Table1同母态仍可作条件量：D3 31/2+、D6 33/2−是BM1_out/BE2_out，另外三对是BM1_in/BE2_out；δ0中心为7.37623/8.99725/3.20169/21.16681/5.47521，不能和强带的in/in直接比较为伙伴强度证据。

新parent-branch-exercise-result-048核能量闭合、终态带身份和寿命/公共归一抵消，并给δ=1、2时分子M1率的条件改变；同母态抵消寿命不会把跨带分母变成带内。原约2hbar对齐差是图/作者解释，还容Fermi/惯量原因，不能称恒定精确差或手征振动证明。未取得δ/完整E2in上限，保readiness，不造弱带实验CI。

## 打印强度上限、共享归一与统计定义

[[musangu-2021-chiral-vibrations-104mo-106mo]] MU21-D18-2–8的TableIV三点(.26,.20,.12)略高打印限(<.2,<.15,<.1)，中央超额30/33.3/20%不是显著性；原文未给这些限的1sigma或CL/producer。Itheo结合TPSM比、实测E2in归一与M1/E2混合，不是独立纯理论概率。

固定全部强度转换、效率/门/归一时可算RE2代理cap .226154/.5745/.620833；它们不是作者测得的刚性B上限。104Mo exp栏空，.006/.0038与同态强馈入线的比较不等于已知探测阈值。本文未测所议伙伴绝对τ/B；Fig20绝对B是模型。新source-boundary-controls-result-047保这些输入角色，不造CI或统计拒绝。

## 不同宇称的寿命基准不能互换

[[kuti-2014-multiple-chiral-doublets-103rh]] KU14-D18-2–11讨论负宇称Bands3–6；[[suzuki-2008-lifetimes-103rh-104rh]] SZ08-D18-2–4的寿命基准是正宇称Band3。相同band号不能跨论文合并，旧脚本.46/.40/.35与.18/.35/.20甚至不在Suzuki真实TableIII，均撤回。

Suzuki真实正宇称25/2+/27/2+/29/2+的BM1=2.3/1.8/1.2、BE2=.077/.14/.11可作为不同对象的方法参照，不证明Kuti负宇称比值“100%由分母驱动”。Kuti原PRM高估部分能量约200keV、未再现约.45MeV对齐跳变等模型边界保持；本文未给负宇称逐态绝对寿命，不扩成全核穷尽absence或排除MχD。

## 跨核多极性与D0提取的几何输入

[[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] L16-D18-2–9的Fig5纵轴为10^-6 fm^-2，78Br红点约.07–.2轴单位，即约10^-7 fm^-2；旧11–15点/.65–2.10×10^-5与D0=.71/Th低11.8倍不是原图/原文数据。读图近似仅定量级，不伪造精确点及误差。

从B(E1)/B(E2)到D0还需Q0、同态分支及转轴/K/CG条件。轴对称strong-coupling K0的独立前向公式给(D0/Q0)^2=5(I−1)R/[8(2I−1)]，高I系数5/16；不能套旧5/6或据此认证实际Br几何。E1 parity-change与M1/E2相对角色可约束解释，但不是“chirality=M1/wobbling=E2/octupole=E1”互相正交的普适充分定律。

## 原实验与后来DSAM综述的来源归属

[[pai-2012-high-spin-bands-194tl]] PAI12-D18-2–12：Pai无三带DSAM，未观察到手征侧带；B2宇称/E2或M2仍需18态寿命，B2/B3被建议6qp（在4qp基础加额外pair）。B1约.34MeV/5hbar crossing是能级派生与作者解释，不能和后来的双带谱混为同实验。

37keV I21、三带B在误差内相似及MPR四带配对不清由后来Bark综述报告；真正寿命引用为Masiteng2016 EPJA52,28，未得primary，不能挂Pai图下当原测量。相似不是严格等值，配对未解不是数学不可能；Guo静态RMF beta.13/gamma45.19不等MPR gamma30/40或DSAM输出。

## 高E2光子份额与结构解释分层

[[petrache-2016-134ce-triaxiality-exotic-rotations]] PE16-D18-2–7确认四个δ=-2.13/-1.73/-2.05/-2.23，条件fE2=.8194/.7496/.8078/.8326。它们为相对光子份额，仍有M1分量，不能直接作绝对集体性。

原CNS对组态/形变的解释不等于对这四线排除wobbling/chirality，也未提供逐线M1相消或scissors机制；20–50Wu普适阈值及“只能DSAM/RDDS”无此原文支持，已撤。原文另引用134Ce isomer半衰期，故无目标线τ不能扩成全核无寿命。保留实际多模型/多观测需求。

## 多带组态比较与相对强度的实际约束

[[guo-2020-pseudospin-chiral-quartet-131ba]] GU20-D18-2–12：原文多数mixing实测，少数弱线借-.2(.1)假设，不能称所有跃迁比严重无约束。作者排除把same-config模型用于131Ba所议四带，因为其计算组态不同；这不反驳103Rh的实际结论。

相同core输入或不同qp组态均不自动给“严格等Qt/必然不同Qt”实验定理；光子δ、波函数mixing和形变分开。原文无本次所议四带绝对寿命/完整强度，不意味着全核无寿命，DSAM也非唯一裁判。反证设计需同带身份的多个矩阵元与模型混合一同核验。

## 邻核类比不能替代本核的原始能级

[[wang-2013-high-spin-104ag]] WS13-D18-2–7纠正旧伪对齐数组：Fig5 A点覆盖I10–18，B只I11–15；原TableI与图定义重构的同I13/14/15 A−B约−.0243/−.1557/+.4659hbar，不支持I14跳3.5或高spin落差3hbar，B16/B18原无点。

该文用自身energy/S(I)/ratio/alignment及多个邻核提出候选，Joshi106Ag只是类比之一；后续106Ag另源解释不能直接证伪104Ag。旧beta .18/.12及Q2.04/1.36非原文实测，2.25只是该自设幅度比平方。本文未报A/B τ/绝对B，尚未穷尽后来文献。

## 倾角的平面条件与分支比的寿命抵消

[[hecht-2001-chiral-symmetry-breaking-136pm-138eu]] HE01-D18-2–5核真实TableI：Pm末行(.425MeV,89°,0°,18.51hbar)，Eu(.350MeV,68.40°,0°,13.50hbar)。phi0是平面条件；Eu表值不支持已至主轴，保留与p.4概述的张力。固定TRS/TAC模型缺两伙伴量子混合，不把采样末点当实验临界频率。

同母态M1/E2-to-E2分支比消本母态寿命，无须另一带等Qt；仍需mixing/ICC/效率合同。本文无个别绝对B/τ，不扩展成全领域无寿命。[[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D18-1的2.0(4)为E2分支/间距与两带混合假定提得的跃迁矩比，非寿命直接给beta两倍。新17项原文/几何检查和声明的同比异绝对率设计见hecht01-planar-reference-correction-result-047，不给实验CI。

## 三轴形变反演的转轴与竞争模型边界

[[hecht-2003-chirality-shape-coexistence-140eu]] HE03-D18-2–5纠正旧“beta平方比直接判别”规则。寿命结合完整分支/内转换/多极混合可导出约化强度，进一步提取Qt必须明确转动几何与有限自旋系数。三轴形变beta/gamma本身不能决定实验B(E2)：本任务条件张量练习给同一对形变参数的三个主轴强度比1.36234/.489184/5.53710，并能选取向得到等强度；不认证实际TAC解。

原Hecht2003结论是比较I≈15hbar附近B(E2)大跳变与平滑增长，寿命实验是重要检验；它未证明DSAM是唯一方法或任意等Qt就是手征。实验设计需比较同自旋的多条绝对带内/带间强度、能量与branch/mixing，检验竞争模型能否同时解释。旧本页最后一节的普适二元判决已撤，原source needs_review保留。

## 136Sm与131Ce DSAM Qt趋势的系统学边界

[[babra-2019-deformation-change-136sm]] B19-D18-2–4修正旧强断言：Babra TableI原文确实报告12+后Qt下降、15% stopping-power系统误差未计入并以TRS/TPSM作形变解释；但中心值回归对称化z≈−2.72只是条件诊断。共同乘性阻停scale会同时缩放斜率和误差，逐态独立15%包络又不是CI，故不能凭“完全覆盖”排他否定或确认形变变化。20+是Qt上限，不是有限点。

[[singh-2016-lifetime-131ce-133pr]] SI16-D18-3/4保留131Ce/133Pr表值与侧馈模式：tauSF/QSF切换及长时feeding是识别性输入，三/四点对称误差回归没有联合Cov，不将z=−.602/−1.678写成论文置信度或feeding已证实伪造。新[qt-systematics-boundary-result-049](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/qt-systematics-boundary-result-049.json)为9项raw/hash/条件检查，不是实验重拟合。

## 135Pr/133La/133Ba混合比根与相空间因子边界（checkpoint050）

[[matta-2015-transverse-wobbling-135pr]] MA15-D18-2/3与[[lv-2022-evidence-against-wobbling-135pr]] LV22P-D18-2/3保留真实大根/小根同核证据，但派生B(E2)仍依分支、in-band E2、响应和协方差；7倍中心差不是无条件CI。[[biswas-2019-longitudinal-wobbling-133la]] BI19-D18-2/3的-.35/-.40/-.38是条件替根，不是原Table1新测根。[[rojeeta-devi-2021-multiphonon-transverse-wobbling-133ba]] RD21-D18-2/3确认(Ein/Eout)^5约1.54/2.29/5.43，但该乘子与强度归一、mixing和效率一起进入换算，不能单独证明本征矩阵元或模式身份。

## 高自旋混合比根与偏振缺口（checkpoint051）

[[amro-2003-wobbling-167lu]] AM03-D18-2/3和[[jensen-2002-second-phonon-wobbling-163lu]] JE02-D18-2/3均说明：DCO/角分布分支可给大/小根条件敏感性，但缺线偏振时不能把模型选支改成实验唯一解。167Lu小根压缩和163Lu 476-keV .51/.019差异都固定其它输入后成立；后者大根由相似转动性质+PRM选择，不能称偏振确证。新[8项结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/highspin-root-boundary-result-051.json)不生成实验CI。

## 187Au与127Xe跃迁强度敏感性与偏振/衰变拓扑边界（checkpoint052）

[[sensharma-2020-longitudinal-wobbling-187au]] SE20-D18-2/3 与 [[guo-2022-low-spin-wobbling-187au]] GU22-D18-2/3 构成了187Au带间强度的典型争议案例：角分布大解（delta=2.6）下对应~164 W.u.，而在偏振/内转换确立的小解（delta=-0.10(5)）下条件塌缩88倍至1.87 W.u.，展现了多极解对强度提取的巨大影响。QTR计算支持Band 2为单粒子轨道激发。

[[chakraborty-2020-multiphonon-longitudinal-wobbling-127xe]] CH20-D18-2/3 报告大解及E2增强，小根为反事实敏感性分析（塌缩8-10倍）；二声子候选带向yrast带的Delta I = 0衰变拓扑反映了准gamma振动耦合特征。新 [au-xe-wobbling-boundary-result-052](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/au-xe-wobbling-boundary-result-052.json) 包含12项检验，不制造实验置信区间。
