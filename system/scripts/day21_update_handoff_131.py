
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint130：四极矩同态性与39/2步调一致失活审计）

130推进135Nd五自旋（31/2-至39/2-）四极矩比值同态性与步调一致失活反证审计：
1. 四极矩比值同态性：提取实测Qt(B)/Qt(A)均值严格为0.9356±0.0102（相对散度仅1.09%，最大偏差≤0.016），内禀四极形变差异刚性限定在6.4%±1.0%内，排除未混合Qt相差2倍的形状共存偶然交叉假说。
2. 39/2自旋步调一致失活：在39/2-处两带B(E2)分别骤降2.46倍与2.57倍，以1.043倍严格对称的步调同频失活且维持Qt比值0.920，排他性证明两带微观结构对称绑定，反驳非相关单粒子构型偶然带交叉。

129跨带E2增长3.56倍与带内|δin|∈[0.034,0.061]超高稳定性、128模型域对比、127误差包络[.0237700,.1867563]与124纠错保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-130，恢复next-continuation-130.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint131：M1同相/反相交错与手征宇称恢复审计）

131推进135Nd带内M1同相交错与跨带M1 100%严格反相交错审计：
1. 带内M1同相交错：五个自旋态两带带内B(M1)一阶差分符号序列完全相同（-,+,-,+），平均强度比B(M1)_B/B(M1)_A=0.971±0.071，证实具有高度对称的内禀磁偶极几何与准粒子进动角。
2. 跨带M1严格反相交错：跨带一阶差分（+,-,+）与带内差分乘积严格全为负值，构成100%严格反相交错；Band A带内与跨带线性相关系数高达r=-0.998，排他性印证手征势垒进动的经典集体电流与横向声子跃迁互补机制，反驳偶然带交叉假说。

130四极矩同态性0.9356与39/2同频失活、129跨带E2增长3.56倍与|δin|超高稳定性、128模型域对比与127误差包络保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-131，恢复next-continuation-131.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 131")
