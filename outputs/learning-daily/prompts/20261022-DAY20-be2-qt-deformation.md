---
type: system-prompt
graph-excluded: true
created: 2026-10-21
updated: 2026-10-22
---

# Day20准备入口：B(E2)、Qt与形变系统学

这是准备文本，不开session/调度、不授学分；启动identity/deadline只认既有runner的新原始receipt。先核Day19是否真正完成并通过逐卡门；尚未完成不得越过19。

按AGENTS与课程matrix启动，source前冻结primed回忆。主线为transition-quadrupole-moment、Petrache1998和Singh2016原件；交付加权趋势、反证与lifetime/strength/deformation证据图。保原review/flags、raw/PLAN/Bib与继承dirty。

Day19 checkpoint008纠错优先：旧截短CG、K=5/2完全闭合、零Qs唯一γ30指纹、低z证伪下降、15%误差覆盖原趋势与feeding方向均已撤回。旧打印式脚本/JSON不作科学验证。正确CG/原表与条件反例见day19_evidence_repair_audit.py；仍不识别作者真实K/producer或给实验CI。现代fast-timing/TDPAD旧hash不等本session完整原读。

只正式计本日完整卡；若时间允许最多恰好下一卡无学分preview，不开Day+2。原run次日15点研究停止，15–16收束；report十标题/唯一writeback/精确atomiclocator、实际sessionreceipt、卡审计、requiredchecks与H3全过后才推进。中途不发布，原deadline不能因checkpoint缩短。最终time gate只认本次实际runner snapshot，不从此准备文本伪造。

checkpoint088优先：079–087科学认证已撤回，019–078待逐claim重审，见Day19的rejected-analysis-registry-088.json及canonical source更正。Nolan Table7是RDM/DSAM；Table5 adopted480fs与Lees710fs不可混；Radeck beta=.0450和真实六环，K16共13态。136Pr N=77终止、128I唯一spin/parent窗界、4ps或15fs普适硬阈值均不延续。25项response控制仅为明示数学设计，不认证原实验CI。仅凭lint/writeback valid不得写“全部科学闭环”。

checkpoint089补充：Suzuki Eq1实际gated I_su/dI_ss，不能泛换成慢分量log slope；103Rh/104Rh两速度/tau身份分开，3.5mg/cm²不是旧自设2um。小Qt比稳定性只在声明的half-chart内，原有限停止/共同Cov未消除。沿原run source/receipt核验，勿把46项数学控制写成原实验精度认证。

checkpoint090补充：Qt平方根缩放与双比值不变只在所有相关态同一total-trajectory重标、固定branch/geometry及相应Cov合同下成立。电子-only变化可有state-dependent响应；共同reference/速度/距离标度的off-diagonal不能以点数平均掉。旧066停止校准/结构免疫认证撤回，58项数学控制不认证actual实验精度。

checkpoint091补充：本Day19实际Radeck全文十页+全部关键图表式scope见source-reading-scope-091.json。TableIII的IBM首B按实验输入归一，高spinB为旧Ref8；新tau使用ring/branch角色不能混。body/table打印B误差差异保literal，原Cov/producer未得，不由全文阅读反造完整fit或新实验。

checkpoint108优先：095–107全部科学认证与过强推论（包括100%全闭合、普适15%手征或20 W.u.摇摆硬阈值、完全无共同系统误差断言）均已正式撤回，26个分析与更新脚本已退役并加SystemExit守卫。Nolan与Régis的全部全文阅读范围（source-reading-scope-092/093/094）保留，严格区分已读文字与未得原数据。

checkpoint109–111补充：快速定时MSCD与方差估计在未知prompt尾部下存在完整时间谱退化（day19_prompt_tail_identifiability109.py）；有限calibrator自身具有方差传递（day19_prompt_calibration_design111.py），等计数规划需视目标寿命与prompt宽度而定，负Q保留不截断；TDPAD实际原读（Ionescu-Bujor 1998全部20页正文与Grodner 2018全部5页正文，source-reading-scope-108/110）确立129Ce未分辨feeding与模型参数（PTR/CDFT）依赖，不冒称为直接电磁矩图像。

checkpoint112–114补充：2015公开GCD原稿scope112保持，raw归档deferred。114修订113：归一化权重相等保证任意pair平移相消；给定平移仅需权重差与平移内积为0，原始权重可成比例。匹配双role的prompt响应可同步抵消alignment影响；113 MC只检Gaussian噪声，未抽样指数等待，勿称完整方差验证。原events/权重/Cov未得，不重造实验CI。以canonical checkpoint114及新result114为准。

<!-- DAILY_LEARNING_CURRICULUM_COVERAGE_V1 -->
## Curriculum card completion record
In the report's Run state include exactly these two machine-readable list lines:
- completed_day_indices: [N, ...]
- partial_day_indices: [N, ...]
Count a card only after every deliverable on that Day card is complete. For every completed day, add `- Day N card audit: complete` under Run state and a `### Day N card completion audit` table with at least four Day-matrix deliverables, each linked to an evidence locator/artifact and marked complete. Partial previews go only in partial_day_indices. List cards contiguously from the requested day; at most one next-day card may be advanced in one run.
For a completed Day 7 card also include these exact audit lines:
- Day 7 scorecard: complete
- Day 7 weekly REFLECT: complete

<!-- DAILY_LEARNING_TIME_GATE_V1 -->
## 时间判断与学习收束
候选问题或来源达到局部证据饱和时，先读取最新 Runtime schedule snapshot；手动恢复且没有新快照时，调用当前时间工具，并按 Asia/Shanghai 与回执中的 overnight_until 比较。
距离硬截止至少 120 分钟：继续当前高信息问题；若当前选定问题已饱和，检查下一张未完成日卡，只有其全部交付项能在剩余时段完成时才整卡前移。
距离硬截止 90–119 分钟：继续当前问题或做有边界的预览，不给下一日卡完整学分。少于 90 分钟：不打开新来源或新卡，只完成当前分析。硬截止后停止研究，用 15:00–16:00 收束。
不能仅因两个候选槽位饱和而提前结束；须重建候选池、检查下一张可行日卡，并记录时间快照和决定。用户明确停止、硬证据/数据/权限阻塞或运行故障可提前结束，但必须保留未完成状态和续接命令。
每次调用生成的新 Runtime snapshot 优先于本文件中的旧快照。课程学分只沿连续完整日卡推进；部分预览不得推进 next_day_index。

Day19正式收束：同session正式19已在原硬截止后按实际内容发布回执115与一次迁移116完成，Day20仍无学分preview。开课先核最新Day19 final-session-receipt-116.json；本prompt不创造Day20 session/执行时间。原件正文未得的Schwalm/Hermans/2010MSCD保持metadata-only；旧generated脚本和passed字段不可作science认证。
