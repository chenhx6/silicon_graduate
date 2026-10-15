---
type: source
title: "67Ga：公开ENSDF的multipolarity、寿命与branch来源"
aliases: [NNDC 67Ga ENSDF 2005, 67Ga evaluated gamma records, 67Ga 958-keV reference inputs]
created: 2026-10-15
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-object
reading_depth: read
data_version: "base200512/cut1-Apr-2005; alphaERR6-Jul-2007; adoptedQ2012; retrieved2026-10-15"
title_original: "Nuclear Data Sheets for A = 67"
authors: [Huo Junde, Huang Xiaolong, J. K. Tuli]
journal: Nuclear Data Sheets
year: 2005
volume: 106
pages: 159--250
doi: 10.1016/j.nds.2005.10.006
canonical_source: "NNDC:ENSDF:67GA:67031001,67031003,67031005,67031006"
citation_key: nndc_2005_67ga_selected_ensdf
raw_file: "raw/data/gpt/day14/nndc-2005-67ga-adopted.ens"
raw_sha256: a8ce3f5d6170357c67f6e750b74a1bb82eba0db723fb4d9507866f523937dcf1
raw_storage_status: reserved-unpopulated-public-data-object-only
language: en
nuclei: [67ga]
reactions: ["57Fe(12C,pn)67Ga", "64Zn(alpha,p)67Ga", "53Cr(16O,pn)67Ga", "12C(58Ni,3p)67Ga"]
observables: [level-energy, gamma-energy, multipole-mixing-ratio, lifetime, relative-gamma-intensity]
methods: [angular-distribution, linear-polarization, recoil-distance-doppler-shift]
tags: [ensdf, level-scheme, source-lineage, lifetime, branching, conversion, day14]
---

# 67Ga：选定公开数据对象的输入契约

## Bibliographic Record

Huo Junde, Huang Xiaolong and J. K. Tuli, *Nuclear Data Sheets*106,159–250(2005)，DOI[10.1016/j.nds.2005.10.006](https://doi.org/10.1016/j.nds.2005.10.006)；Crossref200核题名、三作者、年/月、卷页。本页实际证据是NNDC当前提供的四份选定ENSDF对象，未宣称通读92页质量链评价论文。

## Scope and Reading Depth

总体来源前primed回忆先冻结，首次查询后选择ADOPTED67031001、57Fe(12C,pnγ)67031005、64Zn/53Cr67031006；按ADOPTED的O/Q flags再冻结补读预测并取12C(58Ni,3pγ)67031003。Fe全文67行、alpha全文178行、Ni全文170行已读；ADOPTED762行只读globalcomments、3032/2074/2862与3578/3856相关L/G/continuation，不审全部levels。新XUNDL2024/2026只在目录发现，未研究其科学内容。

从[NNDC ENSDF](https://www.nndc.bnl.gov/ensdf/) POST DatasetFetchServlet，`nuc=67GA,nsrch=Search,searchType=quick,datasource=ensdf`；再POST EnsdfDispatcherServlet，`dbclass=ensdf,page-source=singular,chooseit=ENSDF text format,datasetcheck=<record>,67GA`。实际HTML pre抽取对象identity/hash核验，未以网页目录代替数据读取。

| record / scope | extracted text SHA256 | revision boundary |
| --- | --- | --- |
| 67031001 ADOPTED | a8ce3f5d6170357c67f6e750b74a1bb82eba0db723fb4d9507866f523937dcf1 | header200512/05NDS，cut1-Apr-2005；当前Q行含2012WA38，非原2005不可变blob |
| 67031005 Fe12C | bcb6f6fc977604c522e572166c50a196f761649c25ad054f2928a383f742815a | 同base，header1979ZO01 |
| 67031006 alpha/16O | efe6ea722b9898f7cba4d42d1108dde9e3853cf8a28d12525d699cddb4603a3b | H记录6-Jul-2007 typos correction，header1978AL32/1977AL35 |
| 67031003 Ni58 | b3e280d6da6b1093bf899c832d4a07430fdb352d8d4675adbb8807dbf25d3ec8 | 同base，header1999DA10，E=261MeV/NORDBALL |

raw_file是未来归档的未填保留槽，raw树保持不变；当前可重算文本在`tmp/day14-20261014/nndc67/`，objects/query/reference receipts在DAY14 run。核心字段、原始marker与输入边界固化本页，不把tmp/outputs当长期唯一知识。重新获取须核record/header/hash并记录变化。

## Summary

同一条958γ在不同对象中复用不同层的来源：M/δ与parent半衰期主要追到1978Al32的alpha/16O数据；Fe reaction将M/MR从adopted取回；相对RI和weak168.8来自1999Da10/NORDBALL。多个对象不是多个独立测量。E2(+M3)与δ=−0.00(1)支持nominal近pure-E2处理，保留有限误差与模型约定。parent的4.5ps是T1/2，两个feeder的寿命不可借用。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N67-1 | 四个对象base为05NDS/200512、cut1-Apr-2005；alpha显式H2007修正，ADOPTED有2012Q更新。本页是当前选定对象audit，不是全文质量链或新实验。 | object-identity-and-version | direct | ENSDF67031001 header/Q；67031006 H record | true |
| N67-2 | ADOPTED parent3031.77(6)keV、13/2+，daughter2073.755(25)keV、9/2+；G958.01(5)标E2(+M3)，MR字面−0.00(1)，不是exactδ=0。 | evaluated-record | direct | ENSDF67031001 L3031.77/G958.01；L2073.755 | true |
| N67-3 | Fe12C对象cG M,MR来自adopted；G958在adopted FLAG=DQ，D的M/MR指alpha/16O数据，alpha本线A flag指1978Al32；parent时间C/R为该source的RDM。该round-trip不是第二份独立δ/τ。 | source-lineage | direct | ENSDF67031005 cG M,MR；67031001 FLAG=DQ/CIT；67031006 M(A),MR(A)/T(R) | true |
| N67-4 | Fe RI(958)=58.2(.9)，normalizer是I359+I1202=100；ADOPTED RI958=100(9)、weak168.8(4)的RI=.2(1)，O/Q指Ni58 source。958的CC空白、weak M/CC空白不补0；relative photon不是全部decays份额。 | normalization-and-inventory | direct | ENSDF67031005 cG RI/G958.01；67031001 G168.8/G958.01、E(O,P),RI(O,Q) | true |
| N67-5 | ADOPTED parent3032 T1/2=4.5(4)ps、3578为.16(4)ns、3856为11(2)ps，alpha RDM来源保留。除ln2得mean6.492/230.831/15.870ps为任务换算，不是三条新测量或同一parent。 | evaluated-time-and-task-conversion | mixed | ENSDF67031001 L3031.77/L3577.95/L3855.99；67031006 RDM markers | true |
| N67-6 | G958 continuation印BE2W=9.6(9)，属于评价派生strength。输入CC/完整unseen inventory/fitCov未给，不能把条件gamma-only重算称为重测或重放评价算法。 | evaluated-derived-strength-and-boundary | mixed | ENSDF67031001 G958.01 / BE2W=9.6 9 | true |
| N67-7 | Ni对象G958与G554.4同报DCO1.45(7)；ADOPTED分别E2(+M3)/E1(+M2)。同parent2073.2的另一G871.3报DCO.77(3)。对象未给具体gate/reference/角响应，不以数值alone指定E2或把差异仅归因ΔJ。 | observed-ratio-and-assignment-boundary | mixed | ENSDF67031003 G958.0/G554.4/G871.3 DCO comments；67031001 corresponding M | true |
| N67-8 | alpha对2862级保留angular/polarization曾得11/2−，1343与1353未完全分辨“may explain”；采用11/2+来自Fe反应。评价者的污染解释不是本run已证明的错误因果。 | evaluator-comment-and-counter-evidence | direct | ENSDF67031006 L2862.4 comments；67031005 L2862.43 | true |
| N67-9 | 为核1999DA10的DCO定义，legalOA无文件、publisherPDF403HTML、officialHarvestAPI401JSON、repo metadata无OAurl；没有取得primary。由dataobjects不能补gates/ref/angles/producerCov，后续设计仅chosen model，非NORDBALL重放。 | primary-readiness-boundary | metadata-and-boundary | Day14 Danko99 DOI10.1103/PhysRevC.59.1956 acquisition receipts；N67-7 missinggate scope | true |

## Selected records and source locators

以下来自ADOPTED，本节marker均与上表matching；前五/后两行是L/G records，BE2W是continuation。T字段为half-life：

```text
 67GA  L 2073.755  259/2+
 67GA  L 2862.45   1011/2+             0.87 PS   28
 67GA  L 3031.77   6 13/2+             4.5 PS    4
 67GA2 L FLAG=CIT
 67GA  G     168.8  4    0.2  1                                             O
 67GA  G 958.01    5 100      9E2(+M3)   -0.00   1
 67GA3 G FLAG=DQ
 67GAB G BE2W=9.6 9
 67GA  L 3577.95   6 15/2+             0.16 NS   4
 67GA  L 3855.99   7 17/2+             11 PS     2
```

N67-3的来源规则：`cG M(D),MR(D)`来自64Zn(alpha,pγ)/53Cr(16O,pnγ)，`cG E(O,P),RI(O,Q)`来自12C(58Ni,3pγ)；Fe对象明确`cG M,MR From adopted gammas`，不是重新测得所有adopted输入。

Refs metadata核验：[Fe references](https://www.nndc.bnl.gov/ensdf/getrefs.jsp?recid=67031005&dsid=57FE%2812C%2CPNG%29)的1979ZO01为Zobel79/NPA316,165/[DOI](https://doi.org/10.1016/0375-9474(79)90678-X)；[alpha references](https://www.nndc.bnl.gov/ensdf/getrefs.jsp?recid=67031006&dsid=64ZN%28A%2CPG%29%2C%2053CR%2816O%2CPNG%29)的1978AL32为Al-Naser等J.Phys.G4,1611/[DOI](https://doi.org/10.1088/0305-4616/4/10/011)；[Ni references](https://www.nndc.bnl.gov/ensdf/getrefs.jsp?recid=67031003&dsid=12C%2858NI%2C3PG%29)的1999DA10为Danko等PRC59,1956/[DOI](https://doi.org/10.1103/PhysRevC.59.1956)。这些是references/metadata，不宣称取得三篇primary全文或actual unshared raw files。Fe对象E32–44MeV与NSR摘要32–64MeV的范围也保持各自scope。

## Theory / conditional cross-check

[[level-scheme-reconstruction]]“67Ga：跨对象的parent与强度输入核验”保存38项fixed-column/hash/finiteMR/RI/time/rate控制。基于[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1的rate/RME约定与[[high-spin-lifetime-strength-deformation]]既有现代常数转换，声明zeroIC、only两条observedγ、E2/M3截断与δ=0时算B(E2)=9.61853WU；源9.6(9)保持原值。数值相容不验证库存、feeding、IC或评价者处理。

## Competing Interpretations and Limitations

- 小photon RI不保证total branch小；weak168.8的M/ICC及unseen ledger未闭合。
- 近零δ的quotederror不代表无M3，更不能自动转为angular-response的δ²误差；相干干涉可一阶。
- 单独DCO数值不足指定E/M或stretched sequence，缺exact gates/geometry/reference则只保留源ratio。
- 2862的未分峰/π冲突必须保持；多反应引用并不修复peak identity。
- 原始angular/spectrum/response、fitCov、完整stopping/feeding、primary1978/79/99没有提供；实验L4重放not-ready。

## Project Relation

这是[[a130-thesis-evidence-matrix]]所需的可迁移方法例：谱峰身份、Jπ、M/δ、parentτ、RI normalization与B输入分别回源。它不给A≈130新的观测或模式裁决。

## Extracted Pages

- [[level-scheme-reconstruction]]：真实source records/亲本和强度输入契约。
- [[angular-distribution]]：reference purity的有限误差与DCO阈值边界。
- [[high-spin-lifetime-strength-deformation]]：rate/branch/IC/general covariance的既有定义。

## Self-audit and review boundary

全部N67-1–8 needs_review:true，Codex完成object/locator/条件数学自审，无新增人审。评价记录、评价者解释、标准理论和本任务重算分开；没有重估真ρ/δ/τ、生成真实counts或宣称原作者出错。Day14持续，Day15仅partial无学分。


### 1999 primary的数据边界与设计续路

N67-7的相同ratio现象需要exacttarget/reference gates、角度/探测对、归一/效率与producerCov。Danko等PRC59,1956的原文在本run未取到：合法OA未找到对象、publiccitationPDF不完整验证、直接HTTPS403返回HTML、官方HarvestAPI401、OpenAlex0/SemanticScholar匹配metadata但无OA地址。普通APSdefaultlicense不等OA；没有更改认证、处理challenge、启用hostGUI或反复请求受阻入口，metadata/失败responsehash保留。

故停止该获取分支，不虚构正文页码、gate定义或实际detectorangles。[[angular-correlation]]“67Ga真实序列的门条件设计与single-marginal盲区”使用actualstates加**声明的**40°/90°、参考路径及purelimits，检查模型是否能表示source1.45、unknownnormalizer与单γ校准何时不足。这是source-groundedL2设计，不能用于裁决真实E1/实验ρ、声称原数据冲突或补actualL4缺口。N67-9 true，其余旧claim/review保持。
