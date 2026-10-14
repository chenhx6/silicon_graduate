---
type: source
title: "符合模式下的 γ 射线各向异性度测量"
aliases: ["Zheng 2002 ADO", "Gamma-Ray Anisotropy Measurement in Coincidence Mode"]
created: 2026-09-20
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: method
reading_depth: deep-read
title_original: "符合模式下的 γ 射线各向异性度测量"
authors: ["郑勇", "周小红", "柳敏良", "刘忠", "何建军", "郭应祥", "雷相国", "张玉虎", "罗万居"]
journal: "高能物理与核物理"
year: 2002
volume: 26
issue: 9
pages: "909-913"
language: zh
canonical_source: "郑勇等. 符合模式下的 γ 射线各向异性度测量. 高能物理与核物理 26(9), 909-913 (2002)."
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/2002_郑 et al_符合模式下的γ射线各向异性度测量.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/2002_郑 et al_符合模式下的γ射线各向异性度测量.pdf"
raw_sha256: "03044180a59fa5be55bcb6c517e9b87285c0991855afe5e1104e9dd03e9a7f23"
nuclei: ["145Tb", "144Gd", "143Gd", "142Gd", "143Eu", "146Tb"]
observables: ["R_ADO", "gamma-ray-multipolarity", "angular-distribution", "detector-efficiency"]
methods: ["angular-distribution", "gamma-gamma-coincidence", "ADO", "dco-ratio"]
tags: [ado, coincidence-mode, gamma-ray-anisotropy, multipolarity, detector-efficiency, 145Tb]
---

# 符合模式下的 γ 射线各向异性度测量

## Bibliographic Record

- 作者：中国科学院近代物理研究所郑勇等。
- 中文题名：符合模式下的 γ 射线各向异性度测量。
- 英文题名：*γ-Ray Anisotropy Measurement in Coincidence Mode*。
- 期刊：*高能物理与核物理* 26(9), 909-913 (2002)。收稿日期：2001-10-23。
- 原始文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/2002_郑 et al_符合模式下的γ射线各向异性度测量.pdf`；SHA-256：`03044180a59fa5be55bcb6c517e9b87285c0991855afe5e1104e9dd03e9a7f23`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF 物理页 1-5 全部视觉阅读；覆盖摘要、引言、ADO 原理与公式 (1)-(5)、`145Tb` 实验装置与效率修正、图 1/图 2、总结和参考文献。
- Not covered: 原始 `145Tb` γγ 矩阵、逐事件数据、探测器响应文件和参考文献正文；本论文只提供方法论文中的汇总结果。
- Coverage caveats: PDF 为扫描件，文本提取为空；关键公式、中文段落和图 1/图 2 通过页面视觉核对。ADO 阈值是该装置和校准条件下的结果，不能跨阵列直接移植。

## Paper Question and Scientific Motivation

- 论文问题：在重离子熔合蒸发实验中，如何由 γ-γ 符合数据构造 γ 射线各向异性度（ADO, angular distribution from oriented states）并据此判定跃迁多极性（摘要；PDF pp.1, 5）。
- 作者指出传统完整角分布需要固定探测器角度，DCO 需要选取多极性已知的开门跃迁；ADO 试图利用大、小角度探测器组的符合强度比，在减少束流时间和提高统计量的同时获得多极性信息（PDF p.1）。

## Method and Design Logic

- ADO 构造两组不对称符合矩阵：将 γ-γ 符合中一条 γ 射线按小角度组 `θS` 和大角度组 `θL` 分别作为纵轴，另一条 γ 射线作为横轴；门控 γ 射线的能量分别落入对应矩阵的 x 轴（PDF p.2）。
- 对待测 γ 射线 `γ1`、门控 γ 射线 `γ2`，效率修正后的比值为
  \[
  R_{\mathrm{ADO}}(\gamma_1)=
  \frac{I^{\theta_S}_{\gamma_2}(\gamma_1)/I^{\theta_L}_{\gamma_2}(\gamma_1)}
       {\varepsilon_{\theta_S}(\gamma_1)/\varepsilon_{\theta_L}(\gamma_1)}.
  \]
  论文进一步写成 `R_ADO(γ1)=[ω1(θS)/ω1(θL)] f_ADO`，其中 `f_ADO` 包含门控 γ 射线角分布和各角度探测效率的修正（PDF p.2，式 (1)-(5)）。
- 这一路线把“核的角分布/取向信息”和“探测器角度、效率、门控 γ 射线贡献”分开处理；`f_ADO≈1` 需要由实际阵列和门控能量范围验证，不能作为普适假设。

## Key Evidence and Reasoning Chain

1. 熔合蒸发残余核的角动量在垂直束流方向的平面内取向，γ 射线强度分布因而具有各向异性；这是 ADO 的物理基础（PDF p.1）。
2. `145Tb` 实验使用 12 套 BGO-HPGe 探测器，分为与束流夹角约 `±32°`、`±58°` 和 `90°` 的三组，每组 4 套；用 `152Eu` 和 `133Ba` 标准源作相对效率标定（PDF p.3）。
3. 以门控 γ 能量 `100-1500 keV`、步长 `50 keV` 计算 `f_ADO` 的偏离；四极门时最大偏差约 `5.2%`，偶极门时最大偏差约 `3.2%`（PDF p.3，图 1）。
4. 已知多极性跃迁的 `R_ADO` 与角分布/DCO 结果相符；该实验给出纯四极跃迁约 `1.25`、纯偶极跃迁约 `0.75`，M1/E2 混合跃迁位于两者之间（PDF pp.3-4，图 2）。
5. 作者据此认为，在探测器数量足够、效率修正受控的大型阵列上，ADO 可以较可靠地区分偶极和四极跃迁，并在统计量和处理未知开门多极性的灵活性方面优于传统 DCO（PDF p.4，总结）。

## Summary

这篇方法论文把 ADO 定义为符合模式下的大、小角度探测器组强度比，并显式加入门控 γ 射线角分布与角度依赖效率的修正。基于 `145Tb` 实验的 12 探测器、三角度组布局和标准源效率标定，作者计算 `f_ADO` 在所选角响应和已测效率下的最大偏离，偶极/四极门分别约为 3.2%/5.2%，并用已知跃迁的 ADO 结果与角分布、DCO 结果比较。该来源支持 ADO 的方法逻辑和一个具体阵列的可靠性边界，不支持把 `0.75/1.25` 阈值移植到其它阵列。

## Experimental or Theoretical Setup

- 反应/实验对象：`145Tb` 高自旋实验及邻近 `144Gd`、`143Gd`、`142Gd`、`143Eu`、`146Tb` 已知 γ 跃迁。
- 阵列：12 套 BGO-HPGe，四套一组，角度约为小角、中角、`90°` 大角；相对效率由 `152Eu`、`133Ba` 标定。
- 处理：γ-γ 符合矩阵、角组投影、效率修正、已知多极性参考线比较。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| Z02-1 | 论文定义了效率修正后的 `R_ADO(γ1)`，并将其分解为待测 γ 的角分布比和门控/效率修正因子 `f_ADO`。 | method-definition | direct | PDF p.2，式 (1)-(5) | false |
| Z02-2 | `145Tb` 实验的 12 套 BGO-HPGe 被分为约 `±32°`、`±58°`、`90°` 三个角度组，每组 4 套。 | experimental-fact | direct | PDF p.3 | false |
| Z02-3 | 作者用已测各组效率曲线和给定门控γ角分布，在门控能量100-1500keV范围计算f_ADO；正文报告最大偏离约四极门5.2%、偶极门3.2%，是修正偏离，非全部实验误差。 | method-calculation | direct | PDF p.3，图1与对应正文 | false |
| Z02-4 | 该实验中纯四极跃迁的 `R_ADO` 约为 `1.25`，纯偶极跃迁约为 `0.75`，M1/E2 混合跃迁位于两者之间。 | experimental-result | direct | PDF pp.3-4，图 2 | false |
| Z02-5 | 作者认为在本阵列和校准条件下 ADO 多极性判定与角分布、DCO 结果一致。 | author-interpretation | direct | PDF pp.3-4，总结 | false |
| Z02-6 | 式4给f_ADO=(C−ω2(θS)εS(γ2)/NS)/(C−ω2(θL)εL(γ2)/NL)，式5的C=Σg=S,M,L ω2(θg)εg(γ2)。εg是组效率之和，1/Ng来自不能与同一探测器自符合的修正；同组探测器效率不同时原式近似成立。 | method-definition | direct | PDF p.2，式2/4/5与式2后说明；PDF p.3，组效率说明 | true |
| Z02-7 | Fig1的f(Eγ2)用已测效率与给定ω2计算，正文取Eγ2=100–1500keV、步长50keV；正文5.2/3.2百分数不替代count、效率、alignment/feeding、背景和covariance的完整uncertainty。后半是本任务的使用边界。 | method-and-boundary | mixed | PDF p.3，Fig1和计算说明 | true |
| Z02-8 | 作者明确以145Tb高自旋实验Ref3为例，Fig2的145Tb及邻核参考线来自该实验所获数据；Ref3为Zhou/Zheng/Zhang et al., EPJA12,253–255(2001)。2002方法文与对应实验引用不能重复计独立采集。 | source-lineage | direct | PDF p.1末段；PDF pp.3–4，Fig2/参考文献3 | true |

## Nuclear Structure Information

- 本文的主要对象是 `145Tb` 高自旋 γ 谱学；它不建立新的能带页，而是为 `145Tb` 和邻核已知跃迁提供多极性判别方法边界。
- ADO 的 `R_ADO` 参考区域是阵列、角度组、效率和门控条件共同决定的观测量；`0.75` 与 `1.25` 只作为该实验的局部参考。

## Authors' Interpretation

- 作者解释：ADO 通过符合矩阵中多个探测器组合获得更大的统计量，并减轻 DCO 对已知多极性门控跃迁的依赖。
- 作者把 `f_ADO` 的数值偏离和已知跃迁交叉验证作为方法可靠性的证据；这是方法验证，不等于所有阵列的通用精度证明。

## Model Results

- 不适用。本文没有独立核结构模型计算；其核心是实验几何、效率修正和多极性方法验证。
- 这里“不适用”指无独立核结构模型，不意味着没有计算量：f_ADO和Fig1是给定angular distribution及已测efficiency下的仪器/门控计算，需与Fig2的已知跃迁验证分开。

## Competing Interpretations and Limitations

- 主要方法限制：如果角度组探测器数量不足、相对效率曲线不匹配、门控 γ 的多极性/角分布未受控，`f_ADO` 不一定接近 1。
- `R_ADO` 的偶极/四极区域会受阵列几何、能量、门控条件、取向和 feeding 影响；不能把本文数值当作跨实验固定阈值。
- 与 DCO 的比较是本论文所选阵列和已知参考跃迁下的比较，不能推出 ADO 在所有实验条件下都优于 DCO。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-Z02-1 | Core reconstruction | ADO 是角度组强度比加门控/效率修正；其“可靠”依赖 `f_ADO` 的阵列特定验证。 | PDF p.2 式 (1)-(5)，pp.3-4 | self-checking |
| AR-Z02-2 | Assumptions and dependencies | 依赖角组响应、相对效率、门控 γ 角分布和已知多极性参考线；不能只从比值定义中消除这些依赖。 | PDF pp.2-3 | self-checking |
| AR-Z02-3 | Transfer conditions | 可迁移的是修正流程和验证思路；`R_ADO≈0.75/1.25` 只能在匹配阵列和校准条件下迁移。 | PDF pp.3-4 | provisional |
| AR-Z02-4 | Failure conditions | `f_ADO` 偏差过大、角度组统计不足、效率响应不匹配或门控跃迁存在未知 multipolarity 时，多极性分类会失真。 | PDF pp.2-4 | active-L3 |
| AR-Z02-5 | Reverse/falsification test | 用同一阵列的独立已知 M1/E2/E2 参考线重建 `f_ADO`，并与角分布/DCO/偏振交叉比较；若参考线不能分群，ADO 阈值不能用于新线。 | PDF pp.3-4；可迁移检验 | candidate-L3 |
| AR-Z02-6 | Research-question decision | 本文应更新 ADO 方法页，作为 `σ/I`、feeding 和阵列 response 边界的早期中文方法来源；不单独启动 L4。 | PDF pp.1-4 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 ADO/角分布定义、阵列特定阈值和 `σ/I`/feeding 边界，但缺少这篇中文方法论文的原始公式、`f_ADO` 修正和 `145Tb` 装置验证。
- Effect of this source: `supports` and `methodological-bridge`。
- Reason: 来源直接补充 ADO 公式、效率修正因子和一个具体阵列的误差/参考值，强化“阈值不可跨阵列复用”的现有认识。
- Persistence decision: update `knowledge/methods/angular-distribution.md`; source page retained for locator-level evidence。
- Review state: `unreviewed`; direct method claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[angular-distribution]] | 为 ADO 的公式、角组效率修正和阵列特定参考值提供中文原始方法来源。 |
| methodological-bridge | [[dco-ratio]] | 直接比较 ADO 与 DCO 的门控依赖、统计组合数和未知跃迁适用边界。 |
| supports | [[spin-parity-assignment]] | 多极性判定可作为自旋宇称赋值的一个证据输入，但不能独立闭合赋值。 |

## Human Review Triage

### P0

- Z02-P0-1：`R_ADO≈0.75/1.25` 及 `f_ADO` 的 3.2%/5.2% 偏差必须限定在 `145Tb` 文章的阵列和效率条件；跨阵列使用前需重新标定。

### P1

- Z02-P1-1：ADO 对未知开门多极性的实际优势需要结合其它阵列和独立参考线核验；不能把本文作者结论扩写成普适优越性。

### P2/P3

- 扫描件文本层不可用；页面视觉核对已覆盖公式和图表，后续若论文写作需要逐字引用再做局部高分辨复核。

## Extracted Pages

- Nuclei: `145Tb`、`144Gd`、`143Gd`、`142Gd`、`143Eu`、`146Tb`（方法验证对象）。
- Bands: 不创建。
- Concepts: 关联 ADO、取向态角分布和 multipolarity assignment。
- Methods: 更新 [[angular-distribution]]。

## Non-source Notes and Follow-up

- 下一步：将 `Z02-1` 至 `Z02-5` 的公式和局部阈值写入 `knowledge/methods/angular-distribution.md`，同时保留阵列特定边界。
- 该来源的 `145Tb` 实验不是本 Wiki 中已有某一条 `145Tb` source 的替代；若后续发现同一实验原始论文，需按 lineage 关联而非重复计数。

## Day15 无学分预习：定义、归一与原始阅读

在Day14运行内先保存primed来源前回忆，再核rawhash并视觉读全5页（p1动机、p2 Eq1–5、p3 efficiency/Fig1、p4 Fig2/总结/ref、p5英文abstract）。这是恰好下一张Day15的preview，day_index仍14，不提供formal Day15 card credit。原Z02-1–5的needs_review状态不清除；新增定义/谱系条目true。

Raw扫描件无text layer，未用OCR填式子。原式精确分开targetγ1效率与gateγ2效率/角分布；1/NS、1/NL作用于组响应而非再除一次target group效率。两角计数和target效率比只能求R_ADO；f还需独立本征ratio或Eq4/5门控response，见[[angular-distribution]]“ADO计算单：额外输入、self-exclusion与误差”。

本次条件worksheet与group/individual展开、heterogeneity失败控制和误差图是任务推导，不是论文给出的原始145Tb counts。等权32/58/90对P2/P4的近似抵消也只是任务的解析观察，作者没有在本文明说该设计意图。

外部有界metadata查找未匹配本2002文的exact title，不用异文DOI补空字段；raw header身份仍有效。Ref3的Crossref metadata匹配“In-beam study of145Tb”、作者、EPJA12,253–255(2001)，DOI10.1007/s100500170001；未取得其primary全文，不追加article-specific数据。另有[[zheng-2004-high-spin-145tb-157yb]]的12-detector/145Tb谱系线索，未在本段认证event-list同一性或把thesis的不同参考数值合并为普适阈值。

### Agent self-audit triage — preview

- P0科学：Z02-6的组/单探测器efficiency convention、Eq3乘f方向、Z02-7的calculated deviation与experimental error区分已回raw核；无technical hard P0。
- P1：group formula要求within-group response近似；γγ joint response的factorization、reference gate和finite acceptance仍需actual数据。Z02-8只有明确publication依赖，不补event-ID。Source阈值不移植至193Bi。
- P2：方法/worksheet/图已回链；P3：没有human-review、Zotero/Bib改写、raw写入或Day15学分。
