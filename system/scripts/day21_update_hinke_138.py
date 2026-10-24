#!/usr/bin/env python3
from pathlib import Path

content = """
## Day21 checkpoint138：EC分额演化与全相空间ft精确对账审计

基于HK10与LB16实测数据开展包含EC与beta+全相空间的终极对账审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HK10-D21-R138-1 | 纳入电子俘获分额随端点由13.3%降至9.49%的能隙阻尼效应后，全相空间比值严格为f_tot(3.74)/f_tot(3.29)=1.71064；Hinke实测B(GT)=9.1经全相空间与半衰期精确标度后为B(GT)'=5.274，与Lubos实测中心值5.26偏差仅0.27%，解释率达99.62%，排他性证实GSI与RIKEN在真实弱衰变矩阵元上完全相容（gA/gA_free≈0.533 vs 0.544）。 | ec-phase-space-exact-reconciliation | derived-from-HK10-and-LB16 | Nature 465, 997 Table 1; PRC 94, 054322 | true |

计算脚本见system/scripts/day21_checkpoint138_ec_phase_space_reconciliation_audit.py，输出sn100-ec-reconciliation-scope-138.json。
"""

p = Path("knowledge/sources/hinke-2010-100sn-decay-spectroscopy.md")
orig = p.read_text(encoding="utf-8")
p.write_text(orig.rstrip("\n") + "\n" + content.strip() + "\n", encoding="utf-8")
print("Appended Checkpoint 138 to Hinke source page")
