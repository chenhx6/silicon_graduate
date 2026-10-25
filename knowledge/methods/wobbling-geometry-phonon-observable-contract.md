---
type: method
title: Wobbling几何、声子与四列观测量合同
aliases: [wobbling geometry phonon observable contract]
created: 2026-10-24
updated: 2026-10-24
status: ai-draft
review_status: unreviewed
method_type: collective-mode-identification
tags: [wobbling, phonon, alignment, evidence-matrix]
---

# Wobbling几何、声子与四列观测量合同

## Purpose

把[[wobbling-motion]]的几何定义、声子近似及实验观测分开检验。本文由Codex self-audit维护，所有新增推断保持待复核；不设置通用的绝对B(E2)门槛，不把能量斜率单独当几何测量。

## Inputs and Assumptions

先指定三条形状主轴s/m/l、惯量排序、准粒子组态及j取向，再映射数字轴号。[[frauendorf-2014-transverse-wobbling]] F14-D22-001将j平行最大惯量轴称longitudinal、垂直称transverse。H03的1轴与F14横向例子的1轴不同（[[hamamoto-2003-quantized-wobbling-excitations-alignments]] H03-D22-005）；其惯量安排也不同，单做符号换名并不能使两个模型等价。

应区分两类alignment：实验能量/Routhian曲线提取的准粒子对齐（须写reference和spin assignment），以及角分布/偏振分析的磁子态分布宽度σ/I。后者不是准粒子j沿某一主轴的直接测量。

## HFA局部重建与失效域

以下是对F14-D22-002公式的代数重建。取ℏ=1、角动量无量纲，Ak为MeV；固定J时：

\[
H=A_3(J_3-j)^2+A_1J_1^2+A_2J_2^2,
\qquad J_3=\sqrt{J^2-J_1^2-J_2^2},\quad J=\sqrt{I(I+1)}.
\]

在3轴附近展开给出两条曲率

\[
c_1=A_1-A_3(1-j/J),\quad c_2=A_2-A_3(1-j/J),
\quad\hbar\omega_{\rm HFA}=2J\sqrt{c_1c_2}.
\]

围绕yrast局部最小值须分别检查`c1>0,c2>0`。只看乘积为正也会容许两条曲率均负的能量极大值。第一激发的小角条件可写成

\[
\epsilon_{23}=\frac{3(c_1+c_2)}{2J\sqrt{c_1c_2}}\ll1.
\]

它是近似有效域诊断，不是实验置信度，也未给出一个普适的数值截断。横向粒子例子`A2<A3<A1`中，`c2→0`给出`Jc=jA3/(A3−A2)`，同时该小角条件发散。频率软化时必须重新检验近似，不能直接认作实验模式能量为零（F14-D22-002至004）。

### 有限自旋模型控制

可复现实现为`system/scripts/day22_frozen_alignment_domain.py`，运行时显式给`--output`。它在固定I表示空间量子化F14 Eq. (11)，用`m=-I,…,I`完整基底；保留固定j，**没有**完整QTR的内禀Hamiltonian、准粒子重定向、跃迁算符或实验响应，因此不能当F14原始QTR程序。

输入采用F14 Table I的135Pr fit惯量（1=l、2=m、3=s）`(4,21,13) ℏ²/MeV`，并显式假定`j=11/2`。计算得`Jc=14.4375`，由`J=√I(I+1)`对应`Ic≈13.9462`；这不是实测普适临界自旋。

| I | HFA能量/MeV | 有限矩阵最低两本征值差/MeV | ε23 | 有效域判断 |
|---|---|---|---|---|
| 19/2 | 0.52970 | 0.62514 | 0.6470 | ε未远小于1，不能声称精确声子 |
| 25/2 | 0.33658 | 0.56490 | 0.9310 | 软化时近似误差增长 |
| 27/2 | 0.19291 | 0.53342 | 1.5882 | 小角条件明显失败 |
| 29/2 | 3轴局部最小值消失 | 0.49632 | 不适用 | 不将虚频当负的实测激发能 |

本征值差均是本模型同I谱差，不是由相邻spin yrast内插得到的实验Ewob。有限矩阵的非零间隔也不能证明实际核的声子、隧穿或相变。五个独立解析/算符控制包括轴对称全谱、直接角动量矩阵构造、Casimir、对易关系及H03 Eq. (15)二阶差分；实际误差低于10⁻¹⁰，检验范围仅为实现与给定模型的关系。

### 有效域、惯量标度和模式判据的区别

以下为本任务从公式导出的条件结果。对正曲率`c1,c2`，AM–GM不等式给出`ε_n=(2n+1)(c1+c2)/(2J√(c1c2))≥(2n+1)/J`。这说明即使曲率最均衡，有限低spin也有不可忽略的小角近似下限；下限小并不保证实际ε小。该推导只适用于此谐近似，不是实际核素模式不存在的证明。

若所有惯量同时乘同一正函数`s(I)`，则`Ak→Ak/s(I)`、`ci→ci/s(I)`：局部HFA能量变为`ω/s(I)`，但无量纲ε和固定j的正曲率边界不变。因此共同spin标度能改变能量斜率，却不能单独修复小角条件。脚本中的longitudinal条件例子用`A=(.10,.12,.04)MeV,j=6.5,s=1+.5I`：I=10/20/40/80的局部频率由.31826降至.29962/.28893/.28318MeV，几何始终为j沿最大惯量轴；这只是任意指定标度的数学对照，未拟合实际核，也未声称其等同相邻spin实验Ewob。

[[lawrie-2020-tilted-precession-wobbling]] LAW20-D22-001/004的公式用I，须与F14的J=√I(I+1)区分。按其TableI(v)打印输入重建，正曲率边界20.46、n=1半整数网格最小f≈.48391；Matta原基惯量对应22.611和.46357。原表Imax及Fig9曲线不被这些条件结果自动认证，原producer未得。共同标度对f的相消已数值核到约10⁻¹⁶。两套输入保留，不把定性“f不小”当精确复现了所有图点。

[[frauendorf-2018-comment-wobbling-stability]] FC18-3/4强调FA近似临界点与完整PRM几何稳定性不同；[[tanabe-2018-reply-wobbling-stability]] TR18-2/3则要求I与R的量子化增量，并报告即使用13:21:4惯量延长稳定域仍未满足其判据。两文针对2017争论，早于Lawrie2020。归纳为三个分别待检验的问题：所选几何是否稳定；谐展开是否有效；能量/电磁矩阵元/角动量指标是否呈现相应phonon结构。不能用其中一个问题的通过替代另两个。

## Ratio identity and phonon test

`B(E2,out)/B(E2,in)`比较不同退激跃迁的约化强度；同一条M1/E2混合线有`fE2=δ²/(1+δ²)`，δ还带相位信息。不能用一个比值直接替代另一个。H03 Eq. (14)在特定极限下给出前者对γ的依赖比例于`tan²(γ+30°)`，不提供跨核通用常数（H03-D22-003）。

理想声子阶梯的能量与矩阵元标度须绑定相同自旋比较/插值方式和带身份。有限I非谐性允许相邻间距压缩：H03 Eq. (15)的无alignment轴对称极限给出`Δ²En=−2(A2−A1)<0`，且其实际163Lu拟合仍有未解释之处（H03-D22-002/004）。因此“非等间距”不能单独排除声子，“大E2+两带”也不能单独建立声子标签。

## checkpoint092 163Lu直接观测边界

OD01原文用electric偏振性质排除小根，但没有打印可引用的P正负号；没有在本篇测TSD2寿命。JE02观测四条TSD3→TSD2及八条TSD3→TSD1线，其中476可提两套δ/相对B；八条ΔI=2支路由非谐性解释。原表比值的重建与归一条件见[[interband-e2-strengths]]，原始出处见[[odegard-2001-evidence-wobbling-163lu]] OD01-D22-R092-1/2及[[jensen-2002-second-phonon-wobbling-163lu]] JE02-D22-R092-1至4。

### F14绝对M1输入的参考链仍未闭合

F14 Fig.19对绝对B(M1)的比较保留为作者引用/模型比较。其p.10指Ref.25，而p.12字面条目与[[jensen-2001-165tm-h9-2-configuration]]的165Tm原件相符；这未给出163Lu数据原始寿命身份。见[[frauendorf-2014-transverse-wobbling]] F14-D22-R092-1。该疑点既不新增Lu寿命证据，也不证明Fig.19数据错误；本任务不擅自补引用。

## Four-column evidence procedure

| Band energy | In/out strengths | Alignment | Polarization |
|---|---|---|---|
| 标明母末态、signature、spin及Ewob定义；写明实测能量与模型曲线 | 分开绝对B、相对B、光子强度和δ；列出分支、Eγ幂次、内转换与共同寿命/Cov边界 | 分开参考扣除后的i(ω)、J(2)、组态假设和σ/I；相近曲线支持共同结构但不测定进动锥 | 分开P与计数不对称A、Q(E)、几何校准、角度、门条件；保留δ双解及未测线 |

每个核素/带对须附：支持解释、最强反证/替代、必要伴随观测、来源依赖和触发改判条件。F14 Table II的Pr实验比来自Matta发表前通信，并非独立采集（F14-D22-005）；理论后文再次复引不能增加证据数。

## 原始实验四列证据矩阵

以下四行对应不同证据对象；2015/2022的135Pr是对同一候选带的两组资料（2015含两次互补采集，2022另有JUROGAM采集），不能把它们当两个新模式。支持与反证均保留。

| 候选带/出处 | Band energy | In/out strengths | Alignment | Polarization |
|---|---|---|---|---|
| 163Lu TSD2/TSD1，[[odegard-2001-evidence-wobbling-163lu]] OD01-D22-001至003 | 分离约250–300keV并随spin下降；九条连接线建立带关联 | 多线平均δ=−3.10(+.36/−.44)，E2光子份额90.6(1.3)%；43/2→41/2例λ=.36(.04)，相对强度比较为主 | Fig3相近i_x/J(2)；i_x用25ω+45ω³参考。σ/I=.25(.02)另属磁子态宽度 | electric偏振用于排除小模−.22根；没有在本文重放原计数/Q/Cov；多线平均不算多份独立实验 |
| 163Lu TSD3/TSD2，[[jensen-2002-second-phonon-wobbling-163lu]] JE02-D22-001至004 | 作为二声子候选讨论，存在明显非谐性；四条ΔI=1和八条ΔI=2连接 | 45/2母态476/627keV：λ=.14(.04)；大根rE2=.51(.13)，小根.019(+.024/−.017)。前者与TSD2平均.21(.01)的中央商2.43，不是严格同I全阶梯验证 | TSD2/3的J(2)和相对i_x相近、差约.1ℏ，支持共同内禀family | 476未测到偏振，实验不能选根；作者据PRM/带性质偏好大根，未完成偏振选解 |
| 135Pr side/yrast，[[matta-2015-transverse-wobbling-135pr]] M15-D22-001至003 | Ewob定义为侧带E(I)减yrast相邻I±1能量平均；先降后升 | 813keV rE2=.843(.032)、rM1=.164(.014)；747只列δ和份额，实验rE2栏空白；没有新测绝对寿命 | h11/2组态/TAC、spin相关QTR惯量及高spin组态改变；这些模型j取向不等于实验直接测量 | INGA A747=.047(.012)、A813=.054(.034)，与另一Gammasphere AD互补；A不是P；后一中央正值仅约1.59倍表列误差 |
| 135Pr bands3/1及4/3，[[lv-2022-evidence-against-wobbling-135pr]] L22-D22-001至004 | 新JUROGAM谱重组原TW2候选带；QTR对bands2/5能量仍过估 | 813.2/726同母态给rE2=.12(.08)、rM1=.4(.3)；747/526的.7(+.7/−.5)是通向bands1/2的两条带间支路；755无实测δ | QTR/10轨道/Harris输入推断j/I同步重定向，是模型结果；joint P-Rac同时拟合δ与σ/I，不直接测进动锥 | 新P-Rac给三条|δ|<1；P747中央+.04并不选大根；755未测P。主文P与SI Ap共用采集/校准，不重复计数 |

### 跨质量区主要候选核四列证据全景扩展总表（Master Four-Column Evidence Matrix）

checkpoint091：原068扩展表的全区终审、绝对B值、偏振符号与模式唯一改判撤回；上一节四行逐原文矩阵保留其逐线边界。新增可核的两准粒子对照如下。

| 候选带 / 原文 | Band energy | In/out strengths | Alignment | Polarization |
|---|---|---|---|---|
| 130Ba S1′/S1，[[chen-2019-transverse-wobbling-even-even]] CH19-D22-R091-1 | Fig.1比较两带能量与下降Ewob；惯量参数按能量调整 | Table I给同母态相对比，I13的rE2=.32(+.18/−.15)、rM1=.36(+.19/−.13)；不是绝对B | 模型πh11/2²，Figs.2–3为模型取向与RMS | 复用四角AD小δ；大δ未仅由AD排除，未新增本核偏振 |
| 136Nd L3/L1，[[lv-2022-transverse-wobbling-136nd]] LV22-D22-R091-1 | Eq.(4)/Fig.4下降Ewob；作者支持TW | 751线δ=−.48(+.13/−.14)，rE2=.36(.17)、rM1=.61(.29)；本篇不报告DSAM/绝对B | 两准粒子刚性短轴对齐j=10是模型输入 | 联合P–Rac仅一条；P=.02(+.04/−.05)，另外三条污染/弱；不得单由M1占优判剪刀 |

### 同一组实测能级保留下降曲线

[[lv-2022-evidence-against-wobbling-135pr]] L22-D22-005以其SI能级、并采用[[matta-2015-transverse-wobbling-135pr]] Eq.1的定义，给出下列中央值：

| Side-band I | E_side /keV | Yrast E(I−1),E(I+1) /keV | E_side−邻态平均 /keV |
|---|---|---|---|
| 17/2 | 1477.9 | 730.6,1390.8 | 417.2 |
| 21/2 | 2203.9 | 1390.8,2245.0 | 386.0 |
| 25/2 | 3000.3 | 2245.0,3245.0 | 255.3 |
| 29/2 | 3955.2 | 3245.0,4320.6 | 172.4 |
| (33/2) | 5067.2 | 4320.6,5164.7 | 324.55 |

最后母态spin的括号沿用原表；没有joint能级Cov，不造新误差条。此数据仍有先降后升的曲线，而Lv作者通过新的电磁观测提出TiP解释。因此能量形状本身不能解决两方的模式分歧。

还须区别同I理论谱差、F14基准图的yrast spline和Matta的相邻平均定义。若yrast恰为`A I(I+1)`，相邻平均比同I能量多A；因此相邻平均定义的Ewob比同I激发差少A。脚本以A=30keV的解析控制检验此偏置，不能把这个任意A数值当135Pr实测校正。

### 同母态中央值重建

`system/scripts/day22_strength_ratio_reconstruction.py`显式保存跃迁母末态、光子强度和δ。采用效率修正后的光子率、且分母按纯E2处理：

\[
\frac{B(E2;a)}{B(E2;b)}=
\frac{I_\gamma(a)}{I_\gamma(b)}\left(\frac{E_b}{E_a}\right)^5
\frac{\delta_a^2}{1+\delta_a^2}.
\]

δ定义对应光子率；当输入已是光子强度比时，不再重复乘内转换修正。若输入换成总分支率，则须先还原正确的radiative components。[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1给δ与矩阵元的单位合同；据`δ=0.835 Eγ(MeV) RME(E2)[eb]/RME(M1)[μN]`还可核同一混合线的M1/E2强度关系。

- JE02以图中整数能量476/627和λ=.14重建两根rE2为.5154/.01934，相应rM1为.00628/.08465，接近原表舍入值；这验证分支与能量幂次对应，未重建原误差。
- L22以813.2/726.0、Iγ=6.4/3.7、δ=−.37重建rE2=.11813及rM1≈.398，接近主文.12/.4；Fig4(d)消除表中多行排版导致的母态歧义（L22-D22-002）。
- L22的747.3/526.2以Iγ=9.4/.4、δ=−.47给.73597；526的E2分母是提取假定，SI表该多极性/Rac未列实测，不能写成独立确认的纯E2（L22-D22-001）。
- Matta813的rE2=.843与δ=−1.54给rM1=.16373。若只替换δ而固定其余2015输入，则rE2变.14431；份额敏感度因子5.84不是新旧实验绝对B塌缩，实际原表中心商.843/.12约7.03还包含各自分支/响应差异。

所有数字均是已打印输入的中心值算术，保留原作者区间，不新增联合CI、不平均不同采集、不虚构缺失的branch/δ或寿命。

### 反证与改判条件

#### 偏振和角分布的条件选解

747正P配小δ是原实验逐线结果，不是“任意负δ必正P”的定理；813中央P为负，两线不能混用（[[lv-2022-evidence-against-wobbling-135pr]] L22-D22-R095-1）。已知非零ρ4F4时A4可条件识别实数M1/E2混合比的模；未知独立张量可有正布居同角分布反例，不能等同Gaussian族或Pr实测两谷等深（[[yamazaki-1967-aligned-angular-coefficients]] YA67-D22-R096-1/2）。完整门、相位、a/Q、取向及联合误差决定实际分支证据，旧007/036“全参数精确扫描/跨阵列精确吻合”认证撤回。

“近简并+强E2”不足以单独确证wobbling phonon：大δ仅说明同一线的相对E2/M1光子份额，未给绝对集体强度；[[lawrie-2020-tilted-precession-wobbling]] LAW20-D22-002还指出一般TiP与其他带退激也可有大E2；保留这是作者给出的竞争解释，声子近似另需检验。135Pr两次独立采集给出不同δ结果，须比较相同逐线身份、角度、Q、gate与拟合假设；不能把它们称同一χ²面的两根（L22-19区分了旧AD重拟合与新P-Rac点）。

对TSD3，能改变判断的伴随量包括476的独立偏振/内转换或等效多极约束，以及同I、分母明确、带误差谱系的多级E2矩阵元；“未测偏振”保留不确定性，不等同已测反证。对135Pr，能改变判断的是共同响应/约定下重放原计数和δ-σ/I联合约束，并核实526支路成分与高spin组态混合；现有源页不提供完整原计数和jointCov。

## 跨质量区摆动运动判据对账（checkpoint091校准）

核素、组态、spin区间和电磁算符必须分别核验。163Lu是重要高spin基准；这不证明正常形变或两准粒子wobbling物理上不存在。原本节R/j、f通用数值和“伪模式铁律”撤回，详见[[wobbling-criteria-card]]。本次未完成全核区穷尽审查。

### 4. checkpoint072认证撤回（checkpoint091）

未取得逐核Cγ/Bγ出处或PES拟合。105/14.5/8.5/6等为自设输入；谐振子零点宽度公式也不能使0.5成为普适门限。保守闭合Hamiltonian本身不给耗散率。撤回四核刚度判决。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WOB-METH-072-1 | 原“定理”撤回；见本节边界更正，不作核素认证。 | task-correction | audit-only | checkpoint091 | true |

### 5. checkpoint073认证撤回（checkpoint091）

未核四核绝对寿命/全部多声子文献，不能声称全核区零确证；非谐性可产生有限Δn≈2强度（H03-D22-R091-1）。保留163Lu关键线偏振缺口，撤回38/1.42 W.u.及未来源化间距表。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WOB-METH-073-1 | 原“定理”撤回；见本节边界更正，不作核素认证。 | task-correction | audit-only | checkpoint091 | true |

### 6. checkpoint074认证撤回（checkpoint091）

冻结内禀j仍可在实验室系产生M1；F14 Eqs.(21)–(22)明确非零（F14-D22-R091-1）。撤回M1恒零、0.0035绝对基准及δ通用下限。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WOB-METH-074-1 | 原“定理”撤回；见本节边界更正，不作核素认证。 | task-correction | audit-only | checkpoint091 | true |

### 7. checkpoint079认证撤回（checkpoint091）

Pauli原理不唯一决定经典剪刀角或M1矩阵元；相同g因子双粒子的磁矩与总j关系也不能由差矢量公式替代。两原文保留M1占优的TW解释，未报告所列绝对B值或11倍塌缩。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WOB-METH-079-1 | 原“定理”撤回；见本节边界更正，不作核素认证。 | task-correction | audit-only | checkpoint091 | true |

### 8. checkpoint082认证撤回（checkpoint091）

旧ρ、Vres、壳隙均自设；黄金律需连续/稠密背景、弱耦合和时间尺度前提，不给这些有限核的实测宽度。撤回正常形变声子必融化结论。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WOB-METH-082-1 | 原“定理”撤回；见本节边界更正，不作核素认证。 | task-correction | audit-only | checkpoint091 | true |

### 9. checkpoint083认证撤回（checkpoint091）

AW13-20的871.2是Band1→4，非4→1；不同母态/表归一的强度不可合成46.6%退激分支。纯signature单声子两支的spin序列约束不等于所有混合多支带严格算符禁戒，更不唯一确证γ振动。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WOB-METH-083-1 | 原“定理”撤回；见本节边界更正，不作核素认证。 | task-correction | audit-only | checkpoint091 | true |

### 10. checkpoint084认证撤回（checkpoint091）

Matev可加性适用无配对选定组态集，不证明配对阻塞的任意低spin核。旧Qt=10.5/10.3、3.85/1.15等未绑定原寿命来源；撤回10%/20%及Δix=0绝对门限。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WOB-METH-084-1 | 原“定理”撤回；见本节边界更正，不作核素认证。 | task-correction | audit-only | checkpoint091 | true |

### 11. checkpoint087认证撤回（checkpoint091）

单带Harris灵敏度代数正确，但σJ0/σJ1/ρ是自设输入；共同参考在相同ω两带差中严格抵消。未核137Nd频差，不存在已证明伪造1–1.4ℏ的结论。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WOB-METH-087-1 | 原“定理”撤回；见本节边界更正，不作核素认证。 | task-correction | audit-only | checkpoint091 | true |

### 12. checkpoint089认证撤回（checkpoint091）

未做穷尽检索、未核各核寿命原文，不能由缺偏振推断唯一经验锚点或自然界只能TSD存在。167Ta是明确带假设的相对比推断，条件推断不自动构成逻辑循环。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WOB-METH-089-1 | 原“定理”撤回；见本节边界更正，不作核素认证。 | task-correction | audit-only | checkpoint091 | true |

## checkpoint091 可复核的算符与参考抵消

### 冻结内禀矢量仍可辐射

F14 Eq.(21)在FA/HFA中给出B(M1,n,I→n−1,I−1)=3n[j(gj−gR)x]²/(4πJ)。固定体固坐标的μ3，并不固定实验室系矢量：实验室分量仍随转动Euler角变化。对稳定曲率c1,c2>0，令α=J(c1+c2)、ω=2J√(c1c2)，有x²=(α/ω+1)/2≥1。因而n>0、j(gj−gR)≠0时该式为正；即使c1=c2、y=0，也不会导出这条向下跃迁的M1恒零。此处是原文模型公式的代数结果，不是新核素绝对B测量，也不能推出通用δ下限。来源：[[frauendorf-2014-transverse-wobbling]] F14-D22-R091-1。

### 公共Harris参考在等频带差中抵消

任务代数重建：对两带使用同一f(ω)=J0ω+J1ω³，Δix(ω)=[Ix,a(ω)−f(ω)]−[Ix,b(ω)−f(ω)]=Ix,a(ω)−Ix,b(ω)。因此在相同ω，公共J0、J1的不确定度对该带差的导数均为零，不能把两带的公共误差当独立误差相加。等频插值/频率标定的误差仍需另外传播。

若比较ωa≠ωb，参考贡献为−J0(ωa−ωb)−J1(ωa³−ωb³)，共同参数协方差的贡献才是gᵀΣJg，g=(−(ωa−ωb),−(ωa³−ωb³))。这与单带σ(ix)不是同一对象。本轮未取137Nd逐态频率和参数Cov，故不报告其“伪造多少ℏ”。OD01定义i_x参考与磁子态σ/I为两类对象，见[[odegard-2001-evidence-wobbling-163lu]] OD01-D22-002。

### Agent self-audit triage

P0：逐线分母/δ分支及A/P对象已按原件核清；仍缺原始计数/联合响应和共同Cov，保持限制，不发给用户作为待办。P1：H03/F14轴与模型版本差别、原表舍入误差、476与526伴随观测缺口均已显式记录。新增内容不继承旧页面human-reviewed资格，也不改变原有source flags。

## checkpoint093 定义、有效域与模型比较合同

| 问题 | Lawrie2020 | Chen–Frauendorf2022 | 本任务可检验范围 |
|---|---|---|---|
| wobbling词义 | 将其用于受限的harmonic-phonon近似，要求能量及跃迁对n量子化 | 将其用于完整TR/PTR的进动拓扑，可明显非谐；称对方TiP为其非谐wobbling | 先明确要检验的是严格谐声子、近似误差还是完整拓扑；名称不同不新增实验 |
| frozen j | 为隔离核芯倾斜，在该对照中冻结j | 完整PTR允许Coriolis重取向；HFA只是说明物理的近似 | 不把任何一方的简化实现泛化成所有QTR实现 |
| 小角诊断 | Eq.34检验所用参数下f≪1，Table I(vii)Lu横向组也不很小 | 小振幅/HO可过早预测不稳定；完整波函数仍可具TW拓扑 | f不小直接挑战对应谐展开，不自动抹去完整模型的模式解释 |
| 实验裁决 | 要检验声子式能量与矩阵元标度 | 要比较完整几何/电磁向量并容许非谐修正 | 对同一数据、Hamiltonian/算符/空间明确后比较未用来定标的预测，不能用名称投票 |

直接出处：[[lawrie-2020-tilted-precession-wobbling]] LAW20-D22-R093-1；[[chen-2022-study-wobbling-spin-coherent-state-maps]] CF22-D22-R093-1。定义分歧能解释部分争论，并不消除135Pr独立实验δ结果之间的真实不一致。

### Eq.34的条件下界与共同惯量标度

本任务代数：令c1=A1−A2′>0、c3=A3−A2′>0，则f(n,I)=(2n+1)(c1+c3)/(2I√(c1c3))≥(2n+1)/I。它说明低spin限制，但不是核素模式存在的充要门。正比例共同缩放Ak→s(I)Ak使分子和分母同缩放，f不变，ω按s(I)缩放；能量曲线变化不等于小角近似被修复。

按Lawrie打印Table I(vii)与其I约定，在I=13/2–85/2网格有f1最小≈.31599、f2≈.52665，不能混写成另一个longitudinal输入分支的.10–.18。脚本hfa-sss-controls-093.json只作参数/表示控制，不重跑完整PTR或实验CI。

### 过渡区退激通道与模型定义须一起检验

CF22特定135Pr完整计算的过渡区可有第三带→第一带增强的ΔI=0 E2，并不保留严格谐极限的所有支路规律（CF22-D22-R093-2）。这挑战“任意ΔI=0即排除所有wobbling”的任务规则，但不能反向证明127Xe或其他核符合该模型。应先绑定态身份及参数域，再比较竞争解释的逐线强度。

## What It Can Establish

能把几何定义、模型有效域和实验读取对象对齐，识别“一个观测支持的范围”与未检验假设。F14保留transverse解释，也承认M1及二声子增强的缺陷（F14-D22-006）；应把整套观测向量用于比较。

## What It Cannot Establish Alone

不能从近简并、下降Ewob、大E2混合比或相近alignment中的任意单项，得到唯一wobbling-phonon结论。也不能用有限矩阵或HFA的实现验证代替实际核素的寿命/偏振/组态证据。

## Sources

- [[frauendorf-2014-transverse-wobbling]] F14-D22-001至007。
- [[hamamoto-2003-quantized-wobbling-excitations-alignments]] H03-D22-001至005。
- [[odegard-2001-evidence-wobbling-163lu]] OD01-D22-001至003。
- [[jensen-2002-second-phonon-wobbling-163lu]] JE02-D22-001至004。
- [[matta-2015-transverse-wobbling-135pr]] M15-D22-001至003。
- [[lv-2022-evidence-against-wobbling-135pr]] L22-D22-001至004及L22-16至19。
- [[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1。
- [[fagg-hanna-1959-polarization-measurements]] FH59-1至3。
- [[lawrie-2020-tilted-precession-wobbling]] LAW20-D22-001至005。
- [[frauendorf-2018-comment-wobbling-stability]] FC18-1至4。
- [[tanabe-2018-reply-wobbling-stability]] TR18-1至4。

## Evolution Log

- 2026-10-24：H03/F14原件驱动的几何/有效域合同；有限自旋控制属于本任务模型推断，未增加实验事实、未晋升human-reviewed。

## Day22 checkpoint099：163Lu的SD–ND E2对照

[[domscheit-1999-triaxial-superdeformation-163lu]] DO99-D22-R099-1/2给出两个同为21/2+、相隔111keV的ND/SD1态。作者以带外426/697keV E2退激的两态混合解释约40%光子脱带，并据假设的算符矩阵元提取p和Q比；不是将SD1/SD2识别为声子阶梯。任务打印中心重建p≈.0387、V≈21.4keV、QND/QSD≈.4868，五项指定代数控制通过，没有新Cov/CI或绝对B测量。

这说明同核的强光子脱带、近能量态和E2连接也可有SD–ND混合解释；强度份额还需Eγ^5修正，不能等同约化B。原Q_SD=10.7(.7)b为Schmitz1993旧寿命引用，只约束该带/模型，不能搬给新SD2/3的绝对强度或当三次独立测量。原Schmitz全文未得，F14 Ref25字面疑点仍开放。needs_review: true。

## checkpoint106：HFA软化的有限spin四次势控制

按[[frauendorf-2014-transverse-wobbling]] F14-D22-R106-1/2定义人工族`A=(3A0,A0,2A0),j=J/2,J=√I(I+1)`。此时`c1=2A0,c2=0`，谐频为零。正J3分支展开为`J3=J−(J1²+J2²)/(2J)−(J1²+J2²)²/(8J³)+…`；冻结j哈密顿量有正四次项`A3 j(J1²+J2²)²/(4J³)`。令`q=J2/√J,p=J1/√J`，领先临界算符是`2A0J p²+(A0/4)q⁴`，不是无回复力的自由模式。

独立Fock基Galerkin算`p²+q⁴`最低两级隙为2.73931094（64/96基收敛）。有限spin矩阵I=10…160的`ΔE/[A0J^(2/3)]`趋近该值；完整最低隙为正，尽管局部HFA曲率零。模型中该隙与A0J相比逐渐小，说明需区分相对软化、近似失效和真实能隙零。五项指定控制通过。

本族只作条件数学检验，j随I改变并非真实固定qp；不赋核素/声子阶梯，不算真实B或反演相变。体固对易符号在本横向平方算符模型的谱等价不影响该例，但不能据此免除一般相位约定。数值程序day22_frozen_critical_quartic.py保存输入和边界。needs_review: true。

## checkpoint107：K标签与等价γ扇区不是新物理模式

[[sheikh-jehangir-bhat-2024-tpsm-wobbling]] SHJ24-D22-R107-1–3把投影K、最后混合态及轴约定分开。以`qk=cos(γ−2πk/3)`定义主轴四极特征值，`γ′=−120°−γ`仅交换q2/q3；proper旋转`R=((-1,0,0),(0,0,1),(0,1,0))`给相同无向主轴形状，二/三阶不变量不变。惯量矩阵A、角动量I/j和跃迁张量须一起旋转：`(I−j)^T A(I−j)`才保持相同能量。若只改γ标签、不变换其余对象，就不是已验证的同一物理输入。

K可在投影基中标记分量，但一般三轴H不与某固定轴J3对易，最终配置/K混合态不由一个K数独立识别。short/long量子化轴互换不能当准粒子实际转向或TW→LW相变。四项角度/不变量控制通过，不认证实际TPSM producer或把固定basisγ当实验刚度。F24-D22-R107-1另提醒：多声子矩阵元的“增强/受抑”必须说明绝对B还是各自in归一比，不能将文字读成缺测/零通道。needs_review: true。

此处γ是形变参数扇区；SHJ24 Eq9欧拉旋转的同名字母γ另指取向角，不可混作物理形变变化。

## Day22 checkpoint109：声子代数是局部近似，基占据不等声子标签

以通常spin约定`[J1,J2]=iJ3`作任务代数练习，定义`nK=I−m`、`b=J+/√(2I)`。精确有`[b,b†]=J3/I=1−nK/I`及`abs(⟨nK−1|b|nK⟩)²=nK[1−(nK−1)/(2I)]`。有限矩阵任意commutator的trace为0，故不能在整个有限spin空间精确等于单位阵；低占据局部仍可近似boson。这一全局事实并不否定核内有效phonon。

I=13/2时，b的2→1/1→0平方矩阵元比为1.84615；I=45/2时为1.95556。四组矩阵控制验证对易式、trace和有限ladder修正，最大误差约浮点舍入。这是单一I表示内的scaledJ矩阵元，**不是**跨I核E2跃迁或实测二声子B的修正公式。

nK不是自动等于Bogoliubov对角化后的wobblingphonon数nw；映射还受挤压/非谐项和算符影响。体固总J的对易号须按[[frauendorf-2014-transverse-wobbling]]的约定映射；本练习不直接迁移相位或电磁算符。[[hamamoto-2003-quantized-wobbling-excitations-alignments]] H03-D22-002/004的有限I非谐性和F14-D22-R106-1/2的临界四次项说明应分别核能量阶梯、局部代数与真实跃迁强度，不设统一数值有效门。needs_review: true。

## Day22 checkpoint112：静态g的独立标量约束与几何边界

以下是本任务定义的单一量子j+core模型练习，不是F14或TI19的新g测量。取`I=R+j`、`μ/μN=gR R+gj j`、ħ=1并定义`gI=⟨μ·I⟩/[μN I(I+1)]`，则

`gI=gR+(gj−gR)⟨I·j⟩/[I(I+1)]`，

`⟨R²⟩=I(I+1)+j(j+1)−2I(I+1)(gI−gR)/(gj−gR)`，后式只在gj≠gR且单j/算符模型可信时可用。若gj=gR，gI恒为gR，不能反演核芯几何；接近该极限时问题病态。

独立CG²耦合基核I=j=11/2、R=0/2/4和chosen有理g，磁矩投影期望与该标量式精确相等。R分布`(1/2,1/2,0)`及`(17/20,0,3/20)`有同⟨R²⟩=3及同g=834/715，但分布不同；由均方矩构造的Reff≈1.3028不是确定R量子数。五项exact归一/CG/反演/奇异域/混合控制通过，所有g参数均为人工模型输入。

因此g可在限定模型下补充对粒子/核芯耦合的约束，却不重建三轴取向、进动锥或chirality。[[frauendorf-2014-transverse-wobbling]] F14-D22-R091-1的动态M1含gj−gR、[[timar-2019-transverse-wobbling-105pd]] TI19-D22-R103-3的geff按一条动态δ定标；不能自动把该动态淬火参数当已验证的静态g算符。实际多轨道、pairing/core polarization及g参数误差需另检，不把R≈I−j当量子几何。needs_review: true。

实际测量的迁移还受状态寿命和配置限制：[[grodner-2018-128cs-chiral-g-factor]] GR18-D19-5在128Cs的两odd核子+core三矢量模型下解释g，不能用上述单j式直接替代；原文也要求ps高spin态采用不同于56ns带头TDPAD的技术。本轮只定向复核该文PDF3–5/Eq2–3与结论，不重标g或外场校准。
