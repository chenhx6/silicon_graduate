---
type: source
title: 'Vaquero, Rodríguez & Egido 2013: 能量密度泛函中四极形变与配对涨落对无中微子双贝塔衰变核矩阵元的协同效应 (PRL 111, 142501)'
aliases: [Vaquero 2013 PRL 0nubb Shape Pairing, 'Phys. Rev. Lett. 111, 142501', 10.1103/PhysRevLett.111.142501, 'arXiv:1401.0650']
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: Shape and pairing fluctuations effects on neutrinoless double beta decay nuclear matrix elements
authors: [Nuria López Vaquero, Tomás R. Rodríguez, J. Luis Egido]
journal: Physical Review Letters
year: 2013
volume: 111
pages: '142501'
doi: 10.1103/PhysRevLett.111.142501
arxiv: 1401.0650v1
language: en
canonical_source: https://doi.org/10.1103/PhysRevLett.111.142501
zotero_item_key: ''
citation_key: ''
zotero_uri: ''
library_file: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G35/vaquero-2013-prl111-142501-shape-pairing.pdf
raw_sha256: 9069f66dd9ca177b816a606475e0907ae4b9c6735c8906850b0574c493a657fb
raw_storage_status: archived-local
archive_required: true
learning_candidate: true
nuclei: [48ca, 76ge, 82se, 96zr, 100mo, 116cd, 124sn, 128te, 130te, 136xe, 150nd, 150sm]
reactions: []
experiments: []
models: [energy-density-functional, gogny-d1s, 2d-gcm, pairing-fluctuations, pnamp]
observables: [0nu-nme, half-life, particle-number-dispersion, deformation-beta2, gt-strength, binding-energy, radii]
methods: [two-dimensional-gcm, particle-number-fluctuation-constraint, hill-wheeler-griffin-equation, ucom-src]
tags: [0nu-beta-beta, nuclear-matrix-elements, pairing-fluctuations, gogny-d1s, 2d-gcm, deformation-pairing-interplay, fulltext-read]
---

# Vaquero, Rodríguez & Egido 2013：能量密度泛函中四极形变与配对涨落对无中微子双贝塔衰变核矩阵元的协同效应

## Bibliographic Record

Nuria López Vaquero, Tomás R. Rodríguez, and J. Luis Egido, *Shape and pairing fluctuations effects on neutrinoless double beta decay nuclear matrix elements*, Physical Review Letters **111**, 142501 (2013). DOI: `10.1103/PhysRevLett.111.142501`。arXiv 预印本版本为 `arXiv:1401.0650v1 [nucl-th]`（提交日期为 2014 年 1 月 3 日；预印本首页注记 "(Dated: September 18, 2018)" 与版本/发表年份不同；其产生原因未查明，不据此另立2018年研究）。本地归档 PDF 位于 `raw/papers/gpt/query/20261108-foundations-G35/vaquero-2013-prl111-142501-shape-pairing.pdf`，大小 776,287 字节，SHA-256 值为 `9069f66dd9ca177b816a606475e0907ae4b9c6735c8906850b0574c493a657fb`。

## Scope and Reading Depth

- Completed reading_depth: deep-read（全文 5 页深度精读，涵盖正文公式 Eqs. 1–5、表 I 完整数据、图 1 二维势能面与集体波函数、图 2 形变与配对涨落依赖、图 3 与其它模型对比）。
- Covered scope:
  1. 将 GCM 从一维形变 $\beta_2$ 拓展至自洽二维生成坐标 $(\beta_2, \delta)$，其中 $\delta = \langle (\Delta \hat{A})^2 \rangle_{\varphi}^{1/2}$ 为粒子数涨落约束参数（非 BCS 能隙 $\Delta$）；
  2. 粒子数投影后变分（PN-VAP）生成态，随后角动量投影及二维GCM求解；
  3. 以 $^{136}\text{Xe} \to {}^{136}\text{Ba}$ 为图示算例，分析二维势能面（PES，图 1）与两体跃迁核（图 2）的行为；
  4. 图 2(b) 中跃迁核随粒子数涨落坐标 $(\delta, \delta')$ 的响应：在 $\delta, \delta' < 2$ 时极小，在 $\delta, \delta' > 2$ 时沿非对角宽带区域 $\delta' \approx \delta \pm 3$ 快速增长；
  5. 表 I 系统量化 2D-GCM 相对 1D-GCM 的数值演化：注意在 1D 对应列中，$^{116}\text{Cd}$ 的 $M^{0\nu}(\beta_2)$ 为 4.795（不等同于 2010 年表 I 的 4.72，原因未由本任务查明）；$^{136}\text{Xe}$ 为 4.199 $\to$ 4.773；$^{48}\text{Ca}$ 为 2.370 $\to$ 2.229（$-6\%$）；$^{76}\text{Ge}$ 为 4.601 $\to$ 5.551（$+21\%$）；
  6. 预测半衰期的相对比值 $T_{1/2}(\beta_2, \delta) / T_{1/2}(\beta_2)$。
- Not covered:
  1. 质子-中子同位旋标量配对（$T=0$ pn pairing）的显式动力学处理；
  2. 三轴非轴对称形变自由度 $\gamma$；
  3. 奇奇中间核逐态色散能谱（依然使用闭合近似）。

## Summary

Vaquero 等人 (PRL 2013) 在 Gogny D1S 能量泛函下实现了轴对称四极形变 $\beta_2$ 与粒子数涨落坐标 $\delta = \langle (\Delta \hat{A})^2 \rangle^{1/2}$ 的自洽二维生成坐标法（2D-GCM）。在有限力程相互作用下，约束粒子数方差 $\delta$ 是自洽生成不同超流配对成分基矢的标准手段。以 $^{136}\text{Xe} \to {}^{136}\text{Ba}$ 为例（图 1 与图 2），势能面沿 $\delta$ 坐标展现出宽平软阱；跃迁核随粒子数涨落增大在 $\delta' \approx \delta \pm 3$ 宽带区显著增长。在表 I 计算的具体候选核集合中，除双闭壳核 $^{48}\text{Ca}$ 因势阱在较大配对处陡峭而轻微下降 $-6\%$（$2.370 \to 2.229$）外，其余计算的开壳核矩阵元增加了 $10\% \sim 40\%$（如 $^{76}\text{Ge}$ 为 $4.601 \to 5.551$，$^{136}\text{Xe}$ 为 $4.199 \to 4.773$；注意表 I 中 1D 重算值为 $^{116}\text{Cd}$ 给出 4.795，与 2010 年表 I 的 4.72 存在表值差别，未查明具体原因）。该工作定量证实了配对维度动态涨落对多体模型矩阵元计算具有显著影响。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| V13-1 | 引入约束在粒子数涨落 $\langle (\Delta \hat{A})^2 \rangle_{\varphi}^{1/2} = \delta$ 上的内禀 HFB 态，与轴对称四极矩 $\langle \hat{Q}_{20} \rangle$ 共同构成二维 GCM 基矢，并实施粒子数与角动量投影（2D-PNAMP）。 | model-result | direct | p. 1, col. 2, Eqs. (2)-(3); p. 2, col. 1 | false |
| V13-2 | 在固定四极形变下，原子核势能面沿粒子数涨落坐标 $\delta$ 展现宽平软阱（图 1a-b，以 $^{136}\text{Xe}$ 与 $^{136}\text{Ba}$ 为例），表明基态具有动态配对涨落。 | model-result | direct | p. 2, col. 2; Fig. 1a-b | false |
| V13-3 | 0νββ 跃迁核在配对相空间中，当 $\delta, \delta' < 2$ 时极小，而在 $\delta, \delta' > 2$ 时沿非对角宽带区域 $\delta' \approx \delta \pm 3$ 迅速增长（图 2b，以 $^{136}\text{Xe} \to {}^{136}\text{Ba}$ 为例）。 | model-result | direct | p. 3, col. 2; Fig. 2b | false |
| V13-4 | 在该文计算的开壳候选核算例中，纳入配对涨落后的 $M^{0\nu}(\beta_2, \delta)$ 相比 1D-GCM $M^{0\nu}(\beta_2)$ 增大约 $10\% \sim 40\%$（如 $^{76}\text{Ge}$ 从 $4.601 \to 5.551$, $^{100}\text{Mo}$ 从 $5.084 \to 6.588$, $^{136}\text{Xe}$ 从 $4.199 \to 4.773$, $^{150}\text{Nd}$ 从 $1.707 \to 2.190$；注意 $^{116}\text{Cd}$ 1D 值为 4.795，与 2010 年表 I 的 4.72 存在表值差别，未查明具体原因）。 | model-result | direct | p. 4, Table I | false |
| V13-5 | 在该文计算集合中，双闭壳核 $^{48}\text{Ca}$ 的矩阵元出现轻微下降（$2.370 \to 2.229$，变化率 $-6\%$），源于其闭壳结构使配对势阱在较大配对处陡峭上升，量子涨落重心偏向弱配对区。 | model-result | direct | p. 4, col. 1; Table I | false |
| V13-6 | 在包含配对涨落后，该文计算的除 $^{48}\text{Ca}$ 外的候选核预测半衰期缩短，缩短因子在 $0.52 \sim 0.81$ 之间。 | model-result | direct | p. 4, col. 1; Table I | false |

## Competing Interpretations and Limitations

1. **同位旋破缺假态与 Fermi 矩阵元贡献**：文献指出，未严格恢复同位旋对称性的自洽平均场模型可能包含由于质子-中子非对称性带来的同位旋杂质，对 Fermi 项的评估产生一定影响。
2. **三轴与准粒子破对相消缺位**：该模型仍限制于轴对称几何，且未显式包含破对的两准粒子与四准粒子高 Seniority 态。
3. **闭合近似依赖**：依然采用闭合近似，两体算符未包含更高阶手征流修正。

## Extracted Pages

- Nuclei: $^{48}\text{Ca}, {}^{76}\text{Ge}, {}^{82}\text{Se}, {}^{96}\text{Zr}, {}^{100}\text{Mo}, {}^{116}\text{Cd}, {}^{124}\text{Sn}, {}^{128}\text{Te}, {}^{130}\text{Te}, {}^{136}\text{Xe}, {}^{150}\text{Nd}$.
- Concepts: 二维生成坐标法 (2D-GCM), 粒子数涨落约束, 配对相空间软性, 核矩阵元模型依赖.
- Methods: 变分后二维投影 (2D-PNAMP), 约束 HFB.
