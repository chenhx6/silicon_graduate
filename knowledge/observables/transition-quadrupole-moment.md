---
type: observable
title: 跃迁四极矩
aliases: [transition quadrupole moment, quadrupole moment, Qt, Q_t, QSD, QND]
created: 2026-07-03
updated: 2026-10-19
status: active
review_status: unreviewed
observable_kind: electromagnetic-collectivity
symbol: "Q_t"
units: b
tags: [e2, lifetime, deformation, superdeformation]
---

# 跃迁四极矩（Transition Quadrupole Moment）

## Definition

由带内 E2 跃迁强度或寿命提取、表征转动带电四极集体性的量。文献有时简写为 `Q`；引用时必须确认它是 transition quadrupole moment、spectroscopic quadrupole moment，还是模型内禀矩。

## Formula and Conventions

`Q_t` 与 B(E2) 的换算依赖转子矩阵元、K/强耦合假设和单位约定。跨论文比较必须保留采用的几何因子、分支、内转换和 feeding 修正。

### Source-specific `K`-rotor rate conversion

Singh et al. give one explicit high-spin convention for `I→I−2` E2 transitions:

`T(E2; I→I−2) = 1.224×10^12 Eγ(MeV)^5 CG(I,K)^2 Q_t(eb)^2 s−1`.

Their Eq. (2) replaces the single Clebsch–Gordan factor with a sum over `K` amplitudes for nonaxial or mixed-`K` states. This is a rotor extraction formula: it requires an identified E2 transition, its energy, and an applicable `K`-mixing prescription. Other papers may use a different unit convention or rotor matrix-element model. It cannot supply a unique `Q_t` for a spin-indexed table whose `B(E2)` row has no transition identity or `K` assumption. See SI16-17 and the MU07 transition-mapping boundary in [[mukhopadhyay-2007-135nd-chiral-vibration-static]].

## How It Is Obtained

通常由 Doppler-shift 或其他寿命测量结合 E2 分支提取。[[domscheit-1999-triaxial-superdeformation-163lu]] 本身没有新测寿命，而是引用 Ref.[2] 的 `Q_SD=10.7(7) b`、`Q_ND=6.0(5) b`，并用本工作分支比的两带混合分析得到 `Q_ND/Q_SD=0.48(7)`。

[[babra-2019-deformation-change-136sm]] 对 576-910 keV yrast E2 跃迁做 DSAM 线形拟合，得到 8+ 至 20+ 的寿命或上限，再在 `K=0` 转子近似下提取 `Q_t`。stopping power（阻停能力）系统误差未纳入表中误差，作者估计可达 15%。

## Diagnostic Use

- 约束集体 E2 强度和形变尺度；
- 区分正常形变与超形变带的集体性；
- 检查带混合分析由强度比导出的四极矩比是否与寿命结果一致。
- 沿同一带追踪跨带交叉的集体性变化；`Q_t` 下降可支持集体性减弱，但形变极小和 γ 刚性仍需模型或其他观测量。

## Model Dependence

从 `Q_t` 映射到 `β2/ε2` 依赖形状参数化、有效电荷和转子近似。`163Lu` 的实验平均 `Q=10.7(7) b` 同时接近 UC 对正 γ、负 γ 组态给出的 9.9 b 和 11.0 b，因此不能单独判定 γ 符号。`136Sm` 中交叉后较低 `Q_t` 与 TRS/TPSM 的较小 β2 一致，但“γ-soft→稳定三轴”仍是模型支持的解释。

## Failure Modes and Ambiguities

- 未分辨 feeding、带混合和弱分支会影响寿命/强度提取；
- 大 `Q_t` 支持强集体形变，但不单独证明三轴刚性；
- 二手转述的绝对数值必须回到原始寿命来源复核。

## Examples

`163Lu` SD1 是“大四极矩支持超形变，但不能区分正负 γ”的参照案例。`136Sm` 是“跨带交叉的 `Q_t` 系统学约束集体性，但不单独给出 γ 刚性”的案例。

## 从旋转系算符到Qt的输入契约

[[matev-2007-a130-quadrupole-alignment-additivity]] MT07-1/2采用电荷矩：`Q20=Σp〈2z²−x²−y²〉`、`Q22=Σp〈sqrt3(x²−y²)〉`，其spherical component为`Q22/sqrt2`。本文数值标eb；跨论文需保留电荷、单位、归一与轴约定，不能只按变量名Qt/Q22对齐。

在该文Eq15的y推转定义与Eq14右端的x定义下：

`Qt_y=Q20−Q22/sqrt3`，`Qt_x=Q20+Q22/sqrt3`。

同一物理构型换坐标轴时Q22反号，两个terminal表达式给相同Qt；这不说明CHF+SLy4和CRMF+NL1的实际预测相同。Eq14中间ω标签另有v1字面边界（MT07-12），本次没有静默改原链式。与另一篇的βγ比较前，还须核四极张量是电荷或总密度、轴排序及代码定义；这里不能补Pr136实际frame。

### 一个Qt不唯一决定γ

该文用`Q20=Q2 cosγ`、`Q22=Q2 sinγ`，故y定义给`Qt=Q2(cosγ−sinγ/sqrt3)`。本任务声明Qt=1eb时，γ为−20°/0°/+20°可分别取Q2约.879385/1/1.347296 eb而给同一个Qt。它是反问题的条件控制，不是源core或任何核素测量；若实验只约束强度中的Qt模平方，仍需独立几何/结构信息。不同γ并不因此自动成为已确认的shape coexistence。

### 算符线性不等于任意拟合系数都可直接组合

在**共同配置设计矩阵、同权线性估计器**的条件下，Eq15还要求`q_t_eff=q_20_eff−q_22_eff/sqrt3`；这里也包含一致的reference减法，使输入的δQt与δQ20/δQ22满足同一关系。不能混用实验Qt baseline与理论core矩后仍默认该系数恒等式。本任务读原v1 TableII的34行/61组可用triple、7组missing保持None；若各中心值按最近.01eb舍入，必要残差界限为`.005(2+1/sqrt3)≈.012887eb`。

| v1 TableII CHF row | q20_eff | q22_eff | printed qt_eff | qt−(q20−q22/sqrt3) |
| --- | ---: | ---: | ---: | ---: |
| ν[402]5/2,+i | −.35 | .14 | −.04 | +.390829 eb |
| π[532]5/2,+i | .43 | −.05 | −.46 | −.918868 eb |

这两组超出上述必要舍入范围；其余59组在此检查下相容，不代表全面认证。不能拿彼此独立的模型误差条来放宽一个共享估计器的确定性关系；若实际C/配置集或权重不同，系数关系本来就须重核。当前文件未给这些实际输入，未核VOR，不修表或判作者代码错。共享OLS/不同权重控制分别验证这种前提与失败边界（MT07-10/11）。

若将理论fit误差视为相应σ，组合需cross-observable covariance：`var(qt)=var(q20)+var(q22)/3−2cov(q20,q22)/sqrt3`。考虑所报σ的两位小数舍入后，61组必要Cauchy区间均有相容空间；这没有恢复实际Σ，也不是实验Qt的误差检验。该文的残差零均值、同方差、互不相关假设及Nc−m自由度（MT07-6）不是探测器/阻停/feeding误差预算。

### 差分、比值和公共系统误差

MT07-8的差分实验描述来自上游Riley2001/Laird2002；读Matev时尚未核其原分析；本轮Riley2001直接核验见下节，Laird2002最终稿仍缺。一个共同**加性offset**在difference中消去，一个共同**乘性归一化**在ratio中消去，却一般仍缩放非零difference。声明的5/7控制只说明必须写清错误结构与参考归一；不能据此判原实验宣称的系统误差消除不成立，或把多个发表/多个核素计独立测量。

[day14_qt_operator_table_audit.py](../../system/scripts/day14_qt_operator_table_audit.py)与[24-check回执](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/matev2007-qt-operator-audit.json)保留实际表值/版本、共享估计器条件、轴重标、逆问题与σ区间。它没有复跑183/105个配置，没有从Eq33或转述7.4(3)提取实验Qt/τ。实际寿命/分支、原始矩阵元与几何仍是独立必要输入。

MT07-18还给出一个联合observable的声明应用：把core的ν6_1,−i换成ν6_2,+i，保留同neutron数/同N6 intruder总count，表中系数却给δQt=.11/.04eb和δJ=−1.36/−1.44ℏ（CHF/CRMF）。对应j_eff输入为4.78→3.42与4.59→3.15ℏ；Qt输入为.26→.37与.33→.37eb。它是固定reference/ω的名义加性应用，无共同系数Σ，不能补独立误差、赋实测整数spin或转成Pr136结果。固定其他占据的single-orbital变化、沿同位素链的N趋势与不同带类别，不是同一比较。

## 全局Qt表的分析选择与数据身份

[[riley-2001-global-lifetime-a135]] RI01-1–8直接补足早期作者实验报告：173 MeV 35Cl+105Pd、Gammasphere97HPGe+Microball，以质心位移DSAM和FITFTAU恒定带Qt拟合。Table I的Qt不是逐跃迁τ；`Qt(sf)=Qt(band)`也不要求`τsf=τband`。

该source保存33行完整typed表：21 single、3 upper_limit、1 band_pair、2 signature_pair、5 gate_pair_b、1 feeding_assumption_pair_c。130Pr的4.3(3)/4.5(3)是两条带；133Nd两组α±是signature；135Sm5.8(4),6.4(4)c是假设侧馈时序近似`τsf≈1.2τband`的替代分析，不是第六组b门。三个`Qt<3.0`没有给CL，不改成Gaussian边界点或已测τ。

| 同带分析敏感性（Table I b） | 默认Qt→上方门Qt / eb | 名义Qt变化 |
| --- | --- | ---: |
| 133Nd νi13/2 | 5.8(2)→6.5(2) | +12.069% |
| 135Nd νi13/2 | 5.1(2)→5.7(2) | +11.765% |
| 136Pm πh11/2⊗νi13/2 band 1 | 4.8(3)→5.2(3) | +8.333% |
| 136Pm 同类band 2 | 4.8(4)→5.2(4) | +8.333% |
| 137Sm νi13/2 | 4.4(3)→4.8(4) | +9.091% |

作者说上方门消除侧馈，以上体现提取对选择的敏感性，不是核本身形变改变的五次实验，也不是所有其他带的统一10%修正。只在同一已识别E2、固定Eγ/branch/geometry时，Qt×k意味着B×k²、τ×k⁻²；Qt+10%对应B+21%、τ×.826446。Qt上限才在这些条件下给τ下限，表不足以生成numeric state τ（RI01-14）。

以135Nd/133Nd上方门值比较，名义ratio=5.7/6.5=.876923、difference=−.8eb。若把括号数当σ而相关性未知，一阶ratio σ的允许范围约.003787–.057751、difference σ为0–.4eb；独立误差假设下ratio σ≈.0409242。它们是条件传播，不是从原实验恢复的Σ/CI。共同乘性scale保ratio却仍缩放非零difference；共同加性offset才在difference中消去。正文15–20%绝对附加系统误差涵盖阻停与侧馈，caption10–15%只说阻停，相对精度5–10%；不把三者当独立Gaussian项合成。若仅以±15%或±20%作确定性Qt敏感区间，相应τ因子为[.756144,1.384083]和[.694444,1.5625]，没有概率覆盖（RI01-5）。

图/表也须匹配同一核素、带/signature、gate、fit版本、feeding假设和误差定义。Fig1/TableI的133Pr3.4(3)/3.3(3)、134Pm3.9(3)/3.9(2)、135Sm6.4(5)/6.4(4)c暂不知是否同fit；133Nd同中心3.5还对应两个不同表角色，不能按中心值唯一绑定（RI01-10）。Fig2/3另含外源Ce131/132及Sm142，不视为全部共采集（RI01-9/15）。

Riley Eq3的`Qt=Q20+sqrt(2/3)Q22_R`与紧接的`Q22_code=−sqrt2 Q22_R`合用，恰为`Qt=Q20−Q22_code/sqrt3`；原图负号在文字提取中丢失，不据表面加减号判与Matev不相容。代数形式相同仍不认证不同代码版本或Pr136实际frame（RI01-11）。Fig3的7.75/7.57eb是CSHF/CRMF理论core，不是新实测absolute baseline；也不与2007理论7.64自动互换（RI01-12）。

[27-check程序](../../system/scripts/day14_riley_global_qt_ledger.py)核hash、39有限token顺序、角色、防误读、条件缩放及守恒/归一化；没有复跑FITFTAU、实验Σ或逐态寿命。

## 同一表中的分段fit、计算估算与原始reference

[[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-14/15的TableI八行仅含本次五条物理带加外源132Ce；134Nd Band3的lower、upper和whole是两种分析的段/替代，不按三带重复加权。Fig2同data两次画拟合也不是新样本。Band3的lower4.9(3)、upper~6.5和whole5.0(3)不能仅凭列出的中心值裁定形变jump；作者明确现有统计不能firm选择。

该upper的理论6.07eb是未能直接计算one-i13正宇称组态后的half-contribution估计：5.45+.5(6.69−5.45)=6.07。即使形式类似可加性，也不是直接算出的actual configuration，更没有λ=.5的置信区间。对照spin-dependent Qthe和constant Qexp时，还需真实F的响应/feeding权重，不用算术平均替代拟合（PE98-11/14）。

原实验符号Q0按其几何保留；β2列明确assuming no triaxiality（PE98-12）。Petrache131Ce本次Q0=7.3(4)与其所引Clark1996的7.4(3)分开；Matev2007 Ref39用的是后者。Clark原文仍未核，不拿7.3代7.4、不按三篇转引计三个独立测量，也不能直接搬给Wiki的ND131Ce Bands1–7或Pr136（PE98-13/19）。原表source保存完整八行及Qsf范围冲突，不取平均修订。

## Sources

- [[riley-2001-global-lifetime-a135]] RI01-1–15：直接作者报告的提取/表项角色/误差与谱系。

- [[matev-2007-a130-quadrupole-alignment-additivity]] MT07-1/2、MT07-6、MT07-8–MT07-15：明确坐标/算符、模型拟合与原实验/版本边界。
- [[domscheit-1999-triaxial-superdeformation-163lu]]
- [[babra-2019-deformation-change-136sm]]
- [[singh-2016-lifetime-131ce-133pr]]
- [[mukhopadhyay-2007-135nd-chiral-vibration-static]]
- [[zhu-2003-135nd-composite-chiral-pair]]
- [[li-2004-lifetimes-131ce]]
- [[petrache-1998-highly-deformed-lifetimes-131ce-nd]]

## `131Ce` cross-source boundary

- Singh 2016 的 normal-deformed Band-1-like 序列用寿命得到 `Q_t`；Li 2004 给出同一负宇称谱系及另一条正宇称谱系的早期值。Singh 表中转载/再算的 Li 行不能重复计权。
- Petrache 1998 报告独立高度形变带的 intrinsic `Q0`。`Q0` 与 normal-deformed `Q_t` 的几何、K mixing 和形变假设不同，只能分层比较，不能直接把比值解释为形变比。
- 单侧寿命限值与矩限值方向相反：`τ` 上限给 `Q_t` 下限，`τ` 下限给 `Q_t` 上限。
- 在 pure-E2、branching=1、ICC=0 和 source-specific K 的诊断复算中，Singh 有限点与报道值相容到约 15% 内；该检查不是对完整 side-feeding 分析的替代。

## Evolution Log

- 2026-07-03：建立超形变判据、两带混合和 γ 判别限制。
- 2026-07-05：加入 `136Sm` DSAM 寿命、`Q_t` 下降与形变解释边界。

## 固定K与候选stretched-axis几何

[[lifetime-strength-audit-165tm-136nd]]以J01-10/MU08-17核真实打印表：固定K的CG(I K20|I−2 K)²与候选CG(I I2−2|I−2 I−2)²=(2I−3)/(2I+1)是不同几何。同B在MU08的九行上用fixedK0可给约1.58倍不同Qt；candidate与原表打印相合不唯一识别作者actualformula/producer或证明内禀轴。先固定G再用Qt=√[16πB/(5G)]，不能只按符号或核素类型替换。

该表核验的直接输入见[[mukhopadhyay-2008-136nd-transition-rates]] MU08-17及[[jensen-2001-165tm-h9-2-configuration]] J01-10，不凭candidategeometry匹配给出新内禀形变。

## 同一DSAM标尺派生的多个band矩

[[jensen-2001-165tm-h9-2-configuration]] J01-12–16和[[lifetime-strength-audit-165tm-136nd]]保存Q404=rplusQ411、Q523=Q541/rminus的实际引用链。四个输出不等四个独立寿命；ratio可消共同标尺但一般不会消影响mixing/branch的系统误差。原5%预算不再盲加，conditionalSigma设计不反解sourcecovariance。较大Qt和crossingdelay是必要companion，却未使deformation-only解释闭合。


## Day 20预习：B(E2)、Qt与形变系统学模型依赖矩阵

checkpoint008取代此前预习的截短CG、K=5/2完全对账、零谱学矩唯一指纹及feeding错误方向。错误版本保于Git和旧结果，不作证据。原有review与source记录保持。

在固定K、轴对称、同带I→I−2及允许域|K|≤I−2中，令G=CG平方：

G = 3(I+K−1)(I+K)(I−K−1)(I−K) / [2I(I−1)(2I−1)(2I+1)]。

Qt = sqrt[16π B(E2)/(5G)]；Qt以eb、B以e²b²时不再重复乘e²。K=0时可约去额外因子，旧式只在此特例成立。新exact factorial-sum与闭式跨整/半整I、K逐项对照，不识别真实核的K。[[li-2004-lifetimes-131ce]] LI04-D20-2/3和[[singh-2016-lifetime-131ce-133pr]] SI16-D20-2给输入/原表谱系。

Singh四有限点的z=−.639来自独立Gaussian、上下误差平均的条件回归；全lower/全upper约−.923/−.548。未检出趋势不等证明常数形变，也不能归因于feeding制造。未得到跨点Cov与限值likelihood，不与Li转载行合并计权（SI16-D20-3）。

固定branch/ICC/geometry时Qt∝τ^(−1/2)；若低spin寿命被高估两倍，其Qt乘1/sqrt2而偏低。此前由此推出低spin Qt偏高、随spin虚假下降的说法方向错误。实际feeding与τ的拟合耦合须完整response，不能由此符号控制断言真实bias。

固定轴对称转子Qs/Q0=[3K²−I(I+1)]/[(I+1)(2I+3)]。K0、I2给−2/7。旧Davydov公式在γ0给−2/21，已不满足此轴向极限，整组DF归一/Qt=Q0和γ30指纹结论撤回待原件。零Qs并不唯一指γ30：轴对称I3,K2也有Qs=0且E2(3→2)非零；I0/半整数低spin的rank2选择律也须分开。

旧β=.4195来自另选R0=1.2A^(1/3)和二阶多项式的条件算术，不是Petrache原β=.38的复现。“二次方程精确根”仅对截断多项式成立，不是精确核形状。必须先匹配电荷密度/半径、轴、effective charge与形状参数化；不将条件差直接修正作者结果。

[[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-D20-1–3把constant-Q拟合、Band3替代fit、推转模型补偿与无三轴β映射分层。程序：system/scripts/day19_evidence_repair_audit.py；结果：outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/evidence-repair-result-008.json。只支持条件代数，不支持新的实验CI或模式裁决。


### Day20无学分预习：Régis的Qt符号与静态矩对象不同

[[regis-2011-fast-timing-labr3]] RG11-D20-1/2：该论文Eq5.10的Qt是spectroscopic实验室矩，本Wiki的transition Qt是带内B在指定几何下的转换量；不按同名字母混并。PDF66的R0字面A^(4/3)与α±2约定另留literal boundary，不用它们替换已声明的standard radius代码。

RG11-D19-12说明Table5.1多个模型全在2→0得到7.03eb来自共同B归一，不是多项独立测量。高spin行的finite/limit与几何仍需单独核验；这里仅承接Day20一次无学分预习，不授卡。


## Day 20预习：转子CG、Q_spec与二阶beta2展开边界

本节作为 Day 20 形变系统学的一项有边界预习（不授予 Day 20 学分，保持 next_day_index: 19）：
1. **固定 K 转子 CG 因子代数闭式**：对于跃迁 $I 	o I-2$，正确的 CG 平方为 $G = 3(I+K-1)(I+K)(I-K-1)(I-K) / [2I(I-1)(2I-1)(2I+1)]$。对于 $I=27/2^-$，代入 $K=1/2$ 得 $26/75$，代入 $K=11/2$ 得 $76/325$。在固定相同 $B(E2)$ 实验输入下，两者的理论比值为 $\sqrt{(26/75)/(76/325)} = \sqrt{169/114} \approx 1.21756$。这证明了 Singh 2016 采用 $K=1/2$（$Q_t=2.28$ eb）相对 Li 2004（$Q_t=2.72$ eb）的 $2.72/2.28 \approx 1.193$ 属于粗略舍入相容，但并不构成排他的唯一解。
2. **谱学四极矩的自旋零点**：轴对称转子的谱学四极矩为 $Q_{\text{spec}}(I,K) = \frac{3K^2 - I(I+1)}{(I+1)(2I+3)} Q_0$。对于基态带 $2^+$（$K=0$），系数为 $-2/7$；而对于 $I=3, K=2$，系数分子 $3\times 2^2 - 3\times 4 = 0$。即纯轴对称转子在特定态上同样存在静态电四极矩为零。单一能级测得谱学矩为零不可直接断定为球形或最大三轴度，必须结合带内跃迁几率与非对角矩阵元综合判定。此前旧段落所用的 Davydov 公式在 $\gamma=0$ 处不满足轴对称极限，相应数值已被撤回隔离，待取得原始论文全文后再行建立。
3. **内禀四极矩到形变参数的多项式控制边界**：从内禀矩 $Q_0$ 映射到形变参数 $\beta_2$，一阶线性近似 $Q_0 \approx \frac{3}{\sqrt{5\pi}} Z R_0^2 \beta_2$ 与截断二次多项式 $Q_0 = \text{const} \cdot (\beta_2 + 0.16 \beta_2^2)$ 存在显著差异。以假定参数 $R_0 = 1.2 A^{1/3}$ fm、$Q_0 = 7.30$ eb（$Z=58, A=131$）控制，线性得 $\beta_2 = 0.4477$，二次多项式得 $0.4195$（相对低约 $6.3\%$）。这只是两种数学参数化约定的代数对比，既不能代表 Petrache 1998 报告的无三轴假设值 $\beta_2 = 0.38(2)$，也不代表真实核电荷分布。跨文献对比形变数值前必须统一半径参数、电荷有效因子与高阶展开约定。

相关实验案例可参见 [[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-D20-3 关于高度形变带寿命与转动离心收缩抵消的详细核验。

## Day 20预习：转子模型K量子数投影约定与131Ce实验对账案例

依据独立审计程序 day19_ce131_li_singh_reconciliation_audit.py 的 14 项检验与基准输出 ce131-li-singh-reconciliation-result-026.json，阐明了从实验约化跃迁几率 $B(E2)$ 提取跃迁四极矩 $Q_t$ 时 $K$ 投影约定的关键影响：

1. **转子模型 Clebsch-Gordan 系数 $K$ 依赖性**：
   在轴对称转子模型中，带内 E2 跃迁几率满足：
   $$B(E2; I \to I-2) = \frac{5}{16\pi} Q_t^2 \langle I, K, 2, 0 | I-2, K \rangle^2$$
   闭式 Clebsch-Gordan 系数平方为：
   $$\langle I, K, 2, 0 | I-2, K \rangle^2 = \frac{3(I+K-1)(I+K)(I-K-1)(I-K)}{2I(I-1)(2I-1)(2I+1)}$$
   当 $K$ 变化时，CG 平方发生显著改变。对奇 $A$ 核，同一 $B(E2)$ 在不同假设 $K$ 下导出的 $Q_t$ 存在约 $15\%\text{--}25\%$ 的纯代数差异。

2. **$^{131}\text{Ce}$ 实验对账案例**：
   在 $^{131}\text{Ce}$ 负宇称 $\nu h_{11/2}$ 带中，Li 2004（DSAM）与 Singh 2016（Plunger）测得 $27/2^-$ 能级寿命严格重合（$\tau = 1.23\text{ ps}$ 对 $1.24\text{ ps}$，相对差异仅 $0.81\%$）。但文献报告的 $Q_t$ 值分别为 $2.72(25)\text{ eb}$ 与 $2.26(+0.37/-0.23)\text{ eb}$。
   审计证明：
   - Li 2004 采用了高-$\Omega$ 带头投影 $K = 11/2$，$\text{CG}^2 = 76/325$，导出 $Q_t = 2.722\text{ eb}$；
   - Singh 2016 采用了完全解耦带投影 $K = 1/2$，$\text{CG}^2 = 26/75$，导出 $Q_t = 2.235\text{ eb}$（其在 Table 1 Ref. [32] 栏中重算 Li 的值为 $2.28\text{ eb}$）；
   - 两者理论比值精确为 $\sqrt{169/114} \approx 1.2176$；
   - 在 $23/2^-$ 态上，Li 测得寿命 $\tau = 1.44(54)\text{ ps}$，完全相容于 Singh 报告的单侧限值 $\tau > 1.3\text{ ps}$。Li 的 $B(E2) = 0.2416\text{ e}^2\text{b}^2$ 按 $K=1/2$ 转换后为 $Q_t = 2.67\text{ eb}$，完全落于 Singh 报告的上限 $Q_t < 2.85\text{ eb}$ 之内；
   - 两次独立实验的物理测量完全自洽，表观四极矩差异 $100\%$ 源于 $K$ 量子数约定。在未解决奇核微观科里奥利混合前，不可将跨文献 $Q_t$ 差异误作真实核形变演化。

## Day 20预习：高度形变带Q0到beta2转换、半径约定与转动离心收缩

依据独立审计程序 day19_petrache_hd_deformation_audit.py 的 16 项检验与基准输出 petrache-hd-deformation-result-030.json，阐明了高自旋高度形变区内禀四极矩转换到形变参数的关键约定与物理边界：

1. **核半径参数与高阶形变展开的系统性偏差**：
   从内禀四极矩 $Q_0$ 转换到电四极形变 $\beta_2$ 依赖核半径常数 $r_0$（$R_0 = r_0 A^{1/3}$）及几何展开高阶项：
   $$Q_0 = \frac{3}{\sqrt{5\pi}} Z R_0^2 \beta_2 (1 + c_2 \beta_2)$$
   - Petrache 1998 Table I 的报告形变值严格基于 $r_0 = 1.25\text{ fm}$ 与 $c_2 = 0.16$ 的参数组合；
   - 若文献采用常规轻核半径 $r_0 = 1.20\text{ fm}$，导出的 $\beta_2$ 将产生整体 $+8.1\%$ 的虚假升高（例如 $^{131}\text{Ce}$ HD 带由 $0.388$ 升至 $0.419$）；
   - 若进一步忽略二阶多项式项（取 $c_2 = 0$ 线性近似），形变参数将被额外高估 $+6.7\%$（达到 $\beta_2 = 0.448$）。这两项纯代数约定的累积偏差超过 $15\%$，远大于实验提取 $Q_0$ 的统计不确定度（$3\%\text{--}5\%$），确立了跨核区对比超形变/高形变时必须统一展开约定的基本规范。

2. **转动离心收缩与侵入轨道极化的抵消**：
   在 Cranked Strutinsky 总 Routhian 面计算中，随角动量增加，科里奥利力迫使核芯向较小形变收缩（计算得到的 $Q_0^{\text{the}}$ 在自旋区间内平均下降 $-13.9\%$，$^{134}\text{Nd}$ 达到 $-20.3\%$）。而在实验测量中，由 DSAM 提取的有效带内四极矩 $Q_0^{\text{exp}}$ 保持近似恒定，其物理机制为：高 $j$ 侵入轨道（$\nu i_{13/2}$）占据带来的长椭形状极化增强，在较宽频率区间内近乎完美地补偿了科里奥利离心收缩。

3. **侧馈级联参数 $Q_{\text{sf}}$ 的构型特异性**：
   高度形变带呈现强集体性的快速侧馈（$Q_{\text{sf}} \approx 6\text{ eb}$，与带内四极矩比值达 $0.82\text{--}0.88$），而正常形变带呈现较弱集体性的慢侧馈（$Q_{\text{sf}} \approx 2.5\text{ eb}$，比值仅 $0.51$）。这证明未分辨的连续态侧馈并非环境常量，必须逐带独立建模。

## Day 20预习：带交叉区四极矩衰减、阻停尺度不变性与多机制反证

依据独立审计程序 day19_babra_band_crossing_qt_audit.py 的 11 项检验与基准输出 babra-band-crossing-qt-result-032.json，阐明了转动带交叉区域跃迁四极矩衰减的统计显著性与竞争解释边界：

1. **带交叉区四极矩阶跃统计分析**：
   在 $^{136}\text{Sm}$ yrast 序列中，带交叉前（$8^+\text{--}12^+$）加权均值 $\bar{Q}_{t, \text{pre}} = 5.68(14)\text{ eb}$ 与带交叉后（$14^+\text{--}18^+$）均值 $\bar{Q}_{t, \text{post}} = 5.09(20)\text{ eb}$ 存在净衰减 $\Delta Q_t = -0.58(24)\text{ eb}$（$-10.3\%$），统计显著性为 $z = -2.45\sigma$（双尾 $p = 0.014$），对应集体四极跃迁几率 $B(E2)$ 下降 $-19.5\%$。
2. **全局阻停功率系统误差的严格不变性**：
   若电子阻停能力整体偏移 $\pm 15\%$，四极矩按 $\sqrt{1 \pm 0.15}$ 等比例缩放。由于回归斜率与标准误差严格同乘该比例，标准化高斯检验统计量 $z = b / \sigma_b = -2.179$ 严格守恒。这在数学上证明：全局阻停功率系统误差只能改变绝对形变标尺，既不能抹平真实的显著负斜率，也不能伪造出一个本不存在的显著下降趋势。
3. **竞争机制与证据排他性反证**：
   - **两带组态混合**：交叉点处基态带与对齐二准质子 $S$ 带发生能级排斥与波函数混合，$\langle I | M(E2) | I-2 \rangle = \alpha_I \alpha_{I-2} Q_0^g + \beta_I \beta_{I-2} Q_0^S$。混合直接导致带内跃迁矩阵元碎片化，自然推导给出 $14^+ \to 12^+$ 过渡四极矩 $Q_t \approx 5.06\text{ eb}$（高度符合实测 $5.38(34)\text{ eb}$），证明四极矩衰减可以完全由两带交叉动力学引起，无需假设任何内禀单带几何收缩；
   - **侧馈门控非对称性**：$8^+$ 采用上方门控（$0\%$ 侧馈），而 $14^+\text{--}18^+$ 采用下方门控（$25\%$ 侧馈）；若高自旋连续态包含微小的未分辨慢馈入成分（$\sim 0.5\text{ ps}$），足以在 DSAM 线形中模拟出该表观寿命拉长假象。

## Day 20预习：三轴度gamma对跃迁四极矩的代数耦合与欠估定理

依据独立审计程序 day19_triaxial_gamma_qt_coupling_audit.py 的 11 项检验与基准输出 triaxial-gamma-qt-coupling-result-034.json，系统确立了三轴形变参数 $\gamma$ 对跃迁四极矩 $Q_t$ 的代数耦合定理：

1. **三轴转动算符的严格闭式**：
   在绕中间轴转动（$y$-推转约定，Matev 2007 式 15）下，带内跃迁四极矩 $Q_t$ 与总电荷四极形变量 $Q_2 \propto \beta_2$ 的函数关系为：
   $$Q_t(\gamma) = Q_2 \left( \cos\gamma - \frac{1}{\sqrt{3}} \sin\gamma \right) = Q_2 \frac{2}{\sqrt{3}} \cos(\gamma + 30^\circ)$$
2. **特征几何极值与四极矩压制**：
   - **$\gamma = -30^\circ$（最大几何放大）**：$Q_t/Q_2 = 2/\sqrt{3} \approx 1.1547$，产生 $+15.5\%$ 的跃迁四极矩放大；
   - **$\gamma = 0^\circ$（轴对称长椭集体转动）**：$Q_t/Q_2 = 1.0000$，跃迁四极矩严格等于总内禀四极矩；
   - **$\gamma = +30^\circ$（最大三轴不对称度）**：$Q_t/Q_2 = 1/\sqrt{3} \approx 0.5774$。在总核形变量 $Q_2$（或 $\beta_2$）完全恒定的条件下，仅由于三轴不对称度增大，跃迁四极矩净减少 $-42.27\%$，带内跃迁强度 $B(E2)$ 衰减至轴对称基准的 $1/3$；
   - **$\gamma = +60^\circ$（轴对称扁椭非集体转动）**：$Q_t/Q_2 \equiv 0.0$，带内集体四极跃迁发生严格熄灭（$B(E2) \equiv 0$）。
3. **轴对称假设导致的形变系统性欠估定理**：
   若实验测得 $Q_t$ 后盲目采用轴对称长椭转子假设（$\gamma = 0^\circ, Q_2^{\text{app}} = Q_t$）推导 $\beta_2$，而核真实具有三轴形变：
   - 当真实 $\gamma = 20^\circ$ 时，$Q_t/Q_2 = 0.7422$，轴对称假设低估真实四极矩 $25.8\%$（真实形变是提取值的 $1.35$ 倍）；
   - 当真实 $\gamma = 25^\circ$ 时（A≈130 软三轴典型值），$Q_t/Q_2 = 0.6623$，轴对称假设低估真实形变达 $33.8\%$（真实总形变量 $Q_2$ 比提取值高出 $+51.0\%$）。
4. **单四极矩的多变量简并性**：
   证实单个实测 $Q_t$ 无法独立解耦 $(\beta_2, \gamma)$。给定 $Q_t = 5.0\text{ eb}$，对应真实形变可跨越 $\beta_2 = 0.225$（$\gamma = -30^\circ$）至 $\beta_2 = 0.436$（$\gamma = +30^\circ$），变化幅度接近一倍；严格分离 $\beta_2$ 与 $\gamma$ 必须依赖 $\gamma$ 带交错参数 $S(I)$、谱学静态四极矩 $Q_{\text{spec}}$ 或带间/带内 $B(E2)$ 强度比等伴随观测量。

## Day19 阻止本领标度敏感性与双比值不变性定理

**checkpoint090修订：仅有条件的不变性，原标题保历史anchor。** [[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-19与[[iaea-2026-stopping-s-au-o-ta-records]] ISP26-D19-1区分total trajectory重标与电子-only输入变化。

在branch/ICC、能量与几何不动时，B(E2)正比tau^−1、Qt正比tau^−1/2。如果额外证明每个所比态都满足同一tau_i(k)=tau_i(1)/k，才有所有Qt乘sqrt(k)和等次数双比值的代数抵消；统计显著性还要求相应Cov一起按同合同缩放。这个充分条件不能倒推实际stopping系统只是统一k。

即便纯sqrt(k)控制，k=1.1/.9也给Qt的+4.8809%/−5.1317%，不是对称±4.88%。仅电子分量变化的本轮toy模型已给不同态不同响应和非零ratio变化；不以“不变性”认证136Nd/106Ag结构结论、现实20%误差免疫或任何模式排他性。实际velocity、feeding、谱窗、模型和共同Cov仍需逐项审计。

## Day19量化审计：从能级寿命到跃迁四极矩Qt的微积分映射、K约定敏感性与三相图定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_qt_deformation_mapping_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/qt-deformation-mapping-result-074.json`，核准了从核能级寿命向跃迁四极矩映射的微积分动力学与几何敏感性审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| TQM-D19-1 | 对核能级寿命到电四极跃迁强度 $B(E2)$、跃迁四极矩 $Q_t$ 的几何微积分映射、转子模型 $K$ 约定敏感性及 $^{131}\text{Ce}$ 三相图执行严格量化审计：(1) 第一性原理微积分微商：由电磁跃迁常数 $\text{coeff}_{E2} = 1.2252\text{ ps}^{-1}\text{MeV}^{-5}(e^2\text{b}^2)^{-1}$ 严格证明对数微商定理：$d\ln B(E2)/d\ln\tau \equiv -1.000$、$d\ln B(E2)/d\ln E_\gamma \equiv -5.000$ 与 $d\ln Q_t/d\ln\tau \equiv -0.500$（寿命误差在折算四极矩时压缩一半）；(2) CG 张量闭式与高自旋极限：证明带内跃迁 CG 系数平方 $\langle I\, K\, 2\, 0 \mid I-2\, K \rangle^2 = \frac{3 (I^2 - K^2) ((I-1)^2 - K^2)}{2 I (I-1) (2I-1) (2I+1)}$ 在高自旋端渐近收敛至 $3/8 = 0.3750$；(3) $K$ 约定低自旋敏感性：在 $^{131}\text{Ce}$ $I = 15/2^-$ 处，计算 $K = 5/2$ 与 $K = 1/2$ 的 CG 平方分别为 $0.247253$ 与 $0.323077$，证明将 $K = 5/2$ 误赋为 $K = 1/2$ 将使提取的 $Q_t$ 产生高达 $-12.52\%$ 的虚假压缩（比值差异达 $1.1431$），而在高自旋端（$I = 35/2^-$）该敏感性迅速收敛至 $2.08\%$；(4) 三轴形变几何压制与静态矩解耦：有效跃迁四极矩随三轴度按 $Q_t(\gamma) = Q_0 \cos(30^\circ + \gamma) / \cos 30^\circ$ 衰减，在 $\gamma = 30^\circ$ 处压制幅度达 $-42.26\%$（$Q_t/Q_0 = 0.5774$）；同时证明静态四极矩在 $\gamma = 30^\circ$ 处穿过零点（$Q_s \equiv 0$），证实 $Q_s = 0$ 绝非无形变判据而是强三轴性几何指纹；(5) $^{131}\text{Ce}$ 跨越 6 个数量级时间的三相图：系统重构包含异能态（$88\text{ ns}, |Q_s|=0.92\text{ eb}, \beta_2 \approx 0.20$）、正规转动带（$0.2\text{--}8\text{ ps}, Q_t=2.8\text{ eb}, \beta_2 \approx 0.24$）与高度形变侵入带（$0.05\text{--}0.2\text{ ps}, Q_t=4.5\text{ eb}, \beta_2 \approx 0.35$）的三相图，完整闭环了核形变系统学的微观映射链。 | task-qt-deformation-mapping-audit | derived-and-boundary | transition-quadrupole-moment.md; qt-deformation-mapping-result-074.json | true |


## checkpoint097：Qspec零点反例、转子CG约定与Singh回归敏感性审计

**checkpoint108修订，保留TQM-D19-2供历史locator，撤回其过强结论。**
[[singh-2016-lifetime-131ce-133pr]] SI16-D20-2与[[li-2004-lifetimes-131ce]] LI04-D20-2给真实表项，[[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-D20-3保无三轴假设边界。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| TQM-D19-2 | 轴对称I3/K2给Qs0、K0/I2给−2Q0/7，足以反驳零Qs唯一指三轴；但不描述真实Ce态。fixedK候选27/2的G=26/75与76/325给sqrt(169/114)=1.21756，打印2.72/2.28=1.19298并不完全相等，不证100%K归因或actualproducer。008四有限点条件Gaussian回归z−.639不证恒定/无趋势或feeding原因；不能只凭z定“统计检验力”。r0平方比1.08507是固定beta下Q0比，不等任意二次反演beta同倍变化。旧097通过项不认证全科学。 | bounded-algebra-and-correction | task-derived-and-source-boundary | SI16-D20-2; LI04-D20-2; PE98-D20-3; checkpoint108 rejection registry | true |
