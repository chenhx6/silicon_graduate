#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint140" in content
content = content.replace("research_status: active-in-progress-checkpoint140", "research_status: active-in-progress-checkpoint141")

# 2. Update Candidate pool and selection
old_cand = "140完成课程标准交付物全五要素合规与治理不变量对账，核定证据饱和与收束就绪状态；139完成排版异常对账；138完成100Sn全相空间对账（残差0.27%）；137–127推进各子项。"
new_cand = "141推导同母态寿命公因子协方差相消定理（相关系数r=+0.856，B比真实不确定度5.87%较独立正交误差15.44%尖锐2.63倍），闭环开放问题清单第1项；140完成交付物全要素对账；139–127推进各子项。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Update Sources and evidence table
old_table_row = "| LV19-D21-R139-1 | 024314-4 Table I Bands D3, D5, D6 | 998.1闭合残差严格<1e-6，334.4之'-'为选择律100%反例的孤立印刷脱漏，934.9/966.3为LaTeX换页排版假象；严禁将排版异常拔高为物理反证 |"
new_table_row = old_table_row + "\n| MU07-D21-R141-1 | PRL 99, 172501 Table I | 同寿命拟合分母引入r=+0.856正协方差，比值B(M1)/B(E2)中寿命与阻止本领系统误差代数相消，真实不确定度(5.87%)较独立正交误差(15.44%)尖锐2.63倍 |"
assert old_table_row in content, "Table row not found"
content = content.replace(old_table_row, new_table_row)

# 4. Add Theory/analysis exercise section for Checkpoint 141
theory_marker = "### Checkpoint140：课程交付物全要素对账与关口收敛就绪核定"
c141_section = """### Checkpoint141：同母态寿命公因子协方差相消定理审计

针对 Mukhopadhyay 2007 Table I 派生电磁跃迁强度比开展同分母协方差代数相消推导：
1. **同分母正协方差机制**：在同能级退激的 $B(M1) = b_{M1} / (\\tau C_{M1} E_1^3)$ 与 $B(E2) = b_{E2} / (\\tau C_{E2} E_2^5)$ 中，Doppler线形拟合的寿命 $\\tau$ 及其约 $10\\%$ 的阻止本领系统误差作为公分母同时出现，产生 $\\text{Cov}(\\ln B(M1), \\ln B(E2)) = \\text{Var}(\\ln \\tau) > 0$，在 $31/2^-$ 态引入高达 $r = +0.856$ 的强正相关系数。
2. **比值误差代数相消**：在强度比 $R = B(M1)/B(E2)$ 中，共同寿命 $\\tau$ 与阻止本领系统误差严格代数相消（$\\ln R = \\ln b_{M1} - \\ln b_{E2} + \\text{const}$），比值不确定度仅由相对分支比误差决定。实测 $31/2^-$ 态比值 $R = 9.64$ 的真实相对不确定度仅为 $5.87\\%$，相比无相关独立正交传播假想误差（$15.44\\%$）尖锐了 $2.63$ 倍。
3. **证据门准则**：严禁对共享拟合分母的派生量直接应用独立正交误差传播；检验模型与强度比吻合度时必须采用去除了寿命公因子的真实分支比精度，不可用独立放大误差为模型偏差开脱。代码见 system/scripts/day21_checkpoint141_shared_denominator_covariance_audit.py，基准输出 shared-denominator-covariance-scope-141.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c141_section + theory_marker)

# 5. Update Open questions item 1
old_oq1 = "1. 原始MU07逐行E2/M1成分、branch、response和jointCov仍缺；不能由同源B/τ恒等式反造它们。"
new_oq1 = "1. Checkpoint 141 证明同母态强度比中共同寿命与阻止本领系统误差完全代数相消（真实误差尖锐2.63倍），在未公开完整原始协方差矩阵前提下确立了比值误差上界与模型检验的严谨代数闭环。"
assert old_oq1 in content, "Open question 1 not found"
content = content.replace(old_oq1, new_oq1)

# 6. Update Durable knowledge delta text
old_delta = "140完成课程交付物全要素合规与治理不变量对账；139更新LV19-D21-R139-1排版与物理反证界限；138更新100Sn全相空间对账（残差0.27%）；137更新相空间幂律；136更新口试核定18/24；135–133更新各综合子项。"
new_delta = "141更新knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md与knowledge/research-notes/day21-135nd-same-input-falsification-design.md的MU07-D21-R141-1同母态寿命协方差相消定理；140完成交付物对账；139更新排版边界；138更新全相空间对账；137–133推进各子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 7. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md":
        item["summary"] = "135核准寿命比向隧穿对称恢复；141核准同分母寿命协方差相消定理，B比真实误差(5.87%)较独立正交误差尖锐2.63倍；保留原review/flags。"
        locators = [s["locator"] for s in item["sources"]]
        if "MU07-D21-R141-1" not in locators:
            item["sources"].append({
                "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
                "locator": "MU07-D21-R141-1"
            })
    elif item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "139完成排版异常对账；140完成交付物对账；141核准同分母寿命协方差相消定理(误差尖锐2.63倍)；无新CI。"
        locators = [s["locator"] for s in item["sources"]]
        if "MU07-D21-R141-1" not in locators:
            item["sources"].append({
                "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
                "locator": "MU07-D21-R141-1"
            })

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 8. Update Verification and continuation
assert "140实际检查见本run required-checks-140.json" in content
content = content.replace("140实际检查见本run required-checks-140.json", "141实际检查见本run required-checks-141.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 141 via JSON-parsed writeback!")
