---
type: system-workflow
graph-excluded: true
operation: scheduled-continuation
updated: 2026-09-06
---

# SCHEDULED CONTINUATION：定时续跑流程

## 适用范围

用于配额刷新后继续、延迟复核、定时检查或其他无人值守任务。它管理的是执行可靠性，不替代摄入、查询、综合或 lint 工作流。

## 先判断是否应该调度

1. 任务能否现在安全完成？能则不调度。
2. 等待是否超过 1 小时？超过时不得使用 heartbeat。
3. 是否必须准时完成？若是，只有已经验证的常驻或远端执行环境才可承担；本地尽力调度不够。
4. 到期时本机应用、调度服务和电脑能否保持可用？不能确认时，使用 handoff + 用户唤醒。
5. 配额刷新是否只是执行前提？刷新本身不会唤醒任务。

应用开启、电脑持续接电和禁用休眠只是必要的环境检查，不是本地调度成功的充分条件。即使这些条件全部满足，没有实际运行回执仍按“未触发”处理。

## 调度类型

科研型每周自测的科学深度、L3 升级、L4 手动关口、P0/P1 报告和本地 commit 规则由 `autonomous-research.md` 管理；本文件只管理调度可靠性、回执和恢复。每周自测等待超过一小时且属于独立项目任务，应使用 project cron，不使用 heartbeat。

### 短时同线程续跑

- 仅限 1 小时内；
- 使用 heartbeat；
- 明确要求 Codex 与电脑保持运行和唤醒；
- 到期后仍须核对运行回执。

### 较长或独立工作区任务

- 使用面向工作区的独立调度，不使用 heartbeat；
- 调度前确认工作区、分支、时区、执行命令和权限；
- 若执行环境仍在本机，明确说明它不能唤醒已关闭或挂起的应用/电脑；
- 必须准时完成时，应改用已验证的远端常驻执行环境，或由用户手动唤醒。

### handoff + 用户唤醒

这是本知识库跨额度窗口的默认方案：

1. 把当前状态、未完成事项、精确续跑命令和验证标准写入 `system/handoff.md`；
2. 运行可在当前额度内完成的检查；
3. 告知用户在额度刷新后发送“继续”；
4. 新会话按 `AGENTS.md` 启动顺序恢复。

## Wiki local-project automation

Codex runs these tasks in the Docker terminal. A task may call
`python3 system/scripts/wiki_automation_preflight.py --root .` before Git
publication to verify the working tree and protected BibTeX baseline. The
preflight is a diagnostic convenience, not a second permission system; it does
not inspect Desktop state, ACLs, or PowerShell markers. Keep task recovery in
`system/handoff.md`, reports, and Git files inside the Wiki.

For publication, check the intended files explicitly, run lint, fetch `origin`
(`https://gitee.com/chx6/silicon_graduate`), verify remote ancestry, then use
`git push --dry-run origin HEAD:main` followed by the same non-force refspec.
Network or authentication failure leaves the local content intact and is
reported as `final-not-pushed`.

## Wiki weekly self-test and bounded research expansion

The weekly automation checks evidence quality, internal consistency, P0/P1
risks and human-review boundaries. Classify each run before opening detailed
evidence as `weekly-learning`, `continuation-audit`, or `maintenance`. Only
`weekly-learning` counts toward the learning cadence; a locator repair, status
reconciliation or repeated verification is a `continuation-audit` unless it
produces new decision-relevant information.

For `weekly-learning`, build a Wiki-local read-only candidate pool before
selecting papers or writing pages. Candidates must pass the hard importance
gate and span coverage dimensions such as nucleus/mass region, physical
mechanism, method/observable, evidence type and human-review risk. Use two
slots: a continuity slot for a hard P0/P1, new independent evidence or a
decision-changing unresolved issue, and a novelty slot that must use a
non-overlapping coverage area whenever any eligible candidate exists. If no
eligible novelty candidate exists, emit a verified receipt instead of filling
the slot with low-value work. Pending review does not suppress read-only
global scouting or non-overlapping novelty work; it only blocks overlapping
writes.

Reconstruct coverage from the latest eight repository-local
`weekly-learning` reports, never from Codex host memory/global/sandbox state.
Do not let the same nucleus/project occupy the novelty slot in consecutive
learning cycles, and cool the same core-source fingerprint for two learning
cycles. Hard P0, new independent primary evidence, substantive source
conflict or an explicit user request may override the cooldown only when the
report records the exception. Rank eligible candidates by scientific impact,
coverage debt, time since last touch, independence gap and expected
information gain; use an ISO-week-seeded random tie-break only among equivalent
candidates. During the migration cycle, the next novelty slot excludes
`131Ce`, Ding 2021, `127Xe` 2020 and `129Ba` 2024 unless an exception is
recorded.

It may actively research at most two important problems per run. The total
number of papers is not capped, but each download must belong to a deduplicated,
finite, directly relevant batch; stop when evidence saturates, information
gain falls, time/validation margin is low, or user access is required. Other
important findings go in the report's `Deferred important issues` section with
pages, evidence gaps, a suggested L3/L4 route and whether the next run or the
user should continue them. Every substantive report contains a `Selection
audit` listing the run type, cadence status, candidates/coverage, slot
decisions, source fingerprints and overlap, cooldown exceptions, deferred
reasons, new knowledge and belief revision. Only a task that has actually
started and changed files enters WIP.

For a nuclear-structure question, compare at least one applicable isotope and
one isotone when reliable evidence exists; explain when a comparison is not
physical or not available. L3 may search, obtain lawful full text, audit
locators and ingest evidence through the Nature-first search/downloader
routes. Candidate PDFs enter `raw/papers/gpt/_incoming/<run-id>/`, are verified
before promotion to `raw/papers/gpt/`, and Agent-managed BibTeX goes only to
`raw/zotero/gpt.bib`; `raw/zotero/wiki-inbox.bib` is read-only and never staged.
Download supplementary information only when a key datum or method is there.
If full text needs login, CAPTCHA or user access, record the DOI, route and
handoff instead of looping or treating HTML as PDF.

L4 is a readiness audit, not an automatic experiment. Check existing Wiki
literature/data, level schemes, ADO, linear-polarization information, analyses
and authoritative public data such as NNDC; report the sources, reproducibility,
missing observables/locators and `ready`, `partial` or `not-ready` in
`outputs/l4/<issue>-<date>/report.md`. `partial` or `not-ready` ends only that
issue's expansion; it does not stop the weekly run or disable the automation.
The task never force-pushes. It may perform a normal push only when the current
task explicitly authorizes publication and H3/repository checks pass. With no
substantive change it emits only a verified run receipt and creates no empty
commit.

## Safe suspend

当 Codex 发现上下文、token、5 小时额度或执行余量不足，且当前任务无法稳定完成时，立即执行：

1. 停止新增大范围修改；
2. 运行：

   ```bash
   git status --short
   git diff --stat
   git diff --check
   ```

3. 更新 `system/handoff.md`，写明已完成事项、未完成事项、已修改文件、当前风险，以及下一轮可直接执行的续跑提示词；
4. 除非用户明确要求，不得自动 commit/push；
5. 告知用户等待额度刷新后发送“继续”。

Safe suspend 是一次受控停点，不是让当前任务自动睡眠并原地恢复，也不会自动创建 automation。若用户后续选择 automation，应把它视为额度刷新后启动的新任务，由该任务读取 handoff 后继续。

## 创建前检查

- [ ] 类型与等待时长匹配；
- [ ] 时区为 `Asia/Shanghai`，日期和时间明确；
- [ ] 一次性任务在界面中显示为一次，不显示“每天”；
- [ ] 工作区和目标线程正确；
- [ ] 到期时的应用/调度服务/电脑可用性已经说明；
- [ ] 已写入失败时的 handoff 和人工恢复路径；
- [ ] 没有使用“保证完成”“无需操作”等超出证据的表述。

如果调度器只能把一次任务编码为类似 `FREQ=DAILY;COUNT=1` 的规则，而界面显示“每天”，应视为表达有歧义，不启用该任务。

## 到期后的回执门

必须核对：

1. 是否生成运行记录；
2. 实际开始和结束时间；
3. 退出状态或错误；
4. 目标文件、提交或报告是否真实存在；
5. Git diff 与 `raw/` 边界是否安全。

只有以上证据成立，才能报告“已执行”或“已完成”。没有运行记录时写“未触发”；有记录但产物未核验时写“已触发、未验证”；不得用预定时间推断执行结果。

一次性任务完成或失败后应删除，避免残留触发。
