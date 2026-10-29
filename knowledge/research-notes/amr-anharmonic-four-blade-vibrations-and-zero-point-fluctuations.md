---
type: research-note
title: "AMR 四叶片非简谐角振动与零点量子涨落"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [AMR four-blade anharmonic phonons, AMR zero-point angular fluctuations, 反磁转动四叶片声子]
created_from: "Day26 doctoral research task: anharmonic four-blade AMR phonon expansion"
evidence_sources: [amr-microscopic-quadrupole-shears-restoring-constant, amr-coulomb-repulsion-proton-blades-and-closing-asymmetry, amr-double-shears-core-coupling-and-b-e2-plateau, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
tags: [antimagnetic-rotation, AMR, four-blade, anharmonicity, phonon, zero-point-fluctuation, E2, 110Cd, 104Pd]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
promotion_target: amr-quantum-shears-dynamics
---

# AMR 四叶片非简谐角振动与零点量子涨落

## Research Trigger

已有 AMR 笔记给出四叶片等权粒子—空穴几何的局部恢复常数 `C_AMR`，并指出理想双剪刀的电四极强度带有 `sin^4(theta)` 因子。本任务把经典平衡角 `theta_0` 附近的集体角提升为量子坐标，检验能带终止 `theta_0 -> 0` 时零点涨落是否留下有限的四极强度代理。

## Grounded Evidence

- `amr-microscopic-quadrupole-shears-restoring-constant` 在等权交换偶、同一集体角的条件下推导 `C_AMR=2 C_MR`，并明确 `sin^4(theta)` 和 `J^(2)` 代理的模型边界。
- `amr-coulomb-repulsion-proton-blades-and-closing-asymmetry` 汇总 Roy 的 `110Cd` 带内 `B(E2)=0.14(1)` 到 `0.06(2) e^2 b^2` 与 Rather 的 `104Pd` `0.26(2)` 到 `0.02(1) e^2 b^2`，同时警告有限端点强度不能单独归因于库仑排斥。
- Frauendorf 的 AMR 几何综述支持镜像剪刀的横向四极张量结构，但不是对本量子涨落数值的实验测量。

这些来源支持几何和量级背景；没有来源直接测得 `M_theta`、`kappa_3`、`kappa_4` 或端点声子波函数。因此本页的数值是透明的有效坐标模型结果。

## Provisional Reasoning

令 `x=theta-theta_0`，局部哈密顿量为

`H=p_theta^2/(2M_theta)+C_AMR*x^2/2+kappa_3*x^3/6+kappa_4*x^4/24`。

在稳定极小附近，`omega_shears=sqrt(C_AMR/M_theta)`，所以谐近似零点能为

`E_ZPE=1/2 hbar omega_shears`，

而角坐标方差为

`sigma_theta^2=<x^2>=hbar/(2 M_theta omega_shears)`。

当 `kappa_3,kappa_4` 不为零时，程序在谐振子基底中直接对角化该哈密顿量；一阶高斯平均中三次项不贡献基态能量，但四次项给出 `Delta E_0^(1)=kappa_4 <x^4>_0/24 = kappa_4 sigma_theta^4/8`。三次项通过二阶微扰和波函数偏移重整化 `E_0`、方差与四阶矩，故不应只用谐公式替代数值结果。

在终止端点 `theta_0=0`，若四极几何振幅局部写作 `T(E2)=q_eff theta^2+O(theta^4)`，则基态均方强度代理为

`B(E2)_res = q_eff^2 <theta^4> = 3 q_eff^2 sigma_theta^4`

（谐近似），而非零点经典极小值给出的 `q_eff^2 theta_0^4=0`。标称扫描取 `M_theta=10 hbar^2/MeV`、`C_AMR=0.50 MeV/rad^2`、`kappa_3=0.02 MeV/rad^3`、`kappa_4=0.40 MeV/rad^4`、`q_eff=0.35 eb`，得到 `omega=0.2236 MeV`、谐 `E_ZPE=0.1118 MeV`、数值基态能 `0.1142 MeV`、`<theta^4>=0.1367 rad^4` 和 `B_res=0.0167 e^2 b^2`。给定的端点敏感性扫描范围为 `0.0088–0.0327 e^2 b^2`，因此 `0.01–0.03` 是该有效参数窗口内的残余平台量级。

这里的“平台”是 `q_eff^2<theta^4>` 的几何均方诊断。它不等于任意指定跃迁的约化矩阵元：例如严格对称谐振子中 `theta^2` 对一声子态的矩阵元因宇称而为零，而对二声子或未分辨的均方强度则可非零。实验的 `B(E2)` 还需要带波函数、角动量投影、有效电荷和跃迁初末态定义。

## Assumptions

1. 单一交换偶四叶片集体角可分离为 `theta_0+x`；其它形变坐标和核心转动被吸收到 `M_theta` 与 `C_AMR`。
2. 局部势在所扫描窗口内由三阶和四阶项充分描述，且 `kappa_4>0` 保证远端稳定性。
3. `hbar=1` 仅用于程序单位换算；`M_theta` 的单位为 `hbar^2/MeV`，角度以弧度计算。
4. `q_eff` 是 E2 几何映射的有效系数，不是由本模型独立预测的静态四极矩。
5. 有限基底数值对角化的结果只在基底收敛且局部势没有产生远离极小的深新井时可信。

## Competing Explanations

有限端点 `B(E2)` 也可能来自核心四极极化、频率依赖的 `beta_2`、配对和组态混合、侧馈/寿命系统学、非绝热角动量投影或多个 E2 振幅的相干干涉。AMR 几何本身不能从一个端点强度区分这些机制；库仑闭合延迟也只是已有笔记提出的待检验解释。

## Transfer Conditions

该展开可迁移到保持镜像交换偶、弱形变和单一软角坐标的偶偶 AMR 候选。迁移时必须重新求 `M_theta,C_AMR,q_eff`，并检查 `theta_0` 附近是否为真正极小。奇 A 阻塞、显著三轴非共面构型、多角度耦合或强组态交叉需要扩大坐标空间和跃迁算符。

## Failure Conditions

- 把 `q_eff^2<theta^4>` 当成每条实验 E2 分支的 `B(E2)`，忽略初末态宇称和角动量选择定则。
- 把标称 `0.0167 e^2b^2` 或扫描的 `0.01–0.03` 写成实验提取值或普适 AMR 常数。
- 在 `C_AMR<=0`、负有效四阶稳定性或强隧穿双阱条件下仍使用单极小声子公式。
- 把 `M_theta`、`kappa_3`、`kappa_4` 当成已有来源直接报告的微观量。

## Falsification or Reverse Tests

1. 用投影 PNC-CSM、TAC 或 GCM 计算同一初末态的 E2 矩阵元，检验是否保留端点强度以及一声子宇称抑制。
2. 改变基底数 `N=40,80,120` 并扫描 `kappa_3,kappa_4`；若结果对基底或高阶项不稳定，局部展开失效。
3. 让 `q_eff` 由低自旋静态四极矩或 Coulomb excitation 独立约束；若所需残余平台消失，当前数值只是系数重标定。
4. 同时拟合 `B(E2)`、`J^(2)`、寿命和带间 E2；若核心极化模型可以同样拟合，零点涨落不能被观测单独识别。

## Open Questions

- 能否从自洽 PNC 或 EDF 的时间依赖响应直接提取 `M_theta` 和三、四阶有效曲率？
- `110Cd` 与 `104Pd` 的不同核心惯量是否导致可分辨的零点平台差异？
- 如何通过多极混合比、跨带 E2 或静态四极矩区分均方平台与真实二声子跃迁？
- 四叶片的两个交换偶通道是否有可观测的反对称声子分裂？

## Human Review

本页为 `status: ai-draft`、`review_status: unreviewed`、`reasoning_status: provisional`。公式的谐振子部分是标准量子力学推导；AMR 坐标映射、`q_eff` 和 `0.01–0.03 e^2b^2` 数值窗口尚未经过人工论文级审核。

## Promotion or Rejection History

- 2026-10-29：创建本页和数值工件；接受 `E_ZPE`、`sigma_theta^2` 与端点 `<theta^4>` 的条件推导。
- 2026-10-29：将 `0.01–0.03 e^2b^2` 标记为有效参数扫描窗口，拒绝将其写成实验事实或库仑机制的唯一证明。
- 2026-10-29：显式加入一声子宇称选择定则边界，避免把均方强度非零误写成所有辐射分支非零。

## Reproducible Artifacts

目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-anharmonic-phonons/`。

- `amr_anharmonic_phonons.py`：谐振子基底对角化、端点敏感性扫描和 SVG 绘图。
- `phonon_scan.csv`：`theta_0=0–0.35 rad` 的声子、四阶矩和残余强度。
- `endpoint_sensitivity.csv`：`M_theta,C_AMR,q_eff` 端点扫描。
- `phonon_scan.json`：公式、参数、结果和证据边界。
- `zero_point_residual.svg`：端点平台随经典平衡角变化的矢量图。

运行命令：`python3 amr_anharmonic_phonons.py`。
