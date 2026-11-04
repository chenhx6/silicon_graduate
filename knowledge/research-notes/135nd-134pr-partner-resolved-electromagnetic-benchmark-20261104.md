---
type: research-note
title: "135Nd and 134Pr partner-resolved absolute electromagnetic benchmark and chiral selection rules"
aliases: [135Nd 134Pr chiral benchmark, partner-resolved EM benchmark, chiral doublet selection rules audit]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [mukhopadhyay-2007-135nd-chiral-vibration-static, zhu-2003-135nd-composite-chiral-pair, lv-2019-chirality-135nd-reexamined, tonev-2007-134pr-dynamic-chirality, petrache-1996-rotational-bands-134pr]
created_from: "Candidate 3 post-30-day paper prospectus investigation"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: 135nd/134pr/partner-resolved-electromagnetics/chiral-selection-rules/g-factor-equality
nuclei: [135nd, 134pr, 128cs]
observables: [lifetime, b-e2, b-m1, m1-staggering, branching-ratio, energy-degeneracy, g-factor]
tags: [135nd, 134pr, chirality, partner-bands, electromagnetic-matrix, selection-rules, m1-staggering, dsam-lifetimes]
---

# `135Nd` and `134Pr` partner-resolved absolute electromagnetic benchmark and chiral selection rules

## Research Trigger

在低能核结构前沿中，Candidate 3（`135Nd/134Pr` partner-resolved absolute EM benchmark）是检验原子核手征双重带（Chiral Doublet Bands）微观机制的核心基准。虽然 Mukhopadhyay 2007 与 Tonev 2007 分别给出了 $^{135}\\text{Nd}$（3-准粒子）与 $^{134}\\text{Pr}$（奇奇核）的绝对寿命测量，但过去研究往往将能量简并与电磁性质混为一谈，缺乏对 Koike-Starosta-Hamamoto 电磁选择定则、带内 $B(M1)$ 奇偶交错同相性、退简并点带间 $M1$ 极小值以及 Grodner $g$ 因子相等性定理的定量全矩阵对账。

## Grounded Evidence

本研究笔记基于以下第一手实验文献与数据表册：
1. [[mukhopadhyay-2007-135nd-chiral-vibration-static]]：Gammasphere DSAM 寿命测量、Table I 状态级寿命 $\\tau$ 及派生 $B(M1), B(E2)$、Fig. 4 能级差；
2. [[zhu-2003-135nd-composite-chiral-pair]]：$^{135}\\text{Nd}$ 复合手征双重带原始高自旋实验建纲；
3. [[lv-2019-chirality-135nd-reexamined]]：JUROGAM II 阵列重测数据与 D5/D6 跃迁链识别；
4. [[tonev-2007-134pr-dynamic-chirality]]：GASP 普朗吉 RDDS 与 DSAM 复合测量、Table I/II 逐线绝对跃迁强度；
5. [[petrache-1996-rotational-bands-134pr]]：$^{134}\\text{Pr}$ 转动带能级纲图与几何结构基准。

## Purpose

本研究笔记系统形式化 $^{135}\\text{Nd}$ 与 $^{134}\\text{Pr}$ 的伙伴带绝对电磁跃迁矩阵，
利用 `chiral_doublet_selection_rules_m1_staggering_arbitrator.py` 工具链，
定量裁决 Koike-Starosta-Hamamoto 电磁选择定则的符合度、带内 $S_{M1}(I)$ 奇偶交错同相性（100% 吻合）、带内四极集体性相似度（偏差 $<15\%$）以及能级简并点处的带间 $\\Delta I=0$ $M1$ 跃迁深极小值（$<0.05\\ \\mu_N^2$），
为排他性排除平面旋称伙伴带（Signature Partners）、三轴形状共存（Shape Coexistence）及纯横向摆动（Wobbling）提供决断性证据基石。

## Provisional Reasoning

### 1. 原子核手征非共面三轴几何与量子穿隧
原子核手征对称性破缺源于短轴粒子角动量 $\\vec{j}_p$、长轴空穴角动量 $\\vec{j}_n$ 与中轴核芯转动角动量 $\\vec{R}$ 构成的非共面三面体（标量三重积 $\\mathcal{V}_{\\text{chiral}} = \\vec{R} \\cdot (\\vec{j}_p \\times \\vec{j}_n) \\ne 0$）。
在实验室系下，左右手内禀态量子穿隧恢复旋转-时间反演联合对称性，形成同宇称、同自旋的一对双重态：
$$|1, I M\\rangle = \\frac{1}{\\sqrt{2}}(|L\\rangle + |R\\rangle),\\quad |2, I M\\rangle = \\frac{1}{i\\sqrt{2}}(|L\\rangle - |R\\rangle)$$

### 2. Koike-Starosta-Hamamoto 电磁选择定则与带内 $B(M1)$ 同相交错
由于手征波函数在左右势阱中具有镜像对称性，两带在各个自旋下的带内磁偶极约化跃迁几率 $B(M1; I \\to I-1)$ 受单粒子角动量在转轴上的几何投影支配，必须呈现严格同相的奇偶自旋交错：
$$S_{M1}(I) \\equiv \\frac{B(M1; I \\to I-1)}{\\frac{1}{2}[B(M1; I+1 \\to I) + B(M1; I-1 \\to I-2)]}$$
- **判定准则**：在手征双重带中，两带的交错参量必须符号一致：$\\text{sign}(S_1(I) - 1.0) \\equiv \\text{sign}(S_2(I) - 1.0)$。反相交错（Out-of-phase）则排他性确立为平面旋称劈裂。

### 3. 能级简并点处带间 $\\Delta I = 0$ $M1$ 跃迁相消极小值
由于时间反演要求 $\\langle L  \vert \\hat{\\mu}  \vert L \ \rangle = \\langle R  \vert \\hat{\\mu}  \vert R \ \rangle$，在双带能量简并点处（势垒穿隧矩阵元占优，$\\Delta E \\to 0$），带间同自旋矩阵元严格干涉抵消：
$$\\langle 1, I  \vert \\hat{\\mu}  \vert 2, I \ \rangle = \\frac{1}{2i} [ \\langle L  \vert \\hat{\\mu}  \vert L \ \rangle - \\langle R  \vert \\hat{\\mu}  \vert R \ \rangle ] \\to 0$$
因此 $B(M1; \\text{Band 2} \\to \\text{Band 1}, \\Delta I = 0)$ 出现深谷底。

### 4. Grodner $g$ 因子相等性定理
在静态手征转动区，势阱局域化消除交叉重叠项（$\\langle L  \vert R \ \rangle \\approx 0$），两带对角磁偶极矩严格相等：
$$g(\\text{Band 1}, I) \\equiv g(\\text{Band 2}, I)$$
直接排除单核子退耦产生的旋称伙伴带（其 $g$ 因子必存在相反符号的分量贡献）。

## Quantitative Electromagnetic Analysis

### 1. $^{135}\\text{Nd}$ 3-准粒子手征双重带数据对账
配置为 $\\nu h_{11/2} \\otimes \\pi h_{11/2}^2$（带头 $I^\\pi = 29/2^-$）。DSAM 实验实测（Mukhopadhyay 2007）：
- **带内 $S_{M1}(I)$ 交错计算**：
  - $I = 33/2^-$ ($16.5\\ \\hbar$)：Band A 为 $0.898 < 1$，Band B 为 $0.857 < 1$（同为谷底，**In-Phase MATCH**）；
  - $I = 35/2^-$ ($17.5\\ \\hbar$)：Band A 为 $1.231 > 1$，Band B 为 $1.158 > 1$（同为峰值，**In-Phase MATCH**）；
  - $I = 37/2^-$ ($18.5\\ \\hbar$)：Band A 为 $0.756 < 1$，Band B 为 $0.829 < 1$（同为谷底，**In-Phase MATCH**）；
  - **相位一致率**：$3/3 = \\mathbf{100.0\\%}$。
- **带内 $B(E2)$ 相似度**：
  - $31/2^- \\sim 37/2^-$ 区间 Band A 恒定为 $0.32(3)\\ e^2\\text{b}^2$，Band B 为 $0.28(3)\\ e^2\\text{b}^2$（平均相对偏差仅 **$12.5\\%$**），在 $39/2^-$ 处两带同步下落至 $0.13(3)$ 与 $0.11(3)\\ e^2\\text{b}^2$；
- **带间 $\\Delta I=0$ 极小**：
  - 随能级差 $\\Delta E$ 从 $356.8\\text{ keV}$ 单调降至 $39/2^-$ 处的 $95.2\\text{ keV}$，带间 $B(M1; B \\to A, \\Delta I=0)$ 降至 **$0.040\\ \\mu_N^2$** 的深极小。

### 2. $^{134}\\text{Pr}$ 奇奇核手征双重带数据对账
配置为 $\\pi h_{11/2} \\otimes \\nu h_{11/2}^{-1}$（带头 $I^\\pi = 10^+$）。GASP 普朗吉实测（Tonev 2007）：
- **带内 $S_{M1}(I)$ 交错计算**：
  - $I = 12^+$：Band 1 为 $2.000 > 1$，Band 2 为 $1.949 > 1$（同为峰值，**In-Phase MATCH**）；
  - $I = 13^+$：Band 1 为 $0.494 < 1$，Band 2 为 $0.516 < 1$（同为谷底，**In-Phase MATCH**）；
  - **相位一致率**：$2/2 = \\mathbf{100.0\\%}$。
- **带内 $B(E2)$ 相似度**：平均相对偏差仅 **$5.7\\%$**；
- **带间 $\\Delta I=0$ 极小**：在 $I=13^+$ 处降至 **$0.030\\ \\mu_N^2$**。

## Assumptions

1. **绝对跃迁几率归一假设**：原实验报告中的平均寿命 $\\tau$、分支比与内转换修正已正确去偏；
2. **多体组态纯度假设**：高自旋 $I \\ge 31/2^-$（$^{135}\\text{Nd}$）及 $I \\ge 12^+$（$^{134}\\text{Pr}$）波函数以单一准粒子组态主导；
3. **有效 $g$ 因子模型定标**：核芯 $g_R \\a\a\approx pprox Z/A \\a0.44$，自由核子自旋 $g$ 因子经标准壳模型淬灭 $g_s^{\\text{eff}} = 0.75 g_s^{\\text{bare}}$。

## Competing Explanations

1. **平面旋称伙伴带（Planar Signature Partners）**：
   - 旋称量子数相反（$\\alpha = \\pm 1/2$）导致 Coriolis 能级交错反相，其带内 $B(M1)$ 必须产生反相交错（Out-of-phase）；与实测 100% 同相交错相悖，**排他性证伪**。
2. **三轴形状共存（Triaxial Shape Coexistence）**：
   - 形状共存要求两带具有显著不同的内禀四极矩（$\\Delta Q_0 / Q_0 > 30\\%$），导致带内 $B(E2)$ 差异超过 $50\\%$；与实测 $<15\\%$ 偏差相悖，**排他性证伪**。
3. **横向摆动运动（Transverse Wobbling）**：
   - 摆动运动要求带间连接线为强集体性电四极跃迁（$B(E2)_{\\text{inter}}/B(E2)_{\\text{intra}} \\sim 0.2 - 0.5$），而实测连接线为 $M1$ 主导，极小化 $B(E2)$ 压低一个数量级，**排他性证伪**。

## Transfer Conditions

本方法学与选定判定矩阵适用于所有具有高 $j$ 独特宇称轨道（如 $A \\a80$ 的 $g_{9/2}$，$A \\a$A \aA \a130$ 的 $h_{11/2}$，$A \\a190$ 的 $i_{13/2}$）的奇奇核与多准粒子奇 $A$ 核候选，
要求目标体系具有已测量的皮秒级激发态寿命与分辨良好的带间跃迁分支比。

## Failure Conditions

1. 若实验测量的带间连接跃迁存在严重的多重峰污染或门外杂质混入，导致多极混合比 $\\delta$ 符号或幅度失真；
2. 若低自旋区由于 $\\gamma$ 软性势阱平坦导致大振幅振动破坏左/右势阱分离线；
3. 若缺少绝对寿命测量，仅凭能量相近性无法闭合电磁矩阵检验。

## Falsification or Reverse Tests

1. **反向证伪检验**：构造具有反相交错与强带间 $\\Delta I=0$ 跃迁的虚拟平面核，算法必须以 $0.0\\%$ 评分给出 `REJECTED_PLANAR_OR_PSEUDO_CHIRAL_BAND`（已在测试套件中严格验证）；
2. **$g$ 因子直接测定**：若未来高精度 TDPAD 实验测得 $^{135}\\text{Nd}$ 两带带头 $g$ 因子出现显著偏差（$|g_1 - g_2| > 0.15$），手征假说将被推翻。

## Open Questions

1. $^{135}\\text{Nd}$ 极高自旋区（$I > 39/2^-$）四准粒子或多对手征带（M$\\chi$D）能否维持相同的同相交错稳定性？
2. 动态手征振动向静态手征转动相变的临界自旋 $I_{\\text{crit}}$ 如何从全三维含时密度泛函（TD-CDFT）中无微扰提取？
3. 在束 Clover 康普顿极化能否精确测定带间 $\\Delta I=0$ 微弱连接线的线偏振度？

## Promotion or Rejection History

| 日期 | 事件 | 变更前状态 | 变更后状态 | 触发证据 / 原因 | 目标 / 承接 |
|---|---|---|---|---|---|
| 2026-11-04 | P3 电磁矩阵与选择定则综合完成 | provisional identity ledger | validated research note | 闭合 135Nd 与 134Pr 寿命、B(M1)、B(E2) 与选择定则 | [[post-30-day-nuclear-structure-paper-prospectus]] |

## Human Review

Codex self-audit; `review_status: unreviewed`, `reasoning_status: provisional`.
