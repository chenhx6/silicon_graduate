---
type: system-prompt
graph-excluded: true
created: 2026-09-24
updated: 2026-10-06
---

# Daily learning continuation turn

Continue the same `wiki-daily-learning` session for Day {{DAY_INDEX}}.

- Run ID: `{{RUN_ID}}`
- Run date: `{{RUN_DATE}}`
- Continuation number: `{{CONTINUATION_NUMBER}}`
- Schedule deadline: `{{DEADLINE}}` (`Asia/Shanghai`)

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
remains: continue the current slot and rebuild the candidate pool. With at least 120
minutes remaining, inspect the next uncompleted Day card; you may pre-study knowledge
from exactly that next-day card as an uncredited preview. Keep today's `day_index`, put
the next card only in `partial_day_indices`, do not advance `next_day_index` past it,
and do not open Day+2. Formal card credit remains tied to that card's own day run, even
if its knowledge was covered early. With 90–119 minutes, continue the current issue or
do one bounded preview without crediting the next card. Under 90 minutes, do not open
a new source/card; finish current analysis. At the deadline, switch to closeout-only
work. A user cancellation or hard blocker still stops immediately.

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
