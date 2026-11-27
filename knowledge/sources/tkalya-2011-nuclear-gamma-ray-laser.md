---
type: source
title: "Proposal for a Nuclear Gamma-Ray Laser of Optical Range"
aliases: ["tkalya-2011-nuclear-gamma-ray-laser", "E. V. Tkalya 2011"]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: read
title_original: "Proposal for a Nuclear Gamma-Ray Laser of Optical Range"
authors: ["E. V. Tkalya"]
journal: "Physical Review Letters"
year: 2011
volume: "106"
pages: "162501"
doi: "10.1103/PhysRevLett.106.162501"
canonical_source: "doi:10.1103/PhysRevLett.106.162501"
raw_file: "raw/papers/isomer/isomer_application/nuclear_clock/2011_Tkalya_Proposal for a Nuclear Gamma-Ray Laser of Optical Range.pdf"
raw_sha256: "f92d851c421b6543a6a0d8a9671244fc0f050660415a9cdfb20e23d490c25e0c"
archive_required: true
nuclei: ["229th"]
observables: []
methods: []
tags: ["229th", "isomer", "nuclear-clock", "vuv-spectroscopy"]
---

# Proposal for a Nuclear Gamma-Ray Laser of Optical Range

## Bibliographic Record

- **Citation**: E. V. Tkalya, *Physical Review Letters* **106**, 162501 (2011). DOI: `10.1103/PhysRevLett.106.162501`.
- **Local Raw File**: `raw/papers/isomer/isomer_application/nuclear_clock/2011_Tkalya_Proposal for a Nuclear Gamma-Ray Laser of Optical Range.pdf`
- **File SHA-256**: `f92d851c421b6543a6a0d8a9671244fc0f050660415a9cdfb20e23d490c25e0c`
- **Physical Page Count**: 4 pages.

## Scope and Reading Depth

The local primary PDF was examined under reading depth `read`. Main text, figures, tables, and discussions were inspected. Supplementary information was not bundled in this primary PDF file and is not included in this audit.

## Summary

Tkalya developed a theoretical model for stimulated gamma-ray emission of 229mTh embedded in host dielectric crystals (e.g. LiCaAlF6, CaF2). The proposal demonstrates that recoil-free emission (f_LM ≈ 1) allows optical-range nuclear gamma amplification when population inversion is established via crystal EFG splitting or magnetic fields.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TK11-1 | Theoretical proof that recoil-free fraction f_LM ≈ 1 for 7.6-8 eV nuclear transition in host crystal. | theory-deduction | theoretical model | p. 162501-2, Eq. (2) | true |
| TK11-2 | Population inversion established by combining selective optical pumping with crystal electric field gradient splitting. | theory-deduction | theoretical model | p. 162501-3, Fig. 1 | true |

## Competing Interpretations and Limitations

Theoretical feasibility model assuming idealized crystal defect densities and narrow linewidths. Does not establish experimental amplification or account for realistic color center absorption.

## Extracted Pages

- [[tkalya-2011-nuclear-gamma-ray-laser]]
- [[nuclear-clock-isomer-learning-and-transfer-20261107]]

## 2026-11-27 — 馆藏原件与覆盖核对

- {"pdf_pages": "1–2", "sections": "第1页题名、版本标记、宿主和增益模型式(1)。第2页泵浦速率式(2)、外磁场 Zeeman 方案与图1。"}
- {"pdf_pages": "3–4", "sections": "第3页无反冲估算及电四极分裂图2(a–b)。第4页续完长弛豫方案，讨论脉冲、金属覆层和泵浦条件，列参考文献[1]–[25]。"}
- 本次获取的具体覆盖：逐页审读 PDF 物理第1–4页的抽取文字，覆盖式(1)–(2)、三种反转方案、无反冲估算、弛豫与脉冲估计、致谢和参考文献。两幅图的题注均可辨认，箭头和能级版面待查。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | 按文中采用的 7.6±0.5 eV 跃迁能和增益模型，单靠共振真空紫外泵浦可以积累异能态，但稳态仍达不到式(1)的反转增益条件。 | 理论推导 | source-reported | PDF 第1页能量输入与式(1)，第2页式(2)及其稳态解。 | true |
| A20-2 | 作者估算 7.6 eV 光子的核反冲能约为 1.4×10⁻¹⁰ eV。低温下按 Debye–Waller 因子估计，无反冲分数近于 1。 | 条件性模型估计 | source-reported | PDF 第3页首栏无编号反冲能和 Debye–Waller 表达式，紧接图1跃迁讨论。 | true |
| A20-3 | 外磁场方案假定自旋晶格弛豫时间不超过异能态半衰期。在 100 T、0.01 K 的示例参数下，作者估计选定 Zeeman 跃迁的净增益系数约为 3 cm⁻¹。 | 条件性模型估计 | source-reported | PDF 第2页图1、布居与增益计算，回用第1页式(1)。红色跃迁与终态对应待核第2页。 | true |
| A20-4 | 电四极分裂方案按弛豫时间分两种情形。可及时重分布时，作者估计约 2 cm⁻¹ 的增益。弛豫远慢于异能态衰变时，先使基态子能级达到低温分布再泵浦，估计总体增益约 3 cm⁻¹。 | 条件性模型估计 | source-reported | PDF 第3页图2(a–b)和四极分裂段，第二种情形的增益值续在第4页首段。图2两分图的时间条件与跃迁标记待核第3页。 | true |

历史跃迁能取自[3]，LiCaAlF₆材料依据来自[4]的 ²³²Th 植入研究。辐射宽度由[14–17]的其他跃迁及 Alaga 规则推估，无反冲估算援引[19]。本次只核对预印本正文和所列书目。

- 把本地归档版本和定位统一改为 arXiv:1011.0858v3 的物理页。PRL 106, 162501 (2011) 及其 DOI 只保留为旧笔记提供的同作期刊版线索，待对照期刊原件。
- 将宿主实例收窄至 LiCaAlF₆，删除 CaF₂。将 TK11-1 的 7.6–8 eV 改为文中采用的历史输入 7.6±0.5 eV，并把定位改到 PDF 第3页首栏的无编号表达式。第2页式(2)描述泵浦速率。
- 将 TK11-2 的定位改为 PDF 第3页图2(a–b)及第4页首段，另以第2页图1记录磁场方案。按预泵浦、低温布居和弛豫假设表述有效反转，删除已建立反转的实验性措辞。
- PDF 第2页图1的磁量子数和布居应核图。第3页图2(a)题注的时间不等号抽取成点号，四极场梯度的符号及量级也应核原式。第4页脉冲重复频率的幂次、弛豫时间不等号和根号存在抽取歧义，精确转录前须查原页。
