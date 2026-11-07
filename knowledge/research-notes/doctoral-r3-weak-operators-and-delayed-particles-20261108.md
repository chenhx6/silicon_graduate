---
type: research-note
title: "R3 弱衰变基础：算符、有限能窗、缓发粒子和双 β 的不同合同"
aliases: [R3 weak operators and delayed particles]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "G48/G52研学、T07独立审计与总控原件核查"
promotion_target: ""
evidence_sources: [book-suhonen-from-nucleons-to-nucleus, doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives, engel-menendez-2017-double-beta-matrix-elements-review, cirigliano-2018-leading-short-range-double-beta, dimitriou-2021-beta-delayed-neutron-reference-database]
tags: [doctoral-foundations, weak-decay, ikeda, first-forbidden, beta-delayed-neutron, double-beta]
---

# 同一个“弱强度”名称，可能指不同算符、空间和能窗

## Research Trigger

两翼的基础学习须包含β缓发粒子，不能由GT或0ν主题代答。
本页把总和恒等式、实衰变率、级联粒子分支、实验响应及不同机制分开，
并给出从假设开始的解释检查。不是新的半衰期、Pn或核矩阵元预测。

## Grounded Evidence

| 对象 | 原始入口与locator | 本轮用途 |
|---|---|---|
| Ikeda求和 | [[book-suhonen-from-nucleons-to-nucleus]], 印刷541–543/PDF552–554, Eqs.(17.63)–(17.74) | 完备性与单体代数 |
| GT/首禁戒有效算符 | [[doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives]], PDF2–4, Eqs.(4),(8)–(13),(16) | 强度约定、多rank与CVC条件 |
| 闭合和两体流 | [[engel-menendez-2017-double-beta-matrix-elements-review]], PDF4,17–18 | 轻Majorana动量核与模型依赖 |
| 短程项 | [[cirigliano-2018-leading-short-range-double-beta]], PDF2–5, Eqs.(3)–(18), Figs.1–3 | 非微扰重整化与有限LEC |
| 缓发中子 | [[dimitriou-2021-beta-delayed-neutron-reference-database]], PDF4–11,21,24,84–85 | 定义、效率、级联及竞争 |

综述与其引用的原计算不作两项独立实验；本轮没有重做原反应/多体计算。

## Provisional Reasoning

### 1. Ikeda 的 3 从哪里来

采用 \(t_3|n\rangle=+\frac12|n\rangle\)、\(t_-|n\rangle=|p\rangle\)，
\(O_a^-=\sum_k\sigma_a(k)t_-(k)\)、\(O_a^+=(O_a^-)^\dagger\)。
在完整末态空间对同样的三个笛卡尔分量求和，利用完备性，

\[
S_--S_+=\sum_a\langle[O_a^+,O_a^-]\rangle
=\left\langle\sum_k3\,2t_3(k)\right\rangle=3(N-Z).
\]

不同核子算符对易，且每个Pauli矩阵平方为1。
3来自 \(\boldsymbol\sigma^2=3\)，不是自旋1/2核子有三个自旋投影，
也不是只统计“未配对中子”。一般自旋初态需按一致约定作磁子态平均。
本式强度无量纲且未含gA；若B定义已含\((g_A/g_V)^2\)，差和同步带该因子。

这是**强度差**，不是S−本身，更不是实验有限Qβ窗的积分。
完整空间内改变波函数相关会重分配指定算符的强度；
截断空间、只测某能窗、反应提取偏差和改变物理算符是不同问题。
若 \(J=J_{1b}+J_{2b}+\cdots\)，其对易子还含干涉/两体项，
不能无条件沿用裸单体的 \(3(N-Z)\)。
用q乘单体振幅给q²倍的数学差和，不是同时证明全物理流仍满足裸式。

### 2. “淬灭”为什么不是每种弱过程共享的一个旋钮

β率还要对可达末态乘轻子相空间；允许近似、首禁戒形状因子及干涉各有条件。
FF的rank 0/1/2、轴荷与空间流不同。
Zhi的有限壳空间拟合在Eq.(16)给不同算符不同振幅修正；
例如q(x)=q(x′)=0.51而q(ξ′v)=1.266。它们是该实现的拟合参数，
不等于自由核子耦合发生同样变化，也不唯一证明哪一种微观修正。

CVC约束自由核子矢量荷的零动量归一化及流的连续性，
不能推出有限空间每个矢量矩阵元均无有效修正。
Zhi还假设同位旋为好量子数，以 \(\xi'y=E_\gamma x\)联系相应矢量项；
这里的能差是IAS(i)到f，并非任意电子端点，单位按原文除以 \(m_ec^2\)。
下折叠的Hamiltonian与荷/流须一致；只投影裸算符未必保留同样连续性。
T04已隔离Table I的内部数值疑点，本轮不猜数值或重拟合。

### 3. 喂到阈上态，为什么不等于最后一定发中子

β布居某个 \(E_i>S_n\) 的态，只说明中子道能量上可能打开。
在指定短程、近阈分波条件下，\(\Gamma_n\)可有
\(\epsilon_n^{l+1/2}\)的阈值行为；角动量、宇称和残核态决定可用l。
质子还受库仑势垒影响。阈值幂律不能推出所有阈上态均由γ主导。

对一个只允许“发一个n后终止”或“γ直接到束缚态后终止”的孤立态，
\(p_{n,i}=\Gamma_{n,i}/(\Gamma_{n,i}+\Gamma_{\gamma,i})\)。
若γ先到另一阈上态，或第一次发n后剩余核还能发n，这个一阶分支不是最终Pn。
各级宽度可先除以ħ作速率，分支比无量纲；不能把能量宽度与s⁻¹直接相加。

**任务推导：**为每个已布居态定义最终中子多重度生成函数 \(F_s(z)\)。
在有向退激级联、所列通道完备、暂不含环境再激发时，

\[
F_s(z)=\sum_{\gamma:s\to t}b_{st}^{\gamma}F_t(z)
 +\sum_{n:s\to u}b_{su}^{n}zF_u(z)
 +\sum_{\rm other} b_{sv}^{\rm other}F_v(z).
\]

终止态 \(F=1\)。other通道如也放出中子须带相应z幂，且残核身份随通道改变。
本式是记账框架，不是用统计宽度代替真实逐态资料。
令f_s为**每次β衰变条件下**的feeding分布，则
\(P_{xn}^{(\beta)}=\sum_s f_s[z^x]F_s(z)\)。
若按母态所有衰变归一、且只有β支路引出所计的缓发中子，还需乘母态β分支bβ。
衰变链后代稍后发的中子不是同一次prompt级联，测量时另作Bateman/相关背景处理。

\[
P_{\ge1n}=1-P_{0n}=\sum_{x\ge1}P_{xn},\qquad
\bar\nu_d=\sum_{x\ge1}xP_{xn}.
\]

P0n意为零中子，不必“纯γ”；有βp等其他道时尤其如此。
文献Pn有时指P1n、有时指P≥1n，必须逐来源明确。
分离能用原子质量时
\(S_n(Z,A)=[M_{\rm at}(Z,A-1)+m_n-M_{\rm at}(Z,A)]c^2\)；
若全部使用质量过剩，应将中子项也换为Δn，不能混两种记号。
中性原子β−的标准Q定义与电子/电离修正须另注明。

### 4. 探测一个中子为什么可能来自发了两个中子的事件

IAEA Eq.(1)定义P1n；Eqs.(2)–(4)展示简化效率相消及其修正。
在理想独立等效率计数、无串扰/死时间/偶然的特殊模型中，
发出x个中子而探测y个的响应为
\(R_{y|x}=\binom{x}{y}\epsilon_n^y(1-\epsilon_n)^{x-y}\)。
真实响应还随谱、能量相关、β阈值与时间窗变化，不能直接当作上述二项式。

一般计数关系写为 \(N_y=N_\beta^{\rm true}\sum_xR_{y|x}P_{xn}+B_y\)，
β接受度可并入联合R；若Nβ本身是探测计数，需相应归一，不能重复校正。
\(\langle\epsilon_\beta'\epsilon_n\rangle\)不普遍等于
\(\langle\epsilon_\beta'\rangle\langle\epsilon_n\rangle\)。
IAEA PDF6–7给出的β能量与中子能量相关是实际方法反例。

HPGe漏掉高能分散γ级联会引入Pandemonium偏差；
TAGS改善总feeding信息，也需处理n在闪烁体中的反应响应（PDF11）。
不能把TAGS或triggerless数字DAQ设为所有缓发粒子实验的唯一必要技术。
单个988-keV γ病例不自动给绝对Pn，也不单独测定N=82壳隙改变。

### 5. 0ν 为什么不能直接照搬低能 β 的 q²

以下限定为两个标准左手弱流之间的**轻Majorana中微子交换**。
其幅度含 \(m_{\beta\beta}\)，虚动量为宽积分，典型核动量为百MeV/c量级。
允许近似下2ν的1⁺ GT中间态，与0ν的多极/动量核不同。
闭合用代表性能差替换分母，再用完备性；
动量较大提供动机，不保证所有核、算符和能差的误差一致。
单β的有限Q窗、2ν的实际轻子/中间态分母、0ν的虚动量积分是不同权重。

Cirigliano2018将轻中微子核夹在非微扰1S0强散射之间，
发现仅重整化强NN势不足以使跃迁幅度独立于紫外调节。
在原文省略公共弱耦合后的约定，
\(V_{\nu,\mathrm{CT}}=-2g_\nu^{NN}\tau_1^+\tau_2^+\)，
其无量纲化参数满足
\(\mu\,d\widetilde g_\nu^{NN}/d\mu=(1+2g_A^2)/2\)。
原文τ⁺将n变p，与本页第一节t−命名不同。
尺度运行不能决定有限积分常数；长短程项分别的数值不是无方案可观测量。
所核CIB数据限制C1+C2，而gνNN=C1；C1≈C2是额外假设。
理解这段重整化论证是有限学习目标，求出未知LEC是另一个研究课题。

## Assumptions

代数完整空间、有效空间与物理流分别声明。
级联式假设给定分支/终止条件；有再激发或循环时须解相应主方程。
统计HF近似的态密度条件与离散逐态处理不混同。

## Competing Explanations

Pn/半衰期变化可来自Q、GT/FF、组态、自旋排序、形变、阈值后分支或测量响应。
需要联合母态分辨谱、β强度、粒子谱、多重度与γ支路，再限制模型。
拟合一个率不能唯一识别gA、壳隙或某个形变。

## Transfer Conditions

跨区复用算符和响应合同；数值迁移需重算占据、空间、Q窗、分波、余核能级与环境。
六区的形状研究能约束波函数输入，不代替弱算符与连续谱校准。

## Failure Conditions

混淆P1n/平均中子数、遗漏β母分支、把阈上feeding当最终Pn、
把CVC推广成所有有效算符不变，或将短程例子百分比当经验常数，均破坏推论。

## Falsification or Reverse Tests

有意义的新增观测是同母态的绝对feeding、n多重度和γ竞争联合约束，
以及预先冻结算符后的未拟合分支；不设任意百分比通过线。
本页仅有代数/级联推导，没有真实核Pn拟合或2018之后LEC全景检索。

## Open Questions

具体候选核哪一段强度在Q窗、Sn附近且受不同FF/形变模型分歧支配？
原件及响应足够时再建L4；没有输入时保留可检验合同。

## Human Review

总控与T07定向原件核查，不记录虚构的人工审核。
G48/G52工作稿的自造阈值、普适强度搬迁和过强壳隙归因未采纳。

## Promotion or Rejection History

- 2026-11-08：实质补入β缓发粒子并修正弱算符解释；作为第一阶段基础，未宣称前沿已解决。
