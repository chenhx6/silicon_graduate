# Glossary: 实验核物理与探测器技术专用术语表

本术语表整理吴治华《原子核物理实验方法》与在束核谱学实验中的标准术语定义、符号体系与数学公式。

---

## 1. 统计与计数物理 (Statistics and Dead Time)

- **Dead Time (死时间 $\tau$)**: 探测系统在记录前一个脉冲后，由于物理电荷释放或电路成形处理尚未完成，在一段有限时间内对后续入射事件丧失响应的特性。
- **Non-Paralyzable Dead Time (不可扩展型/非麻痹型死时间 $\tau_N$)**: 死时间期间到达的新事件被完全忽略，且不延长现有的死时间间隔。真实输入率 $m = n / (1 - n \tau_N)$。
- **Paralyzable Dead Time (可扩展型/麻痹型死时间 $\tau_P$)**: 死时间期间到达的新事件虽然不能被记录为独立脉冲，但会从其到达时刻起重新启动一个新的死时间周期。记录率 $n = m e^{-m \tau_P}$。
- **Dual-Root Ambiguity (死时间双根退化)**: 在可扩展型死时间系统中，由于记录率随输入率呈现 $m e^{-m\tau}$ 的非单调单峰行为，每一个实测计数率 $n < n_m_{\max} = 1/(e\tau)$ 均对应两个数学上的实数输入率解（未饱和正常分支与阻塞瘫痪分支）。
- **Live-Time Fraction (活时间分数 $f_{\text{live}}$)**: 测量过程中系统处于可响应状态的有效时间与总时钟时间之比：$f_{\text{live}} = T_{\text{live}} / T_{\text{real}} = N_{\text{pulser,meas}} / N_{\text{pulser,injected}}$。

---

## 2. 半导体探测器与信号成形 (Semiconductor Detectors and Pulse Shaping)

- **Fano Factor (法诺因子 $F$)**: 描述辐射在物质中电离产生载流子数目的实际方差与纯泊松统计方差之比：$F = \sigma_N^2 / \bar{N}$。在 Ge 晶体中 $F \a0.08 - 0.12$（吴书取 $0.10$）。
- **Ballistic Deficit (弹道亏损)**: 探测器电荷收集时间 $t_c$ 的离散涨落导致成形放大器输出脉冲幅度产生人为压低与展宽的现象。消除条件为滤波成形脉冲必须具备平顶（Flat-top）：$T_{\text{flat}} \ge t_{c,\max}$。
- **Shockley-Ramo Theorem (肖克利-拉莫定理)**: 运动电荷 $q$ 在电极上感应出的瞬态瞬时电流由加权场 $\vec{E}_w$ 决定：$i(t) = q \vec{v}(t) \cdot \vec{E}_w(\vec{r})$。
- **Pole-Zero Cancellation (极零相消 PZC)**: 利用电阻-电容网络抵消前置放大器输出信号长指数衰减尾巴（$\tau \sim 50\text{ }\mu\text{s}$）引起的负向基线过冲（Undershoot），消除后续脉冲幅度被压低的问题。
- **Baseline Restorer (基线恢复器 BLR)**: 在高计数率下快速将脉冲尾部电位钳位回零伏基准电平的非线性电路或数字算法，消除低频热噪声漂移与基线波动。

---

## 3. $\gamma$ 谱学与符合测量 (Gamma Spectroscopy and Coincidence)

- **Photopeak Efficiency (全能峰探测效率 $\epsilon_p$)**: 探测器记录的全能吸收峰净面积与源发射的该能量 $\gamma$ 射线总数之比。
- **Peak-to-Total Ratio (峰总比 $P/T$)**: $\gamma$ 能谱中全能光电峰面积与全谱总计数（光电峰加康普顿散射连续谱）之比。未加屏蔽的同轴 HPGe 约为 $0.18 - 0.22$，加装 BGO 抗符合抑制套后可提升至 $0.55 - 0.65$。
- **True Coincidence Summing (真符合求和 TCS)**: 放射性核素衰变级联中相继发射的两个或多个 $\gamma$ 射线由于在分辨时间内同时进入同一晶体而被记录为一个求和脉冲的物理效应，导致级联各单峰计数损失并产生虚假加和峰。
- **Radford Background Subtraction (Radford 本底扣除法)**: 在二维 $\gamma-\gamma$ 符合矩阵中，利用一维总投影谱与平滑康普顿连续谱本底，严格剔除偶然符合与康普顿散射脊的二维解析扣本底算法。

---

## 4. 寿命与反应运动学 (Lifetimes and Reaction Kinematics)

- **Recoil Distance Method (反冲距离法 RDM / Plunger)**: 利用靶箔与阻挡箔之间的微米级精密可调距离 $d$，通过测量飞行中移动峰与减速后停止峰的强度比反演核能态寿命（测量范围 $1\text{ ps} - 1\text{ ns}$）。
- **Differential Decay Curve Method (差分衰变曲线法 DDCM)**: 现代 RDM 寿命解析算法，直接利用停止峰面积随距离的导数 $d I_s(d)/dd$ 反演能态寿命，彻底克服级联前级未知侧馈（Side-feeding）时间延迟对寿命测定的系统偏差。
- **Doppler Shift Attenuation Method (多普勒频移衰减法 DSAM)**: 利用反冲核在厚靶衬底点阵中减速放慢过程（$\sim 1\text{ ps}$）中发射 $\gamma$ 射线的多普勒线形畸变，结合 ZBL 离子阻止本领反演飞秒至皮秒级激发态寿命（$10\text{ fs} - 2\text{ ps}$）。
- **Vacuum Deorientation Effect (真空退取向效应)**: 反冲核在真空中自由飞行时，由于高度电离的原子未配对电子产生强超精细磁场与电场梯度，使核自旋发生快速拉莫尔进动，冲刷其角分布取向系数（取向衰减因子 $G_k < 1.0$）；通过在靶后镀制立方晶格金衬底（Au backer）可使反冲核瞬间阻停并消除该效应（$G_k \to 1.0$）。
