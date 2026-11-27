---
type: source
title: "Possible overestimation of isomer depletion due to contamination"
aliases: [Guo 2021 Mo93m contamination, Guo 2021 Nature Matters Arising]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: comment-article
reading_depth: deep-read
title_original: "Possible overestimation of isomer depletion due to contamination"
authors: [Song Guo, Yongde Fang, Xiaohong Zhou, C. M. Petrache]
journal: Nature
year: 2021
volume: 594
pages: E1--E2 (Critique); E3--E4 (Chiara Reply)
doi: 10.1038/s41586-021-03333-5
language: en
canonical_source: doi:10.1038/s41586-021-03333-5
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2021_Guo et al_Possible overestimation of isomer depletion due to contamination.pdf"
raw_sha256: 5e98a2700de3c7892fac86abe69475194aa4a7d7b74a2e9608f710c0436a9236
archive_required: true
nuclei: [93mo, 95ru, 92mo]
reactions: ["90Zr(alpha,n)93Mo", "90Zr+12C", "7Li+90Zr"]
observables: [chance-coincidence-rate, background-k-ratio, contamination-peak-intensities]
methods: [pace4-fusion-cross-section-calculation, coincidence-background-reanalysis, spectral-overlay-audit]
tags: [mo93m, neec-critique, contamination, chance-coincidences, background-subtraction-flaw, matters-arising]
---

# Guo et al. (2021): Possible overestimation of isomer depletion due to contamination (plus Chiara et al. Reply)

## Bibliographic Record

The archived 4-page PDF contains two separate publications:
1. **Critique**: Song Guo, Yongde Fang, Xiaohong Zhou, and C. M. Petrache, "Possible overestimation of isomer depletion due to contamination," *Nature* **594**, E1--E2 (2021), DOI: `10.1038/s41586-021-03333-5`.
2. **Reply**: C. J. Chiara, J. J. Carroll, M. P. Carpenter, J. P. Greene, D. J. Hartley, R. V. F. Janssens, G. J. Lane, J. C. Marsh, D. A. Matters, M. Polasik, J. Rzadkiewicz, D. Seweryniak, S. Zhu, S. Bottoni, and A. B. Hayes, "Reply to: Possible overestimation of isomer depletion due to contamination," *Nature* **594**, E3--E4 (2021), DOI: `10.1038/s41586-021-03334-4`.

SHA-256 of combined PDF: `5e98a2700de3c7892fac86abe69475194aa4a7d7b74a2e9608f710c0436a9236`.

## Scope and Reading Depth

Deep reading of the critique (pp. E1--E2) and author reply (pp. E3--E4). Locators examined: Guo et al. Fig. 1 target cross sections (PDF p. 2 / printed p. E2), Guo et al. Fig. 2 background overlay scaled by 1.33 (PDF p. 2 / printed p. E2), and Chiara et al. Reply text and Figs. 1--2 (PDF p. 3--4 / printed p. E3--E4).

## Summary

Guo et al. present a Matters Arising critique of Chiara 2018, arguing that in-beam \(^{90}\text{Zr} + {}^{12}\text{C}\) fusion reactions inside the carbon catcher foils produced \(^{93}\)Mo directly at \(\sim 9.3\text{ kHz}\), and that the prominent 263-keV isomer decay line in prompt gates demonstrated unresolved chance/contamination background. In reply, Chiara et al. disputed that the 263-keV line was isomer decay (attributing it to an unpublished prompt 262-keV ANU transition) and defended chance coincidence estimates of \(0.03\%\) to \(0.08(8)\%\).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| G21-1 | PACE4 calculations indicate 90Zr + 12C reactions in carbon stopper produced 93Mo directly at ~9.3 kHz with ~2 kHz prompt 268-keV flux. | contamination-critique | theoretical calculation | printed p.E1--E2, Fig. 1 | true |
| G21-2 | The 263-keV isomer line appears in prompt coincidence with twice the intensity of the 268-keV peak, indicating random coincidence contamination. | spectral-evidence | re-analysis of published data | printed p.E1 | true |
| G21-3 | Re-scaling background spectra by 1.33 shows all prompt background lines share the same ratio as 268 keV, questioning evidence for 3-sigma NEEC excess. | data-analysis-audit | graphical spectral overlay | printed p.E2, Fig. 2 | true |
| G21-4 | Chiara et al. Reply disputes 263-keV attribution (proposing unpublished prompt 262-keV ANU line) and defends chance rates of 0.03% to 0.08%. | author-rebuttal | published author defense | printed p.E3--E4, Figs. 1--2 | true |

## Competing Interpretations and Limitations

The exchange established two competing interpretations: a contamination critique asserting that prompt reaction feeding accounted for the signal, versus the authors' defense asserting low chance rates and a prompt 262-keV contaminant. The dispute could not be settled from the 2018 data alone, leading directly to the 2022 RIBLL isomer-beam benchmark.

## Extracted Pages

- mo93m
- neec
- contamination-critique

## 2026-11-27 — 馆藏原件与覆盖核对

- {"from": 1, "to": 2, "sections": ["Guo等评论（E1–E2）", "污染与偶然符合估算、图1–2及图注、书目1–6"]}
- {"from": 3, "to": 4, "sections": ["Chiara等答复（E3–E4）", "90 ns时间门与原数据重析、图1–2及图注、数据声明、书目1–5"]}
- 本次获取的具体覆盖：通读全部4个物理页的两篇正文、各自图注、书目及声明。建议按DOI分别落实书目与证据归属，更正模型产额和扣底比较的表述后接收旧稿的同版文字覆盖。两篇的图像查验均待复核。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A18-1 | 评论用 PACE4 估算，按锂层和碳层的反应合计，⁹³Mo总产生率约9.3 kHz。再按高自旋布居和支路估算出268 keV线产生率1.7–2.5 kHz，并在100 ns至1 μs假设时间窗下得到偶然符合概率0.03%–0.5%。 | 模型估算 | source-reported | PDF第1页（E1）估算段及未编号的偶然符合关系式，第2页（E2）评论图1。图1插图的层界能量待目视核对。 | true |
| A18-2 | 评论把原论文图3b约262–263 keV处峰归于263 keV异能态衰变，并以约为268 keV峰两倍的强度为污染线索。评论另以1.33的比值叠加原论文扩展数据图3a、c，认为所比较的四条背景线及268 keV线的 k 值可能相近，据此建议把原1.0(3)%视为上限。 | 评论解释 | source-reported | PDF第1页（E1）对原图3b的讨论，第2页（E2）评论图2及 k 的未编号关系式。叠加坐标、横向偏移与770 keV肩峰待目视核对。 | true |
| A18-3 | 答复报告离线时间窗为90 ns，录制时间窗为2 μs。在原数据中比较685 keV事件落入另一90 ns时间窗与落入同一时间窗的计数，得到两次独立⁹³Mo衰变的偶然符合概率 0.08(8)%。 | 原数据重析 | source-reported | PDF第3页（E3）答复的偶然符合估算及时间门重析段。 | true |
| A18-4 | 答复依据四个扣底分量和拟合峰面积，认为采用 k=1.33 会过扣四条背景线。答复将原图3b相关峰归于 ANU 对照中发现、当时尚未发表的静止⁹³Mo 262 keV线，并保留原概率结论。答复举例给出的偶然符合修正使中心值由0.0096降至0.0088。 | 答复解释 | source-reported | PDF第3–4页（E3–E4）答复正文，第4页答复图1插图、图2及末段。拟合 k 值、误差条、缩放与移位待目视核对。 | true |

评论依赖2018年已发表谱图、束流和靶层参数。评论图2比较 g₁g₂ 与 b₁g₂，答复图2比较各自进一步扣底后的 g₁p₂ 与 b₁p₂，并优先采用拟合面积。答复沿用 PACE4 输入估算偶然符合约0.03%，另用90 ns时间门进行数据重析。答复给出的原图3检查为 k=1.07(14)，合并谱中 k 从0.7变至1.3时，派生概率变动约9%。

- 将主条目 `pages` 改为 E1–E2，把 E3–E4、独立 DOI 和答复覆盖移入合订件说明。两篇各自的图1、图2应分别标注。
- 将 G21-1 的“碳停止箔产生约9.3 kHz”改为“按各反应层合计估算约9.3 kHz”，另列268 keV线的1.7–2.5 kHz估算。反应索引中的 90Zr(α,n)93Mo 在本文件中缺少依据，应移除。
- 将 G21-2 的“263 keV异能态衰变线证明随机污染”改为带归属的评论解释，并并列答复的262 keV解释。将 G21-4 的0.03%和0.08(8)%明确标为模型估算和数据重析两项。
- 将 G21-3 限定为评论图2所比较的谱与峰。PDF第2页评论图1插图的层界数字在抽取中串行，图注中 PACE4 后的引文序号也与正文定位存在疑点，两处均须查该页原图及图注。将“直接促成2022年实验”改为“评论提出分离束线方案，2022年论文引用了这场交锋”。
