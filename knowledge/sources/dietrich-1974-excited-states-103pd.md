---
type: source
title: "Dietrich 等 1974：103Pd 激发态与 11/2− 寿命"
aliases: [Excited States in 103Pd, UUIP-882 103Pd]
created: 2026-09-05
updated: 2026-09-05
status: ai-draft
review_status: unreviewed
source_type: experiment-report
reading_depth: deep-read
title_original: "Excited States in 103Pd"
authors: [W. Dietrich, B. Nyman, A. Johansson, A. Bäcklin]
advisor: []
journal: "Uppsala University Institute of Physics report UUIP-882"
year: 1974
volume:
pages: 40
doi:
arxiv:
language: en
canonical_source: "Dietrich, W.; Nyman, B.; Johansson, A.; Bäcklin, A. Excited States in 103Pd. Uppsala University Institute of Physics, UUIP-882, 1974."
zotero_item_key:
citation_key: ""
zotero_uri:
library_file: "raw/papers/degree dissertation/EXCITED STATES IN 103Pd.pdf"
raw_file: "raw/papers/degree dissertation/EXCITED STATES IN 103Pd.pdf"
raw_sha256: "671665819972AC68EFFEA51FFCB18A2C48769A42466D2C2AB96B61BEADE9CE59"
nuclei: [103pd]
reactions: ["103Rh(p,nγ)103Pd", "102Pd(d,n)103Ag followed by 103Ag decay"]
experiments: []
models: [shell-model]
observables: [internal-conversion-coefficient, angular-distribution, lifetime, excitation-function]
methods: [gamma-gamma-coincidence, internal-conversion-analysis, angular-distribution]
tags: [a100, palladium, level-scheme, internal-conversion, experiment-report]
---

# Dietrich 等 1974：`103Pd` 激发态与 `11/2−` 寿命

## Bibliographic Record

W. Dietrich、B. Nyman、A. Johansson、A. Bäcklin，*Excited States in 103Pd*，Uppsala University Institute of Physics report `UUIP-882`，1974，40 页。该文件是实验报告，不计入本批次 15 篇学位论文。原始 PDF SHA-256 为 `671665819972AC68EFFEA51FFCB18A2C48769A42466D2C2AB96B61BEADE9CE59`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 摘要、引言、实验步骤、反应/衰变结果、内转换测量、角分布和结论；核对 `103Rh(p,nγ)`、`103Ag` 衰变、25 个能级、spin-parity tentative assignments 和 784 keV `11/2−` lifetime。
- Not covered: 参考文献原文及扫描/OCR 表格的逐数字再测量。
- Coverage caveats: 报告明确称多数 spin-parity 为 tentative；PDF 为旧扫描 OCR，正式引用前需回看原始表格/谱图。

## Paper Question and Scientific Motivation

报告旨在扩展 `103Pd` 低能级纲图，并利用相对激发函数、γ 多极性、log ft、K-shell conversion 和 pulsed-beam timing 改善自旋宇称及寿命信息（Abstract；pp.1–3）。

## Method and Design Logic

实验在 Uppsala Tandem 进行：`103Rh(p,nγ)` 测量 γ 射线、相对激发函数和角分布；`103Ag` 衰变提供独立 γ/γγ 数据；Si(Li) 内转换谱仪测量 conversion electrons；pulsed proton beam 用于 `11/2−` level lifetime（pp.1–3）。

## Key Evidence and Reasoning Chain

1. 反应和衰变 γ lines 建立/修订 `103Pd` level scheme。
2. 相对激发函数利用 `103Rh` 靶自旋 1/2 和 `(p,2n)` 阈值区分不同 spin feeding。
3. 多极性、K-conversion 和 log ft 共同给出多数能级的 tentative spin/parity。
4. 脉冲束流时间谱得到 784 keV `11/2−` level 的 25±2 ns 半衰期。

## Summary

报告构建了明显扩展的 `103Pd` level scheme，涵盖反应和 `103Ag` 衰变中的约 25 个能级；大多数 spin-parity 仍为 tentative。K-shell conversion、γ multipolarity、relative excitation functions 和 log ft 提供互补约束；784 keV `11/2−` 态寿命测为 `25±2 ns`。

## Experimental or Theoretical Setup

- Uppsala Tandem；两枚 Ge(Li) 探测器、Si(Li) magnetic-lens conversion spectrometer。
- `103Rh(p,nγ)` 反应、`103Ag` 衰变、相对激发函数和 9 角度 γ angular distributions。
- shell-model/systematics 仅作背景；spin/parity assignments 多为 tentative。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| DP74-1 | `103Pd` 能级由 `103Rh(p,nγ)` 和 `103Ag` 衰变的 γ 与内转换测量研究，并建立修订/扩展纲图。 | experimental-fact | direct | multiple-independent | Abstract；pp.1–3 | true |
| DP74-2 | 报告对观察到的大多数约 25 个能级给出 tentative spin-parity assignments，依据包括相对激发函数、多极性、K-conversion 和 log ft。 | experimental-criterion | direct | multiple-independent | Abstract；pp.1–6 | true |
| DP74-3 | 784 keV 的 `11/2−` level 半衰期测为 `25±2 ns`。 | experimental-fact | direct | single | Abstract；lifetime section | true |
| DP74-4 | `103Rh` 靶基态自旋 1/2、`(p,2n)` 高阈值和相对 excitation-function slope 被用于约束产物态 spin。 | experimental-criterion | direct | single | Introduction；pp.1–3 | true |
| DP74-5 | K-shell conversion electron 和 γ angular distributions 为 parity/multipolarity assignment 提供互补证据。 | experimental-criterion | direct | single | Experimental procedure；results | true |
| DP74-6 | 该报告的 assignment 整体不是现代精确 level evaluation；扫描/OCR 表格和多数 tentative labels 需要正式使用前回看原页。 | analytical-boundary | inferred | single | Abstract；report-wide | true |

## Nuclear Structure Information

- `103Pd`：低能级纲图、`11/2−` 784 keV isomer/lifetime candidate、conversion/multipolarity。
- 方法复用：relative excitation function、K-conversion、γ angular distribution、pulsed-beam lifetime。

## Authors' Interpretation

作者将 assignment 作为基于多种实验指标的 tentative 结论，并强调与历史数据的冲突和低能级研究价值。

## Model Results

模型只作为 level/spin systematics 背景；本报告主要是实验来源。

## Competing Interpretations and Limitations

- 多数 spin/parity 不唯一；需结合后来 Nuclear Data Sheets 或原始表格重新核验。
- 旧 OCR 可能误读数值、符号和同位素上标；正式引用不得仅依赖文本提取。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-DP74-1 | Core reconstruction | 可复用核心是早期 `103Pd` level-scheme 与内转换/角分布联合 assignment 案例。 | DP74-1–5 | unreviewed |
| AR-DP74-2 | Assumptions and dependencies | spin/parity 依赖 excitation-function、multipolarity、conversion 和 log ft 的联合判据。 | pp.1–6 | unreviewed |
| AR-DP74-3 | Transfer conditions | 可用于 `103Pd` 历史基线和方法背景，不宜直接与现代 A≈100 数据拼接。 | DP74-2–6 | unreviewed |
| AR-DP74-4 | Failure conditions | OCR/assignment 修正或后续数据若改变 784 keV level identity，寿命/带页需修订。 | DP74-3/6 | unreviewed |
| AR-DP74-5 | Reverse/falsification test | 回看扫描原页、原始 spectra、conversion coefficients，并与后续 evaluated level scheme 比较。 | Report pp.1–40 | unreviewed |
| AR-DP74-6 | Research-question decision | 作为历史 experimental-method source 保存；不进入当前 wobbling/chirality evidence pool。 | DP74-1–6 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 现有 A≈100 `105Pd` wobbling来源，但缺少 `103Pd` 早期低能级/内转换基线。
- Effect of this source: supports historical method background；limits 对 tentative assignment 的直接可用性。
- Reason: 补充 `103Pd` level scheme、conversion 和寿命历史入口。
- Persistence decision: 新建 source；是否建立 `103Pd` nucleus page 留待后续使用决定。
- Review state: 页面 `unreviewed`；DP74-1–6 保留 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[internal-conversion-analysis]] | K-shell conversion 与 multipolarity assignment 案例。 |
| foundational-background | [[spin-parity-assignment]] | 早期 excitation-function/log ft/angular-distribution 联合判据。 |
| limits | [[105pd]] | `103Pd` 是历史邻核背景，不能直接替代 `105Pd` wobbling evidence。 |

## Human Review Triage

### P0

- DP74-3：核对 784 keV `11/2−` level 的能量、宇称和 `25±2 ns` 半衰期，风险是 OCR/旧 assignment 误读。
- DP74-1/DP74-2：核对 level count、reaction/decay provenance 和 tentative assignment 范围。

### P1

- DP74-4/DP74-5：回看 excitation-function、K-conversion 和 angular-distribution 表格。
- DP74-6：正式论文使用前必须回看原始扫描页并与后续 evaluated data 交叉核验。

### P2/P3

- 作为附加实验报告，不计入 15 篇学位论文统计。

## Extracted Pages

- Nuclei: `103Pd` 暂不新建。
- Methods: [[internal-conversion-analysis]]、[[spin-parity-assignment]]。

## Non-source Notes and Follow-up

此来源明确是 `UUIP-882` 实验报告，不应被目录位置误判为博士论文。
