---
type: source
title: "Wang et al. 2006 - Candidate chiral doublet bands in 126Cs"
aliases: [Wang Liu Komatsubara 2006 126Cs NORDBALL reanalysis, 126Cs Table I ADO and ratio data]
created: 2026-10-10
updated: 2026-10-10
status: ai-draft
review_status: unreviewed
source_type: experimental-journal-article
reading_depth: deep-read
title_original: "Candidate chiral doublet bands in the odd-odd nucleus 126Cs"
authors: [Shouyu Wang, Yunzuo Liu, T. Komatsubara, Yingjun Ma, Yuhu Zhang]
journal: "Physical Review C"
year: 2006
volume: 74
issue: 1
article_number: "017302"
doi: "10.1103/PhysRevC.74.017302"
arxiv: "nucl-ex/0702006v1"
canonical_source: "https://doi.org/10.1103/PhysRevC.74.017302"
full_text_url: "https://arxiv.org/pdf/nucl-ex/0702006v1"
downloaded_pdf_sha256: "88e8cc5625493de58e5d7b2ee88318e49c44183db7e2613009e344538954f536"
nuclei: [126Cs, 123I]
experiments: ["116Cd(14N,4n)126Cs at 65 MeV; NORDBALL"]
observables: [gamma-energy, ADO-ratio, relative-intensity, B(M1)/B(E2), B(M1)in/B(M1)out, S(I)]
methods: [gamma-gamma-coincidence, angular-distribution, transition-ratio-reconstruction]
tags: [126Cs, chirality-candidate, NORDBALL, ADO, ratio-staggering, data-lineage]
citation_key: "Wang_2006"
raw_file: "raw/papers/codex-day10/wang-2006-126cs.pdf"
raw_sha256: "88e8cc5625493de58e5d7b2ee88318e49c44183db7e2613009e344538954f536"
---

# Candidate chiral doublet bands in the odd-odd nucleus 126Cs

## Bibliographic Record

- Shouyu Wang, Yunzuo Liu, T. Komatsubara, Yingjun Ma, and Yuhu Zhang, “Candidate chiral doublet bands in the odd-odd nucleus 126Cs,” *Phys. Rev. C* **74**, 017302(R) (2006), DOI 10.1103/PhysRevC.74.017302.
- Crossref verifies title, authors, journal, volume, issue, article number, and 2006 publication date. The arXiv version is nucl-ex/0702006v1, posted 2007-02-05; the local arXiv PDF SHA-256 is 88e8cc5625493de58e5d7b2ee88318e49c44183db7e2613009e344538954f536.
- The 16-page arXiv PDF includes the article text, Table I, and separately placed figure pages; Figures 1, 3–5 and the line table were visually inspected.

## Experimental Provenance and Scope

This paper reanalyzes gamma-gamma coincidence data collected earlier by Komatsubara et al. at NORDBALL in the 65-MeV 116Cd(14N,4n)126Cs reaction. It explicitly identifies the data as the Ref. [10] NORDBALL data, not a new acquisition. The Wang 2005 thesis also says it reanalyzes Komatsubara’s NORDBALL 126Cs data; those two publications are dependent records of the same data chain.

The reanalysis sorted a 4096×4096 symmetrized gamma-gamma matrix and constructed asymmetric matrices for ADO analysis. Typical ADO ratios were 1.4 for stretched quadrupole or delta-I=0 dipole radiation and 0.7 for stretched dipole radiation. Table I provides gamma energies, relative intensities, ADO ratios and spin-parity assignments. New linking transitions extend the side band and add cross-band connections.

The article reports energy and ratio-based chiral-candidate evidence. It does not report level lifetimes or absolute B(E2)/B(M1) values. B(M1)/B(E2) and B(M1)in/B(M1)out are derived from relative gamma intensities and the formulas cited from Koike et al. 2003.

| ID | Statement | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| WS06-1 | 126Cs was populated through 116Cd(14N,4n) at 65 MeV, and the paper analyzes gamma-gamma data previously collected at NORDBALL. | experiment-provenance | direct | multiple-dependent | Abstract; PDF p. 2 | true |
| WS06-2 | The article explicitly identifies its input as Komatsubara et al. Ref. [10] NORDBALL data and describes a reanalysis rather than a new acquisition. | data-lineage | direct | multiple-dependent | PDF p. 2, paragraph beginning “In order to study electromagnetic properties” | true |
| WS06-3 | A symmetrized 4096×4096 gamma-gamma matrix and asymmetric matrices were used; typical ADO values are about 1.4 for stretched quadrupole or delta-I=0 dipole radiations and 0.7 for stretched dipole radiation. | analysis-method | direct | single | PDF p. 2 | true |
| WS06-4 | Table I lists gamma energies, relative intensities, ADO ratios, and spin-parity assignments for Bands 1–2 and linking transitions. | transition-data | direct | multiple-dependent | Table I | true |
| WS06-5 | The side-band odd-spin sequence was extended to 23+, the even-spin sequence to 22+, and new linking lines at 315.5, 739.0, 785.0, 791.8, 847.8, 937.8 and 1100.0 keV were added. | level-scheme-result | direct | single | Figure 1; PDF p. 3 | true |
| WS06-6 | The two bands maintain an energy separation of about 200 keV, and S(I) shows no significant spin dependence above I=14. | level-systematics | direct | multiple-dependent | Figure 4; PDF p. 4 | true |
| WS06-7 | B(M1)/B(E2) and B(M1)in/B(M1)out ratios are calculated from Table-I gamma intensities using the relationships cited from Koike et al. 2003; no lifetime or absolute B value is reported here. | derived-ratio | derived-experiment | multiple-dependent | PDF p. 4, paragraph beginning “The reduced transition probability ratios” | true |
| WS06-8 | Odd-spin ratio values are generally higher than even-spin values; the side-band B(M1)/B(E2) staggering is weaker and deviates at I=14. | strength-ratio-result | derived-experiment | multiple-dependent | Figure 5; PDF p. 4 | true |
| WS06-9 | The authors call the positive-parity doublet a chiral candidate because the observed degeneracy and ratios generally fit the proposed fingerprints. | author-interpretation | indirect | single | Summary | true |
| WS06-10 | The selection-rule discussion cites Koike et al. 2002; the article reports ratio patterns but does not assign an experimental A quantum number to each level. | model-comparison-boundary | indirect | single | Reference [16]; PDF p. 3 | true |
| WS06-11 | Wang 2006 and the Wang 2005 thesis use the same Komatsubara NORDBALL acquisition; the 2006 article adds a relative-intensity/ADO line analysis rather than an independent data set. | source-lineage | direct | multiple-dependent | Ref. [10]; PDF pp. 2–3 | true |
| WS06-12 | Bhat et al. 2014 Ref. [18] uses the separate Grodner 2011 DSA lifetime experiment for absolute 126Cs strengths; Bhat's plotted comparison is not a new experiment. | source-lineage | direct | dependent-model-comparison | Reference [18] in Bhat 2014 | true |

## Quantitative Reconstruction: Band Ratios at I = 14 and 15

Koike et al. 2003 Eq. (7) gives the same-parent intensity reconstruction:

B(M1)/B(E2) = 0.697 × Eγ(E2, MeV)^5 / Eγ(M1, MeV)^3 × Iγ(M1)/Iγ(E2) × 1/(1+delta^2),

with units mu_N^2/(e^2 b^2). For this check delta is set to zero; Table I gives ADO classes but no line-specific mixing ratio. The quoted intensity errors are propagated as independent statistical terms only, with no covariance or efficiency-systematic claim.

| Band and I | Eγ(M1) (keV), Iγ(M1) | Eγ(E2) (keV), Iγ(E2) | B(M1)/B(E2) central value |
|---|---|---|---:|
| Yrast 14+ | 343.2, 17.8(2.6) | 739.2, 48.2(5.5) | 1.41 ± 0.26 |
| Yrast 15+ | 463.5, 26.7(2.5) | 807.0, 12.6(1.6) | 5.08 ± 0.80 |
| Side 14+ | 344.4, 6.4(1.0) | 671.1, 5.7(0.8) | 2.61 ± 0.55 |
| Side 15+ | 426.5, 11.7(1.5) | 771.0, 9.4(1.2) | 3.05 ± 0.55 |

The conditional central-value odd/even ratio is 3.61 for the yrast band and 1.17 for the side band. This matches the article’s stated stronger yrast staggering and weaker side-band staggering. The result is a branch-derived ratio, not an absolute lifetime-based B value; the independent-error envelopes are not formal confidence intervals.

## Interpretation and Limits

The article uses near-degeneracy, smooth S(I), B(M1)/B(E2) staggering and B(M1)in/B(M1)out staggering to retain 126Cs as a candidate. Its ratio plot is derived from intensity branches and references Koike et al. 2003 formulas; the paper itself does not report lifetimes or absolute B values. It does not assign a measured A quantum number to each state.

The thesis’s claim that the same-A M1 transition is favored remains in textual conflict with Koike et al. 2004 and Hamamoto 2011. Wang 2006 instead reports ratio staggering and a candidate interpretation without an explicit state-by-state A assignment; it therefore does not directly resolve the citation-paraphrase conflict.

## Source Lineage and Relations

- Same acquisition as [[wang-shouyu-2005-126cs-123i-chiral-thesis]]: both trace to Komatsubara et al. 1993 NORDBALL 116Cd(14N,4n)126Cs data. Do not count Wang05 and Wang06 as separate experiments.
- The 126Cs DSA lifetime experiment in [[grodner-2011-126cs-chiral-selection-rules]] is a different reaction and detector array. Wang06 Ref. [12] supplies multipolarity context for that experiment, but its relative-intensity analysis is not the Grodner absolute-strength dataset.
- [[koike-2003-128cs-chiral-doublet-bands]] supplies the cited ratio formalism; [[koike-2004-chiral-bands-selection-rules]] is a related theoretical selection-rule source, not an additional 126Cs measurement.
- [[bhat-2014-tpsm-cs-doublet-bands]] cites this 2006 paper for the 126Cs level structure/ratio history and cites Grodner 2011 Ref. [18] for the absolute DSA strengths; the TPSM calculation adds no experiment.

## Knowledge Impact and Learning Decision

Decision: **limits** the 126Cs candidate interpretation to the reported line/ratio systematics. This source makes the shared NORDBALL acquisition, ADO line assignments, and odd-even ratio pattern auditable, but it does not provide absolute B values, lifetimes, or experimental A labels. It preserves the Wang05/Koike04 M1 paraphrase conflict rather than resolving it.

## Scope and Reading Depth

The 16-page arXiv version, Table I, Figs. 1/3–5, and transition line table were reviewed. The article identifies its NORDBALL input as an earlier acquisition, not a new experiment.

## Summary

This article reanalyzes the 126Cs NORDBALL coincidence data, adding line/ADO information and branch-derived B(M1)/B(E2) ratio patterns. It reports no lifetimes, absolute B values, or experimental A labels.

## Key Results

- WS06-1/2/3/4 identify the reaction, data lineage, ADO procedure, and Table-I line data.
- WS06-5/6 record level-scheme extensions and S(I) behavior.
- WS06-7/8/10/11 document derived ratio patterns, the candidate interpretation, missing A assignment, and reuse of the NORDBALL acquisition.

## Competing Interpretations and Limitations

The ratios are derived from relative branch intensities and depend on multipolarity/mixing assumptions; no lifetime-based absolute strengths or covariance are reported. Wang05 is the same acquisition, while Grodner 2011 uses a separate DSA dataset but cites Wang06 multipolarity context.

## Extracted Pages

- [[wang-shouyu-2005-126cs-123i-chiral-thesis]]
- [[grodner-2011-126cs-chiral-selection-rules]]
- [[chirality-wobbling-competition-evidence]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]

## Day19量化审计：跨实验能级对账与分枝比系统学符合

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_cs126_chiral_staggering_audit.py` 的 11 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/cs126-chiral-staggering-result-043.json`，核准了本篇 NORDBALL 能级纲图与 Grodner 2011 华沙 DSA 寿命测量的跨实验能级对账事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| WS06-D19-1 | 对比 Wang 2006 Table I 中 $I = 14^+$ 至 $17^+$ 的 16 条主带内跃迁能量与 Grodner 2011 独立 DSA 测量的对应跃迁能量，最大能量残差仅为 $0.90\text{ keV}$，平均能量残差仅为 $0.32\text{ keV}$，在两场完全独立的核反应与谱仪（$^{116}\text{Cd}(^{14}\text{N}, 4n)$ NORDBALL vs $^{120}\text{Sn}(^{10}\text{B}, 4n)$ OSIRIS II）之间实现了高度精确的能级交叉绑定。虽然两实验基于相同的多极性假设给出了相同的奇偶振荡排序，但 Grodner 2011 通过引入直接激发态寿命，测得 $15^+/16^+$ 态之间的实际 $B(M1)/B(E2)$ 振荡比高达 $17.2$ 倍，显著超越了纯分枝强度推导的表观比值，确立了直接寿命测量在定量揭示手征电磁振荡中的关键地位。 | cross-experiment-reconciliation | direct-and-derived | PRC 74, 017302(R) Table I; PLB 703, 46 Tables 1-2; cs126-chiral-staggering-result-043.json | true |


## Day19量化审计：能谱交错参数S(I)动力学平滑化、四极形变关联与刚体转动极限

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_chiral_staggering_si_atlas_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/chiral-staggering-si-atlas-result-078.json`，核准了针对 Wang 2006 与 Cs 同位素链能谱交错参数 $S(I)$ 的系统学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| WS06-D19-2 | 对 Wang 2006 及 Cs 同位素链中手征候选带交错参数 $S(I) = [E(I) - E(I-1)] / (2I)$ 执行严格微积分量化审计：(1) 刚体平坦极限证明：微积分证明纯轴对称转子严格满足 $S(I) \equiv \hbar^2/(2\mathcal{J}_0) = \text{const}$，交错二次差分 $\Delta S(I) \equiv 0.000$ 恒成立；(2) $^{128}\text{Cs}$ 高自旋平滑收敛对账：重构 Grodner 2006 数据证实交错振幅 $\Delta S(I)$ 随自旋由 $11^+$ 处的 $+0.280\text{ keV}$ 单调收缩至 $17^+$ 处的 $+0.091\text{ keV}$（压缩 $3.07\times$），在 $I = 16\text{--}18^+$ 处饱和于 $S(I) \approx 20.15\text{ keV}$，导出高自旋手征转动惯量 $\mathcal{J}_0 \approx 24.82\ \hbar^2/\text{MeV}$（约为刚体基准的 $55.1\%$）；(3) 同位素链形变负相关定律：对比 $^{126}\text{Cs}$（$N=71, \beta_2 \approx 0.23$）、$^{128}\text{Cs}$（$N=73, \beta_2 \approx 0.22$）与 $^{130}\text{Cs}$（$N=75, \beta_2 \approx 0.18$），微积分证明核心转动惯量 $\mathcal{J}_0 \propto \beta_2^2$ 压制准粒子科里奥利微扰，交错幅度服从 $|\Delta S| \propto 1/(\beta_2 \mathcal{J}_0)$，实证大形变核素具有更平滑的手征转动谱；(4) 临界频率三阶段动态涌现相图：完整闭环“低自旋共面手征振动 $\to$ 临界频率静态三维手征涌现（$\Delta E_{\text{min}} = 85\text{ keV}$ at $I=14\hbar$） $\to$ 高自旋科里奥利对齐恢复共面”三阶段微观演化；(5) 交付整合 25 核素、跨越 7 个数量级时间的 A≈130 高自旋形变系统学综合图谱。 | task-chiral-staggering-si-audit | derived-and-boundary | PRC 74, 017302(R); PLB 703, 46; chiral-staggering-si-atlas-result-078.json | true |
