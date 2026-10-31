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
raw_file: "raw/papers/gpt/learning-daily/20260930-DAY4-pairing-quasiparticle-configuration/194tl-pai-2012/PDFs/Pai-2012-PRC85-064313-194Tl-arXiv-1201.6596v2.pdf"
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

## Day18 更正审计：B1 crossing、B2/B3 组态与后续寿命来源边界

checkpoint047 完整核对本地 arXiv v2 原件全部 12 页主线、Table I、Fig. 5/7 及组态讨论。raw SHA256 `633B068625691C4AEB6200867A9CD8820E6528B9FC19AE1C6CA2A3928FCF7553` 匹配。原 PAI12-1–8、frontmatter 和 review 标记保持；下列新条目明确纠正旧 `PAI12-6` 的组态概括，并取代此前 `PAI12-D18-1`。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PAI12-D18-1 | **superseded / 更正**：撤回将 37-keV 近简并、三带 DSAM、四条 PRM 能带、Q0=3.85 eb 及“数学上不可能唯一配对”归为本文定量结果的复合断言。后续文献与本文的数据、模型及读取范围见以下分列。 | evidence-correction | superseded | 本节 PAI12-D18-2–12；旧 Day18 复合 claim | true |
| PAI12-D18-2 | 本文 B1 的能级派生对齐在 ℏω≈0.34 MeV 附近增加约 5 ℏ；Fig. 7 使用 J0=8、J1=40 的 Harris 参考。该量来自能级，不是寿命或组态的直接测量。 | derived-observable | direct | PDF pp.7–8, Fig. 7 and caption | true |
| PAI12-D18-3 | 作者结合邻核 crossing、阻塞和计算 Routhian，将 B1 的 crossing 解释为第二对 νi13/2 中子对齐，即 2qp 到 4qp 的演化；计算 crossing 约 0.23 MeV 与实验派生约 0.34 MeV 须分开。 | author-interpretation | indirect | PDF pp.7–8, crossing discussion；pp.10–11, Fig. 13 | true |
| PAI12-D18-4 | B2→B1 的 761-keV link 呈 quadrupole-like DCO，但无 IPDCO；作者假设 E2 得到暂定负宇称，同时不排除 M2/正宇称，要求 18(−) 态寿命解除歧义。所列约 50 ps 与 5 ns 是 Weisskopf 半衰期估计，不是实测寿命。 | evidence-boundary | direct | PDF p.6, 761-keV linking-transition discussion；p.5, Table I | true |
| PAI12-D18-5 | **对旧 PAI12-6 的定向更正**：p.9 对 B2 的解释是在 B1 crossing 后的 4qp 基础上再加入一对 i13/2 质子；p.12 总结明确将 B2/B3 均建议为 6qp。B2 的该解释仍被作者称为过早且宇称暂定，不能简写成已建立的 4qp 带。旧 PAI12-6 行及其 flag 保留作历史定位。 | source-correction | direct | PDF p.9, B2 discussion；p.12, conclusion | true |
| PAI12-D18-6 | 本文未实施三带 DSAM 寿命测量，也未给出三带绝对 B(M1)、B(E2) 相等的结果。Table I 是相对强度、DCO/IPDCO；B3 的未观测 E2 crossovers 仅用于估计 B(M1)/B(E2)>28 μN²/(eb)² 的下限。 | evidence-boundary | source-scope | PDF p.5, Table I；p.9, B3 discussion | true |
| PAI12-D18-7 | 作者在本实验中未观察到手征侧带；这只约束本文实验，不裁决之后 194Tl 的候选带。 | experimental-limit | direct | PDF p.8, discussion；p.12, conclusion | true |
| PAI12-D18-8 | Bark 2024 p.16 转述后来候选带能差最小为 I=21 处 37 keV、在所观测范围不超过 110 keV，归于 Masiteng 2013。本文 Pai 的 B1 仅延伸至 I=18；旧脚本 I=17–24 的八点能差数组没有从本文重建，本次也未用后续 primary 核定。 | cross-source-boundary | review-reported | Bark 2024 PDF p.16 / 24302-16；Pai PDF pp.4,6,12 | true |
| PAI12-D18-9 | Bark 2024 p.18 将后续 DSAM 归于 Masiteng et al., EPJ A52,28 (2016)，并称三条负宇称带的 B 值在实验不确定度内相近；2014 的 EPJ A50,119 是另一篇谱学来源。本次只核了综述该段与引文，未取得/原读 2016 primary，不能认证逐态数值、误差覆盖或“完全相等”。 | cross-source-boundary | review-reported | Bark 2024 PDF p.18, Figs.25–27；pp.29–30, Refs.26–27 | true |
| PAI12-D18-10 | Bark 所述 MPR 四带计算采用 ε2=0.15、γ=30°/40°；Guo 2022 的 β=0.13、γ=45.19° 则是 194Tl 的 constrained-RMF 静态 I* 极小值。两者不能合并成同一项“γ≈45° PRM 四带”计算，更不是 Pai 的实验结果。 | model-provenance-boundary | direct-companion | Bark 2024 PDF p.18；Guo 2022 PDF p.5, Table 1 I*；p.7 | true |
| PAI12-D18-11 | 旧脚本以 β=0.13 的轴对称公式求 Q0≈3.846 eb，并用 K=0 高自旋公式求 B(E2)；其 γ 变量未进入计算。所得数值不是 Pai 或 Guo 报告的绝对跃迁强度，也不能代替三轴辐射几何或实测 Qt。 | calculation-boundary | task-self-audit | 旧 day18_masiteng14_194tl_degeneracy_audit.py 的公式；Pai PDF p.9 的 TRS 边界 | true |
| PAI12-D18-12 | Bark 对 γ=40° 情形写的是四条计算带如何分组变得不清楚，并保留未观测第四带的可能；它没有证明实验配对在数学上不可能。能量近简并和 B 值相近提供约束，单独使用不能唯一确定手征几何；需保留模型与竞争解释范围。 | synthesis-boundary | review-and-inference | Bark 2024 PDF p.18；pp.20–22 的竞争解释讨论 | true |

后续来源边界见 [[bark-2024-investigations-nuclear-chirality-ithembalabs]] 与 [[guo-2022-possible-chiral-multiple-chiral-thallium-isotopes]]。本次 Guo 仅定向核其形变与 provenance，不声称新完整原读；Masiteng/Lieder 后续 primary 未得。旧分析合同与结果保留为历史运行记录；其固定 `passed` 不能充当科学验证。本节不授课程学分，不清除任何旧 review flag。
