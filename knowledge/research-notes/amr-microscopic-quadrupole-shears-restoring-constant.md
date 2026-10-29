---
type: research-note
title: "AMR 两体四极残余作用与四剪刀恢复常数 C_AMR"
aliases: [AMR microscopic restoring constant, AMR quadrupole shears, C_AMR]
created: 2026-10-29
updated: 2026-10-29
created_from: "Day26 doctoral task: microscopic inversion of the AMR quadrupole restoring constant"
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-arxiv-full, amr-double-shears-core-coupling-and-b-e2-plateau, amr-cline-quadrupole-invariants-and-triaxial-core-evolution]
tags: [antimagnetic-rotation, quadrupole-quadrupole, shears, restoring-constant, 110Cd, 104Pd, dynamic-moment-of-inertia]
promotion_target: antimagnetic-rotation
---

# AMR 两体四极残余作用与四剪刀恢复常数 C_AMR

## Research Trigger

本轮把已有的 AMR 双剪刀几何推进到一个可计算的局部曲率问题：从粒子—空穴残余作用 `V_2=-chi_2 Q_2·Q_2` 定义等权集体角 `theta`，推导 `V(theta)=C_AMR sin²(theta)+O(sin⁴ theta)` 的微观系数，并用 110Cd、104Pd 的能级间隔给出条件性的 `chi_2` 尺度反演。目标是检验“四叶片使恢复常数约为单剪刀两倍”在什么归一化和对称性条件下成立。

## Grounded Evidence

Roy et al. 的 110Cd Table 1（原件 PDF p.324）给出 16–24+ 的 Eγ = 1075、1224、1323、1314、1358 keV，B(E2) = 0.14、0.12、0.11、0.09、0.06 e²b²；作者在 pp.325–326 使用双剪刀加核芯转动解释高自旋端的平缓下降（[[roy-2011-cd110-systematics-antimagnetic]]）。

Rather et al. 的 104Pd Table I（arXiv 全文 printed p.10）给出 16–26+ 的 Eγ = 927、1064、1193、1256、1365、1468 keV，B(E2) = 0.26、0.22、0.19、0.13、0.07、0.02 e²b²，及随自旋增大的 J^(2)/B(E2)；其模型参数包括 `V_pi nu=1.2 MeV`、`V_pi pi=0.2 MeV`、有效核心惯量约 `5 hbar²/MeV`（[[rather-2014-104pd-antimagnetic-arxiv-full]]）。这些是实验和作者模型的输入/解释，不能当作独立微观 chi_2 测量。

已有综合笔记确认两点边界：双叶电四极张量的横向振幅给出 `sin^4 theta`；核芯响应可减慢剪刀闭合，但高自旋 B(E2) 的有限值还可来自频率依赖形变、配对、侧馈和相干干涉（[[amr-double-shears-core-coupling-and-b-e2-plateau]]）。

## Provisional Reasoning

### 四极作用与单剪刀曲率

将约化的内禀四极矩写作 `q_p`、`q_n`（单位 eb），只保留粒子—空穴的秩 2 标量通道：

`V_2 = -chi_2 sum_{mu} (-1)^mu Q_{2mu}^{(p)} Q_{2,-mu}^{(n)}.`

在一个等权剪刀通道中，角依赖可归入 `P_2(cos theta)`，于是

`V_MR(theta) = -chi_2 q_p q_n P_2(cos theta)`

`= const + (3/2) chi_2 q_p q_n sin²(theta) + O(sin⁴ theta).`

因此在这里采用的约定下

`C_MR = (3/2) chi_2 q_p q_n.`

这一步是局部展开，不是把整个有限角势强行谐振子化；四阶项仍携带实际的 P2 几何非简谐性。

### 四叶片求和与因子二

AMR 的两质子空穴和两中子粒子各自构成交换偶的等权双叶。对每一类 p–n 张量通道做交换偶投影后，四体和可写成两个与单剪刀相同的独立等权通道：

`S_4(theta) = sum_{a=1,2}^{p} sum_{b=1,2}^{n} T_2(a)·T_2(b)`

`= 2 S_2(theta)`  （等长、等权、同一集体角、交换偶投影）。

这里的 `S_2` 是单剪刀的两通道归一化和；原始未归一化四对 p–n 组合确实是 4 对，而单剪刀是 2 对，故通道计数比也是 `4/2=2`。因此

`V_AMR(theta) = 2 V_MR(theta) + const`

`= const + 3 chi_2 q_p q_n sin²(theta)+O(sin⁴ theta)`,

并得到

`C_AMR = 3 chi_2 q_p q_n = 2 C_MR.`

这个证明的“约”字是必要的：若把每一片的 `q` 改定义为总双叶矩，或采用不同的相对角作为 `theta`，系数会重排；可迁移的不变量是交换偶张量通道数量和局部曲率的二倍关系。若直接把四个任意方向的裸 `P_2(cos gamma_ab)` 相加而不做交换偶投影，不能自动得到上述式子。

### J^(2) 条件反演

规则 ΔI=2 序列的中心有限差分取

`J^(2) = 4 / Delta E_gamma`,

其中 `Delta E_gamma` 用 MeV。脚本保留非正差分为 null；110Cd 的 1323→1314 keV 点因此不能被当作正常正惯量。为把 J^(2) 变成有明确假设的曲率尺度，定义局部坐标 `theta_ref=0.5 rad` 和

`C_proxy = (1/2)/(J^(2) theta_ref²)`,  `chi_2,proxy = C_proxy/(3 q_p q_n)`.

这是从动态惯量到局部势曲率的模型代理，不是唯一的实验反演；它假定单一绝热角自由度、忽略阻尼/侧馈和其他形变坐标。以 `q_p=q_n=1 eb` 的示范归一化，程序对 110Cd 正差分中心给出 J^(2) 约 16.1、44.4、114.3 hbar²/MeV（1323→1314 的负差分保留为 null）；104Pd 中心点约 15.0–23.3 hbar²/MeV。数值应结合原始 DSAM 协方差理解，不能作为独立 chi_2 测量。

## Assumptions

- `Q_2·Q_2` 被约化为 p–n 粒子—空穴秩 2 通道；同类 p–p、n–n 和配对重整化不在本次最小模型中。
- 四叶片等长、等电四极权重、等磁权重，保持 AMR 的交换偶对称。
- `theta` 是交换偶集体角；不同论文的单片角、半开角和总相对角不能直接互换。
- `q_p,q_n` 是有效约化矩；`q_p=q_n=1 eb` 仅用于扫描归一化。
- J^(2) 的中心差分和 `C_proxy` 只构成可复现的尺度估计。

## Competing Explanations

有限 B(E2) 或 J^(2) 轨迹也可能由频率依赖 β2、配对塌缩、组态交叉、侧馈、有效电荷变化、核芯集体转动和多振幅干涉造成。104Pd 的 PNC 研究尤其说明固定形变并不能自动重现高频下降。因此 `C_AMR≈2C_MR` 是哈密顿量与几何的条件结论，不是 AMR 的单独实验判据。

## Transfer Conditions

该结果可迁移到保持交换偶、等权双叶和同一集体坐标的偶偶 AMR 构型；需重新计算 `q_p,q_n`、有效电荷和核心惯量。奇 A、四空穴多组态、三轴非共面几何或显著权重不等时，应回到完整 Wigner-Eckart 矩阵元，不能直接套用二倍系数。

## Failure Conditions

若 p–n 四极矩有显著不等权，`S_4=2S_2` 不成立；若角坐标定义改变，曲率系数会出现 Jacobian 因子；若 J^(2) 的有限差分为负或顶端寿命为 effective lifetime，`chi_2,proxy` 不应计算。若把 `chi_2,proxy` 写成第一性原理或独立实验值，则超出证据边界。

## Falsification or Reverse Tests

1. 在代码中令两片权重为 `1+epsilon`、`1-epsilon`，检查四体和的二倍关系随 epsilon 破坏，并观察残余奇张量分量。
2. 分别改变 p–p、n–n 和 p–n 的 chi，测试是否仍能用单一 `C_AMR` 描述。
3. 对同一 Eγ 数据引入核芯惯量和频率依赖 β2，比较 `chi_2,proxy` 是否稳定；若不稳定，反演不可辨识。
4. 用静态四极矩或低自旋 B(E2) 独立固定 `q_p q_n`；若所需 chi_2 与高自旋代理不兼容，应撤回数值反演而保留几何二倍关系。

## Open Questions

- 是否能在投影配对或 EDF 计算中同时输出四个单片的约化 Q2 矩和交换偶投影？
- 110Cd 的核心惯量 19.5 与 104Pd 的约 5 hbar²/MeV 如何进入同一角坐标的绝热曲率？
- 需要新的独立静态四极矩、跨带 E2 或完整 DSAM 协方差，才能把 `chi_2,proxy` 提升为可检验参数。

## Human Review

尚未进行人工审核；本页为 Codex self-audit，`review_status: unreviewed`。来源页和本推导中的数值均保留 `needs_review` 边界。

## Promotion or Rejection History

2026-10-29：新建。接受“等权交换偶四体张量通道使局部曲率加倍”的条件推导；将 `chi_2` 的 J^(2) 反演明确降级为 `chi_2,proxy`，并保留 110Cd 非正有限差分与 104Pd 顶端 DSAM 边界。

## Reproducible Artifacts

目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-restoring-constant/`。

- `amr_restoring_constant.py`：四极 P2 曲率、J^(2) 有限差分和扫描。
- `j2_chi2_scan.csv`：110Cd/104Pd 原始 Eγ、B(E2)、J^(2) 与条件代理。
- `chi2_restoring_scan.csv`：`chi_2`–`C_MR/C_AMR` 扫描。
- `amr_restoring_constant.json`：参数、结果和边界。
- `restoring_constant_scan.svg`：角势和曲率矢量图。

运行命令：`python3 amr_restoring_constant.py`。
