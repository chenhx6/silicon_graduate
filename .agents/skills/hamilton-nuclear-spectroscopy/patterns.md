# Reasoning Patterns: Hamilton 核谱学电磁相互作用分析范式

提炼自 W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》的 5 大角分布多极性反演、偏振仲裁与双根消解分析范式。

---

## Pattern 1: 方向角分布各向异性拟合与自旋序列初步划定范式

- **核心法则**：在束熔合蒸发反应中，核态沿束流垂直方向高度取向（$m \approx 0$ 优势布居）。测定各探头相对于束流轴角 $\theta$ 处的能谱峰面积，归一化后拟合勒让德多项式展开 $W(\theta) = 1 + A_2 P_2(\cos\theta) + A_4 P_4(\cos\theta)$，其展开系数的正负与绝对大小对自旋变化 $\Delta I = I_i - I_f$ 具有严格的几何约束。
- **标准划定程序**：
  1. 测定至少 3 到 6 个不同角度（如 $30^\circ, 55^\circ, 90^\circ, 125^\circ, 150^\circ$）处的净全能峰面积 $N_i$，并扣除探测器绝对探测效率 $\epsilon(\theta_i)$ 与探测器有限立体角衰减因子 $Q_2, Q_4$；
  2. 加权最小二乘拟合提取实验各向异性系数 $A_2^{\text{exp}}$ 与 $A_4^{\text{exp}}$；
  3. **特征自旋序列几何指纹初判**：
     - **拉伸纯电四极跃迁（$\Delta I = 2$, 如 $I \to I-2, E2$）**：
       理论各向异性系数呈现强烈的**正 $A_2$ 与负 $A_4$**：典型实测值为 $A_2 \approx +0.25 \sim +0.35$，$A_4 \approx -0.05 \sim -0.10$；
     - **拉伸纯偶极跃迁（$\Delta I = 1$, 如 $I \to I-1, D$）**：
       由于 $L=1$，四阶张量严格为零（$A_4 \equiv 0$），理论各向异性系数呈现**负 $A_2$**：典型实测值为 $A_2 \approx -0.15 \sim -0.25$，$A_4 \approx 0$；
     - **非拉伸偶极跃迁（$\Delta I = 0$, 如 $I \to I, D$）**：
       理论各向异性系数呈现**正 $A_2$**：典型实测值为 $A_2 \approx +0.30 \sim +0.45$，$A_4 \approx 0$；
     - **偶极-四极混合跃迁（$\Delta I = 1, M1+E2$）**：
       $A_2$ 与 $A_4$ 的数值强烈依赖于多极混合比 $\delta$，且 $A_4$ 不为零（表明含有高阶 $E2$ 辐射）。

---

## Pattern 2: 多极混合比 $\delta(E2/M1)$ 双根退化解析求解与判别式分析范式

- **核心法则**：对于任何包含多极混合（如 $M1+E2$）的辐射跃迁，各向异性系数是混合比 $\delta$ 的二次有理分式：$A_2(\delta) = B_2(I_i) \frac{F_2(1 1 I_f I_i) + 2\delta F_2(1 2 I_f I_i) + \delta^2 F_2(2 2 I_f I_i)}{1 + \delta^2}$。代入实验测量值后，方程严格化为一元二次代数方程，通常存在两个数学等价的解根。
- **标准求解程序**：
  1. 计算或查阅初态统计取向张量 $B_2(I_i)$（由反应自旋取向参数 $\sigma/I$ 确定）；
  2. 查表计算几何系数 $f_{11} = B_2 F_2(1 1 I_f I_i)$，$f_{12} = B_2 F_2(1 2 I_f I_i)$，$f_{22} = B_2 F_2(2 2 I_f I_i)$；
  3. 整理为标准一元二次多项式方程 $a \delta^2 + b \delta + c = 0$：
     $$a = f_{22} - A_2^{\text{exp}}, \quad b = 2 f_{12}, \quad c = f_{11} - A_2^{\text{exp}};$$
  4. **判别式核查**：
     $$\Delta = b^2 - 4 a c = 4 [ f_{12}^2 - (f_{22} - A_2)(f_{11} - A_2) ];$$
     - 若 $\Delta < 0$：无实数解（表明所选自旋假定错误，或实验测量值受系统误差污染）；
     - 若 $\Delta \ge 0$：严格导出两实数解根：
       $$\delta_1 = \frac{-b - \sqrt{\Delta}}{2a}, \quad \delta_2 = \frac{-b + \sqrt{\Delta}}{2a};$$
  5. **物理性质评估**：通常其中一个根绝对值极小（$|\delta_1| \le 0.2$，代表 $M1$ 占绝对主导的跃迁），另一个根绝对值极大（$|\delta_2| \sim 2 - 8$，代表 $E2$ 占绝大部分的集体跃迁）。

---

## Pattern 3: 康普顿线偏振度测量与电磁宇称选择定则排他性裁决范式

- **核心法则**：未极化角分布或普通 DCO 只能给出两个退化解根，无法断定究竟哪一个是真实物理根；康普顿线偏振度对多极混合比具有正负号相反的干涉项，能够以极高的统计显著性彻底打破双根简并。
- **标准裁决程序**：
  1. 利用分段 Clover 探测器或专用康普顿偏振仪测定垂直于反应平面的散射计数 $N_\perp$ 与平行于反应平面的计数 $N_\parallel$；
  2. 采用无偏振放射性源标定几何不对称因子 $a_{\text{geom}} = (N_\perp / N_\parallel)_{\text{unpol}}$；
  3. 计算实验散射不对称度与物理线偏振度：
     $$A_{\text{asym}} = \frac{N_\perp - a_{\text{geom}} N_\parallel}{N_\perp + a_{\text{geom}} N_\parallel}, \quad P_{\text{exp}} = \frac{A_{\text{asym}}}{Q(E_\gamma)};$$
  4. **理论线偏振度计算**（Hamilton 式 15.12）：
     在 $\theta = 90^\circ$ 处，根据两备选根 $\delta_1$ 与 $\delta_2$ 分别计算理论偏振度：
     $$P_{\text{theo}}(\delta) = \frac{\pm \frac{3}{2} B_2 H_2(L L' I_f I_i, \delta) - \frac{5}{8} B_4 H_4(L L' I_f I_i, \delta)}{1 - \frac{1}{2} A_2(\delta) + \frac{3}{8} A_4(\delta)};$$
     - 其中电辐射取正号，磁辐射取负号；
  5. **比较 $\chi^2$ 裁决物理真根**：
     $$\Delta\chi^2 = \frac{(P_{\text{exp}} - P_{\text{theo}}(\delta_2))^2}{\sigma_P^2} - \frac{(P_{\text{exp}} - P_{\text{theo}}(\delta_1))^2}{\sigma_P^2}.$$
     若 $\Delta\chi^2 \ge 25.0$（$5.0\sigma$），以确定无疑的实验置信度完全排除伪根，确立唯一起主导的电磁跃迁本质。

---

## Pattern 4: 未观测中间级联去取向 $U_k$ 连乘校正与初态取向反演范式

- **核心法则**：在复杂高自旋能级纲图中，目标能态往往不是由核反应直接完全布居，而是大部分来自上方更高自旋态的级联退激喂带（Feeding）。未被实验观测到的中间跃迁发射光子随机带走角动量，使得能态自旋取向被逐步抹平（去取向）。
- **标准校正程序**：
  1. 梳理上方主要的级联衰变路径：$I_0 \xrightarrow{L_1} I_1 \xrightarrow{L_2} I_2 \dots \xrightarrow{L_n} I_{\text{target}}$；
  2. 对路径上的每一步未观测跃迁，计算代数去取向因子 $U_k$：
     $$U_k(I_a I_b L) = (-1)^{I_a + I_b + L + k} \sqrt{(2I_a+1)(2I_b+1)} W(I_a I_a I_b I_b; k L);$$
  3. **级联累积衰减**：计算总衰减因子 $\mathcal{U}_k = \prod_{j=1}^n U_k(I_{j-1} I_j L_j)$；
  4. **有效取向张量重构**：目标能级发射 $\gamma$ 线的实际角分布展开系数修正为：
     $$A_k^{\text{eff}} = B_k(I_0) \cdot \mathcal{U}_k \cdot R_k(L, L', I_{\text{target}}, I_f);$$
  5. 消除由于忽略上方退激级联而误将自旋取向衰减归咎为多极混合比 $\delta$ 偏差的系统性推断错误。

---

## Pattern 5: $\arctan\delta$ 均匀网格轮廓似然拟合与非对称误差提取范式

- **核心法则**：由于多极混合比 $\delta \in (-\infty, +\infty)$ 在纯四极跃迁极限下会发散至无穷大，直接对 $\delta$ 采用常规高斯-牛顿梯度拟合极易在发散端出现数值溢出与梯度死锁。Hamilton 建议采用有界紧致角参数化 $\phi = \arctan\delta \in [-90^\circ, +90^\circ]$，在均匀网格上执行全域轮廓似然扫描。
- **标准拟合程序**：
  1. 将混合比参量变换为紧致无界角度：$\phi = \arctan\delta$；
  2. 在全区间 $[-90^\circ, +90^\circ]$ 内按等间距网格步长 $\Delta\phi \le 0.5^\circ$ 生成剖面网格；
  3. 在每个网格点 $\phi_i$ 固定值下，解析求解目标线性归一化参数 $A_0$ 与取向参数 $\sigma/I$ 的极小卡方值：
     $$\chi^2(\phi_i) = \min_{A_0, \sigma/I} \sum_{k=1}^{N_{\text{data}}} \frac{\left( W_{\text{theo}}(\theta_k; \phi_i, A_0, \sigma/I) - W_{\text{exp}}(\theta_k) \right)^2}{\sigma_k^2};$$
  4. 绘制全景轮廓似然曲线 $\chi^2(\phi)$；
  5. **非对称误差提取**：在最低极小点 $\chi_{\min}^2$ 处向上寻找切割交点 $\chi^2(\phi^\pm) = \chi_{\min}^2 + 1.00$（$68.27\%$ 置信度），换算回混合比：
     $$\delta = \tan\phi^*, \quad \Delta\delta^+ = \tan\phi^+ - \tan\phi^*, \quad \Delta\delta^- = \tan\phi^* - \tan\phi^-.$$
  输出严格考虑非线性与极值长尾的非对称误差：$\delta_{-\Delta\delta^-}^{+\Delta\delta^+}$。
