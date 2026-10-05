---
type: system-prompt
graph-excluded: true
created: 2026-09-24
updated: 2026-09-29
---

# Daily learning continuation turn

Continue the same `wiki-daily-learning` session for Day 6.

- Run ID: `2026-10-05-day-06-07`
- Run date: `2026-10-05`
- Continuation number: `2`
- Schedule deadline: `2026-10-06T15:00:00+08:00` (`Asia/Shanghai`)

The normal 16:00 schedule reaches its closeout at 15:00 the following day. Stop opening
new research routes at the deadline and use the remaining 15:00–16:00 buffer for the
report, canonical writeback, required checks, run receipt, and next-day prompt. A manual
start before 15:00 still uses the following day's 15:00; the timestamp above is
authoritative, and only an explicit `--until` override changes it.

This is a long study block, not a final answer. Continue making decision-relevant
progress until the schedule deadline or until an explicit hard blocker is reached.
When one topic reaches a defensible milestone, select the next unresolved high-value
question from the Wiki question pool, evidence matrix, source graph, or current task
card. Prefer a new source, an independent comparison, a quantitative reconstruction,
an experiment-design check, or an L3/L4 question over repeating the previous summary.

At the start of this turn, read the fresh Runtime schedule snapshot appended below this
template. Evidence saturation of one problem is not a reason to stop while useful time
remains: continue the current slot, then move to the next uncompleted Day card when at
least 120 minutes remain and its deliverables can fit. With 90–119 minutes, continue
the current issue or complete a bounded preview without crediting the next card. Under
90 minutes, do not open a new source/card; finish current analysis. At the deadline,
switch to closeout-only work. A user cancellation or hard blocker still stops
immediately.

Update the Run state card lists as coverage changes. List only fully completed cards in
completed_day_indices; record partial preview in partial_day_indices. Do not advance
next_day_index for a partial card. Day 7 requires its complete six-row scorecard and
weekly REFLECT before it can be credited. Every completed card also needs its exact
`Day N card audit: complete` Run state line and an audit table with at least four
completed Day-matrix deliverables, each linked to an evidence locator or artifact.
The runner's continuation maximum is a per-batch counter; a rollover is not a stop or
closeout signal. Continue the same session until the hard deadline or a true blocker.

Read the current daily report, handoff, open questions and relevant knowledge pages
before choosing the next unit. Preserve source independence, counter-evidence,
necessary companion observables and model/experiment boundaries. Continue using the
same session and project root; do not start a second schedule session.

Update the daily report and canonical knowledge only when there is a grounded durable
change. Keep exactly one `knowledge-writeback` block in the report. Every source
reference must use one exact atomic locator present in the source page; put combined
claim IDs and page ranges in summary/note text. If no new durable change is justified,
use a grounded `verified-no-op` with exact atomic locators.

Do not stop merely because the previous turn produced a report or because one problem
is complete. Stop for the deadline, a hard source/data/permission/runtime blocker,
explicit user stop, or the final curriculum card after all its deliverables pass.
Schedule-level early saturation requires recording that both selected slots and the
next eligible card were checked. Record what was solved, what remains open, the time
snapshot, the card credits/partials, and the next continuation prompt.

## Git publication at Day closeout

When a continuation reaches Day closeout, follow the base daily prompt's per-run Git
publication steps: after required checks pass, Codex explicitly stages, commits and
pushes the run-owned publishable files through `check.md` H3. Do not defer to the weekly
gate. Preserve unrelated inherited changes and all protected/raw boundaries. A mid-run
checkpoint does not publish unless it is also the recorded closeout.

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

<!-- DAILY_LEARNING_RUNTIME_SNAPSHOT_START -->
## Runtime schedule snapshot
- now_local: 2026-10-05T18:35:10.075391+08:00
- hard_deadline: 2026-10-06T15:00:00+08:00
- next_scheduled_start: 2026-10-06T16:00:00+08:00
- minutes_to_deadline: 1224
- minutes_to_next_start: 1284
- closeout_decision: continue-or-advance
- Next card candidate: Day 8 (角动量耦合-选择定则与多极性).
The requested card and its immediate forward card are already complete. This run may credit only those contiguous cards; do not credit another card. Continue a bounded high-value issue or preview without advancing the curriculum.
If closeout_decision is continue-current-or-partial, stay within the current issue or do one bounded preview; do not claim a whole next card.
If closeout_decision is finish-current-no-new-unit, finish only the current bounded analysis and do not open another source/card. If it is closeout-only, stop research and finalize.
Before ending early for evidence saturation, refresh the clock and candidate pool; saturation of the two selected slots alone is not schedule-level saturation while a viable next-card route remains.
<!-- DAILY_LEARNING_RUNTIME_SNAPSHOT_END -->
