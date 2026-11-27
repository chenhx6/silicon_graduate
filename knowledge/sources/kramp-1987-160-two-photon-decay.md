---
type: source
title: "Kramp et al. 1987 - Nuclear two-photon decay in 0+ to 0+ transitions"
aliases: [Kramp 1987 two-photon decay]
created: 2026-09-21
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: experiment-and-theory
reading_depth: deep-read
title_original: "Nuclear two-photon decay in 0+ → 0+ transitions"
authors: [J. Kramp, D. Habs, R. Kroth, M. Music, J. Schirmer, D. Schwalm, C. Broude]
journal: "Nuclear Physics A"
year: 1987
citation_key: "kramp_1987_16o-two-photon"
volume: 474
pages: "412-450"
pii: "0375-9474(87)90625-7"
canonical_source: "Kramp et al., Nucl. Phys. A 474, 412-450 (1987)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/electromagnetic/1987_Kramp et al_Nuclear two-photon decay in 0+→0+ transitions.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/electromagnetic/1987_Kramp et al_Nuclear two-photon decay in 0+→0+ transitions.pdf"
raw_sha256: "be1b792e5b3e47a50e177a3ec48f7fbb605ae4db0d8af8f6ec2c60cdf9388413"
nuclei: [16O, 40Ca, 90Zr]
reactions: [16O-proton-scattering]
experiments: [Heidelberg-Darmstadt-crystal-ball, two-photon-coincidence, linear-polarization]
models: [second-order-QED, two-level-polarizability, E1-M1-interference]
observables: [two-photon-branching, energy-sharing, angular-correlation, linear-polarization, matrix-element-ratio]
methods: [Crystal-Ball, particle-gamma-coincidence, gamma-gamma-correlation]
tags: [two-photon-decay, 16O, E1, M1, polarizability, Crystal-Ball]
---

# Nuclear two-photon decay in `0+→0+` transitions

## Bibliographic Record

- J. Kramp *et al.*, *Nucl. Phys. A* **474**, 412–450 (1987), PII `0375-9474(87)90625-7`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/electromagnetic/1987_Kramp et al_Nuclear two-photon decay in 0+→0+ transitions.pdf`。

## Scope and Reading Depth

- PDF pp.412–450 (39 pages) fully read: second-order two-photon theory, Crystal-Ball/particle setup, `16O` energy-angle matrices, PAF/background rejection, branching ratio, polarization, `E1/M1` interference, comparison with `40Ca/90Zr` and Appendix S-matrix/polarizability formalism.
- Not covered: raw event matrices and later two-photon reanalyses.

## Key Results

- The `16O` first excited `0+` state at 6.05 MeV was populated with `7.58-MeV` proton scattering, favoring the `0+` state over the nearby `3−` state by about 16:1. A Heidelberg–Darmstadt 4π Crystal Ball with particle coincidence separates true two-photon decay from Compton and positron-annihilation-in-flight backgrounds (PDF pp.412–418).
- The measured two-photon branching ratio is `Γ2γ/Γtot=(6.6±0.5)×10^-4` for `16O`; the full energy-sharing/angle matrix and event-selection checks establish the candidate branch (PDF pp.417–424, 427–431).
- The angular correlation contains an interference term proving comparable `2E1` and `2M1` amplitudes. The ratio `αE1/χ` is restricted to two inverse solutions, approximately `−6.2±1.5` or `−0.16±0.04`, and linear polarization selects the dominant branch (PDF pp.431–438, 441–447).
- The authors compare `16O`, `40Ca` and `90Zr` through electric polarizabilities and magnetic susceptibilities in a two-level spherical/deformed basis; this gives qualitative/partial quantitative understanding but remains model dependent (PDF pp.447–450, Appendix A).
- Two-photon decay is a second-order QED process with resonance and seagull amplitudes constrained by gauge invariance; they are not separately measurable mechanisms (PDF pp.413–414, Appendix A).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KR87-1 | `16O` `0+→0+` two-photon branching is `(6.6±0.5)×10^-4`. | decay-result | direct | PDF pp.417–438 | true |
| KR87-2 | Angular-correlation interference establishes comparable `2E1` and `2M1` amplitudes with inverse matrix-ratio branches. | matrix-element-result | direct | PDF pp.431–447 | true |
| KR87-3 | Crystal-Ball particle/energy/angle controls separate true 2γ decay from Compton/PAF backgrounds. | method-result | direct | PDF pp.414–431 | false |
| KR87-4 | Polarizability/susceptibility interpretation is a two-level model layer, not a direct measurement of shape. | model-boundary | mixed | PDF pp.447–450, Appendix A | false |

## Summary

Kramp *et al.* establish a careful `16O` two-photon decay measurement and demonstrate that angular correlations and linear polarization reveal interference between `2E1` and `2M1` amplitudes. The source is a direct methodological precursor to modern two-photon nuclear-decay work, with explicit background, branch and model boundaries.

## Competing Interpretations and Limitations

- The two inverse `αE1/χ` branches arise from the angular-correlation fit; polarization and prior model information are needed to choose one.
- PAF and Compton backgrounds can mimic two-photon energy sums; the Crystal-Ball and proton-gate controls are part of the claim.
- The two-level polarizability/susceptibility interpretation depends on spherical/deformed basis mixing and cannot be generalized without nucleus-specific structure input.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| KR87-AR-1 | Event chain | Proton gate → Crystal-Ball two-γ energy/angle → PAF/Compton rejection → branching ratio. | PDF Secs.2–3 | self-checking |
| KR87-AR-2 | Amplitude chain | Second-order E1/M1 amplitudes → angular interference/polarization → inverse matrix-ratio branches. | PDF Sec.3, Appendix A | self-checking |
| KR87-AR-3 | Transfer condition | Use common phase, background and multipole decomposition before comparing with 40Ca/90Zr/Freire/Walz sources. | PDF pp.431–450 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[two-photon-nuclear-decay]], [[compton-polarimetry]], [[linear-polarization-asymmetry]] and the two-photon experimental lineage.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `KR87-P0-1`: Preserve PAF/Compton rejection and the inverse `E1/M1` branch; do not merge two-photon matrix ratios across nuclei without phase/background mapping.

## Extracted Pages

- Concept/methods: [[two-photon-nuclear-decay]], [[compton-polarimetry]], [[linear-polarization-asymmetry]]。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"pdf_pages": [1, 2], "sections": "首页与 §1 引言，含图1的振幅分类"}
- {"pdf_pages": [3, 5], "sections": "§1 末段及 §2 实验方法和装置，含图2–3"}
- {"pdf_pages": [6, 15], "sections": "§3.1–3.5 粒子谱、能量与角关联、偏振、分支比，含图4–10、表1及 §4 开头"}
- {"pdf_pages": [16, 23], "sections": "§4 两态混合与三核比较，含表2–3、图11及 §5 开头"}
- {"pdf_pages": [24, 37], "sections": "§5 结尾、致谢、附录 A.1–A.4，含图12及方向与偏振关联推导"}
- {"pdf_pages": [38, 39], "sections": "附录 A 末段、附录 B 内转换与内对产生、参考文献 [1]–[53]"}
- 本次获取的具体覆盖：逐页阅读 PDF 1–39 的正文、可读图题、表项、附录及参考文献。覆盖由各节原文确认。图像、曲线、误差棒和受损公式排版未作视觉核验。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A18-1 | 以 7.58 MeV 质子非弹性散射布居 ¹⁶O 的 6.05 MeV 0₂⁺ 态，其布居约为邻近 6.13 MeV 3⁻ 态的 16 倍。作者用质子门、两光子的能量差和夹角抑制串散射及飞行中正电子湮灭。图10峰区的 615 个事件扣除 28 个偶然符合后，经效率和切选校正，得到 Γ₂γ/Γtot = (6.6 ± 0.5) × 10⁻⁴。 | 报告的实验结果 | source-reported | PDF 6–7（印刷 417–418）图4与 §3.1，PDF 9–10（420–421）图7与 §3.3，PDF 13–15（424–426）图10、式(4)、表1 | true |
| A18-2 | 两光子方向关联呈前后不对称。纯偶极混合拟合得到 cos θ₁₂ 项系数 −0.63 ± 0.13，作者将其归于 2E1 与 2M1 干涉。α_E1/χ 有两个互为倒数的解，约 −6.2 ± 1.5 与 −0.16 ± 0.04。 | 方向关联拟合与解释 | source-reported | PDF 10–11（印刷 421–422）§3.3、式(2)、图8，PDF 15（426）表1交叉印证。PDF 11 的分数排版及首解数字待目检。 | true |
| A18-3 | 线偏振结果倾向于 ⁴⁰Ca 的 2M1 占优和 ⁹⁰Zr 的 2E1 占优。对 ¹⁶O，约 3 MeV 的平均光子能量下偏振灵敏度偏弱，可分析的康普顿散射事例也少，两个解无法作统计显著区分。 | 报告的偏振结果 | source-reported | PDF 11–13（印刷 422–424）§3.4、式(3)、图9。PDF 12 的面板曲线及误差棒待目检，¹⁶O 的统计结论见 PDF 13 正文。 | true |
| A18-4 | 球形与形变基态的两态混合计算给出 ¹⁶O 的磁化率更接近实验允许的较小 &#124;χ&#124;，对应较大的 &#124;α_E1/χ&#124; 解。作者用贡献相消定性解释电偶极跃迁极化率的减小，其大小和符号仍缺乏定量解释。 | 模型偏好与解释 | source-reported | PDF 18–23（印刷 429–434）§4.1–4.2、式(12)–(17)、图11、表3 | true |

¹⁶O 的分支比依赖符合事件筛选、偶然符合扣除及效率校正。绝对矩阵元还依赖寿命、方向关联拟合和附录速率公式。⁴⁰Ca、⁹⁰Zr 的若干比较数据沿用早期工作，三核偏振比较见本文图9。

- 将旧页码 412–450 明确标为印刷页，并补列物理页。分支比的主定位改为 PDF 13–15／印刷 424–426（图10、式(4)、表1），方向与偏振改为 PDF 10–13／印刷 421–424，三核模型讨论改为 PDF 15–23／印刷 426–434。范围补列 PDF 38 的附录 B。
- 将“线偏振选出 ¹⁶O 的主导解”改为“线偏振未能显著区分 ¹⁶O 的两解，两态磁化率模型偏好小 |χ| 解”。实验确定 α_E1 与 χ 的相对符号，个别矩阵元的符号随相位约定。
- 保留抽取疑点及其物理页。PDF 6 图4图题末项重复标作 (c)，PDF 7 正文称该 ¹²C 面板为 (d)。PDF 9 图6抽取图题的和能窗与 PDF 8–9 正文的 5.75–6.25 MeV 不一致，宜按正文引述并核图题。PDF 8 式(1)、PDF 10 式(2)及拟合参数列、PDF 11 式(3)、PDF 36 式(A.39)–(A.42)和 PDF 37 式(A.47)有符号或幂次损坏，暂缓逐式转录。PDF 37 页首反冲式抽作 (A.24a)，PDF 15 正文指向 (A.42a)，需核原印编号。
