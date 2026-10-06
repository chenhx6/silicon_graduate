---
type: system-prompt
graph-excluded: true
created: 2026-10-06
updated: 2026-10-06
---

# DAY8 — 角动量耦合、选择定则与多极性

## Run context

- run_id: prompt-2026-10-07-day-08
- run_date: 2026-10-07
- timezone: Asia/Shanghai
- day_index: 8
- day_topic: 角动量耦合、选择定则与多极性
- phase: nuclear-structure-framework
- schedule_id: wiki-daily-learning
- schedule_name: Wiki 30-day substantive daily learning
- expected_start: 2026-10-07T16:00:00+08:00
- overnight_until: 2026-10-08T15:00:00+08:00
- output_dir: /workspace/wiki/outputs/learning-daily/20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01
- report_file: /workspace/wiki/outputs/learning-daily/20261007-DAY8-angular-momentum-selection-rules-multipolarity.md
- state_file: /workspace/wiki/outputs/learning-milestones/2026-09-one-month-state.json

## Study contract

在 /workspace/wiki 内执行。开始前读取 README.md、knowledge/index.md、profile.md、active handoff、PLAN.md、DAY7 日报、本学习计划与 daily-task-matrix 的 Day8 卡，以及 autonomous-research / continuous-learning workflow。写前运行 Wiki boundary check；保留既有 dirty files、raw、PLAN.md、课程 state 和 review 状态。日报和可复用结论尽量使用中文。不要把模型结果写成实验事实，也不要设置 human-reviewed 或清除 needs_review。

DAY7 日报已经包含 Day8 知识预习，但预习不计 Day8 学分。正式 Day8 session 必须重新完成本卡交付、建立自己的 recall/evidence record 和 Day8 card audit；不得继承 Day7 预习为已完成结论。若先读到 Day7 预习或知识页，再做 recall，须明确标记为 primed recall，不称为 blind recall。

## Day 8 card

1. 回忆：在查资料前写出 E1/M1/E2 的宇称变化和角动量选择定则，说明 forbidden 与 hindered 的区别；再回到来源核对差异。
2. 主线：阅读已有来源 Lange, Kumar & Hamilton 1982 与 Rose & Brink 1967。记录原文采用的 δ 定义、符号/相位、初末态顺序、发射/吸收约定和适用条件。
3. 练习：对三条合成跃迁列出所有满足角动量三角和宇称规则的低阶及相关高阶多极候选，写出角分布、DCO/角关联、线偏振、内转换或寿命分别能排除什么解。
4. 反证：逐项检查 spin、parity、multipolarity 是否由彼此独立的观测支持；若多个标签来自同一个含假设的拟合，说明依赖关系。
5. 交付：选择定则和多解表；每个符号约定、公式和判断回到 source locator。合成跃迁只作练习题，不对应实验或核素新结果。

Day7 预习中已出现以下合成例，正式 Day8 需要自己重新推导并检查候选多极组合，不能把旧表格直接算作 Day8 作业：

- 3/2+ → 1/2−：ΔJ=1、Ji+Jf=2、宇称改变；检查 E1/M2。
- 2+ → 2+：ΔJ=0、允许 rank 1–4、宇称不变；检查 M1/E2/M3/E4，并说明若只拟合 M1/E2 所用的低阶截断。
- 3+ → 1+：ΔJ=2、允许 rank 2–4、宇称不变；检查 E2/M3/E4，并说明 E2/M3 截断的条件。

优先 source locators：

- Rose & Brink 1967：Sec. III.E, printed p.320 after Eqs.3.40–3.41, angular-momentum/parity selection rules；Secs. III.B–III.E, pp.314–324, Eqs.3.17–3.47, aligned-state angular distribution and interference；p.316 after Eq.3.24, linear polarization；p.318 Eq.3.29, total gamma width；p.326 Eq.3.73, cascade phase.
- Lange, Kumar & Hamilton 1982：Sec. II.A, printed pp.121–123, Eqs.2.1–2.11, E2/M1 δ definition and sign convention.

## Run boundary and evidence rules

- Keep the run day index at 8. The prior Day8 preview belongs only to partial_day_indices in the Day7 report.
- Credit Day8 only after every Day8 deliverable and its card audit pass in this formal run; update state only through the normal course runner/state contract.
- Do not search a new literature batch to fill an exercise. The two Day8 source pages are already in knowledge/sources/.
- Distinguish selection-rule exclusions, model truncations, measured angular/polarization evidence, and inferred transition strengths.
- A lifetime constrains total rate with branching; it does not determine the relative phase/sign of δ. A linear-polarization or angular-distribution result is setup- and convention-dependent.
- L0–L4 follow system/workflows/autonomous-research.md. Missing event data, response, covariance or code means no L4.

## Time-aware continuation gate

Read the latest Runtime schedule snapshot. If resuming manually without a fresh snapshot, call the current-time tool and compare with this run receipt's overnight_until.

- At least 120 minutes before the hard deadline: continue the current high-information Day8 issue. If it saturates, rebuild the candidate pool and inspect only the next uncompleted card. The user-authorized rule permits pre-studying knowledge from exactly Day9 as an uncredited preview; keep day_index=8, list Day9 only in partial_day_indices, do not credit Day9, do not advance next_day_index past Day9, and do not open Day10.
- 90–119 minutes: continue Day8 or do one bounded Day9 preview without credit.
- Under 90 minutes: do not open a new source or card; finish the bounded analysis.
- At the 2026-10-08 15:00 hard deadline, stop new research; use 15:00–16:00 only for closeout.
- Do not stop solely because the requested Day8 card is complete while useful time remains; rebuild the candidate pool and check the permitted Day9 preview route first.
- A user stop, hard evidence/data/permission blocker or runtime failure remains an immediate stop.

## Required report

Write the report to:

/workspace/wiki/outputs/learning-daily/20261007-DAY8-angular-momentum-selection-rules-multipolarity.md

Required headings:

- Run state
- Candidate pool and selection
- Sources and evidence
- Theory/analysis exercise
- Counter-evidence and missing companion observables
- Knowledge Impact and Learning Decision
- Durable knowledge delta
- Open questions and belief revision
- L0–L4 state
- Verification and continuation

In Run state include exactly one completed_day_indices line and one partial_day_indices line. If Day8 is complete, include the exact audit lines:

- Day 8 card audit: complete

and a “### Day 8 card completion audit” table with at least four Day-matrix deliverables, each mapped to a locator/artifact and marked complete. Any Day9 preview belongs only in partial_day_indices; do not advance the course beyond Day8.

Durable knowledge delta must include a concrete knowledge/ path and exactly one valid knowledge-writeback JSON block. Use status updated only when a knowledge page actually changed; otherwise use verified-no-op with grounded source locators. Never make the daily report the only copy of reusable knowledge.

Before closeout:

- python3 system/scripts/wiki_boundary_check.py --root .
- python3 system/scripts/wiki_lint.py --fail-on error
- git diff --check

Only stage this formal Day8 run's task-owned files. Follow the Gitee non-force publication gate in the Wiki instructions.
