---
type: source
title: "NNDC 193Bi 能级与γ记录：2017评价、2019修订和赋值边界"
aliases: [NNDC 193Bi ENSDF evaluation, Basunia A193 2017 selected datasets]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-tables
reading_depth: read
title_original: "193Bi ADOPTED LEVELS, GAMMAS / 165HO(32S,4NG)"
authors: [M. Shamsuzzoha Basunia]
journal: Nuclear Data Sheets
year: 2017
volume: 143
pages: 1-381
doi: 10.1016/j.nds.2017.08.001
data_version: "201709 dataset IDs193083001/193083004; adopted ERR17-Jul-2019; cutoff31-Mar-2017; retrieved2026-10-14"
canonical_source: "https://www.nndc.bnl.gov/ensdf/"
citation_key: Basunia2017A193ENSDF
citation_key_origin: agent-local-online-dataset-label
raw_file: "raw/papers/gpt/day14/nndc-193bi-adopted-2017-2019.ens"
raw_sha256: "c787dea4b406d64712f2eee91867136a3decc8ad8d7029236223362904f065ca"
raw_storage_status: reserved-unpopulated-public-data-object-only
nuclei: [193bi]
reactions: [165Ho-32S-4n]
methods: [level-scheme-reconstruction, gamma-gamma-coincidence, spin-parity-assignment, internal-conversion-analysis]
observables: [level-energy, gamma-energy, relative-intensity, DCO, IPDCO, half-life, conversion-coefficient]
tags: [ensdf, evaluated-data, version, assignment-boundary, source-lineage]
---

# 193Bi：评价对象与原实验的分层

## Bibliographic Record

M. Shamsuzzoha Basunia, “Nuclear Data Sheets for A=193”, *Nuclear Data Sheets*143,1–381(2017), DOI[10.1016/j.nds.2017.08.001](https://doi.org/10.1016/j.nds.2017.08.001)，Crossref核题名/作者/年/卷页。本页实际来源是NNDC当前提供的两份**选定ENSDF对象**，不是宣称读完381页质量链评价论文。

从[NNDC ENSDF](https://www.nndc.bnl.gov/ensdf/)实际表单POST到`/ensdf/DatasetFetchServlet`，参数`nuc=193BI, nsrch=Search, searchType=quick, datasource=ensdf`；选定dataset193083001（ADOPTED）和193083004（165HO reaction）。再POST`/ensdf/EnsdfDispatcherServlet`，参数`dbclass=ensdf, page-source=singular, chooseit=ENSDF text format, datasetcheck=193083001,193BI`或`193083004,193BI`。旧getdataset.jsp返回404；IAEA接口403 HTML，没有用失败页面填数据。

原始HTTP response为HTML `<pre>` 包装；对应response SHA256分别为`4565ae1f3359385fc1041040e98d60f37ec0f6292d0a506ecde2b360229720a2`与`77fecc5ef6372e3654511fcbbf881d70b4a71335b0bc6d6964d8f7d05d2f42de`。抽取ENSDF text对象分别827/819行，SHA256为frontmatter值与`705abb789fcd4bac580b871e4410e9b39715a3fd597b8cf6ad69103c0c6dc0fa`。

保持raw不变：raw_file为未来归档的未填保留槽。当前实际文本在`tmp/day14-20261014/nndc-193bi-adopted.ens`和`nndc-193bi-ho32s.ens`；临时副本失效需重取并核版本/hash。关键行、方法、变量自由度和证据边界已在本页及[[level-scheme-reconstruction]]固化；本地临时路径不是唯一知识副本。citation_key是本Wiki在线对象标识，不表示已修改Zotero/BibTeX。

## Scope and Reading Depth

- 实际范围：对象header/version/cutoff/globalcomments、selected五level七γ及其continuation、352.3和393/394弱线comments、153-ns bandhead、SD X/1836候选、selectedCC与RI；[references页](https://www.nndc.bnl.gov/ensdf/getrefs.jsp?recid=193083001&dsid=ADOPTED%20LEVELS%2C%20GAMMAS)核2004NI06/2015HE27。
- 本页`read`指这个selected data-object audit；未通读质量链381页、所有193Bi反应/衰变原论文或全部弱线，不独立重新评定所有Jπ。
- 数据对象直接可核验，但多数γ数值/赋值采用2015He27；评价者处理与primary measurement不能合并成“第二实验”。

## Paper Question and Scientific Motivation

核对从原图/表到evaluated level/γ records时，精度、scale、normalization、multipolarity label和source dependency究竟发生什么变化。尤其检验原表tentative(E2)与shared polarization的矛盾是否被评估保留。

## Summary

选定公开ENSDF对象支持七条已发表γ的identity crosswalk，并提供评价者的energy/RI处理及有前提的BrIcc CC。它同时保留393/394仅Q、352.3图表spin矛盾和未知SD X。相对精度、版本和派生量有增量，实验独立性、完整δ/branch/parentτ不因数据库出现而自动补齐。

## Method and Design Logic

记录对象ID、文本hash、2017cutoff及2019erratum；按固定列读取L/G记录，保留continuation/comments、括号与X，不把未知表达式数值化。先按source-identifiedγenergy匹配七条唯一行，再比较reaction/ADOPTED字段；不把nearest energy matching当作新placement证明。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| N193-1 | 两对象header为201709、NDS143,1(2017)、cutoff31-Mar-2017；ADOPTED另有17-Jul-2019 ERR，纠正305-keV level半衰期为3.20(14)s。查询日期2026不是新的数据cutoff。 | evaluated-data | direct | ADOPTED header H records；reaction header H records | true |
| N193-2 | reaction globalcomments明确Eγ/RI来自2015He27，认为2015结果以更好统计supersede2004Ni06/2003NiZZ/2001Ni04；这是评价者的version选择，不证明identical event list或新增独立实验。 | evaluated-source-lineage | direct | reaction global c records at lines19–31 | true |
| N193-3 | reaction cG E说明评价者将约0.3-keV statistical uncertainty按quadrature加入；cL E说用γenergy least-squares fit并holding305-keV level fixed。没有给出完整joint calibration/level covariance。 | evaluation-method | direct | reaction global cG E / cL E records at lines25–31 /47–48 | true |
| N193-4 | selectedlevels为605.53(18)、928.93(21)、1228.13(21)、1555.30(25)、1875.1(3)keV；七条γ中心能量与原2015表相同，ENSDF对它们给0.3keV打印误差。图中整数label不应当作独立高精度观测。 | evaluated-data | direct | ADOPTED L605.53 / L928.93 / L1228.13 / L1555.30 / L1875.1 and attached G records | true |
| N193-5 | 393.4/394.0两行M只给Q；reaction comments保留共用DCO/POL、negativePOL与placement-implied(E2)不一致、cascade顺序未established。因此Q只能表示quadrupole，不能自动写成E2。 | evaluated-assignment-boundary | direct | reaction G393.4 cG M / cG E；reaction G394.0 cG M / cG E | true |
| N193-6 | reaction G352.3 multipolarity留空；comment指出Table I M1与Figure2(15/2−)→(11/2−)不一致，并记录作者后来建议无multipolarity assignment的公开compiler说明。该说明不是本任务取得的新private communication或human-review事件。 | evaluated-assignment-boundary | direct | reaction L1609.9 / G352.3 and cG M records at lines262–270 | true |
| N193-7 | ADOPTED的CC说明为BrIcc v2.3a/30-Jun-2013 Frozen Orbitals calculation；299.2/622.4、327.4/626.2、319.8/646.9分别列CC0.467/0.0186、0.366/0.0183、0.390/0.01706。这些按所列multipolarity计算，不是逐线测得δ或ICC。 | model-result | direct | ADOPTED DG CC header；G299.2 / G622.4 / G327.4 / G626.2 / G319.8 / G646.9 | true |
| N193-8 | L605.53给153(10)ns半衰期并引用2004Ni06；reaction cL T写From604.7γ(t)。附注评价者2006Ac01解释该γ强度难从prompt谱可靠取得，且RITU约1μs飞行使大部分该活动在飞行中衰变。原Ni04全文仍未取得，不能把compiler摘要当原完整方法。 | evaluated-lifetime-dependency | direct | ADOPTED L605.53 cL T；reaction L605.53 cL T / G604.7 DG RI records at lines108–118 | true |
| N193-9 | SD14个level仍以X或number+X表达；1836-keV候选在reaction开头unplacedγ区，确认连接仍不足。评价者holding X fixed是相对调整的坐标选择，不是测得absolute X。 | evaluated-data-boundary | direct | ADOPTED L X through L4800.6+X；reaction unplaced G1836 / BAND(G) comments | true |
| N193-10 | reaction的selectedRI相对原Table I七条数值均缩放0.1；ADOPTED selected母态block的strongM1 line为100，E2行46.9/52.0/86。同母态ratio只受圆整微调，跨母态RI不能直接拼接population/flow。 | evaluated-data | direct | reaction G323.4 / G299.2 / G327.4 / G319.8 / G622.4 / G626.2 / G646.9；ADOPTED L1228.13 / L1555.30 / L1875.1 γ blocks | true |

## Selected Records and Reasoning Chain

| γkeV | evaluated母态keV/Jπ | reaction RI | ADOPTED RI | adopted M / CC | 对原图/表的使用边界 |
|---|---|---:|---:|---|---|
|323.4|928.93(21),15/2+|100.0(57)|100|M1 /0.378|低能referenceRI，非absolutebranch；原表标度1000(57)。|
|299.2|1228.13(21),17/2+|25.8(8)|100(3)|M1 /0.467|同母态photon ratio；CC有pure-M1计算前提。|
|327.4|1555.30(25),19/2+|19.6(6)|100(3)|M1 /0.366|不把纸面1556当fixed exactlevel。|
|319.8|1875.1(3),21/2+|12.5(4)|100(4)|M1 /0.390|原表Other transitions、原图约320。|
|622.4|1228.13(21),17/2+|12.1(5)|46.9(19)|E2 /0.0186|与299.2→323.4互斥；非新的coincidence实验。|
|626.2|1555.30(25),19/2+|10.2(4)|52.0(20)|E2 /0.0183|母态block重标；不跨mother求population。|
|646.9|1875.1(3),21/2+|10.8(4)|86(4)|E2 /0.01706|0.3-keV是评价文本打印误差，不是jointΣ。|

五level七边的identity/energy crosswalk保留raw2015行及evaluated行；新增精度来自评价者调整，不是另一束流实验。固定列reader与79项schema/identity/scale/weak-line/SD/条件branch检查见[day14_ensdf_crosswalk.py](../../system/scripts/day14_ensdf_crosswalk.py)和[结果回执](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/ensdf-crosswalk.json)。

## Competing Interpretations and Limitations

- 352.3-keV在原Table I为(13/2−)→(11/2−)、M1，Figure2 p.9的1610-keVlabel为15/2−。若取后一ΔI=2，single-photon M1被triangle排除；取表中ΔI=1则M1允许。不能只凭negativePOL选择哪个spin是真值；评价记录留空M，本任务保留冲突，见[[herzan-2015-193bi-spectroscopy]] HE15-15。
- shared393/394两行的Q/negativePOL与tentative(E2)问题不通过重新求energy sum解决；eval与原文共享数据，也不能充当independent polarization measurement。
- ICC是模型输出，Jπ还是assignment，153-ns仍引用旧测量。α、全branches、δ、parentτ和covariance不能从“数据库有数值”自动补齐。
- SD X和未确认link保持原边界。此source不裁决shape/wobbling/chirality，不认为网站当前日期意味着所有193Bi新研究已纳入。

## Analytical Reconstruction

在“只有两条已报告channel、pure M1/E2、采用上述BrIcc CC”的条件模型中，`pγ,j=Iγ,j / Σ Iγ,k(1+αk)`。三个mother的M1photon fractions约0.5142/0.5276/0.4416，包含conversion的conditional total M1 fractions约0.7543/0.7206/0.6138；它们与只在γ中归一的0.6807/0.6579/0.5376不同。没有δ、unseenbranch completeness或parentτ，此算术不能当作已测totalbranch或absolute B，完整推导在[[level-scheme-reconstruction]]。

## Knowledge Impact and Learning Decision

- `supports`七条source-identified能量/母态crosswalk和评价者quadrature处理；`limits`用整数labels、shared-data重复计数或数据库CC直接认证δ/absolute strength。
- `revises`weak393/394的工作标签应保留Q；352.3的spin/multipolarity冲突必须单列，不能默认原图/表全部一致。原primarysource不被静默重写成评价版本。
- 本source是方法性data-object对照；selected知识由方法/source/matrix承接，未扩展成全193Bi核素或所有band摄入。review_status保持unreviewed。

## Agent self-audit triage

- P0（科学，已self-audit）：Q≠E2、352.3图/表冲突、SD X不可当零、ICC≠测δ、evaluation非independent experiment；均保留needs_review=true与具体locator。不是未隔离技术hard P0。
- P1：来源身份/version/hash及固定列解码、0.1RI缩放和parent重标已核；未给jointΣ和完整Ni04方法。raw槽未填，按当前保护约定不归档；网站变化需重取版本。
- P2：互链至[[herzan-2015-193bi-spectroscopy]]、[[level-scheme-reconstruction]]、[[spin-parity-assignment]]、[[internal-conversion-analysis]]和[[a130-thesis-evidence-matrix]]。P3：未触发human-review或纸稿admission。

## Extracted Pages

- [[level-scheme-reconstruction]]：version/精度/normalization与weak-line判例，以及条件ICC/photon-fraction练习。
- [[herzan-2015-193bi-spectroscopy]]：保留primary原标签、HE15-15直接图表冲突与evaluated comparison。
- [[a130-thesis-evidence-matrix]] / [知识入口](../index.md)：方法对照及导航；未制作全核素/所有band pages。
