---
type: source
title: "Lubos 2016 博士论文：100Sn 及邻近核素衰变谱学"
aliases: [Lubos 2016 100Sn thesis, Decay Spectroscopy of 100Sn and Neighboring Nuclei]
created: 2026-09-05
updated: 2026-09-07
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment
reading_depth: deep-read
title_original: "Decay Spectroscopy of 100Sn and Neighboring Nuclei"
authors: [Daniel Georg Lubos]
advisor: [Reiner Krücken, Stefan Schönert]
journal: "Technical University of Munich doctoral dissertation"
year: 2016
volume:
pages: 111
doi:
arxiv:
language: en
canonical_source: "Lubos, Daniel Georg. Decay Spectroscopy of 100Sn and Neighboring Nuclei[D]. Technical University of Munich, 2016."
zotero_item_key:
citation_key: ""
zotero_uri:
library_file: "raw/papers/degree dissertation/Decay Spectroscopy of 100 Sn and Neighboring Nuclei.pdf"
raw_file: "raw/papers/degree dissertation/Decay Spectroscopy of 100 Sn and Neighboring Nuclei.pdf"
raw_sha256: "C9AA0494F29BACC00EC8FB0055A5D6AC201237E3BAD943EA34D350DEEB8550D9"
nuclei: [100sn, 96cd, 98in, 94ag, 90rh, 99sn, 97in, 95cd, 91pd, 93ag, 96in, 94cd, 92ag, 90pd, 98cd]
reactions: ["124Xe projectile fragmentation on 9Be at 345 AMeV"]
experiments: []
models: [large-scale-shell-model, maximum-likelihood-analysis]
observables: [half-life, q-value, gamow-teller-strength, proton-branching-ratio]
methods: [decay-spectroscopy, beta-gamma-coincidence, maximum-likelihood-analysis, positron-calorimetry]
tags: [a100, 100sn, decay-spectroscopy, riken, gamow-teller, proton-dripline, phd-thesis]
---

# Lubos 2016：`100Sn` 及邻近核素衰变谱学

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

Daniel Georg Lubos，*Decay Spectroscopy of 100Sn and Neighboring Nuclei*，Technical University of Munich，博士学位论文，2016，111 页。原始 PDF SHA-256 为 `C9AA0494F29BACC00EC8FB0055A5D6AC201237E3BAD943EA34D350DEEB8550D9`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: Abstract、Chapters 1–4、Summary/Prospects；核对 RIKEN BigRIPS、WAS3ABi、EURICA、MLH、Q-value/positron response、`100Sn` BGT、`98In/94Ag/90Rh` isomers、N=Z−1/−2 half-lives 和 proton emission。
- Not covered: 全部引用文献独立复核、补充实验 proposal 的后续结果。
- Coverage caveats: 多核素 half-life/Q-value 表格含不同 decay components 和 model assumptions；需按核素、isomer 和 decay branch 分层。

## Paper Question and Scientific Motivation

论文围绕 `100Sn` 及 N=Z、N=Z−1、N=Z−2 邻近核素，测量 half-lives、Q-values、γ/β branching 和 proton emission，以检验壳模型、GT strength、CVC/rp-process 与质子滴线结构（Abstract；Ch.1）。

## Method and Design Logic

实验在 RIKEN RIBF 用 345 AMeV `124Xe` + `9Be` projectile fragmentation，经 BigRIPS 识别并将 A≈100 cocktail 植入 WAS3ABi；EURICA 记录 decay γ，Si array 同时进行 β/positron calorimetry。MLH、Bateman/decay-correlation、`χ²` Q-value fitting 和 branching analysis 将多核素衰变链分离（Chapters 2–4）。

## Key Evidence and Reasoning Chain

1. BigRIPS PID 和 WAS3ABi implantation/decay correlation 确认 `100Sn` 与邻核。
2. Unbinned MLH/decay-chain models 提取多核素 half-lives。
3. `χ²` positron-energy fit 结合 detector response、bremsstrahlung、annihilation 和 implantation geometry 得到 Q-values。
4. EURICA γ/γγ、β-delayed p branches 和 decay components 约束 `100In/98In/94Ag/90Rh` level/isomer structure。
5. `100Sn` half-life+Q-value 得到 `BGT`，与 large-space shell model 比较。

## Summary

在 RIKEN 实验中识别 2525 个 `100Sn`，得到 `T1/2=1.17±0.10 s`、`Q=3.74±0.14 MeV`、`BGT=5.26(+0.90/-1.06)` 和 `log(ft)=2.86±0.08`。确认 `100In` 既有 level ordering，并提出约 50 keV `5+→6+` link candidate。论文还报告 N=Z−2 核素首次识别/寿命、`93Ag` proton emitter `228±16 ns`、`90Rh` long-lived `5+` isomer candidate，以及 `98In` 9+ isomer/双 decay components。各项结论需按 decay chain 和 branch 的证据强度分开。

## Experimental or Theoretical Setup

- RIKEN BigRIPS、WAS3ABi、EURICA；`124Xe` 345 AMeV + `9Be`。
- MLH/Bateman、implantation-decay correlations、positron calorimetry、Q-value fit、γ/γγ coincidence。
- Large-scale shell model、CVC/rp-process 和 proton-emission interpretation。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| LB16-1 | RIKEN `124Xe+9Be` 345 AMeV、BigRIPS/WAS3ABi/EURICA 实验识别 2525 个 `100Sn` 并同时测邻近 A≈100 核素。 | experimental-fact | direct | single | Abstract；Ch.2；Ch.4 | true |
| LB16-2 | `100Sn` half-life 为 `1.17±0.10 s`，Q-value 为 `3.74±0.14 MeV`，由 `BGT=3811.5/[f(Z,Q)T1/2]` 得到 `BGT=5.26(+0.90/-1.06)`、`log(ft)=2.86±0.08`。 | derived-observable + method-formalism | direct | single | Ch.4.4.1–4.4.2 pp.77–81；Eqs.4.19–4.27；Ch.5.1 p.83 | true |
| LB16-3 | `100Sn` β-delayed γ spectroscopy 支持既有 `100In` level ordering；96/141/436 keV 强度近似相等、1297/2048 keV 为两条分支，并提出约 50 keV `5+→6+` link candidate；LSSM 预言的额外弱分支尚未观测。 | experimental-fact + analytical-boundary | indirect | single | Ch.4.2 pp.70–75；Fig.4.17–4.20；Ch.5.1 pp.83–84 | true |
| LB16-4 | N=Z−2 `96In,94Cd,92Ag,90Pd` 首次识别并测寿命；N=Z−1 核素 half-lives 约 27–33 ms。 | experimental-fact | direct | single | Abstract；Ch.4.1；Table 5.1 | true |
| LB16-5 | `93Ag` 被确认是质子发射体，半衰期 `228±16 ns`；`94Ag` 的已报道 1p/2p emission 在本实验未观察到。 | experimental-fact | direct | single | Abstract；Ch.4.13–4.16；Ch.5.1 | true |
| LB16-6 | `98In` decay curve 含 T=0/T=1 fast/slow components，并支持 9+ isomer 与 `98Cd` 8+/10+ daughter branches；level ordering 仍有讨论。 | experimental-fact + author-interpretation | indirect | single | Ch.4.8–4.10；Ch.5.1 | true |
| LB16-7 | `90Rh` 具有 long-lived isomer candidate，γ spectroscopy 给出 `90Ru` daughter ordering 和新 1163/1316 keV lines，`5+` spin-parity 为 tentative。 | experimental-fact + author-interpretation | indirect | single | Ch.4.12–4.13；Ch.5.1 | true |
| LB16-8 | Q-value fit 使用 600–3000 keV 区间、Geant4 positron-response simulation、24 个 `100In` β+ components，显式计入 19.8% daughter contribution 和 96/141 keV conversion-electron deposition；BGT 的系统误差与 fit-range/response 相关。与 Hinke 2010 是独立 RIKEN/GSI experiments，不能简单平均。 | analytical-boundary | inferred | multiple-independent | Ch.4.4.1–4.4.2 pp.77–81；Figs.4.22–4.24 | true |

## Nuclear Structure Information

- `100Sn`：GT decay、Q-value、`100In` low-energy γ scheme。
- `98In/94Ag/90Rh`：odd-odd N=Z isomers、Fermi/GT components、γ/particle branches。
- N=Z−1/−2 核素：half-life、proton emission 和 dripline identification。

## Raw Locator Audit (2026-09-07)

- The corrected Q chain is explicit: raw fit `Q=3.81` with fit-range systematic discussion (p.77), average conversion-electron contribution ≈63 keV from 96/141 keV lines, and corrected `Qcorr=3.74±0.14 MeV` (p.78; Eqs.4.19–4.20).
- The Q spectrum includes 24 simulated `100In` β+ components, 19.8% daughter contribution in the 3 s window, and a statistically useful comparison range of 600–3000 keV (pp.77–78; Fig.4.23).
- `BGT` is calculated from the half-life and Q via Eq.4.25; the thesis attributes the lower value relative to the extreme single-particle 17.78 to large-space/model-space treatment and higher `1+` states, not to a new direct strength observable (pp.80–81; Fig.4.24).

## Authors' Interpretation

作者把 `100Sn` BGT 与 large-space shell model 比较，并把 `93Ag` proton emission、`98In`/`90Rh` isomer 解释放入 N=Z 线和核天体物理背景；对 level ordering、isomer spin 和 missing transitions 保留不确定性。

## Model Results

- MLH/Bateman/response simulation：half-life、Q-value 和 branching extraction。
- LSSM：`100In` level ordering/BGT comparison；CVC/rp-process 用于物理意义讨论。

## Competing Interpretations and Limitations

- Hinke 2010 与 Lubos 2016 的 `100Sn` BGT 不同，来自不同统计、Q-value、response and analysis；差异不能直接写成物理矛盾。
- `100In` 50 keV link、`98In` level ordering、`90Rh` 5+ 和 `94Ag` proton branches 仍需原始谱图/后续 experiment。
- 多核素 half-life table 不等于每个核素拥有相同 detector/branch sensitivity。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-LB16-1 | Core reconstruction | 该论文把 `100Sn` GT/Q-value 与邻近滴线核素 decay spectroscopy 置于同一可复现 MLH/response framework。 | LB16-1–8 | unreviewed |
| AR-LB16-2 | Assumptions and dependencies | Q-value/BGT、isomer half-life 和 branch assignment 依赖 detector response、decay chain 和 branch assumptions。 | Chs.3–4 | unreviewed |
| AR-LB16-3 | Transfer conditions | 可与 Hinke 2010 形成 independent `100Sn` comparison，也可作为 A≈100 decay-spectroscopy 方法基线。 | LB16-2/8 | unreviewed |
| AR-LB16-4 | Failure conditions | 更高统计 γγ/total absorption 或新的 mass/Q measurements 改变 `100In` ordering/BGT 时需修订。 | LB16-3/8 | unreviewed |
| AR-LB16-5 | Reverse/falsification test | 逐核素回查 decay component、Q fit residual、γγ closure、proton branch 和 daughter level ordering。 | Ch.4 tables/figures | unreviewed |
| AR-LB16-6 | Research-question decision | 建立 `100Sn` independent-experiment evidence map，并保留 N=Z dripline 方法桥接。 | LB16-2–8 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: 本轮 Hinke 2010 刚建立 GSI `100Sn` baseline；Lubos 提供独立 RIKEN 高统计更新和邻核扩展。
- Effect of this source: supports and refines；为 `100Sn` BGT/Q-value 和 `100In` level ordering 提供独立实验链，同时引入多核素边界。
- Reason: 两个实验可做独立比较，不应合并统计或视为同一数据集。
- Persistence decision: 新建 source；更新 `100sn` nucleus；不批量建立全部邻核页面。
- Review state: 页面 `unreviewed`；LB16-2–8 保留 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[100sn]] | 提供 RIKEN 独立高统计 `100Sn` decay baseline。 |
| competing-interpretation | [[gamow-teller-strength]] | `BGT` 受 Q-value/response/analysis 条件影响。 |
| methodological-bridge | [[lifetime]] | 多核素 MLH/decay-correlation lifetime extraction。 |

## Human Review Triage

### P0

- LB16-2/LB16-3：核对 `100Sn` T1/2、Q、BGT、log ft、50 keV link 和未观测分支边界。
- LB16-5/LB16-7：核对 `93Ag` proton emitter、`90Rh` 5+ isomer 和新 γ lines 的 assignment 强度。

### P1

- LB16-1/LB16-4：核对 2525 `100Sn`、N=Z−1/−2 sample 和 half-life table。
- LB16-6/LB16-8：与 Hinke 2010 做 independent experiment、response and branch audit。

### P2/P3

- 后续按实际研究问题建立 `98In`/`94Ag`/`90Rh` 页面。

## Extracted Pages

- Nuclei: [[100sn]]。
- Methods: [[lifetime]]、[[gamma-gamma-coincidence]]。

## Non-source Notes and Follow-up

该论文与 Hinke 2010 的 GSI 实验不是同一数据集；两者应作为 `multiple-independent` 证据并列。

## Day19量化审计：高统计Q值拟合、量热计响应与大空间壳模型淬灭符合

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_sn100_gamow_teller_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/sn100-gamow-teller-result-044.json`，系统核准了 Lubos 2016 博士论文关于 $^{100}\text{Sn}$ 高统计衰变谱学与壳模型淬灭的量化事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LB16-D19-1 | Lubos 2016 利用 RIKEN BigRIPS 采集的 2525 个 $^{100}\text{Sn}$ 高统计样本，在正电子量热谱学中通过包含 24 个 $^{100}\text{In}$ 子体成分、19.8% 子体活度贡献及 Geant4 探测器响应的 600–3000 keV 区间拟合，扣除 $-63\text{ keV}$ 内转换电子沉积后提取出精确 $Q_{\text{corr}} = 3.74 \pm 0.14\text{ MeV}$，并导出相空间积分 $f = 619.33$，最终测定 $B(\text{GT}) = 5.26_{-1.06}^{+0.90}$（$\log(ft) = 2.86 \pm 0.08$）。该值与大空间壳模型（LSSM）预言的第一激发 $1_1^+$ 态强度（$B(\text{GT})_{\text{LSSM}} = 5.70$）在 $0.42\sigma$ 内高度吻合，断然排除了极值单粒子模型无淬灭值（$B(\text{GT})_{\text{ESPM}} = 17.78$），证实了在双幻核 $^{100}\text{Sn}$ 处 Gamow-Teller 跃迁依然遵循标准的轴矢量重整化淬灭因子（$g_A/g_V \approx 0.75$，强度淬灭达 $56\%$）。同时，高统计 $\gamma$ 谱揭示的 96、141、436、1297、2048 keV 多分支退激否定了单终态假设，确立了精细探测器量热响应对相空间反演的决定性影响。 | quantitative-benchmark-and-criterion | derived-and-source-boundary | Ch.4.4.1-4.4.2 pp.77-81; Eqs.(4.19)-(4.27); sn100-gamow-teller-result-044.json | true |

## Day21周考推断阶梯审计：100Sn Gamow-Teller 强度与相空间膨胀证据门边界

依据独立审计程序 `system/scripts/day21_checkpoint011_sn100_gamow_teller_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/sn100-gamow-teller-audit-011.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LB16-D21-1 | Lubos 2016 利用 RIKEN BigRIPS 采集的 2525 个 $^{100}\text{Sn}$ 样本，通过精细量热谱学与 Geant4 响应拟合，测得精确 $Q_{\text{corr}} = 3.74 \pm 0.14\text{ MeV}$ 并揭示多分支退激，导出相空间因子 $f = 619.33$ 与 $B(\text{GT}) = 5.26_{-1.06}^{+0.90}$。推断阶梯审计表明：相空间膨胀因子（$619.33 / 361.07 = 1.715$）精准解释了两实验标称强度比值（$9.1 / 5.26 = 1.730$）的 $99.15\%$；实测 $B(\text{GT}) = 5.26$ 与大空间壳模型（LSSM）及包含两体弱流（2BC）的从头算核力计算高度自洽，确立了双幻核 $^{100}\text{Sn}$ 依然遵循普适的轴矢量淬灭规律（$q^2 \approx 0.56$），终结了无淬灭“超 Gamow-Teller”争议。 | claim-boundary-audit | direct-and-derived | PRL 122, 222502; Ch.4.4.1-4.4.2 pp.77-81; sn100-gamow-teller-audit-011.json | true |

## Day21 Checkpoint084 原件核验：高统计量热拟合、子体分支与相空间膨胀

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LB16-D21-R84-1 | superseded：撤回2525端点谱事件、304.25原件f及q²普适性认证；改用LB16-D21-R99-1至4；旧全文保存在本run superseded-099。 | withdrawn-task-certification | rejected-and-replaced | Ch.4.4.1 pp.77-78; Ch.4.4.2 pp.80-81; Eqs.(4.19)-(4.27) | true |

## Day21 checkpoint099：谱样本、子核成分与LOGFT边界

本次实际读取并视觉核对PDF88/89/91/92（printed77/78/80/81）。只作这些页的定向核验，不声称重读全111页。raw哈希与原frontmatter一致。2016学位论文数值不自动标成2019期刊数值。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LB16-D21-R99-1 | printed77说明3s窗及像素选择下，扣除子核/本底后端点谱剩1070事件；2525识别库存不能称此次端点拟合事件数。24个β+成分属于100In子核到100Cd的衰变，子核份额19.8%；它们不证明母核100Sn有24个GT终态。 | sample-and-component-identity | direct-original | printed77 Fig.4.22 and adjacent text | true |
| LB16-D21-R99-2 | Eq4.19为3.81±.14stat(+.10/−.28sys)MeV；fit-range系统量作者称与统计非独立，随后不另加。96/141keV转换电子平均沉积约63keV，Eq4.20给Qβcorr=3.74±.14MeV；Eq4.21的QEC还需加终态激发能和2me，不能把3.74当总质量QEC。 | fitted-endpoint-and-error-convention | direct-original | printed78 Eq.4.20 | true |
| LB16-D21-R99-3 | Eq4.25为BGT=3811.5/(fT1/2)，作者用NNDC LOGFT与1.17±.10s、3.74±.14MeV得到Eq4.26/27的logft=2.86±.08及BGT=5.26(+.90/−1.06)。由该B/T倒算f≈619.333仅是恒等式；304.25是旧078简化β+算术，不是本文结果。 | extraction-provenance-and-task-boundary | direct-original-and-bounded-calculation | printed80 Eq.4.25 | true |
| LB16-D21-R99-4 | printed81分别列LSSM总强度8.19、QEC窗7.82和首1+态5.7，均是模型数；作者保留与旧实验区间相容及较小重叠。不能以本次单个比值宣布普适q²=.56或终结争议。 | model-comparison-and-interpretation | direct-original | printed81 LSSM comparison | true |

必要伴随观测是母核分支、匹配β+/EC定义、谱形与探测器响应及联合误差。不同实验可独立采集，但共享常数/程序和派生量的统计相关仍须另核。原review/flags保持。
