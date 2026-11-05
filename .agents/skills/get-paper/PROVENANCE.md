# get-paper provenance

- Upstream: `https://gitlab.itp.ac.cn/ZhangXin8069/configure`
- Fixed ref: `main` at `57285cef243414ac1c84363a7d49bc732fb822e9`
- Upstream path: `skills/get-paper/`
- License: MIT, copyright ZhangXin8069 (2024); the local `LICENSE` preserves the
  upstream notice.
- Upstream root `LICENSE` SHA-256: `eeb4836b85b7eaa017b5ee8da966aa912999c52231b7b50ec571890b215871ab`.
- Upstream file hashes at the fixed ref:
  - `AGENTS.md`: `f7d2db2dcd6a054ff559bcfc391ff69059371af91f842d6d54b780f302e3b514`
  - `SKILL.md`: `7849fbac1f20b5b4073e53e4924e7b907d4ae064ad516a23318a427048bcf732`
  - `references/sources.md`: `9de497252c3912ddd26d3b2bce810b939d8101085865a835ddce13e6e3c35cfa`
  - `scripts/get-paper.py`: `5edf07c720238bf87eee80ae2ca6b5644999afff09377920d4bb82cef9a588b3`
  - `scripts/test_get_paper.py`: `7f6eb0c9a68ba6485ffc2bcb02c709bdeb57869088956ae7ae35107468fbe59`

The local adapter preserves the standard-library implementation and offline tests.
It changes the user agent to `wiki-get-paper/1.0`, points transient runs to
`tmp/runs/get-paper/`, and adds Wiki-specific instructions for
`raw/papers/gpt/query/` manifests and the archive gate. It does not add API keys,
download private material, bypass access controls, or execute paper contents.
