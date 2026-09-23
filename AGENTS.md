# 低能核结构研究 Wiki：工作约定

本仓库是面向低能原子核结构研究的可追溯知识库。运行环境由使用者提供；仓库规则不假定 Docker、特定操作系统、固定路径或某个 AI 工具配置。运行权限不等于自动扩大研究范围或跳过证据审核。

## 会话启动

开始任务前依次读取：

1. `README.md`；
2. `knowledge/index.md`；
3. 与本轮任务相关的 `profile.md`、`system/memory.md` 或 `system/handoff.md`；
4. 若本地存在未跟踪的 `AGENTS.local.md`，再读取其中的运行环境补充说明。

任务涉及阶段计划或长期研究方向时，再读取 `PLAN.md`。只按本轮需要读取其它 workflow、source 和输出文件，不把 README 的链接当成自动读取清单。

Git 工作树可能包含用户或上一轮留下的修改。写入前先运行 `git status --short --branch`，识别并保留已有修改；不得使用 `git add .` 把无关文件带入提交。

## 任务边界

- 普通问答默认只读；用户明确要求摄入、综合、修复或写作时，才写入相关文件。
- 六类目录的唯一落点契约见 [`system/path-contract.md`](system/path-contract.md)：`raw/` 保存原始材料，`knowledge/` 保存长期知识大脑，`outputs/` 保存日报/周报/审计/回执/调度状态和 `outputs/plans/` 任务计划书，`system/` 保存规则/工作流/脚本/测试/交接，`tools/` 保存外部工具，`tmp/` 保存临时运行数据。
- 任何输出、计划或运行记录中产生的可复用事实、方法、证据矩阵、竞争解释、开放问题或研究设计，都必须同步写入 `knowledge/`；`outputs/` 不是第二知识库，不能成为长期问答或论文事实源。
- `docs/plans/` 已废止，不得重新创建；根目录 `PLAN.md` 仍由用户维护，不迁移到 `outputs/` 或 `knowledge/`。
- `knowledge/` 是可维护的知识层；`system/` 是治理和脚本层；`outputs/` 保存交代性输出。QMD 只索引 `knowledge/**/*.md`。
- `raw/`、`PLAN.md` 默认保持不变；需要修改时必须得到用户明确指令，并逐文件核验。`raw/zotero/wiki-inbox.bib` 是本地 Zotero 输入，不属于公共 Git 跟踪范围。
- 递归删除、历史重写、force push、覆盖原始证据等不可逆操作必须单独确认。
- 不使用桌面端 GUI 或 Computer Use 来代替终端操作。浏览器只用于检索和验证，下载应指定到仓库内路径。

### 30 天 Docker 学习计划授权

用户已明确授权 `daily-learning` 模式在 Wiki Docker 容器内使用 Codex
`danger-full-access`、联网和仓库工具，直接推进 L1/L2/L3/L4 学习、文献检索、
公开/可访问数据分析及工作流优化；不需要另行等待普通 L4 启动语句。每次日报
runner 调用都是新的 Codex session，回执必须保存 `session_id` 和可复制的
`resume_command`，以便用户回到某一日讨论。arXiv、NNDC/ENSDF、Google Scholar、
Crossref、出版商和机构页面都是该计划的正常检索入口。Docker 与 `/workspace/wiki`
是执行边界，Gitee 是恢复远端；不得把容器内授权误写成宿主机或其它项目授权。
证据分层、locator、可复现性和失败记录仍必须保留，模型结果不得冒充实验事实。
当前 daily daemon 的模型优先级为 `gpt-6-luna/max → gpt-6-sol/high → gpt-6-astra/medium`；GPT-5.6 不再作为运行 fallback。
每日 schedule 的稳定标识是 `wiki-daily-learning`，项目根目录为 `/workspace/wiki`；每次触发必须创建新 Codex session，并在 `run.json` 与 scheduler 事件中保存 session ID 和 resume 命令。Docker-local session 不自动等同于宿主机 GUI Scheduled 对象。

## 科学证据规则

1. 重要事实、数值和引文回链到 `knowledge/sources/`，尽量提供页码、图表号、公式或能级位置。
2. 分开记录实验直接报告、作者解释、模型计算和本任务推断。
3. 重复引用不等于独立证据；同一实验的论文、学位论文和综述要标明依赖关系。
4. wobbling、chirality、γ-soft/γ-rigid、shape coexistence 等争议主题必须保留反证、替代解释和适用条件。
5. 原文歧义、图表不可读、元数据或 locator 缺失时保留 `needs_review: true` 或相应 evidence boundary，不能补写确定结论；这类边界由 Codex 在研究报告中自审和追踪，不自动变成用户待办。
6. Codex 可以依据直接来源、locator、竞争解释和适用条件完成 source/claim self-audit 并更新相应证据状态；不得把 self-audit 写成 `human-reviewed`。论文写作或后续问答需要用户裁决时，再对具体 claim 触发定向确认。

A≈130 是重要研究锚点，不是收录边界。是否建立核素、实验、方法、概念或 project 页面，按来源提供的可复用结构信息、实验判据、比较价值和用户当前重点决定。

## 工作流路由

- 论文或笔记摄入：`system/workflows/ingest.md`
- 查询与回答：`system/workflows/query.md`
- 跨来源综合：`system/workflows/reflect.md`
- L0–L4 与人工关口：`system/workflows/autonomous-research.md`
- 每日持续学习：`system/workflows/continuous-learning.md`
- 定时续跑：`system/workflows/scheduled-continuation.md`
- 健康检查：`system/workflows/lint.md` 和 `check.md`
- 路径契约与漂移检查：`system/path-contract.md`、`system/scripts/wiki_boundary_check.py`

L0–L4、P0/P1 和每周自测只在 `autonomous-research.md` 维护；其它文件只做路由和任务记录。研究型任务应记录问题、证据缺口、停止原因和下一步，不以论文数量代替信息增益。

## Git 与发布

用户已为本 Wiki 建立持续自主 commit/push 授权。任务范围内完成且通过发布门的修改，Codex 可自行显式暂存、提交并推送；提交前仍必须检查 `git diff --check`、状态和 staged 文件，推送使用精确 refspec 和非 force 模式：

GitHub 仅作为由 Gitee 同步的镜像，不是本仓库的维护或 CI 入口；不要为本仓库恢复 GitHub remote、Actions 或其它 GitHub 维护链路。

```bash
git fetch origin main
git merge-base --is-ancestor origin/main HEAD
git push --dry-run origin HEAD:main
git push origin HEAD:main
```

认证由 Git 当前环境负责，禁止把 token 写入仓库、日志或脚本。网络或认证失败时保留本地提交并如实记录 `final-not-pushed`，不要改全局凭据、SSL 或 Git 配置。
普通 final commit、治理/工具修改和已通过发布门的内容默认自动 push；当前指令中的“不要 push”“只 commit”“只修改”可覆盖本轮发布。科学 partial/stopped 状态和未触发的用户审核不阻止发布；来源身份、raw/哈希、权限、凭据、危险重叠或 Git 安全问题等未隔离 hard P0 仍必须停在本地。提交后执行 post-commit reconciliation，核对状态、提交文件和 handoff。
Force push、历史重写、已发布标签改写、递归删除、raw 覆盖和其它不可逆操作仍需单独确认；持续 commit/push 授权不扩展到这些动作。当前提交用 branch + subject 作为稳定指针，最终精确 hash 只写入任务回执。

## 通用脚本

仓库脚本统一使用 Python 3，避免依赖单一 shell 或操作系统：

- `system/scripts/clean_knowledge_eol_dirty.py`：检查并清理仅由 LF/CRLF 造成的 tracked knowledge 脏状态；
- `system/scripts/wiki_automation_preflight.py`：检查仓库根目录、配置和受保护 BibTeX 基线；
- `system/scripts/wiki_boundary_check.py`：只读检查六类目录、`outputs/` 分类、已迁移知识页和 QMD collection 边界；
- `system/scripts/update_nature_skills.py`：更新或回退 Nature Skills；
- `script/git20260905.py`：按 manifest 显式暂存、提交并尝试发布批次内容。

若提供 `.cmd` 启动器，它只是 Windows 便捷入口；Linux、macOS 和 WSL 可直接运行 `python3 <script>.py`。脚本不得修改用户未授权的 raw、凭据或其它项目。

## 变更记录

必要的任务状态写入 `system/handoff.md`，日志只追加到 `system/log.md`。修改治理规则时同步更新 `check.md` 和相关用户指南；科学页面的结论、review 状态和引用元数据按原有 schema 维护。
