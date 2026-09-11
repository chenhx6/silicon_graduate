---
type: source
title: "刘红娜 2015 博士论文：12C 中子质子关联以及三体力的研究"
aliases: [刘红娜 12C np correlations thesis, Hongna Liu 12C thesis]
created: 2026-09-11
updated: 2026-09-11
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment
reading_depth: deep-read
title_original: "12C的中子质子关联以及三体力的研究"
authors: [刘红娜]
advisor: [叶沿林, Jenny Lee, H. Sakurai]
journal: "北京大学博士学位论文"
year: 2015
volume:
pages: 124
doi:
arxiv:
language: zh/en
canonical_source: "北京大学博士学位论文, 2015"
zotero_item_key:
citation_key:
zotero_uri:
library_file: "raw/papers/degree dissertation/刘红娜.pdf"
raw_file: "raw/papers/degree dissertation/刘红娜.pdf"
raw_sha256: "fe17cc42333e33a2325bc2124e5b2a9541408e1a9303161e74f592e55c8b9c25"
nuclei: [12c, 10b, 10be]
reactions: ["9Be(12C,11B)X", "9Be(12C,10B)X", "9Be(12C,10Be)X"]
experiments: ["RIKEN RIBF 190 MeV/u 12C on 9Be"]
models: [eikonal-reaction-model, WBP-shell-model, no-core-shell-model]
observables: [inclusive-cross-section, partial-cross-section, np-correlation, isospin]
methods: [two-nucleon-knockout, gamma-residue-coincidence, BigRIPS, SAMURAI, DALI2]
tags: [degree-dissertation, 12c, np-correlation, 3n-forces, knockout, RIBF]
---

# 刘红娜 2015：`12C` 中子质子关联与三体力

## Bibliographic Record

刘红娜，*`12C` 的中子质子关联以及三体力的研究*，北京大学博士学位论文，2015，PDF 124 页。原始文件 SHA-256 为 `fe17cc42333e33a2325bc2124e5b2a9541408e1a9303161e74f592e55c8b9c25`。论文工作在 RIKEN RIBF 完成，涉及 BigRIPS、SAMURAI 和 DALI2。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 题名页/摘要（PDF pp.1–7）；目录和引言（pp.8–21）；束流、靶、探测器和触发（pp.47–70）；粒子鉴别、γ-残余核符合和截面分析（pp.72–94）；理论比较及总结（pp.100–110）；结论页 PDF p.109 和关键谱图 p.47、p.66 视觉核对。
- Not covered: 全部原始事件树、每条 γ 线的独立校准和参考文献逐篇复核。
- Coverage caveats: 截面和比值依赖效率、接受度、残余核 level scheme 与 eikonal/TNA 约定；3N force 的作用不能由本论文单独定量分离。

## Paper Question and Scientific Motivation

论文以双核子敲出反应作为 `N=Z` 核中 `np` 关联的探针，重点区分 `T=0` 与 `T=1` 关联，并检验 p-shell/WBP、NCSM 和三体力对实验截面的解释能力（摘要 PDF pp.3–7）。

## Method and Design Logic

使用 `190 MeV/u 12C+9Be` 反应；BigRIPS 的 `ΔE-TOF` 选择入射束，SAMURAI 以 `ΔE-Bρ-TOF` 识别残余核，DALI2 测量退激 γ。γ-残余核符合把不同 `10B/10Be` 末态分开，再由束流计数、靶厚度、效率和反应产额得到 inclusive/partial cross sections（PDF pp.47–70、72–94）。

## Key Evidence and Reasoning Chain

1. `190 MeV/u` 反应和粒子鉴别 → 得到四个反应道的单举截面（PDF pp.3–4、72–84）。
2. DALI2 γ 与残余核符合 → 分离 `10B` 不同同位旋末态（PDF pp.84–94、Fig.6-1）。
3. `T=0/T=1` 部分截面比 → 约束 `12C` 中 `np` 关联相对强度（PDF p.109）。
4. WBP/eikonal 与 NCSM+3N 比较 → 识别理论低估和三体力解释边界（PDF pp.89–110）。

## Summary

论文报告四个反应道截面约为 `82(2)`、`62(2)`、`42(2)` 和 `9.1(3) mb`，得到 `σ_np/σ_pp=4.6(3)`；`10B` 基态 `T=0,Jπ=3+` 的部分截面为 `20.3(15) mb`，`T=0/T=1=5.9(4)`。WBP p-shell 能较好描述部分 `T=1`/pp 截面，但对 `T=0 np` 低估约一倍；NCSM+3N 可重现趋势但不能同时重现实验绝对值，因此三体力的独立作用仍未清楚。

## Experimental or Theoretical Setup

- Beam/reaction: `190 MeV/u 12C + 9Be` at RIBF。
- Detectors: BigRIPS, SAMURAI, DALI2。
- Observable chain: inclusive and final-state-resolved cross sections, γ-residue coincidence, isospin-separated partial cross sections。
- Theory: eikonal reaction model combined with WBP p-shell or NCSM wave functions, with/without 3N interactions。

## Key Results

| issue_id | priority | core_claim | claim_kind | evidence_level | source_independence | locator | research_status | stage_conclusion | knowledge_increment | remaining_uncertainty | next_autonomous_route | needs_review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DD-20260910-12C-01 | P0 | `190 MeV/u 12C+9Be` 配合 BigRIPS/SAMURAI/DALI2 提取双核子移除到 `10B/10Be` 末态的截面。 | experimental-fact | direct | single | PDF pp.3–7、47–70、72–84 | completed | 实验链和末态分辨方法已核对。 | 新知识 | 接受度和效率系统误差需回到原始表格复核。 | 回读截面归一化、效率和 γ-残余核门条件。 | true |
| DD-20260910-12C-02 | P0 | 四个单举截面约 `82(2),62(2),42(2),9.1(3) mb`，且 `σ_np/σ_pp=4.6(3)`。 | experimental-fact | direct | single | PDF pp.3–4、109–110 | completed | 数值可作为论文直接报告，不能脱离反应定义泛化。 | 新知识 | 不同能量文献的比较依赖相同截面定义和修正。 | 核对表 1-1 至 1-3 的能量、门条件和误差预算。 | true |
| DD-20260910-12C-03 | P0 | `10B` 基态 `T=0,Jπ=3+` 部分截面 `20.3(15) mb`，`T=0/T=1=5.9(4)`，显示 `T=0 np` 关联增强。 | experimental-criterion | direct | single | PDF pp.66、89–94、109–110 | completed | 这是本论文最强的实验约束，但仍是模型定义下的关联 proxy。 | 总结知识 | 末态混合、效率和残余核 level scheme 可能影响分解。 | 独立复算末态归一化并比较其它 N=Z 核。 | true |
| DD-20260910-12C-04 | P1 | WBP/eikonal 对 `T=0 np` 低估约一倍；NCSM+3N 重现趋势但不重现绝对值，3N 的单独贡献不能明确归因。 | model-result + author-interpretation | indirect | single | PDF pp.89–110、Fig.6-1–6-3 | partially-researched | 阶段结论是模型缺口已定位，3N attribution 未闭合。 | 边界/失败知识 | 反应机制、短程关联和波函数截断彼此耦合。 | 做不同波函数/反应模型的敏感性与负例比较。 | true |

## Nuclear Structure Information

本来源主要提供 `12C` 双核子移除和 `10B/10Be` 末态截面，未建立完整高自旋能级纲图。`10B` 基态和同位旋分解是实验入口，不应被写成直接的静态配对波函数测量。

## Authors' Interpretation

作者把较大的 `T=0` 末态截面和 `T=0/T=1` 比值解释为 `T=0 np` 关联增强，并将 WBP 与 NCSM 的差异用于讨论三体力与反应机制。

## Model Results

Eikonal+WBP 与 Eikonal+NCSM(+3N) 都是模型计算。NCSM+3N 只能说明趋势改善，不足以单独证明三体力就是实验-理论差异的唯一来源。

## Competing Interpretations and Limitations

- `np` knockout 截面还受短程关联、中心质心运动、末态相互作用和 eikonal 近似影响。
- `T=0/T=1` 分解依赖 γ-残余核门、level scheme 和同位旋标记。
- 同一实验的期刊/报告/论文若存在，应按 lineage 合并，不重复计数。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-12C-1 | Core reconstruction | 论文把残余核识别、γ 标记和理论截面比较连接成可复用的 np-correlation evidence chain。 | DD-20260910-12C-01–04 | unreviewed |
| AR-12C-2 | Assumptions and dependencies | 末态截面、效率、接受度和 eikonal/TNA 共同决定比值。 | PDF pp.72–110 | unreviewed |
| AR-12C-3 | Reverse test | 需在不同能量、不同 N=Z 核和多种 reaction model 下复算，并检查 T=0/T=1 门定义。 | DD-20260910-12C-03/04 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 原有高自旋和反应方法来源中缺少这条 `12C` np-correlation/3N thesis evidence。
- Effect of this source: `supports` the general requirement to separate experiment and reaction-model inference, and adds a new cross-domain method source。
- Reason: 提供有 locator 的末态分辨和明确的理论失败边界。
- Persistence decision: source-only；当前不新建 `12C`/`10B` nucleus pages。
- Review state: `unreviewed`，claims retain `needs_review: true`。

## Related Knowledge and Project Relations

| relation_type | target | specific_relation |
|---|---|---|
| methodological-bridge | [[in-beam-gamma-spectroscopy]] | γ-残余核符合在反应截面分解中的作用。 |
| limits | [[nuclear-chirality]] | 该来源与手征无直接证据，不应被用于高自旋形变结论。 |
| not-direct-evidence | [[triaxial-projected-shell-model]] | 反应截面模型不是 TPSM 能级计算。 |

## Human Review Triage

### P0

- `DD-20260910-12C-02/03`：PDF pp.3–4、89–110；核对截面定义、数值、末态 `T/Jπ` 和比值误差。
- `DD-20260910-12C-04`：PDF pp.89–110；核对 WBP、NCSM+3N 的比较是否被写成三体力定量证明。

### P1

- `DD-20260910-12C-01`：核对 BigRIPS/SAMURAI/DALI2 的门条件和效率。

### P2/P3

原始事件级数据和所有参考文献留待具体复算时处理。

## Extracted Pages

- Nuclei: 本轮不创建。
- Concepts: np correlation / 3N force 仅作为本 source 的主题。
- Methods: BigRIPS、SAMURAI、DALI2、two-nucleon knockout 的方法链记录在本页。

## Non-source Notes and Follow-up

PDF p.109 结论页已视觉核对；文本提取用于定位数值。未修改 raw、BibTeX 或任何实验原始数据。
