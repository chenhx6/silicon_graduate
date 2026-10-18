---
type: source
title: "104Mo公开ENSDF：gamma-band目标身份、旧M1标签与评价时层"
aliases: [NNDC104Mo 2007 selected records, Mo104 gamma-band reference crosswalk]
created: 2026-10-18
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-object
reading_depth: skimmed
data_version: "base200709/cut30-Mar-2007; adoptedERR14-Dec-2007; adoptedQ2012; retrieved2026-10-18"
title_original: "Nuclear Data Sheets for A = 104"
authors: [Jean Blachot]
journal: Nuclear Data Sheets
year: 2007
volume: 108
pages: 2035--2172
doi: "10.1016/j.nds.2007.09.001"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "NNDC:ENSDF:104MO:104042001,104042005,104042004"
source_url: "https://www.nndc.bnl.gov/ensdf/"
raw_file: "raw/data/gpt/day16-20261018/nndc104mo-adopted-303ccb20a779.ens"
raw_sha256: "303ccb20a7798348aed1ab93467d7fb73357dd4ac39ce0b2ed6d84309475022e"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [104Mo]
reactions: [252Cf-SF, 248Cm-SF]
experiments: [Gammasphere, EUROGAM]
methods: [ENSDF-fixed-column, gamma-gamma-coincidence, source-lineage]
observables: [level-energy, gamma-energy, multipolarity, multipole-mixing-ratio, half-life]
tags: [evaluation-version, gamma-band, reference-identity, shared-data]
---

# 104Mo：旧评价标签不替后来混合比分支选根

## Bibliographic Record

JeanBlachot，*Nuclear Data Sheets*108,2035–2172(2007)，DOI[10.1016/j.nds.2007.09.001](https://doi.org/10.1016/j.nds.2007.09.001)。原ENSDFH记录与Crossref的题名/作者/卷页/2007year相符；本页实际依据为NNDC选定对象，不声称读完138页masschain论文。

NNDC首页初始化session，再POST`DatasetFetchServlet`的`nuc=104MO,nsrch=Search,searchType=quick,datasource=ensdf`；选定`EnsdfDispatcherServlet`的`dbclass=ensdf,page-source=singular,chooseit=ENSDF text format,datasetcheck=<ID>,104MO`，抽HTMLpre原文。检索时间/下载状态不是科学版本日期。

| record | scope与实际阅读 | 原对象textSHA256 |
| --- | --- | --- |
| 104042001 adopted | 325行，仅global/header/所选target/ref/feeder与相关continuation；不是全数据精读 | 303ccb20a7798348aed1ab93467d7fb73357dd4ac39ce0b2ed6d84309475022e |
| 104042005252Cf | 201行全部主线/注释；选定target/ref/feeding字段深核 | 563aa499c2a6d802790a8c217264cc3bba7c307513f402c4c1914058c3038245 |
| 104042004248Cm | 96行全部主线/注释；目标/原来源规则与空fields | d00045878869edafeb02a3e76e5c0928a4565ff1571ac5dbd679735227e4c3a6 |

actualsnapshots在repo`tmp/day16-mo104-evaluation/`，raw_file为未填归档槽，raw树/Bib不改；关键原行/locator/hash在本页持久保存。所有对象base为200709/cut30-Mar-2007，adopted有14-Dec-2007ERR和2012Q行，**不是2018EL18的新评价**。

## Scope and Reading Depth

本页只覆盖列明的三个在线数据对象及selected parent/reference；Cf201行和Cm96行已读全部主线，adopted325行只定向global与所选记录，wholecollection状态skimmed。未读138页NDS全文、Gu96/Jones06 primary、EL18实际峰门与协方差，不把固定栏核验当原实验重分析。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N104-1 | 三选定对象base200709/cut30-Mar-2007；adopted2007ERR只说明修typos，2012Q字段与γlevel数据分层。评价早于EL18，不可据其未列2018δ称后者已独立确认/已被拒。 | object-version-boundary | direct-object | 104042001 header/H/Q lines2–7；104042004/005 H | true |
| N104-2 | adoptedB=GAMMABAND：L1028.35/3+的G836.3/M1/MR空，候选末态L192.19/2+；Cf对象L1027.9/3+/B给G835.5，CmL1028.0/3+/B给G835.8，后两M/MR均空。三energy层保留，不平均/不把它们无记录替入EL18没列energy的表行。 | target-band-and-field-identity | direct-object | 104042001 L1028.35/G836.3/L192.19；104042005 L1027.9/G835.5；104042004 L1028.0/G835.8 | true |
| N104-3 | adopted全局M规则称“From DCO in248CmSFdecay”，但实际所取96行Cm对象只给Gu96/EUROGAM45台与gamma/RI，没target-specificDCO/R/gate/angles/MR。空MR不能补δ0，globalM来源规则也不是本run重放独立DCO measurement。 | multipolarity-provenance-and-readiness | direct-and-boundary-audit | 104042001 cG M line10；104042004 header/global/G835.8 | true |
| N104-4 | reference为adoptedG192.2/E2及CfG192.4/CmG192.0，均对应各自2+→0+记录，MR空。adoptedT1/2=.97(.08)ns除ln2得1.399414(.115416)ns，与EL18Table1tau1.40(.12)打印相容；只是calibration输入身份换算，不是新寿命测量/新课程卡。 | matched-reference-and-time-definition | direct-and-task-conversion | 104042001 L192.19/G192.2；104042005 L192.4/G192.4；EL18Table1 | true |
| N104-5 | Cf1583.4/4+→1027.9/3+的555.5和2060.8/(4−)→1583.4的477.4，可作为EL18额外556/478整数gate的结构候选。原peakcalibration/实际gateledger未给，另200*/331*为partnergate，不因此宣称exactgate/conditionρ已匹配。 | feeder-crosswalk-and-selection-boundary | direct-and-provisional-map | 104042005 L1583.4/G555.5、L2060.8/G477.4；EL18Table2target extra | true |
| N104-6 | Cf对象以2006Jo05/同组2003Ha49/2001Ya06为默认E/level数据，所述Gammasphere102台不同于EL18写101working，exact同events未认证；Cm对象主要Gu96/EUROGAM45台。多个paper与evaluation对象按引用关系分层，不计独立EL18δ实测。 | acquisition-and-processing-lineage | direct-object | 104042005 globalcomments lines4–22；104042004 lines4–6；EL18PDF2 | true |
| N104-7 | Cm标题对象的T来源写2002Sm10，NNDCrefs又明确其为252Cf/SAPHIR-Euroball differentialplunger；不可把Cm对象中的这个companion时间当另一份Cm寿命实验。Ref1996Gu04准确DOI10.1103/PhysRevC.53.1191，只得metadata未得body，不补其DCO定义。 | companion-source-independence | direct-object-and-refmetadata | 104042004 cL T；NNDCgetrefs recid104042004；Ref2002Sm10/1996Gu04 | true |

## Selected Records and Exact Locators

原固定栏节选如下，行尾padding在此省略，不由Markdown片段重建原hash：

```text
104MO cG M$From DCO in {+248}Cm SF decay
104MO  L     192.19 92+                0.97 NS   8                          A
104MO  G 192.2     1 100       E2                      0.12
104MO  L    1028.3512 3+                                                    B
104MO  G 836.3     1 100     10 M1

104MO  L 192.4     2  2+               0.97 NS   8                          A
104MO  G 192.4
104MO  L 1027.9     3 3+                                                    B
104MO  G 835.5

104MO  L     1028.0  3+                                                     B
104MO  G      467.4        11 1
104MO  G      835.8        89 1
```

GammaMR在42–49列/DMR50–55、CC56–62按[[tuli-2001-ensdf-format-manual]]读；adoptedG192.2的.12是CCtotal，不是δ或一次measuredconversion。adoptedtarget能差1028.35−836.3−192.19=−.14keV，Cf1027.9−835.5−192.4约0；前者level是LS结果/γ带各自error，不能为使其闭合改原值，后者闭合也不证明已匹配2018peakgate。

## Summary

本页给EL18表中缺targetenergy的行以可追溯的**band/spin结构候选**，同时显示2007采用M1标签与2018作者的大E2支解释之间存在需追primary的冲突信号。旧MR为空并非独立δ=0测量，时间先后也不单独裁决真伪；两方原文字/版本均保留。

## Competing Interpretations and Limitations

- 旧adoptedM1标签不应被误当genericrealbranchδ=0精确输入；新EL18大δ/小δ/跨pure点的允许域也不能靠旧标签自动排除。
- 网络retrievedcurrent文件仍base2007，不可宣传为2026/2018重新评价。Counterevidence的观测强度要回具体primary/gate/response，evaluationtitle不能补齐它们。
- 1996Gu04/2006Jo05/原1972angularprimary与实际EL18/Goodinproducer尚未原读；不能据NNDCSummary单独给实验错误归因。
- 这里只作time/identity换算，不开展下一卡RDDS/DSAM研究，不重复计Day16或授Day18学分。

## Quantitative Exercise and Reproducibility

[冻结crosswalkinput](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/mo104-crosswalk-input.json)与[原创固定栏/图层审计](../../system/scripts/day16_mo104_reference_crosswalk.py)/[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/mo104-crosswalk-audit.json)核hash、parent/γ/B、blankMR、Mlabel/cutoff、time转换与feeders。adopted325行只定向，Cf201/Cm96读到全文主线；不是masschain全文/实验新fit。

## Knowledge Impact and Learning Decision

`supports`先原行/parent/gate匹配再解释δ；`limits`用旧evaluationlabel关闭新branch、对象标题当采集身份、空MR当0。`revises`“onlinecurrent=最新实验”与把calibrationtau当另一独立测量的直觉。所有claims true，pageunreviewed，不改任何旧人审。

## Extracted Pages

- [[eldridge-2018-gamma-band-mixing-ratios]]：表行identity候选与旧M1/新mixed解释边界。
- [[dco-pdco-ambiguity-worksheet]]、[[angular-correlation]]：旧标签/门/field/version与actualproducer区别。
- [[tuli-2001-ensdf-format-manual]]：MR/CC/unknown字段原规则。
