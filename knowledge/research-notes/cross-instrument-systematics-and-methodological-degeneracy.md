---
type: research-note
title: "跨大型伽马谱仪实验系统误差与方法学伪简并破除"
aliases: [cross-instrument-systematics-and-methodological-degeneracy, Spectrometer systematics Day 27]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [garg-2015-135pr-magnetic-rotation, garg-2019-135pr-polarization-erratum, roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-arxiv-full, odegard-2001-evidence-wobbling-163lu]
created_from: Day 27 spectrometer-systematics worker; cross-instrument systematics and pseudo-degeneracy modeling
tags: [spectrometer, gammasphere, euroball, agata, jurogam, polarimetry, dsam, rdds, systematic-errors, pseudo-degeneracy]
---

# 跨大型伽马谱仪实验系统误差与方法学伪简并破除

> 本页为 Codex source/claim self-audit，`review_status: unreviewed`。

## Research Trigger

高自旋核结构前沿高度依赖大型伽马探测阵列（Gammasphere, Euroball, GASP, JUROGAM, AGATA）对跃迁多极性与能级寿命的精密测定。然而，康普顿极化不对称度校准偏差、DSAM 阻止本领模型差异以及侧向未观测馈送滞后等实验系统误差，屡次造成将一种物理机制误判为完全不同机制的方法学伪简并。本研究系统量化这些系统误差并建立鉴别标准。

## Grounded Evidence

1. **Gammasphere (110 单晶 HPGe):** 双段平面极化分析本领 $Q(662\text{ keV}) \approx 0.13$，DSAM 寿命系统误差约 $10-15\%$；
2. **Euroball (Clover/Cluster):** Clover 晶体内散射极化本领 $Q(662\text{ keV}) \approx 0.22$，RDDS Köln 柱塞法精度达 $0.2\ \mu\text{m}$，系统误差 $6-10\%$；
3. **AGATA (36 段径迹探测):** 脉冲形状分析 (PSA) 多普勒自适应修正，康普顿跟踪极化本领 $Q(662\text{ keV}) \approx 0.42$，系统误差 $3-5\%$；
4. **$^{135}\text{Pr}$ 极化勘误事实:** Garg 2015 未校准 Clover 几何不对称性，导出 813 keV 跃迁 $A_P = -0.20(8)$（拟合为假纯 $M1$）；Garg 2019 引入能量依赖修正后翻转为 $A_P = +0.04(3)$（实际为混合 $M1+E2$）。

## Provisional Reasoning

系统误差在三个关键物理场景下极易诱发假相：
1. **Case 1 (大 $B(M1)/B(E2)$ 偶极带):** 磁转动剪刀机制 vs 强耦合高-$K$ 扁椭带 vs 八极 $E1$ 带。若极化仪将 $E1$（$P > 0$）误判为 $M1$（$P < 0$），将完全颠倒结构解释；
2. **Case 2 (近简并双重带):** 手征双重带 vs 形状共存两能带交叉。若两带内禀四极矩 $Q_t$ 测量误差过大（$> 25\%$），将无法区分单态势阱三轴手征与两态双阱交叉；
3. **Case 3 (衰减的 $B(E2)$ 序列):** 反磁转动（AMR） vs 侧向未观测慢馈送滞后假象。若假设“瞬发馈送”，慢衰变级联（$\tau_{\text{sf}} \approx 80\text{ fs}$）会使高自旋表观寿命偏长，导出假 $B(E2)$ 衰减。

## Assumptions

1. 极化分析本领公式遵循 Klein-Nishina 截面角分布；
2. 固体阻止本领假定以 Ziegler/SRIM 数据库为基准。

## Competing Explanations

1. 813 keV 跃迁多极性：纯 $M1$ 剪刀转动跃迁 vs 混合 $M1+E2$ 剪刀跃迁 vs 纯 $E2$ 摆动跃迁。
2. $^{110}\text{Cd}$ 高自旋 $B(E2)$ 衰减：真实反磁转动剪刀闭合 vs 未观测侧向馈送滞后引起的人为假象。

## Transfer Conditions

1. 康普顿极化测量必须采用能量依赖几何效率因子校准：$a(E_\gamma) = a_0 + a_1 E_\gamma$。
2. DSAM 寿命反演必须开展前向/后向全线形拟合，或使用 RDDS 从上方门控验证。

## Failure Conditions

1. 当极化仪校准误差 $\Delta a / a > 2\%$ 时，弱极化跃迁（$|P| < 0.2$）的宇称判据立即失效。
2. 当高自旋侧向馈送时间未知且未加限制时，禁止仅凭单一线形推断 AMR。

## Falsification or Reverse Tests

运行谱仪误差与伪简并分析模型：
```bash
python3 outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/spectrometer-systematics/spectrometer_systematics_model.py
```
验证极化分析本领曲线与阻止本领偏差矩阵。

## Open Questions

1. 在 AGATA 的全 $4\pi$ 完整安装阶段，低能段（$< 150\text{ keV}$）康普顿跟踪的真实极化本领下限为何？
2. 是否存在完全无模型依赖的直接侧向馈送时间原位测定方案？

## Human Review

本笔记为 Codex source/claim self-audit，尚未经过人工审核；保持 `review_status: unreviewed`。

## Promotion or Rejection History

- 2026-10-29：依据 Day 27 谱仪系统误差与伪简并破除研究任务创建。

## Knowledge Impact and Learning Decision

- `supports` 建立实验系统误差对理论模型判据的定量反作用框架；
- `limits` 严格限制了未校准极化仪与未门控 DSAM 数据在确立新集体模式中的证据权重。

## Review Status

本页为 Codex source/claim self-audit。所有误差分析基于实际装置公开规格与经典公式。`needs_review: true`。
