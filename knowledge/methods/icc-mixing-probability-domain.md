---
type: method
title: ICC反演混合比：物理域、概率测度与pure端点
aliases: [ICC mixing probability domain, mixing-ratio Jacobian, ICC delta tail]
created: 2026-10-18
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
method_type: uncertainty-and-identifiability
tags: [internal-conversion, mixing-ratio, covariance, probability-measure, physical-boundary]
---

# ICC反演混合比：先定义概率对象

## Purpose

[[rezynkina-2017-graphical-extraction-multipole-mixing-ratios]] RZ17-8–12是实际Table1/原式与本任务测度审计的入口。本页给可复用的物理域/Jacobian/尾部合同，不提供新251Fm/W178实验mixingratio或通用置信区间。源“mean/68%/convolution”与实际算法复现要分层。

## Inputs and Assumptions

纯component coefficients记A1/A2，测得mixed记E，先确认同一shell/energy/atomicmodel/实验接受，按source定义q=d²、E=(A1+qA2)/(1+q)。以下只讨论A1>A2、d=abs(delta)>0；反向单调或label交换须重新写域与Jacobian，不把符号从ICC量恢复。

RZ17示例指定A1=14.49(.21)、A2=.227(.004)、E=8.8(3.1)，M2/E3/K/200keV。**本任务选择**三个独立Gaussian概率输入并条件H={A1>E>A2>0}，没有得到原实验likelihood、atomic共同Cov或作者RooFit实现。Quotederror作为Gaussian是source的假设，不自动等于频率覆盖。

## Core Relation

固定A1/A2时

\[
a(d)=A_2+\frac{A_1-A_2}{1+d^2},\qquad
p(d\mid H)\propto G_E[a(d)]\frac{2d(A_1-A_2)}{(1+d^2)^2}.
\]

理论参数不固定时，积到joint density并除Z=P(H)；域外概率不能夹成d=0或∞后声称无损。普通likelihood L(E|d)没有这个变换Jacobian；flatd prior与flatf prior也不同。只给P(delta)四个字不能决定上述选择。

令X=A1−E、Y=E−A2，虽原输入独立，Cov(X,Y)=−Var(E)；本例correlation−.99771255。写q=X/Y、再d=sqrt(q)时不能把X/Y的两个误差再按独立分子分母传播。独立路线

\[
p(d\mid H)=\frac{2d}{Z}\int_0^\infty y\,f_{XY}(d^2y,y)\,dy
\]

可核同一density；若负A2概率不可忽略还须保留该额外条件，本source例其概率小于1e−700。

## Printed convolution与可复现性

RZ17 Eq11–13分别让一输入变动、其它固定，三个Pi都峰在正d0。若Eq14的⊗直接指普通独立sum convolution，则均值必为三个均值之和；theoryerror→0时是Pexp被平移2d0，而非Pexp本身。需要说明zero-centered error kernels、shift、FFT域/边界或别的producerrecipe，才可将这个符号变成程序。

本任务的literal普通convolution mean2.55349未重建source.92；另一个显式jointpushforward mean.924387与source均值相容，但两个interval定义不相同。没有据此宣称实际RooFit用了错误算法，也没有通过调range使其配表。

## Quantitative Exercise

| 对象 | frozenTable1结果 |
| --- | --- |
| 物理域概率Z | .9636291873 |
| direct逆算d0 | .8146850022 |
| jointmean | .9243869963 |
| equaltailed16/84 | [.50937010,1.27145609] |
| mean左右各.34 | [.61566463,1.67006727] |
| sourcegraphicalEq17交点 | [.45154090,1.28236311] |

两种概率区间都不提供未经采样模型证明的frequentistcoverage。图解交点在本分布含约.728064概率只是本例积分，不能升级成普适保守规则。source所报.92^(+.42/−.37)原值保持，actualRooFitrecipe未得，不能重标成上述另一区间。

## Pure端点与尾部

a(d)在d→∞趋A2，若其端点概率密度非零，Jacobian给p(d)∼C/d³，本例C=.0832071531。mean有限、secondmoment对数发散；finitegrid或有限MC的samplevariance不证明Var(d)存在。若忽略变换而用flatd likelihood，则L→Normal(E|A2,sigma)>0，0到∞无法归一。额外prior/range必须显式定义。

以f=d²/(1+d²)存辐射高阶份额可保持[0,1]有界拓扑，但这不消除phase sign、多multipole、ICCmodel或选择/响应不确定度。Pure限值作为f=1保留，不能靠任意dmax把它“排除”。

## Counter-evidence and Missing Companion Observables

均值重建成功不说明原区间/producer也重建；图解/PDF都依赖theory及同对象实测ICC。Sign仍需matched interference observable。Atomic共享Cov、electron/photon响应、peak-gate ledger和真实likelihood若未知，先写readiness，不把toyGaussian替进真实实验。

## Reproducibility

[原创程序](../../system/scripts/day16_rz17_probability_measure_audit.py)以实际Table1参数、GaussHermite/Legendre收敛、独立二元Gaussian ratio解析式及800000MC交叉核验。过程来源/输入/结果hash保存在本日run；source原humanreview全文prefix保持，新判断仅Codex selfaudit。

## What It Can Establish

在明确概率输入、物理域和归一后重建同一分布的mean、分位数与尾部；用zero-theory-error、Jacobian和普通卷积的均值不变量检查算法含义。可精确复算源Eq17交点，并指出尚未恢复的producer配方。

## What It Cannot Establish Alone

不能把本任务的Gaussian条件分布宣称为原实验likelihood、作者RooFit输出或频率覆盖；不能由ICC恢复δ符号，或在缺真实response、atomic共同Cov和选择条件时替换已发表实验结果。

## Sources

- [[rezynkina-2017-graphical-extraction-multipole-mixing-ratios]] RZ17-8–12，printed97 Table1/Eqs7–15、printed98 Eq17/Fig3。
- [[internal-conversion-analysis]]与[[multipole-mixing-ratio]]：相同shell/δ²/选择响应合同，不把概率推导替成实验事实。
