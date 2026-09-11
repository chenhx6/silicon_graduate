---
type: source
title: "Guo 2021：对 135Pr 横向摇摆实验判据的评论"
aliases: [Guo 2021 135Pr wobbling comment, comment on transverse wobbling in 135Pr]
created: 2026-09-13
updated: 2026-09-13
status: ai-draft
review_status: unreviewed
source_type: arxiv-comment-methodological-reanalysis
reading_depth: deep-read
title_original: "Comment on 'Transverse Wobbling in 135Pr [Phys. Rev. Lett. 114, 082501 (2015)]'"
authors: [S. Guo]
journal:
year: 2021
volume:
pages: 2
doi:
arxiv: 2011.14364
language: en
canonical_source: "https://arxiv.org/abs/2011.14364"
zotero_item_key:
citation_key:
zotero_uri:
library_file: "raw/papers/gpt/_incoming/20260912-135pr-refresh/guo-2020-comment-135pr-wobbling.pdf"
raw_file: "raw/papers/gpt/_incoming/20260912-135pr-refresh/guo-2020-comment-135pr-wobbling.pdf"
raw_sha256: "cc9e43e07f23c3e85250c4acf55032d1085901e14d075591bcb141e5fddcdafc"
nuclei: [135pr]
reactions: []
experiments: [atlas-gammasphere-135pr-o16-80mev, tifr-inga-135pr-o16-80mev]
models: []
observables: [multipole-mixing-ratio, linear-polarization-asymmetry, angular-distribution]
methods: [angular-distribution, linear-polarization-asymmetry]
tags: [a130, 135pr, wobbling-counter-evidence, mixing-ratio, polarization, methodological-comment]
---

# Guo（2021）：对 `135Pr` 横向摇摆实验判据的评论

## Bibliographic Record

S. Guo，*Comment on “Transverse Wobbling in `135Pr` [Phys. Rev. Lett. 114, 082501 (2015)]”*，arXiv `2011.14364v3`，2021-01-13 更新，2 页。该文没有在本地元数据中确认 DOI；arXiv 页面和 PDF 的题名、作者、版本日期与引用的 Matta 2015 DOI 相符。本地 PDF SHA-256 为 `cc9e43e07f23c3e85250c4acf55032d1085901e14d075591bcb141e5fddcdafc`。

## Scope and Reading Depth

- `deep-read`：2 页全文及 Fig.1–2、参考文献均已阅读并视觉核对。
- 重点范围：Matta 2015 747、813、755 和 594 keV 连接跃迁的 angular-distribution 双解、mixing-ratio 分支和 polarization interpretation。
- 未覆盖：Matta/Garg 原始实验 raw matrices、完整 polarization calibration、原始 `σ/I` 输入和独立重复实验；本文是 comment/reanalysis，不是新实验。

## Summary

Guo 对 Matta 2015 的 transverse-wobbling 判据提出方法学质疑。评论指出，ΔI=1 `M1/E2` 角分布在适当的 alignment 参数下通常同时允许一个 `|δ|>1` 与一个 `|δ|<1` 的解；若只绘制其中一支并与纯 M1 曲线比较，不能说明大 `|δ|` 已被唯一确定。评论还指出，747 和 813 keV 的正 polarization asymmetry 本身不能唯一证明主要 electric character，因为在假定的 `σ/I` 范围内两个 mixing-ratio 解都可给出正 polarization。其结论是，仅依据 Matta 2015 已报告的实验判据不足以无保留地声明 wobbling，仍需更精确的分析或实验。

## Reanalysis Basis

该 comment 使用 Matta 2015 已报告的角分布/偏振结果作曲线比较，不提供新的 `135Pr` event sample。Fig.1 对 747、813、755 和 594 keV 连接跃迁分别绘制纯 M1、一个大 `|δ|` 解和一个小 `|δ|` 解；文中给出的代表值包括 747 keV 的 `δ=-1.24` 与 `-0.64`、813 keV 的 `-1.54` 与 `-0.50`、755 keV 的 `-2.38` 与 `-0.36`、594 keV 的 `-1.74` 与 `-0.46`（594 keV 另讨论由 Matta 标记的 polarization curve 得到的 `-0.16`）。Fig.2 在不同 `σ/I` 下展示 polarization coefficient 随 `δ` 的变化。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | research_status | needs_review |
|---|---|---|---|---|---|---|---|
| GU21-1 | 评论认为 Matta 2015 wobbling 指认的关键实验依据是 wobbling band 与 normal band 之间的 E2-dominated connecting transitions，但已报告信息不能排除 M1-dominated character。 | author-interpretation | direct | single | PDF p.1, abstract | completed | false |
| GU21-2 | 在适当的 `σ/I` 和 `δ` 假设下，747、813、755 和 594 keV angular distributions 可同时与大 `|δ|>1` 和小 `|δ|<1` 分支相容；评论反对只展示单一解便称其唯一确定。 | experimental-criterion + author-interpretation | direct | single | PDF pp.1–2, Fig.1 and surrounding text | completed | false |
| GU21-3 | 对 747、813 keV，评论计算指出两个 mixing-ratio 分支在假设的 `σ/I` 范围内都可得到正 polarization；因此正 asymmetry sign 不能单独排除小 `|δ|` 或证明主要 electric character。 | experimental-criterion | direct | single | PDF pp.1–2, Fig.2 and text | completed | false |
| GU21-4 | 评论指出从 INGA 数据推导 polarization value 还应明确 calibrated polarization sensitivity 和逐跃迁 `σ/I` 参数，而 Matta 2015 的报告未在评论所检查的范围内充分说明这些输入。 | our-inference + author-interpretation | direct | single | PDF p.2, paragraph before conclusion | completed | false |
| GU21-5 | 评论的结论是，依据 Matta 2015 的已报告实验结果不足以宣布 wobbling 已被确定，需要进一步实验研究澄清该带性质。 | author-interpretation | direct | single | PDF p.2, conclusion paragraph | completed | false |
| GU21-6 | 该文是对 Matta 2015 数据/报告的 methodological comment，不是新的 `135Pr` reaction、detector run 或 independent measurement。 | our-inference | direct | multiple-dependent | PDF pp.1–2, title, abstract and Ref.[1] | completed | false |

## Competing Interpretations and Limitations

- Guo 的双解曲线是基于已发表结果和假设参数的再分析，不能替代 Matta/Garg 的原始角分布计数、响应函数和统计协方差；它构成 counter-methodological evidence，而不是单独的实验重复。
- Lv 2022 使用不同的 `100Mo(40Ar,1p4n)` JUROGAM II 数据，以 `P-R_ac` 联合约束得到小 `|δ|`；该独立 counter experiment 与 Guo comment 的重分析结论方向相近，但证据来源不同。
- Sensharma 2026 对旧 746/812/754 keV Gammasphere angular distributions 重新计算 χ²，报告大 `|δ|` 分支有更低 χ²，并对 Lv 的相关质疑作出回应；这与 Guo 的“两个解均可相容”形成需要统一 raw-data、误差和 fit convention 的方法学冲突。
- 正 polarization asymmetry、`R_ac`、mixing ratio 和 E2 fraction 各自约束不同性质；任何一个单项都不能独自完成 wobbling phonon identity 的判定。
- 评论不讨论 `135Pr` DB1/DB2 的 2026 新连接、绝对寿命或 chiral-partner interpretation，不能扩大为对 2026 论文全部结果的否定。

## Codex Self-audit

| 审计项 | 判断 | 证据 |
|---|---|---|
| Identity/locator | arXiv v3 题名、作者、日期、2 页 PDF、SHA 和 Fig.1–2 已核对；无 DOI 不猜测。 | arXiv metadata；PDF pp.1–2；manifest |
| Claim separation | 双解和 polarization 是 comment 的方法学论证；“wobbling 不足以宣布”保留作者归属；无新实验事实被添加。 | GU21-1–6 |
| Independence | 本 comment 依赖 Matta 2015 报告；不计为新实验，和 Lv 2022、Sensharma 2026 分开记录。 | GU21-6；`135Pr` project |
| Boundary | 未读取/重建原始 INGA calibration、raw matrices 或 covariance；不把曲线重画当成 L4。 | Competing Interpretations and Limitations |
| Review state | 页面 `unreviewed`；GU21 claims 的 `needs_review: false` 仅是 Codex direct-source self-audit，不表示用户审核。 | frontmatter；GU21-1–6 |

## Knowledge Impact and Learning Decision

- **新增方法学反证**：把 `135Pr` 争议中的“角分布双解”和“偏振正号是否足够”固定为一个可回到 Fig.1–2 的直接 counter-source。
- **不改变最终裁决**：该 comment 增强了 Lv 2022 之前的质疑谱系，但没有统一重做三方 raw analysis；项目继续保留 wobbling、TiP/realignment、signature-partner 和 chiral interpretations 的并列状态。
- **Persistence**：建立 comment source，更新 `135Pr` nucleus、争议 project、index 和批次报告；不创建新 band page，不把 comment 当 independent experiment，不启动 L4。

## Extracted Pages

- Nucleus: [[135pr]]
- Bands: [[135pr-yrast-band]]、[[135pr-side-band]]、[[135pr-signature-partner-band]]
- Experiments: [[atlas-gammasphere-135pr-o16-80mev]]、[[tifr-inga-135pr-o16-80mev]]
- Concepts/observables: [[transverse-wobbling]]、[[multipole-mixing-ratio]]、[[linear-polarization-asymmetry]]
- Project: [[135pr-wobbling-controversy]]

## Related Knowledge

- [[matta-2015-transverse-wobbling-135pr]]
- [[lv-2022-evidence-against-wobbling-135pr]]
- [[sensharma-2019-two-phonon-wobbling-135pr]]
- [[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]]
- [[135pr-wobbling-controversy]]

## Later Paper / Q&A Gate

若后续问答或论文写作使用 Guo comment 的双解、偏振或“wobbling 尚未确定”表述，需同时列出其 reanalysis 性质、假定的 `σ/I`/polarization response 边界，以及后续 Lv 2022 与 Sensharma 2026 的相反/回应证据；不得把该短评写成新的实验测量。
