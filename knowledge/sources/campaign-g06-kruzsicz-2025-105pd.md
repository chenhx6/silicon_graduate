---
type: source
title: "Negative-parity high-spin structure of 105Pd"
aliases: [Kruzsicz 2025 105Pd, Kruzsicz 2025 high-spin 105Pd]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Negative-parity high-spin structure of 105Pd"
authors: [B. Kruzsicz, D. Sohler, J. Timár, I. Kuti, Q. B. Chen, S. Q. Zhang, J. Meng, P. Joshi, R. Wadsworth, K. Starosta, et al.]
journal: Physical Review C
year: 2025
volume: 112
pages: 064316
doi: 10.1103/l6vg-jfkv
arxiv: 2607.18953
language: en
canonical_source: https://doi.org/10.1103/l6vg-jfkv
citation_key:
zotero_item_key:
zotero_uri:
library_file:
raw_file: raw/papers/gpt/query/20261107-campaign-G06/kruzsicz-2025-105pd-high-spin-structure-arxiv-2607-18953.pdf
raw_sha256: ac8950306991b96a31e6e0bcb0060dfa3b26b86e2d204e412d1bc4924b6526c7
archive_required: true
nuclei: [105pd]
reactions: ["96Zr(13C,4n)105Pd"]
experiments: [euroball-iv-diamant-105pd-51-58mev]
models: [quantum-particle-rotor-model, relativistic-density-functional-theory]
observables: [multipole-mixing-ratio, wobbling-energy, bm1-be2-ratio, interband-e2-strengths]
methods: [gamma-gamma-coincidence, gamma-gamma-gamma-cube, directional-correlation-oriented-states]
tags: [a100, 105pd, wobbling, two-phonon-wobbling, gamma-vibration, euroball-iv, qprm]
---

# Kruzsicz等：105Pd负宇称高自旋带及N4解释检验

## Bibliographic Record

B. Kruzsicz et al., PRC112,064316(2025)，DOI10.1103/l6vg-jfkv。
实际本地版本arXiv:2607.18953v1，14物理页；期刊年与作者稿上传年分别记录。
不是Comment/Reply；本文是扩展谱学研究。

## Scope and Reading Depth

### Covered scope

14页主线、能级网络、DCO/偏振方法和主要QPRM比较；G10回查SecII与SecIV。
本页保留可定位的主要结论，不把全部图点视为已数值重现。

### Not covered

未取得事件级数据、全部门控谱/Cov或作者QPRM生产程序。
文中没有本次直接测得的全套绝对寿命/矩阵元。

## Experiment and Source Independence

51/58-MeV13C+96Zr(4n)，EUROBALL IV与DIAMANT，原文PDF2 SecII。
作者说明部分结果已发表于Refs17/19；其中包括Timár2019。
因此这是既有实验资料的扩展分析，不能把它与2019工作算两份独立新采集。
新谱学信息仍可有价值，资料复用不等于无信息增益。

## Key Results

| ID | 原文报告/解释 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KR25-1 | 建立6条退耦负宇称带N1–N6和强耦合N7；采用DCO/偏振与符合关系约束 | experimental-fact | direct | PDF2–3、Fig1、TableI | false |
| KR25-2 | N4衰变网络主要连接N2，与N3的连接不满足作者预期的两声子图谱；同输入QPRM比较亦不支持N4两声子指认 | experimental-fact + model-result | direct | PDF9–11 SecIV.B | false |
| KR25-3 | 作者以对齐度/分支模式倾向将N4解释为γ振动相关带 | author-interpretation | direct | PDF10–11 SecIV.B | false |
| KR25-4 | 作者在双门谱中未确认另一工作提出的254/300-keV连接，并讨论102Ru/104Pd峰的污染；据此反对该双重摆动方案 | experimental-fact + author-interpretation | direct | PDF11 SecIV.B | false |
| KR25-5 | N7的伙伴搜索与QPRM几何未给本研究支持的手征解释 | model-result + author-interpretation | direct | PDF12–13 SecIV.D/Fig11 | false |

## Summary

新增证据限制的是特定N4两声子/双重摆动指认，并提供替代γ振动解释。
它不证明105Pd不可能存在任何其它多声子带，也不排除整个A≈100的该模式。
一声子N3参考与N4失败分别判断。

## Competing Interpretations and Limitations

N4的γ振动仍是结合谱学与模型的作者解释，绝对E2可进一步区分。
“未在双门中确认”按实际门/响应/污染讨论保存，不能改写为数学上的零强度。
没有本文适用的完整灵敏度模型时，不给所有未来实验的排除范围。

## Knowledge Impact and Learning Decision

`limits + provisional research-note`：[[campaign-g06-a130-wobbling-discrimination-20261107]]。
与[[timar-2019-transverse-wobbling-105pd]]保留同一采集依赖，
与不同实验的解释冲突则逐线核查，不按论文数量投票。

## Agent Self-audit Triage

P0: none identified in original identity/hash。
P1：G10核出采集依赖；总控撤回“全区两声子破产”“双门未见即严格不存在”及
把局部QPRM结果当全部真实组态禁戒的表述。

## Extracted Pages

本地14页作者稿；方法PDF2–3、解释比较PDF9–13是本页重点。
