---
type: research-note
title: "A130重写研学：四极不变量重耦合、角宽近似与量子涨落的边界"
aliases: [A130 invariant recoupling and width boundaries]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "冻结Gemini样节G63-v1、Terra T08独立审计与总控原件回读"
promotion_target: ""
evidence_sources: [book-suhonen-from-nucleons-to-nucleus, cline-1986-nuclear-shapes-coulomb-excitation, poves-2020-limits-assigning-nuclear-shape, bohr-1952-surface-particle-coupling]
tags: [A130, doctoral-thesis, quadrupole-invariants, recoupling, gamma-fluctuation, covariance]
---

# 公式看似熟悉，仍须把算符、归一和所估计的宽度说清

## Research Trigger

G63-v1第1.2节把若干高阶公式提前放入引入部分，生成了错误相位/归一，
也把模型量子涨落和几何/势面结论混在一起。
本页保存可复用的数学与解释修正，不把过程审计报告作为论文事实源。
冻结输入在`raw/writing/gpt/A130/review-inputs/G63-v1/manifest.json`，
其用途是定位本任务稿件错误，不能成为核物理正确性的证据。

## Grounded Evidence

| 原件 | 实际阅读/locator | 用途与性质 |
|---|---|---|
| [[book-suhonen-from-nucleons-to-nucleus]] | 印刷29–30/PDF44–45，Eqs.(2.27),(2.29),(2.31)–(2.32) | Wigner–Eckart和厄米相位约定 |
| [[cline-1986-nuclear-shapes-coulomb-excitation]] | PDF16–18/印刷698–700 | 标量网络、对易/截断及低高频分离 |
| [[poves-2020-limits-assigning-nuclear-shape]] | v2 PDF2–4，Eqs.(3)–(17), Table I | 高阶不变量、CI模型量子宽度与形状解释 |
| [[bohr-1952-surface-particle-coupling]] | PDF/印刷9–13,19–21 | 无旋流参考、坐标重标记和集体描述 |

T08独立读上述页，总控另回Poves PDF2–4及Suhonen相关页。
下列重耦合为任务推导，不冒称从OCR不清的Cline式子逐字抄得。
数值控制是有限角动量代数，不是核模型拟合或独立实验。

## Provisional Reasoning

### 1. 固定约定后再展开中间态

令 \(T_\mu=\mathcal M(E2,\mu)\)，
\(R_{ab}=\langle aI_a\|T\|bI_b\rangle\)，采用

$$
\langle aI_aM_a|T_\mu|bI_bM_b\rangle
=(-1)^{I_a-M_a}
\begin{pmatrix}I_a&2&I_b\\-M_a&\mu&M_b\end{pmatrix}R_{ab}.
$$

对厄米球张量，
\(T_\mu^\dagger=(-1)^\mu T_{-\mu}\)，
\(R_{ba}=(-1)^{I_b-I_a}R_{ab}^*\)。
态标签还含同自旋的不同能级，完备和包括相应全部态/连续谱；
截断后不能继续称为全部物理空间的精确闭合。

取初态s的自旋为I，二次标量可写

$$
\langle[T\times T]^0\rangle_s
=\frac1{\sqrt{2I+1}}\sum_r(-1)^{I+I_r}
\begin{Bmatrix}2&2&0\\I&I&I_r\end{Bmatrix}|R_{sr}|^2
=\frac1{\sqrt5(2I+1)}\sum_r|R_{sr}|^2.
$$

原稿的一种中间6j形式相位有误，但它同一行最后的正定形式是对的。
I=1、I_r=1时正确系数为 \(+1/(3\sqrt5)\)，不是负值；
单独使用 \((-1)^{I_r}\) 对半整数还产生错误的复相位。
采用q₂归一后，
\(q_2=\sum_r|R_{sr}|^2/(2I+1)=\sum_rB(E2;s\to r)\)。
I=0时只需2⁺中间态，适合作为正文引入的最小公式。

### 2. 三次重耦合及I=0的简单检查

按相同张量耦合和RME排列，插入两次完备集、对磁子态及CG求和得到

$$
\left\langle[ [T\times T]^2\times T]^0\right\rangle_s
=\frac{(-1)^{2I}}{2I+1}\sum_{r,t}
\begin{Bmatrix}2&2&2\\I&I_r&I_t\end{Bmatrix}
R_{sr}R_{rt}R_{ts}.
$$

保留真实复相位；单态重定相改变单个RME，不改变闭合路径乘积。
I=0时I_r=I_t=2且6j=1/5，所以

$$
\left\langle[ [T\times T]^2\times T]^0\right\rangle_0
=\frac15\sum_{r,t}R_{0r}R_{rt}R_{t0},
\qquad
q_3=-\sqrt{\frac7{10}}\sum_{r,t}R_{0r}R_{rt}R_{t0}.
$$

G63-v1的相同耦合项为 \(1/(5\sqrt5)\)，少一个\(\sqrt5\)；
这不是重定相可以补救的归一差别。
当r=t时，项为\(|R_{02}|^2R_{22}\)，对角元有物理作用；
不能说三个单独非对角符号均可独立观测。
一般式和完整重耦合证明放第2章/附录，第一章只需解释为何q₃需要相干网络。

### 3. 三次张量标量与径向幅度立方是不同对象

为避免同一Q³字面混名，定义
\(\hat A=T\cdot T\)、
\(\hat B=-\sqrt{35/2}[ [T\times T]^2\times T]^0\)，
于是 \(q_2=\langle\hat A\rangle\)、\(q_3=\langle\hat B\rangle\)。
仅在声明的可交换坐标实现和匹配主轴约定中，
\(\hat A=Q^2,\ \hat B=Q^3\cos3\gamma\)。

四到六阶中可选 \(\hat A^2,\hat A\hat B,\hat B^2\)，
对应 \(Q^4,Q^5\cos3\gamma,Q^6\cos^23\gamma\)，
不是三个纯径向幂。六阶并非只有一种耦合选择。
Poves PDF2的 \(\hat Q^3_{\rm P20}=[\hat Q\times\hat Q]\cdot\hat Q\)
是三次标量；若其Q与本页T是同一张量，
\(\hat B=-\sqrt{7/2}\hat Q^3_{\rm P20}\)。
因此五/六阶绝对量也分别带相应一次/平方常数；
归一化相对式中的常数可消去，不能据此删除绝对定义差异。

非对易有效算符实现还要检查次序和厄米性，必要时用对称化协方差。
Cline明确某些IBM有效E2不满足坐标算符的同一对易恒等式。

### 4. 角宽公式的线性传播意义

令 \(a=\langle A\rangle>0,b=\langle B\rangle\)，对
\(C=B A^{-3/2}\)在均值附近作一阶展开，

$$
\delta C\simeq a^{-3/2}\delta B-\frac32b\,a^{-5/2}\delta A.
$$

故

$$
\operatorname{Var}(C)\simeq a^{-3}\operatorname{Var}(B)
+\frac94b^2a^{-5}\operatorname{Var}(A)
-3ba^{-4}\operatorname{Cov}(A,B).
$$

b≠0时除以 \(C_0^2=b^2/a^3\)，得到Poves Eq.(16)形式。
原文确实印出该式；本任务指出其线性传播合同，
而不是将它复述为任意宽波包的精确方差恒等式。
b≈0相对形式病态，b=0未定义；原文Eq.(17)另处理该点的绝对宽度。
在相应线性化极限，
\(\sigma(C)\simeq\sqrt{\langle B^2\rangle}/a^{3/2}\)。

严格坐标条件下，真正角函数矩涉及
\(\langle BA^{-3/2}\rangle\)、\(\langle B^2A^{-3}\rangle\)；
有限的正幂矩一般不能唯一决定这些逆矩或完整分布。
同理，\(\Delta\beta/\beta=\sigma_A/(2a)\)是
\(\beta\propto\sqrt A\)的一阶传播，宽分布时不能无条件当精确标准差。

### 5. 一个正权反例，同时检查有效角和宽度

取等概率Q=1与Q=2，两点均γ=0（声明的教学坐标模型）。
则 \(q_2=5/2,q_3=9/2\)，
\(q_3/q_2^{3/2}=9\sqrt{10}/25>1\)，
而真正\(\cos3\gamma\)恒为1。
无需负概率也可超出反余弦定义域。
同一例真实角函数方差为0，线性传播却给 \(121/6250\)，
直接说明它不是普遍恒等式。
反过来，相同Q、等权γ=0与60°给q₃=0，
也不意味着概率集中在30°。

### 6. 三种“宽度”不能互换

Poves所算 \(\sigma_A^2=\langle A^2\rangle-\langle A\rangle^2\)
是给定模型量子态中的算符涨落。
实验计数/拟合对q₂、q₃估计的统计误差及协方差，
以及改变相互作用/空间得到的模型差异，是另外两类对象。
它们可以使用相似的Jacobian代数，不能共用同一物理含义。
特别是第五阶量给出的量子 \(\operatorname{Cov}(A,B)\)
不等于实验RME联合拟合产生的 \(\operatorname{Cov}_{\rm stat}(q_2,q_3)\)。

Poves Table I确有20Ne:0.24、24Mg:0.25、34Si0₁:1.07、68Ni0₁:1.10，
都是指定CI空间/相互作用下的质量四极结果，
文中使用等标有效因子1.77并另谈电荷分布的相似性。
小的A相对宽度不单独证明γ刚性、深势阱或特定微观惯量。
SU(3)控制只涉及该模型的所选四极不变量，不推广到任意内禀多极算符。

## Assumptions

重耦合固定上述WE/厄米约定；坐标解释另需可交换实现/测度。
参考文献中的算符归一、实验B方向与有效电荷分别映射，不能按相同字母合并。

## Competing Explanations

形状共存、连续幅度/角涨落、模型空间和有效算符都可能改变同样低阶矩。
Poves2020对具体核的解释是其模型比较，不自动裁定2026所有实验争议。
模糊的形状均值也不唯一反推出势能面极小不存在。

## Transfer Conditions

一般自旋重耦合跨区适用；具体几何解释必须对齐核/态、算符、空间、
截断、误差与动力学。Cline的低能饱和量级仅为其模型条件下的概括，
不能保证所有核/初态/高阶矩都漏掉同一百分比。
其低高频分离还需弱耦合和高频振幅相对小等条件。

## Failure Conditions

丢相位/根号、把径向幂当角不变量、混量子宽度和测量误差、
将一阶传播写成精确角分布、或把24轴重标记写成阶数8的D₂h，都破坏推论。
一体约化密度不足以恢复一般两体关联，但不是所有关联影响都被抹掉；
q₂自身还含同核子的自项。内禀描述也不只限平均场态。

## Falsification or Reverse Tests

canonical producer为
[`a130_rewrite_invariant_angular_audit.py`](../../system/scripts/a130_rewrite_invariant_angular_audit.py)。
它用直接磁投影/CG和6j两种表示检查I=0至5/2的20二次、61三次通道，
并给上述坐标反例；本次实际运行退出0，20个二次与61个三次通道全部通过。
producer、原件、冻结输入和产物哈希已登记在
`outputs/l4/20261108-A130-invariant-angular-controls/run-provenance.json`。
这些有限代数检查支持公式一致性，不称独立实验或全部核波函数验证。

## Open Questions

何时可用可得高阶矩约束某个实际核的角宽，仍需算符实现、闭合/误差和模型检验。
此研究服务样节修订与附录，不要求重做已闭合的其它toy或全核素图拟合。

## Human Review

Terra独立审计与总控回原件/代数核查，无虚构用户人工审核。
G63-v1尚未因此获得整体科学认可，正确结果需回写后续稿/台账。

## Promotion or Rejection History

- 2026-11-08：从实际初稿错误重建相位/归一及宽度合同，保存可重放通道控制与来源边界。
