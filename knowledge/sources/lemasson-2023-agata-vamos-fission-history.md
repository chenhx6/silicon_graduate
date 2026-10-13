---
type: source
title: "Lemasson 2023：fission Doppler 的角覆盖、degrader 与 prompt-delayed history"
aliases: [AGATA VAMOS fission spectroscopy 2023, Lemasson prompt delayed recoil history]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: instrument-experiment-review
reading_depth: deep-read
title_original: "Advancements of gamma-ray spectroscopy of isotopically identified fission fragments with AGATA and VAMOS++"
authors: [A. Lemasson, J. Dudouet, M. Rejmund, J. Ljungvall, A. Görgen, W. Korten]
journal: The European Physical Journal A
year: 2023
volume: 59
issue: 6
doi: 10.1140/epja/s10050-023-01053-0
arxiv: 2306.10818v1
data_version: public-arxiv2306.10818v1
language: en
canonical_source: "https://arxiv.org/abs/2306.10818v1"
citation_key:
raw_file: "raw/papers/gpt/day13/lemasson-2023-fission-spectroscopy.pdf"
raw_sha256: "f4213d54aacddaa7a5dd34a4e869fb9da2829000246078d48d5beac43a0111be"
raw_storage_status: reserved-unpopulated-public-preprint-only
external_pdf_url: "https://arxiv.org/pdf/2306.10818v1"
nuclei: [98zr, 96kr, 81ga, 84ge, 132te]
methods: [doppler-correction, recoil-distance-doppler-shift, prompt-delayed-coincidence, isotopic-identification]
tags: [agata, vamos, fission, velocity-stage, degrader, angular-coverage, data-lineage]
---

# Fission γ 的 velocity history 与数据归属

## Bibliographic Record

A.Lemasson等，EPJA59(6)(2023)，DOI10.1140/epja/s10050-023-01053-0，Crossref题名/六authors/年/卷/期核验；metadata未给页号，不猜。实际读arXiv2306.10818v1 public12页，header19June2023、PDFbuild21June2023；manuscript占位receipt/article字段不是正式publication页码。

raw保持不变：raw_file未填充，copy仅在 `tmp/day13/reopened/lemasson-2023-fission-spectroscopy.pdf`，hash如上。Figures不少由原publications/thesis改编，review不增加独立acquisition。

## Scope and Reading Depth

- 12页主线：fission/isotopic identification→Table1 fourexperiments/geometry→eventvector/energy correction→EXOGAMcomparison→Kr/Ga examples→RDDS withdegrader→promptdelayed/Te/Sb→conclusion/references。
- 核心：PDFp2Table1、pp.3–5 velocity/angle/Fig3与widths、pp.6–8Fig6/7的after-degrader reference、pp.8–9 focal-plane stopping/PD、p11Ref40/41与campaign acknowledgments。Fig6p7视觉核验。
- 未覆盖：所有underlyingpublications/data/code、完整event-selection、angle/PID/response/covariance、spectrometer/degrader stopping inputs。Source的部分shape/shell解释不作本任务新验证。

## Paper Question and Scientific Motivation

以AGATA+VAMOS++不同configuration的fission spectroscopy说明isotope标签、first-IP精度、velocity history与prompt/delayed采样怎样改善实验判别。这里优先审计Doppler的stage和benchmark比较，避免把same nuclide、同设施或review重复引用当同一/独立数据的充分证据。

## Method and Design Logic

VAMOSenergy-loss/rigidity/path/TOF识别一片fragment→DPS-MWPCvector及AGATAfirst-IP→eventinverse；RDDS换用degrader保留可飞行residue，测得的是post-degrader vd，故S/U对应不同emissionstage。长isomer通道则将target附近prompt与focal-plane停后delayedγ配对。三种history和角覆盖不能合并成一个β/响应。

## Key Evidence and Reasoning Chain

Table1run配置→v/angle acceptance→同nuclide不同array/角选择比较→same-transitionS/U信息→focal-plane晚光子→原report/interpretation/model/lineage分开。更窄峰支持方法改善，未补出allabsoluteintensities或完整lifetimefitpacket。

## Summary

Source明确EXOGAMall-rings15keV、backward-only7keV与AGATA5keV的不同angular selection；98Zrline为1222.9keV。Fig6把post-degrader vd用作reference，保留before-degrader发射的角相关Sband，它是寿命信息的一部分。PDsource另外在离target约760cm处停止ions，lateγ不能沿用targetemitter速度。

## Experimental or Theoretical Setup

Table1四experiments共同238U6.2MeV/A，配置不同：Exp1无degrader、target1.6/5μmBe、32crystals/R13.5cm；Exp2无degrader、10μmBe、24/R13.3cm；Exp3 11μmBe+18.5μmMg、24/R18.6cm；Exp4 10μmBe+16.7μmMg、35/R23.5cm。VAMOS中心角/覆盖也不同。p11列e661/e680/e669/e706 acknowledgments，但不仅按列出顺序补写完整run-file映射。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LS23-1 | Table1将prompt/PD与两RDDS datasets分为Exp1–4，target、Mgdegrader、距离、crystal数、角覆盖不同；相同238Uenergy不等sameacquisition。 | experimental-criterion | direct | PDF p.2, Table1/experiment list | true |
| LS23-2 | 作者提出fragment-angle precision<1°、target-point<1mm作为tracking-resolution主导的设计要求；这是其context的criterion，不消去intrinsic/velocity covariance或所有nuisance。 | experimental-criterion | direct | PDF p.2, tracking/recoil paragraph | true |
| LS23-3 | Exp1 Fig2显示Z40/50/60的v与laboratoryangle/γ–fragmentangle不同相关分布；v2.9–4cm/ns、meanpath760cm对应flight约190–260ns。 | experimental-fact | direct | PDF pp.3–4, Fig2 and text | true |
| LS23-4 | promptinverse用fragmentvector和γfirst-IP；complementaryfragmentγ若用detectedfragmentβ会shift/broaden。Binarypartner correction被作者转述为可借two-body kinematics，primaryRefs3/4本轮未直接读，不认作无条件exact partner reconstruction。 | author-interpretation | direct | PDF p.4, Sec.3, ERF formula and partner paragraph | true |
| LS23-5 | 98Zr2+→0+ line写1222.9keV；EXOGAMall clovers含90°/135°给15keV，backward-only7keV；AGATA100–170°给5keV。不能把15/5当matchedangulargeometry的纯algorithm gain。 | experimental-fact | direct | PDF pp.4–5, Sec.4.1/Fig3 | true |
| LS23-6 | Fig3两个spectra归一到same total counts；不是sourceabsoluteγefficiency/peakretention比较。AGATA例为Exp1，EXOGAM为另一array数据。 | experimental-criterion | direct | PDF p.4, Fig3 caption/section | true |
| LS23-7 | Source引用DPS-MWPC与PSA/energy-dependent位置原文Ref40/41–44；Ref40=VD16、Ref41=LG20。各benchmark仍需run/target/angles绑定，不默认所有98Zr图共一dataset。 | synthesis | direct | PDF pp.3–4; p.11, Refs40–44 | true |
| LS23-8 | Exp4 Fig6在470μm gap以measured post-degrader vd校正：afterdegraderγ是U，beforedegrader vt>vd是S；backwardangles使S能量更低且随α变。U不等stopper里β0。 | experimental-fact | direct | PDF p.7, Fig6/Sec.5.1 | true |
| LS23-9 | Fig7比较AGATAExp4与EXOGAMRef33的S/U及distance演化；引用2+/4+/6+ meanlifetimes3.8±.8/7.5±1.5/2.6±.9ps。不是本review重新独立测三τ，也不据singlepeakheight直接求τ。 | experimental-fact | indirect | PDF pp.7–8, Sec.5.2/Fig7; Refs21/33 | true |
| LS23-10 | 低stats的84GeRDDS采用summing overdistances variant；形状/collectivity推断来自原Ref19与model比较，不由本Dopplerbenchmark独自证明。 | author-interpretation | indirect | PDF pp.7–8, Sec.5.3/Fig8, Refs19/54 | true |
| LS23-11 | Exp1 PD method：target附近AGATAprompt、flight约200ns后ions停在ICgas，7个FP EXOGAM探delayed；source报告100ns–200μs能力范围。具体gate/ε/start packet本轮未取得。 | experimental-criterion | direct | PDF p.8, Sec.6.1 | true |
| LS23-12 | 132Te7− t1/2=28.1μs为external prior；Fig9以delayed151keV门观察prompt292/624/900/1040，又以prompt1040门观察late103/151/697/974；是同Exp1联合correlation，不四/多次独立实验。 | experimental-fact | indirect | PDF p.9, Fig9 and text; Ref12/58 | true |
| LS23-13 | 96Kr515-keVline原dataset受stats限制未可靠placement；review转述后续observedcoincidence后仍未placement。Correctedenergy/observedpeak与唯一levelidentity/Jπ不是同物。 | author-interpretation | indirect | PDF p.5, Sec.4.2, Refs16/49 | true |
| LS23-14 | Source将shapechange、shellclosure/seniority等解释归于原reports/LSSM/beyondmeanfield；data、model与结构interpretation需分层。 | author-interpretation | indirect | PDF pp.5–6,8,10, model comparison paragraphs | true |
| LS23-15 | p5原文把96Kr写Z38，p6一处把78Ni写A50；其它位置及element身份不同。本页保留为printedfield边界，不将这两个标签摄入为核素事实。 | synthesis | direct | PDF pp.5–6, Secs.4.2/4.3 | true |

## Nuclear Structure Information

只将98Zr/132Te/96Kr等作velocity/history/identity方法examples。原Kr/Ga/Ge/Sb的structural解释属于originalsources与models，不能因review+本task多一次引用提高A≈130structure信心。

## Authors' Interpretation

Gamma first-IP与particlevector提高resolvingpower；连续angle提供RDDS杠杆；promptdelayed门跨isomer支持placement。关于N60shape、N50core、B(E2)/seniority是受source/model约束的解释，不作本run新的实验裁决。

## Model Results

原LSSM/PFSDG-U、Ni78core/pseudo-SU3及DD-PC1比较共享publisheddata；本页未运行这些模型。下面的piecewisevelocity/proper-clock、survival/gate练习为our-inference，未拟合originalFigures。

## Competing Interpretations and Limitations

- C23的15→5简述与本篇7(backward)→5的控制范围不同，array、geometry、normalization都需保留。
- Measured post-degrader vector不等每条γ的emittervector；intentional S/U保持可分析history，不能把everyresidual当校正失败。
- Isotope标签只能绑定detectedion；complementaryfragment、移到FP的delayedγ与目标prompt需各自stage/response。
- PD看不到某γ仍需survival、时间/能量window、branch/ICC、材料/几何与background sensitivity，不能直接排isomer。
- Tables/figures/引用thesis与reviews共享acquisition；VD16的校准26°与LG20/本篇配置未完全绑定，source-filemanifest仍缺。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| LS23-AR1 | comparison controls | 不使用15/5证明same-angle纯算法factor3；backward-only7/5仍有不同array/config，未移植efficiency。 | LS23-5/6; [[tracking-array]] | unreviewed |
| LS23-AR2 | history observable | 使用vd使U恢复reference、S保持angleband，是lifetimeanalysis的有意定义；truth βem校正全部energy虽能collapse，却不保留energy-onlyhistory信息。 | LS23-8/9; [[doppler-correction]] | unreviewed |
| LS23-AR3 | delayed absence | source给flight/stop/gate尺度，survival与clock/history是negativeevidence必要输入；任务toy不测新的τ。 | LS23-3/11/12 | unreviewed |

## Knowledge Impact and Learning Decision

`revises`same-angular-coverage benchmark与“U意味着β0”的外推；`supports` velocity-stage/PD设计；`limits`source重复引用、singlecorrectedpeak或晚γabsence的强结论。Detailed公式/条件写 [[doppler-correction]]、[[tracking-array]] 与 [[gamma-gamma-coincidence]]。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-correction]] | post-degrader reference与prompt/FPhistory。 |
| methodological-bridge | [[tracking-array]] | angularselection与normalizedbenchmark控制。 |
| methodological-bridge | [[gamma-gamma-coincidence]] | joint PD/entrypoint及共享counts。 |
| same-lineage | [[crespi-2023-agata-tracking-performance]] | C23引用本篇的comparisondiscussion，需用详细角选择限范围。 |
| methodological-bridge | [[vandebrouck-2016-vamos-dual-position-mwpc]] | Ref40particlevector；run绑定不自动。 |
| methodological-bridge | [[ljungvall-2020-agata-ganil-performance]] | Ref41positionresponse；实验配置保留。 |

## Human Review Triage

P0：sourceidentity/raw未归档与printednucleus标签边界隔离。P1：LS23-5/6angular/scale，LS23-7lineage，LS23-8/9postreference/lifetime，LS23-11/12absence/halfmeanlife，LS23-15打印字段。Self-audit不记human-reviewed。

## Extracted Pages

PDF1–12全文主线；corepp.2–5,7–9,11；Table1/Fig6视觉核验，underlyingfullpacket仍未取得。
