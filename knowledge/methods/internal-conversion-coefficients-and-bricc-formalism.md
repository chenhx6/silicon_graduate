---
type: method
method_type: experimental-analysis-contract
title: "原子核内转换系数（ICC）、多极性鉴别与 BrIcc 参数化计算指南"
aliases: [内转换系数, ICC计算指南, BrIcc参数化, 转换电子谱学, 内转换多极性鉴别]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [internal-conversion, bricc, icc, multipolarity-assignment, conversion-electrons, intensity-balance]
---

# 原子核内转换系数（ICC）、多极性鉴别与 BrIcc 参数化计算指南

## Purpose

### 物理全景：光子发射与电子内转换的电磁竞争

原子核激发态退激时，核内质子与中子波函数重排产生的电磁多极时变场不仅能向远场辐射真实光子（$\gamma$ 射线），而且能直接与原子核外的电子壳层（特别是空间概率密度最靠拢核电荷的 $K$ 壳层和 $L$ 壳层电子）发生近场库仑微扰，将能量直接传递给束缚电子并将其弹出原子，这一量子过程称为**内转换（Internal Conversion）**。

根据 W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》与 T. Kibédi 等（BrIcc 评述，Nucl. Instr. Meth. A 589, 202, 2008）：
1. **定义**：内转换电子发射速率与真实光子发射速率之比定义为**内转换系数（Internal Conversion Coefficient, ICC, 记为 $\alpha$）**：
   $$\alpha \equiv \frac{W_e}{W_\gamma} = \frac{I_e}{I_\gamma}$$
2. **壳层分解**：总内转换系数等于各原子壳层内转换系数的代数和：
   $$\alpha_{\text{tot}} = \alpha_K + \alpha_{L1} + \alpha_{L2} + \alpha_{L3} + \alpha_M + \dots$$
3. **多极性鉴别的终极性**：
   与角分布 $W(\theta)$ 容易受到自旋取向展宽 $\sigma/I$ 和数学双根退化的影响不同，**内转换系数 $\alpha$ 具有严格的无模型依赖性，其数值大小和壳层转换比（$K/L$ 比值）直接由初末态跃迁的多极性（$E1, M1, E2, M2$ 等）严格唯一锁定**！

---

## Inputs and Assumptions

### 内部转换系数的微观标度律与相对论特征

在非相对论与高能极限下，Born 近似给出内转换系数对原子序数 $Z$、能量 $E_\gamma$ 与极数 $L$ 的典型标度律：
$$\alpha(EL) \propto Z^3 \left( \frac{2 m_e c^2}{E_\gamma} \right)^{L + 7/2}$$
$$\alpha(ML) \propto Z^3 \left( \frac{2 m_e c^2}{E_\gamma} \right)^{L + 5/2}$$

**核心物理特征**：
1. **能量负幂次发散**：$\alpha$ 随着光子能量 $E_\gamma$ 降低急剧暴增（正比于 $E_\gamma^{-(L+5/2)}$）。在低能跃迁（$E_\gamma < 100\text{ keV}$）中，内转换往往成为主导衰变模式（$\alpha \gg 1$）；
2. **极数正相关**：跃迁的多极数 $L$ 越高，光子波函数受离心势垒阻碍越强，而内转换电子在核内直接发生相互作用，因此高多极跃迁的 $\alpha$ 远大于低多极跃迁；
3. **电磁宇称区分能力**：
   在相同的跃迁能量下，不同多极性的 $\alpha_K$ 存在数量级分立：
   $$\alpha_K(E1) \ll \alpha_K(M1) < \alpha_K(E2) \ll \alpha_K(M2) < \alpha_K(E3)$$
   这为实验上区分宇称改变的偶极跃迁（纯 $E1$）与宇称守恒的偶极跃迁（$M1+E2$）提供了决定性的裁判标准！

---

## What It Can Establish

### 理论判据与可观测量

## What It Cannot Establish Alone

### 混合跃迁（$M1+E2$）内转换与总跃迁强度计算

在高自旋三轴能带与旋称伙伴带中，最普遍存在的是 $\Delta I = 1$ 的 $M1 + E2$ 混合跃迁。

### (1) 混合内转换系数计算公式
由于内转换矩阵元与光子辐射矩阵元同源，总内转换系数由多极混合比 $\delta = \langle E2 \rangle / \langle M1 \rangle$ 严格调制：
$$\alpha_{\text{tot}}(\delta) = \frac{\alpha_{\text{tot}}(M1) + \delta^2 \cdot \alpha_{\text{tot}}(E2)}{1 + \delta^2}$$

### (2) 能级总辐射强度平衡修正
探测器仅能测量发射光子的峰计数，由此提取的光子强度为 $I_\gamma$。然而，从能级流失的真实微观跃迁总强度必须计入所有被内转换带走的电子：
$$I_{\text{tot}} = I_\gamma + I_e = I_\gamma \cdot [1 + \alpha_{\text{tot}}(\delta)]$$
若在能级纲图构建中忽略 $[1 + \alpha_{\text{tot}}]$ 因子：
- 在高能区（$E_\gamma > 500\text{ keV}$），$\alpha_{\text{tot}} < 0.01$，影响微弱；
- 在低能区（如 $A\approx 130$ 区中经常出现的 $E_\gamma \approx 50 \sim 150\text{ keV}$ 的关键连接线），$\alpha_{\text{tot}} \approx 0.5 \sim 5.0$，**若不经转换修正，能级流出强度将被严重低估数倍，直接导致能级强度平衡方程崩溃**！


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
