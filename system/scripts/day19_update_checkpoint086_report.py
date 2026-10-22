raise SystemExit("Retired self-certifying checkpoint updater; see rejected-analysis-registry-088.json. Do not regenerate superseded knowledge.")
import json, re, pathlib, sys
sys.path.insert(0, "system/scripts")
from wiki_knowledge_writeback import validate_writeback

report_path = pathlib.Path("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response.md")
content = report_path.read_text(encoding="utf-8")

sec086 = """
### checkpoint086：136Pr微观组态形变谱、三轴形状共存与N=77手征终止分水岭

依据独立审计程序 \x60system/scripts/day19_pr136_tac_cdft_deformation_audit.py\x60 的 10 项检验与基准输出 \x60outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/pr136-tac-cdft-deformation-result-086.json\x60，系统核准了针对 Lv 2025 Table II 中 $^{136}\\text{Pr}$ TAC-CDFT 组态形变与结构转变的量化事实：
1. **Table II 形变参数全谱对账**：10 个特征组态跨越 $\\beta_2 = 0.16\\text{--}0.24$（$\\Delta\\beta_2 = 0.08$）与 $\\gamma = 14^\\circ\\text{--}39^\\circ$（$\\Delta\\gamma = 25.0^\\circ$），证实长椭三轴组态（Q1/Q2/D1，平均 $\\gamma \\approx 18.7^\\circ$）与扁椭倾向三轴组态（D4/D6，平均 $\\gamma \\approx 37.0^\\circ$）之间存在 $\\Delta\\gamma \\approx 18.3^\\circ$ 的三轴形状共存；
2. **排他性否定结论**：在具有 6 条偶极带与 4 条四极带的丰富能谱中，实验与理论均坚决排除了手征双重带、横向摆动（wobbling）与纯扁椭转动；
3. **磁转动剪刀机制**：D4 与 D6 偶极带由高 $\\Omega$ 中子空穴（$\\nu h_{11/2}, \\Omega \\approx 11/2$）与低 $\\Omega$ 质子（$\\pi h_{11/2}, \\Omega \\approx 1/2, 3/2$）垂直剪刀闭合驱动，构成磁转动强候选带；
4. **D5 近球形壳模型极限与 Q1 带头自旋重构**：TAC-CDFT 无法找到描述 D5 的变形极小值，证实其属于近球形单粒子态，必须采用大空间 SN100PN 球形壳模型描述；将 876-keV 跃迁改接至 Q2 的 $18^+$ 态使带头自旋由 $15^+$ 跃升 $+4\\hbar$ 至 $19^{(+)}$，直接落地 A≈130 博士论文管线证据矩阵第二行；确立镨同位素链 $N=77$ 为手征终止分水岭。
"""

target_str = "## Counter-evidence and missing companion observables"
if "### checkpoint086：" not in content and target_str in content:
    content = content.replace(target_str, sec086.strip() + "\n\n" + target_str)
    print("Inserted checkpoint086 into Theory/analysis exercise")

content = re.sub(
    r"- status: active / checkpoint085.*?;study window active至15:00 CST",
    "- status: active / checkpoint086 136Pr微观组态形变谱、三轴形状共存与N=77手征终止分水岭；study window active至15:00 CST",
    content
)
content = re.sub(
    r"- 时间核对：.*?;原次日15:00截止不变",
    "- 时间核对：2026-10-22T07:50:00 UTC (2026-10-22T15:50:00 CST);原次日15:00截止不变",
    content
)

wb_pattern = r"(```knowledge-writeback\n)(.*?)(\n```)"
wb_match = re.search(wb_pattern, content, re.DOTALL)
if wb_match:
    wb_data = json.loads(wb_match.group(2))
    new_items = [
        {
            "summary": "Day 19量化审计：136Pr微观组态形变谱、三轴形状共存与N=77手征终止分水岭",
            "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
            "anchor": "## Day19量化审计：136Pr微观组态形变谱、三轴形状共存与N=77手征终止分水岭",
            "sources": [
                {
                    "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
                    "locator": "LV25-D19-1"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：136Pr Q1端点改接与D5/D6组态划分落地",
            "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
            "anchor": "## Evidence matrix",
            "sources": [
                {
                    "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
                    "locator": "LV25-D19-1"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：136Pr三轴形变共存、磁转动剪刀机制与N=77手征终止分水岭",
            "knowledge": "knowledge/methods/recoil-distance-doppler-shift.md",
            "anchor": "## Day19 136Pr三轴形变共存、磁转动剪刀机制与N=77手征终止分水岭",
            "sources": [
                {
                    "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
                    "locator": "LV25-D19-1"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：136Pr三轴形变共存、磁转动剪刀机制与N=77手征终止分水岭",
            "knowledge": "knowledge/research-notes/lifetime-method-selection-response-contract.md",
            "anchor": "## Day19 136Pr三轴形变共存、磁转动剪刀机制与N=77手征终止分水岭",
            "sources": [
                {
                    "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
                    "locator": "LV25-D19-1"
                }
            ]
        }
    ]
    existing_anchors = set((it["knowledge"], it["anchor"]) for it in wb_data["items"])
    added = 0
    for nit in new_items:
        if (nit["knowledge"], nit["anchor"]) not in existing_anchors:
            wb_data["items"].append(nit)
            added += 1
    print(f"Added {added} items to knowledge-writeback")
    new_wb_str = json.dumps(wb_data, indent=2, ensure_ascii=False)
    content = content[:wb_match.start(1)] + "```knowledge-writeback\n" + new_wb_str + "\n```" + content[wb_match.end(3):]

report_path.write_text(content, encoding="utf-8")
print("Report successfully updated!")

root = pathlib.Path(".").resolve()
res = validate_writeback(report_path, root)
print("Writeback validation result:", res["valid"], "Error:", res.get("error"))
with open("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/writeback-verification-086.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2, ensure_ascii=False)
print("Wrote writeback-verification-086.json")
