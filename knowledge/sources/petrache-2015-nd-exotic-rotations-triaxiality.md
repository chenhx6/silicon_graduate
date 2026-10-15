---
type: source
title: "Petrache 2015：Nd核的特殊转动与三轴性"
aliases: [Petrache 2015 Nd exotic rotations, Exotic rotations and triaxiality in Nd nuclei]
created: 2026-10-15
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
source_type: journal-review-and-interpretation
reading_depth: deep-read
title_original: "Exotic rotations and triaxiality in Nd nuclei"
authors: [C. M. Petrache]
journal: Physica Scripta
year: 2015
volume: 90
pages: 114016
doi: 10.1088/0031-8949/90/11/114016
language: en
canonical_source: "https://doi.org/10.1088/0031-8949/90/11/114016"
citation_key: ""
raw_file: "raw/papers/2015-Petrache-Nd-exotic-rotations-triaxiality.pdf"
raw_sha256: cc6f8b952b32ff32b462987cc86f9417a0cb8702b16bc797231356b153ca5b35
nuclei: [128Nd, 129Nd, 130Nd, 131Nd, 132Nd, 133Nd, 134Nd, 135Nd, 136Nd, 137Nd, 138Nd, 139Nd, 140Nd, 141Nd]
reactions: []
models: [cranked-shell-model, total-Routhian-surface, cranked-Nilsson-Strutinsky, tilted-axis-cranking]
observables: [dynamic-moment-of-inertia, transition-quadrupole-moment, band-systematics]
methods: [high-spin-spectroscopy, comparative-systematics]
tags: [a130, neodymium, triaxiality, rotation-axis, selection-boundary]
---

# Petrache（2015）：Nd核的特殊转动与三轴性

## Bibliographic Record

C. M. Petrache, *Physica Scripta* **90**, 114016 (2015)，DOI [10.1088/0031-8949/90/11/114016](https://doi.org/10.1088/0031-8949/90/11/114016)。Crossref题名/作者/卷/文章号与出版商PDF正文首页一致；正文记received2014-10-14、accepted2014-12-22、published2015-10-29。以下使用印刷pp.1–3；下载PDF另含一页出版商封面，故PDF页=印刷页+1。

实际从[出版商入口](http://stacks.iop.org/1402-4896/90/i=11/a=114016/pdf)取得397420 bytes PDF，SHA256如frontmatter，保存于`tmp/day14-20261014/petrache2015/PDFs/Exotic_rotations_and_triaxiality_in_Nd_nuclei.pdf`。下载器将TDM链接误作OA证据并标`open_access_downloaded`；本页只认定**公开入口成功取得出版商PDF，开放许可未核**。Crossref的TDM/copyright不是CC或开放获取证明，未采用该自动许可结论。arXiv精确DOI与HAL检索均0，不将0解释为不存在别的作者副本。

本次按daily-learning授权建立来源记录，**未完成raw归档摄入**；`raw_file`是尚未填入的保留槽，未动raw/Bib。citation key没有本地匹配，留空。出版商封面的下载归属信息属于执行元数据，不作科学证据；原PDF不改，身份回执省略该归属字段。

## Scope and Reading Depth

- **Covered scope**：正文印刷pp.1–3/PDF2–4全部主线、Fig.1、Table1、讨论/寿命展望与参考文献；三页均视觉核验。问题是Nd同位素高自旋带的惯量分组、三轴性与相对转轴解释，不是新实验报告。
- **Not covered**：原始γ事件、每带完整能量/筛选mask、权重与协方差；上游各实验全文本次未重读；没有实际136Pr tensor/axis map、独立共存解或1996Pr原文。未请求SI。
- 来源前回忆已受Lv2025 Ref.[48]及其γ/axis段priming；读取前记录已冻结。全部PT15 claims保留`needs_review: true`，页仍`unreviewed`。

## Summary

文章汇总128–141Nd已有高自旋研究，用经选带和筛选的动态惯量J^(2)展示两组典型量级，并以CNS等模型讨论负γ/中间轴和正γ/短轴转动。作者明确将寿命测量列为检验该转轴变化是否真实的下一步。因此它能解释Lv2025引用的相对轴语境，却不能提供136Pr的真实frame或新实测γ。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PT15-1 | 本文汇总128–141Nd已有GASP/EUROBALL/Gammasphere等研究，讨论全局带系统学；其图和table复用上游文献，不构成一次新独立实验。 | review-scope-and-lineage | secondary | printed p.1 Introduction | true |
| PT15-2 | Table1列138Nd总36/Q28/D8，139Nd 8/3/5，140Nd 23/12/11，141Nd 6/3/3。它是作者当时的band census，Q/D按E2序列或M1/E2 crossover序列归类；不以“triaxial bands”表题把每带形状升级成独立实验确认。 | review-census-and-boundary | secondary | printed p.2 Table1 | true |
| PT15-3 | 作者对选定数据报告轻/重组平均J^(2)约51/23 ħ² MeV^-1，认为差异可能对应转轴由中间轴向短轴变化；平均值不是本次重算或新统计检验。 | review-summary-and-author-interpretation | secondary | printed p.3 first paragraph | true |
| PT15-4 | 图的band纳入规则逐核不同；平均值只取远离interaction且ħω>.3 MeV的点。为凸显两组gap，低J^(2)组图示另删去至少达到各带平均值两倍的点。筛选/图示与均值范围须分开，未给完整mask/原序列，不能独立复算其gap或不受筛选影响的程度。 | selection-method-and-readiness-boundary | direct-and-derived | printed p.2 Discussion | true |
| PT15-5 | 作者将轻Nd的calculated γ<0称为绕中间轴、重Nd的γ>0称为绕短轴；并保留136–138Nd内两类band与不同轨道/形变驱动的例外。这里γ号包含相对转轴的模型语境，不是γ号本身测得两种形状。 | model-mediated-author-interpretation | secondary | printed p.3 gamma-axis paragraph | true |
| PT15-6 | 文章末段说需测量heavy Nd和136/137Nd中非highly-deformed bands的寿命，检验计算形状与转轴/γ号的一致性，并判断N76–77附近轴变化是否真实。原文将其保留为待检验解释。 | author-stated-missing-observable | direct | printed p.3 final Discussion paragraph | true |
| PT15-7 | 对惯量gap的解释同时涉及集体贡献、aligned intruder particles和变形；文中138Nd若干crossing还被赋不同可能原因。单一J^(2)分组不能脱离这些条件唯一反推γ/轴或shape coexistence。 | competing-interpretations-and-scope | secondary-and-derived | printed p.3 crossing and possible-explanation paragraphs | true |
| PT15-8 | 本文没有给136Pr D4/D6逐态tensor或其TableII/Fig16到signedγ的映射，也未直接展开Lv2025所述high-j lowΩ/highΩ完整极化链；主要讨论Nd系统学与模型转轴。引用它不能补Pr136实际输入或1996原始263/405次序。 | cross-source-transfer-boundary | derived | printed pp.1–3 Nd discussion | true |
| PT15-9 | 文中称J^(2)不依赖band spin assignment和excitation energy；该结论不豁免正确序列、相邻跃迁身份与ΔI步长。绝对标签/能量offset与相对顺序/步长是不同输入，需另做能级链检查。 | observable-domain-and-our-inference | direct-and-derived | printed p.2 J^(2) definition paragraph | true |
| PT15-10 | 本文Ref32与46均为Laird2002 PRL88,152501，仅首作者初始字母R.W./R.V.有差异；Crossref/INSPIRE的同DOI元数据支持它们指同一文章，不能算两条独立实证。Ref47 Matev2007是后续理论/数据比较，其实验输入回指早期作者工作。 | citation-identity-and-data-lineage-boundary | direct-and-contextual | printed p.3 Refs32/46/47; Matev2007 PDF p.14 Refs20–21 | true |

## Table1 Cross-Check

| Nd mass | Total | Q | D | Q+D |
| --- | ---: | ---: | ---: | ---: |
| 138 | 36 | 28 | 8 | 36 |
| 139 | 8 | 3 | 5 | 8 |
| 140 | 23 | 12 | 11 | 23 |
| 141 | 6 | 3 | 3 | 6 |

本次逐行算术一致，合计73=46Q+27D。这只是四行census的相容性，不是73次独立采集、73条Fig.1完整曲线或三轴性的显著性。正文例如只画138Nd的14/15高自旋Q bands，而Table1的28Q包含更低自旋或过短/不规则序列；不能由表数反推图的统计样本。

## Competing Interpretations and Limitations

作者用calculated shapes和转轴叙述解释J^(2)gap，同时保留形变、intruder占据、crossing和选带条件。低组显示删点与平均范围均是作者公开说明；它们使结论成为条件系统学，不能仅凭图上空隙宣布一个未经选择影响核查的统计分类器。这不证明作者处理不当，当前也没有原始序列可检验其“should not have any impact”判断。

γ号与中间/短轴的语言有直接来源，但本文没有给Pr136真实坐标、四极张量或完整波函数。[[triaxial-deformation]]的chosen normal form仍不能归给作者实现；same quadrupole不等于same full state。

## Counter-Evidence and Missing Companion Observables

后续已直接核[[matev-2007-a130-quadrupole-alignment-additivity]] MT07-8/18：Ref47是理论/数据比较，实验输入回指Riley2001/Laird2002；固定reference的轨道变化不等于沿同位素链的N趋势，不能从其局部有效矩符号直接裁决本文的系统学措辞。PT15-10所记Ref32/46复引也不增加独立测量；共享采集/引用本身不规定逐点协方差，仍需原分析。

最直接的限制来自PT15-6：源文自身要求寿命来检验轴变化。若要重算或比较J^(2)还需完整有序Eγ、ΔI、interaction/频率/删点mask、校准和协方差，以及对齐/形变的模型对照。相关实验数据与模型解释必须分开。

对[[lv-2025-136pr-tac-covariant-density-functional]]的迁移只到“signedγ可编码相对主轴、惯量与寿命须联合核查”。未补Q1π、D4/D6实验共存、actual RHB输入或1996Primary。

## Related Knowledge and Project Relations

- `methodological-bridge` → [[moments-of-inertia]]：动态惯量的绝对offset不敏感与序列/ΔI/筛选条件分开。
- `limits` → [[triaxial-deformation]]：γ号、相对轴和实验形状判据分层。
- `foundational-background` → [[lv-2025-136pr-tac-covariant-density-functional]]：其Ref.[48]的实际讨论语境，不是Pr136独立实证。

## Knowledge Impact and Learning Decision

Decision: **supports** signedγ的相对转轴语境，**limits** 从J^(2)gap或引用谱系到唯一形状解释。持久化本source与已有triaxial概念的直接来源校准；不扩写Nd核素页、不另建project或research-note。后续高信息路线是正确能级链/ΔI到J^(2)的实际能量练习及selection敏感性，而不是重复几何toy。原PSM/TPSM覆盖2/7和Pr136解释排序不变。overview update deferred：这是现有问题的伴随源校准。

## Agent self-audit triage

- **P0: none identified**。公开入口确实返回身份已核的PDF；下载器OA分类未采用，未改凭据或绕验证。
- **P1 / PT15-4**：严格区分选带、均值范围与图示低组删点；缺原始mask，不断言复现/偏差显著性或作者错误。
- **P1 / PT15-5、6、8**：模型γ/axis与未来寿命验证分开；不给Pr136补frame或新实验结论。
- **P1 / PT15-9**：下一派生J^(2)须固定相邻线身份与ΔI；绝对自旋未定不等于可忽略顺序。
- **P2**：citation key与raw保留槽显式报告；出版商下载归属信息不作为科学证据写回。

## Extracted Pages

- Observables: [[moments-of-inertia]]
- Concepts: [[triaxial-deformation]]
- Related source: [[lv-2025-136pr-tac-covariant-density-functional]]

## Provenance

- [DOI](https://doi.org/10.1088/0031-8949/90/11/114016)与[出版商PDF入口](http://stacks.iop.org/1402-4896/90/i=11/a=114016/pdf)：科学locator与版本。
- [阅读回执](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache2015-reading-audit.json)、[Table1算术](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache2015-table-crosscheck.json)、[access分类边界](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache2015-access-classification.json)。
