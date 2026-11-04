# Glossary: 林承键与 Bertulani 重离子核反应核心术语与物理定义

本术语表汇编林承键《重离子核反应》（科学出版社，2017）与 Bertulani & Danielewicz《Introduction to Nuclear Reactions》（CRC Press，2021）中的核心专业术语、中英文对照及严密物理定义，为在束重离子核反应实验设计与数据反演提供统一动力学语言。

---

## 1. 碰撞运动学与截面体系 (Kinematics and Cross Sections)

- **Center-of-Mass Frame (质心系 / c.m.)**: 总动量严格为零的相对运动参考系，其有效能量为 $E_{\text{c.m.}} = \frac{A_t}{A_p + A_t} E_{\text{lab}}$，约化质量 $\mu = \frac{A_p A_t}{A_p + A_t} u$。
- **Laboratory Frame (实验室系 / lab)**: 靶核处于静止状态的实验观测参考系。
- **Reaction Q-value (反应 Q 值)**: 反应初态各核基态静止质量总和减去末态各核基态静止质量总和：$Q = \sum M_{\text{initial}} c^2 - \sum M_{\text{final}} c^2$。$Q > 0$ 为放能反应，$Q < 0$ 为吸能反应。
- **Threshold Energy (绝对反应阈能 $E_{\text{th}}$)**: 吸能反应在实验室系中能够发生所需的最小弹核入射动能：$E_{\text{th}} = -Q \frac{A_p + A_t}{A_t}$。
- **Recoil Velocity (反冲核速度 $\beta$)**: 熔合形成的复合核沿束流前进方向的无量纲相对运动速度：$\beta = v_{\text{recoil}} / c \approx \frac{\sqrt{2 A_p E_{\text{lab}}}}{(A_p + A_t) u^{1/2} c}$。
- **Differential Cross Section (微分截面 $d\sigma/d\Omega$)**: 单位立体角内散射或反应出射粒子数占入射单位通量密度的几率度量，SI 常用单位为靶恩（$\text{b} = 10^{-28}\text{ m}^2$ 或毫靶 $\text{mb} = 10^{-31}\text{ m}^2$）。

---

## 2. 相互作用势与势垒穿透 (Interaction Potentials and Fusion Barriers)

- **Coulomb Barrier (库仑势垒 $V_C$)**: 两个带正电原子核接触前静电排斥能的极大峰值：$V_C \approx \frac{1.44 Z_1 Z_2}{R_1 + R_2}\text{ MeV}$。
- **Proximity Potential (接近势)**: 基于近距离微小表面间隙无旋液滴相互吸引力积分得到的短程核吸引势：$V_N(r) = 4\pi \gamma \frac{R_1 R_2}{R_1 + R_2} b \Phi(\zeta)$。
- **Bass Barrier (Bass 势垒)**: 实验广泛验证的经典宏观重离子熔合势垒参数化模型，考虑了核表面张力与库仑排斥的平衡。
- **Pocket Condition (势能口袋条件)**: 相互作用势随中心距 $r$ 出现局部极小值（势阱口袋），使得两核能经历暂态束缚并在旋转中熔合的力学充要判据。
- **Critical Angular Momentum ($\ell_n_{\text{crit}}$, 临界角动量)**: 能够克服离心势垒并落入内部势阱口袋的最大入射轨道角动量分波；当 $l > \ell_n_{\text{crit}}$ 时发生弹性、准弹性或深部非弹性散射，不再发生熔合。
- **Wong Formula (Wong 单抛物线势垒穿透公式)**: 将相互作用势在势垒极大值处局部展开为反转简谐抛物线所导出的全能区解析穿透公式：$\sigma_{\text{fus}} = \frac{\hbar\omega_B R_B^2}{2E_{\text{c.m.}}} \ln[1 + \exp(\frac{2\pi(E_{\text{c.m.}}-V_B)}{\hbar\omega_B})]$。
- **Fusion Barrier Distribution (熔合势垒分布 $D_{\text{fus}}(E)$)**: 熔合激发函数乘以能量后关于质心能量的二阶导数：$D_{\text{fus}}(E) = \frac{d^2(E_{\text{c.m.}} \sigma_{\text{fus}})}{d E_{\text{c.m.}}^2}$。

---

## 3. 散射动力学与光学模型 (Scattering and Optical Model)

- **Sommerfeld Parameter (索末菲参数 $\eta$)**: 衡量库仑力在散射碰撞中相对于经典动量重要性的无量纲特征量：$\eta = \frac{Z_1 Z_2 e^2}{\hbar v} = 0.1574 Z_1 Z_2 \sqrt{\frac{A_{\text{red}}}{E_{\text{c.m.}}}} \gg 1$。
- **Grazing Angle ($\theta_{\text{gr}}$, 掠射角)**: 对应两核表面恰好相切（中心距 $r = R_1 + R_2$）时的经典 Rutherford 偏转角：$\sin(\theta_{\text{gr}}/2) = \frac{\eta}{k (R_1 + R_2) - \eta}$。
- **Quarter-Point Angle ($\theta_{1/4}$, 1/4 截面角)**: 弹性散射微分截面与纯 Rutherford 截面之比下降至 0.25 时的散射角，严格用于反演核强相互作用接触半径 $R_{\text{int}}$。
- **Rainbow Scattering (彩虹散射)**: 经典偏转函数 $\Theta(l)$ 随碰撞参数减小到达极小极值点处的散射现象；在彩虹角 $\theta_R$ 处经典微分截面发散，量子效应产生特征 Airy 极大振荡。
- **Complex Optical Model (复光学模型势 $U(r) = V(r) + i W(r)$)**: 用实部势 $V(r)$ 描述弹性折射、虚部势 $W(r)$ 描述通量吸收（反应道损失）的有效单体唯象势场。

---

## 4. 直接反应与多核子转移 (Direct and Transfer Reactions)

- **Direct Reaction (直接反应)**: 碰撞在核表面掠射快速发生（时间尺度 $\sim 10^{-22}\text{ s}$），仅涉及少数几个价核子跃迁，反应角分布强烈向前角聚焦。
- **Optimum Q-value ($Q_{\text{opt}}$, 最优 Q 值)**: 使得入射通道与出射通道在接触点处经典库仑轨迹与径向动量达到最佳几何匹配的能量损失值：$Q_{\text{opt}} \approx \left(\frac{Z_{3} Z_{4}}{Z_1 Z_2} - 1\right) E_{\text{c.m.}}$。
- **DWBA (Distorted Wave Born Approximation, 扭曲波玻恩近似)**: 在复光学模型势求解的弹性散射扭曲波基底上，按一阶微扰论计算核子剥离（Stripping）或拾取（Pickup）转移反应跃迁矩阵元的微观理论。
- **Spectroscopic Factor ($S_{lj}$, 光谱因子)**: 实验测得的微观单粒子转移反应截面与纯极端独立粒子壳模型单粒子基准截面之比，直接反映真实核态中单粒子组态的占据纯度。

---

## 5. 深部非弹性碰撞 (Deep Inelastic Collisions, DIC)

- **Energy Relaxation (能量完全弛豫)**: 碰撞两核在接触窗口形成双核系统并经历剧烈摩擦力，大部分初始动能转化为内部热能，出射动能完全降至两形变核的出射库仑势垒附近。
- **Wilczynski Plot (维尔琴斯基图)**: 在质心散射角 $\theta_{\text{c.m.}}$ 与总动能损失（TKEL）构成的二维平面上绘制的双重微分截面等高线图，其特征“鸟嘴”轨迹直接揭示轨道角动量与能量的连续耗散。
- **Angular Momentum Dissipation (角动量耗散)**: 接触阶段两核表面强核粘滞力阻碍相对转动，将 $28\% - 35\%$ 的入射轨道角动量转化为两碎片的自转内禀角动量。

---

## 6. 复合核与统计衰变 (Compound Nucleus and Statistical Decay)

- **Compound Nucleus (复合核 / CN)**: 弹核与靶核完全熔合在一起、能量与动量在所有核子自由度上经历完全热力学平衡的极端高温致密核系统（寿命 $\sim 10^{-19} - 10^{-16}\text{ s}$）。
- **Bohr Independence Hypothesis (玻尔独立性假设)**: 复合核的衰变模式与其形成历史完全无关，仅取决于其总能量 $E$、总角动量 $J$ 与总宇称 $\pi$。
- **Hauser-Feshbach Theory (Hauser-Feshbach 统计截面理论)**: 在角动量与宇称完全守恒下，利用光学模型分波透射系数 $T_l$ 与剩余核连续能级密度积分严格计算各蒸发通道（$xn, yp, z\alpha$）截面分支的权威微观理论。
- **Level Density Parameter ($a$, 能级密度参数)**: 描述核温与费米能级处单粒子态密度的常数（$a \approx A / 8.5\text{ MeV}^{-1}$），在 Ignatyuk 唯象模型中随激发能升高展示壳效应的指数阻尼（$\sim e^{-\gamma U}$）。
- **Entry State Distribution (入口态分布)**: 复合核完成最后一颗蒸发粒子发射后、体系激发能落入中子分离能以下（$E^* < S_n$）时刻形成的剩余核在 $(E^*, I)$ 平面上的二维微观状态聚集区。
