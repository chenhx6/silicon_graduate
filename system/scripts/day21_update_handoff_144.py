#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint143：收束关口前置冻结与全链路自洽验证）

143完成进入90分钟收束关口前的全链路自洽性验证与前置状态冻结：
1. 全要素链路完备：17项核心量化产物（104至142）全部核验在盘且可独立复现；四大开放问题全项闭环；五大课程交付物全要素对齐；写回块104项结构严整有效。
2. 治理与过渡协议：受保护路径零侵入改动；全库严格保留needs_review: true；随着窗口逼近90分钟，有界冻结当前研究，不开启新源/卡，维持运行窗口开放至15:00硬截止，15:00准时转入收束缓冲小时执行终末计卡、回执与显式路径发布。

142四大开放问题闭环、141同分母协方差相消、140交付物对账、139排版异常对账保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-143，恢复next-continuation-143.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint144：90分钟关口边界转换与收束协议执行）

144正式跨入90分钟关口线（mins_to_deadline<=90，decision转为finish-current-no-new-unit）：
1. 关口协议执行：冻结全部新源、新核素与新课题，锁定Checkpoints 104至143全部17项有界分析；不开启新课题，维持有界守护至15:00硬截止。
2. 治理与收束预案：全库严格保留needs_review: true，严禁提前授分或开启Day 22；15:00硬截止准时转入15:00–16:00收束缓冲小时，依次执行终末计卡、回执签发与显式路径Git发布。

143全链路自洽验证、142四大开放问题闭环、141同分母协方差相消、140交付物对账保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-144，恢复next-continuation-144.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 144")
