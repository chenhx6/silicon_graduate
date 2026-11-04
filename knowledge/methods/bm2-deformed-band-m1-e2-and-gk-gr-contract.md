---
type: method
title: "Bohr & Mottelson Vol. II：形变核带内 M1/E2 跃迁、磁退耦参数 b 与 |g_K - g_R| 反演合同"
aliases: [BM2 deformed band M1 E2, BM2 Section 4-3c M1 matrix elements, magnetic decoupling parameter b, gK - gR extraction from B(M1)/B(E2), rotational magnetic moments]
method_type: "rotational-electromagnetic-spectroscopy-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Bohr & Mottelson Nuclear Structure Vol. II, Section 4-3c (printed pp.54-58 / PDF pp.76-80), Section 5-3b, and Table 4-7 to 4-10"
confidence: "high for analytical formulas, Clebsch-Gordan algebraic relations, and experimental B(M1)/B(E2) branching inversions"
tags: [bohr-mottelson, vol2, m1-matrix-elements, e2-matrix-elements, gk-factor, gr-factor, magnetic-decoupling, branching-ratios, in-beam-spectroscopy]
sources: [book-bohr-mottelson-nuclear-structure-vol2]
---

# Bohr & Mottelson Vol. II：形变核带内 M1/E2 跃迁、磁退耦参数 b 与 |g_K - g_R| 反演合同

## Purpose

本方法合同基于 Aage Bohr 与 Ben R. Mottelson 的巨著《Nuclear Structure》第二卷第 4 章 §4-3c 的系统研究，
解决轴对称形变原子核在束 \(\gamma\) 谱学中通过能带退激分支比与多极混合比反演内禀单粒子结构（回旋比 \(g_K\)）与核芯集体转动结构（集体回旋比 \(g_R\)）的理论与实验对账难题：
通过将磁偶极矩算符因式分解为核芯集体转动项与内禀核子投影项，
严格推导任意自旋能态的静态磁矩公式 \(\mu(I)\)、带内减缩磁偶极跃迁几率 \(B(M1; I \to I-1)\) 以及 \(K=1/2\) 带特有的磁退耦参数 \(b\)（Magnetic Decoupling Parameter），
联合带内强集体电四极跃迁几率 \(B(E2; I \to I-2)\) 建立模型无关的在束 **\(B(M1)/B(E2)\) 实验比值反演方程**，
为形变核单核子组态指认、费米面位置判定及核子顺排提供决定性实验判据：

1. **磁矩矢量算符因式分解定理（式 4-84）**：在强耦合强形变极限下，总磁矩矢量严格分解为核芯集体部分与沿对称轴的内禀部分：\(\vec\mu = g_R \vec I + (g_K - g_R) \vec K\)；
2. **带内磁偶极跃迁解析公式（式 4-85–4-87）**：
   - 对 \(K > 1/2\) 能带：\(B(M1; I \to I-1) = \frac{3}{4\pi} \mu_N^2 \langle I K 1 0  \vert I-1 K  \rangle^2 (g_K - g_R)^2 K^2\)；
   - 对 \(K = 1/2\) 能带：引入内禀磁跃迁张量与退耦相位项，导出含有磁退耦参数 \(b\) 的特征交错公式：
     \[
     B(M1; I \to I-1) = \frac{3}{4\pi} \mu_N^2 \frac{1}{4} \frac{2I-1}{2I} (g_K - g_R)^2 \left[ 1 + (-1)^{I+1/2} b \right]^2
     \]
3. **静态磁偶极矩公式（式 4-88）**：
   - 对 \(K > 1/2\)：\(\mu(I) = g_R I + (g_K - g_R) \frac{K^2}{I+1}\)；
   - 对 \(K = 1/2\)：\(\mu(1/2, I) = g_R I + \frac{g_K - g_R}{4(I+1)} [1 + (2I+1)(-1)^{I+1/2} b]\)；
4. **在束谱学 \(B(M1)/B(E2)\) 实验比值反演法典**：联合 Alaga 带内 \(E2\) 几率，建立直接从实测 \(\gamma\) 射线强度比与多极混合比 \(\delta(E2/M1)\) 提取 \(|g_K - g_R|/Q_0\) 的标准分析方法。

---

## Inputs and Assumptions

### 1. 轴对称强耦合绝热近似

核内禀运动具有轴对称反射不变性（好量子数 \(K = \Omega\)），核芯转动惯量足够大，满足绝热条件：转动频率 \(\omega_{\rm rot}\) 远低于单粒子内禀激发能。
核芯有效电四极矩 \(Q_0\) 与集体回旋比 \(g_R\) 在同一转动能带内近似视为常数。

### 2. 多极算符球张量表示

磁多极算符为一阶张量算符 \(\mathcal{M}(M1, \mu) = \sqrt{\frac{3}{4\pi}} \mu_N \mu_\mu\)。
电四极算符为二阶球张量算符，内禀分量由集体四极矩主导：\(\mathcal{M}(E2, \nu=0) = \sqrt{\frac{5}{16\pi}} e Q_0\)。

---

## What It Can Establish

### 1. 带内 \(M1\) 跃迁减缩几率显式解（式 4-85–4-87）

根据 Wigner-Eckart 定理与 Clebsch-Gordan 系数展开：
- 对于 \(K > 1/2\) 的非简并轴对称带：
  \[
  B(M1; I \to I-1) = \frac{3}{4\pi} \mu_N^2 \frac{K^2 (I^2 - K^2)}{I (2I+1)} (g_K - g_R)^2
  \]
  跃迁几率与自旋呈平滑单调演化，直接正比于因子 \((g_K - g_R)^2\)；
- 对于 \(K = 1/2\) 奇 \(A\) 带：
  由于时间反演相伴态 \(\Omega = -1/2\) 与 \(\Omega = +1/2\) 被一阶张量算符的非对角分量耦合，引入内禀磁退耦参数 \(b\)（式 4-86）：
  \[
  (g_K - g_R) b \equiv -\sqrt{2} \langle K=1/2  \vert \mathcal{M}(M1, \nu=+1)  \vert \overline{K=1/2}  \rangle
  \]
  由此诱发 \(B(M1)\) 强烈的**自旋奇偶交错（Odd-Even Staggering）**：
  当 \(b > 0\) 时，某一签名分支跃迁被极大增强，而相间分支跃迁被强烈压制。

### 2. 静态磁偶极矩解析定理（式 4-88）

在实验室系最高取向状态 \(M=I\) 下，磁偶极矩由矢量代数给出：
- 当 \(K > 1/2\)：
  \[
  \mu(I) = \frac{1}{I+1} \left[ g_R I(I+1) + (g_K - g_R) K^2 \right] = g_R I + (g_K - g_R) \frac{K^2}{I+1}
  \]
  在基态 \(I=K\) 处简化为：\(\mu(I=K) = \frac{K}{K+1} (g_K K + g_R)\)；
- 当 \(K = 1/2\)：
  \[
  \mu(I, K=1/2) = g_R I + \frac{g_K - g_R}{4(I+1)} \left[ 1 + (2I+1) (-1)^{I+1/2} b \right]
  \]
  展现出由磁退耦参数 \(b\) 驱动的锯齿状签名分裂。

### 3. 在束谱学 \(B(M1)/B(E2)\) 比值与结构反演法典

在同一能带内，激发态 \(I\) 可以通过两条竞争通道退激：
1. 跨越 1 个能级的带内电四极跨跃（Crossover）：\(I \to I-2\)（纯 \(E2\) 跃迁）；
2. 级联退激至相邻能级（Cascade）：\(I \to I-1\)（混合 \(M1 + E2\) 跃迁，多极混合比为 \(\delta\)）。

其实测实验分支比由 \(\gamma\) 射线探测强度 \(I_\gamma\) 给出：
\[
\frac{T_\gamma(M1; I \to I-1)}{T_\gamma(E2; I \to I-2)} = \frac{I_\gamma(I \to I-1)}{I_\gamma(I \to I-2)} \frac{1}{1 + \delta^2(E2/M1)}
\]
根据电磁跃迁速率关系 \(T(M1) \propto E_\gamma^3 B(M1)\) 与 \(T(E2) \propto E_\gamma^5 B(E2)\)，导出理论比值公式（\(K > 1/2\)）：
\[
\frac{B(M1; I \to I-1)}{B(E2; I \to I-2)} = 0.697 \cdot \frac{K^2 (2I-1)}{(I-1)(I+K)(I-K)} \cdot \left( \frac{g_K - g_R}{Q_0} \right)^2 \quad \left[ \frac{\mu_N^2}{e^2 \text{b}^2} \right]
\]
式中 \(E_\gamma\) 以 MeV 为单位，电四极矩 \(Q_0\) 以靶恩（\(e\text{b}\)）为单位。
该公式建立了核结构实验中提取物理参量 \(|g_K - g_R|/Q_0\) 的金标准，直接用于：
- 区分质子轨道（\(g_K > g_R\)，如 \(h_{11/2}\) 质子 \(g_K \sim 1.2\)）与中子轨道（\(g_K < g_R\)，如 \(h_{11/2}\) 中子 \(g_K \sim -0.2\)）；
- 判定高自旋下转动对齐粒子性质（破偶核子属于质子还是中子对）。

---

## What It Cannot Establish Alone

1. **不能单凭 \(B(M1)/B(E2)\) 分离 \(g_K - g_R\) 的正负符号**：
   由于跃迁比率只包含差值的平方 \((g_K - g_R)^2\)，符号的确定必须依赖多极混合比 \(\delta(E2/M1)\) 的精确符号测量（如通过角分布系数 \(a_2\) 或 DCO 椭圆判别）；
2. **无法自动排除非绝热 Coriolis 混合与三轴形变**：
   公式假定纯轴对称单带（单一 \(K\)）。在三轴形变核或低 \(K\) 闯入轨道（如 \(h_{11/2}\) 最低能级）中，强 Coriolis 力使不同 \(K\) 组态剧烈混合（\(K\)-mixing），此时必须采用全微观 PTRM、TPSM 或 TAC-CDFT 进行重整化；
3. **集体转动回旋比 \(g_R\) 存在超流配对差异**：
   刚体转动估计通常假定 \(g_R \a\a\approx pprox Z/A \a0.4\)。但由于质子配对能隙与中子配对能隙存在细微差异（\(\Delta_p \ne \Delta_n\)），真实核芯的 \(g_R\) 系统性偏小（\(g_R \a0.30 - 0.35\)），高精度结构分析需结合微观推转计算或 \(2_1^+\) 态直接 \(g\) 因子测量。

---

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：A. Bohr & B. R. Mottelson, *Nuclear Structure*, Vol. II: *Nuclear Deformations*, W. A. Benjamin (1975) / World Scientific (1998), Chapter 4 §4-3c (pp. 54–58), Chapter 5 §5-3b, Tables 4-7 to 4-10.
- [[electromagnetic-transition-rates-weisskopf-and-alaga-rules]]：原子核电磁跃迁几率、Weisskopf 单粒子估计与形变核 Alaga 分支规则法典。
- [[bm2-rotational-intrinsic-coupling-and-mikhailov-contract]]：BM-II §4-4 转动与内禀运动耦合合同（\(\Delta K=2\) Mikhailov 展开式与 Alaga 偏离）。
- [[nilsson-magnetic-moments-and-gk-inversion]]：Nilsson 模型单粒子内禀磁矩、\(g_K\) 因子与在束 \(B(M1)/B(E2)\) 反演法典。
