---
type: source
title: "Evidence against the wobbling nature of low-spin bands in 135Pr"
aliases: [Lv 2022 135Pr, evidence against 135Pr wobbling]
created: 2026-07-03
updated: 2026-10-17
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Evidence against the Wobbling Nature of Low-Spin Bands in 135Pr"
authors: [B. F. Lv, C. M. Petrache, E. A. Lawrie, S. Guo, A. Astier, et al.]
journal: Physics Letters B
year: 2022
volume: 824
pages: 136840
doi: 10.1016/j.physletb.2021.136840
arxiv:
language: en
canonical_source: doi:10.1016/j.physletb.2021.136840
zotero_item_key:
citation_key: lv_2022_Evidencewobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr.pdf"
raw_sha256: 4B87C540BF9DA5141FA88EF8F00859162CB08918D56A5DA74726C7537DF5E26B
nuclei: [135pr]
reactions: [100mo-ar40-1p4n-135pr]
experiments: [jyfl-jurogam2-135pr-ar40-152mev]
models: [triaxial-particle-rotor-model]
observables: [multipole-mixing-ratio, interband-e2-strengths]
methods: [gamma-gamma-coincidence, two-point-angular-correlation-ratio, linear-polarization-asymmetry]
tags: [a130, 135pr, wobbling-counter-evidence, jurogam-ii, qtr, tilted-precession]
---

# Lv 等（2022）：反对 `135Pr` 低自旋带 wobbling 指认的证据

## Bibliographic Record

B. F. Lv et al., *Physics Letters B* **824**, 136840 (2022)，DOI `10.1016/j.physletb.2021.136840`。题名、作者、年份与 DOI 和只读 BibTeX 条目唯一匹配，使用 citation key `lv_2022_Evidencewobbling`。

## Scope and Reading Depth

主文与 supplementary material 全文精读，并视觉核对主文 Fig.1 的能级纲图、Fig.2 的 angular-distribution 双解与联合 `P-R_ac` 约束、Table 1 的 polarization/`R_ac`/mixing ratio、Fig.4 的实验-QTR 比较，以及补充材料 pp.1-6 的选门与污染检查、完整跃迁表和逐带 QTR 波函数成分。

本页按 `experiment-ingest + project-ingest` 建立反对方证据链。它不把 Lv 2022 的作者结论写成本 Wiki 的最终裁决。补充材料作为主论文附属证据层挂接到本 source，不另建 source、DOI 或 BibTeX 条目。

## Supplementary Material Record

- 文件：`raw/papers/2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr supplementary.pdf`
- SHA-256：`C25CF17CE10EFB2D62FC27A665082DF7BFFEB30F0044726B2730754B035BF225`
- 证据边界：该文件补充主文的实验与 QTR 细节，不具有独立文献身份；所有新增 claims 仍引用 `lv_2022_Evidencewobbling`。

## Summary

作者用独立的 JUROGAM II 数据同时测量 two-point angular-correlation ratio `R_ac` 与 linear polarization，重新确定三条关键 connecting transitions 的 mixing ratio。所得 `|δ|<1` 被作者解释为 M1-dominated，与 wobbling 所要求的 E2-dominated interband links 冲突。作者还重组 Sensharma 2019 的 TW2 候选结构，并用采用标准输入、允许单粒子角动量重排的 QTR 计算，把低激发带解释为 tilted-precession bands。

## Experimental or Theoretical Setup

- 152 MeV `40Ar` 束流轰击 `0.5 mg/cm²` 自支撑富集 `100Mo` 靶，经 `100Mo(40Ar,1p4n)135Pr` 产生 `135Pr`；
- JUROGAM II 包含 24 个 EUROGAM clover 与 15 个 EUROGAM phase-one Compton-suppressed Ge detectors；
- 收集约 `5.1×10^10` 个三重及更高重数 γ 符合事件；
- 用 coincidence、`R_ac` 与 clover linear polarization 联合约束 multipolarity 和 mixing ratio；
- QTR 使用 `ε2=0.16, γ=26°`，采用 irrotational-flow moments of inertia，并允许 single-particle angular momentum 自由重排。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L22-1 | 实验使用 152 MeV `100Mo(40Ar,1p4n)135Pr`、JUROGAM II 的 24 个 clover 与 15 个 phase-one Ge detectors，并收集约 `5.1×10^10` 个 fold≥3 γ 符合事件。 | experimental-fact | direct | p.2, right column, experimental setup | false |
| L22-2 | 本文能级纲图不再把 827、764、1009 keV 三条跃迁组成同一 rotational band；作者建立含 688、871 keV 的 band 4，并把 764 keV 视为可能 band 5 的首条跃迁、827 keV 视为 band 5 到 band 4 的连接。 | experimental-fact | direct | p.2, Fig.1 and final paragraph | false |
| L22-3 | 对 ΔI=1 angular-distribution 数据的 `χ²` 拟合通常可产生 `abs(δ_1)>1` 与 `abs(δ_2)<1` 两个解；本文把 linear polarization 与 `R_ac` 联合作为选择 mixing-ratio 解的实验判据。 | experimental-criterion | direct | pp.2-3, text preceding Fig.2 | false |
| L22-4 | 联合 `P-R_ac` 分析给出 747.3、813.2、450.2 keV transitions 的 `δ=-0.47(+0.09/-0.22)`、`-0.37(+0.10/-0.14)`、`-0.31(+0.10/-0.13)`，三者均满足 `abs(δ)<1`。 | experimental-fact | direct | p.3, Fig.2 and Table 1 | false |
| L22-5 | 作者由上述 mixing ratios 得到 747、813、450 keV transitions 分别约 82%、88%、91% 的 magnetic character。 | experimental-fact | direct | p.3, left column, paragraph below Fig.2 | false |
| L22-6 | 755.1 keV connecting transition 太弱而不能提取 polarization asymmetry；其 `R_ac=0.50(6)` 与 813.2 keV 的 `0.48(6)` 接近，作者据此提出两者可能有相近的 `δ` 解。 | experimental-fact | direct | p.3, Table 1 and paragraph below Fig.2 | false |
| L22-7 | 本文报告 `B(E2;747)/B(E2;526)=0.7(+0.7/-0.5)`；作者认为相近的两条 E2 strengths 与把 band 3 视为相对 band 1 的 one-phonon wobbling excitation 不相容。 | experimental-fact | direct | p.3, left column, final paragraph | false |
| L22-8 | Lv 等指出 Matta 2015 在六条候选 wobbling links 中仅对 747、813 keV 给出 polarization，且只使用 polarization 的正负号而非幅度选择 `abs(δ)>1` 解；正号本身不唯一选出大 `abs(δ)`。 | author-interpretation | direct | pp.2-3, discussion before Fig.2 | false |
| L22-9 | Lv 等指出 Matta 2015 的 747、813 keV polarization 与随后使用相同反应和装置的 Garg 2015 结果存在矛盾；后续 erratum 与 Matta 较接近，但相关分析仍曾受到质疑。 | author-interpretation | secondary-comparison | p.2, left column, discussion of Refs.10, 21, 23, 24 | false |
| L22-10 | Sensharma 2019 对 450、551、519 keV links 只使用 angular distribution 与 DCO-like measurements，未给出 polarization；本文测得 450.2 keV 的 `abs(δ)<1`，作者据此反对其 two-to-one-phonon link 解释。 | author-interpretation | direct | pp.2-3, Fig.2 and Table 1 | false |
| L22-11 | 作者把关键 links 的 M1-dominated character、747/526 E2-strength ratio 与能级重组联合解释为反对 band 3 的 one-phonon 和第二个 `19/2-` state 的 two-phonon wobbling 性质。 | author-interpretation | direct | p.3 and p.5, Summary | false |
| L22-12 | 本文 QTR 使用 `ε2=0.16, γ=26°`、irrotational-flow moments of inertia 与 unfrozen single-particle angular momentum；作者将其与先前为维持 short-axis precession 而调整参数和冻结单粒子取向的计算作对照。 | model-result | direct | pp.4-5, model discussion | false |
| L22-13 | 作者在 p.5 正文报告：标准输入 QTR 中五条带均显著受到 Fig.3(d) 所示 single-particle excitation 机制影响，并发生 single-particle 与 total angular momenta 从 short axis 向 intermediate axis 的快速 realignment；逐带性质的细节指向 supplementary material。Fig.4(c) 只显示近似恒定且接近最大值的 `j_parallel=<I·j>/abs(I)`，支持两角动量近乎平行、同步演化，并不直接显示主轴分量。QTR 对 bands 1、3、4 的能量及 747/813 keV mixing ratios、813 keV transition ratio 给出较好比较；作者据此将这些带解释为基于 `πh11/2` 的 tilted-precession bands。 | model-result | direct | pp.4-5, Fig.3(d) as mechanism sketch; p.5 paragraphs before Fig.4 and Summary; Fig.4(a-d) | false |
| L22-14 | 补充材料给出 747、813、450 keV polarization gates 的逐项污染检查：747 keV 使用 450 keV gated spectra；813 keV 只采用 796 keV suitable gate，并排查邻近 `136,137Nd` 线；450 keV 使用 747 keV gate，并以窄 gate 排除邻近 `136Nd` 449 keV line。作者据联合 `P-R_ac` 中心值选择 `δ`，其误差传播自 `P` 与 `R_ac`，而非不同 `σ/I` 本身。 | experimental-criterion | direct | supplementary material pp.1-4, Figs.2-5 | false |
| L22-15 | 补充 QTR 计算采用 `ε2=0.16, γ=26°`、Harris `J0=J1=12.5`（相应单位）、10 个负宇称轨道、`g_s,eff=0.6g_s,free` 与 `g_core=Z/A`，不使用 frozen approximation，也不增强 short-axis moment of inertia。波函数把 bands 1-5 描述为 orbitals #14/#15/#16 的竞争与随自旋向 intermediate axis 的 realignment；single-particle 与 total angular momenta 同步转向且相对夹角近乎不变。 | model-result | direct | supplementary material pp.4-6, calculations section | false |
| L22-16 | 主文Table1列P：747.3为.04(+.08/−.13)、813.2为−.03(+.05/−.12)、450.2为−.07(+.09/−.10)；SI Table1另列Ap分别.006(+.012/−.019)、−.004(+.007/−.016)、−.017(+.022/−.023)。二者是同一次acquisition的A与P，不是两份独立偏振数据。 | published-observable-identity | direct-and-self-audit | mainp3 Table1；SIp5 Table1 | true |
| L22-17 | SI Eq1的Rac是target在157.6+133.6度对75.5+104.5度、同all-detector轴gates的强度比。Eq2给P=Ap/Q、Ap=(aNperp−Nparallel)/(aNperp+Nparallel)，a(E)=.9844(21)+2(1)×10^−5 E；Q另采用Herzan2015 Ref6，不是继承该文的a。 | geometry-and-calibration-definition | direct | SIp1 Eq1/2及两段说明 | true |
| L22-18 | SI称sigma为spin projection的variance但未在该段给Gaussian指数式；该字面用语不能自动认证D96 Eq19的std。主文/SI未给a0/a1、Q的p0/p1或P与Rac的完整joint Cov。引用的marginal error传播说明不等于提供了完整likelihood。 | width-and-covariance-boundary | direct-and-self-audit | SIp4 error-propagation段；SIp1 calibration段 | true |
| L22-19 | Fig2中旧角分布是重用Matta2015/Sensharma2019；747图的旧大/小模曲线标delta−1.24/−.64，813图为−1.54/−.5；新JUROGAM数据另以green/right axis及新P-Rac点给出。旧曲线再分析不能另算一份独立采集，也未由图标给出小模解的jointCI。 | shared-data-and-branch-identity | direct-and-self-audit | mainp3 Fig2(a–f)及图注 | true |

## Nuclear Structure Information

- band 1 对应既有 [[135pr-yrast-band]]；
- band 3 对应 Matta 2015 的 [[135pr-side-band]]；
- Lv 2022 把 Sensharma 2019 的 [[135pr-second-side-band]] 重组为 band 4 与可能的 band 5，不接受原 TW2 grouping；
- 747、813、755 keV 是 band 3→band 1 links；450 keV 是 band 4→band 3 link。

## Authors' Interpretation

- `|δ|<1` 与 M1-dominated links 不满足 wobbling 的 E2-dominated connecting-transition criterion；
- band 3 不应解释为 one-phonon wobbling，第二个 `19/2-` state 不应解释为 two-phonon wobbling；
- 低激发带更适合解释为 tilted-precession bands。

这些是 Lv 2022 的 counter-interpretation，不是本 Wiki 的最终裁决。

## Model Results

- 标准输入 QTR 允许 rotational、Coriolis-favored short-axis 与 single-particle excitation 三种机制竞争；
- Fig.3(d) 只示意 single-particle excitation 可导致 gradual realignment，并非 bands 1-5 的逐带结果图；
- p.5 正文称五条计算带均显著受该机制影响并发生快速 realignment，逐带性质的细节位于 supplementary material；
- Fig.4(c) 的 `j_parallel` 近似恒定且接近最大值，只支持 single-particle 与 total angular momenta 近乎平行、同步演化，不直接给出主轴分量；
- QTR 对 bands 1、3、4 的能量再现较好，对 bands 2、5 尤其高自旋处有高估；Fig.4(b,d) 比较 747/813 keV mixing ratios 与 813 keV transition ratio。

## Competing Interpretations and Limitations

- 本文是 wobbling 反对方原始实验；其 TiP/realignment 解释仍是模型依赖结论；
- 755 keV 缺 polarization，551 与 519 keV links 未在本文给出新的联合 `P-R_ac` mixing ratios；
- 对 Matta/Garg/erratum 的 polarization 争议涉及多篇来源；在这些来源分别摄入前，本页只记录 Lv 2022 的比较性陈述；
- band 5 部分结构依赖此前报告但本实验未观察到的 1009 keV transition；
- QTR 对 bands 2、5 的高自旋能量仍有偏差。

## Extracted Pages

- Nucleus: [[135pr]]
- Bands: [[135pr-yrast-band]], [[135pr-side-band]], [[135pr-second-side-band]], [[135pr-signature-partner-band]]
- Experiment: [[jyfl-jurogam2-135pr-ar40-152mev]]
- Concepts: [[wobbling-motion]], [[transverse-wobbling]]
- Observables: [[multipole-mixing-ratio]], [[interband-e2-strengths]]
- Methods: [[two-point-angular-correlation-ratio]], [[linear-polarization-asymmetry]]
- Model: [[triaxial-particle-rotor-model]]
- Project: [[135pr-wobbling-controversy]]

## Personal Notes

本页建立 counter-source，不裁决争议。用户已完成 source 页面及 L22-1 至 L22-15 的核对，并校正 L22-13 对 Fig.3(d)、p.5 正文与 Fig.4(c) 的证据边界；全部 claims 均为 `needs_review: false`。

## 2026-10-17定向复核：标定谱系与逐量对齐

本次核主文6页、SI7页与各自SHA-256，读实验/分析/反证/QTR主线；视觉核主文Fig2/Table1、SI Eq1/2、SI Table1及Fig3–5的门和污染标签。旧L22-1–15及page级human-reviewed保持；Personal Notes原称“全部claims false”只指当时1–15。新L22-16–19及本节仅Codex self-audit，needs_review:true，不属新增人审。

按SI明确采用的[[herzan-2015-193bi-spectroscopy]] HE15-10，Qpoint=(1+x)/(1+x+x²)、x=E/(me c²)，Q=Qpoint[.42−1.9×10^−4 E(keV)]。[[135pr-mixing-branch-input-contract]]的新计算用独立原件的Q中央系数把SI Ap及其误差尺度变回主文P，三线均在印刷rounding内闭合。它确认两张表的数据身份，不证明完整误差预算已包含/漏掉Q误差，也不恢复原counts/fit Cov。

本文a(E)与Herzan Fig3的a(E)不同；所采用的是其Q(E)，不能因同阵列名称一并复制所有calibration。原件SI p4的width措辞按L22-18保留，不把它改写为方差或标准差已核准的Gaussian prior。没有用本任务integer-only kernel计算135Pr半整数响应，作者模式解释和反方/后续支持方仍并列。


## Day18定量审计：混合比倒转对跃迁强度的塌缩效应核验

在Day18正式学习中对本文Table 1中135Pr带间跃迁数据进行定量提取审计，raw SHA256 `4B87C540BF9DA5141FA88EF8F00859162CB08918D56A5DA74726C7537DF5E26B`已核。原LV22各claim及`human-reviewed`状态完全保留；新LV22P-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LV22P-D18-1 | 本文Table 1中利用线偏振 $P$ 与角分布比 $R_	ext{ac}$ 确立 747、813、450 keV 跃迁的混合比分别为 $-0.47$、$-0.37$、$-0.31$（$E2$ 份额为 $18.1\%$、$12.0\%$、$8.8\%$），与早期报告的 $E2$ 主导（$60.6\%$、$70.3\%$）相比，813 keV 的带间比值 $B(E2)_	ext{out}/B(E2)_	ext{in}$ 由 0.843 崩塌至 $0.12(8)$（降至 $1/7.0$）。这从实验上排除了低自旋wobbling解释，提供了多极混合比裁决对跃迁强度提取起生死作用的最关键证据。 | task-sensitivity-and-counterevidence | derived-and-boundary | PDF p.3 Table 1；新matta15-lv22-135pr-result-018 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/matta15-lv22-135pr-contract-018.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/matta15-lv22-135pr-result-018.json)4项检查全过。
