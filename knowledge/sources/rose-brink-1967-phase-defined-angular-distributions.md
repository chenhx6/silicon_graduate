---
type: source
title: "Rose and Brink 1967 - Angular distributions in phase-defined reduced matrix elements"
aliases: [Rose-Brink 1967 angular distributions]
created: 2026-09-21
updated: 2026-10-07
status: ai-draft
review_status: unreviewed
source_type: theory-method-review
reading_depth: deep-read
title_original: "Angular Distributions of Gamma Rays in Terms of Phase-Defined Reduced Matrix Elements"
authors: [H. J. Rose, D. M. Brink]
journal: "Reviews of Modern Physics"
year: 1967
citation_key: rose_1967_Angular
volume: 39
pages: "306-347"
doi: "10.1103/RevModPhys.39.306"
canonical_source: "Rose & Brink, Rev. Mod. Phys. 39, 306-347 (1967)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1967_Rose et al_Angular Distributions of Gamma Rays in Terms of Phase-Defined Reduced Matrix Elements.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1967_Rose et al_Angular Distributions of Gamma Rays in Terms of Phase-Defined Reduced Matrix Elements.pdf"
raw_sha256: "8f846b61b9320de291ee5600126c5e286a0fe05968df819696816f0dc1ec57dc"
nuclei: [generic]
reactions: [generic-alignment-population]
experiments: [gamma-angular-distribution, gamma-gamma-correlation]
models: [Wigner-Eckart, statistical-tensor, multipole-expansion]
observables: [angular-distribution, gamma-width, mixing-ratio, alignment, polarization]
methods: [phase-defined-multipole-formalism, gamma-gamma-correlation]
tags: [Rose-Brink, angular-distribution, phase-convention, mixing-ratio, alignment]
---

# Angular distributions in phase-defined reduced matrix elements

## Bibliographic Record

- H. J. Rose & D. M. Brink, *Rev. Mod. Phys.* **39**, 306–347 (1967), DOI `10.1103/RevModPhys.39.306`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1967_Rose et al_Angular Distributions of Gamma Rays in Terms of Phase-Defined Reduced Matrix Elements.pdf`。

## Scope and Reading Depth

- PDF pp.306–347 (42 pages) fully read: perturbative emission/absorption starting point, time reversal, spherical-tensor phases, electric/magnetic multipole expansion, aligned-state angular distribution, widths, mixing ratios, alignment-production cases, reduced matrix elements, comments and Appendix coefficient tables.
- Not covered: later software implementations and numerical coefficient tables beyond the printed appendix.

- 2026-10-07 定向复核范围：发射/吸收起点和相位；Secs.III.B–III.E 的 printed pp.314–321；Sec.III.F 的级联 printed pp.321–326；Sec.V 中 printed pp.335–336 的约定讨论。关键公式用原 PDF 图像复核。本轮未逐表重读全部 appendix，不把原有历史全文覆盖声明当成本次新完成的通读。PDF 页号 = printed page − 305（例如 printed p.320 = PDF p.15）；下文旧 `PDF pp.306…` 数字实际指印刷页。
- 同一学习窗口追加：printed p.339 / PDF p.34 的 R_K 表 `Ji=3/2,Jf=1/2,K=2` 行、printed p.340 / PDF p.35 的 L/L′ 表注，以及 printed p.347 / PDF p.42 的 `ρ2(J=3/2,M)` 行。三页均原图复核，用于解析双解练习；本轮实际原图覆盖累计 26/42 页，仍未逐表重读全 appendix。

## Key Results

- The derivation starts from first-order perturbation theory and detailed balance/time reversal, then expands a transverse electromagnetic field into electric and magnetic multipoles with explicitly defined phases (PDF pp.306–315, Eqs.2.1–3.23).
- Interaction multipole operators `T^L_M(λ)` are chosen to share consistent rotation, Hermitian-conjugation and time-reversal properties. This makes reduced matrix elements real under the stated phase convention and gives a reproducible sign for mixed-multipole amplitudes (PDF pp.315–317, Eqs.3.17–3.24).
- For a cylindrically aligned initial state, the angular distribution is expressed as a sum of Legendre polynomials weighted by statistical tensors `B_K(J_i)`, geometry coefficients `R_K(LL'J_iJ_f)` and products of reduced matrix elements (PDF pp.316–318, Eqs.3.25–3.37).
- The mixing ratio is defined as a ratio of phase-defined reduced matrix elements of the lowest-order competing multipoles (Eq.3.39). Its magnitude is related to the square root of partial γ widths, but its sign is a physical relative phase only within the common operator/state convention (PDF pp.318–320).
- 在初末态宇称确定且不观测 γ 偏振、对 helicity 求和时，Eq.3.41 只含偶 `K`，即使初态有 polarization 也成立。另一条充分条件是 alignment 的 `w(−M)=w(M)`，它使 `B_K(odd)=0`，不依赖是否观测 circular polarization。初态有 polarization 本身不能使 helicity-summed、definite-parity 角分布出现奇数 `K`；需按 Eq.3.32/3.40 的偏振与宇称条件判断（printed p.320 / PDF p.15, Eqs.3.40–3.41 与说明）。
- The paper treats alignment from resonant capture, particle–particle reactions and γ cascades. A γ–γ angular correlation is a product of a population tensor from the first transition and a response tensor from the second; Eq.3.73 exposes the relative phase factor for the two mixing ratios (PDF pp.321–326, Eqs.3.51–3.73).
- The authors provide single-particle, two-particle and hole reduced-matrix-element formulas and warn that switching the order of initial/final states or using effective/Siegert operators without phase mapping changes the apparent δ sign (PDF pp.327–336, Secs.IV–V).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RB67-1 | A phase-defined interaction-multipole convention makes the sign of a mixing ratio comparable between measurement and model only after operator and state-order mapping. | formalism-result | direct | PDF pp.306–320, Eqs.3.17–3.39 | true |
| RB67-2 | Aligned-state γ angular distributions factor into population/alignment tensors, geometry coefficients and reduced transition amplitudes. | formalism-result | direct | PDF pp.316–324, Eqs.3.25–3.47 | false |
| RB67-3 | γ–γ correlations require the population tensor of the first transition and the response tensor of the second; mixed multipoles carry a convention-dependent relative phase. | formalism-result | direct | PDF pp.321–326, Eq.3.73 | true |
| RB67-4 | Definite initial/final parity plus unobserved gamma polarization eliminates odd K even for a polarized initial state; independently, alignment `w(−M)=w(M)` eliminates odd `B_K` even in polarization-resolved formulas. | limitation | direct | Sec.III.E, printed p.320 / PDF p.15, Eqs.3.40–3.41 and notes | false |
| RB67-5 | For definite-parity states, an allowed photon multipole must satisfy `abs(Ji−Jf)≤L≤Ji+Jf` with `L≥1`; electric and magnetic multipoles carry parity factors `(-1)^L` and `(-1)^(L+1)`, respectively. Thus same-parity transitions admit M1/E2/M3… and opposite-parity transitions E1/M2/E3… where the angular-momentum triangle permits them; `0↔0` single-photon gamma decay is excluded. | selection-rule | direct | Sec. III.E, printed p.320, following Eqs.3.40–3.41 | true |
| RB67-6 | The Eq.3.39 mixing ratio is the higher multipole's phase-defined interaction RME divided by `√(2L+1)`, relative to the lowest multipole normalized in the same way; initial `J1` is on the left in this definition. Its modulus is the square root of the corresponding partial gamma-width ratio. | convention-boundary | direct | Sec.III.E, printed p.319 / PDF p.14, Eq.3.39 and footnote17; printed p.318 / PDF p.13, Eq.3.29 | true |
| RB67-7 | For an axially symmetric single-gamma distribution, `B_K` limits `K≤2Ji` and `R_K` limits `abs(L−L′)≤K≤L+L′`; a higher allowed photon rank need not create an observable higher angular rank. Cascade formulas use their own population/response tensors. | formalism-result | direct | printed p.317 / PDF p.12, Eq.3.28; printed p.318 / PDF p.13, Eq.3.32 note(iii); printed p.319 / PDF p.14, Eq.3.36; printed p.326 / PDF p.21, Eqs.3.71–3.73 | true |
| RB67-8 | The integrated gamma-rate relation sums squared normalized multipole amplitudes, while the angular distribution contains interference products; a width/lifetime alone cannot recover the relative sign. | formula-and-limitation | direct | printed p.318 / PDF p.13, Eq.3.29; printed p.319 / PDF p.14, Eqs.3.35–3.39; printed p.320 / PDF p.15, Eqs.3.41–3.43 | true |
| RB67-9 | The long-wavelength expansion and powers of k can motivate a lower-multipole approximation, while the two-multipole angular-distribution formula explicitly assumes only two components contribute; allowed higher ranks are not exactly forbidden by that approximation. | approximation-boundary | direct | printed pp.313–314 / PDF pp.8–9, Eq.3.12; printed p.318 / PDF p.13, Eq.3.30; printed p.321 / PDF p.16, before Eq.3.47 | true |
| RB67-10 | For `Ji=3/2→Jf=1/2`, the appendix tabulates K=2 coefficients `R2(11)=0.5000`, `R2(12)=0.8660`, `R2(22)=−0.5000`; for Ji=3/2 the folded population coefficients are `ρ2(M=1/2)=−2.0000`, `ρ2(M=3/2)=2.0000`. These are formalism coefficients, not measured angular data. | tabulated-theory-coefficient | direct | Appendix angular-distribution coefficients, printed p.339 / PDF p.34, Ji=3/2 Jf=1/2 K=2 row; statistical-tensor coefficients, printed p.347 / PDF p.42, Ji=3/2 K=2 row | true |
| RB67-11 | Linear x′/y′ intensities use coherent differences/sums of the two helicity amplitudes; the CG ordering, rotation exponent and magnetic `q^π` factor are part of the amplitude identity and cannot be replaced by a helicity-summed angular response alone. | experimental-criterion | direct | printed p.316 / PDF p.11, Eq.3.24, intervening polarization paragraph and unnumbered WE relation after Eq.3.25; printed p.312 / PDF p.7, footnote7 | true |
| RB67-12 | In the explicitly synthetic Ji=3/2→Jf=1/2 reconstruction, fixed high-M population lets ideal linear polarization separate the RB δ=0/√3 angular branches; alternatively, pure E1/high-M and pure M2/low-M give identical pointwise direction/polarization intensity matrices. These are task-derived conditional counterexamples, not author-reported experiments or a statement about complete photon states. | our-inference | indirect | Premises: printed p.316 / PDF p.11, Eqs.3.24–3.25; printed p.317 / PDF p.12, Eq.3.28; printed p.318 / PDF p.13, Eq.3.29; printed p.347 / PDF p.42, ρ2 table | true |
| RB67-13 | For the explicitly synthetic 2+→2+ case with all M1/E2/M3/E4 retained and unknown aligned diagonal populations, the complete normalized pointwise direction/polarization matrix has four shape coefficients. An exact interior seed gives rank4 for five inputs and a fraction-changing local one-dimensional equal-observable family; fixed population gives local rank3 but no global uniqueness. These are our reconstruction and IFT application. | our-inference | indirect | premises: printed p.316 / PDF11 Eq.3.24 and polarization/WE paragraph; p.317 / PDF12 Eq.3.28 and rotation-product identity; p.319 / PDF14 Eq.3.36; p.324 / PDF19 Eqs.3.62–3.63 and same-initial-state companion paragraph | true |
| RB67-14 | 在固定RB约定、完整M1/E2/M3/E4模型内，正交involution U保持S及四个方向/偏振二次型；给定严格正、非等权且已知布居，两个四成分全非零、分别局部rank3的向量仍有相同pointwise强度而不同γ份额。此为73-check精确全局pair与未观测final-channel unitary解释，不是作者实验结果或所有global branches的分类。 | our-inference | indirect | premises: printed p316 / PDF11 Eq3.24 and WE ordering; p317 / PDF12 Eq3.28; p318 / PDF13 Eq3.29; p319 / PDF14 Eqs3.35–3.39; construction in Four-Multipole Direction and Polarization Reconstruction | true |
| RB67-15 | 合成3+→1+的完整E2/M3/E4、aligned population模型有六个normalized W/Δ系数；一个严格内域的6×5 Jacobian为rank5并给局部逆解。PureE2恒A6=C6=0，但isotropy或higher-response干涉可使K6消失。该41-check重构不证明全局唯一或实际spin/multipolarity赋值。 | our-inference | indirect | premises printed316/PDF11 Eq3.24; printed317/PDF12 Eq3.28; printed318/PDF13 Eq3.32 note(iii); printed319/PDF14 Eq3.36; synthetic reconstruction and exact minor in Supplement | true |

## Summary

Rose and Brink supply the phase-consistent foundation that lets angular distributions, γ–γ correlations and model electromagnetic matrix elements use a common mixing-ratio sign. The practical message is to define the interaction operators, state order, time-reversal phases, alignment tensor and convention together before comparing δ values.

## Competing Interpretations and Limitations

- Rose–Brink, Biedenharn and later experimental conventions may differ in operator phase and initial/final state order; numerical δ signs cannot be merged by magnitude-only comparison.
- Eq.3.41 要求 cylindrical symmetry、确定的初末态宇称与所述 γ 偏振求和；初态可以 aligned 或 polarized。粒子反应布居不自动破坏该式。混合宇称、观测 helicity 或非轴对称条件应回到相应一般式，不按反应类型或 polarized 标签直接判定奇 `K`。
- Effective electric operators from Siegert's theorem are equivalent only with the continuity/gauge assumptions discussed by the authors; replacing the interaction operator silently can alter phase interpretation.
- Model reduced matrix elements depend on wave functions, effective charges/g factors and particle/hole phase conventions; the formalism does not make a model assignment unique.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| RB67-AR-1 | Formal chain | Perturbation theory → multipole operators → Wigner–Eckart reduction → aligned-state tensor distribution → fitted mixing ratio. | PDF Eqs.2.1–3.47 | self-checking |
| RB67-AR-2 | Cascade chain | First γ transition creates `B_K(J)` population tensor; second transition contributes `R_K` and δ; product gives γ–γ correlation. | PDF Eqs.3.65–3.73 | self-checking |
| RB67-AR-3 | Convention transfer | Convert operator phase, state order, parity and alignment assumptions before comparing Hamilton/Taras/DCO values. | PDF pp.318–327, 335–336 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]], [[taras-1971-phase-defined-polarization-formulas]] and the convention audit for Hamilton 1969.
- New reusable rule: every stored δ claim must retain the source convention and state order; a sign disagreement is not a scientific conflict until the phase map is closed.
- Review state: Codex self-audited; not `human-reviewed`.

## Phase and Observable Audit

本文 `J1→J2` 表示跃迁方向，但 Eq.3.39 的 RME 写为 `⟨J1||T_L^π||J2⟩`（初态在左）。它不是去掉 photon-energy 因子后可直接与 BM 核电磁算符之比互换的量。定义：`δ_(L′π′)=[⟨J1||T_(L′)^π′||J2⟩/√(2L′+1)]/[⟨J1||T_(Lbar)^πbar||J2⟩/√(2Lbar+1)]`，`Lbar,πbar` 是本跃迁最低阶成分，其 δ 为 1。本文 multipole label `π=0/1` 表示 E/M，不能与核态的正负宇称混为一符号。定位：printed p.319 / PDF p.14, Eq.3.39。

`T_L^π` 直接定义在 Eq.3.20（printed p.315 / PDF p.10），其相位构造沿 Eqs.3.16–3.23；Eq.3.17 给出 Q/Q′/M/M′ 算符。Eq.3.23、Eq.2.23 和 Eq.3.32 note(v) 陈述 time-reversal 与实矩阵元条件，Eq.3.39 footnote17 讨论 ratio 的实数性和 Lloyd 定理；Eq.3.24 本身是发射振幅的多极展开。共同核态的任意整体相位在比值中抵消，算符与 RME 定义仍须匹配。发射/吸收比较还要回到电算符和状态顺序的映射，不能用一个脱离几何系数的符号替换。[[lange-kumar-hamilton-1982-multipole-admixtures]] printed p.122 / PDF p.4 给出在固定 KS 定义下与 RB/BR 发射级联的显式映射。

线偏振位于 printed p.316 / PDF p.11, Eq.3.24 后的两个 helicity-coherent superpositions 说明；Eq.3.25 的 `P^q(k)` 保持 q 固定，没有对 photon helicity 求和。未测偏振时的非相干求和 `P=P^(+1)+P^(−1)` 在 printed p.319 / PDF p.14, Eq.3.35 之前说明，不能代替线偏振的相干叠加。本文 p.316 没有提供可直接套给任意现代 polarimeter 的单一 `P(θ,δ)` 数值公式；实验符号和幅度需要分析轴、响应和该 setup 的标定。

宽度关系 Eq.3.29（printed p.318 / PDF p.13）在固定 `Ji→Jf`、固定 photon k 下对该跃迁各多极的平方幅度求和，不包含可恢复相对符号的干涉项。多个末态的总 γ 率须逐项用各自 k_f 求和；实验总寿命还须纳入非 γ 通道。级联 Eq.3.73（printed p.326 / PDF p.21）的第一 γ 因子含 `(-1)^(Lbar1−L1)`，其中 Lbar1 是最低阶成分；第二 γ 因子没有此额外 phase。不能让两条 γ 共用未经核对的交叉项符号。该页 Eq.3.73 印刷没有显式列出 K 求和符号；恢复完整 W(θ) 的 K 求和须注明依据 Eqs.3.47、3.71 的上下文。

## Amplitude Reconstruction for Direction and Linear Polarization

以下是把本篇规范落实为可复现计算的公式记录。`L` 是 photon multipole rank，`q=±1` 是 helicity，两者分开；核态宇称另记正/负，算符标签 π=0/1 记 E/M。

取 `a_Lπ=⟨Ji‖T_L^π‖Jf⟩/√(2L+1)`，忽略所有成分共有的 Eq.3.24 因子 `−√[k/(2πℏ)]`，由该页未编号 WE 关系得到：

`Atilde_(Mi Mf)^q = Σ_(Lπ) q^π √(2L+1) a_Lπ CG(Jf,L;Mf,Mi−Mf|Ji,Mi) d^L_(Mi−Mf,q)(θ)`。

这里整数 L 的 WE phase `(−1)^(2L)=1`；调换 CG 输入次序时仍须加对应 permutation phase，不能只交换库参数。采用 Euler `(0,θ,0)`，`khat=(sinθ,0,cosθ)`、`x′=(cosθ,0,−sinθ)`、`y′=(0,1,0)`。p.312 footnote7 定义 `d=exp(−iθJy/ℏ)`；本轮 SymPy 1.14.0 实现的指数号相反，因此使用 `wigner_d_small(L,−θ)`，并检查生成元和完整 angular response。定位：RB67-11。

令 `Sγ=Σ|a_Lπ|²`，初态 axisymmetric weights 的全 Mi 求和归一为 1。维数已归一、角平均为1的方向强度为 `W=Σ_(Mi Mf q) w(Mi)|Atilde^q|²/(2Sγ)`；线偏振强度为 `Ix′=Σw|Atilde^-−Atilde^+|²/(4Sγ)`、`Iy′=Σw|Atilde^-+Atilde^+|²/(4Sγ)`，满足 `Ix′+Iy′=W`。`W/(4π)` 才是归一单位立体角概率密度。分母由 Eqs.3.24/3.29 的共同因子与 γ 宽度相消重构，不是额外 detector response。

本轮定义 `Q_s=(Ix′−Iy′)/(Ix′+Iy′)` 作为该轴下 normalized Stokes 分量；detector analyzing power 和实验 asymmetry 需要另做响应/轴映射。`Q_s` 不能借用其它阵列的 electric-positive 标签；强度为零时该比值未定义。

### Conditional Synthetic Counterexamples

题设 `3/2+→1/2−`，RB δ=M2/E1，实振幅且高-M aligned weights `w(±3/2)=1/2`。由上述 amplitude 独立复现 Eq.3.47 后，令 `x=cosθ`：

`Ix′=[4δ²+(3+2√3δ−3δ²)x²]/[4(1+δ²)]`；`Iy′=[(δ−√3)²+4√3δx²]/[4(1+δ²)]`。

在 δ=0 与 √3 两根，Ix′/Iy′ 的曲线互换，90° 的 Q_s 分别 −1/+1；在此指定布居与理想分析轴下，偏振提供本对角分布解的区分信息。纯 M2/high-M 的 90° 极限为 Q_s=3/5，等权 Mi 则两种线偏振均1/2；不能把本例的符号推广为所有 E/M 的通用实验规则。

再比较 `(a_E1,a_M2)=(1,0), w(±3/2)=1/2` 与 `(0,1), w(±1/2)=1/2`。Eq.3.28/ρ表分别给 B2=+1/−1；直接振幅计算都得到 `W=3(1+x²)/4, Ix′=3x²/4, Iy′=3/4`。在每个 θ，其 (−,+) helicity 强度矩阵都为 `(3/8) matrix((1+x²,1−x²);(1−x²,1+x²))`，trace=W；固定方向的归一偏振矩阵需再除以 W。这证明本例的 pointwise direction/polarization 数据可能具有 population/multipolarity 联合解，不证明不同方向的场相干、γγ 关联、核末态或完整光子量子态均相同。

共同 photon k 与辐射振幅单位 A0 下两例 Sγ=1，目标 γ branch 宽度相同；实验 total lifetime 另受各 multipole 的 ICC、其它分支和非 γ 通道影响。独立同初态/已知 R2 的校准线可以检验 B2 的符号与不确定度；积分转换数据需给 Z/E/壳层与理论/实测区间。都不能由待判跃迁自身含 multipole 假设的拟合重复充当独立证据。这些条件设计和 RB67-12 的数值/矩阵等式是本轮解析推论，书中原图提供的是公式与统计系数。

## Four-Multipole Direction and Polarization Reconstruction

本节从原文振幅/统计张量重构合成 `2+→2+`，不是 RB67 直接报告的实验或该五参数实例。全部单γ候选为M1/E2/M3/E4，不截断高阶；末态Mf全部求和。固定已知对称轴，初态密度在Mi基底对角且aligned：`w0=p0,w±1=p1/2,w±2=(1−p0−p1)/2`，p0≥0、p1≥0、p0+p1≤1。四个interaction amplitudes取实数，`a=(aM1,aE2,aM3,aE4)`、`S=aᵀa>0`；M1/M3的πL=1、E2/E4的πL=0，仍保留Eq.3.24的magnetic q^π。

原文前提的locators：printed p.312 / PDF7 footnote7旋转指数；p.316 / PDF11 Eq.3.24、线偏振段及WE ordering；p.317 / PDF12 Eq.3.28和rotation-product identity；p.318 / PDF13 Eq.3.29及3.32 note(iii)/(v)；p.319 / PDF14 Eq.3.36；p.320 / PDF15 alignment规则；p.324 / PDF19 Eqs.3.62–3.63与同初态其它branch校准段。

Eq.3.28给 `B0=1,B1=B3=0`，`B2=√70(2−4p0−3p1)/14`、`B4=√14(1+5p0−5p1)/14`；两布居坐标的Jacobian determinant是 `5√5/2≠0`。初态J=2限制K≤4；axisymmetry只留N=0，alignment消odd K。对角helicity products的右磁数为0，offdiagonal为±2，故normalized全方向强度恰有

`W=1+A2 P2(x)+A4 P4(x)`，`Δ=Ix′−Iy′=C2 P2^(m=2)(x)+C4 P4^(m=2)(x)`，`x=cosθ`。

这里关联Legendre `P_K^(m=2)=(1−x²)d²P_K/dx²`，不是 `[P_K]²`。`P2^(m=2)=2−2P2`，`P4^(m=2)=2+10P2−12P4`；计数须用矩阵值基底 `{P0 I,P2 I,P4 I,P2^(m=2)σx,P4^(m=2)σx}`，不能称这五个标量函数跨通道独立。归一化角平均W=1固定constant项，剩四个形状系数。

在meridian分析轴 `x′=eθ,y′=eφ`，helicity强度矩阵为 `H=matrix((W,−Δ);(−Δ,W))/2`；U=V=0。已知分析轴旋转生成的U由原Q和旋角决定，不新增独立系数。normalized Stokes Q=Δ/W一般是有理角函数，不是同一有限Legendre多项式。原矩阵是 `H(q,k;q′,k)`；没有比较跨方向场相干、γγ关联或核末态观测。绝对未归一矩阵还有整体尺度S。

### 完整四成分二次型

从CG/Racah与rotation-product reduction得到 `A_K=B_K(aᵀR_Ka)/S`、`C_K=B_K(aᵀT_Ka)/S`，K=2,4。下表按amplitude次序(M1,E2,M3,E4)；R_K、T_K均实对称，T_K是本任务的线偏振差系数定义，不是原文直接印出的独立T表。全部matrix entries由独立factorial-d展开与CG/Racah式核对，trace、Δ和helicity对角元差的符号残差均为0。

| (L,L′), symmetric lower triangle implied | R2 | T2 | R4 | T4 |
|---|---|---|---|---|
| (1,1) | `-sqrt(70)/20` | `-sqrt(70)/40` | `0` | `0` |
| (1,2) | `sqrt(6)/4` | `-sqrt(6)/24` | `0` | `0` |
| (1,3) | `2*sqrt(105)/35` | `sqrt(105)/210` | `-sqrt(21)/14` | `-sqrt(21)/168` |
| (1,4) | `0` | `0` | `sqrt(5)/2` | `-sqrt(5)/40` |
| (2,2) | `3*sqrt(70)/196` | `3*sqrt(70)/392` | `-4*sqrt(14)/49` | `sqrt(14)/147` |
| (2,3) | `4/7` | `1/7` | `5*sqrt(5)/14` | `sqrt(5)/168` |
| (2,4) | `2*sqrt(105)/49` | `-sqrt(105)/294` | `-5*sqrt(21)/98` | `-3*sqrt(21)/392` |
| (3,3) | `-3*sqrt(70)/140` | `sqrt(70)/140` | `-sqrt(14)/28` | `sqrt(14)/84` |
| (3,4) | `5*sqrt(6)/28` | `-5*sqrt(6)/84` | `-3*sqrt(30)/28` | `sqrt(30)/420` |
| (4,4) | `-17*sqrt(70)/196` | `-5*sqrt(70)/196` | `9*sqrt(14)/196` | `sqrt(14)/196` |

其中 `F_K(LL′)=(−1)^(1+L−L′−K)√[5(2L+1)(2L′+1)] W(2,2,L,L′;K,2)`，末尾W是Racah coefficient。`R_K(LL′)=F_K CG(L,L′;1,−1|K,0)`；`T_K(LL′)=−(−1)^πL F_K CG(L,L′;−1,−1|K,−2)√[(K−2)!/(K+2)!]`。R来自Eq.3.36及相同normalization，T与表格是coherent-polarization重构；所有符号以本段分析轴为准。

### 实际局部联合解及校准边界

在M1非零chart取 `a=(1,u,v,z)`，输入顺序(u,v,z,p0,p1)，输出(A2,A4,C2,C4)。种子 `(1/2,1/3,1/4,1/4,1/4)` 的w0=1/4、w±1=1/8、w±2=1/4均严格正；四成分均非零，S=205/144，γ份额为(144,36,16,9)/205。直接完整振幅重构后两强度多项式最高次均为4，没有先删K6/8。

该点4×5 Jacobian在代数域 `QQ<√6+√105>` 的exact rank=4。例如删除p1列后的4×4 minor为

`-9527662382013/24339939627587500 - 87678121707*sqrt(70)/2433993962758750 + 1700102168757*sqrt(6)/24339939627587500 + 30257551998*sqrt(105)/1216996981379375`，exact非零。

将kernel的p1分量归一到1，其约略显示为 `(-1.48209373406,1.43824262351,2.29085159845,−0.738945813644,1)`；对应四个γ份额的导数约为 `(−0.306986787166,−1.11782717340,0.639408853843,0.785405106721)`。这些小数仅展示方向，判零、rank、kernel和份额导数使用exact代数。

rank4使系数映射为局部submersion；隐函数定理给同一四系数的局部一维smooth level set。其tangent改变γ份额，且内域布居/非零振幅由连续性保持，所以附近存在完整pointwise方向/偏振强度相同、multipole fractions不同的精确解。沿kernel直线走有限步通常只一阶不变，不能把该直线上的点称为精确第二解。整体辐射幅度可另归一到相同S以保持相同目标γ宽度；这不自动约束ICC、其它branches或total lifetime。43项检查由主代理复现，属L2重构，不是L4数据拟合。

固定已知p0/p1时，同一点4×3 amplitude-only Jacobian为rank3，选择非零minor可局部逆解；没有证明global唯一。在isotropic p0=1/5,p1=2/5处B2=B4=0，所有同S混合都W=1、Δ=0，直接反证“校准布居即保证所有点唯一”。若另加Gaussian布居或低阶混合ansatz，变量维数会变，但这是额外模型条件，不能冒充独立测量或普遍选律。

新增合成companion设计：假定同一2+初态另有到独立已知0+的γ branch；triangle/parity使该branch是唯一L2、pure E2。Eq.3.36给 `R2c=−√70/14`、`R4c=−2√14/7`，均非零。其两角系数可解 `B2=A2c/R2c,B4=A4c/R4c`，继而 `p0=1/5+2A2c/5−3A4c/10`、`p1=2/5+2(A2c+A4c)/5`。这是未给定、未实测的设计条件，要求相同event/gate/feeding布居、axis、响应/有限角度修正、覆盖与covariance；从未知mixed目标fit出的布居仍是共享假设。原文同初态多branch思路定位p.324右栏末段。

### 已知非等权布居下的精确全局多解

进一步在固定RB convention与上述完整四γ自由振幅模型内，找到实正交involution。令 `rU=√(3/35),sU=√(32/35)`，次序仍为M1/E2/M3/E4：

| U row / column | M1 | E2 | M3 | E4 |
|---|---|---|---|---|
| M1 | 0 | rU | 0 | sU |
| E2 | rU | 0 | sU | 0 |
| M3 | 0 | sU | 0 | −rU |
| E4 | sU | 0 | −rU | 0 |

exact检查 `Uᵀ=U,U²=I` 和 `Uᵀ M U=M`，M依次为I、R2、T2、R4、T4。因此a与b=Ua保持同S和四个radiation二次型；任意共同的aligned布居给同一W/Δ。它在固定算符约定内改变multipole amplitudes与fractions，并不依靠修改population或有限直线步。

主证书取 `a=(1,1/2,1/3,1/4)`、`b=(rU/2+sU/4,rU+sU/3,sU/2−rU/4,sU−rU/3)`。两向量四分量均严格正且非零，S=205/144；已知非等权布居仍为p0=p1=1/4，B2、B4非零，两解各自的projective amplitude Jacobian都为rank3。

| γ multipole | Fraction for a | Fraction for b (exact) | b approximate display |
|---|---|---|---|
| M1 | 144/205 | `(396+144√6)/7175` | 0.104352 |
| E2 | 36/205 | `(944+384√6)/7175` | 0.262663 |
| M3 | 16/205 | `(1179−144√6)/7175` | 0.115160 |
| E4 | 9/205 | `(4656−384√6)/7175` | 0.517825 |

lifted证书 `D=aaᵀ−bbᵀ` 为非零rank2、trace0，并满足 `Tr(R2D)=Tr(T2D)=Tr(R4D)=Tr(T4D)=0`。两个Gram矩阵均positive rank1；四个normalized coefficient residuals exact为0。主代理复现73项检查，零失败。故已知非isotropic population、两个局部rank3解仍能有离散全局多解；这里只给该involution与pair，不分类所有global branches。

补充简例：纯M1 `a=(1,0,0,0)` 映为 `b=(0,rU,0,sU)`，即E2/E4 coherent组合，份额3/35和32/35；sameS与全部R/T同样保持。此简例便于读图，主证书的四成分全非零使论证不只依靠边界。

物理解释从p316 Eq3.24/WE得到θ=0的q+ projected links：`e_m=ΣL √(2L+1)a_L CG(2,L;Mf=m−1,q=1|2,m)`，m=(−1,0,1,2)。其link矩阵满足 `C_linkᵀ C_link=5I`，`C_link U C_link^−1=diag(−1,+1,−1,+1)`。保留magnetic q^π后，q− links遵循m→−m reflection；两个helicity的initial-row/final-column矩阵均满足 `Aq(Ua,z)=−Aq(a,z) Zf`，`Zf=diag[(-1)^Mf]`。共同final-channel unitary在同方向求和未观测Mf时消去；tensor旋转将它携至方向相关Zf(R)。不同方向的Zf不必相同，因此没有全光子态/cross-direction coherence等价声明。

在共同k/辐射尺度下同S给同目标γ宽度（p318 Eq3.29）；ICC、E0、其它branches和total lifetime未被证为相同。较高多极的long-wave、strength上限或微观模型可增加条件，这些信息没有由合成题给出。本例不证明实际核素中高阶显著，不建立新level/transition或L4。

### 合成C：六个角/偏振系数的局部逆解与零点边界

本节仍是本任务L2重构，非RB67作者直接列出的实验。对题设 `3+→1+` 保留全部E2/M3/E4，实RB amplitudes `a=(1,u,v)`；已知轴、aligned diagonal布居 `w0=p0,w±1=p1/2,w±2=p2/2,w±3=(1−p0−p1−p2)/2`。初态与末态Mf遍历完整，M3保留q^π。来源premises为p316 Eq3.24/WE、p317 Eq3.28/rotation product、p318 rank/real-amplitude规则、p319 Eq3.36。

完整求和后W/Δ均为六次even多项式，没有预删K8：`W=1+A2P2+A4P4+A6P6`、`Δ=C2P2^(m=2)+C4P4^(m=2)+C6P6^(m=2)`。关联Legendre定义和meridian分析轴沿前文，normalized P=Δ/W。B2=`√3(−9p0−8p1−5p2+5)/6`，B4=`√22(3p0−2p1−10p2+3)/22`，B6=`√33(−21p0+14p1−7p2+1)/66`，三个population coordinates独立。

为使结果不只留在临时code，本节给六个exact forward functions（S=1+u²+v²），次序与输入(u,v,p0,p1,p2)一致：

`A2 = (9*p0 + 8*p1 + 5*p2 - 5)*(63*u**2 - 10*sqrt(35)*u*v - 24*sqrt(14)*u + 85*v**2 - 8*sqrt(10)*v + 48)/(336*(u**2 + v**2 + 1))`

`A4 = (3*p0 - 2*p1 - 10*p2 + 3)*(7*u**2 - 54*sqrt(35)*u*v - 110*sqrt(14)*u + 81*v**2 - 18*sqrt(10)*v - 88)/(924*(u**2 + v**2 + 1))`

`A6 = (21*p0 - 14*p1 + 7*p2 - 1)*(45*u**2 - 14*sqrt(35)*u*v - v**2 + 32*sqrt(10)*v)/(528*(u**2 + v**2 + 1))`

`C2 = -(9*p0 + 8*p1 + 5*p2 - 5)*(63*u**2 - 10*sqrt(35)*u*v + 18*sqrt(14)*u - 75*v**2 - 2*sqrt(10)*v - 72)/(1008*(u**2 + v**2 + 1))`

`C4 = -(3*p0 - 2*p1 - 10*p2 + 3)*(70*u**2 - 36*sqrt(35)*u*v + 55*sqrt(14)*u - 270*v**2 + 81*sqrt(10)*v - 220)/(27720*(u**2 + v**2 + 1))`

`C6 = (21*p0 - 14*p1 + 7*p2 - 1)*(45*u**2 + 2*sqrt(35)*u*v + 15*v**2 - 32*sqrt(10)*v)/(15840*(u**2 + v**2 + 1))`

seed `(u,v,p0,p1,p2)=(1/2,1/3,1/4,1/4,1/4)` 的所有w严格正、三成分非零，S=49/36，B2=−√3/12、B4=3√22/88、B6=−5√33/132均非零。6×5 Jacobian在`QQ<√10+√14>` exact rank5；rows(A2,A4,A6,C2,C4)的minor为

`-9*(-23338289430*sqrt(14) - 5244034414*sqrt(35) + 14018306057*sqrt(10) + 62121460520)/699996265041920`，exact非零（approx1.52959×10⁻⁴仅展示）。因此这个5-output子映射有smooth local inverse，全部六coefficients在模型内可局部约束两个relative amplitudes与三个population变量。没有从determinant大小推断实验精度，没有证明global唯一；仍需响应/统计covariance与discrete Jπ/模型候选比较。41项由主代理复现（约5.50s）。

边界控制：pureE2 u=v=0时A6=C6恒0，所有population下成立，因L2+L2<6；此点full-map rank4。给定calibrated响应下nonzero K6可排除pureE2，但zero K6不是逆命题。isotropic p0=1/7,p1=p2=2/7、u=1/2,v=1/3仍有higher amplitudes，却W1/Δ0，此点rank3。B6非零也可由R6 response干涉抵消A6：

`A6/B6=−√33[45u²−14√35uv−v²+32√10v]/[264(1+u²+v²)]`。

u=1/2时two real nonzero E4 roots为 `v=16√10−7√35/2±2√(750−140√14)`，A6 exact为0，C6不必为0。仅未见A6不能删M3/E4；population消失与response cancellation要分开。该spin组合的local rank结论校准前例2+→2+的五参数/四coefficients连续解：它们各自依赖给定的Ji/Jf与模型条件，不推广为所有spin组合的统一排解结论。

## Human Review Triage

### P0

- `RB67-P0-1`: Do not compare or average δ signs across source pages until Rose–Brink/Biedenharn/operator/state-order conventions are explicitly mapped.

## Extracted Pages

- Methods/observables: [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]]。

- Day8 方法依赖回链：[[spin-parity-assignment]] 保存 spin/parity/multipolarity 的观测与共享输入审计；[[multipole-mixing-ratio]] 保存三例全候选及 convention 边界。
