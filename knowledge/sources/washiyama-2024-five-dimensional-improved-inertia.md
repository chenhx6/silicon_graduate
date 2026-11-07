---
type: source
title: "Washiyama 等 2024：110Pd 的 FAM-LQRPA 五维集体惯量"
aliases: [Washiyama 2024 improved inertial functions, 110Pd FAM LQRPA]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: read
title_original: "Five-dimensional collective Hamiltonian with improved inertial functions"
authors: [Kouhei Washiyama, Nobuo Hinohara, Takashi Nakatsukasa]
journal: Physical Review C
year: 2024
volume: "109"
pages: L051301
doi: 10.1103/PhysRevC.109.L051301
arxiv: 2403.00214v1
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.109.L051301
citation_key: ""
raw_file: raw/papers/gpt/query/20261108-r2-g43-new-collective-response/washiyama2024-5dch-lqrpa.pdf
raw_sha256: effef84db32ee4729b4400598af831895ad42fbb460eb431159fe53d0a182dc7
raw_storage_status: archived-local
archive_required: true
nuclei: [110pd]
reactions: []
experiments: []
models: [five-dimensional-collective-hamiltonian, skm-star, chfb-lqrpa]
observables: [excitation-energy, be2, collective-inertia]
methods: [finite-amplitude-method, local-qrpa, constrained-hfb]
tags: [doctoral-foundations, time-odd-response, collective-mass, gamma-softness]
---

# 振动质量与转动惯量不共享一个经验增强系数

## Bibliographic Record

出版身份由 Crossref 核对。实际原件 `2403.00214v1` 为 **7 个物理页**，
页边提交 2024-03-01，内部 Dated 2024-03-04；不是出版版逐字校样。
PDF、源码包及题录保存在同目录 manifest；源码不执行。

## Scope and Reading Depth

- Completed reading_depth: read。
- Covered scope: pp. 1–5 的完整正文、Eqs. (1)–(11)、Figs. 1–5；
  总控回读取模、坐标约定、模型设置、增强范围及作者保留的反例。
- Not covered: 原 FAM/5DCH 程序执行、93 点全部数值重放、源码中全部图附件、
  实验数据库的独立更新、出版版与 v1 的逐字差异。

## Paper Question and Scientific Motivation

将早期 P+Q 应用中的 CHFB+LQRPA 扩展到 Skyrme EDF 的 β–γ 平面，
同时改进振动和转动惯量；用 FAM 避免显式构造完整 QRPA 矩阵。
这并不意味着取消 QRPA、绝热集体空间和取模的近似。

## Method and Design Logic

SkM*、体配对、三维 Cartesian 网格；配对强度参照 106Pd 的经验 gap，
实际应用核为 110Pd。β–γ 三角网格包含 93 个形变点。
作者先找实/虚轴的 LQRPA 极点，再用围道积分取得生成元与坐标变换。
选择使 \(W=(D_{\beta\beta}D_{\gamma\gamma}-D_{\beta\gamma}^2)/\beta^2\)
最小的一对候选模式；不是不加选择地永远取最低两个频率。
转动惯量来自零频角动量响应。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| W24-1 | 本文 Dγγ 已包含动能中的 β² 因子，Dβγ 已包含 β 因子；不能将其直接当作另一文献去掉几何因子的 B。 | model-result | direct | p. 2, Eqs. (1)–(3); p. 3, Fig. 2 caption | false |
| W24-2 | 比较对象分别是振动的 perturbative cranking（PC）及转动的 IB；LQRPA 不是只对三条转动惯量乘一个常数。 | model-result | direct | pp. 1–4, 惯量方法和 Results | false |
| W24-3 | 作者报告极小点附近振动质量 LQRPA/PC 为约 1–2，一些局部大质量区超过 3；转动 LQRPA/IB 约 1–1.4，二者的 β–γ 依赖不同。 | model-result | direct | p. 4, Figs. 2–3 的正文讨论 | false |
| W24-4 | 所算弱配对区的振动质量增强较显著，而转动惯量的增强比变小；这是 110Pd 指定计算结果，不是任意核的定理。 | model-result | direct | pp. 3–4, pairing-gap 与惯量讨论 | false |
| W24-5 | LQRPA 压低计算谱并改善总体比较，但 0₂、0₃ 带的 0⁺–2⁺ 间距仍偏大，\(B(E2;2_3^+\to0_2^+)\) 偏小。 | model-result | direct | pp. 4–5, Fig. 4 及解释 | false |
| W24-6 | 两套惯量的 E2 结果相近；作者明确警告，不能把该核中能量较敏感而 E2 较不敏感的结果推广到所有核。 | author-interpretation | direct | p. 4, Fig. 4 讨论末段 | false |

## Summary

本文提供 A≈100 邻近过渡区的真实微观应用，补足早期 Se/Kr 模型与现代 EDF
之间的方法连接。最可复用的增量不是一个更大的统一系数，而是不同方向、不同
坐标和不同响应量具有不同修正；能谱改善也没有消除全部跃迁和激发带偏差。

## Competing Interpretations and Limitations

配对、EDF、坐标选择、取模和势面均进入预测；仅改变惯量的比较能检验该模型的
敏感性，不能将所有剩余偏差唯一归给时间奇场。
局域虚频表示约束态附近的势曲率，不应自动解释为真实实核的不稳定寿命。
Fig. 5 使用特定体积元因子显示波函数，不能把图的颜色直接当成无测度的概率。
作者给出的数百 core-hour 成本属于其机器和设置，不是本任务实际运行成本。

## Knowledge Impact and Learning Decision

supports：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]] 的坐标/响应比较；
limits：把 1.3 等固定因子迁移到所有质量区或所有振动、转动分量。
与早期同研究组方法有依赖，不把 Se/Kr、110Pd 的模型成功计作独立实验重复。

## Agent Self-audit Triage

P0：原件身份、7 页版本、PC/IB 比较对象和 D 的几何因子已核对。
P1：只保留正文明确给出的范围；不采用 worker 未给依据的 0.1–0.3 MeV
偏差范围，不把方法“改进”写成无近似真值。
P2/P3：citation key 留空；取得源码并不等于复现生产计算。

## Extracted Pages

- 可复用方法与比较合同：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。
- 具体案例、真实表与边界：[[doctoral-r2-inertia-evidence-and-band-reconstruction-20261108]]。
- 当前不另建能带或实验页；本来源中的实核数值与模型条件按上文保留，
  不将理论参数登记成新的测量。
