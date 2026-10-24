#!/usr/bin/env python3
from pathlib import Path

content = """
## Day21 checkpoint139：排版印刷异常与物理证伪边界审计

基于LV19 Table I三项局部异常（998.1 vs 997 keV、334.4 keV宇称元组、934.9/966.3 keV重复母态）开展排版印刷与物理反证界限审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV19-D21-R139-1 | 998.1 keV行按其打印Ei=5412.6 keV与D5终态闭合残差严格<1e-6，与5411.6的1.0 keV残差系不同门谱拟合中心微小漂移；334.4 keV的“27/2- -> 25/2+ M1/E2”100%违反电磁选择律，正文、Fig.1与IPDCO一致确证为正宇称，证明该'-'为孤立印刷脱漏；934.9/966.3 keV系LaTeX换页续表排版归入D6列，属D5带内跃迁。三项异常均属印刷排版与拟合舍入范畴，绝不能当作推翻手征对称性的实验反证，严禁擅自修改原表，实证证伪必须依靠物理可观测量（如Checkpoint 134偏振P>0）。 | typographical-anomaly-and-falsification-boundary | derived-from-VoR-and-selection-rules | 024314-4 Table I Bands D3, D5, D6 | true |

计算脚本见system/scripts/day21_checkpoint139_typographical_anomaly_audit.py，输出typographical-anomaly-scope-139.json。
"""

p = Path("knowledge/sources/lv-2019-chirality-135nd-reexamined.md")
orig = p.read_text(encoding="utf-8")
p.write_text(orig.rstrip("\n") + "\n" + content.strip() + "\n", encoding="utf-8")
print("Appended Checkpoint 139 to Lv 2019 source page")
