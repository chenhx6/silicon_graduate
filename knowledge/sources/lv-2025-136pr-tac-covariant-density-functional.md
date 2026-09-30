---
type: source
title: "Lv et al. 2025 - Configuration-dependent shapes and rotations in 136Pr"
aliases: [Lv 2025 136Pr TAC-CDFT study]
created: 2026-09-30
updated: 2026-09-30
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Configuration dependent shapes and types of rotations in the gamma-soft 136Pr nucleus revealed by detailed calculations with tilted axis cranking covariant density functional theory"
authors: [B. F. Lv, C. M. Petrache, Y. K. Wang, P. W. Zhao, J. Meng, J. G. Li, et al.]
journal: Physical Review C
year: 2025
volume: 111
pages: 014321
doi: 10.1103/PhysRevC.111.014321
arxiv:
language: en
canonical_source: "https://doi.org/10.1103/PhysRevC.111.014321"
zotero_item_key: ""
citation_key: ""
zotero_uri: ""
library_file: ""
raw_file: "raw/papers/gpt/day3-mean-field-20260929/136pr-2025-tac-cdfTAC/PDFs/Configuration_dependent_shapes_and_types_of_rotations_in_the_gamma-soft_Pr-136_nucleus_revealed_by_detailed_calculations_with_tilted_axis_cr.pdf"
raw_sha256: c8e14461975a7606d7e38325d6e83b500e75d232027b118743e1f1ff754537d6
nuclei: [136Pr]
reactions: ["100Mo(40Ar,1p3n)136Pr"]
experiments: [JUROGAM-II-136Pr-2025]
models: [tilted-axis-cranking, covariant-density-functional-theory, shell-model]
observables: [level-scheme, RDCO, Rac, B(M1)/B(E2), angular-momentum-alignment]
methods: [gamma-gamma-coincidence, directional-correlation, two-point-angular-correlation]
tags: [a130, 136pr, gamma-softness, tac-cdft, high-spin, configuration-assignment]
---

# Lv 等（2025）：136Pr 高自旋谱学与 TAC-CDFT 组态比较

## Bibliographic Record

Lv et al., Physical Review C 111, 014321 (2025), DOI [10.1103/PhysRevC.111.014321](https://doi.org/10.1103/PhysRevC.111.014321). 本地文件是 Jyväskylä 大学仓储的作者接收稿，来自 [该校开放仓储 PDF](https://jyx.jyu.fi/bitstreams/c9c701b4-dab3-4b19-8a3f-2aa95d467942/download)。Crossref DOI 元数据与接收稿首页题名、作者、卷和文章号一致。接收稿说明其分页与排版可能不同于正式出版版；以下定位均注明为本地 PDF 页。

## Scope and Reading Depth

- 已读正文主线，并核查 Fig. 1 能级纲图、Table I 的跃迁/强度/角关联数据、TAC-CDFT Figs. 6–16、Table II 组态与形变、摘要和结论。
- 覆盖重点：136Pr 新 JUROGAM II 高自旋谱、各带的角动量对齐与组态比较、pairing collapse、模型与数据不一致处、作者提出的竞争解释。
- 未覆盖：重新分析事件数据、重跑 TAC-CDFT/壳模型代码、与原始事件级数据或计算输入协方差做独立比较。
- 本次只获取主文。相关方法、数据表和图均在主文；目前没有发现依赖 SI 才能判读的关键输入或结果。
- 主张均保留 needs_review: true，本页仍为 unreviewed；模型输出不作实验事实。

## Summary

The paper combines a new high-statistics JUROGAM II 136Pr level scheme with PC-PK1 tilted-axis-cranking covariant density functional theory and a large-scale SN100PN shell-model discussion. It offers a direct modern model application to the same Hara Table 5 candidate, but it is not a projected-shell-model calculation and its configuration, deformation and mode assignments remain model-mediated.

## Active Recall Before Opening the Full Text

开全文前的记忆是：136Pr 为 Z=59,N=77 奇奇核；Hara–Sun Table 5 的星号是轴对称 PSM 拟合失败后的三轴候选。TAC-CDFT 应给旋转系下的角动量、组态和形变响应，但不能恢复总角动量好量子数。未知点包括 2025 计算是否真的使用角动量投影、D4/D6 是否是同一形变、对实验跃迁强度的拟合是否一致，以及弱连线是否独立确定宇称。原文核对后确认：这是同一核素的自洽 TAC-CDFT/壳模型研究，不是角动量投影；D4/D6 仍保留替代解释，Q1 宇称依赖模型推断。

## Experimental or Theoretical Setup

- 实验直接报告：100Mo(40Ar,1p3n)136Pr，40Ar 束流能量 152 MeV，JUROGAM II；作者报告采集 5.1×10^10 个三重及更高折符合事件，当前 136Pr 数据统计约为此前一项该核实验的 240 倍（摘要、Sec. II，本地 PDF pp. 2–3）。
- 自旋宇称判据：强跃迁使用方向相关比 RDCO；弱跃迁使用两个角度组的 Rac。Table I 给出 γ 线能量、相对强度、RDCO/Rac、多极性和能级指派（Table I，本地 PDF pp. 6–9）。
- TAC-CDFT：使用 PC-PK1，三维谐振子基底 10 个主壳，Bogoliubov 变换与有限程可分离配对力；若带头配对关联为零，作者对该带后续态关闭 Bogoliubov 配对。作者称 calculation 没有额外调参。正文明确讨论了粒子数投影可能避免 pairing-collapse jump，但未在本工作中实现（Sec. III.A，Fig. 6，本地 PDF pp. 9–10）。
- 另用 SN100PN 有效相互作用进行大空间壳模型计算，重点理解 D5 及其衰变到的正宇称低能态；作者指出实验与计算态之间难建立唯一对应（Sec. III.B，本地 PDF p. 13）。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV25-1 | 新 JUROGAM II 数据确认并扩展 136Pr 高自旋谱；论文图 1 给出 595-keV、Iπ=6+ 异能态以上的 D1–D6、Q1–Q4 能级纲图。 | experimental-fact | direct | Abstract; Sec. II; Fig. 1, PDF pp. 2–4 | true |
| LV25-2 | Table I 报告跃迁能量、初态能量、相对γ强度、RDCO、Rac、多极性和自旋宇称指派；相对强度以 209.5-keV 7+→6+ 跃迁归一。 | experimental-fact | direct | Table I, PDF pp. 6–9 | true |
| LV25-3 | Q1 的 875.6(4)-keV 连接跃迁测得 RDCO=0.47(8)，与拉伸偶极跃迁的标定值相符；其相对强度 2.9(2)，偏振分析因低计数和污染未能确定宇称。 | experimental-criterion | direct | Sec. II, PDF p. 3; Table I, PDF p. 9 | true |
| LV25-4 | TAC-CDFT 使用 PC-PK1、10 个谐振子主壳及 Bogoliubov 配对；本工作不实施角动量或粒子数投影。 | synthesis | direct | Sec. III.A, PDF p. 9 | true |
| LV25-5 | Table II 的组态和 (β,γ) 是 TAC-CDFT 模型输出；D1/D2/D3/D4/D6 与 Q1/Q2/Q3/Q4 的带头形变约跨 β=0.16–0.24、γ=17°–39°。 | model-result | direct | Table II; Fig. 16, PDF p. 15 | true |
| LV25-6 | D1 的计算能量趋势接近实验，但计算 B(M1)/B(E2) 高于从所报告分支比得到的实验派生值。 | model-result | direct | Fig. 6; Sec. III.A, PDF pp. 9–10 | true |
| LV25-7 | D2 的计算 B(M1)/B(E2) 显著低于实验派生值；D3 的预测比值远高于 D1/D2。 | model-result | direct | Figs. 7–8; Sec. III.A, PDF pp. 10–11 | true |
| LV25-8 | TAC-CDFT 没有找到可描述 D5 的组态；作者随后使用 SN100PN 大空间壳模型讨论 D5 及其衰变到的部分低能态。 | model-result | direct | Sec. III.A–B, PDF pp. 11–13 | true |
| LV25-9 | 作者未在目标数据中识别手征转动、wobbling 或 oblate rotation；D4/D6 被讨论为可能磁转动，或作为另一种 D4 偏 prolate、D6 偏 oblate 的形状共存方案，二者是竞争解释。 | author-interpretation | direct | Sec. III.A–C; Figs. 9–11; Summary, PDF pp. 10–15 | true |
| LV25-10 | 2025 年模型计算与实验谱来自同一篇论文的同一 JUROGAM II 数据集，因而模型拟合不是独立实验确认；作者称新数据统计约为此前该核实验的 240 倍。 | synthesis | direct | Sec. II; Figs. 6–16; PDF pp. 2–15 | true |
| LV25-11 | 本次 arXiv、Crossref、OpenAlex、Semantic Scholar 和 INSPIRE 的限定检索未找到 136Pr/137Pr 的直接三轴 PSM/TPSM 全文；检索到并获取的 136Pr 2025 研究是 TAC-CDFT/壳模型，不是角动量投影。Google Scholar HTML 路由卡住并终止，故该路由未验证，检索不构成“文献不存在”的证明。 | our-inference | contextual | Day 3 bounded search record, 2026-09-30 | true |

| LV25-12 | 作者依据 TAC-CDFT 构型为 Q1 提出正宇称；该正宇称并未由本次偏振测量确定。 | author-interpretation | indirect | Sec. II, PDF p. 3 | true |
| LV25-13 | D1 的 TAC-CDFT 总角动量曲线在旋转频率约 0.35 MeV 附近因配对塌缩出现突跳；粒子数投影虽被提及可避免此非物理塌缩，但本研究未实施。 | model-result | direct | Fig. 6; Sec. III.A, PDF p. 10 | true |
| LV25-14 | D3 的带内交叉 E2 跃迁未观测到，因此该带实验 B(M1)/B(E2) 只能给出下限。 | experimental-fact | direct | Fig. 8; Sec. III.A, PDF p. 11 | true |
| LV25-15 | 作者把 D5 未找到 TAC-CDFT 组态视为近球形形变的间接线索，同时提醒 TAC-CDFT 在该形状区可能不适用。 | author-interpretation | direct | Sec. III.A–B, PDF pp. 11–13 | true |
## Nuclear Structure Information

实验报告以 595-keV、Iπ=6+、T1/2=90 ns 异能态为基准的复杂高自旋结构。Fig. 1 显示 D1–D6 偶极带和 Q1–Q4 四极带；D3 为新观测带，原先一条高自旋带在本次分析中分为 D5、D6。Table I 的多极性由 RDCO/Rac 等约束，但若干高自旋指派仍带括号。

## Model Results and Authors' Interpretation

- TAC-CDFT 给出每条带的旋转系能量、总角动量、对齐、构型和形变；Table II 与 Figs. 6–16 是模型结果，不是直接测量的 β、γ 或轨道占据。
- D4/D6 的自洽最佳组态分别含不同 h11/2 质子 Ω；作者另保留磁转动与 prolate/oblate 三轴形状共存两种解释。
- Q1 正宇称没有由偏振测量确立，而由模型帮助选择；不得把模型给出的宇称或构型标签并入实验事实。
- 文章讨论的是本次 136Pr 谱学和 TAC-CDFT/壳模型，不是 projected-shell-model 重算，也不恢复良好总角动量。

## Competing Interpretations and Limitations

- The authors leave D4/D6 as either possible magnetic rotation or a prolate/oblate triaxial shape-coexistence scenario; neither alternative is independently established by the calculated deformation table.
- D1 calculated B(M1)/B(E2) values are above the experimental derived values, D2 values are below them, and TAC-CDFT does not find a configuration for D5. These model-data limits prevent treating the overall reasonable energy fit as a unique configuration proof.
- Q1 positive parity is proposed with TAC-CDFT support after polarization analysis of the weak 875.6-keV link was inconclusive.
- Pairing collapse, omitted particle-number projection and absence of total-angular-momentum restoration limit the mean-field comparison.

## Counter-Evidence and Missing Companion Observables

- 对唯一解释的反证来自模型自身：D1 与 D2 的 B(M1)/B(E2) 偏差方向相反，D5 没有匹配 TAC 组态；pairing collapse 与未做粒子数投影也限制高自旋解。
- Q1 的 875.6-keV 跃迁只支持偶极性质，偏振因低计数与污染不能确定宇称；需更高统计且可控污染的线偏振/角关联测量。
- D4/D6 的模型竞争需要 partner-resolved lifetime、绝对 B(E2)/B(M1) 或 Qt，以及独立形状敏感观测来区分磁转动与形状共存。
- Table II 中形变与 Fig. 16 采用的坐标表示和正文“γ<0°/γ>0°”替代方案还需按作者具体轴约定作进一步复核；当前不将两种解释合并。

## Related Knowledge and Project Relations

- [[136pr]]：核素级实验能级、观测判据和竞争解释汇总。
- [[hara-sun-1995-projected-shell-model-high-spin]]：HS10-4 将 136Pr (N=77) 列为 “presumably triaxial” 候选；它是旧轴对称 PSM 的模型推断。
- [[a130-model-choice-card]]：区分 136Pr TAC-CDFT/SM 应用和 TPSM 投影覆盖计数。
- [[tilted-axis-cranking]] 与 [[covariant-density-functional-theory]]：TAC-CDFT 方法输入、输出与 projection 边界。

## Knowledge Impact and Learning Decision

Decision: revises. 136Pr 从“后续投影覆盖待查”更新为“已有 2025 直接核素 TAC-CDFT/SM 与新实验谱学；尚非 PSM/TPSM 投影复算”。它加强了模型对这一候选核的可比较性，但不能把模型形变或模式解释升级为实验形状事实。

## Human Review Triage

- P1：核对 Q1 宇称是否在后续实验中得到独立验证；保持 LV25-3 的实验事实与模型指派分层。
- P1：复查 Table II、Fig. 16 和 D4/D6 替代形状方案的 γ 轴/转轴约定，不能把二者写成已决形状共存。
- P2：粒子数投影未实施；D5 的模型归类仍依赖较不唯一的大空间壳模型对应。

## Extracted Pages

- Nuclei: [[136pr]]
- Models: [[tilted-axis-cranking]], [[covariant-density-functional-theory]], [[cranked-shell-model]]
- Projects: [[a130-model-choice-card]]
