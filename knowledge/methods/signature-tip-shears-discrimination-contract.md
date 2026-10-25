---
type: method
title: 旋称伙伴、低自旋进动与磁转动剪刀态判别操作规范（Signature, TiP, and Shears Discrimination Contract）
aliases: [signature-tip-shears-contract, signature partner vs tip vs magnetic rotation protocol]
created: 2026-10-24
updated: 2026-10-25
status: ai-draft
review_status: unreviewed
method_type: experimental-and-theoretical-criteria-protocol
tags: [signature-partner, tilted-precession, magnetic-rotation, shears, discrimination-contract, a130]
---

# 旋称伙伴、TiP与剪刀态的证据比较

## Purpose

本页始于Day22的Day23无学分预习；Day23正式运行继续以它组织竞争解释及需要补测的观测量。课程学分只由该run收束时逐卡审核确定；本页不把135Pr争议预先判为TiP，也不把三种模型当互斥且覆盖所有可能。

## Inputs and Assumptions

输入须有来源限定的带身份、spin/parity、逐线强度/δ和可用响应。缺项标unknown，勿补零；a/Q、取向和模型坐标须明示。

## 逐项比较程序

| 步骤 | 记录内容 | 能约束什么 | 不能单独推出什么 |
|---|---|---|---|
| 带/组态身份 | 原实验带标签、Iπ、符合连接、signature、1qp/多qp模型输入 | 正确映射退激和候选组态 | 仅凭qp数不能确定剪刀机制 |
| 电磁分支 | 逐线δ的两支/误差、A或P及a/Q、同母态in/out分母 | 排除不相容的预测、检验E2和M1矩阵元 | M1主导不唯一指SP/TiP/磁转动，E2主导不唯一指wobbling |
| 能谱/对齐 | Ex、Ewob定义、ix同ω/同参考、J(2)、交叉与污染 | 对机制的spin演化提出约束 | Δix必须零或4–6ℏ、固定反弹能量不是通用硬门 |
| 寿命/几何 | 有τ时求绝对B及系统误差；以同组态模型计算j/R和磁矩 | 检验转动集体性、进动/叶片闭合解释 | 未测不作零；不能把i_x或模型图当直接测得三维j |
| 近似定义 | 说明harmonic phonon、完整非谐拓扑或其它耦合模式 | 区分近似失败与观测不支持 | f阈值、R/j、β或固定W.u.值不作跨核充要条件 |

## 135Pr控制样本

[[matta-2015-transverse-wobbling-135pr]] M15-D22-R095-1/2支持原作者的E2-rich/下降Ewob与完整QTR比较；[[lv-2022-evidence-against-wobbling-135pr]] L22-D22-R095-1–3给独立小δ及TiP重解释。[[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]] SH26-D22-R095-1对旧AD作条件χ²回应，并明确完整QTR不冻结j。三者不能按三次独立实验计票，也没有完成共同response重分析。

## 适用范围与撤回

旧本页把β、W.u.、δ、f、Q_t及M1交错的自设数值拼成“六模式排他硬规则”，没有足够原件或普适推导；checkpoint095整体撤回该规则及未复核的137Pr/108In“黄金”数字。原文封存在pre-correction-095.json，相关独立source事实需各自核对后再用。剪刀解释需考察质子/中子矢量及B(M1)的spin演化，不能由弱E2或某条小δ直接宣布。后续新增数据仍可能改变模式排序。

全部新增推断needs_review: true。本页是证据清单，不给实验最终认证。

## What It Can Establish

识别观测量、带身份和模型输入是否支持各候选解释，并提出能区分预测的补测；可定位跨线、跨阵列及跨数据错误。

## What It Cannot Establish Alone

不能由检查清单唯一识别模式，也不替代完整实验响应、绝对尺度或多体模型；不能根据本预习授Day23正式学分。

## Sources

- [[matta-2015-transverse-wobbling-135pr]] M15-D22-R095-1/2。
- [[lv-2022-evidence-against-wobbling-135pr]] L22-D22-R095-1/2/3。
- [[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]] SH26-D22-R095-1。
- [[frauendorf-2014-transverse-wobbling]] F14-D22-R091-1。
- [[chen-2022-study-wobbling-spin-coherent-state-maps]] CF22-D22-R093-1。

## Day22 checkpoint098：Day23无学分预习的独立磁转动对照

| 对照 | 原实验约束 | 解释与限制 |
|---|---|---|
| 137Pr，AG07-D22-R098-1/2 | INGA DCO/IPDCO与弱E2支路；给B(M1)/B(E2)，无τ | 比值先升后降；TAC提出3qp/5qp交叉与叶片重开。43/2打印强度重建不闭合，保留逐门输入缺口 |
| 108In，CHI01-D22-R098-1/2 | 另一核/阵列的DSAM与branch/ICC给绝对B(M1)，含对齐处回升 | 约3.05是18+/19+打印中央比，不是新联合CI；stopping系统量未含在原误差中 |

两条独立实验链提高的是“相对比/绝对强度/组态演化”辨别能力，不能把108In寿命迁入137Pr，或把一条小δ直接标成磁转动。原子出处见[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]] AG07-D22-R098-1/2与[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-D22-R098-1/2。needs_review: true；Day23仍无学分。


## Day23 同线观测向量与响应合同

本节为本任务方法推断，needs_review: true。逐行保留原实验身份，不能先把各装置输出压成同一个δ再比较“模式”。

| 线与来源 | 实验输入/派生输出 | 响应与输入缺口 | 可比较范围 |
|---|---|---|---|
| Pr747.3/813.2/450.2，Lv2022 | P分别+.04/−.03/−.07，δ分别−.47/−.37/−.31；SI另报Ap，同采集 | 本文a、外借Herzan Q；四角组合Rac、逐线gates，完整Cov/原峰面积缺 | 先对齐同一母末态和A/P定义；不能把主文P与SI Ap当两个偏振测量 |
| Pr747.0/812.8，Matta2015 | A=.047(.012)/.054(.034)，δ−1.24(.13)/−1.54(.09)；AD与polarization来自不同装置 | 未在本任务取得原INGA完整Q/Σ；原角分布response/Σ缺 | A不能未经Q校正与Lv P逐值相减；旧AD被重分析不产生新事件 |
| Pr746.3/811.6/754.2，SH26 Fig12 | 延续旧AD谱系的σ/I=.2条件χ²偏好大模解 | 旧计数/完整likelihood未重放；新报告DB观测仍在共享/合并数据谱系内 | 保留条件支持，不能声称自由σ/I时两谷必等深；新DB观测不自动等于新测三条低带P |
| Au376/462，Guo2022 | 新P–Rac联合δ−.26(+.11/−.15)/−.28(+.23/−.69) | 自有a、外借Zheng Q；154°/90°、all-angle gates；462有选门上/下界 | 和Sensharma同线比较前须对齐模型/响应；Fig3(c,d)的αK由本δ换算，不是新转换谱 |
| Au376.3/461.8，Sensharma2020 | 17环AD给δ−2.67/−2.98；未报告这两条P | 两次采集合并；共同效率/取向/完整Cov缺 | 这是独立于HIRFL的实验链；E2 fraction与相对强度复用所选δ |

原子出处：[[lv-2022-evidence-against-wobbling-135pr]] L22-D22-R095-1、L22-17、L22-19；[[matta-2015-transverse-wobbling-135pr]] M15-D22-R095-1；[[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]] SH26-D22-R095-1、SH26-11、SH26-15；[[guo-2022-low-spin-wobbling-187au]] GU22-D23-001、GU22-D23-002、GU22-D23-003；[[sensharma-2020-longitudinal-wobbling-187au]] AU20-1、AU20-4。

### 同源派生强度的秩约束

以已校正效率的光子分支q=Iγ,out/Iγ,in、纯E2带内分母及MeV能量为条件，记K=q(Ein/Eout)^5、c=.697 Eout²，则

$$r_{E2}=K\frac{\delta^2}{1+\delta^2},\qquad
r_{M1}=cK\frac{1}{1+\delta^2},\qquad
c\,r_{E2}-\delta^2r_{M1}=0.$$

本任务据[[lv-2022-evidence-against-wobbling-135pr]] L22-D22-002及L22-D22-R095-2的813.2/726.0共同母态、6.4/3.7强度和δ−.37，得到rE2=.11812877、rM1=.39772213（μN²/e²b²）；与原表.12/.4的印刷舍入相符。系数.697是声明的单位约定；先前记录的.39785为近似重算差异，不能据差异报物理效应。

向量(δ,rE2,rM1)对(δ,K)的Jacobian秩为2，其约束法向量(−2δrM1,c,−δ²)消去Jacobian。三个汇总量包含额外的分支信息K，但rE2和rM1不能被当作在δ和K之外新增的两项独立测量。若构建局部线性误差传播，其Cov有相应零方向；这不是关于非线性样本Cov必奇异的普遍定理，更不宣称实际事件likelihood只有两维。变δ符号不变两项率，故率本身不给符号。τ在同母态相对比中相消；未测τ不能补出绝对B。

可复现实现为`system/scripts/day23_strength_dependency_rank.py`，以有限差分、约束法向量、变号、零M1/E2极限与强度缩放检查公式；不是原实验producer或CI重放。

## Day23 保持计数的组态替代解释与留出检验

冻结实验层D：逐线峰计数/背景、门、效率和响应、自旋宇称、能级与连接均不变。只把Au Band2从同πh9/2组态上的nω=1解释，换成QTR中以第二低h9/2来源轨道#21为主的态（Band1以#19为主）。这是[[guo-2022-low-spin-wobbling-187au]] G22-20的模型归属作为替代假说；**不把伴随SP带改归188Pt**，因为后者改变核素/谱线身份，超出“只改configuration”练习。也不把Sensharma的大δ偷偷换成Guo的小δ；两实验分支冲突仍独立保留。

只更换文字标签不会产生可证伪性。必须固定两套候选Hamiltonian、形变/惯量/配对、算符/effective charges/g及模型误差，再计算未参与调参的量。可证伪问题是：当已用于定标的能量、参考B(E2)与所选分支保持固定时，两种组态归属对同一母态完整退激向量与绝对E2/M1尺度，能否给出在共同响应/不确定度下可分离的预测？

| 检验量 | 必要伴随观测/输入 | 判决边界 |
|---|---|---|
| 逐态τ与完整光子分支、ICC→绝对B(E2)/B(M1) | 同一parent、τ定义、feeding/stopping或timing response、相对/绝对归一、共同Cov | 外借100–200 W.u.本来已参与尺度设定时不能再算独立留出检验；当前未算模型预测差或实验功效 |
| 未用于定标的同母态出口比/跨带矩阵元 | 两出口均测δ及门/污染；模型预先指定目标出口 | 若出口已被拟合，必须另选holdout；不能把由原δ派生的两比值重复计票 |
| 静态g、Qs或轨道选择敏感的转移强度 | 目标态身份、核反应/矩阵元模型及响应；两候选明确数值区间 | 单j极限g_j对同j各轨道未必不同，不能承诺一次g就排他；Qs也需模型可分预测 |

这些是任务设计与缺口，不是新实验结果。Guo的QTR已有数据比较，而一个形式上可写的重指派未获得同等拟合与留出表现，不能按“都可解释”给相同可信度。目前真实计数、共同response/Cov与固定模型producer不齐，L4不ready；继续L2/L3原件和输入调查，不制造δ、Q(E)、τ或机时。
