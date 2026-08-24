---
type: system-wip-queue
graph-excluded: true
updated: 2026-09-01
---

# Pending WIP queue

This page tracks pending local WIP/review tasks that still need follow-up work. Keep entries short. Do not store long reports here. `system/review-history.md` records completed human-review rounds; the same task may appear in both places.

## Active entries

### Review pending: `106Ag` dual-DSAM lineage conflict
- status: final-not-pushed on `main`; focused scientific review and local dual-source ingest remain pending; both Git runtimes failed dry-run because protected AskPass could not be spawned
- branch: `main`
- commit: current main HEAD `Finalize weekly self-tests through 2026-08-31`
- files: 2026-08-31 weekly-learning report; literature-acquisition manifest; handoff/log/queue
- scheduler note: selected as a non-overlapping novelty slot outside the recent `135Pr` and `131Ce` source clusters
- review needed: count Lieder 2014 and Rather 2014 as independent experiments; retain their common falsification of the simple chiral-pair reading while separating their nonidentical configuration/model interpretations
- overview/QMD: unchanged/deferred until both original PDFs are locally verified and ingested
- next action: obtain and hash both PDFs, then perform one dual-source band/lifetime/model crosswalk before changing the `106Ag` nucleus or chirality project
- risks: no local candidate PDF or BibTeX exists; Bark/Wang are repeated secondary lineage, not experimental replication; protected Zotero BibTeX remains unstaged

### Review pending: `131Ce` N=73 isotone discrimination
- status: published to `main` for traceability; focused scientific review remains pending
- branch: `main`
- commit: current main HEAD `Audit 131Ce N=73 evidence lineage`
- files: Ding 2021 source; `131Ce` project/nucleus; 2026-08-17 weekly-learning report; 2026-08-19 continuation-audit report; handoff/log/queue
- scheduler note: the 2026-08-19 continuation audit does not count as a learning cycle; the next true novelty slot must use a non-overlapping coverage area unless a hard exception is recorded
- review needed: D21-8 and the two project evidence rows; verify independence counting, refs.46-48 source lineage and configuration-specific transfer boundaries
- overview/QMD: overview/index unchanged; QMD deferred until review finalization
- next action: review the report P1 items; if manuscript-level use is planned, read Byrne 1992, Palacz 1991 and Bazzacco 1998 before admitting the exact band crosswalk
- risks: protected `raw/zotero/wiki-inbox.bib` remains unstaged; no neighbor wobbling label may be transferred to `131Ce`

### Review pending: `135Pr` mixing-ratio branch reassessment
- status: final-not-pushed on `main`; focused scientific review remains pending; both Git runtimes failed dry-run because protected AskPass could not be spawned
- branch: `main`
- commit: included in current main HEAD `Finalize weekly self-tests through 2026-08-31`
- files: 2026-08-24 weekly-learning report; literature-acquisition manifest; handoff/log/queue
- scheduler note: this is the first post-repair novelty slot and is outside the `131Ce`/Ding/`127Xe`/`129Ba` cooldown cluster
- review needed: classify the 2026 combined Gammasphere dataset as partially independent; compare its large-`|δ|` angular-distribution branch with Lv 2022's independent small-`|δ|` `P-R_ac` branch; retain the unresolved-verdict boundary
- overview/QMD: unchanged/deferred until the 2026 PDF is locally verified and ingested
- next action: review the report P1 items; after network recovery, fresh-fetch and publish the existing WIP if remote ancestry is safe. Separately obtain arXiv:2403.10749v2 or the published PDF into the controlled incoming path before source/project ingest
- risks: no local PDF or BibTeX entry exists; correction notices and Guo comments are not independent experimental replications; protected Zotero BibTeX remains unstaged

## Legacy completed entries

These entries predate `system/review-history.md`. Keep them as legacy context during framework setup; do not backfill or migrate them automatically in this task. Future human-review rounds should be appended to `system/review-history.md`, while queue follow-up remains a separate judgment.

### Sigma-over-I writing-support synthesis
- status: user review finalized; final commit created from the prior `WIP review:` task and ready for push on `main`
- branch: `main`
- commit: current HEAD final `Create sigma-over-I writing-support synthesis`
- files: sigma-over-I project page; sigma-over-I writing-support synthesis; repaired `knowledge/index.md`; `sigma-over-i` and `magnetic-substate-population` concept pages; `spin-alignment-attenuation-factor`; overview; handoff/log/queue
- review needed: none for the current project/synthesis wording round; the low-spin caution remains intentionally bounded rather than universal
- overview/QMD: overview refreshed; `qmd.cmd update`, `qmd.cmd embed -c nuclear-knowledge`, and `qmd.cmd status` succeeded
- next action: optional follow-up is to map the actual P-ADO `sigma/I` code/input convention and calibration-transition strategy before writing code-facing equations
- risks: `.obsidian/` and `raw/zotero/wiki-inbox.bib` remain external/user changes and were not included

### Article10-11 supplemental spin-alignment assumption sources
- status: user review round completed
- execution status: corresponding review-side commit was pushed to `origin/main`
- branch: `main`
- commit: `f4934e7` (`Ingest supplemental spin-alignment assumption sources`)
- files: Ekstrom 1979 and Ionescu 1981 source pages; direct-feeding / compound-nucleus-reaction-model / spin-alignment-attenuation-factor pages; sigma-over-I project; overview; PLAN; handoff/log/queue
- review needed: none for EK79-*, IO81-1..10, or SIO-PROJ-16/17/18/19
- overview/QMD: overview refreshed; `qmd.cmd update`, `qmd.cmd embed -c nuclear-knowledge`, and `qmd.cmd status` succeeded
- next action: optional scientific follow-up is to map the actual P-ADO `sigma/I` code/input convention before writing final equations
- risks: `.obsidian/` and `raw/zotero/wiki-inbox.bib` remain external/user changes and were not included

### Article7-9 sigma-over-I practice sources
- status: user review round completed
- execution status: WIP ingest was amended to a later commit and pushed to `origin/main`
- branch: `main`
- commit: final commit created from prior local `WIP ingest: article7-9 sigma-over-I practice sources for user review`
- files: Chiara 2012, Summary 2013 and Gray 2020 source pages; sigma-over-I project; spin-parity-assignment/TDPAD/g-factor method pages; sigma-over-I concept; index/overview/questions; handoff/log/queue
- review needed: none for CH12-*, SB13-*, G20-* or SIO-PROJ-13/14/15; related method/concept pages remain page-level `unreviewed`
- overview/QMD: overview refreshed; QMD update/embed/status succeeded after sandbox escalation
- next action: map actual P-ADO `sigma/I` code/input convention before writing final equation-level synthesis
- risks: `.obsidian/` and `raw/zotero/wiki-inbox.bib` remain external/user changes and were not included; Summary 2013 `sigma/I = 0.3` stays at guide-level background

### Article4-6 sigma-over-I deorientation/formalism sources
- status: user review round completed
- execution status: WIP ingest was amended to a later commit and pushed to `origin/main`
- branch: `main`
- commit: final commit created from WIP `0e3414d` with message `Finalize article4-6 sigma-over-I source review`
- files: Cejnar 1996, Radeck 2012 and Lauritsen 2025 source pages; new `152Dy` nucleus/experiment pages; deorientation/angular-correlation/tracking-array anchors; sigma-over-I project; index/overview; handoff/log/queue
- review needed: no source/project P0 remains; new `152Dy` nucleus/experiment pages are narrow Lauritsen-derived entries and remain page-level `unreviewed`
- overview/QMD: overview refreshed; QMD update/embed/status succeeded after sandbox escalation
- next action: map actual P-ADO `sigma/I` code/input convention and user-data conditions before writing final equations
- risks: `.obsidian/`, `knowledge/concepts/spin-alignment.md`, and `raw/zotero/wiki-inbox.bib` remain uncommitted external/user changes and were not included

### Sigma-over-I alignment sources
- status: user review round completed
- execution status: corresponding local commit remained unpushed because GitHub/proxy connection failed at that time
- branch: `wip-sigma-over-i-alignment-review`
- commit: `Finalize sigma-over-I alignment source review` local final commit on `wip-sigma-over-i-alignment-review`
- files: Draper 1970, Zobel 1980, Zobel 1983 source pages; sigma-over-I project; overview; handoff/log/queue
- review needed: none identified for DR70-3/6/7, Z80-2/3/10/Fig.5, or Z83 source claims
- overview/QMD: overview refreshed; QMD update/embed/status succeeded after sandbox escalation
- next action: retry `git push origin HEAD:main` or a working proxy push, then map actual P-ADO `sigma/I` input convention and user-data conditions before writing final equations
- risks: `.obsidian/` and `raw/zotero/wiki-inbox.bib` remain uncommitted external/user changes and were not included

## Rules

- Add or update an entry when a task ends as WIP, user-review pending, safe-suspended, not pushed, or has uncertain push status.
- Keep Active handoff short; use this queue for multiple parallel pending WIPs.
- Do not add raw content, source-claim bodies, or long reports here.
- Pending entries only need the latest branch / commit / next action needed to continue review or push; do not preserve every temporary commit/push state here.
- If a WIP commit hash changes after amend or rebase, update the latest branch/commit pointer rather than keeping the old temporary state.
- If a human-review round clearly ends, `system/review-history.md` may receive a new entry even when this queue entry still remains active.
- After a review round is recorded, independently decide whether this queue entry should remain, be updated, or be removed; do not assume a one-way queue-to-history migration.
- If push is skipped or push status is uncertain, keep the task in the pending queue and record that state explicitly rather than guessing completion.
- If the user starts a new ingest while prior WIPs remain unreviewed, keep prior WIPs in this queue instead of overwriting them.
- Before a new ingest/project/synthesis writes files, compare its expected files with active entries. No overlap allows an independent WIP; shared scope continues the original WIP; dependent work records its upstream task/commit; unresolved shared-file overlap is deferred or sent to the user before editing.
- Never record two WIPs as independent when they silently modify the same file. Add a short `depends on` field when dependency is the chosen resolution.
