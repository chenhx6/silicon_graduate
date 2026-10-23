---
type: source
title: "Purry 1997博士论文：178W电子转换、门与旧DCO赋值的修订"
aliases: [Purry 1997 178W thesis, High-spin multi-particle and collective structure in 178W]
created: 2026-10-18
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: phd-thesis
reading_depth: skimmed
title_original: "High-Spin Multi-Particle and Collective Structure in 178W"
authors: [Christopher Stephen Purry]
year: 1997
institution: University of Surrey
degree: Doctor of Philosophy
date_original: May1997
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "Surrey Open Research doctoral record99513285802346, Purry May1997"
source_url: "https://openresearch.surrey.ac.uk/esploro/outputs/doctoral/High-spin-multi-particle-and-collective-structure-in/99513285802346"
raw_file: "raw/papers/gpt/day16-20261018/purry-1997-phd-high-spin-multiparticle-178w-b8ee1308d487.pdf"
raw_sha256: "b8ee1308d4871c1514d0ed54b3d523104da143bb346088a24eb008d97fc96753"
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [178W]
reactions: [170Er-13C-5n]
experiments: [CAESAR, solenoid-SiLi-electron-spectrometer]
models: [blocked-BCS, band-mixing]
observables: [K-conversion-coefficient, angular-distribution, relative-intensity, half-life, level-scheme]
methods: [conversion-electron-spectroscopy, gamma-gamma-coincidence, delayed-spectra, angular-distribution]
tags: [178w, dco-counter-evidence, conversion-electron, primary-source, source-independence]
---

# Purry 1997：先核实际测量，再使用K-shell companion

## Bibliographic Record

Christopher Stephen Purry，*High-Spin Multi-Particle and Collective Structure in 178W*，University of Surrey Department of Physics，PhD thesis，May1997。实际PDF112页，3,748,295bytes，SHA-256见frontmatter。原title页为PDF4；repository wrapper在PDF1、ProQuest reproduction页在PDF3。2017为复制出版页年份，2026为下载时间，均不替代原1997论文日期。

合法公开入口为[Surrey博士记录](https://openresearch.surrey.ac.uk/esploro/outputs/doctoral/High-spin-multi-particle-and-collective-structure-in/99513285802346)，[实际delivery](https://openresearch.surrey.ac.uk/view/delivery/44SUR_INST/12139097650002346/13140443510002346)。OpenAIRE题名/作者检索先发现该institutional URL，随后实际PDF题名/作者/May1997/内容核验。旧epubs `10147989.pdf`只作发现链接，没有下载或认定其hash相同。当前实际PDF位于`tmp/day16-purry-thesis-retrieval/PDFs/High-spin_multi-particle_and_collective_structure_in_178W.pdf`；raw_file是未填充归档槽，本任务不改raw，不称归档已完成。没有匹配本地Bib条目，key留空。

## Scope and Reading Depth

本轮为**围绕电子/γ响应与DCO反证的定向原件阅读**，whole-thesis状态仅skimmed。已读title/abstract/contents、Ch1 printed1–3、Ch3 printed12–24的完整实验和离线分析主线、Ch4 printed25–31的纲图/谱/假设、Table4.1 printed32/39/40的所选reference/921/1090行及脚注、printed49–54相关能级讨论、Ch6 printed95–97结论、bibliography的Do79/Kr88/Kr89/Pu95/Ro78。原图重点核printed21/22/23、28/Fig4.1c、31/Fig4.3、32/39/Table4.1、52/能级修订。

PDF页=printed页+9，例如printed21=PDF30、printed39=PDF48、printed52=PDF61。未完整重读Ch2全部模型、Ch5全部blockedBCS/bandmixing/强度推导和Table4.1的318行；不据本次覆盖将其标为全文deep-read。没有作者raw events、响应/校准曲线、完整fit Cov或production code。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| P97-1 | 原研究以170Er(13C,5n)、80MeV在ANU进行；CAESAR六台suppressed coaxial Ge在±148/±97/±47度，另两LEPS在±45度。γ主靶约97%富集、4mg/cm²；PACE最优能72与实际在线选80分开，不能把计算表值作真实束能。 | experimental-identity | direct-primary | printed16–19 Sec3.1–3.5；Table3.1与正文 | true |
| P97-2 | electron测量是额外配置：1.5mg/cm²靶面与beam30度、1nson/约1.7μsoff，cooledSi(Li)在superconducting-solenoid lens内，另有同时测γ的suppressedGe；不把它当同一次CAESAR六台γ响应。 | detector-and-sample-contract | direct-primary | printed21 Sec3.6/PDF30 | true |
| P97-3 | electron和γ的energy/efficiency用152Eu及internal lines校准；校正能量依赖time response后，取beam后50–400ns的matched spectra，从强度比得conversion并与Ro78理论比。此段未列internal calibrator逐线、效率曲线/完整Σ或921峰分解recipe，未因此宣称完全未校准。 | experimental-calibration-and-boundary | direct-primary-and-self-audit | printed21–22 Sec3.6/PDF30–31；printed31 Fig4.3 | true |
| P97-4 | angular a2来自prompt-gated singles强线或early-delayed角矩阵弱线，作者拟合W0(1+a2P2)；prompt限制旨在减isomer去取向。它不是包含A4的已知完整coefficient，也不自动与50–400ns electron/gamma sample共用ρ。±20ns/±160ns等γγ时间与beam gate有不同定义。 | angular-estimator-and-gate-boundary | direct-primary-and-self-audit | printed22–24 Sec3.7；printed21 timing说明 | true |
| P97-5 | Table4.1 p39的920.8行：3053→2132、11-→10-、Iγ34(2)、a2−.03(.12)、KICC.0067(.0011)；1089.6行：3053→1964、11-→9-、Iγ43(3)、a2+.07(.10)、KICC.0031(.0005)。原图核准两个K值，δ未列。 | measured-selected-target-rows | direct-primary | printed39 Table4.1/PDF48 | true |
| P97-6 | γ强度由singles/coincidence组合，归一237-keV yrast4+→2+为1000；表脚注有通常Eγ±.1keV/weak近keV规则。两行中央I1090/I921=43/34=1.264706只是本任务算术，shared normalization/Cov未得，不能当另一份测得branch或与1989比值独立相乘。 | normalization-and-derived-arithmetic | direct-and-task-calculation | printed25 Ch4intro；printed39–40 Table4.1/脚注 | true |
| P97-7 | Fig4.3上段明确50–400ns、下段高能electron谱标921K与1090K；图像不是原逐bin数据或gate/efficiency矩阵。paper/thesis/ENSDF相同K数值按同一producer谱系，不计三次独立测量。 | spectrum-and-dependency-boundary | direct-primary-and-source-synthesis | printed31 Fig4.3；printed39 Table4.1；N178-12 | true |
| P97-8 | 作者以290-keV KICC=.027(+.004/−.007)对照其旧理论E1 .021/E2 .068，改旧3525态I14为13-；未见旧至yrast12+连接，prompt时序给该态T1/2<1ns，旧35ns改归上方3654态约30±1ns，经68/61两低能线隔开。这是作者的后续实验修订，不倒写成KF89原文已这样赋值。 | experimental-reassignment-and-counter-evidence | direct-primary | printed52–54 Sec4.2.3–4.2.5/PDF61–63；Figs4.1d/4.8/4.9 | true |
| P97-9 | 原文对3053态保留11-并给新branches、tentative4qp组态；对3235态以新branches确认12+。新的3525/3654时序与spin变化提醒复核KF89的35ns/σ假设，但不能据此量化原921 δ改动或自动推翻其两支。 | transfer-and-inference-boundary | direct-primary-and-self-audit | printed50/52–54；KF89 printed337异构体假设 | true |
| P97-10 | Table4.1 p32的168.0/168.3来自不同母态和Jπ路径却同列a2−.67、无误差；必须回原峰/门分解，不能当两个独立系数或补error。若截断P2fit，有限角geometry下未拟合P4会投影至b0/b2，不能直接把quoted a2等同完整A2。 | estimator-and-line-identity-boundary | direct-primary-and-task-calculation | printed32 Table4.1/PDF41；printed23 Sec3.7.2；day16_purry_observable_ledger.py | true |

## Summary

这份primary补齐了reported921 KICC的实验装置、时间窗、校准种类、原表和谱身份，也直接提供旧DCO最终赋值被后续KICC/符合时序修订的反例。它没有提供可重做原实验拟合的全部counts/response/Σ；本任务不以两个理论点的literal比较重测δ或裁决结构模式。

## Competing Interpretations and Limitations

- Kexp已作校准不是“完全未知”；未知的是实际校准/接受/门/峰分解/Σ细节，限制独立重放和联合显著性。
- prompt angular a2、delayed KICC和1989 DCO有不同gate与装置；同母态或同energy不自动证明相同conditional density。
- Kforbidden/hindered interpretation、blockedBCS和tentative组态与直接谱学量分层；本次没有从上限寿命确认动态penetration大小，也未引入自由参数修正ICC。
- 1997 thesis与1998Purry NPA论文的相同数值/实验路线视为dependent；实际正文尚未取得的1998paper不假称逐字一致。

## Analytical Reconstruction and Self-Audit

[day16_purry_observable_ledger.py](../../system/scripts/day16_purry_observable_ledger.py)以PDF hash和selected表行作identity核验，保存γAD与electron两个measurement ledger。对实际47/97/148度作full[1,P2,P4]设计秩检查，再以**声明equal weights**检查省略P4时对[1,P2]的投影；实际权重不在论文中，结果不是source fit或实际A4。Table43/34的rho敏感性只是误差传播，不给新分支误差。

## Knowledge Impact and Learning Decision

`supports` matched electron/γ和original-source优先；`revises` 将reported a2与full A2、delayedK与promptDCO视为共同ρ的做法；以P97-8为`counter-evidence`限制DCO采用值的唯一性。原KF89历史文字保留，新修订不冒充原文结论；source/page/claims均非human-reviewed。

## Related Knowledge and Project Relations

- [[w178-921-dco-gate-double-solutions]]：真实target、KICC与旧DCO反证。
- [[nndc-2009-178w-dco-reference-records]]：primary→评价的相同表值与lineage。
- [[kramer-flecken-1989-use-dco-ratios]]：原35ns/14采用值与后来修订分开。
- [[internal-conversion-analysis]]、[[angular-distribution]]、[[angular-correlation]]：实际measurement/estimator响应合同。

## Human Review Triage

科学P0使用门：quoted Kexp有校准但不意味着其全response已重放；不同gate和truncateda2不静默合并；3525反例不无依据改写921支或原KF89文字。技术归档/Bib缺口公开保留，已核实际112页原件身份/hash/相关原图，不把metadata或OCR单独作为精确数值证据。所有新claims needs_review:true。

## Extracted Pages

- [[w178-921-dco-gate-double-solutions]]、[[internal-conversion-analysis]]、[[dco-ratio]]。
- [[nndc-2009-178w-dco-reference-records]]作为dependent evaluation入口；未新建整核结构或全部band页面。
