---
type: source
title: "Ziliani 2019：AGATA 的 timestamp、能量和 lifetime-control 检查"
aliases: [AGATA PARIS VAMOS spectroscopy calibration 2019, Ziliani energy time controls]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: conference-contribution-preliminary-experiment-calibration
reading_depth: deep-read
title_original: "Spectroscopy of Neutron-rich C, O, N and F Isotopes with the AGATA+PARIS+VAMOS Setup at GANIL"
authors: [S. Ziliani, M. Ciemała, F. Crespi, S. Leoni, B. Fornal, A. Maj]
author_list_scope: first-six-of-publisher-copy
journal: Acta Physica Polonica B
year: 2019
volume: 50
issue: 3
pages: 625-631
doi: 10.5506/APhysPolB.50.625
data_version: publishercopy-received7Jan2019-reportingJuly2017experiment
canonical_source: "https://doi.org/10.5506/APhysPolB.50.625"
citation_key:
raw_file: "raw/papers/gpt/day13/ziliani-2019-agata-calibration.pdf"
raw_sha256: "261b65b42c50350279b0e94f4c5e119342a9f78253be281315ec93ca6c12745a"
raw_storage_status: reserved-unpopulated-public-publisher-copy-only
external_pdf_url: "https://www.actaphys.uj.edu.pl/fulltext?series=Reg&vol=50&page=625"
nuclei: [18o, 19o, 20o, 24mg, 208pb]
methods: [doppler-correction, time-alignment, energy-calibration, gamma-ray-tracking]
tags: [agata, paris, vamos, calibration, shared-data, core-segment, preliminary]
---

# Timestamp 与 energy 标定怎样进入 Doppler 证据

## Bibliographic Record

S.Ziliani等，ActaPhysPolB50(3),625–631(2019)，DOI10.5506/APhysPolB.50.625；官方PDF7页和Crossref题名/作者前缀/年/卷身份核验。Received7Jan2019，2018conference报告；实际experiment11–23July2017，不能把outlook当2026任务状态。

raw保持不变：raw_file未填充，publishercopy存 `tmp/day13/reopened/ziliani-2019-agata-calibration.pdf`，SHA如上。它与[[ciemala-2019-20o-dsam-analysis-status]]是同18O+Ta dataset的关联报告（本篇Ref6/对方Ref8），不是独立重复。

## Scope and Reading Depth

- 7页全主线：C/O NN/NNN motivation→setup/data→fullreplay/timealign→energyanchors/coresegments→18Ocontrol→futurelineshapeanalysis。
- 深核验pp.3–6/journal627–630，Fig2/TableI/Fig4；p4、p6视觉核验。
- 未覆盖：2018master-thesis原文、replayconfiguration/coefficients、RF/velocitycode与sourceexactgates、percrystalΣ、intrinsicwidth/tabledefinition、laterfinalτ。无新实验重跑。

## Paper Question and Scientific Motivation

说明实际AGATA数据准备与knownlifetime transitions的角依赖，支持后续DSAM分析。校准改进是measurement/method证据；本文仍为preliminaryanalysis，不宣称20O/16C新lifetime/force裁决。

## Method and Design Logic

Fullreplay→crystal timestamp对齐→tightpromptcoincidence→coreenergy多anchor regression→degradedcore的segment recovery→knownshort/long18Oline centroid/shape对照。Time/energy、velocityhistory与detectorresponse是不同检查，同事件/配置/parameters仍共享。

## Key Evidence and Reasoning Chain

Rawnearline vsfinecalibration→sourceTable/figure改进→short/long近能量control不同角趋势→futurelifetimecomparison需要simulations。不同mass/time/energyplots能提供互补约束，不能等同所有stage/Σ已独立验证。

## Summary

GGPcrystals存在timestampoffset，replay对齐后可tightgate使peak/background提高>2，photopeakcounts损失<4%。Eu/AmBe之外的Pb/Mg环境线帮助2–3MeVenergyanchors；badcore14A/11C可借calibratedsegmentsrecover。1938.2短τ与1981.93长τ的18Ocontrol说明physicalhistory可留下centroidshift，不能强行把每条shortline归零做calibration。

## Experimental or Theoretical Setup

July2017，18O126MeV+Ta4μm（本篇约6mg/cm²，对CO19写6.64mg/cm²，保留两个printedfields）、31AGATA、PARIS90°、VAMOS45°。Sameexperiment互引明确，但完整targetdefinition/file/hash本任务未得。环境Mg/Pb与staticcal sources不是reactionemitter。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZL19-1 | 实验日期11–23July2017、18O126MeV/Ta4μm、31AGATA/PARIS/VAMOS；本报告与CO19共同原experiment而非新增独立sample。 | experimental-fact | direct | PDF p.2/journal626, Sec.2; p.7Ref6 | true |
| ZL19-2 | Fullreplay添加time/energycal，GGP新electronics部分crystal TS未对齐；replayconfig参数修正后tightpromptgate使P/Bfactor>2、photopeakcounts损失<4%。 | experimental-fact | direct | PDF pp.3–4/journal627–628, Fig2/text | true |
| ZL19-3 | Fig2轴是VAMOS/AGATATimestamp差，具体tick/ns/actualgate参数未全文给出，不从图或100MHz常识自动换成标准timeσ。 | experimental-criterion | direct | PDF p.4/journal628, Fig2/caption | true |
| ZL19-4 | Coreenergyanchors包括Eu<1.5MeV、AmBe:Fe>5MeV及2–3MeV的Pb/Mg环境线；Gaussianpeak+linearbackground后线性regression，不以一个已校正beamline代静止energyanchors。 | experimental-criterion | direct | PDF pp.3–4/journal627–628, energycalparagraph | true |
| ZL19-5 | Crystals14A/11C core退化，以36segment自动energycalibration恢复；energyrecover不由本篇单独验证PSAbasis/firstpointresolution已恢复。 | experimental-fact | direct | PDF pp.4–5/journal628–629, Fig3 | true |
| ZL19-6 | TableI的resolution%为121.8:2.96→1.73；1112.1:.30→.26；2754:.22→.16。Source未explicit说明这表σ/FWHM，不把百分数自动入GaussianΣ。 | experimental-fact | direct | PDF p.4/journal628, TableI | true |
| ZL19-7 | Fig3的2754.007(11)keV明确是24Mg环境line，在Eu-source spectrum中出现；TableI caption泛称Eu transitions，不能把2754当Eu本体branch或已知per-Eudecayintensity。 | synthesis | direct | PDF pp.3–5/journal627–629, TableI/Fig3caption | true |
| ZL19-8 | 18Ocentroidcontrol使用1938.2(2)keV/printedτ26.5(29)fs及1981.93(9)keV/τ2.80(7)ps；source测的是anglebarycentres，不报告新测这些referenceτ。 | experimental-criterion | direct | PDF pp.5–6/journal629–630, Fig4/text | true |
| ZL19-9 | 1938.2shortreference出现角依赖shift/shape，1981.9longreference不同；两相近能量line支持history敏感性，但sameevents/velocitycal/response仍共享，不构成newindependentclock。 | experimental-fact | direct | PDF pp.5–6/journal629–630, Fig4/inset | true |
| ZL19-10 | Source称将用正在developing的reaction simulationextractC/Oτ；本篇没有20O2+2 finalχ²minimum/τ/B。 | author-interpretation | direct | PDF p.6/journal630, Conclusions | true |

## Nuclear Structure Information

18Oreferenceenergies/lifetimes、19Ospectrum为calibration/historyexamples；NN/NNN motivation引用理论。此页不补新levelplacement、absolutetransitionstrength或N3force证据。

## Authors' Interpretation

精准time/energy准备使γcentroid/shape对shortτ敏感，后续reactionmodel可利用这种信息。它不说每条beamgamma都应被强制校正到zeroresidual，也不在这里完成forcecomparison。

## Model Results

背景regression/calibration是数据准备；NN/NNN为引用theory，futuretransport/line-shapecomparison见CO19。No new model run or experimental refit by this task.

## Competing Interpretations and Limitations

- Resolution、centroidaccuracy、PSAposition与velocitycalibration是不同指标；TableI不补每angle/crystalΣ。
- Photopeakcountloss是tightgate计数比较，不是absoluteγefficiency；P/B不等P/T。
- 环境line可以做energyanchor，不自动提供source-activity/intensitynormalization，origin标签需明确。
- Knownτcontrol可约束history/response，但不能从referencecentroidshift单独判某calibration正确或模型全闭合。
- SameJuly2017 CO19/ZL19共享data、calibration、simulation，重复引用不增加独立experiment。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| ZL19-AR1 | layer separation | 新energy/time检查支持analysis准备，不能代原RF/energy/PIDjointΣ或emission/exitfielddefinition。 | ZL19-2/4/6; CO19-3/6/12 | unreviewed |
| ZL19-AR2 | control mapping | CO19“known18O~27fs”的直接Ref8对应1938.2line，而1981.93是2.80ps；不按同isotope/相近energy合并history。 | ZL19-8/9 | unreviewed |
| ZL19-AR3 | calibration origin | 2754作为Mg背景energyreference与Eu知名branch/intensity不同，做ratecal必须另有activity/branchnormalization。 | ZL19-7 | unreviewed |

## Knowledge Impact and Learning Decision

`supports` replay/timing/多energyanchors与knownhistorycontrols，`limits`把source-spectrum所有peak当cal-sourcebranch、把resolution改善当完整独立validation或finalτ。写回 [[doppler-correction]] / [[tracking-array]] 的packet契约。

## Related Knowledge and Project Relations

同data的后续结果 [[ciemala-2020-c16-o20-lifetimes]] CI20-1/5/6/7，不改变本2019report的preliminary状态。[[zanon-2023-o20-high-precision]] 是另一采集；calibrationcontrols与laterfinalτ分开。


| Relation type | Target | Specific relation |
|---|---|---|
| same-lineage | [[ciemala-2019-20o-dsam-analysis-status]] | 同July2017dataset、mutualreferences/calibration。 |
| methodological-bridge | [[doppler-correction]] | 1938.2/1981.93historycontrol与energy/RF区分。 |
| methodological-bridge | [[tracking-array]] | GGPtimealign、coresegmentenergy与PSA/response范围。 |
| methodological-bridge | [[doppler-velocity-validation-contract]] | Time/energyanchors不补allcovariance或absoluteB。 |

## Human Review Triage

P0：metadata/publiccopy/raw未归档边界隔离，未报newτ。P1：ZL19-2gate分母、ZL19-6width定义、ZL19-7origin、ZL19-8/9refτ/lineage、ZL19-10preliminarystatus。No human-reviewedpromotion。

## Extracted Pages

PDF1–7/journal625–631全文；core3–6、TableI/Fig4视觉核验。原2018master-thesis、config/Σ和后续finalfit未取得。
