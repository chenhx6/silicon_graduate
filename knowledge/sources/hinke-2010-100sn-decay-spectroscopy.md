---
type: source
title: "Hinke 2010 博士论文：100Sn 及其衰变谱学"
aliases: [Hinke 2010 100Sn thesis, Spectroscopy of the doubly magic nucleus 100Sn and its decay]
created: 2026-09-05
updated: 2026-09-07
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment
reading_depth: deep-read
title_original: "Spectroscopy of the doubly magic nucleus 100Sn and its decay"
authors: [Christoph B. Hinke]
advisor: [Reiner Krücken, Tobias Lachenmaier]
journal: "Technical University of Munich doctoral dissertation"
year: 2010
volume:
pages: 107
doi:
arxiv:
language: en
canonical_source: "Hinke, Christoph B. Spectroscopy of the doubly magic nucleus 100Sn and its decay[D]. Technical University of Munich, 2010."
zotero_item_key:
citation_key: ""
zotero_uri:
library_file: "raw/papers/degree dissertation/Spectroscopy of the doubly magic nucleus 100Sn and its decay.pdf"
raw_file: "raw/papers/degree dissertation/Spectroscopy of the doubly magic nucleus 100Sn and its decay.pdf"
raw_sha256: "DE8701C318D9C1F973D3F6B3FE8CABEC6D291A19F26059B7B675393C5EDA38D2"
nuclei: [100sn, 100in, 100cd]
reactions: ["124Xe projectile fragmentation on Be at 1 GeV per nucleon"]
experiments: []
models: [shell-model, maximum-likelihood-analysis]
observables: [half-life, beta-endpoint-energy, gamow-teller-strength, gamma-ray-energy]
methods: [decay-spectroscopy, beta-gamma-coincidence, maximum-likelihood-analysis]
tags: [a100, doubly-magic, 100sn, beta-decay, gamow-teller, decay-spectroscopy, phd-thesis]
---

# Hinke 2010：`100Sn` 及其衰变谱学

## Bibliographic Record

Christoph B. Hinke，*Spectroscopy of the doubly magic nucleus 100Sn and its decay*，Technical University of Munich，博士学位论文，2010，107 页。原始 PDF SHA-256 为 `DE8701C318D9C1F973D3F6B3FE8CABEC6D291A19F26059B7B675393C5EDA38D2`。

目录中的旧 `100Sn.pdf` 与本文件 SHA-256 完全相同；本 source 只保留描述性文件名作为 canonical raw path，不重复摄入。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: Abstract、Chapters 1–6、Chapter 7 summary；核对 GSI 2008 projectile-fragmentation setup、SIMBA/RISING、maximum-likelihood half-life analysis、`100In` γ lines、β endpoint、GT strength 和 6+ isomer search。
- Not covered: 参考文献逐篇原文复核、全部 shell-model 计算输入的独立重算。
- Coverage caveats: 样本量很小；`100In` level-scheme scenarios 未被区分，低能 γ lines 的 multipolarity 假设影响 endpoint/strength 解释。

## Paper Question and Scientific Motivation

论文以双幻数、N=Z 的 `100Sn` 为模型核，测量其 β 衰变、`100In` 子核激发态、Gamow–Teller 强度和可能的 6+ isomer，以检验壳模型和 GT quenching（Abstract；Ch.1）。

## Method and Design Logic

`124Xe` 在 1 GeV/u 轰击 Be 产生 `100Sn`，经 GSI FRS 识别后植入高度分段 Si 的 SIMBA，周围 RISING Ge 阵列记录 β-delayed γ。母/子/孙衰变链用 maximum-likelihood analysis 分离，β endpoint 和 `100In` γ 谱据此提取（Chapters 2–5）。

## Key Evidence and Reasoning Chain

1. Event-by-event particle identification 和 implantation correlation 确认 `100Sn`。
2. MLH 使用 mother/daughter/granddaughter/background 的完整衰变链拟合半衰期。
3. β-coincident γ spectrum 给出 `100In` 96、141、436、1297、2048 keV lines。
4. β endpoint 经 annihilation/conversion corrections 得到 `Eβ0`，再结合 half-life 得到 `BGT`。
5. shell-model multiplets 比较和 delayed-γ search 评估 `100In` level scenarios 与 `100Sn` 6+ isomer。

## Summary

在约 70 个 `100Sn` 衰变事件基础上，论文得到 `T1/2=1.16±0.20 s`、`Eβ0=3.29±0.20 MeV` 和 `BGT=9.1(+4.8/-2.3)`。`100In` 观察到 96、141、436、1297、2048 keV γ lines，但统计量不足以区分多个 level-scheme scenarios。对预言的 `100Sn` 6+ isomer 的 delayed γ 搜索没有形成可靠确证；作者认为 3 MeV 附近少数 counts 不能单独归因于 isomeric decay。

## Experimental or Theoretical Setup

- GSI 2008：`124Xe` + Be projectile fragmentation，FRS identification。
- SIMBA 25-layer Si implantation/beta detector；RISING 105 Ge detectors。
- 15 s correlation window、MLH chain fit、β-calorimetry、β-delayed γ spectroscopy。
- shell-model calculations for `100In` proton-hole/neutron-particle multiplets。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| HK10-1 | GSI projectile-fragmentation experiment 用 `124Xe` 1 GeV/u + Be 产生/识别 `100Sn`，SIMBA 植入并由 RISING 记录衰变。 | experimental-fact | direct | single | Abstract；Chs.2–3 | true |
| HK10-2 | MLH 对母、子、孙和背景衰变链联合拟合，得到 `T1/2(100Sn)=1.16±0.20 s`；Table 5.1 将样本分解为约 70 个母核衰变及 daughter/background components。 | experimental-fact + method-formalism | direct | single | Ch.5.1 pp.57–59；Table 5.1 | true |
| HK10-3 | β endpoint 的单终态 MLH 初值为 `3.15±0.20 MeV`；加入 bremsstrahlung/annihilation `+200 keV` 与低能内转换平均沉积 `−59 keV` 后得 `Eβ0=3.29±0.20 MeV`，估计 β+ 约 87%、EC 约 13%。 | experimental-fact + analytical-boundary | direct | single | Ch.5.3 pp.63–66；Fig.5.8 | true |
| HK10-4 | `100In` β-coincident γ spectrum 观察到 96、141、436、1297、2048 keV lines；Table 5.2 给出 6±3、13±4、8±3、7±2.5、4±2 events（约 73 个 `100Sn` decays），低能线在 400 μs gate 内未显示 delayed isomeric character。 | experimental-fact | direct | single | Ch.5.2 pp.59–62；Table 5.2；Fig.5.7 | true |
| HK10-5 | 结合 `100Sn` half-life、endpoint 和 single-channel assumption，论文给出 `BGT=9.1(+4.8/-2.3)`，并称其为 Super Gamow-Teller transition。 | derived-observable + author-interpretation | indirect | single | Ch.6.2 pp.76–79；Ch.7.1 pp.81–82；Eq. (A.8) | true |
| HK10-6 | `100In` 低能态可按 `πg9/2−1⊗νg7/2` 与 `πg9/2−1⊗νd5/2` multiplets 组织；多种 shell-model calculation 预言低位可达的 `1+` 态，但实验数据不能区分完整 scenarios。 | model-result + analytical-boundary | indirect | single | Ch.6.1；Figs.6.1–6.2 | true |
| HK10-7 | 延迟 γ 搜索中 first-25 ns bin 的 3 MeV 附近有 4 counts，但只有在 `Eγ<100 keV` 且 `B(E2)≈40 W.u.` 时概率才合理；对更现实的 `B(E2)≈1 W.u.`，作者认为后续时间窗更可能，故不足以确立 `100Sn` 6+ isomer。 | experimental-criterion + author-interpretation | indirect | single | Ch.5.4 pp.66–68；Fig.5.9 | true |
| HK10-8 | `BGT` 和 endpoint 依赖 single-final-state assumption、MLH model、小样本、bremsstrahlung/annihilation 与 96/141 keV conversion corrections；endpoint analysis 未使用低能 400 keV 以下区段，不能脱离这些条件与 Lubos 2016 结果直接平均。 | analytical-boundary | inferred | multiple-independent | Ch.5.3 pp.63–66；Ch.6.2 pp.76–80 | true |

## Nuclear Structure Information

- `100Sn`：双幻数 N=Z、β+ / EC decay、GT strength、6+ isomer search。
- `100In`：β-delayed γ lines、proton-hole/neutron-particle multiplets 和未区分的 level scenarios。
- `100Cd`：daughter/granddaughter chain，用于 MLH background separation。

## Raw Locator Audit (2026-09-07)

- The endpoint chain is explicit in the PDF: raw MLH fit `3.15±0.20 MeV` (p.64), `+200 keV` bremsstrahlung/annihilation and `−59 keV` conversion correction (pp.64–65), final `3.29±0.20 MeV` (p.65).
- The `BGT` value is derived from the single-transition relation `BGT=3811.5/[f(Z,Q)T1/2]` (Appendix Eq. A.8) using the endpoint and half-life; it is not a direct γ-intensity observable.
- The 6+ isomer claim is a non-confirmation: 4 counts at 3004 keV in the first 25 ns are discussed against timing probability and required `B(E2)` (pp.67–68), not treated as an established line.

## Authors' Interpretation

作者认为 `100Sn` GT decay 极强且未显现明显 quenching，但强调 `BGT` 统计误差仍大；`100In` 的 γ lines 只提供初步 level-scheme clues。

## Model Results

- shell-model multiplet calculations compare `πg9/2−1⊗νg7/2/d5/2` configurations。
- MLH probability-density model separates decay generations and backgrounds。

## Competing Interpretations and Limitations

- `100In` 96/141/436/1297/2048 keV lines 的 branch ordering、multipolarity 和 level scheme 不唯一。
- 6+ isomer 的 delayed-γ candidates 可能是 background/Compton/escape events；未形成 direct evidence。
- `BGT=9.1` 与后续 Lubos `5.26` 来自不同 experiment/sample/analysis，不能静默合并。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-HK10-1 | Core reconstruction | 最稳健贡献是 `100Sn` 小样本 β-decay/γ spectroscopy 与 MLH chain-analysis baseline。 | HK10-1–5 | unreviewed |
| AR-HK10-2 | Assumptions and dependencies | endpoint/BGT 依赖 single-state、conversion、annihilation 和 decay-chain model。 | HK10-3–8 | unreviewed |
| AR-HK10-3 | Transfer conditions | 可作为 `100Sn/100In` 历史 GSI baseline，与 Lubos RIKEN experiment 做 independent comparison。 | HK10-2–8 | unreviewed |
| AR-HK10-4 | Failure conditions | 更高统计、不同 Q-value 或 γγ coincidences 改变 level scenario/BGT 时，既有解释需修订。 | Ch.6–7 | unreviewed |
| AR-HK10-5 | Reverse/falsification test | 对 `100In` 核对 γγ cascade、branching/multipolarity；对 6+ isomer 检查 delayed timing 和 detector response。 | Ch.5.2–5.4 | unreviewed |
| AR-HK10-6 | Research-question decision | 建立 `100Sn` 双实验独立证据链，比较 BGT、Q-value 和 missing low-energy transitions。 | HK10-5–8 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 尚无 `100Sn` 专门 source/nucleus 入口。
- Effect of this source: supports and establishes baseline；同时 limits 小统计、level-scenario 和 isomer claims。
- Reason: 提供双幻数核 GT decay、MLH、implantation/decay spectroscopy 的历史实验基线。
- Persistence decision: 新建 source 和 `100sn` 轻量核素页；与 Lubos 2016 分开记录。
- Review state: 页面 `unreviewed`；HK10-2–8 保留 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[100sn]] | 建立 `100Sn` 衰变和 GT strength 的 GSI baseline。 |
| methodological-bridge | [[lifetime]] | MLH decay-chain lifetime analysis。 |
| competing-interpretation | [[gamow-teller-strength]] | `BGT` 与 model-space/quenching interpretation 需保留假设。 |

## Human Review Triage

### P0

- HK10-2/HK10-5：核对 MLH sample、`T1/2`、`Eβ0`、`BGT` 数值和 single-state assumptions；风险是与 Lubos 2016 数值混合。
- HK10-4/HK10-6：核对 `100In` 五条 γ 线、multipolarity/level-scheme scenario 和“不能区分”边界。
- HK10-7：核对 6+ isomer delayed-γ candidate 的统计和作者否定强度。

### P1

- HK10-1：核对 GSI/FRS/SIMBA/RISING setup 与事件数。
- HK10-8：与 Lubos 2016 做 independent experiment/analysis audit。

### P2/P3

- 补充 `100In`/`100Cd` 页面仅在后续需要时进行。

## Extracted Pages

- Nuclei: [[100sn]]。
- Methods: [[lifetime]]、[[gamma-gamma-coincidence]]。
- Concepts: [[gamow-teller-strength]]。

## Non-source Notes and Follow-up

`100Sn.pdf` 是本文件的同哈希旧文件名，不创建第二个 source；正文引用统一使用描述性文件名。
