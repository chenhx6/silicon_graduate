---
type: source
title: "Fougères2022学位论文第4章：EVASIONS响应、19mm间隙与验证范围"
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

本source只覆盖EVASIONS README明确指定的Chapter4，后续若读其它方法章节须另记actualscope；与[[fougeres-2023-mg23-velocity-difference-lifetime]]及[[evasions-2023-public-release-native-readiness]]同研究/数据链，不重复计独立实验。

## Scope and Reading Depth

先冻primed回忆、查目录与前页，再完整读Chapter4：PDF74–86/printed71–83，Fig4.1–4.8、Table4.1、Eq4.1–4.3及章节结论。关键输入/图式表/验证全部视觉核。front输出曾包含Chapter1第一页通用概述，明确记为额外预览；没有读全201页、Chapter3/5/6/7或附录正文。[actualscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-reading-scope.json)。

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

## Analytical Reconstruction and Self-Audit

[精确选章前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-before.md)、[量化前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-exercise-before.md)、[输入hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-exercise-contract.json)、[程序](../../system/scripts/day17_fougeres2022_ch4_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2022-thesis-ch4-exercise-result.json)。公开停止表只作原字节/逗号单位的只读计算，不修release loader/表，不调用更多MC来假装原τCI通过。

几何反证是本session新source带来的实质修订：`19 mm = 19000 µm`，原pointer/table输出故障与真实装置应逐项分开。同样，一个仪器benchmark可使用不同的归一窗和拟合窗；必须取matchingjob，不能把显示图的全域积分/χ²自动当原程序所用统计量。

## Competing Interpretations and Limitations

Chapter3的实际resolution/target表、Chapter5的事件重建、Chapter6的三个寿命方法/τ能量grid/背景域尚未读。当前不把本章结果补成它们已给的参数或原fit已复现。后续若要推进F23 χ²不闭合，最高信息是准确重建与fit章节，不是修一处公开源码后直接重报τ。

## Knowledge Impact and Learning Decision

`revises`把19000µm当已证几何错误；`supports`按作者实际input/σ/SNR与归一窗口核；`limits`单longlivedbenchmark和文件公开对完整实验CI的保证。新claim全needs_review，无human-reviewed/新实验τ/BR/spin/CI。只为Day17窗口内Day18知识preview，不授18或打开19。

## Extracted Pages

[[evasions-2023-public-release-native-readiness]]、[[fougeres-2023-mg23-velocity-difference-lifetime]]、[[lifetime-strength-audit-165tm-136nd]]、[[doppler-shift-attenuation-method]]。
