#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint144" in content
content = content.replace("research_status: active-in-progress-checkpoint144", "research_status: active-in-progress-checkpoint145")

# 2. Update Candidate pool and selection
old_cand = "144正式进入90分钟截止线关口（decision转为finish-current-no-new-unit），冻结全部新源与新课题，严格维持有界分析至15:00硬截止；143完成全链路冻结；142–127推进各子项推演。"
new_cand = "145完成显式路径暂存清单构建与排除项审计（精确暂存289项，排除Day20继承dirty与受保护文件），确立H3合规发布边界；144执行90分钟关口转换；143–127推进各子项。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Add Theory/analysis exercise section for Checkpoint 145
theory_marker = "### Checkpoint144：90分钟关口边界转换与收束协议执行"
c145_section = """### Checkpoint145：显式路径暂存清单与排除项审计

在 90 分钟收束过渡期建立严格合规的显式 Git 暂存与排除清单：
1. **显式暂存范围（289项）**：精确覆盖本轮研究生成的全部 `knowledge/` 变更、`outputs/learning-daily/` 日报与运行成果、`system/handoff.md`、`system/log.md` 以及 `system/scripts/day21_*.py` 独立验证脚本。
2. **严禁带入项（严格排除）**：
   - 继承自 Day 20 的未跟踪文件（`20261022-DAY20-be2-qt-deformation-systematics-run-01/` 与 `run-02/run.json`）严格排除在暂存清单外；
   - 治理受保护文件（`PLAN.md`、`raw/zotero/wiki-inbox.bib`）零侵入改动；
   - 临时目录 `tmp/` 及运行时日志（`stderr.log`）全部排除。
3. **发布门准则守护**：严禁使用 `git add .` 或 `git add -A`；暂存前执行 `git diff --check`，暂存后执行 `git diff --cached --check`；推送时使用精确无 force 的 `git push origin HEAD:main`，确保远端历史线性和祖先关系完全自洽。代码见 system/scripts/day21_checkpoint145_publication_manifest_audit.py，基准输出 publication-manifest-scope-145.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c145_section + theory_marker)

# 4. Update Durable knowledge delta text
old_delta = "144执行90分钟关口转换协议（转为finish-current-no-new-unit，冻结新源）；143完成全链路自洽验证；142完成四大开放问题闭环；141更新寿命协方差相消定理；140–133推进各子项。"
new_delta = "145构建显式Git暂存清单并审计继承dirty排除项；144执行90分钟关口转换；143完成全链路自洽验证；142完成四大开放问题闭环；141更新寿命协方差相消定理；140–133推进各子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 5. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "143完成全链路自洽验证；144执行90分钟关口转换；145构建显式Git暂存清单与排除项审计；无新CI。"

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 6. Update Verification and continuation
assert "144实际检查见本run required-checks-144.json" in content
content = content.replace("144实际检查见本run required-checks-144.json", "145实际检查见本run required-checks-145.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 145 via JSON-parsed writeback!")
