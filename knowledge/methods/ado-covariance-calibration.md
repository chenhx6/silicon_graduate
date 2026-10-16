---
type: method
title: ADO两路校验与共享校准协方差
aliases: [ADO covariance calibration, ADO correlated worksheet, ADO双路线校验]
created: 2026-10-16
updated: 2026-10-16
status: ai-draft
review_status: unreviewed
method_type: gamma-ray-angular-distribution
tags: [ado, covariance, background, detector-efficiency, identifiability]
---

# ADO两路校验与共享校准协方差

## Purpose

本页把[[angular-distribution]]的ADO定义接到一个可复核的相关输入计算单。来源前已冻结本session的primed回忆，再视觉核读[[zheng-2002-ado-coincidence-angular-anisotropy]]全部5页。原始定义来自Z02-1/6（PDF p.2 / printed910，Eq1/3/4/5）；分离响应的迁移限制来自Z02-9（同页Eq2）。本页的计数、效率、角分布系数、校准误差和背景模型全部自设，不是145Tb、193Bi或其它核素的新实验数据。Codex self-audit不等于human review。

## Inputs and Assumptions

需要两角组净计数、匹配能量的target效率比及其数据谱系；求f还需独立本征参考或gate/geometry输入。下文显式列出chosen背景/校准Cov、组内均匀/point/分离响应及可复算数值；不将这些假设视为实际阵列校准。

## 两路f校验与共享校准协方差

待测线为自设`x=760 keV`，门控线为自设`g=420 keV`，不赋真实spin/parity。沿Zheng的方向记

\[
R=\frac{n_S/n_L}{\epsilon_{tS}/\epsilon_{tL}},\qquad
R=r f,\qquad r=\omega_t(\theta_S)/\omega_t(\theta_L).
\]

两角净计数与target效率比只识别R。没有额外输入时，`(r,f)=(1.28342246,.85)、(1.09090909,1)、(.99173554,1.10)`在下述例中给完全相同R；`(r,f)→R`的Jacobian只有rank1。选择其中f=1不会验证修正。可以另给两个不同来源的输入，并分别检验：

1. **gate/geometry路线**：额外给已归一的gate角分布、gate-energy组效率、探测器数；在源文分离近似内算`f_geo`，再用`r_geo=R/f_geo`。
2. **独立本征参考路线**：额外给独立single-γ测得的`r0`，算`f_emp=R/r0`。本例r0是显式自设的独立输入，未由R倒造；若实际参考与待测比共用事件/效率，独立性假设必须撤销并重建Cov。

### 输入合同与数据表

数据身份为`DAY15-20261016-SYNTHETIC-ADO-COV-01`，输入JSON的SHA-256为`e8e31f0691862296b62adffb34e6e5395d22ba6cdc59f629a00c71a89eeadf04`。全部计数单位为histogram entries，效率为无量纲的整组绝对FEP概率，角度输入单位为degree；脚本调用Legendre函数前显式转radian。能量单位keV。每组4台、组内均匀响应；未指定实际方位角，因而不能把本表当完整pair geometry。

| 角组 | 名义极角/degree | 台数 | target组效率 | gate组效率 | 每台target/gate效率 |
| --- | ---: | ---: | ---: | ---: | --- |
| S | 32 | 4 | .044 | .036 | .011 / .009 |
| M | 58 | 4 | .052 | .048 | .013 / .012 |
| L | 90 | 4 | .040 | .032 | .010 / .008 |

`epsilon_tS/epsilon_tL=1.10`，不能再除一次台数。两个gross峰计数为`P_S=8400、P_L=7200`；共用的背景sideband估计为`B=1500`，固定transport系数`k_S=k_L=.8`，所以`n_S=P_S−k_SB=7200、n_L=P_L−k_LB=6000`。本模型选择P_S、P_L、B三个不重叠原始计数为独立Poisson；不是声称所有符合峰天然独立。若B来自与峰重叠的事件、或k由共同拟合得到，须加入额外交叉项。

门控角分布选`W_g=1+.28 P2+.06 P4`，系数Cov的对角为`(.0009,.0004)`、两个非对角元均为`−.00024`。它们是chosen single-γ normalized coefficients，不是核alpha，也不是maximum/reference系数。独立本征参考选`r0=1.12±.024`（标准不确定度）。

五个所用log-efficiency由独立latent变量构造：

\[
\ell_{e,g}=\ell^0_{e,g}+u_0+h_g+z_{e,g},\quad
\sigma(u_0)=.010,\ \sigma(h_g)=.008,
\quad\sigma(z_{t,g})=.006,\ \sigma(z_{g,g})=.012.
\]

u0是两能量和所有组共同的归一mode，h_g是同组在两能量共享的geometry mode，z是能量/组独立残差；central效率是此lognormal模型的median。该chosen PSD模型给出target/gate间非零校准Cov；未从真实calibration得到。

### 几何路线与独立pair核算

定义`b_j=W_g(theta_j) epsilon_gj`、`C=sum_j b_j`，沿Z02-6：

\[
f_{\rm geo}=\frac{C-b_S/N_S}{C-b_L/N_L}=.9690762577.
\]

本例`W_g(S,M,L)=(1.158513508,.957958708,.8825)`，`b=(.0417064863,.0459820180,.02824)`。独立地对12台探测器构造energy-labelled ordered pairs、删除对角self-coincidence，得到同样的f（浮点差小于10⁻¹⁵）。这个核算只验证所声明的均匀、point、分离模型；Z02-9所指出的relative-angle quantum kernel、pair cuts、tracking、pile-up及finite acceptance都没有因此得到验证。

### 背景、校准与完整传播

共用B使两个净峰相关：

\[
\Sigma_n=\begin{pmatrix}P_S+k_S^2 B&k_Sk_LB\\k_Sk_LB&P_L+k_L^2B\end{pmatrix}
=\begin{pmatrix}9360&960\\960&8160\end{pmatrix}.
\]

这是由本例primitive模型推得；只有两个净峰和各自error、没有其背景/event谱系时，不能把960当作实测Cov。对输入向量`v=(nS,nL,ell_tS,ell_tL,ell_gS,ell_gM,ell_gL,A2g,A4g,r0)`和输出`y=(R,f_geo,r_geo,f_emp)`，使用`Sigma_y=J Sigma_v J^T`。计数共享项在`Var(log R)`中为`−2 Cov(nS,nL)/(nS nL)`；不能既假定独立峰，又在事后重复加同一背景误差。

对`a=C−bS/NS、d=C−bL/NL`，几何灵敏度可直接推导：

\[
\frac{\partial\log f}{\partial b_j}
=\frac{1-\delta_{jS}/N_S}{a}-\frac{1-\delta_{jL}/N_L}{d},\qquad
\frac{\partial\log f}{\partial\ell_{gj}}
=b_j\frac{\partial\log f}{\partial b_j}.
\]

对gate的A2/A4再乘`epsilon_gj Pk(cos theta_j)`后求和。`d log R=(dnS/nS−dnL/nL−dell_tS+dell_tL)`，`d log r_geo=d log R−d log f_geo`。共同效率归一u0精确抵消；将相同边际log-efficiency误差全部改为独立，会丢失这个抵消，也会丢失两能量同组h_g所给的cross covariance。

| 输出 | 中央值 | 完整chosen Cov的标准不确定度 | 同边际误差全部独立的反事实 |
| --- | ---: | ---: | ---: |
| R_ADO | 1.090909091 | .025879569 | .030994534 |
| f_geo | .969076258 | .003211837 | .003216838 |
| r_geo=R/f_geo | 1.125720584 | .026479979 | .032201143 |
| f_emp=R/r0 | .974025974 | .031137791 | .034662270 |

两路f虽使用不同的额外输入，仍可经共享校准相关。必须用`Var(f_emp−f_geo)=Var(f_emp)+Var(f_geo)−2Cov(f_emp,f_geo)`；本例`Cov=9.64930975e−6`，差为`.0049497163±.0309932136`。标准化差`.15970`只检查chosen输入的内部闭合，不是实际仪器、分离近似或多极性的实验验证。

200000次独立随机流的MC（seed20261016，零丢弃）按primitive Poisson、Gaussian log-efficiency latent、给定gate系数Cov和独立r0直接生成。四项MC标准差/一阶传播sigma为`1.000158、1.001354、1.000121、1.000279`；MC不证明比值估计无偏，也不提供真实实验CI。解析梯度/central difference最大绝对差`1.93e−10`；所有输入Cov的PSD及共同效率整体乘3.7的不变性已核验。

### 换门与有限几何的失败控制

只把自设gate系数换成`A2=−.30、A4=0`，其余相同，`f_geo`变为`1.016553737`。若独立本征r0=1.12保持不变，预计未再除f的R从`1.085365409`变为`1.138540186`。这些是分离模型内的设计预测；实际换门还可能选择不同feeding/postselection density，不能把观测到差值全部归于self-exclusion。

把gate的single-γ角矩按均匀20°半锥接受作`Pk→Qk Pk`，本例f变为`.970646822`。该控制只平均gate角矩，未指定target W或完整joint kernel，不能称为完整finite-geometry correction。Zheng的point组公式、single-γ效率校准与full gamma-gamma response是三层不同输入。

下一项区分性观测：在同阵列、相同target/gate身份和cuts下保留逐detector-pair净峰与背景、用已知cascade交叉验证，再比较多个已知门经同一joint response修正后的r及其差的Cov。若修正后仍不闭合，应检验pair acceptance、alignment/feeding与门后布居；不能直接改多极性标签。若问题是E/M判别，还需同一跃迁的偏振或独立ICC；本页不产生真实Jpi/δ结论。

## What It Can Establish

在输入身份、数据依赖和分离响应明示的条件下复算R、两路f及其cross covariance，检验共同scale抵消、背景误差和换门设计是否闭合；给出实际分析需要补足的输入合同。

## What It Cannot Establish Alone

自设计数和Cov不能赋真实多极性、Jpi、mixing ratio、核alignment或集体模式；单γ效率/门控marginal不确定full joint response。线性传播及MC内部闭合不能保证真实弱峰/离散spin模型的覆盖，也不能裁决Zheng原Fig1(a)与正文的不一致。

## Sources

- 计算脚本：[day15_ado_covariance_worksheet.py](../../system/scripts/day15_ado_covariance_worksheet.py)。不提供plot参数即可独立复算数值；绘图时可传安装环境的panel-audit模块目录。
- [输入JSON](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/ado-worksheet-input.json)、[完整结果/矩阵](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/ado-covariance-worksheet.json)、[敏感性图](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/ado-covariance-sensitivity.svg)。图为自设L2分析，非来源Fig1/实验复画；本页已保存可复用定义、完整数值输入、推导和边界。
- [[zheng-2002-ado-coincidence-angular-anisotropy]]：Z02-6（Eq4/5及组效率）、Z02-9（Eq2/joint迁移）、Z02-10（Fig1(a)与正文3.2%的图文边界）。原文百分数不作本页uncertainty输入。
- [[angular-distribution-coefficient]]：拟合A、核alpha、maximum/reference和detector attenuation的语义应分开；本例没有推断核布居σ/J。
