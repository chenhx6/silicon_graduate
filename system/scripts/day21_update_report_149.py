#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint148" in content
content = content.replace("research_status: active-in-progress-checkpoint148", "research_status: active-in-progress-checkpoint149")

# 2. Update Candidate pool and selection
old_cand = "148完成终末会话回执草案与全要素收束核定（核定18/24评分、4项开放问题闭环、289项显式暂存与单卡[21]结算准备）；147核定学分转移草案；146预演H3协议；145构建暂存清单；144–127推进各子项。"
new_cand = "149完成Day 22准备入口提示词模板核定（继承18/24评分与四大闭环，预设wobbling几何、声子与极化大纲，暂存草案待15:00落地）；148核定终末回执草案；147核定学分转移草案；146–127推进各子项。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Add Theory/analysis exercise section for Checkpoint 149
theory_marker = "### Checkpoint148：终末会话回执草案与全要素收束核定"
c149_section = """### Checkpoint149：Day 22准备入口模板核验与收束闭环就绪

全面核验下一正式卡（Day 22 wobbling几何、声子与观测量）准备提示词模板，并预存草案：
1. **要素完整继承**：
   - 继承 Day 21 周考核定口试评分 `18/24`（六维度均稳达 3/4）与全库 `needs_review: true` 治理底线；
   - 继承四大开放问题闭环成果（同分母寿命协方差相消、出版物排版异常界限、100Sn全相空间对账、225.8keV偏振反证设计）；
   - 紧扣课程 matrix Day 22 交付要求：区分横向/纵向 wobbling 声子、阅读 Frauendorf 2014 与 Hamamoto 2003、以 135Pr/135Nd 反例检验“近简并+强E2”非充分性。
2. **防早启与关口协议**：该提示词模板作为草案暂存于 `next-day-prompt-draft-scope-149.json`，在盘正文提示词文件在 15:00 硬截止到达前严禁提前创建，严格恪守“本文件不启动Day22、Day22/23禁开”的边界约定。代码见 system/scripts/day21_checkpoint149_next_prompt_template_audit.py，基准输出 next-day-prompt-draft-scope-149.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c149_section + theory_marker)

# 4. Update Durable knowledge delta text
old_delta = "148完成终末会话回执草案与全要素收束核定（18/24评分、4项问题闭环、单卡[21]结算准备）；147核定学分转移草案；146预演H3协议；145构建暂存清单；144执行90分钟关口转换；143–133推进各子项。"
new_delta = "149完成Day 22准备入口提示词模板核定与收束闭环就绪；148完成终末回执草案；147核定学分转移草案；146预演H3协议；145构建暂存清单；144执行90分钟关口转换；143–133推进各子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 5. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "147核定单卡学分转移草案；148完成终末回执草案；149完成Day 22准备入口提示词模板核定；无新CI。"

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 6. Update Verification and continuation
assert "148实际检查见本run required-checks-148.json" in content
content = content.replace("148实际检查见本run required-checks-148.json", "149实际检查见本run required-checks-149.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 149 via JSON-parsed writeback!")
