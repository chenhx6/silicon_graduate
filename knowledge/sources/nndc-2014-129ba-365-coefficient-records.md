---
type: source
title: "NNDC 129Ba 365-keV记录：角系数、偏振、DCO与假定混合比的谱系"
aliases: [NNDC 129Ba 365 reference records, ENSDF129056001129056013]
created: 2026-10-17
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-tables
reading_depth: read
authors: [Janos Timar, Zoltan Elekes, Balraj Singh]
title_original: "129BA ADOPTED LEVELS, GAMMAS / 120SN(12C,3NG),116CD(18O,5NG)"
journal: Nuclear Data Sheets
year: 2014
volume: 121
pages: 143-394
doi: "10.1016/j.nds.2014.09.002"
citation_key: TimarElekesSingh2014A129ENSDF
citation_key_origin: agent-local-online-dataset-label
canonical_source: "NNDC ENSDF129BA records129056001,129056013; version201408"
data_version: "headers201408/14NDS; cutoff31-May-2014; retrieved17-Oct-2026"
raw_file: "raw/papers/gpt/day15-20261016/nndc-129ba-129056001-201408-15d8e353eb23.ens"
raw_sha256: "15d8e353eb23d55847dc0d0127591fd2fb23e6da63ae98146747aecb233f65f6"
raw_storage_status: archived-agent-managed-public-data-object
nuclei: [129ba]
reactions: [120Sn-12C-3n, 116Cd-18O-5n]
observables: [angular-distribution-coefficient, linear-polarization, DCO, relative-intensity, conversion-coefficient]
methods: [level-scheme-reconstruction, source-lineage-audit]
tags: [ensdf, a130, mixing-ratio, calibration, source-dependence]
---

# 129Ba365keV：多种观测不等于可随意合并

## Bibliographic Record

J. Timar、Z. Elekes、B. Singh，*Nuclear Data Sheets* **121**,143–394(2014)，DOI[10.1016/j.nds.2014.09.002](https://doi.org/10.1016/j.nds.2014.09.002)，Crossref核题名/作者/卷页。实际证据为NNDC当前提供的两个选定ENSDF对象，不声称通读252页评价或所有129Ba反应。

在[NNDC ENSDF](https://www.nndc.bnl.gov/ensdf/) POST `DatasetFetchServlet(nuc=129BA,nsrch=Search,searchType=quick,datasource=ensdf)`选129056001/013，再以`EnsdfDispatcherServlet`的`chooseit=ENSDF text format`取text。对象为201408/14NDS、cutoff31-May-2014；2026是查询时间，不是纳入2024reanalysis的cutoff。

| object | canonical raw | exacttext SHA-256 |
| --- | --- | --- |
| 129056001 ADOPTED，934lines | `raw/papers/gpt/day15-20261016/nndc-129ba-129056001-201408-15d8e353eb23.ens` | `15d8e353eb23d55847dc0d0127591fd2fb23e6da63ae98146747aecb233f65f6` |
| 129056013 HI reactions，555lines | `raw/papers/gpt/day15-20261016/nndc-129ba-129056013-201408-09194d4feed3.ens` | `09194d4feed3bbda013c551ce5ba9ecf55a25799e8c46ec22f23685df1c1ef19` |

官方HTTP HTML wrapper的hash分别为`3f4f3bd8125a2c5c05316d8a23df8c228e96d7cc4c9afe5c2bb4214eec78d067`、`c5837f017e5afba80d8505a676f9fd6125e42b6058e687e1ab3217d115de27ce`。raw为新agent-managed公开数据，原始text不修补、不覆盖旧材料、从不stage。

## Scope and Reading Depth

实际读两对象header/globalcomments、target L643.6/G364.7/FL278.81、461.6同母态branch、相邻reference用于防误认，以及references页1977GI02/1978GI04/1992BY03/1992BY02条目。未逐行审核全部934/555行物理内容，未取得两Gizon primary bodies或actualefficiency/gate/Cov。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N129-1 | 两objectheader201408/14NDS、cutoff31-May-2014，retrieval2026不等于现代δ重分析已进入评价。 | object-version-identity | direct | 129056001/013 H records | true |
| N129-2 | 明确target为643.6(1)13/2−母态的364.7(1)M1+E2至278.81的11/2−；ADOPTED给FL278.81。文献label365不应匹配到对象开头另一个未附L的G365.0(5)。 | level-and-transition-identity | direct-and-self-audit | 129056001 L643.6/G364.7/FL278.81；129056013 L643.6/G364.7 | true |
| N129-3 | 评价global明确成对A2/A4来自1977Gi02，单A2与DCO来自1992By03，POL来自1978Gi04。不能将后续reanalysis/ADOPTED/多图当这些原观测的新增独立样本。 | observable-source-lineage | direct | 129056013 globalc lines19–30；references | true |
| N129-4 | 同G364.7有1992层A2=−.68(.11)/DCO=.36(.05)，1977层A2=−.70(.03)/A4=.16(.05)，1978层POL=.07(.07)。P的评价舍入不构成独立于原.072(.068)的测量；实际angularconditions/Σ未给。 | evaluated-observables-and-boundary | direct | 129056013 G364.7 continuations | true |
| N129-5 | target MR空，CC=.0269(.0024)、KC=.0227(.0025)不代表实测δ；globalcG CC规定M1+E2未给MR时假定δ=.5。不能以这个CC循环验证旧δ或现代δ≈−2。该对象未核定具体atomicproducer版本。 | assumed-conversion-input-boundary | direct-and-self-audit | 129056001/013 globalcG CC；G364.7 MR/CC/KC fields | true |
| N129-6 | 643.6的T字段空白，不补0/邻态寿命；797.4等其它母态的RDDS时间不能借作target的absoluteB输入。 | parent-time-readiness | direct-and-self-audit | 129056013 L643.6；L797.4 | true |
| N129-7 | reaction RI364.7=43.3(1.7)、RI461.6=11.0(.5)；ADOPTED改为100(4)/25.4(1.2)。这是同源photon强度rescaling，不能当两套独立branching或忽略Cov构造totaldecay份额。 | relative-intensity-normalization | direct-and-self-audit | 129056001/013 L643.6 attachedG364.7/G461.6 | true |
| N129-8 | global一行把DCO来源写1992By02，而header及更详细cG写1992By03；refs页的By02实际为反质子弹性散射论文，与本nuclearlevel数据无关。错key已隔离，raw不改，不能把自动refsjoin当正确物理来源。 | isolated-citation-key-conflict | direct-reference-audit | 129056013 globalc line20/cG lines23–26/header；getrefs1992BY02/03 | true |
| N129-9 | 当前objects没有补齐A22/A44 originalcorrection层、布居、finitegeometry/gate/Pcalibration和jointCov；采用M1+E2标签不等于独立δ或wobbling赋值。 | inverse-and-model-readiness | direct-scope-audit | 129056001/013 selectedcomments/targetblocks | true |
| N129-10 | 若同L643.6两branch共享rho/coeff层，461.6为pureE2、target仅M1/E2，则本任务exact6j推得A4target=−(8/3)fE2 s4 A4ref。s4>0时两非零A4须异号；印刷positive margins不合该条件包，不构成actualdataerror/δ排除，purity/gates/Q/Σ尚未核。 | conditional-same-parent-reference-check | task-calculation-from-record-premises | 129056013 L643.6/G364.7/G461.6 pairedA4；本任务exactrank4proof | true |

## Selected Records

```text
129BA  L 643.6     1 13/2-                                                  B
129BA  G 364.7     1 43.3    17M1+E2                   0.0269 24            K
129BAS G KC=0.0227 25$LC=0.00333 9$MC=0.000692 23$
129BA2 G A2=-0.68 11 $ DCO=0.36 5
129BA2 G A2=-0.70 3 $ A4=+0.16 5
129BA cG $POL=+0.07 {I7}
129BA  G 461.6     1 11.0    5 E2                      0.01232              K
```

原80列及所有continuations以raw对象为准，以上是reaction目标marker摘录。ADOPTED在同L643.6/G364.7另给FL278.81。T/MR空白不补值，CC假设见N129-5。

## Summary

数据记录确认365的identity和各观测的不同primary谱系，还暴露了一个自动reference join的错误键。它没有提供现代新δ，也没有解决本文所缺的source coefficient层或完整response。[[ba129-365-mixing-reference-boundary]]据此分开作者report、database复制与chosen-reference计算。

## Competing Interpretations and Limitations

- 1977Gi02的题名为“Triaxial Shape and Onset of High-Spin Bands in129Ba”，DOI`10.1016/0375-9474(77)90714-X`，而1978Gi04为“Gamma-ray Linear Polarization Measurements in129Ba”，DOI`10.1103/PhysRevC.17.596`。HAL两条record目前仅metadata、没有file字段，publisher403/officialharvest401的1978正文未得；不能补取向/修正recipe。
- 1992By03为Byrne等*Nucl.Phys.A548*,131，DOI`10.1016/0375-9474(92)90080-4`；By02的自动join无关已隔离。已知相同facility/反应并不能由此认定不同论文的exacteventoverlap或完整独立性。
- 当前source身份冲突限于一条错误reference key，target header/反应/记录和其余来源已核，不扩大为整条质量链身份错误；未修改raw。

## Extracted Pages

- [[ba129-365-mixing-reference-boundary]]、[[129ba]]：source层与正确现代数值归属。
- [[angular-distribution]]：未核coefficient layer之前，不能用自选最大取向或数据库CC反向认证δ。
