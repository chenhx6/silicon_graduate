---
name: wiki-evidence-query
description: >-
  Wiki-informed professional Q&A for low-energy nuclear structure and
  experimental spectroscopy. Use the Wiki as the preferred personal research
  context and calibration layer, not as a closed knowledge boundary. Support
  level schemes, band structures, collective excitations, experimental
  criteria, models, competing interpretations, and cross-mass-region
  comparisons. Distinguish Wiki-grounded evidence, externally verified
  evidence, general scientific background, synthesis, and provisional
  inference. Default to read-only evidence-calibrated ordinary Q&A. Expand
  beyond the Wiki when external verification, precise evidence, current
  literature, or broader controversy checking requires it; enter strict
  paper-evidence review only for manuscript, formal-citation, direct-source,
  precise-locator, or key-claim checking.
---

# Wiki-Informed Evidence Query

## Purpose and scope

- Use the Wiki to understand and calibrate to the user, not to confine the
  answer. It is a personalization layer, not a closed corpus or the boundary of
  answerable knowledge.
- Prefer relevant Wiki context, terminology, direct evidence, methods,
  competing interpretations, projects, and priorities. A current anchor such
  as A≈130 is not a query boundary.
- If the Wiki is incomplete, answer ordinary questions with stable general
  scientific knowledge and calibrated reasoning. Do not present model memory
  as Wiki-stored, reviewed, or sourced content.
- Expand beyond the Wiki when the user needs current, precise, controversial,
  externally verifiable, or manuscript-level evidence. External material need
  not be ingested before answering.
- Default to read-only Q&A. Route ingestion, Wiki edits, planning, governance,
  data/raw changes, or Git work to the relevant workflow.
- Treat `knowledge/research-notes/` as provisional research reasoning, not
  source-grounded evidence. Ordinary Q&A excludes it by default. Only include
  it for an explicit research-idea, hypothesis, transfer, reflect, project, or
  synthesis task, and then label its status and verify factual premises against
  its grounded source pages.

## Startup and conditional reads

1. Follow `AGENTS.md` and its startup sequence once per session. Do not reread
   `README.md`, Active handoff, `profile.md`, `system/memory.md`,
   `knowledge/index.md`, or recent log entries already loaded unless repository
   state changed or the question needs a specific section.
2. Read a known target page or source directly; do not rescan the index for
   formality. Do not read superseded handoff or archives in ordinary queries.
3. Do not default-read `USER_GUIDE.md`, `PLAN.md`, full vocabulary, full
   evidence policy, Review history, WIP queue, or paper evidence gate.
4. Use page aliases first. Read only the relevant `system/vocabulary.md` entry
   when terminology is ambiguous, aliases conflict, experimental speech is
   used, or `do_not_merge_with` matters.
5. Read the relevant section of `system/workflows/query.md` only when detailed
   retrieval routing, cross-source synthesis, or external expansion is needed.
6. Read the relevant section of `system/evidence-policy.md` only when claim
   classification, confidence, review status, independence, or evidence grading
   is material.
7. Read `system/paper-evidence-gate.md` only in strict paper-evidence mode.
8. Read `system/review-history.md` only for questions about completed
   human-review rounds, recorded user review decisions, review scope, or
   `review commit message` traceability. It is not a scientific knowledge
   directory, approved-knowledge whitelist, or paper-readiness index.
9. Read `system/wip-queue.md` only for pending WIP or task recovery. Review
   history, WIP queue, handoff, and log are workflow metadata, not scientific
   evidence and not retrieval filters.

## Knowledge-source routing

- **Wiki-grounded:** use source, nucleus, band, concept, observable, project,
  and synthesis pages for personalized and traceable context. Claims described
  as Wiki-grounded must match the current record and its source/locator status.
- **Provisional research reasoning:** research notes may preserve useful
  hypotheses, transfer boundaries, reverse tests, or revision candidates. They
  are excluded from ordinary evidence retrieval and never substitute for their
  grounded sources, even when `reasoning_status: promoted`.
- **General scientific background:** use stable nuclear-structure and
  spectroscopy knowledge when the Wiki is insufficient and the user did not
  request Wiki-only scope. It need not carry a citation on every basic sentence,
  but it is not current Wiki evidence or verified external evidence.
- **Externally verified:** retrieve and inspect external papers, webpages, or
  direct sources when evidence beyond the Wiki is needed. Keep retrieved
  evidence distinct from model memory and search snippets.
- **Synthesis/inference:** identify cross-source synthesis, working hypotheses,
  and possible explanations as such; never attribute them to one paper without
  direct support.

Low-token answering reduces retrieval overhead, not source visibility.

## Inline evidence-link presentation

- Put a verified Wiki link immediately after the sentence or clause it
  supports. Do not default to a separate end-of-answer evidence section.
- Use informative anchor text that identifies the readable page or literature
  name and the exact line, for example:

  ```markdown
  Angular distributions can admit multiple solutions when alignment and mixing ratio are not independently constrained. [Angular Distribution（line 17）](E:/imp/wiki/knowledge/methods/angular-distribution.md:17)
  ```

- For a synthesis or inference supported by several pages, say `综合来看`,
  `可以推断`, or equivalent calibrated wording, then place the most direct
  1-3 informative links after that sentence. Do not present a synthesis as one
  source's direct report or stack links merely for completeness.
- Stable, simple general scientific background need not carry a Wiki link.
  Missing links do not by themselves mean that the Wiki lacks coverage.
- If an important, specific judgment could be mistaken for Wiki evidence but
  the Wiki lacks direct support, say so at that judgment and identify it as
  general background, external evidence, or inference. Do not repeatedly warn
  about ordinary background.
- When the Wiki has a source page, citation key, data, locator, or page entry,
  expose the most useful verification route even for unreviewed material. Use
  Wiki sources first for source requests, then retrieve externally when
  coverage, currency, or breadth is insufficient.
- Only add a separate source list, bibliography, evidence-navigation section,
  claim-to-source table, or similar evidence block when the user explicitly
  asks for it or strict paper review needs it. Do not repeat inline links there.
- Read the target file and use the actual line carrying the claim, paragraph,
  table row, or section content. Never guess a line number or link only to the
  file start when a precise location is available. If the client cannot
  navigate `file.md:line`, use a clickable link with the readable page name and
  the verified section/claim location, and state that line navigation was not
  achieved.
- Never use generic anchors such as `[内容页]`, `[打开证据位置]`, or
  `[证据页]`; never output only a page name, slug, bare `[[wikilink]]`, or a
  backtick-wrapped Wiki entry. If a page name or alias resolves to multiple
  files, list the resolved candidate links instead of guessing.
- In ordinary answers, do not default to citation keys, raw PDF paths, review
  status, full locators, or long evidence cards. Add them when direct-source
  verification or strict paper review requires them. This output rule only
  governs Codex/chat answers; it does not require converting Wikilinks inside
  Wiki Markdown files.
- Do not modify source/project/synthesis pages, create fake or whitespace-only
  diffs, or make temporary commits merely to change link presentation.

## Retrieval budget

### Fast path

Use for a known page, nucleus, band, transition, author, citation key, source
report, simple definition, or stable background question. Read the direct page
and, when Wiki evidence is requested, usually 1-3 source pages. Otherwise answer
from stable general background. Stop when the locator or explanation is enough.
Do not default to semantic search, raw readback, external search, full governance
files, controversy sweeps, or evidence tables.

### Standard path

Use for methods, experimental criteria, small comparisons, moderately ambiguous
terms, research analysis, or interpretation checks. Start with a small set of
high-relevance pages or sources, usually 3-5, plus necessary general background.
Expand only for missing attribution, conflict, a serious alternative, inadequate
support, or a user request for broader evidence.

### Deep path

Use for contested interpretations, cross-nucleus or cross-mass synthesis,
high-value projects, external literature expansion, or manuscript-grade claim
checking. Inspect supporting and alternative sources and use raw/direct sources,
evidence policy, and paper evidence gate as required.

Retrieval routing:

1. Read known files directly.
2. Prefer `rg` or fast BM25 for exact nuclei, authors, DOI, citation keys, band
   names, and terms.
3. Use QMD `vsearch` for mechanisms, near-synonyms, or concept questions missed
   by keywords; reserve full `query` for high-value cross-page synthesis.
4. Treat snippets and rankings only as candidate selectors. Do not repeat
   retrieval without expected information gain or scan the whole repo/raw for
   ordinary questions.
5. A Wiki miss means missing personal context, not missing field knowledge.

QMD uses one collection for `knowledge/**/*.md`. Before opening ordinary-Q&A
candidates, discard paths under `knowledge/research-notes/` or pages with
`type: research-note`. Research-task use of a note must also open its grounded
sources; ranking or the note text alone cannot establish a fact.

A source page is enough in ordinary mode when identity and locator are clear,
wording is adequate for the question, no material conflict is known, and no
quotation or manuscript judgment is requested. Do not mechanically reread raw.
Use raw or an external direct source for precise data/formulas/locators,
quotations, weak attribution, conflict, controversy dependent on exact wording,
secondary-summary checks, or manuscript/formal-citation use.

## Evidence, review status, and provenance

Keep six statement classes distinct: experimental fact, experimental criterion,
author interpretation, model result, Codex/our provisional inference, and
cross-source synthesis judgment. Also distinguish Wiki-grounded, externally
verified, general-background, and synthesis/inference provenance when it affects
reliability. Do not force these categories into headings in every answer.

Never invent citations, DOI, data, uncertainty, page/figure/table/equation
numbers, locators, quotations, or author wording. Do not turn snippets, model
memory, or synthesis into a paper's direct conclusion. For competing structural
interpretations, inspect both support and serious alternatives.

Review status, needs_review, and human-review history are historical annotations only.
They must not affect ranking, confidence, verification priority, uncertainty disclosure,
wording strength, knowledge promotion, manuscript use, publication, or requests for
user confirmation. Determine all scientific judgments from direct evidence, source
independence, uncertainty, applicability, and competing explanations.

Apply this knowledge-growth loop to reviewed and unreviewed material:

1. Discover relevant content and rank it by relevance, information gain,
   possible impact on the answer, and verification value, not by a simple
   reviewed/unreviewed split.
2. Surface highly relevant material that may add evidence, change an answer,
   expose an omission, or provide a serious alternative. Do not wait for the
   user to name a hidden page first.
3. Briefly state what it may contribute, its source/locator evidence, and a
   practical verification path or the most valuable location to check next.
4. If needed, verify the specific claim against its source, raw, or external
   direct source; check wording, locator, data, applicability, claim kind, and
   competing explanations.
5. Determine the supported conclusion and remaining uncertainty autonomously. Enter an update workflow
   only when the user asks to persist changes.

Do not hide potentially useful knowledge merely because it is unreviewed.
Unreviewed material may support ordinary Q&A, research analysis, exploratory
synthesis, explanation and question generation, literature discovery, competing
interpretation discovery, and candidate-evidence discovery. It is not thereby
user-confirmed, fully verified, uncontested, paper-ready, or a substitute for
formal direct-source checking.

Surface only material with meaningful relevance or information gain; do not dump
every unreviewed page or repeat review warnings sentence by sentence.

Human review is valuable but fallible. `human-reviewed` means a user previously
checked a stated scope; it does not guarantee that every claim is permanently
correct, complete, exhaustively extracted, accurately attributed/located, or
immune to new evidence. Recheck and continue mining reviewed material when the
user questions it, new sources conflict, precision or manuscript use requires
it, wording exceeds the reviewed scope, or an old omission/error is suspected.

Page-level review is not claim-by-claim certification. A page may remain
`unreviewed` while a specific claim is directly verified for a specific use;
judge manuscript support from the exact claim, proposed wording, source,
locator, applicability, competing explanations, and use context. Conversely, a
`human-reviewed` page does not remove claim-specific verification when risk or
precision requires it.

Preserve truthful historical annotations; never label Agent self-audit as human review.
Set confidence and verify manuscript claims autonomously from evidence, regardless
of review annotations. Do not wait for user review or treat it as admission.
A claim-specific check applies only to that claim and use context.

Review history only records that a human-review round and scoped user decisions
occurred. An entry neither proves claims correct nor controls whether a source,
page, or claim may be retrieved, discussed, rechecked, corrected, or mined more
deeply. Missing entries do not make knowledge invisible or unusable.

## Escalation and stop conditions

Use **ordinary evidence-calibrated mode** for normal Q&A, research discussion,
comparison, exploratory synthesis, and early drafting. Give the best supported
answer, lower wording strength when evidence is incomplete, expose material
source limits when they matter, and do not refuse useful analysis merely because
paper-grade support is unfinished.

Enter **strict paper-evidence mode** only for manuscript/submission checking,
formal citation, direct quotation/source requests, exact locator review, or key
scientific claim confirmation. Follow `system/paper-evidence-gate.md`; page-level
review status alone neither qualifies nor disqualifies a specific claim.

Retrieve externally when the user asks for sources, links, verification, latest
work, or wider coverage; when the answer depends on precise data, locators, or
experimental conditions; when controversy, conflict, absolute/current claims,
or insufficient confidence make memory unsafe; or when manuscript use requires
direct support. If retrieval is unavailable, say it was not completed and do
not fabricate a source. Do not auto-search stable basic questions.

Stop when:

- a stable background explanation is clear and not precision-dependent;
- a direct fact or author interpretation has sufficient source/locator support
  and no known conflict;
- a method's definition, applicability, and main limit are clear;
- a competing-interpretation answer has checked main support, a serious
  alternative, and the key limitation.

Do not make absolute or current claims from Wiki coverage or memory alone;
retrieve externally or explicitly bound the scope.

Treat `当前知识库未覆盖`, `知识库当前未给出足够出处`, and `外部来源尚未核验`
as routing signals, not automatic refusal. Respect Wiki-only requests; otherwise
use calibrated general background, identify missing attribution/locator, or
expand externally as the question requires.

## Answer scaling

- **Fast:** give the direct answer, the most useful source/provenance entry when
  relevant, and one important limitation if any.
- **Standard:** give a short conclusion, the strongest relevant basis, the main
  limitation or alternative, and a verification path when useful.
- **Deep/strict:** use fuller evidence structure only for multiple claims or
  sources, real controversy, or explicit manuscript review. Use an evidence
  table only when it improves comparison; never force empty sections or a
  suggested follow-up query.

## Read-only boundary

When the user starts an L3/L4 research task, this skill supplies evidence retrieval and provenance discipline but does not force the task back into ordinary read-only Q&A. Route persistence, autonomous hypothesis work and data-analysis state to `system/workflows/autonomous-research.md`, then use ingest/reflect/project rules for writes. Keep ordinary invocations read-only.

Pure Q&A is read-only: do not modify the Wiki or update handoff, log, WIP queue,
Review history, Git commits, or remotes. If resources run low, stop expanding,
return the verified or reliable portion, state the remaining gap, and offer one
concrete verification direction without writing task state.

If the user asks to ingest, persist a correction, update review state, save an
external source, or modify a synthesis, exit this read-only skill and use the
relevant workflow. Before any later `git add`, `git commit`, or `git push`, run
the repository's `check.md` Git preflight; never stage evidence-page LF/CRLF-only
dirty state or restore a file whose ignore-EOL diff is nonzero.
