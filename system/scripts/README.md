---
type: system-guide
graph-excluded: true
---

# 通用脚本

仓库脚本使用 Python 3，可在 Linux、macOS、WSL 和 Windows 运行。Windows 的 `.cmd` 文件只是便捷启动器，不再依赖 PowerShell。

## Nature Skills

```bash
python3 system/scripts/update_nature_skills.py --check-only
python3 system/scripts/update_nature_skills.py --no-pull
python3 system/scripts/update_nature_skills.py --rollback
```

可用 `--repo-path`、`--destination-path` 和 `--backup-root` 覆盖默认目录。更新器会检查固定上游、技能目录和 SHA-256，先写入 staging，再激活并保留 `previous` 回退副本；不会执行上游脚本。

## Git 与行尾检查

```bash
python3 system/scripts/clean_knowledge_eol_dirty.py
python3 system/scripts/clean_knowledge_eol_dirty.py --dry-run
python3 system/scripts/wiki_boundary_check.py --root .
python3 system/scripts/wiki_automation_preflight.py --root .
```

行尾脚本只处理 `knowledge/**/*.md` 的 LF/CRLF-only 差异；`wiki_boundary_check.py` 只读检查六类目录、`outputs/plans/` 计划路径、已迁移知识页和 QMD collection。`wiki_automation_preflight.py` 会先运行该边界检查，再检查项目配置、受保护 BibTeX 哈希和仓库根目录/`.git` 的临时写探针；边界失败时不会执行写探针。

## Agent hook 与 farmer

外部 Agent 能力的固定来源、采用边界和恢复约束见
[`system/agent-capability-adoption.md`](../agent-capability-adoption.md)。Hook 是显式、只读的生命周期适配器：

```bash
python3 system/scripts/wiki_hook.py session-start --root .
python3 system/scripts/wiki_hook.py before-edit --root . -- system/workflows/scheduled-continuation.md
python3 system/scripts/wiki_hook.py after-edit --root .
python3 system/scripts/wiki_hook.py session-summary --root .
```

Farmer 只读取 `CODEX_HOME/sessions/**/*.jsonl`，对 Wiki 根目录内的白名单瞬态失败排队一次固定续接消息；状态写入被忽略的 `tmp/farmer/`，不访问 Codex SQLite，也不执行 Git 发布：

```bash
python3 system/scripts/wiki_farmer.py once --root . --dry-run
python3 system/scripts/wiki_farmer.py ensure --root .
python3 system/scripts/wiki_farmer.py status --root .
python3 system/scripts/wiki_farmer.py stop --root .
```

## Docker 内每日学习调度器

每日学习不依赖宿主机任务计划。容器启动入口会拉起以下常驻进程；需要检查
下一次触发时间时，在容器内运行：

```bash
python3 system/scripts/run_daily_learning_daemon.py --root /workspace/wiki --dry-run
```

正常常驻运行使用：

```bash
python3 system/scripts/run_daily_learning_daemon.py --root /workspace/wiki
```

daemon 只调用同一容器内的 `run_daily_learning.py`，默认在
`Asia/Shanghai` 每日 16:00 触发；每次 runner 调用都会启动新的 `codex exec`
session，不复用固定 session。`run.json` 保存 `session_id`、
`session_mode: new-session-per-run` 和可直接复制的 `resume_command`；scheduler
事件也记录这些字段。计划已授权网络检索、`danger-full-access` 和 L1–L4 工作；
模型优先级为 `gpt-6-luna/max → gpt-6-sol/high → gpt-6-astra/medium`，GPT-5.6
不再作为 fallback。
不读取 Docker socket、不调用 PowerShell、不创建宿主机 scheduler。`--once` 仅用于容器内显式测试，不能替代常驻调度。

正式 `daily-learning` runner 的默认收束时刻是 `15:00`。正常 16:00 启动时，学习窗口
延续到次日 15:00；15:00 开始收束，并在 15:00–16:00 完成日报、知识回写、验证、回执和
次日提示词准备。无论本次在 15:00 前手动提前启动还是延迟启动，默认都固定为本次
`run_date` 的次日 15:00；只有明确传入 `--until` 才覆盖。receipt 的 `overnight_until`
记录实际截止。
首个 `codex exec`
完成后，runner 在同一 session 内调用 `codex exec resume <session_id>` 发送 continuation
prompt，继续处理下一个高信息增益问题；每轮都核对实时钟快照。问题局部饱和不能单独
结束 schedule：剩余至少 120 分钟时检查当前问题和下一张未完成日卡，可预习恰好一张
Day+1 卡的知识；保持今日 day_index，只记 partial，不计该卡学分，不打开 Day+2。
剩余 90–119 分钟只继续当前问题或做有限预览；不足 90 分钟不再开新来源/日卡。
硬截止后 runner 发一轮 closeout-only continuation。receipt 记录 `overnight_until`、
`continuation_count`、每轮 prompt/事件文件、收束时间快照和逐卡完成审计。continuation 上限
只限制单批计数；达到后 runner 在同一 session 内滚动批次并继续，不因此提前结束。每张完整日卡必须
附至少四项矩阵交付审计与证据/产物定位，Day 7 另需完整评分表和周度 REFLECT。`acceptance`
模式不启用 overnight 续接，也不会推进 substantive day state。

这个 `wiki-daily-learning` 是 Docker 内的 Wiki-local schedule，不会自动出现在
Codex GUI 的 Scheduled 列表中；GUI schedule 由宿主机/应用侧单独管理。要恢复某次
运行，进入同一容器执行回执中的 `resume_command`，例如：

```bash
codex resume <session_id> -C /workspace/wiki -s danger-full-access -a never
```

每次运行即使最终 `failed-verification`，只要 CLI 返回了 session ID，也会保留该
session 和 resume 信息，便于查看对话、定位失败并优化工作流。

### 已有交互式学习会话的计时监督

手动恢复的交互式 session 没有 foreground runner 时，可使用
`run_learning_session_clock.py` 给**同一 receipt 指定的会话**排队检查点与收束提示：

```bash
python3 system/scripts/run_learning_session_clock.py \
  --root /workspace/wiki \
  --receipt outputs/learning-daily/<name>-run-01/run.json \
  --thread <receipt.session_id> \
  --checkpoint-hours 2 \
  --dry-run
```

先 dry-run 检查时刻表；实际运行去掉 `--dry-run`。该进程同时持有 daemon/runner
两把锁，避免另开重复学习 session；只调用 `codex queue`，不创建 session，不修改
模型、课程 state、run receipt、raw 或 Git。2–3 小时一次检查点，按 receipt 的
run_date 次日 15:00 提醒停止新增研究，15:45 条件提醒，16:00 最多一次逾时提示后退出。
它在本 run 保存 clock-state/events 和每分钟心跳，重启按 event ID 去重；queue exit 0
只证明排队接受，执行需要同会话后续 turn 回执，等待心跳也不计为实际研究时长。
容器与 Codex app server 必须在线；超时/发送中重启记 acceptance unknown，不盲目重发。
监督器只读本 Wiki 的 `tmp/farmer/state.json`：首次实际启动后、本线程的新鲜取消或
人工处理事件会停止排队；Farmer 正在恢复时暂缓提醒，待运行/完成事件恢复后继续。旧、
过期或损坏快照只记录边界，首次启动时间在重启后保留。前台 Ctrl+C 会停止监督器并
释放锁；用户停止学习时应同时停止该计时进程。它不会自动启动下一日 daemon，下一日
仍须经过当前 run 的收束/课程验收及新 session 启动契约。

### 手动前台定时启动

若 daemon 没有运行，可在容器内手动启动一个前台单次等待器。它会按
`Asia/Shanghai` 的指定日期和时间等待，随后调用相同的日学习 runner，并把等待心跳、
prompt、session ID、resume 命令和退出码追加到
`outputs/learning-milestones/2026-09-one-month-scheduler.jsonl`：

```bash
./system/scripts/run_daily_learning_at.sh \
  --at 'YYYY-MM-DD HH:MM' \
  --prompt-file outputs/learning-daily/prompts/YYYYMMDD-DAYn-topic.md \
  --day-index 2
```

先加 `--dry-run` 可检查 target、prompt 和实际 runner 命令；漏过时间后，只有确认当天
没有重复运行时才加 `--run-now`。等待器持有和 daemon 相同的单实例锁；若 daemon 仍在运行，
它会拒绝启动，避免重复任务。等待器在前台运行，因此要保持当前终端和 Docker 容器存活；
它不能唤醒休眠或停止的主机/容器，也不使用宿主机计划任务。
等待时按 `Ctrl+C` 会取消等待且不标记 runner 已启动；runner 启动后按 `Ctrl+C` 会中断
前台 runner，记录 `manual-waiter-interrupted`，并把 scheduler 状态记为 `failed`/退出码 `130`。
被中断的日报可能只有部分产物；如需继续，先检查当次 `run.json`、事件文件和 session ID。

runner 在日报标题检查之外，还验证 `## Durable knowledge delta` 中唯一的
`knowledge-writeback` JSON 区块：每个 item 必须解析到 `knowledge/` canonical 页面、页内 anchor、`knowledge/sources/` 和 source locator；`updated` 还必须通过运行前后的 knowledge 快照变化检查，`verified-no-op` 必须证明没有变化。该验收失败时不推进 day state，避免“只生成日报、没有知识回写”被计为成功。

每日 prompt、日报和 run directory 使用可回访命名：
`YYYYMMDD-DAYn-english-topic-slug.md`，例如
`20260924-DAY1-baseline-research-contract.md`。文件名使用 ASCII English slug 以
避免脚本和跨平台路径乱码；prompt、日报正文和解释尽量使用中文，`γ`、`HFB`、
`ADO/DCO`、`L3/L4` 等特殊术语保留。

实质 Day N 通过最终验收后，runner 会提前生成 Day N+1 的 ASCII prompt 文件；失败、
acceptance-only 或未计数运行不会推进或生成下一日正式 prompt。
