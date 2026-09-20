---
type: model
title: 倾斜轴推转
aliases: [tilted axis cranking, TAC, tilted-axis cranking]
created: 2026-07-01
updated: 2026-07-13
status: active
review_status: unreviewed
model_family: rotating-mean-field
degrees_of_freedom: [intrinsic-shape, rotational-frequency, angular-momentum-orientation]
parameters: [deformation, rotational-frequency]
tags: [high-spin, triaxiality, chirality]
---

# 倾斜轴推转（Tilted Axis Cranking）

## Purpose

自洽或半自洽求解旋转平均场与角动量相对内禀主轴的取向。

## Hamiltonian or Core Formalism

通过最小化 Routhian `H-ω·J` 并要求 ω 与 J 平行确定取向。

Frauendorf 2001 makes the rotating-frame form explicit as `H-prime = H - omega dot J` (and `h-prime = h - omega dot J` for the mean field). A self-consistent solution couples deformation, quasiparticle configuration, rotational frequency and the orientation of `J`.

## Degrees of Freedom

转动频率、形变和角动量方向；可得到 principal-axis、planar 或 aplanar 解。

## Assumptions

平均场近似自发破缺量子对称性；量子隧穿和带间跃迁通常不由单一 TAC 解给出。

## Inputs and Parameters

单粒子场、形变、配对和转动频率。

[[ayangeakaa-2016-133ce-in-beam]] 对 `133Ce` D3 使用 PC-PK1 TAC-CDFT，并在该计算中忽略 pairing。

[[matta-2015-transverse-wobbling-135pr]] 对 `135Pr` 1qp yrast 使用 `Δp=1.1 MeV`、`Δn=1.0 MeV` 并固定 `ε=0.16, γ=26°`；另计算 3qp 和 5qp 组态。

## Predicted Observables

带能量、角动量取向、带内跃迁及 planar/aplanar 几何。

## Strengths

直观揭示 [[chiral-doublet-bands]] 的左右手几何来源。

## Known Limitations

[[frauendorf-meng-1997-tilted-rotation-chirality]] 指出 TAC 不能计算带间跃迁，也不恢复左右手态之间的隧穿。

[[meng-2010-open-problems-nuclear-chirality]] 强调常规 cranking/TAC 是半经典 mean-field description：两个 aplanar 左右手解在 TAC 中简并，正是因为半经典平均场不能描述两者之间的量子隧穿；总角动量通常也不是好量子数。当时的 TAC+RPA 又只覆盖近平衡点的小振幅谐振动。该边界同时回链至 [[frauendorf-meng-1997-tilted-rotation-chirality]]。

`133Ce` D3 的 TAC-CDFT 只在中等自旋收敛，且作者没有对全部偶极带实施同等计算。

`135Pr` 的形变与组态来自平均场计算；TAC 可比较能量和取向，但不独立建立 one-phonon wobbling 的量子带间跃迁。

[[peng-chen-2022-chiral-rotation-rhodium-isotopes]] gives a self-consistent `102-107Rh` 3D-TAC CDFT example: the Routhian is minimized in `theta` and scanned in `phi`, with finite `±phi` minima marking aplanar intrinsic solutions. Its five finite `omega_crit` values are model onsets; `102Rh` only supplies an unconverged lower bound. The calculation fixes configurations and omits pairing, chiral vibration and tunnelling, so it cannot produce the partner spectrum or energy splitting.

[[frauendorf-2018-beyond-unified-model]] provides the broad rotating-mean-field bridge: `H' = H−ω·J`, `J∥ω`, principal-axis/planar/aplanar symmetry classes, and the relation of TAC to cranked-shell and quantum triaxial-rotor descriptions. It explicitly keeps angular-momentum conservation, tunnelling and interband amplitudes as limitations of the semiclassical layer.

## Related Models

[[particle-rotor-model]]

Use the symmetry labels explicitly: PAC preserves a signature-like operation; planar TAC breaks it in a principal plane; aplanar TAC breaks the relevant planar symmetry and yields opposite-handed intrinsic solutions. These are model classifications, not direct band labels.

## Sources

- [[frauendorf-meng-1997-tilted-rotation-chirality]]
- [[ayangeakaa-2016-133ce-in-beam]]
- [[matta-2015-transverse-wobbling-135pr]]
- [[meng-2010-open-problems-nuclear-chirality]]
- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[clark-2000-shears-mechanism]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]
- [[peng-chen-2022-chiral-rotation-rhodium-isotopes]]
- [[frauendorf-2018-beyond-unified-model]]

## Evolution Log

- 2026-07-01：建立 planar/aplanar 与手征用途。
- 2026-07-01：加入 TAC-CDFT 的 `133Ce` 实例和收敛边界。
- 2026-07-03：加入 Matta 2015 的 `135Pr` 1qp/3qp/5qp TAC 比较。
- 2026-07-13：加入 Meng 2010 的 total-angular-momentum、tunneling 与 RPA 边界。
- 2026-08-11: added Peng-Chen 2022 Rh critical-frequency systematics and the configuration-fixed/no-pairing/mean-field boundary.
- 2026-09-20: added Frauendorf 2018 review bridge across TAC, wobbling, chirality, magnetic rotation and termination.
