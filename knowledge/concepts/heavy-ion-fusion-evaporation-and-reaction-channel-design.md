# 重离子熔合蒸发反应截面、光学势垒分布与在束 $\gamma$ 谱学出射道设计：林承键《重离子核反应》与 Bertulani 理论融会

## 1. 物理机制与实验设计导论

在开展高自旋核结构前沿研究（如三轴形变手征双重带、摆动运动、多准粒子高 $K$ 异能态）时，实验方案设计的核心在于：**如何选择最优入射弹靶组合、轰击能量与靶厚度，以最大截面布居目标核的高自旋态，同时将裂变竞争、带电粒子蒸发道与运动学多普勒展宽压制到最低**。

林承键《重离子核反应》（第 2、6、7 章）、Bertulani & Danielewicz《Introduction to Nuclear Reactions》（第 11 章）以及卢希庭《原子核物理（修订版）》（第 9 章）为我们提供了完整的动力学与统计衰变理论基础：
- 库仑势垒穿透与耦合道效应（Coupled-Channels Barrier Distribution）；
- 入射角动量耗散与转动液滴裂变截断（Fission Competition at High Spin）；
- 复合核统计蒸发去激（Statistical Cascade Evaporation）；
- 在束反冲运动学与高纯锗阵列多普勒展宽控制。

---

## 2. 反应入口道动力学与 Wong 势垒穿透公式

### 2.1 质心系能量与 Bass / Christensen-Winther 相互作用势
在实验室坐标系下，具有动能 $E_{\text{lab}}$、质量数 $A_p$、电荷数 $Z_p$ 的重离子轰击静止靶核（$A_t, Z_t$）：
$$E_{\text{c.m.}} = E_{\text{lab}} \frac{A_t}{A_p + A_t}, \quad \mu = m_u \frac{A_p A_t}{A_p + A_t}$$
核相互作用势由库仑势 $V_C(r)$、离心势 $V_\ell(r)$ 及短程强相互作用核吸附势 $V_N(r)$ 叠加构成：
$$V(r, \ell) = \frac{Z_p Z_t e^2}{r} + V_N(r) + \frac{\hbar^2 \ell(\ell+1)}{2\mu r^2}$$
在经典接触半径 $R_B \approx 1.07 (A_p^{1/3} + A_t^{1/3}) + 2.72\text{ fm}$ 处形成主库仑势垒，势垒高度参数化为（Christensen-Winther 标度）：
$$V_B \approx \frac{1.44 Z_p Z_t}{R_B} \left( 1 - \frac{0.63}{R_B} \right) \text{ MeV}$$

### 2.2 Wong 势垒穿透解析截面
假定势垒在峰顶附近可用反转抛物线近似（势垒曲率能量 $\hbar\omega_B \sim 3.5 - 4.5\text{ MeV}$），全部分波 $\ell$ 的穿透几率求和收缩为著名的 **Wong 公式**：
$$\sigma_{\text{fus}}(E_{\text{c.m.}}) = \frac{\hbar\omega_B R_B^2}{2 E_{\text{c.m.}}} \ln \left[ 1 + \exp\left( \frac{2\pi (E_{\text{c.m.}} - V_B)}{\hbar\omega_B} \right) \right]$$
- 当 $E_{\text{c.m.}} \gg V_B$ 时，对数项渐近展开为经典几何截面：
  $$\sigma_{\text{fus}} \approx \pi R_B^2 \left( 1 - \frac{V_B}{E_{\text{c.m.}}} \right)$$
- 当 $E_{\text{c.m.}} < V_B$ 时，截面指数衰减：$\sigma_{\text{fus}} \propto \exp\left[\frac{2\pi(E_{\text{c.m.}}-V_B)}{\hbar\omega_B}\right]$。

---

## 3. 入射角动量输入与转动液滴裂变截断

重离子反应具有巨大的轨道角动量输入，最大入射角动量为：
$$L_{\max} = \frac{R_B}{\hbar} \sqrt{2\mu (E_{\text{c.m.}} - V_B)}$$
根据 Cohen-Plasil-Swiatecki 转动液滴模型（Rotating Liquid Drop Model, RLDM），复合核的有效裂变势垒随自旋急剧压低：
$$B_f(J) = B_f(0) - \frac{\hbar^2 J(J+1)}{2 \mathcal{J}_{\text{eff}}}$$
在质量区 $A \sim 130$（如 $^{136}\text{Ce}^*$ 或 $^{136}\text{Nd}^*$），基态裂变势垒 $B_f(0) \approx 25-30\text{ MeV}$。当自旋 $J$ 超过临界自旋 $J_{\text{fiss}} \approx 50-55\hbar$ 时，$B_f(J) \to 0$，复合核发生 $100\%$ 的瞬发裂变，无法产生蒸发余核。
因此，真实存活转化为在束能级带的有效剩余蒸发截面受限于：
$$\sigma_{\text{evap}} \approx \sigma_{\text{fus}} \cdot f_{\text{surv}}(L_{\max})$$
其中 $f_{\text{surv}} \approx \max\left[0.05, 1 - (L_{\max} / 70.0)^2\right]$。

---

## 4. 统计蒸发去激（$xn$ 出射道）能量匹配准则

复合核激发能由质心系能量与熔合反应 $Q$ 值决定：
$$E^* = E_{\text{c.m.}} + Q_{\text{fus}}, \quad Q_{\text{fus}} = M_p + M_t - M_{\text{CN}}$$
复合核核温度定义为：
$$T = \sqrt{\frac{E^*}{a}}, \quad a \approx \frac{A_{\text{CN}}}{8.5}\text{ MeV}^{-1}$$
每蒸发一个中子带走的平均能量由中子分离能 $S_n$（通常为 $8.0\text{ MeV}$）与麦克斯韦能谱平均动能 $\langle \epsilon_n \rangle = 2T$（通常为 $2.5-3.5\text{ MeV}$）构成：
$$\Delta E_n = S_n + 2T \approx 10.5 \sim 12.0\text{ MeV}$$
为使第 $x$ 个中子蒸发后余核恰好落入高自旋 yrast 线（约高于基态 $5\text{ MeV}$）并激发在束手征/摆动能带，最优复合核激发能呈现严格的高斯窗口匹配：
$$E^*_{\text{opt}}(xn) \approx x \cdot \Delta E_n + E_{\text{yrast}}(J_{\text{entry}})$$
例如：
- $4n$ 蒸发道最佳 $E^* \approx 52 - 58\text{ MeV}$；
- $5n$ 蒸发道最佳 $E^* \approx 64 - 72\text{ MeV}$；
- $6n$ 蒸发道最佳 $E^* \approx 76 - 84\text{ MeV}$。

---

## 5. 在束反冲运动学与 HPGe 多普勒展宽控制

在薄靶反应中，复合核沿束流方向以初速度反冲：
$$\beta = \frac{v_{\text{recoil}}}{c} = \sqrt{\frac{2 E_{\text{lab}}}{931.5 A_p}} \left( \frac{A_p}{A_{\text{CN}}} \right)$$
在典型的 $A \sim 130$ 实验中（如 $^{36}\text{S} + {}^{100}\text{Mo} \to {}^{136}\text{Ce}^*$ 在 $E_{\text{lab}} = 155\text{ MeV}$ 下），$\beta \approx 0.0255$（反冲速度高达光速的 $2.55\%$！）。

### 5.1 探测器几何多普勒效应
位于实验室极角 $\theta$ 处的探测器记录到的 $\gamma$ 光子能量发生多普勒频移：
$$E_\gamma(\theta) = E_{\gamma 0} \frac{\sqrt{1 - \beta^2}}{1 - \beta \cos\theta} \approx E_{\gamma 0} (1 + \beta \cos\theta)$$
探测器探头有限开口半角 $\Delta\theta$（典型值为 $8^\circ \approx 0.14\text{ rad}$）引起的运动学展宽在 $\theta = 90^\circ$ 处达到最大极值：
$$\Delta E_{\text{Doppler}}^{\text{FWHM}} = E_{\gamma 0} \cdot \beta \sin\theta \cdot \Delta\theta$$
对于 $E_{\gamma 0} = 1000\text{ keV}$ 跃迁，在 $90^\circ$ 处的纯运动学展宽高达 **$3.55\text{ keV}$**，远超 HPGe 探测器本征分辨（$\sim 1.9\text{ keV}$）！

### 5.2 靶材厚度设计准则
- **薄自支撑金属箔（Thin Self-Supporting Foil，$\sim 0.5\text{ mg/cm}^2$）**：反冲核飞出靶后在真空靶室中飞行衰变，各角度探测器测量能量服从严格的宏观 $\cos\theta$ 频移，经事件级软件角多普勒校正后即可完全恢复 $\sim 2.0\text{ keV}$ 的尖锐谱线，专用于手征/摆动能带的高分辨在束能级构建；
- **带衬底厚靶（Backed Target，如 Au/Pb 衬底，$\ge 10\text{ mg/cm}^2$）**：反冲核在衬底材料中迅速减速并停滞（阻止时间 $\alpha \approx 1-2\text{ ps}$），产生特征多普勒连续线形，专用于多普勒频移衰减法（DSAM）测定高自旋能级皮秒级寿命。

---

## 6. 科学分析套件实战验证

Wiki 内置模块 `system/scripts/analysis/heavy_ion_fusion_evaporation_channel_calculator.py`（CLI 命令：`python3 system/scripts/analysis/nuclear_analyzer.py fusion`）直接模拟设计了 $A \sim 130$ 手征候选核 $^{130,131}\text{Ce}$ 的轰击方案：

```bash
# 模拟 36S (155 MeV) 轰击 100Mo 靶反应出射道截面与多普勒效应
python3 system/scripts/analysis/nuclear_analyzer.py fusion --Zp 16 --Ap 36 --Zt 42 --At 100 --Elab 155.0 --target-thick 0.5
```

**实测输出解析**：
- 质心能量 $E_{\text{c.m.}} = 113.97\text{ MeV}$，高出库仑势垒 $V_B = 81.40\text{ MeV}$ 达 $32.57\text{ MeV}$；
- 复合核 $^{136}\text{Ce}^*$ 激发能 $E^* = 74.45\text{ MeV}$，入射角动量高达 $72.1\hbar$（受裂变截断截断于 $52\hbar$）；
- 出射道统计分配：$6n$ 蒸发道（产物 $^{130}\text{Ce}$）截面为 $36.2\text{ mb}$（占 $64.1\%$），$5n$ 蒸发道（产物 $^{131}\text{Ce}$）截面为 $20.1\text{ mb}$（占 $35.6\%$）；
- 反冲速度 $\beta = 2.55\%$，若在 $90^\circ$ 放置 HPGe 阵列，几何展宽为 $3.55\text{ keV}$，指导实验必须采用厚度小于 $0.5\text{ mg/cm}^2$ 的自支撑薄靶以确保多普勒角重构精度。
