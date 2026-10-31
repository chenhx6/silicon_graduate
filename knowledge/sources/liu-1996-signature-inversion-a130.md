---
type: source
title: "Liu et al. 1996 - Spin assignments and signature inversion of pi h11/2 times nu h11/2 bands"
aliases: [Liu 1996 signature inversion A130]
created: 2026-09-21
updated: 2026-10-05
status: ai-draft
review_status: unreviewed
source_type: systematics-and-particle-triaxial-rotor-comparison
reading_depth: deep-read
title_original: "Systematic study of spin assignments and signature inversion of πh11/2⊗νh11/2 bands in doubly odd nuclei around A≈130"
authors: [Yunzuo Liu, Jingbin Lu, Yingjun Ma, Shangui Zhou, Hua Zheng]
journal: "Physical Review C"
year: 1996
volume: 54
pages: "719-730"
doi: "10.1103/PhysRevC.54.719"
citation_key: Liu_1996
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Liu et al., Phys. Rev. C 54, 719-730 (1996)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/旋称/1996_Liu et al_Systematic study of spin assignments and signature inversion of π h 1 1 - 2 ⊗ν.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/旋称/1996_Liu et al_Systematic study of spin assignments and signature inversion of π h 1 1 - 2 ⊗ν.pdf"
raw_sha256: "ca3e1c1bc834158112dee525fa4c42c3d44596975a506f3a2a1da023580a346f"
nuclei: [120Cs, 122Cs, 124Cs, 126Cs, 128Cs, 130Cs, 124La, 126La, 128La, 130La, 132La, 134La, 130Pr, 132Pr, 134Pr, 136Pr, 134Pm, 136Pm, 138Pm, 138Eu]
reactions: [compiled-literature-systematics]
experiments: [band-systematics]
models: [particle-triaxial-rotor, Semmes-Ragnarsson-residual-interaction]
observables: [signature-inversion, excitation-energy-systematics, spin-assignment, signature-splitting]
methods: [level-scheme-crosswalk, isotopic-systematics]
tags: [signature-inversion, A130, h11/2, spin-assignment, triaxial-rotor]
---

# Signature inversion in `πh11/2⊗νh11/2` bands around A≈130

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

- Y. Liu *et al.*, *Phys. Rev. C* **54**, 719–730 (1996), DOI `10.1103/PhysRevC.54.719`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/旋称/1996_Liu et al_Systematic study of spin assignments and signature inversion of π h 1 1 - 2 ⊗ν.pdf`。

## Scope and Reading Depth

- PDF pp.719–730 (12 pages) fully read: excitation-energy systematics, revised `I0` assignments for La/Pr/Pm/Eu/Cs chains, Table I/II, signature-inversion plots, comparison with particle–triaxial-rotor calculations and conclusions.
- Not covered: primary spectroscopy papers cited for each isotope and later reassessments.

## Key Results

- The authors revise many lowest observed spins `I0` in `πh11/2⊗νh11/2` bands by requiring smooth excitation-energy systematics across isotopic/isotonic chains. For La/Pr/Pm/Eu, most previously assigned `I0=8` values shift to 7 or 9; Cs admits competing reference choices (`124Cs I0=7`, `130Cs I0=9` or 11) that cannot both be correct (PDF pp.719–725, Tables I–II, Figs.1–14).
- With the revised assignments, all discussed A≈130 doubly odd nuclei show low-spin signature inversion. The inversion spin increases with neutron number in Cs and La isotopes (PDF pp.728–729, Fig.15).
- Particle–triaxial-rotor calculations with a Semmes–Ragnarsson zero-range p–n interaction reproduce the inverted signatures and inversion-spin trend when the revised spin assignments are used (PDF pp.729–730, Tables I–II).
- The paper warns that prior conclusions about equilibrium γ deformation can reverse sign if the bandhead spin is wrong by an odd integer; Cs spin assignments remain unresolved pending new data (PDF pp.728–730).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LU96-1 | Smooth excitation-energy systematics motivate revised bandhead spin assignments across A≈130 chains. | systematics-result | mixed | PDF pp.719–725, Tables I–II | true |
| LU96-2 | Revised assignments make low-spin signature inversion systematic in the discussed `πh11/2⊗νh11/2` bands. | systematics-result | mixed | PDF pp.728–729, Fig.15 | true |
| LU96-3 | Particle–triaxial-rotor calculations agree with inversion trends only after the revised spin crosswalk. | model-comparison | mixed | PDF pp.729–730 | true |
| LU96-4 | Cs reference assignments remain mutually incompatible/undetermined. | unresolved-boundary | direct | PDF pp.723–730, Tables II | false |
| LU96-5 | The agreement of Tajima's Cs inversion-spin calculation with the `124Cs I0=7` reference is not independent validation of that spin anchor: the model parameters were fitted to the same `124Cs` band using `I0=7`. | model-dependence-boundary | direct | PDF p.729, Sec. VI.C | true |

## Summary

Liu *et al.* show that signature-inversion systematics and spin assignments are coupled: changing a bandhead by an odd `ΔI` can reverse the inferred signature order and the inferred γ-deformation discussion. The source is a cautionary crosswalk rather than a direct new spectroscopy experiment.

## Competing Interpretations and Limitations

- The method assumes smooth level-energy trends and similarity of band structures across isotopic/isotonic chains; this is a model/systematics prior, not an independent spin measurement.
- Cs chains have insufficient mutually consistent anchors; the paper presents alternatives rather than a final assignment.
- Particle–triaxial-rotor agreement depends on fitted parameters and the revised spin choices; it does not uniquely establish a triaxial shape.
- Tajima's calculated `I_inv` values agree with the Cs systematics based on `124Cs I0=7`, but the paper states that the calculation parameters were fitted to that same `124Cs` band and spin assignment (PDF p.729, Sec. VI.C); this agreement is not an independent spin anchor.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| LU96-AR-1 | Crosswalk chain | Literature level schemes → common reference spin → smooth excitation curves → revised `I0`/signature labels. | PDF Figs.1–14, Tables I–II | self-checking |
| LU96-AR-2 | Interpretation chain | Revised signature order → inversion spin trend → particle–triaxial-rotor comparison; preserve unresolved Cs alternatives. | PDF Fig.15 and Secs.V–VI | self-checking |
| LU96-AR-3 | Transfer condition | No direct δ/lifetime input; do not transfer γ-shape inference to `131Ba/131Ce` without nucleus-specific assignments. | PDF conclusion | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[signature-inversion]], [[signature-partner-bands]], [[triaxial-deformation]], [[multipole-mixing-ratio]] and A≈130 spin-assignment audit.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `LU96-P0-1`: Preserve the spin-crosswalk prior and unresolved Cs assignments; do not use revised signature inversion as direct γ-deformation evidence.

## Extracted Pages

- Concepts: [[signature-inversion]], [[signature-partner-bands]], [[triaxial-deformation]]。

## Day21周考推断阶梯审计：A≈130 奇奇核旋称反转与自旋奇偶对调证据门边界

依据独立审计程序 `system/scripts/day21_checkpoint013_signature_inversion_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/signature-inversion-audit-013.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LU96-D21-1 | Liu 1996 系统学与微观模型确立 A≈130 奇奇核旋称反转推断阶梯边界：(1) 带头自旋指认依赖性：旋称量子数遵循 $lpha = I mod 2$，带头自旋 $I_0$ 的 $1\hbar$ 微调（如由 8 调至 9）会彻底对调 favored 与 unfavored 枝，使所谓“反转”完全受制于自旋交叉对账；(2) 玻尔—莫特森三轴形变非排他性：在严格轴对称长椭形变（$\gamma = 0^\circ$）下，Semmes-Ragnarsson 零程残余质子—中子（$p-n$）相互作用（$\Delta E_{pn} \sim 80	ext{ keV}$）足以在低自旋压低 unfavored 态，直到角动量增大到科里奥利退耦能克服 $p-n$ 势垒（$I_{	ext{inv}} pprox 12 - 16\hbar$）才恢复正常能序；(3) 翻转自旋随中子数线性增长（斜率达 $0.83\hbar/	ext{中子}$）反映了 $
u h_{11/2}$ 壳层的逐渐填充。推断阶梯确立：严禁仅凭低自旋旋称反转断言负 $\gamma$ 三轴形变，确证反转与微观机制必须依赖绝对带头自旋测定与排他性模型对照。 | claim-boundary-audit | direct-and-derived | PRC 54, 719 pp.719-730; signature-inversion-audit-013.json | true |
