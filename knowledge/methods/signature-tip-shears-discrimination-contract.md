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
