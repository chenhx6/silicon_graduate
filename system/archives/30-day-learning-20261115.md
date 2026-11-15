---
type: system-archive
graph-excluded: true
status: archived
updated: 2026-11-15
---

# 已完成的 30 天学习计划：历史约定归档

2026-11-15，用户确认 30 天学习计划已完成，并要求从全局约定中清理或归档该计划的要求。此日期是清理决定的日期，不推定为最后一天课程的实际完成日期。

本页仅供追溯，以下引文均为已退役的历史规则，不是当前任务指令，也不属于会话启动必读材料。原计划的固定作息、课程日卡、预习计分、每日 prompt、模型 fallback 和容器调度要求不再自动适用于普通研究或新会话。恢复旧 session 用于讨论历史，也不等于重启计划。新学习周期须有新的任务范围和授权。

长期自主研学、文献及 SI 获取、L4 研究与科学证据要求继续由现行 [自治研究工作流](../workflows/autonomous-research.md) 和 [原始材料留档工作流](../workflows/research-archive.md) 管理。课程结束不撤销与后续研究相关的长期授权，也不要求自动延长课程。

## 历史材料入口

- [原持续学习工作流](../workflows/continuous-learning.md)：保留历史执行细节，已标为归档。
- [原学习队列](../learning-queue.md)：保留课程候选和旧周期说明，已标为归档。
- [定时续跑工作流](../workflows/scheduled-continuation.md)：每日 daemon 章节仅作历史运行参考；通用调度可靠性约定继续适用。
- `outputs/learning-daily/`：保留日报、课程 prompt、审计、回执和调度记录，按需查看。
- `raw/papers/gpt/learning-daily/` 及其它 `raw/<type>/gpt/learning-daily/`：保留既有原始材料，不迁移或重写。
- 已形成的 `knowledge/` 页面继续是长期知识来源，不因课程结束降级或撤回。

本次只调整治理文档，未启动、停止或修改 daemon、scheduler 配置、课程 state 或既有运行回执；不据此宣称完成了运行环境停机核验。

## 原 AGENTS.md 专节（历史原文）


用户已明确授权 `daily-learning` 模式在 Wiki Docker 容器内使用 Codex
`danger-full-access`、联网和仓库工具，直接推进 L1/L2/L3/L4 学习、文献检索、
公开/可访问数据分析及工作流优化；不需要另行等待普通 L4 启动语句。每次日报
runner 调用都是新的 Codex session，回执必须保存 `session_id` 和可复制的
`resume_command`，以便用户回到某一日讨论。arXiv、NNDC/ENSDF、Google Scholar、
Crossref、出版商和机构页面都是该计划的正常检索入口。Docker 与 `/workspace/wiki`
是执行边界，Gitee 是恢复远端；不得把容器内授权误写成宿主机或其它项目授权。
证据分层、locator、可复现性和失败记录仍必须保留，模型结果不得冒充实验事实。
当前 daily daemon 的模型优先级为 `gpt-6-luna/max → gpt-6-sol/high → gpt-6-astra/medium`；GPT-5.6 不再作为运行 fallback。用户于 2026-10-28 进一步确立根本准则：Codex 应以真正的核结构博士研究生标准开展研究，无限制地自主学习、调研与深入推演，能力全面开放至 L4 全自动研学，目标是成为核结构专家。学习不能停止，研究不能停止；必须充分利用配置的 API 与网络检索工具，针对未决的理论争议与实验盲区主动开展独立调研；一直学习到要求的收束时间（如每日 15:00），届时再收束并输出报告、不足剖析及次日准备文档。
每日 schedule 的稳定标识是 `wiki-daily-learning`，项目根目录为 `/workspace/wiki`；每次触发必须创建新 Codex session，并在 `run.json` 与 scheduler 事件中保存 session ID 和 resume 命令。Docker-local session 不自动等同于宿主机 GUI Scheduled 对象。
每日学习正常计划于 Asia/Shanghai 16:00 启动，研究硬截止为本次 `run_date` 次日 15:00；15:00–16:00 专用于收束。checkpoint、单个来源完成或局部证据饱和都不代表整段计划完成：每次准备提前结束前先核对当前时间、原始回执截止、重建后的候选池和下一张未完成课程卡；有足够时段时继续当前问题。若当前问题饱和且距离硬截止至少 120 分钟，可预习恰好一张下一日课程卡的知识，但须保持今日 `day_index`、只列入 `partial_day_indices`，不给该卡学分、不将 `next_day_index` 越过该卡、也不打开 Day+2；预习完整知识仍留待该日正式运行后计卡。只有当前问题与这一项下一日预习均无高价值路线，且已检查下一张卡后，才可基于证据饱和提前收束。完整规则由 `system/workflows/continuous-learning.md` 和每日 prompt 维护，课程状态仅在逐卡审计、日报、知识写回、检查、续接提示和发布门通过后推进。
下一日课程 prompt 的 canonical 入口固定为 `outputs/learning-daily/prompts/YYYYMMDD-DAYN-*.md`。run 目录可以保留 `prompt-dayN.md` 作为 provenance copy，但 handoff、receipt、scheduler 参数和下一日恢复说明必须指向 `outputs/learning-daily/prompts/` 下的 canonical 文件；closeout 前必须检查该路径存在且内容与交接版本一致。


## 从长期记忆移出的计划执行记录（历史原文）

- 2026-10-27 用户重申每日学习长期授权：“DAY每日学习不许问。默认能学尽学，应学就学，自行获取应该获取的文章、文件等等一切资源。”在 `daily-learning` 中，正文、Supporting Information（SI）、必要附件/数据/代码及其它应学资源由 Codex 自主选择、检索、获取和核验；默认正文及可用SI，不再询问要不要下载或要不要SI，也不因外部skill的SI确认提示中断学习。该要求跨日、跨session沿用，不只是当前批次偏好。输入不可得时记录已查路线和缺口，继续可解析问题，不把普通学习选择变成用户待办。

- 2026-09-22 用户明确：每日学习自动化必须完全运行在 Docker 内。使用容器内 `run_daily_learning_daemon.py` 负责 Asia/Shanghai 22:00 调度；不得使用宿主机任务计划、Docker socket、PowerShell 或外部 project cron。

- 2026-09-25 用户将每日学习 daemon 的触发时间从 22:00 调整为 Asia/Shanghai 16:00，以便在当天更早验证自启动和 runner 修复；Docker 内运行边界不变。

- 2026-09-23 用户确认：日报 runner 每次用新的 `codex exec` session，不复用固定 session；`run.json` 必须保存 `session_id`、`session_mode` 和可复制的 `resume_command`，便于按日恢复讨论。2026-09-22 的 Day 1/Day 2 仅作为 Docker/runner 实例验收，全部标记为 `acceptance-only`，不计入新的 30 个实质成功日；状态从 `next_day_index: 1` 重新开始。

- 2026-09-23 用户确认：30 天 daily-learning 允许联网使用 arXiv、NNDC/ENSDF、Google Scholar、Crossref、出版商和机构页面，并可自主进入 L1/L2/L3/L4；容器内使用 Codex `danger-full-access`，Gitee 作为恢复远端。证据 locator、来源分层和可复现失败检查仍须记录。

- 2026-09-23 用户更新模型偏好：daily daemon 优先使用 `gpt-6-luna` reasoning `max`，失败时回退到 `gpt-6-sol` `high`，再回退到 `gpt-6-astra` `medium`；GPT-5.6 系列从 daily-learning fallback 中废弃。

## 从全局清单移出的每日执行检查（历史原文）

- [ ] 每日学习遇到问题/来源局部饱和时，先核对实时钟和硬截止，再重建候选池并检查下一张未完成日卡；至少剩 120 分钟时可预习恰好一张 Day+1 卡的知识，但保持今日 `day_index`、只记 `partial_day_indices`，不推进其学分或越过它更新 `next_day_index`，也不打开 Day+2；15:00 前不把 checkpoint/局部饱和当作全日收束，15:00–16:00 只做 closeout；逐卡完成审计通过后才推进状态。
- [ ] 每日学习日报包含唯一 `knowledge-writeback` JSON 区块；每个 item 的 knowledge anchor、source path 和 locator/claim ID 在正文中存在，`updated` 有运行前后 knowledge 变更，`verified-no-op` 有 grounded page 与无变化理由。
- [ ] 每日 runner 每次调用 `codex exec` 创建新 session；`run.json` 含 `session_id`、`session_mode: new-session-per-run` 和 `resume_command`（若 CLI 返回 session ID）。
- [ ] 下一日课程 prompt 已写入 `outputs/learning-daily/prompts/YYYYMMDD-DAYN-*.md` canonical 入口；run 目录中的 `prompt-dayN.md` 若存在仅标记为 provenance copy，handoff/receipt/scheduler 参数没有指向它。
- [ ] 已有交互式日学习 session 使用 `run_learning_session_clock.py` 时，先检查 dry-run、receipt/session 身份与次日 15:00 截止；同一计时进程持有 daemon/runner 锁，只向既有会话排队，不创建 session 或推进 state。心跳、队列接受和实际执行分别留证；普通checkpoint最多一条未确认，后续合并，hard-cutoff独立保留。整轮receipt completed立即退出，卡内容complete仍running；旧消息送达不得重开已完成run。用户停止时一并停止计时监督。

## 原详细指南中的每日执行说明（历史原文）


每日 16:00（Asia/Shanghai）的持续学习任务遵循
[`continuous-learning workflow`](../workflows/continuous-learning.md)。当前从新的 Day 1 开始计数 30 个实质成功日，之前的 Day 1/Day 2 仅作为实例验收，不计入测试。用户已授权该 Docker 计划联网、`danger-full-access` 和 L1–L4 自主推进；每次运行创建新的 Codex session，回执保存 `session_id` 和 `resume_command`。2–3 小时只是 checkpoint。默认学习截止是本次 `run_date` 次日 15:00，15:00–16:00 留作收束；checkpoint 或单个问题的证据饱和不代表整段学习完成。runner 持续刷新当前时刻和未完成课程卡：至少剩 120 分钟时继续当前高价值问题；问题饱和后重建候选池，可预习恰好一张 Day+1 卡的知识，保持今日 `day_index` 并只记录为 partial，不推进其学分或打开 Day+2。90–119 分钟继续当前问题或有限预览，少于 90 分钟不打开新卡/来源。课程只按正式日卡和逐卡交付审计推进；预习不计学分。日报、周报、审计、计划和运行回执写入 `outputs/`；可复用的 source/project/synthesis/矩阵知识写入 `knowledge/`，队列在 `system/learning-queue.md`。

Docker 内每日任务通常由 `system/scripts/run_daily_learning_daemon.py` 在 16:00（Asia/Shanghai）触发；可用 `--dry-run` 检查下一次触发时间和 runner 命令。daemon 不在运行时，可手动执行 `./system/scripts/run_daily_learning_at.sh --at 'YYYY-MM-DD HH:MM' --prompt-file <prompt> --day-index <N>`，让前台脚本等待后调用同一个 runner。它与 daemon 共用单实例锁；终端和容器必须保持运行，不能唤醒休眠或停止的主机/容器。等待时可用 Ctrl+C 取消；任务启动后 Ctrl+C 会中断 runner 并将 scheduler 状态记为失败，日报可能不完整。任务可以使用 arXiv、NNDC/ENSDF、Google Scholar、Crossref 以及出版商/机构页面。可运行 `system/scripts/wiki_automation_preflight.py` 验证路径契约、仓库根目录、配置和受保护 BibTeX 基线；也可单独运行 `python3 system/scripts/wiki_boundary_check.py --root .`。每次日报回执都可直接恢复到对应 session 讨论；Gitee 用于容器外恢复 Wiki 数据。

手动恢复交互式学习 session 而没有 foreground runner 时，可用 [已有会话计时监督](../scripts/README.md#已有交互式学习会话的计时监督) 排队 2–3 小时检查点和次日 15:00 收束提示。它持有 daemon/runner 锁，不另开研究会话或推进学分；心跳证明计时进程在线，queue 接受记录和同会话实际执行记录分别核对。容器与 app server 必须持续在线，用户停止学习时一并停止监督器；该程序不会自动启动下一日运行。

每次实质日报完成且 writeback、路径、lint、diff 和 runner 验收均通过后，Codex 自动显式暂存本轮任务文件、commit 并 push 到 Gitee，不等待周报或周度 gate。暂存前建立 dirty baseline，只包含本轮 `knowledge/`、日报/续接 prompt、回执和必要交接文件；不得使用 `git add .`，不得纳入继承改动、raw 原件、受保护 Zotero BibTeX、凭据或临时日志。发布遵循根目录 `AGENTS.md` 与 `check.md` H3 的 ancestry、dry-run 和精确非 force refspec。验证或 Git 发布门失败时保留本地内容并记录 `final-not-pushed` 与原因；科学结论为 partial/stopped 或普通 `needs_review` 不单独阻止已通过检查的发布。


## 其它退役的计划绑定记录（历史原文）

- 2026-09-23 用户明确 schedule 语义：每日计划使用固定 `wiki-daily-learning` schedule ID 和 `/workspace/wiki` 项目根目录，每次触发必须新建 session，并可凭 `run.json` 的 `resume_command` 恢复。Docker-local CLI schedule 不会自动出现在宿主机 Codex GUI Scheduled 列表，不能把本地 session 误称为 GUI schedule。

- 2026-10-28：用户确立根本准则：Codex 应以真正的核结构博士研究生标准开展研究，无限制地自主学习、调研与深入推演，能力全面开放至 L4 全自动研学，目标是成为核结构专家。学习不能停止，研究不能停止；必须充分利用配置的 API 与爬虫检索工具，针对未决的理论争议与实验盲区主动开展独立调研；一直学习到要求的收束时间（如每日 15:00），届时再收束并输出报告、不足剖析及次日准备文档。Subagents 采用 gpt-5.6-luna (max/fast)，在 subagents 工作的同时主代理也必须同步持续开展研究推演，不出现等待闲置；对话面板只看最终结果，不展示过程性中间回复。

- [ ] Docker daily-learning 只由 daemon 或用户显式启动的前台等待器之一持有时钟；手动等待器共用 daemon 单实例锁、记录 heartbeat/session/exit receipt，并明确不能唤醒休眠的主机或容器；Ctrl+C 在等待阶段不标记 runner 启动，在运行阶段记录失败/130。

- [ ] 当前 Day 1/Day 2 实例验收回执标记为 `acceptance-only`，不计入重新开始的 30 个实质成功日；正式状态从 `next_day_index: 1` 开始。
