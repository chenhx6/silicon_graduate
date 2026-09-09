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
- `knowledge/` 是可维护的知识层；`system/` 是治理和脚本层；`outputs/` 保存报告。
- `raw/`、`PLAN.md` 默认保持不变；需要修改时必须得到用户明确指令，并逐文件核验。`raw/zotero/wiki-inbox.bib` 是本地 Zotero 输入，不属于公共 Git 跟踪范围。
- 递归删除、历史重写、force push、覆盖原始证据等不可逆操作必须单独确认。
- 不使用桌面端 GUI 或 Computer Use 来代替终端操作。浏览器只用于检索和验证，下载应指定到仓库内路径。

## 科学证据规则

1. 重要事实、数值和引文回链到 `knowledge/sources/`，尽量提供页码、图表号、公式或能级位置。
2. 分开记录实验直接报告、作者解释、模型计算和本任务推断。
3. 重复引用不等于独立证据；同一实验的论文、学位论文和综述要标明依赖关系。
4. wobbling、chirality、γ-soft/γ-rigid、shape coexistence 等争议主题必须保留反证、替代解释和适用条件。
5. 原文歧义、图表不可读、元数据或 locator 缺失时标记 `needs-human-review`，不得补写确定结论。
6. 未经用户确认，不把 `confidence` 提升为 `high`，不把 Codex 自审写成 Human review。

A≈130 是重要研究锚点，不是收录边界。是否建立核素、实验、方法、概念或 project 页面，按来源提供的可复用结构信息、实验判据、比较价值和用户当前重点决定。

## 工作流路由

- 论文或笔记摄入：`system/workflows/ingest.md`
- 查询与回答：`system/workflows/query.md`
- 跨来源综合：`system/workflows/reflect.md`
- L0–L4 与人工关口：`system/workflows/autonomous-research.md`
- 每日持续学习：`system/workflows/continuous-learning.md`
- 定时续跑：`system/workflows/scheduled-continuation.md`
- 健康检查：`system/workflows/lint.md` 和 `check.md`

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
普通 final commit、治理/工具修改和已通过科学发布门的内容默认自动 push；当前指令中的“不要 push”“只 commit”“只修改”可覆盖本轮发布。未完成、等待人工审核或存在未隔离 hard P0 的 WIP 仍停在本地，不因持续授权而提前发布。提交后执行 post-commit reconciliation，核对状态、提交文件和 handoff。
Force push、历史重写、已发布标签改写、递归删除、raw 覆盖和其它不可逆操作仍需单独确认；持续 commit/push 授权不扩展到这些动作。当前提交用 branch + subject 作为稳定指针，最终精确 hash 只写入任务回执。

## 通用脚本

仓库脚本统一使用 Python 3，避免依赖单一 shell 或操作系统：

- `system/scripts/clean_knowledge_eol_dirty.py`：检查并清理仅由 LF/CRLF 造成的 tracked knowledge 脏状态；
- `system/scripts/wiki_automation_preflight.py`：检查仓库根目录、配置和受保护 BibTeX 基线；
- `system/scripts/update_nature_skills.py`：更新或回退 Nature Skills；
- `script/git20260905.py`：按 manifest 显式暂存、提交并尝试发布批次内容。

若提供 `.cmd` 启动器，它只是 Windows 便捷入口；Linux、macOS 和 WSL 可直接运行 `python3 <script>.py`。脚本不得修改用户未授权的 raw、凭据或其它项目。

## 变更记录

必要的任务状态写入 `system/handoff.md`，日志只追加到 `system/log.md`。修改治理规则时同步更新 `check.md` 和相关用户指南；科学页面的结论、review 状态和引用元数据按原有 schema 维护。
