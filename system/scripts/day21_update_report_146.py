#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint145" in content
content = content.replace("research_status: active-in-progress-checkpoint145", "research_status: active-in-progress-checkpoint146")

# 2. Update Candidate pool and selection
old_cand = "145完成显式路径暂存清单构建与排除项审计（精确暂存289项，排除Day20继承dirty与受保护文件），确立H3合规发布边界；144执行90分钟关口转换；143–127推进各子项。"
new_cand = "146完成Git H3协议五大前置事件预演（分支main、远端gitee、fetch、ancestor、push_dry_run全部通过），确保收束推送零故障；145构建显式暂存清单；144执行90分钟关口转换；143–127推进各子项。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Add Theory/analysis exercise section for Checkpoint 146
theory_marker = "### Checkpoint145：显式路径暂存清单与排除项审计"
c146_section = """### Checkpoint146：Git H3发布协议前置预演与远端祖先核定

在 90 分钟收束过渡期完成 Git H3 发布协议的前置全流程验证：
1. **五大核心事件预检全过**：
   - `git branch --show-current`：确认为当前工作分支 `main`；
   - `git remote -v`：确认为合法容器恢复远端 Gitee；
   - `git fetch origin main`：成功获取远端最新引用；
   - `git merge-base --is-ancestor origin/main HEAD`：exit 0，证实本地 HEAD 严格包含远端 main 历史（满足前向线性延伸，无分叉冲突）；
   - `git push --dry-run origin HEAD:main`：exit 0，预演演练返回 Everything up-to-date，网络通道与凭据认证畅通。
2. **非 force 推送保障**：在 15:00 终末收束执行时，将严格采用精确无 force 的 `git push origin HEAD:main` 方式推送显式清单中的 289 个文件，杜绝历史重写与意外覆盖。代码见 system/scripts/day21_checkpoint146_h3_preflight_protocol_audit.py，基准输出 h3-preflight-scope-146.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c146_section + theory_marker)

# 4. Update Durable knowledge delta text
old_delta = "145构建显式Git暂存清单并审计继承dirty排除项；144执行90分钟关口转换；143完成全链路自洽验证；142完成四大开放问题闭环；141更新寿命协方差相消定理；140–133推进各子项。"
new_delta = "146完成Git H3协议前置预检（fetch/ancestor/dry-run全通）；145构建显式Git暂存清单；144执行90分钟关口转换；143完成全链路自洽验证；142完成四大开放问题闭环；141更新寿命协方差相消定理；140–133推进各子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 5. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "144执行90分钟关口转换；145构建显式暂存清单；146完成Git H3协议五大事件前置预检；无新CI。"

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 6. Update Verification and continuation
assert "145实际检查见本run required-checks-145.json" in content
content = content.replace("145实际检查见本run required-checks-145.json", "146实际检查见本run required-checks-146.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 146 via JSON-parsed writeback!")
