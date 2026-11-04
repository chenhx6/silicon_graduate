---
type: method
title: "Bohr & Mottelson Vol. II：转动与内禀运动耦合、Coriolis 带混合与 Mikhailov 展开合同"
aliases: [BM2 rotational intrinsic coupling, BM2 Section 4-4 band mixing, Mikhailov formula E2, delta K=2 gamma-ground mixing, Coriolis delta K=1 Inglis cranking]
method_type: "rotational-intrinsic-coupling-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Bohr & Mottelson Nuclear Structure Vol. II, Section 4-4 (printed pp.145-174 / PDF pp.167-196)"
confidence: "high for analytical canonical transformations, Mikhailov formulas, and 166Er/175Lu experimental examples"
tags: [bohr-mottelson, vol2, band-mixing, coriolis-coupling, mikhailov-formula, gamma-vibration, alaga-deviation, inglis-cranking, 166er, 175lu]
sources: [book-bohr-mottelson-nuclear-structure-vol2]
---

# Bohr & Mottelson Vol. II：转动与内禀运动耦合、Coriolis 带混合与 Mikhailov 展开合同

## Purpose

本方法合同基于 Aage Bohr 与 Ben R. Mottelson 的巨著《Nuclear Structure》第二卷第 4 章 §4-4 的系统研究，
解决轴对称与微小非轴对称原子核中绝热假定破缺、转动带与内禀振动能态耦合、Alaga 分支比实验系统性偏离以及转动惯量微观起源的理论难题：
通过引入规范幺正变换（Canonical transformation）将转动–内禀耦合算符微扰对角化，
严格建立 \(\Delta K = 1\) Coriolis 耦合、\(\Delta K = 2\) \(\gamma\) 振动带间耦合与 \(\Delta K = 0\) 离心拉伸耦合的解析矩阵元理论，
导出著名的带间电四极跃迁 **Mikhailov 展开公式**，定量解释形变核中基态带与 \(\gamma\) 振动带间跃迁对 Alaga 规则的系统性偏离，
并严格推导核芯转动惯量的微观 Inglis 推转公式：

1. **转动与内禀微扰混合规范变换算符（式 4-200–4-203）**：通过生成元 \(S = -i(h_{+1} I_- + \mathcal{R}\text{-conj.})\) 实施波函数与跃迁算符的幺正变换，解析推导诱发电磁多极算符修正项 \(\delta\mathcal{M} = i[S, \mathcal{M}]\)；
2. **\(\Delta K = 2\) 带混合与 Mikhailov 公式（式 4-206–4-211、4-230）**：在基态带（\(K=0\)）与 \(\gamma\) 振动带（\(K=2\)）之间引入有效耦合 \(H_2 = \frac{1}{2}(h_{+2} I_-^2 + h_{-2} I_+^2)\)，严格导出含有混合参量 \(z_\gamma\) 的电四极跃迁几率公式：
   \[
   B(E2; K=2, I_i \to K=0, I_f) = 2 M_1^2 \langle I_i 2 2 -2  \vert I_f 0  \rangle^2 \left[ 1 + a_2 (I_f(I_f+1) - I_i(I_i+1)) \right]^2
   \]
3. **\(^{166}\mathrm{Er}\) 经典实验对账（图 4-29、4-30）**：系统解释实测分支比 \(B(E2; 2_\gamma \to 0_g)/B(E2; 2_\gamma \to 2_g)\) 从 Alaga 理想值 0.700 向 0.50 显著压低的物理本质，反演转动–振动耦合矩阵元 \(\epsilon_2\)；
4. **\(\Delta K = 1\) Coriolis 耦合与 Inglis 推转转动惯量微观重整化（式 4-204–4-205）**：将二阶 Coriolis 带混合在能量中的二次自旋项展开，解析证明其等价于单粒子在外场中受迫转动的 Inglis 推转模型转动惯量公式 \(\mathcal{J} = 2\hbar^2 \sum_\nu \frac{|\langle \nu \vert j_x \vert 0 \rangle|^2}{E_\nu - E_0}\)；
5. **\(\Delta K = 0\) 离心畸变与配对淬灭**：推导可变转动惯量（VMI）模型中四阶自旋项 \(B I^2(I+1)^2\) 的微观耦合来源。

---

## Inputs and Assumptions

### 1. 绝热分离与微扰展开条件

内禀激发能 \(\Delta E_{\rm int} = E(K_2) - E(K_1)\) 显著大于转动特征能隙 \(\hbar\omega_{\rm rot} = \frac{\hbar^2}{\mathcal{J}} I\)：
\[
\frac{\hbar\omega_{\rm rot}}{\Delta E_{\rm int}} \ll 1
\]
这保证了带混合可以作为小参数执行微扰展开，未受扰态由好量子数 \(\vert K I M\rangle\) 标记。

### 2. 内禀四极矩近似相等

在计算带间 \(E2\) 矩阵元时，基态带与 \(\gamma\) 振动带（或被混合带）的内禀电四极矩假定近似相等：
\[
Q_0(K=2) \approx Q_0(K=0) \equiv Q_0
\]
高阶形变差异由更高阶自旋乘积吸收。

---

## What It Can Establish

### 1. 规范变换与算符有效展开（式 4-200–4-203）

带混合态波函数表示为基底态的微扰叠加：
\[
|\widetilde{K I M}\rangle = e^{-iS} \vert K I M\rangle \approx \vert K I M\rangle - i S \vert K I M\rangle
\]
跃迁算符在微扰表象下的有效算符展开为：
\[
\mathcal{M}_{\rm eff} = e^{iS} \mathcal{M} e^{-iS} = \mathcal{M} + i[S, \mathcal{M}] - \frac{1}{2} [S, [S, \mathcal{M}]] + \dots
\]
该变换避免了直接求解无穷维耦合微分方程组，将多带混合效应严整地浓缩为具有明确张量阶数的修正项。

### 2. \(\Delta K = 2\) 耦合与 Mikhailov 展开公式（式 4-206–4-211、4-230）

在四极形变空间中，\(\gamma\) 振动（\(K=2\)）与基带（\(K=0\)）通过转动惯量对 \(\gamma\) 自由度的依赖产生有效耦合：
\[
H_2 = \frac{1}{2} (h_{+2} I_-^2 + h_{-2} I_+^2)
\]
规范变换算符为 \(S = -i(h_{+2} I_-^2 + \mathcal{R}\text{-conj.}) / \Delta E\)。
由此导出的微扰波函数为：
\[
\begin{aligned}
|\widetilde{K=0, I}\rangle &\approx |K=0, I\rangle - \epsilon(I) |K=2, I\rangle \\
|\widetilde{K=2, I}\rangle &\approx |K=2, I\rangle + \frac{1}{2} \epsilon(I) [1 + (-1)^I] |K=0, I\rangle
\end{aligned}
\]
其中自旋依赖的微扰混合振幅严格满足：
\[
\epsilon(I) = \epsilon_2 \sqrt{2(I-1)I(I+1)(I+2)}, \quad \epsilon_2 = \frac{\langle K=2  \vert h_{+2}  \vert K=0  \rangle}{E(K=2) - E(K=0)}
\]
电四极跃迁减缩矩阵元解析表示为（Mikhailov 展开）：
\[
\langle K=2, I_i || \mathcal{M}(E2) || K=0, I_f \rangle = \sqrt{2} \langle I_i 2 2 -2  \vert I_f 0 \rangle \left[ M_1 + M_2 (I_f(I_f+1) - I_i(I_i+1)) \right]
\]
其中 \(M_1\) 是内禀跃迁矩阵元，\(M_2 = \epsilon_2 \sqrt{\frac{5}{16\pi}} e Q_0\) 是由带内强集体转动四极矩混入产生的相干修正项。

### 3. Alaga 规则偏离的定量修正（式 4-230–4-231）

定义无量纲带混合参量 \(z_\gamma \equiv \frac{2a_2}{1 - 4a_2}\)（其中 \(a_2 = -M_2/M_1\)）：
跨带 \(B(E2)\) 分支比为：
\[
\frac{B(E2; I_\gamma \to I_{g1})}{B(E2; I_\gamma \to I_{g2})} = \frac{\langle I_\gamma 2 2 -2  \vert I_{g1} 0  \rangle^2}{\langle I_\gamma 2 2 -2  \vert I_{g2} 0 \rangle^2} \left[ \frac{1 + a_2 (I_{g1}(I_{g1}+1) - I_\gamma(I_\gamma+1))}{1 + a_2 (I_{g2}(I_{g2}+1) - I_\gamma(I_\gamma+1))} \right]^2
\]
以 \(2_\gamma^+ \to 0_g^+\) 与 \(2_\gamma^+ \to 2_g^+\) 跃迁为例：
Alaga 规则的非微扰几何比率为 \(\langle 2 2 2 -2  \vert 0 0  \rangle^2 / \langle 2 2 2 -2  \vert 2 0  \rangle^2 = 1 / (10/7) = 0.700\)。
代入 Mikhailov 修正因子：
\[
\frac{B(E2; 2_\gamma \to 0_g)}{B(E2; 2_\gamma \to 2_g)} = 0.700 \cdot (1 - 6 a_2)^2 \a0.700 \cdot (1 - 6 z_\gamma)
\]
在 \(^{166}\mathrm{Er}\) 中，实测值约为 \(0.50\pm0.02\)，由该公式反演出 \(z_\gamma \a0.045\)，完美自洽地再现了全部高自旋激发态（\(I = 2, 3, 4, 5, 6, 7, 8\)）的实验分支比曲线（图 4-30）。

### 4. \(\Delta K = 1\) Coriolis 耦合与 Inglis 推转公式等价性（式 4-204–4-205）

对于由单粒子轨道诱发的 \(\Delta K = 1\) Coriolis 耦合 \(H_1 = -A_{\rm rot} (I_+ j_- + I_- j_+)\)：
在二阶微扰下引起的基态能级移动为：
\[
\Delta E(I) = -\sum_\nu \frac{|\langle \nu  \vert H_1  \vert 0  \rangle|^2}{E_\nu - E_0} = -A_{\rm rot}^2 I(I+1) \sum_\nu \frac{|\langle \nu  \vert j_x  \vert 0  \rangle|^2}{E_\nu - E_0}
\]
将这一修正等效吸收进有效转动能量 \(E_{\rm rot} = \frac{\hbar^2}{2\mathcal{J}_{\rm eff}} I(I+1)\) 中，
微观导出转动惯量的二阶重整化项：
\[
\delta \mathcal{J} = 2\hbar^2 \sum_\nu \frac{|\langle \nu  \vert j_x  \vert 0  \rangle|^2}{E_\nu - E_0}
\]
严格证明微扰带混合图像在多体极限下与外部约束旋转的 Inglis 推转模型（Cranking Model）完全等价。

---

## What It Cannot Establish Alone

1. **微扰有效性受高自旋带交叉强烈限制**：
   Mikhailov 展开式假定混合振幅 \(\epsilon(I) \ll 1\)。在高自旋区（如 \(I \ge 12\hbar\)），当 Coriolis 力驱动高 \(j\) 准粒子对齐或发生回弯（Backbending）带交叉时，能级近简并导致微扰级数发散，必须采用非微扰全矩阵对角化（CSM 或 PTRM）；
2. **无法直接给出无偏内禀跃迁几率 \(M_1\)**：
   \(M_1\) 强烈依赖微观核芯的 \(\gamma\) 振动集体性（声子多体波函数重叠），必须由微观 QRPA 或 5D 玻尔哈密顿量提供；
3. **不能排除 \(\Delta K = 1\) 奇宇称带对 \(M_2\) 的潜在相干污染**：
   虽然 \(M_2\) 主要由 \(\Delta K=2\) 的核芯形变产生，但如果低激发能区存在微弱的八极关联或低能 \(1^+\) 剪刀模，可能通过两步 Coriolis 耦合引入附加的自旋项。

---

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：A. Bohr & B. R. Mottelson, *Nuclear Structure*, Vol. II: *Nuclear Deformations*, W. A. Benjamin (1975) / World Scientific (1998), Chapter 4 §4-4 (pp. 145–174) & Appendix 4A (pp. 199–210).
- [[bm2-particle-rotor-adiabatic-coriolis-contract]]：BM-II 附录 4A 轴对称粒子–转子绝热基与非绝热 Coriolis 耦合合同。
- [[electromagnetic-transition-rates-weisskopf-and-alaga-rules]]：原子核电磁跃迁几率、Weisskopf 单粒子估计与形变核 Alaga 分支规则法典。
- [[gamma-vibrational-band-mixing-and-mikhailov-z-gamma-parameter]]：\(\gamma\) 振动带间耦合、Mikhailov 参数 \(z_\gamma\) 与 Alaga 分支比偏离计算法典。
