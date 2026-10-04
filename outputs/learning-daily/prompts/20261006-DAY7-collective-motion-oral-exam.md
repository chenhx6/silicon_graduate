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
