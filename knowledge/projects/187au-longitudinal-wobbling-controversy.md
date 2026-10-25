---
type: project
title: "187Au low-spin longitudinal-wobbling controversy"
aliases: [187Au longitudinal wobbling controversy, 187Au LW evidence map]
created: 2026-07-03
updated: 2026-10-25
status: active
review_status: human-reviewed
project_stage: competing-evidence-matrix
confidentiality: private
nuclei: [187au]
tags: [187au, longitudinal-wobbling, signature-partner, controversy, evidence-map]
---

# `187Au` Low-Spin Longitudinal-Wobbling Controversy

## Project Purpose

本页是 `187Au` low-spin longitudinal-wobbling 争议的 project-level evidence matrix。它并列整理 Sensharma 2020 的支持链与 Guo 2022 的反证/重解释链，区分实验事实、实验判据、作者解释和模型结果；不裁决哪一方最终正确，也不作为论文草稿或原始来源替代品。

## Agent active summary — Day23 current evidence

本段为2026-10-25 Codex self-audit导航，不扩张既有human-reviewed范围。当前逐量对照见“Day22 checkpoint094”及下方Day23追加条目。

- [[guo-2022-low-spin-wobbling-187au]] GU22-D22-R094-1：旧−.10(5)属于P，不能当δ制造88倍E2变化；新δ从实际Fig.3读取。
- [[guo-2022-low-spin-wobbling-187au]] GU22-D22-R094-2：数W.u.为外部带内尺度的估计，非新增绝对寿命。
- [[guo-2022-low-spin-wobbling-187au]] GU22-D22-R094-3：Q借自同型探测器外部曲线；P–Rac误差矩形给出的δ域不等于公开完整joint-likelihood。
- [[sensharma-2020-longitudinal-wobbling-187au]] AU20-D22-R094-1：band(3)是作者SP指认，并非二声子带。独立反方的核素归属挑战保留，物理终审仍开放。新增内容needs_review: true。

- Day23实际376 δ上误差+.11、API时间窗/clock/total-vs-K及原conversion正文缺口见GU22-D23-001–012；现代导出不新增独立conversion票。
- 实际官方ENSDF注释现已补出旧αK数值及其评价MR依赖，见GU22-D23-013–016；原paper全文仍缺。
- 支持方同线Fig4.12与Table4.4系数阶段尚待绑定，见SE21-D23-8/9；不能直接当同一原始AD向量。
- source模型β/参考core与多轨道算符迁移仍需冻结实际producer；[[signature-tip-shears-discrimination-contract]]保raw/相位/response输入边界，不作最终LW/SP终审。

## Research Question

1. bands (1)/(2) 是否满足 `n_w=0/1` longitudinal-wobbling（LW）判据？
2. Sensharma 2020 的 band (3) 是否是可稳定识别的 associated signature partner，且能否作为 LW/SP 的同核素对照？
3. 相同 376/462 keV connecting transitions 的大/小 mixing-ratio branch 为何在两项独立实验中得出相反结构含义？
4. 低自旋体系是否满足高自旋、小角 harmonic wobbling approximation 的适用条件？

## Source Roles and Independence

| Source | Project role | Evidence independence and boundary |
|---|---|---|
| [[sensharma-2020-longitudinal-wobbling-187au]] | supporting source for the low-spin longitudinal-wobbling interpretation | 两次 ATLAS/Gammasphere 数据合并分析；angular distribution、能量与 PRM 构成同一支持链，connecting transitions 未测 linear polarization |
| [[guo-2022-low-spin-wobbling-187au]] | counter-source/reinterpretation source against the low-spin LW interpretation | 独立 HIRFL 反应、探测阵列与 `R_ac + P` 数据；对 internal-conversion、β-decay 等早期工作仍是二手比较，需另摄入原始来源才能按独立证据计数 |

两篇 source 均为 `human-reviewed`，AU20-1 至 AU20-15、G22-1 至 G22-20 均为 `needs_review: false`。用户已审核本 project 的 AU-SYN-1 至 AU-SYN-12。

## Current Hypotheses

- H1：bands (1)/(2) 是 `n_w=0/1` LW pair；
- H2：Sensharma band (3) 是 yrast 的 `α=-1/2` unfavored signature partner；
- H3：Band 2 主要是相邻 `h9/2` 单粒子轨道之间的 excitation，而非 wobbling phonon；
- H4：Sensharma band (3) 的 `187Au` identity 受 `188Pt` reassignment 挑战；
- H5：低自旋进动可能存在，但未必适用高自旋、小角 harmonic wobbling-phonon approximation；
- 当前状态：H1/H2 有支持方实验与 PRM，H3-H5 有独立反方实验、QTR 与方法学批评；本 project 不作最终取舍。

## Evidence Available

当前直接 evidence pool 仍由 Sensharma 2020 与 Guo 2022 两篇已人工复核 source 构成。2026-09-13 定向外部检索确认 Guo 2022 的 arXiv `2011.14354v3` 是同一发表来源，未发现新的 `187Au` 直接实验或核素专属后续计算。以下矩阵沿用 AU20/G22 source claim ID 与 locator；Rupnik、Bourgeois、Lawrie 和 TiP 案例目前只作为 follow-up，不冒充已独立摄入的底层证据。

## Observed Facts

| Observation | Source claim and locator | Evidence role |
|---|---|---|
| Sensharma Fig.2 给出 yrast band (1)、Band 2 及新建 band (3)；band (3) 以 `E_x=386.3 keV, 11/2-` 为带头 | AU20-2；p.3, Fig.2 | 建立 supporting paper 的三带对象 |
| Band 2 通过六条 ΔI=1 transitions 连接 yrast；最低四条为 376.3、461.8、544.3、639.3 keV | AU20-3；pp.3-4, Figs.2-3 | 建立候选 LW→yrast links |
| Sensharma 对上述四条 links 给出大 `abs(δ)` 与 87.7%-93.3% E2 fractions | AU20-4；p.4, Fig.3(a-d) | 支持 E2-dominated connecting transitions |
| Sensharma band (3) 以 265.3、436.5 keV links 连接 yrast；E2 admixture 约 0.4%、1.0% | AU20-5；pp.3-4, Figs.2-3(e,f) | 建立 M1-dominated signature-partner 对照 |
| 429.2 keV ΔI=2 crossover 连接 Band 2 的 `15/2-` 与 band (3) 的 `11/2-` | AU20-6；pp.3-4, Fig.2 | 支持 supporting paper 的带间身份与 spin/parity 关系 |
| Sensharma Fig.4(d) 给出按 bands (1)/(2) 构造的 `E_wobb` 随自旋增加 | AU20-9；p.4, Fig.4(d) | 支持方用于 LW 分类的能量行为 |
| Guo 独立 HIRFL 数据确认早期 Bands 1-4，并对 Band 2→Band 1 的 376/462 keV links 做联合 `R_ac-P` 分析 | G22-3/G22-5/G22-6；pp.2-3, Figs.2-3 | 对相同争议 links 的独立实验约束 |
| Guo 对 376/462 keV links 得到约 `δ=-0.26/-0.28` 的小 `abs(δ)` branch | G22-7；p.3, Fig.3(a-b) | 支持 M1-dominated character，与 AU20-4 直接冲突 |
| Guo 未观察到 Sensharma 的粉色 band (3) sequence 及 429/437 keV links；相近 265/405/414/551 keV sequence 被归入 `188Pt` | G22-3；p.2, Fig.2 | 对 associated-SP band identity 的直接挑战 |

## Experimental Criteria and Core Observables

| Observable / criterion | Supporting use | Counter-evidence or limitation | Current project status |
|---|---|---|---|
| Connecting-transition E2/M1 character | AU20-8：wobbling→yrast links 应 E2 enhanced，SP→yrast links 应 M1 dominated | G22-12 同意该判据层级，但 G22-7 对相同 376/462 keV links 得到 M1-dominated branch | 核心实验冲突，不是判据定义冲突 |
| Angular-distribution mixing ratio | AU20-4 由 17 个角度环 fits 得到四条大 `abs(δ)` | G22-13/G22-14：`χ²(δ)` 可有大/小双解；Sensharma 未讨论小解 | 必须比较完整 `χ²`、alignment/attenuation 与 branch exclusion |
| Linear polarization | Sensharma 未报告 Band 2 connecting-transition polarization | G22-6/G22-7 联合 `R_ac + P` 选择小 branch；G22-18/G22-19 补齐 calibration、选门、污染与误差处理 | Guo 增加了独立 observable；462 keV 分析仍含污染边界和外部 `Q` calibration 等程序依赖 |
| Internal-conversion cross-check | Sensharma 大 branch 与其 angular distribution 一致 | G22-8 称小 branch 与早期 conversion data 一致 | 当前仅摄入 Guo 的二手比较；原始 conversion sources 尚未进入 evidence gate |
| Wobbling energy | AU20-8/AU20-9：LW 的 `E_wobb` 预期并观察到随自旋增加 | 趋势依赖 bands (1)/(2) 已是 `n_w=0/1` pair 的 assignment；Guo 未否定能量曲线本身 | 条件性支持，不能替代 electromagnetic evidence |
| Relative transition ratios | AU20-14：LW→yrast `B(E2)_out/B(E2)_in` 最大约 0.7，明显高于 SP→yrast | G22-9 由小 δ 与外部 `B(E2)_in` 估计 `B(E2)_out` 仅数 W.u. | 两方量均依赖 mixing-ratio branch，且缺本文独立 lifetime/absolute `B(E2)` |
| Associated signature-partner identity | AU20-5/AU20-10：band (3) 的近纯 M1 links 支持 SP 指认 | G22-3/G22-4：该 sequence 未复现，相近 lines 归入 `188Pt`；Rupnik β decay 至 `I=19/2` 亦未见 | identity-level 冲突削弱同核素 LW/SP 对照前提 |
| Low-spin wobbling approximation | Sensharma AU20-15 以 half-filled `h9/2`/medium-axis 图景解释 LW | G22-15：`J≈j+1` 对应 `R≈1ħ`，难满足高自旋小角近似；Fermi surface 位于 `h9/2` 底部 | 适用条件本身是理论争议，需原始理论来源定量界定 |

## Author Interpretations

| Interpretation | Source claim and locator | Evidence boundary |
|---|---|---|
| bands (1)/(2) 是 `n_w=0/1` longitudinal-wobbling pair | AU20-9；p.4, Fig.4(d) | 作者解释；依赖大-δ branch、E2-rich links 与 PRM |
| band (3) 是 associated unfavored signature partner | AU20-10；pp.3-4, Figs.2-3 | 作者解释；其 sequence identity 被 Guo 2022 挑战 |
| half-filled `h9/2` proton 支持 longitudinal geometry | AU20-15；pp.1-2, Fig.1(c), p.4 | 分类图景；正文未给逐自旋 angular-momentum components |
| Band 2 是 dominant single-particle excitation | G22-17；p.5, Summary | 反方作者解释；由小 δ、QTR orbital content 与早期数据比较支持 |
| Sensharma band (3) 可能不属于 `187Au` | G22-4；p.2, discussion of Ref.24 | 作者基于未观察和二手 β-decay 比较的解释；Rupnik 原文尚未独立摄入 |
| 既有 low-spin identification paradigm 可能遗漏其他机制 | G22-14/G22-16；pp.4-5, Figs.5-6 | 方法学/解释框架批评；β/γ vibration 与 TiP 只是候选替代机制 |

## Model Results

| Model use | Source claim and locator | What it supports | Limitation |
|---|---|---|---|
| Sensharma PRM：`β=0.23, γ=23°`，single-j `h9/2` 为主 | AU20-11；p.4, model setup | bands (1)/(2)/(3) 的 LW/SP 分类框架 | 形变、转动惯量与模型空间为输入；不是实验观测 |
| configuration-fixed CDFT 形变 | AU20-12；p.4 | 支持 PRM 常形变近似 | 只约束形变输入，不独立证明 wobbling |
| PRM energies、`E_wobb` 与 transition ratios | AU20-13/AU20-14；pp.4-5, Figs.4-5 | 总体趋势和 E2 ratios 较好 | 略低估 `E_wobb`；对 LW/SP 的 M1 ratios 有相反方向偏差 |
| Guo QTR：`ε2=0.21, γ=12°`、Harris `J0/J1`、9 个负宇称轨道 | G22-10；p.3 | 允许相邻 `h9/2` orbitals 竞争 | 与 Sensharma PRM 的形变、惯量和空间不同 |
| QTR orbital content 与 transition observables | G22-11/G22-20；main p.3, Fig.4; supplement pp.4-5, Fig.3 | Band 1 以 orbital #19、Band 2 以 #21 为主；低自旋 precession-like #19 成分较小，支持 single-particle excitation 重解释 | 模型结果不能替代实验 branch 冲突 |
| Precession / TiP | G22-16/G22-17；pp.4-5 | 提醒低自旋可有非 wobbling-phonon 的 collective motion | Guo 未对 `187Au` 完成直接 TiP calculation；本轮只列 future source/concept |

## Cross-Source Evidence Matrix

| ID | Project-level claim | Supporting evidence | Counter-evidence / limitation | Source independence | Current status | needs_review |
|---|---|---|---|---|---|---|
| AU-SYN-1 | bands (1)/(2) 构成 reported LW candidate pair，实验上由多条 ΔI=1 links 相连 | AU20-2/AU20-3；p.3, Fig.2 | “相连”不等于 excitation mechanism 已确定 | Band structure 由支持方建立，Guo 确认 Band 2 并复测最低 links | observed structure established; LW label disputed | false |
| AU-SYN-2 | 376/462 keV links 的 electromagnetic character 是争议的首要 observable | AU20-4：大 `abs(δ)`、E2 rich | G22-7：小 `abs(δ)`、M1 dominated | 两套独立反应/阵列；相同 transitions 的直接冲突 | unresolved | false |
| AU-SYN-3 | Sensharma angular distribution 单独不能显示其大 branch 已唯一排除小 branch | AU20-4/AU20-7 | G22-13/G22-14 的双解与方法学批评；Sensharma 无 link polarization | Guo 是独立 experiment，但对 Sensharma fit 的批评仍需原始 fit/系统误差复算 | unresolved methodology | false |
| AU-SYN-4 | Guo 的 `R_ac + P` 为小 branch 增加独立约束，但尚非无条件终局证据 | G22-6/G22-7 | error bars 较大；calibration、`σ/I` 与程序需由补充材料审计 | 独立数据；主文与补充材料共同构成方法链 | stronger counter-constraint, auditable but method-dependent | false |
| AU-SYN-5 | increasing `E_wobb` 支持 LW 分类，但不是独立充分条件 | AU20-8/AU20-9/AU20-13 | 依赖 `n_w=0/1` assignment；不解决 δ branch | 与 transition evidence 同一 supporting chain，不按独立重复证据计数 | conditional support | false |
| AU-SYN-6 | associated signature-partner 对照受到 sequence identity 冲突影响 | AU20-5/AU20-6/AU20-10 | G22-3/G22-4：未复现、`188Pt` reassignment、β-decay non-observation | HIRFL 未观察独立；Rupnik 证据当前为 Guo 二手转述 | identity unresolved | false |
| AU-SYN-7 | Sensharma PRM 为 LW/SP 提供模型一致性，不构成实验证明 | AU20-11-AU20-14 | 参数/空间依赖，M1 ratios 有偏差 | CDFT 形变约束不是独立 wobbling observable | model-supported interpretation | false |
| AU-SYN-8 | Guo QTR 为 single-particle excitation 提供竞争模型解释，不构成实验事实 | G22-10/G22-11 | 与支持方模型输入不同，逐轨道实现见补充材料 | 与 Guo 实验同一论文，模型与数据比较不是独立实验来源 | competing model interpretation | false |
| AU-SYN-9 | low-spin wobbling approximation 的适用性尚未定量闭合 | AU20-15 的 half-filled-shell LW 图景 | G22-15 的 `R≈1ħ`/Fermi-surface 批评 | 两方依赖不同理论前提；需 Lawrie 2020 等原始理论来源 | unresolved theoretical premise | false |
| AU-SYN-10 | 当前材料不能把 `187Au` 直接改判为 TiP | G22-16/G22-17 仅列 alternative mechanisms | 无 `187Au` TiP 专门 calculation、geometry 或区分性 observable | TiP 证据尚未摄入 | future hypothesis only | false |
| AU-SYN-11 | Guo supplementary material 使 376/462 keV 小 branch 的选门、污染控制、校准和误差边界可审计，但不会把该结果升级为无条件终局裁决 | G22-18/G22-19；supplement pp.1-4 | 462 keV 需避开邻近异构态以上 463 keV 污染；`σ/I` 未固定，polarization sensitivity `Q` 采用同型探测器外部 calibration | 与 Guo 主文为同一实验和同一证据链 | stronger audit trail with retained systematics | false |
| AU-SYN-12 | Guo supplementary QTR 具体支持 Band 1/#19 与 Band 2/#21 为不同 dominant orbitals，且低自旋 precession-like 成分较小 | G22-20；supplement pp.4-5, Fig.3 | 逐轨道波函数为模型结果；不能据此把实验 Band 2 单独“证明”为 single-particle excitation | 与 G22-10/G22-11 同一 QTR 计算链 | refined competing-model result | false |

## Counter-Evidence Summary

1. 相同 376/462 keV links 在两项独立实验中落入相反的 mixing-ratio branch。
2. Sensharma 未报告这些 links 的 linear polarization；Guo 指出 angular-distribution `χ²` 双解未被充分讨论。
3. Guo 的小 branch 与其转述的 early internal-conversion data 更一致，但这些原始 conversion sources 尚未独立摄入。
4. Sensharma band (3) 的 `187Au` identity 受到 HIRFL non-observation、`188Pt` reassignment 与 β-decay comparison 的挑战。
5. Guo QTR 提供 single-particle orbital excitation；这削弱“只有 wobbling 或 signature partner 两种选项”的范式，但仍是模型依赖解释。
6. `J≈j+1`、`R≈1ħ` 与 `h9/2` Fermi-surface 位置对低自旋 wobbling approximation 提出适用性问题。

## Paper Evidence Gate

| Material | Gate status | Required use |
|---|---|---|
| AU20-1 至 AU20-15、G22-1 至 G22-17 | eligible evidence pool | 两个 source/上述 claims 已人工复核，citation key 与 locator 完整；写作仍须回到对应 source/raw |
| G22-18 至 G22-20 | eligible evidence pool | 补充材料是 Guo 主文的附属证据层；claims 已人工复核，使用时仍归属于 `guo_2022_Probingnature` |
| 能带、transition energy、实验 δ、E2 fraction、`R_ac`、polarization 与 `E_wobb` | eligible as reported observations | 必须注明 source、实验和 locator；冲突数值必须并列，不得择一写成共识 |
| LW、signature partner、single-particle excitation | eligible only as attributed author interpretations | 必须写“作者解释/指认为”，不得写成裸事实 |
| PRM/CDFT/QTR 结果 | eligible only as model results | 参数、模型空间、偏差和不同输入必须保留 |
| G22-4/G22-8 对 Rupnik、Bourgeois 等早期数据的比较 | follow-up lead / attributed secondary comparison | 可准确转述“Guo 指出”，但原始论文未摄入前不能当作已独立核验的底层证据 |
| G22-9 的数 W.u. `B(E2)_out` | attributed derived estimate | 依赖本文 δ 与外部 `B(E2)_in`，不是本文寿命测量 |
| TiP 对 `187Au` 的解释 | not yet eligible | 当前只有 future alternative；缺专门理论/实验 source 与 `187Au` 直接 calculation |
| Project synthesis matrix（AU-SYN-1 至 AU-SYN-10） | reviewed navigation/synthesis | 用户已人工审核；仍不能代替 source/raw 进入论文正文 |
| AU-SYN-11 至 AU-SYN-12 | reviewed navigation/synthesis | 补充材料新增综合已人工复核；仍不能替代 source/raw |

## Needs Review

- AU20-1 至 AU20-15、G22-1 至 G22-20 与 project-level AU-SYN-1 至 AU-SYN-12 均已审核，`needs_review: false`。
- 本 project 已改为 `review_status: human-reviewed`。

## Unresolved Issues

1. 需要在统一 detector response、alignment/`σ/I`、attenuation、polarization convention 和误差模型下重建 376/462 keV 的完整 `χ²(δ)`。
2. 需要明确 Guo polarization magnitude 对大 branch 的排除置信度，而不只依据 central value。
3. 544/639 keV links 缺 Guo 同等 polarization cross-check；两方冲突目前只直接覆盖最低两条。
4. 需要回到 Sensharma 完整 coincidence/assignment 材料，核对 band (3)、429/437 keV links 与 channel contamination。
5. 需要独立摄入 Rupnik β decay 与早期 internal-conversion sources，区分直接证据和 Guo 的二手比较。
6. 两篇工作均缺可统一比较的独立 lifetime/absolute `B(E2)` 数据集。
7. PRM 与 QTR 使用不同形变、惯量和模型空间；尚缺 common-input benchmark。
8. low-spin wobbling approximation 的定量下限、precession 与 TiP 判别 observables 尚缺专门理论来源。

## Risks and Blockers

- 相同 transition 的 mixing-ratio branch 尚未在统一响应和误差模型下复算；
- Sensharma 的完整 coincidence/systematics 仍未进入 Wiki；Guo supplementary material 已挂接并完成 claim review；
- early internal-conversion 与 β-decay 证据当前通过 Guo 二手转述，独立性尚未闭合；
- band (3) identity 冲突会反向影响“同核素 LW/SP 对照”的证据强度；
- 两方模型输入不同，energy/transition agreement 不能直接比较为同一 benchmark；
- project matrix 已人工审核，但仍不能代替 source/raw 进入论文正文。

## Follow-Up Sources

1. Sensharma 2020 所指 forthcoming/full coincidence、spin/parity 与 angular-distribution analysis，或其 supplementary material。
2. Guo 2022 supplementary material 已作为主文附属证据层挂接并完成 G22-18 至 G22-20 复核，不另建 source/BibTeX。
3. D. Rupnik et al., *Phys. Rev. C* **58**, 771 (1998)，DOI10.1103/PhysRevC.58.771：Guo正文写`187Ag`，LSU馆藏摘要写Hg；母核文字疑点与全文缺口见GU22-D23-004，勿把Ag字面当真实母核认证。
4. C. Bourgeois et al. 1978 与 C. Bourgeois et al. 1989：internal conversion、shape coexistence 与 Band 1/2 早期 assignment。
5. `186Pt/187Au` 的 lifetime/`B(E2)_in` 原始测量，用于审计 G22-9 的 `B(E2)_out` estimate。
6. E. A. Lawrie et al. 2020, *Tilted precession and wobbling in triaxial nuclei*：建立 wobbling approximation、precession 与 TiP 的理论边界。
7. B. F. Lv et al. 2021 `135Nd` tilted-precession 原始工作：作为 TiP 实验/模型案例，不直接替代 `187Au` 证据。

## Cross-Reference to `135Pr`

[[135pr-wobbling-controversy]] 中也存在 angular-distribution 大/小 `abs(δ)` branch、polarization magnitude 与 TiP 替代解释问题。本页只建立判据层 cross-reference；不把 `135Pr` 数据写成 `187Au` 直接证据，也不重写其 project。

## TiP Future Plan

本轮不创建完整 TiP concept，也不把 `187Au` 改判为 TiP。未来应先摄入 Lawrie 2020 理论与 `135Nd` 原始案例，再决定是否建立 tilted-precession concept，并明确能区分 wobbling、single-particle excitation 与 TiP 的 angular-momentum geometry 和 electromagnetic observables。

## Data-Analysis Bridge

后续统一重拟合应保存：原始/背景扣除谱、gate、角度环分组、效率修正、alignment 或 `σ/I`、attenuation coefficients、polarization calibration、响应函数、两个 δ branch、完整 `χ²`/置信区间，以及与 AU20/G22 图表的逐项差异。band (3) identity 还需逐门比较 `187Au/188Pt` channel selectivity。

## Decisions

- Sensharma 2020 只作为 supporting source；Guo 2022 只作为 counter/reinterpretation source。
- observed facts、experimental criteria、author interpretations 与 model results 分层记录。
- increasing `E_wobb` 不脱离 electromagnetic links 和 assignment 前提单独裁决。
- PRM/QTR 一致性不替代实验 mixing-ratio 冲突。
- TiP 仅进入 future source/concept 计划。
- project 不替代 source/raw，不直接作为论文引用。

## Umbrella Project Recommendation

用户已明确启动 [[low-spin-wobbling-controversies]]。当前版本只以 `135Pr` 与 `187Au` 两个已审核案例建立跨案例 identification evidence map；Lawrie 2020 与 `135Nd` TiP 尚未摄入，因此 TiP 仍作为 future extension，不用于裁决本案例。

## Next Actions

1. 优先摄入 Rupnik 1998 与 early internal-conversion sources。
2. 摄入 Lawrie 2020 与 `135Nd` TiP 原始工作，补充现有 umbrella project 的理论边界。
3. 设计 376/462 keV links 的 common-response/common-error reanalysis。

## Related Sources and Pages

- [[low-spin-wobbling-controversies]]
- [[187au]]
- [[sensharma-2020-longitudinal-wobbling-187au]]
- [[guo-2022-low-spin-wobbling-187au]]
- [[187au-yrast-band]]、[[187au-longitudinal-wobbling-band]]、[[187au-signature-partner-band]]
- [[atlas-gammasphere-187au-f19-105-115mev]]、[[hirfl-187au-o18-108mev]]
- [[longitudinal-wobbling]]、[[signature-partner-bands]]、[[wobbling-motion]]
- [[multipole-mixing-ratio]]、[[interband-e2-strengths]]、[[wobbling-energy]]
- [[linear-polarization-asymmetry]]、[[two-point-angular-correlation-ratio]]
- [[particle-rotor-model]]、[[triaxial-particle-rotor-model]]
- [[135pr-wobbling-controversy]]

## 2026-09-13 External Search Audit

本轮以 `187Au low-spin wobbling`、`longitudinal wobbling 187Au` 和相关 arXiv/DOI 元数据做定向检索。唯一直接命中的是 Guo 等 *Physics Letters B* 828, 137010 (2022)，其 arXiv `2011.14354v3` 与当前已摄入的发表版 PDF 同一来源；现有 source 已补入该 arXiv 标识，未重复下载或计数。另命中 2026 年 `185Au` transverse-to-longitudinal wobbling 论文，但其核素为 `185Au`，不属于本页的 `187Au` 直接证据，未创建 source。

阶段结论：本轮对 `187Au` evidence ranking **no material change**。Sensharma 2020 的大 `|δ|`/LW 支持链与 Guo 2022 的独立 `R_ac+P` 小 `|δ|`/single-particle counter chain 仍是主要证据；band (3) identity、原始 internal-conversion/β-decay crosswalk、absolute lifetime/strength 和 common-input model benchmark 仍未闭合。搜索与排除记录见 `outputs/literature-acquisition/20260913-187au-refresh.json`。

本节为 2026 continuation 的 Codex self-audit，不属于此前用户审核的新增 claim；不改变页面既有 `human-reviewed` 历史范围，也不启动 L4。

## Day22 checkpoint094：恢复开放争议与逐量对照

旧Day19/22追加的4σ、88倍、1.1e−4 e²b²及最终物理归属认证撤回；原审阅矩阵保留。原件[[guo-2022-low-spin-wobbling-187au]] GU22-D22-R094-1–3与[[sensharma-2020-longitudinal-wobbling-187au]] AU20-D22-R094-1支持以下受限判断：

| 量/对象 | 支持方 | 反方 | 本任务边界 |
|---|---|---|---|
| 能谱 | 上升Ewobb与PRM支持LW | QTR能谱并结合单粒子解释 | 上升斜率单独不裁决 |
| E2/M1 | 四线大δ；相对rE2最高约.7 | 两线小δ与数W.u.外标估计 | 非同一次测量的两根；不报新绝对τ/B |
| 取向/组态 | PRM β=.23、γ=23°，h9/2中部λ | QTR ε2=.21、γ=12°，底部轨道#19/#21 | 模型推断，不是测得主轴分量 |
| 偏振/响应 | 未测connecting-line P | P–Rac并放开σ/I，Q借同型探测器外部曲线 | 未得到完整联合Cov/likelihood，拒绝擅报σ数 |
| 伴随带 | band(3)被指为SP，不是二声子带 | 未复现、相似序列归188Pt | independent challenge成立，原数据逐门归属仍需核 |

下一步以相同逐线身份、gate/背景、a(E)/Q(E)、σ/I和双分支响应重分析；新寿命可独立定标。历史conversion资料是另一次测量谱系，当前只通过Guo比较，不伪称本次新测。needs_review: true；未给正式物理终审。


## Day23：历史conversion的直接证据缺口与母核文字

本轮以原Guo p.2局部图、Crossref DOI和LSU作者馆藏页交叉核验，发现Guo确实印187Ag而非OCR误识；馆藏摘要为Hg两态衰变且标明无正文可下载。[[guo-2022-low-spin-wobbling-187au]] GU22-D23-004记录原文文字、电荷守恒核查与摘要公式缺失，均needs_review:true，原project/page人审范围不扩张。不能把这处印刷疑点扩大成Rupnik实验失效，也不能据馆藏摘要恢复376/462的αK或SP non-observation灵敏度。

因此当前历史conversion仍是Guo二手比较，尚未增加一个直接核阅的独立实验节点。公开全文获取本次尚未成功，下一路线为原作者/机构公开全文或可访问出版商正文；同时可沿Bourgeois1978原始转换资料调查。新的Q曲线/模型定标核验见[[signature-tip-shears-discrimination-contract]]；既有LW/SP支持与HIRFL反证均保留。


Day23后续追溯：Bourgeois1978精确DOI已核为10.1016/0375-9474(78)90184-7（[[guo-2022-low-spin-wobbling-187au]] GU22-D23-005），但有限公开来源路线未取得原文；1979关于187Au→187Pt衰变的相似题名论文不是该source，不能混入376/462的输入。当前不增加历史conversion的独立直接证据权重。NNDC暂时无法访问亦不改变这一点。


## Day23：官方评价export不等于独立转换测量

本次IAEA公开API成功返回Au187 gammas/levels，数据cutoff为2008-11-01而Extraction_date为2026-10-25。逐snapshot ID绑定376.3/462.1的母末态，total转换系数不能与Guo Fig3的αK混用，mixing_ratio字面正数字也不能缺adopted notes就改成有符号δ。近能量436.6实际是13/2→13/2，并非支持方SP的ΔI1连接；旧截止更不能检验2020新增band的非观察。出处[[guo-2022-low-spin-wobbling-187au]] GU22-D23-006/007/008为明确外部API field自审，非Guo原测量。

两个Band2母态的τ在export为空；9/2−异构态2.3s属于另一个end level，不迁入Band2求绝对B。CSV的重复unc_hl列还要求按列位置保留误差含义。完整adopted notes、原αK表/其引用及正式raw快照仍缺，保持readiness boundary和needs_review:true，不提高独立证据票数或最终归属。


## Day23：支持方完整PRM、版本定标与字段旁证

[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-D23-3/4进一步限定支持方：其h9/2 classical j不严格沿m轴，φj不近90°且short分量重要；作者仍依据total I的m分量/方位分布称LW。这不是严格冻结j的HFA，也不是实验直接测角，不能把与严格rigid-j图像的不同自动当作作者完全没有LW支持。Letter用middle-shell文字而thesis称Fermi不远离底部，两者同λ/.38MeV需实际sp谱/占据与算符核验，不能从单个数字恢复全部物理图像。

| 输入 | S20 Letter | SE21 thesis | 当前边界 |
|---|---|---|---|
| PRM形变/配对/λ | β=.23/γ23°/Δ.88/λ−1.32 | 同样数值 | 不等于Guo ε2=.21/γ12°的同一Hamiltonian；β/ε约定也须核 |
| reference core B(E2) | 186Pt2+→0+为.84(eb)² | printed128为1.44(eb)² | 同引Baglin2003，未读原评价/输入版本前分列，不选择或平均 |
| Au reference B(E2) | 13/2−→9/2−为1.49 | printed128字面正parity，1.49 | thesis文字不用于更改已识别h9/2负parity |
| 支持方模型范围 | h9/2 LW/SP | 另有h11/2 hole-like TW候选 | thesis γ调40°及25/2等失稳仅该参数模型；不是Guo376/462直接测试的同一带对 |

source原子出处为AU20-D23-1与SE21-D23-3/4/5。新内容needs_review:true；无统一operator/producer前不发布同输入拟合胜负。外部187Hg导出还只提供字段身份：GU22-D23-009/010/011确认母核Hg→Au、jp属于母核、强度全空及electron service-code0的非测量含义。它不补历史αK或实验上限。

## Day23：h9/2主导不等于完整单j磁算符

[[guo-2022-low-spin-wobbling-187au]] GU22-D23-012定向核SI Table1：#21和#22明确包含h9/2与f7/2来源，完整9轨道空间另含h11/2；仍保Band1/#19与Band2/#21的作者主要归属。标签/柱形图不等于带符号完整Nilsson/BCS系数，不能仅从dominant h9/2把实际EM振幅认证为某个公共gj j。

[[hamamoto-2002-wobbling-excitations-odd-a-high-j-aligned-particles]] H02-D23-004的h双伙伴角代数只是算符迁移边界，**不是本核新跃迁/混合含量预报**。当前source模型比single-j任务空间更广，亦不自动消除参数/response/Cov缺口。common-scale双比若要用于实际376/462，须先原EM矩阵/phase与occupation/定标输入，不从Pr单j数值跨核搬值。详[[signature-tip-shears-discrimination-contract]]；新needs_review:true，LW支持与独立P–Rac反证继续并存。

## Day23：旧转换证据不再只有Guo图的二手入口

新增[[guo-2022-low-spin-wobbling-187au]] GU22-D23-013–016记录实际官方ENSDF注释：376的旧实验αK转述为.119(15)/.11(3)，462为.050(9)/.08(2)，分别指向1998Ru04/1978Bo05。此次增加可核数值和来源路径；两篇原论文全文/谱与归一仍未取得，不能声称直接读过原实验。评价对象不是一份新增采集，也不与Guo对同一旧测量的引用重复计票。

| 证据节点 | 当前身份与依赖 | 剩余检验 |
|---|---|---|
| 1998Ru04与1978Bo05实验αK | 实际读到官方评价转述，数值逐线可查 | 原paper电子/光子归一、效率、混峰、共享系统和选择条件 |
| evaluator MR=.6/1.1与SG KC | 评价说明MR由实验αK/L计算；不是新的独立δ测量 | 原理论系数/版本/不确定度及采用过程 |
| adopted与IAEA API | 同一评价族的转录，totalCC不是实验αK | 旧Z flag、2013 XREF/母clock更正与逐母态ledger |
| Guo新P/Rac | 独立HIRFL实验，旧转换只作伴随约束 | 实际联合response/Cov，不能将转换单独选符号 |

[[signature-tip-shears-discrimination-contract]]据此收紧下一route：将真实旧αK向量与AD/P预测分别前向比较，保留理论ICC、校准和共同系统，而不是将换算δ和旧αK同时当独立票。本轮尚未作这项联合fit、δ显著性或模式终审。新增needs_review:true，不扩原人审范围；Au旧−.10是P、band3为SP和数W.u.外标边界保持。

标准ICC的sign边界直接回链[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-2；转述αK不单独选δ符号。

## Day23：历史转换的条件前向表与剩余边界

[[signature-tip-shears-discrimination-contract]]的新表用实际官方FO理论K分量（[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D23-001/002）连接376/462旧αK与两来源δ中央。Guo中心给.1412/.0813，Sensharma中心给.0498/.0289；旧αK四点逐一并列见[[guo-2022-low-spin-wobbling-187au]] GU22-D23-013/017，不能把作者整体一致性描述扩张成每点中央相同。大δ来源仍为[[sensharma-2020-longitudinal-wobbling-187au]] AU20-D22-R094-1。

本次解除两个标称能量pure理论K输入缺口，尚未解除历史归一/efficiency/共同Cov和新δ分支全域的比较；未反演新δ、统计排除或认证LW/SP。9项离线输入/角色控制不是科学归属认证，新增needs_review:true，保留原支持链及反方实测。

## Day23：旧转换的逐点相交保留，联合检验仍待输入

[[guo-2022-low-spin-wobbling-187au]] GU22-D23-018和[[signature-tip-shears-discrimination-contract]]补印刷δ端点的确定性映射：376 αK像[.132139,.145829]、462[.055165,.085742]，均与对应两项旧αK各自quoted范围有交集。由此，前一表中央值不同不能直接称新旧实验冲突；四个交集也不认证共同拟合或排除大根。

前提是[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D23-001的名义FO中央固定，实际理论/历史归一/δ响应Cov未传播，原primary全文仍缺。新needs_review:true，原LW/SP支持—反证矩阵、旧数据依赖与最终归属开放状态保持。

## Day23：支持方AD向量与局部分支误差的实际条件

[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-D23-6/7现明确Au376/461.8的A2/A4/r、333.8参考αexp和σ/J=.2；原方法先选较低χ²根再邻域采样。它提供条件信息，窄printed误差不等全球双分支权重，也不能据未公开另一谷声称等深。该thesis与PRL保持同实验谱系。

[[sensharma-2020-longitudinal-wobbling-187au]] AU20-D23-4/5 fresh原图给δ−2.67±.07/−2.98±.02；在[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D23-001名义表和历史能量上，其端点αK像与[[guo-2022-low-spin-wobbling-187au]] GU22-D23-013四个旧quoted范围不相交。这使旧转换反证的条件更具体，仍缺primary归一、完整response/theoryCov和globalδ域，不报新显著性或最终归属。新needs_review:true，原LW/SP支持链及band3身份争议保留。

## Day23：同名A2/A4在图表中有不同阶段

[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-D23-8/9实际新核376的Fig4.12 A2/A4=−.6704/.3194，与Table4.4的−.730/.523不同。[[signature-tip-shears-discrimination-contract]]的条件kernel中，complete系数近Table4.4，Gaussian后376 A2近Fig4.12而A4仍有差；现有结果不认证table去衰减或原程序实现，只要求先恢复图表/校正/拟合阶段。

kernel来源直接回链[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D23-001/002及[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D23-001，KS应用和实际array/gate迁移仍有条件。下一共同向量必须绑定净峰、校正顺序、自由fit系数、选根输出与共同Cov；当前不将表系数与δ重复当独立证据，也不凭条件残差改判LW/SP。新needs_review:true，原支持链与反方测量各自保持。
