---
type: source
title: "Assié 2021：MUGAST-AGATA-VAMOS 的两体反冲与联合测量"
aliases: [MUGAST AGATA VAMOS campaign 2021, Assie particle-assisted Doppler correction]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: journal-instrument-method-experiment
reading_depth: deep-read
title_original: "The MUGAST-AGATA-VAMOS campaign: Set-up and performances"
authors: [M. Assié, E. Clément, A. Lemasson, D. Ramos, A. Raggio, I. Zanon]
author_list_scope: first-six-common-to-public-preprint-and-journal-metadata
journal: Nuclear Instruments and Methods in Physics Research Section A
year: 2021
volume: 1014
pages: 165743
doi: 10.1016/j.nima.2021.165743
arxiv: 2104.10707v1
data_version: "public arXiv2104.10707v1 copy; beam configurations2019/2020 separated"
language: en
canonical_source: "https://arxiv.org/abs/2104.10707v1"
citation_key:
raw_file: "raw/papers/gpt/day13/assie-2021-mugast-campaign.pdf"
raw_sha256: "7eb71ca9d7816083184fbdac2b1f8ca91b77cbb69da47988017a563c4719c451"
raw_storage_status: reserved-unpopulated-public-preprint-only
external_pdf_url: "https://arxiv.org/pdf/2104.10707v1"
nuclei: [17o, 20o, 19ne]
reactions: [16O-d-p-17O, 19O-d-p-20O, 15O-7Li-t-19Ne]
methods: [doppler-correction, gamma-ray-tracking, particle-identification, two-body-kinematics, gamma-particle-coincidence]
models: [nptool, dwba, adwa]
tags: [mugast, agata, vamos, recoil-vector, target-loss, rigidity, pid, normalization]
---

# 粒子信息怎样约束 Doppler correction

## Bibliographic Record

M.Assié等，NIMA1014,165743(2021)，DOI10.1016/j.nima.2021.165743，Crossref题名/首作者/年/卷/页身份核验。实际读arXiv2104.10707v1的13页public copy；arXiv标头21April2021、submission footer/build23April2021分别记录。Frontmatter列共同前六author，正式完整作者顺序应回对应version；Crossref完整列表含F.Delaunay而本copy author header未见，不把两列表视为逐字相同。

raw保持不变：raw_file为未填充保留位置；copy在 `tmp/day13/reopened/assie-2021-mugast-campaign.pdf`，SHA如上。Initial title-field arXiv query返回400，换plain query后找到exact title/id，并以Crossref/OpenAlex/直接PDF核验；search摘要不作为科学证据。

## Scope and Reading Depth

- 13页全文主线：direct-reaction动机→mechanical/lightparticle/AGATA/VAMOS→DAQ/clock→PID/missingmass/target→gamma efficiency→three beam examples→two-body Doppler与rigidity TOF→conclusion/reference。
- 深核验Fig.8/9与7.3–7.4的Figs.17/18、Eq.(1)，PDFpp.7–8/11–12；原图视觉核验。
- 未覆盖：实际events、pixel/beam-spot/target/backing/PSA/rigidity calibration packet、执行nptool/FRESCO/OFT版本、所有相关covariance及PID confusion matrix。无真实L4重拟合。

## Paper Question and Scientific Motivation

将高粒子granularity、γ tracking与heavy-residue identification结合，开展inverse-kinematics direct reactions。对本轮Doppler问题，关键是light-particle measurement能否给emitter momentum、核素/反应道tag能排除哪些污染、以及新材料/触发会付出怎样的接受率代价。

## Method and Design Logic

Light ejectile energy/position + declared two-body channel→heavy-ion momentum；AGATA first-IP→lab photon direction；两者进入energy correction。VAMOS的heavy PID/rigidity/track另用于channel rejection和TOF重构；source与beam efficiency/normalization、材料和target-loss边界分别检查。

## Key Evidence and Reasoning Chain

Mechanical/pixel/clock calibration→lightparticle kinematics→same-line corrected-width comparison→heavyPID/entrypoint辅助→sourceefficiency与target/model/normalization限制。Three subsystems的互补信息仍共享beam/target/DAQ/selection，不能把一个triple-coincidence事件当三个独立实验。

## Summary

19O(d,p)20O的1.673-MeVline在meanβ=.126校正时10.2keVFWHM，light-particle两体重建后7.1keV；是实际particle-assisted Doppler benchmark。Rigidity/trajectory-based TOF也能改善PID，但需先选定integer A/q、处理path与clock。窄峰/强background suppression不提供未知absolute normalization或完整emission-history。

## Experimental or Theoretical Setup

MUGAST backward5trapezoids(2019)/7(2020)、annular及forwardMUST2；backward strips710/760μm、R13cm、geometry angular resolution<.4°。Detector/target pose以3D arm和mask测、reported precision.2mm。AGATA最多41crystals、约18cm；VAMOSzero-degree entrance73cm、4.6°acceptance。13页包含16Ocommissioning、19Othin-target和15Oα-transfer三个dataset，不混成一套statistics/geometry。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AS21-1 | 粒子strips/geometry提供<.4°angular resolution；3D arm/mask给detector/target相对pose、precision.2mm。α-source comparison按annular计数归一simulation，110°附近target-holder shadow尚有差异，不能只以nominalcoverage替实际efficiency。 | experimental-criterion | direct | PDF pp.3–4, Sec.2.1/Fig.2 | true |
| AS21-2 | 三套DAQ经ATS/VTS/AGAVA链接，MUGAST触发、VAMOSvalidated、AGATAtriggerless；500ns crystal coincidence、最大2μs系统匹配与typical1μs event-building各属不同stage。 | experimental-criterion | direct | PDF pp.4–6, Sec.3/Fig.4 | true |
| AS21-3 | 19O8AMeV+CD2 .3mg/cm²(3μm)数据给20O1.67-MeVstate missing-mass width179±4keV；target/straggling/beamspot是主要限制，不能把particle excitation-width直接当gamma width。 | experimental-fact | direct | PDF pp.6–7, Sec.4.2/Figs.7–8 | true |
| AS21-4 | nptool含target/straggling/beam spread/energy response，3μm得191keV；no beam spread得164keV。两者均为指定simulation输出，不是实测source宽度。 | model-result | direct | PDF p.7, Sec.4.2/Fig.8 | true |
| AS21-5 | 厚靶simulation profile非Gaussian，作者要求Gaussian与step的convolution并从half-height定义FWHM；分开target history、fit width与natural width。 | author-interpretation | direct | PDF p.7, Fig.8 and associated fit paragraph | true |
| AS21-6 | 41crystals、R182mm、Eu source1.4-MeVphotopeak效率4.9(1)%；邻晶Add-Back后7.1(1)%但lowenergy P/T变差。实际source geometry/algorithm定义保留。 | experimental-fact | direct | PDF pp.7–8, Sec.5.1/Fig.9 | true |
| AS21-7 | 比MUGAST39crystals/R182mm与plunger35/R233mm的transparency数据在1.4MeV归一；above200keV形状无additional absorption、100keV约10%更透明是该relative comparison，不是绝对efficiency或same-geometry控制。 | experimental-criterion | direct | PDF p.8, Sec.5.2/Fig.9bottom | true |
| AS21-8 | 19O(d,p)20O的1.673MeVline same acquisition/VAMOS20Otag下，两体重建heavy momentum（lightparticle energy/position）给FWHM7.1keV，对meanbeamβ.126的10.2keV；没有完整errors/covariance，不将difference写成新显著性或独立replication。 | experimental-fact | direct | PDF p.11, Sec.7.3/Fig.17 | true |
| AS21-9 | VAMOS A与A/q联合用于mass/charge分离；先identified integer A/q，再由Bρ计算β并用trajectory/path重构heavy TOF。精确integer假设不等于无PID误判，source未给本任务可复算confusionmatrix。 | experimental-criterion | direct | PDF pp.8–9, Figs.10–11; pp.11–12, Sec.7.4.2/Eq.(1) | true |
| AS21-10 | source称rigidity/path resolutions各.2%、reconstructed heavy TOF约800ps；light TOF结合MUGAST-VAMOS time，final1.4ns，约1ns electronics jitter限制；这些resolution的σ/FWHM convention未明示，不擅自变成Gaussianσ预算。 | experimental-fact | direct | PDF p.12, Eq.(1)/Fig.18/Conclusions | true |
| AS21-11 | 16Ocommissioning没有beam current监测，不能作absolute normalization；理论曲线rescale后g.s./s1/2 scaling ratio1.19(6)仅为model-conditioned relative spectroscopic-factor estimate。 | author-interpretation | direct | PDF pp.9–10, Sec.7.1/Fig.14 | true |
| AS21-12 | Particle Ex×γenergy与19Ne heavytag显示相同275-keVline可来自direct population或高位feeding；triple coincidence提供entrypoint/feeding信息，但不是直接证明完整τ或停止历史。 | experimental-fact | direct | PDF pp.10–11, Sec.7.2/Figs.15–16 | true |
| AS21-13 | High-intensityup to10⁸pps需要maskforwardMUST2和VAMOS focal-plane plate；trigger/rate、missingcoverage和未用beam tracking改变normalization/selection，不能拿nominalgeometry当所有runs。 | experimental-criterion | direct | PDF p.11, Sec.7.4.1 | true |
| AS21-14 | Sec.7.1在16O(d,p)17O commissioning段印1mg/cm² CH2；本文另写CD2作为d-target。该段targetlabel与d-channel的对应未核定，不静默改为CD2或以此断言实际反应错。 | synthesis | direct | PDF p.9, Sec.7.1; pp.3,6 | true |
| AS21-15 | Sec.7.2把4.140/4.197MeV两state间隔写51keV，而printedvalues之差为57keV，γ2632/2689keV也差57；原labels/文字保留，未以任务算术更正underlying ENSDF或placement。 | our-inference | indirect | PDF p.10, Sec.7.2; p.11, Fig.15inset | true |
| AS21-16 | 作者认为manufacturer给target厚度3±.5μm的不确定可能解释191keVsimulation与179±4keVmeasurement的部分差，未据此测定真实厚度或唯一选因。 | author-interpretation | direct | PDF p.7, Sec.4.2/Fig.8 | true |
| AS21-17 | Source报告19O(d,pγ)20O run有用于lifetime研究的Au backing；因此原拟用VAMOS精确target-loss/thickness测量未能完成。 | experimental-criterion | direct | PDF p.7, Sec.4.2, Au-backing paragraph | true |
| AS21-18 | Ref11 PLB811,135939的DOImetadata身份是17C single-particle论文，非20Odata；本轮仅核其bibliography，没有借它证明Au/20O history。 | synthesis | direct | PDF p.13, Ref11; Crossref DOI10.1016/j.physletb.2020.135939 identity lookup | true |

## Nuclear Structure Information

17O/20O/19Ne states是apparatus/spectroscopy benchmarks；本source不补新A≈130mode或absoluteB。DWBA/ADWA、relativefactor与γfeeding的证据层分开，未打开它们后续论文作为新课程卡。

## Authors' Interpretation

lightparticle measurements改善重离子recoil correction；heavyPID与triple coincidences有很强background rejection；target thickness、kinematic compression、clock/reference與材料geometry仍重要。Abstract“full rejection”保留为作者措辞，图谱强抑制不能无条件扩写为所有random/contaminants为零。

## Model Results

nptool用于geometry/target/straggling及efficiency；DWBA/ADWA曲线依potentials且rescaled到data，无absolutebeam normalization。All widths/profiles与comparison共享各run或同一simulation，非新增independentexperiment。

## Competing Interpretations and Limitations

- 两体heavy momentum依lightparticle、beam/target loss、channel与missingmass假设；如果有其它未测particle或emission/stop阶段，不能直接以post-reactionvector代所有γ。
- 20O数据Au backing明确存在，光子发射速度history仍需matchedpacket；width7.1不证明所有stopping项已消除。
- Rigidityβ是conditional on integer PID；wrong A/q会造成离散branch/systematic。Path/Bρ/clock共享covariance，不把两条路线当完全独立speed测量。
- sourceγefficiency与relative transparency比较不同geometry/crystal数，1.4MeV归一化会去掉绝对scale。
- AS21-14/15 target/energy间隔打印冲突及author-list版本差保留，actualproduction packet未取得。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AS21-AR1 | added momentum information | 10.2→7.1keV宽化改善是lightparticle+two-body vector的直接source evidence；不能独自分解speed/direction/response各占多少。 | AS21-8; [[doppler-correction]] | unreviewed |
| AS21-AR2 | discrete PID and covariance | Bρ连续error小不保证integer A/q正确；TOF subtraction需要shared covariance/clock convention。 | AS21-9/10; [[doppler-correction]] | unreviewed |
| AS21-AR3 | strength/absolute limit | triple tag/calibration/relative angular curve与absoluteB/absoluteSF归一化不同，commissioning明确缺absolute normalization。 | AS21-11/12 | unreviewed |

## Knowledge Impact and Learning Decision

`supports`除直接heavyvector外，light-ejectile二体重建可提供有意义速度信息；`limits`整数PID、漂亮窄峰、normalizedtransparency或triplecoincidence自动关闭全部nuisance的推断。Source只为实际matchedsetup验证，不代本run实验L4。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[doppler-correction]] | lightparticle recoil vector与rigidity/TOF/PID条件。 |
| methodological-bridge | [[tracking-array]] | geometry/material/trigger和add-back/track效率。 |
| methodological-bridge | [[gamma-gamma-coincidence]] | entrypoint/feeding与联合tag不等独立三样本。 |
| same-lineage | [[crespi-2023-agata-tracking-performance]] | C23 ancillary discussion引用本篇，重复citation不增实验数。 |
| methodological-bridge | [[vandebrouck-2016-vamos-dual-position-mwpc]] | directheavytrack与light-ejectile重建是不同信息路线，不迁移宽度。 |
| methodological-bridge | [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] | particle-based重建的beam/target/channel/coordinate依赖。 |

## Human Review Triage

P0：publiccopy身份/raw未归档与targetlabel冲突明确隔离。P1：AS21-7relative scale、AS21-8sameevents/width、AS21-9/10integer/clock、AS21-11normalization、AS21-14/15printedboundaries。Self-audit未提升human-reviewed。

## Reference-route identity follow-up

2026-10-14 Crossref查核Ref11 PLB811,135939 / DOI10.1016/j.physletb.2020.135939为17C single-particle论文，而非20O Au-backing数据；本轮只核metadata，未读其body，不将候选题名/同apparatus当20O直接证据。Ref27 PRC85,054318的19O(d,p)20O HELIOS身份另已核，仅可作不同apparatus候选。

## Extracted Pages

PDF1–13全文主线；corepp.3–9及11–12的原figure/式。Actualevent/basis/PID/target backingmanifest仍缺失。
