---
type: observable
title: 能带交叉相互作用强度（|V_12|）
aliases: [band crossing interaction, V12, backbending interaction, band-mixing matrix element]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
observable_kind: hamiltonian-matrix-element
symbol: |V_{12}|
units: keV
tags: [backbending, bandcrossing, csm, routhian, quasiparticle-alignment]
---

# 能带交叉相互作用强度（Band Crossing Interaction, $|V_{12}|$）

## Definition

在推转壳模型（CSM）与高自旋能谱中，当基态带（$g$-带）与高 $j$ 准粒子对齐带（$s$-带，Stockholm 带）在临界推转频率 $\hbar\omega_c$ 处发生回避交叉（Avoided Crossing）时，耦合两能带的非对角相互作用哈密顿量矩阵元绝对值 $|V_{12}|$。它直接决定了实验上观测到的转动回弯现象究竟是**尖锐回弯（Sharp Backbending）**还是**平滑上弯（Smooth Upbending）**。

## Formula and Extraction Formalism

在两带混合模型哈密顿量中，转动坐标系下的两未微扰能带准粒子 Routhian 分别为 $e'_1(\omega)$ 与 $e'_2(\omega)$：
$$H'(\omega) = \begin{pmatrix} e'_1(\omega) & V_{12} \\ V_{12} & e'_2(\omega) \end{pmatrix}$$

本征能量为：
$$e'_{\pm}(\omega) = \frac{e'_1 + e'_2}{2} \pm \sqrt{ \left( \frac{e'_1 - e'_2}{2} \right)^2 + |V_{12}|^2 }$$

在精确交叉点 $\omega = \omega_c$ 处，$e'_1(\omega_c) = e'_2(\omega_c)$，两本征能带在转动坐标系下的最小能量间距（回避交叉能隙）直接由相互作用强度决定：
$$\Delta e'_{\text{min}} = e'_+(\omega_c) - e'_-(\omega_c) = 2 |V_{12}|$$

### 实验提取方法
利用实验测得的离散激发能 $E(I)$ 与自旋 $I$，计算推转转动频率 $\hbar\omega = \frac{E(I) - E(I-2)}{I_x(I) - I_x(I-2)}$ 与实验准粒子 Routhian：
$$E'(I) = \frac{1}{2} [E(I) + E(I-2)] - \omega I_x$$
从 $E'(\omega)$ 回避交叉曲线的最小垂直距离直接反演：
$$|V_{12}| = \frac{1}{2} \Delta E'_{\text{min}}$$

## Quantitative Classification Benchmarks

| 相互作用强度量级 | 物理表现形式 | 实验核转动惯量 $\mathcal{J}^{(1)}$ 曲线特征 | 物理微观机制 |
| :--- | :--- | :--- | :--- |
| **$|V_{12}| < 35\text{ keV}$（弱相互作用）** | **尖锐回弯（Sharp Backbending）** | $\hbar\omega$ 曲线出现强烈的负斜率反折（$S$ 型回弯） | 准粒子轨道与核芯弱耦合，配对隙突变去对 |
| **$35\text{ keV} \le |V_{12}| < 65\text{ keV}$（中等）** | **标准回弯** | 频率停滞或小幅度折返 | 费米面适中，两带平滑混合 |
| **$|V_{12}| \ge 65\text{ keV}$（强相互作用）** | **平滑上弯（Smooth Upbending）** | 动力学转动惯量单调上升，无任何负斜率 | 强三轴形变、四极电荷分布强混合或大配对涨落 |

## Oscillations across Isotopic Chains

理论微观推导表明，$|V_{12}|$ 随价核子数填充在同位素链上表现出特征性的**振荡行为（Oscillation of $|V_{12}|$）**：
- 当费米面处于高 $j$ 壳层（如 $h_{11/2}$）特定特定相干点时，$|V_{12}|$ 周期性趋近于 0（导致极端回弯）；而在两极小值之间 $|V_{12}|$ 达到极大（呈现平滑上弯）。这一振荡由内禀单粒子波函数与时间反演核芯相互作用的贝塞尔型干涉产生。
