---
type: method
title: Recoil-distance Doppler-shift and differential decay-curve method
aliases: [RDDS, recoil-distance Doppler-shift, coincidence plunger, DDCM, differential decay curve method, RDDM]
created: 2026-08-11
updated: 2026-08-11
status: ai-draft
review_status: unreviewed
method_type: nuclear-lifetime-coincidence-plunger
tags: [lifetime, plunger, doppler-shift, ddcm, feeding, stopping]
---

# Recoil-distance Doppler-shift / DDCM

## Purpose

RDDS 通过改变 target-stopper distance，比较核在飞行中发射的 shifted γ component 与停止后发射的 unshifted component，提取 excited-state lifetime。Coincidence DDCM 用 feeding-transition gates 隔离 decay curves，并以逐 distance 的 `τ(x)` constancy 检查系统误差。

## Inputs and Assumptions

- calibrated target-stopper distances、recoil velocity 与 detector angles；
- shifted/unshifted peak components and efficiency normalization；
- direct or indirect feeding transition 可分辨并适合作 gate；
- contaminant、unobserved feeding、deorientation、finite stopping and stopping powers 被校正或进入 uncertainty；
- branching/mixing information 足以把 lifetime 转为 `B(Eλ)`/`Q_t`。

## Core Coincidence-DDCM Chain

对单一 direct feeder，Klemme 1999 的 Eq. (3) 可写为：

`τ(x) = I_su^BA(x) / [dI_ss^BA(x)/dx] × 1/v`，

其中 `I_su^BA` 是 feeding transition 的 shifted component 与 depopulating transition 的 unshifted component 的 coincidence intensity，`I_ss^BA` 为 shifted-shifted coincidence intensity，`v` 是 recoil velocity。多 feeder 情形需按 coincidence intensity normalization 扣除 direct-feeding contribution（source Eqs. 1-2）。

每个 distance 可独立给出 `τ(x)`。在敏感 distance range 内，理想结果应近似常数；明显 distance dependence 是 contaminant、feeding 或 peak-separation 系统误差的诊断，而不是应被平均掩盖的散点。

## Coincidence Advantage

在 interest level 上方的 feeder gate 可以显著减少 unobserved feeding 和 low-spin deorientation 对 lifetime 的影响。不同 rings、direct/indirect gates 给出多个相对独立 lifetime estimates，可检查 contaminant sensitivity。

## Short-Lifetime Boundary

当 lifetime 与 stopper 中 slowing time 可比时，停止过程内发射产生额外 line-shape component；纯 shifted/unshifted RDDS 近似不再充分。Klemme 1999 对 Au 中约 `1.1 ps` slowing time 使用 DSAM-like correction，并因 stopping-power ambiguity 给 adopted lifetime asymmetric errors。高统计和小 statistical error 不会消除这项系统边界。

## What It Can Establish

- source-specific level lifetimes；
- 联合 branching/mixing information 后的 `B(E2)`, `B(M1)` 与 `Q_t`；
- distance/gate/ring consistency and feeding-systematic diagnostics；
- 同实验多带/多核的相对 lifetime/collectivity comparison。

## What It Cannot Establish Alone

- 不能单靠 lifetime 决定 γ-soft versus rigid-triaxial shape、microscopic configuration 或 nuclear chirality；
- 不能在缺少 band crosswalk 时把一个早期 level lifetime转移到后来同核素的 band label；
- 不能忽略 branching ratios、mixing ratios、side feeding、finite stopping 或 deorientation 直接把 `τ` 当成 intrinsic quadrupole moment；
- 不同 stopping materials/parametrizations 与 plunger geometries 的 correction 不能跨实验机械复用。

## Inverse-Kinematics Degrader Variant

Suzuki 2008 demonstrates an RDDS variant in which inverse-kinematics recoils are slowed in a degrader rather than stopped. Direct-feeder DDCM uses shifted feeding and unshifted depopulating intensity divided by the shifted-component change between neighboring distances. When the direct feeder is contaminated, an upper transition can gate the cascade and a measured intensity ratio corrects the unwanted contribution. This extension improves short-lifetime access but preserves three boundaries: foil transit/stopping effects must remain small relative to the lifetime, velocity is different before and after the degrader, and indirect-gate lifetimes carry the correction's systematic dependence.

The method yields source-specific lifetimes. Converting them to `B(M1)` or `B(E2)` still requires branching and multipole-mixing information; Suzuki 2008 assumes pure M1 for the dipole branches. One-band lifetimes cannot establish electromagnetic equality of a proposed doublet.

## Source-Level Examples

- [[klemme-1999-lifetimes-134nd-neighbors]]：GASP-II、22 distances、direct/indirect feeder DDCM、constant-`τ` diagnostic 与 `<2 ps` finite-stopping correction。
- [[singh-2016-lifetime-131ce-133pr]]：`131Ce` plunger+DSAM 与 `133Pr` plunger；后者展示 singles-only statistics、long side feeding and pre-crossing validity boundaries。
- [[radeck-2012-deorientation-lifetime-98ru-rdds]]：强调 RDDS 语境下的 distance-dependent deorientation/angular-correlation correction。

## Sources

- [[klemme-1999-lifetimes-134nd-neighbors]]
- [[suzuki-2008-lifetimes-103rh-104rh]]
- [[singh-2016-lifetime-131ce-133pr]]
- [[radeck-2012-deorientation-lifetime-98ru-rdds]]

## Related Methods

[[doppler-shift-attenuation-method]]、[[doppler-correction]]、[[angular-correlation]]、[[transition-quadrupole-moment]]。

## Evolution Log

- 2026-08-11: added Suzuki 2008 inverse-kinematics degrader DDCM, indirect-gate correction and one-band evidence boundary.
- 2026-08-11：由 Klemme 1999 建立 coincidence-DDCM equation/diagnostic 与 finite-stopping boundary，并接入 Singh 2016/Radeck 2012 作为方法关系。


## Day18内无学分Day19预习：分量条件与缺失校准

[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-P19-1–10新完整原读十页/13图3表，旧人审prefix/flags保护。stopper取向冻结的US与按lifetime平均的SH需不同G；90°缺eff由最短距离理论角关联补、两步τ/G迭代与same-data校正后平坦性都不认证完整独立Σ。实际distanceproducer未得，Eq9的d−d0/正8与d3、Eq2后A0=0的literal域保，不改raw/重报τ。新canonical [[lifetime-method-selection-response-contract]]给条件核和actualinput优先级；后续Nolan定向段已补方法选择表与最小校准清单；Nolan非本次完整88页重读、现代fast-timing/TDPAD primary仍缺，正式19留新session。

## 四类时间测量方法选择矩阵（checkpoint060）

在 [[lifetime-method-selection-response-contract]] 中，DSAM（$10\text{ fs}-2\text{ ps}$）、RDDS（$1\text{ ps}-1\text{ ns}$）、Fast Timing MSCD（$5\text{ ps}-50\text{ ns}$）与 TDPAD（$5\text{ ns}-10\ \mu\text{s}$）被整合为完整的实验方法选择矩阵。RDDS 以真空中反冲速度 $v_0$ 与微米飞行距离为时钟，其主导系统误差为距离绝对零点与飞行中时间退取向 $G_k(t)$；在皮秒至纳秒窗口内与现代 [[regis-2011-fast-timing-labr3]] 快速定时形成关键交叉验证。详见新 [timing-method-selection-result-060](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/timing-method-selection-result-060.json)。
