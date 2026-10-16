---
type: method
title: 两点角关联比
aliases: [two-point angular-correlation ratio, angular-correlation ratio, Rac, R_ac]
created: 2026-07-01
updated: 2026-10-17
status: active
review_status: unreviewed
method_type: gamma-ray-angular-correlation
tags: [multipolarity, gamma-spectroscopy, angular-correlation]
---

# 两点角关联比（`R_ac`）

## Purpose

将前后角探测器与约 90° 探测器的符合强度归一化比较，用有限角度统计区分 stretched dipole 和 quadrupole 特征。

## Inputs and Assumptions

探测器角度分组、效率校正、同一 gating 条件、已知跃迁标定以及足够的核取向。

## Procedure

建立 `Eγ(forward/backward)-Eγ(any)` 与 `Eγ(~90°)-Eγ(any)` 非对称矩阵，在相同 gate 下取目标峰强度比并用已知多极性跃迁标定。

### 135Pr原式与门条件边界

[[lv-2022-evidence-against-wobbling-135pr]] L22-17的SI Eq1具体使用target在157.6°+133.6°与75.5°+104.5°角组，另轴为all detectors，放置相同energy gates。它没有交换target/gate的角组，不能与[[dco-ratio]]的KF89公式共用一个未标记的R。

历史Evolution Log中“不依赖gate多极性”是采用all-angle gates的实验设计目标，不是任意finite acceptance、cuts、feeding和self-exclusion下的严格joint-response定理。[[zheng-2002-ado-coincidence-angular-anisotropy]] Z02-6/9与[[angular-distribution]]及[[angular-correlation]]说明single-gamma效率并不认证gamma-gamma response；实际迁移仍须matched-gate controls。

[[135pr-mixing-branch-input-contract]]保存747/813的Rac/P/Ap和calibration采用链。mixed line的.37/.48与本文pure stretched dipole≈.8不同，不能仅凭经验阈值替换成某个pure multipole或唯一定delta。

## What It Can Establish

在特定阵列中支持主要 dipole 或 quadrupole 性质，并据连接关系约束新能级的相对自旋宇称。

## What It Cannot Establish Alone

不能在弱统计下唯一确定 mixing ratio，也不能由多极性本身证明 wobbling、手征几何或某一组态。

## Conventions and Systematics

经验数值高度依赖几何：

- JUROGAM II `135Nd/137Nd`：dipole≈0.8，quadrupole≈1.4；
- GALILEO `131Ba`：dipole≈0.77，quadrupole≈1.54；
- AFRODITE `133Ce`：dipole≈0.74，quadrupole≈1.27；
- Gammasphere `133Ce`：文中采用 quadrupole>1.0、dipole<0.8 的经验区分。

这些阈值不得跨实验机械复用。

## Examples

- [[petrache-2020-137nd-multiple-chiral-bands]] 用 `R_ac` 约束新 D3、D6 的连接跃迁；
- [[ding-2021-131ba-133ce-signature-splitting]] 在两套不同阵列中分别标定 band 2 跃迁。
- [[guo-2022-low-spin-wobbling-187au]] 以 `154°/90°` gated intensities 构造 `R_ac`，并与 clover linear polarization 联合选择 376/462 keV links 的 mixing-ratio branch。
- [[lv-2021-tilted-precession-135nd]] 以 133.6°+157.6° 对 75.5°+104.5°谱、相同 all-angle gates 构造 `R_ac`，并用它补充统计不足以获得 `R_DCO` 的弱 transitions。

## Sources

- [[lv-2022-evidence-against-wobbling-135pr]] L22-16/17/18/19：135Pr原几何、A/P、宽度与shared-data边界。

- [[ayangeakaa-2016-133ce-in-beam]]
- [[petrache-2020-137nd-multiple-chiral-bands]]
- [[ding-2021-131ba-133ce-signature-splitting]]
- [[guo-2022-low-spin-wobbling-187au]]
- [[lv-2021-tilted-precession-135nd]]

## Evolution Log

- 2026-07-01（3 sources）：从 DCO 页面中分离出不依赖 gate 多极性的 `R_ac` 方法。
- 2026-07-04：加入 HIRFL `154°/90°` 几何和与 polarization 联合选解的案例。
- 2026-07-04：加入 Lv 2021 JUROGAM II `135Nd` geometry 与弱线用途。
