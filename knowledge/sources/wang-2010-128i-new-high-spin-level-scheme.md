---
type: source
title: "Wang 2010：128I 高自旋纲图与低能复合峰身份"
aliases: [Wang 2010 new high-spin level scheme 128I, 128I CPL 082701]
created: 2026-10-16
updated: 2026-10-16
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "A New High-Spin Level Scheme of 128I"
authors: [WANG Hai-Xia, ZHANG Yu-Hu, DING-Bing, ZHOU Xiao-Hong, ZHANG Ning-Tao, LIU Min-Liang, MA Ying-Jun, Y. Sasakiz, K. Yamada, H. Ohshima, S. Yokose, M. Ishizuka, T. Komatsubara, K. Furuno]
journal: Chinese Physics Letters
year: 2010
volume: 27
number: 8
pages: "082701"
doi: 10.1088/0256-307X/27/8/082701
language: en
canonical_source: doi:10.1088/0256-307X/27/8/082701
citation_key: ""
raw_file: "raw/papers/codex-day14/wang-2010-128i-new-high-spin-level-scheme.pdf"
raw_sha256: "28b81f5be7dfbe3b7efbb7efb37576eef7e4ac6060baac6c19d54e9c0187c387"
raw_storage_status: reserved-unpopulated-public-pdf-verified-in-wiki-tmp
raw_archive_verified_at: 2026-10-23
public_full_text: "https://cpl.iphy.ac.cn/en/article/pdf/preview/10.1088/0256-307X/27/8/082701.pdf"
public_full_text_sha256: "28b81f5be7dfbe3b7efbb7efb37576eef7e4ac6060baac6c19d54e9c0187c387"
nuclei: [128I]
reactions: ["124Sn(7Li,3n)128I"]
experiments: [tsukuba-127-128i-li7-28-32mev]
observables: [energy-levels, gamma-transitions, ado-ratio, coincidence]
methods: [gamma-gamma-coincidence, angular-distribution, level-scheme-reconstruction]
tags: [iodine, transition-identity, shared-acquisition, high-spin]
---

# Wang等2010：128I的新高自旋能级纲图

## Bibliographic Record

Wang等，*Chinese Physics Letters* **27**(8), 082701 (2010)，DOI [10.1088/0256-307X/27/8/082701](https://doi.org/10.1088/0256-307X/27/8/082701)。[出版商页面](https://cpl.iphy.ac.cn/article/doi/10.1088/0256-307X/27/8/082701)和PDF首页的题名、作者、卷期、DOI一致；Crossref用于身份交叉核，科学内容来自4页正文。只读Bib没有唯一匹配，citation key留空。

2026-10-16从页面`citation_pdf_url`指定的公开PDF入口取得403207bytes、4页，SHA256见frontmatter。`raw_file`仅为schema要求的未填充保留槽，`raw_sha256`是已核公开PDF的期望哈希，不代表该raw路径已存在。文件只放Wiki内tmp用于核验，原raw保持不变，PDF不进Git；正式URL/printed page及图号为持久定位。先前不同入口的restricted访问记录属于历史，不再代表本轮未读状态。

## Scope and Reading Depth

- 完成：全文四页主线、实验/分析、Figs1–4、完整讨论/结论；主要谱图、纲图和低能分峰图经视觉核验。
- 未完成：Refs15/16原件、全72边原事件重拟合、原响应/完整Cov和代码；不把打印图表当原始数据包。
- 实验谱系：Tsukuba、28/32MeV、4mg/cm²、9Ge+1planar、67M γγ/3M Xγ与Ding/Wang学位论文高度匹配，保守按共享/重叠acquisition处理，原run IDs未给，不计独立重复实验。

## Paper Question and Scientific Motivation

作者检验N接近82时重双奇128I是否仍保留较轻碘核中的集体结构，并借低能复合峰的分辨修订先前高自旋纲图（printed082701-1，引言/摘要）。

## Method and Design Logic

124Sn(7Li,3n)反应、两个束流能量与碘KX/γγ关系支持核素归属；planar探测器辅助分辨低能线，Ge阵列提供门和ADO。以既有167.4-keV (6−) isomer为参考，通过符合/能量和/ADO及系统学给spin/parity建议，不能把每个环节都当独立测量。

## Summary

本文把约102-keV复合峰拆到不同能级路径，借planar低能谱的不同门与交叉/平行跃迁建立新纲图。ADO仍保留spinsequence歧义，positiveπ及quasiparticle解释还用到邻核系统学；它补充thesis的直接期刊版本证据，不提供新的独立采集或原始响应/协方差。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| W10I-1 | 本文报告48levels/72γ、最高spin16的128I纲图；这些是论文报告口径，不等于Ding Table6.1的61表行或subset计数。 | author-reported-scheme-scope | direct | printed082701-1 Abstract; printed082701-2 paragraph above Fig2 | true |
| W10I-2 | Tsukuba28/32MeV、4mg/cm²124Sn、planar+9Ge、5台37°/143°其余近90°，67Mγγ/3MXγ；正文未给本任务可对账的100/200ns时间窗或原runID。与thesis指纹匹配，保守不计独立采集。 | apparatus-and-lineage-boundary | direct-and-derived | printed082701-1 Experimental paragraphs | true |
| W10I-3 | Fig1比较两束流能量并标127I/Te/Sb污染；作者将102/411及相关线指认给128I，元素KX不是逐事件同位素tag。 | observed-spectra-and-author-assignment | direct-and-derived | printed082701-1 final paragraph; printed082701-2 Fig1 and text | true |
| W10I-4 | 本文以167.4(6−)175ns和117.8连接固定激发能参考；ADO不能区分stretchedQ、ΔI0D或某些mixedΔI1。764.7的1.45(11)仍需866/101.3的dipole材料给1461/1562的J9/10建议。 | assignment-dependency-and-ambiguity | direct | printed082701-2 right column | true |
| W10I-5 | Fig4是756.5/764.7/117.8门下planar低能谱，横轴明确为Channel，显示101.3与102.2的不同门响应。与thesisFig6.5的能量轴标记作版本对照不能补其校准或直接digitizekeV。 | component-gate-and-axis-identity | direct-and-derived | printed082701-3 Fig4 | true |
| W10I-6 | 作者将101.3放为高位(10+)→(9+)、强102.2放为低位(8−)→(7−)，411只在纲图使用一次；其对Ref16错误方案的比较是作者陈述，Ref16原件本任务未读，不能重建旧拓扑。 | author-placement-and-primary-comparison-boundary | direct | printed082701-3 Fig3 and paragraphs below Fig4 | true |
| W10I-7 | 本文说已知弱102.2占总强度roughly14%；Ding thesis说约10%，两者分别保留。未给共同计数/误差/归一合同，不能作独立实验差异显著性或静默选其一。 | version-specific-intensity-summary | direct-and-derived | printed082701-3 top right paragraph; DingPDF81 printed73 | true |
| W10I-8 | 1461/1562的positiveπ与2qp组态借同位素系统学；无明显collectivefeatures和quasiparticle解释是作者判断，不是寿命/absoluteB/Qt直接测量，文末还说需进一步研究。 | author-interpretation-and-limit | direct | printed082701-3 lower text; printed082701-4 Discussion/Summary | true |
| W10I-9 | Ref16的Zheng2009/CPC33,179可与Crossref和NNDCgetrefs的33(S1)179–181、DOI10.1088/1674-1137/33/S1/057核身份；旧正文在本轮选定入口仍未得，IOP200是验证页，不能按本文批评重建旧图或核独立实验。 | reference-identity-not-body-evidence | direct-and-derived | printed082701-4 Ref16; Crossref DOI record; NNDCgetrefs128053024 entry2009ZH51 | true |
| W10I-10 | 本文Fig3/4的强102.2在285→183，与2015选定ENSDF的15.6/102位置和ECC绑定不同。NNDCtext与PDF是同评价的两表示，不能以adopted或来源较新裁决本文；须核2012Di14原文/版本和原门谱，当前保留冲突。 | direct-primary-versus-compiled-object-boundary | direct-and-derived | printed082701-3 Figs3–4; NNDCreaction PDF2 gamma table | true |

## Nuclear Structure Information

Fig3给出167.4 isomer锚点及183.0、285.2、696.2、1460.9、1562.2等已报告节点，低能triplet与许多平行分支是本轮关注范围。完整核素入口为[[128i]]，不从本文摘要“无明显集体性”替换更详细thesis的逐带/模型边界。

## Authors' Interpretation and Model Results

作者依据能级无规则间隔、多重分支和邻核系统学提出2qp及核芯耦合解释。本文没有报告本任务可重放的PES/NPA数值模型或absolute-strength实验；不把2012 thesis的模型内容倒灌为2010论文结果。

## Competing Interpretations and Limitations

低能复合峰身份改变会重排旧纲图，但ADO/spin/parity仍有多解；positiveπ与组态包含系统学前提。原Ref15低位数据与Ref16先前高自旋方案未直接读取，图中的不见峰也没有逐门检出限。精确planar校准、混峰counts、响应/Cov/时间窗未给，不能宣称完成实验重分析。

## Analytical Reconstruction

[[level-scheme-reconstruction]]“128I低能triplet：transition ID、门与转换字段”用Ding原表端点构造typedgraph，并以本刊Fig3/4作placement/门的直接对照。该图论练习的路径不存在只限选定边，不是实验absence；sameenergy不等sametransition。共scale/photon字段合同下的79/642条件界来自thesisRI，并非本文14%的原拟合或真实置信界。

## Knowledge Impact and Learning Decision

Decision: **supports** 逐component/门/端点核lineidentity；**revises** 相关2010期刊“尚未读到”的当前状态，直接补48/72口径、Channel轴和14%版本表述；**limits** 将论文/thesis计为独立重复、把spin/π与组态都当直接测量。来源页保持unreviewed，全部新claims true。

## Agent self-audit triage

P0：本轮公开PDF身份/哈希/四页正文与DOI/元数据一致，无技术hardP0；raw未改、PDF未公开到Git。P1：原runIDs、时间窗差异、References15/16原件、真实lowenergy校准/门响应及Cov待核；14%/10%只作版本并列，不裁决。P2：后续比较具体node/edge的版本改变，不能以48/72减61条表行计新增。P3：不为补citationkey改受保护Bib。

## Related Knowledge and Project Relations

- [[ding-2012-phd-thesis-127-128i-high-spin]]、[[wang-haixia-2012-173w-128i-high-spin-thesis]]：依赖谱系对照，非新增独立采集。
- [[tsukuba-127-128i-li7-28-32mev]]：装置/反应指纹与时间窗口径边界。
- [[level-scheme-reconstruction]]、[[128i]]、[[a130-thesis-evidence-matrix]]：逐边证据/方法与论文证据管线。

## Extracted Pages

- 来源版本与依赖回链：[[ding-2012-phd-thesis-127-128i-high-spin]]。
- 方法与证据矩阵：[[level-scheme-reconstruction]]、[[a130-thesis-evidence-matrix]]。
- 核素/实验复用既有[[128i]]和[[tsukuba-127-128i-li7-28-32mev]]，没有为本次四页文章另造独立实验页。


## 旧方案身份与2015评价的新增边界

2026-10-16本轮把Ref16精确核为CPC33(S1),179–181(2009)，DOI[10.1088/1674-1137/33/S1/057](https://doi.org/10.1088/1674-1137/33/S1/057)。原旧paper正文仍未取得；CPC连接失败、IOP验证页、Scholar/发现工具失败或restricted只属于所试路线，不证明全球无原文，也不据本文批评填旧图。本文与旧实验的比较目前只按作者陈述与二级评价报告分层。

新[[nndc-2015-128i-selected-level-gamma-records]] N128-4保存实际text/PDF的位置与ECC冲突：NNDC在约285列15.6到270、102在270到167；本文/[[ding-2012-phd-thesis-127-128i-high-spin]]强102为285到183。能量和不足判中间node，版本/更精确能量不能独立裁决。N128-9进一步识别2012Di14为PRC86,034302，但其正文尚未读，未归因错误或改变本sourceassignment。

新W10I-9/10 true，旧1–8/review保持；当前只新增可核身份/冲突边界，没有新增独立采集或假定2012图。下一信息增益来自对应primary/版本，而非重复sameenergy匹配。
