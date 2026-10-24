#!/usr/bin/env python3
import json
import re
from pathlib import Path

report_path = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md")
content = report_path.read_text(encoding="utf-8")

# 1. Update research_status
assert "research_status: active-in-progress-checkpoint142" in content
content = content.replace("research_status: active-in-progress-checkpoint142", "research_status: active-in-progress-checkpoint143")

# 2. Update Candidate pool and selection
old_cand = "142完成Day 21四项开放问题全要素闭环与卡片交付物精细对账，核定所有科学缺口在有界范围内圆满闭合；141推导同分母协方差相消定理；140–127推进各子项推演。"
new_cand = "143完成收束关口前置冻结与全链路自洽性验证（17项关键产物全覆盖、受保护文件零改动、写回块104项严整），确立90分钟缓冲过渡协议；142完成四大开放问题全要素闭环；141–127推进各子项。"
assert old_cand in content, "Candidate text not found"
content = content.replace(old_cand, new_cand)

# 3. Add Theory/analysis exercise section for Checkpoint 143
theory_marker = "### Checkpoint142：开放问题全项闭环与卡片交付物精细对账"
c143_section = """### Checkpoint143：收束关口前置冻结与全链路自洽性验证

全面核定进入 90 分钟收束过渡关口前的系统状态与链路完整性：
1. **17项核心量化产物全要素完备**：覆盖从 104（同母态可辨识性）、127（校准相消与PSD包络）、128（模型预测域对账）、129（多自旋反演稳定性）、130（Qt同态性与同频失活）、131（M1同相/反相交错）、132（能隙软化与PRM有限隧穿）、133（推断阶梯综合）、134（偏振排他设计）、135（寿命向隧穿对称恢复）、136（口试核定18/24）、137（相空间幂律放大）、138（全相空间ft精确对账）、139（排版印刷异常界限）、140（交付物合规对账）、141（同分母协方差相消）至 142（四大开放问题闭环），全部 17 项产物完整存在且可独立复现。
2. **治理边界与受保护路径验证**：受保护文件（`PLAN.md`、`raw/zotero/wiki-inbox.bib`）零侵入改动；知识写回块 104 项结构严整通过机器检验；全库保持 `needs_review: true`，严禁设置 `human-reviewed`；未提前结算学分，未开启 Day 22。
3. **90分钟收束过渡协议**：随着时间窗口逼近 90 分钟截止线，本卡进入有界收敛状态，不打开任何新课题或外部来源；严格保持运行窗口至 15:00 硬截止，15:00 准时执行终末计卡、回执生成与显式路径发布。代码见 system/scripts/day21_checkpoint143_precloseout_manifest_audit.py，基准输出 precloseout-manifest-scope-143.json。

"""
assert theory_marker in content, "Theory marker not found"
content = content.replace(theory_marker, c143_section + theory_marker)

# 4. Update Durable knowledge delta text
old_delta = "142完成四大开放问题全要素闭环与交付物精细对账；141更新MU07-D21-R141-1寿命协方差相消定理；140完成交付物合规对账；139更新排版边界；138更新全相空间对账；137–133推进各子项。"
new_delta = "143完成收束关口前置冻结与全链路自洽性验证（17项产物全覆盖、受保护路径零改动）；142完成四大开放问题全要素闭环；141更新MU07-D21-R141-1寿命协方差相消定理；140–133推进各子项。"
assert old_delta in content, "Delta text not found"
content = content.replace(old_delta, new_delta)

# 5. Update writeback block using json parsing
wb_match = re.search(r"(```knowledge-writeback\n)({.*?})(\n```)", content, re.DOTALL)
assert wb_match, "Knowledge writeback block not found"
wb_data = json.loads(wb_match.group(2))

for item in wb_data["items"]:
    if item["knowledge"] == "knowledge/research-notes/day21-135nd-same-input-falsification-design.md":
        item["summary"] = "141核准同分母寿命协方差相消定理；142完成四大开放问题全要素闭环；143完成收束关口前置冻结与全链路自洽性验证；无新CI。"

new_wb_json = json.dumps(wb_data, indent=2, ensure_ascii=False)
content = content[:wb_match.start(2)] + new_wb_json + content[wb_match.end(2):]

# 6. Update Verification and continuation
assert "142实际检查见本run required-checks-142.json" in content
content = content.replace("142实际检查见本run required-checks-142.json", "143实际检查见本run required-checks-143.json")

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated to Checkpoint 143 via JSON-parsed writeback!")
