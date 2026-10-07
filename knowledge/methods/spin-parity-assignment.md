---
type: method
title: Spin/parity assignment
aliases: [spin parity assignment, spin assignment, parity assignment, Jpi assignment, J^pi assignment]
created: 2026-07-09
updated: 2026-10-07
status: ai-draft
review_status: unreviewed
method_type: level-assignment
tags: [spin-parity, assignment, angular-distribution, dco, gamma-spectroscopy]
---

# Spin/Parity Assignment

## Purpose

Spin/parity assignment combines level-sequence logic, transition properties, and selected experimental observables to constrain `J^pi` for nuclear states.

## Inputs and Assumptions

- reliable level-sequence and coincidence relations;
- at least one transition-property handle such as angular distribution, DCO, polarization, conversion, or lifetime information;
- an explicit statement of what is measured directly and what is inferred from heuristic band regularity or comparison with known patterns.

## Typical Inputs

- transition energies and coincidence relations;
- candidate spin sequence and band context;
- angular distribution or angular-correlation information;
- DCO ratios, linear polarization, conversion coefficients, lifetimes, or band regularity when available.

## Source-Level Practice Boundary

[[summary-2013-bases-spin-parity-assignments]] is the main background source currently ingested for this page. It is a reference guide rather than an original experiment. For high-spin states it records practical heuristics for angular distributions and DCO ratios using a typical orientation parameter `σ/I = 0.3`, and it also distinguishes stronger arguments from weaker arguments for rotational-band assignments.

This page therefore treats spin/parity assignment as a method bundle, not as a single observable. In particular, a quoted "typical orientation parameter" from a guide should not be promoted into a universal `sigma/I` prescription.

## What It Can Establish

When several observables are mutually consistent, spin/parity assignment can narrow or fix plausible `J^pi` values for states and transitions.

## What It Cannot Establish Alone

No single rule is universal across detector geometry, reaction mechanism, and feeding history. Regular level spacing alone is usually weaker than angular-distribution, angular-correlation, polarization, conversion, or lifetime evidence.

## Assignment Evidence Dependencies

自旋、宇称和多极性应逐项列明观测、固定输入和条件推断。同一个含假设的角分布/DCO 拟合输出三个标签，不会产生三份独立证据。观测通道互补、统计独立和实验谱系独立是不同问题；同一事件样本的角分布与偏振计数要保留协方差，共用 response/alignment 或已知 spin anchor 也要明确。

| Claim | 常见约束 | 必须记录的条件或依赖 |
|---|---|---|
| spin / ΔJ | 级联、角分布、角关联/DCO 的候选比较 | 末态 spin anchor、gate multipolarity、alignment；由 band regularity 固定的输入不能再算作观测结果 |
| parity change | 已约束的 photon rank L、E/M 性质 + 已知末态宇称 | 若 E/M 是用待定 parity 选择的拟合模型，parity 结论有循环依赖；需要独立或互补的偏振/转换约束 |
| photon multipolarity | angular rank 和 E/M 候选的联合响应 | 选律仅排除不允许候选；低阶截断不排除允许高阶成分；single-gamma angular rank K 和 photon rank L 不等同 |
| mixing ratio sign | 约定明确的干涉敏感角分布/偏振/角关联 | 算符、bra/ket 顺序、发射/吸收、first/second cascade γ 与响应；率或普通ICC只有 δ² |
| absolute strength / hindrance | 寿命、完整分支、能量、已知多极与参考尺度 | 未观测分支、内转换、E0、feeding、效率与协方差；一个 lifetime 本身不提供唯一多极 |

[[rose-brink-1967-phase-defined-angular-distributions]] 的 RB67-2/3/4/7/8 分开 population、geometry、polarization、interference 与 integrated width；[[lange-kumar-hamilton-1982-multipole-admixtures]] 的 LKH82-1/4/5 分开 γ 振幅约定、级联相位和 E0/ICC。这张表是基于这些 formalism 的分析性证据审计，不是新实验。三条合成跃迁及所有允许高阶候选见 [[multipole-mixing-ratio]]；题设 Jπ 标签不具有实测证据。


实际依赖反例见 [[multipole-mixing-ratio]] 的“布居未知时，角分布和偏振可以共享多极歧义”：在固定题设Jπ但布居分别为high-M/low-M时，pure E1/pure M2能给相同pointwise方向/偏振强度。因此增加一个measurement channel不自动消除共用population的条件推断；该L2反例不声明所有γ观测或真实核素都相同。独立布居校准须来自另一个已建立的约束，不能重用待判multipole拟合。依据 [[rose-brink-1967-phase-defined-angular-distributions]] RB67-10/11/12；实际实验还需响应、背景、gate/feeding与协方差。

## Related Pages

- [[angular-distribution]]
- [[angular-correlation]]
- [[dco-ratio]]
- [[linear-polarization-asymmetry]]
- [[multipole-mixing-ratio]]

## Sources

- [[summary-2013-bases-spin-parity-assignments]]
- [[chiara-2012-cu65-cu67-core-coupled-protons]]
- [[rose-brink-1967-phase-defined-angular-distributions]]
- [[lange-kumar-hamilton-1982-multipole-admixtures]]

### Four-Multipole Local Identifiability

合成2+→2+在固定Jπ、完整M1/E2/M3/E4、未知aligned布居下，完整单γ方向与线偏振仅有四个normalized形状系数。RB67-13的exact内域seed证明五变量映射rank4、存在改变multipole fractions的一维同观测解族；独立固定布居后同点rank3只是局部改进，isotropic点仍不唯一。多个观测通道须列明共享布居与模型先验；Gaussian或低阶截断不增加独立证据。未给定的same-parent2+→0+ pure-E2参考设计可校准B2/B4，须匹配gate/feeding/axis/response；详见[[rose-brink-1967-phase-defined-angular-distributions]]与[[multipole-mixing-ratio]]。这不是实测spin/parity赋值或L4结果。
