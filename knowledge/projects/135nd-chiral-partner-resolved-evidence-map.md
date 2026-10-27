---
type: project
title: "135Nd手征伙伴带：实验、TAC/RPA与竞争解释证据图"
aliases: [135Nd chiral partner-resolved evidence map]
created: 2026-10-26
updated: 2026-10-26
status: active
review_status: unreviewed
confidentiality: public
project_stage: evidence-map-and-model-validity-audit
nuclei: [135nd]
tags: [chirality, partner-bands, tac, rpa, evidence-map]
---

# 135Nd手征伙伴带的逐量证据图

## Agent active summary

本页把[[nuclear-chirality]]中分散的Day24预习整理为可续接的正式研究入口。2007实验对伙伴带的支持保留；TAC/RPA的等强曲线、平均场临界点与实验最近接近点分别归类。Almehed2011进一步区分同I能隙与共同ω的routhian差、有限aplanar窗口、模交叉与局部坐标条件数；不是135Nd参数补表。Qi2009作者Fig5的正半整数网格现已识别并与PDF匹配，完整相干波函数/绘图producer仍缺。2002早期gyro/HF原稿新增了有参数的均匀转动onset与作者自身替代解释，未当2004VoR或135Nd阈值。绝对强度的逐线normalizer、同I/同family的完整EM块、相干信息及两partner的g向量仍缺。本页不改变Day21/22/23学分、人审或撤回；新综合全部`needs_review: true`。课程是否完成只由本日runner审计决定。

## Research Question

在锁定历史Band A/B身份后，哪些量直接支持135Nd的手征伙伴解释，哪些来自特定TAC/RPA动力学，哪些仍能由crossing、组态变化、γ-softness或band mixing重现？不能只凭同核名称将此三准粒子家族与低spin单νh11/2 TiP家族互换。

## Evidence Available

### 伙伴带观测账本

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] Table I（printed172501-2）的原打印量如下。τ为mean lifetime，B为该实验经寿命及分支推导的强度，不是直接计数；单位依次ps、μN²、e²b²。B列不自动绑定到作者未列出的逐条γ。小括号为原打印误差；不假设相互独立。

| Iπ | τA / τB | B(M1)A / B(M1)B | B(E2)A / B(E2)B | 证据属性 |
|---|---|---|---|---|
|31/2−|0.75(8) / 1.46(2)|2.5(3) / 2.7(3)|0.32(3) / 0.28(3)|同一DSAM/分支推导链|
|33/2−|0.44(2) / 0.87(6)|2.2(2) / 2.1(2)|0.32(3) / 0.28(3)|同上|
|35/2−|0.28(2) / 0.64(5)|2.4(3) / 2.2(2)|0.32(3) / 0.28(4)|同上|
|37/2−|0.23(2) / 0.48(3)|1.7(3) / 1.7(2)|0.32(4) / 0.29(4)|同上|
|39/2−|0.22(2) / 0.24(4)|2.1(3) / 1.9(3)|0.13(3) / 0.11(3)|同上；不单点命名静态阈值|

|量|实验/评价实际支持|模型与作者解释|本任务边界及必要输入|
|---|---|---|---|
|同I能量|原2003建纲图与MU07 Fig4能量点；既有官方snapshot在31/2…39/2的EB−EA中心为356.8/280.8/184.1/118.1/95.2keV（MU07-D24P-001、ZH03-D24P-001）|MU07把零/一声子带间差与RPA能量比较|评价字段不算第二次测量；要回原energy/assignment误差和谱系，不将最近接近点等同模型ωc|
|带内M1/E2及比|Table I与Figs2/3的实验点支持作者所称误差内相近；两种B的商不是δ²|TAC曲线供两带共同基线，谐振RPA不改期望值（MU07-D24-001）|等强理论曲线不能作为第二个独立验证；表内derivedB、B比与同τ不重复计票|
|跨带M1/E2|Fig2是M1，Fig3是E2；B→A open-circle图点是实验派生系列，不是RPA线|RPA波函数给带间率；原文承认带间E2偏低，M1 spin趋势也有差异|作者矢量图缩小转录误差，不补parent/Jf/component/absolute-vs-selected normalizer；MU07-D24P-004–010保持条件性|
|三轴角动量几何|τ/B没有直接测出三轴有符号分量；没有由图点单独确定左右手局域概率|FM97固定形状PRM/TAC奠基；MU07最低RPA模以取向涨落为主、有小γ振动混入|固定γ模型不验证实核γ刚性；需实际波函数、形状/取向联合分布及定义清楚的算符|
|g因子|本次已读MU07全文未报告两partner g；当前未获得可绑定向量|组态/算符可产生可检验g预报，但须独立定标|写unknown，不写0；128Cs bandhead测量不能搬入135Nd；g相近也不单独充分|
|采集与误差|175MeV、100Mo+40Ar、thick target Gammasphere；BLUE双门逐ring与LINESHAPE；5000 recoil histories、0.002ps步长、SRIM stopping、局部χ²寿命误差|理论形变/配对是另一条输入链|图/评价/综述复述不是新增采集；jointCov、逐门feeding/branch ledger仍缺|

## 模型有效域及所用输入

[[frauendorf-meng-1997-tilted-rotation-chirality]] FM97-D24-001/002：给定形状的h11/2粒子/空穴加三轴转子，irrotational惯量，TAC把I换经典J并作均场因子化；量子PRM仍有隧穿劈裂。Fig7带间强度抑制是该参数模型结果，不能把实核任何跨带线一概视作反证。文中134Pr高spin跨带未见同时受弱布居限制。

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24-001/002：PQTAC用N=4、5两个major shells，QQ力及constant pair gap，以Strutinsky PES定参数；质子/中子gap分别取odd-even mass difference的50%/80%，是模型输入。RPA含取向、形状及两qp谐振自由度；最低模以取向为主，不等于模型完全删除γ涨落。well below transition时谐振可用；零频/非零φ的均场临界与实测最近接近点相差约1ℏ，临界区方法失效。没有由这些字面输入恢复原producer或从图推确切ωc。

## 近似阶次练习：等强来自什么

以下为本任务推导，来源背景为MU07 printed172501-3 Eq3后和printed172501-4非谐性段；不是作者原程序重放，也不是实核拟合。

用dimensionless小取向坐标q的谐振近似，H=p²/(2𝓜)+𝓜Ω²q²/2，令v=ℏ/(2𝓜Ω)。q为角度（radian），𝓜的量纲使𝓜Ω²为能量。取一个内禀算符分量F(q)=a+bq+cq²，则

$$\langle0|F|0\rangle=a+cv,\qquad
\langle1|F|1\rangle=a+3cv,\qquad
\langle1|F|0\rangle=b\sqrt v.$$

线性算符截断（c=0）下两态对角期望相同，同时允许非零带间振幅；保留曲率项后差为2cv。这说明“振动不改期望值”对应近似阶次。这里对角期望是内禀分量练习，**不是不同I间实验B的RME**；没有把它直接平方成135Nd带内率。实际带内/带间还需正确spin映射、EM张量、波函数和归一。

若Ω→0或a接近角几何零点，小振幅/相对修正展开可能失效；数学发散不能外推成实核测得发散。MU07的θ≈45°敏感性/非谐平均倾角讨论因而应和谐振等强基线同时保留。能隙变小、平均场分岔、有限体系隧穿与实验最小split是四个不同对象。

## Current Hypotheses

### 四条竞争路线与可证伪输入

以下是研究设计，均`needs_review: true`；未实际拟合，不给解释胜负或同等可信度。

|替代路线|可重现的局部特征|必须新增的可检验内容|能改变判断的检验/当前缺口|
|---|---|---|---|
|crossing|两同I候选能级靠近、alignment或能量斜率变化|指定crossing双方组态/形变、保持连续的state mapping，给跨区间全网络预测|单一spin近合不够；同reference能量/对齐、逐态τ与BR/ICC及两侧强度需联合核验|
|configuration change|不同组态也可能有相近能谱或B比|固定H/算符的本征态mapping须过能量、Jπ和全部links；若增加原空间未含的qp组态须声明模型改变|只改标签不产生新预测；独立g/绝对B可作holdout，但当前双partner g与actual producer未得|
|γ-softness|形状/取向涨落可影响能隙和EM|联合shape-orientation动力学，说明刚性极限与混合、同算符的EM趋势|FM97固定γ范围不证明刚性；MU07小γ admixture也不量化实核完整γ分布|
|band mixing|近交叉时强度可重新分配，某些局部峰/谷可来自混合|同Ii/If完整RME块、相位/可用干涉约束、包含遗漏态的空间及归一|只看两条带不能证明封闭；MU07-D24P-008列缺失反向outlets，未观测不设0|

### 四路线的实际检查范围

上表是本核可证伪设计，不表示已经完成四套135Nd替代fit。[[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D25P-001–003给另一核134Pr的crossing/mixing条件例；[[almehed-2011-chiral-vibrations-a135]] AL11-D24-003的RPA模交叉不是实验组态crossing。MU07的小γ混入没有测得完整γ分布，[[chen-2016-two-dimensional-collective-chiral-wobbling]]的θ/φ softness也不等γ-shape softness。

新[[larsson-1978-nuclear-core-quasiparticle-coupling]] LLR78-D24-009/012提供历史跨模型控制：共享已用core参考量后，换γ-unstable/rigid芯可只小改所选odd-A能谱而保留EM差，表中γ4→ground4软/刚B比约3.29163。它说明应检验未用于定标的结构量，不是在A193示意芯之外已经拟合135Nd或133Ce。冻结输入的目标核预测/逐态assignment与响应未得时，结论是相关路线尚未完成比较，不凭机制名字授相同可信度、也不抹去本核实验正支持。

### 原方法的同ω交叉与同I混合不能互换

[[bengtsson-ragnarsson-1985-rotational-bands-particle-hole]] BR85-D24-004/005/013是新原件例：cranking虚avoided crossing在同ω交换波函数，实际配置相互作用应同I；其平滑diabatictracking有意去弱交互，不能由此证明真实混合为零。作者粗(N_rot,α)configuration内还可有多个band，保持粗label不等保持同一态。130Ce的tracked较小shape支与globalyrast换路线分开，是可解析比较，不是本135Nd四替代fit已完成。

这为四路线表补一个真实方法范围：不同matching/能量ensemble/空间会改变所比对象。AL11的RPA模交叉、本源single-particle虚交叉和实验同I bandcrossing分别记录；不能合一个“crossing”标签后说已排除或确认135Nd模式。真实MU07实验支持仍保，fullnormalizer/g/actualproducer不因更多历史方法自动补齐。

### particle–hole参数对偶不等左右手伙伴

[[meyer-ter-vehn-1975-triaxial-rotor-particle-model]] MTV75-D24-001–006的单j等谱把particle/hole、γ、λ和轴/配对一同映射，是声明模型的参数对偶。FM97讨论同一给定模型内左右handedness及finite tunnelling的对象不同；不能用两套对偶参数同谱给实验chiralpartner增加一份独立验证。该源还直接显示等谱下E2/M1可有不同relative sign行为，故energy与unsignedEM相近不代完整signedobservable核验；此不是135Nd实际δ/g预报。

## Risks and Blockers

### What is established vs what is not

Established（本次已读来源范围）：MU07实验报告的伙伴电磁相似性及TAC/RPA总体比较，是135Nd手征解释的正支持；FM97给几何和量子恢复的理论基础。两篇原件的任务边界不同，不能互相冒充新实验。

Not established：模型无关的静态手征起始spin/硬阈值、全部branch/normalizer闭合、两partner g、唯一三维取向、排除所有crossing/组态/γ-softness/混合路线。既有Pr/Au争议不能自动否定本核正支持；本页也不恢复Qt代理CI、225.8keV正P、机时排他认证。

## Knowledge Impact and Learning Decision

`supports`既有135Nd实验支持链；`limits`把共享TAC带内曲线、RPA零频和实验阈值捆绑的推理。下一步优先完成既有原模型后续方法对取向/形状模和近临界非谐性的原文核对；只有具体endpoint/normalizer输入有进展时才重开强度库存问题。

## Next Actions

Almehed2011原方法本轮已核，未提供135Nd逐行input/line-normalizer，单凭此文继续追该输入已无新增信息。Qi2009本核有限量子模型及作者投影网格已在本轮核验；原producer/相干波函数未随作者archive给出。128Cs高spin DSAM与bandhead TDPAD的逐态companion对照本轮已补；下一主问题优先目标核的原量定义/独立实验或可解析模型输入，先重建候选，不将任意toy拟合冒充actualproducer。四条竞争路线须各自提供可冻结参数的预测及holdout，才进入实际比较。

## 共同转频不等同共同自旋

[[almehed-2011-chiral-vibrations-a135]] AL11-D24-001的Fig3是共同转频网格上的实验routhian差，需先锁定该比较对象。令ν=ℏω、I为以ℏ计的无量纲自旋，局部连续近似下

$$R_b(\nu)=E_b(I_b)-\nu I_b,\qquad E_b'(I_b)=\nu,$$
$$\Delta R(\nu)=E_B(I_B)-E_A(I_A)-\nu(I_B-I_A).$$

同ν允许IA≠IB，所以本页表中的同I能隙不是直接的RPA phonon能量检验输入。离散spin的频率定义、插值、alignment/reference、误差相关与可能的crossing都要保留；此式不替代论文实际插值算法。

一个可核代数例取EA(I)=I²/(2𝒥)、EB(I)=D+(I−a)²/(2𝒥)，其中𝒥的单位MeV⁻¹，a无量纲、D为MeV，则IA=𝒥ν、IB=a+𝒥ν，有

$$\Delta R=D-a\nu,\qquad
\Delta E(I_A)=D-a\nu+\frac{a^2}{2\mathcal J}.$$

这只证明两种量可不同；未给任何核素拟合参数。a=0且两曲率相同才回到此特例中的相等，不能从中央same-I gap补RPA/隧穿阈值。

## 有限aplanar窗口与模追踪

AL11-D24-002的136Pm**模型**TableII在ν=.10/.15、.20/.25/.30/.35、.40/.45/.50依次给φ=0、20/38/52/77°、90°；中间四行Ω列横线保持missing。进入/退出的位置只能按此粗网格识别变化区间，不将横线填零或插值为精确临界。其返回90°平面后的谐振解不说明更高spin一定更静态，也不把邻核2qp参数迁到135Nd三qp。

AL11-D24-003提供两个不同的身份检查：134La最低ordinal模在crossing处可换性质；转动spurious零模与物理soft模要区分。若将来取得actualRPA输出，至少保留每个ω的eigenvector、X/Y norm、与转动生成元的耦合/解耦诊断，以及选定规范/metric下的跨步overlap，再把能量和EM连续性共同用于追踪。近简并时需追整个子空间，不以单一vector phase或ordinal作固定身份。此为任务设计，不声称已完成原producer检查。

## 四极坐标反演：奇异、软化与算符身份

由AL11 Appendix A，记q0=〈Q0〉、q2=〈Q2+〉、Q=Cε，q0/Q=cosγ、q2/Q=−sinγ。φ0 chart在radian小角下，令u=(Δφ,Δθ,Δψ)，响应y=(ΔQ2−,ΔQ1−,ΔQ1+)/Q，则

$$y=J_{\rm or}u,\qquad
J_{\rm or}=\begin{pmatrix}
-2\sin\gamma&0&-2\sin\gamma\cos\theta\\
0&-\sin\gamma-\sqrt3\cos\gamma&0\\
0&0&\sin\theta(-\sin\gamma+\sqrt3\cos\gamma)
\end{pmatrix}.$$

shape部分对(Δε/ε,Δγ)的normalized Jacobian为

$$J_{\rm sh}=\begin{pmatrix}\cos\gamma&-\sin\gamma\\-\sin\gamma&-\cos\gamma\end{pmatrix},\quad J_{\rm sh}^{T}J_{\rm sh}=1.$$

这只是特定坐标和欧氏范数的局部逆问题。ε=0时整体shape scale消失，轴对称γ=0时某取向不可辨，θ=0时该Euler chart失效；这三种情况不等于同一种物理软化。

`system/scripts/day24_al11_tensor_conditioning.py`从真实PDF5读取55行，**只对其中30个φ0行**使用上述chart，以Cartesian对称无迹tensor的Rodrigues旋转中央微分独立检验。normalized orientation condition number为约2.712–6.678，最大微分残差约1.34×10⁻¹⁰；157控制通过。φ90/aplanar行不强套，图上的Δφ/Δψ也未重新数字化。这说明所选非退化几何并未强迫反演奇异，不能把真实RPA软化一概说成坐标伪影；也不能用有限条件数认证近谐动力学。

AL11-D24-004还约束observable身份：这些shape/angle分解来自BK修正QQ张量，不自动等于physical electric E2 charge tensor的实测分布。具体EM另用effective charges和g；本文邻奇奇核80%配对输入不能覆盖MU07对135Nd质子50%/中子80%的输入。比较同模型谱系时仍须逐版本/核素/operator核对。

## 三来源REFLECT：支持链与解释范围

FM97奠基的固定shape PRM/TAC、MU07的135Nd实验与PQTAC/RPA、AL11的邻奇奇核方法扩展各提供不同信息。共同支持是取向集体运动可产生双带并与EM比较；差别是有限体系劈裂/隧穿、同ω/同I比较、shape/EM张量和原参数合同。本文三来源没有因重复引用而增为三次135Nd实验，也没有因AL11承认某邻核趋势失败而否定MU07全部正支持。

本次belief revision为`limits`：撤去“高spin更静态”的无条件单调图像，保留模型的有限窗口；要求先确认能量比较坐标及模身份。`supports`：近谐和非谐边界须与角动量几何共同检验。未解决的最高信息缺口仍是本核原branch/normalizer、actual模型job和独立伴随量，不用更多表示小数位关闭。

## Agent self-audit triage

|级别/项|已核证据与本任务判断|未核验风险/后续|
|---|---|---|
|P1 实验支持与归一|原Table I/Figs1–4回读；支持链保留，逐线missing不伪补|图点identity与normalizer仍条件化；论文措辞逐claim回源|
|P1 理论等强与临界|MU07-D24-001/002原文；近似阶次推导明确标为任务推导|不可把谐振截断升格为普适等强/阈值定理|
|P1 竞争解释|FM97-D24-001/002支持适用域，其余为待检验设计|未拟合不分配胜率，不把列名当已有独立反证|
|P2 导航与信用|canonical链接到两source及概念，source反链已补|本页不授分、不更改原人审或撤回|
|P1 共同ω/模/算符|AL11-D24-001–004原文/图/表核到；同I gap、模型窗口、ordinal和BK/charge tensor分别保留|邻核/模型结果不当135Nd新事实；未复现actualRPA|
|P1 局部条件数|AL11-D24-005；实际TableII＋Cartesian微分仅检查φ0局部映射|条件数依赖规范/尺度，不作物理权重、Cov或非谐误差|

## Sources

- [[mukhopadhyay-2007-135nd-chiral-vibration-static]]，MU07-D24-001/002；Table I、Figs1–4；既有D24P-001–010。
- [[frauendorf-meng-1997-tilted-rotation-chirality]]，FM97-D24-001/002；Eqs6–12、Figs1–9。
- [[zhu-2003-135nd-composite-chiral-pair]]，ZH03-D24P-001（既有谱系/端点定位，本轮未重读全篇）。
- [[almehed-2011-chiral-vibrations-a135]]，AL11-D24-001–005；arXivv2 PDF4/5/7/14–18。实际公开staging已核，raw归档/VoR仍deferred。


## Qi2009：正半整数投影网格及有限模型窗口

[[qi-2009-135nd-particle-rotor-chirality]] QI09-D24-001–003把有限量子PRM接入本图，而非增加一套135Nd实验。固定形变/能谱定标能处理有限核劈裂并给transient解释；该v1的39/2与76keV属于原参数模型。实验/PRM/TAC-RPA三层保留，跨带E2的剩余偏差也保留。Ref21引用Almehed的v1，与本页当前已读v2逐版本区分。

本轮取得官方作者archive，并纯文本解码Fig5 EPS：三轴×两band×六spin的36系列，共690个样点，半整数positive-K网格为.5,1.5,…,I。对照原PDF的全部690颜色/顺序及位置，仿射变换只由三个黑色图框锚点固定，最大偏差约.00250pt；去投影后的half-grid残差≤.0669K。此数值是绘图坐标精度，不是物理CI或模式通过门。

正K绘制纵坐标和约.9915–1.0041，与整数绘图坐标±.5舍入模型下的1相容。这支持把图视为已归一的受限/折叠表示之候选，却不能唯一识别actual producer如何fold、bin或插值。正文“P(Ki=0)/P(Ks=0)”仍不是该离散半整数基下一个实有K0本征投影；图中没有K0样点，作者的近原点连续语言与离散概率合同需分开。

由γ=22.4/97.6/142.4得到同一套shape eigenvalues的置换，也只核轴交换；它不提供沿三轴同时可测的经典随机向量。三个单轴边缘概率仍不能恢复相对phase、全部signedRME或左右手局域化/隧穿路径。作者在给定PRM动力学下的解释保持为正模型支持，本任务不把表示疑问升级成paper错误判决。

此项`supports`的是半整数网格/表示身份和有限量子模型路线，`limits`的是把原点叙述、RMS和模型76keV直接转为实验几何/阈值。主要伴随输入仍是actual signed wavefunctions/EM输出及独立实验向量；增加绘图小数位不能关闭它们。


## 128Cs独立伴随观测：核素相同仍须逐态、逐run

[[grodner-2006-128cs-chiral-doublet-lifetimes]] GR06-D24-001/002和[[grodner-2018-128cs-chiral-g-factor]] GR18-D24-001/002是本页方法对照，不给135Nd补任何g或τ。

|输入链|实际对象/装置|可以约束|不能直接迁移的字段|
|---|---|---|---|
|GR06 DSAM|128Cs高spin伙伴；Warsaw55MeV、40mg/cm²Sn、OSIRIS-II；例yrast(18)+ .82(+.20/−.14)ps、930→(16)+|经feeding/BR/停止历史的τ及派生M1/E2，伙伴比较|不是9+ isomer g或全级联每态的g；派生B不独立于τ/BR|
|GR18 Orsay TDPAD|采用9+、T1/2=56ns bandhead；55MeV但22mg/cm²Sn、pulses/磁场/LEPS|多条下游γ共同读同isomer的ωL/g|不是九个level各有g；高转换未见支路及spin采用边界保留|
|GR18 Stony TDPAD|独立47MeV、Sn/Pb、另一场/脉冲/LEPS角组|另一采集对同isomer的g约束|同核/组态/参考物理输入仍可共享，不能把全部误差当独立|
|PRM/CDFT几何|指定β/γ/g/组态、spin与算符|解释特定g与几何的联系|geometry仍为模型层；既有signedχ/RMS/Gram定义问题不自动解决|

两种技术研究同一正宇称family，但读出的状态和clock不同。采用56ns为half-life，有mean=56/ln2≈80.7909ns；与选定.82ps寿命相比约9.85×10⁴倍。若仅假定两态同参考absωL=.0625×10⁹rad/s，则rank2调制在各自mean寿命内累积相位2ωLτ约10.10rad及1.025×10⁻⁴rad。它解释技术选择的尺度差；该假定不提供高spin新g、actualresponse或机时预算。

可执行的联合检验需把各状态的τ/B/g向量绑定到同一模型随spin的预报，并保留各采集的response、stopping/feeding/field nuisance及共同assignment。不同采集可带来独立信息；数据独立不意味着模型、参考g或spin链也独立。当前已有跨spin信息不等同已测得同I两partner g，不能用9+近planar的模型推断全带无chirality，也不能把高spin EM支持反向证明bandhead静态。

本次`supports`的是独立companion可增加约束，`limits`的是按核名/反应名或共享下游γ把观测合并。后续应优先取得同I/同partner的可绑定观测或明确的模型spin迁移合同；本图135Nd的双partner g仍为unknown。


## 临界频率原稿：分岔、soft模、量子劈裂与实验spin

[[olbratowski-2002-critical-frequency-preprint]] OL02-D24-001–005是关联2004PRL的2002三作者v1，原读公式/结果只归该版本。固定s/l gyro与常惯量、均匀ω条件给ω×I=0，并将planar分支与μ=𝒥_m的aplanar分支分开。Eq7的ωc依s_s/s_l及两个惯量差，等号处m分量仍零；非零±m两支在严格大于ωc后出现。

源132La参数5.43/5.00ℏ及8.5/31/20ℏ²MeV⁻¹给ℏωc≈.514639MeV，另一个新planar分支阈值≈1.282267MeV不是它。原HF在.6MeV找到chiral continuation，作者却明确这个起始高于实验候选频率，并在Fig6保留下带planar/上带axial-l的能谱替代解释。新source因此给出必要的反证/方法范围，不能把“模型允许aplanar”直接变成实验排他结论。

这组条件下的连续经典Icrit≈15.9538ℏ，不等实验量子I。2002计算还关闭pairing/time-odd、只用特定组态及14shells；给定常惯量已含odd-nucleon小横向响应，不能重加。它没有量子化左右handed分支的耦合，不计算有限隧穿劈裂。与MU07/AL11的RPA能量、Qi09的量子PRM谱、实际same-I实验gap，各自仍需自己的映射与有效域。

本次三来源之外的新REFLECT为`limits`：经典起始、均场分岔、RPA零频、有限核双带gap和实验候选出现spin是五个对象；即使一个模型把它们近似联系，也须核其输入/核素/比较坐标。root独立代数复算只检源参数，不补135Nd g/branch/normalizer或统一临界门。


### 图上扣参考能量不等Routhian

[[olbratowski-2002-critical-frequency-preprint]] OL02-D24-006明确Fig6横轴为连续经典I、纵轴E−I²/(2𝒥_m)。它与本页的common-ω Routhian及same-I实验gap是不同对象；该经典chiral水平线约−1.791584MeV来自固定参数代数，不是零激发能、量子双带gap或135Nd尺度。独立两路线局部曲率检查支持所声明分支合同，仍没有实际RPA谱/隧穿/实验误差。

## 集体量子化：有限隧穿与遗漏坐标

[[chen-2013-collective-hamiltonian-chiral-modes]] CH13-D24-001–009提供TAC能面到有限量子谱的一个直接桥。它是固定γ、单j对称粒子-空穴示意体系；不是本页135Nd三准粒子的actual输入，也不增加一次实验。读本为16页arXivv2，VoR未核。

|层次|该源实际做了什么|不能跨越的边界|
|---|---|---|
|势与坐标|V(φ)=minθ E′(θ,φ)，φ在±π/2之间连接左右取向|θ随最小化路径可变，但没有其量子动能；固定γ不检实核γ软度|
|质量|cranking激发求和，使用小幅激发和Ω处方；rotation域设Ω≈0|这是质量近似，不是最终量子gap=0；不能称完全无近似惯量|
|量子化与边界|Pauli算符、√B dφ测度、B^−1/4基及Dirichlet壁|盒壁是作者近似；图中abs(ψ)²不是不加说明的flat角度计数|
|静态regime|高频势垒增高、偶/奇低态相近而仍有限gap|双极小起始时量子态仍宽广；偶/奇φ不是核空间宇称或永久单手定态|
|高频反例|原PRM约.35MeV后gap重开，1D collective继续下降|作者明确未含second chiral vibration；不支持无条件高spin更静态|
|比较坐标|在固定ω下比较集体与PRM能量|没有good-I；同I两带的ω可不同，不能直接当same-I实验gap|

本页已有近谐练习描述单阱小涨落的阶次；该集体H允许跨井量子波函数，却仍有其mass/路径/边界近似。OL02经典±m分支、MU07/AL11局部RPA、Qi09量子PRM和CH13一维集体谱因此各有独立合同，不能按“更量子”简单排序后忽略自己的失败区。

### 取向奇量与能量本征态

CH13-D24-006/007的对称φ Hamiltonian，在偶测度下使非简并偶/奇本征态的任意φ奇量期望为零。左右偏向组合可用两态相干叠加构造；有限ΔE时一般非定态。这是本模型空间的条件推断，不能用φ反射的unitary标签替代真实核反幺正手征操作；后者的phase/Kramers边界见[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]] F01-D24P-001/002，属于既有Day23预习。

要让此方法区分135Nd的crossing/configuration/γ软度/mixing，需要本核势/质量/遗漏坐标敏感性、同I映射及EM算符/完整连接，不能只把原示意模型的相似|ψ|²或.01MeV小gap贴到实验点。两个partner的g与actualEM/normalizer缺口继续unknown。

## 固定ω和固定I的全局分支

来源前提为[[olbratowski-2002-critical-frequency-preprint]] OL02-D24-001/002/007。以下是冻结gyro/常对角惯量模型的条件推导，新增needs_review:true。实际HF、量子谱和实验spin映射不由它认证。

给定|ω|时取R(ω)=−½ωᵀ𝒥ω−s·ω，stationarity为(μ1−𝒥)ω=s；给定|I|时取H(I)=½(I−s)ᵀ𝒥⁻¹(I−s)，stationarity为ω=λI。μ有惯量单位、λ有逆惯量单位，只有两者有限非零且矢量非零时才可写λ=1/μ。Euler条件是共线，并不要求每条平面分支ω/I正平行。

对同一球面上的任意另一点，展开二次目标并用相等模长，得到精确证书

$$R(\omega)-R(\omega_*)=\tfrac12\delta\omega^T(\mu1-\mathcal J)\delta\omega,
\qquad H(I)-H(I_*)=\tfrac12\delta I^T(\mathcal J^{-1}-\lambda1)\delta I.$$

所以μ≥max𝒥与λ≤min(1/𝒥)分别给全局最低的充分证书，不只是在抽样根中挑最小。两种约束的切向Hessian、单位和最低分支不同，不能把其特征值直接命名RPA频率。

|约束范围（仅源参数）|全局最低分支/边界|
|---|---|
|0<ω<ωc|fixedω最低R走A，μ>𝒥m；超过ωc为±m两aplanar支|
|0<I<S，S=abs(s)=7.381388758ℏ|fixedI最低H走D，λ<0/μ<0，ω与I反向；源Fig4低I yrast正是D|
|I=S|I=s、ω=0、H=0；λ=0而μ chart发散，不把奇点当新相变|
|S<I<Ic|走A，0<λ<1/𝒥m；Ic=15.953810437ℏ后为两aplanar支|
|原点|约束球塌成单点，不能当regular Lagrange chart|

在同ℏω=.60MeV，平面A有abs(I)=17.555718ℏ、R≈−7.326829MeV，aplanar有18.6ℏ、R≈−7.371584MeV。因此这两个R之差比较不同I，不能写成same-I实验能隙。额外planar根的fixedω阈值1.282267MeV与fixedI阈值17.959923ℏ也是不同根库存对象，都不是新的实验手征起始。

### 零二阶曲率不等连续简并

在ωc取ω*=(a,0,b)、a=ss/(𝒥m−𝒥s)、b=sl/(𝒥m−𝒥l)。沿精确同球面路径ω(t)=√(1−t²/ωc²)ω*+t e_m，令C=(𝒥m−𝒥s)a²+(𝒥m−𝒥l)b²>0，则

$$\Delta R=\tfrac12 C[1-\sqrt{1-t^2/\omega_c^2}]^2
=\frac{C}{8\omega_c^4}t^4+O(t^6).$$

所以阈点虽有零切向二阶曲率，仍是孤立最低点并有正quartic代价；严格阈上才有两个分离最低点。源参数系数约6.385077ℏ⁴/MeV³只属于该t单位，不是动力学频率或实验误差。若另外改变模型为𝒥s=𝒥m且ss=0，则确可有整circle简并；ss单独为0即使形式阈值有限，解也落m-l平面，不能叫三轴chirality。退化与零gyro极限须声明改了哪个前提。

独占脚本`outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/workers/gyro-stability-010/gyro_global_contract.py`作逐极点区间的planar根库存、全局差式及显式变模型极限，72控制通过且root重跑exit0。它服务这个代数增量，不重放HF/RPA、不增加独立实验；本固定参数路线已局部饱和，下一信息来自实际动力学或遗漏坐标，而不是继续加采样点。

## 一维测度的可复现练习

[[chen-2013-collective-hamiltonian-chiral-modes]] CH13-D24-002/004/010提供算符/测度前提。以下额外限定闭盒[−a,a]上B为实C²函数且0<bmin≤B≤bmax<∞，V为实连续函数，取Dirichlet自伴域。这是regular一维数学组件，不是CH13实际网格、135Nd/133Ce模型或实验重分析，新增needs_review:true。

取x(φ)=∫₀^φ√(B/B0)ds，B0>0为参考质量。链式法则使H变为−ℏ²/(2B0)∂x²+V(φ(x))，√B dφ=√B0 dx。若以dx归一，幅Ψ(x)=B0^1/4ψ(φ(x))；质量的影响仍在x盒长度和变换后的势，不能固定新盒/新势后任意改B0。

若保留原φ而改用flat dφ测度，则u=B^1/4ψ，并且

$$H_u=-\frac{\hbar^2}{2}\partial_\varphi(B^{-1}\partial_\varphi)+V+Q_B,
\qquad Q_B=\frac{\hbar^2}{2}\left[\frac{B''}{4B^2}-\frac{7(B')^2}{16B^3}\right].$$

这里Q_B是共轭变换项，不是添加新物理。分部积分的动能二次型为(ℏ²/2)∫B^−1/2 abs[(B^−1/4u)′]²dφ≥0，即使Q_B局部负也不矛盾。三种密度合同是

$$dP=\sqrt B|\psi|^2d\varphi=|u|^2d\varphi=|\Psi|^2dx.$$

φ反射要同时保持B、V和域；V偶单独不够。在regular偶B/V盒中，本征值simple、偶/奇态的奇量期望为0，最低gap严格正；不扩展成禁止真实核其它精确简并。两态|L/R⟩=(|0⟩±|1⟩)/√2在有限Δ下以πℏ/Δ互换、2πℏ/Δ返回，为闭系统相干演化，未含环境退相干或核寿命时钟。

### Synthetic三路谱与误差对象

声明无量纲ℏ=B0=1、a=π/2，选择B=1+.7φ²、V=18(φ²−.85²)²；没有从论文图反推输入。路线分别为均匀φ上的加权generalized FV、用解析x(φ)独立反解的均匀x常质量谱、同φ上的flat-u散度算符加解析Q_B。后两路不复用FV矩阵/本征态来伪装独立求解。V=0的常质量/变质量解析盒极限也已核。

|前4态误差对象（均无量纲）|1023内点|4095内点|
|---|---:|---:|
|FV与独立x-grid路间差|4.431e−6|2.770e−7|
|flat-u与x-grid路间差|6.579e−6|4.112e−7|
|FV与16383点x参考差|1.467e−4|8.609e−6|
|x-grid与16383点x参考差|1.511e−4|8.886e−6|

三路以h²收敛，但路间差远小于共同截断差；不能据4.1e−7一致性认证4.1e−7精度。x参考8191→16383前4态最大变化1.776e−6，gap变化1.816e−8；16383点gap≈.195626391只是数值参考，不是严格界/物理CI。合成两态packet的Pleft约.995355→.004645→.995355，时间无量纲，不据此产生实际核隧穿时间。

同一个合成基态，正确测度给⟨φ²⟩≈.626253，错用flat abs(ψ)²重归一给.598114，约差4.49%。改成正但不偶的B=1+.3φ、仍用同一偶V，ground⟨sgnφ⟩≈+.941，作为“V偶就足够”的负控制；不由此否定CH13的偶B。

### 端点与本组件的停止边界

若端点B发散，x长度由∫√B决定，可以有限或无限；例如距端点s的B∼s^−p在p<2时有限、p≥2时无限。large B本身不普适推出有限盒/硬墙。singular情况下ψ→0也不自动给u普通Dirichlet，必须传递自伴域、V和整个端点条件。CH13从large B选wall仍是作者明确近似，本组件没有证明其唯一性。

可复现脚本为`outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/workers/chiral-metric-011/metric_audit.py`，结果results.json；root读推导/脚本并重跑exit0。连续几何、离散、求解误差和物理输入分层后，本组件已足够回答测度/局域packet问题；不继续用synthetic网格细化填补真实mass/EM缺口。

## 二维方法补到哪一步

[[chen-2016-two-dimensional-collective-chiral-wobbling]] CH16-D24-001–011把θ/φ都作为取向动态变量并保Bθφ交叉质量；γ仍固定，不能把orientation softness改称实核γ-softness。实际v2原30页/12图展示的高频再劈裂与PRM比较有信息增量，低spin失败及新边界也同时保留。它继续推进CH13而非增加一次135Nd实验。

|需区分的合同|CH13|CH16实际改变与剩余边界|
|---|---|---|
|动态空间|φ；每φ最小化θ|保完整θ/φ面，新增θ激发与交叉动能；仍非β/γ或多配置动力学|
|边界|±π/2 Dirichlet box|两坐标周期π；连文内1D对照也改periodic，不能把跨文改进只归给θ|
|质量|小激发推导/Ω处方|Ω0 cranking忽略residual interaction，低频过小；常1.10MeV Ω改善对照但尚非微观解|
|概率|√B dφ，图7字面abs(ψ)²|√detB dθdφ，ρ式已含权；Eq31边际式字面不含权，producer未核前保量身份|
|高频|PRM再劈裂未被1D描述|原Fig8的gap确重开；作者晚期解释为i轴LW，不能只按gap认成同一个second-chiral mode|
|I与E|固定ω，非good-I|按概率平均JTAC、Icoll=Jcoll−½，再用E′+ωJ；仍不是严格I投影|
|benchmark|示意PRM对照有失败|Figs9/10高spin四signature branches及能量有一定符合，低spin明显失败；Fig11改mass改善为假定处方敏感性|

CH16的工作sector按基/后文为Pφ左右反射与Pθ的θ反射；chiral pairs在同Pθ、不同Pφ，signature pairs反之。源PDF7的respectively语句局部反序需保留，但不据此推翻一致的工作基。集体反射标签也不变成真实核antiunitary操作的相位不变±本征值；更不替代实验带族/全links的追踪。

本轮学习决定是`supports`示意方法层的部分闭合，同时`limits`维数增加就保证全域/全模式/全观测正确的推断。最高信息下一路线是该模型实际EM定义：能量/概率平均能否提供跨不同I/sector的相干矩阵元，须读后续原方法，不能从小gap或相似密度代填135Nd双partner g和branch/normalizer。

### 二维质量的rank与极点域

[[chen-2016-two-dimensional-collective-chiral-wobbling]] CH16-D24-003/012支持以下输入前提，推导本身属于任务。令Aat=⟨m|(∂aω)·j|i⟩、Δt=εm−εi；仅在所有相关Δt>0且有限、取源所用实对称质量的条件下，实坐标速度z给

$$z^TBz=2\sum_t\frac{|z_\theta A_{\theta t}+z_\varphi A_{\varphi t}|^2}{\Delta_t^3}\ge0.$$

正半定不等严格正定；后者需要两个响应方向rank2。任意blocked激发占据或能差变号时，不能直接沿用此证明。有限Ω处方也可在非零有限分母和正Δ下写成带2Δ权的Gram，个别分母为负本身不证明tensor不定；分母精确为0需另处置。

Eq19中φ响应含sinθ；若active gaps/矩阵元在θ=0/π有限，则Bφφ=Bθφ=0、w=0。若gap同时零则不能套有限极限或算0/0。故整个闭矩形上的uniform detB>0并不由公式自动保证。源讨论的小分母大mass ridges与这个坐标pole是两种边界。

更具体地，假设极点附近有regular局部展开Bθθ≈a、Bθφ≈θb、Bφφ≈θ²c，a>0、d=ac−b²>0，则w≈θ²d。源θ-even Fourier基的单个非零首项给ψ≈θ^−1/2 f(φ)，其√w加权范数可有限；动能form的leading integrand却为

$$\frac{\theta^{-2}}{\sqrt d}\left[\frac c4|f|^2+b\operatorname{Re}(f^*f')+a|f'|^2\right]
=\frac{\theta^{-2}}{\sqrt d}\left[a\left|f'+\frac b{2a}f\right|^2+\frac d{4a}|f|^2\right].$$

在这些前提下，非零f给正的∫θ^−2发散；L²归一不认证finite kinetic form。特殊线性组合可取消leading f，适当regular基、cutoff/端点flux或其它implemented prescription也可能改变域；actualproducer未得，本推导不判作者的实际谱错误。θ-odd基多一个θ，其该局部leadingform可有限，也不代替完整域检查。

下一高信息输入是actualmetric/基组合/端点处理和截断收敛，不能靠w^−1/4归一相消或平滑图形关闭。该P1限制已隔离在明确条件的理论域，不给实验判据、HF不稳定认证或133Ce程序参数替代。独立审查副本在本run workers/chiral-2d-review-013，root已核原Eq19、质量/Pauli式及完整square。

## EM PartII：带内率平均不补完整相干网络

[[wu-2018-two-dimensional-collective-electromagnetic-transitions]] WU18-D24-001–010填了CH16后续的部分EM输出：同一单j示意体系，把单个集体态的ρ乘局部TAC B值再积分。1D测度√B dφ、2D测度√w dθdφ，计算的是带内M1/ΔI1 E2/ΔI2 E2，明确不含新跨带输出。

$$\overline B_i[X]=\int d\tau\,|\Psi_i(q)|^2 B_\mathrm{TAC}[X](q).$$

它包含density/节点导致的不同平均值，也修正stationary单点取向的不足；但式中没有Ψf、Ii/If的相干态对或off-diagonal核。因此四sector的带内曲线相近，不等于已求得sector间选择规则矩阵、signed RME或M1/E2相对phase；不能用同一组曲线给signed δ或完整跨带衰变预算。原文背景列wobbling/chiral的interband E2诊断，并不表示本篇新计算检验了它们。

局部率角是总J方向θJ/φJ；集体坐标θ/φ则是推转ω方向，只有stationary时相同。离极小点采样不能静默将两组角全域合并。源φeff=E abs(φ)、θeff=E[π/2−abs(π/2−θ)]是折叠坐标矩，不是signed手性、RMS或独立实测几何。类似折叠均值不能固定相干EM网络。

|实际方法支持|同时保留的边界|
|---|---|
|Figs1/3的带内E2尺度/平滑趋势与PRM有一定一致|M1与ΔI1 E2的强odd-even staggering未恢复；作者明确归因非good-I，不能说完整定量符合|
|CH高spin平均M1小而非零，可区别stationary TAC单点零|是源参数取向涨落结果，不是本核新测量/硬spin阈值；零率还需磁矩横向分量条件|
|相同参数进行1D/2D/TAC/PRM比较|gp−gR=1、gn−gR=−1、Q0=1eb为共同示意输入，不给135Nd g或Q|
|继承CH16的periodic计算谱系|本篇未明选PartI Ω0还是1.10MeV质量版本，不先称低spin谱失败已修复|

本轮`supports`的是概率平均带内率的有界模型用途，`limits`有集体波函数/有B曲线就等于完整量子EM算符的推断。这与MU07的harmonic共同TAC基线、Qi09完整PRM及本页真实实验B账本各自不同；不改变MU07实验正支持，也不替换其仍缺的normalizer/跨带组件/g。

### Author source package与actual模型producer

[[chen-2016-two-dimensional-collective-chiral-wobbling]] CH16-D24-013与[[wu-2018-two-dimensional-collective-electromagnetic-transitions]] WU18-D24-011缩小了实际公开输入边界：PartII完整官方包为文章TeX+四图，CH16只得transport-incomplete包但主TeX完整。两个TeX都不足以建立actual数值程序，CH16尾部未得也不能宣称全包无code。

尚缺actualV/Bgrid、positive-gap/occupation跟踪、单位与Ω版本、pole/ridge处理、basis cutoff/flux/收敛和output-to-figure job。现有源可支撑条件独立推导，不能给L4 actualproducer复现盖章。此有界检索三路线已结束，不重复失效端点、不从图/公式重造actualjob或运行114隔离producer；下一可用主线转good-I投影原模型的空间和EM合同。

## good-I投影：态空间、EM核和取向图分别验

[[chen-2017-128cs-angular-momentum-projection-chirality]] CH17-D24-001–008是本轮128Cs方法对照；它复用[[grodner-2006-128cs-chiral-doublet-lifetimes]]实验，不是135Nd或128Cs新采集。其good-I/N/Z态与CH的Jcoll−½映射不同，但也没有自动纳入所有shape/组态竞争。

|对象|原文实际合同|剩余边界|
|---|---|---|
|投影态|3D AMP+PNP，有限四个time-conjugate阻塞κ/K混合|固定shape/阻塞轨道，不是多shape/任意qp GCM|
|norm|Hill–Wheeler非正交基、g=N^1/2 f|raw abs(f)²非概率；actualnormcutoff/矩阵未得|
|EM|Fig2实际带内E2/M1和B→A跨M1，有交错|完整EM核/有效电荷/g/phase未打印，跨E2/signedδ仍缺；高spin E2有偏差|
|K图|metric修正后的±K模方折叠、sumκ|不能倒推内部phase；K0 producer convention unknown|
|azimuthal图|同κ的K振幅先相干，再sumκ/积分ψ′|保K干涉，有限图仍不提供完整跨态核；测度是Euler/Haar，不是质量detB|

投影态用于张量时，RME应为Σ f_f* Tfi f_i，振幅求和后平方；这是据态定义作的任务推导，不能伪称从12页正文恢复了作者全部EM实现。整体state phase任意并非可观测，真正要绑定的是内部相干与E/M算符的一致约定。该区分使WU18的局部率平均与投影态跨M1输出可以各自有用途，也各自留下明确readiness缺口。

几何角也不同：此文φ从i轴量，s-l平面为φ90°；P标准全域的条件范数带sinθ，发表图只显示θ0–90/φ0–180，不按flat图像面积或任意倍数恢复概率。原作者I11/I14/I18的有限静态窗口及高spin E2偏离仍在；good-I不提供高spin必更静态的普适结论。


## 特殊选择规则不能直接变成135Nd的一般必要条件

[[hamamoto-2011-selection-rule-chiral-geometry]] HM11-D24-001–006原件全12physical页回核：odd-odd同j质子粒子/中子空穴γ90的A对称可在非手征几何区存在；core E2非零要求异A，但异A不保证非零。原page7明确把oddA Nd中aligned S-band角动量替代jp的规则列为尚待推导，故不能直接给本核三qp A/B赋其A序列或把某线不合odd-odd模式当普适证伪。

M1示例gR=.5与实际Fig2caption55/130是两个输入。源系数在指定single-j投影后的antisym/sym平方从78000.51变80.03只说明算符接近exchange-odd的条件性，均非实际跃迁B比/压制下界。旧HM11-D19-1的充要/1000/134Pr实测γ与普适必要条件认证已同ID撤回、原行留审计；128Cs原支持和135Nd MU07独立实验支持保留。下一实际比较仍需本核波函数、相干EM与逐线binding，不用更多系数小数替代。


## 低1qp区域系统学不替代高spin手征伙伴

[[meyer-ter-vehn-1975-odd-a-unique-parity-comparison]] MTVII75-D24-001–015直接比较历史135/137Nd、133Ce与邻核，支持在指定空间用E/EM网络联合限制三轴模型；但它是约2Δ以下unique-parity1qp应用，没有给本页MU07三qp伙伴的g/完整相干EM或实际branch。193Hg两γ例可有相似yrast序，137Nd额外态的能量+branch又不能同时配上h11/2，显示谱序与配置指认须有companion。

其γ软度讨论保complete-soft与rigid两个极限皆未达到、fitγ并非波函数宽度，以及尚未完成odd+γdynamic模型。该原件让γsoftness替代路线的输入合同更具体，不表示本核该路线已拟合、已胜出或已排除；本文不新增独立135Nd测量。


## 135Nd早期低1qp参考的直接观测范围

[[gizon-1974-deformed-states-cerium-neodymium]] GZ74-D24-001–007/013–016原1974实验在9/2−参考上给198.5/560.7/792.9/1270.0/1520.5主负序及共门/混合线，且明确没有足够确定的sidebands。它是低νh11/2参考，不是MU07三qp高spinA/B，也不能把现代TiP标签倒写回原论文。1975模型复用该组Ce/Nd数据，不新增独立手征EM支持。

源中I55、AD平均α2、近似δ和prolate模型解释分层；未观测能差线不造强度、原表crossover560.3/正文560.5/图560.7保版本精度。用实际原谱限制configuration映射比只看同核同spin更有信息，但它不关闭本页partnerg/fullnormalizer/Cov或actual3qp输出缺口。


## 134Pr原件对counter-model比较的控制

[[tonev-2007-134pr-dynamic-chirality]] TO07-D24-009/010在另一核提供具体方法控制：能谱计算与几何演示用不同惯量合同，当前EM参与参数/模型family赋名，且作者指出Band1在I>16可能超出原2qp空间。因此比较crossing/configuration/γ-softness/mixing时，先声明spin有效域及定标/选态，不能把失配全归一种机制或将选态所用EM重复当holdout。这不是135Nd新数据，不移植134Pr参数、不削弱MU07已有绝对EM支持；本页四替代路线仍需135Nd自身未定标预测。新增综合needs_review:true。
