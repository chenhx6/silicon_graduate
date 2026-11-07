---
type: source
title: "β decay of 129Cd and excited states in 129In"
aliases: [Taprogge2015, Taprogge 2015 PRC, 129Cd beta decay]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "β decay of 129Cd and excited states in 129In"
authors: [J. Taprogge, A. Jungclaus, H. Grawe, S. Nishimura, P. Doornenbal, G. Lorusso, G. S. Simpson, P.-A. Söderström, T. Sumikama, Z. Y. Xu, H. Baba, F. Browne, N. Fukuda, R. Gernhäuser, G. Gey, N. Inabe, T. Isobe, H. S. Jung, D. Kameda, G. D. Kim, Y.-K. Kim, I. Kojouharov, T. Kubo, N. Kurz, Y. K. Kwon, Z. Li, H. Sakurai, H. Schaffner, K. Steiger, H. Suzuki, H. Takeda, Zs. Vajta, H. Watanabe, J. Wu, A. Yagi, K. Yoshinaga, G. Benzoni, S. Bönig, K. Y. Chae, L. Coraggio, A. Covello, J.-M. Daugas, F. Drouet, A. Gadea, A. Gargano, S. Ilieva, F. G. Kondev, T. Kröll, G. J. Lane, A. Montaner-Pizá, K. Moschner, D. Mücher, F. Naqvi, M. Niikura, H. Nishibata, A. Odahara, R. Orlandi, Z. Patel, Zs. Podolyák, A. Wendt]
journal: "Physical Review C"
year: 2015
volume: 91
pages: 054324
doi: "10.1103/PhysRevC.91.054324"
language: en
canonical_source: "doi:10.1103/PhysRevC.91.054324"
citation_key:
raw_file: "raw/papers/gpt/query/20261107-campaign-G09/Taprogge_2015_PRC_91_054324_AAM.pdf"
raw_sha256: 7502ca1b2b53c2ae990ba4c505060d0265f8edac57b64727ff02ca86f3f6775d
archive_required: true
nuclei: [129cd, 129in, 132sn, 128cd, 130cd]
reactions: [238u-in-flight-fission]
experiments: [riken-ribf-eurica-was3abi]
models: [shell-model, v-low-k, cd-bonn, oxbash]
observables: [beta-decay-half-life, beta-feeding-intensity, log-ft, gamma-ray-energy, level-energy, gamow-teller-strength]
methods: [beta-decay-spectroscopy, beta-gamma-coincidence, isomer-tagged-decay, hpge-cluster-array, was3abi-stopper]
tags: [isomer-beta-decay, gamow-teller, first-forbidden, 129cd, 129in, sn132-neighborhood, phase-space, configuration-fragmentation]
---

# Taprogge2015：129Cd两个β母态的寿命与GT分布

## Bibliographic Record

J. Taprogge et al., PRC91,054324(2015)，DOI10.1103/PhysRevC.91.054324。
本地实际11页AAM；作者稿定位按物理页，不和出版排版页码混用。

## Scope and Reading Depth

### Covered scope

11页主线、能级与β门时间、TableII和OXBASH/GT讨论；
总控回查PDF7寿命、PDF8强度表、PDF9淬灭参数段。

### Not covered

事件级数据、完整feeding/拟合Cov和作者波函数未取得；
没有独立量化两体弱流，不宣称全GT总强度已观测。

## Key Results

| ID | 原文内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TP15-1 | γ门时间拟合得11/2−母态T1/2=155(3)ms、3/2+母态146(8)ms，作者称误差内相容 | experimental-fact | direct | PDF7 Fig6及讨论 | false |
| TP15-2 | 129In逐态β馈送/logft与多个暂定Jπ见TableII；高、低自旋母态的GT分布有集中/碎裂差异 | experimental-fact + author-interpretation | direct | PDF8 TableII；PDF9–10 Fig8 | false |
| TP15-3 | OXBASH计算采用GT矩阵元的.75因子；这不是本实验从每个母态独立提取的通用gA | model-result | direct | PDF9理论段 | false |
| TP15-4 | 模型空间对绝对强度的描述仍有局限，文中讨论未包含完整N=4质子空间的影响 | model-result + author-interpretation | direct | PDF9–10 Fig8与邻段 | false |

## Summary

相近总寿命并不要求相同的GT分布或相同组态。
谱学母态选择、Q窗口和允许/禁戒算符必须先确定，才能讨论有效gA。

## Competing Interpretations and Limitations

不能仅凭logft数值把全部支路划为first-forbidden；需要初末自旋宇称和算符。
反之，宇称改变的支路不能直接当纯允许GT来提取淬灭。
本文中允许GT和禁戒支路、假定母态布居比例及未见feeding处理都有模型/实验依赖。
相近半衰期不证明两母态Q值、f0或每个矩阵元严格相同。

## Knowledge Impact and Learning Decision

`supports + focused L3 comparison`：[[campaign-g09-shell-weak-isomer-20261107]]。
不同方法的In质量测量为组态能量输入提供独立约束，不能直接替代β强度。
本页只报告2015版本，不认证当前评价的所有母态排序与寿命。

## Agent Self-audit Triage

P0: none identified in archived AAM identity/hash。
P1：总控撤回worker的相同寿命必等f0、固定20MeV耗尽Ikeda、
单支logft唯一决定算符或有效gA，以及禁戒跃迁“离心势垒”作为唯一抑制解释。

## Extracted Pages

11页AAM；关键直接核查定位PDF7–10。
