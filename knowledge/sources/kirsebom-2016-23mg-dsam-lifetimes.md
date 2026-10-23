---
type: source
title: "Kirsebom2016：23Mg的DSAM、alpha能损与植入靶响应"
title_original: "Measurement of Lifetimes in 23Mg"
aliases: [Kirsebom2016 DSAM, K16 23Mg lifetimes]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: [O. S. Kirsebom, P. Bender, A. Cheeseman, et al.]
year: 2016
journal: Physical Review C
volume: 93
pages: 025802
doi: 10.1103/PhysRevC.93.025802
citation_key: ""
canonical_source: "Kirsebom et al 2016 PRC93 025802 arxiv1508.07188v1"
source_url: https://arxiv.org/abs/1508.07188v1
raw_file: raw/papers/day17-20261020/kirsebom-2016-23mg-dsam-arxiv-v1.pdf
raw_sha256: 9c4731688a6bfa1338ed229b8967ccb4f37bb11d067aed429ff2b4469a81673b
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [23Mg, 22Na, 24Mg, 28Si]
reactions: [3He(24Mg,alpha)23Mg]
methods: [DSAM, alpha-gamma-coincidence, line-shape, stopping-power]
tags: [lifetime, DSAM, calibration, implanted-target, response]
---

# 先传播粒子到探测器，再解释能量门

## Bibliographic Record

O. S. Kirsebom等，*Phys. Rev. C*93，025802(2016)，DOI [10.1103/PhysRevC.93.025802](https://doi.org/10.1103/PhysRevC.93.025802)。本次实际原件为[arXiv1508.07188v1](https://arxiv.org/abs/1508.07188v1)，提交28Aug2015，十三页；没有取得期刊VoR。PDF日期14Aug2018来自源码`main.tex`的`\date{\today}`，不当作2018新实验或新版本。元数据/原PDF/源码包均实际核，源码包SHA256`851542fe0d82ecbaf5db4f1e8dedd3b2367913f7be8b3a9895bc5519c1db9ae6`。

原PDF缓存`tmp/day17-kirsebom2016/kirsebom2016-arxiv-v1.pdf`，hash见frontmatter；只读取源码包白名单main/body tex，没有任意解包。raw与Bib保持不变。[下载身份](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/kirsebom2016-download-identity.json)与[实际阅读范围](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/kirsebom2016-reading-scope.json)区分arXiv、期刊metadata与公开程序。

## Scope and Reading Depth

承认Sun/IAEA/SDK与alpha-gate练习的strongpriming后冻结回忆，实际原读十三页全部主线/参考文献、Figs1–21、TablesI–II、Eqs1–4；全部页面视觉核。TableII十三行按原标签/拟合Eγ/meanτ或limit保存，没有把低精度Ei标签反推成新精确能级。Forster1976、Alexander1981等上游primary正文未读。 v1参考文献右列部分行被裁切，未把Ref25/27/30/33缺失字段补成已核bibliography。TableII十三态中Figs10–20只展示十一幅寿命谱，6236/7444保留TableII locator，不凭空分配图号。

后续取得论文公开SimDSAM项目，另在[[simdsam-2015-public-dsam-code]]记录版本/输入/组件。公开代码的读取和执行不反过来认证这份预印本对应的最终实验job、原counts/Cov或期刊最终稿。

## Summary

论文在24Mg+3He逆运动学中用alpha门压feeding，利用Monte Carlo描述有限几何、阻止、植入层和多重散射，测出四项有限寿命并给九项上限。核心7787态只有τ<12fs的95%上限，作者明确它不足以解决22Na(p,γ)强度争议。同设施的alpha出靶能损和响应合同可作Sun的必要companion，不能直接迁移具体门值/靶参数或producer。

## Experimental or Method Setup

3.125AMeV的24Mg束，30keV3He植入22.6(.2)µm Au，dose6.6×10¹⁷cm⁻²；SRIM深度峰.07µm、尾到.15µm。Si telescope为100/500µm，中心点几何alpha0–8°；有限束斑与多重散射可使更大实际发射角被接收。四晶HPGe在7.83cm处，角覆盖约32°。这些参数均与Sun的32S/87µm/1mm/35keV植入/25µm foil分开。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| K16-1 | 实际body为2015arxivv1十三页，journalmetadata2016；PDF2018日期来自date-today，不增实验/版本。完整21图/2表/4式已读，VoR未得。 | identity-and-reading-scope | direct-original | PDF1；source main.tex date；reading-scope | true |
| K16-2 | 实验为75MeV24Mg/3He→alpha23Mg，30keV植入22.6(.2)µmAu/dose6.6×10¹⁷，depth峰.07/尾.15µm；100/500µmSi与HPGe7.83cm/约32°，不能当Sun原geometry。 | experimental-input | direct | PDF2–3 SecIII；Figs2–4 | true |
| K16-3 | 源中心点alpha aperture8°，束斑直径约2.5mm可接收到13°实际角，再叠multiple scattering；与一个硬8°或13°角cut不是相同接受算符。 | finite-geometry-and-acceptance | direct-and-author-model | PDF3 SecIII；PDF5 beam-emittance/multiple-scattering | true |
| K16-4 | 作者估计表面凝结约.2µm water-equivalent使beam降.25MeV并产生背景，也提供28Si6877.88keV/escape校验线。±1keV高能标定/gain<±.5keV与稳定yield是本实验控制，不迁Sun。 | calibration-and-contamination | direct-and-author-interpretation | PDF3–4 SecIII；Fig5 | true |
| K16-5 | 高能intrinsic Gaussian、低能另加skewedGaussian/step；FWHM≈3.3keV(E/MeV)^.52。TableI δE/E是作者粗略重要性估计，非可独立quadrature的GaussianΣ；HPGe接受项6‰大于1fs效应.12‰。 | response-and-error-semantics | direct | PDF4–5 SecIV；Fig6；PDF7 TableI | true |
| K16-6 | MC为ROOT/C++，逐样本beam/depth/CM角/指数lifetime，传播alpha到出靶、recoil到decay；Geant4用于gamma能角效率。不能将“有Geant4”理解为本文完整原生Geant4transport。 | actual-model-roles | direct | PDF5–7 SecV；Fig7 | true |
| K16-7 | Eq4同时含He贡献和swelling降density：c_peak1.05，A=.75(.25)，Auρ19.30；Au取Forster实验表±4%、He取SRIM并cubic-spline。不是纯Au常数scale，也不自动认证两个输入独立。 | stopping-mixture-and-lineage | direct-and-author-model | PDF7 SecVI；Eq4；Refs19/23/29 | true |
| K16-8 | alpha出靶后测量谱：2908gamma门给Ealpha≈32MeV，计入约4MeV金靶能损后才与vertex曲线相合；7787对应约21MeV。它直接反证忽略粒子输运的门映射，不能把4MeV补给Sun。 | necessary-companion-and-counter-evidence | direct | PDF7 SecVII；Figs4/9 | true |
| K16-9 | alpha能量总分辨约1MeV FWHM→Ex约.5MeV；示例alpha门2.4MeV。fit用maximumlikelihood，自由normalization/background/energyshift，shift限±(σtab+σcal)为和而非quadrature。 | selection-and-fit-contract | direct | PDF7–8 SecVII；Figs9/12/20 | true |
| K16-10 | 2908τ15(3)fs中角分布项±2fs与统计quadrature；其它系统误差作者称ad-hoc，变gate/background/fitrange/MC参数，数据不支持全面sensitivity。去energyshift约束使2908中心12fs、7787limit14fs，原15/<12并非无条件不变。 | systematic-and-counter-fit | direct | PDF8–9 SecVII–VIII | true |
| K16-11 | TableII十三项为四finite104(18)/98(15)/15(3)/41(6)fs与九个95%upperlimit；7787<12同时兼容旧10(3)及作者从Seattle强度推的约2.4fs，明确未裁决rate争议。 | reported-result-and-limit | direct-and-author-interpretation | PDF9–12 SecVIII/IX；TableII；Fig20 | true |
| K16-12 | v1前文/讨论打印Bp=.037±.07，结论为±.007且文字相对19%；该内部差异在tex也存在，不能静默修成新primarymeasurement。Eq1还依赖J与Bp，源>1.1meV/95%标签不保证本任务已恢复jointcoverage。 | printed-inconsistency-and-boundary | direct-original | PDF1/9 Bp；PDF2 relative19%；PDF12 conclusion；Eq1 | true |
| K16-13 | 固定Bp=.037/J7/2/τ12fs时Eq1算ωγ≈1.11680meV；J5/2为.83760meV。只重放条件中心输入，不把τ单独95%界直接变成含Bp/J不确定度的新95%联合界。 | conditional-strength-reconstruction | task-derivation | exercise-result fixed_central_Bp_strength | true |
| K16-14 | Fig21模拟把alpha8→16°/gamma32→16°，理想cone Ω乘积比≈1.01479，仅近似保统计；更宽alpha门会损Ex分辨/增背景/角分布敏感。不能仅以gamma线变窄认定完整实验FOM改善。 | design-model-and-countertradeoff | direct-and-task-geometry | PDF11 Fig21/discussion；exercise-result geometry | true |
| K16-15 | PDF/source均写t=∫γds/v，公开代码也用gamma/v；通常properclock为∫ds/(γv)，恒β下两者比γ²，在源β范围约1.00349–1.00677。当前是公式/软件合同边界，不给原τ简单重标或判实验CI偏差。 | literal-clock-and-conditional-control | direct-code-companion-and-task-derivation | PDF6–7 SecV/Fig7；SD15-5；exercise-result clocks | true |
| K16-16 | 本文、公开代码/响应表与Sun同设施有共享方法/设备/Forster/SRIM依赖，反应和采集对象不同；未得原experimentalhistograms/fitCov/完整job。公开代码输入的GEANT表/束斑等与正文有差别，README used-for-analysis不是exactjob认证。 | independence-and-readiness | primary-and-code-boundary | SD15-1/3/4/6/8；PDF5 SecV | true |
| K16-17 | 实际IAEA Forster24Mg/Au十点使原about8.5MeV/µm可核：1.6MeV/u给8.4341；publicGEANT reader在1.6/2.0邻点与compiled值约2%内相容。defaultlabel与正文不同并不等已证数值冲突，actualjob/Cov与primary误差定义仍缺。 | actual-reference-companion-and-revision | direct-compilation-and-native | ISP26-14/15/16/17 | true |
| K16-18 | 公开原eventmain已生成并严格重放有界64条MODEL联合alpha-gamma包，schema/条件proposal分母可核；没有取得本实验ROOTanal/experimentalhistograms/Cov或exactjob，模型流不能冒称原数据/置信区间。 | public-producer-data-readiness | native-companion-and-boundary | SD15-17/18/19/20/21 | true |
| K16-19 | Ref29准确身份为Alexander等J.Nucl.Mater96,51–56(1981)，DOI10.1016/0022-3115(81)90217-8；实际只metadata/OA发现，primarybody未得。其题名提DSAM，不据此断言A独立性/循环校准或补原calibrator/误差语义。 | property-input-identity-and-readiness | metadata-only-companion | PDF13 Ref29；alexander1981-crossref-discovery/primary-readiness | true |
| K16-20 | 新本session原读Jenkins2004四页，核其10(3)fs为七角fractional-Doppler加模型、feedingdirect假设；其Tableomega1.8(.7)adoptedAngulo而非新τ推出。原J04prose说finite-recoil已校，K16二级评论旧Ex似未校须定义/版本桥，不据此直接改数据。 | independent-primary-companion-and-revision | direct-original-companion | J04-3/5/7 | true |
| K16-21 | 新202101五official对象把K16九upper/两未平均finite按mean×ln2转half，前两finite另与旧输入合并；7787<12mean与compiled<8.3half同源。Adopted自旋3/2+,5/2+还保留fusion7/2意见，不能把本模型旧J7/2固定成无条件事实。 | official-matched-reference-and-spin-boundary | direct-evaluation-and-reconstruction | M23-4/5/6/8/9/13/14 | true |
| K16-22 | 原读Sallaska2011二十页给直接capture强度的积分/NT/beam/eff及弱模板合同；完整强度积分减少absolute-stopping但弱上限/energy/tail仍含停止/response。K16<12仍不裁决旧强度争议，不把新source中心与旧固定J/Bp拼实验τCI。 | actual-strength-companion-and-shared-boundary | direct-original-companion | S11-2/8/9/11/12/13/15/17 | true |
| K16-23 | 作者Saastamoinen2011 thesis定向原读给低p相对451γ.32(.06)与γ6.63/1.53，daughterBp≈.03774而absoluteβp≈.14%；旧τ/J条件重构omega≈1.366meV不作新测量。spin7/2含势垒/IMME解释、30keV分辨不能排小IAS；原PRCbody/完整Cov仍缺。 | actual-branch-companion-and-boundary | direct-author-thesis-and-reconstruction | SA11-5/6/7/8/9/10 | true |
| K16-24 | 新本session完整原读Fougères2023主7/SI8及真实图数据，独立GANIL τ11(+7,−5)近旧值，但新BRp.68(.17)%/假J7/2使推荐omega.24meV。新tau/新branch与recommended旧新平均分列；sourceData显示区χ²/零grid不闭合待producer，不据此重算K16或新实验CI。 | independent-new-primary-and-reference-revision | direct-original-and-data | F23-3/5/8/9/10/11/15/16 | true |

## Analytical Reconstruction and Self-Audit

[原打印输入合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/kirsebom2016-exercise-contract.json)、[程序](../../system/scripts/day17_kirsebom2016_contract.py)和[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/kirsebom2016-exercise-result.json)保存TableII全部十三行、constant-β时钟、Eq1/4和Fig21控制。

Eq4除以纯Au线性阻止后，`R=[1+(3/197)c r]/[1+A c]`，r为He/Au质量阻止比。只取density部分，c=1.05、A=.75给.55944；A=.5/1给.65574/.48780，这些是参数端点敏感性，非新置信区间。总效应还需He项：净R=1的临界r=197A/3，central为49.25，故不能只凭swelling就断言总阻止下降固定比例。

TableII逐行账本如下；Ei/Ef保留原旧评价标签，Eγ与τ是作者本次拟合报告，不能由标签差反定新精确能级。上限均为作者95%标签，本任务未复现其coverage构造。

| Ei keV | Ef keV | Eγ keV | meanτ fs |
| --- | --- | --- | --- |
| 2052 | 451 | 1601.4±1.3 | 104±18 |
| 2771 | 0 | 2769.7±1.2 | 98±15 |
| 2908 | 0 | 2906.4±1.1 | 15±3 |
| 3798 | 451 | 3343.9±1.3 | 41±6 |
| 4353 | 0 | 4356±2 | <11 |
| 5287 | 451 | 4837±3 | <14 |
| 5453 | 2052 | 3401±2 | <15 |
| 6236 | 2052 | 4186±3 | <40 |
| 6375 | 2052 | 4322±6 | <45 |
| 6899 | 0 | 6907±3 | <10 |
| 7444 | 0 | 7443±3 | <14 |
| 7493 | 2052 | 5442±2 | <20 |
| 7787 | 451 | 7335±2 | <12 |

源短时近似给1fs δβ≈1.18261×10⁻⁴，对7336keV线shift≈.8676keV；FWHM函数在7.8MeV给约9.60keV。均为作者输入的算术量级，不能用它们把TableI各项当独立σ重算CI。原properclock与publiccode的局部问题、beamspot/变量角色另见[[simdsam-2015-public-dsam-code]]，原source保持不改。

## Competing Interpretations and Limitations

- 7787的upperlimit兼容争议两端，不是证实某一强度；J/Bp/τ与原方法误差共同限制rate结论。
- 有alpha门能压feeding，不代表已经知道无间接feeding、角接受/energygate正确或背景无关。
- 4MeV是此反应/foil/energy的作者解释，不能迁Sun；同设施不等相同response/校准数据。
- 原experimentalcounts、actualfit/Σ/置信构造细节和对应job输入未齐。只允许conditional exercise/组件，不写新τ、B、强度或95%CI。

## Knowledge Impact and Learning Decision

`supports`粒子门前需物理传播、植入层需要独立物性输入；`revises`将Geant4名称等同完整transport、将窄线/upperlimit视为已解决rate争议；`limits`本文对Sun实际门/response的迁移。所有新增claim保持needs_review，原件/模型/作者解释/本任务推导分开。

## Extracted Pages

[[simdsam-2015-public-dsam-code]]、[[sun-2023-bayesian-dsam-31s]]、[[doppler-shift-attenuation-method]]、[[lifetime-strength-audit-165tm-136nd]]、[[iaea-2026-stopping-s-au-o-ta-records]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]。当前只为Day17窗口内Day18无学分预习，不计新课程卡。


## Forster实际编译输入补充

[[iaea-2026-stopping-s-au-o-ta-records]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]] ISP26-14–17补24Mg/Au十个真实编译点和原publictable reader对照。物理输入身份没有因此闭合成paperexactjob，但邻近recoil能量的数值并未显示label差异所暗示的必然冲突。Forster原件未读、quoted4%置信定义/Cov和24Mg到23Mg的速度/同位素/混合靶合同仍保持。

公开MODEL packet及其限制见[[simdsam-2015-public-dsam-code]] SD15-17–21。Ref29植入物性原源的[当前readiness](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/alexander1981-primary-readiness-boundary.json)只核身份：OpenAlexclosed、NRC无结果、OAonly0正文；未读其方法/校准寿命/停止模型/共享Cov，仍不能认证A=.75(.25)是可独立迁移的Gaussian物性先验。


## 独立融合蒸发primary：τ与旧强度分列

[[jenkins-2004-23mg-fractional-doppler-rate]] J04-1–14实际原读，确认旧10(3)fs的具体centroid/model/feeding链，也确认omega1.8(.7)是adopted输入。这里的K16重测、J04原采集与对J04的转载须分别计证据。K16对旧energy recoil的解释还需与J04原文明确说已校正的prose匹配photon/levelgap语义，不能把二级评论直接升级成原source实验错误。

## 官方字段补充：上限同源，自旋仍需条件化

[[nndc-2021-mg23-lifetime-strength-reference]] M23-4/5/6/8/9/13/14核half/mean与新强度角色。新upper不裁决旧mean10(3)；J7/2是旧fusion条件，Adopted还列3/2+,5/2+。用任一spin/omega/τ中心组合计算Bp仅是条件模型，不能借编译作本实验联合CI。

## 直接capture原件：避免绝对stopping的范围

[[sallaska-2011-na22-absolute-resonance-strength]] S11-2/8/9/11/12/13/15/17核完整积分/束密度/靶原子数/效率链，弱模板和energyloss仍含stopping。它给K16寿命换强度的真实companion及共享边界，不替K16原line-shape/fitΣ或用新omega中心裁决旧τ。

## 作者thesis中的Bp分母与自旋条件

[[saastamoinen-2011-thesis-al23-proton-response]] SA11-1–14定向原读说明低p.14%是perβ强度，约3.7%是与该态两γ归一后的daughterbranch。其误差/背景、同源gamma/旧DSAM和7/2动力学解释不能省略；不是新原期刊body或独立tau/Q测量。

## 新GANIL输入：τ相容，BRp已另测

[[fougeres-2023-mg23-velocity-difference-lifetime]] F23-1–20实际新原件/公开data改变companion：tau11(+7,−5)与旧10(3)相容，但branch约.68%而非旧3.7%；推荐强度含旧新组合与7/2假设。真实图/衍生event可核，不等原fit已复现；不把sourceData初不闭合反投为K16实验错。

## Day19量化审计：Meyer-Sigmund核多次散射理论、Blaugrund投影速度修正与DSAM线形多普勒偏转失真定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_meyer_sigmund_multiple_scattering_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/meyer-sigmund-multiple-scattering-result-068.json`，核准了针对 Kirsebom 2016 反应体系中核多次散射与角离散的微观动力学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| K16-D19-1 | 对 Kirsebom 2016 $^{24}\text{Mg}+^3\text{He} \to ^{23}\text{Mg}+\alpha$ 反应中金衬底核多次散射与 Blaugrund 投影速度折减执行严格微积分量化审计：(1) Meyer 1971 / Sigmund 1974 理论重构：在 $E_{\text{beam}} = 75\text{ MeV}$（反冲能 $\sim 40\text{ MeV}$）下，穿行 $1\ \mu\text{m}$、 $5\ \mu\text{m}$、 $20\ \mu\text{m}$ 金靶时，约化厚度 $\tau$ 由 $17.19$ 增至 $343.74$，诱发核多次散射半高宽急剧发散为 $\text{FWHM} = 3.69^\circ$、 $9.12^\circ$ 与 $19.87^\circ$（$\sigma = 8.44^\circ$）；(2) 质量比反差定理：Blaugrund 速度折减因子指数正比于质量比 $M_2 / (2 M_1)$。对轻核 $^{23}\text{Mg}$ 在 Au 中，该比值为 $197 / (2 \times 23) = 4.283$，相比中重核 $^{131}\text{Ce}$ 在 Au 中（$0.752$）展现出 $5.70$ 倍的强烈放大效应，实证轻核多普勒线形对核散射的极度敏感性；(3) Blaugrund 投影折减因子 $\langle \cos\theta \rangle(v)$：微积分证明由于低能区核阻止 $S_n$ 剧增，沿前向投影速度 $v_z(t) = v(t) \langle \cos\theta \rangle(t)$ 从初态的 $1.000$ 单调剧降至慢化末端的 $< 0.01$；(4) 分数多普勒频移 $F(\tau)$ 压制：核散射在典型 DSAM 测量窗口（$\tau \approx 0.1\text{--}0.5 t_s$）使前向多普勒频移压低 $16.4\%\text{--}28.9\%$（绝对频移降幅 $\Delta F$ 高达 $-0.2891$）；(5) 核多次散射能级寿命高估定理：微积分严格证明若在线形拟合中忽略核散射角偏转（假定直线减速），为拟合实测的较小频移，分析者将严重高估核能级寿命（$\tau_{\text{fit}} > \tau_{\text{true}}$），在 $\tau \approx 0.2 t_s$ 处虚假高估达 $+35.2\%$；(6) 孔阑横向几何泄漏：Marwick-Sigmund 1975 横向弥散在 $20\ \mu\text{m}$ 靶深达到数微米，与束斑发射度卷积后将源中心点 $8^\circ$ 几何孔阑实际拓展至 $13^\circ$，推翻硬孔阑截断假定；(7) 前向多普勒峰红移非对称拖尾：在 $0^\circ$ 探测角，Rayleigh 散射角分布通过 $\cos\theta \approx 1 - \frac{1}{2}\theta^2$ 赋予光子能量固有的负偏度（$\text{Skewness} = -2.000$），从第一性原理阐明了前向全多普勒峰低能端长拖尾的物理机制。 | task-kirsebom-multiple-scattering-audit | derived-and-boundary | PDF3-7 SecIII-VI; meyer-sigmund-multiple-scattering-result-068.json | true |

## Day19量化审计：23Mg飞秒寿命对账、传统DSAM线形阈值与天体速率坍缩机制

**checkpoint088：撤回旧科学认证；原标题保留为历史anchor。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| K16-D19-2 | checkpoint085修订：TableII实际13态，其中四项有限寿命、九项95%上限；旧脚本遗漏6899→g.s.的6907(3)keV、tau<10fs一行。7787的<12fs不能当有限独立测量参与综合；40与41fs中心接近不证明跨装置绝对标尺无偏。未证传统DSAM普遍15fs死线、DVDM亚飞秒能力或逐event消除停止/散射依赖。固定两通道与J=7/2时omega gamma=(4/7)hbar Bp(1−Bp)/tau，推荐中心.241766meV而旧脚本漏(1−Bp)得.243；95.5%归因未计算，撤回。模型新星产额不当实测天文信号。 | source-and-analysis-correction | direct-where-reread-otherwise-withdrawn | checkpoint088 source scope and rejection registry | true |

## checkpoint088：十三态表与完整宽度分支

本轮定向原读并视觉核PDF10 TableII/Figs15–18；K16原文与F23的不同采集/共同停止知识仍分开。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| K16-D19-3 | TableII共13态=4有限寿命+9项95%上限，含6899→g.s.的6907(3)keV、tau<10fs。7787→451为7335(2)keV、tau<12fs。上限不是额外mean tau测量，不能据三个中心/limit相近认证所有系统无偏。固定J=7/2且只计p/gamma通道的强度公式含Bp(1−Bp)，用F23推荐中心给.241766meV；该算术不重建原fitCI或消除stopping/branch/spin依赖。 | literal-inventory-and-conditional-width | direct-original-and-task-derived | PDF10 TableII; F23-11 | true |
