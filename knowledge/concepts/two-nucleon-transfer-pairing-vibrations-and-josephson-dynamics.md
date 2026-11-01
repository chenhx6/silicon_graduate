---
type: concept
title: "两核子转移反应（Two-Nucleon Transfer）、配对振动（Pairing Vibrations）与原子核约瑟夫森效应动力学"
aliases: [两核子转移反应, 配对振动, 巨对振动, GPV, 约瑟夫森超流, 核库珀对隧穿, 对增加模, 对去除模, (p,t)反应]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [two-nucleon-transfer, pairing-vibrations, giant-pairing-vibration, nuclear-josephson-effect, bcs-superfluidity, cooper-pair, magnex]
---

# 两核子转移反应（Two-Nucleon Transfer）、配对振动（Pairing Vibrations）与原子核约瑟夫森效应动力学

## 1. 物理全景：规范空间对称性破缺与核超流体探针

在原子核多体物理中，若粒子数守恒（$U(1)$ 规范对称性）发生自发对称性破缺，核系统进入 BCS 超流相（Superfluid Phase），基态成为不具有确定粒子数的 Cooper 对相干凝聚态：
$$|BCS\rangle = \prod_{k>0} (u_k + v_k a_k^\dagger a_{\bar{k}}^\dagger) |0\rangle$$

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II（第 6 章）、D. R. Bès & R. A. Broglia (Nucl. Phys. 80, 289, 1966)、C. A. Bertulani《Introduction to Nuclear Reactions》与 M. Cavallaro et al. (Nature Commun. 10, 167, 2019)：
1. **两核子转移作为超流特异性探针**：
   单核子转移反应（如 $(d, p)$）只能探测单粒子谱因子（Spectroscopic Factors）；而**两核子转移反应（如 $(p, t)$、$(t, p)$ 与重离子 $(^{18}\text{O}, {}^{16}\text{O})$）在反应瞬间转移一对空间高度关联的 $J^\pi = 0^+, T=1$ 核子对（核 Cooper 对）**，是直接测量原子核配对波函数相干性与超流相变的排他性工具！
2. **超流基态相干增强因子（Coherent Enhancement）**：
   在开壳超流核中，费米面附近所有退化轨道的配对振幅同相叠加（In-phase Coherence），导致基态到基态（$0_{\text{g.s.}}^+ \to 0_{\text{g.s.}}^+$）的转移截面展现出**较纯单粒子无关联转移高出 $15 \sim 50$ 倍的巨大集体增强**！

---

## 2. 配对振动（Pairing Vibrations）：规范空间简谐声子场论

在双幻闭壳核（如 $^{208}\text{Pb}$ 或 $^{132}\text{Sn}$）附近，系统处于正常费米液体相（未形成静态配对形变凝聚），但对相互作用诱发了体系在**规范空间（Gauge Space）围绕对称点发生的微幅简谐振动——即配对振动模式（Pairing Vibrations）**。

### (1) 对增加模与对去除模算符
根据 Bès-Broglia 场论，定义两类基本配对声子生成算符：
- **对增加声子（Pair Addition Phonon, $\alpha_+^\dagger$）**：将粒子数增加 2（$\Delta N = +2$），对应基态转移反应 $(t, p)$ 或 $(^{18}\text{O}, {}^{16}\text{O})$；
- **对去除声子（Pair Removal Phonon, $\alpha_-^\dagger$）**：将粒子数减少 2（$\Delta N = -2$），对应基态转移反应 $(p, t)$。

两类声子具有明确的微观激发能：
$$\hbar\omega_+ = E_{\text{g.s.}}(A+2) - E_{\text{g.s.}}(A) + 2\lambda_F$$
$$\hbar\omega_- = E_{\text{g.s.}}(A-2) - E_{\text{g.s.}}(A) - 2\lambda_F$$
其中 $\lambda_F$ 为闭壳核芯费米能级化学势。

### (2) 双声子四重态与配对振动同核多重态
在闭壳核 $^{208}\text{Pb}$ 中：
- 单声子态：$^{210}\text{Pb}_{\text{g.s.}}$ 是纯对增加单声子态 $|1, 0\rangle$；$^{206}\text{Pb}_{\text{g.s.}}$ 是纯对去除单声子态 $|0, 1\rangle$；
- **组合双声子态 $|1, 1\rangle$**：在 $^{208}\text{Pb}$ 中，存在一个激发能严格满足 $E_x \approx \hbar\omega_+ + \hbar\omega_- \approx 4.87\text{ MeV}$ 的激发的集体 $0^+$ 态！
  - 该态在 $^{206}\text{Pb}(t, p)^{208}\text{Pb}$ 中以与基态相当的截面强力布居；
  - 同时在 $^{210}\text{Pb}(p, t)^{208}\text{Pb}$ 中亦以同等强度被选择性激发，完美确立了原子核规范对称性振动的谐振子代数！

---

## 3. 巨对振动（Giant Pairing Vibration, GPV）与运动学匹配

1. **跨壳巨配对激发（$2\hbar\omega$ GPV）**：
   Broglia 与 Hansen 预言，正如巨偶极共振是粒子-空穴跨壳激发，两核子转移中同样存在跨越主壳层（$2\hbar\omega$ 能隙，激发能 $E_x \sim 10 \sim 15\text{ MeV}$）的**巨对振动（Giant Pairing Vibration, GPV）**；
2. **轻核突破（Cavallaro 2019, INFN-LNS MAGNEX）**：
   长期以来，$(p, t)$ 反应在重核中未发现清晰的 GPV，物理本质源于轻离子转移中巨大的**运动学动量错配（$Q$-matching Discrepancy）**。2019 年在意大利卡塔尼亚，利用大立体角高分辨 MAGNEX 磁谱仪，通过重离子两中子转移反应 $^{12}\text{C}(^{18}\text{O}, {}^{16}\text{O})^{14}\text{C}$（$E_{\text{lab}} = 84\text{ MeV}$），由于重离子表面掠射库仑与核作用轨迹具有优异的角动量转移条件，首次在 $E_x \approx 20\text{ MeV}$ 清晰观测到耗尽巨大强度的中子巨对振动峰！

---

## 4. 原子核约瑟夫森效应（Nuclear Josephson Effect）

在超导凝聚态物理中，两个被绝缘势垒隔开的超导体之间会产生不依赖外加电压的宏观超导电流（DC Josephson Current）。

在低能重离子碰撞中，当两个处于超流态的重核（如 $^{120}\text{Sn} + {}^{112}\text{Sn}$ 或 $^{160}\text{Dy} + {}^{152}\text{Sm}$）在库仑势垒附近低能掠射时：
1. **核库珀对连续相干隧穿**：
   两核相互靠近形成瞬态微观接触颈缩，两核超流凝聚态波函数的规范相位差 $\Delta \phi = \phi_1 - \phi_2$ 驱动中子对从一个超流核向另一个超流核发生**共振宏观隧穿**；
2. **多中子对转移概率的指数增强**：
   若无超流关联，转移 $n$ 对中子的几率应为单对几率的乘积：$P_{2n} \propto (P_{1n})^2$；而在强超流配对驱动下，观测到 $P_{2n}$ 较非相干预言高出近两个数量级，直接证实了有限微观费米体系中**核约瑟夫森超流（Nuclear Josephson Supercurrent）**的存在！

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/two_nucleon_transfer_pairing_vibration_calculator.py` 中实现了完整的两核子转移与配对振动分析器：
1. **BCS 相干转移截面增强因子求解器**：输入费米面附近轨道占有几率 $u_j, v_j$，计算超流基态相干增强因子 $\sigma_{\text{BCS}} / \sigma_{\text{sp}}$；
2. **配对振动声子能量与双声子态预测器**：输入闭壳邻核结合能，计算对增加模 $\hbar\omega_+$、对去除模 $\hbar\omega_-$ 与组合双声子 $|1, 1\rangle$ 激发能；
3. **两核子转移运动学 $Q$ 匹配评估器**：计算转移反应的最佳反应能差 $Q_{\text{opt}}$ 与动量匹配条件，诊断 $(p, t)$ vs $(^{18}\text{O}, {}^{16}\text{O})$ 反应效率；
4. **核约瑟夫森多对隧穿增强检验器**：评估多对中子转移几率比，检验超流相干性。

---

## 6. 权威文献与理论溯源

1. **Bès, D. R. & Broglia, R. A.** (1966). Pairing vibrations. *Nucl. Phys.*, 80(2), 289-313.
2. **Bohr, A. & Mottelson, B. R.** (1975). *Nuclear Structure*, Vol. II, Chapter 6 (Pairing Vibrations). Benjamin, New York.
3. **Cavallaro, M. et al.** (2019). Giant pairing vibrations in light nuclei. *Nature Commun.*, 10, 167.
4. **von Oertzen, W. & Vitturi, A.** (2001). Pairing correlations of nucleons and multi-nucleon transfer between heavy nuclei. *Rep. Prog. Phys.*, 64(10), 1247.
5. **Bertulani, C. A. & Danielewicz, P.** (2004). *Introduction to Nuclear Reactions*, Chapter 6 (Direct reactions). CRC Press.
