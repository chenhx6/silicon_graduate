---
type: research-note
title: "A130写作核查：辐射强度、混合比多解与缓发中子级联的前向一致性"
aliases: [A130 forward observables and cascade consistency]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "A130正文3.8、4.5、4.7与5.6至5.10逐式核查"
promotion_target: ""
tags: [doctoral-thesis, electromagnetic-transitions, beta-decay, coincidence, covariance, forward-model]
evidence_sources: [book-suhonen-from-nucleons-to-nucleus, book-hamilton-electromagnetic-interaction, doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives, dimitriou-2021-beta-delayed-neutron-reference-database, xiao-xiao-2019-high-spin-74as-thesis, xiao-2022-chirality-octupole-correlations-74as, guo-2022-mo93m-isomer-beam-depletion-limit, dewald-2012-ddcm-recoil-distance, frauendorf-2014-transverse-wobbling, duguet-2015-non-observable-nuclear-shell-structure]
---

# 辐射强度、反演分支与级联概率不能各用一套定义

## Research Trigger

本页保存A130正文复核产生的可复用物理与统计关系。原文报告、模型计算与本任务推导分别标明；不是对尚未验收章节的接受记录。共同接口见
[[doctoral-thesis-notation-and-evidence-style-20261108]]、
[[a130-rewrite-magnetic-unit-and-numerical-normalization-20261113]]及
[[a130-rewrite-cross-region-comparison-and-e0-constraints-20261113]]。

## Grounded Evidence

Suhonen印刷p.119 Eq.(6.7)提供辐射率起点，Hamilton专著提供取向与
方向关联框架；本页的二次分母和误差传播是对这些定义的本任务推导。
Zhi原PDF pp.5、7、10–12的定量范围及肖骁两个版本的带号证据
另列在下文第4、5项，避免将推导当成实测。

## Provisional Reasoning

### 1. 光子分支比与总退激分支比

对同一母态，设平均寿命为 $\tau$，某分支光子发射率为
$\lambda_{\gamma,k}$，内转换系数为 $\alpha_k$。在只有这些电磁通道、
不遗漏E0等其它退激过程的指定模型中，

$$
\tau^{-1}=\sum_k(1+\alpha_k)\lambda_{\gamma,k}.
$$

若 $b_k^{\rm tot}$ 表示相对于全部母态衰变的总转换加光子分支，
则 $\lambda_{\gamma,k}=b_k^{\rm tot}/[\tau(1+\alpha_k)]$。
若 $b_k^\gamma$ 已定义为相对于全部母态衰变的光子发射概率，则
$\lambda_{\gamma,k}=b_k^\gamma/\tau$，不再加一次ICC因子。
若实验表只给相对光子强度 $a_k$，则仍需母态所有出口的归一化。
这里的 $B(\sigma\lambda)\propto\lambda_\gamma$，因此在其它输入固定时
$B\propto\tau^{-1}$，不是 $B\propto\tau$。

在同一电多极算符与单位体系下，写
$\lambda_\gamma(E\lambda)=C_\lambda E_\gamma^{2\lambda+1}B(E\lambda)$。
依 [[book-suhonen-from-nucleons-to-nucleus]] 印刷p.119的Eq.(6.7)，
本任务对E1/E2的共同常数复算给出

$$
\frac{I_\gamma(E1)}{I_\gamma(E2)}
=\frac{100}{3}(\hbar c)^2
 \frac{E_{\gamma,E1}^{3}}{E_{\gamma,E2}^{5}}
 \frac{B(E1)}{B(E2)}.
$$

条件是两条线来自同一母态，$I_\gamma$ 已经相应的效率、门选和
角响应修正，且讨论纯E1与纯E2光子分量。上式没有额外ICC比：
ICC作用已在总分支与光子分支的转换中说明。
$B(E1)/B(E2)$ 的量纲是长度的负二次方；省掉
$C_1/C_2=(100/3)(\hbar c)^2$ 会造成量纲和数值同时错误。
常数比是本任务对标准辐射率公式的代数推导，不是新实验结果。

强耦合单K映射给出的
$|D_0|=|Q_0|\sqrt{(5/12)[B(E1)/B(E2)]\,G_2/G_1}$
还依赖轴对称、相应Clebsch–Gordan因子 $G_1,G_2$ 及非零分母。
$Q_0$ 可以来自独立的同核电四极资料或指定模型，并非必须借用邻核。
脱离单K极限时应回到实际波函数与跃迁算符计算。
测到绝对 $B(E1)$ 有助于约束解释，但不单独确证静态八极形变。

### 2. 二次有理响应与DCO的一般分母

[[book-hamilton-electromagnetic-interaction]] 的取向、辐射及方向关联框架
允许将固定自旋序列、门跃迁、相位和几何条件下的M1/E2强度写成
$N(\delta)/(1+\delta^2)$。$\delta$ 必须是无量纲辐射振幅比，
保留能量、长度、磁单位与相位约定；不能换成裸E2/M1约化矩阵元之比。

本任务推导：若两个角组的条件符合强度分别含二次式 $N,D$，
取比以后共同的 $1+\delta^2$ 消去，留下

$$
R(\delta)=
\frac{n_0+n_1\delta+n_2\delta^2}
     {d_0+d_1\delta+d_2\delta^2}.
$$

所以一般DCO比的分母不是 $1+\delta^2$。对某实测中心比值 $r$，
在分母非零处反解为

$$
(n_2-rd_2)\delta^2+(n_1-rd_1)\delta+(n_0-rd_0)=0.
$$

可有零、一、两个有限实根，以及退化情形；还应检查纯E2的
$|\delta|\to\infty$ 极限、分母零点和响应可实现性。
两个根不必分别落在 $|\delta|<1$ 与 $|\delta|>1$；
它们也不自动具有相同的联合似然。增加偏振或ICC资料可以提供区分，
但能否消歧由实际响应与误差决定。若只是独立拼接任意 $R(\delta)$
和 $P(\delta)$ 曲线，不能据此声称得到某真实自旋序列的DCO与偏振预言。

若原始DCO计数在两角组间交换待测线1和门线2，效率乘积也一起交换：
应使用两条线对应的完整联合响应。只有证明门效率已归一或约去时，
才可省略门线效率。上游门与下游门不能仅靠单光子角分布相互替代。

### 3. 从一步宽度到最终缓发中子多重度

[[dimitriou-2021-beta-delayed-neutron-reference-database]] 提供缓发中子数据定义
及其评价语境。本任务在明确只含gamma和逐次单中子出口的状态网络中，
定义 $\pi_x(s)$ 为从状态 $s$ 出发最终发出恰好 $x$ 个中子的概率，
并定义一步转移概率
$p_\gamma(s,t)=\Gamma_\gamma(s,t)/\Gamma_{\rm tot}(s)$、
$p_n(s,u)=\Gamma_n(s,u)/\Gamma_{\rm tot}(s)$。

则全概率公式要求

$$
\pi_x(s)=
\sum_t p_\gamma(s,t)\pi_x(t)
+\sum_u p_n(s,u)\pi_{x-1}(u),\qquad \pi_{x<0}=0.
$$

无进一步开放中子出口且已退激终止的状态取 $\pi_0=1$、
$\pi_{x>0}=0$；若有直接多中子或其它粒子出口，必须显式增加相应转移核
及终态分类。gamma支路可以到另一个阈上态，并不一定立即终止中子级联。
这说明最终 $\pi_x(s)$ 一般不等于某个局域瞬时宽度
$\Gamma_{xn}(s)/\Gamma_{\rm tot}(s)$。只有将分子明确定义为已经积分
整个级联的有效最终分支，或在特定单步近似成立时，才可这样简写。

给定母核beta衰变的馈送概率 $I_\beta(s)$ 后，

$$
P_{xn}=\sum_s I_\beta(s)\pi_x(s),\qquad
P_{\ge1n}=\sum_{x\ge1}P_{xn},\qquad
\langle M_n\rangle=\sum_{x\ge1}xP_{xn}.
$$

$I_\beta$ 是对beta分支归一还是对母核全部衰变归一，必须与所报
$P_{xn}$ 的口径相同；百分数与0至1概率不能在式内混用。
核态间的统计宽度竞争是概率处理，不因称“多道”就意味着相干振幅求和。
“缓发”的主要等待来自beta母态衰变；馈送后的中子与gamma退激时间
应分别处理，不能把所有缓发中子事件统称为纳秒至微秒延迟。

### 4. 一阶禁戒贡献的跨壳层反例

本任务直接回读
[[doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives]]
所存的arXiv:1301.5225v1原PDF，定位如下：

| 原件位置 | 作者的计算或讨论 | 不能据此推广的陈述 |
|---|---|---|
| PDF p.5，130Cd调参段 | 用该核半衰期拟合 $q_{\rm GT}=0.66$；作者明确说GT主导，FF约13%的影响不可忽略 | 130Cd必由FF主导；该拟合是独立的留出验证 |
| PDF p.7及Fig.5 | 所计算的N=50、Z≥28核中，FF贡献小于5%；讨论78Ni中IPM阻塞与组态混合的部分解阻塞 | 78Ni因跨主壳就必由FF主导；壳模型等同于没有组态混合的独立粒子模型 |
| PDF pp.10–11及Figs.14–16 | 所研究N=126同中子素中，Z≥70时FF超过GT；给出占据、相空间与分量的解释 | 所有丰中子核、所有同位素或所有现代模型都如此 |
| PDF p.4，算符淬灭讨论；p.5 Eq.(16)附近 | 区分各FF算符，有相对增强的类时轴荷分量 | 所有弱轴流用一个常数淬灭；所有空间分量统一同值 |

这些是2013年指定模型空间、有效相互作用与调参下的作者结果，
不是本轮新实验评价。原文“对half-life的贡献”不能未经重建就
偷换成严格定义的 $\lambda_{\rm FF}/\lambda_{\rm total}$ 数值。
推理的重点是占据、矩阵元与有限Q相空间共同决定通道竞争，
而非用质量数或“跨主壳层”单一标签判定主导机制。

### 5. 带号与来源版本是物理身份的一部分

[[xiao-xiao-2019-high-spin-74as-thesis]] 的PDF pp.45、47
讨论负宇称Bands 3/4，并认为其不满足当时采用的手征判据，
保留可能的赝自旋伙伴解释。
[[xiao-2022-chirality-octupole-correlations-74as]] 的讨论重点是
Bands 1–3与E1网络。后文只讨论三条带，不足以推出另一版本中的
Band 4“从未观测”或“物理上不存在”。必须回原能级纲图核对
能级能量、端点、自旋与带号映射，再进行跨版本比较。
这两篇也属于同一实验谱系，不能作为两次独立重复测量。

### 6. 本底扣除的不确定度与事件计数单位

本任务对 $S=P-aR$ 作一阶误差传播，得到

$$
\begin{aligned}
\mathrm{Var}(S)\simeq{}&
\mathrm{Var}(P)+a^2\mathrm{Var}(R)+R^2\mathrm{Var}(a)
-2a\,\mathrm{Cov}(P,R)\\
&-2R\,\mathrm{Cov}(P,a)+2aR\,\mathrm{Cov}(R,a).
\end{aligned}
$$

若 $a$ 是确知时间窗宽度之比，有限的R计数不会自动让 $a$ 不确定；
若 $a$ 从同一数据拟合，就需考察交叉协方差。只有独立Poisson计数、
固定 $a$ 等条件下，才简化为 $P+a^2R$。一个物理事件可向多个矩阵格
填入相关计数，对称镜像格更不能当独立测量。
扣除后的负值是有符号估计量，不是负辐射强度；
它的期望在无信号零假设下才为零。

### 7. DDCM导数的符号与归一

本任务先从速率方程作如下有限模型推导，再用已找到的
[[dewald-2012-ddcm-recoil-distance]] 原PDF pp.38–40／印刷pp.823–825
核对门与导数。对恒定非相对论速度 $v$、瞬时阻止、固定初始布居，
令 $n_i(t)$ 为能级布居，$S_i(t)$ 与 $U_i(t)$ 分别为该能级所有
出口在 $t$ 前与 $t$ 后的累计发射数。若只有指定的馈送与退激，

$$
\dot n_i=-n_i/\tau_i+\sum_k b_{ki}n_k/\tau_k,\qquad
n_i(t)=U_i(t)-\sum_kb_{ki}U_k(t),\qquad
\dot S_i=n_i/\tau_i.
$$

因此在 $t=x/v$、$\dot S_i\ne0$ 的上述模型中，

$$
\tau_i=\frac{U_i(x)-\sum_kb_{ki}U_k(x)}
              {v\,dS_i(x)/dx}.
$$

以增加距离时 $S_i$ 增加的定义，分母前没有额外负号。
若观测的只是某条出口，须先按其分支与响应归一；不能把不同母态
不同光子出口的强度直接代入上述总出口关系。

上方移位馈送门还会使门事件总数随距离变化。设 $I_{ss}$ 是馈送光子
与目标光子均移位的计数，$I_{su}$ 是馈送移位而目标停止后的计数，
则在对应理想模型中 $I_{su}$ 与边界时刻的目标布居相联系，
可导出 $I_{su}/[v\,dI_{ss}/dx]$ 型关系。由于
$I_{ss}+I_{su}$ 一般不是距离无关常数，不能无条件换成
$-I_{su}/[v\,dI_{su}/dx]$。实际应用仍需原方法定义、纯净门、
有限速度分布、靶与阻止箔内退激和联合响应核查。

原综述的PDF p.40／印刷p.825 Eqs.(32)、(34)正是直接上方馈送
$B$ 的移位分量设门时的 $\{B_s,A_u\}/[v\,d\{B_s,A_s\}/dx]$；
更上方的间接馈送门还含额外项，见同页Eqs.(30)、(33)。
PDF p.38 Eqs.(19)–(21)给出单谱的未移位分量及馈送修正，
PDF p.39 Eqs.(24)–(29)定义双光子的时间区间。不能把一般符合强度
中成立的导数恒等式，不经重新检查就搬给距离相关的移位门归一。

### 8. “95%”的对象：93mMo上限的原件反例

本任务回读
[[guo-2022-mo93m-isomer-beam-depletion-limit]] 的六页原PDF：
PDF p.2的实验在HIRFL兰州，采用
$^{12}\mathrm C(^{86}\mathrm{Kr},5n)^{93m}\mathrm{Mo}$、
559 MeV束流及35 m的RIBLL输运。它不是ATLAS实验。

PDF p.4以268-keV附近计数和本底的指定保守构造估计约50个峰计数，
再用Eqs.(1)–(3)得到 $P_{\max}\simeq2\times10^{-5}$。
同段的95%指假设高斯峰在中心3-keV窗中的面积接受比例；
不能把它挪作这一激发几率上限的“95%置信水平”。
上限与此前百分比结果的比较仍要保留束流能量、离子状态与停止条件，
不能把不同设置的差异直接写成原实验同条件下的数学排除。

### 9. 模型输出与角动量近似的跨章接口

[[frauendorf-2014-transverse-wobbling]] 原PDF p.6的HFA作为起点，
本任务将顺排轴标为1，并在领先经典 $I^2$ 球上展开。固定投影 $j$ 时，
$C_{2,3}=A_{2,3}-A_1+A_1j/I$，因而

$$
\frac{(\hbar\omega)^2}{4}
=[(A_2-A_1)I+A_1j][(A_3-A_1)I+A_1j].
$$

两个线性因子的乘积不必在全稳定区单调下降。正的局域激发能要求所选
能量极小的两曲率均正；仅根号为实数更弱。玻色对易也使用
$\mathcal I_1\simeq I$ 的同一局域近似，不是有限I的精确恒等式。
原件的完整QTR与冻结顺排近似应分开，不能以HFA限制代表所有PRM。
这些是指定模型与本任务的局域代数重构，不是一个核的实测惯量或模式确证。

[[duguet-2015-non-observable-nuclear-shell-structure]] 所强调的ESPE定义
也约束模型比较表的写法：自洽平均场单粒子本征值不自动等于Baranger型ESPE，
更不能当作独立实验谱重心。同样，PES、参考态成分和谱因子属于带约定的
模型输出。把表头写作“输出与观测联系”，并逐量说明映射，胜过将它们全部
称作直接可观测量。Feshbach的正交P/Q消元是给定哈密顿量的一种构造，
不是所有经验EDF与集体模型都已完成的字面投影。

## Assumptions

电多极强度采用同一算符及单位；DCO推导固定门跃迁与响应；级联例子
只含显式列出的通道；协方差公式采用一阶近似。各节另有更具体限制。

## Competing Explanations

大相对分支既可来自分子增强也可来自分母阻碍；多个混合比分支可同时
与部分观测相容；阈上馈送可继续发中子，也可经gamma链进入束缚态。
这些不同机制应通过共同前向模型比较。

## Transfer Conditions

跨核区可迁移定义和守恒关系；通道主导性、单K映射和误差大小需重新核验。
同一实验的论文与学位论文不能自动当成独立重复证据。

## Failure Conditions

漏掉电多极辐射常数、重复加ICC、将DCO分母固定成错误形式，
或把最终级联几率等同于一步宽度，都会破坏前向一致性。
把任意教学曲线称为真实核素的预言也超出本页范围。

## Falsification or Reverse Tests

检查同母态全部出口归一、量纲、纯多极极限、级联概率和、镜像计数
协方差；将模型对未参与调参的寿命、偏振和分支预言与独立资料比较。
这些测试能推翻具体实现，不能单凭通过就确证模式。

## Open Questions

- 将上述关系用于实际实验还需要门选、有限几何、馈送和响应参数，
  不能把定义正确当成某个模型已获确证。
- 任何新图必须与正文同一前向定义一致，并标明是实验数据、
  作者模型还是本任务的教学计算。
- 本页的数学推导不代替对各章中真实能级端点和数值的逐项原件核验。

## Human Review

本轮为智能体的原件与代数自审，没有记录新的用户审核事件。

## Promotion or Rejection History

2026-11-13：建立共同定义及反例记录；尚未接受的正文与图仍须各自返修和核验。
