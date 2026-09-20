---
type: source
title: "Evidence for Multiple Chiral Doublet Bands in 133Ce"
aliases: [Ayangeakaa 2013 133Ce MχD]
created: 2026-07-13
updated: 2026-09-20
status: active
review_status: human-reviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Evidence for Multiple Chiral Doublet Bands in 133Ce"
authors: [A. D. Ayangeakaa, U. Garg, M. D. Anthony, S. Frauendorf, J. T. Matta, B. K. Nayak, D. Patel, Q. B. Chen, S. Q. Zhang, P. W. Zhao, B. Qi, J. Meng, R. V. F. Janssens, M. P. Carpenter, C. J. Chiara, F. G. Kondev, T. Lauritsen, D. Seweryniak, S. Zhu, S. S. Ghugre, R. Palit]
journal: Physical Review Letters
year: 2013
volume: 110
pages: 172504
doi: 10.1103/PhysRevLett.110.172504
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevLett.110.172504
zotero_item_key:
citation_key: ayangeakaa_2013_EvidenceMultiple
zotero_uri:
library_file:
raw_file: "raw/papers/2013_Ayangeakaa et al_Evidence for Multiple Chiral Doublet Bands in Ce 133 2.pdf"
raw_sha256: 91EC60DFA43E7D8748276E18327028D8EABDF6C5047682726B0DA4A656D5E837
alternate_version_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/实验/2013_Ayangeakaa et al_Evidence for Multiple Chiral Doublet Bands in Ce 133 1.pdf"
alternate_version_sha256: 3c5a3d7c543140ee25f7cb09376d5aeee760c8ac50c76edd466a010d610c2d0f
alternate_version_identity: "PRL 110, 172504 electronic reprint; same title/DOI and five-page article"
nuclei: [133ce]
reactions: [116Cd(22Ne,5n)133Ce]
experiments: [atlas-133ce-ne22-112mev]
models: [covariant-density-functional-theory, triaxial-particle-rotor-model]
observables: [dco-ratio, angular-distribution, energy-staggering-parameter, bm1-be2-ratio]
methods: [gamma-gamma-coincidence, dco-ratio, angular-distribution]
tags: [multiple-chiral-doublet, triaxial-shape-coexistence, high-spin-spectroscopy]
---

# Ayangeakaa 等（2013）：`133Ce` 中多个手征双带证据

## Bibliographic Record

*Physical Review Letters* 110 (2013) 172504，DOI `10.1103/PhysRevLett.110.172504`。BibTeX key 由题名与 DOI 唯一匹配为 `ayangeakaa_2013_EvidenceMultiple`。

## Scope and Reading Depth

规范期刊版已全文 deep-read；本批提供的五页电子 reprint was reread end-to-end to audit experiment, Fig.1 level scheme/linking transitions, DCO/angular-distribution assignments, Fig.2 fingerprints, Fig.3/Table I RMF, TPRM input, Coriolis attenuation, lifetime gap and MχD/shape-coexistence attribution. No material claim change was found.

## Summary

论文在同一 `133Ce` 数据集中建立两组候选伙伴带：正宇称 Bands 2–3 与负宇称 Bands 5–6。观测到的带内、crossover 和 linking transitions 以及 DCO/角分布结果用于限定同宇称与多极性；close energies、`S(I)` 和实验 `B(M1)/B(E2)` 趋势构成作者的 chirality fingerprints。constrained triaxial RMF 给出两套三准粒子组态及不同三轴极小，TPRM 以这些形变为输入比较能量和跃迁比。MχD 和 triaxial shape coexistence 是作者结合实验结构与模型得到的解释，不是由某个单一 observable 直接测得。

## Experimental or Theoretical Setup

- 两次 ATLAS 测量均用 112 MeV `22Ne` 束流，通过 `116Cd(22Ne,5n)133Ce` 布居高自旋态。
- Gammasphere 记录四重及以上 prompt gamma coincidences，合计约 `4.1 x 10^9` events；RADWARE 分析。
- DCO ratios 为主要多极性判据；可行处用 angular-distribution analyses 复核。
- constrained triaxial RMF（PK1）提供组态/形变，TPRM 比较能谱和电磁跃迁比。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| A13-1 | 两次实验均通过 112 MeV `116Cd(22Ne,5n)133Ce` 反应，用 Gammasphere 收集四重及以上 prompt coincidences；合并数据约 `4.1 x 10^9` events，并用 RADWARE 分析。 | observed-fact | direct | PDF p.1, experimental paragraph | false |
| A13-2 | 本文显著扩展既有能级纲图；新能级的 spin/parity 主要依据 DCO ratios，并在可行处用 angular-distribution analyses 复核。 | experimental-assignment | direct | PDF p.1, final experimental paragraph; Fig.1 | false |
| A13-3 | 正宇称候选对 Bands 2–3 被延伸至 `33/2+`，新增 crossover 与 linking transitions；带内 `Delta I=1` 和 328/338/391 keV links 被指认为 mixed `M1/E2`，544/615 keV links 为 `E2`，共同支持两带同宇称。 | experimental-assignment | direct | PDF pp.1-2, Fig.1 and paragraph below | false |
| A13-4 | 作者根据相互连接/共同退激结构及 RMF 计算，把 Bands 2–3 指认为 `pi(g7/2)^-1(h11/2)^1 x nu(h11/2)^-1`；这是实验结构与模型联合的 configuration assignment，不是直接测量。 | author-interpretation | direct | PDF p.2, paragraph below Fig.1 | false |
| A13-5 | 负宇称候选对 Bands 5–6 中 Band 6 为新带；其 363/367/442/423/468/491 keV 带内线被指认为 `M1/E2`，711/779 keV links 的 `A2/A0` 分别为 `-0.622(13)`、`-0.7312(32)`，1074/1146 keV links 的 DCO ratios 与 stretched `E2` 相容，从而支持 Band 6 与 Band 5 同为负宇称。 | experimental-assignment | direct | PDF pp.2-3, Fig.1 inset and first paragraph on p.3 | false |
| A13-6 | Fig.2 给出两对带的实验 excitation energies、`S(I)` 与 `B(M1)/B(E2)` ratios；论文明确说明这些带未能进行 lifetime measurements，因此没有获得作者所称的重要 transition-probability 独立确认。 | observed-fact | direct | PDF p.3, Fig.2 caption and paragraph above Fig.2 | false |
| A13-7 | Bands 5–6 的能量间隔约 400 keV 并在较宽自旋区近似恒定；Bands 2–3 约 100 keV。作者结合近恒定 `S(I)` 和相似 `B(M1)/B(E2)` 趋势，将两组解释为 chiral partners。 | author-interpretation | direct | PDF pp.4-5, discussion of Fig.2 | false |
| A13-8 | constrained RMF（PK1）给出 ground-state 三轴且 gamma-soft 的 `(beta2,gamma)=(0.20,11.1 deg)`；states a/b 被分别视为 Bands 2/5 的 bandhead states，计算形变为 `(0.22,17.5 deg)`、`(0.23,15.2 deg)`。这些 bandhead 对应、形变与组态是模型结果。 | model-result | direct | PDF pp.3-4, Fig.3 and Table I | false |
| A13-9 | TPRM 使用 RMF 的 `beta/gamma` 作为输入，转子 moment of inertia 调整到实验能量；Bands 2–3 另用 Coriolis attenuation `xi=0.7`，作者把它联系到低 `j` `g7/2` 轨道混合。 | model-result | direct | PDF pp.4-5, paragraphs below Table I and below Fig.2 | false |
| A13-10 | TPRM 较好再现两对带的能量和总体 `B(M1)/B(E2)` 趋势，但计算没有明显 odd-even staggering，而实验显示小幅 staggering；作者将偏差联系到 vibrational-to-tunneling 演化的细节。 | model-result | direct | PDF pp.4-5, Fig.2 discussion | false |
| A13-11 | 作者把 Bands 5–6 的约 400 keV 间隔和跃迁趋势解释为 chiral vibration，其中 Band 5/6 分别对应 zero-/one-phonon states；该 phonon 标签属于作者/模型解释。 | author-interpretation | direct | PDF p.4, lower half | false |
| A13-12 | 论文将结果称为首个 MχD strong experimental evidence，并认为 RMF+TPRM 支持 `133Ce` 中 triaxial shape coexistence；“first/confirm”均应归于作者结论，不能改写为无条件实验事实。 | author-interpretation | direct | PDF p.1, introduction; p.5, Summary | false |
| A13-13 | 作者指出 transition-probability measurements 曾为同中子素 `135Nd` 的手征带提供重要确认；虽然本实验无法测量寿命，但 `135Nd` 手征带对与 `133Ce` Bands 5–6 具有相同的建议组态，作者以此系统学相似性为手征解释增加可信度。该邻核比较可适当弥补本实验信息缺口，但不替代 `133Ce` 自身的寿命或绝对跃迁强度测量。 | author-interpretation | direct | PDF p.3, paragraph above Fig.2; p.4, discussion of Bands 5–6 | false |

## Nuclear Structure Information

- [[133ce-positive-parity-mchd-pair]]：论文标签 Bands 2–3，候选三准粒子正宇称组态。
- [[133ce-negative-parity-mchd-pair]]：论文标签 Bands 5–6，候选三准粒子负宇称组态。
- 这些 pair-page 名称避免与当前 Wiki 中来源不同、标签语境不同的 `133ce-band-2` 混同。

## Authors' Interpretation

作者综合 linking structures、同宇称指认、close energies、`S(I)`、`B(M1)/B(E2)` 及 RMF+TPRM 比较，将两组带解释为 MχD，并把不同三轴组态联系到 triaxial shape coexistence。

## Model Results

- RMF：组态、势能曲线和 `beta/gamma` 极小。
- TPRM：以 RMF 形变为输入，调整 moment of inertia，并对正宇称对使用 `xi=0.7`；比较能量、`S(I)` 与 `B(M1)/B(E2)`。

## Competing Interpretations and Limitations

- 没有 lifetime measurements；实验 `B(M1)/B(E2)` ratios 不等同于绝对 transition probabilities。
- 作者以同中子素 `135Nd` 中相同建议组态的手征带系统学为补充支持；这是邻核比较，不是 `133Ce` 自身 transition probabilities 的替代。
- 模型未完全再现实验 staggering；moment of inertia 与 Coriolis attenuation 含拟合/现象学输入。
- close energies、`S(I)` 或相似 transition ratios 任一项都不是独立充分判据。
- configuration 和 triaxial shape coexistence 依赖 RMF/TPRM 联合解释。

## Project Relation

作为 [[nuclear-chirality-and-multiple-chiral-doublet-bands]] 中 `133Ce` 支持 MχD 的原始实验 source；与 Meng 2010 理论背景形成联系，但不构成简单“预言已完全证实”的线性关系。

## Human Review Record

- 2026-07-13：用户审核 `A13-1..12` 完毕；明确 states a/b 分别是 Bands 2/5 的 bandhead states，并补入 `135Nd` 同中子素系统学对寿命缺口的有限补充作用（`A13-13`）。

## Extracted Pages

- Nuclei: [[133ce]]
- Bands: [[133ce-positive-parity-mchd-pair]], [[133ce-negative-parity-mchd-pair]]
- Concepts: [[multiple-chiral-doublet-bands]], [[triaxial-shape-coexistence]]
- Methods: [[dco-ratio]], [[angular-distribution]]
- Models: [[covariant-density-functional-theory]], [[triaxial-particle-rotor-model]]
- Project: [[nuclear-chirality-and-multiple-chiral-doublet-bands]]

## Personal Notes

该文是支持方原始实验来源，但其 MχD 与 shape-coexistence 结论必须保留 author/model attribution 和 lifetime gap。

## Alternate-version self-audit (2026-09-20)

- The alternate reprint has the same PRL title, authors, DOI, five-page structure and reported values as the canonical source. It confirms the two candidate pairs (Bands 2–3 and 5–6), the `4.1×10^9` event total, the DCO/angular-distribution assignments, RMF/TPRM parameters and the absence of direct lifetimes.
- It is an exact same-paper version audit, not an independent experiment; the existing human-review record remains limited to the prior page-level scope, while this alternate-version check is Codex self-audit.
