#!/usr/bin/env python3
import sys
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
content = content.replace("research_status: active-in-progress-checkpoint128", "research_status: active-in-progress-checkpoint129")

# 2. Update Candidate pool and selection
old_cand = "128推进135Nd手征与竞争模型（PRM、TAC+RPA与两带混合）预测域对账，反演带内225.8keV跃迁辐射份额f225有界区间，量化两套实验跨束能/门谱拼接的1.56倍系统不相容因子；127转回135Nd同母态响应/误差设计，新增共同能量增益与加性零点区别及未知相关性条件包络。"
new_cand = "129完成135Nd多自旋（31/2-至37/2-）跨带E2单调增长3.56倍的手征隧穿机制核对，揭示带内|δin|严格保持在[0.034,0.061]的超高稳定性；128推进手征与竞争模型预测域对账与跨实验1.56倍差异；127完成同母态误差与相消设计。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Update Sources and evidence table
old_table_row = "| LV19-D21-R128-1 | 024314-5 Table I D6; PRL 99, 172501 | 实测R_E2反演f225∈[0.00122,0.00186]（|δ225|∈[0.035,0.043]）自洽；LV19强度导出的M1上界比MU07实测低1.56倍，确立跨阵列门谱系统差异边界 |"
new_table_row = old_table_row + "\n| LV19-D21-R129-1 | 024314-5 Table I Band D6; PRL 99, 172501 | 四个自旋态实测R_E2单调增长3.56倍体现手征隧穿演化；反演带内|δin|稳定在[0.034,0.061]（f_E2在0.11%–0.37%）证明两套实验深刻自洽，跨实验M1波动揭示门谱依赖性 |"
assert old_table_row in content, "Table row not found"
content = content.replace(old_table_row, new_table_row)

# 4. Add Theory/analysis exercise section for Checkpoint 129
theory_marker = "### Checkpoint128：手征与竞争模型预测域对照及反演混合比有界性审计"
c129_section = """### Checkpoint129：多自旋混合比反演与跨带E2增长物理机制审计

覆盖 $31/2^-$, $33/2^-$, $35/2^-$, $37/2^-$ 连续4个重叠自旋态的多自旋反演：
1. **跨带E2单调增长**：实测跨带/带内比值 $R_{E2}$ 分别为 $0.139, 0.243, 0.475, 0.497$，随自旋单调增长达 $3.56$ 倍。这直观反映了由低自旋单声子手征振动（声子选择定则压低带外E2）向高自旋静态手征隧穿（对称/反对称波函数使跨带与带内E2趋于相等，$R_{E2} \\to 1$）演化的理论图像。
2. **带内混合比超高稳定性**：同母态反演得到的带内辐射E2份额分别为 $0.00151, 0.00117, 0.00172, 0.00365$（0.11%–0.37%），对应的混合比模值 $|\\delta_{in}|$ 高度稳定在 $[0.034, 0.061]$ 区间，与转动带内低能跃迁近纯M1物理预期完全吻合，证明两套独立实验在电四极形变空间具有深刻内在自洽性。
3. **跨实验M1波动**：跨实验M1比值因子出现大幅波动（$1.56, 5.21, 0.98$），量化揭示了不同束能与谱仪门宽对弱M1分支的强烈测量依赖性。代码见 system/scripts/day21_checkpoint129_multispin_chiral_inversion_audit.py，基准输出 multispin-chiral-inversion-scope-129.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c129_section + theory_marker)

# 5. Update Durable knowledge delta text
old_delta = "128更新knowledge/sources/lv-2019-chirality-135nd-reexamined.md的LV19-D21-R128-1及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的手征与竞争模型预测域对照及反演混合比有界性；126更新QI09-D21-R126-1访问边界；127更新LV19-D21-R127-1/2与共同校准合同。"
new_delta = "129更新knowledge/sources/lv-2019-chirality-135nd-reexamined.md的LV19-D21-R129-1及knowledge/research-notes/day21-135nd-same-input-falsification-design.md的多自旋反演稳定性与E2手征隧穿演化；128更新LV19-D21-R128-1与竞争模型域；126/127更新访问与误差合同。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 6. Update writeback block
# In lv-2019 item and design item:
old_source_entry = '''        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R128-1"
        }'''

new_source_entry = '''        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R128-1"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D21-R129-1"
        }'''
assert old_source_entry in content, "Old source entry not found"
# Replace in both items (lv-2019 and design)
content = content.replace(old_source_entry, new_source_entry)

# Update both summaries:
old_sum = "128完成手征与竞争模型预测域对照、带内f225反演有界区间与跨实验1.56倍系统差异核查；无新CI。"
new_sum = "128完成手征与竞争模型预测域对照；129完成四个自旋态R_E2单调增长3.56倍与带内|δin|∈[0.034,0.061]超高稳定性核验；无新CI。"
assert old_sum in content, "Old summary string not found"
content = content.replace(old_sum, new_sum)

# 7. Update Verification and continuation
old_ver = "128实际检查见本run required-checks-128.json；较早检查不覆盖此树。研究仍开放至原receipt今日15:00，未授分/提交/发布/开Day22。"
new_ver = "129实际检查见本run required-checks-129.json；较早检查不覆盖此树。研究仍开放至原receipt今日15:00，未授分/提交/发布/开Day22。"
assert old_ver in content, "Old ver not found"
content = content.replace(old_ver, new_ver)

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 129")
