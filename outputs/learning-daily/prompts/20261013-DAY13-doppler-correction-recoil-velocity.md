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
