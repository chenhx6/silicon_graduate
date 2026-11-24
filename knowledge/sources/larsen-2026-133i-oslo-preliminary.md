---
type: source
title: "Larsen 2026 Oslo-method presentation: preliminary 132,133I OCL experiments"
aliases: [Larsen 2026 133I Oslo preliminary, 133I OCL 24 MeV alpha experiment]
created: 2026-11-01
archive_required: true
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: instrument-and-experiment-presentation
reading_depth: skimmed
title_original: "The Oslo method for nuclear-model ingredients: Recent results and applications"
authors: ["Ann-Cecilie Larsen"]
year: 2026
pages: "presentation pp.32-33"
language: en
canonical_source: "https://indico.ijclab.in2p3.fr/event/11675/contributions/39737/attachments/27303/40663/talk_Larsen_PND2-3_Paris_2026.pdf"
source_url: "https://indico.ijclab.in2p3.fr/event/11675/contributions/39737/attachments/27303/40663/talk_Larsen_PND2-3_Paris_2026.pdf"
citation_key: larsen_2026_133i_oslo_preliminary
raw_file: "raw/papers/gpt/learning-daily/20261101-day29-133i-oc/larsen-oslo-method-133i-2026.pdf"
raw_sha256: "633e2470366fa782bc38841e078be40bb031c8635f21079a3ce4236f76808458"
raw_storage_status: verified-public-web-archive
source_independence: dependent-public-presentation-same-ocl-experiment
nuclei: [132i, 133i]
reactions: [130te-alpha-p-gamma-133i, 130te-alpha-d-gamma-132i]
experiments: [ocl-siri-oscar]
models: [oslo-method, talys]
observables: [gamma-strength-function, nuclear-level-density, neutron-capture-rate]
methods: [particle-gamma-coincidence, oslo-method]
tags: [133i, ocl, oslo-method, preliminary, gamma-strength-function, data-readiness]
---

# Larsen 2026：`133I` OCL preliminary analysis boundary

## Bibliographic Record

This 61-page presentation by Ann-Cecilie Larsen was archived from a public conference
attachment on 2026-11-01. The declared PDF hash matches the local raw file. It is a
public presentation dependent on the OCL `132,133I` experiment, not an independent
measurement and not a substitute for the final thesis or event-level analysis package.

## Scope and Reading Depth

The presentation was targeted-read for the `132,133I` experiment slides and the Oslo
method context. The full thesis, γSF numerical tables, raw event data, producer,
response matrices and covariance were not obtained.

## Research Question and Scientific Motivation

The relevant question is whether the existing OCL acquisition can support an independent
γSF/NLD and neutron-capture-rate analysis for `133I`, including a low-energy enhancement
and its electromagnetic character.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LAR26-1 | The presentation identifies `132,133I` OCL experiments in fall 2025; for `133I` it gives `130Te(α,pγ)133I` with `Eα=24 MeV`, using the Oslo method for indirect `(n,γ)` cross-section/rate inputs. | experiment-method | direct-presentation | PDF pp.32–33 | true |
| LAR26-2 | The same slides label the analysis `PRELIMINARY` and state that only a few data files had been sorted; the slides do not report a final γSF, LEE, M1/E1 decomposition, event-level response or covariance. | readiness-boundary | direct-presentation | PDF pp.32–33 | true |

## Summary

This presentation upgrades the `133I` route from a generic public experiment record to a
dated, concrete but preliminary OCL acquisition. It does not close the physics result.

## Extracted Pages

- PDF pp.32–33: `132,133I` fall-2025 OCL experiment, `130Te(α,pγ)133I`,
  `Eα=24 MeV`, preliminary status and limited data sorting.

## Competing Interpretations and Limitations

Any future low-energy enhancement may be physical or may reflect incomplete sorting,
threshold/summing response, unfolding, NLD/spin assumptions or non-statistical feeding.
The presentation does not provide enough information to rank these explanations.

## Knowledge Impact and Learning Decision

`supports`: prioritize obtaining the existing OCL producer, thesis and response package
before proposing a nominally duplicate new beam.

`limits`: preliminary slides cannot support a measured `133I` γSF, LEE, PDR or M1 claim.

## Human Review

This page is a Codex self-audit, remains `unreviewed`, and does not set
`human-reviewed`.


## 2026-11-22 — 报告全文与初步强度图

61 页报告分为背景与装置（PDF 1–14）、方法和不同质量区案例（15–31）、碘与间接反应率案例（32–40）、总结（41–44）、技术备份（45–61）。图像页已回看，含 PDF 15 的 raw / unfolded / primary 顺序、PDF 24–26 的 Sn 引文、PDF 34–40 的 β-Oslo 论文与法国装置案例、PDF 60 的 70Ni 响应。这里记录方法与所引证据的关系，具体反应率应回到各一次文献。

PDF 32 是只排序少量数据的 \(E_x\)–\(E_\gamma\) 符合图。PDF 33 另绘 132I、133I 的初步 γ 强度点与曲线，标记为 **PRELIMINARY**。图提供初步形状信息，未提供可独立核实的数值表、归一化细节或最终分量分解。特别是 133I 的低能端行为仍须回查完整分析及不确定度，Grieg 论文正文尚缺。

PDF 46 从展开谱扣除后继级联提初代分布。PDF 48 的 56Fe 示例为 2052 个数据点和 184 个自由参数，通常安排约 10–20 次迭代、可在 4–5 次已收敛。PDF 49 提出 \(P(E_i,E_\gamma)\propto\rho(E_i-E_\gamma)\mathcal T(E_\gamma)\)。PDF 52 的 \(A,B,\alpha\) 变换保留逐行归一的拟合矩阵，PDF 53–54 说明已知能级、共振间距与平均辐射宽度的常规刻度，PDF 52 同时指出 Shape method 可约束斜率。PDF 57–58 的 51Ti 对照在终态自旋范围几乎相同的条件下比较两路结果，不能直接外推任意反应的布居窗口。
