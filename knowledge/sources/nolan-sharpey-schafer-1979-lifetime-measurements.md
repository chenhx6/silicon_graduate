---
type: source
title: "Nolan & Sharpey-Schafer 1979 - The measurement of the lifetimes of excited nuclear states"
aliases: [Nolan Sharpey-Schafer 1979 lifetime review]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: review-method
reading_depth: deep-read
title_original: "The measurement of the lifetimes of excited nuclear states"
authors: [P. J. Nolan, J. F. Sharpey-Schafer]
journal: "Reports on Progress in Physics"
year: 1979
volume: 42
pages: "1-87"
canonical_source: "Nolan & Sharpey-Schafer, Rep. Prog. Phys. 42, 1 (1979)"
library_file: "raw/papers/gpt/high-spin-20260920/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf"
raw_sha256: "5e20f735e995021f4a0eb8c1a937acedeee53509caed3ffa2cd8ddaa794bbc4f"
nuclei: [lifetime-methods]
reactions: []
experiments: []
models: [DSAM-stopping, recoil-distance, electronic-timing]
observables: [nuclear-lifetime, gamma-energy-shift, attenuation-factor, transition-strength]
methods: [doppler-shift-attenuation-method, recoil-distance-method, electronic-timing, Coulomb-excitation]
tags: [lifetime, DSAM, RDM, Doppler-shift, review, nuclear-structure-method]
---

# The measurement of the lifetimes of excited nuclear states

## Bibliographic Record

- P. J. Nolan and J. F. Sharpey-Schafer, *Reports on Progress in Physics* **42**, 1–87 (1979).
- 规范文件：`raw/papers/gpt/high-spin-20260920/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf`。
- 88-page review PDF (printed pp.1–87); full chapter map and method comparisons read.

## Scope and Reading Depth

- Fully read: Doppler-shift techniques (DSAM, stopping theories, RDM), electronic timing, blocking, fission isomers, indirect Coulomb/electron/resonance/capture methods, exotic techniques and accuracy/reliability comparison.
- Not covered: reanalysis of every historical lifetime experiment, modern stopping codes and post-1979 detector developments.

## Key Evidence and Method Logic

- Lifetime `τ=ℏ/Γ` links measured widths/decay probabilities to electromagnetic matrix elements; complementary spins, parities, branching, multipole mixing and conversion data are required for model comparison.
- DSAM compares Doppler shift/attenuation with recoil slowing time (~`3×10⁻13 s`), requiring electronic/nuclear stopping models, recoil velocity, feeding and side-feeding treatment.
- RDM compares decay time with recoil flight between foils (`~5 μm–2 cm`), while electronic timing and blocking cover other lifetime ranges.
- Indirect methods infer widths from Coulomb excitation, electron scattering, resonance fluorescence or capture; products of matrix elements and ground-state access impose boundaries.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NS79-1 | DSAM and RDM dominate direct lifetime measurements in the `10⁻18–10⁻6 s` range but rely on stopping/flight-time models. | method-framework | direct | PDF Ch.II, Fig.2 | true |
| NS79-2 | Lifetime interpretation requires complementary spin/parity, branching, mixing and conversion information. | method-boundary | direct | PDF pp.3–6 | false |
| NS79-3 | Coulomb excitation and other indirect methods measure matrix-element products/widths rather than direct decay time. | method-boundary | direct | PDF pp.4–6, Ch.VI | false |

## Summary

Nolan & Sharpey-Schafer is a foundational lifetime-method review that calibrates DSAM/RDM, stopping, feeding, timing and indirect-width assumptions. It is the method lineage for later `61Ni`, `165Tm`, `131Ce` and high-spin lifetime sources.

## Competing Interpretations and Limitations

Historical stopping powers, feeding models, detector resolution and side-feeding assumptions can dominate lifetime uncertainty. Direct and indirect methods are not interchangeable; each has a range, observable and input-data boundary.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| NS79-AR-1 | Method chain | Reaction/recoil → Doppler/timing/flight observable → stopping/response model → τ → transition strength. | PDF Chs.II–VIII | self-checking |
| NS79-AR-2 | Transfer condition | Reuse only with matching recoil velocity/material/feeding/detector and uncertainty model. | PDF Ch.II, Sec.VIII | active-L3 |
| NS79-AR-3 | Independence | Review; historical examples are not new experiments. | Scope/References | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` and strengthens [[doppler-shift-attenuation-method]] and lifetime evidence boundaries.
- Persistence: link to Jensen 2001, Wadsworth 1977 and the `131Ce` lifetime project.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `NS79-P0-1`: lifetime-derived strengths cannot be reused without stopping/feeding and method-specific uncertainty mapping.

## Extracted Pages

- Methods: [[doppler-shift-attenuation-method]]。


## Day18内无学分Day19预习：时间窗与交叉方法边界

本段为同一Day18 session在Radeck之后的下一卡无学分preview。原页面旧字节、旧NS79-1–3、`unreviewed`状态和既有flags均保留；以下新claims是本session targeted page verification、`needs_review: true`，不把旧完整阅读记录当本次盲读。核对PDF3 contents、PDF6–7 DSAM/RDM框架、PDF10–12 attenuation与side-feeding、PDF19–23 Coulomb/feeding、PDF78–81 accuracy comparison；没有重建历史实验或现代fast-timing source。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-P19-1 | review把直接方法范围置于约10^-18–10^-6 s；DSAM把寿命和固体/气体减速时间比较，RDM把寿命和5 µm–2 cm两箔间飞行时间比较。此为方法框架，不是任意核素的硬可用区间。 | method-window-framework | direct-review | PDF3 contents；PDF6 | true |
| NS79-P19-2 | DSAM centroid/attenuation的F=〈v〉/v0需Stopping theory；作者区分electronic与nuclear stopping的速度域，并强调F(T)曲线依该理论。 | dsam-stopping-dependence | direct-review | PDF6；PDF10–11 Eqs2.4–2.5/Fig6 | true |
| NS79-P19-3 | 重离子fusion-evaporation中side feeding可在slowing time内发生；上级gate可削弱部分feed，但初始速度/feeding component仍须响应模型。Coulomb excitation可减少side-feeding time，因为目标态由散射过程直接布居，但只适用于可达低能态/稳定体系等条件。 | feeding-method-boundary | direct-review | PDF19–21/Figs11–12 | true |
| NS79-P19-4 | RDM在原理上不需stopping theory且可高精度，但短寿命端受靶—stopper separation标定困难；DSAM/RDM约1–20 ps有重叠，交叉核验本身很难。 | cross-method-overlap-boundary | direct-review | PDF78–81/Table7 | true |
| NS79-P19-5 | review明确警告：DSAM与Coulomb-excitation yield若相合，可能因两者共享相同（甚至错误）stopping powers；不同方法相合不自动等独立确认。 | shared-systematic-counterexample | direct-review | PDF80–81/Table7/Fig56 discussion | true |
| NS79-P19-6 | 对同一候选寿命，方法选择应先看响应主导项：DSAM需stopping/feeding/velocity；RDDS需distance/shifted-US/finite-stopper/deorientation；fast timing需prompt response/time-walk/background。Nolan只直接支持前两者，第三项仍是本preview设计边界，不能冒原文现代结论。 | decision-tree-boundary | synthesis-and-boundary | NS79-P19-1–5；R12-P19-1–10 | true |
| NS79-P19-7 | 由寿命到strength还需spin/parity、branching、mixing、conversion和efficiency；Coulomb-excitation yield本身还受feeding、absolute efficiency、dead time、angular distribution、stopping/target absorption等输入影响。 | strength-input-contract | direct-review | PDF4–5/Eq1.2；PDF65–67 | true |
| NS79-P19-8 | 本session仅完成Nolan targeted pages和方法决策树边界；不把Radeck/Nolan旧文献变成正式Day19 credit，不打开Day20；原Nolan旧full-read status不被改成新盲测。 | actual-scope-and-credit-boundary | task-reading-receipt | nolan-protected-prefix-008；day19-preview-state-007 | true |

本段[访问/身份回执](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/nolan-protected-prefix-008.json)冻结原页/raw hash；没有取得历史DSAM/RDM原计数、现代fast-timing producer或jointCov。与[[radeck-2012-deorientation-lifetime-98ru-rdds]]的R12-P19段合用时，仍须区分综述方法框架、Radeck实测response和本任务条件推断。

正式Day19仍需新session逐卡验收；本preview只补方法边界和决策树，不授课程学分。


## Day18内无学分Day19预习补充：电子计时响应

继续核对本次方法预习的PDF48–52（electronic timing）并保留旧页prefix/status。新claims仍`needs_review: true`，不是新实验或正式Day19学分。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NS79-P19-9 | 电子计时review给出约10^-11–10^-6 s的有效范围；production time由脉冲束、粒子或形成γ定义，decay time由退激γ定义，时间谱是指数衰变与PRF卷积。 | timing-window-and-zero-time | direct-review | PDF48–49 Sec3.1–3.2/Eq3.1/Fig34–35 | true |
| NS79-P19-10 | PRF由prompt decay测得，受探测器距离/固体角、charge-carrier统计、rise time和电子学影响；slope方法适合τ长于PRF尾，centroid方法比较prompt/delayed first moments，可测远小于FWHM的差，但要求系统误差控制。 | prompt-response-contract | direct-review | PDF49–50 Sec3.2；PDF52 centroid examples | true |
| NS79-P19-11 | 电子计时选择应同时记录prompt calibration与delayed spectrum；对小于PRF FWHM约0.5–1%的差异，PRF随γ能量/门条件变化必须核验，不能把统计样本大直接换成窄响应。 | timing-calibration-boundary | direct-review-and-synthesis | PDF50/52；NS79-P19-10 | true |
| NS79-P19-12 | 由DSAM/RDM/electronic timing组成的选择树仍是响应主导的条件设计：DSAM看stopping/feeding，RDM看distance/finite-stop，timing看PRF/zero-time/walk/background。三者结果相合才有交叉价值，若共享reaction/branch/model仍不自动独立。 | complete-preview-decision-boundary | synthesis-and-boundary | NS79-P19-1–11；R12-P19-1–10 | true |
