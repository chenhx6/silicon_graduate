---
type: research-note
title: "奇奇核 Chiral-AMR 四叶片 3D-TAC 非共面拓扑分岔"
aliases: [chiral-amr-four-blade, 3d-tac-pitchfork, nonplanar-shears]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, clark-2000-shears-mechanism, he-chuangye-2006-magnetic-chiral-106ag]
created_from: "Day26 investigation of chiral-AMR four-blade 3D-TAC bifurcation"
tags: [magnetic-rotation, antimagnetic-rotation, chirality, 3D-TAC, four-blade, 106Ag, 106Cd]
---

# 奇奇核 Chiral-AMR 四叶片 3D-TAC 非共面拓扑分岔

## Research Trigger

本轮把已有的平面 MR/AMR 几何诊断扩展为一个最小四叶片 3D-TAC Routhian。目标是检验：两质子空穴与两中子粒子形成的镜像四叶片 AMR 构型，在中间轴推转分量的对称幅度驱动下，是否能从 $I_m=0$ 的平面极小分岔为 $I_m=\pm|I_m|$ 的两个非共面极小，并由此生成内禀几何手征序参量、带内 M1 的对称性解除以及伙伴带劈裂的代理量。

## Grounded Evidence

1. Frauendorf 2001 综述关于三维推转（3D-TAC）与手征离散对称性破缺分类；
2. 106Ag 实验上共存的磁转动与候选同宇称手征双带；
3. 106Cd 实验上作为平面四叶片反磁转动（AMR）的基准。

## Provisional Reasoning

本轮把已有的平面 MR/AMR 几何诊断扩展为一个最小四叶片 3D-TAC Routhian。目标是检验：两质子空穴与两中子粒子形成的镜像四叶片 AMR 构型，在中间轴推转分量的对称幅度驱动下，是否能从 (I_m=0) 的平面极小分岔为 (I_m=pm|I_m|) 的两个非共面极小，并由此生成内禀几何手征序参量、带内 M1 的对称性解除以及伙伴带劈裂的代理量。

模型是经典固定自旋球面上的几何诊断，不是自洽 TAC-HFB/PNC-CSM，也不把数值临界频率或代理跃迁率当作 (^{106}\mathrm{Ag}) 或 (^{106}\mathrm{Cd}) 的实测量。

### 过程记录

### 1. 微观自由度和 Routhian

体坐标取短轴、中间轴、长轴为 ((s,m,l))，净叶片向量写为

\[
 \mathbf j_p=(j_p,0,0),\qquad \mathbf j_n=(0,0,j_n),\qquad
 \mathbf R=\mathbf I-\mathbf j_p-\mathbf j_n .
\]

这里的两个净向量代表两枚镜像质子空穴和两枚镜像中子粒子之和。固定 (|\mathbf I|=I)，令

\[
 I_s=I\sin\theta\cos\phi,\quad I_m=I\sin\theta\sin\phi,
 \quad I_l=I\cos\theta .
\]

计算的 Routhian 为

\[
 \mathcal R=\sum_{k=s,m,l}\frac{(I_k-j_k)^2}{2\mathcal J_k}
 -\frac{\kappa_m\omega_m^2}{2I^2}I_m^2 .
\]

第二项是中间轴推转幅度的有效软化项。采用 (omega_m^2) 而不是带符号的线性 (-omega_m I_m)，是为了保留左右手 (I_m\leftrightarrow-I_m) 的离散等价性。带符号线性外场会选择单一手性，把 pitchfork 变成偏置 crossover。

示例参数为 (j_p=8)、(j_n=10)、((\mathcal J_s,\mathcal J_m,\mathcal J_l)=(10,18,14)\ \hbar^2/\mathrm{MeV})、(kappa_m=44)。扫描 (I=18,22,26,30\hbar)，(omega_m=0)–(0.80\ \mathrm{MeV}/\hbar)，角网格各 721 点。

### 分岔判据和跃迁网络

几何手征量为

\[
 \chi_g=\mathbf j_p\cdot(\mathbf j_n\times\mathbf R)
 =-j_pj_nI_m .
\]

平面 AMR 极小满足 (I_m=R_m=chi_g=0)。当固定 (	heta) 后的平面曲率

\[
 \kappa_\phi=\left.\frac{\partial^2\mathcal R}{\partial\phi^2}\right|_{\phi=0}
\]

由正变负，(phi=0) 变为鞍点，并出现两个等能极小 (phi=pmphi_0)。这就是经典 pitchfork 条件；有限自旋的伙伴带仍需角动量投影和左右波包隧穿。

理想 AMR 的两对镜像叶片使横向磁矩相消，平面分支采用 (B(M1)=0) 的几何基线。分岔后，复合对称 (TR_m(\pi)) 在内禀平均场中被破缺，允许与非平面序参量成正比的横向磁矩。工件使用

\[
 B(M1)_{\rm proxy}\propto (I_m/I)^2,
 \qquad B(E2)_{\rm proxy}=B(E2)_{\rm core}+B(E2)_{\rm blade}(1-q^2)^2,
 \quad q=|I_m|/I .
\]

伙伴劈裂代理按双阱势垒指数衰减。这些量没有实验单位，不能和 DSAM/RDDS 的绝对强度比较。

### 数值结果

工件目录为
`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/chiral-amr-3dtac/`。

在代表性 (I=22\hbar) 下，首个非平面网格点为 (omega_m=0.51\ \mathrm{MeV}/\hbar)：平面曲率为 (-0.1233\ \mathrm{MeV})，镜像极小位于 (phi=\pm20.5^\circ)，(|I_m|=4.392\hbar)，(|\chi_g|=351.33)（示例归一），(B(M1)) 代理为 0.03985，(B(E2)) 代理为 0.2628。左右分支的能量和 (|\chi_g|) 在网格精度内相同。

该临界值是示例参数的模型推断，不是任何核素的实测临界频率。CSV 保存完整扫描，JSON 保存方程和边界，SVG 保存 (|\phi|) 分岔图。

### 4. 106Ag 与 106Cd 对照

在 $^{106}\text{Ag}$ 中，实验上观测到磁转动能带与手征双重带候选共存，表明其具有非共面倾斜转动的倾向；而在偶偶核 $^{106}\text{Cd}$ 中，系统表现为典型的平面四叶片反磁转动（AMR）。两者的微观分歧在于奇核非对称准粒子激发打破了离散镜像对称性。

## Assumptions

- 假定核芯为三轴刚体，具有固定主轴惯量排序 $\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$；
- 假定四个叶片有效角动量矢量在转动中保持模长守恒；
- 假定中间轴推转幅度项为偶函数，保持镜像对称性。

## Competing Explanations

非共面手征分岔与平面剪刀重开、多准粒子非对称排列或大振幅手征振动均是候选解释；单一几何 Routhian 极小不代表有限核中静态手征双重态的确证。

## Transfer Conditions

适用于质子与中子同时占据高 $j$ 侵入轨道的奇奇核与四准粒子偶偶核（如 $A \approx 106$ 与 $A \approx 130$ 核区）；不适用于轴对称核。

## Failure Conditions

若中间轴转动惯量不满足 $\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$，或有效粒子-空穴相互作用抑制中轴倾斜，则非平面 pitchfork 分岔不会发生。

## Falsification or Reverse Tests

在候选核（如 $^{106}\text{Ag}$）中系统测量能级寿命，提取带内与带间 $B(M1)$、$B(E2)$ 跃迁强度的绝对值，检验手征伙伴对称性。

## Open Questions

- 在有限量子隧穿作用下，左右非共面极小的简并如何解除？
- 四叶片电荷分布的四极辐射张量在分岔点附近如何发生突变？

## Human Review

本笔记由自主研学模型计算生成，保持 unreviewed。

## Promotion or Rejection History

- 2026-10-29: 完成四叶片 3D-TAC 模型的 pitchfork 手征拓扑分岔与离散对称破缺微观推演。
