---
type: source
title: "Macklin 1979 - Resonance capture with a total-energy detector"
title_original: "Resonance Capture Reactions with a Total Energy Detector"
aliases: ["Macklin total-energy capture detector and pulse-height weighting"]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: conference-proceedings-chapter
reading_depth: read
authors: ["R. L. Macklin"]
year: 1979
canonical_source: "Neutron Capture Gamma-Ray Spectroscopy, invited paper, printed pp. 475–484"
raw_file: "raw/books/gpt/query/20261119-polarization-delta-collection/RobotNetdisk_2026-11-19_4bdbafaa8be4df9822774187f5bd5a00.pdf"
raw_sha256: "cc722604aa94e765559497ee21022550e035d2ce9407448b0ae81d27dd561005"
raw_pdf_pages: "476-485"
archive_required: true
tags: ["neutron-capture", "total-energy-detector", "pulse-height-weighting", "resonance-yield"]
---

# Macklin 1979：总能计数法的俘获产额与参数约束

## Bibliographic Record

R. L. Macklin，*Neutron Capture Gamma-Ray Spectroscopy*（1979），
印刷页 475–484。该章 PDF 页比印刷页大 1。

## Scope and Reading Depth

Gemini 一单元覆盖 PDF 476–485。Codex 核查源响应方程、加权计数
到产额的步骤及平均截面拟合中的相关性，未重算作者的截面或拟合。

## Summary

脉冲幅度加权按探测器响应矩阵构造对光子能量成比例的平均响应。
将级联的加权总能估计除以级联激发能，再用中子注量和样品量归一，
才可推断俘获产额。加权方法仍依赖响应和实验修正。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- |
| MA-1 | \(\sum_i G(i)P(i,E_\gamma)=E_\gamma\) 是理想线性能量响应条件。\(P(i,E_\gamma)\) 是由给定真实光子能产生第 \(i\) 道脉冲的概率。单个脉冲可只沉积部分入射能量。 | response-definition | direct-original-pages | PDF 477 |
| MA-2 | 从加权总能推算俘获时，文中另考虑死时间、本底、样品内散射和共振自屏蔽等。不能把响应线性当成这些效应已校正。 | experimental-method | direct-original-pages | PDF 478 |
| MA-3 | 文中约 120 keV 以下的若干平均产额拟合只用四个参数，仍可有绝对值达 0.99 的参数相关系数。透射数据可提供额外约束。 | fit-identifiability-boundary | direct-original-pages | PDF 479 |

## Competing Interpretations and Limitations

响应矩阵与权重应匹配同一探测器和门。加权后误差与未加权计数不同；
章中 1.2 和 1.6 倍统计比较随探测器和级联条件而变。原文没有在此
区分统计描述的方差与标准差口径，本页不将其作为通用方差因子。
平均产额拟合相符也不能保证分离价俘获、门态和未分辨共振贡献。

## Extracted Pages

- PDF 476–478：题页、总能测量、响应矩阵和产额修正。
- PDF 479–485：拟合相关性、强度和宽度讨论、文献。
