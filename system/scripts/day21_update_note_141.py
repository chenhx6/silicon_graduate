#!/usr/bin/env python3
from pathlib import Path

content = """
## Checkpoint141：同母态寿命公因子协方差相消定理审计

这是本任务L2误差传播代数解析与L3实验模型对账设计，基于[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07 Table I派生的B(M1)/B(E2)强度比，系统阐明同母态协方差抵消的数学本质与科学判据：

### 同母态寿命协方差相消数学推导

1. **同分母寿命模型**：
   - B(M1) = b_M1 / [tau * C_M1 * E1^3]
   - B(E2) = b_E2 / [tau * C_E2 * E2^5]
   - 对数变换后：ln B(M1) = ln b_M1 - ln tau - const1，ln B(E2) = ln b_E2 - ln tau - const2；
2. **正协方差机制**：
   - 由于多普勒线形拟合的能级寿命 tau 及其伴随的 ~10% SRIM 阻止本领系统误差同时出现在两个量的分母中，Var(ln tau) 构成了两者的共同正协方差项：Cov(ln B(M1), ln B(E2)) = Var(ln tau) > 0；
   - 在 31/2- 态，该共有误差引入的相关系数高达 r = +0.856；
3. **比值误差代数相消**：
   - 在跃迁强度比 R = B(M1) / B(E2) 中：ln R = ln B(M1) - ln B(E2) = ln b_M1 - ln b_E2 + const；
   - 共同寿命 tau 及其 10% 阻止本领系统误差**完全代数相消**，比值误差仅由纯分支比相对误差决定：Var(ln R) = Var(ln b_M1) + Var(ln b_E2)；
   - 实测 31/2- 态比值 R = 9.64 的真实相对不确定度仅为 5.87%，相比无相关独立正交传播假想误差（15.44%）尖锐了 2.63 倍。

### 实验结论证据门准则

- **规则一（严禁无依据独立正交传播）**：严禁对共享拟合分母（寿命、靶厚、阻止本领）的派生观测量直接应用独立方差相加公式；
- **规则二（比值测试的系统误差免疫性）**：同能级跃迁强度比天然消除了阻止本领与复杂全级联 feeding 的系统不确定性，是比绝对 B 值更灵敏、更纯粹的模型检验探针；
- **规则三（理论符合度的真实评判）**：检验理论模型与 B(M1)/B(E2) 吻合度时，必须采用扣除寿命公因子后的真实尖锐误差带（~6%），不可用假想的独立放大误差（~15%）掩盖模型偏离。

代码见 `system/scripts/day21_checkpoint141_shared_denominator_covariance_audit.py`，基准输出 `shared-denominator-covariance-scope-141.json`。
"""

p = Path("knowledge/research-notes/day21-135nd-same-input-falsification-design.md")
orig = p.read_text(encoding="utf-8")
p.write_text(orig.rstrip("\n") + "\n" + content.strip() + "\n", encoding="utf-8")
print("Appended Checkpoint 141 to design note")
