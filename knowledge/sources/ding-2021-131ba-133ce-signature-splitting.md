---
type: source
title: "Signature splitting of the g7/2[404]7/2+ bands in 131Ba and 133Ce"
aliases: []
created: 2026-07-01
updated: 2026-09-28
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Signature splitting of the g7/2[404]7/2+ bands in 131Ba and 133Ce"
authors: [B. Ding, et al.]
journal: Physical Review C
year: 2021
volume: 104
pages: 064304
doi: 10.1103/PhysRevC.104.064304
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevC.104.064304
zotero_item_key:
citation_key: ding_2021_Signaturesplittinga
zotero_uri:
library_file:
raw_file: "raw/papers/2021_Ding et al_Signature splitting of the g 7 - 2 [ 404 ] 7 - 2 + bands in Ba 131 and Ce 133.pdf"
raw_sha256: 752D3C5DA690C20EC7E188DCC043F9DA2A7F062DEEFC371DD8A497A190B66C37
alternate_version_file: "raw/papers/gpt/high-spin-20260920/旋称/2021_Ding et al_Signature splitting of the g 7 - 2 [ 404 ] 7 - 2 + bands in Ba 131 and Ce 2.pdf"
alternate_version_sha256: 47451ae95676399c72b907b0efa10bdeb07e82c794a1ed480759ee20bae0c652
alternate_version_identity: "PRC 104, 064304 published PDF; same title/DOI and fifteen-page article"
nuclei: [131ba, 133ce]
reactions: [122sn-c13-4n-131ba, 125te-c12-4n-133ce]
experiments: [galileo-131ba-c13-65mev, afrodite-133ce-c12-57mev]
models: [cranked-shell-model, triaxial-particle-rotor-model]
observables: [signature-splitting]
methods: [gamma-gamma-coincidence, two-point-angular-correlation-ratio]
tags: [a130, signature-splitting, strong-coupling, in-beam-spectroscopy, n73-systematics, n75]
---

# Ding 等（2021）：`131Ba` 与 `133Ce` 的 νg7/2[404]7/2+ 旋称劈裂

## Bibliographic Record

Physical Review C 104, 064304 (2021)，DOI `10.1103/PhysRevC.104.064304`。本地 PDF 首页是 2021-11-09 稿本，期刊元数据按正式发表记录填写。

## Scope and Reading Depth

规范期刊版已全文精读；本批提供的十五页 PRC PDF was reread end-to-end to audit Fig.1 schemes, Tables I–II, Figs.4–10 systematics/QTR sensitivity, Table III PES parameters and summary. No material claim change was found.

## Summary

作者在 N=75 同中子异位素 `131Ba` 和 `133Ce` 中建立强耦合正宇称 band 2，并指认为 `νg7/2[404]7/2+`。两条带的 signature splitting 明显大于奇质子 Ta/Re 类比，模型分析表明劈裂不是单一 γ 形变刻度：近邻 `νs1/2[400]1/2+` 的 Coriolis 混合可在较小 γ 下产生 staggering，而较强非轴形变也会增强其幅度。

同一论文还汇编 N=73 `129Ba`、`131Ce`、`133Nd` 的既有 `νg7/2[404]7/2+` 带数据作为组态系统学。Fig.4/5 captions 将三核数据分别追溯到 refs.46/47/48（Byrne 1992、Palacz 1991、Bazzacco 1998）；该层是对旧实验的 contextual comparison，不是 Ding 2021 对三核开展的新测量，也不增加独立 `131Ce` 实验谱系。

## Experimental or Theoretical Setup

### `131Ba`

- 反应：`122Sn(13C,4n)131Ba`；
- 束流：65 MeV、5 pnA `13C`，Legnaro XTU Tandem；
- 靶：两层各 0.5 mg/cm² self-supporting `122Sn`；
- 阵列：GALILEO 25 HPGe；EUCLIDES 与 Neutron Wall 作道选择；
- 数据：`1.2×10^9` 个 fold≥3 events。

### `133Ce`

- 反应：`125Te(12C,4n)133Ce`；
- 束流：57 MeV、5 pnA `12C`，iThemba LABS；
- 靶：2 mg/cm²、95.3% 富集 `125Te`，8 mg/cm² Au backing；
- 阵列：AFRODITE 8 个 Compton-suppressed clover；
- 数据：`2.8×10^10` 双符合和 `5.4×10^9` 三重及以上符合 events。

### 理论

configuration-constrained PES、cranked shell model（CSM）和 quasiparticle-plus-triaxial-rotor（QTR）。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| D21-1 | `131Ba` band 2 建于 525.3 keV、7/2+ 态，`133Ce` band 2 建于 340.3 keV、7/2+ 态；两者均形成强耦合 ΔI=1 结构。 | experimental-fact | direct | PDF pp.3-8, Fig.1, Tables I-II | false |
| D21-2 | 作者将两条 band 2 指认为 `νg7/2[404]7/2+`，依据包括带性质、N=73/75 系统学、alignment/Routhian 和 PES 带头能量。 | author-interpretation | indirect | PDF pp.6-9, Figs.4-5, Table III | false |
| D21-3 | N=75 的 `131Ba`、`133Ce` 中子 g7/2 带劈裂幅度约为奇 Z Ta/Re 质子 g7/2 带的十倍。 | experimental-fact | contextual | PDF pp.9-10, Figs.5-6; p.12 Summary | false |
| D21-4 | CSM 在低频、γ=0° 时预测几乎无劈裂；γ≈10° 后出现，幅度随 γ 增加。 | model-result | direct | PDF p.11, Fig.7 | false |
| D21-5 | QTR 用 γ=10° 描述 `133Ce`、γ=15° 描述 `131Ba` 的 S(I)，同时波函数含有近邻 `s1/2[400]1/2+` 小分量。 | model-result | direct | PDF pp.11-12, Figs.8-9 | false |
| D21-6 | 衰减 Coriolis 耦合后，γ≤15° 的计算几乎不产生 staggering，而 γ>15° 仍可产生显著劈裂；作者据此认为低-j 混合和非轴性是两个竞争机制。 | model-result | direct | PDF p.12, Figs.8-9 | false |
| D21-7 | PES 对 7/2+ 候选给出 `131Ba: β2=0.180, γ=9.1°`，`133Ce: β2=0.195, γ=-10.5°`；这些是模型极小值，不是直接实验形变。 | model-result | direct | PDF p.13, Table III | false |
| D21-8 | 作者把 N=73 `129Ba`、`131Ce`、`133Nd` 的 `νg7/2[404]7/2+` 带作系统比较：首次 up-bending 前的 initial alignment 和 `J^(2)` 相近，且三带分别延伸到 `55/2+`、`51/2+`、`67/2+`，被解释为共同组态的 contextual support；三核旧数据分别引自 refs.46/47/48。 | author-interpretation | contextual | PDF pp.5-6, Figs.4-5 and captions; p.9, Fig.6 and paragraph below; refs.46-48 on pp.14-15 | true |
| D21-9 | 作者在 Nilsson 图中提出 N=74 的 `νg7/2[404]7/2+` 与 `νh11/2[514]9/2−` 间隙，并用它定性解释 N=73 相对 N=75 同中子数核的激发能与布居差异；这是模型解释，不是直接测得的能隙。 | model-result | direct | PDF p.10, discussion before Sec. III.C; Figs.4-5 | true |
| D21-10 | Table II 明确将 133Ce 约 2.73 MeV 处列为两个分立母态 2733.9(19/2+) 与 2739.3((19/2+))，分别经 881.4 与 886.8 keV 射线退激至 1852.5 keV(15/2+)，两线中心闭合残差严格为 0.0 keV；依注 a 弱线(Iγ≤10)误差为 ±0.8 keV，证明两态独立存在。 | experimental-fact | direct | PDF p.8, Table II | true |

## Nuclear Structure Information

- 两核都是 `N=75`；
- band 2 的带头分别为 `131Ba` 525.3 keV、`133Ce` 340.3 keV；
- `131Ba` 7/2+ band 2 与 band 3 的 7/2+ 态仅差约 18 keV，存在组态混合；
- `133Ce` 类似近简并出现在 13/2+ 态附近；
- 作者估计这种局部近简并混合本身对整体 splitting 幅度贡献较小，但 QTR 中与 `s1/2` 轨道的全局 Coriolis 混合很关键。
- N=73 `129Ba/131Ce/133Nd` 的高自旋 `[404]7/2+` 系统学来自引用文献的既有数据；本页只把它作为 configuration comparison，不把它计为新的独立实验。

## Authors' Interpretation

两条带是首次在 N=75 同中子异位素中识别的 `νg7/2[404]7/2+` 强耦合带。signature splitting 同时反映形变非轴性和单粒子谱中近邻低-j 轨道的位置，不能作为 γ 的单变量测量。

## Model Results

- CSM 展示 γ 增大会增强 signature splitting；
- QTR 同时改变 γ 和 Coriolis attenuation，分离两个机制；
- PES 给出各一准粒子组态的 β2、γ、β4 和带头能量；
- QTR 与 PES 使用的参数化和 γ 符号约定不完全相同，不能逐数值直接等同。

## Competing Interpretations and Limitations

- 组态指认依赖系统学和多个模型，不是由单一跃迁直接测量；
- `S(I)` 对 γ、Coriolis mixing、近邻轨道、配对和转动惯量均敏感；
- QTR 的 γ=10°/15° 是最佳描述输入，不构成 γ-rigid 证据；
- 两实验使用不同阵列和 `R_ac` 标定值，比较弱跃迁时需保留装置系统差异。
- D21-8 的 N=73 比较依赖 refs.46/47/48 的旧能级和 alignment 数据；本轮只核对了 Ding 对三条来源谱系的归属，未读取这三篇原始全文。若用于精确 band crosswalk 或论文主张，仍需逐核回到 Byrne 1992、Palacz 1991 与 Bazzacco 1998 核验。

## Extracted Pages

- Nuclei: [[131ba]], [[133ce]]
- Bands: [[131ba-band-2]], [[133ce-band-2]]
- Experiments: [[galileo-131ba-c13-65mev]], [[afrodite-133ce-c12-57mev]]
- Concepts: [[triaxial-deformation]], [[signature-partner-bands]]
- Models: [[cranked-shell-model]], [[triaxial-particle-rotor-model]]
- Observables: [[signature-splitting]]
- Methods: [[gamma-gamma-coincidence]], [[two-point-angular-correlation-ratio]]
- Synthesis: [[signature-splitting-mechanisms]]

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: 本页此前主要承载 N=75 `131Ba/133Ce` 新实验与 splitting 机制。
- Effect of this on-touch check: revises the project relation, not the paper conclusion.
- Reason: PDF p.9/Fig.6 还包含直接相关的 N=73 `129Ba/131Ce/133Nd` 组态系统学，但它是引用旧实验的 contextual evidence。
- Persistence decision: add D21-8 and connect it to the `131Ce` project while preserving the independence limit.
- Review state: page-level `human-reviewed` remains unchanged; D21-8 starts as `needs_review: true`.
- 2026-08-19 locator audit: expanded D21-8 from the p.9 summary paragraph to the actual Fig.4/5 observable panels and refs.46-48 source lineage; scientific ranking and review state are unchanged.

## Alternate-version self-audit (2026-09-20)

- The supplied PRC PDF reproduces the canonical source's two reactions, `1.2×10^9`/`2.8×10^10` event totals, `R_ac` calibration, `νg7/2[404]7/2+` assignments, CSM/QTR/PES calculations and the conclusion that low-j `s1/2` mixing and triaxiality compete.
- It is the same experiment/paper version, not an independent measurement. The existing human-review record remains unchanged; this alternate-version check is Codex self-audit.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[131ce-collective-mode-discrimination]] | N=73 `[404]7/2+` systematics strengthen a configuration-specific comparison for the positive-parity `131Ce` sequence, but do not supply new target-nucleus electromagnetic evidence. |

## Human Review Triage

### P0

- None identified.

### P1

- `D21-8`, PDF pp.5-6/Figs.4-5, p.9/Fig.6 and refs.46-48 — verify that the compiled `129Ba/131Ce/133Nd` alignment and spin-extension comparison is accurately bounded as contextual support from prior experiments. The exact citation lineage is now explicit, but the three original papers have not been re-read. Risk if skipped: a useful isotone comparison could be miscounted as an independent Ding 2021 measurement or generalized to unrelated `h11/2` bands.
- `D21-9`, PDF p.10 — the N=74 `νg7/2`–`νh11/2` gap is a Nilsson-model interpretation used to explain the N=73/N=75 systematics; it is not a measured level spacing. This claim was added after the existing human-review scope and remains `needs_review: true`.

### P2/P3

- P2: the new project relation and N=73 tag. P3: date/navigation metadata.

## Personal Notes

这篇论文对知识库的关键贡献不是“用 splitting 测出 γ”，而是说明这一反演通常不唯一：低-j 轨道位置与 Coriolis 混合会和非轴形变共同控制可观测 staggering。

## Day19量化审计：旋称劈裂双机制简并性、(gamma, xi)山谷与电磁比解耦

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_signature_splitting_coriolis_audit.py` 的 11 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/signature-splitting-coriolis-result-039.json`，系统核准了 $N=75$ 强耦合能带旋称劈裂的竞争机制反演简并性定理：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| D21-D19-1 | 在 $N=75$ 同中子异位素（$^{133}\text{Ce}$ 与 $^{131}\text{Ba}$）中，强耦合带（$\nu g_{7/2}[404]7/2^+$）实测出交替的强旋称劈裂（$^{133}\text{Ce}$ 的 $S(11/2) \approx +29.0\text{ keV}$；$^{131}\text{Ba}$ 的 $S(11/2) \approx +52.8\text{ keV}$），其幅度达到奇 $Z$ 核 Ta/Re 质子 $g_{7/2}$ 类比带的 10 倍以上。理论审计证实该劈裂由三轴非轴性（$V_{\text{tri}} \propto \sin\gamma$）与近邻低-$j$ 轨道（$\nu s_{1/2}[400]1/2^+$，解耦参数 $a \approx 1$）的科里奥利混合共同驱动，且在能谱上形成连续的单参数简并山谷：实测 $S(11/2) = 29.0\text{ keV}$ 既可由中等形变加全科里奥利耦合（$\gamma = 10^\circ, \xi = 0.92$）精确复现，亦可由大三轴形变加重度衰减耦合（$\gamma = 26^\circ, \xi = 0.0$）复现。因此，仅凭能级旋称劈裂无法独立反演三轴形变 $\gamma$。打破该简并的排他观测量为跃迁几率比 $B(M1)/B(E2)$：纯三轴转子导致平滑的 $B(M1)/B(E2) \approx 0.23\ (\mu_N/e\text{b})^2$；而 $s_{1/2}$ 轨道的大自旋回转因子（$g_s = -3.826$）在科里奥利混合下必然引发 $>3.5$ 倍的 $B(M1)/B(E2)$ 奇偶交错震荡（$0.42 \text{ vs } 0.11$）。 | quantitative-audit-and-criterion | derived-and-source-boundary | PRC 104, 064304 pp.9-12; Figs.5,8-9; signature-splitting-coriolis-result-039.json | true |

## Day23：稿本、正式版与学位论文的装置和模型输入交叉核查

本轮定向原读两份本地Ding：规范raw实际16页（Nov9,2021稿本，SHA752d3c5da690c20ec7e188dcc043f9da2a7f062deefc371dd8a497a190b66c37），alternate正式PRC15页（SHA47451ae95676399c72b907b0efa10bdeb07e82c794a1ed480759ee20bae0c652）。具体§II.A、QTR段和PES表视觉核，不新增“再次全文已读”声明。旧human-reviewed与旧claim flags保持，本节仅新Codex self-audit。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| D21-D23-064-1 | 两Ding版本均报告133Ce AFRODITE8clovers、4@90°+4@135°；学位论文具体实验段为13、1@45°+8@90°+4@135°。两边57MeV/5pnA、Te2/Au8mgcm−2、double2.8e10/≥triple5.4e9等字段对应，构成强同源候选，但actual8/13需run/event ledger，不按两份Ding+thesis算三次独立采集。 | source-dependency-and-apparatus-conflict | direct-original-and-explicit-readiness | manuscriptPDF2 §II.A; published064304-2 §II.A; WakudyanayePDF61 §5.2.1 | true |
| D21-D23-064-2 | 两版QTR正文均给Ce ε2=.185/γ10°/ε4=.01，Ba .170/8°/.003；PES TableIII用Woods–Saxon β，Ce7/2+为.195/−10.5°/−.023，不能把ε2≈.95β2套给四阶参数，也不能据论文描述静默修thesis表.1为.01或冒actual input。 | model-input-version-and-parameterization | direct-original | manuscriptPDF11 §III.C and PDF13 TableIII; published064304-10 §III.C and064304-8 TableIII | true |
| D21-D23-064-3 | 两Ding的QTR wavefunction讨论仅定性主g7/2加附近s1/2，未给与thesisTable6.3相同逐态完整系数；不能修thesis9/2+的.982归一。intrinsic轨道20展开与QTR总态Kν展开、不同核/γ版本分别处理。 | wavefunction-identity-and-input-gap | direct-original-and-bounded-comparison | manuscriptPDF11–12 QTR discussion; published064304-10–11; WakudyanayePDF78 Table6.2 andPDF82 Table6.3 | true |
| D21-D23-064-4 | 本文alignment图所用Harris参考J0=13.4/J1=33.2，与thesisQTR核芯10.4/35.7用途不同；稿本/正式版页码、Ref号也不同。不能因同名Harris或同source题名直接置换。 | analysis-reference-versus-model-input | direct-original | manuscriptPDF6 alignment paragraph; published064304-5; WakudyanayePDF78 §6.2.1 | true |

装置冲突不撤销原实验谱学/模型支持；它限制重放共同response。[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]和[[133ce-thesis-analysis-blueprint]]保存本轮分析蓝本，不把输出历史认证当事实源。需要detectorID/active mask/角度表/45°事件、sorting geometry版本和逐线选门，而非擅补一套响应。
