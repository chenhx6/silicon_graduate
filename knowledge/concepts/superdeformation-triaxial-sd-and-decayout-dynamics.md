---
type: concept
title: "超形变（SD）、三轴超形变（TSD）与能带退激穿透动力学"
aliases: [超形变物理, 三轴超形变TSD, SD退激穿透, 摆动运动首创实验, 2:1轴比椭球]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [superdeformation, triaxial-superdeformation, tsd-wobbling, decayout-tunneling, 163lu, a130-hd-bands]
---

# 超形变（SD）、三轴超形变（TSD）与能带退激穿透动力学

## 1. 物理全景：宏观空间几何轴比 2:1 的量子孤岛

在原子核有限量子多体系统中，常规四极形变通常处于中等幅度（轴比约 1.2:1 至 1.3:1，对应 $\beta_2 \approx 0.2 \sim 0.3$）。然而，当原子核处于高速推旋转动时，单粒子平均场中会出现一组全新的具有简单整数组合（如长轴与短轴之比为 2:1）的宏观壳层闭合，称为**超形变（Superdeformation, SD: $\beta_2 \approx 0.6 \sim 0.7$）**。

根据 C. M. Petrache 主编《Chirality and Wobbling in Atomic Nuclei》（2024）与 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II：
1. **微观次级势阱（Second Potential Well）**：
   宏观液滴能量随形变单调上升，但由于特定的超形变幻数（如 $Z=66, N=86$ 或 $Z=80, N=112$）产生的微观壳修正能极大下凹，使得总势能曲面（TRS）在 $\beta_2 \approx 0.6$ 处形成一个深度达数兆电子伏的次级稳定极小值；
2. **三轴超形变（Triaxial Superdeformation, TSD）**：
   在镥-钽（Lu-Ta, $A\approx 160 \sim 170$）质量区，核芯在保持极大伸长四极形变的同时，自发产生稳定的三轴非对称性（$\gamma \approx 20^\circ \sim 25^\circ$），成为**人类首次在实验上证实量子化摆动进动（Wobbling motion）的摇篮**；
3. **退激脱落（Decay-out）量子隧穿机制**：
   超形变带如何突然终止并向密集正常形变（ND）基带退激，是连接低温微观结构与高温统计混沌态的终极桥梁。

---

## 2. 三轴超形变（TSD）核中的多声子摆动运动实验基准

在 2001–2003 年期间，国际核物理界在哥本哈根与法国利用 EUROBALL 阵列取得了一系列划时代发现：

### (1) $^{163}\text{Lu}$ 摆动模式的历史首创（Ødegård et al. 2001 PRL）
- 在 $^{163}\text{Lu}$ 中发现了基于高 $j$ 准质子 $\pi i_{13/2}$ 组态的 TSD 能带（$\epsilon_2 \approx 0.38, \gamma \approx 20^\circ$）；
- 在主带（$n_w=0$）上方紧邻处观测到伴随带（$n_w=1$），两带由强烈的跨带 $\Delta I=1$ 纯 $E2$ 射线相连接；
- 测得跨带减缩跃迁几率 $B(E2; n_w=1 \to n_w=0) \approx 20 \sim 100\text{ W.u.}$，以无可辩驳的证据证实了 Bohr-Mottelson 预言半个世纪的三轴转子量子摆动运动！

### (2) 二声子摆动模式的确立（Jensen et al. 2002 PRL）
- 随后在主带上方进一步观测到了二声子激发能带（$n_w=2$）；
- 跨带退激满足声子消灭选择定则：$n_w=2$ 态优先向 $n_w=1$ 态退激，而向 $n_w=0$ 态的直接双声子跃迁被强烈压制；
- 证实了摆动运动在小振幅极限下严格服从一维量子简谐振子的声子代数。

---

## 3. 超形变带退激脱落（Decay-out）统计穿透理论

超形变能带在谱线上具有极其独特的“突然死亡”特征：在自旋 $I \ge 25 \sim 60\hbar$ 范围内，带内发射系列等间距四极 $\gamma$ 射线（$\Delta E_\gamma \approx \text{常数}$，强度保持 $100\%$）；然而当自旋下降到某一临界自旋 $I_{\text{decay}}$ 时，**整条能带在 1–2 个自旋步长内彻底消失**！

### (1) 竞争退激微观分支比
在自旋 $I$ 处，系统面临两大竞争通道：
1. **带内集体四极退激几率（In-band $E2$）**：
   $$\Gamma_{\text{in}} = \frac{1}{\tau_{\text{in}}} \propto E_\gamma^5 \cdot Q_t^2(\text{SD})$$
   由于跃迁能量随自旋下降按 $E_\gamma \propto I$ 递减，$\Gamma_{\text{in}} \propto I^5$ 急剧暴跌！
2. **穿透势垒向正常态的统计隧穿几率（Tunneling Decay-out）**：
   $$\Gamma_{\text{out}} = \Gamma_{\text{tunnel}} = \frac{\hbar \omega_{\text{barrier}}}{2\pi} \cdot P_{\text{WKB}}$$
   其中 WKB 穿透几率为：
   $$P_{\text{WKB}} = \exp\left[ -\frac{2}{\hbar} \int_{\text{well1}}^{\text{well2}} \sqrt{2 M(s) (V(s) - E)} ds \right]$$

### (2) 临界脱落自旋判据
当转动自旋下降到临界点使得带内辐射几率与势垒隧穿几率相当时：
$$\frac{\Gamma_{\text{out}}(I_{\text{decay}})}{\Gamma_{\text{in}}(I_{\text{decay}})} \approx 1.0$$
此时波函数与致密的正常形变复合核态发生强力共振混沌混合，$\gamma$ 退激能量瞬间分散到数万条不可分辨的统计暗通道中，导致超形变带宏观上突然“熄灭”。

---

## 4. 对本 Wiki $A\approx 130$ 质量区高形变带（HD）的直接指引

在铈同位素（如 $^{131}\text{Ce}$ 与 $^{132}\text{Ce}$）中，实验上早已观测到著名的**高形变能带（Highly Deformed Bands, HD: $\beta_2 \approx 0.35 \sim 0.40$）**：
1. **动力学转动惯量平坦度检验**：
   调用本指南的算法，通过检验 $\mathcal{J}^{(2)}$ 是否在宽频率区间保持平坦无回弯平台，严格判定其是否属于微观次级势阱中的超形变/高形变相；
2. **脱落点寻找**：
   在 $^{131}\text{Ce}$ CIAE HI-13 实验中，高形变能带向基态带的连接线极其微弱；利用 WKB 势垒穿透模型，可反演阻隔次级势阱的微观单极势垒高度，为寻找极端微弱的脱落连接线提供能量与多极性预测窗口！
