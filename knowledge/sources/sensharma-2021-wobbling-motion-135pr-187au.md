---
type: source
title: "Sensharma 2021 博士论文：135Pr 与 187Au 的横向、纵向和手征 wobbling"
aliases: [Sensharma 2021 wobbling thesis, Wobbling Motion in Nuclei dissertation]
created: 2026-09-05
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment-and-model
reading_depth: deep-read
title_original: "Wobbling Motion in Nuclei: Transverse, Longitudinal and Chiral"
authors: [Nirupama Sensharma]
advisor: [Umesh Garg]
journal: "University of Notre Dame doctoral dissertation"
year: 2021
volume:
pages: 205
doi:
arxiv:
language: en
canonical_source: "Sensharma, Nirupama. Wobbling Motion in Nuclei: Transverse, Longitudinal and Chiral[D]. University of Notre Dame, 2021."
zotero_item_key:
citation_key: ""
zotero_uri:
library_file: "raw/papers/degree dissertation/Wobbling_Motion_in_Nuclei.pdf"
raw_file: "raw/papers/degree dissertation/Wobbling_Motion_in_Nuclei.pdf"
raw_sha256: "954E6CC853536555F5A691D6EAA257AAA051F79960DE5EB47942F28FB335EF74"
nuclei: [135pr, 187au]
reactions: ["123Sb(16O,4n)135Pr", "174Yb(19F,6n)187Au"]
experiments: [atlas-digital-gammasphere-135pr-o16-80mev, atlas-gammasphere-187au-f19-105-115mev]
models: [particle-rotor-model, quasiparticle-triaxial-rotor-model, triaxial-projected-shell-model]
observables: [wobbling-energy, angular-distribution, dco-ratio, bm1-be2-ratio, signature-splitting]
methods: [gamma-gamma-coincidence, angular-distribution, charged-particle-gating]
tags: [a130, a190, wobbling, transverse-wobbling, longitudinal-wobbling, chiral-wobbling, phd-thesis]
---

# Sensharma 2021：`135Pr` 与 `187Au` 的横向、纵向和手征 wobbling

## Bibliographic Record

Nirupama Sensharma，*Wobbling Motion in Nuclei: Transverse, Longitudinal and Chiral*，University of Notre Dame，博士学位论文，2021，205 页。原始 PDF SHA-256 为 `954E6CC853536555F5A691D6EAA257AAA051F79960DE5EB47942F28FB335EF74`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: Abstract、Chapters 1–5 理论/实验/分析/结果及 Chapter 6 future work；核对 `135Pr` TW2→TW1 450.2/550.5/517.1 keV links、`E_wobb`、E2 fractions、`187Au` h9/2 longitudinal wobbling、h11/2 transverse candidate 和 `135Pr` chiral-wobbler 解释。
- Not covered: 所有引用文献及原始实验的独立全文复核；本页不替代已摄入 Sensharma 2019/2020 journal sources。
- Coverage caveats: 论文中的部分模型参数和结论直接复用/延伸既有 journal analysis；需按 shared dataset lineage 分层。

## Paper Question and Scientific Motivation

论文研究三轴核的 wobbling 模式（横向、纵向及多声子）并探索 `135Pr` 中 wobbling 与 chirality 共存、`187Au` 中 longitudinal/transverse 两类 wobbling 的实验判据（Abstract；Chapter 1）。

## Method and Design Logic

作者使用 Gammasphere 高统计 γγ 数据、角分布和 DCO-like ratios 识别 linking transitions，再用 `E_wobb`、相对 `B(E2)`/`B(M1)`、PRM/QTR/TPSM 和角动量几何比较模式类型（Chapters 3–5）。论文对 `135Pr` 与 `187Au` 分别保留实验事实、模型解释和仍需更高统计/偏振的边界。

## Key Evidence and Reasoning Chain

1. `135Pr` TW2→TW1 的 ΔI=1 transitions 具有 78–92% E2 admixture（Fig.4.17；Ch.5.1）。
2. TW2 wobbling energy 随自旋下降，且相对 E2 ratios 偏离 harmonic factor-of-two，支持 transverse、strong anharmonicity（Figs.5.1–5.3；Ch.5.1）。
3. `187Au` h9/2 links 显示高 E2 admixture，`E_wobb` 随自旋上升，作者称为 longitudinal（Figs.5.4–5.8；Ch.5.2.1）。
4. `187Au` h11/2 pair 的模型给出低自旋下降、约 `I≤25/2` transverse 候选，但作者明确要求更高统计（Figs.5.9–5.13；Ch.5.2.2）。
5. `135Pr` Dipole Bands 1/2 的能量、staggering、in-band ratios 和 large-E2-mixed links 被作者组合为 chiral-wobbler 候选（Figs.5.14–5.19；Ch.5.3）。

## Summary

论文把 `135Pr` 的 TW2 视为首个 A≈130 二声子 wobbling extension，把 `187Au` h9/2 结构视为 longitudinal wobbling，把 h11/2 pair 视为 transverse candidate，并将 `135Pr` 两条 dipole bands 提议为建立在 wobbling 上的 chiral bands。`187Au` h11/2 的结论在论文中仍是“promising/needs higher statistics”，`135Pr` chiral-wobbling 也明确写成 forthcoming work 前的解释候选。

## Experimental or Theoretical Setup

- `135Pr`：`123Sb(16O,4n)`，Gammasphere 高统计数据；TW2→TW1 links 为 450.2、550.5、517.1 keV。
- `187Au`：`174Yb(19F,6n)`，Gammasphere；h9/2、h11/2 结构和 seven-angle angular distributions。
- PRM/QTR/TPSM：模型形变、配对、转动惯量和角动量几何均为模型输入/结果。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| SE21-1 | `135Pr` TW2→TW1 的 450.2、550.5、517.1 keV ΔI=1 links 具有约 78–92% E2 admixture。 | experimental-criterion | direct | multiple-dependent | Fig.4.17；Ch.5.1 pp.121–125 | true |
| SE21-2 | `135Pr` TW2 wobbling energy 随自旋下降，TW2 相对 E2 ratios 偏离 harmonic factor-of-two，作者解释为 transverse wobbling 和强 anharmonicity。 | experimental-criterion + author-interpretation | indirect | multiple-dependent | Figs.5.1–5.3；Ch.5.1 pp.123–125 | true |
| SE21-3 | `187Au` h9/2 links 的 E2 character、随自旋上升的 `E_wobb` 和 PRM 比较被作者解释为 longitudinal wobbling。 | experimental-criterion + author-interpretation | indirect | multiple-dependent | Figs.5.4–5.8；Ch.5.2.1 pp.126–130 | true |
| SE21-4 | `187Au` h9/2 classical geometry 中 valence proton 不严格沿 medium axis，作者保留 longitudinal wobbling 与更一般耦合的边界。 | model-result + analytical-boundary | direct | multiple-dependent | Fig.5.5；Ch.5.2.1 pp.127–129 | true |
| SE21-5 | `187Au` h11/2 pair 的模型在 `I≤25/2` 给出下降 `E_wobb`、大 E2/small M1 ratios 和 transverse-wobbling candidate，但论文明确要求更高统计。 | author-interpretation | indirect | multiple-dependent | Figs.5.9–5.13；Ch.5.2.2 pp.131–136 | true |
| SE21-6 | `135Pr` Dipole Bands 1/2 的 excitation energy、staggering、in-band `B(M1)/B(E2)` 和 interband large-E2-mixed links 被组合为 chiral partners candidate。 | author-interpretation | indirect | multiple-dependent | Figs.5.14–5.18；Ch.5.3 pp.137–140 | true |
| SE21-7 | `135Pr` chiral-wobbler 的 PRM 角动量图显示三轴 aplanar geometry；作者在结尾说明 detailed theoretical interpretation 尚待后续发表。 | model-result + author-interpretation | indirect | multiple-dependent | Fig.5.19；Ch.5.3 pp.140–143 | true |
| SE21-8 | 论文中的模型参数（如 `135Pr` `ε≈0.17`, `γ≈35°` TPSM；`187Au` PRM β/γ）不是直接实验形变测量。 | model-result | direct | multiple-dependent | Ch.5.1–5.2 | true |
| SE21-9 | Eq2.45区分integer Mref=0与half-integer abs(Mref)=1/2的complete-alignment参考；Eq2.49定义alpha=rho/B，Eq2.50给离散CG tensor，Eq2.51的Gaussian指数分母是2sigma²。sigma是指数width，有限离散population的RMS须另算，不把其同名写成实际variance。 | tensor-reference-definition | direct | single | printed41–42/PDF63–64 Eqs2.45/2.49–2.51 | true |
| SE21-10 | Table4.1对135Pr854.3keV列alpha2=.92(5)、alpha4=.30(1)、adopted sigma/J=.2；Table4.3的同线为yrast23/2−→19/2−，列A2exp=.352(1)、A4exp=−.212(1)。两表参数层和source correction不能未经核对相互替换。 | calibration-input-identity | direct-and-self-audit | multiple-dependent | printed97/PDF119 Table4.1；printed109/PDF131 Table4.3 | true |
| SE21-11 | 本任务在同J=23/2、alpha=rho/B及half-integer参考条件下，精确CG/Stevens与独立LP给所有positive P的必要式7−10alpha2+3alpha4≥0；Table4.1均值给−1.3，字面quoted-margin矩形最大仍−.77。此为有条件的定义/校准合同失配，不是作者报告、统计拒绝或原数据错误判决；fullresponse/归一程序未得。 | our-inference | indirect | single | premises printed41–42 Eqs2.45/2.49/2.50；printed97 Table4.1；new canonical calibration audit | true |
| SE21-12 | 854.3参考的below659.8 gate/singles给delta−.04(1)/−.06(1)，此处是DeltaI2的E2/M3对，不是M1/E2；450.2的below372.9/746.6两门给−1.95(3)/−1.85(3)。作者称这些控制支持gate保存角分布；未知共享Cov/response时不据字面误差重算显著性或推广为任意门独立定理。 | gate-control-and-multipole-boundary | direct-and-self-audit | multiple-dependent | printed100–102/PDF122–124 Figs4.14/4.15及正文；printed104/PDF126 pair说明 | true |
| SE21-13 | 作者先合并对称rings形成17.27、34.58、50.07、58.28、69.82、80、90度七组，再逐组效率校准；DCO-like另用Table4.2的forward/middle/backward分组。不是14份独立镜像观测，也不能同别的R定义直接共用阈值。 | geometry-and-sorting-identity | direct-and-self-audit | multiple-dependent | printed96/PDF118；printed103/PDF125 Table4.2；printed151/PDF173 TableA.2 | true |
| SE21-14 | 先用A2初值和Eq2.46/48求delta二根，因A4相对误差大而不另解其二次式；后续仍用W(theta)的A2/A4及chi²选择、细采样。不能将“不解A4二次式”误写成从未利用A4，也不能由初始independent proposal推断posterior Cov=0或全部分支权重已给。 | fit-recipe-boundary | direct-and-self-audit | single | printed98–99/PDF120–121 MCMC五步骤 | true |
| SE21-15 | Table4.1 attenuation提取指向Ref26 Cieplicka2012 PRC86,054322；sigma对应关系指向Ref56 Mateosian/Sunyar1974 ADNDT13,391–406；Ref57是Matta2017 Springer书DOI10.1007/978-3-319-53240-0，Ref99为Yamazaki1967。这些是不同source/版本，未读正文者只作定向跟进线索。 | method-provenance-lead | direct-bibliographic | multiple-dependent | printed175/PDF197 Ref26；printed177/PDF199 Refs56/57；printed181/PDF203 Ref99 | true |
| SE21-16 | 本任务以Eq2.42/43/51、854.3的E2/M3 source ratio、sigma/J=.2构建point single-gamma条件模型。delta−.04/−.06时预测(A2,A4,A6)=(.313673,−.147476,.00026676)/(.289881,−.165429,.00059901)，原文字面delta范围内A4仍未到Table4.3的−.212。source-F与RB直接振幅两路、primary控制和物理极限通过；不是实际response/作者程序或delta重拟合。 | our-inference | indirect | single | premises printed40–42 Eqs2.42/43/51；printed100–101 Fig4.14；printed109 Table4.3；new M3 reference model | true |
| SE21-17 | 同一条件模型的post-calculation scope control：真实Gaussian alpha=(.894266,.689096)物理有效，另取固定operators下的物理相位delta=+.04，仅若误按pureE2反演，会得apparentalpha=(1.009932,.464384)、必要式为−1.706165。它是有意选定的反例，不是源报告delta或KS/RB坐标重写；说明错误reference前提可制造apparent正性失配，不能据此判原数据不物理或定位源问题。 | our-inference | indirect | single | premises printed41–42/97–102；KS70-13/RB67-11；conditional M3 scope control | true |

## Nuclear Structure Information

- `135Pr`：yrast、TW1、TW2、signature partner 和 Dipole Bands 1/2；二声子、手征和 chiral-wobbler 均需保留作者解释层。
- `187Au`：h9/2 longitudinal-wobbling pair、h11/2 transverse candidate 和 signature partner。
- `E_wobb`、E2/M1 ratios、mixing ratios 和角动量概率分布是核心判据。

## Authors' Interpretation

作者认为 `135Pr` TW2 是 transverse two-phonon wobbling，`187Au` h9/2 是 longitudinal wobbling，h11/2 是 hole-like transverse candidate；`135Pr` Dipole Bands 1/2 可能是建立在 wobbling 上的 chiral pair。所有解释均需与现有反方/替代来源并列。

## Model Results

- QTR/TPSM reproduce `135Pr` energies and transition-ratio trends with differing anharmonicity。
- PRM reproduces `187Au` h9/2 increasing `E_wobb` and h11/2 geometry under selected parameters。
- PRM aplanar angular-momentum distributions support the chiral-wobbler geometry candidate。

## Competing Interpretations and Limitations

- `135Pr` low-spin wobbling has later independent angular-correlation/polarization counter-evidence；本论文不能单独裁决 wobbling。
- `187Au` h11/2 transverse claim 明确需要更高统计，不能升级为 established wobbling。
- E2 admixture、`B(E2)_out/B(E2)_in` 和 `E_wobb` 依赖 mixing-ratio branch、模型惯量和 shared dataset；不能把相对量写成绝对 transition strengths。
- `135Pr` chiral-wobbler 只在作者候选层级；未给出完整绝对矩阵元和独立几何测量。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-SE21-1 | Core reconstruction | 该论文把 wobbling 判据从单一能级趋势扩展到 E2/M1、anharmonicity 与 angular-momentum geometry 的联合链。 | Ch.5 | unreviewed |
| AR-SE21-2 | Assumptions and dependencies | 多数结论依赖 shared Gammasphere datasets、mixing-ratio analysis 和 PRM/QTR/TPSM parameterization。 | SE21-1–8 | unreviewed |
| AR-SE21-3 | Transfer conditions | 可用于比较 transverse/longitudinal/chiral-wobbling 的证据结构，但不能替代 independent counter-source。 | SE21-2–7 | unreviewed |
| AR-SE21-4 | Failure conditions | 若偏振、`R_ac`、绝对 strengths 或独立数据重分析不支持 E2 links，wobbling/chiral-wobbler 排序需降级。 | Existing 135Pr/187Au controversy pages | unreviewed |
| AR-SE21-5 | Reverse/falsification test | 逐 link 回查 mixing ratio、polarization、`E_wobb`、band identity 和 source independence，并比较 signature-partner/TiP alternatives。 | SE21-1–7 | unreviewed |
| AR-SE21-6 | Research-question decision | 接入 `135Pr`/`187Au` controversy maps，优先做 shared-data 与 independent-data evidence audit。 | SE21-3–7 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 Sensharma 2019/2020、Lv 2022、Guo 2022 的相关来源；本论文提供更完整的 thesis-level method/result chain。
- Effect of this source: supports and limits；对 wobbling 证据链做结构化补充，但不改变现有争议排序。
- Reason: 将 TW2、longitudinal h9/2、h11/2 candidate 和 chiral-wobbler 的判据/限制统一定位。
- Persistence decision: 新建 source；更新 `135pr`、`187au` 相关来源关系和争议项目入口；不新建重复 band pages。
- Review state: 页面 `unreviewed`；SE21-1–8 均保留 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[135pr]] | 复述/扩展 TW2、chiral-wobbler 与 shared Gammasphere evidence chain。 |
| supports | [[187au]] | 提供 h9/2 longitudinal 与 h11/2 transverse candidate 的 thesis-level chain。 |
| competing-interpretation | [[135pr-wobbling-controversy]] | 与 Lv 2022 的 independent polarization/angular-correlation counter-evidence 并列。 |
| competing-interpretation | [[187au-longitudinal-wobbling-controversy]] | 与 Guo 2022 的 independent `R_ac-P`/QTR reinterpretation 并列。 |

## Human Review Triage

### P0

- SE21-1/SE21-2：核对 `135Pr` TW2→TW1 links 的 E2 percentages、`E_wobb` 定义和 successive phonon spacing；风险是把“TW2 能量低”写成错误的 two-times statement。
- SE21-3/SE21-5：核对 `187Au` h9/2/h11/2 band identity、E2/M1 branches 和“first/cleanly established”措辞；风险是遗漏论文自身对 h11/2 高统计限制。
- SE21-6/SE21-7：核对 `135Pr` chiral-wobbler 的 six links、staggering/B(M1)/B(E2) 和作者“forthcoming”边界；风险是把候选写成确证。

### P1

- SE21-8：核对所有 PRM/QTR/TPSM deformation parameters 的来源和单位。
- 与 Sensharma 2019/2020、Lv 2022、Guo 2022 做 shared/independent data lineage audit。

### P2/P3

- 不再重复建立现有 `135Pr`/`187Au` band pages；仅补来源链接和演化日志。

## Extracted Pages

- Nuclei: [[135pr]], [[187au]]。
- Bands: 使用已有 `135Pr`/`187Au` band pages；不新增重复页面。
- Experiments: [[atlas-digital-gammasphere-135pr-o16-80mev]], [[atlas-gammasphere-187au-f19-105-115mev]]。
- Concepts/observables: [[transverse-wobbling]], [[longitudinal-wobbling]], [[wobbling-motion]], [[nuclear-chirality]], [[angular-distribution]]。

## Non-source Notes and Follow-up

本 thesis 与已摄入 Sensharma journal sources 可能共享实验数据；后续 source-independence 必须显式标注，不能把 thesis 叙述当成新的独立实验复制。

## 2026-09-11 L3 Evidence-Independence Audit

本次按核素和实验运行拆分 thesis 中的支持链与 Wiki 已有的反方/替代来源；“独立”只表示当前记录中的实验数据链不同，不表示作者、装置技术或理论框架完全没有重叠。

| Case | Support-side source lineage | Counter/alternative lineage | Current independence result |
|---|---|---|---|
| `135Pr` | Sensharma 2019 与本 thesis 都围绕 `123Sb(16O,4n)135Pr`、80 MeV Gammasphere 数据；thesis 是更完整的 dissertation-level 复述/延伸，不增加独立实验数。 | Lv 2022 使用 `100Mo(40Ar,1p4n)135Pr`、152 MeV JUROGAM II，约 `5.1×10^10` fold≥3 events，并以 `P-R_ac` 联合约束 747/813/450 keV links（[[lv-2022-evidence-against-wobbling-135pr]] L22-1–5）。 | 反方数据链与 Sensharma 支持链区分明确；关键 δ/E2 判据仍存在方法冲突，不能由 lineage audit 单独裁决。 |
| `187Au` | Sensharma 2020 合并 105/115 MeV `19F+174Yb` Gammasphere runs；本 thesis 的 `187Au` 章节使用同一支持方结构和分析谱系，不作第二个实验计数。 | Guo 2022 的 HIRFL `18O` 外靶数据链提供独立 `R_ac+P` counter/reinterpretation；其 supplementary 是同一 Guo 实验的附属证据，不另计独立来源。 | 支持方与 Guo counter 数据可分层为不同实验链；reported band (3) 的身份、早期 conversion/β-decay 转述和低自旋替代解释仍未由底层原始来源完全闭合。 |

必要伴随证据审计：两边都没有一套可统一比较的 partner-resolved lifetime 和 absolute `B(E2)/B(M1)`；当前 E2 fraction、relative ratios、`E_wobb` 和模型几何只能约束候选解释。missing polarization/弱 link、band identity 或 lifetime 若被后续原始数据改变，会触发 wobbling→TiP/single-particle/signature interpretation 的 belief revision。因而 `SE21-1..8` 的研究状态不提升，且不启动 L4。

## 2026-10-17方法章定向回核与校准边界

先冻结primed回忆，核原205页raw hash；本次全文仅检索定位，实际读PDF60–64、80–83、118–131的相关methods/table、PDF173和197/199/203相关reference。视觉核Eq2.45/2.49–2.51、Table4.1、Table4.3的854.3行、gate控制及七组角表。未重读全部205页，不以此核准Springer2022版本的页码/公式。旧SE21-1–8及review flags保留，新9–15仅Codex self-audit、true。

[[se21-alignment-calibration-consistency]]用新的实际Table4.1输入/J=23/2复用通用finite-J CG helper，不重跑旧67Ga数据充学分。源自定义的Gaussian sigma/J=.2给(alpha2,alpha4)=(.894266,.689096)；逐个匹配alpha2/alpha4的width分别.175284/.350794。更强的positive-population证书排除该字面pair作共同nuclear rho/B；只是把“alpha_exp可以直接当nuclear alignment”的假设改为needs-review。换成非Gaussian P本身不足以消除该条件失配，实际calibration/geometry/gate及reference混合成分仍须核，不能宣布实验或作者code错误。

另用明确doubled-spin CG与pureE2 photon basis给此23/2→19/2的complete-reference系数65/161、−26/161；adoptedGaussian的系数.361039/−.111283。Table4.3字面系数若在该pure-point约定直接相除，得到.871877/1.312769而非Table4.1的.92/.30，进一步表明层次尚未闭合。此计算不是E2/M3响应重拟合；原文small E2/M3、geometry、gate及production normalization均保留为边界，不生成新delta或wobbling裁决。

### 854.3参考的有界E2/M3 forward检查

[[se21-alignment-calibration-consistency]]新增的single-gamma doubled-spin模型先通过DA74 primary rows、DMS74 negative-column作者例题、source-F/direct-amplitude一致和rate/symmetry/degenerate控制，再评估原文small M3 ratio。12/16-node convergence与两路系数差最大约1.1e−14；不用整数专用joint kernel外推half spin，也没有对sigma/delta自由拟合。

结果说明small radiative fraction仍可线性干涉A4，但在声明的point/Gaussian .2条件内，源gated/singles两个ratio范围和七角equal-weight P6遗漏效应均不足以把模型系数移到Table4.3。正性scope反例只证明alpha_exp解释依赖reference纯性，并未复现Table4.1的实际操作或认定真实原因。原始逐角净峰/校准program、actualgeometry/gate/covariance仍缺，停止调参；理论/模型结果不冒充实验事实，新16/17 true，旧flags保持。

Ref26 Cieplicka2012目前仅核DOI/title及OpenAlex/OSTI metadata；publisher/acceptedPDF403、OSTIAPI/record ConnectionError，未得到正文。下载工具拒绝Wiki绝对savePath后未绕过其目录限制。Ref57 Matta2017 public discovery restricted，亦未读body；这些是本run获取边界，不是“世界上不存在可访问版本”的结论。
