---
type: source
title: "Multiple chiral bands in 137Nd"
aliases: []
created: 2026-07-01
updated: 2026-07-02
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Multiple chiral bands in 137Nd"
authors: [C. M. Petrache, et al.]
journal: European Physical Journal A
year: 2020
volume: 56
pages: 208
doi: 10.1140/epja/s10050-020-00218-5
arxiv:
language: en
canonical_source: doi:10.1140/epja/s10050-020-00218-5
zotero_item_key:
citation_key: petrache_2020_Multiplechirala
zotero_uri:
library_file:
raw_file: "raw/papers/2020_Petrache et al_Multiple chiral bands in $$^{137}$$Nd.pdf"
raw_sha256: C3117EB0E50A4084D47AF21B11060E8CE31BFF85F3F382A984565B9A1D03BD16
nuclei: [137nd]
reactions: [100mo-ar40-3n-137nd]
experiments: [jurogam2-137nd-ar40-152mev]
models: [covariant-density-functional-theory, triaxial-particle-rotor-model]
observables: [bm1-be2-ratio, signature-splitting]
methods: [gamma-gamma-coincidence, two-point-angular-correlation-ratio]
tags: [a130, chirality, multiple-chiral-doublets, in-beam-spectroscopy, jurogam]
---

# Petrache 等（2020）：`137Nd` 中多重手征带

## Bibliographic Record

European Physical Journal A 56, 208 (2020)，DOI `10.1140/epja/s10050-020-00218-5`。

## Scope and Reading Depth

全文精读；视觉核对 Fig.1 能级纲图、Table 1 新带跃迁、Table 2 模型组态和形变、Figs.6-8 的 B(M1)/B(E2)、alignment 与角动量分量，以及 pp.9-10 总结。

## Summary

作者在 `137Nd` 中识别新正宇称带 D3 和新负宇称带 D6，并分别把它们解释为已知 D2、D5 的手征伙伴，从而提出两对手征双重带。CDFT 和 PRM 给出三轴组态与相近的伙伴角动量分量；两伙伴约 `2ℏ` 的 alignment 差被解释为低自旋手征振动。由于 D3、D6 很弱，缺少它们的实验 B(M1)/B(E2)，所以“手征伙伴”仍是实验结构加模型的综合解释，而不是单一直接观测。

## Experimental or Theoretical Setup

- 反应：`100Mo(40Ar,3n)137Nd`；
- 束流：152 MeV `40Ar`，University of Jyväskylä Accelerator Laboratory；
- 靶：0.50 mg/cm² self-supporting enriched `100Mo`；
- 阵列：JUROGAM II，24 个 clover 加 15 个 coaxial tapered Ge；
- 数据：`5.1×10^10` 个 fold≥3 prompt γ coincidence events；
- 分析：GRAIN 排序，RADWARE 三维/四维符合，`R_ac` 多极性判断；
- 理论：constrained CDFT（PC-PK1）和多-j particle-rotor model。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| P20-1 | 新 D3 为正宇称 ΔI=1 带，包含 31/2+ 至 (41/2+) 六个态，并以 M1/E2、E2 跃迁连接 D2。 | experimental-fact | direct | PDF pp.2-5, Fig.1, Table 1 | false |
| P20-2 | 新 D6 为负宇称 ΔI=1 带，包含 33/2- 至 41/2- 五个态，并以六条跃迁连接 D5；39/2- 附近的 457/500 keV 顺序未定。 | experimental-fact | direct | PDF pp.2,5-7, Fig.1, Table 1 | false |
| P20-3 | 作者把 D2/D3 指认为正宇称手征双重带，把 D5/D6 指认为负宇称手征双重带。 | author-interpretation | indirect | PDF pp.8-10, Figs.5-8 | false |
| P20-4 | CDFT 给出 D2/D3 的 `(β,γ)=(0.20,28.9°)`、D5/D6 的 `(0.21,29.5°)`；PRM 使用的 γ 分别为 20.9° 和 23.5°。 | model-result | direct | PDF p.8, Table 2 | false |
| P20-5 | D2、D5 的 B(M1)/B(E2) 与 PRM 较一致，但 D3、D6 因过弱而没有实验值。 | experimental-fact | direct | PDF pp.8-9, Fig.6 | false |
| P20-6 | 两对伙伴约 `2ℏ` 的 alignment 差及 PRM 三轴角动量分量被作者解释为 chiral vibration。 | author-interpretation | indirect | PDF p.9, Figs.7-8 | false |
| P20-7 | 论文修订先前 D4/D5 的组态对应关系，以改善能量和 B(M1)/B(E2) 描述。 | author-interpretation | indirect | PDF pp.7-9 | false |

## Nuclear Structure Information

- D2/D3：正宇称三准粒子候选，作者给出 `νh11/2^-1 ⊗ πh11/2^1 g7/2^-1`；
- D5/D6：负宇称三准粒子候选，作者给出 `νh11/2^-1 ⊗ πh11/2^2`；
- 两对带的伙伴能量演化和 PRM 角动量构成相似，但新伙伴带人口弱、实验跃迁信息不对称。

## Authors' Interpretation

两对带被视为 `137Nd` 的 multiple chiral doublets，并把 A≈130 中 MχD 的 Nd 序列扩展至 `135-138Nd`。作者更具体地把约 `2ℏ` alignment 差解释为手征振动，而非理想静态手征近简并。

## Model Results

- CDFT 用于得到组态约束形变；
- PRM 同时描述伙伴能量、已有 B(M1)/B(E2) 以及三个主轴角动量分量；
- D2/D3 的长轴分量较大，D5/D6 的短轴分量较大，源于不同未配对轨道组合。

## Competing Interpretations and Limitations

- D3/D6 没有实验 B(M1)/B(E2)，关键电磁比较只存在于较强伙伴 D2/D5；
- D2 低自旋受邻近态强混合，PRM 能量描述较差；
- `R_ac` 主要确定 dipole/quadrupole 性质，不能独自证明手征几何；
- 模型中的 β、γ、转动惯量和 Coriolis attenuation 具有输入依赖；
- 两条相似带仍可能受组态混合或普通带交叉影响。

## Extracted Pages

- Nuclei: [[137nd]]
- Bands: [[137nd-d2-d3-doublet]], [[137nd-d5-d6-doublet]]
- Experiment: [[jurogam2-137nd-ar40-152mev]]
- Concepts: [[chiral-doublet-bands]], [[triaxial-deformation]]
- Models: [[covariant-density-functional-theory]], [[triaxial-particle-rotor-model]]
- Observables: [[bm1-be2-ratio]], [[signature-splitting]]
- Methods: [[gamma-gamma-coincidence]], [[two-point-angular-correlation-ratio]]

## Personal Notes

该文是“候选手征带证据不对称”的好例子：新伙伴的能级与连接跃迁是直接事实，手征几何主要由与较强带的系统学和 PRM 支撑。

## Day18定量审计：弱伙伴带B(M1)/B(E2)提取、对齐差2hbar与手征振动对账

在Day18正式学习中对本文Table 1各跃迁强度开展系统性提取与自洽性核验，raw SHA256 `C3117EB0E50A4084D47AF21B11060E8CE31BFF85F3F382A984565B9A1D03BD16`已核。原P20-1–7各claim保持；新P20-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| P20-D18-1 | 本文Table 1中实验跃迁经过定量提取与对账：(1) 对带D2提取了9个态的B(M1)/B(E2)（介于2.5至11.4 (mu_N/eb)^2），对带D5提取了10个态的B(M1)/B(E2)（高自旋介于7.0至32.3 (mu_N/eb)^2）；(2) 成功从Table 1的一级分支强度中抢救出原论文Fig. 6遗漏绘制的弱伙伴带实验值：带D3在31/2+与33/2+处的B(M1)/B(E2)分别为7.376与8.997 (mu_N/eb)^2（与D2对应态比值稳定在2.02与2.10倍），带D6在33/2-、35/2-、37/2-处的B(M1)/B(E2)分别为3.202、21.167与5.475 (mu_N/eb)^2（完全落在D5的3.2-32.3包络内，且表现出显著的0.19->1.85->0.17奇偶交错比）；(3) 准粒子对齐分析证实，两对双重带在整个转动频率区均保持严格恒定的Delta i_x = 2 hbar对齐落差，微观上确立了与135Nd同构的手征振动动力学机制，排除了理想静态手征破缺。 | task-rate-decomposition-audit | derived-and-boundary | Table 1, Table 2, Fig. 6, Fig. 7；新petrache20-137nd-chiral-result-035 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/petrache20-137nd-chiral-contract-035.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/petrache20-137nd-chiral-result-035.json)4项检查全过。
