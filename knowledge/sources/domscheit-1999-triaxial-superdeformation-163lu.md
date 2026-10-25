---
type: source
title: "Triaxial superdeformation in 163Lu"
aliases: [Domscheit 1999 163Lu, triaxial superdeformation in 163Lu]
created: 2026-07-03
updated: 2026-07-03
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Triaxial Superdeformation in 163Lu"
authors: [J. Domscheit, S. Törmänen, B. Aengenvoort, H. Hübel, R. A. Bark, et al.]
journal: Nuclear Physics A
year: 1999
volume: 660
pages: 381-392
doi: 10.1016/S0375-9474(99)00392-9
arxiv:
language: en
canonical_source: doi:10.1016/S0375-9474(99)00392-9
zotero_item_key:
citation_key: domscheit_1999_Triaxialsuperdeformation
zotero_uri:
library_file:
raw_file: "raw/papers/1999_Domscheit et al_Triaxial superdeformation in 163Lu.pdf"
raw_sha256: EDDE41A90870CBA7451DA6D93579017EEB046D060513AA69B24661BA5A72B7C8
nuclei: [163lu]
reactions: [139la-si29-5n-163lu, 139la-si29-4n-164lu]
experiments: [legnaro-euroball-163lu-si29-145mev]
models: [cranked-shell-model]
observables: [moments-of-inertia, transition-quadrupole-moment]
methods: [gamma-gamma-coincidence, dco-ratio]
tags: [non-a130, high-spin, superdeformation, triaxiality, band-mixing, euroball]
---

# Domscheit 等（1999）：`163Lu` 三轴超形变

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

J. Domscheit et al., *Nuclear Physics A* **660**, 381-392 (1999)，DOI `10.1016/S0375-9474(99)00392-9`。题名、作者年份和 DOI 与只读 BibTeX 条目唯一匹配，使用给定 citation key `domscheit_1999_Triaxialsuperdeformation`。

## Scope and Reading Depth

全文精读，并视觉核对 Fig.1 的符合谱、Fig.2 的能级纲图、Tables 1-2 的 γ 跃迁与 DCO、Figs.3-4 的能量和转动惯量、Eqs.1-2 的 SD-ND 两能带混合计算、Figs.5-6 的 UC/PES 计算及 Summary。

本文是 `A=163` 的非 A≈130 原始实验与模型来源。它只作为三轴形变/超形变判据和高自旋集体运动的比较性参照，不构成 A≈130 核区的直接证据。

## Summary

作者用 Euroball 研究 `163Lu` 高自旋态，把已知超形变带 SD1 向高、低自旋延伸并连接到正常形变态，确定其激发能、自旋和宇称；同时发现转动惯量相近的较弱 SD2。SD1 与正常形变带之间的两能带混合分析解释 SD1 的部分带外衰变；这里不是指 SD1 与 SD2 相互混合。UC 势能面计算在大形变处给出 `γ≈+20°` 与 `γ≈-15°` 的三轴极小值；因此本文题名中的“三轴超形变”主要依赖实验带性质与模型势能面的联合解释，而不是对 γ 的直接实验测量。

## Experimental or Theoretical Setup

- 反应：论文统写为 `139La(29Si,xn)`；形成 `168Lu` 复合核后，5n 蒸发道产生 `163Lu`，4n 蒸发道产生 `164Lu`。本文只讨论 `163Lu`，`164Lu` 结果另文发表；
- 阵列：当时的 Euroball 配置为 13 Cluster、25 Clover 和 28 tapered 单元；
- 触发：采集约 `3.8×10^9` 个抑康普顿前 Ge fold≥6 事件；
- 稳定性筛选后保留 25 tapered、75 Cluster elements、96 Clover elements，得到 `2.3×10^9` 个抑康普顿 fold≥3 符合事件；
- 数据产品：门控 `Eγ-Eγ` 矩阵、cube、hypercube 和多种门控谱；以 forward/backward 对 near-90° Clover 构造 DCO 矩阵；
- 理论：Ultimate Cranker（UC）组态分离势能面与各 `(π,α)` 对称群最低组态的激发能计算。

## Terminology: Chinese-English Mapping

为避免中文简称在查询时指向错误对象，本页使用以下固定对应。中文正文首次出现时保留英文或缩写；后续查询可用任一名称。

| 中文术语 | English term / abbreviation | 本文中的具体含义 |
|---|---|---|
| 超形变带 | superdeformed band（SD band） | SD1、SD2 |
| 正常形变带 | normal-deformed band（ND band） | SD1 衰变所连接的低形变带结构 |
| SD-ND 两能带混合计算 | two-band mixing calculation | 混合对象是同为 `21/2+` 的 SD1 与 `[411]1/2+` ND 态，不是 SD1 与 SD2 |
| 连接跃迁 | linking transition | 将 SD 带连接到 ND 结构，或把 SD2 连接到 SD1 的 γ 跃迁 |
| 带内/带外分支 | in-band/out-of-band branch | 分别留在同一带内或离开该带的衰变分支 |
| 运动学/动力学转动惯量 | kinematic/dynamic moment of inertia，`J^(1)`/`J^(2)` | 由带内跃迁能量和转动频率构造的转动响应量 |
| 跃迁四极矩 | transition quadrupole moment，`Q_t` | 由寿命和 E2 集体性提取的形变诊断量 |
| 势能面 | potential-energy surface（PES） | UC 计算给出的 `(ε,γ)` 形变能量地形 |
| 宇称/旋称 | parity/signature，`(π,α)` | UC 中组态的离散对称量子数 |
| 摇摆运动 | wobbling motion | SD2 的一种作者推测；本文未由 linking-transition 多极性确认 |

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DO99-1 | 本实验把 SD1 在高自旋端增加两条跃迁、在带底增加一条跃迁；符合谱还显示一条新 191 keV 跃迁与 174 keV 跃迁并行，使原先被认为是基态的能级改置于 17 keV。 | experimental-fact | direct | pp.383-384, Fig.1(a-c), Fig.2 | false |
| DO99-2 | SD1 通过 426.5、529.4 和 697.1 keV 跃迁连接到正常形变结构；Table 1 给出相对强度、DCO 比和自旋指认，其中 426.5 keV 为 `25/2+→21/2+`，529.4 和 697.1 keV 均为 `21/2+→19/2+`。 | experimental-fact | direct | pp.384-386, Fig.2, Table 1, Sec.3.1 | false |
| DO99-3 | 依据 Table 1 的多极性指认，作者确定 SD1 带头为 `13/2+`；Fig.2 的 SD1 序列延伸到 `77/2+`。 | experimental-fact | direct | p.384 Fig.2; p.386 Sec.3.2 first paragraph | false |
| DO99-4 | 新发现的 SD2 强度约占反应道 2%，在约 `37/2` 附近主要衰变到 SD1，但连接跃迁未能建立；其激发能和最低自旋只能暂定约 4.4 MeV 与 `39/2`，宇称未由实验确定。 | experimental-fact | direct | pp.384-386, Fig.2; Sec.3.2 first paragraph | false |
| DO99-5 | 两条 SD 带的 `J^(1)`、`J^(2)` 很相近，作者据此认为二者可能具有相近形变；SD2 的 `J^(1)` 依赖最低态 `I=39/2` 的暂定假设。 | author-interpretation | direct | pp.386-388, Figs.3-4 | false |
| DO99-6 | SD1 低自旋处 `J^(2)` 的大幅波动被作者解释为 2087 和 2198 keV 两个 `21/2+` 正常/超形变态混合；由 426.5/314.9 keV 分支比的 SD-ND 两能带混合计算（two-band mixing calculation）得到 `α²=0.04(1)`、相互作用能 `22(3) keV`。 | model-result | direct | p.387, Eq.1; Fig.3; Table 1 | false |
| DO99-7 | 用 697.1/263.1 keV 分支作一致性检查得到 `Q_ND/Q_SD=0.48(7)`；作者指出该比值与早先寿命工作给出的 `Q_ND=6.0(5) b`、`Q_SD=10.7(7) b` 相符。后两项绝对四极矩是本文对 Ref.[2] 的转述。 | model-result | indirect | p.388, Eq.2 and paragraph below; Ref.[2] | false |
| DO99-8 | SD-ND 两能带混合导致两个 `21/2+` 能级约 5 keV 排斥；校正后 SD1 的 `J^(1)`、`J^(2)` 随频率更平滑。高自旋 `45/2+` 附近的小畸变与约 4.5 keV 相互作用、`α²=0.009` 及未观察到的 721 keV 分支约 1% 上限相容。 | model-result | direct | pp.388-389, Fig.4 and surrounding text | false |
| DO99-9 | UC/PES 在正常形变处给出 `(ε,γ)=(0.20,0°)` 极小值，在大形变处给出 `(0.41,+20.6°)` 与 `(0.39,-15.0°)` 两个三轴 SD 极小值；作者把 N≈94 的中子能隙作为这些极小值在各 `(π,α)` 对称群出现的模型原因。 | model-result | direct | pp.389-390, Fig.5; Sec.3.2 | false |
| DO99-10 | UC 计算把 SD1 指认为最低的 `(π,α)=(+, +1/2)` 大形变组态，并预期 SD2 为 `(-,1/2)`、在 `I≈20` 时高约 400 keV；作者同时明确指出计算高估了 SD1 相对正常形变带的能量。 | model-result | direct | p.390, Fig.6 and two paragraphs above/below | false |
| DO99-11 | 本文引用的 SD1 平均实验四极矩 `Q=10.7(7) b` 不能区分正、负 γ 组态，因为计算分别给出 9.9 b 与 11.0 b；作者认为需要多条三轴 SD 带的系统四极矩测量才能判别。 | experimental-criterion | indirect | p.390, paragraph above wobbling discussion; Ref.[2] | false |
| DO99-12 | 作者把 wobbling 作为 SD2 的另一种可能解释：相同转动惯量的激发带应通过 M1/E2 跃迁衰变到 yrast SD 带；但 SD1-SD2 连接跃迁及多极性尚未找到，因此本文没有实验识别 wobbling。 | author-interpretation | direct | pp.390-391, final paragraph of Sec.3.2 | false |
| DO99-13 | 对本文证据链的判读是：能级连接、DCO/多极性、自旋宇称、相近转动惯量和大四极矩支持“超形变转动结构”；`γ≈±20°` 与具体 `(π,α)` 指认来自 UC/PES 模型，且四极矩不能区分 γ 符号，故“三轴性”不是单一实验量直接证明。 | synthesis | direct | pp.386-391, Figs.2-6, Eqs.1-2, Summary | false |

## Nuclear Structure Information

### SD1

- 带头：`13/2+`；
- Fig.2 中范围：`13/2+` 至 `77/2+`；
- 新/关键低能 SD 跃迁：196.8、263.1、314.9、386.2 keV；
- 到正常形变结构的连接：426.5、529.4、697.1 keV；
- 反应道强度约 10%；
- 低自旋 `21/2+` 态存在显著 SD-ND 混合。

### SD2

- 反应道强度约 2%；
- `J^(1)`、`J^(2)` 与 SD1 相近；
- 约在 `37/2` 附近衰变到 SD1，但连接跃迁未建立；
- 激发能约 4.4 MeV、最低自旋约 `39/2` 均为暂定；实验宇称未知。

### Normal-deformed structures

作者依据邻核系统学将基带指认为质子 `[411]1/2+`，并讨论 `[404]7/2+`、`[523]7/2-` 结构。该组态赋值属于作者解释，不是由单一 γ 跃迁直接测得。

## Authors' Interpretation

- SD1 的低自旋带外衰变主要由同自旋宇称 SD/ND 态混合解释；
- 低自旋较强混合对应 SD 与 ND 极小值间小或消失的势垒，高自旋较弱混合对应模型中的较高势垒；
- SD1 是 `(+, +1/2)` 三轴 SD 最低组态；
- SD2 可能是 `(-,1/2)` 组态，也可能与 wobbling 有关；作者明确保留后一解释为推测。

## Model Results

- SD1 与 `[411]1/2+` 正常形变带的 SD-ND 两能带混合计算（two-band mixing calculation）：`α²=0.04(1)`、`V=22(3) keV`，以及 `Q_ND/Q_SD=0.48(7)`；
- UC/PES：正常形变与两组三轴 SD 极小值，并给出随自旋变化的势垒；
- 计算四极矩：正 γ 组态 9.9 b，负 γ 组态 11.0 b；
- 计算与实验的关键偏差：SD1 相对 ND 带的理论激发能过高。

## Competing Interpretations and Limitations

- SD2 未连接到已知能级，能量、自旋和宇称均不完备；其组态和 wobbling 解释都不能视为已证实；
- 本文没有报告 SD1-SD2 linking transition 的能量、多极性或强度；
- 本实验没有报告偏振、ADO、寿命、绝对 B(M1)、B(E2) 或 B(M1)/B(E2)；绝对四极矩来自 Ref.[2] 的早先寿命测量；
- Table 1 报告 DCO，但没有为每条跃迁单列明确多极性栏；不得仅凭接近 1 的比值跨装置泛化；
- 四极矩和相近转动惯量约束大形变，但不能单独确定 γ 的符号或证明静态三轴刚性；
- `163Lu` 不属于 A≈130；与 A≈130 的联系仅是判据和方法的比较性背景。

## Extracted Pages

- Nucleus: [[163lu]]
- Bands: [[163lu-sd1]], [[163lu-sd2]]
- Experiment: [[legnaro-euroball-163lu-si29-145mev]]
- Concepts: [[superdeformation]], [[triaxial-deformation]], [[rotational-bands]], [[wobbling-motion]]
- Observables: [[moments-of-inertia]], [[transition-quadrupole-moment]]
- Methods: [[gamma-gamma-coincidence]], [[dco-ratio]]
- Project: [[a130-high-spin-collective-modes-evidence-map]]（仅比较性背景）

## Personal Notes

对后续研究最可复用的不是把 `Q≈10.7 b` 或 `J^(2)` 直接等同于三轴性，而是分层使用证据：谱学连接与多极性建立带结构；寿命/四极矩约束形变尺度；转动惯量检验共同转动响应；γ 的大小、符号和组态仍依赖模型，并应由连接跃迁、电磁强度和更多独立测量检验。

用户已完成人工页面级审阅，确认 citation key、主要表述和科学内容无明显问题，并补充确认 `139La(29Si,5n)163Lu` 与 `139La(29Si,4n)164Lu` 道关系；DO99-1 至 DO99-13 据此完成 claim-level 复核。`164Lu` 结果不属于本文正文讨论范围。
## Day21周考推断阶梯审计：超形变与三轴性（TSD）证据门边界

依据独立审计程序 `system/scripts/day21_checkpoint010_superdeformation_tsd_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/superdeformation-tsd-audit-010.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| DO99-D21-1 | **superseded at checkpoint099**：本篇未新测Qt，10.7(.7)b引自Schmitz1993；未证实通用Qt几何式或10W.u.摇摆必要门。见DO99-D22-R099-1/2。 | task-correction | rejected-and-replaced | printed388Eq2;390quadrupole paragraph;391Ref2 | true |

## Day22 checkpoint099：SD1寿命谱系与SD–ND混合对象

本轮实际定向读printed381–382、387–391，视觉核387 Eq1、388 Eq2；Table1四条分支从385逐项核对。不是重称全部12页新读或原Schmitz1993全文已取得；原DO99-1–13人审范围保持，新条目为Codex self-audit。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DO99-D22-R099-1 | quoted Q_ND=6.0(.5)b、Q_SD=10.7(.7)b明确来自Ref2 SchmitzPLB303(1993)230，本文没有新寿命采集。引用对象为ND和原SD1，不是新SD2；p390说明单Q不足区分正/负γ计算（9.9/11.0b）。SD2连接尚未找到，wobbling仅替代猜测；不能将本篇/OD01的相同Q数当独立寿命重复测量或TSD2绝对强度。 | lifetime-lineage-and-object-identity | direct-original-with-secondary-number | printed388belowEq2;390Q/SD2discussion;391Ref2 | true |
| DO99-D22-R099-2 | Eq1/2混合的是2087和2198keV两个21/2+ ND/SD1态，不是SD1/SD2两超形变带。用Table1的I426/I315=12.5/68.1及I697/I263=23.3/18.7与E^5修正，任务中心重建p=.0387153、QND/QSD=.486750；假设实对称两态H后由111keV观测间隙给V=21.4136keV、每态排斥4.2974keV，近作者.04(.01)、22(3)keV与约5keV。这是已采用混合/算符模型的条件重建，不是新τ、绝对E2或唯一机制证明。 | branch-model-and-central-reconstruction | direct-original-and-task-arithmetic | printed385Table1;387Eq1;388Eq2andtext | true |

| DO99-D22-R099-3 | Table1的697.1keV行带footnote3：与相近能量SD线未分辨；因此Eq2用的23.3(4.7)强度不能擅称独立干净门谱量，具体分离/误差需原输入核。后续OD01明确把本篇SD2识别为其TSD2的先前候选并在另一次152MeV EuroballIV采集中建九条links，不能将1999没有连接线的状态误归为2001也没连接。两篇新增采集与重复采用同一Schmitz1993Qt应分别计谱系。 | contamination-and-campaign-lineage | direct-original-and-cross-source | printed385Table1footnote3; OD01 printed5867setup andRef12 | true |
