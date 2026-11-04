# 第 4 章 (二)：玻色子展开技术：Holstein-Primakoff 与高自旋摆动非简谐谱

**来源专著**：A. A. Raduta《Nuclear Structure with Coherent States》（Springer 2016）第 4 章 §4.2
**对应页码**：印刷 pp. 86–101 / 物理 PDF pp. 93–108

---

## 1. 核心理论推导与自旋玻色映射代数

### 1.1 Holstein-Primakoff 展开定义
T. Holstein 与 H. Primakoff (1940) 提出了将自旋群 $SU(2)$ 算符精确映射为单自由度标准简谐玻色子创生湮灭算符（$[a, a^\dagger] = 1$）的代数表象：
以最大自旋对齐轴（取为 $z$ 轴）为量子化基准：
$$\hat{I}_z = I - a^\dagger a,$$
$$\hat{I}_+ = \sqrt{2I - a^\dagger a} \cdot a = \left( \hat{I}_- \right)^\dagger, \quad \hat{I}_- = a^\dagger \sqrt{2I - a^\dagger a}.$$
- **代数保真性**：
  直接验证角动量对易关系：
  $$[\hat{I}_z, \hat{I}_\pm] = [I - a^\dagger a, \pm \hat{I}_\pm] = \pm \hat{I}_\pm,$$
  $$[\hat{I}_+, \hat{I}_-] = (2I - a^\dagger a) a a^\dagger - a^\dagger (2I - a^\dagger a) a = 2(I - a^\dagger a) = 2 \hat{I}_z.$$
  自旋代数在玻色物理空间内严格满足封闭对易子。

### 1.2 高自旋 $1/I$ 渐近级数微扰展开
当自旋 $I \gg 1$ 且玻色激发声子数满足 $n = a^\dagger a \ll 2I$ 时，平方根算符可做严密的泰勒级数二项式展开：
$$\sqrt{2I - a^\dagger a} = \sqrt{2I} \left[ 1 - \frac{a^\dagger a}{4I} - \frac{(a^\dagger a)^2}{32 I^2} + \dots \right].$$
代入直角分量：
$$\hat{I}_x = \frac{\hat{I}_+ + \hat{I}_-}{2} \approx \sqrt{\frac{I}{2}} (a + a^\dagger) - \frac{1}{4\sqrt{2I}} (a^\dagger a a + a^\dagger a^\dagger a),$$
$$\hat{I}_y = \frac{\hat{I}_+ - \hat{I}_-}{2i} \approx \frac{\sqrt{I/2}}{i} (a - a^\dagger) - \frac{1}{4i\sqrt{2I}} (a^\dagger a a - a^\dagger a^\dagger a).$$

---

## 2. 三轴哈密顿量展开与摆动声子能谱求解

将自旋分量展开式代入三轴转子哈密顿量 $\hat{H} = \frac{\hat{I}_x^2}{2\mathcal{J}_x} + \frac{\hat{I}_y^2}{2\mathcal{J}_y} + \frac{\hat{I}_z^2}{2\mathcal{J}_z}$：

### 2.1 零阶基态与一阶简谐摆动项
整理至玻色子二阶项：
$$\hat{H}_2 = E_{\text{g.s.}}(I) + \frac{I}{4} \left( \frac{1}{\mathcal{J}_x} + \frac{1}{\mathcal{J}_y} - \frac{2}{\mathcal{J}_z} \right) (a^\dagger a + a a^\dagger) + \frac{I}{4} \left( \frac{1}{\mathcal{J}_x} - \frac{1}{\mathcal{J}_y} \right) (a^{\dagger 2} + a^2).$$
引入标准 Bogoliubov 玻色标度变换：$a = \cosh\theta \, \alpha + \sinh\theta \, \alpha^\dagger$，消除非对角双声子创生项，直接解析对角化为纯简谐振子能谱：
$$\hat{H}_2 = E_0(I) + \hbar\omega_w \left( \alpha^\dagger \alpha + \frac{1}{2} \right),$$
其中简谐摆动频率（Wobbling Frequency）严格由主轴惯量差给出：
$$\hbar\omega_w = I \sqrt{\left(\frac{1}{\mathcal{J}_x} - \frac{1}{\mathcal{J}_z}\right)\left(\frac{1}{\mathcal{J}_y} - \frac{1}{\mathcal{J}_z}\right)}.$$

### 2.2 四阶非简谐微扰项与声子非线性软化
保留至玻色四阶项，产生有效非简谐四次恢复力项：
$$\hat{H}_4 = V_4 \cdot \alpha^\dagger \alpha^\dagger \alpha \alpha.$$
多声子摆动态能量阶梯展开为：
$$E(n_w, I) = E_0(I) + n_w \hbar\omega_w(I) + V_4(I) n_w (n_w - 1).$$
微观计算证明，在经典分离线附近，四阶系数 $V_4 < 0$ 且随能量升高迅速负发散，直接给出多声子摆动能级间距显著压缩（Anharmonic Softening）的代数微观起源。

---

## 3. 在束谱学应用：多声子摆动能量阶梯实验检验
在超形变核（如 $^{163}\text{Lu}$ 三轴超形变带 TSD1, TSD2, TSD3）中：
- 基态带 $n_w = 0$、一单声子摆动带 $n_w = 1$、双声子摆动带 $n_w = 2$ 均被实验完整观测；
- 实测双声子激发能满足 $E(n_w=2) - E(n_w=1) < E(n_w=1) - E(n_w=0)$，其非简谐下弯幅度与 Holstein-Primakoff 展开导出的 $V_4$ 理论预言自洽吻合，确立了非轴对称转子微观声子结构。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/raduta-gcsm-chiral-and-triaxial-rotor-contract.md`
- **代码实现**：`system/scripts/analysis/multiphonon_wobbling_anharmonic_spectrum_solver.py`
- **上游来源**：`knowledge/sources/book-raduta-coherent-states.md`
