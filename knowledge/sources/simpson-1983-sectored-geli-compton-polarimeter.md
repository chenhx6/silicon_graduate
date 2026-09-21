---
type: source
title: "Application of a sectored Ge(Li) detector as a Compton polarimeter"
aliases: ["Simpson 1983 sectored GeLi polarimeter", "Sectored Ge(Li) Compton polarimeter"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: method
reading_depth: deep-read
title_original: "Application of a sectored Ge(Li) detector as a Compton polarimeter"
authors: ["J. Simpson", "P. A. Butler", "L. P. Ekström"]
journal: "Nuclear Instruments and Methods"
year: 1983
volume: 204
pages: "463-469"
doi: "10.1016/0167-5087(83)90074-1"
citation_key: Simpson_1983
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
language: en
canonical_source: "Simpson, J., Butler, P. A. & Ekström, L. P. Application of a sectored Ge(Li) detector as a Compton polarimeter. Nucl. Instrum. Methods 204, 463-469 (1983)."
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1983_Simpson et al_Application of a sectored Ge(Li) detector as a Compton polarimeter.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1983_Simpson et al_Application of a sectored Ge(Li) detector as a Compton polarimeter.pdf"
raw_sha256: "1216684723d0b98daef22997446168c628951c1a062d8d9283ef3efc9fafa6d9"
nuclei: ["158Er"]
reactions: ["146Nd(16O,4n)158Er"]
models: []
observables: ["linear-polarization", "polarization-asymmetry", "polarimeter-sensitivity", "coincidence-efficiency", "figure-of-merit"]
methods: ["compton-polarimetry", "linear-polarization-asymmetry"]
tags: [Compton-polarimeter, sectored-GeLi, detector-response, 158Er, linear-polarization]
---

# Application of a sectored Ge(Li) detector as a Compton polarimeter

## Bibliographic Record

- 作者：J. Simpson, P. A. Butler, L. P. Ekström。
- 期刊：*Nuclear Instruments and Methods* 204, 463-469 (1983)。DOI：`10.1016/0167-5087(83)90074-1`。
- 原始文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1983_Simpson et al_Application of a sectored Ge(Li) detector as a Compton polarimeter.pdf`；SHA-256：`1216684723d0b98daef22997446168c628951c1a062d8d9283ef3efc9fafa6d2`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.463-469 全文；sectored Ge(Li) 结构、`P/A/Q` 定义、A/B/C coincidence configurations、calibration reactions、efficiency/sensitivity/figure-of-merit curves、电子学和 `158Er` 应用、Table 2/3、Figs.1-11 全部阅读，关键图表视觉核对。
- Not covered: 原始 calibration spectra/event files、完整 electronics response simulation 和引用文献正文。
- Coverage caveats: 1983 年单晶 sectored Ge(Li) 的 `Q`、效率和 F 值是装置特定结果；不能直接替代现代 clover/tracking polarimeter calibration。

## Paper Question and Scientific Motivation

- 论文问题：单个外接触分成八个扇区的 Ge(Li) 晶体，能否像多晶体阵列一样通过 Compton scattering 测量 γ 线性偏振，并在效率与灵敏度之间取得可用折衷（摘要；PDF pp.463-464）。
- 作者进一步把装置用于 `146Nd(16O,4n)158Er` 高自旋 γ 跃迁的线偏振测量。

## Method and Design Logic

- 探测器为外 n 型接触被切成八个绝缘 wedge sectors 的 coaxial Ge(Li) 晶体，另有 core；径向电荷收集使八个扇区近似独立探测器（PDF p.463，Fig.1）。
- 通过不同扇区组合选择近似平行/垂直反应面的 Compton scatters，定义
  `P=[J(φ=0°)−J(φ=90°)]/[J(φ=0°)+J(φ=90°)]`、
  `A=[aN⊥−N∥]/[aN⊥+N∥]`、`A=QP`（PDF p.464，式 (1)-(3)）。
- 三种 sector coincidence configurations A/B/C 分别优化几何方向组合；效率 `εc`、灵敏度 `Q` 和 figure of merit `F=Q²εc` 被分开测量，强调 sensitivity/efficiency trade-off（PDF pp.465-468，式 (4)-(8)）。

## Key Evidence and Reasoning Chain

1. 1.33 MeV `60Co` 测试中，单/双 sector events 约各占 40%，相邻 sector scatter 占双 sector events 的约 75%；说明装置可获得有效 Compton coincidences（PDF p.464，Table 1）。
2. 用已知偏振 E2 transitions（`328/356 keV` `192Pt`、`847 keV` `56Fe`、`1369 keV` `24Mg`、`1779 keV` `28Si`、`4430 keV` `12C`）标定 `Q`（PDF p.466，Table 2）。
3. 配置 C 的 `εc` 最大，配置 B 的 `Q` 最高且接近典型三 Ge(Li) polarimeter；配置 A/C 的 `Q` 约为 B 的一半。提高 sector threshold 可升高 `Q` 但降低效率（PDF pp.466-467，Figs.5-8）。
4. 配置 C 在 `1.33 MeV`、250 mm 时的 `εc≈1.9%`（相对 76×76 mm NaI），其 `F` 约为典型三 Ge(Li) polarimeter 的 `1.5` 倍；F 对 threshold 近似不变，因为 Q 增益抵消效率损失（PDF pp.467-468，Fig.9）。
5. 在 `158Er` 应用中用配置 C 测量 yrast/side-band γ 线，Table 3 给出 `P(90°)`；ground-band 192、334、443、523、579、608 keV 线约为 `0.36-0.66`，938 keV 线约 `0.10`（PDF pp.468-469，Table 3）。

## Summary

这篇方法论文证明了单个八扇区 Ge(Li) 晶体能够通过扇区组合完成 Compton polarimetry。作者把物理偏振 `P`、计数 asymmetry `A`、探测器 sensitivity `Q`、coincidence efficiency 和 figure of merit 分开测量，并用多种已知 E2 线标定 `Q`。配置 B 偏振灵敏度最高，配置 C 效率和综合 F 最好；`158Er` 应用展示了实际高自旋 γ 线偏振测量。所有数值均保留为 1983 装置和几何的响应结果。

## Experimental or Theoretical Setup

- Detector: coaxial Ge(Li), 55 mm diameter/length, 10 mm core, eight outer sectors。
- Calibration range: `0.3-4.4 MeV` sensitivity/efficiency characterization；`158Er` reaction at `84 MeV` `16O` beam。
- Configurations: sector combinations A/B/C；sector threshold default 60 keV。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| S83-1 | 八扇区 Ge(Li) 可作为 Compton polarimeter，测量范围约 `0.3-4.4 MeV`。 | method-result | direct | PDF pp.463-465 | false |
| S83-2 | `A=QP`，`P`、`A` 和 `Q` 分别表示物理偏振、计数不对称和探测器灵敏度。 | method-definition | direct | PDF p.464，式 (1)-(3) | false |
| S83-3 | 配置 B 的 polarization sensitivity 最高；配置 C 的 coincidence efficiency 最高，且 `F=Q²εc` 在 1.33 MeV 约为典型三 Ge(Li) polarimeter 的 1.5 倍。 | detector-result | direct | PDF pp.466-468，Figs.5-9 | false |
| S83-4 | `158Er` application 用配置 C 测得多条 yrast/side-band γ 线的 `P(90°)`。 | experimental-result | direct | PDF pp.468-469，Table 3 | false |

## Nuclear Structure Information

- `158Er` 的偏振值作为高自旋 γ-ray electromagnetic-character 的方法示例；本论文不重建完整 `158Er` 能级或组态解释。
- 该来源的主要可复用内容是 detector response、configuration choice 和 polarimeter calibration，而非 `158Er` 单核素结论。

## Authors' Interpretation

- 作者认为配置 C 由于纳入更多 scatter combinations，具有最好综合 figure of merit；配置 B 更适合追求 polarization sensitivity。
- 1983 设计提高了单晶探测器的几何效率，但 thresholds、sector cross-talk 和 response normalization 仍决定实际性能。

## Model Results

- 不适用；本文为实验装置/方法论文，没有核结构模型计算。

## Competing Interpretations and Limitations

- 扇区间电感/电子串扰可能制造假 coincident sectors；作者通过脉冲形状和 discriminator 前放大约束讨论其影响（PDF pp.465）。
- `P`、`A`、`Q` 和 `F` 依赖 sector geometry、threshold、source distance 和 background，不能把配置 B/C 的数值用于现代 clover 或 tracking array。
- `158Er` 的偏振测量受 reaction alignment、known transition polarization 和 multipolarity assumptions 约束；Table 3 不是独立核结构 proof。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-S83-1 | Core reconstruction | 论文最重要的贡献是把 single segmented crystal 的 sector combinations 变成可校准 polarimeter，并量化 Q/efficiency/F trade-off。 | PDF pp.463-468 | self-checking |
| AR-S83-2 | Assumptions and dependencies | 依赖 Compton event selection、sector cross-talk control、unpolarized efficiency factor `a` 和 known-P calibration lines。 | PDF pp.464-467 | self-checking |
| AR-S83-3 | Transfer conditions | 可迁移的是 P/A/Q/F 分层和 calibration logic；数值 response 只能用于同几何/同阈值装置。 | PDF pp.464-468 | provisional |
| AR-S83-4 | Failure conditions | threshold、sector cross-talk、background 或 low efficiency 变化会改变 Q/F 和 polarization uncertainty。 | PDF pp.465-468 | active-L3 |
| AR-S83-5 | Reverse/falsification test | 用 unpolarized source、多个已知 E2/P lines、threshold scan 和 sector cross-talk control 重建 `a(E)`、Q 和 F；若配置间不能保持预期趋势则 calibration model 失效。 | PDF Tables 1-2，Figs.5-9 | candidate-L3 |
| AR-S83-6 | Research-question decision | 作为早期 segmented-Ge polarimetry 的方法锚点接入现有 P/A/Q project，不启动 L4。 | PDF pp.463-469 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已区分物理 `P`、计数 `A`、灵敏度 `Q` 和效率，但缺少单晶扇区 Compton polarimeter 的历史 calibration/efficiency trade-off。
- Effect of this source: `foundational-background` and `methodological-bridge`。
- Reason: 来源为 clover、CdTe 和 tracking-array methods 提供历史 detector-response baseline，同时明确旧装置数值不能迁移。
- Persistence decision: update [[compton-polarimetry]] and [[linear-polarization-asymmetry]] source lists; no standalone `158Er` page。
- Review state: `unreviewed`; method claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[compton-polarimetry]] | 早期单晶分段 Compton polarimeter 的 P/A/Q/F 定义和响应边界。 |
| methodological-bridge | [[linear-polarization-asymmetry]] | sector asymmetry、normalization `a` 和 known-P calibration example。 |
| supports | [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] | 补充现代 clover/tracking polarimeter 之前的 detector-performance lineage。 |

## Human Review Triage

### P0

- S83-P0-1：配置 A/B/C 的 Q、efficiency 和 F 数值只能用于该 1983 结构与 threshold；跨阵列引用必须重新标定。

### P1

- S83-P1-1：`158Er` Table 3 偏振值依赖已知 E2/反应取向条件，不应独立承担新核素 multipolarity 结论。

### P2/P3

- DOI、页码和 detector dimensions 已由 PDF metadata/正文对齐；低风险导航只需在方法项目中回链。

## Extracted Pages

- Nuclei: 不创建 `158Er` 独立页。
- Bands: 不创建。
- Concepts: 关联 physical polarization、Compton scattering、detector response。
- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。

## Non-source Notes and Follow-up

- 下一步：将 S83 的历史 detector-response baseline 与 HS-009/HS-016 等后续 polarimeter sources 比较，追踪 Q/F/threshold 如何演化。
