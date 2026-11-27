---
type: source
title: "Exciting the Isomeric 229Th Nuclear State via Laser-Driven Electron Recollision"
aliases: ["wang-2021-exciting-229th-electron-recollision", "Wu Wang 2021"]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: read
title_original: "Exciting the Isomeric 229Th Nuclear State via Laser-Driven Electron Recollision"
authors: ["Wu Wang", "Jie Zhou", "Boqun Liu", "Xu Wang"]
journal: "Physical Review Letters"
year: 2021
volume: "127"
pages: "052501"
doi: "10.1103/PhysRevLett.127.052501"
canonical_source: "doi:10.1103/PhysRevLett.127.052501"
raw_file: "raw/papers/isomer/isomer_application/nuclear_clock/2021_Wang et al_Exciting the Isomeric Th 229 Nuclear State via Laser-Driven Electron Recollision.pdf"
raw_sha256: "fc0c16a4c73e6dfd0d89554a376ad8e3e3c8326f856d969a4ed141b5194af672"
archive_required: true
nuclei: ["229th"]
observables: []
methods: []
tags: ["229th", "isomer", "nuclear-clock", "vuv-spectroscopy"]
---

# Exciting the Isomeric 229Th Nuclear State via Laser-Driven Electron Recollision

## Bibliographic Record

- **Citation**: Wu Wang, Jie Zhou, Boqun Liu, Xu Wang, *Physical Review Letters* **127**, 052501 (2021). DOI: `10.1103/PhysRevLett.127.052501`.
- **Local Raw File**: `raw/papers/isomer/isomer_application/nuclear_clock/2021_Wang et al_Exciting the Isomeric Th 229 Nuclear State via Laser-Driven Electron Recollision.pdf`
- **File SHA-256**: `fc0c16a4c73e6dfd0d89554a376ad8e3e3c8326f856d969a4ed141b5194af672`
- **Physical Page Count**: 6 pages.

## Scope and Reading Depth

The local primary PDF was examined under reading depth `read`. Main text, figures, tables, and discussions were inspected. Supplementary information was not bundled in this primary PDF file and is not included in this audit.

## Summary

Wang et al. proposed exciting 229mTh via laser-driven electron recollision in intense femtosecond laser fields. Semiclassical calculations indicate an excitation probability of 10^-9 to 10^-8 per pulse via inelastic electron scattering, which does not require prior resonance knowledge of the transition energy.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WA21-1 | Proposed laser-driven electron recollision scheme for non-resonant isomeric excitation of 229Th. | theory-deduction | theoretical model | p. 052501-1, Abstract, Fig. 1 | true |
| WA21-2 | Calculated excitation probability of 10^-9 to 10^-8 per nucleus per pulse using tabletop femtosecond laser systems. | theory-deduction | model calculation | pp. 052501-3 to 052501-4, Fig. 3 | true |

## Competing Interpretations and Limitations

Theoretical model calculation based on strong-field atomic physics approximations; lacks experimental validation in thorium.

## Extracted Pages

- [[wang-2021-exciting-229th-electron-recollision]]
- [[nuclear-clock-isomer-learning-and-transfer-20261107]]

## 2026-11-27 — 馆藏原件与覆盖核对

- PDF 第 1–2 页，问题背景、再碰撞方案、电子激发截面与轨迹模型输入，图 1、图 2、式（1）–（3）。
- PDF 第 3–4 页，轨迹传播、有效通量、激发概率、电子云吸收和产额估算，图 3–5、式（4）–（6）。
- PDF 第 5–6 页，光场优化展望、RINE–NEEC 循环设想、235U 延伸讨论、致谢、参考文献 [1]–[61] 和更正。
- 本次获取的具体覆盖：通读 PDF 第 1–6 页的抽取文本，覆盖正文、式（1）–（6）的可辨内容、图 1–5 的完整图注、参考文献和更正说明。图像与受损公式字形待查原页。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | 作者提出以强场电离释放外层电子，再由激光场驱动电子返回，通过非弹性散射激发 229Th 核。方案依赖返回电子达到激发阈值，作者认为其宽能谱降低了对异能态能量精确值的依赖。 | 理论方案 | source-reported | PDF 第 1 页正文、图 1 图注；第 4 页结论。 | true |
| A20-2 | 按文中采用的核跃迁强度，电子激发截面以 E2 贡献为主。轨迹计算用 8.3 eV 处的势傅里叶分量判断有效作用范围，并以返回半径小于 1 a.u. 的轨迹估算有效通量。 | 模型计算 | source-reported | PDF 第 2 页图 2(a) 及相邻正文；第 3 页图 3、式（5）前后正文。图 3 曲线待核第 3 页。 | true |
| A20-3 | 30 fs 高斯脉冲的计算中，10¹⁴ W/cm² 时总激发概率约为 10⁻¹⁸ 至 10⁻¹⁷，10¹⁵ W/cm² 时约为 10⁻¹⁷，约为前者的六倍。两种强度下首个逸出电子的返回能量均低于阈值。较高强度时，计算的激发概率约在 10 fs 内累积。 | 模型预测 | source-reported | PDF 第 3 页式（5）后正文；第 4 页图 4(a)–(d) 及图注。各电子分量与读数待核第 4 页。 | true |
| A20-4 | ELSEPA 给出的轴向电子云通量损失估计随入射能量变化，正文按 20、50、100 eV 分别给出约 19%、16%、14%。 | 模型估算 | source-reported | PDF 第 4 页图 5、式（6）及相邻正文。曲线标识和公式排版待核第 4 页。 | true |

半经典结果采用 ADK 隧穿率、GSZ 离子芯势、经典轨迹和首次再碰撞近似，钍的 ADK 系数取 Cₗ=1。式（5）以截面乘有效返回通量，截面采用文献 [37] 的 B(E2)=27 W.u. 和 B(M1)=0.0076 W.u.。截面的完整表达式由正文指向文献 [36]。

- 将摘要及 WA21-2 的 10⁻⁹ 至 10⁻⁸ 改为按两种强度分别报告的正文数值，并将概率图定位改为 PDF 第 4 页图 4(b)、(d)。图 3 位于第 3 页，展示有效半径的傅里叶分量。
- 将 WA21-1 的依据补到 PDF 第 1 页正文及图 1，并以第 4 页结论说明宽能谱与能量精度的关系。以正文列出的阈值条件限定方案表述。
- 在版次记录加入第 6 页更正。第 3 页抽取文本同时给出 0.044 a.u. 和 1.09 eV，换算配对应回看第 3 页及第 6 页更正说明。此前可保留首个电子低于阈值的定性结论。
