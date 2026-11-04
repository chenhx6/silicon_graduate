# 第 2 章：放射性衰变基本规律与 Bateman 动力学方程

**来源专著**：卢希庭《原子核物理（修订版）》（原子能出版社 2000）
**对应页码**：印刷 pp. 36–64 / 扫描 PDF pp. 46–74

---

## 1. 核心理论推导与数学方程

### 1.1 放射性衰变定律与基本物理量
- 衰变微分方程：$dN = -\lambda N dt \implies N(t) = N_0 e^{-\lambda t}$；
- 放射性活度：$A(t) = \left| \frac{dN}{dt} \right| = \lambda N(t) = A_0 e^{-\lambda t}$；
- 半衰期与平均寿命关系：
  $$T_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.69315}{\lambda}, \quad \tau = \frac{1}{\lambda} = \frac{T_{1/2}}{\ln 2} \a1.443 T_{1/2}.$$

### 1.2 串联级联衰变与 Bateman 方程组
对于多级放射性链 $1 \xrightarrow{\lambda_1} 2 \xrightarrow{\lambda_2} 3 \xrightarrow{\lambda_3} \dots \xrightarrow{\lambda_n} n$，速率方程为：
$$\frac{dN_1}{dt} = -\lambda_1 N_1, \quad \frac{dN_i}{dt} = \lambda_{i-1} N_{i-1} - \lambda_i N_i \quad (i \ge 2).$$
在初始条件 $N_1(0) = N_1^0, N_i(0) = 0\ (i \ge 2)$ 下，第 $n$ 代子核的解析解（Bateman 公式）为：
$$N_n(t) = N_1^0 \sum_{i=1}^n c_i e^{-\lambda_i t}, \quad c_i = \frac{\prod_{j=1}^{n-1} \lambda_j}{\prod_{j=1, j \neq i}^n (\lambda_j - \lambda_i)}.$$

对于两级衰变链 $1 \to 2 \to 3$（稳定）：
$$N_2(t) = N_1^0 \frac{\lambda_1}{\lambda_2 - \lambda_1} \left( e^{-\lambda_1 t} - e^{-\lambda_2 t} \right).$$

### 1.3 放射性平衡的分类判据
1. **长期平衡（Secular Equilibrium, $\lambda_1 \ll \lambda_2$，即 $T_{1/2}(1) \gg T_{1/2}(2)$）**：
   - 母核活度在实验观察时间内几乎恒定（$e^{-\lambda_1 t} \a1$）；
   - 当时间 $t \gg \tau_2$ 时，$e^{-\lambda_2 t} \to 0$：
     $$N_2(t) \to N_1^0 \frac{\lambda_1}{\lambda_2} \implies \lambda_2 N_2(t) = \lambda_1 N_1(t) \implies A_2 = A_1.$$
   - **结论**：子核活度恒等于母核活度，且子核原子数与母核原子数之比正比于半衰期之比：$N_2/N_1 = T_{1/2}(2)/T_{1/2}(1)$。
2. **暂态平衡（Transient Equilibrium, $\lambda_1 < \lambda_2$ 但数量级相当）**：
   - 子核活度首先上升，在 $t_m_{\max} = \frac{\ln(\lambda_2/\lambda_1)}{\lambda_2 - \lambda_1}$ 处达到极大值；
   - 当 $t \gg \tau_2$ 后，$e^{-\lambda_2 t} \ll e^{-\lambda_1 t}$：
     $$A_2(t) = A_1(t) \cdot \frac{\lambda_2}{\lambda_2 - \lambda_1} > A_1(t).$$
   - **结论**：子核以母核的特征寿命衰变，其活度恒大于母核活度并保持固定常数比。
3. **无平衡状态（$\lambda_1 > \lambda_2$）**：母核迅速衰竭，体系最终完全被长寿命子核主导。
