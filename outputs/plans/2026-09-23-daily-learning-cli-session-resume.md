# Docker 日报 session 无法通过 CLI picker resume：修复计划

**目标:** 让用户能够在同一 Docker 容器内从 CLI picker 找到并恢复每日 schedule 创建的非交互 session，同时保留按 session ID 精确恢复的路径；不把 Docker-local schedule 虚称为 GUI schedule。

**当前结论（只读分析）:**

- 2026-09-23 日报 session 存在于 `/root/.codex/sessions/2026/09/23/rollout-2026-09-23T22-00-09-01a0ce91-137f-7360-ba4e-d6f5b295cdb3.jsonl`，首条 metadata 的 `originator` 是 `codex_exec`、`source` 是 `exec`、`cwd` 是 `/workspace/wiki`，因此新 session 已真实创建。
- 当前 `codex resume --help` 明确说明：默认 picker 只列 interactive sessions；`--include-non-interactive` 才会把 `codex exec` session 加入 picker，`--all` 关闭 CWD 过滤。用户只输入 `codex resume` 时看不到该日报 session，是 CLI 默认筛选行为，不是 runner 没有创建 session。
- 精确 ID 恢复命令已经写入 receipt；它必须在同一个容器、同一个 `CODEX_HOME=/root/.codex` 下执行。若用户在宿主机执行，宿主机的 session store 与容器 session store 不同，也会看不到该 session。

**范围与约束:** 本计划只修改 resume 发现/登记/验证路径；不执行恢复、不重跑日报、不改变 Day 1 计数、不修改当前失败的 knowledge locator。Docker 仍是运行边界，`/root/.codex` 必须作为持久卷保留。

## 文件结构与职责

- `system/scripts/run_daily_learning.py`：生成精确 resume 命令和 picker 命令，写入每次 receipt。
- `system/scripts/run_daily_learning_daemon.py`：在 scheduler 事件中登记 schedule、项目、session 和恢复信息。
- `system/scripts/resume_daily_learning.py`：按 run ID/day index 查找 receipt，验证 session store 和项目根目录，并启动或打印 resume 命令。
- `system/prompts/daily-learning.md`：向每日 session 注入 schedule ID 和 resume 语义。
- `system/scripts/README.md`、`system/workflows/scheduled-continuation.md`：记录 Docker-local schedule 与 CLI picker 的正确用法。
- `system/tests/test_daily_learning_runner.py`、`system/tests/test_daily_learning_daemon.py`、新建 `system/tests/test_resume_daily_learning.py`：验证命令、登记和缺失 session 的失败信息。

## 任务分解（执行门：用户后续明确继续后才执行）

### Task 1：固定 CLI picker 发现命令

**Consumes:** Codex CLI `resume --help` 的实际参数：`--include-non-interactive`、`--all`、`--last`。

**Produces:** 可测试的 picker command builder。

- [ ] 在 runner 增加 `build_resume_picker_command(root, include_all=False)`，输出 `codex resume --include-non-interactive`、`-C root`、`-s danger-full-access`、`-a never`；`include_all=True` 时追加 `--all`。
- [ ] 保留 `build_resume_command(root, session_id)` 的精确 ID 路径；在 receipt 增加 `resume_picker_command`，不要用 picker 替代精确 ID。
- [ ] 为命令顺序、项目根目录、non-interactive flag 和 all/CWD 选项增加单元测试；测试不启动交互 TUI。

### Task 2：标识 schedule 创建的非交互 session

**Files:** `system/scripts/run_daily_learning.py`、`system/scripts/run_daily_learning_daemon.py`。

- [ ] 给 `codex exec` 命令增加明确的 `--thread-source scheduled`（若当前 CLI 版本接受该值），并在 receipt/event 中记录 `thread_source=scheduled`、`originator=codex_exec`、`source=exec`。
- [ ] 如果 CLI 不接受该值，保留默认 source，同时在 Wiki receipt 中使用 `schedule_id=wiki-daily-learning` 和 `session_scope=one-new-session-for-each-schedule-run` 作为稳定标识，不伪造 Codex metadata。
- [ ] scheduler `runner-started` 和 `runner-finished` 事件必须记录同一个 `run_id`、`day_index`、`schedule_id`、`project_root`、`session_id`、`resume_command` 和 `resume_picker_command`。
- [ ] 增加测试，确认每次 profile/fallback attempt 都是新 session 语义，并且失败验收仍保留 session 登记。

### Task 3：提供按日报回执恢复的 CLI 工具

**新建:** `system/scripts/resume_daily_learning.py`。

**接口:**

```text
python3 system/scripts/resume_daily_learning.py --root /workspace/wiki --run-id 2026-09-23-day-01-01 --print
python3 system/scripts/resume_daily_learning.py --root /workspace/wiki --day-index 1 --latest --print
python3 system/scripts/resume_daily_learning.py --root /workspace/wiki --run-id 2026-09-23-day-01-01
```

- [ ] 按 `run_id` 精确寻找 `outputs/learning-daily/*-run-*/run.json`；`--day-index --latest` 按 run timestamp 选择最近回执，拒绝 acceptance-only 或无 session ID 的记录，除非显式传 `--allow-failed`。
- [ ] 验证 `project_root` 等于 `/workspace/wiki`、`session_id` 为 UUID、`CODEX_HOME` 可读写，并检查 `/root/.codex/sessions/` 中存在对应 session 文件；缺失时输出“容器或 CODEX_HOME 不同/卷未持久化”的确定性诊断。
- [ ] `--print` 只输出 shell-safe 的精确 `codex resume <id> ...` 命令；默认模式使用 `os.execvp` 在同一容器中启动 Codex，不通过 shell 拼接参数。
- [ ] 对 `failed-verification` 记录允许 `--allow-failed` 恢复对话，但明确不改变学习计数或验收状态。

### Task 4：验证当前 session 和未来 schedule

- [ ] 用当前 receipt 运行 `codex resume --include-non-interactive --all -C /workspace/wiki -s danger-full-access -a never`，确认 picker 能列出 `2026-09-23-day-01-01`；再用精确 ID命令确认可进入同一对话。此步骤在执行阶段才运行。
- [ ] 保留 `/root/.codex` Docker 持久卷；重建容器后先检查 session 文件，再声称可 resume。Gitee 只恢复 Wiki 文件，不恢复 Codex 对话数据库。
- [ ] 下一次 22:00 schedule run 应产生新的 session ID；不能复用当前 `01a0ce91-137f-7360-ba4e-d6f5b295cdb3`。测试 scheduler event 和 run receipt 的一一对应关系。
- [ ] 运行全套系统测试、边界检查、preflight、Wiki lint 和 `git diff --check`；不把 GUI Scheduled 列表作为 Docker-local schedule 的验收标准。

**验收标准:** 在同一容器执行 `codex resume --include-non-interactive --all` 能发现日报 session；按 run ID 的工具能输出/启动同一 session；跨容器或缺失 `/root/.codex` 时给出明确失败原因；每次未来 schedule 触发产生新的 session 并留下可恢复回执。

**当前未执行项:** 本计划写入时未创建 resume 工具、未改 resume command、未运行 `codex resume`、未重跑日报，也未改变当前 session 或 Day 1 状态。
