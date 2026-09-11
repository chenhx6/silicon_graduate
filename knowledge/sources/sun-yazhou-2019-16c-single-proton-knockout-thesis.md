---
type: source
title: "孙亚洲 2019 博士论文：16C 单质子敲出反应研究"
aliases: [Sun Yazhou 16C knockout thesis, 16C single-proton knockout]
created: 2026-09-11
updated: 2026-09-11
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment
reading_depth: deep-read
title_original: "16C 单质子敲出反应研究"
authors: [孙亚洲]
advisor: [孙志宇]
journal: "中国科学院近代物理研究所博士学位论文"
year: 2019
volume:
pages: 116
doi:
arxiv:
language: zh/en
canonical_source: "中国科学院近代物理研究所博士学位论文, 2019"
zotero_item_key:
citation_key:
zotero_uri:
library_file: "raw/papers/degree dissertation/孙亚洲 - 16C单质子敲出反应研究.pdf"
raw_file: "raw/papers/degree dissertation/孙亚洲 - 16C单质子敲出反应研究.pdf"
raw_sha256: "d9d900cfdd783890f2f5d774b18832bbfda40eeb2af2db50b353ac18373496c0"
nuclei: [16c, 15b, 12c]
reactions: ["12C(16C,15B)X"]
experiments: []
models: [shell-model, eikonal-reaction-model, Geant4]
observables: [knockout-cross-section, spectroscopic-factor, Rs, separation-energy, particle-identification]
methods: [single-nucleon-knockout, external-target-facility, trajectory-reconstruction, B-rho-deltaE-TOF]
tags: [degree-dissertation, 16c, knockout, spectroscopic-factor-reduction, ETF, eikonal]
---

# 孙亚洲 2019：`16C` 单质子敲出反应

## Bibliographic Record

孙亚洲，*16C 单质子敲出反应研究*，中国科学院近代物理研究所博士学位论文，2019，PDF 116 页。原始文件 SHA-256 为 `d9d900cfdd783890f2f5d774b18832bbfda40eeb2af2db50b353ac18373496c0`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 题名页、中英文摘要和目录（PDF pp.I–VI）；壳模型、程函理论、谱因子与 `R_s` 研究动机（pp.1–20）；HIRFL-CSR/RIBLL2 外靶终端、探测器、电子学和数据格式（pp.21–48）；径迹重建、粒子鉴别、Geant4 比较和分析软件（pp.49–68）；截面归一化、效率、几何修正、误差和结果讨论（pp.69–98）；总结与展望（pp.99–106）。关键视觉页面 PDF pp.1、4、21、46、79、109 已核对。
- Not covered: 75 和 400 MeV/u 文献实验的原始数据/代码、所有 Geant4 输入逐项复现、事件级树和参考文献逐篇回读。
- Coverage caveats: `R_s` 是实验谱因子与理论谱因子的比值，跨能量比较受壳模型、eikonal reaction model、末态选择和效率修正共同影响；论文没有给出独立于这些模型约定的谱因子。

## Paper Question and Scientific Motivation

论文以深束缚质子敲出为背景，利用 `16C` 的 `ΔS≈18.3 MeV` 价质子，补充已有 75 与 400 MeV/u 数据，检验谱因子衰减因子 `R_s` 是否具有反应能量依赖（摘要、PDF pp.1–20）。

## Method and Design Logic

实验在 HIRFL-CSR 的 RIBLL2 与 External Target Facility（ETF）进行：`18O` 在 CSRm 加速、经 15 mm Be 初级靶产生次级 `16C`，次级束约 240 MeV/u 轰击 5 mm C 靶；靶前/靶后飞行时间、能损、漂移室和磁刚度用于束流/残余核识别。论文以 `12C(16C,15B)X` 的单举截面结合效率、几何接受度和靶厚度修正，比较 `R_s` 的能量趋势（PDF pp.21–48、69–98）。

## Key Evidence and Reasoning Chain

1. ETF 轨迹和粒子鉴别 → 选择 `16C` 入射束与 `15B` 残余核（PDF pp.49–68、71–90）。
2. 反应产额、束流计数、靶厚度、探测效率和几何效率 → 得到单质子敲出截面（pp.69–98）。
3. 240 MeV/u 截面与 75、400 MeV/u 文献点比较 → 在论文给出的误差范围内未见明确 `R_s` 能量依赖（摘要、PDF pp.90–98、99–100）。
4. shell-model/eikonal framework → 解释 `R_s` 与分离能的比较边界，而不是直接测量核内谱因子。

## Summary

论文报告 `12C(16C,15B)X` 截面为 `15.9(2.1) mb`。与 75 和 400 MeV/u 已有截面数据结合，作者在误差范围内未发现谱因子衰减的明显反应能量依赖。论文同时提供 ETF 的轨迹重建、粒子鉴别和截面归一化流程；这些方法细节是可迁移的实验设计知识，但 `R_s` 的数值解释仍依赖反应模型、壳模型和跨实验归一化的一致性。

## Experimental or Theoretical Setup

- Beam/target: 240 MeV/u secondary `16C` on 5 mm carbon target at HIRFL-CSR RIBLL2/ETF。
- Reaction: `12C(16C,15B)X` single-proton knockout。
- Detector chain: TOF, drift chambers, multi-sampling ionization chamber, magnetic analysis and particle-ID electronics。
- Theory: shell-model spectroscopic factors and eikonal single-particle cross sections; Geant4 used for detector/trajectory evaluation。

## Key Results

| issue_id | priority | core_claim | claim_kind | evidence_level | source_independence | locator | research_status | stage_conclusion | knowledge_increment | remaining_uncertainty | next_autonomous_route | needs_review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DD-20260910-16C-01 | P0 | 240 MeV/u `16C` 在 ETF 上进行 `12C(16C,15B)X` 单质子敲出，论文得到反应截面 `15.9(2.1) mb`。 | experimental-fact | direct | single | PDF 摘要 pp.I–IV、pp.69–98、结论 pp.99–100 | completed | 实验反应、装置和截面提取链已从正文和视觉页面核对。 | 新知识 | 事件级残余核门和效率/接受度协方差未重算。 | 回读截面表、束流归一化和几何效率代码，检查系统误差传播。 | true |
| DD-20260910-16C-02 | P0 | 将 240 MeV/u 截面与 75、400 MeV/u 文献数据比较时，在论文误差范围内未见明确 `R_s` 反应能量依赖。 | experimental-comparison + author-interpretation | indirect | multiple, cross-experiment | PDF 摘要、pp.90–98、99–100 | partially-researched | 阶段结论是“该数据点不显示显著能量趋势”，不是证明能量依赖不存在。 | 边界/失败知识 | 低/高能数据的靶材、末态门、模型和系统误差尚未统一重算。 | 建立 75/240/400 MeV/u provenance table，按同一 eikonal/壳模型约定做敏感性比较。 | true |
| DD-20260910-16C-03 | P1 | ETF 通过靶前/靶后 TOF、能损、径迹和磁刚度重建选择 `16C` 与 `15B`，并以效率、几何和靶厚度修正截面。 | method-result | direct | single | PDF pp.21–68、69–90 | completed | 可复用为中能放射性束流敲出实验的分析流程，但不等于独立物理结论。 | 总结知识 | 轨迹模型、探测器效率和粒子污染的逐事件影响未全部公开。 | 以空靶/随机门和独立 Monte Carlo 检查粒子污染与接受度。 | true |
| DD-20260910-16C-04 | P1 | `R_s` 的能量趋势比较同时依赖壳模型谱因子和 eikonal 单粒子截面；三体/短程关联、模型截断和反应机制不能由本论文单独分离。 | model-result + limitation | indirect | single | PDF pp.1–20、69–98 | stopped | 反应能量结论的模型依赖已识别，但没有足够独立输入完成归因。 | 边界/失败知识 | 没有多模型绝对截面重算、公开事件数据和统一误差协方差。 | 取得 75/400 MeV/u 原始文献与模型输入后，做多模型敏感性和负例比较；当前无 L4 manifest。 | true |

## Nuclear Structure Information

本来源主要是反应和单粒子结构信息，不建立完整 `16C`/`15B` 能级页。论文指出直接敲出主要关联 `16C` 的 `0p3/2` 质子空穴，并讨论 `15B` 基态及低激发态的末态选择（PDF pp.69–90）；这些为作者的反应模型解释，不应写成独立波函数测量。

## Authors' Interpretation

作者把 `15.9(2.1) mb` 与已有能量数据的比较解释为没有明显的 `R_s` 能量依赖，并将结果视为对高能程函近似适用性的补充约束。该结论是基于跨实验和模型约定的作者解释。

## Model Results

壳模型提供谱因子，eikonal calculation 提供单粒子敲出截面，Geant4 评估轨迹/粒子鉴别。模型输出用于构造 `R_s`，不是实验直接观测量；模型截断、有效相互作用和 reaction inputs 需要保留。

## Competing Interpretations and Limitations

- 没有观察到显著能量依赖可能意味着趋势小于当前不确定度，也可能被跨实验系统误差、末态污染或模型差异掩盖。
- `R_s` 的分离能系统学不能简单归因于单一短程关联或 eikonal approximation failure。
- 240 MeV/u 只有一个截面点，不能替代同一装置、同一末态定义的能量扫描。
- 本论文的 ETF 方法和相关数字 DAQ 与其它 HIRFL source 有方法依赖，但不构成独立核结构实验重复。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-16C-1 | Core reconstruction | 论文把中能放射性束流终端、末态选择和截面归一化连接成一条可复用的 `R_s` evidence chain。 | DD-20260910-16C-01–04；PDF pp.21–100 | unreviewed |
| AR-16C-2 | Transfer conditions | 只有在束流能量、靶材、末态门、接受度、效率和 shell/eikonal inputs 可比时，跨能量 `R_s` 才能排序。 | PDF pp.69–98 | unreviewed |
| AR-16C-3 | Reverse/falsification test | 同一分析流程下的多能量数据或统一模型重算若出现系统趋势，将改变“无能量依赖”的阶段判断。 | DD-20260910-16C-02/04 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 ETF/RDT、数字 DAQ 和核结构 source，但没有 `16C` 深束缚质子敲出及 `R_s` 能量比较的 thesis locator。
- Effect of this source: `supports` 方法边界并 `extends` 跨质量区反应知识，`limits` 对 `R_s` 能量趋势的强解释。
- Reason: 提供一个中高能单质子敲出数据点和完整 ETF 分析链，同时保留模型/跨实验限制。
- Persistence decision: source-only；当前不新建 `16C`/`15B` 正式实体页。
- Review state: `unreviewed`，all claims retain `needs_review: true`。

## Related Knowledge and Project Relations

| relation_type | target | specific_relation |
|---|---|---|
| methodological-bridge | [[zhou-houbing-2012-101pd-rdt-thesis]] | 共享中能束流终端的轨迹、粒子鉴别和 RDT/反应分析方法背景，但不是同一实验。 |
| methodological-bridge | [[wu-hongyi-2020-general-purpose-digital-daq-thesis]] | ETF 电子学/数据获取与数字 DAQ 方法之间的工程桥接。 |
| limits | 程函反应模型（eikonal reaction model；当前未建立独立模型页） | `R_s` 解释不能脱离程函近似和波函数输入。 |

## Human Review Triage

### P0

- `DD-20260910-16C-01`：PDF 摘要、pp.69–100；核对 240 MeV/u 反应、15.9(2.1) mb 和归一化定义。
- `DD-20260910-16C-02`：PDF pp.90–100；核对 75/240/400 MeV/u 比较是否被误写为“没有任何能量依赖”。

### P1

- `DD-20260910-16C-03/04`：PDF pp.21–98；核对效率、几何修正、模型输入和未分离的反应机制系统误差。

### P2/P3

软件架构、参考文献和未参与结果的 ETF 设备细节留待复算需求时抽查。

## Extracted Pages

- Nuclei: no formal page created; `16C`/`15B` remain source-local。
- Bands: none。
- Concepts: spectroscopic-factor reduction remains source-local。
- Methods: ETF trajectory reconstruction, PID, efficiency and knockout cross-section extraction。

## Non-source Notes and Follow-up

PDF 题名/摘要、方法章节、结果章节和结论已实际读取，关键视觉快照包括 p1/p4/p21/p46/p79/p109。OCR 用于检索，数值以原页为准。未修改 raw、BibTeX 或外部实验数据。
