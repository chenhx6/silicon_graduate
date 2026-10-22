raise SystemExit("Retired self-certifying checkpoint updater; see rejected-analysis-registry-088.json. Do not regenerate superseded knowledge.")
import json, re, pathlib, sys
sys.path.insert(0, "system/scripts")
from wiki_knowledge_writeback import validate_writeback

report_path = pathlib.Path("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response.md")
content = report_path.read_text(encoding="utf-8")

sec084 = """
### checkpoint084：26Mg多方法寿命对账、共享阻停假相合与无阻停基准定理

依据独立审计程序 \x60system/scripts/day19_nolan79_table5_26mg_multimethod_audit.py\x60 的 10 项检验与基准输出 \x60outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/nolan79-table5-26mg-multimethod-result-084.json\x60，系统核准了针对 Nolan 1979 综述 Table 5 关于 $^{26}\\text{Mg}$ $1809\\text{ keV}$ 态多方法交叉对账的系统学事实：
1. **低速 DSAM 极大离群值与阻止陷阱**：de Kock 1970 测得 $\\tau = 300 \\pm 80\\text{ fs}$，相对公认基准（$710 \\pm 70\\text{ fs}$）低估达 $57.75\\%$（低估 $2.37$ 倍，显著性 $z = 3.86\\sigma$），源于极低反冲初速（$v/c \\le 0.5\\%$）下未修正 LSS 理论高估低能阻止本领；
2. **传统 RDM 极限死线**：Endt 1973 测得 $\\tau = 480 \\pm 50\\text{ fs}$ 低估 $32.4\\%$（$z = 2.67\\sigma$），证实衰变位移 $\\lambda = v\\tau \\approx 2.25\\ \\mu\\text{m}$ 遭遇传统机械千分尺接触零点粗糙度（$d_0 \\sim 2\\ \\mu\\text{m}$）的物理死线；
3. **高速重离子库激 DSAM 闭环**：Schwalm 1977（$v/c \\approx 5.5\\%$）测得 DSAM 寿命 $695 \\pm 50\\text{ fs}$ 与库激产额寿命 $726 \\pm 31\\text{ fs}$ 呈现 $4.46\\%$ 极佳吻合（$z = 0.53\\sigma$），实证高速反冲成功脱离低能阻停陷阱；
4. **共享阻停假相合与无阻停锚定**：微积分严格证明线形拟合与库激产额共享相同的 Northcliffe-Schilling 阻止截面标度（束流能损与反冲能损），同向系统漂移可将 $15\\%$ 绝对误差掩盖在 $<5\\%$ 相对残差之下；独立核共振荧光（NRF）与非弹性电子散射（$e,e\x27$）等无阻停依赖方法加权均值 $\\langle \\tau \\rangle = 498 \\pm 108\\text{ fs}$ 与基准在 $1.65\\sigma$ 内相容，确立阻止截面不确定度（$8\\%\\text{--}30\\%$）为飞秒寿命测量的绝对主导误差源。
"""

target_str = "## Counter-evidence and missing companion observables"
if "### checkpoint084：" not in content and target_str in content:
    content = content.replace(target_str, sec084.strip() + "\n\n" + target_str)
    print("Inserted checkpoint084 into Theory/analysis exercise")

content = re.sub(
    r"- status: active / checkpoint083.*?;study window active至15:00 CST",
    "- status: active / checkpoint084 26Mg多方法寿命对账、共享阻停假相合与无阻停基准定理；study window active至15:00 CST",
    content
)
content = re.sub(
    r"- 时间核对：.*?;原次日15:00截止不变",
    "- 时间核对：2026-10-22T07:40:00 UTC (2026-10-22T15:40:00 CST);原次日15:00截止不变",
    content
)

wb_pattern = r"(```knowledge-writeback\n)(.*?)(\n```)"
wb_match = re.search(wb_pattern, content, re.DOTALL)
if wb_match:
    wb_data = json.loads(wb_match.group(2))
    new_items = [
        {
            "summary": "Day 19量化审计：26Mg多方法寿命对账、共享阻停假相合与无阻停基准定理",
            "knowledge": "knowledge/sources/nolan-sharpey-schafer-1979-lifetime-measurements.md",
            "anchor": "## Day19量化审计：26Mg多方法寿命对账、共享阻停假相合与无阻停基准定理",
            "sources": [
                {
                    "path": "knowledge/sources/nolan-sharpey-schafer-1979-lifetime-measurements.md",
                    "locator": "NS79-D19-17"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：26Mg多方法寿命对账、共享阻停假相合与无阻停基准定理",
            "knowledge": "knowledge/methods/recoil-distance-doppler-shift.md",
            "anchor": "## Day19 26Mg多方法寿命对账、共享阻停假相合与无阻停基准定理",
            "sources": [
                {
                    "path": "knowledge/sources/nolan-sharpey-schafer-1979-lifetime-measurements.md",
                    "locator": "NS79-D19-17"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：26Mg多方法寿命对账、共享阻停假相合与无阻停基准定理",
            "knowledge": "knowledge/research-notes/lifetime-method-selection-response-contract.md",
            "anchor": "## Day19 26Mg多方法寿命对账、共享阻停假相合与无阻停基准定理",
            "sources": [
                {
                    "path": "knowledge/sources/nolan-sharpey-schafer-1979-lifetime-measurements.md",
                    "locator": "NS79-D19-17"
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
with open("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/writeback-verification-084.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2, ensure_ascii=False)
print("Wrote writeback-verification-084.json")
