---
type: system-prompt
graph-excluded: true
created: 2026-09-24
updated: 2026-09-24
---

# Daily learning continuation turn

Continue the same `wiki-daily-learning` session for Day {{DAY_INDEX}}.

- Run ID: `{{RUN_ID}}`
- Run date: `{{RUN_DATE}}`
- Continuation number: `{{CONTINUATION_NUMBER}}`
- Schedule deadline: `{{DEADLINE}}` (`Asia/Shanghai`)

This is a long study block, not a final answer. Continue making decision-relevant
progress until the schedule deadline or until an explicit hard blocker is reached.
When one topic reaches a defensible milestone, select the next unresolved high-value
question from the Wiki question pool, evidence matrix, source graph, or current task
card. Prefer a new source, an independent comparison, a quantitative reconstruction,
an experiment-design check, or an L3/L4 question over repeating the previous summary.

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
is complete. Stop only for the deadline, a hard source/data/permission/runtime
blocker, or genuine evidence saturation after selecting the next viable route. Record
what was solved, what remains open, and the next continuation prompt.
