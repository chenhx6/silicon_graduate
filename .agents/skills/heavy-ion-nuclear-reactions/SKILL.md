---
name: heavy-ion-nuclear-reactions
description: "林承键《重离子核反应》与 Bertulani《Introduction to Nuclear Reactions》：重离子碰撞运动学、接近势与 Bass 势垒、菲涅耳弹性散射、Wong 熔合穿透公式、Rowley 势垒分布、深部非弹性碰撞 Wilczynski 图、Hauser-Feshbach 统计蒸发与在束实验激发函数设计指南。"
---

<!-- argument-hint: [topic, formula, reaction-channel, or chapter name] -->

# 重离子核反应（林承键 & Bertulani）

**著述基准**：
- 林承键（中国原子能科学研究院）《重离子核反应》，科学出版社 (2017)，223 页
  本地原件：`raw/books/重离子核反应 (林承键) (Z-Library).pdf` (SHA-256 `792bfe7f7807623b7e1439b32eddb7320ab3ec6bf6be7e3894b436c1c9f65b2e`)
- Carlos A. Bertulani & Pawel Danielewicz *Introduction to Nuclear Reactions* (2nd Ed.), CRC Press (2021), 421 页
  本地原件：`raw/books/Introduction to Nuclear Reactions (C.A. Bertulani P. Danielewicz) (Z-Library).pdf` (SHA-256 `ad1391abd781e2277433283b6635679cfc45efc9d9d5472d4aabcd172509cb71`)

本技能提炼两部权威专著中关于重离子弹性散射、相互作用势、熔合势垒穿透、耦合道效应、深部非弹性散射、Hauser-Feshbach 统计蒸发衰变及在束反应靶核实验设计的核心物理框架与工程算法，为低能核结构在束 $\gamma$ 谱学实验设计与高自旋激发态布居提供第一性动力学支撑。

## How to Use This Skill

- **碰撞运动学与坐标变换**：询问 `质心系变换`、`库仑激发反冲动能`、`反应Q方程`、`出射粒子多普勒速度beta`；
- **相互作用势与势垒穿透**：询问 `库仑势垒高度`、`接近势Proximity`、`Bass势参数`、`Wong抛物线穿透公式`、`临界角动量`；
- **弹性散射与光学模型**：询问 `Sommerfeld参数`、`Rutherford截面`、`菲涅耳1/4截面点`、`彩虹散射Airy结构`、`强吸收半径`；
- **近垒熔合与势垒分布**：询问 `Rowley势垒分布`、`二阶导数反演`、`耦合道效应`、`基态四极形变对熔合的增强`；
- **深部非弹性散射 (DIC)**：询问 `Wilczynski能量-角度图`、`能量完全弛豫`、`轨道角动量耗散`、`转动角动量转移`；
- **统计蒸发与通道竞争**：询问 `Hauser-Feshbach截面`、`Bohr独立性假设`、`能级密度参数a与壳阻尼`、`xn与yp道竞争`；
- **在束实验设计全流程**：询问 `最佳束流能量选择`、`激发函数极大值计算`、`靶厚优化与能损`、`衬底选择与寿命测量匹配`。

---

## Core Frameworks and Mental Models

1. **重离子两体碰撞运动学与质心系变换法则（第 1 章）**：
   - 实验室系入射动能 $E_{\text{lab}}$，弹核质量 $A_p$ 与靶核质量 $A_t$；
   - **质心系有效能量 (Center-of-Mass Energy)**：
     $$E_{\text{c.m.}} = \frac{A_t}{A_p + A_t} E_{\text{lab}};$$
   - **复合核初态激发能 (Compound Nucleus Excitation Energy)**：
     $$E^* = E_{\text{c.m.}} + Q_{\text{fus}} = E_{\text{c.m.}} + [M(A_p, Z_p) + M(A_t, Z_t) - M(A_{\text{CN}}, Z_{\text{CN}})] c^2;$$
   - **复合核沿束流方向的反冲动能与反冲速度 $\beta = v/c$**：
     $$E_{\text{recoil}} = \frac{A_p}{A_p + A_t} E_{\text{c.m.}}, \quad \beta = \frac{v_{\text{recoil}}}{c} \approx \sqrt{\frac{2 E_{\text{recoil}}}{M_{\text{CN}} c^2}} = \frac{\sqrt{2 A_p E_{\text{lab}}}}{(A_p + A_t) u^{1/2} c}.$$
     反冲速度 $\beta$ 决定了多普勒线形分析（DSAM/RDDS）的多普勒频移幅度 $\Delta E_\gamma / E_{\gamma 0} = \beta \cos\theta_{\text{det}}$。

2. **重离子相互作用势与经典 Bass 熔合势垒（第 2 章）**：
   - 两个重离子中心距离为 $r$ 时的总径向相互作用势为库仑势、核相互作用势与离心势之和：
     $$V_l(r) = V_C(r) + V_N(r) + \frac{\hbar^2 l(l+1)}{2 \mu r^2};$$
   - **Bass 经验熔合势垒公式**（在束熔合反应最精准宏观标尺）：
     $$V_B = \frac{1.44 Z_1 Z_2}{R_B} - \frac{R_1 R_2}{R_1 + R_2} \frac{d_B}{a_B} \exp\left(-\frac{R_B - R_1 - R_2}{d_B}\right),$$
     其中半径参数 $R_i = 1.16 A_i^{1/3} - 1.39 A_i^{-1/3}\text{ fm}$，势垒半径 $R_B \approx R_1 + R_2 + 2.0\text{ fm}$。$E_{\text{c.m.}} \ge V_B$ 为发生完全熔合反应的经典门槛。

3. **弹性散射、菲涅耳衍射与 1/4 截面点强吸收定理（第 3 章）**：
   - 库仑相互作用由 Sommerfeld 参数控制：$\eta = \frac{Z_1 Z_2 e^2}{\hbar v} = 0.1574 Z_1 Z_2 \sqrt{\frac{A_{\text{red}}}{E_{\text{c.m.}} [\text{MeV}]}}$；重离子反应中通常 $\eta \gg 1$（强库仑主导）；
   - 当角分布比值 $\sigma(\theta) / \sigma_R(\theta)$ 出现特征菲涅耳干涉振荡，并下落至 $1/4$（$0.25$）处时，对应临界强吸收角 $\theta_{1/4}$：
     $$R_{\text{int}} = \frac{\eta}{k} \left[ 1 + \csc\left(\frac{\theta_{1/4}}{2}\right) \right].$$
     为实验直接提取核接触相互作用半径提供无模型依赖的强吸收标尺。

4. **熔合截面 Wong 穿透公式与 Rowley 势垒分布（第 6 章）**：
   - **Wong 单抛物线势垒穿透公式**：
     $$\sigma_{\text{fus}}(E_{\text{c.m.}}) = \frac{\hbar\omega_B R_B^2}{2 E_{\text{c.m.}}} \ln\left[ 1 + \exp\left( \frac{2\pi (E_{\text{c.m.}} - V_B)}{\hbar\omega_B} \right) \right],$$
     其中 $\hbar\omega_B \sim 3 - 5\text{ MeV}$ 描述势垒曲率反转宽度。当 $E_{\text{c.m.}} \gg V_B$ 时，精确还原为经典几何截面：$\sigma_{\text{fus}} \approx \pi R_B^2 (1 - V_B / E_{\text{c.m.}})$；
   - **Rowley 熔合势垒分布二阶导数反演定理**：
     $$D_{\text{fus}}(E_{\text{c.m.}}) \equiv \frac{d^2(E_{\text{c.m.}} \sigma_{\text{fus}})}{d E_{\text{c.m.}}^2}.$$
     单势垒下 $D_{\text{fus}}(E)$ 为半高宽 $\text{FWHM} = 0.56 \hbar\omega_B$ 的单峰；在弹核/靶核存在基态四极形变 $\beta_2$ 或八极声子耦合时，势垒分裂为多重分立峰，证明核形变在近垒能区对熔合截面具有**数个数量级的超强动力学增强**！

5. **深部非弹性散射 (DIC) 与 Wilczynski 图谱（第 5 章）**：
   - 碰撞参数介于准弹性与完全熔合之间（$l_{\text{fus}} < l < l_{\text{DIC}}$），系统经历两体粘滞接触；
   - **能量完全弛豫**：总动能损失（TKEL）可高达数百 $\text{MeV}$，几乎耗尽全部超垒动能；
   - **轨道角动量耗散与内禀自旋布居**：粘滞力矩使得 $28\% - 35\%$ 的相对轨道角动量转化为碎片的内禀自旋（可布居高达 $40 - 50\hbar$ 的非满壳高自旋异能态）；
   - **Wilczynski 能量-角度二维截面脊线**：在 $(\theta_{\text{c.m.}}, \text{TKEL})$ 图上呈现向负偏转角旋转延伸的典型“鸟嘴”轨迹，是辨识完全弛豫深部非弹碰撞的核心实验证据。

6. **复合核统计衰变与 Hauser-Feshbach 蒸发窗（第 7 章）**：
   - 复合核初态具有高激发能 $E^*$ 与高自旋分布（最高达裂变极限 $\ell_n_{\text{crit}} \sim 60 - 70\hbar$）；
   - **Bohr 独立性原理**：复合核在微秒极短时间内达到统计热平衡，衰变道选择与形成历史无关；
   - **Hauser-Feshbach 蒸发竞争**：中子发射无库仑势垒阻挡（$V_C=0$），每个蒸发中子平均带走约 $B_n + 2T \sim 10 - 12\text{ MeV}$ 能量，但仅带走约 $1 - 2\hbar$ 轨道角动量；
   - 经过 $4 - 5$ 步中子蒸发后，体系落入粒子结合能以下区域（$E^* < S_n$），在高自旋区形成极其集中的**在束高自旋入口态（Entry States）自旋窗口（$I \sim 20 - 45\hbar$）**，随后纯粹通过快速统计 $\gamma$ 射线与高自旋退激跃迁级联落到 Yrast 线与手征/摆动带！

---

## Chapter Index

| # | 章节主题 | 核心数学方法与实验应用 |
|---|---|---|
| [ch01](chapters/ch01-kinematics-and-scattering.md) | 重离子碰撞运动学与坐标系变换 | 质心系变换、反冲角、动能损失与反冲核多普勒初速 $\beta$ |
| [ch02](chapters/ch02-heavy-ion-interaction-potentials.md) | 重离子相互作用势与 Bass 熔合势垒 | 库仑势、接近势 (Proximity)、Bass 势垒解析参数与口袋条件 |
| [ch04](chapters/ch04-quasi-elastic-and-transfer-reactions.md) | 准弹性散射与 DWBA 多核子转移反应 | 掠射角、最优 $Q$ 匹配条件 ($Q_{\text{opt}}$)、动量转移与光谱因子提取 |
| [ch05](chapters/ch05-deep-inelastic-collisions-and-wilczynski.md) | 深部非弹性散射 (DIC) 与耗散动力学 | 能量完全弛豫、角动量耗散转矩、Wilczynski 图与高自旋丰中子产生 |
| [ch06](chapters/ch06-fusion-dynamics-and-barrier-distribution.md) | 熔合截面、Wong 公式与势垒分布 | 临界角动量 $\ell_n_{\text{crit}}$、Wong 公式、Rowley 势垒分布二阶导数与形变耦合道 |
| [ch07](chapters/ch07-compound-nucleus-decay-and-statistical-evaporation.md) | 复合核统计衰变与 Hauser-Feshbach 蒸发窗 | Hauser-Feshbach 公式、能级密度 Ignatyuk 壳阻尼、$xn/yp/z\alpha$ 竞争与入口态窗口 |
| [guide](chapters/heavy-ion-experiment-design-guide.md) | 重离子核反应在束实验设计全流程指南 | 最佳束能选择、激发函数极大值、靶厚/能损优化、衬底选择与机时预算 |

## Supporting Reference Files

- [glossary.md](glossary.md) — 重离子核反应动力学、势能曲面与实验设计术语中英双语定义。
- [patterns.md](patterns.md) — 5 大重离子反应实验设计与数据反演核心范式。
- [cheatsheet.md](cheatsheet.md) — 熔合势垒高度速查表、反冲运动学公式卡与常用靶-弹反应常数表。

---

## Scope & Limits

本技能提供重离子碰撞动力学、截面计算与实验束能靶厚设计的物理准则。对于反应出射后的退激 $\gamma$ 射线探测与 HPGe 电子学处理，配合 `nuclear-experimental-methods`；对于多极混合比 $\delta$ 统计双根裁决，配合 `zhu-experimental-statistics`；对于提取得到的能带三轴手征与摆动结构，配合 `chirality-and-wobbling-atomic-nuclei`。
