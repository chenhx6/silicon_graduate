# 每日学习失败修复与可恢复 schedule 启动总计划

**状态:** 执行中；已完成 atomic locator 修复和 Day 1 acceptance，overnight continuation driver 正在按本计划落地；正式 Day 1 仍未计数。

**目标:** 修复 Day 1 的 durable knowledge locator 验收失败，并把每日任务改造成一个由 `.sh` 明确启动、从 `outputs/` 中的日计划 prompt 读取任务、每次创建新 Codex CLI session、可在同一容器中稳定发现和恢复的 Docker-local schedule。

**规格来源:** 用户 2026-09-24 指令；`AGENTS.md`；`system/path-contract.md`；`system/prompts/daily-learning.md`；`system/scripts/run_daily_learning.py`；`system/scripts/run_daily_learning_daemon.py`；`system/workflows/continuous-learning.md`；`system/workflows/scheduled-continuation.md`；Codex CLI `0.155.1` 的 `codex exec --help` 和 `codex resume --help`。

**全局执行门:** 计划审核通过前只允许读和修改本计划文件。审核通过后仍须先执行每个任务的失败测试/只读探针，再实施最小修复；不得把当前失败回执改成成功，不得把失败 Day 1 计入正式 30 天，不得修改 raw、PLAN 或受保护 BibTeX。

## 当前只读分析

### A. Day 1 失败根因

2026-09-23 的 runner 进程退出码为 0，日报标题、路径预检、Wiki lint 和 `git diff --check` 均通过。失败发生在 `validate_writeback()`：

1. 报告的 `knowledge-writeback` 块把 `D12-1`、`D12-7`、`AR-2` 和页码说明合并为一个 locator：`D12-1, D12-7, AR-2 (PDF pp.53-60, 76-80)`。
2. `knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md` 中存在独立的 `D12-1`、`D12-7` 和 `AR-2` 行，但不存在合并字符串。
3. `system/scripts/wiki_knowledge_writeback.py:111-117` 对每个 `sources[].locator` 做原样字符串包含检查，因此必然拒绝该块。
4. validator 在 locator 检查异常处提前返回，尚未执行 `changed_paths` 对账；这解释了 receipt 中 `changed_paths: []`，不能据此推断知识矩阵没有被修改。
5. 当前知识矩阵存在未提交的 Day 1 行，原失败 receipt 仍是 `failed-verification`，`counted_in_substantive_test=false`；这两个事实都必须保留。

结论：这是 writeback 数据结构与 exact-locator contract 的格式契约失败，发生在科学内容验收之前；不能用放宽 locator 匹配或自动拆字符串来掩盖。

### B. CLI session 未出现的根因

1. 今日 session `01a0ce91-137f-7360-ba4e-d6f5b295cdb3` 确实存在于 `/root/.codex/sessions/2026/09/23/`；metadata 标记 `originator=codex_exec`、`source=exec`、`cwd=/workspace/wiki`。
2. 当前 `codex resume --help` 明确说明：默认 picker 只显示 interactive session；`--include-non-interactive` 才会显示 `codex exec` session；`--all` 可关闭 CWD 过滤。
3. 因此裸 `codex resume` 看不到每日 session，是 CLI picker 的默认过滤，不是 schedule 没有创建 session。
4. 若在宿主机而非 Docker 内执行，宿主机的 `CODEX_HOME` 也看不到容器 `/root/.codex`；Gitee 能恢复 Wiki 文件，不能恢复 Codex 对话 session 文件。
5. `codex exec --help` 当前没有 `--name` 参数，只有 `--thread-source <SOURCE>`；不能在未验证 CLI/API 支持前声称可以用 `codex exec --name Day-01` 创建可按名称恢复的 session。

## 目标架构

```text
outputs/learning-daily/prompts/YYYYMMDD-DAYn-english-topic-slug.md
        │
        ▼
system/scripts/run_daily_learning_schedule.sh
        │  (固定 /workspace/wiki，读取 prompt，传 --thread-source scheduled)
        ▼
codex exec --json  ──> /root/.codex/sessions/...  (每次新 session)
        │
        ├── outputs/learning-daily/YYYYMMDD-DAYn-english-topic-slug-run-NN/run.json
        ├── outputs/learning-daily/YYYYMMDD-DAYn-english-topic-slug-run-NN/events.jsonl
        └── outputs/learning-milestones/2026-09-one-month-scheduler.jsonl
```

Python runner 仍负责报告、knowledge-writeback、lint、diff 和 day state 验收；`.sh` 负责把“当天 prompt → 新 CLI session”变成可审计的单一启动入口。每日 prompt 文件是运行输入的快照，不替代 `system/prompts/daily-learning.md` 的长期模板。

session 恢复分两级：

- **已验证路径:** `codex resume <session_id> -C /workspace/wiki -s danger-full-access -a never`。
- **picker 路径:** `codex resume --include-non-interactive --all -C /workspace/wiki -s danger-full-access -a never`。

“按 session name 直接 `codex resume <name>`”只有在 CLI 或 app-server 的实际命名接口被探针和测试证明后才启用；若当前 CLI 没有命名接口，使用 `session-index.jsonl` 将 `wiki-daily-day-01-2026-09-24` 映射到 UUID，并保留 picker/UUID 恢复作为真实可用路径。

## 文件结构与职责

- 新建 `system/scripts/run_daily_learning_schedule.sh`：固定工作根目录、读取当天 `outputs/learning-daily/prompts/` prompt、传递 model/search/sandbox/thread-source 参数并调用 Python runner/CLI 入口。
- 修改 `system/scripts/run_daily_learning.py`：提供 prompt snapshot、exact resume command、non-interactive picker command、session metadata 和失败计数语义。
- 修改 `system/scripts/run_daily_learning_daemon.py`：调用唯一 schedule launcher，登记 schedule/run/day/session 映射。
- 新建 `outputs/learning-daily/prompts/` 下的每日 prompt snapshot（由 runner 生成并写入对应 run directory 前不得启动 CLI）。
- 新建 `outputs/learning-daily/session-index.jsonl`：每行记录 `schedule_id`、`run_id`、`day_index`、`session_id`、`session_name_candidate`、`project_root`、`CODEX_HOME`、status 和 resume commands；它是本地恢复索引，不冒充 Codex GUI 数据库。
- 新建 `system/scripts/resume_daily_learning.py`：按 run ID/day index 查询 receipt/session index，校验容器和 session 文件后打印或 `os.execvp` 启动 resume。
- 修改 `system/prompts/daily-learning.md`：明确 atomic locator、prompt snapshot、schedule ID 和 non-interactive session 语义。
- 修改 `system/scripts/wiki_knowledge_writeback.py`：保持 exact locator 验收，提供可操作错误信息，不猜测拆分 locator。
- 修改 `system/tests/test_wiki_knowledge_writeback.py`、`system/tests/test_daily_learning_runner.py`、`system/tests/test_daily_learning_daemon.py`；新建 `system/tests/test_daily_learning_schedule.py` 和 `system/tests/test_resume_daily_learning.py`。
- 删除已被本总计划取代的旧计划文件：`outputs/plans/2026-09-23-daily-learning-failure-locator-repair.md`、`outputs/plans/2026-09-23-daily-learning-cli-session-resume.md`；不删除任何运行回执、知识页或 raw 文件。

## 执行任务

### Task 1：建立失败 fixture，先证明 locator 根因

**Consumes:** 当前失败日报、Ding source 页、现有 validator。

**Produces:** 可独立运行的 validator 回归测试；不改生产行为。

- [ ] 新增 `test_composite_locator_is_rejected_with_actionable_error`：使用当前失败字符串，断言 `valid=false`，错误指出 source path、非法 locator 和必须拆成 atomic references。
- [ ] 新增 `test_atomic_locators_are_accepted`：分别使用 `D12-1`、`D12-7`、`AR-2`，断言路径、anchor、source link 和 locator 均通过。
- [ ] 新增 `test_locator_failure_does_not_advance_day_state`：模拟报告存在但 writeback 失败，断言 runner 状态为 `failed-verification`、`counted_in_substantive_test=false`、`next_day_index` 不变。
- [ ] 运行 `python3 -m unittest system.tests.test_wiki_knowledge_writeback system.tests.test_daily_learning_runner -v`，预期新增测试先暴露当前 contract 缺口，再进入 Task 2。

### Task 2：固化 atomic locator contract

**Files:** `system/prompts/daily-learning.md`、`system/scripts/wiki_knowledge_writeback.py`、相关测试。

**Interface:** `sources[]` 的每个 `locator` 只能是 source 页中可直接匹配的单一 claim ID、页码、图表号、公式号或能级位置；多个 ID、页码范围和解释文字放到 `note`/`summary`，不进入 locator。

- [ ] 在 prompt 的 JSON 示例中把三个 locator 写成三个独立 source reference，并明确禁止逗号拼接和页码说明混入 locator。
- [ ] 保留 exact containment，增强错误信息；不自动拆模型生成的复合字符串。
- [ ] 对 `updated`、`verified-no-op` 和 changed-path 对账分别补测试；非法 locator 不得被误报为 no-op。
- [ ] 完成后运行本任务相关单测和完整 system tests；不运行真实日报。

### Task 3：核对并处理已有失败 Day 1 候选写回

**Consumes:** Task 2 contract、`outputs/learning-daily/2026-09-23.md`、当前 matrix diff、原失败 receipt。

- [ ] 先用 snapshot 对账确定 matrix 的实际变化只包含报告声明的 Day 1 行。
- [ ] 将 writeback 块改为原子 locator 候选，页码范围留在 summary/note；保留原始失败 receipt，不覆盖其 `failed-verification` 状态。
- [ ] 用 `validate_durable_knowledge(report, root, knowledge_before)` 离线验证，预期 mapped `changed_paths` 只包含 canonical matrix page。
- [ ] 若 matrix 行存在超出 Ding source locator 的科学内容，先暂停该候选并写 evidence boundary；不因修复格式而扩大 claim。
- [ ] 只有完整验收通过并由用户确认执行门后，才决定“补偿 receipt”或“重新执行正式 Day 1”；不得重复计数。

### Task 4：生成每日 prompt snapshot 与 `.sh` launcher

**Files:** `system/scripts/run_daily_learning_schedule.sh`、`outputs/learning-daily/prompts/`、`system/scripts/run_daily_learning.py`、`system/tests/test_daily_learning_schedule.py`。

- [ ] `.sh` 使用 `set -euo pipefail`，固定 `ROOT=/workspace/wiki`，拒绝从宿主机路径读取 prompt，验证 `CODEX_HOME`、prompt 文件、Git root 和 schedule ID。
- [ ] `.sh` 接收 `--run-date`、`--day-index`、`--model`、`--reasoning-effort`、`--prompt-file`；默认读取 `outputs/learning-daily/prompts/YYYYMMDD-DAYn-english-topic-slug.md`，禁止空 prompt；文件名使用 ASCII，正文尽量中文。
- [ ] `.sh` 以参数数组调用 `codex exec -C /workspace/wiki --json --search -s danger-full-access -a never --thread-source scheduled -o <last-message> - < <prompt-file>`，不使用 `--ephemeral`，不通过 `eval` 或未引用 shell 字符串拼接命令。
- [ ] runner 在 CLI 启动前生成并保存 prompt snapshot，记录 hash、run ID、day index 和 schedule ID；receipt 记录该文件路径。
- [ ] 测试只 mock `subprocess.run`，断言 root、prompt path、`--thread-source scheduled`、`--json`、`--search`、sandbox 和 no-ephemeral 参数；不启动真实 Codex。

### Task 5：解决 session 发现与恢复

**Files:** `system/scripts/run_daily_learning.py`、`system/scripts/run_daily_learning_daemon.py`、`system/scripts/resume_daily_learning.py`、`system/tests/test_resume_daily_learning.py`。

- [ ] 增加 `build_resume_picker_command(root, include_all=True)`，包含 `--include-non-interactive`；保留精确 UUID `resume_command`。
- [ ] receipt/event/session index 记录 `originator=codex_exec`、`source=exec`、`thread_source=scheduled`（只有 CLI 实际接受并返回该 metadata 时才写入），以及 `session_id`、prompt hash 和 project root。
- [ ] 新建 resume 工具：`--run-id ... --print` 输出 shell-safe 命令；默认用 `os.execvp`；`--allow-failed` 才允许恢复 `failed-verification` 对话，并明确不改变学习计数。
- [ ] 工具验证 `CODEX_HOME` 与 `/root/.codex/sessions/` 中对应文件；缺失时给出“容器不同、CODEX_HOME 不同或持久卷未挂载”的具体错误。
- [ ] `codex resume --include-non-interactive --all -C /workspace/wiki ...` 作为 picker 验收命令；该命令必须在执行阶段运行，不在本次计划编写阶段运行。

### Task 6：session name 能力门与每日 schedule 状态机

**Files:** `system/scripts/run_daily_learning_schedule.sh`、`system/scripts/run_daily_learning_daemon.py`、`outputs/learning-daily/session-index.jsonl`、相关文档和测试。

- [ ] 先用当前 CLI 版本的 `codex exec --help`、`codex resume --help` 和必要的 app-server read-only help 检查是否存在“创建时指定 session name”或“按 UUID 重命名”的公开接口。
- [ ] 若存在公开接口，使用稳定名 `wiki-daily-day-NN-YYYY-MM-DD`，写入 receipt/session index，并测试 `codex resume <name>` 命中该 session。
- [ ] 若不存在公开接口，不添加虚构的 `--name` 参数；使用 `--thread-source scheduled`、prompt 首行稳定标题、session index 的 name→UUID 映射和 `--include-non-interactive` picker。文档必须明确“name 是 Wiki 映射标签，Codex 原生恢复键仍为 UUID”。
- [ ] 每次 schedule 触发必须产生全新的 session ID；失败验证也写 session index，成功与否只影响学习计数，不影响对话恢复。
- [ ] 对 profile fallback 的每次 CLI attempt 记录 attempt ID 和 session ID，避免把 fallback session 与成功 session 混淆。

### Task 7：完整验收与正式 Day 1 决策

- [ ] 运行完整 system tests、boundary check、automation preflight、Wiki lint 和 `git diff --check`。
- [ ] 在同一 Docker 容器执行一次受控 launcher dry-run；确认 prompt snapshot、session index 和 run receipt 结构，不执行真实科学学习，除非用户单独批准重跑。
- [ ] 用户审核本总计划和 Task 3 的 Day 1 处理选择后，才执行修复或正式重跑。
- [ ] 正式重跑成功条件：新的 session ID、完整 report、atomic writeback、canonical knowledge change、lint/diff/preflight 全部通过；失败仍保持 `failed-verification`，不推进 `next_day_index`。
- [ ] 发布前显式暂存本计划涉及文件，保护当前 knowledge matrix、handoff、raw、临时目录和未纳入范围的运行日志。

## 验收标准

1. 当前 Day 1 的 locator 根因有可重复测试，复合 locator 被拒绝，原子 locator 能通过。
2. 每日任务由 `.sh` 从 `outputs/learning-daily/prompts/` 的确定文件启动，工作根目录固定为 `/workspace/wiki`。
3. 每次 schedule 运行创建新的 `codex exec` session，receipt/session index 保存 UUID、prompt、project root、schedule ID 和 resume 命令。
4. 同一容器内 `codex resume --include-non-interactive --all` 能发现非交互日报 session；精确 UUID 命令能恢复同一对话。
5. 如果 CLI 不支持原生 session name，计划不会伪造 name；改用 Wiki 映射标签和 UUID，并在文档中明确边界。
6. 没有完整验收的日报不会计入正式 Day 1/Day N，任何失败修复都不覆盖原始失败 receipt。

**执行边界:** 本轮只执行了 locator contract、acceptance mode、`.sh` launcher、prompt snapshot、picker 验证和测试；没有执行正式 substantive Day 1，没有推进 Day 1 state，没有修改 knowledge matrix 的既有未提交内容，也没有进入 acceptance session 的对话。

## 2026-09-24 execution update

- Atomic locator contract 已实现并通过回归测试；D12-1、D12-7、AR-2 的独立 locator 可以通过，原来的复合 locator 会给出明确失败。
- Day 1 acceptance 已通过新的 `.sh` launcher 运行：session `01a0cf3e-b7f4-7902-a980-ee8fe50f4496`，writeback `verified-no-op`，正式 state 保持 `next_day_index: 1`。
- CLI picker 已在同一容器通过 `codex resume --include-non-interactive --all` 搜索到该 session；尚未进入该 session 继续对话。
- 为解决学习强度不足，nightly substantive schedule 现在目标窗口为 `Asia/Shanghai 22:00–10:00`：初始 turn 完成后，在同一 session 内发送 continuation prompt，继续处理高信息增益问题，直到 deadline、硬阻塞或真实证据饱和。Acceptance mode 不启用 overnight continuation。
- 实质 Day N 通过最终验收后，runner 会生成 Day N+1 的 `YYYYMMDD-DAYn-english-topic-slug.md` prompt snapshot；失败和 acceptance-only 运行不会生成下一日正式 prompt。
- 旧的“单轮完成即结束”逻辑已改为支持 `--until HH:MM`、`--max-continuations` 和 `codex exec resume <session_id>`；正式 schedule 的默认 deadline 为次日 `10:00`。
