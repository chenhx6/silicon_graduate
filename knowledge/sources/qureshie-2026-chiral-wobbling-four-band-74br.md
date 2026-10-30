---
type: source
title: "Qureshie 等 2026：74Br 手征—摆动四带网络的 TPSM/PTR 预测"
aliases: [Qureshie 2026 74Br four bands, Novel chiral-wobbling excitation mode in atomic nuclei]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper
reading_depth: read
title_original: "Novel chiral-wobbling excitation mode in atomic nuclei"
authors: [Kouser Qureshie, S. P. Rouoof, J. A. Sheikh, Nazira Nazir, G. H. Bhat, S. Jehangir, N. A. Rather, R. J. Guo, S. Y. Wang, C. Liu, Q. B. Chen, S. Frauendorf]
year: 2026
arxiv: 2610.09808v2
doi: ""
canonical_source: https://arxiv.org/abs/2610.09808v2
citation_key: qureshie_2026_chiral_wobbling_74Br
raw_file: raw/papers/gpt/qureshie-2026-chiral-wobbling-74br-arxiv2610.09808v2.pdf
raw_sha256: 84d0bc2407a789e49aeacc7076e89ef49471dcb907570607ae0a573fdd3246cd
nuclei: [74br]
models: [triaxial-projected-shell-model, particle-triaxial-rotor]
observables: [energy-levels, bm1, be2, multipole-mixing-ratio]
methods: [angular-momentum-projection]
tags: [a80, chirality, wobbling, prediction, source-lineage]
---

# 74Br：从三个实验带到第四带预测

## Bibliographic Record

官方 Atom 条目与 PDF 首页面相符；v1 为 2026-10-07，所读 v2 为 2026-10-09。6 页，226515 bytes。获取与身份回执：`outputs/literature-acquisition/20261029-day27-qureshie2026-chiral-wobbling.json`。下载器输入的缩略题名和 incoming 目录名不是正式书目信息。所查条目未给 DOI；不据此宣称期刊版本不存在。

## Scope and Reading Depth

全文六页文字已读；视觉核对 PDF pp.3–4 的 Figs.1–8。未取得作者数值数组、TPSM/PTR 程序或完整参数文件；没有重放其求解器。SI 已按每日授权请求，但直接 PDF 路线不能完成 SI 发现，不把该结果写成“无 SI”。`reading_depth: read` 不代表计算可复现性已闭合。

## Paper Question and Method

本文对 [[guo-2024-chiral-wobbler-74br]] 的 B1–B3 解释作理论扩展：能否存在 B4，分别与 B3 构成手征配对、与 B2 构成摆动连接？采用配对加四极—四极相互作用的 TPSM，并与 PTR 比较。不是新增采集或独立寿命实验。

## Key Results

以下均保留 `needs_review: true`；直接读取只核验对应文字、图示与输入身份，不认证模式指认。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| QU26-1 | B1–B3实验数据来自Guo2024；B4是预测，未作为第四条已观测带给出。 | model-result | direct-model-and-data-lineage | PDF pp.1–2；p.3 Fig.1；p.5结论 | true |
| QU26-2 | TPSM取β=0.367、γ=27°；PTR取β=0.45、γ=27.5°，对照没有固定同一β。 | model-input-and-our-inference | direct-original | PDF p.2参数段 | true |
| QU26-3 | Eq.(1)含球形单粒子、QQ、单极/四极配对；GQ=0.18GM，GM参照奇偶质量差，χ由自洽关系设定。 | model-construction | direct-original | PDF p.2 Eq.(1)及上下文 | true |
| QU26-4 | E2取ep=1.5、en=0.5；M1用列出的轨道/自旋g因子，曲线不能直接迁移成他核实测强度。 | model-input-and-our-inference | direct-original | PDF p.3跃迁算符段 | true |
| QU26-5 | 作者将B1/B2、B3/B4组织为手征配对，B3/B1、B4/B2组织为摆动关系；是带间解释网络。 | author-interpretation | direct-to-source | PDF pp.4–5 Figs.5–8 | true |
| QU26-6 | Fig.7(c)的B4→B3 E2份额有交错且部分点超过50%；整体称M1主导需逐自旋边界。仅定性视觉读取，未数字化。 | figure-observation-and-our-inference | direct-figure | PDF p.4 Fig.7(c)及图下段落 | true |
| QU26-7 | Fig.8用PTR核芯RMS分量且横轴为其平方和开根号R。RMS不保留符号、相位或完整概率；不能据此唯一认证手征隧穿波函数。 | model-output-and-our-inference | direct-figure-and-conditional-reasoning | PDF p.4 Fig.8；p.5几何解释 | true |

## Competing Interpretations and Limitations

Guo2024 是已有实验入口；本文 TPSM/PTR 对同批谱学观测的描述不增加独立实验次数。B4 的双重关系仍可受到组态混合、signature partner 或其它取向激发解释的挑战。本文没有为这些替代解释给出共同输入下的排他性比较。

图中的实验点也没有给出可替代原实验 SI 的完整误差合同。定量再分析须回 Guo2024 Table I 的逐跃迁数值、上限和寿命谱系；不可从本文平滑曲线制造“新实测点”。

## Knowledge Impact and Learning Decision

`revises` [[multimodal-coexistence-and-phase-boundary-topology]]：原先按 β、γ 硬分箱生成的“互斥模式相图”不能认证真实核结构。本篇与 Guo2024 给出需要正面比较的同核多带模式网络，但理论预测不等于实验确证。关联 [[74br]]、[[chirality-wobbling-competition-evidence]]、[[chen-2016-two-dimensional-collective-chiral-wobbling]]。

可检验下一步：针对预测 B4，同时检验 B4→B3 和 B4→B2 的连线、同母态强度比及自旋交错。未见线只有在效率、门、背景及上限灵敏度已知时才构成条件反证；不以 B4 目前未观测直接否定该模型。

## Agent self-audit triage

- P0: none identified。来源身份、实际 raw 文件和哈希已核；未把预测提升为观测。
- P1：QU26-2 的模型输入差异；QU26-6 的逐自旋 E2 份额；QU26-7 的 RMS 信息丢失。作者代码、数组、完整误差与独立组态检验仍缺失。
- P2/P3：DOI/citation key 暂空，版本与 SI 检索范围如实保留。无新增 human-review 事件。


## Summary

本理论工作沿用74Br三带实验并预测第四带的双重带间关系。第四带、模型几何与电磁曲线保留为可检验预测。

## Extracted Pages

PDF1摘要与背景；PDF2 Hamiltonian/参数；PDF3 Figs.1–4；PDF4 Figs.5–8及逐线强度解释；PDF5结论与引用；PDF6引用。视觉覆盖PDF3–4；未读取作者数值程序或未发现的SI。
