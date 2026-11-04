---
type: method
title: "Qi：A≈80 质量区核手征岛、手征-反射对称性联合破缺与手征摆子合同"
aliases: [Qi A~80 nuclear chirality, A~80 chiral island, Br-Rb triaxial RMF, chiral octupole quartet, 74Br chiral wobbler]
method_type: "a80-chiral-systematics-and-multimodal-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Chirality and Wobbling in Atomic Nuclei Ch.15, PDF pp.302-310, full chapter reading"
confidence: "high for RMF calculations, reported experimental data, and published PRL/PLB discovery references"
tags: [a80-region, nuclear-chirality, rmf-triaxial, pk1, 74br, 76br, 78br, 80br, 82br, 84rb, 74as, 81kr, chiral-wobbler, octupole-correlation]
sources: [book-petrache-chirality-and-wobbling]
---

# Qi：A≈80 质量区核手征岛、手征-反射对称性联合破缺与手征摆子合同

## Purpose

本方法合同基于亓斌（山东大学威海分校）在专著《Chirality and Wobbling in Atomic Nuclei》第 15 章的系统研究，
解决低能核结构中手征几何在轻质量区（\(A\a80\)）的存在边界、微观构型依赖性以及手征性与反射对称破缺、集体摆动运动共存竞争的理论难题：
通过组态固定约束三轴相对论平均场（RMF）微观计算与在束 \(\gamma\) 谱学（AFRODITE 多叶 Clover 极化阵列、CIAE 阵列）实验系统测量的紧密结合，
全面确立核素图谱上最轻手征岛的微观起源与前沿交叉模式合同：

1. **\(A\a80\) 质量区手征岛边界与中子费米面演化定律**：在 Br（\(Z=35\)）与 Rb（\(Z=37\)）同位素链中，微观证明随着中子数 \(N\) 从 39 增加到 47，中子费米面由 \(g_{9/2}\) 亚壳底部向顶部移动，空穴性质逐渐理想化，手征几何对称性逐步稳定，伴随带实验能隙 \(\Delta E(I)\) 呈现单调收缩；将手征岛边界拓展至 \(Z=33\)（\(^{74}\mathrm{As}\)）与 \(Z=37\)（\(^{84}\mathrm{Rb}\)）；
2. **奇奇核与奇 \(A\) 核手征构型多样性**：不仅在奇奇核建立正宇称 \(\pi g_{9/2} \otimes \nu g_{9/2}\) 与负宇称 \(\pi(p_{3/2}, f_{5/2}) \otimes \nu g_{9/2}\) 手征带，更在奇 \(A\) 核 \(^{81}\mathrm{Kr}\) 中确立 \(\pi g_{9/2}^2 \otimes \nu g_{9/2}^{-1}\) 与 \(\pi g_{9/2}(p_{3/2}, f_{5/2}) \otimes \nu g_{9/2}^{-1}\) 两对手征双重带；
3. **手征–反射双重对称性联合破缺（Chiral-Parity Quartets）**：在 \(^{78}\mathrm{Br}\)（PRL 2016）与 \(^{76}\mathrm{Br}\)（PLB 2022）中实验确证手征双重带与八极反射不对称性关联共存，建立 8 条强 \(E1\) 跨带连接跃迁与严格同宇称四重带微观图像，阐明反射对称破缺不仅不破坏手征性，反而“催化”稳定了三轴非共面旋转；
4. **首例手征摆子（Chiral Wobbler）微观发现**：在 \(^{74}\mathrm{Br}\)（PRL 2024）中首次实验发现兼具手征对称性自发破缺与非轴对称转动横向摆动运动的新激发态，证实原子核手征几何对大振幅非简谐摆动激发具有强鲁棒性。

---

## Inputs and Assumptions

### 1. 约束三轴相对论平均场理论（Triaxial RMF）

采用标准非线性介子–核子有效相对论拉格朗日密度泛函（PK1 参数集），在无海（No-sea）近似下建立核子狄拉克方程（式 15.1–15.3）：
\[
\left\{ \vec\alpha \cdot [\vec p - \vec V(\vec r)] + \beta m^*(\vec r) + V_0(\vec r) \right\} \psi_i(\vec r) = \varepsilon_i \psi_i(\vec r)
\]
狄拉克旋量基底在三维笛卡尔谐振子基中展开（费米子 12 个主壳层，介子场 10 个主壳层）。由于奇奇核强泡利阻塞效应，准粒子配对关联在此处予以忽略。

### 2. 绝热约束与组态固定约束（Configuration-Fixed Constraining）

- **绝热约束计算（Adiabatic Constraint）**：核子始终填充能量最低的单粒子能级，用于描绘全局基态势能面谷底；
- **组态固定约束计算（Configuration-Fixed Constraint）**：在拉伸四极形变 \(\beta^2 = \langle\hat Q_{20}\rangle^2 + 2\langle\hat Q_{22}\rangle^2\) 过程中，严格锁定非配对质子与中子占据特定的单粒子轨道量子数组合，从而追踪极小能量亚稳三轴态（如态 A–I）的形变演化 \((\beta, \gamma)\) 与微观结合能 \(E_{\rm tot}\)。

---

## What It Can Establish

### 1. 溴同位素链（\(^{74,76,78,80,82,84}\mathrm{Br}\)）手征理论与实验图谱（表 15.1、图 15.1、图 15.3）

- **\(^{74}\mathrm{Br}\)**：理论预言态 D（\(\beta=0.43, \gamma=23.2^\circ, \pi g_{9/2} \otimes \nu f_{5/2}^{-1}\)）与态 H（\(\beta=0.45, \gamma=27.5^\circ, \pi g_{9/2} \otimes \nu g_{9/2}^{-1}\)）具有适宜三轴形变；实验观察到两对手征带，并在其上确立首个手征摆动激发态（Chiral Wobbler, PRL 2024）；
- **\(^{76}\mathrm{Br}\)**：理论预言态 B（\(\beta=0.41, \gamma=20.8^\circ, \pi g_{9/2} \otimes \nu g_{9/2}^{-1}\)）与态 E（\(\beta=0.36, \gamma=32.0^\circ, \pi g_{9/2} \otimes \nu p_{3/2}\)）；实验不仅观测到手征双带，还测定了精确能级寿命，证实手征与八极共存；
- **\(^{78}\mathrm{Br}\)**：理论预言态 F（\(\beta=0.21, \gamma=30.2^\circ, \pi f_{5/2} \otimes \nu g_{9/2}^{-1}\)）与态 H（\(\beta=0.35, \gamma=21.4^\circ, \pi g_{9/2} \otimes \nu g_{9/2}^{-1}\)）；实验测量确立正负宇称两对双重带及 8 条强 \(E1\) 跃迁，确证手征–反射对称性同时破缺；
- **\(^{80}\mathrm{Br}\)**：理论预言态 E（\(\beta=0.34, \gamma=25.2^\circ, \pi g_{9/2} \otimes \nu g_{9/2}^{-1}\)）；实验由 Wang 等（PLB 2011）首次在 \(A\a80\) 发现正宇称手征双带；
- **\(^{82}\mathrm{Br}\)**：理论预言态 H 与 I 具有稳定三轴度；实验成功测得手征双重带（PRC 2019）；
- **中子数演化动力学规律**：随着中子数 \(N\) 上升，\(\Delta E(I)\) 从 \(^{74}\mathrm{Br}\) 的 \(\sim 0.6\) MeV 稳步下降到 \(^{82}\mathrm{Br}\) 的 \(< 0.2\) MeV，在带能级交错参量 \(S(I) \approx 25\text{ keV}/\hbar\) 维持平滑，微观证明中子空穴纯度提高极大增强了手征三脚架的刚性稳定性。

### 2. 铷同位素链（\(^{76,78,80,82,84,86}\mathrm{Rb}\)）多重手征态预言与 \(^{84}\mathrm{Rb}\) 实验确证（图 15.2、15.3）

- **\(^{78}\mathrm{Rb}\) 与 \(^{80}\mathrm{Rb}\) 的新型多重手征带（M\(\chi\)D）**：RMF 预言同一核内存在两组基于相同 \(\pi g_{9/2} \otimes \nu g_{9/2}^{-1}\) 但价轨道不同的三轴极小（态 B 与 I），预言由两套正宇称手征双带与一套负宇称手征双带组合构成的新型 M\(\chi\)D；
- **\(^{82}\mathrm{Rb}\)**：理论计算表明中子费米面高度贴近 \(g_{9/2}\) 顶端，具有最低激发能和最稳定三轴度（\(\gamma \sim 37^\circ\)–\(45^\circ\)），为最佳理论手征候选核；
- **\(^{84}\mathrm{Rb}\)**：CIAE 实验首次观测到基态正宇称手征双重带，将 \(A\a80\) 岛屿的电荷边界拓展至 \(Z=37\)。

### 3. \(^{81}\mathrm{Kr}\) 奇 \(A\) 核手征性突破

打破手征双重带仅局限于奇奇核的旧认知，在奇 \(A\) 核 \(^{81}\mathrm{Kr}\) 中通过三准粒子组态 \(\pi g_{9/2}^2 \otimes \nu g_{9/2}^{-1}\)（正宇称）与 \(\pi g_{9/2}(p_{3/2}, f_{5/2}) \otimes \nu g_{9/2}^{-1}\)（负宇称）成功观测到两对高品质手征双重带，具有高度相似的动力学转动惯量与带内 \(B(M1)/B(E2)\) 奇偶交错同相性。

### 4. 手征–宇称联合破缺与手征摆子新范式

1. **八极关联催化手征对称破缺机制**：
   在 \(^{78}\mathrm{Br}\) 与 \(^{76}\mathrm{Br}\) 中，反射非对称梨形形变不仅未使立体非共面转动失稳，反而通过降低核芯轴对称自由能势垒，促进了核芯绕中轴的稳定转动，使手征简并能隙显著缩窄；
2. **手征摆子（Chiral Wobbler）共存图像**：
   \(^{74}\mathrm{Br}\) 实验证实原子核即使在经历出平面的手征取向时，依然能够承受横向主轴的大振幅简谐/非简谐摆动激发，为角动量在三维空间的非线性进动提供了极端丰富的动力学样板。

---

## What It Cannot Establish Alone

1. **平均场框架不能直接输出量子手征双重带能级裂距**：
   约束三轴 RMF 给出内禀平均场极小与自发破缺手征取向，无法直接计算恢复时间反演–转动对称性后左右手势阱间的大振幅隧穿裂距 \(\Delta E(I)\)，必须结合三维 TAC推转、粒子–转子模型（PRM）或 TPSM 投影壳模型；
2. **不能排除同核素内微观配对涨落对三轴形变软度的平滑效应**：
   计算中忽略了奇奇核与奇 \(A\) 核的动态配对涨落，在低自旋与激发态相变边界处，真实的能量势能面可能表现出显著的 \(\gamma\) 软度或形状共存；
3. **\(^{82}\mathrm{Rb}\) 理论最优手征核尚未被实验完全证实**：
   尽管理论能面显示 \(^{82}\mathrm{Rb}\) 条件最为理想，但受限于束流靶反应道截面与高自旋退激分支，目前实验上完整的双重孪生能带尚未最终建库闭环。

---

## Sources

- [[book-petrache-chirality-and-wobbling]]：B. Qi, Ch. 15 *Studies of nuclear Chirality in A≈80 mass region*, in C. M. Petrache (Ed.), *Chirality and Wobbling in Atomic Nuclei*, CRC Press (2025), pp. 302–310.
- [[global-chiral-doublet-bands-systematics-atlas]]：手征双重带全球四大质量区图谱与同位素链演化系统学。
- [[chiral-octupole-dual-symmetry-breaking-quartet-bands]]：手征–八极双重对称破缺四重能带与强 E1 跃迁动力学。
- [[multiple-chiral-doublets-and-chiral-parity-quartets]]：多重手征双重带与手征–宇称四重带微观机制。
