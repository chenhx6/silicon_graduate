#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint144：90分钟关口边界转换与收束协议执行）

144正式跨入90分钟关口线（mins_to_deadline<=90，decision转为finish-current-no-new-unit）：
1. 关口协议执行：冻结全部新源、新核素与新课题，锁定Checkpoints 104至143全部17项有界分析；不开启新课题，维持有界守护至15:00硬截止。
2. 治理与收束预案：全库严格保留needs_review: true，严禁提前授分或开启Day 22；15:00硬截止准时转入15:00–16:00收束缓冲小时，依次执行终末计卡、回执签发与显式路径Git发布。

143全链路自洽验证、142四大开放问题闭环、141同分母协方差相消、140交付物对账保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-144，恢复next-continuation-144.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint145：显式路径暂存清单与排除项审计）

145构建显式Git暂存清单并完成排除项审计：
1. 精确显式暂存（289项）：覆盖knowledge/全部变更、outputs/learning-daily/日报与成果、system/handoff.md、system/log.md及system/scripts/day21_*.py验证脚本。
2. 严格排除项：排除Day 20继承未跟踪文件（20261022-DAY20两目录）、排除受保护文件（PLAN.md、raw/zotero/wiki-inbox.bib）、排除tmp/与运行时日志，严禁使用git add .或git add -A。

144关口转换协议、143全链路自洽验证、142四大开放问题闭环、141同分母协方差相消保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-145，恢复next-continuation-145.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 145")
