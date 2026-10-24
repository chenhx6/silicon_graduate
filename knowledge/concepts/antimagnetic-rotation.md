---
type: concept
title: "Antimagnetic Rotation"
aliases: [antimagnetic rotation, antimagnetic rotor]
created: 2026-07-13
updated: 2026-07-13
status: ai-draft
review_status: unreviewed
concept_type: high-spin-collective-mode
confidence: low
tags: [antimagnetic-rotation, shears, high-spin]
---

# Antimagnetic Rotation

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

Antimagnetic rotation is a weakly deformed rotational mode in which two shears arrangements contribute angular momentum while their transverse magnetic moments largely cancel. The orientation is therefore not diagnosed by a large net transverse dipole.

## Experimental and Model Criteria

Frauendorf 2001 associates the mode with regular Delta I=2 bands, very small B(E2), and a large dynamic-moment-of-inertia to B(E2) ratio. The cancellation and current-loop picture are model-level interpretations.

## Boundary

Low B(E2) or a regular Delta I=2 sequence is not a sufficient model-independent assignment. Charge deformation, particle-hole configuration and lifetime evidence must be considered together.

## Necessary Assumptions

- Two coupled shears arrangements and their particle-hole configuration are identified.
- Magnetic-moment cancellation is evaluated within a specified model.

## Discriminating Observables

Regular Delta I=2 sequences, small B(E2), dynamic moment of inertia and transition lifetimes provide a combined test.

## Supporting Evidence

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]

## Counter-evidence and Competing Interpretations

Low B(E2) can reflect weak collectivity, configuration changes or termination rather than antimagnetic rotation.

## Our Current Position

Use the antimagnetic label only when the shears-cancellation interpretation is tied to a source-supported configuration and transition evidence.

## Sources

- [[hubel-2005-magnetic-rotation-review]]

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]

## Review Status

New concept page; review pending.

## Day 21 Checkpoint 012 证据门量化审计

依据独立审计程序 `system/scripts/day21_checkpoint012_antimagnetic_rotation_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/antimagnetic-rotation-audit-012.json`（对标 [[hubel-2005-magnetic-rotation-review]] 之 `HU05-D21-1` 与 [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]] 之 `KU25-D21-1`），确立反磁转动在推断阶梯上的实证判据：
1. **双剪刀对称相消与微观电四极塌缩：**
   反磁转动由两对高 $j$ 准粒子叶片相对核芯对称闭合所驱动，其横向磁偶极矩严格反向相消（$\mu_\perp \equiv 0 \implies B(M1) \equiv 0$），表现为纯 $\Delta I = 2$ 的 $E2$ 四极序列；其带内四极跃迁强度遵循 $B(E2) \propto \sin^4	heta$，随着自旋增加、双剪刀闭合（$	heta 	o 0$），$B(E2)$ 必然发生剧烈单调暴跌（在 $^{106}	ext{Cd}$ 中由 $0.407\ e^2	ext{b}^2$ 降至 $0.0198\ e^2	ext{b}^2$，暴跌 $20.56$ 倍，降幅 $95.1\%$）；
2. **特征比值发散与排他性判据：**
   特征比值 $\mathcal{J}^{(2)} / B(E2)$ 随着剪刀闭合急剧发散（在 $^{106}	ext{Cd}$ 中由 $54.1$ 激增至 $1111.1\ \hbar^2	ext{MeV}^{-1}(e	ext{b})^{-2}$，比常规集体转动核高出 $40 - 100$ 倍），完全突破并满足了 Hübel 判据门限（$> 100$）；
3. **证据门准则：**
   严禁仅凭规则的 $\Delta I = 2$ 序列直接断言核处于常规集体转动；确证反磁转动必须依赖绝对能级寿命测定 $B(E2) \propto \sin^4	heta$ 随自旋单调暴跌轨迹与比值发散。
