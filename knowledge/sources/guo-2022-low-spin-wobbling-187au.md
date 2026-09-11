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
- Project: [[187au-longitudinal-wobbling-controversy]]

## Personal Notes

本页是 `187Au` project 的 counter-source/reinterpretation source。用户已完成 source 页面与 G22-1 至 G22-20 的逐条审核；页面为 `human-reviewed`，全部 claims 均为 `needs_review: false`。未建立 `low-spin-wobbling-controversies` umbrella project。
