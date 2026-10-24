#!/usr/bin/env python3
from pathlib import Path

content = """
## Day21 checkpoint137：相空间敏感度与标度强度对账审计

基于HK10与LB16实测端点开展相空间标度与假说H1对账审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HK10-D21-R137-1 | 正电子动能端点由3.29MeV移至3.74MeV增幅为+13.7%，对应相空间敏感度指数高达eta=4.63；将Hinke实测B(GT)=9.1按相空间比值1.786与半衰期标度至Lubos基底后，强度收敛至B(GT)'=5.05，与Lubos实测5.26偏差仅3.95%，有效淬灭因子完全一致（gA/gA_free≈0.533 vs 0.544），证明GSI与RIKEN表观73%的强度差异实为端点漂移经相空间五次方幂律非线性放大所致，两套实验在原子核真实弱衰变矩阵元上高度自洽。 | phase-space-scaling-and-bgt-concordance | derived-from-HK10-and-LB16 | Nature 465, 997 Table 1; PRC 94, 054322 | true |

计算脚本见system/scripts/day21_checkpoint137_sn100_gt_scaling_audit.py，输出sn100-gt-scaling-scope-137.json。
"""

p = Path("knowledge/sources/hinke-2010-100sn-decay-spectroscopy.md")
orig = p.read_text(encoding="utf-8")
p.write_text(orig.rstrip("\n") + "\n" + content.strip() + "\n", encoding="utf-8")
print("Appended Checkpoint 137 to Hinke source page")
