---
type: source
title: "Crespi 2013：AGATA 高能 γ Doppler 校正的速度限制"
aliases: [Crespi AGATA 15.1 MeV response, PSA plus 1HitID high energy gamma]
created: 2026-10-13
updated: 2026-10-13
status: ai-draft
review_status: unreviewed
source_type: journal-method-experiment-with-public-preprint
reading_depth: deep-read
title_original: "Response of AGATA segmented HPGe detectors to gamma rays up to 15.1 MeV"
authors: [F. C. L. Crespi, R. Avigo, F. Camera, S. Akkoyun, A. Atac, D. Bazzacco, et al.]
journal: Nuclear Instruments and Methods in Physics Research A
year: 2013
volume: 705
pages: 47-54
doi: 10.1016/j.nima.2012.12.084
arxiv: 1209.1188v1
language: en
canonical_source: "https://doi.org/10.1016/j.nima.2012.12.084"
citation_key:
raw_file: "raw/papers/gpt/day13/crespi-2013-agata-15mev.pdf"
raw_sha256: "1334b31bac18e12c1ce887de43d2e74e6ec0d409d49e0dc5d5660db03ab5b983"
raw_storage_status: reserved-unpopulated-public-preprint-only
external_pdf_url: "https://arxiv.org/pdf/1209.1188"
nuclei: [12c]
reactions: [d-11B-n-gamma-12C]
methods: [doppler-correction, gamma-ray-tracking, pulse-shape-analysis]
tags: [agata, velocity-vector, high-energy-gamma, pair-production, detector-response]
---

# AGATA 高能 γ：γ 位置精度与反冲速度信息的分工

## Bibliographic Record

F.C.L.Crespi et al., *NIM A*705,47–54(2013)，DOI`10.1016/j.nima.2012.12.084`。Crossref核验题名、年、卷页；实际读取10页preprint `1209.1188v1`，所有PDF locator为preprint页/原table/figure。该preprint与journal是依赖版本；未做publisher版逐字/全author-roster比对。

保持本任务raw不变：frontmatter raw_file只是未填充canonical槽位，未创建；获取字节仅存`tmp/day13/reopened/crespi-2013-agata-15mev.pdf`并以所列SHA指纹核验。长期入口为公开arXiv URL；raw_sha指纹为remote-preprint字节，未声称本地raw archive存在。保留RAW_MISSING边界，临时副本失效需重获核验。

## Scope and Reading Depth

全文主线10页：intro、in-beam/source setup、energy/linearity、multiplicity/neutron capture/escape对照、Doppler/velocity/ordering、simulation及conclusion；视觉核验p.8 Table2/Fig10，p.6–9的velocity/peak说明。未持有events、PACE4参数/完整输出、PSA/executable hash、joint covariance、publisher逐字校对。

## Paper Question and Scientific Motivation

AGATA的高能10–20MeV应用需要检验response、PSA、tracking与pair-production，不可将0–4MeV算法性能直接外推。 Doppler改善是否受γ point resolution还是未测recoil vector限制，是本轮关键问题。

## Method and Design Logic

45MeV11B经29mg/cm²Au foil降到19.1MeV，在490μg/cm² C32D66 target上通过d(11B,nγ)12C产生15.1MeV single M1 γ；0.1mmTa backing停止recoil/beam。两个AGATA triple clusters距target13.5cm，gamma measurement无外部coincidence trigger。 Am-Be-Fe提供静止calibration/multiplicity对照（p.2）。

PSA+1HitID取最高能量interaction为第一点；与crystal/segment中心、标准tracking比较。速度未逐事件测量，作者通过15.1MeV峰centroid/width优化一个平均vector，再用PACE4/Geant4比对（p.6–9）；average fit不是independent velocity measurement。

## Key Evidence and Reasoning Chain

source gain matching/response → high-energy multiplicity与neutron-capture背景 → mean-vector + position options → Table2/Fig10 widths → PACE4/Geant4解释floor。所有position-options与simulation比较共享该实验/输入，不计为独立验证recoil vector。

## Summary

Table2给119keV(PSA+1HitID)、122keV(segment centers)、>160keV(crystal centers)。作者解释119-vs122的弱改善由未逐事件重建12C速度向量限制，而非PSA失效。低γ multiplicity、pair-production主导与background低时，简单add-back+PSA比标准tracking保留更多FEP；不是所有实验的通用排序规则。

## Experimental or Theoretical Setup

- moving12C速度scale约0.05c；平均optimizedβ=0.046，AGATA-frame方向components(0,0.85,0.51)。
- PACE4 meanβ=0.048；原文写95% interval β0.042–0.058及方向偏差0–10°，未在本轮获得其完整统计定义/重建输入，不把它改写成测得βposterior。
- intrinsic width从静止source随E外推约10keV；simulation置8keV，这都不是该119keV线的本征自然宽度或直接intrinsic measurement。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CR13-1 | d(11B,nγ)12C at19.1MeV产生15.1MeVγ，两个triple clusters距target13.5cm；reference sources提供独立静止calibration；此run未测12C event velocity/direction。 | experimental-fact | direct | preprint PDF p.2, Sec.2; p.6, Sec.5 | true |
| CR13-2 | 通过峰centroid/width优化平均β=0.046和方向(0,0.85,0.51)；与PACE4 meanβ0.048比较，原文95%interval0.042–0.058、偏离束轴0–10°。这不是独立逐事件β测量。 | author-interpretation | direct | preprint PDF p.6, Sec.5 | true |
| CR13-3 | Doppler corrected15.1MeV峰FWHM为119keV(PSA+1HitID)、122keV(segment centers)、>160keV(crystal centers)；作者认为未逐事件重建velocity vector是主要限制。 | experimental-fact | direct | preprint PDF p.7, Sec.5; p.8, Table2 and Fig.10 | true |
| CR13-4 | Geant4 simulation使用PACE4 velocity distribution、8keV extrapolated intrinsic response，与119keV谱比较；作者称velocity uncertainty dominates。原始joint-event/response/covariance缺失，不能由此独立复算各variance分量。 | model-result | direct | preprint PDF p.7, Sec.5; p.9, Fig.11 | true |
| CR13-5 | 当前15.1MeV/multiplicity1/低background条件下，standard mgt tracking FEP events约为add-back+PSA+1HitID的0.25；作者指出tracking优化在0–4MeV Compton区，而这里pair-production重要。 | experimental-fact | direct | preprint PDF p.6, Sec.5; p.9, Conclusions | true |
| CR13-6 | 在Am-Be-Fe source中tracking抑制10.196MeV的74Ge neutron-capture sum peak，因为多个γ的总energy不应当作一条line；两种处理在background/line identity上有tradeoff。 | experimental-fact | direct | preprint PDF p.5, Sec.4; p.7, Fig.8 | true |

## Nuclear Structure Information

12C15.1MeV为instrument test line，不在本篇推导新低能collective bands；branch为source列92% ground-state decay context，未用于本任务新的absolute-strength分析。

## Authors' Interpretation

γ position精细化降低finite-solid-angle贡献，但velocity spread/direction在本run成为floor；highest-energy-first在stated high-energy/multiplicity下较有效。 不支持“简单排序总优于完整tracking”。

## Model Results

PACE4/Geant4对distribution/response解释为model层；最佳平均β来自同一谱，不构成model与实验间独立velocity verification。figure agreement只是reported comparison，未把图像曲线数字化为新参数。

## Competing Interpretations and Limitations

- >160→119改善有数据支持；122→119中心差约2.46%，未给joint-width uncertainty不能赋显著性。
- fitted平均velocity与energy-calibration/geometry/lifetime因素可耦合；本篇缺event-vector，所以不能从优化均值作beam/target独立reconstruction。
- intrinsic extrapolation、stopping、source gamma linearity与actual reaction spread是不同层。
- escape/multiplicity/neutron sum peaks与tracking selection改变FEP效率；适用能区/multiplicity必须匹配。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| CR13-AR1 | FEP/selection | corrected energy gate的acceptance随algorithm/width/centroid而变；fixed gate实验设计必须记录efficiency与mapping。数值gate例题属于任务推导，非来源测量。 | CR13-3/5/6; [[doppler-correction]] | unreviewed |
| CR13-AR2 | floor反证 | 与VAMOS直接vertex/vector实验组合，反证单靠更精细γ point必能达到intrinsic width的命题。 | CR13-3/4; [[vandebrouck-2016-vamos-dual-position-mwpc]] VD16-3 | unreviewed |

## Knowledge Impact and Learning Decision

`limits`只升级photon position的充分性；`supports`matched recoil/vertex/PSA信息和algorithm-specific response。更新 [[doppler-correction]] 与 [[tracking-array]]；与VAMOS和Longfellow共享概念，实验不同，无新shape/strength裁决。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-correction]] | matched event-vector/position、平均fit与variance floor。 |
| methodological-bridge | [[tracking-array]] | high-energy pair-production、multiplicity与efficiency改变排序适用性。 |
| competing-interpretation | [[vandebrouck-2016-vamos-dual-position-mwpc]] | 独立geometry/recoil-information实验对照；不转移数值。 |
| methodological-bridge | [[longfellow-2026-gretina-energy-ordering-polarization]] | 两篇都有energy ordering，但setup/energy/multiplicity不同，不当独立测量同一性能。 |

## Human Review Triage

P0：未识别未隔离identity/权限风险；raw保留位置未归档已明示。P1：CR13-2 fitted vector/interval统计定义、CR13-3 width comparison无joint errors、CR13-5/6 efficiency/background tradeoff；全部new claims needs_review。

## Extracted Pages

preprint pp.1–2 motivation/setup，pp.3–5 calibration/multiplicity，pp.6–9 velocity/Table2/figures/conclusion；reusable诊断见 [[doppler-correction]]。
