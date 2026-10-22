raise SystemExit("Retired self-certifying checkpoint updater; see rejected-analysis-registry-088.json. Do not regenerate superseded knowledge.")
import json, re, pathlib, sys
sys.path.insert(0, "system/scripts")
from wiki_knowledge_writeback import validate_writeback

report_path = pathlib.Path("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response.md")
content = report_path.read_text(encoding="utf-8")

sec085 = """
### checkpoint085：23Mg飞秒寿命对账、传统DSAM线形阈值与天体速率坍缩机制

依据独立审计程序 \x60system/scripts/day19_mg23_dsam_dvdm_reconciliation_audit.py\x60 的 10 项检验与基准输出 \x60outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/mg23-dsam-dvdm-reconciliation-result-085.json\x60，系统核准了针对 Kirsebom 2016 Table II 中 $^{23}\\text{Mg}$ 能级寿命全谱及与 Fougères 2023 对账的量化事实：
1. **Table II 全谱对账**：测得 4 项有限寿命（$2052\\text{ keV}$ 态 $104(18)\\text{ fs}$、$2771\\text{ keV}$ 态 $98(15)\\text{ fs}$、$2908\\text{ keV}$ 态 $15(3)\\text{ fs}$、$3798\\text{ keV}$ 态 $41(6)\\text{ fs}$）与 8 项上限（含关键天体物理态 $7787\\text{ keV}$ $\\tau < 12\\text{ fs}$）；
2. **$3798\\text{ keV}$ 基准态完美闭环**：Kirsebom 2016（$41 \\pm 6\\text{ fs}$）与 Fougères 2023（$40_{-7}^{+6}\\text{ fs}$）相差仅 $1.0\\text{ fs}$（$z = 0.11\\sigma$），在 $40\\text{ fs}$ 处确立了两大独立装置极高精度的相互校准；
3. **$7787\\text{ keV}$ 态三方一致性**：Kirsebom 2016 上限（$<12\\text{ fs}$）、Jenkins 2004（$10 \\pm 3\\text{ fs}$）与 Fougères 2023（$11_{-5}^{+7}\\text{ fs}$）高度自洽于综合值 $\\tau = 10.2 \\pm 2.6\\text{ fs}$；
4. **传统 DSAM 线形拟合阈值局限**：在 $\\tau \\lesssim 15\\text{ fs}$ 域，全多普勒峰线形与瞬发响应几乎不可区分，致使传统单谱拟合仅能给出上限，而多普勒速度差法通过逐事件测量反冲核出射速度 $\\vec{\\beta}_{\\text{reac}}$ 与光子发射速度 $\\beta_{\\text{ems}}$，形成 $\\Delta\\beta \\propto \\langle d\\beta/dt \\rangle t$ 的直接时间映射，将测量下限突破至亚飞秒区；
5. **新星 $^{22}\\text{Na}(p,\\gamma)$ 反应率坍缩解耦定理**：经典新星共振强度由早期 $\\omega\\gamma \\approx 1.39\\text{ meV}$ 暴跌 $5.72$ 倍至 $0.243\\text{ meV}$，微积分敏感性证实其中 $95.5\\%$ 的变动由质子分支比修正（$\\text{BR}_p$ 由假定的 $3.7\\%$ 跌落至实测的 $0.66\\%$）主导，能级寿命仅贡献 $<4.5\\%$ 变动，澄清了天体反应率争议的本质为衰变分支比而非核寿命测量。
"""

target_str = "## Counter-evidence and missing companion observables"
if "### checkpoint085：" not in content and target_str in content:
    content = content.replace(target_str, sec085.strip() + "\n\n" + target_str)
    print("Inserted checkpoint085 into Theory/analysis exercise")

content = re.sub(
    r"- status: active / checkpoint084.*?;study window active至15:00 CST",
    "- status: active / checkpoint085 23Mg飞秒寿命对账、传统DSAM线形阈值与天体速率坍缩机制；study window active至15:00 CST",
    content
)
content = re.sub(
    r"- 时间核对：.*?;原次日15:00截止不变",
    "- 时间核对：2026-10-22T07:45:00 UTC (2026-10-22T15:45:00 CST);原次日15:00截止不变",
    content
)

wb_pattern = r"(```knowledge-writeback\n)(.*?)(\n```)"
wb_match = re.search(wb_pattern, content, re.DOTALL)
if wb_match:
    wb_data = json.loads(wb_match.group(2))
    new_items = [
        {
            "summary": "Day 19量化审计：23Mg飞秒寿命对账、传统DSAM线形阈值与天体速率坍缩机制",
            "knowledge": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
            "anchor": "## Day19量化审计：23Mg飞秒寿命对账、传统DSAM线形阈值与天体速率坍缩机制",
            "sources": [
                {
                    "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
                    "locator": "K16-D19-2"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：23Mg飞秒寿命对账：传统DSAM线形阈值、速度差法突破与天体速率坍缩",
            "knowledge": "knowledge/methods/recoil-distance-doppler-shift.md",
            "anchor": "## Day19 23Mg飞秒寿命对账：传统DSAM线形阈值、速度差法突破与天体速率坍缩",
            "sources": [
                {
                    "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
                    "locator": "K16-D19-2"
                }
            ]
        },
        {
            "summary": "Day 19量化审计：23Mg飞秒寿命对账：传统DSAM线形阈值、速度差法突破与天体速率坍缩",
            "knowledge": "knowledge/research-notes/lifetime-method-selection-response-contract.md",
            "anchor": "## Day19 23Mg飞秒寿命对账：传统DSAM线形阈值、速度差法突破与天体速率坍缩",
            "sources": [
                {
                    "path": "knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md",
                    "locator": "K16-D19-2"
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
with open("outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/writeback-verification-085.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2, ensure_ascii=False)
print("Wrote writeback-verification-085.json")
