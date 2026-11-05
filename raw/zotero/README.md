# Wiki BibTeX store

- `wiki-auto-generated.bib` — 由 `system/scripts/wiki_citation_key.py export` 从 `knowledge/sources/` 自动生成。包含全部 source 页的 BibTeX 条目，citation key 格式为 `firstauthor_year_shortkeyword`。每次更新后 commit/push，方便远端拉取后直接用于 LaTeX 编译。
- `gpt.bib` — 历史遗留，已被 `wiki-auto-generated.bib` 取代。
- `wiki-inbox.bib` — 已废弃并清理。

不要把 `zotero.sqlite`、登录凭据、Cookie、token 或个人联系信息放入此目录。
