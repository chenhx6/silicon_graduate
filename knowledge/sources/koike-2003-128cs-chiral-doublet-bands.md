---
type: source
title: "Koike et al. 2003 - Chiral doublet bands in odd-odd Cs isotopes"
aliases: [Koike 2003 128Cs DCO and partner bands]
created: 2026-10-10
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model
reading_depth: deep-read
title_original: "Systematic search of πh11/2⊗νh11/2 chiral doublet bands and role of triaxiality in odd-odd Z=55 isotopes: 128,130,132,134Cs"
authors: [T. Koike, K. Starosta, C. J. Chiara, D. B. Fossan, D. R. LaFosse]
journal: "Physical Review C"
year: 2003
volume: 67
pages: "044319"
doi: "10.1103/PhysRevC.67.044319"
canonical_source: "https://doi.org/10.1103/PhysRevC.67.044319"
repository_record: "https://tohoku.repo.nii.ac.jp/records/5352"
full_text_url: "https://tohoku.repo.nii.ac.jp/record/5352/files/PhysRevC.67.044319.pdf"
repository_access: "Repository API metadata marks the PDF license_free."
downloaded_pdf_sha256: "0aeeb70d4d8fe59e376078d40c9dd7b8c0b6f9c4e9e683b6b9389cb8b802bb5d"
nuclei: [128Cs, 130Cs, 132Cs, 134Cs]
reactions: [122Sn-10B-4n, 124Sn-10B-4n, 130Te-6Li-4n, 130Te-7Li-3n]
experiments: [Stony-Brook-LINAC, HPGe, BGO-multiplicity-filter, DCO]
models: [core-quasiparticle-coupling, Kerman-Klein-Donau-Frauendorf]
observables: [level-scheme, relative-intensity, DCO, mixing-ratio, B(M1)/B(E2), B(M1)-in-out]
methods: [gamma-gamma-coincidence, delayed-coincidence, angular-correlation]
tags: [128Cs, chirality, partner-bands, DCO, transition-strength-ratios]
citation_key: "Koike_2003"
raw_file: "raw/papers/gpt/learning-daily/20261009-DAY10-electromagnetic-ratios-collective-modes/koike-2003-128cs.pdf"
raw_sha256: "0aeeb70d4d8fe59e376078d40c9dd7b8c0b6f9c4e9e683b6b9389cb8b802bb5d"
---

# Chiral doublet bands in odd-odd Cs isotopes: 128Cs transition map

## Bibliographic Record

- T. Koike, K. Starosta, C. J. Chiara, D. B. Fossan, and D. R. LaFosse, “Systematic search of πh11/2⊗νh11/2 chiral doublet bands and role of triaxiality in odd-odd Z=55 isotopes: 128,130,132,134Cs,” *Phys. Rev. C* **67**, 044319 (2003), DOI 10.1103/PhysRevC.67.044319.
- Crossref metadata, Tohoku University repository record 5352, the printed journal header, and the footer article locator identify PRC 67, 044319 (2003). The first-page DOI line in this repository PDF instead prints the placeholder 10.1103/PhysRevC.67.0343XX; this internal mismatch is retained rather than silently repaired.
- The repository API marks the PDF license-free. The temporary PDF used here had SHA-256 0aeeb70d4d8fe59e376078d40c9dd7b8c0b6f9c4e9e683b6b9389cb8b802bb5d.
- Scope: targeted deep reading of the 128Cs experimental sections, Figs. 1–4, Tables I, II, VI, VII, the B-ratio derivation, and the 128Cs ratio discussion/Fig. 16. The remaining isotope sections and later theoretical figures were not read end-to-end.

## Experimental Chain and 128Cs Scheme

The 128Cs study used 122Sn(10B,4n) at 47 MeV, a 3.0 mg/cm² target backed by 34 mg/cm² Pb, six Compton-suppressed HPGe detectors, and a 14-element BGO multiplicity filter. Approximately 54×10⁶ prompt γ-γ events were sorted. Figure 1 labels the 128Cs yrast band Y, its sideband S, and the linking transitions L. The authors support a 9+ yrast bandhead using systematics and delayed-coincidence information.

The 2003 experiment is distinct from Grodner et al. 2006's 55-MeV Warsaw/OSIRIS II DSAM campaign. The 2006 paper follows the 2003 spin/parity assignments, so the level-scheme labels share a source lineage even though the later lifetime/strength data are a separate measurement campaign.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KOIKE03-1 | The 128Cs reaction used 122Sn(10B,4n) at 47 MeV with a 3.0 mg/cm² target, Pb backing, six Compton-suppressed HPGe detectors, and a BGO multiplicity filter. | experiment-method | direct | Table I | true |
| KOIKE03-2 | Figure 1 marks the 128Cs yrast band Y, sideband S, linking transitions L, and the adopted I0=9+ bandhead. | level-scheme-result | direct | Figure 1 | true |
| KOIKE03-3 | Time-gated spectra reverse the 143/159-keV ordering from an earlier scheme and identify the approximately 50-ns isomer with the yrast-band head. | level-scheme-revision | direct | Figure 2 | true |
| KOIKE03-4 | Table II lists 128Cs γ energies, relative intensities, DCO ratios, initial/final spins, and multipolarities; intensities are normalized to the 142.8-keV transition and their quoted uncertainty range is 5–30%. | transition-data | direct | Table II | true |
| KOIKE03-5 | Table VI reports DCO ratios and mixing ratios for selected yrast-band ΔI=1 M1/E2 transitions, including the 349-keV 11+→10+ line with δ=-0.16(+0.07/-0.09). | transition-data | derived-experiment | Table VI | true |
| KOIKE03-6 | Table VII identifies five side-to-yrast mixed ΔI=1 links, their spins, gating transitions, and measured DCO ratios. | transition-data | direct | Table VII | true |
| KOIKE03-7 | Figure 4 labels prompt peaks Y, S, or L for yrast, sideband, and linking transitions, respectively. | transition-identity | direct | Figure 4 | true |
| KOIKE03-8 | Figure 16 shows yrast B(M1)/B(E2) staggering and a same-phase B(M1)In/B(M1)Out trend; open points use fitted intensities and some points are limits. | strength-ratio-result | derived-experiment | Figure 16 | true |
| KOIKE03-9 | Equation (7) constructs B(M1)/B(E2) from same-parent γ intensities, transition energies, and the M1/E2 mixing term; the authors neglect δ² because its effect is small relative to branching uncertainty. | ratio-method | derived-experiment | Eq. (7) | true |
| KOIKE03-10 | The applied core-quasiparticle model uses a triaxial rigid core and reproduces selected strength-ratio staggering; the result is model support, not a direct geometry measurement. | model-result | model | Figure 23 | true |
| KOIKE03-11 | The first-page DOI string is a placeholder, while the journal header/footer, Crossref record, and repository metadata identify DOI 10.1103/PhysRevC.67.044319. | metadata-boundary | direct | PDF p. 1 | true |

## Line-Resolved Linking Transitions

Table VII gives the following side-to-yrast links. All are assigned mixed ΔI=1 M1/E2 character in the authors' analysis; DCO values depend on the stated gating transitions and alignment assumptions.

| Eγ (keV) | Transition | Gate Eγ (keV) | Gate transition | RDCO |
|---:|---|---:|---|---:|
| 509 | 11+→10+ | 143 | 10+→9+ | 0.82(9) |
| 532 | 12+→11+ | 349 | 11+→10+ | 0.87(10) |
| 622 | 13+→12+ | 273 | 12+→11+ | 0.65(14) |
| 571 | 14+→13+ | 408 | 13+→12+ | 0.86(13) |
| 639 | 16+→15+ | 464 | 15+→14+ | 0.63(16) |

This table resolves line identity and spin change for the 2003 linking transitions. It does not bind points in the later 2006 B-value plots without a separate line-by-line comparison of that campaign.

## Derived Ratio Check

For the 11+ yrast parent, Table II gives the 348.6-keV 11+→10+ M1/E2 line with relative intensity 64.1 and the 651.7-keV 11+→9+ E2 crossover with relative intensity 9.1. Using Equation (7), λ=9.1/64.1=0.14197 and energies in MeV:

B(M1)/B(E2) = 0.697 × Eγ(E2)^5 / Eγ(M1)^3 × 1/λ × 1/(1+δ²).

The central-value arithmetic gives 13.62 μN²/(e²b²) when δ² is neglected, or 13.28 μN²/(e²b²) using the Table VI central δ=-0.16. The δ² term changes the result by about 2.50%, consistent with the authors' stated choice to neglect it relative to the branching uncertainty. Table II gives a 5–30% intensity-error range rather than row-specific covariance, so no formal uncertainty is attached here. This is a derived ratio from one parent state's branch and mixing inputs, not an absolute B-value measurement.

## Evidence Boundaries

Figure 16 and Equation (7) show why the same-nucleus comparison requires the line identity, parent-state branching basis, γ energies, and mixing assumptions. The 2003 paper is an experiment with relative intensities and DCO/mixing information; Grodner 2006 adds a separate DSAM lifetime chain; Chen 2017 reuses the 2006 data in its model comparison; Grodner 2018 supplies a separate bandhead TDPAD g factor. These layers are complementary but not four independent measurements of the same observable.

The observed ratio staggering and the model's triaxial-core explanation are distinct evidence types. The model is phenomenological and its agreement supports the authors' interpretation under their core assumptions; it does not directly measure a chiral geometry.

## Scope and Reading Depth

The full article was reviewed, including the 128Cs level scheme, Figs. 1–4/16, Tables I/II/VI/VII, and Eq. (7). The source card preserves the first-page DOI placeholder discrepancy.

## Summary

The paper establishes the 128Cs band/transition scheme and reports DCO and mixing information for linking transitions. Its line-level scheme enables a partial comparison with the later Grodner lifetime experiment.

## Key Results

- KOIKE03-1/2/3 record the experimental setup, yrast/side/link scheme, and isomer placement.
- KOIKE03-4/5/6 give transition energies, DCO/mixing values, and the five Table-VII links.
- KOIKE03-7 identifies the Y/S/L figure labels; KOIKE03-9 supports the same-parent ratio reconstruction.

## Competing Interpretations and Limitations

DCO/mixing and relative intensities do not give absolute B values or a measured A label. Cross-campaign energy matching cannot bind every Grodner 2006 Figure-4 strength marker; I=13 and I=15 remain ambiguous/limited.

## Extracted Pages

- [[grodner-2006-128cs-chiral-doublet-lifetimes]]
- [[chirality-wobbling-competition-evidence]]

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–2页，题页、I 引言、反应条件表 I、图1图注。
- 物理第3–9页，II 实验方法、III 数据分析及四种 Cs 同位素的能级结果，含 DCO 定义式(1)。
- 物理第10–13页，III B 后段、IV 实验量讨论、V A 开头，含带头自旋系统学、双带能差、S(I) 与跃迁强度比。
- 物理第14–20页，V 的 KKDF 耦合推导、核芯参数及 ¹²⁸Cs 计算与实验的比较。
- 物理第21–22页，V 末段、VI 结论、致谢及参考文献。
- 本次获取的具体覆盖：逐页核读物理第1–22页提供的提取文本，覆盖 I–VI 节、致谢、参考文献 [1]–[44]、可提取的表格与公式，以及图1–25的图注。图形、逐点读数及缺失表体仍待核看原页。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A19-1 | ¹²⁸Cs 的时间门谱中，143 keV 线出现在与延迟跃迁符合的瞬发投影，在两个延迟投影中缺失。159 keV 线呈相反的时间行为。作者据此把 143 keV 线置于异能态上方，159 keV 线置于下方，并将已知半衰期约 50 ns 的异能态归于主带带头。 | 实验观测与能级排序 | source-reported | 物理第5页 III A 1，图2(a)–(c)及正文，图3为 266 keV 线的时间谱。峰位与面板待核看物理第5页。 | true |
| A19-2 | ¹²⁸Cs 的 509、532、622、571、639 keV 五条侧带至主带连线均列有实验 DCO 比。作者结合门跃迁混合比和计算的 DCO 响应，将五条线指认为混合 ΔI=1 M1/E2，据此确定侧带的相对自旋和正宇称。 | 基于实验的多极性指认 | source-reported | 物理第4页式(1)，第6页表 VI、VII及图5正文。图5以 509 keV 连线为例。 | true |
| A19-3 | 作者从同一母能级的 γ 分支强度与能量推得约化跃迁概率比，并报告 ¹²⁸Cs 侧带的 B(M1)In/B(M1)Out 交错与主带的 B(M1)/B(E2) 交错同相。¹²⁸Cs 和 ¹³⁰Cs 的空心点采用拟合强度，部分弱分支仅给限值。 | 由实验分支推导的比值 | source-reported | 物理第13页 IV A 4、式(7)–(8)、图16正文及图注。点位、相位和限值方向待核看物理第13页。 | true |
| A19-4 | ¹²⁸Cs 的 KKDF 核芯–准粒子耦合计算采用以 ¹²⁸Xe 数据拟合的刚性三轴核芯和非旋流转动惯量。作者报告 γ=27° 时计算再现两类强度比的交错图样。固定其余参数将 γ 改为 0° 后，计算的主带 B(M1)/B(E2) 交错消失。所比较的中子费米能级方案均未再现实验的 I=12 处 S(I)。 | 唯象模型结果 | source-reported | 物理第15页表 XII，第17页式(26)–(29)及表 XIII，第18–19页图20–23相关正文，第20页图24–25相关正文。 | true |

参考文献 [3] 和 [1] 已分别简报本研究的 ¹²⁸Cs 与 ¹³⁰Cs 结果。图13的 ¹²⁴Cs、¹²⁶Cs 侧带资料来自 [20]、[19]，图16的 ¹²⁴Cs 强度资料来自 [20]。¹²⁸Xe 核芯拟合使用 [38]、[42]，¹²⁹Cs 中间核的能级比较使用 [43]。本次核读确认的是论文如何使用这些文献。比对卡提及的 2006 年 DSAM、2017 年数据复用和 2018 年 TDPAD 属于另行核验的文献链。

- 撤下旧卡用 348.6 与 651.7 keV 算出的 11⁺ 主带比值 13.62 和 13.28。物理第3页表 II 只给自旋标签。第6页表 VI、VII 显示，348.6 keV 来自主带 11⁺，而 508.9 keV 连线来自侧带 11⁺，两者都落到主带 10⁺。再加同一条 142.8 keV 至带头跃迁，两个 11⁺ 母能级分别位于带头以上 491.4 和 651.7 keV。第5页图4的提取标签 Y349 与 S652 也支持这一归属，待核原图。保留式(7)，可改用表 II中同属主带 12⁺ 的 272.7 与 621.6 keV 两支说明同母能级比值。
- 把旧卡“Scope and Reading Depth”下的全文审阅表述改为“¹²⁸Cs 实验与强度比定向深读”，与其书目段记录的范围一致。模型图23的条目以物理第19–20页原文重新定位。
- 将 KOIKE03-2 中的 9⁺ 标为作者依据系统学采用的带头自旋，并将 Y、S、L 三类谱峰标签定位到物理第5页图4图注。保留物理第1页 DOI 占位串与规范 DOI 的差异。
