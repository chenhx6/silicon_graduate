---
type: concept
title: 潮汐波转动
aliases: [tidal wave, tidal-wave rotation]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
concept_type: collective-rotation
confidence: low
tags: [high-spin, collective-motion, vibration, rotating-mean-field]
---

# 潮汐波转动（Tidal Wave）

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

Tidal-wave rotation is a rotating-frame description of weakly deformed yrast vibrational states in which angular momentum grows mainly through increasing collective deformation amplitude while rotational frequency remains near a vibrational frequency.

## Necessary Assumptions

The yrast sequence remains coherent and sufficiently weakly damped; deformation coordinates can be represented by a slowly varying rotating-frame mean field or collective Hamiltonian.

## Discriminating Observables

Moment of inertia versus spin, near-constant rotational frequency, `B(E2)` growth and the ratio `B(E2)/J` relative to harmonic/free-boson and interacting-boson limits.

## Supporting Evidence

[[frauendorf-2018-beyond-unified-model]] discusses Eqs.155–156 and `102Pd/110Cd` examples; the figures are review-level routes to the cited original calculations and data.

## Counter-evidence and Competing Interpretations

Band crossings, aligned quasiparticles, anharmonic vibrations and ordinary collective rotation can produce similar moment-of-inertia trends. A tidal-wave label is not a direct deformation measurement.

## Our Current Position

Use tidal-wave language as a rotating-frame collective interpretation, with `B(E2)`, frequency and configuration evidence kept separate.

## Sources

- [[frauendorf-2015-low-energy-quadrupole-mode]]
- [[frauendorf-2018-beyond-unified-model]]

## Day 21 Checkpoint 014 证据门量化审计

依据独立审计程序 `system/scripts/day21_checkpoint014_tidal_wave_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/tidal-wave-audit-014.json`（对标 [[frauendorf-2015-low-energy-quadrupole-mode]] 之 `FR15-D21-1`），确立四极潮汐波在推断阶梯上的实证判据：
1. **转动频率迟滞与非刚性转动本质：**
   在弱形变 $\gamma$-软核（如 $^{102}	ext{Pd}$）中，转动频率 $\hbar\omega = \Delta E / 2$ 随自旋增长极其迟缓（在 $^{102}	ext{Pd}$ 中自旋由 $2^+$ 升至 $10^+$，频率仅由 $278.2	ext{ keV}$ 升至 $490.0	ext{ keV}$，比值为 $1.76$，远低于刚性转子的 $5.0$），排除了常规刚性集体转动；
2. **$B(E2)$ 离心拉伸与声子退相干：**
   实测带内 $B(E2)$ 随自旋发生大幅激增（由 $32	ext{ W.u.}$ 扩张至 $105	ext{ W.u.}$，增长 $3.28$ 倍），显著打破了刚性转子 Clebsch-Gordan 几何因子的饱和极限（预测饱和上限仅 $1.69$ 倍），同时低于简谐 5 声子自由玻色子预测（$5.0$ 倍），与四极振幅随自旋拉伸的潮汐波物理图像（$B(E2) \propto eta_2^2(I) \propto I$）完全符合；
3. **证据门准则：**
   严禁仅凭表观等间距能级或 $R_{4/2} pprox 2.0 - 2.4$ 直接断言原子核处于简谐多声子振动态或刚性形变转动；确证四极潮汐波集体机制必须依赖绝对能级寿命测量提取 $B(E2) \propto I$ 随自旋线性或超线性增长轨迹，并联合转动频率迟滞排除回弯与静态转子假象。
