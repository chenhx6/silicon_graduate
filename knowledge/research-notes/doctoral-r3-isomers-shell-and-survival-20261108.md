---
type: research-note
title: "R3 异能态、壳演化与反应：阻碍、网络和存活的不同层级"
aliases: [R3 isomers shell survival]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "G51/G53研学、总控代数与原件复核"
promotion_target: ""
evidence_sources: [book-jain-nuclear-isomers, doctoral-r1-g33-gintautas-2009-176lu-thermal-equilibration, doctoral-r1-g33-gosselin-2010-plasma-isomers-176lu-180ta, doctoral-r1-g28-otsuka-2023-type-ii-shell-evolution, zagrebaev-2001-superheavy-synthesis-survival, xu-2004-superheavy-high-spin-isomer-stability]
tags: [doctoral-foundations, isomer, seniority, k-mixing, thermal-network, shell-evolution, superheavy]
---

# 一个态寿命长，不代表它必能形成，也不代表所有环境都保留它

## Research Trigger

连接低能核结构的阻碍机制、天体环境、占据反馈与重离子产额。
相邻主题之间既有共同波函数输入，也有不同的物理过程；
不能以学完某个相邻主题代替其余主题。

## Grounded Evidence

| 来源 | locator | 内容 |
|---|---|---|
| [[book-jain-nuclear-isomers]] | PDF18/印刷6；Ch.3–6 | 机制重叠、准自旋、K与形状阻碍 |
| [[doctoral-r1-g33-gintautas-2009-176lu-thermal-equilibration]] | PDF2–5, Eqs.(16)–(27), Fig.3 | 未知混合V、两簇与破坏 |
| [[doctoral-r1-g33-gosselin-2010-plasma-isomers-176lu-180ta]] | §II–V | 单支电子增强不决定全网络 |
| [[doctoral-r1-g28-otsuka-2023-type-ii-shell-evolution]] | 文章PDF7–8,13,17–19 | 单极、占据反馈和冻结模型干预 |
| [[zagrebaev-2001-superheavy-synthesis-survival]] | PDF1,6–7,9,11 | 分波三阶段与逐步级联 |
| [[xu-2004-superheavy-high-spin-isomer-stability]] | PDF1–4, Figs.1–5 | 阻塞PES、α分支与裂变 |

本轮总控新增回读Jain的PDF18,49–50,94–95,113及Xu四页；
Gintautas/Gosselin/Otsuka/Zagrebaev沿用R1已核定位并作条件推导。
这些入口不意味着全部原计算已重现。

## Provisional Reasoning

### 1. 四种阻碍是物理诊断，不是互斥身份证

Spin trap强调可达末态、自旋/宇称与多极能量相空间；
seniority强调指定空间中算符的代数相消；
K阻碍强调轴对称内禀结构的投影改变；
shape isomer强调不同组态/形状的重叠及势垒。
Jain印刷6明确它们可组合。不存在普适“ΔJ≥3才是spin trap”，
也不能把所有shape isomer都设为2:1轴比的第二势阱。
低能γ率含 \(E_\gamma^{2L+1}\) 与B两个因素，率小不唯一表示矩阵元极小。

单j、相同seniority v、相应一体偶阶电算符的RME可写为

\[
\langle j^n v J_f\|T^{(L)}\|j^n v J_i\rangle
=\frac{\Omega-n}{\Omega-v}
\langle j^v v J_f\|T^{(L)}\|j^v v J_i\rangle,\qquad
\Omega=(2j+1)/2.
\]

需 \(\Omega\ne v\)，并保持纯seniority态/算符条件；
不能把该比式套到v=Ω的奇点。
半满节点限制这类跃迁，不使所有E/M、多极或β衰变率为零。
现实多轨道与seniority混合、有效多体算符可解除节点。
本项目已有精确单j/三体控制和Sn实核反例，R3不重复同义toy。

### 2. K 混合改变的是振幅，不是一个通用寿命倍数

纯轴对称强耦合选择定则在 \(|\Delta K|>L\) 时阻碍；
\(\nu=|\Delta K|-L>0\)、\(F_W=T^\gamma_{1/2}/T^W_{1/2}\)、
\(f_\nu=F_W^{1/\nu}\)是常用表征。ν≤0时不能继续解释为该禁戒度根。
光子分寿命、ICC和总分支关系见[[doctoral-r3-daq-spectroscopy-inverse-20261108]]。
经验fν不是普适常数。

两端混合态
\(|i\rangle=\sum_Ka_K|iK\rangle,\ |f\rangle=\sum_{K'}b_{K'}|fK'\rangle\)
的振幅含 \(\sum_{KK'}b_{K'}^*a_K\langle fK'|T|iK\rangle\)。
可有干涉和多个通道；只以初态一个混合概率或统一自旋幂次求寿命会漏项。
三轴项允许K混合，强度仍依赖组态、矩阵元、能隙和波函数。
所以长寿命不唯一证明γ=0，三轴也不自动消除所有阻碍。

### 3. 两个率满足详细平衡，整张开放网络仍可能不热平衡

光子浴中令 \(n_\gamma=[e^{\Delta E/kT}-1]^{-1}\)，
在适用的EM/热浴条件下
\(\lambda_{l\to u}=(g_u/g_l)A_{ul}n_\gamma\)、
\(\lambda_{u\to l}=A_{ul}(1+n_\gamma)\)。
成对率比给Boltzmann关系；g=2I+1。
它不强制带有生产、破坏或变温的整张网络处在该分布。

将各簇内部快平衡消去后，一个指定的两簇开放模型为

\[
\dot{\mathbf N}=
\begin{pmatrix}
-(a+D_g)&b\\ a&-(b+D_m)
\end{pmatrix}\mathbf N+\mathbf P .
\]

a,b,D单位s⁻¹，P为每秒生产数。闭合、恒温、无源汇时，
非零交换本征率为a+b；开放/变温条件须连同破坏和生产求解。
簇带头比、簇总布居和单能级权重不能互相替代。
Gintautas Fig.3的ns与10⁵s是特定T9、混合与初值算例，非所有astromer的时间门。

孤立gateway在简化的两侧分支、适当稳态条件下，
有效桥接含 \(\Gamma_g\Gamma_m/(\Gamma_g+\Gamma_m+\cdots)\)。
只增强强侧不能独立提升弱侧瓶颈；
Gosselin的180Ta例子体现局部约10倍而整体变化很小的可能性。
不将该例倒推为所有NEEC或所有环境均无效。

### 4. 单极反馈为何既重要又不是“没有它就不能形变”

指定壳模型分解中，ESPE变化含
\(\Delta\epsilon_j=\sum_{j'}V^{\rm mono}_{jj'}\Delta n_{j'}\)，
单极矩阵元有能量单位，占据差无量纲。
Type I比较不同核子数；Type II强调同一核内组态重排改变平均壳结构。
张量力可产生有特点的单极依赖，但中央、LS和其它作用也参与；
ESPE不是一条可直接读取的实验单粒子峰。

Otsuka的154Sm冻结干预依赖参考态：球形HF参考冻结后仍可三轴形变，
不能反写成“冻结单极后核必为球形”。
微观占据、配对与形状相互反馈，不能只用一个E2反演各轨道占据。
转移、核子去除/敲出等在各自反应模型、缺失强度和归一条件下可约束占据。
这不意味只有一种反应才是合法探针。

### 5. 存活与产额为什么不是同一个概率

在三阶段近似、给定E和分波下，

\[
\sigma_{\rm ER}(E)\simeq\frac{\pi\hbar^2}{2\mu E}
\sum_\ell(2\ell+1)T_\ell(E)P_{{\rm CN},\ell}(E)W_{{\rm sur},\ell}(E^*).
\]

前因子为面积，三个因子无量纲。capture到接触、形成复合核、
蒸发后达到特定冷剩余核分别需要不同动力学。
准裂变与热平衡复合核裂变不能只按近对称质量分布唯一判别。
存活因子不能普遍提出分波求和；单点σ也不能唯一反演P_CN或Bf。

更完整的xn存活是对逐步能量、角动量和分支历史的条件平均；
若写归一中子能谱p(ε)，其单位为能量⁻¹，\(\int p(\epsilon)d\epsilon=1\)。
各步Γn/Γtot和终末γ冷却是无量纲概率，
裸Γγ有能量单位，不能单独作为终末“存活率”。
固定中心能量处的乘积只是进一步近似，不代表不同级联步骤统计独立。

Xu2004**确实含Fig.4–5**；四页不意味着只有三张图。
PDF3转引256Fm7⁻总半衰期70ns、裂变部分半衰期0.8ms，
对照无阻碍估计2.5μs，约320倍；不能将0.8ms当总半衰期。
本文给固定组态PES势垒，并明确实际裂变时未必保持固定组态。
非轴向计算相对轴向使该例基态/异能态势垒分别降低2.4/2.6MeV，
是模型结果，不是所有超重核的统一修正。
γ与裂变的率由不同过程决定，但共享组态/形状与配对输入，
不能称微观上完全独立。

计数还需 \(\int dt\,\Phi(t)\int dx\,n(x,t)\sigma[E(x,t)]\epsilon(x,t)\)。
异能态branch、分离器传输、live及衰变链接受度必须一致条件化；
不能凭冷态稳定性直接保证大合成截面，也不虚构固定机时/产额。

## Assumptions

单j代数、近轴K图像、恒温消去、统计复合核与固定组态PES分别有适用条件。
本页没有把这些近似合并成一个通用微观理论。

## Competing Explanations

异能寿命可由能量相空间、不同阻碍、未见分支或电子环境共同决定；
反应产额还受进入/蒸发/feeding影响。对应的额外观测必须针对实际退化。

## Transfer Conditions

跨区迁移的是阻碍与响应的计算方法。
不同核区能否有同类态，须检查可用高j/Ω轨道、占据、配对、势垒与衰变末态；
区名不能提供存在/不存在的定理。

## Failure Conditions

将机制互斥、节点当全部率零、成对平衡当总体Boltzmann、
把Γ当概率或部分寿命当总寿命，会得到错误跨区预测。

## Falsification or Reverse Tests

可测弱分支、ICC、多极/母态身份、独立占据探针和反应激发函数改变解释排序。
具体条件未给全时只形成研究设计，不宣称新异能态或新合成率。

## Open Questions

最有信息量的桥接/占据/产额观测由具体核素与可得数据决定。
未知热轨迹、LEC或全反应producer不构成无限期准备门。

## Human Review

总控对原件和公式作条件核查；不是用户人工审核或新独立测量。
曾怀疑Xu四页不含Fig.4–5，已由原件纠正；不按先前摘要的怀疑删掉真实材料。

## Promotion or Rejection History

- 2026-11-08：补入网络、占据及存活的解释检查；撤回普适阈值与完全独立论，保留实际源内数值条件。
