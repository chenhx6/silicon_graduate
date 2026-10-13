---
type: source
title: "Söderström 2008：AGATA tracking 与两距离 position 标定提案"
aliases: [Soderstrom 2008 two-distance resolution, AGATA Vertex 2008 proceedings]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: conference-proceedings-method-simulation
reading_depth: deep-read
title_original: "AGATA: Gamma-ray tracking in segmented HPGe detectors"
authors: [P.-A. Söderström, A. Al-Adili, J. Nyberg, F. Recchia, E. Farnea, A. Gadea]
journal: "17th International Workshop on Vertex detectors proceedings; arXiv public preprint"
year: 2008
arxiv: 0812.0091v1
language: en
canonical_source: "https://arxiv.org/abs/0812.0091v1"
citation_key:
raw_file: "raw/papers/gpt/day13/soderstrom-2008-proceedings.pdf"
raw_sha256: "6b1ba0ff312d264d600c827d6ee1e46860d31278dea08374455d2ad00b82d69e"
raw_storage_status: reserved-unpopulated-public-preprint-only
external_pdf_url: "https://arxiv.org/pdf/0812.0091v1"
nuclei: [38ar, 49ti, 52cr, 86sr, 82kr, 142ce]
methods: [gamma-ray-tracking, doppler-correction, position-resolution-calibration]
models: [geant4]
tags: [agata, geometry, two-distance, simulation, formula-boundary]
---

# 两距离 Doppler-position 标定的设计条件

## Bibliographic Record

P.-A. Söderström等，2008 Vertex workshop proceedings 的公开 arXiv0812.0091v1，2008-11-29。PDF10页，会议为2008-07-28至08-01、Utö Island；未核定正式 proceedings DOI/页号，不由相近检索结果填充。PDF给出作者拥有版权、CC BY-NC-SA说明。

保持raw不变：frontmatter的raw_file是未填充保留位置；获取字节在 `tmp/day13/reopened/soderstrom-2008-proceedings.pdf`，SHA为所列值。此页不声明归档或2011期刊论文已读。

## Scope and Reading Depth

- 10页全文主线：历史/AGATA设计→PSA inputs/basis→forward/backtracking→Doppler宽度与两距离提案→preliminary simulations/限制→references。
- 重点核验pp.5–8 Eqs.(4.1)–(4.4)、Figs.3–6；p7 Eq.(4.4)视觉核对，确认无宽度/距离平方的提取丢失。
- 未覆盖：原Recchia学位论文、2009/2011期刊全文、实际MGT/PSA代码/事件；正文引用的过往分辨率实验不算本稿新实验。

## Paper Question and Scientific Motivation

如何以较短commissioning时间估计PSA位置分辨率，并减少单距离Doppler标定对reaction Monte Carlo的依赖。文章是早期方法/模拟提案，不能把未来计划写成已完成的beam test。

## Method and Design Logic

PSA与first-point ordering确定photon方向；印刷四项宽度平方和分开intrinsic、recoil speed、recoil angle和photon angle。后者随source-to-first-point几何变化，所以提出两距离比较，以消去相同的其它宽化项。共同baseline、相同响应与有限角度/深度是本任务需要显式检验的条件。

## Key Evidence and Reasoning Chain

one-distance width→reaction-model依赖→two-distance differential design→simulated p与input smearing的比较→wide-angle/curved-face限制。模型解释与已引实验报告分层，不能用后两者重复增加独立样本。

## Summary

论文给出实用的几何杠杆思路，但preliminary Figs.4/6不证明两距离法在任意有限阵列里无模型依赖。印刷Eq.(4.4)的形式不能在通常的 `Wθγ=kp/d` 前提下从此前平方和直接导出；保留原式，本任务另列有明确假设的平方差推导。

## Experimental or Theoretical Setup

Fig.3为9Be(80Se,3n)86Sr模拟、source-front distance40mm、position smearing5mm；Figs.4/6涉及其它候选反应及40/140mm geometry。引用的Cologne single-crystal/triple-cluster实验属于外部谱系；无本稿实验事件包。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SD08-1 | PSA使用hit segment、邻段mirror charges及core波形；扫描库与计算库各有时间/impurity/charge-mobility边界。 | author-interpretation | direct | PDF p.3, Sec.2.1/Fig.1 | true |
| SD08-2 | Forward/cluster tracking假定source zeroth point，对cluster permutations计算FOM；backtracking从候选最后photoelectric deposit回溯，算法性能依完整event与physics条件。 | experimental-criterion | direct | PDF pp.4–5, Secs.3.1–3.2 | true |
| SD08-3 | Eq.(4.1)写四项FWHM平方和，Eq.(4.3)给Doppler angular sensitivity；它不是保留所有covariance或非Gaussian kernels的普遍线型公式。 | synthesis | direct | PDF p.5, Eqs.(4.1)–(4.3) | true |
| SD08-4 | 文章转述Cologne single-crystal与triple-cluster分辨率4.3mm@2168keV、4.4mm@1382keV，并认为reaction Monte Carlo是主要估计不确定度；原实验/版本本轮未独立读。 | experimental-fact | indirect | PDF pp.6–7; Refs.[21],[27],[28] | true |
| SD08-5 | p7 Eq.(4.4)印刷为p²=k⁻²(Wclose−Wfar)(dclose⁻¹−dfar⁻¹)⁻¹，无相应平方。以同一W的quadrature及Wθγ=kp/d解释时不能直接导出；source未明确给k的单位，不能据此宣布执行代码错误。 | our-inference | indirect | PDF p.7, Eq.(4.4), visual check; p.5, Eqs.(4.1)/(4.3) | true |
| SD08-6 | 作者把Fig.6估计/输入smearing的偏差解释为近距离wide-angle coverage及弯曲front face导致的distance不确定，并计划进一步改进。 | author-interpretation | direct | PDF p.8, Fig.6 and following paragraph | true |
| SD08-7 | Fig.4归于当时Al-Adili master thesis manuscript，Fig.6为本文preliminary design；与后来AA09同一模型/作者谱系，不计为两次独立实验或保证版本/字节相同。 | synthesis | direct | PDF pp.6,8,10; Refs.[23],[29] | true |

## Nuclear Structure Information

核素/反应为commissioning方法样例；本稿不测新的A≈130collective-mode、寿命或绝对B。

## Authors' Interpretation

近90°、较高β、近detector加强position sensitivity；neutron channel能减小reaction spread；两距离比单距离减少Monte Carlo依赖。有限角度/face shape的限制也由作者明确提出，不能省略。

## Model Results

Figs.3–6是模型/设计结果；过去实验分辨率是引用。原input/events/code缺失，不宣称本任务复现这些图。 [day13_two_distance_resolution.py](../../system/scripts/day13_two_distance_resolution.py)仅执行本任务声明的Gaussian/common-baseline/point-distance模型，见 [[doppler-correction]]。

## Competing Interpretations and Limitations

- 已知核速度并不消去intrinsic/position/ordering；两距离法只消去确实相同的nuisance。
- distance-to-front与distance-to-first-IP不同；角接受率、能量/深度响应和threshold可随geometry改变。
- Eq.(4.4)原式与本任务平方差公式并列，未覆盖raw、未称author-approved修正，也未验证生产代码。
- 本稿与AA09、被引用Recchia工作/后续综述共有模型或实验谱系，不重复计数。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SD08-AR1 | two-distance algebra | 在W²=B²+(kp/R)²且B/k/p相同的前提下，p²应来自width平方差/距离倒数平方差；不同原式不静默替换。 | SD08-3/5; [[doppler-correction]] | unreviewed |
| SD08-AR2 | transfer | 两点总能拟合common-baseline两参数；第三distance/held-out geometry、独立particle vector及first-IP geometry才提供额外失败检查。 | SD08-6; [[doppler-correction]] | unreviewed |

## Knowledge Impact and Learning Decision

`supports`利用geometry改变提高可识别性的设计；`limits`不加条件的Monte Carlo independent或两距离等于独立calibration断言。保留source printed formula与execution缺口。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-correction]] | 共同variance、distance杠杆和held-out geometry。 |
| same-lineage | [[aladili-2009-agata-doppler-simulation]] | Fig.4引用master manuscript，版本不保证一致。 |
| methodological-bridge | [[tracking-array]] | PSA/first-point、扫描库与geometry transfer条件。 |

## Human Review Triage

P0：raw槽位未归档/直接文件身份明示。P1：SD08-3/5 algebra与假设，SD08-4 secondary实验谱系，SD08-6 geometry transfer。本任务self-audit不升级human-reviewed。

## Extracted Pages

PDF1–10主线；关键5–8，Eq.(4.4) p7视觉核验。2011文章仅metadata，不以本稿代替其正式结果。
