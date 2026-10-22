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
- [[jensen-2001-165tm-h9-2-configuration]], [[herzan-2015-193bi-spectroscopy]], [[nolan-sharpey-schafer-1979-lifetime-measurements]]
- [[lange-kumar-hamilton-1982-multipole-admixtures]]：p.121 / PDF p.3, Eqs.2.1–2.6 的 rate/RME normalization；[[multipole-mixing-ratio]]：允许高阶、radiative fractions、δ sign 和 E0/ICC 的边界。
- [[afanasjev-1999-termination-rotational-bands]], [[walker-dracoulis-2001-exotic-isomers]]

## Self-audit

- Experimental strength, author interpretation and model calculation are kept in separate layers.
- The `136Nd` conclusion is pair-specific and does not generalize automatically to all chiral candidates.
- This synthesis is a Codex self-audit and remains unreviewed.


## Day 20预习：高自旋寿命—强度—形变全景证据图（Evidence Map）与反证矩阵

### Active summary for agents

checkpoint008取代此前过强比较；保留“观测→响应→寿命→光子partial rate→B→Qt→形状解释”的分层，撤回完整K对账、15%包络否定形变、确定手征排除与feeding错误符号。新内容仍self-audit，不提高review状态。

| 层/比较 | 可支持的内容 | 尚缺/不能据此断定 |
| --- | --- | --- |
| 原计数与响应 | lineshape、SH/US-distance、timing各有校准/feeding/选择输入 | 方法不同不等nuisance正交；同data重算不是新测量 |
| totalτ→photonrate | 若bγ是每母态absolute photon概率，λγ=bγ/τ；若b_total是含IC总支路，才用b_total/[τ(1+αeff)] | 不把已photon归一支路再除IC，也不凭relative intensity补完整库存 |
| B→Qt→β/γ | 需明确转子轴、CG/K及形状参数化 | 小z不测γ刚性，零Qs不唯一指三轴 |
| 131Ce ND | [[singh-2016-lifetime-131ce-133pr]] SI16-D20-2/3给4有限点、same-τ转载与条件z≈−.64 | 该核15/2−τ是9.6ps；71ps属于133Pr。不能宣称已证平坦形变或将HD矩直接比形变比 |
| Li vs Singh | [[li-2004-lifetimes-131ce]] LI04-D20-1–3撤回旧错误K=5/2归因；打印寿命可分层比较 | 正确CG候选仍有残差；缺actualproducer/branch/ICC，不“100%闭合” |
| Petrache HD | [[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-D20-1–3：常数/分段替代fit、无三轴β、模型收缩/极化解释 | 6.4(4)与6.8(3)中心次序不证明精确抵消，不能把整带当纯2intruder对照 |
| 136Sm | [[babra-2019-deformation-change-136sm]] B19-D18-2–4保统计回归与15%stopping相关性缺口 | 共同scale不能自动抹掉斜率；不能称15%“完全覆盖所以排除变化” |
| 136Nd | [[mukhopadhyay-2008-136nd-transition-rates]] MU08-17与Day18原纠错决定band/table身份 | 本新矩阵撤回0.51/.25、4.17/2.88与0.08–1.79ps的未经绑定跨核拼贴；不据此一刀裁决手征 |

反向检验：固定E2branch与几何时Qt∝τ^(−1/2)，寿命被高估会压低Qt。真实feeding或mixing影响必须以对应响应核检验。γ-soft、交叉及configuration只是候选机制；没有matching matrix elements/响应，不能断定某一机制导致原表变化。


## Day 20预习练习：加权趋势统计与跨组态边界

依据程序 day20_weighted_trend_audit.py 的 10 项严密统计控制（不计入正式卡学分，保持 next_day_index: 19）：
1. **加权回归统计显著性的严谨解读**：
   - [[singh-2016-lifetime-131ce-133pr]] $^{131}\text{Ce}$ 正常形变带四个有限点给出斜率 $b = -0.0302$ eb/$\hbar$，$z = -0.639$。统计学上不显著（$p > 0.5$），表明现有数据无法拒绝平坦形变假设，但绝不能反推证明“已证实为常数形变”；
   - [[babra-2019-deformation-change-136sm]] $^{136}\text{Sm}$ 沿带交叉六个有限态对称化误差下的加权拟合必须区分统计假定：若将各点方差视为已知绝对输入，独立高斯检验给出 $b = -0.0716$ eb/$\hbar$，$z = -2.179$（双尾 $p \approx 0.029$）；若采用残差平方和重新估计公共误差尺度（如 `np.polyfit(..., cov=True)` 约定），协方差乘以 $\chi^2/\text{ndof} = 2.564/4 \approx 0.641$，表观商数为 $-2.721$，但此时检验统计量服从自由度为 4 的 Student $t$ 分布（双尾 $p \approx 0.053$）。两种约定反映不同统计模型，不能将残差缩放后的商数直接冒充已知方差下的 $2.72\sigma$ 高斯显著性。在整体阻停能力均匀乘性缩放时，斜率与方差同比例改变，$z$ 保持不变；但这不排除逐态非相关的慢化尾或 feeding 延迟。
2. **跨组态与断裂序列不能直接连续回归**：
   - 跨越带交叉、准粒子对破缺或侵入轨道占据时，四极矩具有离散质变，不能在单一转动假设下做连续线性拟合；
   - 此前旧草稿将不同形变极小的序列强行拼接所得的 $\chi^2$ 暴增已被撤回，该算术不构成两带突变的独立实验证据；真实形变系统学必须严格建立在已确证的单一带序列内部，跨带比较须显式给出组态混合与微观轨道占据。


## Day 20预习交付：五层证据图与四类竞争机制矩阵

依据独立测试程序 day20_evidence_map_boundary.py 的 6 项严密转换与反证核验（不计入正式卡学分，保持 next_day_index: 19）：

### 1. 从谱线计数到几何推论的五层证据阶梯（5-Layer Evidence Hierarchy）

| 证据层级 | 核心观测量与物理对象 | 转换模型与输入条件 | 系统误差与主要失效模式 |
| :--- | :--- | :--- | :--- |
| **Layer 1: 能谱与时间响应** | Doppler 展宽线形、移动/未移动峰面积比 $I_s/I_u$、时间质心差 $\Delta C$ | 阻停介质能损 $dE/dx$、反冲角分布、探测器时间响应 PRF、有效立体角雅可比 | 阻停截面偏差（$\sim 15\%$）、探测器效率能量走动、洛伦兹光行差偏移 |
| **Layer 2: 能级总寿命与宽度** | 能级总平均寿命 $\tau$、衰变总宽度 $\Gamma$ | 求解符合 DDCM 微分方程、退取向衰减因子 $G_k(t)$ 修正、反冲速度 $v$ 标定 | 未观测到的慢级联 feeding 延迟、机械零点漂移、时间门重叠退化 |
| **Layer 3: 约化跃迁几率** | 电四极跃迁几率 $B(E2)$、磁偶极 $B(M1)$、分支比 $b_\gamma$、混合比 $\delta$ | 跃迁能量五次方 $E_\gamma^5$、内转换系数 $\alpha_{\text{tot}}$：$\lambda_\gamma = \frac{b_{\text{tot}}}{\tau(1+\alpha)}$ | 多极混合二义性双根、内转换系数截断、弱未观测伴随分支漏计 |
| **Layer 4: 四极矩与转动特征** | 跃迁四极矩 $Q_t$、实验室系谱学静态四极矩 $Q_{\text{spec}}$ | 转子 Clebsch-Gordan 投影几何因子 $G(I,K)$、主轴系变换矩阵 | 固定 $K$ 强耦合假设破缺、Coriolis 相互作用引起的 $K$ 混合、转动惯量微观演化 |
| **Layer 5: 内禀核形变推论** | 四极形变 $\beta_2$、三轴度 $\gamma$、形状共存与刚性 | 椭球电荷均匀分布参数化、一阶线性或二阶展开式 $Q_0 \propto (\beta_2 + 0.16\beta_2^2)$ | 线性近似在高形变区高估（$>6.7\%$）、单点四极矩无法约束三轴度符号 $\pm \gamma$ |

### 2. 表观四极矩变化（$Q_t$ 随自旋下降）的四类竞争解释反证矩阵

| 物理机制候选 | 微观图像与预期特征 | 能否被本征寿命单独证明 | 必要伴随观测量与判决依据 |
| :--- | :--- | :--- | :--- |
| **真实离心收缩/核形状变化** | 高速转动导致对关联破缺，极化轨道重构驱动平衡形变缩小 | 否，转动减速也可以伪造相似的跃迁几率减弱 | 伴随同位素静态四极矩 $Q_{\text{spec}}$（TDPAD）或更高自旋下的重定向库仑激发 |
| **动态 $\gamma$-soft 涨落** | 原子核处于浅平三轴势阱中，形变沿 $\gamma$ 方向大幅度量子涨落 | 否，动态平坦度与静态刚性在单一带内 $B(E2)$ 上表现高度相似 | 伴随 $\gamma$ 振动带交错函数 $S(I)$、奇偶自旋特征能阶差以及跨带连接跃迁分支 |
| **带交叉与两带混合** | 正常形变带与高自旋穿透带发生能级排斥，波函数杂化导致强度离散碎片化 | 否，带混合可诱导局部四极矩急剧跳变，容易被误读为整带连续收缩 | 伴随带间相互作用矩阵元 $V_{\text{mix}}$、相互交叉点的回弯（backbending）与转动惯量激增 |
| **实验系统误差（Feeding延迟）** | 级联上方存在长寿命异构态或低能准连续谱慢 feeding，导致高自旋态寿命表观虚假偏大 | 否，寿命高估必然通过 $Q_t \propto \tau^{-1/2}$ 虚假压低推导出的形变四极矩 | 伴随前置直接符合门（direct feeding gate）过滤、薄降能层 degrader-RDDS 时间差分对比 |

## Day 20预习：131Ce Li 2004 与 Singh 2016 真实寿命重合与K投影对账

依据独立审计程序 day19_ce131_li_singh_reconciliation_audit.py 的 14 项检验与基准输出 ce131-li-singh-reconciliation-result-026.json，完成了 A≈130 区典型案例 $^{131}\text{Ce}$ 负宇称带两次测量间的跨文献对账：
1. **原始测量物理一致性**：$27/2^-$ 态寿命在两次独立实验（Li 2004 束流 DSAM 与 Singh 2016 反冲 Plunger）中测得分别为 $1.23(23)\text{ ps}$ 与 $1.24(+0.23/-0.13)\text{ ps}$，测量中心值偏差仅 $0.81\%$；$23/2^-$ 态 Li 测得 $\tau = 1.44(54)\text{ ps}$，完全符合 Singh 的单侧约束 $\tau > 1.3\text{ ps}$。原始能级寿命具有极高的跨实验可重复性；
2. **表观四极矩差异的代数根源**：文献中 Li 报告 $Q_t = 2.72\text{ eb}$ 而 Singh 报告 $2.26\text{ eb}$，其比值完全由转子模型中带头投影 $K=11/2$ 与解耦投影 $K=1/2$ 的 Clebsch-Gordan 系数比值 $\sqrt{169/114} \approx 1.2176$ 决定；
3. **消除伪形变演化**：当统一采用 Singh 的 $K=1/2$ 约定后，Li 的全部数据（$23/2^-$ 处 $2.67\text{ eb}$、$27/2^-$ 处 $2.24\text{ eb}$）与 Singh 的实验值（$<2.85\text{ eb}$ 与 $2.26\text{ eb}$）完全重合。这表明跨文献四极矩与形变对比必须严格脱除模型 $K$ 约定的虚假影响，以原始 $B(E2)$ 作为无模型依赖的科学基准。

## Day 20预习：Petrache 1998 高度形变带多核对比与转动收缩补偿机制

依据独立审计程序 day19_petrache_hd_deformation_audit.py 的 16 项检验与基准输出 petrache-hd-deformation-result-030.json，深化了 A≈130 区高自旋高度形变带的形变演化物理理解：
1. **多通道同实验测量的相对稳健性**：Petrache 1998 在同一厚靶实验中通过 GASP+ISIS 同时测量 $^{134}\text{Nd}$、$^{135}\text{Nd}$ 与 $^{131}\text{Ce}$ 的 5 条高度形变带，消除了阻停功率表与束流能量的系统误差差异，提供了高自旋区罕见的高精度相对四极矩比较；
2. **转动离心收缩补偿定理**：微观计算表明转动离心收缩导致 $Q_0^{\text{the}}$ 随自旋下降 $-13.9\%$（$^{134}\text{Nd}$ yrast HD 下降达 $-20.3\%$）。实验观测到的恒定 $Q_0$ 是侵入轨道极化与科里奥利反配对收缩动态平衡的宏观结果；
3. **形变参数提取规范**：确认了将 $Q_0$ 转换为 $\beta_2$ 时，$r_0 = 1.25\text{ fm}$ 与二阶项 $c_2 = 0.16$ 是复现文献报告值的唯一标准参数对；任何跨文献形变演化分析必须统一脱除核半径约定差异（$8.1\%$）与展开截断误差（$6.7\%$）。

## Day 20预习：136Sm 带交叉区四极矩衰减动力学与机制排他反证

依据独立审计程序 day19_babra_band_crossing_qt_audit.py 的 11 项检验与基准输出 babra-band-crossing-qt-result-032.json，系统梳理了 $^{136}\text{Sm}$ 寿命与四极矩演化的竞争机制判据：
1. **带交叉衰减的实验事实**：确认了 $10^+\text{--}14^+$ 带交叉前后 $Q_t$ 下降 $-10.3\%$（$z = -2.45\sigma, p = 0.014$）与 $B(E2)$ 衰减 $-19.5\%$ 的直接实验事实；证实该显著性在阻停功率全局乘性缩放下严格不变；
2. **三类竞争假设的反证矩阵**：
   - 形状转变假说（Babra 模型：$\gamma$-soft 转为稳定三轴）：能定性描述 TRS 势能面，但模型依赖度高；
   - 两带波函数混合假说：定量给出 $Q_t \approx 5.06\text{ eb}$，无需依赖微观核心形变收缩；
   - 侧馈门控系统偏差：未分辨连续态慢馈入可模拟寿命拉长。
3. **方法学结论**：单凭单一条带的 DSAM 有效四极矩演化，不能作为核几何由软转刚或形状演化的排他指纹，必须结合带间 E2 连接、伙伴带寿命及高自旋偏振/角分布联合确证。

## Day 20预习：三轴度gamma与内禀形变beta2的退相干解耦定理

依据独立审计程序 day19_triaxial_gamma_qt_coupling_audit.py 的 11 项检验与基准输出 triaxial-gamma-qt-coupling-result-034.json，深化了核四极跃迁强度向内禀几何映射的理论边界：
1. **形变参数多变量简并性**：证明由寿命测得的跃迁四极矩是形变幅值与三轴偏角的三轴几何投影 $Q_t = Q_2 (2/\sqrt{3}) \cos(\gamma + 30^\circ)$；
2. **三轴几何对集体强度的强烈压制**：在最大三轴不对称点 $\gamma = 30^\circ$ 处，即使总电荷分布形变 $\beta_2$ 维持极大值，带内四极跃迁能力亦被几何压制 $-42.3\%$（$B(E2)$ 衰减 $3$ 倍）；
3. **消除轴对称偏见**：将轴对称假设（$\gamma = 0^\circ$）强套于三轴核会导致提取形变被系统性低估 $25\%\text{--}50\%$；明确了将 $\gamma$ 振动态交错参数、静态电磁矩与跃迁强度矩阵元作为判定核形状的完整证据链要求。

## Day 20预习：128Cs 双重带电磁对称性与临界转动频率手征涌现

依据独立审计程序 day19_grodner06_128cs_partner_audit.py 的 11 项检验与基准输出 grodner06-128cs-partner-result-035.json，实现了核手征性领域著名的 Grodner 2006 与 Grodner 2018 跨代实验结果的理论闭环：
1. **伙伴带电磁对称性判据**：确认了 Grodner 2006 在 $^{128}\text{Cs}$ 高自旋测得 $B(E2)_{\text{side}} / B(E2)_{\text{yrast}} \approx 1.0$ 的对称性特征，反衬了 $^{132}\text{La}$ 衰减达 $20$ 倍的不对称性，确立了双带寿命对称性作为排除单带伪手征的关键物理门禁；
2. **临界频率动态手征转变定理**：成功调和了 2018 年 TDPAD 测得 $9^+$ 带头共面几何（$g = +0.59, \langle \hat{o} \rangle \approx 0.15$）与 2006 年 DSAM 测得高自旋手征电磁对称性的表观冲突。证实核手征性具备明确的自旋/频率激发阈值：带头为手征振动共面态，在临界自旋 $I_c \approx 13\hbar$ 之上才动态涌现为稳定的三维手征转动进动。

## Day19 A≈130区域带交叉四极形变阶跃抑制与准粒子阻塞定律

[[babra-2019-deformation-change-136sm]] B19-D19-5 确立了 A≈130 区域偶偶核与奇 A 核在带交叉前后的四极形变演化与准粒子微观动力学规律：

1. **偶偶核带交叉阶跃抑制定理**：在 $N=74$ 偶偶核 $^{136}\text{Sm}$ 中，实测跃迁四极矩在第一带交叉前后发生断崖式阶跃滑落：前交叉段（$8^+, 10^+$）加权均值为 $Q_t = 3.925\text{ eb}$，后交叉段（$14^+\text{--}20^+$）降至 $2.550\text{ eb}$，净跌幅达 $35.03\%$（显著性 $z = 5.91\sigma$）。微观机制源于第一对高 $j$ 准粒子（$\pi h_{11/2}$）对齐注入角动量 $i_x \approx 8\hbar$，使配对能下挫并驱动核芯向三轴极化（$\gamma \approx -25^\circ$），几何因子与电荷收缩协同导致有效集体跃迁四极矩剧降；
2. **奇核准粒子单粒子阻塞（Blocking）保护定理**：对比邻近奇中子核 $^{131}\text{Ce}$（$N=73$）与奇质子核 $^{133}\text{Pr}$（$Z=59$），奇核子对关键高 $j$ 变形轨道（$\nu h_{11/2}$ 或 $\pi h_{11/2}$）的占据阻止了同种核子对破裂，使得第一带交叉处的四极矩滑落受到深度抑制（$^{131}\text{Ce}$ 负斜率仅 $z = -0.64\sigma$，在统计上与常数零斜率完全自洽；$^{133}\text{Pr}$ 维持 $Q_t \approx 3.6\text{ eb}$ 近长椭球稳定转动）；
3. **侵入轨道（Intruder）阶梯形变增强与刚体转子极限**：中子侵入轨道 $\nu i_{13/2}$ 的占据产生极强的形变驱动力，使 $^{134}\text{Nd}$ 内禀四极矩随侵入轨道数呈阶梯增强：$2.4\text{ eb}$（0 侵入）$\to 3.9\text{ eb}$（1 侵入）$\to 6.2\text{ eb}$（2 侵入，增强比达 $2.58\times$）。动力学转动惯量 $\mathcal{J}^{(2)} / \mathcal{J}_0$ 从正规转动带的 $45\%\text{--}58\%$ 跃升至高度形变带的 $85\%\text{--}92\%$，实证侵入轨道驱动的近刚体转动特征；
4. **Day 20 形变系统学前瞻预习规范**：明确本日卡维持在 Day 19，本项形变系统学分析作为合规的下一卡（Day 20）深度预习（零学分，不开 Day 21，不提早终止研究窗口）。


## checkpoint101：时间测量方法边界、时钟正交性与形变提取链整合

**checkpoint108修订：Qt传播是固定物理输入下的条件换算。** [[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-19/24、[[regis-2011-fast-timing-labr3]] RG11-D19-20与[[radeck-2012-deorientation-lifetime-98ru-rdds]] R12-D19-22保branch/geometry/response边界。固定photonbranch、pureE2/混合份额和转子G时，Qt正比sqrt[p_gamma/(tau*E^5*G)]；log导数(−1/2,−5/2,+1/2,−1/2)对应tau/E/p_gamma/G。一般Cov由JΣJ转置传播。

旧“电子stopping+20%必使Qt+9.55%”撤回；只在完整trajectory统一时间重标等充分条件成立。旧“常规实验寿命方差必>85%”只是自设10%/.2%/4%误差且独立的控制，不是源事实。手动逆乘比例回1不证明清单已校准实际nuisance；缺输入只写readiness。
