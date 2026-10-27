---
type: research-note
title: "A≈130区核手征反例与三轴形状共存系统学研究：从近简并破缺到电磁跃迁伴随量判据"
aliases: [A130手征反例与形状共存系统学, A130 chirality counterevidence and shape coexistence systematics]
created: 2026-10-27
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [petrache-2006-near-degenerate-chiral-misinterpretation, grodner-2006-128cs-chiral-doublet-lifetimes, tonev-2006-134pr-lifetime-chiral, tonev-2007-134pr-dynamic-chirality, lv-2019-chirality-135nd-reexamined, petrache-2018-chiral-bands-even-even-136nd, mukhopadhyay-2007-135nd-chiral-vibration-static]
created_from: Day25 task continuation
promotion_target: chirality-shape-coexistence-companion-matrix
tags: [a130, chirality, shape-coexistence, counterexamples, near-degeneracy, companion-observables, transition-strengths]
---

# A≈130区核手征反例与三轴形状共存系统学研究

## Research Trigger

Day25主线要求解释近简并的非充分性，并分开手征双重带与形状共存。近简并不直接测角动量几何或形状；有限自旋手征振动也不必满足静态极限的小劈裂。旧稿中的“普遍必要”“全核无寿命”“六级必需链”和模式排他认证在checkpoint009撤回，采用下列逐family证据。正式比较表见[[chirality-shape-coexistence-companion-matrix]]。

## Grounded Evidence

|对象|直接观测或派生量|作者/模型与解释边界|
|---|---|---|
|134Pr旧Band1/2|[[tonev-2007-134pr-dynamic-chirality]] TO07-D24-002/008保存逐点带内B(E2)与寿命；同spin中央强度比随spin变化，不能用固定4倍替代全段|[[petrache-2006-near-degenerate-chiral-misinterpretation]] PE06-D25-A005-01–03的简化两带解混合给Q0比约2.0(4)、短段\|V\|约14–17keV。不是直接β测量；Tonev两文共享实验，分支资料谱系另核，不能重复计票|
|132La对照|[[grodner-2006-128cs-chiral-doublet-lifetimes]] GR06-D18-4报告侧带B(E2)约低20倍、M1约低2–5倍|作者认为不符合内禀手征对称要求；不据此排除所有手征动力学，不把sqrt(20)自动称为实测内禀Qt比，也未证明唯一“杂质态”|
|135Nd负D5/D6|[[mukhopadhyay-2007-135nd-chiral-vibration-static]] TableI给两带寿命和派生绝对EM，构成较强支持|TAC/RPA解释振动与趋近静态的有限spin演化；τ、branch与B同链相关，不是三项独立实验证据|
|135Nd正D3/D4|[[lv-2019-chirality-135nd-reexamined]] LV19-D25-002的新谱学/角响应/偏振与一个D3比值点|本篇未给该pair成对absoluteEM或新τ；不得从负pair借证，也不声称全领域正pair均无寿命|
|136Nd逐pair|[[petrache-2018-chiral-bands-even-even-136nd]] PE18-D25-001/003：D5/D5-chiral双方有相近相对比；四弱伙伴缺自己的比|D3模型非共面解不借给D5；[[mukhopadhyay-2008-136nd-transition-rates]] TableII旧Band1/2有绝对EM，低spin对应后来D4/D3主带，不是各自新伙伴，不能说全核无寿命|
|133Ce|[[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]]给候选对的谱学及相对比，未测目标寿命|RMF/TPRM支持MχD/三轴形状共存的作者解释有模型中介；[[ding-2021-131ba-133ce-signature-splitting]]对正Bands2–3给签名伙伴竞争解释；[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]低spin Band4的TiP不等于原高spin候选对整体重指认|

## Provisional Reasoning

### 1. 能谱与结构机制

两能级条件模型有 ΔEobs=sqrt[(E1−E2)²+4|V|²]。固定未扰动能差时排斥增大gap；相互靠近的未扰动轨迹与小V可产生窄gap。一个实测gap不能独立求V与混合角，更不能在手征、组态交叉和形状共存之间唯一选解。

理想静态手征近似可预期伙伴的电磁相似性，但相等强度、交错或强带间连接均须按具体配置和有限spin预报检验，不能提升为所有手征模式的普遍充要条件。不同形状也可在特定通道给相近B值；同一Qt不足以分别确定β、γ及其涨落。

### 2. 两带前向幅度与正交不变量

声明封闭的实两态子空间，初末态各以正交矩阵Ri、Rf混合，Mfi=Rfᵀ Qfi Ri。若再取实对称 $Q=\begin{pmatrix}q_1&q_{12}\\q_{12}&q_2\end{pmatrix}$，则

$$
\|M\|_F^2=\|Q\|_F^2=q_1^2+q_2^2+2q_{12}^2,
\qquad |\det M|=|q_1q_2-q_{12}^2|,
\qquad \sigma_k(M)=\sigma_k(Q).
$$

这是声明模型的代数，不是原实验已重构的signed矩阵元。B到振幅还需相位、初始spin归一和完整通道。特定ansatz Q=q0I给退化奇异值；非退化可否定该ansatz或封闭子空间假设，不能直接否定所有同形状手征波函数，也不能唯一证明形状共存。

PE06固定混合角下，允许q12并调整q2可使原四个分支目标保持相容；本run `forward-checks-005.py/json`只是条件敏感性，不是联合likelihood/置信区间。相同比值隐藏绝对尺度，绝对EM、其它结构量及可失败预报可帮助进一步区分。

### 3. 最小伴随量组合与缺项降级

本页“最小”针对已声明竞争问题选取，采用四步设计，和课程L0–L4分级无关：

1. **身份与响应**：逐母末态/Jπ、带family、branchrole、效率/门/混合比/ICC。身份未闭合时暂停matched比较；缺某项角观测不自动使所有spin未知，须看其它独立约束。
2. **匹配绝对尺度**：目标母态τ加完整branch与混合成分是一条重要路线；也可按其它独立绝对EM/结构量的实际覆盖评估。无clock且无其它尺度时只得relativeEM，不借邻态/邻核时钟。
3. **固定模型与可失败预报**：预先声明空间、算符、参数和允许nuisance；检验具体强度向量、links与spin演化，而非只换配置标签。
4. **分离预报的独立holdout**：按可行性选g、Qs、E0、转换、转移反应或其它量。缺该量时保留等效解释；完整组合也不保证唯一模式。

[[heyde-wood-2011-shape-coexistence-review]] HW11-D25P-001/002的E0混合关系涉及电荷分布与态混合；非零E0不唯一分解形状、混合角及其它组态效应，零E0也不普遍排除共存。g因子不直接测三维角动量几何。它们不是每核都必须具备的终判。

## Assumptions

条件代数采用封闭实二维子空间、正交混合及指定Q核；一般初末态矩阵不必实对称。寿命、feeding、阻停及Cov仍按原实验假设和误差处理保存，不能预设已经全部独立控制。

## Competing Explanations

配置交叉/带混合、形状涨落、不同结构极小和手征振动可分别重现部分谱学特征。134Pr简化Q比或132La强度反差限制理想伙伴解释，但不独立确立唯一替代机制。

## Transfer Conditions

可迁移的是逐态身份、响应与证据分层的方法；参数、参考Harris、phase、时钟、阵列阈值和实际灵敏度须逐case核验，不将本页条件设计跨核推广为硬判据。

## Failure Conditions

只看近简并、相同比值或PES极小作模式认证；将观测/派生B/模型几何重复计为独立证据；将未见线补零；将不完整振幅模方当作完整signed矩阵；以缺测本身证明作者误认，均使推断失效。

## Falsification or Reverse Tests

为每个模型预先保存可测的partner-resolved强度/links/独立结构量预测及不确定度。若matched绝对EM向量与具体ideal-pair预测不相容，降低该模型的支持，继而检验允许动态/混合的替代；不用统一3–5倍或20倍阈值排除所有动力学。134Pr实验和PE06分析是近简并非充分的具体控制，非形状唯一判决。

## Open Questions

134Pr实际signed E2核与联合Cov未得；135Nd正pair、136Nd各弱伙伴的匹配绝对EM仍需逐文献/逐态补全。133Ce实际输入、目标时钟及分母身份见[[133ce-thesis-analysis-blueprint]]，不以本笔记结项。

## Human Review

本页为Codex self-audit，review_status保留unreviewed；源页既有human review与needs_review不变。

## Promotion or Rejection History

2026-10-27建立。2026-10-28 checkpoint009撤回旧普适必要/充分、唯一形状、全核无寿命和固定数值硬门；保留模型代数与逐来源支持。旧稿由Git保留，当前页采用上述证据边界。
