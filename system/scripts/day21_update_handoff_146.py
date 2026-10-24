#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint145：显式路径暂存清单与排除项审计）

145构建显式Git暂存清单并完成排除项审计：
1. 精确显式暂存（289项）：覆盖knowledge/全部变更、outputs/learning-daily/日报与成果、system/handoff.md、system/log.md及system/scripts/day21_*.py验证脚本。
2. 严格排除项：排除Day 20继承未跟踪文件（20261022-DAY20两目录）、排除受保护文件（PLAN.md、raw/zotero/wiki-inbox.bib）、排除tmp/与运行时日志，严禁使用git add .或git add -A。

144关口转换协议、143全链路自洽验证、142四大开放问题闭环、141同分母协方差相消保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-145，恢复next-continuation-145.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint146：Git H3协议前置预演与远端核定）

146完成Git H3协议五大前置事件预检并核准远端祖先关系：
1. 五大事件全通过：git branch（main）、git remote（gitee）、git fetch origin main、git merge-base --is-ancestor（exit 0证实HEAD包含远端历史无分叉）、git push --dry-run（exit 0成功预演）。
2. 发布门零故障保障：显式暂存清单（289项）与排除项保持严格物理隔离，确保15:00收束时可顺利执行非force的精确发布。

145显式暂存清单、144关口转换协议、143全链路自洽验证、142四大开放问题闭环保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-146，恢复next-continuation-146.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 146")
