#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint131" in content
content = content.replace("research_status: active-in-progress-checkpoint131", "research_status: active-in-progress-checkpoint132")

# 2. Update Candidate pool and selection
old_cand = "131完成135Nd带内M1同相交错与跨带M1 100%严格反相交错（相关系数r=-0.998）审计，确立手征势垒进动与声子互补跃迁的排他性实证；130完成Qt同态性0.9356与39/2同频失活；129/128/127完成多自旋反演与误差设计。"
new_cand = "132完成135Nd能隙单调软化4.39倍（423.1至96.4keV）非V字型轨迹与全量子PRM有限隧穿76.0keV对账，确立非零隧穿本质并排除偶然带交叉；131完成M1同相/反相交错（r=-0.998）；130完成Qt同态性0.9356与39/2同频失活；129/128/127完成多自旋反演与误差设计。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Update Sources and evidence table
old_table_row = "| MU07-D21-R131-1 | PRL 99, 172501 Table I and Fig. 3 | 两带带内B(M1)一阶差分符号完全同相（-,+,-,+），跨带差分（+,-,+）严格反相且线性相关r=-0.998，确立角动量进动手征宇称恢复机制 |"
new_table_row = old_table_row + "\n| LV19-D21-R132-1 | 024314-4 Table I Bands D5 and D6 | 两带能差由423.1单调降至96.4keV排除V字型偶然交叉；39/2态96.4keV与PRM有限隧穿76.0keV吻合度79%，确立非零隧穿本质并否定RPA零劈裂外推 |"
assert old_table_row in content, "Table row not found"
content = content.replace(old_table_row, new_table_row)

# 4. Add Theory/analysis exercise section for Checkpoint 132
theory_marker = "### Checkpoint131：带内M1同相交错与跨带M1反相交错反证审计"
c132_section = """### Checkpoint132：声子软化单调性与有限隧穿劈裂反证审计

覆盖 $29/2^-$ 至 $39/2^-$ 六个自旋态能隙动力学分析：
1. **能隙单调软化与非V字型轨迹**：两带能差 $\\Delta E(I) = E(D6) - E(D5)$ 分别为 $423.1, 357.8, 282.0, 185.1, 118.5, 96.4$ keV，单调下降达 $4.39$ 倍，一阶差分从单步 $96.9$ keV 平稳收敛至 $22.1$ keV。排除了两带孤立偶然交叉的对称V字型急剧回弹模型，符合双阱势垒抬升与渐近量子穿透特征。
2. **全量子PRM有限隧穿对账**：微观近谐 TAC+RPA 因对称性破缺分叉预测声子发散性软化趋零（$\\Delta E \\to 0$）；而全量子 PRM（Qi 2009）考虑有限角动量量子涨落预测 $39/2^-$ 态剩余穿透劈裂 $\\Delta E_{PRM} \\approx 76$ keV。实测最小能隙 $96.4$ keV 与 PRM 预测吻合度达 $79\\%$，实证确立手征在有限核中的非零隧穿本质，否定将 RPA 发散零劈裂当成实验相界的模型外推。代码见 system/scripts/day21_checkpoint132_chiral_phonon_softening_audit.py，基准输出 chiral-phonon-softening-scope-132.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c132_section + theory_marker)

# 5. Update Durable knowledge delta text
old_delta = "131更新knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md的MU07-D21-R131-1及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的M1带内同相/跨带反相交错（r=-0.998）；130更新MU07-D21-R130-1与Qt同态性；129/128/127更新多自旋反演与误差合同。"
new_delta = "132更新knowledge/sources/lv-2019-chirality-135nd-reexamined.md的LV19-D21-R132-1及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的能隙单调软化与PRM有限隧穿对账；131更新M1同相/反相交错；130更新Qt同态性0.9356；129/128/127更新多自旋反演与误差合同。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 6. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/sources/lv-2019-chirality-135nd-reexamined.md":
        item["summary"] = "124纠正过强量词；128完成模型域对比；129完成多自旋反演稳定性；132完成能隙单调软化4.39倍与PRM有限隧穿76.0keV对账，确立非零隧穿本质；保留原review/flags。"
        locators = [s["locator"] for s in item["sources"]]
        if "LV19-D21-R132-1" not in locators:
            item["sources"].append({
                "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
                "locator": "LV19-D21-R132-1"
            })
    elif item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "130核准Qt同态性0.9356与39/2同频失活；131核准带内M1同相与跨带M1反相交错（r=-0.998）；132完成能隙单调软化4.39倍与PRM有限隧穿76.0keV对账；无新CI。"
        locators = [s["locator"] for s in item["sources"]]
        if "LV19-D21-R132-1" not in locators:
            item["sources"].append({
                "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
                "locator": "LV19-D21-R132-1"
            })

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 7. Update Verification and continuation
assert "131实际检查见本run required-checks-131.json" in content
content = content.replace("131实际检查见本run required-checks-131.json", "132实际检查见本run required-checks-132.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 132 via JSON-parsed writeback!")
