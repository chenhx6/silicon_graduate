---
type: system-prompt
graph-excluded: true
created: 2026-10-21
updated: 2026-10-21
---

# Day20正式独立课程准备：B(E2)、Q_t 与形变系统学

本文件只是准备入口，不启动session/调度、不授学分。预计2026-10-22 16:00上海由既有Docker-local wiki-daily-learning runner新开独立session；研究硬截止预期2026-10-23 15:00上海、15–16收束，实际identity/deadline只认runner新原始receipt。不得自行创建daemon/GUI Scheduled或凭准备文本创造executionmetadata。

先按rootAGENTS读取startup、profile/activehandoff/PLAN、continuous-learning/autonomous与三份课程计划、最近日报；跑boundary，冻结dirtybaseline与带本sessiontime/session/hash的primed主动回忆，再开source/raw。按matrix唯一Day20卡执行；本session只授正式20，任何Day19知识preview/旧scripts不能兑换本session独立交付。保留旧review/needs_review，不设human-reviewed；保护raw/PLAN/Bib/继承dirty/credentials。

主线：transition-quadrupole-moment、petrache-1998-highly-deformed-lifetimes-131ce-nd、singh-2016-lifetime-131ce-133pr；原件fullmainline/关键fig/table/equation/levelscheme/uncertainty和actualreadscope如实核。交付lifetime/strength/deformation证据图与模型依赖分析，区分测量寿命、转子矩阵元、K量子数投影、分支比与微观形变参数（beta2, gamma）的转换链条；至少一项本session新quant/design exercise、counterinput/companion/同data边界，缺input写readiness不造fitCI。

Day19原run/session已完成RDDS、fast timing与时间响应全景分析：rdds-timing-response-result.json涵盖常规与逆运动学3.19倍空间拉伸、真空退取向两分量条件平均G_SH/G_US渐近极限（0.555 vs 0.180）、快速定时MSCD能量走时对消及DSAM vs RDDS系统误差交叉分水岭（tau_cross = 0.65–0.74 ps）。Day20将承接该寿命基础，深入探究从寿命tau到B(E2)与Qt的转子几何转换，以及从Qt到微观形变的内禀模型依赖。

本日输出按runner实际report/run-dir/statefile；日报有固定Runstate等十标题、唯一knowledge-writeback（exactanchor/每atomiclocator一reference）和>=4complete行的Day20cardaudit，formalcompleted[20]；若时间门允许只下一卡无学分preview，不跨更多课卡、不提早终止有用窗口。研究15点停止新路，收束完成report/canonicalknowledge/checks/continuation/nextprompt/actualsessionreceipt/发布后才推进一次学分。普通发布沿Gitee origin精确manifest/H3/fetch/ancestry/dry-run/nonforce HEAD:main；实际hash只receipt，不写本commit自身hash。科学partial不阻普通安全发布，failedrequiredcheck或未隔离hardP0则留本地如实。

<!-- DAILY_LEARNING_CURRICULUM_COVERAGE_V1 -->
## Curriculum card completion record
In the report's Run state include exactly these two machine-readable list lines:
- completed_day_indices: [N, ...]
- partial_day_indices: [N, ...]
Count a card only after every deliverable on that Day card is complete. For every completed day, add `- Day N card audit: complete` under Run state and a `### Day N card completion audit` table with at least four Day-matrix deliverables, each linked to an evidence locator/artifact and marked complete. Partial previews go only in partial_day_indices. List cards contiguously from the requested day; at most one next-day card may be advanced in one run.

<!-- DAILY_LEARNING_TIME_GATE_V1 -->
## 时间判断与学习收束
候选问题或来源达到局部证据饱和时，先读取最新 Runtime schedule snapshot；手动恢复且没有新快照时，调用当前时间工具，并按 Asia/Shanghai 与回执中的 overnight_until 比较。
距离硬截止至少 120 分钟：继续当前高信息问题；若当前选定问题已饱和，检查下一张未完成日卡，只有其全部交付项能在剩余时段完成时才整卡前移。
距离硬截止 90–119 分钟：继续当前问题或做有边界的预览，不给下一日卡完整学分。少于 90 分钟：不打开新来源或新卡，只完成当前分析。硬截止后停止研究，用 15:00–16:00 收束。
不能仅因两个候选槽位饱和而提前结束；须重建候选池、检查下一张可行日卡，并记录时间快照和决定。用户明确停止、硬证据/数据/权限阻塞或运行故障可提前结束，但必须保留未完成状态和续接命令。
每次调用生成的新 Runtime snapshot 优先于本文件中的旧快照。课程学分只沿连续完整日卡推进；部分预览不得推进 next_day_index。

<!-- DAILY_LEARNING_RUNTIME_SNAPSHOT_START -->
## Runtime schedule snapshot
- now_local: 2026-10-21T18:25:00+08:00
- hard_deadline: 2026-10-23T15:00:00+08:00
- next_scheduled_start: 2026-10-22T16:00:00+08:00
- minutes_to_deadline: 2675
- minutes_to_next_start: 1295
- closeout_decision: continue-or-advance
- Next card candidate: Day 20 (B(E2)-Qt与形变系统学).
<!-- DAILY_LEARNING_RUNTIME_SNAPSHOT_END -->
