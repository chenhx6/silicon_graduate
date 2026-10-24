#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint146" in content
content = content.replace("research_status: active-in-progress-checkpoint146", "research_status: active-in-progress-checkpoint147")

# 2. Update Candidate pool and selection
old_cand = "146完成Git H3协议五大前置事件预演（分支main、远端gitee、fetch、ancestor、push_dry_run全部通过），确保收束推送零故障；145构建显式暂存清单；144执行90分钟关口转换；143–127推进各子项。"
new_cand = "147完成单卡学分转移草案与防重防越界审计（锁定只计Day21一次学分，count由20进至21，next由21进至22，禁开Day22）；146预演H3协议；145构建暂存清单；144执行90分钟关口转换；143–127推进各子项。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Add Theory/analysis exercise section for Checkpoint 147
theory_marker = "### Checkpoint146：Git H3发布协议前置预演与远端祖先核定"
c147_section = """### Checkpoint147：单卡学分转移草案与防重防越界审计

在 90 分钟收束过渡期完成 Day 21 单卡学分结算与防重防越界不变量核定：
1. **状态转移单步前进**：当前课程基线 `completed_day_count=20`、`next_day_index=21`；15:00 终末计卡时严格执行单步递进至 `completed_day_count=21`、`next_day_index=22`。
2. **防双计与防越界保障**：
   - 严格遵循单一卡片计分原则：本次 run 只给 Day 21 正式学分（`completed_day_indices: [21]`）；
   - 严格禁止提前消费：`partial_day_indices` 保持为空，不给 Day 22 任何学分或预习授分，未打开 Day 23；
   - 防早退锁：在 15:00 硬截止到达前，里程碑状态文件保持 `count=20` 原封不动，严禁提前将草案写入状态库。代码见 system/scripts/day21_checkpoint147_card_credit_template_audit.py，基准输出 card-credit-draft-scope-147.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c147_section + theory_marker)

# 4. Update Durable knowledge delta text
old_delta = "146完成Git H3协议前置预检（fetch/ancestor/dry-run全通）；145构建显式Git暂存清单；144执行90分钟关口转换；143完成全链路自洽验证；142完成四大开放问题闭环；141更新寿命协方差相消定理；140–133推进各子项。"
new_delta = "147核定单卡学分转移草案与防重防越界不变量；146完成Git H3协议预演；145构建显式暂存清单；144执行90分钟关口转换；143完成全链路自洽验证；142完成四大开放问题闭环；141更新寿命协方差相消定理；140–133推进各子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 5. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "145构建显式暂存清单；146完成H3协议预检；147核定单卡学分转移草案与防重防越界不变量；无新CI。"

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 6. Update Verification and continuation
assert "146实际检查见本run required-checks-146.json" in content
content = content.replace("146实际检查见本run required-checks-146.json", "147实际检查见本run required-checks-147.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 147 via JSON-parsed writeback!")
