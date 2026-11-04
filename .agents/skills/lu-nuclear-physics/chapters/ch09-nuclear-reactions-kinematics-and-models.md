# 第 9 章：原子核反应运动学、截面与反应机制模型

**来源专著**：卢希庭《原子核物理（修订版）》（原子能出版社 2000）
**对应页码**：印刷 pp. 227–294 / 扫描 PDF pp. 237–304

---

## 1. 核心理论推导与数学方程

### 1.1 核反应运动学与 $Q$ 方程
考虑两体核反应 $A(a, b)B$：入射粒子 $a$（动能 $E_a$）打击静止靶核 $A$，出射轻粒子 $b$（动能 $E_b$，出射角 $\theta_b$）与反冲重核 $B$。
- **反应能 $Q$**：
  $$Q = (M_A + M_a - M_B - M_b) c^2 = E_b + E_B - E_a.$$
- **经典 $Q$ 方程**：
  $$Q = E_b \left(1 + \frac{M_b}{M_B}\right) - E_a \left(1 - \frac{M_a}{M_B}\right) - \frac{2}{M_B} \sqrt{M_a M_b E_a E_b} \cos\theta_b.$$
- **吸热反应（$Q < 0$）绝对阈能**：
  在质心系中，必须有足够的入射动能转化为反应能 $Q$：
  $$E_{\text{c.m.}} \ge |Q| \implies E_a^{\text{th}} = |Q| \left( 1 + \frac{M_a}{M_A} \right).$$

### 1.2 核反应机制三大阶段分类
根据反应相互作用时间尺度的不同，核反应可严格划分为三种机制：
1. **直接反应（Direct Reactions, $\tau_{\text{int}} \sim 10^{-22}\text{ s}$）**：
   - 快速外围碰撞，粒子掠过靶核表面，仅与一个或少数几个核子发生动量交换；
   - 典型反应：弹性散射、非弹性散射、单核子剥离/拾取反应 $(d, p), (p, d)$；
   - 实验角分布特征：前向强烈出射峰，服从贝塞尔函数球面衍射分布，直接用于提取单粒子轨道角动量 $l$ 与光谱因子 $S_{lj}$。
2. **复合核反应（Compound Nucleus Reactions, $\tau_{\text{int}} \sim 10^{-16} - 10^{-18}\text{ s}$）**：
   - 入射粒子被靶核完全吞并，能量在全核所有核子间充分统计碰撞均分，系统完全“遗忘”形成道记忆；
   - 复合核 Hauser-Feshbach 统计衰变（发射中子、质子、$\alpha$ 粒子或级联 $\gamma$ 射线）；
   - 实验角分布特征：质心系关于 $90^\circ$ 前后严格对称（$W(\theta) = W(\pi - \theta)$）。
3. **深部非弹性散射（Deep Inelastic Collisions, DIC, $\tau_{\text{int}} \sim 10^{-20}\text{ s}$）**：
   - 介于直接反应与复合核之间的重离子反应过程，伴随巨大的动能损失、大量质量转移与大角动量耗散（Wilczynski 鸟喙图特征）。

### 1.3 光学模型（Optical Model）复数势
将弹核在靶核场中的大量复杂反应道等效为一个光学介质对德布罗意波的折射与吸收：
$$U(r) = - V f(r) - i W g(r) + V_{ls} \lambdabar_\pi^2 \frac{1}{r} \frac{df_{ls}(r)}{dr} (\vec{l}\cdot\vec{\sigma}) + V_C(r),$$
- 实部 $V \approx 40 - 50\text{ MeV}$：描述核平均势场引起的相移与相干弹性散射；
- 虚部 $W \approx 5 - 15\text{ MeV}$：描述所有非弹性与反应通道导致的入射粒子通量吸收（连续性方程中 $\nabla\cdot\vec{j} \neq 0$）；
- 表面导数形虚势（Surface-peaked $W$）：适用于低能中子与重离子周边吸收。
