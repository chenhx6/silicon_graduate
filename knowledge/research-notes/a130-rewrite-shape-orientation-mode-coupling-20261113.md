---
type: research-note
title: "A130重写：gamma形状模与取向模耦合的微观机制与判据边界"
aliases: [shape-orientation-mode-coupling, gamma-wobbling-mixing]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "父根据已接受LaTeX正文与实际原件重建；旧稿仅留本地历史"
promotion_target: ""
evidence_sources: [prochniak-rohozinski-2009-bohr-collective-hamiltonian, matsuzaki-2004-nuclear-inertia-and-wobbling, kvasil-2006-dy156-yb162-crpa-wobbling, doctoral-r1-g37-oi-2001-wobbling-gamma-coupling, doctoral-r1-g37-bhat-2025-microscopic-wobbling-even-even]
tags: [doctoral-thesis, section-3-6, wobbling, gamma-vibration, mode-coupling, avoided-crossing]
---

# 形状与取向：耦合项、混合态和可观察检验

## Research Trigger

第3.6节要把耦合坐标谐振子、离散量子两态与真正微观响应分开，再问实核是否支持某个混合解释。
本页保存已核的量纲、相位及文献实现边界。

## Grounded Evidence

| 原件 | 选定定位及范围 |
|---|---|
| [[matsuzaki-2004-nuclear-inertia-and-wobbling]] | rawPDF3–6 Eqs.(1)、(5)–(12)、(19)–(24)：推转RPA、赝模因子及指定有效惯量与EM。 |
| [[kvasil-2006-dy156-yb162-crpa-wobbling]] | rawPDF1–4、16：Dy/Yb模型比较、带交叉附近的配对处方及高自旋EM。 |
| [[doctoral-r1-g37-oi-2001-wobbling-gamma-coupling]] | rawPDF2–3：选定164Hf的TAC-HFB与另设的一维示意量子化。 |
| [[doctoral-r1-g37-bhat-2025-microscopic-wobbling-even-even]] | rawPDF2–3、9：截断TPSM、形变/配对标定及EM解释，232Th为反例。 |
| [[prochniak-rohozinski-2009-bohr-collective-hamiltonian]] | 原综述的集体坐标、质量与响应框架；不是下列二振子参数的实核拟合输入。 |

原件与哈希回各source。本轮没有重跑上述微观计算，也未把作者引述的实验当成本轮新测量。

## Provisional Reasoning

声明无量纲局域坐标xi1、xi2及其共轭动量，取

$$H=\sum_i p_i^2/(2B_i)+\tfrac12C_1\xi_1^2+\tfrac12C_2\xi_2^2+C_{12}\xi_1\xi_2.$$

B量纲为能量乘时间平方，C量纲为能量。质量加权矩阵D=B^(-1/2)CB^(-1/2)
的本征值是omega²，量纲为时间负二次方。两质量正且C正定时，两支频率正：

$$\omega_\pm^2=\frac{\omega_1^2+\omega_2^2\pm\sqrt{(\omega_1^2-\omega_2^2)^2+4C_{12}^2/(B_1B_2)}}2.$$

零行列式仅说明二次恢复力在一方向为零，需高阶项；负行列式才有负曲率方向。
相等未耦合频率处的平方差是2|C12|/sqrt(B1B2)，不是离散态能量隙2V。
该常质量/刚度模型未含一般旋转体系的陀螺速度耦合。

另取相同I、宇称及相容离散标签的两正交态，重定相使V>=0，Delta=E1−E2。
定义theta=.5 atan2(2V,Delta)，使|+>=cos(theta)|1>+sin(theta)|2>、
|−>=−sin(theta)|1>+cos(theta)|2>覆盖全失谐支路。V=Delta=0不能定混合角。
固定V且失谐穿零才有最小能隙2V；V本身变化时要算完整曲线。

若到同一末态的两个E2 RME记为a、b，则

$$B_+=|\cos\theta\,a+\sin\theta\,b|^2/(2I_i+1).$$

干涉交叉项含Re(ab*)，可以增强、抵消或为零；相干叠加不要求二态覆盖整个Hilbert空间。
固定算符、相同初态自旋的这次幺正二态旋转，保留到固定末态的两个B之和；
将它推广成实核总强度守恒还要检查遗漏态和变化的算符。delta仍是辐射振幅比，不能改成裸RME比。

对物理J与角频率omega，定义动态J-omega响应chi(Omega;omega_rot)。
它有惯量量纲，但任一张量元不自动等于某一模式的有效横向标量惯量。
若全H转动不变，[H−omega_rot Jx,Jx]=0，而横向J±给频率omega_rot的运动学因子；
RPA实现需检查参考态、残余力、截断和赝模解耦。沿带d<Jx>/domega不是一般横向响应。

Oi文献的TAC-HFB空间未重现预期TSD形变，一维量子化另设边界/质量；不能写成TAC+GCM
或完整EM确证。原式a=Mw omega²/2之后的质量反解有因子2疑点，是本任务代数核查而非已证实验定论。
Kvasil模型对Dy/Yb分别讨论gamma软化与中子顺排，配对隙近交叉含唯象处方。
Bhat的六核比较有固定/拟合形变与调整配对，不是六核全都被实测确证为摆动。

## Assumptions

二振子是声明的局域模型；两态能量模型另有正交性、相位与固定算符条件。
微观RPA及投影结果只在各自实现和参数范围内使用。

## Competing Explanations

能级排斥和非谐性也可来自普通构型交叉、准粒子顺排或惯量变化。
波函数中间表象不直接等于实验轨迹，需要通过共同可观察预言比较。

## Transfer Conditions

能标接近可放大非零耦合的混合效应，但不接近不意味着耦合项为零。
迁移到另一核区需重新检验允许自由度、对称性、曲率与算符。

## Failure Conditions

忽略质量加权；把omega²当能量；把2V图当同一个二振子频率图；
无条件声称非零RME必有非零干涉；用沿带惯量直接替横向模式惯量；
将示意一维量子化冒作全微观质量/GCM或实测EM。

## Falsification or Reverse Tests

独立对角化声明模型核相位和强度和；用未调参的绝对EM与响应比较竞争实现。
父控制仅核两态和质量加权数学，未复现真实核波函数。

## Open Questions

哪些同输入模型与实际EM测量能区分形状-取向耦合与普通准粒子交叉？

## Human Review

本轮为智能体直接原件与数学自审，没有新增真实用户审核事件。

## Promotion or Rejection History

2026-11-13：父按已接受3.6重建，撤回旧稿错误的模型身份、闭合条件、量纲与普遍性表述。
