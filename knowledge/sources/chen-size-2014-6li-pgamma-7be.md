---
type: source
title: "陈思泽 2014 博士论文：6Li(p,γ)7Be 低能截面"
aliases: [陈思泽2014博士论文, Chen Size 6Li p gamma 7Be thesis]
created: 2026-09-05
updated: 2026-09-05
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment
reading_depth: deep-read
title_original: "Experimental study of the low energy cross section of 6Li(p, gamma)7Be"
authors: [陈思泽]
advisor: [何建军]
journal: "University of Chinese Academy of Sciences doctoral dissertation"
year: 2014
volume:
pages: 88
doi:
arxiv:
language: zh
canonical_source: "陈思泽. 6Li(p,γ)7Be低能截面的实验研究[D]. 中国科学院大学/近代物理研究所, 2014."
zotero_item_key:
citation_key: ""
zotero_uri:
library_file: "raw/papers/degree dissertation/陈思泽.pdf"
raw_file: "raw/papers/degree dissertation/陈思泽.pdf"
raw_sha256: "3CFAB3B6DDED29F7EE9A6FA8C8EAB2E438AC4CE41A2C72F77DA714AB4D052ABD"
nuclei: [6li, 7be, 3he]
reactions: ["6Li(p,gamma)7Be", "6Li(p,alpha)3He"]
experiments: []
models: [r-matrix]
observables: [astrophysical-s-factor, reaction-cross-section, angular-distribution]
methods: [low-energy-nuclear-astrophysics, clover-gamma-detection, cross-section-measurement]
tags: [low-energy-reaction, nuclear-astrophysics, s-factor, 7be, phd-thesis]
---

# 陈思泽 2014：`6Li(p,γ)7Be` 低能截面

## Bibliographic Record

陈思泽，*6Li(p,γ)7Be 低能截面的实验研究*，中国科学院大学/近代物理研究所博士学位论文，2014，88 页。原始 PDF SHA-256 为 `3CFAB3B6DDED29F7EE9A6FA8C8EAB2E438AC4CE41A2C72F77DA714AB4D052ABD`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 摘要、目录、第一至六章；核对 320 kV 低能终端、能量/效率/宇宙线测试、`6Li(p,γ)7Be` 与 `6Li(p,α)3He` 相对测量、S-factor anomaly、R-matrix fit、`7Be` 3/2+ level proposal 和 astrophysical implication。
- Not covered: 全部引用文献原文、后续独立实验对新共振的验证。
- Coverage caveats: `195 keV` 共振及新 `7Be` level 是作者根据 S-factor structure 的候选解释，论文明确要求其它实验验证。

## Paper Question and Scientific Motivation

论文旨在建立低能核天体物理实验终端，并测量 `6Li(p,γ)7Be` 在 `Ep=70–300 keV` 的反应截面/天体物理 S 因子，检验低能反应模型与 `7Be` 产生相关的天体物理意义（摘要；第 1、3–6 章）。

## Method and Design Logic

在近物所 320 kV 高压平台搭建低能终端，测试束流能量、Clover γ 探测器效率和塑闪宇宙线抑制。由于靶中 `6Li` 含量难以绝对标定，实验同时测 `6Li(p,γ)7Be` 与 `6Li(p,α)3He` 产额，用已有 `(p,α)` 截面作相对归一化，再用 R-matrix 拟合 S-factor structure（第 3–5 章）。

## Key Evidence and Reasoning Chain

1. 终端测试给出能量精度、Clover efficiency 和 cosmic-ray veto 性能。
2. `(p,γ)` 与 `(p,α)` simultaneous yield ratio 得到相对 S factor。
3. 200 keV 附近的异常结构用 R-matrix resonance fit 描述。
4. 作者将拟合 resonance 关联到 `7Be` 候选 `Jπ=3/2+` level，并讨论其对 `6Li(p,α)` angular-distribution `a1` 的影响。
5. SUSY/Big-Bang calculation 评估低能 S-factor 下降对 `7Be` abundance 的影响。

## Summary

论文报告低能终端能量精度优于 `0.5 keV`，Clover 实验效率与 GEANT 模拟一致，塑闪抑制宇宙线本底有效。`6Li(p,γ)7Be` 相对测量在约 200 keV 出现类似共振峰结构；R-matrix 给出 `ER≈195 keV`、`Γp≈50 keV` 的候选共振，并提出 `7Be` 新 `3/2+` 激发态解释。该 level/resonance 仍是 provisional，需要低能散射或镜像核 `7Li` 实验验证；作者的天体物理模型估计低能 S-factor 下降不改变最终 `7Be` 丰度。

## Experimental or Theoretical Setup

- 320 kV platform；Clover γ detector、plastic scintillator cosmic veto。
- `Ep=70–300 keV`，`6Li(p,γ)7Be` 与 `6Li(p,α)3He` simultaneous relative measurement。
- R-matrix fit；astrophysical S factor、cross section、angular-distribution implication。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| CS14-1 | 320 kV 低能终端能量精度优于 `0.5 keV`，Clover efficiency 与 GEANT 模拟吻合，塑闪可显著抑制宇宙线本底。 | experimental-fact | direct | single | Abstract；Ch.3；Ch.6.1 | true |
| CS14-2 | `6Li(p,γ)7Be` 在 `Ep=70–300 keV` 的 S factor 通过与 `6Li(p,α)3He` 产额比进行相对测量。 | experimental-fact + method-formalism | direct | single | Abstract；Chs.4–5 | true |
| CS14-3 | 约 200 keV 处的 S-factor 数据显示类似共振峰结构，R-matrix fit 倾向 `ER≈195 keV`、`Γp≈50 keV`。 | experimental-fact + model-result | indirect | single | Ch.5；Ch.6.1 | true |
| CS14-4 | 作者将该结构解释为 `7Be` 候选 `Jπ=3/2+` 新能级，并联系 `6Li(p,α)3He` angular-distribution `a1` 系数问题。 | author-interpretation | indirect | single | Ch.5；Ch.6.1 | true |
| CS14-5 | 基于 Big-Bang/SUSY 模型，作者认为低能 S-factor 下降不会改变 `7Be` 最终丰度。 | model-result | contextual | single | Ch.5；Ch.6.1 | true |
| CS14-6 | 新共振/新能级需要 `6Li(p,p)6Li` 或镜像 `7Li` 等独立实验验证；当前相对测量受靶含量绝对标定限制。 | analytical-boundary | direct | single | Ch.6.2 pp.69–70 | true |

## Nuclear Structure Information

- `7Be`：低能反应拟合提出的 `3/2+` level candidate。
- `6Li`/`3He`：反应截面和 S-factor method context。

## Authors' Interpretation

作者将 200 keV 附近的结构解释为新 `7Be` resonance/level 候选，但明确要求其它实验佐证；天体物理影响来自模型计算。

## Model Results

- R-matrix：`ER≈195 keV`、`Γp≈50 keV` candidate fit。
- Big-Bang/SUSY model：`7Be` abundance sensitivity。

## Competing Interpretations and Limitations

- S-factor peak 可能来自 resonance、normalization/systematics 或未建模反应贡献；本 thesis 不提供独立 scattering proof。
- 相对测量依赖已有 `(p,α)` cross section 和靶含量假设，不能直接当作绝对 capture cross section。
- `7Be` spin-parity candidate 不能进入当前高自旋核结构 evidence pool。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-CS14-1 | Core reconstruction | 最稳健贡献是低能核反应终端及相对 S-factor measurement workflow。 | CS14-1–2 | unreviewed |
| AR-CS14-2 | Assumptions and dependencies | S factor 依赖 `(p,α)` reference、target composition、efficiency/beam-energy calibration 和 R-matrix model。 | CS14-2–6 | unreviewed |
| AR-CS14-3 | Transfer conditions | 可作低能 reaction/experimental-method source；不直接迁移到高自旋 γ spectroscopy。 | CS14-1–6 | unreviewed |
| AR-CS14-4 | Failure conditions | 独立散射/镜像核实验若不支持 195 keV resonance，level interpretation 需撤回。 | CS14-3–6 | unreviewed |
| AR-CS14-5 | Reverse/falsification test | 复核 target composition、absolute normalization、R-matrix alternatives、elastic-scattering and mirror-nucleus evidence。 | Ch.6.2 | unreviewed |
| AR-CS14-6 | Research-question decision | source-only；仅在低能核反应或实验终端方法问题中调用。 | CS14-1–6 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 主线是低能核结构 γ spectroscopy；尚无 `6Li(p,γ)7Be` source。
- Effect of this source: foundational-background/methodological bridge；不改变当前主线科学结论。
- Reason: 低能终端和相对截面方法具有实验复用价值，物理 resonance 仍为候选。
- Persistence decision: 新建 source；不新建正式 `7Be` level/band page。
- Review state: 页面 `unreviewed`；CS14-2–6 保留 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | 低能核反应实验方法 | 低能反应终端、效率和相对截面测量的通用方法背景；当前未建立泛化概念页。 |
| not-direct-evidence | [[rotational-bands]] | 不提供当前高自旋带结构证据。 |

## Human Review Triage

### P0

- CS14-3/CS14-4：核对 S-factor peak、R-matrix 参数和 `7Be` `3/2+` 候选措辞；风险是把 provisional resonance 写成已发现能级。
- CS14-2/CS14-6：核对相对归一化、靶含量限制和所需独立验证。

### P1

- CS14-1：核对 320 kV 终端测试指标、Clover efficiency 和 cosmic veto。
- CS14-5：核对 astrophysical model assumptions，不把模型结果写成实验事实。

### P2/P3

- source-only；不批量建立 `6Li/7Be` 页面。

## Extracted Pages

- Source-only；不新增正式核素/带页。
- Methods: 低能反应、效率和相对截面方法保留在 source 内。

## Non-source Notes and Follow-up

该论文与当前 A≈130 高自旋主题距离较远，但其低能终端和相对测量方法具有有限方法学复用价值。
