---
type: source
title: "Sallaska2011：22Na绝对共振强度、完整积分与共享校准"
title_original: "Absolute determination of the 22Na(p,gamma)23Mg reaction rate in novae"
aliases: [Sallaska2011 Na22, S11 absolute capture strength]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
authors: [A. L. Sallaska, C. Wrede, A. García, et al.]
year: 2011
journal: Physical Review C
volume: 83
pages: 034611
doi: 10.1103/PhysRevC.83.034611
citation_key: ""
canonical_source: "Sallaska et al PRC83034611, arxiv1009.3925v2"
source_url: https://arxiv.org/abs/1009.3925v2
raw_file: raw/papers/gpt/learning-daily/20261020-DAY18-dsam-lifetime-strength/sallaska-2011-na22-arxiv-v2.pdf
raw_sha256: 19a8218ff8c0199409b785dad7ee036445db1b299b2c4b9ab2dc62d6e360efc5
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [22Na, 23Mg, 23Na]
reactions: [22Na(p,gamma)23Mg, 23Na(p,gamma)24Mg]
methods: [gamma-spectroscopy, resonance-strength, absolute-calibration]
tags: [lifetime-companion, stopping-power, covariance, branching, response]
---

# 完整积分减少一项依赖，绝对归一仍需要证据

## Bibliographic Record

A. L. Sallaska等，*Phys. Rev. C*83，034611(2011)，[DOI10.1103/PhysRevC.83.034611](https://doi.org/10.1103/PhysRevC.83.034611)。实际原件为[arXiv1009.3925v2](https://arxiv.org/abs/1009.3925v2)，4Feb2011版，20页；未取得期刊VoR。v1于20Sep2010提交。PDF的24Mar2022正文日期及17Apr2022生成metadata不作新实验，官方源码`longpaper_accepted.tex`的`\date{\today}`已核。

PDF缓存`tmp/day17-sallaska2011/sallaska2011-arxiv-v2.pdf`，hash见frontmatter；source包SHA256`593ae11f277ea77a5037a0adca008f414593f7695df9194e6f7c122ef99c5b18`，白名单tex SHA256`01c548ae4889181a5e21a750e26877de8c2c88a355f35e12f7916c9716694543`。不写raw或Bib。[PDF身份](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2011-download-identity.json)、[源码身份](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2011-source-identity.json)。

## Scope and Reading Depth

在声明K16/J04/NNDC强priming之后冻结回忆；本session读20页全部主线及参考文献、18图、6表、Eqs1–7；所有页视觉浏览，PDF10/16/18的caption、脚注、量化输入另放大核。[actual scope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2011-reading-scope.json)。未取得原excitation函数点、原计数/分析程序、Penelope输入或完整校准Cov。Ref29的2010PRL与其erratum仅识别引用，未读正文；本论文自称补充旧报告，不能计另一独立采集。

## Experimental or Method Setup

UW150–700keV质子、约45µA，TRIUMF30keV植入22Na到Cu，主靶加20nm Cr保护；5mm活动区由较大raster照满，ρb由Al coin/solid比较。±55°两只100%HPGe、26mm Pb和宇宙线反符合；radioactivity导致live time35–45%，以pulser校正。此实验是直接capture，与J04fusion/K16alpha-tagged DSAM采集不同，但后续混合率仍复用旧分支和模型输入。

## Summary

有限强度以每条γ的积分产额求partial，再求和；避免在单一峰值产额中显式依赖绝对停止功率和靶厚。代价是总照射靶原子数、束密度、效率和有限扫描尾部必须有合同。弱共振形状伸缩和能量损失仍用停止输入，不能把摘要的优势扩大到所有结果。该文直接观察213keV的第二γ分支，并把5732归于213而非J04的209候选；其68%上限仍有重叠与条件形状边界。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| S11-1 | 实际原件20页arxivv2 Feb2011，date-today解释PDF2022；完整18图/6表/7式已读。作者称补充2010报告/学位论文，不计独立重复实验；VoR/旧erratumbody未读。 | identity-reading-and-dependence | direct-original | PDF1–2；PDF20 Ref29/30；source date | true |
| S11-2 | Eq1为target与beam面密度重叠；uniform raster照满全部活动区时Eq2/3用总NT与ρb。完整beam-energy积分Eq4给2π²λbar²(m+M)/M NTρb omega，λbar为CM reduced wavelength。需要完整扫描与重叠条件，不等任意峰值/局部照射可免stopping。 | measurement-normalization-contract | direct | PDF2 Eqs1–4 | true |
| S11-3 | 主靶3/4有20nmCr，232用无保护旧靶；30keV植入、5mm活动区、raster条件与Cu基底均有身份。不同靶/积累charge会改变退化，不能用同一NTloss修正全部共振。 | actual-target-and-response | direct | PDF3 SecIIB；PDF8；Fig15 | true |
| S11-4 | 两HPGe±55°意在减小P2，finiteangle/CMlab与P4仍有贡献；作者模拟a2=1约2.6(.4)%、a4=.05约2.0(.4)%，另给3%angular项，总eff6%。名义55并非精确54.7356°，pointP4约−.385，不能称所有角分布消失。 | angular-companion-and-boundary | direct-and-declared-point-control | PDF4–6 SecIIE2；exercise nominal_angle_control | true |
| S11-5 | Penelope geometry在1332Co标定后后移Ge前脸1.7mm使之匹配，另用Na24/Al反应跨能量检验；5%isotropic项再加3%angular为6%。1.7%Co source注明99%CL，后续误差语义不能未经桥接全当同一SD。 | efficiency-calibration-and-confidence-contract | direct | PDF4–6；Fig4 | true |
| S11-6 | ρb由coin/solid Eq5测2.60(.09)/2.55(.10)cm−2，选2.58；MC可接受域2.33–2.83并给±.25系统尺度。MC与测量共享beam约束，不是第三次独立ρ测量。 | beam-density-companion | direct-and-author-systematic | PDF6–7 Eq5；Fig5 | true |
| S11-7 | Eq6先分别除live time再用η1+η2合并；radioactivity使live35–45%。加Na源Al控制从97%降50%而校正yield比.99(.02)，selfveto singles/反符合比较>99%一致。有效检查不证明所有门/能量/原Σ。 | actual-count-estimator-and-control | direct | PDF4 SecIID；PDF7 Eq6 | true |
| S11-8 | 213曲线最高点未到零，借454及三个610参考补最后梯形，补量为total的10(5)%。本任务故得total/observed1.1111，局部f-only相对尺度.05556；非额外独立实验误差或原尾部重拟合。 | finite-window-and-shared-template | direct-and-arithmetic | PDF11 SecIIIA3；exercise 213_tail_normalization | true |
| S11-9 | 弱198/232参考形状伸缩固定为Cu stopping比；209混合数据需按活动度缩放且5067/5055窗口重叠，最小χ²位置可能归198。上限改限制能量shift为J04±2σ，故不是无条件独立209峰检出。 | stopping-and-identity-counter-evidence | direct | PDF8–10；Figs12–14 | true |
| S11-10 | Eq7从exp(−χ²/2)二维grid沿E求和投影，再对非负omega归一积分给CL；不是profile最小化或自动证明frequentist coverage。grid/measure/Σ未得，不由图重建原likelihood。 | statistical-construction-and-readiness | direct-and-boundary | PDF9–10 Eq7；Fig14 | true |
| S11-11 | in-situ1275活动度不能独自追踪照射区NT：溅射Na仍可留在附近；reference面积与移靶前后残余活动共同约束loss。作者选198/213无loss中心但−5%边界，288取.88(+.12,−.06)，232取.59并给40%尺度。 | necessary-target-companion | direct-and-author-systematic | PDF11–12；Fig15；TableI | true |
| S11-12 | 共振能量另用TRIM2008.01修Cr20nm/Cu4nm损失约3–5keV并假20%stopping误差；γ法另校Doppler4–7、recoil.6–1.5及rate-dependentgain2.4–3.8keV。完整强度积分的优势不移除能量/弱模板停止依赖。 | energy-response-contract | direct | PDF12–13 SecIIID；TableII | true |
| S11-13 | TableIII213 finitepartial5.1(.5)/.6(.3)meV，对应7334/5732，branch89.4(5.3)/10.6(5.3)%；弱支形状强制同强支。5732归213的选择与J04归209不同，作者承认5067/5055重叠，不能只近能合并母态。 | actual-branch-and-placement-counter-evidence | direct-and-author-association | PDF14；PDF16 TableIII footnotef/g | true |
| S11-14 | TableIII finitepartial不含系统，observedbranch总和假100%；finalspin1/2的可疑2.2(1.6)被作者视stat fluctuation而不入total。其它upper直接增加totalupper，610的6112因F背景用旧branch20(1.8)%估118(13)partial，不是全部partial独立直接观测。 | inventory-and-model-selection-boundary | direct | PDF13–14；PDF16 TableIII footnotesa/h/k/l | true |
| S11-15 | TableIV给213 5.7(+1.6,−.9)、28839(8)、454166(22)、610591(+103,−74)meV；198≤.51、209≤.40、232≤.67均68%CL。低45/70由模型输入、503/740/796从旧值缩放，整表不是十二项新强度测量。 | measured-versus-limit-versus-scaled | direct | PDF17 TableIV/notes | true |
| S11-16 | 本任务按打印partial独立stat-quadrature加TableI系统、再linear加允许upper，213得−.8859/＋1.5895，288−8.038/＋7.970，610−73.907/＋102.907，接近打印；454约20.903而原22未闭合，保留残差，不调Cov/加被排支强配。 | rounded-input-budget-reconstruction | task-derivation | exercise rows | true |
| S11-17 | NT由1275/η1275，captureyield除ηHigh，故共同效率乘法尺度在η1275/ηHigh条件比中相消；实际完整Cov未得。五个声明scale代数控制通过，不足以指控原误差重复计数/替作者CI。 | shared-calibration-covariance | task-derivation-from-source-estimator | PDF5/11；exercise shared_efficiency_scale_control | true |
| S11-18 | Fig12caption把a232/b198与a5055/b7801+7350门对应，和Fig13/TableIII的物理分支相反；图轴/能级/正文另存，未静默更正PDF。SecV/TableV caption称upper16%/lower84%，而数值lower<central<upper，保留文字/数值不闭合。 | literal-label-boundary | direct-original | PDF10 Fig12/13；PDF15 SecV；PDF18 TableV | true |
| S11-19 | R由MC对finite对称/非对称Gaussian及Fig14分布采样，median与两个版本率表另列；SHIVA 22Na质量分数/探测距离变化为作者模型，不是天文检出或新核结构实验。原MCratecode/共享calibrationCov未得。 | model-result-and-dependence | direct-author-model | PDF15/17–19；Figs17/18；TablesV/VI | true |
| S11-20 | 作者23Na512控制得79(17)meV对旧91.3(12.5)，含约12%漏照区修正；它支持绝对方法在该条件可用，但靶错位误差大且共享标定，不证明22Na原系统误差完备或争议已独立裁决。 | counter-control-and-independence | direct | PDF13–15 SecIIIF；Fig16 | true |
| S11-21 | 新本session原读2010Letterv2四页并比较v1：Eq1/TableI源码同、rateEPS同；LetterlambdaLab²与本文Eq4CM定义有字面frame边界，NR桥须r²。正式2010erratumbody未得，不猜其内容或重标本强度；两报告仍同采集链。 | actual-shortreport-version-companion | direct-original-and-conditional-bridge | S10-1/2/3/4/5/6/9 | true |

## Theory/analysis exercise

[冻结输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2011-exercise-before.md)、[合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2011-exercise-contract.json)、[程序](../../system/scripts/day17_sallaska2011_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/sallaska2011-exercise-result.json)。实际打印预算控制保留454未闭合，未更改表/原raw或制造拟合CI。

完整积分的可复用条件推导：若扫描能量响应是归一且与能量无关的shift kernel，`Y(E0)=NT rho_b ∫k(u) σ(E0−u)du`，则全域积分为`NT rho_b ∫σ(E)dE`；有限窗口则有丢尾。这个声明条件模型解释Eq4的作用，不认证任意能变stopping、beam变化、漏照或实际有限扫描核均满足归一假设。213尾部和弱共振模板正是必须另查的输入。

当同一效率标定进入靶活动度和capture产额，条件比值的误差含

\[
\operatorname{Var}\log(\eta_{1275}/\eta_H)=
\operatorname{Var}\log\eta_{1275}+\operatorname{Var}\log\eta_H
-2\operatorname{Cov}(\log\eta_{1275},\log\eta_H).
\]

共同scale与跨能量形状误差应分开。本文原完整Cov未得，不能仅从6%和2.6%打印预算回推作者是否已处理某共同项。

## Competing Interpretations and Limitations

绝对方法控制、靶退化和效率验证都与主实验共享部分装置或reference；同一2010/2011论文与评价转载不是新增采集。四有限强度的峰计数、模板Cov、partial间协方差、tail相关性与beam/NT/eff全合同仍缺。源认为旧实验局部target退化可能解释差异，是作者解释，不是本session独立测得的历史误差。

S11-13的placement争议、弱模板停止比、P4残余和NT活动度角色反证了仅以一个强度值、一个角度或完整积分口号宣称核结构输入无条件确定。K16上限和本直接强度也不能在固定旧J/Bp后随意拼新τ置信区间。

## Knowledge Impact and Learning Decision

`supports`将直接capture强度作为DSAM总宽换算的必要companion；`revises`把“避免绝对stopping”扩成所有结果零停止依赖、把表中partial/branches/limits视相互独立；`limits`中心代数、共享校准和同源转载对新实验CI的保证。新claims均needs_review，没有human-reviewed，没有新τ、Jπ、Bp或率测量。只为Day17原窗口内Day18无学分预习。

## Extracted Pages

[[nndc-2021-mg23-lifetime-strength-reference]]、[[jenkins-2004-23mg-fractional-doppler-rate]]、[[kirsebom-2016-23mg-dsam-lifetimes]]、[[lifetime-strength-audit-165tm-136nd]]、[[doppler-shift-attenuation-method]]、[[linear-polarization-asymmetry]]。

## Letter版本补充：frame定义需要实际程序桥

[[sallaska-2010-na22-letter-version-contract]] S10-1–10实际原读v2/定向比较v1，Eq1明确lambdaLab²而本文Eq4称CM。声明NR关系lambdaCM²=r²lambdaLab²，质量数控制r²≈1.093；只是打印定义/条件推导，未得producer或正式erratum，不按此重标实验。旧S11-1保留当时未读短报的范围，正式erratum仍未读。
