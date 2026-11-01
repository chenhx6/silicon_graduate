---
type: concept
title: "低计数 gamma 峰拟合：Poisson 似然、有限样本偏差与边界推断"
aliases: [Poisson peak fitting, Baker-Cousins deviance, 低计数峰面积推断]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [counting-statistics, poisson-likelihood, peak-fitting, finite-sample, boundary]
---

# 低计数 gamma 峰拟合：Poisson 似然、有限样本偏差与边界推断

## Definition

Poisson 最大似然估计（maximum likelihood estimation, MLE）正确保留原始计数的生成模型，但不保证有限样本无偏，也不自动保证区间覆盖率。单次拟合误差不能称作方法的系统偏差。这里的计算器仅拟合非负峰面积，固定峰位、宽度和已知本底；它是可核查的统计练习，不是完整实验谱学发现流程。

## Supporting Evidence

下列 locator 均回读本地 PDF，页码采用「印刷页 / PDF 文件页」。已有书籍来源页的泛化总结不能替代这些具体段落。

| 来源入口 | 本轮回读位置 | 可以支持的内容 |
| --- | --- | --- |
| [[book-behnke-data-analysis-hep]] | Behnke 与 Moneta，Ch.2，§2.3.2，p.31 / PDF p.49 | MLE 的有限样本偏差与渐近性质须区分；不能宣称一般严格无偏。 |
| 同上 | §2.3.4.1–2，p.37 / PDF p.55，Eqs.(2.33–2.36) | 似然比区间的渐近校准及 nuisance profiling 定义。 |
| 同上 | §§2.5.3–2.5.4，pp.59–61 / PDF pp.77–79，Eqs.(2.86),(2.88–2.93) | bin 积分、Poisson 联合似然、Pearson/Neyman 定义及特定自由归一化模型下的偏差。 |
| 同上 | Schott，§3.5.4，p.88 / PDF p.105 | 固定峰位 local significance 与扫描峰位 global significance 不同。 |
| [[book-bonamente-statistics-scientific-data]] | Ch.15，pp.277–279 / PDF pp.289–291，尤其 Eq.(15.3) | 原始整数计数与 Cash/Poisson deviance。 |
| 同上 | §§16.3.1–16.3.3，pp.302–304 / PDF pp.313–315；§16.4，pp.307–309 / PDF pp.318–320，Fig.16.4 | 最小 deviance 的拟合优度分布与参数似然比的分布不同；低计数下不能仅因 bin 多就采用标准卡方。 |
| 同上 | §17.3，p.319 / PDF p.329，Eq.(17.6) | 本底扣除需要传播总计数和本底观测的不确定度。 |
| [[cowan2011-asymptotic-likelihood-tests]] | **arXiv v3 PDF** p.4 Eqs.(2–7)，p.7 Eq.(12)，pp.14–15 Eqs.(49–53)，pp.26–27 §5.2 | 联合似然、单侧非负信号检验、边界混合分布、local/global 区分。 |

书籍身份以所读原件为准：Behnke 等是 **2013 年编者**，Ch.2 作者为 Behnke 与 Moneta；Bonamente 原件版权页为 **2022 年第三版**，eBook DOI `10.1007/978-981-19-0365-6`。本页不沿用未经原件支撑的朱永生章节归因，也不把已有 source 页误写的书章/ISBN 当作证据。教材彼此可以提供独立方法讲解，不能由重复引用制造独立实验验证。

## Necessary Assumptions

对互不重叠、独立原始计数道，设

$$
n_i\sim\operatorname{Pois}(\mu_i),\qquad
\mu_i=A p_i+b_i,\qquad A\geq0,
$$

$$
p_i=\int_{e_i}^{e_{i+1}}
\frac{\exp[-(x-c)^2/(2\sigma^2)]}{\sqrt{2\pi}\sigma}\,dx
=\Phi\!\left(\frac{e_{i+1}-c}{\sigma}\right)
-\Phi\!\left(\frac{e_i-c}{\sigma}\right).
$$

$A$ 是整个高斯峰的期望面积，拟合窗口内信号期望为 $A\sum_i p_i$。窗口截断后不自动归一化模板；否则参数含义会改成窗口内面积。当前函数以等间隔道中心推断边界，单道宽度默认为 1，`bg` 为已知每 bin 本底期望；非等距输入须使用另建的显式边界模型，当前实现拒绝它。窄峰也必须积分，不能把峰心密度直接作为道计数。上述模型来自 Behnke–Moneta Eq.(2.86) 与 Cowan PDF Eqs.(2–4)；固定本底及全峰面积定义是本练习的实现选择。

独立性来自采集模型，不能只由非负整数外观判定。固定总事件数的归一化直方图是 multinomial 问题；加权、重复投影、共享事件或重用侧带也可能产生相关性。若 $T_i$ 与 $B_i$ 独立，$D_i=T_i-\alpha B_i$ 一般不是 Poisson，且

$$
\operatorname{Var}(D_i)=\operatorname{Var}(T_i)+\alpha^2\operatorname{Var}(B_i).
$$

整数扣谱也不例外。可从原始 on/off 观测建立

$$
\mathcal L(A,\boldsymbol b)=
\prod_i\operatorname{Pois}(T_i\mid A p_i+b_i)
\operatorname{Pois}(B_i\mid \tau_i b_i),
$$

并在每个 $A$ 重新拟合 $b_i$ 或共享本底参数；相关控制样本则不能直接相乘。Cowan PDF p.23 Eq.(90) 是单 bin 的明确例子；此处多 bin 写法是相同独立性条件下的推广。当前计算器**未实现 on/off 拟合**，`data_kind` 非 `raw-counts` 时拒绝推断。

## Poisson deviance、零道与非负 MLE

由饱和模型相对于指定均值的似然比得到

$$
C(A)=2\sum_i\left[\mu_i-n_i+n_i\ln(n_i/\mu_i)\right].
$$

这是统计量 deviance，中文不宜与估计量 bias 混称「偏差」。Bonamente Eq.(15.3) 给出这一形式；[[baker-cousins-1984-histogram-fits]] 是历史方法入口，本页不借其待审内容引入额外定量结论。

每个 bin 的数学边界为：$n_i=0$ 时贡献 $2\mu_i$，包括 $(0,0)$ 贡献零；$n_i>0,\mu_i=0$ 时似然为零、deviance 为无穷大。不能删除零道、伪造正计数或用任意小常数替换不可能的均值。负均值、负/非整数观测、NaN、无穷输入及长度不一致均拒绝。

对本练习的固定 $p_i,b$，内部解满足 score 方程

$$
\frac{d\ln\mathcal L}{dA}
=\sum_i p_i\left(\frac{n_i}{A p_i+b}-1\right)=0.
$$

其导数为 $-\sum_i n_i p_i^2/(A p_i+b)^2\leq0$；若 $A=0$ 的 score 已非正，约束 MLE 为零，否则求唯一内部根。对正本底可用 $A_{\rm upper}=\sum_i n_i/\sum_i p_i$ 括住根，无固定面积扫描上限。若 $b=0$ 且数据有模型支撑，$\hat A=\sum_i n_i/\sum_i p_i$。这些是本任务对固定模板模型的解析推导，不是教材报告的实验结果。

## Counter-evidence and Competing Interpretations

比较目标采用显式约定

$$
Q_N(A)=\sum_i\frac{(n_i-Ap_i-b)^2}{\max(1,n_i)}.
$$

这是对零道作修改的 Neyman 型损失，并非标准 $1/n_i$ 在零道处的定义。它对向下涨落给出较大数据权重，会使许多模型的归一化估计偏低；偏差大小和符号仍取决于本底、信号形状、约束与零道处理。Behnke–Moneta Eqs.(2.92–2.93) 的自由总归一化结论不能原样移植到有固定非零本底的净峰面积上。没有通用的固定百分比范围，也不能断言任意低计数拟合都会下偏。

对一次生成的数据，$\hat A-A_{\rm true}$ 是 **single-realization estimation error**。方法偏差是重复实验的

$$
\operatorname{Bias}(\hat A)=E[\hat A]-A_{\rm true}.
$$

若另做 $R$ 次模拟，应报告 ensemble 的 $\overline{\hat A}-A_{\rm true}$、Monte Carlo 标准误 $s_{\hat A}/\sqrt R$、RMS error、边界命中率及区间覆盖率，并说明 $R$、生成模型、种子和拟合失败处理；$A_{\rm true}=0$ 时百分比偏差无定义。当前 API 只生成一个 realization，不输出 ensemble bias。

MLE 本身也可有边界偏差：单 bin、已知 $b>0$ 时，$\hat A=\max(0,n-b)/p$；在 $A_{\rm true}=0$，$n\sim\operatorname{Pois}(b)$，这个非负估计量以正概率取正值，因此 $E[\hat A]>0$。这是本任务的精确反例，足以否定「正确 Poisson 似然保证所有小样本估计严格无偏」，与 Behnke–Moneta §2.3.2 相容。

## Discriminating Observables

一般有 nuisance 参数 $\eta$ 时，

$$
\lambda(A)=\frac{\mathcal L(A,\hat{\hat\eta}(A))}
{\mathcal L(\hat A,\hat\eta)},\qquad
-2\ln\lambda(A)=C_{\rm prof}(A)-C_{\min}.
$$

当前模型没有自由 nuisance，所以返回的是固定形状、本底条件下的一维 likelihood-ratio interval，也是无 nuisance 的 profile 特例。上下端点分别解 $\Delta C=1$，若下端点越过物理边界则保留零；不以对称 `+/-` 取代。$\Delta C=1$ 与约 $3.84$ 分别对应**正则大样本单参数**约 68% 与 95% 双侧区间，有限计数或边界处不能直接声明这些覆盖率。给定阈值的似然等高区间也不是自动得到的 Feldman–Cousins 置信带或 95% 单侧上限；后者必须明确统计量、ordering 与覆盖率校准。

同样，$C_{\min}$ 的稀疏数据拟合优度不自动服从 $\chi^2_{N-k}$；增加大量几乎没有信息的空道不等于达到正则渐近极限。Bonamente §§16.3.2–16.3.3 明确区分 $\Delta C$ 和 $C_{\min}$。本程序不输出未经校准的拟合优度 $p$ 值。

检验 $A=0$ 相对于 $A>0$，固定且预先指定的峰形给出

$$
q_0=C(0)-C(\hat A)\geq0,\qquad
q_0=0\ \text{if }\hat A=0.
$$

在 nuisance 正则、可识别、信息充分且零假说本底为正等条件下，边界检验的渐近分布为

$$
q_0\ \overset{H_0}{\sim}\ \tfrac12\delta_0+\tfrac12\chi^2_1,\qquad
p_{0,\rm local}\simeq1-\Phi(\sqrt{q_0}),\quad
Z_{\rm local,asym}\simeq\sqrt{q_0}\quad(q_0>0).
$$

这不是把边界当作正则内部点套用 Wilks 的完整 $\chi^2_1$ 分布。Cowan **v3 PDF** p.14 Eq.(49)、p.15 Eqs.(51–53) 是所用原式。$q_0=0$ 有概率原子，本实现明示采用包含等号的尾概率 $p=1$ 与「无正向超额」$Z=0$ 约定；此点的 $Z$ 不再按 $\Phi^{-1}(1-p)$ 换算。若沿用 Cowan Eq.(52) 的 $1-F(0)$ 约定会得到 $p=0.5$，两者均不得被误写为正向证据。

若已知本底严格为零，零假说只能生成全零数据；正计数导致零假说似然为零，不能报普通高斯「无穷 sigma」。程序保留 `null_has_zero_likelihood`，把无限 deviance / $q_0$ 的 JSON 表示设为 `null`，并以 `unavailable-zero-background-null` 标记不提供渐近 $p,Z$；即使观测也全零，仍不使用该渐近校准。

扫描未知峰位或宽度会引入 trial / look-elsewhere 问题，峰形参数在 $A=0$ 时还可能不可识别；不能机械套单参数混合律。低计数的离散尾概率、系统误差及窗口选择需用完整观测模型进行检验反演或专门的模拟校准，少量 toys 不能验证极端尾部。$5\sigma$ 也只是统计约定；Cowan PDF p.3 直接说明统计拒绝仅是发现的一部分。本任务进一步要求核谱学检验峰来源、响应/本底伪峰、符合关系与能量闭合，才讨论新跃迁及能级归属；这些是应用判断，不是 Cowan 报告的新核结构事实。

## Our Current Position

```bash
python3 system/scripts/analysis/poisson_likelihood_peak_fitting_bias_calculator.py --area 60 --bg 2 --seed 42
python3 system/scripts/analysis/poisson_likelihood_peak_fitting_bias_calculator.py --area 0 --bg 0 --json
python3 -m unittest discover -s system/tests -p test_poisson_peak_inference.py
```

`evaluate_peak_fitting_methods(true_area, centroid, sigma, bg_counts, seed)` 的五参数调用和两个主要结果 section 保留。模拟新增 NumPy 依赖并采用局部 `default_rng(seed).poisson`，不会重置 Python/NumPy 全局 RNG；新旧相同 seed 的 realization **不相同**，不能继续比较旧版示例数字。`infer_peak_area(...)` 是直接对原计数推断的新入口；`fit_peak_area_1d` 保留 `(area, loss, upper_delta_loss_1_distance)` 三元组，第三项不保证是对称标准误，Neyman 情况仅为损失等高距离。

| 字段 | 当前含义 / 集成处理 |
| --- | --- |
| `fitted_area_counts`、`min_deviance_chi_lambda2`、`min_neyman_chisq` | 保留；高斯改用 bin 积分，数值随之改变。 |
| `estimation_error_counts`、`relative_error_percentage` | 单次模拟误差；零真面积的百分比为 `null`。 |
| 旧 `bias_percentage` | 暂留 deprecated alias，数值等于单次 `relative_error_percentage`；不可据它判无偏。 |
| `profile_likelihood_interval`、`area_error_lower_counts`、`area_error_upper_counts` | 非对称 LR 端点与距离，并附固定 nuisance 和未校准 coverage 状态。 |
| 旧 Poisson `area_uncertainty_1sigma` | 暂留 deprecated alias，仅等于上侧 $\Delta C=1$ 距离。 |
| `local_test.q0`、`z_asymptotic_local`、`p_asymptotic_local` | 固定峰位/宽度、本底条件下的渐近 local 数量，含边界/奇异状态。 |
| 旧 `delta_chi2`、`statistical_significance_Z_sigma` | 分别 alias 为上述 $q_0,Z$；奇异零本底时可能 `null`。 |
| `is_unbiased`、`systematic_underestimation`、Neyman `area_uncertainty_1sigma` | 删除，避免由一次 realization 作科学认证。 |
| `simulation`、`api_notes` | 记录生成均值、原始计数、种子、sampler 与弃用语义。 |

共享 `nuclear_analyzer.py` 的五参数 wrapper 仍可调用；旧 `test_analysis_suite.py` 用单个 seed 的所谓 `bias_percentage < 15%` 认证无偏，父任务应改成解析/边界/统计契约检验，不能挑选有利 seed 维持该断言。本子任务不改 wrapper、共享测试、索引或交接。

## Claim self-audit

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
| --- | --- | --- | --- | --- | --- | --- |
| PP-1 | Poisson MLE 不保证一般有限样本无偏。 | synthesis | direct | single | Behnke–Moneta §2.3.2，p.31 / PDF p.49 | false |
| PP-2 | bin 积分和计数采集假设决定模型；减本底不等于独立 Poisson 原计数。 | synthesis | direct | multiple-independent | Behnke–Moneta Eqs.(2.86),(2.88)；Bonamente §17.3 Eq.(17.6)；Cowan PDF Eq.(90) | false |
| PP-3 | 非负信号边界的常用大样本 local excess 校准为半卡方混合律。 | model-result | direct | single | Cowan v3 PDF pp.14–15 Eqs.(49–53)；条件见本页 | false |
| PP-4 | 当前 score 求解、精确单 bin 反例与零本底处理适用于固定模板模型。 | our-inference | direct | single | 本页推导；`test_poisson_peak_inference.py` 的解析回归 | false |
| PP-5 | 稀疏数据 $C_{\min}$ 不由 bin 数多自动取得标准卡方拟合优度校准。 | synthesis | direct | single | Bonamente §16.3.3 pp.303–304 / PDF pp.314–315 | false |
| PP-6 | 真实弱 gamma 跃迁的有限样本覆盖率、全局显著性和新能级归属尚需具体数据与 nuisance 模型。 | our-inference | contextual | multiple-dependent | Cowan PDF p.3、§5.2；本练习未输入真实实验数据 | true |

本次为 Codex 定向 self-audit，不标 `human-reviewed`。仍待具体实验解决的边界是本底约束、响应模型、窗口/试验选择、覆盖率与符合证据，不是要求用户替本任务作一般方法审核。外部 Cowan 原件、快照及 SHA-256 清单见来源页；已存在的教材沿用本地原路径和登记哈希，本轮未复制或改写。

## Sources

- [[book-behnke-data-analysis-hep]]：原件支持 MLE 偏差、bin 积分和 nuisance profiling 的条件。
- [[book-bonamente-statistics-scientific-data]]：原件支持 Cash 统计量及稀疏数据的校准边界。
- [[cowan2011-asymptotic-likelihood-tests]]：本轮留档的作者 PDF，支持非负信号检验及渐近 local significance。
- [[baker-cousins-1984-histogram-fits]]：历史方法入口，其待审定量练习未作为本页结论依据。
