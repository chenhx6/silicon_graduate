---
type: source
title: "Fougères2022学位论文第3–6章：真实校准、重建与寿命合同"
title_original: "Understanding the cosmic abundance of 22Na: lifetime measurements in 23Mg"
aliases: [Fougeres2022 thesis Ch4, F22 EVASIONS response]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: phd-thesis
reading_depth: skimmed
authors: [Chloé Fougères]
year: 2022
institution: Normandie Université, Université de Caen Normandie
citation_key: ""
canonical_source: "HALtel03768524v1 NNT2022NORMC209 Chapters3–6 and AppendicesA.2/B; scoped reading receipts"
source_url: https://theses.hal.science/tel-03768524v1
raw_file: raw/theses/day17-20261020/fougeres-2022-thesis.pdf
raw_sha256: 4f34adb73a9bc9092158c10cb8696f331455d4c027bc57cc884785aaee9d2af1
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [23Mg, 24Mg, 28Si]
reactions: [3He(24Mg,alpha)23Mg, 24Mg-fusion-evaporation]
methods: [Monte-Carlo-response, gamma-lineshape, stopping, validation]
tags: [DSAM, EVASIONS, uncertainty, geometry, source-dependence]
---

# 作者输入说明修订几何疑点，却不认证完整paperjob

## Bibliographic Record

Chloé Fougères，*Understanding the cosmic abundance of 22Na: lifetime measurements in 23Mg*，2022博士论文，NNT2022NORMC209，3Mar2022答辩、4Sep2022存入[HAL tel-03768524v1](https://theses.hal.science/tel-03768524v1)。实际201页，70228097bytes，SHA256见frontmatter，缓存`tmp/day17-fougeres2022-thesis/hal_document.pdf`。HAL生成metadata为Oct2026、正文修改日期Mar2022，不计新实验或新的论文内容版本。[下载/metadata](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-hal_document-discovery.json)。

本source最初覆盖EVASIONS README明确指定的Chapter4；后续本session独立冻结后又完整读Chapter5，actualscope分次记录；与[[fougeres-2023-mg23-velocity-difference-lifetime]]及[[evasions-2023-public-release-native-readiness]]同研究/数据链，不重复计独立实验。

## Scope and Reading Depth

先冻primed回忆、查目录与前页，再完整读Chapter4：PDF74–86/printed71–83，Fig4.1–4.8、Table4.1、Eq4.1–4.3及章节结论。关键输入/图式表/验证全部视觉核。front输出曾包含Chapter1第一页通用概述，明确记为额外预览；该次没有读全201页、Chapter3/5/6/7或附录正文；后续Ch5增量见下。[actualscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-reading-scope.json)。

后续新问题前冻结后完整读Chapter5/PDF87–103/printed84–100，Figs5.1–5.15、Tables5.1–5.3、Eqs5.1–5.11全部文本/视觉核；22行门另按原text逐项核转录。[Ch5actualscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch5-reading-scope.json)。该次Chapter3/6/7与附录仍未读；后续Ch6增量见下，不借sourcehash代全文阅读。

后续又独立冻结后完整读Chapter6/PDF105–126/printed102–123，17图9表4式全部文本/视觉核，包括粒子分支/自旋失败的章节结论；该次仍未读Chapter3/7/附录；后续A.2增量另记。[Ch6actualscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch6-reading-scope.json)。

后续定向完整读AppendixA.2/PDF168/printed165文本与FigA.2，实际等30keV三窗。相邻页读取命令额外输出A.3/PDF168tail–170全文，记为priming，未视觉核其全部图、不称完整附录阅读。Chapter3/7与其它附录未读。[A2scope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-a2-reading-scope.json)。

后续又新冻Ch3问题并完整读Chapter3/PDF44–72/printed41–69，31图8表11式全部文本/视觉核；Ch3–6各章主线已完整，仍非201页全读，Chapter7与AppendixB未读。[Ch3scope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch3-reading-scope.json)。

随后独立冻结并完整读AppendixB/PDF171–178/printed168–175，7图2表、无编号式，文本/视觉全核；TableB.2完整64通道字面保留，缺失/歧义不填。[Bscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-appendixB-reading-scope.json)。仍非201页全文，Ch7等未读。

## Summary

作者明确测得靶与束流收集箔间隙19(1)mm，支持公开输入19000µm。故EV23-10中它与F23“back-to-back”文字比较只应保留描述/版本桥，不能当已证实几何错误。Chapter4还给出响应分辨率的σ含义、数据派生SNR与背景、28Si验证的归一/拟合窗口；这些补强输入合同，仍不等完整原paperfit/联合CI可重放。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| F22-1 | 实际HAL201页论文只完整读Chapter4/PDF74–86及front/目录，答辩/提交2022与HAL2026再生metadata分开；同F23/GANIL研究链，不当新采集或全文已读。 | identity-version-and-scope | direct-thesis | PDF1–4；Ch4；reading-scope | true |
| F22-2 | Sec4.2.1明确active3He0–1000Å、target+catcher25µm、vacuum separation19(1)mm。19000µm公开输入有作者实测依据；此前back-to-back措辞对照不是几何故障证据，不能纳入release错误列表。 | actual-geometry-and-revision | direct-thesis | printed73/PDF76 Sec4.2.1 | true |
| F22-3 | 两体相空间、isotropicγ/p和实验beam能量/位置输入用于response；作者称spin未进入模拟。它是该forwardmodel假设，不证明所有alignment/acceptance物理自动消失或能用此模型独立测spin。 | model-assumptions-and-boundary | direct-thesis | printed72–73/77；Fig4.1 | true |
| F22-4 | 3He深度未实际测；SRIM给target1–2较均匀、3–5较浅峰，模拟用T12 step0–1000Å与T345 Dirac250Å。shape理想化与actualprofile/协方差不同，不能把两个模型图当两次独立实测。 | actual-input-readiness | direct-thesis | printed73–76；Figs4.2/4.3 | true |
| F22-5 | Fig4.4用不同profile/τ1与12、2keV与.5keV展示影响；Table4.1极端深度估δE/E≈.28‰，DopplerE≈6750给1.89keV印刷量级。作者“低统计完全可忽略”为该设计判断，不是binwidth=resolution或效应严格0的统计定理。 | model-sensitivity-and-interpretation-boundary | direct-model-and-arithmetic | printed74–76；Eq4.1/Table4.1/Fig4.4 | true |
| F22-6 | 作者给110.83MeV束过1000ÅAu损失.662(.001)MeV；本任务仅正确解析公开表逗号/单位、固定SP线性lookup得.63074MeV，保.03126名义差。该表版本/密度/积分未match，不据小打印scale判原实验错。 | actual-input-crosscheck-and-boundary | task-query-of-public-table | printed74；exercise table_query | true |
| F22-7 | 作者1%He/99%Au混合SRIM给dE/dx差约.95/.92%，这些是模型composition输入与结果，局部深度/剂量/密度定义尚未另核。不能替实验targetprofile或无条件迁到K16混合靶。 | model-stopping-and-domain | direct-author-model | printed76 stopping-power paragraph | true |
| F22-8 | Ch4设dx5Å/dt.1fs、TGenPhaseSpace反应、N10000与NEx50000、停止后剩余decay；公开release不同MC常数/故障不等本生产实现。时间膨胀≤.2%是作者量级判断，未据此认证所有时钟/原CI。 | declared-simulation-contract | direct-thesis | printed77 Sec4.3.1/Eq4.2 | true |
| F22-9 | 原Fig4.5 Gaussian仅示意，作者实际偏好从SRIM抽取完整exit-angle分布；thick/thin straggling明显不同，p的少fs lifetime形状不敏感为作者模拟结论。不能用单Gaussian宽或p谱单独裁τ。 | actual-particle-response-model | direct-author-model | printed77–81；Fig4.5/Fig4.7 | true |
| F22-10 | Eq4.3 prose明确σ=FWHM/2.35、输入来自近能restγ和tripleα源，σθγ=.667(.001)°；σ/能量resolution/bin三者不能无合同互换。公式指数分母字面写2σ而非2σ²，量纲/归一不完整；publicROOTGaus表达式另有正确std参数，不能由印刷式判实际代码用了错分布。 | resolution-and-literal-formula-boundary | direct-thesis-and-code-companion | printed78–79 Eq4.3；EV23 source MC_sim.C | true |
| F22-11 | CodeA以测得近窗noise(Eγ,θ)作generator并匹配实验SNR，CodeB曾模拟fusion noise不够而改用pureAu背景减除。高MC统计不使这些共享实验输入成为独立新噪声测量，也不补templateCov。 | measured-background-and-shared-input | direct-thesis | printed79 Sec4.3.2 | true |
| F22-12 | 28Si benchmark用pureAu无3He数据约450counts/SNR10，模型fusion-evaporation；归一窗6.81–6.91MeV，χ²fit窗6.84–6.90，报τ2.0(.4)ps/90%CL对旧2.7(+.8,−.7)。是有限条件的longlived验证，不认证全部fs/BR或coverage。 | actual-benchmark-and-fit-domain | direct-thesis | printed81–82/Fig4.8 | true |
| F22-13 | Fig4.8caption角窗120–160与prose/legend120–170不一致，窗口身份需原job核；不同normalization/fitdomain也说明F23全显示区χ²不必等原grid。不能把benchmark窗口直接移作F23真实fit窗口。 | literal-window-boundary | direct-thesis-and-use-gate | printed81–82 Fig4.8 | true |
| F22-14 | 声明β.075/propermeanτ10fs时meanlabpath.22548µm，到剩4.9µm firstfoil的constantβsurvival≈3.65e−10；只是条件量级解释keydecay为何少受远gap影响，不替真实v(t)/实验CI/long28Si重放。 | declared-transport-scale-control | task-design | exercise declared_constant_beta_proper_mean_control | true |
| F22-15 | 本章补真实geometry/σ/SNR/验证域，仍无F23完整τ/Eγ0fitjob或全Cov。原publicloader/scalar问题独立保留，19mm几何疑点已被新primary限制；不以同thesis/codelabel强认证原paperproducer。 | knowledge-revision-and-readiness | synthesis-with-primary | F22-2/10/11/12；EV23-6/8/13 | true |
| F22-16 | 本session新增完整Ch5/PDF87–103主线与全部15图3表11式文本/视觉核，非全201页；Ch4/F23/publicrelease有priming，回忆与新量化前分别冻结，不当盲测或Day18正式学分。 | actual-reading-scope | direct-thesis | Chapter5 printed84–100；reading-scope | true |
| F22-17 | PID选Z=2、Bρ>0及wellreconstructed(Bρ,t*)，m/q约2(.2)指alpha；低Z重建差/pileup另剔。公开derived Tree缺原TOF/QPL全PID链，不由12branch认证原raw筛选。 | actual-selection-and-readiness | direct-thesis | printed85–86 Figs5.1/5.2；Eqs5.1/5.2 | true |
| F22-18 | Table5.1 key(Ex7.785,Eγ7.333)alpha实验门37.5–39.5MeV、模拟38.1–39.5，邻7770/7782/7803门重叠；真实22行区间交集不提供污染率或独占母态，须matchingγ/response。 | actual-gates-and-identity | direct-thesis-and-arithmetic | printed88 Table5.1 | true |
| F22-19 | Eq5.3/5.4用反应点alpha能量与角重建recoil、φrecoil=π+φα；alpha实测能量在target/catcher后，先加loss。不能把aftertarget量直接当vertex能量。 | reconstruction-variable-contract | direct-thesis | printed88 Eqs5.3/5.4 | true |
| F22-20 | 实测alpha角由VAMOS与DCT组合：差小于3°θ及30°φ则均值，否则选DCT，因VAMOSφ较不可靠。公共Theta/Phi无原DCT与job不能认证这一步。 | actual-combined-angle-selection | direct-thesis | printed89–90 Fig5.5 | true |
| F22-21 | Eq5.5厚靶字面loss=6.55−.0106E−.000689E²，38/46/54MeV给5.1523/4.6045/3.9685MeV，与Fig5.4蓝线约3.5→2.8MeV不按字面闭合；保打印系数与图，不猜改式或判实际producer用错。 | literal-formula-figure-boundary | direct-thesis-and-arithmetic | printed89 Eq5.5/Fig5.4 | true |
| F22-22 | 4356例alpha门使SNR1.1(.2)→7.5(.8)，平均β.075校正有低角延迟尾偏移；平均βDoppler校正不是所有τ/angle下无偏eventresponse。 | actual-gate-gain-and-limitation | direct-thesis | printed91–92 Fig5.7 | true |
| F22-23 | Eq5.6先校正AGATAefficiency再以两支计数和归一，非absoluteγpopulation。Table5.2 key打印7.785支>97而prose/图说仅7.333观察、ground7.785未见；保标签冲突不据此创造新branch。 | normalization-and-literal-label-boundary | direct-thesis | printed92–94 Eq5.6/Table5.2 | true |
| F22-24 | 作者明确剔除7333Dopplershift与静止28Si6879相交的(Eγ,θγ)区，紫圈仅示意，实际numericcut/job缺。β.077的单点交叉给θDS144.6878°，非labθγcut；不猜mask或把全显示χ²当原fit。 | actual-contamination-cut-and-readiness | direct-thesis-and-design-control | printed93–95 Figs5.8/5.9 | true |
| F22-25 | Eq5.7以γ与recoil方向点积得θDS，作者明确未采用θDS≈θγ近似。公共原角变量/坐标与合成步骤需完整match，不用beamaxis近似认证生产重建。 | actual-doppler-angle-contract | direct-thesis | printed95 Eq5.7 | true |
| F22-26 | Eq5.8 thin[20.43,−.185,−.00354]/thick[20.20,−.187,−.00351]为模拟拟合Ex(Ealpha)；key37.5–39.5门映thin7.5992–8.5144、thick7.3370–8.2516MeV。不是真实ExCI；大门仍需gamma身份。 | actual-polynomial-gate-crosscheck | direct-model-and-arithmetic | printed96–97 Eq5.8/Fig5.11 | true |
| F22-27 | 7333gamma门7.318–7.348MeV与局部背景减除后Fig5.13得Ex7.78(.02)、sigma.1451(.0142)MeV、χ²29.18/13；Table5.3另列sigma.15。此resolution不能单独分离几keV邻态，图fit不是τfit。 | actual-parent-resolution | direct-thesis | printed97–98 Fig5.13/Table5.3 | true |
| F22-28 | 截面先校正γeff/两侧background/VAMOSnoise-eff，再以key7.785population/reference截面归一其它态；共享scale，不是22个独立absolute测量。printed98写150Eu，与F23的152Eu不同，需原job/Chapter3核。 | shared-normalization-and-version-boundary | direct-thesis | printed98–99 Sec5.4.2/Fig5.14 | true |
| F22-29 | Eqs5.9–5.11对backward cosθDS≤0且R=Eγ/Eγ0≤1仅一physicalβ≥0根(R=1为0)；Ch5Fig5.15横轴βems，F23Δβ=βreac−βems须eventmatched转换，不能直接同名谱/同fit。 | observable-and-domain-contract | direct-thesis | printed99–100 Eqs5.9–5.11/Fig5.15 | true |
| F22-30 | 新Ch5实际PID/合成角/contaminationcut/谱变量使F23fullshownχ²不闭合的解释更具体，但未得numericmask/原job/fitCov，不归因唯一原因、未重fitτ/BR/CI；下一最高信息Ch6方法与背景fitdomain。 | knowledge-update-and-readiness | synthesis-with-primary | F22-18/20/24/25/29 | true |
| F22-31 | 新完整读Ch6/PDF105–126/printed102–123、17图9表4式文本/视觉核；只有Ch4–6完整，未读全thesis/Ch3/7/appendix。三次冻结及priming分开，无formal18credit。 | actual-reading-scope | direct-thesis | Chapter6；reading-scope | true |
| F22-32 | Sec6.2.1每个τ/E0将MC按同能区积分归一到data，区间含peak和两侧noise；称ROOThistogram maximumlikelihood option，但未给完整job/所有numericfitwindows。不能从术语唯一确定统计量/零bin/MCerror。 | actual-fit-normalization-and-ambiguity | direct-thesis | printed102 Sec6.2.1 | true |
| F22-33 | Table6.1给68/95%且m=1/2/3阈值；本章声明τ/E0两自由参数m2、systematics含forwardmodel而quotedτerrors为statonly。jointcontour与单参数projection及边界coverage仍需统计合同，不能拿fixedE0slice当已profile。 | stated-CI-contract | direct-thesis | printed102–103 Table6.1 | true |
| F22-34 | keyDSAMθDS154–162°，作者将4keV/bin改12keV/bin以令χ²/ndf靠1，τ<17fs/95%依knownE0。此是原分析选择与upperlimit，不证明调bin到χ²≈1就获得校准coverage。 | actual-binning-and-upper-limit | direct-thesis-and-use-boundary | printed104–106 Fig6.2/Table6.2 | true |
| F22-35 | keyβM报11(+6,−4)fs、E07333.0(+1.2,−.4)keV，Fig6.4横轴βems，集全角events但非多次独立采集；对near7770/7782复合峰用5067重建并显式模拟0/3fs与错误energy产生的高β尾。 | actual-beta-method-and-companion | direct-thesis | printed106–109 Figs6.3–6.5/Table6.3 | true |
| F22-36 | DCLM Eq6.1对每个τ从MC算meanβDC，再把data与MC各自event变换为Doppler-corrected谱，key9.5(+4.5,−2)fs；data变换本身依τ，不能当固定观测histogram参数扫描或独立data验证。 | parameter-dependent-transform | direct-thesis | printed109–111 Eq6.1/Figs6.6/6.7 | true |
| F22-37 | Fig6.8跨态相对差均值3.64%/SD30.4、22entries且两侧各半；作者据此称无systematic。相同data/response的共同bias可同时不出现在差值中，本图不证明绝对systematic为0。 | author-interpretation-and-counter-evidence | direct-thesis-and-inference | printed111–112 Fig6.8 | true |
| F22-38 | 三knownlifetime态用τ/ZAGATA扫描得位置−252.3(1.7)mm，另DCT/VAMOS角法得148(+12,−8)mm；作者据此用17mm targetshift修survey值。它是不同估计路线与共享标定，非新的keylifetime独立实验。 | actual-geometry-calibration | direct-thesis | printed113–114 Fig6.9/Table6.5/Fig6.10 | true |
| F22-39 | Table6.6灵敏度为特定Ex7785/Eγ7333/τ1fs的EVASIONS模型，energy/angle resolution占主导、作者等效约1fs。以1%stopping扰动得到的变化不等实际stopping已知1%或全responseCov。 | conditional-systematic-model | direct-author-model | printed115 Table6.6 | true |
| F22-40 | Sec6.2.6明确三方法同data不独立，Eq6.2用逆variance中心及minσ而非独立合并误差；Table6.7 finalkey9.9(+4.5,−2)fs/Γ66(+17,−21)meV。minσ政策不是一般sharedCov定理。 | shared-data-combination-policy | direct-thesis | printed115–116 Eq6.2/Table6.7 | true |
| F22-41 | 以实际11/9.5与声明对称化σ5/3.25算weightedcenter9.9455fs；固定weights下ρ>.4623125时真实Gaussianlinearσ大于min3.25。仅条件反证任意ρ下保守性，actualρ/原asymmetry未知，不改实验CI。 | conditional-covariance-counterexample | task-arithmetic-with-actual-inputs | exercise Eq6p2_conditional_covariance | true |
| F22-42 | Table6.4 keyDCLMτ9.5(+4.5,−2)与Γ60(+18,−22)的中心不按hbar/τ闭合：字面应69.2855；Table6.7τ9.9则66.4861对应打印66。保各表原值，不猜修或据此否定原实验。 | literal-width-table-boundary | direct-thesis-and-arithmetic | printed112 Table6.4；printed116 Table6.7 | true |
| F22-43 | BRp以2DExVAMOS/ExSPIDER去pureAu背景并选abs差≤.45MeV，防高态到22Na583串入；10态模板中7770被BRp<.2%先验约束，χ²仅7.65–7.85MeV。全显示域不等fitdomain。 | actual-proton-selection-and-prior | direct-thesis | printed116–119 Figs6.11–6.14/Eq6.3 | true |
| F22-44 | SPIDERintrinsic效率假设100%、geometricMC及γeff归一；residualnoise选−1.5≤ExVAMOS−ExSPIDER≤−.5。thesisBRp.68(.06)%、Γp.45(+.16,−.17)meV与F23.68(.17)%版本不同，非两独立BR，缺完整job/Cov不重算CI。 | actual-branch-normalization-and-version | direct-thesis | printed119–121 Fig6.15/Tables6.8/6.9 | true |
| F22-45 | 另一alpha有无γ计数法仅BR15(+16,−15)%、约1000vs设计50000counts，非第二精密.68确认；7855/8016因γ未见只下限，shellmodelτ/J用于coherence非独立实验BR。 | failed-companion-and-model-boundary | direct-thesis | printed120–121 Table6.9 | true |
| F22-46 | TALYS截面与data低高Ex分区失配，fsim.29(.22)后点散布factor5，keyJ5/2与7/2预测.79/.66差小于实测误差；作者明确未能定J。Fig6.13示意7/2标签不能升级本实验spin确定。 | actual-negative-spin-result | direct-thesis | printed121–123 Fig6.16/Eq6.4 | true |
| F22-47 | Ch6公开了shareddata/minerror/targetshift/branch模板与fitdomain的实质合同，仍未给原ROOT版本/actualjob/所有τfitmask与Σ。publicLL与manual似然的API语义另需新核，不由thesis文字认证paper统计实现。 | readiness-and-next-input | synthesis-with-primary | F22-32/36/40/43/44 | true |
| F22-48 | AppendixA.2实际中心DCγ7318–7348keV，左右7288–7318/7348–7378各30keV；投影到EalphaVAMOS再减两侧平均，FigA.2(c)有负值。原窗口来自primary，不是自行选择。 | actual-background-windows | direct-thesis | printed165 AppendixA.2/FigA.2 | true |
| F22-49 | 按原均值合同D=S−(L+U)/2，完整Var=VS+VL/4+VU/4−CSL−CSU+CLU/2；只有独立primitivePoisson特例才S+(L+U)/4。源未给逐bin计数/完整Cov，不能以减后D替Poissonvariance。 | conditional-error-propagation | task-exact-algebra | exercise general_variance | true |
| F22-50 | 对γ背景densityb0+b1x+b2x²、三连续等宽h，原中心减side平均的背景残差精确−b2h³；真实h30keV给−27000b2，constant/linear消但曲率未消。actualb2未知，不据此量化源偏差。 | conditional-background-curvature | task-exact-polynomial-integral | exercise background_residual_symbolic | true |
| F22-51 | signal也以Acenter−(Alower+Aupper)/2进入；若线形尾漏到side，须matchingresponse评估，不能从±15keV自动称总γyield或无泄漏。source没有给该泄漏fraction。 | response-leakage-readiness | task-inference-from-actual-operator | FigA.2；exercise signal_contribution | true |
| F22-52 | closed区间打印共享边界不等实际digital重复计数，原bin/halfopen实现未知；多个track可共享event，窗口不重叠也不能无条件称所有counts独立。原job/Σ未补。 | digital-boundary-and-source-dependence | inference-with-readiness | printed165 FigA.2；EV23-3 | true |
| F22-53 | A.2只补实际背景operator/window，不提供原lifetimefulljob/CI；Ch6pureAu2D减与A.2局部side估计层次不同，不以新符号式给实验误差。额外A.3文字暴露已记，非新卡/完整附录读。 | scope-and-statistical-use-boundary | synthesis-with-primary | A2reading-scope；F22-43/44/48/49 | true |
| F22-54 | 新增完整Ch3/PDF44–72/printed41–69、31图8表11式文本/视觉核；连此前Ch4–6+A.2均独立scope记录，不称201页全文读、未知Ch7/B及原producer。 | actual-reading-scope | direct-thesis | Chapter3；Ch3reading-scope | true |
| F22-55 | 实测beam110.83±.443MeV/spotradius1.6(.2)mm，而MC XYσ用radius/4；intensity10–30enA且未准确量化。catcher19(1)mm/20(.5)µm再次支持gap，不等beamprofile/absoluteyield/Cov已知。 | actual-beam-and-model-contract | direct-thesis | printed42 Table3.1/Fig3.2 | true |
| F22-56 | Table3.2/3.3区分producerimplanted与Demokritos事后测得3He面密度；两reference截面带10%systematic、depth未测、target10online损坏。薄靶keyγ不足，不能当独立thin/thickτ对照或将implant数代实际密度。 | actual-target-and-negative-companion | direct-thesis | printed43–44 Tables3.2/3.3/Fig3.4 | true |
| F22-57 | VAMOS轻粒子IC信号低于threshold未用；PLcharge未校准，PID经DC/PL/HF与Bρ/t*。HF7.8456MHz/127.46ns、TPL1175ns处分支减一周期是实际alias处理，不是仅singleTOF测量。 | actual-PID-and-RF-contract | direct-thesis | printed46–49 Figs3.7–3.10/Eqs3.1–3.5 | true |
| F22-58 | Eq3.6在Bρ=p/q定义下以r=Bρq/(mc)作1/sqrt(1−r²)−1，与momentum关系sqrt(1+r²)−1不同；原constants/Bρ.95给43.7863vs42.7813MeV。为字面物理关系边界，不认原calibration/job已使用错能量。 | literal-momentum-versus-beta-boundary | direct-thesis-and-arithmetic | printed50 Eq3.6 | true |
| F22-59 | publicTools.C Brho_Ekin_conv同一形式r=.3204ZB/A；原body native.95/M3728/A4/Z2给43.93835，而同r momentum式42.92645，差1.01190。反向返回.95只证明两式互逆，不证明physicalrigidity合同；未修source/重报实验。 | native-public-companion-and-limit | direct-code-and-native | Tools.C L176–181；Ch3exercise original_native_conversion | true |
| F22-60 | AGATA31晶体、θγ120–176°，trackingframe到lab有−π/2绕beam旋转且Ylab=−Xtrack；trackedcoords不是未经合同可直接与VAMOSphi组合。DAQ/replay/PSA/crosstalk/trigger链同研究输入，不新独立data。 | actual-geometry-frame-and-producer | direct-thesis | printed52–56 Figs3.14–3.16/Eq3.8 | true |
| F22-61 | Co60用于preprocess，Eu152在靶点给efficiency/低能resolution；AmBeFe受空间限制不在靶点、只高能energycal到8MeV。高能cal源不能直接叫绝对inbeam/靶点eff测量，F22-28的150Eu文字由此限为版本/打印边界。 | actual-calibrator-roles | direct-thesis | printed56–57 Fig3.17 | true |
| F22-62 | 在线七个unshiftedγ峰测FWHM，能量函数fit差后实际MC用测得σ；角σ.667(.001)来自547Au门trackedcoords加引用4mmPSA尺度的扰动/拟Gaussian(打印χ²约10100/31)，不是独立已知trueposition的localization测量或完整σθ系统误差。 | response-origin-and-uncertainty-boundary | direct-thesis | printed57–58 Fig3.18 | true |
| F22-63 | Eu152已知activity/age给低能绝对eff，Geant4同geometry曲线跨100–8000keV，经1.80(.06)归一；Fig3.19红高蓝低，归一因子角色需matchjob。7333效率为normalizedmodel/interpolation，非该能量新实测或独立MCcal。 | actual-efficiency-calibration-and-domain | direct-thesis | printed58–59 Fig3.19/Eq3.9 | true |
| F22-64 | Eq3.9自然log且E用keV，ε是fraction：1300给.0429969、7333给.0105908。Fig3.19更精细打印coeff在两能量给.0408452/.00987088，rounded/full差5.268/7.293%；保各表达式，不把舍入差当独立统计矛盾或推原CI。 | literal-coefficient-and-unit-contract | direct-thesis-and-arithmetic | printed58 Eq3.9；printed59 Fig3.19 | true |
| F22-65 | 声明β.077/θDS120/145/176时Eobs7040.18/6877.44/6789.70keV，Eq3.9 εobs/εrest1.0395/1.0628/1.0758；仅能量role敏感性控制，未得job不认实际eff用错E或修BR。 | conditional-energy-role-control | task-arithmetic-with-actual-curve | Ch3exercise energy_role_control | true |
| F22-66 | 三个实测background能窗1.5–1.6/4.2–4.3/6.65–6.75MeV的角形相似，作者称mostlikely比例于geometryeff。它不是任意source角分布/γ门下已测绝对angularresponse或polarimeterQ。 | angular-acceptance-companion-boundary | direct-thesis-and-use-gate | printed59–60 Fig3.20 | true |
| F22-67 | Au547/Si6878随time的energy与31coretiming未见明显漂移为实际monitor；其resolution范围/fit统计限不提供所有eventenergy/angle跨参数Cov。 | actual-stability-companion | direct-thesis | printed60–61 Fig3.21 | true |
| F22-68 | Table3.5 front300(1)/back640(5)µm、frontAl.3µm及r24/48,Z95、backr23/48,Z110；Fig3.14另298/580并有105mm位置标注，publicdefaultZ119.8/r23。保对象/版本桥，不硬配17mm shift或选一个默认冒exactgeometry。 | geometry-version-readiness | direct-thesis-and-code-input | printed53 Fig3.14；printed62 Table3.5；publicinputs L39–44 | true |
| F22-69 | Table3.5单面point角front14.178–26.806°、back11.810–23.575°，与表列12.8–24.5°需原定义/位置match；这些不等双ring联合接受/实测ε，也不由裸solidangle重算BR。 | conditional-geometry-crosscheck | actual-input-arithmetic | Ch3exercise single_face_geometry_crosschecks | true |
| F22-70 | SPIDER三alpha源5.1566/5.4856/5.8048MeV用Gaussian+低能exponentialtail校准；FWHM四象限74.2/74.7/89.3/94keV与back49.6keV，Table3.7 σθ.35但∆φ22.5是分割宽，不能全当Gaussianσ。 | actual-particle-calibration-and-width-contract | direct-thesis | printed62–64 Tables3.6/3.7/Figs3.23–3.25 | true |
| F22-71 | SPIDER选strip/sector能量相符剔drift，并用SRIMΔE/Eres识别同位素和检验厚度；source校准与cleaning/threshold/deadlayer/inbeam效率不是同输入。publicderivedtree缺原strip/sector完整字段，不能认证这一选择。 | actual-particle-selection-and-readiness | direct-thesis | printed64–65 Figs3.26/3.27 | true |
| F22-72 | DCT实验gaspressure未记，故以SPIDER孔投影/线影位置校准电子drift约50mm/µs；两DCT independently从target点构角，再均值，90%theta差<.7°/75%phi差<5°是分位范围，不自动Gaussian1σ或独立绝对角真值。 | actual-position-calibration-and-dependence | direct-thesis | printed66–69 Table3.8/Figs3.28–3.31/Eqs3.10/3.11 | true |
| F22-73 | Ch3补source/MC/highE/angleorigin和PID/strip/geometry链；仍无fullpaperjob/calΣ/actualsourcefitcoeffCov，不能以更多模型history填空。Bρ原表达式native边界保留，原data34source未改、不新实验τ/BR/CI。 | updated-input-readiness | synthesis-with-primary | F22-56/59/62/63/68/71/72 | true |
| F22-74 | publicTree实际trackZ已为约−324至−108mm的坐标，代码−17为relative nominal修正；thesisAGATA绝对−252.3位置不是另一次eventoffset。新预检在计数前纠正此混同，原calibration/target/θDS/gate仍须matching，不由query替生产合同。 | coordinate-role-companion | direct-public-data-and-code | EV23-18/19/23 | true |
| F22-75 | 新增完整AppendixB八页文本/视觉/7图2表；B.1补实际PSA/电子学/source与在线response，B.2给64通道线性cal表，非原traces/producer/coeffCov已得或全thesis读。 | actual-reading-scope | direct-thesis | printed168–175 AppendixB；Breading-scope | true |
| F22-76 | PSA有6mm粗网格后局部2mm细网格；同segment二interaction线性组合、更高multiplicity不妥善处理；broken少数segment可借core/crosstalk恢复，postPSA强制sumsegments=core并校neutrondamage。不能以trackedTree重放未给的36×36校正矩阵/traces或认证高能selection。 | actual-electronics-and-response-limit | direct-thesis | printed169–170 SecB.1.2/FigsB.2/B.3 | true |
| F22-77 | B.1.3 sourceEu152打印τ4.267e8s、A0 18755/s、age6.127e8s、acquisition5029s；FigB.4是coreE且SNR≥10峰Gaussian，Ch3Fig3.19效率是TrackE。不同observable/selection不能直接拿图峰面积闭合trackedε。 | actual-source-input-and-observable | direct-thesis | printed170–171 SecB.1.3/FigB.4 | true |
| F22-78 | 把同打印时间分别声明为mean或half时，计算Astart4461.82或6932.14/s、ratio1.553656；这只是角色控制。NNDC两route/IAEA/LNHB实取TLS失败无body，当前不凭记忆裁τ标签或原activity/eff用错，不强配1.80归一。 | conditional-normalization-and-missing-input | task-arithmetic-and-readiness | Bexercise activity_role_controls；official-discovery receipts | true |
| F22-79 | TableB.1七行在线unshifted峰明确σ：279/547/1369/1779/4496/5099/6878keV对应1.6/1.8/2.4/2.6/2.9/3.4/4.4keV；4496/5099的quotedσerror3.7/4.4大，不能当精密已知globalresolution或忽略uncertainty。 | actual-response-table-and-limit | direct-thesis | printed172 TableB.1/FigB.5 | true |
| F22-80 | 同28Si6878线出现在onlineσ表与Ch4longlivedbenchmark，至少同仪器/线/研究链，actualevents是否完全相同未明。不能把二者当完全独立的responsecal和validation来数证据。 | shared-calibration-boundary | cross-source-within-thesis | TableB.1；F22-12 | true |
| F22-81 | TableB.2实际64通道仅62组全numeric；Q1strip14的offset/gain均/，Q4strip6 offset打印−833.7.q±42.29而gain17.6±.12。均保字面，不修q/用相邻/均值补missing，不认blank=zero或active/dead状态已知。 | actual-calibration-readiness | direct-thesis-and-literal-transcription | printed175 TableB.2 | true |
| F22-82 | 以Q2strip1真实offset−623.6±51.87、gain14.7±.12在5485.6keV得rawA415.5918；若quotedscales作variance，未知ρ的parameterpredictionstd可1.999–101.741keV(ρ0为71.956)。不是实际calCI或intrinsicFWHM，不能选ρ强配线宽。 | conditional-real-parameter-covariance | task-algebra-on-actual-table | Bexercise actual_parameter_covariance_controls | true |
| F22-83 | 固定rawAi/Aj时共同calibrationCov(Ei,Ej)=Varb+AiAjVarm+(Ai+Aj)Cov(b,m)，未知fitCov/quotedCL/rawcentroids不可补；把每event独立Gaussian-smear与sharedcalibration参数误差互换会改变统计合同。 | shared-parameter-use-contract | exact-linear-algebra | Bexercise shared_calibration_cross_event_covariance | true |
| F22-84 | B.2完整cal系数仍不提供原strip/quad/rawamplitudes/eventcuts，publicTree只有Si_dE等summary；不能凭现在有64表就重新认证原粒子selection/BR或raw→event重放。 | actual-data-readiness | direct-thesis-and-public-schema | SecB.2/TableB.2；EV23-2/23 | true |
| F22-85 | TableB.1的unshifted近7MeV响应为σ4.4±2.1keV，不是FWHM4.4；作者因子2.35换10.34keV。源profile/core/TrackE/cal/inbeam核/完整Cov应分层，不由一个打印精度补全原response。 | width-and-selection-contract | direct-thesis-and-arithmetic | TableB.1；Bexercise TableB1_resolution_crosschecks | true |
| F22-86 | B补可复用七线表与64通道输入/缺口、source时间角色控制，未得独立Eu半衰body/原calCov/精确producer。当前只supports合同可复核，limits完整实验eff/BR/τCI复现；新cal/核模型不冒实验。 | knowledge-delta-and-readiness | synthesis-with-primary | F22-77/78/79/81/83/84/85 | true |
| F22-87 | actualpublicSi_theta的16值逐项matchBackup119.8mm/stripcenterrecipe，收窄publicdefault119.8与dataset无关的疑虑；它是生成规则指纹，不是独立survey/geometry精度或原paperproducer认证，Table3.5/图/对象桥仍保。 | new-actual-data-companion | direct-public-data-and-code | EV23-24/25/26 | true |
| F22-88 | 原Eq3.5 mrad/out-of-horizontal-plane θ公式得到publicThetaLdeg actual363176条的浮点级支持；two-projected-slope式不同，θ一致仍不定φ reflection/relativeframe或DCTcombined/recoilcalibration。新actualquery补变量合同，非独立geometry/τ/BR测量。 | actual-data-convention-companion | direct-data-and-equation | EV23-29/30/31/32/33 | true |

## Analytical Reconstruction and Self-Audit

[精确选章前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-before.md)、[量化前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-exercise-before.md)、[输入hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-exercise-contract.json)、[程序](../../system/scripts/day17_fougeres2022_ch4_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-exercise-result.json)。公开停止表只作原字节/逗号单位的只读计算，不修release loader/表，不调用更多MC来假装原τCI通过。

几何反证是本session新source带来的实质修订：`19 mm = 19000 µm`，原pointer/table输出故障与真实装置应逐项分开。同样，一个仪器benchmark可使用不同的归一窗和拟合窗；必须取matchingjob，不能把显示图的全域积分/χ²自动当原程序所用统计量。

## Competing Interpretations and Limitations

Chapter3–6与A.2/B现已读；Ch7尚未读，全部numericjob/ROOT版本/Σ尚未取得。当前不把本章结果补成它们已给的参数或原fit已复现。后续若要推进F23 χ²不闭合，最高信息是准确重建与fit章节，不是修一处公开源码后直接重报τ。

## Knowledge Impact and Learning Decision

`revises`把19000µm当已证几何错误；`supports`按作者实际input/σ/SNR与归一窗口核；`limits`单longlivedbenchmark和文件公开对完整实验CI的保证。新claim全needs_review，无human-reviewed/新实验τ/BR/spin/CI。只为Day17窗口内Day18知识preview，不授18或打开19。

## Extracted Pages

[[evasions-2023-public-release-native-readiness]]、[[fougeres-2023-mg23-velocity-difference-lifetime]]、[[lifetime-strength-audit-165tm-136nd]]、[[doppler-shift-attenuation-method]]。

## Chapter5实际门与反演的可复算合同

[量化前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch5-exercise-before.md)、[22行原输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch5-exercise-contract.json)、[程序](../../system/scripts/day17_fougeres2022_ch5_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch5-exercise-result.json)。key门与另六行有非零区间交集，交集长度只为几何量不等污染概率。单平均β的Doppler运动学交叉在θDS≈144.6878°，说明污染可重叠；不从紫圈推数值拒绝门。Eqs5.9–5.11前逆恒等控制最大误差3.82e−16，仅验证声明表达式。

`supports`完整粒子—γ身份/方向重建/response合同；`limits`从公共derivedevents或全显示曲线直接复原原fit；印刷边界保留，未造erratum/新实验CI。无原producer和Σ仍是readiness缺口，不能以本thesis与2023同研究链重复计独立验证。

## Chapter6同数据三方法与统计合同

[新量化前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch6-exercise-before.md)、[实际表输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch6-exercise-contract.json)、[程序](../../system/scripts/day17_fougeres2022_ch6_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch6-exercise-result.json)。hbar/tau精确端点变换、实际数值下条件Cov范围只核合同，不新报CI。

作者已经承认同data依赖，不能把βM/DCLM相符当独立采集；Fig6.8差值约对称仍容许共同bias。对θ/E响应、同数据归一和每个τ改变的DCLM坐标需联合记录。Table6.1名义68%与常用68.27%的舍入不同，不以末位阈值差发明erratum；joint2D阈值亦不等单τprofilecoverage。

`supports`同数据显式分层与原fitdomain合同；`limits`minσ无条件保守、跨方法无差即无bias及示意图spin标签。下一有界高信息是publicChi2Test LL/手写likelihood实际API与零bin/范围语义；原paperjob未认证，不修producer/原表。

## A.2真实三窗的背景算符

[量化前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-a2-exercise-before.md)、[实际三窗](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-a2-exercise-contract.json)、[标准库Fraction程序](../../system/scripts/day17_fougeres2022_a2_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-a2-exercise-result.json)。初系统Python无sympy失败exit1已保存，改用标准库精确有理数积分，没有装包或改原输入。

通用协方差与背景曲率只为原operator的数学合同；没有抄图造逐bincounts、给actualcurvature或将减后负值裁0再当rawPoisson。源actualnormalization/事件依赖/response仍决定实验CI，不把本任务符号推导升级实验测量。

## Ch3实际校准与Bρ原表达式边界

[量化前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch3-exercise-before.md)、[实际输入及hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch3-exercise-contract.json)、[原转换函数](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch3-conversion-exact.ccfrag)、[程序](../../system/scripts/day17_fougeres2022_ch3_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch3-exercise-result.json)。native只摘取确定输入的转换函数，不执行原未初始化全MC。原bytehash保持，互逆通过不充物理oracle。

三类响应需分别保存：低能source绝对eff→模型高能外推；测得/引用PSA尺度导出的angularkernel；粒子strip校准与实际cleaning/geometry。公式/图coeff、geometry版本/原calibration桥未闭，不把5–7%字面曲线差或1.01MeV条件转换差换算实验τ/BR偏差。新primary限制旧“测得σθ”的简称，并不清原needs_review或给humanreview。

## AppendixB实际校准台账与shared参数合同

[量化前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-B-exercise-before.md)、[七线/时间输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-B-exercise-contract.json)、[64通道结构化转录](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-B-strip-table.json)、[程序](../../system/scripts/day17_fougeres2022_appendixB_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-B-exercise-result.json)。

Eu152时间常数的officialgroundstate half/mean验证是当前显式missinginput：NuDat两入口、IAEA与LNHB官方URL在本次传输中TLS失败，没有body证据；保失败、不禁用TLS、不凭记忆将τ当half或推实验用错。mean/half两个条件activity不是两个测量。coreE峰与TrackEeff、quoted参数尺度与intrinsicwidth、共同cal与独立eventsmear分别保存。

### TableB.1原七线响应输入

| emitter | rounded Eref keV | centroid keV | σ keV | quoted σ error keV |
| --- | --- | --- | --- | --- |
| 197Au | 279 | 278.8 | 1.6 | 0.003 |
| 197Au | 547 | 547.3 | 1.8 | 0.003 |
| 24Mg | 1369 | 1368.3 | 2.4 | 0.1 |
| 28Si | 1779 | 1778.4 | 2.6 | 0.2 |
| 28Si | 4496 | 4496.6 | 2.9 | 3.7 |
| 28Si | 5099 | 5099.2 | 3.4 | 4.4 |
| 28Si | 6878 | 6877 | 4.4 | 2.1 |

### TableB.2原字面校准输入（64通道）

offset单位keV，gain单位keV/a.u.；仅原quoted尺度，不给covariance或置信度解释。

| quadrant | strip | offset literal | gain literal | status |
| --- | --- | --- | --- | --- |
| Q1 | 1 | -392.5±32.71 | 17.2±1.00 | numeric |
| Q2 | 1 | -623.6±51.87 | 14.7±0.12 | numeric |
| Q3 | 1 | -854.8±108.70 | 15.6±0.26 | numeric |
| Q4 | 1 | -686.5±52.53 | 15.0±0.13 | numeric |
| Q1 | 2 | -296.1±26.86 | 17.3±0.77 | numeric |
| Q2 | 2 | -418.7±39.81 | 14.4±0.10 | numeric |
| Q3 | 2 | -374.4±83.57 | 13.1±0.19 | numeric |
| Q4 | 2 | -268.5±58.68 | 13.7±0.14 | numeric |
| Q1 | 3 | -108.9±44.63 | 14.3±1.19 | numeric |
| Q2 | 3 | -790.2±52.80 | 14.2±0.12 | numeric |
| Q3 | 3 | -886.3±125.50 | 15.8±0.31 | numeric |
| Q4 | 3 | -879.0±54.29 | 13.6±0.12 | numeric |
| Q1 | 4 | -457.5±32.71 | 17.9±0.98 | numeric |
| Q2 | 4 | -368.6±43.07 | 13.5±0.10 | numeric |
| Q3 | 4 | -288.9±144.70 | 14.9±0.37 | numeric |
| Q4 | 4 | -457.8±60.65 | 16.7±0.17 | numeric |
| Q1 | 5 | -737.6±70.44 | 10.6±0.12 | numeric |
| Q2 | 5 | -1024.0±63.39 | 14.7±0.14 | numeric |
| Q3 | 5 | -1016.0±285.30 | 14.0±0.59 | numeric |
| Q4 | 5 | -1205.0±35.28 | 18.0±0.09 | numeric |
| Q1 | 6 | -836.5±60.34 | 16.0±0.15 | numeric |
| Q2 | 6 | -559.2±40.46 | 12.3±0.08 | numeric |
| Q3 | 6 | -485.3±109.40 | 14.1±0.26 | numeric |
| Q4 | 6 | -833.7.q±42.29 | 17.6±0.12 | ambiguous-literal |
| Q1 | 7 | -931.6±51.59 | 16.6±0.13 | numeric |
| Q2 | 7 | -812.6±35.20 | 12.8±0.07 | numeric |
| Q3 | 7 | -896.5±95.89 | 16.1±0.25 | numeric |
| Q4 | 7 | -1087.0±44.22 | 17.7±0.12 | numeric |
| Q1 | 8 | -984.0±19.70 | 19.3±0.59 | numeric |
| Q2 | 8 | -877.5±50.04 | 16.5±0.13 | numeric |
| Q3 | 8 | -1006.0±136.8 | 16.7±0.39 | numeric |
| Q4 | 8 | -972.2±48.81 | 18.4±0.14 | numeric |
| Q1 | 9 | -524.8±65.73 | 12.3±0.13 | numeric |
| Q2 | 9 | -602.7±38.78 | 10.7±0.07 | numeric |
| Q3 | 9 | -716.3±100.40 | 14.4±0.23 | numeric |
| Q4 | 9 | -972.9±61.13 | 18.2±0.17 | numeric |
| Q1 | 10 | -723.9±63.48 | 16.1±0.16 | numeric |
| Q2 | 10 | -467.9±54.56 | 11.7±0.11 | numeric |
| Q3 | 10 | -1101.0±150.00 | 17.5±0.40 | numeric |
| Q4 | 10 | -808.2±53.84 | 17.9±0.15 | numeric |
| Q1 | 11 | -222.2±28.71 | 8.7±0.70 | numeric |
| Q2 | 11 | -585.2±46.53 | 14.8±0.11 | numeric |
| Q3 | 11 | -502.5±88.60 | 13.5±0.20 | numeric |
| Q4 | 11 | -592.9±39.93 | 17.8±0.12 | numeric |
| Q1 | 12 | -593.4±56.93 | 14.6±0.14 | numeric |
| Q2 | 12 | -694.9±64.90 | 16.4±0.18 | numeric |
| Q3 | 12 | -705.8±92.64 | 15.3±0.23 | numeric |
| Q4 | 12 | -695.9±63.66 | 17.8±0.18 | numeric |
| Q1 | 13 | -468.8±87.72 | 14.4±0.21 | numeric |
| Q2 | 13 | -519.5±59.88 | 17.1±0.17 | numeric |
| Q3 | 13 | -496.2±128.40 | 14.2±0.30 | numeric |
| Q4 | 13 | -292.1±64.44 | 13.7±0.15 | numeric |
| Q1 | 14 | / | / | missing |
| Q2 | 14 | -583.8±48.55 | 17.9±0.14 | numeric |
| Q3 | 14 | -364.5±87.06 | 14.7±0.22 | numeric |
| Q4 | 14 | -435.5±59.76 | 13.9±0.14 | numeric |
| Q1 | 15 | -859.6±96.35 | 14.3±0.22 | numeric |
| Q2 | 15 | -876.7±53.02 | 18.0±0.15 | numeric |
| Q3 | 15 | -741.8±121.10 | 15.1±0.29 | numeric |
| Q4 | 15 | -709.5±63.43 | 15.6±0.16 | numeric |
| Q1 | 16 | -867.6±66.43 | 16.6±0.18 | numeric |
| Q2 | 16 | -1098.0±87.54 | 19.1±0.26 | numeric |
| Q3 | 16 | -1530.0±286.80 | 20.4±0.81 | numeric |
| Q4 | 16 | -927.6±90.32 | 13.7±0.19 | numeric |
