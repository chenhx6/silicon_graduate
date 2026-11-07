---
type: source
title: "Petrík & Kortelainen 2018：零频 FAM 的空间转动 TV 惯量"
aliases: [Petrik Kortelainen 2018 rotational inertia, FAM rotational NG]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: skimmed
title_original: "Thouless-Valatin rotational moment of inertia from linear response theory"
authors: [Kristian Petrík, Markus Kortelainen]
journal: Physical Review C
year: 2018
volume: "97"
pages: "034321"
doi: 10.1103/PhysRevC.97.034321
arxiv: 1709.08534v1
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.97.034321
citation_key: ""
raw_file: raw/papers/gpt/query/20261108-r2-g39-fam-ng/petrik-2018-thouless-valatin-rotational-inertia-fam.pdf
raw_sha256: 6036ed6c1ccaae0800ce1632ecae0a51e4424613ab93d272f10dab5d5d61bb74
raw_storage_status: archived-local
archive_required: true
nuclei: [166er, 168yb]
reactions: []
experiments: []
models: [skm-star, hfb, fam-qrpa]
observables: [rotational-inertia, induced-current]
methods: [finite-amplitude-method, zero-frequency-response]
tags: [doctoral-foundations, thouless-valatin, pairing, linear-response]
---

# 时间反演不变的静态态，也需要时间奇的动态响应

## Bibliographic Record

Crossref 核题名和 DOI，发表记录为 2018-03-22。
实际 `1709.08534v1` PDF 为 **10 个物理页**，内部 Dated 2021-11-10；
不将内部重生成日期当作作品年份，也不声称本地是出版校样。

## Scope and Reading Depth

- Completed reading_depth: skimmed。
- Covered scope: 摘要与 PDF pp. 4–8 的 FAM 方程、NG 惯量、设置、稀土结果、
  自洽推转对照及诱导电流讨论。
- Not covered: 全文全部方法推导、锕系逐核结果、作者提及的补充计算表、
  原代码和全部电流图数字化。

## Paper Question and Scientific Motivation

把零频 FAM 的 NG 响应用于空间转动惯量，
并考察配对对稀土和锕系惯量/诱导电流的影响。
本项目重点学习 Er/Yb；其它质量区作为原文范围记录，不扩展本任务主线。

## Method and Design Logic

轴对称 HFBTHO、SkM*、体配对、60 MeV 准粒子 cutoff；
各链参照一个核的经验质/中 gap 调配对强度。
虽然静态参考态保留时间反演，FAM 响应仍使用完整时间奇 EDF。
在所用轴对称/simplex 条件下，以 \(J_y=L_y+S_y\) 为外场，
用严格零复频率求响应；它不同于对有限频强度做 Lorentz 展宽。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PK18-1 | FAM 自洽诱导场依赖 X/Y，不能视作固定外场一次求值；NG 惯量由 \(S(J_i;0)=-M_{\rm NG}^{J_i}\) 得到。 | model-result | direct | pp. 4–5, Eqs. (12)–(18) | false |
| PK18-2 | 静态时间反演对称与响应使用完整时间奇项相容。 | model-result | direct | p. 5, Numerical results 设置 | false |
| PK18-3 | 调配对强度会使同链惯量整体移动；无配对计算明显较大，图中为比较而除以 2。这个显示因子不是普适物理倍率。 | model-result | direct | pp. 5–7, Figs. 1–2 和正文 | false |
| PK18-4 | 对 166Er、16 壳共同设置，FAM 给 34.511 MeV⁻¹，自洽推转外推给 34.533 MeV⁻¹；后者不是冻结场 IB。 | model-result | direct | p. 7, independent-calculation 段 | false |
| PK18-5 | 由实验 2⁺ 能量给出的惯量带有转动模型映射，不是实验直接测量三轴 TV 张量；本文计算亦基于轴对称参考态。 | our-inference | contextual | pp. 5–7, Fig. 1 caption、设置与比较 | false |

## Summary

本来源使“静态场”和“运动时的诱导场”有了可实现的计算接口。
FAM 与自洽推转零频极限的对照是方法核验，不是两个独立实验。
从偶偶轴对称参考态移到奇核阻塞/三轴高自旋，需要重新处理对称性和响应，
不能直接沿用本篇结果。

## Competing Interpretations and Limitations

作者的无配对与有配对对照包含参考态和响应的整体改变，
不是只把一个能量分母改小。惯量较大不充分证明流场已成为理想刚体。
局域流线图不能充当新的普适流场拓扑分类。
FAM 的数值自洽也不取消 EDF、配对、基底和近似误差。

## Knowledge Impact and Learning Decision

foundational-background：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]；
methodological-bridge：[[moments-of-inertia]]。
34.511/34.533 只用于共同设置的方法比较，不与其它泛函或基底的数值合并。

## Agent Self-audit Triage

P0：零频、诱导场、轴对称条件和 cranked-HFB/IB 区别已回原文。
P1：不采用 worker 的“配对塌缩必然刚体化 2–3 倍”、固定 δ 或百分比阈值。
P2/P3：当前只读目标范围，citation key 不猜测；补充材料仍未取得。

## Extracted Pages

- 可复用方法与比较合同：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。
- 具体案例、真实表与边界：[[doctoral-r2-inertia-evidence-and-band-reconstruction-20261108]]。
- 当前不另建能带或实验页；本来源中的实核数值与模型条件按上文保留，
  不将理论参数登记成新的测量。
