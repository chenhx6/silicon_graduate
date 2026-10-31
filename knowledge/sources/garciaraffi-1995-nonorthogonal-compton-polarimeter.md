---
type: source
title: "Non-orthogonal gamma-ray Compton polarimeters"
aliases: ["Garcia-Raffi 1995 non-orthogonal polarimeter", "EUROBALL CLUSTER non-orthogonal polarimetry"]
created: 2026-09-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: method
reading_depth: deep-read
title_original: "Non-orthogonal gamma-ray Compton polarimeters"
authors: ["L. M. Garcia-Raffi", "J. L. Tain", "J. Bea", "A. Gadea", "L. Palafox", "J. Rico", "B. Rubio"]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1995
volume: 359
pages: "628-631"
doi: "10.1016/0168-9002(95)00229-4"
citation_key: Garcia_Raffi_1995
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
language: en
canonical_source: "Garcia-Raffi, L. M. et al. Non-orthogonal gamma-ray Compton polarimeters. Nucl. Instrum. Methods Phys. Res. A 359, 628-631 (1995)."
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1995_Garcia-Raffi et al_Non-orthogonal gamma-ray compton polarimeters.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1995_Garcia-Raffi et al_Non-orthogonal gamma-ray compton polarimeters.pdf"
raw_sha256: "129ccca13b7e6ea0153b47e81a37d54832b4979eb6e649cc183822a9b76ff67a"
nuclei: []
models: ["Geant3-Monte-Carlo-response"]
observables: ["linear-polarization", "polarization-asymmetry", "polarimeter-sensitivity", "figure-of-merit", "coincidence-efficiency"]
methods: ["compton-polarimetry", "linear-polarization-asymmetry", "detector-response-simulation"]
tags: [non-orthogonal-polarimeter, EUROBALL, CLUSTER, Compton-scattering, detector-response, P-A-Q]
---

# Non-orthogonal gamma-ray Compton polarimeters

## Bibliographic Record

- 作者：L. M. Garcia-Raffi 等。
- 期刊：*Nuclear Instruments and Methods in Physics Research A* 359, 628-631 (1995)。DOI：`10.1016/0168-9002(95)00229-4`。
- 原始文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1995_Garcia-Raffi et al_Non-orthogonal gamma-ray compton polarimeters.pdf`；SHA-256：`129ccca13b7e6ea0153b47e81a37d54832b4979eb6e649cc183822a9b76ff67a`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.628-631 全文；非正交 geometry 的理论推导、`P/A/Q` 关系式、merit 定义、EUROBALL CLUSTER 七晶体几何、Geant3 simulation、threshold/energy dependence、Fig.1-3 和总结均已阅读。
- Not covered: 原始 Geant3 input、实测 CLUSTER response 数据和后续“to be published” polarimeter source。
- Coverage caveats: 论文是理论/模拟方法 Letter；CLUSTER 的 Q、efficiency 和 merit 主要是设计几何下的计算，不是普适 detector constants。

## Paper Question and Scientific Motivation

- 正交 Compton polarimeter 通常把两个分析方向设为 0°/90°；EUROBALL CLUSTER 的七晶体 honeycomb geometry 不能简单旋转到正交方向。论文推导非正交方向下由 measured asymmetry 反演 `P` 的关系，并判断这种配置是否仍有足够 merit（PDF pp.628-629）。

## Method and Design Logic

- 对任意两个 analyzer 方向 `φ`、`φ'`，由 Klein-Nishina cross section 写出 scatter rates。非正交 polarimeter 的 asymmetry 一般写成
  \[
  A=\frac{Q_3+Q_2P}{1+Q_1P},
  \]
  其中 `Q1,Q2` 由两个方向和pointQ0决定，原Eq10给Q3=0（printed629 Eqs7–11）。只有匹配归一/对称合同才可退为线性，详Day17补段。
- 为方便使用，作者把 `Q=Q2` 作为 sensitivity，并写出 polarization-dependent effective factor `Q/(1+αQP)`；扩展 polarimeter 的 Q 需用 known-P transitions 校准或由等效正交装置估计（PDF p.629，式 (12)-(13)）。
- Merit `M` 同时包含 efficiency、asymmetry correction 和 Q；小偏振近似下可用 `M=4f/(1+f)^2 εQ²` 比较不同非正交配置（PDF p.630，式 (14)-(15)）。

## Key Evidence and Reasoning Chain

1. CLUSTER 由 7 个紧密排列的 hexagonal Ge crystals 组成；选择四组相邻 crystal pairs 作为 `0°/60°/120°` 等方向，效率比只使用 0°/90° 配置更高（PDF p.630，Fig.2）。
2. 简单几何估计和 Geant3 Monte Carlo 均显示：非正交组合灵敏度有所降低，但可通过更多 coincidence pairs 提高效率和 merit；threshold 提升会提高 Q、降低 efficiency（PDF pp.630-631，Fig.3）。
3. 在 `~1.3 MeV`，CLUSTER sensitivity 与四扇区 coaxial Ge 装置相近；在 `4.4 MeV` sensitivity 降到约后者的三分之一，但 merit 在 `1.3 MeV` 可高约数倍（PDF p.630-631）。
4. 结论是：只要用非正交公式而不是硬套 `A=QP`，某些几何下无需把 CLUSTER 物理旋转 90°，仍可用于 γ 线性偏振测量（PDF p.631）。

## Summary

该 Letter 把非正交 Compton polarimeter 的几何不对称显式写进 `A(P)` 关系，指出在原efficiency-normalized point配置中，Eq10的Q3恒为0；非正交可产生polarization-dependent denominator，而未校efficiency/其它response才可能另有offset。对 EUROBALL CLUSTER，选择多个相邻晶体 pair 可弥补部分灵敏度损失；最终性能取决于 Q、coincidence efficiency、threshold 和 background。它为现代多晶体/跟踪阵列方法提供一个重要边界：测得的 count asymmetry 不能在非正交几何下直接用正交 `A=QP` 解释。

## Experimental or Theoretical Setup

- Detector concept: seven individually canned tapered hexagonal Ge crystals in a honeycomb CLUSTER detector。
- Simulation: modified Geant3 including linear polarization in Compton scattering; design distance `d=44 cm`。
- Energies: `0.197, 0.423, 0.847, 1.368, 2.754, 4.438 MeV`；sector thresholds `40` and `350 keV`。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR95-1 | 非正交 polarimeter 的一般关系为 `A=(Q3+Q2P)/(1+Q1P)`，正交极限才退化为线性 `A=QP`。 | method-definition | direct | PDF p.629，式 (7)-(13) | false |
| GR95-2 | CLUSTER 采用多个相邻 crystal pairs 的 `0°/60°/120°` 几何，比单纯 0°/90° 配置具有更高效率。 | detector-design | direct | PDF p.630，Fig.2 | false |
| GR95-3 | threshold 提高会提高 Q、降低 efficiency；总体 merit 需要同时考虑两者，而不能只最大化 Q。 | detector-result | direct | PDF pp.630-631，式 (14)-(15)，Fig.3 | false |
| GR95-4 | CLUSTER 在约 1.3 MeV 的 sensitivity 可与四扇区 coaxial Ge 相近，并可能有更高 merit；高能端 sensitivity 相对下降。 | simulation-result | direct | PDF pp.630-631，Fig.3 | true |

## Nuclear Structure Information

- 不适用；来源是 detector/formalism 方法论文，未提供具体核素结构结论。

## Authors' Interpretation

- 非正交 geometry 并不自动使 polarimeter 无效；正确的 `A(P)` 参数化和 merit 评估可以判断是否值得使用。

## Model Results

- Geant3 simulation 预测 CLUSTER 的 sensitivity、efficiency 和 merit；这些是 detector-response 结果，不是核结构模型输出。

## Competing Interpretations and Limitations

- 若直接把非正交测量套入正交 `A=QP`，会产生偏振值偏差；`Q1/Q2/Q3` 与方向定义必须显式报告。
- 计算 merit 忽略或简化 peak-to-background、实际 dead time、response nonuniformity 和后续 reconstruction；实测值需独立校准。
- `1.3 MeV` 与 `4.4 MeV` 的比较只属于该 CLUSTER/距离/threshold 设定，不能移植到其它阵列。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-GR95-1 | Core reconstruction | 非正交几何的核心不是一个新物理偏振定义，而是 count asymmetry 到 P 的响应函数改变。 | PDF pp.628-630 | self-checking |
| AR-GR95-2 | Assumptions and dependencies | 依赖 pointlike/extended geometry、方向角、Klein-Nishina response、efficiency ratio 和 known-P calibration。 | PDF pp.629-631 | self-checking |
| AR-GR95-3 | Transfer conditions | 公式结构可迁移，`Q1/Q2/Q3` 数值必须按每个阵列 response 重建。 | PDF pp.629-631 | provisional |
| AR-GR95-4 | Failure conditions | 未建模 geometry、threshold、background 或 detector pair efficiency 会使 merit/反演偏差。 | PDF pp.630-631 | active-L3 |
| AR-GR95-5 | Reverse/falsification test | 用已知-P calibration lines 和 unpolarized source 验证 offset、denominator 和 pair efficiency；与正交 reference polarimeter 交叉比较。 | PDF pp.629-631 | candidate-L3 |
| AR-GR95-6 | Research-question decision | 作为现代 clover/tracking polarimetry 的非正交 response bridge 持久化；不启动 L4。 | PDF pp.629-631 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 P/A/Q 分层和现代 tracking-array formalism，但尚未记录非正交 geometry 的 `Q1/Q2/Q3` 响应项。
- Effect of this source: `revises` and `methodological-bridge`。
- Reason: 来源限制了“所有 polarimeter 都可用 `A=QP`”的过度简化，并补充 geometry-specific merit 评估。
- Persistence decision: update [[compton-polarimetry]] and [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] project source set。
- Review state: `unreviewed`; method claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[compton-polarimetry]] | 非正交 Compton response、offset/denominator 和 merit 定义。 |
| limits | [[linear-polarization-asymmetry]] | 限制把非正交 detector asymmetry 直接当作 `A=QP`。 |
| supports | [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] | 连接早期 segmented/CLUSTER polarimeter 与现代 detector response map。 |

## Human Review Triage

### P0

- GR95-P0-1：非正交 geometry 下必须使用完整 `Q1/Q2/Q3` 关系；不能把 `Q2` 当作无条件 universal sensitivity。

### P1

- GR95-P1-1：CLUSTER simulation merit 与现代阵列比较前需匹配 detector size、distance、threshold 和 background。

### P2/P3

- DOI/卷页和 PII 已由 PDF metadata 对齐；后续只需在方法项目中维护来源关系。

## Extracted Pages

- Nuclei: 不创建。
- Bands: 不创建。
- Concepts: physical polarization、non-orthogonal Compton response、detector merit。
- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。

## Non-source Notes and Follow-up

- 下一步：将 GR95 的非正交响应边界加入 gamma-ray polarization project 的 evidence table，并继续 HS-010。


## Day17原件自审：非正交分母与零偏置条件

本session先冻primed回忆再新读4页/3图/15式/8refs，hash129ccca13b7e6ea0153b47e81a37d54832b4979eb6e649cc183822a9b76ff67a/394455bytes保持。旧GR95-1–4行/falsefalsefalsetrueflags保持，reviewunreviewed；新12条待审。原本就是theory/simulationletter，以下不新增实验或认证原modifiedGEANT3producer。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR95-D17-1 | 原P=(Iparallel−Iperp)/(sum)，Eq6先对两N除各efficiency再差/和，Eq7的一般ratio到Eq10给Q3=0（该normalizedpointsetup恒等）；非正交不是天然有offset。旧Wiki把offset当必然的叙述已收缩，未校eff/其它response另需合同。 | normalized-offset correction | direct | pp.628–629 Eqs1/6–10 | true |
| GR95-D17-2 | pointθ90下Q0=a/(a²−a+1)、a=1/(1+E/mec²)，Q1=(sin²φ′−cos²φ)Q0、Q2=(cos²φ−cos²φ′)Q0。φ0/φ′60给Q1=−Q0/4、Q2=3Q0/4、alpha=−1/3，A=QP/(1−QP/3)，P=A/[Q(1+A/3)]。 | actual-geometry algebra | direct plus arithmetic | p.629 Eqs8–13 | true |
| GR95-D17-3 | 本非正交的P相关sum使Eq12/13分母真实必要；与B73正交原P=A/Q不同，不能把一个分母跨对象搬运。正交sin²φ′=cos²φ令Q1=0，Q2可正/负/零，不能所有pair任称正Q。 | limiting-case and transfer-boundary | direct | p.629 following Eq11 and Eqs12–13 | true |
| GR95-D17-4 | 作者对extendedpolarimeter沿Eq12仅称seemsreasonabletoassume，Q由knownP校准或同geometry正交估计。实际两extendedchannel的cos2响应未取得，alpha未被实测/全核证明固定为pointgeometry值，不能把单点Q校准当两响应参数独立识别。 | author-assumption and readiness | direct | p.629 following Eq12 | true |
| GR95-D17-5 | 新独立pointKN计数组对原0/60几何在E1.368给Q0=.339091/Q=.254318，P±1时A=.277874/−.234444；裸A/Q给1.092625/−.921852，而完整inverse还原±1。orthogonal/null/labelswap/zeroQ控制过，非新MC或实际arraybias。 | Codex source-geometry exercise | derived conditional | p.629 Eqs3–13 | true |
| GR95-D17-6 | 一般normalizedextendedrates n_i=1−q_iP产生Q1/Q2；若不预固定alpha，two known distinctnonzeroP从P/A=1/Q2+(Q1/Q2)P可辨两参数，一knownP不够，null只约offset。新正的responsecountercontrolalpha=−5/11不同point−1/3只是合同反例，不判原CLUSTER失效。 | calibration-identifiability design | derived | p.629 Eqs7/12–13 | true |
| GR95-D17-7 | Fig2 actualN0为12/34/15/67四对，N60等价组为13/45/16/27/14/56/17/23八对；作者简单equaladjacentpair估f2、εnonrot=3εrot、Q=.75Q0，Eq15 merit比=3×(.75)²×8/9=1.5。不是实测12对独立Cov或任意事件sorting证明。 | actual-pair grouping and approximation | direct and arithmetic | p.630 Fig2 and Sec3 | true |
| GR95-D17-8 | Eq14的finiteA计时量与Eq15smallP merit不同；原忽略peak/background依赖，ε定义为unpolarizedphoton总coincidenceeff，f为两组ε比。新literalEq14在1.368P±1给相对rotmerit1.57186/1.29496，不把1.5普推全P/含背景实际time。 | finite-P and denominator-boundary | direct plus conditional replay | p.630 Eqs14–15 | true |
| GR95-D17-9 | Fig3是modifiedGEANT3含POL的模型：source距44cm、六γ输入.197/.423/.847/1.368/2.754/4.438MeV、twofold阈值40或350keV；Q/eff/merit共享同模拟，非六条实测knownP标定或独立三证据。actual修改Ref7为tobepublished，input/events/Cov未得。 | simulation-provenance | direct | pp.630–631 Fig3 and References6–7 | true |
| GR95-D17-10 | higherthreshold在该模型增加Q但效率损失使merit变差；同solidangle与sectoredcoax比较约1.3MeV M近5倍、高能>2倍但Q在4.4仅约1/3，作者明确systematicasymmetry需控制。不能仅Q提升选cut或称含背景实验优势已证。 | counter-evidence to Q-only optimization | direct-model interpretation | pp.630–631 Fig3 discussion | true |
| GR95-D17-11 | 当前publicGEANT3标准callpath无POL消费的既有Wiki核验与原95modifiedproducer不是同代码；本session只新读文和解析point设计，未用旧Day16MCchecks认证原Fig3或补真实response。 | code-version and independence boundary | source-mapped readiness | p.630 simulation paragraph; p.631 Ref7 | true |
| GR95-D17-12 | 本sessionQ3=0/0–60inverse/finiteP与smallP对照修订Wiki泛offset，保完整P/A/Q/eff合同；无newexperimentalP/Q/CI/merit/模式推断。 | knowledge-impact and limits | synthesis | Eqs6–15; Fig2 | true |

[原geometry/pairedgroups输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/garciaraffi1995-geometry-contract.json)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/garciaraffi1995-geometry-result.json)，script `system/scripts/day17_gr95_nonorthogonal_audit.py`。ε0=1/ε60=2是原simplepairratio的声明pointdesign，原actualcounts/eff/Cov未取得；rawunpoloffset1/3经eff归一消失，不以此模拟真实仪器偏置。

这也解释B73旧误式为何不能凭形状迁移：Eq13的1−alphaA是此nonorthogonal模型反演的一部分，B73实际正交Eq4并无此项。[[compton-polarimetry]]/[[linear-polarization-asymmetry]]/[[polarimetry-shared-calibration-count-design]]分别记录对象；本页不修raw或旧reviewflags。
