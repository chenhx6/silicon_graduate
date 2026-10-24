#!/usr/bin/env python3
from pathlib import Path

content = """
## Day21 checkpoint141：同母态寿命公因子协方差相消定理审计

基于MU07 Table I派生B(M1)/B(E2)比值开展同分母协方差代数相消审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D21-R141-1 | 在同一能级派生的B(M1)与B(E2)中，共同寿命tau及其约10%的SRIM阻止本领系统误差产生r=+0.856的强正相关协方差；在比值B(M1)/B(E2)中tau严格代数相消，比值真实相对不确定度（5.87%）较无相关独立正交传播假想误差（15.44%）尖锐2.63倍，确立了B比测试模型优于绝对B值但严禁独立误差四则传播的证据门法则。 | shared-denominator-covariance-cancellation | derived-from-Table-I-and-rate-equations | PRL 99, 172501 Table I | true |

计算脚本见system/scripts/day21_checkpoint141_shared_denominator_covariance_audit.py，输出shared-denominator-covariance-scope-141.json。
"""

p = Path("knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md")
orig = p.read_text(encoding="utf-8")
p.write_text(orig.rstrip("\n") + "\n" + content.strip() + "\n", encoding="utf-8")
print("Appended Checkpoint 141 to MU07 source page")
