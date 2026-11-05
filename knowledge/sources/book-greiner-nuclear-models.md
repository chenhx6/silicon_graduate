---
type: source
title: "Walter Greiner & Joachim A. Maruhn 1996 - Nuclear Models"
aliases: [Greiner1996, Greiner Nuclear Models, 格莱纳核模型]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "Nuclear Models"
authors: [Walter Greiner, Joachim A. Maruhn]
publisher: "Springer-Verlag Berlin Heidelberg"
year: 1996
citation_key: "greiner_1996_models"
pages: "399"
isbn: "9783540591801"
canonical_source: "W. Greiner and J. A. Maruhn, Nuclear Models, Springer-Verlag (1996)"
library_file: "raw/books/Nuclear Models (Walter Greiner, Joachim A. Maruhn) (Z-Library).pdf"
raw_file: "raw/books/Nuclear Models (Walter Greiner, Joachim A. Maruhn) (Z-Library).pdf"
raw_sha256: "db5e43efaa80877822540bf0caae9be93d54d5499c5df89faae69769e6f77091"
nuclei: []
reactions: []
experiments: []
models: [davydov-filipov-model, rotation-vibration-model, bohr-hamiltonian, interacting-boson-model]
tags: [triaxiality, collective-hamiltonian, triaxial-rotor, e2-branching-ratios, nuclear-deformation]
---

# Walter Greiner & Joachim A. Maruhn 1996 - Nuclear Models

## 专著全貌与学术定位

法兰克福学派理论物理权威教程。全书以极其清晰严整的解析推导著称，系统阐述了原子核集体运动的数学物理表象，特别是**三轴刚性转子模型（Davydov-Filipov 模型）**、Bohr 集体汉密尔顿量、Faessler-Greiner 转动振动模型（Rotation-Vibration Model, RVM）与相互作用玻色子模型（IBM）。

对于三轴核结构研究而言，本书第 6 章提供了求解非轴对称转子本征能量与 $E2$ 跃迁矩阵元最经典的解析代数框架。

## 核心章节精要与理论物理内容

### Chapter 5 & 6: The Asymmetric Rotor Model (Davydov-Filipov Model) (pp. 135–182)
- **Davydov-Filipov 汉密尔顿量**：
  假设原子核在内禀系中具有固定的三轴形变参量 $(\beta, \gamma)$，转动惯量遵循水动力学假定：
  $$\mathcal{J}_k = 4 B \beta^2 \sin^2\left(\gamma - \frac{2\pi}{3} k\right) \quad (k = 1, 2, 3)$$
  转动汉密尔顿量为：
  $$\hat{H} = \sum_{k=1}^3 \frac{\hat{I}_k^2}{2\mathcal{J}_k} = \frac{\hbar^2}{8 B \beta^2} \sum_{k=1}^3 \frac{\hat{I}_k^2}{\sin^2(\gamma - \frac{2\pi}{3} k)}$$
- **$I=2^+$ 态的二重能级分裂**：
  在轴对称转子中，$I=2^+$ 只有一个态；而在三轴转子中，对称性要求波函数为 $D_{MK}^I$ 展开，本征方程给出两个正宇称 $2^+$ 态（$2_1^+$ 和 $2_2^+$）：
  $$E(2_1^+, 2_2^+) = \frac{9 \hbar^2}{4 B \beta^2} \frac{1 \mp \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}{\sin^2(3\gamma)}$$
  - $2_1^+$ 对应基带（Ground band）的 $2^+$ 态；
  - $2_2^+$ 对应反常非对称转动激发的 $2_\gamma^+$ 态。
  两态能量比随 $\gamma$ 的演化为：
  $$\frac{E(2_2^+)}{E(2_1^+)} = \frac{1 + \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}{1 - \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)}}$$
  当 $\gamma \to 0^\circ$ 时，比值趋于无穷大（$\gamma$ 带无限抬升）；当 $\gamma = 30^\circ$ 时，比值降为极小值 $2.0$！这是利用低激发能级比值直接提取原子核三轴非对称角 $\gamma$ 的最经典经验判据。
- **减缩四极跃迁几率比值（$B(E2)$ 检验）**：
  Davydov-Filipov 模型严格预言了 $2_2^+ \to 0_1^+$ 与 $2_2^+ \to 2_1^+$ 的跃迁分支比仅取决于形变角 $\gamma$：
  $$\frac{B(E2; 2_2^+ \to 0_1^+)}{B(E2; 2_2^+ \to 2_1^+)} = \frac{20}{7} \frac{\sin^2(3\gamma)}{9 - 8\sin^2(3\gamma)}$$
  为实验检验原子核是“三轴刚性（Triaxial Rigid）”还是“$\gamma$ 软核（$\gamma$-soft）”提供了基准解析标尺。


## Bibliographic Record

本书完整原著收录于 `book-greiner-nuclear-models.md` 对应原始路径，哈希与元数据已于前置卡固化。


## Scope and Reading Depth

覆盖全书核心章节与关键推导，结合在束谱学需求进行深度研学。


## Summary

提供系统性核结构与实验数据分析理论框架。


## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SRC-1 | 本专著提供了自洽的核理论与实验分析基准。 | model-result | direct | Ch. 1 | false |


## Competing Interpretations and Limitations

唯象模型与微观第一性原理计算在适用范围与截断上存在边界差异。


## Extracted Pages

核心章节已提取并形式化为 Wiki 概念与方法合同。
