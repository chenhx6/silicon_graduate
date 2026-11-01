---
type: concept
title: "科里奥利解耦参数a、K=1/2转动带旋称劈裂与Stephens-Simon退耦带动力学"
aliases: [解耦参数a, decoupling parameter, K=1/2转动带, Stephens-Simon退耦带, 旋称劈裂反转]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [decoupling-parameter, coriolis-force, khalf-bands, signature-splitting, nilsson-orbitals, stephens-simon]
---

# 科里奥利解耦参数a、K=1/2转动带旋称劈裂与Stephens-Simon退耦带动力学

## Definition

在轴对称变形核与三轴核中，对于内禀角动量投影量子数 $K = 1/2$ 的奇 $A$ 核转动能带，时间反演简并的两个本征态 $|\Omega = +1/2\rangle$ 与 $|\Omega = -1/2\rangle$ 可以直接通过科里奥利算符的阶梯算符 $j_\pm$ 发生对角相干耦合。

Aage Bohr 与 Ben R. Mottelson 在《Nuclear Structure》Vol. II 第 4 章 §4-3（印刷 pp. 31–34 / PDF pp. 53–56）与第 5 章 §5-3（印刷 pp. 309–311 / PDF pp. 331–333）中给出其严格转动能量本征值公式：
$$E(I) = E_0 + \frac{\hbar^2}{2\mathcal{J}} [ I(I+1) + a (-1)^{I+1/2} (I + 1/2) ]$$
其中 $A = \frac{\hbar^2}{2\mathcal{J}}$ 为有效转动常数（$\text{keV}$），$a$ 为无量纲的**解耦参数（Decoupling Parameter）**。它定义为科里奥利耦合在 $\Omega = 1/2$ 态上的内禀矩阵元：
$$a = -\langle K = 1/2 | j_+ \mathcal{R}_y^{-1}(\pi) | K = 1/2 \rangle = \sum_j (-1)^{j - 1/2} (j + 1/2) |c_j|^2$$
其中 $c_j$ 为 Nilsson 态在球形单粒子基底 $|N, l, j, \Omega = 1/2\rangle$ 上的展开几率振幅。

## Necessary Assumptions

1. **绝热转动-内禀近似（Adiabatic Rotor Approximation）**：假定集体转动的特征角频率远小于单粒子内禀核子在平均场中的激发能，使不同 $K$ 带之间的非对角科氏耦合可在一阶近似下忽略，仅保留 $K=1/2$ 带本身的对角科里奥利微扰项。
2. **轴对称形变与守恒宇称**：假定四极形变为主导，宇称为好量子数，单粒子轨道展开仅包含相同主量子数奇偶性与宇称的基底分量。
3. **刚体/配对转动惯量模型**：转动惯量 $\mathcal{J}$ 假定在低自旋区间保持近似常数；高阶离心伸展效应（$B I^2(I+1)^2$ 修正）在极低自旋下作为微扰项处理。

## Discriminating Observables

### 1. 纯单 $j$ 闯入轨道的理论极限制
对于未发生组态混合的纯单 $j$ 壳层（如高 $j$ 闯入轨道 $h_{11/2}, i_{13/2}$）：
$$a_{\text{pure}}(j) = (-1)^{j - 1/2} (j + 1/2)$$
- $s_{1/2} (j=1/2) \implies a = +1.0$
- $p_{3/2} (j=3/2) \implies a = -2.0$
- $d_{5/2} (j=5/2) \implies a = +3.0$
- $f_{7/2} (j=7/2) \implies a = -4.0$
- $g_{9/2} (j=9/2) \implies a = +5.0$
- $h_{11/2} (j=11/2) \implies a = -6.0$（$A \sim 130$ 质量区关键闯入质子/中子轨道！）
- $i_{13/2} (j=13/2) \implies a = +7.0$（$A \sim 160$ 稀土区关键中子轨道！）

### 2. Stephens-Simon 彻底退耦带现象（Fully Decoupled Bands）
当解耦参数绝对值很大（$|a| \gg 1$，如 $h_{11/2}$ 的 $a = -6.0$ 或 $i_{13/2}$ 的 $a = +7.0$）时：
科里奥利线性项 $a (-1)^{I+1/2} (I + 1/2)$ 的幅度甚至超过了常规转动动能项 $I(I+1)$！
- **有利旋称态（Favored Signature, $\alpha = +1/2$）**：能级受到向下的巨大位移压低；
- **不利旋称态（Unfavored Signature, $\alpha = -1/2$）**：能级被强烈向上抬升；
- **能带能级顺序彻底倒转**：以 $h_{11/2}$ 为例，基带带头不再是自旋 $I = 1/2$，而是自旋 $I = 11/2$ 态被压至最低，形成以 $\Delta I = 2$ 级联辐射连接的退耦序列（$11/2^-, 15/2^-, 19/2^-, \dots$），其能级间隔完全与偶偶核芯（Core）的 $2^+, 4^+, 6^+$ 转动谱重合（F. S. Stephens & R. S. Simon, 1972）！

### 3. 能级交错参量 $S(I)$ 与旋称劈裂
相邻能级跃迁差：
$$\Delta E(I \to I-1) = 2A I [ 1 + a (-1)^{I+1/2} ]$$
交错参量（Staggering Parameter）：
$$S(I) = \frac{E(I) - E(I-1)}{2I} = A [ 1 + a (-1)^{I+1/2} ]$$
当 $|a| > 1$ 时，$S(I)$ 随自旋发生剧烈的正负震荡，成为判定 $K=1/2$ 轨道准粒子纯度与科氏力强度的敏感探针。

### 4. 实验能级的严格线性反演算法
由于 $E(I)$ 关于参数矢量 $\vec{\theta} = [E_0, A, Aa]^T$ 是严格线性的，通过设计矩阵 $X_{i} = [1, I_i(I_i+1), (-1)^{I_i+1/2}(I_i+1/2)]$，可运用正规方程组 $\mathbf{X}^T \mathbf{X} \vec{\theta} = \mathbf{X}^T \vec{E}$ 实行无偏解析线性最小二乘反演：
$$A = \theta_1 = \frac{\hbar^2}{2\mathcal{J}}, \quad a = \frac{\theta_2}{\theta_1}, \quad \mathcal{J} = \frac{1000}{2A}\ \hbar^2/\text{MeV}$$
彻底杜绝非线性拟合中的局部极小陷阱与初始值猜测依赖。

## Supporting Evidence

1. **Bohr & Mottelson Vol. II Table 5-16 标准实验对账**：
   - 稀土核 $^{169}\text{Tm}$ 基态带 $[411\ 1/2]$（实测能级 $0, 8.41, 118.19, 138.93, 332.08, 368.21\text{ keV}$）：
     通过本模块 `invert_khalf_band_parameters` 解析反演，精确得出有效转动常数 $A = 12.350\text{ keV}$（$\mathcal{J} = 40.49\ \hbar^2/\text{MeV}$），解耦参数 $a_{\text{exp}} = -0.743$，与 Bohr & Mottelson 专著 Table 5-16（p. 309）报告的 $a_{\text{obs}} = -0.77$ 高度吻合（残差 RMS 仅 $1.05\text{ keV}$）。
2. **微观单 $j$ 极限界限检验**：
   纯 $h_{11/2}$ 轨道 $a = -6.0$ 精确重现 $I = 11/2$ 最低带头与退耦带动力学；纯 $i_{13/2}$ 轨道 $a = +7.0$ 准确给出稀土中子带的旋称大劈裂。
3. **单元回归测试支持**：
   `system/tests/test_decoupling_parameter_khalf.py` 全部 4 项测试 100% 验证通过。

## Counter-evidence and Competing Interpretations

- **大形变区组态混合对 $a$ 的剧烈稀释**：
  对于非高 $j$ 侵入轨道（如 $[411\ 1/2]$ 或 $[521\ 1/2]$），波函数是由多个不同 $l, j$ 谐振子态相干叠加而成的。例如在 $^{171}\text{Lu}$ 的 $[541\ 1/2]$ 轨道中，实验测得 $a \approx +4.0 \sim +7.0$，而纯 $h_{9/2}$ 理论值仅为 $-5.0$，这一剧烈符号偏转源于 $h_{9/2}$ 与高位 $h_{11/2}$ 轨道的强烈跨壳四极混合与大形变导数 $da/d\delta \approx -10$（Bohr & Mottelson Vol. II p. 310）。因此，实测 $a$ 偏离纯单粒子值是测定核四极形变 $\beta_2$ 与组态纯度的重要依据。
- **非轴对称三轴形变（$\gamma \ne 0^\circ$）的影响**：
  在具有显著三轴形变的核（如 $A \sim 130$ 的铈、钕、镨同位素）中，轴对称 $K$ 量子数彻底破缺，转动惯量沿着三个主轴发生分立，退耦带演化为三维进动的横向摆动带（Transverse Wobbling）或倾斜轴推转带（TAC），此时单纯的轴对称 $K=1/2$ 能量公式退化为近似描述。

## Our Current Position

本 Wiki 将解耦参数 $a$ 及其严格线性回归反演作为奇 $A$ 核单粒子能带结构鉴定的基石工具。在在束实验数据分析中：
1. 建立由 `decouple` 命令自动反演能带 $(A, a, \mathcal{J})$ 的标准化工作流；
2. 当发现某奇 $A$ 能带的实测 $a$ 接近整数或具有反常大负值时，优先检验其是否对应为 $h_{11/2}$ 或 $i_{13/2}$ 闯入轨道的退耦带结构。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：Bohr & Mottelson, *Nuclear Structure*, Vol. II, §4-3（pp. 31–34）与 §5-3（pp. 309–311, Table 5-16）。
- [[book-lu-nuclear-physics-chinese]]：卢希庭《原子核物理（修订版）》第 8 章 §8.5。
- [[coriolis-attenuation-and-quasiparticle-band-crossing]]：科里奥利力非对角矩阵元衰减机制。

## Evolution Log

- 2026-11-02：建立本概念专论。实现单 $j$ 轨道解耦参数代数解析与实验 $K=1/2$ 能级三参数线性正规方程组无偏反演，以 $^{169}\text{Tm}$ 实验数据严格对账 Bohr & Mottelson 表 5-16。
