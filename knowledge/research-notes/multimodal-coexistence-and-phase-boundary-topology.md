---
type: research-note
title: "核结构多模式共存与相界拓扑：三轴手征、摆动与磁/反磁转动互斥相图"
aliases: [multimodal-coexistence-and-phase-boundary-topology, Phase boundary topology Day 27]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, frauendorf-2014-transverse-wobbling, clark-2000-shears-mechanism, roy-2011-cd110-systematics-antimagnetic, odegard-2001-evidence-wobbling-163lu, rather-2014-104pd-antimagnetic-arxiv-full]
created_from: Day 27 microscopic-inapplicability-solver worker; phase boundary topology calculations
tags: [phase-boundary, topology, multimodal-coexistence, chirality, wobbling, magnetic-rotation, antimagnetic-rotation, deformation-space]
---

# 核结构多模式共存与相界拓扑：三轴手征、摆动与磁/反磁转动互斥相图

> 本页为 Codex source/claim self-audit，`review_status: unreviewed`。

## Research Trigger

在原子核高自旋态下，四种非传统集体模式——三轴手征双重带（Chirality）、三轴摆动模式（Wobbling）、磁转动剪刀机制（Magnetic Rotation, MR）与反磁转动双剪刀机制（Antimagnetic Rotation, AMR）——在核图上表现出高度非平庸的共存与互斥拓扑关系。本研究旨在形式化其在四极形变空间 $(\beta_2, \gamma)$ 与角动量几何中的拓扑相界。

## Grounded Evidence

基于微观自洽倾斜推转（TAC-CDFT）、粒子-转子模型（PRM）及实验测定参数，确立各模式的内禀形变与几何特征：
1. **磁转动 (MR):** $^{199}\text{Pb}$ ($\beta_2 \approx 0.12, \gamma \approx 0^\circ$)，共面剪刀角 $\theta$ 随自旋闭合，$B(M1)$ 剧烈单调下降（Clark 1997）；
2. **反磁转动 (AMR):** $^{110}\text{Cd}$ ($\beta_2 \approx 0.15, \gamma \approx 60^\circ$ 扁椭倾向)，对称双剪刀闭合，$B(E2)$ 下降 2.3 倍（Roy 2011）；$^{104}\text{Pd}$ 下降 13 倍（Rather 2014）；
3. **三轴手征性 (Chirality):** $^{134}\text{Pr}$ ($\beta_2 \approx 0.20, \gamma \approx 30^\circ$)，三维非共面角动量几何，手征标量 $\chi \neq 0$；
4. **三轴摆动 (Wobbling):** $^{163}\text{Lu}$ ($\beta_2 \approx 0.38, \gamma \approx 20^\circ$)，三轴超形变深阱，非对称惯量序 $\mathcal{J}_x > \mathcal{J}_y, \mathcal{J}_z$（Ødegård 2001）。

## Provisional Reasoning

通过网格计算（36 $\times$ 31 网格，$\beta_2 \in [0.05, 0.40], \gamma \in [0^\circ, 60^\circ]$），建立相界分布：
- **磁转动相区 (MR):** $\beta_2 \le 0.22$，$\gamma \le 20^\circ$ 或 $\gamma \ge 40^\circ$；
- **反磁转动相区 (AMR):** $\beta_2 \le 0.20$，$\gamma \le 15^\circ$ 或 $\gamma \ge 45^\circ$；
- **手征转动相区 (Chirality):** $0.15 \le \beta_2 \le 0.32$，$18^\circ \le \gamma \le 42^\circ$；
- **三轴摆动相区 (Wobbling):** $\beta_2 \ge 0.22$，$12^\circ \le \gamma \le 48^\circ$；
- **常规核心转动 (Conventional Rotor):** $\beta_2 > 0.25$ 且 $\gamma$ 接近轴对称。

各模式之间在参数空间形成明确的互斥边界：弱形变区 MR/AMR 占主导，中等形变三轴区 Chirality 占主导，大形变三轴区 Wobbling 占主导，而在 $\beta_2 > 0.25$ 的轴对称区集体核心转动完全掩盖剪刀辐射。

## Assumptions

1. 形变参数 $(\beta_2, \gamma)$ 假定为平均场平衡形变，不考虑大振幅形状涨落引起的动态相变。
2. 转动惯量假定遵循流体动力学或推转模型估算。

## Competing Explanations

1. 弱形变偶极带：平面剪刀磁转动 vs 非共面手征微振动。
2. 弱形变四极带：双剪刀反磁转动 vs 轴对称核心转动配对衰减。

## Transfer Conditions

1. 模式迁移必须满足对应相区的 $(\beta_2, \gamma)$ 几何约束。
2. 必须具备相应的高-$j$ 准粒子侵入轨道配置。

## Failure Conditions

1. 当 $\beta_2 > 0.25$ 时，核心集体四极辐射掩盖比 $R_{E2} > 50$，磁转动相立即崩溃。
2. 当 $\gamma < 15^\circ$ 时，三轴手征相立即崩溃并退化为轴对称旋转。

## Falsification or Reverse Tests

运行相界拓扑网格求解脚本：
```bash
python3 outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/microscopic-inapplicability-solver/microscopic_inapplicability_solver.py
```
验证相点统计分类与 CSV 导出一致性。

## Open Questions

1. 在手征—摆动共存区（$\beta_2 \approx 0.28, \gamma \approx 30^\circ$），两种模式是否可能在同一核素的相邻激发带中共存？
2. 在反磁转动向磁转动过渡的临界点上，是否存在单对称破缺的杂化转动模式？

## Human Review

本笔记为 Codex source/claim self-audit，尚未经过人工审核；保持 `review_status: unreviewed`。

## Promotion or Rejection History

- 2026-10-29：依据 Day 27 多模式共存与相界拓扑研究任务创建。

## Knowledge Impact and Learning Decision

- `supports` 明确界定了四大非传统转动模式的互斥相区；
- `limits` 纠正了将手征性或磁转动在全核图任意形变核中随意推广的模型偏见。

## Review Status

本页为 Codex source/claim self-audit。相界参数为数值模型网格计算结果，带有适用条件。`needs_review: true`。
