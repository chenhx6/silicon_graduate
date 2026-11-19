---
type: source
title: "Schreckenbach 1979 - High precision conversion-electron spectroscopy"
title_original: "High Precision (n,e-) Spectroscopy"
aliases: ["Schreckenbach BILL conversion-electron spectroscopy"]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: conference-proceedings-chapter
reading_depth: read
authors: ["K. Schreckenbach"]
year: 1979
canonical_source: "Neutron Capture Gamma-Ray Spectroscopy, invited paper, printed pp. 125–143"
raw_file: "raw/books/gpt/query/20261119-polarization-delta-collection/RobotNetdisk_2026-11-19_4bdbafaa8be4df9822774187f5bd5a00.pdf"
raw_sha256: "cc722604aa94e765559497ee21022550e035d2ce9407448b0ae81d27dd561005"
raw_pdf_pages: "137-155"
archive_required: true
tags: ["conversion-electrons", "multipole-mixing", "neutron-capture"]
---

# Schreckenbach 1979：内转换电子谱与混合分量

## Bibliographic Record

K. Schreckenbach，*Neutron Capture Gamma-Ray Spectroscopy*
（1979），印刷页 125–143。该章 PDF 页比印刷页大 12。

## Scope and Reading Depth

Gemini 两单元各覆盖 PDF 137–146 和 147–155。前者在未读数组
列出了任务未要求的后半章，原收据的格式拒绝仍保留，实际输入的
10 页均有已处理记录。Codex 核查原式、分辨率条件和表例。

## Summary

BILL 用分壳转换电子强度补充 γ 谱。测量绝对 \(\alpha_K\) 需要
电子/γ 相对响应刻度。测量 \(L_1/L_3\) 强度比需要两条电子峰可分辨，
以及可用于该核素和能量的理论壳层转换系数。对于 M1/E2 两分量、
相同强度约定及已校正的壳层系数，令 \(r=\delta^2\)，则
\[
\alpha_{K,\mathrm{mix}} =
\frac{\alpha_K(\mathrm{M1})+r\alpha_K(\mathrm{E2})}{1+r},\qquad
R_{13} =
\frac{\alpha_{L_1}(\mathrm{M1})+r\alpha_{L_1}(\mathrm{E2})}
{\alpha_{L_3}(\mathrm{M1})+r\alpha_{L_3}(\mathrm{E2})}.
\]
这些观测约束 \(r\) 或 \(r/(1+r)\)，保留 \(\delta\) 的符号歧义。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| SE-1 | 文中给 \(Z=50\)、约 400 keV 处两种 \(\alpha_K\) 相等的例子。此处用绝对 K 壳层系数无法分辨两分量。 | identifiability-boundary | direct-original-pages | PDF 141–143, Fig. 2 |
| SE-2 | \(L_1/L_3\) 可提供另一约束。文中约 5% 的精度假设以壳层峰可分辨为条件。理论系数比接近时，该比值也失去区分力。 | method-and-boundary | direct-original-pages and algebra | PDF 143–144, Fig. 3 |
| SE-3 | 168Er 79.804 keV 的 \(L_1/L_3\) 原表为 0.0859(6)，理论列 0.0812，作者列差异 \(+5.8\pm0.7\%\)。这是该跃迁及所比系数的偏离例。 | measurement-and-theory | direct-original-pages | PDF 145, Table 1 |

## Competing Interpretations and Limitations

峰重叠、电子拖尾、壳层理论系数和额外多极成分都可改变推断。小差异
不能自动分给 M1 或 E2。仅比较两分量的电子强度比也无法确定相位。
本章用途是内转换与多极性分析，原件没有在本轮被用于 PDM 拟合。

## Extracted Pages

- PDF 137–140：题页、BILL 测量及性能。
- PDF 141–145：绝对及相对壳层方法，Figs. 2–3 与 Table 1。
- PDF 146–155：转换异常、误差与实验例证。
