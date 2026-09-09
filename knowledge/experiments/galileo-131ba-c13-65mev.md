---
type: experiment
title: "GALILEO 131Ba experiment"
aliases: [122Sn(13C,4n)131Ba GALILEO]
created: 2026-07-01
updated: 2026-08-11
status: active
review_status: unreviewed
experiment_id: galileo-131ba-c13-65mev
facility: Laboratori Nazionali di Legnaro XTU Tandem
beam: 13C
target: 122Sn
beam_energy: 65 MeV
reaction: 122Sn(13C,4n)131Ba
evaporation_channel: 4n
residual_nuclei: [131ba]
detector_array: GALILEO + EUCLIDES + Neutron Wall
data_status: published
sources: [guo-2020-pseudospin-chiral-quartet-131ba, ding-2021-131ba-133ce-signature-splitting]
tags: [fusion-evaporation, galileo, signature-splitting, a130, nuclear-chirality, octupole-correlation]
---

# GALILEO `131Ba` 实验

## Identity

用于建立 `131Ba` 高自旋 D3-D8 六带流形及后来正宇称 band 2 的 fusion-evaporation γ 谱学数据集。

## Beam, Target and Reaction

- 65 MeV、5 pnA `13C`；
- 两层各 0.5 mg/cm² self-supporting `122Sn`；
- `122Sn(13C,4n)131Ba`。

## Detector Configuration

GALILEO 25 个 Compton-suppressed HPGe，分布于 90°、119°、129°、152°；EUCLIDES silicon ball 与 Neutron Wall 用于反应道区分。

## Trigger and Coincidence Conditions

记录 `1.2×10^9` 个三重及以上 events。

## Data Products

Doppler 校正后的 γγγ cube；RADWARE/GASPware；90°/152° 的 `R_ac`，实验标定约为 stretched quadrupole 1.5-1.54、stretched dipole 0.77-0.8。Guo 2020 Fig.3 的 `R_ac` 估计采用 `σ/I=0.24`，并以四角 angular distributions 提取多数 M1/E2 mixing ratios。

## Nuclei and Bands Studied

[[131ba]]；Guo 2020 重点为 [[131ba-positive-parity-pseudospin-chiral-quartet]] 与 [[131ba-negative-parity-chiral-doublet-candidate]]，D4/D8 为新带；Ding 2021 重点为 [[131ba-band-2]]。

## Known Limitations

经验 `R_ac` 标定只适用于该阵列和排序；不能直接套用到 AFRODITE 或其他实验。

Guo 2020 把完整数据分析细节指向 Ref.27；其正文没有逐条列出所有 mixing ratios，且少数弱带内跃迁采用 `δ=-0.2(1)`。

## Sources

- [[guo-2020-pseudospin-chiral-quartet-131ba]]
- [[ding-2021-131ba-133ce-signature-splitting]]
- [[qiang-2019-high-spin-130-131ba-87zr]]

## Evolution Log

- 2026-07-01：由 2021 signature-splitting 论文建立。
- 2026-08-11：on-touch 前移 Guo 2020 原始六带用途、`R_ac`/angular-distribution 条件和弱线 assumed-δ 边界。
- 2026-09-05：接入 Qiang 2019 thesis；保留其与本实验 journal sources 的 multiple-dependent 关系。
