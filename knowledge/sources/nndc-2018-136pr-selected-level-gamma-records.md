---
type: source
title: "136Pr：2018公开评价对象中的旧连接与顺序边界"
aliases: [NNDC 136Pr ENSDF 2018, 136Pr 1996Pe12 evaluation crosswalk]
created: 2026-10-15
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-object
reading_depth: read
data_version: "201810;cut1-Apr-2018;retrieved2026-10-15"
title_original: "Nuclear Data Sheets for A=136"
authors: [E. A. McCutchan]
journal: Nuclear Data Sheets
year: 2018
volume: 152
pages: 331--667
doi: 10.1016/j.nds.2018.10.002
canonical_source: "NNDC:ENSDF:136PR:136059001,136059003"
citation_key: nndc_2018_136pr_selected_ensdf
raw_file: "raw/data/gpt/day14/nndc-2018-136pr-adopted.ens"
raw_sha256: cb1ca8660bbf0df17920ec4f366b245cb564d707f116bc1544738fdcfff94604
raw_storage_status: reserved-unpopulated-public-data-object-only
language: en
nuclei: [136pr]
reactions: ["110Pd(30Si,p3n)136Pr", "122Sn(19F,5n)136Pr", "136Ce(p,n)136Pr"]
observables: [level-energy, gamma-energy, spin-parity, relative-gamma-intensity, dco-ratio]
methods: [gamma-gamma-coincidence, angular-distribution, directional-correlation]
tags: [a130, ensdf, level-scheme, source-lineage, version-boundary, day14]
---

# 136Pr：选定2018评价对象

## Bibliographic Record

E. A. McCutchan, *Nuclear Data Sheets for A=136*, NDS152,331–667(2018)，DOI[10.1016/j.nds.2018.10.002](https://doi.org/10.1016/j.nds.2018.10.002)。Crossref200核题名/作者/卷页/年；metadata发表月为9月，dataset版本201810各自保留。实际证据为NNDC公开ENSDF对象，不宣称读完337页质量链论文或取得1996primary。

## Scope and Reading Depth

来源前回忆ensdf136-before-source-recall.md已在查询前冻结；研究截止前已读136059003 reaction全部401行，以及136059001 adopted的global/selectedblocks（770行中部分）。15:37观察到硬截止后只将既有摘录写回，没有继续开来源或做新分析。原始response在tmp/day14-20261014/nndc136，raw槽明示未填、raw树不写。对象获取URL/request/hash在本run nndc136-object-receipt.json；选定line markers如下。

| 对象 | 版本/范围 | 精确text SHA256 |
| --- | --- | --- |
| 136059001 ADOPTED | 201810/cut1-Apr2018；770行，global/selected读取 | cb1ca8660bbf0df17920ec4f366b245cb564d707f116bc1544738fdcfff94604 |
| 136059003 110PD(30SI,P3NG) | 同cut；401行，全文读取；主要1996PE12，含其它legacy反应 | b90fe01705fc98992c49e04b57f829d6d55e469930508da4a98494c553c3922d |

[NNDC query](https://www.nndc.bnl.gov/ensdf/DatasetFetchServlet?nuc=136PR&nsrch=Search&searchType=quick&datasource=ensdf)；text请求POST [dispatcher](https://www.nndc.bnl.gov/ensdf/EnsdfDispatcherServlet)，dbclass=ensdf、page-source=singular、chooseit=ENSDF text format、datasetcheck=136059001,136PR或136059003,136PR。查询仅列ADOPTED、EC decay与110Pd反应，均2018，不能假定包含2025新工作。

## Summary

本对象保留2025以前的Q1旧endpoint及bandH tentative assignment。它使旧版评价与[[lv-2025-136pr-tac-covariant-density-functional]]的逐线crosswalk可核，但不补1996原图/全部方法，不将数据库视为独立新实验，也不裁决263/405顺序为何不同。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N136-1 | 两对象H为201810/cut1-Apr2018；ADOPTED E来自evaluator least-squares，主要Eγ/RI/M从110Pd反应取回。反应Eγunc来自2001PeZY私人通信，J由1996Pe12 multipolarities/角分布/DCO且supported IBM；不能当全部字段都在1996同表直接测量。 | evaluated-field-provenance | direct | 136059001 lines2–23; 136059003 lines2–20 | true |
| N136-2 | Reaction记录125-MeV30Si+110Pd、GASP40Ge/80BGO，并含19F+122Sn和p+136Ce资料。相对2025的152-MeV40Ar+100Mo是不同实验入口；具体独立性与原始切选仍按来源，不以评价对象数计新采集。 | evaluated-experiment-description | direct | 136059003 lines4–11 | true |
| N136-3 | Reaction3998.8(7) J15的G876.1(5) RI3.3(6)、M=D、R=.65(11)接3122.7(5)14+；ADOPTED3998.7(7)(15)接3122.6(5)(14+)，RI重标100且M=D。评价无π，D不等于独立测得E1或M1。 | evaluated-old-endpoint-and-normalization | direct | 136059003 L3998.8/G876.1 lines278–280; 136059001 L3998.7/G876.1 lines569–572 | true |
| N136-4 | Reaction旧H链为3677.7 15(-)→262.9→3414.8 14(-)→404.9→3009.9 13(-)；ADOPTED对应3677.6/3414.7/3009.8，保留同order但J写(15)/(14)/(13)无π。Reactionproposal不可直接覆盖adopted更弱赋值。 | evaluated-versioned-order-and-parity | direct | 136059003 lines228–258; 136059001 L3009.8/L3414.7/L3677.6 | true |
| N136-5 | 旧754.4-keV Q的R(DCO)=.45(10)且注明dipole gated，compiler说与Q inconsistent、perhaps typo。这是评价者解释，当前不改ratio、不宣称1996原文已证错。 | evaluator-comment-and-counter-evidence | mixed | 136059003 G754.4 lines133–136 | true |
| N136-6 | Reaction594.70-keV6+半衰期91(1)ns是多个旧值weighted average，1996Pe12的90(4)ns等另列。该值不属于高能17+或Q1母态；2025图90ns与此评价91ns要按版本/来源保留。 | evaluated-lifetime-provenance | direct | 136059003 L594.70 lines87–94 | true |
| N136-7 | 首条311.7G在第一个L前，原文另称doublet在1996Table1未放置但Fig1画到351.9；不能让parser把首G错挂0level或把编者图表冲突修成已定identity。 | evaluator-placement-boundary | direct | 136059003 lines37–38; lines67–74 | true |
| N136-8 | 1996Pe12对应Petrache等NPA603,50–76 DOI10.1016/0375-9474(96)00107-8，metadata已核；OA无文件、arXiv连接拒绝、Semantic429、Scholar失败、Padua403，未得primary。2025转述/2018评价不能代替原文或认证重排原因。 | primary-readiness-boundary | metadata-and-boundary | Day14 petrache96-metadata/openalex-doi/padua/downloader-boundary receipts | true |

## Competing Interpretations and Limitations

[[lv-2025-136pr-tac-covariant-density-functional]] LV25-26的D5链为3678.4 15+→405.1→3273.3 14+→263.1→3010.2 13+，与N136-4的263/405次序及中间level不同。中心值/版本/拓扑差异是真实记录差异；没有1996primary/新逐门净计数，原因仍unknown，可能的reassignment或transcription都只为待核路线，不能裁决任何一方错误。

Q1旧3998.8→3122.7与2025 5347.8→4472.2不同；数据库截止早于2025，不把滞后的旧版称为独立反证。ADOPTED与reaction共享1996Pe12主线并经编者变更，不计两条独立实验。

## Knowledge Impact and Learning Decision

Decision: revises字段版本和π充分性的认识，supports精确endpoint与顺序crosswalk，limits从最新论文/旧评价直接判旧原文的做法。Durable结果在[[level-scheme-reconstruction]]“136Pr：2018评价与2025接受稿的顺序冲突”，[[136pr]]、[[a130-thesis-evidence-matrix]]回链。没有新计算结果、新τ/B或mode裁决。

## Extracted Pages

- [[136pr]]、[[level-scheme-reconstruction]]、[[a130-thesis-evidence-matrix]]。
- [[lv-2025-136pr-tac-covariant-density-functional]]：直接2025接受稿；共享引用不是独立重测评价本身。

## Self-audit and review boundary

N136-1–8全部needs_review:true，page unreviewed。没有清旧claim标记、设置human-reviewed或改raw。未完成fixed-column通用parser/新χ拟合不算已完成；本页只固化截止前已检查的literalrecords和获取边界。原数据仍缺事件、逐门response/Cov与完整原文。
