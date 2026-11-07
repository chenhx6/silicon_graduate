---
type: source
title: "Matsuzaki 等 2004：摆动的频率依赖有效惯量"
aliases: [Matsuzaki Shimizu Matsuyanagi 2004 inertia, PRC69 034325]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: skimmed
title_original: "Nuclear moments of inertia and wobbling motions in triaxial superdeformed nuclei"
authors: [Masayuki Matsuzaki, Yoshifumi R. Shimizu, Kenichi Matsuyanagi]
journal: Physical Review C
year: 2004
volume: "69"
pages: "034325"
doi: 10.1103/PhysRevC.69.034325
arxiv: nucl-th/0310052v2
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.69.034325
citation_key: ""
raw_file: raw/papers/gpt/query/20261108-r2-g42-inertia-observables/matsuzaki-2004-nuclear-moments-of-inertia-prc69-034306.pdf
raw_sha256: 9ea9fb2c8b9e73b0352a219ace7efc6182d6b5471b38d32cb96bc539e4aa6bf7
raw_storage_status: archived-local
archive_required: true
nuclei: [163lu, 167lu, 168hf, 174hf]
reactions: []
experiments: []
models: [cranked-shell-model, random-phase-approximation]
observables: [wobbling-energy, effective-inertia, be2]
methods: [rotating-frame-rpa]
tags: [doctoral-foundations, wobbling, alignment, dynamic-response]
---

# 摆动公式里的有效横向惯量，不是沿带 J(2) 差分

## Bibliographic Record

正确 DOI 是 **10.1103/PhysRevC.69.034325**；
034306 属于另一篇核力论文，初稿错配已以 Crossref 记录纠正。
文件名保留 `034306` 的 legacy 字样，**没有更改 PDF 字节或将它当作作品标识**。
实际底本 `nucl-th/0310052v2`，22 个物理页，页边 2004-02-10。
内部 2018 Dated 不作为出版年份。
出版商另有 [[matsuzaki-2004-wobbling-publishers-note]]，
只涉及在线排印，不是物理方程勘误。

## Scope and Reading Depth

- Completed reading_depth: skimmed。
- Covered scope: pp. 1–5 的物理问题、模型和色散式，相关顺排解释，
  pp. 17–18 的 167Lu/168Hf 对照及未再现的 E2；
  对读 1 页 Publisher’s Note。
- Not covered: 全部参数扫描、原程序、全部图点与 RPA 求和规则的独立重放、
  正式出版版逐字/逐式对照。

## Paper Question and Scientific Motivation

作者考察正 γ 形状下的摆动及频率依赖。
Nilsson 形变和配对 gap 是其计算的参数，不是与 EDF 参考态相同的输入合同。
残余作用、旋称选择和 RPA 小振幅条件也不能省略。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| M04-1 | 其色散关系将转动伪模与物理模分开；物理根涉及 \({\cal J}_{y,z}^{\rm eff}(\omega_{\rm wob})\)，需自洽求解频率。 | model-result | direct | pp. 3–4, Eqs. (1)–(12) | false |
| M04-2 | \({\cal J}_x=\langle J_x\rangle/\omega_{\rm rot}\) 是沿主轴的运动学量；横向有效惯量带模式/频率依赖，不等于能谱的 \(J^{(2)}=dJ/d\omega_{\rm rot}\)。 | model-result | direct | pp. 4–5, Eqs. (11)–(12) 及说明 | false |
| M04-3 | 准粒子顺排可改变惯量排序，使指定正 γ 参数下出现稳定摆动解；不是只有一个轨道在任意核都能稳定摆动的唯一机制定理。 | author-interpretation | direct | pp. 1–2,7–8 的顺排讨论 | false |
| M04-4 | 作者承认 Nilsson 速度依赖使 Jx 偏大，横向量的相应修正尚未给出，因此其比值可靠性的主张也带模型假设。 | author-interpretation | direct | p. 5, Eq. (12) 后段 | false |
| M04-5 | 167Lu 示例未再现全部频率数据；相应带间 E2 比值计算低于测量约 2–3 倍，不能只展示定性成功。 | model-result | direct | pp. 17–18, Fig. 9、Sec. III D | false |

## Summary

本来源使“横向有效动态惯量”和“实验沿带动力学惯量”的区别明确化。
公式外观与刚体相同，并不表示其惯量是三个常数。
单带的能量差分可约束选定模型，却不在没有额外限制时唯一给出一般横向响应。

## Competing Interpretations and Limitations

本文的频率依赖既含准粒子、取向及残余响应，也受固定形变/gap 及 Nilsson 近似影响；
不能从 J(2) 相近或一个下降的带间能量唯一判断核芯软性。
刚性有限转子本身也可能非谐，强/弱两量子连接不是无条件的软核分类阈值。
早期 γ 模与高自旋摆动的联系有历史先例，不把本任务重提耦合称为首次发现。

## Knowledge Impact and Learning Decision

methodological-bridge：[[moments-of-inertia]]、
[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。
与既有 [[campaign-g07-matsuzaki-2004-wobbling-instability]] 为不同论文，
后者是 PRC69,064317，不合并 DOI 或原件。

## Agent Self-audit Triage

P0：DOI 错配已消除，legacy 文件名边界写明；
有效横向惯量与 J(2) 的区别已回公式核对。
P1：保留速度依赖问题、167Lu 频率与 E2 偏差及小振幅域。
P2/P3：不把下载的 2002 伴随原件自动晋升为已精读来源；citation key 留空。

## Extracted Pages

- 可复用方法与比较合同：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。
- 具体案例、真实表与边界：[[doctoral-r2-inertia-evidence-and-band-reconstruction-20261108]]。
- 当前不另建能带或实验页；本来源中的实核数值与模型条件按上文保留，
  不将理论参数登记成新的测量。
