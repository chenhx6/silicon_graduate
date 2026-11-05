# absorb provenance

- Upstream: `https://gitlab.itp.ac.cn/ZhangXin8069/configure`
- Fixed ref: `main` at `57285cef243414ac1c84363a7d49bc732fb822e9`
- Upstream path: `skills/absorb/`
- License: MIT, copyright ZhangXin8069 (2024); the local `LICENSE` preserves the
  upstream notice.
- Upstream root `LICENSE` SHA-256: `eeb4836b85b7eaa017b5ee8da966aa912999c52231b7b50ec571890b215871ab`.
- Upstream file hashes at the fixed ref:
  - `AGENTS.md`: `7cb8a9fbab57a0649ec8664a895e7964a789d17d3a54917461b7d39f57227aec`
  - `SKILL.md`: `9461ff7eaee32f4e5f0e824402605a87304e31f29d2ab7eab3597a10f3eb1931`
  - `references/sources.md`: `6eb1b51369b54b99606091b8b5040f4776ba161ecc835dcd9e8d5e8f8ce166e9`
  - `scripts/absorb_inventory.py`: `77da233e3c205860d3a7566eb8be2acc3102b58c73e67015869dcab785c9ed9c`
  - `scripts/test_absorb_inventory.py`: `4faa919c5a424c8089d0cc817bf00867dce4c0533bc237eeea7947792ab5645c`

The local adapter preserves the inventory algorithm and offline tests. It points
runtime inventories to `tmp/runs/absorb/` and replaces upstream project-specific
verification commands with Wiki boundary and lint checks. It does not enable
external hooks, installers, background services, credentials, or destructive
operations.
