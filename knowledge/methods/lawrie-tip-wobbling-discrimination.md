---
type: method
title: "Lawrie TiP 与声子 wobbling 的实验判据卡"
aliases: [TiP vs wobbling, tilted precession discrimination, Lawrie Table 6.1]
method_type: "experimental-mode-discrimination"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
tags: [wobbling, tilted-precession, tip, triaxiality, b-e2, gamma-spectroscopy, petrache-2025]
sources: [book-petrache-chirality-and-wobbling]
---

# Lawrie TiP 与声子 wobbling 的实验判据卡

## Purpose

把原书中的 TiP/声子 wobbling 区分条件整理成可复核的能级、跃迁和谐近似指标，
服务于在束 \(\gamma\) 谱学的候选带筛选与竞争解释比较。

## Question and Scope

如何把 Petrache 编著本第 6 章的核心区别转成在束 \(\gamma\) 谱学可以实际检查的
量：刚性三轴转子的倾斜进动（tilted precession, TiP），还是一维转动上叠加的
量子摆动声子（wobbling phonon）？

本页只整理 Lawrie Ch. 6 的模型判据和当前代码接口，不把一个判据自动升级为
真实核素的模式确认。

## Inputs and Assumptions

输入包括已确认的能级身份、同自旋相对激发能、绝对或相对 \(B(E2)\)、转动常数
\(A_s,A_i,A_l\)、自旋和必要的实验效率/寿命修正。解析 TiP 比较主要针对
\(\gamma=30^\circ\) 及其附近；书中模型比值示例约为
\(20^\circ\le\gamma\le30^\circ\)。真实核的 \(\gamma\) 软性、构型混合和误差协方差
需要另外输入。

## Definition

三轴偶偶核转动能可写为
\[
E=\frac{\hbar^2}{2\mathcal J_s}I_s^2+
  \frac{\hbar^2}{2\mathcal J_i}I_i^2+
  \frac{\hbar^2}{2\mathcal J_l}I_l^2 .
\]

在 \(\gamma=30^\circ\) 的解析例中，令
\[
m=I-I_i
\]
表示总角动量偏离中间轴的转动量子数。TiP 的激发能对 \(m\) 呈二次依赖：
\[
E_{\mathrm{TiP}}(I,m)=
\frac{\hbar^2}{2\mathcal J_i}
\left[I(I+4)+3m(2I-m)\right].
\]

声子 wobbling 则以声子数 \(n\) 标记：
\[
E_{\mathrm{wob}}(I,n)=
\frac{\hbar^2}{2\mathcal J_i}I(I+1)
+(n+\tfrac12)\hbar\omega_w,
\]
其相对激发能在理想谐近似下对 \(n\) 线性。书中强调 \(m=n\) 的数值相同不代表
TiP 转动量子和 wobbling 声子具有相同物理含义。

## Necessary Assumptions

- 统一 \(s,i,l\) 轴和转动惯量/转动常数约定；
- 明确能级是同一自旋的相对激发能，还是不同自旋的实验能量；
- 先完成能级身份、分支、效率和寿命的谱学核查，再计算 \(B(E2)\) 比值；
- 理想声子选择定则只适用于谐近似，TiP 与 wobbling 在高自旋极限可能逐渐接近；
- \(\gamma\neq30^\circ\) 时，TiP 的某些零跃迁不再严格为零；
- Table 6.1 是多项条件性模型比较，不是七维、三点或固定阈值自动分类器；
- 真实核还可能有 \(\gamma\) 振动、旋称伙伴带、构型混合、磁转动或两准粒子耦合。

## Discriminating Observables

### 1. 能量加和与相对激发能

对偶偶核的低自旋测试：
\[
\Delta_{\mathrm{sum}}=
E(2_\mathrm{g}^+)+E(2_\gamma^+)-E(3_\gamma^+).
\]

Lawrie 的解析参考为：

- TiP（\(\gamma=30^\circ\) 解析参考）：\(E(3_\gamma^+)=E(2_\mathrm{g}^+)+E(2_\gamma^+)\)，因此
  \(\Delta_{\mathrm{sum}}\approx0\)；
- wobbling：\(E(3_\gamma^+)<E(2_\mathrm{g}^+)+E(2_\gamma^+)\)，因此
  \(\Delta_{\mathrm{sum}}>0\)。

这是特定惯量、形变和低自旋模型下的关系。它只能说明数据更接近某一参考模型，
不能单独确认 TiP 或 wobbling，也不能排除 \(\gamma\)-soft 和构型混合。

### 2. \(B(E2)\) 比值

定义：
\[
R_{2\gamma/2g}=
\frac{B(E2;2_\gamma^+\rightarrow2_g^+)}
     {B(E2;2_g^+\rightarrow0_g^+)},
\]
\[
R_{3\gamma/2\gamma}=
\frac{B(E2;3_\gamma^+\rightarrow2_\gamma^+)}
     {B(E2;2_g^+\rightarrow0_g^+)}.
\]

在书中给出的 \(20^\circ\le\gamma\le30^\circ\) 模型比较中，\(R_{2\gamma/2g}\)
对 TiP 可落在约 \(0.4\)–\(1.4\) 的范围，而理想 wobbling 参考为零；\(R_{3\gamma/2\gamma}\)
的 TiP 与 wobbling 参考分别约为 \(1.78\) 和 \(1.0\)。这些是模型参考范围，
需要结合 \(\gamma\)、有效电荷、寿命和实验协方差使用。

在 TiP 解析比较中，四极矩先按长轴定义 \(Q_0,Q_2\)，再变换到中间轴：
\[
Q'_0=-\frac12Q_0+\sqrt{\frac32}Q_2,\qquad
Q'_2=\sqrt{\frac38}Q_0+\frac12Q_2.
\]
在 \(\gamma=30^\circ\) 时，部分 TiP 分支因 \(Q'_0=0\) 消失；偏离
\(\gamma=30^\circ\) 后这些分支可以恢复。因此这些零点是特定解析模型的结果，
不是所有三轴核的严格选择定则。

### 3. \(\Delta n=2\) 或 \(\Delta m=2\) 跃迁

理想声子 wobbling 中，改变两个以上声子数的同阶 \(E2\) 跃迁被禁止，例如
\[
B(E2;n\rightarrow n-2)=0.
\]

TiP 的转动重耦合不受同一声子选择定则约束，\(\Delta m=2\) 分支可以非零，某些
分支甚至在低自旋和 \(\gamma\neq30^\circ\) 时较强。因此，实验中应区分理论量子数
\(\Delta n\)、\(\Delta m\) 与仅用于统一带编号的 \(k\)。\(\Delta m=2\) 的观测必须
以绝对 \(B(E2)\)、寿命和分支完整性为基础，不能只用“看见/没看见一条线”判定。

### 4. 高自旋谐近似边界

书中给出高自旋谐近似控制量：
\[
f(n,I)=
(2n+1)\,
\frac{A_s+A_l-2A_i}
{2I\sqrt{(A_s-A_i)(A_l-A_i)}}\ll1.
\]

只有当 \(f(n,I)\) 足够小，三维转动的 TiP 描述才可近似映射为一维转动加声子
wobbling。低自旋时，二次 \(m\) 依赖与线性 \(n\) 依赖的差别必须保留。书中
PDF p.135 的 \(A_i\) 文字定义与前文约定存在内部排印不一致；本 Wiki 采用
\(A_i=\hbar^2/(2\mathcal J_i)\)，并将该处作为原书内部错误记录。

## Supporting Evidence

- Petrache 编著本 Ch. 6，PDF p. 131 / 印刷 p. 112：\(x,y,\alpha\) 与 wobbling
  \(B(E2)\) 关系，Eqs. (6.12)–(6.13)。
- PDF p. 131 / 印刷 p. 112：TiP 哈密顿量与 \(m\) 标记，Eq. (6.14)–(6.15)。
- PDF p. 132 / 印刷 p. 113：图 6.3、能量加和 Eqs. (6.16)–(6.17)；页面图像已核对。
- PDF p. 134 / 印刷 p. 115：\(Q'_0,Q'_2\)、TiP 与 wobbling 的带内/带间
  \(B(E2)\) 差异、\(\Delta m=2\) 与 \(\Delta n=2\) 选择定则；页面图像已核对。
- PDF p. 135 / 印刷 p. 116：高自旋谐近似控制量 \(f(n,I)\)，Eq. (6.22)；页面图像已核对。
- PDF p. 140–141 / 印刷 pp.121–122：横向耦合的 \(B(M1)\) 分支；
- PDF pp.146–148 / 印刷 pp.127–129：实验流程、Table 6.1 的 15 项模型比较、
  \(^{192}\mathrm{Os}\) 和 \(^{163}\mathrm{Lu}\) 适用域；
- PDF p.152 / 印刷 p.133：\(^{135}\mathrm{Pr}\) 两个混合比解及相应
  \(B(E2)_{\rm inter}/B(E2)_{\rm intra}\) 分支。
- 代码接口：`calculate_lawrie_tip_wobbling_metrics` 位于
  `system/scripts/analysis/triaxial_wobbling_tip_chiral_analyzer.py`，返回判据量和
  参考预期，但 `mode_verdict` 固定为 `None`。

## Counter-evidence and Competing Interpretations

- 低自旋的 TiP 能级可能被错误标为 wobbling，尤其当只比较一条带间能量时；
- 高自旋 TiP 与 wobbling 的能量和跃迁行为逐渐接近，单一观测量的区分力下降；
- \(\gamma\) 软性、构型混合和两准粒子耦合可以同时改变能量和 \(B(E2)\)；
- 观测到非零 \(\Delta m=2\) 分支支持 TiP 方向，但不能排除混合模式；
- wobbling 模型本身可以有非零 \(B(M1)\) 分支；M1 主导不能作为脱离组态和
  矩阵元的普遍排除条件；
- 理想声子零跃迁在有限实验灵敏度下可能只是上限，需显式记录检测效率和置信区间。

## What It Can Establish

它可以计算和报告 \(\Delta_{\mathrm{sum}}\)、\(R_{2\gamma/2g}\)、
\(R_{3\gamma/2\gamma}\)、\(\Delta m=2\) 分支是否偏离理想声子参考，以及高自旋
谐近似控制量 \(f(n,I)\)，从而指出数据更接近哪一类模型参考。

## What It Cannot Establish Alone

它不能单独证明某个核素存在 wobbling 或 TiP，也不能替代寿命、混合比、线偏振、
组态、\(\gamma\) 形变和竞争模型比较。`mode_verdict=None` 是有意保留的证据边界。

## Our Current Position

Wiki 采用“判据卡”而非自动分类器：先报告 \(\Delta_{\mathrm{sum}}\)、
\(R_{2\gamma/2g}\)、\(R_{3\gamma/2\gamma}\)、\(\Delta n/\Delta m\) 强度和 \(f(n,I)\)，
再由共同的能级、寿命、混合比、偏振和模型比较建立模式解释。现有函数只生成
可审计指标，不输出“确认 wobbling”或“确认 TiP”。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[petrache-ch5-experimental-wobbling-evidence-contract]]
- [[wobbling-model-common-input-and-evidence-boundary]]
- [[odd-a-wobbling-mode-stability-and-bifurcation]]
- [[nuclear-chirality-and-wobbling-triaxial-foundations]]
- [[davydov-filippov-triaxial-rotor-and-wobbling-dynamics]]
