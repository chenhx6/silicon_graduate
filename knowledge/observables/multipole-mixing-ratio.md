---
type: observable
title: 多极混合比
aliases: [multipole mixing ratio, E2/M1 mixing ratio, mixing ratio, δ]
created: 2026-07-01
updated: 2026-10-07
status: active
review_status: unreviewed
observable_kind: electromagnetic-transition-observable
symbol: δ
units: dimensionless
tags: [gamma-transition, multipolarity, wobbling]
---

# 多极混合比（Multipole Mixing Ratio）

## Definition

混合多极跃迁中两种辐射振幅之比；本库当前主要关注 ΔI=1 跃迁的 E2/M1 mixing ratio。

## Formula and Conventions

δ 的符号与相位约定必须沿用原文；只比较绝对值时也要说明。

### 辐射振幅、能量因子与约定映射

[[lange-kumar-hamilton-1982-multipole-admixtures]] 的 LKH82-1（printed p.121 / PDF p.3, Eqs.2.1–2.6）定义 `δKS²=Tγ(E2)/Tγ(M1)`，完整有符号定义为：

`δKS=(√3/10)[Eγ/(ℏc)] ⟨Jf||M(E2)||Ji⟩/⟨Jf||M(M1)||Ji⟩`。

其 BM 约定末态在左、初态在右；若 Eγ 用 MeV，E2/M1 RME 分别用 eb/μN，则系数为 `0.835 Eγ(MeV)`。δ 是包含运动学归一化的辐射振幅比，不是裸 RME 或 B 值之比。原文 “positive root” 固定比例系数，矩阵元比仍可为负。公式只适用于 E2/M1 同时允许的跃迁，不能套到 E1/M2 或 E2/M3。

[[rose-brink-1967-phase-defined-angular-distributions]] 的 RB67-6（printed p.319 / PDF p.14, Eq.3.39）使用相位定义的 interaction operator，初态 `J1` 在 RME 左侧，并对每个振幅除以 `√(2L+1)`：`δ_(L′π′)=a_(L′π′)/a_(Lbar πbar)`，`a_(Lπ)=⟨J1||T_L^π||J2⟩/√(2L+1)`；最低阶成分的 δ 为 1。其模的平方对应部分 γ 宽度比。`π=0/1` 是该文的 E/M 标签，核态宇称另记 `πi,πf`。实数性与相位条件回到 Eq.3.32 note(v) 和 Eq.3.39 footnote17，不凭名称互换 BM 与 RB 的矩阵元。

在 LKH82-4 的发射级联 `J1→J2→J3` 下，`δKS(γ1)=−δBR(γ1)=−δRB(γ1)`，`δKS(γ2)=+δBR(γ2)=−δRB(γ2)`；第一、第二 γ 的 BR 转换不同。吸收、电/磁算符与几何系数须再核对 Eqs.2.9–2.11。共同核态的任意整体相位在比值中抵消，算符/约化定义的相位及发射吸收映射仍需保持。

## Angular-Momentum and Parity Filters

For a gamma photon of multipole rank `L`, the angular-momentum triangle requires `|Ji−Jf|≤L≤Ji+Jf`, with `L≥1`. Electric and magnetic radiation change parity by `(-1)^L` and `(-1)^(L+1)`, respectively. For definite-parity states, the commonly used low-rank cases are:

| Multipole | Nuclear parity | Angular momentum |
|---|---|---|
| E1 | Changes | `\|Ji−Jf\|≤1≤Ji+Jf`，因此不含 `0↔0` |
| M1 | Conserves | `\|Ji−Jf\|≤1≤Ji+Jf`，因此不含 `0↔0` |
| E2 | Conserves | `\|Ji−Jf\|≤2≤Ji+Jf`；不能只排除 `0↔0`，例如 `1/2↔1/2` 与 `0↔1` 也不允许 E2 |

These are the leading low-rank candidates, not an exhaustive list. The triangle rule also permits higher ranks when `L≤Ji+Jf`; same-parity transitions can contain M3/E4… components, and opposite-parity transitions E1/M2/E3… components, subject to the same rank bound. State the low-rank truncation when using an E1, M1, or E2-only fit. Rose–Brink gives the general rule in Sec. III.E, printed p.320, after Eqs.3.40–3.41; the discussion assumes definite parities and gives broader conditions on pp.320–324.

“Forbidden” means that a specific multipole amplitude violates an exact angular-momentum or parity rule under the stated assumptions. It does not mean every other multipole is forbidden. “Hindered” means an allowed transition has unusually small strength relative to a named reference or expected scale; a selection rule alone cannot establish hindrance.

上述术语区分是一般理论教学定义；RB67-5 直接支持角动量/宇称过滤，LKH82 printed p.120 / PDF p.2 则讨论特定最简集体模型的 leading M1 被禁止或受抑，不能把该模型规则升级成普遍守恒定则。近似对称性下的 K-forbidden 等标签也需另写近似和对称性破缺条件。

### 三条合成跃迁的完整候选

以下是选律演绎练习，不对应任何核素、实验跃迁或新测量。`Ji,πi,Jf,πf` 是题设，尚无独立观测来支持这些标签。

| 合成跃迁 | 角动量边界与宇称 | 全部允许的单 γ 多极 | 低阶截断及非 γ 边界 |
|---|---|---|---|
| `3/2+→1/2−` | `1≤L≤2`，宇称改变 | E1、M2 | E1-only 或 E1/M2 是不同模型；M2 不能按选律删除；指定跃迁没有 E0 |
| `2+→2+` | `1≤L≤4`，宇称保持 | M1、E2、M3、E4 | M1/E2 拟合忽略 M3/E4，是需说明的截断；另允许 E0 转换，E0 不属于单 γ 多极 |
| `3+→1+` | `2≤L≤4`，宇称保持 | E2、M3、E4 | 没有 M1；E2/M3 拟合忽略 E4；纯 E2 还忽略 M3，指定跃迁没有 E0 |

来源：RB67-5 的 general triangle/parity rules 与 LKH82-5 的 same-spin E0 条件。低阶振幅经常在适用的长波长和结构条件下占优，但没有本题的能量、尺度、矩阵元或测量上限，不能量化高阶抑制，更不能把截断写成 forbidden。

### 多解与互补观测的条件

固定两个候选、实数 δ 与 setup 后，角分布中每一几何系数可写成 `C_K(δ)=[C_K,ll+2δ C_K,lh+δ² C_K,hh]/(1+δ²)`，这是 RB67 Eqs.3.41–3.43 与 LKH82 Eqs.2.8–2.9 的两成分代数形式；交叉项的符号须从所选约定读取。换 δ 符号和几何系数映射同时进行，才保持可观测量不变。仅含 δ² 的率比、ICC 或寿命不能完成此相位判断。

| 观测 | 有条件能排除的解 | 必须保留的依赖与未定量 |
|---|---|---|
| 单 γ 角分布 | 预测角形状与完整数据不相容的 spin/multipole/δ 组合 | 需要 alignment/population、角度效率/有限立体角、feeding 和协方差；不测偏振的角分布不能单独区分同 L 的 E/M 宇称标签 |
| γγ 角关联 / DCO | 在已知级联或 gating transition 下不相容的 rank/δ/spin 组合 | gate 的自旋、多极、混合比与响应进入结果；DCO 数值不具有跨阵列通用阈值，和由相同计数计算的 angular fit 不是独立重复证据 |
| 线偏振 | 在明确分析轴、响应和角度下排除不相容的 E/M 或混合分支 | 要使用幅度和误差、完整候选而非只看正负；若 Jπ 已由该 E/M 假设推来，不能再作为独立 parity 证明 |
| 内转换 | 在 Z、Eγ、壳层与候选已知时约束 radiative fractions 或 pure/mixed 候选 | 普通积分 ICC 对 δ 的符号不敏感；`2+→2+` 还需考虑 E0 与 penetration；理论 ICC 与 electron/γ 标定仍是输入 |
| 寿命 + 完整分支 | 给部分率与在已知多极下的绝对强度；可与明确 strength 预测比较 | 无独立矩阵元/参考尺度时，任一允许 L 均可用不同矩阵元匹配一个率；寿命不独立指定多极或 δ 的正负；未观测分支会改变归一化 |

这些是可以设计的观测判别，不是本题实际排除了任何数据解。正式使用须回到 RB67-2/3/4/8 的张量与宽度关系和 LKH82-4/5 的约定/ICC 边界。

### 角分布 rank 上限不等于 photon rank 上限

对于轴对称单 γ 角分布，`B_K` 的 CG 系数给出 `K≤2Ji`，`R_K` 给出 `|L−L′|≤K≤L+L′`（RB67-7）。初末态宇称确定、helicity 求和时只保留偶 K；它不要求初态只能 aligned，polarized 初态也可满足。三例的最大可能偶 K 依次为 2、4、6。特别是 `2+→2+` 即使含 M3/E4，也没有 K=6/8，不能用“没看见高 K”证明高阶光子多极不存在。上限不保证每个允许系数非零或可测；γγ 级联要按其 intermediate-spin/population 公式重新判断。

解析识别性检查：在相位/时间反演条件下取实振幅，N 个成分除去整体率归一化后有 N−1 个相对幅度。`2+→2+` 的四个 gamma 成分有三个比值，而单 gamma 分布最多给 A2/A4 两个非平凡偶 K 系数；即使布居已知，只有这两个数也不保证一般三参数解唯一，未知布居会再增加依赖。此维数分析根据 RB67-6/7 的归一化与rank条件，不是新数据拟合。RB67-9 的长波与两多极近似可减少参数，但必须说明它是截断，不能把减少的参数误称为实验排除。

### E0 对转换系数和寿命归一化的影响

在 M1/E2 γ 截断下，LKH82-5 给出 `αK,obs=[αK(M1,λpen)+δ²(1+qK²)αK(E2)]/(1+δ²)`；`qK²` 是 E0_K/E2_K 电子率比，`λpen` 是 M1 penetration 参数。忽略这两项才得到常用两成分 ICC 式。`2+→2+` 的 E0 没有单 γ 对应项，只靠 γ 强度归一化所有衰变分支可能漏掉它。另两例指定跃迁无 E0，但初态到其它同自旋、同宇称末态的 E0 分支仍可能影响总寿命。Pair 通道另需能量条件，这里没有给定能量，保留为一般背景可能性。

### 合成 E1/M2 的精确角分布双解

进一步检验合成 A `3/2+→1/2−`：使用 RB Eq.3.39 的 `δ=a_M2/a_E1`（initial bra、phase-defined T 及其归一化），并**指定**轴对称对齐布居 `w(+3/2)=w(−3/2)=1/2`，其它 M 的布居为零。此布居是理想教学输入，没有实测 calibration。RB67-10 的附表与 Eq.3.28 给出 `B2=1`；Eq.3.36 的精确 CG/Racah 计算给出 `R2(11)=1/2`、`R2(12)=√3/2`、`R2(22)=−1/2`，且 `R0(11)=R0(22)=1`、`R0(12)=0`。

由 RB Eq.3.47 解析重构：

`W(θ)=1+a2(δ)P2(cosθ)`，`a2(δ)=[1+2√3δ−δ²]/[2(1+δ²)]`。

令 `φ=atanδ`，则 `a2=cos(2φ−π/3)`，范围为 `[−1,1]`。负例/极限：纯 M2 的 `|δ|→∞` 给 `a2=−1/2`；`δ=−√3` 给 `a2=−1`，所以在固定 RB 系数下改 sign 确会改变图形；`δ=1/√3` 给 `a2=+1`。若四个 M 子态等权 `w(M)=1/4`，则 `B2=0`、所有 δ 都给 isotropic `W=1`。本题 `K=4` 系数为零，不能凭空增加一个 A4 观测来解方程。这些控制由同一精确 CG/Racah 表达式推得。

令 `a2(δ)=a2(0)=1/2`，得到两个精确解 `δ=0` 与 `δ=√3`。前者纯 E1，后者 M2 的 **γ 率份额**为 `δ²/(1+δ²)=3/4`；由于该单 γ 分布只有 K=0/2，两根在全部 θ 给出相同归一角分布。这是 formalism 的解析负例，不是作者的新实验结果或本任务的 measured δ。它没有说明大 M2 份额对真实核素是否合理。

若分别选归一辐射振幅 `(a_E1,a_M2)=(1,0)` 和 `(1/2,√3/2)`，两者 Σa² 都等于 1；固定同一 Jf 与 photon k 时也给出相同 Eq.3.29 γ 宽度。这直接证明本 γ channel 的率不能自动排除第二根；它不声称两根在有不同 ICC/其它分支时也给出相同实验总寿命。没有独立矩阵元/强度、ICC 与完整分支输入时，τ 本身仍不提供唯一 δ。互补 polarization/ICC 要用相应 setup 和完整候选逐项比较，不能预先保证任一单个测量必得唯一解。

本负例的 source locators 是 [[rose-brink-1967-phase-defined-angular-distributions]] RB67-6/7/8/10：printed pp.317–321 / PDF pp.12–16 的 Eqs.3.28/3.29/3.36/3.39/3.47 与 pp.339/347 附表。精确根、归一宽度一致性均为本轮 L2 数学推论，未建立事件/模拟数据集或进入 L4。

### 固定布居时，用理想线偏振区分角分布双解

继续上述合成 A：指定高-M aligned 布居 `w(±3/2)=1/2`，保持 RB δ=M2/E1、initial-bra interaction operators 和 real amplitudes。取 `khat=(sinθ,0,cosθ)`，右手 transverse axes `x′=(cosθ,0,−sinθ)`、`y′=(0,1,0)`。`x′` 在 z–k 平面内，`y′` 垂直该平面。用 RB67-11 的 q^π 因子、WE 次序与 `d=exp(−iθJy/ℏ)`，先复现完整 unpolarized W，再构造两种 helicity 的 coherent sums。

令 `x=cosθ`，归一线偏振强度为：

`Ix′=[4δ²+(3+2√3δ−3δ²)x²]/[4(1+δ²)]`，
`Iy′=[(δ−√3)²+4√3δx²]/[4(1+δ²)]`，`Ix′+Iy′=W`。

定义本例的 normalized Stokes `Q_s=(Ix′−Iy′)/(Ix′+Iy′)`；detector sensitivity `Q(E)` 和 measured asymmetry 另需响应标定与轴映射。90° 时 `Q_s=[3δ²+2√3δ−3]/[5δ²−2√3δ+3]`。

| 本例 RB δ | Ix′ | Iy′ | Q_s(90°) |
|---|---|---|---|
| 0：pure E1 | `3cos²θ/4` | `3/4` | −1 |
| √3：E1/M2 angular branch | `3/4` | `3cos²θ/4` | +1 |

因此指定布居和理想分析轴下，本对 full-angular 双解的线偏振不同；真实实验只有在布居、响应/geometry、有限接受角、背景和误差足够约束时才能据此排解。控制：两根在0/180°均 Q_s=0；pure M2/high-M 在90° Q_s=3/5；等权 Mi 时 Ix′=Iy′=1/2。δ=−√3 在0/180°强度为零，Stokes比未定义。省略 magnetic q^π 能保留同一 unpolarized W 却改变 linear intensities，所以复现 W 不能单独认证偏振实现。定位：[[rose-brink-1967-phase-defined-angular-distributions]] RB67-11/12，p.316 Eqs.3.24–3.25 与 p.312 footnote7；数值是本轮 L2 重构。

### 布居未知时，角分布和偏振可以共享多极歧义

放松前一例的独立布居约束，比较两组**题设假设**，两者仍是 `3/2+→1/2−`、同一 photon k：

| Hypothesis | 辐射振幅 (E1,M2) | w(M) | B2 |
|---|---|---|---|
| pure E1 / high-M | `(1,0)` | `w(±3/2)=1/2` | +1 |
| pure M2 / low-M | `(0,1)` | `w(±1/2)=1/2` | −1 |

第二例直接用 a_E1=0,a_M2=1 构造，没有把无限δ当有限参数。ρ2 表给 `ρ2(3/2)=+2`、`ρ2(1/2)=−2`，与 Eq.3.28 的 full-M 求和一致。独立从 Eq.3.24 振幅算得两者每个 θ 都有：

`W=3(1+x²)/4`，`Ix′=3x²/4`，`Iy′=3/4`，`Q_s=(x²−1)/(x²+1)`。

更具体地，两者在固定方向的 (−,+) helicity 强度矩阵同为 `(3/8) matrix((1+x²,1−x²);(1−x²,1+x²))`，trace=W；对应 conditional polarization matrix 再除以 W。这是 **pointwise direction/polarization intensities** 的联合歧义，不涉及不同方向的场相干、γγ correlations、核末态观测或完整光子量子态的等价。真实反应可以对布居施加额外约束；这里没有实测布居，也不把这种理想构造当典型fusion-evaporation σ/I。

共同A0与k、Sγ=1给相同目标γ宽度；总寿命仍需ICC/其它通道。若要区别这两组，优先独立检验 B2 的符号和区间，例如同一初态另一个已建立multipole、非零R2的branch，并匹配gate/feeding/response；不从待定跃迁的含假设拟合再给自己校准。指定Z/E/壳层的转换测量和理论区间可能提供另一约束，但只有区间确实有分辨力才排解，未查询本题数值ICC。source前提见 RB67-2/7/10/11；矩阵等式与研究设计是 RB67-12 的解析推论。

### 一个积分ICC不能拆开γ混合与E0：含零参考成分的边界

对合成B 2+→2+，先声明只保留M1/E2 gamma、忽略penetration、高阶M3/E4，并要求αK(E2)>0。取 `t=δ²`、`z=qK²`、`a=αK(M1)/αK(E2)`、`r=αK,obs/αK(E2)`。LKH82-5的式子给 `z=(r−a)/t+r−1`；有限t>0时 z≥0等价于 `(r−1)t≥a−r`。完整分型见 [[lange-kumar-hamilton-1982-multipole-admixtures]] 的 LKH82-6 和 ICC/E0 Identifiability 段。

r大于1时，若a>r，需t≥(a−r)/(r−1)，否则任意t>0可行；r=1时有限解需a≤1；r小于1时需a<r且0<t≤(r−a)/(1−r)。普通z=0式只给pure ICCs的convex hull；高侧越界不独证E0，低側越界连加入非负E0也不能解释该无penetration的两gamma模型。纯代数输入a=4,r=2既可(t,z)=(2,0)，也可(4,1/2)，数字不是atomic coefficients或测量。

参考成分为零时优先用率本身：`y=tz=T_K(E0)/[αK(E2)Tγ(M1)]`，`r=(a+t+y)/(1+t)`。t=0给r=a+y，仍容许E0 electrons；z的E2-rate分母为零而未定义。pure E2则用E2参照r=1+z，t/y未定义。αK(E2)=0或两保留gamma rates均零时对应ICC归一化失效，不作新的选律排除；其它壳层、pair与高阶候选要检查各自条件。

这说明radiative δ=0只表明E2 gamma率为零，不能据此删除选律允许的E0转换。该式只含δ²，sign仍需干涉与convention；total τ要另计总壳层转换、其它branch和非γ通道。前提来自LKH82 printed p.123/PDF5 Eq.2.12及p.169/PDF51 Eq.4.1，所有不等式和参考零点为本轮L2解析重构，没有新ICC数据或L4。

## How It Is Obtained

可由角分布、角关联/DCO、线偏振和内转换系数与理论响应比较得到。

Spin, parity and multipolarity are separate assignment claims. An angular-distribution or DCO fit can retain multiple spin/multipole branches, and a parity label inferred from a chosen E/M multipole is not an independent parity measurement. Use complementary handles such as a known cascade, calibrated polarization or conversion data, and state the shared alignment/response assumptions; do not count one fitted angular ratio twice as independent support for spin, parity and multipolarity. Rose–Brink's tensor formulas make the alignment, geometry and phase dependencies explicit (Secs.III.B–III.E, printed pp.314–321 / PDF pp.9–16; cascades in Sec.III.F, printed pp.321–326 / PDF pp.16–21).

Diamond 1966 gives an early alignment-dependent route: if a pure transition from the same initial state calibrates the magnetic-substate alignment, a mixed E2/M1 angular distribution can constrain the amplitude mixing ratio. Without that calibration, the paper recommends a probable range rather than a unique value.

## Diagnostic Use

较大的集体 E2 成分可支持 wobbling-band 间跃迁；接近纯 M1 更符合普通 signature partner。

## Model Dependence

DCO 几何、alignment 参数、角分布系数和探测器响应进入提取过程。理论 mixing ratio 还依赖 E2/M1 transition operators、effective charges、`g` factors 和模型波函数；模型给出的 `δ` 不能写成实验提取值。

## Failure Modes and Ambiguities

弱跃迁、有限角度覆盖和系统误差可能产生多解或大不确定度。

angular-distribution `χ²(δ)` 可能同时存在大 `abs(δ)` 与小 `abs(δ)` 两个局部解。只比较大解与 pure-M1 曲线，或只依据 polarization 符号而不使用其幅度与不确定度，不能证明已唯一选出 E2-dominated branch。

ICC-based `delta` extraction 也可能带来明显非对称误差；当 experimental conversion coefficient 相对误差较大时，简单反演混合 ICC 公式可能低估 `delta` 的中心值或区间。

## Examples

`131Xe` 的 671、882、1055 keV 连接跃迁 δ 很小，构成反对 wobbling 指认的重要证据。

[[matta-2015-transverse-wobbling-135pr]] 的 Table I 报告 `135Pr` 747.0、812.8、754.6 keV side-to-yrast transitions 分别有 `δ=-1.24(13)`、`-1.54(9)`、`-2.38(37)`；这些值是其 wobbling 支持链的关键待审数据。

[[sensharma-2019-two-phonon-wobbling-135pr]] 的 Fig.2 报告 450.2、550.5、517.1 keV second-side-to-side-band transitions 的 `δ` 分别为约 `-1.91`、`-2.26`、`-3.48`。它们支持较大 E2 成分，但 phonon-order 解释仍依赖 band assignment。

[[lv-2022-evidence-against-wobbling-135pr]] 强调 angular distribution 可产生大/小 `abs(δ)` 双解，并由联合 polarization/`R_ac` 得到 747.3、813.2、450.2 keV 的小 `abs(δ)` 解。

[[sensharma-2020-longitudinal-wobbling-187au]] 报告四条 LW→yrast links 的 `δ` 约为 `-2.67` 至 `-3.72`，而两条 SP→yrast links 为 `-0.06(1)`、`-0.10(1)`；本文未报告 connecting-transition polarization。

[[guo-2022-low-spin-wobbling-187au]] 用独立数据联合 `R_ac` 与 linear polarization，对同一 376/462 keV links 得到约 `δ=-0.26/-0.28` 的小 `abs(δ)` branch，并指出该解与早期 internal-conversion data 更一致。两篇结果构成直接实验冲突，不能把任一 branch 当作无争议事实。

[[rusev-2009-multipole-mixing-ratios-11b]] 明确展示，同一个 measured polarization-related asymmetry 也可能对应两支 `delta` 解；作者对 `11B` 选择较小 `|δ|` branch，是基于大 `|δ|` branch 会给出异常大 `E2` admixture 的物理判断。

[[rezynkina-2017-graphical-extraction-multipole-mixing-ratios]] 与 [[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] 共同说明：ICC-based `delta` extraction 需要把 theoretical ICC、transition-energy 与 `delta` 本身的不确定度一起传播。

[[nomura-2022-questioning-wobbling-ibfm]] 用 IBFM transition operators 计算 `135Pr/133La/127Xe/105Pd` 的 `δ(E2/M1)`。多数被比较 links 的计算值偏向小 `abs(δ)`/M1 dominance，但 `127Xe` 低自旋存在由近零 M1 matrix element 导致的异常大 `abs(δ)`；该模型比较挑战 wobbling assignments，却不替代原始 angular-distribution/polarization analysis。

## Sources

[[konigshofen-2001-mixing-ratios-130ba]] provides direct `130Ba` δ values under the Rose–Brink sign convention, including dominant M1 admixtures and one no-unique-solution case. Its M1-corrected `B(E2)` ratios are detector-angle and reference-transition dependent.

[[greiner-1966-magnetic-properties-even-nuclei]] is a historical model bridge linking M1/E2 mixing and rotational gR suppression to a proton–neutron deformation-difference tensor; use it as a model assumption, not a universal prior.

[[hamilton-1969-mixing-ratios-pt194-196]] is a high-resolution cascade-separation example: `194Pt` gives `δ=−(30^{+39}_{−19})` and `196Pt` gives `δ=+4.03(12)` under the Biedenharn convention. The source demonstrates that convention mapping, contaminant correction and unresolved feeding (the 759-keV warning) are part of the observable identity, not post-processing details.

[[rose-brink-1967-phase-defined-angular-distributions]] defines δ as a ratio of phase-defined reduced interaction-multipole matrix elements. Its sign is physical only after operator phase, initial/final state order, time-reversal convention and parity/alignment assumptions are mapped; the magnitude is related to partial-width ratios but does not remove these convention boundaries.

[[lange-kumar-hamilton-1982-multipole-admixtures]] relates δ² to E2/M1 partial rates and documents the Krane–Steffen sign convention and its operator/state-order boundaries. [[rose-brink-1967-phase-defined-angular-distributions]] gives the angular-momentum/parity rules, the linear interference term in the angular distribution, and the distinction between total lifetime information and relative phase. The simple E1/M1/E2 table above is a low-rank shorthand; do not infer that higher allowed multipoles are exactly forbidden.

[[eldridge-2018-gamma-band-mixing-ratios]] demonstrates the uncertainty topology in practice: IPAC `A2/A4` ovals for 37 Mo/Ru/Pd γ-band links can admit pure-E2 `δ=±∞`, finite positive/negative branches or very large alternatives. Retain all branches within the stated `(A2,A4)` uncertainty before using a shape-systematics interpretation.

[[krane-steffen-1970-cd110-mixing-ratios]] supplies a 25-correlation `110Cd` network with explicit emission-matrix-element conventions and Compton-background control. Its δ values are portable only after the Rose–Brink/Biedenharn state-order map is reproduced.

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[frauendorf-2024-wobbling-review]]
- [[matta-2015-transverse-wobbling-135pr]]
- [[sensharma-2019-two-phonon-wobbling-135pr]]
- [[lv-2022-evidence-against-wobbling-135pr]]
- [[sensharma-2020-longitudinal-wobbling-187au]]
- [[guo-2022-low-spin-wobbling-187au]]
- [[nomura-2022-questioning-wobbling-ibfm]]
- [[rezynkina-2017-graphical-extraction-multipole-mixing-ratios]]
- [[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]]
- [[rusev-2009-multipole-mixing-ratios-11b]]
- [[diamond-1966-nuclear-alignment-heavy-ion-reactions]]
- [[taras-1971-phase-defined-polarization-formulas]]

## Evolution Log

- 2026-07-01：由 `131Xe` 判别问题建立。
- 2026-07-03：加入 Matta 2015 的 `135Pr` 大 mixing-ratio 支持案例。
- 2026-07-03：加入 Sensharma 2019 的 TW2→TW1 mixing-ratio 支持案例。
- 2026-07-03：加入 Lv 2022 的双解问题与联合 polarization/`R_ac` counter-evidence。
- 2026-07-03：加入 Sensharma 2020 的 `187Au` LW/SP angular-distribution 对照。
- 2026-07-04：加入 Guo 2022 的 `R_ac-P` 小 `abs(δ)` branch 与同一 links 的直接冲突。
- 2026-07-05：加入 Nomura 2022 的 IBFM `δ` 预测、实验值比较及 `127Xe` 异常分母边界。
- 2026-07-12：加入 Rusev 2009 的 asymmetry 双解，以及 Rezynkina 2017 / Kibedi 2008 的 ICC-based `δ` 不确定度边界。
