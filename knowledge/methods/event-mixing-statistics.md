---
type: method
title: 事件混合中的复用与比值协方差
aliases: [event mixing statistics, mixed-partner covariance, event-level variance floor]
created: 2026-10-16
updated: 2026-10-16
status: ai-draft
review_status: unreviewed
method_type: gamma-gamma-coincidence-statistics
tags: [event-mixing, covariance, u-statistic, physical-event, identifiability]
---

# 事件混合中的复用与比值协方差

## Purpose

[[smith-2019-griffin-angular-correlation-analysis]] SG19-4（v1 PDF6–7 Sec3.2）描述以同一interaction配多个partners提高mixed分母统计量，但未提供本Wiki可直接使用的event ledger/完整Cov。本页从一个明确的chosen配对算法推导复用方差及prompt/mixed cross covariance；是本任务L2统计推导，不是GRIFFIN真实误差重算，也不否定SG19-5/6的实测响应闭合。

## Inputs and Assumptions

每个physical event有两个已记录的二元标签`Z_i=(X_i,Y_i)`，不同i独立、固定事件数N。它们只是coarse response/direction tags，**不是实际γγ角响应或GEANT4输入**。选择`p=P(X=1)=.35、q=P(Y=1)=.60、c=Cov(X,Y)=.02`；按00/01/10/11排列的joint概率为`(.28,.37,.12,.23)`。定义一个pair bin `H(X,Y)=1[X=Y]`。

prompt取同一event的两标签：`P_N=N⁻¹ sum_i H(X_i,Y_i)`。mixed的每个trigger X_i从其它N−1个events中均匀**无放回**选K个不同Y_j，排除j=i；不同行的partner选择条件独立。生产程序若采用固定时间邻居、全局不复用、其它权重或不同池大小，本页公式不能照搬。这里没有DAQ、background、time drift、efficiency、未探测photon或真实spin/multipolarity输入。

输入身份`DAY15-20261016-SYNTHETIC-MIXED-EVENT-01`，JSON SHA-256 `b0a0bb6503d01e8dc432e1a866960872b4fbc1bebd89a1737ca766eab9bab72c`；N/K为physical events/每trigger的partners数，概率、比和sigma均无量纲。不是把NK个pair entries声明为NK个独立衰变。

## 复用事件的精确方差与退化控制

### 从全配对到U统计量

全配对均值为

\[
M_N=\frac{1}{N(N-1)}\sum_{i\ne j}H(X_i,Y_j),\qquad
a=E P_N=.51,\quad m=E M_N=.47.
\]

令`Sx=sum X_i、Sy=sum Y_i、Sxy=sum X_i Y_i`，可独立核算

\[
M_N=1-\frac{S_x+S_y}{N}
+\frac{2(S_xS_y-S_{xy})}{N(N-1)}.
\]

用对称kernel `h_s(Z,Z')=[H(X,Y')+H(X',Y)]/2`，M_N等价于二阶U统计量。其一阶投影的两倍为

\[
\psi(Z)=(2q-1)(X-p)+(2p-1)(Y-q),
\quad V_1=\operatorname{Var}\psi,
\quad V_2=2\operatorname{Var}(h_s)-V_1,
\quad C=\operatorname{Cov}(H(X,Y),\psi).
\]

对独立physical events做重叠指标计数或Hoeffding分解，精确得到

\[
\operatorname{Var}(P_N)=\frac{a(1-a)}{N},\qquad
\operatorname{Var}(M_N)=\frac{V_1}{N}+\frac{V_2}{N(N-1)},\qquad
\operatorname{Cov}(P_N,M_N)=\frac{C}{N}.
\]

本例`V1=.0283、V2=.22、C=.0331`，是从四状态概率推得的数，未由GRIFFIN数据取得。即使记录所有N(N−1)个ordered pairs，非退化的一阶投影仍留下1/N方差项。

### 有限partners的配对噪声

在上述逐行无放回算法下，条件于同一批physical events，mixed均值`M_NK`的条件期望就是M_N。每行是有限总体抽样；对coarse equality kernel平均条件方差后得到

\[
\operatorname{Var}(M_{NK})=
\underbrace{\frac{V_1}{N}+\frac{V_2}{N(N-1)}}_{\text{physical-event sampling}}
+\underbrace{q(1-q)\frac{N-1-K}{N(N-1)K}}_{\text{partner selection}},
\qquad\operatorname{Cov}(P_N,M_{NK})=\frac{C}{N}.
\]

条件独立的row choices是必要条件。N>2时可由`E[p_i(1−p_i)]=q(1−q)(N−2)/(N−1)`和无放回有限总体因子相乘推得；N=2,K=1由直接枚举给同一极限。增加K只压低后一项；K=N−1时配对噪声为零，但一般的event样本方差没有消失。

| 固定N=10000，K | 正确mixed sigma | 假设NK个pairs独立的反事实sigma |
| --- | ---: | ---: |
| 1 | .005179749 | .004990992 |
| 10 | .002286876 | .001578290 |
| 100 | .001752084 | .000499099 |
| 1000 | .001689319 | .000157829 |
| 9999 | .001682914 | .000049912 |

反事实使用`m(1−m)/(NK)`，保持同一bin均值但抹去重用相关，不是实际测得误差。最后一行的sigma差约33.7倍是这个自设模型的结果；不能把它套在GRIFFIN已发表error bars上。

### 平衡控制没有非零1/N主导项

改选`p=q=.5、c=0`，则ψ恒为0，`V1=0、V2=1/4`，全配对方差仅为`1/[4N(N−1)]`。所以“复用一定有非零1/N floor”过强；真正条件是一阶投影是否退化。理想对称、匹配权重或受约束校准可能使某些kernel的投影消失；不能只凭肉眼阵列对称或pair数很多便预设此条件。

## 比值传播需要prompt与mixed的交叉项

令`T=P_N/M_NK`，在分母远离零、局部线性传播适用时，

\[
\operatorname{Var}(T)\simeq
\frac{\operatorname{Var}(P_N)}{m^2}
+\frac{a^2\operatorname{Var}(M_{NK})}{m^4}
-\frac{2a\operatorname{Cov}(P_N,M_{NK})}{m^3}.
\]

同一chosen输入在N=10000、K=9999时，完整sigma为`.009782928`；只删cross Cov而保留两边际方差给`.011323625`；把mixed当固定分母给`.010636170`。K=1时完整sigma却为`.014953905`，大于固定分母值。因此仅“忽略分母误差”在这个模型内就可随K低估或高估，不能据惯例称作保守。

### 弱分母与独立验证

代码对N=2/3/4的完整状态、以及N=3,K=1的所有partner choices作独立有理数枚举，均与解析均值、方差和Cov相同。N=2时`P(M=0)=.2801`，比值未定义；上述delta sigma不是这类小样本的精确置信区间。不得静默删去零/负分母再宣称覆盖正确。

独立MC用N=400、20000个重复样本、seed2026101602，逐row以hypergeometric抽样实际实现K=1/10/100/399；不是用一个Gaussian噪声直接生成理论sigma。方差/Cov相对其MC误差的最大绝对z为1.2080，MC ratio sigma/delta sigma为`1.009452、1.005228、.999728、.999587`，零分母观测0次。这验证所选模型及局部传播尺度，不能推成真实experiment coverage或所有N下分母非零。

## 用公开pair计数检查退化假设的条件界

SG19-2的v1 Table1（PDF3）列64晶体，部分opening-angle bin有48个ordered pairs（如33.7°）。**再自设**两能量photon tags各自在64个晶体上独立均匀，H为该bin的binary adjacency；并不假定真实FEP效率/有限几何满足此模型。

每晶体在该bin的integer out-degree为d_j，平均`48/64=3/4`，故不可能所有d_j相等；任何具有该均值的整数degree分布都满足`Var(d)≥3/16`。对symmetric adjacency及独立uniform tags，一阶投影系数有

\[
V_1=\frac{2\operatorname{Var}(d)}{64^2}\ge\frac{3}{32768}.
\]

N=10000时仅这个1/N项的sigma下界约`9.5683e−5`。这是source nominal pair count加chosen uniform采样下的条件界，不是GRIFFIN实际Cov、完整方差或文中χ²的重估。实际需要逐crystal/pair响应、两能量权重、event labels和生产mixed算法；公开表只有总数，不决定完整Cov。

## What It Can Establish

明确区分physical-event数与mixed pair entries，给出在声明算法/概率模型下的精确矩、有限K噪声、退化反例和ratio交叉项；从公开nominal pair总数提出可检验的kernel-degree问题。它可改进mixed reference输入合同与统计验证设计。

## What It Cannot Establish Alone

不能从本页推断GRIFFIN或任何ADO实验漏算了多少误差，不能补真实event ledger、背景、time drift、calibration或full response；也不能授新Jpi/δ/多极性。source的实测χ²改善不因本toy而被否定。固定N且每event都有两标签、row-wise独立无放回等条件改变时，须重新推导。

真实分析至少保存physical-event IDs、partners/复用规则、time/configuration blocks、两能量/cuts、每pair权重及background/normalization谱系。若用bootstrap，须按physical events或合适time blocks重建mixed reference与prompt归一；直接把mixed pair rows独立重采样通常不会检验本页的一阶投影问题。该建议尚未在真实GRIFFIN数据上执行。

## Sources

- [[smith-2019-griffin-angular-correlation-analysis]] SG19-4：PDF6–7 Sec3.2的event-mixing算法动机/时间条件及actual Cov缺口；SG19-2：PDF3 Table1的64晶体/ordered pair计数。数学公式、chosen数值、枚举与MC均是本任务推导，不归为作者报告。
- [[angular-correlation]]“事件混合：效率归一之后仍有有限响应”：先区分single/conditional/full响应；本页只解决一个统计合同。
- [计算脚本](../../system/scripts/day15_event_mixing_covariance.py)、[输入/hash](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/mixed-event-input.json)、[精确/MC结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/mixed-event-covariance.json)、[partner敏感性图](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/mixed-event-partner-sensitivity.svg)。图为纯chosen解析曲线，MC在另一明确N下作验证；没有不匹配N的实验点。输入、公式、概率、数值和边界已在本页保存，不只留在outputs。
