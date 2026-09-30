---
type: source
title: "Banik et al. 2020 - Multiple band structures in 131Xe"
aliases: [Banik 2020 131Xe INGA experiment, 131Xe alpha-induced multiple bands]
created: 2026-09-30
updated: 2026-09-30
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Revealing multiple band structures in 131Xe from α-induced reactions"
authors: [R. Banik, S. Bhattacharyya, S. Biswas, Soumik Bhattacharya, G. Mukherjee, S. Rajbanshi, Shabir Dar, S. Nandi, Sajad Ali, S. Chatterjee, S. Das, S. Das Gupta, S. S. Ghugre, A. Goswami, A. Lemasson, D. Mondal, S. Mukhopadhyay, H. Pai, S. Pal, D. Pandit, R. Raut, Prithwijita Ray, M. Rejmund, S. Samanta]
journal: Physical Review C
year: 2020
volume: 101
pages: 044306
doi: 10.1103/PhysRevC.101.044306
language: en
canonical_source: "https://doi.org/10.1103/PhysRevC.101.044306"
zotero_item_key: ""
citation_key: ""
zotero_uri: ""
library_file: ""
raw_file: "raw/papers/gpt/day3-mean-field-20260929/banik-2020-131xe-reaction/PDFs/Banik_et_al_2020_131Xe_multiple_band_structures.pdf"
raw_sha256: 21e7e1eed7a93ffc3c38f4580fcf93863d02c56e40ffc900b1634df14c7f34e6
nuclei: [131Xe]
reactions: [130Te-alpha-3n-131xe]
experiments: [inga-131xe-alpha-38mev]
models: [cranked-shell-model, routhian]
observables: [level-scheme, relative-gamma-intensity, rdco, linear-polarization, signature-splitting, aligned-angular-momentum]
methods: [in-beam-gamma-spectroscopy, gamma-gamma-coincidence, directional-correlation-from-oriented-states, gamma-ray-linear-polarization]
tags: [131xe, a130, inga, signature-partner, gamma-softness, total-routhian-surface]
---

# Banik 等（2020）：`131Xe` 多能带结构与 TRS 解释

## Summary

这项 `130Te(α,3n)` 38-MeV INGA 实验扩展了 `131Xe` 能级图，报告 72 条新置跃迁，并以符合关系、`R_DCO` 和 `Δ_PDCO` 约束多极性。作者把 `B1(a)` 解释为 `νh11/2` yrast 的 signature partner；另一个弱侧带 `B1(b)` 是否为 γ band 仍未闭合。TRS 计算给出随转频变化的 γ-soft、三轴和多极小模型极小值。论文未报告绝对寿命或绝对跃迁强度，形变/组态结论保持在模型和作者解释层。

## Bibliographic Record

R. Banik et al., *Physical Review C* **101**, 044306 (2020), DOI [10.1103/PhysRevC.101.044306](https://doi.org/10.1103/PhysRevC.101.044306)。Crossref 核对题名、作者、年份、卷和文章号。APS 页面标准许可标记不是 OA 授权；Nature Downloader 的 OA-only 查询返回 `oa_not_found`。随后 APS 公开 PDF 直链返回 HTTP 200、`application/pdf`、`%PDF-1.3`，按 publisher-direct public URL 获取，不记为开放许可。主文 15 页已通读，SHA-256 见 frontmatter 与 [`manifest.json`](../../raw/papers/gpt/day3-mean-field-20260929/banik-2020-131xe-reaction/manifest.json)。用户要求先取主文；正文足以复核这里的实验与 TRS 结论，不需要 SI。

## Scope and Reading Depth

- 完整通读 15 页主文；视觉复核 Fig. 3 能级纲图、Fig. 4 的 `R_DCO/Δ_PDCO` 分布、Table I 两页跃迁表、Figs. 14–16 的 signature-staggering 曲线，以及 Figs. 17–20 的频率依赖 TRS 面。
- 重点追踪新 INGA 数据中的负宇称 `νh11/2` yrast band `B1`、其候选 signature partner `B1(a)`、弱侧带 `B1(b)`，以及作者如何把 signature/alignment 与 Woods–Saxon Strutinsky TRS 联系起来。
- 未重建原始符合矩阵或重新排序事件；论文报告相对强度、DCO 和偏振，不提供绝对寿命或绝对 `B(E2)/B(M1)`。

## Experimental Setup and Data Chain

- 反应为 `130Te(α,3n)131Xe`，束流能量 38 MeV；富集 `130Te` 靶厚 2 mg/cm²，Mylar backing 600 μg/cm²。
- VECC 的 INGA 使用 7 台 Compton-suppressed clover HPGe：4 台位于 90°、2 台位于后向 55°、1 台位于前向 40°，探头距靶约 25 cm；使用 PIXIE-16 250-MHz、12-bit 数字采集，记录时间戳列表模式事件。
- `Mγ≥2` 符合与 `Mγ≥1` 单谱模式均被采集。能量/效率由 `133Ba`、`152Eu` 标准源校准；IUCPIX 生成矩阵/立方体，RADWARE 与 LAMPS 用于符合分析。
- `R_DCO` 由 90°/55° 非对称矩阵测量；90° clover Compton 分段测 `Δ_PDCO`。文章报告在 `Eγ–Eγ` 符合中将能级图扩展 72 条跃迁。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BNK20-1 | `130Te(α,3n)131Xe`、38-MeV INGA 实验建立了扩展能级图，作者报告新放置 72 条 γ 跃迁。 | experimental-fact | direct | Abstract; Sec. II; Fig. 1, PDF pp. 1–4 | true |
| BNK20-2 | Table I 给出跃迁能量、初末态、自旋宇称、相对强度、`R_DCO`、`Δ_PDCO` 和多极性；相对强度按 642.2-keV E2 跃迁归一到 `100(6)`。 | experimental-fact | direct | Table I and footnote, PDF pp. 5–6 | true |
| BNK20-3 | 现有 11/2− yrast band `B1` 被延伸到 35/2−；新建序列 `B1(a)` 通过多条连接跃迁接到 `B1`，作者将其解释为该负宇称带的 signature partner。 | experimental-fact / author-interpretation | direct | Fig. 3; discussion of `B1(a)`, PDF pp. 4, 7–8 | true |
| BNK20-4 | `B1(b)` 有若干衰变到 `B1` 的跃迁，但其内部跃迁很弱或未建立；作者说目前不能据此确认它是 γ-vibrational band。 | experimental-fact / author-interpretation | direct | Fig. 3; Discussion, PDF pp. 4, 10 | true |
| BNK20-5 | Table I 的强度均为符合谱中提取的相对 γ-ray intensity；文章未报告 DSAM/RDDS lifetime 或绝对 `B(E2)/B(M1)` 矩阵。 | synthesis | direct | Sec. IV; Table I and normalization footnote, PDF pp. 4–6 | true |
| BNK20-6 | 对 `B1` 的 1-qp Woods–Saxon Strutinsky TRS，低频 `ℏω=0.11–0.16 MeV` 有 γ-soft 极小，`0.21–0.26 MeV` 极小移至约 `γ=−26°`，`0.31–0.36 MeV` 出现约 `−12°` 与 `−75°` 两个极小。 | model-result | direct | Figs. 17–18; TRS discussion, PDF pp. 12–13 | true |
| BNK20-7 | 对 `B4/B4(a)` 的 3-qp TRS 给出 `β₂≈0.15`、约 `γ=−60°` 的近 oblate 极小，并在约 `−86°≤γ≤−45°` 内保持 100-keV 范围的低能区；这是模型预测，不是形状测量。 | model-result | direct | Fig. 20 and discussion, PDF p. 14 | true |
| BNK20-8 | Table II 的组态标签是基于邻核系统学、能带关系与 TRS 的作者指认；例如 `B4/B4(a)` 为 `π(g7/2 h11/2)⊗νf7/2`，`B3` 上部为五准粒子候选，不是直接轨道占据测量。 | author-interpretation | indirect | Table II; Secs. V–VI; Summary, PDF pp. 11–14 | true |
| BNK20-9 | `B1(a)` 的实验连接与 signature staggering 支持作者的 signature-partner 指认，但不能单独裁定 wobbling；`B1(b)` 缺少带内连接和可比 inter/intraband strengths。 | synthesis | indirect | Figs. 3, 6–7, 14; Discussion, PDF pp. 4, 7–11 | true |
| BNK20-10 | Banik 2020 calls high-spin `B1(a)` a signature partner; Chakraborty 2023 says the unfavored partner was not identified in earlier 131Xe work and identifies a `9/2−–21/2−` sequence, favoring the yrare `13/2−` band while leaving the yrast `13/2−` origin open. Because C23 reanalyzes Banik data, this is an unresolved level/band-label crosswalk within one acquisition, not independent experimental evidence. | synthesis | indirect | Fig. 3 and discussion, PDF pp. 4, 7–11; Chakraborty 2023 Introduction/Results/Discussion, PDF pp. 2–6 | true |

## Data Lineage and Later Reanalysis

Chakraborty et al. 2023 明确说其 `131Xe` 研究是对本论文数据的重新分析（该文 Sec. II, PDF p. 2, Ref. [22]）。他们用同一 `130Te(α,3n)` 38-MeV INGA 谱重新放置一条含 705、816、930-keV 跃迁的序列，测得/拟合部分连接跃迁的 mixing ratio，并将其解释为 M1 主导的 unfavoured signature partner，而未发现 wobbling 实验证据（[[chakraborty-2023-131xe-wobbling-origin]] C23-1–C23-3, C23-7）。这带来新的 level-scheme placement 和解释，但不是第二套独立的反应或探测器采集。

Jehangir et al. 2022 的 TPSM Fig. 7 用先前的 `131Xe` 数据 Refs. [52]–[54]，其中 Ref. [53] 即本实验（[[jehangir-2022-odd-neutron-tpsm-extension]] JN22-5, JN22-11, JN22-12）。因此 2020 实验、2022 TPSM 数据比较和 2023 重分析至少共享这一 INGA 原始实验谱系；后两篇是理论比较/同数据再分析，不能与 2020 数据作为三个独立实验计数。

**Later band-label crosswalk:** BNK20-3 identifies the high-spin B1(a) sequence as a signature partner; Chakraborty et al. 2023 state that the unfavored partner had not been identified in prior 131Xe work and use the reanalyzed data to identify a low-spin sequence. They favor the yrare 13/2− band as the partner and leave the yrast 13/2− origin open (C23-3, C23-6). The exact mapping between Banik labels B1(a)/B5 and the 2023 sequence is not resolved here; retain the difference as a same-data assignment issue, not evidence for an independent experiment.

## Competing Interpretations and Limitations

- 实验直接量是能量、符合放置、归一化相对强度、`R_DCO` 和 `Δ_PDCO`；`B1(a)` 的 signature-partner 标签、B4 组态和 TRS 形状演化属于作者解释或模型输出。
- B1 的 `S(I)` / alignment 趋势被作者用于支持三轴或 γ-soft 行为；TRS minima 依赖 Woods–Saxon 参数化和转动频率，不是独立形状观测。
- B1(b) 可作为侧带候选，但内部跃迁未充分识别，作者无法闭合其 γ-band 判据；需可追踪的带内和带间强度，尤其 inter/intraband `B(E2)`。
- 需要 lifetime/绝对 `B(E2), B(M1)`、带伙伴分辨的 `Q_t` 与完整连接跃迁来区分 signature partner、wobbling、γ vibration 和配置混合；本实验表格的相对强度不能替代这些量。
- TRS 计算在 B1 给出随频率变化的浅谷/多极小，在 B4/B4(a) 给出宽 γ-soft 区域。宽谷意味着报告中的单一 γ 最小值不代表窄分布或刚性形状。

## Extracted Pages

- Models: [[cranked-shell-model]], [[routhian]], [[triaxial-projected-shell-model]]
- Projects: [[a130-model-choice-card]]
- Related sources: [[jehangir-2022-odd-neutron-tpsm-extension]], [[chakraborty-2023-131xe-wobbling-origin]]

## Self-audit

来源 PDF 哈希已与本地 manifest 对应；表内强度保持 relative intensity；所有新增 `BNK20-*` 均 `needs_review: true`，本页保持 `unreviewed`。未修改或重审既有人审的 `knowledge/nuclei/131xe.md` 与 Chakraborty 2023 source page。
