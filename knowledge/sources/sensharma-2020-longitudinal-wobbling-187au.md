---
type: source
title: "Longitudinal wobbling motion in 187Au"
aliases: [Sensharma 2020 187Au, longitudinal wobbling in 187Au]
created: 2026-07-03
updated: 2026-07-03
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Longitudinal Wobbling Motion in 187Au"
authors: [N. Sensharma, U. Garg, Q. B. Chen, S. Frauendorf, D. P. Burdette, et al.]
journal: Physical Review Letters
year: 2020
volume: 124
pages: 052501
doi: 10.1103/PhysRevLett.124.052501
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevLett.124.052501
zotero_item_key:
citation_key: sensharma_2020_LongitudinalWobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2020_Sensharma et al_Longitudinal Wobbling Motion in Au 187.pdf"
raw_sha256: F348DCE9976AD076FD9B1D5281A728E0923053ACED33B0270F643D770729366A
nuclei: [187au]
reactions: [174yb-f19-6n-187au]
experiments: [atlas-gammasphere-187au-f19-105-115mev]
models: [particle-rotor-model, covariant-density-functional-theory]
observables: [multipole-mixing-ratio, interband-e2-strengths, wobbling-energy]
methods: [gamma-gamma-coincidence]
tags: [a190, 187au, longitudinal-wobbling, signature-partner, gammasphere, prm]
---

# Sensharma 等（2020）：`187Au` longitudinal-wobbling 支持方实验

## Bibliographic Record

N. Sensharma et al., *Physical Review Letters* **124**, 052501 (2020)，DOI `10.1103/PhysRevLett.124.052501`。题名、作者、年份和 DOI 与只读 BibTeX 条目唯一匹配，使用 citation key `sensharma_2020_LongitudinalWobbling`。

## Scope and Reading Depth

全文精读，并视觉核对 Fig.2 的部分能级纲图、Fig.3 的 angular-distribution fits 与 mixing ratios、Fig.4 的 band energies/`E_wobb`，以及 Fig.5 的实验-PRM transition-ratio 比较。

本页建立 Sensharma 2020 对 `187Au` longitudinal-wobbling 的支持方证据链，不裁决后续低自旋 wobbling 争议。

## Summary

作者利用两次 ATLAS/Gammasphere 实验的合并数据研究 `187Au` 低自旋负宇称带。band (2) 到 yrast 的四条最低 connecting transitions 被 angular-distribution analysis 赋予约 88%-93% E2 admixture；新建 band (3) 到 yrast 的两条 links 几乎为纯 M1。作者将 band (2) 指认为 `n_w=1` longitudinal-wobbling band，将 band (3) 指认为 signature partner，并用随自旋增加的 `E_wobb` 与 PRM 比较支持该解释。

## Experimental or Theoretical Setup

- 富集 `174Yb` 靶为 `13 mg/cm²`，带 `33 mg/cm²` `208Pb` backing；
- 两次 `19F` 束流能量分别为 105 和 115 MeV；
- Gammasphere 分别使用 57 与 73 个 Compton-suppressed Ge detectors；
- 合并获得 `1.08×10^9` 个三重及更高重数 γ 符合事件；
- 以 RADWARE 建立 γ-γ matrices 与 γ-γ-γ cubes，并利用 17 个角度环进行 angular-distribution analysis；
- PRM 描述 `h9/2` proton 与 triaxial rotor 的耦合。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AU20-1 | 两次实验以 105/115 MeV `19F` 轰击带 `208Pb` backing 的富集 `174Yb` 靶；Gammasphere 分别有 57/73 个工作的 Ge detectors，合并得到 `1.08×10^9` 个 fold≥3 γ 符合事件。 | experimental-fact | direct | p.3, left column, experimental setup | false |
| AU20-2 | Fig.2 给出 yrast band (1)、此前被称为 unfavored signature partner 的 band (2)，以及本工作新建、以 `E_x=386.3 keV` 的 `11/2-` state 为带头的 band (3)。 | experimental-fact | direct | p.3, Fig.2 and surrounding text | false |
| AU20-3 | band (2) 通过六条 ΔI=1 transitions 衰变到 yrast；Fig.3(a-d) 分析其中最低的 376.3、461.8、544.3、639.3 keV 四条 links。 | experimental-fact | direct | pp.3-4, Figs.2-3 | false |
| AU20-4 | 四条最低 band (2)→yrast links 的 `δ` 为 `-2.67(7)`、`-2.98(+0.02/-0.03)`、`-3.44(3)`、`-3.72(+0.11/-0.12)`，E2 fractions 分别为 `87.7(+0.5/-0.6)%`、`89.9(1)%`、`92.2(1)%`、`93.3(4)%`。 | experimental-fact | direct | p.4, Fig.3(a-d) | false |
| AU20-5 | band (3) 通过 265.3、436.5 keV ΔI=1 transitions 衰变到 yrast；angular distributions 给出 `δ=-0.06(1)`、`-0.10(1)` 和约 0.4%、1.0% E2 admixture。 | experimental-fact | direct | pp.3-4, Figs.2-3(e,f) | false |
| AU20-6 | 新观察到 429.2 keV ΔI=2 crossover，连接 band (2) 的 `15/2-` level 与 band (3) 的 `11/2-` level；作者结合 in-band stretched-E2 与两条 SP→yrast pure-ΔI=1 links 进行 spin/parity assignment。 | experimental-fact | direct | pp.3-4, Fig.2 and paragraph below Fig.3 | false |
| AU20-7 | 333.8、413.7 keV 两条已知 yrast stretched-E2 transitions 的 angular-distribution fits 给出 `δ=-0.04(1)`、`-0.03(1)`，被用于检查分析方法。 | experimental-fact | direct | p.3 and p.4, Fig.3(g,h) | false |
| AU20-8 | 本文采用的区分判据是：wobbling→yrast ΔI=1 links 应有 collectively enhanced E2 component，而 signature-partner→yrast links 应主要为 M1；LW 的 `E_wobb` 预期随自旋增加。 | experimental-criterion | direct | pp.2-4, Eqs.1-3 and discussion; Figs.1,3-4 | false |
| AU20-9 | 由 Fig.4(d) 中实验 `E_wobb` 随自旋增加，作者把 band (1)/(2) 指认为 `n_w=0/1` longitudinal-wobbling pair。 | author-interpretation | direct | p.4, Fig.4(d) and surrounding text | false |
| AU20-10 | 作者把 band (3) 指认为 yrast 的 unfavored signature partner，依据是 265.3、436.5 keV links 几乎为纯 M1，并结合 band 内 stretched-E2 与 429.2 keV crossover。 | author-interpretation | direct | pp.3-4, Figs.2-3 and surrounding text | false |
| AU20-11 | PRM 使用 `β=0.23, γ=23°`、`Δ=0.88 MeV`、`λ=-1.32 MeV`、`J_0=38.0 ħ²/MeV`，以 single-j `h9/2` proton 为主；加入 `f7/2` 后其波函数 admixture 小于 5%。 | model-result | direct | p.4, right and left columns, PRM setup | false |
| AU20-12 | configuration-fixed CDFT 给出从 `I=9/2` 的 `(β,γ)=(0.28,22°)` 到 `I=29/2` 的 `(0.28,25°)`，作者据此认为 PRM 使用常形变近似合理。 | model-result | direct | p.4, right column, model setup | false |
| AU20-13 | PRM 较好再现三条带的总体能量趋势和增加的 `E_wobb`，但对 `E_wobb` 数值略有低估。 | model-result | direct | pp.4-5, Fig.4 | false |
| AU20-14 | 实验 LW→yrast 的 `B(E2)_out/B(E2)_in` 最大约 0.7，明显大于 SP→yrast；PRM 较好再现 E2 ratios，但高估 LW 的、低估 SP 的 `B(M1)_out/B(E2)_in`。 | model-result | direct | p.5, Fig.5 and surrounding text | false |
| AU20-15 | 论文以 half-filled `h9/2` shell 中准质子趋向沿 medium axis 的分类图景解释 longitudinal geometry；正文未给出逐自旋 angular-momentum-component 图。 | author-interpretation | direct | pp.1-2, Fig.1(c); p.4 PRM setup | false |

## Nuclear Structure Information

- [[187au-yrast-band]]：band (1)，作者作为 `n_w=0` 基带；
- [[187au-longitudinal-wobbling-band]]：band (2)，作者重新指认为 `n_w=1` LW；
- [[187au-signature-partner-band]]：新建 band (3)，作者指认为 unfavored signature partner。

## Authors' Interpretation

- band (1)/(2) 为 `n_w=0/1` longitudinal-wobbling pair；
- band (3) 为 associated signature partner；
- 增加的 `E_wobb`、E2-rich LW links 与 M1-dominated SP links 联合区分两类 excitation；
- `187Au` 被作者称为首个同时识别 associated signature partner 的 longitudinal-wobbling 案例。

以上为作者解释，不是本 Wiki 对低自旋 wobbling 争议的最终裁决。

## Model Results

- PRM 计算能量、`E_wobb`、`B(E2)_out/B(E2)_in` 与 `B(M1)_out/B(E2)_in`；
- CDFT/HFB-D1S 为形变输入提供比较；
- PRM 对 E2 ratios 较好，但对 M1 ratios 存在相反方向偏差；
- angular-momentum geometry 主要以 Fig.1 与 half-filled-shell 分类说明，未展示逐自旋分量。

## Competing Interpretations and Limitations

- 本文是 longitudinal-wobbling 支持方原始实验，后续 counter-source 尚未在 `187Au` project 中摄入；
- 完整 coincidence、spin/parity 与系统误差细节被留给 forthcoming publication；
- angular distributions 的效率修正、spin alignment、attenuation coefficients 等完整讨论未在本 PRL 展开；
- 未识别 `n_w≥2` bands；
- PRM 的形变、转动惯量、single-j truncation 与 state mixing 具有模型依赖；
- 本文未报告 connecting-transition linear polarization。

## Extracted Pages

- Nucleus: [[187au]]
- Bands: [[187au-yrast-band]], [[187au-longitudinal-wobbling-band]], [[187au-signature-partner-band]]
- Experiment: [[atlas-gammasphere-187au-f19-105-115mev]]
- Concepts: [[wobbling-motion]], [[longitudinal-wobbling]], [[signature-partner-bands]]
- Observables: [[multipole-mixing-ratio]], [[interband-e2-strengths]], [[wobbling-energy]]
- Method: [[gamma-gamma-coincidence]]
- Models: [[particle-rotor-model]], [[covariant-density-functional-theory]]
- Project: [[187au-longitudinal-wobbling-controversy]]

## Personal Notes

本页只建立 Sensharma 2020 支持方证据链。用户已审核 source 页面及 AU20-1 至 AU20-15，未发现问题；这不构成对后续 `187Au` 争议的裁决。

## Day18定量审计：纵向wobbling声称在内转换系数与线偏振判据下的塌缩

在Day18正式学习中对本文Fig. 3与Fig. 5中声称的187Au纵向wobbling跃迁强度进行对照审计，raw SHA256 `F348DCE9976AD076FD9B1D5281A728E0923053ACED33B0270F643D770729366A`已核。原SE20-1–12各claim及`human-reviewed`状态完全保留；新SE20-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SE20-D18-1 | 本文基于Gammasphere角分布拟合挑选大混合比解（delta ~ 2.6-3.0，E2份额87%-90%），报告B(E2_out)/B(E2_in)高达~0.70并声称核内首例“纵向wobbling”。结合已知带内跃迁极强集体性（1.49 e2b2 = 234.6 W.u.），该比值对应高达164.2 W.u.的超集体带间跃迁。然而后续Guo 2022与早期Bourgeois 1989内转换测量确立真实物理小解为delta = -0.10(5)（E2份额仅0.99%），使B(E2_out)暴跌88.0倍至仅1.87 W.u.，完全退化为单准粒子Nilsson能级间跃迁。本文对偏振测量的缺失和对角分布大解的盲目采纳制造了虚假的集体四极增强假象。 | task-rate-decomposition-audit | derived-and-boundary | PDF pp.3-5 Figs. 3, 5；新guo22-sensharma20-187au-result-022 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/guo22-sensharma20-187au-contract-022.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/guo22-sensharma20-187au-result-022.json)4项检查全过。
