---
type: source
title: "Sato & Hinohara 2011：Kr 形状混合中的势能与转动竞争"
aliases: [Sato Hinohara 2011 Kr LQRPA, proton-rich krypton shape mixing]
created: 2026-11-08
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: read
title_original: "Shape mixing dynamics in the low-lying states of proton-rich Kr isotopes"
authors: [Koichi Sato, Nobuo Hinohara]
journal: Nuclear Physics A
year: 2011
volume: "849"
pages: "53–71"
doi: 10.1016/j.nuclphysa.2010.11.003
arxiv: 1006.3694v1
language: en
canonical_source: https://doi.org/10.1016/j.nuclphysa.2010.11.003
citation_key: ""
raw_file: raw/papers/gpt/query/20261108-r2-g38-lqrpa-light/sato-2011-npa849-53.pdf
raw_sha256: e6ee1f1c96e44b63588c863627bf81f7657ea5984942947ac07edeab802aed41
raw_storage_status: archived-local
archive_required: true
nuclei: [72kr, 74kr, 76kr]
reactions: []
experiments: []
models: [chfb-lqrpa, pairing-plus-quadrupole, five-dimensional-collective-hamiltonian]
observables: [excitation-energy, be2, quadrupole-moment, rho2-e0]
methods: [local-qrpa, collective-quantization]
tags: [doctoral-foundations, shape-mixing, rotational-localization, pairing]
---

# 势面的最低点没有独自决定 76Kr 的转动态

## Bibliographic Record

出版身份由 Crossref 核对；本地 `1006.3694v1` 为 **29 个物理页**。
出版页范围 53–71 不是这份预印本的物理页数；
不能沿用 worker 的“19 页全文”定位。

## Scope and Reading Depth

- Completed reading_depth: skimmed。
- Covered scope: PDF pp. 1–14 正文方法与主要逐核解释；
  关键谱图 Fig. 6/8 另作原图核查；E0 公式、标定和态对应直接回正文。
- Not covered: 全部 14 幅图逐条数值数字化、完整求解器重放、
  实验矩阵元的重新 CoulEx 拟合和当代评价更新。

## Paper Question and Scientific Motivation

将 CHFB+LQRPA 应用于 72,74,76Kr，用谱、E2、对角四极矩和 E0
比较扁椭—长椭混合及随自旋的局域化。
与 [[hinohara-2010-local-qrpa-shape-mixing]] 共享理论方法和参数化脉络，
不是一次新的独立测量。

## Method and Design Logic

两大壳 P+Q 加四极配对，忽略 Fock；力参照 Skyrme-HFB 极小点作标定与质量标度。
E2 极化电荷 \(\delta e_{\rm pol}=0.834e\) 用
74Kr 的 \(B(E2;2_1^+\to0_1^+)\) 定标，因此该点不作留出验证。
E0 采用最低阶几何关系，而非完整微观半径算符计算。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SH11-1 | 动能 D 的几何约定、体积元和 E2 算符必须配套；图中仅乘 β⁴ 显示波函数，不等于把完整测度省略为物理概率。 | model-result | direct | pp. 4–5, Eqs. (2), (10), (13)–(15); p. 11, 显示方式说明 | false |
| SH11-2 | E2 极化电荷以 74Kr 的 2₁→0₁ 定标；不能声称全部 E2 都是未拟合的纯预测。 | model-result | direct | p. 10, Sec. 2.4 末段 | false |
| SH11-3 | 作者给出的 76Kr 静态绝对极小为扁椭，但计算 2₁、4₁、6₁ 波函数在长椭侧局域；转动响应与势面竞争。 | model-result | direct | pp. 10,13, Figs. 1,12 的讨论 | false |
| SH11-4 | 76Kr 的计算四极矩绝对大小偏小，作者还讨论实验 2₂ 与计算 2₃ 等序列的替代对应；不能只按能量排序自动逐态匹配。 | author-interpretation | direct | pp. 13–14, Sec. 3.3 | false |
| SH11-5 | E0 用 \(3Z\langle\beta^2\rangle/(4\pi)\) 的跃迁矩阵元近似；模型中通常的径向单极矩阵元退化限制了直接微观 E0。 | model-result | direct | p. 9, Eq. (39); p. 14, Sec. 3.4 | false |
| SH11-6 | 72Kr 的 LQRPA 谱较 IB 压低且总体改善；作者明确指出 2₁⁺ 是相符程度的例外，不能写“所有能级精确重现”。 | model-result | direct | p. 11, Fig. 6 讨论 | false |
| SH11-7 | 74Kr 的大 \(B(E2;0_3^+\to2_1^+)\) 未被再现；激发 0⁺ 结构对 β/大振幅 γ 混合敏感。 | model-result | direct | p. 14, Sec. 3.4 | false |

## Summary

本例使“静态极小点不等于全部转动态形状”成为具体模型比较，
同时保留了有效电荷标定、E0 算符近似、谱学偏差及替代态对应。
它支持跨区核查势—惯量竞争，不能独自确定其它核的混合概率或质量函数。

## Competing Interpretations and Limitations

形状分布、配对、有效相互作用、算符和状态映射共同影响结果。
实验输入与 R1 的 Kr CoulEx 来源有依赖；不将同一 E2 反复引用计作多份证据。
“形状共存增强”与“γ 振动/大振幅涨落”是作者结合波函数和跃迁作的解释，
不由低 0⁺ 能量一个数唯一决定。

## Knowledge Impact and Learning Decision

supports：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]] 的势—响应合同；
limits：将拟合 E2 当盲测、将静态极小点直接赋给整个基态带、
将 E0 称完全微观且无模型的配对探针。

## Agent Self-audit Triage

P0：29 页身份、极化电荷拟合点、E0 近似及 76Kr 态对应已核。
P1：原图能量不凭记忆补值；保留 72Kr 的 2₁⁺ 例外与 74Kr 弱点。
P2/P3：不伪造 citation key；未执行原生产计算。

## Extracted Pages

- 可复用方法与比较合同：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。
- 具体案例、真实表与边界：[[doctoral-r2-inertia-evidence-and-band-reconstruction-20261108]]。
- 当前不另建能带或实验页；本来源中的实核数值与模型条件按上文保留，
  不将理论参数登记成新的测量。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"start_page": 1, "end_page": 3, "sections": "首页、§1 引言、§2 方法开头。"}
- {"start_page": 4, "end_page": 10, "sections": "§2.1–2.4 五维哈密顿量、CHFB+LQRPA、E2/E0 算符与数值设定，式 (1)–(41)，以及 §3 势面开头。"}
- {"start_page": 11, "end_page": 18, "sections": "§3 各 Kr 同位素的谱、惯量、波函数及比较，§4 结论、致谢与参考文献 [1]–[41]。"}
- {"start_page": 19, "end_page": 29, "sections": "图注与可辨图字。第 19 页图 1，第 20 页图 2–3，第 21 页图 4–5，第 22 页图 6–7，第 23–29 页依次为图 8–14。"}
- 本次获取的具体覆盖：通读物理第 1–18 页的正文、结论、致谢和书目，并读取第 19–29 页的 14 幅图注及可辨图字。可接受既有 Wiki 同版第 1–14 页的 skimmed 文字覆盖。比较注所提图 6、8 原图核查未在本次复核，既有范围不升级为全件或视觉覆盖。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | 在 ⁷²Kr 的计算中，作者报告图示的两个对角振动惯量及三个转动惯量的 LQRPA/IB 比值随形变而变且大于 1。改用 LQRPA 惯量后谱能量较 IB 结果降低，整体更接近实验，2₁⁺ 为相符程度的例外。 | model-result | source-reported | 物理第 7–8 页式 (24)–(30)，第 11 页 §3、§3.1。比值图在第 20–21 页图 3、5，谱图在第 22 页图 6，图中数值和连线待核对应原页。 | true |
| A20-2 | E2 极化电荷取 0.834e，以 ⁷⁴Kr 的实验 B(E2; 2₁⁺→0₁⁺) 定标。作者指出计算未再现同核较大的 B(E2; 0₃⁺→2₁⁺)。 | model-calibration-and-comparison | source-reported | 物理第 10 页 §2.4 末段、第 14 页 §3.4。第 23 页图 8 的跃迁标签、方向及数值待核原图。 | true |
| A20-3 | ⁷⁶Kr 的计算势面绝对极小在扁椭侧，计算的 2₁⁺、4₁⁺、6₁⁺ 振动波函数却在长椭侧局域。作者将此解释为转动效应随自旋增加而超过静态势面偏好。 | model-result-and-interpretation | source-reported | 物理第 10 页 §3、第 13 页 §3.3。势面在第 19 页图 1(c)，波函数在第 27 页图 12，等值线和态标签待核原图。 | true |
| A20-4 | E0 用同自旋初末态之间的最低阶 β² 跃迁矩阵元乘以 3Z/(4π) 近似。作者报告算得的 ρ²(E0) 在 A＝74 达峰，并将其与既有实验和 GCM(GOA) 结果比较。 | model-result | source-reported | 物理第 9 页式 (39)、第 14 页 §3.4、第 29 页图 14。点位、误差和图例待核第 29 页原图。 | true |

本篇为理论计算。两大壳 P+Q 模型含四极配对并省略 Fock 项，保留的时奇场贡献依赖该相互作用。LQRPA 方法依赖 [22]，⁷²Kr 参数继承 [18] 对 Skyrme-HFB 极小点的匹配。实验谱和 E2 比较沿用 [4]、[6]–[8]，E0 图沿用 [3]、[4]，与 Wiki 的 Kr CoulEx 来源共享的输入只计一次。

- 沿用比较注对旧记录的修正。本地阅读定位用 29 个物理页，期刊 53–71 页及 2011 年单列为同作出版信息。首页的 2022 年页脚日期保留为原样版本证据，不能覆盖 arXiv v1 标记。
- 将 Wiki 的 E0 公式文字明确为同自旋初末态之间的非对角 β² 跃迁矩阵元。图 14 的 ρ²(E0) 登记为跃迁强度。物理第 9 页式 (39) 的 K 求和指标和测度排版待核原页。
- 物理第 4 页式 (6)–(7) 的根号和括号层次、第 5 页式 (12) 的 Wigner D 下标、第 9 页式 (36)–(37) 的相位及指标在抽取中错位，逐式转录前核对原页。图 1–14 的图注均可定位，物理第 19–27 页的部分轴标、等值线或谱箭头标签抽取错序，不据此补配图中数值。
- 物理第 16 页 [9] 的卷号未见于抽取，回查该页后再登记。物理第 17 页 [23] 的 Nulcear Structure 规范为 Nuclear Structure。
