---
type: source
title: "Vandebrouck 2016：VAMOS++ 双位置 MWPC 与 Doppler 速度向量重建"
aliases: [Vandebrouck DPS-MWPC, VAMOS++ dual position tracking]
created: 2026-10-13
updated: 2026-10-13
status: ai-draft
review_status: unreviewed
source_type: journal-method-experiment-with-public-preprint
reading_depth: deep-read
title_original: "Dual Position Sensitive MWPC for tracking reaction products at VAMOS++"
authors: [M. Vandebrouck, A. Lemasson, M. Rejmund, G. Fremont, J. Pancin, A. Navin, C. Michelagnoli, J. Goupil, C. Spitaels, B. Jacquot]
journal: Nuclear Instruments and Methods in Physics Research A
year: 2016
volume: 812
pages: 112-117
doi: 10.1016/j.nima.2015.12.040
arxiv: 1512.08881v1
language: en
canonical_source: "https://doi.org/10.1016/j.nima.2015.12.040"
citation_key:
raw_file: "raw/papers/gpt/day13/vandebrouck-2016-vamos-mwpc.pdf"
raw_sha256: "66afd2c355fb3a6e4e507b9c369154f282e7a685848c0ad4110397b6c8d57e71"
raw_storage_status: reserved-unpopulated-public-preprint-only
external_pdf_url: "https://arxiv.org/pdf/1512.08881"
nuclei: [98zr]
reactions: [238U-9Be-fission]
methods: [doppler-correction, recoil-tracking, time-of-flight]
tags: [vamos, agata, doppler-correction, position-resolution, velocity-vector]
---

# VAMOS++ 双位置 MWPC：靶点、方向与速度

## Bibliographic Record

M. Vandebrouck et al., *NIM A* **812**, 112–117 (2016), DOI `10.1016/j.nima.2015.12.040`，Crossref本轮核验题名、作者、卷页；2015 preprint为同一来源谱系。正文实际读取公开的8页 arXiv `1512.08881v1`，不是出版商分页；所有下述PDF页码均指这份preprint。

**本地原始材料边界：**为保持本任务 `raw/` 不变，frontmatter的raw_file是未填充的规范保留位置，文件未创建，不能声称已归档。此次获取字节仅在 `tmp/day13/reopened/vandebrouck-2016-vamos-mwpc.pdf`，SHA-256为上列值；长期重获入口为公开URL/arXiv ID。`raw_sha256`记录实际获取的preprint字节指纹，不是未存在raw文件的本地校验结果。若临时副本消失，须重新获取并核验；保留RAW_MISSING边界。preprint封面印有August23,2018编译日期，与arXiv v1/date及期刊2016年份不是同一字段，未据此更改出版年。

## Scope and Reading Depth

- Covered scope：8页全文主线，introduction需求、detector geometry、两次performance测量、positions/angles/TOF/efficiency、AGATA Doppler对照、summary及相关references。
- Deep checks：p.5 wire-shadow/mask过程、p.6 Table1和Sec.3.5、p.7 Fig.5与数据谱系；关键页视觉核验。
- Not covered：原始focal-plane/γ事件、path-length maps、完整joint covariance、E680原始数据、期刊最终版逐字比对。
- Review boundary：self-audit不等于human-reviewed；σ与FWHM、独立测试与共享数据区分。

## Paper Question and Scientific Motivation

γ tracking精细化后，仅用focal-plane trajectory推回target角度且假定point-like beamspot，可能限制Doppler分辨率。作者开发位于VAMOS++入口的双位置/时间测量，以直接约束scattering direction和target interaction point（p.1–2）。

## Method and Design Logic

两低压MWPC的4个坐标定义ion trajectory，两个fast timing信号支持TOF。 cathodes相距105mm，detector assembly位于target下游174mm；薄window/低压gas降低能损与straggling（p.2 Fig.1）。位置用wire charge distribution的hyperbolic-secant拟合，reference-wire shadow与target mask/MC校验。TOF性能用252Cf source与额外MWPC/Si测量；in-beam性能使用238U 6.2MeV/u+9Be 1.85mg/cm²（p.3,5–6）。

## Key Evidence and Reasoning Chain

4-coordinate/TOF测量 → target position/direction重建 → isotopically identified98Zr gate + first γ interaction → 与旧trajectory方法比较同一1222.9-keV line的校正谱（p.6–7）。两种校正是同次γ数据重处理，不是两次独立核结构测量。

## Summary

作者报告305(11)ps TOF FWHM、2.5(3)mrad angle FWHM与560(70)μm target position FWHM。98Zr1222.9(1)-keV line从8.6(1)到5.5(1)keV，约1.6倍改善。该结果支持同时重建recoil vector与target vertex；不会将任意γ array/beam的速度误差自动变成这些性能值。

## Experimental or Theoretical Setup

- source test：252Cf，2.3mbar；TOF gate选择light-fragment一部分能区。
- in-beam：238U6.2MeV/u，9Be1.85mg/cm²，VAMOS++26°，6mbar；detected fission products约Z28–65、2–8MeV/u。
- AGATA compact configuration，nominal target distance23.5cm而阵列沿下游平移8.8cm；100°–170°覆盖，不能将平移量直接当作所有crystal相同radial distance。
- gamma first-point resolution约5mm FWHM为引用先前工作；对应compact约1.9°、nominal约1.2°（p.6），不是本篇独立测得所有点的σ。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| VD16-1 | 双position-sensitive MWPC以(X1,Y1,X2,Y2)约束target vertex/scattering方向，同时提供TOF start；cathode间距105mm，assembly距target174mm。 | experimental-fact | direct | preprint PDF p.2, Sec.2; p.3, Fig.1 | true |
| VD16-2 | source/in-beam校验给TOF FWHM305(11)ps、scattering-angle FWHM2.5(3)mrad、target-point FWHM560(70)μm；Table1以σ列130(5)ps、1.1(1)mrad、239(30)μm，以及front/back73(9)/84(11)μm。 | experimental-fact | direct | preprint PDF p.5, Secs.3.2–3.3; p.6, Table1 | true |
| VD16-3 | 使用测得98Zr velocity vector、target point和AGATA first point，同一1222.9(1)-keV line的校正width为5.5(1)keV，旧focal-plane角度重建为8.6(1)keV，约1.6倍改善。 | experimental-fact | direct | preprint PDF p.6, Sec.3.5; p.7, Fig.5 | true |
| VD16-4 | tracked event效率约96%；单plane(t,X,Y)效率约98%，geometrical transparency每plane约96%。这些定义不同，不能相互替代为γ detection efficiency。 | experimental-fact | direct | preprint PDF p.6, Sec.3.4 | true |
| VD16-5 | 旧path-length/rigidity/target-angle重建依赖focal-plane信息及point-like beamspot假设；新target-point/direction可与spectrometer信息结合改善path length/rigidity。Fig.5原始γ数据获E680 collaboration提供。 | author-interpretation | direct | preprint PDF p.7, Summary and acknowledgements | true |

## Nuclear Structure Information

本篇使用已知98Zr line来检验仪器/校正性能，没有新的集体模式、partner强度或nucleus-level结构裁决。

## Authors' Interpretation

直接测量的vertex/direction精度可解除旧重建对beamspot的严格要求，并匹配下一代γ tracking能力；优越性依赖当前geometry/beam/测量条件。

## Model Results

target-mask的position/angle分辨率由含测量position resolution的MC估计并与mask image比较（p.5）。因此FWHM为data-constrained performance，不当作所有event的完整posterior/covariance。

## Competing Interpretations and Limitations

- photon first-point、recoil direction、target vertex、TOF/path length共同贡献；Fig.5改善不能仅归给β magnitude一项。
- 305ps是受能区gate的source TOF FWHM；估计单detector216ps需start/stop相同响应假设，不直接套入experiment全程flight-time resolution。
- σtarget与σangle来自相同two-plane coordinates，可能相关；Table1没有joint covariance。
- apparatus透明度、reconstructed-event效率、γ photopeak效率为不同对象；simulation只是局部校验。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| VD16-AR1 | 两点geometry | 在自设straight-line、小角度、独立plane errors和L1=174/L2=279mm假设下，σangle约1.060mrad、σtarget约0.23875mm，与Table1 scale相容；Cov(target,angle)<0且ρ≈−0.973。这是任务推导，不是作者joint-covariance测量。 | VD16-1/2; [[doppler-correction]] | unreviewed |
| VD16-AR2 | 信息增益 | γ first-point精细化仍须独立recoil/vertex precision；与Crespi的velocity-limited15.1MeV对照组合形成可检验诊断。 | VD16-3; [[crespi-2013-agata-high-energy-doppler-response]] | unreviewed |

## Knowledge Impact and Learning Decision

`supports` event-by-event vector/vertex重建，`revises`把angle/vertex误差视为互不相关的简化，`limits`mean β/γ position alone。 owning method为 [[doppler-correction]]；本页与Crespi独立实验对照，不制造99Zr/collective解释或实验L4。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-correction]] | 双点/TOF/target geometry接到精确energy correction及covariance。 |
| methodological-bridge | [[tracking-array]] | photon first-point改善只有在recoil vector/vertex已充分约束时兑现。 |
| competing-interpretation | [[crespi-2013-agata-high-energy-doppler-response]] | 独立仪器实验，区分geometry改善与velocity主导floor，不复用数据。 |

## Human Review Triage

P0：未识别到未隔离的source-identity/权限问题；未填充raw槽位已明示，不声称原始数据归档。P1：VD16-2的σ/FWHM，VD16-3的same-event/data依赖，VD16-AR1的plane-error/geometry假设；未来论文使用需回到指定claim。

## Extracted Pages

preprint pp.1–3 setup，p.5 position/mask/time，p.6 Table1/efficiency/Doppler，p.7 Fig.5/summary；long-term方法见 [[doppler-correction]]。
