---
type: source
title: "NNDC 178W DCO参考：2009评价对象、空MR栏与同母态角分布"
aliases: [NNDC 178W DCO reference records, 1979Do02 1989Kr01 selected ENSDF]
created: 2026-10-18
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-tables
reading_depth: read
title_original: "178W ADOPTED LEVELS, GAMMAS / 164DY(18O,4NG) / 177HF(A,3NG) / 170ER(13C,5NG)"
authors: [E. Achterberg, O.A. Capurro, G.V. Marti]
journal: Nuclear Data Sheets
year: 2009
volume: 110
pages: 1473-1688
doi: "10.1016/j.nds.2009.05.002"
citation_key: ""
citation_key_status: verified-DOI-but-no-unique-local-BibTeX-entry
data_version: "200907 / 09NDS headers, cutoff31-May-2008; retrieved2026-10-18; laterQ record separated"
canonical_source: "NNDC ENSDF 178W records178074001,178074004,178074006,178074005; header200907"
raw_file: "raw/papers/gpt/day16-20261018/nndc-178w-178074001-200907-a758b17a8a52.ens"
raw_sha256: "a758b17a8a52102c12ba87b66ea6d7c4cdd499dbd831d78e911d2fe08f51fd21"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [178W]
reactions: [164Dy-18O-4n, 177Hf-alpha-3n, 170Er-13C-5n]
observables: [level-energy, gamma-energy, multipolarity, angular-distribution-coefficient, relative-intensity, conversion-coefficient, K-conversion-coefficient]
methods: [dco-ratio, angular-distribution, source-lineage-audit, fixed-column-ENSDF]
tags: [ensdf, evaluated-data, dco, mixing-ratio, calibration, source-independence]
---

# 178W评价记录：参考行里没有已给出的signed δ

## Bibliographic Record

E. Achterberg、O.A. Capurro、G.V. Marti，*Nuclear Data Sheets for A=178*，**110**(7),1473–1688(2009)，DOI[10.1016/j.nds.2009.05.002](https://doi.org/10.1016/j.nds.2009.05.002)。题名/三作者/卷页已由Crossref核对；本次只读四个官方**选定ENSDF文本对象**，没有通读216页质量链文章。两个本地BibTeX文件未唯一命中此DOI，citation_key留空，不编造key或改Bib。

官方[ENSDF入口](https://www.nndc.bnl.gov/ensdf/)初始化普通HTTP session后，POST `DatasetFetchServlet`：`nuc=178W, nsrch=Search, searchType=quick, datasource=ensdf`；再POST `EnsdfDispatcherServlet`：`dbclass=ensdf, page-source=singular, chooseit=ENSDF text format, datasetcheck=<record>,178W`。HTML pre逐字提取，text hash与HTTP wrapper hash分开。

| 对象 | text SHA-256 | 本次读取快照 |
| --- | --- | --- |
| 178074001 ADOPTED | `a758b17a8a52102c12ba87b66ea6d7c4cdd499dbd831d78e911d2fe08f51fd21` | `tmp/day16-nndc-w178/178074001.ens` |
| 178074004 164DY(18O,4NG) | `01476a95d302609746ee6057fe7f5e47d70782c4d73cb109d3b7b074e66f6c6f` | `tmp/day16-nndc-w178/178074004.ens` |
| 178074006 177HF(A,3NG) | `317c67228e1bb1ae88421e2d7fdd73bddf2e6743902c9106ecfa7db8ba802251` | `tmp/day16-nndc-w178/178074006.ens` |
| 178074005 170ER(13C,5NG) | `b3215bcbf6609924392278f9e60df57550dfd2f7dd9c3c5f42f155f96bc58d9e` | `tmp/day16-nndc-w178/178074005.ens` |

HTTP wrapper hashes及成功/失败访问回执保存在本日run目录的选定对象manifest。**raw_file是尚未填充的归档槽位**：本任务保持raw不变，当前原始快照只在repo tmp，非已完成raw摄入。上面的对象/版本/hash及下方精确原行使关键事实可复核；归档缺口显式保留，不进入论文级ready状态，不以临时路径当长期知识正文。

## Scope and Reading Depth

- 178074004共102行：完整读header、globalcomments与L/G列表；只审核与921 target、169/137及306/225参考有关的身份，不声称重判全部能级。
- 178074006共223行：完整读方法、RI/AD来源和L/G/continuations，特别核1965.20与2133.93两个母态及3054.89的弱线。它是1979Do02的评价转述，不是Dors全文或原谱重放。
- 178074001共1434行：读header/global E,RI/M规则、1827/1964/2133/3053目标邻接和相近能量替代对象；没有逐条重审全部高K组态。
- 178074005共1028行：定向读header/global E/RI/M来源、同母态137/225与169/306、3053.61的921/1090 AD和K-conversion，以及相近168.0的替代母态；未完整核1028行全部结构内容。Refs页面另核1998Pu01、1999Cu02、1995Pu06、1997Wa29的身份，不冒称已读这些primary全文。
- headers为200907/09NDS、cutoff31-May-2008；adopted的Q record另有2012WA38。检索日2026不代表gamma信息更新到2026，Q的后加来源也不更新整张gamma表的cutoff。
- 没有取得原event、efficiency、finite-geometry response、DCOMAP、完整Σ或1979原件的混合比算符定义。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N178-1 | 四选定对象同200907/09NDS headers、三作者及2008cutoff；实际是在线选定记录，不是通读A178全文或2026新实验。Q的2012WA38来源另行区分。 | evaluated-object-identity | direct-evaluated-object | records178074001/004/006 H records；001 Q record | true |
| N178-2 | alpha对象归1979DO02：91.7%富集177Hf、38MeV、Ge(Li)，αγ角分布七角90–155度；RI明确125度，且提到辅助164Dy(18O,4n)实验。不能只凭alpha标题宣称所有输入与后续18O数据完全独立。 | evaluated-method-and-lineage | direct-evaluated-object | 178074006 header/globalcomments lines2–12 | true |
| N178-3 | L1965.20/(9-)的G137.34为M1,E2、A2=−.64(.05)、A4=.06(.05)，同母态225.83为E2、A2=.30(.03)、A4=−.04(.04)。逗号/括号按原样保留；这些系数是评价转述的AD，不是新测量。 | evaluated-same-parent-observables | direct-evaluated-object | 178074006 L1965.20/G137.34/G225.83及cG M continuations | true |
| N178-4 | L2133.93/(10-)的G168.71为M1,E2、A2=−.79(.04)、A4=.04(.05)；同母态306.05为E2、A2=.22(.04)，此行未给A4。不能以“未列A4”为0。 | evaluated-reference-observables | direct-evaluated-object | 178074006 L2133.93/G168.71/G306.05及cG M continuations | true |
| N178-5 | 上述137.34和168.71的MR/DMR固定栏均空；1.5(.4)和.8(.3)在CC栏，不是delta。记录本身未给这些CC的独立实验/计算recipe，不把字段存在当独立conversion测量或新的signed MR。 | fixed-column-identity-boundary | direct-and-self-audit | 178074006 G137.34/G168.71 columns42–55与56–64 | true |
| N178-6 | 18O对象归1989KR01；L3055.2只列(11)，G920.9为literal D、MR空。adopted L3053.81列11-/G920.8 M1+E2但MR仍空，Jcomment回指DCO与decay pattern；不是评价新增一次独立宇称/δ测量。 | evaluation-versus-experiment-assignment | direct-evaluated-object | 178074004 L3055.2/G920.9；178074001 L3053.81/G920.8及cL J | true |
| N178-7 | adopted的E,RI默认来自170Er(13C,5nγ)，M另混合多个反应的AD/ce/DCO。其1090/921的RI100/79不应当作原1989强度比1.2±.2的另一份同count、同response测量。 | normalization-and-source-dependency | direct-and-self-audit | 178074001 globalcG E,RI/M；L3053.81/G1089.6/G920.8 | true |
| N178-8 | alpha对象G1089.7的连写1.314按固定栏是RI1.3、DRI14，即1.3±1.4；不是RI1.314。同母态920.9 RI1.45(.08)，两者是125度RI，未取得原件/修正/Σ时不重造angle-integrated branch或以负下沿宣称记录错误。 | fixed-field-precision-and-response-boundary | direct-and-self-audit | 178074006 L3054.89/G920.9/G1089.7 columns22–31；globalcG RI | true |
| N178-9 | adopted相近137.0来自1875.7未知J的母态，136.9才属于1964.46/9-参考序列；相近168/921也各有其它母态。能量窗口命中不能代替level/line identity。不同对象的LS能量也不能作为独立数据平均。 | level-gamma-identity-boundary | direct-and-self-audit | 178074001 L1875.7/G137.0；L1964.46/G136.9；L4879.72/G168.0；L8578.6/G921 | true |
| N178-10 | 本任务在same-parent/common-coefficient-layer、pureE2 reference及Q2比=1条件下，137/225的A2比给D96坐标两根−2.16625/−.342242；169/306的central比超全δ可达范围，但一倍quoted-margin rectangle已有相交。不是新测MR/CI，也不靠调sigma/Q强配旧−1.9。 | bounded-reference-compatibility-check | task-calculation | 本页N178-3/4原行；D96 Eq3/7；day16_ensdf178_reference_audit.py固定输入 | true |
| N178-11 | 13C对象混收1998Pu01的80MeV/CAESAR AD与ce、以及1999Cu02的83/86MeV/Gammasphere DCO等；E与RI缺省取1998Pu01，另有X标记的1999Cu02归一。1998组又包括1995Pu06/1997Wa29，不能按论文数量计独立实验。 | evaluated-acquisition-and-reuse-lineage | direct-evaluated-object | 178074005 header/globalcomments lines2–29 | true |
| N178-12 | 13C对象L3053.61/11-的920.8行明确alphaKexp=.0067(.0011)、A2=−.03(.12)；同母态1089.6给alphaKexp=.0031(.0005)、A2=.07(.10)。二者MR仍空；显式Kexp不等于CC total .009(.004)/.00380，实际校准/计数/Cov/primary仍缺。 | evaluated-matched-K-shell-companion | direct-evaluated-object | 178074005 L3053.61/G920.8/G1089.6及cG M continuations | true |
| N178-13 | 13C记录中的168.3来自2132.83/10-，168.0来自4879.52/18-；两行都列literal A2=−.67且未给error。不能因为能量/数字相同把它们当同一reference或两次独立AD校准，也不补一个误差；是否共享峰/门分解待primary。 | near-energy-response-and-dependency-boundary | direct-and-self-audit | 178074005 G168.3/G168.0及各cG M；L2132.83/L4879.52 | true |

## Selected Records and Exact Locators

下列保留原固定空栏。Gamma第42–49列是MR、第50–55列是DMR；CC在56–62列，第63–64列为DCC。避免按空格token把CC搬进MR：

```text
178W   L 1965.20   11(9-)                                                   F
178W   G 137.34    5      8.4 5M1,E2                   1.5    4
178W  cG M$A{-2}=-0.64 {I5}, A{-4}=0.06 {I5}
178W   G 225.83    5      3.5 2E2                      0.206
178W  cG M$A{-2}=0.30 {I3}, A{-4}=-0.04 {I4}

178W   L 2133.93   11(10-)                                                  F
178W   G 168.71    5      3.6 2M1,E2                   0.8    3
178W  cG M$A{-2}=-0.79 {I4}, A{-4}=0.04 {I5}
178W   G 306.05    5     5.74 3E2                      0.0801
178W  cG M$A{-2}=0.22 {I4}

178W   L 3054.89   14
178W   G      920.9 2    1.45 8
178W   G     1089.7 1     1.314
```

本页excerpt省去行末padding；机器复算读取上述hash约束的完整text，按固定位置切列，不能从省略padding的Markdown复制重建原hash。

13C对象的实际K-shell companion另列，不能以CC列替代：

```text
178W   L 3053.61   1311-
178W   G 920.8     1 3.4     2 M1+E2                   0.009  4
178W  cG M$A{-2}=-0.03 {I12}, |a(K)exp=0.0067 {I11}
178W   G 1089.6    1 4.3     3 E2                      0.00380
178W  cG M$A{-2}=+0.07 {I10}, |a(K)exp=0.0031 {I5}
```

1998Pu01已由官方Refs与Crossref唯一匹配C.S.Purry等，*Multi-quasiparticle isomers and rotational bands in 178W*，NPA632,229–274(1998)，DOI[10.1016/S0375-9474(97)00654-4](https://doi.org/10.1016/S0375-9474(97)00654-4)。这里只核文献身份；未取得46页primary全文和K校准recipe。

## Summary

评价记录提供了137/169参考的真实AD摘要和对象映射，同时证明这些行**没有已填入的MR**。其CC栏、adopted M1+E2标签或125度RI均不能补造原KF89 reference的完整signed δ定义/测量。[[w178-921-dco-gate-double-solutions]]保留原实验双候选和本任务的新条件检验。

## Competing Interpretations and Limitations

137/225或169/306同母态只支持一个有用的shared-density候选；是否同selection、同coefficient layer、已有何种geometry/energy correction仍需primary。括号自旋及pureE2 reference的截断是假设，不因评价标签被提升为无条件已知。

N178-10的central不相容只涉及条件包；实际quoted margins已经能改变相容性，且Cov未知。不能借此裁决Dors的平均−1.9错误，也不能重新测定169或把旧AD/评价当独立于原data的实验支持。

## Analytical Reconstruction and Self-Audit

路径为官方对象/hash→固定栏/母态/line identity→原AD系数→显式shared-density/Q条件→全δ range与全部根。独立photon Legendre投影与generalized F核本任务矩阵到约6e−16，但共享CG/Wigner primitives；不是原producer重放。代码[day16_ensdf178_reference_audit.py](../../system/scripts/day16_ensdf178_reference_audit.py)，冻结input及完整audit在本日run目录。

## Knowledge Impact and Learning Decision

`revises` 把紧邻数字/CC/adopted标签当signed MR的做法；`supports` 先核same-parent reference和真实coefficient layer；`limits` 用评价重复引用替代独立实证。论文级δ、模式或原Dors producer仍not-ready；当前新事实由Codex self-audit核验，未发生人工审核。

## Related Knowledge and Project Relations

- [[kramer-flecken-1989-use-dco-ratios]]：1989KR01被同一评价对象引用，不能重复计实验。
- [[droste-1996-pdco-formalism]]、[[krane-steffen-1970-cd110-mixing-ratios]]：条件F矩阵/δ坐标，不代替1979自身的operator定义。
- [[angular-correlation]]、[[dco-ratio]]、[[w178-921-dco-gate-double-solutions]]：响应/门/phase与reference readiness。

## Human Review Triage

P0科学使用门：不把MR空栏读成CC、不由D/M1+E2评价标签清除原双候选、不把条件反演当实验新δ。无来源身份未隔离的技术P0：对象ID/headers/hash与临时原文已核；raw归档和本地Bib key缺口分别公开保留。P1为1979原件的AD修正/门/Σ、CC recipe、125度RI和adopted第三反应谱系；没有默认用户待办或新human-reviewed。

## Extracted Pages

- [[w178-921-dco-gate-double-solutions]]：同target双候选、同母态reference检验及匹配K-shell companion。
- [[dco-ratio]]、[[angular-correlation]]：gate/response/phase和评价复用边界。
- [[internal-conversion-analysis]]：K-shell/total分开、delta平方份额与实际electron/photon校准合同；本数据页不提供新实验拟合。
