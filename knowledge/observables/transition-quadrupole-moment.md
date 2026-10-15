---
type: observable
title: 跃迁四极矩
aliases: [transition quadrupole moment, quadrupole moment, Qt, Q_t, QSD, QND]
created: 2026-07-03
updated: 2026-10-15
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
