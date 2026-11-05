# Wiki project skills

These skills are repository-local adapters for the Wiki. They must keep research
artifacts inside the path contract, use `tmp/` for transient runs, and avoid
credentials, private data, automatic hooks, and external configuration changes.

External skills require a fixed source commit, license evidence, provenance record,
offline tests, `git diff --check`, and the relevant Wiki boundary/lint checks.
The root `AGENTS.md` and the skill's own `SKILL.md` remain the governing rules.
