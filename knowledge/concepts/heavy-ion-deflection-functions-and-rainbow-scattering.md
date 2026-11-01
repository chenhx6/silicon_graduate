---
type: concept
title: "重离子半经典偏转函数、核彩虹散射动力学与掠射角探测器布局准则"
aliases: [偏转函数, 核彩虹散射, 掠射角, Blair四分之一法则, 强吸收半径, 库仑核势平衡, 探测器布局准则, 转移反应截面]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [heavy-ion-scattering, deflection-function, nuclear-rainbow, grazing-angle, blair-quarter-point, rainbow-angle, airy-oscillations, experimental-methods]
---

# 重离子半经典偏转函数、核彩虹散射动力学与掠射角探测器布局准则

## 1. 物理全景：重离子散射从宏观轨道到量子衍射的半经典统一

在重离子物理与在束带电粒子核反应实验中，由于重核质量巨大且电荷极高，体系的 Sommerfeld 参数往往极大（$\eta = Z_p Z_t e^2 / (\hbar v) \gg 1$），德布罗意波长 $\lambda = 1/k \ll 1\text{ fm}$ 远小于核几何尺度。
这使得重离子的弹性散射、准弹性转移与深部非弹性碰撞在很大程度上服从经典力学轨迹方程，可用**半经典偏转函数（Semiclassical Deflection Function, $\Theta(l)$）**精确描述。

根据 C. A. Bertulani & P. Danielewicz《Introduction to Nuclear Reactions》、林承键《重离子核反应》以及 D. A. Goldberg & S. M. Smith（Phys. Rev. Lett. 29, 500, 1972）：
重离子偏转函数描绘了**排斥性长程库仑势与吸引性短程核表面势**在不同轨道角动量 $l$（或碰撞参数 $b = l/k$）下的剧烈力学竞争：
1. **大角动量远距离轨道（$l \gg l_{\text{grazing}}$）**：两核相距遥远，核力不可及，粒子受纯库仑斥力主导，发生正散射角偏转（纯 Rutherford 散射）；
2. **掠射碰撞轨道（$l \approx l_{\text{grazing}}$）**：两核表面发生掠射接触，强吸收导致弹性散射截面急剧跌落。著名的 **Blair 四分之一法则（Quarter-point Angle, $\theta_{1/4}$）** 定义了截面比跌落至 $0.25$ 的宏观临界散射角；
3. **近距吸引轨道与核彩虹（Nuclear Rainbow, $\theta_{\text{rainbow}}$）**：当角动量进一步降低，强大的核引力弯曲弹核轨迹，使偏转角 $\Theta(l)$ 向前乃至负角弯折，在极值点处导数归零：
   $$\left. \frac{d\Theta(l)}{dl} \right|_{l = l_{\text{rainbow}}} = 0$$
   经典微分截面 $d\sigma/d\Omega \propto 1 / |d\Theta/dl|$ 在此处发散，产生壮丽的**核彩虹现象（Nuclear Rainbow）**，并在量子力学中表现为周期性的艾里函数（Airy Oscillations）震荡！

---

## 2. 严格半经典偏转方程与彩虹特征

### (1) 经典偏转积分方程
设质心系有效径向相互作用势为 $V_{\text{eff}}(r) = V_C(r) + V_N(r) + \frac{\hbar^2 l(l+1)}{2\mu r^2}$。
经典偏转角 $\Theta(l)$ 定义为粒子从无穷远入射到经典回折点 $r_{\text{turn}}$ 再出射至无限远的总散射角：
$$\Theta(l) = \pi - 2 \int_{r_{\text{turn}}}^\infty \frac{l \hbar / r^2}{\sqrt{2\mu [E_{\text{c.m.}} - V_{\text{eff}}(r)]}} dr$$
解析近似形式为库仑项与核力梯度的代数差：
$$\Theta(l) = 2 \arctan\left(\frac{\eta}{l}\right) - \Theta_{\text{nuclear}}(l)$$
其中 Sommerfeld 库仑参数：
$$\eta = \frac{Z_p Z_t e^2}{\hbar v} = \frac{Z_p Z_t \cdot 1.44\text{ MeV}\cdot\text{fm}}{\hbar c \cdot \beta}$$

---

### (2) 掠射角动量 $l_{\text{grazing}}$ 与 Blair 四分之一角 $\theta_{1/4}$
两核相互作用距离定义为强吸收半径：
$$R_{\text{int}} = r_0 (A_p^{1/3} + A_t^{1/3})\text{ fm} \quad (r_0 \approx 1.25\text{ fm})$$
接触处库仑势垒高度为 $V_C(R_{\text{int}}) = \frac{1.44 Z_p Z_t}{R_{\text{int}}}\text{ MeV}$。

掠射轨道角动量（低于此值的粒子将发生强接触吸收）：
$$l_{\text{grazing}} = k R_{\text{int}} \sqrt{\max\left(1 - \frac{V_C(R_{\text{int}})}{E_{\text{c.m.}}}, 0\right)}$$
其中渐近波数 $k = \frac{\sqrt{2\mu E_{\text{c.m.}}}}{\hbar}$。

**Blair 四分之一法则（The Blair Quarter-Point Recipe）**：
在重离子弹性散射角分布中，比值 $\sigma(\theta) / \sigma_{\text{Ruth}}(\theta) = 0.25$ 的角度 $\theta_{1/4}$ 与掠射角动量具有精确的对应关系：
$$\theta_{1/4} = 2 \arcsin\left( \frac{\eta}{\sqrt{\eta^2 + l_{\text{grazing}}^2}} \right)$$

---

### (3) 核彩虹散射极值与艾里震荡
随着 $l$ 逐渐降至核表面内部，偏转角由于核力强吸引而急剧下降，到达极小值：
$$\theta_{\text{rainbow}} = \min_{l} [ \Theta(l) ]$$
- **明区（Bright Side, $\theta > \theta_{\text{rainbow}}$）**：存在两条不同碰撞参数的轨迹对应同一个散射角度，两经典路径发生相干干涉，产生强烈的宏观量子**艾里多重峰（Airy Peaks）**；
- **暗区（Shadow / Dark Side, $\theta < \theta_{\text{rainbow}}$）**：属于经典禁戒区，截面呈纯指数快速隧穿衰减。

---

## 3. 在束实验探测器布局实战黄金法则

在策划重离子转移反应、库仑激发或在束带电粒子测量时，实验大厅的探测器布局必须严格服从以下法则：

1. **带电粒子望远镜的“掠射角锁定”（Grazing Angle Gating）**：
   - 准弹性核子转移反应（如单中子、单质子、两核子转移）以及深部非弹性散射（DIC）的反应几率**在掠射角 $\theta \approx \theta_{1/4}$ 处达到全局极大值**！
   - 若将探测器放得过于靠前（$\theta \ll \theta_{1/4}$），将遭遇巨大的纯 Rutherford 弹性散射计数洪流，导致探测器瘫痪或前放饱和；
   - 若放得过于靠后（$\theta \gg \theta_{1/4}$），强吸收使得直接反应产额急剧衰竭；
   - **黄金法则**：将 $\Delta E - E$ 望远镜中心轴精准校准在 $\theta_{\text{lab}} \approx \theta_{1/4}$ 处，既能最大化获取转移物理事件，又能维持可控的探测器计数率！
2. **核彩虹角度作为内禀核势检验窗**：
   彩虹角 $\theta_{\text{rainbow}}$ 的测量值对核光学势的实部深度极其敏感，是唯一能够打破光学模型“强吸收离散势模糊性（Discrete Ambiguities）”的决定性判据。

---

## 4. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/heavy_ion_elastic_rainbow_scattering_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `rainbow` 命令。

### 运行示范（模拟经典重离子散射 $^{16}\text{O} + {}^{208}\text{Pb}$ 在 $E_{\text{lab}} = 100\text{ MeV}$ 下的散射动力学）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py rainbow \
  -Zp 8 -Ap 16 -Zt 82 -At 208 -E 100.0 --json
```

### 计算输出核心物理特征：
1. **质心系运动学与接触几何**：
   - 质心能量 $E_{\text{c.m.}} = 92.86\text{ MeV}$，Sommerfeld 库仑参数高达 $\eta = 41.32$（强库仑半经典区）；
   - 强吸收半径 $R_{\text{int}} = 10.56\text{ fm}$，接触库仑位垒 $V_C = 89.49\text{ MeV}$；
   - 算得掠射角动量 $l_{\text{grazing}} = 16.3\hbar$；
2. **Blair 四分之一法则与彩虹角**：
   - 算出 Blair 四分之一散射角为 $\theta_{1/4} = 136.8^\circ$（指导实验望远镜部署方位）；
   - 偏转函数极值搜索得出核彩虹出现在 $l_r = 17.3\hbar$ 处，核彩虹角达到：
     $$\theta_{\text{rainbow}} = 98.7^\circ$$
   - 确认彩虹效应处于活跃状态（`is_rainbow_active: True`），展现出清晰的半经典偏转弯折图像！

---

## 5. 与相关前沿概念的交叉引用
- [[linear-momentum-transfer-and-incomplete-fusion]]：掠射角附近的擦边碰撞是不完全熔合（ICF）和破裂反应（Breakup）的主产区；
- [[multi-nucleon-transfer-and-deep-inelastic-collisions]]：多核子转移反应截面的角分布峰位严格定域在 Blair 掠射角 $\theta_{1/4}$ 处；
- [[charged-particle-identification-and-stopping-power]]：在掠射角处测量的反应产物依赖 $\Delta E - E$ 望远镜进行单同位素鉴别。
