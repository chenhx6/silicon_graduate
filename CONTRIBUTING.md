# Contributing

Contributions are welcome through focused pull requests.

The canonical repository is [Gitee `chx6/silicon_graduate`](https://gitee.com/chx6/silicon_graduate). GitHub, if present, is a mirror and is not maintained directly.

## Workflow

1. Fork the repository.
2. Make a focused change in your fork.
3. Preserve the existing directory structure, front matter, citation keys,
   and provenance.
4. Run the available checks.
5. Open a pull request on Gitee describing the change and its evidence.

Making the repository public does not grant direct write access to the
maintainer's `main` branch.

## Evidence and citations

Clearly distinguish:

- facts directly reported by a source;
- source-author interpretations;
- model or calculation results;
- cross-source synthesis;
- your own inference or working hypothesis.

Use existing citation keys when available. New references should include
verifiable bibliographic information and, where practical, a page,
section, figure, table, or equation locator.

Do not fabricate citations, identifiers, locators, quotations, or data.

## Repository boundaries

Do not submit:

- publisher PDF full texts or unauthorized book contents;
- unauthorized third-party images or datasets;
- credentials, tokens, passwords, private keys, or private data;
- unrelated bulk reformatting;
- unreviewed mass rewrites of `raw/zotero/wiki-inbox.bib`.

The bibliography snapshot is maintained by the repository owner.
Citation-key changes must be checked against all Wiki references.

See [`DISCLAIMER.md`](DISCLAIMER.md) for research-use and safety
limitations.

## Checks

Run when applicable:

```powershell
git diff --check
python system/scripts/wiki_lint.py --fail-on error
```
