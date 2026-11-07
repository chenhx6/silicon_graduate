---
type: source
title: "Zagrebaev et al. 2001 - Synthesis of superheavy nuclei: How accurately can we describe it and calculate the cross sections?"
aliases: [Zagrebaev 2001 superheavy survival, superheavy multi-chance fission survival, ZAG01]
created: 2026-10-30
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: skimmed
title_original: "Synthesis of superheavy nuclei: How accurately can we describe it and calculate the cross sections?"
authors: [V. I. Zagrebaev, Y. Aritomo, M. G. Itkis, Yu. Ts. Oganessian, M. Ohta]
journal: Physical Review C
year: 2001
volume: 65
issue: 1
pages: "014607"
doi: "10.1103/PhysRevC.65.014607"
canonical_source: "https://doi.org/10.1103/PhysRevC.65.014607"
citation_key: zagrebaev2001superheavy
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/PhysRevC.65.014607.pdf"
raw_sha256: 0fbce3d3faded1e072ce25eeb8a758cabb81d54b2df2eee71f55efd1686116c8
archive_required: true
nuclei: [208pb, 248cm, 292114, 294116, 298114, 304120]
reactions: ["48Ca + 248Cm -> 296-x 116 + xn", "48Ca + 244Pu -> 292-x 114 + xn"]
experiments: [Dubna-FLNR-DGAS]
models: [multidimensional-langevin, statistical-model, Bohr-Wheeler-fission, Ignatyuk-level-density]
observables: [evaporation-residue-cross-section, survival-probability, fission-barrier, gamma-f-over-gamma-n]
methods: [coupled-channels-capture, Langevin-trajectory-simulation, multi-chance-fission-cascade]
tags: [superheavy-elements, multi-chance-fission, survival-probability, fission-barrier-inversion, Day27]
---

# Synthesis of superheavy nuclei: How accurately can we describe it and calculate the cross sections?

## 2026-11-07 原件核查与旧数值撤回

本次按原件PDF p.1、pp.6–7的Eqs.(1)、(7–11)和相关正文定向重读，
并检查14页全部图表题注。原件图号止于Fig.10，未发现下文旧ZAG01-3/4
所称Fig.12或Table1。这四条旧数值尚未在原件中完成逐项认证，
不得继续以“direct/source-reported”使用。旧条目标识保留为明确撤回记录，
其原文由Git历史保存；不能因为旧needs_review=false恢复可信度。

本次实际阅读范围只支持`skimmed`，不沿用既有“全篇deep-read”保证。
未重新阅读其余所有章节、未复现反应计算，也未逐一验证所有参考文献。

| ID | 重新核验的来源陈述 | claim_kind | locator | 适用边界 |
|---|---|---|---|---|
| ZAG01-R7-1 | ER截面分为分波俘获、复合核形成和到特定冷剩余核的衰变概率三个阶段；作者明确称其为近似分解。 | author-interpretation + model-result | PDF p.1，Eq.(1)及右栏 | 不能把其中任一概率的区域经验值视为普适常数。 |
| ZAG01-R7-2 | xn级联对各蒸发中子能量积分，含Γn/Γtot和终末γ冷却概率。 | model-result | PDF p.7，Eqs.(10–11) | 固定中心能量下的两宽度乘积是进一步近似。 |
| ZAG01-R7-3 | 作者计算Γtot时还计入γ、质子和α等通道，裂变势垒、壳阻尼和能级密度均带模型输入依赖。 | model-result | PDF pp.6–7，Eq.(7–9)及§V | 不支持所有步长都Γf/Γn=100–1000或固定生存率的主张。 |
| ZAG01-R7-4 | §V.A的No邻区例子给液滴势垒部分约1.2 MeV，并讨论壳效应主导；“主要由壳修正决定”不能改成所有超重核宏观势垒严格为零。 | model-result | PDF p.7，右栏末段 | 该数值属于指定反应/模型背景，不是全核区测量。 |

**Knowledge Impact：revises。** 修订
[[high-spin-isomers-and-decay-modes-systematics]] 的存活公式边界。
P0：未发现未隔离的原件身份或哈希问题；虚构locator和未证实数值已在本节隔离。
P1：ZAG01-1/2的具体阈值、势垒和热阻尼数值仍需另行对应真实图/公式，
当前不用于定量预测。以下历史表不构成当前推荐数值来源。

## Bibliographic Record

PRC 65, 014607 (2001), DOI `10.1103/PhysRevC.65.014607`.

## Scope and Reading Depth

- Completed reading_depth: `skimmed`；本轮为定向原读，不沿用历史全篇保证。
- Covered scope: PDF p.1及pp.6–7的阶段分解、宽度、级联积分和相关说明；
  全部14页仅额外检查图表题注，未据此宣称正文全读。
- Not covered: 其余正文逐项核查、反应程序与参数敏感性重放。
- Coverage caveats: 旧数值表的认证已撤回，以下记录用于追踪本任务认识修订。

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| ZAG01-1 | 撤回旧的普适“宏观势垒为零”和固定势垒/分离能数值认证；原文No邻区例子还给出非零液滴部分。 | unsupported-task-claim-withdrawal | 本轮原件纠错 | PDF p.7 §V.A；见ZAG01-R7-4 | true |
| ZAG01-2 | 撤回旧的统一温度/激发能对应Bf≤1.5 MeV断言；热阻尼与势垒必须绑定指定模型和核素。 | unsupported-task-claim-withdrawal | 未完成原断言核验 | PDF p.6 Eq.(7)周围的模型定义；旧数值未认证 | true |
| ZAG01-3 | 撤回固定Γf/Γn及每一步统一存活比例；所引Fig.12不在原件中。 | unsupported-task-claim-withdrawal | 原件范围核查 | 全文图题止于Fig.10；PDF p.7 Eq.(10) | true |
| ZAG01-4 | 撤回固定3n/4n生存率及所引Table1认证；具体ER截面须保留分波、能量级联与输入。 | unsupported-task-claim-withdrawal | 原件范围核查 | 未发现Table1；PDF p.1 Eq.(1)、p.7 Eqs.(10–11) | true |

## Cross-Mass-Region Transferability Significance

1. **稳定核统计蒸发模型向超重区迁移的条件边界**：在本文指定的稳定核与超重核模型参数之间，直接忽略壳修正热阻尼和裂变竞争会使 calculated production cross sections 偏高；高估倍数取决于反应、势垒、level density 和多次裂变参数，不能作为普适实验修正因子。
2. **微观热相变与动力学耗散的模型分解**：本文把超重核生存概率分解为中子蒸发速率、热壳能耗散和裂变竞争的共同作用；这是统计/Langevin framework 内的结果，不是对所有超重核反应的唯一因果定律。

## Summary

本轮核对三阶段截面框架及含竞争宽度/能量积分的级联近似，撤回不存在图表
所支撑的旧统一数值。该理论来源没有提供脱离核素、能量、自旋和参数的普适生存率。

## Key Results


| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZAG01-R7-1 | 三阶段ER截面分解带近似和输入条件。 | model-result | direct | PDF p.1 Eq.(1)及讨论 | false |
| ZAG01-R7-2 | xn级联含Γtot、中子能量积分和终末γ冷却。 | model-result | direct | PDF p.7 Eqs.(10–11) | false |
| ZAG01-R7-3 | Γtot计入相应竞争通道；势垒、壳阻尼和能级密度依赖模型。 | model-result | direct | PDF pp.6–7 Eqs.(7–9)、§V | false |
| ZAG01-R7-4 | 指定No邻区例子的液滴势垒部分约1.2 MeV，限制“所有宏观部分为零”的断言。 | model-result | direct | PDF p.7 §V.A末段 | false |

原页面既有的直接报告、作者解释和模型结果保持原文分层；缺失 locator 或原件的项目仍保持相应证据边界。

## Competing Interpretations and Limitations

竞争解释、来源依赖、原件访问和必要伴随观测缺口按原页面记录；不得把模型结果或评价字段升级为直接实验事实。

## Extracted Pages

本轮定向读取PDF p.1、pp.6–7并检查14页图表题注；未重做其它正文、
数值程序或实验比较，后续按具体claim补核。
