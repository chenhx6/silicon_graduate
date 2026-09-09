---
type: system-workflow
graph-excluded: true
operation: ingest-strategies
updated: 2026-07-16
---

# INGEST STRATEGIES：运行时短规则

本文件是普通文献摄入默认读取的短规则。详细 workflow 教程、策略说明、长示例、复杂案例和历史说明见 [ingest-strategies-detail.md](ingest-strategies-detail.md)。普通单篇摄入不默认读取 detail；detail 不是 PDF reading depth，不读取 detail 不得降低 PDF 阅读深度。只有用户要求解释策略、修改 workflow、短规则不足以判断、要求 detailed workflow recap / detailed strategy-policy audit，或明确要求查阅详细教程时才读取。

## 运行时共同规则

1. 只记录文中实际存在且可定位的信息，不为填满清单而编造。
2. 默认保持深度文献读取；优化目标是减少启动、扫描、QMD 和复盘固定开销，不降低 evidence quality。
3. 每条 key claim 尽量给出 page、section、figure、table、equation、caption、level scheme、spectrum 或具体段落等 locator。
4. 区分 observed fact、experimental criterion、model result、author interpretation 和 Wiki synthesis。
5. 需要人工核对的 claim 保留 `needs_review: true`；页面级 `human-reviewed` 与 claim-level `needs_review` 独立。
6. 不修改 raw PDF、论文、数据、图片或 `raw/zotero/wiki-inbox.bib`；不新增 Skill、automation、脚本或调度器。
7. 普通摄入不修改 lint 脚本、lint 配置或测试；若认为必须修改，停止并询问用户。
8. 普通文献摄入默认由 Agent 完成逐 claim 自审；长任务可保留单一 rolling `WIP ingest:`，完成且无未隔离 hard P0 时 amend 为 final，并按仓库持续 commit/push 授权自动发布。Agent 自审不改变 `unreviewed` / `needs_review`；用户明确禁止 push、禁止任何本地 commit 或要求先审核时按该覆盖指令执行。
9. 普通单篇摄入不强制 QMD embed；可把 QMD refresh 写为 deferred，并说明原因与建议补跑时机。
10. 普通单篇摄入不默认更新 `knowledge/overview.md`；overview 是阶段性地图。
11. 只做与本轮任务直接相关的最小同步；有帮助但非必要的优化只列建议。
12. 标准深入阅读必须做简短 Knowledge Impact and Learning Decision：说明来源对既有 Wiki 认识是 supports、limits、revises、conflicts 还是 no material change，并选择 source-only、project、synthesis、provisional research-note 或 overview 的持久化落点；不要求长篇填写或机械创建页面。
13. Related Knowledge / Project Relation 只为重要关系使用 `supports`、`limits`、`conflicts`、`foundational-background`、`methodological-bridge`、`competing-interpretation`、`retrospective-connection` 或 `not-direct-evidence`，并附具体说明；普通 Wiki 链接无需类型化。

## 默认读取清单

普通文献摄入默认读取：`AGENTS.md`、`system/workflows/ingest.md`、本文件、`system/evidence-policy.md`、`system/paper-evidence-gate.md` 和 `check.md`。不默认读取 `ingest-strategies-detail.md`。

## 普通单篇与多篇摄入

普通单篇摄入指：一篇目标文献、明确 PDF 路径、明确 BibTeX key、明确摄入策略、明确研究主题、明确 project 关系，且不要求跨文献综合、修改 workflow、解释摄入策略、detailed workflow recap 或 detailed strategy-policy audit。不默认读取 detail 教程只表示不读取长 workflow 教程，不表示降低 PDF 阅读深度；PDF 阅读深度由 source note 的 `reading-depth` / evidence-reading 状态决定。

多篇摄入不自动等于复杂摄入。若用户要求逐篇摄入，按顺序一篇一篇完成；每篇都必须有独立 source note、claim kind、locator、needs_review、project relation、source-level / claim-level 审核重点和 P0/P1 triage。不得因为多篇在同一提示词出现而合并成粗略批处理。只有多篇之间需要跨文献比较、冲突证据判断、project/synthesis 大综合、策略选择不明确，或用户要求 detailed strategy-policy audit 时，才读取 detail 教程。

## Thematic batch REFLECT

在多篇摄入任务中，同一任务连续摄入至少三篇直接相关来源、形成明确的理论/实验/方法主题阶段，或新来源可能改变 project/synthesis 证据结构时，在自然主题阶段结束处执行一次批次级 REFLECT；不必等待整个大批次完成。单篇重要来源只执行 Knowledge Impact，不因其可能改变 project/synthesis 而单独触发 batch REFLECT。对“核心研究论文 + 后续宽泛综述”的批次，核心论文阶段结束后先 REFLECT，综述完成后再判断是否补充或修正，不得用尚未完成的宽泛综述推迟已经成熟的核心主题综合。

REFLECT 应产生跨来源认识，而不是拼接逐篇摘要，并至少检查：

1. 理论、实验或方法的演化谱系；
2. 各来源的假设、适用条件和失效边界；
3. supporting、limiting 和 conflicting evidence；
4. 竞争解释及区分它们所需的观测量或检验；
5. 对现有 project/synthesis 认识的影响；
6. 是否需要 project、synthesis、provisional research-note 或 overview 更新；
7. 若不持久化综合结果，记录 no-persistence decision 和具体原因。

不机械创建页面，不要求固定篇幅、固定数量的研究问题、竞争解释或 reverse tests，也不重复抄写逐篇 source 已经完成的内容。

## PDF staged evidence reading

Staged evidence reading 是阅读顺序优化，不是降低摄入标准。用户模式的 canonical 定义见 `ingest.md`；用户未指定时采用标准深入阅读模式。`reading_depth` 只记录实际完成状态，不与三种模式一一映射；来源页必须同时说明 covered scope 与 not covered。

1. 建立论文主线：title、abstract、introduction、conclusion/summary，判断研究问题、对象核区、方法、主结论和 topic 关系。
2. 建立结构地图：识别 sections、experiment/theory/method/results/discussion 边界，以及 figures、tables、equations、appendix、supplemental references。
3. 深入读取关键证据：围绕 key claims 阅读 method/results/discussion、figures/tables/equations/captions，重点核查 transition、spin/parity、multipolarity、mixing ratio、ADO/DCO、polarization、lifetime、B(E2)/B(M1)、wobbling energy、model parameters、PES、calculated spectra 等高风险内容。
4. Claim 与 locator 回查：每条 key claim 回查 locator；locator 不确定且影响核心判断时保留 `needs_review: true`。
5. Project/synthesis 关联：任务要求 project-ingest 时才把证据接入相关 section/evidence matrix/evidence gap；active summary 只作导航，不替代 source locator。
6. 执行余量不足时 safe suspend，说明已读范围、未读 section/figure/table/locator 和下一轮继续提示词，不得降低核心读取标准。

## 策略短定义

- `review-ingest`：综述、历史框架或领域背景；抽取 scope、topic map、terminology、review-level synthesis、follow-up original sources；不得把二手转述写成原始证据。
- `experiment-ingest`：原始实验论文；抽取 reaction、detector、level scheme、transitions、spin/parity、multipolarity、DCO/ADO、polarization、lifetime、strength ratios、author interpretation 和 limitations。
- `theory-ingest`：理论或模型论文；抽取 model assumptions、Hamiltonian/equations、parameters、calculated spectra/observables、comparison with experiment 和 model limitations。
- `method-ingest`：方法、装置或分析技术；抽取 measured quantity、geometry、formula/ratio、gating/normalization、uncertainty 和 applicability。
- `targeted-ingest`：只查用户指定问题、图表、公式或局部章节；必须标明未覆盖范围，不伪装成全文摄入。
- `project-ingest`：为特定 project 或研究问题摄入；记录 source contribution、supporting/counter/alternative evidence、evidence gaps、data-analysis bridge 和 innovation candidate notes。
- `daily-ingest`：1-2 篇或小批量；每篇单独判断策略、单独列 P0/P1，不为数量牺牲 locator 或 claim kind。
- `claim-review-update`：只按用户审核报告修改明确 source/claim/project；页面级审核不自动清除 claim-level `needs_review`。
- `data-analysis-bridge`：接入用户数据处理结果；分开 user-provided data facts、analysis outputs、possible/competing interpretations、innovation candidates 和 paper-level candidates。

## Project / synthesis active summary

大型 project 或 synthesis 可维护短的 `Agent active summary` / `Active summary for agents`。普通摄入优先读取 active summary 和相关 section，不默认全文读取大型页面。Active summary 只能帮助定位、判断相关 section 和减少启动开销，不得替代 source locator、project/synthesis 主体或原文证据。

如果本轮实际修改 project/synthesis 主体、添加 evidence row/source relation/evidence gap/next action，必须同步最小更新该页 active summary；若页面没有 active summary 且本轮实际修改该页，应创建短 summary。用户明确要求更新 project/synthesis 时，不得只改 active summary。只有正式 project-level synthesis / cross-project synthesis 才默认完整读取相关 project/synthesis。

## Overview 阶段性更新

普通单篇文献摄入不默认更新 `knowledge/overview.md`。以下情况建议更新：多篇文献批量摄入完成；新建或显著更新 project；新建或显著更新 synthesis；主题知识地图发生结构性变化；用户明确要求；paper evidence gate 或 major concept map 变化。

若本轮不更新 overview，最终复盘写明 `overview update deferred`、deferred reason 和建议何时更新。`knowledge/index.md` 可做最小索引更新，但不得扩写成综合性 overview。若 overview 加入科学判断、跨文献总结或争议判断，Human review triage 至少列为 P1；低风险统计或导航更新列为 P2/P3。

## Human review triage

P0/P1 是复盘重点，不把所有 `needs_review` 等权重铺开；但科学风险不能因展示预算被隐藏。

- `P0`：无总量硬上限。每项必须给出实际判断、文件、section/claim ID、source locator、grounded evidence、Agent inference、为什么重要、用户检查什么和不审核的风险。可按认知负担分批继续或 safe suspend，但完整 P0 队列必须保留，不得聚合隐藏、降级、删除或直接晋升。
- `P1`：允许软性展示预算和按文件分组，但每个重要判断仍须显示 evidence、Agent inference 与审核目的，不能退化为纯文件名列表。
- `P2/P3`：按文件或内容类型聚合；低风险 index/overview/handoff/log 与科学 claim 分开。
- 没有 P0 时写 `P0: none identified`。
- Source-specific triage 必须持久化到对应 source 页面，不得只保留在聊天或最终报告；页面直接引用本节定义，不复制第二套分级规则。Human Review Notes/Human Review Record 只在用户批注或审核事件真实发生后加入。
- 若 P0 较多，当前轮说明本批范围和后续未审 P0 队列；“精力有限时建议先看”只决定顺序，不改变总清单。

## Compact final recap

普通 ingest / project / synthesis 最终复盘默认结构：

1. Result status：completed / partial / safe suspend；commit hash；是否 push；是否存在未提交文件。
2. Files changed：只列关键文件；index/overview/handoff/log 可聚合说明。
3. Human review triage：按完整 P0、可分组 P1、聚合 P2/P3 输出。
4. Checks：`git status --short`、`git diff --stat`、`git diff --check`、wiki_lint 结果。
5. Next action：用户下一步审核什么；partial 时给继续提示词。

除非用户要求 detailed workflow recap，普通最终复盘建议控制在 400-900 中文字。commit/push 状态必须醒目；未 push 写 `not pushed`，已 push 写 commit hash 和 branch。
