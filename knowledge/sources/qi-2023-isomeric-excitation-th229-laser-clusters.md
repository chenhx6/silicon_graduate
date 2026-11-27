---
type: source
title: "Isomeric Excitation of 229Th in Laser-Heated Clusters"
aliases: ["qi-2023-isomeric-excitation-th229-laser-clusters", "Jintao Qi 2023"]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: read
title_original: "Isomeric Excitation of 229Th in Laser-Heated Clusters"
authors: ["Jintao Qi", "Hanxu Zhang", "Xu Wang"]
journal: "Physical Review Letters"
year: 2023
volume: "130"
pages: "112501"
doi: "10.1103/PhysRevLett.130.112501"
canonical_source: "doi:10.1103/PhysRevLett.130.112501"
raw_file: "raw/papers/isomer/isomer_application/nuclear_clock/2023_Qi et al_Isomeric Excitation of Th 229 in Laser-Heated Clusters.pdf"
raw_sha256: "3d133e8d1139255b43f9742a1fe6d7ffddb195eb9b91a5bca38fc7167f33fba6"
archive_required: true
nuclei: ["229th"]
observables: []
methods: []
tags: ["229th", "isomer", "nuclear-clock", "vuv-spectroscopy"]
---

# Isomeric Excitation of 229Th in Laser-Heated Clusters

## Bibliographic Record

- **Citation**: Jintao Qi, Hanxu Zhang, Xu Wang, *Physical Review Letters* **130**, 112501 (2023). DOI: `10.1103/PhysRevLett.130.112501`.
- **Local Raw File**: `raw/papers/isomer/isomer_application/nuclear_clock/2023_Qi et al_Isomeric Excitation of Th 229 in Laser-Heated Clusters.pdf`
- **File SHA-256**: `3d133e8d1139255b43f9742a1fe6d7ffddb195eb9b91a5bca38fc7167f33fba6`
- **Physical Page Count**: 6 pages.

## Scope and Reading Depth

The local primary PDF was examined under reading depth `read`. Main text, figures, tables, and discussions were inspected. Supplementary information was not bundled in this primary PDF file and is not included in this audit.

## Summary

Qi, Zhang, and Wang theoretically investigated isomeric excitation of 229Th in laser-heated nanoclusters. They demonstrated that tuning laser intensity between 10^15 and 10^17 W/cm^2 shifts the dominant mechanism continuously between nuclear excitation by electron capture (NEEC) and inelastic electron scattering (NEIES).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| Q23-1 | Modeled isomeric excitation in nanoclusters with continuous tuning between NEEC and NEIES via laser intensity. | theory-deduction | theoretical model | p. 112501-1, Abstract, Fig. 1 | true |
| Q23-2 | Repeated electron-ion collisions in picosecond nanoplasma enhance excitation yield relative to planar targets. | theory-deduction | model calculation | pp. 112501-3 to 112501-4, Fig. 3 | true |

## Competing Interpretations and Limitations

Theoretical cluster-plasma simulation; experimental verification of NEEC remains an open challenge.

## Extracted Pages

- [[qi-2023-isomeric-excitation-th229-laser-clusters]]
- [[nuclear-clock-isomer-learning-and-transfer-20261107]]

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–2页，引言、激光–团簇相互作用和团簇膨胀起始段。第1页图1，第2页图2。
- 物理第3–4页，团簇膨胀续段、核激发截面、速率与产额计算、讨论及结论开头。第3页图3和式(1)–(2)，第4页图4。
- 物理第5–6页，结论末段、致谢、作者脚注及编号[1]–[84]的书目，第5页[36]指向外置补充材料。
- 本次获取的具体覆盖：顺读物理第1–6页的正文、讨论、结论、图1–4图注、式(1)–(2)提取文本及书目。接受旧条目的同版主文文本覆盖。强度范围、证据定位及固体靶比较须按下列内容修订，图像仍待目检。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A18-1 | 在约10⁶个原子的团簇模拟中，受限电子在皮秒尺度反复碰撞，高密度核心贡献了大部分计算核激发。产额由局部速率对体积和时间积分得到。 | model-result | source-reported | 物理第2–3页，团簇膨胀段、物理第2页图2及第3页式(1)–(2)。密度剖面和时间演化须目检第2页图2。 | true |
| A18-2 | 对文中计算的 ²²⁹Th⁺，电子能量低于8.28 eV时出现离散 NEEC 共振，高于8.28 eV时为连续的 NEIES 截面。 | model-result | source-reported | 物理第3页，核异能态激发段和图3。共振、连续谱、能阈及插图须目检第3页。 | true |
| A18-3 | 按5 ps计算，约10¹⁴ W/cm²时 NEEC 占优，约10¹⁶ W/cm²时 NEIES 占优，两者在约10¹⁵ W/cm²接近。总产额在约2×10¹⁴ W/cm²达到每团簇略高于0.4个异能核。 | model-result | source-reported | 物理第4页，图4(a)–(d)及邻段。交叉和总产额峰值须目检第4页图4(d)。 | true |
| A18-4 | 文章转述两项 ⁹³ᵐMo 束流实验。Chiara 等报告异能态耗尽，Guo 等在类似实验中未见耗尽信号。 | reported-observation | source-reported | 物理第2页及物理第6页书目[64]–[68]。 | true |

团簇动力学使用 EPOCH 二维三速度分量 PIC 模拟，并与三维膨胀模型比较。截面使用 Dirac 畸变波 Born 近似、RADIAL 电子波函数及引文[74]的核跃迁强度。NEEC 截面计算假定初始离子处于基态，产额还依赖随激光强度变化的电荷态权重。

- Q23-1 将机制切换的强度范围改为约10¹⁴至10¹⁶ W/cm²，并以物理第4页图4(d)为主证据。第1页图1是方案示意。
- Q23-2 将高密度核心、重复碰撞及产额分别定位至物理第2页图2、第3页式(1)–(2)及第4页图4。物理第3页图3给出截面。与固体靶激光烧蚀羽流的比较见物理第4页讨论(c)，限于结构、动力学与密度的定性比较，删去定量产额优势的表述。
- 将旧稿的图表已检查改成图1–4图注与主文已读。VUV 光谱若保留为标签，应标为引言中的研究背景。
