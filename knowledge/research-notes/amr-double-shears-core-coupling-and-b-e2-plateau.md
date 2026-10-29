---
type: research-note
title: "110Cd 与 104Pd 反磁转动：双剪刀、核芯耦合与 B(E2) 平台"
aliases: [amr-double-shears-core-coupling-and-b-e2-plateau, Cd-Pd AMR double shears]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-first-page, zhang-2019-104pd-pnc-antimagnetic-rotation, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
created_from: Day26 AMR double-shears and core-coupling study
promotion_target: antimagnetic-rotation
tags: [110Cd, 104Pd, antimagnetic-rotation, double-shears, B(E2), dynamic-moment-of-inertia]
---

# 110Cd 与 104Pd 反磁转动：双剪刀、核芯耦合与 B(E2) 平台

## Research Trigger

本轮任务检验两个相连的问题：110Cd Band B（16+–24+）和 104Pd 高自旋 yrast 带的寿命、Eγ、B(E2) 及 J^(2)/B(E2) 系统学；以及双剪刀的离散对称性、sin⁴θ 角因子和弱长椭核芯为何能让 B(E2) 保持有限。这里把实验事实、论文作者的粒子加转子解释、可复现的条件计算和本轮推断分开。

## Grounded Evidence

### 实验数据

Roy et al. 的 110Cd Table 1（PDF p.324）给出带内 E2 的平均寿命和绝对强度：

| 初态 I | Eγ (keV) | τ (ps) | B(E2) (e²b²) |
|---:|---:|---:|---:|
| 16+ | 1075 | 0.36(3) | 0.14(1) |
| 18+ | 1224 | 0.23(3) | 0.12(2) |
| 20+ | 1323 | 0.17(3) | 0.11(2) |
| 22+ | 1314 | 0.21(7) | 0.09(3) |
| 24+ | 1358 | 0.27(7) | 0.06(2) |

这些数值支持“缓慢下降”而非由实验直接支持的恒定平台。1323→1314 keV 的有限差分为负；因此用 J^(2)=4/ΔEγ 时该点不能被无提示地当作正常正惯量。Roy 的阻止本领和 feeding 误差边界仍适用（[[roy-2011-cd110-systematics-antimagnetic]]，p.324 Table 1；pp.325–326 Fig.4）。

Rather et al. 的 104Pd Table I（完整 arXiv 版本 printed p.11；出版物正文第一页摘要和模型定义见 [[rather-2014-104pd-antimagnetic-first-page]]）给出：

| 初态 I | Eγ (keV) | τ (ps) | B(E2) (e²b²) | J^(2)/B(E2) |
|---:|---:|---:|---:|---:|
| 16+ | 927 | 0.45(3) | 0.26(2) | 112.3(8.6) |
| 18+ | 1064 | 0.27(2) | 0.22(2) | 140.9(12.8) |
| 20+ | 1193 | 0.18(1) | 0.19(1) | 334.2(17.6) |
| 22+ | 1256 | 0.20(1) | 0.13(1) | 282.3(21.7) |
| 24+ | 1365 | 0.24(2) | 0.07(1) | 554.3(79.2) |
| 26+ | 1468 | 0.66(3) | 0.02(1) | — |

因此用户所说的约 0.21→0.08 是对中高自旋区间的概括；原表的完整范围是 0.26→0.02。论文 p.3 的换算式为 `B(E2)=0.0816/(Eγ^5 τ)`，p.3–5 说明 DSAM、lineshape、side feeding 和 40°/157°双角度 global fit；p.4 明确说 J^(2)/B(E2) 随自旋增加且远大于良好形变转子。

### 论文模型和组态

Roy 2011（pp.323–326）采用 `π(g9/2)^−2 ⊗ ν(h11/2)^2` 的 110Cd 双剪刀加核芯模型，打印的模型参数为 `j_h=9/2`、`j_n=10`、`𝓙_c=19.5 ℏ²/MeV`、`V_πν≈1.2 MeV`、`V_ππ≈0.15–0.2 MeV`。Rather 2014（arXiv pp.4–6）对 104Pd 采用 `π(g9/2)^−2 ⊗ ν[h11/2²(g7/2/d5/2)²]`，`j_h=9/2`、`j_n=16`、`𝓙≈5 ℏ²/MeV`、`𝓙_rot≈17 ℏ²/MeV`、`V_πν=1.2 MeV`、`V_ππ=0.2 MeV`、`eQ_eff=1.3 eb`。π(g9/2)^−4 是邻近核或更高空穴数的变体，不能把它直接当成上述两条带的同一冻结子空间。

两篇论文都给出

\[
 I_{sh}=j_p+2j_h\cos\theta,
 \qquad B(E2)=\frac{15}{32\pi}(eQ_{eff})^2\sin^4\theta .
\]

Roy 的作者解释是核芯转动分担一部分角动量，使剪刀闭合变慢；Rather 的 104Pd 文章把同一粒子加转子思路用于 16+–26+。这些是作者解释或模型结果，不是从 B(E2) 单独反演出的实验核芯角动量。

## Provisional Reasoning

### 双剪刀几何与反幺正边界

在总转轴为 z、两支等长且等磁权重的理想几何中，取

\[
 \mathbf j_\pm=j_h(\pm\sin\theta\cos\phi,\;\pm\sin\theta\sin\phi,\;\cos\theta),
 \quad \mathbf j_n=(0,0,j_n).
\]

质子空穴的磁矩为 `g_h j_±` 时，

\[
 \boldsymbol\mu_{h,\perp}=g_h(\mathbf j_{+,\perp}+\mathbf j_{-,\perp})=0,
 \quad \mu_z=2g_hj_h\cos\theta+g_nj_n .
\]

这证明的是内禀横向期望值相消；它不证明纵向静态磁矩、局域电流、任意跨带 M1 矩阵元都为零。

需要严格区分两个对称操作。对轴矢量，时间反演后再做 `R_y(π)` 给出

\[
 S=R_y(\pi)T:\quad (J_x,J_y,J_z)\mapsto(J_x,-J_y,J_z).
\]

若 cranked 内禀态是 S 的本征态，则 S-odd 的 `J_y` 期望值为零；`J_x` 在 S 下为偶，单独的 S 不能令它为零。`J_x` 的相消来自两支等价刃的交换/镜像条件（可由 `R_z(π)` 将 `j_+↔j_-` 表示），再与共同的平面几何合并才得到完整的 `μ_x=μ_y=0`。因此题目中“仅由 R_y(π)T 保证整个 μ⊥=0”需要修正为“`S` 加等价双刃交换对称保证内禀横向磁矩相消”。同样，理想 AMR 的固定 signature ΔI=2 带内序列不产生强 ΔI=1 M1，但这不是所有跨带 M1 的普适零算符定理。

### 不可约四极张量

用 `C_2m=√(4π/5)Y_2m`，有

\[
 C_{21}=-\sqrt{3/2}\,z(x+iy),\qquad C_{22}=\sqrt{3/8}(x+iy)^2 .
\]

两支等电四极权重相加时，横向坐标在 `C21` 中变号，在 `C22` 中平方，因此

\[
 Q_{21}=0,\qquad Q_{22}=2q\sqrt{3/8}\sin^2\theta e^{2i\phi}.
\]

定义归一化 `T_2m=Q_2m/[q√(3/8)]` 后，才是题目要求的

\[
 \boxed{T_{21}=0,\qquad T_{22}=2\sin^2\theta e^{2i\phi}}.
\]

因此绕转轴的 E2 振幅满足 `|T22|²∝sin⁴θ`。例如 θ=30° 时相对 θ=90° 的强度为 1/16，θ=15° 时为 0.00449（下降约 223 倍）。这个幂律是固定等权几何的角因子；绝对尺度仍由 `Q_eff`、有效电荷、核芯相干振幅和实验分支决定。

### 核芯耦合和平台

粒子加转子模型可写为

\[
 I(\theta)=I_{sh}(\theta)+\mathcal J_c\omega_{sh}(\theta),
 \quad \omega_{sh}=\frac{1.5V_{\pi\nu}}{j_h}\cos\theta-
 \frac{6V_{\pi\pi}}{n j_h}\cos2\theta\cos\theta .
\]

若稳定支上 `dω_sh/dcosθ>0`，`𝓙_c dω_sh/dcosθ` 增大 `dI/dcosθ`，同样的自旋增量对应更小的剪刀闭合，故 B(E2) 的下降被拉平。这解释了为什么 110Cd 的有限核芯响应可以把纯剪刀的快速塌缩改成缓降；它并不自动产生一个独立、恒定的 B(E2) 底座。

本轮脚本按 Roy 打印式和参数直接求根：110Cd 的 θ 为 70.0°、62.6°、54.2°、44.3°、31.1°（16+–24+），模型 B(E2) 为 0.141、0.112、0.078、0.043、0.013 e²b²，而原表为 0.14、0.12、0.11、0.09、0.06 e²b²。结论是“核芯角动量响应的机制成立”，不是“打印参数逐点完美复现实验平台”。104Pd 脚本求得 θ≈90.0°→23.3°，模型 B(E2) 0.252→0.006 与原表 0.26→0.02 同量级并保留高自旋端偏差。

### β2≈0.12 的核芯 B(E2) 尺度

为量化“底座”而不把它冒称实验分解，采用明确的均匀带电轴对称 K=0 转子估计：

\[
 R=1.2A^{1/3}\mathrm{fm},\quad Q_0=\frac{3}{\sqrt{5\pi}}ZR^2\beta_2,
\]

\[
 B_{core}(E2;I\to I-2)=\frac{5}{16\pi}Q_0^2
 \frac{3I(I-1)}{2(2I-1)(2I+1)} .
\]

在 I=20、β2=0.12 时得到：

| 核 | Q0 (eb) | 条件估计 B_core(E2) (e²b²) | 与观测端点的关系 |
|---|---:|---:|---|
| 110Cd (Z=48) | 1.441 | 0.0737 | 与 24+→22+ 的 0.06(2) 同一量级 |
| 104Pd (Z=46) | 1.331 | 0.0628 | 与 24+→22+ 的 0.07(1) 同一量级，但 26+→24+ 为 0.02(1) |

这给出一个有用的数量级：β2≈0.12 的长椭核芯若保持 K=0 相干转动，可贡献约 0.06–0.08 e²b² 的高自旋 E2 尺度。它不是“实验 B(E2) 中 100% 来自核芯”的比例，也不是 Roy/Rather 从寿命直接分离出的项；真实 AMR 跃迁是剪刀振幅、核芯振幅和相位的相干和。104Pd 的 PNC-CSM 结果进一步显示，固定 ε2=0.18 不能重现实验在 ħω>0.6 MeV 的快速下降，作者需拟合 ε2 随频率下降至约 0.75 MeV 趋零（[[zhang-2019-104pd-pnc-antimagnetic-rotation]]，PDF p.4 Fig.3及 pp.5–7），所以“β2=0.12 必然产生平台”不是可迁移定律。

### J^(2)/B(E2) 巨比值

对规则 ΔI=2 序列，在跃迁中心使用

\[
 \mathcal J^{(2)}\simeq\frac{4}{E_\gamma(I+2\to I)-E_\gamma(I\to I-2)} .
\]

104Pd Table I 直接报告的比值由 112(9) 增至 554(79)；110Cd 用 Table 1 Eγ 和 B(E2) 可得到典型约 100–340 的量级，但 1323→1314 keV 的回弯点必须保留为有限差分异常。大比值的微观含义是剪刀/准粒子重新排布仍能增加 I 和改变能量曲率，而电荷四极辐射随横向剪刀分量衰减；它是上下文诊断量，不能单独作为无条件 AMR 排他门。

## Assumptions

- 双剪刀推导采用两支等长、等磁权重、等电四极权重的半经典内禀矢量。
- `T22=2sin²θe^{2iφ}` 使用文中明示的归一化；物理 Q2m 还含 q 和球谐归一化因子。
- Roy/Rather 的 `Q_eff`、`𝓙`、`V_πν` 和 `V_ππ` 是论文模型输入，不等同于独立实验测得的 β2 或核芯矩。
- β2 核芯底座计算采用均匀电荷、轴对称 K=0、`r0=1.2 fm`，只作尺度估计。
- 未把 π(g9/2)^−4 变体、配对涨落、组态混合和量子投影强行压入 π(g9/2)^−2 双剪刀模型。

## Competing Explanations

有限 B(E2) 还可能来自频率依赖形变、配对/占据重排、side feeding、带交叉、有效电荷变化和多个电四极振幅的相干干涉。104Pd 的 PNC-CSM 是重要反向证据：双剪刀几何和 normal alignment 并不足以保证平台，形变演化仍是模型输入/拟合量。弱形变集体转动也能给出有限 B(E2)，但同时应检查其绝对强度、角动量曲率、带内 ΔI=1 M1 和形变独立约束。

## Transfer Conditions

可迁移的是等价双刃下的奇 q 张量相消、`sin⁴θ` 角因子、相干振幅求和和 `J^(2)` 的有限差分定义。不可直接迁移的是 110Cd 的 `𝓙_c=19.5`、104Pd 的 `𝓙=5`、β2=0.12 的数值底座、18–26% 的核芯比例或“J^(2)/B(E2)>100 即排他 AMR”阈值。奇 A、π(g9/2)^−4、多组态或三轴几何必须重新求解磁/电权重和 signature。

## Failure Conditions

若双刃磁权重不等、存在显著三维不对称、跨带组态混合或 `Q_eff(I)` 变化，`μ_perp=0` 与固定 `sin⁴θ` 不能直接使用。若把 S=R_y(π)T 单独当作令 Jx、Jy 均为零的定理，或把内禀期望值零升级成任意 B(M1) 矩阵元零，推导即越过适用边界。若未来测得独立 β2 与寿命分解明显不支持 0.06–0.08 e²b² 的核芯尺度，当前底座估计应被撤回而保留角动量耦合机制。

## Falsification or Reverse Tests

1. 在脚本中令 `g1=1+ε,g2=1−ε`，检查 `μ_perp∝ε sinθ`、相应 M1 强度 `∝ε²`；这反证精确相消依赖等权双刃。
2. 分别改变电四极权重和磁权重，检查 `C21` 与 `μ_perp` 的独立恢复，区分电张量对称和磁矩对称。
3. 固定双剪刀几何而令 `Q_eff(I)` 或核心 β2 随频率变化，比较同一 θ 轨迹下不同 B(E2)；这检验“核芯响应减慢闭合”与“核芯直接提供振幅”是否可辨识。
4. 对 110Cd 的 1323→1314 keV 保留负有限差分，并对 104Pd 26+ 端点单独处理；任何删点后才出现的单调巨比值都不应称为独立验证。

## Open Questions

- Roy 2011 Fig.4 的原始 bandhead/spin 映射和完整 feeding 协方差能否获得，以判断打印式与实验 B(E2) 的偏差来自参数、分支还是寿命系统误差？
- 104Pd 的完整出版商正文、实验形变约束和 PNC-CSM 拟合协方差能否补齐？
- 是否能在同一投影配对或 EDF 框架中同时得到 Cd/Pd 的绝对 B(E2)、核心四极矩和弱跨带 M1？
- β2≈0.12 的核芯“0.06–0.08 e²b²”尺度能否由独立静态四极矩、低自旋 E2 或新一代寿命数据约束，而不是从高自旋 B(E2)反推？

## Human Review

尚未进行人工审核；`review_status: unreviewed`。本页的原件数值和模型定位是 Codex self-audit，不能写成 `human-reviewed`。

## Promotion or Rejection History

2026-10-29：新建。保留 Roy 2011 与 Rather 2014 的逐点数据、S 对称性的条件证明、归一化四极张量、β2 核芯尺度计算和 104Pd PNC-CSM 的反向边界。撤回“仅凭 S 即保证所有横向矩阵元为零”“打印参数完美复现 110Cd 平台”和“J^(2)/B(E2)>100 为普遍排他阈值”等过强表述。

## Reproducible Artifacts

本页的固定角度和核芯尺度讨论由 [[amr-core-quadrupole-drive-and-shears-torque]] 的固定总角动量两自由度模型继续展开。

脚本和结果位于 `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-double-shears/`：

- `amr_double_shears_core.py`：张量、磁矩、粒子加转子、β2 核芯尺度和来源哈希。
- `amr_double_shears_core.json`：计算结果、原始数据表、参数和边界。
- `angle_and_core_scale.csv`、`beta2_core_scale.csv`：角因子与 β2 扫描。

运行：`python3 amr_double_shears_core.py`。网格检查得到 `max|C21|=0`、`max|T22−2sin²θe^{2iφ}|=8.01×10⁻¹⁶`、`max|μ⊥|=0`；这些只验证代数实现，不验证真实多体波函数。
