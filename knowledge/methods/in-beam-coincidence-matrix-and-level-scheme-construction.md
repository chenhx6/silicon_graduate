---
type: method
method_type: experimental-analysis-contract
title: "在束 γ-γ 符合矩阵分析、背景扣除与能级纲图构建实战指南"
aliases: [符合矩阵分析指南, 能级纲图构建, 背景扣除算法, 跃迁强度平衡, Radware方法论]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [coincidence-matrix, background-subtraction, intensity-balance, level-scheme, efficiency-calibration, radware]
---

# 在束 γ-γ 符合矩阵分析、背景扣除与能级纲图构建实战指南

## Purpose

### 物理测量全景：从原始事件列表（List-mode Data）到能级纲图

在束重离子核反应中，探测器阵列（如多探头 HPGe 阵列）以多参数事件列表（List-mode data: 包含时间戳 $t_i$、探测器编号 $\text{det}_i$、脉冲幅度 $E_i$）记录所有光子信号。

根据吴治华《原子核物理实验方法》（第 10 章）与在束谱学国际标准（如 Radware 软件包算法），将百亿字节的离线数据转化为清晰自洽的原子核能级纲图，必须经历以下**五大离线处理台阶**：

```
  ┌─────────────────────────────────────────────────────────────┐
  │ 【台阶 1: 时间符合选门与偶然符合扣除 (Prompt vs Random)】   │
  │  - 设定 20-50 ns 即时时间窗提取真符合                       │
  │  - 设定离轴宽时间窗估计并扣除偶然符合本底                   │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 【台阶 2: 二维能量对称符合矩阵构建 (E1 - E2 Matrix)】      │
  │  - 探测器增益对齐 (Gain matching: 0.5 keV/channel)          │
  │  - 剔除同探测器自符合与散射串扰 (Cross-talk rejection)      │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 【台阶 3: 峰门选谱与三点连续背景扣除 (3-Point Subtraction)】 │
  │  - 选取峰门区间 [G_low, G_high]                             │
  │  - 选取两翼纯康普顿连续本底门 [B1_low, B1_high] & [B2...]   │
  │  - 执行归一化面积差分，提取纯净级联退激一维能谱             │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 【台阶 4: 全能峰探测效率校准与发射光子强度计算】           │
  │  - 利用 152Eu, 133Ba 标准源拟合效率曲线 epsilon(E)          │
  │  - 发射光子强度归一化: I_gamma = Area / epsilon(E)          │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 【台阶 5: 节点进出强度平衡方程与纲图闭环检验】             │
  │  - 考虑内转换系数: I_tot = I_gamma * (1 + alpha_tot)        │
  │  - 对每个能级检验: Total Inflow == Total Outflow            │
  │  - 定位强度不平衡节点 -> 发现未观测弱线或形状共存转换跃迁   │
  └─────────────────────────────────────────────────────────────┘
```

---

## Inputs and Assumptions

### 核心算法与数学差分方程

### (1) 标准三点背景扣除法（Standard 3-Point Background Subtraction）
在对二维符合矩阵投门时，若仅仅对全能峰所在的能量通道求和，所得的一维能谱中将不可避免地混入该能量下方的**连续康普顿散射本底所产生的伪符合峰**。

设峰门区间为 $[G_{\text{low}}, G_{\text{high}}]$，通道宽度为 $W_G = G_{\text{high}} - G_{\text{low}} + 1$；
在全能峰左右两侧无特征峰的平坦康普顿平原分别选取左背景门 $[B1_{\text{low}}, B1_{\text{high}}]$（宽 $W_{B1}$）与右背景门 $[B2_{\text{low}}, B2_{\text{high}}]$（宽 $W_{B2}$）。

从矩阵中投影出的切片谱分别记为 $P(E), B_1(E), B_2(E)$。净级联符合谱为：
$$S(E) = P(E) - f_B \cdot \left[ B_1(E) + B_2(E) \right]$$
其中背景归一化权重因子为：
$$f_B = \frac{W_G}{W_{B1} + W_{B2}}$$
该算法严格消除了连续康普顿背景对能谱拓扑的污染，是确认两条 $\gamma$ 射线是否处于同一退激级联链条的黄金判据。

### (2) 探测器阵列全能峰效率校准（Radware 经验公式）
在宽能区（$50\text{ keV} \sim 4\text{ MeV}$），HPGe 探测器阵列的绝对/相对全能峰探测效率 $\epsilon(E_\gamma)$ 由对数多项式严格参数化：
$$\ln\epsilon(E_\gamma) = \left[ (A + B x + C x^2)^{-G} + (D + E y + F y^2)^{-G} \right]^{-1/G}$$
其中 $x = \ln(E_\gamma / 100\text{ keV})$（低能项），$y = \ln(E_\gamma / 1000\text{ keV})$（高能项），$G$ 为平滑过渡参数。

由此计算出每条 $\gamma$ 射线的发射相对强度：
$$I_\gamma = \frac{\text{Net\_Peak\_Area}}{\epsilon(E_\gamma)}$$

---

## What It Can Establish

### 理论判据与可观测量

## What It Cannot Establish Alone

### 纲图拓扑构建：节点进出强度平衡方程（Intensity Balance）

在建立的激发态能级纲图中，对于任何一个非基态中间能级 $L_k$（激发能 $E_k$，自旋宇称 $I_k^\pi$），依据电荷与微观粒子流守恒，**从上方所有能级馈入该能级的总跃迁强度，必须严格等于从该能级向下退激的所有跃迁总强度**：

$$\sum_{j > k} I_{\text{tot}}(L_j \to L_k) + I_{\text{feeding}}^{\text{side}}(L_k) = \sum_{m < k} I_{\text{tot}}(L_k \to L_m)$$

其中总跃迁强度 $I_{\text{tot}}$ 必须包含内转换电子（Internal Conversion Electron, ICE）的贡献：
$$I_{\text{tot}} = I_\gamma \cdot (1 + \alpha_{\text{tot}})$$
（$\alpha_{\text{tot}}$ 由 BrIcc 转换系数程序包精确提供）。

### (1) 强度泄漏（Intensity Leakage）排查
若在实验分析中发现某能级流出强度显著大于已知流入强度（$\Delta I = I_{\text{out}} - I_{\text{in}} > 3\sigma$）：
1. 表明存在**尚未被识别的高自旋侧馈送跃迁（Side feeding）**；
2. 提示该能级可能是某条未知弱能带的带头（Bandhead）。

### (2) 强度阻断（Intensity Stagnation）排查
若流入强度显著大于流出强度（$I_{\text{in}} \gg I_{\text{out}}$）：
1. 表明该能级向下存在**未被观测到的极低能跃迁（$E_\gamma < 50\text{ keV}$）**，由于 HPGe 铍窗与死层吸收无法探测，但具有极大的内转换系数 $\alpha_{\text{tot}} \gg 10$；
2. 提示存在**电单极 $E0$ 纯转换电子跃迁**（常见于形状共存原子核中不同形变基带之间的混合脱激）。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
