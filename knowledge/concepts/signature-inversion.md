---
type: concept
title: Signature inversion
aliases: [signature inversion, 旋称反转]
created: 2026-09-05
updated: 2026-09-05
status: ai-draft
review_status: unreviewed
tags: [signature-splitting, rotational-bands, high-spin]
---

# Signature inversion

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

在奇 A 或奇奇核转动带中，favored/unfavored signature 分支的相对能量顺序在某个自旋区间发生反转。它是能级和 signature-splitting 的观测现象，不是单一形变或组态机制的唯一指纹。

## Sources in This Batch

- [[wang-huale-2006-170re-176ir-thesis]]：`170Re` `πh11/2⊗νi13/2` 候选带的低自旋 inversion。
- [[smith-1998-rotational-bands-127-131pr]]：`Pr` 同位素 `πh11/2` 相关带和 N 依赖 systematics。

## Interpretation Boundary

残余质子-中子相互作用、非轴形变、Coriolis coupling 和组态混合都可能影响 inversion；必须结合 alignment、Routhian、带交叉和电磁跃迁证据。

## Necessary Assumptions

讨论 inversion 时必须明确 favored/unfavored signature、核素、带、spin interval、能量参考和是否存在 band crossing；不能把任意 staggering 当成 inversion。

## Discriminating Observables

signature splitting/inversion 随自旋的能量序列、alignment、Routhian、band crossing、组态系统学、混合比和寿命/电磁强度。

## Supporting Evidence

[[liu-1996-signature-inversion-a130]] demonstrates that signature inversion conclusions depend on the bandhead-spin crosswalk: revised `I0` values make inversion systematic across A≈130 chains, while unresolved Cs anchors can reverse the inferred signature order and γ interpretation.

[[wang-huale-2006-170re-176ir-thesis]] 与 [[smith-1998-rotational-bands-127-131pr]] 报告 `170Re`/Pr 相关带的 signature inversion 或其系统学。

## Counter-evidence and Competing Interpretations

非轴形变、残余 pn interaction、Coriolis coupling、组态混合和错误的 band crosswalk 都可能产生相似的能量重排；signature inversion 不是独立的形变证明。

## Our Current Position

把 signature inversion 作为可观测能级现象保留；具体机制必须由 alignment、模型比较和电磁观测量联合约束。

## Sources

- [[liu-1996-signature-inversion-a130]]
- [[wang-huale-2006-170re-176ir-thesis]]
- [[smith-1998-rotational-bands-127-131pr]]

## Human Review Triage

### P0

- 核对具体 nucleus、band、spin 区间和 favored/unfavored 定义，避免把 signature splitting 误写为 inversion。

### P1

- 比较 CSM/PRM/系统学解释及其模型依赖。

## Day 21 Checkpoint 013 证据门量化审计

依据独立审计程序 `system/scripts/day21_checkpoint013_signature_inversion_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/signature-inversion-audit-013.json`（对标 [[liu-1996-signature-inversion-a130]] 之 `LU96-D21-1`），确立旋称反转在推断阶梯上的实证判据：
1. **带头自旋指认的奇偶对调陷阱：**
   旋称量子数由 $lpha = I mod 2$ 决定。奇奇核带头自旋 $I_0$ 的 $1\hbar$ 平移（例如由 $8$ 修正至 $9$）会完全颠覆 favored（$lpha=1$）与 unfavored（$lpha=0$）的指认，将表观正常劈裂变成反转或反之。确证旋称反转必须依赖绝对自旋与多极性测量；
2. **残余质子—中子相互作用与轴对称相容性：**
   在恒定轴对称长椭形变（$\gamma = 0^\circ$）下，未配对准质子与准中子之间的短程四极与张量残余力（$\Delta E_{pn} \sim 80	ext{ keV}$）产生倾斜对齐势垒，使 unfavored 态能量低于 favored 态；当频率增大至科里奥利力压倒残余力时（$I_{	ext{inv}} \sim 12 - 16\hbar$），恢复正常科里奥利能序；
3. **证据门准则：**
   严禁仅凭低自旋旋称能量反转直接断言原子核处于负 $\gamma$ 或刚性三轴形变；确证旋称反转必须排除恒定轴对称形变下残余质子—中子相互作用的非排他竞争机制。
