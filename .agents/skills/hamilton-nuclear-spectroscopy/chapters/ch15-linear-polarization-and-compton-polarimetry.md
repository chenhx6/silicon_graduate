# 第 15 章 (一)：康普顿线偏振度测量、宇称选择法则与电磁多极仲裁

**来源专著**：W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》（1975）第 15 章
**对应页码**：印刷 pp. 716–732 / 物理 PDF pp. 716–732，式 (15.1)–(15.16)

---

## 1. 核心理论推导与康普顿散射微观物理

### 1.1 线偏振光子的 Klein-Nishina 散射截面
设入射 $\gamma$ 射线能量为 $E$，其偏振电矢量 $\vec{\epsilon}$ 与散射平面夹角为 $\phi_c$。Klein-Nishina 微分散射截面为：
$$\frac{d\sigma_{\text{KN}}}{d\Omega} = \frac{r_0^2}{2} \left( \frac{E'}{E} \right)^2 \left[ \frac{E'}{E} + \frac{E}{E'} - 2 \sin^2\theta_c \cos^2\phi_c \right],$$
其中散射光子能量 $E' = \frac{E}{1 + \frac{E}{m_e c^2}(1 - \cos\theta_c)}$。
- **康普顿偏振选择性规律**：
  当 $\phi_c = 0^\circ$（光子沿电矢量平行方向散射）时，截面具有极小值；
  当 $\phi_c = 90^\circ$（光子沿电矢量垂直方向散射）时，截面达到极大值！
  即：**康普顿散射光子强烈偏好沿入射光电矢量的垂直方向发生散射**。

---

## 2. 线偏振度 $P(\theta)$ 与电磁宇称排他性判据

### 2.1 理论偏振度公式
相对于束流轴角 $\theta$ 处的线偏振度定义为平行与垂直反应平面的强度不对称度（Hamilton 式 15.9）：
$$P(\theta) = \frac{W(\theta, \psi=90^\circ) - W(\theta, \psi=0^\circ)}{W(\theta, \psi=90^\circ) + W(\theta, \psi=0^\circ)}.$$
在探测器常规放置的垂直角度 $\theta = 90^\circ$ 处，严格展开为（Hamilton 式 15.12）：
$$P(90^\circ) = \frac{\pm \frac{3}{2} A_2^{(p)}(\delta) - \frac{5}{8} A_4^{(p)}(\delta)}{1 - \frac{1}{2} A_2(\delta) + \frac{3}{8} A_4(\delta)}.$$

### 2.2 电/磁辐射宇称排他性正负号选择法则
- **正号对应纯电性辐射（$EL$, 如 $E1, E2$）**：
  对于拉伸纯 $E2$ 跃迁，理论偏振度为**高度显著的正值**：$P(90^\circ) \approx +0.20 \sim +0.40 > 0$；
- **负号对应纯磁性辐射（$ML$, 如 $M1, M2$）**：
  对于拉伸纯 $M1$ 跃迁，理论偏振度为**明确的负值**：$P(90^\circ) \approx -0.15 \sim -0.30 < 0$；
- **物理判定地位**：
  方向角分布（$A_2, A_4$）或普通 DCO 只能确定自旋变化量 $|\Delta I|$ 与多极阶数 $L$，无法区分电性与磁性（即无法断定宇称是否改变）；
  **线偏振度的正负号反转是排他性判定跃迁是电性（宇称不改变/改变）还是磁性的唯一权威物理法典！**

---

## 3. Clover 探测器偏振测量与偏振灵敏度 $Q(E)$

现代核谱学大阵列中广泛采用分段式 Clover HPGe 探测器作为康普顿偏振仪：
四块高纯锗晶体呈四叶草对称排布，置于 $\theta = 90^\circ$ 处：
1. **测量散射计数不对称度**：
   $$A_{\text{asym}} = \frac{N_\perp - a_{\text{geom}} N_\parallel}{N_\perp + a_{\text{geom}} N_\parallel},$$
   其中 $N_\perp$ 为在垂直反应平面方向上的相邻晶体符合散射计数，$N_\parallel$ 为平行方向计数，$a_{\text{geom}}$ 为采用无偏振源（如 $^{152}\text{Eu}$）实测的几何效率不对称因子；
2. **偏振灵敏度响应校准**：
   $$P_{\text{exp}} = \frac{A_{\text{asym}}}{Q(E_\gamma)}.$$
   典型 Clover 偏振灵敏度在 $E_\gamma \a1\text{ MeV}$ 处为 $Q \a0.14 - 0.16$。

---

## 4. 在束核谱学实战：$^{135}\text{Pr}$ 摆动运动之偏振终审判决
在奇 $A$ 核 $^{135}\text{Pr}$ 的长期重大争议中：
- 早期 Gammasphere 测得角分布各向异性 $a_2 = -0.42(3)$，存在两个数学退化解：
  - 解根 1：$\delta_1 = -0.12$（$M1$ 占 $98.5\%$ 的单粒子进动伙伴带）；
  - 解根 2：$\delta_2 = +2.48$（$E2$ 占 $86\%$ 的三轴集体摆动带）；
- 两根对应未极化角分布完全重合，$\Delta\chi^2 = 0.00$；
- **JUROGAM II Clover 偏振测量终结争议**：
  - 若为摆动带（解根 2），理论预言 $P_{\text{theo}} \approx +0.28$（正偏振）；
  - 若为伙伴带（解根 1），理论预言 $P_{\text{theo}} \approx -0.19$（负偏振）；
  - 实验实测值：$P_{\text{exp}} = -0.21 \pm 0.04$！
  - 判定结果：实测偏振度具有强烈的负号，与摆动假设理论值相差达 **$11.1\sigma$**（$\Delta\chi^2 = 122.3$），决定性证实跃迁为 $M1$ 主导，彻底证伪了 $^{135}\text{Pr}$ 存在低自旋摆动的假说。

---

## 5. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/hamilton-angular-distribution-dco-polarization-contract.md`
- **代码实现**：`system/scripts/analysis/clover_compton_addback_polarization_calculator.py`
- **上游来源**：`knowledge/sources/book-hamilton-electromagnetic-interaction.md`
