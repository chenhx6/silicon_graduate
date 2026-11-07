---
type: source
title: "Hinohara 等 2010：Se 核的 CHFB+LQRPA 形状混合"
aliases: [Hinohara 2010 CHFB LQRPA, Se local QRPA inertial functions]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: skimmed
title_original: "Microscopic description of large-amplitude shape-mixing dynamics with inertial functions derived in local quasiparticle random-phase approximation"
authors: [Nobuo Hinohara, Koichi Sato, Takashi Nakatsukasa, Masayuki Matsuo, Kenichi Matsuyanagi]
journal: Physical Review C
year: 2010
volume: "82"
pages: "064313"
doi: 10.1103/PhysRevC.82.064313
arxiv: 1004.5544v2
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.82.064313
citation_key: ""
raw_file: raw/papers/gpt/query/20261108-r2-g38-lqrpa-light/hinohara-2010-prc82-064313.pdf
raw_sha256: c34f2ff4025e3ec8050caabae83c396f6621a80b4ff5b4bbf92066dbf9d7ed04
raw_storage_status: archived-local
archive_required: true
nuclei: [68se, 70se, 72se]
reactions: []
experiments: []
models: [chfb-lqrpa, ascc, pairing-plus-quadrupole]
observables: [collective-inertia, excitation-energy, be2]
methods: [local-qrpa, collective-quantization]
tags: [doctoral-foundations, shape-mixing, time-odd-fields, pairing]
---

# 轻区形状混合的局域响应，不是给转子加一个常数

## Bibliographic Record

题名和 DOI 由 Crossref 核对；底本 `1004.5544v2` 为 **17 个物理页**。
内部 Dated 2018-11-17 不作为发表年份。worker 初稿的 19 页及
“与出版版完全一致”未得到版本逐字对照支持，已撤回。

## Scope and Reading Depth

- Completed reading_depth: skimmed，有界方法深读。
- Covered scope: pp. 1–8 的科学动机、ASCC 到 CHFB+LQRPA 的近似、
  动能与生成元、P+Q 设置及选模 criterion；关键图值另作定向核查。
- Not covered: 全部 Se 谱学逐点复算、原求解器与网格重放、
  发表版逐字校样及全部有效相互作用附属来源。

## Paper Question and Scientific Motivation

由慢集体坐标/生成元构造五维四极 Hamiltonian，使振动与转动惯量含有运动
诱导的时间奇场。模型应用为 68,70,72Se 的扁椭—长椭混合，
而非这些核全部激发机制的统一计算。

## Method and Design Logic

CHFB+LQRPA 是 ASCC 的实用近似：舍去相应曲率项，并以约束参考态
替代完整 moving-frame 自洽态。每个 β–γ 点的局域模式映射到集体坐标，
再作 Pauli 量子化。实际采用 P+Q 加四极配对、两大壳空间并忽略 Fock，
因此作者在数值部分称 HB。有效电荷为 \(e_n=0.4e,e_p=1.4e\)。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| H10-1 | 其振动动能直接以 Dβγ、Dγγ 为坐标质量元，不能将它们与去掉 β/β² 的 B 函数直接等同。 | model-result | direct | p. 2, Eq. (2); pp. 4–5, 坐标映射 | false |
| H10-2 | CHFB+LQRPA 保留诱导场，但仍有局域与集体空间近似；不能称完整 ASCC 或无近似 TDHFB 解。 | model-result | direct | pp. 3–4, Secs. II B–C | false |
| H10-3 | 作者明确限定：在其 P+Q、HB 和所讨论集体质量中，四极配对产生时间奇贡献；这不是单极配对在任意通道永远没有时间奇效应的定理。 | model-result | direct | p. 6, Sec. III A | false |
| H10-4 | 力参数参照 68Se 的 Skyrme-HFB 极小点形变和配对，另作质量标度；有效电荷处理截断空间外极化。 | model-result | direct | p. 6, Sec. III A | false |
| H10-5 | 二模式选择用较小振动 metric 的判据；大 β 区配对振动可能成为较低模式，因此不能机械选最低两个本征频率。 | model-result | direct | pp. 7–8, Figs. 3–4 及讨论 | false |
| H10-6 | 作者所画 ASCC 路径通过三轴谷而非球形点；它是所选三核及相互作用的模型结果，不是所有形状隧穿的必经路线。 | model-result | direct | pp. 6–7, Fig. 1 及讨论 | false |

## 补核的原图值

PDF13 Fig.10及正文给68Se下行2₁→0₁的CHB+LQRPA值492 e²fm⁴，
引用实验中央值432 e²fm⁴；该处没有列实验误差。
不得把两中央值的接近称为已核的统计一致性，也不把模型结果当作新实测。
Fig.9是沿路径的动力学比较，不能与Fig.10的E2图混淆。

## Summary

本来源解释了惯量如何从局域准粒子响应产生，以及为何配对较弱、模式较密集时，
选择哪个集体坐标本身就是理论输入。形状混合不只由势垒高度决定，
但不能由这个例子直接预言另一核区一定出现质量发散或新的核模式。

## Competing Interpretations and Limitations

相互作用、占据、模式选择、惯量和算符均影响谱；不能把不同模型的成功只归给
一个四极配对项。未进行同一 Hamiltonian 的反事实生产计算，
不采纳 worker 关于 Skyrme 排斥项、IB 伪极点被屏蔽或 A130 固定能量偏差的确定断言。
本文数值惯量增强也不能作为任意 QRPA 核的 TV≥IB 证明。

## Knowledge Impact and Learning Decision

与 [[sato-hinohara-2011-krypton-shape-mixing]] 和
[[washiyama-2024-five-dimensional-improved-inertia]] 建立方法依赖：
由半现实 P+Q 应用到现代 EDF，不计作独立重复实验。
学习结果进入 [[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。

## Agent Self-audit Triage

P0：17 页版本、D/B 坐标因子、近似层次和“present model”限制已直接核对。
P1：初稿数字/实验趋势只在另行原图核实后使用；新颖性、跨区质量峰值和精确反事实
未得到本原作支持。P2/P3：citation key 留空，论文包内代码未执行。

## Extracted Pages

- 可复用方法与比较合同：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。
- 具体案例、真实表与边界：[[doctoral-r2-inertia-evidence-and-band-reconstruction-20261108]]。
- 当前不另建能带或实验页；本来源中的实核数值与模型条件按上文保留，
  不将理论参数登记成新的测量。
