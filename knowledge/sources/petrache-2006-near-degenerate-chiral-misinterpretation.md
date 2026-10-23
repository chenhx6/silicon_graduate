---
type: source
title: "Petrache et al. 2006 - Risk of misinterpretation of nearly degenerate pair bands as chiral partners"
aliases: [Petrache 2006 chiral-band caution]
created: 2026-09-21
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
source_type: critical-analysis-and-model
reading_depth: deep-read
title_original: "Risk of Misinterpretation of Nearly Degenerate Pair Bands as Chiral Partners in Nuclei"
authors: [C. M. Petrache, G. B. Hagemann, I. Hamamoto, K. Starosta]
journal: "Physical Review Letters"
year: 2006
volume: 96
pages: "112502"
doi: "10.1103/PhysRevLett.96.112502"
citation_key: Petrache_2006
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevLett.96.112502"
library_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2006_Petrache et al_Risk of Misinterpretation of Nearly Degenerate Pair Bands as Chiral Partners in.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2006_Petrache et al_Risk of Misinterpretation of Nearly Degenerate Pair Bands as Chiral Partners in.pdf"
raw_sha256: "ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f"
nuclei: [134Pr, 136Pm]
reactions: [literature-systematics, band-crossing-analysis]
experiments: [134Pr-transition-probabilities]
models: [band-mixing, ultimate-cranking, total-routhian-surface]
observables: [B(E2), quadrupole-moment-ratio, alignment, signature-staggering, band-degeneracy]
methods: [critical-analysis, energy-systematics, transition-strength-analysis]
tags: [chirality, counterexample, band-mixing, A130]
---

# Risk of misinterpretation of nearly degenerate pair bands as chiral partners

## Bibliographic Record

- C. M. Petrache *et al.*, *Phys. Rev. Lett.* **96**, 112502 (2006), DOI `10.1103/PhysRevLett.96.112502`.

## Scope and Reading Depth

- The four-page PRL was read end-to-end, including Figs.1–3, Eqs.(1–5), Table I, `134Pr` and `136Pm` systematics, potential-energy surfaces and the conclusion.

## Core Argument

The paper tests whether near-degenerate same-parity `ΔI=1` bands in the `N=75` isotones are genuinely chiral. It argues that ideal chiral partners should have not only similar energies but also similar alignments, shapes and electromagnetic transition probabilities (PDF p.1). In `134Pr`, several 4-qp crossings compress the yrast/yrare separation over `13<I<19`; the energy near-degeneracy therefore does not by itself identify a chiral regime (pp.1–2, Fig.1).

For the `I=14–18` region the alignment difference is about `2ℏ` and the observed 15/16 energy splittings imply an interaction `|V|<18 keV`. Using a two-band mixing wave function (Eqs.1–3) and measured in/out E2 branching ratios, the authors obtain `|V|≈14–17 keV` and `Q0,1/Q0,2=2.0(4)` (pp.2–3, Table I). The ratio is far larger than the `~1.25` expected from the cited UC shape minima, and even the TRS comparison gives only `~1.7`; the bands therefore have substantially different intrinsic shapes.

The `136Pm` pair shows different signature staggering and disappears at different 4-qp crossings; the available data are likewise not favorable to a chiral assignment, although transition-probability measurements are required for a decisive test (p.4, Fig.4).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE06-1 | Several crossings can mimic a near-degenerate `134Pr` pair over a finite spin range. | counter-evidence | direct | PDF pp.1–2, Fig.1 | true |
| PE06-2 | `Q0,1/Q0,2=2.0(4)` and alignment differences disfavor ideal chiral partners. | derived-observable | mixed | PDF pp.2–3, Table I | true |
| PE06-3 | `136Pm` signature/crossing behavior is not favorable to chirality but needs electromagnetic tests. | evidence-boundary | direct | PDF p.4, Fig.4 | true |

## Summary

Petrache *et al.* establish a reusable critical test: near-degeneracy is necessary at most, while shape, alignment and transition-strength equality must be checked explicitly.

## Competing Interpretations and Limitations

- The `Q0` ratio is obtained through a simplified two-band mixing model and depends on the adopted branching data.
- The analysis critiques the ideal-pair interpretation of these cases; it does not prove that all future near-degenerate pairs are nonchiral.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| PE06-AR-1 | Degeneracy mechanism | Crossings can mimic a near-degenerate pair over a finite spin interval; energy spacing is not a chiral observable by itself. | PDF pp.1–2, Fig.1 | self-checking |
| PE06-AR-2 | Shape inference | `Q0` ratio is extracted through a two-band mixing model and measured E2 branches; it is stronger evidence than a visual level-spacing argument but remains assumption-dependent. | PDF pp.2–3, Eqs.1–5, Table I | self-checking |
| PE06-AR-3 | Transfer boundary | The critique supplies a necessary-condition test for candidate chirality, not a universal claim that every near-degenerate pair is nonchiral. | PDF pp.1–4 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `limits` energy-degeneracy-only claims in [[nuclear-chirality-and-multiple-chiral-doublet-bands]], and provides a direct counterexample to compare with HS-083/HS-119/HS-012.
- L3 question: for each candidate pair, can partner-resolved `B(E2)`, `B(M1)` and alignment data reject crossing/shape-coexistence alternatives before a chiral label is retained?
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `PE06-P0-1`: Do not promote near-degeneracy to chirality without transition strengths, alignment and band-crossing checks; preserve the two-band-mixing assumptions behind `Q0,1/Q0,2`.

## Extracted Pages

- Project/concept: [[nuclear-chirality-and-multiple-chiral-doublet-bands]], [[signature-inversion]]。

## Day18参照核验：2.0(4)的实际提取链

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE06-D18-1 | 2.0(4)指E2 transition moments的Q0,1/Q0,2；作者以实测E2 out/in分支和ΔE解混合振幅/V/矩比，假定无off-diagonal E2、短spin段V不变。允许范围1.6–2.4是该分析与输入的范围；寿命B的差异只作定性一致性对照，不是这项比值的直接来源，也不能把其转成beta两倍。 | source-derivation-and-lineage-audit | direct-and-boundary | PDF2最后两栏；PDF3 Eqs3–5/TableI及2.0(4)段；PE06-2 | true |

原PE06-1–3及review保持。此次独立worker完整四页文字、PDF2–3视觉；主代理定向原读PDF2–3及PDF3视觉，未重拟合V/Q或原实验CI。联系[[hecht-2001-chiral-symmetry-breaking-136pm-138eu]] HE01-D18-5，明确这是参照而非另两核的新测量。
## Day20量化审计：134Pr两带波函数解混合、四极矩2倍不对称与伪手征证伪（checkpoint030）

> checkpoint032：本节旧认证已撤回；程序通过只曾检自设输入。以下R32为本次定向原读纠正。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PE06-D20-1 | checkpoint032：旧科学认证撤回，原因：Invented gap sequence conflicts with printed36/44keV; chosen V not extracted; arcsin branch ambiguity; allowed1.6-2.4 range not Gaussian; invented128Cs uncertainties; exclusive configuration/handedness labels not established.；当前可用陈述见下方R32原读纠正。 | withdrawn-task-certification | rejected-and-replaced | checkpoint032; PE06-D20-R32-1 | true |

## checkpoint032：原件定位与科学认证纠正

本次Codex self-audit，原review状态与全部已有claim flags保持；不是新增独立实验或全文阅读认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE06-D20-R32-1 | PDF2明确I15/16两态间隙36/44keV；PDF3奇/偶序列V约14/17keV、矩比允许1.6–2.4，TableI α15y=.894、α16ny=.427。旧31keV序列、37.7度等反解认证撤回；振幅需保yrast/nonyrast身份与混合分支。 | literal-model-table-correction | direct-original-and-visual | PDF2 near-gap paragraph; PDF3 Eq3/TableI | true |
| PE06-D20-R32-2 | 2.0(4)来自无off-diagonal E2、短spin段V固定的分支比解混合允许范围；作者用它反对理想手征带解释。未给该范围Gaussian抽样含义，不作z2.5/p.0124或所有手征动力学排除；寿命B仅定性对照。 | range-versus-CI-and-interpretation-boundary | direct-original-and-visual | PDF3 Eqs4–5 and possible-ranges paragraph; PE06-D18-1 | true |


### checkpoint051：两带混合矩阵元与伪简并电磁非对称性审计

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PE06-D20-R51-1 | checkpoint101撤回旧“独立程序严格认证/终极唯一判据”。保留此前原读对36/44keV能隙及作者模型允许Q比1.6–2.4的分层记录；2.0(4)不能改称已知Gaussian测量。两能级模型DeltaE>=2|V|只给条件上限，不独立提取V/混合角。旧alpha/beta标签和过强排他裁决不沿用；矩阵元不对称需连同模型条件、带身份及替代解释讨论。 | withdrawn-overclaim-and-model-boundary | task-boundary-correction | PRL96,112502 TableI; PE06-D20 source corrections; checkpoint101 | true |
### checkpoint142：两带解混合、内禀四极矩双倍不对称与伪手征陷阱审查

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PE06-D20-R142-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |
