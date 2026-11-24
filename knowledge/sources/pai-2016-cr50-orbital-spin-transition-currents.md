---
type: source
title: "Magnetic dipole excitations of 50Cr: orbital/spin interference and transition-current boundary"
aliases: [pai-2016-cr50-orbital-spin-transition-currents]
created: 2026-10-29
updated: 2026-11-22
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Magnetic dipole excitations of 50Cr"
authors: ["H. Pai", "T. Beck", "J. Beller", "R. Beyer", "M. Bhike"]
year: 2016
journal: "Physical Review C"
volume: "93"
article_number: "014318"
pages: "014318"
doi: "10.1103/PhysRevC.93.014318"
citation_key: "pai_2016_50cr-magnetic-dipole"
canonical_source: "Phys. Rev. C 93, 014318 (2016); arXiv:1601.01905v1"
source_url: "https://arxiv.org/abs/1601.01905v1"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/2016-pai-cr50-scissors.pdf"
raw_storage_status: raw-pdf-archived
raw_sha256: "aec3ddaf120312d487c3f3a627323bc7904343c03b7e1ab8f234bb5259fe8ff7"
nuclei: [50Cr]
observables: [B(M1), transition-current, scissors-mode]
methods: [NRF, QRPA, LSSM]
tags: [50Cr, scissors-mode, M1, transition-current, QRPA, spin-orbit-interference]
---

# Magnetic dipole excitations of 50Cr

## Bibliographic Record

H. Pai et al., *Phys. Rev. C* **93**, 014318 (2016), DOI `10.1103/PhysRevC.93.014318`; arXiv `1601.01905v1`. 取得 10 页 PDF，归档至 `raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/2016-pai-cr50-scissors.pdf`，SHA-256: `aec3ddaf120312d487c3f3a627323bc7904343c03b7e1ab8f234bb5259fe8ff7`。

## Scope and Reading Depth

阅读全文 arXiv v1 PDF1–10，涵盖两套光子束测量、宽度与跃迁强度表、QRPA 及大规模壳模型、单粒子组态表、计算流场、对比案例与结论。图示流场未数字化，外引比较实验留给相应来源页。

## Summary

本工作利用核共振荧光（NRF）测量了 $^{50}\text{Cr}$ 中 $3.628\text{ MeV}$ 的低激发 $1^+$ 态，提取了电磁跃迁几率 $B(M1; 0^+ \to 1^+) = 1.113(49)\ \mu_N^2$。微观 Skyrme QRPA 与大规模壳模型计算证实轨道与自旋矩阵元存在显著的相干相长干涉（干涉项占总强度约 $47\%$），跃迁对流场呈现赤道附近质子-中子反相流动的特征。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PA16-1 | NRF 实验指认 50Cr 在 3628.2 keV 处存在强 1+ 激发态，B(M1; 0+ -> 1+) = 1.113(49) muN2。 | measurement-result | direct | p.4, Table I; p.9 | true |
| PA16-2 | 3.628-MeV 态的分支比 B(M1; 1+ -> 2+) / B(M1; 1+ -> 0+) = 1.02(2)，超出轴对称 Alaga 规则预言的 0.5。 | measurement-ratio | derived | p.4 | true |
| PA16-3 | 文中 QRPA 的总、轨道、自旋强度为 1.52、0.60、0.21 \(\mu_N^2\)，相减得该模型的相长交叉项 0.71 \(\mu_N^2\)。壳模型的对应值为 0.826、0.316、0.120，差为 0.390 \(\mu_N^2\)。Table III 的 \(R\) 定义为轨道强度除以自旋强度，表列 2.9 和 2.6。实验栏只给总 M1 强度，两个分量及 \(R\) 为空。 | model-result | derived | p.9 Table III; pp.6–7 | true |
| PA16-4 | QRPA 态主要两准粒子组态为主导的中子 [303]7/2[312]5/2 (69%) 与质子 [312]5/2[321]3/2 (27%)。 | model-structure | derived | p.7 Table II | true |
| PA16-5 | 跃迁对流场为反相的质子-中子流动，同位旋矢量流在赤道附近最强，符合内部流场图像。 | model-analysis | derived | pp.6–7 Fig.8; p.9 | true |

## Competing Interpretations and Limitations

详细平衡换算向下强度为 $B(M1; 1^+ \to 0^+) = 0.371(16)\ \mu_N^2$。跃迁对流场描述的是基态到激发态的非对角跃迁密度，不能与高自旋磁转动中多准粒子态的静态对角电流场混淆；不能将低能集体剪刀模直接等同于高自旋磁转动带。

## Extracted Pages

- [[orbital-scissors-mode-to-high-spin-mr-microscopic-boundary]]
