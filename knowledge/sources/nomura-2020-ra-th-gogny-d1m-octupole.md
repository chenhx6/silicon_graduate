---
type: source
title: "Octupole correlations in light actinides from the interacting boson model based on the Gogny energy density functional"
aliases: [nomura-2020-ra-th-gogny-d1m-octupole]
created: 2026-10-29
updated: 2026-11-22
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Octupole correlations in light actinides from the interacting boson model based on the Gogny energy density functional"
authors: ["K. Nomura", "R. Rodríguez-Guzmán", "Y. M. Humadi", "L. M. Robledo", "J. E. García-Ramos"]
year: 2020
journal: "Phys. Rev. C"
volume: "102"
pages: "064326"
doi: "10.1103/PhysRevC.102.064326"
citation_key: "nomura_2020_ra-octupole-correlations"
canonical_source: "Phys. Rev. C 102, 064326 (2020); arXiv:2008.08870v2"
source_url: "https://arxiv.org/abs/2008.08870v2"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/2020-nomura-ra-th-d1m.pdf"
raw_storage_status: raw-pdf-archived
raw_sha256: "c22d0422bcfb86d3f4e24a7f2012de8d6eadecec0ff264826c62d3eb44d3d4ec"
nuclei: [Ra, Th]
observables: [potential-energy-surface, octupole-deformation, excitation-energy, E1, E2, E3]
methods: [Gogny-HFB, mapped-sdf-IBM]
tags: [octupole, double-well, mean-field, model-boundary]
---

# Octupole correlations in light actinides from the interacting boson model based on the Gogny energy density functional

## Bibliographic Record

arXiv API提供的题名、作者和DOI与实际PDF首页相符；期刊卷页由API记录或DOI字段所指书目信息记录。取得2008.08870v2预印本，15页、2022542 bytes，已归档至 `raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/2020-nomura-ra-th-d1m.pdf`。

## Summary

本工作基于 Gogny D1M 势能面微观映射的相互作用玻色子模型（sdf-IBM）研究轻锕系核（Ra 与 Th 同位素）的八极关联。确立 224Ra 与 226Th 处于八极关联最显著极值，而轻端 220Th 保持近球形软八极特征，指出八极势垒存在强核素依赖。

## Scope and Reading Depth

阅读全文 arXiv v2 PDF1–15。PDF1–3涵盖轴对称 D1M-HFB 约束及 Fig. 1，PDF4–6建立相干态映射并给出映射参数，PDF7–10对比能谱、宇称劈裂及 E1–E3，PDF11–13给出跃迁率、部分能级纲图和约化矩阵元，PDF14–15为参考文献。图点和势垒未数字化。期刊书目信息与实际阅读版本分别记录。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NO20-1 | D1M 泛函势能面表明 220Ra 与 222Th 在 beta3~0.1 出现局域极小，最强八极形变汇聚于 224Ra 与 226Th (beta3~0.15)。 | model-result | derived | PDF p.2, Fig. 1 on p.3 | true |
| NO20-2 | 在该计算中，220Th 近球形且沿 beta3 较软，限制了在同一模型中对整条同位素链采用深势垒双阱近似。 | model-analysis | derived | PDF pp.2–3 | true |
| NO20-3 | 作者用质子 \(i_{13/2}\!-\!f_{7/2}\) 与中子 \(j_{15/2}\!-\!g_{9/2}\) 的轨道耦合解释该区域的八极驱动。 | author-interpretation | model-based | PDF p.3, Sec. II | true |
| NO20-4 | \(sdf\)-IBM 相干态能量映射主要约束 Gogny-D1M 势能面的极小值邻域。远离极小值的玻色子势能面明显偏平，作者将此联系到有限价空间。 | model-method | model-based | PDF pp.4–6, Eqs. (3)–(9), Figs. 1–2 | true |
| NO20-5 | E2、E3 玻色子有效电荷取 HFB 极小值上的内禀矩并作经验缩放，\(s_1=1.55/(9.3-0.3N_B)\) 和 \(s_2=0.33\)。E1 另取 \(e_B^{(1)}=0.0277\,e\,\mathrm b^{1/2}\) 以复现 222Ra 的 \(B(E1;1_1^-\!\to0_1^+)\)。 | model-calibration | calibrated | PDF pp.9–10, Eqs. (14)–(16) and text | true |
| NO20-6 | 224Ra D1M 映射结果的 \(B(E3;3_1^-\!\to0_1^+)\) 为 50 W.u.，表列实验为 42(3) W.u.。同表的 \(B(E3;1_1^-\!\to2_1^+)\) 为 86 对 210(40) W.u.。作者指出 224Ra 的 E1 值可偏高 \(10^2\) 至 \(10^3\) 倍。Fig. 10 中计算的部分 E3 矩阵元随自旋明显交错，已有数据趋势更平缓。 | model-to-data-comparison | model-and-cited-experiment | PDF pp.11–13, Table I and Fig. 10 | true |

## Competing Interpretations and Limitations

PES及极小值深度均为给定EDF与变分约束下的模型输出；既不是实验测得势垒，也不等于宇称劈裂。惯性、零点修正、投影与组态混合共同影响动力学；不能把坐标相同误认为不同模型结果已可逐点等价比较。

Fig. 10 的实验点来自 [[butler-2020-222-228ra-octupole-evolution]]（222Ra、228Ra）、[[gaffney-2013-pear-shaped-rn-ra]]（224Ra）和文中 Ref. [62]（226Ra）。与 [[nndc-ra-th-cluster-decay-adopted]] 比较时按其引用链对同源数据去重。分支、能级劈裂和多跃迁矩阵元各自约束不同的量。局域映射的形状与跃迁结果只覆盖价玻色子空间内的谱学问题，团簇发射势垒另需大振幅路径和隧穿计算。

## Knowledge Impact and Learning Decision

提供有locator的跨区势能面量级与直接反例，限制固定“锕系深/稀土浅”阈值及势垒到劈裂的直接反演。

## Extracted Pages

- [[actinide-lanthanide-doublewell-schiff-boundary]]

## Sources

- arXiv 2008.08870v2; DOI 10.1103/PhysRevC.102.064326。
