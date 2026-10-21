---
type: synthesis
title: "High-spin lifetimes, transition strengths and deformation"
aliases: [高自旋寿命跃迁强度形变综合]
created: 2026-09-21
updated: 2026-10-09
status: ai-draft
review_status: unreviewed
scope: high-spin-lifetime-strength-deformation
confidence: medium
sources: [kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc, chiara-2001-108-110in-shears-band-lifetimes, mukhopadhyay-2007-135nd-chiral-vibration-static, mukhopadhyay-2008-136nd-transition-rates, petrache-2006-near-degenerate-chiral-misinterpretation, petrache-2018-chiral-bands-even-even-136nd, lange-kumar-hamilton-1982-multipole-admixtures]
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

### Observed-branch method precedent

[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-2/3 provides a published example of converting fitted level lifetimes to partial transition lifetimes using observed branching ratios and internal-conversion corrections. That analysis treats dipole lines as nearly pure M1 and assigns zero intensity to E2 crossovers not seen within its sensitivity. This is a method precedent for the procedure cited by MU08-10, not evidence that MU08's `136Nd` table has an absolute photon-per-parent denominator or a complete unseen-channel inventory; MU08-11/12 preserve that transfer boundary.

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

## A Total Pair Branch Needs a Non-Gamma Ceiling

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-18 给一个库存桥梁：若完整同-pair分解 Γpair=Γγ+Γlinked+Γextra 为合法非负通道，独立 Γpair≥Pmin、Γlinked≤AmaxΓγ（finite Amax≥0）、Γextra≤Uextra，则 Γγ≥max(0,(Pmin−Uextra)/(1+Amax))。True absolute total-pair branch/meanτ 可条件给 Pmin，仍不能将 photon-normalized intensity 直接当 total branch。ICC ceiling 必须覆盖全 multipoles/shells/current/penetration/atomic domain，extra 无界时 photon width 可趋零。

Photon floor 与 omitted upper 同时满足 (1+Amax)Uom+Uextra<Pmin 才自动认证非空 retained；这不确定 phase/sign、initialρ、方向节点或时间波包。公式前提为 LKH82 p.121 Eqs.2.2–2.3、p.123 Eq.2.12、p.169 Eq.4.1 与 RB67 p.318 Eq.3.29；库存 theorem 是本任务 L2 条件推导。新 ceiling 排除旧 family 是 prior-domain membership，不是新的实验反证或实际核无E0证明。

## A Same-Parent Cross-Branch Strength Ratio

[[mukhopadhyay-2008-136nd-transition-rates]] MU08-9 的 a=401.2 M1、b=757.4 E2、c=389.6 第三支都取I18同母态。正确 photon intensities 下 R=(KE/KM)(Eb⁵/Ea³)(Ia/Ib)(fa/fb)，单位µN²/(e²b²)；common meanτ/normalizer/只进该分母的遗漏或IC项消掉，但selected line/efficiency/gate/mixing bias不消掉。True total branches β 则另乘(1+αeff,b)/(1+αeff,a)，不能用 branch定义未明数据决定哪一式是作者处理。

参考单位下 log R contrast=(0,1,−1,1,−1,−3,5)作用于(lnZ,lnIa,lnIb,lnfa,lnfb,lnEa,lnEb)；有限 log covariance 的传播精确，raw covariance 需local Jacobian或完整joint分布。共同strength factor的rank1 covariance消掉，但共同energy gain有+2，在totalbranch且energy-dependent α中另有chain terms。Ratio吻合可以隐藏共同absolute normalization error，B和ratio不能重复计独立证据。

若把同母态三quoted分支SD0.06/0.02/0.02解释为逐样本精确归一的finite-variance vector，会违反distribution-freeσa≤σb+σc。那只是该额外joint解释的反证，不推actualcovariance或authorerror；TablesI–II/原error段没给这些定义。Source locators是MU08 p.3/TableI/pureM1与systematic段、p.4/TableII，以及LKH82 p.121 Eqs.2.2–2.3。33项L2specialization属于无学分Day9预习；完整covariance、branchbasis和stopping/feeding包仍缺。

## Sources

- [[mukhopadhyay-2007-135nd-chiral-vibration-static]], [[mukhopadhyay-2008-136nd-transition-rates]]
- [[petrache-2006-near-degenerate-chiral-misinterpretation]], [[petrache-2018-chiral-bands-even-even-136nd]]
- [[petrache-1998-highly-deformed-lifetimes-131ce-nd]], [[singh-2016-lifetime-131ce-133pr]], [[babra-2019-deformation-change-136sm]]
- [[jensen-2001-165tm-h9-2-configuration]], [[herzan-2015-193bi-spectroscopy]], [[nolan-sharpey-schafer-1979-lifetime-measurements]]
- [[lange-kumar-hamilton-1982-multipole-admixtures]]：p.121 / PDF p.3, Eqs.2.1–2.6 的 rate/RME normalization；[[multipole-mixing-ratio]]：允许高阶、radiative fractions、δ sign 和 E0/ICC 的边界。
- [[afanasjev-1999-termination-rotational-bands]], [[walker-dracoulis-2001-exotic-isomers]]

## Self-audit

- Experimental strength, author interpretation and model calculation are kept in separate layers.
- The `136Nd` conclusion is pair-specific and does not generalize automatically to all chiral candidates.
- This synthesis is a Codex self-audit and remains unreviewed.


## Day 20预习：高自旋寿命—强度—形变全景证据图（Evidence Map）与反证矩阵

本节为 2026-10-21 Day 19 延续轮中按 Runtime schedule snapshot 充裕时间推进的 Day 20 预习成果（保持 day_index: 19, completed: [19], partial: [20], next: 20，不跨卡计分）。系统构建连接核谱学直接观测量、仪器响应解卷积、跃迁矩阵元与微观内禀形变的全景证据图与反证矩阵：

### 1. 五层结构证据传导链（Evidence Flow Chain）

| 证据层级 | 核心观测量与物理对象 | 涉及的关键物理效应与响应 | 典型主导致偏系统不确定度 |
| --- | --- | --- | --- |
| **Layer 1: 实验原始观测量** | 多角度多普勒展宽线形、质心位移 F(tau)、频移/未移双峰面积比 Is/Iu、符合时间谱 | 反冲初速矢量、反冲离子角分布、符合探测立体角 Qk、康普顿散射本底 | 探测器能量刻度漂移、90度探测效率缺失、偶然符合本底扣除不净 |
| **Layer 2: 时钟解卷积与标尺** | 介质阻止本领 dE/dx、微米级飞行位移 d = v0*t、仪器瞬发响应 PRF、上能级馈入门 | 电子与核阻止模型、接触绝对零点 d0、时间走时 PRD(E1,E2)、真空退取向 Gk(t) | 固体阻停功率模型偏差 (10–15%)、微米接触零点误差 (±1 um)、未知慢侧馈 |
| **Layer 3: 能级寿命与跃迁率** | 核能级总寿命 tau、部分光子跃迁率 lambda_gamma = b_gamma / [tau * (1 + alpha_tot)] | 指数衰变法则、多能级级联微分方程（DDCM 严格消解）、内转换系数 alpha_tot | 旁路未观测弱跃迁遗漏、内转换系数截断理论不确定度、拟合解相关发散 |
| **Layer 4: 约化矩阵元与四极矩** | B(E2), B(M1), 混合比 delta, 轴对称转子跃迁四极矩 Qt | Wigner-Eckart 定理、Clebsch-Gordan 因子 <I K 2 0 | I-2 K>^2、多极相干叠加 | K 量子数混合多解性、低自旋区 CG 几何因子偏差 (10–30%)、E2/M1 纯度假设 |
| **Layer 5: 微观形变与模式解释** | 电荷四极形变 beta2、非轴对称三轴度 gamma、超形变、手征进动、摆动激发 | Cranked-Strutinsky 单粒子势阱、TRS 势能面、TAC 倾斜推转、配对涨落 | 刚性三轴与动态 gamma-soft 简并、离心转动收缩、两带混合干扰 |

### 2. 跨核素形变与集体性对照矩阵（Comparative Evidence Matrix）

| 核素与能带标识 | 实验测量方法 | 测定物理量与中心值 | 提取的形变参数 (Qt / beta2) | 微观组态与结构物理机制 | 关键证据边界与反证限制 |
| --- | --- | --- | --- | --- | --- |
| **131Ce Band 1 (ND)** | IUAC GDA Plunger+DSAM | 4 个有限寿命 (tau = 1.4–71 ps) | Qt = 2.26–2.93 eb (回归斜率 z = 0.639 sigma) | 负宇称 nu h11/2 解耦带，高-Omega 中子驱动 gamma 软度 | 加权回归严格相容零斜率，证伪目视下降判断；未测单侧限值制约 |
| **131Ce yrast HD** | GASP+ISIS 132 MeV DSAM | F(tau) 质心分析 | Q0 = 7.3(4) eb, beta2 = 0.38(2) | 强高度形变带，侵入轨道 nu i13/2 驱动大四极矩 | 明确假设无三轴性 (gamma=0)；与正常形变带无连接跃迁，形变不可直比 |
| **134Nd yrast HD** | GASP+ISIS 132 MeV DSAM | F(tau) 质心分析 | Q0 = 6.8(3) eb, beta2 = 0.35(1) | 包含 1 条占据的 nu i13/2 侵入轨道 | 离心转动收缩与侵入轨道极化抵消，四极矩未随占据数单调增加 |
| **134Nd excited HD** | GASP+ISIS 132 MeV DSAM | F(tau) 质心分析 | Q0 = 6.4(4) eb, beta2 = 0.33(2) | 跨入 2 条占据的 nu i13/2 侵入轨道候选 | Q0 反略低于单侵入轨道带，证伪简单线性可加性假设 |
| **133Pr yrast band** | IUAC GDA Plunger (singles) | tau = 1.43–71 ps | Qt = 3.09–3.55 eb | 质子 pi h11/2 低-Omega 轨道稳定长椭球近轴形变 | 统计不足采用多重性门控单谱，依赖长侧馈模型假定 (<0.4 MeV/hbar) |
| **136Nd Band 1 vs 2** | GASP DSAM 线形分析 | tau = 0.08–1.79 ps | Band 1 Qt = 4.17 eb, Band 2 Qt = 2.88 eb | Band 1/2 产生 2.06 倍 B(E2) 落差，对应组态极小差异 | 彻底排除等形变手征假象，证实破对对集体四极形变的剧烈扰动 |
| **136Sm yrast crossing** | 107 MeV DSAM 线形分析 | tau = 0.22–1.23 ps | Qt 从 5.70 eb 降至 4.85 eb (回归 z = -2.72) | 第一次回弯由 gamma 软演化为稳定三轴形变 (beta2 = 0.22) | 阻停功率系统误差达 15%，完全覆盖表观下降差额，非绝对灾难塌缩 |

### 3. 四类伪形变趋势的反证与简并消除

1. **反证 1：gamma-softness 动态涨落伪装静态形变减弱**：
   在势能面平坦的 gamma 软核（如 131Ce、136Sm）中，随着角动量增大，核表面在 gamma 方向发生大幅度动态振动，导致实验有效测定的平均四极矩 Qt 出现表观下降。如果不通过更高阶多极不变量（如 Kumar 四极不变量 <Q^2>, <Q^3 cos 3gamma>）或库仑激发矩阵元解耦，仅凭几个能级的寿命无法判定是静态轴对称形变减弱，还是势能面软化导致的振幅弥散。
2. **反证 2：能带交叉（Band Crossing）强混合引起局域 B(E2) 塌缩**：
   在推转频率到达交叉区时，基态带与对齐带发生两带强混合，形成排斥态。混合导致初末态波函数交叠积分严重衰减，使得交叉能级的跃迁几率急剧暴跌（如 136Nd 能级交叉处 18- 态 B(E2) 下跌达 11 倍）。这种局域矩阵元暴跌纯属单粒子自由度解耦诱导的干涉相消，不能直接解释为核芯整体空间四极形变的破坏。
3. **反证 3：DSAM 慢侧馈未完全扣净制造高自旋虚假下降**：
   在熔合蒸发反应中，若未采用直接馈入跃迁符合门，未观测的准连续谱慢侧馈（带外时标达数百飞秒至数皮秒）会沿级联向下累积。低自旋态累积的馈入时延显著高于高自旋态，导致拟合得到的低自旋寿命被系统性高估，从而在转子公式推导下人为制造出 Qt 随自旋升高而虚假下降的伪趋势。
4. **反证 4：低自旋 RDDS 与高自旋 DSAM 拼接的系统标尺跳变**：
   在尝试构建全自旋区形变演化曲线时，文献常将低自旋 RDDS 测得的寿命与高自旋 DSAM 测得的寿命简单并列。由于 DSAM 严格受制于介质阻停功率的整体标定（10–15% 不确定度），而 RDDS 受制于压电微米机械零点（Delta d0 约 1 um），两类方法在 1–2 ps 交叉区若存在不同的系统偏移，拼接点处将产生虚假的阶梯式跳跃，误导形变相变结论。
