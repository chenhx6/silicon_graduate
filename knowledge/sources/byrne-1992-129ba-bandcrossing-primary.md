---
type: source
title: "Byrne 1992：129Ba 分支强度、DCO与模型辅助电磁比"
aliases: [Byrne1992 Ba129 bandcrossings, 1992By03 primary]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-model-comparison
reading_depth: read
title_original: "High-spin bandcrossings in 129Ba"
authors: [A. P. Byrne, K. Schiffer, G. D. Dracoulis, B. Fabricius, T. Kibedi, A. E. Stuchbery, K. P. Lieb]
journal: Nuclear Physics A
year: 1992
volume: 548
pages: 131-158
doi: 10.1016/0375-9474(92)90080-4
canonical_source: https://doi.org/10.1016/0375-9474(92)90080-4
citation_key: Byrne1992Ba129
citation_key_origin: task-bibliography-in-ba129-model-readiness
raw_file: raw/papers/gpt/query/20261105-ba129-model-readiness/byrne1992-main.pdf
raw_sha256: e7fd04cd2eb33070e7b0d9e60dfdef70b0bba2f45a3c24dc05b6aeee05ed9fa0
archive_required: true
nuclei: [129ba]
methods: [in-beam-gamma-spectroscopy, dco, pulsed-beam-timing]
observables: [branching-ratio, lifetime, mixing-ratio, bm1-be2-ratio]
tags: [a130, primary-source, branching, model-dependence, holdout]
---

# 不把模型辅助的 B 比当作独立电磁测量

## Summary

原文提供129Ba高自旋能级、经角关联校正的符合强度及带交叉解释。
其中B(M1)/B(E2)分析含由光子分支和pure-K/等Q假设导出的δ，
因此这些B比不能作为独立于分支和该模型的保留检验。
正文与封面束流能量字段不同，寿命定义亦需与评价半衰期分开。

## Bibliographic Record

原件28页，来源为出版商 FULL XML 明列的 MAIN attachment。封面题名使用
复数“bandcrossings”，API题名为单数，DOI/作者/卷页一致。本次保留原件题名。

## Scope and Reading Depth

读取引言、§§2–3方法与低能连接、§4.1–4.5讨论及结论；视觉核
p.135 Table1表头和153.8/364.7行、p.137续表、p.154 Eqs.2–4。
未逐条复核所有高自旋峰放置或全部28页图中数据，不称事件重分析。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BY92-1 | §2和Table1写86-MeV的116Cd(18O,5n)采集；封面反应框却印82 MeV。此字段差异单列，本文分析采用明确的正文/表头条件，不混成两个独立实验。 | source-field-discrepancy | direct-original | pp.131–133；p.135 Table1 | true |
| BY92-2 | 相对强度由单谱和符合谱提取；Table1明确符合谱提取时校正角关联效应。不能把这些数误称未经校正原始counts。 | experimental-method | direct-original-visually-checked | p.133 §3.1；p.135 Table1 caption | true |
| BY92-3 | 有限角度不足以可靠求a4或δ；σ/I约0.3由所选纯E2线定标，DCO依其实际角组与门定义。 | method-limitation | direct-original | pp.133、140–141 §3.2 | true |
| BY92-4 | 182和2463-keV态的23(2)、68(2) ns在正文是mean lives，不能直接与ENSDF的半衰期字段等同。 | quantity-identity | direct-original | pp.145–146；封面摘要 | true |
| BY92-5 | §4.4用光子分支构造B(M1)/B(E2)，其中δ经“相同Q、pure K”的转动模型关系推得。Fig14的B比不是额外独立于分支和该模型的观测。 | model-assisted-derived-observable | direct-original-visually-checked | p.154 Eqs.2–3及其间文字 | true |
| BY92-6 | CSM/TRS解释包含组态与形状极化假设；作者明确提醒γ-soft体系中对齐/交叉解释有条件。 | author-interpretation | direct-original | pp.148、151–157 | true |

## Equation consistency check

以下是本任务推导，不改原式。p.154将
\(\lambda=I_\gamma(I\to I-2)/I_\gamma(I\to I-1)\) 定义为光子分支比，
而印刷Eq.3的右端只含 \(\lambda^{-1}\) 与两个CG系数平方之比。
按同页“pure K、相同Q”的前提和E2光子宽度的 \(E_\gamma^5\) 因子，
应有

\[
\frac{1}{\delta^2}
=\frac1\lambda
\left(\frac{E_{\gamma,\Delta I=2}}{E_{\gamma,\Delta I=1}}\right)^5
\frac{|\langle IK20|I-2,K\rangle|^2}
{|\langle IK20|I-1,K\rangle|^2}-1.
\]

原印刷式缺少能量比，除非该式另用了经过能量重标度的λ。
这是一处**定义与印刷式的相容性问题**；没有作者程序，不能断言Fig14实际
漏用了能量因子，也不能据此宣称实验数据或作者物理解读被推翻。

## Competing Interpretations and Limitations

已报告的光子强度可按其方法说明用于新的模型比较；完整raw事件缺失不自动
禁止这种用途。须声明协方差、IC、弱分支和门处理边界。不能同时把RI、由RI
导出的δ及B比作为三套独立数据，更不能以这些模型导出δ作为新模型的盲检验。

## Knowledge Impact and Learning Decision

`supports`：1992By03原件闭合了评价RI的出处与所声明的角关联修正。
`limits`：优先使用逐母态光子比，保留模型辅助B比为对照而非独立holdout。
本页提供模型检验的数据分层，不新增129Ba模式指认。

## Extracted Pages

- [[ba129-model-input-and-holdout-contract]]
- [[ba129-rank4-identifiability]]
- [[nndc-2014-129ba-365-coefficient-records]]

## Human Review

仅Codex原件自审。印刷式问题保留needs_review，不冒称作者erratum或human-reviewed。
