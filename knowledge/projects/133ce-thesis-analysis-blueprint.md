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

本项目继续作为133Ce实际分析蓝本，不能以source/译稿完成结项。Day24先完成手征主卡原件与逐伙伴证据图的高价值工作，再推进本页“有限all-detector门的接受度练习”；13/8clovers的actual run仍待ledger。Day24另已把131Ce实际寿命/限值和本核三个母态的九条observed边接成迁移合同，不移植数值τ/Qt。A13高spin/版本零点与WK22程序引文层的新边界已分栏。新用户原件[[larsson-1978-nuclear-core-quasiparticle-coupling]]的历史signedEM/矩阵接口现已原读，关闭此前方法body缺口，原actual input仍缺。新推断needs_review:true，不改变既有Band5用户审核、raw或模型actual输入边界。

## Research Question

怎样把[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]的实验分析、signature/Coriolis机制和QTR电磁检验真正转为可迁移的研究能力，并为用户尚未完成的分析提供步骤、输入及失败检查？用户明确要求像[[alwaleedi-2013-band-structures-131ce]]支撑其131Ce分析那样严格对待；这是整体知识的重要补充，不能以source建页/普通摄入或一次summary结束。本工程起于Day23补充，当前在Day24主卡高价值工作后继续；本项目不另启课程卡、不自动替代主课学分。

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

### 582.7 keV out/out 分母未闭合之严格核查

针对 Table 6.11 给出的 582 keV 出带比 [rE2=5.06, rM1=3.95]，对其分母跃迁进行逐级核查：
1. **能级差推算**：母态 Band 4 17/2− 为 1409.8 keV，若向 Band 1 13/2−（592.1 keV）发射同母态 $\Delta I = 2$ 跃迁，其能量差为 $1409.8 - 592.1 = 817.7\text{ keV}$。
2. **实验账本与纲图核查**：全面复核 WK22 Table 5.2（实验跃迁账本）与 Figure 5.1（能级纲图），均未出现 817.7 keV 跃迁，亦未记录其光子强度 $I_\gamma$、DCO 或探测限。817.7 keV 纯属能级能量差，非已观测 $\gamma$ 射线。
3. **历史文献比对**：Gizon 1974 Table 4 列有一条未指认（unassigned）弱线 817.3 keV（相对强度3.4），但无任何符合或门谱证据将其绑定于 1409.8 keV 母态，无法作为同母态参考。
4. **边界与规范**：Table 6.11 的 582 keV out/out 分母身份缺失直接实验支持，分母保持严格未闭合；禁止从能级差逆向虚构观测线或捏造 $I_\gamma$。

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

[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-14/30/38明确保存三个不同问题。正宇称Table6.1与紧接正文（physicalPDF77）分别印十六极形变ε4=.1/.01；Ding正文.01提供引用谱系，尚不能证明哪一项是排版错误或actual输入。负宇称参数另为ε4=.015（WK22-16），不混用正宇称冲突。

单粒子能是Tables6.2/6.4（physicalPDF78/88）的ε(MeV)，正宇称Ce/Ba的λF=50.6/51.0 MeV见physicalPDF78/87。共同零点和换算未闭合，不凭ħω约8 MeV改单位或求实际BCS占据；负宇称λ不能继承正宇称值。程序链仍需版本/header、λ/Δ及单位/offset、空间/阻塞、core-R惯量、完整本征态与规范一致的EM输出。

Larsson/Leander/Ragnarsson1978在thesis是Ref40（physicalPDF124），不是Ref1；该历史原件本日已读，见[[larsson-1978-nuclear-core-quasiparticle-coupling]]及下文。RS88另为Ref62。历史方法/算符已得不等于2022实际GAMPN→ASYMO→PROBMO producer已恢复，亦不能以程序名相同证明选项相同。

## 同源装置与参数账本：8/13不能任选

[[ding-2021-131ba-133ce-signature-splitting]] D21-D23-064-1–4与[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-01/02/31给强同源线索，actual run/geometry ledger仍缺。thesis physicalPDF61明确为125Te(12C,4n)133Ce、57 MeV、5 pnA、2 mg/cm² Te靶及8 mg/cm² Au背衬，2.8×10^10 double与5.4×10^9 triple及以上事件；不是122Sn+16O/85 MeV，也不是4.8×10^8/2.8×10^8计数。总事件数不能充当弱线有效counts。

Ding稿本/正式版写4@90°+4@135°，thesis具体实验段写1@45°+8@90°+4@135°。同事件数不能替代run、active detector mask、45°事件选择、sorting geometry及同门参考counts。AD/DCO/Rac参考值依阵列/门/取向/效率，不跨布局直接搬用。

原Eq4.6后的陈述是all-detector gate下RAD不依赖gate multipolarity，不能改引为“消除核取向衰减”。下文有限接受度练习仅检验特定角关联核在4π与有限gate下的消去条件，不是实际取向/去取向重放。PES β4与QTR ε4、alignment Harris与core Harris也分别保留。

## 整体M1缩放与configuration-only的区别

固定H、所有态/相位、E2算符、能量和母末态/reference，仅作整个M1乘η>0，则δ→δ/η、rM1→η²rM1、rE2不变。原表两spin从δ分别需要QTR η=4.07273/16、FA .890909/2.88235；从rM1需QTR5/3.95811、FA1.14708/2.75330。625 QTR中心+.89到实测中心−1.5无正η解，但其大误差/其它根未纳入，不能据中心判sign排除或成分占优。

这些只是Tables6.9–11打印中央值不能被单个共同正η精确同化的条件诊断，不是显著性/模型错误/实际g拟合。rM1(19/2)/rM1(17/2)在整体η²下不变，表QTR3、FA31/95，实验47/25；图QTR约.10→.03的下降分支另外保留，不用它替表.01。FA rE2表/图10倍冲突同样不受M1整体缩放改变。

模型mixed photon yield u不是冻结量：u(η)=u(1)(η²+δ(1)²)/(1+δ(1)²)。实验计数保原数据，改变的是模型预测；如果模型yield也强制不变就与固定E2/仅改M1的合同冲突。单改gs会因l/s/core干涉产生逐线不同变化，不等同整体η。若B槽同时调整g、Q、惯量或态空间，必须登记新增模型自由度，不能称只重指派configuration。

## BCS与reduced-B归一的独立练习

[[ragnarsson-semmes-1988-particle-rotor-moments]] RS88-17/18限定86项精确控制：选定u/v=(3/5,4/5)、(5/13,12/13)，Fock散射T-odd63/65、T-even−33/65；对角电算符的qp总期望1减真空32/25才为−7/25。它不确定实际核素占据、不恢复1978显式EM矩阵元。声明3j约定下固定Mi完整Mf/q和已给B，不能重复初态平均；数学rank0控制不对应单光子γ。

上述数学修正服务于后续读/编真实模型；当时1978正文及2022实际producer均缺。后续032已取得并原读1978方法/附录，见下节历史接口；actual2022仍缺，不能把条件控制精确度写成实验精度。所有新增分析needs_review:true，长期学习继续。

## 冻结实验层的组态重指派：实际预测仍需共同producer

[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-33把三种操作分开：同一态纯relabel无新预测；固定同H/T本征态集合的mapping须同时过Ex/Jπ/全链接网络；新增3qp、pairing/势/算符是实质模型改变。重解释时保持已报告实验数据及处理约定；原表相对Iγ不等原始N，公开21节点/48边不代表已重放缺失N/AD/P/Cov。Ex、branch和response含分析/校准依赖，不称它们全是未经处理的直接计数。

Ce Band4 #17/#16已在九轨道空间和原混合内；裸ε差不能预测qp带头，同Δ时能序还依(εν−ε18)(εν+ε18−2λ)。负宇称λ/Δ/零点未知，3qp的pair-breaking/blocking/core与残余能未得，832 keV仅为已报告带头，3qp可行性保持unknown。Au保持[[sensharma-2020-longitudinal-wobbling-187au]] Band2原wobbling/Band3普通SP身份；[[guo-2022-low-spin-wobbling-187au]]不同主轨道解释须在共同H/算符下比较。

纯νh11/2在gs=.6free时gj=−.208691，对不同Ω相同；渐近Nilsson gK属另一极限。good-K的gK来自规范一致的内禀对角磁矩与K/Ω，三轴混合态不能无条件赋唯一gK。B值需要正确归一RME的模平方；δ符号进一步需要E2/M1相对符号/相位。当前完整态和实际EM输出缺失，不能用纯j/gK或good-K带内CG比冒实际跨带预测。3qp→1qp也非一体物理算符普适禁戒，Bogoliubov展开含qp数差±2项。τ、BR/ICC/Cov和静态矩只有在预冻结预测可分且未作定标时才提供联合holdout，不承诺一量终判。

## 131Ce/133Ce逐带与分析操作迁移

[[alwaleedi-2013-band-structures-131ce]] AW13-D23-064-1–3与[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-34支持按源/带头/具体links对照：

1. **带头与零点不可按同号合并**：131Ce基态为7/2+，其Band3为Ex 61.8 keV的1/2+低激发带（作者指认为可能νs1/2[400]1/2+）；133Ce基态自身即为1/2+，其同号Band3以1/2+基态（0.0 keV）为带头。相同带号绝不等同于相同单粒子组态或零点基线，不能把131Ce的零点或s/d混合参数直接跨核套用。
2. **133Ce 13/2+近邻能级与跨带连接（WK22-34）**：133Ce中Band2的13/2+（1459.9 keV）与Band3同spin的13/2+（1445.8 keV）中央能差14.1 keV。Table5.4的412.4 keV和767.7 keV均来自1445.8母态，分别到Band2的1033.4 keV/11/2+与678.1 keV/9/2+；不是两个13/2+态各发一条。这两个近邻态构成明确的同自旋节点身份区分练习，但能差小不自动等于测得了转动交叉频率ωc或带混合矩阵元；Table5.3在Band2列出的2733.4与2739.5 keV两个19/2+态也分别保留（WK22-07），不因同spin合并。
3. **AW13图文冲突与Band 5人工审核边界**：
   - 131Ce AW13 Figure 5.2图注将该曲线指认为Band 4，而正文（§5.2.1）则将其作为Band 1讨论；该文献内部的图文排版冲突严格保留，不作猜测性修正。
   - AW13 Table 5.3将Band 5两个低自旋signature分量在高自旋端均映射为`e⊗AEFG`（即`e⊗AE → e⊗AEFG`与`f⊗AE → e⊗AEFG`）。经2026-08-11用户显式审核裁定，忠实采用原表映射，撤回将第二行重构为`f⊗AEFG`的主观推断；在133Ce蓝本中严格继承该人工审核边界，不得以signature连续性或133Ce对照擅自篡改既有审核结论。

WK22未给可直接配套的实验ix/crossing数值，模型Rl≈2不当cranking ix；两source的Band4带头自旋/解释不同，不并成同一声子。上述mapping要求是任务比较设计，含声明的模型误差/共同零点，不能强迫经验H在实验亚keV误差内重现全部Ex。公开21节点/48边仅为选定B1/B4网络，并非全论文四带或完整branch耗尽。

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


## 131Ce真实寿命参考怎样接到133Ce目标节点

本节的来源分别是[[li-2004-lifetimes-131ce]] LI04-D24-001/002、[[singh-2016-lifetime-131ce-133pr]] SI16-D24-001/002与[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-36/37。Li原3页由leader视觉核；Singh由独立worker读11页/全部关键图表、leader抽Table1；WK22由worker与leader抽核原表。新综合needs_review:true，不改旧用户审核/撤回。

### 参考核已有τ，但它们各有节点和证据类型

|131Ce输入|原态/γ边|原meanτ或limit ps|依赖与迁移边界|
|---|---|---|---|
|Li2004负序列|19/2−→15/2− 642；23/2−→19/2−750；27/2−→23/2−827；31/2−→27/2−892|>4；1.44(54)；1.23(23)；<1.04 effective|最后一项未feeding correction；原DSAM/停止/门独立记录|
|Li2004正序列|13/2+→9/2+610；17/2+→13/2+725；21/2+→17/2+796；25/2+→21/2+649|1.46(56)；1.32(10)；.60(26)；<2.19 effective|与负序列相反宇称，不是同宇称chiral伙伴；不能按yrast合并|
|Singh2016 present有限|15/2−510；27/2−827；31/2−892；35/2−922，均ΔI2|9.6(+1.9/−3.8)；1.25(+.41/−.25)；.51(5)；.60(+.11/−.10)|低spin plunger以本工作高spin DSAM矩作约束；方法不同不等全输出独立|
|Singh2016 present limits|19/2−642；23/2−750；39/2−962|<7.31；>1.3；<.54|23/2正文另称约3ps上界，不能合成有确定联合CI的区间；各limit完整likelihood未给|
|Singh Table1 Ref32|旧Li27/2−827等行|1.23(23)旧τ；比较列Qt2.28(21)|旧τ经另一转子约定再转换，既不是present1.25也不是第三次采集|

Li Fig1与Singh Fig1的整数γ链可在各自明确零点下作rounded-sum辅助ledger；原表未列精确Ex/误差时，不能给加和值伪造亚keV精度。对131Ce旧采集/新采集的共同family支持，还需保完整edge链、spin/parity与后续版本差。更不能把131Ce的7/2+基态零点搬到133Ce的1/2+基态，或仅按同号Band3识别同一态。

### 133Ce独立clock必须落在哪些母态

以下列的是WK22 Table5.2中三个选择母态的**全部所列**出口，不认证真实branch完整性。Iγ为相对170keV参考线的原表强度；photon/内转换校正的实际口径仍须ledger确认，不由符号默定，未转换成总branch。

|WK22 Band4 parent Ex/Jπ|实际Eγ keV|daughter/source band Ex/Jπ|Iγ|原multipolarity|
|---|---|---|---|---|
|832.0，13/2−|624.6|B1 207.4，11/2−|3.3(4)|M1+E2|
|832.0，13/2−|794.8|B1 37.2，9/2−|8.0(14)|E2|
|1409.8，17/2−|209.0|B4 1200.8，15/2−|5.5(6)|M1+E2|
|1409.8，17/2−|577.8|B4 832.0，13/2−|3.22(21)|E2|
|1409.8，17/2−|582.7|B1 827.1，15/2−|3.53(25)|M1+E2|
|1809.1，19/2−|399.3|B4 1409.8，17/2−|1.66(18)|M1+E2|
|1809.1，19/2−|608.3|B4 1200.8，15/2−|1.89(18)|E2|
|1809.1，19/2−|464.4|B1 1344.7，17/2−|1.89(18)|M1+E2|
|1809.1，19/2−|982.0|B1 827.1，15/2−|1.95(17)|E2|

这里37.2是WK22本身的207.4−170.2与592.1−554.9能差一致所得，Fig5.1只标37；不是该thesis另印的decimal Ex行。982.0是真实E2边，作为out/out分母仍称reference候选，尚未认证作者ratio producer；582 out/out的817.7仍只有1409.8−592.1能差，不在observed边账本，不填Iγ/upperlimit/δ。625 out/in破折号也不补低Band4节点。

要使624.6/582.7/464.4变成absolute B输入，寿命必须分别属于832.0/1409.8/1809.1这些**母态**；终态207.4/827.1/1344.7的寿命、下游门、band平均或131Ce某态不能替代。608.3参考还受608.7近邻及实际门/响应的污染合同约束。所有已列出口归一相加不等完整branch耗尽，更不等已知ICC。

### 从参考核迁移的合同

1. 节点键同时含核素、source/campaign、Ex零点/误差、Jπ和全link邻域；band号只是source内标签。edge另有parent/daughter、Eγ/unc、多极/δroot、门与效率口径。
2. clock分finite/upper/lower/effective，分meanτ/T1/2、directparent/feeding；图上采用的ns/min half-life不填入ps present表。不同parent不能消τ。
3. 同parent相对rate可在相容photon-yield/门/效率条件下消τ；absoluteB还要本母态τ、全BR/未见支路界、ICC、mixed组分和jointCov。缺失值保持unknown。
4. 方法选择依目标寿命/beam/backing/velocity/角组/响应及feeding；不移植131Ce的sidefeeding、stopping、惯量、10%误差规则或Harris参考为133Ce实际条件。
5. τ/B/Qt/静态Q/g/shape分层。转子Qt及TRSγ、核g的模型解释不自动成为直接形变或模式终判；独立时钟/静态矩也须逐态匹配。
6. 来源链区分旧采集、转载、同τ再转换Qt、图重绘和共享约束；不能把一条输入链反复计票。新增研究要预冻结模型的可分观测向量，holdout与定标量分开。

### 含较高spin延伸，不等已验证3qp crossing

WK22 Band1观测表到35/2−5401.8keV、Band4到27/2−3616.2keV；“low-lying结构”描述不表示只有很低spin。其1qp九轨道QTR的随spin组分变化却仍是原空间内混合，不能据此建立高spin3qp本征态或ωc。核对其它133Ce高spin论文必须另外做source/零点/带头/全links映射，而非搬band字母、参考Harris或取同spin态合并。

### Agent self-audit triage — checkpoint005

P0: none identified（新增范围）。P1：参考核finite/limit/oldτ的身份由原表核，目标核九条observed边由两人原表核；source内derived37.2和missing817.7明确隔离。Cov、实际branch/ICC、目标clock/moment、producer及高spin空间映射仍缺。P2：worker报告/ledger是审计副本，以上canonical表/合同是可复用知识owner；不会以outputs替代原source。


## A13高spin论文不能按Band号接入WK22

来源：[[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]] A13-D24-001–004。A13 raw是8页accepted（带cover），alternate是5页reprint，页码和个别gamma标签须分别保留；新对照需明确选用哪一版。

|身份层|原件支持|仍不能推定|
|---|---|---|
|低lyingnegativefamily|A13 Band4 ↔ WK22 Band1：9/2−isomer及170/385/555/235/620网支持；A13caption直接给isomer37.2|WK22自身37.2的来源仍是边能差推得；A13516/751与WK22 517.6/752.6非精确同值，不静默统一|
|WK22新Band4|13/2−832.0、15/2−1200.8、17/2−1409.8、19/2−1809.1及三条选定EM连接|未映为A13高spin MχD5/6，也不是A13同号Band4；不能移植其3qp身份|
|A13正B2/3|TableI取19/2+头、约100keV伙伴间隔及实际crosslinks；三qp组态为作者RMF/TPRM解释|不等WK22 g7/2 Band2；同19/2+不合并|
|A13负B5/6|29/2−比较head、实际711/779混合links及1074/1146 E2；约400keVgap与chiral-vibration解释|观测连线不直接测声子/3qp count；作者未得这些bands的τ，不能填absoluteB/g|
|采集谱系|A13两次112MeV Cd+Ne/Gammasphere，同paper版本共享数据；WK22为Te+C/AFRODITE的另一描述采集|knownlevels/Ma1987等旧来源可共同采用，不能把每张图/每个已知level当独立票|

A13 TableI的Ex2.378/3.734MeV与从37.2isomer向上按integer图标签求的2378/3734keV一致；若选择ground参考则条件值应再加37.2。保两种字段和原出处，不认定原表究竟用哪个零点，也不把它修成“精确ground head”。B6的两图路径还差1keV，仅给条件重建4162/4163 relative-isomer，不造新采用能级。

这个例子说明，移植高spin/crossing结论前要同时锁定版本、零点、band/family、母末态及全links；连接路径不等态身份。WK22的一qp QTR随spin组分变化，与A13高spin三qp参数/空间仍是不同合同。前者不足以认证后者，后者也不能替低lying三母态的actual波函数/寿命/响应。

## GAMPN链的引用层与未恢复输入

[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-38原字面把程序[39,40]、κ/μ[11]、Harris[30,48]和RS88[62]分成不同路由：

|层|可核出处|输入仍需什么|
|---|---|---|
|历史formalism|WK22 Ref40=L–L–R1978；旧006仅metadata/body0，后续032用户原件已原读§2.3/Appendix显式signedEM；Ref39另为1973势能面方法|历史字段已恢复，2022actual输入/算符库/phase输出仍须独立核；不能将body取得视作程序复现|
|程序分工|PDF49明确GAMPN单粒子、ASYMO耦合、PROBMO电磁，§3.4作者归属与Refs39/40字面不完全对齐|代码版本/hash/header、实际input/output与矩阵/phase接口，而非依作者名自动认版本|
|参数来源|κ/μ据Ref11(1985)；ε/γ可来自PES或实验；惯量有2+或Harris路由|2022实际参数卡、共同单位/能量零点/λ/Δ/blocking、空间截断与coreR惯量；不凭引用谱系选具体值|
|既有RS88|另列Ref62，说明坐标/BCS/coreR/算符框架；odd EM细节指其Ref1(1978)|1988原方法不等2022actualproducer；historical收敛经验不认证本核9轨道精度|

本轮没有关闭ε5–6MeV与λ50.6零点、ε4 .1/.01、负parityλ或signedEM缺口。共同能量平移只有在同一合同内才从ε−λ消去；两列未证同零点不能自动相消。下步有actualheader/input/output或新可访问body时再开该路线；当前已查入口不重复空转，不把未得输入转成用户待办。


## Li正宇称寿命对应AW13 Band2，Band3零点另保留

[[alwaleedi-2013-band-structures-131ce]] AW13-D24-001–004与[[li-2004-lifetimes-131ce]] LI04-D24-001/002支持以下有条件的source-family桥：

|Ji→Jf（均正）|Li04 Eγ keV|AW13 Band2 Eγ keV|旧Li寿命对象|
|---|---|---|---|
|9/2→7/2|257|255.8|Li没有该态τ，不填|
|13/2→9/2|610|607.7|mean1.46(56)ps，旧Li采集|
|17/2→13/2|725|723.7|mean1.32(10)ps，旧Li采集|
|21/2→17/2|796|793.6|mean.60(26)ps，旧Li采集|
|25/2→21/2|649|647.4|<2.19ps effective、未feeding correction|

这是同π/同JiJf/连续链接支持的provisionalfamily对应，不是能量精确相等/已经统计相容、AW13新测τ或目标133Ce的输入。各γ相差1.2–2.4keV，双方误差/能量校准联立未给，分别保留。Li的257+610=867与AW13的255.8+607.7=863.5也只为各source选路求和，不混合成一个高精度Ex。

AW13作者采用的正g7/2 family是Band2，负h11/2 family是Band1；131Ce Band3的1/2+61.8keV是另一低lying结构。133Ce WK22同号Band3的1/2+ground不能因名称相同迁入61.8或Li τ，更不能以同spin把Band2/Band5的19/2+合并。

AW13 Table4.6的344.9/410.1端点与Fig4.1不一致，285.1+344.9对607.7还差22.3keV；保原行/图，不据整个表盲建adopted levels、S(I)或crossing。Table4.4的743.3与Table4.7的743.4行强度不同，即使Eγ和spin近同也不自动当duplicate；前者parent带身份未解，后者图示为Band5→Band3 link。913.2表/图终态也待核，不能从分组标题造一个确认Band3 19/2+。

这项对照把模型/寿命参考桥落实到可核母末态，并给出在哪里必须停止数值拼接。AW13 Fig5.2 caption Band4/正文Band1、原Band5高spin两分量人审边界继续保留；本节没有重写这些结论或给新δ/τ/Cov。


## EM输出类型仍须绑定实际producer

[[wu-2018-two-dimensional-collective-electromagnetic-transitions]] WU18-D24-001/003/004/009提供一个方法对照：它对单态概率平均局部TAC带内率，未给不同集体态间的相干跨带RME或signedδ。不能因另一个模型有wavefunction/B曲线，就替本蓝本的GAMPN→ASYMO→PROBMO补完整signedEM输出，也不能用其gp−gR=±1/Q0=1eb示意输入填本核gK/绝对B。

这个对照不宣称RS88或WK22实际程序也是rate-average；它们各自的空间、相位、算符、版本与输出合同仍须原件/input闭合。133Ce的582 out/out reference、负parityλ、实际coreR/阻塞/完整wavefunctions仍各自unknown，817.7仍非已观测γ；主线方法的进展不使本附属研究结项。

[[lv-bingfeng-2019-chirality-136nd-135nd-thesis]] TH19-D25P-001/005给136Nd的实际两条observedE2同母态实例：已绑定photon强度/能量可条件消τ和全BR求relativeB，但仍不给absoluteB/phase。它不替133Ce提供582的缺失reference，也不把energy-only817.7变观测线；本核必须先有自己的observed denominator与component/response身份，不能因另一核算得relative比就借其输入。


## 1978原方法的新原件：历史字段已闭合，actual合同继续开放

[[larsson-1978-nuclear-core-quasiparticle-coupling]] LLR78-D24-001–012现直接提供此前缺的原方法/附录，旧006及RS88“0页/未得”的访问过程保留为当时状态，不回填历史。新原件由用户另项获取登记提供；032实际方法读区为PDF1–11、31–34，不把自动提取35页当全文精读。此项进展不是133Ce工程结项。

|阶段|现在可以明确的历史字段|2022 actual输入/输出仍缺|
|---|---|---|
|GAMPN类单粒子|εν、完整signed c_NljΩ及barred相位；Eqs11–16的六类j/j² coupling矩阵|实际νID/header、κ/μ/频率/deformation卡、单位/零点、截断/全部矩阵；能表与最大组分权重不够|
|ASYMO类耦合|D2 good-I基、body-fixed I+降K、Coriolis及recoil；fullBCS与schematicBCS为两方案|实际选哪种λ/Δ/u/v/blocking/ξ规则、Harris/coreR消费、全部a_Kν(I,state)；历史constant惯量不填现代Harris|
|PROBMO类EM|A1–A4给real signed a_f a_i相干核，M1 spin/orbit/core、E2 coreQ+particleq在振幅层相加；A5–16伸长坐标变换|operator/有效g/Q/单位与相位、完整初末态系数和数值RME/δ导出；历史Ref23(1975)后续已原读，A8仅轴向同态；完整三轴/actual库仍未得，不自造library|

A3/A4没有印共轭star；通用复幅a_f* a_i是推广，不冒literal。A2印⟨I∥M∥I−1⟩且有sqrt(.7)，其direction/WE/单位与2022实际export需对齐，不能单凭前因子盖章。历史BCS明确忽略blocking/recoil特殊性，不能拿来推定2022也这样处理；整个core+particle E2不统一照搬coupling-H的plus配对因子。

A2方向另由LLR78-D24-020/037独立代数核清：在标准3j WE、M1/E2同Hermitian tensor与real convention下，反向共同spin相位相消，RME比不另翻相对号；这一条件数学点已闭合。仍未核的是2022实际单位/算符归一/emission字典，不把它们与方向代数混成一个永远unknown；个别B的初态统计权重仍不同。

这使下一actualexport可逐字段验收，而不是继续凭程序名字重建输入。ε表5–6MeV与λ50.6共同零点、负πλ、ε4.1/.01、582 observed reference、active detector mask和完整EM/clock/BR/ICC/Cov仍各自unknown。source得到不改变817.7 energy-only身份，不把旧114当actualproducer运行。

原件Fig1/Table1还给具体方法校准：同E2+/.419reference下不同芯QME可只小改所选odd-A谱，部分γ→ground B却分离。LLR78-D24-012原模型表γ4→ground4软/刚B比约3.29163，ground4→2仅1.09057；不是本核观测或预测，而是选择未用EM holdout的理由。实际133Ce须自己的state/space/算符和响应，不搬A193/Z79的core结果。


### 历史应用给出的实际失败检查

同原件LLR78-D24-013–019的应用主线已由036另读并核全部Figs3–10/Tables2–5，连同032覆盖科学正文/附录；不是把自动text当全文复现。185Re用奇核Q/惯量/bandhead调参，Seγ/惯量/ξ同样有具体选参，不能把用于定标的量再作独立验证。Se的部分能谱/EM支持与明显EM/parityoffset失败并存，作者建议blocking等改善未实际完成；不把这些失败搬成133Ce测得结果。

两个可直接执行的核验原则由此具体化：一是每个输出注明是否采用实验Eγ、是否含ICC/其它mode及完整clock/branch合同（原Tables3/4明确略IC、用实测Eγ）；二是把ε4/γ/Fermi/跨壳mixing的不同机制与未定标EM一起检验。source Fig9/10能给相似局部谱移并不证明所有参数永远不可辨，也不替本核ε4 .1/.01择值。unfavoured态不自动是简单反对齐，dominant轨道或band能序不能代完整spin-dependent state mapping。


### 已闭合的条件归一，不等actual输出已识别

[[larsson-1978-nuclear-core-quasiparticle-coupling]] LLR78-D24-021/022与WK22-40把纯数学字典补清：若M1字段明确定义为bareμ，T(M1)=√(3/4π)μ使B乘3/(4π)；若E2已标准，则相同正Eγ系数下人工bare-μ δ转standard需乘√(4π/3)。若E2字段又为完整O2μ=√(16π/5)T2μ，则两算符一起转换的δ因子改为√(5/12)。这不支持对已有PROBMO值盲乘任何一个factor或宣称作者漏因子。

WK22 ∫ρr²Y2已含球谐归一，A4的Q-like核需20/±1/±2的完整Cartesian/tesseral字典，不能仅看Q0就补整个E2前因子。普通ME若不是RME，还要明确Mi/Mf/q与3j；静态μ也非直接跃迁RME。下一实际output应先标字段类型、单位/ℏ、core/particle电荷、轴/相位、Eγ来源及radiation约定，再选已证明的转换，不把已可解的条件数学和actual分类unknown混在一起。


### physical E2坐标桥可条件求出，不冒历史库已恢复

[[larsson-1978-nuclear-core-quasiparticle-coupling]] LLR78-D24-023/024给042任务推导的五分量字典。明确选dimensionful X_i=√(ω_i/ω0)x_i后，physical r²Y2μ可按几何精确转换；若采用dimensionless ξ_i，还需x_i=√(ℏ/(mω_i))ξ_i的length²桥。042当时未读Ref23不妨碍这些定义层命题成立，后续043/044的原读范围见下节，但actual GAMPN选择何坐标/单位、径向basis矩阵和电荷仍未知，不能称完整历史q库或Ce输出恢复。

伸缩球谐展开中出现r_t²函数不等物理E0：一般r_t²不与physical L对易，完整q连同加权physical生成元仍满足rank2关系。不能删trace项强行用L^t、也不能从这种坐标项推E0跃迁。轴对称/球形极限、Hermitian和五分量tensor关系已在声明尺度下核，source保存完整连续公式，root重跑只核坐标恒等式。下一actualexport仍须基/长度/电荷/轴/phase/截断与signedRME，不把数学闭合替换为actual producer认证。


## 1975 Ref23原件推进：坐标与对角Q闭合，actual输入不替代

[[leander-larsson-1975-potential-energy-surfaces-n-equals-z]] LL75-D24-001–012已按真实21页原件分工读完科学主线/Appendix/全部12图2表，043方法与044PES范围分列；完整API对象来源/哈希在source，不把先前1页preview当全文。原始用户PDF/PLAN/Bib未动，候选在tmp。

现在可直接核A1的dimensionless ξ、ω0/ω0°不同及A7含γ/ε4的体积选择；A2/A3是CG约定的一般angular ME，不含actual径向/变形系数；A8/A9明确忽略γ且同ν对角，q2ν为Q-like而非任意μ。Q0为总proton sum，Q40却显式除Z，Table1 fm²/fm⁴也不是B(E2)单位。完整三轴off-diagonal库、actual κμ/ω/BCS/space/header与signed态仍须另得。

A8与042桥现可逐式对：γ0下p=1+ε/3、s=1−2ε/3、ℓ0²=ℏ/(mω0)，physical(2z²−x²−y²)=ℓ0²/(ps)[(2ζ²−ξ²−η²)+2ερ²/3]，再取同ν期望即原式。这个ρ²项不产生物理E0；把同pointwise恒等式用于任意bra/ket是任务推广，不能倒填成1975原件已印全transition库。

其staticPES主线还给实际检查：κ.08/μ.10、9–11shell与ΔN>4抑制、surface/高multipole最小化都是N=Z A12–44的具体输入；40Ca失败、24Mg surface敏感与投影/ZPE/混合限制必须随结果保留。不能因同MO方法谱系或hbarω公式就自动填本核ε/λ共同零点、ε4 .1/.01或κμ数值。下一个可解析输入应对准WK22真正所引的参数源或actualexport，不以继续摄入历史论文代替producer证明。


## Ref11原参数与高spin实例：补谱系，不代实际计算

[[bengtsson-ragnarsson-1985-rotational-bands-particle-hole]] BR85-D24-001–014现已分工读完69页主线/全部32图4表，rootTable1及130Ce离散例核。κμ按N_rot/pn分列（neutron4为.070/.39、5为.062/.43），原势用stretched l、其空间Eq11限N=N′=N_rot。N_rot是删除跨壳项后近似保留的rotating-HO标签，不是本核νID或QP计数；原表可核不等2022实际逐轨道输入已重建。

本文configuration是(N_rot,α)组占据数，band是连续trackedorbitals，同一粗configuration可含多band并有组内crossing。弱virtual interaction在同ω中被有意清除，作者承认并非完全物理；真实同I的bandmixing不由平滑支反推为零。Σeω、labspenergy、Strutinskytotal及减reference图线也不是同零点；这些区分直接要求未来actualexport给轨道/态mapping、空间和能量定义。

130Ce§8.4提供更贴近区域的实际方法例：globalyrast换向ε.35后，继续ε约.25的组态支仍可描述已见discreteEγ。作者用continuum J_band^(2)52与discrete45的惯量差推cascade可能走largerdeformedroute，仍希望观测其带内跃迁；不把modelminima或平均量当已resolved两shape，更不移成133Ce的3qpcrossing、Harris或τ。BR85明确不适低spin定量no-pairing谱，不能借高spin成功删除本核λ/Δ/blocking合同。

### 三源REFLECT：相同方法谱系仍分三类证据

LL75给single-particle/shape坐标、角ME和PES判读；LLR78给core–qp耦合与signedEM公式；BR85给另一no-pairing cranked路径的参数表、diabatictracking和多核失败检查。三篇分别关闭历史定义/参数来源，却都不交付2022三程序actualjob。能量拟合、参数谱系、程序执行和独立EM检验不能互相替代。

本轮belief revision为supports：历史矩阵元、坐标与κμ不再只是metadata/转引，下一export已有逐字段可核字典；limits：相同参数名或相近Eγ曲线不保证同态/同形状/同相位，staticminima与yrastenvelope不等实验band。方向/归一/指定stretch的条件数学已能闭合，不笼统留unknown；actual基/卡/频率零点/阻塞/signedcoefficients/EM核与实验582分母/响应仍独立unknown。下一最高信息路线优先取得实际已引用实验观测的定义或actualinput，而不继续用toy控制数代替缺数据。


### 130Ce原实验续核：先固定观测对象再做迁移

[[nolan-1983-ce130-high-spin-moment-inertia]] NO83-D24-001–007为BR85 Ref63真实primary。谷宽W=8ℏ²/J_band^(2)，不是Jeff计数；同一Mo+S采集的选门离散谱与raw关联矩阵有不同selection/背景，约20%129Ce/La贡献且作者保mostlikely归属。原文isomer至28−确认/30−possible，最高yrast线order不全；BR85结合另Ref77的32+陈述不能直接回填本primary。

BR85的52vs45概括与primary的justabove50、ε.25 rigidreference52分层；constantJ只suggest不发生大shape变化，不等γrigid测量。原式名义J52/45对应W153.85/177.78keV，差23.93keV只是任务尺度，不据4keVchannel给显著性/分辨力或复测数。实际完整离散线/response/Cov仍缺，不能移Harris/τ/g或3qp归属到133Ce。这里的进展是将数据—平均量—配置/shape推断的合同收紧，不以旧理论更好看替实际谱学证据。


## particle–hole等谱不是任意configuration relabel

[[meyer-ter-vehn-1975-triaxial-rotor-particle-model]] MTV75-D24-001–012与WK22-42核到一项直接影响替代解释的原条件：single-j Hp=(εj−λ)τz+Vpτz+Δτx把同壳εj设0，HR为同ph core；Γ变γ→60−γ、λ→−λ、Δ→−Δ并循环换轴，再ph σy合成等谱。它是参数/particle-hole对偶，不是同一实际H两条不同实验band自动degenerate或纯标签互换。

若实际表用Eν和Λ，须先证共同E0；映射是Eν′=2E0−Eν、Λ′=2E0−Λ。正宇称λ50.6与ε5–6的接口零点未知时不盲负，更不能把−λ叫negativeparity input；ph不改变轨道空间宇称。给多轨道迁移盖章需要实际闭合U空间，使h′−E0=−U(h−E0)U†，配对/惯量/coreR/阻塞/截断一起协变；quadrupole轴负关系不自动覆盖h0不同谱、spinorbit/l²、ε4。不是先验断言多轨道必不等谱，而是actual合同尚未给。

原模型还明确对应Q odd/M even：在同对应初末态/共同phase和radiation convention下，E2 RME反号、M1不变，B不变而δ反号；普通state整体rephase则两算符同乘phase、δ不变，两者不同。故只拟合能谱或unsignedB不能恢复实际signedδ；原PartI这条sign关系不冒133Ce跨带预测。Fig10画的是有单位/去Eγ的δ′，Table2 sign经验规则限低激发/sizable且b>3/λ≤第二sp能e₂，不借它填三条实际跨带线符号。

完整j壳的取向/Coriolis混合不等单方向frozenj，但fixedβγ/1qp<2Δ仍是模型域。Fig11换惯量会改掉许多crossings，能谱联合约束shape/MoI而非独立测唯一γ；Table3 higher K/Ω分类很tentative，Fig13大带内B也不保证partialwidth最大。actualwavefunctions、能量因子/全branch和算符仍须逐态检，不把方法对称当工程结项。


## Ref52实际133Ce例：历史谱、目标定标和γ软度分开

[[meyer-ter-vehn-1975-odd-a-unique-parity-comparison]] MTVII75-D24-001–015已核真实25页实验比较主线。standardγ的prolate/oblate侧仍用odd-A谱，壳内tildeλ fit第一(j−1)态；Fig2–9的λ为相对single-j端点/间隔坐标。199Tl/195Au还调整β，理论率/δ可使用实测Eγ。故“essentially parameter-free”只限文中取参规则，不恢复本thesis actual负宇称λ、header或signedjob。

133Ce Fig9以exp11/2−为0，9/2−为−170；模型triaxial9/2+18、axial+37，最低9/2显式失败，作者没有加ad hoc attenuation。两例β.22/γ23与β.19/γ0不同，不是单独改变γ。N75同中子素135Nd/133Ce/131Ba不等131Ce。历史相对zero、现代Ex、同spin多态和整个branch网络须各自验证，不因低两态可平移就合并整条带；原图未清注释/最高spin字不猜。

形状结论也限模型：Table6只挑战完全γ独立Wilets–Jean极限，同时说rigid limit未达；Table7 dynamic rms与effective fitγ不是同量，±2°不等CI/σγ。作者明确rigid literal naive、暂无定量PES结论，要求尚缺的odd+γdynamic比较。不能把低1qp谱的成功或ΔI1/2共存自动解释成手征/两shape/现代3qp crossing。

原表还保失败检查：Table2一列百分比仅80、不补缺；Table3b五条δ只有两条在原范围，既不据此给完整模型p值，也不隐藏作者积极支持。下一最高信息输入已指向该篇Ref26真实原实验的zero/links，而不是继续用原理论名词填2022 producer。


## 1974原实验：历史零点、已观测未指认线与一个可闭合节点

[[gizon-1974-deformed-states-cerium-neodymium]] GZ74-D24-001–016是实际22页primary，主线/全部图表分工核读，不只是source建页。方法用16O+Sn/Te、Ge/GeLi、prompt/delayed与0/55/90°；Iγ为55°相对值，原AD忽A4并按核用pureE2的平均α2，133Ce为.69(.19)。这不能搬成AFRODITE actual13clover响应、任意allangle gate定理或新的σ/I。

1974作者对5.4h/I9/2与97min/I1/2明确尚不知谁ground/isomer，Fig8以9/2为零；不是现代ground0。其11/2170/13/2554.9/15/2789.7/17/21306.3/19/21552.3与现代Ex须逐state/link核。以WK22派生37.2作任务暂定offset，13/2给592.1、支态1163.6给1200.8，两者608.7边与现代观测相合；原A2−.64(.06)亦支持支态spin候选。原先PartII994/1164数值参考现闭合为1163.6−170≈994、1163.6≈1164。它仍不提供832带头/整Band4同一性，高态差与历史ground身份不被抹去。

本篇已观测但未放置的624.8、582.2、464.6、817.3等光子线，是有意义的检索线索而非现代edge认证。尤其old817.3/I55=3.4不能自动绑定现代energy-only817.7为同母ΔI2outreference；旧582.2/I4.7也没有现代1409.8母态/终态binding。582 out/out分母仍missing，不造Iγ、不改observed标签、不用近能线凑表。

原Table4/图还保619.7的J标注、159.5的末态2450/2449.5不一致；同235峰至少一半强度在更高sideband且高段顺序不清。sideband约≤3ns是原源的有限feeding时钟描述，不能配给现代三个母态各自τ。135Ce的8±2ns另核另态，不移给133Ce。负δ/粗50±25%E2与prolate结论依取向和g/Q sign前提，不给actual跨带signed RME或γrigid证明。

本轮belief revision有具体增益：一项历史节点/能量参考从unknown到可追溯；一组实际未指认光子线丰富候选，却不足关闭目标分母；实验—转引理论的共享谱系明确。actual2022卡/波函数/signedEM、582母态分母、事件mask/Cov依旧各自开放，133Ce分析蓝本继续而非摄入结项。


## 公开评估的现代zero：有实际记录，但非新增独立实验

[[nndc-2011-133ce-low-level-reference-records]] N133CE11-D24-001–008实取NNDC adopted133058001、reaction133058014及IAEA同源CSV。服务本轮返回2011/201104、cutoff2010-10-31评估：GS0/1/2+/97(4)min；9/2−异能态37.2(7)keV/5.1(3)h。这样现代0与历史9/2参考的关系已有actualpublicrecord，不再只有WK22能差算术；不把2011评估叫2026新测。

WK22的37.2派生decimal保其当时出处，不自动继承评估.7误差或升级review。adopted207.4(7)与37.2(7)、直接170.2(2)γ共享least-squares/anchor，缺Cov不把各level误差独立传播；37.2激发能亦不等已测37.2ITγ，原ENSDF明保IT=?/EC+B+LT100。

reaction子记录仍印37.3(6)/4.9(4)h，heldfixed且E/T fromadopted，与当前adopted不完全同步；逐record保，不平均、不从差.1keV裁错。5.1h加权包含1967旧5.4h测量，NuDat/IAEA又共ENSDF，所以这些不是多份独立实验票。ground/isomer后知不回改1974作者当时未知。原absoluteanchor首次观测路径尚未由循环comments唯一闭合。

reaction开头首L之前的817.3/582.2等仍unplaced，evaluated误差由一般规则赋，不冒原始逐线误差。此entry不补582sameparentoutreference或actualGAMPN零点。后续已有1997Em01RDDS等原引用可沿Ei/Jπ/branch/clock接寿命网络，需原文定义，不把数据库T列直接叫meanτ；低1qp不自动迁高3qp。


Day24 primary link: [[butler-1975-la129-la131-rd-lifetimes]]


## 1997 RDDS primary：133Ce时钟与评估T1/2分开

[[emediato-1997-133ce-rdds-lifetimes]] EM97-D24-001–009为同反应70MeV的真实4页RDDS primary。原Table II报mean τ=76(3)ps（170keV 11/2−→9/2−），而NNDC评估52.7(2.1)ps是乘ln2的T1/2，不能把数据库T列冒原论文τ。13/2−7.9(.5)、15/2−3.8(.8)、17/2−/19/2≤1ps及正宇称三qp5.3/.6、4.5/.5、5.3/.6逐态保存；同一τ服务双放置线/上限，不计独立钟。

RDDS合同含13距离、d0=22.5(1.0)μm、14条曲线/340点/22参数、sidefeeding、solid-angle/alignment/slowing修正和reducedχ²2.1；rawkernel/fullCov/ICC缺失。B(M1)纯M1假设、385/235 double placement、TableIII E1 23/42正文—表顺序冲突、模型γ−5与signature−30/字面[541]均保留。该primary关闭寿命网络的一条真实路线，不关闭582母态/branch/signedEM/actualproducer，也不证明手征。


## 1998高自旋DSAM：另一条时钟，不能覆盖低spin/modern Band4

[[joss-1998-133ce-triaxial-band-lifetimes]] JO98-D24-001–010是Gammasphere 4页primary：887.4/999.3/1097.6/1188.1keV四条高spin带内线的meanτ=1.11(.13)/.33(.04)/.20(.02)/.21(.02)ps，Qt=1.94(.10)/2.65(.16)/2.66(.21)/2.15(.15)eb，作者加权Qt≈2.2(.1)。DSAM/DBLS依赖5000-history阻停、固定sidefeeding、角组和模型输入，raw/fullCov/producer缺；加权表算术不替系统误差。

TRS给γ≈−30单ν、−73三ν，高spin图还给−83与SD极小值，β由Qt转换依γ/无hexadecapole假设；这是模型势面，不是静态γ或手征伙伴测量。高spinJπ多为括号/无低带link；现代ENSDF bandF、WK22 Band4或1997低spinτ不能按标签迁入。该primary增加高spin clock/collectivity证据，同时保shape、feeding、configuration和partnerEM缺口。


## 1991Pa04入口缺口与1998 primary谱系

079核对ENSDF Ref 1991Pa04为Paul等 *J Phys G*17 (1991)605–617, DOI10.1088/0954-3899/17/5/009，涉及N=75同位素低spin电磁/δ与120Sn(16O,3n)、92Mo(50Cr,n2p)；合法PDF端点只返回HTML，未把metadata冒原文。[[joss-1998-133ce-triaxial-band-lifetimes]]则为独立Gammasphere highspin primary，已完整核读并写JO98-D24-001–010；不能用Joss替代1991 body或把同TRS谱系计成独立理论票。


Day24 SD primary link: [[hauschild-1995-133ce-superdeformed-bands]]


## 1995超形变primary：独立高自旋节点，不补寿命/分母

[[hauschild-1995-133ce-superdeformed-bands]] HA95-D24-001–010为116Cd(22Ne,5n)120MeV Gammasphere primary，识别三条133Ce SD带，给J(2)、alignment和条件PES/configuration。无SD→normal linking、τ、Qt、absoluteB、DCO；带内E2与Jπ/构型均保条件。它与Joss 1998 normal-triaxial DSAM、Gizon/Emediato低spin为独立反应/观测节点，但1996Ha20复用同一Hauschild/Gammasphere campaign，只是新增带/分析扩展；不填现代Band4低态母态τ或582分母，也不提供手征判定。


Day24 1996 primary link: [[hauschild-1996-133ce-triaxial-bands]]


## 1996高自旋三轴带primary：多带观测与配置缺口

[[hauschild-1996-133ce-triaxial-bands]] HA96-D24-001–005独立116Cd(22Ne,5n)120MeV Gammasphere primary，报告六条新约100keV序列、relative populations、alignment和tentative νh11^3/πh11^2/πg7^2/5qp构型。DCO统计不足、linking缺失、bandhead spin/K假设使配置保持模型解释；无τ/Qt/absoluteB，不能替现代BandF、Joss时钟或582分母。与1995 SD和1998 DSAM互补而非重复票。

## 逐态 crosswalk：现代 Band4 的缺口仍是缺口

|现代对象|已知连接|寿命/分母状态|结论|
|---|---|---|---|
|WK22 832.0, 13/2−|能级、部分旧边可核|该母态 τ 未得|不能从 1997 低带 τ 迁移|
|WK22 1409.8, 17/2−|1409.8−592.1=817.7|τ 未得；817.7 为能差|旧 817.3 光子未绑定母末态；582.7的同母out分母仍缺失|
|WK22 1809.1, 19/2−|464.4/982.0/399.3/608.3等边|τ 未得；982.0为该母态out reference候选|该母态无582跃迁，分母缺口属1409.8|
|旧 1163.6→554.9, 608.7|Gizon Table4/Fig8 有实际边，J 为作者suggest|只支持单 node/edge|不能升级 whole Band4 或 signed EM|

## Normal-triaxial 与超形变集体性不能混成一个 Qt

Joss1998 的高自旋 normal-triaxial 带给 `Q_t≈2.2(1) eb`、`T(E2)≈35 W.u.`；其同文比较的 132Ce SD1 约 `7.4(3) eb`、约 `490 W.u.`，而 Hauschild1995/1996 的 SD讨论引用的先前 `Q_t≈7.5±0.8 eb`。这些数字来自不同带、不同数据/模型合同；它们可作数量级和相对collectivity的证据，但不能把Joss的Qt迁给现代Band4、也不能把Hauschild的SD带当作Joss四条τ线的同一构型。绝对Qt仍受阻停、sidefeeding和转换假设影响。
