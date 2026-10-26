---
type: source
title: "Probing the nature of the conjectured low-spin wobbling bands in atomic nuclei"
aliases: [Guo 2022 187Au, low-spin wobbling counter-source, probing low-spin wobbling bands]
created: 2026-07-04
updated: 2026-10-25
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


### Day23：Bourgeois1978原转换资料的身份与访问

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-005 | 本文Ref25的Bourgeois/Kilcher/Letessier/Berg/Desthuilliers、NPA295(1978)424–444，经Crossref题名/作者/卷页核定DOI10.1016/0375-9474(78)90184-7。OpenAlex无OA位置、HAL精确DOI无记录，publisher discovery无PDF候选，ADS该文端点403；尚未获得正文或376/462的原αK表。因此当前只完成追溯身份，不新增一份直接核阅的实验或δ约束。 | original-reference-metadata-and-access-boundary | direct-reference-and-external-metadata | main p.5 Ref.25; https://doi.org/10.1016/0375-9474(78)90184-7 | true |

本次Elsevier metadata工具缺pybliometrics配置，NNDC入口域名解析失败；这些是路线限制，不是文献不存在。Rupnik的另一路publisher下载工具拒绝仓库内输出路径，未改其安全目录或下载到仓库外；公开ADS端点超时后没有自动当作成功/永久不可访问。继续以原子claim、实际转换系数与谱系为目标，不以访问次数替代科学信息。


## Day23 外部官方API字段核验（非本文新测量）

以下是外部IAEA接口的本次field自审，不归属Guo2022实测，也不冒称已取得Rupnik/Bourgeois全文。请求URL为`https://www-nds.iaea.org/relnsd/v0/data?fields=gammas&nuclides=187au`与`fields=levels`；官方guide为`https://www-nds.iaea.org/relnsd/vcharthtml/api_v0_guide.html`。CSV只在tmp公开staging读取，按raw保护边界未新增/覆盖raw；正式原始快照归档仍deferred，不能把本节用作新实验paper-level数据。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-006 | 实际gammas/levels响应有640/312行，Extraction_date=2026-10-25，但Au187条目publication cut-off=1-Nov-2008、authors=M.S.Basunia；guide Data sources称ENSDF April2022 snapshot。gammas row(16,2,2)列496.73→120.33keV、376.3、(11/2−)→9/2(−)、mixing_ratio=.6、unc_mr=.3、tot_conv_coeff=.147、tce_unc=.024；row(38,10,3)列815.81→353.66keV、462.1、(15/2−)→(13/2−)、mixing_ratio=1.1、unc_mr=.3、tot_conv_coeff=.064、tce_unc=.012。这些是export字面字段；完整adopted notes/符号约定未得，不将正数字串认证为正物理δ，也不把total系数冒充独立测得的αK或2020/2022之后裁决。 | evaluated-export-field-readout | direct-public-api-with-archival-boundary | IAEA gammas187au; snapshot row keys(start_level_idx,end_level_idx,gamma_idx)=(16,2,2),(38,10,3); guide Data sources | true |
| GU22-D23-007 | API近能量436.6keV row(92,48,0)是1393.34→956.44、(13/2−)→(13/2−)，与支持方436.5的SP→yrast ΔI1不是同一endpoint identity。不能仅按接近能量合并/否定两线；旧2008评价无2020新序列也不构成其非观察实验。 | transition-identity-and-cutoff-boundary | direct-export-and-cross-source-boundary | IAEA gammas187au row(92,48,0); AU20-5 | true |
| GU22-D23-008 | 实际levels CSV的unc_hl列名出现两次（0-based列12与15），分别邻half_life及half_life_sec；普通DictReader会覆盖第一列。以snapshot idx相连时，376/462母态16/38的half_life均空白，不能用end-level idx2的2.3s异构态寿命填入。空白不是零。guide给idx同核素连接但未为本export的全部重复/新增字段提供完整解释。 | CSV-identity-and-lifetime-readiness | direct-api-schema-self-audit | IAEA levels187au header positions12/15; levels idx16,38,2; guide General notes | true |

两CSV SHA256依次为8c38df9d5634f6255bc57d8c26e3231042cb78f95a02c4235191c81bac01155b与ffa9e79ea076ca7d857e0eb01d681295c05212eda1316da78de89c6232fbb279；字段/target rows重放程序`system/scripts/day23_au187_api_identity.py`，不是原实验producer。首次严格CSV宽度检查发现末尾空record，改为仅跳过全空record后重跑6项identity controls通过，没有丢弃非空不等宽行。

Knowledge Impact and Learning Decision：supports对376/462近能量/端点和来源时间窗的逐量核验，limits用total/αK、magnitude/sign、daughter/parent lifetime或evaluation/new acquisition互换；本次没有恢复独立历史αK表、共同Cov、δ显著性或模式最终归属。


## Day23 外部187Hg衰变导出：母核、空值与服务码

以下继续为外部API field核验，原始完整CSV仍tmp staging/正式raw归档deferred，非Guo原测量；URL为`https://www-nds.iaea.org/relnsd/v0/data?fields=decay_rads&nuclides=187hg&rad_types=g`及`rad_types=e`。含义依据同一官方guide的decay_rads及Error codes。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-009 | γ导出595行均列母核(pZ,pN,symbol)=(80,107,Hg)、daughter=(79,108,Au)、EC+B+，从而支持母核Hg→Au的身份核查，不能把原PDF的187Ag当真实单步母核。两parent均p_energy=0，却分别带empty/X的p_energy_shift与jp3/2(−)/13/2(+)及1.9/2.4m；不能按0能量合并两state，也不把X+0认证为实际零激发。这里jp/half_life字段属于Hg母态，不是Auγ初态。它不替代Rupnik1998正文/具体选样。 | evaluated-parent-daughter-field-identity | direct-official-api-with-boundary | IAEA decay_rads187hg rad_types=g; guide common fields | true |
| GU22-D23-010 | 本次595γ行intensity/unc_i全空；376.3/462.1只出现在X-shifted 13/2(+)母态组，Au初态half-life也空。13/2(+)母态144s、376末态2.3s和γ初态空值是不同clock。对应γ初末态能量496.79/120.40与815.89/353.78，与adopted export略不同，需保留dataset身份；两个导出unc_mr分别字面3和.3，未获统一说明/原notes前不合并误差。没有从这些空强度恢复photon branch或αK。 | missing-intensity-and-field-role-boundary | direct-export-and-self-audit | IAEA decay_rads187hg target energies376.3/462.1; GU22-D23-006 | true |
| GU22-D23-011 | electron请求HTTP200但body仅0换行；官方guide Error codes定义0为请求有效、无满足条件的数据，非实测零电子强度/未观察转换线，故不提供αK、上限、排除置信度或机时。γ字段conversion_coeff在guide明确为total；接口可读不等于取得独立K-shell测量。 | service-status-versus-negative-evidence | direct-official-documentation-and-response | IAEA decay_rads187hg rad_types=e body0; guide Error codes and gamma fields | true |

γ/e响应SHA256依次为61834a8d4ebfcb70431bd9540e0591ec85c8d6b0decf88c12a95c2a040c00200与9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa；既有Au identity脚本扩展optional parent inputs，原6项和新6项role/空值/service-code控制合计12项通过。此结果仍是reading/readiness，非原实验或BrIcc重放。


### Day23 API版本对照的行顺序边界

同查询另取guide所列v1服务后，187Hgγ返回同样595行，文件SHA不同，但按全部字段字符串及重复行计数作multiset比较完全相同（0个v0-only、0个v1-only）；区别是若干同能量条目的顺序。电子v1同样返回0，字节/hash相同。不能把逐行zip的母态/能量差当新评价变化，也不能以能量单列去重而丢掉不同母态数据。该核验仅比较本次两个响应，不断言接口在所有核素/所有版本恒等。

v1 γ SHA为f585ef106e48aed4edba408273c3ec6067cd1e860b24ee02aa0559b82a761801；URL仅将上述v0换v1。本次原始快照仍未正式raw归档，不能把字段一致当多源独立确认。

## Day23：原QTR多轨道内容与磁算符readiness

本次定向回读主文PDF3参数段与SI PDF4/5 QTR/Table1/Fig3说明，SI PDF4 fresh视觉核，原SI SHA相符；不新称全文重读。旧G22人审claims保持，新增needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-012 | SI Table1的9轨道包含h11/2、h9/2与f7/2来源；#21列(h9/2;3/2)、(f7/2;1/2)，#22列(f7/2;1/2)、(h9/2;3/2)、(h9/2;1/2)。Band1主要#19、Band2主要#21，另有#19/#21/#22/#23分量。故dominant h9/2不是严格纯单j声明；这些标签/图中柱不能替代完整带符号振幅、BCS occupation、radial及磁/电矩阵元。单jnormalized SM/SE消去结果只能作为条件练习，不能直接认证本QTR双比或从图补造physicalδ。 | original-QTR-model-space-and-operator-readiness | direct-original-and-bounded-inference | SI PDF4 Table1 and QTR calculations; SI PDF5 Fig.3 and text | true |

跨j的完整磁算符边界见[[hamamoto-2002-wobbling-excitations-odd-a-high-j-aligned-particles]] H02-D23-004。其l5角代数只是h双伙伴分量，不是本论文实际波函数含量，更不计算h/f混合或观测到的新M1。主文给J0=25/J1=8、ε2=.21/γ12°，这些输入与支持方PRM不同；冻结实验D进行替代解释可行，但不能称二者是只换configuration的同H受控实验。

## Day23：官方ENSDF注释提供旧转换数值的转述层

本节是外部官方评价记录的定向读取，不归为Guo2022的新测量，也不声称已读Rupnik1998/Bourgeois1978原论文。经[DatasetFetchServlet](https://www.nndc.bnl.gov/ensdf/DatasetFetchServlet)实际POST nuc=187AU，读取表单后向[EnsdfDispatcherServlet](https://www.nndc.bnl.gov/ensdf/EnsdfDispatcherServlet) POST dbclass=ensdf、page-source=singular、chooseit=ENSDF text format，datasetcheck分别187079001,187AU、187079003,187AU、187079004,187AU。HTTP200对象实际为含pre的XML/HTML，抽取pre后才按ENSDF列读取。文件在tmp，正式raw归档deferred；这里不作完整NDS或primary全文摄入。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-013 | 官方187079003的376.3行组、母496.79(11/2−)，实验注释转述αK=.119(15)[1998Ru04]和.11(3)[1978Bo05]；462.1行组、母815.89(15/2−)，转述αK=.050(9)[1998Ru04]和.08(2)[1978Bo05]。原字串分别{I15}/{I3}/{I9}/{I2}，括号按最后位表记，不由它们新定coverage/CI。它们是已读取评价对历史实验的明确数值归属，仍未核两篇原实验的谱/归一/误差。 | externally-evaluated-experimental-report | direct-official-annotation-secondary-to-primary | 187079003 pre lines193–203 and405–421, target cG alpha(K)exp comments | true |
| GU22-D23-014 | 同dataset的cG MR总说明明确混合比由评价者据αKexp或αLexp计算。目标G列MR=.6(3)/1.1(3)、totalCC=.147(24)/.064(12)，与SG行KC=.119(21)/.051(10)及实验comment的αK必须分角色保留。adopted187079001和API又转录这些采用量；不能把实验αK、评价MR、SG KC、API total当四份独立实验，也不能由无符号MR字串恢复物理δ正号。 | derived-evaluation-and-shared-input | direct-official-annotation-plus-dependency-inference | 187079003 pre lines43–47; target G/SG/cG groups376.3 and462.1; 187079001 target G groups | true |
| GU22-D23-015 | 三对象都写NDS110,999(2009)、CUT1-Nov-2008，并有7-Nov-2013 ERR记录：adopted交换XREF B/C，两decay对象修正母半衰期。P行分别为0+X、13/2(+)、2.4m与0、3/2(−)、1.9m；伴注指出1998Ru04印刷时间与作者通信、非该文新测。不能把publication cutoff当文件全无后续修订，也不能把Hg母clock用于Au争议能级τ。 | evaluation-version-and-clock-provenance | direct-official-headers-and-parent-records | 187079001 H records; 187079003/004 H and P records plus cP T comments | true |
| GU22-D23-016 | 评价将1998Ru04/1994RuZX/1995Ru07合列于一段实验描述，而不是声明三次独立采集；1978Bo05另有Au(p,xn) mass-separation描述，187079004还提醒原1978 decay scheme合并两母态数据。adopted旧376/462带Z flag，header定义其E/RI来自1.9m dataset，但当前003中亦列两线，且2013有XREF/clock更正；此处冻结每个记录的文字/端点，不由标签自行重写哪批events属于哪个母态。 | source-family-and-assignment-boundary | direct-official-annotation-and-unresolved-ledger | 187079003/004 experiment headers; 187079004 1978Bo05 combined-parent comment; 187079001 cG E(Z)/RI(Z) and target G flags | true |

三响应SHA256：adopted663bbcedab538fcd87b882a4d82757fda2cc637218e166cdaeb0f946213d8096；2.4m 1b1ae7cdf23afe312655285ebcc0b4f4d0526ac6167eff24dd47283c0457d7d8；1.9m ab682db5108decfd1ec01d8451585bf6b91533f2b3be3656795421d9b3a1c454。抽取文本1678/1522/679行，定向实际读headers、目标母态/γ及其comments，未逐行精读全评价。`system/scripts/day23_au187_conversion_provenance.py`的15控制仅核hash/解析/字段/来源角色，无新δ/理论ICC/似然。[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-2的标准混合式只含δ²；旧转换可约束幅度而不单独选择符号。本节没有实际运行BrIcc、量化大根排除度或终审LW/SP。新增needs_review:true，原G22人审范围不改。

## Day23：旧转换与新δ中心并非逐点完全重合

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-017 | 在本任务实际FO查询的历史E376.3/462.1标称能量和标准M1/E2截断下，本文δ中央−.26/−.28前向αK约.1412/.0813，支持方大δ中央给.0498/.0289。旧评价转述376的.119(15)/.11(3)与462的.050(9)/.08(2)须各自并列；不能把“旧转换与新结果一致”的概述改写为四个旧点均与本文δ中央完全相同。尤其462的1998与1978中心不同。未传播各自δ/归一/理论/能量及共同Cov，不据这些中心差报排除度、原paper错误或最终归属。 | conditional-cross-source-centre-comparison | actual-theory-query-plus-secondary-experiment-and-task-forward-model | main PDF3 Fig.3(c,d); GU22-D23-013; KB08-D23-001/002 and task input-contract030 | true |

实际理论输入与条件计算直接回链[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D23-001/002；大δ源中央为[[sensharma-2020-longitudinal-wobbling-187au]] AU20-D22-R094-1。没有反演或补造本核新δ，没有把quoted误差盒当CI；理论表输入缺口已部分解除，历史电子/光子谱归一与全response/Cov仍缺。新增needs_review:true，旧人审及P/δ身份不变。

## Day23：印刷δ端点的前向区间

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-018 | 仅将已报376 δ端点[−.41,−.15]、462[−.97,−.05]代入本任务固定FO K式，αK像分别[.132139,.145829]、[.055165,.085742]；与GU22-D23-013旧实验每项“quoted中央±quoted误差”坐标范围分别有交集。因此GU22-D23-017的中央不同不自动给出区间不相交。此处无任何置信水平、joint coverage或同时拟合含义，未传播理论/能量Cov、历史归一及原δ联合响应；不是新δ/αK测量或全分支认证。 | deterministic-endpoint-image-and-boundary | original-quoted-endpoints-plus-actual-theory-and-task-math | main PDF3 Fig.3(a,b); GU22-D23-001; GU22-D23-013; KB08-D23-001/002; task input-contract031 | true |

[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-2及KB08-D23-001/002给标准式与实际标称理论输入。这里保留印刷不对称误差端点，只作确定性映射，不假定原δ为Gaussian或独立；四个逐点交集不能拼成存在共同nuisance参数的联合区域。新needs_review:true，旧source审核及实际分支争议保持。

## Day23：外部188Pt原文的实际层次与候选端点

本节是2014外部primary的只读分析，不归属Guo本文测量，也不把它冒作Guo Ref23的2017文。S. Mukhopadhyay et al.，*Coexisting shape- and high-K isomers in the shape transitional nucleus188Pt*，PLB739(2014)462–467，DOI[10.1016/j.physletb.2014.10.069](https://doi.org/10.1016/j.physletb.2014.10.069)。INSPIRE record1333158给[实际PDF](https://inspirehep.net/files/8138a35652bdbd80d9ea769239e24cfd)，200/513325bytes/SHA256 6d6d56de993b0d962757a5ffcbbb457e206a82333718010b39ce02d570a627e8。首版权CC BY3.0/SCOAP3已实际核。全文6页主线/公式/三表已读，视觉核Fig1/2、Table3/Eq1/2，未逐一摄入所有参考。PDF仅tmp/day23-originals/pt188-verifiedlink036-e219ce97.pdf，正式raw归档deferred；不改原Guo元数据/review范围。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU14-D23-001 | 2014 primary使用174Yb(18O,4n)、85MeV、TIFR/INGA18clover，四90°、两65°、40/115/140/157°各三，>10^9 fold≥2事件，DCO用90/157矩阵并按本array控线校准，另测偏振。它是Pt独立研究，不是支持Au的19F+174Yb或Guo新HIRFL数据；与2017是否同一采集尚无event ledger，不能只因作者/核素相同强认或重复计票。 | primary-campaign-and-method-identity | direct-external-primary | printed463 experimental paragraphs | true |
| MU14-D23-002 | Fig1的188Pt基带低部为2+→0+约266(正文/表2为265.6)、4+→2+约405(Fig2门表为405.1)、6+→4+约513，再有598/655；SeqII另有约414和551，而SeqV有约412和549。必须按各自端点/序列标识，不能把图整数能量当精确γ或与Au SP的265.3/404.5/412.3/548.6逐条合并。Pt的整数spin端点与Au半整数端点亦是不同核素假说下的身份，不是同一level重标两名。 | primary-levelscheme-and-near-energy-boundary | direct-external-figure-and-text | printed464 Fig1; Fig2 caption; printed465 Table2 | true |
| MU14-D23-003 | Pt Fig2的实际谱来自689.9与列表{202.6,583.7,894.5,405.1,265.6}之一的双门sum，标新high-K相关峰；这不是Au的232.5+436.5双门。本文局部谱图未提供同Au门窗/时间/效率对象，不能由Pt近能量网络或本篇未列某Au门能量便裁决该门的Pt泄漏为0或必然存在。 | primary-gate-and-companion-identity | direct-external-spectrum | printed464 Fig2 caption and spectrum | true |
| MU14-D23-004 | Pt作者以alignment与分支强度分析，比较9−high-K的ν[615]11/2+⊗ν[503]7/2−和ν[624]9/2+⊗ν[505]9/2−候选；Table3给计算(gK−gR)/Q0=−.09/−.04，所谓实验项是绝对组合|gK−gR|/Q0=.02(1)，Q0=5.4eb、gR=.21为采用输入。它不是新独立直接g因子测量。作者偏好后一组态，SeqV的K5−仍不能排K3−；有限形式可行不赋两配置等可信，也不把磁尺度当独立holdout。 | primary-configuration-and-derived-operator-boundary | direct-external-model-and-extraction | printed466 Eqs1/2 and Table3; SeqV K discussion | true |
| MU14-D23-005 | 两个已报isomer时钟的角色不同：12+1形状候选T1/2=.66(4)ns来自旧Richter1979，9−3 high-K也引用旧.66ns；Table2的B(E2)使用旧寿命和本次分支，且9−3的.06(1)W.u.脚注明确不含寿命/半衰期误差。它们不能移用为Au争议母态τ，也不能以两个同值时钟推同一态/同一CI。 | primary-reused-clock-and-uncertainty-lineage | direct-external-primary-and-footnote | printed463 isomer paragraphs; printed465 Table2 footnote | true |

另一路Guo Ref23：PRC96,014315(2017)，DOI10.1103/PhysRevC.96.014315与此2014不同。当前Crossref/INSPIRE身份已核，publisher PDF403、harvest401、OSTI连接失败，INSPIRE无body/arXiv信息；发现metadata附Publisher's Note DOI10.1103/PhysRevC.96.019901但note正文未得，不臆测更正内容。publisher Markdown工具provider unavailable且未真正发起代理获取；不把discovery候选当PDF成功。SCOAP3旧API q返回无关最新条目，已核DOI剔除；猜测文件路径403也不作target evidence。下一仍需2017原级联与真实门/净峰匹配，不由检索困难认证Au/Pt身份。

[[sensharma-2021-wobbling-motion-135pr-187au]] SE22-D23-003/004的实际支持门谱与此Pt primary并列，[[signature-tip-shears-discrimination-contract]]保存gate/endpoint合同。新claims均needs_review:true，原G22审核保持。

## Day23：188Pt官方评价与2022编译的端点/自旋差

本节为外部ENSDF记录的定向读取，不代替Pt2017原文。实际POST[DatasetFetchServlet](https://www.nndc.bnl.gov/ensdf/DatasetFetchServlet) nuc188PT后按真实表单取得[EnsdfDispatcherServlet](https://www.nndc.bnl.gov/ensdf/EnsdfDispatcherServlet)的datasetcheck188078001,188PT(adopted)、188078004,188PT(HI)及xunpostcheck188078009,188PT(XUNDL5)。三份200对象含pre，提取后866/371/36行。这里只读headers及目标四线/相关comments，不称全文NDS已读；原快照仅tmp，raw归档deferred。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PT18-D23-001 | adopted/HI header为Kondev/Juutinen/Hartley，NDS150,1(2018)，CUT1-Feb-2018。HI将2014Mu12/2017Mu12合写在85MeV18O、1.14mg/cm²174Yb/约750μgAl、18clover的实验段，说明scheme based on二者，E/RI from2017Mu12。该实际评价支持两报告的共同实验谱系候选，仍无逐event/选择ledger，不能依论文数作两独立采集或认证每个点完全复用。 | evaluated-campaign-and-primary-lineage | actual-official-evaluation | 188078004 pre header/experimental paragraphs and cG E,RI | true |
| PT18-D23-002 | HI目标母态/γ为265.59(2+)/265.6、670.80(4+)/405.1、1085.16(4+)/414.4、1636.12(6+)/550.9keV；目标γ的comments有2017Mu12的DCO/POL，literal POL未在本任务由primary方法辨定P或asymmetry，不作新偏振点。414.4连接两个4+态，属于跨带ΔI0，而550.9连接6+→4+，不能只按近能量把这些读成AuSP的半整数ΔI2级联。 | evaluated-endpoint-and-observable-semantics | actual-official-evaluation | 188078004 L265.59/G265.6; L670.80/G405.1; L1085.16/G414.4; L1636.12/G550.9 | true |
| GU22-D23-019 | XUNDL5明确compiled unevaluated from2022Gu04，Dec1/16,2022编校，列同一HIRFL108MeV/8clover+16HPGe实验，并直接转述本源将旧549/412/405/265的Au归属换为Pt551/414/405/265。它是本文的编译副本，不增一次独立non-observation/identity验证；该简表目标强度/多极/δ栏空，不补0。 | compilation-lineage-and-empty-fields | actual-official-compiled-record | 188078009 pre identification/experiment/cG comments and four target rows | true |
| GU22-D23-020 | XUNDL5的L1636字面Jπ=8+、G551，而本源主文Fig2(a)绿色顶态实际6+，2018HI的L1636.12也是6+。本次fresh原PDF2图核与SHA相符；这是一处明确编译/源图版本失配，保持原snapshot并needs_review，不擅改raw或由8+→4+制造新的E4推断。XUNDL整数能量的约1keV闭合差也不认证新能量错误或同事件。 | source-figure-versus-compiled-spin-discrepancy | actual-source-visual-and-official-record-comparison | mainPDF2 Fig2(a) greenPt top6+; 188078009 L1636/G551; 188078004 L1636.12/G550.9 | true |

三原response SHA：adopted f89dc018e7dd6683477ecb7d2cdb95aefcd7651fb7759b73ec0ece3fd8705d2c；HI c12ecc1b74df6c7be62423c53ab3dcc11034433e4303dccae2022d4eaac6df10；XUNDL5 0e872908ba5de28dd88694265ee216e6c8e3f87ea61782810295fdaae439e77b。`system/scripts/day23_pt188_official_identity.py`十一项hash/提取/目标/空值/版本控制通过，只核字段合同。2017primary及PublisherNote正文仍未得，不能以官方评价已引用它就宣称原全文已读。[[signature-tip-shears-discrimination-contract]]和[[187au-longitudinal-wobbling-controversy]]保同门响应/归属仍未闭合；新needs_review:true，旧G22人审范围不改。

## Day23：h/f内容的具体算符边界

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-021 | 沿本页GU22-D23-012实际#21/#22的h9/2/f7/2来源，任务补不同l角算符组件：标准l/s M1保l，bare h/f直接块0，而r²C2有允许的h/f角块；各l,j对角磁投影不同。它解释为何不能仅凭dominant h9/2把完整QTR的M1/E2共同因子/径向量全部消去，但未计算作者实际矩阵元、混合核态B/δ或证明偏差显著。 | source-motivated-conditional-operator-transfer | actual-model-space-plus-declared-task-algebra | SI PDF4 Table1/PDF5Fig3; H02-D23-005; task input-contract038 | true |

源模型内容来自原件既有定向核查，本轮只复用该输入、非新全文阅读。完整推导回链[[hamamoto-2002-wobbling-excitations-odd-a-high-j-aligned-particles]] H02-D23-003/005；[[signature-tip-shears-discrimination-contract]]把不同l的径向/相干/BCS条件具体化，不补physicalg/Q/δ或核态。新增needs_review:true，原G22审核保持。

## Day23：Rupnik历史学位论文的精确身份与正文边界

本节只保存外部原作者机构元数据/NSR，不冒称读到转换原表。经[NSR1994RUZX](https://www.nndc.bnl.gov/nsr/?search-type=keynumber&key=1994RuZX)与LSU公开OAI metadata定位到Dubravka Rupnik，*Complete Spectroscopy in the Mercury-187m,g Decay: The Structure of Gold-187.* (1994)，[LSU item5753](https://repository.lsu.edu/gradschool_disstheses/5753)，DOI10.31390/gradschool_disstheses.5753。OAI identifier的内部article6752与公开item5753是不同字段，不拼成同一数字。机构页面实际200且列259页、1994授位、advisor E.F.Zganjar；2017-03入库不是新实验年。公开摘要与原259页正文严格分层。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-D23-022 | LSU原作者摘要明确对象为187g/mHg的β+/EC后187Au，并说γ与conversion electrons在ORNL/UNISOR线上采集。这进一步核清本源印刷187Ag的母核疑点，但摘要不足以确定逐母态spin/feed选择、每条αK或SP序列非观察灵敏度。不能从摘要重建376/462的原表。 | external-original-author-metadata-and-parent-boundary | direct-institutional-abstract-not-body | LSU5753 Abstract; OAI oai:repository.lsu.edu:gradschool_disstheses-6752 dc:description | true |
| GU22-D23-023 | NSR1994RUZX为同题thesis；1995RU07对应PRC51,R2867、DOI10.1103/PhysRevC.51.R2867；1998RU04为PRC58,771、DOI10.1103/PhysRevC.58.771。三记录共同指向Hg decay/γ-ce/PTRM研究谱系，但NSR身份和共同作者不能证明逐event或所有observable完全同源，也不能当三份独立conversion采集。 | external-bibliographic-lineage-and-independence-boundary | direct-official-NSR-metadata | NSR1994RUZX; NSR1995RU07; NSR1998RU04 | true |
| GU22-D23-024 | LSU单篇landing提供公开Download与OAI精确PDF地址，但本次对cgi/viewcontent.cgi?article=6752&context=gradschool_disstheses及context/gradschool_disstheses/article/6752/viewcontent/9502140.pdf的正常单篇请求均403，未获得PDF。没有绕过challenge、批量采正文或把application/pdf元数据当已读body；原1998/1978conversion谱/校准/误差仍缺。此为本次access边界，不是世界范围全文不存在或旧观测无效。 | external-access-and-reading-scope | actual-single-item-access | LSU5753 Download; OAI dc:identifier PDF URL; 1994 thesis landing availability | true |

OAI metadata允许正常索引；本次只读元数据定位目标，未下载库中其它正文。精确原件路线比旧模糊检索更可恢复，然而GU22-D23-013的αK当前仍是官方评价转述。摘要所称h9/2–f7/2混合是作者解释线索，未据此填完整wavefunction/operator/δ，亦不重复计算采集票。新needs_review:true，原G22人审范围不变。
