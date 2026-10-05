# 时间感知的每日学习收束与前移计划

**状态:** 方案，尚未实施
**目标:** 防止每日学习在研究窗口仍有充足余量时，以局部 evidence saturation 提前结束；在不重复计数、不丢失 Day 卡进度的前提下，继续当前问题或完整前移下一张任务卡。
**规格来源:** 用户 2026-10-05 指令；system/prompts/daily-learning.md；system/prompts/daily-learning-continuation.md；system/workflows/continuous-learning.md；system/workflows/scheduled-continuation.md；system/scripts/run_daily_learning.py；system/scripts/run_daily_learning_daemon.py。
**约束:** 时区 Asia/Shanghai；研究截止仍以回执 overnight_until 为准；15:00 停止新增来源，15:00–16:00 做关闭工作；不改 PLAN.md/raw/credentials；不改 GUI/Docker 外调度；保持知识证据与 needs_review 边界。
**本计划不改代码或学习状态。**

## 现状与问题证据

- 当前 prompt 和 continuous-learning workflow 已要求 runner 在同一 session 中续跑到截止时间，并将 15:00–16:00 留给日报、写回和验证。
- run_daily_learning.py 已有按 overnight_until 循环调用 resume 的机制；但 continuation 模板允许以“证据确实饱和”提前收束，没有明确要求先核对剩余时间、继续当前问题或前移下一天任务。
- 若原 runner/session 中断后由用户直接恢复 Codex session，父 runner 的时间循环不再运行；恢复后的手动回合需要独立执行相同的时间门。
- 按用户校正的口径，Day 6 在 10 月 5 日 02:00 左右启动，原定 10 月 6 日 15:00 收束，约 37 小时；下次 schedule 为 10 月 6 日 16:00，约 38 小时后。
- 回执精确记录 02:04:39 启动、overnight_until=10 月 6 日 15:00，启动至截止约 36 小时 55 分；同一 session 实际 03:56:32 提前完成，距截止仍约 35 小时 03 分。scheduler 的 last_scheduled_date=2026-10-05，因此 next_due 是 10 月 6 日 16:00。计划统一以 receipt deadline 和 scheduler last_scheduled_date/next_due 为准，不从 run_date 猜算。
- 计划编写时刻为 10 月 5 日约 14:56；距离原 run deadline 约 24 小时，距离下次 schedule 约 25 小时。DAY6 已是 completed/published；本方案不回开或改计 DAY6，适用于后续 scheduled-learning run。
- DAY6 实际完成 03:56 时，距回执 deadline（次日15:00）约35小时；离 daemon 的下一次 10月6日16:00 触发约36小时。规划时的当前时间约为10月5日14:56，距该 deadline 约24小时、距下一次 schedule 约25小时。receipt 已 completed/published；本方案只适用于后续运行，不回开或改计 DAY6。

## 推荐策略

### 收束状态机

| 状态 | 进入条件 | 动作 | Day 计数 |
|---|---|---|---|
| 继续当前问题 | 尚未达到 hard deadline，距 deadline ≥90 分钟，当前两个问题仍有可改变判断的来源、比较或定量任务 | 保持当前连续性/新颖性槽位，完成下一项高信息增益工作；刷新时间快照 | 不提前关闭 |
| 前移下一任务卡 | 当前槽位已分别核查至证据饱和，距 deadline ≥120 分钟，且下一张卡可以在余量内完成全部交付 | 在同一 session 执行下一张卡；日报明确分开列出各卡交付与 locator | 仅完整通过该卡自身验收后计入 |
| 部分预学 | 距 deadline 为90–119分钟，当前槽位已饱和；下一卡可拆出一个边界清楚的短练习，但无法完成全卡 | 做单个练习并记录具体完成/未完成项；不生成该卡完成信用 | 不递增 next_day_index |
| 仅做收束 | 距 deadline <90分钟；或已经到 15:00；或剩余时段不足以完成可验证的实质单元 | 停止开启来源；整理报告、知识写回、lint/diff、回执和下一提示 | 按已完整通过的卡计数 |
| 硬停止 | 用户取消、session/runtime/权限硬故障、真实数据授权关口 | 停止研究，保留 interrupted/blocked 原因和 resume 信息；不伪造成功 | 不计未完成卡 |

90 分钟是启动一个有边界的同题研究单元的最低建议值；前移一张完整 Day 卡建议至少预留 2 小时。卡片本身若有更长阅读/验收要求，以预计工作量为准，不因达到固定阈值而承诺完成。15:00 是新增研究的硬截止；即使下一次 schedule 尚有很长时间，15:00 之后也只做 15:00–16:00 的关闭工作。

### 选择次序与课程进度

1. 在当前槽位内继续最有信息增益的来源、cross-check、定量练习或设计核查；不因日报已经成形而结束。
2. 连续性和新颖性两个槽位都饱和后，检查下一张未完成 Day 卡；若时间足够，则前移该卡。
3. 只有该卡的回忆/主线/练习/反证/交付全部完成，才记录为已完成卡。部分预学只记录覆盖项，不增加课程信用。
4. run.json 增加 completed_day_indices、partial_day_indices、curriculum_cards_completed、closeout_decision 和每次时间快照。counted_in_substantive_test 保持布尔兼容（本 run 至少完整完成一张卡时为 true）；计数明细用 curriculum_cards_completed。state 文件 next_day_index 始终指向第一张未完整通过的卡；例如 Day 6 与 Day 7 均完整通过则变为 8，Day 7 只有部分预学则仍为 7。计数口径改为30张完整 curriculum cards；一次 runner run 可贡献多张，但不能重复或跳卡。
5. 报告的 Run state 增列本次覆盖卡片。完整前移 Day 7 时，在同一日报中包含 Day 7 口试评分表和 weekly REFLECT；不通过输出标题或报告日期冒充另一轮 runner。下一 prompt 由更新后的 next_day_index 生成。
6. 单次 runner 仍以一个 session 为单位；30 天计数以完整通过的 curriculum card 为单位，而不是运行次数。手动停止和 runner 缺席时不得把“早停”自动转成完整日。

### 当前时间快照

每次模型准备写入 early-closeout/verified-no-op/evidence-saturated 时，取 Asia/Shanghai 当前时间并记录：

- receipt 中的 overnight_until；
- scheduler 根据 last_scheduled_date 计算的 next_scheduled_start；
- minutes_to_deadline 和 minutes_to_next_start；
- 当前 closeout_decision 及理由；
- 若 runner 已不在运行，记录 parent runner 状态并仍执行相同的续学/前移判断。

next_scheduled_start 仅用于展示实际空档；是否启动新研究主要看 hard deadline 前剩余的可用时间。不得把“距离下次启动 >1 小时”直接当作可在截止之后继续研究的授权。

## 文件结构与职责

- system/prompts/daily-learning.md：定义 early-closeout 时间门、当前问题继续和下一卡前移规则。
- system/prompts/daily-learning-continuation.md：每轮续接携带 now、hard deadline、剩余分钟、下一 schedule 时间、已完成/部分完成卡和下一步决策。
- system/workflows/continuous-learning.md：定义 evidence saturation 的运行级含义及15:00/15:00–16:00边界。
- system/workflows/scheduled-continuation.md：定义父 runner 缺席或手动 resume 时继续使用同一时间门，不把 resume 直接视为 day closeout。
- system/scripts/run_daily_learning.py：新增纯时间快照/决策 helper；防止 max_continuations 在 deadline 之前被误当作成功终点；写入 covered/partial card 元数据；从 state 的第一张未完成卡生成 next prompt。
- system/tests/test_daily_learning_runner.py：覆盖阈值、时间区、计数和截止状态转换。
- system/scripts/README.md 与 USER_GUIDE_DETAIL.md：解释早停规则和 receipt 字段。
- USER_GUIDE.md：将当前 schedule 时间说明与实际 16:00 trigger 对齐（当前行仍写 22:00）。
- check.md：增加 closeout gate 与多卡计数的发布/验收检查。
- outputs/learning-milestones/2026-09-one-month-state.json：只在 runner 完整验收后由 runner 原子更新；运行前状态不作为计划阶段修改目标。

不修改 system/scripts/run_daily_learning_daemon.py 的触发时间：daemon 仍负责 16:00 启动；state 的 next_day_index 决定加载哪张卡。若实现发现 daemon 的 last_scheduled_date 与 forward-credit state 有冲突，再由对应测试约束，不提前重构 daemon。

## 实施任务

### Task 1：定义并测试时间快照/决策函数

**文件:** 修改 system/scripts/run_daily_learning.py；修改 system/tests/test_daily_learning_runner.py。
**接口产出:** 纯函数接受 timezone-aware now、hard_deadline、next_scheduled_start、minimum_current_block=90分钟、minimum_full_card_block=120分钟，返回 decision、剩余分钟和 closeout reason。函数不读取全局时钟、不写文件。

新增测试：

- test_closeout_gate_continues_at_0400_with_eleven_hours_remaining：正常 16:00 开始、次日 04:00 检查，输出 continue-current 或 advance-next，不能输出 completed/closeout。
- test_closeout_gate_uses_actual_deadline_for_manual_run：receipt deadline 与 run_date 不一致时以 overnight_until 为准。
- test_closeout_gate_enters_closeout_below_minimum_block：距 deadline 89 分钟时不开新卡；当前问题可做有限收尾。
- test_closeout_gate_stops_new_research_at_deadline：now 等于或晚于 deadline 时只允许 closeout。
- test_closeout_gate_reports_gap_to_next_schedule：同时输出 deadline 余量和 daemon next_due，不能把两者混成一个时间。
- test_continuation_limit_before_deadline_does_not_advance_state：达到 96 续接上限但仍有实质窗口时，receipt 标记 continuation-limit-reached，next_day_index 不前进。

### Task 2：把时间门写进 scheduled 与 manual continuation

**文件:** 修改 system/prompts/daily-learning.md、system/prompts/daily-learning-continuation.md、system/workflows/continuous-learning.md、system/workflows/scheduled-continuation.md。

- 在初始 prompt 和每个 continuation 中注入 runner 计算的当前时间/剩余分钟/决策建议；模型仍需重新核对快照年龄，过期则重算。
- 将“证据饱和”从单问题停止理由收窄为候选局部状态：槽位饱和后，只要 runway 达标，继续当前主题的高信息增益检查或按状态机前移下一卡。
- 明确 manual resume 在 runner_terminal_event_missing 时也执行时间门；父 runner 消失不是学习窗口自动结束的理由。
- 明确用户 stop、hard blocker、15:00 hard deadline 的优先级。
- 保留两槽候选限制；前移下一张课程卡不变成第三个科学问题。
- 15:00 后不启动新 source/problem；15:00–16:00 只做 closeout。

### Task 3：增加多卡完成/部分预学的状态对账

**文件:** 修改 system/scripts/run_daily_learning.py；修改 system/tests/test_daily_learning_runner.py。

- 在报告 Run state 读取 completed_day_indices 与 partial_day_indices，并写入 run.json；只在所有列出的卡片验收通过后设置其完成信用。
- 只允许从当前 next_day_index 开始连续计卡，不允许跳过中间卡。
- runner 对每张前移卡检查 daily-task-matrix 的交付契约；Day 7 必须包含六项 0–4 口试评分和 weekly REFLECT，才能进入 completed_day_indices。
- state.next_day_index 设为首张未完成卡，并同步 counting_policy/card count；next prompt 使用该值，不固定使用 initial_day_index+1。
- 完整 Day 6+Day 7 应生成 state.next_day_index=8、Day 8 prompt；Day 7 partial 应保持 next_day_index=7，并把已完成练习/待完成交付写入 handoff/resume prompt。
- 兼容旧 state 文件：缺少新字段时从现有 next_day_index 解释为此前所有卡顺序完成，不回写或重算历史 run。

新增测试：

- test_completed_cards_advance_to_first_unfinished_card：连续卡6、7完成后 next=8。
- test_partial_forward_card_does_not_advance_credit：卡7 partial 时 next=7。
- test_forward_credit_rejects_skipped_day_index：6、8 不得跳过7。
- test_next_prompt_uses_state_after_forward_credit：完成卡7后准备 Day8 prompt。
- test_day7_credit_requires_scorecard_and_weekly_reflect：缺任一交付时不得给卡7 credit。

### Task 4：同步文档与端到端验收

**文件:** 修改 system/scripts/README.md、USER_GUIDE_DETAIL.md、USER_GUIDE.md、check.md；按需要更新 daily report 验收逻辑。

验收场景：

- Case A：window deadline 次日15:00，当前时间04:00，下一次 schedule 16:00。receipt 显示剩余11小时，runner继续当前问题或前移下一卡，不生成成功终态。
- Case B：当前14:00、hard deadline15:00。只允许当前问题短时收尾；不打开新 source/卡片。
- Case C：当前15:00。停止新增研究并进入closeout。
- Case D：父 runner缺失但原session可恢复。手动resume依据原receipt deadline继续，不丢失日卡/知识写回/来源状态。
- Case E：用户明确stop。立即中断、不计未完成卡、不由时间门自动重启。
- Case F：达到max_continuations而deadline未到。保持可恢复的未完成状态，不伪报day完成。
- 验收后通过 boundary、Wiki lint、report/writeback validation、git diff checks；只显式暂存本轮文件，按 Gitee H3 发布门提交。

## 通过标准

1. evidence saturation 不再单独导致有充足 runway 的 run 提前记为 completed。
2. 每个 continuation 都能看到准确 Asia/Shanghai 当前时间、deadline 和 next scheduled start。
3. 90 分钟用于同题 bounded continuation，120 分钟用于申请完整前移卡；若时间不足则保留 partial，不计下一卡。
4. next_day_index 总指向第一张未完整通过的卡，report、run.json、scheduler event 和下一 prompt 一致。
5. 用户 stop 与 hard deadline 边界不被自动延长；15:00–16:00 不启动新研究。
6. Day6 回执的手动恢复路径与正常 runner 使用同一 closeout gate。

## 本次实际执行状态

本轮仅读取 prompt/workflow/runner/测试/状态文件并形成方案；未修改科学内容、scheduler、里程碑或 runner 代码。当前 DAY6 已是 completed/published，计划只适用于后续 scheduled-learning run。
