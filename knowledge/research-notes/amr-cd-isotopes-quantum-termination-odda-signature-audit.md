---
type: research-note
title: "Cd同位素AMR、量子终止与奇A签名：微观证据与条件推导"
aliases: [Cd AMR quantum termination oddA signature, AMR finite j Pauli audit]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, zhang-2013-105106cd-pnc-superfluidity, zhao-2012-105cd-cdft-antimagnetic, zhang-2019-104pd-pnc-antimagnetic-rotation, roy-2013-105cd-amr-comment-metadata, negi-2010-107in-shears-metadata]
created_from: Day26 delegated AMR isotope termination and oddA study
promotion_target: antimagnetic-rotation
tags: [antimagnetic-rotation, band-termination, pairing, signature, 105Cd, 106Cd, 108Cd, 110Cd, 107In]
---

# Cd同位素AMR、量子终止与奇A签名

## Research Trigger

本页追问三个问题：106,108Cd与110Cd的强度差异能否全部归给核芯转动；剪刀闭合是否必然伴随全核配对崩溃和形状跳变；奇A核怎样保留横向磁矩相消。原始任务中的“纯剪刀剧烈塌缩—核芯平台”是待检验表述，不是本页预设。结论分成文献结果、有限模型严格代数和未决的全核问题。本页延续正式Day26；不创建新运行、截止或课程学分。

## Grounded Evidence

| 对象 | 原件与locator | 可以支持 | 不能支持 |
|---|---|---|---|
| 106/108/110Cd寿命和E2 | [[roy-2011-cd110-systematics-antimagnetic]] printed324 Table1 | 具体自旋、误差及effective lifetime脚注 | 把所有点当无系统误差的严格单调序列 |
| 108与110配置比较 | Roy printed324–326 Eqs3–6、Figs3–4 | 该粒子加转子方案中，110无g7/2中子对齐支持、用非零核芯惯量 | 把所有Cd微观波函数强制分成纯剪刀与惰性核芯 |
| 105/106Cd配对计算 | [[zhang-2013-105106cd-pnc-superfluidity]] ZH13-01–06，PDF pp4–10 | 配对改善惯量、改变交叉；106高频需形变变化 | 配对为零是AMR必要条件 |
| 奇105Cd自洽几何/形变 | [[zhao-2012-105cd-cdft-antimagnetic]] ZH12-01–06，PDF pp11–23 | 阻塞h11/2奇中子、对称空穴、混合gd中子共同对齐 | 三支固定矢量足以解释全部波函数 |
| 105Cd争论入口 | [[roy-2013-105cd-amr-comment-metadata]] | 正式评论存在 | 未读正文时替作者编造争点或宣布争论已解决 |
| 107In身份核验 | [[negi-2010-107in-shears-metadata]] | 2010原论文题为high spin spectroscopy and shears mechanism | 题名不足以确认AMR；本次未取得可核验107In AMR寿命证据 |

## Provisional Reasoning

### 1. 重读实测数据：“平台”和“塌缩”都须给出自旋范围

Roy Table1的B(E2)，单位均为e²b²：

| 核 | 无effective脚注的点 | effective脚注点 | 读法 |
|---|---|---|---|
| 106Cd | I=18,20,22,24：0.15(1),0.14(2),0.07(1),0.05(1) | I=26：0.07，未列标准差 | 18→24降3倍；最高点反升且为effective lifetime，不能删去后声称全序列严格单调归零 |
| 108Cd | I=16,18,20：0.15(1),0.14(1),0.09(1) | I=22：0.03，未列标准差 | 不含effective点时下降40%；“下降5倍”依赖末个effective点 |
| 110Cd | I=16,18,20,22,24：0.14(1),0.12(2),0.11(2),0.09(3),0.06(2) | 顶端26寿命为effective，未给相应E2 | 16→24中心值下降约57%；16–22可称相对缓降，不能全段叫严格0.10平台 |

以上106/108点由Roy复列早先实验，不与原测量独立计数。跨不同spin范围的中心值倍率不是统计显著性检验，表中stopping系统误差也未完全进入括号误差。特别是106Cd 18→24与110Cd16→24比较，并不单凭两个末端比值就证明机制差别；仍需配置、I(ω)、强度形状和feeding约束。此前约245–414的J²/B范围不在此恢复认证。

Roy为108Cd采用π(g9/2)^−2⊗ν[(h11/2)²(g7/2)²]、jν=16、n=8；106Cd用有效jν=18与bandhead18ℏ。110Cd作者则因alignment图不支持g7/2对齐而取π(g9/2)^−2⊗ν(h11/2)²、jν=10、n=4，并引入Jc=19.5ℏ²/MeV。不同中子对齐空间和bandhead约定才是该解释的结构依据。**这里106Cd的jν=18是唯象合矢量输入，不能写成只含一对h11/2中子的量子自旋。**

在该方案，I=Ish+Jcωsh使同一剪刀角变化覆盖较宽spin范围；固定Qeff的E2下降因此缓慢。但[[amr-double-shears-tensor-core-coupling-audit]]已发现按打印Eq3直接求根不能完美重现Roy高spin平台。bandhead映射仍未解决，本页不宣称完成Fig4精确复现。

更微观的PNC-CSM给出反向约束：106Cd以固定ε2不能重现实验高频E2，需约0.14→0.12的额外形变变化；配对使105Cd剪刀闭合更明显。[[zhang-2019-104pd-pnc-antimagnetic-rotation]]又提供正常对齐增加、E2仍急降的Pd反例。因此“纯”仅指Roy给定模型置Jc=0，不等于无形变变化、无配对、无其它价中子对齐。

### 2. 量子终止：Pauli上界、配对响应与形状演化是三个问题

对同一j壳两相同费米子，完全对齐行列式只能占m=j与m=j−1：

$$
J_{\max}(j^2)=2j-1.
$$

所以g9/2两空穴Jp,max=8，h11/2两中子Jn,max=10。**仅在其余粒子固定为J=0的四准粒子子空间**，

$$
I_{\max}=8+10=18.
$$

这不同于把两支质子刃当长度4.5的可分辨经典矢量、同时令中子对为10时得到19；若中子也按两支5.5矢量相加则为20。19与20是不同经典近似，不是此有限量子空间的定理。带有gd价中子、核芯对齐或跨壳激发的实际Cd不能受18ℏ全核硬门限制。

在这个最小量子空间，最大投影态有明确结构：

$$
|18,18\rangle=
|g_{9/2}^{-2};J_p=8,M_p=8\rangle
\otimes|h_{11/2}^{2};J_n=10,M_n=10\rangle.
$$

它是该空间的唯一最大M态，无法再通过同一组粒子提高自旋。继续出现更高I要求额外对齐或改变占据空间；不要求能带、形状或配对观测量在I=18处必定发生一阶跳变。

计算脚本通过45个g9/2两粒子和66个h11/2两粒子Slater行列式计数，得到允许J分别0,2,4,6,8与0,2,4,6,8,10，各一次。空穴空间与粒子空间有同构的角动量计数。

令

$$
S^\dagger=\sum_{m>0}(-1)^{j-m}a_m^\dagger a_{-m}^\dagger,
\qquad H_{\rm pair}=-G S^\dagger S.
$$

归一J=0对有〈S†S〉=Ω=j+1/2，g壳为5、h壳为6；最大对齐对均为0。因此**指定两粒子壳的J=0单极对关联**在该最高J态确实消失。这是壳内seniority v=2的结果，不能推广为其它壳中配对都消失或全核超流发生热力学相变。尤其PNC方法固定粒子数，〈aa〉本来就是0；判断配对须使用〈S†S〉、配对能、pair-transfer或能量奇偶效应，不能把异常密度零当无关联。

最简单的n=2纯配对推转H′=−GS†S−ωJz中，J=0与g壳J=8拉伸态在ω/G=5/8处交叉；这是受控玩具模型，不是Cd交叉频率预测。实际多壳配置与配对混合可平滑或延迟占据重排；ZH13原文即显示该效应。一个量子终止态可以是同一配置的平滑极限，**终止本身不蕴含必须重组波函数、彻底配对崩溃或形状跳变**。

### 3. 经典E2归零不等于量子终止跃迁严格为零

固定等价刃和固定四极振幅时，半经典sin⁴θ律在θ=0为0；它描述辐射q=±2的几何极限。有限j量子态仍可有Imax→Imax−2的非零约化E2矩阵元；Imax+2不存在才是“同配置不能继续转动”的上界。

用单粒子约化〈j||q2||j〉=1归一，显式反对称化、单体E2算符与Clebsch–Gordan耦合计算得到：

| 有限空间 | 端点跃迁 | B(E2)/单粒子约化q² |
|---|---|---:|
| g9/2² | J8→6 | 0.02545454545 |
| h11/2² | J10→8 | 0.01561596298 |
| 固定Jp8、Jn10耦合，E2仅作用质子 | I18→16 | 0.001548255666 |

这些量无实际e²b²标度，只证明矩阵元不被上界强制为零。实际空穴符号、有效电荷、径向积分、核芯和中子有效电荷改变绝对强度。它们不是实验拟合，更不是全Cd壳模型复现。

形状也须独立核验：Zhao2012对105Cd计算得到质子β≈0.18→0.12、γ≤7°，即长椭趋近球；文中对smoothly terminating Sn/Sb所述长椭→三轴→非集体扁椭是另一条形状路径。两者共享价粒子最终对齐图像，不说明AMR必经同样的非集体扁椭终止。文中近常数J²、下降B(E2)与smooth termination二者同降的对比只作该数据区辨别线索，不升级为普适必要充分条件。

### 4. 奇A不破坏相消定理：关键是整个阻塞态的签名

105Cd已有原实验与两类微观模型讨论，不能把AMR限于偶偶核。PNC方案中的主要配置为ν[h11/2(g7/2)²]与两个g9/2质子空穴；TAC-CDFT还显示其余gd中子的混合对齐不可忽略。两篇模型共享Choudhury2010数据，不能相互计成独立实验验证。正式Roy2013评论已核实存在，全文未取得；未把争论方向或结果补写为确定事实。

取总转轴z，令U=Rz(π)。若**包括阻塞奇核子**的整个态满足

$$
U|\Psi_r\rangle=r|\Psi_r\rangle,
\quad r=\pm i\quad(\text{half-integer spin}),
$$

且磁偶极是轴矢量，则

$$
U^\dagger\mu_xU=-\mu_x,\quad
U^\dagger\mu_yU=-\mu_y,\quad
U^\dagger\mu_zU=\mu_z.
$$

于是〈μx〉=〈μy〉=0而〈μz〉可非零。相位r在期望值里相消，r=±i与偶偶r=±1具有同样相消结论。密度矩阵版本为[ρ,U]=0；若时间依赖或自洽解破坏此不变性，不能沿用结论。

若空间反射本身破缺，但simplex S=PRz(π)守恒，磁矩在P下为偶，仍可用同一证明令横向期望为零。这里simplex为本页条件推广，所读Cd论文没有独立实验证明每条奇A带都严格保该对称。离散对称性**允许并约束**相消，仍需动力学检验基态/自洽极小及阻塞轨道是否实际保它。

不要用A=Ry(π)T替代上述证明。轴矢量在A下变为(μx,−μy,μz)；保持A只迫使μy=0，μx仍可有值。它只保护平面性，不单独保护两个横向分量都零。单独T把有向自旋反号，旋转态并不因此恢复T；TAC-CDFT也明确指出奇核子流在ω=0可破坏T。

### 5. 期望值相消、M1跃迁选择与AMR鉴别仍是三层

对U的本征态，球张量μ1q满足相位选择：同签名r_f=r_i时奇q分量矩阵元消失；异签名可允许。对同一ΔI=2序列，相邻能级M1受一般角动量三角条件禁止。二者均不能推出所有跨带M1严格为零。若阻塞轨道或混合态破坏U，横向磁矩可以恢复；小破缺时振幅一阶恢复、强度二阶恢复。

签名守恒还存在于普通主轴转动；横向静态期望零也存在于许多好角动量态。因此该代数不能单独确认AMR。仍要结合自洽双剪刀占据、微观电流、寿命与E2、惯量、可能交叉及替代的普通转动/终止解释。

107In尤其要保持身份边界：本次取得并核验的Negi2010原始元数据是“High spin spectroscopy and shears mechanism in 107In”，未取得证明107In AMR的完整实验来源。此时回答应是“105Cd有AMR文献、107In本次尚未核验”，不能因两者均奇A而把107In写成已确立AMR，也不能据未检得声称绝不存在。

## Reproducible Artifacts

目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-termination-oddA-20261029/`。

- `amr_quantum_termination_audit.py`：标准库实现Wigner3j/CG、两粒子反对称Slater态、单体E2及单极配对范数；无外部核模型代码。
- `quantum_termination_audit.json`：有限j允许态、上界、配对范数及非零终止跃迁；明确不是全Cd计算。
- `cd_BE2_reinspection.csv`：逐核逐自旋数据及effective脚注，没有擅自补误差。
- `acquisition.json`：实际PDF签名、字节、页数、哈希及Simons403、评论401失败。
- `metadata-acquisition.json`和Crossref原回包：原始元数据载荷身份。

## Assumptions

量子计数固定两相同粒子/空穴的单j壳与其它粒子J=0；配对玩具只含单极S†S；E2数值按单位单粒子约化矩阵元，没有径向/电荷标度。奇A期望值定理要求整个态或密度保签名/simplex，包含被阻塞奇核子。原文推转图中RMS向量不等于有向单刃观测。

## Competing Explanations

下降E2可能来自几何闭合、形变减弱、占据/配对重排、普通终止或feeding偏差。核芯角动量和核芯电荷四极振幅不同；固定惯量的角动量模型不自动提供后者。有关105Cd正式评论未读正文，保留争议入口。

## Transfer Conditions

Pauli计数、张量变换和签名相位推导可跨区迁移。特定j空间最大I、Roy Jc/jν、拟合形变、有限j单位强度及实验J²/B阈值不可无条件外推。

## Failure Conditions

若把有效寿命当独立精确寿命、把18ℏ当全核上界、把有限壳〈S†S〉=0当全核配对坍缩、把〈μ⊥〉=0当所有M1跃迁禁戒，或把107In的shears题名当AMR确认，本页结论失效。若奇轨道破坏总签名，须重新求横向矩与电磁矩阵元。

## Falsification or Reverse Tests

同一I最大态的E2数值反例检验“终止意味着严格零E2”；固定非零配对的PNC研究检验“AMR需要配对先崩溃”；A=RyT仍允许μx的变换律检验“平面对称保证完全横向相消”。对真实核应增加独立静态四极矩或寿命、pair-transfer或关联能、配置可辨的γ支路及末端形状约束。

## Open Questions

Roy110Cd bandhead与Eq3映射仍待原代码确认；105Cd评论正文及reply未取得；107In是否有独立AMR寿命证据仍须原始论文；本次没有Cd完整投影多体终止波函数。后续高价值路线是同一Hamiltonian/EDF中计算占据、pair关联、βγ、绝对E2及弱带间M1，避免把来自不同模型的图像拼成唯一微观机制。

## Knowledge Impact and Learning Decision

`supports` 奇A签名保护下的横向相消与有限空间Pauli终止；`revises` 纯剪刀等于无配对、110全段严格平台和终止必然全核配对崩溃的表述；`limits` 107In未核验AMR、评论正文缺失和全核波函数终止未完成。未恢复历史013普适阈值或单独T认证。

## Sources

- [[roy-2011-cd110-systematics-antimagnetic]]
- [[zhang-2013-105106cd-pnc-superfluidity]]
- [[zhao-2012-105cd-cdft-antimagnetic]]
- [[zhang-2019-104pd-pnc-antimagnetic-rotation]]
- [[roy-2013-105cd-amr-comment-metadata]]
- [[negi-2010-107in-shears-metadata]]

## Human Review

Codex source/claim self-audit，保持unreviewed；未升级human-reviewed、未更改既有撤回或课程信用。

## Review Status

有限j代数计算已执行，来源字段与载荷已记录；全核终止波函数、正式评论正文和107In AMR实验归属仍未解决。

## Promotion or Rejection History

2026-10-29：新建Day26 AMR后续笔记，新增有限量子空间反例和奇A条件证明；原文结果、模型输入与本任务推导分列。所有未取得来源保留失败边界。

## Continuation Handoff

主代理可从本页与worker JSON直接续接。发布交由主代理统一处理；本worker不提交。优先取得Roy2013评论与reply，随后再决定是否补105Cd实验source；不以更多模型重复引用取代独立寿命。次要路线为107In AMR原始证据与Cd同一微观框架的终止配对/形变联合计算。
