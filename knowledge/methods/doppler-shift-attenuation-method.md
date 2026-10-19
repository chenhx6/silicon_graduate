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
