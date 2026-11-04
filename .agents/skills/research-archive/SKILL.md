---
name: research-archive
description: |
  Use when a research source, thesis, note, dataset, figure, web snapshot, private analysis input, or other evidence must be saved for later retrieval; trigger on “留档”, “归档”, “存到 raw”, “保存原文/图片/数据”, “可复现”, “哈希”, “source-to-raw”, or when creating a knowledge source that depends on a local file.
metadata:
  openclaw:
    emoji: 🗃️
---

# research-archive — 研究材料留档门

## Purpose

Every durable research claim needs a durable local artifact. `knowledge/` explains
what was learned; `raw/` preserves the material that can be checked again.
Keeping these layers separate prevents a later summary from silently replacing
the source.

## Workflow

1. Choose a stable `raw/` destination before downloading or generating a
   source-dependent artifact.
   - Papers: `raw/papers/gpt/learning-daily/<date>-<topic>/`
   - On-demand answer or paper-review acquisition: `raw/papers/gpt/query/<date>-<topic>/`.
     This is separate from the `learning-daily/` directory reserved for the 30-day study plan.
   - Theses: `raw/theses/gpt/learning-daily/<date>-<topic>/`
   - Imported notes and reports: `raw/notes/gpt/learning-daily/` and `raw/reports/gpt/learning-daily/`.
   - Figures and their companion web snapshots: `raw/figures/gpt/learning-daily/<date>-<topic>/`.
   - User datasets: keep the user-defined path under `raw/data/`
   - Personal documents: keep the existing `raw/personal/` structure.
2. Preserve the original bytes. Do not overwrite a file with the same name.
   If a destination exists, compare hashes and use a new versioned filename or
   record the identity as an exact duplicate.
3. Create a sibling `manifest.json` for a downloaded or generated collection.
   Set `archive_type: research-archive-v1` and a timezone-qualified actual
   `retrieved_at`. Each entry contains `path`, `sha256`, and `url` or a local
   `source` description; record `size` when known. The manifest is the archive
   index. For sources acquired while answering a question or checking a
   manuscript, also record `acquisition_context`, `learning_candidate`,
   `learning_topic`, and `collection_reason` when the source should be retained
   for a later topic-level study.
4. In the corresponding `knowledge/sources/*.md`, set `raw_file` to the
   archived path and set `raw_sha256` for a single-file source. For a
   collection, point `raw_file` to its manifest, record the manifest's own
   `raw_sha256`, and cite exact file entries in the notes.
   For newly registered sources also set `archive_required: true`; these
   sources are rechecked even after their Markdown page is committed.
5. Run the archive gate before claiming the source was ingested:

   ```bash
   python3 system/scripts/wiki_archive_gate.py check --root . -- path/to/source.md path/to/manifest.json
   ```

   For a final repository check:

   ```bash
   python3 system/scripts/wiki_archive_gate.py check --root . --full
   ```

   The normal bounded publication check is `check --root . --changed`.
   It runs automatically through `wiki_automation_preflight.py`, which the
   daily runner and Git publication helper already call, and through the
   explicit `after-edit` and `session-summary` lifecycle checks.

6. If the gate fails, report the missing path or hash mismatch and keep the
   source at its evidence boundary. Do not replace a missing artifact with a
   URL-only citation.

## Query and writing behavior

When an external source is materially useful but absent from the Wiki, the
agent may acquire it through a lawful, configured route without waiting for a
separate per-paper instruction. The source must enter
`raw/papers/gpt/query/YYYYMMDD-<topic>/`, be hash-registered, and remain
distinguishable from a source that was actually read and synthesized.
`learning_candidate: true` queues the source for future batch learning; it does
not claim that the paper has been read, reviewed, or promoted to `knowledge/`.

## Required source-page shape

```yaml
raw_file: "raw/papers/example.pdf"
raw_sha256: "<sha256>"
raw_storage_status: archived-local
archive_required: true
```

The source page must also preserve the original URL or citation and explain
what was actually read. A local snapshot does not make an external result
independent evidence.

## Failure handling

- Missing raw file: stop at access/readiness boundary and leave `needs_review: true`.
- Hash mismatch: treat the artifact as a new version; do not silently update the
  source page's hash.
- URL-only source: it may support a search lead, but it does not satisfy the
  local archive requirement.
- Private data: preserve it under `raw/`; keep unpublished analyses and derived
  observables local as well. Publication needs separate authorization for the
  actual content. Generic methods and explicitly sanitized provenance may be
  used in publishable documentation.

## Validation

The canonical repository rule is `system/workflows/research-archive.md`.
The deterministic implementation is
`system/scripts/wiki_archive_gate.py`. The lifecycle hook runs the same gate
for changed source pages and manifests; the skill supplies the behavior when
the work is performed outside the explicit hook commands.

This gate checks registered files, source pages and manifests. It cannot
discover unrecorded browser downloads or prove that every material ever read
has been declared. Every research unit must register the materials it uses;
imported original notes are archived in `raw/notes/`, while newly authored
durable analysis remains in `knowledge/`.
