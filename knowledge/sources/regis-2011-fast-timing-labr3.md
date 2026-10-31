---
type: source
title: "Régis 2011 博士论文：LaBr3(Ce) 快速定时与 MSCD 方法"
aliases: [Régis 2011 fast timing thesis, LaBr3 fast timing dissertation]
created: 2026-09-05
updated: 2026-09-05
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-method-and-experiment
reading_depth: deep-read
title_original: "Fast Timing with LaBr3(Ce) Scintillators and the Mirror Symmetric Centroid Difference Method"
authors: [Jean-Marc Régis]
advisor: [Jan Jolie, Alfred Dewald, Patrick H. Regan]
journal: "University of Cologne doctoral dissertation"
year: 2011
volume:
pages: 111
doi:
arxiv:
language: en
canonical_source: "Régis, Jean-Marc. Fast Timing with LaBr3(Ce) Scintillators and the Mirror Symmetric Centroid Difference Method[D]. University of Cologne, 2011."
zotero_item_key:
citation_key: ""
zotero_uri:
library_file: "raw/theses/degree-dissertation/LaBr3时间.pdf"
raw_file: "raw/theses/degree-dissertation/LaBr3时间.pdf"
raw_sha256: "54EF3C5B70D7EF4ED694AD9089FA40533D39E2BB060228EB3D1A304B03555F52"
nuclei: [176w, 172hf, 214bi, 214po, 133cs]
reactions: ["in-beam gamma-ray fast-timing measurements", "beta-gamma delayed-coincidence calibration sources"]
experiments: []
models: [interacting-boson-model, shell-model]
observables: [lifetime, time-walk, centroid-shift, prompt-response-difference]
methods: [fast-timing, time-differential-perturbed-angular-distribution, gamma-gamma-coincidence]
tags: [fast-timing, labr3, lifetime, ms-cd, detector-method, phd-thesis]
---

# Régis 2011：LaBr₃(Ce) 快速定时与 MSCD 方法

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

Jean-Marc Régis，*Fast Timing with LaBr3(Ce) Scintillators and the Mirror Symmetric Centroid Difference Method*，University of Cologne，博士学位论文，2011，111 页。原始 PDF SHA-256 为 `54EF3C5B70D7EF4ED694AD9089FA40533D39E2BB060228EB3D1A304B03555F52`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: Abstract、Chapters 2–6；核对 LaBr₃(Ce) detector、PMT/CFD time walk、centroid shift、MSCD、PRD calibration、`214Bi/214Po/133Cs` benchmark lifetimes、`176W` in-beam fast timing 和 IBA/shape-transition discussion。
- Not covered: 所有引用来源和探测器硬件的逐元件复现。
- Coverage caveats: 具体 lifetime 数值依赖 prompt curve、CFD setting、background correction 和 detector response；方法结论不能无条件转移到其它阵列。

## Paper Question and Scientific Motivation

论文旨在改进皮秒级核态寿命测量，系统研究 LaBr₃(Ce) 快速闪烁体和电子学 timing response，并提出对 centroid-shift 更敏感的 mirror symmetric centroid difference（MSCD）方法（Abstract；Chapters 1–4）。

## Method and Design Logic

作者从 scintillator/PMT/CFD 的时间响应出发，建立 energy-dependent CFD time marker 和 prompt-response calibration；随后用 delayed γγ coincidence、标准源和 in-beam `176W` 数据验证 MSCD，并通过 PRD、background correction 和多种 PMT/CFD 设置估计系统误差（Chapters 2–5）。

## Key Evidence and Reasoning Chain

1. LaBr₃(Ce) 以高时间分辨率和可用能量分辨率支撑皮秒 timing。
2. CFD time walk 与能量、PMT 工作电压和 shaping delay 相关，prompt curve 需实测校准。
3. MSCD 利用镜像对称的组合时间分布减少单探测器响应偏差，并用 PRD 校准整套响应。
4. 标准源与 `214Bi/214Po/133Cs` 结果检查方法的灵敏度和上限；`176W` 给出 in-beam 应用。

## Summary

论文建立了 LaBr₃(Ce) 快速定时的实验/电子学知识链，推导能量依赖的 CFD 时间标记，系统比较 centroid shift 与 MSCD，并提出 PRD 校准和背景修正。作者报告 `133Cs` 161 keV 态的加权寿命约 `235(10) ps`、`214Po` 609 keV 态 `τ≤6 ps`、`214Bi` 53 keV 态保守上限 `τ≤15 ps`；这些 benchmark 依赖具体设备与拟合条件。第 5 章将 MSCD 用于 `176W` 基态带四个低激发态，并与 IBA 和 Hf/Os N=104 系统学比较。

## Experimental or Theoretical Setup

- LaBr₃(Ce)+PMT+CFD fast-timing setup；比较 anode/dynode、PMT voltage 和 CFD delay。
- 标准 γ 源、delayed γγ coincidence、`214Bi/214Po/133Cs` 和 in-beam `176W`。
- centroid shift、MSCD、PRD、prompt curve、background correction；IBA 用于 `176W`/邻近偶偶核结构解释。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| RG11-1 | LaBr₃(Ce) 闪烁体在 `Eγ>300 keV` 时具有约 2–4% 能量分辨率，同时提供远高于 HPGe 的时间响应，适合皮秒级寿命测量。 | experimental-fact | direct | single | Abstract；Ch.2 | true |
| RG11-2 | 论文首次推导/使用能量依赖的 CFD time marker，并显示 time walk 随能量、PMT 电压和 shaping delay 改变。 | method-formalism + experimental-criterion | direct | single | Ch.2.3；Ch.4.2–4.5 | true |
| RG11-3 | MSCD 利用组合时间分布的镜像对称性，相比单 detector centroid shift 对时间响应不对称更敏感；PRD 校准整套线性组合 response。 | method-formalism | direct | single | Ch.3.2–3.3；Ch.4.3 | true |
| RG11-4 | 在具体设置下，`133Cs` 161 keV 态得到 `τ≈235(10) ps`，`214Po` 609 keV 态 `τ≤6 ps`，`214Bi` 53 keV 态保守给出 `τ≤15 ps`。 | experimental-fact | direct | single | Ch.4.6；Table 4.1 | true |
| RG11-5 | `176W` in-beam MSCD 测量得到基态带最低四个激发态的寿命，并用 IBA 及邻近 W/Hf/Os 系统学讨论集体性和 N=104 形状相变。 | experimental-fact + author-interpretation | indirect | single | Ch.5；Ch.6 | true |
| RG11-6 | lifetime 结果受 prompt curve、CFD setting、PMT response、background 和 PRD 系统误差控制；不能把单一装置的 timing performance 当作普适常数。 | analytical-boundary | inferred | single | Ch.3–4；Table 4.1 | true |

## Nuclear Structure Information

- `214Bi/214Po/133Cs`：fast-timing benchmark 与核结构解释。
- `176W`：in-beam `γγ` fast timing、基态带 lifetimes、IBA/邻核比较。
- `172Hf` 与 W/Hf/Os N=104 链：寿命与集体性/形状相变背景。

## Authors' Interpretation

作者把 MSCD 视为 centroid-shift 的更敏感扩展，并认为 `176W` 结果显示转子样集体性；具体 IBA 参数和 N=104 形状转变属于模型/系统学解释。

## Model Results

- IBA/CQF Hamiltonian 描述 `214Po` 振动态和 `176W`/Hf/Os 集体性。
- CFD/prompt-response 模型描述 detector timing response 和 time walk。

## Competing Interpretations and Limitations

- `214Bi/214Po` 的 lifetime 上限和 B(M1)/B(E2) 解释依赖转换系数、分支比和核模型。
- MSCD 灵敏度优势是对具体 response symmetry 的方法学结论，不能替代每次实验的 prompt calibration。
- `176W` 的 rotor/IBA 解释不等于直接 γ 形变测量。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-RG11-1 | Core reconstruction | 该论文最可复用的贡献是从 CFD time walk 到 MSCD/PRD 的完整 fast-timing 误差链。 | Chapters 2–4 | unreviewed |
| AR-RG11-2 | Assumptions and dependencies | MSCD 依赖镜像响应、prompt calibration、energy walk model 和 background treatment。 | RG11-2–6 | unreviewed |
| AR-RG11-3 | Transfer conditions | 可作为未来 lifetime/fast-timing 实验的 methodological bridge；需按 detector/CFD 条件重新校准。 | Ch.3–5 | unreviewed |
| AR-RG11-4 | Failure conditions | 未校正 time walk、prompt asymmetry 或 background 会把 ps 级 lifetime 偏差误写成核结构差异。 | Ch.3–4 | unreviewed |
| AR-RG11-5 | Reverse/falsification test | 用标准源、不同 PMT voltage/delay、mirror-side consistency 和 independent lifetime compare 检查方法稳定性。 | Ch.4；Table 4.1 | unreviewed |
| AR-RG11-6 | Research-question decision | 为 Wiki 的 lifetime、fast-timing 和 B(E2) evidence chain 提供方法学桥接。 | RG11-3–6 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 RDDS/DSAM/lifetime 来源，但缺少 LaBr₃(Ce) fast timing、MSCD 和 PRD 的系统方法来源。
- Effect of this source: supports and extends 方法层；limits 不同设备间的直接数值迁移。
- Reason: 补充 ps 级寿命、prompt calibration 和系统误差边界。
- Persistence decision: 新建 source；按需更新 `lifetime`、`recoil-distance-doppler-shift` 和 timing method 入口。
- Review state: 页面 `unreviewed`；RG11-2–6 保留 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[lifetime]] | 提供 LaBr₃(Ce)/MSCD 的 ps 级寿命测量链。 |
| methodological-bridge | [[gamma-gamma-coincidence]] | delayed γγ coincidence 与 prompt-response calibration。 |
| limits | [[gamma-soft-vs-gamma-rigid-diagnostics]] | `176W` IBA/系统学解释不是直接形变测量。 |

## Human Review Triage

### P0

- RG11-3/RG11-4：核对 MSCD/PRD 定义、Table 4.1 lifetime 数值、上限和系统误差；风险是把 benchmark 数值脱离实验设置引用。

### P1

- RG11-2：核对 CFD time-walk 公式、energy range 和 shaping-delay 条件。
- RG11-5/RG11-6：核对 `176W` IBA/形状相变解释及方法迁移边界。

### P2/P3

- 可在后续方法综合中补充实际 fast-timing setup 与 calibration checklist。

## Extracted Pages

- Nuclei: `176W`、`214Bi`、`214Po`、`133Cs` 暂不机械新建。
- Methods: [[lifetime]]、[[gamma-gamma-coincidence]]。
- Concepts: [[gamma-soft-deformation]]、[[rotational-bands]]。

## Non-source Notes and Follow-up

该来源以方法为主；核结构 benchmark 结果保留在 source 内，不把 LaBr₃ 的装置性能与其它 detector array 直接合并。


## Day19原件核验：MSCD定义、门角色、背景与误差

2026-10-21同Day19 session checkpoint009。保留原RG11-1–6及旧审核状态。本次实际读取PDF3–5摘要、PDF7–8目录/引言、PDF21–30 Ch3全段、PDF42–53 Sec4.3（含4.2结尾）、PDF96–98 AppendixA；图/式视觉范围另记scope。不是111页新全文阅读，也不是重做原实验。

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
| --- | --- | --- | --- | --- | --- | --- |
| RG11-D19-1 | Eq3.8/3.9对decay参考定义signed ΔC=C(D)stop−C(D)start=PRD+2τ；feeder参考按Eq3.10另反转支路顺序，仍为PRD+2τ。须保Ef−Ed符号和参考门角色，不把绝对质心差统一套成有符号式。 | method-definition | direct-original | single-source-method | PDF27–29 Eqs3.8–3.13 | true |
| RG11-D19-2 | Eq3.13给ΔE=0时PRD=0、ΔC=2τ；PDF28/30提出在已分辨级联数据上向零点插/外推。若实际同能量门使feeder与decay角色不可分，不能把同一time spectrum复制为两种已标记因果分布；该测量可识别性边界由新对称混合设计说明，不是作者测得的失败案例。 | zero-point-and-role-contract | direct-original-and-task-inference | same-method-not-new-experiment | PDF28 Fig3.7；PDF29 Eq3.13；PDF30 item7 | true |
| RG11-D19-3 | 同一能量沉积的Compton与full-energy响应可不同：Fig4.12有明显曲线差异，作者据此用full-energy事件校准。其两LaBr3+XP20D0、约−850V/20ns设置下，240–1300keV的PRD residual误差8ps被称2σ、对应寿命约4ps量级；这是本设置/误差约定，不是任意探测器普适下限或原jointCov。 | calibration-domain | direct-original | one-setup | PDF42 Fig4.12；PDF43 setup；PDF44–45 Eq4.13/Fig4.16 | true |
| RG11-D19-4 | 444−244keV的同一PRD被在两参考能量处以相反符号重用。镜像点可帮助校准曲线连接，但不是第二份独立计数；须保共享事件/校准协方差，不能凭画成两点宣称sqrt2统计增益。 | same-datum-reuse | direct-original-and-task-inference | dependent-mirror-reuse | PDF43 final paragraph | true |
| RG11-D19-5 | AppendixA写ΔCT=(ΔCD+αΔCC)/(1+α)，α为background-to-peak；PDF98明确此差值公式仅在两timing支路相同peak-to-background比时成立，本实验约满足并用均值加10%系统。768keV例α=.3、ts=−39(8)ps给ΔC修正−11.7(2.6)ps；不把此修正另算新寿命测量。 | background-mixture-contract | direct-original | same-experiment | PDF97–98 EqsA.1–A.2 | true |
| RG11-D19-6 | PDF22 Eq3.3字面dC=sqrt(<t²>−<t>²)给的是分布宽度形式；独立N事件样本均值SE另有1/sqrtN。PDF30 Eq3.16若被读成同一非零τ的完整delayed曲线反对称，与Eq3.13零点会留下4τ残差。保字面定义边界，需区分prompt曲线、参考族和τ符号；不擅改raw或宣告erratum。 | literal-moment-and-mirror-boundary | direct-original-and-conditional-algebra | no-new-experiment | PDF22 Eq3.3；PDF29 Eq3.13；PDF30 Eq3.16 | true |
| RG11-D19-7 | 新设计取τ20ps/PRFσ80ps，完整标记的±指数卷积质心为±20ps；无角色标记的等权混合质心0但方差σ²+2τ²。仅取±80ps窗再直接MSCD得5.314ps；背景比.3/.1若强用平均α会得24.895ps，逐支路校正才返20ps。均为自设反例，不是LaBr3实测性能、fit或CI。 | conditional-gate-response-design | task-derived | synthetic-not-independent-data | PDF22 Eq3.4；PDF97–98 EqsA.1–A.2；timing-gate-response-result-009.json | true |

## Day19校准图与实验伴随量；Day20符号边界

checkpoint010在继续实际读取Ch2、Ch4其余方法/测试、Ch5实验与结构讨论及Ch6后追加。仅关键图表视觉已核范围可以认证，不把文本抽取算逐图验证。未阅读的引用primary不作独立新证据；review状态不变。

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
| --- | --- | --- | --- | --- | --- | --- |
| RG11-D19-8 | CFD的TCF/ARC条件、PMT voltage/shape与动态range须匹配：20ns并非所有PMT的最优设定，本文XP20D0和XP2020给不同timewalk随delay趋势。相同核态在不同PRD曲线校准后相合支持装置控制，但共享reference lifetimes/calibration来源不等全独立实验。 | operating-domain-and-companion | direct-original-and-boundary | multi-setting-shared-references | PDF17–20 Eqs2.5–2.15；PDF59–61 Fig4.40/Table4.1 | true |
| RG11-D19-9 | Eq4.13 fit1中央参数a=−826391 ps√keV、b=3316.85keV、c=−1.28444ps/keV、d=14104.7ps。以g(Ef)−g(Ed)算1120/609约126.390ps、344/609约−128.651ps，与文中126(8)/−129(8)中央舍入相容；不复现fitCov/CI。相同ΔE400keV的800/400与1000/600分别约161.558和112.851ps，PRD不是只由ΔE数值决定的通用函数。 | central-curve-reconstruction | direct-original-and-derived | same-calibration-not-new-measurement | PDF44 Eq4.13 fit1；PDF48 Eqs4.15/4.18 | true |
| RG11-D19-10 | 在separable且稳定响应的设计模型中，PRD可表示节点势差g(Ef)−g(Ed)：5能量节点连通校准图rank4，镜像再画不加rank；cycleclosure可检出非gradient污染，却看不见任意h(Ef)−h(Ed)型共同误校。新h=.02E与τ20ps控制能使cycle全过而1120/609目标τ偏成14.89ps。这不是对原实验有该误差的判断。 | calibration-identifiability-design | task-derived | synthetic-not-new-data | PDF43–45 reference shifting；prd-calibration-graph-result-010.json | true |
| RG11-D19-11 | 176W实验用BGO主动抑制、HPGe符合监视未分辨污染；509keV线受511keV影响。原unshielded低能108keV谱含delayed background，作者称不能可靠插值扣除；shielded的2+寿命1.44(4)ns，后续e−γ为1.43(2)ns转引Ref19。不能只用相同count或相同能量门假定背景响应相同。 | inbeam-background-companion | direct-original | present-data-and-dependent-quoted-comparator | PDF73–80 Figs5.3–5.13 | true |
| RG11-D19-12 | Table5.1的2+→0+采用1430(20)ps而非本节shielded1440(40)ps；IBA及各极限的effective charge均归一到同一B(E2;2→0)输入，故该行全为Q=7.03不是各模型独立验证。4+/6+寿命与8+上限角色分开，模型shape解释归作者。 | input-lineage-and-model-normalization | direct-original-and-boundary | shared-normalization | PDF79/81–83 Table5.1 and preceding text | true |
| RG11-D20-1 | 本文Eq5.10将实验室系spectroscopic矩写作Qt，与本Wiki常称transition moment的Qt对象不同；本任务用Qs^(RG)标该静态矩，不能按字母混并。Eq5.9由B连接intrinsic Q0，Table5.1正的Q(Ji)另是由这些B转换出的量，不冒静态Qs直接实测。 | symbol-and-observable-disambiguation | direct-original-and-boundary | same-source | PDF67 Eqs5.9–5.11；PDF81–83 Table5.1 | true |
| RG11-D20-2 | PDF66 Eq5.1后字面印R0=1.2 A^(4/3)，Eq5.2印α±2=βsinγ；保字面且不自动用于standard radius/归一的代码。缺实际shape producer，不擅改raw或宣告作者分析按这些字面执行。旧β=.4195不是从本源或Petrache实际producer复现。 | literal-radius-and-convention-boundary | direct-visual-and-boundary | source-text-not-code-execution | PDF66 Eqs5.1–5.2；PDF67 Eq5.11 | true |

## Day19量化审计：MSCD走时曲线PRD微积分敏感性、能量门偏置与三元闭环定理

**checkpoint088来源/代码纠正，原标题只保历史anchor。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RG11-D19-13 | Eq4.13中央曲线可重算PRD，g(E)差的cycleclosure只是可分离模型恒等式，不能认证所有串扰/漂移无误。100keV处斜率算术是在本次240–1300keV限制范围外，不认实测能力。旧本底练习只算单branch标量，未复现真实双支路混合；“4ps普适极限”及硬填passed=True认证撤回。能量门漂移的偏差符号须先定义实际PRD减采用PRD的差，不将自设符号直接当原实验方向。原fit Cov缺失仍保留。 | calibration-and-inference-boundary | direct-original-and-task-analysis | PDF27–29 Eqs3.9–3.13; PDF44–45 Eq4.13/Fig4.16 | true |

## Day19量化审计：176W基态带MSCD寿命重构、B4/2 Alaga vs X(5)检验与Hf-W历史寿命修正

**checkpoint088：撤回旧科学认证；原标题保留为历史anchor。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RG11-D19-14 | checkpoint082修订：Table5.1的2+行采用1430(20)ps的e−gamma参考，而本节shielded gamma-gamma为1440(40)ps，不能把四行全部称本次MSCD独立测量。表列B(E2)比1.312/.983=1.33469；若额外假定两误差独立Gaussian则sigma=.08527，实际Cov未给。X(5)排除是作者结合模型比较的解释，不能由该一比值及任意sigma阈值当无条件裁决。8+的≤4ps是此设置的报告上限，不是电子学普遍物理极限；NB=14及1.407的先前推式未经原方程验证，撤回。 | source-and-analysis-correction | direct-where-reread-otherwise-withdrawn | checkpoint088 source scope and rejection registry | true |

## checkpoint088：采用值、模型归一与装置上限

本轮定向读PDF81–83，视觉核PDF83 Table5.1/Fig5.15；原科学全文scope不据此扩大。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RG11-D19-15 | Table5.1逐行tau为1430(20)/67(4)/12(4)/≤4ps，B为.983(21)/1.312(79)/1.216(406)/≥1.207(eb)²；第一行采用e−gamma参考，模型有效电荷归一到同B2。作者PDF82排除X(5)并tentatively置O(6)–SU(3)区域；这是带模型和输入依赖的解释。8+上限及PRD误差是该设置条件，不能变成所有Fast Timing的硬分辨极限或三种方法通用交叉窗口。 | source-input-and-model-attribution | direct-original-and-boundary | PDF81–83 Table5.1 and Fig5.15; PDF82 interpretation paragraphs | true |

## checkpoint088：PRD参数误差与完整协方差

本轮另读PDF27–29与44–45文本，视觉核PDF44 Eq4.13参数/Fig4.15。原Fit1四边际误差为111713ps sqrt(keV)、357.39keV、.00944ps/keV、1194.7ps。没有恢复actual fit covariance，不用原“全绿”补齐。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RG11-D19-16 | 对1120/609keV的r=g(Ef)−g(Ed)，offset d严格抵消。以原中央参数求Jacobian，额外独立参数假设给sigma_r=146.12785ps；两个同边际误差的PSD rank-one协方差例分别给201.65543ps/.32098ps。二例是本任务合法反例，不是作者fit Cov或实际误差。PDF45的8ps为该fit残差2sigma、4ps为此实验240<Egamma<1300keV的限制；残差与参数预测误差是不同统计对象，不能互换。原参考寿命/parallel-shift及背景依赖仍需对应实际job。 | actual-marginals-and-covariance-counterexample | direct-original-and-task-derived | PDF44 Eq4.13 Fit1; PDF45 Fig4.16 and following paragraph | true |


## checkpoint094：现代timing方法主线与分设置校准

本轮实际文字读PDF1–64、72–83、93–105，共89页；视觉核30页，source-reading-scope-094.json逐项保存。正文印刷页与PDF页此处一致。覆盖Ch2电子学、Ch3分析/MSCD、Ch4完整detector/calibration、176W目标段、结论和AppendixA；未以此声称全部105科学页或111页学位全文。旧source/review/needs_review保留。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RG11-D19-17 | 理想CFD线性rise/amplitudeindependent前提下TCF/ARC零交叉可不随amplitude，但实际charge-sensitive comparator的斜率、rise形、threshold和PMT非线性仍引timewalk。XP20D0较长delay与XP2020较短delay各有适用设置，不能把20ns/同硬件名当通用最优或免校准。 | electronics-domain | direct-original | PDF11–20 Ch2 Eqs2.5–2.15; PDF54–61 Sec4.4–4.5 | true |
| RG11-D19-18 | Fit1的8ps(2sigma)残差绑定240–1300keV与该-850V/20ns设置；Fit3用133Cs的53→303级联及已知30(5)ps补低能点，连同214Po高能数据扩到50–1510keV，仍报告8ps(2sigma)。Fit3不是把Fit1函数无输入外推到53keV，采用参考及其共享依赖须保留。 | calibration-family-and-range | direct-original | PDF42–51 Sec4.3 Eqs4.13–4.20 Figs4.16/4.26 | true |
| RG11-D19-19 | 176W inbeam另用-1200V/8ns、beamspot处152Eu源36h校PRD，7ps为3sigma残差，与Ch4的8ps/2sigma不是同一误差对象。原2+~1.44ns由slope读，不能凭该calibration就认证108keV任意20ps目标的MSCD输入充分。 | setup-specific-calibration | direct-original-and-transfer-boundary | PDF75–80 Figs5.6/5.12–5.13 | true |
| RG11-D19-20 | 176W对6+ tau12(4)ps仅取直接440keV feeder；4+直接351keV feeder给2tau=134(8)ps，更高feeding门另移21(8)ps归为中间6+延迟。远端feeder门的centroid对应所跨级联的累计等待时间，不能只归目标tau。 | feeding-path-and-centroid | direct-original | PDF75–78 Figs5.7–5.9 | true |
| RG11-D19-21 | Table4.1的214Bi单设置上限≤2/3/8/7ps，不是最终最保守源结果；作者考虑133Cs53keV校准背景10ps系统后，讨论用214Bi≤15ps、214Po≤6ps，133Cs235(10)ps含5psbackground系统。不能挑最小上限或把这些上限改成未报告95%CI。133Cs参考在Fig4.22为248(6)ps，正文245(6)ps，两literal均保。 | uncertainty-and-adopted-result | direct-original | PDF49 Fig4.22; PDF52/57; PDF61 Table4.1 and preceding paragraphs; PDF63 | true |
| RG11-D19-22 | 176W未shield谱Fig5.12的slope为1.52(7)ns、chi²1.22，但作者明说低能background延迟不能可靠插值，可能高估寿命；shielded单谱Fig5.13为1.45(4)ns、chi²1.04，两detector合1.44(4)ns。只作源的可靠性countercase，不由这些相近中心值宣布已证明具体bias或新的显著性。 | fit-quality-versus-response | direct-original | PDF78–80 Figs5.11–5.13 and discussion | true |
| RG11-D19-23 | Eq3.3字面是分布width而非带N的samplemeanSE；Eq3.16若同时把两完整delayed曲线读成同非零tau反对称，则零点2tau与−2tau不相容。保参考族/role/符号的解释边界，不凭source摘要“只剩background”删除时间漂移、几何与门稳定前提；AppendixA单alpha公式仍须两branch比例匹配。 | literal-and-assumption-boundary | direct-original-and-task-consistency | PDF22 Eq3.3; PDF27–30 Eqs3.8–3.16; PDF94; PDF97–98 EqA.1–A.2 | true |

## checkpoint109：未知prompt尾部下的完整谱可识别性设计

本轮没有新增原PDF页阅读；引用本session scope094实际核过的PDF12 Eq2.1、PDF24同能量role歧义和PDF27–30 signed/reference定义。下面全为本任务明示模型，不是Régis实测失败案例，source/review状态不变。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RG11-D19-24 | 无background/drift且feeder/decay角色丢失，假设等权正负指数等待时间，则观察核为对称Laplace L_tau=exp(−abs(t)/tau)/(2tau)。允许未知prompt族时，对任意0<tau2<tau1，a=tau2²/tau1²，正归一prompt P1=G_sigma*(a delta+(1−a)L_tau1)满足P1*L_tau2=G_sigma*L_tau1。故该允许族里完整谱也不识别tau；不是所有fasttiming不识别，也不证明真实PRF如此。 | conditional-full-spectrum-alias | task-derived-from-declared-convolution | PDF12 Eq2.1; PDF24 final paragraph; PDF27–30; prompt-tail-identifiability-result-109.json | true |
| RG11-D19-25 | 合成sigma80ps、tau1=20ps/tau2=10ps给a=.25，两个prompt方差6400/7000ps²而完整观测均7200ps²。七个t的独立time-convolution积分（1600/3200格）与解析原谱相对最大差2.75e−9以内；特征函数恒等式及归一另核。±80ps窗共同接受.65564147，任意相同确定性ROI也不能破该精确alias。需要matchedprompt尾部或独立role约束排除alternateprompt；不报实际fitCI。 | numerical-identity-and-readiness | task-derived | RG11-D19-24; prompt-tail-identifiability-result-109.json | true |

## checkpoint111：matchedprompt的方差差校准设计

本节不新增PDF阅读，不声称作者使用此方差估计器。基于本session scope094实际核过的卷积/centroid和role定义，另做稳定、无背景/feeding/drift、完整时间支持且已知zero mean的设计。不是原实验统计/CI，也不构成通用Fast Timing门槛。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RG11-D19-26 | 对Gaussianprompt方差sigma²与等权正负指数tau，Qhat=(M2signal−M2prompt)/2估tau²。Var(t_signal²)=A=2sigma⁴+8sigma²tau²+20tau⁴，Var(t_prompt²)=B=2sigma⁴。独立N/N0样本下Var(Qhat)=(A/N+B/N0)/4，局部Var(tauhat)=Var(Qhat)/(4tau²)仅离零边界适用；若共享事件/reference需−2Cov项。已知prompt方差可破109构造，但FWHM、截断窗口矩和完整二阶矩不能自动等同。 | moment-calibration-design | task-derived | PDF12 Eq2.1; PDF22 Eqs3.2–3.4; RG11-D19-24; prompt-calibration-design-result-111.json | true |
| RG11-D19-27 | 合成sigma80ps、目标局部sigma_tau=.5ps且N=N0，tau20ps的规划各117200counts，tau5ps各1651325；仅该估计器/假设，非beamtime或MSCD能力排名。每谱1000count、2000次独立MC中tau20/5的Q<0比例.033/.4625，empirical/analytic Var(Q)约.9688/.9756，保负Q不clip或报Gaussian tauCI。tau20而采用prompt sigma78/82ps给表观tau23.622/15.427ps；tau5且误用82ps给Q−137ps²。都是声明mismatch控制，不是实际source偏差。 | finite-calibrator-and-boundary-design | task-derived | RG11-D19-26; prompt-calibration-design-result-111.json | true |

## checkpoint112：2010原稿身份与2015公开GCD companion

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RG11-D19-28 | Ref18原文写NIMA622,81(2010)；Crossref/OpenAlex核精确方法题名对应DOI10.1016/j.nima.2010.07.047、83–92页，2015GCD稿Ref3也写83。2010原body未得，不按元数据标已读；2015公开稿的阵列/pair/PRD/Compton定义另读，依赖性单列，不作为2011同data独立复测。 | bibliographic-and-companion-boundary | metadata-and-direct-companion | PDF100 Ref18; 2015 PDF5 Ref3; focused-metadata112 | true |

## checkpoint026：快速定时质心差法推断阶梯边界审计

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| REG11-D21-1 | 快速定时镜像对称质心差（MSCD/GCD）方法将能级寿命提取转化为时间谱一阶矩位移 Delta C(E_feeder, E_decay) = PRD(E_feeder, E_decay) + 2*tau。当目标能级寿命进入皮秒区（tau < 20 ps）时，该方法对探测器瞬发响应差（PRD）校准曲线的能量依赖性与前序喂居延迟（feeding delay）极度敏感；未校准的 PMT 时间游走或几步中间能级级联延迟会直接淹没内禀微观跃迁寿命，严禁将未经实验 PRD 校准的外推能区质心差直接作为短寿命确证。 | fast-timing-mscd-inference-boundary | direct-original-and-quantitative-audit | PDF27–30 Eqs3.8–3.16, PDF75–78; fast-timing-gcd-audit-026.json | true |

[[regis-2015-generalized-centroid-difference]] RG15-1–8保存公开出版物实际scope、6PDF页含空白末页、4图/12式、pair筛选/alignment/100Zr背景示例。其raw槽未填、publiccache已核，不写raw/Bib；不沿简化平均式给所有sorter背书。
