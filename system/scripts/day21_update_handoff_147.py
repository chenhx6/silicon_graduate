#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint146：Git H3协议前置预演与远端核定）

146完成Git H3协议五大前置事件预检并核准远端祖先关系：
1. 五大事件全通过：git branch（main）、git remote（gitee）、git fetch origin main、git merge-base --is-ancestor（exit 0证实HEAD包含远端历史无分叉）、git push --dry-run（exit 0成功预演）。
2. 发布门零故障保障：显式暂存清单（289项）与排除项保持严格物理隔离，确保15:00收束时可顺利执行非force的精确发布。

145显式暂存清单、144关口转换协议、143全链路自洽验证、142四大开放问题闭环保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-146，恢复next-continuation-146.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint147：单卡学分转移草案与防重防越界审计）

147完成Day 21单卡学分转移草案与防重防越界不变量核定：
1. 状态转移单步前进：锁定状态库由next=21/count=20严格单步进至next=22/count=21，无学分跳跃；
2. 防双计与防越界保障：仅授Day 21正式学分（completed_day_indices: [21]），禁开Day 22，不给Day 22预习学分，未打开Day 23；防早退锁保持在盘状态库count=20直至15:00硬截止。

146 H3协议预检、145显式暂存清单、144关口转换协议、143全链路自洽验证保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-147，恢复next-continuation-147.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 147")
