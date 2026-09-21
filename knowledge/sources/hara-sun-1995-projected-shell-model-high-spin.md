---
type: source
title: "Projected Shell Model and High-Spin Spectroscopy"
aliases: ["Hara Sun 1995 PSM review", "Projected shell model high-spin review"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: review
reading_depth: deep-read
title_original: "PROJECTED SHELL MODEL AND HIGH-SPIN SPECTROSCOPY"
authors: ["Kenji Hara", "Yang Sun"]
journal: "International Journal of Modern Physics E"
year: 1995
volume: 4
issue: 4
pages: "637-785"
doi: "10.1142/S0218301395000250"
citation_key: HARA_1995
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
language: en
canonical_source: "Hara, K. & Sun, Y. Projected Shell Model and High-Spin Spectroscopy. Int. J. Mod. Phys. E 4, 637-785 (1995)."
library_file: "raw/papers/gpt/high-spin-20260920/review/1995_Hara_Sun_PROJECTED SHELL MODEL AND HIGH-SPIN SPECTROSCOPY.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/1995_Hara_Sun_PROJECTED SHELL MODEL AND HIGH-SPIN SPECTROSCOPY.pdf"
raw_sha256: "13ca9edbd3092d2d3c4612e9d22b7cb1ff740d07f0f97c5f139ac901a7b26dac"
nuclei: ["A≈130 doubly-odd nuclei", "rare-earth nuclei", "doubly-even nuclei", "odd-neutron nuclei", "odd-proton nuclei"]
models: ["projected-shell-model", "Nilsson-model", "BCS-pairing", "particle-rotor-model", "cranked-shell-model"]
observables: ["band-energies", "backbending", "signature-splitting", "signature-inversion", "g-factor", "B(E2)", "B(M1)", "alignment"]
methods: ["angular-momentum-projection", "configuration-mixing", "particle-number-projection", "band-diagram"]
tags: [projected-shell-model, high-spin-spectroscopy, angular-momentum-projection, signature-inversion, band-crossing, A130, rare-earth]
---

# Projected Shell Model and High-Spin Spectroscopy

## Bibliographic Record

- 作者：Kenji Hara、Yang Sun。
- 期刊：*International Journal of Modern Physics E* 4(4), 637-785 (1995)。DOI：`10.1142/S0218301395000250`。
- 原始文件：`raw/papers/gpt/high-spin-20260920/review/1995_Hara_Sun_PROJECTED SHELL MODEL AND HIGH-SPIN SPECTROSCOPY.pdf`；SHA-256：`13ca9edbd3092d2d3c4612e9d22b7cb1ff740d07f0f97c5f139ac901a7b26dac`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 149 页全文通过临时 OCR 副本逐页提取并按章节阅读；标题页、关键公式、代表性 band diagrams/level plots、章节开头/结论和 Appendix 结构做页面视觉核对。覆盖第 1-6 章：球形/形变壳模型动机、角动量投影、半经典极限、PSM Hamiltonian、decoupled motion、signature rule、two-qp high-K bands、band diagrams、doubly-even/doubly-odd/odd-mass applications、signature inversion/selfinversion、g-factor/M1/E2 以及技术附录。
- Not covered: 参考文献逐篇全文、原作者程序代码、每一幅图的原始数值提取。
- Coverage caveats: 原始 PDF 的页面文本层主要只有版权水印，OCR 存在公式/符号误识；本页保留模型结构和适用边界，论文级公式引用必须回到视觉页或可复制的原始版本。

## Paper Question and Scientific Motivation

- 综述问题：如何在重变形、高自旋核中以可解释且可计算的截断 shell-model 基底处理角动量、组态混合、带交叉、signature dependence 和电磁观测量（PDF pp.637-640）。
- 作者认为球形大空间 shell model 难以同时保留物理图像和计算可行性；PSM 以变形 Nilsson+BCS intrinsic states 为起点，再通过 angular-momentum projection 恢复旋转对称性，用少量物理相关组态描述高自旋谱学。

## Method and Design Logic

- 变形 intrinsic basis 通过 Nilsson Hamiltonian 和 BCS pairing 建立；projection operator `P^I_MK` 把 broken-rotational-symmetry states 投影到良好角动量。
- 配置混合在 projected basis 中进行，核心 Hamiltonian 为单粒子项、quadrupole-quadrupole、monopole pairing 和 quadrupole pairing：`H=H0−χQ·Q−G_M P†P−G_Q P_2†·P_2`（PDF §2.4，式 (2.40) 及后续定义）。
- 通过 Hill-Wheeler/generalized eigenvalue diagonalization 得到谱和 wave-function amplitudes；能谱、alignment、signature splitting、磁矩、B(E2)/B(M1) 与 band-crossing 可统一比较。
- PSM 的截断按物理相关准粒子组态进行；作者讨论 particle-number projection 的收益与在截断空间中的 spurious-state 风险。

## Key Evidence and Reasoning Chain

1. 角动量投影把 intrinsic Nilsson+BCS basis 转为 shell-model basis，并在数值上避免球形大空间的爆炸（PDF §§1-2）。
2. 半经典极限与 particle-rotor model 对应，说明 projected wave function 可提取 decoupling、K、signature 和 rotational alignment 图像（PDF §§2.2-2.3）。
3. 对 decoupled bands、two-quasiparticle high-K bands 和 band diagrams 的示例显示，PSM 能把 backbending、signature dependence 和 configuration crossing 放到统一的 projected basis 中（PDF §3）。
4. `A≈130` doubly-odd 应用把实验谱与 shape assumptions 比较，综述将 N=76/78 附近的 prolate→triaxial→oblate 过渡作为候选图景，但明确当时 axial code 无法直接证明 triaxial shape（PDF §5.1，Table 5）。
5. Odd-mass Er/Yb、odd-proton nuclei 和 rare-earth examples 展示 PSM 对 yrast/side bands、g-factors、B(E2)/B(M1)、signature inversion/selfinversion 的应用；高自旋趋势通常比单一低能级更能区分配置（PDF §§4-6）。
6. Review repeatedly separates successful numerical reproduction from physical interpretation: basis truncation, deformation, pairing, effective charges and omitted multi-quasiparticle configurations can change high-spin conclusions (PDF §§2.4, 4.3-4.4, 6，Appendix)。

## Summary

Hara 与 Sun 的综述建立了 PSM 的方法链：变形 Nilsson+BCS intrinsic states → angular-momentum projection → projected-basis configuration mixing → high-spin energies and electromagnetic observables. 综述通过大量 rare-earth、A≈130 doubly-odd、doubly-even 和 odd-mass examples 说明 PSM 如何处理 band crossings、signature effects、high-K bands、shape candidates、g-factors、M1/E2 和 γ/side bands。其长期可复用价值在模型结构和适用边界，而不是 1995 年具体数值或未经后续验证的形状分类。

## Experimental or Theoretical Setup

- Model inputs: deformation `ε`, Nilsson orbitals, pairing strengths, quadrupole interaction, selected multi-quasiparticle configurations。
- Projection: angular momentum; particle number optionally projected, with truncation/spurious-state caveats。
- Applications: doubly-even yrast/side bands, doubly-odd A≈130 shape and signature evolution, odd-neutron/odd-proton rare-earth bands, magnetic moments and E2/M1 transitions。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HS10-1 | PSM 用变形 Nilsson+BCS intrinsic basis、角动量投影和配置混合高效处理重变形核的高自旋谱。 | model-definition | direct | PDF §§1-2，式 (2.40) 及 projection equations | false |
| HS10-2 | PSM 的半经典极限与 particle-rotor picture 对应，可解释 decoupling、K 和 alignment。 | model-result/interpretation | direct | PDF §§2.2-2.3 | false |
| HS10-3 | PSM 示例覆盖 band crossing、signature splitting/inversion、two-qp high-K、g-factors、B(E2)/B(M1) 和 odd-mass/doubly-odd spectroscopy。 | review-synthesis | direct | PDF §§3-6 | false |
| HS10-4 | A≈130 doubly-odd application 曾依据 axial PSM 与实验不一致提出 N=76/78 附近三轴形状候选，但综述明确 axial code 不能直接证明 triaxiality。 | author-interpretation/review-summary | direct | PDF §5.1，Table 5 | true |
| HS10-5 | Particle-number projection 可改善部分 band-crossing agreement，但截断空间中的 spurious pair states 需要特别处理。 | method-limitation | direct | PDF §4.3，Figs.26-27 | false |

## Nuclear Structure Information

- 该来源是理论综述，不建立单一核素或能带页面。
- A≈130 内容与本 Wiki 的 `131Ce`/A≈130 collective-mode map 有历史方法关联，但具体 shape-transition 表格必须回到对应原始实验和后续 triaxial calculations。

## Authors' Interpretation

- PSM 的主要优势不是单纯计算速度，而是用物理相关 intrinsic configurations 保留高自旋结构解释；作者将其作为“可解释截断”的核心论点。
- 综述把 signature inversion、自洽形变、残余相互作用、组态混合和 angular-momentum alignment 视为互相耦合的问题，而非单一 universal mechanism。

## Model Results

- Hamiltonian 使用 schematic Q·Q + pairing interactions；deformation 通过自洽或经验输入确定，effective operators 用于 B(E2)/B(M1) 和 g-factor。
- 具体 nuclei 的 level agreement、shape assignment 和 transition rates 是 review 中的 model applications，不应脱离原始数据源升级为实验事实。

## Competing Interpretations and Limitations

- 轴对称 PSM 失败或偏差可以提示 triaxiality，也可能来自 basis truncation、遗漏 3/4-qp configurations、pairing/interaction 参数或实验 assignment；不能单独证明 shape。
- Particle-number projection 在截断空间可能引入/放大 spurious pair states；作者提出处理策略但不声称所有截断问题已消除。
- Doubly-odd level density 高、configuration weights 近简并，使预测对 shell filling 和 deformation assumptions 更敏感。
- 早期综述中的 model results 不能替代现代 CSM/TPSM/DFT 和直接 lifetime/polarization evidence。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-HS10-1 | Core reconstruction | PSM 将对称性破缺作为计算工具，再通过投影恢复物理对称性；configuration truncation 是物理解释而不是纯数值压缩。 | PDF §§1-2 | self-checking |
| AR-HS10-2 | Assumptions and dependencies | 结果依赖 intrinsic deformation、pairing、selected qp space、effective operators 和 particle-number treatment。 | PDF §§2.4,4.3-4.4 | self-checking |
| AR-HS10-3 | Transfer conditions | PSM 方法可迁移；1995 review 的特定 band/shape conclusion 只能作为历史背景，迁移需回原始 source 和现代 calculation。 | PDF §§3-6 | provisional |
| AR-HS10-4 | Failure conditions | 若更完整 basis、triaxial projection 或现代 interaction 改变 level ordering/shape inference，旧结论需修订。 | PDF §5.1，Appendix | active-L3 |
| AR-HS10-5 | Reverse/falsification test | 用相同 experimental dataset 比较 axial PSM、triaxial TPSM、CSM/DFT，并检查 B(E2), g-factor, signature and lifetime simultaneously。 | PDF §§4-6 | candidate-L3 |
| AR-HS10-6 | Research-question decision | 作为 TPSM/高自旋方法基础来源和 A≈130 shape-inference 的历史边界持久化；不单独启动 L4。 | PDF §§1-6 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 TPSM、triaxiality、signature-inversion、band-crossing 和 A≈130 collective-mode pages；该综述补足 PSM 的历史方法起点、投影公式、模型选择和截断边界。
- Effect of this source: `foundational-background` and `limits`。
- Reason: 来源为现有 TPSM/PSM pages 提供理论谱系，但其 1995 个案的 shape/level conclusions 必须与现代来源分开。
- Persistence decision: update [[triaxial-projected-shell-model]] with a historical source relation and PSM limitation note; no broad automatic rewrite of all project pages。
- Review state: `unreviewed`; review-level claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[triaxial-projected-shell-model]] | PSM 的 projection/configuration-mixing 历史方法基础。 |
| foundational-background | [[high-spin-phenomena]] | backbending、signature、alignment 和 high-K band 的统一理论背景。 |
| limits | [[gamma-soft-vs-gamma-rigid-diagnostics]] | 综述中的轴对称失败→triaxial 候选不能单独取代直接 γ-soft/γ-rigid evidence。 |

## Human Review Triage

### P0

- HS10-P0-1：综述级 PSM/shape claims 与原始实验/现代模型必须分层；不能把 `A≈130` Table 5 的形状分类写成直接实验事实。

### P1

- HS10-P1-1：公式 OCR 和图表符号需在论文写作引用时回到页面或正式可检索版本；本次 source page 只固化可稳定复核的框架。

### P2/P3

- 149 页 OCR 副本仅位于 `/tmp/hs010ocr.fNAshU/`，不进入仓库；原始 PDF 不改。

## Extracted Pages

- Nuclei: 不创建。
- Bands: 不创建。
- Concepts: PSM、angular-momentum projection、signature inversion、band crossing、configuration mixing。
- Models: [[triaxial-projected-shell-model]]。

## Non-source Notes and Follow-up

- 下一步：补充 HS10 到 TPSM model page 的历史来源关系，然后继续 HS-011；使用原始 PDF 与 OCR checkpoint，不把 OCR 文件作为永久证据。
