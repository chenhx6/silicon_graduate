---
type: research-note
title: "α 团簇分子态与平均场八极形变：微观等价、投影重叠与拓扑边界"
date: 2026-10-29
category: research-notes
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
aliases: [alpha clustering vs mean-field octupole boundary, alpha-cluster-octupole-overlap]
tags: [alpha-clustering, octupole, mean-field, molecular-states, e1-e3-transitions]
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, gaffney-2013-pear-shaped-rn-ra, bernard-2016-144ba-sccm-octupole, warda-2011-actinide-cluster-radioactivity-gogny, robledo-2010-bcp-d1s-octupole-ra-ba, nomura-2020-ra-th-gogny-d1m-octupole]
created_from: "跨来源综合与可复现点团簇—平均场投影重叠边界模型"
---

# α 团簇分子态与平均场八极形变：微观等价、投影重叠与拓扑边界

> 本页是 2026-10-29 的研究型综合记录。`status: ai-draft` 表示本轮交付完成；`review_status: unreviewed` 和 `reasoning_status: provisional` 保留科学自审边界，不表示用户已逐条审核。数值工件是可复算的 surrogate model，不是反对称化 Gogny/Skyrme HFB 或 GCM 的生产计算。

## Research Trigger

反射不对称性在低能核结构中有两种常被并置的语言：一是具有非零 `β3` 的变形平均场，二是两个相对运动的核团簇或分子态。两种语言都可以给出交替宇称、增强 E3 和有限 E1，但它们预设的自由度、反对称化方式、渐近边界和实验判据并不相同。本任务的目标是建立一个可复用的边界：在哪些层面二者是同一个电多极算符的不同表示，在哪些层面必须保留为竞争的波函数图像。

结论先行：

1. **算符层等价成立。** 在质心系，点团簇的有效 E1 电荷与平均场的质子—中子质心位移都来自同一个平移不变偶极算符；轴向点团簇的 `Q3` 也可以映射到同一个实验室 E3 算符。
2. **态空间层等价不自动成立。** Brink 波函数预选了片段、相对坐标和 Pauli 允许的 Wildermuth 通道；HFB/GCM 波函数预选了密度、配对、形变坐标和投影。只有在相同 EDF、粒子数/宇称/角动量投影、Pauli 处理、norm kernel 与渐近匹配下计算重叠，才可以讨论定量等价。
3. **`β3` 与 α 通道是不同拓扑坐标。** 低能八极集体运动通常是紧致密度上的奇形变坐标；α 衰变或分子态通道要求颈变细、局域片段粒子数趋近整数并接到大 `R` 渐近区。二者可由同一多维势能面连接，但不能由 `β3` 一个数互相替代。
4. **轻核到锕系不存在单一质量阈值。** 轻核中相对距离、Pauli 允许的低阶通道和低密度表面可使 α 片段局域化显著；`212Po/224Ra` 中 Coulomb 能量、重叠核子交换和配对/惯性使同一 α 通道更像衰变坐标，而低能八极谱学可由紧致平均场的静态形变或软振动描述。`224Ra` 的实验静态样八极证据并不等于其基态有一个可测的 α 预形成概率。

## Grounded Evidence

### 1. 微观八极驱动与平均场边界

Butler–Nazarewicz 综述将反射不对称的单粒子起源归于费米面附近的相反宇称轨道对，特别是 `Δl=Δj=3`。可迁移的例子包括 `π d5/2↔h11/2`、`ν f7/2↔i13/2`（A≈144）以及 `ν f7/2↔i13/2`、`ν g9/2↔j15/2`（A≈224）；这些是平均场八极不稳定性的驱动条件，而不是 α 片段存在的直接证据。见 [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]] 的 Sec.III.A、Figs.4–8 与其 `BN96-4`。

同一综述明确区分静态八极极小、八极软振动、隧穿/宇称恢复和分子态；均值场的非零 `β3` 是内禀 order parameter，实验室态必须经过宇称和角动量恢复。这个区分见该源的 Secs.III.C/F、IV–VII（`BN96-3`）。因此，`β3≠0` 不能直接当作分子态振幅，`B(E3)` 也不能单独给出静态或 α 结构的唯一判定。

Robledo 等的 BCP/Gogny 计算在 Ra 与 Ba 中给出核素依赖的八极势能面：`222Ra` 的 D1S 双阱势垒约 1.5 MeV，`144Ba` 的 D1S 势阱约 0.7 MeV；这些是特定 EDF、约束和零点修正下的模型输出，不能等同实验势垒或宇称劈裂。见 [[robledo-2010-bcp-d1s-octupole-ra-ba]] 的 `RO10-1/2`（PDF p.4 Fig.1、PDF p.10 Fig.9）。Nomura 等以 Gogny D1M 势能面映射到 sdf-IBM，得到 `224Ra/226Th` 八极关联增强而 `220Th` 仍较软，这反驳“整个锕系都处于同一深双阱”的简化说法；见 [[nomura-2020-ra-th-gogny-d1m-octupole]] 的 `NO20-1/2`（PDF pp.2–3, Fig.1）。

### 2. 直接 E3、E1 与静态/动态边界

Gaffney 等用 REX-ISOLDE/MINIBALL/GOSIA 对 `220Rn` 与 `224Ra` 直接拟合 E1/E2/E3 矩阵元。其 Table 1 给出 `0+→3−` E3 矩阵元约 `810(50)` 与 `940(30) e fm^3`，并得到 `Q3≈2180(130)` 与 `2520(90) e fm^3`；`Q2`、`Q3` 在测量的自旋范围近似稳定，`224Ra` 的八极集体性更强、更相干。见 [[gaffney-2013-pear-shaped-rn-ra]] 的 `GA13-1/2/3`，PDF pp.200–203, Figs.3–5, Tables 1–2。

该实验同时给出关键的证据边界：E2/E3 矩阵元可以与静态四极—八极分布或四极核上的八极振动相容，单独不能区分两者（`GA13-6`，PDF p.202）。因此 `224Ra` 的“静态梨形”是多观测量和模型系统学支持的作者解释，不是从一个 E3 数值反演出的无模型事实。

`144Ba` 的投影 GCM 计算先作轴对称四极/八极约束 HFB，再恢复 `J`、宇称、`N`、`Z` 并解 HWG 组态混合；其二维 GCM 计算给出 `0+↔3−` E3 矩阵元 `0.460 e b^(3/2)`、向下 `B(E3)=25 W.u.`。它同时报告沿 `β3` 的软性、有限基底和缺少 cranking/配对响应的限制。见 [[bernard-2016-144ba-sccm-octupole]] 的 `BE16-D26-001/004/007`（PDF pp.1–4, Eqs.1–5, Fig.1, Table I）。这提供了平均场—投影—GCM 的真实计算链，但不是 α 通道重叠的直接计算。

### 3. 团簇通道与高阶形变边界

Warda–Robledo 用轴对称 Gogny-D1S HFB 约束 `Q20`、`Q30` 和颈算符，把 `222/224/226Ra` 的 14C 通道以及 Th 的 O 通道描述为超非对称裂变路径。对 `224Ra`，低形变基态 `β3≈0.14` 与颈缩后接近 Pb 样密度片段的路径是不同区域；作者没有给独立微观 α/14C 预形成概率。见 [[warda-2011-actinide-cluster-radioactivity-gogny]] 的 `WR11-1/2/3/4`（PDF pp.1–5, 10–13, Eqs.2–7, Fig.10）。这直接支持“八极坐标与团簇衰变坐标可在同一 HFB 多维 PES 上相连，但不相同”的边界。

### 4. 证据矩阵

| 主张 | 支持证据 | 反证/限制 | 竞争解释 | 当前状态 |
|---|---|---|---|---|
| `Δl=Δj=3` 轨道对可驱动八极平均场 | BN96 Sec.III.A, Figs.4–8；NO20 PDF p.3 | 轨道近简并不证明静态极小或 α 片段 | γ-soft、配对、组态混合 | 确证为机制，静态结论需模型/实验 |
| `B(E3)` 是强八极集体性证据 | GA13 Table 1/2；BE16 Table I | 单个 E3 不能区分静态形变和软振动 | 投影软势、振动态、形状混合 | 确证为观测层，形状归因为作者解释 |
| α 点团簇与平均场可有同一 E1 算符 | 质心修正代数推导；BN96 Sec.II.B | 内部极化、交换、反对称化改变振幅 | 单粒子占据相消、IVGDR 混合 | 算符层确证，态层暂定 |
| `224Ra` 的低能八极坐标等于 `220Rn+α` 相对坐标 | 强 E3/Q3 与 Warda Q30 共同提供背景 | 无统一 EDF 下的 norm kernel/通道匹配；Warda 是衰变路径 | 紧致梨形平均场、八极振动 | 不成立为普适等价 |
| 重核 α 局域化随 A 减弱 | Coulomb/Pauli 量纲诊断与 Warda 颈路径 | `alpha_loc` 非标准观测量，未拟合数据 | 配对、惯性、外部势垒也改变通道概率 | 暂定趋势，需微观通道计算 |

## Provisional Reasoning

### 1. Brink 波函数、Wildermuth 条件与平均场基底

取核心 `C=(A_c,Z_c)` 和 α `(4,2)`，相对坐标

\[
\mathbf R=\mathbf R_\alpha-\mathbf R_c,
\qquad A_c\mathbf R_c+4\mathbf R_\alpha=0.
\]

一个 Brink 型内禀态可写为

\[
|\Phi_C(\mathbf R)\rangle
 =\mathcal A\{\,|\phi_c\rangle |\phi_\alpha\rangle
 \chi_{nL}(R)Y_{LM}(\widehat R)\,\},
\]

其中 `𝒜` 是全体核子的反对称化算符。Wildermuth 条件把相对振子量子数限制为

\[
G=2n+L=\sum_{i\in\alpha}(2n_i+\ell_i),
\]

以避免 α 核子占据核心已经使用的壳层。`G` 不是一个由质量数唯一决定的常数：它随振子长度、核心组态和壳层填充定义变化。当前工件采用常见的示意值 `G=4,8,18,18` 对应 `12C+α`、`16O+α`、`208Pb+α`、`220Rn+α`；这些值只作通道基线，不能冒充逐核微观反对称化计算。`

平均场态可以写为

\[
|\Phi_{\rm MF}(q)\rangle=|\Phi_{\rm HFB}(\beta_2,\beta_3,\kappa,\ldots)\rangle,
\]

其中 `q` 还可含配对、颈密度、质子/中子八极矩和其它约束。投影态为

\[
|\Psi^{J\pi}_{\rm MF}(q)\rangle
 =\frac{P^J P^\pi P^N P^Z|\Phi_{\rm MF}(q)\rangle}
 {\sqrt{\langle\Phi_{\rm MF}|P^J P^\pi P^N P^Z|\Phi_{\rm MF}\rangle}}.
\]

宇称投影 `P^π=(1+π\hat Π)/2`；角动量投影为标准三 Euler 角积分

\[
P^J_{MK}=\frac{2J+1}{8\pi^2}\int d\Omega\,
D^{J*}_{MK}(\Omega)\hat R(\Omega).
\]

### 2. 重叠矩阵元：原始量、归一化量与 GCM 度规

用户要求的矩阵元可严格写成

\[
\mathcal O_{C,MF}^{J\pi}(R,q)
 =\left|\langle\Psi_C(R)|P^\pi P^J|\Psi_{\rm MF}(q)\rangle\right|^2.
\]

但是非正交 Brink 基底和投影 HFB 基底中，单独的模平方不是概率。可复用的归一化定义是

\[
\widetilde{\mathcal O}_{C,MF}^{J\pi}
 =\frac{\left|N_{C,MF}^{J\pi}(R,q)\right|^2}
 {N_{C,C}^{J\pi}(R,R)N_{MF,MF}^{J\pi}(q,q)},
\]

\[
N_{C,MF}^{J\pi}(R,q)=
\langle\Phi_C(R)|P^\pi P^J P^N P^Z|\Phi_{\rm MF}(q)\rangle.
\]

若要得到某个 GCM 本征态的团簇含量，还需把 `N` 与 Hamiltonian kernel 放进 HWG 方程并对所有 `R,q` 求和；单个 `\widetilde{\mathcal O}` 不能称作 `S_α` 或 `P_α`。相位、粒子数、角动量、宇称和 center-of-mass 约定必须在两套基底中一致。

工件中的 surrogate 采用两个集体坐标高斯核，给出

\[
\widetilde{\mathcal O}_{\rm toy}
 =\exp[-\tfrac12((R-R_{MF})^2/\Sigma_R^2+
(\beta_{3,C}-\beta_{3,MF})^2/\Sigma_3^2)]
 \frac{1+\pi K_\Pi}{2}K_J,
\]

其中 `K_Π` 是两 lobe 的反射核，`K_J=exp[-J(J+1)/(2J_0^2)]`。它只检查投影符号、极限和参数趋势；没有计算 Slater determinant overlap、Pfaffian、norm-kernel 本征值或 HWG 谱。

### 3. E1：严格的质心修正和两种语言

在质心系，点团簇的轴向偶极矩为

\[
D_{0,\,C}(R)
 =e\left(Z_cR_c+2R_\alpha\right)
 =e\frac{A_cZ_\alpha-4Z_c}{A}R.
\]

这就是用户给出的 `e(A1 Z2-A2 Z1)R/A`，其中取 `(A1,Z1)=(A_c,Z_c)`、`(A2,Z2)=(4,2)`。翻转内禀轴只改变符号。完整核的平移不变算符是

\[
\hat D_z=e\frac{N}{A}\sum_p z_p-e\frac{Z}{A}\sum_n z_n
 =e\frac{NZ}{A}(R_{p,z}-R_{n,z}).
\]

如果密度真的可分成两个固定 `Z/A` 的点片段，二式代数等价；在平均场中，轨道占据、质子—中子极化和配对决定 `R_p-R_n`。因此“同一个 E1 算符”不等于“同一个波函数”。

最重要的轻核反例是 `16O=12C+α` 和 `20Ne=16O+α`：两个片段均有 `Z/A=1/2`，所以点团簇 `D0_C=0`，但 `c3` 不为零。这说明 E1 可以因荷质比相消而消失，而 E3 仍很强；真实核中的有限尺寸、内部同位旋极化和反对称化会破坏严格零点。

平均场/液滴耦合可用一个明确约定的原始尺度表示为

\[
D_{0,MF}^{\rm raw}=C\,Z A^{1/3}\beta_2\beta_3,
\qquad C=\frac{9r_0}{4\pi},\; r_0=1.20\,\mathrm{fm}.
\]

`C` 必须带 `e fm` 单位；该式只是几何—液滴尺度。单粒子壳修正、质子—中子相对极化和 IVGDR 相消应另作为有符号的 isovector response 计算，不能用一个没有来源的“普适相消百分比”代替。

### 4. E3：点团簇和平均场的条件对账

对轴向点团簇，令

\[
c_3=Z_c(4/A)^3-2(A_c/A)^3,
\qquad Q_{3,C}=2e c_3R^3.
\]

在 `K=0` 转子约定下，工件采用

\[
B(E3;3^-\to0^+)=\frac{7}{16\pi}Q_{3,C}^2,
\qquad
B(E1;1^-\to0^+)=\frac{3}{4\pi}D_{0,C}^2.
\]

平均场比较量取

\[
Q_{3,MF}=\frac{3}{\sqrt{7\pi}}Ze(r_0A^{1/3})^3\beta_3,
\qquad B(E3)=\frac{7}{16\pi}Q_{3,MF}^2.
\]

这些公式只在相同 `K=0`、初末态方向、矩阵元与内禀量约定下对账；实验 `B(Eλ)` 还包含初态简并、方向和真实波函数混合。E3 增强较少受 E1 那样的单粒子相消影响，故更适合作为八极集体性观测量，但仍不能独自决定静态或分子解释。

## Assumptions

1. 四个系统都用同一个 `r0=1.20 fm`、对称核物质 `ρ0=0.16 fm^-3` 和 `kF=1.33 fm^-1`，便于比较而不是拟合具体核半径。
2. `β2,β3`、相对距离增量、波包宽度和 `G_wildermuth` 是示意输入；没有把任何一个输入称为实验测量。
3. `alpha_loc` 定义为诊断量：

   \[
   \alpha_{loc}=e^{-(k_F\sigma_R)^2/2}
   e^{-0.75(R_c/R)^8(A/224)^{1/3}}
   e^{-V_C/E_F},
   \quad V_C=1.44\frac{2Z_c}{R}\;\mathrm{MeV}.
   \]

   第一因子描述有限宽度，第二因子是 Pauli 重叠惩罚，第三因子是 Coulomb/费米能标度；它不是标准 spectroscopic factor。
4. 重叠扫描只在 `(R,β3)` 二维空间，未引入颈算符、`β5/β7`、三轴性、配对坐标、质子—中子分离、连续谱或 particle-number projection。
5. `alpha_channel_weight_surrogate=clip(1.5 alpha_loc,0,1)` 仅把 locality 诊断映射成图表用权重，绝不等同 `P_α`。

## 可复现数值结果

运行

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/alpha-clustering-octupole/alpha_clustering_octupole_model.py
```

输出目录见 [README](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/alpha-clustering-octupole/README.md)。四行主结果如下；`D0_mf_raw` 是未施加 isovector 相消的原始尺度，所有 `B(Eλ)` 是公式代理量。

| 系统 | `R` (fm) | `α_loc` | `D0_cluster` (e fm) | `D0_mf_raw` (e fm) | `Q3_cluster` (e fm³) | `Q3_mf` (e fm³) | `O²(0+)` | `O²(3−)` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `16O=12C+α` | 5.802 | 0.495 | 0.000 | 0.312 | −293.0 | 17.0 | 0.402 | 0.270 |
| `20Ne=16O+α` | 6.079 | 0.413 | 0.000 | 1.890 | −431.3 | 39.8 | 0.403 | 0.277 |
| `212Po=208Pb+α` | 9.765 | 0.0784 | 4.053 | 1.722 | −3516.5 | 984.3 | 0.729 | 0.139 |
| `224Ra=220Rn+α` | 9.799 | 0.0442 | 4.200 | 11.575 | −3564.7 | 3050.7 | 0.487 | 0.321 |

从主表可直接检查：

- `16O/20Ne` 的点团簇 E1 严格为零，但 E3 不为零；这是荷质比相消的代数极限，不是“所有真实 E1 都为零”。
- `212Po/224Ra` 的点团簇几何 `D0` 约 4 e fm，而平均场原始尺度由 `β2β3` 取值决定，二者不自动匹配；真实 E1 还需微观有符号核和极化。
- `alpha_loc` 从轻核到重核下降，反映本模型放入的宽度、Pauli 和 Coulomb 因子；它没有资格被解释为实验 α 含量。
- 投影 surrogate 的 `O²` 不按 `A` 单调，因为它同时取决于 `R`、`β3`、波包宽度和宇称/J 因子。这正是“拓扑边界不是单一质量数”的数值示范。

## 拓扑边界：何时应称分子态，何时应称平均场八极集体

把描述空间写为

\[
\mathcal M=(R,\beta_2,\beta_3,q_{neck},\Delta_p,\Delta_n,
N_{\alpha\text{-channel}},\rho_p-\rho_n).
\]

建议用四个可检查的边界变量，而不是一个标签：

1. **局域化边界 `L_R`：** `R-R_contact`、密度双峰性、片段粒子数和 `alpha_loc` 是否共同显示两个局部核团。只有距离大、颈薄和片段粒子数同时出现时，才是分子/衰变通道候选。
2. **Pauli/Wildermuth 边界 `G`：** 相对运动必须落在允许的 `G` 子空间；低阶禁戒通道不能以一个较大的 `β3` 代替。
3. **八极集体边界 `C_3`：** `Q3` 或 E3 矩阵元随自旋是否稳定，宇称带劈裂是否随自旋塌缩，PES 沿 `β3` 是深阱、浅双阱还是单阱软面。这些量适合判定紧致集体形变/振动，不能单独判定 α 片段。
4. **投影重叠边界 `O^{Jπ}`：** 在同一规范下的归一化 norm kernel 是否在物理 `R` 区间出现稳定峰，并且对网格、投影点数、EDF、配对和颈约束收敛。单一 intrinsic overlap 峰不够。

在这套边界下：

- `20Ne` 可同时有强 α 分子态语言和平均场形变语言；二者的联系需要在允许的 `G=8` 通道上投影，而不能仅比较 `β3`。
- `212Po` 的 `208Pb+α` 更自然地是 α 衰变/外部通道坐标；低能八极谱和 α 预形成需要不同的边界条件、惯性和渐近匹配。
- `224Ra` 的 `Q3`、交替宇称和静态样转动证据支持紧致八极集体，但 Warda 的大 `Q30` 颈路径仍是另一条超非对称裂变/团簇衰变路线；二者只有通过多维 HFB/GCM norm kernel 才可定量桥接。

## Competing Explanations

1. **平均场静态梨形：** 非零 `β3` 极小、稳定 `Q3`、交替宇称劈裂快速减小和投影后旋转谱共同支持；它不要求存在预形成 α。
2. **八极软振动/形状混合：** 大 E3 可来自软势面和零点涨落；`B(E3)` 与单一 `β3` 或 α 分子态不一一对应。Gaffney 的 `GA13-6` 是直接边界。
3. **α/重团簇分子态：** 相对距离、Wildermuth 允许通道、片段化密度、颈坐标和渐近衰变通量共同支持；不能用低能 `β3` 或 E1 相消单独证明。
4. **E1 单粒子相消/IVGDR 混合：** 小 E1 可由质子—中子极化相消产生。`144Ba/146Ba` 的直接 E3 中心值接近而 E1 显著不同，说明 E1 不可作为八极强度的一对一代理；见 [[octupole-cluster-dipole-dynamics-conditional-equivalence]] 的条件推导及 [[bucher-2017-146ba-direct-octupole]] 的 E1/E3 原件边界。

## Transfer Conditions

跨质量区转移结论前至少需要：

- 同一 EDF、配对处方和 oscillator length；
- 相同 `P^N P^Z P^π P^J` 投影与 Euler/gauge 网格收敛；
- 同一 center-of-mass、E1/E3 算符和 intrinsic-to-laboratory 归一化；
- 相同 Brink 片段密度、Wildermuth `G`、Pauli 投影和匹配半径；
- `Q20/Q30/Q50/Q70`、颈密度、片段粒子数、惯性和零点修正的联合记录；
- E1、E3、宇称能级、分支/寿命和角动量依赖的共同 holdout。

若只在一个 `β3` 点比较两种 `D0`，不满足这些条件；若仅比较 E3 中心值，也不满足。

## Failure Conditions

- 把点团簇 `D0=0`（`16O/20Ne`）升级成真实核 E1 必为零；
- 把 `D0_mf_raw` 当作实验 intrinsic dipole，或报告一个没有有符号微观来源的相消百分比；
- 把 `O²_toy`、`alpha_loc` 或 `alpha_channel_weight_surrogate` 称为 spectroscopic factor、`P_α` 或实验预形成概率；
- 把 `224Ra` 的低能 E3/交替宇称带等同于 `220Rn+α` 大距离通道；
- 把 `G_wildermuth` 示意值当作所有核心构型的唯一 Pauli 条件；
- 用 `B(E3)` 单独裁决静态形变、八极振动或 α 分子态；
- 忽略投影 norm kernel 的小本征值、相位规范、粒子数投影和网格收敛。

## Falsification or Reverse Tests

1. 在同一 Gogny/Skyrme EDF 中建立 `(Q20,Q30,Q50,Q70,q_neck)` 网格，同时保存质子/中子密度、片段粒子数、配对张量和 ATDHFB 惯性。
2. 对每个网格点构造 Brink `C+α` 基底，施加同一个粒子数、宇称和 `J` 投影，给出 `N_{C,MF}`、norm-kernel 本征谱和匹配半径依赖。
3. 在 `16O,20Ne,212Po,224Ra` 上同时拟合 `E1/E3`、交替宇称能级、`Q3(I)` 和 α/重团簇衰变通量；预先固定 E1/E3 之外的 holdout。
4. 对 `D0` 做质子/中子过渡密度分解；如果 E1 过零而 `O²` 不增强，则反驳“偶极相消必然意味着团簇预形成增强”。
5. 逐步放开 `β5/β7` 和颈自由度，比较势能降低、惯性变化和最小作用量路径；只降低局部 PES 不能证明半衰期或 `P_α` 增强。
6. 改变 oscillator length、Wildermuth `G`、Pauli projector 和 parity/J 网格，要求物理结论在合理范围内稳定；否则将结果降级为模型依赖。

## Open Questions

- 是否存在同一 EDF/同一投影规范下，把 `20Ne` 的分子基底与 `224Ra` 的紧致八极 GCM 基底放在统一 HWG 空间中的数值实现？
- `224Ra` 的 `Q3`、交替宇称和 α 衰变通道在一个多维 norm kernel 中的相对权重能否由独立的衰变分支和低能 E1/E3 holdout 约束？
- 对 `212Po`，Pauli 允许的 `G=18` 通道与 `208Pb+α` 外部渐近波函数的匹配半径、配对和惯性如何共同影响通道形成振幅？
- `144,146Ba` 中 E3 相近而 E1 相差很大，能否用有符号质子/中子过渡密度与 cluster projected kernel 同时解释，而不把 occupancy 模型结果写成实验事实？
- 是否能用 `Q3(I)` 的自旋稳定性、颈密度和投影重叠构造可跨核素的“紧致八极—团簇通道”相图，而不是按 `A` 设硬阈值？

## Human Review

本轮完成 Codex source self-audit；没有发生用户逐条 claim 审核，因此保留 `review_status: unreviewed`，不写 `human-reviewed`。重点复核入口是：

- `P0`: 点团簇与平均场的 E1/E3 归一化、初末态方向、`B(Eλ)` 简并因子；`
- `P0`: 任何由 surrogate overlap 或 `alpha_loc` 推出真实 `P_α` 的措辞；
- `P1`: Gaffney `Q3` 与作者静态/动态解释的分层；
- `P1`: Wildermuth `G` 和重核通道的 oscillator/核心组态约定；
- `P1`: 将 Warda 的 Q30/颈路径与低能 `β3` 连接时的惯性、零点和渐近边界。

## Agent Self-Audit Triage

### P0

1. **No microscopic overlap claim.** 本页只给出归一化重叠的定义和二维 Gaussian surrogate；没有声称生产 HFB/GCM 数值。若删除这个边界，读者可能把 `O²` 当 `P_α`。
2. **No static-shape exclusivity from E3.** `GA13-6` 明确保留静态与振动竞争；E3 的直接观测和作者解释分开。
3. **No universal E1 cancellation percentage.** E1 是有符号、质子—中子和单粒子占据敏感的矩阵元；本工件的 `D0_mf_raw` 只是几何尺度。

### P1

- `G_wildermuth` 的数值是本工件的示意输入，精确论文用途需要回到具体核心组态、振子基和 Pauli 约定。
- `Q3` 的点团簇系数、转子约定和实验 `B(E3)` 的初态简并必须在后续共同 producer 中逐项统一。
- `alpha_loc` 的 A 趋势是模型构造出的 diagnostic，不是已发表实验系统学。

## Promotion or Rejection History

2026-10-29：创建受控研究笔记；把“微观等价”限定为平移不变算符和投影 kernel 的条件等价，拒绝把 `β3`、E3 或 surrogate overlap 直接解释为 α 预形成概率。后续若获得同一 EDF 下的 Brink–HFB norm kernels，需追加数值结果并重新评估 `reasoning_status`；在此之前保持 `provisional`。

## Sources

- [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]] — `Δl=Δj=3` 八极轨道、静态/振动/分子模型框架，Sec.III.A/C/F。
- [[gaffney-2013-pear-shaped-rn-ra]] — `220Rn/224Ra` 直接 E1/E2/E3 矩阵元与静态/动态解释边界，PDF pp.199–204, Tables 1–2, Figs.3–5。
- [[bernard-2016-144ba-sccm-octupole]] — Gogny-D1S 轴对称 HFB、对称性恢复、二维 GCM 和 E3 计算，PDF pp.1–4, Eqs.1–5, Table I。
- [[warda-2011-actinide-cluster-radioactivity-gogny]] — Gogny-HFB `Q30`/颈约束的超非对称裂变和团簇通道，PDF pp.1–5, 10–13, Eqs.2–7, Fig.10。
- [[robledo-2010-bcp-d1s-octupole-ra-ba]] — Ra/Ba 八极势能面和 EDF 依赖，PDF p.4 Fig.1、p.10 Fig.9。
- [[nomura-2020-ra-th-gogny-d1m-octupole]] — D1M 势能面映射和锕系核素依赖，PDF pp.2–3, Fig.1。
- [[bucher-2017-146ba-direct-octupole]] — `144/146Ba` E3 相近、E1 差异和 occupancy-sensitive SCCM 解释。
- [[octupole-cluster-dipole-dynamics-conditional-equivalence]] — 点团簇 E1 零点、E3 条件匹配及其非唯一性分析。

## Reproducible Artifacts

- [README](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/alpha-clustering-octupole/README.md)
- [Python model](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/alpha-clustering-octupole/alpha_clustering_octupole_model.py)
- [Systematics CSV](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/alpha-clustering-octupole/systematics.csv)
- [Overlap scan CSV](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/alpha-clustering-octupole/overlap_scan.csv)
- [Results JSON](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/alpha-clustering-octupole/results.json)
- [Chart data JSON](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/alpha-clustering-octupole/chart_data.json)
