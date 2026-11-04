# 第 12 章 (二)：未观测级联跃迁去取向 $U_k$ 理论与初态取向衰减

**来源专著**：W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》（1975）第 12 章 §12.5
**对应页码**：印刷 pp. 550–558 / 物理 PDF pp. 550–558，式 (12.207)–(12.213)

---

## 1. 核心理论推导与去取向张量变换

### 1.1 未观测中间跃迁与对齐度损失
在实际高自旋在束实验中，探测器阵列所观测的目标跃迁往往不是由初态复合核直接退激发射，而是经历了一条复杂的未观测高激发能级级联退激喂带链：$I_a \xrightarrow{\gamma_{\text{unobs}}} I_b$。
- **物理机制**：未被观测到的光子向 $4\pi$ 空间各向同性发射，其随机带走的角动量分量迫使子能级 $I_b$ 的磁子态分布发生热扩散展宽，从而导致核态的空间对齐程度被逐步抹平；
- **张量代数变换**：由角动量张量代数定理，未观测跃迁后子能级的统计取向张量与母能级张量之间满足严格的线性标度变换：
  $$\rho_{kq}(I_b) = U_k(I_a I_b L) \cdot \rho_{kq}(I_a).$$

### 1.2 去取向系数 $U_k(I_a I_b L)$ 解析表达式
去取向系数 $U_k$ 是纯几何的 Wigner $6j$ 符号重耦合函数（Hamilton 式 12.209）：
$$U_k(I_a I_b L) = (-1)^{I_a + I_b + L + k} \sqrt{(2I_a+1)(2I_b+1)} W(I_a I_a I_b I_b; k L) = (-1)^{I_a + I_b + L + k} \sqrt{(2I_a+1)(2I_b+1)} \begin{Bmatrix} I_a & I_a & k \\ I_b & I_b & L \end{Bmatrix}.$$
- **恒等性质**：
  1. $k=0$ 阶恒等为 1：$U_0(I_a I_b L) \equiv 1$（总几率守恒）；
  2. 对于偶数阶 $k = 2, 4$，通常 $0 < U_k < 1$；且 $U_4 < U_2$，表明四阶高阶张量衰减速度显著快于二阶张量；
  3. 当自旋 $I_a, I_b \gg L$（高自旋极限）时，单次拉伸四极跃迁的去取向极微弱：$U_2 \to 1 - \frac{k(k+1)}{4 I^2} \a0.95 - 0.98$。

### 1.3 混合未观测跃迁的推广
若未观测跃迁本身包含混合多极性（如 $L$ 与 $L'$ 混合）：
$$U_k(I_a I_b L L') = \frac{U_k(I_a I_b L) + \delta^2 U_k(I_a I_b L')}{1 + \delta^2}.$$

---

## 2. 级联退激连乘守恒定理

对于相继发生的 $n$ 步未观测跃迁链 $I_0 \xrightarrow{L_1} I_1 \xrightarrow{L_2} I_2 \dots \xrightarrow{L_n} I_n$：
统计取向张量满足**逐级连乘定理 (Cascade Product Theorem)**：
$$B_k(I_n) = B_k(I_0) \cdot \prod_{j=1}^n U_k(I_{j-1} I_j L_j).$$
目标态最终发射的观测 $\gamma$ 射线方向角分布各向异性系数展开为：
$$A_k^{\text{obs}} = B_k(I_0) \cdot \left[ \prod_{j=1}^n U_k(I_{j-1} I_j L_j) \right] \cdot R_k(L, L', I_n, I_f).$$

---

## 3. 在束谱学应用：多极混合比 $\delta$ 反演偏差的彻底纠正
在实验数据处理中，若实验者忽略上方喂带级联的去取向效应，误将 $A_k^{\text{obs}}$ 直接解释为无衰减的 $B_k(I_0) R_k$：
1. 会误以为初始反应的自旋取向参数 $\sigma/I$ 异常偏大（误判对齐度差）；
2. 会在求解 Pattern 2 的二次方程时，由于人为压低了 $A_2$，导致反演出的多极混合比 $\delta$ 发生**高达 $30\% - 50\%$ 的严重系统偏差**！
通过在能级纲图中追踪侧馈流强（Side Feeding）并显式施加 $\mathcal{U}_k$ 级联连乘修正，方可获得具有绝对物理可信度的微观跃迁矩阵元。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/hamilton-angular-distribution-dco-polarization-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`cascade-deorientation` 子命令)
- **上游来源**：`knowledge/sources/book-hamilton-electromagnetic-interaction.md`
