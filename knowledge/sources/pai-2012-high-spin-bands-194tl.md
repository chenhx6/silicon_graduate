---
type: source
title: "High-spin band structures in doubly-odd 194Tl"
aliases: [Pai 2012 194Tl INGA bands, 194Tl early i13/2 crossing]
created: 2026-09-30
updated: 2026-09-30
status: active
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: read
title_original: "High spin band structures in doubly-odd 194Tl"
authors: [H. Pai, G. Mukherjee, S. Bhattacharyya, M. R. Gohil, T. Bhattacharjee, C. Bhattacharya, R. Palit, S. Saha, J. Sethi, T. Trivedi, S. Thakur, B. S. Naidu, S. K. Jadav, R. Donthi, A. Goswami, S. Chanda]
journal: Physical Review C
year: 2012
volume: 85
issue: 6
pages: "064313"
doi: 10.1103/PhysRevC.85.064313
arxiv: 1201.6596v2
language: en
canonical_source: doi:10.1103/PhysRevC.85.064313
citation_key: Pai2012_194TlHighSpin
raw_file: "raw/papers/gpt/day4-20260930/194tl-pai-2012/PDFs/Pai-2012-PRC85-064313-194Tl-arXiv-1201.6596v2.pdf"
raw_sha256: 633b068625691c4aeb6200867a9cd8820e6528b9fc19ae1c6ca2a3928fcf7553
source_url: https://arxiv.org/pdf/1201.6596v2
nuclei: [194tl]
reactions: []
experiments: []
models: [cranked-shell-model, routhian]
observables: [gamma-ray-energy, alignment, moment-of-inertia, dco-ratio, linear-polarization]
methods: [gamma-gamma-coincidence, dco-ratio, linear-polarization-asymmetry]
tags: [a190, odd-odd, quasiparticle-crossing, four-quasiparticle]
---

# Pai 等（2012）：`194Tl` 高自旋能带与 crossing

## Bibliographic Record

H. Pai *et al.*, *Phys. Rev. C* **85**, 064313 (2012), DOI `10.1103/PhysRevC.85.064313`; arXiv:1201.6596v2. 公共 arXiv PDF：<https://arxiv.org/pdf/1201.6596v2>。

本地只读来源副本为 12 页、441,074 bytes，SHA-256 `633b068625691c4aeb6200867a9cd8820e6528b9fc19ae1c6ca2a3928fcf7553`；下载日期 2026-09-30，哈希与 arXiv v2 PDF 匹配。

## Scope and Reading Depth

定向阅读 PDF pp.1–2、4–6、8–10、12：检查摘要和反应/装置、Fig.5 能级图、Table I 的相对强度/DCO/IPDCO、Fig.7 alignment、crossing 讨论、B2 寿命与宇称边界，以及 TRS/准粒子 Routhian 模型比较。未逐条复核参考文献，也未检查补充材料。

## Summary

Pai 等的 INGA 数据将 `194Tl` 的 B1 band 延伸到 `18−`，并从能级派生约 `0.34 MeV` 的 alignment gain。作者将其解释为第二对 `νi13/2` neutron alignment，因而把 crossing 前后依次解读为 2qp 与 4qp 结构。B2 的 linking-transition 多极性与宇称仍有歧义，作者指出 `18−` lifetime 是必要 companion observable。该论文为后来的 iThemba 近简并 partner 研究提供了独立的早期能级数据背景。

## Experimental Setup

- 反应为 `185,187Re(13C,xn)`，束能 75 MeV；论文报告 γ–γ 符合测量，使用 INGA 阵列与数字化获取。
- 论文将 B1 的 `293.1-keV`, `8−` 带头及相关跃迁置入 `194Tl` 能级纲图；实验用 γ 能量、符合、相对强度、DCO 和可用时的 IPDCO 约束能带与跃迁指认。
- Pai 的 Re+C / INGA 采集与后来 iThemba 的 `181Ta(18O,5n)` / AFRODITE 数据不同；后续工作延伸了共同的物理带谱系，不能把两篇论文都算作同一观测的独立重复，也不能把它们误作同一批事件。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PAI12-1 | `185,187Re(13C,xn)` at 75 MeV and INGA γ–γ coincidence populated high-spin states in `194Tl`; the paper reports 19 new γ transitions and extends the scheme to 4.1 MeV. | experimental-fact | direct | PDF p.1 abstract and p.2 experimental setup | true |
| PAI12-2 | Negative-parity band B1 is built on the `293.1-keV`, `8−` level and is extended to `18−`; the placements are based on observed γ coincidences and transition data. | experimental-fact | direct | PDF pp.4–6, Fig.5 and associated level-scheme discussion | true |
| PAI12-3 | Fig.7 shows an initial alignment near `5ℏ` and a gain of about `5ℏ` near `ℏω≈0.34 MeV`; the plotted alignment is derived from the level scheme using a Harris reference (`J0=8 ℏ² MeV⁻¹`, `J1=40 ℏ⁴ MeV⁻³`). | derived-observable | derived | PDF p.8, Fig.7 and caption | true |
| PAI12-4 | The authors interpret the `≈0.34-MeV` alignment gain as alignment of a second `νi13/2` neutron pair, the first pair being blocked in odd-odd `194Tl`; they describe B1 as evolving from a 2qp bandhead to a post-crossing 4qp configuration. | author-interpretation | indirect | PDF p.8 crossing discussion; p.10, Fig.13 and quasiparticle-Routhian discussion | true |
| PAI12-5 | For the 761-keV B2→B1 link, DCO is quadrupole-like but IPDCO is unavailable; assuming E2 gives tentative negative parity, while M2 is not excluded. The authors state that the `18−` lifetime is needed to resolve the ambiguity. | evidence-boundary | direct | PDF p.6, B2/B1 linking-transition discussion | true |
| PAI12-6 | B2 has a tentative `18ℏ` bandhead near 3.16 MeV and is described as not well developed; a post-crossing 4qp explanation is proposed from odd-A Tl systematics, not established experimentally. | candidate-interpretation | indirect | PDF p.9, B2 discussion | true |
| PAI12-7 | Table I lists relative γ intensities normalized to the 293.1-keV transition, DCO/IPDCO ratios and multipolarity assignments; it does not report band lifetimes or absolute `B(M1)`/`B(E2)` values. | evidence-boundary | direct | PDF p.5, Table I | true |
| PAI12-8 | The authors report no indication of a chiral side band in the present `194Tl` experiment. | experimental-limit | direct | PDF p.12, conclusion | true |

## Competing Interpretations and Limitations

- The crossing near `0.34 MeV` is an energy-derived alignment feature under the stated Harris reference; it is not a direct measurement of a configuration label or a pairing gap.
- The experimental alignment gain and the authors' pair-alignment explanation are separate evidence layers. The calculated quasiparticle Routhians predict other crossing frequencies and must not be confused with the experimental alignment plot.
- B2 transition character and parity remain ambiguous without an `18−` lifetime; its post-crossing 4qp assignment remains provisional.
- The paper reports no absolute lifetime/strength systematics across the crossing. Relative intensities and DCO/IPDCO cannot replace those companion observables.
- Pai reports no observed chiral side band in this experiment (`PAI12-8`); this is experiment-specific and does not settle later chirality candidates in `194Tl`.

## Knowledge Impact and Learning Decision

- Effect: `limits` a novelty claim based on the existence of a `194Tl` 2qp→4qp crossing—the crossing was already reported by this independent INGA experiment.
- Reusable boundary: retain the crossing frequency as a derived alignment handle; retain 2qp→4qp as author interpretation; retain the B2 lifetime/parity limitation.
- The later near-degenerate 4qp pair reported by Masiteng and summarized by Bark is a separate iThemba data lineage, but its primary 2013/2014 full texts were not available for this run. Bark remains secondary for that post-crossing partner claim.
- Review state: page remains `unreviewed`; every claim retains `needs_review: true`.

## Related Knowledge

- Nucleus: [[194tl]]
- Secondary comparison: [[bark-2024-investigations-nuclear-chirality-ithembalabs]]

## Extracted Pages

- Nucleus: [[194tl]]
- Models: [[cranked-shell-model]], [[routhian]]
- Methods: γ–γ coincidence, DCO and linear-polarization asymmetry
- Observables: band energies, alignment, moment of inertia, DCO/IPDCO
