---
type: source
title: "NNDC 164Yb 490/647-keV PDCO参考：2018评价对象、转换系数与寿命谱系"
aliases: [NNDC 164Yb PDCO reference records, Singh Chen A164 selected ENSDF]
created: 2026-10-17
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-tables
reading_depth: read
title_original: "164YB ADOPTED LEVELS, GAMMAS / 152SM(16O,4NG) / 124SN(44CA,4NG)"
authors: [Balraj Singh, Jun Chen]
journal: Nuclear Data Sheets
year: 2018
volume: 147
pages: 1-381
doi: "10.1016/j.nds.2018.01.001"
citation_key: SinghChen2018A164ENSDF
citation_key_origin: agent-local-online-dataset-label
data_version: "201712 headers; cutoff30-Nov-2017; NNDC records164070001/164070004/164070003 retrieved2026-10-17"
canonical_source: "NNDC ENSDF 164YB records 164070001,164070003,164070004; version201712"
raw_file: "raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/nndc-164yb-164070001-201712-606ddb5aaea1.ens"
raw_sha256: "606ddb5aaea1a6563da05ed19c906e839b577b28dadc62707bf6a0b2c27fc569"
raw_storage_status: archived-agent-managed-public-data-object
nuclei: [164Yb]
reactions: [152Sm-16O-4n, 124Sn-44Ca-4n]
observables: [level-energy, gamma-energy, relative-intensity, conversion-coefficient, angular-distribution-coefficient, half-life]
methods: [level-scheme-reconstruction, source-lineage-audit, conversion-coefficient-analysis]
tags: [ensdf, evaluated-data, pdco, 164yb, calibration, source-independence]
---

# 164Yb：评价记录不自动解决PDCO双解

## Bibliographic Record

B. Singh与J. Chen，“Nuclear Data Sheets for A=164”，*Nuclear Data Sheets* **147**,1–381(2018)，DOI[10.1016/j.nds.2018.01.001](https://doi.org/10.1016/j.nds.2018.01.001)。Crossref核题名、作者、2018年1月、卷页；本次实际证据为NNDC当前提供的三个**选定ENSDF文本对象**，没有通读381页质量链论文。

从[ENSDF目录](https://www.nndc.bnl.gov/ensdf/) POST `DatasetFetchServlet`，参数`nuc=164YB, nsrch=Search, searchType=quick, datasource=ensdf`；再POST `EnsdfDispatcherServlet`，参数`dbclass=ensdf, page-source=singular, chooseit=ENSDF text format, datasetcheck=<record>,164YB`。官方HTML pre内的完整ENSDF text逐字抽取，新建如下agent-managed raw，不覆盖已有证据，也不将raw纳入Git。

| record /对象 | canonical raw文件 | text SHA-256 |
| --- | --- | --- |
| 164070001 ADOPTED | `raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/nndc-164yb-164070001-201712-606ddb5aaea1.ens` | `606ddb5aaea1a6563da05ed19c906e839b577b28dadc62707bf6a0b2c27fc569` |
| 164070004 152SM(16O,4NG) | `raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/nndc-164yb-164070004-201712-eec3131d9213.ens` | `eec3131d9213eba97bdcdeca9cb2d6963b045e87520df08ea224675ca0e347d8` |
| 164070003 124SN(44CA,4NG) | `raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/nndc-164yb-164070003-201712-a46a5830695a.ens` | `a46a5830695aa2f345fa3e2fa8f83c821a26a0568df57d45b6f81405f7ac0db2` |

对应原HTTP response SHA-256依次为`500e6c10478b82a64d0e3a7424ed5d1dd2945eea81386d00ba5f0930ff85232d`、`0d31ca592d514721f8e3adbe3bc695685a49734761e0052c5ae2eecf6954de0f`和`10194fd7716fae453f90717febd5c0a7d4972952c225f3c3d9a53ad7133b2820`。HTML wrapper与text不是相同hash；来源版本/字段依据text对象，包装hash只标访问记录。

## Scope and Reading Depth

- ADOPTED653行：header/version/globalcomments，七个ground-band reference，2400.80与3388.98目标及必要band/gamma邻接记录；不声称逐条审核全部653行物理内容。
- 152SM对象527行：globalcomments/来源定义、相同目标和reference的L/G/continuation、647 EKC及489理论KC、302弱branch。不是原1986/1995论文全文。
- 124SN对象202行：完整读header、方法/时标/修订comments和L/G列表，特别核3390.0的寿命与489.9；没有重放其DSAM/RDDS。
- References页核1986JO02/1995NO04/1996NO12/1996XI01/1976BO27的题名/作者/DOI和reaction摘要。它们是metadata，不冒称已得primary body。
- Source/claim self-audit；新claims `needs_review: true`，没有human review或新核素/集体模式裁决。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N164-1 | 三对象header为201712/18NDS，cutoff30-Nov-2017，对应2018评价；2026是retrieval date，不是新的实验cutoff。 | evaluated-object-identity | direct | records164070001/003/004 H records | true |
| N164-2 | ADOPTED高spin E/RI主要取1995No04，M/MR来自angular/ce及部分RUL；152SM对象A2/A4/EKC缺省指1986Jo02，CC/KC则为BrIcc v2.3 Frozen Orbitals。三类量与原实验不能同层计数。 | evaluated-source-lineage | direct | 164070001 globalcG E,RI/M,MR/dG CC；164070004 globalcG andDG CC | true |
| N164-3 | ADOPTED3388.98(13)、J字面(16+)母态的489.8(1)到2899.20(13)14+；同母态302.3(1)的RI2.9(.7)，489.8为100.0(2.2)。保留tentative标记，非PDCO单独唯一spin。 | evaluated-level-and-branch-identity | direct | 164070001 L3388.98/G489.8/G302.3；L2899.20 | true |
| N164-4 | 152SM对应L3389.26(18)、G489.8(1)的RI27.2(.6)，G302.3 RI.8(.2)；489的A2=+.30(.01)/A4=−.08(.01)，另附1972值。该块未给EKC；KC=.01475(.00021)/CC=.0188是理论字段，不能说已测490转换。 | evaluated-observable-identity | direct | 164070004 L3389.26/G489.8 continuations | true |
| N164-5 | ADOPTED2400.80(12)、J字面(11)-的647.4(1)到1753.35(11)10+；M为E1(+M2)、MR=+.016(.026)，这里MR是M2/E1，非E2/M1。 | evaluated-multipole-and-spin-boundary | direct | 164070001 L2400.80/G647.4；L1753.35 | true |
| N164-6 | 152SM647.4块有EKC<.0042，confidence level未注明；来源缺省1986Jo02。该块CC=.00351(.00010)、KC=.00298(.00009)由BrIcc给出，不能将实测上限与理论值当两份conversion测量。647已被ST99拿来校准alignment，此先验不可重复计为其独立确认。 | experimental-limit-and-theory-separation | evaluated-record-and-source-synthesis | 164070004 G647.4 line189/EKC；globalcG；ST99Sec4 | true |
| N164-7 | ADOPTED目标T字段为1.75(.35)ps；124SN对象3390.0/16+、489.9同列该值。按ENSDF half-life定义换mean tau=2.524716(.504943)ps，lambda=3.960841e11s^-1为任务换算；原primary fit/feeding/mean-time列还未核。 | evaluated-time-and-unit-conversion | direct-and-task-calculation | 164070001 L3388.98 T；164070003 L3390.0/G489.9 | true |
| N164-8 | ADOPTED G489.8的BE2W=2.1E2(5E1)是采用E2/branch/time模型的评价派生列，不是独立于该假设的新B(E2)实验或δ分支证明。 | evaluated-derived-strength-boundary | evaluated-derived | 164070001 G489.8/BE2W continuation | true |
| N164-9 | ADOPTED与152SM相同ground reference的level central差约−.26至−.34keV、target γ仍同489.8/647.4；它们是不同LS/输入选择下的评价表示，不能忽略shared calibration/levelCov而作独立chi²或平均。 | evaluation-normalization-and-covariance | direct-and-task-crosswalk | 164070001/004 selectedGS L records；globalcL E/globalcG E,RI | true |
| N164-10 | G302.3的M/CC空白保留unknown，不补0；仅有parent T、相对photon RI和采用E2的CC，不足以重算两候选的absolute strengths或总branch，缺unseen inventory/302 ICC/actualΣ。 | inverse-readiness-boundary | direct-and-self-audit | 164070001 L3388.98/G302.3/G489.8 | true |
| N164-11 | 152SM globalcomment把secondary reaction写150Sm(16O,4n)，其A平衡为162；NSR1986JO02及Lund作者机构abstract均写150Sm(18O,4n)，可给164。此metadata冲突已隔离，未改raw或将16O版本作为另一个164采集；机构abstract非primary全文。 | isolated-reaction-metadata-conflict | direct-secondary-source-comparison | 164070004 globalcomments lines5–14；NSR1986JO02 reactionabstract；Lundrecord389c199a abstract | true |
| N164-12 | 124SN对象混收124Sn44Ca、138Ba30Si及128Te40Ar工作；global寿命规则明确g.s. up-to18的RDDS，不能不看row/primary就把所有sideband寿命和effectiveF(t) half-times同化。3390未带高spin F/G/H effective标记，primary方法归属仍需核。 | lifetime-source-and-method-boundary | direct-and-self-audit | 164070003 header/globalcL T/T(F,G,H)；L3390.0 | true |
| N164-13 | ST99候选atanδ=−21°给radiative M1/E2 fractions .871572/.128428，是同一gamma的component fraction；不能当整个母态branch或把缺失mixed-ICC沿用pureE2 CC。 | source-hypothesis-component-calculation | task-calculation | ST99Table3 mixedbranch；164070001 G489.8/302.3 scope | true |

## Selected Records and Exact Locators

以下原行同时保留source标记与空白，不把未列量当0：

```text
164YB  L    3388.9813(16+)             1.75 PS    35                        K
164YB  G 302.3     1  2.9    7
164YB  G 489.8     1 100.0   22E2                      0.0188
164YBB G BE2W=2.1E+2 5

164YB  L    2400.8012(11)-                                                  F
164YB  G 647.4     1 100.0   22E1(+M2)   +0.016  26

164YB  L    3389.261816+                                                    K
164YB  G      302.3 1     0.8 2
164YB  G 489.8     1     27.2 6 (E2)                   0.0188
164YB2 G A2=+0.30 1 $ A4=-0.08 1
164YBS G KC=0.01475 21$LC=0.00314 5$MC=0.000726 11

164YB  G 647.4     1    13.4  3E1(+M2)   +0.016  26    0.0035110            B
164YB2 G A2=-0.17 1 $ A4=-0.04 1 $ EKC LT 0.0042
164YBS G KC=0.00298 9$LC=0.000418 14$MC=9.3E-5 3

164YB  L    3390.0   16+                1.75 PS  35                         E
164YB  G      489.9
```

首两组为ADOPTED，后两组152SM，末组124SN；多处相同field是评价搬运/换normalization，不计多份独立采集。真正raw的80列和所有continuations保存在上列.ens，以上仅target marker摘录。

## Sources and Independence

- [1986JO02 refs](https://www.nndc.bnl.gov/ensdf/getrefs.jsp?recid=164070004&dsid=152SM%2816O%2C4NG%29)：S. Jonsson等，*NPA*449,537–578，DOI`10.1016/0375-9474(86)90234-4`。题名Near-Yrast Spectroscopy...，含angular与mini-orange/Si(Li) ce。此稿body尚未取得；数据采用层不写成primary精读。
- 1995NO04：A. Nordlund等，*NPA*591,117，DOI`10.1016/0375-9474(95)00124-J`，NORDBALL83.2MeV；sourcecomments提醒其Table1 column2的部分Jπ印值有误，本任务不凭这一备注重新确定目标spin。
- [1996XI01 refs](https://www.nndc.bnl.gov/ensdf/getrefs.jsp?recid=164070003&dsid=124SN%2844CA%2C4NG%29)：H. Xie等，“The Loss of Collectivity at High Spins in164Yb and Its Neighboring Even-Even Nuclei”，*NPA*599,560–578，DOI`10.1016/0375-9474(95)00446-7`；metadata核1996年3月，尚无primary body/producer。
- 1976BO27：B. Bochev等，*NPA*267,344，DOI`10.1016/0375-9474(76)90665-5`；g.s. RDDS来源，不自动覆盖sideband3390。
- [[starosta-1999-pdco-experimental-test]]的138Ba30Si主采集不同于152Sm/124Sn所述采集，但其647 prior和Fig1引用本链；同论文的四P、integratedP、RDCO也不重复计独立。
- [Lund作者机构记录](https://lup.lub.lu.se/record/389c199a-7493-48eb-8cc0-9ea30c4745f7)公开abstract亦写150Sm(18O,4n)，未给公开PDF链接；它佐证N164-11的metadata判断，不是本次取得primary body。

## Summary

当前评价支持目标identity、647实测K-conversion上限的谱系及目标寿命，未给所查489.8块的实测conversion。adopted E2、theory CC和derived BE2W彼此有假设依赖。没有据此宣布PDCO两解已经由“数据库+寿命”消除。

## Competing Interpretations and Limitations

- 16+ E2与14+ M1/E2为ST99的实验候选；评价的band association、RUL、derived strength不能循环作为新独立证据。
- source字段空白与metadata冲突须保留，尤其302 ICC、secondary projectile、647限制的CL及primary寿命定义。
- 避免nearest-energy误认：附近492.6/491.8/650.4/645.7等属于不同parent/bands。目标匹配用原ST99级联和选定daughter/band；energy residual本身不证明placement或无污染。

## Analytical Reconstruction and Self-Audit

[冻结input](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-n164-record-crosswalk-input.json) SHA-256 `d412f15d95efeb69ba48a18d95f2ef790eb5561cc6e4de1afbb8ddb90bd6138c`；[parser/crosswalk](../../system/scripts/day16_n164_record_crosswalk.py)核三raw hash、field/unknown、record header和unique selector，完整结果见[artifact](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-n164-record-crosswalk.json)。首轮col77 comment flag错取col76，触发reference选择断言且无numeric output；修正至官方field位置并只在global BAND声明内解释flag，未改raw或physical selectors。

level/RI两对象的nominal变换不做独立拟合或新χ²；lifetime只作ln2单位转换；未知Cov/feeding/完整branch不补。可复用解释与下一输入合同写入[[st99-pdco-calibration-table-replay]]。

## Knowledge Impact and Learning Decision

- `supports`：把647已知性质追回真正的ce/AD谱系；补目标寿命与record身份。
- `limits`：所查489记录仍无measured ICC，theory/adopted标签不能独立选分支；actual L4仍not-ready。
- `revises`：明确T1/2/mean tau、total CC/KC/EKC及两种RI normalization，隔离secondary reaction metadata冲突。

## Human Review Triage

新claims self-audited、非human-reviewed。未得到primary body、actualΣ或shell-matched490转换测量时，只保留具体研究边界，不自动转为用户待办。

## Extracted Pages

- [[st99-pdco-calibration-table-replay]]：所查EKC/理论CC、time、RI归一和derived strength的具体使用门。
- [[dco-pdco-ambiguity-worksheet]]：actualreference数据身份与双解保留；不新增独立164Yb核素或band页面。
