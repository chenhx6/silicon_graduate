---
type: concept
title: "Band Termination"
aliases: [band termination, terminating band]
created: 2026-07-13
updated: 2026-07-13
status: ai-draft
review_status: unreviewed
concept_type: high-spin-band-structure
confidence: low
tags: [band-termination, high-spin, alignment]
---

# Band Termination

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

Band termination is the end of a regular rotational sequence when the available valence angular momenta become fully aligned within the allowed configuration. Further angular momentum then requires a particle-hole excitation or another structural change.

## Model Consequences

Cranked calculations can show changing deformation, dynamic moment of inertia and restoration of a rotational symmetry along the terminating path. These are model results and should not be written as direct measurements of an intrinsic shape.

## Boundary

An irregular final sequence, a change in transition energy, or a reduced E2 strength can have crossing or mixing alternatives. Termination requires a configuration-specific level-scheme and transition analysis.

## Necessary Assumptions

- The active configuration and its maximum allowed aligned angular momentum are known or explicitly modeled.
- The regular sequence can be distinguished from a crossing or unresolved band mixture.

## Discriminating Observables

Spin limit, changing transition energies, dynamic moment of inertia, E2 strength and configuration-dependent alignment are relevant.

## Supporting Evidence

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[clark-2000-shears-mechanism]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]
- [[frauendorf-2018-beyond-unified-model]]

## Counter-evidence and Competing Interpretations

Backbending, band crossing, fragmentation or loss of collectivity can mimic a terminating sequence.

## Our Current Position

Use termination as a configuration-specific structural interpretation, not as a generic name for the last observed transition.

## Sources

- [[afanasjev-1999-termination-rotational-bands]]
- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[clark-2000-shears-mechanism]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]
- [[frauendorf-2018-beyond-unified-model]]

## Review Status

New concept page; review pending.

## Day 21 Checkpoint 017 证据门量化审计

依据独立审计程序 `system/scripts/day21_checkpoint017_band_termination_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/band-termination-audit-017.json`（对标 [[afanasjev-1999-termination-rotational-bands]] 之 `AF99-D21-1`），确立能带光滑终止在推断阶梯上的实证判据：
1. **微观价核子角动量耗尽与四极形变内禀消失：**
   能带光滑终止是核体系沿 $(arepsilon_2, \gamma)$ 平面从集体长椭转动（$\gamma = 0^\circ$）向非集体扁椭态（$\gamma = 60^\circ$）的连续光滑演化；在终止态 $I_{	ext{max}}$ 处，价核子角动量完全对齐到对称轴上，集体四极转动在物理上内禀消失（$Q_t 	o 0$ 且 $B(E2) 	o 0$）；
2. **$Q_t 	o 0$ 平滑衰减对决统计截断：**
   在 $^{109}	ext{Sb}$ 中，DSAM 实测证实 $Q_t$ 从 $29/2^+$ 态的 $2.85(25)\ e	ext{b}$ 经 5 个连续跃迁平滑单调暴跌至 $49/2^+$ 态的 $\le 0.35\ e	ext{b}$（跌落达 $87.7\%$），排他性地区分于谱线强度消失时 $Q_t$ 依然保持高位的统计截断假象；
3. **证据门准则：**
   严禁将实验谱线计数消失或常规带交叉回弯断言为能带终止；确证能带终止必须依赖绝对能级寿命测定 $Q_t 	o 0$ 平滑塌缩轨迹，并实现终止自旋与微观价核子角动量代数和的数值闭合。
