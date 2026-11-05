---
type: concept
title: "倾斜轴推转（TAC）、3D手征三面体几何与非共面手征体积度规动力学"
aliases: [倾斜轴推转, TAC, 手征三面体几何, 手征体积度规, 非共面性, 手征振动, 静态手征转动, 手征双重带, 角动量重整]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [tilted-axis-cranking, tac, nuclear-chirality, chiral-doublet-bands, aplanarity-metric, 3d-angular-momentum, spontaneous-symmetry-breaking, triaxiality]
---

# 倾斜轴推转（TAC）、3D手征三面体几何与非共面手征体积度规动力学

## Definition

### 物理全景：原子核自发手征对称性破缺的微观几何图像

在三维空间中，一个物体如果不能通过任何空间纯旋转操作与其镜像重合，该物体便具有手征性（Chirality，如人类的左右手）。
在微观原子核中，**原子核手征性（Nuclear Chirality）**是自发对称性破缺（Spontaneous Symmetry Breaking）中最优雅的量子现象之一。
根据 S. Frauendorf & J. Meng（Nucl. Phys. A 617, 131, 1997）、S. Frauendorf（Rev. Mod. Phys. 73, 463, 2001）以及 C. M. Petrache 2024《Chirality and Wobbling in Atomic Nuclei》：
在具有稳定三轴刚性形变（$\gamma \approx 30^\circ$）的原子核中（典型代表为 $A \approx 130$ 区的奇奇核 $^{128, 130}\text{Cs}, ^{132}\text{La}$ 与奇 $A$ 核 $^{133}\text{Ce}, ^{135}\text{Nd}$）：
1. **三维角动量正交三面体（3D Angular Momentum Trihedron）**：
   - 处于空壳底部的价质子粒子（如 $\pi h_{11/2}$）受形变势驱动，沿原子核**短轴（Short axis, $s$）**取向；
   - 处于满壳顶部的价中子空穴（如 $\nu h_{11/2}^{-1}$）沿原子核**长轴（Long axis, $l$）**取向；
   - 三轴核心的转动惯量在中轴达到最大值（$\mathcal{J}_m > \mathcal{J}_s > \mathcal{J}_l$），驱动核心集体转动矢量 $\mathbf{R}$ 沿**中轴（Intermediate axis, $m$）**取向！
2. **非共面性（Aplanarity）与动标架手征性**：
   这三个相互垂直的角动量分量合成总自旋 $\mathbf{I} = \mathbf{j}_p + \mathbf{j}_n + \mathbf{R}$，**该矢量严格偏离核的三个主对称平面（$s-m, m-l, s-l$ 平面）**，指向第一卦限！
   将时间反演操作 $\mathcal{T}$ 与绕主轴转动 $180^\circ$ 的空间旋转 $\mathcal{R}_k(\pi)$ 复合，在内禀参考系中构成了左手（Left-handed）与右手（Right-handed）两种互为镜像、能量退化的旋转手性态！
3. **量子化投影与实验室系手征双重带（Chiral Doublet Bands）**：
   在实验室系中，恢复自洽宇称导致左手态与右手态发生宏观量子简并，形成一对**自旋相同、宇称相同、能量高度简并、转动惯量极为相近且具有近乎相同电磁跃迁特征的双重带（Twin Bands）**。

---

## Necessary Assumptions

### 严格 3D TAC 几何代数推演与度规

### (1) 倾斜轴推转（TAC）哈密顿量
在旋转内禀参考系中，推转哈密顿量为：
$$H_{\text{TAC}} = H_{\text{def}} - \vec{\omega} \cdot \vec{J} = H_{\text{def}} - (\omega_s J_s + \omega_m J_m + \omega_l J_l)$$
其中旋转角速度矢量 $\vec{\omega} = (\omega_s, \omega_m, \omega_l)$ 指向任意三维空间取向，极角与方位角定义为：
$$\omega_s = \omega \sin\theta_{\text{tilt}} \cos\phi_{\text{tilt}}, \quad \omega_m = \omega \sin\theta_{\text{tilt}} \sin\phi_{\text{tilt}}, \quad \omega_l = \omega \cos\theta_{\text{tilt}}$$

---

### (2) 空间手征非共面体积度规（Aplanarity Volume Metric, $\mathcal{V}_{\text{chiral}}$）
定义由质子角动量 $\mathbf{j}_p$、中子角动量 $\mathbf{j}_n$ 与核心转动 $\mathbf{R}$ 构成的混合三重标量积：
$$\chi = \mathbf{j}_p \cdot (\mathbf{R} \times \mathbf{j}_n)$$
定义无量纲归一化的 **非共面手征体积度规（Chiral Volume Metric, $\mathcal{V}_{\text{chiral}}$）**：
$$\mathcal{V}_{\text{chiral}} = \frac{|\mathbf{j}_p \cdot (\mathbf{R} \times \mathbf{j}_n)|}{|\mathbf{j}_p| \cdot |\mathbf{R}| \cdot |\mathbf{j}_n|} \in [0, 1]$$

#### 极限性质：
- 若 $\mathcal{V}_{\text{chiral}} = 0$：三个矢量必然共面（Coplanar），混合标量积严格为零，时间反演-旋转复合对称性未破缺，**手征性严格禁戒**！
- 若 $\mathcal{V}_{\text{chiral}} \ge 0.40$：三个矢量强烈非共面张开，构成坚固的三维空间手征三面体。

---

### (3) 手征相变的自旋演化三阶段
随着总角动量 $I$ 从带头向极高自旋演化，原子核经历三大动力学相变区间：
1. **手征振动区（Chiral Vibration, 低自旋区，典型 $I \sim 9 \sim 11\hbar$）**：
   此时核心转动分量 $|\mathbf{R}|$ 较小，左手态与右手态之间的平面分离势垒较低，系统通过量子穿透发生剧烈隧道振荡，表现为简谐手征振动。实验特征：双重带之间的能量差较大（$\Delta E(I) = E_2(I) - E_1(I) \sim 150 \sim 300\text{ keV}$）；
2. **静态手征转动区（Static Chiral Rotation, 中高自旋区，典型 $I \sim 12 \sim 16\hbar$）**：
   $|\mathbf{R}|$ 达到 $6 \sim 10\hbar$，三面体非共面度达到极大（$\mathcal{V}_{\text{chiral}} \to 1.0$），势垒极其深邃，量子隧穿几率指数衰减。双重带能量差趋于严格简并：
   $$\Delta E(I) \to 0\text{ keV} \quad (\text{通常 } < 50\text{ keV})$$
   自发手征对称性完全破缺，这是手征双重带的最辉煌特征！
3. **哥氏平面重整区（Coriolis Planar Restoration, 极高自旋区，典型 $I > 18\hbar$）**：
   在巨大的离心与哥氏力扭矩作用下，价核子角动量 $\mathbf{j}_p$ 与 $\mathbf{j}_n$ 最终被强行对齐到转动惯量最大的中轴 $m$ 方向，非共面体积坍缩为零（$\mathcal{V}_{\text{chiral}} \to 0$），手征结构解体，转为普通的平面推转对齐带。

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 手征双重带的实验排他性判据（Four-Point Criteria）

为防止将普通的形状共存带或准粒子交叉带误报为手征带，Petrache 2024 与 Frauendorf 确立了刚性四道门准则：

| 检验准则 | 手征双重带（Chiral Doublet）要求 | 竞争机制假象（Shape Coexistence / Crossing） |
| :--- | :--- | :--- |
| **能量简并度 $\Delta E(I)$** | 在静态区出现能级靠拢平台，$\Delta E \le 60\text{ keV}$ | 能带持续发散或仅在带交叉点出现单点相交 |
| **$B(M1)$ 跃迁交错对称律** | **带内 $B(M1)$ 与带间 $B(M1)$ 大小几乎相等**：$B(M1)_{\text{in}} \approx B(M1)_{\text{out}}$ | 带间跃迁受到剧烈阻尼，$B(M1)_{\text{out}} \ll B(M1)_{\text{in}}$ |
| **孪生带核心 $B(E2)$ 恒同性** | 两带的内带 $B(E2)$ 几乎完全相等（共享相同三轴椭球） | 结构不同的能带具有明显不同的电四极矩与 $B(E2)$ |
| **转动惯量 $\mathcal{J}^{(1)}, \mathcal{J}^{(2)}$ 镜像重合** | 运动学与动力学转动惯量随自旋演化轨迹高度镜像重合 | 表现出迥异的角动量对齐和回弯轨迹 |

---

## 4. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/chiral_geometry_tac_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `chiral` 命令。

### 运行示范（以经典手征核 $^{128}\text{Cs}$ 为例）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py chiral \
  --jp 5.5 --jn 5.5 --Rm 8.0 --delta-e-keV 42.0 \
  --bm1-ratio 1.15 --be2-ratio 1.08 --json
```

### 计算输出核心物理特征：
1. **三维角动量几何构型**：
   - 质子 $j_p = 5.5\hbar$（指向短轴），中子 $j_n = 5.5\hbar$（指向长轴），核心 $R_m = 8.03\hbar$（指向中轴）；
   - 合成总自旋 $|\mathbf{I}| = 11.66\hbar$，倾角 $\theta_{\text{tilt}} = 59.0^\circ, \phi_{\text{tilt}} = 53.1^\circ$，极其完美地指向第一卦限中心；
2. **手征体积度规**：
   - 标量积 $\chi = 242.0$，归一化手征体积度规高达 $\mathcal{V}_{\text{chiral}} = 0.996 \approx 1.0$；
   - 确立处于 `Static_Chiral_Rotation` 静态手征转动区；
3. **四道门全绿仲裁（4/4 PASS）**：
   - 能级简并度 $\Delta E = 42\text{ keV} \le 60\text{ keV}$；
   - $B(M1)_{\text{in}}/B(M1)_{\text{out}} = 1.15 \approx 1$；
   - $B(E2)$ 孪生一致度达 $1.08 \approx 1$；
   - **条件性结论：`conditional-chiral-doublet-screening-pass`**。该输出是
     caller-supplied 参数下的几何/能谱 screening，不能替代带有寿命、偏振、
     响应和竞争模型的实验手征判定。

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用

- [[davydov-filippov-triaxial-rotor-and-wobbling-dynamics]]：手征双重带（三主轴皆有分量）与摆动运动（围绕单主轴进动）共同构成三轴核的两大奇迹；
- [[tdpad-hyperfine-precession-and-gfactor-dynamics]]：TDPAD 三矢量磁矩测量可直接通过 $g$ 因子检验手征矢量的三维取向；
- [[triaxial-projected-shell-model-microscopic-dynamics]]：微观 TPSM 能直接从多准粒子基底中投影出手征双重带的波函数对称性。
