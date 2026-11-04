---
type: concept
title: "高纯锗（HPGe）数字化脉冲成形、极零相消（PZC）与弹道亏损动力学消除"
aliases: [HPGe脉冲成形, 极零相消, PZC, 弹道亏损, Ballistic Deficit, 梯形滤波, 前放指数衰减, 堆积判弃, 死时间模型]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [hpge-detectors, pulse-processing, pole-zero-cancellation, ballistic-deficit, trapezoidal-filter, dead-time, pileup-rejection, nuclear-instrumentation]
---

# 高纯锗（HPGe）数字化脉冲成形、极零相消（PZC）与弹道亏损动力学消除

## Definition

### 物理全景：高计数率束内核谱学中的能量分辨率瓶颈

在现代大型在束 $\gamma$ 探测阵列（如中国 CAGRA、欧洲 AGATA、美国 GRETA/Gammasphere）实验中，高纯锗（HPGe）探测器是无可替代的高分辨率探测中枢。
然而，当实验处于大束流强、高本底反应（总道计数率超过 $20 \sim 50\text{ kcps}$）时，HPGe 谱仪的能量分辨率（FWHM）往往发生显著劣化，特征谱线呈现出明显的低能侧不对称拖尾，甚至导致弱谱线被完全淹没。

根据吴治华《原子核物理实验方法》（第三版）、汪晓莲《粒子探测技术》、G. F. Knoll《Radiation Detection and Measurement》以及 V. T. Jordanov & G. F. Knoll（NIM A 345, 337, 1994）：
这一恶化主要由两大非理想模拟/数字电子学效应主导：
1. **前置放大器极点与长拖尾——极零相消（Pole-Zero Cancellation, PZC）失配**：
   电荷灵敏前置放大器（CSP）积分电荷后，通过反馈电阻 $R_f$ 缓慢放电，脉冲具有长达 $40 \sim 100\text{ }\mu\text{s}$ 的指数衰减拖尾。在数字化微分成形时，若极点未被精确抵消，将产生严重的基线负下冲（Undershoot）或正台阶，导致后续脉冲基线发生剧烈随机漂移；
2. **同轴锗晶体内电荷收集时间弥散——弹道亏损（Ballistic Deficit, BD）**：
   同轴 HPGe 晶体体积巨大（直径达 $7 \sim 9\text{ cm}$），光子发生光电效应或康普顿散射的径向深度不同。由于载流子迁移率有限，电子和空穴漂移至电极所需的**电荷收集时间 $t_c$ 具有剧烈涨落（$100 \sim 600\text{ ns}$）**。若数字成形平顶宽度不足，输出幅度将随反应位置随机缩水，形成灾难性的峰形展宽与下拖尾！

---

## Necessary Assumptions

### 严格物理与数字信号处理（DSP）数学表述

### (1) 电荷敏前置放大器输出响应
当单色光子在晶体内电离产生总电荷 $Q = E / w$（锗中平均电离能 $w = 2.96\text{ eV}$）时，前放电容 $C_f$ 上的电压输出为：
$$V_{\text{preamp}}(t) = V_0 \left[ 1 - \exp\left(-\frac{t}{t_{\text{rise}}}\right) \right] \exp\left(-\frac{t}{\tau_{\text{decay}}}\right)$$
其中：
- 阶跃上升时间 $t_{\text{rise}} \approx t_c$（电荷收集时间，通常 $100 \sim 600\text{ ns}$）；
- 指数衰减时间常数 $\tau_{\text{decay}} = R_f C_f$（典型值为 $50\text{ }\mu\text{s}$）；
- 阶跃幅值 $V_0 = Q / C_f$。

---

### (2) 频域极点分析与极零相消（PZC）算符
在拉普拉斯复频域，前放衰减信号的主导传递函数具有一个低频极点：
$$S_{\text{preamp}}(s) \propto \frac{1}{s + 1/\tau_{\text{decay}}}$$
为了消除信号直流分量并提取幅度，常规成形器包含一个微分环节（引入零点 $s = 0$）。
若直接微分，频域响应变为 $\frac{s}{s + 1/\tau_{\text{decay}}} = 1 - \frac{1/\tau_{\text{decay}}}{s + 1/\tau_{\text{decay}}}$。
在时域上，这将产生一个**幅度为 $-1/\tau_{\text{decay}}$、时间常数为 $\tau_{\text{decay}}$ 的巨大负指数下冲（Undershoot）**！在 $50\text{ kcps}$ 计数率下，下一个脉冲必将叠在尚未归零的下冲尾巴上，导致幅度测量严重偏低。

**极零相消网络（PZC Filter）**引入可调时间常数 $\tau_{\text{PZ}}$ 的零点来精确中和前放极点：
$$H_{\text{PZ}}(s) = \frac{s + 1/\tau_{\text{decay}}}{s + 1/\tau_{\text{PZ}}}$$
当硬件或数字化参数严格调节至：
$$\tau_{\text{PZ}} = \tau_{\text{decay}}$$
时，传递函数退化为 1，时域响应中的长衰减拖尾被**彻底瞬时截断**，脉冲瞬时恢复基线！

#### 数字离散化递归递推形式（Jordanov 算法）：
采样周期为 $T_s$（如 100 MHz 采集卡 $T_s = 10\text{ ns}$），离散化衰减补偿因子为 $M = \frac{1}{e^{T_s / \tau_{\text{decay}}} - 1} \approx \frac{\tau_{\text{decay}}}{T_s}$。
输入序列 $x[n]$ 经过 PZC 变换后得到纯阶跃序列 $p[n]$：
$$p[n] = x[n] + \frac{1}{M} \sum_{k=0}^n x[k]$$
- 若设置 $\tau_{\text{PZ}} < \tau_{\text{decay}}$（欠补偿）：时域出现持续负下冲；
- 若设置 $\tau_{\text{PZ}} > \tau_{\text{decay}}$（过补偿）：时域出现虚假正隆起。

---

### (3) 弹道亏损（Ballistic Deficit）的动力学起源与平顶覆盖律
弹道亏损定义为：由于探测器电荷收集过程具有有限时间 $t_c$，导致实际滤波输出的脉冲极大值 $V_{\text{max}}$ 相比于瞬时点电荷输入峰值 $V_{\text{ideal}}$ 的相对缺失量：
$$\text{BD} = \frac{V_{\text{ideal}} - V_{\text{max}}}{V_{\text{ideal}}}$$

在数字梯形滤波器（Trapezoidal Filter）中，参数由上升时间 $t_{\text{rise}}$（成形时间）与平顶时间 $t_{\text{flat}}$ 完全确定。
输出梯形幅度平顶区对应于对电流信号的积分。因此：
- **完全消除弹道亏损的充要条件**：
  $$t_{\text{flat}} \ge \max(t_c)$$
  当滤波平顶宽度 $t_{\text{flat}}$ 大于晶体内载流子的最长可能收集时间（同轴大 Ge 约为 $500\text{ ns}$）时，所有感应电荷在平顶结束前已完全收集完毕，**弹道亏损严格为零**（$\text{BD} \equiv 0$）！
- **平顶不足时的弹道亏损解析展开（$t_{\text{flat}} < t_c$）**：
  若平顶不足以完全覆盖漂移时间，电流脉冲截断将引入二阶亏损：
  $$\text{BD} \approx \frac{1}{12} \left( \frac{t_c - t_{\text{flat}}}{t_{\text{rise}}} \right)^2$$
  由于不同反应事件在晶体内部的发生位置随机分布，$t_c$ 呈平滑统计分布，导致各事件的 $\text{BD}$ 发生涨落，引起光电全能峰的特征性展宽和低能侧拖尾。

---

### (4) 高计数率死时间模型与谱线堆积（Pile-up）
设探测器实际入射物理事件率为 $R$（cps），数字梯形脉冲的总时间宽度为：
$$\tau_{\text{pulse}} = 2 t_{\text{rise}} + t_{\text{flat}}$$
1. **非可瘫痪型死时间模型（Non-paralyzable Model）**：
   输出计数率 $R_{\text{out}} = \frac{R}{1 + R \tau_{\text{pulse}}}$，死时间比例为 $\frac{R \tau_{\text{pulse}}}{1 + R \tau_{\text{pulse}}}$；
2. **可瘫痪型死时间模型（Paralyzable Model）**：
   输出计数率 $R_{\text{out}} = R \exp(-R \tau_{\text{pulse}})$；
3. **峰形堆积几率（Peak Pile-up Probability）**：
   两脉冲在成形积分时间窗口内重叠导致能量失真的几率：
   $$P_{\text{pileup}} = 1 - \exp(-2 R t_{\text{rise}})$$
   该部分畸变事件必须被数字化堆积判弃电路（Pile-up Rejector, PUR）彻底标记丢弃。

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/hpge_pulse_processing_pole_zero_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `hpge` 命令。

### 运行示范（模拟大体积同轴 HPGe 高计数率工况）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py hpge \
  --tc-ns 500.0 --trise-ns 2000.0 --tflat-ns 400.0 \
  --tau-preamp 50.0 --tau-pz 45.0 --rate-cps 40000.0
```

### 计算输出核心物理特征：
1. **弹道亏损诊断**：载流子收集时间 $t_c = 500\text{ ns}$，而平顶仅设为 $t_{\text{flat}} = 400\text{ ns}$（不足 $100\text{ ns}$），计算得出弹道亏损为 $0.0208\%$，在 $^{60}\text{Co}$ $1332.5\text{ keV}$ 峰上造成高达 $0.278\text{ keV}$ 的反常下移与峰形展宽；若调节 $t_{\text{flat}} = 600\text{ ns} > 500\text{ ns}$，亏损立即归零；
2. **PZC 极零失配审计**：前放 $\tau = 50\text{ }\mu\text{s}$，而采集卡误设为 $45\text{ }\mu\text{s}$（$0.9$ 倍），判定为 `Under_Compensated`，基线存在 $10\%$ 的持续负下冲拖尾；
3. **高计数率死时间评价**：在 $40\text{ kcps}$ 强流下，脉冲总长 $4.4\text{ }\mu\text{s}$，非可瘫痪死时间达 $14.97\%$，脉冲堆积失真几率达到 $14.79\%$，为实验现场的成形时间压缩（如 $t_{\text{rise}}$ 调整至 $1.2\text{ }\mu\text{s}$）提供了精确量化依据！

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用

- [[digital-pulse-processing-algorithms-nuclear-detectors]]：经典的梯形滤波在本文中得到了基于载流子漂移时间与极零相消的完备硬件物理支撑；
- [[poisson-maximum-likelihood-and-gamma-peak-fitting-bias]]：未校准弹道亏损与 PZC 产生的低能拖尾，正是高斯峰拟合中需要引入 Erfc 阶跃拖尾函数的直接物理根源；
- [[heavy-ion-fusion-evaporation-and-statistical-decay]]：在束实验流强上限往往受限于 HPGe 探测器的这套死时间与堆积边界。
