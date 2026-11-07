# Local literature archive skill maintenance

- This is a repository-owned internal agent adapter. Keep `SKILL.md` concise;
  maintain the operational contract in `system/workflows/local-literature-archive.md`.
- Keep only skill instructions here. Do not add UI metadata, user tutorials,
  originals, catalog snapshots, extracted text, credentials, or private paths.
- The script lives at `system/scripts/local_literature_archive.py`; inspect its
  help before documenting exact flags. Keep optional features explicitly optional.
- Preserve originals and independent learning records. Catalog maintenance does
  not authorize source repairs, raw recovery, BibTeX sync, or get-paper changes.
- Validate frontmatter, relative links, scoped diffs and repository boundaries.
  Report documentation checks separately from unexecuted CLI behavior checks.
