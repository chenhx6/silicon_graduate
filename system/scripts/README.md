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
`Asia/Shanghai` 每日 22:00 触发；每次 runner 调用都会启动新的 `codex exec`
session，不复用固定 session。`run.json` 保存 `session_id`、
`session_mode: new-session-per-run` 和可直接复制的 `resume_command`；scheduler
事件也记录这些字段。计划已授权网络检索、`danger-full-access` 和 L1–L4 工作。
不读取 Docker socket、不调用 PowerShell、不创建宿主机 scheduler。`--once` 仅用于容器内显式测试，不能替代常驻调度。

runner 在日报标题检查之外，还验证 `## Durable knowledge delta` 中唯一的
`knowledge-writeback` JSON 区块：每个 item 必须解析到 `knowledge/` canonical 页面、页内 anchor、`knowledge/sources/` 和 source locator；`updated` 还必须通过运行前后的 knowledge 快照变化检查，`verified-no-op` 必须证明没有变化。该验收失败时不推进 day state，避免“只生成日报、没有知识回写”被计为成功。
