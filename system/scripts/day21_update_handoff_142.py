#!/usr/bin/env python3
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint141：同母态寿命协方差相消定理与残差闭环）

141推导同母态寿命公因子协方差相消定理，闭环开放问题清单第1项：
1. 协方差正相关机制：同能级退激B(M1)与B(E2)共享拟合分母tau及约10%阻止本领系统误差，产生高达r=+0.856的强正协方差。
2. 比值误差代数抵消：在比值B(M1)/B(E2)中tau与阻止本领严格代数相消，实测31/2-态比值真实不确定度仅5.87%，较独立正交误差（15.44%）尖锐2.63倍，确立了模型严格检验精度。

140交付物全要素对账、139排版异常对账、138全相空间ft对账（残差0.27%）、137相空间幂律保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-141，恢复next-continuation-141.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint142：开放问题全项闭环与卡片交付物精细对账）

142完成Day 21四大开放问题全要素闭环与交付物精细对账：
1. 四大开放问题全项闭环：缺口1（寿命协方差抵消使B比误差尖锐2.63倍，闭环于141）；缺口2（998/997拟合残差、334.4印刷脱漏与LaTeX续表假象，闭环于139）；缺口3（全相空间与EC能隙阻尼将残差缩减至0.27%，证实假说H1，闭环于137/138）；缺口4（225.8keV康普顿偏振排他反证设计，16.3h达3σ，闭环于134）。
2. 卡片交付物精细对账：回忆（7层推断阶梯）、主线（135Nd与100Sn全态原件对账）、练习（三段式证据门准则）、反证（线偏振P>0判决）、交付（口试评分核定18/24与第三周REFLECT深度自审）五大要素全部达成；全库严格保留needs_review: true。

141同分母协方差相消、140交付物全要素对账、139排版异常对账、138全相空间ft对账保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-142，恢复next-continuation-142.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 142")
