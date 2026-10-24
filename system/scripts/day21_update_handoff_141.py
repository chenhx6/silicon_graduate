#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint140：课程交付物全要素对账与收束就绪）

140完成Day 21课程标准五大交付物全要素对账与收束就绪核定：
1. 交付物闭环核验：回忆（7层推断阶梯）、主线（135Nd与100Sn逐claim对账）、练习（可以说/不能说/下一步证据门）、反证（134偏振排他设计，16.3h达3σ）、交付（口试评分18/24与第三周REFLECT）全五项要素全部达成并经验证。
2. 治理与收束准备：全库保留needs_review: true，严禁设置human-reviewed；写回块104项结构严整有效；保持运行窗口至15:00硬截止，15:00准时转入收束缓冲小时执行终末计卡、回执与显式路径发布。

139排版异常对账、138全相空间ft对账（残差0.27%）、137相空间幂律、136口试核定18/24保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-140，恢复next-continuation-140.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint141：同母态寿命协方差相消定理与残差闭环）

141推导同母态寿命公因子协方差相消定理，闭环开放问题清单第1项：
1. 协方差正相关机制：同能级退激B(M1)与B(E2)共享拟合分母tau及约10%阻止本领系统误差，产生高达r=+0.856的强正协方差。
2. 比值误差代数抵消：在比值B(M1)/B(E2)中tau与阻止本领严格代数相消，实测31/2-态比值真实不确定度仅5.87%，较独立正交误差（15.44%）尖锐2.63倍，确立了模型严格检验精度。

140交付物全要素对账、139排版异常对账、138全相空间ft对账（残差0.27%）、137相空间幂律保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-141，恢复next-continuation-141.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 141")
