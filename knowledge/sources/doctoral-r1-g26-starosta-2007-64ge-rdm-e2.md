---
type: source
title: Starosta等2007：64Ge反冲距离法寿命测定与伽马软非谐振动解释
aliases: [Starosta 2007 64Ge RDM E2, Starosta 2007 PRL, 10.1103/PhysRevLett.99.042503]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: 'Shape and Structure of N=Z 64Ge: Electromagnetic Transition Rates from the Application of the Recoil Distance Method to a Knockout Reaction'
authors: [K. Starosta, A. Dewald, A. Dunomes, P. Adrich, A. M. Amthor, T. Baumann, D. Bazin, M. Bowen, B. A. Brown, A. Chester, A. Gade, D. Galaviz, T. Glasmacher, T. Ginter, M. Hausmann, M. Horoi, J. Jolie, B. Melon, D. Miller, V. Moeller, R. P. Norris, T. Pissulla, M. Portillo, W. Rother, Y. Shimbara, A. Stolz, C. Vaman, P. Voss, D. Weisshaar, V. Zelevinsky]
journal: Physical Review Letters
year: 2007
volume: 99
pages: '042503'
doi: 10.1103/PhysRevLett.99.042503
arxiv: nucl-ex/0703021v1
language: en
canonical_source: https://doi.org/10.1103/PhysRevLett.99.042503
zotero_item_key: null
citation_key: ''
zotero_uri: null
library_file: null
raw_file: raw/papers/gpt/query/20261108-foundations-G26/starosta-2007-64ge-rdm-e2.pdf
raw_sha256: 715a4c8ada9a6e4bcc2be1df8c845e680d81b6f0c4f91bf70931fe7b10592ad8
nuclei: [64Ge, 62Zn]
reactions: ['natC(65Ge,64Ge) neutron knockout', 'natC(63Zn,62Zn) neutron knockout']
experiments: [NSCL-A1900-S800-SeGA-Plunger]
models: [GXPF1A-SM, quartic-cubic-anharmonic-vibrator, O(5)-symmetry]
observables: [tau, B(E2), Q(2+), R42]
methods: [recoil-distance-method, intermediate-energy-knockout, Doppler-lineshape-analysis]
tags: [triaxiality, gamma-softness, a60, 64ge, n-equals-z, rdm-lifetime, doctoral-foundations]
archive_required: true
---

# Starosta2007：64Ge寿命及非谐集体解释

## Bibliographic Record

K. Starosta等，*Shape and Structure of N=Z 64Ge: Electromagnetic Transition Rates from the Application of the Recoil Distance Method to a Knockout Reaction*，PRL99,042503(2007)，DOI `10.1103/PhysRevLett.99.042503`。
实际底本为四物理页arXiv预印本`nucl-ex/0703021`，不是期刊排版PDF；哈希见frontmatter。

## Scope and Reading Depth

G26读取四页主线；总控独立核PDF2–3的实验/feeding/减速箔处理和Table I。
寿命提取、理论列与实测列已区分；没有原始波形、事件和线形producer。
0₂的1.353MeV与相应跃迁、两个Qs属于th.列，不声称实测该态或测过其寿命。

## Summary

敲出反应配合中能RDM取得64Ge2₁、2₂寿命与绝对E2，对非谐集体解释提供约束。
GXPF1A再现若干强跃迁，但弱2₂→0₁预报明显偏大；反号Qs是待检模型输出。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST07-1 | τ(2₁)=3.3(5)ps、τ(2₂)=8⁺⁴₋₂ps | reported-experiment | direct-original | PDF3 Table I下正文 | false |
| ST07-2 | 三条向下B分别410(60)、620(210)、1.5(5)e²fm⁴，对应2₁→0₁、2₂→2₁、2₂→0₁ | experiment-plus-adopted-branches | direct-original | PDF3 Table I exp.列 | false |
| ST07-3 | GXPF1A用ep=1.5e、en=0.5e；弱跨带B预测14，Qs(2₁)=−18.6、Qs(2₂)=+18.5efm² | model-result | direct-original | PDF3 Table I th.列与正文 | false |
| ST07-4 | 约40%激发来自减速箔反应，64Ge2₂喂居2₁约30%；62Zn检验τ=4.2(7)ps对采用4.2(3)ps | experiment-specific-response | direct-original | PDF3左栏 | false |

原靶为500μm natC，减速箔250μm93Nb，间距0/200/500μm；原来的9Be敲出靶误写已撤回。
实测E(4₁)/E(2₁)约2.28，表中理论约2.13，不能交换二者。

## Competing Interpretations and Limitations

作者讨论非谐大振幅四极运动与反号矩，未直接测量完整γ分布。
N=Z身份、能比或三条E2不独立证明普适γ软势；理论弱跃迁失配应保留。
本文不测高自旋取向，不提供其它轻核的核芯形变输入。

## Extracted Pages

见[[doctoral-r1-g26-a60-collectivity-20261108]]的实验链与迁移合同。

## Agent Self-audit Triage

P0：底本身份、方向、Table I列与靶/箔已核。
P1：0₂、Qs为理论量；未取得原线形代码及全Cov，不声称重放实验。
