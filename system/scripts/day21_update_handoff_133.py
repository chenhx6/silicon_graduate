
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint132：能隙单调软化与PRM有限隧穿审计）

132推进135Nd六自旋（29/2-至39/2-）能隙动力学与PRM有限隧穿反证审计：
1. 能隙单调软化：两带能差由423.1keV单调下降4.39倍至96.4keV，差分变缓收敛至22.1keV，排他性反驳两带孤立偶然交叉的对称V字型回弹假说，符合双阱渐近量子穿透特征。
2. 全量子PRM有限隧穿对账：实测39/2态最小能隙96.4keV与全量子PRM理论预测的有限隧穿能隙76.0keV吻合度达79%，实证确立有限核系统的非零量子隧穿本质，否定将RPA发散性零劈裂当成实验相界的模型外推。

131 M1同相/反相交错（r=-0.998）、130四极矩同态性0.9356与39/2同频失活、129跨带E2增长3.56倍与128模型域对比保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-132，恢复next-continuation-132.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint133：推断阶梯与五大支柱证据门综合）

133完成推断阶梯与五大实证支柱（135Nd手征、34Si气泡、135Pr摆动、133Ce多重手征、76Ge库仑激发伪刚性）证据门综合：
1. 135Nd手征与转动模式：能量近简并不充分（134Pr实证），总寿命相等不必要（135Nd代数平衡）；五自旋Qt比值0.9356±0.0102同态性排除形状共存；39/2态两带骤降2.5倍且对称比1.043同频失活；带内M1同相与跨带M1 100%严格反相（r=-0.998）确立微观进动互补跃迁；能差单调下降4.39倍至96.4keV与全量子PRM有限隧穿76.0keV对账，排除对称V字型偶然带交叉。
2. 质子气泡与双体SO力（34Si vs 35Si）：单粒子谱因子非空间密度直接成像，2s1/2敲出单极张量为零，2p劈裂压低完全由双体SO力承载，GCM与有限半径折叠使Fsat平滑至0.09。
3. 摆动双解与偏振排他（135Pr）：角分布大小模双解严禁用理论偏好挑选，集体模式必须由联合线偏振或内转换独立排他确立。
4. 跨核借用禁令（133Ce）：能级寿命为全通道倒数和，严禁跨核素借用寿命替代未测绝对矩阵元。
5. 库仑激发截断伪刚性假象（76Ge）：四体闭环四阶矩收敛极慢，有限态截断人为切除涨落导致方差趋零假象，严禁将截断不变量方差趋零作为刚性形变排他实证。

132能隙软化4.39倍、131 M1反相交错（r=-0.998）、130四极矩同态性与124纠错保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-133，恢复next-continuation-133.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 133")
