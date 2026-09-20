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
