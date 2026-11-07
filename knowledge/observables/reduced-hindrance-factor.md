---
type: observable
title: 折合阻碍因子（f_nu）
aliases: [reduced hindrance factor, f_nu, K-isomer hindrance]
created: 2026-11-06
updated: 2026-11-07
status: active
review_status: unreviewed
observable_kind: transition-hindrance-metric
symbol: f_\nu
units: dimensionless
tags: [isomers, k-isomer, forbidden-transition, triaxiality, k-mixing]
---

# 折合阻碍因子（Reduced Hindrance Factor, $f_\nu$）

## Definition

用于定量评估**高 $K$ 同核异能态（$K$-Isomers）**跃迁禁戒程度的物理观测量。在轴对称形变核中，总角动量在对称轴上的投影 $K$ 是一个良好量子数。若跃迁初末态之间的角动量投影改变 $\Delta K = |K_i - K_f|$ 大于跃迁多极阶数 $\lambda$，该跃迁按照几何选择定则是严格禁戒的。此时跃迁禁戒度定义为：
$$\nu = \Delta K - \lambda$$
仅在ν>0且名义K与多极性有意义时定义折合阻碍因子。
它把该支路相对Weisskopf估计的速率抑制按禁戒度归一化；
不是不依赖初末态的形变量。

## How It Is Obtained

定义F_W=Tγ,partial/TW。若btotal是该跃迁**光子加转换电子**
相对于所有母态衰变的分支，α是该多极的总内转换系数，则
\[
T_{\gamma,\mathrm{partial}}
=T_{\mathrm{total}}\frac{1+\alpha}{b_{\mathrm{total}}}.
\]
若输入已经是qγ=λγ/λtotal，则Tγ,partial=Ttotal/qγ，不重复修正α。
仅在“Branching Ratio”明确指qγ时，旧页的Ttotal/Branching Ratio才成立。
平均寿命与半衰期可分别使用，但分子和Weisskopf分母必须采用同一种时间定义。

对于 $\nu$-重禁戒跃迁，折合阻碍因子按禁戒阶数归一化为：
$$f_\nu = (F_W)^{1/\nu} = \left( \frac{T_{1/2}^\gamma}{T_{1/2}^W} \right)^{1/(\Delta K - \lambda)}$$

## Diagnostic Use

某些良好形变核的经验fν约100，但离散、支路与组态依赖显著
（[[dracoulis-2013-192os-isomers-gamma-soft]]印刷p.331）。
不将100–300或5–30作为核区判决阈值。
跃迁振幅含初、末态K分量及算符的相干求和：
\[
\langle f|T_{\lambda\mu}|i\rangle
=\sum_{K_f,K_i}c_{fK_f}^*c_{iK_i}
\langle I_fK_f|T_{\lambda\mu}|I_iK_i\rangle.
\]
小fν可能与静态三轴、γ涨落、Coriolis顺排、偶然近能态混合或不同组态有关；
振幅还可能相消，不能从一个数唯一反演γ。

## Failure Modes and Ambiguities

- **跃迁两端**：[[hayes-2005-k-conservation-178hf]]结论PDF pp.279–281
  区分低K带的随旋转混合和仍较纯的高K带；不把混合全归给异能态自身。
- **寿命与阻碍不同**：192Os表1的长寿命10−态可有约5–11的支路fν；
  高多极性、低Eγ与K阻碍共同决定寿命，不能只从总寿命判断K好坏。
- **多极混合比影响**：若跃迁包含混合多极性（如 $M1+E2$），计算 $F_W$ 时必须根据实测混合比 $\delta$ 分别分解 $M1$ 与 $E2$ 的分阻碍因子，不可直接使用全跃迁强度。

P1 self-audit：具体提取须核对ΔK、ν>0、支路定义、α、δ的约定、时间定义和误差。
fν的相对误差、谱线混叠及未观测分支必须传播；本页不宣称已测得任何核的γ。

## Model Dependence

名义K、支路多极性与Weisskopf归一是定义输入；初末态K混合及矩阵元相干决定实际强度。

## Sources

- [[hayes-2005-k-conservation-178hf]]，结论PDF pp.279–281。
- [[dracoulis-2013-192os-isomers-gamma-soft]]，印刷p.331、Table1。
