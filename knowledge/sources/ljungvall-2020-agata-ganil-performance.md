---
type: source
title: "Ljungvall 2020：GANIL 的 AGATA Doppler、PSA 与事件混合响应"
aliases: [AGATA GANIL performance 2020, Ljungvall GANIL efficiency position]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: journal-instrument-method-experiment
reading_depth: deep-read
title_original: "Performance of the Advanced GAmma Tracking Array at GANIL"
authors: [J. Ljungvall, R. M. Pérez-Vidal, A. Lopez-Martens, C. Michelagnoli, E. Clément, J. Dudouet, A. Gadea, H. Hess, A. Korichi, M. Labiche, N. Lalović, H. J. Li, F. Recchia]
journal: Nuclear Instruments and Methods in Physics Research Section A
year: 2020
volume: 955
pages: 163297
doi: 10.1016/j.nima.2019.163297
arxiv: 2011.08003v1
data_version: "public PDF requested at arXiv2011.08003v1; header2020 and printed submission footer2022 both preserved"
language: en
canonical_source: "https://arxiv.org/abs/2011.08003v1"
citation_key:
raw_file: "raw/papers/gpt/learning-daily/20261013-DAY13-doppler-correction-recoil-velocity/ljungvall-2020-ganil-performance.pdf"
raw_sha256: "07cb8ea5bf3fa310ad00802a08ef9e07702e7a837d27ba15ae567a3a6adfe3c9"
raw_storage_status: reserved-unpopulated-public-preprint-only
raw_archive_verified_at: 2026-10-23
external_pdf_url: "https://arxiv.org/pdf/2011.08003v1"
nuclei: [98zr, 92mo, 152sm, 152gd]
methods: [doppler-correction, gamma-ray-tracking, pulse-shape-analysis, angular-correlation, event-mixing]
models: [geant4]
tags: [ganil, agata, vamos, detector-response, normalization, shared-data, version-boundary]
---

# GANIL 的 Doppler 位置估计与联合接受率

## Bibliographic Record

J.Ljungvall等，NIMA955,163297(2020)，DOI10.1016/j.nima.2019.163297；Crossref题名/作者/年/卷/页核验。实际读公开URL `arxiv.org/pdf/2011.08003v1` 获取的33页PDF。首页arXiv标注12Nov2020，但同页submission footer印23September2022；以获取copy的URL/hash及两个打印日期标识，不假定它字节等同2020publisher article或已解决全部version history。

raw保持不变：raw_file为未填充保留位置，获取字节仅在 `tmp/day13/reopened/ljungvall-2020-ganil-performance.pdf`，SHA如上。文中performance snapshot为mid2016，不把旧rates/code/foreseen schedule写成2026状态。

## Scope and Reading Depth

- 33页主线：setup/raw processing→crystal resolution/efficiency→OFT及source/in-beam response→98ZrDoppler position estimate→source γγ event mixing→conclusion/Appendix detector table/relevant references。
- 核心原图/表：Table2p12、Figs.9–13pp.13–17、Fig.15/Eqs.(1)–(4)pp.18–20、Figs.16–18pp.21–22；关键页图像核验。
- 未覆盖：原实验events、PSA basis/code/calibration versions、simulation input/seed、所有width covariance、source活动度和dead-time的完整测量packet、underlying Söderström2011原文。没有运行原OFT或实验L4重拟合。

## Paper Question and Scientific Motivation

给2016GANIL AGATA30active-detector配置的source与in-beam效率、P/T、PSA位置响应及angular-correlation normalization一个可用实验基准，同时诊断实际material/PSA与ideal simulation之间的差异。

## Method and Design Logic

Crystal calibration/cross-talk/charge-trapping corrections→PSA local points→event merger加入complementary data→OFT global tracking→source efficiencies/单hit/P-T→独立VAMOS vector的98Zrpeak-width interpolation→混合interaction points再tracking构造联合接受率。每个阶段的identity、event selection和shared normalization保留。

## Key Evidence and Reasoning Chain

source与in-beam响应比较→rate/material/PSA的限制→实际Doppler宽度对simulated position response的依赖→γγ pair selection无法简单factorize→known source correlation的验证。更高P/T、全谱窄化和同source归一化不是结构结论。

## Summary

论文给出独立particle vector支持下的Doppler position估计，以及直接实验的tracking前/后event mixing比较。5.1mm average position FWHM属于能量依赖响应、指定六detectors及simulation interpolation，不能当作所有IP的σ。单hit拒绝、rate和γγ close-angle losses说明效率必须匹配实际event条件。

## Experimental or Theoretical Setup

mid2016共有30active crystals，02C不稳定而从efficiency排除，29参与效率；nominalfront23.5cm、compactfront13.5cm。Co/Eu activity来自Table1；source材料/trigger/raw100sample traces、Narval与post-PSA replay说明pp.3–6。Doppler例为238U+10μm9Be、VAMOS28°、选六个相对recoil≈112°的detectors；另92Mo+92Mo beam效率测试仅23crystals、约45kHz/channel（pp.17–20）。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LG20-1 | 同一local preprocessing/PSA→postPSA→event builder/merger→OFT代码可在线或replay；PSA后traces被移除，若仅存postPSA points，只能重跑后续阶段；完整traces记录有rate/dead-time条件。 | experimental-criterion | direct | PDF pp.5–6, Sec.3/Fig.2 | true |
| LG20-2 | OFT Table2 σθ单位cm；simulation2.4mm与actual6–8mm optimum描述FOM position-error调参。增大此量可增加高能效率，却损失低能/高fold single hits并改变pair acceptance。 | experimental-criterion | direct | PDF pp.11–13, Table2 and OFT parameter discussion | true |
| LG20-3 | Core source efficiency1332keV nominal2.95(6)%/compact5.5(1)%；tracked1.4MeV3.67(1)%、add-back factor1.285(4)。singles有activity/dead-time依赖，γγ方法须angular correlation/close-pair losses修正。 | experimental-fact | direct | PDF pp.9,13–14, Figs.7–10 | true |
| LG20-4 | Co test以第30detector的1332.5±5keV core作外trigger，对其余29detectors近似Mγ1；P/T36.4(4)%，排single hits后52.4(6)%而FEP效率损失17%。 | experimental-fact | direct | PDF pp.14–15, Sec.5.2/Figs.11–12 | true |
| LG20-5 | 四套material/dead-layer simulations P/T49/48/43/41%，实测约36%；VAMOS steel、walls/chamber与dead layers会改变backscatter/profile，但这些改动未完全解释差异。 | model-result | direct | PDF pp.16–17, Fig.13 | true |
| LG20-6 | 92Mo test在23crystals、约45kHz、2.5μs shaping下，1510keV tracked efficiency1.5(1)%对约2.5%expectation；作者讨论pileup/close-pair losses及未解释的约15%loss，不把40%总差完全归于某项。 | author-interpretation | direct | PDF pp.17–18, Sec.5.3/Fig.14 | true |
| LG20-7 | 98Zrposition法以VAMOS recoil方向近似精确、relative speed error∆β/β=.0045（mass resolution派生），作者将velocity contribution作为.13%FWHM并在simulated widths上quadrature添加；这些是指定分析inputs，不是通用TOFσ。 | experimental-criterion | direct | PDF pp.18–20, Sec.6/Eqs.(1)–(3) | true |
| LG20-8 | Geant4包含target energy loss/straggling、VAMOS acceptance，truth vector假设∆v=0，intrinsic FWHM2.6keV@1332；position law∆ri=1.9+4.4√(100keV/Ei)mm FWHM按scale变化，再Gaussian-fit widths与quadratic interpolation对接实验。 | model-result | direct | PDF pp.19–20, Eq.(4)/Fig.15 | true |
| LG20-9 | 六detectors由position-width法给3.7–6.1mm FWHM、weightedaverage5.1mm，平均estimated error1mm；作者提醒2.4mm范围在六个σ1mm Gaussian draws下约50%可见，不证明detectors确实不等性能。 | author-interpretation | direct | PDF p.20, Fig.15 and following paragraph | true |
| LG20-10 | Source γγ correlation的normalizer将两次uncorrelated events的interaction points先concatenate、后tracking，保留pair closeness/cluster损失；Fig.18显示tracking后才混合不能覆盖完整angle response。 | experimental-fact | direct | PDF pp.20–23, Sec.7/Figs.16–18 | true |
| LG20-11 | 244.7/121.8 cascade的拟合a22=.13±.02、a44=−.02±.03，对theory .102/.0091；1408/121.8为.25±.02/−.01±.03，对theory .25/0。未提供joint fit/input covariance，不能把四数当独立全局χ²。 | experimental-fact | direct | PDF pp.21–22, Eq.(5)/Fig.17 | true |
| LG20-12 | 作者强调source mixing方法适用于高peak/background、不同decays无correlation；in-beam lowpeak/background及aligned nuclei的cross-event correlations使直接迁移更困难。 | author-interpretation | direct | PDF p.23, end of Sec.7 | true |
| LG20-13 | Bodyp8打印core before correction2.93keV、sum segments5.22，after2.57/3.08；conclusionp23的core before打印3.08keV。两处before值保留，不静默选择或反改raw。 | synthesis | direct | PDF pp.8,23 | true |
| LG20-14 | Source Eq.(4)标FWHM in one dimension，Fig15upperaxis为实际用于Doppler的平均IP response；名义Gaussianσ、energy-dependent IP FWHM和拟合scale是不同输入。 | experimental-criterion | direct | PDF pp.18,20, Fig.15 caption/Eq.(4) | true |
| LG20-15 | 首页公开copy同时印arXiv12Nov2020和submission23September2022；science snapshotmid2016、Crossrefpubyear2020、copy/date/hash字段分别记录，publisher-version equivalence未核定。 | synthesis | direct | PDF p.1; Crossref DOI identity; PDF p.3 | true |

## Nuclear Structure Information

98Zr1223-keV、92Mo1510-keV与152Sm/152Gd source cascades用于response/normalization。本文不据position改善测新的collective mode、absoluteB或level scheme；source/spin inputs保持原文语境。

## Authors' Interpretation

PSA/response改善需考虑physical/IP merging、material scatter和detector maintenance；source效率/位置分辨率可指导GANIL数据，但in-beam rates/alignments要另配response。论文保留未解释效率损失和detector之间差别的统计限制。

## Model Results

模拟未显式重建真实particle-vector误差，而在最终width上添加项；energy-dependent smear、target与acceptance为其特定packet。性能比较共享simulation/template和source，不能当多次independent replication。

## Competing Interpretations and Limitations

- measured particle vector提供独立信息，但.0045、.13%及directions-negligible是此分析假设，covariance/σ–FWHM不能泛化。
- source activity/dead-time、γγ branch/correlation和close-pair损失影响不同efficiency estimator，不能把两种结果当完全独立error samples。
- 完整traces与postPSA points的可重放范围不同；code list或最终谱不能替raw/basis/history。
- publishedreview [[crespi-2023-agata-tracking-performance]] C23-7/12依赖本篇source数据；98Zr与[[vandebrouck-2016-vamos-dual-position-mwpc]]涉及同设施/可能campaign关联，无runmanifest不默认实验独立。
- LG20-13/15打印/version边界保留，self-audit未宣布erratum或稳定publisher数字。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| LG20-AR1 | joint acceptance | tracking前混raw IP和tracking后混独立γ不同；后者只近似product of single efficiencies，不能捕获joint clustering。 | LG20-10; [[tracking-array]] | unreviewed |
| LG20-AR2 | covariance/readiness | 持有width/energy-dependent response模板和particle vector假设支持位置估计；真实L4仍需events/code/basis/selection/covariance，5.1不是universalσ。 | LG20-7/8/9/14; [[doppler-correction]] | unreviewed |
| LG20-AR3 | source to in-beam | common beam alignment可使cross-event pair-angle分布非isotropic，source normalizer不能无条件移植；详见本任务声明的harmonic toy。 | LG20-12; [[tracking-array]] | unreviewed |

## Knowledge Impact and Learning Decision

`supports`particle vector结合matched simulation的position估计与tracking前mixing；`limits`source效率、nominal5mm、same-source独立性或P/T改善的泛化。方法同步 [[doppler-correction]]、[[tracking-array]] 与 [[gamma-gamma-coincidence]]。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-correction]] | 指定source/velocity/response的position估计。 |
| methodological-bridge | [[tracking-array]] | 联合接受率、raw/postPSA replay和FOM units。 |
| methodological-bridge | [[gamma-gamma-coincidence]] | mixing必须保留pair-selection与in-beam alignment边界。 |
| same-lineage | [[crespi-2023-agata-tracking-performance]] | 综述重复本篇efficiency/P-T实验，非新复测。 |
| methodological-bridge | [[vandebrouck-2016-vamos-dual-position-mwpc]] | 同设施vector/98Zr主题；无runmanifest不主张独立dataset。 |

## Human Review Triage

P0：public获取身份/未归档raw槽位/version字段明示。P1：LG20-7/14速度/width units与covariance、LG20-9 detectorspread、LG20-10/12jointmixing、LG20-13/15打印差异。无human-review状态升级。

## Extracted Pages

PDF1–24正文/Appendix，25–33参考按相关项回链；核心12–23。实际events和原2011模板论文仍未取得。
