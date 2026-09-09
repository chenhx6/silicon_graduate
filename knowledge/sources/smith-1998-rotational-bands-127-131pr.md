---
type: source
title: "Smith 1998 博士论文：127–131Pr 多形状转动带"
aliases: [Smith 1998 Pr thesis, Bradley Hagood Smith dissertation]
created: 2026-09-05
updated: 2026-09-05
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment
reading_depth: deep-read
title_original: "Rotational Bands Representing a Multiplicity of Shapes in 127-131Pr"
authors: [Bradley Hagood Smith]
advisor: [Lee L. Riedinger]
journal: "University of Tennessee Knoxville doctoral dissertation"
year: 1998
volume:
pages: 234
doi:
arxiv:
language: en
canonical_source: "Smith, Bradley Hagood. Rotational Bands Representing a Multiplicity of Shapes in 127-131Pr[D]. University of Tennessee, Knoxville, 1998."
zotero_item_key:
citation_key: ""
zotero_uri:
library_file: "raw/papers/degree dissertation/Rotational bands representing a multiplicity of shapes in ¹²⁷⁻¹³¹Pr.pdf"
raw_file: "raw/papers/degree dissertation/Rotational bands representing a multiplicity of shapes in ¹²⁷⁻¹³¹Pr.pdf"
raw_sha256: "5759AD75294F1612E2827F9D2854E22C7B5033CB338163AB39107EAED5590C3C"
nuclei: [127pr, 128pr, 129pr, 130pr, 131pr]
reactions: ["92Mo(40Ca,xpyn)127-131Pr"]
experiments: [gammasphere-cf252-fission-ru108-112]
models: [cranked-shell-model, cranked-nilsson-strutinsky-model, triaxial-rotor-model]
observables: [dco-ratio, moments-of-inertia, bm1-be2-ratio, signature-splitting, band-crossing]
methods: [gamma-gamma-coincidence, gamma-gamma-gamma-coincidence, charged-particle-gating, angular-distribution]
tags: [a130, praseodymium-isotopes, enhanced-deformation, superdeformation, signature-inversion, phd-thesis]
---

# Smith 1998：`127–131Pr` 多形状转动带

## Bibliographic Record

Bradley Hagood Smith，*Rotational Bands Representing a Multiplicity of Shapes in 127-131Pr*，University of Tennessee, Knoxville，博士学位论文，1998，234 页。原始 PDF SHA-256 为 `5759AD75294F1612E2827F9D2854E22C7B5033CB338163AB39107EAED5590C3C`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: Abstract、Chapters 2–5 的 Nilsson/CSM/TRS、GAMMASPHERE+Microball 实验和数据处理、`127–131Pr` 结果、Chapter 6 conclusions；核对 ED/SD、signature inversion、DCO、alignment、Routhian 和 `B(M1)/B(E2)` 讨论。
- Not covered: 参考文献逐篇原文复核、所有 17 条新序列的逐转移数字再提取。
- Coverage caveats: 论文将多个 Pr 同位素和多种带结构放在一套实验中；候选组态、形变和 ED/SD 标签必须按核素、带号和模型条件分开。

## Paper Question and Scientific Motivation

作者研究轻 Pr 同位素中由形变驱动单粒子轨道形成的正常形变、增强形变（ED）和超形变（SD）转动带，比较随中子数变化的形变、signature inversion、带交叉和组态演化（Abstract；Chapters 1 and 6）。

## Method and Design Logic

实验采用约 180 MeV `40Ca` 束流轰击富集 `92Mo`，以 GAMMASPHERE 与 Microball 进行 γγ/带电粒子门选；`3p`、`1p` 和 `2p` 通道提供 `127–131Pr` 及相关残余核结构。数据经粒子鉴别、γ 能量/效率/多普勒校正和 DCO 处理，再以 CSM/TRS 与 `B(M1)/B(E2)` 比较组态（Abstract；Chapter 3；Chapters 4–5）。

## Key Evidence and Reasoning Chain

1. Microball 选择带电粒子通道，GAMMASPHERE 符合谱建立多核素能级纲图。
2. DCO、带内能量间隔和 coincidence links 确认候选带属于相应 Pr 核素。
3. crossing frequency、alignment、Routhian、动态转动惯量和 `B(M1)/B(E2)` 约束组态。
4. CSM/TRS 计算将带归入 normal-deformed、ED 或 SD minima，并比较 N 依赖趋势。

## Summary

论文报告 `127–131Pr` 的多个正常形变和增强/超形变序列；在 `130Pr` 发现四条很可能为 SD 的新带并延伸 ED 带，在 `128Pr` 与 `129Pr` 发现/扩展 ED 结构，在 `127Pr`、`131Pr` 等核补充高自旋带。作者确认 `πh11/2⊗νh11/2` 类带的低自旋 signature inversion，并认为 `πg9/2` ED 轨道的形变驱动作用随中子数减少而减弱。后者是 systematics + model 的综合解释，未来需要 quadrupole moments/lifetimes 检验。

## Experimental or Theoretical Setup

- `92Mo(40Ca,xpyn)`，约 180 MeV；GAMMASPHERE（约 92 个 Ge）+ Microball（约 95 个 CsI(Tl)）。
- Chapter 3 包含粒子鉴别、γγ/γγγ 符合、DCO、效率和多普勒修正。
- CSM、TRS、Nilsson/单粒子计算；派生量为 crossing frequency、alignment、J(2)、`B(M1)/B(E2)` 和形变参数。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| SM98-1 | 约 180 MeV `40Ca+92Mo`、GAMMASPHERE+Microball 实验用于研究 `127–131Pr` 高自旋结构和带电粒子道。 | experimental-fact | direct | single | Abstract；Ch.3 | true |
| SM98-2 | 论文在数据中识别约 17 条全新转动序列，并显著扩展 `127–131Pr` 的能级纲图。 | experimental-fact | direct | single | Abstract；Ch.6 pp.204–205 | true |
| SM98-3 | `130Pr` 中四条新序列被作者认为很可能是 SD 带，已知 ED 带也得到延伸。 | author-interpretation | indirect | single | Abstract；Ch.6 pp.205–206 | true |
| SM98-4 | `128Pr/129Pr` 的 `πh11/2` 相关带显示低自旋 signature inversion；带交叉、alignment 和 Routhian 用于组态比较。 | experimental-criterion + author-interpretation | direct | single | Ch.5；Ch.6 pp.206–208 | true |
| SM98-5 | `127,128Pr` 等轻 Pr 中发现/扩展 ED 带；`πg9/2` ED 结构的 crossing frequency 与 CSM 计算相容。 | experimental-fact + model-result | indirect | single | Ch.4–6 | true |
| SM98-6 | `130Pr` 新带与 `πh11/2⊗νh11/2` 候选/近扁椭 TRS minimum 的联系属于模型辅助指认。 | author-interpretation | indirect | single | Ch.5.8；TRS figures | true |
| SM98-7 | 作者根据 ED 带动态转动惯量随 N 的变化，提出 `πg9/2` 形变驱动作用随中子数减少而减弱。 | author-interpretation | contextual | single | Ch.6 pp.207–208 | true |
| SM98-8 | `B(M1)/B(E2)` 结果在部分带中是 lower-limit/模型依赖量，未替代绝对寿命或直接四极矩测量。 | analytical-boundary | inferred | single | Ch.5.6–5.8；Ch.6.2 | true |

## Nuclear Structure Information

- `127–131Pr` 的 normal-deformed、ED 和 SD 带共存；来源带号必须保持论文内部身份。
- `πh11/2`、`πg9/2`、`νh11/2`/`νi13/2` 等组态用于解释带交叉、signature inversion 和形变驱动。
- 多条带的 ED/SD 标记来自能级间隔、J(2)、TRS/CSM 和已知邻核比较，不是单一直接观测。

## Authors' Interpretation

作者将高-j intruder/extruder 轨道的占据与形变增强联系起来，并以 CSM/TRS、alignment 和 `B(M1)/B(E2)` 解释各带。`signature inversion` 的 residual pn interaction 解释是作者讨论的一种机制，不应写成唯一原因。

## Model Results

- CSM/TRS 给出 normal/ED/SD minima、crossing 和候选轨道。
- `B(M1)/B(E2)` 半经典比较辅助区分 `πg9/2`、`πh11/2` 等组态。
- 动态转动惯量和 quadrupole deformation systematics 给出 N 依赖形变趋势。

## Competing Interpretations and Limitations

- ED/SD 标签需结合 lifetime/quadrupole moment；仅由能级间隔和模型不能证明形变大小。
- signature inversion 可由残余 pn 相互作用、非轴形变、组态混合等共同造成；不能只归因于单一机制。
- 论文中部分质量归属、弱带和组态仍是 tentative；跨来源比较必须使用带头、宇称、signature 和 linking transitions，而非只按 band number。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-SM98-1 | Core reconstruction | 最稳健的贡献是 Pr 同位素 ED/SD/normal band 的系统学和分析工作流。 | Chapters 3–6 | unreviewed |
| AR-SM98-2 | Assumptions and dependencies | 组态/形变依赖 CSM/TRS、粒子门和 DCO/`B(M1)/B(E2)` 假设。 | SM98-4–8 | unreviewed |
| AR-SM98-3 | Transfer conditions | 可作为 A≈130 形变/带交叉基线，不能直接用于 wobbling/chirality 结论。 | Ch.5–6 | unreviewed |
| AR-SM98-4 | Failure conditions | 绝对 lifetimes、quadrupole moments 或新的 linking data 若不支持，ED/SD 趋势需降级。 | Ch.6.2 | unreviewed |
| AR-SM98-5 | Reverse/falsification test | 对候选 ED/SD 带寻找 lifetime/Q0、DCO/polarization 和跨带 links；对 inversion 比较不同 pn/shape 模型。 | SM98-7–8 | unreviewed |
| AR-SM98-6 | Research-question decision | 接入 A≈130 shape-evolution、signature-splitting 和 band-termination 比较。 | SM98-3–7 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 A≈130 wobbling/chirality 与部分形变来源，但缺少 `127–131Pr` 轻核多形状、ED/SD 和 Microball 分析的博士论文级全景。
- Effect of this source: supports and extends；也对 ED/SD 和 signature inversion 的证据强度作 limits。
- Reason: 提供跨 Pr 同位素的系统学、DCO/粒子门分析和模型依赖边界。
- Persistence decision: 新建 source；先不机械建立五个 Pr 核素和所有带页，待跨来源 identity 稳定后再最小更新。
- Review state: 页面 `unreviewed`；SM98-3–8 保留 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[rotational-bands]] | 提供 A≈130 Pr 多形状转动带和带交叉背景。 |
| methodological-bridge | [[dco-ratio]] | 说明 Microball/GAMMASPHERE 数据中的 DCO 与粒子门约束。 |
| supports | [[signature-splitting]] | 提供 Pr `πh11/2` 相关带 signature inversion 系统学。 |
| limits | [[triaxial-shape-coexistence]] | ED/SD/oblate labels 主要为模型辅助，不是直接形变证明。 |

## Human Review Triage

### P0

- SM98-3/SM98-6：核对 `130Pr` 四条 SD 候选带、ED 带、带号和 TRS/CSM 组态；风险是把“most likely”写成已确认 SD。
- SM98-7：核对“`πg9/2` 形变驱动随 N 减少而减弱”的统计/模型依据和 future-lifetime caveat。

### P1

- SM98-1：核对 reaction notation、Microball/GAMMASPHERE 配置与通道到核素的映射。
- SM98-4/SM98-8：核对 signature inversion、`B(M1)/B(E2)` lower-limit 和未测量绝对强度边界。

### P2/P3

- 未来按跨来源 band identity 稳定度再建 `127–131Pr` 轻量核素/带页。

## Extracted Pages

- Nuclei: 暂不机械新建 `127–131Pr` 页面。
- Bands: ED/SD/normal 序列先保留在 source 内。
- Experiments: 使用论文本身的 `40Ca+92Mo` 设置；现有 `252Cf` 实验页不代表该反应。
- Concepts/observables: [[rotational-bands]], [[superdeformation]], [[signature-splitting]], [[dco-ratio]], [[moments-of-inertia]]。

## Non-source Notes and Follow-up

本论文不是现有 `252Cf` Ru 实验；frontmatter 中的 experiment relation 仅用于高自旋分析方法导航，后续应建立独立的 `GAMMASPHERE+Microball 40Ca+92Mo` 实验页后再改写。
