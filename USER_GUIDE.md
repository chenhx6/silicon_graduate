# 低能核结构 Wiki 使用指南

这套 Wiki 面向熔合蒸发反应和低能原子核结构研究。Obsidian 是人的浏览、审阅和写作界面；Agent 负责摄入、交叉引用、综合、检查与维护；Markdown 文件是双方共享的长期记忆。

当前系统是 Continuous Research-Learning v2（硅基研究生 V2）：面向低能核结构研究的 Human-in-the-loop research Wiki。授权摄入/综合任务默认运行 L2 研究学习闭环，高价值问题可进入 L3；真实、公开或可靠模拟数据到位并由用户手动启动后，L4 执行可复现的数据—分析—失败—修正闭环。ordinary Q&A 保持轻量。A≈130 是当前研究锚点，不是收录边界。详细架构见 [architecture updates](system/architecture-updates/README.md)。Wiki 不是最终权威，不保证文献完整覆盖，不能替代原文阅读和人工科学判断。

本文件是快速使用指南。需要了解目录层级、证据术语、人工审阅、project、写作准备和可复制提示词时，请查看 [USER_GUIDE_DETAIL.md](USER_GUIDE_DETAIL.md)。

## 1. 目录怎么理解

```text
raw/         原始论文、笔记、图像和数据；默认由你管理，Agent 仅管理约定的 gpt 文献入口
knowledge/   经过证据化整理的科研知识；Agent 维护，你审阅
system/      schema、模板、流程、记忆、日志和交接状态
outputs/     审计、报告、文章草稿和演示产物
```

最重要的入口：

- `PLAN.md`：你维护的宏观阶段计划、个人好奇心与研究方向草稿；
- `knowledge/index.md`：知识导航；
- `knowledge/overview.md`：健康概览；
- `knowledge/questions.md`：开放科研问题；
- `system/handoff.md`：最近任务做到哪里、改了什么、下一步是什么；

Wiki 可在不同操作系统和 AI 工具环境中使用；`.codex/`、`.obsidian/` 和个人运行参数属于本地配置，不随公共仓库分发。任务仍需遵守证据规则、raw 保护和不可逆操作确认，且不依赖桌面端 GUI 或 Computer Use。

### 科研自治入口

完整 L0–L4、每周自测、P0/P1 和人工关口只在 [autonomous-research workflow](system/workflows/autonomous-research.md) 维护。常用触发示例：`摄入 <文献>` 默认完成 L0–L2；`开始 L3 研究：<问题>` 启动课题调查；L4 必须先有数据候选并由你发送 `开始 <项目> L4：数据=<Wiki 内路径>`。`:danger-full-access` 只是终端运行权限，不是科学自治等级。每周自测有实质变化时先建立本地 WIP 和集中 P0/P1 报告，经你审核后才发布。

90 天持续学习由 [continuous-learning workflow](system/workflows/continuous-learning.md) 和 [learning queue](system/learning-queue.md) 管理。每日 22:00（Asia/Shanghai）的独立任务以 2–3 小时为 checkpoint，不是硬停止，不限制主题或论文数量；达到里程碑或信息增益下降才收敛。若 Git、网络或认证失败，任务仍可写回安全的知识页和学习记录并标为 `content-complete / final-not-pushed`，不会伪造已发布。
- `system/log.md`：只追加的操作历史；
- `check.md`：系统与科学质量检查。

`PLAN.md` 管“接下来可能想去哪里”，`system/handoff.md` 管“上一次任务停在哪里”。Agent 不会把 PLAN 当作 cite-key 文献清单、执行日志或必须立即执行的待办；普通小任务不强制读取 PLAN，涉及阶段计划、研究优先级、文献选择方向、项目建立、长期探索或多步骤知识库建设时才会读取。

## 2. 在 Obsidian 中打开

1. 在 Obsidian 选择“打开本地仓库作为库”。
2. 选择 clone 后的整个仓库目录，不要只选择 `knowledge/`。
3. 这样可以同时看到证据、知识、治理规则和输出，但日常主要浏览 `knowledge/`。

推荐启用的核心功能：

- Backlinks；
- Outgoing links；
- Graph view；
- Properties；
- Templates；
- Search。

当前 vault 已启用 Dataview。它用于列出页面元数据，不替代 Markdown 正文和 Git 中可读的静态索引。

建议把附件目录设为 `raw/figures/`。该目录由你或 Obsidian 写入，Agent 不主动修改。

### 图谱过滤

在 Graph view 的 Filters 中使用：

```text
-path:"raw" -path:"system" -path:"outputs" -path:"share_message"
```

这样图谱主要显示核素、能带、概念、模型、观测量和来源之间的科研关系。

Dataview 插件程序本体位于 `.obsidian/plugins/`，不进入 Git；启用清单和核心 Obsidian 配置可以进入 Git。Zotero Integration 等其他社区插件应在轻量流程稳定后再引入，避免插件配置反客为主。

### Dataview 常用查询

在个人工作台页面中可粘贴：

````markdown
```dataview
TABLE type, review_status, updated
FROM "knowledge"
WHERE review_status = "needs-human-review"
SORT file.name ASC
```
````

查看某个核素的带页：

````markdown
```dataview
TABLE band_label, parity, spin_range, interpretation_status
FROM "knowledge/bands"
WHERE nucleus = "137nd"
SORT file.name ASC
```
````

## 3. 日常摄入论文

### 从 Zotero 选论文

1. 在 Zotero 建立 Collection：`Wiki Inbox`。
2. 把准备精读的论文加入该 Collection。
3. 将对应 PDF 复制到 `raw/papers/`。
4. 告诉 Agent：

```text
摄入 raw/papers/论文名.pdf。先检查重复和 Zotero 元数据，
列出拟创建或更新的页面，再开始写入。
```

一次处理一篇。不要把整个 Zotero 库批量倒进来。

需要 Agent 查找新文献时采用 Nature-first 路由：先以结构化学术检索核对 DOI、作者、年份和期刊，再补查 Google Scholar（不通时用学术镜像），最后由下载技能写入 Wiki 内的隔离区。候选 PDF 通过首页、DOI、页数、文件签名、SHA-256 与重复检查后，才从 `raw/papers/gpt/_incoming/<run-id>/` 晋升到 `raw/papers/gpt/`；书目只追加到 `raw/zotero/gpt.bib`。允许下载文件，但 Agent 必须显式指定 Wiki 目标路径；无法控制目标路径、会默认落入外部 Downloads 的浏览器下载交给用户处理。APS/PRC 或 Scholar 出现验证码或真人验证时，由你在原标签页完成后再让 Codex 继续。

日常摄入按以下闭环执行：

1. 你提供一篇新论文或指定 `raw/papers/` 中的新文件；
2. Codex 读取原文，建立或更新 source 页；
3. Codex 按 schema 更新相关 nucleus、band、concept、observable、model、experiment 和必要的 synthesis 页面；
4. Codex 在最终复盘中列出修改文件、新增 claims、self-audit 结果、缺失原始文献和竞争解释；
5. Codex 自行完成 source 页和关键 claims 的研究核查；用户不需要在本批次逐项审核；
6. 后续问答或论文写作需要使用具体 claim 时，再完成直接来源、locator、适用条件和竞争解释核验；论文级最终措辞仍由用户确认，不要求先全面审核整页。

### 摄入后 Codex 自审什么

- 实验事实是否与作者解释分开；
- 能级、自旋宇称、跃迁能量和单位是否正确；
- 图号、表号、页码等 locator 是否足够；
- 组态、wobbling、chiral、γ-soft/γ-rigid 是否保留候选或争议状态；
- Agent 拟合并的概念是否真的物理等价；
- `needs-human-review` 或 `needs_review` 项的证据边界、后续核验路径和措辞强度。

页面级 `review_status: human-reviewed` 只表示真实用户看过该页并完成页面层复核。Codex 可以在完成直接来源、locator、claim kind、适用条件和竞争解释的 self-audit 后更新对应 claim 的 `needs_review` 或 confidence 技术记录，但不得把该动作写成用户审核。后续问答或论文写作中的最终措辞仍按具体 claim 触发用户确认。

### 本地 WIP 检查点

每日持续学习把内容写回与 Git 发布分轨：发布门失败不等于学习失败，但根目录、配置/sentinel、BibTeX 基线和 dirty/raw overlap 不安全时必须 safe-suspend；完整 H1/H2/H3 通过后才 commit/push。

普通文献摄入像研究生自行读文献：Codex 逐篇完成全文回查、locator/claim kind、证据分层、竞争解释与 P0/P1 self-audit。长任务可保留一个本地 rolling `WIP ingest:`；完成且没有技术 hard P0 时 amend 为 final，并按仓库的持续 ingest 授权完成 H3、fresh fetch、精确 refspec dry-run 和非 force push。科学 partial/stopped 状态不单独阻止 final/push；页面是否 `human-reviewed`、论文 claim 是否准入分别由真实用户事件和 paper evidence gate 决定。独立 project、synthesis、跨来源研究结论也由 Codex self-audit 后收尾，不主动要求用户审核。

后续用户审核发生时，Codex 根据报告修改明确项目，并使用 `git commit --amend` 把对应 WIP 转为落实本轮审核意见的 review commit / final commit。普通研究由 Codex self-audit 后直接收尾；技术 hard P0、检查失败或远端异常时保留本地 WIP。你已授予持续自主 commit/push：通过 H3、lint、远端 ancestry 和精确 refspec dry-run 后，Codex 默认自动发布。同一分支不累积多个 active WIP。当前指令中的“不要 push”“只 commit”“只修改”可覆盖本轮发布。若确实不希望任何本地 commit，请明确写“禁止本地 WIP commit”。

多篇文献仍逐篇摄入并优先在同一主题 rolling WIP 中连续完成，以减少 nucleus、concept、project、synthesis、index 等共享页重叠；不再逐篇等待人工审核。存在多个 pending WIP 时仍需按文件 overlap 处理：无重叠可独立；同一范围继续并 amend 原 WIP；依赖未 final 内容时记录 dependent WIP；共享文件无法安全隔离时暂缓修改。Codex 会把中断、未隔离 hard P0、未 push checkpoint 或 push 状态 uncertain 的短恢复索引记录到 `system/wip-queue.md`，Active handoff 只保留最近一次活动。

写任务第一次修改文件前、创建 WIP/final commit 前及 push 前，Codex 会按 `check.md` 运行仅限 LF/CRLF 行尾格式差异的清理入口。用户也可手动运行：

```bash
python3 system/scripts/clean_knowledge_eol_dirty.py
python3 system/scripts/clean_knowledge_eol_dirty.py --dry-run
```

脚本只清理未暂存且可证明为 LF/CRLF-only 的 tracked `knowledge/**/*.md`；普通行尾空格、Markdown 双空格和 Tab 都视为 substantive 并保留。脚本不触碰 staged 内容、不处理其它目录，并保留 substantive/mixed 状态。exit code `1` 只表示仍需由 Codex 按授权范围、入口 baseline 和 WIP 归属分类；完全属于当前授权任务的 substantive diff 不会因此被无条件阻断。

`system/review-history.md` 只记录后续问答或论文写作中真实结束的人工审核轮次；Agent self-audit 不写入这里。科学研究的 WIP 在 self-audit 和技术发布门通过后可以 final/push，即使尚未发生用户审核；需要论文使用时仍回到具体 claim 的 paper evidence gate。

审核完成时可以直接写简短结论，例如：

```text
审核：
1. ...
2. ...
审核完毕，除了以上几点外无问题。
```

Codex 应自动把这类消息理解为“本轮人工审核已经结束”，记录本轮 Review history，并进入 review-finalization：按审核意见做最小修改，按 workflow 触发条件评估 overview/QMD，完成 review/final commit，并在检查通过后自动 push，再独立判断 queue 是否继续保留。“不要 push”只表示继续不 push，不会取消已经明确结束的人工审核或本地 finalization。你不必使用固定短语；只要整体语义可以无歧义地判断本轮人工审核已经结束即可。如果你不想进行本地 finalization，需要明确写“只修改不 finalization”“只修改，不提交”或“只 commit，不进行其它收尾”；“不要更新 overview”或“不要刷新 QMD”只覆盖对应收尾步骤。

普通问答、跨来源比较、研究讨论和早期草稿默认采用 evidence-calibrated ordinary mode：Codex 会基于当前已有证据给出最佳可支持答案，区分事实、作者解释、模型结果、综合判断和暂时推断。已核实的 Wiki 页面名称和行号链接直接放在它所支持的句子后面，方便立即核对；默认不再在末尾重复列出同一批证据页。一般专业背景不要求每句附链接；知识库未覆盖时仍可补充稳定的一般专业背景，但会说明它不是 Wiki-grounded 或 externally verified evidence。重要但 Wiki 尚无直接证据的判断会在出现位置说明。普通回答不默认展开 citation key、raw PDF、review 状态或长 evidence card；原文核查、论文级审查或 strict paper mode 再补充完整核查信息。Wiki 正文仍保留 Obsidian Wikilink，也不会为了改变打开界面而修改证据页或制造 Git diff。打开证据页可能让 `knowledge/*.md` 显示 modified；Codex 会在每次 commit/push preflight 中区分授权修改与 LF/CRLF-only dirty 状态，后者确认无实质差异后清理，存在实质差异时停止并要求用户确认。用户也应避免使用 `git add .`。论文或投稿核查、正式引用、直接来源或原文引文、精确 locator、关键科学 claim 确认时才进入严格的 paper evidence mode；普通争议讨论本身不自动触发 strict mode。

## 4. Zotero 轻量连接

当前推荐 Zotero 继续作为书目和标注主库，不直接读写运行中的 `zotero.sqlite`。

Better BibTeX 可将 `Wiki Inbox` 自动导出为 BibTeX/Better BibTeX JSON。具体约定见 `system/zotero-integration.md`。来源页预留：

- `zotero_item_key`
- `citation_key`
- `zotero_uri`
- `library_file`

没有导出元数据时也可摄入，Agent 会从 PDF 和文件名提取信息并标记待核对项。

当前自动导出文件为 `raw/zotero/wiki-inbox.bib`，由 Zotero/Better BibTeX 更新，Agent 只读且不会暂存。把新论文加入 `Wiki Inbox` 后，应确认该文件出现对应 citation key，再请求摄入。Agent 自主获取并验证的书目单独写入 `raw/zotero/gpt.bib`，不得覆盖或合并回 `wiki-inbox.bib`。

截至 2026-07-02，`wiki-inbox.bib` 的 9 条记录通过 DOI、题名和文件名覆盖 `raw/papers/` 中的 9 个 PDF；现有 7 个 source 页均可唯一匹配 citation key。citation key 缺失主要影响未来 BibTeX 写作链稳定性，不表示科学内容错误。

## 5. 如何提问

可显式使用 `$wiki-evidence-query` 进行默认只读、区分证据类型并给出处的核结构知识问答。

`knowledge/research-notes/` 保存少量高价值、尚未成熟的“暂定研究推理”。普通问答默认不把它当作正式证据，也不会自动检索或创建；授权 L2、活跃 L3/L4、reflect/project/synthesis 只有在满足持久化门时才使用，并会标明 provisional 状态、回到原始 source 核查。创建 note 或 Codex 自审核不等于人工审核或知识晋升。

查询会使用 `system/vocabulary.md` 和页面 aliases 做中英文双向扩展：“壳模型”与 `shell model` 会归一到同一泛称入口；“开门”或 `gate by x keV` 会在 γ 谱学语境中扩展到 coincidence gating。泛称可能对应 CSM、PSM、TPSM 等多个候选时，回答会列出候选，不会擅自合并。

### QMD 本地检索

QMD `2.5.3` 已配置为 `knowledge/` 的本地搜索层。你正常提问即可，不需要每次提醒“使用 qmd”；Agent 会根据问题自动选择：

- 精确核素、作者、DOI、citation key 或术语：`rg` / `qmd search`；
- 近义表达、机制和竞争解释：按需 `qmd vsearch`；
- 高价值跨页综合：执行余量充足时才使用完整 `qmd query`。

索引位于被 Git 忽略的 `.qmd/`，只包含 `knowledge/**/*.md`，不会索引 PDF、`raw/`、系统规则或 Obsidian 工作区。Research notes 暂时仍在同一 collection，但 ordinary Q&A 会按路径/type 排除。你可在仓库根目录检查：

```bash
qmd.cmd status
qmd.cmd search "wobbling signature splitting" -c nuclear-knowledge
```

知识页发生变化后，Agent 应自动运行：

```bash
qmd.cmd update
qmd.cmd embed -c nuclear-knowledge
```

`qmd pull` 是首次下载或修复本地模型的命令，不是 Git pull；当前三类模型已经下载。不要使用 `qmd update --pull`，仓库同步继续由独立 Git 流程处理。QMD 只负责发现候选页面，回答仍必须打开完整页面并回到 source/raw 核验。

示例：

```text
根据知识库，比较 A≈130 区 transverse wobbling 与 signature-partner
解释所依赖的实验判据。区分观测事实、模型结果和作者解释，并给出处。
```

```text
检查 131Xe 的现有页面：哪些观测真正区分 wobbling 与普通 signature splitting？
缺少哪些测量？
```

```text
把 γ-band staggering 对 γ-soft 和 γ-rigid 的判别写成证据矩阵，
同时列出模型前提和可能失效的情况。
```

Agent 应先检索 `knowledge/`，再回到 `knowledge/sources/` 和 `raw/` 核验，不得用模型记忆冒充本库证据。

日常使用边界：

- Wiki 可用于找线索、找判据、找文献和组织问题；
- Wiki 不能替代原文阅读；
- 未完成 claim-specific verification 的相关内容仍可作为 candidate evidence 主动呈现并参与研究讨论、探索性综合和早期草稿，但必须说明 review/source/locator 状态与核查路径，不能直接写成最终论文结论；
- synthesis 是综合层，不是原始文献；
- 写论文时必须回到 source、raw、精确 locator 和 citation key；
- 对存在竞争解释的主题，必须区分观测事实、实验判据、模型结果、作者解释和综合判断。

## 6. 如何用于科研写作

推荐写作链：

```text
source 页 → nucleus/band/concept/model/observable 页
→ synthesis 证据矩阵 → outputs 中的文章或报告草稿
```

- `source` 保存一篇文献实际说了什么；
- `concept/model/observable` 积累跨文献认识；
- `synthesis` 专门处理证据、反证和竞争解释；
- `outputs` 承载论文段落、综述、报告和幻灯片。

要求 Agent 起草时可使用：

```text
根据 knowledge/synthesis/相关页面起草一节论文。
每个物理判断必须能追到 source 页；知识库未覆盖的引用用 TODO 标记，
不要编造参考文献。
```

论文级文字必须先通过 [system/paper-evidence-gate.md](system/paper-evidence-gate.md)。当前阶段不创建写作 Skill；只预留接口，等 source/synthesis 层、citation key、证据门和至少一个真实 project 闭环稳定后再处理。

Project 可以随具体研究问题、阶段性数据处理结果、证据比较任务或写作目标进入工作流，不必等待固定时间点或全部数据处理完成。

现阶段 Skill 只承担证据型知识问答入口。ingest、reflect、lint 等流程继续使用现有 workflow，等真实使用稳定后再决定是否封装；未来写作 Skill 不在当前阶段创建。

## 7. 会话记忆和版本保护

聊天不是长期记忆。每次实质任务结束后，Agent 应更新：

- `system/handoff.md`
- `system/wip-queue.md`（仅当存在 pending WIP、等待审核或未 push checkpoint）
- `system/log.md`
- `knowledge/index.md`
- 必要时更新 `knowledge/overview.md` 与 `knowledge/questions.md`

每次还必须判断本指南是否需要更新。

Git 只管理 Markdown、规则和小型文本资产。PDF、数据和个人材料默认不进入普通 Git 历史；它们由 Zotero、原始存储和备份负责。

公开主远端仓库为 [Gitee `chx6/silicon_graduate`](https://gitee.com/chx6/silicon_graduate)。GitHub 若存在仅作为 Gitee 镜像，不作为本库维护或 CI 入口。本地 `origin` 应指向：

```bash
git remote set-url origin https://gitee.com/chx6/silicon_graduate
git push -u origin main
```

若 `git remote -v` 已显示 `origin`，不要重复执行 `remote add`。未发表内容、合作材料、审稿材料、个人数据和敏感原始材料应继续留在被忽略的私有目录，不进入公开远端。

### Push 前检查

提交或推送前运行跨平台预检并确认 staged 文件：

```bash
python3 system/scripts/wiki_automation_preflight.py --root .
git diff --cached --check
git push --dry-run origin HEAD:main
git push origin HEAD:main
```

`raw/zotero/wiki-inbox.bib` 仍由 Zotero 管理，不要修改或暂存；认证失败时保留本地提交并记录 `final-not-pushed`。

## 8. 自动 lint

在仓库根目录运行：

```bash
python system/scripts/wiki_lint.py --fail-on error
```

正常结果类似：

```text
GOVERNANCE page_unreviewed=48 source_unreviewed=0 claims=45 claim_needs_review=9 claim_missing_locator=0 claim_missing_kind=0 source_missing_raw_file=0 source_missing_citation_key=0
SUMMARY pages=61 wikilinks=372 hashes=7 errors=0 warnings=0 info=9
```

自动检查包括：

- Markdown frontmatter、必需字段、type 和目录对应；
- slug、aliases、index 覆盖和 Wikilink；
- source PDF 路径与 SHA-256；
- 核素 A/Z/N、元素 Z；
- 可解析的 `(beam,xn)` 熔合蒸发反应道守恒；
- `confidence: high` 是否有人类确认记录；
- 页面/source 审阅状态、claim 待审和缺失字段统计；
- `raw/` 工作树变化和知识页是否被 Git 忽略。

需要更严格或机器可读输出时：

```bash
python system/scripts/wiki_lint.py --fail-on warning
python system/scripts/wiki_lint.py --format json --output outputs/lint-report.json
```

自动 lint 不判断“某带是否真的属于 wobbling/chiral”这类科学结论，也不会自动合并或改写页面。维护远端为 Gitee，GitHub 镜像不运行本库维护工作流；由于 PDF 不进入公开远端，云端缺少 PDF 时只报告 warning；完整哈希核验应在本机运行。

当前自动 lint 主要证明结构健康，不等于科学内容已全部人工复核。输出中的 `GOVERNANCE` 行会自动统计页面级/source 页 unreviewed、claim-level `needs_review: true`、缺 locator、缺 `claim_kind`、source 缺 `raw_file` 和缺 citation key。`CLAIM_NEEDS_REVIEW` 作为非阻断 info 保留人工审阅队列；缺 locator/kind 为 error，缺 citation key 为 warning。

## 9. 定时续跑与无人值守任务

Codex 中的定时续跑不是 Windows 任务计划程序，也不能仅靠“额度在某时刷新”自动恢复。它依赖相应的本地调度链路在到期时真正消费任务；电脑休眠、应用退出或后台进程被挂起时可能不运行，但应用保持开启、电脑持续接电且不休眠也不构成执行保证。

建议按以下方式使用：

- 1 小时内、继续当前线程的短等待可以使用 heartbeat，但应保持 Codex 与电脑可用；
- 超过 1 小时的等待优先使用面向工作区的独立调度；它仍不是远端执行保证，除非已明确配置远端常驻环境；
- 配额刷新只恢复可用额度，不会主动唤醒会话；
- 一次性任务在界面中必须显示为一次，而不是“每天”；若界面表达有歧义，不应启用；
- 到期后先查看运行回执和实际产物。没有运行记录时，应按“未触发”处理，不能把预定时间当作完成证据。

对本知识库，最稳妥的长等待方案是：Agent 先保存未完成状态、精确续跑命令和下一步到 `system/handoff.md`；额度刷新后由你发送“继续”，再从 handoff 恢复。只有在已经验证常驻调度环境时，才适合承诺无人值守执行。

如果 Codex 判断剩余上下文、token、5 小时额度或执行余量不足以稳定完成任务，会进入 safe suspend：停止扩大修改范围，检查 Git 状态和 diff，把已完成/未完成事项、修改文件、风险及可直接使用的续跑提示词写入 handoff，然后请你在额度刷新后发送“继续”。大量 Markdown diff 场景会优先创建仅保存在本地的 WIP checkpoint，暂停本轮自动 push，以减少持续文件扫描和 CPU 占用；已有同任务 WIP 时通过 amend 更新，不创建第二个。这不会让原任务自动睡眠或原地恢复，也不会自动创建 automation。

## 10. 常用指令

```text
按 check.md 检查本次改动，不自动合并科学概念。
```

```text
更新 handoff，写清本次完成内容、未解决问题和下一步。
```

```text
检查 USER_GUIDE、AGENTS、schema、templates 是否需要同步。
```

```text
做一次反向检验：主动寻找反证、替代解释和证据依赖关系。
```
