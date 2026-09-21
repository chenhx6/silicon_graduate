---
type: source
title: "Coriolis effects and rotation alignment in nuclei"
aliases: ["Stephens 1975 Coriolis effects", "Coriolis rotation alignment review"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: review
reading_depth: deep-read
title_original: "Coriolis effects and rotation alignment in nuclei"
authors: ["F. S. Stephens"]
journal: "Reviews of Modern Physics"
year: 1975
volume: 47
issue: 1
pages: "43-64"
doi: "10.1103/RevModPhys.47.43"
citation_key: Stephens_1975
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
language: en
canonical_source: "Stephens, F. S. Coriolis effects and rotation alignment in nuclei. Rev. Mod. Phys. 47, 43-64 (1975)."
library_file: "raw/papers/gpt/high-spin-20260920/转动/1975_Stephens_Coriolis effects and rotation alignment in nuclei.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/转动/1975_Stephens_Coriolis effects and rotation alignment in nuclei.pdf"
raw_sha256: "25369cc4420667d6c38c52d5e6e5a489b48431aaa709998c4743f92ab5049ac3"
nuclei: ["182W", "235U", "rare-earth odd-mass nuclei", "A≈130 context"]
models: ["particle-rotor-model", "cranked-shell-model", "Nilsson-model"]
observables: ["rotation-alignment", "backbending", "signature-splitting", "band-crossing", "moments-of-inertia"]
methods: ["angular-momentum-alignment", "rotational-band-analysis"]
tags: [Coriolis-coupling, rotation-alignment, backbending, band-crossing, review, rare-earth]
---

# Coriolis effects and rotation alignment in nuclei

## Bibliographic Record

- 作者：F. S. Stephens。
- 期刊：*Reviews of Modern Physics* 47(1), 43-64 (1975)。DOI：`10.1103/RevModPhys.47.43`。
- 原始文件：`raw/papers/gpt/high-spin-20260920/转动/1975_Stephens_Coriolis effects and rotation alignment in nuclei.pdf`；SHA-256：`25369cc4420667d6c38c52d5e6e5a489b48431aaa709998c4743f92ab5049ac3`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.43-64 全文；Coriolis Hamiltonian、`182W` 两带混合、`235U` 多带、奇质量 Er、弱形变核、偶偶核 rotation alignment、backbending、模型比较和结论均已阅读。
- Not covered: cited papers and later cranked-shell/particle-rotor developments。
- Coverage caveats: review uses axial particle-plus-rotor/CSM language and historical notation; later triaxial/TPSM interpretations require separate sources。

## Paper Question and Scientific Motivation

- 综述问题是 Coriolis coupling 如何从小扰动演化为显著的 band mixing、rotation alignment、signature behavior 和 backbending（PDF pp.43-44）。
- 估算 `E_Coriolis(max)~2(ħ²/2J)Ij`：稀土区 `j≈13/2`、中等 `I` 时可达约 `0.5 MeV`，因此不能把 Coriolis 作用当成总是微扰。

## Method and Design Logic

- 以变形轴对称 core 与粒子耦合的 particle-rotor Hamiltonian 为起点，把总角动量写为 `R=I−j`，Coriolis term 连接相邻 `K` bands。
- 低影响情形用带混合/扰动处理；高自旋或弱耦合情形用多带混合、rotation-alignment 和 cranked-shell descriptions 比较。
- 综述用 `182W` 两带、`235U` 多带、奇质量 Er 和偶偶/odd-mass backbending 例子建立从解析模型到系统学的路径。

## Key Evidence and Reasoning Chain

1. Coriolis matrix elements increase with spin, particle `j` and rotational frequency, while level spacing and moment of inertia set the perturbative boundary（PDF pp.43-48）。
2. `182W` demonstrates two-band Coriolis mixing; fitted level repulsion can reproduce spectra but parameters are not unique because vibrational admixtures and additional Nilsson states can mimic effects（PDF pp.44-48）。
3. `235U` and odd-mass Er examples show large-j orbitals and alignment change rotational spacings, signature dependence and band crossings（PDF §§II-III）。
4. Even-even rotation alignment/backbending is described as a two-quasiparticle alignment phenomenon; odd-mass backbending depends on particle-core coupling and blocking（PDF §IV）。
5. The review treats deformation, pairing and residual interactions as coupled causes; it does not support assigning every crossing to a single Coriolis mechanism（PDF §§III-V）。

## Summary

Stephens' review supplies the historical physical map from Coriolis coupling to rotation alignment, band mixing and backbending. It is valuable as a model and terminology anchor, but its axial particle-rotor/CSM examples do not by themselves settle later γ-soft, triaxial, wobbling or chiral interpretations.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST75-1 | Coriolis energy grows with `Ij(ħ²/2J)` and can become comparable to level spacings in rare-earth nuclei. | model-principle | direct | PDF pp.43-44, Eq.(1) | false |
| ST75-2 | Coriolis coupling mixes neighboring K bands and produces level repulsion, alignment and signature effects. | review-synthesis | direct | PDF §§II-III | false |
| ST75-3 | Backbending is linked to rotational alignment of high-j quasiparticles, with blocking and pairing modifying odd-mass cases. | review-synthesis | direct | PDF §IV | true |
| ST75-4 | Historical fits can reproduce spectra while leaving deformation/vibrational/extra-orbital parameter ambiguity. | limitation | direct | PDF pp.44-48 | false |

## Nuclear Structure Information

- `182W`, `235U`, odd-mass Er and even-even/odd-mass rare-earth cases are examples; no new single-nucleus source page created。

## Competing Interpretations and Limitations

- A band crossing can reflect Coriolis mixing, quasiparticle alignment, deformation change, pairing change or residual interactions; the review itself shows parameter non-uniqueness。
- Axial particle-rotor language does not establish triaxiality, γ-softness, wobbling or chirality。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-ST75-1 | Core reconstruction | Coriolis coupling is a mechanism linking single-particle angular momentum to collective rotational response; its observable fingerprints are shared by several competing models. | PDF §§I-V | self-checking |
| AR-ST75-2 | Transfer conditions | Use formulas and alignment logic as background; transfer of numerical crossing shifts requires matched deformation/pairing/reference parameters. | PDF §§II-IV | provisional |
| AR-ST75-3 | Failure conditions | Assigning a crossing to Coriolis alone without blocking/pairing/deformation controls is underdetermined. | PDF §§III-V | active-L3 |
| AR-ST75-4 | Research-question decision | Link to alignment/backbending model pages; no L4. | PDF §§III-IV | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki already has angular-momentum alignment, backbending, cranked-shell and high-spin background pages; this source supplies a historical mechanism review and explicit parameter ambiguity。
- Effect of this source: `foundational-background` and `limits`。
- Persistence decision: update [[angular-momentum-alignment]] and [[backbending]] source lists。
- Review state: `unreviewed`; review claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[angular-momentum-alignment]] | Coriolis coupling and quasiparticle alignment mechanism。 |
| foundational-background | [[backbending]] | Historical rotation-alignment interpretation and odd-mass blocking boundary。 |
| limits | [[triaxial-deformation]] | Axial review examples cannot independently establish triaxial geometry。 |

## Human Review Triage

### P0

- ST75-P0-1：不要把综述中的历史机制解释写成具体核素实验的唯一归因。

### P1

- ST75-P1-1：跨到 A≈130 或现代 wobbling/chirality 任务时，需补充后续模型和直接观测 source。

### P2/P3

- DOI、页码和章节结构已由 PDF metadata/正文核对。

## Extracted Pages

- Nuclei: no standalone pages。
- Bands: no standalone pages。
- Concepts: [[angular-momentum-alignment]], [[backbending]], [[high-spin-phenomena]]。
- Models: [[cranked-shell-model]], [[particle-rotor-model]]。
