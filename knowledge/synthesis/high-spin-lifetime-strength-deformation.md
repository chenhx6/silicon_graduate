---
type: synthesis
title: "High-spin lifetimes, transition strengths and deformation"
aliases: [高自旋寿命跃迁强度形变综合]
created: 2026-09-21
updated: 2026-10-08
status: ai-draft
review_status: unreviewed
scope: high-spin-lifetime-strength-deformation
confidence: medium
sources: [kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc, mukhopadhyay-2007-135nd-chiral-vibration-static, mukhopadhyay-2008-136nd-transition-rates, petrache-2006-near-degenerate-chiral-misinterpretation, petrache-2018-chiral-bands-even-even-136nd, lange-kumar-hamilton-1982-multipole-admixtures]
tags: [high-spin, lifetime, transition-strength, deformation, evidence-map]
---

# High-spin lifetimes, transition strengths and deformation

## Question and Scope

This synthesis follows the evidence chain from level identity and line shape to lifetime, transition strength, alignment and deformation interpretation.

## Evidence Matrix

`coincidence gates → Doppler shift/line shape → stopping and feeding model → τ → B(M1)/B(E2), Qt → configuration/deformation interpretation`

The chain is explicit in Jensen, Mukhopadhyay 2007/2008, Petrache, Herzan and the lifetime-method review. The uncertainty is carried by stopping powers, side feeding, gate choice, branching normalization and configuration assignment.

## 从寿命、分支到约化强度

本节区分来源直接定义、作者报告值和我们的条件性重构。率/矩阵元定义来自 [[lange-kumar-hamilton-1982-multipole-admixtures]]，printed p.121 / PDF p.3, Eqs.2.1–2.6；原表与实验假设来自 [[mukhopadhyay-2008-136nd-transition-rates]] 的 MU08-4/5。两者分别提供 formalism 和同一次 DSAM 实验，不构成两次寿命测量。

### 率、单位与矩阵元

LKH82 Eq.2.2 在其 Gaussian 电磁算符约定下给出

`Tγ(XL)=8π(L+1)/{L[(2L+1)!!]²ℏ} × [Eγ/(ℏc)]^(2L+1) × B_G(XL)`。

Eq.2.3a：`B(XL;Ji→Jf)=|⟨Jf||M(XL)||Ji⟩|²/(2Ji+1)`。初态在右；率已按此 B 定义归一化，不能把由率求出的 B 再除一次 `2Ji+1`。本文添加 `G` 下标只为提醒单位系统，原文没有此下标；直接把 SI 电荷/磁矩填入原式会漏掉转换因子。对这里的 E2/M1，SI 形式分别补 `1/(4πε0)` 和 `μ0/(4π)`。

用现代 CODATA 2022 常数重构，并采用 `Eγ` 为 MeV，得到

`Tγ(E2)=K_E2 Eγ⁵ B(E2)`，`K_E2=1.2251867220×10¹³ s⁻¹ MeV⁻⁵ (e²b²)⁻¹`；

`Tγ(M1)=K_M1 Eγ³ B(M1)`，`K_M1=1.7583661766×10¹³ s⁻¹ MeV⁻³ μN⁻²`。

可复现的系数关系为 `K_E2=(4π/75) αfine×10⁴/[ℏ(MeV·s)(ℏc(MeV·fm))⁴]` 与 `K_M1=(4π/9) αfine/[ℏ(MeV·s)(mpc²(MeV))²]`。`1 b=100 fm²`，故 `1 b²=10⁴ fm⁴`；`μN=eℏ/(2mp)` 为 SI 核磁子。这些现代数值是我们的单位重构，不是 LKH82 直接印出的绝对寿命系数；数字位数记录常数约定，不代表实验精度。

以 ps 表示 mean lifetime 时，`C_E2=10¹²/K_E2=0.0816202120`，`C_M1=10¹²/K_M1=0.0568709756`。常见 `0.0816` 与此舍入相容；`0.05697` 不是本组现代常数的简单舍入，也不能据 LKH82 p.121 给它补上出处。复用历史 B 值须保留原作者数值，现代重算另列。宽度 `Γγ=ℏTγ` 的单位是能量，不能与 `s⁻¹` 率混写。

### B↑、B↓与同一算符的反向归一

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-13由p121 Eq2.3a/b/c、p122 Eq2.11和state-reversal约定重构：physical Hermitian核多极在BM/Wigner–3j归一下 `Rif=(−1)^(Ji−Jf)Rfi*`，故 `B(Jf→Ji)=(2Ji+1)/(2Jf+1) B(Ji→Jf)`。这是同一pair与同一operator；B↑/B↓不同来自各方向的初态统计平均，BM RME模相同，B不提供sign/phase。若仅改RB RME归一，bra-spin factor也随反向改变；不能把RB radiativeT的特殊adjoint/phases直接当physicalM。

合成2+↔0+ E2给B↑=5B↓，合成3/2+↔1/2+ M1给factor2，均以complex RME复共轭控制核验。MU08 Band1I18的0.14(2)e²b²按37/33给reverse16→18约0.157±0.022e²b²，BM magnitude=√518/10eb≈2.276eb；数值仅继承作者printed精度与假设。B_up=cB_down、c=37/33，因此Σ=Var(B_down) vvᵀ、v=(1,c)ᵀ，rank1/correlation+1；不能独立平均两方向或检验差异。Quoted误差只统计，原stopping/feeding/branch/ICC界不被该变换修复。

Upward nuclear strength不是upward spontaneousγ lifetime；Coulomb/其他excitation process需自身响应与kinematics，若独立实测才增加实验支持。190实质+247phase-domain检查属于Day9预习L2，正式Day9仍须独立record/card audit。

### 三种分支量及遗漏通道

令 level 总率 `Ttot=1/τ`，τ 是平均寿命。若输入为半衰期，则 `τ=T1/2/ln2`；把半衰期当 τ 会使所推 B 放大 `1/ln2`。

| 分支量 | 定义 | 对 absolute B 的意义 |
|---|---|---|
| `b_tot,j` | `Ttot,j/Ttot`，该末态支路占全部 level decays 的份额 | 普通 γ+IC 完整时，`pγ,j=b_tot,j/(1+αtot,j)` |
| `pγ,j` | `Tγ,j/Ttot`，每次 level decay 发出该 γ 的份额 | `τγ,j=τ/pγ,j`，`Tγ,j=pγ,j/τ` |
| `βγ,j` | `Iγ,j/Σk Iγ,k`，同母能级的相对 photon fraction | 通常不等于前两者；须补 photon/total-rate 归一化 |

`Iγ` 须为同母能级、已修正效率和门偏差的强度，且 γ 分支齐全。若 `b_extra` 是未计入各支路普通 all-shell IC 的额外非γ衰变份额，则

`pγ,j=(1−b_extra) Iγ,j / Σk [Iγ,k(1+αtot,k)]`。

这个式子是总率守恒的重写，不是 MU08 Table I 已明确使用的定义。`αK` 不能代替 all-shell `αtot`；E0、pair 或其它非γ贡献须进入明确的 ledger。已包含在有效非γ系数中的通道不能又作为 `b_extra` 加一次。分支中心值之和为1不能验证漏枝为零。额外未观测 photon branch 也会改变分母，不能只检验非γ通道。

### 混合 γ 的强度与共享误差

在明确只保留 M1/E2 γ、实 δ 的假设下，`t=δ²=Tγ(E2)/Tγ(M1)`，`fM1=1/(1+t)`、`fE2=t/(1+t)`。完整候选和高阶截断见 [[multipole-mixing-ratio]]；f 是 γ 率份额，不是总衰变份额。

`B(M1)[μN²]=C_M1 pγ/[τ(ps) Eγ(MeV)³(1+t)]`；

`B(E2)[e²b²]=C_E2 pγ t/[τ(ps) Eγ(MeV)⁵(1+t)]`。

若已知的是 total branch，普通 IC 完整且无额外 E0/pair，定义 `Dmix=1+αtot(M1)+t[1+αtot(E2)]`，则两式分别为 `C_M1 b_tot/(τ E³ Dmix)` 和 `C_E2 b_tot t/(τ E⁵ Dmix)`。同一 γ 的两种 B 之比可消去 τ/pγ；宽度及这些 B 都不给 δ 的相对 sign。

一般传播须用 `ΣB=JΣinput Jᵀ`。pγ 路线有 `d lnB_L=d ln pγ−d lnτ−(2L+1)d lnE+d ln fL`；在 t>0 时，M1/E2 对 t 的 log derivatives 为 `−1/(1+t)` 和 `1/[t(1+t)]`。共享 τ/branch 使两种 B 相关，t 转移率份额可产生反相关；不能将同一 t 同时作为独立 mixing error 和独立 αmix error 重复计入。t=0 的 E2 log derivative 未定义，改用 B 本身的 Jacobian 或保留端点分支。多解、上限或非Gaussian误差不能压成一个对称标准差。

### MU08 的有条件输入—公式—输出—误差核验

选用 Band 1 `Ex=6711.4 keV, 18−` 母态。下列 reported values 都属同一实验；衍生数值是本轮 L2 算术重构。

| 输入/步骤 | 数值或公式 | 输出/误差与条件 | Source locator |
|---|---|---|---|
| 母态 lifetime | `τ=0.56(8) ps` | 按 mean-lifetime convention；来自 stopping/feeding model 的 DSAM fit | MU08 printed 034311-4 / PDF p.4, Table II, Band 1 I=18− |
| 目标 transition | `Eγ=757.4 keV=0.7574 MeV`, `18−→16−` | 沿作者 B(E2) 多极赋值作纯 E2 重算；Table I 未给能量误差 | MU08 printed 034311-3 / PDF p.3, Table I, Ex=6711.4 group |
| 同母态全部印出分支 | `401.2:0.57(6); 757.4:0.24(2); 389.6:0.19(2)` | 三中心值和1；branch 是 photon/total 或含何 IC 未明，协方差未给 | 同 Table I 三行 |
| 条件性 photon fraction | `pγ=0.24` | 假定 gamma-only、印出分支齐全；不由 quoted B 反推 α | 来源输入 + 本节率守恒重构 |
| partial γ lifetime / rate | `τγ=τ/pγ=2.3333 ps`; `Tγ=4.28571×10¹¹ s⁻¹` | 不等于母态 τ，也不是新增测量 | LKH82 Eq.2.2 + mean-lifetime 定义 |
| absolute B(E2) | `0.0816202120×0.24/[0.56×0.7574⁵]` | `0.14034 e²b²`；作者报告 `0.14(2)`，保留原值 | MU08 Table II；率公式 LKH82 p.121, Eq.2.2 |
| RME magnitude | `sqrt[(2×18+1)B(E2)]` | 条件性 `2.27876 eb`；不给核态相位或 signed RME，也不等同 Qt | LKH82 p.121, Eq.2.3a |
| quoted τ/b 误差重算 | `σB/B=sqrt[(0.08/0.56)²+(0.02/0.24)²]` | 独立误差、忽略能量误差时 `σB=0.02321 e²b²`；不是完整 confidence interval | MU08 quoted inputs + 本轮一阶传播 |

中心值一致不验证 IC、feeding 或 branch 定义。若保留 τ/b correlation ρ，上行 variance 应加 `−2ρ(στ/τ)(σb/b)`；在仅固定这两个误差尺度、ρ可为−1到+1的代数范围内，σB 可从0.00835到0.03174。这不是实测误差带，也不能从作者0.02反解一个ρ并当作输入。能量误差若可得，另有 `25(σE/E)²` 及交叉协方差。

原文 stopping-power systematic 可达15%且不在 quoted errors 内；没有给其分布或共享 covariance，不能自动与统计量按独立1σ求和。Feeding 的 five-transition cascade、门控 tails 和 global-fit 条件见 MU08 PDF pp.2–3；这里没有重新拟合。Pure M1 的 ΔI=1 假设来自 MU08 PDF p.3，不能当 measured δ=0。若存在漏枝/额外非γ率，或允许 multipole fractions 未约束，这条绝对强度链仍条件化。B、Qt 与本轮回算都依赖相同 τ/branch，不能作为独立确认。

本节 `supports` 明确的输入、公式、单位与误差路径，`limits` gamma-only 归一化与视觉强度推 B 的用法；没有改变具体集体模式排序。缺 line-shape/event、response、stopping/feeding 可执行输入与 covariance，不进入 L4。

### 用不同能区检查单条回算的一致性

[[mukhopadhyay-2008-136nd-transition-rates]] 的MU08-6保存两母态四branch的gamma-only控制。Band1 I18的401.2-keV M1、757.4-keV E2条件值为0.89639μN²、0.140344e²b²，作者为0.9(2)、0.14(2)；Band2 I15的199.6-keV M1、382.0-keV E2条件值为5.23707μN²、0.553064e²b²，作者为4.4(3)、0.54(8)。全部使用各branch原归一化份额；Band1选中两枝之和0.81，不能归一到1而删去另0.19。

低能M1的条件性中心值相差19.02%，所选高能E2仅相差0.246%。百分比不构成独立显著性或作者错误判断；两计算共享原数据，IC/branch定义、covariance、能量误差与feeding/stopping未闭合。不能从这些输出差值倒求输入α、δ或ρ。若获得独立可追溯atomic coefficients，可将total-branch与photon-branch公式分别forward计算，但现代理论不能说明作者实际上采用了哪一处理。该控制检验input-chain条件，不改变集体模式排序。

### 独立理论ICC的条件forward敏感性

[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] 的dated supplement与KB08-D8-1/2/3保存五个official BrIccFO Z60输入：401.2M1 Tot0.0320(5)、389.6M1 0.0345(5)、757.4E2 0.00416(6)、199.6M1 0.204(3)、382.0E2 0.0251(4)。两高能点N6未返回，保留program Tot/warning；1.4%已含interp，NH数值/actual136Nd radius没有验证。实际web为v2.3(9-Dec-2011)，local help v2.3d只作probe。

分别把Mu08同一数字作photon g或total β，Dg(B1I18)=1.0257934、Dg(B2I15)=1.191477。各branch的`(Tγ,photon/Tγ,total−1)`为：401.2 +0.605%、757.4 −2.109%、389.6 +0.849%、199.6 +1.051%、382.0 −13.964%。使用所有同母态branches；这些是明确FO/complete-inventory假设的中心值敏感性，没有从quoted B倒推input、判定作者使用的branch定义或模式。两条warning与缺energy error/covariance/feeding/extra branches使完整uncertainty仍未闭合。五个理论lookup不是五份独立实验。

### Vacancy-model 的nominal敏感性与打印精度

[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D8-5 认证原五点的NH inputs，与旧FO分开。B1完整三个printedbranches的Dg两者均1.0257934，打印值上的rate差0；B2 Dg,FO=1.191477、Dg,NH=1.191470，photon-g定义下两支NH/FO−1≈+0.000588%，total-β下199.6支0、382.0支≈+0.009756%。固定E/mode/τ的B变化具有同倍率，不是作者实际算法或新measured B。

零差限打印精度，多位forward digits不提升输入精度。Theory spread不是独立1σ或独立实验，N6 coverage、radius、branch定义/遗漏与feeding/covariance仍保留。FO/NH vacancy不同于NP/SC penetration；现代DF不能未经mapping再叠加NP修正。Five NH只补input sensitivity，没有补齐真实event/response/完整uncertainty，Day9仍无学分预习。

## Synthesis

The `136Nd` history is a useful internal control. Early near-degenerate bands were discussed as possible chiral partners, but Mukhopadhyay 2008 found substantially different `B(E2)` values and favored distinct configurations with band mixing. Petrache 2006 reached the same methodological warning from `134Pr/136Pm` crossing, alignment and quadrupole-moment analysis. Petrache 2018 later strengthened one `136Nd` pair with partner-resolved strength while retaining four weaker candidates. These papers form a chronological evidence gradient, not contradictory labels to average.

## Model Dependence

- `Qt` and `B(E2)` are observables derived through analysis assumptions; they are stronger than energy proximity but do not directly measure an intrinsic shape.
- A band crossing can change alignment and transition strengths without establishing a phase transition.
- Magnetic-rotation and band-termination interpretations require configuration tracking and, where possible, lifetimes and moments.
- Review sources organize methods and examples; they do not add independent replications.

## Counter-evidence

Band crossings, configuration mixing and stopping/feeding alternatives can reproduce energy or strength changes without a unique shape transition.

## Open L3 questions

- Which partner-resolved strength set is minimally sufficient to reject crossing and configuration-mixing alternatives?
- Can DSAM and RDDS results be compared after harmonizing stopping, feeding and transition identity?
- Which observables distinguish a shrinking quadrupole collectivity at termination from a change of configuration?

## Limitations and Missing Evidence

The batch does not contain a complete common raw-data and response package for a reproducible L4 re-fit. Future L4 work requires an explicit data path, transition map, stopping model, uncertainty propagation and a negative/control case.

## Independent Photon Width and a Truncation Floor

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-17 连接 total parent meanτ、**某条跃迁的 absolute photon probability** b_rad 与 g=Γpair,γ=hbar b_rad/τ。它分开 photon-relative intensity、含 IC/E0 的 total pair branch、parent 全 photon 分支和同-pair photon width。若其独立 joint region 给 gmin>0，而同-pair omitted width ceiling Uom<gmin，则 retained>0、ε≤Uom/gmin；不要求 E2 单独非零。Γ 和 rate 相差 hbar，half-life 先换 meanτ。

保留 joint region 可比 marginal extremes 更强；unknown E0/nonγ 可在固定 parent τ、total branches、photon-relative fractions 下使每条 photon width 趋零。即使 αi>0，extra_i=bi−(1+αi)x fi≥0 的 formal family 仍有同样边界；per-branch b_rad,i=x fi 与 all-photon sum x 不能混用。Source p.121 Eqs.2.2–2.3、p.123 Eq.2.12、p.169 Eq.4.1 与 RB67 p.318 Eq.3.29 是公式/库存前提；截断不等式和 family 是本任务 L2 推导，没有新的实测 lifetime/ICC 或 physical prior。Rate 下限不确定 δ 的相对符号或 initial population，也不把有限时波包变化包含进角分布误差界。

## Sources

- [[mukhopadhyay-2007-135nd-chiral-vibration-static]], [[mukhopadhyay-2008-136nd-transition-rates]]
- [[petrache-2006-near-degenerate-chiral-misinterpretation]], [[petrache-2018-chiral-bands-even-even-136nd]]
- [[jensen-2001-165tm-h9-2-configuration]], [[herzan-2015-193bi-spectroscopy]], [[nolan-sharpey-schafer-1979-lifetime-measurements]]
- [[lange-kumar-hamilton-1982-multipole-admixtures]]：p.121 / PDF p.3, Eqs.2.1–2.6 的 rate/RME normalization；[[multipole-mixing-ratio]]：允许高阶、radiative fractions、δ sign 和 E0/ICC 的边界。
- [[afanasjev-1999-termination-rotational-bands]], [[walker-dracoulis-2001-exotic-isomers]]

## Self-audit

- Experimental strength, author interpretation and model calculation are kept in separate layers.
- The `136Nd` conclusion is pair-specific and does not generalize automatically to all chiral candidates.
- This synthesis is a Codex self-audit and remains unreviewed.
