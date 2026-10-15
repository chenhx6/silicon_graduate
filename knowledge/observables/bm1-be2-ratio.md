---
type: observable
title: B(M1)/B(E2) 比值
aliases: [B(M1)/B(E2), magnetic-to-electric transition ratio]
created: 2026-07-01
updated: 2026-10-15
status: active
review_status: unreviewed
observable_kind: reduced-transition-probability-ratio
symbol: B(M1)/B(E2)
units: source-dependent
tags: [electromagnetic-transition, band-structure]
---

# B(M1)/B(E2) 比值

## Definition

约化磁偶极跃迁概率与约化电四极跃迁概率之比，用于比较同一能级或带结构中的磁、集体四极成分。

## Formula and Conventions

单位和所选 M1/E2 跃迁必须随数值一并记录；不同文献的归一化不能直接混用。

### Difference from the multipole mixing ratio `δ`

`B(M1)/B(E2)` is a quotient of reduced transition probabilities and normally carries units such as `μN²/(e²b²)`. It is not the dimensionless same-transition mixing ratio `δ²`. For one identified transition containing M1 and E2 photon components,

`δ² = Tγ(E2)/Tγ(M1)`.

In the common-unit Krane–Steffen convention, the same-transition conversion is `δ² = [0.835 Eγ(MeV)]² × B(E2)[e²b²]/B(M1)[μN²]` (LKH82 printed p.121 / PDF p.3, Eqs.2.1–2.6). The `Eγ²` factor comes from the E2/M1 photon-rate ratio. The signed `δ` also retains the relative reduced-matrix-element sign; B values alone give only its magnitude. This conversion requires the same initial/final state, transition energy, and specified M1/E2 decomposition. A ratio formed from spin-row B values alone cannot be converted to `δ²` if the row does not identify the relevant transition and `Eγ`.

For the `135Nd` MU07 Table I, the printed columns are indexed by initial spin and list a lifetime, `B(M1)`, and `B(E2)`, without row-specific transition energies or final spins. The matched-spin `B(M1)/B(E2)` quotients are therefore derived strength summaries, not transition-specific mixing ratios. See MU07-5/11 and LKH82-1 for the source boundary and rate definition.

Alwaleedi 2013 由相对分支强度推导该比值时使用 E2/M1 mixing ratio `δ=0`。保留其它输入不变，Equation 5.6 给出

`R(δ) = R(0) / (1 + δ²)`。

因此在 `|δ|≤0.5` 时，δ=0 近似相对真实 `R(δ)` 最多高估 25%；若以 `R(0)` 为分母，差值最多为 20%。δ 的符号不影响这一幅值修正，但对偏振、相位和完整多极混合判断仍有意义。引用由该方法得到的数值时必须显式写出 δ=0 假设。

## How It Is Obtained

由分支比、mixing ratio、跃迁能量和必要的寿命/内转换信息推导，或由模型计算。由 branching intensity 单独反演时，未知 δ 是显式系统假设，而不是可以省略的细节。

## Diagnostic Use

可检验组态和 signature partner 模型描述。

## Model Dependence

模型值依赖 g 因子、内禀四极矩、波函数和配对。

### Shared-amplitude identifiability example

For a fixed parent spin and a specified M1/E2 transition pair, suppose a model has a shared dimensionless transition-amplitude factor `c(I)`:

`⟨f||M(M1)||i⟩ = c(I) m(I)`, `⟨f'||M(E2)||i⟩ = c(I) q(I)`.

Under the standard reduced-probability definition, the common `|c(I)|²/(2I+1)` factor cancels in `B(M1)/B(E2)`. Thus a stable ratio alone cannot exclude a shared change in the absolute transition scale. This is a constructed algebraic identifiability example; it is **not** evidence that a particular paper has this factorized mechanism. Test such alternatives with partner-resolved absolute strengths, transition identity, feeding/branch controls and independent geometry or configuration observables.

In the `135Nd` Day10 preview, the five matched-spin quotients and cross-band quotient-of-quotients are deterministic combinations of the same Table-I B values; they do not add independent evidence or a measured same-transition `δ²` ([[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-7).

## Failure Modes and Ambiguities

实验比值与模型比值相等不构成唯一结构证明。不要把 `|δ|≤0.5` 导致的 25% 最大相对高估，与内转换系数反演中约 25% 的实验不确定度混为一谈；两者来源和分母不同。

## Examples

`131Xe` yrare 17/2- 的实验值 1.27(14) 与 TPRM 1.27 一致；yrast 17/2- 的 2.54(4) 明显偏高。

### Ratio staggering can be denominator-driven

Suzuki *et al.* report that in their measured candidate sequences of `103Rh` and `104Rh`, `B(M1)` decreases with spin while weak odd-even variation appears in `B(E2)`, so the observed `B(M1)/B(E2)` staggering is attributed to the E2 denominator rather than to an M1 staggering signal. This is a source-specific lifetime-based example, not a universal mechanism; the paper measured only one member of each proposed doublet and assumed pure M1 for the ΔI=1 strengths (SU08-6/7/8/13).

[[lv-2021-tilted-precession-135nd]] 比较 D1 带内及 TiP1→D1 的 `B(M1)out/B(E2)in` ratios 与 QTR。618.3/566.0 keV TiP1→D1 links 的实验 ratios 为 0.28(10)/0.24(14)；其中 566.0 keV 与另一个 566.8 keV connecting transition 应保持区分。Agreement 是模型一致性证据，不构成 TiP 的单独充分判据。

[[nomura-2022-questioning-wobbling-ibfm]] 比较四核的计算与既有实验 `B(M1)out/B(E2)in`。IBFM 常给出比 wobbling 支持数据更强的相对 M1 成分，但不同核/自旋的 agreement 不一致；该比值依赖所选 E2/M1 operators 和波函数，不能单独裁决 band identity。

## Sources

- [[mukhopadhyay-2007-135nd-chiral-vibration-static]]
- [[suzuki-2008-lifetimes-103rh-104rh]]
- [[lange-kumar-hamilton-1982-multipole-admixtures]]
- [[chakraborty-2023-131xe-wobbling-origin]]
- [[lv-2021-tilted-precession-135nd]]
- [[nomura-2022-questioning-wobbling-ibfm]]
- [[alwaleedi-2013-band-structures-131ce]]

## Evolution Log

- 2026-07-01：记录 `131Xe` 两条 13/2- 序列的区分用途。
- 2026-07-04：加入 Lv 2021 `135Nd` TiP1→D1 relative-M1 comparison。
- 2026-07-05：加入 Nomura 2022 的 IBFM relative-M1 comparison 与模型依赖。
- 2026-07-27：固化 Alwaleedi 2013 的 δ=0 假设、`R(δ)` 修正及 25%/20% 误差口径。
- 2026-10-08：加入一个明确标作 Codex algebraic counterexample 的 shared-amplitude cancellation例子，并链接 MU07 Table I 的 Day10 uncredited derived-ratio audit；没有声称 MU07/其它来源拟合了该因子。
- 2026-10-09：区分有量纲 `B(M1)/B(E2)` quotient 与同一跃迁的 rate-defined `δ²`，并记录 MU07 Table I 缺少逐行跃迁能和末态自旋，不能仅按同初始自旋换算。


## 同母态radiative比值的抵消条件

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1（printed121/PDF3 Eqs2.1–2.6）的radiative-rate与B定义给同gamma的δ。若比较的是**同一母态的两条不同γ**，一条d含M1/E2成分，另一条c的E2 photon fraction为fE2,c，则在matching corrected photon-yield与该截断模型下：

\[
\frac{B(M1;d)}{B(E2;c)}=
\kappa\frac{E_c^5}{E_d^3}\frac{I_{\gamma,d}}{I_{\gamma,c}}
\frac{1}{(1+\delta_d^2)f_{E2,c}}.
\]

E用MeV，B商用μN²/(e²b²)。SIradiationprefactors给kE2=1.225186722e13 s⁻¹/(MeV⁵ e²b²)、kM1=1.758366177e13 s⁻¹/(MeV³ μN²)，κ=kE2/kM1=.696775642；sqrtκ=.834730880，舍入成LKH的.835。用源中舍入κ=.835²引入约.0645%的数值变化，只是常数舍入，不是实验冲突。不同单位下κ数值必须重算：把keV直接当MeV会因净E²产生10⁶错误。

令Tγ,d为d的总photon rate，则M1 photon partialrate是Tγ,d/(1+δ²)，c的E2 rate是fE2,c Tγ,c。若两线观测强度确满足同一population/selection下`Iγ,j ∝ Tγ,j/λtotal`，共同λtotal和population消去，**不需要**该parentτ或未计其它分支库存来求这个component比；同样不把ICC重复乘进已是photonrate的ratio。ICC/其它decaychannel会影响λtotal，但该分母共同取消。与之相对，absoluteB、从totalbranch转photonbranch或不同母态间比较仍需要相应τ/α/branch信息。上文一般的“必要寿命/转换信息”必须按这个scope判断，不能一律要求或一律省略。

这种抵消不认证source Iγ已经满足matchedangle/gate/efficiency条件，也不提供δ或fE2,c。source-label M1+E2与E2不等于已测δ0/纯度1。Fixed fE2,c=1时，δ0只给conditional R0上界，非零δ使R下降；允许fE2,c改变就不再有同一个无条件上界。不能把这个两gamma商当同一跃迁的δ²，也不能因τ取消而把结果叫absoluteB。

### 误差和归一化

对sourcequotedmarginals作独立、一阶控制，`d lnR=dId/Id−dIc/Ic−3dEd/Ed+5dEc/Ec`。共同intensitynormalizer的梯度严格抵消；共同energygain却留下2倍相对变化。真实error需用完整jointΣ和component/response nuisance传播，不能用每列error替代Cov。小crossover强度的倒数尤其非线性；弱分母的线性±σ不是完整confidence region，也不从未知原counts补Gaussian/Poisson似然。

[[lv-2025-136pr-tac-covariant-density-functional]] LV25-31的D4八对给直接应用：[[level-scheme-reconstruction]]相应小节保存同parent/blankM/quotederror与71checks。示例只说明何时可从同parentγ强度求conditionalcomponent商；尚未取得逐线δ/纯度/实际response/Σ，没有给新绝对强度、实验显著性或mode裁决。
