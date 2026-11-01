---
type: concept
title: "原子核均方电荷半径、激光同位素移动（Isotope Shifts）与King图线性检验法典"
aliases: [电荷半径, 均方电荷半径, 同位素移, Isotope Shift, King图, King Plot, 场移, 质量移, 激光光谱学, 电荷半径奇偶交错]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [charge-radii, isotope-shift, king-plot, field-shift, mass-shift, laser-spectroscopy, odd-even-staggering, shape-evolution]
---

# 原子核均方电荷半径、激光同位素移动（Isotope Shifts）与King图线性检验法典

## 1. 物理全景：原子光学超精细跃迁对原子核体积与形变的直接映射

原子核均方电荷半径 $\langle r^2 \rangle$ 是低能核结构中极少数完全不依赖特定核模型假设、可由高精度原子光学光谱学或电子弹性散射绝对测定的宏观基本物理量。

在共线激光光谱（Collinear Laser Spectroscopy, CLS）与共振电离激光光谱（CRIS）实验中，通过测量同位素链不同核素原子能级跃迁频率的微小差频——**同位素移动（Isotope Shift, $\delta \nu^{A, A'} = \nu^A - \nu^{A'}$）**，能够以极其优异的精度（达到 $10^{-4}\text{ fm}^2$）反演核电荷半径随中子数的微观演化！

根据 W. H. King《Isotope Shifts in Atomic Spectra》（1984）、I. Angeli & K. P. Marinova (ADNDT 99, 69, 2013)、P. Ring《Relativistic Mean Field Theory》与卢希庭《原子核物理（修订版）》（第 1 章）：
1. **光学同位素移动物理分解**：
   $$\delta \nu_i^{A, A'} = \delta \nu_{i, \text{MS}}^{A, A'} + \delta \nu_{i, \text{FS}}^{A, A'} = (M_i + S_i) \mu_{A, A'} + F_i \cdot \delta \langle r^2 \rangle^{A, A'}$$
   - **质量移（Mass Shift, MS）**：由有限核质量反冲动能产生，包含正常质量移（NMS，$M_i = \nu_0 m_e / M_u$）与电子动量关联特殊质量移（SMS，$S_i$），正比于质量倒数差 $\mu_{A, A'} = \frac{m_A - m_{A'}}{m_A m_{A'}}$；
   - **场移（Field Shift, FS）**：**直接包含原子核结构信息的核心部分**！电子波函数在核体积内的有限空间电荷分布产生的库仑势摄动，严格正比于原子核均方电荷半径差 $\delta \langle r^2 \rangle^{A, A'} = \langle r^2 \rangle^A - \langle r^2 \rangle^{A'}$，比例常数 $F_i$ 为原子场移电子因子；
2. **电荷半径的双重驱动力**：
   $$\langle r^2 \rangle = \langle r^2 \rangle_{\text{sph}} \left( 1 + \frac{5}{4\pi} \langle \beta_2^2 \rangle \right)$$
   电荷半径的变化不仅反映球形液滴体积随核子数的单调膨胀，而且直接耦合了原子核基态四极形变 $\beta_2^2$ 与动态表面零点振动涨落 $\langle \beta_2^2 \rangle$！

---

## 2. King 图线性理论（King Plot Analysis）与高精度微观解耦

在实际实验中，原子电子因子 $F_i$ 与质量移参数 $M_i, S_i$ 难以纯理论无误差计算。King 图分析法通过联立两个不同原子跃迁，消去未知的核半径项，提供了一种严格自洽的线性验证标准。

### (1) 修改同位素移（Modified Isotope Shift）定义
引入修正因子 $\mu_{A, A'}^{-1} = \frac{m_A m_{A'}}{m_A - m_{A'}}$，构造修改同位素移：
$$\xi_i^{A, A'} \equiv \mu_{A, A'}^{-1} \delta \nu_i^{A, A'} = K_i + F_i \cdot \left[ \mu_{A, A'}^{-1} \delta \langle r^2 \rangle^{A, A'} \right]$$

### (2) King 线性方程（King's Linearity Theorem）
将第二条跃迁 $\xi_2$ 对第一条跃迁 $\xi_1$ 作二维点图：
$$\xi_2^{A, A'} = \frac{F_2}{F_1} \xi_1^{A, A'} + \left( K_2 - \frac{F_2}{F_1} K_1 \right)$$
- **严格一阶线性**：在一阶微扰理论与单玻色子库仑交换框架下，各同位素对的测量点必须严格落在同一直线上；
- **斜率物理内涵**：直线斜率直接给出两跃迁原子电子场移因子的绝对比值 $F_2 / F_1$；
- **截距物理内涵**：直接给出两跃迁结合质量移常数的正交标定；
- **非线性偏离诊断（King Non-linearity）**：若数据点发生统计显著（$>3\sigma$）的弯曲偏离，标志着超精细二级微扰态混合、核极化效应或超出标准模型的新标量玻色子相互作用！

---

## 3. 电荷半径系统学两大经典谱学指纹

### (1) 电荷半径奇偶交错（Odd-Even Staggering, OES in Radii）
在全核素图的几乎所有同位素链中：
- 偶偶核的电荷半径随中子数平滑上升；
- **奇中子核的电荷半径系统性小于相邻偶偶核的平均内插值（$\langle r^2 \rangle_{\text{odd}} < \frac{1}{2}[\langle r^2 \rangle_{N-1} + \langle r^2 \rangle_{N+1}]$）**，导致同位素移呈现特征性的齿状锯齿震荡；
- **微观物理机制（Blocking Effect）**：偶偶核中核子完全配对，允许基态发生大幅度电四极表面零点振动（$\langle \beta_2^2 \rangle_{\text{dyn}} > 0$）；而在奇 $N$ 核中，孤立价核子的泡利阻塞效应强烈冻结了表面振动模式，降低了动态形变涨落，导致奇核有效电荷半径反常紧缩！

### (2) 形状交错与形状突变（Shape Staggering & Inversion）
当同位素链跨越临界形变边界时，电荷半径展现出极端敏感的相变指纹：
- **经典 ISOLDE 汞同位素形状交错（$^{181-186}\text{Hg}$）**：偶数汞同位素保持弱扁椭形状（$\beta_2 \approx 0.1$），而奇数同位素（$^{181, 183, 185}\text{Hg}$）基态突变陷入长椭大变形势阱（$\beta_2 \approx 0.3$），导致电荷半径发生数个 fm$^2$ 的巨大跳跃，开创了“同位素形状共存与突变”的现代研究篇章；
- **稀土区 $N=88 \to 90$ 形变陡跃**：在 Nd, Sm, Gd 同位素链中，跨过 $N=88$ 时 $\delta \langle r^2 \rangle$ 发生陡峭的台阶状跃升，与 $B(E2)$ 翻倍及两中子分离能平台完美重合。

---

## 4. 与在束高自旋实验的互补闭环

在博士课题直接相关的 $A\approx 130$（如 $^{128-136}\text{Xe}, {}^{129-135}\text{Ce}, {}^{130-136}\text{Ba}$）中：
1. **基态均方电荷半径作为形变零点锚点**：
   激光光谱测定的基态电荷半径演化 $\delta \langle r^2 \rangle$ 给出了零自旋下内禀总四极形变平方 $\langle \beta_2^2 \rangle = \beta_2^2 + \sigma_{\beta_2}^2$ 的绝对值；
2. **区分静态刚性形变与动态 $\gamma$ 软度**：
   结合在束库仑激发测得的 Kumar 不变量 $q_2^2$、高自旋转动带的 $B(E2)$ 以及基态电荷半径，三位一体解耦原子核是处于稳定的三轴刚性自发破缺态，还是大振幅 $\gamma$ 涨落的软核态，构成了完整的核结构验证闭环！

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/isotope_shift_charge_radii_calculator.py` 中实现了完整的激光同位素移动与电荷半径分析器：
1. **正常质量移与特殊质量移分离器**：计算理论 NMS 贡献，分离纯场移分量；
2. **均方电荷半径差反演器**：从测得的 $\delta \nu_{\text{exp}}$、电子场移因子 $F$ 与质量移参数 $K$ 反演 $\delta \langle r^2 \rangle$（$\text{fm}^2$）；
3. **电荷半径形变分解器**：将 $\delta \langle r^2 \rangle$ 严格因式分解为球形体积膨胀项与四极形变项 $\Delta \langle \beta_2^2 \rangle$；
4. **King 图二维线性拟合与残差检验器**：输入两组独立原子跃迁的同位素移，自动执行修改质量坐标转换、正交距离线性回归与非线性残差诊断；
5. **电荷半径奇偶交错（OES）量化器**：计算半径交错参数 $\gamma_r(N)$，诊断表面振动阻塞效应与异常形状突变。

---

## 6. 权威文献与理论溯源

1. **King, W. H.** (1984). *Isotope Shifts in Atomic Spectra*. Plenum Press, New York.
2. **Angeli, I. & Marinova, K. P.** (2013). Table of experimental nuclear ground state charge radii: An update. *At. Data Nucl. Data Tables*, 99(1), 69-95.
3. **Karthein, C. M. et al.** (2024). Electromagnetic properties of ground and isomeric states in indium isotopes towards $^{100}\text{Sn}$. *Nature Phys.*, 20(3), 390-396.
4. **Otten, E. W.** (1989). Nuclear radii and moments of unstable isotopes. *Treatise on Heavy-Ion Science*, Vol. 8, pp. 517-638. Plenum Press.
5. **卢希庭、江栋兴、叶沿林** (2000). 《原子核物理（修订版）》第 1 章：核半径与电荷分布测量. 原子能出版社.
