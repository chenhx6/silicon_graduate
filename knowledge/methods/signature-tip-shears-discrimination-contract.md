---
type: method
title: 旋称伙伴、低自旋进动与磁转动剪刀态判别操作规范（Signature, TiP, and Shears Discrimination Contract）
aliases: [signature-tip-shears-contract, signature partner vs tip vs magnetic rotation protocol]
created: 2026-10-24
updated: 2026-10-26
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
| Pr746.3/811.6/754.2，SH26 Fig12 | 延续旧AD谱系的σ/I=.2条件χ²偏好大模解 | S19与新63Ge run合并；Fig12具体事件组成仍缺ledger；共同likelihood未重放 | 保留条件支持，不能声称自由σ/I时两谷必等深；新DB观测不自动等于新测三条低带P |
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


## Day23 外借Q的能量共同误差与迁移边界

本节是声明条件的任务推导，needs_review: true。Zheng2013的Q校准用90° EXOGAM、316–1264keV的pureE2参考（[[zheng-2013-linear-polarization-91ru]] Z13-1、Z13-2、Z13-7）；Herzáň2015用75.5°/104.5° JUROGAM-II及stretched M1/E2（[[herzan-2015-193bi-spectroscopy]] HE15-D23-1）。Guo2022承认自身因isomer布居而难以定Q，借前者同型detector曲线；Lv2022借后者，但各自测a。因此a≈1不等于Q≈1，也不认证所有target/reference acceptance相同。

将来源印刷参数代入Q(E)=Qpoint(E)(p0+p1E)，m_ec²=511keV，得到以下**来源曲线中央值**。它们不是target重标定，且不能把两曲线当可互换的“高/低Q情景”。

| 所采用曲线/目标能量keV | Q曲线值 | 仅p0/p1印刷marginals与未知ρ下的一阶σQ范围 |
|---|---|---|
| Zheng2013，Au376 | .314472 | .006647–.023843 |
| Zheng2013，Au462 | .292257 | .004296–.023690 |
| Herzáň2015，Pr450.2 | .236763 | .006007–.050624 |
| Herzáň2015，Pr747.3 | .148787 | .006589–.049403 |
| Herzáň2015，Pr813.2 | .134271 | .008559–.049019 |

条件是印刷σ为可比较marginal标准差。固定能量时σQ=Qpoint sqrt(σ0²+E²σ1²+2Eρσ0σ1)，ρ∈[−1,1]，范围端点为Qpoint|σ0−Eσ1|与Qpoint(σ0+Eσ1)。这不是重拟合/CI，也没有覆盖从reference到target的transfer κ(E)、selection或取向不确定度；不将端点指定为真实Q误差。

共同曲线给跨线Cov：X_i=(1,E_i)、J_i=Qpoint_i X_i时，C_Q=J C_p Jᵀ。忽略reference/target交叉项、且暂假定target A与外部参数独立时，P=A/Q的一阶C_P包含D_(1/Q) C_A D_(1/Q)以及H C_p Hᵀ，其中H_i=−P_i X_i/(p0+p1E_i)。每条线单独抽一个独立Q误差会丢失这项跨线结构；但真实C_p和target C_A仍缺，不能把该公式冒充已恢复Cov。

同曲线的形状比中共同尺度可相消：本曲线Q376/Q462=1.076013，σ[ln(Q376/Q462)]在上述ρ自由合同下为.005240–.006437；Q747.3/Q813.2=1.108109，对应.019464–.033035。两者只说明相邻能量的源曲线形状与绝对归一误差不同；若κ(E)有未知能量依赖，或target两条线的选样权重不同，该抵消不再充分。没有计算P跨线比，因为其实验误差/分母零域与共同Cov尚未处理。

最小transfer合同写Q_target(E)=κ(E)Q_reference(E)，κ必须由matching参考线、响应模拟或实际校准证据约束，不能自行设为精确1。正的共同κ改变P幅度而不翻A/Q符号；但a、背景和取向尚可影响实际符号/模型P，故不从这个代数事实判定哪条δ分支已排除。尤其**P不是脱离取向的跃迁本征属性**：即使两实验Q都正确，同核同线的P仍因初态布居/feeding/门而不同，应分别用各自response约束共同δ，不能直接P相减。

可复现计算`system/scripts/day23_polarization_calibration_transfer.py`保留原参数、目标能量、完整两参数有限差分、PSD协方差范围、rank≤2与共同尺度抵消控制；不是实验producer。Z13-9/10/13已有原表误差/拟合/1368点边界继续有效，本节未用新的假独立拟合替代来源。

### 组态重指派与换模型的区别

只冻结实测D而改解释标签是可构造的替代解释；Guo与Sensharma两个发表模型还改变了形变、惯量与模型空间，不能称为只改configuration的受控数值实验。[[sensharma-2020-longitudinal-wobbling-187au]] AU20-D23-1表明其PRM β输入已参考旧绝对E2，[[guo-2022-low-spin-wobbling-187au]] G22-10/G22-20则用不同γ、Harris惯量和多轨道QTR。若要隔离configuration作用，须预先固定H/算符/拟合集，再把同一实验带分别映射到候选本征态并检查能量残差与holdout；当前producer不足，尚未执行这一受控对比。

同样，Band2在QTR中#21主导、Band1#19主导的“single-particle excitation”不自动等于“同一内禀轨道的两个signature partners”；两条带的交错自旋/旋称标签可兼容多种微观归属。保持它们作为竞争解释，不把SP、TiP和磁转动合成一个小δ类别。


## Day23 已发表的计数不变组态交换：110In的对照练习

[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-D23-1提供比纯换标签更具体的例子：保持bands8/9全部γ计数、能量和符合网络，交换BEF/EFG组态。原parities只是tentative，因此这是解释层变化，不篡改已独立确定的Jπ。交换更合alignment，却不合Routhian相对次序与3↔8 crosstalk；同一组态假说必须一起面对这些量。它不是本任务已做的独立拟合/先验留出试验，更不能由形式可行给两方案等可信度。

一个**新增可检验预测**来自两组态的相反parity：若原Band3 parity及748.4-keV连接/spin路径成立，BEF→原Band8与EFG→交换Band8对其相对parity不同，因而预期8→3允许的电磁多极族不同（同parity的M1/E2对异parity的E1/M2等）。原TableIV的748.4是(18+)→(17+)、M1/E2、两RDCO栏空白，薄/衬相对强度1.0(.1)/.2(.1)；不把标签当实测parity，也不把不同靶强度解释成两次独立测同一branch。

必要伴随观测是该线干净gates/污染、独立spin路径、联合AD/角关联与偏振、匹配a/Q/取向和可用的转换约束。正偏振不能单独排除E2-rich M1/E2，DCO也不能单独分E1/M1；须按候选多极组合比较完整响应。实际强线门/效率、净计数、背景、Q/Σ与模型transition operators尚未齐备，当前不报可行性功效、δ、τ或机时。若最终发现parity与原指派相反，将针对性降低原组态解释；若相同，则限制交换方案。其它orbital mixing/shape alternatives仍须另检验。

这是MR/弱带组态辨别的独立案例，只迁移“冻结实验D、列相反预测与检验已用量”的方法，不用110In结果代替135Pr/187Au逐线证据。实际剪刀角定义、configuration crossing前后的M1趋势见[[shears-mechanism]]及[[clark-2000-shears-mechanism]] CL00-D23-001/002；全部新增推断needs_review:true。


### 五类术语的逻辑层级

| 名称 | 首先是什么 | 需要的组合证据/条件 |
|---|---|---|
| signature partner | 同组态的旋称分支关系 | signature/self-consistent组态、spin对应、staggering与电磁连接；不同于pseudospin伙伴 |
| wobbling | 进动/量子激发的动力学解释；harmonic与完整拓扑分层 | 明确模式定义、同态电磁矩阵元与模型几何；不以统一δ或W.u.硬门命名 |
| TiP | 特定3D QTR/进动框架及重定向解释 | 共同输入下的角动量分布/能谱/电磁量；一条M1占优不足 |
| magnetic rotation | 指定粒子/空穴叶片及磁矩产生spin的机制解释 | absolute M1与E2、组态演化和core贡献；crossing前后分段，开角不直接测得 |
| antimagnetic rotation | 理想双剪刀横向磁矩抵消的机制图像 | 同spin窗口的寿命/E2/J2与组态；弱E2/无shift不是单独证明 |

这些不是一套互斥且穷尽的标签：旋称是分类关系，动力学近似和角动量生成机制是不同层次。原框架/本任务比较依据[[clark-2000-shears-mechanism]] CL00-D23-001/002、[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-17/19与CHI01-D23-1、[[lv-2022-evidence-against-wobbling-135pr]] L22-13/15及[[signature-partner-bands]]的定义。新综合均needs_review:true，无跨核最终模式认证。


## Day23：采集、观测与解释的三层依赖

“独立/同源”须说明是哪一层。[[sensharma-2019-two-phonon-wobbling-135pr]] S19-D23-1/2提供一个实物例：新增DGS采集既有自身TW2观测，也在Fig3继承Matta2015 TW1点；[[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]] SH26-D23-1/2又把该DGS样本和新63Ge run合并。不能把同一旧点加三次权重，也不能把真正新增run说成完全没有信息。n_w层级和模型参数还继承旧解释；这项逻辑依赖不同于events是否重叠。

SH26 Fig12是固定σ/I=.2的条件支持；其caption旧refs与SecII combined-data程序之间，仍缺逐图event/run ledger。当前不宣布该图逐event等于2015，也不宣布它没有新run贡献。若将来获得分run独立likelihood，可先以独立run数据项相乘，再对共享calibration、取向/feeding与模型参数统一处理；不能把合并后再发表的δ或强度点当作第三个独立因子。

## Day23：Au187官方export的逐线身份合同

外部field原子记录见[[guo-2022-low-spin-wobbling-187au]] GU22-D23-006/007/008；CSV暂存读取，正式raw归档deferred。本节仅为可复用的读取/比较规范，needs_review:true。

| 检查对象 | 本次实际输入 | 能/不能作为何种证据 |
|---|---|---|
| 时间版本 | Extraction_date2026-10-25；publication cut-off2008-11-01；guide指ENSDF April2022 snapshot | 读到文件不等于评价已覆盖2020/2022争议 |
| 376/462绑定 | 同snapshot gammas(16,2,2)/(38,10,3)，按z/n/symbol和start/end idx连levels | 相同能量还须有相同母末态；idx只有本snapshot内意义 |
| conversion字段 | tot_conv_coeff .147/.064；无αK栏、无逐条原reference notes | 不替代Guo Fig3 αK测量、不新增独立conversion采集；未认证字段是直接测量还是采用值计算 |
| mixing_ratio字段 | .6/1.1及unc_mr .3/.3为export字符串 | 缺原adopted notes/phase convention，不认证正物理δ、不补本任务δ，也不拟合两实验谁对 |
| 近能量436.6 | (13/2−)→(13/2−)，不是SP的ΔI1支路 | 不能仅以ΔE小把它与436.5合并或据旧库缺条目否定新序列 |
| parentτ/不确定度 | 母态16/38 half_life空；unc_hl标题重复两次 | 不填0、不用end-level9/2异构态2.3s代母态；按字段位置/单位保留两个unc_hl |

`system/scripts/day23_au187_api_identity.py`保留原字符串、重复列位置及snapshot SHA，6项join/空值/错线控制通过。一个全空终止record被识别为CSV格式尾行，非零counts或数据缺失。它不重放原spectroscopy producer、alphaK拟合、τ或实验Cov。


## Day23：母核衰变导出与样本总数的边界

[[guo-2022-low-spin-wobbling-187au]] GU22-D23-009–011确认187Hg→187Au export：parent shift/jp须和p_energy合读，两母态同为0字符串不代表同一state；γ初态τ与Hg母态144s及Au终态2.3s不能互换。γ列的intensity全部空白，electron body0是有效请求无数据的服务码，不能作为转换未观察/零强度、upperlimit或机时输入。v0/v1本次γ行multiset相同而等能条目顺序不同；需按完整身份和重复行比较，不用顺序zip或γ能量单键丢项。

这条路线提供了可复核的母核/字段合同，却没有恢复历史αK测量或其uncertainty/原notes；API现在可读不等于L4全部输入ready。full CSV仍临时staging，raw保护不变。扩展identity脚本原6+新6项检查只覆盖给定snapshot对象/字段，不认证物理模式或原实验。

[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-D23-1/2还提示：论文说“合并events”须配科学run号、版本、event selection、ring/eff/live-time weights。thesis Pr1.52e10与SH26 2.5e10无法仅从正文闭合，不能倒减得新增run精确exposure；即使总events一致，也不等目标peak、P散射选样或同一likelihood。Au4.4e8/6.3e8与Letter1.08e9为舍入报告，不据小差判未记录采集。

模型输入也按来源版本冻结：SE21-D23-3/4给Au reference-core B(E2)文字/数值与j几何边界。1.44/.84尚未核同一评价和采用约定前不平均、不默选、不改变负parity；λ同值也不替代完整sp谱/occupancy/EM operators。下一步优先核186Pt原evaluation或两模型实际operator，而不是靠增减任意参数制造匹配。


## Day23：186Pt参考尺度的条件重算与历史边界

checkpoint006把现代评价一致性写成“完全证实旧引用”的认证，范围过强，已撤回；旧文字/程序快照见本run pre-correction-006.json，旧七项数值flag不是独立物理验证。本节为Codex self-audit，needs_review:true。

| 对象 | 公开API字段/时间窗 | 条件rate重算 e²b² | 表列WU换算 e²b² |
|---|---|---|---|
| 186Pt191.53keV，2+→0+ | T1/2=240ps，αtot=.417；cutoff2022-03-01；b_e2=102 W.u. | .645283 | 约.64333 |
| 187Au233.4keV，(13/2−)→9/2(−) | T1/2=56ps，αtot=.224；cutoff2008-11-01；b_e2=188 W.u. | 1.191357 | 约1.19426 |

使用声明的公式B(E2)=.0816 ln2/[E(MeV)^5 T1/2(ps)(1+αtot)]，并假定唯一列明的E2/CE分支耗尽该level退激；relative intensity100本身不证明无漏枝。Weisskopf定义使用r0=1.2fm与B_W(E2)=(1/4π)(3/5)²R⁴，以1b²=10^4fm⁴换单位。差约千分之几，只是舍入/公式约定下的中央算术相容，不是原producer精确重放；b_e2与τ/α本就来自同一评价链，不能当两份独立测量。

没有恢复原始不确定度/完整Cov及转换系数误差，不将只变半衰期得到的区间称原实验CI或完整误差。现代Pt cutoff2022导出不能证明Baglin2003的实际采用值，也不能单凭两个中央值“完全核实”Guo2022宽泛100–200W.u.引述；当前只能说现代表列102/188在该数字范围内，原引用链仍需核。

[[sensharma-2020-longitudinal-wobbling-187au]] AU20-D23-2和[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-D23-3确实记录两来源引用数字.84/1.44，比例1.714；**两文β输入却同为.23**，不能把引用文字差称作实际β/producer输入改变1.71倍或其已证实误差。Thesis正parity字面亦不用于重指派实际h9/2分支。

当前程序`system/scripts/day23_core_reference_b_e2_audit.py`改为从实际CSV读取四份输入、保留重复列/数据hash并检查目标身份与时钟单位；输出status=computed-conditional，不再用硬编码结果的passed认证旧文献或原实验。输出core-reference-conditional-007.json保存假设与误差边界。


## Day23：同输入模型比较前的基底与转子组件门

依据[[streck-2018-behavior-collective-rotor-wobbling]] ST18-D23-001/002/003，先限定对象为固定I/j的D2 PRM基底和Hcoll=ΣRk²/(2Jk)，不是完整H_intr或E2/M1拟合。角动量用ℏ、惯量用ℏ²/MeV、Hcoll为MeV；输入s/i/l惯量13/21/4取原SecIII，C/配对/算符不设默认假值。

本任务`system/scripts/day23_prm_basis_rotor.py`独立构造两路Hcoll：一路用Eq11的K↔R变换及各R的D2转子block，另一路在body-fixed total I（反常commutator）×单粒子j空间构造(I−j)²再投影Eq6基底。I=11/2、13/2、17/2、25/2以及两个j1/2小极限共6域，矩阵两路最大差约9.1e−15MeV；正交误差≤6.7e−16，球形惯量相等极限R(R+1)/(2J)回到解析值，合计22项CG/正交/两路/极限/概率控制通过。它们只验证原source的数学组件和本实现的范围，不证明完整PRM核态或实验归属。

I=13/2、j=11/2的合法两基底均42维，其中15个weakbasis分量属于oddR≥3，R1没有。若未经轴对称条件擅去全部oddR，仅剩27维；对明示的strong基底态K=−7/2、Ω=−11/2会丢掉1/2归一。这个chosen基底态不是某个135Pr实测/原H本征态。另chosen两个R2分量的相干叠加只给两处各1/2概率，若误用概率非相干乘积则向其它分量分散，L1差约1.642；只是Eq20的相干控制，不作核素模式判据。

因此组态重指派需同时冻结物理空间、归一/phase、轴和operators。把K/R/RMS、signature、phonon数或图形标签直接互换会改变模型问题；在C数值/配对/EMoperators未齐时，正确的基底门也不能让完整same-H benchmark变成ready。Ref33最初只有metadata，随后期刊公开PDF成功取得并实际读4页；ST18-D23-005记录旧Eq3/新Eq11、N与MeV定义。公式可读解除一个输入缺口，但原作者实际处方/实现、pairing与完整EMoperator还须分开确认，不用熟悉公式默补。新增needs_review:true；模型谱/几何解释与真实电磁数据保留分层。


下一有界模型路线可以在明确标注“ST18无配对H + Wang2009 Eq11处方”的任务variant下实现H_intr与有限D2空间对角化，保留原数据D和全部输入，不用拟合/调参取得某标签。预先比较的是不同候选本征态的R分布、j²分量和〈I·j〉/I(I+1)这一静态g的几何系数；真实g还需gj/gR与多轨道/算符校准，不承诺该量一定可分。完整E2/M1强度/模式判决仍不能从组件检查推出。该路线是本任务模型实验，不冒充author producer或新核态/新实验CI。


## Day23：固定Hamiltonian与不改计数的候选态mapping

沿[[streck-2018-behavior-collective-rotor-wobbling]] ST18-D23-006，指定无pairing single-j particle+、A135/N5/j11/2/β.17/γ−26、(s,i,l)惯量13/21/4、Wang Eq11的C=.233738451MeV；所有参数冻结，不为某一标签fit。完整D2有限空间（I11/2–37/2）对角化，先按能量ordinal0/1/2记录，**不自动称SP、TiP或wobbling**。这是本任务近似模型variant，不是Lv多轨道QTR/Au模型或原作者code复现，亦不实现所有多qp组态重指派。

两路basis谱及矩阵残差、零C/Hcoll R²守恒、intrinsic D2闭合、Hermiticity、norm、energy decomposition和j²/Casimir共87项控制通过（max eigen residual7.2e−14MeV，D2leak2.3e−16MeV，Casimir矩阵误差1.3e−13ℏ²）。它们证实有限矩阵算对到给定精度，不能证实核模型充分、真实Jπ或模式。

| 同I比较 | 原Lv Band2/Band3 Ei keV | 实测中央E3−E2 keV | 固定Eq11最低两态gap keV | 对ordinal0/1只交换mapping |
|---|---|---|---|---|
| 17/2 | 1433.9 / 1477.9 | +44.0 | 841.203 | 预测−841.203或+841.203，幅度不变 |
| 21/2 | 2159.4 / 2203.9 | +44.5 | 839.717 | 预测−839.717或+839.717，幅度不变 |

实测输入[[lv-2022-evidence-against-wobbling-135pr]] L22-D23-001本轮fresh原表视觉核实。此诊断保持计数/能级/响应D不变，任何共同能量offset也不能改两态gap。改变文字标签可使次序相符，却不能让这两候选态的幅度匹配；形式可写不等同数据支持，若要改H/组态空间那是另一假说。这里只检验所列两种mapping，不排除其它本征态/参数/模型，不给modelerror/Cov/p值或宣称原实验被推翻。来源参数本身可能使用旧能谱定标，因此也不是前瞻blind holdout。

同H下可计算未在本任务定标的伴随量几何系数。定义单j/core常数磁矩μ=gR R+gj j，则

$$g=g_R+(g_j-g_R)a,\qquad
a=\frac{\langle\mathbf I\cdot\mathbf j\rangle}{I(I+1)}
=\frac{I(I+1)+j(j+1)-\langle R^2\rangle}{2I(I+1)}.$$

算符是量子标量，〈R²〉由完整R概率或独立body-I·j矩阵求得并互核；这不重建全部body几何。

| I | ordinal0的a | ordinal1的a | 差a0−a1 |
|---|---|---|---|
| 17/2 | .565133 | .504198 | .060935 |
| 21/2 | .468548 | .423580 | .044968 |
| 27/2 | .387731 | .383045 | .004686 |
| 31/2 | .335762 | .342471 | −.006709 |

这些**不是physicalg测量/预报数值**，physical差仍为(gj−gR)Δa；gj/gR、operator校准及single-j有效性均须证据。gj=gR时所有差都消失，a近也不意味着每轴RMS/概率相同，不能建统一g排他阈值。I27/2两态的体轴RMS不同但a很近，是当前固定H本征态的模型例；它比任意选择的态更具体，也仍不证明真实Pr归属。能量mapping若未先闭合，不可据此直接规划目标态g精度或机时。

使用旧Wang Eq3的明确处方敏感性C=.180757460MeV，两个gap变为715.129/723.189keV，也没仅由换标签闭合44keV。两个输出文件只保存各自variant，不混均值/误差，不把C差当实际作者调参史。源码`system/scripts/day23_prm_fixed_state_mapping.py`与model-contract-009保输入/单位/验证范围；新推断needs_review:true。下一优先补source-grounded相对E2算符/连接预测及actual model mapping，而不是捏造完整M1、δ、Q、τ或机时。


这一中央gap问题也不能仅靠给**这两个固定eigenstates**追加任意Hermitian非对角V来缩小：在固定对角能量E0/E1的2×2子空间，gap=sqrt[(E1−E0)²+4|V|²]，总不小于原gap。该代数只限定“固定两对角+off-diagonal-only”的补救，不排除改变单粒子能量/惯量、加入其它态/组态空间或其它自洽模型的影响。这里没有新增实际nuclear V、混合强度或置信界，不借旧任意100–200keV相互作用故事恢复模式认证。


## Day23：固定H的normalized core-only E2连接

本任务显式采用T2μ=SΣνD²μνqν，ν=0,±2，在1s/2i/3l轴上定义q0=cosγE、q±2=sinγE/sqrt2，并选γE=−26°与009 H同角。未知S有电荷×面积单位，始终不拟成某个实测Q；同一S在同operator的B比值中才相消。电荷与mass/potential同γ、共轴以及仅保core E2是额外假设，未认证粒子E2物理上不存在。原旋转形式/约定边界见[[hamamoto-2002-wobbling-excitations-odd-a-high-j-aligned-particles]] H02-D23-001；不能直接把另一轴系的Lund角/Q0换入本定义。[[frauendorf-2014-transverse-wobbling]] F14-D23-001的HFA式也未当低spin精确矩阵元。

约定lab矩阵元=CG(IiMi,2μ|IfMf)/sqrt(2If+1)×reduced，B=|reduced|²/(2Ii+1)。本实现先用ST18强耦合±K/±Ω对称基底投影，逐Ω取core spectator，再以CG对Ki/Kf和ν相干求和；physicalS被整体因子化。算法检验包括pure-axial fixedK CG、rank2 triangle、Hermitian reverse与详细平衡、tensor norm/完整final-space closure，以及三条matrix element用exp(−iβJy)生成Wigner-d并作24/40 Gauss-Legendre节点积分的独立核对。两处方各25检查通过，CG与独立积分最大差约1.9e−15、closure误差≤7.8e−16、reverse≤1.4e−15；与冻结009相同H的最低3态能量相同（数值差0）。这只证明finite-I operator实现，不验证实际nuclear mapping。

**closure不是实验branch sum**：其中包含向上、同I与diagonal/elastic矩阵元；不能用ΣB/S²=1给未测γ线强度或判全部退激完整。省掉这些项检验实验sum也不是该算符恒等式的含义。

| 条件mapping | rE2(747→yrast /526→另一band) | rE2(813→yrast /726同band) | 009同H能量诊断 |
|---|---|---|---|
| A：B3=ordinal0、B2=ordinal1；WangEq11 | 137.3196仅形式矩阵比，526为上跃 | .505399 | gap约841/840keV不等观测44/44.5；526候选ΔE=−.506395MeV |
| B：B3=ordinal1、B2=ordinal0；WangEq11 | .0299216 | .00349706 | 换mapping翻gap号但幅度不改 |
| A；旧WangEq3另variant | 22.2669仅形式矩阵比，526为上跃 | .500773 | 同两gap约715/723keV；526候选ΔE=−.356500MeV |
| B；旧WangEq3另variant | .0165857 | .00113266 | 同前限制，非原作者调参史 |
| Lv原作者联合提取/已报中央值 | .7(+.7/−.5) | .12(.08) | 原始能级与新测δ链保留 |

实测ratio出处[[lv-2022-evidence-against-wobbling-135pr]] L22-D22-001/002和L22-D22-R095-2：747/526为同母态两个带间出口，526在SI Table1多极性/Rac空白，按pureE2分母是原提取条件；813/726才是同母态out/in E2。不能把model r747/“假定存在的B3低spin in-band”=.708336当作实测747/526的比值来宣布相符。不同分母选择可让看似相近的数字代表完全不同问题。

两映射的相对向量不同，却都未同时闭合这个指定variant的能量/ratio中央值；未给实验jointCov/完整operator/modelerror，不做χ²或领域范围模式排除，也不赋两形式同等可信度。来源参数和ratio链并非独立：E2实验ratio来自原δ/强度输入，模型数值均来自同H/operator；不能按这些列再加独立“票”。小分母的r747对C处方敏感也提醒不按单一大ratio命名模式。

源码`system/scripts/day23_prm_core_e2.py`强制显式C处方、γE和冻结009参考模型文件，记录code/input hash与physical缺项。sameordinal acrossspin只是当前mapping假设，不等同证明adiabatic band/phonon。后续须检验wavefunction tracking/其它候选态，或补真实电磁operator，而不是拟chargeγ到某个ratio、从E2结果造M1/δ/Q/τ/机时。所有新推断needs_review:true，原Pr/Au争议支持与反证并列。


**必须用同H检验退激方向**：在mapping A，模型I17/2母态ordinal0与I13/2末态ordinal1间ΔE=−.506395MeV（旧C也为−.356500），所以“137.3/22.3”只是两个量子矩阵强度的形式比，不能称理论预测的526自发γ退激比；非零吸收/上跃矩阵元不意味着放光通道开放。程序为这种γ比输出null并保留形式矩阵量，而非将原实测526计数改为零。mapping B的对应ΔE=+1.151563MeV虽为向下，也与实测526keV能量不等，原模型差别仍须检验。这比只比较B大小更清楚地暴露特定mapping的适用边界，但不排除其它H/态/模型。

## Day23：同一固定H的M1、静态矩与尺度消去检验

从[[hamamoto-2002-wobbling-excitations-odd-a-high-j-aligned-particles]] H02-D23-003的算符，在本任务固定单j投影下写

$$\boldsymbol\mu=g_R\mathbf I+(g_j-g_R)\mathbf j.$$

总I生成元不连接不同I，也不改变同I空间的正交multiplicity态；它对对角静态磁矩仍有贡献。因此跨I的M1可以因子化为未知 $S_M=\sqrt{3/(4\pi)}(g_j-g_R)\mu_N$ 乘 $j_{\rm lab}$，对角静态量则仍用完整的g公式。单j投影、常数gj/gR和core磁矩近似必须明示，不能把另一核素的effectiveg默放进来；gj=gR时跃迁磁算符消失，也不能由非零j矩阵元保证实际M1必非零。

本任务用ST18 Eq7的lab耦合态逐m/MR求rank1矩阵元，保持R/KR，再用已核U变换；没有从body-j RMS猜测跃迁强度。源码`system/scripts/day23_prm_particle_m1.py`强制冻结009和010输入以及显式C处方。每处方32项控制通过：freeR0解析极限、两个labM提取、triangle、Hermitian reverse/详细平衡、完整j closure、j+R生成元和对角Casimir。最大closure误差3.6e−14ℏ²、生成元误差2.8e−14、对角a与009独立body-Casimir差≤4.5e−16；009能谱和010 E2差0。**closure仅对particle-j，不是完整磁矩，也不是γ分支总和**。这里的有限PRM允许内禀j动力学变化，不能称又算了一次冻结j；F14的冻结j非零M1论证独立保留。

| 映射与处方 | B(M1)/未知SM²：747 /813候选 | normalized E2/j振幅：747 /813候选 | 跨线振幅双比 |
|---|---|---|---|
| A，Wang Eq11 | 1.661094 /1.311946 | −.279323 /−.285530 | .978261 |
| B，Wang Eq11 | .00839147 /.00987035 | +.317974 /+.285737 | 1.112823 |
| A，旧Wang Eq3 | 1.419514 /1.089001 | −.302379 /−.312115 | .968807 |
| B，旧Wang Eq3 | .02748968 /.02484233 | +.116704 /+.102295 | 1.140861 |

这些均为源定义下的本任务模型量，见[[streck-2018-behavior-collective-rotor-wobbling]] ST18-D23-011/012，不是原作者新报告或实际δ。Eq11在I21/2的两mapping下，E2与M1强度都相差约两数量级，normalized E2/M1比却几乎相同（.081527/.081645）；同一混合比能掩盖相当不同的绝对强度。实际绝对尺度仍未知，且能量mapping已经不闭合，不据此为目标态给机时或排他精度。

若两条同型M1+E2线共用算符、scale与phase/radiative约定，写 $\delta_t/E_{\gamma,t}=K(S_E/S_M)(e_t/m_t)$，则

$$D=\frac{\delta_{747}/E_{747}}{\delta_{813}/E_{813}}
=\frac{e_{747}/m_{747}}{e_{813}/m_{813}}.$$

共同scale与常数K消去，得到上表末列。这个量仍依赖charge tensor形状、single-j模型和mapping；若effective磁算符随spin改变，就不能声称已消去全部物理输入。表中振幅比对核态的任意整体rephasing不变；跨multipole物理约定与全局operator符号须统一，双比又消去了相同的全局符号。

[[lv-2022-evidence-against-wobbling-135pr]] L22-4的已报中心值与747.3/813.2keV给D中央1.382288。它只重用原δ提取，不是新增独立实验；两条不对称marginal误差及共用校准不构成joint likelihood，当前不造CI、显著性或宣布哪一mapping获胜。unknown model scale也不意味着真实P/Rac不能选根，SH26固定σ/I=.2的大根条件支持仍须保留。

另一个伴随量是跨母态的M1强度比，Eq11下A/B为1.266129/.850170，旧C为1.303501/1.106566，scale在相同算符下消去。实测它仍需**两母态寿命、全部退激分支及转换修正**，不能用两线计数或relative intensity直接代替。必要输入还包括正确Jπ/placement、净谱与响应/feeding的共同Cov、未用于本任务定标的EM输入，以及首先可接受的same-H能量mapping。不存在的τ/Q/δ、实验率和机时保持空缺。新推断needs_review:true。

## Day23：从单j练习迁移到原多轨道QTR的算符门

[[lv-2022-evidence-against-wobbling-135pr]] L22-D23-002/003与[[guo-2022-low-spin-wobbling-187au]] GU22-D23-012将原模型与当前ST18单j任务variant分开：Pr的10轨道/配对、Au的9轨道含h11/2/h9/2/f7/2，都有实际source前提。Au #21/#22还明确列混合来源；Pr #14/15/16虽均为h11/2来源，也不由“standard parameters”给出完整相干幅/occupation/EM矩阵。**不同Nilsson轨道不自动意味着不同spherical j**；若严格限制同一l,j且同一常数单体算符，任意Ω混合仍保留single-j投影。因此既不能默搬共同SM，也不能只数轨道就断言SM必失败。

完整磁矩在跨I时为 $(g_l-g_R)\mathbf l+(g_s-g_R)\mathbf s$。在同l、s1/2的两个j不可约子空间间，总j=l+s的矩阵元为0，所以 $\langle j_-|\mathbf l|j_+\rangle=-\langle j_-|\mathbf s|j_+\rangle$，而两项各自一般非零；相应M1系数是 $g_s-g_l$，不是可乘零跨j生成元的一个gj。对角block则有 $\mathbf s=\pm\mathbf j/(2l+1)$，恢复两种Landé投影。该exact角代数见[[hamamoto-2002-wobbling-excitations-odd-a-high-j-aligned-particles]] H02-D23-004，源码`system/scripts/day23_multij_m1_operator.py`保完整l×s空间与CG变换。

l=1和l=5的22项unitarity、Casimir、j directsum、跨j l+s相消、diagonal投影、closure与detailed-balance检查通过。l5纯角分量的 $B_s(11/2\to9/2)=5/11$、反向6/11，角矩用ℏ=1；不是实际Au/Pr的γ强度，未选gl/gs/gR、radial/BCS或混合权重。gs=gl时该跨伙伴磁算符消失只是符号极限，不代表核内实际系数相等。closure包括elastic/upward，依旧不是实验branch sum。

由此，011跨线D尺度消去只有在实际EM振幅能共同因子化时才适用。完整模型中须先核l/s与core、particle E2各项的相干组合、轨道/占据与配对约定、参数定标集和共同phase；不能把实际多轨道矩阵写成一个未经证明的g_eff，再把缺项当已消去。当前exact分量只证明迁移有条件，不证明它在某个h-dominant具体态必然给显著偏差；实际大小仍缺输入。

| 输入层 | 原件目前可核 | 仍缺/不能默补 |
|---|---|---|
| Pr QTR H | ε2.16/γ26、Harris12.5/12.5、10负宇称、Fermi44MeV、standard Nilsson/pairing | 完整数值轨道系数/占据与原实现，不按standard造κ/μ/Δ |
| Pr QTR EM | gs,eff=.6gs,free、gcore=Z/A文字 | 全相干EM矩阵/phase及逐量定标史，不能只用这两常数重放模型 |
| Au QTR H/space | ε2.21/γ12、Harris25/8、9轨道与Table1来源、bands主要#19/#21 | 表标签与柱图不是完整波函数/BCS矩阵；不臆填h/f权重 |
| task单j variant | 009–011完整H、两C与normalized operator均已固定/可重算 | 只限定此variant与mapping；energy失败不排除原多轨道QTR |
| 实验response | 两篇原P/Rac/gates/误差及外部校准链 | 原net spectra/feeding/共同Cov/likelihood与独立τ仍缺 |

可证伪问题修订为：**固定一个足以描述实际能级的明确组态空间、算符与定标集后，候选configuration能否同时预报未用于定标的跨线δ/E形状和跨母态强度比？** 必要伴随量仍是两τ、完整branch/转换及逐线response；先确认common-scale条件或直接用完整EM振幅，不因代数可写或source模型较完整就给等可信度/最终模式认证。新needs_review:true，SH26条件AD支持与Pr/Au实际反证并列保留。

## Day23：半整数spin的单光子响应组件门

依据[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D23-001/002与[[droste-1996-pdco-formalism]] DR96-D23-001/002，本任务新增`system/scripts/day23_halfspin_singles_response.py`，完整保留半整数Mi/Mf，不把旧integer-only kernel直接移用于Pr。参数d_RB是RB interaction amplitude的aE2/aM1，初态在左并含原source的能量/相位规范；未默认为Lv、Guo或SH26的已发表δ。

取h=±1，磁项π=1、电项π=0，振幅逐项包含h^π、sqrt(2L+1)、CG(IfMf,L(Mi−Mf)|IiMi)与d^L_(Mi−Mf,h)(θ)，d=exp(−iθJy)。角强度W归一为角平均1；线分析轴x′在发射平面内、y′垂直平面，用A−−A+和A−+A+相干叠加求Ix′/Iy′，P_stokes=(Ix′−Iy′)/W。它不是Compton计数A，也未认证实际核物理δ/实验偏振约定的映射。

14项控制通过：RB67的3/2→1/2 R2解析表、I1/2 singles约束、isotropic W1/Stokes0、positive密度/Stokes球、full角归一、反射、M/E dual、方向rank0/2/4以及混合/有界局部Jacobian。解析与归一误差≤2.3e−15、禁戒高rank数值矩≤5.0e−14。控制只核所定义halfspin singles数学组件，不是原PDCO程序/array或实际实验认证。

| 条件设计量 | 本任务结果 | 适用边界 |
|---|---|---|
| I17/2→15/2、d_RB+.5、σ/I.2、θ154°的相干W减纯项非相干加权 | −.519249 | 实际M1/E2响应不能忽略干涉；数值不是Pr观测 |
| I17/2、d_RB−.5、σ/I.2的Rpoint154/90与local90 P | 1.768130 /−.843860 | 名义角点、singles、无actualgate；不与Lv/Guo点直接比fit |
| 同点两参数Jacobian determinant | −1.397913，step折半差1.4e−8 | 仅说明此理想局部可逆，不证global唯一/真实likelihood |
| I17/2、Gaussian输入σ/I.8的实际离散rms/I | .542317 | 截断分布rms与输入width不同，不能混名 |

Gaussian严格定义为DR96 Eq19的exp[−M²/(2σ²)]，但Lv对sigma的variance文字歧义仍保留，未以本任务习惯认证原producer。对称Mi布居是模型假设，未从计数或所有门选样中反推为已知事实。

**singles≠任意all-detector-gate观测**：实际gated all-angle spectra仍包含有限acceptance/效率/门级联与feeding条件；完整4π积分的数学边缘不同。实际比较仍需每条线的gate、角环固体角/效率/合并权重、散射几何与a/Q、deorientation、相位/状态顺序和联合Cov。两个实验不能只凭同名P/Rac或sigma/I就共用响应；当前未用新kernel给Pr/Au拟合、报physicalδ/CI、改SH26固定σ/I条件支持或预判两谷等深。新needs_review:true。

## Day23：Pr上游门与母态取向的独立输入

[[lv-2022-evidence-against-wobbling-135pr]] L22-D23-004绑定实际顺序：796.4 E2的25/2→21/2先于813.2的21/2→19/2，450.2的19/2→17/2先于747.3的17/2→15/2。因此两条偏振选门均在上游，不能把积分**下游**光子恢复先发γ边缘的恒等式，倒用于认为目标母态已独立Gaussian取向。源公式边界来自[[droste-1996-pdco-formalism]] DR96-D23-003和[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D23-003。

本任务`system/scripts/day23_halfspin_upstream_gate.py`将ρdaughter=Σh G_hρ0G_h†（保未归一的gate yield）再接target振幅，和直接two-photon contraction独立收缩互核。上游4π通道另用CG的photon磁子态求和，交叉multipole积分消去；axisymmetric初态的Wigner角积分24/40节点给同一结果。对后续γ完整trace保先发photon密度、isotropic limit、positive/归一、halfspin M1/M1解析式等共19控制通过，最大joint/两路差≤7.8e−16。它们不认证实际Pr的条件响应。

以下**只是design**：初态Gaussian输入σ/I=.2；target d_RB=−.5，450-shaped门也只取d_RB−.5的设计probe，未把已发表δ−.31映射到RB。796 gate的E2类别取原表，其余初态/响应没有从数据估计。

| 设计序列 | 上游完整4π后的target局部P90 | 独立重设target Gaussian .2的P90 | 共面point门90°条件P90 |
|---|---|---|---|
| 25/2→21/2 E2，再21/2→19/2 mixed | −.813104 | −.833536 | −.882194 |
| 19/2→17/2 mixed，再17/2→15/2 mixed | −.815883 | −.843860 | −.902633 |

第一例4π后daughter rms/I=.218217，第二例.225081，都不是简单重新设置的.2。对于90°共面point门，若把daughter非对角元人为删掉，P90分别变成−.812605/−.819218；这说明coherence在这种设计中可影响target响应，**不是测得偏差或原分析漏项**。actualall-detector gate的方位角合并可能消去这些offdiagonal项，必须带实际acceptance/效率/weights再核，不能用pointgate效果替阵列估误差。

“谱峰clean”与“条件密度响应正确”是不同检验；本练习不质疑原污染排除，也未认定原作者没处理取向。两实验要比较同一逐线观测向量，仍需initial/feeding密度或可追溯的nuisance模型、gate次序/placement、角环φ/θ及效率合并、散射响应a/Q、sidefeeding/去取向与jointCov。没有这些输入就保持original-response not-ready，不拟新的Prδ/CI或恢复根等深认证。新needs_review:true。

## Day23：方位角合并会消去哪部分上游门相干

014的coplanar pointgate只是一项条件设计，不能由它对实际all-detector gate给偏差估计。依[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D23-004，Mi对角初态下，gate两个振幅的差给q=mf−mf′，L≤2使|q|≤4；方向改变φ只给daughter矩阵元相位exp(iqφ)。因此在固定gate polar θ、声明正且归一权重下，

$$\bar\rho_{ff'}(\theta)=\rho_{ff'}(\theta,0)\eta_{m_f-m_{f'}},\qquad
\eta_q=\sum_d w_d e^{iq\phi_d}.$$

uniform Cn、n>4使ηq=0 (q=1…4)，足够消去所有offdiagonal；这不是n>4为必要条件的分类，个别selection可让更小n也足够。C4仍有η4=1，不能只看“方位对称”就认为全消。若12点正权重取1+.2cos2φ这一**纯设计**，则η2=.1、其它q1/3/4为0，留一部分coherence。显式G(φ) photontrace、daughter旋转合并与ηq乘法三路、全体旋转/PSD/秩等24项控制通过，max差≤7e−17；源码`system/scripts/day23_gate_azimuth_moments.py`。

| 同014设计、gateθ90 | 796/813-shaped target P90 | 450/747-shaped target P90 |
|---|---|---|
| 单coplanar pointgate | −.882194 | −.902633 |
| uniform C5或C12 azimuth，fixedθ | −.812605 | −.819218 |
| 12点的1+.2cos2φ正权重 | −.821797 | −.830516 |
| 完整上游4π gate | −.813104 | −.815883 |

均匀方位角确实消除了014相应offdiagonal影响；固定θ的diagonal布居仍不同于4π，两个设计的density最大差约.000268/.003201。所以上游4π、uniform ring和单pointgate是不同response，不能互相代替，也不由表中接近数字给actualexperiment误差上限。

最小输入合同见[[droste-1996-pdco-formalism]] DR96-D23-004：ηq及θ权重必须是**选定target/gate detector pairs的有效响应**。即使nominal detector positions均匀，逐台efficiency/live time、同探测器veto、散射选样或coincidence构造都可使target条件下的weights不同。应按能量、run、gate与target类别保留接受度或它在当前假设下的低阶moments，而不是从clover数量默造等权。跨θ合并先加未归一density/yield，再求P；新needs_review:true，未给实际ηq、δ/CI/Q/τ/率或机时。

## Day23：AMR原模型的正支持与受控对照边界

[[kumar-2025-review-magnetic-antimagnetic-rotational-structures]] KU25-D23-001/002/003明确外部核阅的原Zhao2011 PC-PK1 TAC结果，而非2025新实验：双剪刀闭合、neutron mixing、selfconsistent形变共同给出105Cd的能谱/E2支持，pairing被忽略；2010实验点是重用。没有inert core的微观模型不能直接塞回固定core+刚性三blades图像，作者“corelike3ℏ”也只是所定义分解下的模型量。

**polarization有量身份**：本模型Fig3/4指两质子空穴诱发的密度/形变重排，非Compton测量的γ线偏振P。其ablation先算107Sn再冻结势移去两质子，改变H/自洽场，不是只换configuration assignment；因此不能拿这两条曲线充当本卡“保持H/算符只换标签”的受控比较。数据层D仍可保持不变，但model-layer所改输入必须列明。该区分也适用于Pr/Au两个不同H的发表模型。

| 层次 | 这个正支持案例提供什么 | 仍不能推出什么 |
|---|---|---|
| 几何 | Fig1/2模型双剪刀闭合与neutron alignment/mixing | 新测j/R方向或唯一核态模式 |
| 电磁 | 同源2010 B(E2)点与模型/形变相符，selfcons vs frozen-field不同 | 独立新增寿命、所有跨带M1禁止、固定β统一门 |
| 参数 | PC-PK1、2D/N10/无pairing明确 | 无任何历史定标、完整pairing/数值误差已验证 |
| 替代/反证 | 冻势约17ℏ终止及E2压制给有条件可检验趋势 | 只改标签的same-H实验、全核区排他结论 |

可证伪问题：在明确fixed configuration/算符与配对适用范围下，**能量之外的寿命/完整分支B(E2)及J2，能否共同支持同一随spin的形变与alignment轨迹？** 必要输入是原τ、sidefeeding/branch/ICC与系统误差，以及对应model density/occupation，而非从图读一个下降趋势再赋新机时。当前原2010实验与2013Comment/Reply仍未核，外部原模型正式归档deferred，故保needs_review:true。Pr/Au争议不否决这个AMR模型支持，反过来也不拿105Cd替代Pr/Au的逐线证据。

## Day23：同母态、同分母还须同一绝对归一

Day24无学分preview的135Nd诊断（[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24P-006/007）对本卡A槽提供一个方法桥：相近图点/同spin/相同B标签仍不足以证明可相加、相除或用于δ。需同时绑定γ的parent/daughter、multipole component、能量幂与absolute/conditional normalizer；同parent的M1_in与E2_in也可能属于ΔI1/2不同支路，不能直接当混合γ两成分。

模型component标签m对应I→I−m见[[almehed-2011-chiral-vibrations-a135]] AL11-D24P-001，B到光子率见[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D24P-001。多量联合比较应先核这个quantity identity再比较数值；未闭合时不由形式可行的normalization重解释赋同等可信度、不把legacy budget控制当paper-error认证。此方法迁移不把135Nd物理结果迁到Pr/Au，也不授Day24学分。

## Day23：configuration relabel的可检验范围

从Day24无学分preview迁回本卡的方法合同：[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D24P-004/005区分basis change、energy-eigenstate relabel与fixed-operator physical mixing。保持原实验counts/level scheme的替代解释可以换mapping，却不能把改变H/算符/截断空间的数值变换称作“仅换configuration”。本卡009–011的ordinal交换保H与operator，能量gap不被换标签修复；它不是对任意多轨道alternative的否证。

完整EM块的不变量或phase反例只有在同Ii/If、固定operator、封闭projectors及所需RME信息齐备才可用；[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24P-008的实际缺单元说明，未测/上跃/逆向不应填零来制造完整性。该方法仅迁移逻辑，不迁移核素数值、actualδ或新机时，所有新推断needs_review:true。

## Day23：伙伴关系还需标明所用对称操作

[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]] F01-D23-001与[[signature-partner-bands]]分清unitary signature、ordinaryT/Kramers和手征antiunitaryC；非零ω的Routhian T变换改变ω，不能用零频Kramers要求同一ω的两signature分支简并。式I=α+2n的自旋子序列不是当前fixed-j数学toy的eigenstate枚举，也不是自动的phonon标签。

`system/scripts/day23_signature_cranking_symmetry.py`以声明dimensionless intrinsic hω、六个j表示、Rz/T/C与projection phase共86检查通过，零频半整数Kramers与非零频分支可分相容。它不计算真实nucleus/rotor spectra，归一unitary phase不变也不认证任何实验mode。Pr/Au的same-count重指派必须保留这个relationship层：共享signature或类似能量不足以把SP/TiP/wobbling互换，也不等于pseudospin。新needs_review:true，不赋统一δ/W.u.或g门。

## Day23：共同因子相消不是独立验证

Day24无学分preview的实际135Nd例（[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24P-009/010）提供一项可迁移原则：同parent/sameXL/sameisotope时，WU和共同τ可在B比中消去；但如果B字段与Iγ-Epower本由同一评价链派生，它们相近不能当两次独立验证。缺parent/line/component/normalizer时，消共同单位并没有消掉这些身份条件。

对本卡Pr/Au支持—反证—依赖矩阵，relativeB、δ、分支强度或评价重复引述也须标同源；跨核不能以数值比接近替代共同响应/算符定标。数学相消有效域和实际数据独立性分别检验；保持source条件、空值和needs_review，不造δ/τ/Q/机时或统一hardgate。

## Day23：从约定可比到逐线前向响应的条件边界

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D23-001明确该发射约定下KS=−RB；[[starosta-1999-pdco-experimental-test]] ST99-D23-001明确Efield相对发射平面的P与Compton计数A不是同一个parallel/perp标签。source013的RB basis若改用含(−1)^L的native basis，必须同步d_native=−d_RB；完整amplitude仅差global−，ρ/IQUV不变。300点/11项basis/axis/pure/mixed/positive控制通过；未映射mixed coordinate可改干涉，pure limits却不能发现此错。

现在只在**额外假定Lv的quotedδ采用这里精确KS定义**时，把[[lv-2022-evidence-against-wobbling-135pr]] L22-4的两个中心映为d_RB+.47/+.37。原producer的实际δ/轴约定仍未由本练习核定，未拟任何width或实验点。declaredGaussian target σ/I=.2/.4/.8与nominal154/90 singles及local90 EfieldP给：

| 源线/中心δ | width design | ideal point W154/W90 | ideal local P90 |
|---|---|---|---|
| 747.3，quoted−.47→conditionaldRB+.47 | .2 / .4 / .8 | .235097 / .424487 / .759873 | +.033501 / +.013840 / +.002639 |
| 813.2，quoted−.37→conditionaldRB+.37 | .2 / .4 / .8 | .296696 / .480410 / .788306 | −.023059 / −.024560 / −.012010 |

这说明在所声明响应中small negative KSδ并不要求同一个P号；747 P+.04/δ−.47与813 P−.03/δ−.37须逐线保留，不能把两个偏振号混用。**数值接近也不是复现实验**：实际Pr的Rac使用157.6+133.6与75.5+104.5角组，还包含upstream796/450、有限角/效率/合并权重/feeding/attenuation与jointCov；这些仍缺。局部Efield矩阵已算对只解除一个component/convention问题，不代替全响应、独立多极证据或共同likelihood。

源码`system/scripts/day23_mixing_convention_bridge.py`保source参数角色、extra KS-assumption和null fitted_width/likelihood。没有将模型forward例改成新measuredδ、P/Rac CI或σ/I估计，更不预判两谷等深；SH26固定σ/I=.2的AD大根条件支持照保。Q/a/g/Q(E)/τ、真实rate与机时未填造，新增推断needs_review:true。

## Day23：真实名义角组不等于已恢复真实array响应

[[lv-2022-evidence-against-wobbling-135pr]] L22-D23-005把157.6/133.6和75.5/104.5的名义极角锁到原Eq1。即使polar angles实际可核，实际每个selected target/gate pair的有限acceptance、效率/live time、相对组归一和feeding仍须数据。任务只在**每组已独立归一为positive weighted mean**的声明下，写

$$R=\eta\frac{fW_{157.6}+(1-f)W_{133.6}}{nW_{75.5}+(1-n)W_{104.5}},\qquad f,n\in[0,1].$$

η是实际relative group normalizer/calibration的占位符，**未赋本实验数值**。在source013的axisymmetric singles模型里，两near镜角W/P相同，所以n相消；在η=1的额外条件下，R落在min(Wfar)/max(Wnear)与max(Wfar)/min(Wnear)之间。若η未获，则这里只限制R/η，不能称actualRac绝对bound，也不能说原实验没校准或nuisance先验可任意自由。

| 025同样source-bound KS假设、width .4设计 | conditional R/η的positive-weight envelope | 等权示例R/η | near组ideal P | 旧nominal154/90 idealR |
|---|---|---|---|---|
| 747.3，dRB+.47 | .413899–.682381 | .548140 | +.009083 | .424487 |
| 813.2，dRB+.37 | .472193–.717138 | .594665 | −.026947 | .480410 |

这些都不是实际fit/CI或对原点的排除。只看旧点角数值偶近而忽略角组/归一/门，会比较不同对象。KS映射与width均保原conditional角色，不能据表恢复actualσ或δ；原L22、SH26的真实分支支持/反证没有因此被改写。

[[droste-1996-pdco-formalism]] DR96-D23-005给finitegate条件对称的原source边界。task pureE2上游point45°设计的近镜角ρ差8.65e−5，而联合gate/target反射恢复到浮点误差；实际full-array可能去相干，不能从point例推bias。求groupP须先Σwρ而不是等权平均P；该小例的两种P差只有1.9e−9，同样不代表新可测精度。`system/scripts/day23_pr_angle_group_response.py`的11controls只核所声明组件、convex group algebra/PSDs与对称，不认证actualresponse或原producer。

下一输入合同因此具体为：按line/run/gate/target-detector pair的φ/θ acceptance和效率/live time/η校准、conditional feeding/去取向密度与a/Q、共同Cov/likelihood。不能因本任务没拿到这些值就把它们放开无界后宣判两谷等深；SH26 fixedσ/I=.2 AD大根条件支持继续保留。新needs_review:true，未造新δ/g/Q/τ/机时。

## Day23：same-data向量不能增加独立票数

[[lv-2022-evidence-against-wobbling-135pr]] L22-D23-006与[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D23-002把813/726的derivedB写成一个联合变换。令y=(Iout/Iden)/h_E2den，K=(Eden/Eout)^5，L=(cE2/cM1)Eden⁵/Eout³，则

$$e=r_{E2}=Ky\frac{\delta^2}{1+\delta^2},\qquad
m=r_{M1}=Ly\frac{1}{1+\delta^2}.$$

e无量纲、m按μN²/(e²b²)记。直接逆变换给y=e/K+m/L和δ²=(e/K)/(m/L)；它只是回到输入的共同组合，不是由两derivedB新增测得δ/h。两个输出在非零δ的一支上可local rank2，不代表global sign可恢复：±δ的两个B完全相同，P/AD的干涉量另有信息。

$$J=\begin{pmatrix}
K\delta^2/(1+\delta^2)&2Ky\delta/(1+\delta^2)^2\\
L/(1+\delta^2)&-2Ly\delta/(1+\delta^2)^2
\end{pmatrix},\qquad
\Sigma_{e,m}=J\Sigma_{y,\delta}J^T.$$

实际Σ未给，本文不赋ρ或ratio CI。只在differential设计中，y固定/δ变化给反相关方向，δ固定/y变化给同向方向；这说明忽略原Cov不能默认两个输出独立，不是对原实验真实相关系数的估计。δ=0的局部rank降为1，near-zero时的反演/误差还需原likelihood，而不能照搬Gaussian线性传播。

813/726的source中心代入得e=.118129、m=.397594；旧本页使用声明近似系数.697给m=.397722，差来自率系数约定/舍入，是两次条件中央算术，不是新calibration/物理效应或producer已经复现。它们均与原printed.12/.4的角色相容，但不能拿“δ符合、rE2符合、rM1符合”当三次独立采集/选根支持。若有真正不同采集的absolute强度当然可另检验，必须明确那份独立source/normalizer，当前derivedpair没有自动获得它。

747/526的den不是同band in-branch，且SI多极/Rac空，纯E2 den只是原提取条件；未知h会共同缩放两个B，不能由公式逆得actualdenδ。`system/scripts/day23_derived_strength_vector.py`的12控件仅核变换/单位/输入角色，不填任何新δ/Q/g/τ/CI/探测率/机时，也不抹SH26 fixedσ/I条件支持或宣布真实两谷等深。新needs_review:true。

## Day23：先冻结母态身份，再寻找绝对强度伴随量

[[nndc-2008-135pr-selected-mixing-records]] N135-D23-001/002/003的官方CSV示例说明：寿命检索须绑定核素、母态端点、Jπ及评价版本，不能只在同核附近找到ps数就代入。旧母33/54分别是1478.2/2204.7keV的争议候选，half_life空；lower10/29有22.9/2.4ps但属于退激末态，不提供这两母态absoluteB。接口cutoff2008亦不重放Lv的新P/Rac/δ。

| 所需输入 | 已实际获得 | 尚不能做的推断 |
|---|---|---|
| gamma母末态身份 | 全部174条与105能级同快照连接；目标527/747.1/726/814 | 不能由跨版本接近端点证明同事件/同response |
| 母态时钟 | 33/54为空；10/29半衰期属于其它态 | 不能移用末态T1/2，不能补争议母meanτ |
| 混合/转换/branch | 目标δ/B/total转换空，relativeI是母态局部归一 | D不等M1/δ/P；空值不0，归一不保证出口完整 |
| 新旧观测比较 | [[lv-2022-evidence-against-wobbling-135pr]]原新线与中心另保留 | 旧评价提取年月不成为额外实验或分支裁决 |

实际输入缺口因此具体到争议母态τ、完整光子分支及转换/多极性、feeding和响应/Σ；当前没有absoluteQ/B/新设施率或机时。`system/scripts/day23_pr135_export_identity.py`的15项CSV/端点/单位/空值控制不等于原实验likelihood验证。新增needs_review:true，保持其它核正支持链与SH26条件AD信息。

## Day23：转换系数的实验节点与评价派生节点

[[guo-2022-low-spin-wobbling-187au]] GU22-D23-013–016补实际官方评价annotation层。比较用的旧观测向量应冻结为376/462两线的实验αK转述及各自研究来源，不能直接拿API的MR/totalCC替代：评价明确MR由αK/L计算，SG KC与G total亦各有角色。

依[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-2，标准两多极截断下αK(δ)=[αK(M1)+δ²αK(E2)]/(1+δ²)。因此旧αK可以向前比较|δ|分支，但不单独恢复干涉符号；由该αK反演的δ又不是新的独立约束。当前没有本两能量的明确理论表/原测归一与共同Cov，不能把中央值或一倍误差盒直接变成联合置信限。

readiness新增具体项：1978两母态合并的选择/归一、1998报告族1994/1995/1998的采集与编译对应、2013 parent-clock/XREF更正后逐记录的端点映射。完整NDS/原paper正文仍未读，官方注释的可读数值不填补所有实验方法。没有用Hg分钟clock或Au末态秒clock补争议母ps寿命；没有新测δ/Q/τ/ICC/设施率/机时。新needs_review:true。

## Day23：先前向比较旧转换，避免把概述当逐点等同

[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D23-001/002提供本次实际Z79/FO纯分量，[[guo-2022-low-spin-wobbling-187au]] GU22-D23-013/017给旧实验的评价转述与本任务角色。以下统一采用历史标称E，不改任一新源原值；各预测只使用所列δ中央，不代表允许分支的全范围。

| 历史Eγ keV | αK(M1)/αK(E2)名义FO | Guo小δ中心的αK | Sensharma大δ中心的αK | 1998 / 1978实验αK的评价转述 |
|---|---|---|---|---|
| 376.3 | .1483 / .0360 | .141189 | .049815 | .119(15) / .11(3) |
| 462.1 | .0859 / .0225 | .081291 | .028917 | .050(9) / .08(2) |

原[[sensharma-2020-longitudinal-wobbling-187au]] AU20-D22-R094-1的大δ为−2.67/−2.98，Guo为−.26/−.28。旧实验的中央并不要求等于某一δ中央的预测；一条旧线与一个新中心靠近也不能当全分支已在共同响应中验证。尤其462两份旧αK中心不同，若只写“旧转换支持小根”会丢失具体程度和采集/归一条件。此表不给新δ或显著性，也不推两模式等可信。

下一高信息输入从缺理论表转为缺原电子/光子归一、shell效率/角响应和共同Cov。理论打印误差与历史quoted误差均已记录，未默认独立Gaussian；sourceδ的不对称范围也未被当置信集。不得把此表再与由旧αK计算的评价MR相乘似然。正负δ不由标准ICC区分；若要联合选根仍须AD/P干涉量的actualresponse。新needs_review:true，无新τ/Q/设施率/机时。

## Day23：端点映射与共同拟合的输入缺口

在030的实际FO K中央固定后，沿[[guo-2022-low-spin-wobbling-187au]] GU22-D23-018，将原printed不对称δ端点代入标准式：376[−.41,−.15]映为αK[.132139,.145829]；462[−.97,−.05]映为[.055165,.085742]。理论来自[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D23-001，未重新查询或改能量。

| 旧αK的评价转述 | 中央±所报误差的坐标范围 | 与上述新δ端点像的交集 |
|---|---|---|
| 376,1998Ru04 .119(15) | [.104,.134] | [.132139,.134] |
| 376,1978Bo05 .11(3) | [.08,.14] | [.132139,.14] |
| 462,1998Ru04 .050(9) | [.041,.059] | [.055165,.059] |
| 462,1978Bo05 .08(2) | [.06,.10] | [.06,.085742] |

四个逐点交集都存在。030的“中心不全相同”和此处“端点坐标范围相交”均成立；后者没有指定任何coverage，也不等于同一组共享校准/归一参数同时满足所有数据。原论文/response/联合δ域、电子光子归一与共同Cov仍缺；不能把单维印刷误差拼接成联合置信域，不能从此处宣布历史αK已经验证新方完整likelihood或大根已排除。

该练习只固定名义理论分量作确定性运算，打印theorymarginals与E误差仍未传播。`system/scripts/day23_au187_quoted_endpoints.py`五项输入/端点/符号/交集控制通过，不新增实验、δ反演、τ/Q或机时。新增needs_review:true。

## Day23：Au支持方的可比向量与原采样范围

[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-D23-6/7补了真实发表的reduced AD向量，而非只有最终δ：376 A2/A4=−.730(2)/.523(1)，461.8为−.699(1)/.502(1)。相应DCO-like r=.48(3)/.38(1)须保本定义，不能当Guo Rac；333.8参考的αexp=.84(1)/.81(1)和σ/J=.2属于校准/模型输入层。完整净峰/共同Cov、ring/gate/效率与原producer仍缺，表列多量不自动独立。

源方法实际先比较二次式候选的χ²并选较低根，之后只在该根邻域采样；所以printed局部误差与全局双分支/所有nuisance的概率比较要分别记录。不能抹掉源χ²条件信息，也不能在未获另一谷曲线时假定其等深。PRL Ref26仍为未具名待刊；学位论文可读步骤是同支持链的补充说明，不新增实验。

为对称检查两边印刷端点，[[sensharma-2020-longitudinal-wobbling-187au]] AU20-D23-4/5的源376 δ−2.67±.07、461.8−2.98±.02在固定历史E和[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D23-001名义FO下映为[.049200,.050472]/[.028840,.028995]。与[[guo-2022-low-spin-wobbling-187au]] GU22-D23-013旧αK各自printed范围不相交；这和031小δ端点像的四个交集构成明确的条件反证比较，仍无共同coverage/排除度。它检验的是所列printed端点与名义表的组合，不是原全允许大根族/校准系统的完整检验。新needs_review:true，不造δ/CI/绝对Q/τ或机时。

## Day23：先绑定AD系数所处阶段，再作共同向量比较

[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-D23-8/9收紧032的reduced-vector用法：Table4.4的列名是A2exp/A4exp，376字面(−.730,.523)；Fig4.12却给同线初始fit参数(−.6704,.3194)，图4.13的局部δ为−2.6637。这些字段与图的关系还需逐步校正/拟合输出，不能只据“experimental”列名当作未经衰减的净峰观测向量。A0在两个fit图的不同均值也不代表新的实测产额变化。

在[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D23-001/002和[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D23-001的任务kernel下，额外假设quotedδ使用该KS发射坐标，得到：

| 实际source centre | complete absM=1/2 A2/A4 | Gaussianσ/I=.2 A2/A4 | 假定参考α=.84/.81直接移用后的A2/A4 |
|---|---|---|---|
| 376.3 δ−2.67 | −.728040 / .523327 | −.668133 / .390306 | −.611553 / .423895 |
| 461.8 δ−2.98 | −.699904 / .501974 | −.633247 / .358304 | −.587920 / .406599 |

complete一列接近Table4.4，Gaussian的376 A2又接近Fig4.12，但A4仍有差。它们不能反推原作者用了哪种response或哪里有错：实际finiteangle/gate、参考α的定义/迁移、phase与修正顺序均未完整恢复。尤其参考333.8属于不同J，经验α移用只是另一个声明模型，不是已核原recipe或完整physicaldensity。

这把A槽缺口定位为**原逐环净峰→效率/门/取向校正→自由A2/A4 fit→选根及其系数表**各阶段的映射和共同Cov。不同阶段同名A2/A4不得直接拼jointfit；derived table接近某理论也不能当新的独立支持。小δ中心在同任务条件下的A4约.028–.041，但未据此对原数据给排除数或预判谷深。`system/scripts/day23_au187_ad_vector_forward.py`八项hash/归一/rank/12–24节点控制通过，最大projection差约2e−14；这些只验证组件，未复现作者likelihood。新增needs_review:true，无新δ/Q/τ/CI/率或机时。

## Day23：AD公式坐标已核，实际处理链仍待输入

沿[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-D23-10，直接实现源Eq2.43的F系数和Eq2.45/2.50的B/ρ，以明确Racah相位与exact Fraction阶乘和核查；再与[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D23-001/002的photon矩阵路径比较。打印公式的δEq与任务kernel满足dRB=−δEq：36个设计点在complete/Gaussian各自一致至约5e−15。两路共享CG primitive，独立性只限收缩路径；这些是数学检查，不是新增实验票。

因此可以在源AD公式层使用这个坐标桥，033未认证的producer/finitearray/gate/实际P轴并未随之自动得到。Fig4.13打印均值−2.6637的源式结果为complete(−.729393,.523023)、Gaussian .2(−.669375,.390079)；Table4.4与Fig4.12的数据阶段映射仍需原逐步输出。部分分量接近不能决定table已做哪项校正，不能把残差作原校准错误或globalroot判断。

下一研究输入优先级据此转为：支持方详细后续发表/版本是否公开净峰、衰减/几何校正顺序、链样本与两分支全局曲线。对2020 Ref26的未具名待刊文做有界发现；2022学位论文书版是版本候选，先核身份/实际body，不预设其与2021逐字相同，也不新增一次实验。新needs_review:true，无新δ/Q/τ/CI/机时。

## Day23：总体产额与选门弱峰纯度须分别输入

[[sensharma-2021-wobbling-motion-135pr-187au]] SE22-D23-001–005给实际2022章的版本/门谱。所核校准、A2/A4图表和选根程序与2021对应项相同，仍缺原处理阶段映射；版本出版不是新独立采集。Band3支持谱则具体到232.5+436.5门与412.3/548.6等伴随峰，已具可逐门核对的输入，不能继续只写抽象“支持方有巧合”。

若r=Y_Pt/Y_Au是总体布居比，κ_Pt、κ_Au分别为每个核在指定峰/门/trigger/效率/窗口下的有效贡献，则选定峰的Pt份额为

$$c=rac{r\,\kappa_{Pt}}{\kappa_{Au}+r\,\kappa_{Pt}}.$$

即使r<约.1，κ比未知时也不能推出c<.1；弱Au出口和强Pt出口、不同门效率会改变局部份额。此式为条件计数记账，不给实际r、κ或c新估计，不是设施率/机时。本源PACE4与低能线总体强度论据须保留其条件，target peak purity仍需逐门净谱/效率/分支/背景和isotope-specific companions。

[[guo-2022-low-spin-wobbling-187au]]的188Pt候选与支持方门谱下一步要用同一端点/能量分辨率和具体cascade比较。把Band3改归另一核素是身份重指派，超出只改configuration的B槽；B槽必须继续冻结核素、计数、能级和response，另检验组态/算符对未用于定标量的预测。原Band3在支持方是SP，不是二声子；其身份争议与Band2的LW/SP/轨道解释分别记录。新增needs_review:true，不作最终Au/Pt认证或任何新δ/Q/τ/机时。

## Day23：近能量匹配不能替代共同门谱

[[guo-2022-low-spin-wobbling-187au]] MU14-D23-001–005是已实际读的Pt2014 primary，不是Guo Ref23的Pt2017全文。它把比较对象从四个近能量数推进到真实级联：Pt基带265.6(2+→0+)与405.1(4+→2+)及513/598/655，另有SeqII414/551和SeqV412/549；不能把不同序列按能量单键接成一条虚构带。

支持Au的[[sensharma-2021-wobbling-motion-135pr-187au]] SE22-D23-003给232.5+436.5门及伴随412.3/548.6/333.8/413.7/567.0；Pt2014实际Fig2却用689.9与{202.6,583.7,894.5,405.1,265.6}之一双门sum。两图不共享同一门/响应/计数对象。当前只能列出“若Pt假说要解释该Au门谱，必须同时解释门内事件与全部伴随峰”的可证伪问题，不能由近能量或一份partial图未列门能量就填零泄漏/上限。

configuration槽亦有校准提醒：Pt2014 Table3的所谓实验g组合实际是由分支/δ相关式提取的|gK−gR|/Q0，而Q0、gR有采用输入。它提供组态偏好的条件支持，不能拿同源派生磁量当独立未定标检验。真正B槽仍须冻结Au核素、计数、能级/response和H/operator，改映射后预报未用于定标的observable；Pt换核素另属identity审计。新增needs_review:true，不新增physicalg/δ/τ/CI或机时。

## Day23：Pt近能量向量包含跨带出口，不能只当单一signature序列

[[guo-2022-low-spin-wobbling-187au]] PT18-D23-001/002及GU22-D23-019/020补实际官方端点：265.6为2+→0+、405.1为4+→2+，414.4为另一个4+→基带4+的跨带ΔI0，550.9为6+→4+。它们可以处于一条实际退激路径，但不构成四条相同ΔI/同一band的直观signature阶梯。AuSP候选的半整数端点与此Pt整数端点是不同isotope假说，须保持各自完整network和实测门。

评价的2017Mu12能量/强度及DCO/POL是其引用层，不是新采集；2022Gu04 XUNDL又是Guo的同数据编译。尤其编译1636标8+而实际Guo图/2018评价为6+，应标source-layer失配而不是物理新ΔI4或实验自相矛盾终审。缺原2017全文与POL定义时只留literal字段，不填新P/δ/CI。

这让identity合同更具体，仍不能从partial记录缺某个门能量推Pt在Au门窗内贡献为0。需要原事件/γ分辨率、每个门的background/time/效率和全部必要伴随；当前不赋纯度/上限/机时。配置B槽另检H/operator/未定标量，核素重指派不混入。新needs_review:true。

## Day23：实际h9/2–f7/2成分需要不同的磁与电输入

[[guo-2022-low-spin-wobbling-187au]] GU22-D23-012/021与[[hamamoto-2002-wobbling-excitations-odd-a-high-j-aligned-particles]] H02-D23-005把012同l spin-orbit例推进到本Au模型实际出现的不同l内容。对标准单体μ=gl l+gs s，l3/f和l5/h之间没有直接矩阵；每个选定j block内则分别为gj,f=gl+(gs−gl)/7、gj,h=gl−(gs−gl)/11。这里不给gl/gs实际数值，也不把这些裸j态当已耦合转子的好I核态。

电四极角张量不同。声明C2q=√(4π/5)Y2q，有

$$\langle l'm'|C^2_q|lmangle=\sqrt{rac{2l+1}{2l'+1}}\langle l0,20|l'0angle\langle lm,2q|l'm'angle.$$

spin不变，h/f的Δl2角块允许；本任务角强度h9/2→f7/2约.017316、反向.021645，为dimensionless C2的平均平方和。physicalE2仍乘相应的未知⟨n'l'|r²|nl⟩及电荷；hh、ff、hf不预设同一径向尺度。九项CG/独立球面积分/投影/对称控制过，只证角块与归一。

因此实际混合核态的M1可来自各保l分量和core耦合，不能把bare cross-l零写成全band M1禁戒；E2的跨l相干项又依赖真实幅/phase/radial。换configuration assignment时，必须预先固定这些operators和radial/BCS/rotor条件，再对未用于定标的跨线相对量评分。只知图中dominant标签无法恢复完整幅，更不能挑某角因子判原QTR已失效或两解释同等可信。新增needs_review:true，无新g/δ/B/Q/τ/CI、率或机时。
