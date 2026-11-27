---
type: source
title: "Das et al. 2020 - High spin states of 37Ar"
aliases: [Das 2020 37Ar high spin]
created: 2026-09-21
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: experiment-and-shell-model
reading_depth: deep-read
title_original: "High spin states of 37Ar"
authors: [Ananya Das, Abhijit Bisoi, M. Saha Sarkar, S. Sarkar, S. Ray, D. Pramanik, R. Kshetri, S. Nag, P. Singh, K. Selvakumar, A. Goswami, S. Saha, J. Sethi, T. Trivedi, B. S. Naidu, R. Donthi, V. Nanal, R. Palit]
journal: "Physical Review C"
year: 2020
volume: 101
pages: "044310"
doi: "10.1103/PhysRevC.101.044310"
citation_key: Das_2020
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Das et al., Phys. Rev. C 101, 044310 (2020)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/2020_Das et al_High spin states of Ar 37.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/2020_Das et al_High spin states of Ar 37.pdf"
raw_sha256: "b7c28e74a0c6a572a9c46642982c2d8b19a4ee643fc9f8f7be03aee8f13b6483"
nuclei: [37Ar, 36Ar, 38Ar]
reactions: [27Al-12C-np]
experiments: [INGA, Pixie-16, RDCO, RADO, IPDCO]
models: [large-basis-shell-model, sd-pf-cross-shell, two-level-mixing]
observables: [level-scheme, RDCO, RADO, IPDCO, mixing-ratio, configuration-mixing]
methods: [gamma-gamma-coincidence, DCO, ADO, linear-polarization]
tags: [37Ar, INGA, high-spin, level-scheme, shell-model, RDCO, IPDCO]
---

# High-spin states of `37Ar`

## Bibliographic Record

- A. Das *et al.*, *Phys. Rev. C* **101**, 044310 (2020), DOI `10.1103/PhysRevC.101.044310`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/2020_Das et al_High spin states of Ar 37.pdf`。

## Scope and Reading Depth

- PDF pp.044310-1–13 fully read: `27Al(12C,np)` at 40 MeV, 15-clover INGA/Pixie-16 analysis, RDCO/RADO/IPDCO definitions, level scheme to 10.5 MeV, Tables I–II, shell-model restrictions, two-level mixing and conclusion.
- Not covered: raw event list, full shell-model code and later evaluations.

## Key Results

- About `6×10^8` twofold coincidences were recorded with 15 clovers at six angles. The `37Ar` scheme was extended to 10.5 MeV with 18 new γ transitions and eight new levels (PDF pp.1–4, Fig.3, Tables I–II).
- DCO uses θ=157° gates and `σ/J=0.3`; pure dipole/pure quadrupole RADO references are approximately 0.8/1.7. IPDCO signs provide electric/magnetic character after the measured clover asymmetry correction (PDF pp.2–4, Eqs.1–6).
- New/confirmed assignments use combined observables: ten new δ values were extracted, several earlier E2 mixing ratios were simplified to pure E2, and Doppler-shifted peaks were handled with angle-independent matrices (PDF pp.3–6, Table I).
- Large-basis shell-model calculations with different sd/pf particle restrictions and a two-level mixing calculation are used to interpret single-particle versus multiparticle–multihole components; these are model interpretations of the observed scheme (PDF pp.7–12).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DA20-1 | `37Ar` level scheme is extended to 10.5 MeV with multimethod spin/parity evidence. | experiment-result | direct | PDF pp.1–6, Fig.3, Tables I–II | true |
| DA20-2 | `σ/J=0.3`, RADO reference values and clover calibration enter δ/IPDCO assignments. | method-boundary | direct | PDF pp.2–4 | false |
| DA20-3 | sd–pf shell-model restrictions and two-level mixing explain configuration content but do not directly measure shape. | model-result | mixed | PDF pp.7–12 | true |

## Summary

Das *et al.* provide a modern light-nucleus high-spin benchmark in which level placement, RDCO/RADO/IPDCO and δ are jointly used before shell-model interpretation. The source reinforces that alignment and detector calibration are part of the assignment evidence, while cross-shell configuration mixing remains a model layer.

## Competing Interpretations and Limitations

- RADO/RDCO thresholds depend on the INGA geometry, gate multipolarity and `σ/J`; low statistics and Doppler shifts can weaken assignments.
- Earlier pure-E2 versus mixed assignments may differ because of statistical fluctuations and limited ANGCOR branch resolution.
- Shell-model particle restrictions and two-level mixing are not direct deformation measurements and should not be transplanted to A≈130 without a model-space audit.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| DA20-AR-1 | Assignment chain | Coincidence scheme → RDCO/RADO/IPDCO/δ → spin/parity and multipolarity; retain weak/tentative branches. | PDF pp.2–6, Tables I–II | self-checking |
| DA20-AR-2 | Model chain | Level energies/transition strengths → restricted sd–pf shell-model and two-level mixing; model results are not measured shape. | PDF pp.7–12 | self-checking |
| DA20-AR-3 | Transfer condition | Recalibrate `σ/J`, angles and detector response before comparing to other INGA runs or nuclei. | PDF pp.2–4 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-correlation]], [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]] and light-nucleus method comparators.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `DA20-P0-1`: Preserve the INGA alignment/calibration and shell-model restriction boundaries; do not treat model configuration mixing as direct shape evidence.

## Extracted Pages

- Methods/observables: [[angular-distribution]], [[angular-correlation]], [[compton-polarimetry]], [[multipole-mixing-ratio]]。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"from": 1, "to": 4, "sections": "题录、§I–II、§III开头、式(1)–(6)、图1–3"}
- {"from": 5, "to": 8, "sections": "§III.A–C、表I–II、图4–6及§IV开头"}
- {"from": 9, "to": 12, "sections": "§IV截断空间、组态和两能级混合、图8、表III–VII、§V、致谢和参考文献开头。图7在第8页"}
- {"from": 13, "to": 13, "sections": "参考文献[11]–[36]"}
- 本次获取的具体覆盖：逐页读取物理PDF第1–13页所给文本，从实验与结果段落追到模型、结论和参考文献。图的使用限于图注、可读标签和正文交叉引用，未目视核验。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A17-1 | 40 MeV的¹²C束在²⁷Al靶上经np蒸发道布居³⁷Ar，15台INGA clover记录约6×10⁸个双重符合事件。作者报告新增18条γ跃迁和8个能级，达到10574 keV。 | experiment-result | source-reported | 物理PDF第2页§II、第3–4页§III、图3及第5–6页表I–II。图3中新线、虚线及括号归属待第4页目视核对。 | true |
| A17-2 | 作者用R_DCO与ANGCOR提取δ，并按Krane–Steffen约定报告1192和1574 keV跃迁的δ分别为+0.14(6)和+0.47（+0.10/−0.09）。文中以相位约定及用旧δ回算R_DCO的结果讨论符号差异。 | experimental-inference | source-reported | 物理PDF第2–3页式(1)–(6)、第5页表I、第7页§III.A。 | true |
| A17-3 | 作者据完全多普勒移位且无停止分量的谱线，结合Au背衬约430 fs的计算停止时间，为六个能级估计寿命上限。表VI对其中四级另给壳模型计算寿命。 | experimental-inference | source-reported | 物理PDF第7页图5、第10–11页§IV.C及第11页表VI。谱峰有无停止分量待第7页目视核对。 | true |
| A17-4 | Pos-2的2p–2h计算把15/2⁺至21/2⁺的yrast能量重现到约250 keV以内。两能级拟合估得yrast 9/2⁺、11/2⁺、13/2⁺中的0p–0h份额分别为14%、21%、4.5%，另列第二个11/2⁺为4.8%。这四项是给定模型下的组态估计。 | model-result | source-reported | 物理PDF第8–9页图7及§IV.A、第10页表III、第11–12页§IV.D和表VII。第8页图7的图内宇称字符缺失，表III和表VII提供交叉定位。 | true |

R_DCO使用157°与90°互换观测轴和符合门，并依赖门跃迁的多极性及δ。ANGCOR采用σ/J = 0.3。此阵列的纯偶极与四极R_ADO参照约为0.8与1.7。Δ_IPDCO依赖clover几何不对称修正，ΔJ = 0时电磁判据的符号反转，混合跃迁还依赖混合程度。第3页式(3)–(4)的平行分量字符和个别Δ在提取中损坏，公式入库前须核字。

- 将Wiki的“DCO uses θ=157° gates”改为“式(1)在157°和90°交换观测与设门角，门跃迁的多极性和δ已知”。在偏振说明补入第3页ΔJ = 0符号反转及混合跃迁限制。
- 将Wiki所称以角度无关矩阵处理多普勒移位峰改为“用90°×90°对称矩阵测移位峰相对强度及辅助放置，用角度无关矩阵的1611 keV门谱中1508 keV强度归一”。依据物理PDF第4、7页。18条跃迁和8个能级的表定位改为第5页表I及第6页表II，能级图在第4页图3。
- Wiki若收录逐条δ，应保留原文异文。物理PDF第7页对521及937 keV所引旧δ为0.50及0.31，第5页表I旧值栏为−0.03(10)及−0.14(3)。第11页正文对2019 keV写实验δ = 0.01(5)，第5页表I写−0.01（+0.09/−0.11）。逐页核字并标明出处。
