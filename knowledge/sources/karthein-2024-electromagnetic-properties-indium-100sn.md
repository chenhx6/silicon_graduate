---
type: source
title: "Karthein 等 2024：铟同位素电磁性质与 100Sn 双幻数"
aliases: [Karthein 2024 100Sn, electromagnetic properties indium 100Sn]
created: 2026-09-12
updated: 2026-09-12
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Electromagnetic properties of indium isotopes illuminate the doubly magic character of 100Sn"
authors: [J. Karthein, C. M. Ricketts, R. F. Garcia Ruiz, CRIS Collaboration]
journal: Nature Physics
year: 2024
volume: 20
pages: 1719-1725
doi: 10.1038/s41567-024-02612-y
arxiv: 2310.15093
language: en
canonical_source: "https://doi.org/10.1038/s41567-024-02612-y"
zotero_item_key:
citation_key: Karthein_2024
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
zotero_uri:
library_file: "raw/papers/gpt/_incoming/20260912-100sn-refresh/100sn-indium-2024-arxiv.pdf"
raw_file: "raw/papers/gpt/_incoming/20260912-100sn-refresh/100sn-indium-2024-arxiv.pdf"
raw_sha256: "4a833c6fbf425ae2f6b190661103ea61335ec1547728788bc9f21f25bf40bd17"
nuclei: [100sn]
reactions: ["ISOLDE proton-induced production of 101-131In"]
experiments: []
models: [density-functional-theory, valence-space-in-medium-similarity-renormalization-group]
observables: [nuclear-quadrupole-moment, nuclear-magnetic-moment, nuclear-charge-radius, quadrupole-collectivity]
methods: [collinear-resonance-ionization-spectroscopy, laser-spectroscopy, hyperfine-spectroscopy]
tags: [a100, 100sn, indium-isotopes, doubly-magic, nuclear-collectivity, precision-laser-spectroscopy]
---

# Karthein 等（2024）：铟同位素电磁性质与 `100Sn` 双幻数

## Bibliographic Record

J. Karthein、C. M. Ricketts、R. F. Garcia Ruiz 等（CRIS Collaboration），*Electromagnetic properties of indium isotopes illuminate the doubly magic character of `100Sn`*，*Nature Physics* **20**, 1719–1725 (2024)，DOI `10.1038/s41567-024-02612-y`，arXiv `2310.15093`。Crossref、Nature 文章页和本地 arXiv PDF 的题名、作者首位、卷页与 DOI 相符；本地 PDF 为 26 页，SHA-256 为 `4a833c6fbf425ae2f6b190661103ea61335ec1547728788bc9f21f25bf40bd17`。

## Scope and Reading Depth

- `deep-read`：完整读取本地 PDF 的正文、Methods、Extended Data 说明、数据/代码可用性和参考文献主线。
- 视觉核对：PDF p.1 题名/摘要，pp.3–5 实验设计、集体性讨论、结论和数据可用性，p.6 Table 1；其余 Methods/Extended Data 以文本提取定位。
- 核心范围：`101–131In` 的 hyperfine/isotope-shift spectroscopy、`Q_s`、磁矩、电荷半径、`100Sn` 壳闭合解释、DFT/VS-IMSRG 比较和公开数据入口。
- 不覆盖：未对 596 MB/390 MB 原始压缩包做本地下载或逐文件复算；本论文也不直接测量 `100Sn` β 衰变、`100In` γ branching 或 `B(GT)`。
- 版本边界：本地文件是 arXiv 版本；Nature DOI 版本身份由 Crossref/Nature 元数据核对。论文正文的 Zenodo Ref.[99] DOI 与 publisher/Zenodo 当前结果图记录存在一处 metadata discrepancy，单独保留。

## Summary

论文用 ISOLDE 的 collinear-resonance-ionization spectroscopy 测量 `101–115In`，并结合此前 `113–131In` 数据，提取奇 A 铟同位素 `I^π=9/2+` 基态及可用的 `1/2−` 异能态的核四极矩、磁矩和相对电荷半径。结果显示接近 `N=50` 时集体性下降；作者将其作为支持 `100Sn (Z=N=50)` 双幻数的独立电磁性质证据。该结论是地面态电磁/半径与模型比较的作者解释，不是对 `100Sn` GT 衰变或 `100In` 能级图的直接重测。

## Experimental and Analysis Chain

两次 ISOLDE campaign 使用约 1.4 GeV proton beam 在厚 La 或 uranium-carbide target 上产生铟同位素；离子经选择性共振激光电离、质量分离、冷却聚束和 sodium-vapour neutralization 后进入 CRIS。扫描 246.0/246.8 nm 原子跃迁的 hyperfine spectra，提取 `A_hf`、`B_hf` 和 isotope shifts，再结合 atomic electric-field-gradient calculation 转换为核 `Q_s`、磁矩和电荷半径（PDF pp.2–3、6）。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | research_status | needs_review |
|---|---|---|---|---|---|---|---|
| KAR24-1 | 论文报告 `101–131In` 的精密激光谱学，覆盖从 `N=52` 到 `N=82` 的铟同位素，并提取 `Q_s`、磁矩和差分电荷半径。 | experimental-fact | direct | single | PDF pp.1–3、Table 1–2 | completed | false |
| KAR24-2 | `101In` 的 Table 1 行给出 `Q_s=48.6(16) e·fm²`，随后随中子数增加出现抛物线型集体性趋势；表中 `Q_s` 由 hyperfine `B_hf` 和原子场梯度换算。 | experimental-fact | direct | single | PDF p.6, Table 1 | completed | false |
| KAR24-3 | 作者以铟的 `Q_s` 与相对电荷半径向 `N=50` 的集体性下降，支持 `100Sn` 的双幻数性质。 | author-interpretation | direct | single | PDF pp.1、3–5 | completed | false |
| KAR24-4 | 对 `Q_s` 和半径的 DFT、VS-IMSRG 比较显示理论在集体性幅度、配对和球形参考下存在系统差异；VS-IMSRG 对 `Q_s` 的绝对幅度低估属于模型结果/模型限制。 | model-result | direct | single | PDF pp.3–5；Methods H/I/J | completed | false |
| KAR24-5 | Extended Data Fig.6/Methods K 中，研究的偶偶 Cd PES 很软而 odd-In `9/2+` 构型有 odd-proton-induced axial-prolate minimum；作者据此称静态三轴形变对所研究 cases 不重要。 | model-result | direct | single | PDF pp.18–19，Extended Data Fig.6；结论 p.5 | completed | false |
| KAR24-6 | 论文公开关联数据：101–115In raw archive 为 Zenodo `10.5281/zenodo.10138423`，113–131In companion archive 为 `10.5281/zenodo.6406949`；结果图 CSV 为 Zenodo `10.5281/zenodo.11061390`。 | experimental-fact | direct | single | PDF p.5、Refs.[98–100]；Zenodo API | completed | false |
| KAR24-7 | 2024 source 研究 `In` 地面态电磁性质，不直接提供 `100Sn` β-decay `B(GT)`、`100In` γ branching 或 6+ isomer evidence，因此对 Hinke/Lubos 两条 `B(GT)` 数值没有 material change。 | our-inference | indirect | multiple-independent | PDF pp.1–5；[[hinke-2010-100sn-decay-spectroscopy]]；[[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]] | completed | false |

## Data and L4 Boundary

- Zenodo `10138423` API 当前给出 `CRIS_101-115In_raw-data.zip`，596,324,027 bytes，MD5 `04b6e0dcf719139c6eb710be2dff818e`；Zenodo `6406949` 给出 `In_rich_EMs_data.zip`，390,597,795 bytes，MD5 `5239574e2ab0cbbfb747d32c9ea0a054`。本轮只核对 metadata，不下载两个大型 archive。
- Zenodo `11061390` 给出结果图 CSV/TSV/PDF；本地 CSV 为 7,122 bytes，SHA-256 `5f685ef18a3d6177c8d4f2a89d3b7559c99ecc40a51f242070a7b1cda709e68c`，其行列和 `N/Q_s` 数据与图 2 数据文件身份相符。
- Preprint text 的 Ref.[99] 将“Raw Data Results Figure”写成 `10.5281/zenodo.10138423`，而 Nature publisher page 和 Zenodo 的专门结果图记录指向 `10.5281/zenodo.11061390`；这是 metadata/引用层 discrepancy，不擅自改写成作者勘误。
- 不启动 L4：该数据问题不对应本批次 `100Sn` B(GT) 核心问题，且本轮没有建立新的可检验假设、完整下载输入、参数记录、分析代码和 sensitivity/negative-control package。它只作为未来公开数据研究入口。

## Competing Interpretations and Limitations

- `Q_s` 是由原子超精细参数和 atomic theory conversion 得到的核观测量；它与 γ 衰变 `B(E2)` 不是同一直接实验 observable，不能替代 `100Sn`/`100In` decay evidence。
- “`100Sn` 双幻数”是作者将 In isotope trends、Sn comparison 和 many-body calculations 结合后的解释；它支持壳闭合背景，但不能由此推出 `B(GT)` 值或 `100In` level ordering 已解决。
- DFT/VS-IMSRG 的 pairing、spherical/deformed reference 和 missing correlations 会改变对集体性的解释；“static triaxial deformation irrelevant”限定在论文研究的 In/Cd cases 和模型空间内。
- 两个大型 Zenodo archive 的 metadata 可追溯，但没有在本轮构成可执行的 L4 数据包；结果图 CSV 也只是公开图数据，不等于原始 spectroscopy event data。

## Codex Self-audit

| 审计项 | 判断 | 证据 |
|---|---|---|
| Identity and direct reading | 题名、DOI、卷页、作者首位、arXiv PDF SHA、关键正文/表格页面已核对。 | Crossref/Nature metadata；PDF pp.1–6、18–19 |
| Claim separation | Qs/半径/谱学是实验事实；双幻数是作者解释；DFT/VS-IMSRG/PES 是模型结果；“不改变 BGT”是 Codex scope inference。 | KAR24-1–7 |
| Data provenance | 三个 Zenodo record 的 DOI、文件名、字节数/MD5 已核对；Ref.[99] 与结果图 record 的 DOI 差异单列。 | PDF p.5、Refs.[98–100]；Zenodo API；manifest |
| L4 gate | 没有把公开 CSV 或大型 archive 元数据冒充 L4；无新 analysis run、sensitivity 或 negative control。 | Data and L4 Boundary |
| Review state | 页面仍为 `unreviewed`；`KAR24-* needs_review: false` 表示 Codex 已完成本轮 claim self-audit，不表示用户审核或论文准入。 | frontmatter；KAR24-1–7 |

## Knowledge Impact and Learning Decision

- **支持/温故知新**：为 `100Sn` 双幻数和 A≈100 集体性提供新的、与 GSI/RIKEN 衰变谱学不同实验方法的电磁背景证据。
- **无 material change**：它没有测量 `100Sn` 半衰期、Q/endpoint、`100In` γ branching 或 `B(GT)`，因此不改变 `100Sn` project 的两值差异和核心解释排序。
- **新增边界**：把 `Q_s`–`B(E2)` 转换、DFT/VS-IMSRG 模型依赖、公开数据大小和 DOI discrepancy 写入可追溯记录；不把其结果并入 `100Sn` decay lineages。
- **Persistence**：建立本 source，更新 `100Sn` 汇总/index 和批次温故知新记录；不创建 `101–131In` 全套核素页，不启动 L4。

## Extracted Pages

- Nucleus: [[100sn]]
- Concepts/observables: [[gamow-teller-strength]]、`Q_s`/charge-radius context（不新建重复 observable 页）
- Public data: [[100sn-gamow-teller-independent-evidence]]（仅记录无 material change 和数据边界）

## Related Knowledge

- [[hinke-2010-100sn-decay-spectroscopy]]
- [[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]]
- [[100sn]]
- [[gamow-teller-strength]]

## Later Paper / Q&A Gate

若后续问答或论文写作需要使用“`100Sn` 双幻数由铟电磁矩支持”、某个 `Q_s` 数值或 Zenodo 数据，需回到本页列出的原始页码、原子场梯度转换和数据 record；不得把该 source 当作 `B(GT)` 或 `100In` γ-scheme 的直接证据。
