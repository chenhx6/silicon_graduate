---
type: research-note
title: "三轴八极手征四重态中静态磁偶极矩张量与 K=1/2 自旋退耦"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [octupole chiral quadruplet static magnetic moments, four-state magnetic moment tensor, 八极手征四重态磁矩]
tags: [mxd, chirality, octupole, magnetic-moments, spin-decoupling]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 octupole-chiral static magnetic moments and K=1/2 spin-decoupling investigation"
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
---

# 三轴八极手征四重态中静态磁偶极矩张量与 K=1/2 自旋退耦

## Research Trigger

本轮任务要求把三轴手征自由度、反射不对称八极自由度、静态磁偶极矩和
`K=1/2` Coriolis 退耦放在同一可计算框架，并对账 `78Br` 与 `133Ce` 的磁矩/
g 因子证据。核心问题是区分实验室可观测量、内禀破缺态的局部量，以及由
投影和态混合产生的干涉项。工件位于
`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-chiral-magnetic-moments/`。

## Grounded Evidence

### 1. 转动核芯、准粒子和磁偶极算符

Frauendorf 综述把旋转系写成 `H' = H - omega dot J`，并强调内禀平均场的离散
对称破缺态需要角动量量子化和对称性恢复后才对应实验室能带；TAC 的方向和
左右手性本身不是实验室直接观测量（[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]，
F01-4--F01-9，PDF pp.467--485）。这为以下分解提供了适用边界。

在粒子—转子分解 `J = R + j` 下，取一阶磁偶极算符

$$
  \hat\mu_z = g_R\hat R_z + \hat\mu_{q,z},
  \qquad
  \hat\mu_q=\sum_a(g_l^{(a)}\hat l_a+g_s^{(a)}\hat s_a).
$$

对实验室 stretched 态 `|IM=I;nu>`，恒等式 `R_z=J_z-j_z` 给出

$$
  \mu_\nu(I)=g_R I+
  \langle IM=I;\nu|\hat\mu_{q,z}-g_R\hat j_z|IM=I;\nu\rangle.
  \tag{1}
$$

因此第一项是集体核芯的 `g_R I`，第二项是准粒子轨道—自旋极化、有效
`g_s`、配对、阻塞、核芯极化和投影共同决定的内禀项。式 (1) 不说 `g_R I`
一定能从实验中独立分离；`g_R=Z/A`、有效 `g_s` 和 `j` 分解都是模型输入。

Butler--Nazarewicz 综述将八极形变、八极软振动、隧穿和宇称恢复明确分开，
并指出 E1 对质子—中子位移相消敏感而 E3 较集体（[[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]，
BN96-1--BN96-4，Secs. II--VII）。所以 E1 网络或近简并宇称伙伴不能单独
给出式 (1) 的内禀项。

### 2. 四态磁矩张量的代数

用局部基底

$$
 |1\rangle=|\chi=+1,p=+1\rangle,\quad
 |2\rangle=|\chi=-1,p=+1\rangle,\\
 |3\rangle=|\chi=-1,p=-1\rangle,\quad
 |4\rangle=|\chi=+1,p=-1\rangle,
$$

其中 `chi` 标记左右手性局部波包，`p` 标记八极双阱的局部反射分支。局部态
不是实验室的良宇称态。将式 (1) 的内禀部分在四态空间展开，最小对角
磁矩张量为

$$
 \hat\mu=\mu_0\,1+\mu_\chi\tau_z+\mu_p\pi_z
       +\mu_{\chi p}\tau_z\pi_z+\hat\mu_{\rm off},
 \tag{2}
$$

其中 `mu_0` 含 `g_R I` 与平均准粒子项，`tau_z`、`pi_z` 分别作用于 `chi`
与 `p`，而 `mu_chi p` 是两个破缺自由度的相干交叉项。直接代入可得

$$
 \mu_1-\mu_2=2(\mu_\chi+\mu_{\chi p}),\qquad
 \mu_3-\mu_4=-2(\mu_\chi-\mu_{\chi p}),
$$
并且

$$
 (\mu_1-\mu_2)+(\mu_3-\mu_4)=4\mu_{\chi p}.                 \tag{3}
$$

所以题目给出的
`mu_1 - mu_2 = -(mu_3 - mu_4)` 是一个有条件的对称极限：在本态序下它
等价于 `mu_chi p=0`。当 `T` 与 `P` 都在内禀态中破缺、且八极混合和手征
混合同时存在时，`mu_chi p` 一般允许非零，式 (3) 就是非平凡干涉劈裂。
这比把负号关系当成所有四重态的定理更严格。

必须区分三层对称性：时间反演使磁偶极算符变号，并把 `M=I` 映到 `M=-I`；
空间宇称对磁偶极（轴矢量）本身不变，但交换反射不对称局部井。故 `P` 或
`T` 恢复后会约束式 (2) 中的系数，具体约束取决于投影相位和态的对称标签，
不能仅由“破缺”二字指定。`hat mu_off` 还会在四态 Hamiltonian 对角化后
产生额外的相干修正。

### 3. `K=1/2` 退耦常数与八极宇称分岔

在强耦合 `K=1/2` 约定下，保留 Coriolis 退耦的旋转能写成

$$
 E_{\rm dec}(I,p)=A\,b_0^{(p)}(-1)^{I+1/2}(I+1/2),
 \qquad A=\frac{\hbar^2}{2\mathcal J}.
 \tag{4}
$$

对纯 `j` 轨道，常见极限是
`b_0=(-1)^{j+1/2}(j+1/2)`；在真实粒子—转子空间，`b_0` 是带波函数对
退耦算符的期望值，包含轨道混合和 Coriolis 重排。

用一对相反宇称轨道的最小混合块

$$
 H_{\rm orb}=\begin{pmatrix}\epsilon_a&\beta_3V_3\\
 \beta_3V_3&\epsilon_b\end{pmatrix},
 \qquad
 \theta=\frac12\tan^{-1}\frac{2\beta_3V_3}{\Delta\epsilon},
 \tag{5}
$$

并令八极分支的退耦算符在两个分支上有不同矩阵元，可写成工件所用的

$$
 b_0^{(p)}=b_{00}+p\,b_{03}\sin(2\theta),
 \qquad
 b_0^{(+)}-b_0^{(-)}=2b_{03}\sin(2\theta).                 \tag{6}
$$

`sin(2theta)=2 beta3 V3/sqrt((Delta epsilon)^2+4 beta3^2 V3^2)`，所以分岔
随八极混合从零开始，在强混合时趋于饱和。更一般地，若两轨道的对角退耦
矩阵元分别为 `b_a,b_b` 且存在 `b_ab`，则

$$
 b_0^{(p)}=b_a\cos^2\theta_p+b_b\sin^2\theta_p
              +2b_{ab}\sin\theta_p\cos\theta_p,
$$

而 `theta_+` 与 `theta_-` 不同会产生比式 (6) 更强的宇称分岔。这个机制
需要相反宇称、角动量相差约三的八极耦合候选；它不是由任意同宇称轨道标签
自动推出的。

为把 `b_0` 对静态磁矩的影响量化，工件采用明确标注的现象学代理

$$
 \delta\mu_{\rm dec}^{(p)}(I)=c_\mu b_0^{(p)}
 \frac{(-1)^{I+1/2}}{I+1}.                                      \tag{7}
$$

式 (7) 不是普适定理，而是把 `K=1/2` 波函数重排映射到 `mu_N` 的最小闭合
参数化。以脚本默认参数、`I=11/2`、barrier=`0.5` 为例：

| `beta3` | `b0+` | `b0-` | `delta mu_dec+` (`mu_N`) | `delta mu_dec-` (`mu_N`) |
|---:|---:|---:|---:|---:|
| 0.00 | 1.1000 | 1.1000 | 0.01100 | 0.01100 |
| 0.15 | 1.1846 | 1.0154 | 0.01185 | 0.01015 |
| 0.25 | 1.2397 | 0.9603 | 0.01240 | 0.00960 |
| 0.35 | 1.2931 | 0.9069 | 0.01293 | 0.00907 |

这些是 forward-model 数字，不是 `78Br` 或 `133Ce` 的实验抽取。`b_0` 的
相位和符号随文献约定改变，跨论文比较前必须固定旋转波函数相位。

### 4. `78Br` 与 `133Ce` 对账

现有本地原件不能提供题目所要求的目标核静态磁矩或 g 因子数值闭合：

| 核素 | 可核验的磁/电磁信息 | 对本任务的结论 |
|---|---|---|
| `78Br` | Liu 2016 的观测量是能谱、ADO/偏振、`B(M1)/B(E2)`、`B(E1)/B(E2)` 和 `delta E`；八条 E1 link 与 `beta30` softness 构成八极关联证据（[[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]]，L16-1--L16-14）。该 source 未报告静态 μ、TDPAD g 或四态 partner-resolved μ。 | 能对账的是“模型需要 M1/E1 矩阵元和寿命”，不能填入静态 μ 或 `b_0`。论文把 quartet 作为未来可观测方向，不能把四带当作已确证四重态。 |
| `133Ce` | Ayangeakaa 2013 报告两对 MχD 候选及相对 `B(M1)/B(E2)` 趋势，但明确没有目标带寿命；Paul 1991 测的是带内 `delta(E2/M1)`；两者均不提供本任务所需的静态 μ 或直接 g。[[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]]，A13-1/A13-6；[[paul-1991-n75-electromagnetic-properties-triaxiality]]，PA91-1--PA91-6。 | `133Ce` 的 g/μ 仍是证据缺口；不能用相对混合比反演式 (1) 的 `g_R I` 与内禀项。 |

`128Cs` 的 TDPAD `g=+0.59(1)`（Grodner 2018）可作为“g 因子是手征几何的 companion observable、且核芯转动必须显式加入”的邻核方法对照，但不能移植为 `78Br` 或 `133Ce` 数值。该对账结果是“当前 corpus 中没有目标核 direct μ/g record”，不是“世界上从未测量”。后续应优先检索 ENSDF/Stone 汇编、原始 hyperfine/TDPAD 论文并建立独立 source 页。

## Provisional Reasoning

1. 式 (1) 是粒子—转子磁偶极算符的实验室分解；它把核芯转动和准粒子极化分开，但 `g_R`、有效 `g_s`、阻塞和 projection 仍需同一模型计算。
2. 式 (2)--(3) 给出四态磁矩张量的完整一阶对角结构。负号关系是 `mu_chi p=0` 的条件极限；八极—手征相干可用 `mu_chi p` 量化。
3. 式 (4)--(7) 说明 `K=1/2` 的退耦分岔如何随 `beta3` 增强，并给出它对静态 μ 的显式、可替换代理项。真正的 `b_0` 需从 parity-projected PRM、blocked-HFB 或 GCM 波函数计算。
4. 运行默认扫描在 `beta3=0` 时得到 `symmetry_residual=0`；`beta3=0.25`、`I=11/2`、barrier=`0.5` 时得到 `delta_mu_12=0.06354 mu_N`、`delta_mu_34=-0.04737 mu_N`、残差 `0.01617 mu_N`，且残差等于 `4 mu_chi p` 到 `1.7e-15` 数值误差。这只验证代码代数，不验证核素。

## Assumptions

- `chi` 与 `p` 是局部波包标签；实验室宇称和总角动量必须由投影/对角化恢复。
- `g_R=0.40`、`g_K0=0.72`、`b0_base=1.10` 等均为 synthetic 参数，不是 `78Br`/`133Ce` 拟合值。
- `K=1/2` 退耦式采用式 (4) 的相位 convention；相位反转会改变 `b_0` 符号而不改变物理可观测谱。
- Hamiltonian 只含四态隧穿、八极混合和最低阶磁矩张量，不含完整多准粒子空间、配对涨落、带交叉、内转换和 feeding。
- `M=I` 静态磁矩按 `mu_N` 计；CSV/JSON 中的能量为 MeV、磁矩为 `mu_N`。
- 工件扫描的是 odd-A 半整数 `I=1/2,...,31/2`；`78Br` 是奇奇核整数自旋，直接迁移前需改 signature/自旋网格。

## Competing Explanations

- `78Br` 的异宇称 E1 网络也可由组态混合或八极声子产生；Liu 2016 的 TPRM 对
  `f5/2-p3/2` mixing 的遗漏说明八极解释不是唯一解释。
- `133Ce` 的 MχD 候选可能受 γ-softness、Coriolis attenuation、3qp 组态和带混合控制；相对 `B(M1)/B(E2)` 不能单独确定静态手征。
- `b_0^+ != b_0^-` 也可能来自不同 blocked orbital、配对和惯量，而非八极场；必须在相同组态空间中关闭/打开 `beta3` 反事实比较。
- 静态磁矩劈裂还可由有效 `g_s` 淬灭、核芯自旋极化、时间奇场和实验态混合造成；式 (3) 的交叉项不自动等于“静态八极形变”。

## Transfer Conditions

迁移到具体核素至少需要同一带组的逐态 `I^pi`、绝对寿命和分支、偏振/混合比、`B(E1)`、`B(M1)`、`B(E2)`，以及同一 blocked-PRM/HFB/GCM 组态空间中的 `beta2,beta3,g_R,g_s` 和惯量。必须同时计算 parity projection、Coriolis mixing 和核芯极化，再比较式 (1) 的两项，而不能把相对强度直接当静态 μ。

## Failure Conditions

- 把 `78Br` 四条候选带称为已确证手征—八极四重态。
- 把式 (3) 的 `mu_chi p=0` 极限宣称为所有破缺四重态的定理，或把非零残差直接命名为静态八极观测。
- 把 `b_0` 代理式 (7) 当作从能级差唯一反演的实验常数。
- 把 `128Cs` 的 `g=0.59(1)`、邻核或相对 `B(M1)/B(E2)` 移植成 `78Br`/`133Ce` 的静态磁矩。
- 以 odd-A 半整数自旋脚本结果直接解释 odd-odd `78Br` 的整数 signature 序列。

## Falsification or Reverse Tests

1. 在同一 blocked-PRM/HFB 模型中作 `beta3=0`、仅质子混合、仅中子混合和完整混合四组计算；若 `b_0^+-b_0^-` 在关闭八极场后仍保持同样大小，八极因果不可识别。
2. 用直接静态 μ/g、partner-resolved 寿命和绝对 `B(M1)` 联合拟合；若式 (1) 不能同时描述磁矩和跃迁强度，应加入核芯极化、带混合或更大组态空间。
3. 对四态矩阵施加 `mu_chi p=0`，若实验或可信 microscopic calculation 仍要求稳定非零残差，则最小张量需要更高阶项或态序需重新定义。
4. 重复 integer-spin (`78Br`-like) 与 half-integer-spin (`133Ce`-like) 网格；若结论依赖错误的 `(-1)^(I+1/2)` 相位，退耦扫描应被判为无效。

## Open Questions

- `78Br` 是否存在可由 TDPAD、laser/hyperfine 或其它方法直接测量的目标带静态 μ/g？当前 Wiki corpus 尚未建立该原件账本。
- `133Ce` 的哪一条已知低/高自旋带最适合做 g 因子或静态矩测量，且如何与 Paul 1991 的带内 mixing-ratio 及寿命谱系对齐？
- 在 parity-projected 3qp PRM 中，`mu_chi p` 能否从四条 partner-resolved μ(I) 线性组合稳定反演，还是与 `g_s^eff`、`g_R` 完全简并？
- 八极势垒深度改变 `t_parity` 与 `b_0` 的方式是否能由同一 E1/E3/磁矩数据集区分，还是需要绝对 E3/Q3？

## Human Review

本页由 Codex 依据 `Frauendorf 2001`、`Butler--Nazarewicz 1996` 及 Wiki 中
`78Br`/`133Ce` source 页完成 self-audit，`review_status: unreviewed`。需要人工
复核的重点是：式 (4) 的 `b_0` 相位 convention、具体目标核的静态 μ/g 原始
文献检索、以及把局部四态矩阵投影到实验室态时的 `hat mu_off` 定义。任何论文
级结论都必须在获得目标核直接原件后再提升。

## Promotion or Rejection History

- 2026-10-29：`supports` 旋转系的“核芯集体项 + 准粒子内禀项”分解及对称恢复边界（Frauendorf 2001）。
- 2026-10-29：`supports` 八极静态、软振动、隧穿和宇称恢复必须分层，E1 受相消影响（Butler--Nazarewicz 1996）。
- 2026-10-29：`revises` 题目中的负号关系为 `mu_chi p=0` 的条件关系；保留非零干涉劈裂 `4 mu_chi p`。
- 2026-10-29：`supports` `K=1/2` 八极混合可导致 `b_0^+ != b_0^-` 的现象学机制；`rejects` 将合成扫描数字当作实验结果。
- 2026-10-29：`rejects` 用 `78Br`/`133Ce` 的相对跃迁比或邻核 `128Cs` g 因子填补目标核静态磁矩证据缺口。
