# 低能核结构 Wiki 详细使用说明

## 1. Purpose / 文件定位

`USER_GUIDE.md` 是快速使用指南，用于查找入口、常用流程和命令。本文件是详细说明书：当简洁版中的规则、流程或术语不够清楚时，从这里查阅背景和操作边界。

本文件面向用户和研究生，解释如何使用 Wiki。它不替代以下治理文件：

- `AGENTS.md`：Agent 行为契约；
- `system/schema.md`：页面类型与字段规范；
- `system/evidence-policy.md`：证据与置信度政策；
- `system/paper-evidence-gate.md`：论文级证据准入条件。

## 2. What this Wiki is / 这个 Wiki 是什么

当前 Wiki 是证据型知识问答库、研究辅助库和证据导航系统。它用于：

- 从已有知识页定位概念、判据、核素、能带和文献；
- 追踪一条主张来自哪篇论文、哪个位置；
- 区分观测事实、实验判据、模型结果和物理解读；
- 汇总竞争解释、证据缺口和研究决策；
- 将文献证据与数据处理结果连接起来，梳理创新点候选；
- 为后续科研写作准备可审查的证据基础。

## 3. What this Wiki is not / 这个 Wiki 不是什么

本 Wiki：

- 不是最终权威，不能替代原始论文阅读；
- 不保证文献完整覆盖；
- 不能仅凭已有页面生成可直接投稿的确定结论；
- 不能把尚未完成 claim-specific verification 和用户确认的 candidate evidence 写成最终论文依据；
- 不能因为未收录某类文献就断言“没有相关工作”；
- 不能用 synthesis 页面代替原始文献引用。

论文级结论必须回到 source、必要的 raw 原文、精确 locator、citation key 和人工复核，并通过 paper evidence gate。普通 Wiki 问答、研究讨论、跨来源综合和早期草稿不默认进入严格 paper evidence gate；这些场景仍应基于现有证据给出最佳可支持内容，只是需要校准措辞并说明限制。

## 4. Core layers / 核心层级

| 层级或页面 | 作用 |
| --- | --- |
| `raw/` | 原始论文、笔记、数据和图片；默认由用户管理，只有 `raw/papers/gpt/**` 与 `raw/zotero/gpt.bib` 是已授权的 Agent 文献入口 |
| `knowledge/` | 从来源中整理出的可检索、可交叉引用知识层 |
| source | 记录一篇来源实际报告了什么，并连接 raw 与 citation key |
| nucleus | 汇总一个核素的结构、相关能带、实验和来源 |
| band | 记录一条能带或双重带的观测、指认与证据状态 |
| concept | 解释可复用的概念、定义、适用条件和竞争解释 |
| observable | 记录观测量的定义、提取方法、判别作用和局限 |
| model | 记录理论模型、假设、参数依赖和计算结果 |
| experiment | 记录反应、束流、靶、装置和数据集 |
| synthesis | 跨来源比较支持证据、反证、限制与替代解释 |
| project | 围绕具体研究问题连接证据、数据结果、决策和下一步 |
| `knowledge/index.md` | 正式知识页的导航入口 |
| `system/log.md` | 只追加的操作历史 |
| `system/handoff.md` | 最近任务状态、文件修改和下一次交接 |
| `PLAN.md` | 用户维护的阶段计划、好奇点和长期研究方向 |

`PLAN.md` 管“可能去哪里”，handoff 管“上次停在哪里”。PLAN 不是执行日志或 Agent 可自由整理的任务清单。

## 5. Evidence vocabulary / 证据术语

| 术语 | 含义 |
| --- | --- |
| locator | 页码、图号、表号、能级、跃迁或数据位置等精确定位 |
| citation key | `.bib` 中用于稳定引用文献的键，不得猜测或编造 |
| `claim_kind` | 主张类型；当前 schema 使用此字段，不另造 `claim_type` |
| `review_status` | 页面级审阅状态 |
| `human-reviewed` | 用户已看过页面并完成页面层检查，不代表所有 claim 已确认 |
| `unreviewed` | 页面尚未完成用户页面级检查 |
| `needs_review` | claim-level 待审标记；`true` 表示该具体陈述仍需确认 |
| synthesis | 跨来源综合层，不是原始文献 |
| evidence gap | 当前证据链缺失的来源、观测、定位或验证步骤 |
| competing interpretation | 对同一现象或数据的竞争性解释 |
| research-note | “暂定研究推理”；保存有跨任务价值但尚未成熟的假设、迁移边界、反向检验或认识修正候选，不是正式 evidence |
| `reasoning_status` | 暂定推理的科学成熟度/处置状态；与页面审核状态分离 |

页面级 `review_status` 和 claim-level `needs_review` 是两个独立状态。Lint 通过只说明自动检查未发现阻断性结构问题，不代表科学内容全部复核完成。

Research note 还使用第三个独立状态：`reasoning_status`。新 note 为 `review_status: unreviewed`、`reasoning_status: provisional`；审核只改变人工流程状态，不能自动把推理晋升为正式知识。`promoted`、`rejected`、`superseded`、`withdrawn` 记录科学处置，修订本身写 history。

## 6. How to ask knowledge questions / 如何提问

问题中最好说明对象、比较范围、证据分类和出处要求。例如：

```text
根据知识库解释某个概念。区分观测事实、实验判据、模型结果、
作者解释和综合判断；给出来源与 locator。证据不足时明确列出缺口。
```

```text
比较 wobbling 与 signature partner 的实验判据。
只使用当前知识库证据，列出竞争解释，不要把模型结果写成实验事实。
```

```text
当前哪些来源讨论这个问题？请区分原始论文与 synthesis，
并说明哪些 claim 尚未人工复核。
```

可显式调用 `$wiki-evidence-query`。该 Skill 默认只读；知识库缺少足够出处时，应明确报告证据边界。普通问答仍可补充稳定的一般专业背景，但不得将其冒充 Wiki 已收录、已审核或已外部核验的证据，也不得用模型记忆虚构论文、数据、locator 或作者结论。

### 回答中的 Wiki 证据链接

Wiki 直接支持的事实或判断，会把已实际读取并核实的链接紧跟在对应句子或分句之后，例如：

```markdown
角分布可能因 alignment 和 mixing ratio 未独立约束而存在多个候选解。[Angular Distribution（line 17）](E:/imp/wiki/knowledge/methods/angular-distribution.md:17)
```

跨来源综合或推断应使用“综合来看”“可以推断”等校准措辞，并在该判断后并列最直接的少量链接。稳定、简单的一般专业背景不机械附 Wiki 链接；如果某个重要而具体的判断容易被误认为已有 Wiki 证据，但当前 Wiki 缺少直接支持，应在该判断处说明证据边界和 provenance。普通回答默认不在末尾重复列证据页；只有用户明确要求来源汇总、阅读清单、bibliography、claim-to-source table，或 strict paper review 确有需要时才增加独立来源区。

链接文字使用可读的页面或文献名称和 `line N`。行号必须来自实际读取的承载 claim 的行、段落、表格或小节，不得猜测；若客户端不能跳转 `file.md:line`，改用带页面名称和已核实小节/claim 定位的文件链接，并说明 fallback。Wiki 正文中的 Obsidian Wikilink 不需要因此改写。

## 7. How to ingest papers daily / 如何日常摄入论文

文献摄入与自主研究按问题价值、证据缺口、信息增益和资源成本动态推进，不采用“每天至少若干篇”或固定检索次数等机械指标；每篇仍按独立闭环处理：

1. 用户提供论文，或指定 `raw/papers/` 中的新文件；
2. Codex 阅读原文，建立或更新 source 页；
3. Codex 按 schema 更新相关 concept、observable、nucleus、band、model、experiment 和必要的 synthesis；
4. Codex 在复盘中列出新增 claims、待审 claims、竞争解释和证据缺口；
5. 用户审阅 source 页和关键 claims；
6. 可能用于论文的具体 claim 完成直接来源、locator、适用条件和竞争解释核验，并由用户确认当前拟用措辞后，才进入论文级证据池；页面整体无需先完成全面审核。

不要把聊天内容或整批未读文献机械倒入 knowledge。新文献应先检查重复、书目信息、citation key 和原始文件定位。

Agent 主动查找文献时采用 Nature-first 路由：先调用 `nature-academic-search`，低能核结构默认并行查询 CrossRef 与 arXiv并按 DOI、题名和第一作者去重；随后必须补查 Google Scholar，无法访问时再用学术镜像。Scholar 或镜像提供的 PDF 可以先进入 `raw/papers/gpt/_incoming/<run-id>/`，不能因入口不稳定直接丢弃；只有文件签名、页数、首页题名、作者、年份、DOI、SHA-256 和全库重复检查均通过，才晋升到 `raw/papers/gpt/`，并把完整核对后的 BibTeX 追加到 `raw/zotero/gpt.bib`。`raw/zotero/wiki-inbox.bib` 始终由用户/Zotero 管理，Agent 不得修改或暂存。每次获取的去凭据记录保存在 `outputs/literature-acquisition/<run-id>.json`，下载、校验、BibTeX 与 ingest 使用独立状态。

APS/PRC 或 Google Scholar 出现 Turnstile、图片验证码、QR、OTP、登录或反复安全验证时，Codex 保留原标签页并交给用户处理，不循环重试。这里的“禁用浏览器原生 Download”只禁止无法指定路径、会默认写入 Wiki 外 Downloads 的下载方式，不是禁止下载：`nature-downloader`、命令行下载器、browser-context downloader 或可靠的“另存为 Wiki 路径”均可使用。用户若手工下载到外部目录，Agent 只能读取并复制到 Wiki，不得移动、删除或清理外部原文件。

Wiki 可在不同操作系统和 AI 工具环境中使用；`.codex/`、`.obsidian/` 和个人运行参数属于本地配置，不随公共仓库分发。任务仍遵守 raw 保护、证据规则和不可逆操作确认，工作流不依赖桌面端 GUI 或 Computer Use。

用户可以明确声明某篇文献、核素、反应体系或实验方法属于当前分析、未来课题或论文写作重点。例如：

```text
这篇文章属于我当前分析/未来课题/论文写作需要重点参考的实验核结构文献，请按重点文献摄入。
```

这类声明属于 explicit user-declared priority。Codex 应据此提高摄入优先级，不得仅因质量区不属于当前核心锚点而降级处理。即使用户没有显式声明，非 A≈130 文献也不能仅因质量区被排除；仍应按实验核结构价值、证据密度和复用价值判断。

本节只说明使用接口，不记录用户的具体学位论文题目、具体实验反应道或具体核素作为个人经历。

### Rolling WIP ingest → Agent self-audit → final

摄入主体完成且检查通过后，默认流程是：

1. 长任务或中断时，Codex 显式暂存本轮摄入文件，创建/更新单一 rolling `WIP ingest:`；
2. Codex 逐篇回查全文、locator、claim kind、证据层、竞争解释和 P0/P1；等待审核或存在 hard P0 的 WIP 不 push，也不代表页面或 claims 已人工复核；
3. 摄入完整、检查通过且没有未隔离 hard P0 时，Codex 使用 `git commit --amend` 把 rolling WIP 转为 final ingest commit，不创建第二个 final commit；
4. Agent 自审不写 Human Review Record/history，不把页面升级为 `human-reviewed`，也不自行清除 `needs_review`；
5. 用户已经为普通 ingest 建立持续 commit/push 授权；除非当前指令明确要求不 push，Codex 在 H3、fresh fetch、remote ancestry 和精确 refspec dry-run 通过后使用同一 refspec 非 force push；
6. 认证、远端漂移、检查失败或未隔离 hard P0 均 safe suspend。后续问答、研究和论文证据采用时，再按具体 claim 由用户审核证据陈述。

同一分支最多保留一个 active WIP。旧式“不 commit/push，等待审核”表示不 final commit、不 push，但允许本地 WIP；若要禁止所有本地 commit，需明确写“禁止本地 WIP commit”。Safe suspend 遇到大量 Markdown diff 时也优先采用本地 WIP checkpoint，暂停本轮自动 push，减少 Codex、Git、编辑器或文件监听的持续 CPU 占用；checkpoint 在恢复并通过发布门后再发布。

默认按主题连续逐篇摄入，在自然批次完成 Agent 自审后统一 final/push；不再逐篇等待人工审核。多个 pending WIP 仍需在新任务第一次写入前比较预期文件：无重叠可独立；同一范围继续并 amend 原 WIP；依赖上游未 final 内容时记录 dependent WIP；两个独立任务需要同一共享文件时，先 final 上游或暂缓该文件。不得静默创建两个独立且修改同一文件的 WIP。

任何写任务第一次写入前建立 dirty baseline，区分本轮授权、明确承接 WIP、受保护的任务前修改和 unresolved overlap。后续发现新的必要关联文件时，只在该文件第一次写入前执行 file-entry gate；不要求每次编辑后重跑全量脚本。跨会话或 safe suspend 恢复时重新建立 baseline，并用 handoff、queue、分支/commit 和实际 diff 恢复归属。

已有 pending WIP commit 与仍留在 Git index 的 staged 文件不同：commit 不会自动混入当前 commit，任务前 staged 文件却会。write-entry 和 commit preflight 必须检查完整 cached name/stat；无关 staged 内容不得混入本轮，也不得在归属不明时擅自 unstage。若治理允许且归属明确，可先安全保存到所属 WIP；否则暂停并询问用户。

统一脚本 `system/scripts/clean_knowledge_eol_dirty.py` 只处理 tracked knowledge Markdown 的 LF/CRLF-only worktree dirty state，不忽略普通行尾空格、Markdown 双空格或 Tab。exit code `0` 表示清理流程成功，`1` 表示 substantive/mixed/unsafe 状态仍需按 baseline 和授权范围分类，`2` 表示脚本或 Git 错误并停止写操作。脚本不审批科学修改，也不替代 pending-WIP overlap 判断。

`system/review-history.md` 记录的是已经明确结束的人工审核轮次，不要求任务已经 closed，也不要求已经 push。之后可以说“列出 pending WIP”“继续审核 Sigma-over-I alignment sources”“列出最近完成的 reviews”或“哪些 review 已完成但还没写入论文？”；Codex 应从 queue、handoff、review history 和 Git 状态恢复，而不是把旧 WIP 从 Active handoff 中丢失。

审核完成后可以用短句触发 finalization，例如：

```text
审核：1... 2... 审核完毕，除以上两点外无问题。
```

Codex 应自动理解为：本轮人工审核已经结束，可以记录一条 Review history，然后按审核意见做最小修改，处理明确确认范围内的 `needs_review`，更新 overview，刷新 QMD，完成 review/final commit，并在检查通过后自动 push。是否保留 queue entry 需要独立判断；Review history 与 Pending WIP 可以同时存在。

若不想执行其中某项，需要明确写“不要更新 overview”“不要刷新 QMD”“不要 push”或“只修改不 finalization”。如果是否结束本轮审核存在歧义，Codex 不应擅自写入 Review history。

`system/review-history.md` 是 forward-looking 的人工审核轮次索引；普通 framework setup 不会自动回填旧 reviews。它记录 `review commit message`，不记录 commit hash 或 push 状态，也不把 review commit message 解释为 task closure、finalization complete 或 push complete。若用户明确要求历史审计，再单独处理。

## 8. How to review claims / 如何人工审阅

人工审阅至少检查：

- 陈述是否忠实于原文；
- claim kind 是否正确；
- locator 是否能精确定位；
- 作者解释、模型结果和实验事实是否分开；
- citation key 是否与来源唯一匹配；
- 是否遗漏限制条件、反证或竞争解释。

用户查看 source 页只足以更新页面级状态，不自动清除 `needs_review: true`。只有用户明确确认某条 claim，或明确圈定的一组 claims，Codex 才能更新对应 claim-level 状态。

### 如何根据审核优先级审核 Codex 输出

文献摄入、project、synthesis、data-analysis-bridge 和 claim-review-update 完成后，Codex 应提供 Human review triage：

- **P0 优先处置**：影响核心科学结论、关键数值/指认、数据/权限安全或论文级证据门的位置。Codex 可通过自校验、隔离、降级、L3/L4 调查或标记受阻来处置研究型 P0；只有未隔离的 hard P0、正式结论越级或权限/数据风险必须阻止 finalization 与 push。
- **P1 优先审核**：关键 source claims、evidence matrix、模型假设、跨来源总结、定义和高歧义 aliases。有时间应优先看。
- **P2 可抽查**：背景摘要、follow-up sources、evidence gaps 和 planning notes，按文件抽查即可。
- **P3 快速扫过**：index、overview、handoff/log、普通反链、格式和低风险导航。

P0/P1 是当前关键 claim 或证据项的 focused review 优先级，不要求全面审核整页或整篇文献，除非当前 claim 依赖更广上下文。局部 claim 核验和用户确认只适用于该 claim 与当前使用语境，不自动改变页面或其它 claims 的 review 状态。

审核时，source 重点核对原文与 locator；project 重点核对证据归类、研究问题和数据桥；synthesis 重点核对跨来源结论是否过强；data-analysis-bridge 重点核对数据事实、分析结果、物理解释和创新点候选是否分层。页面级 `human-reviewed` 与 claim-level `needs_review` 仍然独立，不能因整页通过就自动清除具体 claim 的待审状态。

审核点很多时，完整 P0 inventory 仍须保留且可分轮审核；“精力有限时建议先看”的 3–5 个位置只是当前阅读顺序，不得隐藏、聚合或降级其它 P0。对每个 P0/P1，审核报告可明确写：

```text
<文件 / claim ID>：通过 / 需要修改；
needs_review：保留 true / 可改为 false；
修改意见：<如有>。
```

## 9. How to use projects / 如何使用 project

Agent 新建的 project、decision 和 failure 默认保持 `unreviewed`。`confidentiality` 仅用于描述，不能限制公开 Git 仓库中的可见性；未公开的用户或合作实验数据在获得明确发布授权并建立数据 manifest 边界前，不得写入通常会被跟踪的知识页或输出文件。

Project 不必等到一个月后或数据处理全部结束才建立。出现以下任一情况即可进入 project 工作流：

- 有具体研究问题；
- 已有阶段性数据处理结果；
- 需要比较多条证据或竞争解释；
- 有明确的写作或汇报目标。

Project 可以记录研究问题、连接数据处理结果、汇总 source 与 synthesis、比较竞争解释、梳理创新点候选，并保存失败经验和研究决策。它连接已有证据，不替代 source，也不预先决定最终创新性。

### 暂定研究推理如何使用

在已授权的 ingest、reflect、project 或 synthesis 任务中，如果一项推理具有跨来源/跨任务价值、可检验性、可能改变现有判断，或丢失会造成明显研究损失，Codex 可以创建 research note。它必须把 `Grounded Evidence` 与 `Provisional Reasoning` 分开，并在 Human review triage 中告知你。普通联想、重复摘要和低价值问题不会持久化。

你可以要求保留 provisional、修改、晋升、拒绝、撤回或标记 superseded。晋升需要 Human review，并由正式 project/synthesis/method/concept 吸收、回链原始 source；research note 自身始终不替代论文证据。

## 10. How to prepare for writing / 如何为写作准备

未来写作 Skill 可基于 source、synthesis、project、citation key、数据处理结果和用户确认结论辅助：

- literature review 或 background 草稿；
- related-work 比较；
- 证据表转段落；
- 创新点候选梳理；
- 引用候选和缺失证据清单。

当前只预留接口，不创建写作 Skill。普通讨论和早期草稿可以先基于现有证据工作，并明确区分直接事实、作者解释、模型结果、跨来源综合和暂时推断；论文或投稿核查、正式引用、直接来源或原文引文、精确 locator、关键科学 claim 确认时，再执行 `system/paper-evidence-gate.md`，逐项检查 source、locator、claim kind、citation key、人工复核状态、竞争解释及 synthesis 是否被误当成原始来源。普通争议讨论本身不自动进入 strict mode。

## 11. How to use Skills / 如何使用 Skill

当前 repo 级 `$wiki-evidence-query` 用于证据型知识问答：

- 从现有 Wiki 检索并回答；
- 区分证据类型和综合判断；
- 给出来源、locator 和证据缺口；
- 默认只读，不自动修改 Wiki。

论文摄入、综合、lint 和写作目前继续使用已有 workflow 与规则文件。等真实流程稳定后，再评估 ingest、reflect、lint 或 writing Skill，避免过早固化尚未验证的流程。

### QMD 与 Skill 的关系

QMD 是 `$wiki-evidence-query` 和普通查询流程可自动调用的底层检索工具，不是另一个知识库，也不需要用户在每条问题中点名。当前 `nuclear-knowledge` collection 只索引 `knowledge/**/*.md`；research notes 仍在同一 collection，但 ordinary Q&A 会按路径/type 排除。研究型任务使用 note 时必须同时回读其 grounded sources。索引数据库保存在被忽略的 `.qmd/`，模型保存在用户缓存，两者都不进入 Git。

推荐分层：

1. 已知页面直接读取；
2. 精确词使用 `rg` 或 `qmd search`；
3. 近义概念和跨页问题使用 `qmd vsearch`；
4. 只有复杂、高价值综合才使用完整 `qmd query`；
5. 所有候选都必须回读完整页面、source 和必要的 raw locator。

维护命令（普通单篇摄入不强制每次运行 `embed`；deferred 时复盘说明原因和建议补跑时机）：

```bash
qmd.cmd status
qmd.cmd update
qmd.cmd embed -c nuclear-knowledge
```

模型缺失或损坏时才运行 `qmd pull`。不要运行 `qmd update --pull`，避免检索工具在用户存在未提交修改时隐式操作 Git。


## 12. How to reduce ingest overhead without losing evidence quality / 如何减少 Codex 摄入固定开销而不牺牲证据质量

用户日常仍然可以使用短提示词启动文献摄入；未指定模式时采用标准深入阅读模式。优化目标是减少启动文件、长 handoff/log、无过滤全库扫描、每篇强制 QMD embed、过长策略文件和超长复盘带来的浪费，不是降低用户模式要求。`reading_depth` 只在完成后记录实际覆盖状态，不从默认模式预先推定。

`ingest-strategies-detail.md` 的 detail 是 workflow detail：策略说明、长示例、复杂案例和历史说明；不是 PDF reading depth。不默认读取 detail 教程不代表降低文献阅读深度，也不代表可以省略关键图表、公式、数值或 locator 核查。需要长说明时，可以单独要求 “输出 detailed workflow recap” 或 “输出 detailed strategy-policy audit”，这两者都不是“仔细阅读 PDF”的同义词。

不应被节省的内容包括：关键 claims、locator、图表和公式、数值、transition、observable、model assumption、author interpretation，以及 observed fact / model result / author interpretation / Wiki synthesis 的分层。PDF staged evidence reading 是阅读顺序优化：先建立论文主线和结构地图，再围绕关键证据、图表、表格、公式和 locator 深入读取。若当前模式要求的核心读取未完成，Codex 应 safe suspend，说明已读范围和未完成 section / figure / table / locator，而不是伪装成更高 `reading_depth`。

多篇文献如果用户要求逐篇摄入，应逐篇完成 source、claim、locator、project relation 和 P0/P1 triage；每篇都有自己的 source-level / claim-level 审核重点，不应合并成粗略批处理。

用户主要看最终复盘中的 Result status、commit hash、是否 push、完整 P0（可分批但不隐藏）、可审核 P1、精力有限时建议先看的顺序和检查结果。

`knowledge/overview.md` 是阶段性地图，不需要每篇 source 都更新；source、project 和 synthesis 才是主要知识承载。overview deferred 不代表摄入失败。大型 project/synthesis 可维护 `Agent active summary` 作为导航入口，但 active summary 不是 source，不替代 project/synthesis 主体，也不替代原文 locator。
## 13. Git and safety / Git 与安全边界

### 90 天持续学习与发布解耦

每日 22:00（Asia/Shanghai）的持续学习任务遵循
[`continuous-learning workflow`](system/workflows/continuous-learning.md)，周期为 90 天、约 80% 核结构与 20% 相邻核科学。2–3 小时只是督促 checkpoint；主题数、来源数和是否切换问题由里程碑、信息增益、证据质量与资源决定。日/周/阶段记录分别写入 `outputs/learning-daily/`、`outputs/learning-weekly/` 和 `outputs/learning-milestones/`，队列在 `system/learning-queue.md`。

每日任务可运行 `system/scripts/wiki_automation_preflight.py` 验证仓库根目录、配置和受保护 BibTeX 基线。Git 发布前确认 dirty baseline、staged 文件、lint 和远端 ancestry；网络或认证失败时保留本地内容并记录 `content-complete / final-not-pushed`。该检查不替代普通摄入、周测和 L4 人工关口。

- 不要使用不加检查的 `git add .`；应显式暂存目标文件；
- `raw/`、PDF、论文、数据和图片不得被 Agent 误改或误提交；
- 用户维护的 BibTeX 和 Obsidian 配置应与治理改动分开确认；
- `system/handoff.md` 记录当前状态和下一次任务入口；
- `system/wip-queue.md` 只记录多个 pending WIP 的恢复索引，不保存长报告或 source claim 正文；
- 文献摄入、project、synthesis 或 framework 任务正常结束后，Codex 应自动刷新 Active handoff 并向 `system/log.md` 追加简短记录，用户不需要每次手动要求；
- safe suspend 是写回状态后结束本轮，不是后台睡眠或自动恢复；
- 长任务、余量不足、检查失败或无法可靠完成时，应 checkpoint / safe suspend，留下下一轮可继续的交接信息；
- commit/push 前运行项目规定的 lint、测试和 Git diff 检查。

## 14. Common mistakes / 常见错误

- 把 synthesis 当作原始文献；
- 把作者解释写成观测事实；
- 把模型结果写成实验事实；
- 把尚未完成 claim-specific verification 和用户确认的 candidate evidence 写成最终论文结论；
- 认为 Wiki 未收录就等于没有相关工作；
- 缺少 locator 或 citation key 时自行猜测；
- 让 Codex 大规模重写用户维护的 `PLAN.md`；
- 把本详细指南扩写成核物理百科或底层 Agent 规则副本。

## 15. Example prompts / 示例提示词

### 知识问答

```text
使用 $wiki-evidence-query，根据现有知识库回答这个问题。
区分事实、判据、模型、作者解释和综合判断，给出处并列出证据缺口。
```

### 文献摄入

```text
按 ingest workflow 摄入 raw/papers/指定论文.pdf。
先检查重复和 citation key；完成后列出新增 claim、待审 claim、
竞争解释和缺失证据。
```

### 人工审阅

```text
列出这个 source 页中 needs_review: true 的 claims、locator 和原文依据。
先生成审阅清单，不要自行改变 review 状态。
```

### Project 创建

```text
围绕这个具体研究问题提出一个最小 project 页面方案，
连接现有 source、synthesis 和阶段性数据结果；不要预设最终结论。
```

### 创新点候选梳理

```text
结合已复核证据和我提供的数据处理结果，列出创新点候选。
分别说明支持证据、竞争解释、仍缺验证和不能宣称的内容。
```

### 写作前证据检查

```text
按 paper evidence gate 检查这些拟写入论文的 claims。
列出 source、locator、claim kind、citation key、审阅状态、
竞争解释和投稿前仍需补做的检索。
```
