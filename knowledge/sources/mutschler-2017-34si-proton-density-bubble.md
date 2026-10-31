---
type: source
title: "Mutschler2017：34Si质子敲出、占据与中心密度解释"
title_original: "A proton density bubble in the doubly magic 34Si nucleus"
aliases: [Mutschler 2017 34Si bubble, 34Si质子密度亏空实验]
created: 2026-10-23
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model
reading_depth: deep-read
authors: [A. Mutschler, A. Lemasson, O. Sorlin, D. Bazin]
journal: Nature Physics
year: 2017
volume: "13"
pages: "152-156"
doi: "10.1038/nphys3916"
arxiv: "1707.03583v1"
citation_key: Mutschler_2017
citation_key_origin: locally-assigned-from-verified-DOI
canonical_source: "https://doi.org/10.1038/nphys3916"
source_url: "https://arxiv.org/pdf/1707.03583v1"
raw_file: "raw/papers/gpt/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam/mutschler-2017-34si-proton-density-bubble.pdf"
raw_sha256: "eb0450b2cfee9fc52098668d090db23b7e728899ec1116528d827e90a6b09a85"
raw_storage_status: existing-raw-read-only-verified-checkpoint124
public_staging_verified_at: 2026-10-23
public_staging_file: "tmp/day21/mutschler2017/PDFs/A_proton_density_bubble_in_the_doubly_magic_34Si_nucleus.pdf"
source_independence: NSCL-proton-removal-experiment-with-reused-36S-reference-and-model-density
nuclei: [34Si, 33Al, 36S]
reactions: [34Si-9Be-one-proton-removal]
experiments: [NSCL, S800, GRETINA]
models: [eikonal, RHFB, PKO2]
observables: [partial-cross-section, longitudinal-momentum-distribution, gamma-gamma-coincidence]
methods: [one-proton-knockout, in-beam-gamma-spectroscopy]
tags: [a34, density, shell-occupancy, reaction-model, evidence-boundary]
---

# 从敲出末态布居到质子密度解释

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

Mutschler等，Nature Physics **13**, 152–156 (2017)，DOI: 10.1038/nphys3916。2026-10-23实际核对Crossref精确DOI和出版商文章页citation_firstpage/lastpage均为152/156，online日期2016-10-24、印刷2017-02。arXiv API的journal_ref写142–146，保留为元数据差异；科学locator统一指实际6页arXiv v1，不冒称出版商PDF页码。作者栏列主要作者，完整作者表见原件首页。

公开arXiv PDF已用nature-downloader的单篇OA路线取得并验证PDF/6页/哈希。按本次无人值守配置先取正文，SI未检；没有创建、覆盖raw或Bib。较早记录把raw_file当作预留槽；124实际只读确认该raw路径现存且hash与staging一致。其创建不归本检查点，本轮未写raw；public_staging_file是另一个同hash副本。

## Scope and Reading Depth

Day21本session新读PDF1–6主线、Methods、Data availability及参考入口；视觉核PDF2的Fig.1，PDF3的Fig.2及能级图放大，PDF4的Fig.3和Eq.(1)。未取得事件、逐bin响应、原eikonal输入、联合协方差或作者按请求提供的derived data。Ref.[19]的36S敲出实验及Ref.[23/24]的中子/转移实验在本轮尚未独立原读。

## Summary

Mutschler等人在NSCL利用34Si次级束发生单质子移除反应，结合S800谱仪与GRETINA阵列测定33Al的激发态能级方案、截面分支比与纵向动量分布p∥，确认2101 keV与3704 keV态为ℓ=0质子敲出。结合程函反应模型提取出34Si基态的2s1/2质子轨道占据数仅为0.17(3)，与36S中近乎全满的1.7(4)形成鲜明对比（仅为其10%）。作者由此推断34Si存在质子中心密度空洞（bubble structure），并结合RHFB模型讨论了该中子-质子密度不对称性对自旋-轨道相互作用密度依赖与同位旋依赖的制约。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MU17-1 | NSCL以140 MeV/u的48Ca在846 mg/cm² Be上产生约4×10⁵/s的34Si束；其在100 mg/cm² Be次级靶上反应，S800识别33Al，七模块GRETINA记录γ。140 MeV/u指初级48Ca，不得作为本文未在此段给出的34Si次级能量。 | experimental-setup | direct-original | PDF p.2 | true |
| MU17-2 | Fig.1给singles及γ门谱；空三角标记线约占5.8%截面，作者认为不属于单质子移除机制。γγ/相对强度重建Fig.2方案，并与先前β衰变方案有差异。 | experimental-analysis-and-author-assignment | direct-original | Fig.1 | true |
| MU17-3 | Fig.2以γ门p∥形状比较ℓ=0/2；2101和3704 keV态支持ℓ=0，0/1621/1651 keV态支持ℓ=2。弱布居bKO<1%的态统计不足以利用其p∥；ground-state分布由扣除激发态贡献得到。PDF2的一处文字印“210”而图/后段为2101，不据此新建210-keV态。 | experimental-criterion-and-identity-boundary | direct-text-and-visual | Fig.2 | true |
| MU17-4 | Methods Eq.(1)为C²S_norm=bKO_f σ_inc,KO/(Rs σ_sp,f)，其中σ_inc,KO=27.7(1.0) mb，bKO为**敲出至末态的布居比例**，不是该态的γ衰变分支。Fig.2的2101/3704态bKO分别为1.5(4)%/1.4(3)%；百分数在乘截面前需除100。 | reaction-extraction-formalism | direct-original-equation-and-figure | Eq.(1) | true |
| MU17-5 | 作者推导2s1/2质子占据0.17(3)，与36S的1.7(4)比较；若四个未赋ℓ的弱态全取ℓ=0，增加0.07(3)。这只是所列四态的保守赋值变化，不是所有未测强度的置信上限。ℓ=2前三态谱因子和5.5±1.0，3926态归1d3/2为tentative。 | derived-observable-and-assignment-boundary | direct-author-extraction | PDF p.2 | true |
| MU17-6 | Fig.3的34Si/36S中子/质子密度是RHFB+PKO2计算，作者称其占据接近实验推导值，用于可视化；并明确泛函、pairing及quadrupole correlations会改变密度。不是电子散射实测密度图或90%中心亏空测量。 | model-result-and-author-limitation | direct-caption-and-text | Fig.3 | true |
| MU17-7 | Methods明确谱因子/占据并非直接observable，反应模型有有效势等不确定性；差分比较依赖这些效应在相邻闭壳核中相近的假设。作者另报告36S/34Si的ℓ=0截面比约12，作为比占据更贴近观测的支持，但本文不提供该比的完整联合误差。 | nonobservable-and-transfer-boundary | direct-original-method | PDF p.4 | true |
| MU17-8 | p∥比较仅用高动量侧，以避免eikonal对低动量耗散的近似；理论分布卷积次级束动量散布、靶内straggling和反应位置展宽。Fig.2误差含feeding扣除与经验Rs约20%的不确定度。 | response-and-error-contract | direct-original-method-and-caption | PDF p.4 | true |
| MU17-9 | Data availability仅说明raw数据来自NSCL、其它derived data向作者请求；建议未来电子—放射性核碰撞设施作更直接质子密度测量。本文没有给可下载的完整事件/response/Cov包，也没有证明当前Wiki装置能完成该测量。 | data-readiness-boundary | direct-original | PDF p.5 | true |

## Competing Interpretations and Limitations

作者的差分敲出数据支持2s占据耗尽与质子中心亏空解释；谱因子依赖反应模型并不抹去此支持。Fig.3是RHFB/PKO2的质子与中子密度，不能称直接空间成像。[[yao-2012-34si-beyond-mean-field-bubble]]比较的是另一模型的点质子/折叠电荷密度；不能只拿0.09反驳本实验。[[burgunder-2014-35si-two-body-spin-orbit]] BU14-D21-R106-3/4/5限定校准SM与指定K分解，不声称所有真实力效应唯有双体SO。原事件、反应job与jointCov未得。

## Extracted Pages

- Nuclei: [[experimental-claim-boundaries]]、[[high-spin-lifetime-strength-deformation]]、[[burgunder-2014-35si-two-body-spin-orbit]]、[[yao-2012-34si-beyond-mean-field-bubble]]。
- Methods: [[experimental-claim-boundaries]]。
- Synthesis: [[high-spin-lifetime-strength-deformation]]。


## Day21 checkpoint107：单质子敲出、占据数与空间密度推断边界审计（124纠正）

107的6页阅读按原记录保留；124只定向实读arXiv v1 PDF2–5文字、视觉PDF4 Fig.3/Methods。107的冻结回忆早于原读；108及110–113部分“冻结”文件实际晚于该轮源读取/运算，不能作为source前盲回忆。公开staging hash eb0450b2cfee9fc52098668d090db23b7e728899ec1116528d827e90a6b09a85；不声称本轮写入raw。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU17-D21-R56-1 | superseded：用MU17-D21-R124-1/2/3；旧复合locator与归档误称撤回。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| MU17-D21-R56-2 | superseded：不可把Yao电荷密度结果归到Mutschler Fig.3，改用MU17-D21-R124-4。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| MU17-D21-R107-1 | superseded：旧复合页码与实验/模型归属由R124逐项替代。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| MU17-D21-R107-2 | superseded：误差已含由Fig.2 caption支持，公式由PDF4支持，改用R124-2/3分开。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| MU17-D21-R107-3 | superseded：0.24(4)不是作者报告的新总占据误差，不能自行合并两个相关误差，改用R124-1。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| MU17-D21-R107-4 | superseded：Fig.3实际在arXiv PDF4，改用R124-4。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| MU17-D21-R107-5 | superseded：高动量比较与低统计弱态各自locator分开，改用R124-2/3。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| MU17-D21-R107-6 | superseded：未来更直接质子密度实验在PDF4；data availability跨PDF4/5，改用R124-3/6。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| MU17-D21-R124-1 | 两个ℓ0终态2101/3704keV导出2s占据0.17(3)；四个未定弱态全取ℓ0时作者另说增加0.07(3)。本任务只能加中央值得0.24，不能自造总误差(4)或全未测强度上限。 | author-extraction-and-alternative-assignment | direct-arxiv-text | arXiv v1 PDF p.2 occupancy paragraph | true |
| MU17-D21-R124-2 | Fig.2的bKO为末态布居百分数，feeding已扣；C²S误差含约20%的Rs项，不能再独立加入一次。2101/3704的1.5(4)%/1.4(3)%不是原始γ强度；弱布居p分布统计不足。 | measured-analysis-and-error-contract | direct-caption-and-visual | arXiv v1 PDF p.3 Fig.2 | true |
| MU17-D21-R124-3 | Methods给σinc,KO=27.7(1.0)mb及Eq1：若b以百分数存储，实际代入为(b/100)σinc/(Rsσsp)。只比较高动量侧，低动量耗散近似与响应卷积保留；谱因子非直接observable，跨核比较以反应效应相似为条件。未来设施被建议用于更直接质子密度约束。 | reaction-extraction-and-transfer-boundary | direct-arxiv-text | arXiv v1 PDF p.4 Methods | true |
| MU17-D21-R124-4 | Fig.3画RHFB+PKO2计算的质子/中子密度；占据与推导值接近提供可视化，非直接电子散射电荷密度。 | model-result | direct-caption-and-visual | arXiv v1 PDF p.4 Fig.3 | true |
| MU17-D21-R124-5 | 作者报告36S的ℓ0移除截面约为34Si的12倍，作为差分支持；本任务没有从独立36S事件重建该比值。 | author-reported-differential-evidence | direct-arxiv-text | arXiv v1 PDF p.4 measured-inclusive-cross-section paragraph | true |
| MU17-D21-R124-6 | 其余derived data依请求提供；本任务未取得这些数据或事件/Cov，也未联系作者。 | data-readiness | direct-arxiv-text | arXiv v1 PDF p.5 Data availability continuation | true |

### 124选定态中央账本

按Fig.2末态布居中央1.5%+1.4%=2.9%，乘Methods σinc=27.7mb给.8033mb，仅为选定两态的中央部分截面；不能当完整独立截面重提取。0.17/1.7=.10，作者四弱态替代的中央比(.17+.07)/1.7=.141176；未有共同Cov，不赋新的总占据误差或显著性。脚本system/scripts/day21_checkpoint124_literal_rounding_scope.py。
