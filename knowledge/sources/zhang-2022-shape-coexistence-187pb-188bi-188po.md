---
type: source
title: "张文强 2022 博士论文：Z≈82, N≈104 缺中子核区形状共存"
aliases: [张文强形状共存论文, Wenqiang Zhang shape coexistence thesis]
created: 2026-09-10
updated: 2026-09-10
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment
reading_depth: deep-read
title_original: "Shape Coexistence in Neutron-Deficient Nuclei with Z≈82, N≈104"
authors: [张文强]
journal: "中国科学院大学博士学位论文"
year: 2022
pages: 132
language: zh/en
canonical_source: "张文强. Z=82,N=104核区缺中子原子核的形状共存研究[D]. 中国科学院大学, 2022."
citation_key: ""
raw_file: "raw/papers/degree dissertation/张文强.pdf"
raw_sha256: "0BC7A14983E601D81D7E2052587F114B4ECE87756F77955A004D0AAE616616CC"
nuclei: [187pb, 188bi, 188po]
experiments: [argonne-gas-filled-analyzer-187pb-188bi-188po]
models: [potential-energy-surface, cranked-shell-model]
observables: [lifetime, be2, gamma-ray-energy, rdt-efficiency]
methods: [in-beam-gamma-spectroscopy, recoil-decay-tagging, delayed-gamma-spectroscopy]
tags: [shape-coexistence, shape-isomer, a190, phd-thesis]
---

# 张文强 2022：`Z≈82, N≈104` 缺中子核区形状共存

## Bibliographic Record

张文强，*Z=82,N=104核区缺中子原子核的形状共存研究*，中国科学院大学博士学位论文，2022，132 页。原始 PDF SHA-256 为 `0BC7A14983E601D81D7E2052587F114B4ECE87756F77955A004D0AAE616616CC`。

## Scope and Reading Depth

- `deep-read`：读取题名页、摘要（PDF pp.7–10）、目录、实验与数据处理章节（Chs.2–4）、`187Pb` 结果/讨论（Ch.5）、`188Bi/188Po` 结果/讨论（Ch.6）和总结（Ch.7，PDF pp.94、111–113）。
- 重点视觉/文本核对 RDT 关联、isomer 半衰期、能级/转动带摘要、`B(E2)` 数值、Po `2+` 能量和 RDT efficiency 讨论。
- 未覆盖：293 条参考文献的逐篇原文复核、全部矩阵元的独立重算；模型和作者解释保持未审核。

## Summary

论文以 Argonne Gas-Filled Analyzer 的 RDT 在束/延迟 γ 谱学研究 `187Pb`、`188Bi`、`188Po`，将 isomer、转动带和低位 `2+` 结果放入形状共存问题中。

## Key Results

## Experimental design and key claims

实验在 Argonne Gas-Filled Analyzer 进行，以 `50Cr + 142Nd → 192Po*` 熔合蒸发产生 `187Pb`、`188Bi`、`188Po`，用 prompt/delayed γ spectroscopy 与 recoil-decay tagging 区分核素（摘要 pp.7–10；Ch.3）。

| issue_id | 主张 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DD-20260910-MP-001 | `187Pb` 在球形 `3/2−` 基态上方 `308 keV` 发现 `5.15(15) μs` isomer；其上建立强耦合转动带。 | experimental-fact | direct | 摘要 p.7；Ch.5.4，PDF p.94 | true |
| DD-20260910-MP-002 | 该带与 `185Hg` 的 `7/2−[514]` 长椭带相似，作者据此把 isomer 指认为 `(7/2−)`、长椭形状，并由 `B(E2)=5.6(2)×10−4 W.u.` 解释迟发跃迁。 | author-interpretation | indirect | 摘要 p.7；Ch.5.3–5.4 | true |
| DD-20260910-MP-003 | 结合既有 α 衰变/激光谱学和 PES，作者提出 `187Pb` 负宇称低能区存在球形–扁椭–长椭三重形状共存。 | author-interpretation + model-result | indirect | 摘要 pp.7–10；Ch.5.4 p.94；Ch.7 p.113 | true |
| DD-20260910-MP-004 | `188Bi` 的 `(10−)` isomer 半衰期为 `0.25(5) μs`，其上瞬发级联是长椭转动带候选；`188Po` 首个 `2+` 能量为 `242(2) keV`。 | experimental-fact + author-interpretation | direct/indirect | Ch.6.4，PDF p.111；摘要 p.10 | true |
| DD-20260910-MP-005 | `188Bi/188Po` 的 RDT γ 产额可能因长寿命 isomer 飞离靶和未观测强内转换跃迁而降低；作者将其作为效率/可行性边界。 | analytical-boundary | indirect | Ch.6.3.4–6.4，PDF pp.109–111 | true |

## Competing Interpretations and Limitations

`187Pb` 的形状指认依赖同中子素相似性、PES 和 `B(E2)`，不是独立直接的形状测量；三重共存还依赖 α/激光谱学的依赖来源。`188Bi` 级联的长椭解释仍是候选，`188Po 2+` 的低能量也不能单独证明形状。RDT efficiency 解释需要对 conversion、isomer lifetime、飞行距离和门条件做灵敏度检查。

## Knowledge impact and relations

- Effect: `supports` and `extends`；为 A≈190 形状共存、isomer 与 RDT efficiency 提供 thesis-level evidence，同时限制“已证明形状”的措辞。
- Related: [[triaxial-shape-coexistence]]（形状共存判据背景）、[[nuclear-chirality-and-multiple-chiral-doublet-bands]]（竞争判据背景）、[[recoil-distance-doppler-shift]]。
- Shared/independent lineage：本论文的 RDT 数据是单一实验谱系，不能与后续期刊复述重复计为独立实验。

## Human review triage

### P0

- `DD-20260910-MP-001/002`：核对 `308 keV`、`5.15(15) μs`、`B(E2)`、带头和 `(7/2−)` 指认；风险是把模型/系统学解释写成直接形状观测。
- `DD-20260910-MP-003`：核对三重共存所依赖的独立 α/激光证据和 PES 条件。

### P1

- `DD-20260910-MP-004/005`：核对 `188Bi`/`188Po` 级联与 RDT efficiency 的门条件、conversion 和未观测信号边界。

## Knowledge increment

`new-knowledge`: 将 `187Pb` shape-isomer、`188Bi` low-lying isomer 和 `188Po` `2+` 结果置于同一 RDT 实验链；`boundary/failure-knowledge`: RDT 产额低并不等于没有带结构，长寿命/内转换会改变可见性。所有 issue 保留 `needs_review`。

## Extracted Pages

- 摘要：PDF pp.7–10；方法/数据：Chs.2–4；`187Pb`：Ch.5；`188Bi/188Po`：Ch.6；总结：Ch.7，PDF pp.94、111–113。
