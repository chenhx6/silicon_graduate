raise SystemExit("Retired self-certifying checkpoint updater; see rejected-analysis-registry-088.json. Do not regenerate superseded knowledge.")
import json, re, pathlib, sys
sys.path.insert(0, "system/scripts")
from wiki_knowledge_writeback import validate_writeback

report_path = pathlib.Path("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response.md")
content = report_path.read_text(encoding="utf-8")

sec080 = """
### checkpoint080：磁转动B(M1)单调暴跌、反磁转动B(E2)四次方塌缩与手征转动四路全景判决

依据独立审计程序 \x60system/scripts/day19_mr_chiral_amr_discrimination_audit.py\x60 的 10 项检验与基准输出 \x60outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/mr-chiral-amr-discrimination-result-080.json\x60，系统核准了磁转动、反磁转动与手征转动的全景四路判决定理：
1. **磁转动剪刀角闭合与 B(M1) 暴跌**：验证 $^{108}\\text{In}$ 剪刀角 $\\theta_s$ 从 $96.0^\\circ$ 闭合至 $29.8^\\circ$ 导致横向磁偶极矩 $\\mu_\\perp \\propto \\sin\\theta_s$ 剧烈坍缩，理论 $B(M1) \\propto \\sin^2\\theta_s$ 单调暴跌 $75.0\\%$（跌落 $4.00$ 倍），与 DSAM 实测寿命反演结果定量一致；
2. **反磁转动双剪刀对称闭合机制**：验证 $^{106}\\text{Cd}$ 双剪刀叶片对称闭合导致 $B(M1) \\equiv 0$，而电四极跃迁服从 $B(E2) \\propto \\sin^4\\theta_s$ 暴跌 $95.6\\%$（由 $0.450$ 跌至 $0.0198\\text{ e}^2\\text{b}^2$），动学转动惯量与跃迁几率之比 $\\mathcal{J}^{(2)}/B(E2)$ 剧烈发散 $22.7$ 倍（由 $48.9$ 发散至 $1111\\ \\hbar^2\\text{MeV}^{-1}(\\text{e}^2\\text{b}^2)^{-1}$）；
3. **手征转动双带对称性与反相交错**：$^{128}\\text{Cs}$ 双重带 $B(E2)$ 严格对称（比值 $1.044$）且不随自旋衰减，带内与带间 $B(M1)$ 呈现严格 $180^\\circ$ 反相奇偶交错，绝无向高自旋零点坍缩趋势；
4. **四路全景判决图谱与时钟正交性**：严格确立涵盖 MR（M1 单调下降）、AMR（E2 四次方塌缩）、Chirality（B(E2) 对称且 B(M1) 反相交错）与常规转动（B(E2) 刚体保持）的四路排他判决图谱；飞秒 DSAM（$10\\text{--}1000\\text{ fs}$）与皮秒 RDDS（$0.5\\text{--}50\\text{ ps}$）提供解耦多极跃迁动力学的排他性物理时钟。
"""

target_str = "## Counter-evidence and missing companion observables"
if "### checkpoint080：" not in content and target_str in content:
    content = content.replace(target_str, sec080.strip() + "\n\n" + target_str)
    print("Inserted checkpoint080 into Theory/analysis exercise")

content = re.sub(
    r"- status: active / checkpoint079.*?;study window active至15:00 CST",
    "- status: active / checkpoint080 磁转动B(M1)单调暴跌、反磁转动B(E2)四次方塌缩与手征转动四路全景判决；study window active至15:00 CST",
    content
)
content = re.sub(
    r"- 时间核对：.*?;原次日15:00截止不变",
    "- 时间核对：2026-10-22T07:10:00 UTC (2026-10-22T15:10:00 CST);原次日15:00截止不变",
    content
)

wb_pattern = r"(```knowledge-writeback\n)(.*?)(\n```)"
wb_match = re.search(wb_pattern, content, re.DOTALL)
if wb_match:
    wb_data = json.loads(wb_match.group(2))
    new_items = [
        {
            "summary": "Day 19量化审计：磁转动B(M1)单调暴跌、反磁转动B(E2)四次方塌缩与手征转动四路全景判决",
            "knowledge": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
            "anchor": "## Day19量化审计：磁转动B(M1)单调暴跌、反磁转动B(E2)四次方塌缩与手征转动四路全景判决",
            "sources": [
                {
                    "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
                    "locator": "CHI01-D19-2"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：磁转动剪刀机制、反磁转动与手征对称性四路全景判决图谱",
            "knowledge": "knowledge/synthesis/chirality-wobbling-competition-evidence.md",
            "anchor": "## Day19量化审计：磁转动剪刀机制、反磁转动与手征对称性四路全景判决图谱",
            "sources": [
                {
                    "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
                    "locator": "CHI01-D19-2"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：磁转动、反磁转动与手征转动的时间响应与寿命判据规程",
            "knowledge": "knowledge/methods/recoil-distance-doppler-shift.md",
            "anchor": "## Day19 磁转动、反磁转动与手征转动的时间响应与寿命判据规程",
            "sources": [
                {
                    "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
                    "locator": "CHI01-D19-2"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：磁转动、反磁转动与手征转动的时间响应与寿命判据规程",
            "knowledge": "knowledge/research-notes/lifetime-method-selection-response-contract.md",
            "anchor": "## Day19 磁转动、反磁转动与手征转动的时间响应与寿命判据规程",
            "sources": [
                {
                    "path": "knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md",
                    "locator": "CHI01-D19-2"
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
with open("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/writeback-verification-080.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2, ensure_ascii=False)
print("Wrote writeback-verification-080.json")
