---
type: research-note
title: "反磁转动中核芯四极驱动与四叶片非谐剪刀力矩"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [amr-core-quadrupole-drive-and-shears-torque, AMR core quadrupole drive, four-blade non-harmonic shears torque]
tags: [antimagnetic-rotation, core-polarization, shears-torque, quadrupole-deformation, cadmium110]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 AMR core quadrupole drive and non-harmonic shears torque study"
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-first-page, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
---

# 反磁转动中核芯四极驱动与四叶片非谐剪刀力矩

## Research Trigger

本轮任务检验一个可计算的机制链：在偶偶 Cd/Pd 反磁转动中，四叶片剪刀闭合、核芯四极极化和核芯转动惯量是否能够在同一个两自由度能量中相互反馈，并形成非谐的剪刀回复/闭合力矩。题目给出的“离心力必然把 $β_2$ 从 0.11 拉到 0.15”以及“实验 $B(E2)$ 可以精确分成剪刀和核芯份额”需要降格为模型假设或可证伪推断；现有来源并未提供这样的模型无关证明。

本笔记采用固定总自旋 $I$ 的实验室系能量极小化。极小化后用共轭关系得到 $ω$，这样 $β_2$ 依赖的 $ℐ_{core}$ 会在固定 $I$ 下真实改变剪刀所需提供的残余角动量。可复现代码和数据在 `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-core-drive/`。

## Grounded Evidence

### 直接实验与来源边界

Roy et al. 2011 的本地原件知识页记录：110Cd 16+–24+ 的平均寿命为 0.36(3)、0.23(3)、0.17(3)、0.21(7)、0.27(7) ps，对应带内 $B(E2)$ 为 0.14(1)、0.12(2)、0.11(2)、0.09(3)、0.06(2) $e^2b^2$（PDF p.324, Table 1；[[roy-2011-cd110-systematics-antimagnetic]], RO11-1）。1323 与 1314 keV 线之间的负有限差分必须保留，不能无提示地把 $J^{(2)}=4/Delta E_gamma$ 当成正常正值（同源页 RO11-D26C-003）。

同一论文的作者模型把 110Cd 表述为双剪刀与核芯集体转动耦合，并采用 $ℐ_m=19.5\ \hbar^2/\mathrm{MeV}$；这是粒子加转子模型输入/解释，不是独立测得的 $β_2$ 或核芯四极矩（PDF pp.325–326；RO11-2, RO11-3）。$V_{πν}\approx1.2$ MeV 和 $V_{ππ}\approx0$–0.2 MeV 也是唯象参数，未包含三维微观自洽形变涨落。

Rather et al. 2014 的本地材料实际只有期刊第一页。该页直接给出对称两刃几何 $I_\mathrm{sh}=j_p+2j_h\cos\theta$、横向磁矩相消和 $B(E2)=15(eQ_\mathrm{eff})^2\sin^4\theta/(32\pi)$ 的条件模型（[[rather-2014-104pd-antimagnetic-first-page]], RA14-EX-01）；其摘要说明通过 DSAM 研究 104Pd 高自旋 yrast E2 强度。后四页未取得，因此本文不把 104Pd 的逐点寿命、核芯惯量或表格强度当作已核验原始证据。

Frauendorf 2001 的综述将 AMR 归入高-$j$ 电流回路的反磁排列，强调双剪刀横向磁矩相消、弱 E2 和较大的 $J^{(2)}/B(E2)$；它同时提醒 TAC/平均场方向不是实验室观测量，量子恢复与集体涨落需要单独处理（[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]], PDF pp.487–488, 499–505）。

### 两自由度模型

为避免把 Routhian 的固定-$\omega$ 极小误当成固定-$I$ 的反馈，本轮使用

$$
 E(\theta,\beta;I)=V_s\cos^2\theta+\frac12C(\beta-\beta_0)^2+
 \frac{[I-I_\mathrm{qp}(\theta)]^2}{2\mathcal J_\mathrm{core}(\beta)},
$$

$$
 I_\mathrm{qp}=j_p+2j_h\cos\theta,
 \qquad \mathcal J_\mathrm{core}=\mathcal J_0+\mathcal J'_\beta(\beta-\beta_0).
$$

这里 $θ=0$ 表示四叶片闭合，$θ=\pi/2$ 表示开放；$V_s\cos^2\theta$ 是使无转动极限偏向开放、而固定总角动量项推动闭合的最小剪刀势。代码的 110Cd-like 基线为 $β_0=0.11$、$C=700$、$ℐ_0=8$、$ℐ'_\beta=120$、$V_s=5$ MeV、$j_h=5.5\ \hbar$、$j_p=8\ \hbar$。

对 $β$ 求导得到

$$
 \frac{\partial E}{\partial\beta}=C(\beta-\beta_0)-\frac12\omega^2\mathcal J'_\beta=0,
 \qquad
 \beta_*(\omega)=\beta_0+\frac{\mathcal J'_\beta}{2C}\omega^2.
$$

因此模型中的四极驱动力为

$$
 F_\mathrm{quad}=-\frac{\partial E}{\partial\beta}
 =-C(\beta-\beta_0)+\frac12\mathcal J'_\beta\omega^2.
$$

在极小点总力为零；所谓“驱动”是旋转项 $+\mathcal J'_\beta\omega^2/2$ 与弹性回复力的竞争，不能把它写成净力仍非零的静态自发加速。若 $ℐ'_\beta>0$，有限角速度会使 $β$ 增大，但这个结论依赖 $ℐ(\beta)$ 的正斜率和谐近似。

### 非谐剪刀力矩与反作用

由 $V_\mathrm{shears}=V_s\cos^2\theta$，

$$
 \tau_\mathrm{shears}=-\frac{\partial V_\mathrm{shears}}{\partial\theta}
 =V_s\sin(2\theta).
$$

这是非谐力矩：它不是小角度下全程线性的 $\kappa\theta$，并在 $\theta=0$ 和 $\pi/2$ 处退化。固定 $I$ 时闭合项为

$$
 \tau_\mathrm{close}=2j_h\omega\sin\theta,
 \qquad \tau_\mathrm{shears}=\tau_\mathrm{close}
$$

（内部符号约定相反时，两项的代数和为零）。$β$ 增大使 $ℐ_\mathrm{core}$ 增大，于是同一个 $I-I_\mathrm{qp}$ 对应更小的 $ω$ 和更小的闭合力矩。代码以

$$
 \tau_\mathrm{retarding}=2j_h\sin\theta(I-I_\mathrm{qp})
 \left(\frac1{\mathcal J_0}-\frac1{\mathcal J_\mathrm{core}(\beta)}\right)
$$

量化这一固定-$I$ 反作用；它是模型派生量，不是直接测得的 torque。

### $B(E2)$ 平台与数值分解

若把四叶片横向电四极张量和核芯集体张量写成同一约化振幅的相干和，则

$$
 B(E2;I\to I-2)=\frac5{16\pi}
 \left[Q_\mathrm{shears}\sin^2\theta+Q_\mathrm{core}(\beta)\right]^2.
$$

该式需要固定归一化、相位和有效电荷；它不是由一条寿命数据自动推出的实验恒等式。脚本将 $\sqrt{5/(16\pi)}$ 吸收到有效振幅中，故 CSV 的 `B_E2_total` 仍以 $e^2b^2$ 报告。`B_E2_shears_only` 与 `B_E2_core_only` 是去掉交叉项后的条件平方项，交叉项仍必须单独报告。

在 110Cd-like 基线的固定-$I$ 极小中，最接近 16+、18+、20+、22+、24+ 的五点如下。实验列来自 Roy Table 1；模型列不是拟合后的实验分解。

| $I$ | $\omega$ (MeV) | $\theta$ (deg) | $\beta_2$ | 模型 $B(E2)$ | 剪刀平方项 | 核芯平方项 | 交叉项 | Roy 实验 $B(E2)$ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 16 | 0.372 | 65.86 | 0.1218 | 0.1185 | 0.0494 (41.7%) | 0.0148 (12.5%) | 0.0542 (45.7%) | 0.14(1) |
| 18 | 0.451 | 60.28 | 0.1274 | 0.1081 | 0.0406 (37.5%) | 0.0162 (15.0%) | 0.0513 (47.5%) | 0.12(2) |
| 20 | 0.524 | 54.84 | 0.1335 | 0.0973 | 0.0318 (32.7%) | 0.0178 (18.3%) | 0.0476 (49.0%) | 0.11(2) |
| 22 | 0.591 | 49.46 | 0.1399 | 0.0865 | 0.0238 (27.5%) | 0.0196 (22.6%) | 0.0432 (49.9%) | 0.09(3) |
| 24 | 0.653 | 44.06 | 0.1466 | 0.0760 | 0.0167 (21.9%) | 0.0215 (28.3%) | 0.0378 (49.8%) | 0.06(2) |

该条件模型给出 $β_2=0.1133\to0.1534$、$B(E2)=0.1354\to0.0660\ e^2b^2$ 的端点尺度，且高自旋时 $\tau_\mathrm{retarding}$ 增大。它再现“缓降”的形状和量级，但没有证明实验的每个 $B(E2)$ 都可由这两个平方项唯一分解。模型的 $J^{(2)}/B(E2)$ 在中高自旋点约为 $206$、$244$、$293$、$357$、$438\ \hbar^2\mathrm{MeV}^{-1}(e^2b^2)^{-1}$；该比值对频率差分和带交叉敏感，不能作为单一排他阈值。

## Provisional Reasoning

1. 在此模型中，核芯四极“驱动”来自旋转自由能对 $ℐ_\mathrm{core}(\beta)$ 的二阶响应，严格结果是 $β-\beta_0\propto\omega^2/C$。这支持一个机制层面的离心极化图像，但不等同于微观 HFB 自洽的静态形变证明。
2. 四叶片剪刀力矩的 $\sin(2\theta)$ 形式给出非谐回复行为；核芯惯量增大通过固定-$I$ 约束降低 $\omega$，从而降低准粒子闭合力矩。这是“非谐反作用”的可检验代理定义。
3. 110Cd 实验端点从 0.14(1) 降至 0.06(2) 与该基线计算的 0.135→0.066 同量级，但约化振幅中的交叉项约占总强度 46%–50%，故不能把端点 0.06 直接标成“核芯贡献”。
4. 106,108Cd 与 102,104Pd 可共享结构方程和对称性，但 $ℐ_0$、$C$、组态、有效电荷和 $β_0$ 必须逐核重定；来源没有支持“同一套参数普适”。

## Assumptions

- 双剪刀等长、等权且用一个公共角 $θ$ 表示；三轴、叶片不等权和组态混合被压缩掉。
- $\mathcal J_\mathrm{core}$ 对 $β$ 在线性范围内增加，核芯恢复能在 $β_0$ 附近为谐振子势。
- $I_\mathrm{qp}=j_p+2j_h\cosθ$，未显式加入配对塌缩、带交叉和阻塞变化。
- $Q_\mathrm{shears}$ 与 $Q_\mathrm{core}$ 是约化有效振幅；相位取同号只是基线选择。
- 代码采用固定-$I$ 极小后反演共轭 $ω$，不是固定频率 cranked HFB，也没有角动量投影。

## Competing Explanations

有限端点 $B(E2)$ 还可以来自频率依赖的平均场形变、有效电荷变化、配对/占据重排、带交叉、side feeding 误差和多个电四极振幅的干涉。Roy 论文自己的核芯转动解释是经典粒子加转子模型结果；Frauendorf 综述提醒平均场方向需要实验室系恢复。若采用纯剪刀角因子而固定核芯形变，可能也能产生部分缓降；若采用弱集体转动，亦可产生残余 E2，但需同时对照 $J^{(2)}$、$B(M1)$、静态四极矩和组态演化。

## Transfer Conditions

可迁移的是：在等价双刃极限下，横向磁矩相消、$B(E2)_\mathrm{shears}\propto\sin^4\theta$、固定-$I$ 角动量预算以及 $ω$ 共轭关系。不可直接迁移的是本页的 $C=700$、$ℐ'_\beta=120$、$β_0=0.11$、$Q_\mathrm{shears}=0.267$ 和 110Cd-like 的端点数值。奇 A、不同空穴数、显著三轴性或强带交叉均需重新建模。

## Failure Conditions

若 $ℐ'_\beta\le0$，模型不会给出旋转诱导的 $β$ 增长；若 $C$ 太小，线性惯量会越界或能量面失稳。若 $Q_\mathrm{shears}$ 和 $Q_\mathrm{core}$ 的相位不明，平方项比例不是可识别量。若 $θ$ 不再是单公共角，$\sin^4\theta$ 也不应原样套用。固定-$I$ 代理忽略了真实推转态的量子投影，因此不能代替微观 TAC/HFB。

## Falsification or Reverse Tests

1. 令 $\mathcal J'_\beta=0$：应得到 $β=\beta_0$ 且 `tau_retarding=0`；若仍有反作用，说明代码混入了未声明的耦合。
2. 令 $C\to\infty$：$β$ 应冻结在 $β_0$，$B(E2)$ 平台只剩固定核芯振幅和剪刀干涉。
3. 改变 $Q_\mathrm{core}$ 的符号：若端点强度大幅改变而轨迹不变，说明“份额”受相位控制，不能由 B(E2) 单独反演。
4. 令 $V_s\to0$ 和 $V_s\to\infty$：分别检查剪刀角是否失去恢复约束、以及轨迹是否趋向开放/闭合极限。
5. 用 Roy 的 1323→1314 keV 原始相邻能量计算 $J^{(2)}$，必须保留负有限差分；删除该点后才出现的单调巨比值不能算独立验证。

## Open Questions

- 能否取得 110Cd DSAM 的逐门计数、阻止本领和 feeding 协方差，以判断端点 $B(E2)$ 的误差是否允许检验这个幅度模型？
- 能否取得 Rather 2014 104Pd 的完整正文并核对逐点表、$ℐ_\mathrm{core}$ 和形变输入？
- 在同一个带投影 HFB/PNC-CSM 框架中，能否同时计算 $β_2(\omega)$、$ℐ^{(2)}$、$B(E2)$ 和跨带 $B(M1)$？
- 独立静态四极矩或低自旋 E2 数据能否区分“核芯直接提供振幅”和“核芯惯量延缓剪刀闭合”？
- 106,108Cd 和 102,104Pd 的参数后验是否显示共同的 $ℐ'_\beta/C$ 标度，还是每个核需要独立的极化响应？

## Human Review

尚未进行人工审核；`review_status: unreviewed`。Roy 数值、Rather 第一页模型定义和 Frauendorf 综述边界均为本地来源页的 Codex self-audit；模型参数、端点分解、力矩和反作用均为本轮 provisional 推断，不能写成 `human-reviewed`。

## Promotion or Rejection History

2026-10-29：新建。采纳固定-$I$ 两自由度能量、$F_\mathrm{quad}$ 的变分推导、非谐 $\sin(2\theta)$ 剪刀力矩、$ℐ_\mathrm{core}$ 增长导致的固定-$I$ retarding diagnostic，以及 110Cd-like 的可复现扫描。拒绝把“离心力必然产生静态形变”“B(E2) 端点可被实验精确分项”“Rather 2014 全部逐点表已核验”写成直接事实。
