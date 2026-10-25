---
type: source
title: "Probing the nature of the conjectured low-spin wobbling bands in atomic nuclei"
aliases: [Guo 2022 187Au, low-spin wobbling counter-source, probing low-spin wobbling bands]
created: 2026-07-04
updated: 2026-07-04
status: ai-draft
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Probing the Nature of the Conjectured Low-Spin Wobbling Bands in Atomic Nuclei"
authors: [S. Guo, X. H. Zhou, C. M. Petrache, E. A. Lawrie, S. H. Mthembu, et al.]
journal: Physics Letters B
year: 2022
volume: 828
pages: 137010
doi: 10.1016/j.physletb.2022.137010
arxiv: 2011.14354
language: en
canonical_source: doi:10.1016/j.physletb.2022.137010
zotero_item_key:
citation_key: guo_2022_Probingnature
zotero_uri:
library_file:
raw_file: "raw/papers/2022_Guo et al_Probing the nature of the conjectured low-spin wobbling bands in atomic nuclei3.pdf"
raw_sha256: DE541977E4C8402C905EF8268EBC5707303F4B92F244EB4F59405A70C3473206
nuclei: [187au]
reactions: [175lu-o18-6n-187au]
experiments: [hirfl-187au-o18-108mev]
models: [triaxial-particle-rotor-model]
observables: [multipole-mixing-ratio, interband-e2-strengths]
methods: [gamma-gamma-coincidence, two-point-angular-correlation-ratio, linear-polarization-asymmetry]
tags: [a190, 187au, wobbling-counter-evidence, hirfl, qtr, low-spin-precession]
---

# Guo 等（2022）：`187Au` 低自旋 wobbling 反方实验与重解释

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

S. Guo et al., *Physics Letters B* **828**, 137010 (2022)，DOI `10.1016/j.physletb.2022.137010`，arXiv `2011.14354v3`。题名、作者、年份、DOI 和 arXiv 版本身份一致，使用 citation key `guo_2022_Probingnature`。

## Scope and Reading Depth

主文与 supplementary material 全文精读，并视觉核对主文 Fig.1 的高/低自旋进动几何、Fig.2 的 `187Au/188Pt` 部分能级纲图与门谱、Fig.3 的联合 `P-R_ac` 与内转换比较、Fig.4 的实验-QTR 比较、Fig.5-6 对 mixing-ratio 双解和偏振不确定度的讨论，以及补充材料 pp.1-5 的选门、偏振校准、误差处理和 QTR 波函数分解。

本页按 `experiment-ingest + project-ingest` 建立针对 reported low-spin wobbling bands 的 counter-source/reinterpretation source。它不把 Guo 2022 的反方解释写成本 Wiki 的最终裁决。补充材料作为主论文的附属证据层挂接到本 source，不另建 source、DOI 或 BibTeX 条目。

## Supplementary Material Record

- 文件：`raw/papers/2022_Guo et al_Probing the nature of the conjectured low-spin wobbling bands in atomic nuclei supplement.pdf`
- SHA-256：`8525CAA69D98E808253E3C790430982451F621A01CE4E7F438AB3FE1D836BCD6`
- 证据边界：该文件补充主文的数据分析、计算与评估细节，不具有独立文献身份；所有新增 claims 仍引用 `guo_2022_Probingnature`。

## Summary

作者用 `175Lu(18O,6n)187Au` 的独立实验数据，同时测量 two-point angular-correlation ratio `R_ac` 与 linear polarization `P`，重新约束 Sensharma 2020 所称 longitudinal-wobbling candidate（Band 2）到 Band 1 的两条最低 connecting transitions。本文得到小 `abs(δ)`、M1-dominated 解，并以 QTR 计算把 Bands 1/2 主要联系到 `h9/2` 子壳层的最低与次低单粒子轨道，据此提出 dominant single-particle excitation 重解释。作者还批评把高自旋、小角 harmonic wobbling approximation 外推到低自旋，以及只采用大 `abs(δ)` 解并仅在 wobbling/signature-partner 两种解释间选择的识别范式。

## Experimental or Theoretical Setup

- HIRFL 以 108 MeV `18O` 束流轰击两层各 `0.7 mg/cm²` 的自支撑天然 Lu 靶，经 `175Lu(18O,6n)187Au` 产生目标核；
- 阵列包含 8 个 segmented clover detectors 与 16 个 coaxial HPGe detectors，其中 8 个 HPGe 配 anti-Compton shields；
- clover detectors 位于垂直束流的一个环；16 个 HPGe 分布在相对束流 `26°`、`51°`、`129°`、`154°` 四个环；
- 记录约 `5×10^10` 个 double- or higher-fold events；
- `R_ac` 由 `154°` 与 `90°` 探测器谱强度比获得，gate 使用所有探测器可见跃迁；`P` 由 clover 相邻晶体中垂直/平行方向的 Compton scattering events 获得；
- QTR 采用 one-quasiparticle-plus-triaxial-rotor calculation；详细程序与更多结果指向 supplementary material。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| G22-1 | 实验使用 108 MeV `175Lu(18O,6n)187Au`，靶为两层各 `0.7 mg/cm²` 的自支撑天然 Lu；记录约 `5×10^10` 个 fold≥2 events。 | experimental-fact | direct | p.2, left column, experimental setup | false |
| G22-2 | 阵列由 8 个 segmented clover 和 16 个 coaxial HPGe 构成；clover 位于垂直束流的环，HPGe 位于 `26°/51°/129°/154°` 四环，其中 8 个 HPGe 有 anti-Compton shields。 | experimental-fact | direct | p.2, left column, experimental setup | false |
| G22-3 | 本文确认早期工作的 Bands 1-4，但未观察到 Sensharma 2020 报告的粉色负宇称序列及其 429、437 keV links；能量相近的 265、405、414、551 keV 序列被归入同一反应中产生的 `188Pt`。 | experimental-fact | direct | p.2, Fig.2(a-b) and surrounding text | false |
| G22-4 | 作者进一步以本实验未见该粉色序列、且 Rupnik 等的详细 `187Ag` β-decay study 在观察到大量 `187Au` excited states、覆盖至 `I=19/2` 的情况下仍未见该序列为依据，质疑其属于 `187Au` 的指认。 | author-interpretation | secondary-comparison | p.2, right column, paragraph below Fig.2 | false |
| G22-5 | `187Au` Band 2 为 ΔI=2 sequence，并以若干 ΔI=1 transitions 衰变到 Band 1；本文把 376 与 462 keV 两条最低 links 作为联合 `R_ac-P` 分析对象。 | experimental-fact | direct | pp.2-3, Figs.2-3 | false |
| G22-6 | 本文以 `R_ac` 和 linear polarization 两项互补测量联合提取 mixing ratio；`R_ac` 比较 `154°/90°` 谱强度，`P` 使用 clover 相邻晶体的 Compton scattering。 | experimental-criterion | direct | pp.2-3, method paragraph and Fig.3 | false |
| G22-7 | 376 与 462 keV links 的联合分析得到约 `δ=-0.26`、`-0.28` 的小 `abs(δ)` 解；尽管误差较大，作者据 `abs(δ)<1` 将其归为 M1-dominated。 | experimental-fact | direct | p.3, Fig.3(a-b) and first paragraph | false |
| G22-8 | Guo 等指出其小 `abs(δ)` 结果与早期 internal-conversion measurements 一致，却与 Sensharma 2020 的 `δ=-2.67(7)`、`-2.98(+0.02/-0.03)` 大 `abs(δ)` 解明显不一致。 | author-interpretation | secondary-comparison | p.3, Fig.3(a-d) and first paragraph | false |
| G22-9 | 由文献给出的 Band 1/`186Pt` core 带内 `B(E2)=100-200 W.u.` 与本文小 mixing ratios，作者估计 `B(E2)_out` 仅数 W.u.，并据此反对 Band 2 相对 Band 1 的集体 wobbling excitation。 | author-interpretation | derived | p.3, left column, paragraph before QTR discussion | false |
| G22-10 | QTR 采用 standard Nilsson/pairing parameters、irrotational-flow-like γ dependence、`J0=25 ħ² MeV^-1`、`J1=8 ħ⁴ MeV^-3`、`ε2=0.21`、`γ=12°`，并包含 Fermi level 附近 9 个负宇称轨道。 | model-result | direct | p.3, QTR setup paragraph | false |
| G22-11 | QTR 波函数把 Bands 1/2 主要联系到源自 `h9/2` 的最低/次低轨道；计算的 energies、`δ`、`B(M1)_out/B(E2)_in` 与 `B(E2)_out/B(E2)_in` 同本文及较早 internal-conversion data 较一致，而与 Sensharma 2020 的大 `δ` 数据冲突。 | model-result | direct | p.3, Fig.4(a-d) and final paragraph | false |
| G22-12 | 论文采用的核心实验判据是：one-phonon wobbling candidate 到 zero-phonon band 的 ΔI=1 links 应有 predominant E2 character；能量和 transition-probability ratios 的模型比较只能提供附加支持。 | experimental-criterion | direct | p.4, first paragraph | false |
| G22-13 | 作者指出 angular-distribution `χ²(δ)` 常有 `abs(δ1)>1` 与 `abs(δ2)<1` 两个解；应报告置信水平并检验第二解能否排除，精确 polarization 可帮助选解，但 gated spectra 与偏振统计会影响不确定度。 | experimental-criterion | direct | p.4, Figs.5-6 and surrounding text | false |
| G22-14 | 对 Sensharma 2020，Guo 等具体批评其未测 Band 2 links 的 linear polarization，未讨论可能的小 `abs(δ)` 解，并把大 `abs(δ)` 曲线主要与 pure-M1 情形比较；因此 angular distribution 本身不足以唯一选出 E2-dominated 解。 | author-interpretation | secondary-comparison | p.4, Fig.5(d) and paragraphs before/after Fig.5 | false |
| G22-15 | 作者把 wobbling phonon 描述限定为高自旋下的小角 harmonic approximation。总角动量满足矢量耦合 `J=j+R`；多数 reported low-spin bands 的最低态约为 `J=j+1`，对应集体角动量 `R` 仅约 `1ħ`、collective rotation 极慢，难以形成该近似所要求的高自旋小角进动。对 `187Au h9/2`，作者还指出 proton Fermi surface 靠近 intruder subshell 底部，与其概括的 LW 需准质子处于 j-shell 中部的几何条件冲突。 | author-interpretation | direct | pp.1-2, Fig.1 and discussion before experimental setup | false |
| G22-16 | 作者批评既有范式只在 signature partner 与 wobbling 间选择，并指出 β/γ vibration、tilted precession 等低自旋集体机制也可能产生增强的 E2 links；大 `abs(δ)` 单独不足以无歧义证明 wobbling。 | author-interpretation | secondary-comparison | pp.4-5, final discussion | false |
| G22-17 | 作者最终把 `187Au` Band 2 重解释为 dominant single-particle excitation，而非 wobbling phonon；对其他 reported low-spin wobbling cases 只作“现有证据通常不足”的总体评估，并要求以可区分 wobbling、TiP 与振动的观测量继续检验。 | author-interpretation | direct | p.5, final two paragraphs and Summary | false |
| G22-18 | 补充材料说明 `R_ac` 由相同全角度 gates 下的 `154°/90°` 效率归一谱强度比取得；偏振不对称校正由标准源标定为 `a(Eγ)=0.975(24)+7.6(379)×10^-6 Eγ`。由于高自旋异构态使 `σ/I` 不能由本实验固定，作者在所有可行 `σ/I` 上取穿过实验误差矩形的椭圆曲线来界定 `δ` 区间。 | experimental-criterion | direct | supplementary material pp.1, 3-4, data-analysis section and Fig.2 | false |
| G22-19 | 对 376 keV transition，作者合并 316、319、400、417、471、565、625 keV 七个 clean gates；对邻近异构态以上 463 keV 线可能污染的 462 keV peak，则选择 316/400 keV gates 并限制 313 keV peak 的左侧区间，采用 upper/central/lower bounds。拟合至少重复五轮，finite-opening-angle correction 小于 3%，并对 efficiency/opening-angle 采用 5% systematic uncertainty。 | experimental-fact | direct | supplementary material pp.1-3, Figs.1-2 | false |
| G22-20 | 补充 QTR 波函数显示 Band 1 主要由 orbital #19、`K_long=1/2` 构成，Band 2 主要由 orbital #21、`K_long=3/2` 构成；Band 2 中 orbital #23、`K_long=5/2` 的贡献随自旋增加，而作者联系到 nuclear precession 的 orbital #19、`K_long=3/2` 成分在低自旋处较小。 | model-result | direct | supplementary material pp.4-5, Table 1 and Fig.3 | false |

## Nuclear Structure Information

- [[187au-yrast-band]]：本文 Band 1；QTR 主要对应 `h9/2` 来源的最低轨道；
- [[187au-longitudinal-wobbling-band]]：本文重新检验的 Band 2；作者以 M1-dominated links 和 QTR 提出 dominant single-particle excitation；
- [[187au-signature-partner-band]]：Sensharma 2020 报告的粉色 sequence 是 `11/2-、15/2-、19/2-、23/2-` 的负宇称 `α=-1/2` 序列，被解释为 `πh9/2` Band 1 的 unfavored signature branch；Guo 本实验未观察到该序列，并把相近 γ 线归入 `188Pt`，因而对其 `187Au` 身份提出质疑；
- Guo Fig.2 中标作 Bands 3/4 的既有结构不是 Sensharma 2020 新建 “band (3)” 的同一稳定标签，后续引用必须带来源说明。

## Authors' Interpretation

- Band 2→Band 1 links 是 M1-dominated，而非 wobbling 所需的 E2-dominated；
- Bands 1/2 的差异主要来自相邻 `h9/2` 单粒子轨道 excitation；
- Sensharma 2020 的大 mixing-ratio branch 并非 angular-distribution data 的唯一解；
- 低自旋进动仍可能存在，但不应自动用高自旋 wobbling-phonon approximation 描述。

以上均为 Guo 2022 的 counter-interpretation，不是本 Wiki 对 `187Au` 争议的最终裁决。

## Model Results

- QTR 输入与模型空间见 G22-10；
- Fig.4 比较 energies、mixing ratios 和两类相对 transition ratios；
- 波函数的 orbital content 支持作者所称 single-particle excitation；
- 补充材料给出 orbitals #19/#21/#23 的逐自旋波函数成分；这些是 QTR model results，不是实验测得的主轴分量；
- TiP 在本文中作为可能的低自旋替代机制和 `135Nd` 已报道案例出现，不是本文对 `187Au` 的直接模型计算结果。

## Competing Interpretations and Limitations

- [[sensharma-2020-longitudinal-wobbling-187au]] 以四条 Band 2→Band 1 links 的大 `abs(δ)`、增加的 `E_wobb` 与 PRM 比较支持 LW；Guo 2022 则以独立 `R_ac-P`、internal conversion 比较与 QTR 支持 single-particle reinterpretation；
- Guo 的两条关键 links 虽得到 `abs(δ)<1`，正文明确指出误差较大，精确数值与系统学仍需人工复核；
- `B(E2)_out` 为从 mixing ratio 和外部 `B(E2)_in` 数据推导的估计，不是本文寿命测量；
- 对 `135Pr`、`133La`、`105Pd`、`183Au`、`127Xe` 等案例的讨论是 broader controversy assessment，不作为这些核素的原始实验摄入；
- 补充材料已挂接并补齐 polarization procedure 与 QTR 波函数细节；G22-18 至 G22-20 已完成人工复核。

## Extracted Pages

- Nucleus: [[187au]]
- Bands: [[187au-yrast-band]], [[187au-longitudinal-wobbling-band]], [[187au-signature-partner-band]]
- Experiment: [[hirfl-187au-o18-108mev]]
- Concepts: [[wobbling-motion]], [[longitudinal-wobbling]]
- Observables: [[multipole-mixing-ratio]], [[interband-e2-strengths]]
- Methods: [[gamma-gamma-coincidence]], [[two-point-angular-correlation-ratio]], [[linear-polarization-asymmetry]]
- Model: [[triaxial-particle-rotor-model]]
- Project: [[187au-longitudinal-wobbling-controversy]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]

## Personal Notes

本页是 `187Au` project 的 counter-source/reinterpretation source。用户已完成 source 页面与 G22-1 至 G22-20 的逐条审核；页面为 `human-reviewed`，全部 claims 均为 `needs_review: false`。未建立 `low-spin-wobbling-controversies` umbrella project。

## Day18 checkpoint052修订：内转换/偏振约束与单粒子解释边界

原GU22-claims/review保持；旧GU22-D18-1降为superseded。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D18-1 | **superseded**：旧关于“彻底瓦解全区wobbling”的断言降格，由GU22-D18-2/3分层记录作者对187Au的测量与QTR单粒子解释。 | task-correction | superseded-interpretation | 本段D18-2/3；旧guo22-sensharma20-187au-result-022 | true |
| GU22-D18-2 | **superseded at checkpoint094**：旧偏振/δ身份、跨数据强度或排他认证不得沿用；见GU22-D22-R094-1至3。 | task-correction | superseded-interpretation | checkpoint094原件核验 | true |
| GU22-D18-3 | QTR模型波函数计算表明Band 1与Band 2主要基于h9/2亚壳的最低与次低轨道，表现为单粒子性质；作者据此提出低自旋带由单粒子激发主导的解释。这构成本核及该能带的具体结构结论，不作为排除所有低自旋集体效应的普适定理。 | author-interpretation-boundary | direct-and-boundary | PDF pp.3-5 Fig. 4；Sec. III | true |

## Day19量化审计：低自旋摆动声子普遍证伪、内转换系数排他性与M1支配定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_low_spin_wobbling_systematics_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/low-spin-wobbling-systematics-result-076.json`，核准了针对 Guo 2022 及 $^{135}\text{Pr}, ^{133}\text{La}, ^{187}\text{Au}, ^{105}\text{Pd}, ^{133}\text{Ba}, ^{131}\text{Xe}$ 六大低自旋摆动候选执行的系统学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GU22-D19-1 | **superseded at checkpoint094**：旧偏振/δ身份、跨数据强度或排他认证不得沿用；见GU22-D22-R094-1至3。 | task-correction | superseded-interpretation | checkpoint094原件核验 | true |

## Day 21 Checkpoint 019 证据门量化审计：联合偏振排他解算与纵向摇摆证伪

依据推断阶梯方法论（[[experimental-claim-boundaries]]）及独立量化程序 day21_checkpoint019_longitudinal_wobbling_187au_audit.py（产物 outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/longitudinal-wobbling-187au-audit-019.json），对 Guo 2022 的反方测量与单粒子重解释完成推断阶梯边界核定：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D21-1 | **superseded at checkpoint094**：旧偏振/δ身份、跨数据强度或排他认证不得沿用；见GU22-D22-R094-1至3。 | task-correction | superseded-interpretation | checkpoint094原件核验 | true |

## Day22 checkpoint094：偏振量身份、相对强度和伴随带边界

定向复读主文pp.1–5物理正文、SI六页及其方法图；视觉核主文p.3 Fig.3/4、SI p.3 Fig.2。原G22-1–20及既有review范围不变；以下均为新增Codex self-audit，needs_review: true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D22-R094-1 | Fig.3(a,b)打印376/462 keV的δ分别为−.26(+.11/−.15)、−.28(+.23/−.69)。正文的−.10(5)是376 keV线的旧测量polarization P，不是新δ。作者在不固定σ/I下以P–Rac联合约束得到小模解；误差大，不能从图的区间直接报新3σ/4σ显著性。 | experimental-result-and-quantity-identity | direct-original | main p.3 Fig.3(a,b) and first paragraph | true |
| GU22-D22-R094-2 | p.3的数W.u.是采用外部187Au/186Pt带内B(E2)=100–200 W.u.的估计，非本实验寿命。Fig.3(c,d)把本次δ换算为αK与旧Rupnik/Bourgeois测量比较，不是新取得独立conversion谱。旧88倍和1.1e−4 e²b²没有本文依据；该绝对数值也不能与数W.u.互换。 | absolute-relative-and-source-lineage-boundary | direct-original | main p.3 Fig.3(c,d), caption and paragraph before QTR | true |
| GU22-D22-R094-3 | 本实验未见Sensharma伴随signature-partner序列及429/437 links，相似265/405/414/551线归188Pt；这是本数据的non-observation/reassignment，不能把Sensharma全数据逐事件重归属或称二声子带证伪。QTR的Band1/2轨道#19/#21、低spin进动成分小是模型解释，未直接测主轴j。SI承认Q由同型探测器的外部Zheng2013曲线迁移，δ区间取可穿过P–Rac误差矩形的全部σ/I曲线，非公开完整joint-likelihood。 | experiment-model-and-response-boundary | direct-original | main p.2 Fig.2; main p.3 Fig.4; SI pp.3–5 Fig.2/3 and Table1 | true |

按打印中央δ计算，376/462的E2光子份额约6.33%/7.27%；若强行保持同一光子分支、能量和分母，则相对Sensharma δ=−2.67/−2.98的E2份额变化因子约13.85/12.36。此为条件敏感性，不是两个独立实验的实测绝对B变化，更不是物理随spin塌缩。完整错误旧文本存于Day22 run的pre-correction-094.json。


## Day23 原件复核：误差上标与新增观测的依赖

本次回读主文6页、SI6页的全文主线，视觉核主文p.3 Fig.3/4；对376/462两处图例另作4倍局部渲染。两份raw的SHA与原记录一致。原page review与既有claim flags保留，以下为Codex self-audit，needs_review: true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-001 | Fig.3(a)图例实际为δ=−.26(+.11/−.15)，并非继承GU22-D22-R094-1中的+.16；本轮定向更正该条和questions的上误差。Fig.3(b)仍为−.28(+.23/−.69)。文本抽取的上标易错，中央值不变，不据此新增显著性或最终模式裁决。 | printed-uncertainty-correction | direct-original-visual | main p.3 Fig.3(a) | true |
| GU22-D23-002 | SI p.3说明本实验因强线主要由isomers布居而难以自身确定Q，故采用Zheng2013同型clover的曲线；本次标准源确定的是a(E)。SI的5%系统误差用于效率及有限张角对Rac的影响，不能把它当作所有偏振校准参数的完整joint prior。 | response-calibration-dependence | direct-original | SI p.3, polarization-sensitivity and systematic-error paragraphs | true |
| GU22-D23-003 | 462keV分析使用316/400门得到Rac/A上界，313窄门得到中央/下界；463keV异构态以上线与465keV E1污染须分别处理。这些选门结果属于同一采集的选择敏感性，不能按独立重复实验相乘。作者未给这些门之间完整Cov。 | gate-selection-and-independence-boundary | direct-original-and-bounded-inference | SI p.2, first paragraph; SI p.3, first paragraph | true |

Knowledge Impact and Learning Decision：revises一处印刷误差，limits同源多量计票及跨装置响应迁移；未判支持/反对任一模型已最终胜出。实际比较程序见[[signature-tip-shears-discrimination-contract]]，争议谱系见[[low-spin-wobbling-controversies]]。


### Day23：Rupnik引用的母核文字疑点

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-004 | 本PDF p.2实际印作Rupnik等对187Ag的β-decay study，3倍局部图核实这不是OCR把Hg读成Ag。该Ag→Au归属不符合单步β衰变ΔZ=±1的电荷核查；LSU原作者馆藏页DOI10.1103/PhysRevC.58.771摘要则写Hg两态衰变，并明确正文当前不可下载。馆藏摘要的质量数/宇称公式显示为[Formula Presented]，不足以代替完整原文校定；本轮仅标出Guo母核印刷疑点，不从摘要补376/462的αK值、母核完整Jπ或SP非观察的灵敏度。G22-4原用户核阅flag保留，其Ag字面只按作者引用记录，不当真实母核已认证。 | source-identity-text-boundary | direct-original-visual-and-repository-abstract | main p.2, paragraph below Fig.2; https://repository.lsu.edu/physics_astronomy_pubs/4634/ Abstract and availability statement | true |

Rupnik访问：Crossref200题名/作者/DOI匹配，publisher直PDF403、harvest401，LSU200但无正文；OpenAlex索引无OA正文位置，Google Scholar本次超时。这是本次有界检索结果，不声称全文永不可得，也不把搜索失败转成原核态不存在。下一条高信息路线仍为原文conversion表、母核/选择条件与独立性，而非重复引用Guo。
