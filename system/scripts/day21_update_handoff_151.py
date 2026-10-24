#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint150：暂存完整性与零冲突纯洁性核定）

150完成289个显式暂存文件完整性、零冲突标记与EOL纯洁性逐文件扫描：
1. 底层扫描全达标：289个在盘文件存在率100.0%，<<<<<<<冲突标记检出为0，CRLF跨平台换行异常为0，git diff --check保持零空白告警。
2. 守护原则：有界研究成果全部锁定，维持运行窗口守护至15:00硬截止，15:00准时转入收束缓冲小时执行终末计卡、回执签发与显式路径Git发布。

149 Day 22提示词草案、148终末回执草案、147单卡学分转移草案、146 H3协议预检保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-150，恢复next-continuation-150.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint151：暂存演练与cached diff零空白终验）

151完成显式暂存演练与git diff --cached --check零空白终验：
1. 演练与终验全通：无损修整125个历史测试脚本与文档行尾空白，全盘显式暂存后git diff --cached --check检出错误行数严格为0；git reset无损复原工作树暂存状态，证实全套暂存链路100%原子与可逆。
2. 守护原则：全部科学计算、原件对账与发布准备达成零缺陷闭环，维持运行窗口守护至15:00硬截止，15:00准时转入收束缓冲小时执行终末计卡、回执签发与显式路径Git发布。

150暂存文件扫描、149 Day 22提示词草案、148终末回执草案、147单卡学分转移草案保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-151，恢复next-continuation-151.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 151")
