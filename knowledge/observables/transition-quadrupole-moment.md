---
type: observable
title: 跃迁四极矩
aliases: [transition quadrupole moment, quadrupole moment, Qt, Q_t, QSD, QND]
created: 2026-07-03
updated: 2026-10-09
status: active
review_status: unreviewed
observable_kind: electromagnetic-collectivity
symbol: "Q_t"
units: b
tags: [e2, lifetime, deformation, superdeformation]
---

# 跃迁四极矩（Transition Quadrupole Moment）

## Definition

由带内 E2 跃迁强度或寿命提取、表征转动带电四极集体性的量。文献有时简写为 `Q`；引用时必须确认它是 transition quadrupole moment、spectroscopic quadrupole moment，还是模型内禀矩。

## Formula and Conventions

`Q_t` 与 B(E2) 的换算依赖转子矩阵元、K/强耦合假设和单位约定。跨论文比较必须保留采用的几何因子、分支、内转换和 feeding 修正。

### Source-specific `K`-rotor rate conversion

Singh et al. give one explicit high-spin convention for `I→I−2` E2 transitions:

`T(E2; I→I−2) = 1.224×10^12 Eγ(MeV)^5 CG(I,K)^2 Q_t(eb)^2 s−1`.

Their Eq. (2) replaces the single Clebsch–Gordan factor with a sum over `K` amplitudes for nonaxial or mixed-`K` states. This is a rotor extraction formula: it requires an identified E2 transition, its energy, and an applicable `K`-mixing prescription. Other papers may use a different unit convention or rotor matrix-element model. It cannot supply a unique `Q_t` for a spin-indexed table whose `B(E2)` row has no transition identity or `K` assumption. See SI16-17 and the MU07 transition-mapping boundary in [[mukhopadhyay-2007-135nd-chiral-vibration-static]].

## How It Is Obtained

通常由 Doppler-shift 或其他寿命测量结合 E2 分支提取。[[domscheit-1999-triaxial-superdeformation-163lu]] 本身没有新测寿命，而是引用 Ref.[2] 的 `Q_SD=10.7(7) b`、`Q_ND=6.0(5) b`，并用本工作分支比的两带混合分析得到 `Q_ND/Q_SD=0.48(7)`。

[[babra-2019-deformation-change-136sm]] 对 576-910 keV yrast E2 跃迁做 DSAM 线形拟合，得到 8+ 至 20+ 的寿命或上限，再在 `K=0` 转子近似下提取 `Q_t`。stopping power（阻停能力）系统误差未纳入表中误差，作者估计可达 15%。

## Diagnostic Use

- 约束集体 E2 强度和形变尺度；
- 区分正常形变与超形变带的集体性；
- 检查带混合分析由强度比导出的四极矩比是否与寿命结果一致。
- 沿同一带追踪跨带交叉的集体性变化；`Q_t` 下降可支持集体性减弱，但形变极小和 γ 刚性仍需模型或其他观测量。

## Model Dependence

从 `Q_t` 映射到 `β2/ε2` 依赖形状参数化、有效电荷和转子近似。`163Lu` 的实验平均 `Q=10.7(7) b` 同时接近 UC 对正 γ、负 γ 组态给出的 9.9 b 和 11.0 b，因此不能单独判定 γ 符号。`136Sm` 中交叉后较低 `Q_t` 与 TRS/TPSM 的较小 β2 一致，但“γ-soft→稳定三轴”仍是模型支持的解释。

## Failure Modes and Ambiguities

- 未分辨 feeding、带混合和弱分支会影响寿命/强度提取；
- 大 `Q_t` 支持强集体形变，但不单独证明三轴刚性；
- 二手转述的绝对数值必须回到原始寿命来源复核。

## Examples

`163Lu` SD1 是“大四极矩支持超形变，但不能区分正负 γ”的参照案例。`136Sm` 是“跨带交叉的 `Q_t` 系统学约束集体性，但不单独给出 γ 刚性”的案例。

## Sources

- [[domscheit-1999-triaxial-superdeformation-163lu]]
- [[babra-2019-deformation-change-136sm]]
- [[singh-2016-lifetime-131ce-133pr]]
- [[mukhopadhyay-2007-135nd-chiral-vibration-static]]
- [[zhu-2003-135nd-composite-chiral-pair]]
- [[li-2004-lifetimes-131ce]]
- [[petrache-1998-highly-deformed-lifetimes-131ce-nd]]

## `131Ce` cross-source boundary

- Singh 2016 的 normal-deformed Band-1-like 序列用寿命得到 `Q_t`；Li 2004 给出同一负宇称谱系及另一条正宇称谱系的早期值。Singh 表中转载/再算的 Li 行不能重复计权。
- Petrache 1998 报告独立高度形变带的 intrinsic `Q0`。`Q0` 与 normal-deformed `Q_t` 的几何、K mixing 和形变假设不同，只能分层比较，不能直接把比值解释为形变比。
- 单侧寿命限值与矩限值方向相反：`τ` 上限给 `Q_t` 下限，`τ` 下限给 `Q_t` 上限。
- 在 pure-E2、branching=1、ICC=0 和 source-specific K 的诊断复算中，Singh 有限点与报道值相容到约 15% 内；该检查不是对完整 side-feeding 分析的替代。

## Evolution Log

- 2026-07-03：建立超形变判据、两带混合和 γ 判别限制。
- 2026-07-05：加入 `136Sm` DSAM 寿命、`Q_t` 下降与形变解释边界。
