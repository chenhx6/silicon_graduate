---
type: method
title: "低能重离子熔合蒸发实验设计与 Proposal 撰写全指南"
aliases: [重离子熔合实验设计, 实验Proposal指南, Fusion-Evaporation Experiment Design, 重离子实验方案]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
topics: [heavy-ion-fusion, fusion-evaporation, experiment-design, beam-energy-selection, cross-section-calculation]
---

# 低能重离子熔合蒸发实验设计与 Proposal 撰写全指南

## 1. 物理全景与实验设计目标

在低能实验核结构研究中，利用重离子熔合蒸发反应（Heavy-Ion Fusion-Evaporation Reaction）布居中高自旋态是探测三轴形变、摆动运动（wobbling）、手征双重带（chiral doublet bands）以及形状共存的最有效手段。

撰写一份具备强竞争力、可直接提交至国内外大型加速器实验室（如中国原子能科学研究院 CIAE HI-13 串列、中科院近代物理研究所 HIRFL、南非国家研究基金会 iThemba LABS、芬兰 Jyväskylä JYFL 等）的束流申请（Beam-time Proposal），必须完成以下**六大核心物理与工程计算**：
1. **弹核与靶核的最佳组合选择（Entrance Channel Selection）**；
2. **最佳入射束流能量计算（Beam Energy Optimization）**；
3. **复合核激发能与出射蒸发道竞争（$xn, yp, z\alpha$ 蒸发窗计算）**；
4. **反冲核运动学与多普勒展宽控制（Kinematics & Doppler Broadening）**；
5. **靶厚选择与有效能量展宽（Target Thickness & Energy Loss）**；
6. **束流强度、实验计数率与机时需求核算（Count Rate & Beam Time Estimation）**。

---

## 2. 核心物理公式与计算步骤

### 步骤 1：运动学转换与质心能量 $E_{\text{cm}}$
设入射束流弹核质量数为 $A_p$、电荷数为 $Z_p$，实验室系束流能量为 $E_{\text{lab}}$（MeV）；静止靶核质量数为 $A_t$、电荷数为 $Z_t$。
质心系有效碰撞能量 $E_{\text{cm}}$ 为：
$$E_{\text{cm}} = E_{\text{lab}} \frac{A_t}{A_p + A_t}$$

### 步骤 2：相互作用半径与标称库仑势垒 $V_B$
根据林承键《重离子核反应》中的 Bass 势垒模型与接触半径公式：
$$R_B = r_0 (A_p^{1/3} + A_t^{1/3}) + \Delta R \quad (\text{通常取 } r_0 \approx 1.07\text{ fm}, \Delta R \approx 2.72\text{ fm})$$
接触面间的标称库仑势垒为：
$$V_B = \frac{e^2}{4\pi\epsilon_0} \frac{Z_p Z_t}{R_B} \approx 1.44 \frac{Z_p Z_t}{R_B}\text{ (MeV)}$$
**实验设计准则**：为使弹核有效克服库仑斥力发生核接触，同时不使体系发生剧烈的深部非弹性散射或准裂变，入射能量通常选择在势垒上：
$$E_{\text{cm}} = V_B + (5 \sim 25\text{ MeV})$$

### 步骤 3：临界角动量 $\ell_{\text{crit}}$ 与总熔合截面 $\sigma_{\text{fus}}$
入射重离子的相对运动带来极高的轨道角动量。体系能够承受的擦边角动量为：
$$\ell_{\text{max}} = R_B \sqrt{\frac{2\mu}{\hbar^2} (E_{\text{cm}} - V_B)} \approx 0.2199 R_B \sqrt{\mu (E_{\text{cm}} - V_B)}$$
其中折合质量 $\mu = \frac{A_p A_t}{A_p + A_t}$（以原子质量单位 u 计）。
由于复合核在高旋转下裂变势垒急剧降低，对于 $A\sim 130$ 质量区核，复合核能承受的最大角动量极限通常为 $\ell_{\text{crit}} \approx 45 \sim 55\hbar$。
总熔合截面 $\sigma_{\text{fus}}$ 估算为：
$$\sigma_{\text{fus}} \approx \pi R_B^2 \left( 1 - \frac{V_B}{E_{\text{cm}}} \right) \quad (\text{单位：} 1\text{ fm}^2 = 10\text{ mb})$$

### 步骤 4：复合核激发能 $E^*$ 与蒸发道选择
完全熔合形成复合核 $(A_{\text{CN}}, Z_{\text{CN}}) = (A_p + A_t, Z_p + Z_t)$，其初态激发能为：
$$E^* = E_{\text{cm}} + Q_{\text{fus}} = E_{\text{cm}} + [M(A_p, Z_p) + M(A_t, Z_t) - M(A_{\text{CN}}, Z_{\text{CN}})] c^2$$
其中 $M$ 为核基态质量亏损（查 AME2020）。
**蒸发道竞争物理规律**：
- 每个蒸发中子带走一个分离能 $S_n \approx 8\text{ MeV}$ 以及中子的动能 $2T \approx 2 \sim 3\text{ MeV}$，即蒸发一个中子平均消耗约 $10 \sim 11\text{ MeV}$ 的激发能。
- 典型 $xn$ 蒸发窗口：
  - $3n$ 反应道最佳激发能：$E^* \approx 35 \sim 42\text{ MeV}$；
  - $4n$ 反应道最佳激发能：$E^* \approx 45 \sim 55\text{ MeV}$；
  - $5n$ 反应道最佳激发能：$E^* \approx 58 \sim 68\text{ MeV}$。

### 步骤 5：反冲核速度 $\beta = v/c$ 与多普勒展宽
复合核因动量守恒在实验室系具有前冲速度：
$$P_{\text{CN}} = P_p \implies \beta = \frac{v_{\text{recoil}}}{c} \approx \sqrt{\frac{2 E_{\text{lab}}}{A_p \times 931.5}} \frac{A_p}{A_p + A_t}$$
反冲速度 $\beta$ 通常在 $1.5\% \sim 3.0\%$ 之间。
在束发射的 $\gamma$ 射线在实验室系角 $\theta_d$ 处产生多普勒频移：
$$E_\gamma(\theta_d) = E_{\gamma 0} \frac{\sqrt{1-\beta^2}}{1 - \beta \cos\theta_d} \approx E_{\gamma 0} (1 + \beta \cos\theta_d)$$
**多普勒展宽公式（能量分辨率劣化项）**：
$$\Delta E_D = E_{\gamma 0} \beta \sin\theta_d \cdot \Delta\theta_d$$
其中 $\Delta\theta_d$ 为 HPGe 探测器的立体角半张角。在设计靶室与探测器距离时，必须使 $\Delta E_D$ 匹配 HPGe 的固有分辨率（约 2 keV），否则谱线将严重宽化！

---

## 3. Proposal 中的实验参数核算模板

在向加速器实验室提交 Proposal 时，必须列出标准的**计数率预算表（Count Rate Budget）**：

1. **靶核面密度 $N_t$**：
   $$N_t = \frac{\rho \cdot d \cdot N_A}{M_t} \quad (\text{核子数}/\text{cm}^2)$$
   若靶厚 $w = 1.0\text{ mg/cm}^2$，同位素丰度为 $f_{\text{iso}}$，则 $N_t = \frac{10^{-3} \times f_{\text{iso}} \times 6.022 \times 10^{23}}{M_t}$。
2. **束流粒子流强 $I_p$**：
   若束流强度为 $I = 2\text{ pnA}$（粒子纳安），则粒子发射率 $\Phi_p = \frac{I}{e} = \frac{2 \times 10^{-9}}{1.602 \times 10^{-19}} \approx 1.25 \times 10^{10}\text{ 粒子/秒}$。
3. **目标残核生成率 $R_{\text{prod}}$**：
   $$R_{\text{prod}} = \Phi_p \cdot N_t \cdot \sigma_{\text{channel}}$$
   （例如 $\sigma_{4n} \approx 300\text{ mb} = 300 \times 10^{-27}\text{ cm}^2$）。
4. **双符合（$\gamma-\gamma$）有效事件率**：
   $$R_{\gamma\gamma} = R_{\text{prod}} \cdot b_\gamma \cdot \epsilon_{\text{array}}^2 \cdot P_{\text{coinc}}$$
   其中 $\epsilon_{\text{array}}$ 为探测器阵列全能峰总效率（如 10 台 HPGe 阵列通常为 $1\% \sim 3\%$），$b_\gamma$ 为级联分支比。
5. **统计学门槛需求**：
   为在 $\gamma-\gamma$ 矩阵中清晰辨识高自旋微弱跃迁（峰本比约 1:5），单条关键弱线门内全能峰净计数不得少于 $10^3$ counts，由此倒推总有效机时（通常为 72–120 小时）。
