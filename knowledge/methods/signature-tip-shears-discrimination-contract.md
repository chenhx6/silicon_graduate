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


## Day23：186Pt核芯参考B(E2)与定标输入交叉核验

本节为可复现的任务量化核验（程序`system/scripts/day23_core_reference_b_e2_audit.py`，产物`core-reference-be2-006.json`），needs_review: true。

| 量 / 来源 | 能量与寿命输入 | 导出 B(E2) [e²b²] | 导出 W.u. | 来源与对账结论 |
|---|---|---|---|---|
| 186Pt 2+→0+ (IAEA 2022/2026) | 191.53 keV, T1/2=240(20) ps, α_tot=0.417 | 0.645(+0.059/-0.050) | 102.3 W.u. (表列 102) | ENSDF 采用值，源自 Batchelder 2022 评估 |
| 187Au 13/2-→9/2- (IAEA 2008/2026) | 233.4 keV, T1/2=56(5) ps, α_tot=0.224 | 1.194(+0.119/-0.098) | 187.6 W.u. (表列 188) | ENSDF 采用值，源自 Basunia 2009 评估 |
| Guo 2022 PLB p.3 引用范围 | 引用 Baglin 2003 与 Basunia 2009 | 0.63–1.27 e²b² | 100–200 W.u. | 明确包络了 186Pt (102 W.u.) 与 187Au (188 W.u.) 的采用值 |
| Sensharma 2020 PRL p.4 | 引用 Baglin 2003 | 0.84 e²b² | 133.2 W.u. | PRM 形变定标所用数值，比 0.645 高出 1.30 倍 |
| Sensharma 2021 thesis p.128 | 同引 Baglin 2003，伴随 13/2+ 正宇称笔误 | 1.44 e²b² | 228.3 W.u. | 比 2020 PRL 数值高出 1.714 倍，两者文字差未闭合 |

核验证明：
1. Guo 2022 所称“100–200 W.u.”是对 186Pt (102 W.u.) 和 187Au (188 W.u.) 评价寿命强度的客观包络，与 IAEA ENSDF 数据严格相符；
2. Sensharma 支持方 PRM 模型选择 β=0.23 的依据是使计算 B(E2) 符合核芯参考值，但作者在 2020 PRL 中写 0.84 e²b²，在 2021 学位论文中写 1.44 e²b²，相差 1.71 倍，且学位论文将 h9/2 跃迁印为 13/2+→9/2+ 正宇称；
3. 无论是 0.84 还是 1.44 e²b²，均不等于从 T1/2=240 ps 严格导出的 0.645 e²b²，表明存在未说明的寿命修正、转换截断或上/下跃迁约定差异。在统一模型比较前，禁止在不同计算间混用核芯 B(E2) 尺度。
