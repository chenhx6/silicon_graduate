#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint138" in content
content = content.replace("research_status: active-in-progress-checkpoint138", "research_status: active-in-progress-checkpoint139")

# 2. Update Candidate pool and selection
old_cand = "138完成100Sn全相空间（结合EC分额能隙阻尼与beta+）ft精确对账，Hinke标度后强度为5.274，与Lubos实测5.26残差仅0.27%（解释率99.62%），彻底解决强度冲突；137推进正电子相空间；136完成口试18/24；135–127推进各子项。"
new_cand = "139完成Lv 2019 Table I三项局部异常（998.1 vs 997keV、334.4keV宇称元组、934.9/966.3keV重复母态）排版印刷与物理反证边界对账，确立印刷脱漏不得等同于物理证伪的证据门；138完成100Sn全相空间对账（残差0.27%）；137–127推进各子项。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Update Sources and evidence table
old_table_row = "| HK10-D21-R138-1 | Nature 465, 997; PRC 94, 054322 | 纳入EC分额(13.3%降至9.49%)阻尼后全相空间比为1.71064；Hinke强度标度后为5.274与Lubos实测5.26残差仅0.27%(解释率99.62%)，真实弱矩阵元完全相容 |"
new_table_row = old_table_row + "\n| LV19-D21-R139-1 | 024314-4 Table I Bands D3, D5, D6 | 998.1闭合残差严格<1e-6，334.4之'-'为选择律100%反例的孤立印刷脱漏，934.9/966.3为LaTeX换页排版假象；严禁将排版异常拔高为物理反证 |"
assert old_table_row in content, "Table row not found"
content = content.replace(old_table_row, new_table_row)

# 4. Add Theory/analysis exercise section for Checkpoint 139
theory_marker = "### Checkpoint138：电子俘获分额与全相空间ft精确对账（残差消除至0.27%）"
c139_section = """### Checkpoint139：排版印刷异常与物理证伪边界审计

系统对账 Lv 2019 Table I 三项文献印刷与排版异常：
1. **998.1 vs 997 keV 质心微小漂移**：$998.1$ keV 与其打印母态（$5412.6$ keV）及终态（$4414.5$ keV）闭合残差严格 $< 10^{-6}$；与正文标示的 $997$ keV 的 $1.0$ keV 差属于多维符合谱不同门峰质心的拟合残差，属于统计/系统精度范畴，不构成核态物理冲突。
2. **334.4 keV 宇称元组选择律排他判定**：表格打印 $27/2^- \\to 25/2^+$ 并标 $M1/E2$， $100\\%$ 违反电磁宇称选择律（$M1/E2$ 严格要求 $\\Delta \\pi = 0$）；正文（PDF p.2）、Fig. 1 以及 4 条跨带线偏振测量一致确证 Band D3 为正宇称，排他性证明该 '-' 系印刷脱漏字符（应为 $27/2^+$）。
3. **934.9/966.3 keV 分栏排版延续归属**：两行母态能量（$5787.6$ 与 $6281.5$ keV）与 Band D5 能级完全重合，系多栏排版跨页续表造成的编排假象，属 Band D5 带内 $\\Delta I = 2$ 跃迁。
4. **方法学证据门准则**：严禁在知识库中静默篡改原始出版物文字；严禁将排版异常拔高为推翻动力学对称性的实验反证；物理证伪必须依赖明确物理观测量（如 Checkpoint 134 建立的偏振 $P > 0$ 判决）。代码见 system/scripts/day21_checkpoint139_typographical_anomaly_audit.py，基准输出 typographical-anomaly-scope-139.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c139_section + theory_marker)

# 5. Update Open questions item 2
old_oq2 = "2. VoR已得，缺口已收窄到998.1/997、334.4及重复母态的原校准/作者更正；不再沿用“VoR未取得”。"
new_oq2 = "2. Checkpoint 139 已完成 998.1/997、334.4 及续表排版异常的闭环审计（分别对应门质心拟合残差、印刷字符脱漏与分栏假象），确立印刷脱漏不得替代物理反证，缺口正式闭环。"
assert old_oq2 in content, "Open question 2 not found"
content = content.replace(old_oq2, new_oq2)

# 6. Update Durable knowledge delta text
old_delta = "138更新knowledge/projects/100sn-gamow-teller-independent-evidence.md与knowledge/sources/hinke-2010-100sn-decay-spectroscopy.md的HK10-D21-R138-1全相空间ft精确对账（残差消除至0.27%）；137更新正电子相空间；136更新口试核定18/24；135更新寿命向隧穿对称恢复；134更新偏振排他设计；133更新推断阶梯综合矩阵。"
new_delta = "139更新knowledge/sources/lv-2019-chirality-135nd-reexamined.md与knowledge/research-notes/day21-135nd-same-input-falsification-design.md的LV19-D21-R139-1排版印刷与物理反证边界审计；138更新100Sn全相空间对账（残差0.27%）；137更新相空间幂律；136更新口试核定18/24；135–133更新各综合子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 7. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/sources/lv-2019-chirality-135nd-reexamined.md":
        item["summary"] = "134完成偏振排他反证设计；139完成998/997、334.4印刷异常与排版归属对账，确立印刷脱漏不得等同于物理反证；保留原review/flags。"
        locators = [s["locator"] for s in item["sources"]]
        if "LV19-D21-R139-1" not in locators:
            item["sources"].append({
                "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
                "locator": "LV19-D21-R139-1"
            })
    elif item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "135核准寿命向隧穿对称恢复；136完成口试评分18/24；139完成排版印刷异常与物理反证界限对账；无新CI。"
        locators = [s["locator"] for s in item["sources"]]
        if "LV19-D21-R139-1" not in locators:
            item["sources"].append({
                "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
                "locator": "LV19-D21-R139-1"
            })

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 8. Update Verification and continuation
assert "138实际检查见本run required-checks-138.json" in content
content = content.replace("138实际检查见本run required-checks-138.json", "139实际检查见本run required-checks-139.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 139 via JSON-parsed writeback!")
