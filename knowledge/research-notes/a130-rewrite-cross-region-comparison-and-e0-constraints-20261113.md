---
type: research-note
title: "A130重写研学：跨区比较、二态E0约束与观测量身份"
aliases: [cross-region comparison and two-state E0 constraints]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "第四章写作中的原件回读与二态代数核查"
promotion_target: ""
evidence_sources: [doctoral-r1-g26-crider-2016-68ni-shape-coexistence, doctoral-r1-g27-clement-2007-prc-krypton-coulex, continuation-g17-chen-singh-2020-nds-98mo, karmakar-2025-2026-98mo-octupole-preview, saracino-2026-102ru-scissors-octupole-resonances, poves-2020-limits-assigning-nuclear-shape]
tags: [A130, cross-region, shape-coexistence, E0, inverse-problem, evidence]
---

# 比较之前先固定态、算符与所比较的量

## Research Trigger

六区比较写作需要把模型条件与原表数据连起来。混合角相位、E0电荷归一、
半衰期与平均寿命、相对强度与绝对强度若混用，会产生表面合理却不成立的跨区类比。
本页保存可复用的代数和辨别方法。

## Grounded Evidence

| 原件入口与本轮定位 | 实际可支持的范围 |
|---|---|
| [[doctoral-r1-g26-crider-2016-68ni-shape-coexistence]]，所持PDF2、4及Table 1 | 区分本次寿命、采用分支、E0上限与限定二态模型；不将形状指认当作直接密度成像 |
| [[doctoral-r1-g27-clement-2007-prc-krypton-coulex]]，PDF11 Table VI、15 Table XI | 所选Kr态的带符号矩；角动量态和实验列不能替换成基态形状标签 |
| [[continuation-g17-chen-singh-2020-nds-98mo]]，归档adopted PDF2 | 734.75(4)keV的0₂半衰期21.8(9)ns与787.384(17)keV的2₁半衰期3.47(7)ps分别登记 |
| [[karmakar-2025-2026-98mo-octupole-preview]]，实际8页出版PDF4 Table 1、6–7 Tables 2/3 | 弱线多极性证据、相同母态分支和B(E3)/B(E2)；basename中的preview不代表当前只有预览 |
| [[saracino-2026-102ru-scissors-octupole-resonances]]，出版PDF3、5、6 | 偶极强度的态与积分区间，以及作者的双声子、偶极—八极混合解释；NRF偶极观测不等于直接测E3静态矩 |
| [[poves-2020-limits-assigning-nuclear-shape]]及[[a130-rewrite-invariant-recoupling-and-width-boundaries-20261108]] | 有限低阶矩对形状反演的限制；不能从一个有效角恢复完整概率分布 |

各原件路径与SHA回各source；本次没有重拟CoulEx产额、NRF原始事件或作者全部理论曲线。
同一实验的论文、学位论文、评价采用量不能作为独立重复测量计数。

## Provisional Reasoning

### 原表列与采用量的增量核查

本轮直接回读Crider2016的PDF4 Table 1及模型比较段：
68Ni的0₃半衰期为0.57(5)ns；到0₁、0₂的E0强度上限分别是
$\rho^2<0.0050$和$<0.0258$，不能错写为已测强度或随意换成另一个
$10^{-3}$刻度。作者将0₁、0₂、0₃分别与球形、扁椭、长椭模型构型联系；
A3DA与LNPS的0₃半衰期预言约108ns、1.5ns，仍须与实测值区分。

Starosta2007的PDF3 Table I也须逐列读取：64Ge的$Q(2_1^+)$为
GXPF1A计算栏的$-18.6\,e\,\mathrm{fm}^2$，不是实测静矩，也不是未经来源核实的
$-0.13\,e\,\mathrm b$。寿命与分支导出的实验B(E2)在另一列。

Thomas2016的完整出版XML元素`ce:table id="tl0020"`（Table 2）给出了采用量标记：
双星号表示取自NDS；强度栏横线表示该次实验因灵敏度或本底而未观测。
52.6keV支路有这些标记，不能把表列采用量再计为该次反应的独立新观测。
这些核查没有重拟任何原始事件。

### 二态混合的相位与简并端点

以下是声明条件的教学重构。取正交基底和实对称矩阵
$$
H=\begin{pmatrix}E_A&V\\V&E_B\end{pmatrix},\qquad
|1\rangle=\cos\theta|A\rangle+\sin\theta|B\rangle,\quad
|2\rangle=-\sin\theta|A\rangle+\cos\theta|B\rangle .
$$
消去非对角项要求
$$
\tfrac12(E_B-E_A)\sin2\theta+V\cos2\theta=0.
$$
因此在非零分母处，$\tan2\theta=-2V/(E_B-E_A)$。
对$E_A<E_B,V>0$取$-\pi/4<\theta<0$；相等对角能量且$V>0$时取连续极限$-\pi/4$。
完全简并的$E_A=E_B,V=0$不能由这个哈密顿量固定混合角。

观测能隙为$\sqrt{(E_B-E_A)^2+4V^2}$，只给一个组合约束。
混合由相对能隙决定；绝对值很小的$V$也可在更小的未扰动能隙下产生强混合。

### E0的电荷因子与未混合矩阵元

取相对质心的点质子坐标，$T(E0)=e\sum_p r_p^2$；
每质子平均均方半径为$\langle r^2\rangle_{A/B}=Z^{-1}\langle A/B|\sum_p r_p^2|A/B\rangle$。
再假设基底中的非对角E0矩阵元可忽略，才有
$$
\langle2|T(E0)|1\rangle=eZ\sin\theta\cos\theta
(\langle r^2\rangle_B-\langle r^2\rangle_A),
$$
$$
\rho^2(E0)=\frac{Z^2}{4}\sin^22\theta\,
\frac{(\Delta\langle r^2\rangle)^2}{R_0^4}.
$$
正交性本身不保证非对角E0为零。强度约束的是乘积，不能分别唯一给出混合角与半径差。
同位素位移比较的是不同核的半径期望值，也不能直接替代同核E0跃迁矩阵元。

### 量的身份与前向模型

静四极矩$Q_s(2^+)$属于指定实验室态；把它映射为轴向内禀$Q_0$需要额外转子条件。
0⁺一阶矩、二阶不变量、带间强度与形成截面分别约束不同对象。
NRF中的E1聚集、八极模型解释与高自旋宇称连接网络也须分开。

质量数和$\Omega$标签可提供轨道线索，具体形变驱动仍须结合占据、
粒子/空穴参考、相互作用和核芯响应。有效参数能否迁移应逐模型检验，
不能把它们一律当作普适常数，也不能宣布一律不可迁移。

## Assumptions

二态模型使用正交基底、实$V$与指定相位；E0简式另忽略基底非对角矩阵元。
原表数据使用各自版本、态与积分区间；拟合输出及模型解释分别标记。

## Competing Explanations

低能0⁺、相近能谱或强E0可在不同混合与连续分布描述中出现。
区分能力取决于联合预言和误差，不存在对所有核通用的“能量最低、E0最高”信息量排名。

## Transfer Conditions

角动量代数、量纲核验和证据身份可跨区使用；轨道占据、有效电荷、
反应布居与势能/惯量输入需在新体系中检查。实际完整原件优先于早期获取失败记录。

## Failure Conditions

相位不一致；E0遗漏$e$或$Z$；将半衰期换成平均寿命却不除$\ln2$；
从单一低阶矩宣布完整势面；把不同强度积分区间相加；把1页预览写作PDF第12页。

## Falsification or Reverse Tests

由实际矩阵验算二态非对角项为零，检查两态正交与完全简并端点；
核对能级顺序是否允许所写向下退激；逐项核文件页数、原表列、单位和误差身份。
若某数值不能完成这些检查，应撤下该数值，而非补一条想象的定位符。

## Open Questions

给定有限E2/E0网络，还需要何种独立测量最能区分离散混合与连续软性？
98Mo的相对E3/E2增强在获得寿命后会如何分解为分子、分母的改变？

## Human Review

本轮为智能体对原件和代数的自审，未发生真实用户审核事件。

## Promotion or Rejection History

2026-11-13：保留可复用条件与原件入口；不作全核区形状定论或新发现优先权声明。
