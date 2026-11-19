---
aliases: []
status: "ai-draft"
review_status: "unreviewed"
reasoning_status: "provisional"
evidence_sources: ["international-thesis-acquisition-20261119-source", "hungerford-1979-ill-angular-correlation-164dy"]
created_from: "User-requested literature acquisition and learning design; scope-specific provenance, not completed full-text learning"
type: research-note
title: "核结构文献深入学习：证据链与迁移框架"
created: 2026-11-19
updated: 2026-11-19
tags: [literature-learning, spectroscopy, evidence, research-method]
---

# 核结构文献深入学习：证据链与迁移框架

这是研究学习方法与问题设计，不是本批文献已经获得的科学结论。
来源身份与取得范围见 [[international-thesis-acquisition-20261119-source]]；
执行顺序保存在 `outputs/plans/20261119-archive-deep-learning.md`。

## 以什么问题组织知识

学习沿六条能力线展开：谱学量到自旋宇称/混合比的推断；寿命与绝对强度；
三轴模型及其近似；运动模式的竞争判据；形状共存与多模集体性；
异能态、壳演化和跨区方法迁移。它们是阅读问题，不是预设物理答案。

实验阅读重建“布居—装置—标定/符合—实测量—估计与误差—结构解释”；
理论阅读重建“自由度—哈密顿量—对称性/近似—参数—可观测量—比较—边界”。
作者结论必须能沿这条链回到原件，而不能只留下一个摘要句。

## 如何避免假学习

- 标准深入阅读覆盖正文主线；局部精核只记录实际章节，不升级整篇阅读深度。
- 目录用于导航，摘要用于建问题，二者均不证明关键实验或理论推理已被核验。
- 学位论文、其收录文章、SI、同实验后续论文保留依赖；版本和重复引文不算独立证据。
- 重复基础章节通过已有知识对账，独有方法、附录、数据与限制仍需读。
- 关键数字、公式条件、分支和能改变结论的图表全部回原件；不以模型相互赞同代替核查。
- 除来源页外，把确实可复用的解释和方法写回最相关知识节点，不只增加文献卡片数量。

## σ/I 与混合比专题的研究设计

比较最终估计与误差处理，而不是仅比较曲线绘图方法。分别记录固定取值、
扫描、联合估计、profile、边缘化、未报告及不适用；一种程序可能组合多个步骤。
仅有固定取向参数的曲线不能单独证明最终估计把该参数固定；没有说明参数也不能
擅自补作固定值。此框架用于检验原先判断，允许证据修正投稿措辞。

P、偏振不对称度与灵敏度，单 γ 角分布与 γγ 方向关联，以及 ADO/DCO/Rac 的实际
矩阵和门定义需要逐原件识别；不以缩写相似直接合并。暂不启动 PDM 重算。

## 研究能力的验收

能说明作者为什么这样设计，关键证据在哪；能重建核心推理和适用条件；
能识别至少实际存在的竞争解释或说明没有足够依据生成；能指出何种观测
可能区分解释；能明确新来源支持、限制、修正或不改变既有认识。
小型公式核算可以验证理解，但必须区分分析核验、模型计算与实验事实。

专题综合在证据形成自然闭环时进行，不按固定篇数触发。缺件记录其对结论的
真实影响，不自动化为用户待办。未经定位的主张和未完成的整篇阅读不伪装完成。

## 可复用的 worker 监督方法

提示词监督应落实为可验证的任务合同，而不是情绪性评价或“保证认真”的口号：

- 每次明确科学问题、目标、原件版本、实际所供页、逐项交付 ID、权限与验收。
- API 模式实际附送内容；本地路径不等于模型已读文件，也不能据此声称有终端工具。
- 有效 JSON 仅表示可解析；请求 ID、返回 ID 和实际页范围必须逐项对账。
- 关键结论回原件核验，真实歧义和缺页保留；不以模型自称完成或互相同意作证据。
- 单元完成与整篇阅读分开，遗漏不静默接受，partial/blocked 不算完整学习。
- 返工明确原错误 ID、定位、需要的修正和已通过项，只补错项，不重复整篇阅读。
- 原文和响应缓存复用；只有管理层验收后才写正式知识，不让并发 worker 互相覆盖。
- 记录真实调用模型/参数/usage 和结束状态，不把请求档位、解析成功或模型自报当作执行结果。

完整可复用提示词、已填原件实例和验收/返工规则保存在
`outputs/plans/20261119-archive-deep-learning.md` 第 5 节。

## Research Trigger

User-requested collection or learning-design question; the original scope and historical stage are retained below.

## Grounded Evidence

Evidence anchors: [[international-thesis-acquisition-20261119-source]], [[hungerford-1979-ill-angular-correlation-164dy]]. Original locators and actual coverage are recorded in those sources and the tables below.

## Provisional Reasoning

The original discussion below is a scope-bounded data/method comparison or learning design, not a new experimental result or certified field-wide prevalence estimate.

## Assumptions

Bibliographic identity, version and reading coverage must be checked separately; filenames and page counts do not establish independent works or completed reading.

## Competing Explanations

Different reported values can arise from different experiments, conventions or analysis conditions; repeated publication of one experiment is not independent support. No new physical alternative is invented merely to fill this section.

## Transfer Conditions

Reuse only with the original measurement object, geometry/gates, calibration, definitions and uncertainty treatment. Learning-design recommendations remain recommendations, not physical claims.

## Failure Conditions

Missing originals, illegible figures, unresolved version/identity or absent numerical covariance constrain reuse; do not silently fill gaps or claim a full reproduction.

## Falsification or Reverse Tests

Return any material numerical or methodological discrepancy to its source locator; revise the interpretation if the original contradicts the extraction or proposed classification.

## Open Questions

Outstanding scientific or acquisition boundaries are listed in the original discussion below or the linked sources. Historical download requests are superseded by the user closing acquisition.

## Human Review

No new human-reviewed event is asserted. The user closing downloads or accepting a table format does not certify every scientific claim.

## Promotion or Rejection History

2026-11-19: normalized provenance and schema for baseline publication; retained provisional status and original numerical content. No automatic promotion of physical conclusions.
