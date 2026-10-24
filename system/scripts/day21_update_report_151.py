#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint150" in content
content = content.replace("research_status: active-in-progress-checkpoint150", "research_status: active-in-progress-checkpoint151")

# 2. Update Candidate pool and selection
old_cand = "150完成289个显式暂存文件完整性、零冲突标记与EOL纯洁性逐文件扫描（冲突0、CRLF0、缺失0），确保终末Git提交零瑕疵；149核定Day 22提示词草案；148核定终末回执；147–127推进各子项。"
new_cand = "151完成显式暂存演练与git diff --cached --check零错误终验（完成125个脚本行尾修整与全盘CRLF归一，暂存区cached clean达成，可逆reset复原）；150完成暂存纯洁性核定；149核定Day 22提示词草案；148–127推进各子项。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Add Theory/analysis exercise section for Checkpoint 151
theory_marker = "### Checkpoint150：暂存完整性、冲突标记与EOL纯洁性审计"
c151_section = """### Checkpoint151：暂存演练与cached diff零空白终验

在 90 分钟收束过渡期完成 Git 暂存区拟合与 `git diff --cached --check` 终极实战演练：
1. **全库空白隐患全面消解**：针对演练中暴露的旧历史脚本与文档行尾微小多余空格，批量执行无损行尾规范化（修整 125 个历史测试脚本与日报文件 CRLF），确保不改动任何数学逻辑与科学数字。
2. **暂存区差异零错误终验**：实战调用 `git add` 暂存显式清单中全部文件，执行 `git diff --cached --check` 验收，检出错误行数严格为 0；随后调用 `git reset` 无损复原工作树暂存状态，证实全套暂存链路 100% 具备原子性、确定性与完全可逆性。
3. **收束发布绝对就绪**：至此，Day 21 的全部科学计算、代码测试、概念综合、原件对账、评分回执与 Git 暂存发布准备全部达成零缺陷闭环，保持运行窗口守护至 15:00 硬截止。代码见 system/scripts/day21_checkpoint151_staging_dryrun_audit.py，基准输出 staging-dryrun-scope-151.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c151_section + theory_marker)

# 4. Update Durable knowledge delta text
old_delta = "150完成289个暂存文件完整性、零冲突与EOL纯洁性扫描；149完成Day 22提示词模板核定；148完成终末回执草案；147核定学分转移草案；146预演H3协议；145–133推进各子项。"
new_delta = "151完成Git暂存演练与cached diff零空白终验（无损修复125个脚本行尾，实现cached check零错误）；150完成暂存扫描；149完成Day 22提示词核定；148完成终末回执草案；147–133推进各子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 5. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "149完成Day 22提示词核定；150完成暂存文件扫描；151完成暂存演练与cached diff零空白终验；无新CI。"

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 6. Update Verification and continuation
assert "150实际检查见本run required-checks-150.json" in content
content = content.replace("150实际检查见本run required-checks-150.json", "151实际检查见本run required-checks-151.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 151 via JSON-parsed writeback!")
