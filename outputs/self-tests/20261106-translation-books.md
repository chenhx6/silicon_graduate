# translation-books creation and validation

Date: 2026-11-06. Scope: create a portable book-translation skill from the successful
workflow, with optional nuclear-physics guidance. No book was retranslated or modified.

## Maintained and installed packages

- Canonical Wiki package: `.agents/skills/translation-books/`.
- Shared installation: `/root/.agents/skills/translation-books/`.
- Both contain 11 identical files, verified by relative-path/SHA-256 manifests.
- Shared Git checkpointing belongs to the existing shared-library sync service.
  This task does not change that service or its settings.

The package includes concise instructions, three supporting references, a compilable
A4 LaTeX template, read-only tool/dependency inventory, PDF inspection/contact-sheet
helper, interface metadata, maintenance instructions, and three behavioral scenarios.
No book-specific title, absolute project path, translator address, or acknowledgment
was copied into it.

## Executed validation

- Skill structure validation passed for both installations.
- Both Python helpers passed syntax compilation; relative Markdown references resolve.
- Preflight succeeded with an explicitly located installed TeX engine and reviewer.
- Missing reviewer and missing source were detected.
- A different installed reviewer was not selected silently; an explicit selection succeeded.
- Missing TeX engine on PATH was detected. No tools or language skills were installed.
- The supplied template compiled with the existing Tectonic executable into five A4 pages.
  Font embedding, title metadata, three bookmark levels, actual internal links and build log
  passed the PDF helper. Whole-template contact sheet and enlarged body page were viewed.
- An intentionally defective PDF/log fixture was rejected for wrong dimensions,
  missing title, missing bookmarks, unembedded font and build errors.
- A rotated A4 test page was accepted and separately flagged for intended-use review.
- The existing 472-page integrated book was inspected read-only as a regression example:
  mechanical checks passed. Raster-DPI hints remain warnings, not assertions of faulty
  crops or a new visual review. Translation fidelity and scientific content were not
  re-audited in this skill-creation task.
- Wiki boundary check passed.

Internal fixtures, build logs, machine reports and hash manifests are under
`tmp/translation-books-validation/`; the reusable implementation is entirely in the
skill package, so those temporary files are not required for future use.

## Independent behavioral review

One independent agent walked through three scenarios: a chemistry project with a
missing reviewer, a nuclear book with contextual terminology, and multi-edition
integration with historical deliverables/personal details. This was instruction and
code review, not execution of three full translations or measured activation testing.

Two findings were corrected: integration now tracks removed/superseded material and
unresolved inclusion policy; the PDF helper accepts landscape A4 pages for wide tables.
Draft translation is explicitly allowed to continue while a reviewer choice is pending.

## Publication isolation

The initial working tree already contained unrelated research changes. Full working-tree
lint reported five errors in two untracked Ba129 research pages: missing index links,
duplicate canonical source, missing year, and unsupported reading-depth value.
They were not changed or included in this task.
Whole-working-tree `git diff --check` also reported existing trailing whitespace in
`PLAN.md`; the task's staged files are checked independently.

The skill files are selected explicitly for publication. A separate lint check uses
tracked HEAD knowledge/governance plus this skill, with local raw evidence accessible
read-only: it passed with zero errors and 369 existing warnings. Exact publication result and commit are recorded in
`20261106-translation-books-receipt.json`.
