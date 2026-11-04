---
type: method
title: "BM-II 有限自旋纯转子与高自旋谐近似共同输入对账"
aliases: [BM-II finite-spin benchmark, asymmetric-rotor harmonic-limit audit]
method_type: "model-comparison-benchmark"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Finite-spin asymmetric rotor compared with BM-II Vol. II §4-5e harmonic expansion"
confidence: "high for the implemented Hamiltonian and low for any experimental interpretation"
tags: [bohr-mottelson, asymmetric-rotor, triaxiality, wobbling, benchmark, finite-spin]
sources: [book-bohr-mottelson-nuclear-structure-vol2]
---

# BM-II 有限自旋纯转子与高自旋谐近似共同输入对账

## Purpose

把同一组 \(A_1,A_2,A_3\) 和自旋 \(I\) 同时送入：

1. 完整有限维纯转子哈密顿量
   \[
   H_{\mathrm{rot}}=A_1I_1^2+A_2I_2^2+A_3I_3^2;
   \]
2. BM-II §4-5e 的高自旋横向玻色化近似
   \[
   E_{\mathrm{harm}}(n,I)
   =A_1I(I+1)+(n+\tfrac12)\hbar\omega,
   \qquad
   \hbar\omega=2I\sqrt{(A_2-A_1)(A_3-A_1)}.
   \]

这使有限自旋修正可以在进入粒子-转子、QTR、TAC 或实验响应分析之前单独量化。

## Inputs and Assumptions

- 采用 BM-II 的轴约定 \(A_1<A_2<A_3\)，即
  \(\mathcal J_1>\mathcal J_2>\mathcal J_3\)；
- \(I\) 必须为整数或半整数；
- 有限维计算在完整 \(\vert I,K\rangle\) 表象中构造 \(I_1,I_2,I_3\) 并直接对角化；
- 高自旋比较使用排序后最低能级的相邻二元组平均值作为轨迹中心；
- 这个二元组是数值对账标签，不等同于实验能带标签，也不替代偶偶核
  \(D_2\) 对称块的明确投影。

可复用函数：

```text
system/scripts/analysis/bm2_asymmetric_rotor_matrix_diagonalizer.py
  diagonalize_bm_asymmetric_rotor(...)
  compare_bm_high_spin_with_finite_spin(...)
```

## What It Can Establish

BM-II 的式 (4-296)–(4-304) 以 \(I_1\simeq I\) 和小横向涨落构造谐近似；
式 (4-306)–(4-307) 要求
\[
I^2\gg\langle I_2^2+I_3^2\rangle
\]
并给出含 \(n\) 与惯量参数的有效性尺度。因而“较大的 \(I\)”只是必要背景，
不能单独证明近似有效。

BM-II pp. 193–194 的式 (4-310)–(4-314) 说明同一 \(\hat n\) 轨迹内的 E2
连接和改变 \(\hat n\) 的连接具有不同的振幅阶数。有限自旋能量对账只能检查
哈密顿量近似边界，不能由能量残差推导 \(B(E2)\)、wobbling 身份或三轴刚性。

pp. 195–196 的 Regge 轨迹讨论还说明：非轴对称转子可以在不同主轴表象中构造
轨迹，轨迹序号 \(K\) 是解的排序/延拓标签；在中间惯量轴表象中，作者讨论了
连续谱的解析结构。因此代码中的 pair-centroid 只用于数值收敛诊断，不能被写成
严格守恒的 \(K\) 量子数。

## Diagnostic Outputs

对每个 \(n\) 输出：

- exact finite-spin pair energies；
- pair centroid；
- pair splitting；
- harmonic energy；
- centroid minus harmonic residual；
- residual divided by \(\hbar\omega\)。

建议先看 \(n=0\) 的残差和 pair splitting，再增加 \(n\)。高 \(n\) 的残差更容易
暴露有限自旋、非谐性和排序映射的影响；这是一项模型自洽性检查，不是实验拟合优度。

## Verification

2026-11-03 的回归检查：

- \(I=40,\ (A_1,A_2,A_3)=(8,12,30)\) 的最低二元组在
  \(\hbar\omega\) 归一化后残差小于 \(0.01\)；
- 同一输入的最低二元组分裂小于 \(10^{-6}\)（数值精度范围）；
- 小维度谱不允许请求超出可用二元组数的 \(n_m_m_{\max}\)；
- BM-II 高自旋计算器与有限维矩阵计算器的 8 项专项测试通过。

## What It Cannot Establish Alone

该对账不能确定真实核素的 wobbling 声子数、TiP 身份、\(\gamma\) 刚性、手征性、
准粒子组态或实验跃迁多极性。它也不能把有限自旋谱的近简并 pair 直接对应到
某一条实验能带。

## Boundaries and Competing Explanations

- 纯转子有限维对角化不包含准粒子、配对、Coriolis 粒子-转子耦合、构型混合、
  feeding、寿命、效率和偏振响应；
- pair centroid 接近谐公式不能确认实验带是 wobbling，也不能区分 TiP、
  \(\gamma\) 振动和旋称伙伴；
- 如果 \(A_2\) 或 \(A_3\) 接近 \(A_1\)，BM-II 有效性尺度会变差，应转向完整
  有限自旋计算并明确报告轴对称极限；
- 真正的 A≈130 数据对账必须在同一自旋、组态、\(Q_0/Q_2\) 轴定义和实验响应
  合同下同时比较能级、分支、寿命、混合比和偏振。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]
- [[bm2-high-spin-asymmetric-rotor-e2-contract]]
- [[bm2-asymmetric-rotor-d2-and-transition-contract]]
