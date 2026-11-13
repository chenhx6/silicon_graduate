---
type: research-note
title: "A130重写研学：同核异能态机制、Seniority 半满壳相消与 K 阻碍度选择边界"
aliases: [A130 seniority and K selection rules in nuclear isomers]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "针对博士论文第4.6节同核异能态多体波函数选择定则与半满壳相消的微观推演"
promotion_target: ""
evidence_sources: [book-jain-nuclear-isomers, book-bohr-mottelson-nuclear-structure-vol2, continuation-g18-lukasiak-1979-191ir-triaxial-rotor, nndc-130sn-adopted-2001-snapshot-20261113]
tags: [A130, doctoral-foundations, isomers, seniority, quasi-spin, k-isomers, shape-isomers, fission-barrier]
---

# 同核异能态的选择性阻碍与可检验边界

## Research Trigger

第4.6节需要把低能相空间、单体代数、K选择与形状势垒分别讲清，再讨论叠加。
本轮父核查纠正了Sn130半满壳误用、Ir191寿命外推及Hf178光子出口混淆。

## Grounded Evidence

| 来源原件 | 本轮实际定位 | 支持内容与边界 |
|---|---|---|
| [[book-jain-nuclear-isomers]] | PDF52–54／印刷41–43，Eqs.(3.11)–(3.21) | 单j准自旋与单体偶多极的粒子数归约；不同seniority及多轨道情形另论。 |
| 同书 | PDF95–96／印刷84–85，Fig.5.4 | Hf178的四准粒子高K例及部分能级图；2446.1-keV的16+态标31年。图中部分自旋带括号，不补造精确分支和转换系数。 |
| [[nndc-130sn-adopted-2001-snapshot-20261113]] | 2001评价采用表，cutoff 2001-05-11；10+态及其96.54-keV支路 | 采用能量2434.79(12)keV、半衰期1.61(15)微秒，到2338.26(11)keV的8+态；alpha=1.829，B(E2)=0.38(4)W.u.属于评价与反演量，不是独立于寿命的新测量。 |
| [[continuation-g18-lukasiak-1979-191ir-triaxial-rotor]] | 实际完整XML原件；摘要及低能模型讨论 | 摘要报告激发能超过2MeV、5.5(.7)s异能态；低能PRM与高自旋异能衰变闭环分开。不引用并不存在的另一份PDF/SHA。 |

原件路径与实际哈希回各source页面；本页不复制未经逐字节核实的旧稿路径。

## Provisional Reasoning

令Omega=(2j+1)/2。单j同种费米子体系的准自旋为
S=(Omega-v)/2、S0=(n-Omega)/2，J=0对升算符每次增加两个粒子。
对单体偶L>0电算符，Delta-v=0的RME缩放为

$$
\langle j^n vJ_f\|T(EL)\|j^n vJ_i\rangle
=\frac{\Omega-n}{\Omega-v}
 \langle j^v vJ_f\|T(EL)\|j^v vJ_i\rangle ,\qquad v<\Omega.
$$

同一多重态允许n=v,v+2,...,2Omega-v；半满节点还须满足n与v同奇偶。
Omega5、v2的允许占据是2、4、6、8，没有n5；Omega6、v2则可到n6。
v=Omega时缩放公式的分母不可用，须单独处理S=0选择定则，不能解释为发散。
纯h11/2、v2、n10的因子为−1，模平方与两粒子相同；不能将Sn130称为半满节点。
真实Sn同位素中的占据并不由A单独决定，还需多轨道模型及有效算符。

独立数值控制见`system/scripts/a130_seniority_fock_controls.py`：在真实反对易的
稀疏Fock基底中，从两粒子最高权J=2j−1态施加J=0对产生算符，直接计算
T20=sum[3m^2−j(j+1)]n_m的期望，检查其固定J、M的粒子数因子。
Omega5得到相对值1、1/3、−1/3、−1；Omega6得到1、1/2、0、−1/2、−1。
这检验对角E2矩阵元及相同J下的RME缩放，不冒充全部跃迁、寿命或实测核素拟合。

轴对称强耦合近似下DeltaK<=L；对DeltaK>L定义nu=DeltaK−L>0，
FW=B_W/B、fnu=FW^(1/nu)。这是比较量的定义，不是SU2推导出的微观幂律。
从总分支b_tot提取部分光子寿命时，tau_gamma=tau(1+alpha)/b_tot；
若b_gamma已经是相对于全部母态衰变的光子概率，则tau_gamma=tau/b_gamma。
两种口径不能重复乘ICC。固定B与能量时，增加IC会提高总率、缩短寿命。

K混合后的RME是初、末两端系数与基底矩阵元的相干双重和；小系数主导时
才可近似用其模平方估计阻碍。非正交投影基底还需重叠度规，不能用简单
sum|cK|^2=1替代。Coriolis和其它残余作用也可能混K，低fnu并非三轴形状独证。

Jain的Hf178图示16+2446.1到(13)-2433.3的端点差约12.8keV。
若讨论最低允许E3及名义K16到K8，则nu=5；这不是一个已测fnu数值。
级联中的495keV线不能被移作此异能态的直接E3出口。
形状异能态的WKB指数另需集体路径、势面及质量；不能凭冷态寿命给出hot-fusion存活截面。

## Assumptions

单j缩放采用同种核子、纯seniority与固定单体算符。K公式采用指定轴和
强耦合近似；真实支路还需多极性、光子份额和ICC。Fock控制只在所述固定J态中实施。

## Competing Explanations

低能Egamma的高幂压制与小B可以共同产生长寿命；K选择、形状阻碍与多轨道混合
也可叠加。不能把所有寿命都归于单一代数节点或一种几何标签。

## Transfer Conditions

可迁移的是定义、选择定则和给定假设下的推导；具体占据、阻碍数值及
裂变存活需在目标核与反应条件下重新核验。

## Failure Conditions

把Omega奇数、偶v的连续抛物线零点当作实际允许粒子数；把Sn130当半满；
把IC当作给定B条件下的寿命延长原因；给Hf未核分支虚构fnu；
将Ir低能PRM的适用范围外推为高自旋异能寿命已被完整重现，均超出证据。

## Falsification or Reverse Tests

先独立确定目标模型的轨道占据及适用有效算符，再用同一参数比较一组
同seniority跃迁；若粒子数缩放和相关磁矩、电磁资料联合不符，再比较
多轨道混合、seniority破缺等解释。不能预先把某段N范围指定为半满并据此“证伪”。
对K混合则比较多个实际部分支路及其相位敏感组合，而非只看总半衰期。

## Open Questions

哪些实核资料足以区分多轨道seniority变化与有效算符变化？
哪些高K支路有同一波函数、同一算符与完整分支/ICC的闭环描述？

## Human Review

本轮为智能体的原件与代数自审，没有新增真实用户审核事件。

## Promotion or Rejection History

2026-11-13：父核查后重建，撤回旧稿的错误原件路径、控制字符损坏、
不适用的半满N范围与Hf495-keV出口；保留指定模型与原件边界。
