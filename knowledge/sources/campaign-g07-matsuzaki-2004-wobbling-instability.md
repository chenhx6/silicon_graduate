---
type: source
title: "Matsuzaki & Ohtsubo 2004 - Instability of nuclear wobbling motion and tilted axis rotation"
aliases: [Matsuzaki 2004 wobbling instability, Matsuzaki 2004 PRC 163Lu]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Instability of nuclear wobbling motion and tilted axis rotation"
authors: [Masayuki Matsuzaki, Shin-Ichi Ohtsubo]
journal: Physical Review C
year: 2004
volume: 69
pages: 064317
doi: 10.1103/PhysRevC.69.064317
arxiv: nucl-th/0309082
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.69.064317
citation_key:
zotero_item_key:
zotero_uri:
library_file:
raw_file: raw/papers/gpt/query/20261107-campaign-G07/matsuzaki-2004-wobbling-instability-prc-nucl-th-0309082.pdf
raw_sha256: 0c8d23e8c8fb25fb3cab413447a74654afbbcf66ceeeda24b2212173cb9a154e
archive_required: true
nuclei: [163lu, 162yb, 146gd]
reactions: []
experiments: []
models: [cranked-shell-model, random-phase-approximation, tilted-axis-cranking]
observables: [wobbling-energy, wobbling-frequency, potential-energy-surface]
methods: [rpa-cranking, 3d-tilted-axis-cranking]
tags: [theory-ingest, wobbling, tilted-axis-rotation, triaxial-superdeformation, 163Lu, rpa, tac]
---

# Matsuzaki–Ohtsubo：摆动失稳与倾斜转动的指定模型比较

## Bibliographic Record

PRC69,064317(2004)，DOI10.1103/PhysRevC.69.064317。
本地arXiv:nucl-th/0309082v2标记2004-05-13，共13物理页；
内部Dated字段为December16,2018，不据此重定义版本或冒称出版版逐字对照。

## Scope and Reading Depth

### Covered scope

Worker通读13页；总控回查摘要、模型/结论及PDF9–11、Figs3–6。
比较1D推转+RPA与3D TAC Routhian势面，146Gd指定组态的γ变化、
以及163Lu/162Yb TSD组态的示例。

### Not covered

未恢复作者程序、全网格、完整数值协方差，也未证明此模型对应所有核的普适分岔。
该理论文引用的163Lu实验不是本文独立新采集。

## Key Results

| ID | 指定模型结果 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MO04-1 | 146Gd所用扁椭组态随γ改变，RPA摆动失稳与TAC倾斜最低点出现相联系 | model-result | direct | PDF7–9 Figs1–3、PDF11结论 | false |
| MO04-2 | 对163Lu，固定ε2=.43、γ20°、Δn=Δp=.3MeV、ħωrot=.5MeV，RPA给ħωwob=.185MeV、θwob14.2°、φwob7.6° | model-result | direct | PDF9、Fig5/PDF10 | false |
| MO04-3 | 作者将转动参照系的TSD3/TSD2相对TSD1能量比较与势面软化联系；不是不同自旋原始激发能的任意倍数比较 | author-interpretation | direct | PDF9–10 Fig4及定义 | false |
| MO04-4 | 162Yb的0QP示例有x-y平面倾斜极小，与163Lu的πi13/2准粒子稳定主轴转动相对照 | model-result | direct | PDF10–11 Fig6 | false |

## Summary

这提供了在明确组态与参数下连接小振动和有限倾角解的微观模型例子。
不能由模型软化直接宣称163Lu实验已越过临界点，或所有失稳都唯一成为TiP。

## Competing Interpretations and Limitations

推转Routhian通常含−ω·J；不能将草案+ħωJ项单独当总Hamiltonian。
163Lu/162Yb是相关组态比较，不是已完成的同核全部自由度自洽反事实。
作者指出要更深入理解二声子态需要更复杂多体方法；没有从该文得到统一γ势垒阈值。

## Knowledge Impact and Learning Decision

`supports + bounded model comparison`，关联[[campaign-g07-a160-tsd-kmix-20261107]]。
将“实验声子阶梯”与“模型局部稳定性”分开。

## Agent Self-audit Triage

P0: none identified in original identity/hash。P1：总控收窄所谓全核普适严格超叉分岔，
修正推转项符号与轴约定边界；未核citation_key留空。

## Extracted Pages

13页作者稿；关键模型数字与结论定位如上。
