---
type: system-prompt
graph-excluded: true
created: 2026-10-08
updated: 2026-10-08
---

# DAY9 — B(E2)、B(M1)、约化矩阵元与强度比

## Run context

- run_id: 2026-10-08-day-09-01
- run_date: 2026-10-08
- day_index: 9
- timezone: Asia/Shanghai
- schedule_id: wiki-daily-learning
- expected_start: 2026-10-08T16:00:00+08:00
- overnight_until: 2026-10-09T15:00:00+08:00
- output_dir: /workspace/wiki/outputs/learning-daily/20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01
- report_file: /workspace/wiki/outputs/learning-daily/20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths.md
- state_file: /workspace/wiki/outputs/learning-milestones/2026-09-one-month-state.json

RUN_ID/OUTPUT_DIR占位由正常runner绑定到实际run；不得把prompt seed当真实session ID。每次正式调用创建新的Codex session，run receipt保存session_id和可复制resume_command，不复用Day8 session。最新Runtime snapshot的时刻/剩余分钟优先于旧静态时间；snapshot中的通用advance/complete-next-card措辞不授予Day10学分，课程不变量是onlyDay9credit/Day10partial。

## 正式卡与预习边界

Day8 session已预习本题知识和有条件算术，但仅Day8计卡。正式Day9必须重新建立自己的recall/evidence record、输入链练习、反证和card audit；不继承预习为已完成。先读Day8日报或知识页后回忆，应标primed recall；已有记忆也不冒称blind。

在/workspace/wiki依次读README、knowledge/index、profile/activehandoff、PLAN、Day8日报、[本计划](/workspace/wiki/outputs/plans/2026-10-08-DAY9-be2-bm1-reduced-matrix-elements-strengths.md)、daily-task-matrix的Day9卡和autonomous-research/continuous-learning workflows。写前boundary与gitstatus；保留继承dirty文件、raw、PLAN、review flags。课程state只通过normalrunner/state contract推进，不设置human-reviewed或清除needs_review。

## Day9 card

1. 回忆：查Day9来源正文前，独立说明partial lifetime、branching、mixing fractions与B/RME的关系，写mean lifetime/half-life和单位区别；标明priming，之后核对差异。
2. 主线：读knowledge/synthesis/high-spin-lifetime-strength-deformation.md与knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md。率/核算符归一回到LKH82 p.121 Eqs.2.2–2.3；表格回到MU08 printed034311-3/TableI与034311-4/TableII。
3. 练习：选MU08 Band1 I18、Ex6711.4组，独立核原表三枝401.2/757.4/389.6-keV及tau0.56(8)ps，重算一条有条件B(E2)或B(M1)输入链，逐项列数值、单位、分支basis、radiativefractions、IC/E0和误差。不能从quotedB倒推alpha/delta/covariance再验证自己。
4. 反证：检查漏枝、feeding、stopping、IC、branch uncertainty以及同数据派生输出的依赖。未知branch定义保留至少两种forward解释；15%stopping不自动作独立1sigma或跨带共模。精确归一化/quotedSD的不相容只排除额外joint解释，不判作者错误。
5. 交付：一页输入—公式—输出—误差表；每个判断回source locator，不能把视觉强度当B。绝对B、RME、reverseB、Qt或same-parentratio若共享输入，不重复计独立证据。

## 来源与候选优先级

- 第一优先是branch/lifetime/ICC/单位/不确定度闭合；先用已有source与immutableDay8 receipts核实，而非增加无关核素或文献数量。
- MU08 p.3说提取过程参照Chiara etal.[16]；p.6列C.J.Chiara etal.,Phys.Rev.C64,054314(2001)。若定义缺口仍改变判断，可在正式Day9验证该候选身份/合法全文再精读；当前未给其题名/DOI或方法作为事实。
- 现代BrIcc FO/NH inputs只是条件理论输入，不能证明MU08实际采用哪种处理；N6/shellcoverage、atomicradius、penetration/current域与模型相关性保留。
- 独立事件、line-shape、response、stopping/feeding代码与covariance缺失时不计L4；本日前述预习只L2。可靠模拟也不能冒充实验事实。

## 时间与课程

保持day_index=9。>=120分钟继续高信息当前题；局部饱和后重建候选池，只可预习恰好Day10知识，无学分、partial10，不把next_day_index越过10，不打开Day11。90–119分钟有界继续；<90分钟不打开新source/card，finishcurrent；2026-10-09 15:00停止研究，15:00–16:00收束。卡内容完成不单独结束窗口；等待/心跳不计研究时长。

日报使用标准十heading。Runstate只一行completed_day_indices和一行partial_day_indices；只有Day9全部deliverables完成才写completed=[9]与`Day 9 card audit: complete`，有至少4行completionaudit表。Day10只能partial，旧模板任何整卡前移计学分措辞在本运行禁用。Durable知识同步knowledge并保留唯一合法knowledge-writeback JSON，updated须真实改页，否则groundedverified-no-op。

Closeout执行boundary、wiki_lint --fail-on error、gitdiff --check及originalbaseline report/writeback/card验证；显式stage本runownedmanifest。Gitee freshfetch→ancestor→HEAD:main dryrun→同refspec非forcepush/H3。正常runner state最多credit9，生成下一未完成卡plan/prompt；hash仅run receipt，canonical指针branch+subject。

<!-- DAILY_LEARNING_TIME_GATE_V1 -->
## 时间判断与学习收束
候选问题或来源达到局部证据饱和时，先读取最新 Runtime schedule snapshot；手动恢复且没有新快照时，调用当前时间工具，并按 Asia/Shanghai 与回执中的 overnight_until 比较。
距离硬截止至少 120 分钟：继续当前高信息问题；若当前选定问题已饱和，检查下一张未完成日卡，只有其全部交付项能在剩余时段完成时才整卡前移。
距离硬截止 90–119 分钟：继续当前问题或做有边界的预览，不给下一日卡完整学分。少于 90 分钟：不打开新来源或新卡，只完成当前分析。硬截止后停止研究，用 15:00–16:00 收束。
不能仅因两个候选槽位饱和而提前结束；须重建候选池、检查下一张可行日卡，并记录时间快照和决定。用户明确停止、硬证据/数据/权限阻塞或运行故障可提前结束，但必须保留未完成状态和续接命令。
每次调用生成的新 Runtime snapshot 优先于本文件中的旧快照。课程学分只沿连续完整日卡推进；部分预览不得推进 next_day_index。

<!-- DAILY_LEARNING_CURRICULUM_COVERAGE_V1 -->
## Curriculum card completion record
In the report's Run state include exactly these two machine-readable list lines:
- completed_day_indices: [N, ...]
- partial_day_indices: [N, ...]
Count a card only after every deliverable on that Day card is complete. For every completed day, add `- Day N card audit: complete` under Run state and a `### Day N card completion audit` table with at least four Day-matrix deliverables, each linked to an evidence locator/artifact and marked complete. Partial previews go only in partial_day_indices. List cards contiguously from the requested day; at most one next-day card may be advanced in one run.
For a completed Day 7 card also include these exact audit lines:
- Day 7 scorecard: complete
- Day 7 weekly REFLECT: complete

<!-- DAILY_LEARNING_RUNTIME_SNAPSHOT_START -->
## Runtime schedule snapshot
- now_local: 2026-10-08T16:00:01.836897+08:00
- hard_deadline: 2026-10-09T15:00:00+08:00
- next_scheduled_start: 2026-10-09T16:00:00+08:00
- minutes_to_deadline: 1379
- minutes_to_next_start: 1439
- closeout_decision: continue-or-advance
- Next card candidate: Day 9 (B(E2)-B(M1)-约化矩阵元与强度比).
If closeout_decision is continue-or-advance, continue the current high-value issue; if both selected slots are saturated, inspect the next card and complete it only if its full deliverable fits the window.
If closeout_decision is continue-current-or-partial, stay within the current issue or do one bounded preview; do not claim a whole next card.
If closeout_decision is finish-current-no-new-unit, finish only the current bounded analysis and do not open another source/card. If it is closeout-only, stop research and finalize.
Before ending early for evidence saturation, refresh the clock and candidate pool; saturation of the two selected slots alone is not schedule-level saturation while a viable next-card route remains.
<!-- DAILY_LEARNING_RUNTIME_SNAPSHOT_END -->
