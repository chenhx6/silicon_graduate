---
type: method
method_type: experimental-analysis-contract
title: "在束级联侧馈送动力学、时间延迟分布与多普勒线形解卷积指南"
aliases: [侧馈送动力学, Side-Feeding解卷积, 多普勒线形侧馈修正, 顶门符合寿命法, DSAM时间延迟修正]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [side-feeding, dsam, doppler-lineshape, lifetime-measurements, top-gate-coincidence, quasicontinuum-cascade]
---

# 在束级联侧馈送动力学、时间延迟分布与多普勒线形解卷积指南

## Purpose

### 物理测量背景：准连续态级联与横向馈送

在重离子熔合蒸发反应中，由高速旋转核芯蒸发数个轻粒子后形成的残核，初始处于激发能 $E^* \approx 10 \sim 30\text{ MeV}$、角动量高达 $30 \sim 50\hbar$ 的致密**准连续态区（Quasicontinuum Region）**。

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II 与吴治华《原子核物理实验方法》（第 15 章）：
1. **能量瀑布流**：系统首先通过高能统计连续 $E1$ 跃迁迅速冷却，继而在 yrast 线平行的准连续态中通过大量的非集体/集体四极跃迁逐步向下流动；
2. **侧馈送（Side Feeding）概念**：
   当离散能带中的某一能态 $I$ 被激发时，它所接收的粒子流由两部分组成：
   - **带内直接下落（Direct In-band Feeding）**：来自上一相邻能级 $I+2$ 的直接级联退激；
   - **横向侧馈送（Side Feeding）**：从准连续态横向直接注入该能级的光子流（通常由多条不可分辨的微弱快级联汇聚而成）。
3. **测量危机**：侧馈送流并非瞬间到达，而是带有特征的时间延迟分布（$\tau_{\text{feed}} \sim 10 \sim 500\text{ fs}$）。若在 DSAM 寿命反演中忽视侧馈送，测得的表观多普勒衰减因子 $F(\tau)$ 将严重偏小，导致**能态内禀寿命被虚假拉长，内禀四极矩 $Q_t$ 与微观形变被严重低估**！

---

## Inputs and Assumptions

### 连续时间卷积积分与多普勒衰减因子 $F(\tau, \tau_{\text{feed}})$ 严格修正

### (1) 双能级瞬态布居微分方程
设能级自身的内禀寿命为 $\tau_0$；从侧馈送通道注入的粒子流强度比为 $f_{\text{feed}} \in [0, 1]$（带内直接流占比 $1 - f_{\text{feed}}$）。
假定侧馈送级联的时间延迟服从特征参数为 $\tau_{\text{feed}}$ 的单指数分布：
$$\frac{d N_{\text{feed}}(t)}{dt} = \frac{f_{\text{feed}}}{\tau_{\text{feed}}} \exp\left( -\frac{t}{\tau_{\text{feed}}} \right)$$

待测能级的布居数 $N(t)$ 满足卷积微分方程：
$$\frac{d N(t)}{dt} = -\frac{N(t)}{\tau_0} + (1 - f_{\text{feed}}) \cdot \delta(t) + \frac{d N_{\text{feed}}(t)}{dt}$$

解析解出待测能级发射光子的瞬态时间几率密度分布：
$$P(t) = \frac{1 - f_{\text{feed}}}{\tau_0} e^{-t/\tau_0} + \frac{f_{\text{feed}}}{\tau_0 - \tau_{\text{feed}}} \left[ e^{-t/\tau_0} - e^{-t/\tau_{\text{feed}}} \right]$$

### (2) 考虑侧馈送的多普勒衰减因子积分
在反冲核指数减速模型（$v(t) = v_0 e^{-t/\alpha}$，$\alpha$ 为衬底慢化时间）下，实验可测的平均频移比例定义为：
$$F_{\text{eff}} \equiv \int_0^\infty \frac{v(t)}{v_0} P(t) dt$$
代入 $P(t)$ 解析完成拉普拉斯积分，推导出著名的**双时间参数多普勒衰减定理**：
$$F_{\text{eff}}(\tau_0, \tau_{\text{feed}}, f_{\text{feed}}) = (1 - f_{\text{feed}}) \cdot \frac{\alpha}{\alpha + \tau_0} + f_{\text{feed}} \cdot \frac{\alpha}{\alpha + \tau_0 + \tau_{\text{feed}}}$$

**物理精要反思**：
- 若 $\tau_{\text{feed}} = 0$（瞬发侧馈），上式退化为无侧馈单能级解 $F = \frac{\alpha}{\alpha + \tau_0}$；
- 若侧馈送时间显著（$\tau_{\text{feed}} > 0$），由于分母增大了 $\tau_{\text{feed}}$，导致在相同的内禀寿命 $\tau_0$ 下，$F_{\text{eff}}$ 明显变小（表现出更大的多普勒减速滞后）；
- **如果不经解卷积直接反演，提取出的表观寿命 $\tau_{\text{app}} = \tau_0 + f_{\text{feed}} \tau_{\text{feed}}$ 严重虚胖**！

---

## What It Can Establish

### 理论判据与可观测量

## What It Cannot Establish Alone

### 破局方案：顶门符合法（Top-Gating Coincidence Method）

为了从实验测量根本上彻底消除侧馈送时间模型的非唯一性与系统误差，现代大阵列核谱学必须执行**顶门符合（Top-Gate Coincidence）**：

```
  [准连续态 Quasicontinuum]
       │
       ▼ (侧馈流仅注入顶端能级)
  ┌────────────────────────────────────────────────────────┐
  │ [顶端能级 I_top + 2]                                   │
  │   │                                                    │
  │   ▼ 【设立严格符合门 (Gating Transition)】              │
  │ [待测能级 I_top]  ─────────────────────────────────┐   │
  │   │ (此时侧馈送被完全隔离在外，进流 100% 确定为上级单线)│   │
  │   ▼                                                │   │
  │ [待测能级 I_top - 2]                               │   │
  └────────────────────────────────────────────────────┴───┘
```

**实战协议**：
1. 在 $\gamma-\gamma$ 矩阵中，将选门通道严格卡在待测能级上方的顶端跃迁；
2. 门谱中下方所有跃迁接收的进流在时间上由顶门跃迁唯一锚定，横向未分辨侧馈送被物理隔绝（$f_{\text{feed}} \to 0$）；
3. 此时直接应用解析反演公式 $\tau_0 = \alpha (1/F - 1)$，提取出的寿命具有极高置信度与严格的微观模型独立性！


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
