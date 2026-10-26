---
type: experiment
title: "AFRODITE 133Ce experiment"
aliases: [125Te(12C,4n)133Ce AFRODITE]
created: 2026-07-01
updated: 2026-07-01
status: active
review_status: unreviewed
experiment_id: afrodite-133ce-c12-57mev
facility: iThemba LABS separated-sector cyclotron
beam: 12C
target: 125Te
beam_energy: 57 MeV
reaction: 125Te(12C,4n)133Ce
evaporation_channel: 4n
residual_nuclei: [133ce]
detector_array: AFRODITE
data_status: published
sources: [ding-2021-131ba-133ce-signature-splitting]
tags: [fusion-evaporation, afrodite, signature-splitting, a130]
---

# AFRODITE `133Ce` 实验

## Identity

用于补全 `133Ce` band 2 两支 signature 序列的 γ 谱学数据集。

## Beam, Target and Reaction

- 57 MeV、5 pnA `12C`；
- 2 mg/cm²、95.3% enriched `125Te`；
- 8 mg/cm² Au backing；
- `125Te(12C,4n)133Ce`。

## Detector Configuration

AFRODITE 8 个 Compton-suppressed clover，90° 和 135° 各四个。

## Trigger and Coincidence Conditions

记录 `2.8×10^10` 个双符合及 `5.4×10^9` 个三重及以上 coincidence events。

## Data Products

二维、三维 γ 符合矩阵；`R_ac` 标定约为 stretched quadrupole 1.27、stretched dipole 0.74。

## Nuclei and Bands Studied

[[133ce]]，重点为 [[133ce-band-2]]。

## Known Limitations

阵列角度数少于 GALILEO；弱线多极性判断依赖本实验自己的 `R_ac` 标定。

## Sources

- [[ding-2021-131ba-133ce-signature-splitting]]

## Evolution Log

- 2026-07-01：由 2021 signature-splitting 论文建立。


## Day23：装置描述冲突须回run ledger

[[ding-2021-131ba-133ce-signature-splitting]] D21-D23-064-1的稿本/正式版均报告8clovers=4@90°+4@135°；[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] WK22-31的具体实验段报告13=1@45°+8@90°+4@135°。束流/靶/总事件字段相同，强同源候选不重复计实验票；不能据此裁定actual配置。后续需要run dates/ID、active detectors、45°event存在性和sorting geometry/目标线角门，不补造response；新needs_review:true，旧人审/claims保留。
