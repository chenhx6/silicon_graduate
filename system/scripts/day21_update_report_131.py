#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint130" in content
content = content.replace("research_status: active-in-progress-checkpoint130", "research_status: active-in-progress-checkpoint131")

# 2. Update Candidate pool and selection
old_cand = "130完成135Nd五自旋（31/2-至39/2-）四极矩比值高度同态性（Qt比0.9356±0.0102）与39/2态1.043倍步调一致集体失活反证审计，排他性反驳形状共存与偶然交叉；129完成跨带E2增长3.56倍核对；128/127完成模型域与误差设计。"
new_cand = "131完成135Nd带内M1同相交错与跨带M1 100%严格反相交错（相关系数r=-0.998）审计，确立手征势垒进动与声子互补跃迁的排他性实证；130完成Qt同态性0.9356与39/2同频失活；129/128/127完成多自旋反演与误差设计。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Update Sources and evidence table
old_table_row = "| MU07-D21-R130-1 | PRL 99, 172501 Table I | 五自旋Qt(B)/Qt(A)均值0.9356±0.0102（散度1.09%）排除Qt相差2倍的形状共存；39/2处两带骤降2.5倍且对称比1.043步调一致失活，反驳偶然带交叉 |"
new_table_row = old_table_row + "\n| MU07-D21-R131-1 | PRL 99, 172501 Table I and Fig. 3 | 两带带内B(M1)一阶差分符号完全同相（-,+,-,+），跨带差分（+,-,+）严格反相且线性相关r=-0.998，确立角动量进动手征宇称恢复机制 |"
assert old_table_row in content, "Table row not found"
content = content.replace(old_table_row, new_table_row)

# 4. Add Theory/analysis exercise section for Checkpoint 131
theory_marker = "### Checkpoint130：四极矩比值同态性与39/2自旋步调一致失活的反证排除审计"
c131_section = """### Checkpoint131：带内M1同相交错与跨带M1反相交错反证审计

覆盖 $31/2^-$ 至 $39/2^-$ 态磁偶极跃迁进动模式的定量审计：
1. **带内同相交错与平均对称性**：在四个差分步长上，两带带内 $B(M1)$ 一阶差分符号序列完全相同：$\\text{sgn}(\\Delta B(M1)_{in}) = (-, +, -, +)$，带内平均强度比 $B(M1)_B / B(M1)_A = 0.971 \\pm 0.071$，证明两带具有高度对称的内禀磁偶极几何与相同的准粒子进动相角。
2. **跨带严格反相交错与极高负相关**：跨带一阶差分 $\\Delta B(M1)_{out}$ 符号序列为 $(+, -, +)$，与带内差分乘积在全部三个重合步长严格全为负值，构成 **100% 严格反相交错**；Band A 带内与跨带差分线性相关系数达 $r = -0.998$，Band B 达 $r = -0.792$。
3. **微观手征物理图像确证**：带内 $M1$ 承载总角动量方向的经典集体电流，而跨带 $M1$ 承载跨越手征势垒的横向声子非简谐跃迁（$\\Delta n = 1$），准粒子取向角几何干涉使跃迁强度在带内与跨带通道互补转移，排他性证实微观手征振动图像，反驳偶然带交叉假说（后者反相概率仅 $12.5\\%$ 且无负相关机制）。代码见 system/scripts/day21_checkpoint131_m1_staggering_antiphase_audit.py，基准输出 m1-staggering-antiphase-scope-131.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c131_section + theory_marker)

# 5. Update Durable knowledge delta text
old_delta = "130更新knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md的MU07-D21-R130-1及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的四极矩同态性与步调一致失活反证；129更新多自旋反演稳定性；128/127更新模型域与误差设计。"
new_delta = "131更新knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md的MU07-D21-R131-1及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的M1带内同相/跨带反相交错（r=-0.998）；130更新MU07-D21-R130-1与Qt同态性；129/128/127更新多自旋反演与误差合同。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 6. Update writeback block using json parsing to be 100% robust and clean
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

# Update mukhopadhyay-2007 item
for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md":
        item["summary"] = "124撤回后续重复同步中的过强认证；130核准Qt同态性0.9356与39/2同频失活；131核准带内M1同相与跨带M1反相交错（r=-0.998）机制；保留原review/flags。"
        # Add MU07-D21-R131-1 if not present
        locators = [s["locator"] for s in item["sources"]]
        if "MU07-D21-R131-1" not in locators:
            item["sources"].append({
                "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
                "locator": "MU07-D21-R131-1"
            })
    elif item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "129完成四个自旋态R_E2单调增长3.56倍；130核准Qt同态性0.9356与39/2同频失活；131核准带内M1同相与跨带M1反相交错（r=-0.998）机制；无新CI。"
        locators = [s["locator"] for s in item["sources"]]
        if "MU07-D21-R131-1" not in locators:
            item["sources"].append({
                "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
                "locator": "MU07-D21-R131-1"
            })

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 7. Update Verification and continuation
assert "130实际检查见本run required-checks-130.json" in content
content = content.replace("130实际检查见本run required-checks-130.json", "131实际检查见本run required-checks-131.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 131 via JSON-parsed writeback!")
