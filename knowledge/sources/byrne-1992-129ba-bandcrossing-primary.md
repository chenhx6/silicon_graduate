---
type: source
title: "Byrne 1992：129Ba 分支强度、DCO与模型辅助电磁比"
aliases: [Byrne1992 Ba129 bandcrossings, 1992By03 primary]
created: 2026-11-05
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-model-comparison
reading_depth: skimmed
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

## 2026-11-27 — 馆藏原件与覆盖核对

- {"start_page": 1, "end_page": 8, "sections": "刊头、§§1–3.2前段、图1与表1表头及可辨行，续表门脚注局部可读"}
- {"start_page": 10, "end_page": 19, "sections": "§3.2续段、正负宇称能级、异能态、§4.1开头及图3–11可辨图注，式(1)和角度排印待核"}
- {"start_page": 21, "end_page": 23, "sections": "§4.1续段、§4.2 signature splitting、图13及§4.3异能态解释"}
- {"start_page": 24, "end_page": 28, "sections": "§4.3末段、§§4.4–4.5、图14图注、§5结论及参考文献，公式仅作局部辨读"}
- 本次获取的具体覆盖：查读全部28个页标，从可辨正文读到实验、数据分析、讨论和结论。物理第9页图2缺可读图注，第20页旋转提取使连续论证、图12和表2不可完整阅读，多页表格、谱图与公式只能局部辨认。本次为部分文字审读，无视觉核验。建议仅接受既有同版 read 明列的分节与局部核对范围。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A17-1 | 相对 γ 强度由 86 MeV 的 116Cd(18O,5n) 数据的单谱和符合谱提取，表1明确说明符合谱强度经过角关联修正。DCO 多极性判断依赖实际探测器角组、所用 E2 门及归一化。作者说明有限角度不能可靠提取 a₄ 或 δ。 | 实验数据与提取方法 | source-reported | 物理第3–4页§§3.1–3.2及图1、第5–8页表1及门脚注、第10–11页式(1)、图3和正文。角度与式(1)待核第3–4、10页。 | true |
| A17-2 | 正文报告 182 keV 和 2463 keV 态的平均寿命分别为 23(2) ns、68(2) ns。2463 keV 态另见 126、316 keV 衰变分支，作者结合连接关系及转换强度证据给出 23/2⁺ 指认。 | 实验结果与能级指认 | source-reported | 物理第15页图7–8、第16页计时与分支正文、第27页结论。图7所示跃迁待核第15页，分支放置待核第9页图2。 | true |
| A17-3 | 图14的数据比值由光子分支导出。§4.4 的 δ 估计采用相同四极矩和纯 K 的转动模型关系。图14的计算曲线另使用实验对齐量以及引入的 Q₀、g 因子等输入。 | 模型辅助导出量 | source-reported | 物理第24页§4.4及式(2)–(4)，第25页图14及说明。式(2)–(4)原排印待核第24页，点线身份待核第25页。 | true |
| A17-4 | 作者用 CSM 和所引 TRS 系统学把正、负宇称带的首次回弯主要归于 h₁₁/₂ 质子对对齐，并提出伴随形状极化。更高频率的中子对齐和 2463 keV 态的高 K 三准中子组态均属作者指认。 | 作者解释 | source-reported | 物理第17–19页图9–11、第20页图12和表2待核、第21–23页图13与讨论、第27页结论。 | true |

表1光子强度、由其构造的分支、纯 K 假设下的 δ 和图14的 B(M1)/B(E2) 共享输入。CSM 对齐解释还依赖 Harris 参照、形变、配对、阻塞及 TRS 系统学。卷末引文仅查到其在文内的用途。

- 保留物理第1页反应摘要框的 82 MeV 异文，实验条件采用第2–3页§2–3与第5页表1表头共同支持的 86 MeV。第3页 Sn 质量数和第4页图1内反应标签有 OCR 异常，按各自原页确认后转录。
- 物理第15页图7图注写 473 keV，物理第16页正文却指图7为 126 keV 衰变曲线。图7所示线身份保留待审。第13页负宇称段落的图号也待核，第14页图6的可辨图注明确指向 h₁₁/₂ 序列。
- 物理第24页式(2)–(4)提取严重破损。对照笔记记录式(3)可能缺少能量因子。若 λ 定义为未重标度的 ΔI=2 与 ΔI=1 光子强度比，则同页纯 K、等四极矩前提下，1/λ 乘 Clebsch–Gordan 系数平方比的项应再乘 (Eγ,ΔI=2/Eγ,ΔI=1)^5，末尾再减 1。保留为定义与印刷式的相容性疑点，图14实际算法待证。
- 补记提取缺口。物理第9页图2无可读图注，物理第20页图12和表2的图注、行列及相邻正文错序。物理第5–8页表1的自旋、误差和门脚注有缺损，第18页 CSM 参数的希腊字母、数值与单位也待核原页。
