---
type: source
title: "Isomer depletion as experimental evidence of nuclear excitation by electron capture"
aliases: [Chiara 2018 Mo93m NEEC, Chiara 2018 Nature NEEC claim]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: experiment-article
reading_depth: deep-read
title_original: "Isomer depletion as experimental evidence of nuclear excitation by electron capture"
authors: [C. J. Chiara, J. J. Carroll, M. P. Carpenter, J. P. Greene, D. J. Hartley, R. V. F. Janssens, G. J. Lane, J. C. Marsh, D. A. Matters, M. Polasik, J. Rzadkiewicz, D. Seweryniak, S. Zhu, S. Bottoni, A. B. Hayes, S. A. Karamian]
journal: Nature
year: 2018
volume: 554
pages: 216--219
doi: 10.1038/nature25483
language: en
canonical_source: doi:10.1038/nature25483
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2018_Chiara et al_Isomer depletion as experimental evidence of nuclear excitation by electron capture.pdf"
raw_sha256: 5a6d0f39b280e527fce655e37a894c49ce90720ac252915327d880425fcf16ee
archive_required: true
nuclei: [93mo]
reactions: ["7Li(90Zr,p3n)93mMo"]
observables: [isomer-depletion-probability, triple-gamma-coincidence, doppler-shifted-feeding, resonance-cross-section]
methods: [inverse-kinematics-fusion-evaporation, digital-gammasphere, beam-foil-stopping, double-gating-background-subtraction]
tags: [mo93m, neec, isomer-depletion, gammasphere, controversial-observation, nuclear-battery]
---

# Chiara et al. (2018): Isomer depletion as experimental evidence of nuclear excitation by electron capture

## Bibliographic Record

C. J. Chiara, J. J. Carroll, M. P. Carpenter, J. P. Greene, D. J. Hartley, R. V. F. Janssens, G. J. Lane, J. C. Marsh, D. A. Matters, M. Polasik, J. Rzadkiewicz, D. Seweryniak, S. Zhu, S. Bottoni, A. B. Hayes, and S. A. Karamian, "Isomer depletion as experimental evidence of nuclear excitation by electron capture," *Nature* **554**, 216--219 (2018), DOI: `10.1038/nature25483`. Primary PDF is 10 pages, SHA-256: `5a6d0f39b280e527fce655e37a894c49ce90720ac252915327d880425fcf16ee`.

## Scope and Reading Depth

Deep reading of main text, Methods, and Extended Data display items. Visual inspection of Fig. 1 decay scheme (PDF p. 2 / printed p. 217), Fig. 2 coincidence spectra (PDF p. 2 / printed p. 217), Fig. 3 Doppler-corrected 2475-keV and unshifted 268-keV spectra (PDF p. 3 / printed p. 218), and Methods background subtraction parameter \(k_{\text{ave}} = 0.99(8)\).

## Summary

The paper reports claimed experimental evidence for Nuclear Excitation by Electron Capture (NEEC) in \(^{93\text{m}}\)Mo. Reconstructing \(^{90}\text{Zr} + {}^{7}\text{Li}\) reaction products stopping in a carbon foil, the authors report prompt coincidences between Doppler-shifted 2475-keV \(\gamma\)-rays feeding the 6.85-h isomer and unshifted 268-keV \(\gamma\)-rays depopulating a 2430-keV intermediate state. They extract an excitation probability \(P_{\text{exc}} = 1.0(3)\%\) and average cross section \(\bar{\sigma}_{\text{exc}} \approx 40\text{ b}\).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| C18-1 | Reports observation of prompt coincidences between Doppler-shifted 2475-keV feeding line and unshifted 268-685-1478 keV cascade in 93Mo. | measured-coincidence | direct experimental report | printed p.216--217, Fig. 2 | true |
| C18-2 | Extracts isomer depletion probability P_exc = 1.0(3)% from ratio of unshifted 268-keV area (510 counts) to Doppler-corrected 2475-keV area (15400 counts). | derived-quantity | derived experimental value | printed p.217--218, Fig. 3 | true |
| C18-3 | Deduces average target-stopping cross section sigma_exc ~ 40 b across 5 mg/cm2 carbon catcher. | derived-quantity | derived value | printed p.217--218 | true |
| C18-4 | Calculates Coulomb excitation (GOSIA: 3e-6) and inelastic scattering (FRESCO: 2e-6) as insufficient to explain observed 1% depletion. | model-calculation | model bound | printed p.218, Methods | true |

## Competing Interpretations and Limitations

后续证据不能倒写成2018原实验已经唯一查明的污染来源。Guo2021提出产生/停止靶反应及符合背景的竞争解释，原作者的时间门答复也须保留；Wu2019的理论率与实验率比较依赖停止、电子态和核输入。Guo2022使用隔离异能束，在其条件下未见显著268-keV峰，给出约\(2\times10^{-5}\)的上限，对百分比量级的先前报告构成实质挑战。该上限既不是所有NEEC过程的排除，也不单独证明2018数据的唯一背景机制。评论、答复与隔离束的实际证据及各自依赖见[[mo93-neec-evidence-and-depletion-transfer-20261107]]、[[guo-2021-mo93m-depletion-contamination-challenge]]和[[guo-2022-mo93m-isomer-beam-depletion-limit]]。

## Extracted Pages

- mo93m
- neec
- isomer-depletion
- gammasphere

## 2026-11-27 — 馆藏原件与覆盖核对

- {"from": 1, "to": 3, "sections": ["主文、反应与符合分析、对照实验和竞争机制", "图1–3及图注", "参考文献1–27和声明"]}
- {"from": 4, "to": 6, "sections": ["Methods：靶构造、谱构建和扣底、激发概率和截面、替代机制、标定及不确定度", "式（1）–（2）、代码和数据可用性、参考文献28–36"]}
- {"from": 7, "to": 10, "sections": ["扩展数据图1–4的图注和可提取标注，依次为分层靶、2475 keV线形、四个扣底分谱和FRESCO计算"]}
- 本次获取的具体覆盖：通读全部10个物理页的抽取正文、方法、书目及图注。第7页的靶结构示意与照片只读到图注。建议更正书目和实验表述后接收旧稿的同版文字覆盖。旧稿所称图像目视查验仍待独立复核。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A18-1 | 作者报告，移位的2475 keV线与未移位的268、685和1478 keV级联相容。2475/1478 keV双门谱出现268、685 keV峰，2475/268 keV双门谱出现685、1478 keV峰。作者报告268 keV线仅计统计误差约为7σ，计入扣底不确定度后约为3σ。 | 实验报告 | source-reported | PDF第2页（印刷217页）图1、图2a–c，峰形与门控谱待目视核对。PDF第4–6页 Methods 式（1）–（2）及 Uncertainties。 | true |
| A18-2 | 作者从 Doppler 校正的2475 keV净面积 1.54(3)×10⁴ 与未校正的268 keV拟合面积 5.1(16)×10² 推得激发概率 1.0(3)%。计算使用相对效率 0.28 和268 keV内转换系数 0.0355。按两层碳合计约5 mg/cm²的全厚度折算，平均截面约40 b。 | 实验派生量 | source-reported | PDF第2页（印刷217页）概率推导段，第3页（印刷218页）图3a–b，谱线和积分对象待目视核对。PDF第5页 Methods 的 Excitation probability and cross-section，概率和截面关系式未编号。 | true |
| A18-3 | 作者用 FRESCO 估算锂层和碳层的非弹性激发概率分别为 6×10⁻⁸ 和 2×10⁻⁶，用 GOSIA/RACHEL 估算铅层库仑激发概率约 3×10⁻⁶。计算采用壳模型给出的直接 E2 跃迁强度 B(E2)=72 e² fm⁴。 | 模型计算 | source-reported | PDF第3页（印刷218页）正文，第5页 Methods 的 Alternative reactions and excitation mechanisms，第10页扩展数据图4及图注。 | true |
| A18-4 | 作者把符合序列解释为异能态经 NEEC 激发至高约4.85(9) keV的中间态。该归因依赖对已考察反应、常规激发机制及背景的排查。 | 作者解释 | source-reported | PDF第1–3页（印刷216–218页）正文，第2页图1–2，第5页 Methods 的 Alternative reactions and excitation mechanisms。 | true |

图2a用123、203、770、963 keV背景线定标，得到 k_ave=0.99(8)。图2c采用另一组背景线，得到 k_ave=1.03(10)。图3的概率估计使用241/1442及241/686 keV双门并相加。约40 b依赖碳层全厚度，是全厚度平均量。原文未计算共振峰值。

- 将 Wiki 书目和前置元数据中的216–219改为216–218，另记物理PDF共10页，含 Methods 和4幅扩展数据图。
- 将“反冲核在碳箔停止”改为“反冲核在较厚碳层中减速，最终停在²⁰⁸Pb衬底”。依据为PDF第4页 Methods 和第7页扩展数据图1图注。
- 将 C18-1 定位到PDF第2页图2a、c的互补双门谱。将 C18-2 的整数计数替换为带不确定度的净峰面积，并补列效率和内转换修正。
- 将 C18-3 改为两层碳合计厚度上的平均截面。将 C18-4 补全为锂、碳、铅三层各自的模型概率，定位至PDF第3、5页及第10页扩展数据图4。
