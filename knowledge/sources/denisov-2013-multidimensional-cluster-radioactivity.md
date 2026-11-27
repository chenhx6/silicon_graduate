---
type: source
title: "Denisov 2013：多维团簇放射性模型、动态形变与惯性边界"
aliases: [Denisov 2013 multidimensional cluster radioactivity]
created: 2026-10-29
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory
reading_depth: read
canonical_source: "Phys. Rev. C 88, 044608 (2013); arXiv:1311.3810v1"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/denisov-2013-multidimensional-cluster-arxiv1311.3810v1.pdf"
raw_sha256: "cf00e8012f9100edb443571cbd77c1af14b251dc6a78bb81f1c1e02ef6f181be"
title_original: "Multidimensional model of cluster radioactivity"
authors: [V. Yu. Denisov]
year: 2013
journal: Physical Review C
volume: "88"
pages: "044608"
doi: "10.1103/PhysRevC.88.044608"
citation_key: "denisov_2013_228th-multidimensional-cluster"
source_url: "https://arxiv.org/abs/1311.3810v1"
raw_storage_status: "raw-pdf-archived-new-original"
staging_file: "tmp/day26-cluster/1311.3810.pdf"
staging_sha256: "cf00e8012f9100edb443571cbd77c1af14b251dc6a78bb81f1c1e02ef6f181be"
nuclei: [228Th, 208Pb, 20O, 232U, 236Pu, 242Cm]
observables: [cluster-half-life, action-integral, barrier-height]
methods: [extended-Thomas-Fermi, Skyrme-SkM-star, shell-correction, multidimensional-WKB]
tags: [cluster-radioactivity, dynamical-deformation, preformation, collective-inertia]
---

# 多维团簇放射性模型

## Bibliographic Record

Crossref题名、作者和 DOI 与 arXiv:1311.3810v1 首页相符。实际读取12页、1068033 bytes的预印本；PDF签名和 SHA-256 已核验，已逐文件核验后以新增原件归档至frontmatter所列raw路径，没有覆盖既有文件。

## Scope and Reading Depth

定向阅读PDF1–2、5–10：密度参数化、势能/壳修正、Eqs21–31、惯性和最小作用量路线、228Th比较及局限。没有复算ETF能量、动态轨迹或参数标定。

## Summary

多维动态片段形变与壳修正可改变团簇通道作用量；作者设形成因子S=1，因此半衰期符合不构成独立P0测定。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DE13-1 | 以团簇与子核的距离和动态表面形变为多维坐标，用ETF/Skyrme+壳修正求势能并最小化WKB作用量；动态形变可降低球形片段路径的势垒，但结果同时依赖惯性。 | model-method | direct-original-preprint | PDF1–2, PDF5–8, Eqs16–31 | true |
| DE13-2 | Eq21写T=ln2/[nu S T(Q)]，但作者在实际密度ansatz中设预形成因子S=1；这不是测得所有核中P0=1。 | model-assumption | direct-original-preprint | PDF5–6, Eqs21–24 | true |
| DE13-3 | 惯性使用水动力学值再乘增强因子，部分因子受片段E2数据约束；惯性改变可显著改变作用量及半衰期。 | model-input-and-limit | direct-original-preprint | PDF6–9, Eqs25–31 | true |
| DE13-4 | 228Th→208Pb+20O的计算半衰期约5.0×10^20 s，与本文引用的实验(5.29±1.01)×10^20 s相近；不是新的独立实验。 | model-comparison | direct-original-preprint | PDF9 | true |

## Competing Interpretations and Limitations

该模型把团簇预先包含于密度参数化，设S=1并在路径/惯性中承载内部重排代价。它与采用P0≪1的势垒模型可以描述同一衰变率；P0的分解依赖模型定义。动态表面形变不能被自动等同为某一固定beta3、beta5或beta7；本文不提供单独逐阶的beta5/beta7实验增强倍数。

## Knowledge Impact and Learning Decision

支持形变改变势垒与作用量的机制；限制“成功拟合半衰期就测得P0”及“动态形变必等同于基态八极形变”的解释。综合见 [[octupole-cluster-radioactivity-preformation-boundary]]。

## Extracted Pages

- [[octupole-cluster-radioactivity-preformation-boundary]]

## Review Status

Codex source self-audit，保留needs_review。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"start_page": 1, "end_page": 4, "sections": "首页、§I 引言、§II.A–C 宏观势、能量密度泛函及弛豫密度参数化。"}
- {"start_page": 5, "end_page": 6, "sections": "§II.D–E 壳修正、半衰期、WKB 作用量及惯性，随后进入 §III。"}
- {"start_page": 7, "end_page": 9, "sections": "§III 四个衰变通道的势面、轨迹、半衰期和惯性敏感性。图 1–2 在第 7 页，表 I 与图 3 在第 8 页，图 4 在第 9 页。"}
- {"start_page": 10, "end_page": 12, "sections": "§III 总结、§IV 结论、致谢及参考文献 [1]–[102]。"}
- 本次获取的具体覆盖：逐页审核物理第 1–12 页的抽取文本，覆盖 §I–IV、式 (1)–(32)、图 1–4 图注、表 I、致谢及参考文献 [1]–[102]。建议接受既有笔记明列的第 1–2、5–10 页同版定向文本覆盖，并按本回执补录第 3–4、11–12 页。图表结论待目检，ETF 势能、最小作用量路径与半衰期未复算。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A21-1 | 模型以片段距离 R 和两个轴对称椭球形变 ξ₁、ξ₂ 为集体坐标，用含 Skyrme、库仑项的非局域 ETF 构造宏观势，再加入含配对贡献的壳修正。作者在三次多项式路径族内最小化 WKB 作用量，并依据预含团簇的密度设定取 S=1。 | 模型方法与假定 | source-reported | 物理第 2–5 页式 (1)–(20)，第 5–6 页式 (21)–(25) 及 S 的说明，第 8 页式 (32)。 | true |
| A21-2 | 对 ²⁴²Cm → ²⁰⁸Pb + ³⁴Si，在同一组增强因子 (k₀,k₁,k₂)=(3.35,6.07,14.01) 下，作者给出的双片段动态形变路径半衰期为 1.4×10²³ s，球形路径为 2.2×10²⁶ s。正文另给出全取 kᵢ=1 的球形路径对照，加入壳修正后由 8.3×10¹⁵ s 增至 2.5×10²⁴ s。 | 作者报告的模型计算 | source-reported | 物理第 8 页表 I、图 3 及同页壳修正对照段。表列和轨迹图例待第 8 页目检。 | true |
| A21-3 | 作者引述的实验半衰期为 ²²⁸Th 通道 (5.29±1.01)×10²⁰ s、²⁴²Cm 通道 1.4（+0.5/−0.3）×10²³ s、²³²U 通道 (2.4±0.2)×10²⁰ s、²³⁶Pu 通道 3.3（+0.7/−1.2）×10²¹ s。 | 本文转引的实验观测 | source-reported | 物理第 8–9 页 §III，实验来源分别为 [16]、[20]、[13]、[17]。第 8 页 ²⁴²Cm 的不对称误差上下标待核。 | true |
| A21-4 | 作者用 ²⁴²Cm 通道固定唯一拟合参数 k₀，并将该值用于其余通道。模型给出 ²²⁸Th 通道 5.0×10²⁰ s，与所引实验值接近。²³²U 和 ²³⁶Pu 通道的计算值分别为 5.8×10¹⁹ s 和 1.0×10²¹ s，约为各自实验中心值的四分之一和三分之一。 | 标定与模型对照 | source-reported | 物理第 8 页表 I 及相邻正文，第 9 页 §III 数值比较，第 10 页 §IV 标定说明。 | true |

惯性以无旋流体质量参数为基准，k₁、k₂ 用外部四极激发能与 B(E2) 数据 [98] 约束，k₀ 是接触点内的经验增强参数，见物理第 6 页式 (26)–(31)。ETF、壳修正及基态形变输入分别见 [78]、[79]、[83]。参考文献 [1]–[102] 仅审核本预印本的书目和引用关系。

- 对照笔记的 title_original 若用于所归档的预印本，应补上首页题名开头的 The。期刊书目保留 Phys. Rev. C 88, 044608 (2013)。
- DE13-1 的密度与形状依据应补物理第 3–4 页式 (9)–(15)，路径参数化应补第 8 页式 (32)。nuclei 字段若列齐四个通道，应补 ²⁴Ne、²⁸Mg、³⁴Si。
- DE13-3 应明确 k₀=3.35 由 ²⁴²Cm 通道标定，k₁、k₂ 由外部 E2 数据约束。DE13-4 应补实验来源 [16]，并注明 ²²⁸Th 比较沿用该 k₀。总括四个通道时应注明 ²³²U、²³⁶Pu 的计算值偏低约 3–4 倍。
- ETF 阶数中的 ~2、~4 是抽取时失真的 ℏ 幂次，核对物理第 1–3、10 页后写作 ℏ²、ℏ⁴。需要逐式转录时，核对第 3 页式 (7) 的梯度项括号、第 4 页 ξ 与 β 比例式的根号，以及第 6 页式 (24)–(25)、(30)–(31) 的根号、张量下标和幂次。第 4 页式 (15) 应按质子数和中子数分别守恒转写。图 1–4 与表 I 的题注文本均有提供。
