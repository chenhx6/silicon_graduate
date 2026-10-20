---
type: source
title: "Grodner et al. 2006 - 128Cs partner-band lifetimes and transition strengths"
aliases: [Grodner 2006 128Cs chiral doublet]
created: 2026-10-10
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "128Cs as the Best Example Revealing Chiral Symmetry Breaking"
authors: [E. Grodner, J. Srebrny, A. A. Pasternak, I. Zalewska, T. Morek, Ch. Droste, J. Mierzejewski, M. Kowalczyk, J. Kownacki, M. Kisieliński, S. G. Rohoziński, T. Koike, K. Starosta, A. Kordyasz, P. J. Napiorkowski, M. Wolińska-Cichocka, E. Ruchowska, W. Płóciennik, J. Perkowski]
journal: "Physical Review Letters"
year: 2006
volume: 97
pages: "172501"
doi: "10.1103/PhysRevLett.97.172501"
canonical_source: "https://doi.org/10.1103/PhysRevLett.97.172501"
repository_record: "https://tohoku.repo.nii.ac.jp/records/5385"
full_text_url: "https://tohoku.repo.nii.ac.jp/record/5385/files/PhysRevLett.97.172501.pdf"
repository_access: "Repository API metadata marks the PDF license_free."
downloaded_pdf_sha256: "654527dc34f2ff9e455d3dc16f88e83f7e846ec457c97c453e652e22c51f01c9"
nuclei: [128Cs, 132La]
reactions: [122Sn-10B-4n, 122Sn-14N-4n]
experiments: [OSIRIS-II, Doppler-shift-attenuation-method]
models: [side-feeding, core-quasiparticle-coupling]
observables: [level-scheme, lifetime, B(E2), B(M1), band-energy-splitting]
methods: [gamma-gamma-coincidence, Doppler-shift-attenuation-method]
tags: [128Cs, chirality, DSAM, transition-strengths, partner-bands]
citation_key: "Grodner_2006"
raw_file: "raw/papers/codex-day10/grodner-2006-128cs.pdf"
raw_sha256: "654527dc34f2ff9e455d3dc16f88e83f7e846ec457c97c453e652e22c51f01c9"
---

# 128Cs partner-band lifetimes and transition strengths

## Bibliographic Record

- E. Grodner *et al.*, “128Cs as the Best Example Revealing Chiral Symmetry Breaking,” *Phys. Rev. Lett.* **97**, 172501 (2006), DOI 10.1103/PhysRevLett.97.172501.
- The full text was retrieved from the Tohoku University repository record 5385. Its public record identifies the PDF as license-free. The temporary copy used in this run had SHA-256 654527dc34f2ff9e455d3dc16f88e83f7e846ec457c97c453e652e22c51f01c9.
- Crossref DOI metadata and the article's first page agree on title, author list, journal, volume, article number, and year.

## Scope and Reading Depth

The four-page article was read end-to-end. Figures 1–6 were inspected, including the 128Cs level scheme, DSAM line-shape examples, measured strength plots, and the article's core-quasiparticle-coupling comparison.

## Experimental and Derived-Strength Chain

The 128Cs states were populated with 122Sn(10B,4n) at 55 MeV. The thick target also served as stopper; about 10^8 gamma-gamma coincidences were recorded with ten Compton-suppressed HPGe detectors in OSIRIS II. Lifetimes were obtained with DSAM. Cascade feeding was included, while unobserved side feeding was modeled. The side-feeding parameters for 128Cs were assumed from 131La; two limiting side-feeding parameter sets were used to account for lifetime uncertainty.

Spin/parity assignments in the scheme follow the earlier 128Cs study cited as Ref. [6]. Branching ratios were determined from gamma-line intensities corrected for Doppler broadening. The reported B(E2) and B(M1) values are derived from the lifetimes and branching ratios, not independent observables. For B(M1; I→I−1), the authors assume pure M1 because the E2 admixture contributes less than 10%; that is a stated analysis assumption supported by prior data.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR06-1 | 128Cs was populated through 122Sn(10B,4n) at 55 MeV and studied with OSIRIS II using a thick target that also served as stopper. | experiment-method | direct | printed p. 1 | true |
| GR06-2 | DSAM lifetime fits included observed cascade feeding and modeled unobserved side feeding. | analysis-method | derived-experiment | printed p. 1 | true |
| GR06-3 | For 128Cs, side-feeding parameters were transferred from 131La and the variation of two limiting parameter sets was included in the lifetime uncertainty. | uncertainty-model | derived-experiment | printed p. 2 | true |
| GR06-4 | Reported branching ratios use gamma-line intensities corrected for Doppler broadening, and the B(E2)/B(M1) values are calculated from lifetime and branching inputs. | derived-strength | derived-experiment | printed p. 2 | true |
| GR06-5 | Extraction of B(M1; I→I−1) assumes pure M1 because the E2 contribution is estimated below 10%. | multipolarity-assumption | derived-experiment | printed p. 2 | true |
| GR06-6 | Figure 4 displays in-band B(E2), in-band B(M1), and side-to-yrast B(M1); the authors describe similar side/yrast strengths and M1 staggering for 128Cs. | transition-strength-result | derived-experiment | Figure 4 | true |
| GR06-7 | The 128Cs partner-band energy splitting is reported as about 200 keV. | level-scheme-result | direct | printed p. 3 | true |
| GR06-8 | The core-quasiparticle-coupling calculation reproduces the main strength features, while its B(M1) staggering is more pronounced than the data. | model-comparison | mixed | Figure 6 | true |
| GR06-9 | Figure 2 gives the 128Cs partner-band level scheme and transition energies; its spin/parity assignments follow Koike et al. 2003 Ref. [6]. | scheme-lineage | direct | Figure 2 | true |
| GR06-10 | Figure 4 shows side-to-yrast B(M1) points at I=12,13,14,16 and an I=15 limit; its accompanying spectrum labels linking lines L509, L532, L571, L639 and an overlapping Y622/L622 peak. | strength-line-crosswalk | mixed | Figure 4 | true |

## Figure-Level Reading

- Figure 2 gives the partner-band level scheme; arrow widths encode relative transition probabilities normalized to the total intensity depopulating a level, and italic values under spins are lifetimes. This is not a line-by-line table of absolute branches.
- Figure 3 shows Doppler-broadened line shapes for the 930-keV 18→16 transition in the 128Cs yrast band and a 132La control transition.
- Figure 4 plots the derived B(E2) and B(M1) values. Its bottom 128Cs panel is specifically the side-to-yrast B(M1) series; the article does not plot an interband B(E2) series there.
- Figure 6 compares the experimental strengths with the core-quasiparticle-coupling calculation. The paper says the main features are reproduced but the calculated M1 staggering is much stronger.

## Evidence Boundaries

The paper does not provide an event-level spectrum/response package or a covariance matrix for a new analysis. Its B values share the same lifetime, branch, side-feeding, and multipolarity assumptions. The gamma-ray transition probabilities are derived results; a visually similar strength pattern is not an independent geometric measurement. Figure 2's energy labels align with the line assignments established in Koike et al. 2003, which the 2006 article cites for spins/parities. In Figure 4, the spin-indexed out-of-band points at I=12,14,16 can be tentatively paired with L532, L571, L639 by their energy labels and scheme; the I=13 point is ambiguous because the spectrum marks Y622/L622, and the I=15 entry is only a limit. The plot does not provide a point-by-point B-versus-Eγ table. Chen et al. 2017 cite this paper as Ref. [14] for their Figure 2 experimental points, so that theoretical comparison does not add a second experiment.

## Summary

This experiment reports partner-band lifetimes and derived transition strengths in 128Cs. The electromagnetic patterns are compatible with the authors’ chiral interpretation within their DSAM and transition assumptions.

## Key Results

- GR06-1/2 identify the reaction, detector setup, and DSAM lifetime analysis.
- GR06-3/4/5 record side-feeding, pure-M1 assumptions, and derived B(E2)/B(M1) values.
- GR06-6/9/10 report the staggering interpretation and the partial line-marker mapping; I=13 remains ambiguous and I=15 is an upper limit.

## Competing Interpretations and Limitations

Absolute strengths depend on lifetime, feeding, and pure-M1 assumptions. Figure-level line mapping remains partial; the paper does not measure an experimental A quantum number or geometry directly. Chen 2017 reuses these data.

## Extracted Pages

- [[koike-2003-128cs-chiral-doublet-bands]]
- [[chirality-wobbling-competition-evidence]]

## Day18原件复核纠正：侧馈迁移、强度对比与手征解释边界

2026-10-21 对主原件 `raw/papers/codex-day10/grodner-2006-128cs.pdf` 重新核读，SHA-256 为 `654527dc34f2ff9e455d3dc16f88e83f7e846ec457c97c453e652e22c51f01c9`。本段为 Codex self-audit；前文 GR06-1–10、原有 review 状态和证据边界保持，不计新增实验或课程学分。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR06-D18-1 | **superseded（2026-10-21）**：原追加段中侧馈迁移、132La约20倍B(E2)差异有直接来源，但“Qt崩塌4.5倍”“128Cs Qt约2.1 eb”“彻底否定静态手征”及“确立真手征”没有原称强度的支持，由 GR06-D18-2–7 分项替代；旧 result-034/contract-034不再验证这些结论。 | superseded-task-audit | corrected-and-boundary | 本段 GR06-D18-2–7；旧 grodner11-126cs-dsam-result-034 与 contract-034 | true |
| GR06-D18-2 | 作者用厚Sn靶兼作阻停体，以DSAM测128Cs与132La寿命，再由寿命和分支导出B值；它们共享输入，不能当作独立几何测量。“靶兼阻停体”不表示无飞行中发射或不依赖停止历史。 | experiment-and-derived-chain | direct-and-boundary | PDF pp.1–2 / 172501-1–2实验方法；p.2 Fig.2 | true |
| GR06-D18-3 | Qlow/Qhigh/SMR由131La研究确定并假设迁移到128Cs与132La。128Cs用两组侧馈参数的变化计入寿命误差；132La侧馈模式导致的寿命影响估计约±15%。这是作者的模型与误差处理，不是本次重拟合。 | side-feeding-assumption-and-budget | direct | PDF p.2 / 172501-2左栏首两段；Fig.1 | true |
| GR06-D18-4 | 原文直接报告132La侧带B(E2)约比对应yrast值低20倍，M1约低2–5倍，并在总结中认为其派生强度不符合内禀手征的对称要求。保留作者结论的对象及模型语境，不写成排除所有手征动力学的唯一实验裁决。 | reported-strength-and-author-interpretation | direct | PDF p.2右栏末段至p.3左栏首段；Fig.4；p.4总结 | true |
| GR06-D18-5 | 将B(E2)比20换成Qt比sqrt(20)≈4.47，须假设相同spin及相同转轴/γ/K等矩阵元几何；这是条件推导，不是作者直接报告的Qt或沿spin“崩塌”。原文无128Cs两带Qt均约2.1 eb的报告，旧034脚本也未读入或计算128Cs数据；该数值撤回。 | quadrupole-conversion-boundary | derived-and-source-boundary | PDF pp.1–4全文；Fig.4报告B值；旧034脚本输入与计算主体 | true |
| GR06-D18-6 | 作者报告128Cs伙伴带对应B(E2)/B(M1)相似及带内/side→yrast的M1交错，认为符合核模型预期的手征伙伴特征；模型计算的M1交错比实验更强。提取仍假设pure M1，所引先前实验支持E2贡献小于10%；相似强度不能单独证明形变相等或指定内禀几何。 | author-interpretation-and-extraction-boundary | direct | PDF p.2右栏pure-M1段；p.3正文/Fig.4；p.4 Fig.6及总结 | true |
| GR06-D18-7 | 本次完整读取四页正文主线与图注，视觉核PDF2–3的Fig.1–5；Fig.6本次仅文字/图注读取。未数字化强度点，未取得原谱、完整响应或联合协方差，不生成新寿命/Qt或实验CI。 | current-source-reading-scope | direct-and-boundary | 主raw PDF pp.1–4；本次视觉范围PDF pp.2–3 | true |

旧[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/grodner11-126cs-dsam-contract-034.json)与[结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/grodner11-126cs-dsam-result-034.json)在本段审计用途上标为 **superseded**；其未读入本128Cs原件，固定passed字段不能验证本页的侧馈、强度或Qt。原输出保留为历史记录，本次不重跑或覆盖。
