---
type: method
method_type: experimental-analysis-contract
title: "在束谱学 ADO 比值、线偏振度与多极性二维联合判决指南"
aliases: [ADO比值分析, POL-ADO联合判决, 多极混合比2D扫描, Clover偏振拟合, 角分布比值法]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [ado-ratio, linear-polarization, clover-detectors, multipole-mixing-ratio, dual-root-elimination, in-beam-spectroscopy]
---

# 在束谱学 ADO 比值、线偏振度与多极性二维联合判决指南

## Purpose

### 物理测量背景：全角度拟合与特征环比值的互补

在在束 $\gamma$ 谱学实验中，测定辐射跃迁的电磁多极性（如纯四极 $E2$、纯偶极 $E1/M1$、或偶极-四极混合跃迁 $M1+E2$）是建立原子核自旋宇称与能带结构判据的基石。

根据 W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》与吴治华《原子核物理实验方法》（第 10 章）：
1. **全角度拟合局限**：对包含 10–15 个角度的完整角分布 $W(\theta)$ 拟合，需要极高且均衡的统计计数；当某条关键弱跨带线统计量有限时，全角度拟合误差往往很大；
2. **ADO 比值（Angular Distribution from Oriented States Ratio）的高信噪比优势**：
   探测器阵列（如中国原子能院 HI-13 谱仪、南非 iThemba AFRODITE 阵列或 Gammasphere）通常由特定的对称环构成（如前向/后向环 $\theta_1 = 30^\circ/150^\circ$ 与垂直环 $\theta_2 = 90^\circ$）。直接对这两个环提取效率归一化计数比值，称为 **ADO 比值（$R_{\text{ADO}}$）**；
3. **联合 Clover 线偏振（POL-ADO 2D Analysis）**：
   结合垂直环上 Clover 复合探测器的康普顿散射不对称度线偏振测量，构建二维联合似然空间，彻底解除混合比 $\delta$ 的数学双根退化！

---

## Inputs and Assumptions

### 核心数学方程与多极性响应特征

### (1) ADO 比值理论公式
定向核发射的 $\gamma$ 射线角分布展开为：
$$W(\theta) = 1 + a_2 P_2(\cos\theta) + a_4 P_4(\cos\theta)$$
ADO 比值定义为前向（或后向）环与 $90^\circ$ 环的理论比值：
$$R_{\text{ADO}} \equiv \frac{W(\theta_1)}{W(\theta_2)} = \frac{1 + a_2 P_2(\cos\theta_1) + a_4 P_4(\cos\theta_1)}{1 + a_2 P_2(\cos\theta_2) + a_4 P_4(\cos\theta_2)}$$

对于典型的探测器环角度配置（$\theta_1 = 30^\circ, \theta_2 = 90^\circ$）：
$$P_2(\cos 30^\circ) = +0.625, \quad P_2(\cos 90^\circ) = -0.500$$
$$P_4(\cos 30^\circ) = +0.180, \quad P_4(\cos 90^\circ) = +0.375$$

**特征多极性参考窗口**：
- **拉伸四极跃迁（Stretched $E2$, $\Delta I = 2$）**：
  $a_2 \approx +0.30, a_4 \approx -0.05 \implies R_{\text{ADO}}(30^\circ/90^\circ) \approx 1.30 \sim 1.45$；
- **纯偶极跃迁（Stretched Dipole, $\Delta I = 1$, 纯 $E1$ 或纯 $M1$）**：
  $a_2 \approx -0.25, a_4 \approx 0.0 \implies R_{\text{ADO}}(30^\circ/90^\circ) \approx 0.70 \sim 0.80$；
- **非拉伸偶极跃迁（$\Delta I = 0$）**：
  $a_2 \approx +0.35, a_4 \approx 0.0 \implies R_{\text{ADO}}(30^\circ/90^\circ) \approx 1.40 \sim 1.55$。

### (2) 多极混合比 $\delta(E2/M1)$ 对 ADO 的非线性调制
对于最常见的 $\Delta I = 1$ 偶极-四极混合跃迁，角分布系数是混合比 $\delta$ 的二次分式：
$$a_2(\delta) = \alpha_2 \frac{F_2(1 1 I_f I_i) + 2\delta F_2(1 2 I_f I_i) + \delta^2 F_2(2 2 I_f I_i)}{1 + \delta^2}$$
$$a_4(\delta) = \alpha_4 \frac{\delta^2 F_4(2 2 I_f I_i)}{1 + \delta^2}$$
其中 $\alpha_2 = B_2/B_0$ 与 $\alpha_4 = B_4/B_0$ 为依赖于自旋取向展宽参数 $\sigma/I$ 的取向衰减因子。

---

## What It Can Establish

### 理论判据与可观测量

## What It Cannot Establish Alone

### Clover 探测器康普顿线偏振度（Linear Polarization）与双根破除

在 $90^\circ$ 处放置的 Clover 探测器由 4 个独立的 $n$-型 HPGe 晶体组成。当光子入射并在一个晶体中发生康普顿散射、在相邻晶体中被吸收时：
1. **散射不对称度（Asymmetry Ratio）**：
   $$\Delta_{\text{IPDCO}} = \frac{N_\perp - a \cdot N_\parallel}{N_\perp + a \cdot N_\parallel}$$
   其中 $a = N_\perp^{\text{unpol}} / N_\parallel^{\text{unpol}}$ 为偏振仪本征几何不对称因子（通常由标准无偏振源如 $^{152}\text{Eu}$ 精确校准，约在 $1.00 \pm 0.02$）。
2. **绝对线偏振度 $P$**：
   $$P = \frac{\Delta_{\text{IPDCO}}}{Q(E_\gamma)}$$
   其中 $Q(E_\gamma)$ 为康普顿散射偏振灵敏度系数（通常随能量在 $0.15 \sim 0.25$ 之间）。

### (3) 二维联合剖面似然（2D Profile Likelihood）判决法则：
对候选物理态构建联合检验卡方：
$$\chi^2(\delta) = \left( \frac{R_{\text{ADO}}^{\text{exp}} - R_{\text{ADO}}^{\text{theo}}(\delta)}{\sigma_{R_{\text{ADO}}}} \right)^2 + \left( \frac{P^{\text{exp}} - P^{\text{theo}}(\delta)}{\sigma_P} \right)^2$$

**判决法典**：
- 仅凭 $R_{\text{ADO}}$ 会在 $\chi^2$ 空间产生两个等价的深谷（绝对双根退化）；
- 引入 $P$ 之后，由于磁跃迁与电跃迁在线偏振灵敏度公式中的分子交叉项相差一个负号，其中一个解处的 $\chi^2$ 将剧增；
- **若 $\Delta\chi^2 > 9.0$（排除显著性 $> 3\sigma$），即可合法宣称证伪假根，确立唯一起源！**


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
