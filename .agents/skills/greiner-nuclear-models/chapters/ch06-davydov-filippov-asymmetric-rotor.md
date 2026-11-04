# 第 6 章 (一)：Davydov-Filippov 三轴刚性转子模型与本征代数求解

**来源专著**：Walter Greiner & Joachim A. Maruhn《Nuclear Models》（Springer 1996）第 6 章 §6.4.3
**对应页码**：印刷 pp. 145–147 / 物理 PDF pp. 164–166，式 (6.169)–(6.174)

---

## 1. 核心理论推导与模型表象

### 1.1 Davydov-Filippov 哈密顿量与水动力学惯量
A. S. Davydov 与 G. F. Filippov (1958) 提出假定原子核在内禀系中具有冻结的刚性四极形变参量 $(\beta, \gamma)$。自由旋转体系的量子哈密顿量为：
$$\hat{H}_{\text{rot}} = \sum_{k=1}^3 \frac{\hat{I}_k^2}{2\mathcal{J}_k},$$
主轴转动惯量取自无旋水动力学流动：
$$\mathcal{J}_k = 4 B \beta^2 \sin^2\left(\gamma - \frac{2\pi}{3} k\right) \quad (k = 1, 2, 3).$$
展开为内禀升降算符 $\hat{I}_\pm = \hat{I}_1 \mp i \hat{I}_2$（注意体固坐标系下角动量对易关系反号：$[\hat{I}_1, \hat{I}_2] = -i \hbar \hat{I}_3$）：
$$\hat{H}_{\text{rot}} = A \hat{\vec{I}}^2 + B_1 \hat{I}_3^2 + C (\hat{I}_+^2 + \hat{I}_-^2),$$
其中系数由惯量唯一确定：
$$A = \frac{\hbar^2}{4} \left( \frac{1}{\mathcal{J}_1} + \frac{1}{\mathcal{J}_2} \right), \quad B_1 = \frac{\hbar^2}{2\mathcal{J}_3} - A, \quad C = \frac{\hbar^2}{8} \left( \frac{1}{\mathcal{J}_1} - \frac{1}{\mathcal{J}_2} \right).$$

### 1.2 $D_2$ 四元对称群本征波函数展开
由于内禀系三主轴不可分辨，真实物理态在绕三主轴旋转 $\pi$ 的操作 $\mathcal{R}_k(\pi)$ 下必须具有正本征值：
$$|IMK\rangle_$C_{\text{sym}}$ = \sqrt{\frac{2I+1}{16\pi^2(1+\delta_{K0})}} \left[ D_{MK}^I(\theta_i) + (-1)^I D_{M,-K}^I(\theta_i) \right].$$
该对称性严格禁戒了奇数 $K$，使得只有 $K = 0, 2, 4, \dots \le I$ 的对称态参与构建。

---

## 2. 低自旋能级的严格矩阵对角化与三态和则

### 2.1 自旋 $I=2^+$ 的 $2 \times 2$ 特征矩阵
基底为 $|2M0\rangle_$C_{\text{sym}}$$ 与 $|2M2\rangle_$C_{\text{sym}}$$：
- 矩阵元（以 $\epsilon_0 = \frac{\hbar^2}{4 B \beta^2}$ 为单位）：
  $$H_{00} = 6 A = \frac{9 \epsilon_0}{\sin^2(3\gamma)} [1 - \cos(3\gamma)],$$
  $$H_{22} = 2 A + 4 B_1 = \frac{9 \epsilon_0}{\sin^2(3\gamma)} [1 + \cos(3\gamma)],$$
  $$H_{02} = H_{20} = 2\sqrt{3} C = \frac{3\sqrt{3}\epsilon_0}{\sin^2(3\gamma)} \sin(3\gamma).$$
- **特征方程求根**：
  $$\det(H - E) = E^2 - \text{Tr}(H) E + \det(H) = 0;$$
  $$\text{Tr}(H) = \frac{18 \epsilon_0}{\sin^2(3\gamma)}, \quad \det(H) = \frac{72 \epsilon_0^2}{\sin^2(3\gamma)}.$$
直接导出本征能量解析解（Greiner 式 6.172）：
$$E(2_1^+, 2_2^+) = \frac{9 \hbar^2}{4 B \beta^2} \frac{1 \mp \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}{\sin^2(3\gamma)}.$$

### 2.2 自旋 $I=3^+$ 的严格单态与三态求和恒等式
对于 $I=3^+$，受 $D_2$ 宇称约束（$(-1)^I = -1$），基底仅有唯一允许态 $|3M2\rangle_$C_{\text{sym}}$$（$1 \times 1$ 一维）：
$$E(3_1^+) = H_{22}(I=3) = \frac{18 \hbar^2}{4 B \beta^2 \sin^2(3\gamma)}.$$
将 $E(2_1^+)$ 与 $E(2_2^+)$ 直接相加：
$$E(2_1^+) + E(2_2^+) = \frac{9 \epsilon_0}{\sin^2(3\gamma)} \left[ (1 - \sqrt{\dots}) + (1 + \sqrt{\dots}) \right] = \frac{18 \epsilon_0}{\sin^2(3\gamma)} \equiv E(3_1^+)!$$
**数学证明结论**：无论水动力学还是微观刚体惯量，只要体系为三轴刚性转子，**该三态线性求和恒等式严格恒等成立**。

---

## 3. 电四极跃迁几率比定理

内禀四极跃迁算符在三轴系中包含两个不变量分量（沿长轴与短轴）：
$$\mathcal{M}(E2, \mu) = \frac{e Q_0}{2} \left[ \cos\gamma D_{\mu 0}^2 + \frac{\sin\gamma}{\sqrt{2}} (D_{\mu 2}^2 + D_{\mu,-2}^2) \right].$$
将本征波函数代入 Wigner-Eckart 定理求约化跃迁矩阵元，严格消去内禀四极矩 $Q_0$ 与常数因子：
$$\frac{B(E2; 2_2^+ \to 0_1^+)}{B(E2; 2_2^+ \to 2_1^+)} = \frac{20}{7} \frac{\sin^2(3\gamma)}{9 - 8\sin^2(3\gamma) + \sqrt{9 - 8\sin^2(3\gamma)}}.$$
在最大三轴形变 $\gamma = 30^\circ$ 处取得绝对理论极小值 $\frac{7}{40} = 0.1750$，为实验检验三轴性提供了高灵敏度探针。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/greiner-asymmetric-rotor-and-rvm-contract.md`
- **代码实现**：`system/scripts/analysis/bm2_asymmetric_rotor_matrix_diagonalizer.py`
- **上游来源**：`knowledge/sources/book-greiner-nuclear-models.md`
