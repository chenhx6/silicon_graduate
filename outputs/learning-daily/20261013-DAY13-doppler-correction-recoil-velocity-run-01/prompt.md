---
type: system-prompt
graph-excluded: true
created: 2026-10-12
updated: 2026-10-12
---

# Day 13 — Doppler correction、反冲与速度信息

## Run context

- `run_id`: `2026-10-13-day-13-01`
- `run_date`: `2026-10-13`
- `timezone`: `Asia/Shanghai`
- `day_index`: `13`
- `day_topic`: Doppler correction、反冲与速度信息
- `phase`: `gamma-spectroscopy-and-level-schemes`
- `schedule_id`: `wiki-daily-learning`
- `schedule_name`: `Wiki 30-day substantive daily learning`
- `project_root`: `/workspace/wiki`
- `hard_deadline`: `2026-10-14T15:00:00+08:00`
- `state_file`: `outputs/learning-milestones/2026-09-one-month-state.json`
- `previous_cards_completed`: `[11, 12]`

本 prompt 只提供下一次运行入口。runner 应按通用 `system/prompts/daily-learning.md` 创建一个新的 Codex session，并严格执行 daily-task-matrix 中匹配 Day 13 的课程卡；本文件不授予 Day 13 学分，不预先写入该卡的科学结论。

## Start requirements

1. 读取 `README.md`、`knowledge/index.md`、`profile.md`、`system/handoff.md` Active handoff、`PLAN.md`、最近学习记录、`system/workflows/continuous-learning.md`、30 天计划、每日任务矩阵和 A≈130 thesis pipeline。
2. 核对 `outputs/learning-milestones/2026-09-one-month-state.json` 为 `next_day_index: 13` 后再执行 Day 13 卡；若状态/矩阵不一致，记录并安全暂停，不自行改日序。
3. 写入知识前运行 `python3 system/scripts/wiki_boundary_check.py --root .`，保留继承的工作树修改。
4. 先对 Day 13 主题进行来源前主动回忆，再读卡中指定方法/论文；分开记录实验报告、作者解释、模型输出和本任务推断。
5. 检查竞争解释、至少一个反证、必要伴随观测、独立性/共享数据边界，以及一个定量或设计练习；产物同步写入 `knowledge/` 与当日报告。
6. 按运行时快照执行时间门；不要把局部来源饱和当作整段运行完成。若规则允许，只能预习紧邻的 Day 14；不得打开 Day 15。
7. 报告须含 Day 13 card completion audit、唯一 `knowledge-writeback` block、L0–L4 readiness、检查结果、session ID/resume command，并按仓库发布门提交/推送本次任务文件。

完成报告、canonical knowledge 写回、路径/内容检查和发布后，将课程状态从 Day 13 推进。raw 文件、凭据和 `PLAN.md` 保持不变；原始证据的权限/locator 边界继续按 Wiki 规则处理。

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
- now_local: 2026-10-13T17:12:58.564161+08:00
- hard_deadline: 2026-10-14T15:00:00+08:00
- next_scheduled_start: 2026-10-14T16:00:00+08:00
- minutes_to_deadline: 1307
- minutes_to_next_start: 1367
- closeout_decision: continue-or-advance
- Next card candidate: Day 13 (Doppler-correction-recoil与速度信息).
If closeout_decision is continue-or-advance, continue the current high-value issue; if both selected slots are saturated, inspect the next card and complete it only if its full deliverable fits the window.
If closeout_decision is continue-current-or-partial, stay within the current issue or do one bounded preview; do not claim a whole next card.
If closeout_decision is finish-current-no-new-unit, finish only the current bounded analysis and do not open another source/card. If it is closeout-only, stop research and finalize.
Before ending early for evidence saturation, refresh the clock and candidate pool; saturation of the two selected slots alone is not schedule-level saturation while a viable next-card route remains.
<!-- DAILY_LEARNING_RUNTIME_SNAPSHOT_END -->
