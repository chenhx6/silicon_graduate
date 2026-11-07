---
type: synthesis
title: "三轴集体模式的共同输入、局部稳定性与跨区迁移检验"
aliases: [三轴普适动力学与迁移总律, universal-triaxial-mechanics-and-migration, 跨区物理出现与禁戒根源]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
confidence: medium
scope: conditional-cross-region-mechanisms-and-evidence
sources: [frauendorf-2014-transverse-wobbling, book-bohr-mottelson-nuclear-structure-vol2, peng-2019-possible-chiral-doublets-60ni, guo-2024-chiral-wobbler-74br, timar-2019-transverse-wobbling-105pd, sensharma-2019-two-phonon-wobbling-135pr, hayes-2005-k-conservation-178hf, dracoulis-2013-192os-isomers-gamma-soft]
tags: [triaxiality, wobbling, chirality, cross-region-transfer, stability, evidence-boundaries]
---

# 三轴模式的共同输入与迁移检验

## Agent active summary

本页保留原路径以承接历史链接；2026-11-07撤回旧的区域“严格禁戒”、
刚性/手征充要条件、固定势垒阈值及错误摆动频率。
以下公式只在写明的Hamiltonian、单位和展开范围内使用。
六区原始证据见[[triaxial-collective-evolution-across-mass-regions]]，
本轮精确单j数值检验见[[seniority-mid-shell-cross-region-model-test-20261107]]。

## Question and Scope

### 纯转子、轴序与单位

取I为以ℏ为单位的无量纲角动量，A_k=ℏ²/(2𝒥_k)为能量，
\[
H=\sum_{k=s,m,l}A_k I_k^2.
\]
对最大惯量m轴附近的低能转动展开，A_m<A_s,A_l；高自旋谐近似给
\[
\hbar\omega_w\simeq2I\sqrt{(A_s-A_m)(A_l-A_m)}.
\]
这是纯转子局部频率，不是实际核中所有旁带的精确能差。
核子的阻塞、取向响应、有限I修正和惯量随频率变化均可能改变结果。
经典Euler稳定性还区分能量极小和极大附近的转动，不能只凭一个乘积为正
就认证某条核能带为yrast摆动。

## Synthesis

### 冻结对齐的条件化结果

指定一个固定j沿短轴s，Hamiltonian为
\[
H=A_s(I_s-j)^2+A_mI_m^2+A_lI_l^2.
\]
在I_s≈I、I_m/I,I_l/I很小且j不重排的展开中，二次恢复系数为
\[
c_m=A_m-A_s+A_sj/I,\qquad c_l=A_l-A_s+A_sj/I,
\]
\[
\hbar\omega_{\rm FA}\simeq2I\sqrt{c_mc_l}.
\]
所选分支为局部能量极小时须c_m,c_l>0。
在𝒥_m>𝒥_s且相应分支存在的条件下，c_m=0给
\[
I_c=j\frac{\mathcal J_m}{\mathcal J_m-\mathcal J_s}.
\]
这不是所有核的临界自旋，也不推出失稳后必为手征；
解冻准粒子、配对/组态交叉、其它局部极小或γ响应都可改变后续运动。
接近软模时小振幅展开本身最需要检验。

原始理论入口：[[frauendorf-2014-transverse-wobbling]]
PDF p.6 Eqs.(11–15),(23–24)，含J=√[I(I+1)]约定及谐近似失效讨论；
本页的I是对应的高自旋简化，不能默默混用两种自旋定义。
该来源也讨论163Lu横向摆动频率下降，故旧页的“Lu必上升”不成立。

## Counter-evidence

### 有利几何与量子证据

经典的非共面指标可写作
\[
\mathcal V=\mathbf j_1\cdot(\mathbf j_2\times\mathbf R).
\]
非零体积表示这组三矢量不共面；严格90°不是必需条件，
也不能对一般多准粒子态把它直接换成三个指定轴分量的简单乘积。
高j粒子—空穴加核芯是一个有利构型，并非所有手征的必要且充分组态。
奇A、偶偶多准粒子及跨壳激发必须按实际自由度分析。

精确对称本征态的带符号期望可以为零，即便模型存在左右取向分布。
因此需要方位概率、主轴分量、能量劈裂和伙伴分辨电磁网络的共同比较。
粒子标签、近简并或某个角度阈值单独不能认证静态手征。
60Ni模型是区域禁止论的直接理论反例；它的拟合与取向分布仍是模型结果，
未因此变成实验直接测得静态手征。

## Model Dependence

### 不同集体坐标与势垒

γ形状涨落、左右手征取向隧穿、正常/强形变态之间的衰变可能跨越不同的势垒。
一个TSD井的存在不提供另一个坐标的势垒高度，也不自动确定惯量。
比较前要固定组态、自旋/频率约束、能量零点、集体路径和动能度量。

若局部模型确为
\[
T_\gamma=p_\gamma^2/(2B_\gamma),\quad
V_\gamma=V_0+\tfrac12 C_\gamma(\gamma-\gamma_0)^2,
\]
且γ以弧度计，则
\[
E_{\rm ZPE}=\tfrac{\hbar}{2}\sqrt{C_\gamma/B_\gamma},\qquad
\sigma_\gamma^2=\frac{\hbar}{2\sqrt{B_\gamma C_\gamma}}.
\]
Bγ由所选集体动能定义，不存在脱离约定的通用Bγ=4Bβ²。
势垒相对ZPE可作局域化的启发指标，但多维势、质量变化、几何边界、组态耦合
和非谐性使它不是刚性/软性充要条件。大势垒也不令有限质量的σγ严格为零。
旧页的“1 MeV允许/300 keV禁止”“二声子600–800 keV必溶解”没有
逐态原件和共同Hamiltonian支持，已撤回。

## Evidence Matrix

### 共同输入与可推翻条件

| 研究机制 | 需要固定/记录的输入 | 原假设可被怎样推翻 |
|---|---|---|
| 摆动与单粒子进动 | 相同波函数、惯量轴序、配对/取向、E2/M1算符及混合比约定 | 同一组谱/强度由解冻单粒子或signature模型更好解释；或预测带外E2在已知灵敏度下缺失 |
| 手征与其它双带 | 组态对应、取向分布/隧穿、能级与伙伴矩阵元、同数据拟合依赖 | 非共面分布不能维持；其它组态/γ振动模型给出全部观测；必要连接被可靠排除 |
| 八极与手征联合 | 反射坐标、γ/取向惯量、宇称及E1/E3与同宇称M1/E2网络 | 仅三带或E1可由混合解释；β3极小与实际组态不对应；缺少关键宇称伙伴 |
| K/形状/自旋异能态 | 各支路能量、多极性、ICC、初末态组态与时间窗 | 长寿命只由低Eγ/高L解释；小fν来自末态Coriolis混合；没有独立形状证据 |
| seniority抑制 | 价核芯、n/空穴、j、对称性、同v或异v、一体/有效算符 | 占据非半满、态的粒子—空穴signature不同或模型空间改变；弱支路无法由同一算符再现 |

由此把“不会出现”限制为一个明确Hamiltonian或实验合同内的结论。
若只证明轴对称输入的模型不能产生非轴向模式，那是模型边界；
若没有完整搜索和响应上限，应该写本轮未覆盖或未建立，而不是物理上不存在。

## Limitations and Missing Evidence

### 有界L4与后续问题

精确单j计算显示，破坏纯配对不必破坏半满壳节点；
因此研究异能态与γ软性的联系时，不能把所有强度恢复归因于“seniority混合”。
192Os原始论文和Hayes博士论文还显示寿命/阻碍由多支路及两端波函数决定。
这些是下一步选择多观测量数据的依据。

P0：错误公式与没有原件支持的普适阈值已隔离，不以旧审核/模型通过记录恢复。
P1：真实核的共同输入、参数协方差、缺失信号的响应与原作者计算仍需逐项目恢复。
本页没有证明所有模式的互斥相图，没有给出全球未发现核素清单，
后续定量问题进入[[isomer-six-region-transfer-research]]的明确候选。

## Sources

- [[frauendorf-2014-transverse-wobbling]]
- [[book-bohr-mottelson-nuclear-structure-vol2]]
- [[peng-2019-possible-chiral-doublets-60ni]]
- [[guo-2024-chiral-wobbler-74br]]
- [[timar-2019-transverse-wobbling-105pd]]
- [[sensharma-2019-two-phonon-wobbling-135pr]]
- [[hayes-2005-k-conservation-178hf]]
- [[dracoulis-2013-192os-isomers-gamma-soft]]
