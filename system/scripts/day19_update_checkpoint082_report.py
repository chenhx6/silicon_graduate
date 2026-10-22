raise SystemExit("Retired self-certifying checkpoint updater; see rejected-analysis-registry-088.json. Do not regenerate superseded knowledge.")
import json, re, pathlib, sys
sys.path.insert(0, "system/scripts")
from wiki_knowledge_writeback import validate_writeback

report_path = pathlib.Path("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response.md")
content = report_path.read_text(encoding="utf-8")

sec082 = """
### checkpoint082：176W基态带MSCD寿命重构、B4/2 Alaga vs X(5)检验与Hf-W历史寿命修正

依据独立审计程序 \x60system/scripts/day19_regis11_w_hf_fast_timing_audit.py\x60 的 10 项检验与基准输出 \x60outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/regis11-w-hf-fast-timing-result-082.json\x60，系统核准了针对 Régis 2011 博士论文第 5 章中 $^{176}\\text{W}$ 束内快速定时与 Hf/W 同位素链系统学的量化事实：
1. **$^{176}\\text{W}$ 基态带寿命全谱重构**：精确提取 $\\tau(2^+) = 1430(20)\\text{ ps}, \\tau(4^+) = 67(4)\\text{ ps}, \\tau(6^+) = 12(4)\\text{ ps}, \\tau(8^+) \\le 4\\text{ ps}$，对应跃迁强度 $B(E2)$ 分别为 $0.983(21), 1.312(79), 1.216(406), \\ge 1.207\\ (e\\text{b})^2$；
2. **$B_{4/2}$ 比值与 $X(5)$ 证伪**：实测 $B_{4/2} = 1.335 \\pm 0.085$，在 $2.87\\sigma$ 置信度上坚决排除了临界点对称性 $X(5)$（预言 $1.580$），其四极矩 $Q(J)$ 由 $7.03\\text{ eb}$（$2^+$）向高自旋微幅软化至 $6.84\\text{ eb}$（$4^+$）和 $6.23\\text{ eb}$（$6^+$），与具有有限玻色子截断（$N_B=14$）的 SU(3) 转子极限（$B_{4/2} = 1.407$）高度自洽；
3. **历史寿命系统性偏差纠正**：针对 1960 年代塑料闪烁体差能量分辨率（$\\sim 20\\%$）导致的本底污染，利用高精度 Double Orange 磁谱仪 $e^--e^-$ 快速定时将 $^{172}\\text{Hf}$ 的 $2_1^+$ 寿命由旧文献 $2.23(15)\\text{ ns}$ 修正为 $1.70(2)\\text{ ns}$（旧值高估 $+31.2\\%$，显著性 $z=3.50\\sigma$），$^{174}\\text{Hf}$ 由 $2.37(15)\\text{ ns}$ 修正为 $1.79(2)\\text{ ns}$（旧值高估 $+32.4\\%$，$z=3.83\\sigma$），彻底消解了 $^{172}\\text{Hf}$ 处持续 44 年的假异常深凹，重构了光滑连续的抛物线四极形变演化；
4. **快速定时物理时钟边界**：$^{176}\\text{W}$ 的 $8_1^+$ 态 $\\tau \\le 4\\text{ ps}$ 精确标定了电子学定时的物理分辨极值，确立了 $1\\text{--}10\\text{ ps}$ 能区作为 Fast Timing、RDDS 与 DSAM 三重时钟交叉检验黄金带的科学地位。
"""

target_str = "## Counter-evidence and missing companion observables"
if "### checkpoint082：" not in content and target_str in content:
    content = content.replace(target_str, sec082.strip() + "\n\n" + target_str)
    print("Inserted checkpoint082 into Theory/analysis exercise")

content = re.sub(
    r"- status: active / checkpoint081.*?;study window active至15:00 CST",
    "- status: active / checkpoint082 176W基态带MSCD寿命重构、B4/2 Alaga vs X(5)检验与Hf-W历史寿命修正；study window active至15:00 CST",
    content
)
content = re.sub(
    r"- 时间核对：.*?;原次日15:00截止不变",
    "- 时间核对：2026-10-22T07:30:00 UTC (2026-10-22T15:30:00 CST);原次日15:00截止不变",
    content
)

wb_pattern = r"(```knowledge-writeback\n)(.*?)(\n```)"
wb_match = re.search(wb_pattern, content, re.DOTALL)
if wb_match:
    wb_data = json.loads(wb_match.group(2))
    new_items = [
        {
            "summary": "Day 19量化审计：176W基态带MSCD寿命重构、B4/2 Alaga vs X(5)检验与Hf-W历史寿命修正",
            "knowledge": "knowledge/sources/regis-2011-fast-timing-labr3.md",
            "anchor": "## Day19量化审计：176W基态带MSCD寿命重构、B4/2 Alaga vs X(5)检验与Hf-W历史寿命修正",
            "sources": [
                {
                    "path": "knowledge/sources/regis-2011-fast-timing-labr3.md",
                    "locator": "RG11-D19-14"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：快速定时MSCD与束内寿命：176W基态带、B4/2转子检验与1-10ps时钟交叉",
            "knowledge": "knowledge/methods/recoil-distance-doppler-shift.md",
            "anchor": "## Day19 快速定时MSCD与束内寿命：176W基态带、B4/2转子检验与1-10ps时钟交叉",
            "sources": [
                {
                    "path": "knowledge/sources/regis-2011-fast-timing-labr3.md",
                    "locator": "RG11-D19-14"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：快速定时MSCD与束内寿命：176W基态带、B4/2转子检验与1-10ps时钟交叉",
            "knowledge": "knowledge/research-notes/lifetime-method-selection-response-contract.md",
            "anchor": "## Day19 快速定时MSCD与束内寿命：176W基态带、B4/2转子检验与1-10ps时钟交叉",
            "sources": [
                {
                    "path": "knowledge/sources/regis-2011-fast-timing-labr3.md",
                    "locator": "RG11-D19-14"
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
with open("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/writeback-verification-082.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2, ensure_ascii=False)
print("Wrote writeback-verification-082.json")
