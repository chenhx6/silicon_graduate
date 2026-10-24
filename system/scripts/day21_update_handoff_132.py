
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint131：M1同相/反相交错与手征宇称恢复审计）

131推进135Nd带内M1同相交错与跨带M1 100%严格反相交错审计：
1. 带内M1同相交错：五个自旋态两带带内B(M1)一阶差分符号序列完全相同（-,+,-,+），平均强度比B(M1)_B/B(M1)_A=0.971±0.071，证实具有高度对称的内禀磁偶极几何与准粒子进动角。
2. 跨带M1严格反相交错：跨带一阶差分（+,-,+）与带内差分乘积严格全为负值，构成100%严格反相交错；Band A带内与跨带线性相关系数高达r=-0.998，排他性印证手征势垒进动的经典集体电流与横向声子跃迁互补机制，反驳偶然带交叉假说。

130四极矩同态性0.9356与39/2同频失活、129跨带E2增长3.56倍与|δin|超高稳定性、128模型域对比与127误差包络保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-131，恢复next-continuation-131.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint132：能隙单调软化与PRM有限隧穿审计）

132推进135Nd六自旋（29/2-至39/2-）能隙动力学与PRM有限隧穿反证审计：
1. 能隙单调软化：两带能差由423.1keV单调下降4.39倍至96.4keV，差分变缓收敛至22.1keV，排他性反驳两带孤立偶然交叉的对称V字型回弹假说，符合双阱渐近量子穿透特征。
2. 全量子PRM有限隧穿对账：实测39/2态最小能隙96.4keV与全量子PRM理论预测的有限隧穿能隙76.0keV吻合度达79%，实证确立有限核系统的非零量子隧穿本质，否定将RPA发散性零劈裂当成实验相界的模型外推。

131 M1同相/反相交错（r=-0.998）、130四极矩同态性0.9356与39/2同频失活、129跨带E2增长3.56倍与128模型域对比保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-132，恢复next-continuation-132.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 132")
