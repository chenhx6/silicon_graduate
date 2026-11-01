---
type: experiment
title: VECC 38 MeV α 束 ¹³¹Xe 实验
aliases: [130Te alpha 3n 131Xe, VECC 131Xe INGA experiment]
created: 2026-07-01
updated: 2026-07-01
status: active
review_status: unreviewed
experiment_id: vecc-131xe-alpha-38mev
facility: VECC K-130 cyclotron
beam: 4He
target: 130Te
beam_energy: 38 MeV
reaction: 130Te(4He,3n gamma)131Xe
evaporation_channel: 3n
residual_nuclei: [131xe]
detector_array: INGA 7 Compton-suppressed clover HPGe
data_status: reanalyzed-existing-dataset
sources: [banik-2020-131xe-multiple-band-structures, chakraborty-2023-131xe-wobbling-origin, jehangir-2022-odd-neutron-tpsm-extension]
tags: [fusion-evaporation, in-beam-gamma, INGA]
---

# VECC 38 MeV α 束 `131Xe` 实验

## Identity

在 VECC K-130 回旋加速器利用 `130Te(4He,3nγ)131Xe` 布居 `131Xe` 中高自旋态。2023 论文重新分析了先前数据集。

## Beam, Target and Reaction

- α 束能量：38 MeV；
- 靶：2 mg/cm² enriched `130Te`；
- backing：600 µg/cm² Mylar；
- 蒸发道：3n；
- 余核：`131Xe`。

## Detector Configuration

7 个 Compton-suppressed clover HPGe，位于相对束流 40°、90°、125°。

## Trigger and Coincidence Conditions

Pixie-16 250 MHz、12 bit 数字 DAQ，记录带时间戳的 singles/coincidence events。

## Data Products

使用 IUCPIX 构造对称/非对称矩阵，INGASORT 与 RADWARE 进行离线分析；产生符合谱、DCO、偏振和能级纲图。

## Nuclei and Bands Studied

- [[131xe]]
- [[131xe-nu-h11-2-favored-sequence]]
- [[131xe-negative-parity-yrare-sequence]]
- [[131xe-negative-parity-yrast-13-2-sequence]]


## Acquisition Lineage and Dependent Analyses

本实验（`vecc-131xe-inga-38mev-130te-a3n`）对应在加尔各答 VECC K-130 回旋加速器上使用 7 个 Compton-suppressed clover HPGe 探测器完成的单次物理采集（`independent_experiment_count: 1`）。该实验后续产生了三篇关键文献：

1. **Banik et al. (2020)** (*Phys. Rev. C* 101, 044306)：首次系统报道该实验的能级纲图扩展（72 条新跃迁）、DCO 与偏振分析，建立了 Bands 1–7 的框架（`lineage_role: primary-analysis`）。
2. **Jehangir et al. (2022)** (*Phys. Rev. C* 105, 054310)：将奇中子 TPSM 扩展到五准粒子基底，其 131Xe 能谱比较直接沿用 Banik 2020 Ref. [53] 数据（`lineage_role: dependent-theory-comparison`）。
3. **Chakraborty et al. (2023)** (*Phys. Rev. C* 107, 064318)：使用相同的原始 INGA 数据集重新构建符合矩阵，对低自旋区进行精细分析，提出负宇称 yrare 带为 signature partner 而非 wobbling 带（`lineage_role: dependent-reanalysis`）。

三篇文献共享同一套束流能量（38 MeV α）、靶厚（2 mg/cm² 130Te）、探测器角度排布（40°, 90°, 125°）和 Pixie-16 数字 DAQ 采集事件，不能在综合分析中按三套独立实验赋予统计权重。
## Known Limitations

- 只有三个主要角度组；
- 弱连接跃迁偏振误差较大；
- 多项已知跃迁强度和偏振取自更早 Ref.[22]，需独立摄入后区分本次新结果与沿用数据。

## Sources

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[banik-2020-131xe-multiple-band-structures]] — earlier analysis of the same INGA acquisition lineage.

## Evolution Log

- 2026-07-01：由 2023 论文实验章节建立。

