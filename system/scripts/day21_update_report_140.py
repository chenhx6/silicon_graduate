#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint139" in content
content = content.replace("research_status: active-in-progress-checkpoint139", "research_status: active-in-progress-checkpoint140")

# 2. Update Candidate pool and selection
old_cand = "139完成Lv 2019 Table I三项局部异常（998.1 vs 997keV、334.4keV宇称元组、934.9/966.3keV重复母态）排版印刷与物理反证边界对账，确立印刷脱漏不得等同于物理证伪的证据门；138完成100Sn全相空间对账（残差0.27%）；137–127推进各子项。"
new_cand = "140完成课程标准交付物全五要素合规与治理不变量对账，核定证据饱和与收束就绪状态；139完成排版异常对账；138完成100Sn全相空间对账（残差0.27%）；137–127推进各子项。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Add Theory/analysis exercise section for Checkpoint 140
theory_marker = "### Checkpoint139：排版印刷异常与物理证伪边界审计"
c140_section = """### Checkpoint140：课程交付物全要素对账与关口收敛就绪核定

全面对账 Day 21 课程标准五大交付物与治理不变量：
1. **五大交付物完备性核定**：回忆（7层推断阶梯与冻结回忆）、主线（135Nd VoR与MU07逐claim原件对账、100Sn GSI与RIKEN相空间对账）、练习（自拟未知摘要证据门“可以说/不能说/下一步测什么”）、反证（Checkpoint 134 康普顿线偏振排他反证，16.3h达3σ）、交付（口试评分表核定18/24、claim-level审计与第三周REFLECT深度总结），全部五项要素均已完整闭环。
2. **治理不变量严格守护**：全库保留 needs_review: true，严禁将自审升格为 human-reviewed；受保护路径（PLAN.md、raw/zotero/wiki-inbox.bib）零改动；前一日及历史 run.json 保持完整；知识写回块 104 项结构严整有效；未提前授分、未开启 Day 22。
3. **收束关口准备**：当前研究窗口已达到高信息饱和与全要素完备，运行状态保持开放直至 15:00 硬截止；15:00 准时转入收束缓冲小时，执行终末计卡、回执生成与显式路径推送。代码见 system/scripts/day21_checkpoint140_curriculum_deliverable_audit.py，基准输出 curriculum-deliverable-scope-140.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c140_section + theory_marker)

# 4. Update Durable knowledge delta text
old_delta = "139更新knowledge/sources/lv-2019-chirality-135nd-reexamined.md与knowledge/research-notes/day21-135nd-same-input-falsification-design.md的LV19-D21-R139-1排版印刷与物理反证边界审计；138更新100Sn全相空间对账（残差0.27%）；137更新相空间幂律；136更新口试核定18/24；135–133更新各综合子项。"
new_delta = "140完成课程交付物全要素合规与治理不变量对账；139更新LV19-D21-R139-1排版与物理反证界限；138更新100Sn全相空间对账（残差0.27%）；137更新相空间幂律；136更新口试核定18/24；135–133更新各综合子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 5. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "136完成口试评分18/24；139完成排版异常对账；140完成课程交付物全要素对账与收束就绪核定；无新CI。"

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 6. Update Verification and continuation
assert "139实际检查见本run required-checks-139.json" in content
content = content.replace("139实际检查见本run required-checks-139.json", "140实际检查见本run required-checks-140.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 140 via JSON-parsed writeback!")
