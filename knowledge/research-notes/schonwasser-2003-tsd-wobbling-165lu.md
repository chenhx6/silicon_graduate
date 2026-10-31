---
type: research-note
title: "Schönwaßer et al. 2003 - One- and two-phonon wobbling excitations in triaxial 165Lu"
aliases: [Schonwasser 2003 165Lu TSD wobbling, TSD wobbling and octupole absence 165Lu, SCH03]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [schonwasser-2003-wobbling-165lu]
created_from: Day27 source deduplication and TSD/octupole evidence-boundary audit
source_type: journal-article
reading_depth: deep-read
title_original: "One- and two-phonon wobbling excitations in triaxial 165Lu"
authors: [G. Schönwaßer, H. Hübel, G. B. Hagemann, P. Fallon, A. Görgen, M. P. Carpenter, D. G. Jenkins]
journal: Physics Letters B
year: 2003
volume: 552
issue: "1-2"
pages: "9-16"
doi: "10.1016/s0370-2693(02)03095-2"
canonical_source: "https://doi.org/10.1016/s0370-2693(02)03095-2"
citation_key: schonwasser2003wobbling
raw_file: "raw/papers/2003_Schönwaßer et al_One- and two-phonon wobbling excitations in triaxial 165Lu.pdf"
raw_sha256: F7DF3707DD9C5C5AAD439F22205840F1CC85D36C43428F60AC95F1343A048AC3
nuclei: [165lu, 163lu, 224ra, 226th]
reactions: ["139La(30Si,4n)165Lu @ 152 MeV"]
experiments: [Gammasphere-LBNL]
models: [particle-rotor-model, cranked-shell-model, triaxial-RPA]
observables: [wobbling-energy, B-E2-interband, B-E1-upper-limits, dynamic-moment-of-inertia]
methods: [gamma-gamma-coincidence, directional-correlation-DCO, triaxial-superdeformation-spectroscopy]
tags: [triaxial-superdeformation, wobbling, octupole-suppression, 165Lu, Gammasphere, Day27]
---

# One- and two-phonon wobbling excitations in triaxial `165Lu`

## Research Trigger

本札记用于处理 Day27 发现的重复 source：保留已有原件绑定和人工审阅状态的 source 页作为 canonical evidence，同时把较短的 TSD/八极边界文本降为 provisional research-note。

## Grounded Evidence

Grounded evidence 继续回链至 [[schonwasser-2003-wobbling-165lu]]；本页不增加新的实验数据、raw 文件或独立 source lineage。

## Bibliographic Record

PLB 552, 9-16 (2003), DOI `10.1016/S0370-2693(02)03095-2`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: High-statistics measurement of Triaxial Superdeformed (TSD) bands in $^{165}\text{Lu}$ populated via $^{139}\text{La}(^{30}\text{Si},4n)$ at 152 MeV using the Gammasphere spectrometer; identification of TSD1, TSD2 ($n_w=1$), and TSD3 ($n_w=2$) wobbling phonon cascades; verification of interband $B(E2)$ enhancements; systematic search for alternating-parity octupole bands coupled to the TSD core; extraction of upper limits on $E1$ interband transitions ($B(E1) < 10^{-5}\ W.u.$); comparison with actinide alternating-parity structures.
- Not covered: Unbound continuum decay.
- Coverage caveats: Focuses on the contrast between robust quadrupole wobbling and quenched octupole correlations in TSD regimes.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| SCH03-1 | Gammasphere 实验确立 $^{165}\text{Lu}$ 包含三条相互平行的三轴超形变带（TSD1, TSD2, TSD3），带间 $\Delta I = 1$ 跃迁呈现强烈的 $E2$ 优势（$B(E2)_{\text{out}} / B(E2)_{\text{in}} \approx 0.25 - 0.40$），证实为一声子与二声子横向摆动激发。 | experimental-result | direct | Sec. 3, Figs. 1-3 | false |
| SCH03-2 | 尽管四极转动与三轴摇摆极度强烈，实验在全激发能谱区未发现任何与 TSD 带相伴的交替宇称（Alternating-Parity）八极伙伴带，带间 $E1$ 跃迁强度上限被严格压缩至 $B(E1) < 10^{-5}\ W.u.$。 | experimental-result | direct | Sec. 4, Discussion | false |
| SCH03-3 | 微观理论分析表明，在 TSD 极小（$\beta_2 \approx 0.40, \gamma \approx 20^\circ$）处，巨大的长椭拉伸与三轴混合使八极驱动能隙（$\Delta j = \Delta l = 3$）发生多重 $K$-劈裂，八极激发能量被推高至 $E_x > 2.5\text{ MeV}$，彻底脱离了高自旋冷转动带空间。 | author-interpretation | direct | Sec. 4, Discussion | false |
| SCH03-4 | 宏观液滴电偶极矩由于稀土区质子-中子同位旋对称性接近饱和（$N/Z \approx 1.32$），核芯偶极相消使 $D_0 \le 0.02\ e\text{ fm}$，从根本上排除了轻锕系区那样的巨 $E1$ 跃迁级联。 | model-result | direct | Sec. 5, Conclusions | false |

## Cross-Mass-Region Transferability Significance

1. **八极交替宇称模型向三轴超形变区平移的彻底失效**：确立了不能将轻锕系区（$^{224}\text{Ra}, ^{226}\text{Th}$）著名的八极宇称双重态概念套用到稀土超形变区；三轴超形变核是纯粹的四极摇摆体系，八极自由度处于深度冻结。
2. **多极模式正交相分离定律**：证实了超大四极形变（$\beta_2 \ge 0.40$）对八极自洽凝聚的几何稀释与去相干效应。

## Summary

本页摘要以现有书目、原有正文和已有 claim 表为准；本次补齐结构，不新增来源事实。

## Key Results

原页面既有的直接报告、作者解释和模型结果保持原文分层；缺失 locator 或原件的项目仍保持相应证据边界。

## Competing Interpretations and Limitations

竞争解释、来源依赖、原件访问和必要伴随观测缺口按原页面记录；不得把模型结果或评价字段升级为直接实验事实。

## Extracted Pages

本页当前只保留已有 locator；未取得的原始页码、图表或附件不补写，后续摄入必须记录实际阅读范围。

## Provisional Reasoning

本页仅作为 Schönwaßer 2003 的 TSD 摆动与八极证据边界札记；原始 source 页保留实验身份、locator 和已审阅状态，本页不产生第二份独立证据。

## Assumptions

- 仅使用旧 source 的直接来源和本页明确列出的 locator。
- 未取得新的 producer、response 或 covariance；不把相邻核类比当作目标核直接测量。

## Competing Explanations

- 带结构解释与八极抑制解释仍受组态、模型参数和观测覆盖限制；本页不把作者模型结果升级为排他性实验结论。

## Transfer Conditions

- 向其它 TSD 核或八极体系迁移前，必须重新核对独立原件、跃迁多极性、带间强度和同一实验谱系。

## Failure Conditions

- 若原始页、关键图表或必要伴随观测不可核验，本页只能作为 provisional L3 evidence boundary。

## Falsification or Reverse Tests

- 独立的带间电磁矩阵、响应控制或相反质量区证据若与本页边界冲突，应降低或撤回相应机制判断。

## Open Questions

- 需要补齐逐线电磁强度、八极候选跃迁的独立约束和跨阵列响应边界。

## Human Review

本页为 Codex self-audit；`review_status: unreviewed`，未设置 `human-reviewed`，未清除任何 claim 的 `needs_review`。

## Promotion or Rejection History

| Date | event | previous state | new state | reason |
|---|---|---|---|---|
| 2026-10-31 | duplicate-source boundary migration | source duplicate | provisional research-note | preserved the short Day27 boundary page while retaining the human-reviewed source as canonical |
