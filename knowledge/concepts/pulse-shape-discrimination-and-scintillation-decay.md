---
type: concept
title: "闪烁体脉冲形状鉴别（PSD）、双成分荧光衰变动力学与优值因子（FOM）"
aliases: [脉冲形状鉴别, PSD, 闪烁体发光机制, 双门积分电荷比较法, CCM, 过零时间法, ZCM, 优值因子, FOM, 快中子与伽马分离]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [pulse-shape-discrimination, psd, scintillation-decay, charge-comparison-method, zero-crossing, figure-of-merit, fom, neutron-gamma-separation, nuclear-instrumentation]
---

# 闪烁体脉冲形状鉴别（PSD）、双成分荧光衰变动力学与优值因子（FOM）

## Definition

### 物理全景：混合辐射场中快中子与γ射线的超纯分离

在实验核物理、重离子熔合蒸发反应与核安全监测中，实验大厅与靶室环境总是充斥着高通量的混合辐射（强 $\gamma$ 射线背景与快中子伴随产生）。
对于液闪探测器（如 BC501A, NE213, EJ-301）、有机晶体（如对联苯、二苯乙烯 Stilbene）以及某些无机晶体（如 $\text{CsI}(\text{Tl})$）：
**脉冲形状鉴别（Pulse Shape Discrimination, PSD）技术是利用探测器单一晶体物理输出区分入射粒子种类的终极王牌！**

根据吴治华《原子核物理实验方法》（第三版）、汪晓莲《粒子探测技术》、G. F. Knoll《Radiation Detection and Measurement》以及 R. A. Winyard（NIM 95, 141, 1971）：
1. **分子激发态与双成分发光动力学**：
   有机闪烁分子受到入射带电粒子电离激发时，产生大量的激发单重态（Singlet, $S_1$）与激发三重态（Triplet, $T_1$）。由于自旋禁戒，单重态迅速退激产生**快发光成分（Prompt fluorescence, $\tau_{\text{fast}} \approx 2 \sim 30\text{ ns}$）**；而三重态是长寿命亚稳态，只能通过双分子碰撞（Triplet-Triplet Annihilation）延迟形成激发单重态，产生**慢发光成分（Delayed fluorescence, $\tau_{\text{slow}} \approx 200 \sim 1000\text{ ns}$）**；
2. **电离密度（$dE/dx$）对慢成分比例的绝对支配**：
   - 低电离密度粒子（如 $\gamma$ 射线引起的康普顿散射电子）：$dE/dx$ 极小，电离轨迹极其弥散，分子间距大，三重态双分子碰撞几率微弱，几乎只有快荧光（慢成分占比仅 $\sim 10\%$）；
   - 高电离密度粒子（如快中子弹性散射产生的反冲质子，或 $\alpha$ 粒子）：$dE/dx$ 极大，在核心形成高密度等离子体激发柱，两两碰撞几率暴增数倍，诱发强烈的延迟慢荧光（慢成分占比达 $25\% \sim 35\%$）；
3. **数字化双门电荷比较法（CCM）与优值因子（Figure of Merit, FOM）**：
   通过数字化高采样率采集卡在时域上建立全积分门 $Q_{\text{total}}$ 与尾部门 $Q_{\text{tail}}$，能够以无模型方式提取 PSD 比值。优值因子 $\text{FOM} \ge 1.27$ 构成了现代核物理中宣布中子与 $\gamma$ 实现 $3\sigma$ 完全物理分离的标准门槛。

---

## Necessary Assumptions

### 严格时域物理推导与鉴别算法

### (1) 闪烁发光时间电流谱方程
光电倍增管（PMT）阳极输出的感应电流脉冲时域波形表述为快慢双指数叠加模型：
$$I(t) = I_0 \left[ (1 - f_{\text{slow}}) \frac{1}{\tau_{\text{fast}}} \exp\left(-\frac{t}{\tau_{\text{fast}}}\right) + f_{\text{slow}} \frac{1}{\tau_{\text{slow}}} \exp\left(-\frac{t}{\tau_{\text{slow}}}\right) \right]$$
典型有机液体闪烁体参数：
- 快成分寿命：$\tau_{\text{fast}} \approx 3.2\text{ ns}$；
- 慢成分寿命：$\tau_{\text{slow}} \approx 270\text{ ns}$；
- 慢成分积分权重比：$\gamma$ 射线下 $f_{\text{slow}} \approx 0.12$，中子反冲质子下 $f_{\text{slow}} \approx 0.28$。

---

### (2) 数字化双门电荷比较法（Charge Comparison Method, CCM）
在数字化数据采集系统中，设定触发时刻为 $t=0$：
- **总积分门（Total Gate, $0 \to t_{\text{long}}$，典型 $300 \sim 500\text{ ns}$）**：
  $$Q_{\text{total}} = \int_0^{t_{\text{long}}} I(t) dt = I_0 \left[ (1 - f_{\text{slow}}) (1 - e^{-t_{\text{long}}/\tau_{\text{fast}}}) + f_{\text{slow}} (1 - e^{-t_{\text{long}}/\tau_{\text{slow}}}) \right]$$
- **尾部延迟门（Tail Gate, $t_{\text{tail}} \to t_{\text{long}}$，典型起始于峰值后 $30 \sim 40\text{ ns}$）**：
  此时快成分（$e^{-t/\tau_{\text{fast}}}$）已完全衰减归零（$< 10^{-4}$），积分几乎全由慢成分贡献：
  $$Q_{\text{tail}} = \int_{t_{\text{tail}}}^{t_{\text{long}}} I(t) dt \approx I_0 f_{\text{slow}} \left( e^{-t_{\text{tail}}/\tau_{\text{slow}}} - e^{-t_{\text{long}}/\tau_{\text{slow}}} \right)$$
- **无量纲 PSD 鉴别参量**：
  $$\text{PSD} = \frac{Q_{\text{tail}}}{Q_{\text{total}}}$$
由于 $f_{\text{slow}}(\text{neutron}) > 2 \times f_{\text{slow}}(\gamma)$，在二维关联谱 $(Q_{\text{total}}, \text{PSD})$ 上，中子事件形成明显高于 $\gamma$ 事件的上方独立平滑分支带。

---

### (3) 模拟双极过零时间法（Zero-Crossing Method, ZCM）
在模拟电子学模块中，阳极电流通过微分-双积分网络（CR-(RC)$^2$）成形为双极性脉冲（Bipolar Pulse）。
输出脉冲穿过零基线的时间 $t_{\text{zc}}$ 严格依赖于输入脉冲的拖尾等效衰减时间：
$$t_{\text{zc}} \approx 2 \tau_{\text{shaping}} + C \cdot (f_{\text{slow}} \tau_{\text{slow}})$$
由于慢成分更强，中子脉冲的过零时间滞后于 $\gamma$ 脉冲达 $15 \sim 35\text{ ns}$，通过恒比定时（CFD）与时间-幅度转换器（TAC）即可完成甄别。

---

### (4) 优值因子（Figure of Merit, FOM）统计判定法典
在特定能量区间截取的 1D PSD 直方图呈现两个独立的高斯峰：
- $\gamma$ 峰中心为 $\mu_\gamma$，标准差为 $\sigma_\gamma$（半高宽 $\text{FWHM}_\gamma = 2.355 \sigma_\gamma$）；
- 中子峰中心为 $\mu_n$，标准差为 $\sigma_n$（半高宽 $\text{FWHM}_n = 2.355 \sigma_n$）。

标准 **优值因子（Figure of Merit, FOM）** 定义为：
$$\text{FOM} = \frac{S}{\text{FWHM}_\gamma + \text{FWHM}_n} = \frac{|\mu_n - \mu_\gamma|}{2.355 (\sigma_\gamma + \sigma_n)}$$

| FOM 数值区间 | 分离纯度评定 | 物理假鉴别率与实验适用性 |
| :--- | :--- | :--- |
| **$\text{FOM} < 1.0$** | **不合格（Poor Separation）** | 两峰严重交叉重叠，假中子污染率 $> 5\%$，不可用于弱通道物理实验 |
| **$1.0 \le \text{FOM} < 1.27$** | **临界合格（Acceptable）** | 低能端部分重叠，需要设置极高的甄别阈以抑制泄漏 |
| **$1.27 \le \text{FOM} < 1.5$** | **标准 $3\sigma$ 完全分离（Clean $3\sigma$）** | 经典核谱学黄金标准；假信号污染率 $< 0.13\%$，适用于在束中子墙符合实验 |
| **$\text{FOM} \ge 1.5$** | **卓越分离（Pristine Discrimination）** | 完全隔绝，即便在极高 $\gamma$ 泛滥本底下仍能实现单中子精密标记 |

**能量标度律**：由于光电子发射服从泊松统计，峰宽与光电子数的平方根成反比，因此 FOM 随发光能量开方放大：
$$\text{FOM}(E) \approx \text{FOM}_0 \sqrt{E_{\text{MeVee}}}$$
这解释了为何 PSD 鉴别在极低能端（$< 100\text{ keVee}$）必然发生恶化与融合。

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/pulse_shape_discrimination_psd_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `psd` 命令。

### 运行示范（模拟典型 NE213 液闪在 $1.0\text{ MeVee}$ 电子等效能量下的响应）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py psd -E 1.0 --json
```

### 计算输出核心物理特征：
1. **双门电荷比值**：
   - 设定尾部门 $30 \sim 400\text{ ns}$，计算得出 $\gamma$ 脉冲 $\text{PSD}_\gamma = 0.0824$，快中子脉冲 $\text{PSD}_n = 0.1997$；
   - 质心中心距分离达到 $\Delta \text{PSD} = 0.1173$；
2. **双极过零延迟**：双极成形下，$\gamma$ 过零时间为 $84.86\text{ ns}$，中子为 $91.34\text{ ns}$，净时间延迟达 $6.48\text{ ns}$；
3. **优值因子判定**：在 $1.0\text{ MeVee}$ 下 $\text{FOM} = 1.038$；在 $1.5\text{ MeVee}$ 下升至 $\text{FOM} = 1.27$，达到在束中子打靶实验的标准 $3\sigma$ 清晰隔离门槛！

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用

- [[charged-particle-identification-and-stopping-power]]：$\Delta E - E$ 望远镜鉴别带电轻离子（$p, d, \alpha$）与本 PSD 模块鉴别中子/$\gamma$ 互为实验带电/中性粒子鉴别的完整闭环；
- [[heavy-ion-fusion-evaporation-and-statistical-decay]]：在束 $(HI, xn)$ 实验中，中子墙的 PSD 纯中子触发门是滤除数千倍巨偶极辐射 $\gamma$ 泛滥的生命线；
- [[digital-pulse-processing-algorithms-nuclear-detectors]]：数字化多通道采集卡对闪烁脉冲的高速数字化是双门电荷积分算法落地的硬件载体。
