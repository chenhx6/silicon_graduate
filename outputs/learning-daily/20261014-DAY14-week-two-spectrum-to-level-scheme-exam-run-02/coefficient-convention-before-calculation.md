# 符号层级练习：计算前冻结预测

冻结时间：2026-10-15T04:56:44.512525+08:00。本项明确受 checkpoint007、已有 Z83-1/Eq1–2 以及本轮 source-page 与 p389 复核 priming；不是新的盲来源前考试，不修改正式21/24。

1. 未归一 β0/β2/β4 随整体计数规模改变；Aexp=βk/β0，α=Aexp/Amax，后两者不是同一个无量纲数。
2. fixed spin、pure E2、point response 条件下，上批 c2>0/c4<0；Aexp 的 Cov 应为 DΣαD，相关系数符号随 c2c4<0 翻转。正确变换模型和 Cov 后，联合 Mahalanobis 距离应保持不变。
3. 原表两个errors不足提供真实ρ；只选择一个ρ控制说明变换，不能还原 source joint fit。计算出的 Aexp 也只是条件转换，不是新实测表列。
4. β0有误差时 ratio Jacobian 需要 β0 cross terms；若 Amax 的δ也不固定，需共同 nuisance/cross covariance，不能仅乘两个固定数就声称完整误差。Detector acceptance、conditional gate和nuclear alignment分别建模。
5. 两种把数值代入W的表达都可能保持归一与非负，故这两个检查本身不能验证变量语义；必须回源定义。

下一执行：核原Eq1–2、保留原observable mixed-EOL与审核metadata，写一张变量层级表和可复算conditional transformation。不新开source、不给Day15信用。
