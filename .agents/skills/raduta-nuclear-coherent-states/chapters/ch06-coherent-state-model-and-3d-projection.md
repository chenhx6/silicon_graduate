# 第 6 章：相干态模型 (CSM) 与三维连续角动量投影正规化

**来源专著**：A. A. Raduta《Nuclear Structure with Coherent States》（Springer 2016）第 6 章
**对应页码**：印刷 pp. 179–235 / 物理 PDF pp. 186–242

---

## 1. 核心理论推导与内禀变形相干态

### 1.1 变形四极相干态的构建
A. A. Raduta 等人建立了相干态模型（Coherent State Model, CSM）。通过引入五维四极玻色子算符 $b_{2\mu}^\dagger$（$\mu = -2, \dots, +2$），定义内禀变形相干基态：
$$|\psi(d)\rangle = \exp\left[ d (b_{20}^\dagger - b_{20}) \right] |0\rangle = \exp\left(-\frac{d^2}{2}\right) \sum_{n=0}^\infty \frac{d^n}{\sqrt{n!}} |n, 20\rangle,$$
其中实参数 $d$ 直接度量原子核的轴对称四极形变程度（与 Bohr 参量关系为 $d \propto \beta$）。
- 该态是湮灭算符的本征态：$b_{20} |\psi(d)\rangle = d |\psi(d)\rangle$；
- 宏观相空间展示出局域高斯波包的极小不确定度特性，但在实空间破坏了球对称性，混杂了所有可能偶数角动量分量。

---

## 2. Peierls-Yoccoz 三维角动量投影与三大集体能带

### 2.1 三维旋转投影算符
应用全空间旋转群 $SO(3)$ 投影技术：
$$\hat{P}_{MK}^I = \frac{2I+1}{8\pi^2} \int_0^{2\pi} d\alpha \int_0^\pi \sin\beta d\beta \int_0^{2\pi} d\gamma \, D_{MK}^{I*}(\alpha, \beta, \gamma) \hat{R}(\alpha, \beta, \gamma).$$

### 2.2 三大物理集体能带的自洽提取
从相干态及其激发多项式中，自洽正交投影出基带、$\beta$ 振动带与 $\gamma$ 振动带：
1. **基态转动带 (Ground Band, $g$-band)**：
   $$|\phi_{IM}^{(g)}\rangle = \frac{1}{N_I^{(g)}(d)} \hat{P}_{M0}^I |\psi(d)\rangle, \quad I = 0^+, 2^+, 4^+, 6^+, \dots;$$
2. **$\beta$ 振动带 ($\beta$-band, $K=0$)**：
   $$|\phi_{IM}^{(\beta)}\rangle = \frac{1}{N_I^{(\beta)}(d)} \hat{P}_{M0}^I \left[ \hat{\Omega}_\beta^\dagger |\psi(d)\rangle \right], \quad I = 0^+, 2^+, 4^+, \dots;$$
3. **$\gamma$ 振动带 ($\gamma$-band, $K=2$)**：
   $$|\phi_{IM}^{(\gamma)}\rangle = \frac{1}{N_I^{(\gamma)}(d)} \hat{P}_{M2}^I \left[ b_{22}^\dagger |\psi(d)\rangle \right], \quad I = 2^+, 3^+, 4^+, 5^+, \dots$$

### 2.3 投影重叠积分核 (Norm Overlap Kernels)
正规化系数 $N_I(d)$ 通过对 Euler 角的一维勒让德代换精确积分：
$$N_I^{(g)2}(d) = (2I+1) e^{-d^2} \int_0^1 P_I(x) \exp\left[ d^2 P_2(x) \right] dx.$$
- 当 $d \to 0$ 时，投影态平滑还原为微扰谐振子球形多重态；
- 当 $d \gg 1$ 时，积分核展示渐近行为，严格还原刚体转子的 $I(I+1)$ 能谱律与经典 Alaga 跃迁定则。

---

## 3. 在束谱学应用：无截断自洽电多极跃迁 $B(E2)$
在传统玻色子模型中，电四极算符往往被任意截断；而在 CSM 中，四极跃迁算符由集体坐标正则生成：
$$\hat{Q}_{2\mu} = q_1 (b_{2\mu}^\dagger + (-1)^\mu b_{2,-\mu}) + q_2 (b^\dagger b)_{2\mu}.$$
在正规化投影基底之间直接求矩阵元，完全不需要人为引入额外的自由微扰截断，高精度复现了低能核谱学中带内增强四极跃迁（$\sim 50\text{ W.u.}$）与带间禁戒跃迁的实验实测值。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/raduta-gcsm-chiral-and-triaxial-rotor-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`angular-momentum-projection-amp` 子命令)
- **上游来源**：`knowledge/sources/book-raduta-coherent-states.md`
