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
sources: [chakraborty-2023-131xe-wobbling-origin]
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

## Known Limitations

- 只有三个主要角度组；
- 弱连接跃迁偏振误差较大；
- 多项已知跃迁强度和偏振取自更早 Ref.[22]，需独立摄入后区分本次新结果与沿用数据。

## Sources

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[banik-2020-131xe-multiple-band-structures]] — earlier analysis of the same INGA acquisition lineage.

## Evolution Log

- 2026-07-01：由 2023 论文实验章节建立。

