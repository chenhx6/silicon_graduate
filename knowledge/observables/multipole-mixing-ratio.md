---
type: observable
title: 多极混合比
aliases: [multipole mixing ratio, E2/M1 mixing ratio, mixing ratio, δ]
created: 2026-07-01
updated: 2026-10-08
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

### 模型项为零、受抑与大 δ 的尺度边界

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-8–11（printed pp.125–129, Eqs.3.9/3.21–3.24/3.31–3.40）限定 `μ_N g_R J` 的形变无关零阶项；它对 rotationally invariant H 有 `[H,Jq]=0`，故不同能量态之间为零。完整一阶算符含 αJ 修正，microscopic M1 又有独立 orbital/spin 权重。通用 rank-1 张量并不必须等于 J；模型零值不能代替普遍 triangle/parity 禁止，也不能作为 measured hindrance。

直接算符修正与 wave-function band mixing 在 n=1→0 小振幅展开中同阶，需共同保留；首阶导数为零不保证所有阶次为零。PPQ 的空间内 mixing 处理保留 projection、adiabatic、pairing、basis 和 quasiparticle truncation 条件（p.131），不能外推完整 high-spin nuclear current。

大 δ 仅给 E2/M1 光子率比，不能确定 absolute E2 enhancement。同能量的两个任意 √rate 振幅 `(1/100,1)` 与 `(1/10000,1/100)` 均 δ=100，E2 率相差10⁴；不是 eb/μ_N 裸 RME 数值。判断增强/受抑需 partial rate/B 与指定参考。允许 M3/E4 时，`δ²/(1+δ²)` 也只表示 M1/E2 子集中的份额。自由振幅多解迁移到真实核还需共同 states/current、long-wave/natural-size 条件、高阶上限和实验响应，不能将形式反例直接当成同等可信的核素模型。

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

### 四γ成分与未知布居：完整线偏振仍可有连续联合解

对合成2+→2+保留完整M1/E2/M3/E4，已知轴、aligned diagonal布居 `w0=p0,w±1=p1/2,w±2=(1−p0−p1)/2` 和实RB amplitudes。[[rose-brink-1967-phase-defined-angular-distributions]] 的RB67-13保存完整B_K、R_K/T_K二次型、seed Jacobian和source locators（pp.316–319、324），属于本任务L2重构。

全点对点normalized矩阵可写 `H=matrix((W,−Δ);(−Δ,W))/2`，`W=1+A2P2+A4P4`、`Δ=Ix′−Iy′=C2P2^(m=2)+C4P4^(m=2)`。关联Legendre不是P_K的平方；meridian轴U=V=0，轴旋转不新增独立coefficients。完整四shape coefficients使用矩阵值函数基底计数，不能跨通道将五个相关scalar函数当独立。M3/E4允许且非零，也不产生本问题的K6/8。

M1参考chart `a=(1,u,v,z)`，seed `(u,v,z,p0,p1)=(1/2,1/3,1/4,1/4,1/4)` 严格内域且四成分非零；份额为(144,36,16,9)/205。主代理43项exact检查复现了五输入→四coefficients的rank4与改变radiative fractions的kernel。IFT据此证明附近存在一维精确同观测解族；kernel是tangent，不能把沿它的有限直线步称为精确第二解。相同四coefficients意味着全部理想角分布、线偏振强度及Q=Δ/W相同；没有声称跨方向光子相干、γγ关联、ICC或total τ相同。

独立已知p0/p1后同一点amplitude-only Jacobian为rank3，局部识别性改善；isotropic B2=B4=0时任意混合仍W=1、Δ=0，所以不能推广为global唯一。新增的合成same-parent2+→0+ pure-E2参考branch可因R2/R4皆非零同时校准两个B_K，但该branch不是题设或测量。需要spin/parity独立锚点与gate/feeding/axis/response匹配、角覆盖和covariance；Gaussian布居或低阶截断只是额外模型条件。

### 校准布居后仍可有全局多解：精确U对

RB67-14在相同四成分模型给出正交U，保留S及R2/T2/R4/T4全部二次型。a=(1,1/2,1/3,1/4)与b=Ua均四分量非零/正，固定p0=p1=1/4，两个解各自local rank3，却具有相同全部W、Δ和pointwise photon matrix。a的fractions为(144,36,16,9)/205，b约为(0.10435,0.26266,0.11516,0.51783)。精确U、向量、fractions与rank2 trace-zero lifted证书在[[rose-brink-1967-phase-defined-angular-distributions]]保存，73项由主代理复现。

较简的pure-M1向量也映为E2/E4组合，fractions=3/35、32/35，相同photon响应；它没有说明实际核素具有显著E4。给定photon ranks/low-order truncation或额外strength/ICC/核末态信息可以改变判断，须各自给证据。U在固定convention内改变multipole内容，同方向核末态trace隐藏某些projected channel phases；没有声称跨方向coherence、cascade或total τ同一。这里证明的是一组global pair，不是完整反演分类。

### Case C 的局部满秩与K6消失条件

合成3+→1+保留E2/M3/E4和三个unknown aligned population参数时，完整W/Δ含K2/4/6六shape coefficients。RB67-15在三amplitudes非零、所有w正的seed给6×5 exact rank5；所选五coefficients有局部inverse。前例2+→2+的连续联合解不能直接套到这个spin组合，rank也不证明global唯一。全部forward expressions/41-check/minor在[[rose-brink-1967-phase-defined-angular-distributions]]保存。

PureE2因L2+L2<6使A6=C6恒零；properly calibrated nonzero K6可排除此pure-mode模型。Zero A6可来自isotropic B6=0或higher amplitudes的R6干涉抵消，即使B6≠0。u=1/2时v=16√10−7√35/2±2√(750−140√14)给two非零M3/E4组合的A6=0，C6不必为0。需同时对照population、完整angular/polarization curve、response与covariance，不按未见K6删除所有higher candidates。

### Case C：局部inverse的全局分支与双K6零点

RB67-16给E2/M3/E4的精确U_C reflection。a=(1,1/2,1/3)与U_Ca同physical S、六个完整W/Δ coefficients，两个five-input点都local rank5，却有不同fractions；新的b fractions约(0.37816,0.29360,0.32824)。所以更多角系数和一个local inverse仍要检查global branch。详细矩阵、exact vectors和29-check在[[rose-brink-1967-phase-defined-angular-distributions]]保存。

pureE2也映为三成分非零的(5/21,2√14/21,2√10/7)，fractions=(25/441,8/63,40/49)，B6≠0但A6=C6均0且完整curve同pureE2。它提供response cancellation的联合零点，不能把未见两个K6视作higher amplitudes为零；独立higher-strength界/模型条件仍要明示。此证书不扩到cascade/ICC/total τ或其它spin。

### 加入total ICC与τ后，E0仍可能完成不同γ解

LKH82-7将RB67-14 pair与selection-allowed E0相连。在明确no-penetration/no-pair/complete inventory模型，κ_j=Σf_L,jα_e,total,L，若αobs≥maxκ且λγ、Ω_e,total>0，取T_j(E0)=λγ(αobs−κ_j)，两不同fractions同时有same photon curves/gamma scale、total ICC与τ^-1=λγ(1+αobs)。α低于某κ的非负约束可以排除此model；λγ/τ一致性失败不能靠E0任意修复。

额外shell contrast d_s=η_s(κ_b−κ_a)−(κ_s,b−κ_s,a)，η_s=Ω_s/ΣΩ；d_s可测时shell/total提供新约束，全部δκ_s=η_sδκtot时仍无法分开。shell/shell比可能盲于同比例差异，counts共用的统计covariance与独立信息数要分别记录。详细47-check、单位、reference-zero/closed-shell边界与Poisson特例在[[lange-kumar-hamilton-1982-multipole-admixtures]]；没有赋原子数值或实际核素。

### penetration 的基线与 E0 排除条件

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-12（p.169/PDF51）明给 `αM1(λpen)=αM1,ref[1+B1λpen+B2λpen²]`，作者叙述为增强 IC；本题没有系数或允许 λ 域。固定基线 κ 下非负 E0 要求 αobs≥κ；未知修正时应核物理允许域中的 lower bound，不能任意改 κ 或忽略作者的增强条件。独立固定 t=δ²、M1/E2 截断、E2 不修正且修正 M1 系数非负时，仍有 `κK≥t αK(E2)/(1+t)` 的条件下界。未知 t 或 electric correction 可使该下界失效。

KB08 p.207–208 Eq.24/NP–SC 比较表明，现代 DF/FO 已近似含 SC penetration，不可未经 reference mapping 再乘 NP/Hager 修正。FO/NH 是 vacancy 选择，No Hole 不意味着 no penetration。固定 λ 时 scalar ICC 仍不给 δ 的符号；线性 B1λ 可含 penetration 参数自身的符号信息，需与 photon mixing phase 分开。完整零参考率、E0/penetration 分配和 K/total 寿命边界见 LKH82 source；35项符号推导不作为真实核修正或实验结果。

### 级联对单 γ 多解的判别依赖几何与相干

[[rose-brink-1967-phase-defined-angular-distributions]] RB67-17 扩展原2+→2+ U pair为一条合成2+→2+→0+、独立pureE2末支。第一 γ 沿初始alignment轴时，两支整个中间态 R 相等，任何固定次级分析器都盲；只把第一 γ 改至θ1=π/3、第二保持θ2=π/4（φ均0）后，pure边界ΔW12=45/256、full-support ΔW12≈0.02288275。Δ为归一强度差，不是实验DCO阈值或全局唯一证明。

该对的判别来自第一 γ 坐标系内 off-diagonal spin coherence；random初态或理想该轴dephasing使差异归零。Odd Q可存在于even K张量，不能混同。R的trace是W1，conditional density才是R/W1；W12/W1与joint W12的统计信息还需共享计数/归一协方差。末支、多极截断、布居/响应与中间寿命/deorientation必须独立取证。原Eq3.73 random-source/two-component条件及148项相位/完整Ω归一核验见source，不向真实核素外推。

### 同一个级联观测可补局部约束，但不增加重复信息

RB67-18 在旧 `(x,y,z,p0,p1)=(1/2,1/3,1/4,1/4,1/4)`、相同2+→2+→0+/pureE2/离轴角点，加一个 normalized W12 使 unknown-population rank4→5；旧核导数及5×5行列式都经56项精确核验。它给该模型/seed附近的局部逆，不证明所有振幅、Jπ和布居候选全局唯一。独立已知布居的rank3→3仍可增进离散branch判别，rank与global ambiguity须分开。

等布居仅使固定population的amplitude rank0→1（unknown p时rank2→3），不够完整反演；“随机初态对该U pair盲”不等于“级联对所有amplitudes都盲”。`W12/W1` 与W12通过已知形状确定的正W1作可逆行变换，只能作为等价替代信息，需要共享 covariance。未标定的coincidence-yield尺度是额外nuisance，不在五变量满秩证明内。精确证书、source/归一条件见[[rose-brink-1967-phase-defined-angular-distributions]] Local Rank with One Cascade Coordinate。

### 加一个级联约束后，局部inverse仍可有全局分支

RB67-19 在RB67-18同一五normalized outputs下，用可复现interval contraction认证第二个正布居、不同fractions解。原exactseed和新盒中的zero各自local rank5，仍映到同四shapes+一个W12；conditionalW12/W1也随之相同。盒中“唯一”仅为该邻域，不是全局所有roots唯一。证明用exacttarget/radical多项式、positive S清分母和严格端点/收缩界，非只靠数值residual。

第二分支改变了布居，结论只给unknown-population模型，不能反证independently fixed-population切片的唯一性。两chartγ份额不同不等于真实核可实现/同等可信；共同many-body current、long-wave/absolute-rate约束和response须另核。27-check parent复现与58-check独立审计及两组参数到[[rose-brink-1967-phase-defined-angular-distributions]]；不作核素实验结论或L4。

### 配对反证可设计消产额比值，需独立标定

RB67-20 对认证global pair仅加预定secondaryθ2=0、保留firstθ1π/3，以旧θ2π/4为分母，新/旧理想W12为约0.42419270与0.37276339，interval差严格排除0。`μj=c εj Wtilde_j`中的共同c能被比值消去，前提是same selected population/cascade/ordering/时间窗及独立relative-efficiency/acceptance标定。不同选择留下ca/cb，counts/ε不能自动纠正finite acceptance；这不是通用DCO数值或所有候选全局唯一证明。

28-check及原box传播到[[rose-brink-1967-phase-defined-angular-distributions]]，无counts/covariance或finite-count separability。Shared gate/calibration与derived ratio需joint传播，零观测分母另处理；不能把理论pair差直接写成实验排除。

### 用长波与矩阵元约束说明率截断

LKH82-14 用同pair的E4/E2 physical electric RME定义 `χ=M4/(R²M2)`，在所用long-wave rate近似内给 `r42=(5/23814)(qR)^4|χ|²`。小qR还需独立|χ|界或absolute-strength/matrix-element约束；选择定则不提供χ自然尺度，lower M2 hindered/zero尤其需要另核。RB normalized辐射振幅已经含energy/multipole因素，不能将aE4/aE2直接当χ。

Formal global pair分别需约34.5065和100.6230除(qR)²的|χ|；未给真实E/R/current，不据此排除真实核模型。一个partial-rate小也不意味着角分布/偏振误差同样小，interference按振幅尺度进入。系数、单位和ratio端点46项核验及source current/retardation条件见[[lange-kumar-hamilton-1982-multipole-admixtures]]，不外推M3/M1或所有高阶都可忽略。

### 从被省率到测量误差：归一与支持条件

RB67-21以同initialρ、transition/E/radialmode与SR>0重构：省略totalphoton-rate份额ε时，full与renormalized-retained radiation-state距离为√ε，同boundedfinite-bin effect的absoluteprobability差≤√ε。干涉control可达O√ε；不能直接用ε作angular/polarizationerror。改fitρ、time/nonγ或measurementchannel需另控，postselection小success概率会放大。

RB67-22另加fixedJi/Jf/parity有限Hemit支持，三原题κ2/5/7使角平均1的W满足absolutepoint-bound κ√ε；positivepol强度也成立。它使用full emittedspace D含finalspin，不把arbitraryreducedD套同κ。节点relative、signedStokes、polarizationratio、unknownJ和unboundedunfolding各有额外条件。FullΩ/isometry、CP/filter、CG谱与locators见[[rose-brink-1967-phase-defined-angular-distributions]]；95/329项parent核验均为L2理论，未提供实际omittedfraction或experimentalerrors。

### 标清极化属于哪条γ和哪种选样

RB67-23给firstE/Mduality控制：第一γ方向已tag但pol未测/只circularselected时，A′q=qAq使middleR完全同，photon2任意fixedmeasurement也同。Firstlinear tag可以交换jointintensities；source初态random时firstlocalP0仍可有joint信息。合成2?→2+→0+的γ2P=3/17对M1/E1firsthyp都同，firstlinear-tag + secondarydirection才给相反±3/17。

γ2polar证据直接归于γ2的E/M/levelparityrelation，firstparity可经independentanchors链式推断，不能重复计作directγ1measurement。坐标/Jones/response、tag与ordering明确后比较，不把positivepolsign作通用type阈值。99项source-phase/CG控制与全部boundary见[[rose-brink-1967-phase-defined-angular-distributions]]，不产生实验宇称赋值。

### 截断先验、布居下限与 parity null 的依赖

同一 2+→2+ 的 M3/E4 被省率可在独立 hard-support、磁 moments/domain 与正 B(E2) floor 下条件性上界；小 qR 或目标 M1/E2 拟合本身不提供这些先验。LKH82-15/16 写明单位、gradient 系数、rate ceiling 与 failure edges，不能用参数拟合精度代替 model-error bound。

RB67-24 的独立同母态 pure-E2 reference 只在 J=2 symmetric-diagonal 模型中把 A2/A4 映为完整组布居。独立 rmin>0 与 rmax 给 W_R≥(2Ji+1)rmin 和相对误差≤[(rmax−rmin)/rmin]√ε；需联合不确定域、选样与响应核验。未控 orientation/coherence 或换成 cascade-conditioned 中间态后，不能沿用该 floor。

RB67-25 区分 odd-K 消失的充分条件与逆命题。放松核态确定宇称的同 rank E1/M1 形式控制可 W isotropic 而 circular polarization 非零；accepted odd counts 又可由合法响应制造。没有 odd K 不证明 parity，odd counts 也不独自证明 parity mixing。来源条件、η 的 interaction-amplitude 单位/相位和未作实验推断的边界见 [[rose-brink-1967-phase-defined-angular-distributions]]。以上均为 L2 自审知识。

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
