---
type: source
title: "Jouni Suhonen 2007 - From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory"
aliases: [Suhonen2007, Suhonen微观核理论, 从核子到原子核]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory"
authors: [Jouni Suhonen]
publisher: "Springer-Verlag Berlin Heidelberg"
year: 2007
pages: "654"
isbn: "9783540488590"
canonical_source: "J. Suhonen, From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory, Springer (2007)"
library_file: "raw/books/From nucleons to nucleus concepts of microscopic .pdf"
raw_file: "raw/books/From nucleons to nucleus concepts of microscopic .pdf"
raw_sha256: "4d4b799b8d91784638bac29e0749fe08ba9720f067fd76317f7e256d6f8cd27c"
nuclei: []
reactions: []
experiments: []
models: [spherical-shell-model, bcs-quasiparticle, qrpa, sdi, tensor-algebra]
tags: [angular-momentum-coupling, tensor-operators, wigner-eckart-theorem, electromagnetic-transition-operators]
---

# Jouni Suhonen 2007 - From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory

## 专著概况与定位

芬兰于韦斯屈莱大学（Jyväskylä）Jouni Suhonen 教授所著的微观核结构教材，是国际上把**角动量 Racah 代数、球张量算符、Wigner-Eckart 定理与电磁跃迁几率计算**推导得最详尽、最适合作为手算与编程基准的实战宝典。

## 核心章节精要与物理内容

### Chapters 1–4: Angular Momentum & Tensor Operators（张量代数机器）
- **不可约球张量算符**：$[T_k, J_\pm]$ 的对易子关系。
- **Wigner-Eckart 定理的严格相位约定**：
  $$\langle j_f m_f | T_{\lambda \mu} | j_i m_i \rangle = (-1)^{2\lambda} \frac{C_{j_i m_i \lambda \mu}^{j_f m_f}}{\sqrt{2 j_f + 1}} \langle j_f || T_\lambda || j_i \rangle$$
  给出了单粒子与多体初末态约化矩阵元与 Clebsch-Gordan 系数分离的标准相位。

### Chapters 6–7: Electromagnetic Transitions（电磁跃迁微观理论）
- **跃迁几率与约化矩阵元**：
  $$T_{fi}(\sigma\lambda) = \frac{8\pi(\lambda+1)}{\lambda[(2\lambda+1)!!]^2} \frac{k^{2\lambda+1}}{\hbar} B(\sigma\lambda; I_i \to I_f)$$
  $$B(\sigma\lambda; I_i \to I_f) = \frac{1}{2I_i + 1} |\langle I_f || \mathcal{M}(\sigma\lambda) || I_i \rangle|^2$$
- **单粒子电多极与磁多极算符显式表达**：包含轨道磁矩 $g_l$ 与自旋磁矩 $g_s$ 的淬灭（Quenching）效应。

### Chapters 12–19: Quasiparticles, BCS & QRPA（准粒子平均场与组态混合）
- **Bogoliubov-Valatin 变换**：费米子算符向准粒子算符 $a_j^\dagger = u_j c_j^\dagger - v_j \tilde{c}_j$ 映射。
- **表面 $\delta$ 相互作用（Surface Delta Interaction, SDI）**：在紧凑模型空间下精确求解二体剩余相互作用矩阵元。


## Bibliographic Record

本书完整原著收录于 `book-suhonen-from-nucleons-to-nucleus.md` 对应原始路径，哈希与元数据已于前置卡固化。


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
