#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint142：开放问题全项闭环与卡片交付物精细对账）

142完成Day 21四大开放问题全要素闭环与交付物精细对账：
1. 四大开放问题全项闭环：缺口1（寿命协方差抵消使B比误差尖锐2.63倍，闭环于141）；缺口2（998/997拟合残差、334.4印刷脱漏与LaTeX续表假象，闭环于139）；缺口3（全相空间与EC能隙阻尼将残差缩减至0.27%，证实假说H1，闭环于137/138）；缺口4（225.8keV康普顿偏振排他反证设计，16.3h达3σ，闭环于134）。
2. 卡片交付物精细对账：回忆（7层推断阶梯）、主线（135Nd与100Sn全态原件对账）、练习（三段式证据门准则）、反证（线偏振P>0判决）、交付（口试评分核定18/24与第三周REFLECT深度自审）五大要素全部达成；全库严格保留needs_review: true。

141同分母协方差相消、140交付物全要素对账、139排版异常对账、138全相空间ft对账保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-142，恢复next-continuation-142.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint143：收束关口前置冻结与全链路自洽验证）

143完成进入90分钟收束关口前的全链路自洽性验证与前置状态冻结：
1. 全要素链路完备：17项核心量化产物（104至142）全部核验在盘且可独立复现；四大开放问题全项闭环；五大课程交付物全要素对齐；写回块104项结构严整有效。
2. 治理与过渡协议：受保护路径零侵入改动；全库严格保留needs_review: true；随着窗口逼近90分钟，有界冻结当前研究，不开启新源/卡，维持运行窗口开放至15:00硬截止，15:00准时转入收束缓冲小时执行终末计卡、回执与显式路径发布。

142四大开放问题闭环、141同分母协方差相消、140交付物对账、139排版异常对账保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-143，恢复next-continuation-143.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 143")
