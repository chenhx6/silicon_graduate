---
type: source
title: "Duguet 等 2001：自洽平均场中三点与五点质量交错的解释边界"
aliases: [Duguet2001OESPart2]
created: 2026-11-02
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper
reading_depth: read
title_original: "Pairing correlations. Part 2: Microscopic analysis of odd-even mass staggering in nuclei."
authors: ["T. Duguet", "P. Bonche", "P.-H. Heenen", "J. Meyer"]
year: 2001
arxiv: "nucl-th/0105050v1"
citation_key: duguet2001oespart2
language: en
canonical_source: "https://arxiv.org/abs/nucl-th/0105050v1"
raw_file: "raw/papers/gpt/learning-daily/20261102-odd-even-mass-stencils/duguet2001-part2-v1.pdf"
raw_sha256: "66f50d1fd31bf328bf5e3931271d982526a9363ca55037480952d1f50019f044"
raw_storage_status: archived-local
archive_required: true
tags: [pairing, mass-staggering, hfb, time-odd-fields, blocking]
---

# 质量滤波器不自动等于自洽配对隙

## Bibliographic Record

本地 arXiv v1 为 41 个物理页，边栏日期 2001-05-21。首页排版日期
2018-10-28 与提交日期分开；未核验期刊终版，不混用终版 locator。

## Scope and Reading Depth

核对首页题名/作者及摘要入口，读取 PDF 2–8（引言、§2.1–2.3 及 §3 开头）。
渲染 PDF 7 核对式 (5)–(7)。PDF 9–41 的计算、表图、完整结论未在本轮读取；
初读止于上述范围。2026-11-27 已对账并补读本地 arXiv v1 全 41 页，实际覆盖与限制见本页末尾的范围复核。

## Method and Design Logic

§2 引入将奇核也按无阻塞、保持时间反演的偶真空计算的 HFBE 参考，
区分平滑能量、阻塞配对损失及时间反演破缺的极化能。PDF 5–6, Eq. (3)。

## Summary

三点和五点差分对平滑背景、阻塞与极化贡献的处理不同；抑制背景与扩大跨核平均
之间存在取舍。选段不足以据此选定任意核区的最佳配对隙提取器。

## Extracted Pages

PDF 2–4 引言及问题框架；PDF 5–8 §2 的参考能量分解、有限差分与适用条件，
PDF 7 已渲染核对式 (5)–(7)。PDF 9–41 未读，不引用其数值图表作为本轮证据。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DBHM-1 | 作者的奇核能量分解含平滑 HFBE、极化能与自洽配对贡献，不能默认 OES 只含其中一项。 | model-result | direct | PDF 5–6, §2.1, Eq. (3) | false |
| DBHM-2 | 三点质量差含平滑能量二阶导数项；五点式是四阶差分，在其能量约定下带有负的奇偶因子。 | method/formalism | direct | PDF 6–7, Eqs. (4)–(7) | false |
| DBHM-3 | 提高差分阶数可抑制平滑背景，却也在更多核之间平均配对加极化贡献；阶数选择须兼顾局域变化。 | author-interpretation | direct | PDF 8, §2.3 | false |
| DBHM-4 | 作者指出，零配对 HF 下的分离不能未经检查用于具有现实配对的情形。 | author-interpretation | direct | PDF 3–4, 引言 | false |

## Competing Interpretations and Limitations

HFBE 是该理论分析中定义的参考，不是可由三到五个实测质量唯一重建的实验量。
壳闭合、N=Z、轻核或形状快速变化会挑战平滑展开；不能把滤波消项当作对这些
机制的实验排除。此处未审阅全文数值比较，暂不作哪一个指标在特定核区最佳的结论。

## Analytical Reconstruction

本库正结合能约定下须令 E=-B 加上线性静质量项；后者被差分消去。
代码的五点算符从式 (7) 转换，四点左平均从
[[book-bohr-mottelson-nuclear-structure]] Eq. (2-92) 和
[[satula-1998-odd-even-staggering-pairing-shape]] Eq. (2) 对账。

## Knowledge Impact and Learning Decision

支持把 `pairgap` 限定为质量交错指标计算及完整质量协方差传播。
撤回“用 Δ(5) 自动给出断对阈值和固定阻塞淬灭百分比”的功能声明。

## Human Review Triage

P0 self-audit：源公式与正结合能符号转换已对账，未把 HFBE 当作直接观测。
P1：全文的配对强度扫描、极化能定量及目标核模型迁移仍开放。
无 human-review 事件。

## 2026-11-27 — 馆藏原件与覆盖核对

在本地 arXiv:nucl-th/0105050v1 中，§2 与式 (3)–(7) 把自洽阻塞能写成 \(S=\Delta+E^{\mathrm{pol}}\)，参照是具有奇平均粒子数、保持时间反演的完全配对 HFB 真空。平滑参考能量的曲率与时间奇极化属于不同贡献。原稿的数值比较使用三点和五点，PDF 7 的 “fourth-order” 对应五点模板。四点可以由相邻三点指标平均得到，是本轮的代数复核。按负结合能 \(E=-B\) 与 \(p=(-1)^N\)，左中心模板为 \(p[E(N+1)-3E(N)+3E(N-1)-E(N-2)]/4\)，它消去二次背景，但仍对 \(\Delta\) 和 \(E^{\mathrm{pol}}\) 使用相同权重。

PDF 10–14 Figs. 2–5 的 Sn 计算与同一质量评价的三点／五点差比较，闭壳附近保留异常。PDF 14–17 Figs. 6–8 的 Ce 结果是形变 HFB 计算，作者指出当时实验质量误差不支持有意义的相同检验。PDF 33–38 Eqs. (14)–(15) 与 Fig. 16 中，在现实配对并远离闭壳时，五点指标通常跟踪局部平均的 \(\Delta+E^{\mathrm{pol}}\)。奇中心三点有时更接近估计的配对隙，原因是负的平滑曲率与正的极化在这些 Ce 算例近似抵消。该抵消依赖相互作用及 Part I 的微扰极化估计，质量差本身不能单独分离两项。
