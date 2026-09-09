---
type: system-workflow
graph-excluded: true
operation: reflect
updated: 2026-08-06
---

# REFLECT：综合与反向检验

本 workflow 在授权写入任务中默认承担 L2 研究学习闭环；活跃 L3/L4 的自主选题、假设循环和数据分析状态由 `autonomous-research.md` 负责，本文件只维护证据矩阵、反向检验、research-note 与 project/synthesis 晋升边界。

## Stage 0：反证优先

在形成结论前主动寻找：

- 与目标解释不一致的跃迁、寿命或强度行为；
- 支持替代模型的计算或实验；
- 不满足判据前提的情况；
- 同一实验数据的不同解释；
- 来源之间并非独立的证据链。

对每个高风险主张固定追问：

1. 主张成立时最小必要的 companion observable 是什么？
2. companion 是否被观测到？
3. 若未观测，是否有足够的统计、效率、gate、分辨率和 binning 灵敏度把它视为反证？
4. 是否存在更简单的背景、选择偏差或谱线混淆解释？
5. 哪个新结果会触发 belief revision？

“Expected-but-absent” 先写成 conditional contradiction，不直接写成已证伪。

导师 comment 或审稿意见可作为高价值 external counter-argument；在未读取其底层原始来源前，不得写成独立核验事实，但也不得隐藏它可能改变核心判断的价值。

未找到反证时，写明“未找到”而不是“没有反证”。

## Stage 1：证据矩阵

建议按下表组织：

| 主张 | 支持证据 | 反证/限制 | 替代解释 | 来源独立性 | 当前置信度 | 必要伴随预测（可选） | 当前观测/缺失状态（可选） | 缺失的灵敏度条件（可选） | Falsifier（可选） | Belief revision 触发条件（可选） |
|---|---|---|---|---|---|---|---|---|---|---|

对 wobbling、chiral doublet、γ-soft/γ-rigid 等主题，不能省略“替代解释”和“判据前提”。

## Stage 2：深度综合

- 完整读取关键来源页，必要时回到 raw 原文；
- 识别哪些是观测，哪些是解释；
- 说明模型依赖、参数依赖和约定；
- 使用 `system/templates/synthesis-template.md` 写入综合页。

## Stage 2.2：认识修正与晋升

Project 用于承载特定研究问题下的证据组织、候选解释和决策状态；synthesis 用于承载具有跨任务复用价值、证据边界清楚且经过相称审核的跨来源综合。只有新证据真实改变证据矩阵、解释强度、适用条件或开放问题时才更新这些页面，不因每篇新文献机械重写。

重用旧 project/synthesis 时，只对本轮实际使用且确有必要的部分做最小 on-touch migration；仅有格式差异不触发机械重写，不批量补历史字段或转换旧 Personal Notes。任何新的科学判断、竞争解释、结论或状态变化继续进入 Human review triage。

暂定研究推理、迁移假设、反向检验和认识修正候选不得直接写成正式 project/synthesis 结论。晋升时至少记录：此前认识、新认识、触发证据与 locator、支持/冲突来源、关键假设、仍存不确定性、Human review 结果和晋升目标。被修正、拒绝或取代的认识保留简短 history，不静默删除。

### Research-note 创建与生命周期

在用户已授权的 ingest、reflect、project 或 synthesis 写入任务中，Agent 只有在暂定推理满足至少一项持久化门时才可创建 `knowledge/research-notes/` 页面：具有明确跨来源或跨任务复用价值；形成可检验预测/问题；可能改变 project/synthesis；存在真实竞争解释；值得长期追踪；或当次输出结束后丢失会造成明显研究损失。普通联想、关键词关系、重复摘要和低价值问题不持久化。

创建时必须有 grounded evidence、locator/证据入口、创建理由，并使用 `review_status: unreviewed`、`reasoning_status: provisional`。创建不等于审核或晋升，必须进入 Human review triage。普通 Q&A 不创建 research note。

生命周期：

1. `provisional`：证据与推理已分开，但尚未晋升；可保持 `unreviewed`，只有可能改变科学结论、project/synthesis 或 paper evidence 的项进入 P0，其余高价值判断进入 P1。
2. `promoted`：用户完成相称审核，正式 owning page 吸收结论并回链 note/source；记录 promotion target、日期、理由和触发证据。
3. `rejected`：当前推理被审核否决；保留否决依据。
4. `superseded`：由更完整 note 或正式认识取代；链接后继页面。
5. `withdrawn`：创建者/用户主动撤回且不再作为活动候选；保留原因。

修订记录写入 history，状态回到适用稳定值。不得通过静默删除掩盖错误认识；用户明确要求删除尚未正式接纳的草稿时，按用户指令处理。Research note 不得成为所有文献的默认产物，也不得反向替代其 grounded sources。


## Stage 2.5：Project / synthesis active summary

大型 project 或 synthesis 页面应维护短的 `Agent active summary` / `Active summary for agents`，用于帮助后续任务定位相关 section 和减少启动开销。Active summary 不得替代 source locator、project/synthesis 主体或原文证据。

普通单篇摄入只需要读取 active summary 和相关 section；正式 project-level synthesis / cross-project synthesis 才默认完整读取相关 project/synthesis。若本轮实际修改 project/synthesis 主体、添加 evidence row/source relation/evidence gap/next action，必须同步最小更新 active summary；用户明确要求补充 project/synthesis 时，不得只改 active summary。给现有大型页面新增 active summary 时，只摘录已有页面结构和已有结论，不新增科学判断，并在 Human review triage 中列为 P1。
## Stage 3：Gap Analysis

寻找：

- 只有单一或非独立来源支持的重要主张；

高价值但当前无法解决的 gap，应以一个简短、可检验的问题写入 `knowledge/questions.md`；只有满足持久化门的复杂假设才创建 research note。活跃 L3/L4 继续自主选择下一步，不因发现 gap 自动停止等待用户逐项指示。
- 缺少精确 locator 的关键数值；
- 缺少寿命、偏振、角关联等区分性观测；
- 多次出现但尚无独立页面的核素、能带或概念；
- 可能改变结论的新实验或计算。

## Stage 4：人工决策

涉及 `confidence: high`、概念合并或研究方向决策时，展示证据矩阵并等待用户确认。

若综合结果将用于论文级主张，还必须通过 `system/paper-evidence-gate.md`：回到原始 source/raw、检查 locator、claim kind、人工复核状态、citation key 和竞争解释。综合页自身不能替代原始文献。

普通综合、研究讨论和早期写作不默认进入严格 paper evidence gate。综合可以提出任何单篇文献未逐字写出的 synthesis、inference、working hypothesis 或 possible interpretation，但必须标明其性质、主要支撑来源和证据限制；不得把综合结论写成某一来源直接报告的事实，不得因为直接证据尚不完整就无必要地拒绝合理综合。

## Stage 5：Human review triage

Project、synthesis 或跨来源 reflect 完成后，必须按 `system/workflows/ingest-strategies.md` 的统一格式输出 Human review triage。至少评估：

- synthesis 主结论和 “What is established vs what is not”；
- project evidence matrix 中 supporting/counter/alternative source 的归类；
- cross-source interpretation 和 “Current Wiki understanding”；
- 需要回 source/locator 核对的位置；
- 可能过度裁决、把模型解释写成事实，或把 synthesis 写成 paper conclusion 的段落；
- Motivation/why this matters 中可能过强的判断；
- innovation candidate notes、data-analysis bridge 和争议性解释总结。

主结论、evidence matrix 归类、用户数据解释、创新点候选和 paper evidence gate 候选通常属于 P0/P1。Planning notes、follow-up sources 与低风险导航可归入 P2/P3。所有 P0 无总量硬上限，必须逐项展示实际判断、证据、Agent inference、locator、审核目的和不审核风险；可分批但不得聚合隐藏。P1 可分组但不能退化为纯文件名列表。

综合主体完成、等待用户审核时，按 `AGENTS.md` 创建单个本地 `WIP review: <task short name> for user review`，不 push，并在 `system/wip-queue.md` 写入或更新 pending entry。queue 只保留继续审核所需的最新 branch/commit/next action；若后续 amend/rebase 改变 WIP hash，只更新到最新 commit。用户审核完成后，必须把该 WIP amend 为 final commit；通过发布门后按持续授权自动 push，不得另建 review/final commit；用户指定 final message 时原样使用，未指定时由 Codex 推荐直接相关的 message 并在最终报告中说明。

若上一轮处于 project review、synthesis review、cross-project synthesis review、waiting for user review、waiting for user P0/P1 review 或 `WIP review:` 状态，且用户给出实质性审核意见，并明确表示或根据当前消息与上下文可以无歧义地判断本轮审核已经结束，应识别为 human-review completion event，并在适用时进入 `review-finalization request`。

不要求固定触发短语；若存在歧义，不得自动写入 `system/review-history.md`。

Review finalization 在规则允许时可以默认完成审核意见对应的最小修改、检查、本地 commit、自动 push 与状态同步；当前指令中的“不要 push”“只 commit”“只修改”可覆盖本轮发布。完整 Git 边界由根目录 `AGENTS.md` 的 Review-finalization / Safe suspend 规则和 `check.md` 的 Git preflight 维护，本 workflow 不复制。其余收尾按审核范围处理：仅更新用户明确确认的 `needs_review`，确认无 unresolved P0/locator gaps 后按触发条件处理 overview/QMD，追加 `system/review-history.md`，独立判断 queue，刷新 Active handoff 和 short log。

若仍有 unresolved P0、locator gaps、审核意见未落实、审核意见无法唯一映射到具体 project/synthesis statement、project/synthesis 仍存在高风险不确定内容，或 HEAD 不是对应 WIP 且无法确认归属，不得强行 finalization；应停止并报告阻塞，必要时 safe suspend。

若用户明确不要 overview/QMD、只修改不 finalization、不要 push，或 push 状态无法确认，Review history 仍可记录本轮已经明确结束的人工审核，但 queue 是否保留必须独立判断。

Project、synthesis、cross-project synthesis 或 framework 任务正常结束后，必须自动刷新 `system/handoff.md` 的 Active handoff 并向 `system/log.md` 追加一条简短记录；用户不需要每次手动要求。Active handoff 写当前任务状态、commit/push 状态、未完成事项、P0/P1 审核重点、风险和下一步；若任务结束为 WIP、未 push、push 状态 uncertain 或等待审核，同步更新 `system/wip-queue.md`。

若某一轮人工审核已明确结束，则按规则追加 `system/review-history.md`；`system/log.md` 只写短事件，不保存长复盘。

若综合任务执行余量不足、检查失败需要用户决策、project/synthesis 修改未完成，或无法可靠完成，应进入 safe suspend：停止新增科学 claim，记录已完成步骤、已修改文件、未完成项、未核查 locator / claim gaps、P0/P1 风险和 continuation prompt；必要时创建本地 WIP checkpoint，但不 push。
