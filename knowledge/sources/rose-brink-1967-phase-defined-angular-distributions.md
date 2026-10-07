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

## Human Review Triage

### P0

- `RB67-P0-1`: Do not compare or average δ signs across source pages until Rose–Brink/Biedenharn/operator/state-order conventions are explicitly mapped.

## Extracted Pages

- Methods/observables: [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]]。

- Day8 方法依赖回链：[[spin-parity-assignment]] 保存 spin/parity/multipolarity 的观测与共享输入审计；[[multipole-mixing-ratio]] 保存三例全候选及 convention 边界。
