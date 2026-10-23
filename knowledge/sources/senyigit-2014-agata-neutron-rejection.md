---
type: source
title: "Şenyiğit 2014：AGATA 中子背景、反冲附加能量与 cut 边界"
aliases: [Senyi AGATA neutron rejection, Senyigit 2013 preprint neutron response]
created: 2026-10-13
updated: 2026-10-13
status: ai-draft
review_status: unreviewed
source_type: journal-method-experiment-with-public-preprint
reading_depth: deep-read
title_original: "Identification and rejection of scattered neutrons in AGATA"
authors: [M. Senyigit, A. Atac, S. Akkoyun, et al.]
journal: Nuclear Instruments and Methods in Physics Research A
year: 2014
volume: 735
pages: 267-276
doi: 10.1016/j.nima.2013.09.035
arxiv: 1306.2788v1
language: en
canonical_source: "https://doi.org/10.1016/j.nima.2013.09.035"
citation_key:
raw_file: "raw/papers/gpt/day13/senyigit-2014-agata-neutrons.pdf"
raw_sha256: "cb796a846c155927d1f559a87a4772cd703904c2d6bdd81bcdde61a7dd06986c"
raw_storage_status: reserved-unpopulated-public-preprint-only
raw_archive_verified_at: 2026-10-23
external_pdf_url: "https://arxiv.org/pdf/1306.2788v1"
nuclei: [70ge, 72ge, 74ge, 76ge, 27al]
methods: [gamma-ray-tracking, neutron-gamma-discrimination, time-of-flight, doppler-correction]
tags: [agata, neutron-background, recoil-energy, gate-logic, spectral-width]
---

# 中子诱发背景与非目标核宽线

## Bibliographic Record

M.Şenyiğit et al., *NIM A*735,267–276(2014)，DOI10.1016/j.nima.2013.09.035。Crossref核验journalyear2014，2013为arXiv/DOIonline年。实际读15页arXiv1306.2788v1，preprint封面编译日期2018-10-30不作为出版年；所有locator为该preprint页。Publisher finalPDF未作逐字比对，以下文本/表冲突仅定位到该preprint。

raw保留位置未填充，raw_file未创建；真实字节仅存`tmp/day13/reopened/senyigit-2013-agata-neutrons.pdf`（文件名按preprintyear），SHA为frontmatter所列。保留公开versionedURL和RAW_MISSING，不声称已raw归档。

## Scope and Reading Depth

全文主线15页：neutron-backgroundmotivation、252Cf/60Co/TOF setup、ADL/grid-search/mgt processing、detectorrecoils/lineorigin、TOF与trackingcuts、Tables1–4的efficiency/background、simulationcomparison与conclusion。视觉核验p5/p11/p13tables及p6/p7spectra；p14结论谓词与正文p10/p13逐字比较。

未覆盖：原events/traces、productionmgt版本/完整predicate实现、normalization/peakfitjointcovariance、publisherfinal文字、所有Ge/nuclearlevel评价原文。不能凭本篇比对重写生产cuts或给独立τ/B测量。

## Paper Question and Scientific Motivation

中子弹性/非弹性散射在HPGe中产生recoil与γ背景，混入trackingclusters时可降低谱纯度、形成false-energyfeatures。作者以独立TOF标签优化trackingneutronrejection，同时控制trueγFEP损失（pp.1–3）。

## Method and Design Logic

252Cf source与4ATC(12crystals)距约50cm、16HELENA BaF2距source14cm作timeref；5cmPbshield改变n/γrelativeflux。60Co calibration以3ATC/50cm采集，检验无neutronevents时的FEP损失。ADLbasis2010-07-28、adaptivegrid-search、mgtlim=0.02定义standardtracking；额外Eint1/Eint2/Δθ/FM cuts与TOF门比较（pp.3–10）。

## Key Evidence and Reasoning Chain

TOF/data/controlsource → detectorrecoil/Geγpeak及high-energybump → standardtracking与extraNRcut/TOFgate → 分母明确的背景/trueγretention → simulationthreshold比较。此TOF标签检验incidentparticle类别，不自动证明某targetisotope身份；其它材料发出的真γ仍可通过γTOF门。

## Summary

约40keV的高能侧凸起可来自Ge-recoilvisibleenergy加到Geγline；27Al2211-keVpeak报告DopplerFWHM15keV，作者引用母态meanlife26.6fs。extraNR处理进一步压低70Ge1040peak/bump，但损失约18.5%的standardtracked1332-keVCo计数。原表与正文conclusion的gate语义、部分Co列标签不完全一致，保持执行版边界。

## Experimental or Theoretical Setup

- 252Cf5.3×10⁶triggered events，约3日；60Co约10⁶events；仅此setup与cuts的性能。
- coreCFDthreshold10–20keV；hardware读取全部36segment，offline数字CFD约10keV；较低threshold的信息能改变neutronrejection。
- Fission/Geant4/neutroninteraction输入与actualdata分开；simulated5/10keVthreshold不是实验两份独立测量。
- TOF为HPGecoretime与平均BaF2time之差；finitepath/timewalk/response限制距离迁移。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SY14-1 | 50cm252Cf+4ATC、14cmHELENA与独立60Co控制用于TOF标签和tracking/FEP检验；mgtlim.02定义当前standardtracking。 | experimental-fact | direct | preprint PDF pp.2–5, Sec.2; Fig.1, Table1 | true |
| SY14-2 | Ge(n,n′γ)峰高能侧约40keVbumps由Ge-recoil能量与γenergy相加解释；2MeVneutronrecoil约100keV物理最大值，pulse-height-defect后的visibleenergy scale约35keV为引用背景。 | author-interpretation | direct | preprint PDF pp.4–6, Secs.2.4–2.6; Fig.2 | true |
| SY14-3 | source报告27Al2211-keVpeak为Dopplerbroadened、FWHM15keV，引用2212-keVlevelmeanlife26.6fs；若以通用Γ=ℏ/τ估自然width则远小于此keVFWHM，τ不是本篇独立测量。 | author-interpretation | direct | preprint PDF p.5, Sec.2.6; Ref29 | true |
| SY14-4 | 在约50cmsetup，100–1200keVEint的γtimepeakFWHM约9.8→7.7ns；γTOF门抑制Ge峰/bumps，但保留部分Fe/Al/Ba/Pb或annihilation真γ。source指出23.5cm或更短距离的TOF分离受当前timing限制。 | experimental-fact | direct | preprint PDF pp.6–7, Sec.3.1; Figs.3–5 | true |
| SY14-5 | Table4中1040peak、peak+bump的core→standard→NRcentralreductions为57%再28%→69%、52%再42%→72%；Co1332为9.0%再18.5%→25.8%。这些percent分别使用不同分母，表误差为statistical。 | experimental-fact | direct | preprint PDF p.13, Table4; p.11, Table2 | true |
| SY14-6 | body/Table2/Table4给acceptance样式OR：Eint1>30 OR Eint2>30 OR signedΔθ<40° OR FM<.01；p14conclusion改写为反向inequalities的OR。若将后者理解为rejectrule，其complement是ANDgood，与bodyORgood不同。没有executedpredicate/publisherversion不能选作者实际语义。 | experimental-criterion | direct | preprint PDF pp.10–11, Table2; p.13, Table4; p.14, Conclusions | true |
| SY14-7 | Sec3.2.1文字称Co1173/1332standardloss约9%/12%，而Table4是11.7(6)%/9.0(6)%；结论也称1332约9%。保留text/tablelabel差异，本文工作引用表值时明确locator，不静默统一。 | experimental-fact | direct | preprint PDF p.8, Sec.3.2.1; p.13, Table4; p.14 | true |
| SY14-8 | Table1的trackingefficiency分母为core-spectrumFEPcounts，宽松lim时可>100%；不能把此count-reconstructionratio当所有发射γ的概率或absolutephotopeakefficiency。 | experimental-criterion | direct | preprint PDF pp.4–5, Sec.2.2, Table1 | true |
| SY14-9 | Table2对Co1332列Eint1>45单项loss3.9(6)%、四条件OR(gt30)loss18.5(6)%。若解释为同一fixed-cluster/energy/counting基础上的acceptancepost-filter，则OR包含Eint1>30并包含Eint1>45，联合loss应≤3.9%，与表中心值不相容。此为有条件任务set-inclusion推断，不证明actualmgt实现有bug；retracking/reassembly/peakfit/stagedefinition仍可改变集合前提。 | our-inference | indirect | preprint PDF p.11, Table2; task-derived monotonicity under stated fixed-post-filter assumptions | true |

## Nuclear Structure Information

这里Ge/Al/Fe/Ba/Pb line主要是detector/environmentbackground标签，不能加入targetnucleus的levelscheme。τ/assignments部分取自externallevel-data资料；本篇贡献为apparatusresponse/selection，而非新target核的B矩阵。

## Authors' Interpretation

tracking本身排除部分recoil-likehits；TOF、Eint/Δθ/FM可进一步分离neutron-inducedfeatures，并与FEPretention折衷。expectedfuturePSAimprovement是作者预期，不写成当前2026性能。

## Model Results

Geant4对fourATC/50cm、5与10keVthreshold结果在Table3；与实际Table2共享模型/geometry假设，不同threshold不计两份独立实验。source未给本文可replay的production事件/covariance。

## Competing Interpretations and Limitations

- broadline/high-sidebump可能是额外recoildeposit、localneutronγ或其它materialγ，不仅是targetβspread或未分辨transition。
- γTOFtag并非targetidentity；neutron在附近材料诱发的真γ可快速到达Ge而保留。
- OR/AND、signedΔθ/absoluteangle及严格inequality边界都影响cut；不能把p14谓词自动修成正文，或者把Δθ<40°改成|Δθ|<40°。
- 57%+28%不能相加为85%；不同分母应乘survivalfractions。source表统计误差不提供jointcovariance。
- calibration/acquisitiongeometry与standardlim定义specific；AK12overview与本source可共享仪器/算法脉络，不能将quotedcalibration数重复当独立同一性能验证。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SY14-AR1 | denominatoraudit | 1−(1−rA)(1−rB)重算Table4centralreductions与roundedvalues相容；未独立测量或传播缺失jointerrors。 | SY14-5; [[doppler-correction]] | unreviewed |
| SY14-AR2 | predicatecounterexample | 4goodbooleans的16种assignment中，ORgood与rejectORbad所隐含ANDgood在14种mixedcase不同；不是14/16datafraction，不决定exec-code。 | SY14-6; [[gamma-gamma-coincidence]] | unreviewed |
| SY14-AR3 | natural-widthscale | τ26.6fs给parentΓ约2.47×10⁻5keV，不能解释reported15keVDopplerwidth；其寿命为source引用input，不虚构独立evaluation核验。 | SY14-3; [[doppler-correction]] | unreviewed |
| SY14-AR4 | cutmonotonicity | literalacceptanceORpost-filter不能同时解释Table2的single/combinedcontrol-loss，需恢复actualcutstage/restructuring与countdefinition，而非从summary猜predicate。 | SY14-9; [[doppler-correction]] | unreviewed |

## Knowledge Impact and Learning Decision

`revises`宽峰诊断加入detectororigin/recoildeposit；`limits`γTOFtag、cleanedP/T和cutsummary的充分性。owningmethods为 [[doppler-correction]]、[[tracking-array]]、[[gamma-gamma-coincidence]]；sourceinternalpredicate保留needs_review和实际code缺口，不向用户发泛化审核待办。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-correction]] | falsewidth/localemitter、naturalΓscale与selectionaudit。 |
| methodological-bridge | [[tracking-array]] | TOFlabel、recoilhits、mgtgate和FEP/P-Ttradeoff。 |
| methodological-bridge | [[gamma-gamma-coincidence]] | predicate/reference-denominator和backgroundlineidentity。 |
| foundational-background | [[akkoyun-2012-agata-instrument-response]] | instrument/PSAresponse被原文引用，重复引用不新增独立实验。 |
| competing-interpretation | [[crespi-2013-agata-high-energy-doppler-response]] | distinctsourceacquisitions中neutronsumfeatures/algorithmselection的比较，threshold和numbers不移植。 |

## Human Review Triage

P0：无未隔离身份/权限风险；productioncut未知以SY14-6明示，不执行或推荐未经核实的实际NRpredicate。P1：SY14-3的externalτ与width、SY14-5/7分母/textlabels、SY14-6OR/AND语义和publisherversion、SY14-8非概率efficiency。Self-audit不升级human-reviewed。

## Extracted Pages

preprintpp.2–5setup/controls/lineorigins，pp.6–10TOF/tracking，p11Table2–3，p13Table4，p14conclusionlogic；核心tables/figures视觉核验。
