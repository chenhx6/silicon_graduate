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
python3 system/scripts/wiki_automation_preflight.py --root .
```

行尾脚本只处理 `knowledge/**/*.md` 的 LF/CRLF-only 差异；预检检查项目配置、受保护 BibTeX 哈希和仓库根目录/`.git` 的临时写探针。

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
