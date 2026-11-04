---
type: concept
title: "重离子熔合蒸发反应动力学、统计衰变级联与在束γ谱学实验设计准则"
aliases: [重离子熔合蒸发反应, 熔合截面, Bass模型, 统计衰变级联, Hauser-Feshbach, 临界角动量, 旋转液滴模型, RLDM, 实验设计准则, 束流能量优化]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [heavy-ion-reactions, fusion-evaporation, statistical-decay, hauser-feshbach, bass-model, critical-angular-momentum, rldm, in-beam-spectroscopy, experimental-design]
---

# 重离子熔合蒸发反应动力学、统计衰变级联与在束γ谱学实验设计准则

## Definition

### 物理全景：从束流碰撞到高自旋核结构态的布居

在低能实验核物理中，为了产生高自旋激发态、研究三轴超形变、寻找手征双重带与摆动运动，**重离子熔合蒸发反应（Heavy-Ion Fusion-Evaporation Reaction）**是最有效、最主要的实验合成手段。
根据林承键《重离子核反应》、R. Bass《Nuclear Reactions with Heavy Ions》以及 W. Hauser & H. Feshbach（Phys. Rev. 87, 366, 1952）：
1. **熔合阶段（Fusion Stage）**：
   弹核 $(Z_p, A_p)$ 克服与靶核 $(Z_t, A_t)$ 之间的库仑位垒 $V_B$，两核强相互作用接触并融合成一个高度热化、高度激发、快速旋转的**复合核（Compound Nucleus, CN）**：
   $$E^* = E_{\text{c.m.}} + Q_{\text{fus}}$$
   反应带入巨大的轨道角动量（$l \sim 20 \sim 60\hbar$）；
2. **统计蒸发阶段（Statistical Evaporation Stage）**：
   受激发复合核处于强相互作用平衡，通过热力学平衡的粒子发射（中子 $n$、质子 $p$、$\alpha$ 粒子）迅速带走大量激发能。当激发能降至各粒子分离能阈值以下时，转入电磁跃迁级联（准连续区统计 $\gamma$ 谱 $\to$ 沿 Yrast 线的离散在束 $\gamma$ 谱带），最终衰变至基态或长寿命同质异能态；
3. **实验设计之核心权衡（The Experimental Trade-off）**：
   - 束流能量过低：库仑穿透几率骤降，总熔合截面极低，无法带入研究所需的高角动量；
   - 束流能量过高：复合核转动动能与激发能过高，导致离心力撕裂（裂变几率 $\Gamma_f$ 剧烈增大）或蒸发更多中子（跨越到 $5n, 6n$ 甚至带电蒸发通道，稀释目标产物截面）。

---

## Necessary Assumptions

### 严格物理公式与动力学机制

### (1) 质心系运动学与库仑/Bass 相互作用位垒
设实验室系束流能量为 $E_{\text{lab}}$：
- 质心系能量（Center-of-Mass Energy）：
  $$E_{\text{c.m.}} = E_{\text{lab}} \frac{A_t}{A_p + A_t}$$
- 约化质量（Reduced Mass）：
  $$\mu = m_u \frac{A_p A_t}{A_p + A_t}$$
- **Bass 邻近势相互作用位垒 $V_B$ 与接触半径 $R_B$**：
  $$R_i = 1.12 A_i^{1/3} - 0.94 A_i^{-1/3}\text{ [fm]}$$
  $$R_{12} = \frac{R_p R_t}{R_p + R_t}, \quad R_B = R_p + R_t + 2.7\text{ fm}$$
  $$V_B = \frac{1.44 Z_p Z_t}{R_B} - 0.03 R_{12}\text{ [MeV]}$$

---

### (2) 极限角动量与熔合截面 $\sigma_{\text{fus}}$
根据经典力学与量子位垒穿透，轨道角动量 $l$ 的最大穿透值由有效势极大值决定：
$$l_{\text{fus}}^2 = \frac{2\mu R_B^2}{\hbar^2} \max(E_{\text{c.m.}} - V_B, 0)$$
当复合核转动角动量超过某一阈值时，巨大的离心势能将彻底消除核液滴的裂变势垒。
根据 **Cohen-Plasil-Swiatecki 旋转液滴模型（Rotating Liquid Drop Model, RLDM）**：
核的可裂变度参数（Fissility Parameter）：
$$x = \frac{Z_{\text{CN}}^2}{50.88 A_{\text{CN}} [1 - 1.78 ((A_{\text{CN}} - 2Z_{\text{CN}})/A_{\text{CN}})^2]}$$
此时液滴失稳裂变极限角动量约为：
$$l_{\text{RLDM}} \approx 80 (1 - x)\hbar$$
实际能够存活形成蒸发残核的临界角动量为两者较小值：
$$l_{\text{crit}} = \min(l_{\text{fus}}, l_{\text{RLDM}})$$

总熔合截面由分波求和得出（夏普截止近似）：
$$\sigma_{\text{fus}}(E_{\text{c.m.}}) = \frac{\pi \hbar^2}{2\mu E_{\text{c.m.}}} l_{\text{crit}}^2$$

---

### (3) Weisskopf-Ewing / Hauser-Feshbach 统计衰变分宽度
在每个蒸发步长中，激发复合核通过各竞争通道衰变的分宽度由相空间能级密度主导：
1. **中子发射宽度 $\Gamma_n$**（不受库仑势垒阻碍，中重核中最优势通道）：
   $$\Gamma_n \propto (2s_n + 1) \frac{m_n R^2}{\pi \hbar^2} T_n^2 \frac{\rho_{\text{res}}(E^* - S_n)}{\rho_{\text{CN}}(E^*)}$$
2. **质子与 $\alpha$ 带电粒子发射宽度 $\Gamma_p, \Gamma_\alpha$**（受到穿透因子阻尼）：
   由于带电粒子需穿透残核库仑势垒 $V_C = \frac{1.44 z_p Z_{\text{res}}}{R_{\text{coul}}}$，有效激发能量被削减约 $0.7 V_C$：
   $$\Gamma_p \propto (2s_p + 1) \frac{m_p R^2}{\pi \hbar^2} T_p^2 \frac{\rho_{\text{res}}(E^* - S_p - 0.7 V_C)}{\rho_{\text{CN}}(E^*)}$$
3. **裂变宽度 $\Gamma_f$（Bohr-Wheeler 鞍点过渡态公式）**：
   $$\Gamma_f \propto \frac{T_f}{2\pi} \frac{\rho_{\text{saddle}}(E^* - B_f(l))}{\rho_{\text{CN}}(E^*)}$$
   其中旋转有效裂变势垒随自旋下降：$B_f(l) \approx B_f(0) - \frac{\hbar^2 l^2}{2\mathcal{J}_{\text{eff}}}$；
4. **辐射 $\gamma$ 宽度 $\Gamma_\gamma$**：
   通过巨偶极共振（GDR）发射统计 $E1$ 光子，典型宽度 $\Gamma_\gamma \sim 1 \sim 3\text{ eV}$。

---

### (4) 蒸发级联（Evaporation Cascade）与产物截面分布
多步蒸发级联通过主方程（Master Equation）逐步推演：
- 每一阶段发射粒子带走平均动能 $\langle \epsilon \rangle \approx 2 T = 2\sqrt{E^* / a}$，以及结合能 $S_i$；
- 统计分支比 $P_i = \Gamma_i / \Gamma_{\text{tot}}$ 决定了残留核通道走向；
- 各残核截面：
  $$\sigma(x n, y p, z \alpha) = \sigma_{\text{fus}} \times \prod_{\text{steps}} P_i$$

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 在束 $\gamma$ 谱学实验设计实战准则

在设计研究三轴形变核（例如 $^{130}\text{Ba}, ^{134}\text{Ce}$）的在束实验时，必须遵循以下黄金法则：

1. **弹核与靶核选择的同位旋与形变倾向**：
   - 尽量选择富中子或丰质子稳定同位素靶（如 $^{116}\text{Cd}, ^{120}\text{Sn}, ^{124}\text{Sn}$）；
   - 选用较重较紧凑的弹核（如 $^{16, 18}\text{O}, ^{13, 14}\text{C}, ^{30}\text{Si}$），既能提供足够的质心系动能，又避免由于深部非弹性散射过早截断熔合；
2. **最佳束流能量的峰值定位（Peak Energy Tuning）**：
   - 复合核中，每发射一个中子大约带走 $S_n + 2T \approx 8 + 3 = 11\text{ MeV}$ 的激发能；
   - 若目标产物为 $4n$ 出射道（如 $^{116}\text{Cd}(^{18}\text{O}, 4n)^{130}\text{Ba}$），理想激发能应为：
     $$E^* \approx 4 \times 11 + 5 = 49\text{ MeV}$$
   - 反推所需束流能量 $E_{\text{lab}} \approx 65 \sim 70\text{ MeV}$；若能量升至 $75\text{ MeV}$（$E^* \approx 59\text{ MeV}$），则主反应通道将完全切换为 $5n$ 通道（生成 $^{129}\text{Ba}$）！
3. **靶衬底（Backing）选择策略**：
   - **自支撑薄靶（Self-supporting, $\sim 0.5 \sim 1.0\text{ mg/cm}^2$）**：反冲核飞入真空中，配合柱塞反冲距离法（RDM）测量皮秒量级（$\sim 1 \sim 100\text{ ps}$）寿命；
   - **厚衬底靶（Backed target, e.g. Au/Pb, $\sim 10 \sim 20\text{ mg/cm}^2$）**：反冲核在衬底介质中迅速慢化（$\tau_{\text{stop}} \sim 1\text{ ps}$），配合多普勒频移衰减法（DSAM）测量飞秒量级（$\sim 50 \sim 1000\text{ fs}$）内带寿命，此时要求靶衬底对束流无强烈的非弹性库仑激发背景。

---

## 4. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/compound_nucleus_evaporation_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `evap` 命令。

### 运行示范（以 $^{18}\text{O} + ^{116}\text{Cd}$ 反应为例）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py evap -Zp 8 -Ap 18 -Zt 48 -At 116 -E 75.0 --json
```

### 计算输出核心物理特征：
1. **熔合运动学**：$E_{\text{lab}} = 75.0\text{ MeV}$ 时，$E_{\text{c.m.}} = 64.93\text{ MeV}$，克服 Bass 位垒 $V_B = 52.38\text{ MeV}$；
2. **复合核参数**：生成 $^{134}\text{Ba}^*$，激发能量 $E^* = 59.05\text{ MeV}$，临界角动量达到 $l_{\text{crit}} = 32.3\hbar$；
3. **总截面与出射道分布**：总熔合截面 $\sigma_{\text{fus}} = 675.7\text{ mb}$。在 $59\text{ MeV}$ 激发能下，级联主导通道为 $5n$ 蒸发（分支比 $97.7\%$, 截面 $660.5\text{ mb}$），轻质子蒸发通道 $p4n$ 占 $1.5\%$（$9.9\text{ mb}$），定量指导了实验束流能量的微调方向！

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用

- [[gilbert-cameron-composite-level-density-and-shell-damping]]：蒸发残核能级密度的精确描述是截面预测精度的基石；
- [[heavy-ion-fusion-evaporation-and-statistical-decay]]：熔合蒸发残核的质心系反冲速度 $\beta = v/c$ 决定了在束 $\gamma$ 探测的多普勒展宽校正；
- [[fission-barriers-strutinsky-and-superheavy-dynamics]]：超重核合成中的极端竞争（极低存活几率），本质是蒸发级联中 $\Gamma_n / \Gamma_f \ll 10^{-2}$ 的极端情形。
