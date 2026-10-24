#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint149：Day 22准备模板核验与收束闭环）

149完成Day 22准备入口提示词模板核定与收束闭环就绪：
1. 要素完整继承：全面继承Day 21口试18/24、四大开放问题闭环、225.8keV偏振反证设计及100Sn全相空间对账；紧扣Day 22课程要求（横向/纵向wobbling、Frauendorf 2014、Hamamoto 2003、反例检验）。
2. 防早启隔离：提示词模板暂存于next-day-prompt-draft-scope-149.json，在盘正文提示词严禁提前创建，严格恪守“本文件不启动Day22”边界；维持运行窗口守护至15:00硬截止。

148终末回执草案、147单卡学分转移草案、146 H3协议预检、145显式暂存清单保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-149，恢复next-continuation-149.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint150：暂存完整性与零冲突纯洁性核定）

150完成289个显式暂存文件完整性、零冲突标记与EOL纯洁性逐文件扫描：
1. 底层扫描全达标：289个在盘文件存在率100.0%，<<<<<<<冲突标记检出为0，CRLF跨平台换行异常为0，git diff --check保持零空白告警。
2. 守护原则：有界研究成果全部锁定，维持运行窗口守护至15:00硬截止，15:00准时转入收束缓冲小时执行终末计卡、回执签发与显式路径Git发布。

149 Day 22提示词草案、148终末回执草案、147单卡学分转移草案、146 H3协议预检保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-150，恢复next-continuation-150.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 150")
