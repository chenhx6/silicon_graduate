---
type: method
title: "有限模型空间常配对 BCS 求解器与相位约定审计"
aliases: [constant-pairing BCS solver, Suhonen BCS numerical baseline, BCS gap solver]
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
method_type: bcs-solver
tags: [bcs, pairing, quasiparticle, suhonen, nuclear-structure, numerical-method]
sources: [book-suhonen-from-nucleons-to-nucleus]
---

# 有限模型空间常配对 BCS 求解器与相位约定审计

## Purpose

如何把 Suhonen 第 13–14 章的 BCS 数值入口变成一个可重复、可测试、能服务于
A≈130 核结构计算的 Python 基线，同时避免把球形常配对结果误当成三轴高自旋的
最终模型？

本页对应实现：

`system/scripts/analysis/bcs_constant_pairing_solver.py`

它只解决有限球形模型空间中的常数单极配对问题，用来检查粒子数、配对隙、
化学势、准粒子能量和占据数的内部一致性。

### Mathematical Definition

对轨道 \(a\)，令 \(\Omega_a=(2j_a+1)/2\) 为时间反演成对简并度，采用正的
\(u_a,v_a\) 相位和配对隙幅值 \(\Delta\)，实现的方程是
\[
E_a=\sqrt{(\epsilon_a-\lambda)^2+\Delta^2},
\]
\[
v_a^2=\frac12\left[1-\frac{\epsilon_a-\lambda}{E_a}\right],
\qquad
u_a^2+v_a^2=1,
\]
\[
\bar N=\sum_a 2\Omega_a v_a^2,
\qquad
\Delta=G\sum_a\Omega_a u_a v_a.
\]
程序在每一个 \(\Delta\) 迭代步用二分法求 \(\lambda\)，从而显式满足目标平均粒子数；
再用阻尼固定点更新 \(\Delta\)。

## Inputs and Assumptions

- 单粒子能量和 \(\Omega_a\) 已给定，模型空间有限；
- 相互作用由单一正的吸引强度 \(G\) 表示；
- 靶粒子数是平均粒子数，BCS 态本身不具有严格粒子数；
- \(u,v\) 采用正值规范，\(\Delta\) 作为幅值输出；
- 不含轨道依赖 SDI 自能、Lipkin–Nogami 粒子数投影、阻塞、形变、Coriolis
  场或推转 QRPA。

如果需要比较 Suhonen 的 CS/BR 相位，必须另外携带轨道相位和带符号的矩阵元；
不能从本求解器输出的 \(|\Delta|\) 单独恢复相位信息。

## What It Can Establish

实现返回：

- `particle_number` 与 `particle_number_residual`：粒子数约束；
- `gap_MeV` 与 `gap_equation_residual_MeV`：自洽间隙方程；
- `chemical_potential_MeV`：费米面位置；
- 每个轨道的 \(\eta_a=\epsilon_a-\lambda\)、\(E_a\)、\(u_a\)、\(v_a\) 和 \(v_a^2\)；
- `converged`、迭代次数和明确的模型边界。

单一简并壳的半填充测试提供了解析基准：当 \(\epsilon=0\)、\(\Omega=3\)、
\(\bar N=3\)、\(G=1\) MeV 时，
\[
\lambda=0,\qquad u^2=v^2=\frac12,\qquad \Delta=\frac{G\Omega}{2}=1.5\text{ MeV}.
\]
该测试只验证数值求解和规范化，不构成真实核的配对隙测量。

### Supporting Evidence and Benchmarks

- Suhonen Ch. 13 printed pp. 391–416：BCS 真空、准粒子变换、粒子数涨落和
  变分方程。
- Suhonen Ch. 14 printed p. 418 / physical PDF p. 414，Eqs. (14.1) 对应
  \(u_a,v_a,E_a,\Delta_a\) 和粒子数关系；physical PDF p. 414 已渲染核对。
- Suhonen Ch. 14 printed pp. 418–420：迭代数值流程、\(\lambda\) 修正和收敛判据；
  physical PDF pp. 414–416 的相邻页面作为数值流程定位。
- Suhonen physical PDF pp. 420–423 / printed pp. 422–425：SDI 示例中的自能简化、
  \(d\)-\(s\) 与 \(f\)-\(p\)-\(0g_{9/2}\) 模型空间和占据概率系统学。
- 代码回归：`system/tests/test_bcs_constant_pairing.py` 验证半填充解析隙、
  粒子数守恒、准粒子恒等式和非法输入拒绝。

## What It Cannot Establish Alone

- **BCS 隙不是唯一实验量。** 质量差分得到的经验配对指标、准粒子能量、阻塞后的
  动态配对响应和模型中的 \(\Delta\) 可能不同。
- **常配对强度不是 SDI。** Suhonen 的 SDI 矩阵元包含角动量几何、相位、归一化和
  轨道依赖结构；本求解器只提供均匀配对基线。
- **粒子数投影会改变弱配对区行为。** BCS gap collapse 不能直接解释成有限核中
  相关完全消失；LN-BCS、投影方法或固定粒子数计算可能保留不同的关联。
- **球形基线不能直接回答三轴问题。** 对 wobbling、chirality、形状共存和高自旋
  CAP，仍需把 Nilsson/BCS、PRM、TPSM、TAC 或 HFB/QRPA 与实验跃迁联合比较。

### Current Scope and Boundary

该求解器作为微观计算链的“配对底座”：

```text
单粒子能量 + 简并度
    -> BCS (lambda, Delta, u, v)
    -> QTDA/QRPA 或 blocked/cranked 扩展
    -> 电磁跃迁、能带交叉、wobbling/chirality 竞争解释
```

在 A≈130 应用中，任何由本模块生成的 \(\Delta\)、\(u/v\) 或准粒子能量都应标记为
`constant-pairing spherical baseline`，并与实际形变、有效相互作用、粒子数投影和
实验约束分开记录。

## Sources

- [[book-suhonen-from-nucleons-to-nucleus]]
- [[suhonen-bcs-qrpa-and-transition-crosswalk]]
- [[multi-quasiparticle-isomers-and-blocked-bcs-pairing]]
- [[coriolis-anti-pairing-and-moment-of-inertia-expansion]]
