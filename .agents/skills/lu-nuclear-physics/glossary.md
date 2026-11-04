# Glossary: 卢希庭《原子核物理》中文标准术语与英汉对照规范

本术语表整理《原子核物理（修订版）》（卢希庭等，原子能出版社 2000）中的标准中文学术术语、国际对应英文术语以及规范定义。

---

## 1. 静态性质与结合能 (Static Properties and Binding Energy)

- **Binding Energy (结合能 $B(A, Z)$)**: 自由核子结合成原子核时释放的总能量：$B(A, Z) = [Z M_H + (A - Z) M_n - M(A, Z)] c^2$。
- **Binding Energy per Nucleon (比结合能 / 平均结合能 $\epsilon$)**: $\epsilon = B(A, Z) / A$，衡量原子核稳定程度的核心物理量，中等质量区（$A \approx 56 - 62$）达到极大值（$\sim 8.8\text{ MeV}$）。
- **Separation Energy (分离能)**:
  - 中子分离能 ($S_n$): 从原子核中移走一个中子所需的最小能量：$S_n = B(A, Z) - B(A-1, Z)$；
  - 质子分离能 ($S_p$): 从原子核中移走一个质子所需的最小能量：$S_p = B(A, Z) - B(A-1, Z-1)$。
- **Semi-Empirical Mass Formula (SEMF, 半经验质量公式 / Bethe-Weizsäcker 公式)**: 基于液滴模型描述结合能随 $A$ 和 $Z$ 变化的五项公式（体积能、表面能、库仑能、对称能、对能）。
- **$\beta$-Stable Valley (Beta 稳定谷)**: 结合能曲面在固定 $A$ 截面上抛物线底部的连线，电荷数满足 $Z_{\text{stable}} = A / (2 + 0.015 A^{2/3})$。

---

## 2. 放射性与衰变运动学 (Radioactivity and Decay Kinetics)

- **Decay Constant (衰变常数 $\lambda$)**: 单位时间内一个放射性原子核发生衰变的几率，与半衰期关系为 $T_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda}$，与平均寿命关系为 $\tau = 1/\lambda$。
- **Activity (活度 $A(t)$)**: 单位时间内发生的核衰变次数：$A(t) = \lambda N(t)$，SI 单位为贝可勒尔（$\text{Bq} = \text{s}^{-1}$），历史单位为居里（$\text{Ci} = 3.7 \times 10^{10}\text{ Bq}$）。
- **Bateman Equations (贝特曼方程)**: 描述多级放射性连续级联衰变链中各代子核核素数目随时间演化的微分方程组解析解。
- **Secular Equilibrium (长期平衡)**: 母核半衰期远大于子核半衰期（$\lambda_1 \ll \lambda_2$）时的衰变平衡状态，经过数个子核半衰期后，子核活度趋于等于母核活度（$A_2 \approx A_1$）。
- **Transient Equilibrium (暂态平衡)**: 母核半衰期稍大于子核半衰期（$\lambda_1 < \lambda_2$）时的衰变平衡状态，子核活度在达到峰值后与母核保持固定活度比值衰减（$A_2 / A_1 = \lambda_2 / (\lambda_2 - \lambda_1) > 1$）。

---

## 3. 衰变机制与电磁跃迁 (Decay Modes and Gamma Transitions)

- **Geiger-Nuttall Law (盖革-纳托尔定律)**: $\alpha$ 衰变常数对数与 $\alpha$ 粒子动能或衰变能平方根的倒数呈线性经验关系：$\log \lambda = A + B / \sqrt{E_\alpha}$。
- **Kurie Plot (居里图 / Fermi-Kurie 图)**: 检验 $\beta$ 衰变谱形是否符合允许跃迁理论的线性图，横轴截距直接给出衰变最大端点能量 $E_0$。
- **Comparative Half-life ($\log ft$, 比较半衰期)**: 将实测半衰期与费米积分相空间函数相乘并取对数所得的无量纲参数，纯粹反映弱相互作用微观核跃迁矩阵元 $|M_{fi}|^2$ 的大小。
- **Fermi Transition (费米跃迁)**: $\beta$ 衰变发射的电子与中微子自旋反平行（$S=0$），角动量选择定则为 $\Delta I = 0, \Delta \pi = \text{no}$。
- **Gamow-Teller Transition (加莫夫-泰勒跃迁)**: $\beta$ 衰变发射的电子与中微子自旋平行（$S=1$），角动量选择定则为 $\Delta I = 0, \pm 1$ ($0 \to 0$ 禁戒)，$\Delta \pi = \text{no}$。
- **Internal Conversion Coefficient (ICC, 内转换系数 $\alpha$)**: 发生内转换发射轨道电子的几率与发射光子的几率之比：$\alpha = \lambda_e / \lambda_\gamma$。
- **Weisskopf Units ($W.u.$, 维斯科普夫单位 / 单粒子单位)**: 假设核跃迁纯粹由一个质子在球形方势阱两个极值轨道间跃迁所算得的电磁跃迁几率理论基准值。

---

## 4. 核模型与反应理论 (Nuclear Models and Reactions)

- **Independent Particle Shell Model (独立粒子壳模型)**: 将核子运动等效为在球对称自洽平均场中运动的模型，引入强自旋-轨道耦合解释幻数（Magic numbers: 2, 8, 20, 28, 50, 82, 126）。
- **Spin-Orbit Splitting (自旋-轨道分裂)**: 具有相同轨道角动量 $l$ 的能级分裂为 $j = l + 1/2$ 与 $j = l - 1/2$ 两支，总角动量较大的分支能量被强烈压低。
- **Optical Model (光学模型)**: 将核子与靶核复杂的强相互作用等效为一个具有复数折射率的光学介质势场，实部描述弹性散射，虚部描述非弹性与反应吸收。
- **Compound Nucleus (复合核)**: 入射粒子被靶核完全吸收后，核子间频繁碰撞将能量和角动量完全统计分配形成的长寿命亚稳中间态，衰变道与形成道彼此独立。
- **Breit-Wigner Formula (布赖特-维格纳单能级公式)**: 描述低能孤立共振散射与吸收反应截面随入射能量变化的解析洛伦兹线形公式。
