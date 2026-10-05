---
type: system-prompt
graph-excluded: true
created: 2026-10-05
updated: 2026-10-05
---

# DAY7 — 第一次周考：集体运动口试

## Run context

- run_id: prompt-2026-10-06-day-07
- run_date: 2026-10-06
- timezone: Asia/Shanghai
- day_index: 7
- day_topic: 第一次周考：集体运动口试
- phase: nuclear-structure-framework
- schedule_id: wiki-daily-learning
- overnight_until: 2026-10-07T15:00:00+08:00
- output_dir: /workspace/wiki/outputs/learning-daily/20261006-DAY7-collective-motion-oral-exam-run-01
- state_file: /workspace/wiki/outputs/learning-milestones/2026-09-one-month-state.json

## Study contract

在 /workspace/wiki 内执行。开始前读取 README.md、knowledge/index.md、profile.md、active handoff、PLAN.md、Day 1–6 日报、本学习计划与 daily-task-matrix 的 Day 7 卡，以及 autonomous-research / continuous-learning workflow。写前运行 Wiki boundary check；保留既有 dirty files、raw、PLAN.md 和 review 状态。日报和可复用结论尽量使用中文。不要把模型结果写成实验事实，也不要设置 human-reviewed 或清除 needs_review。

## Day 7 card

1. 不看资料，随机回答 Day 1–6 各一道定义题；把回忆和随后核对的差异记录为个人错题。
2. 从 Day 1–6 已读案例中选一个，优先 131Ce，复述“壳结构/形变 → 能级与跃迁 → alignment/signature → 作者解释 → 竞争解释”的证据链。精确回到知识页和 source locator。
3. 对一个未知的短能带摘要做 20 分钟结构判读：写组态候选、必要观测、替代解释、证据停止条件。未知摘要只可作练习题，不能伪造为实验来源或当作新结果。
4. 指出最可能改变当前判断的一条证据，并说明出现何种结果时会如何修订排序。
5. 形成理论、判图、误差、证据分层、反证、可证伪问题六项周考评分表，每项 0–4 分；再形成 weekly REFLECT。把有复用价值的错误模式、判据或证据矩阵变化写回适当的 knowledge 页面，日报不能是唯一副本。

L0–L4 按现有状态机记录。缺少原始事件、response、covariance 或代码时不进入 L4。选题最多一项连续问题和一项不重叠新问题；Day 7 是复习考核，不扩成新的文献批次。

## Required report

写到：

/workspace/wiki/outputs/learning-daily/20261006-DAY7-collective-motion-oral-exam.md

必需标题：Run state、Candidate pool and selection、Sources and evidence、Theory/analysis exercise、Counter-evidence and missing companion observables、Knowledge Impact and Learning Decision、Durable knowledge delta、Open questions and belief revision、L0–L4 state、Verification and continuation。

Durable knowledge delta 必须包含至少一个 knowledge/ 下的具体路径和唯一一个有效 knowledge-writeback JSON 块。完成前运行：

- python3 system/scripts/wiki_boundary_check.py --root .
- python3 system/scripts/wiki_lint.py --fail-on error
- git diff --check

仅在报告、知识写回、prompt 和检查均完成后按 Wiki 的 Gitee 发布门发布；仅暂存本轮任务文件。

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
