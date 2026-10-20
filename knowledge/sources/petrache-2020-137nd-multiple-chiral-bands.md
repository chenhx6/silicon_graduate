---
type: source
title: "Multiple chiral bands in 137Nd"
aliases: []
created: 2026-07-01
updated: 2026-07-02
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Multiple chiral bands in 137Nd"
authors: [C. M. Petrache, et al.]
journal: European Physical Journal A
year: 2020
volume: 56
pages: 208
doi: 10.1140/epja/s10050-020-00218-5
arxiv:
language: en
canonical_source: doi:10.1140/epja/s10050-020-00218-5
zotero_item_key:
citation_key: petrache_2020_Multiplechirala
zotero_uri:
library_file:
raw_file: "raw/papers/2020_Petrache et al_Multiple chiral bands in $$^{137}$$Nd.pdf"
raw_sha256: C3117EB0E50A4084D47AF21B11060E8CE31BFF85F3F382A984565B9A1D03BD16
nuclei: [137nd]
reactions: [100mo-ar40-3n-137nd]
experiments: [jurogam2-137nd-ar40-152mev]
models: [covariant-density-functional-theory, triaxial-particle-rotor-model]
observables: [bm1-be2-ratio, signature-splitting]
methods: [gamma-gamma-coincidence, two-point-angular-correlation-ratio]
tags: [a130, chirality, multiple-chiral-doublets, in-beam-spectroscopy, jurogam]
---

# Petrache 等（2020）：`137Nd` 中多重手征带

## Bibliographic Record

European Physical Journal A 56, 208 (2020)，DOI `10.1140/epja/s10050-020-00218-5`。

## Scope and Reading Depth

全文精读；视觉核对 Fig.1 能级纲图、Table 1 新带跃迁、Table 2 模型组态和形变、Figs.6-8 的 B(M1)/B(E2)、alignment 与角动量分量，以及 pp.9-10 总结。

## Summary

作者在 `137Nd` 中识别新正宇称带 D3 和新负宇称带 D6，并分别把它们解释为已知 D2、D5 的手征伙伴，从而提出两对手征双重带。CDFT 和 PRM 给出三轴组态与相近的伙伴角动量分量；两伙伴约 `2ℏ` 的 alignment 差被解释为低自旋手征振动。由于 D3、D6 很弱，缺少它们的实验 B(M1)/B(E2)，所以“手征伙伴”仍是实验结构加模型的综合解释，而不是单一直接观测。

## Experimental or Theoretical Setup

- 反应：`100Mo(40Ar,3n)137Nd`；
- 束流：152 MeV `40Ar`，University of Jyväskylä Accelerator Laboratory；
- 靶：0.50 mg/cm² self-supporting enriched `100Mo`；
- 阵列：JUROGAM II，24 个 clover 加 15 个 coaxial tapered Ge；
- 数据：`5.1×10^10` 个 fold≥3 prompt γ coincidence events；
- 分析：GRAIN 排序，RADWARE 三维/四维符合，`R_ac` 多极性判断；
- 理论：constrained CDFT（PC-PK1）和多-j particle-rotor model。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| P20-1 | 新 D3 为正宇称 ΔI=1 带，包含 31/2+ 至 (41/2+) 六个态，并以 M1/E2、E2 跃迁连接 D2。 | experimental-fact | direct | PDF pp.2-5, Fig.1, Table 1 | false |
| P20-2 | 新 D6 为负宇称 ΔI=1 带，包含 33/2- 至 41/2- 五个态，并以六条跃迁连接 D5；39/2- 附近的 457/500 keV 顺序未定。 | experimental-fact | direct | PDF pp.2,5-7, Fig.1, Table 1 | false |
| P20-3 | 作者把 D2/D3 指认为正宇称手征双重带，把 D5/D6 指认为负宇称手征双重带。 | author-interpretation | indirect | PDF pp.8-10, Figs.5-8 | false |
| P20-4 | CDFT 给出 D2/D3 的 `(β,γ)=(0.20,28.9°)`、D5/D6 的 `(0.21,29.5°)`；PRM 使用的 γ 分别为 20.9° 和 23.5°。 | model-result | direct | PDF p.8, Table 2 | false |
| P20-5 | D2、D5 的 B(M1)/B(E2) 与 PRM 较一致，但 D3、D6 因过弱而没有实验值。 | experimental-fact | direct | PDF pp.8-9, Fig.6 | false |
| P20-6 | 两对伙伴约 `2ℏ` 的 alignment 差及 PRM 三轴角动量分量被作者解释为 chiral vibration。 | author-interpretation | indirect | PDF p.9, Figs.7-8 | false |
| P20-7 | 论文修订先前 D4/D5 的组态对应关系，以改善能量和 B(M1)/B(E2) 描述。 | author-interpretation | indirect | PDF pp.7-9 | false |

## Nuclear Structure Information

- D2/D3：正宇称三准粒子候选，作者给出 `νh11/2^-1 ⊗ πh11/2^1 g7/2^-1`；
- D5/D6：负宇称三准粒子候选，作者给出 `νh11/2^-1 ⊗ πh11/2^2`；
- 两对带的伙伴能量演化和 PRM 角动量构成相似，但新伙伴带人口弱、实验跃迁信息不对称。

## Authors' Interpretation

两对带被视为 `137Nd` 的 multiple chiral doublets，并把 A≈130 中 MχD 的 Nd 序列扩展至 `135-138Nd`。作者更具体地把约 `2ℏ` alignment 差解释为手征振动，而非理想静态手征近简并。

## Model Results

- CDFT 用于得到组态约束形变；
- PRM 同时描述伙伴能量、已有 B(M1)/B(E2) 以及三个主轴角动量分量；
- D2/D3 的长轴分量较大，D5/D6 的短轴分量较大，源于不同未配对轨道组合。

## Competing Interpretations and Limitations

- D3/D6 没有实验 B(M1)/B(E2)，关键电磁比较只存在于较强伙伴 D2/D5；
- D2 低自旋受邻近态强混合，PRM 能量描述较差；
- `R_ac` 主要确定 dipole/quadrupole 性质，不能独自证明手征几何；
- 模型中的 β、γ、转动惯量和 Coriolis attenuation 具有输入依赖；
- 两条相似带仍可能受组态混合或普通带交叉影响。

## Extracted Pages

- Nuclei: [[137nd]]
- Bands: [[137nd-d2-d3-doublet]], [[137nd-d5-d6-doublet]]
- Experiment: [[jurogam2-137nd-ar40-152mev]]
- Concepts: [[chiral-doublet-bands]], [[triaxial-deformation]]
- Models: [[covariant-density-functional-theory]], [[triaxial-particle-rotor-model]]
- Observables: [[bm1-be2-ratio]], [[signature-splitting]]
- Methods: [[gamma-gamma-coincidence]], [[two-point-angular-correlation-ratio]]

## Personal Notes

该文是“候选手征带证据不对称”的好例子：新伙伴的能级与连接跃迁是直接事实，手征几何主要由与较强带的系统学和 PRM 支撑。

## Day18原件复核纠正：同母态跨带条件比与对齐解释

2026-10-21 的 checkpoint048 原件 self-audit 核读主raw，SHA-256 `c3117eb0e50a4084d47af21b11060e8ce31bff85f3f382a984565b9a1d03bd16`。前文P20-1–7及原有review记录保持；以下新增条目均待审，不能借用前文人工审核状态，不新增实验或课程学分。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| P20-D18-1 | **superseded（2026-10-21）**：旧追加段把退激到强伙伴的E2分支当作弱带内部crossover，因而“抢救Fig.6遗漏实验比值”、与强带2倍/包络/交错比较及“严格恒定2ħ确立机制”结论撤回。五个同母态中心可重标为条件out/out或in/out强度比，见P20-D18-5–9；旧result-035/contract-035不再验证原结论。 | superseded-task-audit | corrected-and-boundary | 本段P20-D18-2–12；旧petrache20-137nd-chiral-result-035及contract-035 | true |
| P20-D18-2 | 原文明确D3/D6因弱而未观测其带内E2 crossover，Fig.6相应面板只绘模型值。Table1虽有同母态的跨带E2，不能因此得到相同物理对象的弱带in-band B(M1)/B(E2)；“缺inE2”是该观测量的readiness边界，不表示其它同母态条件量无意义。 | reported-observable-boundary | direct | PDF p.8正文与Fig.6图注；Table1 PDF pp.4–5 | true |
| P20-D18-3 | Table1脚注b称Iγ已作效率修正，归一到699.4-keV线，并由total projection和gated spectra组合取得。dipole多标M1/E2；p.8实验比值采用δ=0，依据DCO/Rac与pure M1相容，不是逐线测得δ。条件率比需M1分率1/(1+δ²)、纯E2分母及相同母态。 | intensity-and-mixing-contract | direct-and-boundary | PDF p.5 Table1脚注b/c；p.8 Fig.6前正文 | true |
| P20-D18-4 | 旧脚本的9个D2、10个D5是选中配对数，不能称完整的同类带内比值清单。D5的25/2−配对675.4/877.3 keV两枝都连接D1；27/2−的138.7为D5带内、814.6连接D1。高spin另有D3/549.1强度<0.1、D6/1050.3强度≤0.05等限制，不能补成中央观测值。 | branch-role-and-limit-audit | direct-and-boundary | PDF p.2 Fig.1；Table1 PDF pp.4–5，D5/3756.4与3895.6、D3/7101.6、D6/6861.4行 | true |
| P20-D18-5 | D3母态31/2+、Ex=4711.7 keV：601.4线Iγ=0.42(15)→D2的29/2+、Ex=4110.3；1038.2线Iγ=0.22(7)→D2的27/2+、Ex=3673.5。两枝均跨带；δ=0且分母纯E2时，旧d3_raw[0]可重标BM1_out/BE2_out=7.37623 μN²/(e²b²)，不是带内比。 | conditional-same-parent-strength-ratio | derived-and-source-boundary | PDF p.4 Table1 D3 Ei=4711.7；p.2 Fig.1；pp.5/7 decay-out正文 | true |
| P20-D18-6 | D3母态33/2+、Ex=5146.7：435.0线Iγ=0.4(1)→D3的31/2+、Ex=4711.7；1036.4线Iγ=0.45(9)→D2的29/2+、Ex=4110.3。δ=0且分母纯E2时，旧d3_raw[1]可重标BM1_in/BE2_out=8.99725 μN²/(e²b²)；不能与强带in/in比作伙伴同一观测量比较。 | conditional-same-parent-strength-ratio | derived-and-source-boundary | PDF p.4 Table1 D3 Ei=5146.7；p.2 Fig.1；pp.5/7正文 | true |
| P20-D18-7 | D6母态33/2−、Ex=5212.4：699.4线Iγ=0.17(4)→D5的31/2−、Ex=4513.0；1053.0线Iγ=0.14(3)→D5的29/2−、Ex=4159.4。两枝均跨带；δ=0且分母纯E2时，旧d6_raw[0]可重标BM1_out/BE2_out=3.20169 μN²/(e²b²)。 | conditional-same-parent-strength-ratio | derived-and-source-boundary | PDF p.5 Table1 D6 Ei=5212.4；p.2 Fig.1；p.7正文 | true |
| P20-D18-8 | D6母态35/2−、Ex=5522.4：310.0线Iγ=0.19(5)→D6的33/2−、Ex=5212.4；1009.4线Iγ=0.22(8)→D5的31/2−、Ex=4513.0。δ=0且分母纯E2时，旧d6_raw[1]可重标BM1_in/BE2_out=21.16681 μN²/(e²b²)，不新增弱带内部E2观测。 | conditional-same-parent-strength-ratio | derived-and-source-boundary | PDF p.5 Table1 D6 Ei=5522.4；p.2 Fig.1；p.7正文 | true |
| P20-D18-9 | D6母态37/2−、Ex=5904.6：382.2线Iγ=0.17(4)→D6的35/2−、Ex=5522.4；996.1线Iγ=0.38(7)→D5的33/2−、Ex=4908.5。δ=0且分母纯E2时，旧d6_raw[2]可重标BM1_in/BE2_out=5.47521 μN²/(e²b²)。本段五比均为打印中心条件计算，不给新实验CI或宣称交错显著性。 | conditional-same-parent-strength-ratio | derived-and-source-boundary | PDF p.5 Table1 D6 Ei=5904.6；p.2 Fig.1；p.7正文 | true |
| P20-D18-10 | 原文从Fig.7讨论伙伴约2ħ的对齐差，同时列出不同Nilsson轨道占据和/或准粒子诱导惯量差的可能来源，并通过135Nd类比支持手征振动解释。本次未作曲线数字化或恒差拟合；“整个频率严格恒定”“唯一确立振动”“排除静态手征”超出这些证据。 | alignment-observation-and-author-interpretation | direct-and-boundary | PDF pp.8–9正文；p.9 Fig.7及其Harris参考说明 | true |
| P20-D18-11 | Table2须区分CDFT形变与PRM输入：D2/D3分别为(.20,28.9°)/(.20,20.9°)，D5/D6分别为(.21,29.5°)/(.21,23.5°)。PRM角动量分量支持作者几何解释，不是独立测得的三轴几何。 | model-input-and-result-boundary | direct | PDF p.8 Table2；p.9 Fig.8与正文 | true |
| P20-D18-12 | 本次读取十页完整正文主线、两表及全部图注；视觉核PDF2 Fig.1、PDF3–5 Table1、PDF9 Figs.7–8。未数字化Fig.6/7或获得原谱/效率协方差。旧脚本不读取declared raw，固定status=passed；本次只核源与独立中心算术，不重跑旧输出。 | current-source-scope-and-producer-boundary | direct-and-boundary | 主raw PDF pp.1–10；旧035脚本输入/输出主体 | true |

五个条件比使用 k=1.225187e13/1.758366e13 及 R=k(E_E2/MeV)^5/(E_dip/MeV)^3×I_dip/I_E2，在δ=0下计算；它们分别标明in/out，不能替代Fig.6的in/in实验值。旧[合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/petrache20-137nd-chiral-contract-035.json)与[结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/petrache20-137nd-chiral-result-035.json)在原结论用途上标为 **superseded**，保留历史文件，不覆盖或称为新验证。

### Day18新的同母态物理量重标练习

[新合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/parent-branch-exercise-contract-048.json)与[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/parent-branch-exercise-result-048.json)保五个同母态真实能量/强度及终态带。原数字可保为两项out/out和三项in/out的δ0条件量，不能拿作Fig6 in/in。给定δ1/δ2时M1分量只为δ0量的1/2或1/5；共同寿命抵消仍成立，但不认证实际δ或生成CI。程序检查能量闭合和角色，不把这些新条件量当独立实验。
