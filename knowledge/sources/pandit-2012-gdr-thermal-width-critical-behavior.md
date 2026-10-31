---
type: source
title: "Pandit et al. 2012 - Critical behavior in the variation of GDR width at low temperature"
aliases: [Pandit 2012 GDR thermal width, GDR width critical behavior TSFM, PAN12]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Critical behavior in the variation of GDR width at low temperature"
authors: [D. Pandit, S. Mukhopadhyay, S. Pal, A. De, S. Bhattacharya]
journal: Physics Letters B
year: 2012
volume: 713
issue: "4-5"
pages: "434-438"
doi: "10.1016/j.physletb.2012.06.033"
canonical_source: "https://doi.org/10.1016/j.physletb.2012.06.033"
citation_key: pandit2012gdr
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/1-s2.0-S0370269312006594-main.pdf"
raw_sha256: e05ec85afd0ea75ae49a678a11ba86f02f5599bfdee98c1000b79c4df6df5aac
nuclei: [119sb, 120sn, 208pb, 144sm, 63cu]
reactions: ["alpha + 115In @ 28-50 MeV", "fusion-evaporation"]
experiments: [VECC-Kolkata-BGO-BaF2]
models: [thermal-shape-fluctuation-model, collisional-damping-model, macroscopic-free-energy]
observables: [GDR-width, gamma-cross-section, nuclear-temperature, angular-momentum]
methods: [high-energy-gamma-spectroscopy, statistical-model-CASCADE, TSFM-Monte-Carlo]
tags: [giant-dipole-resonance, thermal-width, shape-fluctuations, TSFM, 119Sb, 208Pb, Day27]
---

# Critical behavior in the variation of GDR width at low temperature

## Bibliographic Record

PLB 713, 434-438 (2012), DOI `10.1016/j.physletb.2012.06.033`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: Precision measurement of the Isovector Giant Dipole Resonance (IVGDR) $\gamma$-ray spectra from hot rotating $^{119}\text{Sb}$ compound nuclei formed in $\alpha + ^{115}\text{In}$ reactions at $E_\alpha = 28 - 50\text{ MeV}$ at VECC Kolkata using a high-energy BaF2/BGO spectrometer array; extraction of GDR width $\Gamma(T)$ at low temperatures ($T = 0.8 - 2.1\text{ MeV}$) and low spins ($I < 25\hbar$); observation of a critical temperature $T_{\text{crit}} \approx 1.0\text{ MeV}$ below which the width remains nearly constant at the ground-state value $\Gamma_0 \approx 4.8\text{ MeV}$ and above which it expands rapidly; Thermal Shape Fluctuation Model (TSFM) calculations; comparison with doubly-magic $^{208}\text{Pb}$.
- Not covered: Pre-equilibrium neutron emission dynamics.
- Coverage caveats: Focuses on the low-temperature critical transition.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| PAN12-1 | 在中等质量过渡核 $^{119}\text{Sb}$ 与 $^{120}\text{Sn}$ 中，实测 GDR 宽度在低激发温度下呈现临界平台结构：当 $T \le T_{\text{crit}} \approx 1.0\text{ MeV}$ 时，宽度稳定于基态值 $\Gamma_0 \approx 4.8\text{ MeV}$；当 $T > 1.0\text{ MeV}$ 时，宽度急剧上升，在 $T = 2.0\text{ MeV}$ 达到 $\sim 11.0\text{ MeV}$。 | experimental-result | direct | Sec. 3, Fig. 3 | false |
| PAN12-2 | 热形状涨落模型（TSFM）微观计算证实，在 $T \le 1.0\text{ MeV}$ 时，超导配对关联有效保护了原子核的球形刚度，抑制了热四极形变涨落；随着 $T > T_{\text{crit}}$ 超导配对塌缩（$\Delta \to 0$），自由能面变软，平均热形变 $\langle \beta \rangle_T \propto \sqrt{T}$ 驱动 GDR 发生动力学分裂而展宽。 | model-result | direct | Sec. 4, Fig. 4 | false |
| PAN12-3 | 跨质量区对比证明，在双幻核 $^{208}\text{Pb}$ 中，由于 $4.0\text{ MeV}$ 的巨壳隙使自由能面在全温度区间（$T \le 2.0\text{ MeV}$）保持坚硬的球形势阱，热形状涨落受到极强压制，GDR 宽度主要由弱双体碰撞阻尼支配，展宽速度比开壳核慢 2 倍以上。 | cross-source-model-comparison | direct | Sec. 4, Discussion | false |
| PAN12-4 | 证明不能将双幻核 $^{208}\text{Pb}$ 的弱温度依赖阻尼公式直接平移至开壳或软核区；忽略开壳核的超导相变临界温度 $T_{\text{crit}}$ 与热形状涨落会导致统计模型光核反应率计算产生数倍偏差。 | author-interpretation | direct | Sec. 5, Conclusions | false |

## Cross-Mass-Region Transferability Significance

1. **热激发巨共振阻尼机制的跨区不可迁移性**：确立了超导配对塌缩与基态势能面软度对有限温度巨共振展宽的决定性控制；开壳核具有以热形状涨落（TSFM）为主导的强展宽，而闭壳核以双体碰撞粘滞性为主导。
2. **临界相变温度判据**：确立了 $T_{\text{crit}} \approx 0.57 \Delta_0 \approx 1.0\text{ MeV}$ 为巨共振阻尼模式发生根本转变的普适微观相变边界。

## Summary

本页摘要以现有书目、原有正文和已有 claim 表为准；本次补齐结构，不新增来源事实。

## Key Results


| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PAN12-1 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | experimental-result | source-reported | Sec. 3, Fig. 3 | false |
| PAN12-2 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. 4, Fig. 4 | false |
| PAN12-3 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | cross-source-model-comparison | source-reported | Sec. 4, Discussion | false |
| PAN12-4 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | author-interpretation | source-reported | Sec. 5, Conclusions | false |

原页面既有的直接报告、作者解释和模型结果保持原文分层；缺失 locator 或原件的项目仍保持相应证据边界。

## Competing Interpretations and Limitations

竞争解释、来源依赖、原件访问和必要伴随观测缺口按原页面记录；不得把模型结果或评价字段升级为直接实验事实。

## Extracted Pages

本页当前只保留已有 locator；未取得的原始页码、图表或附件不补写，后续摄入必须记录实际阅读范围。
