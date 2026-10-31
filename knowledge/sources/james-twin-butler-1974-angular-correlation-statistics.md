---
type: source
title: "James, Twin and Butler 1974 - Statistical analysis of gamma-ray angular-correlation experiments"
aliases: [James Twin Butler 1974 angular-correlation statistics]
created: 2026-09-21
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "The statistical analysis of γ-ray angular correlation experiments"
authors: [A. N. James, P. J. Twin, P. A. Butler]
journal: "Nuclear Instruments and Methods"
year: 1974
volume: 115
pages: "105-113"
pii: "0029-554X(74)90433-9"
doi: "10.1016/0029-554X(74)90433-9"
canonical_source: "James, Twin & Butler, Nucl. Instr. Meth. 115, 105-113 (1974)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/DCO/1974_James et al_The statistical analysis of γ-ray angular correlation experiments.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/DCO/1974_James et al_The statistical analysis of γ-ray angular correlation experiments.pdf"
raw_sha256: "c629c42b34570b1a03f450d63feed892f22df864732a47ab02bfa2d9e2a8101a"
nuclei: [generic]
reactions: [generic-alignment-reaction]
experiments: [gamma-angular-correlation]
models: [least-squares, chi-square, alignment-model]
observables: [angular-distribution, mixing-ratio, alignment, confidence-interval]
methods: [statistical-analysis, DCO, angular-correlation]
tags: [angular-correlation, statistics, alignment, mixing-ratio, uncertainty]
---

# Statistical analysis of γ-ray angular-correlation experiments

## Bibliographic Record

- A. N. James, P. J. Twin & P. A. Butler, *Nucl. Instr. Meth.* **115**, 105–113 (1974), PII `0029-554X(74)90433-9`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/DCO/1974_James et al_The statistical analysis of γ-ray angular correlation experiments.pdf`。

## Scope and Reading Depth

- PDF pp.105–113 (9 pages) fully read: uncertain alignment, direct/indirect data, χ²/F tests, design-matrix rank, spin-hypothesis testing, mixing-ratio error estimates, variance components, fitting and alignment prescriptions.
- Not covered: implementation code and later covariance treatments.

## Key Results

- Angular-correlation fits should combine direct intensities/polarization, indirect δ measurements and uncertain alignment-model outputs in one statistical comparison; the alignment estimate is data with its own variance, not a fixed prior (PDF pp.105–108, Secs.2–4).
- `χ²` compatibility uses the number of data terms minus the rank of the design matrix. Correlation alone does not determine rank; the unidentifiable and identifiable examples without alignment data have different ranks and degrees of freedom (PDF pp.106–109, Tables 1–2).
- `arctan δ` is recommended as a fitting coordinate because it is more uniformly spaced in the `(a2,a4)` plane; error estimates should be obtained from confidence intersections, not by reading a symmetric interval on δ (PDF pp.107–111, Sec.7, Fig.5).
- Internal errors from counting statistics and external errors from model/variance mismatch must be distinguished. If residual dispersion is too large, scale parameter errors by the estimated variance rather than claiming a precise δ (PDF pp.107–113, Secs.7.3–7.5).
- The paper warns that near a compensation between alignment and δ, an angular-distribution experiment may be intrinsically unable to separate them; additional γ rays, polarization or independent alignment information are required (PDF pp.107–109, Fig.2).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JT74-1 | Alignment-model uncertainty must enter the same χ²/design-matrix analysis as angular-correlation data. | statistics-result | direct | PDF pp.105–109 | false |
| JT74-2 | The effective degrees of freedom are `n−rank(design matrix)`, not simply the number of angle bins. | statistics-result | direct | PDF pp.106–109, Tables 1–2 | true |
| JT74-3 | `arctan δ` confidence intersections are preferable to symmetric δ error bars under nonlinear angular-response ovals. | uncertainty-method | direct | PDF pp.107–113, Sec.7 | true |
| JT74-4 | Alignment/δ compensation can make a single angular distribution non-identifying. | limitation | direct | PDF pp.107–109, Fig.2 | false |

## Summary

James, Twin and Butler provide the statistical discipline needed for angular-correlation and DCO mixing-ratio claims. Their practical message is that alignment, δ, calibration and model error belong in one covariance-aware fit; a small formal χ² or a symmetric δ interval is not evidence of unique identification by itself.

## Competing Interpretations and Limitations

- The recommended Gaussian/least-squares approximations rely on adequate counts and a locally quadratic statistic; nonlinear or bounded δ branches require confidence contours.
- Model alignment errors can dominate counting statistics; treating `σ/J` as exact understates uncertainty and overstates spin/multipole discrimination.
- Degrees-of-freedom and variance scaling are experiment-specific; do not transplant the paper's numerical thresholds without the design matrix.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| JT74-AR-1 | Data chain | Counts/polarization/δ/alignment estimate → design matrix → χ²/F test → spin-hypothesis confidence. | PDF Secs.2–6 | self-checking |
| JT74-AR-2 | Error chain | Internal counting variance + external alignment/model variance → covariance/design rank → confidence contour in `arctan δ`. | PDF Sec.7 | self-checking |
| JT74-AR-3 | Failure condition | Alignment/δ compensation or underestimated systematic error leaves the fit non-identifying. | PDF Fig.2, Secs.7–8 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-correlation]], [[angular-distribution]], [[multipole-mixing-ratio]], [[dco-ratio]] and self-audit of DCO/ADO fits.
- New reusable rule: every future δ or spin assignment should record alignment-model variance, design-matrix rank, confidence topology and independent-discriminator status.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `JT74-P0-1`: Do not report δ errors or spin confidence without including alignment/model covariance and correct effective degrees of freedom.

## Extracted Pages

- Methods/observables: [[angular-correlation]], [[angular-distribution]], [[multipole-mixing-ratio]], [[dco-ratio]]。


## DAY16原文重核：profile阈值、F表与相关性的语境

本session对9页（printed105–113=PDF1–9）完整主线重读，视觉核全部Tables1–3及Figs.1–6，包含反应alignment估计、design matrix、spin tests、internal/external error、cautious recipe与实际拟合/布居处方。Crossref另核DOI[10.1016/0029-554X(74)90433-9](https://doi.org/10.1016/0029-554X(74)90433-9)，作者/115/105–113/1974相符；收到稿日期1973-08-20不替代出版年。旧claim及review flags未动；只纠正旧摘要把correlation笼统等同rank变化的措辞。

### 新增证据与原表的条件复算

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| JT74-5 | 对θ=arctanδ，S_h是在固定θ时仍重新最小化其它参数的profile，R是全局minimum。已知输入方差取增量E32=1；由dispersion估方差取E32=(R/ν)F32(1,ν)；作者建议较大者。绝对S阈值是R+E32，不能把它称δ标准差或只在固定nuisance切片取交点。 | statistics-method | direct | printed110，Sec.7.2/Fig.5；111，Secs.7.3–7.5/Eq.(3)/Fig.6 | true |
| JT74-6 | ν=n−rank(A)中的n包含进入S的alignment数据项。原Table1 n=d+p、rank=p+2给d−2；Table2加alignment项n=d+1、rank3也给d−2；不加该约束时原文在compensation附近称rank2/d−2、离开时rank3/d−3。参数相关本身不等于精确秩亏。 | design-rank-and-identifiability | direct-and-clarification | printed108–109，Sec.6/Tables1–2；Fig.2 | true |
| JT74-7 | Sec.7.1所谓相关通常可忽略，是Fig.4中只把一个θ与不依赖nuisance的核结构理论比较时使用其marginal variance；紧接着δ1=Cδ2的joint假设明确要用covariances。不能据该短句删去数据Cov、联合δ的Cov或在profile时固定nuisance。 | covariance-context | direct-and-Codex-interpretation | printed110，Sec.7.1/Fig.4及随后cascade例 | true |
| JT74-8 | Table3明印32%上尾临界值，但十二项逐值按标准F(1,ν)核得上尾约.30405–.30807；各最后位±.005仍不覆盖.32。原表与其标签的精确概率对应未重现；表值、标签及现代计算各保留，不据此重估任一原实验CI。 | printed-table-probability-audit | conditional-calculation | printed111，Table3 caption/全部12行；Eq.(3) | true |
| JT74-9 | JT74的max增量结构与公开DELTA的SIGMA结构代数相同，但两者F表不同：DELTA程序unit19引Gill1975、标CDF .683，ν1用3.38而JT74用3.69；ν>16该代码返回1。实际编译未改F unit验证此行为，不能称重放同一F表或认证EL18实际producer。 | cross-source-and-code-audit | direct-code-and-calculation | printed111，Eq.(3)/Table3；DELTA unit19及DIPS，见D101-9 | true |
| JT74-10 | 原Sec.8把低于.02的布居在当时a2/a4精度约.01条件下裁零；针对2s/1d的(α,n)/(α,p)反应，给小布居σ=.1、中等布居σ=.5e(ω)、大于.5者自由等处方。它是特定反应/精度的alignment模型做法，不是所有高统计DCO的Gaussian σ/J校准。 | alignment-model-scope | direct | printed112–113，Secs.8.2–8.3 | true |

### 单个δ误差的profile与适用条件

令θ=arctanδ、ν=n−c>0，原式的变量关系为

\[
R=\min_{\theta,\eta}S(\theta,\eta),\quad
S_h(\theta)=\min_\eta S(\theta,\eta),\quad
E=S_h-R,
\]
\[
E_{\rm crit}=\max\!\left(1,\frac{R}{\nu}F_{32\%}(1,\nu)\right),\qquad
S_{\rm crit}=R+E_{\rm crit}.
\]

η表示其它待拟合参数，不是把η固定在全局best。作者的χ²/F分布论以Gaussian及局部quadratic/linear-regression近似为基础，p.108明确说选θ是为了更接近二次行为，不是证明所有angular likelihood都线性。Sec.3还指出theory若为假，S的分布不能由上述理论保证；放大误差或cautious max不自动修复错误spin、response或模型。

Sec.7.5的较大者是在已知方差与由残差估方差之间采取保守处方，**不等于事先校准过的通用68%覆盖保证**。单个θ的阈值不同于对多个参数协调值的joint confidence region；作者明确把Cline–Lesser的multiple-hypothesis程序与此区分。这里不把RZ17的P(δ)分位区间、EL18印刷rectangle与这种profile set混成同一概率对象。

### Table3逐值核验及真实程序函数

| ν | JT74印刷F | 标准F的上尾概率 | 精确32%上尾F | DELTA实际F |
| --- | --- | --- | --- | --- |
| 1 | 3.69 | .30556164 | 3.30873643 | 3.38000011 |
| 2 | 1.84 | .30778134 | 1.72023810 | 1.75 |
| 4 | 1.38 | .30525970 | 1.28685573 | 1.29999995 |
| 10 | 1.17 | .30479507 | 1.09500028 | 1.11000001 |
| 14 | 1.13 | .30576827 | 1.06307059 | 1.08000004 |
| 20 | 1.11 | .30464464 | 1.03999929 | 1.0（>16默认） |

全部12行的原表数字在输入冻结后计算。除了SciPy F survival/inverse，另由Student-t密度直接积分复核上尾（最大绝对差1.45×10^-15），ν1/2还用闭式CDF；因此这里是数学映射不闭合，未将原因猜作OCR、作者计算/排版或后期勘误，也未改原表。DELTA FF的source hash与本页关联的D101内容对象一致，抽出**未改字节的F program unit**实际编译/运行，非仅从注释想象行为。

DELTA ν17/20/30取F=1时，标准上尾分别.331333/.329257/.325309；这是该实现的finite-ν近似，不能从注释.683推定所有ν都精确同coverage。ν≤0时孤立F unit也默认1，不使无有效自由度的统计分析变得有意义；完整DELTA另有warning。这里没有新experimentalδ或误差更正。

### 秩与相关：原Fig.2的判读边界

原Fig.2的J=3→2 M1/E2 oval展示δ与alignment变化在A附近近乎互相补偿，B附近则可分；Table1/2把额外alignment信息当有误差的data加入S，而非先固定一个“正确σ/J”。精确列依赖使rank改变；强相关但非零小奇异值是弱识别，不能仅因相关系数接近1就随意少算一个参数。没有实际design/Σ，不为EL18或W178替选ν。

Sec.7.1/Fig.4使用一个参数的marginal variance，等价于保留拟合联合不确定度后取该对角元素；不是条件在已知η下的更窄variance。若检验δ1=Cδ2，原文明确使用Cov可更有判别力。本run据此`revises`旧摘要含糊的“correlation reduces degrees of freedom”，`supports`profile/nuisance处理，`limits`无输入地借historic表或max处方认证某个实验CI。

复算：[原12行与rank输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-statistics-input.json)、[固定代码F表输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-delta-input.json)、[程序](../../system/scripts/day16_jt74_statistics_audit.py)、[CDF/quad/actual Fortran结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-statistics-audit.json)。原raw hash未变；新claims均needs_review，未把self-audit当human review。


### Fig.2动机下的非regular控制：不是所有profile都二次

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| JT74-11 | 本任务由原Fig.2的3→2 M1/E2路径构造正density族p0=1−u、p±1=u/2（0<u<1）。在明确D96振幅约定下，纯M1点的(a2,a4)对(δ,u)Jacobian秩1、profile距离首项δ^4；已知非零Q的matched P90使局部秩2，Q自由则三参数仅秩2。声明known正定Σ及高统计/interior u条件时，δ0=0的LR极限为半质量0加半χ1²，ΔS=1的覆盖约.841345。它是任务条件推导，不是作者原结论或实际DCO误差重估。 | Codex-theory-and-failure-control | conditional-model-calculation | 原printed107 Fig.2的spin path；108–110的rank/profile假设；本任务冻结positive-density推导 | true |

本run没有构造实验counts或新测量。沿用原Fig.2的spin path，**另外声明**轴对称positive density族；caption中“equal m0 and m1”未明确单substate或±group口径，本任务检查u=.5与2/3两种interior解释，均不称原图精确曲线重放。JT74的δ operator相位未从此文认证；计算采用已明确的D96 native M1=1/E2=δ，(−1)^L映射到Jones probe。δ坐标换号会换interference斜率，下面rank、阶数与局部边界结论保持。

SymPy独立CG/Wigner-d与既有显式photon trace给同一normalized coefficients（最大差1.78×10^-15）：

\[
a_2=\frac{(4-u)\,[5\delta^2+14\sqrt{30}\delta-14]}
{140(1+\delta^2)},\qquad
 a_4=\frac{(6-5u)\delta^2}{7(1+\delta^2)}.
\]

纯M1处

\[
\frac{\partial(a_2,a_4)}{\partial(\delta,u)}\bigg|_{0}
=\begin{pmatrix}(4-u)\sqrt{30}/10&1/10\\0&0\end{pmatrix}
\]

只有rank1。对具有已知正定Σ的Gaussian (a2,a4)估计，固定δ时均值对u恰为affine，故可解析profile；以true mean作中心的profile距离满足

\[
S_h(\delta)-R=
\frac{(6-5u_0)^2}{49\Sigma_{44}}\delta^4+O(\delta^5),
\qquad 0<u_0<1.
\]

Σ44表示a4的marginal variance；这个式子保留一般Σ24，没有把Cov置零。它说明此条件族在纯M1点不是对δ的regular二次profile。若harmonic误差按N^-1/2下降，此未校alignment的局部δ尺度可为N^-1/4，而非通常的N^-1/2；没有把N指定为任何原实验counts。

在声明的高统计局部模型中，去掉a2的自由mean后，rank4方向的λ=δ²≥0，LR在true λ0=0时等于[max(Z,0)]²、Z为标准normal。因此在该点以ΔS=1检验的覆盖为Φ(1)=.84134475；该模型68%局部临界增量约.218742。**这是一项regularity失败控制，不能把.218742移植为其它δ、实际RDCO、未知Σ或有active population边界时的阈值。** JT74已要求局部quadratic，本计算限制它的外推，没有说原作者给出了上述混合分布。

### 伴随偏振何时增加信息

在同一单γ、density/选择/方向定义下，令H90为4π(I_parallel−I_perpendicular)、W90=1−a2/2+3a4/8，P90=H90/W90。计算给

\[
H_{90}=\frac{-3(4-u)-\sqrt{30}(4-u)\delta+(15-10u)\delta^2}
{20(1+\delta^2)},\quad
\det\frac{\partial(a_2,P_{90})}{\partial(\delta,u)}\bigg|_0
=\frac{2\sqrt{30}(4-u)}{5(24-u)}\ne0.
\]

所以在这套条件模型下，已知非零Q的matched A=QP幅度可以补齐局部rank；Q=0则不行。把Q也当自由参数时，(a2,a4,A)对(δ,u,Q)只rank2；再加入一项**真正独立且匹配response的Q校准**才达到三参数rank3。源校准Q若本来来自同一transition的A/P回代，不能假当这个额外独立row（对照Z13-11）。局部满秩不保证全局唯一branch或自动给出actual covariance/coverage。

另用完整isotropic density作失败控制，W=1、P=0且对δ无single-photon信息，误差<2×10^-12；它不属于上述受限family，说明布居/response条件不能丢。pure-E2的P90另通过源式(12a2+5a4)/(8−4a2+3a4)检查。所有密度非负、trace1、有限角intensity非负与mixed/pure controls均通过；无raw/旧helper修改。

复算[冻结理论问题](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-nonregular-before-analysis.md)、[输入/hash](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-nonregular-input.json)、[SymPy独立推导/trace程序](../../system/scripts/day16_jt74_nonregular_profile.py)、[exact式/rank/quad/幂次结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-nonregular-profile.json)。初次因环境缺SymPy退出1；官方PyPI的SymPy1.14.0及依赖只装repo tmp，原helpers hash不变，随后actual analysis exit0。重放须令PYTHONPATH指向本run的tmp/day16-jt74/python-deps，第三方包不stage，不改全局环境。
