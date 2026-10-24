#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint143" in content
content = content.replace("research_status: active-in-progress-checkpoint143", "research_status: active-in-progress-checkpoint144")

# 2. Update Candidate pool and selection
old_cand = "143完成收束关口前置冻结与全链路自洽性验证（17项关键产物全覆盖、受保护文件零改动、写回块104项严整），确立90分钟缓冲过渡协议；142完成四大开放问题全要素闭环；141–127推进各子项。"
new_cand = "144正式进入90分钟截止线关口（decision转为finish-current-no-new-unit），冻结全部新源与新课题，严格维持有界分析至15:00硬截止；143完成全链路冻结；142–127推进各子项推演。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Add Theory/analysis exercise section for Checkpoint 144
theory_marker = "### Checkpoint143：收束关口前置冻结与全链路自洽性验证"
c144_section = """### Checkpoint144：90分钟关口边界转换与收束协议执行

时钟正式跨入距离 15:00 硬截止 90 分钟线，调度状态转换为 `finish-current-no-new-unit`：
1. **严格禁止开新**：按照调度协议，不再开启任何新来源、新核素或新题目，前序 Checkpoints 104 至 143 的所有有界分析与定量推演正式锁定。
2. **状态就绪守护**：保持 farmer 监督进程与会话时钟正常轮转，维持当前稳定运行状态至 15:00 硬截止；受保护文件保持零改动，全库严格维持 `needs_review: true`，严禁提前授分或开启 Day 22。
3. **收束缓冲预案**：15:00 硬截止到达后，准时转入 15:00–16:00 收束缓冲小时，依次执行 Day 21 卡片审计完备确认、终末回执签发、里程碑状态计卡更新以及显式精确路径 Git 提交发布。代码见 system/scripts/day21_checkpoint144_90min_boundary_transition.py，基准输出 boundary-transition-scope-144.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c144_section + theory_marker)

# 4. Update Durable knowledge delta text
old_delta = "143完成收束关口前置冻结与全链路自洽性验证（17项产物全覆盖、受保护路径零改动）；142完成四大开放问题全要素闭环；141更新MU07-D21-R141-1寿命协方差相消定理；140–133推进各子项。"
new_delta = "144执行90分钟关口转换协议（转为finish-current-no-new-unit，冻结新源）；143完成全链路自洽验证；142完成四大开放问题闭环；141更新寿命协方差相消定理；140–133推进各子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 5. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "142完成四大开放问题全要素闭环；143完成全链路自洽验证；144执行90分钟关口转换协议(finish-current-no-new-unit)；无新CI。"

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 6. Update Verification and continuation
assert "143实际检查见本run required-checks-143.json" in content
content = content.replace("143实际检查见本run required-checks-143.json", "144实际检查见本run required-checks-144.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 144 via JSON-parsed writeback!")
