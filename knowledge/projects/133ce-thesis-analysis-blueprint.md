---
type: project
title: "133Ce学位论文深入学习与数据分析蓝本"
aliases: [133Ce thesis analysis blueprint, Wakudyanaye深入学习]
created: 2026-10-26
updated: 2026-10-26
status: active
review_status: unreviewed
confidentiality: public
project_stage: source-grounded-deep-learning-and-bounded-analysis
nuclei: [133ce, 131ce, 131ba]
tags: [thesis, deep-learning, spectroscopy, qtr, analysis-blueprint]
---

# 133Ce学位论文：持续深入学习与实际分析蓝本

## Agent active summary

本项目继续作为133Ce实际分析蓝本，不能以source/译稿完成结项。Day24先完成手征主卡原件与逐伙伴证据图的高价值工作，再推进本页“有限all-detector门的接受度练习”；13/8clovers的actual run仍待ledger。新推断needs_review:true，不改变既有Band5用户审核、raw或模型actual输入边界。

## Research Question

怎样把[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]的实验分析、signature/Coriolis机制和QTR电磁检验真正转为可迁移的研究能力，并为用户尚未完成的分析提供步骤、输入及失败检查？用户明确要求像[[alwaleedi-2013-band-structures-131ce]]支撑其131Ce分析那样严格对待；这是整体知识的重要补充，不能以source建页/普通摄入或一次summary结束。本轮主体仍是Day23；本项目不另启课程卡、不自动替代主课学分。

用户独立实验event和未公开拟合本轮未读取；原开题材料仅用于识别相关研究问题，未复制全文，也不将用户称重合度超过80%写成测得文本相似度。

## Current Hypotheses

|问题|当前可以支持的解释|竞争/边界|
|---|---|---|
|g7/2正宇称Band2的S|三轴性和邻s1/2/d3/2的Coriolis混合共同影响|固定χ的γ偏好不等于唯一形状测量，更不等于γ-rigid|
|h11/2负宇称Band1/4|作者九轨道QTR/TiP比较有部分能量/S与rE2支持|FA连接δ较近，两模型rM1趋势都与实验不同；不认证“全观测通过”|
|configuration替代|保持实测计数/能级和响应不变，改变候选态与模型本征态的组态映射，比较全链接网络|若改算符、形变和定标则已额外改模型；若只重命名则无新可检验内容|
|是否wobbling/MR/AMR|需按[[signature-tip-shears-discrimination-contract]]共同观测向量逐项比较|小δ不能唯一指定MR/TiP；不恢复跨核δ/W.u.硬门|

## Evidence Available

主source WK22-01–28提供原件定位与分层。所有新分析needs_review:true；“核过原字面”不等于实验/模式认证。正文主线已读，关键实验/模型图表已核；正文Ch1–7/前置逐段对照现已齐备，目录/参考保留原件；深入学习继续。


### 逐量、母态与未闭合矩阵


原件SHA及读区见 `alignment_matrix.md`；仅局部self-audit，所有尚未解释的不闭合保留。图点约数是视觉量级读数，未作精确digitization；不能与表值平均。原件裁切精确页/坐标见 `visual_crop_manifest.json`。

## 实验三线与两种分母

Table5.2/PDF67给出的实际γ能量用于同母态身份；Table6.11/PDF112使用整数标签625、582、465，不据标签差异创建第二条线。

| ID | 母态与主出口（Band4→Band1） | δ原字面值 | out/out的E2分母 | out/out：[rE2,rM1] | out/in的E2分母 | out/in：[rE2,rM1] |
|---|---|---|---|---|---|---|
| C133-EXP-625 | Ex832.0，13/2−→11/2−，624.6keV，Iγ3.3(4) | −1.5 +.97/−5.7 | 同母态→Band1 9/2−，794.8keV E2，Iγ8.0(14) | [1.15 +.48/−.79, .14 +.21/−.13] | 无Table6.11条目 | [—,—]，**不能补0** |
| C133-EXP-582 | Ex1409.8，17/2−→15/2−，582.7keV，Iγ3.53(25) | −.55 +.12/−.25 | Table6.11未显式命名；当前Table5.2/Fig5.1未提供相同母态17/2−→Band1 13/2−的可直接确认ΔI=2行 | [5.06 +3.45/−1.66, 3.95 +.39/−.81] | 同母态→Band4 13/2−，577.8keV，Iγ3.22(21) | [.33 +.28/−.13, .25 +.03/−.05] |
| C133-EXP-465 | Ex1809.1，19/2−→17/2−，464.4keV，Iγ1.89(18) | −.17 +.09/−.2 | 同母态→Band1 15/2−，982.0keV E2，Iγ1.95(17)，作为待核分母候选 | [1.06 +3.49/−.82, 5.54 +.12/−.53] | 同母态→Band4 15/2−，608.3keV，Iγ1.89(18) | [.09 +.34/−.07, .47 +.01/−.04] |

单位：rE2为无量纲；rM1为 μN²/(e²b²)。out/out和out/in不能混列为同一“B比”。上述out/out分母候选按带身份给出，尚未取得作者实际强度/转换校正producer；尤其582这一格保持missing。

## 确定可以做的条件算术

按论文Eq3.24/印37/PDF48，`δ²=.7 Eγ² B(E2)out/B(M1)out`；实验同一分母的打印比值给约束 `δ²≈.7 Eγ² rE2/rM1`。`bounded_checks.py`实际执行并输出JSON。

| 线 | δ中央值的E2光子份额 δ²/(1+δ²) | Table6.11 out/out闭合所得δ² vs 原δ² | Table6.11 out/in闭合所得δ² vs 原δ² |
|---|---:|---|---|
| 624.6 | .69231 | 2.24322 vs2.25（约−.30%） | missing |
| 582.7 | .23225 | .30447 vs.3025（约+.65%） | .31373 vs.3025（约+3.71%） |
| 464.4 | .02809 | .028885 vs.0289（约−.05%） | .028909 vs.0289（约+.03%） |

这说明这些表列复用同δ与强度分支；差异仅作打印/单位/依赖诊断，不给显著性。**正文印100/PDF111称582有“约30%”E2，按−.55中央δ重算为23.2%**；不是30%的独立测量。δ端点区间的单调映射保存在JSON，仅是打印端点像，不是新置信区间。

以Table5.2打印Iγ/能量、Table6.11中央δ、同parent纯E2分母为条件（效率校正光子yield、门/污染一致且相对归一可消去）：

| 线 / 分母类型 | 条件重组 [rE2,rM1] | Table6.11打印 [rE2,rM1] | 判断 |
|---|---|---|---|
| 624.6 /794.8 out/out | [.95280,.11564] | [1.15,.14] | 中央summary不完全相等；原强度/δproducer和Cov缺失，不解释为显著冲突 |
| 582.7 /577.8 out/in | [.24408,.19177] | [.33,.25] | 同上；不靠误差条重叠宣布“通过” |
| 464.4 /608.3 out/in | [.10831,.56577] | [.09,.47] | 同上；608.3/608.7近双峰尤其需实际gates |

这里τ相消，无需ICC额外因子是**直接光子部分衰变率比**的条件；如果输入Iγ是总转换校正强度而非光子yield，需恢复对应(1+α)口径。得到绝对B必须另有τ和完整BR/ICC；本任务不从这些比值反演寿命、绝对B或CI。

## 模型与图表原字面值

| ID | 来源 / 模型 | I=17/2− δ,rE2,rM1 | I=19/2− δ,rE2,rM1 | 视觉图像 |
|---|---|---|---|---|
| C133-MOD-QTR | Table6.9/PDF111，9轨道 | −2.24,.75,.01 | −2.72,.32,.03 | Fig6.16(a)/PDF114黑点约.10,.03；第一rM1与表差约10倍量级 |
| C133-MOD-FA | Table6.10/PDF111，单轨道18 | −.49,.44,.19 | −.49,.11,.062 | Fig6.16(b)/PDF114绿色点约.044,.011；rE2与表差约10倍量级 |

Table6.9/6.10还各列13/2−→11/2−的δ=.89/−.58，但两r缺失。其父态模型能量、实际operator/transition output不齐；不能用实测625/582/465替作者模型Eγ宣判代数错误。

把打印三元组代入 `Eγ=sqrt(δ² rM1/(.7 rE2))`只得“所需一致性目标”：QTR17/2为.30915MeV、19/2为.99542MeV；FA17/2为.38486MeV、19/2为.43969MeV。这些**不是模型预测、实验测量或恢复的实际作者输入**。它们规定应向actual producer检查哪种能量/单位/矩阵元定义；也不能用Eγ目标逆向“修正”表或图。

## 原子审计状态

| ID | 已核文字/视觉 | 状态与下一必要输入 |
|---|---|---|
| C133-A01 | Table6.1/PDF77 Ce正宇称ε4=.1；正文=.01 | actual input-card missing；两值各保留；负宇称ε4=.015不受此字面冲突自动波及 |
| C133-A02 | Table6.9 rM1首点=.01，Fig6.16约.10 | table/curve internal mismatch，actual transition output missing |
| C133-A03 | Table6.10 rE2=.44,.11，Fig6.16约.044,.011 | 同上；不可自行选用小10倍图值 |
| C133-A04 | Fig6.16(b) caption in/out倒置，图轴/正文out/in | 字面in/out冲突已核；不能按caption反转实验母/末态 |
| C133-A05 | Table6.11三线δ与两率大体代数相关 | 不能把δ、rE2、rM1作为三次独立拟合约束；原Cov missing |
| C133-A06 | Table5.2的Iγ重组不同于Table6.11中央结果 | summary-lineage mismatch open；未做显著性检验；需实际gate/背景/效率/所选分支/转换口径 |
| C133-A07 | PDF113 FA跨带δ较近；PDF114两模型rM1趋势均错 | 保留分项失效；不得总称“TiP所有观测通过” |
| C133-A08 | 582 out/out分母未能由现有Table5.2确认 | identity missing，不以相邻state补齐；需作者transition ledger |
| C133-A09 | δ²份额使582中央23.2%而正文“∼30%” | 条件算术已执行；不把近似散文当额外实验 |
| C133-A10 | Table6.3/PDF82 9/2+行振幅字面.982,−.202,+.185；caption声明贡献为振幅平方 | 父代理先发现、本worker独立visual回核；在所述正交basis/归一态假设下，仅三项平方和1.039353>1，甚至按末位±.0005舍入最小和仍>1；不能靠截断遗漏补回归一。actual producer/basis convention缺失，不改.982、不静默重归一 |

所有新解释保持 `needs_review: true`；“已核”仅指对应字面/视觉位置，不表示整篇论文、模式标签或用户数据分析通过。

## Risks and Blockers

缺原event与run ledger、sorting与逐门背景/peak fit、效率及共同归一Cov、AD/P response和δ所有根、模型版本/输入卡/完整波函数/transition output。582 out/out分母没有直接身份；Tables6.9/6.10与Fig6.16不能凭中央值任选一边。未取得用户数据不等于用户没有这些数据；这些是本轮可用输入的边界，不自动变成用户待办。

## Analysis or Reasoning

### 四能级S与重复计权

原Eq2.37可写为

$$S_I=\tfrac12 E_{I-2}-\tfrac32E_{I-1}+\tfrac32E_I-\tfrac12E_{I+1}.$$

即$S=LE$，$\mathrm{Cov}(S)=L\mathrm{Cov}(E)L^T$。相邻S共享能级；若能量进入拟合后又把S当独立数据，联合向量$(E,S)=(1,L)E$有冗余。它们能以不同图形暴露不同spin结构，却不能增加独立实验维数。所有旋称劈裂定义必须先核原式，勿与$E_\gamma/(2I)$混用。

依据Tables5.1/5.2重建Band1/4后，Band1的I=13/2到29/2可用S中央值依次182.10、−216.15、277.30、−318.60、345.25、−342.50、351.35、−369.60、410.30keV；Band4 I=17/2到25/2为−175.05、49.60、100.55、−166.80、247.65keV。9/2−的37.2keV由表边推得，33/2−缺态不插值；不提供没有Cov支持的实验误差条。这是原表中央值练习，未重分析event。

### 同母态强度比的可识别输入

令混合线a的效率校正光子yield为$Y_a$，同母态纯E2线b为$Y_b$。若峰分解、门接受度与归一一致，$u=Y_a/Y_b$，则

$$r_{E2}=u\frac{\delta^2}{1+\delta^2}(E_b/E_a)^5,$$

$$r_{M1}=0.7 E_a^2\frac{r_{E2}}{\delta^2}=\frac{0.7u}{1+\delta^2}\frac{E_b^5}{E_a^3}.$$

第二式用论文Eq3.24，此式$E_a,E_b$均以MeV、B(E2)以e²b²、B(M1)以μN²；δ=0处须用第一式消去δ²的连续极限计算rM1，不能数值0/0。若输入yield已作conversion总强度校正，先恢复其光子口径；无同母态则τ不能相消。绝对B另需τ、完整分支与ICC。$\delta,r_{E2},r_{M1}$在固定$E_a,E_b$与reference身份后依赖两个基本输入$(\delta,u)$，至少一个代数约束，不能当三份独立测量。

### QTR的交叉项与磁算符

从原Eq3.14逐轴展开$R_k^2=(I_k-j_k)^2$，保留$-I_kj_k-j_kI_k$交叉项和$j_k^2$。在相应可交换表示里可写$-2I_kj_k$；不能像背景Eq2.24字面少写一倍交叉项后直接编程。Coriolis attenuation是对指定耦合项的处方，需实际输入确认，不等于将所有H或g缩放。

Eq3.22以$R=I-l-s$重写为$\Gamma(M1)=g_R I+(g_l-g_R)l+(g_s-g_R)s$（保留作者的算符归一合同）。总I生成元不连接不同I表示；跨I的M1来自相对磁矩项及态之间矩阵元。冻结一条内禀j或一条轨道不能据此推出所有M1为零。实际B计算仍需完整带符号波函数、BCS因子、算符单位与轴约定，三个主成分平方不能恢复干涉。

### 组态重指派的可证伪问题

在冻结125Te+12C实验的计数、能级、spin/parity和响应后，若把Band4从主要轨道18加额外芯转动的候选，改映到近Fermi的另一负宇称轨道所生的orbital-excited带，能否在不重调g/Q/惯量的同一模型合同下，同时描述624.6/582.7/464.4的δ符号与spin趋势、带内M1/E2及跨带ΔI2分支？这是待计算的替代解释，尚无量化预测，不能称与原模型等可信。

先用能量和明确的一组定标量冻结合同，留未用于定标的双向links、完整branch或已有独立磁/四极观测检验；若只按rE2单一比值选模型，无法检验rM1趋势失配。需要完整模型本征态/算符输出、共同实验Cov和line ledger；不编造δ、Q(E)、τ或设施率。该问题连接Day23的B槽，同时133Ce作为独立案例保留自己的实验身份。

## Learning Decision

已形成比普通摄入更具体的学习工程：有来源化母末态矩阵、内部不闭合、S中央值/设计矩阵、强度依赖推导、模型合同和替代解释检验。当前decision=limits-and-refines：强化分析流程和逐量判断，不认证任何普适模式；继续完成逐段reader、有限模型组件及实际输入可追溯性。

## Next Actions


此稿落实用户最新澄清：Wakudyanaye 2022 的133Ce硕士论文是整体研究知识和实际分析蓝本的重要补充，含用户尚未做而论文已示范的分析。它应像131Ce《Band structures of 131Ce》一样持续支撑数据分析、推导和反证训练，不以“一次摄入/summary完成”作终点。当前主任务仍是Day23 signature/wobbling/TiP/MR/AMR；本合同不另启课程卡或声称今日已完成长期课题。

## 问题绑定和阶段交付

绑定开题报告P52/P59：131Ba/133Ce/135Nd `νh11/2` 非晕结构和S相位演化的机制；P53：低自旋新结构；P54：强γ的P/AD/δ；P41/P59：γ软硬与进动/振动竞争。所有研究练习保留原始obs、派生量、模型输出和我们的推断四层。

| 学习单元 | 必须实际做出的工作 | 反证/失败练习 | 完成后留下什么 |
|---|---|---|---|
| A 原件/带/谱线身份 | 重建Band1/4节点边表；把Tables5.1–2、Fig5.1和选门文本逐项对齐；检查能量闭合 | 608/609双峰使并行路径出现在同gate，故单门见峰不足以建立唯一link；将一个终态误标后验证哪些强度比立刻失效 | 带/母态/终态/门/误差/谱系manifest，不靠band编号跨文合并 |
| B S(I)与signature | 由Eq2.37推导四能级线性组合，重算Band1/4各可用spin的S；若无Cov则只出中央值和缺口 | 固定能谱，改变spin/带归属会否伪造phase reversal；验证S是派生量，重复纳入χ²会重复计权 | 原能量→S的线性矩阵及条件Cov，不作模式认证 |
| C AD/P与δ | 从探测器角度/选门/取向/有限几何到Wθ，再到实测不对称与Q；保留所有允许根 | 同一δ²给相同率却偏振干涉项可异；改变gate/背景或Q迁移时检查选根稳定性 | 真正需要的计数/response输入表；若actual data未齐，只有条件练习 |
| D 强度与依赖 | 推导同parent τ消去、Eγ幂、δ²拆分与单位；重组Table6.11并与Table5.2核对 | 故意混out/out与out/in、将相对Iγ当绝对B、把δ和两派生率计三次；应被身份/维数/秩检查抓住 | `bounded_checks.py/json`本地已开始；下一步actual输入闭合，不编统计CI |
| E QTR空间与近似 | 写清GAMPN→ASYMO→PROBMO输入/输出；从Hcoll=Σ(Ik−jk)²/2Jk识别cross terms及j自由度；逐行检查basis、系数归一 | 仅限制一条Nilsson轨道是否真正冻结所有j方向，和完整九轨道/高自旋HFA差别分别检验；Table6.3/PDF82 9/2+三振幅平方和1.039353>1，在所述正交basis下不闭合，不擅改或重归一 | 可复现Hamiltonian/空间/轴/算符合同；没有作者producer时不叫复现 |
| F γ–Coriolis可辨识性 | 正宇称g7/2控制线扫描γ、χ、邻轨道能差及惯量；负宇称单独参数；定义能量与电磁holdout | 使不同γ/χ同时拟合S，检查哪些未定标量能分开；固定γ最佳值不等于测得γ刚性 | 参数退化和holdout预测矩阵，不能跨组态套γ |
| G 逐量模型优劣 | 预先冻结训练量与holdout，分别列能量、S、δ、rE2、rM1，不用summary结论投票 | 全空间能量/S较好但跨带δ差，FAδ近但能量/S差；两模型rM1 spin趋势错，能否找到共同失效参数/模型假设 | observable-by-observable残差、actual模型误差/响应缺口；表–图冲突保留 |
| H γ软硬、振动与MR/AMR | 提出γ-soft/γ-rigid/particle-core、vibrational、signature/Coriolis、TiP以及shears候选的共同可检验向量 | 小δ不等于MR，固定转子不预测动态γ软度；寿命、完整branch、静态矩/其它结构观测是否能提供独立量 | 原则上可分预测和最小补测/补分析；没有量化预测不承诺一次观测排他 |

## 用户现有数据分析的迁移合同

这三列区分“可以学习的步骤”“尚缺输入”和“不能直接搬用的数值/判断”。用户原始数据本轮未读取，不能把论文中的实验过程写成用户实际已完成。

| 可迁移的实验分析步骤 | 尚缺的实际输入 | 不可直接跨核/跨run套用 |
|---|---|---|
| 原event排序、particle gate/反应道纯度、2Dγγ/3Dγγγ符合构建 | 用户数据manifest、runID、反应、timestamp、触发/死时间、particle PID/效率、sorting版本 | 不能把GALILEO EUCLIDES/NeutronWall道选择当AFRODITE或用户阵列现成筛选 |
| 能量/效率校准、各角Doppler校正、门和背景侧带 | 用户source runs、峰表、增益漂移、角度/速度、efficiency误差/共享Cov | 不搬57/65MeV、Te/Au厚度、13或8-clover配置、相关rAD参考值 |
| 从互符合/反符合、cascade能量和相对yield建/扩纲图 | 用户逐门谱、peak-fits、双峰分解与污染、上限/缺测 | 不搬133Ce Band4等标签到131Ce Band4；不以同spin差推同带身份 |
| AD/DCO/Rac/P共同提多极/δ | 实际角组与acceptance、reference transition、取向/feeding、a/Q/plane convention、所有roots | 不搬另阵列Q、R_DCO≈.5或R_AD≈.8/1.3作通用硬门；不以论文缺P说明用户也无P |
| 同parent branching→relative B比，τ+BR→absolute B | 实际同parent line ledger、光子/总强度口径、conversion、τ定义与response | 不搬Table6.11δ/误差、tau、g或Qt；不同parent寿命不能相消 |
| S、J(1)/J(2)、alignment/crossings等spin演化比较 | 目标能级/Jπ、参考参数/ω定义、缺态/交叉窗 | 不搬g7/2的γ/Coriolis参数解释h11/2，也不搬133Ce的J0/J1到131Ce |
| 候选模式预先规定模型、训练量与holdout | 目标核PES/core、空间、Fermi/pairing、算符、实际代码和输入卡 | 不因133Ce论文“TiP”就标签用户的低自旋带；MR/AMR需要专门几何和绝对强度比较 |

## 131Ce现有工程可借鉴的结构（本轮只读定位）

1. `knowledge/sources/alwaleedi-2013-band-structures-131ce.md`：Key Results AW13-9（line91）保留δ=0派生比；AW13-16/19/20/21/22（lines98–104）分开611.1、504.9、871.2、538.3、994.3、1108及其同parent分母；line132汇总table/figure/prose交叉定位。可复用的是**先身份、后observable、再模型**，不能把131Ce具体线表搬到133Ce。
2. `knowledge/projects/131ce-collective-mode-discrimination.md`：line139的band/transition manifest；line155公共来源seed；line198的same-parent E2条件重算；line214的互向Band1/4链接与四阶段检验。该项目已显式区分论文数据和用户独立实验，延续这一约束。
3. 131Ce已有模型比较、lifetime/Qt及source-lineage是结构参照；现有页面的review标签不替代133Ce当前逐量审核。133Ce新工程应新增自己的独立source和model-input manifest，而不是把新论文塞进旧结论。
4. 本轮仅为定位打开上述canonical页面相关部分，未重读131Ce原始PDF，未改canonical/Git，未读取用户独立数据。

## 当前立即可推进的路线和未完成边界

当前最高信息路线是`atomic_matrix.md`中A01–A10：先找Table6.9/6.10与Fig6.16、ε4表–正文和Table6.3归一的actual输入/输出；并在同一母态账本下核Table6.11的out/out分母，尤其582keV。只用打印中央值做的条件算术已保存；真实δ根拟合、Cov、绝对强度和模型Eγ未恢复。

随后完成h11/2 Band1/4能级→S的有界重算与wavefunction/空间练习，再以g7/2线理解Coriolis/γ退化，逐项提出实际数据可做而用户尚未做的分析。每个阶段只在真实输入和验证达到合同后标完成；完成全文阅读、一个checkpoint或一次摄入均不表示长期学习收束。

## Linked Sources

- [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-01–28为本工程直接原件边界。
- [[ding-2021-131ba-133ce-signature-splitting]]为正宇称同源论文；[[alwaleedi-2013-band-structures-131ce]]和[[131ce-collective-mode-discrimination]]为分析工程参照，未把旧review状态转移到本工程。
- [[frauendorf-2014-transverse-wobbling]]、[[chen-2019-transverse-wobbling-even-even]]保留支持链；[[lv-2022-evidence-against-wobbling-135pr]]、[[guo-2022-low-spin-wobbling-187au]]保逐线反证和独立性边界。


## 单轨道投影、经典冻结与变分比较的三个边界

来源动机为[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-18/29；selected lab单$j=11/2$、$P=\mathrm{span}\{|m=9/2\rangle,|m=-9/2\rangle\}$，$Q=1-P$、ħ=1，仅作解析控制，非真实轨道18或作者FA。对任一Hermitian $j_k$：

$$Pj_k^2P-(Pj_kP)^2=Pj_kQj_kP=(Qj_kP)^\dagger(Qj_kP)\ge0.$$

本P内$Pj_xP=Pj_yP=0$，但$Pj_x^2P=Pj_y^2P=31/4$、$Pj_z^2P=81/4$（均乘二维单位矩阵），最高权重$m=j$也仍有横向二阶矩$j/2=11/4$。因此限制内禀空间与严格经典向量零横向涨落是不同假设。压缩一阶算符不再自动满足完整su(2)；时间反演完整Kramers对子保持$T^2=-1$。本例P与原轨道18完整展开/BCS未等同，不能推出本核任何EM量或模式标签。

在另一个人为外部spin-L2张量矩阵中取$A_x=1/3,A_y=2/5,A_z=1/2$，对$H=\sum_kA_k(X_k-j_k)^2$，精确$PHP$与把$Pj_kP$直接代入后平方的差为$(31/4)(A_x+A_y)\mathbf1=341/60\mathbf1$。固定A/此P下它只共同平移能量，不改变该空间内劈裂；I依赖惯量或不同block/不同空间之间不能统一当常数消去。此X不是已经验证的body-fixed总I实现，此H不产生133Ce谱或新δ。

Rayleigh–Ritz只约束同一H、同参数/零点、真正嵌套空间的有序绝对能量。各空间分别减自己的ground不保相同gap单调：diag(0,1,100)限制到后两态给gap99而fullgap1；diag(0,99,100)同样限制给gap1而fullgap99。不同I、模型定标/组态映射变化更不能直接套用变分排序。原论文FA能量偏高可保留为作者解释，尚未由本练习复现实际两套输入/状态逐点对应。

## QTR原方法与本论文输入不能合并

[[ragnarsson-semmes-1988-particle-rotor-moments]] RS88-02/03/04/05/08/09/10给出具体核验项目：physical operator与stretched basis转换、bodyfixed I±的K作用、core-H的UU′+VV′配对与offdiagonal ξ、good-core-R基中的ERα、M1/E2及静态矩、gs=.7/coreQ microscopic与本论文gs=.6/Harris的版本差。程序名相同不能证明这些选项相同；coreR不是总I的无条件替代。

原方法185Au Table2也有能量/部分rate可描述而一条M1/E2性质错配，Table3对两种strongcoupled候选给不同δ符号，是待原观测检验的模型预测；它们支持本工程按观测逐量检验的做法，不给187Au或133Ce新增实验票。所有新推导/综合needs_review:true，实际producer缺口保留。

## 单粒子能、Fermi能和程序接口的未闭合输入

[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-30核ε表头MeV/5.45–6.51与正宇称λ50.6/51.0的字面，现有文本未闭合共同零点/单位。不可凭背景ħω约8MeV把某一列自改成ħω单位，也不能把正宇称λ当负宇称输入。后续要保存各核素/宇称的GAMPN输出header、ASYMO λ/Δ、统一offset/换算、对应轨道ID和实际版本；未取得前不输入数值求BCS占据或产physicalδ。这个缺口不证明实际代码错，而是论文summary不足以直接复制输入。

## 同源装置与参数账本：8/13不能任选

[[ding-2021-131ba-133ce-signature-splitting]] D21-D23-064-1–4和[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-31将实际版本对齐：Ding16页稿本/15页正式版的8clovers两环，同thesis13clovers三环相抵；反应/束流/靶/事件数对应，actual detector/event ledger仍缺。这使“同观测向量/同响应”不能仅由标题/事件总数宣布完成。PES β4与QTR ε4不互换，alignment Harris参考与核芯Harris不互换，期刊QTR ε4=.01支持正文谱系但不修实际input或表.1。

## 整体M1缩放与configuration-only的区别

固定H、所有态/相位、E2算符、能量和母末态/reference，仅作整个M1乘η>0，则δ→δ/η、rM1→η²rM1、rE2不变。原表两spin从δ分别需要QTR η=4.07273/16、FA .890909/2.88235；从rM1需QTR5/3.95811、FA1.14708/2.75330。625 QTR中心+.89到实测中心−1.5无正η解，但其大误差/其它根未纳入，不能据中心判sign排除或成分占优。

这些只是Tables6.9–11打印中央值不能被单个共同正η精确同化的条件诊断，不是显著性/模型错误/实际g拟合。rM1(19/2)/rM1(17/2)在整体η²下不变，表QTR3、FA31/95，实验47/25；图QTR约.10→.03的下降分支另外保留，不用它替表.01。FA rE2表/图10倍冲突同样不受M1整体缩放改变。

模型mixed photon yield u不是冻结量：u(η)=u(1)(η²+δ(1)²)/(1+δ(1)²)。实验计数保原数据，改变的是模型预测；如果模型yield也强制不变就与固定E2/仅改M1的合同冲突。单改gs会因l/s/core干涉产生逐线不同变化，不等同整体η。若B槽同时调整g、Q、惯量或态空间，必须登记新增模型自由度，不能称只重指派configuration。

## BCS与reduced-B归一的独立练习

[[ragnarsson-semmes-1988-particle-rotor-moments]] RS88-17/18限定86项精确控制：选定u/v=(3/5,4/5)、(5/13,12/13)，Fock散射T-odd63/65、T-even−33/65；对角电算符的qp总期望1减真空32/25才为−7/25。它不确定实际核素占据、不恢复1978显式EM矩阵元。声明3j约定下固定Mi完整Mf/q和已给B，不能重复初态平均；数学rank0控制不对应单光子γ。

上述数学修正服务于后续读/编真实模型，但当前1978正文及2022实际producer仍缺，不能把条件控制精确度写成实验精度。所有新增分析needs_review:true，长期学习继续。

## 冻结实验层的组态重指派：实际预测仍需共同producer

[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-33把三种操作分开：同一态纯relabel无新预测；固定同H/T本征态集合的mapping须同时过Ex/Jπ/全链接网络；新增3qp、pairing/势/算符已是实质模型改变。原表相对Iγ不等原始N，当前可冻结公开21节点/48边，但不称已重放缺失N/AD/P/Cov。

Ce Band4 #17/#16本已在九轨道空间和原混合内；裸ε差不能预测qp带头，因为同Δ时能序还依(εν−ε18)(εν+ε18−2λ)。负宇称λ/Δ/零点未知，3qp的pair-breaking/blocking/core与残余能也未得，832keV仅是已测带头而非能量可行性证明。Au保持[[sensharma-2020-longitudinal-wobbling-187au]]的Band2原wobbling、Band3普通SP身份；[[guo-2022-low-spin-wobbling-187au]]中不同主轨道解释仍需统一H/算符后才是纯mapping对比。

选定球形纯j控制νh11/2在gs=.6free时gj=−.208691，对Ω5/2、7/2、9/2相同；渐近Nilsson gK是另一个极限，不能拿其差异当实际mixedQTR预测。轴对称goodK带内M1/E2公式含K²，实际δ符号需相干signed RME，gK或B平方不够；跨带Table6.11不能套带内CG比。3qp→1qp也非物理一体算符普适禁戒，Bogoliubov变换有qp数差±2项。τ、完整BR/ICC/Cov与静态矩等只有在预冻结模型预测向量可分且未定标时，才提供联合holdout；不承诺一量终判。

## 131Ce/133Ce逐带与分析操作迁移

[[alwaleedi-2013-band-structures-131ce]] AW13-D23-064-1–3与WK22-34支持按源/带头/具体links对照。131Ce Band3为61.8keV低态，133Ce同号为ground；133Ce Band3/2 13/2+差14.1和412.4/767.7links是same-spin身份练习，不是ωc或混合强度。133Ce论文未给可配套实验ix/crossing数值，保持unknown，模型Rl≈2不当cranking ix。两个“Band4”的head spin/解释也不相同，不合并成同一声子。

| 同定义selected路径S（keV） | 131Ce | 133Ce |
|---|---:|---:|
| Band1 I13/2 | 180.80 | 182.10 |
| Band1 I15/2 | −237.80 | −216.15 |
| Band1 I17/2 | 320.50 | 277.30 |
| Band4 I19/2 | 65.20 | 49.60 |
| Band4 I21/2 | 17.15 | 100.55 |

这些只是透明选定相邻M1路径的中央算术，不是原作者完整adopted S、未给Cov/CI或γ反演。131Ce Fig5.2 caption/正文身份差保留，回原γ rows避免一图双用。

可迁移步骤：先作run/detector/line manifest；608.3/608.7重叠门用原响应、独立互符合/反符合和第三门检验候选拓扑，缺峰用上限而非零；AD/RAD/DCO/Rac按实际角组/门/取向/效率处理，dipole不单独定E/M；branch先同母态/分母出口再消τ，完整BR/ICC和mean/half定义齐才求absoluteB。131Ce已有Li/Singh寿命与静态矩各按具体态/带接入，不说全核无τ或把DSAM/RDDS当充分判据。

附属研究下一日优先选一个实际输入可得的问题：582 out/out分母身份；程序ε/λ单位和完整input卡；131Ce Band3零点及互链；高spin3qp/crossing逐态mapping；真实角响应/双峰；既有独立τ能否接到目标母态。主日课程优先，缺口不靠插值/补δ/τ/机时关闭。全部新增推断needs_review:true。


## 有限all-detector门的接受度练习

来源：[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-35、原PDF54/58/59/61；[[ding-2021-131ba-133ce-signature-splitting]] D21-D23-064-1，稿本PDF2。当前是Day24附属研究的有边界进展，不替代[[135nd-chiral-partner-resolved-evidence-map]]主卡。

本轮回读thesis PDF54–61方法连续段，fresh视觉PDF59/61；定向读Ding稿本PDF2，原SHA匹配。thesis Ch4一般介绍为8clovers+LEPS，Ch5具体run为13clovers；Ding稿本与此前已核正式版为8clovers。同一束流/靶/2.8×10¹⁰双符合和5.4×10⁹高fold事件数只给强同源线索。已查入口为这些原件段、其source、AFRODITE实验页和既有crosswalk；它们未提供run ID/date、active detector mask、45°events、实际sorting geometry或逐门counts。没有声称搜索穷尽全库/设施档案，未反复请求旧失败端点，也未把一般阵列图视作actual mask。

### 连续对象、近似与可计算量

真实目标是门条件下的联合响应积分，而非只读一条single-γ角分布：

$$N_{t,G}\propto\int d\Omega_t\,d\Omega_g\,
A_t(\Omega_t,E_t)A_G(\Omega_g,E_g)\,
W(\Omega_t,\Omega_g;\rho,\delta_t,\delta_g,\ldots).$$

actual A包含效率、有限立体角、active mask、addback/self-pair veto与sorting。Eq4.6分子分母的G虽然名为同一“all”，仍须这些条件匹配，不能把有限求和直接替换成对4π均匀积分。

为隔离这一点，本任务只定义**无取向母态、点角度、各探测器等权、各环作方位平均**的数学族；不作AFRODITE实测响应。设两光子开角核为

$$W(\hat n_t\!\cdot\!\hat n_g)=1+\sum_{k=2,4}a_kP_k(\hat n_t\!\cdot\!\hat n_g),\qquad
G_k={\sum_rw_rP_k(\cos\theta_r)\over\sum_rw_r}.$$

Legendre addition theorem在方位平均后给

$$\overline W_G(\theta_t)=1+\sum_{k=2,4}a_kP_k(\cos\theta_t)G_k.$$

均匀4π gate对k>0有Gk=0；有限环一般不满足。两套原件的极角/数量分别作equalweight条件输入：

|描述布局（未选择为actual）|G2|G4|
|---|---|---|
|4@90°+4@135°|−1/8=−.125|−1/64=−.015625|
|1@45°+8@90°+4@135°|−11/52≈−.211538|31/416≈.074519|

数量只在此练习充当权重；真实能量效率/晶体或clover合并、非均匀方位、coincidence排除等会改变响应。尤其单个45°探测器不等同一个方位均匀环；这是假定的方位平均控制，不掩饰实际缺口。

### 两条计算路线、极限与误差

`system/scripts/day24_finite_gate_acceptance.py`以exact Fraction给独立polar基准，以开角核直接做128/256方位节点积分，与addition-theorem结果比较；还检查全球Gauss积分的rank0归一和rank2/4消去、权重整体缩放/顺序、偶rank前后角镜像。32个有限数学控制通过，双路线差的检查界2×10⁻¹⁵只限舍入/此多项式求积，不是实验系统误差。

为展示残余项可影响条件比，另选positive kernel a2=.2、a4=.1（W≥.7），得到synthetic W135/W90分别约.982677和.963326；均匀4π gate为1。这些系数没有绑定真实cascade，数值**不是实测/理论预测的R_AD、DCO或Rac**，不能和1.3/.8或1.27/.74做拟合或指认修正。零关联a2=a4=0时响应退回常数；有orientation的实际反应需更完整张量响应，而非直接套本无取向例。

### 知识影响与下一个可得输入

`limits`的是将“all-detectors”升级成任意有限阵列的精确门无关定理；保留作者实验校准及其经验适用范围。此练习不能裁定论文错误、选择8还是13、给共同response likelihood或为未测线分配δ。若actual ledger可得，优先核run/active mask/45°事件及两种sorting用的同门已知参考线，再纳入有限立体角/效率/取向和Cov。没有该输入时继续可解析的模型/节点问题，不重复空缺mask检索。582 out/out分母、ε/λ零点、signed EM和高spin迁移缺口全部保持；817.7不变成观测线。
