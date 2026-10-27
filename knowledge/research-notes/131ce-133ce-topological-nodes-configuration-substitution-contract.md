---
type: research-note
title: "131Ce与133Ce拓扑节点对照、组态替代可证伪性合同与符号矩阵元红线"
aliases: [131Ce 133Ce topological nodes and configuration substitution, 131-133Ce节点与组态替代合同]
created: 2026-10-27
updated: 2026-10-27
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [wakudyanaye-2022-triaxiality-rotational-bands-133ce, alwaleedi-2013-band-structures-131ce, sensharma-2020-longitudinal-wobbling-187au, guo-2022-low-spin-wobbling-187au]
created_from: Day25 checkpoint005 source audit
confidentiality: public
tags: [133ce, 131ce, spectroscopy, topological-nodes, configuration-substitution, 3qp, signed-rme, analysis-blueprint]
---

# 131Ce/133Ce节点、组态替代与相位一致性

## Research Trigger

保留可迁移的节点与全连接分析合同，服务[[133ce-thesis-analysis-blueprint]]。checkpoint005核AW13 PDF86、WK22 PDF69/71及Au两原件；新增needs_review:true。旧3Δ激发下限、832keV排除3qp、Au争议源于RME符号错误、确定轨道下移机制撤回；旧稿有入口快照。

## Grounded Evidence

[[alwaleedi-2013-band-structures-131ce]] AW13-7、PDF86/printed82：Band3为1/2+、61.8keV，作者提出possible νs1/2[400]1/2+。[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-34/45：133Ce Band3为1/2+基态。原件对照不唯一测定轨道重排机制，不转移能量误差、参数或寿命。

WK22 PDF69 Table5.3、PDF71 Table5.4的节点账本：

|母态Ex/Jπ|归属|所列Eγ及末态|
|---|---|---|
|1445.8/13/2+|Band3|244.4→1201.4/11/2+；629.9→815.9/9/2+；412.4→Band2 1033.4/11/2+；767.7→Band2 678.1/9/2+|
|1459.9/13/2+|Band2|426.4→1033.4/11/2+（中心闭合残差+.1keV）；781.8→678.1/9/2+|
|2733.4/19/2+|原表一行|881.2；若末态1852.7，则Ei−Ef−Eγ=−.5keV|
|2739.5/19/2+|原表另一行|886.8；同末态时中心闭合0|

412.4与767.7同出1445.8，不造1047.5节点。14.1keV只是中心能差，不独立给混合强度/ωc。两个19/2+原表行分别保存，前行闭合待核；不凭同spin合并，也不据两行自动认证两个已独立确立的物理母态。

AW13 Fig5.2 caption Band4/正文Band1冲突保留；Band5高spin e⊗AEFG既有人审不改。

## Provisional Reasoning

|替代类型|实际工作|当前证据边界|
|---|---|---|
|纯relabel|H/态/算符均不变|没有新预测|
|同H本征态mapping|同空间/算符下匹配能量、Jπ和全部已观测links|候选，不把改名当拟合|
|引3qp空间|新增blocking、配对、残余力、转动能与EM核并留holdout|832keV可行性unknown|

实测N、Ex、响应保持；不裁剪冲突分支。未见线需真实灵敏度/上限才能反证。引3qp不是原1qp空间的基变换。

固定BCS参考下1qp/3qp能量和约Δ/3Δ，但奇A基态已含1qp，因此3Δ不是相对该核基态的Ex下限。连2Δ差也受轨道、blocking、形变、残余力与转动能重排影响；不能据经验Δ排除832.0keV。来源边界：WK22-33/37、PDF99/104/107，当前未建立该3qp计算。

## 4. 相干相位与基底规范

$$\langle f\Vert O\Vert i\rangle
=\sum_{\alpha\beta}C^*_{f\alpha}C_{i\beta}
 \langle\alpha\Vert O\Vert\beta\rangle.$$

只给|C|²和前三分量不能恢复相干和。但同步变换基矢相位、系数与算符不改变观测。态整体rephase使E2/M1 RME共同乘e^(i(φi−φf))，B和同跃迁δ均不变；真正物理相对混合/算符改变才可改干涉。这是WK22 PDF47–48 Eqs3.17–3.24前提下的数学说明，非作者完整波函数恢复。

actual gK、δ符号与绝对B缺输入时unknown；pure-j/渐近gK/good-K带内比不能代实际跨带预测。

## 5. Au身份不能颠倒

[[sensharma-2020-longitudinal-wobbling-187au]] PDF3 Fig2/PDF4：原Band2=wobbling、Band3=SP。[[guo-2022-low-spin-wobbling-187au]] PDF2–4用Rac/P、旧ICC及不同QTR输入质疑Band2大|δ|。无原件证明旧计算有RME符号错误或Band2/3选择定则翻转，不将此臆断写成争议根源。

## Learning Decision

revises伪3qp下限与相位归因；supports逐节点、完整links、相干核和相位规范检验。

## Assumptions

节点账本按所标Table行保存；能差只是中心算术，Jπ和branch类型继承原源。BCS能量和的说明限固定参考，不赋实际3qp阈值。相干和采用统一基底/算符相位。

## Competing Explanations

同H的不同本征态映射、增加3qp空间、不同形变/混合属于不同模型合同。未获得完整输入前不能给候选可信度排序或用改名补足预报。

## Transfer Conditions

只迁移逐节点/逐线/全links核对流程。跨核Band号、零点、Harris、寿命和渐近gK均不自动迁移；原AW13 Band5审核范围保持。

## Failure Conditions

将2733.4行残差静默改平、以3Δ排除832keV、把基底rephase写成观测改变，均使本推断失效。缺实际signed核时δ符号unknown。

## Falsification or Reverse Tests

将同一初末态的E2/M1 RME同时乘态phase，检查B和δ不变；只给|C|²无法重建相干和。候选mapping若无法同时对应能量/Jπ/已观测links则该映射失败，非全模式终判。

## Open Questions

2733.4/881.2行的实际placement、目标3qp空间、signed wavefunctions/算符输出和响应仍缺；保持unknown，不逆造节点。

## Human Review

本页未发生用户claim裁决，review_status保持unreviewed；不迁移其它source或Band5的人审到本推理。

## Promotion or Rejection History

2026-10-27 checkpoint005撤回旧强认证，以原件和声明条件的前向控制替代；reasoning_status为provisional。旧稿在Git和入口快照保留，未将self-audit写成human-reviewed。
