---
type: method
title: "Bohr–Mottelson Vol. II §4-5e：高自旋非轴对称转子与 E2 观测量合同"
aliases: [BM-II asymmetric rotor high-spin, three-axis rotor E2 contract, 三轴转子高自旋近似]
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
method_type: "high-spin-asymmetric-rotor"
scope: "Rendered verification of BM-II §4-5e, PDF pp. 212-218 / printed pp. 190-196"
confidence: "high for the displayed equations and approximation boundary"
tags: [bohr-mottelson, triaxial-rotor, wobbling, high-spin, e2-transition, approximation-validity]
sources: [book-bohr-mottelson-nuclear-structure-vol2]
---

# Bohr–Mottelson Vol. II §4-5e：高自旋非轴对称转子与 E2 观测量合同

## Purpose

把非轴对称转子高自旋近似中的四个层次分开：

```text
惯量排序/轴约定
-> 高自旋玻色化
-> 能量与摆动/进动量子 n
-> E2 矩阵元、B(E2) 和连接跃迁
```

这组公式是实验判断 wobbling 候选带时的重要理论基线，但只适用于书中给出的
高 \(I\)、小横向涨落和指定轴约定，不能直接当作完整 QTR、TAC 或粒子-转子计算。

## Inputs and Assumptions

- 旋转参数 \(A_k=\hbar^2/(2\mathcal J_k)\) 按
  \(A_1<A_2<A_3\) 排列，因此 \(\mathcal J_1\) 是最大惯量轴；
- 研究的是给定 \(I\) 的 yrast 或附近高自旋态，\(|I_1|\simeq I\)；
- 横向分量满足
  \[
  I^2\gg\langle I_2^2+I_3^2\rangle;
  \]
- 对 \(I_2,I_3\) 使用近似玻色算符，并以 \(D_2\) 对称性约束偶偶核的允许状态；
- E2 算符中的 \(Q_0,Q_2\) 必须相对于明确的主转轴定义；
- \(\hat n\) 是推导中的玻色数算符；选定数态后才用 \(n\) 表示其本征值，
  二者都不自动等于实验上命名的 wobbling phonon 数。

## What It Can Establish

### 能量与高自旋量子

原书 Eq. (4-296)–(4-304) 给出
\[
\hbar\omega
=2I\sqrt{(A_2-A_1)(A_3-A_1)},
\]
\[
E(n,I)=A_1 I(I+1)+\left(n+\frac12\right)\hbar\omega.
\]

\(n\) 描述相对于总角动量方向的轴进动/横向振动；在小振幅极限，它具有谐振动
形式。偶偶核还要满足原书的 \(D_2\) 对称性选择条件。

### 近似有效域

原书 Eq. (4-306)–(4-307) 把近似有效性写成
\[
I^2\gg\langle I_2^2+I_3^2\rangle,
\]
并给出含数算符 \(\hat n\) 和三个 \(A_k\) 的显式下限；在 \(\hat n\) 本征态中
才可将其写成数值 \(n\)。若 \(A_3\) 远大于 \(A_2,A_1\)，
从 \(K\simeq I_3\simeq0\) 到 \(K\simeq I_1\simeq I\) 的结构转换可能需要更高
的角动量；不能只凭“自旋很大”宣称近似有效。

### E2 矩阵元和带间观测

原书 Eq. (4-308)–(4-311) 以相对于 \(1\) 轴的 \(Q_0,Q_2\) 写出 E2 矩阵元。
领先阶结果包括：
\[
Q\simeq Q_0,
\qquad
B(E2;nI\rightarrow n,I+2)
\simeq \frac{5}{16\pi}e^2Q_2^2,
\]
以及改变 \(n\) 的连接跃迁：
\[
B(E2;nI\rightarrow n-1,I-1)
\simeq \frac{5}{16\pi}e^2\frac{n}{I}
(\sqrt3 Q_0x-\sqrt2 Q_2y)^2,
\]
\[
B(E2;nI\rightarrow n+1,I-1)
\simeq \frac{5}{16\pi}e^2\frac{n+1}{I}
(\sqrt3 Q_0y-\sqrt2 Q_2x)^2.
\]
两条连接分别含 \(n/I\) 和 \((n+1)/I\) 的抑制因子；\(x,y\) 是将原始横向
玻色子变换到对角化变量的系数，满足 \(x^2-y^2=1\)。

因此，能量上看到等间隔或近似线性量子序列，还必须同时检查：

- 同一 \(n\) 内的强 E2 级联；
- \(\Delta n=\pm1\) 连接跃迁的相对弱度，且分支要区分 \(n/I\) 与 \((n+1)/I\)；
- \(Q_0,Q_2\) 主轴约定；
- 实验效率、门条件和 feeding。

## Discriminating Observables

代码或拟合接口至少应保存：

- \(A_1,A_2,A_3\) 及其主轴标签；
- \(I,n,\hbar\omega,E(n,I)\)；
- 近似有效性指标
  \[
  \epsilon=\frac{(2n+1)(A_2+A_3-2A_1)}
  {2I\sqrt{(A_3-A_1)(A_2-A_1)}};
  \]
- \(Q_0,Q_2\) 的定义和轴变换；
- \(\Delta n=0\) 与 \(\Delta n=\pm1\) 的 E2 强度预测；
- 同一实验响应下的能量和跃迁强度残差。

可复用实现为
`system/scripts/analysis/davydov_wobbling_rotor_calculator.py` 中的
`calculate_bm_high_spin_asymmetric_rotor`。它明确要求 \(A_1<A_2<A_3\)，返回
\(\hbar\omega\)、\(E(n,I)\)、近似指标和 leading-order E2 proxies；`mode_inference`
固定为 `None`。

## Counter-evidence and Competing Interpretations

- \(n\)-线性或近似等间隔能量可以被其它集体或准粒子结构模拟；
- 强 \(\Delta n=0\) E2 和弱连接跃迁是该近似的结果，但会受到非谐性、粒子-转子
  耦合、configuration mixing 和未观测 feeding 改变；
- \(Q_0,Q_2\) 互换主轴后，公式外观和“中轴/短轴/长轴”标签可能改变；
- 中间轴附近的完整量子谱不能用单一高自旋 yrast 展开替代；
- 该近似本身不判断实验带是 wobbling、TiP、\(\gamma\) vibration 还是其它模式。

## What It Cannot Establish Alone

这些公式不能单独确定一个真实核素的 wobbling 声子数、TiP 身份、三轴静态形状或
手征双带。实验使用时还必须加入带间连接、寿命、偏振、混合比、feeding 和响应
协方差；缺少这些输入时只能报告模型 benchmark。

## Model Dependence

```text
BM-II harmonic asymmetric rotor
        -> energy and E2 benchmark
full particle-rotor/QTR/TAC/TPSM
        -> finite-spin, quasiparticle and configuration corrections
experiment
        -> calibrated energies, intensities, lifetimes, polarization and feeding
```

只有第一层输入时，输出应标为 model benchmark；不能自动写成核素结构结论。

## Limitations and Missing Evidence

本页核对 BM-II Vol. II PDF pp. 212–218 / printed pp. 190–196 的页面图像和文字。
尚未完成 §4-5 后续全部轨迹例题、附录、完整 E2 网络或现代粒子-转子计算。真实
wobbling 判断还需要共同母态、带间连接、混合比、寿命、偏振和响应协方差。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]
- [[lawrie-tip-wobbling-discrimination]]
- [[nuclear-chirality-and-wobbling-triaxial-foundations]]
