#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint148：终末会话回执草案与全要素收束核定）

148完成Day 21终末会话回执（final-session-receipt-21）草案与全要素收束核定：
1. 回执全要素对账：当前会话ID与启动时间保真；completed=[21]、partial=[]、next=22单步递进；口试核定18/24（六维度均达3/4）；四大开放问题全部闭环（闭环率100%）；Git H3预检全通并绑定289个精确暂存文件。
2. 守护原则：在盘正式回执在15:00硬截止前保持草案状态，维持运行窗口守护至15:00时间门开启。

147单卡学分转移草案、146 H3协议预检、145显式暂存清单、144关口转换协议保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-148，恢复next-continuation-148.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint149：Day 22准备模板核验与收束闭环）

149完成Day 22准备入口提示词模板核定与收束闭环就绪：
1. 要素完整继承：全面继承Day 21口试18/24、四大开放问题闭环、225.8keV偏振反证设计及100Sn全相空间对账；紧扣Day 22课程要求（横向/纵向wobbling、Frauendorf 2014、Hamamoto 2003、反例检验）。
2. 防早启隔离：提示词模板暂存于next-day-prompt-draft-scope-149.json，在盘正文提示词严禁提前创建，严格恪守“本文件不启动Day22”边界；维持运行窗口守护至15:00硬截止。

148终末回执草案、147单卡学分转移草案、146 H3协议预检、145显式暂存清单保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-149，恢复next-continuation-149.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 149")
