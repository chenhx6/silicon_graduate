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
