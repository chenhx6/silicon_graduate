---
type: source
title: "Fougères2022学位论文第4–5章：响应、重建与污染选择合同"
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
canonical_source: "HALtel03768524v1 NNT2022NORMC209 Chapter4 printed71–83/PDF74–86"
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

后续新问题前冻结后完整读Chapter5/PDF87–103/printed84–100，Figs5.1–5.15、Tables5.1–5.3、Eqs5.1–5.11全部文本/视觉核；22行门另按原text逐项核转录。[Ch5actualscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch5-reading-scope.json)。Chapter3/6/7与附录仍未读，不借sourcehash代全文阅读。

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

## Analytical Reconstruction and Self-Audit

[精确选章前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-before.md)、[量化前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-exercise-before.md)、[输入hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-exercise-contract.json)、[程序](../../system/scripts/day17_fougeres2022_ch4_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-exercise-result.json)。公开停止表只作原字节/逗号单位的只读计算，不修release loader/表，不调用更多MC来假装原τCI通过。

几何反证是本session新source带来的实质修订：`19 mm = 19000 µm`，原pointer/table输出故障与真实装置应逐项分开。同样，一个仪器benchmark可使用不同的归一窗和拟合窗；必须取matchingjob，不能把显示图的全域积分/χ²自动当原程序所用统计量。

## Competing Interpretations and Limitations

Chapter5现已读并明确原PID/合成角/contaminationcut合同；Chapter3的实际resolution/target表、Chapter6的三个寿命方法/τ能量grid/背景域尚未读。当前不把本章结果补成它们已给的参数或原fit已复现。后续若要推进F23 χ²不闭合，最高信息是准确重建与fit章节，不是修一处公开源码后直接重报τ。

## Knowledge Impact and Learning Decision

`revises`把19000µm当已证几何错误；`supports`按作者实际input/σ/SNR与归一窗口核；`limits`单longlivedbenchmark和文件公开对完整实验CI的保证。新claim全needs_review，无human-reviewed/新实验τ/BR/spin/CI。只为Day17窗口内Day18知识preview，不授18或打开19。

## Extracted Pages

[[evasions-2023-public-release-native-readiness]]、[[fougeres-2023-mg23-velocity-difference-lifetime]]、[[lifetime-strength-audit-165tm-136nd]]、[[doppler-shift-attenuation-method]]。

## Chapter5实际门与反演的可复算合同

[量化前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch5-exercise-before.md)、[22行原输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch5-exercise-contract.json)、[程序](../../system/scripts/day17_fougeres2022_ch5_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch5-exercise-result.json)。key门与另六行有非零区间交集，交集长度只为几何量不等污染概率。单平均β的Doppler运动学交叉在θDS≈144.6878°，说明污染可重叠；不从紫圈推数值拒绝门。Eqs5.9–5.11前逆恒等控制最大误差3.82e−16，仅验证声明表达式。

`supports`完整粒子—γ身份/方向重建/response合同；`limits`从公共derivedevents或全显示曲线直接复原原fit；印刷边界保留，未造erratum/新实验CI。无原producer和Σ仍是readiness缺口，不能以本thesis与2023同研究链重复计独立验证。
