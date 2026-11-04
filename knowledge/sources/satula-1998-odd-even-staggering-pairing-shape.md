---
type: source
title: "Satuła 等 1998：质量奇偶交错中的配对与形变平均场贡献"
aliases: [Satula1998OES]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper
reading_depth: read
title_original: "Odd-Even Staggering of Nuclear Masses: Pairing or Shape Effect?"
authors: ["W. Satuła", "J. Dobaczewski", "W. Nazarewicz"]
year: 1998
arxiv: "nucl-th/9804060v1"
citation_key: satula1998oes
language: en
canonical_source: "https://arxiv.org/abs/nucl-th/9804060v1"
raw_file: "raw/papers/gpt/learning-daily/20261102-odd-even-mass-stencils/satula1998-oes-v1.pdf"
raw_sha256: "0eb0490badeadcf29bcb0e54695ad3ba1a37b37ec7219607d2b0ef7150556a91"
raw_storage_status: archived-local
archive_required: true
tags: [pairing, mass-staggering, mean-field, deformation, evidence-boundary]
---

# 质量奇偶交错：配对与形变平均场须分开

## Bibliographic Record

按本地 arXiv v1 登记。边栏提交日期为 1998-04-23；正文自动排版日期显示
2018-09-04，不把后者当作首次研究年份。未在本轮核验期刊版本及其页码。

## Scope and Reading Depth

读取 PDF 1–4 的正文、公式和图注；PDF 1 已渲染核对式 (1)–(2)。
未对 Fig. 1–4 的曲线作数值读图或数字化；不把图中文字抽取当成图中点值。
`read` 表示这份短文正文的阅读范围，不认证其引用书籍已读完。

## Method and Design Logic

作者以关闭配对的 HF 计算作为对照，讨论形变单粒子能级对质量交错的贡献。
目标是比较质量滤波器的物理内容，而非把所有交错直接归为配对。PDF 1–2。

## Summary

所研究的无配对平均场也贡献质量交错。奇偶中心三点指标和相邻平均的物理内容
须在指定核区、配对强度及平均场变化条件下解释，不采用普适纯配对指认。

## Extracted Pages

PDF 1：式 (1)–(2) 的约定、研究问题和方法，已核图像；PDF 2–4：
正文与图注、近似条件及 N=Z 限制。图中数值点未数字化，排除在数值复核范围外。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SDN-1 | 作者采用负结合能约定，三点式含粒子数奇偶因子；四点式等于相邻三点指标的平均。 | method/formalism | direct | PDF 1, Eqs. (1)–(2) | false |
| SDN-2 | 所研究的无配对 HF 对照仍能产生 OES，说明质量交错并非配对的充分证据。 | model-result | direct | PDF 2, Fig. 1 讨论 | false |
| SDN-3 | 作者在所讨论的轻核模型条件下以奇数粒子中心三点式近似分离配对贡献；该提法附带平均场随粒子数变化较小等近似。 | author-interpretation | direct | PDF 3, Eqs. (5)–(7) 及前后段 | false |
| SDN-4 | N=Z 附近 Wigner 能/质中关联还会贡献质量交错；作者没有用上述简单分离覆盖该问题。 | author-interpretation | direct | PDF 4, 结论后段 | false |

## Competing Interpretations and Limitations

不把关闭配对的 HF 对照当作具有现实配对强度的 HFB 结论。
[[duguet-2001-odd-even-mass-staggering]] 重新考察这一迁移，不能把二者压成
“奇数中心三点式永远最佳”的规则。重复讨论相同质量数据不构成独立实验。

## Analytical Reconstruction

本库使用正结合能 B，因此式 (1)–(2) 的输入符号需反转。
该约定转换及协方差推导见
[[two-neutron-separation-energy-pairing-gaps-and-shell-closures]]。

## Knowledge Impact and Learning Decision

修订旧 Wiki 中“五点公式给出无污染配对隙”的说法；本来源支持检验平均场
污染的必要性，不直接给出 A≈130 高自旋惯量、阻塞百分比或带交叉频率。

## Human Review Triage

P0 self-audit：已将“质量交错等于纯配对”隔离为错误推断，不晋升。
P1：Fig. 1–4 数值、与期刊版对应和目标核质量评价仍待专项核验。
这是 Codex self-audit，无 human-review 事件。
