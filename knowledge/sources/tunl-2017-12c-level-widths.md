---
type: source
title: "TUNL 2017KE05 在线 12C 宽度表：total/partial Γ 与修订版本"
aliases: [TUNL 12C evaluated widths, TUNL 2017KE05 tables 12.13 12.14]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-tables
reading_depth: read
title_original: "Energy levels of light nuclei A=12 — TUNL online Tables 12.13 and 12.14"
authors: [J. H. Kelley, J. E. Purcell, C. G. Sheu]
journal: Nuclear Physics A
year: 2017
volume: 968
pages: 71-253
doi: 10.1016/j.nuclphysa.2017.07.015
data_version: "online 2017KE05 tables accessed 2026-10-14; companion manuscript revised 08 October 2020"
canonical_source: "https://nucldata.tunl.duke.edu/nucldata/HTML/A=12/12_13_2017.pdf"
citation_key:
raw_file: "raw/papers/gpt/day13/tunl-12c-table-12-13-2017.pdf"
raw_sha256: "f24d1df603869579b2de604ea726e5de65b766985f8b07724d6dfa66a3c61727"
raw_storage_status: reserved-unpopulated-public-evaluation-table-only
external_pdf_url: "https://nucldata.tunl.duke.edu/nucldata/HTML/A=12/12_13_2017.pdf"
nuclei: [12c]
methods: [doppler-correction]
observables: [natural-level-width, gamma-partial-width, lifetime, branching-ratio]
tags: [tunl, evaluated-data, width, photon-recoil, evidence-version]
---

# 12C 的 natural width、部分宽度与版本身份

## Bibliographic Record

J.H.Kelley/J.E.Purcell/C.G.Sheu，*Nuclear Physics A*968,71–253(2017)，DOI10.1016/j.nuclphysa.2017.07.015，Crossref身份核验。本source使用**官方在线数据表**：Table12.13(6页)与[Table12.14(5页)](https://nucldata.tunl.duke.edu/nucldata/HTML/A=12/12_14_2017.pdf)，标签2017KE05、获取日期2026-10-14；不是声称逐字引用未经修订的2017publisherPDF。

官方[companion PDF](https://nucldata.tunl.duke.edu/nucldata/ourpubs/12_2017.pdf)封面明确为“Revised Manuscript /08October2020”，并说明纠正出版后错误、referencesclosed2016、introductionomitted。PDFheader另一处印2016，而abstract/Crossref出版年2017；这些日期字段分开保留。选定15.110MeV行在onlineTable13p3与companionfilep45匹配，不能据此保证全部online表与所有publicationversions一致。

保持raw不变：raw_file为未填充保留位置；真实Table13获取字节在`tmp/day13/reopened/tunl-12c-table-12-13-2017.pdf`，SHA为frontmatter列值。Table14的SHA为`d12054bb0e5aa91b1f61c00fcdb52f7d410c59e9b7ecd7ddb75c9f5d3a1d407a`；companionPDF为`eab1e594a921be2565ee87817a4447e1fe2d7cc77bebe8fa2ecf3eadb63c6146`。临时副本失效须重获并核对版本/指纹；不声明已raw归档。

## Scope and Reading Depth

- 实际范围：selected12Clevelrecords、Table13/14相关rows与footnotes、官方HTML/质量链入口和companionrevisionmetadata；15.110row与referencekey/version查核。
- 核验位置：Table13p1的4.43982、p2的9.641/14.079、p3的15.110/16.1060、p5–6footnotes；Table14p1的15.11partials和p4–5deduction/branchingfootnotes。核心PDF页视觉核验。
- Not covered：257页parentA=12evaluation全部主线、每个reaction/level原实验、完整widthcovariance、2020all-correctionslist、当前所有更新或ENSDF独立比对。本页`read`仅指已声明dataset-record范围，不把parentarticle标deep-read。
- 评价表是许多实验的综合，Table13/Table14/HTML/companion并非几份独立测量。

## Paper Question and Scientific Motivation

本次读取目标是给Doppler宽线诊断一个有版本/locator的naturalΓ与γpartialΓ锚点，区分levelwidth、branchrate、detector/kinematicwidth和photonrecoil。未给12Ccollective-mode新解释。

## Method and Design Logic

从官方质量链12入口进入12C2017KE05记录，再读可下载Table13/14及其footnotes，并与companionrevision声明/selectedrow比对。直接字段Γcm、Γγ0、Γγ/Γ与各自单位/分母保留；derivedwidths不当成独立inputs。旧LiveChart403challengeHTML不用于数据填充。

## Key Evidence and Reasoning Chain

levelidentity/Γcm → partial/radiative/particle-widthblock → footnotededuction → naturalτ/branch中心商 → 与Crespi15.1MeV119keVline的instrument/motionwidth分层。instrumentpaper与evaluation回答不同observable，不将两个source当作独立测量同一β或Γ。

## Summary

Table13的15.110±3keV、1+;T1level给totalΓcm=43.6±1.0eV。Table14给groundγpartial38.5±.8eV、totalγ41.8±1.1eV、γfraction.959±.009，并注明部分量deduced。自然statewidth0.0436keV远小于Crespireported119keVFWHM；不能以groundpartial38.5eV代替totalΓ计算lifetime。

## Experimental or Theoretical Setup

数据类型为evaluatedcompilation，不是本任务rawexperiment。Table13其他例子：4.43982MeV2+ totalwidth10.8±.6meV，9.641MeV3− Γ46±3keV，14.079MeV4+ Γ272±6keV；不同level的naturalwidth可以跨多个量级。Broadgroup还可能有stateidentity/interference边界，见footnoteq。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| T12C-1 | 在线Table13列Ex15.110±3keV、Jπ=1+、T1、Γcm=(43.6±1)×10⁻3keV，decaysγ/α；companionfilep45selectedrow一致。 | synthesis | direct | online Table12.13 PDF p.3, 15.110-MeVrow; revisedcompanionfilep45 | true |
| T12C-2 | Table14在15.11block列Γγ0=38.5±.8eV、Γγ=41.8±1.1eV、Γα=1.79±.39eV、Γ=43.6±1eV，以及Γγ/Γ=.959±.009；footnotes e/g/h/i/r说明部分width/ratio的shared/deduced谱系。 | synthesis | direct | online Table12.14 PDF p.1,15.11block; p.4,footnotese,g,h,i,r | true |
| T12C-3 | Table14footnotee给gamma-decaybranchground92±2%、到4.4等分支及未探到的10.3分支；它与totaldecay含α的分母不同。中心商38.5/41.8≈.921与38.5/43.6≈.883为本任务算术，不给缺失covariance的ratioerror。 | our-inference | indirect | online Table12.14 PDF pp.1,4,15.11block andfootnotee | true |
| T12C-4 | Table13的4.43982MeV Γ10.8±.6meV与9.641MeV Γ46±3keV展示naturallevelwidth不必统一很小；这些不是本任务观察到的γFWHM。9.641width有weighted/external-errorfootnoteb。 | synthesis | direct | online Table12.13 PDF pp.1–2; p.5,footnoteb | true |
| T12C-5 | Table14printed15.11γpartials的中心值合42.74eV，而printedtotalγ41.8eV；差.94eV，且多项deduced/shared、jointcovariance未给，不能仅据中心sum宣布erratum或修表。 | our-inference | indirect | online Table12.14 PDF p.1,15.11block; p.4,footnotese/h | true |
| T12C-6 | Table13footnoteq把historic10.3MeVbroadgroup保留为有未解决identity/interference问题的记录；不能把一个宽group无条件写成单孤立resonance天然Γ。 | author-interpretation | direct | online Table12.13 PDF p.6,footnoteq | true |
| T12C-7 | 官方companion封面为2020-10-08修订，说明出版后纠错；Table13/14以2017KE05标识。需要分别记录pubyear、online-tableaccess/hash和revisiondate，不能把online数值默认为未修订2017original。 | synthesis | direct | revisedcompanionPDF filep1; onlineTable12.13 header | true |

## Nuclear Structure Information

本页只固定选定level/width/branch记录与边界；不用这些methodexamples定义新的12Cband或A≈130mode。Broadαresonance、narrowM1level与instrumentDopplertest需依specificstate/decaychannel比较。

## Authors' Interpretation

评价正文/footnotes对部分broadgroup和deducedbranch保留历史/适用解释；这些解释不能从一个fieldΓ直接消去。source正是multi-sourcecompilation，不假定当下争议已关闭。

## Model Results

Γ/τ关系、free-nucleustwo-bodyphotonrecoil和Lorentzframe比对为本任务通用物理/推导，见 [[doppler-correction]] 与 [day13_photon_recoil_width.py](../../system/scripts/day13_photon_recoil_width.py)。parent/daughterframe例题采用mass-numberapproximation，不是source再拟合。

## Competing Interpretations and Limitations

- totallevelΓ≠某γpartialΓ；以partial代total给radiative等效time，不是levelmeanlife。
- measuredkeVFWHM不能直接当totalnaturalΓ；反过来Γ≪observedwidth也不能独自分解β/position/response。
- Table13/14依赖同一evaluation、原branchinputs和deductions，repeatcitation不增加独立样本；中心ratio只作算术。
- 单个broadgroup可能含overlap/interference；footnotes及reactionidentity不能被discard。
- online/table与publisheroriginal存在版本边界，未独立读原实验/完整parentarticle，不升级human-reviewed。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| T12C-AR1 | naturalwidthfloor | 15.11Γtotal.0436keV→centralmeanlife15.10as；不足以解释Crespi119keV，但不选其kinematicnuisance。 | T12C-1; [[crespi-2013-agata-high-energy-doppler-response]] CR13-3 | unreviewed |
| T12C-AR2 | denominator | Γγ0/Γγ与Γγ0/Γtotal不同，源Crespi92%用语需保留gamma-subset/all-decay的适用context；不因source比较宣布其yield归一错误。 | T12C-2/3; CR13-1 | unreviewed |
| T12C-AR3 | photonrecoil | free-nucleusmass-numberM=12u、gap15.110MeV给parent-restphoton15.0998MeV，gap与photon不相等；真实精确输入仍需nuclearmass/energy/frame。 | T12C-1; [[doppler-correction]] | unreviewed |

## Knowledge Impact and Learning Decision

`supports`有版本的width/branch输入，`revises`把γenergy、levelgap、partial/totalwidth混为一物的判断，`limits`broadgroup/linewidth-only推断。source与 [[doppler-correction]] 双向关联；不计新的independentexperiment或进入实际L4fit。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-correction]] | total/partialΓ、freephotonrecoil和正确emitterframe。 |
| limits | [[crespi-2013-agata-high-energy-doppler-response]] | 15.1MeVtestline的widthscale/branchcontext，不能独自裁决velocityfit。 |
| methodological-bridge | [[level-scheme-reconstruction]] | levelgap与restγenergy、broadgroupidentity需保留原表/footnotes。 |

## Human Review Triage

P0：无未隔离identity/permission风险；online/revision边界与raw未归档明示。P1：T12C-1/2单位/totalpartial、T12C-3/5sharedderivedratios、T12C-6broadgroup、T12C-7版本；正式使用具体claim时回原record/underlyingsources。

## Extracted Pages

Table13selectedrowspp.1–3与footnotespp.5–6；Table14p1与p4–5notes；companionp1/provenance与p45selectedrow。未建立fullparentarticle/PaperCard阅读完成声明。
