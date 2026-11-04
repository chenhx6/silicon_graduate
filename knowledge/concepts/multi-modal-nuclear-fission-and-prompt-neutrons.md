---
type: concept
title: "多模式核裂变碎片质量产额分布、Viola总动能（TKE）系统学与瞬发中子锯齿谱动力学"
aliases: [多模式核裂变, 碎片质量分布, Brosa模型, Viola系统学, TKE, 瞬发中子锯齿谱, 断点颈缩, 132Sn球形壳, 非对称裂变]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [nuclear-fission, fission-fragment-mass-yield, brosa-model, viola-systematics, prompt-neutrons, sawtooth-multiplicity, 132sn-shell, tke]
---

# 多模式核裂变碎片质量产额分布、Viola总动能（TKE）系统学与瞬发中子锯齿谱动力学

## Definition

### 物理全景：从液滴模型对称裂变到壳效应主导的非对称断颈

在低能核裂变（如 $^{235}\text{U}(n_{\text{th}}, f), ^{239}\text{Pu}(n_{\text{th}}, f), ^{252}\text{Cf}(\text{sf})$）实验中，一个最引人入胜的物理现象是：
**经典液滴模型预言原子核应沿中间对称裂开（质量相等的两块碎片），但实验测得的重核裂变产额却压倒性地表现为强烈的非对称双峰分布！**

根据 U. Brosa 等（Phys. Rep. 197, 167, 1990）、V. E. Viola（Phys. Rev. C 31, 1550, 1985）与 R. Vandenbosch & J. R. Huizenga《Nuclear Fission》：
1. **多模式无规颈缩理论（Brosa Multi-Modal Fission）**：
   在核裂变从鞍点（Saddle point）滑向断点（Scission point）的势能多维曲面上，量子壳效应开辟了数条互不相通的动力学裂变山谷（Fission Valleys）。总质量产额 $Y(A)$ 是多个独立物理模式的相干叠加：
   - **Standard I 模式（ST-I）**：受双幻核 $^{132}\text{Sn}$（$Z=50, N=82$）极其坚固的球形壳效应锁死，重碎片中心稳定锚定在 $A_H \approx 134$ 处。断点时两碎片极其紧凑，释放极高的库仑动能（$\text{TKE}$ 极大）；
   - **Standard II 模式（ST-II）**：受形变中子中壳闭合（$N \approx 88$ 形变壳）主导，重碎片峰位移动至 $A_H \approx 141$；
   - **Superlong 模式（SL）**：宏观无结构液滴的残存通道，经由极度延展的长圆柱形颈部发生对称断裂（$A_H = A_{\text{CN}}/2$），$\text{TKE}$ 最低；
2. **断点形变转化与瞬发中子“锯齿谱”（The Sawtooth Multiplicity $\bar{\nu}(A)$）**：
   在断点瞬间，两碎片因颈部撕裂而保留了剧烈的延伸形变。断裂后，形变弹性能迅速热化松弛为碎片的内禀激发能。
   由于 $^{132}\text{Sn}$ 附近碎片近乎为刚性硬球，几乎不承受任何断点形变，其激发能极低，**发射的瞬发中子极少（$\bar{\nu} \approx 0.5$）**；反之，其互补的轻碎片及 $A > 150$ 的极重碎片在断点时极度拉长，断裂后具有巨大内能，**发射大量瞬发中子（$\bar{\nu} \approx 2.5 \sim 3.5$）**，由此形成了闻名遐迩的**中子多重数“锯齿形”依赖曲线**！

---

## Necessary Assumptions

### 严格物理模型与系统学方程

### (1) Brosa 多模式高斯对叠加质量产额公式
总裂变质量分布（归一化为 $200\%$ 产额）：
$$Y(A) = 200 \sum_{m \in \{\text{ST1}, \text{ST2}, \text{SL}\}} w_m Y_m(A)$$
其中非对称模式由一对镜像对称的高斯函数构成：
$$Y_m(A) = \frac{1}{2 \sqrt{2\pi}\sigma_m} \left[ \exp\left(-\frac{(A - \bar{A}_{H, m})^2}{2\sigma_m^2}\right) + \exp\left(-\frac{(A - (A_{\text{CN}} - \bar{A}_{H, m}))^2}{2\sigma_m^2}\right) \right]$$
对热中子诱发 $^{235}\text{U}$ 裂变，标准权重比例约为：
$$w_{\text{ST1}} \approx 0.20, \quad w_{\text{ST2}} \approx 0.78, \quad w_{\text{SL}} \approx 0.02$$

---

### (2) Viola 裂变总动能（TKE）系统学公式
两裂变碎片在无限远处的总动能主要由断点处的相互静电库仑势能决定：
$$\langle\text{TKE}\rangle = 0.1189 \left( \frac{Z_{\text{CN}}^2}{A_{\text{CN}}^{1/3}} \right) + 7.3\text{ [MeV]}$$
各裂变模式因断点两核电荷中心间距 $d_{\text{sciss}}$ 不同，呈现出严格的能阶分离：
$$\text{TKE}_{\text{ST1}} > \text{TKE}_{\text{ST2}} > \text{TKE}_{\text{SL}}$$
- 紧凑的 Standard I 模式具有最小的颈长，库仑排斥最强烈，$\text{TKE}$ 高出平均值约 $10 \sim 15\text{ MeV}$；
- 超长 Superlong 对称模式在两碎片拉伸到极长距离后方才断裂，库仑排斥显著弱化，$\text{TKE}$ 低于平均值约 $20\text{ MeV}$。

---

### (3) 瞬发中子锯齿形多重数 $\bar{\nu}(A)$
根据原子核热力学统计蒸发理论，碎片每蒸发一个中子大约消耗结合能与平均动能 $S_n + 2T \approx 8.5\text{ MeV}$。
断裂能量守恒给出碎片平均瞬发中子数：
$$\bar{\nu}(A) = \frac{E_{\text{def}}(A) + E_{\text{int}}(A) - E_{\gamma, \text{rot}}}{S_n + 2T}$$
唯象紧凑形式反映了距 $^{132}\text{Sn}$ 壳层的距离：
$$\bar{\nu}(A_H) \approx 0.5 + 2.2 \left[ 1 - \exp\left(-0.06 |A_H - 132|^{1.3}\right) \right]$$
全事件平均瞬发中子产额为质量积分：
$$\bar{\nu}_{\text{tot}} = \frac{1}{200} \int Y(A) \bar{\nu}(A) dA \approx 2.4 \sim 3.8\text{ (n/fission)}$$

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/fission_fragment_mass_yield_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `fissfrag` 命令。

### 运行示范（模拟典型 $^{235}\text{U}(n, f)$ 裂变复合核 $^{236}\text{U}$）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py fissfrag -Z 92 -A 236 --json
```

### 计算输出核心物理特征：
1. **非对称双峰截面**：
   - 产生强烈的双峰裂变产额：轻碎片峰位于 $A_L = 96$，重碎片峰位于 $A_H = 140$；
   - 质量非对称比值达到 $A_H / A_L = 1.458$，再现了热中子裂变的经典双峰实验谱；
2. **Viola 动能系统学**：
   - 库仑参数 $Z^2 / A^{1/3} = 1369.6$，预测平均 $\text{TKE} = 170.15\text{ MeV}$；
   - 紧凑 Standard I 动能高达 $182.15\text{ MeV}$，而 Superlong 对称裂变动能骤降至 $150.15\text{ MeV}$；
3. **锯齿形瞬发中子谱**：
   - 在 $A \approx 130 \sim 132$ 处，中子多重数大幅探底至 $\bar{\nu} \approx 0.8\text{ n/frag}$；
   - 在 $A = 115$ 与 $A = 155$ 等大形变碎片处，多重数大幅抬升至 $2.6 \sim 2.8\text{ n/frag}$；
   - 平均单次裂变发射 $\bar{\nu}_{\text{tot}} = 3.47$ 个瞬发中子，为反应堆中子学与核裂变反中微子能谱提供了严格物理约束！

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用

- [[fission-barriers-strutinsky-and-superheavy-dynamics]]：双峰裂变势垒的高度与第二势阱深度直接决定了穿透到多模式断裂山谷的几率；
- [[beta-decay-phase-space-log-ft-and-cvc-unitarity]]：两碎片及其同量异位素链的 $\beta$ 衰变级联直接构成了核反应堆衰变热与反应堆中微子反常（RAA）的物理源头。
