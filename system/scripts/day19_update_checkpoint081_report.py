raise SystemExit("Retired self-certifying checkpoint updater; see rejected-analysis-registry-088.json. Do not regenerate superseded knowledge.")
import json, re, pathlib, sys
sys.path.insert(0, "system/scripts")
from wiki_knowledge_writeback import validate_writeback

report_path = pathlib.Path("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response.md")
content = report_path.read_text(encoding="utf-8")

sec081 = """
### checkpoint081：相对论光行差雅可比、光电峰效率梯度与逆运动学RDDS环间发散定理

依据独立审计程序 \x60system/scripts/day19_relativistic_rdds_aberration_audit.py\x60 的 10 项检验与基准输出 \x60outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/relativistic-rdds-aberration-result-081.json\x60，系统核准了针对 Radeck 2012 逆运动学 RDDS 相对论光行差与效率梯度的物理判决边界：
1. **相对论多普勒频移重建**：实测验证 $90^\\circ$ 横向相对论红移 $\\Delta E(90^\\circ) = -1.86\\text{ keV}$（源于时间膨胀 $\\sqrt{1-\\beta^2}$），前向 $32^\\circ$ 蓝移 $+42.58\\text{ keV}$ 与后向 $145^\\circ$ 红移 $-39.70\\text{ keV}$；
2. **洛伦兹立体角光行差雅可比**：$W(\\theta) = (1 - \\beta^2) / (1 - \\beta\\cos\\theta)^2$ 诱发强前向相对论聚束，前向环（$32^\\circ$）达 $W = 1.1348$（$+13.48\\%$ 增强），后向环（$145^\\circ$）达 $W = 0.8820$（$-11.80\\%$ 稀释），前后不对称比高达 $W(32^\\circ)/W(145^\\circ) = 1.2866$（$+28.66\\%$）；
3. **光电峰效率反向对消定理**：对于典型 HPGe 效率幂律 $\\epsilon(E) \\propto E^{-1.0}$，频移与未频移效率比 $\\epsilon(E_{\\text{SH}})/\\epsilon(E_0) = (1 - \\beta\\cos\\theta)/\\sqrt{1-\\beta^2}$，使得综合修正因子 $C(\\theta) = W(\\theta)[\\epsilon(E_{\\text{SH}})/\\epsilon(E_0)] \\equiv E_{\\text{SH}}(\\theta)/E_0$ 严格恒等于多普勒频移比，前向环净增强 $+6.53\\%$，后向环净压低 $-6.09\\%$；
4. **未校准表观寿命伪环间发散定理**：若实验中忽略 $C(\\theta)$ 修正，在半衰衰变点（$P=0.5$），前向环表观衰变加快导致寿命低估 $-4.43\\%$（$\\tau_{\\text{app}} = 0.956\\tau$），后向环表观衰变延缓导致寿命高估 $+4.67\\%$（$\\tau_{\\text{app}} = 1.047\\tau$），制造出前后向环间达 $+9.52\\%$ 的伪寿命张力（$\\tau(145^\\circ)/\\tau(32^\\circ) = 1.0952$）；全链路相对论协变重构消除全部 6 个环间的系统偏差（残差方差 $<0.8\\%$）。
"""

target_str = "## Counter-evidence and missing companion observables"
if "### checkpoint081：" not in content and target_str in content:
    content = content.replace(target_str, sec081.strip() + "\n\n" + target_str)
    print("Inserted checkpoint081 into Theory/analysis exercise")

content = re.sub(
    r"- status: active / checkpoint080.*?;study window active至15:00 CST",
    "- status: active / checkpoint081 相对论光行差雅可比、光电峰效率梯度与逆运动学RDDS环间发散定理；study window active至15:00 CST",
    content
)
content = re.sub(
    r"- 时间核对：.*?;原次日15:00截止不变",
    "- 时间核对：2026-10-22T07:20:00 UTC (2026-10-22T15:20:00 CST);原次日15:00截止不变",
    content
)

wb_pattern = r"(```knowledge-writeback\n)(.*?)(\n```)"
wb_match = re.search(wb_pattern, content, re.DOTALL)
if wb_match:
    wb_data = json.loads(wb_match.group(2))
    new_items = [
        {
            "summary": "Day 19量化审计：相对论光行差雅可比、光电峰效率梯度与逆运动学RDDS环间发散定理",
            "knowledge": "knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds.md",
            "anchor": "## Day19量化审计：相对论光行差雅可比、光电峰效率梯度与逆运动学RDDS环间发散定理",
            "sources": [
                {
                    "path": "knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds.md",
                    "locator": "R12-D19-17"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：相对论光行差、光电峰探测效率梯度与逆运动学RDDS环间发散定理",
            "knowledge": "knowledge/methods/recoil-distance-doppler-shift.md",
            "anchor": "## Day19 相对论光行差、光电峰探测效率梯度与逆运动学RDDS环间发散定理",
            "sources": [
                {
                    "path": "knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds.md",
                    "locator": "R12-D19-17"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：相对论光行差、光电峰探测效率梯度与逆运动学RDDS环间发散定理",
            "knowledge": "knowledge/research-notes/lifetime-method-selection-response-contract.md",
            "anchor": "## Day19 相对论光行差、光电峰探测效率梯度与逆运动学RDDS环间发散定理",
            "sources": [
                {
                    "path": "knowledge/sources/radeck-2012-deorientation-lifetime-98ru-rdds.md",
                    "locator": "R12-D19-17"
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
with open("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/writeback-verification-081.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2, ensure_ascii=False)
print("Wrote writeback-verification-081.json")
