---
type: learning-audit
graph-excluded: true
created: 2026-10-07
updated: 2026-10-07
---

# DAY8 来源前 recall 原始记录

- session_id: `01a111fb-370d-7ed1-afe9-881ccc47caf4`
- captured_at_utc: `2026-10-06 16:15:17 UTC`
- recall_kind: prompt-primed recall；尚未读取 DAY7 正文与两篇 Day8 source 页/原文；用户 prompt 已提供合成题和部分选择定则
- 这份原答在来源核对前保存在当前工具上下文中；通过写前 boundary/preflight 后原样持久化。后续差异单列，保留原答。

## 原答

实光子多极 rank L≥1；|Ji−Jf|≤L≤Ji+Jf。电多极 πiπf=(−1)^L；磁多极 πiπf=(−1)^(L+1)。E1：宇称改变，常写 ΔJ=0,±1，仍需三角规则，0→0 不能单光子。M1：宇称保持，同样 rank1 三角；E2：宇称保持，常写 |ΔJ|≤2，但须 Ji+Jf≥2。0→0 的 E0 不能发射单个 γ，可有内转换/对产生，不能当成 E2 候选。forbidden 是指定过程在给定守恒/选择定则下振幅为零；hindered 是选择定则允许但矩阵元/速率相对适当参照受抑，需声明参照与额外近似（如 K）。3/2+→1/2− 的 L=1,2 给 E1/M2；2+→2+ 的 L=1..4 给 M1/E2/M3/E4；3+→1+ 的 L=2..4 给 E2/M3/E4。混合比暂记高阶/低阶辐射振幅比，但不凭记忆固定各文献的算符相位或 bra-ket 顺序。寿命与分支只给速率及强度绝对值，不给混合比相对相位；角度/偏振结果须有 alignment、response 与 convention。

## 来源后核对

| 原答项 | 来源后核对与差异 | Locator |
|---|---|---|
| E1/M1/E2 与 triangle/parity | 一般规则正确；E2 必须有 `Ji+Jf≥2`，不能把口诀简化为只排除 0→0。额外负例 `1/2+→1/2+`、`0+→1+` 都只允许 M1 单 γ | Rose–Brink printed p.320 / PDF p.15, Eq.3.41 note(ii) |
| 三条题设 gamma 候选 | 按全部整数 rank 重新枚举得到 E1/M2；M1/E2/M3/E4；E2/M3/E4，与原答一致。独立运行记录为 synthetic-multipoles.json，无实验数据 | Rose–Brink RB67-5；本 run synthetic-multipoles.json |
| 0→0 E0 通道 | 正确区分非 γ 过程；原答漏写 2+→2+ 也允许 E0 转换。另两例指定跃迁无 E0，仍须考虑初态其它衰变分支 | LKH82 printed p.123 / PDF p.5, Eq.2.12；p.169 / PDF p.51, Eq.4.1 |
| forbidden / hindered | 作为一般背景的区分保留；LKH82 p.120 的模型禁止不等于普遍 angular-momentum/parity 禁止，不能把所有高阶候选自动叫受抑 | Rose–Brink RB67-5；LKH82 printed p.120 / PDF p.2 的模型讨论 |
| δ 暂记高/低阶辐射振幅比，未固定相位 | 需补齐归一化和参考成分：RB Eq.3.39 含 √(2L+1) 且 initial bra；KS Eq.2.5 含 qγ、BM 核算符且 final bra。positive-root 系数并不消除负 δ；级联第一/第二 γ 与 absorption 不能共用一个 sign map | Rose–Brink printed p.319 / PDF p.14, Eq.3.39；LKH82 printed pp.121–122 / PDF pp.3–4, Eqs.2.5,2.9–2.11 与页末关系 |
| τ 和 branch 不给 δ sign | 原答正确；寿命是率约束，需完整分支和非 γ 通道，ICC/E0 比也只有 δ² | Rose–Brink printed p.318 / PDF p.13, Eq.3.29；LKH82 printed p.169 / PDF p.51, Eq.4.1 |

新增认识：single-gamma 的 angular rank K 受 `K≤2Ji` 限制，和 photon rank L 不同；初末态宇称确定、未测 γ 偏振时，即使初态 polarized 也不出现 odd K。这些在初始原答中未写出，已据 RB67-4/7 写回知识页。Day7 的预习没有被继承为本次完成证据。
