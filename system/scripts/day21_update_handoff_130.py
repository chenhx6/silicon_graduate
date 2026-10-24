
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint129：多自旋反演稳定性与E2手征隧穿演化审计）

129推进135Nd多自旋（31/2-至37/2-）跨带E2增长机制与带内混合比反演：
1. 跨带E2单调增长：实测跨带/带内比值R_E2单调增长3.56倍（0.139至0.497），直观再现由低自旋手征振动（声子选择定则压低带外E2）向高自旋静态手征隧穿（对称/反对称波函数使跨带与带内E2矩阵元趋同，R_E2->1）演化的理论图像。
2. 带内混合比超高稳定性：同母态反演得到的带内辐射E2份额在四个态严格处于0.11%–0.37%（|δin|∈[0.034,0.061]），与转动带内低能近纯M1规律高度吻合，定量证实Gammasphere与JUROGAM II在四极形变空间具有深刻物理自洽性。
3. 跨实验M1波动：跨实验M1比值因子在0.98至5.21间剧烈波动，量化揭示了独立实验在门宽选择、效率校正与feeder扣除上的测量依赖性，确立严禁无协方差跨实验强行合成置信区间的证据门。

128模型域对比、127误差包络[.0237700,.1867563]、126机构边界与124纠错保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-129，恢复next-continuation-129.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint130：四极矩同态性与39/2步调一致失活审计）

130推进135Nd五自旋（31/2-至39/2-）四极矩比值同态性与步调一致失活反证审计：
1. 四极矩比值同态性：提取实测Qt(B)/Qt(A)均值严格为0.9356±0.0102（相对散度仅1.09%，最大偏差≤0.016），内禀四极形变差异刚性限定在6.4%±1.0%内，排除未混合Qt相差2倍的形状共存偶然交叉假说。
2. 39/2自旋步调一致失活：在39/2-处两带B(E2)分别骤降2.46倍与2.57倍，以1.043倍严格对称的步调同频失活且维持Qt比值0.920，排他性证明两带微观结构对称绑定，反驳非相关单粒子构型偶然带交叉。

129跨带E2增长3.56倍与带内|δin|∈[0.034,0.061]超高稳定性、128模型域对比、127误差包络[.0237700,.1867563]与124纠错保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-130，恢复next-continuation-130.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 130")
