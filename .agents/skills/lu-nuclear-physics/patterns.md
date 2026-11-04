# Reasoning Patterns: 卢希庭核物理基础推理与计算范式

提炼自卢希庭《原子核物理（修订版）》的 5 大基础核理论推导与工程计算范式。

---

## Pattern 1: 结合能差分、核分离能与滴线位置计算范式

- **核心法则**：原子核的稳定性由核子分离能正负决定。当中子分离能 $S_n \le 0$ 时到达中子滴线（Neutron drip line）；当质子分离能 $S_p \le 0$ 时到达质子滴线。
- **标准计算程序**：
  1. 由原子质量 $M(A, Z)$ 或质量过剩 $\Delta(A, Z) = [M(A, Z) - A] c^2$ 计算中子分离能：
     $$S_n(A, Z) = [\Delta(A-1, Z) + \Delta_n - \Delta(A, Z)] c^2,$$
     其中中子质量过剩 $\Delta_n = 8.071\text{ MeV}$；
  2. 计算双中子分离能（消除奇偶配对效应扰动）：
     $$S_{2n}(A, Z) = [\Delta(A-2, Z) + 2\Delta_n - \Delta(A, Z)] c^2;$$
  3. 绘制 $S_{2n}$ 随中子数 $N$ 的变化曲线。若曲线在某幻数（如 $N=8, 20, 28, 50, 82$）处出现急剧向下的断崖式台阶，证明该中子数对应壳层闭壳；若断崖消失，预示产生反转岛（Island of Inversion）或壳层淬灭。

---

## Pattern 2: $\beta$ 衰变类型判定与 $\log ft$ 比较半衰期推算范式

- **核心法则**：实测半衰期 $T_{1/2}$ 强烈依赖于衰变端点能量 $E_0$（相空间因子 $f \propto E_0^5$），绝不能用实测半衰期长短直接衡量衰变几率，必须转换为无量纲比较半衰期 $\log ft$。
- **标准推算程序**：
  1. 测定 $\beta$ 能谱，通过 Fermi-Kurie 图线性外推确定真实端点能量 $E_0$；
  2. 查表或利用费米积分函数解析积分计算相空间因子 $f(Z, E_0)$；
  3. 计算比较半衰期乘积：$ft = f(Z, E_0) \cdot T_{1/2}$（$T_{1/2}$ 必须换算为秒 $\text{s}$）；
  4. 由 $\log_{10} ft$ 的数值区间裁决跃迁类型：
     - $\log ft = 3.0 - 3.6$：**超允许跃迁（Superallowed）**，初始态与终态属于同一同位旋多重态的同位旋类似态（IAS），矩阵元 $|M_{fi}|^2 \approx 2$；
     - $\log ft = 4.0 - 6.0$：**允许跃迁（Allowed）**，无轨道角动量带出（$L=0$），包括允许 Fermi（$\Delta I=0$）与允许 Gamow-Teller（$\Delta I=0, \pm 1$）；
     - $\log ft = 6.0 - 9.0$：**一阶禁戒跃迁（First-Forbidden）**，带出 $L=1$ 轨道角动量，发生宇称改变（$\Delta \pi = \text{yes}$）；
     - $\log ft > 9.0$：**高阶禁戒跃迁（Unique Forbidden）**，多重角动量抑制。

---

## Pattern 3: $\gamma$ 跃迁多极性竞争与混合比 $\delta$ 估算范式

- **核心法则**：辐射几率随多极阶数 $L$ 急剧降低（每升高一阶下降 $10^4 - 10^5$ 倍）；在同一多极阶数下，电辐射通常比磁辐射强约两个数量级：$T(EL) \a10^2 \cdot T(ML)$。
- **跃迁竞争判定准则**：
  1. 当宇称不改变且自旋差 $\Delta I = 1$ 时，允许最低多极跃迁为 $M1$（角动量 $L=1$）与 $E2$（角动量 $L=2$）；
  2. 尽管 $E2$ 为高一阶多极，但在变形核集体增强效应下（$B(E2) \sim 10 - 200\text{ W.u.}$），集体 $E2$ 能够与未增强甚至受阻的单粒子 $M1$ 强烈竞争，形成具有可观多极混合比 $\delta(E2/M1)$ 的混合跃迁；
  3. 混合比定义为：$\delta = \frac{\langle I_f || \mathcal{M}(E2) || I_i \rangle}{\langle I_f || \mathcal{M}(M1) || I_i \rangle}$，其中光子强度比为 $I_\gamma(E2)/I_\gamma(M1) = \delta^2$。

---

## Pattern 4: 核反应运动学 $Q$ 方程、出射粒子动能与阈能计算范式

- **核心法则**：非相对论核反应 $A(a, b)B$ 的能量与动量守恒导向著名的反应 $Q$ 方程。
- **标准计算程序**：
  1. 由质量亏损计算反应能 $Q$：$Q = (M_A + M_a - M_B - M_b) c^2$；
  2. 若 $Q < 0$（吸热反应），由质心系动能限制求出实验室系绝对阈能：
     $$E_{\text{th}} = |Q| \left(1 + \frac{M_a}{M_A}\right);$$
  3. 对于出射角 $\theta_b$（实验室系相对于入射束流方向），出射轻粒子 $b$ 的动能 $E_b$ 满足二元二次方程：
     $$\sqrt{E_b} = \frac{\sqrt{M_a M_b E_a} \cos\theta_b \pm \sqrt{M_a M_b E_a \cos^2\theta_b + (M_B + M_b)[M_B Q + (M_B - M_a)E_a]}}{M_B + M_b}.$$

---

## Pattern 5: 共振截面 Breit-Wigner 单能级分析与热中子 $1/v$ 定律范式

- **核心法则**：当入射粒子（特别是低能慢中子）能量接近复合核某个准束缚单能级 $E_0$ 时，反应截面呈现尖锐共振峰。
- **计算与分析程序**：
  1. 复合核总衰变宽度为各出射道分宽度之和：$\Gamma = \Gamma_n + \Gamma_\gamma + \Gamma_\alpha + \dots$；
  2. 弹性散射截面与辐射捕获截面由 Breit-Wigner 公式严格给出：
     $$\sigma_{n\gamma}(E) = \pi \lambdabar^2 g_J \frac{\Gamma_n \Gamma_\gamma}{(E - E_0)^2 + (\Gamma/2)^2};$$
  3. 当中子能量远低于第一共振能级时（$E \ll E_0$），中子分宽度主要由出射通道的渗透率控制（$\Gamma_n \propto \sqrt{E}$），而德布罗意波长平方反比于能量（$\lambdabar^2 \propto 1/E$）：
     $$\sigma_{n\gamma}(E) \propto \frac{1}{E} \cdot \frac{\sqrt{E} \cdot \Gamma_\gamma}{E_0^2 + (\Gamma/2)^2} \propto \frac{1}{\sqrt{E}} \propto \frac{1}{v}.$$
     严格证明了热中子和慢中子捕获截面普遍遵循的 **$1/v$ 吸收定律**。
