#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint132" in content
content = content.replace("research_status: active-in-progress-checkpoint132", "research_status: active-in-progress-checkpoint133")

# 2. Update Candidate pool and selection
old_cand = "132完成135Nd能隙单调软化4.39倍（423.1至96.4keV）非V字型轨迹与全量子PRM有限隧穿76.0keV对账，确立非零隧穿本质并排除偶然带交叉；131完成M1同相/反相交错（r=-0.998）；130完成Qt同态性0.9356与39/2同频失活；129/128/127完成多自旋反演与误差设计。"
new_cand = "133完成多自旋四极同态性、M1严格反相交错、声子单调软化与五大支柱实验推断阶梯综合，确立无偏证据门矩阵；132/131/130/129/128/127完成各子项量化推演与反证设计。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Add Theory/analysis exercise section for Checkpoint 133
theory_marker = "### Checkpoint132：声子软化单调性与有限隧穿劈裂反证审计"
c133_section = """### Checkpoint133：多自旋四极同态、M1反相交错与推断阶梯综合

整合127至132各项量化推演，在推断阶梯中完成五大实证支柱与证据门综合：
1. **Case 1（135Nd vs 134Pr 手征与四极矩）**：能量近简并不充分（134Pr未混合Qt相差2倍），总寿命相等不必要（135Nd两倍寿命差由能量五次方与分支比代数平衡）；五态Qt(B)/Qt(A)均值0.9356±0.0102（散度1.09%）排除形状共存；39/2态两带骤降2.5倍且对称比1.043步调一致同频失活；带内M1同相（-,+,-,+）与跨带M1 100%严格反相（+,-,+，r=-0.998）确立角动量进动互补跃迁机制；能差单调下降4.39倍至96.4keV与全量子PRM有限隧穿76.0keV对账，排他性反驳偶然带交叉V字型回弹模型。
2. **Case 2（34Si vs 35Si 质子气泡与双体SO力）**：敲出反应谱因子为反应模型提取量而非空间电荷直接成像；2s1/2敲出单极张量项严格为零，中子2p劈裂压低完全由双体自旋-轨道力承载；GCM动力学四极涨落与有限电荷半径将中心耗尽平滑至0.09。
3. **Case 3（135Pr 摆动双解与偏振排他）**：角分布多极混合比双解严禁由模型预期挑选，集体转动模式性质必须由联合线偏振或内转换系数独立消解多解简并（排他确立小模解M1主导否定横向摆动）。
4. **Case 4（133Ce MχD与跨核借用禁令）**：能级寿命为全通道倒数和，严禁借用同中子素或邻核寿命替代本核未测的绝对矩阵元，MχD确证必须依赖本核 partner-resolved 绝对矩阵元与寿命。
5. **Case 5（76Ge 库仑激发与截断伪刚性假象）**：四体闭环四阶矩与高阶弥散度收敛极慢，有限态截断人为切除高能涨落导致四阶矩接近二阶矩平方制造方差趋零假象，严禁将截断不变量方差趋零作为刚性形变排他实证。代码见 system/scripts/day21_checkpoint133_cross_pillar_synthesis.py，基准输出 cross-pillar-synthesis-scope-133.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c133_section + theory_marker)

# 4. Update Durable knowledge delta text
old_delta = "132更新knowledge/sources/lv-2019-chirality-135nd-reexamined.md的LV19-D21-R132-1及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的能隙单调软化与PRM有限隧穿对账；131更新M1同相/反相交错；130更新Qt同态性0.9356；129/128/127更新多自旋反演与误差合同。"
new_delta = "133更新knowledge/methods/experimental-claim-boundaries.md的推断阶梯综合矩阵；132更新LV19-D21-R132-1与能隙软化；131更新M1同相/反相交错（r=-0.998）；130更新Qt同态性0.9356与39/2失活；129/128/127更新多自旋反演与误差合同。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 5. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/methods/experimental-claim-boundaries.md":
        item["summary"] = "124纠正过强量词；133完成多自旋四极同态、M1严格反相交错、声子单调软化与五大支柱实验推断阶梯综合，确立无偏证据门矩阵；保留原review/flags。"
    elif item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "130核准Qt同态性0.9356与39/2同频失活；131核准带内M1同相与跨带M1反相交错（r=-0.998）；132完成能隙单调软化4.39倍与PRM有限隧穿76.0keV对账；133完成推断阶梯综合；无新CI。"

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 6. Update Verification and continuation
assert "132实际检查见本run required-checks-132.json" in content
content = content.replace("132实际检查见本run required-checks-132.json", "133实际检查见本run required-checks-133.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 133 via JSON-parsed writeback!")
