---
type: source
title: "Ciemała 2019：20O DSAM 的离子时标、未知γ能量与分析进展"
aliases: [20O AGATA PARIS VAMOS lifetimes 2019, Ciemala DSAM analysis status]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: conference-contribution-preliminary-experiment-method
reading_depth: deep-read
result_status: analysis-in-progress-no-final-2plus2-lifetime-fit
title_original: "Determination of Lifetimes of Excited States in Neutron-rich 20O Isotope from Experiment with the AGATA+PARIS+VAMOS Setup"
authors: [M. Ciemała, S. Ziliani, F. Crespi, S. Leoni, B. Fornal, A. Maj]
author_list_scope: first-six-of-publisher-copy
journal: Acta Physica Polonica B
year: 2019
volume: 50
issue: 3
pages: 615-624
doi: 10.5506/APhysPolB.50.615
data_version: public-publisher-copy-received23Jan2019
canonical_source: "https://doi.org/10.5506/APhysPolB.50.615"
citation_key:
raw_file: "raw/papers/gpt/day13/20o-2019-acta-dsam.pdf"
raw_sha256: "2021d2e0cac8641d3816ec47c36ac41e2bff91504b857f0423ac5b805f94224b"
raw_storage_status: reserved-unpopulated-public-publisher-copy-only
external_pdf_url: "https://www.actaphys.uj.edu.pl/fulltext?series=Reg&vol=50&page=615"
nuclei: [20o, 18o, 19o]
reactions: [18O-181Ta-deep-inelastic]
methods: [doppler-correction, doppler-shift-attenuation-method, particle-identification, gamma-ray-tracking]
tags: [agata, paris, vamos, rf-drift, calibration, lifetime-energy-degeneracy, preliminary]
---

# 20O 的 DSAM 能量—时间—velocity 契约

## Bibliographic Record

M.Ciemała等，ActaPhysPolB50(3),615–624(2019)，DOI10.5506/APhysPolB.50.615，Crossref/官方PDF身份核验。论文为2018Zakopane conference contribution，received23Jan2019；title中的“Determination”不能代替其实际analysis-in-progress结论。

raw未改：raw_file保留槽未填充；public publisher PDF10页copy在 `tmp/day13/reopened/20o-2019-acta-dsam.pdf`，SHA如上。实际覆盖整篇，不把publishercopy或会议总结说成已归档raw/events。

## Scope and Reading Depth

- 全文10页：motivation/model predictions→deep-inelastic setup→VAMOS/PARIS/AGATA校准→mass/RF drift→anglecentroids→五stage simulation→plannedtwo-parameterχ²。
- 关键视觉核验PDFp4/journal618 calibration式，p8/622 output/plannedenergyfit，p10/624 Fig8/τlabel。
- 未覆盖：已发布的后续finalfit、rawevents/code/targetstopping/tracking/response版本、precise2396-keVrestenergy、完整RF-cycleassignment与calibrationcovariance、引用abinitio计算原文。未提取新τ/B。

## Paper Question and Scientific Motivation

用DSAM测试neutron-rich20O的第二2+态transitionproperties与NN/NNN force模型；本轮优先学习其velocity-history、energy/calibration和实际result status，避免将modelnumbers或futureχ²拟合写成已经测得的寿命。

## Method and Design Logic

VAMOSpath/TOF得到exit-ionvelocity并结合energy/PID校准；PARIS提供RF drift参考；knownlongline与shortline角依赖对照；用targetreaction/slowing+γtracking+crystalresponse生成模拟，再拟合寿命及unknownγenergy。每步共享数据/模型必须保留。

## Key Evidence and Reasoning Chain

RF/energy/path联立校准→Oisotope/charge IDs与mass稳定→angle-dependentcorrectedenergy→lifetime/energy响应模型→计划二维χ²。没有finalminimum/uncertainty/τtable，也不由model320/200fs直接判断实验偏向某force。

## Summary

实际18O126MeV+181Ta6.64mg/cm²、31AGATA/PARIS/VAMOS实验独立于AS21的19O(d,p)20O MUGAST数据。长2+1→ground参考与短2396keVline的angle shifts不同；source指出需要jointτ/Eγfit，但最终值在本篇尚未给出。RF/energy/PID校准与输出velocitystage仍是必要身份信息。

## Experimental or Theoretical Setup

18O7AMeV深度非弹性，beam在target中心约116MeV；projectilelikeβ≈.10。VAMOS45°、31AGATA约120–175°、PARIS与额外LaBr3约90°。Focaldrift/ionization/plastics及target后20cm entrance tracking说明pp.2–3。此target不是AS21的CD2/Aubacking。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CO19-1 | NN与NN+NNN计算的20O2+2 lifetime320/200fs为引用modelpredictions；本篇不报告将它们测成这两个数字。 | model-result | indirect | PDF p.2/journal616, Introduction, Refs1/2 | true |
| CO19-2 | Deep-inelastic18O126MeV+Ta6.64mg/cm²(4μm)、31AGATA/2PARIS/VAMOS45°为该实验；不能绑定AS21transferdataset或Au history。 | experimental-fact | direct | PDF pp.2–3/journal616–617, Sec.2 | true |
| CO19-3 | v=D/T，RFpulse间隔102ns；source明确masses依time与energy，要求同时校准。M/Q用Bρ/(3.105γβ)，M0=Etot/[931.5016(γ−1)]，Qint为nearestinteger，再Mr=(M/Q)Qint。 | experimental-criterion | direct | PDF p.4/journal618, Sec.3 equations | true |
| CO19-4 | Source不同旧constants3.105/931.5016与AS213.107/现代u值不静默改写；执行calibration/version与RF-cycleoffsetprocedure尚未给全，不仅据integerlabel或massmatching认独立clockvalidation。 | synthesis | direct | PDF p.4/journal618; [[assie-2021-mugast-agata-vamos]] AS21-9/10 | true |
| CO19-5 | Fig3显示O q7/8；caption为readability统一用Mr=(M/Q)×8绘图，故q7位置被shift，不是实际两条masspeak无歧义。 | experimental-criterion | direct | PDF p.5/journal619, Fig3/caption | true |
| CO19-6 | 实际18Omass随run time漂移与PARIS–RFtiming同pattern；源以PARIStiming修正ionT后提高mass稳定。SharedRF影响仍不能当两套完全独立clock。 | experimental-fact | direct | PDF pp.6–7/journal620–621, Fig5 | true |
| CO19-7 | Long20O2+1→ground line约1674keV，Fig8 labelτ10.5ps；作者将平均energy差≈0解释为主要target外emission，不提供本任务独立τ测量或alloutside概率。 | author-interpretation | direct | PDF pp.6,10/journal620,624, Fig8/description | true |
| CO19-8 | 2396keV2+2→2+1 correctedcentroid相对tabulatedenergy的差随backwardangle增大；authors以known18O27fs/19O92fs等趋势作method对照。具体sourcecal原文Ref8未读，不把这些τ当本篇新测。 | experimental-fact | direct | PDF p.6/journal620, Fig8; Ref8 | true |
| CO19-9 | precise2396restenergy缺口使作者要求varyτ和Eγ；计划two-dimensionalχ²min尚待进行，本文无finalτ/CL或absoluteB。 | experimental-criterion | direct | PDF pp.8–9/journal622–623, simulation setup/Conclusions | true |
| CO19-10 | Generator让beam能损、按literal“linear probability in target”发生transfer，fragmentexcitation以measuredvdistribution调节；current-ionvelocity作forwardDopplershift，若γ在target内发出则ion继续处理到target末端。 | model-result | direct | PDF pp.8–9/journal622–623, event-generator bullets | true |
| CO19-11 | Detectorgeometry31crystals、same-as-experimenttracking/correction、experimentallyextractedcrystalenergyresolution/count-rate weights，再比较χ²；这些是modelchain/拟合设计，不新独立数据。 | model-result | direct | PDF p.9/journal623, simulation bullets | true |
| CO19-12 | 输出“velocityvector of every gamma emitter”及“Dopplercorrected”未在本文明确所有variable的emission/targetexit标签；forward/currentvelocity与targetend处理需executedcode确认，不能据名称判已correct-with-truthor宣称源code错误。 | our-inference | indirect | PDF p.9/journal623, output/tracking bullets | true |
| CO19-13 | Authors称angle shifts表明τ2+2 below~300fs、stats足够；这是preliminarysensitivity interpretation，没有quantifiedCLupperlimit或已给finalbestfit。 | author-interpretation | direct | PDF p.9/journal623, Conclusions | true |
| CO19-14 | 正文p6把PARIS的4+分支写为→g.s.，Fig6p8却标1894keV4+→2+；本页保留branchlabel冲突，不把该line补成独立已核placement或更改publishedfigure。 | synthesis | direct | PDF pp.6,8/journal620,622, Fig6/text | true |

## Nuclear Structure Information

2+1与2+2 transition是示例；320/200fs属于引用理论，10.5ps为source参考label、below~300fs为初步解释，三者不可合并成newmeasuredabsolute-strength或NNN-force裁决。

## Authors' Interpretation

角依赖centroid对shortτ敏感，longτ参考line帮助calibration/history检查；需要将τ与Eγ一起拟合。关于NNNforce的motivation是未来test，不是本报告已支持某模型。

## Model Results

反应深度、两fragmentexcitation、currentvelocity、γisotropy、stopping/targetexit和detectorresponse同属source generator/transport/tracking链。Literal“linearprobability”未给执行density函数，不擅自替成uniformdepth；source当前不是我们独立reproducedpacket。

## Competing Interpretations and Limitations

- lifetime与unknownEγ/calibration、velocity/stopping/feeding/response可耦合；directbenchmark不唯一选择τ。
- mass与time/energy共同计算，PARIS/RF修正也是shared reference，需covariance/RFcycle/basis/code而非独立error叠加。
- correctedenergy的“emittervector”必须有stage；采用truth instantaneousβ会移除所需energyhistory，而实验是late-ionmeasurement。这是variablecontract需求，不指控源实现。
- 深度非弹性Ta4μm与AS21的transfer/CD2/Au不同；只同20O不计同dataset或可移植history。
- 后续paper若已有finalτ需另读/另记version，不反投到2019progressreport。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| CO19-AR1 | result boundary | nofinalτ，below~300fs不是正式CLlimit，200/320不是measuredvalues。 | CO19-1/9/13 | unreviewed |
| CO19-AR2 | stage/calibration | late-ionspeed、RF/energy/PID、currentγforward/stopping都需明确contract，obs与simulation共校准/weights。 | CO19-3/6/10/11/12; [[doppler-correction]] | unreviewed |
| CO19-AR3 | companion | longline/angle/knownτcontrols帮助排calibration/velocity差，但不能替actualΣ或把meanflight视alloutside。 | CO19-7/8 | unreviewed |

## Knowledge Impact and Learning Decision

`supports` jointenergy/historycalibration与独立companionline；`limits`paper title/modelnumbers/zeroaveragecentroid/稳定mass自动证明finallifetime。与 [[doppler-velocity-validation-contract]]、[[doppler-correction]] 同步，actual实验L4仍not-ready。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-correction]] | exitvelocity/history、jointτ/E、RF/energy/PID。 |
| methodological-bridge | [[tracking-array]] | same-as-data modelchain需要stage/responseidentity。 |
| competing-interpretation | [[assie-2021-mugast-agata-vamos]] | same20O不同reaction/target/DAQ，不转移Au/width/normalization。 |
| methodological-bridge | [[vandebrouck-2016-vamos-dual-position-mwpc]] | source引用entrance-vector方法，实验条件另行。 |

## Human Review Triage

P0：source身份/public/raw未归档与no-final-result状态隔离。P1：CO19-1/7/9/13数值层；CO19-3/4/6sharedcalibration，CO19-10/12emissionexitvariablecontract。No human-reviewed升级，无新增τ/B。

## Extracted Pages

2026-10-14directRef8续读 [[ziliani-2019-agata-calibration-controls]] ZL19-1/2/4/8/9：同July2017data，提供GGPtimealign、energyanchors及1938.2/1981.93short/longcontrol的preciselocator；不新增independentdataset，不补本文的finalτ或outputβ-stagecode。

PDF1–10/journal615–624全主线；关键4/8/9/10视觉核验。Originalcode/stopping/Σ及后续fit仍未取得。
