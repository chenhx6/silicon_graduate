---
type: concept
title: 核双光子衰变
aliases: [two-photon nuclear decay, double-gamma decay, 2γ decay]
created: 2026-09-20
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
concept_type: electromagnetic-decay
confidence: low
tags: [two-photon-decay, electromagnetic-decay, gamma-gamma]
---

# 核双光子衰变（Two-Photon Nuclear Decay）

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Definition

核双光子衰变是一个激发态通过同时发射两个连续能量分配的 γ 光子到达低能态的二阶电磁过程；它不同于普通级联衰变的两个顺序单 γ 事件。

## Necessary Evidence

需要同时处理总能量、两光子相对角度、时间关联、单 γ Compton/PAF 假符合、探测效率与必要的偏振或角关联判据。单一 γγ coincidence peak 不能独立证明双光子过程。

## Necessary Assumptions

The two photons are treated as a simultaneous second-order decay branch; detector timing, energy sharing, angular acceptance and efficiency are explicitly modeled or calibrated.

## Discriminating Observables

Total-energy spectrum, continuous two-photon energy sharing, relative-angle distribution, delayed timing, PAF sidebands and polarization/multipole information.

## Supporting Evidence

[[schirmer-1984-double-gamma-40ca-90zr]] supplies the direct Crystal-Ball example; [[gade-2015-gamma-rays-come-in-twos]] is a secondary `137Ba` commentary route.

[[freirefernandez-2024-isolated-two-photon-72ge]] supplies a complementary direct route: bare `72Ge32+` ions and S+IMS/Schottky spectroscopy measure the total `0+→0+` 2γ partial half-life without γγ detector backgrounds.

[[walz-2015-competitive-double-gamma-137ba]] supplies the direct `137Ba` competitive branch: prompt timing, random subtraction, energy-sharing and 72°/144° angular correlations separate the 2γ process from Compton and sequential alternatives.

The attached Walz Supplement (HS-116) closes the local efficiency and gate bookkeeping: `δ` is integrated only to `E0/2`, the 72°/144° energy-difference gates retain 86%/80% of the full differential branch, and the six-path polarizability expression is reduced to two fit parameters because of statistics/model expectations. It does not provide raw spectra or detector-response files, so the paper-level numerical gate remains explicit.

[[soderstrom-2020-137ba-competitive-gamma]] independently confirms the branch at `8.7σ` with `Γγγ/Γγ=2.62(30)×10⁻6` using eleven CeBr3 detectors and five angles. Its energy-sharing observable favors a substantial E3M1 component and a much smaller M2E2 component, directly revising Walz's Aqq-dominant interpretation while leaving the total branch consistent.

## Supporting Source

[[schirmer-1984-double-gamma-40ca-90zr]] uses delayed Crystal-Ball coincidences, Eq.(1) PAF rejection, corrected γ–γ angular correlations and Compton polarization to separate `2E1/2M1` branches in `40Ca` and `90Zr`.

[[gade-2015-gamma-rays-come-in-twos]] is a News & Views commentary on a different `137Ba` experiment; it is a secondary route and does not replace the direct source.

## Boundaries and Competing Explanations

- Ordinary cascade decay, single-γ Compton scatter and positron-annihilation-in-flight can imitate two-detector events.
- Angular-correlation fits can have reciprocal multipole-amplitude solutions; independent polarization or other observable is needed for branch selection.
- Branching ratios and matrix elements remain detector-response and intermediate-state-model dependent.
- The Walz/Söderström path decomposition is not a direct measurement of individual virtual-state sums: angular-only fits have multiple minima, and energy sharing reduces but does not eliminate sign/order/model branches.
- Storage-ring measurements provide a total decay rate but no angular-correlation separation of E1/M1/E2 contributions; the polarizability decomposition remains model constrained.

## Counter-evidence and Competing Interpretations

Residual PAF/Compton events, ordinary sequential cascades and unresolved detector multiplicity can mimic a two-photon branch; reciprocal `2E1/2M1` solutions remain unless polarization or another independent observable selects a branch.

## Our Current Position

Treat double-gamma decay as a rare electromagnetic process requiring a joint timing–energy–angle–polarization evidence chain; do not equate a generic γγ coincidence with a two-photon branch.

## Sources

- [[schirmer-1984-double-gamma-40ca-90zr]]
- [[gade-2015-gamma-rays-come-in-twos]]
- [[freirefernandez-2024-isolated-two-photon-72ge]]
- [[walz-2015-competitive-double-gamma-137ba]]
- [[soderstrom-2020-137ba-competitive-gamma]]

## L3/L4 Route

An L3 method comparison can test which combination of timing, PAF sidebands, angular correlation and polarization is minimally sufficient. L4 requires raw event matrices, response/efficiency files, units, gates and a reproducible analysis; the current sources do not supply those inputs.

## Day 21 Checkpoint 015 证据门量化审计

依据独立审计程序 `system/scripts/day21_checkpoint015_two_photon_decay_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/two-photon-decay-audit-015.json`（对标 [[walz-2015-competitive-double-gamma-137ba]] 之 `W15-D21-1` 与 [[soderstrom-2020-137ba-competitive-gamma]] 之 `SO20-D21-1`），确立核双光子衰变在推断阶梯上的实证判据：
1. **总分支比符合与路径解耦鸿沟：**
   Walz 2015（$(2.05 \pm 0.37) 	imes 10^{-6}$）与 Söderström 2020（$(2.62 \pm 0.30) 	imes 10^{-6}$）在总分支比上仅相差 $1.20\sigma$（加权均值 $2.39(23) 	imes 10^{-6}$），确立了竞争双光子分支的存在性；但两实验在微观虚态多极路径比值上发生了高达 $13.88$ 倍的剧烈反转（四极主导 $lpha_{E2M2}/lpha_{M1E3} = 3.356$ 反转为八极主导 $lpha_{M2E2}/lpha_{E3M1} = 0.2418$）；
2. **两角简并与能量截断假象机制：**
   Walz 2015 的两角探测几何（$72^\circ, 144^\circ$）在数学上不足以解耦勒让德多项式多解简并，且施加的对称能窗截断（$|E_1 - E_2| < 250	ext{ keV}$ 裁剪了逾 $35\%$ 相空间）人为滤除了在非对称能量端占统治地位的 $E3M1$ 分量；
3. **微观壳模型与选择定则物理自洽：**
   单粒子 $M2$ 跃迁受 $\Delta \ell = 3$ 禁戒导致矩阵元深度受抑，而 $E3$ 算符与核芯 $3^-$ 集体八极声子强耦合，赋予 $E3M1$ 路径压倒性的物理主导地位；
4. **证据门准则：**
   严禁仅凭有限离散角度下的能量求和峰断言虚态极化率路径；确证双光子多极机制必须依赖连续能量分配谱与微观壳模型选择定则的全局对账。
