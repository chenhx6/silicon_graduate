---
type: source
title: "Lv et al. 2022 - Experimental evidence for transverse wobbling bands in 136Nd"
aliases: [Lv 2022 136Nd transverse wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Experimental evidence for transverse wobbling bands in 136Nd"
authors: [B. F. Lv, C. M. Petrache, R. Budaca, A. Astier, K. K. Zheng, P. Greenlees, H. Badran, T. Calverley, D. M. Cox, T. Grahn, J. Hilton, R. Julin, S. Juutinen, J. Konki, J. Pakarinen, P. Papadakis, J. Partanen, P. Rahkila, P. Ruotsalainen, M. Sandzelius, J. Saren, C. Scholey, J. Sorri, S. Stolze, J. Uusitalo, B. Cederwall, A. Ertoprak, H. Liu, S. Guo, J. G. Wang, H. J. Ong, X. H. Zhou, Z. Y. Sun, I. Kuti, J. Timár, A. Tucholski, J. Srebrny, C. Andreoiu]
journal: Physical Review C
year: 2022
volume: 105
pages: 034302
doi: 10.1103/PhysRevC.105.034302
canonical_source: https://doi.org/10.1103/PhysRevC.105.034302
citation_key: lv_2022_Experimentalevidence
raw_file: "raw/papers/2022_Lv et al_Experimental evidence for transverse wobbling bands in Nd 136.pdf"
raw_sha256: C5C8A30FE8450372D97DD09FD004A4FF9C1E4427BC837EE7AA157C3DA07D9D69
nuclei: [136nd]
reactions: ["100Mo(40Ar,4n)136Nd"]
experiments: []
models: [particle-rotor-model, triaxial-projected-shell-model]
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio]
methods: [two-point-angular-correlation-ratio, linear-polarization-asymmetry]
tags: [experiment-ingest, transverse-wobbling, even-even, two-quasiparticle]
---

# Transverse wobbling bands in `136Nd`

## Bibliographic Record

PRC 105, 034302 (2022), DOI `10.1103/PhysRevC.105.034302`; the supplied PDF is a self-archived published version and matches the BibTeX record.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full published-version text, L1/L3 bands, contamination audit, combined `P-R_ac`, 751-keV `δ`, wobbling energy and new two-quasiparticle PRM.
- Not covered: earlier same-dataset papers' full experimental details and independent calculation.
- Coverage caveats: only one connecting transition permits a combined polarization/correlation mixing-ratio extraction.

## Paper Question and Scientific Motivation

- Author-explicit motivation: test the predicted two-quasiparticle transverse-wobbling assignment of bands L1/L3 in even-even `136Nd` using a clean connecting transition (PDF pp.1-2).

## Method and Design Logic

- Audit four links for contamination, combine polarization and two-point angular correlation for the 751-keV line, derive δ/E2 fraction, and compare E_wob and electromagnetic ratios with a two-quasiparticle PRM (PDF pp.2-5, Figs.1-5).

## Key Evidence and Reasoning Chain

- One clean mixed M1-dominated link + decreasing E_wob → necessary experimental support; two-quasiparticle PRM mapping → transverse interpretation; model electromagnetic parameters are normalized to the same single point.

## Summary

The paper reports necessary experimental evidence for a two-quasiparticle transverse-wobbling interpretation in even-even `136Nd`. Its link is M1-dominated (`19%` E2), explicitly differing from one-quasiparticle odd-A cases.

## Experimental or Theoretical Setup

High-statistics JuroGam II dataset from the previously documented `100Mo(40Ar,4n)136Nd` experiment. This paper refers setup details to earlier same-run publications and focuses on `R_DCO`, `R_ac` and polarization.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV22-1 | Bands L1 and L3 are treated as predicted zero-/one-phonon candidates built on a two-quasiproton `πh11/2^2` configuration. | author-interpretation | indirect | PDF pp.2-3, Fig.1 | true |
| LV22-2 | Four L3→L1 `ΔI=1` links are known, but contamination/weakness prevents polarization analysis for 768, 785 and 740 keV. | experimental-fact | direct | PDF pp.2-3 | true |
| LV22-3 | Combined polarization and `R_ac` for the clean 751-keV `17+→16+` link yields `δ=-0.48^{+0.13}_{-0.14}`, corresponding to about `19%` E2. | experimental-criterion | direct | PDF pp.3-4, Figs.2-3 | true |
| LV22-4 | The paper explicitly states the link is M1-dominated, unlike one-quasiparticle wobblers, because two aligned quasiprotons give larger M1 matrix elements. | author-interpretation | indirect | PDF p.4 | true |
| LV22-5 | Experimental `E_wob` decreases with spin and is reproduced by a rigid two-quasiparticle PRM. | model-result | direct | PDF p.4, Fig.4 | true |
| LV22-6 | The E2 operator's second-order term is fixed to the single experimental `B(E2)_out/B(E2)_in` point; `g_eff/Q` is fitted to the 751-keV `δ`. | model-result | direct | PDF p.5, Fig.5 | true |
| LV22-7 | Authors conclude this is the second even-even transverse-wobbling case. | author-interpretation | indirect | PDF p.5, Summary | true |

## Nuclear Structure Information

L1/L3 are assigned as zero-/one-phonon bands on πh11/2². Three of four connecting transitions cannot support equivalent polarization analysis because of weakness/contamination.

## Authors' Interpretation

The authors explicitly argue that two-quasiparticle wobbling can have an M1-dominated link, unlike common odd-A one-quasiparticle criteria.

## Model Results

The rigid PRM reproduces E_wob and selected ratios, but second-order E2 and g_eff/Q parameters are fixed to the sole usable experimental transition point.

## Competing Interpretations and Limitations

The model normalizes key electromagnetic parameters to the only measured link/strength point and assumes rigid short-axis quasiparticle alignment; high-spin discrepancies are attributed to alignment depletion. The conventional “predominant E2” criterion is not transferable unchanged to this two-quasiparticle case.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| LV22-AR-1 | Core reconstruction | Direct evidence is one clean M1-dominated mixed link plus decreasing E_wob; two-quasiparticle wobbling geometry is model-dependent. | Key Results and Competing Interpretations above | unreviewed |
| LV22-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| LV22-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| LV22-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| LV22-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| LV22-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: Direct evidence is one clean M1-dominated mixed link plus decreasing E_wob; two-quasiparticle wobbling geometry is model-dependent.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| limits | [[wobbling-motion]] | Two-quasiparticle candidate with M1-dominated connecting transition. |
| limits | [[interband-e2-strengths]] | Demonstrates configuration-dependent criterion boundaries. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `LV22-3`/`LV22-4`, 751-keV link, Figs.2-3 — Evidence: δ≈-0.48 and only ~19% E2, so the clean link is M1 dominated. Agent inference: this is a configuration-specific exception, not support for a universal E2-dominant rule. User check: sign/uncertainty and contamination audit. Risk: mislabeling it E2 dominated reverses the experimental result.

### P1

- `LV22-6`, Fig.5 — Evidence: second-order E2 and g_eff/Q are fixed to the sole usable point. Agent inference: model agreement is not an independent multi-point prediction. User check: normalization procedure and remaining predictions. Risk: fitted reproduction may be overstated as validation.

### P2/P3

- P1: rigid alignment/high-spin depletion. P2/P3: metadata/navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[136nd]]
- Concepts: [[transverse-wobbling]]
- Methods: [[two-point-angular-correlation-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

P0: do not describe the 751-keV link as E2-dominant.


## Day18定量审计：136Nd连接跃迁强度与PRM单点定标边界

在Day18正式学习中对本文Table/Fig数据进行深入定量审计，raw SHA256 `C5C8A30FE8450372D97DD09FD004A4FF9C1E4427BC837EE7AA157C3DA07D9D69`已核。原LV22-1–7各claim及`human-reviewed`状态完全保留；新LV22-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV22-D18-1 | 本文751 keV（17+→16+）连接跃迁是四条候选线中唯一获得有效线偏振与 $R_	ext{ac}$ 测量的跃迁；其 $\delta = -0.48^{+0.13}_{-0.14}$ 对应 $E2$ 份额仅为 $18.7\%$（$10.9\%	ext{--}27.8\%$），与奇质量数wobbler中 $E2 > 90\%$ 的主导特征截然不同。Fig. 5中两准粒子PRM理论曲线的二阶E2参数（$\chi eta_2 = 2.14 	imes 0.185$）与M1参数（$g_	ext{eff}/Q$）系完全由这单一实验点和实验 $\delta$ 强制匹配定标而来，因此模型曲线的高自旋外推是对该单点的参数化延拓而非无参预测。 | task-rate-and-model-audit | derived-and-boundary | PDF pp.3–5 Figs.3–5；新lv22-136nd-wobbling-result-017 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/lv22-136nd-wobbling-contract-017.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/lv22-136nd-wobbling-result-017.json)4项检查全过，确立了136Nd多能带谱系中跃迁强度提取与理论定标的真实边界。

## Day19量化审计：751 keV混合比M1主导性与单点参数化定标边界

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_nd136_chiral_wobbling_crossing_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/nd136-chiral-wobbling-crossing-result-049.json`，核准了 $^{136}\text{Nd}$ 候选横向摇摆连接跃迁多极混合比的物理性质：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV22-D19-2 | 对四条候选 $L3 \to L1$ 连接跃迁进行完整实验多极性审计，确认仅有 751 keV（$17^+ \to 16^+$）获得有效线偏振与 $R_{\text{ac}}$ 提取（其余 740, 768, 785 keV 均因弱或污染无法分析）。751 keV 的混合比 $\delta = -0.48^{+0.13}_{-0.14}$ 导出电四极 $E2$ 份额仅为 $18.73\%$（$10.91\%\text{--}27.77\%$），磁偶极 $M1$ 份额高达 $81.27\%$（$72.2\%\text{--}89.1\%$）。这一 $M1$ 压倒性特征与经典单粒子横向摇摆（$E2 > 90\%$）完全相左。理论 PRM 曲线的高自旋行为依赖于将二阶 $E2$ 参数与 $M1$ 参数强制对齐该单一实验点，因此偶偶核 $^{136}\text{Nd}$ 尚未具备多能级多极性与绝对跃迁寿命所要求的摆动模式充分判定依据。 | task-multipole-and-wobbling-audit | derived-and-boundary | PDF pp.3-5 Figs.3-5; nd136-chiral-wobbling-crossing-result-049.json | true |
