---
type: concept
title: "Wigner超多重态SU(4)对称性、Casimir不变量与N=Z质量尖点维格纳能动力学"
aliases: [Wigner超多重态, SU(4)对称性, Casimir不变量, 维格纳能, Wigner Cusp, N=Z质量尖点, 同标量对能, 质子中子配对, 质量公式修正]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [wigner-supermultiplet, su4-symmetry, casimir-invariants, wigner-energy, mass-cusp, n-equals-z, pn-pairing, nuclear-masses]
---

# Wigner超多重态SU(4)对称性、Casimir不变量与N=Z质量尖点维格纳能动力学

## 1. 物理全景：经典液滴质量公式的尖点偏离与自旋-同位旋统一

在宏观核物理模型中，Bethe-Weizsäcker 经典液滴质量公式将核对称能简单描述为同位旋非对称度（$N-Z$）的光滑二次抛物线项：
$$E_{\text{sym}}(A, T) = - a_{\text{sym}} \frac{(N - Z)^2}{A} = - 4 a_{\text{sym}} \frac{T_z^2}{A}$$
根据该平滑抛物线假定，结合能对同位旋的导数在 $N = Z$（$T_z = 0$）处应平滑地等于零。
然而，精确的高精度原子核质量测量（AME 数据集）无可辩驳地揭示出一个普适的惊人反常：
**核质量曲面在 $N = Z$ 处呈现出一个尖锐的、非微商平滑的“尖点”（Wigner Cusp），自共轭核（Self-conjugate nuclei）的实测结合能比液滴模型抛物线外推值系统性高出数个 MeV！**

根据 E. P. Wigner（Phys. Rev. 51, 106, 1937）、A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. I（第 1 章）以及 W. Satuła 等（Phys. Lett. B 407, 103, 1997）：
这一额外的宏观结合能被称为**维格纳能（Wigner Energy, $E_W$）**。
其根本微观物理源头由两大对称性基石支撑：
1. **Wigner $SU(4)$ 自旋-同位旋超多重态对称性（Supermultiplet Symmetry）**：
   在轻中质量核（$A \le 100$）中，核力的空间交换力强于自旋-轨道耦合力，核子在自旋空间（$S=1/2$）与同位旋空间（$T=1/2$）的 4 个本征态 $|p\uparrow, p\downarrow, n\uparrow, n\downarrow\rangle$ 组合成庞大的 $SU(4)$ 群表象。空间对称配对使得具有最大空间对称性的超多重态基态获得巨大的结合能收益；
2. **同标量（$T=0, S=1$）质子-中子配对关联（Isoscalar $p-n$ Pairing）**：
   在 $N \approx Z$ 核中，未配对的价质子与价中子以极高的几率占据**完全相同的单核子空间轨道**。除了传统的同矢量配对（$T=1, S=0$）外，同标量类氘核配对（$T=0, S=1$）释放了巨大的重叠吸引势能，这正是维格纳能的现代微观多体本质！

---

## 2. 严格物理公式与代数推导

### (1) Wigner $SU(4)$ 代数与 Casimir 不变量
群 $SU(4)$ 具有 15 个生成元：
- 3 个自旋算符：$S_i = \frac{1}{2} \sum_k \sigma_i(k)$；
- 3 个同位旋算符：$T_a = \frac{1}{2} \sum_k \tau_a(k)$；
- 9 个联合自旋-同位旋算符：$Y_{ia} = \frac{1}{2} \sum_k \sigma_i(k) \tau_a(k)$。

系统的二次 Casimir 算符为各生成元二次代数求和：
$$\hat{C}_2(SU(4)) = \sum_i S_i^2 + \sum_a T_a^2 + \sum_{i, a} Y_{ia}^2$$
在由 Young 氏图分割量子数 $[P, P', P'']$ 标定的不可约表示中，其本征期望值为：
$$\langle \hat{C}_2(SU(4)) \rangle = \frac{1}{2} \left[ P(P + 4) + P'(P' + 2) + P''^2 \right]$$

---

### (2) 各类核素基态的 Wigner 分割数 $[P, P', P'']$
受泡利原理与空间对称性最大化约束，核素基态的 Casimir 算符数值严格离散化：
1. **偶偶核（Even-Even, $T = |N - Z|/2$）**：
   分割数为 $[P, P', P''] = [T, 0, 0]$：
   $$\langle C_2 \rangle = \frac{1}{2} T(T + 4)$$
   特别地，在 $N = Z$ 偶偶核（如 $^{12}\text{C}, ^{16}\text{O}, ^{40}\text{Ca}, ^{48}\text{Cr}$）中，$T = 0 \implies \langle C_2 \rangle = 0$；
2. **奇 $A$ 核（Odd-$A$）**：
   分割数为 $[P, P', P''] = [T, 1/2, \pm 1/2]$：
   $$\langle C_2 \rangle = \frac{1}{2} T(T + 4) + \frac{3}{4}$$
3. **自共轭奇奇核（$N = Z, T = 0$）**：
   空间高度对称的类氘核态，具有自旋三重态（$S=1$），其分割数为 $[P, P', P''] = [1, 0, 0]$：
   $$\langle C_2 \rangle = \frac{1}{2} \times 1 \times (1 + 4) = 2.50$$
4. **一般奇奇核（Odd-Odd, $N \ne Z$）**：
   分割数为 $[P, P', P''] = [T, 1, 0]$：
   $$\langle C_2 \rangle = \frac{1}{2} T(T + 4) + 1.50$$

---

### (3) 维格纳能 $E_W(A, T)$ 的解析与唯象形式
1. **微观超多重态能**：
   结合能贡献正比于 Casimir 不变量：
   $$E_W(A, T) = \frac{a_W}{A} \langle C_2(SU(4)) \rangle$$
   其中能量系数 $a_W \approx 35 \sim 47\text{ MeV}$；
2. **经验线性绝对值尖点形式（The Cusp Term）**：
   为了在宏观-微观质量模型（如 FRDM、WS4、HFB）中准确拟合结合能，通常将维格纳能参数化为对不对称度的直接线性依赖：
   $$E_W(A, |N - Z|) = \frac{W_0}{A} |N - Z| + \delta_{N, Z} \Delta E_d$$
   正是绝对值函数 $|N - Z|$ 在 $N = Z$ 处的不可微导数突变，在理论上自洽重现了实验测量到的“质量尖顶”！

---

## 3. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/wigner_supermultiplet_su4_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `wigner` 命令。

### 运行示范（以 $A=48$ 同质异位素链扫描为例揭示 $N=Z$ 尖点）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py wigner -Z 24 -A 48 --scan-isobar --json
```

### 计算输出核心物理特征：
1. **自共轭核基态识别**：$^{48}\text{Cr}$（$Z=N=24$）具有同位旋 $T=0$，偶偶对称态 $\langle C_2 \rangle = 0$；
2. **同量异位素链 $A=48$ 质量尖点剖面**：
   - 当偏离 $N=Z$（如 $^{48}\text{V}$ 的 $|N-Z|=2, T=1$）时，微观 Wigner 能迅速上升至 $3.50\text{ MeV}$；
   - 当中子过剩增至 $|N-Z|=8$（$^{48}\text{Ca}, T=4$）时，Wigner 能飙升至 $14.00\text{ MeV}$；
   - 在 $|N-Z|=12$（$^{48}\text{Ar}, T=6$）处达到 $26.25\text{ MeV}$；
   - 展现出完美的 $V$ 字形尖点轮廓，彻底阐明了开壳层自共轭核中额外束缚能的代数对称性根基！

---

## 4. 与相关前沿概念的交叉引用
- [[isobaric-analog-states-and-coulomb-energy-differences]]：同位旋类似态（IAS）的同位旋多重态能量在扣除电磁库仑项后，基底完全由此处 $SU(4)$ 体系维格纳能支配；
- [[two-nucleon-transfer-pairing-vibrations-and-josephson-dynamics]]：自共轭核之间的双核子转移反应（如 $(p, t)$ 与 $(^3\text{He}, p)$）正是探测同标量 $T=0$ 对能的重要工具。
