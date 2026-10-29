---
type: research-note
title: "静态八极形变中的 IVGDR 多重劈裂与低能 E1 能量加权求和规则边界"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [octupole GDR splitting, low-energy E1 EWSR, octupole-induced IVGDR fragmentation]
tags: [octupole, gdr-splitting, e1-transitions, ewsr, dipole-moment]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 L4 microscopic and phenomenological octupole-IVGDR/E1-EWSR investigation
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole]
---

# 静态八极形变中的 IVGDR 多重劈裂与低能 E1 EWSR 边界

## Research Trigger

本轮问题是：在平均场具有反射不对称分量 `beta3 != 0` 时，传统轴对称四极形变给出的 `K=0` 与 `K=1` IVGDR 双峰是否会因奇多极自由度而进一步碎裂？同一问题还要求解释低能负宇称 `1-` 激发为何可以有局域增强的 `B(E1)`，却只消耗很小的 E1 能量加权和规则（EWSR）。

研究对象必须分层处理。实验室系的有限核态仍可取良好宇称；反射不对称的是内禀密度或未投影平均场。因而 `beta3` 产生的“奇宇称分量”在实验室响应中表现为宇称恢复后的跃迁核、门道态混合和响应碎片化，而不是把一个实验室态直接标成“无宇称”。

可复现工件位于 [`octupole-gdr-e1` worker](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-gdr-e1/)。它是透明的现象学扫描，不冒充自洽 QRPA/RPA 或 Ba/Ra/Th 的实测 GDR 分解。

## Grounded Evidence

| 主张 | 证据层 | 来源与定位 | 边界 |
|---|---|---|---|
| 反射不对称核的 E1 对质子—中子位移和相消敏感，E3 通常是更集体的八极观测量；静态形变、软振动与宇称恢复不能混为一谈。 | review-synthesis | [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]，RMP pp.349–421，Secs. II–VII，尤其 Sec. II.B、III、IV.C–D、VII | 综述地图，不是本轮 GDR 劈裂的直接计算。 |
| `144Ba` 与 `146Ba` 均有强的直接基态 E3；`146Ba` 的小 E1 不能单独作为八极集体性减弱的证据。 | direct experiment plus model interpretation | [[bucher-2016-144ba-direct-octupole]] Table I；[[bucher-2017-146ba-direct-octupole]] PDF pp.3–5, Table I, Figs.3–5 | GOSIA 的 E1 约束主要依赖既有寿命/分支；SCCM 的占据—相消是模型解释。 |
| `146Ba` Table I 的向上 E1 幅度 `0.000223 e b^(1/2)` 换算为 `B(E1)=4.9729e-6 e^2 fm^2`；在本工件的 `E=1.05 MeV` 和 `S_TRK=615.186 MeV e^2 fm^2` 下，单态能权份额约为 `8.49e-9`。 | source value plus explicit unit algebra | [[bucher-2017-146ba-direct-octupole]] PDF p.3 Table I；`e1_ewsr_partition.csv` | 这是一个低能单态的 toy 份额，不等于覆盖全部 pygmy/低能 E1 带。 |
| E1 的总能权额度由带增强因子的 TRK 型表达式控制；单个低能态所占份额还取决于它的能量和绝对 `B(E1)`。 | exact sum-rule identity under stated Hamiltonian convention | 工件 `results.json` 的 `equations` 与 `e1_ewsr_partition.csv` | `kappa=0.20` 是本扫描设定；真实值依赖速度依赖相互作用、交换流和模型约定。 |

## Provisional Reasoning

### 1. Thouless 生成元与质心不变的内禀偶极算符

令总质心坐标为

\[
 \mathbf R_{\rm cm}=\frac{1}{A}\left(\sum_{p=1}^{Z}\mathbf r_p+\sum_{n=1}^{N}\mathbf r_n\right).
\]

实验室电荷偶极的平移不变形式沿内禀轴 `z` 为

\[
 \hat D_z=e\left(\sum_p z_p-ZR_{{\rm cm},z}\right)
 =e\frac{N}{A}\sum_p z_p-e\frac{Z}{A}\sum_n z_n.
\]

定义质子和中子子系统质心 `\bar z_p=Z^{-1}\sum_p z_p`、`\bar z_n=N^{-1}\sum_n z_n`，得到严格恒等式

\[
 \boxed{\hat D_z=e\frac{NZ}{A}(\bar z_p-\bar z_n)}.
\]

这等价于质子有效荷 `e_p=N/A`、中子有效荷 `e_n=-Z/A` 的等矢量 E1 算符。Thouless 观点中，`exp(i\eta\hat D_z/\hbar)` 生成试探偶极扰动；由于 `D_z` 与总平移生成元对易，质心平移零模不被当成物理 IVGDR。对平移投影算符

\[
 \hat P_{\rm cm}=\int d^3a\,e^{i\mathbf a\cdot\hat{\mathbf P}_{\rm cm}/\hbar}
\]

先投影或使用上述有效荷，给出的响应核与直接在质心系计算一致；具体差异来自截断模型空间和未完全自洽的剩余相互作用，而非偶极算符本身。

这里必须区分同位旋通道。简单的等标量 `\sum_i r_iY_{1\mu}` 是质心生成元并含有伪激发；物理等标量压缩偶极通常使用形如 `r^3Y_1-(5/3)\langle r^2\rangle rY_1` 的修正算符。本笔记给出的 TRK 额度和 IVGDR 劈裂扫描针对等矢量 E1，不把等标量压缩模和 IVGDR 合并。

### 2. 八极形变如何进入 GDR 响应

轴对称四极形变首先把等矢量 GDR 分成沿对称轴的 `K=0` 与垂直方向的 `K=1` 分量。反射不对称内禀场可写成

\[
 \rho_q(r,\theta)=\rho_{q0}(r)+\beta_2\rho_{q2}(r)Y_{20}(\theta)
 +\beta_3\rho_{q3}(r)Y_{30}(\theta)+\cdots,
\]

其中 `q=p,n`。在线性化 TDHF/QRPA 语言中，`beta3` 会使偶极过渡密度与奇多极门道组态共享非对角响应核；库仑表面项和等矢量表面项分别改变质子—中子相对流和局域表面恢复力。对一个固定 `K` 的最小门道模型，可写成

\[
 H_K=\begin{pmatrix}E_K-\Delta_K/2&g_{3K}\\g_{3K}&E_K+\Delta_K/2\end{pmatrix},\qquad
 g_{3K}=c_K E_{\rm GDR}\beta_3,
\]

从而

\[
 E_{K,\pm}=E_K\pm\sqrt{(\Delta_K/2)^2+g_{3K}^2}.
\]

当 `beta3→0` 时，每个 `K` 的门道伙伴退化；当 `beta3` 增大时，原来的两类 `K` 结构变成最多四个响应成分。它们是响应峰的成分，不能在宇称恢复后直接称为四个实验室宇称本征态。工件中 `g3`、线宽和峰强分配都是公开的现象学参数，目的在于给出可证伪的趋势：`K=0/K=1` 的基线分裂来自 `beta2`，额外伙伴间隔随 `beta3` 增强。

### 3. 内禀偶极矩、局部八极质心偏移与中子皮

若八极表面使中子和质子局部密度的质心沿 `z` 方向偏移 `\delta z=\bar z_p-\bar z_n`，则 `D_0=eNZ\delta z/A`。中子皮通过两个因素进入：一是 `N/Z` 改变几何权重 `NZ/A`，二是表面八极密度的中子分量比质子分量更宽，使局部 `\delta z` 对 `beta3` 的响应改变。这个关系不要求把整个核看成两个刚性液滴；它只要求密度矩存在。

工件采用

\[
 \delta z=0.018\,\beta_3[1+2(N-Z)/A][1+0.5\,\Delta r_{np}/0.20\,\mathrm{fm}]\ \mathrm{fm}
\]

作为数量级扫描的闭合式。`0.018 fm` 是明确标记的示意尺度，不是实验拟合。以 `146Ba` 的 `beta3=0.10`、`\Delta r_{np}=0.17 fm` 为例，脚本给 `\delta z=0.00376 fm`、`D_0=0.130 e fm`；改变 `beta3` 或中子皮参数会线性地改变这两个量。这一计算展示了质心修正项如何演化，不能替代 SCCM 的有符号投影跃迁核。

### 4. E1 TRK EWSR 与低能份额

对等矢量 E1，采用本轮指定的额度

\[
 S_{\rm TRK}(E1)=\frac{9}{4\pi}\frac{\hbar^2e^2}{2m_N}\frac{NZ}{A}(1+\kappa).
\]

对 `146Ba`、`\kappa=0.20` 和 `\hbar^2/(2m_N)=20.73553 MeV fm^2`，脚本得到

\[
 S_{\rm TRK}=615.186\ \mathrm{MeV\,e^2fm^2}.
\]

某一低能态的能权份额是

\[
 f_{\rm low}=\frac{E_{\rm low}B(E1;0^+\to1^-)}{S_{\rm TRK}}.
\]

在 `E_low=1.05 MeV` 下，`146Ba` 若要单态贡献 `0.1%`、`0.3%`、`1%`，分别需要 `B(E1)=0.586`、`1.758`、`5.859 e^2fm^2`。按 `K=0` 转子约定 `B(E1)=3D_0^2/(4\pi)`，相当于 `D_0=1.567`、`2.714`、`4.953 e fm`。这些是“给定份额所需的强度”反算，不是 `146Ba` 的测量值。

相反，Bucher 2017 Table I 的 `0.000223 e b^{1/2}` 给出 `B=4.9729e-6 e^2fm^2`，本脚本的单态份额仅 `8.49e-9`（即 `8.49e-7%`）。按轴对称 `K=0` 关系 `B(E1)=3D_0^2/(4\pi)`，该幅度对应 `D_0≈0.00456 e fm`。因此“低能 E1 常见的 0.1–1%”只能用于一个已覆盖多个低能态的集成区间或其它核素，不能自动套到这一个 Ba 离散跃迁。局域 `10^{-4}–10^{-2} W.u.` 的增强也不等价于大 EWSR 份额，因为 W.u. 是无能量权的单态标度，EWSR 还乘以 `E` 并除以整个 TRK 额度。

### 5. 高能 GDR 尾部相消的正确表述

若低能态和一个 GDR 门道真正混合成同一末态，跃迁幅度可以写成

\[
 D_{\rm low}'=D_{\rm low}\cos\theta-D_{\rm GDR}\sin\theta,
 \qquad \tan2\theta=\frac{2g_3}{E_{\rm GDR}-E_{\rm low}}.
\]

因为 GDR 的总 EWSR 很大，`D_GDR` 的幅度尺度远大于低能壳极化偶极；很小的 `theta` 就可能把低能净幅度推近零。这是**幅度级**的相消，不能把 GDR 强度函数的高能尾部直接从低能 `B(E1)` 中非相干相减。必须满足共同末态、相同多极性、相对相位和同一反应响应条件。现有 Ba 来源支持“中子占据引起的质子—中子偶极贡献相消”，但没有给出 IVGDR 门道的共同末态相位测量；因此 IVGDR 相消在本笔记中仍是可检验的竞争假设。

## Assumptions

1. `K=0/K=1` 基线由轴对称 `beta2` 产生，`beta3` 通过每个 `K` 分支的两能级门道耦合产生额外响应成分。
2. 峰形使用固定 Lorentzian 线宽 `Gamma=3.8 MeV`；它只用于生成曲线数据，不表示任何特定核素的实验宽度。
3. `kappa=0.20`、经验 GDR 质心公式和 `delta_z` 闭合式均是扫描输入；EWSR 代数结构比这些数值设定更稳健。
4. `B(E1)=3D_0^2/(4\pi)` 只用于 `K=0` 转子尺度换算。实验 E1 振幅的方向、`K` 混合和分支完整性需要按具体谱学重新处理。
5. 低能份额中的 0.1–1% 是参数扫描区间，不是对 `144,146Ba` 或 `224Ra/226Th` 的直接实验认证。

## Competing Explanations

- **质子—中子局部相消**：Bucher 2017 的 SCCM 解释，现有来源支持到模型层；它不需要 IVGDR 与低态共同末态相干。
- **IVGDR 门道相消**：若小的八极耦合把巨大 GDR 幅度混入低态，可以产生极小净 E1；需要相对相位和响应函数证据。
- **八极软振动/宇称投影**：大 `B(E3)` 和小 E1 可以来自动态八极波函数的非对角积分，并不要求静态刚性梨形势阱。
- **等标量压缩偶极或背景碎片化**：若观测量实际含等标量压缩模、PDR、准粒子碎片或多步库仑激发，它们会改变“单一 IVGDR”解释；必须先做通道分解。

## Transfer Conditions

算符恒等式 `D_0=eNZ(\bar z_p-\bar z_n)/A` 和份额定义可跨核迁移。GDR 劈裂的峰位、线宽、`g_3`、`kappa`、中子皮和 `beta3` 映射必须逐核重新输入。将 `144,146Ba` 的直接 E3/E1 对照迁移到 `224Ra` 或 `226Th` 时，需有同方向的寿命、分支、能级和响应数据；不能只凭八极质量区相似性迁移。

## Failure Conditions

- 线性小振幅近似失效、`beta3` 使门道与多准粒子连续谱强耦合时，四峰两能级模型不再足够。
- 自洽残余相互作用、交换流或连续谱耦合使 `kappa` 远离扫描值时，数值 EWSR 份额只能作基准。
- 没有共同末态和相对相位时，不能把 GDR 尾部相消写成已证实机制。
- `B(E1)` 的单位、跃迁方向、初态简并或 `K` 因子混用时，低能份额会出现数量级错误。

## Falsification or Reverse Tests

1. 做反射不对称自洽 QRPA/TDHF：固定 `beta2`，扫描 `beta3`，检查是否出现超出常规 `K=0/K=1` 双峰的可分辨响应成分，并同时核对完整 EWSR。
2. 释放 `g_3`，用同一套参数联合拟合能量、线宽、E1 绝对强度和角分布；若只靠逐态重设相位/强度才能拟合，则门道模型失去解释力。
3. 对 `146Ba` 取得低能 E1 的更多分支、相对符号或干涉敏感观测；若相位与 GDR 门道不相容，IVGDR 相消假设被降级，而 SCCM 占据相消仍可独立保留。
4. 用完整低能区积分而非一个 `1-` 态计算 `m_1/m_0`；若集成强度仍远低于 0.1%，则“0.1–1%”只能适用于其它核或更宽能区。
5. 反向设置 `beta3=0`：工件应恢复每个 `K` 的单一峰；反向设置 `N=Z` 或 `delta_z=0`：质心修正偶极应为零。

## Open Questions

- `144,146Ba`、`224Ra` 和 `226Th` 是否已有同一实验设置下的能量分辨 E1 响应，可把 PDR、IVGDR 尾部和离散 E1 分开？
- 自洽 Gogny/Skyrme QRPA 中，八极静态场对 IVGDR `K` 分支的耦合矩阵元与速度依赖增强因子 `kappa` 各是多少？
- 能否通过相对相位、极化或库仑轨迹依赖的观测区分 SCCM 的占据相消和 IVGDR 共同末态相消？
- `D_0` 的静态内禀尺度与实验室 `B(E1)` 在强宇称投影/大振幅 GCM 中如何由同一过渡密度核闭合？
- 低能 E1 的 `0.1–1%` 区间应定义为积分窗口、单态份额还是 `m_1` 的实验包络；不同定义对跨核比较的影响有多大？

## Human Review

本页为 Codex self-audit 研究草稿，`review_status: unreviewed`。需要人工重点复核：TRK 归一化约定、E1 旋转因子、`beta3`—GDR 耦合的模型域，以及将 146Ba 小 E1 解释为 IVGDR 相消时所需的共同末态证据。任何 `0.1–1%` 的实验性概括都应回到具体核素和完整低能窗口的原始数据。

## Promotion or Rejection History

2026-10-29：依据 Day26 任务建立 provisional research note；写入质心修正推导、E1 TRK 份额核算、四分支 GDR 现象学扫描和相消反向检验。当前不晋升为正式 synthesis，也不把现象学 GDR 劈裂写成已观测事实。
