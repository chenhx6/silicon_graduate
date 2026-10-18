---
type: source
title: "A=25官方评价：1041身份、混合比版本与字段谱系"
aliases: [NNDC A25 mixing references, 25Na1041 ENSDF crosswalk]
created: 2026-10-18
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-object
reading_depth: skimmed
data_version: "202508 ENSDF/cut31-May-2025; 202602 XUNDL/compiled19-Jan-2026; 200908 ENSDF in200910 archive/cut1-Feb-2008"
title_original: "Nuclear Structure and Decay Data for A=25 Isobar"
authors: [M. Shamsuzzoha Basunia, Anagha Chakraborty]
journal: Nuclear Data Sheets
year: 2025
volume: 205
pages: 1--188
doi: "10.1016/j.nds.2025.08.001"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "NNDC:25011001,25011012,25011015,25012001,25012036; selected25Mg reaction objects; official200910 ensdf.025"
source_url: "https://www.nndc.bnl.gov/ensdf/"
raw_file: "raw/data/gpt/day16-20261018/a25-25mg-adopted-18d5f7ec5728.ens"
raw_sha256: "18d5f7ec5728299cacefc78d9c1f9a49748dd105a7176a18a3a5164afec70a80"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [25Na, 25Mg]
reactions: []
experiments: [GRETINA, FMA]
methods: [ENSDF-fixed-column, phase-convention, source-lineage]
observables: [level-energy, gamma-energy, multipole-mixing-ratio, angular-distribution-coefficient, experimental-asymmetry]
tags: [evaluation-version, reference-identity, polarization, shared-data]
---

# A=25：评价字段与原实验的观测对象

## Bibliographic Record

2025评价为Basunia/Chakraborty，*Nuclear Data Sheets*205,1–188，DOI[10.1016/j.nds.2025.08.001](https://doi.org/10.1016/j.nds.2025.08.001)。ENSDF基版202508、cut31-May-2025；Crossref期刊出版月为2025-10，不能用基版月份代替。2009对照为R.B.Firestone，*NDS*110,1691–1744，DOI[10.1016/j.nds.2009.06.001](https://doi.org/10.1016/j.nds.2009.06.001)；实际读取的是NNDC官方存档中的200908对象，不声称读过被403阻止的期刊PDF。

官方入口[ENSDF Archives](https://www.nndc.bnl.gov/ensdfarchivals/)的真实JS引用`distributions/files.json`；据该目录下载[ensdf_0910_099.zip](https://www.nndc.bnl.gov/ensdfarchivals/distributions/dist09/ensdf_0910_099.zip)，仅提取`ensdf.025`，不猜旧对象URL。zip SHA256=`060f8b7c291c3f5a9193f3918f7cf959220be767b8a7e2d3b232ae0e11cd084b`；成员SHA256=`ba804aacea3a87f4f020f7e91204fb53d2e2c0f0db6d299bbdff1e7b97e0da66`；25Mg Adopted子对象为成员726–1518行，SHA256=`0ae9e923ed4ca2b25e6accd94db109071d5724023ac583203697c5f94231eeae`。下载日、zip发行日与评价cutoff各有不同角色。

## Scope and Reading Depth

2026-10-18实际取得九个当前官方文本对象和一个旧Adopted子对象，原文放repo `tmp/day16-a25-reference/`，raw槽尚未归档。完整读过25Na BeO反应142行、两个XUNDL23/25行、25Mg NRF15行；当前Adopted Na392行/Mg1291行、旧Adopted Mg793行及其余反应对象均只定向读header/目标level/gamma/MR注释与references。未通读A25 mass-chain全部评价、未研究寿命或强度。XUNDL Na官方一页PDF已实得并视觉核靶厚度、表/注释与level scheme；PDF SHA256=`79a5d5ea28a1b41d83b811614ae754e81aaf994ba4dd75d448c1b9b4d84be87f`。

取得方式为NNDC `DatasetFetchServlet`选核素，`EnsdfDispatcherServlet`按精确datasetcheck/xunpostcheck选文本/PDF。十对象身份/hash、冻结输入与数值审计见[本run输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/a25-reference-input-v2.json)及[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/a25-reference-audit.json)；保存物理结论的是本页及对应knowledge笔记。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N25-1 | 当前Na/Mg Adopted为base202508/cut31-May-2025；两个XUNDL为202602 header、19-Jan-2026由E.A.McCutchan从同一2026Lo01编译，标明unevaluated。XUNDL并非第二次独立采集。 | version-and-data-lineage | direct-object | 25011001/25012001 H；25011015/25012036 header/comments | true |
| N25-2 | Na Adopted1041.3(.4)位于3459.4(.7)(9/2+)→2418.3(.7)(9/2+)，M=(M1)、MR空；原注释M1来自(18O,pnγ)，RUL允许M1或E1。不能从空MR或旧标签推出δ=0。 | evaluated-target-identity | direct-evaluation | 25011001 L2418.3/L3459.4/G1041.3；cG M | true |
| N25-3 | Na BeO对象给FSU Ebeam35MeV、35/90/145°探测器；对象另概述角分组45/135°与90°。1041(1)在3458.6(.8)→2418.5(.8)，M1、MR空、A2=+.28(.09)；2418.5的J注释保留原论文(9/2)+及(7/2,9/2)+不一致。此为2015Vo12评价转录，不是本run原paper重拟合。 | evaluated-experimental-record | direct-evaluation | 25011012 header；L2418.5 J；L3458.6/G1041/A2 | true |
| N25-4 | XUNDL Na1041连3459(9/2+)→2419(9/2+)，M1(+E2)；numeric MR/DMR仍空，δ=0.0(.2)存cG MR注释。POL=+.043(.008)对应L26 Table2的A0，非physical P；仅取numeric gamma栏会漏掉已报告comment，补空为0则丢失误差/来源。 | format-and-observable-crosswalk | direct-object-and-primary-crosswalk | 25011015 G1041/continuation/cG MR；L26 Table2/Eq17 | true |
| N25-5 | XUNDL靶厚度的竖线m编码由官方PDF排成1.152 µg/cm²；L26 Sec3写1.152 mg/cm²，数值单位相差1000。保留转录差异，不改原件；不把XUNDL靶厚度误用于能损/响应重建。 | source-transcription-boundary | direct-object-versus-primary | 25011015 intro；officialPDFp1 beam-target line；L26 PDF3 Sec3 | true |
| N25-6 | 2009存档Mg三个Adopted MR为1611.712:−.189(.012)、1793.1:−.13(.03)、3970.3:−.02(.03)。在相同相邻multipole/单emitter合同下δRB=−δKS，转换后与L26 Table1引用的+.189(.012)/+.13(.03)/+.02(.03)逐项闭合。 | historical-reference-and-phase-crosswalk | direct-old-object-and-primary-crosswalk | official200910 member ensdf.025；MgAdopted G1611.712/G1793.1/G3970.3；L26 Table1/Ref40 | true |
| N25-7 | 当前Mg1611.712(7/2+→5/2+) MR=−.207(.013)，1793.1(9/2+→7/2+)为−.13(.02)，3970.3(7/2−→5/2+)为−.02(.03)。1612旧/新差别在相位转换后仍是评价数值更新；同版本谱系未知Cov，不作独立z检验或称新实验冲突。 | evaluated-MR-version-boundary | direct-evaluation-and-comparison | 25012001 G1611.712/G1793.1/G3970.3及parent J | true |
| N25-8 | 当前1612注释列−.22(.02) alpha,n、−.23(.04) p,p′、−.19(.02) NRF、−.18(.07) N,p；各反应MR分别指1975Bu14、1967Mc11/1968So03、1961Ra05、1988He15。3970的FLAG=F使alpha,n对象MR(F)指1972Ke13，覆盖默认1975Bu14。反应名或header主要作者不足以认证每个字段primary/独立性。 | field-specific-source-lineage | direct-evaluation | 25012001 G1611.712 MR comment；25012005 cG MR/MR(F)/G3970.3 FLAG；25012011/09/23 targetMR | true |
| N25-9 | 声明分量误差独立时，1612加权重放−.206805±.013098，与当前采用值舍入相容；1793中央−.13而内部σ=.012792，采用σ=.02未由此简单公式逐字复现。未取得evaluator误差选择程序，不替换原采用误差。 | conditional-arithmetic-replay | Codex-calculation-from-direct-values | 25012001 G1611.712/G1793.1 MR comments；本页加权公式 | true |
| N25-10 | XUNDL Mg3971原G值保留3971；当前Adopted为3970.3，后者nearest-keV是3970，不能以“rounded”名义静默改成同值。当前Adopted说明无误差Eγ可为level差扣recoil，level/gamma也不可强制简单相减闭合。 | energy-and-snapshot-boundary | direct-object-and-arithmetic | 25012036 G3971/cG E；25012001 cG E/G3970.3 | true |

## Summary

官方对象补齐Na1041 level identity、L26三个旧Mg reference的相位/版本对应；没有提供新的独立分支裁决。XUNDL原靶厚度token为`1.152 |mg/cm{+2}`，其官方PDF确实显示µg，不是本run将未解码文本误当mg。

## 旧值、当前值与相位顺序

| 同一条Mg分支 | 2009 official MR | L26引用δRB | 2025 official MR | primary谱系边界 |
| --- | --- | --- | --- | --- |
| 1612：7/2+→5/2+ | −.189(.012) | +.189(.012) | −.207(.013) | 当前注释四项加权；旧对象未列该平均的逐项算法 |
| 1793：9/2+→7/2+ | −.13(.03) | +.13(.03) | −.13(.02) | 当前三项加权；采用误差不由独立内部公式完全重现 |
| 3970：7/2−→5/2+ | −.02(.03) | +.02(.03) | −.02(.03) | MR(F)→Kean1972，非默认Butler1975 |

相位桥须连同[[martin-1987-ensdf-mixing-ratio-phase-conventions]] MA87-1/2、[[krane-steffen-1970-cd110-mixing-ratios]] KS70-13和[[longfellow-2026-gretina-energy-ordering-polarization]] L26-21的完整RME/系数合同使用；表中负转正不是新的物理解，也不许可任意cascade门直接换号。[[tuli-2001-ensdf-format-manual]] TU01-1/2约束显式号/未知/空栏；本页不从格式手册推断每篇旧primary的真实算符。

条件练习使用`w_i=1/σ_i²`、`δbar=Σw_iδ_i/Σw_i`、`σ_internal=1/sqrt(Σw_i)`。1612分量归一权重为.428884/.107221/.428884/.035011；1793为.409091/.181818/.409091。这里只重放评价列出的数字，不能把一个p,p′对象中两篇引用拆成两次新增独立测量，亦不把两个评价版本当独立数据。1793误差程序未恢复属于明确边界。

## Competing Interpretations and Limitations

L26作者对25Na1041的两支δRB≈0/−.85给A0pred+.021(.007)/+.002，两项同号；本页旧M1标签、XUNDL选定comment及同paper POL转录均不能增加独立选根证据。需要同target/门/事件选择的AD–A0 jointCov、实际Q/response和布居/feeding合同。FSU是另一35MeV反应采集，但目前本页只取得其评价文本、未取得原angular fit/误差与门，因此不把其A2直接组合进55MeV联合fit。

官方references身份已核：VonMoss2015 DOI10.1103/PhysRevC.92.034301；Butler1975 DOI10.1088/0305-4616/1/6/014；Sowerby1968 DOI10.1016/0375-9474(68)90213-3；McCallum1967 DOI10.1016/0370-2693(67)90193-1；Rasmussen1961 DOI10.1103/PhysRev.123.1386；Headly1988 DOI10.1103/PhysRevC.38.1698。此处只有官方书目，未把它们当已读primary。1975Bu14的NSR keyword写22Na(α,n)，但反应对象写22Ne(α,n)，电荷守恒也要求后者；保留metadata discrepancy，不照抄成真实反应。

## Knowledge Impact and Learning Decision

`supports`1041的明确level identity和L26旧Mg reference的版本/符号来源；`revises`此前“target Ei/Ef尚未定位”和“Firestone旧数值未直接核”的知识缺口。`limits`把XUNDL POL当P、空MR当0、默认参考作者覆盖field flag，以及用评价标签或同paper转录代替多解的独立companion。原实验δ/refit、真实response/Cov仍未恢复；新claims均needs_review，无human review或新课程信用。

## Extracted Pages

- [[gretina-25na1041-polarization-response-contract]]：target身份与旧/新reference矩阵。
- [[multipole-mixing-ratio]]：格式、phase、评价版本与原实验谱系分开。
- [[compton-polarimetry]]：A0/P不能因POL字段名互换；真实response仍需匹配。
