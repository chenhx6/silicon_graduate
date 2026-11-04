# 第 6 章 (五)：巨多极共振宏观流体动力学与形变双峰分裂

**来源专著**：Walter Greiner & Joachim A. Maruhn《Nuclear Models》（Springer 1996）第 6 章 §6.9
**对应页码**：印刷 pp. 197–206 / 物理 PDF pp. 216–225，式 (6.256)–(6.280)

---

## 1. 核心理论推导与宏观流体两模型

### 1.1 等标与等矢多极共振的流体动力学分类
巨多极共振是原子核所有核子高度相干协同振荡的高激发宏观动力学模式：
- **等标模式（Isoscalar, $\Delta T = 0$）**：质子流与中子流在空间同相运动，表现为全核形状或密度的宏观振动（如等标巨单极共振 ISGMR 呼吸模、等标巨四极共振 ISGQR 表面波）；
- **等矢模式（Isovector, $\Delta T = 1$）**：质子流与中子流在空间作反相相对振动，表现为交变电偶极极化或同位旋分离（如等矢巨偶极共振 IVGDR、等矢巨四极共振 IVGQR）。

### 1.2 Goldhaber-Teller (GT) 刚体球相对位移模型
M. Goldhaber 与 E. Teller (1948) 假定：
1. 质子球（半径 $R_0$）与中子球（半径 $R_0$）各自为内部不可压缩的刚性核物质流体球；
2. 两球体沿相对平移矢量 $\vec{d} = \vec{r}_p - \vec{r}_n$ 发生宏观位移；
3. **表面恢复力**：体积内部质中密度比无变化，恢复力纯粹产生于两球错开时在核表面形成的过剩单质子与单中子层（表面对称能恢复力）；
4. **能级标度律**：
   $$E_{\text{GT}} = \hbar\omega_{\text{GT}} \propto A^{-1/6}.$$

### 1.3 Steinwedel-Jensen (SJ) 声学声压驻波模型
H. Steinwedel 与 J. H. D. Jensen (1950) 假定：
1. 原子核总表面严格固定为一个不可移动的刚性球形外壳（边界半径 $R_0 = r_0 A^{1/3}$ 恒定）；
2. 质子流密度 $\rho_p(\vec{r}, t)$ 与中子流密度 $\rho_n(\vec{r}, t)$ 满足局部连续性方程，总密度保持常数 $\rho_0 = \rho_p + \rho_n$；
3. 质子与中子在核体内部发生周期性可压缩流体动力学反相振动，恢复力源于体积对称能势能密度 $V_$C_{\text{sym}}$ \propto b_$C_{\text{sym}}$ (\rho_n - \rho_p)^2 / \rho_0$；
4. **Helmholtz 波动方程**：声速 $u = \sqrt{8 b_$C_{\text{sym}}$ / M^*}$，球面边界条件 $\left.\frac{\partial \rho_p}{\partial r}\right|_{r=R_0} = 0$；
5. **能级标度律**：
   $$E_{\text{SJ}} = \hbar\omega_{\text{SJ}} = \frac{z_1 u \hbar}{R_0} \propto A^{-1/3}, \quad z_1 \approx 2.08.$$

---

## 2. 等矢巨偶极共振 (IVGDR) 在形变核中的双峰分裂

在轴对称变形核中，原子核三维球对称性被破坏：
1. **沿主长轴（$z$ 轴，半轴长 $a$）的振动**：
   - 声学驻波波长较长（$\lambda_a \propto a$），恢复力较小，对应较低的共振激发能：
     $$E_a \approx \frac{\text{const}}{a};$$
2. **沿两垂直短轴（$x, y$ 轴，半轴长 $b$）的简并振动**：
   - 表面曲率大，波长短（$\lambda_b \propto b$），对应较高的共振激发能：
     $$E_b \approx \frac{\text{const}}{b} > E_a;$$
3. **共振峰面积积分守恒律**：
   由于短轴方向在空间包含两个相互正交的简并自由度（$x$ 与 $y$），两共振峰在光核吸收截面曲线下的积分面积之比严格为：
   $$\frac{\int \sigma_a(E) dE}{\int \sigma_b(E) dE} \equiv \frac{1}{2};$$
4. **基态四极形变 $\beta_2$ 解析反演公式**：
   $$\frac{E_b - E_a}{E_{\text{mean}}} \a0.95 \cdot \beta_2.$$
   实测 IVGDR 双峰间距直接测定了原子核基态四极形变量，是高激发集体动力学与基态宏观几何的完美统一。

---

## 3. Thomas-Reiche-Kuhn (TRK) 能量加权求和规则

经典光核吸收截面全能量积分满足非相对论性严格求和恒等式：
$$\Sigma_{\text{TRK}} = \int_0^\infty \sigma_{\text{abs}}(E) dE = \frac{2\pi^2 e^2 \hbar}{M c} \frac{N Z}{A} \approx 60 \frac{N Z}{A}\text{ MeV}\cdot\text{mb}.$$
- **交换力增强因子 $(1 + \kappa)$**：
  核力中包含的 Heisenberg 空间交换与 Majorana 同位旋交换分量使得两体相互作用哈密顿量与偶极坐标算符不完全对易：$[\hat{V}, \hat{D}] \ne 0$；
  实验测得实际积分截面通常耗尽 TRK 规则的 $120\% - 140\%$（$\kappa \a0.2 - 0.4$），为微观张量力与介子交换流提供了宏观实验证据。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/greiner-asymmetric-rotor-and-rvm-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`gdr-lorentzian-trk` 子命令)
- **上游来源**：`knowledge/sources/book-greiner-nuclear-models.md`
