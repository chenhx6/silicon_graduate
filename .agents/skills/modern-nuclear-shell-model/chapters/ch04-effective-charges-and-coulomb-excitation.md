# 第 4 章：微观极化有效电荷、低能库仑激发与 Talmi 矩阵元完全相消

**来源专著**：I. Talmi、A. E. Stuchbery、M. Rocchini 等《The Nuclear Shell Model 70 Years after Its Advent》（MDPI 2023）第 1、2、7 篇专论
**对应页码**：印刷 pp. 1–86, 175–192 / 物理 PDF pp. 12–97, 186–203

---

## 1. 核心理论推导与 Talmi $^{14}\text{C}$ 衰变相消奇迹

### 1.1 $^{14}\text{C}$ 超长半衰期之谜
$^{14}\text{C}$ 向 $^{14}\text{N}$ 基态的允许 Gamow-Teller $\beta$ 衰变比较半衰期高达 $\log ft = 9.04$（半衰期达 $5730\text{ 年}$），比常规允许跃迁（$\log ft \approx 3.5 - 5.0$）慢了近一百万倍！
I. Talmi 严格运用微观壳模型两体矩阵元证明了其相消机制：
1. **微观波函数组态混合**：
   $$|^{14}\text{C}(0^+)\rangle = \alpha |(1p_{1/2})^2; 0^+\rangle + \beta |(1p_{3/2})^{-2}; 0^+\rangle;$$
   $$|^{14}\text{N}(1^+)\rangle = \alpha' |(1p_{1/2})^2; 1^+\rangle + \beta' |(1p_{3/2})^{-1} (1p_{1/2}); 1^+\rangle;$$
2. **加莫夫-泰勒跃迁矩阵元的完全相消**：
   $$\langle ^{14}\text{N}(1^+) || \sum_i \tau_i^+ \vec{\sigma}_i || ^{14}\text{C}(0^+) \rangle = \alpha \alpha' M_{11} + \alpha \beta' M_{12} + \beta \alpha' M_{21} + \beta \beta' M_{22};$$
3. **微观张量力驱动的代数抵消**：
   核力中的张量分量引入的特定组态混合系数比值恰好满足：
   $$\frac{\beta}{\alpha} \approx - \frac{\langle p_{1/2}^2 || \sigma || p_{1/2}^2 \rangle}{\langle (p_{3/2})^{-1} p_{1/2} || \sigma || p_{1/2}^2 \rangle} \approx - \sqrt{2}.$$
   导致两项主导矩阵元大小相等、代数符号严格相反，发生**高达 $99.99\%$ 的代数完全相消**，彻底确立了壳模型微观矩阵元相干抵消的经典典范。

---

## 2. 核芯极化有效电荷与微观集体性

### 2.1 巨四极共振 (GQR) 虚激发与感生电荷
在有限截断的价模型空间中，价中子名义电荷为零（$e_n = 0$）。然而实验测得纯中子态跃迁具有显著非零的 $B(E2)$ 几率：
- **微观极化机制**：价中子通过两体残余力微扰极化致密的带电核芯，诱发核芯发生高频 $2\hbar\omega$ 巨四极共振（GQR）虚激发；
- **重整化有效电荷公式**：
  $$e_{\text{eff}}^\nu \a0.5 - 0.7 e, \quad e_{\text{eff}}^\pi \approx e + \delta e_{\text{pol}} \a1.3 - 1.5 e.$$

---

## 3. 低能库仑激发与 Kumar 四极不变量

M. Rocchini 与 K. Zielińska 形式化了低能库仑激发（Coulex）在确定核形状上的绝对优势：
在低于库仑势垒的安全能量（Cline 判据）下碰撞，反应纯粹由经典电磁场激发，不涉及强相互作用核势的不确定度：
1. **全阶矩阵元测定**：通过变换不同散射角与束能，同时测定能态之间的全部非对角跃迁矩阵元 $\langle 2_1^+ || \mathcal{M}(E2) || 0_1^+ \rangle$ 与对角静态电四极矩 $\langle 2_1^+ || \mathcal{M}(E2) || 2_1^+ \rangle$；
2. **Kumar 四极不变量 (Quadrupole Invariants)**：
   应用正交完备性求和规则直接构造：
   $$q_2 = \langle 0_1^+ | [\mathcal{M}(E2) \times \mathcal{M}(E2)]_0 | 0_1^+ \rangle \propto Q_0^2 \propto \beta^2;$$
   $$q_3 = \langle 0_1^+ | [[\mathcal{M}(E2) \times \mathcal{M}(E2)]_2 \times \mathcal{M}(E2)]_0 | 0_1^+ \rangle \propto Q_0^3 \cos(3\delta) \propto \beta^3 \cos(3\gamma).$$
   无需任何微观模型假设，直接在实验上无偏提取原子核均方四极形变 $\beta$ 与非轴对称刚性三轴角 $\gamma$，成为连接微观壳模型与宏观三轴形变的最权威实验桥梁。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/low-energy-coulomb-excitation-shell-model-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`coulex-kumar-invariant` 子命令)
- **上游来源**：`knowledge/sources/book-nuclear-shell-model-70-years.md`
