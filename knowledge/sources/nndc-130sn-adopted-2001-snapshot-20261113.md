---
type: source
title: "NNDC 130Sn 采用能级与衰变数据（2001年评价快照）"
aliases: [NNDC 130Sn 2001 evaluation, NuDat 3 130Sn adopted, Singh 2001 NDS 130Sn]
created: 2026-11-13
updated: 2026-11-13
status: active
review_status: unreviewed
source_type: evaluated-data-review
reading_depth: skimmed
title_original: "Nuclear Data Sheets for A = 130"
authors: [Balraj Singh]
journal: Nuclear Data Sheets
year: 2001
volume: "93"
pages: "33–242"
doi: "10.1006/ndsh.2001.0011"
canonical_source: "B. Singh, Nuclear Data Sheets 93, 33 (2001); NNDC NuDat 3 online snapshot cutoff 11-May-2001"
citation_key: singh-2001-nds-130sn-adopted
raw_file: raw/papers/gpt/query/20261113-A130-seniority-check/nudat3-130sn-adopted.html
raw_sha256: 5ebd6fc678cdd6af703981f7e3fba424fb5bb5ae3f2fad6a6efacc4c9404932c
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261113-A130-seniority-check/manifest.json
actual_read_pages: [1]
actual_read_scope: "NNDC NuDat 3 数据库在线采用能级与射线表HTML快照，定向核查 130Sn 激发能 2434.79(12) keV 态及其 96.54(5) keV E2 跃迁分支参数。本数据基于 2001 年 5 月 11 日截断的 B. Singh NDS 93 (2001) 评价，2026 年抓取快照仅为获取时间，不代表 2026 年新测量或最新核数据评价。"
nuclei: [130sn]
reactions: [beta-minus-decay]
experiments: []
models: [spherical-shell-model, seniority-isomers]
observables: [level-energy, half-life, gamma-energy, transition-multipolarity, b-e2, conversion-coefficient]
methods: [evaluated-nuclear-structure-data]
tags: [A130, 130sn, isomers, seniority, b-e2, half-life, nndc, evaluated-data]
---

# NNDC 130Sn 采用能级与衰变数据（2001年评价快照）

## Bibliographic Record

- **数据来源**：美国布鲁克海文国家实验室国家核数据中心（NNDC）NuDat 3 数据库在线抓取快照。
- **评价依据与发表信息**：Balraj Singh, *Nuclear Data Sheets for A = 130*, Nuclear Data Sheets 93, 33–242 (2001), DOI: 10.1006/ndsh.2001.0011。
- **文献截断日期（Cutoff Date）**：2001 年 5 月 11 日。
- **本地归档文件**：`raw/papers/gpt/query/20261113-A130-seniority-check/nudat3-130sn-adopted.html`（36,108 字节，SHA-256: `5ebd6fc678cdd6af703981f7e3fba424fb5bb5ae3f2fad6a6efacc4c9404932c`）。
- **时间界限声明**：本记录创建于 2026 年 11 月 13 日，反映 2026 年从 NNDC 镜像获得的 2001 年基线评价数据；严禁将获取时间误称为“2026 年新实验”或“最新已验证评价数据”。

## Scope and Reading Depth

本记录基于本地 HTML 快照的定向核查，仅覆盖 $^{130}\mathrm{Sn}$ 高自旋异能态及其主要退激分支行：
- 能级行：$E_x = 2434.79(12)\text{ keV}$，$J^\pi = (10^+)$，半衰期 $T_{1/2} = 1.61(15)\,\mu\mathrm{s}$；
- 退激射线：$E_\gamma = 96.54(5)\text{ keV}$，多极度 $E2$，终态能级 $2338.26(11)\text{ keV}$，终态 $J^\pi = (8^+)$；
- 附加射线数据表（Additional Gamma Data）：总内转换系数 $\alpha = 1.829$（$\alpha_K = 1.313, \alpha_L = 0.414$），约化跃迁几率 $B(E2) = 0.38(4)\,\text{W.u.}$。

未对 $^{130}\mathrm{Sn}$ 全部 40 余条低激发能级与复杂中子共振态进行全库核对。

## Summary

该评价快照给出了 $^{130}\mathrm{Sn}$ 中微秒级高自旋同核异能态的基准采用数据。结果表明，半衰期为 $1.61(15)\,\mu\mathrm{s}$ 的异能态身份为 $(10^+)$ 态（位于 $2434.79\text{ keV}$），其主要通过发射一条低能 $96.54\text{ keV}$ 的 $E2$ 跃迁退激至下方的 $(8^+)$ 态（位于 $2338.26\text{ keV}$），实测跃迁强度为 $B(E2) = 0.38(4)\,\text{W.u.}$。该数据直接澄清了文献草稿中将该态误记为 $8^+ \to 6^+$ 跃迁（$E_\gamma = 400\text{ keV}, B(E2) = 0.05\,\text{W.u.}$）的混淆错误。

## Key Results

| ID | 声明与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NNDC-130SN-1 | $^{130}\mathrm{Sn}$ 具有位于 $E_x = 2434.79(12)\text{ keV}$ 的 $(10^+)$ 异能态，半衰期为 $T_{1/2} = 1.61(15)\,\mu\mathrm{s}$（来源自 1981Fo02 等 $\beta\gamma(t)$ 测量）。 | evaluated-level | direct | HTML table row `2434.79 12` | false |
| NNDC-130SN-2 | 该 $(10^+)$ 异能态主要通过 $E_\gamma = 96.54(5)\text{ keV}$ 的 $E2$ 跃迁向 $(8^+)$ 态（$E_x = 2338.26(11)\text{ keV}$）退激，分支比强度为 100。 | evaluated-decay | direct | HTML table row `96.54 5 E2` | false |
| NNDC-130SN-3 | 该 $96.54\text{ keV}$ 跃迁的总内转换系数为 $\alpha = 1.829$，实测约化跃迁几率为 $B(E2) = 0.38(4)\,\text{W.u.}$。 | evaluated-electromagnetic | direct | HTML `AdditionalGammaData` row `2434.79` | false |
| NNDC-130SN-4 | 在纯单 $j=11/2$ 壳层（$\Omega_j = 6$）假定下，该态对应于 $h_{11/2}^{10}$（两中子空穴，即 $n=10, v=2$），其归约因子平方为 $[(\Omega_j - n)/(\Omega_j - v)]^2 = [(-4)/4]^2 = 1$，属于粒子-空穴对称态而非处于 $n=\Omega_j=6$ 的半满相消零点；其长寿命主因在于 $96.54\text{ keV}$ 的低跃迁能量与大内转换。 | task-deduction | direct | Algebraic check on Eq.(3.20) | false |

## Competing Interpretations and Limitations

本数据反映 2001 年 B. Singh 评价快照，后续若有更新的高精度在束测量（例如重离子深非弹性散射或裂变碎片谱学），需以最新主测量为准。此处采用 2001 评价作为典型历史教学基准反例，说明低能相空间与自旋陷阱可独立诱发微秒长寿命，不可将所有长寿命态都强行归结为半满壳相消。

## Extracted Pages

选读范围直接对应本地文件 `raw/papers/gpt/query/20261113-A130-seniority-check/nudat3-130sn-adopted.html` 中的能级表及附加 $\gamma$ 射线表，关键参数提取至 [[a130-rewrite-seniority-k-selection-20261113]]，作为博士论文第 4.6 节中澄清 $^{130}\mathrm{Sn}$ 粒子-空穴对称性反例的严格数据锚点。
