#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint147" in content
content = content.replace("research_status: active-in-progress-checkpoint147", "research_status: active-in-progress-checkpoint148")

# 2. Update Candidate pool and selection
old_cand = "147完成单卡学分转移草案与防重防越界审计（锁定只计Day21一次学分，count由20进至21，next由21进至22，禁开Day22）；146预演H3协议；145构建暂存清单；144执行90分钟关口转换；143–127推进各子项。"
new_cand = "148完成终末会话回执草案与全要素收束核定（核定18/24评分、4项开放问题闭环、289项显式暂存与单卡[21]结算准备）；147核定学分转移草案；146预演H3协议；145构建暂存清单；144–127推进各子项。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Add Theory/analysis exercise section for Checkpoint 148
theory_marker = "### Checkpoint147：单卡学分转移草案与防重防越界审计"
c148_section = """### Checkpoint148：终末会话回执草案与全要素收束核定

全面核定 Day 21 终末会话回执（final-session-receipt-21）草案结构与关口元素：
1. **回执全要素闭环核验**：
   - 身份与生命周期：核定当前有效会话 `01a167eb-3c9c-74c0-a0a0-12720a4e1f4d`，启动与截止时间点完全保真；
   - 课程与学分映射：`completed_day_indices: [21]`，`partial_day_indices: []`，`next_day_index: 22`，单卡累计完成数达到 `21`；
   - 评估与缺口状态：口试评分核定 `18/24`（六维度均达 3/4），四大开放问题全部闭环（闭环率 `100.0%`）；
   - 治理与发布规范：全库严格保留 `needs_review: true`，受保护路径零侵入改动，知识写回块 104 项结构严整有效，Git H3 预检通过并绑定 289 个精确暂存文件。
2. **防早结与时间门守则**：在盘正式回执在 15:00 硬截止前保持草案状态，维持运行窗口守护至 15:00 时间门开启。代码见 system/scripts/day21_checkpoint148_final_receipt_template_audit.py，基准输出 final-session-receipt-draft-scope-148.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c148_section + theory_marker)

# 4. Update Durable knowledge delta text
old_delta = "147核定单卡学分转移草案与防重防越界不变量；146完成Git H3协议预演；145构建显式暂存清单；144执行90分钟关口转换；143完成全链路自洽验证；142完成四大开放问题闭环；141更新寿命协方差相消定理；140–133推进各子项。"
new_delta = "148完成终末会话回执草案与全要素收束核定（18/24评分、4项问题闭环、单卡[21]结算准备）；147核定学分转移草案；146预演H3协议；145构建暂存清单；144执行90分钟关口转换；143–133推进各子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 5. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "146完成H3协议预检；147核定单卡学分转移草案；148完成终末会话回执草案与全要素收束核定；无新CI。"

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 6. Update Verification and continuation
assert "147实际检查见本run required-checks-147.json" in content
content = content.replace("147实际检查见本run required-checks-147.json", "148实际检查见本run required-checks-148.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 148 via JSON-parsed writeback!")
