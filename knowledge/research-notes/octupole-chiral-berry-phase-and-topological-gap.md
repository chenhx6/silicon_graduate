---
type: research-note
title: "反射不对称手征三轴核中的 Berry 相位与拓扑量子几何态"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [octupole chiral Berry phase, Berry phase in chiral octupole nuclei, quantum geometric tensor chiral rotation]
tags: [octupole, chirality, berry-phase, quantum-geometry, topological-phase]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 research task on Berry phase and quantum geometric tensors in octupole-chiral rotating nuclei
promotion_target: chiral-octupole-coexistence
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, butler-nazarewicz-1996-intrinsic-reflection-asymmetry, liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br, simons-2005-130cs-chiral-structures, ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce, mukhopadhyay-2007-135nd-chiral-vibration-static]
---

# 反射不对称手征三轴核中的 Berry 相位与拓扑量子几何态

## Research Trigger

本任务要求把三轴非共面转动、反射不对称八极自由度和参数空间的 Berry 几何放入同一个可计算框架，并判断四重局域态、非阿贝尔联络、谱学劈裂与 E1/M1 分支是否能够成为可检验的核结构命题。候选体系包括 `78Br`、`130Cs`、`133Ce` 和 `135Nd`，但本页的数值结果是条件性 toy model，不是任一核素的参数拟合。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 推转平均场可通过离散空间—时间操作产生手征左右构型；量子恢复和有限隧穿会决定 partner splitting。 | [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]，printed pp.474–476, Sec.II.F；source claims F01-D23/F01-D24 | review source，作者理论框架；部分代数为 Wiki self-audit | 不推出某个真实核的四重简并，也不提供 Berry 曲率数值。 |
| 反射不对称核的静态形变、八极软性/振动、宇称恢复、E1/E3 和交替宇称带必须分层；E1 对质子—中子位移相消敏感，E3 更集体。 | [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]，RMP Secs.II–VII, Figs.15–33 | review synthesis，BN96-1–5 | 1996 综述不是 `A≈130` 目标核的直接 Berry 或 lifetime 测量。 |
| `78Br` 有两对 MχD 候选带和八条 E1 连接；MDC-CDFT 沿 `beta30` 的软性支持 octupole correlations，但论文把单核素 chiral–parity quartet 作为未来可观测方向。 | [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]]，PDF pp.3–5, Figs.1–6, L16-5–L16-14 | 实验事实、模型结果和作者解释分层 | 不能把 E1 网络或软势面写成已证实的四重简并或静态非零 `beta3`。 |
| `130Cs` 的 DCO/偏振、`S(I)` 和强度派生比值支持手征候选带的谱学讨论，但 Band B 无稳定 staggering，存在高自旋 crossing，缺少 partner-resolved lifetime/absolute strengths。 | [[simons-2005-130cs-chiral-structures]]，source claims SIM05-1, SIM05-3–SIM05-7 | 实验来源页；同一实验谱系 | intensity-derived ratios 不是绝对 `B(M1)/B(E2)`，不能单独裁决几何相位。 |
| `133Ce` 和 `135Nd` 的 MχD/手征振动—静态手征计算给出近简并、`B(M1)/B(E2)` 和 TAC/RPA 连接；`135Nd` partner strengths 受 DSAM、line identity 和模型输入边界约束。 | [[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]]；[[mukhopadhyay-2007-135nd-chiral-vibration-static]] | 实验与模型混合来源 | 这些来源没有计算 Berry connection/QGT，也没有证明参数空间 Chern 数。 |

## Provisional Reasoning

### 1. 四个局域极小态的条件性构造

取内禀手性坐标 `chi` 和八极坐标 `q3`，最低阶对称势可写为

\[
 V(chi,q_3;beta_2,omega)=a_chi(chi^2-chi_0^2)^2+a_3(q_3^2-q_{3,0}^2)^2+c\,chi^2q_3^2-\lambda_\omega\,omega\,chi q_3.
\]

在 `a_chi>0`、`a_3>0`、正定 Hessian 条件和 `chi_0,q_{3,0}>0` 下，`(chi,q3)=(+chi0,+q30),(−chi0,+q30),(+chi0,−q30),(−chi0,−q30)` 是四个局域井的连续极限。它们可标成 `|L,+>`,`|R,+>`,`|L,->`,`|R,->`；这里 `+/-` 是八极井的局域标签，不是实验室宇称。转动平面外的 `J` 分量、三轴四极惯量和八极坐标共同决定 `chi` 是否真正对应左/右手征，而不是标签本身。

因此“反射不对称 + 三轴非共面必然产生四个简并极小”不是一般定理。四个等能井还需要近似的 `chi→−chi` 与 `q3→−q3` 对称、足够小的线性偏置和相等的质量参数；转动频率、奇粒子阻塞、配对和高阶耦合都会解除简并。当前脚本把这四态作为局域基底，再用隧穿项计算量子恢复。

### 2. 四态 Hamiltonian 与非阿贝尔联络

令 `tau` 作用于 `L/R`，`xi` 作用于 `q3=+/-`。最小局域 Hamiltonian 是

\[
 H(R)=E_0(R)1+\boldsymbol d_\chi(R)\cdot\boldsymbol\tau+\boldsymbol d_3(R)\cdot\boldsymbol\xi+\lambda(R)\tau_z\xi_z,
 \qquad R=(\hbar\omega,\beta_2,\beta_3).
\]

`tau_x`、`xi_x` 是左右/八极井间隧穿；推转项生成 `tau_y,xi_y` 分量，允许反幺正时间反演在有限 `omega` 下破缺；`beta3` 改变反射不对称混合。对最低两条本征态组成的矩阵 `U(R)`，非阿贝尔联络和曲率写成

\[
 A_\mu=iU^\dagger\partial_\mu U,
 \qquad F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu-i[A_\mu,A_\nu].
\]

计算中使用规范不变的投影表达式 `Tr F_{mu nu}=i Tr P[partial_mu P,partial_nu P]`，以及量子度量

\[
 g_{\mu\nu}=\tfrac12\operatorname{Re}Tr[(\partial_\mu P)(\partial_\nu P)].
\]

沿闭合曲线 `C` 的 Wilson 矩阵由极分解后的重叠矩阵相乘得到，`gamma_B=-arg det W_C`，等价于用户给出的 `oint_C <psi|i nabla_R|psi>·dR` 约定。工件采用固定 `beta2=0.20` 的 `(omega,beta3)` 椭圆回路，并同时输出最低态 Abelian 参考相位。

### 3. 曲率、拓扑相位和隧穿失调

当 `omega!=0`、`beta3!=0` 且不同 Pauli 分量随两个坐标独立变化时，`d_mu d_nu` 的叉乘通常不为零，因而曲率是非零的。其物理来源是推转导致的时间反演破缺与反射不对称坐标的非交换参数响应；在曲率集中接近能隙变小时，量子度量也会变大。数值网格会直接给出这一相关性。

但“非零曲率”不等于量子化拓扑数。只有把参数面闭合成无奇点的二维曲面，确认整个占据子空间有能隙，并对 Berry 曲率积分后，才可以讨论 Chern 数；有限四态 toy 的单个回路相位一般依赖半径和模型参数。若回路包围有效简并/近简并点，Wilson 相位会改变有效两路径隧穿 `t_1+t_2 exp(i(gamma_B+gamma_dyn))`，导致

\[
 Delta E_{tun}=2|t_1+t_2e^{i(\gamma_B+\gamma_{dyn})}|.
\]

脚本中的 gap shift 和 `S_proxy(I)` 正是这个干涉式的可复现代理；它们展示机制，不是核素能级拟合。

### 4. 动力学相位与几何相位

对最低态，动力学相位为 `gamma_dyn(T)=-∫_0^T E_0(t)dt/ℏ`，随运行时间、速度和能量零点改变；几何相位 `gamma_B` 只依赖参数路径和本征态纤维，绝热极限下与路径参数化速度无关。实验中二者不会直接分离，必须用同一能谱、转动频率扫描和路径/模型反演联合约束。工件的 `berry_loop_accumulation.csv` 保存几何累积曲线，`results.json` 同时保存回路的 Wilson 相位和最低态相位；不能把两者的数值差直接宣称为实验拓扑相位。

### 5. 观测量的条件性印记

手征伙伴的 M1 通道要求保持宇称，八极诱导的 E1 通道要求改变宇称：

\[
 p_f(E\lambda)=p_i(-1)^\lambda,\qquad p_f(M\lambda)=p_i(-1)^{\lambda+1}.
\]

因此 Berry 相位若改变手征/宇称路径的相干叠加，可在 `S(I)`、伙伴间 M1 以及异宇称 E1 分支中表现为共同的相位依赖；但单一 `S(I)` 或 E1/M1 比不能反演几何相位。脚本用 `Gamma_{XL}\propto E_gamma^{2L+1}|A_{XL}|^2` 写出一个 E1/M1 分支代理，并把选择定则写入 CSV；幅度系数是 synthetic。

## Assumptions

1. 局域双井已存在，`|L/R>` 与 `|q3=+/- >` 是低维波包基底；真实 EDF/GCM 需要从 PES、重叠核和投影波函数产生它们。
2. `beta2`、`beta3` 无量纲，`hbar*omega` 使用 MeV；脚本的 Hamiltonian 系数以 keV 表示并仅作尺度示意。
3. 最低两态是一个可跟踪的近简并子空间；若 gap 闭合或与更高态强烈混合，rank-two truncation 失效。
4. 所有网格、回路半径、隧穿和 E1/M1 幅度均为 synthetic；输出不是 `78Br`、`130Cs`、`133Ce` 或 `135Nd` 的测量值。
5. “时间反演破缺”在模型中由有限推转项表示；八极反射对称的具体实现依赖轴约定和 parity/simplex 表示，不能由 Pauli 标签自动替代。

## Competing Explanations

- `S(I)` 交错或伙伴非简并可以由组态交叉、Coriolis mixing、gamma-soft 振动、配对阻塞和普通隧穿解释，不需要 Berry 拓扑。
- E1 连接和增强可能来自八极软性、局部组态混合、中心质子—中子位移相消改变或 feeding 网络；Butler–Nazarewicz 的 E1/E3 边界明确反对把 E1 当静态 beta3 的充分判据。
- `130Cs` 的高自旋 crossing、`133Ce/135Nd` 的模型输入与 DSAM line identity 可能制造相位无关的强度变化；能级近简并也可能是 band crossing。
- 在有限参数空间中 Berry 曲率可由任意复相位参数化产生；若无封闭曲面、能隙和微观不变量，称其为“拓扑相”属于过度解释。

## Transfer Conditions

转移到真实核需要：同一组态的 cranked CDFT/TAC 或 PRM/GCM Hamiltonian；随 `omega,beta2,beta3` 的自洽 PES 和惯量张量；parity/angular-momentum projection；partner-resolved lifetime、绝对 `B(E1)`,`B(M1)`,`B(E2)`、混合比和偏振；以及在不同路径半径/方向下的能隙与几何响应。最小检验应同时拟合 `S(I)`、M1/E2 比、E1 links 和 `beta3` 的独立 E3/shape 约束。

## Failure Conditions

- 把四个局域标签写成四个实验室简并能级，或把四重态动机误报成 `78Br`/`130Cs` 已确证。
- 把有限回路 Berry 相位称作量子化 Chern 数，或在能隙闭合时继续使用绝热 Wilson 结果。
- 忽略 dynamical phase、带交叉、组态混合、配对和实验 feeding，把 `S(I)` 的变化直接归因于几何相位。
- 用 E1/M1 分支代理的 synthetic amplitude 当作实验 `B(E1)`/`B(M1)` 或寿命。
- 交换奇奇核 integer-spin 与奇 A 核 half-integer-spin 的 signature/simplex 约定，或把 `beta3` 软势面当作静态梨形测量。

## Falsification or Reverse Tests

1. 在相同 microscopic input 下把 `omega`、`beta3` 的复相位项置零；若曲率、Wilson 相位和 gap proxy 不按对称性退化，则检查 gauge、有限差分和占据子空间排序。
2. 扫描回路半径、方向和速度：几何相位应对速度不敏感但对路径/包围的近简并结构敏感；动态相位应随总时间线性改变。若两者无法分离，不能声称观测拓扑印记。
3. 对真实候选带做 leave-one-observable-out 检验：只用能级和 `S(I)` 拟合后，预报 partner-resolved E1/M1/E2；若加入绝对寿命后无法同时重现，则 Berry 四态解释降级为普通组态混合/γ-soft 模型。
4. 构造 parity-symmetric `beta3=0` 与 time-reversal-symmetric `omega=0` 对照路径；若仍有不可消除的几何相位，说明模型的对称算符或相位规范实现不一致。
5. 在二维闭合参数曲面上计算曲率积分并改变网格/步长；非整数且不收敛的积分只能作为几何响应，不能晋升为拓扑不变量。

## Open Questions

- 能否从含 `beta3` 的自洽 cranked CDFT/GCM 计算中构造稳定的低能 rank-two bundle，并在实际 `78Br` 或 `133Ce` 的转动窗口保持能隙？
- `t_{chi pi}` 是否能由同一自旋下正负宇称的 partner splitting 差与 E1/M1/E2 联合约束，还是被组态混合完全遮蔽？
- `130Cs` 的 `S(I)` 和 `135Nd` 的 DSAM strengths 是否存在一个速度无关、路径可重复的几何响应组合？当前来源没有这样的测量协议。
- 八极 E3、E1 相消、γ-softness 与 Berry curvature 是否能在同一实验量矩阵中区分，还是需要独立的 Coulomb excitation / lifetime / polarization 数据？
- 真实核的反幺正手征操作 `C=T R_k(pi)`、宇称和 simplex 在含八极场的轴约定下如何共同表示，才能避免把 antiunitary phase 当成可测量 quantum number？

## Human Review

- Review scope: 本页的证据层、四井条件性构造、Berry/Wilson/QGT 公式、代理观测量和失败边界。
- Decision: `unreviewed`; Codex self-audit completed, no claim promoted to `human-reviewed`。
- Complete unresolved P0/P1 inventory: P0 — 真实核中是否存在可用于 Berry bundle 的自洽四态低能子空间，尚无 direct microscopic calculation。P1 — `78Br`/`130Cs`/`133Ce`/`135Nd` 没有路径依赖的几何相位观测；现有 E1、S(I)、近简并和 DSAM 证据不能单独补足。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-29 | created as provisional research note | absent | ai-draft / unreviewed | User requested Berry phase, QGT and reproducible four-state worker; existing `78Br`/octupole pages provide motivation but retain quartet and static-beta3 boundaries. | `chiral-octupole-coexistence` |
| 2026-10-29 | rejected strong universal claim | proposed “four degenerate minima and topological splitting are automatic” | conditional model only | Symmetry permits a four-well construction, but degeneracy requires additional potential and microscopic assumptions; finite-loop curvature is not a quantized invariant. | retain for human review and microscopic follow-up |
