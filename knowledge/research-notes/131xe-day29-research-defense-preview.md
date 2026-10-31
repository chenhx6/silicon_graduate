---
type: research-note
title: "131Xe 794-keV宇称与882-keV双根：Day29研究设计答辩预习"
aliases: [131Xe Day29 research defense preview]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [chakraborty-2023-131xe-wobbling-origin, banik-2020-131xe-multiple-band-structures]
created_from: "Day28 uncredited Day29 preview"
promotion_target: "131xe-low-spin-partner-crosswalk"
tags: [131xe, research-design, negative-control, polarization, internal-conversion, l4-readiness]
---

# 131Xe 794-keV宇称与882-keV双根：Day29研究设计答辩预习

## Research Trigger

Day28已把两个未决问题压缩为可检验设计：1600.9-keV节点的2020/2023宇称版本冲突，以及881.8-keV `δ` 双分支。本文是Day29的无学分预习，不改变Day28课程状态，也不把设计输入当作已有实验数据。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 2020的794.8-keV行列17/2+→15/2− E1；2023列17/2−→15/2−且766.5-keV新增连接 | [[banik-2020-131xe-multiple-band-structures]] BNK20-D28-2/3；[[chakraborty-2023-131xe-wobbling-origin]] C23-D28-2/8 | 两篇来源的原件表/图 | 2023 Table I没有766偏振；宇称冲突未裁决 |
| 881.8-keV线RDCO=0.64(11)、偏振栏空，Fig.5有小根与负δ交点 | [[chakraborty-2023-131xe-wobbling-origin]] C23-D28-3/9 | C23 Table I/Fig.5 | 没有原始峰形、角对、响应、协方差 |
| 794.6-keV评估EKC与BrIcc候选集合 | [[131xe-1601-parity-version-boundary]] | ENSDF评估记录与官方BrIcc回执 | 原始EKC表和误差语义未闭合 |

## Provisional Reasoning

### 最小测量组合

**A. 794-keV宇称/多极性块。** 优先取得或新测量同一794.6/794.8-keV线的K壳电子与γ符合比，并同时记录电子能量、K层峰、γ峰、背景、门条件和效率协方差。比较E1、M1、E2以及必要的M2候选，统一使用同一BrIcc版本、Z、能量、壳层和FO/NH约定。历史`EKC=0.0017(7)`只能作为待核输入，不能把评估字段当作已复现的primary计数。

**B. 882双根块。** 对881.8/880.1双线逐门保留峰形和污染模板，按实际clover/crystal角对形成DCO，并在已校准Compton scatter-bin中测量882本线偏振。使用同一1046-keV条件取向/feeding模型，记录816/930上游门、663控制门、随机窗和sideband；704.6-keV线只作同母态竞争退激的取向参考，不能与882硬设互符合。

**C. 共享校准块。** 同时采集或复用同run的已知E2、E1和无偏振校准线，建立能量增益、全能峰效率、K电子传输、有限几何、Compton分析响应、轴符号、deadtime/livetime和背景缩放的联合协方差。校准数据只能在联合似然中使用一次。

### 必需的最小输入

| 输入 | 不能省略的字段 | 缺失后果 |
|---|---|---|
| 对象与门 | run/时间段、event或互斥bin、峰窗、sideband、cascade order、双线峰形 | 不能确认794/882是否是同一对象或估计880污染 |
| γ响应 | 每个角对的接受度、效率、addback/抑制、几何和校准协方差 | 不能把名义40/90/125度替代真实DCO响应 |
| 电子响应 | K壳电子传输、探测效率、背景、电子/γ时间窗和共同归一 | 不能把EKC与BrIcc直接比较 |
| 取向/feeding | 1046条件密度矩阵或统计张量、未观测feeding和退取向 | 不能把704参考线自动当作完整取向标定 |
| 偏振响应 | scatter-bin、`Qeff`或完整Stokes矩阵、轴符号、串扰和阈值 | 不能由一个总`Δasym`选择882根 |
| 协方差与代码 | 原始计数或完整压缩Σ、ANGCOR版本/input、相位/δ约定 | 不能给联合likelihood、σ或全局根权重 |

### Negative controls

1. 用已知642-keV E2线检验角度响应和取向传播；
2. 用2020反复标为E1的795-keV线检验电子/γ归一与电磁响应，但不把它当作794节点宇称裁决；
3. 用704.6-keV同母态竞争退激检验1046母态的条件取向，明确其不能作为882互符合门；
4. 用无偏振源和空门检验Compton轴符号、随机背景和双线模板。

### 三种结果与 belief revision

| 结果 | 更新 | 正式措辞 |
|---|---|---|
| 794电子/γ比与E1预测分离，且882两分支经profile后不交 | 削弱2020 E1版本和RDCO小根简并；可提高指定重指认的优先级 | “在声明的响应/理论合同内排除候选” |
| 794与M1/E2凸包或882两分支预测重叠 | 保留宇称冲突与双根，不能排序 | “数据对该设计不足，未裁决” |
| 共同响应显示污染/取向解释吸收分支差异 | 降级原先的小根和模式判断，优先修正对象/门身份 | “先修订谱学身份，再讨论机制” |

## Assumptions

设计只假定可获得真实事件或充分压缩的联合计数；不假定原始数据一定存在，不假定E1/M1/E2理论误差独立，不假定同一母态不同退激共享完整取向，也不把模拟计数当作实验结果。

## Competing Explanations

宇称差异可能来自共同沿用的旧标签、污染/双线、不同版本的放置或真实重指认；882双根可能来自真实角分布简并、取向未知、响应吸收或880污染。设计必须先区分对象和响应，再比较signature partner、wobbling、粒子—芯耦合等解释。

## Transfer Conditions

这套设计可迁移到其它A≈130混合比双根问题，但必须重新校准核素、反应、探测器、门选和取向。BrIcc的Z、能量、壳层和原子模型不能跨核素直接复用。

## Failure Conditions

原始事件或逐门峰形不存在、电子探测器无法校准、880污染无界、取向模型无控制、偏振轴符号未知、共享校准被重复计权、或理论ICC误差/能量误差无定义，均会阻止事件级L4和统计裁决。遇到这些失败时只保留readiness boundary，不生成代理结果。

## Falsification or Reverse Tests

若所有可实现的794电子/γ和882偏振/角分布设计在共同响应剖面后都不能分离候选集合，则“单次最小设计可稳健选根”的命题被否定；若能分离，也只支持该实验/理论合同下的候选排除，不自动证明wobbling或signature partner。

## Open Questions

已有INGA原始事件、794电子数据和880峰形是否保存？电子探测器与γ阵列能否共享事件时间戳？原始ENSDF EKC误差是统计、系统还是评估综合？这些问题决定Day29正式答辩能否进入事件级L4。

## Human Review

- Review scope: Day29无学分预习；基于Day28已核source与882响应合同。
- Decision: provisional；未发生human review。
- Complete unresolved P0/P1 inventory: 原始事件/电子响应、共同协方差和primary EKC表仍为P1边界。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-30 | Day29 uncredited preview | none | provisional research-note | Day28证据路线局部饱和且距离硬截止超过120分钟；设计输入仍缺真实数据 | [[131xe-low-spin-partner-crosswalk]] |
