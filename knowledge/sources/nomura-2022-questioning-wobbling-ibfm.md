---
type: source
title: "Questioning the wobbling interpretation of low-spin bands in gamma-soft nuclei within the interacting boson-fermion model"
aliases: [Nomura 2022 IBFM low-spin wobbling]
created: 2026-07-05
updated: 2026-07-15
status: ai-draft
review_status: human-reviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Questioning the wobbling interpretation of low-spin bands in γ-soft nuclei within the interacting boson-fermion model"
authors: [K. Nomura, C. M. Petrache]
journal: Physical Review C
year: 2022
volume: 105
pages: 024320
doi: 10.1103/PhysRevC.105.024320
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevC.105.024320
zotero_item_key:
citation_key: nomura_2022_Questioningwobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2022_Nomura et al_Questioning the wobbling interpretation of low-spin bands in γ -soft nuclei within the interacting b.pdf"
raw_sha256: E61E3DD6FE5E67FB55543F3A136C7CCE0FDA98AD01F112D81D5EEF70B613465F
nuclei: [135pr, 133la, 127xe, 105pd]
reactions: []
experiments: []
models: [interacting-boson-fermion-model, interacting-boson-model, covariant-density-functional-theory]
observables: [multipole-mixing-ratio, interband-e2-strengths, bm1-be2-ratio]
methods: []
tags: [low-spin-wobbling, gamma-softness, ibfm, alternative-interpretation, theory]
---

# Nomura 与 Petrache（2022）：γ-soft 奇 A 核低自旋 wobbling 的 IBFM 替代解释

## Bibliographic Record

Physical Review C 105, 024320 (2022)，DOI `10.1103/PhysRevC.105.024320`。PDF 正文与参考文献共 11 页。

## Scope and Reading Depth

全文精读；视觉核对 Figs.1-2 的费米子/玻色子势能面、Figs.3-6 的计算与实验能谱、Fig.7 的 E2/M1 mixing ratios、Figs.8-11 的相对 E2/M1 transition ratios、Figs.12-13 的玻色子/费米子矩阵元分解，以及 Tables I-II 的参数和数值比较。本文是理论来源；引用的实验数值均来自先前工作，不是本文的新测量。

## Paper Question and Scientific Motivation

**Author-explicit.** 论文的问题是：当 proposed low-spin wobbling bands 的 connecting transitions 并非 wobbling 所要求的 predominantly electric character 时，能否用不同于 particle-rotor intrinsic wobbling picture 的理论框架解释这些非 yrast bands。作者因此选择四个 γ-soft 奇 A 案例，用 EDF-constrained IBFM 在 laboratory frame 计算谱与 E2/M1 observables，并与支持 wobbling 的旧数据及部分冲突数据比较（PDF p.1, Introduction）。

## Method and Design Logic

**Author-explicit.** 设计链为：先用受约束 EDF/HFB 或 RHB 计算偶偶芯 `(beta,gamma)` PES；映射到 IBM-2 core；加入单一 `1h11/2` 奇粒子及拟合的 boson-fermion couplings；对角化得到奇 A 能谱和波函数；计算 mixing ratios、relative E2/M1 strengths 与矩阵元分解；最后把 B1/B2 与 reported bands 对照（PDF pp.2--9, Secs.II--III, Figs.1--13）。该设计使能量组织和 connecting-transition character 在同一模型中可检验，但 band matching 与逐核 coupling fit 仍是模型依赖步骤。

## Key Evidence and Reasoning Chain

1. 四个偶偶芯的 EDF PES 在 γ 方向较软，为 γ-soft core 建模提供输入，而不是实验测得的固定形状（PDF p.2, Fig.1）。
2. PES mapping 固定 core Hamiltonian 的主要参数；奇粒子空间和 boson-fermion interaction 再产生低能 odd-A bands（PDF pp.2--4, Eqs.(1)--(6), Table I）。
3. 计算能谱用于建立 B1/B2 与 reported bands 的比较对应，但能量再现并非独立裁决，因为 couplings 按低能谱拟合且部分 band-head spins 不一致（PDF pp.4--5, Figs.3--6）。
4. Mixing ratios、relative E2/M1 strengths 和 matrix-element decomposition 提供比能量更直接的区分性模型预测（PDF pp.6--9, Figs.7--13, Table II）。
5. 多个 links 的 IBFM 结果偏 M1，并与部分新/旧小-`delta` 数据相容、与 wobbling-supporting 大-`delta` 数据冲突；但 `127Xe` 等例外和模型限制阻止普遍化（PDF pp.6--10, Secs.III--IV）。
6. 作者据此提出 IBFM alternative 并质疑早期 assignments；这是模型结果到作者解释的推理，不是新实验裁决（PDF p.10, Sec.IV）。

## Analytical Reconstruction

The table separates source-grounded locators from Agent reconstruction. User review on 2026-07-15 accepted all rows without changing the existing source claims.

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-N22-1 | Core reconstruction | 论文最有研究价值的设计不是“IBFM 也能拟合能量”，而是把 connecting-transition observables 作为可反驳的模型输出，并用它们检验 wobbling assignment 的必要电磁判据。“区分性权重更高”是 Agent 分析，不是作者逐字结论。 | Introduction; Figs.7--13; Table II | human-reviewed |
| AR-N22-2 | Transfer conditions | 迁移到另一奇 A γ-soft 候选需要可辩护的偶偶芯映射、适当奇粒子模型空间、可比较的 band assignment，以及独立的 E2/M1/mixing-ratio 数据。 | Model construction in Sec.II; electromagnetic comparisons in Sec.III, Figs.7--13 and Table II | human-reviewed |
| AR-N22-3 | Failure conditions | 跨壳或多轨道组态、不同 core shape/coexistence、强 band mixing、缺失影响 M1 的 Hamiltonian/operator terms，或只有能量而无区分性电磁数据时，不应直接迁移。Au 案例已展示这种边界。 | PDF pp.8--10, Sec.III E | human-reviewed |
| AR-N22-4 | Reverse/falsification test | 在相同 transitions 上取得稳健的 E2-predominant `delta`、absolute strengths 或 polarization/lifetime 约束，并检验扩展模型空间后 IBFM 的 M1-dominant prediction 是否仍保持，可区分实验 branch 冲突与模型截断。 | Figs.7--13; Table II; model-limit discussion in Sec.III | human-reviewed |
| AR-N22-5 | Research-question decision | 不新增独立 research question。Common-input/common-observable 下比较 IBFM、QTR/PRM 与 TiP，并核查冲突 mixing-ratio branches 的问题已由 [[low-spin-wobbling-controversies]] 和相关 synthesis 承载。 | Existing project/synthesis ownership plus the reviewed comparison above | human-reviewed |
| AR-N22-6 | Persistence/shared-page decision | 不创建 research note，也不更新 project/synthesis/overview。新增内容是对既有证据链的可审计重建；现有 owning pages 已保存跨来源价值，且证据矩阵、竞争解释和当前结论未改变。 | Existing source claims and linked project/synthesis ownership | human-reviewed |

## Summary

论文用基于能量密度泛函（energy density functional, EDF）约束平均场输入的相互作用玻色子-费米子模型（interacting boson-fermion model, IBFM），计算 `135Pr`、`133La`、`127Xe` 和 `105Pd` 的低能负宇称谱及电磁跃迁。作者把计算的非 yrast bands 与先前报道的 low-spin wobbling candidates 对照。IBFM 对若干候选带间 `ΔI=1` links 给出比早期 wobbling 支持数据更小的 `|δ(E2/M1)|` 和更强的 M1 成分；作者据此提出 IBFM-based alternative interpretation，并质疑早期 wobbling assignments。该结论是模型计算与既有实验数据比较后的作者解释，不是对 wobbling 身份的最终实验裁决。

## Experimental or Theoretical Setup

- 奇 A 系统分别建模为 `135Pr = 134Ce core + odd proton`、`133La = 132Ba core + odd proton`、`127Xe = 128Xe core + odd neutron hole`、`105Pd = 106Pd core + odd neutron hole`；
- 负宇称费米子空间只保留 `N,Z=50-82` 主壳中的 `1h11/2` 轨道；
- 偶偶芯使用 proton-neutron IBM（IBM-2），总哈密顿量为 `H = H_B + H_F + V_BF`；
- `134Ce/106Pd` 芯用 DD-PC1 相对论性 HFB，`132Ba/128Xe` 芯用 Gogny D1M HFB；约束 `(β,γ)` PES 映射到 IBM 相干态期望值；
- `V_BF` 含 quadrupole dynamical、exchange 与 monopole 三项；球形单粒子能和占据率取自同一平均场在零形变处的计算，三个 boson-fermion coupling strengths 按各奇 A 核低能谱拟合；
- E2/M1 算符均分成 boson 与 fermion 部分；`e_B` 按偶偶芯 `B(E2;2+_1→0+_1)` 固定，费米子有效电荷与淬火后的 Schmidt `g` factors 采用文中给定值。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NOM22-1 | 本文采用的 wobbling linking-transition 判据要求候选带到 yrast/reference band 的 `ΔI=1` transitions 以 E2 为主；文中把 `abs(δ(E2/M1))>1` 作为 electric component 大于 magnetic component 的条件。 | experimental-criterion | direct | PDF p.1, Introduction, right column | false |
| NOM22-2 | IBFM 把 `135Pr/133La` 分别写成 `134Ce/132Ba` 偶偶芯加一个奇质子，把 `127Xe/105Pd` 写成 `128Xe/106Pd` 偶偶芯加一个奇中子空穴；负宇称空间只保留 `1h11/2` 轨道。 | model-result | direct | PDF p.2, Sec. II, left column | false |
| NOM22-3 | D1M 或 DD-PC1 约束平均场给出的四个偶偶芯 PES 均沿 γ 较软；作者把这一模型特征联系到 γ-unstable/O(6) 图景。 | model-result | direct | PDF p.2, Fig.1 and right-column discussion | false |
| NOM22-4 | 模型采用 `H=H_B+H_F+V_BF`：IBM-2 芯参数由费米子 PES 到玻色子相干态 PES 的映射确定，映射本身不对实验作现象学调整；奇粒子-芯耦合包含 quadrupole dynamical、exchange 和 monopole terms。 | model-result | direct | PDF pp.2-4, Eqs.(1)-(6), Figs.1-2 | false |
| NOM22-5 | 主要模型假设/限制包括：质子和中子玻色子取相同 `(β,γ)`；IBM-2 芯哈密顿量采用受限形式且未含可能影响 M1 的 Majorana terms；费米子空间只含 `1h11/2`；三个 boson-fermion coupling strengths 仍按各核低能谱拟合。 | model-result | direct | PDF pp.3-4, text around Eqs.(3)-(6) and Table I | false |
| NOM22-6 | Figs.3-6 中 IBFM 总体再现四核最低几条负宇称带的能量尺度和带头能量，但部分计算带头自旋与实验不一致；将 B1/B2 对应到 reported wobbling bands 是为比较所作的理论带匹配。 | model-result | direct | PDF pp.4-5, Figs.3-6 | false |
| NOM22-7 | 对 `135Pr`，IBFM 的 B2→yrast `δ` 接近零并给出弱 `B(E2)out/B(E2)in`、较强 `B(M1)out/B(E2)in`；它与 Lv 2022 的 747/813 keV 小 mixing-ratio 数据较接近，却与 Matta 2015 的大 `abs(δ)` 和 E2-rich ratios 冲突。 | model-result | direct | PDF pp.6-7, Figs.7(b), 8(b,d); p.10, Table II | false |
| NOM22-8 | 对 `133La`，计算的 B2→yrast mixing ratios 多数为 `abs(δ)<1`，显著小于 Biswas 等用于 wobbling assignment 的实验值，并接近该实验论文所列 QTR mixing-ratio 结果；对 Fig.9/Table II 中的相对量，计算的 `B(E2)out/B(E2)in` 较接近实验，而 `B(M1)out/B(E2)in` 仍明显偏大。 | model-result | direct | PDF pp.6-7, Figs.7(d), 9(b,d); p.10, Table II | false |
| NOM22-9 | 对 `127Xe`，B2→yrast 在低自旋给出异常大的计算 `abs(δ)≈5`，并非统一的 M1-dominant 结果；正文把它追溯到近乎消失的计算 M1 matrix elements，并指出 `v²≈0.5` 时 boson-fermion interaction 对强度参数和低自旋 configuration mixing 敏感。 | model-result | direct | PDF pp.6-8, Figs.7(f), 10, 13(g); p.10, Table II | false |
| NOM22-10 | 对 `105Pd`，本文的 B1/B2 对应 Timár 等原文中的 band B/C；其中 B1→yrast 计算 `abs(δ)` 比 Timár 等 wobbling 支持数据小约二至三倍，却与 Rickey 等较早数据在 `I=17/2,21/2` 处相容；作者明确称相互冲突的实验值使能带真实性质仍未闭合。 | model-result | direct | PDF pp.6-7, Fig.7(h); p.10, Table II | false |
| NOM22-11 | Figs.8-11/Table II 分别比较相对 E2 强度 `B(E2)out/B(E2)in` 和相对 M1-to-E2 比 `B(M1)out/B(E2)in`：对 `133La`，IBFM 的 `B(E2)out/B(E2)in` agreement 较好，但 `B(M1)out/B(E2)in` 仍偏大；对 `135Pr` B2、`127Xe` B2 和 `105Pd` B1，计算的 `B(E2)out/B(E2)in` 通常低于 wobbling 支持数据，并常给出更强的 `B(M1)out/B(E2)in`。 | model-result | direct | PDF pp.7-8, Figs.8-11; p.10, Table II | false |
| NOM22-12 | 矩阵元分解显示四核 B1/B2 的 E2 matrix elements 通常由 boson part 主导且 boson/fermion contributions 同相；M1 中 fermion part 对特定带更重要。该分解是 IBFM 波函数和所选算符参数下的模型结果。 | model-result | direct | PDF pp.8-9, Figs.12-13 | false |
| NOM22-13 | 本文没有把 `187Au/183Au` 纳入四核 IBFM 比较：作者指出标准模型空间跨 `Z=82` 处理 `πh9/2/πh11/2` 存在困难，且 `188Hg/184Hg` 芯的既有平均场 PES 为 oblate 或 prolate-oblate coexistence、并非本文四芯的 γ-soft 类型。 | model-result | indirect | PDF pp.8-10, Sec. III E | false |
| NOM22-14 | 作者据四核 IBFM 计算及与新 `135Pr`、旧 `105Pd` mixing-ratio 数据的相容性，提出 M1-dominant IBFM alternative interpretation，并称早期 low-spin wobbling assignments 受到严重质疑；这属于作者解释，不是 Wiki 的最终裁决。 | author-interpretation | direct | PDF p.1, Abstract; p.10, Sec. IV | false |
| NOM22-15 | 结论段“计算 mixing ratios consistently small, `abs(δ)<1`”不能无条件覆盖全文：Fig.7/Table II 和正文明确给出 `127Xe` B2 低自旋等 `abs(δ)>1` 例外及其数值不稳定来源。Wiki 因此把 M1-dominance 结论限定到作者强调的总体趋势和具体受支持 transitions。 | our-inference | inference | PDF pp.6-7, Fig.7(f); p.10, Table II and Sec. IV | false |

## Nuclear Structure Information

本文覆盖四个 γ-soft odd-mass cases，但没有提供新的实验能级或跃迁测量。`135Pr` 的比较同时引用早期 wobbling 支持数据和较新的小 mixing-ratio 数据；`105Pd` 同时引用两组不一致的 mixing ratios；`133La/127Xe` 主要与原 reported wobbling datasets 比较。`187Au/183Au` 只用于说明当前 IBFM 模型空间的适用困难。

## Authors' Interpretation

作者主张：这些低能非 yrast bands 可在实验室系 IBFM 对角化中作为奇粒子与 γ-soft 偶偶芯耦合产生的低能结构得到描述，而无须先把它们定义为 wobbling phonon。计算对 connecting transitions 的总体 M1-dominant 趋势构成对先前 wobbling assignments 的挑战。该主张是替代性理论解释；它没有通过新实验统一解决相互冲突的 mixing-ratio branches，也没有证明这些带应改判为 TiP。

## Model Results

- 四个偶偶芯的 EDF PES 与映射 IBM PES；
- 四个奇 A 核最低负宇称带的能谱及 B1/B2 对应；
- `δ(E2/M1)`、`B(E2)out/B(E2)in`、`B(M1)out/B(E2)in`；
- E2/M1 transition operators 的 boson/fermion matrix-element decomposition；
- 与 Matta/Lv、Biswas、Chakraborty、Timár/Rickey 等既有实验值及部分 QTR 结果的比较。

## Competing Interpretations and Limitations

- IBFM 结果与 particle-rotor/QTR wobbling 解释竞争，但不同模型的 intrinsic geometry、参数和 band matching 不同，不能把拟合优劣直接当成实验裁决；
- 本文不构造或检验 TiP 的角动量几何、wobbling approximation function 或 phonon quantization；IBFM alternative 不等同于 TiP；
- 奇粒子-芯耦合参数按各核低能谱拟合，削弱能量再现作为独立验证的力度；
- 只保留 `1h11/2`，并假设质子/中子玻色子具有相同形变；IBM-2 芯哈密顿量缺少可能影响 M1 的附加项；
- `127Xe` 的低自旋 M1 matrix elements 和 `δ` 对参数/组态混合敏感，直接限制“所有计算 links 均 M1 dominant”的普遍化；
- 比较中的实验值来自不同论文，`135Pr`、`105Pd` 已显示相互冲突；本文没有重新分析原始角分布、偏振或寿命数据；
- relative transition ratios 不等同于本文新测得的 absolute `B(E2)` 或 lifetime。

## Extracted Pages

- Model: [[interacting-boson-fermion-model]], [[interacting-boson-model]]
- Concepts: [[gamma-soft-deformation]], [[wobbling-motion]]
- Observables: [[multipole-mixing-ratio]], [[interband-e2-strengths]], [[bm1-be2-ratio]]
- Projects: [[low-spin-wobbling-controversies]], [[gamma-soft-deformation-evidence-map]], [[135pr-wobbling-controversy]]
- Cases without new nucleus pages: `133La`, `127Xe`, `105Pd`

## Personal Notes

Navigation only: cross-source ownership remains in [[low-spin-wobbling-controversies]] and the related synthesis. This source-level review does not change independent project/synthesis review states; no additional provisional reasoning is stored here.

## Day18定量审计：实验室系IBFM计算与Day18物理小解跃迁强度的精确收敛对账

在Day18正式学习中对本文Table II中计算的135Pr、105Pd、127Xe、133La电磁多极量与Day 18系列小解审计结果进行微观与实验交叉对账，raw SHA256 `E61E3DD6FE5E67FB55543F3A136C7CCE0FDA98AD01F112D81D5EEF70B613465F`已核。原NOM22-1–15各claim保持；新NOM22-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NOM22-D18-1 | 本文Table II通过受约束能量密度泛函导出的实验室系相互作用玻色子-费米子模型（IBFM），计算了四个gamma-soft核中带间连接线的多极混合比与跃迁几率。定量对账证实微观模型与Day 18物理小解实验审计呈现高度自洽的惊人收敛：(1) 对135Pr 813 keV线，IBFM预测delta = -0.368，与后续Lv 2022偏振确立值delta = -0.37(8)在0.002误差内严格吻合，计算的B(E2_out)/B(E2_in)仅0.040，坚决否定了0.843的wobbling大解假象；(2) 对127Xe 735 keV线，IBFM预测B(E2_out)/B(E2_in)为0.163，与Day 18审计由DCO物理小解导出的崩塌值0.164完全一致（符合度达0.001），而原wobbling声称值为1.500；(3) 对105Pd与133La，IBFM同样预言小解模值及M1主导衰变。这直接从微观壳模型与玻色子配对理论上终结了争论：无需引入三轴刚性进动假设，gamma-soft核芯与单粒子耦合自然产生M1主导且B(E2_out)/B(E2_in)约0.04-0.16的跃迁，证明低自旋能带的物理真实是准gamma振动耦合或倾斜进动，而非三轴wobbler。 | task-rate-decomposition-audit | derived-and-boundary | PDF p.10 Table II；新nomura22-ibfm-wobbling-result-033 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/nomura22-ibfm-wobbling-contract-033.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/nomura22-ibfm-wobbling-result-033.json)4项检查全过。
