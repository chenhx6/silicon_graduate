---
type: source
title: "Saastamoinen2011学位论文：23Al低能质子、β背景与分支分母"
title_original: "Studies of Tz = -3/2 Nuclei of Astrophysical Interest"
aliases: [Saastamoinen2011 thesis, SA11 Al23 proton response]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: phd-thesis
reading_depth: skimmed
authors: [Antti Saastamoinen]
year: 2011
institution: University of Jyväskylä
citation_key: ""
canonical_source: "JYX Research Report9/2011 ISBN9789513945565 targetedAl23/response/AppendixA"
source_url: https://jyx.jyu.fi/jyx/Record/jyx_123456789_40105
raw_file: raw/theses/day17-20261020/saastamoinen-2011-thesis.pdf
raw_sha256: 53050e00d906ee42d7e4bf15d80feafbebc4e2c52ecfffd451eb432afdcb197c
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [23Al, 23Mg, 22Na]
reactions: [23Al-beta-delayed-proton-decay]
methods: [beta-decay, gamma-spectroscopy, implanted-detector-response, background-subtraction]
tags: [branching, spin, covariance, response, lifetime-companion]
---

# 每次β衰变的质子强度与激发态的质子份额不同

## Bibliographic Record

Antti Saastamoinen，University of Jyväskylä Research Report9/2011，2011年12月学位论文，电子ISBN978-951-39-4556-5。[JYX官方记录](https://jyx.jyu.fi/jyx/Record/jyx_123456789_40105)直接提供[公开PDF](https://jyx.jyu.fi/bitstreams/66f77d37-d92f-409a-bd6b-f05eb749ead1/download)。实际112页、7996041bytes，缓存`tmp/day17-saastamoinen2011/saastamoinen2011-thesis.pdf`，hash见frontmatter；raw槽不改。

原拟读PRC83 045808(2011)/[DOI10.1103/PhysRevC.83.045808](https://doi.org/10.1103/PhysRevC.83.045808)，当前正文未得：TAMU仓储403、APS harvest401、OSTI只有指向DOI的“Accepted Manuscript”链接、arXiv exactDOI0。学位论文Sec5.3自称依据该文的brief overview，没有期刊重印。它是作者对本实验的primary说明，却不能冒称期刊全文/VoR或新增独立采集。[下载身份](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/saastamoinen2011-thesis-download-identity.json)。

## Scope and Reading Depth

frontmatter/摘要/目录后另冻章节回忆，承认K16/capture/官方记录priming；实际读PDF52–60的Sec4.2、PDF69–78的Sec5.3、PDF97–103的AppendixA及相关refs，关键PDF57/58/73/74/77/78/98/100/101/103视觉核。未读112页全文或其它结果章节；4.2中31Cl装置/时间段只作上下文，不执行其它课程卡。[actual scope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/saastamoinen2011-thesis-reading-scope.json)。原23Al事件、原fit/背景histogram、实际脚本与完整Cov未得。

## Experimental or Method Setup

SetupI为69µm W1 DSSSD、16×16 strips与998µm Si pad，45°安装，单70%HPGe约11cm；Al degrader控制23Al植入深度，42AMeV束限制到600–800pps，约17µm深度FWHM。质子/β同pixel求和，front/back一致与multiplicity1等条件清背景。低能仍借22Mg无p背景响应，测得谱不是纯proton kinetic energy或可直接套外源detector峰。

## Summary

Table5.4低能行的0.32(6)是相对每100条451γ的质子强度；乘外部绝对451γ强度43.3(1.0)%约为每次23Al β衰变0.13856%，不是Γp/Γtotal。Fig5.7再与该态两条γ相对强度6.63/1.53比较，才得到约3.77%的条件daughter质子份额。作者据旧寿命和自旋解释推宽度/强度，此链混合多实验输入，不是本次直接测了τ/ωγ。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SA11-1 | 实际JYX112页论文仅定向4.2/5.3/AppendixA/refs，Sec5.3称依据PRC83045808的overview；期刊body未得且无重印，不冒全文或独立实验。 | identity-and-readiness | direct-thesis | PDF1/18/69；reading-scope | true |
| SA11-2 | 23Al用69µmW1/998µm pad/45°/HPGe11cm，beam42AMeV600–800pps与17µm implantation FWHM。较薄/较小pixel减少β背景，不与其它setup的响应/阈值混用。 | actual-response-identity | direct-thesis | PDF52–59 Sec4.2；Figs4.3/4.7 | true |
| SA11-3 | Eq4.3/4.4 Eobs包含p、recoil ionization k/Mrecoil项及β沉积，k由TRIM；proton escape与βhigh-tail另有Geant4/经验shape。Table5.4 measured214(11)与EpCM206(11)为不同对象，不把前者当新resonance labEp。 | measurement-variable-contract | direct-thesis | PDF56–59 Eqs4.3–4.5；Table5.4 | true |
| SA11-4 | 21Mg外标及Al23两内部p线校能，multiplicity1/front-back一致切成256pixels；低p背景仍到约400keV，借22Mg响应减除。作者将旧低能noise解释为峰的说法为其判断，不是本任务已查旧raw。 | observed-spectrum-and-author-counterinterpretation | direct-and-author-interpretation | PDF71–72；Fig5.6 | true |
| SA11-5 | Table5.4十二行相对451γ强度乘外部I451abs43.3(1.0)%给absoluteβp；低行.32(.06)→.13856%，近打印.14(.03)%。全表打印sum1.22(.05)%与名义乘积1.21673%分列，共同I451输入并非十二次独立测量。 | denominator-and-common-normalization | direct-and-reconstruction | PDF73 Table5.4；exercise rows | true |
| SA11-6 | Fig5.7该态p .32、7336γ6.63、5736γ1.53均per100451γ，名义归一Bp.0377358、两γ.781840/.180425；作者prose3.7/78.2/18保留，不强称最后位完全闭合。absoluteβp.14%不能替Bp。 | matched-daughter-channel-normalization | direct-and-reconstruction | PDF74 Fig5.7；PDF77；exercise daughter fractions | true |
| SA11-7 | 固定mean10fs/J7/2/仅所列pγ支，本任务得Γp2.48382、Γγ63.33738、omega1.36577meV，近作者2.5(1.1)/63(20)/1.4(+.5,−.4)。这是中心条件重构，原joint误差/旧τ系统未复现，不是新宽度/τ/CI。 | conditional-width-and-strength | task-derivation | PDF77；exercise fixed_tau_J_width_control | true |
| SA11-8 | 作者把低group归7787而非16keV旁IAS，依据energy/feeding及isospin；典型p分辨30keVFWHM仍不能排小IAS贡献。不能以resolution比spacing或母态名字直接认event-level唯一分离。 | near-parent-identity-boundary | direct-and-author-association | PDF71–72；Fig5.7 | true |
| SA11-9 | 作者以allowedβ给3/2/5/2/7/2，再因L2不利与IAS/IMME混合论证偏好7/2。角动量/正parity本身仍允许J3/2的L2通道，同J5/2也不强制大混合矩阵元；排除依赖额外宽度/混合动力学，不能当纯selection-rule测定。 | spin-interpretation-and-necessary-companion | author-interpretation-and-task-selection-rule-control | PDF77；exercise allowed_channel_angular_momenta；M23-4 | true |
| SA11-10 | 作者说低p背景减除会影响强度、约20%尺度，但本混合omega误差主要来自旧τ；提出新寿命以区分directcapture。gamma来自Zhai2007/Iacob2006、τ来自J04，非本次三项独立观测；作者“低p不太可能遗漏”是解释非完整eff/Cov证明。 | shared-input-and-readiness | direct-author-boundary | PDF78；Refs92/93/111 | true |
| SA11-11 | AppendixA用Rebin1→4keV、ShowBackground→Smooth、150keV匹配（试120–190）后Add缩放/减去22Mg；原ROOT版本注5.22。matching由数据估计，scale/shape与误差不保证独立；原脚本/实际API执行未得。 | actual-background-procedure | direct-thesis | PDF97–100 SecA.1/2；FigA.1 | true |
| SA11-12 | EqA.2给data+bkg方差，prose称各ROOT步骤传播errors、最后约16%而裸Poissonfit约2%/另一估计13%。该断言需要版本代码/实际scale和smoothingCov核，不把Sumw2对角buffer等同完整Cov；尚未读代码不先判实现错误。 | statistical-contract-to-verify | direct-and-readiness | PDF100 EqA.2/footnote2 | true |
| SA11-13 | EqA.3字面exp(−λ/2+exp(−λ))在λ→−∞增长，不能作为全轴归一的Moyal/Landau密度；作者称近似fit相关能域。实际fitcode未得，不猜其实现或把印刷边界叫实验失效。 | literal-formula-and-domain-boundary | direct-formula-and-asymptote | PDF101 EqA.3；FigA.3 | true |
| SA11-14 | 声明共同I451-only误差的12×12外积Cov为ri rj sigmaI²，总和贡献.0281个百分点；它不是原fit全Cov，也不能由打印sum误差.05反推不存在背景/eff/ratio相关。 | conditional-common-calibration-covariance | task-derivation | exercise common_I451_only_covariance_percent_squared | true |
| SA11-15 | 后续真实v5-22-00代码审计显示Smooth不改stored errors、ShowBackground clone/reset后只写content；原表达式/当前ROOThelper组件核两buffer分支。故“所有步骤自动传播”不能保证完整Cov，但exactpatch/原script未得，不据此断言本16%用零背景error或重报实验BpCI。 | actual-software-companion-and-revision | direct-code-and-component | R522-1/2/3/4/5/8/11 | true |
| SA11-16 | 新Fougères2023实测BRp.68(.17)%并引Friedman2020 .65(.08)%，显著不同于本旧pγ条件约3.7%；该旧结果保持历史/同源字段，不当当前唯一branch。新论文仍assumeJ7/2，2020primary未读，不从转引猜旧背景错因。 | new-independent-primary-companion | direct-original-companion | F23-8/9/10/11/18 | true |

## Analytical Reconstruction and Self-Audit

[算前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/saastamoinen2011-thesis-exercise-before.md)、[真实字段/hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/saastamoinen2011-thesis-exercise-contract.json)、[程序](../../system/scripts/day17_saastamoinen2011_thesis_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/saastamoinen2011-thesis-exercise-result.json)保存两层分母、固定宽度与角动量允许集合。所列gamma共同scale可在daughter归一消掉；不同实验的效率/绝对馈入/背景不因此全消。

Jtarget3、sp1/2给channel spin5/2或7/2；L0只产生相同J，L2允许J3/2。故观测p只说明该通道有幅度，若要靠L2势垒排除需独立partial width/单粒子上界/半径与测量误差。作者IMME论证也须实际混合矩阵元和质量精度模型；本文不以通道“允许”反过来证明任一J。

## Competing Interpretations and Limitations

原PRC全文、实际events/校准响应/模板/fitΣ和ROOT5.22 exactpatch+scripts仍缺。没有把作者thesis和期刊摘要当两个实验；Zhai2007/Iacob2006 γ输入与旧DSAM同源传播明确。source的7770 parity文字/旧spin标签保原版本，不拿来重写J04或当前Adopted。

下一高信息是AppendixA的实际ROOT5.22 API合同：Smooth/ShowBackground是否更新error，以及Add/scale如何处理共享归一和off-diagonal；只有读真实代码后才判断哪些自动传播主张成立。此问题直接关联Day17计数/共享校准及Day18companion，不另开课程卡。

## Knowledge Impact and Learning Decision

`revises`混淆绝对βp与daughterBp、将自旋偏好读成无条件选择律；`supports`匹配gamma/proton归一及独立寿命输入；`limits`背景减除后的净Poisson、打印方差与工具名对完整实验CI的保证。全部新claim needs_review，无human-reviewed或新实验分支/自旋/寿命/强度。

## Extracted Pages

[[kirsebom-2016-23mg-dsam-lifetimes]]、[[nndc-2021-mg23-lifetime-strength-reference]]、[[sallaska-2011-na22-absolute-resonance-strength]]、[[lifetime-strength-audit-165tm-136nd]]、[[linear-polarization-asymmetry]]。

## ROOT5.22公开API反证：内容改变不代表误差闭合

[[root-2008-v522-background-error-contract]] R522-1–11以真实tag/blob及原方法表达式组件核验：Smooth不修改stored errors；ShowBackground返回对象有buffer时可zeroerrors，无buffer则fallbacksqrtcontent。Add按固定系数传播diagonal，不含估计matching/平滑Cov。这里修订自动传播的一般保证，保留本页SA11-12的原报告/当时未读代码状态；仍不认证原exactpatch/job或重新计算16%/BpCI。

## 历史Bp不是当前唯一输入

[[fougeres-2023-mg23-velocity-difference-lifetime]] F23-8/9/10/11新directp/γ约.68%与旧条件约3.7%分列，旧branch/βp/背景记录不改。仍需原Friedman2020与实际响应/nearstate来判差异，不能从新推荐值补旧错误或将assume7/2升为自旋直接测量。
