---
type: source
title: "β decay of 129Cd and excited states in 129In"
aliases: [Taprogge2015, Taprogge 2015 PRC, 129Cd beta decay]
created: 2026-11-07
updated: 2026-11-27
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

## 2026-11-27 — 馆藏原件与覆盖核对

- PDF 第 1–3 页，书目信息、引言、RIBF 实验方法与谱线来源，含第 3 页图 1。
- PDF 第 4–7 页，γ 线强度、符合门、¹²⁹In 能级与半衰期拟合，含第 4 页表 I、第 5 页图 2–3、第 6 页图 4、第 7 页图 5–6。
- PDF 第 8–11 页，逐态 β 馈送和 log ft、壳模型能级及 GT 比较、结论、致谢及参考文献 [1]–[34]，含第 8 页表 II、第 9 页图 7、第 10 页图 8。
- 本次获取的具体覆盖：逐页核读第 1–11 页所给正文、两张表、八幅图的图注与可提取图中文字，以及致谢和参考文献。建议接受既有同版全文文字覆盖，修正页码、母态分配和模型结论的证据标注后，由管理者核验所列关键图。本次未作视觉核验。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A19-1 | 作者依据 γ–γ 符合和相对强度，从 78 条归于 ¹²⁹Cd→¹²⁹In 的 γ 线中将 69 条纳入能级图，报告 31 个激发态，余下 9 条未定位。¹²⁹In 的 1/2⁻ 态由 γ 跃迁网络定在 451(1) keV。 | 实验观察及能级重建 | source-reported | PDF 第 4 页表 I 与星号说明，第 5 页图 3，第 6 页第 III.A.3 节与小结，第 11 页结论。 | true |
| A19-2 | 按作者的母态归属，对子核 γ 线分别设门后得到 ¹²⁹Cd 的 11/2⁻ 态半衰期 155(3) ms、3/2⁺ 态 146(8) ms，两值在实验误差内相容。母核毫秒异能态标签另给出 11/2⁻ 态的 151(15) ms。 | 实验拟合 | source-reported | PDF 第 7 页图 6(a)–(c) 及相邻门控和拟合段，第 8 页首段。门、面板和拟合标值待核第 7 页图 6。 | true |
| A19-3 | 作者由 γ 强度平衡及母态分配得到三条主要馈送。11/2⁻ 母态至 3150 keV 态的 log ft 为 4.2(1)，3/2⁺ 母态至 3184 和 3348 keV 态分别为 4.5(1) 和 4.7(1)。三态的 (13/2⁻)、(5/2⁺)、(5/2⁺) 来自 β 馈送与 γ 支路的联合暂定归属。 | 实验推导及作者归属 | source-reported | PDF 第 4 页表 I、第 5 页图 3、第 8 页表 II 和第 9 页第 IV 节。 | true |
| A19-4 | OXBASH 对 GT 矩阵元采用 0.75 的输入淬灭因子。计算再现了 3/2⁺ 母态相较 11/2⁻ 母态更分散的主要 GT 馈送，同时高估绝对强度。作者将偏差归因于质子空间未包含完整的 N = 4 振子壳。图 8 的实验比较点限于三个暂定自旋态。 | 模型结果及作者解释 | source-reported | PDF 第 9 页第 V 节计算设置，第 10 页图 8 图注及邻段。实验点、计算分布及坐标标记待核第 10 页图 8。 | true |

RIBF 的 ²³⁸U 飞行裂变数据经 BigRIPS 鉴别、WAS3ABi 植入–β 关联和 EURICA γ 探测取得。表 II 的分母态馈送依赖 γ 强度平衡、衰变路径归属及 49(4)% 对 51(4)% 的母态份额估计。LOGFT 采用文献 Qβ = 9330(200) keV，并假定 3/2⁺ 态约在 300 keV。壳模型以 ¹³²Sn 为闭壳核，使用经 Vlow k 重整化及多极部分修正的 CD-Bonn 有效相互作用。

- TP15-1 的数值保留，补注两组子核 γ 门的母态归属及图 6(c) 的独立标签结果。PDF 第 7 页门控正文把 1586.2 keV 线的母能级写为 3384 keV，按第 4 页表 I 中 1586.2 keV 由 3348 keV 态退激至 1762 keV 态的记录，Wiki 引用应取 3348 keV，并核第 7 页原文。
- TP15-2 将第 8 页表 II 的强度推导、第 9 页的母态份额与自旋归属、第 10 页图 8 的模型比较分开标引。图 8 的物理页统一为第 10 页，主要馈送点的核图状态保留待核。
- TP15-3 保留 PDF 第 9 页第 V 节的 0.75，标明它是 GT 矩阵元的计算输入。TP15-4 中完整 N = 4 质子空间缺失与绝对强度高估的关联，定位到第 10 页图 8 邻段并标为作者解释。
- 书目中的 054324 按期刊文章号记录，本地页数单列为 11，并保留 AAM 物理页定位。
