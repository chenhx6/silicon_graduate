---
type: research-note
title: "P-ADO benchmark 的 Zobel 1980/1983 source lineage 审计"
aliases: [Zobel 1980 1983 lineage audit, 67Ga benchmark lineage]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [zobel-1980-magnetic-substate-distributions, zobel-1983-energy-projectile-alignment]
created_from: "P-ADO paper source-lineage audit"
scope: pado/source-lineage/67ga/1980-1983
nuclei: [67ga]
tags: [pado, zobel, source-lineage, 67ga, covariance-boundary]
---

# P-ADO benchmark 的 Zobel 1980/1983 source lineage 审计

## Research Trigger

P-ADO 文章使用 Zobel 1983 Table 1 的 `^{67}Ga` 958-keV pure-E2 十行表格。
统计审查指出，Zobel 1980 中也存在同一 parent/transition 的相关输入，不能把
两篇文章自动当作独立实验或静默合并。

## Grounded Evidence

- Zobel 1980 source 页的 Z80-17 记录 `^{67}Ga` 958.0-keV
  \(13/2^+\to9/2^+\) 行，并指出 Table 1 的 reaction-A 条件为
  \(^{57}\mathrm{Fe}+^{12}\mathrm C\) at 40.0 MeV。
- Zobel 1980 source 页的 Z80-18 记录该 Table 1 行引用 Ref.9，即 Zobel 等
  *Nuclear Physics A* 316, 165--188 (1979)；该 work 与 Zobel 1983 的 Ref.4
  身份相同。
- Zobel 1983 source 页的 Z83-13 记录四条 selected E2 的纯度/零 mixing-ratio
  依据依赖 Ref.4 (1979) 和 Ref.5 (1980)；Z83-11/Z83-12 记录 1983 Table 1
  的 quoted errors、row-internal covariance 缺失和 alpha-pair error ellipse
  边界。
- 当前 Wiki 原件和 source pages 没有提供足以证明 1979、1980、1983 三篇文章
  使用相互独立 raw acquisition、共同 raw event set 或同一 fitted output 的
  producer-level 记录。

## Provisional Reasoning

当前最强的 source-level 判断是：1980、1983 和 1979 构成相关文献谱系，至少
存在共同实验/方法依赖的可能；不能把它们作为三票独立证据。1983 Table 1 仍可
作为本文 canonical public benchmark，因为本文明确使用其 printed p.392 /
PDF p.4 Table 1、反应标签和 quoted marginal errors；这只是 fixture identity
选择，不是对 raw acquisition 独立性的证明。

## Assumptions

文章当前只使用 1983 Table 1 的十行拟合摘要，不从 1980 表格补行、不平均两篇
文章的数值、不把 1979 Ref.4 的 metadata 当作 raw data。

## Competing Explanations

- 1980 与 1983 可能使用同一实验谱系的不同分析版本；
- 也可能是不同 acquisition，但两文共享同一 level-scheme、purity 或方法
  calibration；
- 表格差异可能来自不同 beam condition、拟合合同、版本或引用链，而不是
  物理变化；
- 在没有 producer/raw provenance 时，不能从数值差异反推哪一种解释。

## Transfer Conditions

如果未来取得 1979/1980/1983 的 raw spectra、fit logs、beam-current records、
detector response 或作者/实验组说明，才能把 lineage 从 `dependent-source
boundary` 升级为独立 acquisition 或同源 reanalysis 的确定判断。

## Failure Conditions

若文章把 1980、1983 和 1979 当作独立实验重复计数，或用 1980 数值静默修正
1983 fixture，PADO-02 和 PADO-12 必须退回 unresolved，不能进入 final paper
claim set。

## Falsification or Reverse Tests

逐篇对照 reaction、beam energy、target、level identity、quoted errors、reference
chain 和 data-generation wording；寻找作者明确写出的 “same data”, “previous
measurement”, “new measurement” 或 analysis-version 说明。仅凭 DOI、相同核素或
相似数值不能完成独立性判断。

## Open Questions

- 1979 `NPA 316` raw/fit provenance 是否能合法取得？
- 1980 Table 1 与 1983 Table 1 的差异是否由同一 analysis lineage 产生？
- 1983 Ref.5 对 1980 的引用是方法依赖、数据依赖还是两者兼有？
- 作者是否愿意在最终稿中明确把 1983 fixture 标为 canonical dependent source？

## Human Review

本页是 Codex self-audit；PADO-02/PADO-12 仍需作者对最终措辞和 source lineage
做定向确认。

## Promotion or Rejection History

2026-11-05：将 1980/1983 关系从未声明风险提升为显式 dependent-source boundary；
没有把两篇文章合并为独立实验，也没有修改任何 raw 原件。
