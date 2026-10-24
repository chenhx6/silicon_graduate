
from pathlib import Path

handoff_path = Path("system/handoff.md")
content = handoff_path.read_text(encoding="utf-8")

old_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint128：模型预测域对照与跨实验系统差异审计）

128推进135Nd手征与竞争模型预测域对账及反演混合比有界性审计：
1. 竞争模型预测域：全量子PRM（Qi 2009）低自旋预测R_M1∈[0.020,0.040]与实测0.0311[0.025,0.039]吻合，但转子对称性低估跨带E2（预测[0.018,0.054] vs 实测[0.113,0.172]）；近谐TAC+RPA（Almehed 2011）声子选择定则压低带外E2（[0.010,0.030]），实测高出4倍以上排他性确立非谐性/γ软振动；两带解混合模型（Petrache 2006）若解释为偶然带交叉，要求4个自旋内维持恒定混合角θ≈45°，物理上支持手征对称性。
2. 实测R_E2反演：由R_E2=C/f225反演得到225.8keV辐射E2份额f225∈[0.00122,0.00186]（|δ225|∈[0.0350,0.0432]），高度符合低能带内近纯M1转动辐射规律。
3. 跨实验拼接系统差异：LV19相对强度导出的M1上界D/(1-f225)≈0.020比MU07实测R_M1≈0.031低1.56倍，定量确立了JUROGAM II（152 MeV）与Gammasphere（175 MeV）跨束能/门谱条件的系统差异，严禁无联合协方差强行拼接。

127校准相消与PSD误差包络[.0237700,.1867563]、126机构访问边界、124纠错及canonical167保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-128，恢复next-continuation-128.md。"""

new_entry = """## 当前唯一执行入口 — Day21继续（Checkpoint129：多自旋反演稳定性与E2手征隧穿演化审计）

129推进135Nd多自旋（31/2-至37/2-）跨带E2增长机制与带内混合比反演：
1. 跨带E2单调增长：实测跨带/带内比值R_E2单调增长3.56倍（0.139至0.497），直观再现由低自旋手征振动（声子选择定则压低带外E2）向高自旋静态手征隧穿（对称/反对称波函数使跨带与带内E2矩阵元趋同，R_E2->1）演化的理论图像。
2. 带内混合比超高稳定性：同母态反演得到的带内辐射E2份额在四个态严格处于0.11%–0.37%（|δin|∈[0.034,0.061]），与转动带内低能近纯M1规律高度吻合，定量证实Gammasphere与JUROGAM II在四极形变空间具有深刻物理自洽性。
3. 跨实验M1波动：跨实验M1比值因子在0.98至5.21间剧烈波动，量化揭示了独立实验在门宽选择、效率校正与feeder扣除上的测量依赖性，确立严禁无协方差跨实验强行合成置信区间的证据门。

128模型域对比、127误差包络[.0237700,.1867563]、126机构边界与124纠错保持；无学分/发布/Day22，仍同session今日15:00截止。联合实际检查见required-checks-129，恢复next-continuation-129.md。"""

assert old_entry in content, "Old entry not found"
content = content.replace(old_entry, new_entry)
handoff_path.write_text(content, encoding="utf-8")
print("Handoff updated to Checkpoint 129")
