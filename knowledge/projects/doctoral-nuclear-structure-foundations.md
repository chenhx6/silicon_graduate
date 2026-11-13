---
type: project
title: "博士论文前置研究：六区集体激发、核芯形变与实验观测链"
aliases: [博士论文前置研学, doctoral-nuclear-structure-foundations]
created: 2026-11-08
updated: 2026-11-13
status: active
review_status: unreviewed
research_status: active-L3
project_stage: phase3-A130-frontmatter-rewrite
confidentiality: public
sources: [cline-1986-nuclear-shapes-coulomb-excitation, poves-2020-limits-assigning-nuclear-shape, henderson-2020-quadrupole-invariant-convergence, wu-hongyi-2020-general-purpose-digital-daq-thesis]
tags: [doctoral-foundations, collective-excitation, triaxiality, cross-region, research-design]
---

# 博士论文前置研究：从核子运动到可测量的形变信息

## 当前任务与阶段边界

### Agent active summary

R1–R3第一阶段已完成知识、原件/数值核验及授权发布，
原生第一阶段goal已完成。六区/21主题/七项依据见
[[doctoral-r3-readiness-evidence-matrix-20261108]]，领域未决问题仍开放。
章节设计goal也已完成验证发布。
[[doctoral-thesis-architecture-and-section-map-20261108]]选定五章/39节，
[[doctoral-thesis-sample-reading-design-findings-20261108]]保存有限样本的观察。
当前active goal为A130前置非个人成果正文重写：
11月8日旧34文件完成逐项归档；11月13日复核发现工作树归档已被后续外部操作移除，
其中17项原正文/源文件及旧PDF仍可由Git历史精确恢复，保持用户删除现状。
[[doctoral-thesis-notation-and-evidence-style-20261108]]统一符号/引用，
各稿仍须逐主张、公式与读者台阶核查，尚未完成整部正文。
三样节与第二批七节的发布已经核对。
11月13日起改用用户提供的LaTeX工程，15节、附B/C已交付范围与7组矢量图
已作为128页检查点发布。当前内容接受范围扩展到27节：第一章全章、第二章全章、
3.1/3.2/3.3/3.5/3.6、4.1/4.2/4.3/4.6以及5.1/5.3/5.4/5.5/5.9；
附B/C和附F已交付范围随组稿核验。其余12节与必要附录继续写作和返修，
尚未完成整部39节稿。本次27节检查点已编译为220页并发布，引用、交叉引用、缺字、
越界排版及Bib问题均为0；64项工程输入集合和9组SVG/PDF已逐项核对。
具体范围与保留的非致命提示回任务回执，不套用早期128页结果。
已写内容不等于未知个人成果或学校送审材料。
写作暴露的原件与推导修正已分别保存为
[[a130-rewrite-invariant-recoupling-and-width-boundaries-20261108]]、
[[a130-rewrite-chiral-nonorthogonal-and-fingerprint-boundaries-20261108]]、
[[a130-rewrite-absolute-rates-and-selection-boundaries-20261108]]；
样节验收关注科学论证和读者台阶，不要求将所有开放争议先解决。
第二批新增[[a130-rewrite-bcs-convention-and-model-hamiltonian-boundaries-20261108]]与
[[a130-rewrite-digital-pulse-gain-and-data-boundaries-20261108]]：
同一BCS字母不保证同一哈密顿量，形式正确的数字滤波式也不能替代逐行数据核对。
本轮新增的可复用修正见
[[a130-rewrite-cross-region-comparison-and-e0-constraints-20261113]]、
[[a130-rewrite-magnetic-unit-and-numerical-normalization-20261113]]、
[[a130-rewrite-forward-observables-and-cascade-consistency-20261113]]与
[[a130-rewrite-seniority-k-selection-20261113]]：
模型输出与可观测量的映射、支路与ICC口径、最终级联概率、单j允许占据及
独立Fock空间控制均须保持各自条件，不能从区域名称或一条能量曲线直接迁移。
取向展开与参考系条件另见
[[a130-rewrite-alignment-frame-and-precession-20261113]]，形状坐标与取向坐标的
质量加权、混合及干涉边界见
[[a130-rewrite-shape-orientation-mode-coupling-20261113]]。

用户要求先全力研学，再重建博士论文。前置研究和设计均已收束，当前进入正文，
具体物理研学继续服务高价值问题与写作暴露的缺口。
总控负责问题选择、基础推导、原件核查、跨区综合与最终就绪判断；
Gemini Flash Tiered/high承担大部分分域研学；复杂理论交给Terra/xhigh。
模型路由与产量不能代替正确性。原生goal于本会话创建，任务状态保持active。

研究骨架为：
**壳结构与占据 → 配对和集体惯量 → 量子涨落 → 激发模式 →
电磁/弱观测量 → 实验响应与反演。**
质量数是比较坐标，不预先决定某个模式存在与否。
[[isomer-six-region-transfer-research]]保存此前机制迁移成果，本项目向基础理论、
低自旋形变测量和实验技术补足，避免重新运行已经闭合的toy反例。
当前跨区综合入口为[[six-region-shape-and-collective-dynamics-foundations]]；
它比较已核代表案例，不能当作六区所有核已穷尽或论文准备已经结束。

用户对旧稿的不满是新的研究触发，旧“完成”“Master”等标签不构成准备充足的证据。
11月8日当时，`raw/writing/gpt/A130/`的原34文件逐一核SHA后完整移动到
`raw/writing/gpt/_archive/20261108-A130-before-rewrite/original/`，
集合manifest的归档门已通过；未递归删除或改写Git历史。
用户已明确授权准备充分后清空该精确目录并重写；
目前条件已满足并已实施可恢复目录替换，新A130保存分节稿和证据台账。
本阶段不触碰其它手稿，不修改用户拥有的`PLAN.md`，不改变daily课程或调度。
这项普通专题研究没有凭空设定的每日15:00截止。

## Research Question

1. 实验室旋转不变量、有效内禀电荷形状、物质分布与集体惯量分别是什么？
   一个平均角、一个势能极小点或一个转动带能否约束其余量？
2. 同一核或邻核的不同组态为何可能出现不同形状、惯量和取向动力学？
   粒子/空穴、占据、配对与自旋分别改变哪个环节？
3. 六区看到的模式有多少来自共同的动力学，有多少依赖具体壳结构和可布居窗口？
   “未见”“未搜索”“理论上不稳定”如何区分？
4. 静态三轴、γ软分布、离散形状混合、核芯振动和取向振动何时可被同一组数据混淆？
   哪一项新观测最可能改变解释排序？
5. 八极、异能态与弱衰变提供的是独立探针，还是同一数据及模型的重新表达？
6. 数字获取和数据选择怎样改变强度、分支、角关联及寿命？
   如何从校准信号一直解释到核结构主张？

这些是研究问题，不是已经发现的关联。每个候选都须有最强替代解释、
适用条件、失败判据及可获取的区分观测；不能从局部检索无命中宣称新颖。

## Evidence Available

| 核区 | 本轮主要增量 | 与其它区的迁移问题 | 必须保持的区别 |
|---|---|---|---|
| A≈60 | 绝对E2、轻核形状共存与高自旋残余相互作用 | 低自旋电荷形状约束能否限制高自旋取向模型 | 不同核、不同组态、不同自旋不是同一核芯测量 |
| A≈80 | Kr多步CoulEx与形状混合；与已有Br/As宇称资料衔接 | 带符号E2网络怎样区分软分布与离散混合 | CoulEx形状信息不直接证明八极或手征 |
| A≈100 | 98→100Zr的跃迁强度和微观壳重排 | 突变、共存与γ软性是否来自同一种势面变化 | Zr的形变转变不代替Mo/Ru的逐态证据 |
| A≈130 | 130Ba偶偶核激发组态与核芯/取向耦合 | 奇A/奇奇的模式语言如何迁移到两准粒子偶偶核 | 能谱、混合比、绝对矩阵元和模型波函数分开 |
| A≈160 | 轴对称高K进动与三轴TSD摆动 | 不同稳定转轴、惯量和小振幅极限如何衔接 | 相似带间E2不意味着相同形变或同一激发机制 |
| A≈190 | Hg/Pt/Os低自旋CoulEx与既有Ir异能态互补 | 低自旋软性对高自旋组态究竟约束什么 | 扁椭、三轴、进动、K混合不得靠区名合并 |

本表是工作合同；具体实验结论只从对应source及locator取得。
六区可复用结论将在本轮原件核查后写回本项目及综合页，不把worker完成状态当作结论。

已回原件并纠正的本批知识入口：
[[doctoral-r1-g26-a60-collectivity-20261108]]、
[[doctoral-r1-g27-a80-shape-coexistence-20261108]]、
[[doctoral-r1-g28-a100-shell-shape-20261108]]、
[[doctoral-r1-g29-a130-core-orientation-20261108]]、
[[doctoral-r1-g30-a160-precession-wobbling-20261108]]、
[[doctoral-r1-g31-a190-charge-shape-20261108]]。
基础解释与有界模型为
[[doctoral-foundations-laboratory-shape-and-dynamics-20261108]]、
[[doctoral-r1-t03-shape-invariants-and-softness-20261108]]；
实验链见[[doctoral-r1-g32-digital-daq-observable-chain-20261108]]，
复杂弱算符的独立核查见[[doctoral-r1-t04-first-forbidden-operator-audit-20261108]]。
本批14项worker均已回传并关闭，总控按原件重建后进入整体检查；本页链接不自动赋予某个未限定主张可靠性。

## 全范围学习矩阵

“核心深入、两翼较少”不能成为其它主题只登记而不学习的理由。以下主题全部在范围内；
深度状态按原件理解、推导、可测量量、竞争解释和跨区迁移分别说明，不计算伪精确总完成率。

| 主题 | 已有基础入口 | 本阶段需要能讲清的内容 | 当前增量/缺口 |
|---|---|---|---|
| 旋转对称性与形变语言 | [[cline-1986-nuclear-shapes-coulomb-excitation]] | 实验室态、体坐标、张量、有效形状及有限体系的区别 | 原始历史来源、算符约定与清晰解释 |
| 四极形状矩与高阶闭合 | [[poves-2020-limits-assigning-nuclear-shape]]、[[henderson-2020-quadrupole-invariant-convergence]] | 有限矩、符号环、截断、加权角分布及误差 | T03推进真实动力学可识别性；避免重做checkpoint113/150 |
| γ软/刚与集体Hamiltonian | [[universal-triaxial-collective-mechanics-and-cross-region-migration]] | 测度、势曲率、惯量、边界条件、能标 | 静态矩与动力学信息的独立性 |
| 转子、振动与配对 | [[book-bohr-mottelson-nuclear-structure-vol2]] | 近似如何产生、失效在哪里、对应什么观测 | R2已核坐标质量、PC/IB/TV、实/虚QRPA、空间/配对NG与实际应用；共同模型、非绝热域和原producer仍有缺口 |
| 壳演化与组态重排 | [[campaign-g05-rong-2023-96zr-mdc-cdft]] | 单极、张量、配对、占据反馈和type-II机制 | Zr实验与微观模型的合同，继续补基础综述 |
| 形状共存与混合 | [[triaxial-collective-evolution-across-mass-regions]] | E0、绝对E2、对角矩阵元、混合及可辨别性 | Ge/Kr/Zr/Hg原件的状态映射 |
| 手征动力学 | [[octupole-and-chiral-coexistence-in-transitional-nuclei]] | 对称性、有限隧穿、波函数、EM模式及替代解释 | 跨区组态与核芯可变性的共同模型 |
| 摆动与进动 | [[continuation-g16-soft-core-wobbling-20261107]]、[[continuation-g23-lu163-absolute-quadrupole-20261107]] | 稳定轴、软模、小振幅与准粒子耦合 | 130Ba与高K轴对称极限；不以δ单点裁决 |
| 高自旋、TSD与带交叉 | [[campaign-g07-a160-tsd-kmix-20261107]] | 可布居窗口、终止、惯量、顺排与绝对E2 | 模型输入版本和替代组态 |
| 八极与反射对称性 | [[continuation-t02-ru102-covariant-effective-e1-20261107]] | 轴向/非轴向、宇称恢复、E1/E3和极化 | 复用既有RAT-PRM原读，推进共同算符比较，不能只讲Δl=Δj=3 |
| 电偶极与剪刀模式 | [[continuation-g14-ru102-si-thesis-20261107]] | 平移不变性、有效算符、独立响应及强度分布 | 联合Cov/未拟合预测；同数据依赖 |
| Seniority与K异能态 | [[high-spin-isomers-and-decay-modes-systematics]] | 节点、粒子空穴、两端K混合、能量与矩阵元瓶颈 | 已有精确控制；转向真实多轨道证据 |
| GT、禁戒β与gA | [[continuation-g19-cd-in-common-weak-operator-20261107]] | 总和规则、有限Q窗、分支、FF形状因子与有效算符 | 已读Zhi2013并有T04独立核查；真实核共同实现与留出仍待完成 |
| β缓发粒子 | [[doctoral-r3-weak-operators-and-delayed-particles-20261108]] | feeding、阈值、分波/γ竞争、最终多重度与探测响应 | IAEA2021原件已定向学习；具体核的Pn需完整级联/效率，不由GT主题代答 |
| 0νββ与形变/配对 | [[isomer-shell-evolution-astrophysics-and-superheavy-transfer-20261107]] | 矩阵元、模型空间、算符和形状匹配 | 已读2010/2013投影与配对原作；更近三轴/算符研究继续，不由GT淬灭直接外推 |
| Astromer与热耦合 | [[isomer-shell-evolution-astrophysics-and-superheavy-transfer-20261107]] | 中间态网络、详细平衡、时间尺度及热化失效 | 已读176Lu K混合与等离子体整体瓶颈；实际轨迹与率输入逐任务补 |
| NEEC与耗散 | [[mo93-neec-evidence-and-depletion-transfer-20261107]] | 通道、产额、污染反证与电子环境 | 不把理论截面增强当净实验耗散 |
| 核钟 | [[nuclear-clock-isomer-learning-and-transfer-20261107]] | 核跃迁、宿主、线宽、系统误差与频标 | 版本/时间敏感的新进展须查证 |
| 熔合蒸发与超重核 | [[high-spin-isomers-and-decay-modes-systematics]] | 捕获/完全熔合/存活三因子和实验产额 | 已核逐分波/级联原式与历史实例；实际动态输入仍需逐体系补 |
| 在束γ谱与寿命 | [[continuation-g23-lu163-absolute-quadrupole-20261107]] | 选择定则、DCO/偏振、δ双根、DSAM/RDM与feeding | 响应、Cov与可复现实验输入 |
| 数字电子学与获取 | [[wu-hongyi-2020-general-purpose-digital-daq-thesis]] | 信号、滤波、时间、触发、死时间及观测偏差 | G32原件学习，从吴论文出发而不代写章节 |

若入口名称发生变化，应追踪真实source；导航不是证据。
本矩阵不声称每一主题已经完成博士深度，也不要求先解决领域内所有开放争议。
R3按每个主题的公式、实验链、反方和适用域重新对账，见
[[doctoral-r3-readiness-evidence-matrix-20261108]]。R1/R2表中的开放producer、
Cov与个别原文仍是具体研究边界，不作为无期限推迟基础准备的理由。

R3新增解释入口：
[[doctoral-r3-quantum-labels-and-model-boundaries-20261108]]、
[[doctoral-r3-daq-spectroscopy-inverse-20261108]]、
[[doctoral-r3-isomers-shell-and-survival-20261108]]、
[[doctoral-r3-weak-operators-and-delayed-particles-20261108]]。
核钟与NEEC旧页已原位修订无源门槛及过强因果，保留Git修订历史。

## Current Hypotheses

采用独立生成→证据核查→反方评议→重新生成的短循环。已有结果已公开给worker的，
标记为文献启发，不能声称盲态独立验证。总控不按赞成票选物理机制。

候选登记必须包含：

- 问题与来源、目前已看到的数据、实际检索范围；
- idea、assumption、prediction与located evidence的区别；
- 共同Hamiltonian、算符、组态、自旋区间及需要冻结/释放的输入；
- 最强竞争解释，以及它能否产生同样的预计信号；
- 最小区分观测、已有实验可达性、零结果价值、失败与转向条件；
- 下一步属于继续检索、模型计算、数据重分析还是新实验设计。

优先级依据是信息增益、与本项目的相关性、可获得输入和可证伪性。
全球新颖性未充分检索时只称候选。多模型同意、更多篇幅或更多token不增加证据独立性。
无实际输入时保留L3合同；有清楚可重放的输入与控制才进入有界L4。

本轮比较中保留的机制问题包括：形状—取向联合分布相对于SCS边缘图增加什么、
静态PES未固定的磁关联能否影响M1、壳占据反馈与形变如何共同受未拟合EM限制、
以及门选/联合live能否混淆弱分支。它们均为候选，不是新核模式。
已撤回的任意角宽、固定W.u.、整区禁戒和单个δ充要线不再参与候选排序。
候选、反方、输入可得性和失败/转向合同见
[[doctoral-foundations-research-question-register-20261108]]，不以推测数量计完成度。

## 进入论文设计的准备条件

以下为解释和证据的充分性，不是论文篇数、固定页数或模型打分：

1. 六区均有至少一个能重建“物理问题—原始测量—作者推断—替代解释”的实质案例；
   比较真正涉及壳占据、配对/惯量、形状涨落、激发与观测链，不只是模式名录。
2. 核心框架能从假设、约定和推导讲起，指出刚性、绝热、小振幅、截断与有限体系边界；
   历史路径来自实际原始文献，不编造“早期科学家如何想”的故事。
3. 两翼全部主题有实质理解与可追溯材料；未决问题明确，不能靠相邻主题代答。
4. 实验链包含电子学、探测响应、选择、统计、寿命和EM反演；
   已知方法与用户个人实验参数严格区分。
5. 新观点说明相对旧框架增加了什么可检验内容，而非仅使用新术语。
6. 存在面向初学者的解释能力检查：能解释一个公式从何来、符号可测性、典型误解和反例；
   叙事引子不替代推导，不虚构个人成果或实验经历。
7. 总控完成分域原件抽查、推导/数值核验及整体缺口复盘后，再记录是否就绪。

当前判断：**前置研究/设计均已验证发布，LaTeX正文正在迁移、增写与核查。**
旧稿原正文/源文件及旧PDF可由Git历史恢复，新A130工程已启用。七项条件、21项主题和六区原件见证已逐项列出，
不是“整个核结构都已研究完毕”的声明。
就绪不是“把所有争议解决”；未决争议可以成为高质量综述的一部分，
前提是理解证据与竞争解释，而不是掩盖缺口。

## Risks and Blockers

部分worker初稿出现了理论列误当实验、跃迁方向/统计因子错误、页码/版本不符、
普适化阈值和不实遥测。总控以原件缩减重建，未把修辞强度或多模型同意作为证据。
已核知识与过程草稿的身份应保持明确；源内数值疑点不应猜测修补。R1的23个source/15个collection的局部归档门已通过；整库发布检查以本批最终回执为准。
Kumar1972全文、部分真实核的完整矩阵元/Cov、联合形状—取向波函数和用户实验设置仍缺。
这些科学边界不等于请求用户确认，也不妨碍发布已正确限定的研究结果。

## Next Actions

R3来源归档、数值/路径/A130保护、检索及发布验收已完成。
设计研究已发布五章/39节工作结构、通用合同及六个重点推导合同；
五份学位样本同时记录优点、可补台阶和外推边界。
接收演练与发布完成后，已派Gemini写1.2/3.5/5.9样节；
首份1.2-v1已冻结送Terra审6j/高阶矩/原作归属，Gemini同时按总控范围/文体意见修订。
先逐节核查并完成可读样本，再扩大到其余正文。
不预设用户个人实验经历或结果，也不在设计前用旧目录机械改名。
具体未决物理继续以D9–D12等问题推进，可与写作准备并行；
阶段转换不结束长期研学，不把未知LEC/完整Cov/所有producer当无限门。
过程回执在`outputs/l3/20261108-doctoral-foundations-r1/`，
R2在`outputs/l3/20261108-doctoral-foundations-r2/`；
执行计划为`outputs/plans/20261108-doctoral-foundations.md`及R2计划。
R3过程在`outputs/l3/20261108-doctoral-foundations-r3/`，
执行计划`outputs/plans/20261108-doctoral-foundations-r3.md`。
当前设计过程在`outputs/l3/20261108-doctoral-thesis-design/`，
计划在`outputs/plans/20261108-doctoral-thesis-design.md`。
正文过程在`outputs/degree-dissertation/20261108-A130-rewrite/`，
计划在`outputs/plans/20261108-A130-frontmatter-rewrite.md`；
实际分节稿/台账在精确A130目录，旧目录归档不作科学内容源。

## 2026-11-13：LaTeX正文与执行分工

用户指定以`raw/writing/gpt/A130/these_2023_template/these_template/Thesis.tex`
为当前正文入口，分节内容写入`Tex/Sections/`。已有Markdown研究稿保留为迁移输入；
此后的正文续写直接使用LaTeX。新图用Python生成，在工程`Img/`同时留存SVG和PDF，
正文引用PDF，并记录输入、生产代码和模型/实验身份。

当前GPT会话承担章节蓝图、详细执行合同、关键科学审查和接受/定点返修；
Gemini Tiered/high承担主要阅读、正文迁移与续写、工程清理、绘图和编译修复。
只有需要新的复杂独立推导时才安排Terra/xhigh。
复用此前已核实的原表和约定，默认审查增量、冲突和确定性结果，不重复整篇改写。
其中2.2节的谱重心、单极冻结及非正交重叠沿用
[[a130-rewrite-espe-centroids-freezing-and-overlaps-20261108]]中的定义与限制。
2.5节写作暴露的投影选择条件、度规截断和有限试探空间边界，
同步保存于[[a130-rewrite-projection-selection-and-metric-truncation-20261113]]；
投影本身不保证精确的全空间本征态或刚性转子能谱。
数字定时的算法约定、离散采样及共享时钟误差见
[[a130-rewrite-cfd-timing-and-clock-boundaries-20261113]]，与能量成形的增益/接受度边界分开使用。
3.2节的体固定负对易、两类惯量简并与近软模有效性条件，见
[[a130-rewrite-wobbling-local-limits-20261113]]；其中高K进动采用
[[shimizu-2005-high-k-precession]]的实际归档预印本，区分共转系与实验室系比较。
联合活时间的参考测度、条件独立教学模型和到达采样边界，见
[[a130-rewrite-joint-live-and-arrival-sampling-20261113]]与
[[wolff-1982-poisson-arrivals-see-time-averages]]，不能把时间busy占比直接当任意符合事件的损失率。
弱算符的多体关联与两体流问题，定向回到
[[gysbers-2019-ab-initio-beta-decay-quenching]]、
[[wang-2026-axial-coupling-quenching-joint-effects]]及
[[a130-rewrite-axial-operator-scope-20261113]]的实际选读范围；
这两项采用不同的结构与算符实现，Wang2026当前仅按已取得v1预印本使用。
第四章的二态E0、相位、数据方向与跨区输入条件见
[[a130-rewrite-cross-region-comparison-and-e0-constraints-20261113]]；
形状共存的解释须保留构型假设，不能把一个寿命或能比当完整势面的直接测量。
模板需先逐文件备份并验证哈希，再可恢复清理示例；未知作者、导师、装置及个人成果不填写。

完整五章39节及附录目标继续有效。工程编译成功、迁移完成或worker返回
都不能代替科学验收和全稿完成。
本轮执行蓝图在`outputs/plans/20261113-A130-latex-execution.json`；
验收与派发回执在`outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/`。

开放网络的条件归一化、初始复合核与蒸发后进入态标签，以及有限时间接受度的解析核查，见[[a130-rewrite-open-network-and-entry-ensemble-20261113]]。
