#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint147：单卡学分转移草案与防重防越界审计）

147完成Day 21单卡学分转移草案与防重防越界不变量核定：
1. 状态转移单步前进：锁定状态库由next=21/count=20严格单步进至next=22/count=21，无学分跳跃；
2. 防双计与防越界保障：仅授Day 21正式学分（completed_day_indices: [21]），禁开Day 22，不给Day 22预习学分，未打开Day 23；防早退锁保持在盘状态库count=20直至15:00硬截止。

146 H3协议预检、145显式暂存清单、144关口转换协议、143全链路自洽验证保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-147，恢复next-continuation-147.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint148：终末会话回执草案与全要素收束核定）

148完成Day 21终末会话回执（final-session-receipt-21）草案与全要素收束核定：
1. 回执全要素对账：当前会话ID与启动时间保真；completed=[21]、partial=[]、next=22单步递进；口试核定18/24（六维度均达3/4）；四大开放问题全部闭环（闭环率100%）；Git H3预检全通并绑定289个精确暂存文件。
2. 守护原则：在盘正式回执在15:00硬截止前保持草案状态，维持运行窗口守护至15:00时间门开启。

147单卡学分转移草案、146 H3协议预检、145显式暂存清单、144关口转换协议保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-148，恢复next-continuation-148.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 148")
