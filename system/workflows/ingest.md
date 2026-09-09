---
type: system-workflow
graph-excluded: true
operation: ingest
updated: 2026-08-06
---

# INGEST：来源摄入流程

原则：一次精确处理一个来源；原始文件只读；先建证据链，再做物理解读。

## 策略选择

开始摄入前，默认只读取 [ingest-strategies.md](ingest-strategies.md) 运行时短规则，并遵守其中的共同规则。普通单篇摄入不默认读取 [ingest-strategies-detail.md](ingest-strategies-detail.md)；这里的 detail 指 workflow 教程、策略说明、长示例、复杂案例和历史说明，不是 PDF 阅读深度。只有用户要求解释策略、修改 workflow、短规则不足以判断、要求 detailed workflow recap / detailed strategy-policy audit，或明确要求查阅详细教程时才读取 detail。

- `review-ingest`
- `experiment-ingest`
- `theory-ingest`
- `method-ingest`
- `targeted-ingest`
- `project-ingest`
- `daily-ingest`
- `claim-review-update`
- `data-analysis-bridge`

同一文献可以组合两个直接相关的策略，例如 `experiment-ingest + project-ingest`，但不得借组合策略扩大到用户未要求的页面或结论。用户只需提供目标路径、BibTeX key、策略、研究主题、project 关系、特别注意事项和 commit/push policy；无需重复策略默认清单。

普通单篇摄入指：一篇目标文献、明确 PDF 路径、明确 BibTeX key、明确摄入策略、明确研究主题、明确 project 关系，且不要求跨文献综合、修改 workflow、解释摄入策略、detailed workflow recap 或 detailed strategy-policy audit。普通单篇摄入不默认读取 detail 教程，但这不表示降低 PDF 阅读深度。

多篇摄入不自动等于复杂摄入。若用户一次给出多篇文献但要求逐篇摄入，Codex 应按“一篇一篇顺序摄入”执行；每篇都必须保持 source note、claim kind、locator、needs_review、project relation 和 Human review triage 标准，并有自己的 source-level / claim-level 审核重点。不得因为多篇文献在同一提示词中出现，就合并成粗略批处理。只有多篇之间需要跨文献比较、冲突证据判断、project/synthesis 大综合、策略选择不明确，或用户要求 detailed strategy-policy audit 时，才读取 detail 教程。多篇任务达到自然主题阶段时，按短版 strategy 的 `Thematic batch REFLECT` 触发和收尾，不默认等待整个批次结束。

开始新文献前检查 HEAD commit message，并在任务涉及未完成 WIP、review continuation 或非串行工作时读取 `system/wip-queue.md`。若 HEAD 是 active `WIP ingest:` 或 `WIP suspend:`，不得在同一分支直接开始下一篇摄入；先按 handoff/queue finalize/amend 当前 WIP，或等待用户明确要求另开分支、分离 pending WIP、放弃 WIP。

### 用户摄入模式

用户层面的三种摄入模式是任务控制信息，与下文 `reading_depth` 完成状态相互独立：

- **定向问题阅读模式**：围绕用户明确问题、章节、图表、公式或判据进行范围受控的深读；必须明确未覆盖范围，不冒充全文阅读。
- **标准深入阅读模式**：默认模式。重建论文问题、科学动机、方法与设计逻辑、关键证据链、假设、限制及与现有 Wiki 的必要联系，并评估迁移、竞争解释、反向检验、研究问题和认识修正的可能性。
- **严格全证据核查模式**：用于论文级关键主张、争议裁决或用户明确要求的高强度核查；扩大到完整证据链、关键补充材料、公式/图表/数值与竞争来源的系统复核，但仍受任务范围约束。

用户未指定时采用标准深入阅读模式。摄入请求同时授权与该来源直接相关的 L2：知识固化、关联、质疑、低成本验证和高价值问题记录。若问题需要系统背景、多个竞争解释或可能形成课题，可按 `autonomous-research.md` 自然进入 L3；L4 仍须 safe suspend 后由用户手动启动。三种模式不得与 `metadata-only`、`skimmed`、`read`、`deep-read` 建立一一对应关系。

活跃 L3 中的多来源摄入归入同一 project-level WIP 或通过发布门的 final commit；仍需逐来源建立 source、locator、claim kind 和 triage，但不执行逐篇等待人工审核的阻塞节奏。P0/P1 是内部优先级，不要求用户逐项处理；每个重要问题必须有状态、依据和后续路线。

## 1. 预检

1. 按 `AGENTS.md` 完成会话启动。
2. 确认目标位于 `raw/`；若不是，只读分析但不正式摄入。
3. 计算 SHA-256，记录文件大小和修改时间。
4. 查找 DOI、题名、作者、期刊、年份和已有 `canonical_source`，避免重复。
5. 若有 Zotero/BibTeX 元数据，记录 citation key、Zotero item key 和 select URI。
6. 检查 `system/vocabulary.md`、现有 aliases 和文件 slug。
7. 判断来源类型，并按 `system/workflows/ingest-strategies.md` 确认 ingest strategy。

citation key 只可在 DOI、题名或文件名能够唯一匹配 BibTeX 条目时写入；无法唯一匹配则留空并在复盘中列出，不得猜测或改写 `.bib`。

## 2. 阅读深度

在来源页标记：

- `metadata-only`：仅获得书目信息；
- `skimmed`：阅读摘要、结论和关键图表；
- `read`：完整阅读正文；
- `deep-read`：核对关键数据、图表、方法和补充材料。

`reading_depth` 只记录实际完成状态，不记录用户选择的摄入模式。来源页还必须说明 `Covered scope` 与 `Not covered`。局部问题即使核查很深，也不能据此把未完整阅读的全文标记为 `deep-read`；不得把 `metadata-only` 或 `skimmed` 写成已经精读。
## 2.1 PDF staged evidence reading

阅读义务由用户模式和任务范围决定，`reading_depth` 只在完成后如实记录结果。标准深入阅读通常需要完整理解正文主线并核查关键证据，但不得预先把状态指定为 `read` 或 `deep-read`。严格模式也只有在实际覆盖相应正文、关键证据和相关补充材料后才可记录 `deep-read`。

Staged evidence reading 只是阅读顺序优化，不是降低摄入标准，也不是默认快速 skim。可以节省的是启动治理文件、handoff/log、QMD、无过滤扫描、过长 workflow 和超长复盘；不能节省的是核心证据读取、locator、claim kind、关键图表/公式/数值核查。

1. 先读取 title、abstract、introduction、conclusion/summary，建立论文主线。
2. 再识别 sections、experiment/theory/method/results/discussion 边界，以及 figures、tables、equations、appendix 和 supplemental references。
3. 对 key claims 相关的 method/results/discussion、figures/tables/equations/captions 深入读取，重点核查 transition、spin/parity、multipolarity、mixing ratio、ADO/DCO、polarization、lifetime、B(E2)/B(M1)、wobbling energy、model parameters、PES、calculated spectra 等高风险内容。
4. 每条 key claim 回查 locator；locator 不确定且影响核心判断时保留 `needs_review: true`。
5. token 或执行余量不足时进入 safe suspend，写明已完成读取阶段、未完成 section/figure/table/claim locator 和下一轮继续提示词，不得省略核心读取或把未完成读取伪装成完成。

## 2.2 标准深入阅读的持续学习闭环

标准深入阅读必须逐项**检查**以下环节，但只在有充分证据和实际研究价值时输出或持久化；“未生成”不自动等于失败，无依据地硬生成才是失败：

1. Paper question 与 scientific motivation；
2. Method and design logic；
3. Key evidence and reasoning chain；
4. Assumptions、dependencies、limitations 与 failure conditions；
5. 与最相关现有 Wiki 知识的实质联系，以及 supporting/conflicting evidence；
6. Transfer potential 与 transfer failure boundary；
7. Competing explanations；
8. Reverse test 或 falsification route；
9. 可检验 research-question potential；
10. 新证据是否要求修正现有认识；
11. 该内容应留在当次输出、进入受控暂定推理层，还是经审核后晋升到正式知识；
12. Human review 与 promotion decision。

### 2.2.1 伴随观测与反证审计（高风险谱学 claim）

对 γ feeding、level scheme、decay assignment、branching ratio 或单线身份等高风险主张，增加一轮最小反证审计：若主张成立，哪些 companion transitions、branch ratios、级联或中间跃迁是必要伴随预测？伴随信号是否观测到？若未见，当前统计、效率、gate、能量分辨率、图表显示阈值和 binning 是否足以把它标成 `absence candidate`？目标峰附近是否存在 annihilation line、Compton/backscatter continuum、pile-up 或 detector-response contamination？衰变路径、组态、自旋宇称和中间跃迁是否整体闭合？

结果使用 `observed`、`expected-but-not-established`、`absence candidate`、`blocked-needs-raw/event-level data`，而不是笼统写成“需要更多统计”。无法闭合且可能改变核心判断的伴随证据记为 P1 或 `active-L3`；不要求每篇文献机械生成固定数量的替代解释。

不得为满足模板制造固定数量的迁移案例、反向检验、竞争解释或研究问题。没有可靠依据时，应简要说明为何不生成或不持久化。标准模式不要求穷尽所有关联、全文逐句注释、自动读取全部 supplementary、每篇都更新 project/synthesis/overview、每篇都创建暂定推理页，或自动生成 manuscript-grade 段落；这些高成本动作只在严格模式、用户明确要求或真实证据变化需要时执行。

标准深入阅读还应在 source 页留下简短的 `Knowledge Impact and Learning Decision`：明确既有 Wiki 认识、来源影响（supports / limits / revises / conflicts / no material change）、理由、持久化决定与 review state。该决策必须检查但不要求长篇填写；`no material change` 和 `source-only` 是合法结果。

## 3. 核结构信息抽取

按来源实际内容抽取，缺失项留空：

- 涉及核素、质量区和核反应；
- 束流、靶核、束流能量、蒸发道、余核；
- 探测装置、触发条件和符合关系；
- 能级、自旋宇称、γ 跃迁能量、相对强度、分支比和不确定度；
- DCO/角分布、线偏振、内转换、寿命等指认证据；
- 转动带或双重带标签；
- 组态指认、形变参数和理论模型；
- 作者的主解释、竞争解释与明确限制；
- 可精确定位的页码、图号、表号或补充材料位置。

## 3.1 Scope and nucleus-page decision

Do not use mass region alone as an exclusion or inclusion criterion.

During ingest, decide whether to create or update a source page, nucleus page, band page, concept page, method page, or project link based on:

1. source-supported low-energy nuclear-structure information;
2. reusable level-scheme, band-structure, transition, spin-parity, configuration-assignment, collective-motion, or competing-interpretation content;
3. reusable experimental-observable or analysis-method content, such as angular distribution, angular correlation, DCO ratio, linear polarization, ADO, mixing ratio, or alignment;
4. comparative value for current or future low-energy nuclear-structure questions;
5. explicit user-declared priority in the current request or repository records.

A source outside the current main research anchor may still justify lightweight nucleus, method, concept, band, or project pages if it contains reusable, source-supported nuclear-structure information. If a source is kept source-only, the reason must be evidence density, reuse value, or task scope, not mass region alone.

## 4. 建立来源页

使用 `system/templates/source-template.md` 创建 `knowledge/sources/<slug>.md`。

每条关键主张标记为：

- 实验事实；
- 实验判据；
- 作者解释；
- 模型结果；
- 我们的推断或综合判断。

无法核实的内容标记 `needs-human-review`。

来源页中的 scientific motivation、method/design logic、reasoning chain 和 limitations，若为作者明确陈述，应给出 locator 并标为作者内容。若由 Agent 根据原文分析性重建，必须单列为 `Analytical reconstruction` 或 `provisional interpretation`，列出证据、locator、关键推断步骤与不确定性，不得写成 source-grounded fact。重要或存在歧义的分析性重建进入 P0/P1；低复用内容留在当次输出，高复用且值得长期保留的内容按受控暂定研究推理流程处理，未经审核不得晋升为正式 synthesis/project 判断。

每篇 source 必须把 source-specific Human review triage 写回页面，直接采用短版 strategy 的 P0/P1/P2/P3 定义，不在 source 或聊天中另建分级规则。Triage 不得只存在于最终报告。Human Review Notes 与 Human Review Record 为事件驱动的可选区块：前者只在用户实际给出批注后加入，Agent 可为清晰度压缩、重排或整理用户表达，但必须保持原意和判断强度并与 Agent inference 分开；后者只记录真实发生的审核事件。

重要的 Related Knowledge / Project Relation 可使用轻量关系类型：`supports`、`limits`、`conflicts`、`foundational-background`、`methodological-bridge`、`competing-interpretation`、`retrospective-connection`、`not-direct-evidence`。只标注有助于知识判断的主要关系，并附简短具体说明；普通链接无需全部类型化。`retrospective-connection` 不得把后来术语倒灌为早期作者表述，`not-direct-evidence` 明确理论、方法或历史背景不能直接支持具体实验结论。

新建页面默认 `review_status: unreviewed`。页面级人工审阅与 claim-level `needs_review` 分开维护；Codex 不得因用户浏览过页面而自动清除具体 claim 的待审状态。

## 5. 更新领域页面

重用旧 source、nucleus、band、concept、method、project 或 synthesis 页面时，只按本轮实际需要做最小 on-touch migration；不得因为旧格式本身扩大任务范围、批量补历史 ingest mode、创建 research-note、转换 Personal Notes 或统一补 frontmatter。若修改科学 claim、interpretation、review/reasoning state 或知识关系，必须进入 Human review triage；未触及的历史页面保持不变。

1. 核素信息更新到 `knowledge/nuclei/`。
2. 具体能带或双重带更新到 `knowledge/bands/`。
3. 物理现象和解释框架更新到 `knowledge/concepts/`。
4. 束流、靶、反应道和装置更新到 `knowledge/experiments/`。
5. 理论框架更新到 `knowledge/models/`。
6. 诊断观测量更新到 `knowledge/observables/`。
7. 实验分析、数据处理或计算方法更新到 `knowledge/methods/`。
8. 新来源与旧来源发生冲突时，并列写入，不静默覆盖。
9. 只有长期可复用的内容才进入综合页。

## 6. 人工复核门

以下变化必须向用户展示后再落为确定结论：

- 新的自旋宇称或组态指认；
- 从“候选”升级为较强的结构解释；
- γ-soft 与 γ-rigid 之间的判断；
- wobbling、chiral doublet 或其他竞争解释的取舍；
- `confidence: high`；
- 概念页或能带页的合并。

只有用户明确确认某条 claim 或明确圈定的一组 claims 已完成复核，Codex 才能把相应 `needs_review: true` 改为 `false`。未复核内容可以帮助定位问题，但不能进入论文级证据池。

## 7. 收尾与 WIP lifecycle

- 按本轮新增或修改页面判断是否需要对 `knowledge/index.md` 做必要的最小入口同步；无需时不机械重写。`knowledge/overview.md` 按下述触发条件判断是否 deferred。
- 普通单篇摄入如果只是新增 source、少量 claims 或最小 project relation，overview update 可以 deferred；最终复盘写明 `overview update deferred`、原因和建议补跑时机。
- 新建或显著更新 project/synthesis、批量摄入、主题知识地图结构性变化、paper evidence gate 或 major concept map 变化，或用户明确要求时，才更新 overview。
- 若实际修改大型 project/synthesis 主体、添加 evidence row/source relation/evidence gap/next action，必须同步最小更新该页 `Agent active summary`；如果页面没有 active summary 且本轮实际修改该页，应创建短 summary。
- QMD refresh 不是普通单篇摄入固定收尾成本；可只运行轻量状态检查，或写明 `QMD refresh deferred`、原因和建议补跑时机。批量摄入、多篇文献完成、用户明确要求或大型 project/synthesis 依赖最新检索时，再运行 `qmd update` / `qmd embed`。
- 检查是否推进 `knowledge/questions.md` 中的开放问题；不为形式完整而新增重复问题。
- 向 `system/log.md` 追加简短 ingest 记录，更新 `system/handoff.md` 的 Active handoff；用户不需要每次手动要求 handoff/log 收尾。
- 普通摄入结束后由 Agent 完成全文、locator、claim kind、证据层、竞争解释和 P0/P1 自审；不存在未隔离 hard P0 且检查通过时，可把 rolling WIP amend 为 final，并按用户已建立的持续 commit/push 授权进入 H3 与非 force push。Agent 自审不改变页面级 `unreviewed` 或 claim-level `needs_review`，也不写入 Human Review Record/history。
- 摄入尚未完成、存在未隔离 hard P0、检查失败、远端异常，或用户明确要求先审核时，创建/保留本地 WIP ingest commit、不 push，并在 `system/wip-queue.md` 写入或更新 pending entry；queue 只保留继续处理所需的最新 branch/commit/next action，overview/QMD 可按规则 deferred。
- handoff/log 不保存长复盘；Active handoff 记录任务状态、commit/push 状态、未完成事项、P0/P1 审核重点、风险和下一步。
- 执行 `check.md` 中与本次摄入相关的项目。
- 最终复盘采用 compact final recap：Result status、commit/push、关键文件、Human review triage、checks、next action。
- 最终复盘必须按 `system/workflows/ingest-strategies.md` 输出 Human review triage。所有 P0 都必须逐项可读、可审核，可分批展示但不得聚合隐藏、降级或遗漏；P1 可分组展示但仍须呈现实际判断、证据、Agent inference 和审核目的。多篇摄入必须按每篇分别列 P0/P1。

### 7.1 Ingest completion and Agent self-audit

摄入主体完成后：

1. 运行 `git status --short`、`git diff --stat`、`git diff --check`；
2. 运行 `python system/scripts/wiki_lint.py --fail-on error`；
3. 回查每篇全文与 source-specific triage，确认核心 claim 有可用 locator、事实/作者解释/模型/Agent synthesis 分层明确、竞争解释与反证未被抹平；P0 必须逐项处置，P1 保留为未来证据采用时的复核优先级；
4. Agent 自审通过且不存在未隔离 hard P0 时，显式暂存本轮摄入相关文件，不使用 `git add .`；若 HEAD 是本任务 rolling WIP，则 amend 为与实际范围相符的 final commit，否则直接创建 final commit；
5. 不把 Agent 自审记为 Human review，不写 `system/review-history.md`，不将 `review_status` 升为 `human-reviewed`，不自行把 `needs_review: true` 改为 `false`；
6. 用户的持续 commit/push 授权在普通 ingest 通过发布门后生效：完成 H3、fresh fetch、remote ancestry、精确 refspec dry-run，再以同一 refspec 非 force push；当前指令中的“不要 push”“只 commit”“只修改”可覆盖本轮发布，认证、远端漂移或检查失败立即 safe suspend；
7. 尚未完成、存在未隔离 hard P0、检查失败或用户明确要求先审核时，创建/保留 `WIP ingest: <paper short name> for user review`，更新 pending queue，不 push；
8. 最终复盘列出 final/WIP hash、message、push 状态、关键文件、Agent self-audit 结果、Human review triage 与未来 claim 复核重点。

WIP ingest 是长任务、中断、hard P0 或用户明确审核请求下的本地检查点，不表示科学内容已人工复核。普通 ingest 的 final/push 也只表示 Agent 已完成摄入自审和工程检查，不表示页面或 claims 已经人类复核。若用户明确禁止本地 WIP，保留工作树 diff，并在 diff 较大时提示可能产生 Codex、Git 或文件监听的持续 CPU 负担。

### 7.2 Review finalization

用户审核后，若上一轮处于 `WIP ingest:` / source review / waiting for user review / waiting for user P0/P1 review 状态，且用户给出实质性审核意见，并明确表示或根据当前消息与上下文可以无歧义地判断本轮人工审核已经结束，应识别为 human-review completion event，并在适用时进入 `review-finalization request`。

不要求固定触发短语；若存在歧义，不得自动写入 `system/review-history.md`。用户明确要求“只修改不 finalization”“只修改，不提交”或“只 commit，不进行其它收尾”时，不进入本地 finalization；“不要更新 overview”或“不要刷新 QMD”只覆盖对应步骤。“不要 push”只表示继续不 push，不取消 review-finalization 或本地 commit。没有这些覆盖要求时，默认进入适用的 finalization，并在发布门通过后自动 push。

Finalization 包括：

在执行下列步骤时，将用户实际批注按原意整理进适用 source 的 Human Review Notes，并为本轮真实发生的审核事件追加简短 Human Review Record；不得为未发生的审核预建记录。

1. 只根据审核报告修改明确提到的 source、claim、project 或 `review_status`；
2. 不自动清除审核报告未提到的 `needs_review`；
3. 处理用户明确确认范围内的 `needs_review` 状态；
4. 若仍有 unresolved P0、未核查 locator gaps、审核意见未落实，或 source 仍存在高风险不确定内容，不得强行 finalization，应 safe suspend 或报告阻塞；
5. 若审核意见已落实且无 unresolved P0，重新评估本 workflow 的 overview 触发条件；只有新证据改变综合判断、关键知识关系或 project/synthesis 证据结构，用户明确要求，或本轮明确判定为必要同步时才更新 `knowledge/overview.md`，否则记录 `overview update deferred` 及理由；
6. 执行 QMD refresh（`qmd.cmd update`、`qmd.cmd embed -c nuclear-knowledge`、`qmd.cmd status`）；
7. 重新运行 Git 检查和 Wiki lint；
8. 重新输出 Human review triage，列明已处理项目、仍保留的 P0/P1 和 paper evidence gate 影响；
9. 确认 HEAD 是对应的 WIP ingest commit 后，使用 `git commit --amend` 把 WIP 转换为 review/final commit，不新建额外 review commit；
10. 用户指定本轮提交 message 时原样使用；未指定时由 Codex 根据实际摄入与审核修改推荐直接相关的 message，并在最终报告中说明；
11. 完成本地 review/final commit 后，在 H3、fresh fetch、remote ancestry 和精确 refspec dry-run 通过时自动 push，并报告 commit hash、检查结果和远端状态；当前指令中的“不要 push”“只 commit”“只修改”可覆盖本轮发布；
12. 为本轮明确结束的人工审核追加 `system/review-history.md` 条目；记录审核范围、用户判断、要求修改、遗留问题、下一步、相关页面，以及 `review commit message`（若本轮实际创建或 amend 了 review commit）；
13. 在同一个 finalization 流程中刷新 `system/handoff.md` Active handoff，并独立判断 `system/wip-queue.md` 对应 entry 是继续保留、更新还是清除；不得使用简单的 queue-to-history 自动迁移模型；
14. 向 `system/log.md` 追加短记录；
15. 最终复盘报告 overview、QMD、commit、push、handoff、queue、review history 和 log 状态。

如果 HEAD 不是对应 WIP，或无法确认 WIP 归属，停止并询问用户，不得擅自 amend。若用户明确“不要更新 overview”“不要刷新 QMD”“不要 push”或“只修改不 finalization”，Review history 仍可记录本轮已明确结束的人工审核，但 queue 是否保留必须独立判断。若 push 状态无法确认，应 safe suspend，并在 handoff/queue 中写明 `push status: uncertain`。Finalization 使用 amend，避免 WIP commit 累积，也避免在 push 后再额外创建 queue/status 修正 commit。
