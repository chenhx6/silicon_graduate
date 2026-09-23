---
type: system-wip-queue
graph-excluded: true
updated: 2026-09-13
---

# Pending WIP queue

This page tracks pending local WIP/review tasks that still need follow-up work. Keep entries short. Do not store long reports here. `system/review-history.md` records completed human-review rounds; the same task may appear in both places.

## Active entries

### Unread degree-dissertation corpus: adaptive ingest and full-Wiki closure (2026-09-10)
- status: final research package on `main`; Codex self-audit and local publication gates complete; explicit partial/stopped L3 boundaries remain for future research
- plan: `docs/plans/2026-09-10-degree-dissertation-corpus-ingest.md`
- scope: all PDFs under `raw/papers/degree dissertation`; adaptive coverage, high-value deep reading, full-Wiki bidirectional linking, cross-source review and two independent self-audits
- completion gate: all files have a truthful reading state; high-value claims have source locators; affected Wiki pages are linked; reports and lint/graph/hash checks pass; remaining scientific gaps are recorded with stop reasons and next routes
- completed: 55 PDFs / 54 unique hashes / 1 duplicate; 46 raw-to-source mappings; no queued PDF; L3 `31 completed / 21 partially-researched / 3 stopped`; L4 `0`; external `135Nd` parity, `100Sn` context and `135Pr` controversy crosswalks recorded; farmer PID 8571 running with no pending recovery
- next action: optional future research on `135Pr` common-response/absolute-strength or `16C`/`32S`/CSR data conditions; no user review request is made
- Git gate: this final package is scoped for exact non-force `HEAD:main` publication; scientific partial/stopped and unreviewed claims do not block, while technical hard P0, protected-path/hash, lint, ancestry or remote/auth failures remain stopping conditions

### Daily learning: `100Sn` independent B(GT) evidence map (2026-09-07 continuation)
- status: content-complete / final-not-pushed; active-L2; raw-PDF locator crosswalk completed
- files: `knowledge/projects/100sn-gamow-teller-independent-evidence.md`, both `100Sn` source pages, `outputs/learning-daily/2026-09-07.md`, `system/handoff.md`, `system/log.md`
- next action: retain the claim-specific phase-space/B(GT) and `100In` branching boundary for future Q&A or paper use; no user review request is made
- Git gate: Docker terminal runtime is available; publication awaits explicit staged-file checks, not advance human review

### 90-day continuous nuclear-structure learning: 2026-09-05–2026-12-03
- status: framework-ready; daily 22:00 Asia/Shanghai project automation `wiki` is ACTIVE; content and Git publication are explicitly decoupled
- scope: four phases, dynamic multi-topic/multi-source reading, graph closure, thematic REFLECT, daily/weekly/milestone records; seed corpus is the 15-dissertation batch
- files: `system/workflows/continuous-learning.md`, `system/learning-queue.md`, `knowledge/` durable learning assets, `outputs/learning-daily/`, `outputs/learning-weekly/`, `outputs/learning-milestones/`, README/user-guide/check updates
- next action: first run starts with dissertation graph closure and cross-mass-region comparison; write a daily record, then select the highest-information-gap problem
- Git gate: if network or remote publication fails, keep Wiki content write-back and record `content-complete / final-not-pushed`

### Degree dissertation batch: 2026-09-05
- status: content-complete; one-time publication remains pending after the Python tooling migration; no new commit/push
- scope: 15 degree dissertations represented (Ding existing, Alwaleedi re-read, 13 new thesis sources) plus the `103Pd` experiment report; source/nucleus/concept/observable/index/overview/report/script files
- self-audit boundary: all new source claims retain their evidence flags; complete P0/P1 list is in `outputs/degree-dissertation-ingest-20260905.md`; later Q&A/paper use may trigger claim-specific review
- protected: `raw/zotero/wiki-inbox.bib`, `.codex/config.toml`, `system/lint-config.json`, all raw PDFs and extracted raw images remain unstaged
- commit target: one explicit-stage commit using `Ingest 15 degree dissertations corpus` (do not use `git add .`)
- next action: run `python3 script/git20260905.py --dry-run`, then publish only after reviewing the manifest scope

### Review pending: 丁兵 2012 `127,128I` thesis correction
- status: current HEAD is the existing `WIP ingest: Ding 2012 127I 128I high-spin thesis`; the path correction and batch synchronization remain in the current worktree
- files: source note; `127I`/`128I` nucleus and five band pages; University of Tsukuba experiment page; index; handoff/log
- self-audit boundary: all 11 source claims retain their evidence flags; ADO values, two-branch mapping, NPA ordering/configuration boundaries and exact thesis-to-journal crosswalks remain future claim-specific verification routes
- risks: keep `raw/zotero/wiki-inbox.bib` unstaged; do not use the historical `ciae-hi13-127-128i-li7-28-32mev` slug
- next action: include the corrected Ding source path in the batch's explicit manifest; do not amend the already tracked WIP commit or force-push it

### Review pending: `106Ag` dual-DSAM lineage conflict
- status: final-not-pushed on `main`; focused scientific review and local dual-source ingest remain pending; both Git runtimes failed dry-run because protected AskPass could not be spawned
- branch: `main`
- commit: current main HEAD `Finalize weekly self-tests through 2026-08-31`
- files: 2026-08-31 weekly-learning report; literature-acquisition manifest; handoff/log/queue
- scheduler note: selected as a non-overlapping novelty slot outside the recent `135Pr` and `131Ce` source clusters
- self-audit route: when source PDFs become available, count Lieder 2014 and Rather 2014 as independent experiments; retain their common falsification while separating their nonidentical configuration/model interpretations
- overview/QMD: unchanged/deferred until both original PDFs are locally verified and ingested
- next action: obtain and hash both PDFs, then perform one dual-source band/lifetime/model crosswalk before changing the `106Ag` nucleus or chirality project
- risks: no local candidate PDF or BibTeX exists; Bark/Wang are repeated secondary lineage, not experimental replication; protected Zotero BibTeX remains unstaged

### Review pending: `131Ce` N=73 isotone discrimination
- status: published to `main` for traceability; focused scientific review remains pending
- branch: `main`
- commit: current main HEAD `Audit 131Ce N=73 evidence lineage`
- files: Ding 2021 source; `131Ce` project/nucleus; 2026-08-17 weekly-learning report; 2026-08-19 continuation-audit report; handoff/log/queue
- scheduler note: the 2026-08-19 continuation audit does not count as a learning cycle; the next true novelty slot must use a non-overlapping coverage area unless a hard exception is recorded
- self-audit route: verify D21-8, the two project evidence rows, independence counting, refs.46-48 source lineage and configuration-specific transfer boundaries; no advance user review request
- overview/QMD: overview/index unchanged; QMD deferred until review finalization
- next action: review the report P1 items; if manuscript-level use is planned, read Byrne 1992, Palacz 1991 and Bazzacco 1998 before admitting the exact band crosswalk
- risks: protected `raw/zotero/wiki-inbox.bib` remains unstaged; no neighbor wobbling label may be transferred to `131Ce`

### Self-audit continuation: `135Pr` mixing-ratio branch reassessment
- status: Codex self-audit continuation completed for current source acquisition; final publication is pending; no user review request is made
- branch: `main`
- commit: included in current main HEAD `Finalize weekly self-tests through 2026-08-31`
- files: 2026-08-24 weekly-learning report; literature-acquisition manifest; handoff/log/queue
- scheduler note: this is the first post-repair novelty slot and is outside the `131Ce`/Ding/`127Xe`/`129Ba` cooldown cluster
- self-audit result: 2026 combined Gammasphere data are a dependent support lineage; Guo 2021 double-solution comment and Lv 2022 independent small-`|δ|` `P-R_ac` branch remain explicit counter-evidence; retain unresolved-verdict boundary
- overview/QMD: unchanged/deferred until the 2026 PDF is locally verified and ingested
- next action: retain the two verified PDFs/manifests and use the common-response/absolute-strength route only if raw spectra, calibration and executable analysis become available; otherwise proceed to final publication gates
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
