---
type: source
aliases: ["G D Jones 2021 three polarization planes"]
tags: [gamma-ray-polarization, compton-polarimetry, clover]
title: "Reaction planes, polarization planes and scattering planes in γ-ray linear polarization events"
title_original: "Reaction planes, polarization planes and scattering planes in γ-ray linear polarization events"
created: "2026-11-27"
updated: "2026-11-27"
status: "ai-draft"
review_status: "unreviewed"
source_type: "journal-article-method"
reading_depth: "read"
year: 2021
journal: "Nuclear Instruments and Methods in Physics Research A"
volume: "987"
pages: "164869"
doi: "10.1016/j.nima.2020.164869"
canonical_source: "https://doi.org/10.1016/j.nima.2020.164869"
raw_file: "raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_j.nima.2020.164869.pdf"
raw_sha256: "0eaf47648b1cd7eaff64f96bf30a204c0c1658f715a6247140fef06ee9c019fe"
archive_required: true
---

# Reaction planes, polarization planes and scattering planes in γ-ray linear polarization events

## Bibliographic Record

G. D. Jones. Nuclear Instruments and Methods in Physics Research A 987 (2021), 164869. DOI 10.1016/j.nima.2020.164869.

## Summary

本文建立反应平面、偏振平面和散射平面的几何关系，再以按事件加权的康普顿截面计算探测器不对称度与灵敏度。

## Extracted Pages

Elsevier 刊版，PDF 1–9（含参考文献），§§1–8、Figs. 1–5、Tables 1–3、Eqs. (1)–(30)。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| JONES2021-1 | 仪器模型以四块 40×40×70 mm³ 长方体 Ge 构成基准 clover，将事件筛选和有限立体角平均用于 Q=A/P。 | model-method | direct-original | PDF 2–5, Eqs. (7)–(24), Figs. 1–4, §6 | true |
| JONES2021-2 | 197 keV、∣P∣=1 的两种模拟方向在阈值 60 keV 时给 A=+0.216、−0.218，在 35 keV 时给 +0.288、−0.289。 | model-result | direct-original | PDF 7, Tables 2–3 | true |
| JONES2021-3 | 旧校准样本对 Q/Q_P 的线性斜率拟合为 0.027±0.026 MeV⁻¹。 | derived-observable | direct-original | PDF 8, Fig. 5 and adjoining text | true |

## Scope and Reading Depth

Elsevier 刊版，PDF 1–9（含参考文献），§§1–8、Figs. 1–5、Tables 1–3、Eqs. (1)–(30)。 本轮回查决定性原页，未重算。

## Competing Interpretations and Limitations

阈值收益随能量、路径筛选和晶体几何变化。模型使用直角晶体和主要相互作用，不能直接移用为其它阵列的偏振校准。Table 1 重用 [[jones-1995-clover-compton-calibration]] 的 EUROGAM 校准，属于同一实验输入。

## Agent Self-Audit Triage

- P1：转用原测量或模拟值时保留版本、取向、几何、支路和实验依赖等适用条件。
