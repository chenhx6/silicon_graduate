---
type: output
graph-excluded: true
created: 2026-11-07
updated: 2026-11-07
---

# 同核异能态原件学习与六大质量区机制研究

## 授权与目标

用户于2026-11-07要求摄入 `raw/papers/isomer/`，重点研读综述和学位论文，
深化六大质量区比较、物理迁移及新现象候选，明确允许L3/L4。
本轮不以此前“Master级综合已完成”的标签作为科学结论成立的证据。

验收依据：

1. 建立所给目录的逐文件身份、版本、哈希及真实阅读范围台账；副本和附件不重复计证。
2. 综述建立可追溯source；学位论文回到刘晨、肖骁等本地原件，核对核心机制和实验判据。
3. 修订三篇主综合及直接相关的普适迁移综合，六区分别保留具体核素、来源、
   迁移成立条件、失效条件、尚未搜索/尚未发现/存在反证的区别。
4. 检索新的高信息增益原始研究，下载前本地预查，原件合法获取并留档；
   元数据/摘要/正文/补充材料分别记录，不冒称取得全文。
5. 提出可证伪候选，给出竞争解释、必要伴随信号、可区分观测和停止条件；
   有可靠数值问题时完成有界L4模型检验，模拟结果不冒充实验或发现。
6. 自审来源、locator、依赖、公式和措辞，运行lint/boundary/archive/preflight，
   按显式文件清单commit/push，并记录剩余科学缺口。

## 模型与写入分工

| 工作单元 | 模型/effort | 独占写入范围 |
|---|---|---|
| 总控、两篇学位论文、主综合及集成 | Sol/xhigh | 四篇既有综合、关联学位论文source、项目、index/questions、handoff/log及本计划 |
| R1 异能态综述与Jain专著 | Gemini Flash Tiered/high | 四个新综述source、Jain既有source、独立review研究笔记 |
| R2 核耗散与NEEC | Gemini Flash Tiered/high | 该目录的新source、独立depletion研究笔记 |
| R3 核钟与精密测量 | Gemini Flash Tiered/high | 该目录的新source、独立clock研究笔记 |
| R4 天体/壳演化/超重核 | Gemini Flash Tiered/high | 对应新source、独立astro/SHE研究笔记 |
| R5 六区直接证据与反例 | Gemini Flash Tiered/high | 新原始研究source、独立六区比较研究笔记 |
| R6 复杂理论与L4 | Terra/xhigh | 独立seniority研究笔记、专用数值脚本和L4结果 |
| R7–R8 证据反查与Jain逐页阅读 | Gemini Flash Tiered/high | 独立审核回执、Jain原件阅读账及其source |
| R9 旧过程回执对账 | Gemini Flash Tiered/high | astro/clock/six-region过程报告及旧审核记录 |
| R10 候选机制反方审计 | Gemini Flash Tiered/high | 独立候选判别研究笔记及审计JSON |
| R11 四篇综述的真实阅读覆盖 | Gemini Flash Tiered/high | 四篇综述source及独立块级阅读账 |
| R12 A100寿命全文补证 | Gemini Flash Tiered/high | 两篇100Ru原文的新source、获取清单和阅读回执 |

所有worker禁止继续派生代理或执行Git变更。既有综述和实验来源仅由唯一指定写者修改。
原有raw文件只读；新下载进入对应 `raw/papers/gpt/query/20261107-*/`，
带URL、大小、SHA-256、实际时间及候选主题的manifest。
本轮不修改用户PLAN、不改调度器、不将既有博士论文重构扩大为新写作任务。

## 研究循环与收束

采用 `all` 编排，`dispatch` 拆域，`local-literature-archive` 本地预查，
`nature-academic-search` 的multi-source-search及 `get-paper` 检索，
`research-archive` 留档。最多五轮针对实质缺口的研究—反证—自审；
首轮建立原件事实，后续只对会改变解释排序的问题补证。
不把文件数量、提取全文、source数量或模型标签当作学习完成率。
存在不可得原件或不能唯一归属的证据时保留具体边界和可续接路线。

本任务属于用户主动研究，不冒充daily-learning课程学分，不改变课程状态。
本计划只保存执行合同；可复用科学结论、证据矩阵和研究设计必须进入knowledge。

## 续接执行合同

用户补充调用`auto / go-on / brainstorm / optim / all`，继承已有授权和进度。
auto负责无人值守收束，go-on恢复既有产物及运行中的worker，
brainstorm用于C1–C4的有界可行性探针，all以原有六项验收标准编排。
不重新请求已给出的L3/L4、检索或普通Git发布授权。
原生goal工具已查得无活动目标；本轮没有另外显式请求创建goal，
因此继续使用本计划与项目页跟踪，不将工具查询写成goal已启用。

优化只处理观察到的瓶颈，不修改科学判据或扩张成系统维护：
已实测全库lint约103秒，避免边读边重复全量执行；
不相干的报告/原文阅读由独占写入范围的Gemini并行推进。
没有等价的优化前后计时，不报告百分比性能提升。
单j数值重放用单BLAS线程，20行结果与留档结果逐值比较；
单j模型及独立Wigner检查不等于独立的真实核计算。

本轮收束以范围内身份、原件/哈希、科学强断言、可检验候选、
结构增量、归档和Git发布门为准；既有全库lint缺陷作基线隔离，
不能将全库非零退出码宣称为全绿。
继续发现会改变候选排序的新原文时可补证；
仍未取得的数据明确列出，不把开放科学问题自动转成用户审批事项。
