---
type: research-note
title: "199Tl三线AD：同母态、正布居与取向条件"
aliases: [D66 three AD feasibility, Tl199 sameparent reference model]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
question: "实际三条AD在共同上态约束下，哪些结论依赖额外的取向输入？"
evidence_sources: [diamond-1966-nuclear-alignment-heavy-ion-reactions]
created_from: daily-learning-phys-model
promotion_target:
reproducibility_entry: system/scripts/day16_diamond1966_three_ad_feasibility.py
nuclei: [199Tl]
tags: [angular-distribution, sameparent-reference, identifiability, conditional-model]
---

# 实际AD支持条件解，不把中央数和误差域混为一谈

## Research Trigger

[[diamond-1966-nuclear-alignment-heavy-ion-reactions]] D66-D16-2给出实际197Au(4He,2n)199Tl三线AD及作者“19→5→3”的推断。本文检查共同母态与取向前提，不重新指定199Tl自旋或复现作者的完整处理。

## Grounded Evidence

331和701keV来自同一个上态，370keV来自中间态，底态是749keV、9/2−。原Fig2报告：

| γ/keV | A2 | A4 |
| --- | --- | --- |
|331 |−.58±.03 |−.02±.03 |
|370 |−.36±.02 |−.03±.02 |
|701 |+.26±.04 |−.03±.04 |

原文称AD把19种序列降至5种，再用expected alignment得到3种probable序列；图中后三者为上/中态(13/2,11/2)、(9/2,11/2)、(9/2,7/2)。那5个中间候选的完整列表与原producer未取得，不替作者补表。ICC与其它资料仍是作者所需companion。

## Assumptions

本run采用明确point、4π归一的Legendre模型。上/中态候选各为5/2至13/2，三条spin差≤2，恰有19对。|ΔJ|=2只取L2，其余允许real native L1/L2混合；全取负宇称可给一组合法的AD实现，但不是实测宇称指定。

331与701共享一个非负对称P(m)；370的total P(m)另作未知，不能因看见331 feeding就假设中态只由这条线布居。响应、方向门、feeding强度与联合Cov未恢复。每个quoted±数只作为所选边际box半宽，不把它当联合置信域或原实验likelihood。

对照两域：任意非负对称q；额外要求上态与中态各自`u2≤0`。后者仍比固定Gaussian弱，是模型前提。

## Provisional Reasoning

### 找到的正布居解是存在证据

固定arctanδ网格步长5°，每组振幅下用LP最大化所有|m|pair概率的共同下界。先找独立370域，再查共享上态的331/701。5845次LP中找到：

| 取向域 | 有严格正q的网格序列数 | 正确含义 |
| --- | --- | --- |
|free positive q |8 |至少有这8个条件解，非完整允许数 |
|额外u2≤0 |3 |找到作者列出的3个probable序列，未证明只有3个 |

有限网格零命中不能排连续δ或孤立根。这不是复现原“19→5”，也不能把8/3当实验后验、候选概率或新指定。

例如(上态13/2、中态11/2)有如下低m条件解：native β331=−20°、701为pureL2、β370=−15°。输出(331 A2,A4)=(-.55,+.01)，701=(+.259173,−.032057)，370=(-.34,−.01)，均在所设box内。它们在部分box边界上；“strict”仅指所有q严格为正。

为使witness不只保存在outputs，上态按|m|=6.5,5.5,…,.5的pair概率为：

`qtop=(e,e,e,e,.483316664716,.376639232863,e)`，`e=.0280088204841`。

中态按|m|=5.5,4.5,…,.5为：

`qmid=(f,f,f,.690083622463,.160767245802,f)`，`f=.0372872829338`。

每一±m各取pair的一半。其u2上/中态约−.181421/−.133441；这是数学布居，不是测得的PM或D66作者δ。

free域还找到例如(7/2,9/2)的正q条件解，所给中态u2≈+.326086，说明该witness并不满足低m前提。不能由这一点断言该序列在整个lowm连续域无解，也不能把其高m布居说成实际反应产物。

### 中央A4的必要关系不是带误差数据的排除

对同一上态，L1纯项和L1/L2干涉都不含rank4；所以A4由高多极photon份额`f=δ²/(1+δ²)`乘共同rank4矩给出。独立6j与photon核核对，三组作者probable spins的pureE2系数比A4(331)/A4(701)依次为：

`−8/3、−16/39、−8/7`。

核与这些精确比的最大差小于7.6×10^-15。若两条A4中央值均非零且同为负，这些负比例不可能由非负f满足；因而这三组在**精确中央数**问题中不闭合。但两个A4的quoted-margin区间都含0，前面的共享上态witness也确实在区间内。不能把中央数的必要失配改写成实验自旋被排除。

若将quoted误差条件性地当作边际标准差，写必要残差`r=A4(331)+k A4(701)`，k≥0。其中央绝对值为`.02+.03k`；允许任意PSD相关性时，标准差的上界为`.03+.04k`。故

\[
\frac{2}{3}\le\frac{.02+.03k}{.03+.04k}<\frac34.
\]

这一比使用“最大允许标准差”，不是实际z值；它只说明该数对不给一个对所有未知Cov都成立的一倍标准差排除。实际联合统计仍需原谱/拟合Cov。

## Competing Explanations

源作者的expected alignment、几何与拟合流程可能比本模型的任意q更强。任意非负q可容纳与入口反应机制不相称的布居；lowm又只是二阶矩条件，不等于Gaussian。三种域不能混用，也不由当前数学witness对源作者的5个或3个候选投票。

## Falsification or Reverse Tests

后续若取得真实response、trigger/feeding及联合Σ，应按同一观测对象重建域；若它排除现有freeq witness，更新条件解，不把旧存在证据删除为“从未存在”。若要证明完整spin允许数，需连续参数的根/可行域证书，当前网格不能承担该结论。

## Agent Self-audit Triage

P0：未识别未隔离的原件身份、权限或路径问题。D66输入和旧helpers哈希保持。

P1：所有新增native振幅、PM、网格计数和误差域均为Codex条件分析；未恢复原角响应、全部5候选、δphase或联合Cov，不赋予实验Jπ/δ/CI。

## Reproducibility

[网格/LP程序](../../system/scripts/day16_diamond1966_three_ad_feasibility.py)actualexit0；[独立rank4/误差/全部witness重构](../../system/scripts/day16_diamond1966_rank4_certificate.py)actualexit0。11个记录（8free与3lowm）逐个从kernel重构，observable差0、box残差约1.6×10^-15。合同和post-grid设计时序均保留，不冒称盲测；没有生成toy counts。

## Transfer Conditions

只迁移“同母态共享密度、中央值与误差域分开、存在与排除分开”的方法。换spin、门、响应、rank或δ约定均需重建，不能拿这些native数填其它核素。

## Failure Conditions

源系数并非这里的响应层、两线非相同条件布居、实际角门改变density、原不确定度不支持所设box，或任一正性/归一/核验失败时，模型不用于实验赋值。

## Open Questions

作者AD-only五个候选的具体名单和complete-alignment约束怎样实现？实际三线共享何种trigger、角响应和Cov？有哪些匹配ICC/参考线能区分probable序列？

## Human Review

尚无本note的用户审核；旧D66人审只属于其原前缀，新分析保持unreviewed。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
| --- | --- | --- | --- | --- | --- |
|2026-10-19 |created |none |provisional |实际AD、共同母态与正q存在证据；实际response/Σ仍缺 |不晋升实验结论 |
