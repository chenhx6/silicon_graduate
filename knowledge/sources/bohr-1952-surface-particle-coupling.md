---
type: source
title: "Bohr 1952：核表面振动与单粒子运动的耦合原作"
aliases: [Bohr 1952 unified model original, surface oscillations individual nucleons]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: read
title_original: "The Coupling of Nuclear Surface Oscillations to the Motion of Individual Nucleons"
authors: [Aage Bohr]
journal: "Det Kongelige Danske Videnskabernes Selskab, Matematisk-fysiske Meddelelser"
year: 1952
volume: "26"
pages: "no. 14"
doi: ""
language: en
canonical_source: https://gymarkiv.sdu.dk/MFM/kdvs/mfm%2020-29/mfm-26-14.pdf
citation_key: ""
raw_file: raw/papers/gpt/query/20261108-r3-bohr-1952/originals/bohr-1952-mfm26-14.pdf
raw_sha256: aa1abb0377c020ecae64eb7735cf5156988682feb7f06617a8957d7d68ad818d
raw_storage_status: archived-local
archive_required: true
nuclei: []
reactions: []
experiments: []
models: [quadrupole-collective-model, particle-surface-coupling, strong-coupling]
observables: [energy-spectrum, quadrupole-moment]
methods: [collective-coordinate-quantization, angular-momentum-coupling]
tags: [doctoral-foundations, original-history, quadrupole, symmetry]
---

# 振动、转动与单粒子耦合：先看原作者限定了什么

## Bibliographic Record

机构馆藏扫描本，40 个物理页，封面明确卷 26、no.14、1952。
使用南丹麦大学的实际文件；未给它猜配 DOI。
早先未核定的候选 URL 访问失败，不表示原作不可得。

## Scope and Reading Depth

- Completed reading_depth: read。
- Covered scope: pp. 3–39 正文主线；重点核坐标、动能、量子化和对称性、
  单粒子/空穴及强耦合近似。pp. 8、21 的关键公式经页面图像核查，
  其它公式以实际页文本/图辅助，不称全部代数已独立重推。
- Not covered: 所有历史引文原件、全部边界扰动积分、现代实核参数重拟合。
- 扫描文字层有希腊字母/上下标错误；不把 OCR 的单个符号当作原文勘误。

## Paper Question and Scientific Motivation

pp. 3–6 用核四极矩的壳依赖与集体量级说明需要同时考虑粒子和可形变表面，
研究重点是耦合模型、状态分类及近似的条件；不是无条件推广液滴能级。

## Method and Design Logic

先构造小幅表面振动，再将五个四极分量改写成 β、γ 和三个 Euler 角；
随后加入一个核子及其形状依赖作用，讨论弱/强耦合与扰动。
这里的形状—取向分拆有明确坐标和模型前提。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| B52-1 | β、γ与三个角替代五个四极坐标；主轴命名有24重冗余，轴对称处还有连续冗余。 | model-result | direct | pp. 9–11, Eqs. (10)–(17); pp. 19–21 | false |
| B52-2 | 不可压、常密度、无旋流给 \(B_\lambda=\rho_0R_0^5/\lambda\)；作者同时强调可形变性会受壳结构影响。 | model-result | direct | p. 8, Eqs. (4)–(9) 及正文 | false |
| B52-3 | 该单一 B 模型给 \(T_{\rm vib}=\frac B2(\dot\beta^2+\beta^2\dot\gamma^2)\)，及 \({\cal J}_k=4B\beta^2\sin^2(\gamma-2\pi k/3)\)。 | model-result | direct | pp. 12–13, Eqs. (19)–(28) | false |
| B52-4 | 曲坐标量子化引入 \(\beta^4|\sin3\gamma|\) 测度；I=0 的角方程在该模型化为 Legendre 方程。 | model-result | direct | pp. 16–22, Eqs. (43)–(71)，尤p.21 | false |
| B52-5 | 单值纯四极标量波函数的主轴一致性限制 K 和 I；I=1 不存在属于这个集体空间。 | model-result | direct | pp. 19–21, Eqs. (56)–(65) | false |
| B52-6 | 加入粒子后转动能含 \((I_k-j_k)^2/{\cal J}_k\)，一致性条件也同时作用于粒子态，不能把纯表面规则直接套给总态。 | model-result | direct | pp. 25–28, Eqs. (81)–(93) | false |
| B52-7 | 强耦合近似需控制形状涨落与扰动矩阵元/能量分母；作者指出粗估中分离未必很大，近简并也会破坏近似。 | author-interpretation | direct | pp. 31–39, 尤pp.33–34,36–39 | false |

## Summary

原作已经把壳依赖、零点涨落及近似失效纳入论证。
今天使用其坐标、无旋惯量或强耦合式时，应同时保留这些条件；
不能由某个质量数或“经典模型”名称直接指定核的模式。

## Competing Interpretations and Limitations

单粒子固定 j、四极截断及无旋流均是模型选择。
本文的同一 B 不等于现代完整响应张量；表面坐标的轴对称冗余不禁止高K粒子转子能带。
一阶固定空间内 j=1/2 的四极耦合消失，不意味着现实 j=1/2 核不能有形变核芯。
现代的 signature、QRPA、配对准粒子与手征术语不能全部倒写为本文已实现的理论。

## Knowledge Impact and Learning Decision

历史原作与任务推导的区分进入
[[doctoral-r3-quantum-labels-and-model-boundaries-20261108]]。
与 [[bohr-mottelson-1953-collective-individual-original]] 是理论发展依赖，
不是两个独立实验。
R1 的正确 γ 测度/Legendre 控制有本原作入口，不重新运行同义计算。

## Agent Self-audit Triage

P0：原件身份、40页、动能/测度/纯四极空间规则回原页核对。
P1：扫描公式、β与γ约定、实验/示例和现代适用域分别记录；
未据粗略历史估计校准当前实核。
P2/P3：DOI与citation key不猜测，扫描全文不进入公开Git。

## Extracted Pages

- 基础方法与模型边界：[[doctoral-r3-quantum-labels-and-model-boundaries-20261108]]。
- 不从历史模型示例新建核素实验事实或赋予整个核区统一参数。
