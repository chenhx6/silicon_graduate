# 第 6 章 (三)：Wilets-Jean 完全 $\gamma$ 软核模型与 $O(5)$ 动力学对称性

**来源专著**：Walter Greiner & Joachim A. Maruhn《Nuclear Models》（Springer 1996）第 6 章 §6.6
**对应页码**：印刷 pp. 168–170 / 物理 PDF pp. 187–189，式 (6.221)–(6.228)

---

## 1. 核心理论推导与 $O(5)$ 势能几何

### 1.1 完全 $\gamma$ 不稳定软核模型假定
L. Wilets 与 M. Jean (1956) 提出了著名的完全 $\gamma$ 软核理论：
假定原子核集体势能完全由总形变量 $\beta$ 决定，而**对非轴对称角 $\gamma$ 完全独立平坦（平原势场）**：
$$V(\beta, \gamma) \equiv V(\beta).$$
在此假定下，波函数沿 $\gamma \in [0^\circ, 60^\circ]$ 方向没有任何深势阱束缚，原子核在所有三轴形状之间自由无规量子流动。

### 1.2 五维球面拉普拉斯算符与 Seniority 量子数
在五维集体坐标空间中，Bohr 动能算符可严格分离为 $\beta$ 径向算符与关于 $(\gamma, \theta_i)$ 的五维角向动量算符 $\hat{\Lambda}^2$：
$$\hat{T} = -\frac{\hbar^2}{2B} \left( \frac{1}{\beta^4} \frac{\partial}{\partial \beta} \beta^4 \frac{\partial}{\partial \beta} - \frac{\hat{\Lambda}^2}{\beta^2} \right),$$
其中五维 Casimir 算符 $\hat{\Lambda}^2$ 具有五维旋转群 $O(5)$ 的群代数本征值：
$$\hat{\Lambda}^2 \Psi_v = v(v + 3) \Psi_v, \quad v = 0, 1, 2, 3, \dots$$
$v$ 称为五维 Seniority 玻色量子数。

---

## 2. 解析能级结构与多重态简并

在谐振子势 $V(\beta) = \frac{1}{2} C \beta^2$ 或深袋方形势阱下，能级能量严格由 $v$ 决定：
$$E(v) \propto v(v + 3).$$

### 能级多重态阶梯：
1. **基态（$v=0$）**：唯一允许自旋为 $I = 0_1^+$，能量取为基准点 $0$；
2. **第一激发态（$v=1$）**：唯一允许自旋为 $I = 2_1^+$，相对能量为 $1 \times 4 = 4$；
3. **第二激发多重态（$v=2$）**：
   五维群分解 $O(5) \supset O(3)$ 要求 $v=2$ 状态严格分裂出两个自旋：$I = 4_1^+$ 与 $I = 2_2^+$，且两者在零阶下**完全严格能量简并**：
   $$E(4_1^+) \equiv E(2_2^+) \propto 2 \times 5 = 10;$$
   - **标志性能级比值**：
     $$R_{4/2} = \frac{E(4_1^+)}{E(2_1^+)} = \frac{10}{4} = 2.500.$$
     $R_{4/2} \approx 2.50$ 是判断原子核属于完全 $\gamma$ 软核（或 IBM $O(6)$ 极限）的国际通用权威标志！
4. **第三激发多重态（$v=3$）**：包含自旋 $I = 0_2^+, 3_1^+, 4_2^+, 6_1^+$，相对能量为 $3 \times 6 = 18$。其中 $E(3_1^+) \approx E(4_2^+)$ 呈现特征成对聚集。

---

## 3. 刚性三轴 (DF) vs 完全 $\gamma$ 软核 (WJ) 实验裁决准则

由于刚性三轴转子在 $\gamma \approx 25^\circ - 30^\circ$ 附近也能给出 $R_{4/2} \approx 2.6 - 2.8$ 与 $E(2_2^+)/E(2_1^+) \approx 2.0 - 2.5$，实验上甄别二者的关键在于高阶可观测量：

1. **准 $\gamma$ 带奇偶自旋交错指数 $S(J)$（Zamfir-Casten 判据）**：
   - **刚性三轴核（Davydov-Filippov）**：原子核具有稳定三轴极小，能级按 $(2^+, 3^+)$、$(4^+, 5^+)$ 成对，交错指数呈现深负值（$S(4) < 0$）；
   - **$\gamma$ 软核（Wilets-Jean）**：由于 $O(5)$ 对称性，能级按 $(3^+, 4^+)$、$(5^+, 6^+)$ 成对聚集，交错指数为大正值（$S(4) > 0$）；
2. **三态求和恒等式**：
   - 刚性三轴核严格满足 $E(2_1^+) + E(2_2^+) \equiv E(3_1^+)$；
   - $\gamma$ 软核中 $E(2_1^+) + E(2_2^+) \propto 4 + 10 = 14$，而 $E(3_1^+) \propto 18$，求和差值高达 $+28\%$，彻底打破刚性转子恒等式！

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/greiner-asymmetric-rotor-and-rvm-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`collective-quadrupole-pes` 子命令)
- **上游来源**：`knowledge/sources/book-greiner-nuclear-models.md`
