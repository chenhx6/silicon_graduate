---
type: source
title: "Dynamical Control of Nuclear Isomer Depletion via Electron Vortex Beams"
aliases: [Wu 2022 vortex electron NEEC, Wu 2022 OAM electron isomer depletion]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: deep-read
title_original: "Dynamical Control of Nuclear Isomer Depletion via Electron Vortex Beams"
authors: [Yuanbin Wu, Simone Gargiulo, Fabrizio Carbone, Christoph H. Keitel, Adriana Pálffy]
journal: Physical Review Letters
year: 2022
volume: 128
pages: 162501
doi: 10.1103/PhysRevLett.128.162501
language: en
canonical_source: doi:10.1103/PhysRevLett.128.162501
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2022_Wu et al_Dynamical Control of Nuclear Isomer Depletion via Electron Vortex Beams.pdf"
raw_sha256: 47ff862a3b55c3a0674c076d917e3b2ea8b16f209f375962ed71bd665a24e3f8
archive_required: true
nuclei: [93mo]
reactions: []
observables: [neec-cross-section-enhancement, orbital-angular-momentum-matching, subshell-selective-recombination]
methods: [bessel-beam-electron-wavefunctions, dirac-equation-with-oam, multipole-expansion-matching]
tags: [electron-vortex-beam, orbital-angular-momentum, neec, mo93m, isomer-depletion, quantum-wavefunction-control]
---

# Wu et al. (2022): Dynamical Control of Nuclear Isomer Depletion via Electron Vortex Beams

## Bibliographic Record

Yuanbin Wu, Simone Gargiulo, Fabrizio Carbone, Christoph H. Keitel, and Adriana Pálffy, "Dynamical Control of Nuclear Isomer Depletion via Electron Vortex Beams," *Physical Review Letters* **128**, 162501 (2022), DOI: `10.1103/PhysRevLett.128.162501`. Primary PDF is 6 pages, SHA-256: `47ff862a3b55c3a0674c076d917e3b2ea8b16f209f375962ed71bd665a24e3f8`.

## Scope and Reading Depth

The 6-page Letter was read completely. Reading covers relativistic Dirac-Bessel electron vortex states with orbital angular momentum (OAM \(m_l\hbar\)) (PDF p. 1--2 / printed p. 162501-1--2, Fig. 1), multipole expansion of the interaction Hamiltonian (PDF p. 2--3 / printed p. 162501-2--3, Eqs. 1--4), subshell-specific cross-section enhancement ratios (PDF p. 3 / printed p. 162501-3, Fig. 2), and macroscopic depletion rates vs spontaneous decay (PDF p. 4 / printed p. 162501-4, Fig. 3).

## Summary

The authors propose using relativistic electron vortex beams with non-zero orbital angular momentum to drive NEEC. Matching the electron beam OAM to the nuclear transition multipolarity (\(E2\) for \(^{93\text{m}}\)Mo) enhances spatial overlap with high-angular-momentum bound orbitals, yielding calculated cross-section enhancements of up to \(10^6\) into specific tailored subshells (\(3d_{5/2}, 4d_{5/2}\)) and depletion rates exceeding spontaneous decay by 4 orders of magnitude at \(10^5\text{ A/cm}^2\).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| W22-1 | Proposes orbital angular momentum matching (m_l*hbar) in electron vortex beams to overcome centrifugal suppression for high-multipolarity nuclear transitions. | theoretical-proposal | theoretical derivation | printed p.162501-1--2, Fig. 1 | true |
| W22-2 | Calculates partial cross-section enhancements up to 10^6 for 93mMo E2 transition into specific high-j subshells (3d_5/2, 4d_5/2). | model-calculation | derived value | printed p.162501-3, Fig. 2 | true |
| W22-3 | Predicts macroscopic depletion rates exceeding spontaneous isomer decay by 4 orders of magnitude at current density 10^5 A/cm2. | model-prediction | theoretical prediction | printed p.162501-4, Fig. 3 | true |
| W22-4 | Connects attosecond electron beam shaping (Vanacore 2018) with quantum control of nuclear decay degrees of freedom. | methodology-context | conceptual linkage | printed p.162501-1--2 | true |

## Competing Interpretations and Limitations

This is a theoretical proposal. Practical realization requires experimental development of high-flux, low-energy electron vortex sources overlapped with trapped isomer ions.

## Extracted Pages

- electron-vortex-beams
- mo93m
- neec

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–2页，NEEC 背景、涡旋束方案、图1(a)–(c)及两种核跃迁算例的设定。
- 物理第3–4页，涡旋波函数、截面和速率的式(1)–(4)、93mMo 的图2(a)–(b)及 152mEu 的表I。
- 物理第5–6页，Eu 算例结论、Mo 单离子速率估计、实现条件、致谢及参考文献[1]–[64]。
- 本次获取的具体覆盖：逐页审读物理第1–6页的抽取文字，覆盖理论方案、Mo 和 Eu 两个算例、单离子速率外推、图1–2的图注、表I的抽取表项及参考文献表。图面及公式排版待复核。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | 模型以平面波电子双旋量的相干叠加描述带拓扑荷 m 的涡旋束。较大的增强依赖于限制碰撞参数的平均范围，若将范围扩展至无穷，文中给出的速率增强仅为 p/p_z。 | 理论构造及适用条件 | source-reported | 物理第2页图1(a)–(b)图注，物理第3页式(1)–(4)及碰撞参数段。图1几何标记待查第2页，碰撞参数符号待查第3页。 | true |
| A20-2 | 对初始为电子基态的 Mo³⁶⁺，以同一俘获轨道的平面波共振强度为分母，涡旋束在 p 轨道给出约两个数量级的增强，在部分 f 轨道达到约六个数量级。以平面波最强的 2p₃/₂ 通道为统一分母时，涡旋 3d₅/₂ 通道约为其 12.96 倍。 | 模型计算 | source-reported | 物理第3页末段至第4页图2(a)–(b)及其讨论。两种分母、轨道与曲线对应须核对物理第4页图2。 | true |
| A20-3 | 在裸 152mEu 离子的 19.70 keV M1 算例中，平面波下最强的所列通道为 2s₁/₂，涡旋拓扑荷 m=3 与 m=5 时分别转为 2p₁/₂ 和 2p₃/₂。 | 模型计算 | source-reported | 物理第2页跃迁设定、物理第4页表I及物理第5页开头。m=3、5 的列与绝对共振强度须核对物理第4页表I。 | true |
| A20-4 | 对 93mMo 的 2p₃/₂ 通道取 m=5，作者以约 1 barn·eV 的共振强度乘以假设的谱通量 10²⁴ cm⁻² s⁻¹ eV⁻¹，估得约 1 s⁻¹ 每离子。相对于 6.8 h 半衰期对应的自然衰变率，作者概括为约四个数量级的提升。 | 条件性速率外推 | source-reported | 物理第5页左栏速率估计正文，物理第4页图2(b)为共振强度的相关定位。 | true |

能级取自文献[3]，轨道结合能用 GRASP92 计算。正文式(3)–(4)所依赖的详细速率表达式另见补充材料[45]，径向积分也指向文献[12、47]。现有笔记可确认同版，先替换核心数值归属和定位，再接受其整篇文本覆盖。

- 图1在物理第2页，式(1)–(4)全在第3页，图2与 152mEu 表I在第4页。旧稿所引第4页图3在本版抽取中无对应图号或图注，速率结果应定位至第5页正文。
- 将 W22-2 的六数量级结果改为图2(a)中部分 f 轨道相对各自平面波通道的共振强度比。涉及 3d₅/₂ 等轨道相对最强平面波通道的结论时，注明图2(b)另用平面波 2p₃/₂ 作为统一基准。
- 用物理第5页给出的谱通量 10²⁴ cm⁻² s⁻¹ eV⁻¹ 替换旧稿的 10⁵ A/cm²，并明确约 1 s⁻¹ 是每离子的理论反应率。
- 将‘OAM 与 E2 直接匹配’改写为核跃迁和俘获轨道共同限定参与的部分波，可在受限碰撞参数范围内调节 m 以改变俘获强度。W22-4 可据第5页写为作者讨论超快调控的设想，Vanacore 等对应文献[29]在第6页列为 2019 年。
