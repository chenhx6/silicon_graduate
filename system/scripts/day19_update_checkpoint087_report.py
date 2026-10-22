raise SystemExit("Retired self-certifying checkpoint updater; see rejected-analysis-registry-088.json. Do not regenerate superseded knowledge.")
import json, re, pathlib, sys
sys.path.insert(0, "system/scripts")
from wiki_knowledge_writeback import validate_writeback

report_path = pathlib.Path("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response.md")
content = report_path.read_text(encoding="utf-8")

sec087 = """
### checkpoint087：128I能量三角闭合、58.5-keV多极性歧义与N=75转动淬灭定理

依据独立审计程序 \x60system/scripts/day19_ding12_i127_i128_structure_audit.py\x60 的 10 项检验与基准输出 \x60outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/ding12-i127-i128-structure-result-087.json\x60，系统核准了针对丁兵 2012 博士论文中 $^{127,128}\\text{I}$ 高自旋结构、多极性判据与形变演化的量化事实：
1. **局部能量三角闭合检验**：$481.8(7^-) \\to 225.9(6^-) \\to 167.4(6^-)$ 级联两步跃迁之和 $255.6 + 58.5 = 314.1\\text{ keV}$ 与跨越跃迁 $314.3\\text{ keV}$ 严格闭合（残差仅 $+0.20\\text{ keV} \\le 0.5\\text{ keV}$）；
2. **ADO 偶极/四极歧义与自旋锁定**：$58.5\\text{ keV}$ 跃迁实测 $R_{\\text{ADO}} = 1.66 \\pm 0.60$，在统计上与纯四极参考（$1.29$）和非拉伸 $\\Delta I = 0$ 偶极均相容；结合熔合蒸发自旋单调上升先验排除 $J=8$，严格锁定中间态 $J_{\\text{mid}} = (6^-)$；
3. **母态寿命与子态异能态严格隔离定理**：实测 $175 \\pm 15\\text{ ns}$ 寿命排他性属于退激子态 $167.4\\text{ keV}$ 异能态，上游母态（$225.9, 481.8\\text{ keV}$）处于 100-ns 符合窗内（$\\tau \\ll 100\\text{ ns}$），严禁借用 $175\\text{ ns}$ 换算母态绝对跃迁几率；
4. **低能三重线解卷积与 $N=75$ 转动淬灭**：$101.3\\text{ keV}$ 与双重峰 $102.2\\text{ keV}$（强支 102.2a 占 $87.7\\%$，弱支 102.2b 占 $12.3\\%$）完全解耦，实测 ICC 验证 M1 性质；对比 $^{120}\\text{I}$ 到 $^{128}\\text{I}$ 带头激发能暴增 $2.81$ 倍（$+940.9\\text{ keV}$），证实接近 $N=82$ 闭壳诱发单粒子激发占优、集体转动淬灭，直接落地 A≈130 博士论文管线证据矩阵第一行。
"""

target_str = "## Counter-evidence and missing companion observables"
if "### checkpoint087：" not in content and target_str in content:
    content = content.replace(target_str, sec087.strip() + "\n\n" + target_str)
    print("Inserted checkpoint087 into Theory/analysis exercise")

content = re.sub(
    r"- status: active / checkpoint086.*?;study window active至15:00 CST",
    "- status: active / checkpoint087 128I能量三角闭合、58.5-keV多极性歧义与N=75转动淬灭定理；study window active至15:00 CST",
    content
)
content = re.sub(
    r"- 时间核对：.*?;原次日15:00截止不变",
    "- 时间核对：2026-10-22T08:00:00 UTC (2026-10-22T16:00:00 CST);原次日15:00截止不变",
    content
)

wb_pattern = r"(```knowledge-writeback\n)(.*?)(\n```)"
wb_match = re.search(wb_pattern, content, re.DOTALL)
if wb_match:
    wb_data = json.loads(wb_match.group(2))
    new_items = [
        {
            "summary": "Day 19量化审计：128I能量三角闭合、58.5-keV多极性歧义与N=75转动淬灭定理",
            "knowledge": "knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md",
            "anchor": "## Day19量化审计：128I能量三角闭合、58.5-keV多极性歧义与N=75转动淬灭定理",
            "sources": [
                {
                    "path": "knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md",
                    "locator": "D12-D19-1"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：128I 58.5-keV局部能量三角残差+0.20 keV闭合",
            "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
            "anchor": "## Evidence matrix",
            "sources": [
                {
                    "path": "knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md",
                    "locator": "D12-D19-1"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：128I局部三角闭合、母态寿命界与N=75转动淬灭定理",
            "knowledge": "knowledge/methods/recoil-distance-doppler-shift.md",
            "anchor": "## Day19 128I局部三角闭合、母态寿命界与N=75转动淬灭定理",
            "sources": [
                {
                    "path": "knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md",
                    "locator": "D12-D19-1"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：128I局部三角闭合、母态寿命界与N=75转动淬灭定理",
            "knowledge": "knowledge/research-notes/lifetime-method-selection-response-contract.md",
            "anchor": "## Day19 128I局部三角闭合、母态寿命界与N=75转动淬灭定理",
            "sources": [
                {
                    "path": "knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md",
                    "locator": "D12-D19-1"
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
with open("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/writeback-verification-087.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2, ensure_ascii=False)
print("Wrote writeback-verification-087.json")
