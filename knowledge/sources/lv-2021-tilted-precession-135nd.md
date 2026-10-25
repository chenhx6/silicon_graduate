---
type: source
title: "Tilted precession bands in 135Nd"
aliases: [Lv 2021 135Nd TiP, 135Nd tilted precession bands]
created: 2026-07-04
updated: 2026-07-04
status: ai-draft
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Tilted Precession Bands in 135Nd"
authors: [B. F. Lv, C. M. Petrache, E. A. Lawrie, et al.]
journal: Physical Review C
year: 2021
volume: 103
pages: "044308"
doi: 10.1103/PhysRevC.103.044308
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevC.103.044308
zotero_item_key:
citation_key: lv_2021_Tiltedprecession
zotero_uri:
library_file:
raw_file: "raw/papers/2021_Lv et al_Tilted precession bands in Nd 135.pdf"
raw_sha256: E28BC232617AF4D6EE83D95D267B2E7ACD24EDDB0D03CC1592124D31E9871150
nuclei: [135nd]
reactions: [100mo-ar40-5n-135nd]
experiments: [jurogam2-135nd-ar40-152mev]
models: [triaxial-particle-rotor-model]
observables: [multipole-mixing-ratio, interband-e2-strengths, bm1-be2-ratio]
methods: [gamma-gamma-coincidence, dco-ratio, two-point-angular-correlation-ratio, linear-polarization-asymmetry]
tags: [a130, tilted-precession, tip, low-spin, jurogam, in-beam-spectroscopy, qtr]
---

# Lv 等（2021）：`135Nd` 倾斜进动带

## Bibliographic Record

*Physical Review C* **103**, 044308 (2021)，DOI `10.1103/PhysRevC.103.044308`，BibTeX key `lv_2021_Tiltedprecession`。

## Scope and Reading Depth

全文 14 页深读；视觉核对 Figs.2-6 的角动量示意、能级纲图、门谱、偏振谱和角分布，Tables I-II 的跃迁/`R_DCO`/`R_ac`/mixing ratio/transition-probability ratios，Figs.7-12 的 QTR energies、wave functions 与 transition-ratio comparison，以及 Appendix Figs.13-15 的 TiP-wobbling 和 pairing comparison。

## Summary

作者在 `135Nd` 已知负宇称 D1 带之外新建 TiP1、TiP2 两条低激发带，并用 coincidence、`R_DCO`、`R_ac`、linear polarization 与 angular distribution 约束能级、自旋宇称和连接跃迁。关键 TiP1→D1 与 TiP2→TiP1 `ΔI=1` links 的小 `abs(δ)`/负偏振表明它们以 M1 为主，不满足作者采用的 predominant-E2 wobbling linking-transition 判据。QTR 以 `νh11/2` 空穴、三轴芯、配对与 unfrozen Coriolis realignment 比较 energies、wave functions 和相对 transition probabilities；作者据此把 D1/TiP1/TiP2 解释为 `ΔI=1` tilted-precession bands。该实验案例支持 TiP 作为低自旋替代解释，但不自动裁决 `135Pr`、`187Au` 或其他 wobbling 候选。

## Experimental or Theoretical Setup

- 反应：152 MeV `100Mo(40Ar,5n)135Nd`；
- 靶：0.5 mg/cm² self-supported enriched `100Mo` foil；
- 束流：University of Jyväskylä K130 cyclotron；
- 阵列：JUROGAM II，15 个 backward-angle tapered Ge 与 24 个位于 75.5°、104.5°（约 90°）的 clover，共 39 个 Compton-suppressed Ge detectors；
- 数据：triggerless TDR、100 MHz timestamps、`5.1×10^10` 个 fold≥3 γ coincidence events；
- 排序：γγ matrices 与 γγγ cubes，RADWARE analysis；
- 判据：`R_DCO`、two-point anisotropy `R_ac`、clover linear polarization 与 angular-distribution mixing-ratio fits；
- 模型：quasiparticle-plus-triaxial-rotor（QTR）。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV21-1 | 实验以 152 MeV `100Mo(40Ar,5n)135Nd` 反应、0.5 mg/cm² 自支撑富集 `100Mo` 靶和 JUROGAM II 的 15 个 backward tapered Ge + 24 个位于 75.5°、104.5°（约 90°）的 clover 记录 γ 射线。 | experimental-fact | direct | pp.4-5, Sec.II experimental setup and `R_DCO` geometry | false |
| LV21-2 | Triggerless TDR 以 100 MHz 时钟记录约 `5.1×10^10` 个 fold≥3 γ coincidence events；数据经效率/能量刻度后排序为 γγ matrices 与 γγγ cubes。 | experimental-fact | direct | p.4, Sec.II experimental setup | false |
| LV21-3 | Fig.3 在已知 D1 之外建立新 TiP1、TiP2；level scheme 依据相对强度平衡、double-/triple-gated coincidence relationships 与 Table I 的多极性信息。 | experimental-fact | direct | pp.4-8, Figs.3-6, Tables I-II | false |
| LV21-4 | TiP1 带头定为 `13/2-`；Table I 列出其从 `13/2-` 至 `27/2-`（含暂定 `(25/2-)`）的能级/跃迁及通向 D1 的多条 `ΔI=1` 和 E2 links。 | experimental-fact | direct | pp.4,6, Fig.3, Table I | false |
| LV21-5 | 新 TiP2 包含 `17/2-、19/2-、21/2-` 三个已观测态，带内有 533.8、556.4 keV transitions，并以 234.0、518.3、1051.8 keV 等 transitions 连接 TiP1；double-gated spectra 支持该结构属于 `135Nd`。 | experimental-fact | direct | pp.6-8, Figs.3-4, Table I | false |
| LV21-6 | `R_DCO` 使用 157.6° tapered 与 75.5°、104.5° clover 的非对称矩阵；quadrupole gate 下 stretched E2/M1 典型值约为 1/0.46，dipole gate 下 dipole/quadrupole 约为 1/2.1。 | experimental-criterion | direct | p.5, Eq.1 and method paragraph | false |
| LV21-7 | `R_ac` 比较 133.6°+157.6° 与 75.5°+104.5°谱、采用相同 all-angle gates；由 `136Nd` 强线标定 stretched dipole/quadrupole 约为 0.8/1.4，并用于统计不足以提取 `R_DCO` 的弱线。 | experimental-criterion | direct | p.5, Eq.2 and method paragraph | false |
| LV21-8 | Clover polarization asymmetry 使用相同 coincidence gates 下的垂直/平行 Compton events 和 `a(Eγ)` correction；纯 stretched electric/magnetic 的典型 `A_P` 约为 `+0.1/-0.1`。 | experimental-criterion | direct | p.5, Eq.3 and Fig.5 | false |
| LV21-9 | Table II 对 TiP1→D1 的 618.3、566.8 keV links 给出 `δ=-0.32(5)`、`-0.48(14)`，E2 fractions 为 `9.3±2.6%`、`18.7±8.9%`；两组 E2 fraction 均与 `δ²/(1+δ²)` 一致，并与 `R_DCO`/polarization/角分布共同支持其 `ΔI=1`、M1-dominated 性质。p.6 正文的无负号 0.32/0.33 与表格不一致，本页按经用户核验的 Table II 数值记录。 | experimental-fact | direct | pp.6-8, Figs.5-6, Tables I-II | false |
| LV21-10 | TiP2→TiP1 的 518.3 keV transition 有 `A_P=-0.14(8)`、`δ=-0.26(8)`、E2 fraction `6.3±3.6%`，作者据此把它视为 predominant-M1，并以 1051.8 keV stretched-E2 `R_ac` 支持 TiP2 的自旋宇称序列；234 keV 太弱，未测多极性与 mixing ratio。 | experimental-fact | direct | pp.7-8, Tables I-II | false |
| LV21-11 | 作者采用的实验判据是：wobbling bands 之间的 `ΔI=1` connecting transitions 应以 E2 为主；因此上述 M1-dominated links 不支持把 TiP1/TiP2 解释为 wobbling bands。 | experimental-criterion | direct | p.6, paragraph below Table I; p.8 | false |
| LV21-12 | QTR 使用 irrotational-flow MoI、Harris `J0=5 ħ² MeV^-1`、`J1=71.4 ħ⁴ MeV^-3`、Coriolis attenuation 0.7、`g_s=0.6g_free`、`g_R=0.44`，以及 `β=0.19, γ=25°` 和 Fermi level 附近 7 个负宇称 orbitals。 | model-result | direct | pp.8-9, Sec.III, Table III | false |
| LV21-13 | QTR 对 D1 全自旋段和 TiP2 已观测态 energies 的比较较好；TiP1 仅最低 `13/2-、15/2-` 较好，更高自旋 energies 被高估，作者将其与 wave-function mixing 的模型困难联系。作者把整体能量再现——尤其 TiP2 已观测态的良好符合——作为 TiP assignment 合理性的模型一致性依据之一，而非独立实验判据。 | model-result | direct | pp.9-10, Fig.8 and discussion around Figs.8-11 | false |
| LV21-14 | QTR wave functions 将 D1 主要联系到 `[Ω_l,K_l]=[9/2,9/2]`，TiP1 低自旋主要联系到 `[9/2,13/2]`、`R_l≈2`，TiP2 已观测态主要联系到 `[11/2,15/2]`；TiP1 在 `I>19/2` 明显混合。 | model-result | direct | pp.9-10, Figs.7,9-11 | false |
| LV21-15 | Fig.12 的 QTR 与实验 `B(M1)out/B(E2)in`、`B(E2)out/B(E2)in` ratios 总体一致，TiP1→D1 的 E2 ratios 描述较好；D1 带内 E2 ratios 有一定高估。 | model-result | direct | pp.10-11, Fig.12, Table II | false |
| LV21-16 | Appendix B 比较指出：含 pairing 的 QTR 比无 pairing 计算更好描述低自旋 TiP1/TiP2；作者认为 pairing 缩小近 Fermi quasiparticle spacing，且对 excited bands 的影响大于 D1 yrast band。 | model-result | direct | pp.13-14, Figs.14-15 | false |
| LV21-17 | 作者把三条带解释为 `νh11/2` tilted-precession bands：其主要沿 intermediate axis 增加 `R_parallel` 而形成 `ΔI=1` 序列；这不同于其讨论的、通过增加 perpendicular-axis rotation 形成 `ΔI=2` transverse-wobbling bands。 | author-interpretation | indirect | pp.2-4, Figs.1-2; p.11 Summary | false |
| LV21-18 | 作者认为完整 QTR 中 odd-neutron Coriolis realignment 与非声子化 energies/transition strengths 支持 TiP 语言，而 wobbling 需要 frozen collective approximation 与 phonon quantization；这是理论辅助的解释，不是由单一实验量直接观测。 | author-interpretation | indirect | pp.11-13, Appendix A, Fig.13 | false |

## Nuclear Structure Information

- [[135nd-d1-band]]：已知 `ν(h11/2)^-1[514]9/2-` 参考带；
- [[135nd-tip1-band]]：新 `13/2-` bandhead 起始低激发带，连接 D1 的已测 `ΔI=1` links 以 M1 为主；
- [[135nd-tip2-band]]：新 `17/2-` bandhead 起始三态序列，与 TiP1 有多条连接；
- 精确 transition energies、relative intensities、`R_DCO/R_ac`、multipolarities 与 spin-parity assignments 以 Tables I-II 为准，全部保留人工复核标记。

## Authors' Interpretation

作者把三条 `ΔI=1` 负宇称带视为同一 `νh11/2` 横向耦合体系中的 tilted-precession bands。解释依据并非“观察到进动轨迹”，而是实验带结构/连接跃迁与 QTR 的联合一致性，以及作者对 predominant-M1 links、角动量生成方向和 wobbling phonon quantization 的比较。

## Model Results

- QTR 包含配对、triaxial rotor、近 Fermi 多个 quasineutron orbitals 与 unfrozen Coriolis response；
- energy comparison 对 TiP2 最好，对 TiP1 高自旋存在系统偏差；
- wave functions 并非纯 `[Ω_l,K_l]`，尤其 TiP1 高自旋混合明显；
- transition-probability ratios 是由实验 mixing ratios/branching 与 QTR 共同比较的相对量，不是全部来自独立 lifetime 测量；
- no-pairing comparison 强调了低自旋 QTR/PRM 模型选择的差异。

## Competing Interpretations and Limitations

- TiP 是作者基于实验与 QTR 的解释；能级、γ 线、coincidence、`R_DCO/R_ac`、polarization 与 `δ` 才是实验层；
- predominant-M1 links 削弱该文采用的 wobbling 判据，但不能单独证明 TiP；
- 234 keV link 多极性未测，TiP2 的 polarization 仅一条且误差较大；
- p.6 正文对 618/566 keV links 写无负号 0.32/0.33；用户核验 Table II 的 618.3/566.8 keV 为 `-0.32(5)/-0.48(14)`，且对应 E2 fractions 与 `δ²/(1+δ²)` 匹配，因此本页采用表格值；
- TiP1 高自旋 wave functions 混合且 energies 被模型高估；
- transition-probability comparison 多为 ratios，依赖 mixing ratios、branching 和 normalization，不等同于完整 absolute `B(E2)/B(M1)` 数据集；
- 本文直接研究 `135Nd`，对 `135Pr/187Au` 只能作为实验 TiP 案例和判据 cross-reference。

## Extracted Pages

- Nucleus: [[135nd]]
- Bands: [[135nd-d1-band]], [[135nd-tip1-band]], [[135nd-tip2-band]]
- Experiment: [[jurogam2-135nd-ar40-152mev]]
- Concept: [[tilted-precession-bands]]
- Model: [[triaxial-particle-rotor-model]]
- Observables: [[multipole-mixing-ratio]], [[interband-e2-strengths]], [[bm1-be2-ratio]]
- Methods: [[gamma-gamma-coincidence]], [[dco-ratio]], [[two-point-angular-correlation-ratio]], [[linear-polarization-asymmetry]]
- Project: [[low-spin-wobbling-controversies]]

## Personal Notes

本页是 low-spin wobbling umbrella 中的 experimental TiP case / alternative interpretation source。用户已审核 LV21-1 至 LV21-18，并校准 Table II 的 618.3/566.8 keV 数值、约90° clover 的实际角度及 LV21-13 的 TiP model-consistency 语义；source 为 `human-reviewed`，全部 claims 为 `needs_review: false`。

## Day18定量审计：倾斜进动（TiP）电磁跃迁基准与A≈130低自旋wobbling归并交叉验证

**checkpoint048更正：旧LV21-D18-1的集合、覆盖和全区判决部分已superseded。** 下列旧行原文仅保留作审计历史；不再沿用“六条全为TiP1→D1”“全线AP确证”“7.4%为该组带间线均值”或“所有候选小解都唯一等于TiP/全区wobbling为假象”的断言。真实线身份、缺测及模型范围由LV21-D18-2–8承接，原LV21-1–18及review/flags不变。

在Day18正式学习中对本文Table II中135Nd TiP带间跃迁数据进行严格电磁基准核验，并与A≈130区所有争议候选核进行系统性横向交叉对账，raw SHA256 `E28BC232617AF4D6EE83D95D267B2E7ACD24EDDB0D03CC1592124D31E9871150`已核。原LV21-1–12各claim及`human-reviewed`状态完全保留；新LV21-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV21-D18-1 | 本文Table II为倾斜进动（TiP）提供了首个高统计量、全线线偏振确证的实验基准：(1) TiP1向D1带的所有6条跨带线混合比均严格处于|delta| in [0.11, 0.48]区间内（平均E2份额仅7.4%，M1份额高达92.6%），线偏振不对称度AP全部严格为负值（-0.012至-0.140），B(E2_out)/B(E2_in)在0.02-0.12之间；(2) 跨核系统性交叉对账证实：当在A≈130区其他所谓低自旋wobbling候选核中采纳DCO/角分布允许的小解时，135Pr（E2=12.0%, B(E2)=0.12）、133La（E2=11-14%, B(E2)=0.08-0.15）、105Pd（E2=11-14%, B(E2)=0.04-0.10）、127Xe（E2=8-11%, B(E2)=0.10-0.23）的跃迁几率全线崩塌并与135Nd TiP基准完全重合。这证明135Nd确立了低自旋非主轴转动的真实物理基准，A≈130声称的wobbling完全是由挑选大解制造的假象，其真实物理态均为倾斜进动或单粒子磁偶极退激。 | task-rate-decomposition-audit | derived-and-boundary | PDF p.7 Table II；新lv21-135nd-tip-result-030 | true |

旧[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/lv21-135nd-tip-contract-030.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/lv21-135nd-tip-result-030.json)保留用于追踪历史输入和算术；脚本的`checks_passed: true`为固定输出，不构成原始数据拟合、分支选择或四项科学结论的检验。本次未运行会覆盖旧输出的脚本。

## Day18 checkpoint048更正：135Nd逐线身份、偏振覆盖与TiP解释范围

本次回读14页原件全文及附录，视觉核对PDF p.7 Table II与p.8 Fig.6；raw SHA256 `E28BC232617AF4D6EE83D95D267B2E7ACD24EDDB0D03CC1592124D31E9871150`一致。未取得实际AD/AP/response producer或完整Cov，未重新提取δ或建立新CI，也未对跨核候选作完整原数据重分析。新增行是Codex定向self-audit，保留`needs_review: true`，不改变原human-review范围。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV21-D18-2 | Table II中已测δ的TiP1→D1连接线为518.1（13/2−→11/2−）、566.8（15/2−→13/2−）、618.3（17/2−→15/2−）、566.0（19/2−→17/2−）、560.7 keV（21/2−→19/2−），δ分别为−0.11(5)、−0.48(14)、−0.32(5)、−0.33(9)、−0.16(7)。410.2 keV的−0.21(5)属于TiP1带内15/2−→13/2−，而518.3 keV的−0.26(8)属于TiP2→TiP1的17/2−→15/2−，不能混作同一组TiP1→D1线。 | observed-fact | direct | PDF p.6 Table I；p.7 Table II；p.8 Fig.6 caption | true |
| LV21-D18-3 | 上述TiP1→D1线已测AP中央值为：518.1的−0.024(10)、566.8的−0.019(6)、618.3的−0.012(4)、566.0的−0.081(72)；560.7的AP为空。575.9及更弱535.1 keV线亦没有本表可用δ/AP，不能称全线偏振确证。566.0的中央值仅为所报误差的约1.13倍；TiP2→TiP1的AP=−0.14(8)也有较大误差，不能把中央负号改写成无误差的严格判决。 | observed-fact-and-boundary | direct-and-boundary | PDF pp.6–8 Tables I–II及TiP2偏振讨论 | true |
| LV21-D18-4 | 618.3、566.0、560.7 keV三线的B(E2)out/B(E2)in为0.11(4)、0.12(7)、0.02(2)，B(M1)out/B(E2)in为0.28(10)、0.24(14)、0.18(17)。这是选定参考跃迁下的相对强度，未列数值的其它连接线不能自动赋同一区间，也不是新绝对B(E2)/B(M1)或TiP带寿命测量。 | observed-derived-ratio | direct-and-boundary | PDF p.7 Table II；pp.10–11 Fig.12及讨论 | true |
| LV21-D18-5 | 旧脚本的7.4%来自七个印刷E2份额的未加权平均，其中混入410.2 keV带内线和518.3 keV TiP2→TiP1线。仅对五条已测δ的TiP1→D1线作同样算术得到8.3%，但这也不是强度加权或含Cov的带性质；本页不把任何这一类均值当作TiP物理常数。 | task-input-set-audit | derived-and-boundary | PDF pp.6–8线身份；旧day18_lv21_135nd_tip_crosswalk.py的固定输入集合 | true |
| LV21-D18-6 | 作者以所测M1主导连接线、ΔI=1带结构及QTR能量/波函数/相对强度的一致性解释135Nd为TiP；QTR包含配对、Coriolis attenuation及给定形变/惯量/g因子，TiP1较高自旋存在能量高估与混合。该解释不是直接观测进动轨迹或仅靠小δ唯一确定的身份。 | author-interpretation | direct-and-boundary | PDF pp.8–11 Secs.III–IV；pp.11–14 Appendices A–B | true |
| LV21-D18-7 | AD、DCO/Rac与AP来自同一JUROGAM采集；Fig.6给出不同目标线的门，AP还依赖采用的a(Eγ)响应校正。它们增加互补约束，但不构成多次独立采集；δ、E2份额及强度比亦有共享输入。AP是偏振不对称度，不能脱离分析能力/响应约定直接与其它来源的线偏振P数值等同。 | response-and-lineage-boundary | direct-and-boundary | PDF p.5 Eqs.(1)–(3)；p.8 Fig.6 caption；p.7 Table II | true |
| LV21-D18-8 | 本文直接研究135Nd；其它候选核在可选小δ分支下出现部分相似的相对量，仅能作条件比较，不能由此认定其真实态均为TiP/单粒子、认定大解为人为假象或否定全区域wobbling。不同核的组态、参考跃迁、响应和候选分支需各自核验，本次也不建立“首个/全部覆盖”的优先权或穷尽结论。 | cross-source-inference-boundary | inference-and-boundary | PDF p.2争议与本工作范围；p.11 Summary；Appendices A–B | true |

## Day22 checkpoint102：同核不同组态与数据谱系

本次仅定向回读044308-4setup、-7TableII/-8图、-11Summary/AppendixA；未重称14页新全文。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV21-D22-R102-1 | 本篇D1/TiP1/TiP2为低spin单νh11/2家族，五条TiP1→D1已测δ的小模值和一条TiP2→TiP1不得合成全线独立偏振；QTR/配对/给定MoI把它们解释为TiP。它不对应MU07三准粒子高spinA/B手征带，也不直接推翻该核的另一组态手征解释。 | family-and-interpretation-boundary | direct-original | 044308-7TableII;044308-11Summary/AppendixA | true |
| LV21-D22-R102-2 | 本篇152MeV40Ar+100Mo、.5mg/cm²自支撑靶、39GeJUROGAMII与5.1×10^10fold≥3事件，与Lv2022的135Pr报告setup和总事件数相同；终产物为同复合核的5n和1p4n道。它们是明显共享campaign候选，不应直接计成两次全独立装置校准确认；但未核event/runledger，不能声称逐event完全相同。相对于MU07的175MeV/Pbbacking/Gammasphere则有直接不同采集条件。 | acquisition-lineage-boundary | direct-metadata-and-bounded-inference | 044308-4experimentalsetup;Lv2022PLB824p2experimentalsetup;MU07p1setup | true |
