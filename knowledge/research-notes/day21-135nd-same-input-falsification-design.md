---
type: research-note
title: "135Nd同输入反证设计：先绑定跃迁，再检验模型预测"
aliases: [135Nd同输入反证设计]
created: 2026-10-23
updated: 2026-10-24
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [mukhopadhyay-2007-135nd-chiral-vibration-static, zhu-2003-135nd-composite-chiral-pair, lange-kumar-hamilton-1982-multipole-admixtures, petrache-2006-near-degenerate-chiral-misinterpretation, frauendorf-meng-1997-tilted-rotation-chirality, lv-2019-chirality-135nd-reexamined]
created_from: Day21 checkpoint050
promotion_target: experimental-claim-boundaries
tags: [135nd, chirality, experimental-design, covariance, provisional]
---

# 135Nd：给“支持手征”设置明确的可证伪对象

## Research Trigger

Day21主案例需要把“支持手征”拆成可检验的特定解释，优先确认观测身份及预测域，而非以寿命相似性作普适判据。

## Grounded Evidence

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D21-R43-1至4给出真实配对寿命/带内强度、DSAM方法、作者TAC+RPA解释与近不稳定点失效。[[zhu-2003-135nd-composite-chiral-pair]] ZH03-D21-R44-2/3给候选线终态及部分多极性；它没有为MU07每个B列完成成分绑定。[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1（printed121 Eqs2.1–2.6）给光子率与RME约定。[[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D21-R45-1/4说明形状/分支的模型检验必须绑定假设，不能用另一个核的结论替换本核实验。

[[frauendorf-meng-1997-tilted-rotation-chirality]] FM97-D21-R50-1定向核原文同宇称前提，将普通手征双带与parity doubling分开。

本页是本任务的有条件实验/分析设计，不是新实验或真实拟合；原source review与flags保持。source前回忆已受上述资料priming，不作为盲测评分。

## Provisional Reasoning

当前保留的解释是：这两带的电磁数据支持作者的手征振动到强非谐/隧穿图像。它包含具体的组态、近谐区域及TAC+RPA适用范围，不等于“所有手征带必有相同寿命或完全相同B”。

将候选检验区间先限于配对数据的低spin端31/2−–35/2−，但是否足够远离RPA软化仍需模型后续原文/本征频率核定。本页不擅定数值model tolerance，也不把B_A=B_B的严格等式替代作者的近似预测。正式检验前必须冻结模型参数域Θ、预测向量及失效区间；没有它们，就不能量化声称已否定原模型。

## Assumptions

| 层次 | 至少需要什么 | 当前实际边界 |
|---|---|---|
| 身份 | 同核、初末态Iπ、原带/能量排序、γ能量、混合多极成分 | Ref8只给旧部分网络，MU07逐行E2绑定尚缺 |
| 观测 | 按角组/门定义的谱、背景、效率、相对γ强度与原始统计 | 原文展示代表谱，原事件与全逐门数据未取得 |
| 率 | meanτ、目标线photon branch、δ/IC及其它退激库存 | τ/B有发表值，不能从其恒等式重造真实branch |
| 响应 | stopping、feeding、门宽/门线时间角色与共同校准 | 原文说明宽门避时间选择，但缺原job/response/Σ |
| 模型 | 同一已定义母态/成分的带内外预测及Θ | 近临界失效已知，完整可重放预测/容差未得 |

## Transfer Conditions

对同一母态、同一多极阶L的out/in比较，按相同光子率约定有

R_L = B_L,out/B_L,in = (q_out f_L,out)/(q_in f_L,in) × (E_in/E_out)^(2L+1)。

这里q是每次母态衰变在该线发光子的绝对概率，f_L是该光子线中所选多极成分的份额；在M1/E2光子截断下f_E2=δ²/(1+δ²)。共同meanτ在这个比值中消去；q_out/q_in也可由同母态、同选择条件下经过效率/角关联校正的相对光子强度比得到。此法的优先输入是逐线身份、成分和门/响应合同，而非再做一个未知寿命扫描。没有这些条件时不得声称实际已消除了feeding或gate偏差。

跨两带的B_B(I)/B_A(I)来自不同母态，寿命不会这样自动消去。若有经验证的共同乘性校准g，两带B同时乘g，log(B_B/B_A)才保持不变。真实stopping/feeding不预设为这个g；带特异和逐线误差仍保留，原jointCov未得。

当前TableI的五个E2对数比仅是已派生强度的确定性对比，见本run `same-input-design-050.json`。它们没有添加独立实验信息，也没有给相似性、等价性或不相似的显著性。

## Falsification or Reverse Tests

对指定的近谐固定组态模型：若按同一谱/门/响应分析、在允许的stopping与feeding域内，匹配母态的强度/交错向量稳定落在模型Θ产生的全部预测域之外，而该数据的统计与校准合同仍成立，则该版本解释被反驳。接近失稳点出现的带间差异不能直接套用这一近谐检验，也不能由此排除全部动态手征。

本装置已实际完成两带的角门DSAM与符合分析（MU07-D21-R43-2），因此这类观测在已有技术链中有直接可行性依据。是否能把某个新差异测到足以区分模型，仍缺计数/效率/分辨率/feeding/背景与Θ；本页不报告曝光时长、功效或最小可测差，也不假定Gammasphere具有已标定的线偏振性能。

对本页讨论的普通转动手征双带，若新、可靠的多极类型/宇称约束确定这两条候选带相反宇称，则这对具体伙伴的身份前提被反驳（FM97-D21-R50-1），而非仅见某个B稍不相等。若线属于另一个核素，亦须撤回相应本核归属。相反，仅发现比较的两个数据点spin不匹配，首先需要重新配对，不能据此排除两条完整带的其它同spin伙伴可能。

现有原文支持同核同宇称，尚未出现上述新反证。核素/线归属可由符合网络检验；可靠相对宇称仍需多极类型及标定，本次未证明靠未标定角分布就能排他判决。装置已实施谱学/DSAM，只证明相关技术路线可用，不保证某条弱线的未来误差或自动具备偏振性能。

## Open Questions

本轮公开定向检索遇Scholar timeout、Curate搜索HTTP202空体、Figshare搜索HTTP403；其它索引返回的多数命中是无关主题或理论文章。没有据此断言实验记录或学位论文不存在。当前未新取得逐线branch、原job或jointCov。

最高信息路线仍是同核原分析输入。051已读[[almehed-2011-chiral-vibrations-a135]]实际arXiv v2全文：p.2/8把135Nd转给Ref.13，邻核Table I/II不能补本核预测域；p.4/15–16明确近谐软化、非谐需求及部分趋势失败。这是真实方法后续，不等于MU07 Ref32全部承诺已闭合，更不是实验branch表。本页仍为L3设计/readiness，不是新实验CI或L4完成。

## Competing Explanations

近简并可与组态混合、形状差别等竞争解释相容；PE06的异核反例只限制普适推断，不直接裁定135Nd。必须对本核同一观测向量比较预测。

## Failure Conditions

母态或多极成分身份未绑定、门选择不匹配、响应未校准、或近谐模型已失效时，不执行本页的排他检验。缺失jointCov时不报告联合显著性。

## Human Review

本页尚无用户逐claim审阅；维持unreviewed和provisional，不改变引用来源的原有review状态。

## Promotion or Rejection History

2026-10-23 checkpoint050建立有条件L3设计，尚未提升为实验结论；首次lint的schema/链接错误已在同一检查点修正，失败记录保留。

## Checkpoint051：线性振幅的条件域

AL11-D21-R51-7的A3–A6给Q0=Cεcosγ、Q2+=−Cεsinγ，Jacobian行列式为−C²ε；ε→0时角坐标反演失效。冻结其它自由度，采用R3=e^(−iφJ3)，则精确Q2−/Q2+(初始)=sin(2φ)，线性为2φ。30/40度时线性相对精确分别偏高约20.9%/41.8%，但这只是有限转动运动学演示；原论文的量子声子振幅不能无条件当成经典摆幅，因此这些百分数不是实际RPA误差，更不是135Nd实验修正。角分母在退化轴失效也不证明出现某一集体模式。

模型检验仍需本核Θ、spin到ω的映射及有效域；不能把邻核大振幅描述转成135Nd被证伪。原计算的带内TAC和带间RPA是同一理论链的组成部分，不算独立实验支持。

## Checkpoint052：后续实验补什么、不补什么

[[lv-2019-chirality-135nd-reexamined]] LV19-D21-R52-1至6提供本核独立JUROGAM采集的逐线信息，绝对强度仍指向MU07。Table I的Iγ为对198.8keV归一的效率修正相对数，不能直接当每母态photon branch。

D6 31/2的225.8/648.9/896.8keV共享4007.8keV母态，但前两线只有M1/E2标签而无δ；E2带外/带内成分比保留系数除以f_E2(225.8)。D6内591.8/681/812的multipolarity空白保持；31/2、33/2的带内ΔI2不由能量相加补观测。表头重复行/998.1母态能差另记源页。新数据确实缩小谱学缺口，尚未绑定原MU07每个E2点，不得据此恢复旧分支补偿认证。

可测优先项是这些同母态线的成分及同门相对强度/响应；原装置有相应谱学能力，但本次仍缺具体计数功效与校准，不保证可达精度。具体模型比较须冻结与之匹配的PRM或TAC+RPA参数，不能把两者看成一个已定预测域。

## Checkpoint053：模型预测点已得，但参数域Θ仍未得

新读[[qi-2009-135nd-particle-rotor-chirality]] QI09-D21-R53-1至6，取得本核全量子PRM的一组实际参数点（β=.235, γ22.4度, 𝓙0=29.0，Q0=4.0eb），但该点按实验能谱调整，作者未给出允许的参数域Θ或误差合同。此外，该v1参数与Lv2019转述的(.24, 22.2)有版本差，不能合并成一个无歧义空间。

作者明确带外E2被计算低估（p.6），且模型基于固定形变；它支持超越近谐RPA的必要性，不消除模型不确定性。Figs.3–4的RMS分量sqrt〈Jk²〉是非负数，单凭三轴非零不能判定带符号的非共面取向或手性，声明反例见`prm-geometry-scope-053.json`。检验前仍须冻结具体预测、Θ与带外线成分绑定；当前未闭合这些条件。

## Checkpoint060：文献与实验数据血缘闭环（124纠正优先）

MU07、Qi2009、Almehed2011及Lv2019的已核引用关系是有限文献谱系，不证明全领域唯一发表、无任何未见实验长文或原数据已穷尽。后续方法篇明确135Nd结果not shown here（AL11-D21-R51-1），不能作为完整原模型job/Θ。旧R60复合认证由124撤回。

## Checkpoint089：与七大实证支柱及相空间敏感度的跨方法对账

099修订：不能要求物理量与分支/相空间“完全解耦”；强度恰由这些量联合反演。可操作的合同是绑定跃迁/通道、统一定义和响应、传播其共同误差，并冻结待比较的特定模型及有效域。100Sn的简化β+积分不增加135Nd逐线branch/Cov，通用方法类比不作跨核实验输入。见[[hinke-2010-100sn-decay-spectroscopy]] HK10-D21-R99-3与本页052边界。

## Checkpoint103：VoR取得后，缺口收窄到局部对象

[[lv-2019-chirality-135nd-reexamined]] LV19-D21-R103-1至5现已从期刊VoR核验，不能再把“未取得VoR”作为当前缺口。VoR仍保留空multipolarity、重复母态及998.1/997局部冲突；需原producer/作者更正，不从核能差单独补赋观测线或纯E2。

可执行的反证首先检查同一对象：已明确的M1/E2连接若两个态宇称确实不同，将反驳该多极指认；目前334.4的冲突只是印刷元组不一致，不能当实测相反宇称反证。D5/D6绝对B仍指Ref36，模型γ按B比校准仍保留。下一步若有原门谱/独立偏振，可用来裁定局部身份；在此之前，不运行原MU07逐线joint检验或承诺装置可达显著性。

## Checkpoint104：最少伴随输入与可辨识性

输入取[[lv-2019-chirality-135nd-reexamined]] LV19-D21-R104-1，率约定沿用[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1。以下为本任务L2推导/L3设计，假设同母态与匹配光子率/响应、896.8纯E2、另两线只含M1/E2；并不把作者的多极标签提升为无高阶混合的独立证明。

定义u=δ225²>0、v=δ649²≥0，由已印中央强度/能量得到C=(.79/3.8)(225.8/896.8)^5=.0002103706674，D=(1.8/3.8)(225.8/648.9)^3=.01995847704。于是

R_E2=B(E2;896.8)/B(E2成分;225.8)=C(1+u)/u；
R_M1=B(M1成分;648.9)/B(M1成分;225.8)=D(1+u)/(1+v)。

同母态总寿命与共同强度归一因子在这些比值中消去。因Iγ为光子率，不能再次无条件乘IC；若改用total-decay branch，须先转换为该线photon branch。完整未观测支路库存对绝对q/强度重要，但不自动妨碍经过匹配响应的同母态相对比。

### 可以识别什么

强度表只固定C/D，不能在u/v未知时唯一确定两个B比。若模型或其它独立输入给R_E2，则u=C/(R_E2−C)；纯E2/匹配合同内R_E2>C、下确界C、无有限上界。此条件界不区分手征与其它模式；若放开896.8的纯E2份额，该界也需相应改变。

对数强度比关于(u,v)的Jacobian为两行(-1/[u(1+u)],0)、(1/[1+u],−1/[1+v])，行列式1/[u(1+u)(1+v)]>0（内部域）。这只说明当两个B比已独立确定时可局部反演两个幅度平方，不是说现有强度表已提供它们。B比只含δ²，不能由强度比定δ号；角分布/偏振仍需相位与干涉合同。

### 下一步测什么，何时可被反驳

| 目标 | 最少补充输入 | 当前结论边界 |
|---|---|---|
| 同母态E2 out/in | 225.8的δ²或E2份额；匹配相对光子强度及共同门/效率/背景误差 | 无需先假定新τ；未得δ时不报唯一R_E2 |
| 同母态M1 out/in | 还需648.9的δ²；两线共同响应/误差 | 一个新τ不识别u/v |
| 绝对B/静态矩比较 | meanτ、绝对分支/IC、feeding/stopping与相应矩阵元定义 | 不能将相对比替代绝对强度 |
| 排他反证/曝光设计 | 预先冻结指定模型Θ及可观测预测、联合误差/原计数与响应 | 无上述输入，不报需要几天曝光或多少sigma |

原JUROGAM文章实际测过角比与部分连接线偏振，说明有相关谱学技术路线；这不保证225.8/648.9弱线的新精度。最小可复核设计应先取得匹配门条件和校准，联合约束u/v；若观测向量及其完整响应误差在指定Θ全预测域外，才可反驳该版本模型。若光子率/多极合同自身失败，应先修身份/响应，不能直接宣布手征消失。

程序system/scripts/day21_checkpoint104_same_parent_identifiability.py用声明的有理数控制点核反演、Jacobian及共同τ/归一相消；控制点不是该核实测δ，不是CAS普遍证明。首次因环境缺sympy退出1，改用标准库Fraction后实际运行成功；失败记录保留。actual_B_ratios、experimental_delta、Cov、CI和曝光功效均null。


## Checkpoint127：同母态比值的共同校准、相关误差与份额坐标

这是本任务L2解析练习/L3设计，未重分析原计数。输入沿[[lv-2019-chirality-135nd-reexamined]] LV19-D21-R104-1与R127-1/2；率合同沿[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1。保持104的同母态/匹配photon率响应、896.8纯E2及225.8/648.9仅M1/E2截断。

### 物理对象与验收范围

定义f=δ225²/(1+δ225²)，0<f≤1，R_E2=C/f，C=(I896/I225)(E225/E896)^5。f是辐射E2份额，不是总能级分支，也不给δ号。用f作坐标避免大δ端点的不便，但f→0时比值仍无有限上界；坐标变换没有补充实验信息。M1比可写D(1−f649)/(1−f225)，需两份额且避开分母为零的端点。

### 哪些共同误差相消

共同I乘性归一与共同E乘性增益在C中精确消去。共同能量加性零点a通常不消去：dlnC/da=5(1/E225−1/E896)=.0165681keV⁻¹（在打印中心处）。这只是冻结其它输入的条件导数，不估计原校准偏差；feeding、门或背景误差也不能预设为共同乘性因子。

### 完整误差合同

按x=(I225,I896,E225,E896)，局部g=∂lnC/∂x=(−1/I225,1/I896,5/E225,−5/E896)，在相应单位下Var(lnC)≈gΣgᵀ。若进一步讨论R，Var(lnR)≈Var(lnC)+Var(lnf)−2Cov(lnC,lnf)。由共享谱/角数据拟合的份额误差不能无依据独立相加。

仅为设计，若把打印.4/.06/.2/.2解释为边际标准差并允许所有相容PSD矩阵，gΣgᵀ的标准差包络是[.0237700,.1867563]；独立误差特例为.1298826。它们是局部logC的条件量，不是原实验精度、置信区间或实际协方差的估计。令a_i=g_iσ_i，Gram表示及三角不等式给上界Σ|a_i|，下界max(0,2max|a_i|−Σ|a_i|)；本例下界非零，两个端点均由声明rank1的Σ=vvᵀ实现，脚本用有理数精确核验。

另把±项仅当输入矩形盒，可由单调性求C的集合像；只有另给0<f_lo≤f_hi≤1才有R∈[C_lo/f_hi,C_hi/f_lo]。程序的f∈[.1,.2]只是声明控制，不是实测混合比/相容解或真实CI。

### 下一项测量与可证伪范围

若目标仅是相对E2比，优先取得225.8的联合份额/强度响应及共享误差，核其与896.8的门和效率匹配；总τ不能代替该份额。若独立校准证实主要为共同增益，可用相消减少该nuisance；若有能量零点或逐线响应差异，则必须保留相应导数/协方差。实际模型反证仍需同一观测的Θ与响应域，不以本包络或小C裁定手征。

代码system/scripts/day21_checkpoint127_same_parent_covariance.py与本run same-parent-covariance-scope-127.json；actual_f/Cov/CI/exposure均null。第一次误读能量脚注的执行已标superseded，纠正输入后才使用结果。


## Day22 checkpoint110：撤回旧排他机时方案，保留可执行的输入清单

旧Checkpoint128–141追加的精密δ反演、形状/交叉排他、positiveP模式证伪与16.3/45.3h预算整体撤回；原文封存在Day22run的pre-correction-110.json，不修改Day21正式卡学分或历史回执。当前仍为provisional research note，不作正式实验proposal。

原子依据：[[lv-2019-chirality-135nd-reexamined]] LV19-D22-R110-1–3；[[taras-1971-phase-defined-polarization-formulas]] T71-D22-R110-1；135Nd强度/手征范围另见[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D22-R102-1–3。

1. 先锁定225.8/648.9/896.8的共母态、终态与成分假设；两mixed线无实测δ，跨campaignMU07图点/branch身份不自动补足。
2. 为31/2−→29/2−构建phase-consistent方向/偏振联合响应，保留M1/E2干涉、m布居/feeding、角接受和gating；同一采集校准a(E)/Q(E)，包括共享误差。
3. 用pilot或明确原始计数输入分别确定signal/background、selectedpolarimetry效率、lineyield、livetime与系统误差，不能从相对Iγ=3.8假设绝对2%产额。
4. 冻结指定机制版本的参数域Θ和竞争模型的完整预测向量，再定义待检验的观测（两模型分离、P正号、或某δ分支排除是不同目标），报告型I错误/检验功效而非只给n/sqrtN。
5. 需要新τ时说明其提供绝对B；同母态份额/比值若已消τ则先补δ/匹配分支与共同Cov。不能以一条P符号直接测得三维手征轨迹或否定所有手征解释。

旧663counts下，即便沿用未验证A1=.02885，正号仅约.743个条件标准差；所推约10803counts只是反例诊断，不是新的可交付机时。源/原producer缺口由本任务跟踪，不自动变成用户待办。needs_review: true。

## Day22 checkpoint111：pilot与双bin统计合同

依据[[miller-2007-sega-polarization]] MI07-D22-R111-1/2，把任务拆为rawsignal/背景账本、几何a、偏振Q/reference及模型P(δ,orientation,gate)四层。a约定须先映射倒数；selectedsignal数量不等photopeakheadline。无背景/knowna/Q的两bin公式只作起点，实际jointlikelihood须保peak/sideband、a/Q与同reference相关。

pilot应提供各目标线的live raw/gated/selected事件率及背景模型，独立校准或可识别的a(E)/Q(E)响应；不要用16.3h反推这些输入。若a完全自由，两bin目标均值本身不能识别P；若a已被窄校准约束，必须以实际约束重做profile，不用无界witness声称真实不可识别。该页仍provisional，不授新实验或机时。

## Day22 checkpoint113：效应分离度不等检验功效

以下只用旧134未验证的A0=−.08770、A1=.02885作统计目标诊断，不认可其核/探测器预测。额外假设a=1已知、无背景、exclusiveselectedcounts且N固定，则Nperp∼Binomial(N,(1+A)/2)。对预先指定的单侧α=erfc(z/√2)/2，选择最小整数k使PrH0(Nperp≥k)≤α，再在H1下计算检验功效；z只指定假阳性率，不是检验功效或模型为真的概率。

| 条件目标 | selectedN | z对应单侧阈值 | exact H1拒绝概率 |
|---|---|---|---|
| 旧A0与A1分离 | 663 | z3，Nperp≥342 | .48666 |
| 旧A0与A1分离 | 1841 | z5，Nperp≥948 | .49188 |
| A1相对零正号 | 663 | z3，Nperp≥371 | .01101 |
| A1相对零正号 | 10803 | z3，Nperp≥5558 | .49886 |

另选1500/23000counts可在各自指定目标下给约.934/.916功效；它们不是最小设计解，也不转换成真实小时。五项概率质量/最小整数阈值/功效控制通过。原P混合模型、a/Q/背景、selectedrate和机制参数域未验证，故本表不提供D6真实预算或chirality反证。

该练习沿[[lv-2019-chirality-135nd-reexamined]] LV19-D22-R110-3区分旧均值分离与正号目标，并在[[miller-2007-sega-polarization]] MI07-D22-R111-2计数合同下说明功效定义。实际设计还需calibration/背景likelihood和指定Θ；若a/Q自由且无独立约束，增加targetN不能修复结构性不可识别。needs_review: true。

## Day22 checkpoint115：独立matched-null四计数的条件检验

[[miller-2007-sega-polarization]] MI07-D22-R115-1/2为当前225.8方案提供统计组成部分，所有数值是任务控制，不是该线实测或proposal预算。假设四rawcells独立Poisson、events独占、无背景、calibration已知physicalP0，并且energy/gates/acceptance/arrayweights使两sample共享有效a。令target(x_t,y_t)、null(x_c,y_c)，则

`odds=(x_t/y_t)/(x_c/y_c)`，`Ahat=tanh[log(odds)/2]`，`Phat=Ahat/Q`。

在行/列margin条件下，`X_t | margins ~ Hypergeom(Ntotal,Kperp,Ntarget)`；fullPoisson因子中的a与未知yield尺度消去。非零A的conditionaldistribution另乘`[(1+A)/(1−A)]^x`再归一。无需把a当精确已知常数，但null校准的计数不确定性已包含于四格联合对象，不等于“无校准”。绝对P仍需Q，sign解释须已知Q符号。

局部Poisson方差为`[(1−A²)/(2Q)]² (1/x_t+1/y_t+1/x_c+1/y_c)`，与完整四参数Fisher逆矩阵吻合；有限样本不宣称无偏或新CI。chosen整数table(954,940;900,1000)、Q=.2给P=.3、σlocal≈.16188、单侧p≈.03463；四倍chosen表p≈.00011565，不称检验功效或真实曝光。六项条件概率/直接Poisson/Fisher/失配控制通过。

若target有效a与null不同，P0也可精确给同四均值；因此conditional统计消nuisance不验证物理shareda。净峰减背景、reusedevents、非独立reference、energy插值/γ角分布造成权重不同、或未验证的“无偏振”制备，均需实际jointlikelihood/response，不能直接套表。尤其不把MI07实际single/alpha选样视为本任务独立rows已验证。更少的统计假设不替代核模型的phase/alignment/Θ；P正号或小p值不单独裁决chirality/wobbling。needs_review: true。

## Day22 checkpoint118：检验方向与区间尾部一致

[[miller-2007-sega-polarization]] MI07-D22-R118-1延续115的相同四计数条件模型。对给定margins，以alternative odds加权hypergeometric，反演包含观测x的两尾：下限满足Prω(X≥x)=.025，上限满足Prω(X≤x)=.025；边界表保留0/∞ odds极限。chosen表的central95 P区间为[−.023264,.620768]，单侧95 lower=.027894。前者含零而单侧p=.034634，不构成冲突；单侧和中央双侧的α分配不同。

这里的cross-product odds是unconditional四Poisson模型的估计，不能直接称conditional MLE；exact interval来自条件分布的尾部反演。五项尾值/极端表/小margin精确枚举检查通过，只覆盖所声明模型。真实Q、shared a、null制备、背景及事件独立性不由区间反演验证；不得把chosen控制区间作为225.8keV、SeGA或核模型的实验置信区间。needs_review: true。
